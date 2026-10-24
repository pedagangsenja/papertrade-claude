# Sampel rawak posisi Papertrade C lawan kline harian Moomoo (lapisan 3 jaminan data, 24 Okt 2026). Rutin 6:02 MYT memilih
# sampel berketentuan daripada sesi terakhir, mengambil kline harian Moomoo (alat baca sahaja quote_history_kline, autype 0
# = tanpa pelarasan) dan membanding nilai CSV dengan bar rasmi. Sumber kedua yang bebas daripada yfinance/stor repo: kesilapan
# seperti DAC M80/M90 (beli 164.162 lawan buka rasmi 170.19) dikesan pada pagi yang sama. Tiada order; tiada tulisan ke CSV.
#
#   python3 BacktestShariah2/standard/sampel_semak.py pilih [--n 15] [--tarikh YYYY-MM-DD] [--folder PT] [--keluar F.json]
#       -> JSON {"tarikh", "n", "posisi": [...], "ambil": [{"saham", "simbol", "mula", "akhir", "num"}]} ke stdout.
#          Campuran (cincangan sha1 tarikh|kunci; sama setiap kali bagi data sama): ~1/3 belian baharu sesi itu (separuh
#          daripada saham tanpa bar sesi itu dalam terkini.csv, iaitu tanpa sumber kedua), ~1/3 keluar baharu (lorong 1 dan
#          lorong 2 bertarikh sesi itu), selebihnya posisi terbuka rawak. Kekurangan satu kumpulan diisi kumpulan lain.
#   python3 BacktestShariah2/standard/sampel_semak.py banding <kline.csv> [--pilih F.json] [--tarikh D] [--n 15]
#           [--keluar data/semakan/sampel.json]
#       kline.csv: saham,tarikh,buka,tinggi,rendah,tutup (saham dengan/tanpa 'US.'; tarikh YYYY-MM-DD atau YYYYMMDD).
#       Tanpa --pilih, sampel dipilih semula dengan peraturan sama (CSV tidak boleh berubah antara pilih dan banding).
#       Semakan (toleransi 0.3%): harga_beli = buka hari beli; harga_keluar = buka (buka bawah henti / buka atas sasaran /
#       isyarat keluar jual pada buka) atau tutup (had masa, isyarat palsu ambil alih, delist) hari keluar; kena henti dalam
#       hari: rendah <= harga_keluar dan buka >= harga_keluar; capai sasaran dalam hari: tinggi >= harga_keluar dan buka <=
#       harga_keluar; harga_keluar_henti = buka hari keluar lorong 2 (tutup bagi keluar paksa); harga_terkini posisi terbuka =
#       tutup sesi. Tulis {"tarikh", "dibina", "status": "ok"|"beza"|"belum", "n", "n_beza", "beza": [{"saham", "kaedah",
#       "tarikh_beli", "medan", "csv", "moomoo"}], "n_pilih", "tiada_kline"}. Kod keluar 1 jika ada beza, 2 jika fail kline
#       tidak sah.
import argparse, csv, hashlib, json, os, re, sys
from datetime import date, datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
BS2 = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import sahkan as SH  # noqa: E402

PT = os.path.join(BS2, 'papertrade')
TERKINI = os.path.join(BS2, 'data', 'harga', 'terkini.csv')
KELUAR = os.path.join(BS2, 'data', 'semakan', 'sampel.json')
TOL = 0.003
N_LALAI = 15


# ---------------------------------------------------------------- pilih
def baca_c(folder):
    """[(fail, baris, r)] semua posisi dibeli Papertrade C (claude*.csv)."""
    out = []
    for p in SH.fail_posisi_dalam(folder)[1:]:
        if os.path.exists(p):
            for i, r in enumerate(SH.baca(p)[1], start=2):
                if SH.dibeli(r):
                    out.append((os.path.basename(p), i, r))
    return out


def sesi_akhir(posisi):
    return max((r.get(k) or '' for _, _, r in posisi for k in ('tarikh_beli', 'tarikh_keluar', 'tarikh_keluar_henti')
                if SH.TARIKH.match(r.get(k) or '')), default='')


def cincang(D, x):
    f, _, r = x
    return hashlib.sha1(f'{D}|{f}|{r["saham"]}|{r["kaedah"]}|{r["tarikh_beli"]}'.encode()).hexdigest()


def bar_yf(terkini, D):
    """Set saham yang ada bar sesi D dalam terkini.csv (sumber kedua bagi belian sesi itu)."""
    if not terkini or not os.path.exists(terkini):
        return set()
    d = D.replace('-', '')
    with open(terkini, newline='', encoding='utf-8') as f:
        return {r['ticker'] for r in csv.DictReader(f) if str(r.get('date')) == d}


def ambil_dari(calon, q, dipilih, D, saham_ada=None):
    """Ambil q posisi daripada calon (susunan cincangan), utamakan saham yang belum dipilih; langkau posisi sudah dipilih."""
    calon = sorted(calon, key=lambda x: cincang(D, x))
    kunci = lambda x: (x[0], x[1])
    sudah = {kunci(x) for x in dipilih}
    saham = {x[2]['saham'] for x in dipilih} if saham_ada is None else saham_ada
    out = []
    for lulus in (0, 1):
        for x in calon:
            if len(out) >= q:
                return out
            if kunci(x) in sudah or (lulus == 0 and x[2]['saham'] in saham):
                continue
            out.append(x); sudah.add(kunci(x)); saham.add(x[2]['saham'])
    return out


def jenis_keluar(teks):
    """Jenis harga keluar lorong 1 daripada isyarat_keluar: 'buka' | 'tutup' | 'henti' | 'sasaran' | None."""
    s = (teks or '').lower()
    if 'isyarat palsu' in s or 'delist' in s or 'had masa' in s:
        return 'tutup'
    if 'buka bawah henti' in s or 'buka atas sasaran' in s or 'isyarat keluar' in s or 'jual pada buka' in s:
        return 'buka'
    if 'henti' in s:
        return 'henti'
    if 'sasaran' in s:
        return 'sasaran'
    return None


def butiran(x, D, kumpulan):
    f, i, r = x
    perlu = {r['tarikh_beli']}
    d = dict(kumpulan=kumpulan, fail=f, baris=i, saham=r['saham'], kaedah=r['kaedah'], tarikh_beli=r['tarikh_beli'],
             harga_beli=r['harga_beli'], nota_beli='buka sementara' if 'buka sementara' in (r.get('nota') or '') else '')
    if SH.benar(r.get('keluar')):
        d.update(tarikh_keluar=r.get('tarikh_keluar', ''), harga_keluar=r.get('harga_keluar', ''), henti=r.get('henti', ''),
                 isyarat_keluar=r.get('isyarat_keluar', ''), jenis_keluar=jenis_keluar(r.get('isyarat_keluar')))
        if SH.TARIKH.match(r.get('tarikh_keluar') or ''):
            perlu.add(r['tarikh_keluar'])
    else:
        d.update(harga_terkini=r.get('harga_terkini', ''), sesi=D)
        perlu.add(D)
    if SH.benar(r.get('keluar_henti')):
        st = r.get('status_henti') or ''
        d.update(tarikh_keluar_henti=r.get('tarikh_keluar_henti', ''), harga_keluar_henti=r.get('harga_keluar_henti', ''),
                 jenis_keluar_henti='tutup' if st.startswith(('Keluar: isyarat palsu', 'Keluar: delist')) else 'buka')
        if SH.TARIKH.match(r.get('tarikh_keluar_henti') or ''):
            perlu.add(r['tarikh_keluar_henti'])
    d['kline_tarikh'] = sorted(t for t in perlu if t <= D)
    return d


def pilih(folder=PT, n=N_LALAI, D=None, terkini=TERKINI):
    posisi = baca_c(folder)
    D = D or sesi_akhir(posisi)
    if not D or not posisi:
        return dict(tarikh=D or '', n=0, posisi=[], ambil=[])
    beli = [x for x in posisi if x[2]['tarikh_beli'] == D]
    k1 = [x for x in posisi if SH.benar(x[2].get('keluar')) and x[2].get('tarikh_keluar') == D]
    k2 = [x for x in posisi if SH.benar(x[2].get('keluar_henti')) and x[2].get('tarikh_keluar_henti') == D]
    buka = [x for x in posisi if SH.dipegang(x[2]) and not SH.benar(x[2].get('keluar')) and x[2]['tarikh_beli'] < D]
    qb = n // 3; qk = n // 3; qt = n - qb - qk
    dipilih = []
    yf = bar_yf(terkini, D)
    tanpa = [x for x in beli if x[2]['saham'] not in yf]
    q0 = min(len(tanpa), (qb + 1) // 2) if yf else 0
    g = [(x, 'beli_baru') for x in ambil_dari(tanpa, q0, dipilih, D)]
    dipilih += [x for x, _ in g]
    g += [(x, 'beli_baru') for x in ambil_dari(beli, qb - len(g), dipilih, D)]
    dipilih = [x for x, _ in g]
    q2 = (min(len(k2), max(1, qk // 2)) if k1 else min(len(k2), qk)) if qk else 0   # lorong 2 sekurang-kurangnya 1
    for calon, q, nm in ((k2, q2, 'keluar_lorong2'), (k1, qk - q2, 'keluar_lorong1'), (buka, qt, 'terbuka')):
        a = ambil_dari(calon, q, dipilih, D)
        g += [(x, nm) for x in a]; dipilih += a
    for calon, nm in ((buka, 'terbuka'), (k1, 'keluar_lorong1'), (k2, 'keluar_lorong2'), (beli, 'beli_baru')):
        if len(g) >= n:
            break
        a = ambil_dari(calon, n - len(g), dipilih, D)
        g += [(x, nm) for x in a]; dipilih += a
    out = [butiran(x, D, nm) for x, nm in g[:n]]
    ambil = {}
    for d in out:
        a = ambil.setdefault(d['saham'], set()); a.update(d['kline_tarikh'])
    pelan = []
    for t in sorted(ambil):
        ts = sorted(ambil[t])
        hari = (date.fromisoformat(ts[-1]) - date.fromisoformat(ts[0])).days
        pelan.append(dict(saham=t, simbol=f'US.{t}', mula=ts[0], akhir=ts[-1], num=min(370, hari + 2), tarikh=ts))
    return dict(tarikh=D, n=len(out), posisi=out, ambil=pelan,
                arahan='quote_history_kline: symbol, start=mula, end=akhir, ktype 2, autype 0 (tanpa pelarasan); simpan '
                       'CSV saham,tarikh,buka,tinggi,rendah,tutup; kemudian: sampel_semak.py banding <kline.csv>')


# ---------------------------------------------------------------- banding
def baca_kline(path):
    """{(saham, 'YYYY-MM-DD'): dict(buka, tinggi, rendah, tutup)}; ValueError jika lajur tiada."""
    K = {}
    with open(path, newline='', encoding='utf-8') as f:
        rd = csv.DictReader(f)
        lajur = [c.strip().lower() for c in (rd.fieldnames or [])]
        perlu = ['saham', 'tarikh', 'buka', 'tinggi', 'rendah', 'tutup']
        if any(c not in lajur for c in perlu):
            raise ValueError(f'lajur kline mesti {",".join(perlu)} (dapat {",".join(lajur)})')
        for r in rd:
            r = {k.strip().lower(): (v or '').strip() for k, v in r.items() if k}
            t = re.sub(r'^US\.', '', r['saham'].upper()); d = SH.isy(r['tarikh'])
            b = {k: SH.nombor(r[k]) for k in perlu[2:]}
            if t and d and all(v is not None and v > 0 for v in b.values()):
                K[(t, d)] = b
    return K


def hampir(a, b, tol=TOL):
    return a is not None and b is not None and b > 0 and abs(a / b - 1) <= tol


def banding_satu(d, K, beza, tiada):
    """Banding satu posisi (butiran pilih) dengan kline K. Pulang True jika sekurang-kurangnya satu medan dibanding."""
    t = d['saham']; disemak = False

    def bar(tk):
        b = K.get((t, tk))
        if b is None:
            tiada.append(f'{t} {tk}')
        return b

    def catat(medan, csv_, mm):
        beza.append(dict(saham=t, kaedah=d['kaedah'], tarikh_beli=d['tarikh_beli'], medan=medan, csv=csv_, moomoo=mm))

    b = bar(d['tarikh_beli'])
    hb = SH.nombor(d.get('harga_beli'))
    if b and hb:
        disemak = True
        if not hampir(hb, b['buka']):
            catat('harga_beli' + (' (buka sementara)' if d.get('nota_beli') else ''), hb, b['buka'])
    if d.get('tarikh_keluar'):
        b = bar(d['tarikh_keluar']); hk = SH.nombor(d.get('harga_keluar')); j = d.get('jenis_keluar')
        if b and hk and j:
            disemak = True
            if j in ('buka', 'tutup') and not hampir(hk, b[j]):
                catat(f'harga_keluar ({j})', hk, b[j])
            elif j == 'henti':
                if b['rendah'] > hk * (1 + TOL):
                    catat('henti disentuh (rendah <= harga_keluar)', hk, b['rendah'])
                if b['buka'] < hk * (1 - TOL):
                    catat('harga_keluar (buka bawah henti: patut = buka)', hk, b['buka'])
            elif j == 'sasaran':
                if b['tinggi'] < hk * (1 - TOL):
                    catat('sasaran dicapai (tinggi >= harga_keluar)', hk, b['tinggi'])
                if b['buka'] > hk * (1 + TOL):
                    catat('harga_keluar (buka atas sasaran: patut = buka)', hk, b['buka'])
    elif d.get('sesi') and SH.nombor(d.get('harga_terkini')):
        b = bar(d['sesi'])
        if b:
            disemak = True
            ht = SH.nombor(d['harga_terkini'])
            if not hampir(ht, b['tutup']):
                catat(f'harga_terkini (tutup {d["sesi"]})', ht, b['tutup'])
    if d.get('tarikh_keluar_henti'):
        j = d.get('jenis_keluar_henti') or 'buka'
        b = bar(d['tarikh_keluar_henti']); hk = SH.nombor(d.get('harga_keluar_henti'))
        if b and hk:
            disemak = True
            mm = b['buka'] if j == 'buka' else b['tutup']
            if not hampir(hk, mm):
                catat(f'harga_keluar_henti ({j})', hk, mm)
    return disemak


def banding(kline, sampel, keluar=KELUAR):
    K = baca_kline(kline)
    beza, tiada, n = [], [], 0
    for d in sampel['posisi']:
        n += banding_satu(d, K, beza, tiada)
    out = dict(tarikh=sampel.get('tarikh', ''), dibina=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC'),
               status='beza' if beza else ('ok' if n else 'belum'), n=n, n_beza=len(beza), beza=beza,
               n_pilih=len(sampel['posisi']), tiada_kline=sorted(set(tiada)))
    if keluar:
        os.makedirs(os.path.dirname(os.path.abspath(keluar)), exist_ok=True)
        with open(keluar, 'w', encoding='utf-8') as f:
            json.dump(out, f, ensure_ascii=False, indent=1)
            f.write('\n')
    return out


def main(argv=None):
    ap = argparse.ArgumentParser(description='Sampel posisi Papertrade C lawan kline harian Moomoo (rutin 6:02)')
    sp = ap.add_subparsers(dest='cmd', required=True)
    p = sp.add_parser('pilih')
    b = sp.add_parser('banding'); b.add_argument('kline')
    b.add_argument('--pilih', help='JSON keluaran pilih (lalai: pilih semula dengan peraturan sama)')
    b.add_argument('--keluar', default=KELUAR, help='fail keputusan (lalai data/semakan/sampel.json)')
    for x in (p, b):
        x.add_argument('--n', type=int, default=N_LALAI); x.add_argument('--tarikh')
        x.add_argument('--folder', default=PT); x.add_argument('--terkini', default=TERKINI)
    p.add_argument('--keluar', help='simpan JSON pilihan ke fail ini juga')
    a = ap.parse_args(argv)
    if a.cmd == 'pilih':
        s = pilih(a.folder, a.n, a.tarikh, a.terkini)
        teks = json.dumps(s, ensure_ascii=False, indent=1)
        if a.keluar:
            with open(a.keluar, 'w', encoding='utf-8') as f:
                f.write(teks + '\n')
        print(teks)
        return 0
    if a.pilih:
        with open(a.pilih, encoding='utf-8') as f:
            s = json.load(f)
    else:
        s = pilih(a.folder, a.n, a.tarikh, a.terkini)
    try:
        out = banding(a.kline, s, a.keluar)
    except (OSError, ValueError) as e:
        print(f'kline tidak sah: {e}', file=sys.stderr)
        return 2
    print(json.dumps({k: out[k] for k in ('tarikh', 'status', 'n', 'n_beza', 'n_pilih')}, ensure_ascii=False))
    for x in out['beza']:
        print('BEZA', x['saham'], x['kaedah'], x['tarikh_beli'], x['medan'], 'csv', x['csv'], 'moomoo', x['moomoo'])
    if out['tiada_kline']:
        print('TIADA KLINE', ', '.join(out['tiada_kline']))
    return 1 if out['beza'] else 0


if __name__ == '__main__':
    sys.exit(main())
