# statistik.py — statistik kajian PIT (pra-daftar PRA_DAFTAR.md §5–§7): t berkelompok ikut bulan, DSR, PBO (CSCV),
# penanda aras belian rawak tempoh sama, CAGR/MDD. Tiada pandang hadapan: semua fungsi menerima data yang sudah dibina.
import math
from itertools import combinations
from statistics import NormalDist

import numpy as np
import pandas as pd

_N = NormalDist()
GAMMA = 0.5772156649015329


def cagr(s):
    s = pd.Series(s).dropna()
    if len(s) < 2 or s.iloc[0] <= 0: return float('nan')
    y = (s.index[-1] - s.index[0]).days / 365.25
    if y <= 0 or s.iloc[-1] <= 0: return float('nan') if y <= 0 else -1.0
    return float((s.iloc[-1] / s.iloc[0]) ** (1 / y) - 1)


def mdd(s):
    s = pd.Series(s).dropna()
    return float((s / s.cummax() - 1).min()) if len(s) else float('nan')


def t_berkelompok(x, kelompok):
    """Purata x dan t dengan SE berkelompok CR1: SE^2 = G/(G-1) * sum_g (sum_{k in g} (x_k - xbar))^2 / n^2.
    Pulang dict(purata, se, t, n, G). G < 2 -> se/t = NaN."""
    x = np.asarray(x, float); k = np.asarray(kelompok)
    ok = ~np.isnan(x); x = x[ok]; k = k[ok]; n = len(x)
    if n == 0: return dict(purata=float('nan'), se=float('nan'), t=float('nan'), n=0, G=0)
    m = float(x.mean()); e = pd.Series(x - m).groupby(k).sum().values; G = len(e)
    if G < 2: return dict(purata=m, se=float('nan'), t=float('nan'), n=n, G=G)
    se = math.sqrt(G / (G - 1) * float((e ** 2).sum())) / n
    return dict(purata=m, se=se, t=(m / se if se > 0 else float('nan')), n=n, G=G)


def sr0(V, N):
    """Jangkaan SR maksimum di bawah hipotesis nol bagi N percubaan bebas dengan varians SR = V (Bailey & Lopez de Prado)."""
    if N < 2 or not V > 0: return 0.0
    return math.sqrt(V) * ((1 - GAMMA) * _N.inv_cdf(1 - 1 / N) + GAMMA * _N.inv_cdf(1 - 1 / (N * math.e)))


def dsr(r, s0):
    """Deflated Sharpe Ratio siri pulangan r (per tempoh) lawan ambang s0 (unit per tempoh yang sama)."""
    r = pd.Series(r).dropna(); T = len(r)
    if T < 3 or not r.std() > 0: return float('nan')
    sr = r.mean() / r.std(); sk = float(r.skew()); ku = float(r.kurt()) + 3.0
    dd = math.sqrt(max(1e-12, 1 - sk * sr + (ku - 1) / 4 * sr ** 2))
    return float(_N.cdf((sr - s0) * math.sqrt(T - 1) / dd))


def sharpe(r):
    r = pd.Series(r).dropna()
    return float(r.mean() / r.std()) if len(r) > 2 and r.std() > 0 else float('nan')


def pbo_cscv(R, S=16):
    """PBO (Bailey, Borwein, Lopez de Prado & Zhu 2017) dengan CSCV: R = ndarray T x K pulangan (lajur = calon).
    S blok bersebelahan; setiap gabungan S/2 blok = dalam sampel, selebihnya luar sampel; ukuran = Sharpe.
    Pulang dict(pbo, n_gabungan, logit_median). K < 2 -> pbo NaN."""
    R = np.asarray(R, float); T, K = R.shape
    if K < 2 or T < S * 2: return dict(pbo=float('nan'), n_gabungan=0, logit_median=float('nan'))
    R = np.nan_to_num(R, nan=0.0)
    b = np.array_split(np.arange(T), S)
    s1 = np.array([R[i].sum(axis=0) for i in b]); s2 = np.array([(R[i] ** 2).sum(axis=0) for i in b])
    nb = np.array([len(i) for i in b], float)
    lam = []
    semua = np.arange(S)
    for c in combinations(range(S), S // 2):
        ins = np.array(c); oos = np.setdiff1d(semua, ins)
        def _sr(ix):
            n = nb[ix].sum(); m = s1[ix].sum(axis=0) / n; v = s2[ix].sum(axis=0) / n - m ** 2
            return m / np.sqrt(np.where(v > 0, v, np.nan))
        a, o = _sr(ins), _sr(oos)
        a = np.nan_to_num(a, nan=-np.inf); o = np.nan_to_num(o, nan=-np.inf)
        best = int(np.argmax(a))
        w = (pd.Series(o).rank(method='average').iloc[best]) / (K + 1)
        lam.append(math.log(w / (1 - w)))
    lam = np.array(lam)
    return dict(pbo=float((lam <= 0).mean()), n_gabungan=len(lam), logit_median=float(np.median(lam)))


def rawak(T, O, Cf, E, tarikh, benih=range(20), kos=0.0025):
    """Penanda aras belian rawak tempoh sama (pra-daftar §5).
    T: DataFrame dagangan (lajur sig, ent, ex, jenis). O, Cf: ndarray (tarikh x ticker) buka dan tutup ffill.
    E: ndarray bool (tarikh x ticker) alam layak pada hari isyarat. tarikh: DatetimeIndex baris O/Cf/E.
    Setiap benih memilih seragam satu ticker layak pada hari isyarat yang mempunyai buka pada hari masuk; jual pada buka
    hari keluar jika jenis == 'buka' (tiada buka -> tutup terakhir <= hari keluar), selain itu tutup terakhir <= hari keluar.
    Pulang ndarray (len(T),) purata pulangan rawak merentas benih (NaN jika tiada calon)."""
    if len(T) == 0: return np.array([])
    pos = pd.Series(np.arange(len(tarikh)), index=tarikh)
    ds = pos.reindex(pd.DatetimeIndex(T.sig)).values; de = pos.reindex(pd.DatetimeIndex(T.ent)).values
    dx = pos.reindex(pd.DatetimeIndex(T.ex)).values; buka = (T.jenis.values == 'buka')
    benih = list(benih); hasil = np.full((len(T), len(benih)), np.nan)
    df = pd.DataFrame({'ds': ds, 'de': de, 'baris': np.arange(len(T))}).dropna()
    for (s, e), kump in df.groupby(['ds', 'de']):
        s, e = int(s), int(e)
        calon = np.flatnonzero(E[s] & ~np.isnan(O[e]))
        if len(calon) == 0: continue
        rows = kump.baris.values.astype(int)
        for bi, b in enumerate(benih):
            rng = np.random.default_rng([int(b), s, e])
            pilih = calon[rng.integers(0, len(calon), size=len(rows))]
            x = dx[rows].astype(int)
            px = np.where(buka[rows], O[x, pilih], np.nan)
            px = np.where(np.isnan(px), Cf[x, pilih], px)
            hasil[rows, bi] = px / O[e, pilih] * (1 - kos) / (1 + kos) - 1
    return np.nanmean(hasil, axis=1) if len(benih) else np.full(len(T), np.nan)
