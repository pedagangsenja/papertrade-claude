"""Pusingan 2 (tinjauan): gabungan serentak 2-6 daripada 31 keadaan (+7-8 daripada 17 asal) dan
turutan 2-4 langkah daripada 29 peristiwa, tingkap 5/10/20 hari. Kaedah pegang/jual tetap:
saham atas MA50, henti -8%, jual selepas dua tutup bawah MA50. Dengan PLASEBO (hasil dianjak masa)."""
import pandas as pd, numpy as np, itertools, time, sys
rng = np.random.default_rng(5)
pd.set_option('display.width', 330, 'display.max_rows', 400, 'display.max_colwidth', 150)
NAMA = {'k_macd': 'MACD hijau', 'k_macd0': 'MACD>0', 'k_ma1020': 'MA10>MA20', 'k_ma2050': 'MA20>MA50', 'k_ma50200': 'MA50>MA200', 'k_c200': 'tutup>MA200',
        'k_rsi50': 'RSI>50', 'k_sqon': 'squeeze ON', 'k_sqlepas10': 'squeeze lepas(10h)', 'k_adx': 'ADX>25&+DI>-DI', 'k_st': 'Supertrend naik', 'k_awan': 'atas awan',
        'k_ema20': 'tutup>EMA20', 'k_stoch': 'Stoch K>D', 'k_vol': 'volum>=1.5x', 'k_rs80': 'RS>=80', 'k_52w': 'dalam 10% puncak 52w', 'k_obv': 'OBV>purata20',
        'k_mfi': 'MFI>50', 'k_cci': 'CCI>0', 'k_wr': 'Williams%R>-50', 'k_psar': 'atas PSAR', 'k_aroon': 'Aroon naik>turun', 'k_ema821': 'EMA8>EMA21', 'k_dmi': '+DI>-DI',
        'k_roc': 'ROC20>0', 'k_cmf': 'CMF>0', 'k_mingguan': 'trend mingguan naik', 'k_wmacd': 'MACD mingguan hijau', 'k_rendah_naik': 'rendah lebih tinggi', 'k_don': 'atas tengah Donchian',
        'e_macd': 'MACD silang naik', 'e_sqon': 'squeeze mula ON', 'e_sqlepas': 'squeeze lepas', 'e_ma1020': 'MA10 silang MA20', 'e_ma2050': 'MA20 silang MA50', 'e_gc': 'golden cross',
        'e_rsi50': 'RSI silang 50', 'e_kelt': 'pecah Keltner', 'e_st': 'Supertrend naik', 'e_awan': 'pecah awan', 'e_hh20': 'pecah tinggi 20h', 'e_adx': 'ADX silang 25',
        'e_rsi2': 'undur RSI2<10', 'e_vol': 'lonjakan 4%+volum 2x', 'e_c50': 'silang atas MA50', 'e_obv': 'OBV tinggi baharu', 'e_mfi': 'MFI silang 50', 'e_cci': 'CCI silang 100',
        'e_psar': 'PSAR bertukar naik', 'e_aroon': 'Aroon silang', 'e_ema821': 'EMA8 silang EMA21', 'e_dmi': '+DI silang -DI', 'e_cmf': 'CMF silang 0', 'e_wmacd': 'MACD mingguan silang',
        'e_engulf': 'bullish engulfing', 'e_hammer': 'hammer', 'e_nr7': 'pecah NR7', 'e_inside': 'pecah inside day', 'e_gap': 'gap naik 2%'}
ASAL = ['k_macd', 'k_macd0', 'k_ma1020', 'k_ma2050', 'k_ma50200', 'k_c200', 'k_rsi50', 'k_sqon', 'k_sqlepas10', 'k_adx', 'k_st', 'k_awan', 'k_ema20', 'k_stoch', 'k_vol', 'k_rs80', 'k_52w']


def dalam(m, N):
    cs = np.cumsum(m, axis=0, dtype=np.int32); o = cs.copy(); o[N:] -= cs[:-N]; return o > 0


class Set:
    def __init__(s, f, y0):
        P = pd.read_pickle(f); P['k_rs80'] = P.rs >= 80; P['k_52w'] = P.f_j52 >= -0.10
        s.dts = np.sort(P.tarikh.unique()); di = np.searchsorted(s.dts, P.tarikh.to_numpy()); ti = P.saham.cat.codes.to_numpy(); s.shape = (len(s.dts), len(P.saham.cat.categories))
        def M(v, fill, dt=float):
            m = np.full(s.shape, fill, dtype=dt); m[di, ti] = np.asarray(v, dt); return m
        ok = M(P.layak & (P.f_ma50 > 0), False, bool); R = M(P.x03 * 100, np.nan); ada = M(np.ones(len(P)), False, bool)
        awal = np.zeros(s.shape, bool); awal[ada.argmax(axis=0), np.arange(s.shape[1])] = True
        s.idx = np.flatnonzero(ok & ~np.isnan(R)); s.r = R.flat[s.idx]
        T = s.shape[0]; off = rng.integers(60, T - 60, size=s.shape[1])
        Rp = np.take_along_axis(R, (np.arange(T)[:, None] - off[None, :]) % T, axis=0); s.rp = Rp.flat[s.idx]     # PLASEBO: hasil dianjak masa
        s.yi = (np.broadcast_to((s.dts // 10000)[:, None], s.shape).flat[s.idx] - y0).astype(np.int64)
        s.kn = [k for k in P.columns if k[:2] == 'k_']; s.en = [k for k in P.columns if k[:2] == 'e_']
        s.T, s.Y = {}, {}
        for k in s.kn:
            m = M(P[k], False, bool); p = np.ones(s.shape, bool); p[1:] = m[:-1]; p[awal] = True
            s.T[k] = m.flat[s.idx]; s.Y[k] = p.flat[s.idx]
        s.E = {k: M(P[k], False, bool) for k in s.en}; s.Ef = {k: s.E[k].flat[s.idx] for k in s.en}

    def st(s, ev, r):
        x = r[ev]; y = s.yi[ev]
        if r is s.rp:
            g = ~np.isnan(x); x = x[g]; y = y[g]
        n = len(x)
        if n < 200: return None
        cnt = np.bincount(y, minlength=7); sm = np.bincount(y, weights=x, minlength=7); nA = cnt[:3].sum(); nB = cnt[3:].sum()
        if nA < 100 or nB < 100: return None
        v = cnt >= 15
        return (n, sm.sum() / n, (x > 0).mean() * 100, sm[:3].sum() / nA, sm[3:].sum() / nB, nA, nB, ((sm[v] / cnt[v]) > 0).sum(), v.sum())

    def vmean(s, ev, r):
        x = r[ev]; x = x[~np.isnan(x)]; return (len(x), x.mean() if len(x) else np.nan)


P = Set('panel_mentah.pkl', 2020); V = Set('panel_stor.pkl', 2025)
semua = np.ones(len(P.r), bool); k0 = P.st(semua, P.r); k0p = P.st(semua, P.rp); CA, CB, CAp, CBp = k0[3], k0[4], k0p[3], k0p[4]
CV = V.vmean(np.ones(len(V.r), bool), V.r)[1]; CVp = V.vmean(np.ones(len(V.r), bool), V.rp)[1]
print('KAWALAN sebenar: semua %.2f A %.2f B %.2f lain %.2f | plasebo: A %.2f B %.2f lain %.2f' % (k0[1], CA, CB, CV, CAp, CBp, CVp), flush=True)
REK = []     # (keluarga, kunci, sebenar(9), plasebo(9))


def rekod(kel, kunci, ev):
    a = P.st(ev, P.r); b = P.st(ev, P.rp)
    if a is None and b is None: return
    REK.append((kel, kunci, a, b))


# ---------------- A. SERENTAK ----------------
def dfs(names, kel_fmt, lo, hi, start=0, t=None, y=None, ch=()):
    for i in range(start, len(names)):
        k = names[i]; t2 = P.T[k] if t is None else t & P.T[k]
        if t2.sum() < 250: continue
        y2 = P.Y[k] if y is None else y & P.Y[k]; c2 = ch + (k,)
        if len(c2) >= lo: rekod(kel_fmt % len(c2), c2, t2 & ~y2)
        if len(c2) < hi: dfs(names, kel_fmt, lo, hi, i + 1, t2, y2, c2)


t0 = time.time(); dfs(P.kn, 'serentak %d (31 keadaan)', 2, 6); print('serentak 2-6/31 siap %.0fs, rekod %d' % (time.time() - t0, len(REK)), flush=True)
t0 = time.time(); n0 = len(REK); dfs(ASAL, 'serentak %d (17 asal)', 7, 9); print('serentak 7-9/17 siap %.0fs, rekod %d' % (time.time() - t0, len(REK) - n0), flush=True)

# ---------------- B. BERTURUTAN ----------------
SEQ = {}   # kunci -> (N, kunci) untuk penilaian saham lain
for N in (5, 10, 20):
    t0 = time.time(); W = {k: dalam(P.E[k], N) for k in P.en}; WAB = {}
    for a, b in itertools.permutations(P.en, 2):
        m = P.E[b] & W[a]; rekod(f'turutan 2 langkah ({N}h)', (a, b), m.flat[P.idx])
        WAB[(a, b)] = dalam(m, N)
    n3 = 0
    for (a, b), wab in WAB.items():
        wf = wab.flat[P.idx]
        if wf.sum() < 250: continue
        for c in P.en:
            if c in (a, b): continue
            ev = P.Ef[c] & wf
            if ev.sum() < 200: continue
            rekod(f'turutan 3 langkah ({N}h)', (a, b, c), ev); n3 += 1
            if N == 10:
                w3 = dalam(P.E[c] & wab, N).flat[P.idx]
                if w3.sum() < 250: continue
                for d_ in P.en:
                    if d_ in (a, b, c): continue
                    ev4 = P.Ef[d_] & w3
                    if ev4.sum() >= 200: rekod('turutan 4 langkah (10h)', (a, b, c, d_), ev4)
    print(f'turutan N={N} siap %.0fs, jumlah rekod %d' % (time.time() - t0, len(REK)), flush=True)
    del W, WAB

# ---------------- C. penilaian ----------------
def evV(kel, kunci, r):
    if kel.startswith('serentak'):
        t = np.ones(len(V.r), bool); y = np.ones(len(V.r), bool)
        for k in kunci: t &= V.T[k]; y &= V.Y[k]
        return V.vmean(t & ~y, r)
    N = int(kel.split('(')[1].split('h')[0]); m = V.E[kunci[0]]
    for k in kunci[1:]: m = V.E[k] & dalam(m, N)
    return V.vmean(m.flat[V.idx], r)


col = ['n', 'jgk', 'mng', 'A', 'B', 'nA', 'nB', 'yp', 'yv']
D = pd.DataFrame([(k, q) + (a if a else (np.nan,) * 9) + (b if b else (np.nan,) * 9) for k, q, a, b in REK], columns=['kel', 'kunci'] + col + ['p_' + c for c in col])
D.to_pickle('habis.pkl'); print('\nJUMLAH gabungan direkod (>=200 dagangan, >=100 setiap separuh):', len(D), flush=True)
RING = []; LULUS = []
for kel, T in D.groupby('kel', sort=False):
    S = T.dropna(subset=['jgk']).copy(); S['xA'] = S.A - CA; S['xB'] = S.B - CB
    Pl = T.dropna(subset=['p_jgk']).copy(); Pl['xA'] = Pl.p_A - CAp; Pl['xB'] = Pl.p_B - CBp
    tA = S.sort_values('xA', ascending=False).head(20); tB = S.sort_values('xB', ascending=False).head(20)
    ok = S[(S.n >= 300) & (S.xA > 0.3) & (S.xB > 0.3) & (S.yp >= S.yv - 1)].copy()
    okp = Pl[(Pl.p_n >= 300) & (Pl.xA > 0.3) & (Pl.xB > 0.3) & (Pl.p_yp >= Pl.p_yv - 1)].copy()
    vv = [evV(kel, q, V.r) for q in ok.kunci]; ok['nV'] = [v[0] for v in vv]; ok['jgkV'] = [v[1] for v in vv]
    vp = [evV(kel, q, V.rp) for q in okp.kunci]; okp['nV'] = [v[0] for v in vp]; okp['jgkV'] = [v[1] for v in vp]
    fin = ok[(ok.nV >= 30) & (ok.jgkV > CV + 0.3)].copy(); finp = okp[(okp.nV >= 30) & (okp.jgkV > CVp + 0.3)]
    fin['kel'] = kel; LULUS.append(fin)
    RING.append(dict(keluarga=kel, diuji=len(S), purata=S.jgk.mean(), atasi_kawalan_2separuh=((S.xA > 0) & (S.xB > 0)).mean() * 100, korelasi_AB=S.xA.corr(S.xB, method='spearman'),
                     top20A_ke_B=tA.xB.mean(), top20B_ke_A=tB.xA.mean(), lulus_utama=len(ok), plasebo_lulus_utama=len(okp), lulus_semua=len(fin), plasebo_lulus_semua=len(finp)))
RG = pd.DataFrame(RING); print('\n== RINGKASAN SETIAP KELUARGA =='); print(RG.round(2).to_string(index=False))
print('\nJUMLAH: diuji %d | lulus utama %d (plasebo %d) | lulus semua %d (plasebo %d)' % (RG.diuji.sum(), RG.lulus_utama.sum(), RG.plasebo_lulus_utama.sum(), RG.lulus_semua.sum(), RG.plasebo_lulus_semua.sum()))
L = pd.concat(LULUS); L['nama'] = [(' + ' if k.startswith('serentak') else ' -> ').join(NAMA[x] for x in q) for k, q in zip(L.kel, L.kunci)]
L['min_lebih'] = L[['xA', 'xB']].min(axis=1); L['lebihV'] = L.jgkV - CV; L.to_pickle('habis_lulus.pkl')
for kel, T in L.groupby('kel', sort=False):
    print(f'\n-- {kel}: lulus semua {len(T)}; 8 teratas ikut lebihan terkecil antara dua separuh --')
    print(T.sort_values('min_lebih', ascending=False)[['nama', 'n', 'jgk', 'mng', 'A', 'B', 'yp', 'yv', 'nV', 'jgkV']].head(8).round(2).to_string(index=False))
# keadaan/peristiwa paling kerap muncul dalam yang lulus semua
from collections import Counter
cs = Counter(x for q in L.kunci for x in q); print('\nPALING KERAP dalam gabungan yang lulus semua:', [(NAMA[k], v) for k, v in cs.most_common(15)])
