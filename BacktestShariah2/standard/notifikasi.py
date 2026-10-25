# Satu baris notifikasi telefon (< 200 aksara) daripada papertrade/status_harian.json selepas kerja GitHub Actions
# (permintaan pengguna 24 Okt 2026: notifikasi kerja papertrade sahaja, mula selepas peralihan). Dipakai oleh
# jadual/tolak_db.md (bahagian A selepas harian.yml + lejar.yml + analisis.yml; bahagian B selepas beli.yml) dan
# jadual/notifikasi_harian.md. Tanpa rangkaian: senarai workflow gagal diberi oleh sesi Claude (--gagal).
# "Kalau tak beli, cakap tak beli."
#
# Sejak 25 Okt 2026 (audit operasi item 6; jadual/CADANGAN_JADUAL.md):
#   --amaran  tambah "AMARAN: …" jika data luar tidak dikemas kini (umur > had): SST (penyambung mati sejak 19 Okt 2026
#             tanpa amaran), EDGAR (edgar.yml tidak menulis apa-apa tanpa rahsia SEC_USER_AGENT), kalendar earnings Nasdaq.
#   --db F    dokumen db dalam folder output `jana_db.py --keluar F` yang >= 80% had 262,144 bait (atau melebihi had dan
#             dilangkau jana_db.py, daripada F/ringkas.json) -> "db ≥80%: …".
#   sedia     kesediaan tolakan db: --untuk malam = harian.yml + lejar.yml + analisis.yml sudah memproses sesi dijangka;
#             --untuk beli = beli.yml sudah merekod belian hari ini (NY). Cetak satu baris JSON; kod keluar 0 = siap,
#             3 = belum (medan `tembak` = workflow yang boleh ditembak sekali jika tiada larian queued/in_progress).
#
# Guna:
#   python3 notifikasi.py malam [--folder F] [--gagal harian.yml,lejar.yml] [--masa "YYYY-MM-DD HH:MM"] [--tambah TEKS]
#                               [--amaran] [--db FOLDER_DB] [--akar BacktestShariah2]
#   python3 notifikasi.py beli  [… sama]
#   python3 notifikasi.py sedia [--untuk malam|beli] [--folder F] [--masa …] [--akar …]
# --masa dalam UTC (lalai: sekarang). --folder lalai: papertrade/ (MOD_ACTIONS rasmi) atau bayang/papertrade/ (bayang).
import argparse, csv, glob, json, os, re, sys
from datetime import date
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
BS2 = os.path.dirname(HERE)
FOLDER = os.path.join(BS2, 'papertrade')
HAD = 199
HAD_SST_HARI = 8          # SST dikumpul mingguan (jadual/mingguan.md, Ahad): > 8 hari kalendar = terlepas satu minggu
HAD_EDGAR_SESI = 2        # edgar.yml setiap malam hari kerja (+ sandaran pagi): > 2 sesi di belakang sesi dijangka
HAD_KALENDAR_SESI = 2     # kalendar earnings Nasdaq (pemangkin.yml) setiap hari dagangan: > 2 sesi di belakang
AMARAN_DB = 0.8           # sama dengan jana_db.AMARAN_HAD
HAD_DB = 262144           # sama dengan bahagi_db.HAD_DB (had keras dokumen db dashboard)
DATE_RE = re.compile(r'(\d{4})-?(\d{2})-?(\d{2})')


def kal():
    import exchange_calendars as xc
    return xc.get_calendar('XNYS')


def baca_json(p):
    try:
        with open(p, encoding='utf-8') as f:
            return json.load(f)
    except (OSError, ValueError):
        return None


def tarikh(x):
    """'2026-10-23', '20261023', '2026-10-23 12:21 UTC' -> date, atau None."""
    m = DATE_RE.match(str(x or '').strip())
    if not m:
        return None
    try:
        return date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
    except ValueError:
        return None


def folder_lalai(akar):
    try:
        mod = open(os.path.join(akar, 'MOD_ACTIONS')).read().strip()
    except OSError:
        mod = 'rasmi'
    return os.path.join(akar, 'bayang', 'papertrade') if mod == 'bayang' else os.path.join(akar, 'papertrade')


def sesi_jangka(kini):
    """Sesi NYSE terakhir sebelum tarikh MYT hari ini (harian.yml memproses sesi AS semalam)."""
    c = kal()
    hari = kini.tz_convert('Asia/Kuala_Lumpur').tz_localize(None).normalize()
    return str(c.sessions_in_range(hari - pd.Timedelta(days=10), hari - pd.Timedelta(days=1))[-1].date())


def sesi_di_belakang(d, S):
    """Bilangan sesi NYSE selepas tarikh d hingga S (inklusif); 0 jika d >= S."""
    S = date.fromisoformat(S)
    if d >= S:
        return 0
    return len(kal().sessions_in_range(pd.Timestamp(d) + pd.Timedelta(days=1), pd.Timestamp(S)))


def ringkas(teks, gagal, tambah, amaran=''):
    bah = [teks]
    if gagal:
        bah.append('GAGAL: ' + ', '.join(gagal))
    if amaran:
        bah.append(amaran)
    if tambah:
        bah.append(tambah)
    s = ' | '.join(bah)
    return s if len(s) <= HAD else s[:HAD - 1] + '…'


# ---------------------------------------------------------------- amaran data luar dan saiz db
def tarikh_sst(akar):
    """Tarikh data SST terkini dalam repo: papertrade/sektor.csv (rutin 6:02), data/db/sektor_snapshot.json
    (sst_tarikh / sst_tarikh_kumpulan; mingguan), data/sst/*.json dan data/pemangkin/market_events.json (mingguan)."""
    calon = []
    p = os.path.join(akar, 'papertrade', 'sektor.csv')
    if os.path.exists(p):
        with open(p, newline='', encoding='utf-8') as f:
            calon += [tarikh(r.get('tarikh')) for r in csv.DictReader(f)]
    sn = baca_json(os.path.join(akar, 'data', 'db', 'sektor_snapshot.json')) or {}
    calon += [tarikh(sn.get('sst_tarikh')), tarikh(sn.get('sst_tarikh_kumpulan'))]
    for p in glob.glob(os.path.join(akar, 'data', 'sst', '*.json')) + [os.path.join(akar, 'data', 'pemangkin', 'market_events.json')]:
        d = baca_json(p)
        if isinstance(d, dict):
            calon += [tarikh(d.get(k)) for k in ('tarikh', 'sesi', 'dijana')]
        m = DATE_RE.search(os.path.basename(p))
        if m:
            calon.append(tarikh(m.group(0)))
    calon = [d for d in calon if d]
    return max(calon) if calon else None


def tarikh_edgar(akar):
    st = baca_json(os.path.join(akar, 'data', 'edgar', 'status.json'))
    return None if not isinstance(st, dict) else tarikh(st.get('hari_terakhir'))


def tarikh_kalendar(akar):
    calon = []
    for p in ('earnings_nasdaq.json', 'status.json'):
        d = baca_json(os.path.join(akar, 'data', 'pemangkin', p))
        if isinstance(d, dict):
            calon += [tarikh(d.get('tarikh')), tarikh(d.get('nasdaq_tarikh'))]
    calon = [d for d in calon if d]
    return max(calon) if calon else None


def amaran_data(akar, kini, S=None):
    """['SST 9 hari', 'EDGAR tidak aktif', …] bagi sumber yang umurnya melebihi had (ringkas: baris < 200 aksara)."""
    S = S or sesi_jangka(kini)
    hari = kini.tz_convert('Asia/Kuala_Lumpur').date()
    out = []
    d = tarikh_sst(akar)
    if d is None:
        out.append('SST tiada data')
    elif (hari - d).days > HAD_SST_HARI:
        out.append(f'SST {(hari - d).days} hari')
    d = tarikh_edgar(akar)
    if d is None:
        out.append('EDGAR tidak aktif')   # tiada data/edgar/status.json: rahsia SEC_USER_AGENT belum ditetapkan
    elif sesi_di_belakang(d, S) > HAD_EDGAR_SESI:
        out.append(f'EDGAR {sesi_di_belakang(d, S)} sesi')
    d = tarikh_kalendar(akar)
    if d is None:
        out.append('kalendar tiada')
    elif sesi_di_belakang(d, S) > HAD_KALENDAR_SESI:
        out.append(f'kalendar {sesi_di_belakang(d, S)} sesi')
    return out


def amaran_db(folder):
    """Dokumen db (folder output jana_db.py --keluar) >= AMARAN_DB x HAD_DB, susun menurun; dokumen yang melebihi had
    dilangkau jana_db.py dan hanya tercatat dalam ringkas.json. -> ['papertrade/claude_9 LEBIH had', 'prestasi/mae 91%']"""
    if not folder or not os.path.isdir(folder):
        return []
    saiz = []
    for p in glob.glob(os.path.join(folder, '*', '*.json')):
        sz = os.path.getsize(p)
        if sz >= AMARAN_DB * HAD_DB:
            kol = os.path.basename(os.path.dirname(p))
            saiz.append((sz, f'{kol}/{os.path.basename(p)[:-5]} {sz / HAD_DB:.0%}'))
    lebih = []
    for r in (baca_json(os.path.join(folder, 'ringkas.json')) or {}).get('ralat') or []:
        m = re.match(r'^(\S+): \d+ bait melebihi had db', str(r))
        if m:
            lebih.append(f'{m.group(1)} LEBIH had')
    return lebih + [t for _, t in sorted(saiz, reverse=True)]


def teks_amaran(data, db):
    bah = []
    if data:
        bah.append(', '.join(data))
    if db:
        bah.append('db≥80% ' + ', '.join(db[:3]) + (f' +{len(db) - 3}' if len(db) > 3 else ''))
    return ('AMARAN: ' + '; '.join(bah)) if bah else ''


# ---------------------------------------------------------------- baris notifikasi
def baris_malam(st, kini):
    """Sesi dijangka = sesi NYSE terakhir sebelum tarikh MYT hari ini (harian.yml memproses sesi AS semalam)."""
    c = kal()
    S = sesi_jangka(kini)
    m = st.get('malam') or {}
    if m.get('sesi') != S:
        return f"Harian {S} BELUM siap (sesi terakhir diproses: {m.get('sesi') or '-'}); semak harian.yml"
    kj = m.get('keluar_baru_jumlah') or {}
    kc = (m.get('keluar_baru') or {}).get('C') or {}
    jenis = ', '.join(f'{k} {v}' for k, v in sorted(kc.items()) if v)
    seterus = str(c.next_session(pd.Timestamp(S)).date())
    td = len(m.get('tidak_dibeli') or [])
    return (f"Harian {S}: keluar C {kj.get('C', 0)}" + (f' ({jenis})' if jenis else '') + f", M {kj.get('M', 0)}; "
            f"menunggu {m.get('menunggu', 0)}" + (f'; tidak sah {td}' if td else '') +
            f"; senarai beli {m.get('senarai_beli', 0)} ({m.get('saham_unik', 0)} saham) untuk {seterus}")


def baris_beli(st, kini):
    D = str(kini.tz_convert('America/New_York').date())
    if not kal().is_session(pd.Timestamp(D)):
        return f'Tak beli {D}: pasaran AS tutup'
    b = st.get('beli') or {}
    if b.get('tarikh') != D:
        return f"Tak beli {D} (belum direkod; belian terakhir {b.get('tarikh') or '-'}); semak beli.yml"
    if not b.get('direkod'):
        return f"Tak beli {D}: {b.get('nota') or 'tiada calon lulus'}"
    lw = len(b.get('buka_lewat') or [])
    return (f"Beli {D}: {b['direkod']} direkod ({b.get('saham_unik', 0)} saham), {b.get('dilangkau', 0)} dilangkau"
            + (f', {lw} buka lewat' if lw else '') + f"; {b.get('sumber_buka', '')}").rstrip('; ')


# ---------------------------------------------------------------- kesediaan tolakan db
def sedia(untuk, st, akar, kini):
    """Kesediaan tolakan db (jadual/tolak_db.md). malam: harian.yml (status_harian.malam.sesi), lejar.yml
    (lejar/status.json sesi_terakhir) dan analisis.yml (data/analisis/papan.json kini) bagi sesi dijangka; beli:
    status_harian.beli.tarikh = hari ini NY (hari bukan sesi = cuti, tiada belian dijangka)."""
    if untuk == 'beli':
        ny = kini.tz_convert('America/New_York'); D = str(ny.date())
        if not kal().is_session(pd.Timestamp(D)):
            return dict(untuk='beli', jangka=D, cuti=True, siap=True, belum=[], tembak=[])
        b = (st.get('beli') or {}).get('tarikh') or ''
        belum = [] if b == D else ['beli.yml']
        awal = ny.hour * 60 + ny.minute < 9 * 60 + 31
        return dict(untuk='beli', jangka=D, beli=b, cuti=False, siap=not belum, belum=belum,
                    tembak=[] if awal else list(belum), nota='sebelum gerbang 9:31 NY' if awal and belum else '')
    S = sesi_jangka(kini)
    h = (st.get('malam') or {}).get('sesi') or ''
    l = (baca_json(os.path.join(akar, 'lejar', 'status.json')) or {}).get('sesi_terakhir') or ''
    pp = baca_json(os.path.join(akar, 'data', 'analisis', 'papan.json')) or {}
    a = str(pp.get('lejar_sesi') or pp.get('kini') or '')[:10]
    belum = [w for w, v in (('harian.yml', h), ('lejar.yml', l), ('analisis.yml', a)) if v < S]
    tembak = [w for w in belum if w != 'analisis.yml'] + (['analisis.yml'] if 'analisis.yml' in belum and l >= S else [])
    return dict(untuk='malam', jangka=S, harian=h, lejar=l, analisis=a, siap=not belum, belum=belum, tembak=tembak)


def main(argv=None):
    ap = argparse.ArgumentParser(description='Baris notifikasi kerja papertrade GitHub Actions')
    ap.add_argument('peringkat', choices=['malam', 'beli', 'sedia'])
    ap.add_argument('--folder', default=None, help='folder status_harian.json (lalai ikut MOD_ACTIONS)')
    ap.add_argument('--akar', default=BS2, help='folder BacktestShariah2 (data/, lejar/, MOD_ACTIONS)')
    ap.add_argument('--gagal', default='', help='nama fail workflow gagal, dipisah koma')
    ap.add_argument('--masa', default=None, help='UTC "YYYY-MM-DD HH:MM" (ujian)')
    ap.add_argument('--tambah', default='')
    ap.add_argument('--amaran', action='store_true', help='tambah amaran SST/EDGAR/kalendar yang tidak dikemas kini')
    ap.add_argument('--db', default=None, help='folder output jana_db.py --keluar (amaran dokumen >= 80% had)')
    ap.add_argument('--untuk', choices=['malam', 'beli'], default='malam', help='sedia: tolakan A (malam) atau B (beli)')
    a = ap.parse_args(argv)
    folder = a.folder or folder_lalai(a.akar)
    st = baca_json(os.path.join(folder, 'status_harian.json')) or {}
    kini = pd.Timestamp(a.masa, tz='UTC') if a.masa else pd.Timestamp.now(tz='UTC')
    if a.peringkat == 'sedia':
        r = sedia(a.untuk, st, a.akar, kini)
        print(json.dumps(r, ensure_ascii=False))
        return 0 if r['siap'] else 3
    teks = (baris_malam if a.peringkat == 'malam' else baris_beli)(st, kini)
    am = teks_amaran(amaran_data(a.akar, kini) if a.amaran else [], amaran_db(a.db))
    print(ringkas(teks, [g.strip() for g in a.gagal.split(',') if g.strip()], a.tambah.strip(), am))
    return 0


if __name__ == '__main__':
    sys.exit(main())
