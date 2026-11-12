"""Tinjauan besar (BUKAN pradaftar): isyarat masuk x hasil x cara pegang/keluar.
Guna: python3 panel.py <mentah|stor> <fail_keluar.pkl>
Isyarat dikira pada TUTUP bar i (data <= i sahaja). Beli pada BUKA bar i+1. Kos 0.5% pusingan."""
import sys
import os
import numpy as np, pandas as pd
from numpy.lib.stride_tricks import sliding_window_view as swv

AKAR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))) + '/'
SUMBER, KELUAR = sys.argv[1], sys.argv[2]
H = 126 if SUMBER == 'mentah' else 60
HR = 60                      # tingkap perlumbaan sasaran lawan henti
KOS, HENTI = 0.005, 0.08

if SUMBER == 'mentah':
    d = pd.concat([pd.read_csv(AKAR + f'data_mentah/dataset_{s}.csv') for s in ('S1', 'S2', 'S3', 'S4')])
    ix = pd.read_csv(AKAR + 'data_mentah/index_benchmark.csv')
else:
    d = pd.concat([pd.read_csv(AKAR + f'BacktestShariah2/data/harga/stor/harga_{s}.csv') for s in ('A', 'B')])
    ix = pd.read_csv(AKAR + 'BacktestShariah2/data/harga/stor/harga_idx.csv')
    lama = set(pd.concat([pd.read_csv(AKAR + f'data_mentah/dataset_{s}.csv', usecols=['ticker']) for s in ('S1', 'S2', 'S3', 'S4')]).ticker)
    d = d[~d.ticker.isin(lama)]          # hanya saham yang TIADA dalam set 431
d = d.drop_duplicates(['ticker', 'date']).sort_values(['ticker', 'date']).reset_index(drop=True)
q = ix[ix.ticker == 'QQQ'].sort_values('date').set_index('date').close
REJIM = ((q > q.rolling(50).mean()) & (q.rolling(10).mean() > q.rolling(20).mean()))

# kekuatan relatif rentas saham: pangkat peratus pulangan 126 hari pada setiap tarikh
px = d.pivot(index='date', columns='ticker', values='close')
RS = (px / px.shift(126) - 1).rank(axis=1, pct=True) * 100


def wilder(s, n): return s.ewm(alpha=1 / n, adjust=False, min_periods=n).mean()
def silang(a, b): return (a > b) & (a.shift() <= b.shift())
def dalam(ev, n): return ev.astype(float).rolling(n).max().fillna(0).astype(bool)
def F(s): return s.fillna(False).astype(bool)


def pertama(m, n):
    k = m.argmax(axis=1); k[~m.any(axis=1)] = n; return k


def supertrend(h, l, c, atr, m=3.0):
    n = len(c); arah = np.ones(n); hl = (h + l) / 2
    ub, lb = hl + m * atr, hl - m * atr
    fu, fl = ub.copy(), lb.copy()
    for i in range(1, n):
        if np.isnan(atr[i - 1]) or np.isnan(atr[i]):
            continue
        fu[i] = ub[i] if (ub[i] < fu[i - 1] or c[i - 1] > fu[i - 1]) else fu[i - 1]
        fl[i] = lb[i] if (lb[i] > fl[i - 1] or c[i - 1] < fl[i - 1]) else fl[i - 1]
        arah[i] = 1 if c[i] > fu[i - 1] else (-1 if c[i] < fl[i - 1] else arah[i - 1])
    return arah


out = []
for tk, g in d.groupby('ticker', sort=False):
    g = g.reset_index(drop=True); T = len(g)
    if T < 252 + H + 5:
        continue
    o_, h_, l_, c_, v_ = g.open, g.high, g.low, g.close, g.volume.astype(float)
    pc = c_.shift()
    tr = pd.concat([h_ - l_, (h_ - pc).abs(), (l_ - pc).abs()], axis=1).max(axis=1)
    atr14 = wilder(tr, 14); atr10 = wilder(tr, 10); atr20 = tr.rolling(20).mean()
    dl = c_.diff()
    rsi = lambda n: 100 - 100 / (1 + wilder(dl.clip(lower=0), n) / wilder((-dl).clip(lower=0), n).replace(0, np.nan))
    rsi14, rsi2 = rsi(14), rsi(2)
    um, dm = h_.diff(), -l_.diff()
    pdm = pd.Series(np.where((um > dm) & (um > 0), um, 0.0)); ndm = pd.Series(np.where((dm > um) & (dm > 0), dm, 0.0))
    pdi, ndi = 100 * wilder(pdm, 14) / atr14, 100 * wilder(ndm, 14) / atr14
    adx = wilder(100 * (pdi - ndi).abs() / (pdi + ndi).replace(0, np.nan), 14)
    ma = {n: c_.rolling(n).mean() for n in (10, 20, 50, 150, 200)}
    ema = lambda n: c_.ewm(span=n, adjust=False, min_periods=n).mean()
    ema10, ema20 = ema(10), ema(20)
    macd = ema(12) - ema(26); sig = macd.ewm(span=9, adjust=False).mean()
    sd20 = c_.rolling(20).std(ddof=0); bb_a, bb_b = ma[20] + 2 * sd20, ma[20] - 2 * sd20
    hh = lambda n: h_.rolling(n).max().shift(1)          # tinggi n bar SEBELUM hari ini
    ll = lambda n: l_.rolling(n).min().shift(1)
    h252 = h_.rolling(252).max(); l252 = l_.rolling(252).min()
    v50 = v_.rolling(50).mean().shift(1); vr = v_ / v50.replace(0, np.nan)
    ret1 = c_ / pc - 1; gap = o_ / pc - 1
    pos = (c_ - l_) / (h_ - l_).replace(0, np.nan)
    kc_atas = ema20 + 2 * atr20
    sq_on = (bb_a < ma[20] + 1.5 * atr20) & (bb_b > ma[20] - 1.5 * atr20)
    mom = c_ - ((h_.rolling(20).max() + l_.rolling(20).min()) / 2 + ma[20]) / 2
    sq_lepas = (~sq_on) & F(sq_on.shift()) & (mom > 0)
    st = pd.Series(supertrend(h_.to_numpy(float), l_.to_numpy(float), c_.to_numpy(float), atr10.to_numpy(float)))
    tenkan = (h_.rolling(9).max() + l_.rolling(9).min()) / 2; kijun = (h_.rolling(26).max() + l_.rolling(26).min()) / 2
    awan = pd.concat([((tenkan + kijun) / 2).shift(26), ((h_.rolling(52).max() + l_.rolling(52).min()) / 2).shift(26)], axis=1).max(axis=1)
    stk = 100 * (c_ - l_.rolling(14).min()) / (h_.rolling(14).max() - l_.rolling(14).min()).replace(0, np.nan)
    sk = stk.rolling(3).mean(); sdd = sk.rolling(3).mean()
    rs = RS[tk].reindex(g.date).reset_index(drop=True)
    templat = (c_ > ma[50]) & (ma[50] > ma[150]) & (ma[150] > ma[200]) & (ma[200] > ma[200].shift(20)) & (c_ >= 0.75 * h252) & (c_ >= 1.3 * l252)
    julat60 = hh(60) / ll(60) - 1
    tidur = julat60 <= 0.30
    bbw = (bb_a - bb_b) / ma[20]
    tidur2 = (adx.shift(1) < 20) & (bbw.shift(1) <= bbw.shift(1).rolling(252).quantile(0.30))
    v10 = v_.rolling(10).mean(); kering = v10 <= v10.rolling(60).min() * 1.05
    turun_v = v_.where(c_ < pc, 0.0).rolling(10).max().shift(1)
    baru252 = h_ >= h252
    gapday = (gap >= 0.05) & (vr >= 2)
    gh = h_.where(gapday).ffill(limit=10)
    bwh50 = (c_ < ma[50]).astype(float)
    bwh150 = (c_ < ma[150]).astype(float)

    S = {
        # A. indikator biasa (Moomoo)
        'A01 MACD silang naik': silang(macd, sig),
        'A02 MACD silang naik bawah sifar': silang(macd, sig) & (macd < 0),
        'A03 MACD silang naik atas sifar': silang(macd, sig) & (macd > 0),
        'A04 MA10 silang atas MA20': silang(ma[10], ma[20]),
        'A05 MA20 silang atas MA50': silang(ma[20], ma[50]),
        'A06 Golden cross MA50/MA200': silang(ma[50], ma[200]),
        'A07 RSI14 silang atas 50': silang(rsi14, pd.Series(50.0, index=g.index)),
        'A08 RSI14 silang atas 30 (bangkit terlebih jual)': silang(rsi14, pd.Series(30.0, index=g.index)),
        'A09 RSI2<10 atas MA200 (Connors)': (rsi2 < 10) & (c_ > ma[200]),
        'A10 Tutup pecah atas Keltner': silang(c_, kc_atas),
        'A11 Tutup pecah atas jalur atas Bollinger': silang(c_, bb_a),
        'A12 Bawah jalur bawah Bollinger + RSI<30': (c_ < bb_b) & (rsi14 < 30),
        'A13 Squeeze lepas ke atas': sq_lepas,
        'A14 Supertrend bertukar naik': (st > 0) & (st.shift() < 0),
        'A15 ADX silang atas 25 & +DI>-DI': silang(adx, pd.Series(25.0, index=g.index)) & (pdi > ndi),
        'A16 Ichimoku: tutup pecah atas awan': silang(c_, awan) & (tenkan > kijun),
        'A17 Stochastic silang naik dari bawah 20': silang(sk, sdd) & (sk.shift() < 20),
        'A18 Pecah tinggi 20 hari': c_ > hh(20),
        'A19 Pecah tinggi 55 hari': c_ > hh(55),
        'A20 Holy Grail: ADX>30, undur sentuh EMA20, tutup > tinggi semalam': (adx > 30) & (l_ <= ema20) & (c_ > h_.shift(1)),
        # B. saham tidur yang bangun
        'B01 Gap and go (buka >2% atas tinggi semalam, volum 1.5x)': (o_ > h_.shift(1) * 1.02) & (c_ > o_) & (vr >= 1.5),
        'B02 Episodic pivot (gap >=8%, volum 3x, bertahan)': (gap >= 0.08) & (vr >= 3) & (c_ >= o_),
        'B03 Lonjakan >=4% + volum 2x + tutup dekat tinggi': (ret1 >= 0.04) & (vr >= 2) & (pos >= 0.75),
        'B04 Lonjakan (B03) selepas tidur: julat 60 hari <=30%': (ret1 >= 0.04) & (vr >= 2) & (pos >= 0.75) & tidur,
        'B05 Lonjakan (B03) selepas tidur: ADX<20 & Bollinger sempit': (ret1 >= 0.04) & (vr >= 2) & (pos >= 0.75) & tidur2,
        'B06 Pecah tapak 3 bulan (kedalaman <=35%) + volum 1.5x': (c_ > hh(60)) & (julat60 <= 0.35) & (vr >= 1.5),
        'B07 Pecah tinggi 6 bulan + volum 1.5x': (c_ > hh(126)) & (vr >= 1.5),
        'B08 Tinggi 52 minggu pertama selepas >=6 bulan': baru252 & ~dalam(baru252.shift(1).fillna(False), 126),
        'B09 Stage 1->2: silang atas MA150 mendatar + volum': silang(c_, ma[150]) & ((ma[150] / ma[150].shift(20) - 1).abs() <= 0.02) & (vr >= 1.5) & (bwh150.shift(1).rolling(100).mean() >= 0.5),
        'B10 Bangkit dari jatuh: >=30% bawah puncak, silang atas MA50 + volum': (c_ <= 0.7 * h252) & silang(c_, ma[50]) & (bwh50.shift(1).rolling(50).mean() >= 0.8) & (vr >= 1.5),
        'B11 Volum kering kemudian meletup (naik >=2%, volum 2x)': dalam(F(kering.shift(1)), 10) & (vr >= 2) & (ret1 >= 0.02),
        'B12 Pocket pivot (volum > semua hari turun 10 hari)': (c_ > pc) & (v_ > turun_v) & (c_ > ma[50]) & (c_ <= 1.05 * ma[10]),
        'B13 Squeeze panjang (>=15/20 hari) lepas ke atas + volum': sq_lepas & (sq_on.astype(float).shift(1).rolling(20).sum() >= 15) & (vr >= 1.5),
        'B14 Jatuh lama, rendah lebih tinggi, pecah tinggi 20 hari + volum': (c_ <= 0.75 * h252) & (c_ > hh(20)) & (ll(10) > l_.rolling(30).min().shift(11)) & (vr >= 1.5),
        'B15 Pecah tinggi hari gap (sambungan dalam 10 hari)': (c_ > gh) & (pc <= gh.shift(1)) & ~gapday & F(gh.notna()),
        # C. pemimpin momentum (pakar)
        'C01 Templat trend Minervini (keadaan)': templat,
        'C02 VCP: templat + tapak ketat 10 hari + pecah + volum': F(templat.shift()) & ((hh(10) / ll(10) - 1) <= 0.10) & (c_ > hh(10)) & (vr >= 1.5),
        'C03 Qullamaggie: naik >=30% dahulu, rehat ketat, pecah + volum': ((c_.shift(10) / c_.shift(50) - 1) >= 0.30) & ((hh(10) / ll(10) - 1) <= 0.15) & (c_ > hh(10)) & (vr >= 1.5) & (c_ > ma[20]),
        'C04 RS >=90 & atas MA50 (keadaan)': (rs >= 90) & (c_ > ma[50]),
        'C05 RS baru masuk 10% teratas': (rs >= 90) & (rs.shift(1) < 90) & (c_ > ma[50]),
        'C06 Pemimpin undur ke MA20 (RS>=80, dekat puncak, sentuh MA20, tutup atas)': (rs >= 80) & (c_ >= 0.85 * h252) & (ma[50] > ma[50].shift(20)) & (l_ <= ma[20]) & (c_ > ma[20]) & (c_ > o_),
        "C07 O'Neil: pecah tinggi 50 hari + volum + RS>=80 + atas MA200": (c_ > hh(50)) & (vr >= 1.5) & (rs >= 80) & (c_ > ma[200]),
        'C08 Undur ke MA50 yang naik (sentuh, tutup atas, hari naik)': (ma[50] > ma[50].shift(20)) & (c_ > ma[200]) & (l_ <= ma[50] * 1.01) & (c_ > ma[50]) & (c_ > pc),
        'C09 EMA crossback: MA10>MA20>MA50, sentuh EMA20, tutup atas': (ma[10] > ma[20]) & (ma[20] > ma[50]) & (l_ <= ema20) & (c_ > ema20) & (c_ > o_),
        'C10 Dalam 5% dari puncak 52 minggu & RS>=80 (keadaan)': (c_ >= 0.95 * h252) & (rs >= 80),
    }

    o, h, l, c = (x.to_numpy(float) for x in (o_, h_, l_, c_))
    e = np.arange(253, T - H - 1)
    if len(e) < 5:
        continue
    W = lambda a: swv(np.asarray(a, float), H)[e]
    O, Hh, L, C = W(o), W(h), W(l), W(c); NO = swv(o, H)[e + 1]; P = o[e][:, None]; kk = np.arange(H)[None, :]
    cmax = np.maximum.accumulate(C, axis=1)
    cmax_dulu = np.concatenate([np.full((len(e), 1), -np.inf), cmax[:, :-1]], axis=1)
    chand = C < np.maximum.accumulate(cmax - 4 * W(atr14), axis=1)
    dua = lambda m: np.concatenate([np.zeros((len(e), 1), bool), m[:, 1:] & m[:, :-1]], axis=1)
    masa = lambda n: np.broadcast_to(kk == n - 1, C.shape)
    kosong = np.zeros_like(C, bool)
    h8 = np.broadcast_to(P * (1 - HENTI), C.shape)
    hbe = np.where(cmax_dulu >= P * (1 + HENTI), P, P * (1 - HENTI))

    def laksana(sg, henti=None, sasaran=None):
        sg = sg.copy(); sg[:, H - 1] = True
        ks = pertama(sg, H); t = 4 * ks + 4; px_ = np.take_along_axis(NO, ks[:, None], 1)[:, 0]
        if henti is not None:
            kh = pertama(L <= henti, H); khc = np.minimum(kh, H - 1)[:, None]
            pxh = np.minimum(np.take_along_axis(O, khc, 1), np.take_along_axis(henti, khc, 1))[:, 0]
            th = np.where(kh < H, 4 * kh + 1, 10 ** 9); m = th < t; t = np.where(m, th, t); px_ = np.where(m, pxh, px_)
        if sasaran is not None:
            ps = P * (1 + sasaran); kt = pertama(Hh >= ps, H); ktc = np.minimum(kt, H - 1)[:, None]
            pxt = np.maximum(np.take_along_axis(O, ktc, 1)[:, 0], ps[:, 0])
            tt = np.where(kt < H, 4 * kt + 2, 10 ** 9); m = tt < t; t = np.where(m, tt, t); px_ = np.where(m, pxt, px_)
        return (px_ / P[:, 0] - 1 - KOS).astype('float32'), (t // 4 + 1).astype('int16')

    R = {'tarikh': g.date.to_numpy()[e - 1].astype('int32')}
    for n in (5, 10, 20, 40, 60):
        R[f'r{n}'] = (c[e + n - 1] / o[e] - 1 - KOS).astype('float32')
    Lr, Hr = L[:, :HR], Hh[:, :HR]
    ks = pertama(Lr <= P * (1 - HENTI), HR)
    for tg in (8, 16, 24):
        kt = pertama(Hr >= P * (1 + tg / 100), HR)
        R[f'm{tg}'] = (kt < ks)                  # capai +tg% DAHULU sebelum -8% (bar sama: henti dahulu)
    R['kena8'] = ks < HR
    R['mae20'] = (L[:, :20].min(axis=1) / P[:, 0] - 1).astype('float32')
    if True:
        X = {
            'biar lari (henti -8% sahaja)': (kosong, h8, None),
            'Chandelier 4xATR': (chand, h8, None),
            'pulang modal selepas +8%, kemudian Chandelier': (chand, hbe, None),
            'dua tutup bawah MA50': (dua(C < W(ma[50])), h8, None),
            'dua tutup bawah MA20': (dua(C < W(ma[20])), h8, None),
            'tutup bawah EMA10': (C < W(ema10), h8, None),
            'MA10 bawah MA20': (W(ma[10]) < W(ma[20]), h8, None),
            'Supertrend bertukar turun': (W(st) < 0, h8, None),
            'MACD silang turun': (W(macd) < W(sig), h8, None),
            'RSI14 bawah 50': (W(rsi14) < 50, h8, None),
            'tutup bawah rendah 10 hari': (C < W(ll(10)), h8, None),
            'tutup bawah rendah 20 hari': (C < W(ll(20)), h8, None),
            'sasaran +16%': (kosong, h8, 0.16),
            'sasaran +24%': (kosong, h8, 0.24),
            'pegang 10 hari': (masa(10), h8, None),
            'pegang 20 hari': (masa(20), h8, None),
            'pegang 40 hari': (masa(40), h8, None),
            'TANPA henti: Chandelier 4xATR': (chand, None, None),
            'TANPA henti: dua tutup bawah MA50': (dua(C < W(ma[50])), None, None),
        }
        for j, (kn, (sg, ht, ss)) in enumerate(X.items()):
            R[f'x{j:02d}'], R[f'd{j:02d}'] = laksana(sg, ht, ss)
        r5, d5 = laksana(masa(5), h8, None); ra, da = R['x05'], R['d05']
        R['x19'], R['d19'] = ((r5 + ra) / 2).astype('float32'), ((d5 + da) // 2).astype('int16')   # jual separuh hari ke-5, baki ikut EMA10
    f = pd.DataFrame(R)
    f['saham'] = tk
    nilai20 = (c_ * v_).rolling(20).mean()
    f['layak'] = ((c_ >= 10) & (nilai20 >= 1e6)).to_numpy()[e - 1]
    f['on'] = REJIM.reindex(f.tarikh).fillna(False).to_numpy()
    f['atrp'] = (atr14 / c_).to_numpy()[e - 1].astype('float32')
    f['rs'] = rs.to_numpy()[e - 1].astype('float32')
    f['atas200'] = (c_ > ma[200]).to_numpy()[e - 1]
    ciri = {'f_ret1': ret1, 'f_vr': vr, 'f_pos': pos, 'f_adx1': adx.shift(1), 'f_bbwp': bbw.shift(1).rolling(252).rank(pct=True),
            'f_julat60': julat60, 'f_gap': gap, 'f_j52': c_ / h252 - 1, 'f_roc60': c_.shift(1) / c_.shift(61) - 1,
            'f_ma200': c_ / ma[200] - 1, 'f_ma50': c_ / ma[50] - 1}
    for kf, vf in ciri.items():
        f[kf] = vf.to_numpy(float)[e - 1].astype('float32')
    L50 = pd.Series(50.0, index=g.index); L25 = pd.Series(25.0, index=g.index)
    kead = {'k_macd': macd > sig, 'k_macd0': macd > 0, 'k_ma1020': ma[10] > ma[20], 'k_ma2050': ma[20] > ma[50], 'k_ma50200': ma[50] > ma[200],
            'k_c200': c_ > ma[200], 'k_rsi50': rsi14 > 50, 'k_sqon': sq_on, 'k_sqlepas10': dalam(sq_lepas, 10), 'k_adx': (adx > 25) & (pdi > ndi),
            'k_st': st > 0, 'k_awan': c_ > awan, 'k_ema20': c_ > ema20, 'k_stoch': sk > sdd, 'k_vol': vr >= 1.5}
    pecah20 = F(c_ > hh(20))
    peris = {'e_macd': silang(macd, sig), 'e_sqon': F(sq_on) & ~F(sq_on.shift()), 'e_sqlepas': sq_lepas, 'e_ma1020': silang(ma[10], ma[20]),
             'e_ma2050': silang(ma[20], ma[50]), 'e_gc': silang(ma[50], ma[200]), 'e_rsi50': silang(rsi14, L50), 'e_kelt': silang(c_, kc_atas),
             'e_st': (st > 0) & (st.shift() < 0), 'e_awan': silang(c_, awan), 'e_hh20': pecah20 & ~F(pecah20.shift()), 'e_adx': silang(adx, L25) & (pdi > ndi),
             'e_rsi2': (rsi2 < 10) & (rsi2.shift() >= 10), 'e_vol': (ret1 >= 0.04) & (vr >= 2) & (pos >= 0.75), 'e_c50': silang(c_, ma[50])}
    # ---- pusingan 2: indikator tambahan ----
    tp = (h_ + l_ + c_) / 3
    obv = (np.sign(dl).fillna(0) * v_).cumsum()
    mf = tp * v_; mpos = mf.where(tp > tp.shift(), 0.0).rolling(14).sum(); mneg = mf.where(tp < tp.shift(), 0.0).rolling(14).sum()
    mfi = 100 - 100 / (1 + mpos / mneg.replace(0, np.nan))
    tpa = tp.to_numpy(float); wv = swv(tpa, 20); cci_ = np.full(len(tpa), np.nan)
    mm = wv.mean(axis=1); cci_[19:] = (tpa[19:] - mm) / (0.015 * np.abs(wv - mm[:, None]).mean(axis=1) + 1e-12); cci = pd.Series(cci_)
    wr = -100 * (h_.rolling(14).max() - c_) / (h_.rolling(14).max() - l_.rolling(14).min()).replace(0, np.nan)
    ha, la = h_.to_numpy(float), l_.to_numpy(float); n_ = len(ha); ps = np.full(n_, np.nan); naik_ = True; af = 0.02; ep = ha[0]; ps[0] = la[0]
    for i in range(1, n_):
        p0 = ps[i - 1] + af * (ep - ps[i - 1])
        if naik_:
            p0 = min(p0, la[i - 1], la[i - 2] if i > 1 else la[i - 1])
            if la[i] < p0: naik_ = False; p0 = ep; ep = la[i]; af = 0.02
            elif ha[i] > ep: ep = ha[i]; af = min(af + 0.02, 0.2)
        else:
            p0 = max(p0, ha[i - 1], ha[i - 2] if i > 1 else ha[i - 1])
            if ha[i] > p0: naik_ = True; p0 = ep; ep = ha[i]; af = 0.02
            elif la[i] < ep: ep = la[i]; af = min(af + 0.02, 0.2)
        ps[i] = p0
    psar = pd.Series(ps)
    au = np.full(n_, np.nan); ad_ = np.full(n_, np.nan)
    au[25:] = 100 * swv(ha, 26).argmax(axis=1) / 25; ad_[25:] = 100 * swv(la, 26).argmin(axis=1) / 25
    au, ad_ = pd.Series(au), pd.Series(ad_)
    ema8, ema21 = ema(8), ema(21)
    cmf = ((((c_ - l_) - (h_ - c_)) / (h_ - l_).replace(0, np.nan)) * v_).rolling(20).sum() / v_.rolling(20).sum().replace(0, np.nan)
    wm = ema(60) - ema(130); wms = wm.ewm(span=45, adjust=False).mean()
    Z0 = pd.Series(0.0, index=g.index); Z100 = pd.Series(100.0, index=g.index)
    julat = h_ - l_; badan = (c_ - o_).abs()
    kead.update({'k_obv': obv > obv.rolling(20).mean(), 'k_mfi': mfi > 50, 'k_cci': cci > 0, 'k_wr': wr > -50, 'k_psar': c_ > psar, 'k_aroon': au > ad_,
                 'k_ema821': ema8 > ema21, 'k_dmi': pdi > ndi, 'k_roc': c_ > c_.shift(20), 'k_cmf': cmf > 0, 'k_mingguan': (ma[50] > ma[150]) & (c_ > ma[150]),
                 'k_wmacd': wm > wms, 'k_rendah_naik': ll(10) > l_.rolling(20).min().shift(11), 'k_don': c_ > (h_.rolling(20).max() + l_.rolling(20).min()) / 2})
    obvh = F(obv >= obv.rolling(20).max())
    peris.update({'e_obv': obvh & ~F(obvh.shift()), 'e_mfi': silang(mfi, L50), 'e_cci': silang(cci, Z100), 'e_psar': (c_ > psar) & (pc <= psar.shift()),
                  'e_aroon': silang(au, ad_), 'e_ema821': silang(ema8, ema21), 'e_dmi': silang(pdi, ndi), 'e_cmf': silang(cmf, Z0), 'e_wmacd': silang(wm, wms),
                  'e_engulf': (c_ > o_) & (pc < o_.shift()) & (c_ > o_.shift()) & (o_ < pc),
                  'e_hammer': ((np.minimum(o_, c_) - l_) >= 2 * badan) & ((h_ - np.maximum(o_, c_)) <= 0.3 * julat) & (julat > 0) & (c_ < ma[20]),
                  'e_nr7': (julat.shift(1) <= julat.shift(1).rolling(7).min()) & (c_ > h_.shift(1)),
                  'e_inside': (h_.shift(1) < h_.shift(2)) & (l_.shift(1) > l_.shift(2)) & (c_ > h_.shift(1)), 'e_gap': o_ > h_.shift(1) * 1.02})
    for kf, vf in {**kead, **peris}.items():
        f[kf] = F(vf).to_numpy()[e - 1]
    for j, (sn, sv) in enumerate(S.items()):
        f[sn] = F(sv).to_numpy()[e - 1]
    out.append(f)

P_ = pd.concat(out, ignore_index=True)
P_['saham'] = P_.saham.astype('category')
P_.to_pickle(KELUAR)
print(SUMBER, 'baris', len(P_), 'saham', P_.saham.nunique(), 'tarikh', P_.tarikh.min(), P_.tarikh.max(), 'layak', P_.layak.mean().round(3))
if SUMBER == 'mentah':
    import json
    json.dump(list(X) + ['jual separuh hari ke-5, baki ikut EMA10'], open(KELUAR + '.keluar.json', 'w'))
