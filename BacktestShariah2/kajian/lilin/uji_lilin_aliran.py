"""Ujian 5: adakah corak lilin pembalikan dalam aliran naik menambah nilai berbanding persediaan
aliran/tarikan balik yang SAMA tanpa lilin? Data AUTOTUNE 2000 saham AS (dibaca sahaja).

Reka bentuk ditetapkan sebelum keputusan dilihat; lihat
`kajian/research_notes/Ujian lilin atas 2000 saham/lilin_dalam_aliran.md`.

Ringkasan:
- S0 (hari isyarat t, dikira pada tutup t, beli buka t+1): tutup > SMA50 > SMA200; proksi RS (persentil pulangan
  126 bar antara semua saham universe hari itu, A+B) >= 80; tarikan balik = >= 3 tutup lebih rendah dalam 5 perubahan
  harian berakhir t atau t-1, atau RSI2 < 10 pada t atau t-1. Saham mesti dalam universe bulan t dan kumpulan sampel.
- Varian lilin = S0 dan corak lilin pada t (subset tepat S0), dengan/tanpa volum >= 1.5x median 20 bar sebelumnya.
- Keluar: (a) Chandelier tutup 4xATR14 (keluar_lorong.lorong_henti) dengan had 60 hari; (b) pegang 10 hari.
  Kos sisi = enjin_at.kos_sisi (0.1% + slippage ikut median nilai 20 hari pada hari isyarat).
- Sampel: PILIH (A, 2013-2021), SAH-B (B, 2013-2021), SAH-22 (A+B, 2022-akhir).
- Metrik peringkat isyarat (setiap isyarat = satu dagangan), t berkelompok ikut tarikh beli, kawalan rawak, semakan
  konvensyen enjin (satu posisi setiap saham), dan portfolio 8 slot x 12.5% (enjin_at.Pasaran, rank = proksi RS).

Larian: python3 BacktestShariah2/kajian/lilin/uji_lilin_aliran.py [--keluar DIR]
Output (lalai DIR = scratchpad/lilin): hasil.json, isyarat.parquet, ringkasan.txt.
Tiada fail di luar DIR ditulis.
"""
import argparse
import json
import sys
import time
from pathlib import Path

import numpy as np
import pandas as pd
from numba import njit

AKAR = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(AKAR / 'AUTOTUNE'))
from teras.enjin_at import kos_sisi, Pasaran  # noqa: E402
from teras.objektif import cagr, mdd  # noqa: E402

CACHE = AKAR / 'AUTOTUNE' / '.cache'
LALAI_KELUAR = Path('/tmp/claude-0/-home-user-papertrade-claude/0793050f-2ee1-522e-9bf0-b633a13089db/scratchpad/lilin')
SAMPEL = {'PILIH': ('A', '2013-01-01', '2021-12-31'),
          'SAH-B': ('B', '2013-01-01', '2021-12-31'),
          'SAH-22': ('AB', '2022-01-01', None)}
VARIAN = {'V00_S0': 'S0', 'V01_engulf': 'engulf', 'V02_piercing': 'pierce', 'V03_hammer': 'hammer',
          'V04_3LS': 'tls', 'V05_HAflip': 'ha', 'V06_IBbreak': 'ib',
          'V07_engulf_vol': 'engulf+vol', 'V08_piercing_vol': 'pierce+vol', 'V09_hammer_vol': 'hammer+vol',
          'V10_3LS_vol': 'tls+vol', 'V11_IBbreak_vol': 'ib+vol'}
KELUAR = {'chandelier': 0, 'pegang10': 1}
N_RAWAK = 1000
BENIH = 20261022


# ------------------------------------------------------------------ penunjuk (numba, ikut segmen saham)
@njit(cache=True)
def _sma(x, mula, akhir, w):
    out = np.full(len(x), np.nan)
    for q in range(len(mula)):
        s, e = mula[q], akhir[q]
        acc = 0.0
        for i in range(s, e):
            acc += x[i]
            if i - s >= w:
                acc -= x[i - w]
            if i - s >= w - 1:
                out[i] = acc / w
    return out


@njit(cache=True)
def _med_gulung(x, mula, akhir, w, sebelum):
    """Median gulung w bar; sebelum=True -> bar i-w..i-1 (tanpa i), selain itu i-w+1..i."""
    out = np.full(len(x), np.nan)
    buf = np.empty(w)
    for q in range(len(mula)):
        s, e = mula[q], akhir[q]
        for i in range(s, e):
            hujung = i - 1 if sebelum else i
            if hujung - s < w - 1:
                continue
            for k in range(w):
                buf[k] = x[hujung - w + 1 + k]
            out[i] = np.median(buf)
    return out


@njit(cache=True)
def _rsi(c, mula, akhir, n):
    """Sama seperti enjin.rsi: EWM alfa 1/n, adjust=False, bermula pada diff pertama."""
    out = np.full(len(c), np.nan)
    a = 1.0 / n
    for q in range(len(mula)):
        s, e = mula[q], akhir[q]
        au = np.nan; ad = np.nan
        for i in range(s + 1, e):
            d = c[i] - c[i - 1]
            up = d if d > 0 else 0.0
            dn = -d if d < 0 else 0.0
            if np.isnan(au):
                au = up; ad = dn
            else:
                au = (1 - a) * au + a * up
                ad = (1 - a) * ad + a * dn
            if ad == 0.0:
                out[i] = 100.0 if au > 0 else np.nan
            else:
                out[i] = 100 - 100 / (1 + au / ad)
    return out


@njit(cache=True)
def _atr(h, l, c, mula, akhir, n):
    """Sama seperti enjin.atr: purata mudah julat sebenar n bar (bar pertama = tinggi - rendah)."""
    out = np.full(len(c), np.nan)
    for q in range(len(mula)):
        s, e = mula[q], akhir[q]
        acc = 0.0
        tr = np.empty(e - s)
        for i in range(s, e):
            if i == s:
                t = h[i] - l[i]
            else:
                t = max(h[i] - l[i], abs(h[i] - c[i - 1]), abs(l[i] - c[i - 1]))
            tr[i - s] = t
            acc += t
            if i - s >= n:
                acc -= tr[i - s - n]
            if i - s >= n - 1:
                out[i] = acc / n
    return out


@njit(cache=True)
def _ha_hijau(o, h, l, c, mula, akhir):
    out = np.zeros(len(c), np.bool_)
    for q in range(len(mula)):
        s, e = mula[q], akhir[q]
        ho = (o[s] + c[s]) / 2
        hc = (o[s] + h[s] + l[s] + c[s]) / 4
        out[s] = hc > ho
        for i in range(s + 1, e):
            ho = (ho + hc) / 2
            hc = (o[i] + h[i] + l[i] + c[i]) / 4
            out[i] = hc > ho
    return out


@njit(cache=True)
def _anjak(x, mula, akhir, k):
    """x[i-k] dalam segmen yang sama; NaN jika tiada."""
    out = np.full(len(x), np.nan)
    for q in range(len(mula)):
        s, e = mula[q], akhir[q]
        for i in range(s + k, e):
            out[i] = x[i - k]
    return out


# ------------------------------------------------------------------ simulasi dagangan
@njit(cache=True)
def _simulasi(o, h, l, c, atr, sig_row, n_end, jenis, tmax):
    """Setiap isyarat (baris r) -> masuk buka r+1. jenis 0 = Chandelier tutup 4xATR14 + had tmax (j - r >= tmax ->
    tutup j); jenis 1 = pegang tetap tmax (tutup r+tmax). n_end[k] = indeks selepas bar terakhir tetingkap saham.
    Pulang (baris keluar, harga keluar, 1 jika keluar pada buka, sebab 0 hujung/3 isyarat/4 masa)."""
    m = len(sig_row)
    xr = np.empty(m, np.int64); xp = np.empty(m); xb = np.zeros(m, np.int64); why = np.empty(m, np.int64)
    for k in range(m):
        r = sig_row[k]; n = n_end[k]
        puncak = -np.inf; paras = -np.inf
        jumpa = False
        j = r + 1
        while j < n:
            if jenis == 0:
                if c[j] > puncak:
                    puncak = c[j]
                if not np.isnan(atr[j]):
                    v = puncak - 4.0 * atr[j]
                    if v > paras:
                        paras = v
                if c[j] < paras and j + 1 < n:
                    xr[k] = j + 1; xp[k] = o[j + 1]; xb[k] = 1; why[k] = 3; jumpa = True; break
            if (j - r) >= tmax:
                xr[k] = j; xp[k] = c[j]; why[k] = 4; jumpa = True; break
            j += 1
        if not jumpa:
            xr[k] = n - 1; xp[k] = c[n - 1]; why[k] = 0
    return xr, xp, xb, why


# ------------------------------------------------------------------ statistik
def t_kelompok(x, g):
    """Min dan t (SE berkelompok CR1) bagi x dengan kelompok g."""
    x = np.asarray(x, float); n = len(x)
    if n < 2: return float(np.mean(x)) if n else np.nan, np.nan
    u = x - x.mean()
    s = pd.Series(u).groupby(np.asarray(g)).sum().values
    G = len(s)
    if G < 2: return float(x.mean()), np.nan
    se = np.sqrt((s ** 2).sum() * G / (G - 1)) / n
    return float(x.mean()), float(x.mean() / se) if se > 0 else np.nan


def regresi_kelompok(y, d, g):
    """y = a + b d; pulang (b, t_b) dengan SE berkelompok CR1."""
    y = np.asarray(y, float); d = np.asarray(d, float)
    X = np.column_stack([np.ones(len(y)), d])
    XtX = X.T @ X
    if np.linalg.matrix_rank(XtX) < 2: return np.nan, np.nan
    iv = np.linalg.inv(XtX)
    b = iv @ X.T @ y
    u = y - X @ b
    sk = pd.DataFrame(X * u[:, None]).groupby(np.asarray(g)).sum().values
    G = len(sk); N = len(y)
    V = iv @ (sk.T @ sk) @ iv * G / (G - 1) * (N - 1) / (N - 2)
    return float(b[1]), float(b[1] / np.sqrt(V[1, 1]))


def metrik(T):
    if len(T) == 0:
        return dict(n=0, hari_beli=0)
    mx, tx = t_kelompok(T.lebih.values, T.ent.values)
    return dict(n=int(len(T)), hari_beli=int(T.ent.nunique()),
                min_ret=float(T.ret.mean() * 100), median_ret=float(T.ret.median() * 100),
                menang=float((T.ret > 0).mean() * 100), p5=float(np.percentile(T.ret, 5) * 100),
                min_lebih=float(mx * 100), t_lebih=tx, median_lebih=float(T.lebih.median() * 100),
                hari=float(T.days.mean()))


def enjin_konvensyen(T):
    """Satu posisi setiap saham (seperti enjin): isyarat seterusnya mesti >= baris keluar + 1."""
    T = T.sort_values(['ticker', 'sig_row'])
    simpan = np.zeros(len(T), bool)
    tk = T.ticker.values; sr = T.sig_row.values; xr = T.ex_row.values
    akhir = {}
    for k in range(len(T)):
        if sr[k] >= akhir.get(tk[k], -1):
            simpan[k] = True; akhir[tk[k]] = xr[k] + 1
    return T[simpan]


# ------------------------------------------------------------------ utama
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--keluar', default=str(LALAI_KELUAR))
    a = ap.parse_args()
    out = Path(a.keluar); out.mkdir(parents=True, exist_ok=True)
    t0 = time.time()

    univ = pd.read_parquet(CACHE / 'universe.parquet')
    tick = sorted(univ.ticker.unique())
    kump = univ.drop_duplicates('ticker').set_index('ticker').kumpulan
    bahagian = [pd.read_parquet(CACHE / f'harga_{y}.parquet', filters=[('ticker', 'in', tick)]) for y in range(2009, 2027)]
    df = pd.concat(bahagian, ignore_index=True); del bahagian
    df = df.sort_values(['ticker', 'date'], kind='mergesort').reset_index(drop=True)
    print('baris', len(df), 'saham', df.ticker.nunique(), f'{time.time() - t0:.0f}s', flush=True)

    o, h, l, c = (df[k].to_numpy(np.float64) for k in ('open', 'high', 'low', 'close'))
    v = df['volume'].to_numpy(np.float64)
    tcode, tnama = pd.factorize(df.ticker, sort=True)
    seg = np.r_[0, np.flatnonzero(np.diff(tcode)) + 1]
    mula = seg.astype(np.int64); akhir = np.r_[seg[1:], len(df)].astype(np.int64)
    tarikh = df.date.to_numpy()
    ym = (df.date.dt.year * 100 + df.date.dt.month).to_numpy()
    tarikh_akhir = pd.Timestamp(df.date.max())
    del df

    sma50 = _sma(c, mula, akhir, 50); sma200 = _sma(c, mula, akhir, 200)
    atr = _atr(h, l, c, mula, akhir, 14)
    rsi2 = _rsi(c, mula, akhir, 2)
    medv = _med_gulung(c * v, mula, akhir, 20, False)       # = enjin_at.medv_bersambung
    medvol = _med_gulung(v, mula, akhir, 20, True)          # median volum t-20..t-1
    c1, c2, c3, c4, c5 = (_anjak(c, mula, akhir, k) for k in (1, 2, 3, 4, 5))
    o1, o3 = _anjak(o, mula, akhir, 1), _anjak(o, mula, akhir, 3)
    h1, h2 = _anjak(h, mula, akhir, 1), _anjak(h, mula, akhir, 2)
    l1, l2 = _anjak(l, mula, akhir, 1), _anjak(l, mula, akhir, 2)
    c126 = _anjak(c, mula, akhir, 126)
    rsi2_1 = _anjak(rsi2, mula, akhir, 1)
    ha = _ha_hijau(o, h, l, c, mula, akhir)
    ha1 = _anjak(ha.astype(float), mula, akhir, 1)

    # universe titik masa + kumpulan
    ukod = pd.Index(tnama).get_indexer(univ.ticker.values).astype(np.int64)
    uym = (univ.bulan.str[:4].astype(int) * 100 + univ.bulan.str[5:7].astype(int)).values.astype(np.int64)
    dalam_u = np.isin(tcode.astype(np.int64) * 1000000 + ym.astype(np.int64), ukod[ukod >= 0] * 1000000 + uym[ukod >= 0])
    kumpulan = kump.reindex(tnama).values[tcode]
    print('penunjuk siap', f'{time.time() - t0:.0f}s', flush=True)

    # proksi RS: persentil pulangan 126 bar antara saham universe (A+B) hari itu
    r126 = c / c126 - 1
    sah = dalam_u & np.isfinite(r126)
    rs = np.full(len(c), np.nan)
    rs[sah] = pd.Series(r126[sah]).groupby(tarikh[sah]).rank(pct=True).values * 100

    # tarikan balik
    dn = np.nan_to_num((c < c1).astype(float) * np.isfinite(c1))
    dn1 = np.nan_to_num(_anjak(dn, mula, akhir, 1)); dn2 = np.nan_to_num(_anjak(dn, mula, akhir, 2))
    dn3 = np.nan_to_num(_anjak(dn, mula, akhir, 3)); dn4 = np.nan_to_num(_anjak(dn, mula, akhir, 4))
    dn5 = np.nan_to_num(_anjak(dn, mula, akhir, 5))
    L5 = (dn + dn1 + dn2 + dn3 + dn4) >= 3
    L5_1 = (dn1 + dn2 + dn3 + dn4 + dn5) >= 3
    with np.errstate(invalid='ignore'):
        pb = L5 | L5_1 | (rsi2 < 10) | (rsi2_1 < 10)
        aliran = (c > sma50) & (sma50 > sma200)
        S0 = aliran & (rs >= 80) & pb & dalam_u
        body = c - o
        merah1 = c1 < o1
        engulf = merah1 & (c > o) & (o <= c1) & (c >= o1) & (body >= 0.6 * atr)
        pierce = merah1 & (o < l1) & (c > (o1 + c1) / 2) & (c < o1)
        rng = h - l
        bb = np.minimum(o, c) - l
        hammer = (rng > 0) & (bb >= 2 * np.abs(body)) & ((c - l) >= rng * 2 / 3)
        tls = (c3 < c4) & (c2 < c3) & (c1 < c2) & (c > o3)
        hav = ha & (ha1 == 0)
        ib = (h1 <= h2) & (l1 >= l2) & (c > h1)
        vol = v >= 1.5 * medvol
    corak = {'S0': np.ones(len(c), bool), 'engulf': engulf, 'pierce': pierce, 'hammer': hammer, 'tls': tls,
             'ha': hav, 'ib': ib}
    tanda = {}
    for nm, kod in VARIAN.items():
        b, _, vv = kod.partition('+')
        m = S0 & corak[b]
        if vv: m = m & vol
        tanda[nm] = m
    del (sma50, sma200, rsi2, medvol, c1, c2, c3, c4, c5, o1, o3, h1, h2, l1, l2, c126, rsi2_1, ha, ha1, r126, sah,
         dn, dn1, dn2, dn3, dn4, dn5, L5, L5_1, pb, aliran, body, merah1, engulf, pierce, rng, bb, hammer, tls, hav, ib,
         vol, corak, v, ym)

    # SPY
    ix = pd.read_parquet(CACHE / 'idx.parquet')
    spy = ix[ix.ticker == 'SPY'].sort_values('date').set_index('date')
    spy_o = spy.open.astype(float); spy_c = spy.close.astype(float)
    kos = kos_sisi(medv)

    hasil = {'meta': dict(baris=int(len(c)), saham=int(len(tnama)), tarikh_akhir=str(tarikh_akhir.date()),
                          isyarat_S0_semua=int(S0.sum()))}
    rng_gen = np.random.default_rng(BENIH)
    simpan_isyarat = []
    tik_arr = tnama.values if hasattr(tnama, 'values') else np.asarray(tnama)

    for snm, (kp, m0, m1) in SAMPEL.items():
        m0 = pd.Timestamp(m0); m1 = pd.Timestamp(m1) if m1 else tarikh_akhir
        # n_end setiap saham: indeks selepas bar terakhir <= m1
        n_end_seg = np.array([s + np.searchsorted(tarikh[s:e], np.datetime64(m1), 'right')
                              for s, e in zip(mula, akhir)], np.int64)
        dlm_kp = np.isin(kumpulan, list(kp))
        ne_row = n_end_seg[tcode]
        rows = np.flatnonzero(S0 & dlm_kp)
        rows = rows[(rows + 1 < ne_row[rows])]
        rows = rows[tcode[rows + 1] == tcode[rows]]
        ent_d = tarikh[rows + 1]
        rows = rows[(ent_d >= np.datetime64(m0))]
        print(snm, 'isyarat S0', len(rows), f'{time.time() - t0:.0f}s', flush=True)
        pas = None
        hasil[snm] = {}
        for knm, jenis in KELUAR.items():
            tmax = 60 if jenis == 0 else 10
            xr, xp, xb, why = _simulasi(o, h, l, c, atr, rows.astype(np.int64), ne_row[rows], jenis, tmax)
            e = o[rows + 1]; k = kos[rows]
            ret = xp / e * (1 - k) / (1 + k) - 1
            ent = pd.DatetimeIndex(tarikh[rows + 1]); ex = pd.DatetimeIndex(tarikh[xr])
            so = spy_o.reindex(ent).values
            sx = np.where(xb == 1, spy_o.reindex(ex).values, spy_c.reindex(ex).values)
            T = pd.DataFrame(dict(ticker=tik_arr[tcode[rows]], sig_row=rows, ex_row=xr, sig=tarikh[rows], ent=ent, ex=ex,
                                  ret=ret, spy=sx / so - 1, days=xr - rows, why=why, rank=rs[rows]))
            T['lebih'] = T.ret - T.spy
            for nm in VARIAN:
                T[nm] = tanda[nm][rows]
            hilang = int(T.spy.isna().sum())
            T = T[T.spy.notna()].reset_index(drop=True)
            simpan_isyarat.append(T.assign(sampel=snm, keluar=knm))
            if pas is None:
                fr = {t: pd.DataFrame({'close': c[s:e]}, index=pd.DatetimeIndex(tarikh[s:e]))
                      for t, s, e in zip(tik_arr, mula, akhir) if kump.get(t) in kp}
                pas = Pasaran(fr, m0, m1); del fr
                spy_cv = spy_c[(spy_c.index >= m0) & (spy_c.index <= m1)]
                spy_cv = spy_cv / spy_o[spy_cv.index[0]]
                hasil[snm]['SPY'] = dict(cagr=cagr(spy_cv) * 100, mdd=mdd(spy_cv) * 100)
            base = T[T['V00_S0']]
            mS0 = metrik(base)
            R = {'_spy_hilang': hilang}
            for nm in VARIAN:
                Tv = T[T[nm]]
                M = metrik(Tv)
                Mc = metrik(enjin_konvensyen(Tv))
                M['enjin'] = {kk: Mc.get(kk) for kk in ('n', 'hari_beli', 'min_ret', 'min_lebih', 't_lebih', 'p5', 'menang')}
                cv = pas.lengkung(Tv[['ticker', 'ent', 'ex', 'ret', 'rank']])
                M['port_cagr'] = cagr(cv) * 100; M['port_mdd'] = mdd(cv) * 100
                if nm != 'V00_S0' and M['n'] > 0:
                    b, tb = regresi_kelompok(T.lebih.values, T[nm].values.astype(float), T.ent.values)
                    M['beza_lebih'] = M['min_lebih'] - mS0['min_lebih']
                    M['b_lilin_vs_bukan'] = b * 100; M['t_beza'] = tb
                    M['beza_p5'] = M['p5'] - mS0['p5']
                    K = M['n']; xs = base.lebih.values
                    if K < len(xs):
                        mr = np.array([xs[rng_gen.choice(len(xs), K, replace=False)].mean() for _ in range(N_RAWAK)]) * 100
                        M['rawak'] = dict(min=float(mr.mean()), lo=float(np.percentile(mr, 2.5)),
                                          hi=float(np.percentile(mr, 97.5)),
                                          p_emp=float((mr >= M['min_lebih']).mean()))
                R[nm] = M
            hasil[snm][knm] = R
            print(snm, knm, 'siap', f'{time.time() - t0:.0f}s', flush=True)
        del pas

    # peraturan lulus
    lulus = {}
    for knm in KELUAR:
        for nm in VARIAN:
            if nm == 'V00_S0': continue
            sebab = []
            for snm in SAMPEL:
                M = hasil[snm][knm][nm]; B = hasil[snm][knm]['V00_S0']
                if M.get('n', 0) == 0: sebab.append(f'{snm}: tiada isyarat'); continue
                if not M['min_lebih'] > B['min_lebih']: sebab.append(f'{snm}: min lebihan tidak > S0')
                if M['hari_beli'] < 10: sebab.append(f'{snm}: hari beli < 10')
                if M['p5'] < B['p5'] - 1: sebab.append(f'{snm}: p5 lebih buruk > 1 mata')
            tP = hasil['PILIH'][knm][nm].get('t_beza')
            if not (tP is not None and np.isfinite(tP) and tP > 3): sebab.append(f'PILIH: t beza = {tP}')
            lulus[f'{nm}|{knm}'] = dict(lulus=not sebab, sebab=sebab)
    hasil['lulus'] = lulus

    (out / 'hasil.json').write_text(json.dumps(hasil, indent=1, default=float))
    pd.concat(simpan_isyarat).drop(columns=['sig_row', 'ex_row']).to_parquet(out / 'isyarat.parquet')
    print('selesai', f'{time.time() - t0:.0f}s')


if __name__ == '__main__':
    main()
