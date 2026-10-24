# kira_semula.py — pengiraan semula BEBAS setiap malam (24 Okt 2026; audit dashboard: aritmetik betul tetapi takrif tidak
# seragam). Membanding "kebenaran" (fail CSV papertrade + stor harga + fail AUTOTUNE) dengan dokumen db yang dibaca halaman
# dashboard (output `jana_db.py --keluar <folder>`). Sebarang beza -> status "beza" -> `jana_db.py` menambah baris
# "semakan: …" dalam harian/status.ralat (lampu sistem merah).
#
#   python3 BacktestShariah2/standard/kira_semula.py --db <folder db> [--json <keluar>] [--folder <papertrade>]
#       [--stor <stor>] [--terkini <terkini.csv | ''>] [--papan <analisis papan.json>] [--autotune <AUTOTUNE papan.json>]
#       [--pemangkin <folder kalendar earnings>]
#   -> data/semakan/kira_semula.json (lalai) {tarikh, dibina, status ok|beza|gagal, n_semak, n_beza, beza[<= 30], nilai}
#   Kod keluar: 0 ok, 1 beza, 2 gagal (input tiada / pengecualian).
#
# Semakan (kategori dalam nilai.semak = {kategori: [n_semak, n_beza]}):
#   baris        setiap baris papertrade/ringkas_c (sandaran claude*) dan ringkas_m lawan claude*.csv / moomoo.csv, dipadan
#                ikut (saham, kaedah, tarikh_beli, ke-n): saham, kaedah, tarikh_beli, harga_beli, harga_terkini, untung_pct,
#                keluar, tarikh_keluar, harga_keluar, untung_akhir_pct, keluar_henti, untung_henti_pct, tidak_sah, tidak_dibeli,
#                tutup_semua; baris hilang/lebih
#   earn_kini    earnings seterusnya pada/selepas sesi data = tarikh pertama >= sesi dalam kalendar gabungan
#                (kalendar_earnings.muat; tarikh > 80 hari tidak disemak kerana bergantung pada peraturan siri)
#   watchlist    papertrade/watchlist (+ bahagian) lawan watchlist.csv: Harga, % hampir (100 hanya isyarat lengkap, selainnya
#                maks 99.9), Syarat belum cukup, tarikh_data; baris hilang/lebih
#   agregat      angka yang dipapar halaman dikira dua kali dengan takrif yang sama (CSV lawan db dinyahkod): kiraan segmen
#                Posisi, belum direalisasi (setiap posisi dan ikut saham), direalisasi, aktiviti terkini, blok Esok "Dijual pada
#                buka", watchlist; prestasi/harian_kaedah (np, j akaun C) dikira semula daripada CSV
#   harga        posisi C terbuka (lorong kaedah): untung_pct CSV = tutup stor sesi data ÷ harga_beli − 1 (toleransi 0.05 mata);
#                posisi tanpa bar sesi itu dilapor berasingan (nilai.harga), bukan beza
#   penganalisis analisis/papan: at_label / at_cagr_bersih / lulus_at = AUTOTUNE/hasil/papan.json, lulus = bilangan semakan
#                lulus, swing = hari 3–30 (kecuali dalam 0.05 sempadan; hari dibundar), ditolak = bt_keputusan DITOLAK,
#                rujukan.at_spy_bersih = spy_bersih AUTOTUNE, Σ h_posisi = fasa.jumlah_hadapan = lejar_posisi −
#                lejar_tindih + c_pra_lejar, Σ h_matang = fasa.matang_hadapan, Σ p_top5 ≈ min(5, n), Σ p_top1 ≈ 1,
#                pangkat_p5 <= pangkat_p95; corong "Pintu wang sebenar" dalam nilai.pintu
# Bebas daripada jana_db.py: tiada fungsi pengiraannya diimport; format db (ringkas_pt, bahagi) dinyahkod di sini mengikut
# `nyahkod`/`subBhg` halaman dashboard_v2.html. Takrif agregat = takrif halaman (normPT, ptKpis2, kpiAktiviti, panelEsok, wBeli),
# kecuali baris tidak_dibeli yang di sini tidak pernah dikira "dibeli" (halaman v104 hanya menapis tidak_sah dalam prSrc dan
# bergantung pada konvensyen data tidak_dibeli => tidak_sah; benar bagi 64/64 baris pada 24 Okt 2026).
import argparse, csv, glob, hashlib, json, math, os, re, statistics as stt, sys
from datetime import date, datetime, timedelta, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
BS2 = os.path.dirname(HERE)
REPO = os.path.dirname(BS2)
PT = os.path.join(BS2, 'papertrade')
STOR = os.path.join(BS2, 'data', 'harga', 'stor')
TERKINI = os.path.join(BS2, 'data', 'harga', 'terkini.csv')
PAPAN = os.path.join(BS2, 'data', 'analisis', 'papan.json')
AUTOTUNE = os.path.join(REPO, 'AUTOTUNE', 'hasil', 'papan.json')
PEMANGKIN = os.path.join(BS2, 'data', 'pemangkin')
KELUAR = os.path.join(BS2, 'data', 'semakan', 'kira_semula.json')

TOL_UNTUNG = 0.05      # mata peratus: untung_pct CSV lawan tutup stor
TOL_SAMA = 1e-6        # nombor yang sepatutnya sama (db = CSV)
TOL_J = 0.011          # prestasi/harian_kaedah j dibundar 2 tp
TOL_P = 0.05           # Σ p_top5 / p_top1 (setiap nilai dibundar 3 tp)
HAD_BEZA = 30
DEKAT = 80             # kalendar_earnings.DEKAT: tarikh seterusnya dalam 80 hari sentiasa diterima
LENGKAP = 'Tiada (isyarat sah)'
MEDAN_TEKS = ('tarikh_keluar',)
MEDAN_NOMBOR = ('harga_beli', 'harga_terkini', 'untung_pct', 'harga_keluar', 'untung_akhir_pct', 'untung_henti_pct')
MEDAN_BOOL = ('keluar', 'keluar_henti', 'tidak_sah', 'tidak_dibeli', 'tutup_semua')


# ---------------------------------------------------------------- nilai asas
def benar(v):
    """Sama dengan benar() halaman: True, 'True', 'true'."""
    return v is True or (isinstance(v, str) and v.strip().lower() == 'true')


def nombor(v):
    if v is None or isinstance(v, bool):
        return None
    if isinstance(v, (int, float)):
        return None if isinstance(v, float) and math.isnan(v) else float(v)
    try:
        x = float(str(v).strip())
    except ValueError:
        return None
    return None if math.isnan(x) else x


def taip(v):
    """Nilai CSV -> nilai bertaip (bentuk baris db): 'True'/'False' -> bool, nombor -> float, selainnya teks."""
    if v in ('True', 'False'):
        return v == 'True'
    x = nombor(v)
    return x if x is not None else v


def teks(v):
    return None if v in (None, '') else str(v).strip()


def bulat(x, n=4):
    return None if x is None else round(float(x), n)


def purata(L):
    v = [x for x in L if x is not None]
    return stt.mean(v) if v else None


# ---------------------------------------------------------------- baca input
def baca_csv(p):
    if not os.path.exists(p):
        return []
    with open(p, newline='', encoding='utf-8-sig') as f:
        return list(csv.DictReader(f))


def no_fail_c(p):
    m = re.fullmatch(r'claude(?:_(\d+))?\.csv', os.path.basename(p))
    return (int(m.group(1)) if m.group(1) else 1) if m else None


def baca_c(folder):
    """Semua baris Papertrade C (claude.csv, claude_2.csv, … ikut nombor)."""
    fail = sorted((p for p in glob.glob(os.path.join(folder, 'claude*.csv')) if no_fail_c(p)), key=no_fail_c)
    out = []
    for p in fail:
        out += baca_csv(p)
    return out, [os.path.basename(p) for p in fail]


def baca_doc(db, path):
    p = os.path.join(db, path + '.json')
    if not os.path.exists(p):
        return None
    with open(p, encoding='utf-8') as f:
        return json.load(f)


class TiadaBahagian(Exception):
    pass


def nyahkod_ringkas(db, koleksi, nama):
    """papertrade/ringkas_c|m (padat ikut lajur) -> (dokumen {meta…, rows}, id) seperti `nyahkod` halaman. None jika asas tiada.
    Bahagian/kamus yang tiada atau `induk` lain -> TiadaBahagian (halaman tidak memapar data sehingga semua tiba)."""
    asas = baca_doc(db, f'{koleksi}/{nama}')
    if asas is None:
        return None, None
    B = asas.get('bahagian') or {'n': 1, 'nk': 0}
    rows = list(asas.get('rows') or [])
    for i in range(2, int(B.get('n') or 1) + 1):
        ch = baca_doc(db, f'{koleksi}/{nama}_{i}')
        if not ch or ch.get('induk') != B.get('id'):
            raise TiadaBahagian(f'{koleksi}/{nama}_{i} tiada atau induk bukan {B.get("id")}')
        rows += ch.get('rows') or []
    M = {}
    for i in range(1, int(B.get('nk') or 0) + 1):
        km = baca_doc(db, f'{koleksi}/{nama}_kamus_{i}')
        if not km or km.get('induk') != B.get('id'):
            raise TiadaBahagian(f'{koleksi}/{nama}_kamus_{i} tiada atau induk bukan {B.get("id")}')
        for c, mula, v in km.get('kamus') or []:
            L = M.setdefault(c, {})
            for j, x in enumerate(v):
                L[mula + j] = x
    K, J = asas.get('kolum') or [], asas.get('jenis') or []
    out = []
    for a in rows:
        r = {}
        for j, c in enumerate(K):
            v, t = a[j], J[j]
            if v is None:
                continue
            if t in ('k', 'j'):
                if not v:
                    continue
                v = M[c][v - 1]
                if t == 'j':
                    v = json.loads(v)
            elif t == 'b':
                v = bool(v)
            r[c] = v
        out.append(r)
    d = {k: v for k, v in asas.items() if k not in ('kolum', 'jenis', 'rows', 'bahagian')}
    d['rows'] = out
    return d, B.get('id')


def gabung_bahagian(db, path):
    """Dokumen dibahagi (bahagi_db): asas {bahagian:{id,n}} + <nama>_2… {induk, rows} -> (dokumen, [bahagian hilang])."""
    asas = baca_doc(db, path)
    if asas is None:
        return None, []
    b = asas.get('bahagian')
    rows, hilang = list(asas.get('rows') or []), []
    if b and int(b.get('n') or 1) > 1:
        for i in range(2, int(b['n']) + 1):
            c = baca_doc(db, f'{path}_{i}')
            if c and c.get('induk') == b.get('id'):
                rows += c.get('rows') or []
            else:
                hilang.append(f'{path}_{i}')
    return dict(asas, rows=rows), hilang


def tanda_db(baca):
    """Cap jari KANDUNGAN dokumen db yang disemak (tidak berubah apabila jana_db dijalankan semula atas data sama): ringkas_c/m =
    bahagian.id (cincang baris, ringkas_pt); watchlist dan harian_kaedah = cincang baris semua bahagian; papan = dibina;
    sesi = harian/status.harga_tutup_pada. baca(path) -> dokumen atau None. jana_db.py membanding cap jari ini dengan
    dokumen yang ditolak: berbeza = keputusan kira_semula LAPUK (bagi db lain)."""
    def cincang(p):
        d = baca(p)
        if d is None:
            return None
        b = d.get('bahagian') or {}
        if 'kolum' in d:
            return b.get('id')
        rows = list(d.get('rows') or [])
        for i in range(2, int(b.get('n') or 1) + 1):
            c = baca(f'{p}_{i}') or {}
            rows += (c.get('rows') or []) if c.get('induk') == b.get('id') else [None]
        return hashlib.sha1(json.dumps(rows, ensure_ascii=False, separators=(',', ':')).encode('utf-8')).hexdigest()[:12]
    return dict(ringkas_c=cincang('papertrade/ringkas_c'), ringkas_m=cincang('papertrade/ringkas_m'),
                watchlist=cincang('papertrade/watchlist'), harian_kaedah=cincang('prestasi/harian_kaedah'),
                papan=(baca('analisis/papan') or {}).get('dibina'), sesi=(baca('harian/status') or {}).get('harga_tutup_pada'))


def bar_sesi(stor, terkini, S, tickers=None):
    """{ticker: tutup} pada sesi S (YYYY-MM-DD) daripada stor (harga_A/B.csv); bar terkini.csv dipakai bagi ticker yang tiada
    bar S dalam stor. Juga pulang sesi penuh terakhir stor+terkini (>= 50% bilangan maksimum saham)."""
    import pandas as pd
    Si = int(S.replace('-', ''))
    fr = []
    for f in ('harga_A.csv', 'harga_B.csv'):
        p = os.path.join(stor, f)
        if os.path.exists(p):
            fr.append(pd.read_csv(p, usecols=['ticker', 'date', 'close']))
    st = pd.concat(fr, ignore_index=True) if fr else pd.DataFrame(columns=['ticker', 'date', 'close'])
    tk = pd.read_csv(terkini, usecols=['ticker', 'date', 'close']) if terkini and os.path.exists(terkini) else st.iloc[:0]
    semua = pd.concat([st, tk], ignore_index=True)
    semua['date'] = semua.date.astype(int)
    n = semua.drop_duplicates(['ticker', 'date']).date.value_counts()
    penuh = str(max(d for d, k in n.items() if k >= 0.5 * n.max())) if len(n) else ''
    out = {}
    for src in (tk, st):   # stor diutamakan (ditulis kemudian)
        x = src[src.date.astype(int) == Si]
        if tickers is not None:
            x = x[x.ticker.isin(tickers)]
        out.update(zip(x.ticker, x.close.astype(float)))
    return out, (f'{penuh[:4]}-{penuh[4:6]}-{penuh[6:]}' if penuh else '')


def muat_kalendar(folder):
    try:
        sys.path.insert(0, HERE)
        import kalendar_earnings as KE
        return KE.muat(folder)
    except Exception:  # noqa: BLE001
        return None


def hari_dag_berikut(t):
    """Hari dagangan NYSE selepas t (YYYY-MM-DD); tanpa exchange_calendars: hari bekerja."""
    d = date.fromisoformat(t[:10])
    try:
        import exchange_calendars as xc
        import pandas as pd
        c = xc.get_calendar('XNYS')
        s = c.sessions_in_range(pd.Timestamp(d + timedelta(days=1)), pd.Timestamp(d + timedelta(days=15)))
        return str(s[0].date()) if len(s) else ''
    except Exception:  # noqa: BLE001
        d += timedelta(days=1)
        while d.weekday() > 4:
            d += timedelta(days=1)
        return d.isoformat()


# ---------------------------------------------------------------- pengumpul beza
class Semak:
    def __init__(self):
        self.n, self.beza, self.kat, self._kb = 0, [], {}, []

    def catat(self, kat, medan, dijangka, didapati, nota=''):
        k = self.kat.setdefault(kat, [0, 0])
        k[1] += 1
        self.beza.append(dict(medan=medan, dijangka=dijangka, didapati=didapati, nota=nota))
        self._kb.append(kat)

    def contoh(self, had=HAD_BEZA):
        """<= had beza bergilir antara kategori (setiap kategori yang ada beza terwakili), susunan asal dalam kategori."""
        kump = {}
        for k, b in zip(self._kb, self.beza):
            kump.setdefault(k, []).append(b)
        out, i = [], 0
        while len(out) < had and any(i < len(v) for v in kump.values()):
            out += [v[i] for v in kump.values() if i < len(v)][:had - len(out)]
            i += 1
        return out

    def beza_terus(self, kat, medan, dijangka, didapati, nota=''):
        """Satu semakan yang sudah diketahui gagal (baris/bahagian hilang)."""
        self.n += 1
        self.kat.setdefault(kat, [0, 0])[0] += 1
        self.catat(kat, medan, dijangka, didapati, nota)

    def banding(self, kat, medan, dijangka, didapati, tol=None, nota=''):
        self.n += 1
        self.kat.setdefault(kat, [0, 0])[0] += 1
        if sama(dijangka, didapati, tol):
            return True
        self.catat(kat, medan, dijangka, didapati, nota)
        return False


def sama(a, b, tol=None):
    if a is None or b is None:
        return a is None and b is None
    if isinstance(a, bool) or isinstance(b, bool):
        return bool(a) == bool(b) and isinstance(a, bool) == isinstance(b, bool)
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return abs(float(a) - float(b)) <= (TOL_SAMA if tol is None else tol) + 1e-12
    return a == b


# ---------------------------------------------------------------- baris (db lawan CSV)
def kunci_baris(rows, f_saham='saham', f_kaedah='kaedah', f_tarikh='tarikh_beli'):
    """{(saham, kaedah, tarikh, ke-n): baris} — kunci unik SKEMA + nombor kejadian (pendua dipadan ikut susunan)."""
    out, n = {}, {}
    for r in rows:
        k = (teks(r.get(f_saham)), teks(r.get(f_kaedah)), teks(r.get(f_tarikh)))
        n[k] = n.get(k, 0) + 1
        out[k + (n[k],)] = r
    return out


def nama_kunci(ak, k):
    return f"{ak}:{k[0]}|{k[1]}|{k[2]}" + (f'#{k[3]}' if k[3] > 1 else '')


def semak_baris(sm, ak, csv_rows, db_rows):
    A, B = kunci_baris(csv_rows), kunci_baris(db_rows)
    sm.banding('baris', f'{ak}:bilangan_baris', len(csv_rows), len(db_rows))
    for k in A.keys() - B.keys():
        sm.beza_terus('baris', nama_kunci(ak, k), 'ada dalam CSV', None, 'baris tiada dalam db')
    for k in B.keys() - A.keys():
        sm.beza_terus('baris', nama_kunci(ak, k), None, 'ada dalam db', 'baris tiada dalam CSV')
    for k in sorted(A.keys() & B.keys(), key=lambda x: tuple(str(y) for y in x)):
        c, d = A[k], B[k]
        for f in MEDAN_TEKS:
            sm.banding('baris', f'{nama_kunci(ak, k)}.{f}', teks(c.get(f)), teks(d.get(f)))
        for f in MEDAN_NOMBOR:
            sm.banding('baris', f'{nama_kunci(ak, k)}.{f}', nombor(c.get(f)), nombor(d.get(f)))
        for f in MEDAN_BOOL:
            sm.banding('baris', f'{nama_kunci(ak, k)}.{f}', benar(c.get(f)), bool(d.get(f)) if not isinstance(d.get(f), str) else benar(d.get(f)))


def semak_earn(sm, ak, db_rows, S, K):
    """earn_kini (medan db sahaja) = tarikh pertama >= S dalam kalendar gabungan. Tarikh > DEKAT hari: tidak disemak."""
    if not S or K is None:
        return
    D = date.fromisoformat(S)
    cache = {}
    for r in db_rows:
        t = r.get('saham')
        if t not in cache:
            akan = sorted(d for d in K.get(t, {}) if d >= D)
            cache[t] = akan[0] if akan else None
        x = cache[t]
        got = teks(r.get('earn_kini'))
        k = f"{ak}:{t}|{r.get('kaedah')}|{r.get('tarikh_beli')}.earn_kini"
        if got is not None:
            sm.banding('earn_kini', k, x.isoformat() if x else None, got, nota='earnings pertama pada/selepas sesi data')
        elif x is not None and (x - D).days <= DEKAT:
            sm.banding('earn_kini', k, x.isoformat(), None, nota=f'kalendar ada earnings {x} (<= {DEKAT} hari)')


# ---------------------------------------------------------------- takrif halaman
def norm_pt(r):
    """Baris (bertaip) -> semantik normPT halaman (keluar, tutup_semua, untung_akhir_pct, harga_terkini, …)."""
    kel = bool(r.get('keluar') if not isinstance(r.get('keluar'), str) else benar(r.get('keluar'))) or bool(teks(r.get('tarikh_keluar')))
    ts = r.get('tutup_semua')
    kh = r.get('keluar_henti')
    if ts not in (None, ''):
        tutup = benar(ts)
    elif r.get('status_henti') or kh not in (None, ''):
        tutup = kel and benar(kh)
    else:
        tutup = kel
    tsah = r.get('tidak_sah')
    return dict(saham=teks(r.get('saham')), kaedah=teks(r.get('kaedah')) or teks(r.get('id_kaedah')) or '–',
                tarikh_beli=teks(r.get('tarikh_beli')), tarikh_keluar=teks(r.get('tarikh_keluar')), keluar=kel,
                keluar_henti=benar(kh), tutup_semua=tutup, tidak_sah=benar(tsah) if isinstance(tsah, str) else bool(tsah),
                tidak_dibeli=benar(r.get('tidak_dibeli')) if isinstance(r.get('tidak_dibeli'), str) else bool(r.get('tidak_dibeli')),
                untung_pct=nombor(r.get('untung_pct')),
                untung_akhir_pct=(nombor(r.get('untung_akhir_pct')) if nombor(r.get('untung_akhir_pct')) is not None
                                  else nombor(r.get('untung_pct'))) if kel else None,
                isyarat_keluar=teks(r.get('isyarat_keluar')) or ('Keluar' if kel else 'Pegang'),
                status_henti=teks(r.get('status_henti')) or '')


def ikut_saham(L, f):
    m = {}
    for r in L:
        if r.get(f) is not None:
            m.setdefault(r['saham'], []).append(r[f])
    return purata([stt.mean(v) for v in m.values()]) if m else None


def agregat_pos(R):
    """Angka tab Posisi / Hari ini (Papertrade C) daripada baris norm_pt."""
    pos = [r for r in R if not r['tidak_dibeli']]           # posRows('c')
    sah = [r for r in pos if not r['tidak_sah']]
    ts = [r for r in pos if r['tidak_sah']]
    peg = [r for r in sah if not r['keluar']]
    l2 = [r for r in sah if r['keluar'] and not r['keluar_henti']]
    tut = [r for r in sah if r['tutup_semua']]
    op = [r for r in peg if r['untung_pct'] is not None]
    ex = [r for r in sah if r['keluar'] and r['untung_akhir_pct'] is not None]
    dB = max((r['tarikh_beli'] or '' for r in sah), default='')
    dK = max((r['tarikh_keluar'] or '' for r in sah if r['keluar']), default='')
    jual = [r for r in sah if not r['tutup_semua'] and ((not r['keluar'] and 'menunggu' in r['isyarat_keluar'])
                                                      or (not r['keluar_henti'] and 'menunggu' in r['status_henti']))]
    return dict(
        posisi=dict(semua=len(pos), sah=len(sah), tidak_sah=len(ts), pegang=len(peg), l2_sahaja=len(l2), tutup=len(tut),
                    tidak_dibeli=len(R) - len(pos)),
        pegang=dict(posisi=len(peg), saham=len({r['saham'] for r in peg}), kaedah=len({r['kaedah'] for r in peg}),
                    belum_direalisasi=bulat(purata([r['untung_pct'] for r in op])),
                    pct_sedang_untung=bulat(100 * sum(r['untung_pct'] > 0 for r in op) / len(op)) if op else None,
                    ikut_saham=bulat(ikut_saham(op, 'untung_pct'))),
        direalisasi=dict(posisi=len(ex), purata=bulat(purata([r['untung_akhir_pct'] for r in ex])),
                         ikut_saham=bulat(ikut_saham(ex, 'untung_akhir_pct')),
                         pct_menang=bulat(100 * sum(r['untung_akhir_pct'] > 0 for r in ex) / len(ex)) if ex else None),
        aktiviti=dict(tarikh_beli=dB, dibeli=sum(r['tarikh_beli'] == dB for r in sah) if dB else 0,
                      tarikh_keluar=dK, keluar=sum(r['keluar'] and r['tarikh_keluar'] == dK for r in sah) if dK else 0),
        esok=dict(jual_posisi=len(jual), jual_saham=len({r['saham'] for r in jual})))


def agregat_watch(W, t0, sah_c):
    """Watchlist dipapar (90–100%), isyarat lengkap, dan blok Esok "Isyarat lengkap dalam watchlist" (menunggu belian)."""
    hp = [r for r in W if 90 <= (nombor(r.get('pct_dipenuhi')) or 0) <= 100]
    lk = [r for r in hp if str(r.get('syarat_belum') or '').strip().lower().startswith(LENGKAP.lower())]
    beli = [r for r in sah_c if r['tarikh_beli']]
    akhir = max((r['tarikh_beli'] for r in beli), default='')
    tb = hari_dag_berikut(t0) if t0 else ''
    tunggu = 0
    for r in lk:
        sama_k = [x for x in beli if x['saham'] == teks(r.get('saham')) and x['kaedah'] == teks(r.get('kaedah'))]
        if any(x['tarikh_beli'] > t0 for x in sama_k) or any(not x['keluar'] and x['tarikh_beli'] <= t0 for x in sama_k):
            continue
        if tb and akhir >= tb:
            continue
        tunggu += 1
    return dict(baris=len(W), hampir=len(hp), lengkap=len(lk), lengkap_menunggu=tunggu)


def norm_pct_hampir(r):
    """% hampir dalam db: 100 hanya bagi isyarat lengkap; selainnya dihadkan 99.9 (SKEMA watchlist.csv, 24 Okt 2026)."""
    v = nombor(r.get('% hampir'))
    if v is not None and (r.get('Syarat belum cukup') or '').strip() != LENGKAP and v > 99.9:
        v = 99.9
    return v


def semak_watch(sm, W_csv, W_db):
    A = kunci_baris(W_csv, 'Saham', 'Kaedah', 'Set')
    B = kunci_baris(W_db, 'saham', 'kaedah', 'set')
    sm.banding('watchlist', 'watchlist:bilangan_baris', len(W_csv), len(W_db))
    for k in A.keys() ^ B.keys():
        sm.beza_terus('watchlist', nama_kunci('W', k), 'ada dalam CSV' if k in A else None, 'ada dalam db' if k in B else None,
                 'baris tiada dalam db' if k in A else 'baris tiada dalam CSV')
    for k in A.keys() & B.keys():
        c, d, n = A[k], B[k], nama_kunci('W', k)
        sm.banding('watchlist', n + '.harga_terkini', nombor(c.get('Harga')), nombor(d.get('harga_terkini')))
        sm.banding('watchlist', n + '.pct_dipenuhi', norm_pct_hampir(c), nombor(d.get('pct_dipenuhi')))
        sm.banding('watchlist', n + '.syarat_belum', teks(c.get('Syarat belum cukup')), teks(d.get('syarat_belum')))
        sm.banding('watchlist', n + '.tarikh_data', teks(c.get('tarikh_data')), teks(d.get('tarikh_data')))


def harian_kaedah_csv(C):
    """prestasi/harian_kaedah akaun C: {kaedah | 'Semua': (np, j)} — posisi sah (bukan tidak_dibeli/tidak_sah/luar_peraturan,
    harga_beli > 0, ada tarikh_beli); j = purata untung akhir (keluar) atau semasa (dipegang)."""
    g = {}
    for r in C:
        if benar(r.get('tidak_dibeli')) or benar(r.get('tidak_sah')) or benar(r.get('luar_peraturan')):
            continue
        if not nombor(r.get('harga_beli')) or not r.get('tarikh_beli'):
            continue
        u = nombor(r.get('untung_akhir_pct') if benar(r.get('keluar')) else r.get('untung_pct')) or 0.0
        for k in (r.get('kaedah'), 'Semua'):
            g.setdefault(k, []).append(u)
    return {k: (len(v), round(stt.mean(v), 2)) for k, v in g.items()}


# ---------------------------------------------------------------- penganalisis
PINTU = [('swing', lambda r, s: bool(r.get('swing'))),
         ('berkedudukan', lambda r, s: r.get('kedudukan') is not None),
         ('tidak_ditolak', lambda r, s: not r.get('ditolak')),
         ('autotune', lambda r, s: r.get('at_label') in ('SEDERHANA', 'TINGGI')),
         ('bersih_atasi_spy', lambda r, s: r.get('at_cagr_bersih') is not None and s is not None and r['at_cagr_bersih'] > s),
         ('kuat', lambda r, s: r.get('status') == 'KUAT')]


def pintu(rows, spy_bersih):
    """Corong "Pintu wang sebenar" (halaman PINTU/pintuM): bilangan kaedah yang melepasi pintu 1..k berturut-turut."""
    out, hidup = {'aktif': len(rows)}, list(rows)
    for k, f in PINTU:
        hidup = [r for r in hidup if f(r, spy_bersih)]
        out[k] = len(hidup)
    return out


def semak_papan(sm, P, A):
    rows = P.get('rows') or []
    at = {r['id']: r for r in (A or {}).get('kaedah', [])} if A else None
    if at is not None:
        for r in rows:
            a = at.get(r['id'])
            ada = a is not None
            lbl = a.get('label') if ada else None
            cb = round(a['cagr_bersih'], 3) if ada and nombor(a.get('cagr_bersih')) is not None else None
            if ada and None not in (nombor(a.get('cagr_a')), nombor(a.get('spy_a')), nombor(a.get('cagr_b')), nombor(a.get('spy_b'))):
                la = a['cagr_a'] > a['spy_a'] and a['cagr_b'] > a['spy_b']
            else:
                la = None
            sm.banding('penganalisis', f"{r['id']}.at_label", lbl, r.get('at_label'), nota='AUTOTUNE/hasil/papan.json label')
            sm.banding('penganalisis', f"{r['id']}.at_cagr_bersih", cb, r.get('at_cagr_bersih'), tol=5e-4,
                       nota='AUTOTUNE cagr_bersih (3 tp)')
            sm.banding('penganalisis', f"{r['id']}.lulus_at", la, r.get('lulus_at'), nota='cagr_a > spy_a dan cagr_b > spy_b')
        sb = [nombor(a.get('spy_bersih')) for a in at.values() if nombor(a.get('spy_bersih')) is not None]
        sm.banding('penganalisis', 'rujukan.at_spy_bersih', round(sb[0], 4) if sb else None,
                   (P.get('rujukan') or {}).get('at_spy_bersih'), tol=5e-5, nota='spy_bersih AUTOTUNE')
        if len(set(sb)) > 1:
            sm.banding('penganalisis', 'autotune.spy_bersih_seragam', 1, len(set(sb)), nota='spy_bersih berbeza antara kaedah AUTOTUNE')
    for r in rows:
        n = sum(bool(r.get(k)) for k in ('lulus_subset', 'lulus_wfo', 'lulus_at'))
        sm.banding('penganalisis', f"{r['id']}.lulus", n, r.get('lulus'), nota='bilangan semakan luar sampel lulus')
        # input pintu 1 dan 3: swing = pegang backtest 3–30 hari; ditolak = keputusan backtest DITOLAK
        # (hari dibundar 1 tp dalam papan: dalam 0.05 daripada sempadan 3/30 tidak boleh ditentukan, cth. M34 30.02 -> "30.0")
        h = nombor(r.get('hari'))
        if h is None or min(abs(h - 3), abs(h - 30)) > 0.05:
            sm.banding('penganalisis', f"{r['id']}.swing", h is not None and 3 <= h <= 30, r.get('swing'), nota=f'hari pegang {h}')
        sm.banding('penganalisis', f"{r['id']}.ditolak", r.get('bt_keputusan') == 'DITOLAK', r.get('ditolak'),
                   nota=f"bt_keputusan {r.get('bt_keputusan')}")
    F = P.get('fasa') or {}
    hp, hm = sum(int(r.get('h_posisi') or 0) for r in rows), sum(int(r.get('h_matang') or 0) for r in rows)
    sm.banding('penganalisis', 'fasa.jumlah_hadapan', hp, F.get('jumlah_hadapan'), nota='Σ h_posisi')
    sm.banding('penganalisis', 'fasa.matang_hadapan', hm, F.get('matang_hadapan'), nota='Σ h_matang')
    if None not in (P.get('lejar_posisi'), P.get('lejar_tindih'), P.get('c_pra_lejar')):
        sm.banding('penganalisis', 'h_posisi.jumlah_terdokumen', P['lejar_posisi'] - P['lejar_tindih'] + P['c_pra_lejar'], hp,
                   nota='lejar_posisi − lejar_tindih + c_pra_lejar (PENGANALISIS.md) lawan Σ h_posisi')
    rk = [r for r in rows if r.get('p_top5') is not None]
    if rk:
        sm.banding('penganalisis', 'Σ p_top5', float(min(5, len(rk))), round(sum(r['p_top5'] for r in rk), 4), tol=TOL_P)
        sm.banding('penganalisis', 'Σ p_top1', 1.0, round(sum(r.get('p_top1') or 0 for r in rk), 4), tol=TOL_P)
        for r in rk:
            a, b = r.get('pangkat_p5'), r.get('pangkat_p95')
            sm.banding('penganalisis', f"{r['id']}.pangkat_p5<=p95", True, a is not None and b is not None and 1 <= a <= b <= len(rk))
    sp = (P.get('rujukan') or {}).get('at_spy_bersih')
    return dict(kaedah=len(rows), berkedudukan=sum(r.get('kedudukan') is not None for r in rows), swing=sum(bool(r.get('swing')) for r in rows),
                matang_hadapan=F.get('matang_hadapan'), jumlah_hadapan=F.get('jumlah_hadapan'), kini=P.get('kini')), pintu(rows, sp)


# ---------------------------------------------------------------- utama
def semak(db, folder=PT, stor=STOR, terkini=None, papan=None, autotune=AUTOTUNE, kal=None):
    """Semua semakan (tanpa menulis fail) -> (Semak: n, beza, kat; nilai: angka dijangka yang dipapar; S: sesi data)."""
    sm = Semak()
    nilai = {}
    st = baca_doc(db, 'harian/status') or {}
    S = teks(st.get('harga_tutup_pada')) or teks(st.get('tarikh_data')) or ''
    S = S[:10] if re.match(r'\d{4}-\d\d-\d\d', S) else ''
    nilai['sesi'] = S
    # --- baris C
    C, fail_c = baca_c(folder)
    dc, _ = nyahkod_ringkas(db, 'papertrade', 'ringkas_c')
    sumber_c = 'papertrade/ringkas_c'
    if dc is None:   # halaman v90+: tanpa ringkas_c, baca claude, claude_2, …
        rows, n = [], 1
        while True:
            d = baca_doc(db, 'papertrade/claude' + ('' if n == 1 else f'_{n}'))
            if d is None:
                break
            rows += d.get('rows') or []; n += 1
        if n == 1:
            raise FileNotFoundError(f'{db}: papertrade/ringkas_c dan papertrade/claude tiada')
        dc, sumber_c = dict(rows=rows), 'papertrade/claude*'
    semak_baris(sm, 'C', C, dc['rows'])
    nilai['db_tanda'] = tanda_db(lambda p: baca_doc(db, p))
    nilai['baris'] = dict(c=len(C), c_db=len(dc['rows']), sumber_c=sumber_c, fail_c=len(fail_c))
    # --- baris M (arkib Moomoo)
    M = baca_csv(os.path.join(folder, 'moomoo.csv'))
    dm, _ = nyahkod_ringkas(db, 'papertrade', 'ringkas_m')
    if dm is None:
        dm = baca_doc(db, 'papertrade/moomoo')
    if M or dm:
        semak_baris(sm, 'M', M, (dm or {}).get('rows') or [])
        nilai['baris'].update(m=len(M), m_db=len((dm or {}).get('rows') or []))
    # --- earn_kini
    if kal is not None:
        semak_earn(sm, 'C', dc['rows'], S, kal)
        if dm:
            semak_earn(sm, 'M', dm.get('rows') or [], S, kal)
    # --- agregat: CSV (kebenaran) lawan db dinyahkod, takrif halaman
    Rc = [norm_pt({k: taip(v) for k, v in r.items() if v not in ('', None)}) for r in C]
    Rd = [norm_pt(r) for r in dc['rows']]
    ag, ag_db = agregat_pos(Rc), agregat_pos(Rd)
    for kump, d in ag.items():
        for k, v in d.items():
            sm.banding('agregat', f'{kump}.{k}', v, ag_db[kump][k], tol=1e-6)
    nilai.update(ag)
    # watchlist
    Wc = baca_csv(os.path.join(folder, 'watchlist.csv'))
    wd, hilang = gabung_bahagian(db, 'papertrade/watchlist')
    for h in hilang:
        sm.beza_terus('watchlist', h, 'bahagian ada', None, 'bahagian watchlist tiada atau induk lain')
    if Wc or wd:
        Wd = (wd or {}).get('rows') or []
        semak_watch(sm, Wc, Wd)
        t0 = teks((wd or {}).get('tarikh_data')) or ''
        sah_c = [r for r in Rc if not r['tidak_dibeli'] and not r['tidak_sah']]
        Wc_db = [dict(saham=r.get('Saham'), kaedah=r.get('Kaedah'), pct_dipenuhi=norm_pct_hampir(r),
                      syarat_belum=r.get('Syarat belum cukup')) for r in Wc]
        aw, aw_db = agregat_watch(Wc_db, t0, sah_c), agregat_watch(Wd, t0, sah_c)
        for k, v in aw.items():
            sm.banding('agregat', f'watchlist.{k}', v, aw_db[k])
        nilai['watchlist'] = dict(aw, tarikh_data=t0)
    # prestasi/harian_kaedah (np, j) akaun C
    hk, hilang = gabung_bahagian(db, 'prestasi/harian_kaedah')
    if hk is not None:
        jangka = harian_kaedah_csv(C)
        dapat = {r['k']: (r.get('np'), r.get('j')) for r in hk.get('rows') or [] if r.get('a') == 'C'}
        for k in sorted(jangka.keys() | dapat.keys()):
            e, g = jangka.get(k, (None, None)), dapat.get(k, (None, None))
            sm.banding('agregat', f'harian_kaedah.C.{k}.np', e[0], g[0])
            sm.banding('agregat', f'harian_kaedah.C.{k}.j', e[1], g[1], tol=TOL_J)
        for h in hilang:
            sm.beza_terus('agregat', h, 'bahagian ada', None, 'bahagian prestasi/harian_kaedah tiada atau induk lain')
    # --- harga: untung_pct posisi C terbuka lawan tutup stor sesi S
    if S:
        buka = [r for r in C if not benar(r.get('tidak_dibeli')) and not benar(r.get('keluar')) and not r.get('tarikh_keluar')
                and (nombor(r.get('harga_beli')) or 0) > 0]
        tutup, penuh = bar_sesi(stor, terkini, S, {r['saham'] for r in buka})
        tanpa = []
        for r in buka:
            c = tutup.get(r['saham'])
            if c is None:
                tanpa.append(r); continue
            hb = nombor(r['harga_beli'])
            sm.banding('harga', f"C:{r['saham']}|{r['kaedah']}|{r['tarikh_beli']}.untung_pct", round((c / hb - 1) * 100, 4),
                       nombor(r.get('untung_pct')), tol=TOL_UNTUNG,
                       nota=f"tutup stor {S} {c:g} ÷ harga_beli {hb:g}; harga_terkini CSV {r.get('harga_terkini')}")
        nilai['harga'] = dict(sesi_stor=penuh, terbuka=len(buka), disemak=len(buka) - len(tanpa), tanpa_bar_sesi=len(tanpa),
                              saham_tanpa_bar=sorted({r['saham'] for r in tanpa})[:30],
                              bil_saham_tanpa_bar=len({r['saham'] for r in tanpa}))
    # --- penganalisis
    pp = papan or (os.path.join(db, 'analisis', 'papan.json') if os.path.exists(os.path.join(db, 'analisis', 'papan.json')) else PAPAN)
    if os.path.exists(pp):
        with open(pp, encoding='utf-8') as f:
            P = json.load(f)
        A = None
        if autotune and os.path.exists(autotune):
            with open(autotune, encoding='utf-8') as f:
                A = json.load(f)
        nilai['penganalisis'], nilai['pintu'] = semak_papan(sm, P, A)
        dbp = os.path.join(db, 'analisis', 'papan.json')
        nilai['penganalisis'].update(autotune=bool(A), sumber='db analisis/papan' if os.path.abspath(pp) == os.path.abspath(dbp) else pp)
    nilai['semak'] = sm.kat
    return sm, nilai, S


def main(argv=None):
    ap = argparse.ArgumentParser(description='Pengiraan semula bebas: CSV + stor harga + AUTOTUNE lawan dokumen db dashboard')
    ap.add_argument('--db', required=True, help='folder output jana_db.py --keluar')
    ap.add_argument('--json', default=KELUAR)
    ap.add_argument('--folder', default=PT)
    ap.add_argument('--stor', default=STOR)
    ap.add_argument('--terkini', default=None, help="terkini.csv (lalai: data/harga/terkini.csv jika --stor = stor repo; '' = tiada)")
    ap.add_argument('--papan', default=None, help='analisis papan.json yang dibaca halaman (lalai: <db>/analisis/papan.json)')
    ap.add_argument('--autotune', default=AUTOTUNE)
    ap.add_argument('--pemangkin', default=PEMANGKIN, help="folder kalendar earnings ('' = tidak semak earn_kini)")
    a = ap.parse_args(argv)
    tk = a.terkini if a.terkini is not None else (TERKINI if os.path.abspath(a.stor) == os.path.abspath(STOR) else None)
    dibina = datetime.now(timezone(timedelta(hours=8))).strftime('%Y-%m-%d %H:%M') + ' MYT'
    try:
        if not os.path.isdir(a.db):
            raise FileNotFoundError(f'folder db tiada: {a.db}')
        kal = muat_kalendar(a.pemangkin) if a.pemangkin else None
        sm, nilai, S = semak(a.db, a.folder, a.stor, tk or None, a.papan, a.autotune, kal)
        out = dict(tarikh=S, dibina=dibina, status='beza' if sm.beza else 'ok', n_semak=sm.n, n_beza=len(sm.beza),
                   beza=sm.contoh(), nilai=nilai)
        kod = 1 if sm.beza else 0
    except Exception as e:  # noqa: BLE001
        try:   # cap jari db tetap direkod supaya jana_db melapor "gagal" (merah), bukan "lapuk"
            nl = dict(db_tanda=tanda_db(lambda p: baca_doc(a.db, p)))
        except Exception:  # noqa: BLE001
            nl = {}
        out = dict(tarikh='', dibina=dibina, status='gagal', n_semak=0, n_beza=0,
                   beza=[dict(medan='kira_semula', dijangka='larian lengkap', didapati=None, nota=f'{type(e).__name__}: {e}'[:300])],
                   nilai=nl)
        kod = 2
    os.makedirs(os.path.dirname(os.path.abspath(a.json)), exist_ok=True)
    with open(a.json, 'w', encoding='utf-8') as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
        f.write('\n')
    r = dict(status=out['status'], tarikh=out['tarikh'], n_semak=out['n_semak'], n_beza=out['n_beza'],
             kategori=out['nilai'].get('semak'), json=a.json)
    print(json.dumps(r, ensure_ascii=False))
    for b in out['beza'][:10]:
        print(f"  beza {b['medan']}: dijangka {b['dijangka']!r}, didapati {b['didapati']!r} {b['nota']}", file=sys.stderr)
    return kod


if __name__ == '__main__':
    sys.exit(main())
