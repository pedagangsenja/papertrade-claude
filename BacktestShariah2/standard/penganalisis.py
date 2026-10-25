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
# v4 (25 Okt 2026, audit pratonton: skor mengukur pulangan mentah = hanyutan pasaran, bukan edge; PRATONTON sahaja):
#   1. Skor atas LEBIHAN. Prior = lebihan purata dagangan backtest atas belian rawak tempoh sama (purata sama berat 431 saham,
#      buka masuk -> buka/tutup keluar; pulangan bersih kos 0.2% pusingan tolak pulangan kasar rawak; kalibrasi_skor.py
#      lebihan_rawak), dikecut ke lebihan 0 (bukan ke pulangan mentah). Kredit: asas 25% + 25% HANYA jika lulus AUTOTUNE (label
#      SEDERHANA/TINGGI: ujian bebas 2000 saham AS); S1–S4 (kestabilan dalam sampel) dan WFO (separa dalam sampel) 0 kredit,
#      dilapor sahaja. u3 (lebihan atas purata semua dagangan hari sama) dilapor (bt_u3).
#   2. Bukti hadapan atas LEBIHAN EW: setiap posisi matang lawan EW alam Shariah tempoh sama (data/analisis/ew_harian.csv,
#      standard/penanda_ew.py). Hanya C >= 14 Okt 2026 dan Lejar Penuh; kohort C 8–13 Okt = isi semula (backfill), dikecualikan
#      (lajur kohort jika ada, dan tarikh beli). Pulangan umur tetap h_r5/h_r10/h_r20 (lebihan EW pada sesi beli + k, posisi
#      yang umurnya cukup; tiada sensor kanan) dan purata ikut saham (h_lebihan_saham) dilapor.
#   3. n berkesan dua hala (kelompok hari beli + saham; SE Cameron–Gelbach–Miller). KUAT = had bawah z 3.0 skor > 0; nb_perlu
#      pada z 3.0; p sehala bukti hadapan (lebihan > 0) dilaras Holm merentas kaedah (h_p_holm, h_z_terlaras).
#   4. Pantau dua hala: SPRT Wald (medan sprt) antara H0 lebihan = 0 dan H1 lebihan = jangkaan dipotong (skala kohort) atas
#      purata lebihan kohort harian matang; CUSUM kekal brek bencana (label OK -> TIADA BENCANA); GANTUNG/BERSARA kekal (atas
#      pulangan mentah, skor_mentah).
#   5. Pintu wang sebenar A–F (pintu, pintu_lulus, kurang) dan corong aras atas; 6. bendera (data/analisis/bendera_kaedah.csv:
#      DITOLAK, ARTIFAK, HAMPIR_PENDUA, CIRI regex kasar); 7. swing dan bukan swing dipisah (skor sebulan swing sahaja);
#   8. sejarah_skor.csv + ramalan (Spearman skor minggu t lawan lebihan EW umur 5 sesi posisi minggu t+1).
import argparse, glob, hashlib, inspect, json, math, os, re
from datetime import datetime, timedelta, timezone
from fractions import Fraction
from statistics import NormalDist

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
# versi formula ranking/skor/pantau (audit ketepatan data 24 Okt 2026, lapisan 4): naikkan VERSI_FORMULA dan tambah satu baris dalam
# data/analisis/LOG_FORMULA.md bagi setiap perubahan cara skor, kedudukan, pantau atau P(5 teratas) dikira. cap_formula() mengesan
# perubahan yang tidak direkod (parameter, kalibrasi_skor.json atau kod fungsi teras), supaya kedudukan tidak berubah senyap.
VERSI_FORMULA = '4.0'
LOG_FORMULA = os.path.join(BS2, 'data', 'analisis', 'LOG_FORMULA.md')
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
LABEL_SEMAKAN = dict(s14='S1–S4 = kestabilan dalam sampel (subset 431 saham, tempoh sama; tiada kredit)',
                     wfo='WFO = separa dalam sampel (dalam tempoh pemilihan, versi ditala; tiada kredit)',
                     at='AUTOTUNE = 2000 saham AS lain, label SEDERHANA/TINGGI (satu-satunya ujian bebas; +25%)')
PANTAU_BERGULIR = 20    # GANTUNG hadapan: purata N kohort matang terakhir lawan p5 purata bergulir N kohort backtest
PANTAU_OK = 'TIADA BENCANA'   # v4: CUSUM ialah brek bencana sahaja; ketiadaan amaran bukan bukti edge (lihat sprt)
PANTAU_STATUS = ['BERSARA', 'GANTUNG', 'AMARAN', PANTAU_OK, 'BELUM CUKUP']
# v4 (25 Okt 2026): lebihan, bukti hadapan, n berkesan dua hala, SPRT, pintu, bendera, ramalan
BUKTI_MULA_C = '2026-10-14'   # bukti hadapan Papertrade C bermula; kohort 8–13 Okt = isi semula (backfill), dikecualikan
EW_HARIAN = os.path.join(BS2, 'data', 'analisis', 'ew_harian.csv')
Z_KUAT = 3.0            # KUAT dan nb_perlu (Harvey, Liu & Zhu t > 3; dahulu 1.96 tanpa pembetulan ujian berganda)
UMUR_TETAP = (5, 10, 20)   # pulangan umur tetap (sesi selepas hari beli)
SPRT_ALFA, SPRT_BETA = 0.00135, 0.10   # alfa = ekor sehala z 3.0 (sama dengan KUAT); beta 10%
SD_KOHORT_MIN = 1.0     # sd minimum purata kohort lebihan (%) dalam SPRT
PINTU_C_HARI = 40       # pintu C: >= 40 hari beli matang
PINTU_D_SESI = 126      # pintu D: inkubasi >= 126 sesi (~6 bulan) ...
PINTU_D_EW = 0.10       # ... termasuk satu pembetulan EW alam >= 10% (puncak ke lembah)
PINTU_E_SESI = 126      # pintu E: portfolio 10 slot berkaitan dijejak >= 126 sesi
AT_LULUS = ('SEDERHANA', 'TINGGI')
ARTIFAK = {'M81': 'pandang hadapan: _exit_ekor menanda exitc[j-1] daripada rendah hari j (AUTOTUNE/hasil/AUDIT_M81.md); '
                  'sedang dibaiki dalam BacktestShariah2/kod'}
PENDUA_AMBANG = 0.8     # HAMPIR_PENDUA: >= 80% isyarat (saham, tarikh) terkandung dalam kaedah lain ...
PENDUA_MIN = 20         # ... bagi kaedah dengan >= 20 isyarat malam
ISYARAT = os.path.join(BS2, 'data', 'isyarat')
KOD_KAEDAH = os.path.join(BS2, 'kod', 'kaedah')
JENIS = os.path.join(BS2, 'kod', 'jenis_kaedah.csv')
BENDERA = os.path.join(BS2, 'data', 'analisis', 'bendera_kaedah.csv')
SEJARAH = os.path.join(BS2, 'data', 'analisis', 'sejarah_skor.csv')
PRA_DAFTAR = os.path.join(BS2, 'data', 'analisis', 'pra_daftar.json')
UJIAN_PIT = os.path.join(BS2, 'data', 'analisis', 'ujian_pit.json')
RAMALAN_MIN_KAEDAH = 5  # kaedah minimum setiap pasangan minggu dalam ujian ramalan
ND = NormalDist()
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
    """{id: dict(label, cagr_a, spy_a, cagr_b, spy_b, cagr_kunci, spy_kunci, cagr_bersih, spy_bersih, dsr, pbo)} — 2000 saham AS
    (A01): OOS A/B 2013 – Sep 2024 (versi ditala), tempoh kunci Okt 2024 – Okt 2026, ujian bersih 2013–2018 (parameter asal)."""
    if not os.path.exists(path):
        return {}
    k = ('label', 'cagr_a', 'spy_a', 'mdd_a', 'cagr_b', 'spy_b', 'cagr_kunci', 'spy_kunci', 'cagr_bersih', 'spy_bersih', 'dsr', 'pbo')
    return {r['id']: {x: r.get(x) for x in k} for r in json.load(open(path, encoding='utf-8')).get('kaedah', [])}


def semakan(reg, wfo, at):
    """Tiga semakan luar sampel: (subset, wfo, autotune) masing-masing True/False/None (tiada data). autotune = CAGR OOS-A dan
    OOS-B > SPY (lulus_at; disemak kira_semula.py). v4: kredit prior hanya daripada kredit_at() (label dikunci)."""
    s = (reg['subset_menang'] >= 3) if reg and reg.get('subset_n') else None
    w = (wfo['cagr'] > wfo['ew']) if wfo and wfo.get('cagr') is not None and wfo.get('ew') is not None else None
    a = None
    if at and None not in (nombor(at.get('cagr_a')), nombor(at.get('spy_a')), nombor(at.get('cagr_b')), nombor(at.get('spy_b'))):
        a = at['cagr_a'] > at['spy_a'] and at['cagr_b'] > at['spy_b']
    return s, w, a


def kredit_at(at):
    """Lulus ujian bebas AUTOTUNE = label dikunci SEDERHANA/TINGGI (CAGR OOS-A dan OOS-B > SPY dan MDD OOS-A >= -30%;
    AUTOTUNE/SPEC.md; sama dengan pintu B dan corong halaman)."""
    return bool(at) and at.get('label') in AT_LULUS


def kekal(lulus_bebas):
    """Pecahan prior backtest dikekalkan: asas 25% + 25% HANYA jika lulus AUTOTUNE (ujian bebas). S1–S4 dan WFO tidak bebas
    (dalam sampel / separa dalam sampel): 0 kredit (audit 25 Okt 2026: 8/22 kredit WFO jatuh pada kaedah DITOLAK)."""
    return ASAS_KEKAL + TAMBAH_KEKAL * bool(lulus_bebas)


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
# v4: buka_keluar (lorong 1 keluar pada BUKA), hb (harga beli pada skala stor), kohort (label kohort C jika ada)
LAJUR_TAMBAH = ['buka_keluar', 'hb', 'kohort']


def buka_keluar_c(teks):
    """Posisi C keluar pada BUKA (isyarat keluar, jurang bawah henti / atas sasaran) daripada teks isyarat_keluar."""
    t = str(teks).lower()
    return 'isyarat keluar' in t or 'buka bawah henti' in t or 'buka atas sasaran' in t


def buka_keluar_lejar(sebab, harga_keluar, henti, sasaran):
    """Posisi Lejar keluar pada BUKA: isyarat keluar (jual buka esok), atau henti/sasaran dengan harga keluar melepasi paras
    (jurang buka); henti/sasaran tepat pada paras = dalam hari (dinilai pada tutup hari keluar, anggaran)."""
    s = str(sebab); hk, h, g = nombor(harga_keluar), nombor(henti), nombor(sasaran)
    if s == 'isyarat keluar':
        return True
    if s == 'henti' and hk is not None and h is not None:
        return hk < h - 1e-9
    if s == 'sasaran' and hk is not None and g is not None:
        return hk > g + 1e-9
    return False


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
        return pd.DataFrame(columns=LAJUR_POS + LAJUR_TAMBAH)
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
                         sumber='lejar', buka_keluar=t1 and buka_keluar_lejar(r.sebab_keluar, r.harga_keluar, r.henti, r.sasaran),
                         hb=hb, kohort='lejar'))
    return pd.DataFrame(rows, columns=LAJUR_POS + LAJUR_TAMBAH)


def muat_c(pt=PT, akhir=None, buka=None):
    """Posisi sah Papertrade C (semua claude*.csv): lajur LAJUR_POS. Lorong 1 = untung C (akhir jika keluar; jika dipegang,
    dinilai pada tutup terakhir `akhir` (harga hingga sesi Lejar, satu vintaj dengan Lejar), atau untung semasa C jika tiada
    harga). Lorong 2 yang masih dipegang dinilai pada tutup terakhir (akhir)."""
    f = sorted(glob.glob(os.path.join(pt, 'claude*.csv')))
    if not f:
        return pd.DataFrame(columns=LAJUR_POS + LAJUR_TAMBAH)
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
                         hasil2=bersih(g2) if g2 is not None else None, sumber='C',
                         buka_keluar=t1 and buka_keluar_c(getattr(r, 'isyarat_keluar', '')), hb=hb,
                         kohort=str(getattr(r, 'kohort', '') or '')))
    return pd.DataFrame(rows, columns=LAJUR_POS + LAJUR_TAMBAH)


def pisah_backfill(C, mula=BUKTI_MULA_C):
    """(C bukti hadapan, C isi semula): kohort C 8–13 Okt 2026 ialah isi semula (backfill; audit 25 Okt 2026), jadi bukti
    hadapan C bermula `mula`. Lajur kohort (jika diisi agen lain) yang mengandungi 'backfill' atau 'isi' juga dikecualikan."""
    if not len(C):
        return C, C
    k = C['kohort'].astype(str).str.lower() if 'kohort' in C else pd.Series('', index=C.index)
    bf = (C.tarikh_beli < mula) | k.str.contains(r'backfill|isi[ _-]?semula', regex=True)
    return C[~bf], C[bf]


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


def se_dua_hala(x, hari, saham):
    """Ralat piawai purata berkelompok dua hala (Cameron, Gelbach & Miller 2011): V = V_hari + V_saham - V_hari∩saham, setiap
    satu CR1 (G/(G-1) x Σ jumlah sisa kelompok² / n²); V <= 0 -> maks(V_hari, V_saham). n berkesan = s² / V (maks n).
    < HARI_KLUSTER_MIN hari beli: n berkesan = bilangan hari (konservatif) dan se = s / √nb.
    -> dict(se, nb, g_hari, g_saham); n < 2 -> se None, nb = n."""
    x = np.asarray(x, float); n = len(x)
    hari = np.asarray(hari).astype(str); saham = np.asarray(saham).astype(str)
    gh, gs = len(set(hari)), len(set(saham))
    if n < 2:
        return dict(se=None, nb=float(n), g_hari=gh, g_saham=gs)
    e = x - x.mean(); s2 = float(x.var(ddof=1))

    def V(k):
        g = pd.Series(e).groupby(k).sum(); G = len(g)
        return G / (G - 1) * float((g ** 2).sum()) / n ** 2 if G > 1 else float((e.sum()) ** 2) / n ** 2

    if gh < HARI_KLUSTER_MIN:
        nb = float(min(n, gh)); return dict(se=math.sqrt(s2 / nb) if s2 > 0 else 0.0, nb=nb, g_hari=gh, g_saham=gs)
    vh, vs, vhs = V(hari), V(saham), V(np.char.add(np.char.add(hari, '|'), saham))
    v = vh + vs - vhs
    if v <= 0:
        v = max(vh, vs)
    if v <= 0 or s2 <= 0:
        return dict(se=0.0, nb=float(gh), g_hari=gh, g_saham=gs)
    return dict(se=math.sqrt(v), nb=float(min(n, s2 / v)), g_hari=gh, g_saham=gs)


def muat_ew(path=EW_HARIAN):
    """data/analisis/ew_harian.csv (standard/penanda_ew.py; baca sahaja) -> DataFrame ikut tarikh 'YYYY-MM-DD': ew_cc, ew_oc,
    ew_indeks dan ew_co = (1 + cc) / (1 + oc) - 1 (tutup semalam -> buka; anggaran daripada purata). None jika tiada fail."""
    if not os.path.exists(path):
        return None
    e = pd.read_csv(path, dtype={'tarikh': str}).set_index('tarikh').sort_index()
    e['ew_co'] = (1 + e.ew_cc) / (1 + e.ew_oc) - 1
    return e


def ew_tempoh(ew, mula, akhir, buka=None):
    """Pulangan EW (pecahan) bagi setiap tempoh: beli BUKA mula, nilai TUTUP akhir (= penanda_ew.tempoh), atau BUKA akhir jika
    buka (keluar pada buka: hingga tutup sesi sebelum akhir x (1 + ew_co[akhir])). akhir bukan sesi siri -> sesi terakhir <= akhir
    (nilai tutup). NaN jika mula bukan sesi siri atau akhir < mula. Bervektor (mula, akhir, buka: senarai sama panjang)."""
    mula = np.asarray(mula, dtype=str); akhir = np.asarray(akhir, dtype=str); n = len(mula)
    buka = np.zeros(n, bool) if buka is None else np.asarray(buka, bool)
    ix = ew.index.values.astype(str); m = len(ix)
    if not n or not m:
        return np.full(n, np.nan)
    oc, co = ew.ew_oc.values.astype(float), ew.ew_co.values.astype(float)
    L = np.concatenate([[0.0], np.cumsum(np.log1p(ew.ew_cc.values.astype(float)))])   # L[k] = Σ cc[0..k-1]
    i0 = np.searchsorted(ix, mula); j0 = np.minimum(i0, m - 1)
    ok = (i0 < m) & (ix[j0] == mula)
    i1 = np.searchsorted(ix, akhir, side='right') - 1; j1 = np.maximum(i1, 0)
    ok &= i1 >= i0
    tepat = (i1 >= 0) & (ix[j1] == akhir)
    tutup = (1 + oc[j0]) * np.exp(L[j1 + 1] - L[j0 + 1]) - 1
    b = (1 + oc[j0]) * np.exp(L[j1] - L[j0 + 1]) * (1 + co[j1]) - 1
    r = np.where(buka & tepat & (i1 > i0), b, tutup)
    return np.where(ok, r, np.nan)


def tambah_lebihan(P, ew, kini):
    """Lajur ew (%: EW alam tempoh sama) dan lebihan (= hasil1 - ew, %) setiap posisi: akhir = tarikh keluar lorong 1 (BUKA jika
    buka_keluar) atau kini (posisi terbuka dinilai pada tutup kini, seperti hasil1)."""
    P = P.copy()
    if ew is None or not len(P):
        P['ew'] = np.nan; P['lebihan'] = np.nan
        return P
    t1 = P.tutup1.astype(bool) & (P.tarikh_keluar.astype(str) != '')
    akhir = np.where(t1, P.tarikh_keluar.astype(str), str(kini))
    bk = (P['buka_keluar'].fillna(False).astype(bool) if 'buka_keluar' in P else pd.Series(False, index=P.index)) & t1
    P['ew'] = ew_tempoh(ew, P.tarikh_beli.astype(str).values, akhir, bk.values) * 100
    P['lebihan'] = pd.to_numeric(P.hasil1, errors='coerce') - P['ew']
    return P


def tutup_stor(saham, mula, stor=STOR, path=TERKINI):
    """{(ticker, 'YYYY-MM-DD'): tutup} sejak mula bagi saham diberi: terkini.csv didahulukan, stor repo selebihnya (seperti
    harga_akhir) — untuk pulangan umur tetap."""
    out, saham, m = {}, set(saham), str(mula).replace('-', '')
    for f in [os.path.join(stor, 'harga_A.csv'), os.path.join(stor, 'harga_B.csv'), path]:
        if not saham or not os.path.exists(f):
            continue
        x = pd.read_csv(f, usecols=['ticker', 'date', 'close'], dtype={'date': str})
        x = x[x.ticker.isin(saham) & (x.date >= m)]
        out.update({(t, f'{d[:4]}-{d[4:6]}-{d[6:8]}'): float(c) for t, d, c in zip(x.ticker, x.date, x.close)})
    return out


def tambah_umur_tetap(P, ew, tutup, sesi, kini, ks=UMUR_TETAP):
    """Lajur x5/x10/x20: lebihan EW (%) pada umur tetap k sesi (sesi beli + k), hanya bagi posisi yang sesi itu <= kini (tiada
    sensor kanan: setiap posisi dinilai pada umur sama). Lorong 1 keluar pada/sebelum sesi itu -> hasil akhir lawan EW hingga
    keluar (tunai selepas keluar = 0); selainnya tutup sesi itu (harga beli dilaras hb, bersih kos) lawan EW hingga tutup itu."""
    P = P.copy()
    for k in ks:
        P[f'x{k}'] = np.nan
    if ew is None or not len(P) or 'hb' not in P:
        return P
    pos = {d: i for i, d in enumerate(sesi)}
    mula, akhir, buka, nilai, kol, baris = [], [], [], [], [], []
    for j, r in enumerate(P.itertuples(index=False)):
        i0 = pos.get(r.tarikh_beli)
        if i0 is None:
            continue
        for k in ks:
            if i0 + k >= len(sesi) or sesi[i0 + k] > str(kini):
                continue
            dk = sesi[i0 + k]
            if r.tutup1 and r.tarikh_keluar and r.tarikh_keluar <= dk:
                v, a, b = nombor(r.hasil1), r.tarikh_keluar, getattr(r, 'buka_keluar', False) == True  # noqa: E712 (NaN -> False)
            else:
                c, hb = tutup.get((r.saham, dk)), nombor(r.hb)
                v, a, b = (bersih((c / hb - 1) * 100) if c and hb else None), dk, False
            if v is None:
                continue
            mula.append(r.tarikh_beli); akhir.append(a); buka.append(b); nilai.append(v); kol.append(f'x{k}'); baris.append(j)
    if baris:
        e = ew_tempoh(ew, mula, akhir, buka) * 100
        for j, c, v, x in zip(baris, kol, nilai, e):
            if not np.isnan(x):
                P.iat[j, P.columns.get_loc(c)] = v - x
    return P


def holm(p):
    """p terlaras Holm (step-down, FWER) bagi senarai p; None dikekalkan dan tidak dikira dalam keluarga."""
    idx = sorted((i for i, v in enumerate(p) if v is not None), key=lambda i: p[i])
    m, out, naik = len(idx), list(p), 0.0
    for k, i in enumerate(idx):
        naik = max(naik, min(1.0, (m - k) * p[i])); out[i] = naik
    return out


def z_daripada_p(p):
    """z sehala bagi p (Φ⁻¹(1 - p)), dihad ±8; None jika p None."""
    if p is None:
        return None
    return float(max(-8.0, min(8.0, ND.inv_cdf(min(1 - 1e-15, max(1e-15, 1 - p))))))


def sprt(c, mu1, sd, tarikh=None, winsor=None, alfa=SPRT_ALFA, beta=SPRT_BETA, n_min=None):
    """SPRT Wald atas purata lebihan EW kohort harian matang c (susunan tarikh beli): H0 mu = 0 (lebihan <= 0 selepas kos;
    sempadan) lawan H1 mu = mu1 (jangkaan dipotong, skala kohort). Teguh (winsor = dict(lo, hi, h0, h1, sd) daripada
    kalibrasi_skor.py sprt_winsor): kohort diwinsor [lo, hi] ~ Normal(h0 atau h1, sd²), llr = Σ (h1 - h0)(x - (h0 + h1)/2) / sd²;
    tanpa winsor: kohort mentah ~ Normal(0 atau mu1, sd²). Had = [ln(beta / (1 - alfa)), ln((1 - beta) / alfa)]. Keputusan =
    lintasan had PERTAMA selepas >= n_min kohort (pengawal bukti; llr semasa tetap dilapor), kemudian kekal (ujian berjujukan).
    mu1 <= 0 atau tiada -> 'H0' (tiada H1 positif)."""
    n_min = PANTAU_KOHORT if n_min is None else n_min
    A, Bh = math.log((1 - beta) / alfa), math.log(beta / (1 - alfa))
    c = np.asarray(c, float)
    out = dict(status='TERUSKAN', llr=None, had=[round(Bh, 2), round(A, 2)], kohort=int(len(c)), mu1=bulat(mu1, 3),
               sd=bulat(sd, 2), h0=0.0, h1=bulat(mu1, 3), skala='mentah', pada=None, nota='')
    if mu1 is None or mu1 <= 0:
        out.update(status='H0', h1=None, nota='jangkaan dipotong ≤ 0: tiada H1 positif untuk diuji')
        return out
    h0, h1 = 0.0, mu1
    if winsor and None not in (winsor.get('h0'), winsor.get('h1'), winsor.get('sd')) and winsor['h1'] > winsor['h0']:
        c = np.clip(c, winsor['lo'], winsor['hi']); h0, h1, sd = winsor['h0'], winsor['h1'], winsor['sd']
        out.update(h0=bulat(h0, 3), h1=bulat(h1, 3), skala='winsor')
    s = max(SD_KOHORT_MIN, sd or SD_KOHORT_MIN); out['sd'] = bulat(s, 2)
    llr = np.cumsum((h1 - h0) * (c - (h0 + h1) / 2) / s ** 2) if len(c) else np.zeros(0)
    out['llr'] = round(float(llr[-1]), 3) if len(llr) else 0.0
    for i in range(n_min - 1, len(llr)):
        if llr[i] >= A or llr[i] <= Bh:
            out.update(status='H1' if llr[i] >= A else 'H0', pada=(str(tarikh[i]) if tarikh is not None else i + 1))
            break
    if out['status'] == 'TERUSKAN' and len(c) < n_min:
        out['nota'] = f'{len(c)} kohort matang (< {n_min}): belum diputuskan'
    return out


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
               pangkas=None, median=None, n_berkesan=0.0, hari_beli=0, lintas_earnings=0, purata_tanpa_earnings=None,
               nb_mentah=0.0, lebihan=None, lebihan_sd=None, lebihan_se=None, z=None, p=None, g_saham=0, lebihan_saham=None,
               lebihan_n=0, kohort_lebihan=pd.Series(dtype=float), mula=None)
    for k in UMUR_TETAP:
        out[f'r{k}'] = None; out[f'n_r{k}'] = 0
    if not len(P):
        return out
    out['mula'] = str(P.tarikh_beli.min())
    for k in UMUR_TETAP:   # umur tetap: semua posisi yang umurnya cukup (bukan hanya matang)
        if f'x{k}' in P:
            v = pd.to_numeric(P[f'x{k}'], errors='coerce').dropna()
            out[f'r{k}'] = float(v.mean()) if len(v) else None; out[f'n_r{k}'] = int(len(v))
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
        d2 = se_dua_hala(x.values, M.tarikh_beli.values, M.saham.values)
        out.update(matang=int(len(M)), purata=float(x.mean()), menang=float((x > 0).mean()),
                   sd=float(x.std(ddof=1)) if len(M) > 1 else None, pangkas=purata_pangkas(x), median=float(x.median()),
                   n_berkesan=d2['nb'], nb_mentah=d2['nb'], hari_beli=int(M.tarikh_beli.nunique()), g_saham=d2['g_saham'],
                   lintas_earnings=int(le.sum()), purata_tanpa_earnings=float(x[~le.values].mean()) if (~le).any() else None)
        y = M.hasil2.dropna().astype(float)
        out['purata_l2'] = float(y.mean()) if len(y) else None
        if 'lebihan' in M:   # bukti atas LEBIHAN EW (v4): n berkesan dua hala, z, p sehala (H0 lebihan <= 0)
            X = M[pd.to_numeric(M.lebihan, errors='coerce').notna()]
            if len(X):
                xl = X.lebihan.astype(float)
                d = se_dua_hala(xl.values, X.tarikh_beli.values, X.saham.values)
                z = float(xl.mean() / d['se']) if d['se'] else None
                out.update(lebihan=float(xl.mean()), lebihan_sd=float(xl.std(ddof=1)) if len(xl) > 1 else None,
                           lebihan_se=d['se'], n_berkesan=d['nb'], g_saham=d['g_saham'], z=z,
                           p=float(1 - ND.cdf(z)) if z is not None else None, lebihan_n=int(len(xl)),
                           lebihan_saham=float(xl.groupby(X.saham.values).mean().mean()),
                           kohort_lebihan=xl.groupby(X.tarikh_beli.values).mean().sort_index())
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
        out['pantau'] = PANTAU_OK
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
    ikut n berkesan nb jika diberi). BELUM CUKUP: < 20 matang atau < 10 hari beli berbeza (hari). KUAT: lo > 0, dengan lo = had
    bawah skor pada z Z_KUAT (3.0; v4, dahulu 1.96). LEMAH: hi (had atas julat 95%) < 0. Selainnya PERHATI. v4: skor, xbar dan
    mu0 ialah LEBIHAN atas EW / belian rawak, jadi KUAT = edge > 0, bukan pulangan > 0."""
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


def nb_perlu(mu0, sd, n0, z=Z_KUAT):
    """n berkesan hadapan yang diperlukan untuk BUKTI: julat z skor (v4: z = Z_KUAT 3.0, sama dengan KUAT) tidak merangkumi 0
    jika purata hadapan = jangkaan dipotong mu0, iaitu |mu0| - z x SD / sqrt(n0 + nb) > 0 -> nb = (z x SD / |mu0|)^2 - n0 (SD
    seperti skor(): hadapan jika >= 20 matang, jika tidak backtest; min SD_MIN). Lantai NB_MIN (pengawal bukti minimum; keluar
    BELUM CUKUP pula perlu >= 20 matang dan >= 10 hari beli: g_matang/g_perlu dan tarikh_sebenar). None jika mu0 = 0."""
    if not mu0:
        return None
    return int(max(NB_MIN, math.ceil((z * max(SD_MIN, sd or SD_MIN) / abs(mu0)) ** 2 - n0)))


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
    sw = [r for r in rows if r.get('swing')]
    pecah = dict(matang=sum(r['h_matang'] for r in sw), posisi=sum(r['h_posisi'] for r in sw),
                 kaedah_bukti=sum(r['status'] != 'BELUM CUKUP' for r in sw))
    lain = dict(matang=mat - pecah['matang'], posisi=jum - pecah['posisi'], kaedah_bukti=len(bukti) - pecah['kaedah_bukti'])
    calon = [r for r in rows if r.get('tarikh_sebenar')]
    pt = min(calon, key=lambda r: (r['tarikh_sebenar'], r['kedudukan'] or 10 ** 6)) if calon else None
    top = sorted((r for r in rows if r.get('kedudukan') and r['kedudukan'] <= TOP_N), key=lambda r: r['kedudukan'])
    t5 = [r.get('tarikh_sebenar') for r in top]
    t5 = [min((x for x in t5 if x), default=None), max(t5) if t5 and all(t5) else None]
    pertama = dict(id=pt['id'], kedudukan=pt['kedudukan'], tarikh=pt['tarikh_sebenar']) if pt else None
    kd = lambda r: f"#{r['kedudukan']}" if r['kedudukan'] else 'bukan swing/sampel kecil'
    pisah = (f"swing {pecah['matang']:,}/{pecah['posisi']:,}, bukan swing {lain['matang']:,}/{lain['posisi']:,} matang/posisi; "
             f"bukti hadapan sejak {tarikh_ms(BUKTI_MULA_C)} (C) / Lejar")
    if not bukti:
        teks = (f"Fasa 0 — skor = lebihan backtest dipotong: 0 kaedah ada bukti hadapan ({mat:,} daripada {jum:,} posisi hadapan "
                f"matang; {pisah}). Status sebenar pertama ±{tarikh_ms(pt['tarikh_sebenar']) if pt else '–'}"
                + (f" ({pt['id']}, {kd(pt)})" if pt else '')
                + f"; {TOP_N} teratas ±{tarikh_ms(t5[0])} – {tarikh_ms(t5[1]) if t5[1] else 'lebih lewat'}. Bukan cadangan wang sebenar.")
    else:
        teks = (f"Fasa 1 — {len(bukti)} kaedah ada bukti hadapan (≥ {N_MIN} matang, ≥ {N_HARI_MIN} hari beli; swing "
                f"{pecah['kaedah_bukti']}); {mat:,} daripada {jum:,} posisi matang ({pisah}). Kaedah lain masih lebihan backtest "
                "dipotong. Bukan cadangan wang sebenar.")
    return dict(matang_hadapan=int(mat), jumlah_hadapan=int(jum), kaedah_bukti=len(bukti), tarikh_sebenar_pertama=pertama,
                tarikh_top5=t5, teks=teks, swing=pecah, bukan_swing=lain)


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


# ---------------------------------------------------------------- v4: bendera, pintu wang sebenar, corong, ramalan
def ciri_kaedah(kod=KOD_KAEDAH, jenis=JENIS):
    """Klasifikasi regex KASAR kod entry setiap kaedah (bahagian sebelum def hampir; port skrip audit a4_isyarat/ciri_kaedah.py):
    tinggi52 (dekat tinggi 52 minggu), rs (RS keratan rentas), rejim (SPY/QQQ), volum, adr, ketat (kontraksi/julat sempit) +
    jenis (kod/jenis_kaedah.csv: momentum/pantulan). -> {id: dict}."""
    J = pd.read_csv(jenis).set_index('kaedah').jenis.to_dict() if os.path.exists(jenis) else {}
    out = {}
    for f in glob.glob(os.path.join(kod, 'M*.py')):
        mid = os.path.basename(f)[:-3]
        if not re.fullmatch(r'M\d+', mid):
            continue
        t = open(f, encoding='utf-8').read().split('def hampir')[0]
        c = '\n'.join(l.split('#')[0] for l in t.splitlines()
                      if not re.match(r'\s*(ID|NAMA|VARIAN|TMAX|WARM|PERLU_BAR|HENTI_KOD|KELUAR_KOD)\s*=', l))
        out[mid] = dict(tinggi52=bool(re.search(r'rolling\((252|250|260)\)\.max|h252|H252|hi52|52w|tinggi52', c, re.I)),
                        rs=bool(re.search(r'rank\(axis=1|SILANG\s*=\s*True', c)),
                        rejim=bool(re.search(r"idx\[['\"](SPY|QQQ)['\"]\]|idx\.get\(['\"](SPY|QQQ)", c)),
                        volum=bool(re.search(r'\.volume|\bv\.|\bv\s*[<>]=?|\bV\[|vol', c, re.I)),
                        adr=bool(re.search(r'adr|ADR', c)),
                        ketat=bool(re.search(r'vcp|kontrak|ketat|sempit|nr7|nr4|inside|squeeze|julat|tight|bbw|width', c, re.I)),
                        jenis=J.get(mid, ''))
    return out


def kelas_ciri(c):
    """PANTULAN (jenis pantulan) / MOMENTUM_PRO ((tinggi52 atau RS) + volum + (kontraksi, ADR atau rejim)) / PENUNJUK."""
    if not c:
        return None
    if c.get('jenis') == 'pantulan':
        return 'PANTULAN'
    if (c['tinggi52'] or c['rs']) and c['volum'] and (c['ketat'] or c['adr'] or c['rejim']):
        return 'MOMENTUM_PRO'
    return 'PENUNJUK'


def pendua_isyarat(folder=ISYARAT, susunan=None, ambang=PENDUA_AMBANG, n_min=PENDUA_MIN):
    """{id: (induk, pecahan terkandung, n isyarat)}: kaedah dengan >= n_min isyarat malam (saham, tarikh_data) yang >= ambang
    terkandung dalam set kaedah lain yang lebih besar (sama besar: kaedah lebih awal dalam susunan katalog = induk).
    Sumber: data/isyarat/*.csv.gz (semua isyarat malam, dirancang atau tidak)."""
    f = sorted(glob.glob(os.path.join(folder, '*.csv.gz')))
    if not f:
        return {}
    I = pd.concat([pd.read_csv(p, usecols=['tarikh_data', 'kaedah', 'saham'], dtype=str) for p in f], ignore_index=True)
    S = {m: set(zip(g.saham, g.tarikh_data)) for m, g in I.groupby('kaedah')}
    tertib = {m: i for i, m in enumerate(susunan or sorted(S))}
    out = {}
    for a, A in S.items():
        if len(A) < n_min:
            continue
        calon = []
        for b, Bs in S.items():
            if b == a or len(Bs) < len(A) or (len(Bs) == len(A) and tertib.get(b, 10 ** 6) > tertib.get(a, 10 ** 6)):
                continue
            k = len(A & Bs) / len(A)
            if k >= ambang:
                calon.append((k, len(Bs), -tertib.get(b, 10 ** 6), b))
        if calon:   # induk = pecahan terkandung tertinggi, kemudian set terbesar, kemudian lebih awal dalam katalog
            k, _, _, b = max(calon)
            out[a] = (b, k, len(A))
    return out


def bina_bendera(kat, REG, kini, isyarat=ISYARAT, kod=KOD_KAEDAH, jenis=JENIS):
    """Senarai bendera kaedah (id, bendera, sebab, sumber): DITOLAK (registry 431), ARTIFAK (pandang hadapan, ARTIFAK),
    HAMPIR_PENDUA:<induk> (pendua_isyarat) dan CIRI:<kelas> (kelas_ciri; regex kasar). Tarikh diisi oleh tulis_bendera()."""
    ids = [m for m, _, _ in kat]
    pd_ = pendua_isyarat(isyarat, ids); ci = ciri_kaedah(kod, jenis)
    out = []
    for m in ids:
        if (REG.get(m) or {}).get('keputusan') == 'DITOLAK':
            out.append(dict(id=m, bendera='DITOLAK', sebab='keputusan registry set 431 = DITOLAK',
                            sumber='data/registry_M_gabung.csv'))
        if m in ARTIFAK:
            out.append(dict(id=m, bendera='ARTIFAK', sebab=ARTIFAK[m], sumber='AUTOTUNE/hasil/AUDIT_M81.md'))
        if m in pd_:
            b, k, n = pd_[m]
            out.append(dict(id=m, bendera=f'HAMPIR_PENDUA:{b}', sebab=f'{k:.0%} daripada {n} isyarat malam terkandung dalam {b}',
                            sumber='data/isyarat/*.csv.gz'))
        k = kelas_ciri(ci.get(m))
        if k:
            c = ci[m]
            out.append(dict(id=m, bendera=f'CIRI:{k}', sebab='regex kasar kod entry: ' + (', '.join(
                x for x in ('tinggi52', 'rs', 'rejim', 'volum', 'adr', 'ketat') if c[x]) or 'tiada ciri') + f"; jenis {c['jenis'] or '?'}",
                sumber='kod/kaedah/*.py, kod/jenis_kaedah.csv'))
    return out


def tulis_bendera(bendera, kini, path=BENDERA):
    """Tulis bendera_kaedah.csv (id, bendera, sebab, sumber, tarikh); tarikh = tarikh pertama (id, bendera) dikesan (dikekalkan
    daripada fail sedia ada), selainnya kini."""
    lama = {}
    if os.path.exists(path):
        x = pd.read_csv(path, dtype=str, keep_default_na=False)
        lama = {(a, b): t for a, b, t in zip(x.id, x.bendera, x.tarikh)}
    d = pd.DataFrame([dict(b, tarikh=lama.get((b['id'], b['bendera']), str(kini))) for b in bendera],
                     columns=['id', 'bendera', 'sebab', 'sumber', 'tarikh'])
    os.makedirs(os.path.dirname(path), exist_ok=True)
    d.to_csv(path, index=False)
    return d


def muat_ikut_id(path):
    """Fail JSON pilihan (pra_daftar.json, ujian_pit.json; mungkin dijana agen lain) -> {id: dict}. Format diterima: senarai id,
    senarai {id: …}, {id: {…}} atau salah satu itu di bawah 'kaedah'/'rows'. Tiada fail atau rosak -> None."""
    try:
        d = json.load(open(path, encoding='utf-8'))
    except (OSError, ValueError):
        return None
    if isinstance(d, dict):
        d = d.get('kaedah', d.get('rows', d))
    if isinstance(d, list):
        return {(x if isinstance(x, str) else x.get('id')): ({} if isinstance(x, str) else x) for x in d
                if isinstance(x, str) or (isinstance(x, dict) and x.get('id'))}
    if isinstance(d, dict):
        return {k: (v if isinstance(v, dict) else dict(nilai=v)) for k, v in d.items() if re.fullmatch(r'M\d+', str(k))}
    return None


def inkubasi(mula, kini, sesi, ew):
    """(sesi inkubasi sejak mula hingga kini inklusif, pembetulan EW alam terbesar dalam tempoh itu, pecahan puncak ke lembah)."""
    if not mula:
        return 0, None
    n = sum(1 for x in sesi if mula <= x <= str(kini))
    dd = None
    if ew is not None:
        e = ew.ew_indeks[(ew.index >= mula) & (ew.index <= str(kini))]
        if len(e):
            dd = float((1 - e / e.cummax()).max())
    return n, dd


def muat_slot(path=GABUNGAN_BEKU, slot=SLOT, ew=None):
    """{id: butiran pintu E}: portfolio 10 slot berkaitan kaedah (TOP1_10 = kaedah #1 sahaja; GABUNGAN_10 = ahli gabungan
    beku) lawan kawalan RAWAK_KAEDAH_10, SPY dan EW alam (tempoh sama). Pulangan % sejak mula jejak."""
    try:
        g = json.load(open(path, encoding='utf-8'))
    except (OSError, ValueError):
        return {}

    def pul(nm):
        try:
            e = pd.read_csv(os.path.join(slot, f'{nm}_ekuiti.csv'), dtype={'tarikh': str})
        except (OSError, ValueError):
            return None
        return e if len(e) else None

    kaw = pul('RAWAK_KAEDAH_10')
    peta = {k['id']: 'GABUNGAN_10' for k in g.get('kaedah', []) if k.get('id')}
    t1 = ((g.get('rujukan') or {}).get('TOP1_10') or {}).get('id')
    if t1:
        peta[t1] = 'TOP1_10'
    out = {}
    for m, nm in peta.items():
        e = pul(nm)
        if e is None:
            continue
        a, b = str(e.tarikh.iloc[0]), str(e.tarikh.iloc[-1])
        ew_p = None
        if ew is not None:
            s = ew.ew_indeks[ew.index < a]; t = ew.ew_indeks[ew.index <= b]
            if len(s) and len(t):
                ew_p = (float(t.iloc[-1] / s.iloc[-1]) - 1) * 100
        k = None
        if kaw is not None:
            kk = kaw[kaw.tarikh.astype(str) <= b]
            k = (float(kk.ekuiti.iloc[-1]) - 1) * 100 if len(kk) else None
        out[m] = dict(portfolio=nm, kawalan='RAWAK_KAEDAH_10', mula=a, akhir=b, sesi=int(len(e)),
                      pulangan=bulat((float(e.ekuiti.iloc[-1]) - 1) * 100, 2), kawalan_pulangan=bulat(k, 2),
                      spy=bulat((float(e.spy.iloc[-1]) - 1) * 100, 2), ew=bulat(ew_p, 2))
    return out


def pintu_kaedah(r, bendera, pra, pit, ink, slot):
    """Pintu wang sebenar A–F satu kaedah -> (pintu {A..F: bool/None}, pintu_lulus (berturut dari A), kurang [teks BM]).
    A: dibekukan & didaftar (pra_daftar.json); B: lulus ujian bebas (AUTOTUNE SEDERHANA/TINGGI atau ujian_pit.json lulus_B) dan
    bukan ARTIFAK/HAMPIR_PENDUA; C: bukti hadapan lebihan EW > 0, z terlaras Holm >= 3, >= 40 hari beli matang; D: inkubasi >= 126
    sesi termasuk pembetulan EW >= 10%; E: portfolio 10 slot berkaitan atasi kawalan + SPY + EW selepas >= 126 sesi (None jika
    tiada portfolio); F: modal berperingkat (belum bermula: sentiasa False)."""
    kurang = []
    A = bool(pra) and r['id'] in pra
    if not A:
        kurang.append('A: belum dibekukan/didaftar' + ('' if pra is not None else ' (tiada pra_daftar.json)'))
    halang = [b for b in bendera if b.startswith(('ARTIFAK', 'HAMPIR_PENDUA'))]
    pit_b = bool((pit or {}).get(r['id'], {}).get('lulus_B'))
    at_ok = r.get('at_label') in AT_LULUS
    Bp = (at_ok or pit_b) and not halang
    if not Bp:
        kurang.append('B: ' + (f"{', '.join(halang)} tidak boleh lulus" if halang else
                               f"AUTOTUNE {r.get('at_label') or 'tiada'}" + ('' if pit is not None else '; tiada ujian PIT')))
    hb_, z, lb = r.get('h_hari_beli') or 0, r.get('h_z_terlaras'), r.get('h_lebihan')
    C = lb is not None and lb > 0 and z is not None and z >= Z_KUAT and hb_ >= PINTU_C_HARI
    if not C:
        kurang.append(f"C: {hb_}/{PINTU_C_HARI} hari beli matang" + (f", lebihan {lb:+.2f}%" if lb is not None else '')
                      + (f", z terlaras {z:.1f}/{Z_KUAT:.0f}" if z is not None else ''))
    n, dd = ink
    D = n >= PINTU_D_SESI and dd is not None and dd >= PINTU_D_EW
    if not D:
        kurang.append(f"D: inkubasi {n}/{PINTU_D_SESI} sesi" + (f", pembetulan EW {dd:.0%}/{PINTU_D_EW:.0%}" if dd is not None else ''))
    if slot:
        E = slot['sesi'] >= PINTU_E_SESI and None not in (slot['pulangan'], slot['kawalan_pulangan'], slot['spy'], slot['ew']) and \
            slot['pulangan'] > max(slot['kawalan_pulangan'], slot['spy'], slot['ew'])
        if not E:
            kurang.append(f"E: {slot['portfolio']} {slot['sesi']}/{PINTU_E_SESI} sesi")
    else:
        E = None
        kurang.append('E: tiada portfolio 10 slot berkaitan')
    F = False
    kurang.append('F: modal berperingkat belum bermula')
    p = dict(A=A, B=Bp, C=C, D=D, E=E, F=F)
    lulus = 0
    for k in 'ABCDEF':
        if not p[k]:
            break
        lulus += 1
    return p, lulus, kurang


CORONG = ['Semua', 'Swing 3–30', 'Bukan DITOLAK/ARTIFAK', 'Lulus B', 'Lulus C', 'Lulus D', 'Calon wang sebenar']


def corong(rows):
    """Corong pintu (kumulatif): Semua -> swing 3–30 -> bukan DITOLAK/ARTIFAK -> lulus B -> C -> D -> calon (semua pintu A–F)."""
    s = list(rows); out = [dict(peringkat=CORONG[0], n=len(s))]
    langkah = [lambda r: r['swing'], lambda r: not any(b in ('DITOLAK', 'ARTIFAK') for b in r['bendera']),
               lambda r: r['pintu']['B'], lambda r: r['pintu']['C'], lambda r: r['pintu']['D'],
               lambda r: all(r['pintu'][k] for k in 'ABCDEF')]
    for nm, f in zip(CORONG[1:], langkah):
        s = [r for r in s if f(r)]; out.append(dict(peringkat=nm, n=len(s)))
    return out


def susun_pintu(rows):
    """susunan_pintu (swing sahaja): bukan DITOLAK/ARTIFAK dahulu, kemudian pintu_lulus, bilangan pintu B–E lulus, P(lebihan > 0)
    (= Φ(skor / se); tidak bergantung pada hari pegang, tidak seperti P(5 teratas) skor sebulan) dan skor sebulan menurun; bukan
    swing = None."""
    sw = [r for r in rows if r['swing']]
    k = lambda r: (any(b in ('DITOLAK', 'ARTIFAK') for b in r['bendera']), -r['pintu_lulus'],
                   -sum(bool(r['pintu'][x]) for x in 'BCDE'), -(r.get('p_lebihan') or 0),
                   -(r['skor_bulan'] if r['skor_bulan'] is not None else -1e9))
    for i, r in enumerate(sorted(sw, key=k), 1):
        r['susunan_pintu'] = i
    for r in rows:
        r.setdefault('susunan_pintu', None)


def tulis_sejarah(rows, kini, path=SEJARAH):
    """Tambah (tarikh, id, skor) larian ini ke sejarah_skor.csv; larian semula tarikh sama menggantikan baris tarikh itu."""
    baru = pd.DataFrame([dict(tarikh=str(kini), id=r['id'], skor=r['skor']) for r in rows], columns=['tarikh', 'id', 'skor'])
    if os.path.exists(path):
        lama = pd.read_csv(path, dtype={'tarikh': str, 'id': str})
        baru = pd.concat([lama[lama.tarikh != str(kini)], baru], ignore_index=True)
    baru = baru.sort_values(['tarikh', 'id'], kind='stable')
    os.makedirs(os.path.dirname(path), exist_ok=True)
    baru.to_csv(path, index=False)
    return baru


def spearman(a, b):
    """Korelasi pangkat Spearman (pangkat purata bagi seri); None jika < 3 pasangan atau varians sifar."""
    a, b = pd.Series(a, dtype=float).rank(), pd.Series(b, dtype=float).rank()
    if len(a) < 3 or a.std() == 0 or b.std() == 0:
        return None
    return float(np.corrcoef(a, b)[0, 1])


def ramalan(sejarah, H, swing_ids, n_min=RAMALAN_MIN_KAEDAH):
    """Ujian "skor meramal?": skor setiap kaedah swing pada larian terakhir minggu t (minggu ISO) lawan purata lebihan EW umur 5
    sesi (x5) posisi bukti hadapan kaedah itu yang DIBELI dalam minggu t+1; Spearman merentas kaedah setiap pasangan minggu (>=
    n_min kaedah), dipurata. None jika sejarah < 2 minggu."""
    if sejarah is None or not len(sejarah):
        return None
    s = sejarah[sejarah.id.isin(swing_ids)].copy()
    s['minggu'] = pd.to_datetime(s.tarikh).dt.strftime('%G-W%V')
    if s.minggu.nunique() < 2:
        return None
    s = s.sort_values('tarikh').groupby(['minggu', 'id']).tail(1)
    X = H[pd.to_numeric(H.get('x5'), errors='coerce').notna()].copy() if len(H) and 'x5' in H else pd.DataFrame(columns=['id', 'tarikh_beli', 'x5'])
    X['minggu'] = pd.to_datetime(X.tarikh_beli).dt.strftime('%G-W%V') if len(X) else []
    hasil = X.groupby(['minggu', 'id']).x5.mean() if len(X) else pd.Series(dtype=float)
    mg = sorted(s.minggu.unique()); rho = []
    for t, t1 in zip(mg, mg[1:]):
        a = s[s.minggu == t].set_index('id').skor
        if t1 not in hasil.index.get_level_values(0):
            continue
        b = hasil.loc[t1]; ids = [i for i in a.index if i in b.index and pd.notna(a[i])]
        if len(ids) >= n_min:
            r = spearman([a[i] for i in ids], [b[i] for i in ids])
            if r is not None:
                rho.append(dict(minggu=t, minggu_hadapan=t1, rho=round(r, 3), n=len(ids)))
    return dict(spearman=round(float(np.mean([x['rho'] for x in rho])), 3) if rho else None, n_minggu=len(rho),
                minggu_sejarah=int(len(mg)), pasangan=rho[-8:],
                nota='skor minggu t lawan lebihan EW umur 5 sesi posisi dibeli minggu t+1 (swing; Spearman merentas kaedah)')


def analisis(kini=None):
    kat = muat_katalog()
    REG = muat_registry({i: v for i, _, v in kat})
    WF, AT = muat_wfo(), muat_autotune()
    sesi_lejar = _lejar_sesi()
    akhir, tarikh_harga = harga_akhir(hingga=kini or sesi_lejar)   # harga hingga sesi Lejar sahaja (satu vintaj)
    kini = kini or sesi_lejar or tarikh_harga or datetime.now(timezone.utc).strftime('%Y-%m-%d')
    L, C = muat_lejar(akhir), muat_c(akhir=akhir)
    Cb, Cbf = pisah_backfill(C)   # v4: bukti hadapan C >= 14 Okt; kohort 8–13 Okt (isi semula) dikecualikan
    H, mula_lejar, tindih = gabung_hadapan(L, Cb)
    EW = muat_ew()
    SESI = sesi_nyse('2026-09-01', str((pd.Timestamp(kini) + pd.Timedelta(days=5 * 366)).date()))
    H = tambah_lebihan(H, EW, kini)
    if len(H):
        H = tambah_umur_tetap(H, EW, tutup_stor(H.saham.unique(), H.tarikh_beli.min()), SESI, kini)
    ERN = muat_earnings()
    KAL, K_CUSUM, KALL = muat_kalibrasi(semua=True)
    Hg = dict(tuple(H.groupby('id'))) if len(H) else {}
    Cg = dict(tuple(C.groupby('id'))) if len(C) else {}
    BEN = bina_bendera(kat, REG, kini)
    bmap = {}
    for x in BEN:
        bmap.setdefault(x['id'], []).append(x['bendera'])
    PRA, PIT, SLOT_E = muat_ikut_id(PRA_DAFTAR), muat_ikut_id(UJIAN_PIT), muat_slot(ew=EW)
    # kadar isyarat sebenar setiap kaedah dalam Lejar Penuh (sesi isyarat dengan sekurang-kurangnya satu belian/belian tertunda)
    sesi_isy, TG = muat_isyarat_lejar()
    I = pd.concat([L[['id', 'tarikh_isyarat']], TG[['id', 'tarikh_isyarat']]], ignore_index=True)
    n_sesi = len(sesi_isy) or int(I.tarikh_isyarat.nunique())
    hari_isy = I.groupby('id').tarikh_isyarat.nunique().to_dict() if len(I) else {}
    pos_isy = I.groupby('id').size().to_dict() if len(I) else {}
    lejar_n = L.groupby('id').size().to_dict() if len(L) else {}
    beli_tunda = next((x for x in SESI if x > kini), None) if len(TG) else None   # belian sesi berikutnya (tunggu.csv)
    akhir_tahu = beli_tunda or kini
    DEPAN = [x for x in SESI if x > akhir_tahu]
    tunda = TG.groupby('id').size().to_dict() if len(TG) else {}
    rows, matang = [], []
    for mid, nama, var in kat:
        r = REG.get(mid) or {}
        w, a = WF.get(mid), AT.get(mid)
        s_sub, s_wfo, s_at = semakan(r, w, a)
        lulus = sum(bool(x) for x in (s_sub, s_wfo, s_at))
        k_at = kredit_at(a)
        kk = kekal(k_at)   # v4: hanya AUTOTUNE (ujian bebas, label SEDERHANA/TINGGI) memberi kredit
        hari = r.get('days')
        swing = bool(hari is not None and SWING[0] <= hari <= SWING[1])
        kal = KAL.get(mid); ka = KALL.get(mid) or {}
        avg_bt = r['avg'] * 100 if r.get('avg') is not None else None
        lb_bt = nombor(ka.get('lebihan_rawak'))
        mu0 = lb_bt * kk if lb_bt is not None else 0.0          # prior atas LEBIHAN, dikecut ke lebihan 0
        mu0_m = avg_bt * kk if avg_bt is not None else 0.0      # prior pulangan mentah (BERSARA / brek bencana sahaja)
        sd0 = sd_backtest(r)   # SD setiap dagangan (anggaran bawah, seperti v3; SD lebihan mentah dikuasai ekor squeeze)
        Pm = Hg.get(mid, H.iloc[:0])
        hd = ringkas_hadapan(Pm, hari, kini, ERN)
        if hd['matang']:
            tb = pd.to_datetime(Pm.tarikh_beli)
            matang.append(Pm[(tb <= pd.Timestamp(kini) - pd.Timedelta(days=hd['umur_hari'])).values & Pm.hasil1.notna().values]
                          .assign(swing=swing))
        n0 = berat_backtest(r.get('n'))
        # skor atas LEBIHAN matang penuh dan n berkesan dua hala; SD hadapan dipakai jika >= N_MIN matang
        nb = hd['n_berkesan'] if hd['lebihan'] is not None else 0.0
        sdf = hd['lebihan_sd'] if hd['matang'] >= N_MIN else None
        mu, lo, hi = skor(mu0, sd0, nb, hd['lebihan'] or 0.0, sdf, n0)
        lo3 = mu - Z_KUAT * (hi - mu) / Z95
        st = status_kaedah(hd['matang'], hd['lebihan'] or 0.0, hd['lebihan_sd'], mu0, lo3, hi, hd['hari_beli'], nb)
        sdm = hd['sd'] if hd['matang'] >= N_MIN else None
        mu_m, lo_m, hi_m = skor(mu0_m, sd_backtest(r), hd['nb_mentah'], hd['purata'] or 0.0, sdm, n0)
        c = Cg.get(mid)
        pt = pantau_kaedah(Pm, hd['umur_hari'], kini, kal, kk, mu_m, lo_m, hi_m, hd['hari_beli'], K_CUSUM, hd['nb_mentah'])
        p_sas, p_amb = teks_pantau(kal, kk, K_CUSUM)
        mk = nombor(ka.get('lebihan_mu_kohort'))
        mu1 = kk * mk if mk is not None else (mu0 if lb_bt is not None else None)
        wz = ka.get('lebihan_winsor') or [None, None]
        wz = dict(lo=wz[0], hi=wz[1], h0=nombor(ka.get('lebihan_h0_winsor')), sd=nombor(ka.get('lebihan_sd_winsor')),
                  h1=nombor((ka.get('lebihan_h1_winsor') or {}).get(str(kk)))) if ka.get('lebihan_winsor') else None
        sp = sprt(hd['kohort_lebihan'].values, mu1, nombor(ka.get('lebihan_sd_kohort')) or sd0, list(hd['kohort_lebihan'].index), wz)
        sebulan = (lambda v: v / hari * HARI_BULAN) if (hari and swing) else (lambda v: None)   # skor sebulan: swing sahaja
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
        mula_ink = hd['mula']
        if PRA and mid in PRA and PRA[mid].get('tarikh'):
            mula_ink = max(str(PRA[mid]['tarikh']), mula_ink or '')
        ink = inkubasi(mula_ink, kini, SESI, EW)
        rows.append(dict(
            id=mid, nama=nama, varian=var, swing=swing,
            hari=bulat(hari, 1), bt_keputusan=r.get('keputusan'), bt_skor=bulat(r.get('skor'), 1), bt_cagr=bulat(r.get('cagr'), 4),
            bt_mdd=bulat(r.get('mdd'), 4), bt_menang=bulat(r.get('win'), 4), bt_purata=bulat(avg_bt, 2), bt_n=r.get('n'),
            bt_setahun=bulat(r.get('setahun'), 1), n0=bulat(n0, 1),
            bt_lebihan=bulat(lb_bt, 2), bt_lebihan_pangkas=bulat(ka.get('lebihan_pangkas'), 2), bt_ew_tempoh=bulat(ka.get('ew_tempoh'), 2),
            bt_lebihan_t=bulat(ka.get('lebihan_t_hari'), 2), bt_u3=bulat(ka.get('u3'), 2),
            subset=f"{r.get('subset_menang', 0)}/{r.get('subset_n', 0)}" if r else None, lulus_subset=s_sub,
            wfo_cagr=bulat(w and w['cagr'], 4), wfo_ew=bulat(w and w['ew'], 4), wfo_mdd=bulat(w and w['mdd'], 4),
            wfo_dsr=bulat(w and w['dsr'], 2), lulus_wfo=s_wfo,
            at_label=a and a.get('label'), at_cagr_a=bulat(a and a.get('cagr_a'), 4), at_cagr_b=bulat(a and a.get('cagr_b'), 4),
            at_spy=bulat(a and a.get('spy_a'), 4), at_cagr_kunci=bulat(a and a.get('cagr_kunci'), 3),
            at_cagr_bersih=bulat(a and a.get('cagr_bersih'), 3), at_dsr=bulat(a and a.get('dsr'), 3), at_pbo=bulat(a and a.get('pbo'), 2),
            lulus_at=s_at, lulus=lulus, kredit_at=k_at, kekal=kk, jangkaan=bulat(mu0, 2), jangkaan_mentah=bulat(mu0_m, 2),
            h_posisi=hd['posisi'], h_tutup=hd['tutup'], h_matang=hd['matang'], h_purata=bulat(hd['purata'], 2),
            h_menang=bulat(hd['menang'], 4), h_purata_l2=bulat(hd['purata_l2'], 2), h_umur=hd['umur_hari'],
            h_pangkas=bulat(hd['pangkas'], 2), h_median=bulat(hd['median'], 2), h_n_berkesan=bulat(nb, 1),
            h_hari_beli=hd['hari_beli'], h_lintas_earnings=hd['lintas_earnings'],
            h_purata_tanpa_earnings=bulat(hd['purata_tanpa_earnings'], 2),
            h_lebihan=bulat(hd['lebihan'], 2), h_lebihan_se=bulat(hd['lebihan_se'], 3), h_z=bulat(hd['z'], 2), h_p=bulat(hd['p'], 4),
            h_g_saham=hd['g_saham'], h_lebihan_saham=bulat(hd['lebihan_saham'], 2),
            **{f'h_r{k}': bulat(hd[f'r{k}'], 2) for k in UMUR_TETAP}, **{f'h_n_r{k}': hd[f'n_r{k}'] for k in UMUR_TETAP},
            matang_mula=hd['matang_mula'], matang_20=hd['matang_20'],
            c_posisi=int(len(c)) if c is not None else 0,
            c_purata=bulat(c.hasil1.dropna().mean(), 2) if c is not None and c.hasil1.notna().any() else None,
            skor=bulat(mu, 2), skor_bawah=bulat(lo, 2), skor_atas=bulat(hi, 2), skor_bawah3=bulat(lo3, 2), skor_mentah=bulat(mu_m, 2),
            p_lebihan=bulat(phi(mu / ((hi - mu) / Z95)), 3) if hi > mu else None,
            skor_bulan=bulat(sebulan(mu), 2), skor_bulan_bawah=bulat(sebulan(lo), 2), skor_bulan_atas=bulat(sebulan(hi), 2),
            lb_bulan=bulat(sebulan(lo), 3),
            g_matang=hd['hari_beli'], g_perlu=N_HARI_MIN, nb=bulat(nb, 1), nb_perlu=nb_perlu(mu0, sdf or sd0, n0),
            tarikh_sebenar=t_sebenar, tarikh_asas=asas,
            ditolak=r.get('keputusan') == 'DITOLAK', lejar_n=int(lejar_n.get(mid, 0)),
            median_bt=bulat(ka.get('median'), 2), pangkas5_bt=bulat(ka.get('u1_pangkas'), 2), pct_top1=bulat(ka.get('pct_top1'), 1),
            status=st, **pt, pantau_sasaran=p_sas, pantau_ambang=p_amb, sprt=sp,
            bendera=bmap.get(mid, []), inkubasi_sesi=ink[0], inkubasi_ew_dd=bulat(ink[1], 3), pintu_e=SLOT_E.get(mid),
            _p=hd['p'], _kb=sebulan(mu), _se=(sebulan(hi) - sebulan(mu)) / Z95 if (hari and swing) else None))
    # p sehala bukti hadapan dilaras Holm merentas kaedah (keluarga = kaedah dengan bukti hadapan lebihan)
    for r, ph in zip(rows, holm([r['_p'] for r in rows])):
        r['h_p_holm'] = bulat(ph, 4); r['h_z_terlaras'] = bulat(z_daripada_p(ph), 2)
    for r in rows:
        r['pintu'], r['pintu_lulus'], r['kurang'] = pintu_kaedah(r, r['bendera'], PRA, PIT, (r['inkubasi_sesi'], r['inkubasi_ew_dd']),
                                                                 r['pintu_e'])
    sw, kecil, lain = susun_kedudukan(rows)
    # peluang pangkat (Monte Carlo) dalam set berkedudukan; selainnya None
    p1, p5, q5, q95 = peluang_pangkat([r['_kb'] for r in sw], [r['_se'] for r in sw])
    for r, a, b, c, d in zip(sw, p1, p5, q5, q95):
        r.update(p_top1=round(float(a), 3), p_top5=round(float(b), 3), pangkat_p5=int(c), pangkat_p95=int(d))
    for r in kecil + lain:
        r.update(p_top1=None, p_top5=None, pangkat_p5=None, pangkat_p95=None)
    semua = sw + kecil + lain
    kelompok_rows(semua, KALL)
    susun_pintu(semua)
    for r in semua:
        r.pop('_kb'); r.pop('_se'); r.pop('_p')
    Mt = pd.concat(matang, ignore_index=True) if matang else pd.DataFrame(columns=list(H.columns) + ['swing'])
    Cbf2 = tambah_lebihan(Cbf, EW, kini) if len(Cbf) else Cbf
    meta = dict(kini=kini, harga_pada=tarikh_harga, mula_lejar=mula_lejar,
                lejar_posisi=int(len(L)), lejar_tindih=tindih, c_posisi=int(len(C)),
                c_pra_lejar=int((Cb.tarikh_beli < mula_lejar).sum()) if mula_lejar and len(Cb) else int(len(Cb)),
                lejar_sesi=sesi_lejar, lejar_sesi_isyarat=n_sesi, beli_tertunda=beli_tunda,
                bukti_mula=dict(c=BUKTI_MULA_C, lejar=mula_lejar),
                kohort_backfill=dict(posisi=int(len(Cbf)),
                                     tarikh=[str(Cbf.tarikh_beli.min()), str(Cbf.tarikh_beli.max())] if len(Cbf) else None,
                                     purata=bulat(pd.to_numeric(Cbf.hasil1, errors='coerce').mean(), 2) if len(Cbf) else None,
                                     lebihan=bulat(pd.to_numeric(Cbf2.lebihan, errors='coerce').mean(), 2) if len(Cbf) else None,
                                     nota='kohort C 8–13 Okt 2026 = isi semula (backfill): tidak dikira dalam bukti hadapan'),
                ew_harian=dict(mula=str(EW.index[0]), akhir=str(EW.index[-1]), sesi=int(len(EW))) if EW is not None else None,
                fasa=fasa_papan(semua), label_semakan=LABEL_SEMAKAN, gabungan_beku_nota=nota_gabungan(semua),
                ringkasan=ringkasan_kumpulan(semua, Mt, H), corong=corong(semua), _bendera=BEN, _H=H)
    return semua, meta


def ringkasan_kumpulan(rows, Mt, H):
    """Ringkasan berasingan swing (pegang 3–30) dan bukan swing: kaedah, posisi, matang, lebihan EW purata posisi matang dan
    ikut saham-hari (pasangan saham + tarikh beli dikira sekali merentas kaedah), umur tetap, status/pantau/SPRT/pintu."""
    sid = {r['id'] for r in rows if r['swing']}
    out = {}
    for nm, ya in (('swing', True), ('bukan_swing', False)):
        R = [r for r in rows if r['swing'] == ya]
        M = Mt[Mt.swing == ya] if len(Mt) else Mt
        x = pd.to_numeric(M.lebihan, errors='coerce') if len(M) else pd.Series(dtype=float)
        Hx = H[H.id.isin(sid) == ya] if len(H) else H
        sh = M.assign(x=x).dropna(subset=['x']).groupby(['saham', 'tarikh_beli']).x.mean() if len(M) else pd.Series(dtype=float)
        o = dict(kaedah=len(R), posisi=int(sum(r['h_posisi'] for r in R)), matang=int(len(M)),
                 lebihan=bulat(x.mean(), 2) if x.notna().any() else None, saham_hari=int(len(sh)),
                 lebihan_saham_hari=bulat(sh.mean(), 2) if len(sh) else None,
                 status={k: sum(r['status'] == k for r in R) for k in STATUS},
                 pantau={k: sum(r['pantau'] == k for r in R) for k in PANTAU_STATUS},
                 sprt={k: sum(r['sprt']['status'] == k for r in R) for k in ('H1', 'H0', 'TERUSKAN')},
                 pintu_lulus={str(k): sum(r['pintu_lulus'] == k for r in R) for k in range(7) if any(r['pintu_lulus'] == k for r in R)})
        for k in UMUR_TETAP:
            v = pd.to_numeric(Hx[f'x{k}'], errors='coerce').dropna() if len(Hx) and f'x{k}' in Hx else pd.Series(dtype=float)
            o[f'r{k}'] = bulat(v.mean(), 2) if len(v) else None; o[f'n_r{k}'] = int(len(v))
        out[nm] = o
    return out


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
    # AUTOTUNE: SPY tempoh kunci (Okt 2024 – Okt 2026) dan ujian bersih (2013–2018, parameter asal); sama bagi semua kaedah
    A = next((v for v in muat_autotune().values() if v.get('spy_bersih') is not None), None) or {}
    out.update(at_kunci_tempoh='Okt 2024 – Okt 2026', at_spy_kunci=bulat(A.get('spy_kunci'), 4),
               at_bersih_tempoh='2013–2018 (parameter asal)', at_spy_bersih=bulat(A.get('spy_bersih'), 4))
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
    """3 penemuan (v4): (1) susunan pintu + corong, (2) bukti hadapan atas lebihan EW (swing/bukan swing dipisah), (3) prior
    lebihan backtest, kredit, bendera dan portfolio 10 slot."""
    out = []
    cr = {x['peringkat']: x['n'] for x in meta.get('corong') or []}
    sw = sorted((r for r in rows if r['swing']), key=lambda r: r['susunan_pintu'] or 10 ** 6)
    maks = max((r['pintu_lulus'] for r in rows), default=0)
    gagal, tiada_e = {}, 0
    for r in sw:
        if not any(b in ('DITOLAK', 'ARTIFAK') for b in r['bendera']):
            tiada_e += r['pintu']['E'] is None
            for k in 'BCDE':
                if not r['pintu'][k]:
                    gagal[k] = gagal.get(k, 0) + 1
    atas = ', '.join(f"{r['id']} (lulus {r['pintu_lulus']}; P(lebihan > 0) {p(r['p_lebihan'], 0)})" for r in sw[:3]) if sw else 'tiada'
    out.append(' → '.join(f"{k} {v}" for k, v in cr.items()) + '. '
               + f"Susunan pintu wang sebenar (bukan skor mentah): pintu lulus berturut maksimum {maks}/6"
               + (' — pintu A gagal bagi semua (tiada pra_daftar.json: kaedah belum dibekukan & didaftar)' if maks == 0 else '')
               + f"; tiga teratas swing ikut susunan pintu: {atas}. Antara swing bukan DITOLAK/ARTIFAK, gagal pintu "
               + ', '.join(f'{k} {v}' for k, v in sorted(gagal.items())) + f' ({tiada_e} tanpa portfolio 10 slot berkaitan). '
               'Bukan cadangan wang sebenar.')
    rk = meta.get('ringkasan') or {}; s, b = rk.get('swing') or {}, rk.get('bukan_swing') or {}
    bf = meta.get('kohort_backfill') or {}
    sp = {k: sum(r['sprt']['status'] == k for r in sw) for k in ('H1', 'H0', 'TERUSKAN')}
    sp0 = sum(r['sprt']['status'] == 'H0' and r['sprt']['llr'] is None for r in sw)
    kuat = [r['id'] for r in rows if r['status'] == 'KUAT']
    pt = {k: [r['id'] for r in rows if r.get('pantau') == k] for k in ('BERSARA', 'GANTUNG', 'AMARAN')}
    f = meta.get('fasa') or {}; t1 = f.get('tarikh_sebenar_pertama') or {}
    teks = (f"Bukti hadapan atas lebihan EW alam (C ≥ {tarikh_ms(BUKTI_MULA_C)}, Lejar ≥ {tarikh_ms(meta.get('mula_lejar'))}; "
            f"{bf.get('posisi', 0)} posisi C isi semula 8–13 Okt dikecualikan): swing {s.get('matang', 0)} matang daripada "
            f"{s.get('posisi', 0)} posisi, lebihan {sg(s.get('lebihan'))} (saham-hari {sg(s.get('lebihan_saham_hari'))}); bukan swing "
            f"{b.get('matang', 0)}/{b.get('posisi', 0)}. Umur tetap 5 sesi (tiada sensor kanan): swing {sg(s.get('r5'))} "
            f"({s.get('n_r5', 0)} posisi), bukan swing {sg(b.get('r5'))} ({b.get('n_r5', 0)}). KUAT (z ≥ {Z_KUAT:.0f}) "
            f"{len(kuat)}: {senarai(kuat)}. SPRT swing: H1 {sp['H1']}, H0 {sp['H0']} ({sp0} kerana jangkaan dipotong ≤ 0), "
            f"TERUSKAN {sp['TERUSKAN']}. Status sebenar pertama ±{tarikh_ms(t1.get('tarikh'))} ({t1.get('id', '–')}).")
    if any(pt.values()):
        teks += ' Pantau: ' + '; '.join(f'{k} ({len(v)}): {senarai(v)}' for k, v in pt.items() if v) + '.'
    out.append(teks)
    lb = [r['bt_lebihan'] for r in sw if r['bt_lebihan'] is not None]
    u3 = [r['bt_u3'] for r in sw if r['bt_u3'] is not None]
    n = {k: sum(1 for r in rows if r[f'lulus_{k}']) for k in ('subset', 'wfo', 'at')}
    wd = sum(1 for r in rows if r['lulus_wfo'] and r['ditolak'])
    bd = {k: sum(any(x.startswith(k) for x in r['bendera']) for r in rows) for k in ('DITOLAK', 'ARTIFAK', 'HAMPIR_PENDUA')}
    sl = ruj.get('slot') or {}
    out.append(f"Prior backtest atas lebihan (belian rawak tempoh sama, bersih kos 0.2% pusingan): {sum(x > 0 for x in lb)}/{len(lb)} "
               f"swing berlebihan > 0 (median {sg(float(np.median(lb)) if lb else None)}); lebihan atas purata dagangan hari sama (u3) "
               f"> 0: {sum(x > 0 for x in u3)}/{len(u3)}. Kredit hanya AUTOTUNE SEDERHANA/TINGGI ({sum(bool(r['kredit_at']) for r in rows)} kaedah) — S1–S4 "
               f"({n['subset']} lulus) dan WFO ({n['wfo']} lulus, {wd} daripadanya DITOLAK) dilapor tanpa kredit. Bendera: DITOLAK "
               f"{bd['DITOLAK']}, ARTIFAK {bd['ARTIFAK']}, HAMPIR_PENDUA {bd['HAMPIR_PENDUA']} (data/analisis/bendera_kaedah.csv). "
               + (f"Portfolio 10 slot sejak {tarikh_ms(sl.get('mula'))}: RS_10 {sg(sl.get('RS_10'))}, RAWAK_10 {sg(sl.get('RAWAK_10'))}, "
                  f"SPY {sg(sl.get('spy'))}." if sl else ''))
    return out


def senarai(ids, had=8):
    return 'tiada' if not ids else ', '.join(ids[:had]) + (f' dan {len(ids) - had} lagi' if len(ids) > had else '')


def tanda(v):
    return '–' if v is None else ('✓' if v else '✗')


def jana_md(rows, meta, ruj, pen, dibina):
    bf = meta.get('kohort_backfill') or {}
    L = ['# Papan Penganalisis — banding semua kaedah (backtest + papertrade)', '',
         f"Dijana {dibina} oleh `standard/penganalisis.py` v{VERSI_FORMULA} (GitHub Actions `analisis.yml`, selepas Lejar Penuh). Data harga "
         f"hingga {tarikh_ms(meta['harga_pada'])}; Lejar sesi terakhir {tarikh_ms(meta['lejar_sesi'])}. Rekod analisis sahaja: tiada order, "
         'tiada wang sebenar. Dashboard: tab Analisis (db `analisis/papan`).', '',
         f"> **{(meta.get('fasa') or {}).get('teks', '')}**", '']
    if meta.get('gabungan_beku_nota'):
        L += [f"Gabungan beku (portfolio_slot GABUNGAN_10): {meta['gabungan_beku_nota']}.", '']
    L += ['## 3 penemuan utama', ''] + [f'{i}. {x}' for i, x in enumerate(pen, 1)] + ['']
    L += ['## Corong pintu wang sebenar', '', '| Peringkat | Kaedah |', '|---|---|'] + \
         [f"| {x['peringkat']} | {x['n']} |" for x in meta.get('corong') or []] + ['',
         'Pintu (setiap kaedah, medan `pintu`): **A** dibekukan & didaftar (data/analisis/pra_daftar.json); **B** lulus ujian bebas '
         '(AUTOTUNE SEDERHANA/TINGGI atau data/analisis/ujian_pit.json lulus_B; ARTIFAK dan HAMPIR_PENDUA tidak boleh lulus); '
         f'**C** bukti hadapan lebihan EW > 0 dengan z terlaras Holm ≥ {Z_KUAT:.0f} dan ≥ {PINTU_C_HARI} hari beli matang; **D** '
         f'inkubasi ≥ {PINTU_D_SESI} sesi termasuk satu pembetulan EW ≥ {PINTU_D_EW:.0%}; **E** portfolio 10 slot berkaitan atasi '
         f'kawalan RAWAK_KAEDAH_10, SPY dan EW selepas ≥ {PINTU_E_SESI} sesi (– jika tiada portfolio); **F** modal berperingkat '
         '(belum bermula). Corong kumulatif; calon wang sebenar = semua pintu A–F lulus.', '']
    rk = meta.get('ringkasan') or {}
    if rk:
        L += ['## Ringkasan swing lawan bukan swing', '',
              '| Kumpulan | Kaedah | Posisi · matang | Lebihan EW matang · saham-hari | Umur tetap r5 · r10 · r20 (n r5) | '
              'SPRT H1 · H0 · TERUSKAN | Pantau |', '|---|---|---|---|---|---|---|']
        for nm, o in rk.items():
            L.append(f"| {nm.replace('_', ' ')} | {o['kaedah']} | {o['posisi']:,} · {o['matang']:,} | {sg(o['lebihan'])} · "
                     f"{sg(o['lebihan_saham_hari'])} ({o['saham_hari']}) | {sg(o['r5'])} · {sg(o['r10'])} · {sg(o['r20'])} ({o['n_r5']}) | "
                     f"{o['sprt']['H1']} · {o['sprt']['H0']} · {o['sprt']['TERUSKAN']} | "
                     + ', '.join(f'{k} {v}' for k, v in o['pantau'].items() if v) + ' |')
        L.append('')
    rm = meta.get('ramalan')
    L += ['## Ujian "skor meramal?"', '',
          ('Belum cukup sejarah (< 2 minggu dalam data/analisis/sejarah_skor.csv); ujian bermula apabila sejarah skor mingguan '
           'bertambah.' if not rm else
           f"Spearman purata skor minggu t lawan lebihan EW umur 5 sesi posisi minggu t+1: {rm['spearman'] if rm['spearman'] is not None else '–'} "
           f"atas {rm['n_minggu']} pasangan minggu (sejarah {rm['minggu_sejarah']} minggu)."), '',
          '## Cara skor dikira (v4)', '',
          '- Prior backtest = LEBIHAN purata dagangan set 431 dalam sampel (varian aktif) atas belian rawak tempoh pegang sama: purata '
          'sama berat 431 saham dari buka hari masuk hingga harga keluar (buka hari keluar jika enjin keluar pada buka; selainnya '
          'tutup), pulangan dagangan bersih kos 0.1% setiap belah (0.2% pusingan) tolak pulangan kasar rawak (kalibrasi_skor.py '
          f'lebihan_rawak). Dikekalkan {int(ASAS_KEKAL * 100)}% + {int(TAMBAH_KEKAL * 100)}% HANYA jika lulus AUTOTUNE (label '
          'SEDERHANA/TINGGI, 2000 saham AS; ujian bebas). S1–S4 = kestabilan dalam sampel dan WFO = separa dalam sampel: dilapor, 0 '
          'kredit. Pengecutan ke lebihan 0 (bukan ke pulangan mentah). u3 = lebihan atas purata semua dagangan semua kaedah hari sama.',
          f"- Bukti hadapan = posisi matang Lejar Penuh + Papertrade C pra-Lejar sejak {tarikh_ms(BUKTI_MULA_C)} ({meta['c_pra_lejar']} "
          f"posisi; {meta['lejar_tindih']} posisi Lejar bertindih dengan C pra-Lejar kaedah+saham sama dibuang). Kohort C 8–13 Okt "
          f"({bf.get('posisi', 0)} posisi, purata {sg(bf.get('purata'))}, lebihan {sg(bf.get('lebihan'))}) = isi semula (backfill), "
          f"dikecualikan. Matang = dibeli ≥ maks({UMUR_MIN} hari, 1.5 × hari pegang backtest) lalu. Setiap posisi dinilai atas "
          'LEBIHAN EW alam Shariah tempoh sama (data/analisis/ew_harian.csv; keluar pada buka = hingga buka hari keluar).',
          f'- Pulangan umur tetap r5/r10/r20 = lebihan EW pada sesi beli + 5/10/20 bagi semua posisi yang umurnya cukup (keluar '
          'lebih awal: hasil akhir; tiada sensor kanan). Purata ikut saham (setiap saham sama berat) dan saham-hari (ringkasan).',
          f'- Skor = (n0 × jangkaan + nb × lebihan matang) ÷ (n0 + nb), n0 = berat backtest (maks {N0}); nb = n berkesan DUA HALA '
          '(kelompok hari beli + saham, SE Cameron–Gelbach–Miller; < 5 hari beli: nb = bilangan hari). Julat 95% = skor ± 1.96 × SD ÷ '
          f'√(n0 + nb); had z {Z_KUAT:.0f} = skor − {Z_KUAT:.0f} × SD ÷ √(n0 + nb). Skor sebulan (swing sahaja) = skor ÷ hari pegang × {HARI_BULAN}.',
          f'- Status: AMARAN = ≥ {N_AMARAN} matang, ≥ {N_HARI_MIN} hari beli, nb ≥ {NB_MIN} dan lebihan matang jauh di bawah jangkaan '
          f'(t < −2); BELUM CUKUP = < {N_MIN} matang atau < {N_HARI_MIN} hari beli; KUAT = had z {Z_KUAT:.0f} skor LEBIHAN > 0; '
          'LEMAH = julat 95% < 0; selainnya PERHATI. p sehala bukti hadapan (H0 lebihan ≤ 0) dilaras Holm merentas kaedah.',
          f'- SPRT Wald (medan sprt): purata lebihan EW kohort harian matang ~ Normal; H0 lebihan = 0 lawan H1 lebihan = jangkaan '
          f'dipotong (skala kohort); α {SPRT_ALFA} (sehala z 3), β {SPRT_BETA}; keputusan pada lintasan pertama selepas ≥ '
          f'{PANTAU_KOHORT} kohort; jangkaan ≤ 0 → H0 (tiada H1 positif).',
          f'- Pantau (brek bencana, pulangan mentah): BELUM CUKUP = < {PANTAU_KOHORT} hari beli matang atau nb < {NB_MIN}; BERSARA = '
          f'P(pulangan ≤ 0) > {PANTAU_P} dengan ≥ {PANTAU_G} hari beli, atau ≥ 2 amaran CUSUM; GANTUNG = kejatuhan ekuiti kohort > '
          f'{PANTAU_DD} × maks backtest, tempoh di bawah puncak > maks backtest, atau purata {PANTAU_BERGULIR} hari beli terakhir < p5 '
          f'bergulir backtest; AMARAN = 1 amaran CUSUM bawah; {PANTAU_OK} = tiada pencetus (BUKAN bukti edge; lihat SPRT).',
          f'- Ranking: kedudukan = skor sebulan lebihan tanpa bundar (swing); P(#1)/P({TOP_N} teratas) Monte Carlo {MC_CABUTAN:,} cabutan '
          f'berbiji; susunan_pintu = bukan DITOLAK/ARTIFAK dahulu, pintu lulus, pintu B–E, P(lebihan > 0) = Φ(skor ÷ se), skor sebulan.',
          f'- Bendera (data/analisis/bendera_kaedah.csv): DITOLAK (registry), ARTIFAK (pandang hadapan), HAMPIR_PENDUA:<induk> '
          f'(≥ {PENDUA_AMBANG:.0%} isyarat malam terkandung dalam kaedah lain, ≥ {PENDUA_MIN} isyarat), CIRI:MOMENTUM_PRO/PENUNJUK/PANTULAN '
          '(klasifikasi regex KASAR kod entry).',
          f"- Label semakan: {LABEL_SEMAKAN['s14']}; {LABEL_SEMAKAN['wfo']}; {LABEL_SEMAKAN['at']}.",
          f'- Swing = purata pegang backtest {SWING[0]}–{SWING[1]} hari dagangan; < {N_BT_MIN} dagangan backtest = sampel kecil (tanpa '
          'nombor kedudukan). Kaedah bukan swing disenarai berasingan dan tiada skor sebulan.', '',
          '## Rujukan', '',
          f"- Backtest dalam sampel ({ruj['is_tempoh']}): EW 431 {p(ruj['is_ew'])}, SPY {p(ruj['is_spy'])} setahun.",
          f"- WFO luar sampel ({ruj['wfo_tempoh']}): EW 423 {p(ruj['wfo_ew'])}, SPY {p(ruj['wfo_spy'])} setahun.",
          f"- AUTOTUNE luar sampel ({ruj['at_tempoh']}): SPY {p(ruj['at_spy'])} setahun."]
    s = ruj.get('slot')
    if s:
        L.append(f"- Portfolio maya 10 slot ({tarikh_ms(s['mula'])} – {tarikh_ms(s['akhir'])}, {s['sesi']} sesi): RS_10 {sg(s['RS_10'])}, "
                 f"RAWAK_10 {sg(s['RAWAK_10'])}, SPY {sg(s['spy'])}. Kajian portfolio: `kajian/KAJIAN_PORTFOLIO.md`.")
    hd = ('| # · pintu | Kaedah | Bendera | Hari | Backtest 431: CAGR · purata · lebihan rawak · u3 | S1–S4 · WFO · AUTOTUNE | '
          'Kekal · jangkaan lebihan % | Hadapan: posisi · matang · mentah · lebihan EW · ikut saham | Umur tetap r5 · r10 · r20 | '
          'nb dua hala · hari beli · saham | z · p Holm · z terlaras | Skor lebihan % [95%] · had z3 | Skor sebulan % [had bawah] | '
          'P(#1) · P(5) · pangkat 90% | Bukti: hari beli /10 · nb / nb perlu · status sebenar | Status | SPRT | Pantau | Pintu A–F · lulus |')
    sep = '|' + '---|' * 19

    def baris(r):
        sp = r['sprt']; pn = r['pintu']
        return (f"| {r['kedudukan'] or '–'} · {r['susunan_pintu'] or '–'} | {r['id']} {r['nama']} | {' '.join(r['bendera']) or '–'} | "
                f"{r['hari'] if r['hari'] is not None else '–'} | "
                f"{p(r['bt_cagr'])} · {sg(r['bt_purata'])} · {sg(r['bt_lebihan'])} · {sg(r['bt_u3'])} | "
                f"{tanda(r['lulus_subset'])} {r['subset'] or ''} · {tanda(r['lulus_wfo'])} {p(r['wfo_cagr'])} · {tanda(r['lulus_at'])} "
                f"{r['at_label'] or '–'} | {int(r['kekal'] * 100)}% · {sg(r['jangkaan'])} | {r['h_posisi']} · {r['h_matang']} · "
                f"{sg(r['h_purata'])} · {sg(r['h_lebihan'])} · {sg(r['h_lebihan_saham'])} | "
                f"{sg(r['h_r5'])} · {sg(r['h_r10'])} · {sg(r['h_r20'])} ({r['h_n_r5']}) | {r['h_n_berkesan']} · {r['h_hari_beli']} · "
                f"{r['h_g_saham']} | {r['h_z'] if r['h_z'] is not None else '–'} · {r['h_p_holm'] if r['h_p_holm'] is not None else '–'} · "
                f"{r['h_z_terlaras'] if r['h_z_terlaras'] is not None else '–'} | "
                f"{sg(r['skor'])} [{sg(r['skor_bawah'])}, {sg(r['skor_atas'])}] · {sg(r['skor_bawah3'])} | "
                + (f"{sg(r['skor_bulan'])} [{sg(r['lb_bulan'])}]" if r['skor_bulan'] is not None else '–') + ' | '
                + (f"{p(r['p_top1'])} · {p(r['p_top5'])} · #{r['pangkat_p5']}–#{r['pangkat_p95']}" if r['p_top1'] is not None else '–')
                + f" | {r['g_matang']}/{r['g_perlu']} · {r['nb']} / {r['nb_perlu'] if r['nb_perlu'] is not None else '–'} · "
                f"{tarikh_ms(r['tarikh_sebenar'])}{' (B)' if r['tarikh_asas'] == 'backtest' else ''} | {r['status']} | "
                f"{sp['status']}{' ' + str(sp['llr']) if sp['llr'] is not None else ''} | "
                f"{r['pantau']}{' (' + r['p_sebab'] + ')' if r['p_sebab'] else ''} | "
                + ''.join(k if pn[k] else ('–' if pn[k] is None else '·') for k in 'ABCDEF') + f" · {r['pintu_lulus']} |")
    sw = [r for r in rows if r['swing']]
    lain = [r for r in rows if not r['swing']]
    L += ['', f'## Kaedah swing ({SWING[0]}–{SWING[1]} hari), susun ikut skor sebulan lebihan tanpa bundar ({len(sw)} kaedah)', '',
          'Pintu: huruf = lulus, · = gagal, – = tiada portfolio. # = kedudukan skor · susunan pintu.', '', hd, sep] + [baris(r) for r in sw]
    L += ['', f'## Bukan swing (pegang < {SWING[0]} atau > {SWING[1]} hari; {len(lain)} kaedah; tiada skor sebulan)', '', hd, sep] + \
         [baris(r) for r in lain]
    L += ['', '## Batasan', '',
          '- Set 431 ialah senarai Shariah hari ini (bias kemandirian); kaedah dibina dan ditapis atas data 2019–2026. Sebab itu prior '
          'lebihan dipotong 75% dan hanya ujian bebas AUTOTUNE menambah kredit.',
          '- Belian rawak backtest = purata sama berat 431 saham (bukan alam Shariah semasa); EW hadapan = alam univ.txt harga ≥ USD10 '
          '(penanda_ew.py). Keluar dalam hari (henti/sasaran) dinilai lawan EW hingga tutup hari keluar (anggaran).',
          '- SD backtest dianggar daripada dagangan (lebihan_sd); SPRT mengandaikan purata kohort normal dan bebas antara hari.',
          '- Peluang pangkat menganggap skor kaedah bebas; HAMPIR_PENDUA dikira atas beberapa malam isyarat sahaja; CIRI ialah '
          'klasifikasi regex kasar.',
          '- Moomoo lama (1–8 Okt 2026, varian v1) dan kohort C isi semula 8–13 Okt tidak dikira dalam bukti hadapan.']
    return '\n'.join(L) + '\n'


def cap_formula(param, kalibrasi=KALIBRASI):
    """Cap jari 10 aksara: parameter papan + kalibrasi_skor.json + kod fungsi teras (skor, status, kedudukan, pantau, MC, nb_perlu,
    semakan). Berubah = kedudukan/status mungkin berubah kerana formula, bukan kerana prestasi."""
    h = hashlib.sha256(json.dumps(param, sort_keys=True, default=str).encode())
    try:
        h.update(open(kalibrasi, 'rb').read())
    except OSError:
        pass
    for f in (skor, status_kaedah, susun_kedudukan, peluang_pangkat, nb_perlu, pantau_kaedah, sasaran_cusum, berat_backtest, semakan,
              kekal, kredit_at, se_dua_hala, ew_tempoh, tambah_lebihan, tambah_umur_tetap, holm, sprt, pintu_kaedah, corong, susun_pintu,
              pisah_backfill, pendua_isyarat, kelas_ciri, ramalan):
        h.update(inspect.getsource(f).encode())
    return h.hexdigest()[:10]


def log_formula(path=LOG_FORMULA):
    """Baris terakhir log formula ('- vX (tarikh): perubahan'), '' jika tiada."""
    try:
        L = [x.strip() for x in open(path, encoding='utf-8') if x.startswith('- v')]
        return L[-1][2:] if L else ''
    except OSError:
        return ''


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
    ap.add_argument('--sejarah', help='sejarah_skor.csv (lalai: sebelah --json)')
    ap.add_argument('--bendera', help='bendera_kaedah.csv (lalai: sebelah --json)')
    a = ap.parse_args(argv)
    d_json = os.path.dirname(os.path.abspath(a.json))
    f_sej = a.sejarah or os.path.join(d_json, os.path.basename(SEJARAH))
    f_ben = a.bendera or os.path.join(d_json, os.path.basename(BENDERA))
    rows, meta = analisis(a.kini)
    BEN, H = meta.pop('_bendera'), meta.pop('_H')
    tulis_bendera(BEN, meta.get('kini'), f_ben)
    sej = tulis_sejarah(rows, meta.get('kini'), f_sej)
    meta['ramalan'] = ramalan(sej, H, [r['id'] for r in rows if r['swing']])
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
                                                    kredit='asas 25% + 25% jika lulus AUTOTUNE (SEDERHANA/TINGGI); S1–S4 dan WFO 0',
                                                    prior='lebihan atas belian rawak tempoh sama (kalibrasi_skor.py lebihan_rawak)',
                                                    hadapan='lebihan EW alam tempoh sama (data/analisis/ew_harian.csv)',
                                                    bukti_mula_c=BUKTI_MULA_C, z_kuat=Z_KUAT, umur_tetap=list(UMUR_TETAP),
                                                    nb='dua hala: kelompok hari beli + saham (Cameron–Gelbach–Miller)',
                                                    sprt=dict(alfa=SPRT_ALFA, beta=SPRT_BETA, sd_min=SD_KOHORT_MIN, kohort_min=PANTAU_KOHORT),
                                                    pintu=dict(c_hari=PINTU_C_HARI, c_z=Z_KUAT, d_sesi=PINTU_D_SESI, d_ew=PINTU_D_EW,
                                                               e_sesi=PINTU_E_SESI, at_lulus=list(AT_LULUS)),
                                                    bendera=dict(pendua_ambang=PENDUA_AMBANG, pendua_min=PENDUA_MIN, artifak=sorted(ARTIFAK)),
                                                    pantau=dict(dd=PANTAU_DD, p=PANTAU_P, g=PANTAU_G, kohort=PANTAU_KOHORT,
                                                                bergulir=PANTAU_BERGULIR, nb_min=NB_MIN, k=muat_kalibrasi()[1], ok=PANTAU_OK),
                                                    mc=dict(cabutan=MC_CABUTAN, biji=MC_BIJI, top=TOP_N)),
               penemuan=pen, rujukan=ruj, rows=rows,
               nota='Papan Penganalisis v4 (standard/penganalisis.py). Skor = LEBIHAN purata setiap dagangan (%) atas belian rawak / EW alam '
                    'tempoh sama: prior backtest dipotong (kredit hanya AUTOTUNE) digabung dengan posisi hadapan matang (C >= 14 Okt, Lejar). '
                    'Pintu A–F dan corong menentukan calon wang sebenar. Rekod analisis sahaja.')
    cap = cap_formula(doc['parameter']); lf = (lama or {}).get('formula') or {}
    doc['formula'] = dict(versi=VERSI_FORMULA, cap=cap, log=log_formula(), sebelum=lf.get('cap'), versi_sebelum=lf.get('versi'),
                          berubah=bool(lama) and lf.get('cap') != cap)   # papan lama tanpa cap formula = formula berubah
    doc['formula']['tanpa_log'] = doc['formula']['berubah'] and lf.get('versi') == VERSI_FORMULA   # berubah tanpa versi baharu
    if doc['formula']['berubah']:   # anak panah kedudukan tidak bermakna apabila formula berubah
        for r in rows:
            r['kedudukan_sebelum'] = None
    try:   # kandungan sama (hanya masa dibina berbeza) -> fail tidak ditulis semula, jadi tiada commit
        if not a.lama and {k: v for k, v in lama.items() if k != 'dibina'} == \
                json.loads(json.dumps({k: v for k, v in doc.items() if k != 'dibina'})) and os.path.exists(a.md):
            print(f"penganalisis: tiada perubahan sejak {lama.get('dibina')}"); return
    except (OSError, ValueError, AttributeError):
        pass
    open(a.json, 'w', encoding='utf-8').write(json.dumps(doc, ensure_ascii=False, separators=(',', ':')))
    open(a.md, 'w', encoding='utf-8').write(jana_md(rows, meta, ruj, pen, dibina))
    print(f"penganalisis: {len(rows)} kaedah ({sum(r['swing'] for r in rows)} swing), "
          f"{sum(r['h_matang'] for r in rows)} posisi matang; corong {[x['n'] for x in meta['corong']]}; {a.md}, {a.json} "
          f"({os.path.getsize(a.json)} bait)")


if __name__ == '__main__':
    main()
