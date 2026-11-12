#!/usr/bin/env python3
"""Analisa satu per satu kaedah M dan N: data LANGSUNG Lejar Penuh + backtest sedia ada (12 Nov 2026).

Permintaan pengguna 12 Nov 2026: nilai SEMUA kaedah M dan N dalam papertrade satu per satu (masuk, pegang,
keluar), susun datanya, dan cari yang terbaik. Keputusan pengguna pada hari sama: "analisa dulu" (TIADA Nxx
baharu didaftar), "data langsung + backtest sedia ada" (tiada backtest baharu), "biar data tentukan" tempoh
pegang, hasil disimpan dalam repo.

Ini MAKLUMAT, BUKAN keputusan: satu-satunya keputusan wang sebenar ialah `laporan/KAD_SKOR.md`. Skrip ini
hanya MEMBACA Lejar, stor harga, kad skor dan fail backtest; ia tidak mengubah mana-mana daripadanya.

Apa yang dikira:
  1. Setiap kaedah: angka kad skor (posisi, jangkaan termasuk posisi terbuka, tanpa5, payoff, hari-0) +
     pulangan UFUK TETAP 1/3/5/10/15 sesi (beli pada buka -> tutup sesi ke-h, kos 0.2%) + lift lawan saham lain
     yang Lejar beli pada hari sama dan tercile ATR sama (reka bentuk `standard/lift_kaedah.py`) + dua separuh
     hari beli + lorong 2 (Chandelier) atas posisi yang sama + backtest sedia ada.
  2. Kestabilan: adakah kaedah yang baik pada separuh hari beli juga baik pada separuh lagi? (pecahan rawak)
  3. Plasebo senarai pantau: berapa kaedah lulus tapis jika sahamnya dipilih RAWAK pada hari dan ATR sama?
  4. Nxx: pecahan masuk x keluar (langsung dan backtest). Mxx: keluar kaedah lawan Chandelier.
  5. Kombinasi kaedah pada data langsung: bilangan kaedah sepakat, dan semua pasangan Mxx (kestabilan sahaja;
     TIADA pasangan dipilih).

Guna: python3 BacktestShariah2/kajian/analisa_mn/analisa.py        (~2 minit)
Keluaran: BacktestShariah2/kajian/analisa_mn/hasil/*.csv, SEMUA_KAEDAH.md, log.txt
"""
import json
import os
import re
import sys

import numpy as np
import pandas as pd
from scipy import stats

HERE = os.path.dirname(os.path.abspath(__file__))
BS2 = os.path.dirname(os.path.dirname(HERE))
AKAR = os.path.dirname(BS2)
sys.path.insert(0, os.path.join(BS2, 'standard'))
import lift_kaedah as lk  # noqa: E402
import status_kad  # noqa: E402

HASIL = os.path.join(HERE, 'hasil')
UFUK = (1, 3, 5, 10, 15)
BENIH = 20261112
N_PECAH = 500          # pecahan rawak hari beli (kestabilan)
N_PLASEBO = 300        # cabutan plasebo senarai pantau
# Tapis senarai pantau (ditulis sebelum lift 5/10 sesi dan separuh hari beli dilihat; angka kad skor sudah dilihat)
MIN_N, MIN_HARI = 30, 10
HARI0_MAKS = 20.0      # sama dengan label cantas C1
LOG = []


def cetak(*a):
    s = ' '.join(str(x) for x in a)
    LOG.append(s)
    print(s)


def keluarga(mid):
    return 'GB' if str(mid).startswith('GB') else str(mid)[:1]


def pecah_n(mid):
    """'N19X13' -> ('N19', 'X13'); selain itu (None, None)."""
    m = re.fullmatch(r'(N\d+)(X\d+)', str(mid))
    return (m.group(1), m.group(2)) if m else (None, None)


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
    return P


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
    f = os.path.join(BS2, 'data', 'penanda_aras', 'spus_harian.csv')
    d = pd.read_csv(f, comment='#', header=None, names=['tarikh', 'buka', 'tutup'])
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
                 bt_h1=a.h1 * 100, bt_h2=a.h2 * 100)
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


PERATURAN = {}


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
    """Lift purata setiap kaedah pada hari beli berindeks genap (A) dan ganjil (B), ikut hari beli kaedah itu."""
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


def kelas(r):
    """Label mekanikal (maklumat). Tertib penilaian tetap."""
    def ada(v):
        return v is not None and np.isfinite(v)
    if r.n >= MIN_N and r.hari0_pct >= HARI0_MAKS:
        return 'STRUKTUR GAGAL', f'henti hari-0 {r.hari0_pct:.0f}% posisi (G4 pasti gagal)'
    if r.n < MIN_N or r.hari_beli < MIN_HARI:
        return 'TERLALU AWAL', f'{r.n} posisi, {r.hari_beli} hari beli'
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


def f(v, k=2, tanda=True):
    if v is None or (isinstance(v, float) and not np.isfinite(v)) or pd.isna(v):
        return '–'
    return f'{v:+.{k}f}' if tanda else f'{v:.{k}f}'


# ---------------------------------------------------------------- utama

def main():
    os.makedirs(HASIL, exist_ok=True)
    KS = json.load(open(os.path.join(BS2, 'data', 'analisis', 'kad_skor.json'), encoding='utf-8'))
    K = pd.DataFrame(KS['rows'], columns=KS['kol']).set_index('id')
    num = ['n', 'tutup', 'buka_pct', 'hari_beli', 'jangkaan', 'pul_tutup', 'pul_buka', 'menang', 'untung_purata',
           'rugi_purata', 'payoff', 'cvar10', 'terburuk', 'tanpa5', 'mae', 'mfe', 'jangkaan_slip', 'hari0_pct',
           'hari_on', 'hari_off', 'buku_harian', 'buku_ci_bawah', 'buku_ci_atas', 'bt_hari', 'bt_purata',
           'bt_menang', 't4_sesi', 't4_pul', 't4_mdd', 't4_spus', 't4_persentil']
    K[num] = K[num].apply(pd.to_numeric, errors='coerce')
    cetak(f"Kad skor harga {KS['harga_pada']}: {len(K)} kaedah, {KS['posisi']} posisi langsung, "
          f"{KS['hari_beli']} hari beli (ON {KS['hari_on']}, OFF {KS['hari_off']})")

    P = muat_posisi()
    cetak(f'Posisi langsung dimuat: {len(P)} ({P.id_kaedah.nunique()} kaedah)')
    sesi, C, A = lk.panel_harga()
    mentah = lk.posisi()
    XU = {h: ufuk_tetap(mentah, sesi, C, A, h) for h in UFUK}

    # ---- 1. kadar asas kolam ikut ufuk (semua saham-hari unik) lawan SPUS tingkap sama
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
            sp = []
            for d in U.tarikh_beli:
                i = ibuka.get(d)
                sp.append((SP.tutup[i + h - 1] / SP.buka[i] - 1) * 100 if i is not None and i + h - 1 < len(SP) else np.nan)
            asas.append(dict(ufuk=h, kolam=kel, hari_beli=U.tarikh_beli.nunique(), saham_hari=len(U),
                             r_purata=U.r.mean(), r_median=U.r.median(), menang=(U.r > 0).mean() * 100,
                             spus_tingkap_sama=float(np.nanmean(sp))))
    asas = pd.DataFrame(asas)
    asas.to_csv(os.path.join(HASIL, 'kadar_asas.csv'), index=False, float_format='%.3f')
    cetak('\n== Kadar asas kolam (saham-hari unik; beli buka -> tutup sesi ke-h; kos 0.2%) ==')
    cetak(asas.to_string(index=False, float_format=lambda v: f'{v:.2f}'))

    # ---- 2. jadual setiap kaedah
    T = K.copy()
    for h, X in XU.items():
        if not X.empty:
            T = T.join(ringkas_ufuk(X, h))
    for h in (5, 10):
        T = T.join(separuh(XU[h], h))
    g = P.groupby('id_kaedah')
    T = T.join(pd.DataFrame({'l2_jangkaan': g.pul2.mean(), 'l2_tutup': g.terbuka2.apply(lambda s: int((~s).sum())),
                             'l2_lebih_l1': g.apply(lambda x: (x.pul2 - x.pul).mean(), include_groups=False),
                             'hari_pegang_median': g.hari_pegang.median()}))
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
    ke = [kelas(r) for r in T.itertuples()]
    T['kelas'], T['sebab_kelas'] = [x[0] for x in ke], [x[1] for x in ke]
    T['masuk_n'], T['keluar_n'] = zip(*[pecah_n(i) for i in T.index])
    depan = ['nama', 'keluarga', 'kelas', 'sebab_kelas', 'status', 'n', 'tutup', 'hari_beli', 'jangkaan', 'tanpa5',
             'menang', 'payoff', 'pul_tutup', 'pul_buka', 'hari0_pct', 'mfe', 'mae', 'hari_pegang_median',
             'buku_harian', 'buku_ci_bawah', 'buku_ci_atas']
    T = T[depan + [c for c in T.columns if c not in depan]]
    T.sort_values(['keluarga', 'jangkaan'], ascending=[True, False]).to_csv(
        os.path.join(HASIL, 'kaedah.csv'), float_format='%.4f')
    cetak('\n== Kelas (label mekanikal, maklumat) ==')
    cetak(pd.crosstab(T.kelas, T.keluarga).to_string())

    cukup = T[(T.n >= MIN_N) & (T.hari_beli >= 5)]
    cetak(f'\nKaedah dengan >= {MIN_N} posisi dan >= 5 hari beli: {len(cukup)}; jangkaan > 0: '
          f'{int((cukup.jangkaan > 0).sum())}; had bawah selang 95% buku harian > 0: '
          f'{int((cukup.buku_ci_bawah > 0).sum())}; tanpa5 > 0: {int((cukup.tanpa5 > 0).sum())}')
    a = T[(T.keluarga == 'M') & (T.tutup >= 20)].dropna(subset=['bt_purata', 'jangkaan'])
    s1 = stats.spearmanr(a.bt_purata, a.jangkaan)
    b = a.dropna(subset=['lift5'])
    s2 = stats.spearmanr(b.bt_purata, b.lift5)
    cetak(f'Spearman backtest lawan langsung (Mxx, >= 20 ditutup, n {len(a)}): jangkaan {s1.statistic:+.2f} '
          f'(p {s1.pvalue:.2f}); lift 5 sesi {s2.statistic:+.2f} (p {s2.pvalue:.2f})')
    an = T[(T.keluarga == 'N')].dropna(subset=['btn_tahan', 'jangkaan'])
    if len(an) > 10:
        s3 = stats.spearmanr(an.btn_tahan, an.jangkaan)
        cetak(f'Spearman backtest tahan lawan langsung (Nxx, n {len(an)}): {s3.statistic:+.2f} (p {s3.pvalue:.2f})')

    m = T[(T.keluarga == 'M') & (T.n >= MIN_N) & (T.hari_beli >= MIN_HARI) & (T.hari0_pct < HARI0_MAKS)]
    tap = {'jangkaan > 0': m.jangkaan > 0, 'tanpa5 > 0': m.tanpa5 > 0, 'lift 5 sesi > 0': m.lift5 > 0,
           'lift 10 sesi > 0': m.lift10 > 0, 'lift 5 sesi > 0 pada kedua-dua separuh': (m.lift5_A > 0) & (m.lift5_B > 0),
           'backtest > 0': m.bt_purata > 0}
    cetak(f'\n== Tapis senarai pantau: {len(m)} Mxx cukup data dan bukan STRUKTUR GAGAL ==')
    for k_, c in tap.items():
        cetak(f'  {k_}: {int(c.sum())}')
    pd.DataFrame([dict(tapis=k_, lulus=int(c.sum()), daripada=len(m)) for k_, c in tap.items()]).to_csv(
        os.path.join(HASIL, 'tapis.csv'), index=False)
    lg = T[(T.n5 >= MIN_N)].sort_values('r5', ascending=False)
    kolp = ['nama', 'kelas', 'n5', 'hb5', 'r1', 'r3', 'r5', 'r10', 'r15', 'lift3', 'lift5', 'lift10', 'jangkaan', 'tanpa5']
    lg[kolp].to_csv(os.path.join(HASIL, 'lengkung_pegang.csv'), float_format='%.2f')
    cetak(f'\n== Lengkung pegang: {len(lg)} kaedah dengan >= {MIN_N} saham-hari 5 sesi; r3, r5 dan r10 semua > 0: '
          f'{int(((lg.r3 > 0) & (lg.r5 > 0) & (lg.r10 > 0)).sum())} ==')
    cetak(lg[kolp].head(15).to_string(float_format=lambda v: f'{v:.2f}'))
    X5 = XU[5]
    sd_hari = X5.drop_duplicates(['saham', 'tarikh_beli']).groupby('tarikh_beli').r.mean()
    cetak(f'\nPulangan 5 sesi kolam ikut HARI BELI: min {sd_hari.min():+.2f}, maks {sd_hari.max():+.2f}, '
          f'SD {sd_hari.std():.2f} mata; SD lift 5 sesi merentas KAEDAH (>= {MIN_N} saham-hari): {lg.lift5.std():.2f} mata')
    sd_hari.rename('r5_kolam').to_csv(os.path.join(HASIL, 'kolam_ikut_hari.csv'), float_format='%.2f')

    # ---- 3. ilusi "tutup sahaja"
    il = T[(T.tutup >= 20)].sort_values('pul_tutup', ascending=False).head(15)
    il[['nama', 'n', 'tutup', 'pul_tutup', 'pul_buka', 'jangkaan', 'tanpa5']].to_csv(
        os.path.join(HASIL, 'ilusi_tutup_sahaja.csv'), float_format='%.2f')

    # ---- 4. kestabilan + plasebo
    rng = np.random.default_rng(BENIH)
    st = []
    for h in (3, 5, 10):
        X = XU[h]
        st.append(kestabilan(X[X.kel == 'M'], f'Mxx lift {h} sesi', rng=rng))
        st.append(kestabilan(X[X.kel == 'N'], f'Nxx lift {h} sesi', min_sep=10, rng=rng))
    st = pd.DataFrame(st)
    st.to_csv(os.path.join(HASIL, 'kestabilan.csv'), index=False, float_format='%.3f')
    cetak('\n== Kestabilan: pecahan rawak hari beli kepada dua separuh ==')
    cetak(st.to_string(index=False, float_format=lambda v: f'{v:.2f}'))

    idm = list(T[(T.keluarga == 'M') & (T.n5 >= MIN_N)].index)
    M5, M10 = XU[5][XU[5].kel == 'M'].copy(), XU[10][XU[10].kel == 'M'].copy()
    hari1 = min(M5.tarikh_beli)
    pl = {'semua hari beli': plasebo_tapis(M5, M10, idm),
          f'tanpa hari beli pertama {hari1}': plasebo_tapis(M5[M5.tarikh_beli != hari1], M10[M10.tarikh_beli != hari1], idm)}
    json.dump(pl, open(os.path.join(HASIL, 'plasebo_tapis.json'), 'w'), indent=1)
    st2 = pd.DataFrame([kestabilan(M5[M5.tarikh_beli != hari1], f'Mxx lift 5 sesi tanpa {hari1}', rng=rng),
                        kestabilan(XU[3][(XU[3].kel == 'M') & (XU[3].tarikh_beli != hari1)], f'Mxx lift 3 sesi tanpa {hari1}', rng=rng)])
    st = pd.concat([st, st2], ignore_index=True)
    st.to_csv(os.path.join(HASIL, 'kestabilan.csv'), index=False, float_format='%.3f')
    cetak(st2.to_string(index=False, float_format=lambda v: f'{v:.2f}'))
    cetak('\n== Plasebo tapis ufuk tetap (Mxx, >= 30 saham-hari 5 sesi): lift5 > 0, kedua-dua separuh > 0, lift10 > 0 ==')
    for k_, v_ in pl.items():
        cetak(f'  {k_}: ' + json.dumps({a_: round(b_, 2) for a_, b_ in v_.items()}))

    # ---- 5. Nxx: masuk x keluar
    N = T[T.masuk_n.notna()].copy()
    N['berat'] = N.n
    piv = N.pivot_table(index='masuk_n', columns='keluar_n', values='jangkaan')
    piv.to_csv(os.path.join(HASIL, 'nxx_masuk_x_keluar_langsung.csv'), float_format='%.2f')
    N.pivot_table(index='masuk_n', columns='keluar_n', values='btn_tahan').to_csv(
        os.path.join(HASIL, 'nxx_masuk_x_keluar_backtest.csv'), float_format='%.2f')
    kl = []
    for x, gx in N.groupby('keluar_n'):
        # berpasangan: beza lawan purata keluar LAIN bagi masuk yang sama
        beza = [r.jangkaan - N[(N.masuk_n == r.masuk_n) & (N.keluar_n != x)].jangkaan.mean()
                for r in gx.itertuples() if ((N.masuk_n == r.masuk_n) & (N.keluar_n != x)).any()]
        kl.append(dict(keluar=x, peraturan=PERATURAN.get(x, ''),
                       kombinasi=len(gx), posisi=int(gx.n.sum()), tutup_pct=gx.tutup.sum() / gx.n.sum() * 100,
                       langsung_jangkaan=np.average(gx.jangkaan, weights=gx.n), langsung_tanpa5=gx.tanpa5.mean(),
                       langsung_menang=np.average(gx.menang, weights=gx.n),
                       beza_berpasangan=float(np.mean(beza)) if beza else np.nan,
                       backtest_tahan=gx.btn_tahan.mean(), backtest_lift=gx.btn_lift_tahan.mean(),
                       backtest_tanpa5=gx.btn_tanpa5.mean(), backtest_menang=gx.btn_menang.mean()))
    kl = pd.DataFrame(kl).sort_values('backtest_tahan', ascending=False)
    kl.to_csv(os.path.join(HASIL, 'nxx_keluar.csv'), index=False, float_format='%.2f')
    cetak('\n== Nxx ikut cara KELUAR (langsung 6 hari beli; backtest tahan 2020-25) ==')
    cetak(kl.to_string(index=False, float_format=lambda v: f'{v:.2f}'))
    ms = N.groupby('masuk_n').agg(nama=('nama', lambda s: s.iloc[0].split(' → ')[0].split(' x X')[0][:44]),
                                  kombinasi=('n', 'size'), posisi=('n', 'sum'),
                                  langsung_jangkaan=('jangkaan', 'mean'), langsung_lift5=('lift5', 'mean'),
                                  langsung_r3=('r3', 'mean'), backtest_tahan=('btn_tahan', 'mean'),
                                  backtest_lift=('btn_lift_tahan', 'mean')).sort_values('langsung_jangkaan', ascending=False)
    ms.to_csv(os.path.join(HASIL, 'nxx_masuk.csv'), float_format='%.2f')
    cetak('\n== Nxx ikut isyarat MASUK ==')
    cetak(ms.to_string(float_format=lambda v: f'{v:.2f}'))
    e1 = stats.spearmanr(ms.backtest_tahan, ms.langsung_jangkaan)
    e2 = stats.spearmanr(ms.backtest_lift, ms.langsung_lift5.fillna(0) * 0 + N.groupby('masuk_n').lift3.mean().reindex(ms.index),
                         nan_policy='omit')
    cetak(f'Spearman peringkat MASUK ({len(ms)} isyarat): backtest tahan lawan jangkaan langsung {e1.statistic:+.2f} '
          f'(p {e1.pvalue:.4f}); lift backtest lawan lift langsung 3 sesi {e2.statistic:+.2f} (p {e2.pvalue:.2f})')
    for x in ('X36', 'X16'):
        gx = N[N.keluar_n == x].dropna(subset=['btn_tahan', 'jangkaan'])
        e3 = stats.spearmanr(gx.btn_tahan, gx.jangkaan)
        cetak(f'  dalam keluar {x} sahaja ({len(gx)} kombinasi): {e3.statistic:+.2f} (p {e3.pvalue:.3f})')

    # ---- 6. Mxx: keluar kaedah (lorong 1) lawan Chandelier (lorong 2) atas posisi sama
    M = T[(T.keluarga == 'M') & (T.n >= MIN_N)]
    PM = P[P.id_kaedah.str.startswith('M')]
    lor = dict(kaedah=len(M), l1_purata_kaedah=float(M.jangkaan.mean()), l2_purata_kaedah=float(M.l2_jangkaan.mean()),
               l2_lebih_baik_pct=float((M.l2_lebih_l1 > 0).mean() * 100), posisi=len(PM),
               l1_semua_posisi=float(PM.pul.mean()), l2_semua_posisi=float(PM.pul2.mean()),
               l1_rugi_lebih_15_pct=float((PM.pul < -15).mean() * 100),
               l2_rugi_lebih_15_pct=float((PM.pul2 < -15).mean() * 100))
    json.dump(lor, open(os.path.join(HASIL, 'mxx_lorong.json'), 'w'), indent=1)
    cetak('\n== Mxx: keluar kaedah (L1) lawan Chandelier 4xATR (L2), posisi sama ==')
    cetak(json.dumps(lor))

    # ---- 7. kombinasi kaedah pada data langsung
    kb = []
    hari1 = min(XU[5].tarikh_beli)
    for h in (5, 10):
        kb += konsensus(XU[h], h)
        kb += konsensus(XU[h][XU[h].tarikh_beli != hari1], h, f'tanpa hari beli pertama {hari1}')
    kb = pd.DataFrame(kb)
    kb.to_csv(os.path.join(HASIL, 'konsensus.csv'), index=False, float_format='%.3f')
    cetak('\n== Bilangan kaedah sepakat atas saham-hari yang sama ==')
    cetak(kb.to_string(index=False, float_format=lambda v: f'{v:.2f}'))
    ps = pasangan(XU[5])
    json.dump(ps, open(os.path.join(HASIL, 'pasangan_mxx.json'), 'w'), indent=1)
    cetak('\n== Semua pasangan Mxx (saham-hari bersama, lift 5 sesi) ==')
    cetak(json.dumps(ps))

    # ---- 8. senarai pantau + jadual semua kaedah
    pantau = T[T.kelas == 'PANTAU'].sort_values('jangkaan', ascending=False)
    kol = ['nama', 'n', 'tutup', 'hari_beli', 'jangkaan', 'tanpa5', 'menang', 'payoff', 'r3', 'r5', 'r10', 'lift5',
           'lift10', 'lift5_A', 'lift5_B', 'l2_jangkaan', 'hari0_pct', 'buku_ci_bawah', 't4_pul', 't4_persentil',
           'bt_purata', 'bt_menang', 'bt_hari', 'bt_set_positif', 'teks_masuk', 'teks_keluar', 'teks_pegang', 'teks_henti']
    pantau[kol].to_csv(os.path.join(HASIL, 'senarai_pantau.csv'), float_format='%.2f')
    cetak(f'\n== Senarai pantau: {len(pantau)} kaedah ==')
    cetak(pantau[kol[:22]].to_string(float_format=lambda v: f'{v:.2f}'))
    nawal = T[(T.keluarga == 'N')].sort_values('btn_tahan', ascending=False)
    nawal[['nama', 'n', 'tutup', 'hari_beli', 'jangkaan', 'tanpa5', 'r3', 'lift3', 'l2_jangkaan', 'btn_pangkat',
           'btn_tahan', 'btn_lift_tahan', 'btn_tanpa5', 'btn_menang', 'btn_rugi']].to_csv(
        os.path.join(HASIL, 'nxx_semua.csv'), float_format='%.2f')

    tertib = {'PANTAU': 0, 'CAMPUR': 1, 'TERLALU AWAL': 2, 'LEMAH': 3, 'STRUKTUR GAGAL': 4}
    S = T.assign(t=T.kelas.map(tertib)).sort_values(['keluarga', 't', 'jangkaan'], ascending=[True, True, False])
    L = ['# Semua kaedah M dan N, satu per satu (data langsung; maklumat, BUKAN keputusan)', '',
         status_kad.baris(), '',
         f"Dijana `kajian/analisa_mn/analisa.py` atas kad skor harga {KS['harga_pada']}. Jangan ubah manual. "
         'Penjelasan lajur dan bacaan: `kajian/KAJIAN_M_N_SATU_PER_SATU.md`. Jadual penuh (semua lajur, teks masuk / '
         'pegang / keluar): `hasil/kaedah.csv`.', '',
         'Lajur: **Jangkaan** = purata semua posisi termasuk yang masih terbuka (ditanda ke pasaran), ikut keluar '
         'kaedah. **r3/r5/r10** = pulangan purata selepas 3/5/10 sesi tanpa mengira peraturan keluar. **Lift 5** = '
         'r5 tolak saham lain yang Lejar beli pada hari dan tahap turun-naik sama. **A/B** = lift 5 pada dua separuh '
         'hari beli. **L2** = jangkaan jika keluar ikut Chandelier. **Backtest** = purata setiap dagangan '
         '(Mxx set 431; Nxx tingkap tahan).', '']
    for kel, tajuk in (('M', 'Kaedah Mxx'), ('N', 'Kombinasi Nxx (masuk × keluar)')):
        L += [f'## {tajuk}', '',
              '| Kaedah | Kelas | Posisi/tutup | Hari beli | Jangkaan % | tanpa5 % | r3 | r5 | r10 | Lift 5 | A / B | L2 % | Hari-0 % | Backtest % | Sebab |',
              '|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|']
        for i, r in S[S.keluarga == kel].iterrows():
            bt = r.bt_purata if kel == 'M' else r.btn_tahan
            L.append(f"| `{i}` {str(r.nama)[:38]} | {r.kelas} | {int(r.n)}/{int(r.tutup)} | {int(r.hari_beli)} | "
                     f"{f(r.jangkaan)} | {f(r.tanpa5)} | {f(r.get('r3'))} | {f(r.get('r5'))} | {f(r.get('r10'))} | "
                     f"{f(r.get('lift5'))} | {f(r.get('lift5_A'))} / {f(r.get('lift5_B'))} | {f(r.l2_jangkaan)} | "
                     f"{f(r.hari0_pct, 0, False)} | {f(bt)} | {r.sebab_kelas} |")
        L.append('')
    open(os.path.join(HASIL, 'SEMUA_KAEDAH.md'), 'w', encoding='utf-8').write('\n'.join(L))
    open(os.path.join(HASIL, 'log.txt'), 'w', encoding='utf-8').write('\n'.join(LOG) + '\n')
    return 0


if __name__ == '__main__':
    sys.exit(main())
