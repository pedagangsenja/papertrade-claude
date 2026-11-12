"""Tinjauan (BUKAN pradaftar): henti tetap -8% x cara keluar x isyarat masuk.
Data: data_mentah/dataset_S1..S4 (431 saham, 2019-01..2026-10). Beli buka esok selepas isyarat.
Kos 0.5% pusingan. Ufuk maksimum 126 bar."""
import sys
import os
import numpy as np, pandas as pd
from numpy.lib.stride_tricks import sliding_window_view as swv

AKAR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))) + '/'
H = 126
KOS = 0.005
HENTI = float(sys.argv[1]) if len(sys.argv) > 1 else 0.08

d = pd.concat([pd.read_csv(AKAR + f'data_mentah/dataset_{s}.csv') for s in ('S1', 'S2', 'S3', 'S4')])
d = d.drop_duplicates(['ticker', 'date']).sort_values(['ticker', 'date'])
ix = pd.read_csv(AKAR + 'data_mentah/index_benchmark.csv')
q = ix[ix.ticker == 'QQQ'].sort_values('date').set_index('date').close
rejim = ((q > q.rolling(50).mean()) & (q.rolling(10).mean() > q.rolling(20).mean()))


def wilder(s, n):
    return s.ewm(alpha=1 / n, adjust=False, min_periods=n).mean()


def penunjuk(g):
    o, h, l, c, v = g.open, g.high, g.low, g.close, g.volume
    x = pd.DataFrame(index=g.index)
    pc = c.shift()
    tr = pd.concat([h - l, (h - pc).abs(), (l - pc).abs()], axis=1).max(axis=1)
    x['atr'] = wilder(tr, 14)
    dl = c.diff()
    for n in (2, 14):
        up, dn = wilder(dl.clip(lower=0), n), wilder((-dl).clip(lower=0), n)
        x[f'rsi{n}'] = 100 - 100 / (1 + up / dn.replace(0, np.nan))
    um, dm = h.diff(), -l.diff()
    pdm = pd.Series(np.where((um > dm) & (um > 0), um, 0.0), index=g.index)
    ndm = pd.Series(np.where((dm > um) & (dm > 0), dm, 0.0), index=g.index)
    pdi, ndi = 100 * wilder(pdm, 14) / x.atr, 100 * wilder(ndm, 14) / x.atr
    x['adx'] = wilder(100 * (pdi - ndi).abs() / (pdi + ndi).replace(0, np.nan), 14)
    for n in (20, 50, 150, 200):
        x[f'ma{n}'] = c.rolling(n).mean()
    x['ema21'] = c.ewm(span=21, adjust=False, min_periods=21).mean()
    macd = c.ewm(span=12, adjust=False).mean() - c.ewm(span=26, adjust=False).mean()
    x['macd'] = macd
    x['sig'] = macd.ewm(span=9, adjust=False).mean()
    x['hh20'] = h.rolling(20).max().shift()
    x['hh10'] = h.rolling(10).max().shift()
    x['julat10'] = ((h.rolling(10).max() - l.rolling(10).min()) / c).shift()
    x['h252'] = h.rolling(252).max()
    x['l252'] = l.rolling(252).min()
    x['vr'] = v / v.rolling(20).mean().shift()
    x['nilai20'] = (c * v).rolling(20).mean()
    return x


def isyarat(g, x):
    c = g.close
    templat = (c > x.ma50) & (x.ma50 > x.ma150) & (x.ma150 > x.ma200) & (x.ma200 > x.ma200.shift(20)) \
        & (c >= 0.75 * x.h252) & (c >= 1.3 * x.l252)
    s = {
        'ASAS setiap bar': pd.Series(True, index=g.index),
        'S1 pecah tinggi 20h + volum 1.5x': (c > x.hh20) & (x.vr >= 1.5) & (c > x.ma50),
        'S2 templat trend Minervini': templat,
        'S3 pullback RSI2<10 dalam trend naik': (c > x.ma200) & (x.ma50 > x.ma200) & (x.rsi2 < 10),
        'S4 pecah tapak ketat (ala VCP)': templat.shift().fillna(False) & (x.julat10 <= 0.10) & (c > x.hh10) & (x.vr >= 1.5),
        'S5 MACD silang naik atas MA200': (x.macd > x.sig) & (x.macd.shift() <= x.sig.shift()) & (c > x.ma200),
        'S6 tinggi 52 minggu baharu': (g.high >= x.h252) & (g.high.shift() < x.h252.shift()),
    }
    return s


def pertama(m):
    """indeks benar pertama setiap baris; H jika tiada"""
    k = m.argmax(axis=1)
    k[~m.any(axis=1)] = H
    return k


hasil = []
for tk, g in d.groupby('ticker', sort=False):
    g = g.reset_index(drop=True)
    T = len(g)
    if T < 252 + H + 5:
        continue
    x = penunjuk(g)
    S = isyarat(g, x)
    o, h, l, c = (g[k].to_numpy(float) for k in ('open', 'high', 'low', 'close'))
    e = np.arange(253, T - H - 1)            # bar masuk; isyarat pada e-1
    W = lambda a: swv(a, H)[e]
    O, Hh, L, C = W(o), W(h), W(l), W(c)
    NO = swv(o, H)[e + 1]                    # buka bar seterusnya
    P = o[e][:, None]
    kk = np.arange(H)[None, :]
    A = lambda nm: W(x[nm].to_numpy(float))
    cmax = np.maximum.accumulate(C, axis=1)
    cmax_dulu = np.concatenate([np.full((len(e), 1), -np.inf), cmax[:, :-1]], axis=1)
    chand = lambda m: C < np.maximum.accumulate(cmax - m * A('atr'), axis=1)
    bwh50 = C < A('ma50')
    dua50 = bwh50.copy(); dua50[:, 1:] &= bwh50[:, :-1]; dua50[:, 0] = False
    masa = lambda n: np.broadcast_to(kk == n - 1, C.shape)
    kosong = np.zeros_like(C, bool)

    def laksana(sig, henti=None, sasaran=None):
        """sig: syarat pada tutup -> jual buka esok. henti: matriks paras. sasaran: pecahan."""
        sig = sig.copy(); sig[:, H - 1] = True
        ks = pertama(sig)
        t = 4 * ks + 4
        px = np.take_along_axis(NO, ks[:, None], 1)[:, 0]
        jenis = np.zeros(len(e), int)
        if henti is not None:
            kh = pertama(L <= henti)
            ada = kh < H
            khc = np.minimum(kh, H - 1)[:, None]
            pxh = np.minimum(np.take_along_axis(O, khc, 1), np.take_along_axis(henti, khc, 1))[:, 0]
            th = np.where(ada, 4 * kh + 1, 10 ** 9)
            g_ = th < t
            t, px, jenis = np.where(g_, th, t), np.where(g_, pxh, px), np.where(g_, 1, jenis)
        if sasaran is not None:
            ps = P * (1 + sasaran)
            kt = pertama(Hh >= ps)
            ada = kt < H
            ktc = np.minimum(kt, H - 1)[:, None]
            pxt = np.maximum(np.take_along_axis(O, ktc, 1)[:, 0], ps[:, 0])
            tt = np.where(ada, 4 * kt + 2, 10 ** 9)
            g_ = tt < t
            t, px, jenis = np.where(g_, tt, t), np.where(g_, pxt, px), np.where(g_, 2, jenis)
        return px / P[:, 0] - 1 - KOS, t // 4 + 1, jenis

    h8 = np.broadcast_to(P * (1 - HENTI), C.shape)
    hbe = np.where(cmax_dulu >= P * (1 + HENTI), P, P * (1 - HENTI))
    K = {
        'pegang 126 hari (rujukan)': (kosong, None, None),
        'henti sahaja': (kosong, h8, None),
        'Chandelier 4xATR TANPA henti (lorong 2 kini)': (chand(4), None, None),
        'henti + Chandelier 4xATR': (chand(4), h8, None),
        'henti + Chandelier 3xATR': (chand(3), h8, None),
        'henti -> pulang modal selepas +henti, + Chandelier 4x': (chand(4), hbe, None),
        'RSI14>70 TANPA henti (X13)': (A('rsi14') > 70, None, None),
        'henti + RSI14>70': (A('rsi14') > 70, h8, None),
        'henti + ADX<20': (A('adx') < 20, h8, None),
        'henti + dua tutup bawah MA50': (dua50, h8, None),
        'henti + tutup bawah EMA21': (C < A('ema21'), h8, None),
        'henti + MACD silang turun': (A('macd') < A('sig'), h8, None),
        'henti + ekori 8% dari tutup tertinggi': (C < 0.92 * cmax, h8, None),
        'henti + sasaran 2R': (kosong, h8, 2 * HENTI),
        'henti + sasaran 3R': (kosong, h8, 3 * HENTI),
        'henti + masa 10 hari': (masa(10), h8, None),
        'henti + masa 20 hari': (masa(20), h8, None),
    }
    tar = g.date.to_numpy()[e - 1]
    ok = (x.nilai20.to_numpy()[e - 1] >= 1e5)
    rj = rejim.reindex(tar).fillna(False).to_numpy()
    for kn, (sg, ht, ss) in K.items():
        r, hari, jenis = laksana(sg, ht, ss)
        for sn, sv in S.items():
            m = sv.to_numpy(bool)[e - 1] & ok
            if m.any():
                hasil.append(pd.DataFrame({'masuk': sn, 'keluar': kn, 'tarikh': tar[m], 'r': r[m], 'hari': hari[m],
                                           'henti': jenis[m] == 1, 'on': rj[m]}))

R = pd.concat(hasil, ignore_index=True)
R['tempoh'] = np.where(R.tarikh < 20230101, 'A 2020-22', 'B 2023-26')
R.to_pickle(f'keluar8_{int(HENTI*100)}.pkl')


def ring(z):
    w, k = z.r[z.r > 0], z.r[z.r <= 0]
    return pd.Series({'n': len(z), 'jangkaan%': z.r.mean() * 100, 'menang%': (z.r > 0).mean() * 100,
                      'p.menang%': w.mean() * 100, 'p.rugi%': k.mean() * 100, 'hari': z.hari.mean(),
                      '%/hari': z.r.mean() * 100 / z.hari.mean(), 'kena henti%': z.henti.mean() * 100})


pd.set_option('display.width', 250, 'display.max_rows', 500, 'display.max_colwidth', 60)
print('tarikh', R.tarikh.min(), R.tarikh.max(), 'HENTI', HENTI)
a = R[R.masuk == 'ASAS setiap bar']
print('\n== ASAS (beli setiap bar), semua tempoh ==')
print(a.groupby('keluar').apply(ring).sort_values('%/hari', ascending=False).round(2))
print('\n== ASAS: jangkaan% dan %/hari ikut tempoh dan rejim ==')
t = a.groupby(['keluar', 'tempoh']).apply(ring)[['jangkaan%', '%/hari']].unstack().round(3)
t2 = a.groupby(['keluar', 'on']).apply(ring)[['jangkaan%', '%/hari']].unstack().round(3)
print(pd.concat([t, t2], axis=1))
print('\n== LIFT isyarat atas ASAS pada keluar sama (jangkaan%, mata) ==')
b = R.groupby(['masuk', 'keluar', 'tempoh']).r.mean().mul(100).unstack('tempoh')
base = b.loc['ASAS setiap bar']
lift = (b - base.reindex(b.index.get_level_values('keluar')).to_numpy()).round(2)
n = R.groupby(['masuk', 'keluar']).size()
for kn in ['henti sahaja', 'henti + Chandelier 4xATR', 'henti + RSI14>70', 'henti + dua tutup bawah MA50', 'henti + masa 20 hari']:
    x_ = lift.xs(kn, level='keluar').copy(); x_['n'] = n.xs(kn, level='keluar')
    x_['jangkaan A'] = b.xs(kn, level='keluar')['A 2020-22'].round(2); x_['jangkaan B'] = b.xs(kn, level='keluar')['B 2023-26'].round(2)
    print('\n--', kn); print(x_)
