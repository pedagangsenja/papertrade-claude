#!/usr/bin/env python3
"""Analisa BERSTRUKTUR kaedah M dan N, langkah demi langkah (12 Nov 2026; maklumat, BUKAN keputusan).

Permintaan pengguna 12 Nov 2026: nilai SEMUA kaedah M dan N dalam papertrade satu per satu (masuk, pegang,
keluar), susun datanya, dan cari yang terbaik — secara berstruktur, langkah demi langkah. Keputusan pengguna
pada hari sama: (1) analisa dulu, TIADA Nxx baharu didaftar; (2) data langsung + backtest sedia ada, tiada
backtest baharu; (3) biar data tentukan tempoh pegang; (4) simpan dalam repo; (5) kaedah M dan N sahaja (tanpa
rejim/industri); (6) semua langkah dijalankan terus; (7) tiada skill baharu — guna skill yang sudah dipasang.

Satu-satunya keputusan wang sebenar ialah `laporan/KAD_SKOR.md`. Skrip ini hanya MEMBACA Lejar, stor harga, kad
skor, registry dan `REVERSE/jejak_semua.csv`; ia tidak mengubah mana-mana daripadanya.

Langkah (setiap satu menulis fail berawalan L<nn> dalam hasil/):
  L01 Data dan semakan kualiti      - penyebut, pendua, harga, padanan dengan kad skor (senarai semak validate-data)
  L02 Kad setiap kaedah             - satu baris setiap kaedah: teks masuk/pegang/keluar/henti + semua angka
  L03 MASUK                         - lift ufuk tetap lawan saham lain pada hari dan tercile ATR sama
  L04 PEGANG                        - pulangan selepas 1/3/5/10/15 sesi (langsung) dan 5/10/20/60 (backtest Mxx)
  L05 KELUAR                        - sebab keluar; Nxx 6 cara keluar atas masuk sama; Mxx kaedah lawan Chandelier
  L06 RISIKO                        - rugi terburuk, CVaR, rugi > 15 %, henti hari beli, MDD lorong T4
  L07 Pasaran lawan kaedah          - skill residual-edge-analyzer: buku harian kaedah lawan kolam Lejar dan SPUS
  L08 Kualiti backtest              - skill backtest-expert (evaluate_backtest.py) atas registry set 431 (Mxx)
  L09 KOMBINASI                     - Nxx masuk x keluar; bilangan kaedah sepakat; semua pasangan Mxx
  L10 Kebolehpercayaan              - kestabilan dua separuh hari beli, plasebo, backtest lawan langsung
  L11 Corong dan senarai akhir      - tapis dipakai satu demi satu; senarai pantau

Tapis senarai pantau (L11) ditulis sebelum lift 5/10 sesi dan separuh hari beli dilihat (angka kad skor sudah
dilihat). L07 dan L08 ialah maklumat tambahan; ia TIDAK dijadikan tapis baharu selepas data dilihat.

Guna: python3 BacktestShariah2/kajian/analisa_mn/analisa.py        (~1.5 minit)
"""
import importlib.util
import json
import os
import re
import sys
import tempfile
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

HERE = os.path.dirname(os.path.abspath(__file__))
BS2 = os.path.dirname(os.path.dirname(HERE))
AKAR = os.path.dirname(BS2)
sys.path.insert(0, os.path.join(BS2, 'standard'))
import kad_skor as ks  # noqa: E402
import lift_kaedah as lk  # noqa: E402
import status_kad  # noqa: E402

HASIL = os.path.join(HERE, 'hasil')
SKILL = os.path.join(AKAR, '.claude', 'skills')
UFUK = (1, 3, 5, 10, 15)
BENIH = 20261112
N_PECAH = 500          # pecahan rawak hari beli (kestabilan)
N_PLASEBO = 300        # cabutan plasebo
MIN_N, MIN_HARI = 30, 10
HARI0_MAKS = 20.0      # sama dengan label cantas C1
MIN_SESI_BUKU = 15     # L07: sesi buku harian minimum untuk dijalankan (penganalisis sendiri mahu >= 60)
MDD_PENGGUNA = 10.0    # toleransi MDD akaun pengguna (%), L08
CAIR_MIN = 10e6        # nilai dagangan median 20 hari minimum (USD) untuk wang sebenar: kajian/FABLE_CADANGAN.md §2 butir 5
LUAR_BIASA = 60.0      # L01: posisi dengan pulangan melebihi ini (%) disenaraikan untuk semakan munasabah
LOG = []
RINGKAS = {}
PERATURAN = {}


def cetak(*a):
    s = ' '.join(str(x) for x in a)
    LOG.append(s)
    print(s)


def tajuk(n, nama):
    cetak(f'\n{"=" * 100}\nLANGKAH {n}: {nama}\n{"=" * 100}')


def simpan(nama, df, **kw):
    kw.setdefault('float_format', '%.3f')
    df.to_csv(os.path.join(HASIL, nama), **kw)


def simpan_json(nama, d):
    json.dump(d, open(os.path.join(HASIL, nama), 'w', encoding='utf-8'), indent=1, ensure_ascii=False, default=float)


def keluarga(mid):
    return 'GB' if str(mid).startswith('GB') else str(mid)[:1]


def pecah_n(mid):
    """'N19X13' -> ('N19', 'X13'); selain itu (None, None)."""
    m = re.fullmatch(r'(N\d+)(X\d+)', str(mid))
    return (m.group(1), m.group(2)) if m else (None, None)


def muat_modul(nama, laluan):
    spec = importlib.util.spec_from_file_location(nama, laluan)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[nama] = mod
    spec.loader.exec_module(mod)
    return mod


def f(v, k=2, tanda=True):
    if v is None or (isinstance(v, float) and not np.isfinite(v)) or pd.isna(v):
        return '–'
    return f'{v:+.{k}f}' if tanda else f'{v:.{k}f}'


# ---------------------------------------------------------------- data

def muat_posisi():
    """Posisi LANGSUNG tanpa data dikuarantin: pul (lorong 1, seperti kad skor) dan pul2 (lorong 2)."""
    akhir, idx, _ = lk.harga_akhir()
    P = lk.nilai(lk.posisi(), akhir, idx)
    P = P[lk.langsung(P)].copy()
    try:
        import kuarantin as KR
        P = P[~KR.topeng_posisi(P).to_numpy()].copy()
    except Exception as e:  # pragma: no cover
        cetak('amaran: kuarantin tidak dimuat:', e)
    beli = pd.to_numeric(P.harga_beli, errors='coerce')
    kini = (P.saham.map(akhir) / beli - 1) * 100
    kh = P.keluar_henti.astype(str) == 'True'
    P['pul2'] = np.where(kh, pd.to_numeric(P.untung_henti_pct, errors='coerce'), kini) - lk.KOS
    P['terbuka2'] = ~kh
    P['sebab_keluar'] = P.sebab_keluar.fillna('').astype(str)
    P['kel'] = P.id_kaedah.map(keluarga)
    P['dv20'] = nilai_dagangan(P)
    P['cair'] = P.dv20 >= CAIR_MIN
    return P


def nilai_dagangan(P):
    """Nilai dagangan (tutup x volum) median 20 sesi hingga hari ISYARAT setiap posisi, USD (stor harga)."""
    fl = [os.path.join(lk.STOR, x) for x in ('harga_A.csv', 'harga_B.csv')]
    H = pd.concat([pd.read_csv(x, usecols=['ticker', 'date', 'close', 'volume']) for x in fl if os.path.exists(x)],
                  ignore_index=True)
    H['date'] = H.date.astype(str)
    H = lk.potong_sesi(H).drop_duplicates(['ticker', 'date']).sort_values(['ticker', 'date'])
    H['dv20'] = (H.close * H.volume).groupby(H.ticker).transform(lambda x: x.rolling(20, min_periods=10).median())
    peta = dict(zip(zip(H.ticker, H.date), H.dv20))
    isy = P.tarikh_isyarat.astype(str).str.replace('-', '', regex=False)
    return np.array([peta.get(k, np.nan) for k in zip(P.saham, isy)], dtype=float)


def ufuk_tetap(P_semua, sesi, C, A, h):
    """Saham-hari unik setiap kaedah dengan ufuk h lengkap: r, q, lift (tinggal-satu-keluar), liftp (lawan sel)."""
    lk.UFUK = h
    Q = lk.saham_hari(P_semua, sesi, C, A, lk._kuarantin())
    lk.UFUK = 10
    if Q.empty:
        return Q
    X = lk.lift_masuk(Q)
    kol = Q.drop_duplicates(['saham', 'tarikh_beli'])
    sel = kol.groupby(['tarikh_beli', 'q']).r.mean().rename('asasp')
    X = X.join(sel, on=['tarikh_beli', 'q'])
    X['liftp'] = X.r - X.asasp
    X['kel'] = X.id_kaedah.map(keluarga)
    return X


def spus():
    fl = os.path.join(BS2, 'data', 'penanda_aras', 'spus_harian.csv')
    d = pd.read_csv(fl, comment='#', header=None, names=['tarikh', 'buka', 'tutup'])
    d = d[pd.to_numeric(d.buka, errors='coerce').notna()].copy()
    d['buka'], d['tutup'] = d.buka.astype(float), d.tutup.astype(float)
    return d.sort_values('tarikh').reset_index(drop=True)


def backtest_m():
    """Backtest set 431 bagi varian produksi setiap Mxx + lengkung pegang + bilangan set S1-S4 positif."""
    kat = {r['id']: r for r in json.load(open(os.path.join(BS2, 'standard', 'katalog_kaedah.json'),
                                               encoding='utf-8'))['rows']}
    R = pd.read_csv(os.path.join(BS2, 'data', 'registry_M_gabung.csv'), dtype={'set': str})
    baris = {}
    for mid, k in kat.items():
        if not mid.startswith('M'):
            continue
        g = R[(R.id == mid) & (R.varian == k.get('varian_kod'))]
        a = g[g.set == '431']
        if a.empty:
            continue
        a = a.iloc[0]
        d = dict(bt_keputusan=a.keputusan, bt_n=int(a.n), bt_cagr=a.cagr * 100, bt_mdd=a.mdd * 100,
                 bt_h1=a.h1 * 100, bt_h2=a.h2 * 100, bt_win=a.win * 100, bt_avgwin=a.avgwin * 100,
                 bt_avgloss=a.avgloss * 100, bt_tahun=a.n / a.dagangan_setahun if a.dagangan_setahun else np.nan)
        for bahagian in str(a.pegang).split('|'):
            if ':' in bahagian:
                x, y = bahagian.split(':')
                if x in ('5', '10', '20', '60'):
                    try:
                        d[f'bt_r{x}'] = float(y)
                    except ValueError:
                        pass
        s = g[g.set.isin(['S1', 'S2', 'S3', 'S4'])]
        d['bt_set_positif'] = f'{int((s.avg > 0).sum())}/{len(s)}' if len(s) else ''
        baris[mid] = d
    return kat, pd.DataFrame.from_dict(baris, orient='index')


def backtest_n():
    J = pd.read_csv(os.path.join(AKAR, 'REVERSE', 'jejak_semua.csv'))
    J['id'] = J.masuk + J.keluar
    PERATURAN.update(dict(zip(J.keluar, J.peraturan)))
    return J.set_index('id')[['pangkat', 'jangkaan_latih', 'lift_latih', 'jangkaan_tahan', 'lift_tahan',
                              'tanpa5_tahan', 'menang', 'untung', 'rugi', 'n_tahan']].rename(
        columns={'pangkat': 'btn_pangkat', 'jangkaan_latih': 'btn_latih', 'lift_latih': 'btn_lift_latih',
                 'jangkaan_tahan': 'btn_tahan', 'lift_tahan': 'btn_lift_tahan', 'tanpa5_tahan': 'btn_tanpa5',
                 'menang': 'btn_menang', 'untung': 'btn_untung', 'rugi': 'btn_rugi', 'n_tahan': 'btn_n'})


# ---------------------------------------------------------------- kiraan

def ringkas_ufuk(X, h):
    g = X.groupby('id_kaedah')
    return pd.DataFrame({f'n{h}': g.r.size(), f'hb{h}': g.tarikh_beli.nunique(), f'r{h}': g.r.mean(),
                         f'menang{h}': g.r.apply(lambda s: (s > 0).mean() * 100), f'lift{h}': g.lift.mean()})


def separuh(X, h):
    """Lift purata setiap kaedah pada hari beli berindeks genap (A) dan ganjil (B)."""
    hari = {d: i for i, d in enumerate(sorted(X.tarikh_beli.unique()))}
    X = X.assign(sep=X.tarikh_beli.map(hari) % 2)
    a = X[X.sep == 0].groupby('id_kaedah').lift.agg(['mean', 'size'])
    b = X[X.sep == 1].groupby('id_kaedah').lift.agg(['mean', 'size'])
    return pd.DataFrame({f'lift{h}_A': a['mean'], f'n{h}_A': a['size'], f'lift{h}_B': b['mean'], f'n{h}_B': b['size']})


def kestabilan(X, label, min_sep=10, rng=None):
    """Pecahan rawak hari beli kepada dua separuh: Spearman lift kaedah A lawan B, dan untung memilih 10 teratas."""
    rng = rng or np.random.default_rng(BENIH)
    hari = np.array(sorted(X.tarikh_beli.unique()))
    if len(hari) < 4:
        return dict(label=label, hari=len(hari), kaedah=0)
    kod_k, nama_k = pd.factorize(X.id_kaedah)
    kod_h = pd.Series(X.tarikh_beli).map({d: i for i, d in enumerate(hari)}).to_numpy()
    v = X.liftp.to_numpy()
    K, H = len(nama_k), len(hari)
    S = np.zeros((K, H))
    N = np.zeros((K, H))
    np.add.at(S, (kod_k, kod_h), v)
    np.add.at(N, (kod_k, kod_h), 1)
    rho, pilih, bil = [], [], []
    for _ in range(N_PECAH):
        a = np.zeros(H, bool)
        a[rng.permutation(H)[:H // 2]] = True
        na, nb = N[:, a].sum(1), N[:, ~a].sum(1)
        ok = (na >= min_sep) & (nb >= min_sep)
        if ok.sum() < 20:
            continue
        ma, mb = S[ok][:, a].sum(1) / na[ok], S[ok][:, ~a].sum(1) / nb[ok]
        rho.append(stats.spearmanr(ma, mb).statistic)
        top = np.argsort(-ma)[:10]
        pilih.append(mb[top].mean() - mb.mean())
        bil.append(int(ok.sum()))
    if not rho:
        return dict(label=label, hari=H, kaedah=0)
    q = lambda x, p: float(np.percentile(x, p))  # noqa: E731
    return dict(label=label, hari=H, kaedah=int(np.median(bil)), pecahan=len(rho),
                spearman_median=q(rho, 50), spearman_p5=q(rho, 5), spearman_p95=q(rho, 95),
                top10_lebih_median=q(pilih, 50), top10_lebih_p5=q(pilih, 5), top10_lebih_p95=q(pilih, 95),
                top10_lebih_positif_pct=float((np.array(pilih) > 0).mean() * 100))


def plasebo_tapis(X5, X10, ids, rng=None):
    """Bilangan kaedah lulus tapis ufuk tetap (lift5 > 0, lift5 kedua-dua separuh > 0, lift10 > 0) lawan dua plasebo:
      bebas   = saham setiap kaedah dicabut RAWAK daripada kolam pada (hari beli, tercile ATR) sama, kiraan sama,
                setiap kaedah berasingan (mengabaikan bahawa kaedah berkongsi saham);
      tindih  = keahlian kaedah x saham-hari DIKEKALKAN, pulangan dikocok antara saham-hari dalam sel yang sama
                (kaedah yang berkongsi saham lulus/gagal bersama, seperti data sebenar). Inilah plasebo yang adil."""
    rng = rng or np.random.default_rng(BENIH + 1)
    X5 = X5[X5.id_kaedah.isin(ids)]
    U = X5.drop_duplicates(['saham', 'tarikh_beli'])[['saham', 'tarikh_beli', 'q', 'liftp']].rename(
        columns={'liftp': 'l5'}).reset_index(drop=True)
    u10 = X10.drop_duplicates(['saham', 'tarikh_beli']).set_index(['saham', 'tarikh_beli']).liftp
    U['l10'] = pd.MultiIndex.from_frame(U[['saham', 'tarikh_beli']]).map(u10.to_dict())
    hari = {d: i for i, d in enumerate(sorted(U.tarikh_beli.unique()))}
    sep = (U.tarikh_beli.map(hari) % 2).to_numpy()
    sel = [g.index.to_numpy() for _, g in U.groupby(['tarikh_beli', 'q'])]
    pos = {k: i for i, k in enumerate(zip(U.saham, U.tarikh_beli))}
    km, nama = pd.factorize(X5.id_kaedah)
    B = np.zeros((len(U), len(nama)))
    B[[pos[k] for k in zip(X5.saham, X5.tarikh_beli)], km] = 1
    l5, l10 = U.l5.to_numpy(), U.l10.to_numpy()

    def lulus(Bm, v5, v10):
        ada = np.isfinite(v10)
        with np.errstate(divide='ignore', invalid='ignore'):
            m5 = (Bm.T @ v5) / Bm.sum(0)
            ma = (Bm.T @ (v5 * (sep == 0))) / (Bm.T @ (sep == 0).astype(float))
            mb = (Bm.T @ (v5 * (sep == 1))) / (Bm.T @ (sep == 1).astype(float))
            m10 = (Bm.T @ np.where(ada, v10, 0.0)) / (Bm.T @ ada.astype(float))
        return int(((m5 > 0) & (ma > 0) & (mb > 0) & (m10 > 0)).sum())

    sebenar = lulus(B, l5, l10)
    tindih, bebas = [], []
    for _ in range(N_PLASEBO):
        o = np.arange(len(U))
        for ix in sel:
            o[ix] = rng.permutation(ix)
        tindih.append(lulus(B, l5[o], l10[o]))
        Bp = np.zeros_like(B)
        for ix in sel:                       # setiap kaedah: cabutan sendiri dalam sel, kiraan sama
            n = B[ix].sum(0).astype(int)
            for j in np.nonzero(n)[0]:
                Bp[rng.choice(ix, size=n[j], replace=False), j] = 1
        bebas.append(lulus(Bp, l5, l10))
    tindih, bebas = np.array(tindih), np.array(bebas)
    return dict(kaedah=len(nama), lulus_sebenar=sebenar,
                bebas_purata=float(bebas.mean()), bebas_p5=float(np.percentile(bebas, 5)),
                bebas_p95=float(np.percentile(bebas, 95)), p_bebas=float((bebas >= sebenar).mean()),
                tindih_purata=float(tindih.mean()), tindih_p5=float(np.percentile(tindih, 5)),
                tindih_p95=float(np.percentile(tindih, 95)), p_tindih=float((tindih >= sebenar).mean()))


def konsensus(X, h, label=''):
    """Saham-hari unik: bilangan kaedah Mxx berbeza dan masuk Nxx berbeza yang membelinya; pulangan ikut baldi.
    t = lift / SE dua hala (saham, hari beli); tingkap bertindih antara hari beli menjadikannya optimistik."""
    X = X.assign(masuk=X.id_kaedah.map(lambda m: pecah_n(m)[0] or m))
    k = X.groupby(['saham', 'tarikh_beli']).agg(r=('r', 'first'), liftp=('liftp', 'first'),
                                                 kM=('masuk', lambda s: s[s.str.startswith('M')].nunique()),
                                                 kN=('masuk', lambda s: s[s.str.startswith('N')].nunique())).reset_index()
    baris = []
    for lajur, nama in (('kM', 'kaedah Mxx sepakat'), ('kN', 'masuk Nxx sepakat')):
        b = pd.cut(k[lajur], [-1, 0, 1, 2, 4, 9, 999], labels=['0', '1', '2', '3-4', '5-9', '10+'])
        for baldi, g in k.groupby(b, observed=True):
            t = np.nan
            if len(g) >= 20 and g.tarikh_beli.nunique() >= 3:
                se, _ = lk.se_dua_hala(g.liftp, g.saham, g.tarikh_beli)
                t = g.liftp.mean() / se if se > 0 else np.nan
            baris.append(dict(ufuk=h, set=label or 'semua hari', jenis=nama, baldi=baldi, saham_hari=len(g),
                              saham=g.saham.nunique(), hari_beli=g.tarikh_beli.nunique(), r=g.r.mean(),
                              menang=(g.r > 0).mean() * 100, lift=g.liftp.mean(), t=t))
    return baris


def pasangan(X, min_n=30, min_sep=15):
    """Semua pasangan Mxx yang membeli saham-hari sama: lift purata saham-hari bersama, dan kestabilan separuh."""
    X = X[X.kel == 'M']
    sh, _ = pd.factorize(pd.MultiIndex.from_frame(X[['saham', 'tarikh_beli']]))
    km, nama = pd.factorize(X.id_kaedah)
    B = np.zeros((sh.max() + 1, len(nama)))
    B[sh, km] = 1
    u = X.assign(sh=sh).drop_duplicates('sh').set_index('sh').sort_index()
    v = u.liftp.to_numpy()
    hari = {d: i for i, d in enumerate(sorted(u.tarikh_beli.unique()))}
    sep = u.tarikh_beli.map(hari).to_numpy() % 2
    iu = np.triu_indices(len(nama), 1)

    def kira(topeng):
        Bm = B[topeng]
        return (Bm.T @ Bm)[iu], (Bm.T @ (Bm * v[topeng][:, None]))[iu]

    N, S = kira(np.ones(len(v), bool))
    Na, Sa = kira(sep == 0)
    Nb, Sb = kira(sep == 1)
    cukup = N >= min_n
    m = S[cukup] / N[cukup]
    d = dict(pasangan_mungkin=len(N), pasangan_cukup=int(cukup.sum()), lift_purata=float(m.mean()),
             lift_p5=float(np.percentile(m, 5)), lift_p95=float(np.percentile(m, 95)),
             positif_pct=float((m > 0).mean() * 100))
    ok = (Na >= min_sep) & (Nb >= min_sep)
    ma, mb = Sa[ok] / Na[ok], Sb[ok] / Nb[ok]
    d['pasangan_dua_separuh'] = int(ok.sum())
    d['spearman_A_B'] = float(stats.spearmanr(ma, mb).statistic)
    top = np.argsort(-ma)[:20]
    d['top20_A_pada_A'] = float(ma[top].mean())
    d['top20_A_pada_B'] = float(mb[top].mean())
    d['semua_pada_B'] = float(mb.mean())
    top = np.argsort(-mb)[:20]
    d['top20_B_pada_A'] = float(ma[top].mean())
    d['semua_pada_A'] = float(ma.mean())
    return d


def baki_kelebihan(P, sesi, C):
    """L07 — skill residual-edge-analyzer: buku harian setiap kaedah (kasar) lawan kolam Lejar (utama) dan SPUS
    (kepekaan). Kedua-dua asas dinyatakan SEBELUM hasil dilihat. Dengan <= 19 sesi, status penganalisis ialah
    INSUFFICIENT_EVIDENCE (minimum 60); metrik yang dikeluarkan bersifat penerokaan."""
    mod = muat_modul('analyze_residual_edge',
                     os.path.join(SKILL, 'residual-edge-analyzer', 'scripts', 'analyze_residual_edge.py'))
    B = ks.buku_harian(P, sesi, C, kos=0.0)
    kolam = ks.buku_harian(P.assign(id_kaedah='KOLAM'), sesi, C, kos=0.0)['KOLAM']
    sp = spus()
    sp = (sp.tutup.pct_change() * 100).set_axis(sp.tarikh.str.replace('-', '', regex=False))
    cfg = {"schema_version": "1.0", "date_column": "date", "strategy_column": "strategy_return",
           "return_unit": "decimal", "frequency": "daily",
           "primary_model": {"name": "kolam_lejar", "baseline_columns": ["kolam_return"]},
           "sensitivity_models": [{"name": "spus", "baseline_columns": ["spus_return"]}],
           "hac_lags": "auto", "include_series": False,
           "data_declarations": {"baseline_selection": "predeclared", "strategy_return_basis": "gross",
                                 "baseline_return_basis": "gross", "analysis_scope": "live",
                                 "universe_data": "point_in_time"}}
    baris = []
    with tempfile.TemporaryDirectory() as d:
        fc = Path(d) / 'cfg.json'
        fc.write_text(json.dumps(cfg))
        for mid, s in sorted(B.items()):
            df = pd.DataFrame({'strategy_return': s / 100, 'kolam_return': kolam.reindex(s.index) / 100,
                               'spus_return': sp.reindex(s.index) / 100}).dropna()
            if len(df) < MIN_SESI_BUKU:
                continue
            df.index = pd.to_datetime(df.index).strftime('%Y-%m-%d')
            df.index.name = 'date'
            fi = Path(d) / f'{mid}.csv'
            df.to_csv(fi)
            try:
                rep = mod.analyze(fi, fc)
            except Exception as e:  # pragma: no cover
                baris.append(dict(id=mid, sesi=len(df), status=f'RALAT: {e}'))
                continue
            M = {m['name']: m for m in rep['models']}
            a, b = M['kolam_lejar'], M['spus']
            beta = next(c['estimate'] for c in a['coefficients'] if c['name'] == 'kolam_return')
            baris.append(dict(id=mid, sesi=len(df), status=rep['verdict']['status'],
                              layak_keputusan=rep['verdict']['decision_eligibility'],
                              r2_kolam=a['r_squared'], beta_kolam=beta,
                              alpha_harian_pct=a['alpha']['periodic'] * 100, alpha_t=a['alpha']['t_stat'],
                              r2_spus=b['r_squared'], alpha_t_spus=b['alpha']['t_stat']))
    return pd.DataFrame(baris).set_index('id') if baris else pd.DataFrame()


def kualiti_backtest(T):
    """L08 — skill backtest-expert (evaluate_backtest.py) atas registry set 431 varian produksi (Mxx sahaja; Nxx
    tiada MDD setiap kombinasi dalam jejak_semua). slippage_tested = False: enjin registry memakai kos 0.1 % setiap
    belah tanpa ujian tekanan slippage. Bilangan parameter tidak direkod dalam registry, jadi skor 0-100 TIDAK
    dilaporkan; hanya `decision` dan `blocking_reasons` (yang tidak bergantung pada bilangan parameter)."""
    mod = muat_modul('evaluate_backtest', os.path.join(SKILL, 'backtest-expert', 'scripts', 'evaluate_backtest.py'))
    baris = {}
    for mid, r in T[T.keluarga == 'M'].iterrows():
        if not np.isfinite(r.get('bt_n', np.nan)):
            continue
        hujah = dict(total_trades=int(r.bt_n), win_rate=float(r.bt_win), avg_win_pct=float(r.bt_avgwin),
                     avg_loss_pct=abs(float(r.bt_avgloss)), max_drawdown_pct=abs(float(r.bt_mdd)),
                     years_tested=int(r.bt_tahun), num_parameters=5, slippage_tested=False)
        try:
            a = mod.evaluate(**hujah)
            b = mod.evaluate(**hujah, max_acceptable_drawdown_pct=MDD_PENGGUNA)
            baris[mid] = dict(bte_keputusan=a['decision'], bte_sebab=';'.join(a['blocking_reasons']),
                              bte_keputusan_mdd10=b['decision'])
        except Exception as e:
            baris[mid] = dict(bte_keputusan='TIDAK SAH', bte_sebab=str(e)[:80], bte_keputusan_mdd10='TIDAK SAH')
    return pd.DataFrame.from_dict(baris, orient='index')


def kelas(r):
    """Label mekanikal (maklumat). Tertib penilaian tetap, sama dengan corong L11."""
    def ada(v):
        return v is not None and np.isfinite(v)
    if r.n < MIN_N or r.hari_beli < MIN_HARI:
        return 'TERLALU AWAL', f'{int(r.n)} posisi, {int(r.hari_beli)} hari beli'
    if r.hari0_pct >= HARI0_MAKS:
        return 'STRUKTUR GAGAL', f'henti hari-0 {r.hari0_pct:.0f}% posisi (G4 pasti gagal)'
    gagal = []
    if not (r.jangkaan > 0):
        gagal.append('jangkaan <= 0')
    if not (ada(r.tanpa5) and r.tanpa5 > 0):
        gagal.append('tanpa5 <= 0')
    if not (ada(r.lift5) and r.lift5 > 0):
        gagal.append('lift 5 sesi <= 0')
    if not (ada(r.lift10) and r.lift10 > 0):
        gagal.append('lift 10 sesi <= 0')
    if not (ada(r.lift5_A) and ada(r.lift5_B) and r.lift5_A > 0 and r.lift5_B > 0):
        gagal.append('lift tidak positif pada kedua-dua separuh hari beli')
    bt = r.bt_purata if r.keluarga == 'M' else r.btn_tahan
    if not (ada(bt) and bt > 0):
        gagal.append('backtest <= 0 atau tiada')
    if not gagal:
        return 'PANTAU', 'lulus semua tapis (BUKAN terbukti)'
    if not (r.jangkaan > 0) and not (ada(r.lift5) and r.lift5 > 0):
        return 'LEMAH', '; '.join(gagal)
    return 'CAMPUR', '; '.join(gagal)


def corong(T):
    """Tapis dipakai SATU DEMI SATU (kumulatif), berasingan bagi Mxx dan Nxx."""
    def pos(s):
        return s.fillna(-1) > 0
    langkah = [
        ('Semua kaedah dalam kad skor', lambda t: pd.Series(True, index=t.index)),
        (f'Cukup data: >= {MIN_N} posisi dan >= {MIN_HARI} hari beli', lambda t: (t.n >= MIN_N) & (t.hari_beli >= MIN_HARI)),
        (f'Bukan struktur gagal: henti hari beli < {HARI0_MAKS:.0f}% posisi', lambda t: t.hari0_pct < HARI0_MAKS),
        ('Jangkaan > 0 (semua posisi, termasuk terbuka)', lambda t: t.jangkaan > 0),
        ('tanpa5 > 0 (untung selepas buang 5% posisi terbaik)', lambda t: pos(t.tanpa5)),
        ('Lift 5 dan 10 sesi > 0 (pilih saham lebih baik daripada kolam)', lambda t: pos(t.lift5) & pos(t.lift10)),
        ('Lift 5 sesi > 0 pada kedua-dua separuh hari beli', lambda t: pos(t.lift5_A) & pos(t.lift5_B)),
        ('Backtest sedia ada > 0', lambda t: pos(t.bt_purata.where(t.keluarga == 'M', t.btn_tahan))),
        ('Maklumat: sifar henti pada hari beli (gate G4 kad skor)', lambda t: t.hari0 == 0),
    ]
    baris, hidup = [], pd.Series(True, index=T.index)
    for i, (nama, fn) in enumerate(langkah):
        hidup = hidup & fn(T)
        baris.append(dict(tahap=i, tapis=nama, Mxx=int((hidup & (T.keluarga == 'M')).sum()),
                          Nxx=int((hidup & (T.keluarga == 'N')).sum()),
                          baki=', '.join(sorted(T.index[hidup])) if hidup.sum() <= 12 else ''))
    return pd.DataFrame(baris)


# ---------------------------------------------------------------- utama

def main():
    os.makedirs(HASIL, exist_ok=True)
    KS = json.load(open(os.path.join(BS2, 'data', 'analisis', 'kad_skor.json'), encoding='utf-8'))
    K = pd.DataFrame(KS['rows'], columns=KS['kol']).set_index('id')
    num = ['n', 'tutup', 'buka_pct', 'hari_beli', 'jangkaan', 'pul_tutup', 'pul_buka', 'menang', 'untung_purata',
           'rugi_purata', 'payoff', 'cvar10', 'terburuk', 'tanpa5', 'mae', 'mfe', 'jangkaan_slip', 'hari0', 'hari0_pct',
           'hari_on', 'hari_off', 'buku_harian', 'buku_ci_bawah', 'buku_ci_atas', 'bt_hari', 'bt_purata',
           'bt_menang', 't4_sesi', 't4_pul', 't4_mdd', 't4_spus', 't4_persentil']
    K[num] = K[num].apply(pd.to_numeric, errors='coerce')
    mentah = lk.posisi()
    P = muat_posisi()
    sesi, C, A = lk.panel_harga()
    RINGKAS['harga_pada'] = KS['harga_pada']

    # ================================================================ L01
    tajuk(1, 'DATA DAN SEMAKAN KUALITI')
    j = P.groupby('id_kaedah').pul.mean()
    hb = pd.to_numeric(P.harga_beli, errors='coerce')
    d1 = dict(
        harga_pada=KS['harga_pada'], sesi_lejar=lk.sesi_lejar(), bar_stor_terakhir=sesi[-1],
        posisi_lejar_semua=len(mentah), posisi_langsung=len(P), posisi_kad_skor=int(KS['posisi']),
        sepadan_kad_skor=bool(len(P) == KS['posisi']), posisi_isian_tidak_dikira=int(KS['posisi_isian']),
        posisi_kuarantin_tidak_dikira=int(KS['posisi_tercemar']),
        kaedah=int(P.id_kaedah.nunique()), kaedah_M=int((K.keluarga == 'M').sum()), kaedah_N=int((K.keluarga == 'N').sum()),
        saham_unik=int(P.saham.nunique()),
        pendua_kaedah_saham_hari_beli=int(P.duplicated(['id_kaedah', 'saham', 'tarikh_beli']).sum()),
        harga_beli_tidak_sah=int((~(hb > 0)).sum()), pulangan_kosong=int(P.pul.isna().sum()),
        posisi_M=int((P.kel == 'M').sum()), posisi_N=int((P.kel == 'N').sum()),
        hari_beli_M=int(P[P.kel == 'M'].tarikh_beli.nunique()), hari_beli_N=int(P[P.kel == 'N'].tarikh_beli.nunique()),
        hari_beli_pertama_M=str(P[P.kel == 'M'].tarikh_beli.min()), hari_beli_pertama_N=str(P[P.kel == 'N'].tarikh_beli.min()),
        hari_beli_terakhir=str(P.tarikh_beli.max()), hari_on=int(KS['hari_on']), hari_off=int(KS['hari_off']),
        masih_terbuka_pct=float(P.terbuka.mean() * 100),
        beza_maks_jangkaan_lawan_kad_skor=float((j - K.jangkaan.reindex(j.index)).abs().max()),
        pulangan_min=float(P.pul.min()), pulangan_maks=float(P.pul.max()),
    )
    d1['lulus'] = bool(d1['sepadan_kad_skor'] and d1['pendua_kaedah_saham_hari_beli'] == 0 and d1['harga_beli_tidak_sah'] == 0
                       and d1['pulangan_kosong'] == 0 and d1['beza_maks_jangkaan_lawan_kad_skor'] < 0.011
                       and d1['sesi_lejar'] == d1['bar_stor_terakhir'])
    lb = P[P.pul > LUAR_BIASA]
    d1['posisi_pulangan_luar_biasa'] = int(len(lb))
    d1['saham_luar_biasa'] = {t: dict(posisi=int(len(g_)), posisi_N=int((g_.kel == 'N').sum()), purata=float(g_.pul.mean()),
                                      nilai_dagangan_median_usd=float(g_.dv20.median()), cair=bool(g_.cair.all()))
                              for t, g_ in lb.groupby('saham')}
    d1['posisi_tidak_cair_pct'] = float((~P.cair).mean() * 100)
    simpan_json('L01_data.json', d1)
    RINGKAS['L01'] = d1
    for k_, v_ in d1.items():
        cetak(f'  {k_}: {v_}')

    # ================================================================ kiraan bersama (dipakai L02-L11)
    XU = {h: ufuk_tetap(mentah, sesi, C, A, h) for h in UFUK}
    T = K.copy()
    for h, X in XU.items():
        if not X.empty:
            T = T.join(ringkas_ufuk(X, h))
    for h in (5, 10):
        T = T.join(separuh(XU[h], h))
    g = P.groupby('id_kaedah')
    T = T.join(pd.DataFrame({'l2_jangkaan': g.pul2.mean(), 'l2_tutup': g.terbuka2.apply(lambda s: int((~s).sum())),
                             'l2_lebih_l1': g.apply(lambda x: (x.pul2 - x.pul).mean(), include_groups=False),
                             'hari_pegang_median': g.hari_pegang.median(),
                             'rugi15_pct': g.pul.apply(lambda s: (s < -15).mean() * 100),
                             'rugi8_pct': g.pul.apply(lambda s: (s < -8).mean() * 100)}))
    gc = P[P.cair].groupby('id_kaedah')

    def tanpa5(s_):
        v_ = np.sort(s_.to_numpy())
        k_ = int(np.ceil(0.05 * len(v_)))
        return float(v_[:len(v_) - k_].mean()) if len(v_) - k_ > 0 else np.nan
    T = T.join(pd.DataFrame({'n_cair': gc.pul.size(), 'jangkaan_cair': gc.pul.mean(), 'tanpa5_cair': gc.pul.apply(tanpa5)}))
    T['n_cair'] = T.n_cair.fillna(0)
    kat, BM = backtest_m()
    T = T.join(BM).join(backtest_n())
    for c in ('masuk', 'keluar', 'pegang', 'henti'):
        T[f'teks_{c}'] = [(kat.get(i) or {}).get(c, '') for i in T.index]
    try:
        SK = json.load(open(os.path.join(BS2, 'data', 'analisis', 'skor_kaedah.json'), encoding='utf-8'))
        sk = pd.DataFrame(SK['rows'], columns=SK['kol']).set_index('id')
        T['skor_kaedah'] = pd.to_numeric(sk.get('skor'), errors='coerce')
    except Exception as e:
        cetak('amaran: skor_kaedah.json tidak dibaca:', e)
    T['masuk_n'], T['keluar_n'] = zip(*[pecah_n(i) for i in T.index])
    RE = baki_kelebihan(P, sesi, C)
    if not RE.empty:
        T = T.join(RE.add_prefix('re_'))
    T = T.join(kualiti_backtest(T))
    ke = [kelas(r) for r in T.itertuples()]
    T['kelas'], T['sebab_kelas'] = [x[0] for x in ke], [x[1] for x in ke]

    # ================================================================ L02
    tajuk(2, 'KAD SETIAP KAEDAH (satu per satu)')
    depan = ['nama', 'keluarga', 'kelas', 'sebab_kelas', 'status', 'teks_masuk', 'teks_pegang', 'teks_keluar', 'teks_henti',
             'n', 'tutup', 'hari_beli', 'jangkaan', 'tanpa5', 'menang', 'payoff', 'pul_tutup', 'pul_buka', 'hari0', 'hari0_pct',
             'mfe', 'mae', 'hari_pegang_median', 'buku_harian', 'buku_ci_bawah', 'buku_ci_atas']
    T = T[depan + [c for c in T.columns if c not in depan]]
    simpan('L02_kaedah.csv', T.sort_values(['keluarga', 'jangkaan'], ascending=[True, False]), float_format='%.4f')
    kl = pd.crosstab(T.kelas, T.keluarga)
    cetak(kl.to_string())
    cukup = T[(T.n >= MIN_N) & (T.hari_beli >= 5)]
    RINGKAS['L02'] = dict(kelas={k_: {c_: int(kl.loc[k_, c_]) for c_ in kl.columns} for k_ in kl.index},
                          cukup_posisi=len(cukup), jangkaan_positif=int((cukup.jangkaan > 0).sum()),
                          had_bawah_positif=int((cukup.buku_ci_bawah > 0).sum()), tanpa5_positif=int((cukup.tanpa5 > 0).sum()),
                          median_jangkaan_M=float(T[T.keluarga == 'M'].jangkaan.median()),
                          median_jangkaan_N=float(T[T.keluarga == 'N'].jangkaan.median()))
    cetak(f"Kaedah >= {MIN_N} posisi dan >= 5 hari beli: {len(cukup)}; jangkaan > 0: {RINGKAS['L02']['jangkaan_positif']}; "
          f"had bawah 95% buku harian > 0: {RINGKAS['L02']['had_bawah_positif']}; tanpa5 > 0: {RINGKAS['L02']['tanpa5_positif']}")
    cetak(f"Median jangkaan: Mxx {RINGKAS['L02']['median_jangkaan_M']:+.2f}%, Nxx {RINGKAS['L02']['median_jangkaan_N']:+.2f}%")

    # ================================================================ L03
    tajuk(3, 'MASUK — adakah kaedah memilih saham lebih baik daripada saham lain pada hari sama?')
    km = ['nama', 'keluarga', 'kelas', 'n3', 'hb3', 'lift1', 'lift3', 'lift5', 'lift10', 'lift15', 'lift5_A', 'lift5_B', 'n5', 'hb5', 'n10', 'hb10']
    Mk = T[km].sort_values('lift5', ascending=False)
    simpan('L03_masuk.csv', Mk)
    m5 = T[(T.keluarga == 'M') & (T.n5 >= MIN_N)]
    RINGKAS['L03'] = dict(mxx_diuji=len(m5), lift5_positif=int((m5.lift5 > 0).sum()), lift5_median=float(m5.lift5.median()),
                          lift5_lebih_2=int((m5.lift5 > 2).sum()), lift5_kurang_neg2=int((m5.lift5 < -2).sum()),
                          dua_separuh_positif=int(((m5.lift5_A > 0) & (m5.lift5_B > 0)).sum()),
                          nxx_hari_beli_5sesi=int(XU[5][XU[5].kel == 'N'].tarikh_beli.nunique()))
    cetak(f"Mxx dengan >= {MIN_N} saham-hari (5 sesi): {len(m5)}; lift 5 sesi > 0: {RINGKAS['L03']['lift5_positif']}; "
          f"median {RINGKAS['L03']['lift5_median']:+.2f} mata; positif pada kedua-dua separuh: {RINGKAS['L03']['dua_separuh_positif']}")
    cetak('10 teratas ikut lift 5 sesi (Mxx, >= 30 saham-hari):')
    cetak(m5.sort_values('lift5', ascending=False)[['nama', 'n5', 'hb5', 'lift3', 'lift5', 'lift10', 'lift5_A', 'lift5_B']].head(10)
          .to_string(float_format=lambda v: f'{v:.2f}'))
    N = T[T.masuk_n.notna()].copy()
    ms = N.groupby('masuk_n').agg(nama=('nama', lambda s: s.iloc[0].split(' → ')[0].split(' x X')[0][:44]),
                                  kombinasi=('n', 'size'), posisi=('n', 'sum'),
                                  langsung_jangkaan=('jangkaan', 'mean'), langsung_lift3=('lift3', 'mean'),
                                  langsung_r3=('r3', 'mean'), backtest_tahan=('btn_tahan', 'mean'),
                                  backtest_lift=('btn_lift_tahan', 'mean')).sort_values('langsung_jangkaan', ascending=False)
    simpan('L03_masuk_nxx.csv', ms)
    e1 = stats.spearmanr(ms.backtest_tahan, ms.langsung_jangkaan)
    e2 = stats.spearmanr(ms.backtest_lift, ms.langsung_lift3, nan_policy='omit')
    RINGKAS['L03'].update(nxx_masuk=len(ms), nxx_spearman_bt_langsung=float(e1.statistic), nxx_spearman_p=float(e1.pvalue),
                          nxx_spearman_lift=float(e2.statistic), nxx_spearman_lift_p=float(e2.pvalue))
    cetak('\nNxx ikut isyarat MASUK (10 teratas ikut jangkaan langsung; 6 hari beli):')
    cetak(ms.head(10).to_string(float_format=lambda v: f'{v:.2f}'))
    cetak(f'Spearman peringkat MASUK Nxx ({len(ms)} isyarat): backtest tahan lawan jangkaan langsung {e1.statistic:+.2f} '
          f'(p {e1.pvalue:.4f}); lift backtest lawan lift langsung 3 sesi {e2.statistic:+.2f} (p {e2.pvalue:.2f})')

    # ================================================================ L04
    tajuk(4, 'PEGANG — pulangan selepas beberapa hari, tanpa mengira peraturan keluar')
    SP = spus()
    ibuka = dict(zip(SP.tarikh, SP.index))
    asas = []
    for h, X in XU.items():
        if X.empty:
            continue
        for kel, U in (('semua', X), ('M', X[X.kel == 'M']), ('N', X[X.kel == 'N'])):
            U = U.drop_duplicates(['saham', 'tarikh_beli'])
            if U.empty:
                continue
            sp = [(SP.tutup[ibuka[d] + h - 1] / SP.buka[ibuka[d]] - 1) * 100
                  if d in ibuka and ibuka[d] + h - 1 < len(SP) else np.nan for d in U.tarikh_beli]
            asas.append(dict(ufuk=h, kolam=kel, hari_beli=U.tarikh_beli.nunique(), saham_hari=len(U),
                             r_purata=U.r.mean(), r_median=U.r.median(), menang=(U.r > 0).mean() * 100,
                             spus_tingkap_sama=float(np.nanmean(sp))))
    asas = pd.DataFrame(asas)
    simpan('L04_kadar_asas.csv', asas, index=False)
    cetak(asas.to_string(index=False, float_format=lambda v: f'{v:.2f}'))
    ikut_hari = XU[5].drop_duplicates(['saham', 'tarikh_beli']).groupby('tarikh_beli').r.mean()
    simpan('L04_kolam_ikut_hari.csv', ikut_hari.rename('r5_kolam').to_frame())
    # Lengkung SEJAJAR: saham-hari yang sama pada setiap ufuk (hari beli dengan 10 sesi lengkap), supaya ufuk boleh dibanding
    kunci = ['id_kaedah', 'saham', 'tarikh_beli']
    SJ = XU[10][kunci + ['r', 'kel']].rename(columns={'r': 'r10'})
    for h in (1, 3, 5):
        SJ = SJ.merge(XU[h][kunci + ['r']].rename(columns={'r': f'r{h}'}), on=kunci, how='inner')
    Us = SJ.drop_duplicates(['saham', 'tarikh_beli'])
    sej = pd.DataFrame([dict(ufuk=h, hari_beli=Us.tarikh_beli.nunique(), saham_hari=len(Us), r_purata=Us[f'r{h}'].mean(),
                             r_median=Us[f'r{h}'].median(), menang=(Us[f'r{h}'] > 0).mean() * 100) for h in (1, 3, 5, 10)])
    simpan('L04_kadar_asas_sejajar.csv', sej, index=False)
    cetak('Kohort SEJAJAR (hari beli yang sama pada setiap ufuk):')
    cetak(sej.to_string(index=False, float_format=lambda v: f'{v:.2f}'))
    gs = SJ[SJ.kel == 'M'].groupby('id_kaedah')
    sjm = gs[['r1', 'r3', 'r5', 'r10']].mean()[gs.size() >= 20]
    terbaik = sjm.idxmax(axis=1).str[1:].value_counts().to_dict()
    kp = ['nama', 'keluarga', 'kelas', 'n5', 'hb5', 'r1', 'r3', 'r5', 'r10', 'r15', 'bt_r5', 'bt_r10', 'bt_r20', 'bt_r60', 'bt_hari',
          'hari_pegang_median', 'mfe', 'mae']
    Pg = T[kp].copy()
    Pg = Pg.join(sjm.add_prefix('sejajar_'))
    simpan('L04_pegang.csv', Pg.sort_values('r5', ascending=False))
    mp = T[(T.keluarga == 'M') & (T.n5 >= MIN_N) & T.r10.notna()]
    semua3 = int(((mp.r3 > 0) & (mp.r5 > 0) & (mp.r10 > 0)).sum())
    btm = T[(T.keluarga == 'M')].dropna(subset=['bt_r5', 'bt_r10', 'bt_r20', 'bt_r60'])
    RINGKAS['L04'] = dict(asas=asas[asas.kolam == 'semua'].set_index('ufuk')[['hari_beli', 'saham_hari', 'r_purata', 'menang', 'spus_tingkap_sama']].to_dict('index'),
                          kolam_hari_min=float(ikut_hari.min()), kolam_hari_maks=float(ikut_hari.max()), kolam_hari_sd=float(ikut_hari.std()),
                          sd_lift_kaedah=float(T[T.n5 >= MIN_N].lift5.std()), mxx_ufuk10=len(mp), mxx_r3_r5_r10_positif=semua3,
                          bt_mxx=len(btm), bt_median_r5=float(btm.bt_r5.median()), bt_median_r10=float(btm.bt_r10.median()),
                          bt_median_r20=float(btm.bt_r20.median()), bt_median_r60=float(btm.bt_r60.median()),
                          bt_naik_dengan_masa=int((btm.bt_r60 > btm.bt_r20).sum()),
                          sejajar=sej.set_index('ufuk').to_dict('index'), mxx_sejajar=len(sjm), ufuk_terbaik_sejajar=terbaik)
    cetak(f"Kolam 5 sesi ikut HARI BELI: min {ikut_hari.min():+.2f}, maks {ikut_hari.max():+.2f}, SD {ikut_hari.std():.2f} mata; "
          f"SD lift 5 sesi merentas KAEDAH: {RINGKAS['L04']['sd_lift_kaedah']:.2f} mata")
    cetak(f'Mxx dengan ufuk 10 sesi ({len(mp)}): untung pada 3, 5 DAN 10 sesi = {semua3}')
    cetak(f"Backtest Mxx ({len(btm)} kaedah), median pulangan purata selepas 5/10/20/60 hari: "
          f"{RINGKAS['L04']['bt_median_r5']:+.2f} / {RINGKAS['L04']['bt_median_r10']:+.2f} / {RINGKAS['L04']['bt_median_r20']:+.2f} / "
          f"{RINGKAS['L04']['bt_median_r60']:+.2f} %; 60 hari > 20 hari bagi {RINGKAS['L04']['bt_naik_dengan_masa']} kaedah")
    cetak(f"Ufuk terbaik atas kohort sejajar ({len(sjm)} Mxx dengan >= 20 saham-hari): {terbaik}")

    # ================================================================ L05
    tajuk(5, 'KELUAR — bagaimana posisi ditutup, dan cara keluar mana lebih baik atas belian yang sama')
    sb = np.where(P.terbuka, 'masih terbuka', P.sebab_keluar.replace('', 'lain'))
    hari0 = (~P.terbuka) & (P.tarikh_keluar == P.tarikh_beli.astype(str)) & (P.sebab_keluar == 'henti')
    sb = np.where(hari0, 'henti pada hari beli', sb)
    Xs = P.assign(sebab=sb)
    SB = Xs.groupby(['kel', 'sebab']).pul.agg(posisi='size', purata='mean', menang=lambda s: (s > 0).mean() * 100).reset_index()
    SB['bahagian_pct'] = SB.posisi / SB.groupby('kel').posisi.transform('sum') * 100
    simpan('L05_sebab_keluar.csv', SB.sort_values(['kel', 'posisi'], ascending=[True, False]), index=False)
    cetak(SB.sort_values(['kel', 'posisi'], ascending=[True, False]).to_string(index=False, float_format=lambda v: f'{v:.2f}'))
    il = T[(T.tutup >= 20)].sort_values('pul_tutup', ascending=False).head(15)
    simpan('L05_ilusi_tutup_sahaja.csv', il[['nama', 'n', 'tutup', 'pul_tutup', 'pul_buka', 'jangkaan', 'tanpa5']], float_format='%.2f')
    klr = []
    for x, gx in N.groupby('keluar_n'):
        beza = [r.jangkaan - N[(N.masuk_n == r.masuk_n) & (N.keluar_n != x)].jangkaan.mean()
                for r in gx.itertuples() if ((N.masuk_n == r.masuk_n) & (N.keluar_n != x)).any()]
        klr.append(dict(keluar=x, peraturan=PERATURAN.get(x, ''), kombinasi=len(gx), posisi=int(gx.n.sum()),
                        tutup_pct=gx.tutup.sum() / gx.n.sum() * 100,
                        langsung_jangkaan=np.average(gx.jangkaan, weights=gx.n), langsung_tanpa5=gx.tanpa5.mean(),
                        langsung_menang=np.average(gx.menang, weights=gx.n),
                        beza_berpasangan=float(np.mean(beza)) if beza else np.nan,
                        backtest_tahan=gx.btn_tahan.mean(), backtest_lift=gx.btn_lift_tahan.mean(),
                        backtest_tanpa5=gx.btn_tanpa5.mean(), backtest_menang=gx.btn_menang.mean(),
                        backtest_rugi_min=gx.btn_rugi.min(), backtest_rugi_maks=gx.btn_rugi.max()))
    klr = pd.DataFrame(klr).sort_values('backtest_tahan', ascending=False)
    simpan('L05_keluar_nxx.csv', klr, index=False, float_format='%.2f')
    cetak('\nNxx ikut cara KELUAR (langsung 6 hari beli; backtest tahan 2020-25):')
    cetak(klr.to_string(index=False, float_format=lambda v: f'{v:.2f}'))
    M = T[(T.keluarga == 'M') & (T.n >= MIN_N)]
    PM = P[P.kel == 'M']
    lor = dict(kaedah=len(M), l1_purata_kaedah=float(M.jangkaan.mean()), l2_purata_kaedah=float(M.l2_jangkaan.mean()),
               l2_lebih_baik_pct=float((M.l2_lebih_l1 > 0).mean() * 100), posisi=len(PM),
               l1_semua_posisi=float(PM.pul.mean()), l2_semua_posisi=float(PM.pul2.mean()),
               l1_rugi_lebih_15_pct=float((PM.pul < -15).mean() * 100), l2_rugi_lebih_15_pct=float((PM.pul2 < -15).mean() * 100))
    simpan_json('L05_keluar_mxx_lorong.json', lor)
    RINGKAS['L05'] = dict(sebab={k_: g_.set_index('sebab')[['posisi', 'bahagian_pct', 'purata', 'menang']].to_dict('index')
                                 for k_, g_ in SB.groupby('kel')}, lorong_mxx=lor,
                          keluar_nxx=klr.set_index('keluar').to_dict('index'))
    cetak('\nMxx: keluar kaedah (L1) lawan Chandelier 4xATR tanpa henti (L2), posisi sama:')
    cetak(json.dumps({k_: round(v_, 2) for k_, v_ in lor.items()}))

    # ================================================================ L06
    tajuk(6, 'RISIKO — berapa teruk rugi boleh jadi')
    kr = ['nama', 'keluarga', 'kelas', 'n', 'n_cair', 'jangkaan', 'jangkaan_cair', 'terburuk', 'cvar10', 'rugi_purata', 'rugi8_pct', 'rugi15_pct', 'hari0', 'hari0_pct', 'mae',
          't4_sesi', 't4_pul', 't4_mdd', 'bt_mdd']
    simpan('L06_risiko.csv', T[kr].sort_values('cvar10'))
    r6 = {}
    for kel in ('M', 'N'):
        Pk, Tk = P[P.kel == kel], T[(T.keluarga == kel) & (T.n >= MIN_N)]
        r6[kel] = dict(posisi=len(Pk), rugi8_pct=float((Pk.pul < -8).mean() * 100), rugi15_pct=float((Pk.pul < -15).mean() * 100),
                       rugi25_pct=float((Pk.pul < -25).mean() * 100), terburuk=float(Pk.pul.min()),
                       kaedah=len(Tk), kaedah_terburuk_bawah_25=int((Tk.terburuk < -25).sum()),
                       median_cvar10=float(Tk.cvar10.median()), kaedah_ada_henti_hari_beli=int((Tk.hari0 > 0).sum()),
                       t4_mdd_median=float(Tk.t4_mdd.median()), t4_mdd_terburuk=float(Tk.t4_mdd.min()),
                       t4_mdd_lebih_10=int((Tk.t4_mdd < -10).sum()))
    bm = T[T.keluarga == 'M'].bt_mdd.dropna()
    r6['backtest_M'] = dict(kaedah=len(bm), mdd_median=float(bm.median()), mdd_terbaik=float(bm.max()),
                            mdd_dalam_10=int((bm >= -MDD_PENGGUNA).sum()))
    for kel in ('M', 'N'):
        Pk, Tk = P[P.kel == kel], T[(T.keluarga == kel) & (T.n >= MIN_N)]
        r6[f'kecairan_{kel}'] = dict(posisi_tidak_cair_pct=float((~Pk.cair).mean() * 100), jangkaan_semua=float(Pk.pul.mean()),
                                     jangkaan_cair=float(Pk[Pk.cair].pul.mean()), jangkaan_tidak_cair=float(Pk[~Pk.cair].pul.mean()),
                                     kaedah_jangkaan_positif=int((Tk.jangkaan > 0).sum()),
                                     kaedah_jangkaan_cair_positif=int((Tk.jangkaan_cair > 0).sum()),
                                     kaedah_tanpa5_positif=int((Tk.tanpa5 > 0).sum()),
                                     kaedah_tanpa5_cair_positif=int((Tk.tanpa5_cair > 0).sum()))
    simpan('L06_kecairan.csv', T[['nama', 'keluarga', 'kelas', 'n', 'n_cair', 'jangkaan', 'jangkaan_cair', 'tanpa5', 'tanpa5_cair']]
           .assign(beza=lambda d_: d_.jangkaan_cair - d_.jangkaan).sort_values('beza'))
    RINGKAS['L06'] = r6
    for k_, v_ in r6.items():
        cetak(f'  {k_}: ' + json.dumps({a_: round(b_, 2) for a_, b_ in v_.items()}))

    # ================================================================ L07
    tajuk(7, 'PASARAN LAWAN KAEDAH — skill residual-edge-analyzer (penerokaan: sampel di bawah minimum 60 sesi)')
    if RE.empty:
        cetak('tiada kaedah dengan sesi buku harian mencukupi')
        RINGKAS['L07'] = {}
    else:
        simpan('L07_pasaran_lawan_kaedah.csv', RE.join(T[['nama', 'kelas']]).sort_values('alpha_t', ascending=False))
        RINGKAS['L07'] = dict(kaedah=len(RE), sesi_maks=int(RE.sesi.max()), status=RE.status.value_counts().to_dict(),
                              layak=RE.layak_keputusan.value_counts().to_dict(),
                              r2_kolam_median=float(RE.r2_kolam.median()), beta_kolam_median=float(RE.beta_kolam.median()),
                              r2_spus_median=float(RE.r2_spus.median()),
                              alpha_t_lebih_2=int((RE.alpha_t > 2).sum()), alpha_t_kurang_neg2=int((RE.alpha_t < -2).sum()),
                              alpha_t_lebih_2_kedua_asas=int(((RE.alpha_t > 2) & (RE.alpha_t_spus > 2)).sum()),
                              sauh_t_berganda=float(stats.norm.ppf(1 - 0.05 / len(RE) / 2)))
        cetak(json.dumps({k_: (round(v_, 2) if isinstance(v_, float) else v_) for k_, v_ in RINGKAS['L07'].items()}))
        cetak('10 teratas ikut t alpha lawan kolam (penerokaan sahaja):')
        cetak(RE.join(T[['nama', 'kelas']]).sort_values('alpha_t', ascending=False)[
            ['nama', 'kelas', 'sesi', 'status', 'r2_kolam', 'beta_kolam', 'alpha_harian_pct', 'alpha_t', 'alpha_t_spus']].head(10)
            .to_string(float_format=lambda v: f'{v:.2f}'))

    # ================================================================ L08
    tajuk(8, 'KUALITI BACKTEST — skill backtest-expert atas registry set 431 (Mxx sahaja)')
    Bq = T[T.bte_keputusan.notna()][['nama', 'kelas', 'bt_keputusan', 'bt_n', 'bt_tahun', 'bt_win', 'bt_avgwin', 'bt_avgloss', 'bt_purata',
                                     'bt_cagr', 'bt_mdd', 'bt_h1', 'bt_h2', 'bt_set_positif', 'bte_keputusan', 'bte_sebab', 'bte_keputusan_mdd10']]
    simpan('L08_kualiti_backtest.csv', Bq.sort_values('bt_mdd', ascending=False))
    sebab = pd.Series([s for x in Bq.bte_sebab for s in str(x).split(';') if s]).value_counts().to_dict()
    RINGKAS['L08'] = dict(kaedah=len(Bq), keputusan=Bq.bte_keputusan.value_counts().to_dict(), sebab=sebab,
                          keputusan_had_mdd10=Bq.bte_keputusan_mdd10.value_counts().to_dict(),
                          tahun_diuji=float(Bq.bt_tahun.median()), h1_dan_h2_positif=int(((Bq.bt_h1 > 0) & (Bq.bt_h2 > 0)).sum()))
    cetak(json.dumps(RINGKAS['L08'], ensure_ascii=False))

    # ================================================================ L09
    tajuk(9, 'KOMBINASI — masuk x keluar, kaedah sepakat, pasangan kaedah')
    simpan('L09_nxx_masuk_x_keluar_langsung.csv', N.pivot_table(index='masuk_n', columns='keluar_n', values='jangkaan'), float_format='%.2f')
    simpan('L09_nxx_masuk_x_keluar_backtest.csv', N.pivot_table(index='masuk_n', columns='keluar_n', values='btn_tahan'), float_format='%.2f')
    nx = T[T.keluarga == 'N'].sort_values('btn_tahan', ascending=False)
    simpan('L09_nxx_semua_kombinasi.csv', nx[['nama', 'n', 'tutup', 'hari_beli', 'jangkaan', 'tanpa5', 'r3', 'lift3', 'l2_jangkaan', 'btn_pangkat',
                                              'btn_tahan', 'btn_lift_tahan', 'btn_tanpa5', 'btn_menang', 'btn_rugi']], float_format='%.2f')
    an = T[T.keluarga == 'N'].dropna(subset=['btn_tahan', 'jangkaan'])
    s3 = stats.spearmanr(an.btn_tahan, an.jangkaan)
    top10bt = nx.head(10)
    hari1 = min(XU[5].tarikh_beli)
    kb = []
    for h in (5, 10):
        kb += konsensus(XU[h], h)
        kb += konsensus(XU[h][XU[h].tarikh_beli != hari1], h, f'tanpa hari beli pertama {hari1}')
    kb = pd.DataFrame(kb)
    simpan('L09_kaedah_sepakat.csv', kb, index=False)
    ps = pasangan(XU[5])
    simpan_json('L09_pasangan_mxx.json', ps)
    RINGKAS['L09'] = dict(nxx_kombinasi=len(an), nxx_spearman_bt_langsung=float(s3.statistic),
                          top10_backtest_jangkaan_langsung=float(top10bt.jangkaan.mean()),
                          semua_nxx_jangkaan_langsung=float(nx.jangkaan.mean()),
                          top10_backtest_positif=int((top10bt.jangkaan > 0).sum()), pasangan=ps,
                          sepakat=kb[(kb.ufuk == 5) & (kb.jenis == 'kaedah Mxx sepakat')].to_dict('records'))
    cetak(f"Nxx: 10 kombinasi berpangkat backtest tertinggi -> jangkaan langsung purata {top10bt.jangkaan.mean():+.2f}% "
          f"({int((top10bt.jangkaan > 0).sum())}/10 positif) lawan semua 94: {nx.jangkaan.mean():+.2f}%; Spearman {s3.statistic:+.2f}")
    cetak(top10bt[['nama', 'n', 'tutup', 'jangkaan', 'tanpa5', 'btn_pangkat', 'btn_tahan', 'btn_tanpa5', 'btn_rugi']].to_string(float_format=lambda v: f'{v:.2f}'))
    cetak('\nBilangan kaedah sepakat atas saham-hari sama (5 sesi):')
    cetak(kb[kb.ufuk == 5].to_string(index=False, float_format=lambda v: f'{v:.2f}'))
    cetak('\nSemua pasangan Mxx: ' + json.dumps({k_: round(v_, 2) for k_, v_ in ps.items()}))

    # ================================================================ L10
    tajuk(10, 'KEBOLEHPERCAYAAN — adakah "terbaik" kekal terbaik?')
    rng = np.random.default_rng(BENIH)
    st = []
    for h in (3, 5, 10):
        X = XU[h]
        st.append(kestabilan(X[X.kel == 'M'], f'Mxx lift {h} sesi', rng=rng))
        st.append(kestabilan(X[X.kel == 'N'], f'Nxx lift {h} sesi', min_sep=10, rng=rng))
    M5, M10 = XU[5][XU[5].kel == 'M'].copy(), XU[10][XU[10].kel == 'M'].copy()
    st.append(kestabilan(M5[M5.tarikh_beli != hari1], f'Mxx lift 5 sesi tanpa {hari1}', rng=rng))
    st.append(kestabilan(XU[3][(XU[3].kel == 'M') & (XU[3].tarikh_beli != hari1)], f'Mxx lift 3 sesi tanpa {hari1}', rng=rng))
    st = pd.DataFrame(st)
    simpan('L10_kestabilan.csv', st, index=False)
    cetak(st.to_string(index=False, float_format=lambda v: f'{v:.2f}'))
    idm = list(T[(T.keluarga == 'M') & (T.n5 >= MIN_N)].index)
    pl = {'semua hari beli': plasebo_tapis(M5, M10, idm),
          f'tanpa hari beli pertama {hari1}': plasebo_tapis(M5[M5.tarikh_beli != hari1], M10[M10.tarikh_beli != hari1], idm)}
    simpan_json('L10_plasebo.json', pl)
    a = T[(T.keluarga == 'M') & (T.tutup >= 20)].dropna(subset=['bt_purata', 'jangkaan'])
    s1 = stats.spearmanr(a.bt_purata, a.jangkaan)
    b = a.dropna(subset=['lift5'])
    s2 = stats.spearmanr(b.bt_purata, b.lift5)
    RINGKAS['L10'] = dict(kestabilan=st.set_index('label').to_dict('index'), plasebo=pl,
                          mxx_bt_lawan_langsung=dict(n=len(a), jangkaan=float(s1.statistic), p=float(s1.pvalue),
                                                     lift5=float(s2.statistic), p_lift5=float(s2.pvalue)))
    for k_, v_ in pl.items():
        cetak(f'Plasebo ({k_}): ' + json.dumps({a_: round(b_, 2) for a_, b_ in v_.items()}))
    cetak(f'Spearman backtest lawan langsung (Mxx, >= 20 ditutup, n {len(a)}): jangkaan {s1.statistic:+.2f} (p {s1.pvalue:.2f}); '
          f'lift 5 sesi {s2.statistic:+.2f} (p {s2.pvalue:.2f})')

    # ================================================================ L11
    tajuk(11, 'CORONG DAN SENARAI AKHIR')
    cr = corong(T)
    simpan('L11_corong.csv', cr, index=False)
    cetak(cr.to_string(index=False))
    pantau = T[T.kelas == 'PANTAU'].sort_values('jangkaan', ascending=False)
    ka = ['nama', 'teks_masuk', 'teks_pegang', 'teks_keluar', 'teks_henti', 'n', 'tutup', 'hari_beli', 'jangkaan', 'tanpa5', 'n_cair', 'jangkaan_cair',
          'tanpa5_cair', 'menang', 'payoff',
          'r3', 'r5', 'r10', 'lift5', 'lift10', 'lift5_A', 'lift5_B', 'n5', 'n10', 'l2_jangkaan', 'hari0', 'terburuk', 'rugi15_pct',
          'buku_ci_bawah', 't4_pul', 't4_mdd', 't4_persentil', 're_r2_kolam', 're_beta_kolam', 're_alpha_t', 're_alpha_t_spus', 're_status',
          'bt_purata', 'bt_menang', 'bt_hari', 'bt_cagr', 'bt_mdd', 'bt_set_positif', 'bte_keputusan', 'bte_sebab', 'bte_keputusan_mdd10']
    simpan('L11_senarai_pantau.csv', pantau[ka], float_format='%.2f')
    nawal = T[(T.keluarga == 'N') & (T.btn_pangkat <= 10) & (T.jangkaan > 0) & (T.tanpa5 > 0)].sort_values('btn_pangkat')
    simpan('L11_nxx_awal.csv', nawal[['nama', 'teks_masuk', 'teks_keluar', 'n', 'tutup', 'hari_beli', 'jangkaan', 'tanpa5', 'n_cair', 'jangkaan_cair',
                                      'tanpa5_cair', 'r3', 'lift3',
                                      'btn_pangkat', 'btn_tahan', 'btn_lift_tahan', 'btn_tanpa5', 'btn_menang', 'btn_rugi']], float_format='%.2f')
    RINGKAS['L11'] = dict(corong=cr.to_dict('records'), pantau=list(pantau.index), nxx_awal=list(nawal.index))
    cetak(f'\nSenarai pantau ({len(pantau)}): {list(pantau.index)}')
    cetak(pantau[['nama', 'n', 'tutup', 'hari_beli', 'jangkaan', 'tanpa5', 'n_cair', 'jangkaan_cair', 'tanpa5_cair', 'lift5', 'lift10', 'hari0', 're_alpha_t', 're_r2_kolam',
                  'bte_keputusan', 'bte_keputusan_mdd10', 'bt_mdd']].to_string(float_format=lambda v: f'{v:.2f}'))
    cetak(f'\nNxx awal (pangkat backtest <= 10, jangkaan dan tanpa5 langsung > 0; TERLALU AWAL): {list(nawal.index)}')
    cetak(nawal[['nama', 'n', 'tutup', 'jangkaan', 'tanpa5', 'n_cair', 'jangkaan_cair', 'tanpa5_cair', 'lift3', 'btn_pangkat', 'btn_tahan', 'btn_rugi']]
          .to_string(float_format=lambda v: f'{v:.2f}'))

    # ---------------------------------------------------------------- jadual semua kaedah (L02)
    tertib = {'PANTAU': 0, 'CAMPUR': 1, 'TERLALU AWAL': 2, 'LEMAH': 3, 'STRUKTUR GAGAL': 4}
    S = T.assign(t=T.kelas.map(tertib)).sort_values(['keluarga', 't', 'jangkaan'], ascending=[True, True, False])
    L = ['# Semua kaedah M dan N, satu per satu (langkah 2; data langsung; maklumat, BUKAN keputusan)', '',
         status_kad.baris(), '',
         f"Dijana `kajian/analisa_mn/analisa.py` atas kad skor harga {KS['harga_pada']}. Jangan ubah manual. "
         'Bacaan setiap langkah: `kajian/KAJIAN_M_N_SATU_PER_SATU.md`. Jadual penuh (semua lajur, teks masuk / pegang / '
         'keluar / henti): `hasil/L02_kaedah.csv`.', '',
         'Lajur: **Jangkaan** = purata semua posisi termasuk yang masih terbuka (ditanda ke pasaran), ikut keluar '
         'kaedah. **r3/r5/r10** = pulangan purata selepas 3/5/10 sesi tanpa mengira peraturan keluar. **Lift 5** = '
         'r5 tolak saham lain yang Lejar beli pada hari dan tahap turun-naik sama. **A/B** = lift 5 pada dua separuh '
         'hari beli. **L2** = jangkaan jika keluar ikut Chandelier. **Backtest** = purata setiap dagangan '
         '(Mxx set 431; Nxx tingkap tahan).', '']
    for kel, tjk in (('M', 'Kaedah Mxx'), ('N', 'Kombinasi Nxx (masuk × keluar)')):
        L += [f'## {tjk}', '',
              '| Kaedah | Kelas | Posisi/tutup | Hari beli | Jangkaan % | tanpa5 % | r3 | r5 | r10 | Lift 5 | A / B | L2 % | Hari-0 % | Backtest % | Sebab |',
              '|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|']
        for i, r in S[S.keluarga == kel].iterrows():
            bt = r.bt_purata if kel == 'M' else r.btn_tahan
            L.append(f"| `{i}` {str(r.nama)[:38]} | {r.kelas} | {int(r.n)}/{int(r.tutup)} | {int(r.hari_beli)} | "
                     f"{f(r.jangkaan)} | {f(r.tanpa5)} | {f(r.get('r3'))} | {f(r.get('r5'))} | {f(r.get('r10'))} | "
                     f"{f(r.get('lift5'))} | {f(r.get('lift5_A'))} / {f(r.get('lift5_B'))} | {f(r.l2_jangkaan)} | "
                     f"{f(r.hari0_pct, 0, False)} | {f(bt)} | {r.sebab_kelas} |")
        L.append('')
    open(os.path.join(HASIL, 'L02_SEMUA_KAEDAH.md'), 'w', encoding='utf-8').write('\n'.join(L))
    simpan_json('ringkasan.json', RINGKAS)
    open(os.path.join(HASIL, 'log.txt'), 'w', encoding='utf-8').write('\n'.join(LOG) + '\n')
    return 0


if __name__ == '__main__':
    sys.exit(main())
