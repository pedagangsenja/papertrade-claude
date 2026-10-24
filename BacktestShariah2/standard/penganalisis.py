# penganalisis.py — Papan Penganalisis: satu jadual banding semua kaedah aktif, menggabungkan bukti backtest dan data hadapan
# (keputusan pengguna 20 Okt 2026). Tanpa LLM; dijalankan oleh GitHub Actions `analisis.yml` sebaik `lejar.yml` siap.
#
#   python3 BacktestShariah2/standard/penganalisis.py [--kini YYYY-MM-DD] [--json laluan] [--md laluan] [--lama papan_lama.json]
#   -> BacktestShariah2/laporan/PENGANALISIS.md, BacktestShariah2/data/analisis/papan.json (= dokumen db dashboard analisis/papan)
# Tarikh papan (kini) = sesi terakhir Lejar Penuh (lejar/status.json), dan harga penilaian diambil hingga sesi itu sahaja
# (24 Okt 2026, audit item 6), supaya Lejar, harga dan posisi C satu vintaj.
#
# Sumber bukti setiap kaedah (varian aktif = katalog_kaedah.json varian_kod):
#   1. Backtest dalam sampel set 431 (data/registry_M_gabung.csv): asas jangkaan, DIPOTONG kerana dipilih atas data sama.
#   2. Tiga semakan luar sampel, setiap satu yang lulus menambah 25% kepercayaan pada angka backtest (asas 25%):
#      S1–S4 (registry; varian sama atasi EW dalam >= 3/4 subset), WFO W01 (WFO/data/hasil; luar sampel 2023–2026, CAGR > EW
#      423 tempoh sama) dan AUTOTUNE A01 (AUTOTUNE/hasil/papan.json; 2000 saham AS, luar sampel 2013–2024, CAGR > SPY dalam
#      kumpulan A dan B).
#   3. Data hadapan: Lejar Penuh (semua isyarat, seluruh alam Shariah) + kohort Papertrade C sebelum Lejar bermula (tidak
#      bertindih). Hanya posisi MATANG dikira (dibeli >= maks(14 hari, 1.5 x hari pegang backtest) lalu; tutup = untung akhir,
#      terbuka = untung semasa) supaya bias "tutup awal kebanyakannya kena henti" tidak masuk (sama seperti WFO/kod/analisis_sebenar.py).
#      Papertrade C selepas Lejar bermula = isyarat sama dengan Lejar, jadi dipapar sebagai semakan sahaja (tidak dikira dua kali).
#      Posisi Lejar yang isyaratnya jatuh semasa C pra-Lejar masih memegang kaedah+saham sama dibuang (enjin mengabaikan isyarat
#      itu), supaya laluan harga sama tidak dikira dua kali. Harga beli Lejar dilaras jika stor dilaras (split), seperti lejar.py.
# Skor (purata pulangan bersih setiap dagangan, %) = (n0 x jangkaan backtest dipotong + nb x purata matang) / (n0 + nb);
# julat 95% = skor ± 1.96 x SD / sqrt(n0 + nb), n0 = 1 / (1/N0 + 1/n backtest) (backtest kecil diberi berat kurang). Skor sebulan =
# skor / hari pegang backtest x 21. Swing = purata pegang backtest 3–30 hari.
# Kukuh (22 Okt 2026, kajian/KAJIAN_DATA_TERCEMAR.md R5–R7): nb = n berkesan = n / kesan reka bentuk berkelompok ikut hari beli (posisi hari sama bergerak bersama pasaran; < 5 hari beli
# berbeza -> nb = bilangan hari); BELUM CUKUP sehingga >= 10 hari beli berbeza; posisi melintas earnings dilapor berasingan.
# Purata penuh (22 Okt 2026, keputusan pengguna; Fasa 4 skor swing): skor dan status guna purata matang PENUH. Purata dipangkas
# 5% (R6) kekal dilapor (h_pangkas) sebagai semakan sahaja: kalibrasi_skor.py menunjukkan pangkas 5% menukar purata backtest 60
# daripada 75 kaedah swing menjadi negatif (untung swing datang daripada ekor kanan), dan jangkaan backtest pula tidak dipangkas.
# Pantau (22 Okt 2026, Fasa 4 item 15 laporan reports/Skor KPI pemilihan kaedah swing.md; lajur pantau, p_*): kohort = purata
# pulangan bersih lorong 1 posisi matang yang dibeli hari sama. BERSARA = P(mu <= 0) > 0.9 dengan >= 20 hari beli, atau >= 2 amaran
# CUSUM; GANTUNG = kejatuhan ekuiti kohort > 1.5 x maks backtest atau tempoh di bawah puncak > maks backtest (hari dagangan; kekal
# hingga semakan semula), atau (22 Okt 2026, brek ikut data hadapan) purata 20 kohort matang terakhir < persentil ke-5 purata bergulir
# 20 kohort backtest - (1 - kekal) x purata kohort backtest (bawah 5% jika kaedah berprestasi pada jangkaan); AMARAN = 1 amaran CUSUM bawah (k 0.5, h bootstrap ARL0 ~ 2 tahun; kohort diwinsor p5–p95 backtest,
# sasaran = purata winsor - (1 - kekal) x purata kohort backtest, dibahagi sd winsor); OK; BELUM CUKUP < 5 kohort matang.
# Parameter backtest: data/analisis/kalibrasi_skor.json 'pantau' (standard/kalibrasi_skor.py). Label sahaja: tiada order.
# Pantau v3 (24 Okt 2026, audit dashboard tab demi tab item 18): sasaran CUSUM = min(purata winsor, kekal x purata winsor)
# (winsor dengan winsor; dahulu purata winsor - (1 - kekal) x purata MENTAH, negatif bagi 68/75 kaedah swing); ambang GANTUNG
# bergulir = p5 purata bergulir 20 kohort DIWINSOR backtest - (purata winsor - sasaran), dibanding purata 20 kohort hadapan diwinsor;
# k CUSUM 0.25 dan h bootstrap blok bulanan (kalibrasi_skor.py v3); pengawal bukti minimum (>= 10 hari beli matang dan nb >= 10)
# disemak SEBELUM BERSARA/GANTUNG/AMARAN (dahulu BERSARA disemak dahulu: 4 kohort boleh BERSARA).
# Ranking tunggal (24 Okt 2026, audit item 6/16/17): kedudukan ikut skor sebulan TANPA bundar; setiap baris juga membawa
# p_top1/p_top5 dan selang pangkat 90% (Monte Carlo berbiji), lb_bulan (had bawah julat skor sebulan; susunan lalai halaman),
# meter bukti (g_matang/g_perlu, nb/nb_perlu, tarikh_sebenar), ditolak/lejar_n, ekor backtest (median_bt, pangkas5_bt, pct_top1),
# kelompok korelasi (kalibrasi_skor.json) dan teks pantau (pantau_sasaran, pantau_ambang); aras atas: fasa, label_semakan,
# gabungan_beku_nota. Formula: lihat fungsi peluang_pangkat(), nb_perlu(), tarikh_bukti(), kelompok_rows().
import argparse, glob, json, math, os, re
from datetime import datetime, timedelta, timezone
from fractions import Fraction

import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
BS2 = os.path.dirname(HERE)
REPO = os.path.dirname(BS2)
KATALOG = os.path.join(HERE, 'katalog_kaedah.json')
REGISTRY = os.path.join(BS2, 'data', 'registry_M_gabung.csv')
WFO_HASIL = os.path.join(REPO, 'WFO', 'data', 'hasil')
WFO_LAPORAN = os.path.join(REPO, 'WFO', 'laporan', 'W01_LAPORAN.md')
AUTOTUNE = os.path.join(REPO, 'AUTOTUNE', 'hasil', 'papan.json')
LEJAR = os.path.join(BS2, 'lejar')
PT = os.path.join(BS2, 'papertrade')
TERKINI = os.path.join(BS2, 'data', 'harga', 'terkini.csv')
STOR = os.path.join(BS2, 'data', 'harga', 'stor')
INDEKS = os.path.join(REPO, 'data_mentah', 'index_benchmark.csv')
SLOT = os.path.join(BS2, 'portfolio_slot')
OUT_MD = os.path.join(BS2, 'laporan', 'PENGANALISIS.md')
OUT_JSON = os.path.join(BS2, 'data', 'analisis', 'papan.json')

N0 = 30                 # berat maksimum backtest = 30 dagangan hadapan setara (dikurangkan jika dagangan backtest sedikit)
ASAS_KEKAL = 0.25       # pecahan jangkaan backtest dalam sampel yang dikekalkan tanpa semakan luar sampel lulus
TAMBAH_KEKAL = 0.25     # tambahan bagi setiap semakan luar sampel yang lulus (3 semakan -> 100%)
SWING = (3, 30)         # purata hari pegang backtest bagi kaedah swing (keputusan pengguna 20 Okt 2026)
N_MIN = 20              # posisi matang minimum sebelum status dinilai (tugasan_v3 §7: 20 dagangan)
N_AMARAN = 10           # posisi matang minimum bagi AMARAN awal
N_BT_MIN = 100          # dagangan backtest minimum untuk diberi nombor kedudukan (sampel kecil disusun di hujung)
UMUR_MIN = 14           # hari kalendar minimum sebelum posisi dikira matang
TOL_LARAS = 0.003       # sama dengan lejar.TOLERANSI_LARAS: buka stor hari beli lain daripada harga beli -> stor dilaras
TOL_LARAS_C = 0.2       # Papertrade C (harga Moomoo lawan stor yfinance): hanya split jelas dilaras
SD_MIN = 5.0            # SD minimum setiap dagangan (%)
PANGKAS = 0.05          # pecahan dipangkas setiap hujung (purata dipangkas: semakan sahaja sejak 22 Okt 2026)
KALIBRASI = os.path.join(BS2, 'data', 'analisis', 'kalibrasi_skor.json')
PANTAU_DD = 1.5         # GANTUNG: kejatuhan ekuiti kohort > 1.5 x maks backtest (Davey 1.2–1.5x)
PANTAU_P = 0.9          # BERSARA: P(mu <= 0) > 0.9 ...
PANTAU_G = 20           # ... dengan >= 20 hari beli matang
PANTAU_KOHORT = 10      # kohort (hari beli) matang minimum sebelum pantau dinilai (pengawal bukti; dahulu 5)
NB_MIN = 10             # n berkesan minimum: pengawal bukti pantau/AMARAN dan lantai nb_perlu
CUSUM_K = 0.25          # lalai jika kalibrasi tiada 'k' (kalibrasi_skor.py v3)
MC_CABUTAN = 20000      # cabutan Monte Carlo peluang pangkat
MC_BIJI = 20261024      # biji Monte Carlo (keputusan boleh diulang)
TOP_N = 5               # p_top5
Z95 = 1.96
GABUNGAN_BEKU = os.path.join(BS2, 'data', 'analisis', 'gabungan_beku.json')
LABEL_SEMAKAN = dict(s14='S1–S4 = kestabilan dalam sampel (subset 431 saham, tempoh sama)',
                     wfo='WFO = dalam tempoh pemilihan, versi ditala',
                     at='AUTOTUNE = 2000 saham AS lain (satu-satunya ujian bebas)')
PANTAU_BERGULIR = 20    # GANTUNG hadapan: purata N kohort matang terakhir lawan p5 purata bergulir N kohort backtest
PANTAU_STATUS = ['BERSARA', 'GANTUNG', 'AMARAN', 'OK', 'BELUM CUKUP']
N_HARI_MIN = 10         # hari beli berbeza minimum sebelum status dinilai (R5)
HARI_KLUSTER_MIN = 5    # < 5 hari beli berbeza: n berkesan = bilangan hari (anggaran kesan reka bentuk tidak stabil)
TV = os.path.join(BS2, 'data', 'skrin', 'tv_us.csv')
PENDAPATAN = os.path.join(BS2, 'data', 'pemangkin', 'tarikh_pendapatan.csv')
KOS = 0.001             # kos enjin v1.2 setiap belah
HARI_BULAN = 21
TEMPOH_IS = ('2019-11-01', '2026-10-02')
STATUS = ['KUAT', 'PERHATI', 'LEMAH', 'AMARAN', 'BELUM CUKUP']
B = lambda v: str(v).strip().lower() == 'true'


def nombor(x):
    try:
        v = float(x)
    except (TypeError, ValueError):
        return None
    return None if math.isnan(v) or math.isinf(v) else v


def bulat(x, p=2):
    v = nombor(x)
    return None if v is None else round(v, p)


def bersih(untung_pct):
    """Untung kasar % -> pulangan bersih % dengan kos enjin v1.2 (0.1% setiap belah), sama seperti registry."""
    return ((1 + untung_pct / 100) * (1 - KOS) / (1 + KOS) - 1) * 100


def umur_matang(hari_bt):
    """Hari kalendar sebelum posisi dikira matang: maks(14, 1.5 x hari dagangan pegang backtest x 7/5)."""
    h = nombor(hari_bt) or 10
    return max(UMUR_MIN, int(math.ceil(1.5 * h * 7 / 5)))


# ---------------------------------------------------------------- backtest
def muat_katalog(path=KATALOG):
    return [(r['id'], r.get('nama', ''), r.get('varian_kod') or r.get('varian', '')) for r in json.load(open(path, encoding='utf-8'))['rows']]


def muat_registry(varian, path=REGISTRY):
    """{id: dict(baris 431 varian aktif + subset_menang)}; subset_menang = bil. subset S1–S4 (varian sama) yang atasi EW."""
    r = pd.read_csv(path)
    r = r[[varian.get(i) == v for i, v in zip(r['id'], r['varian'])]]
    out = {}
    for mid, g in r.groupby('id'):
        a = g[g['set'].astype(str) == '431']
        if not len(a):
            continue
        x = a.iloc[0]
        s = g[g['set'].astype(str).isin(['S1', 'S2', 'S3', 'S4'])]
        out[mid] = dict(keputusan=x['keputusan'], skor=nombor(x['skor']), cagr=nombor(x['cagr']), mdd=nombor(x['mdd']),
                        win=nombor(x['win']), avg=nombor(x['avg']), avgwin=nombor(x['avgwin']), avgloss=nombor(x['avgloss']),
                        days=nombor(x['days']), n=int(x['n']) if nombor(x['n']) is not None else 0, hit10=nombor(x['hit10']),
                        setahun=nombor(x['dagangan_setahun']),
                        ew=nombor(x['ew_cagr']), subset_n=int(len(s)),
                        subset_menang=int(sum(B(v) for v in s['menang_ew'])))
    return out


def sd_backtest(r):
    """SD pulangan setiap dagangan (%) daripada kadar menang, purata menang dan purata rugi (anggaran bawah; min SD_MIN)."""
    w, aw, al, av = (r.get(k) for k in ('win', 'avgwin', 'avgloss', 'avg'))
    if None in (w, aw, al, av):
        return SD_MIN
    v = w * aw ** 2 + (1 - w) * al ** 2 - av ** 2
    return max(SD_MIN, math.sqrt(max(v, 0)) * 100)


def muat_wfo(hasil=WFO_HASIL, laporan=WFO_LAPORAN):
    """{id: dict(cagr, mdd, win, avg, hari, n, ew, dsr, keputusan)} — WFO luar sampel 2023–2026 (W01)."""
    lap = {}
    if os.path.exists(laporan):
        for l in open(laporan, encoding='utf-8'):
            c = [x.strip() for x in l.strip().strip('|').split('|')]
            if len(c) == 14 and c[0].isdigit() and re.fullmatch(r'M\d+', c[1]):
                lap[c[1]] = dict(dsr=nombor(c[12]), keputusan=c[13])
    out = {}
    for f in glob.glob(os.path.join(hasil, 'M*.json')):
        h = json.load(open(f, encoding='utf-8'))
        if h.get('status') != 'SIAP':
            continue
        o = h.get('oos') or {}
        out[h['id']] = dict(cagr=nombor(o.get('cagr')), mdd=nombor(o.get('mdd')), win=nombor(o.get('win')), avg=nombor(o.get('avg')),
                            hari=nombor(o.get('hari')), n=int(o.get('n') or 0), ew=nombor((h.get('ew') or {}).get('cagr')),
                            spy=nombor((h.get('spy') or {}).get('cagr')), **lap.get(h['id'], dict(dsr=None, keputusan='')))
    return out


def muat_autotune(path=AUTOTUNE):
    """{id: dict(label, cagr_a, spy_a, cagr_b, spy_b, cagr_kunci, spy_kunci, dsr, pbo)} — 2000 saham AS (A01)."""
    if not os.path.exists(path):
        return {}
    k = ('label', 'cagr_a', 'spy_a', 'mdd_a', 'cagr_b', 'spy_b', 'cagr_kunci', 'spy_kunci', 'dsr', 'pbo')
    return {r['id']: {x: r.get(x) for x in k} for r in json.load(open(path, encoding='utf-8')).get('kaedah', [])}


def semakan(reg, wfo, at):
    """Tiga semakan luar sampel: (subset, wfo, autotune) masing-masing True/False/None (tiada data)."""
    s = (reg['subset_menang'] >= 3) if reg and reg.get('subset_n') else None
    w = (wfo['cagr'] > wfo['ew']) if wfo and wfo.get('cagr') is not None and wfo.get('ew') is not None else None
    a = None
    if at and None not in (nombor(at.get('cagr_a')), nombor(at.get('spy_a')), nombor(at.get('cagr_b')), nombor(at.get('spy_b'))):
        a = at['cagr_a'] > at['spy_a'] and at['cagr_b'] > at['spy_b']
    return s, w, a


# ---------------------------------------------------------------- hadapan
def harga_akhir(path=TERKINI, stor=STOR, hingga=None):
    """{ticker: tutup terakhir} dan tarikh data terkini (YYYY-MM-DD): data/harga/terkini.csv, dan bagi saham yang tiada di
    situ, stor harga repo (harga_A/B.csv, sumber yang dipakai Lejar Penuh) hingga tarikh sama. hingga (YYYY-MM-DD, cth. sesi
    terakhir Lejar): bar selepas tarikh itu diabaikan, supaya harga satu vintaj dengan Lejar."""
    h = hingga.replace('-', '') if hingga else None
    d = [pd.read_csv(path, usecols=['ticker', 'date', 'close'], dtype={'date': str})] if os.path.exists(path) else []
    if d and h:
        d[0] = d[0][d[0].date <= h]
    t = d[0]['date'].max() if d and len(d[0]) else None
    ada = set(d[0].ticker) if d else set()
    for nm in ('harga_A.csv', 'harga_B.csv'):
        f = os.path.join(stor, nm)
        if os.path.exists(f):
            x = pd.read_csv(f, usecols=['ticker', 'date', 'close'], dtype={'date': str})
            x = x[~x.ticker.isin(ada)]
            if t or h:
                x = x[x.date <= (t or h)]
            d.append(x)
    if not d:
        return {}, None
    d = pd.concat(d, ignore_index=True).sort_values(['ticker', 'date'])
    if not len(d):
        return {}, None
    t = t or d['date'].max()
    akhir = d.groupby('ticker').tail(1)
    return dict(zip(akhir.ticker, akhir.close.astype(float))), f'{t[:4]}-{t[4:6]}-{t[6:8]}'


LAJUR_POS = ['id', 'saham', 'tarikh_isyarat', 'tarikh_beli', 'tarikh_keluar', 'tutup1', 'hasil1', 'hasil2', 'sumber']


def buka_stor(saham, stor=STOR):
    """{(ticker, 'YYYY-MM-DD'): harga buka} daripada stor harga repo bagi saham diberi (untuk semakan laras split)."""
    out, saham = {}, set(saham)
    for nm in ('harga_A.csv', 'harga_B.csv'):
        f = os.path.join(stor, nm)
        if not saham or not os.path.exists(f):
            continue
        x = pd.read_csv(f, usecols=['ticker', 'date', 'open'], dtype={'date': str})
        x = x[x.ticker.isin(saham)]
        out.update({(t, f'{d[:4]}-{d[4:6]}-{d[6:8]}'): float(o) for t, d, o in zip(x.ticker, x.date, x.open)})
    return out


def laras_beli(hb, saham, tarikh_beli, buka, tol):
    """Harga beli pada skala stor semasa: jika buka stor hari beli berbeza > tol daripada harga beli (stor dilaras selepas
    split), harga beli didarab nisbah sama seperti lejar.py kerja(); jika tiada bar, harga beli asal."""
    ob = buka.get((saham, tarikh_beli))
    return ob if hb and ob and abs(ob / hb - 1) > tol else hb


def muat_lejar(akhir, lejar=LEJAR, buka=None):
    """Posisi Lejar Penuh: id, saham, tarikh_isyarat, tarikh_beli, tarikh_keluar, tutup1, hasil1 (bersih %), hasil2 (lorong 2,
    bersih %). Posisi terbuka dinilai pada tutup terakhir dengan harga beli dilaras jika stor dilaras (split)."""
    f = sorted(glob.glob(os.path.join(lejar, 'tutup', '*.csv'))) + [os.path.join(lejar, 'terbuka.csv')]
    d = [pd.read_csv(p, dtype=str, keep_default_na=False) for p in f if os.path.exists(p)]
    if not d:
        return pd.DataFrame(columns=LAJUR_POS)
    d = pd.concat(d, ignore_index=True)
    buka = buka if buka is not None else buka_stor(d.saham.unique())
    rows = []
    for r in d.itertuples(index=False):
        hb = laras_beli(nombor(r.harga_beli), r.saham, r.tarikh_beli, buka, TOL_LARAS)
        kini = akhir.get(r.saham)
        semasa = (kini / hb - 1) * 100 if hb and kini else None
        t1 = r.tarikh_keluar != ''
        h1 = (nombor(r.pulangan) * 100 if nombor(r.pulangan) is not None else bersih(nombor(r.untung_pct))) if t1 else \
            (bersih(semasa) if semasa is not None else None)
        g2 = nombor(r.untung_henti_pct) if B(r.keluar_henti) else semasa
        rows.append(dict(id=r.id_kaedah, saham=r.saham, tarikh_isyarat=r.tarikh_isyarat, tarikh_beli=r.tarikh_beli,
                         tarikh_keluar=r.tarikh_keluar, tutup1=t1, hasil1=h1, hasil2=bersih(g2) if g2 is not None else None,
                         sumber='lejar'))
    return pd.DataFrame(rows, columns=LAJUR_POS)


def muat_c(pt=PT, akhir=None, buka=None):
    """Posisi sah Papertrade C (semua claude*.csv): lajur LAJUR_POS. Lorong 1 = untung C (akhir jika keluar; jika dipegang,
    dinilai pada tutup terakhir `akhir` (harga hingga sesi Lejar, satu vintaj dengan Lejar), atau untung semasa C jika tiada
    harga). Lorong 2 yang masih dipegang dinilai pada tutup terakhir (akhir)."""
    f = sorted(glob.glob(os.path.join(pt, 'claude*.csv')))
    if not f:
        return pd.DataFrame(columns=LAJUR_POS)
    d = pd.concat([pd.read_csv(p, dtype=str, keep_default_na=False) for p in f], ignore_index=True)
    for k in ('tidak_sah', 'tidak_dibeli', 'keluar_henti'):
        d[k] = d[k].map(B) if k in d else False
    d = d[~d.tidak_sah & ~d.tidak_dibeli & (d.harga_beli != '') & (d.tarikh_beli != '')]
    akhir = akhir or {}
    buka = buka if buka is not None else (buka_stor(d.saham.unique()) if akhir else {})
    rows = []
    for r in d.itertuples(index=False):
        t1 = B(r.keluar)
        hb = laras_beli(nombor(r.harga_beli), r.saham, r.tarikh_beli, buka, TOL_LARAS_C)
        kini = akhir.get(r.saham)
        semasa = (kini / hb - 1) * 100 if hb and kini else None
        g = nombor(r.untung_akhir_pct) if t1 else (semasa if semasa is not None else nombor(r.untung_pct))
        if r.keluar_henti:
            g2 = nombor(getattr(r, 'untung_henti_pct', None))
        elif not t1:
            g2 = g
        else:   # lorong 1 sudah keluar (harga_terkini beku), lorong 2 masih dipegang
            g2 = semasa
        rows.append(dict(id=r.id_kaedah or r.kaedah, saham=r.saham, tarikh_isyarat=getattr(r, 'tarikh_isyarat', ''), tarikh_beli=r.tarikh_beli,
                         tarikh_keluar=r.tarikh_keluar if t1 else '', tutup1=t1, hasil1=bersih(g) if g is not None else None,
                         hasil2=bersih(g2) if g2 is not None else None, sumber='C'))
    return pd.DataFrame(rows, columns=LAJUR_POS)


def gabung_hadapan(L, C):
    """Bukti hadapan = Lejar Penuh + kohort C sebelum belian pertama Lejar (C selepas itu = isyarat sama; semakan sahaja).
    Posisi Lejar yang isyaratnya jatuh semasa posisi C pra-Lejar kaedah+saham sama masih dipegang dalam lorong 1 (termasuk hari
    lorong 1 keluar) dibuang: enjin mengabaikan isyarat itu, jadi laluan harga sama tidak dikira dua kali.
    -> (gabungan, tarikh belian pertama Lejar, bilangan posisi Lejar dibuang)"""
    mula = L.tarikh_beli.min() if len(L) else None
    pra = C[C.tarikh_beli < mula] if mula else C
    pegang = {}
    for r in pra.itertuples(index=False):
        pegang.setdefault((r.id, r.saham), []).append((r.tarikh_beli, r.tarikh_keluar))
    tindih = [any(tb <= ti and (tk == '' or tk >= ti) for tb, tk in pegang.get((i, s), ()))
              for i, s, ti in zip(L.id, L.saham, L.tarikh_isyarat)] if len(L) else []
    L2 = L[[not x for x in tindih]] if len(L) else L
    return pd.concat([L2, pra], ignore_index=True), mula, int(sum(tindih))


def purata_pangkas(x, p=PANGKAS):
    """Purata selepas membuang pecahan p terendah dan tertinggi (tiada pangkas jika n < 1/p)."""
    s = np.sort(np.asarray(x, float)); k = int(len(s) * p)
    return float(s[k:len(s) - k].mean()) if len(s) > 2 * k else float(s.mean())


def n_berkesan(x, kump):
    """n berkesan = n / kesan reka bentuk (varians berkelompok ikut kump ÷ varians bebas), maks n. Kurang daripada
    HARI_KLUSTER_MIN kelompok: bilangan kelompok (konservatif)."""
    x = np.asarray(x, float); n = len(x); g = pd.Series(x - x.mean()).groupby(np.asarray(kump)).sum()
    G = len(g)
    if n < 2 or G < HARI_KLUSTER_MIN:
        return float(min(n, G))
    v_bebas = x.var(ddof=1) / n
    v_klus = G / (G - 1) * float((g ** 2).sum()) / n ** 2
    if v_bebas <= 0:
        return float(G)
    return float(min(n, n / max(v_klus / v_bebas, 1.0)))


def muat_earnings(tv=TV, sejarah=PENDAPATAN):
    """{ticker: [tarikh sesi kesan earnings]}: TradingView (laporan terakhir dan seterusnya, cap masa UTC) + sejarah Nasdaq/SST.
    Laporan selepas 16:00 NY -> kesan pada sesi berikutnya (hari kalendar berikutnya; hujung minggu ditangani oleh perbandingan julat)."""
    out = {}
    if os.path.exists(tv):
        t = pd.read_csv(tv, usecols=['ticker', 'earnings_release_date', 'earnings_release_next_date'], dtype=str)
        for c in ('earnings_release_date', 'earnings_release_next_date'):
            ts = pd.to_datetime(pd.to_numeric(t[c], errors='coerce'), unit='s', utc=True).dt.tz_convert('America/New_York')
            d = ts.dt.normalize() + pd.to_timedelta((ts.dt.hour >= 16).astype(int), unit='D')
            for k, v in zip(t.ticker, d):
                if pd.notna(v):
                    out.setdefault(k, set()).add(str(v.date()))
    if os.path.exists(sejarah):
        s = pd.read_csv(sejarah, dtype=str)
        for k, v in zip(s.ticker, s.d0):
            out.setdefault(k, set()).add(v)
    return {k: sorted(v) for k, v in out.items()}


def lintas_earnings(P, earnings, kini):
    """Siri boolean: posisi memegang saham melalui tarikh kesan earnings (tarikh_beli < kesan <= tarikh keluar atau kini)."""
    if not earnings or not len(P):
        return pd.Series(False, index=P.index)
    akhir = P.tarikh_keluar.where(P.tarikh_keluar != '', str(kini))
    return pd.Series([any(b < e <= a for e in earnings.get(t, ())) for t, b, a in zip(P.saham, P.tarikh_beli, akhir)], index=P.index)


def ringkas_hadapan(P, hari_bt, kini, earnings=None):
    """Statistik hadapan satu kaedah: semua posisi, posisi matang (bukti: purata, purata dipangkas, median, n berkesan ikut hari
    beli, hari beli berbeza, lintas earnings), lorong 2 matang dan tarikh 20 posisi matang."""
    umur = umur_matang(hari_bt)
    out = dict(posisi=int(len(P)), tutup=int(P.tutup1.sum()) if len(P) else 0, umur_hari=umur,
               matang=0, purata=None, menang=None, sd=None, purata_l2=None, matang_mula=None, matang_20=None,
               pangkas=None, median=None, n_berkesan=0.0, hari_beli=0, lintas_earnings=0, purata_tanpa_earnings=None)
    if not len(P):
        return out
    tb = pd.to_datetime(P.tarikh_beli)
    had = pd.Timestamp(kini) - pd.Timedelta(days=umur)
    M = P[(tb <= had).values & P.hasil1.notna().values]
    s = sorted(tb)
    out['matang_mula'] = str((s[0] + pd.Timedelta(days=umur)).date())
    if len(s) >= N_MIN:
        out['matang_20'] = str((s[N_MIN - 1] + pd.Timedelta(days=umur)).date())
    if len(M):
        x = M.hasil1.astype(float)
        le = lintas_earnings(M, earnings, kini)
        out.update(matang=int(len(M)), purata=float(x.mean()), menang=float((x > 0).mean()),
                   sd=float(x.std(ddof=1)) if len(M) > 1 else None, pangkas=purata_pangkas(x), median=float(x.median()),
                   n_berkesan=n_berkesan(x.values, M.tarikh_beli.values), hari_beli=int(M.tarikh_beli.nunique()),
                   lintas_earnings=int(le.sum()), purata_tanpa_earnings=float(x[~le.values].mean()) if (~le).any() else None)
        y = M.hasil2.dropna().astype(float)
        out['purata_l2'] = float(y.mean()) if len(y) else None
    return out


# ---------------------------------------------------------------- pantau
def muat_kalibrasi(path=KALIBRASI, semua=False):
    """({id: parameter pantau backtest}, k CUSUM); tiada fail -> ({}, CUSUM_K). semua=True: juga {id: baris kalibrasi penuh}
    (ekor dagangan, kelompok korelasi) sebagai unsur ketiga."""
    try:
        d = json.load(open(path, encoding='utf-8'))
    except (OSError, ValueError):
        return ({}, CUSUM_K, {}) if semua else ({}, CUSUM_K)
    kal = {m: r['pantau'] for m, r in d.get('kaedah', {}).items() if r.get('pantau')}
    k = (d.get('pantau') or {}).get('k', CUSUM_K)
    return (kal, k, d.get('kaedah', {})) if semua else (kal, k)


def phi(z):
    return 0.5 * (1 + math.erf(z / math.sqrt(2)))


def sasaran_cusum(kal, kekal):
    """Sasaran kohort CUSUM (skala winsor): purata winsor backtest dipotong ikut kekal (winsor dengan winsor). Potongan hanya
    menurunkan sasaran: min(purata winsor, kekal x purata winsor)."""
    m = kal['mu_winsor']
    return min(m, kekal * m)


def teks_pantau(kal, kekal, k=CUSUM_K):
    """(pantau_sasaran, pantau_ambang) sebagai teks % yang boleh dibaca; (None, None) tanpa kalibrasi."""
    if not kal:
        return None, None
    sas = sasaran_cusum(kal, kekal); sd = max(kal['sd_winsor'], 1e-6); lo = kal['winsor'][0]
    p5 = kal.get('p5_bergulir_winsor', kal.get('p5_bergulir'))
    n = int(kal.get('n_bergulir', PANTAU_BERGULIR))
    sasaran = f"{sas:+.2f}% setiap hari beli" + (' (negatif: ekor kanan)' if sas < 0 else '')
    bah = []
    if p5 is not None:
        bah.append(f"GANTUNG: purata {n} hari beli < {p5 - (kal['mu_winsor'] - sas):+.2f}%")
    if kal.get('arl_bootstrap', 1) is None:
        bah.append('CUSUM tidak aktif')
    else:   # paras kohort yang, jika berulang 10 hari beli berturut, mencetus amaran CUSUM (S naik (sas - x) / sd - k sehari)
        x10 = sas - sd * (k + kal['h'] / 10)
        if x10 >= lo:
            bah.append(f"AMARAN: 10 hari beli berturut ≤ {x10:+.2f}%")
        else:
            d = (sas - lo) / sd - k
            bah.append(f"AMARAN: {math.ceil(kal['h'] / d) if d > 0 else '∞'} hari beli berturut ≤ {lo:+.2f}%")
    return sasaran, '; '.join(bah)


def pantau_kaedah(P, umur, kini, kal, kekal, mu, lo, hi, hari_beli, k=CUSUM_K, nb=None):
    """Status pantau satu kaedah daripada posisi hadapan P (lorong 1, hasil1 bersih) dan parameter backtest kal (atau None).
    Pengawal bukti dahulu: < PANTAU_KOHORT hari beli matang atau n berkesan < NB_MIN -> BELUM CUKUP (pencetus yang sudah
    dikira dilapor dalam p_sebab sebagai 'belum dinilai'); kemudian BERSARA, GANTUNG, AMARAN, OK."""
    se = (hi - mu) / Z95 if hi is not None and mu is not None else None
    p_rugi = phi(-mu / se) if se and se > 0 else None
    out = dict(pantau='BELUM CUKUP', p_rugi=bulat(p_rugi, 3), p_kohort=0, p_dd=None, p_dd_had=None, p_dd_tempoh=None,
               p_dd_tempoh_had=None, p_bergulir=None, p_bergulir_had=None, p_cusum=None, p_h=None, p_amaran=0, p_sebab='')
    if len(P):
        tb = pd.to_datetime(P.tarikh_beli)
        M = P[(tb <= pd.Timestamp(kini) - pd.Timedelta(days=umur)).values & P.hasil1.notna().values]
    else:
        M = P
    c = M.groupby('tarikh_beli').hasil1.mean().astype(float).sort_index() if len(M) else pd.Series(dtype=float)
    out['p_kohort'] = int(len(c))
    if nb is None:
        nb = n_berkesan(M.hasil1.astype(float).values, M.tarikh_beli.values) if len(M) else 0.0
    sebab = []
    if len(c) and kal:
        eq = c.cumsum().values; pk = np.maximum.accumulate(np.maximum(eq, 0.0))
        out['p_dd'] = bulat(float((pk - eq).max()), 2); out['p_dd_had'] = bulat(PANTAU_DD * kal['dd_maks'], 2)
        hari = np.array(c.index, dtype='datetime64[D]'); t_pk = hari[0]; tinggi = 0.0; lama = 0
        for t, v in zip(hari, eq):
            if v >= tinggi:
                tinggi, t_pk = v, t
            lama = max(lama, int(np.busday_count(t_pk, t)))
        if eq[-1] < tinggi:
            lama = max(lama, int(np.busday_count(t_pk, np.datetime64(str(kini)[:10], 'D'))))
        out['p_dd_tempoh'] = lama; out['p_dd_tempoh_had'] = int(kal['dd_tempoh'])
        # CUSUM bawah atas kohort diwinsor, sasaran winsor dipotong (winsor dengan winsor); hanya jika bootstrap backtest boleh
        # beramaran (taburan kohort sangat condong ke kanan: z bawah tidak melepasi k)
        sasaran = sasaran_cusum(kal, kekal)
        cw = np.clip(c.values, *kal['winsor'])
        z = (cw - sasaran) / max(kal['sd_winsor'], 1e-6)
        if kal.get('arl_bootstrap', 1) is not None:
            S = 0.0; n = 0
            for v in z:
                S = max(0.0, S - v - k)
                if S > kal['h']:
                    n += 1; S = 0.0
            out.update(p_cusum=bulat(S, 2), p_h=kal['h'], p_amaran=n)
        if out['p_dd'] > out['p_dd_had']:
            sebab.append(f"kejatuhan {out['p_dd']:.1f} > {out['p_dd_had']:.1f}")
        if lama > kal['dd_tempoh']:
            sebab.append(f"tempoh di bawah puncak {lama} > {int(kal['dd_tempoh'])} hari")
        n = int(kal.get('n_bergulir', PANTAU_BERGULIR))
        p5 = kal.get('p5_bergulir_winsor', kal.get('p5_bergulir'))
        if p5 is not None and len(c) >= n:
            out['p_bergulir'] = bulat(float(cw[-n:].mean()), 2)
            out['p_bergulir_had'] = bulat(p5 - (kal['mu_winsor'] - sasaran), 2)
            if out['p_bergulir'] < out['p_bergulir_had']:
                sebab.append(f"purata {n} hari beli {out['p_bergulir']:+.2f}% < p5 backtest {out['p_bergulir_had']:+.2f}%")
    p_bersara = p_rugi is not None and p_rugi > PANTAU_P and hari_beli >= PANTAU_G
    if p_bersara:
        sebab.insert(0, f"P(purata ≤ 0) {p_rugi:.2f} > {PANTAU_P}")
    if out['p_amaran']:
        sebab.insert(0, f"{out['p_amaran']} amaran CUSUM")
    if len(c) < PANTAU_KOHORT or nb < NB_MIN:   # pengawal bukti minimum SEBELUM BERSARA/GANTUNG/AMARAN
        out['pantau'] = 'BELUM CUKUP'
        if sebab:
            sebab.insert(0, f"belum dinilai ({len(c)} hari beli matang, nb {nb:.1f}; perlu ≥ {PANTAU_KOHORT} dan nb ≥ {NB_MIN})")
    elif p_bersara or out['p_amaran'] >= 2:
        out['pantau'] = 'BERSARA'
    elif any(x.startswith(('kejatuhan', 'tempoh', 'purata ')) for x in sebab):
        out['pantau'] = 'GANTUNG'
    elif out['p_amaran']:
        out['pantau'] = 'AMARAN'
    else:
        out['pantau'] = 'OK'
    out['p_sebab'] = '; '.join(sebab)
    return out


# ---------------------------------------------------------------- skor
def berat_backtest(n_bt):
    """n0 = 1 / (1/N0 + 1/n backtest): varians jangkaan = ketidakpastian model (N0) + ralat sampel backtest (n backtest)."""
    return N0 * n_bt / (N0 + n_bt) if n_bt and n_bt > 0 else 1.0


def skor(mu0, sd0, n, xbar, sdf, n0=N0):
    """Pengecutan normal–normal: (n0 x mu0 + n x xbar) / (n0 + n); SD = SD hadapan jika n >= N_MIN, jika tidak SD backtest;
    kedua-duanya minimum SD_MIN."""
    s = sdf if (n >= N_MIN and sdf) else sd0
    s = max(SD_MIN, s or SD_MIN)
    mu = mu0 if not n else (n0 * mu0 + n * xbar) / (n0 + n)
    se = s / math.sqrt(n0 + n)
    return mu, mu - 1.96 * se, mu + 1.96 * se


def status_kaedah(n, xbar, sdf, mu0, lo, hi, hari=None, nb=None):
    """AMARAN: >= 10 matang, >= 10 hari beli berbeza, nb >= NB_MIN dan purata matang di bawah jangkaan (t < -2, ralat piawai
    ikut n berkesan nb jika diberi). BELUM CUKUP: < 20 matang atau < 10 hari beli berbeza (hari). KUAT: julat 95% skor > 0. LEMAH: julat 95% skor < 0.
    Selainnya PERHATI."""
    nb = n if nb is None else nb
    cukup = nb >= NB_MIN and (hari is None or hari >= N_HARI_MIN)   # pengawal bukti minimum sebelum AMARAN (24 Okt 2026)
    if n >= N_AMARAN and cukup and sdf and sdf > 0 and (xbar - mu0) / (sdf / math.sqrt(nb)) < -2:
        return 'AMARAN'
    if n < N_MIN or (hari is not None and hari < N_HARI_MIN):
        return 'BELUM CUKUP'
    return 'KUAT' if lo > 0 else 'LEMAH' if hi < 0 else 'PERHATI'


# ---------------------------------------------------------------- ranking tunggal (24 Okt 2026, audit item 6/16/17)
def susun_kedudukan(rows):
    """Kedudukan: kaedah swing dengan >= N_BT_MIN dagangan backtest ikut skor sebulan TANPA bundar (_kb; dahulu nilai dibundar 2
    tempat perpuluhan, jadi seri disusun ikut katalog), kemudian swing sampel kecil dan bukan swing (tanpa nombor). Susunan
    stabil. -> (swing berkedudukan, swing sampel kecil, bukan swing)."""
    k = lambda r: -(r['_kb'] if r['_kb'] is not None else -1e9)
    for r in rows:
        r['sampel_kecil'] = (r['bt_n'] or 0) < N_BT_MIN
    sw = sorted([r for r in rows if r['swing'] and not r['sampel_kecil']], key=k)
    kecil = sorted([r for r in rows if r['swing'] and r['sampel_kecil']], key=k)
    lain = sorted([r for r in rows if not r['swing']], key=k)
    for i, r in enumerate(sw, 1):
        r['kedudukan'] = i
    for r in kecil + lain:
        r['kedudukan'] = None
    return sw, kecil, lain


def peluang_pangkat(mu, se, cabutan=MC_CABUTAN, biji=MC_BIJI, top=TOP_N):
    """Monte Carlo pangkat: skor sebulan setiap kaedah ~ Normal(mu, se) secara bebas, se = (had atas julat 95% - skor) / 1.96;
    cabutan berbiji (boleh diulang); pangkat 1 = tertinggi. -> (P(pangkat 1), P(pangkat <= top), persentil ke-5 dan ke-95
    pangkat = selang pangkat 90%) setiap kaedah. Korelasi antara kaedah diabaikan (anggaran)."""
    mu = np.asarray(mu, float); se = np.maximum(np.asarray(se, float), 1e-9); n = len(mu)
    if not n:
        return np.zeros(0), np.zeros(0), np.zeros(0, int), np.zeros(0, int)
    X = np.random.default_rng(biji).normal(mu, se, size=(cabutan, n))
    pangkat = np.empty((cabutan, n), dtype=np.int32)
    pangkat[np.arange(cabutan)[:, None], np.argsort(-X, axis=1)] = np.arange(1, n + 1, dtype=np.int32)
    q = np.quantile(pangkat, [0.05, 0.95], axis=0, method='inverted_cdf')
    return (pangkat == 1).mean(0), (pangkat <= top).mean(0), q[0].astype(int), q[1].astype(int)


def nb_perlu(mu0, sd, n0):
    """n berkesan hadapan yang diperlukan untuk BUKTI: julat 95% skor tidak merangkumi 0 jika purata hadapan = jangkaan dipotong
    mu0, iaitu |mu0| - 1.96 x SD / sqrt(n0 + nb) > 0 -> nb = (1.96 x SD / |mu0|)^2 - n0 (SD seperti skor(): hadapan jika
    >= 20 matang, jika tidak backtest; min SD_MIN). Lantai NB_MIN (pengawal bukti minimum; keluar BELUM CUKUP pula perlu
    >= 20 matang dan >= 10 hari beli: g_matang/g_perlu dan tarikh_sebenar). None jika mu0 = 0."""
    if not mu0:
        return None
    return int(max(NB_MIN, math.ceil((Z95 * max(SD_MIN, sd or SD_MIN) / abs(mu0)) ** 2 - n0)))


def sesi_nyse(mula, akhir):
    """Sesi NYSE mula..akhir (inklusif), 'YYYY-MM-DD': exchange_calendars XNYS (dipin kekangan.txt); di luar julat kalendar
    atau tanpa pakej -> hari bekerja Isn–Jum."""
    t0, t1 = pd.Timestamp(mula), pd.Timestamp(akhir)
    out = []
    try:
        import exchange_calendars as xc
        c = xc.get_calendar('XNYS')
        a, b = max(t0, c.first_session), min(t1, c.last_session)
        if a <= b:
            out = [str(d.date()) for d in c.sessions_in_range(a, b)]
    except (ImportError, ValueError, KeyError):
        out = []
    mula_bd = pd.Timestamp(out[-1]) + pd.Timedelta(days=1) if out else t0
    return out + [str(d.date()) for d in pd.bdate_range(mula_bd, t1)]


def tarikh_bukti(beli, umur, kadar, sehari, depan, sesi, n_min=N_MIN, g_min=N_HARI_MIN):
    """Anggaran sesi pertama kaedah boleh keluar BELUM CUKUP (>= n_min posisi matang DAN >= g_min hari beli berbeza matang).
    beli = {tarikh beli: bilangan posisi} (sedia ada + belian tertunda Lejar); kadar = pecahan sesi isyarat dengan belian
    (Fraction; Lejar Penuh); sehari = posisi setiap hari beli (Fraction); depan = sesi akan datang selepas tarikh beli terakhir
    yang diketahui; sesi = semua sesi NYSE (rujukan matang). Hari beli ke-j akan datang = depan[ceil(j / kadar) - 1]; tarikh =
    sesi pertama >= tarikh beli hari beli syarat + umur hari kalendar (takrif matang). None jika kadar 0 atau di luar kalendar."""
    n = g = 0; Bt = None
    for t in sorted(beli):
        n += beli[t]; g += 1
        if n >= n_min and g >= g_min:
            Bt = t; break
    if Bt is None:
        if not kadar or not sehari:
            return None
        k = max(g_min - g, math.ceil(Fraction(n_min - n) / sehari), 1)
        i = math.ceil(Fraction(k) / kadar) - 1
        if i >= len(depan):
            return None
        Bt = depan[i]
    t = str((pd.Timestamp(Bt) + pd.Timedelta(days=umur)).date())
    return next((x for x in sesi if x >= t), None)


def muat_isyarat_lejar(lejar=LEJAR):
    """(sesi isyarat Lejar [YYYY-MM-DD], belian tertunda DataFrame id/tarikh_isyarat bagi sesi terakhir) daripada status.json
    dan tunggu.csv."""
    try:
        st = json.load(open(os.path.join(lejar, 'status.json'), encoding='utf-8'))
    except (OSError, ValueError):
        st = {}
    sesi = sorted({x.get('sesi') for x in st.get('larian', []) if x.get('sesi')})
    f = os.path.join(lejar, 'tunggu.csv')
    T = pd.read_csv(f, dtype=str, usecols=['id_kaedah', 'tarikh_isyarat']) if os.path.exists(f) else \
        pd.DataFrame(columns=['id_kaedah', 'tarikh_isyarat'])
    akhir = st.get('sesi_terakhir') or (sesi[-1] if sesi else None)
    T = T[T.tarikh_isyarat == akhir] if akhir else T.iloc[:0]
    return sesi, T.rename(columns={'id_kaedah': 'id'})


def kelompok_rows(rows, KALL):
    """kelompok = nombor kelompok korelasi pulangan bulanan backtest (kalibrasi_skor.py: pautan lengkap, rho >= 0.7), dinombor
    1.. ikut ahli terbaik; kelompok_wakil = ahli terbaik (kedudukan swing tertinggi; tanpa kedudukan: skor sebulan tertinggi)."""
    lab = {r['id']: (KALL.get(r['id']) or {}).get('kelompok') for r in rows}
    kunci = lambda r: (0, r['kedudukan']) if r.get('kedudukan') else (1, -(r['_kb'] if r['_kb'] is not None else -1e9))
    kump = {}
    for r in rows:
        if lab[r['id']]:
            kump.setdefault(lab[r['id']], []).append(r)
    wakil = {g: min(rs, key=kunci) for g, rs in kump.items()}
    no = {g: i for i, g in enumerate(sorted(kump, key=lambda g: kunci(wakil[g])), 1)}
    for r in rows:
        g = lab[r['id']]
        r['kelompok'] = no.get(g); r['kelompok_wakil'] = wakil[g]['id'] if g else None


def fasa_papan(rows):
    """Fasa papan (banner): posisi hadapan matang, kaedah dengan bukti (keluar BELUM CUKUP), tarikh status sebenar pertama
    dan julat tarikh 5 teratas."""
    mat = sum(r['h_matang'] for r in rows); jum = sum(r['h_posisi'] for r in rows)
    bukti = [r for r in rows if r['status'] != 'BELUM CUKUP']
    calon = [r for r in rows if r.get('tarikh_sebenar')]
    pt = min(calon, key=lambda r: (r['tarikh_sebenar'], r['kedudukan'] or 10 ** 6)) if calon else None
    top = sorted((r for r in rows if r.get('kedudukan') and r['kedudukan'] <= TOP_N), key=lambda r: r['kedudukan'])
    t5 = [r.get('tarikh_sebenar') for r in top]
    t5 = [min((x for x in t5 if x), default=None), max(t5) if t5 and all(t5) else None]
    pertama = dict(id=pt['id'], kedudukan=pt['kedudukan'], tarikh=pt['tarikh_sebenar']) if pt else None
    kd = lambda r: f"#{r['kedudukan']}" if r['kedudukan'] else 'bukan swing/sampel kecil'
    if not bukti:
        teks = (f"Fasa 0 — kedudukan = backtest dipotong: 0 kaedah ada bukti hadapan ({mat:,} daripada {jum:,} posisi hadapan "
                f"matang). Status sebenar pertama ±{tarikh_ms(pt['tarikh_sebenar']) if pt else '–'}"
                + (f" ({pt['id']}, {kd(pt)})" if pt else '')
                + f"; {TOP_N} teratas ±{tarikh_ms(t5[0])} – {tarikh_ms(t5[1]) if t5[1] else 'lebih lewat'}. Bukan cadangan wang sebenar.")
    else:
        teks = (f"Fasa 1 — {len(bukti)} kaedah ada bukti hadapan (≥ {N_MIN} matang, ≥ {N_HARI_MIN} hari beli); {mat:,} daripada "
                f"{jum:,} posisi matang. Kaedah lain masih backtest dipotong. Bukan cadangan wang sebenar.")
    return dict(matang_hadapan=int(mat), jumlah_hadapan=int(jum), kaedah_bukti=len(bukti), tarikh_sebenar_pertama=pertama,
                tarikh_top5=t5, teks=teks)


def nota_gabungan(rows, path=GABUNGAN_BEKU):
    """Nota gabungan beku (item 20): SEMENTARA + kedudukan kini kaedah beku dalam ranking ini (fail beku tidak diubah)."""
    try:
        ids = [k['id'] for k in json.load(open(path, encoding='utf-8')).get('kaedah', [])]
    except (OSError, ValueError, KeyError, TypeError):
        return None
    if not ids:
        return None
    kd = {r['id']: r.get('kedudukan') for r in rows}
    pos = '/'.join(f"#{kd[i]}" if kd.get(i) else '–' for i in ids)
    return f"SEMENTARA — dipilih atas data C belum matang; kedudukan kini {pos} dalam ranking ini ({'/'.join(ids)})"


def analisis(kini=None):
    kat = muat_katalog()
    REG = muat_registry({i: v for i, _, v in kat})
    WF, AT = muat_wfo(), muat_autotune()
    sesi_lejar = _lejar_sesi()
    akhir, tarikh_harga = harga_akhir(hingga=kini or sesi_lejar)   # harga hingga sesi Lejar sahaja (satu vintaj)
    kini = kini or sesi_lejar or tarikh_harga or datetime.now(timezone.utc).strftime('%Y-%m-%d')
    L, C = muat_lejar(akhir), muat_c(akhir=akhir)
    H, mula_lejar, tindih = gabung_hadapan(L, C)
    ERN = muat_earnings()
    KAL, K_CUSUM, KALL = muat_kalibrasi(semua=True)
    Hg = dict(tuple(H.groupby('id'))) if len(H) else {}
    Cg = dict(tuple(C.groupby('id'))) if len(C) else {}
    # kadar isyarat sebenar setiap kaedah dalam Lejar Penuh (sesi isyarat dengan sekurang-kurangnya satu belian/belian tertunda)
    sesi_isy, TG = muat_isyarat_lejar()
    I = pd.concat([L[['id', 'tarikh_isyarat']], TG[['id', 'tarikh_isyarat']]], ignore_index=True)
    n_sesi = len(sesi_isy) or int(I.tarikh_isyarat.nunique())
    hari_isy = I.groupby('id').tarikh_isyarat.nunique().to_dict() if len(I) else {}
    pos_isy = I.groupby('id').size().to_dict() if len(I) else {}
    lejar_n = L.groupby('id').size().to_dict() if len(L) else {}
    SESI = sesi_nyse('2026-09-01', str((pd.Timestamp(kini) + pd.Timedelta(days=5 * 366)).date()))
    beli_tunda = next((x for x in SESI if x > kini), None) if len(TG) else None   # belian sesi berikutnya (tunggu.csv)
    akhir_tahu = beli_tunda or kini
    DEPAN = [x for x in SESI if x > akhir_tahu]
    tunda = TG.groupby('id').size().to_dict() if len(TG) else {}
    rows = []
    for mid, nama, var in kat:
        r = REG.get(mid) or {}
        w, a = WF.get(mid), AT.get(mid)
        s_sub, s_wfo, s_at = semakan(r, w, a)
        lulus = sum(bool(x) for x in (s_sub, s_wfo, s_at))
        kekal = ASAS_KEKAL + TAMBAH_KEKAL * lulus
        hari = r.get('days')
        avg_bt = r['avg'] * 100 if r.get('avg') is not None else None
        mu0 = avg_bt * kekal if avg_bt is not None else 0.0
        sd0 = sd_backtest(r)
        Pm = Hg.get(mid, H.iloc[:0])
        hd = ringkas_hadapan(Pm, hari, kini, ERN)
        n0 = berat_backtest(r.get('n'))
        # skor atas purata matang penuh dan n berkesan (R5); SD hadapan dipakai jika >= N_MIN matang
        sdf = hd['sd'] if hd['matang'] >= N_MIN else None
        mu, lo, hi = skor(mu0, sd0, hd['n_berkesan'], hd['purata'] or 0.0, sdf, n0)
        st = status_kaedah(hd['matang'], hd['purata'] or 0.0, hd['sd'], mu0, lo, hi, hd['hari_beli'], hd['n_berkesan'])
        c = Cg.get(mid)
        kal = KAL.get(mid); ka = KALL.get(mid) or {}
        pt = pantau_kaedah(Pm, hd['umur_hari'], kini, kal, kekal, mu, lo, hi, hd['hari_beli'], K_CUSUM, hd['n_berkesan'])
        p_sas, p_amb = teks_pantau(kal, kekal, K_CUSUM)
        sebulan = (lambda v: v / hari * HARI_BULAN) if hari else (lambda v: None)
        # meter bukti: tarikh sebenar ikut kadar isyarat Lejar (sandaran: kadar kohort backtest jika tiada isyarat Lejar)
        beli = Pm.groupby('tarikh_beli').size().to_dict() if len(Pm) else {}
        if tunda.get(mid):
            beli[beli_tunda] = beli.get(beli_tunda, 0) + tunda[mid]
        if hari_isy.get(mid):
            kadar, sehari, asas = Fraction(hari_isy[mid], n_sesi), Fraction(pos_isy[mid], hari_isy[mid]), 'lejar'
        elif kal and kal.get('kohort') and kal.get('kohort_setahun') and ka.get('n'):
            kadar = Fraction(min(1.0, kal['kohort_setahun'] / 252)).limit_denominator(10 ** 4)
            sehari, asas = Fraction(ka['n'] / kal['kohort']).limit_denominator(10 ** 4), 'backtest'
        else:
            kadar = sehari = None; asas = None
        t_sebenar = tarikh_bukti(beli, hd['umur_hari'], kadar, sehari, DEPAN, SESI)
        rows.append(dict(
            id=mid, nama=nama, varian=var, swing=bool(hari is not None and SWING[0] <= hari <= SWING[1]),
            hari=bulat(hari, 1), bt_keputusan=r.get('keputusan'), bt_skor=bulat(r.get('skor'), 1), bt_cagr=bulat(r.get('cagr'), 4),
            bt_mdd=bulat(r.get('mdd'), 4), bt_menang=bulat(r.get('win'), 4), bt_purata=bulat(avg_bt, 2), bt_n=r.get('n'),
            bt_setahun=bulat(r.get('setahun'), 1), n0=bulat(n0, 1),
            subset=f"{r.get('subset_menang', 0)}/{r.get('subset_n', 0)}" if r else None, lulus_subset=s_sub,
            wfo_cagr=bulat(w and w['cagr'], 4), wfo_ew=bulat(w and w['ew'], 4), wfo_mdd=bulat(w and w['mdd'], 4),
            wfo_dsr=bulat(w and w['dsr'], 2), lulus_wfo=s_wfo,
            at_label=a and a.get('label'), at_cagr_a=bulat(a and a.get('cagr_a'), 4), at_cagr_b=bulat(a and a.get('cagr_b'), 4),
            at_spy=bulat(a and a.get('spy_a'), 4), lulus_at=s_at, lulus=lulus, kekal=kekal, jangkaan=bulat(mu0, 2),
            h_posisi=hd['posisi'], h_tutup=hd['tutup'], h_matang=hd['matang'], h_purata=bulat(hd['purata'], 2),
            h_menang=bulat(hd['menang'], 4), h_purata_l2=bulat(hd['purata_l2'], 2), h_umur=hd['umur_hari'],
            h_pangkas=bulat(hd['pangkas'], 2), h_median=bulat(hd['median'], 2), h_n_berkesan=bulat(hd['n_berkesan'], 1),
            h_hari_beli=hd['hari_beli'], h_lintas_earnings=hd['lintas_earnings'],
            h_purata_tanpa_earnings=bulat(hd['purata_tanpa_earnings'], 2),
            matang_mula=hd['matang_mula'], matang_20=hd['matang_20'],
            c_posisi=int(len(c)) if c is not None else 0,
            c_purata=bulat(c.hasil1.dropna().mean(), 2) if c is not None and c.hasil1.notna().any() else None,
            skor=bulat(mu, 2), skor_bawah=bulat(lo, 2), skor_atas=bulat(hi, 2),
            skor_bulan=bulat(sebulan(mu), 2), skor_bulan_bawah=bulat(sebulan(lo), 2), skor_bulan_atas=bulat(sebulan(hi), 2),
            lb_bulan=bulat(sebulan(lo), 3),
            g_matang=hd['hari_beli'], g_perlu=N_HARI_MIN, nb=bulat(hd['n_berkesan'], 1), nb_perlu=nb_perlu(mu0, sdf or sd0, n0),
            tarikh_sebenar=t_sebenar, tarikh_asas=asas,
            ditolak=r.get('keputusan') == 'DITOLAK', lejar_n=int(lejar_n.get(mid, 0)),
            median_bt=bulat(ka.get('median'), 2), pangkas5_bt=bulat(ka.get('u1_pangkas'), 2), pct_top1=bulat(ka.get('pct_top1'), 1),
            status=st, **pt, pantau_sasaran=p_sas, pantau_ambang=p_amb,
            _kb=sebulan(mu), _se=(sebulan(hi) - sebulan(mu)) / Z95 if hari else None))
    sw, kecil, lain = susun_kedudukan(rows)
    # peluang pangkat (Monte Carlo) dalam set berkedudukan; selainnya None
    p1, p5, q5, q95 = peluang_pangkat([r['_kb'] for r in sw], [r['_se'] for r in sw])
    for r, a, b, c, d in zip(sw, p1, p5, q5, q95):
        r.update(p_top1=round(float(a), 3), p_top5=round(float(b), 3), pangkat_p5=int(c), pangkat_p95=int(d))
    for r in kecil + lain:
        r.update(p_top1=None, p_top5=None, pangkat_p5=None, pangkat_p95=None)
    semua = sw + kecil + lain
    kelompok_rows(semua, KALL)
    for r in semua:
        r.pop('_kb'); r.pop('_se')
    meta = dict(kini=kini, harga_pada=tarikh_harga, mula_lejar=mula_lejar,
                lejar_posisi=int(len(L)), lejar_tindih=tindih, c_posisi=int(len(C)),
                c_pra_lejar=int((C.tarikh_beli < mula_lejar).sum()) if mula_lejar and len(C) else int(len(C)),
                lejar_sesi=sesi_lejar, lejar_sesi_isyarat=n_sesi, beli_tertunda=beli_tunda,
                fasa=fasa_papan(semua), label_semakan=LABEL_SEMAKAN, gabungan_beku_nota=nota_gabungan(semua))
    return semua, meta


def _lejar_sesi():
    try:
        return json.load(open(os.path.join(LEJAR, 'status.json'), encoding='utf-8')).get('sesi_terakhir')
    except (OSError, ValueError):
        return None


# ---------------------------------------------------------------- rujukan
def cagr_indeks(ticker='SPY', mula=TEMPOH_IS[0], akhir=TEMPOH_IS[1], path=INDEKS):
    if not os.path.exists(path):
        return None
    d = pd.read_csv(path, usecols=['ticker', 'date', 'close'], dtype={'date': str})
    d = d[(d.ticker == ticker) & (d.date >= mula.replace('-', '')) & (d.date <= akhir.replace('-', ''))].sort_values('date')
    if len(d) < 2:
        return None
    t = (pd.Timestamp(d.date.iloc[-1]) - pd.Timestamp(d.date.iloc[0])).days / 365.25
    return float((d.close.iloc[-1] / d.close.iloc[0]) ** (1 / t) - 1)


def rujukan(rows, WF=None):
    reg = pd.read_csv(REGISTRY, usecols=['set', 'ew_cagr'])
    ew = reg[reg['set'].astype(str) == '431'].ew_cagr.dropna()
    w = next((r for r in rows if r.get('wfo_ew') is not None), None)
    at = next((r for r in rows if r.get('at_spy') is not None), None)
    out = dict(is_tempoh='1 Nov 2019 – 2 Okt 2026', is_ew=bulat(ew.iloc[0], 4) if len(ew) else None, is_spy=bulat(cagr_indeks(), 4),
               wfo_tempoh='1 Jan 2023 – 2 Okt 2026', wfo_ew=w and w['wfo_ew'], wfo_spy=None,
               at_tempoh='2013 – Sep 2024 (2000 saham AS)', at_spy=at and at['at_spy'], slot=None)
    WF = WF if WF is not None else muat_wfo()
    sp = next((v['spy'] for v in WF.values() if v.get('spy') is not None), None)
    out['wfo_spy'] = bulat(sp, 4)
    try:
        s = {}
        for k in ('RS_10', 'RAWAK_10'):
            e = pd.read_csv(os.path.join(SLOT, f'{k}_ekuiti.csv'))
            s[k] = bulat((e.ekuiti.iloc[-1] - 1) * 100, 2)
            s['spy'] = bulat((e.spy.iloc[-1] - 1) * 100, 2)
            s['mula'], s['akhir'], s['sesi'] = str(e.tarikh.iloc[0]), str(e.tarikh.iloc[-1]), int(len(e))
        out['slot'] = s
    except (OSError, ValueError, KeyError, IndexError):
        pass
    return out


# ---------------------------------------------------------------- penemuan + output
def p(x, d=1):
    return '–' if x is None else f'{x * 100:.{d}f}%'


def sg(x, d=2):
    return '–' if x is None else f'{x:+.{d}f}%'


def tarikh_ms(t):
    if not t:
        return '–'
    d = datetime.strptime(t, '%Y-%m-%d')
    return f"{d.day} {['Jan', 'Feb', 'Mac', 'Apr', 'Mei', 'Jun', 'Jul', 'Ogo', 'Sep', 'Okt', 'Nov', 'Dis'][d.month - 1]} {d.year}"


def penemuan(rows, meta, ruj):
    sw = [r for r in rows if r['swing'] and r['kedudukan']]
    out = []
    if sw:
        t = sw[0]
        lb = max(sw, key=lambda r: r['lb_bulan'] if r['lb_bulan'] is not None else -1e9)
        out.append(f"Swing teratas ikut skor gabungan: {t['id']} {t['nama']} — {sg(t['skor_bulan'])} sebulan "
                   f"setiap posisi (julat {sg(t['skor_bulan_bawah'])} hingga {sg(t['skor_bulan_atas'])}), {t['lulus']}/3 semakan luar sampel, "
                   f"status {t['status']}; CAGR backtest bersendirian {p(t['bt_cagr'])} ({t['bt_setahun']} dagangan setahun). "
                   f"Tetapi P(benar-benar #1) hanya {p(t['p_top1'], 0)} dan selang pangkat 90% #{t['pangkat_p5']}–#{t['pangkat_p95']}"
                   + (' (DITOLAK dalam registry)' if t['ditolak'] else '') + '. Tiga seterusnya: ' + ', '.join(r['id'] for r in sw[1:4])
                   + f". Had bawah julat tertinggi: {lb['id']} ({sg(lb['lb_bulan'])} sebulan).")
    dinilai = [r for r in rows if r['h_matang'] >= N_MIN]
    if dinilai:
        kuat = [r['id'] for r in dinilai if r['status'] == 'KUAT']
        amaran = [r['id'] for r in rows if r['status'] == 'AMARAN']
        out.append(f"{len(dinilai)} kaedah ada ≥ {N_MIN} posisi hadapan matang; KUAT ({len(kuat)}): {senarai(kuat)}; "
                   f"AMARAN, jauh di bawah jangkaan ({len(amaran)}): {senarai(amaran)}.")
    else:
        mt = sum(r['h_matang'] for r in rows)
        f = meta.get('fasa') or {}; t1 = f.get('tarikh_sebenar_pertama') or {}; t5 = f.get('tarikh_top5') or [None, None]
        out.append(f"Data hadapan belum matang: {mt} posisi matang daripada {sum(r['h_posisi'] for r in rows)} "
                   f"(Lejar sejak {tarikh_ms(meta['mula_lejar'])}, Papertrade C sejak 8 Okt 2026). Kedudukan kini = backtest dipotong. "
                   f"Status sebenar pertama (≥ {N_MIN} matang dan ≥ {N_HARI_MIN} hari beli) dijangka {tarikh_ms(t1.get('tarikh'))} "
                   f"({t1.get('id', '–')}); {TOP_N} teratas {tarikh_ms(t5[0])} – {tarikh_ms(t5[1]) if t5[1] else 'lebih lewat'}.")
    pt = {k: [r['id'] for r in rows if r.get('pantau') == k] for k in ('BERSARA', 'GANTUNG', 'AMARAN')}
    if any(pt.values()) and out:   # kekal 3 penemuan: pantau ditambah pada penemuan data hadapan
        out[-1] += ' Pantau: ' + '; '.join(f'{k} ({len(v)}): {senarai(v)}' for k, v in pt.items() if v) + '.'
    n = {k: sum(1 for r in rows if r[f'lulus_{k}']) for k in ('subset', 'wfo', 'at')}
    dua = [r['id'] for r in rows if r['lulus'] >= 2]
    s = ruj.get('slot') or {}
    out.append(f"Ketahanan backtest lemah: lulus S1–S4 {n['subset']}, WFO {n['wfo']}, 2000 saham AS {n['at']} kaedah; "
               f"≥ 2 daripada 3 semakan: {', '.join(dua) if dua else 'tiada'}. "
               + (f"Portfolio 10 slot sejak {tarikh_ms(s.get('mula'))}: RS_10 {sg(s.get('RS_10'))}, RAWAK_10 {sg(s.get('RAWAK_10'))}, "
                  f"SPY {sg(s.get('spy'))}." if s else ''))
    return out


def senarai(ids, had=8):
    return 'tiada' if not ids else ', '.join(ids[:had]) + (f' dan {len(ids) - had} lagi' if len(ids) > had else '')


def tanda(v):
    return '–' if v is None else ('✓' if v else '✗')


def jana_md(rows, meta, ruj, pen, dibina):
    L = ['# Papan Penganalisis — banding semua kaedah (backtest + papertrade)', '',
         f"Dijana {dibina} oleh `standard/penganalisis.py` (GitHub Actions `analisis.yml`, selepas Lejar Penuh). Data harga hingga "
         f"{tarikh_ms(meta['harga_pada'])}; Lejar sesi terakhir {tarikh_ms(meta['lejar_sesi'])}. Rekod analisis sahaja: tiada order, "
         'tiada wang sebenar. Dashboard: tab Analisis (db `analisis/papan`).', '',
         f"> **{(meta.get('fasa') or {}).get('teks', '')}**", '']
    if meta.get('gabungan_beku_nota'):
        L += [f"Gabungan beku (portfolio_slot GABUNGAN_10): {meta['gabungan_beku_nota']}.", '']
    L += ['## 3 penemuan utama', ''] + [f'{i}. {x}' for i, x in enumerate(pen, 1)] + ['',
         '## Cara skor dikira', '',
         f'- Jangkaan backtest = purata pulangan bersih setiap dagangan, set 431 dalam sampel (varian aktif), dikekalkan '
         f'{int(ASAS_KEKAL * 100)}% + {int(TAMBAH_KEKAL * 100)}% bagi setiap semakan luar sampel yang lulus: S1–S4 (atasi EW dalam ≥ 3/4 '
         'subset), WFO (CAGR luar sampel 2023–2026 > EW 423 tempoh sama) dan 2000 saham AS (AUTOTUNE A01: CAGR > SPY dalam kumpulan A dan B).',
         f'- Bukti hadapan = posisi matang Lejar Penuh + kohort Papertrade C sebelum Lejar bermula ({meta["c_pra_lejar"]} posisi; '
         f'{meta["lejar_tindih"]} posisi Lejar yang isyaratnya jatuh semasa C pra-Lejar masih memegang kaedah+saham sama dibuang). Matang = '
         f'dibeli ≥ maks({UMUR_MIN} hari, 1.5 × hari pegang backtest) lalu; tutup = untung akhir, terbuka = untung semasa (bersih kos 0.1% '
         'setiap belah). Papertrade C selepas Lejar bermula = isyarat sama dengan Lejar: lajur semakan sahaja.',
         f'- Skor = (n0 × jangkaan + nb × purata matang) ÷ (n0 + nb), n0 = berat backtest (maks {N0}; kurang jika dagangan '
         f'backtest sedikit). Purata penuh, tidak dipangkas (sejak 22 Okt 2026: untung swing datang daripada ekor kanan; purata '
         f'dipangkas {int(PANGKAS * 100)}% setiap hujung dipapar sebagai semakan). nb = n berkesan: posisi '
         'yang dibeli pada hari sama bergerak bersama pasaran, jadi n dibahagi kesan reka bentuk berkelompok ikut hari beli '
         f'(< {HARI_KLUSTER_MIN} hari beli berbeza: nb = bilangan hari). Julat 95% = skor ± 1.96 × SD ÷ √(n0 + nb). Skor sebulan = skor ÷ '
         f'hari pegang backtest × {HARI_BULAN}, iaitu untung setiap posisi jika modal dipusing semula sebaik keluar.',
         f'- Status: AMARAN = ≥ {N_AMARAN} matang, ≥ {N_HARI_MIN} hari beli, nb ≥ {NB_MIN} dan purata matang jauh di bawah jangkaan '
         f'(t < −2 atas nb); BELUM CUKUP = < {N_MIN} matang atau < {N_HARI_MIN} hari beli berbeza; KUAT = julat 95% di atas 0; LEMAH = '
         'julat 95% di bawah 0; selainnya PERHATI.',
         f'- Pantau (label sahaja): pengawal bukti dahulu — BELUM CUKUP = < {PANTAU_KOHORT} hari beli matang atau nb < {NB_MIN}; '
         f'kemudian BERSARA = P(purata ≤ 0) > {PANTAU_P} dengan ≥ {PANTAU_G} hari beli, atau ≥ 2 amaran CUSUM; GANTUNG = '
         f'kejatuhan ekuiti kohort harian > {PANTAU_DD} × maks backtest, tempoh di bawah puncak > maks backtest, atau purata '
         f'{PANTAU_BERGULIR} hari beli matang terakhir (diwinsor) < persentil ke-5 purata bergulir {PANTAU_BERGULIR} hari beli backtest '
         '(diwinsor, dilaras ke sasaran); AMARAN = 1 amaran CUSUM bawah (kohort diwinsor p5–p95 backtest; sasaran = min(purata winsor, '
         'kekal × purata winsor); k 0.25; h dikalibrasi bootstrap blok bulanan supaya amaran palsu ~ sekali dalam 2 tahun). Sasaran dan '
         'ambang setiap kaedah dipapar dalam % (pantau_sasaran, pantau_ambang).',
         f'- Ranking tunggal: kedudukan = skor sebulan tanpa bundar; P(#1) dan P({TOP_N} teratas) serta selang pangkat 90% = Monte Carlo '
         f'{MC_CABUTAN:,} cabutan berbiji ({MC_BIJI}), skor sebulan setiap kaedah ~ Normal(skor, (had atas − skor) ÷ 1.96), bebas; had bawah '
         'julat sebulan (lb_bulan) = susunan lalai dashboard.',
         f'- Meter bukti: hari beli matang / {N_HARI_MIN}; nb / nb perlu, nb perlu = maks({NB_MIN}, (1.96 × SD ÷ |jangkaan|)² − n0) = n '
         'berkesan supaya julat 95% tidak merangkumi 0 jika purata hadapan = jangkaan; status sebenar (anggaran) = sesi NYSE pertama dengan '
         f'≥ {N_MIN} matang DAN ≥ {N_HARI_MIN} hari beli matang, ikut kadar isyarat kaedah dalam Lejar Penuh (pecahan sesi isyarat '
         'berbelian; posisi setiap hari beli) — tiada isyarat Lejar: kadar kohort backtest (ditanda B).',
         '- Ekor backtest (dagangan backtest varian aktif, kalibrasi_skor.py): median, purata dipangkas 5% dan % jumlah untung daripada 1% '
         'dagangan terbaik. Kelompok = korelasi purata pulangan bulanan backtest (ikut bulan masuk), pautan lengkap, ρ ≥ 0.7 antara setiap '
         'pasangan; wakil = ahli berkedudukan tertinggi.',
         f"- Label semakan: {LABEL_SEMAKAN['s14']}; {LABEL_SEMAKAN['wfo']}; {LABEL_SEMAKAN['at']}.",
         '- Lintas earnings = posisi matang yang dipegang melalui tarikh earnings (TradingView + sejarah Nasdaq/SST); purata tanpa '
         'posisi itu dipapar berasingan (tidak mengubah skor).',
         f'- Swing = purata pegang backtest {SWING[0]}–{SWING[1]} hari dagangan. Kaedah swing dengan < {N_BT_MIN} dagangan backtest '
         '(sampel kecil) tiada nombor kedudukan dan disusun di hujung jadual swing. Kaedah lain disenarai berasingan.', '',
         '## Rujukan', '',
         f"- Backtest dalam sampel ({ruj['is_tempoh']}): EW 431 {p(ruj['is_ew'])}, SPY {p(ruj['is_spy'])} setahun.",
         f"- WFO luar sampel ({ruj['wfo_tempoh']}): EW 423 {p(ruj['wfo_ew'])}, SPY {p(ruj['wfo_spy'])} setahun.",
         f"- AUTOTUNE luar sampel ({ruj['at_tempoh']}): SPY {p(ruj['at_spy'])} setahun."]
    s = ruj.get('slot')
    if s:
        L.append(f"- Portfolio maya 10 slot ({tarikh_ms(s['mula'])} – {tarikh_ms(s['akhir'])}, {s['sesi']} sesi): RS_10 {sg(s['RS_10'])}, "
                 f"RAWAK_10 {sg(s['RAWAK_10'])}, SPY {sg(s['spy'])}. Kajian portfolio: memilih ikut RS pasaran mengatasi memilih ikut kaedah "
                 '(`kajian/KAJIAN_PORTFOLIO.md`).')
    hd = ('| # | Kaedah | Hari | Dagangan/tahun | Backtest 431: CAGR · MDD · menang · purata | S1–S4 · WFO · 2000 AS | Jangkaan % | '
          'Hadapan: posisi · matang · purata · dipangkas · median · menang | nb · hari beli | Lintas earnings · purata tanpa | '
          'Lorong 2 % | C: posisi · purata | Skor % [julat 95%] | Skor sebulan % [had bawah] | P(#1) · P(5 teratas) · pangkat 90% | '
          'Bukti: hari beli /10 · nb / nb perlu · status sebenar | Ekor bt: median · pangkas 5% · 1% teratas | Kelompok · wakil | '
          'Lejar · registry | Status | Pantau | Sasaran · ambang pantau |')
    sep = '|' + '---|' * 23

    def baris(r):
        return (f"| {r['kedudukan'] or '–'} | {r['id']} {r['nama']} | {r['hari'] if r['hari'] is not None else '–'} | "
                f"{r['bt_setahun'] if r['bt_setahun'] is not None else '–'} | "
                f"{p(r['bt_cagr'])} · {p(r['bt_mdd'])} · {p(r['bt_menang'], 0)} · {sg(r['bt_purata'])} | "
                f"{tanda(r['lulus_subset'])} {r['subset'] or ''} · {tanda(r['lulus_wfo'])} {p(r['wfo_cagr'])} · {tanda(r['lulus_at'])} "
                f"{p(r['at_cagr_a'])}/{p(r['at_cagr_b'])} | {sg(r['jangkaan'])} | {r['h_posisi']} · {r['h_matang']} · {sg(r['h_purata'])} · "
                f"{sg(r['h_pangkas'])} · {sg(r['h_median'])} · {p(r['h_menang'], 0)} | {r['h_n_berkesan']} · {r['h_hari_beli']} | "
                f"{r['h_lintas_earnings']} · {sg(r['h_purata_tanpa_earnings'])} | {sg(r['h_purata_l2'])} | {r['c_posisi']} · {sg(r['c_purata'])} | "
                f"{sg(r['skor'])} [{sg(r['skor_bawah'])}, {sg(r['skor_atas'])}] | {sg(r['skor_bulan'])} [{sg(r['lb_bulan'])}] | "
                + (f"{p(r['p_top1'])} · {p(r['p_top5'])} · #{r['pangkat_p5']}–#{r['pangkat_p95']}" if r['p_top1'] is not None else '–')
                + f" | {r['g_matang']}/{r['g_perlu']} · {r['nb']} / {r['nb_perlu'] if r['nb_perlu'] is not None else '–'} · "
                f"{tarikh_ms(r['tarikh_sebenar'])}{' (B)' if r['tarikh_asas'] == 'backtest' else ''} | "
                f"{sg(r['median_bt'])} · {sg(r['pangkas5_bt'])} · {r['pct_top1'] if r['pct_top1'] is not None else '–'}% | "
                f"K{r['kelompok'] or '–'} · {r['kelompok_wakil'] or '–'} | {r['lejar_n']} · {'⚑ DITOLAK' if r['ditolak'] else r['bt_keputusan'] or '–'} | "
                f"{r['status']} | {r['pantau']}{' (' + r['p_sebab'] + ')' if r['p_sebab'] else ''} | "
                f"{r['pantau_sasaran'] or '–'} · {r['pantau_ambang'] or '–'} |")
    sw = [r for r in rows if r['swing']]
    lain = [r for r in rows if not r['swing']]
    L += ['', f'## Kaedah swing ({SWING[0]}–{SWING[1]} hari), susun ikut skor sebulan tanpa bundar ({len(sw)} kaedah)', '', hd, sep] + [baris(r) for r in sw]
    L += ['', f'## Bukan swing (pegang < {SWING[0]} atau > {SWING[1]} hari; {len(lain)} kaedah)', '', hd, sep] + [baris(r) for r in lain]
    L += ['', '## Batasan', '',
          '- Set 431 ialah senarai Shariah hari ini (bias kemandirian); kaedah dibina dan ditapis atas data 2019–2026. Sebab itu jangkaan '
          'backtest dipotong dan semakan 2000 saham AS diberi berat.',
          '- SD backtest dianggar daripada kadar menang, purata menang dan purata rugi (anggaran bawah), jadi julat sebelum data hadapan '
          'matang lebih sempit daripada sebenar.',
          '- Skor sebulan menganggap modal dipusing semula sebaik keluar; kaedah dengan isyarat jarang tidak menggunakan modal sepenuhnya '
          '(lihat CAGR backtest).',
          '- Moomoo lama (1–8 Okt 2026, varian v1) tidak dikira.',
          '- Peluang pangkat menganggap skor kaedah bebas antara satu sama lain (kaedah sekelompok sebenarnya bergerak bersama) dan '
          'taburan normal; tarikh status sebenar ialah anggaran ikut kadar isyarat beberapa sesi Lejar sahaja.']
    return '\n'.join(L) + '\n'


def kedudukan_sebelum(rows, kini, lama):
    """kedudukan_sebelum = kedudukan pada data sesi terdahulu (anak panah perubahan tab Analisis). Larian semula pada data
    yang sama mengekalkan rujukan lama, jadi anak panah tidak hilang apabila papan dijana dua kali sehari."""
    if not lama:
        return
    L = {r.get('id'): r for r in lama.get('rows', [])}
    for r in rows:
        x = L.get(r['id'])
        if x is not None:
            r['kedudukan_sebelum'] = x.get('kedudukan_sebelum') if lama.get('kini') == kini else x.get('kedudukan')


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument('--kini', help='tarikh data (YYYY-MM-DD); lalai = sesi terakhir Lejar Penuh (lejar/status.json)')
    ap.add_argument('--md', default=OUT_MD); ap.add_argument('--json', default=OUT_JSON)
    ap.add_argument('--lama', help='papan terdahulu (kedudukan_sebelum; lalai = fail --json sedia ada), cth. untuk pratonton di luar repo')
    a = ap.parse_args(argv)
    rows, meta = analisis(a.kini)
    ruj = rujukan(rows)
    pen = penemuan(rows, meta, ruj)
    try:
        lama = json.load(open(a.lama or a.json, encoding='utf-8'))
    except (OSError, ValueError):
        lama = None
    kedudukan_sebelum(rows, meta.get('kini'), lama)
    dibina = (datetime.now(timezone.utc) + timedelta(hours=8)).strftime('%Y-%m-%d %H:%M') + ' MYT'
    os.makedirs(os.path.dirname(a.json), exist_ok=True)
    doc = dict(dibina=dibina, **meta, parameter=dict(n0_maks=N0, asas_kekal=ASAS_KEKAL, tambah_kekal=TAMBAH_KEKAL, swing=list(SWING),
                                                    n_min=N_MIN, n_amaran=N_AMARAN, umur_min=UMUR_MIN, hari_bulan=HARI_BULAN,
                                                    pangkas=PANGKAS, n_hari_min=N_HARI_MIN, hari_kluster_min=HARI_KLUSTER_MIN,
                                                    pantau=dict(dd=PANTAU_DD, p=PANTAU_P, g=PANTAU_G, kohort=PANTAU_KOHORT,
                                                                bergulir=PANTAU_BERGULIR, nb_min=NB_MIN, k=muat_kalibrasi()[1]),
                                                    mc=dict(cabutan=MC_CABUTAN, biji=MC_BIJI, top=TOP_N)),
               penemuan=pen, rujukan=ruj, rows=rows,
               nota='Papan Penganalisis (standard/penganalisis.py). Skor = purata pulangan bersih setiap dagangan (%) gabungan backtest '
                    'dipotong dan posisi hadapan matang. Rekod analisis sahaja.')
    try:   # kandungan sama (hanya masa dibina berbeza) -> fail tidak ditulis semula, jadi tiada commit
        if not a.lama and {k: v for k, v in lama.items() if k != 'dibina'} == \
                json.loads(json.dumps({k: v for k, v in doc.items() if k != 'dibina'})) and os.path.exists(a.md):
            print(f"penganalisis: tiada perubahan sejak {lama.get('dibina')}"); return
    except (OSError, ValueError, AttributeError):
        pass
    open(a.json, 'w', encoding='utf-8').write(json.dumps(doc, ensure_ascii=False, separators=(',', ':')))
    open(a.md, 'w', encoding='utf-8').write(jana_md(rows, meta, ruj, pen, dibina))
    print(f"penganalisis: {len(rows)} kaedah ({sum(r['swing'] for r in rows)} swing), "
          f"{sum(r['h_matang'] for r in rows)} posisi matang; {a.md}, {a.json} ({os.path.getsize(a.json)} bait)")


if __name__ == '__main__':
    main()
