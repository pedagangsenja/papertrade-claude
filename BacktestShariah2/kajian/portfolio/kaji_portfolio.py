# Kajian portfolio modal terhad (19 Okt 2026; laporan kajian/KAJIAN_PORTFOLIO.md).
# Soalan: Papertrade C membeli setiap isyarat (~800 sehari). Dengan modal sebenar 10 slot (10% ekuiti setiap satu),
# isyarat mana patut diambil apabila isyarat lebih banyak daripada slot kosong?
# Calon = semua dagangan enjin v1.2 134 kaedah (set 431, data_mentah 2019–2026), dijana oleh kaji_lorong2.py jana.
# Dua cara keluar: L1 = peraturan kaedah (enjin), L2 = Chandelier tutup 4xATR14 paras naik tanpa henti (lorong 2 semasa).
# Semua ukuran pemilihan diambil pada tutup hari isyarat (tiada pandang hadapan), kecuali 'Kaedah statik' (rujukan sahaja).
# Guna (dari akar repo; perlu numba):
#   KAJIAN_LORONG2=<folder> python3 BacktestShariah2/kajian/lorong2/kaji_lorong2.py jana
#   git show origin/kajian-gred:BacktestShariah2/kajian/data/kumpulan_harian.csv.gz > <folder>/kumpulan_harian.csv.gz
#   KAJIAN_LORONG2=<folder> python3 BacktestShariah2/kajian/portfolio/kaji_portfolio.py sedia
#   KAJIAN_LORONG2=<folder> python3 BacktestShariah2/kajian/portfolio/kaji_portfolio.py semak   -> enjin.portfolio = enjin kajian
#   KAJIAN_LORONG2=<folder> python3 BacktestShariah2/kajian/portfolio/kaji_portfolio.py sim
#   KAJIAN_LORONG2=<folder> python3 BacktestShariah2/kajian/portfolio/kaji_portfolio.py ringkas
#   KAJIAN_LORONG2=<folder> python3 BacktestShariah2/kajian/portfolio/kaji_portfolio.py tahan     -> ketahanan bias set 431
#   KAJIAN_LORONG2=<folder> python3 BacktestShariah2/kajian/portfolio/kaji_portfolio.py playbook  -> PLAYBOOK_10 / RAWAK_PADAN_10
#       (pra-daftar kajian/portfolio/PRA_DAFTAR_PLAYBOOK.md §8; enjin standard/portfolio_slot.bina_pb yang sama dengan jejak
#       hadapan) -> playbook.csv, playbook_tahunan.csv, playbook_corong.csv, mdd_jangka.json
import argparse, glob, json, os, pickle, sys
import numpy as np, pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'lorong2'))
from kaji_lorong2 import AKAR, COST, KOD, OUT, muat, sim, tatasusunan  # noqa: E402

BS2 = os.path.join(AKAR, 'BacktestShariah2')
MULA = pd.Timestamp('2020-11-02')          # 12 bulan sejarah dagangan untuk skor kaedah walk-forward
H1_AKHIR = pd.Timestamp('2023-10-31')
SLOT, W = 10, 0.10
BENIH = 30
JAUH = np.datetime64('2100-01-01')
BERMASALAH = {'ASST', 'FCEL', 'MTDR', 'OVV', 'PR', 'SM', 'VAL', 'XENE'}   # peristiwa korporat tidak terlaras (LAPORAN_UTAMA §10)


# ---------------------------------------------------------------- 1. calon + ukuran pada hari isyarat
def skor_industri(path, spy):
    """Gred Industri v2 (standard/gred_kumpulan.py siri) daripada indeks kumpulan harian cawangan kajian-gred."""
    K = pd.read_csv(path); K = K[K.jenis == 'Industri']; K['tarikh'] = pd.to_datetime(K.tarikh)
    I, M1, N = (K.pivot(index='tarikh', columns='nama', values=v) for v in ('indeks', 'm1m', 'n'))
    I = I.ffill(); ok = N >= 3
    rs = I.div(spy.reindex(I.index), axis=0); mrs = rs / rs.rolling(252).mean() - 1; ma = I.rolling(150).mean()
    w1 = (mrs > 0).astype(float).where(mrs.notna())
    w2 = (mrs > mrs.shift(21)).astype(float).where(mrs.notna() & mrs.shift(21).notna())
    w3 = ((I > ma) & (ma > ma.shift(20))).astype(float).where(mrs.notna() & ma.shift(20).notna())
    pk = lambda X: X.where(ok).rank(axis=1, pct=True)
    return 100 * pk((w1 + w2 + w3) / 3 + pk(M1))


def cmd_sedia(a):
    T = pd.concat([pickle.load(open(f, 'rb')) for f in sorted(glob.glob(f'{OUT}/T/*.pkl'))], ignore_index=True)
    T = T[T.ent >= pd.Timestamp('2019-11-01')].reset_index(drop=True)
    fr, idx = muat(); so, sc = idx['SPY'].open, idx['SPY'].close
    n = len(T); print('dagangan', n, 'kaedah', T.mid.nunique(), flush=True)
    F = {k: np.full(n, np.nan) for k in ('buka', 'ret2', 'mom126', 'mutlak12', 'mansfield', 'atrp')}
    ex2 = np.empty(n, 'datetime64[ns]'); akhir2 = np.zeros(n, bool)
    for t, G in T.groupby('ticker'):
        g = fr[t]; dts = g.index; o, h, l, c, A, we, pwc = tatasusunan(g)
        ks = dts.get_indexer(G.ent).astype(np.int64); ss = dts.get_indexer(G.sig); ix = G.index.to_numpy()
        J, X, Wk = sim(o, h, l, c, A['atr14'], we, pwc, ks, np.full(len(ks), np.nan), 6, 4.0, 1)
        F['buka'][ix] = o[ks]; F['ret2'][ix] = X / o[ks] * (1 - COST) / (1 + COST) - 1
        ex2[ix] = dts[J].values; akhir2[ix] = Wk == 2
        cl = g.close; rl = cl / sc.reindex(dts).ffill()
        F['mom126'][ix] = (cl / cl.shift(126) - 1).to_numpy()[ss]
        F['mutlak12'][ix] = (cl / cl.shift(252) - 1).to_numpy()[ss]
        F['mansfield'][ix] = (rl / rl.rolling(252).mean() - 1).to_numpy()[ss]
        pc = cl.shift(1); tr = pd.concat([g.high - g.low, (g.high - pc).abs(), (g.low - pc).abs()], axis=1).max(axis=1)
        F['atrp'][ix] = (tr.rolling(14).mean() / cl).to_numpy()[ss]
    for k, v in F.items(): T[k] = v
    T['ex2'] = ex2; T['akhir2'] = akhir2; T['akhir1'] = T.why.eq('hujung')
    cf = lambda d: sc.reindex(pd.DatetimeIndex(d), method='ffill').to_numpy()
    T['spy1'] = cf(T.ex) / so.reindex(T.ent).to_numpy() - 1
    T['spy2'] = cf(T.ex2) / so.reindex(T.ent).to_numpy() - 1
    T['spy_atas'] = (sc > sc.rolling(200).mean()).reindex(T.sig).to_numpy()
    rs = pd.read_csv(os.path.join(BS2, 'kajian', 'rs', 'rs_pasaran_431.csv.gz'))
    rs['sig'] = pd.to_datetime(rs.date.astype(str)); rs = rs.rename(columns={'rs_pasaran': 'rs'})[['sig', 'ticker', 'rs']]
    T = T.merge(rs, on=['sig', 'ticker'], how='left')
    peta = pd.read_csv(os.path.join(BS2, 'papertrade', 'peta_industri.csv')).drop_duplicates('ticker').set_index('ticker').industri
    S = skor_industri(a.kumpulan, sc).stack().rename('ind_skor').reset_index().rename(columns={'tarikh': 'sig', 'nama': 'industri'})
    T['industri'] = T.ticker.map(peta)
    T = T.merge(S, on=['sig', 'industri'], how='left')
    T['konsensus'] = T.groupby(['ticker', 'sig']).mid.transform('nunique')
    T.drop(columns=['mfe'], errors='ignore').to_pickle(f'{OUT}/calon.pkl')
    print('liputan: rs %.1f%%, industri %.1f%%, mansfield %.1f%%' % tuple(100 * T[k].notna().mean() for k in ('rs', 'ind_skor', 'mansfield')))


# ---------------------------------------------------------------- 2. enjin portfolio slot
def portfolio(ent_i, ex_i, ret, tk, e_open, susun, Cm, slots=SLOT, w=W):
    """Ikut enjin.portfolio v1.2: keluar direalisasi dahulu; masuk ikut susunan skor; satu posisi bagi setiap saham;
    saiz = min(tunai, ekuiti semalam x w). Nilai pasaran = saiz x tutup / buka masuk."""
    nd = Cm.shape[0]; cash = eq = 1.0; pos = []; held = set(); curve = np.empty(nd); npos = np.empty(nd); ambil = []; amaun = []
    for d in range(nd):
        keep = []
        for q, am in pos:
            if ex_i[q] == d: cash += am * (1 + ret[q]); held.discard(tk[q])
            else: keep.append((q, am))
        pos = keep
        for q in susun[d]:
            if len(pos) >= slots: break
            if tk[q] in held: continue
            am = min(cash, eq * w)
            if am <= 1e-12: break
            cash -= am; pos.append((q, am)); held.add(tk[q]); ambil.append(q); amaun.append(am)
        keep = []
        for q, am in pos:
            if ex_i[q] == d and ent_i[q] == d: cash += am * (1 + ret[q]); held.discard(tk[q])
            else: keep.append((q, am))
        pos = keep
        eq = cash + sum(am * Cm[d, tk[q]] / e_open[q] for q, am in pos); curve[d] = eq; npos[d] = len(pos)
    portfolio.amaun = np.array(amaun)
    return curve, npos, np.array(ambil, int)


class Pasar:
    def __init__(self, T, fr, mula=MULA):
        self.hari = pd.DatetimeIndex(sorted(set().union(*[g.index for g in fr.values()])))
        self.hari = self.hari[self.hari >= mula]
        self.tick = sorted(fr); tid = {t: i for i, t in enumerate(self.tick)}
        self.Cm = pd.concat([fr[t].close.rename(t) for t in self.tick], axis=1).reindex(self.hari).ffill().to_numpy()
        self.pilih = ((T.ent >= mula) & ~T.ticker.isin(BERMASALAH)).to_numpy(); self.T = T[self.pilih].reset_index(drop=True)
        self.tk = self.T.ticker.map(tid).to_numpy(); self.e_open = self.T.buka.to_numpy()
        self.ent_i = self.hari.get_indexer(self.T.ent)
        cap = lambda d: np.minimum(self.hari.searchsorted(pd.DatetimeIndex(d)), len(self.hari) - 1)
        self.ex_i = {1: cap(self.T.ex), 2: cap(self.T.ex2)}
        self.ret = {1: self.T.ret.to_numpy(float), 2: self.T.ret2.to_numpy(float)}

    def jalan(self, L, skor, tapis=None, benih=0, slots=SLOT, w=W):
        ok = np.ones(len(self.T), bool) if tapis is None else np.asarray(tapis, bool)
        q = np.flatnonzero(ok & (self.ent_i >= 0))
        bunyi = np.random.default_rng(benih).random(len(q))
        q = q[np.lexsort((bunyi, -np.nan_to_num(np.asarray(skor, float)[q], nan=-1e18), self.ent_i[q]))]
        cut = np.searchsorted(self.ent_i[q], np.arange(len(self.hari) + 1))
        susun = [q[cut[d]:cut[d + 1]] for d in range(len(self.hari))]
        cv, npos, ambil = portfolio(self.ent_i, self.ex_i[L], self.ret[L], self.tk, self.e_open, susun, self.Cm, slots, w)
        return pd.Series(cv, self.hari), npos, ambil


def cagr(s):
    y = (s.index[-1] - s.index[0]).days / 365.25; return (s.iloc[-1] / s.iloc[0]) ** (1 / y) - 1


def metrik(cv, npos, P, L, ambil):
    T = P.T.iloc[ambil]; r = P.ret[L][ambil]; ex = r - T[f'spy{L}'].to_numpy()
    h1 = cv[cv.index <= H1_AKHIR]; h2 = cv[cv.index > H1_AKHIR]
    mdd = (cv / cv.cummax() - 1).min(); c = cagr(cv)
    hari = (P.ex_i[L][ambil] - P.ent_i[ambil] + 1)
    return dict(cagr=c, mdd=mdd, mar=c / abs(mdd), h1=cagr(h1), h2=cagr(pd.concat([h1.iloc[-1:], h2])),
                n=len(ambil), menang=(r > 0).mean(), purata=r.mean(), lebih_spy=np.nanmean(ex), hari=hari.mean(),
                slot=npos.mean())


def skor_wf(T, L, hari=365, nmin=10):
    """Purata lebihan SPY dagangan kaedah (cara keluar L) yang sudah keluar dalam 12 bulan sebelum tutup hari isyarat."""
    ex = T[f'ex{L}' if L == 2 else 'ex'].to_numpy('datetime64[ns]').copy(); ex[T[f'akhir{L}'].to_numpy()] = JAUH
    x = (T['ret' if L == 1 else 'ret2'] - T[f'spy{L}']).to_numpy(float); s = T.sig.to_numpy('datetime64[ns]')
    out = np.full(len(T), np.nan)
    for _, ix in T.groupby('mid').indices.items():
        o = np.argsort(ex[ix]); e = ex[ix][o]; cs = np.r_[0.0, np.cumsum(np.nan_to_num(x[ix][o]))]
        hi = np.searchsorted(e, s[ix], 'right'); lo = np.searchsorted(e, s[ix] - np.timedelta64(hari, 'D'), 'right')
        k = hi - lo; v = (cs[hi] - cs[lo]) / np.maximum(k, 1); v[k < nmin] = np.nan; out[ix] = v
    return out


def peraturan(T, L):
    pk = lambda v: pd.Series(v).rank(pct=True).to_numpy()
    wf = skor_wf(T, L)
    x = (T['ret' if L == 1 else 'ret2'] - T[f'spy{L}'])
    statik = T.mid.map(x.groupby(T.mid).mean()).to_numpy()
    rs = T.rs.fillna(50).to_numpy(); ind = T.ind_skor.fillna(50).to_numpy()
    sah = ((T.rs >= 80) & (T.mutlak12 > 0) & (T.mansfield > 0) & T.spy_atas.astype(bool)).to_numpy()
    gab = (pk(np.nan_to_num(wf)) + pk(rs) + pk(ind) + pk(T.konsensus.to_numpy())) / 4
    return {'Konsensus kaedah': T.konsensus.to_numpy(float), 'RS pasaran': rs, 'RS disahkan dahulu': rs + 100 * sah,
            'Industri v2': ind, 'Kaedah walk-forward 12 bulan': np.nan_to_num(wf), 'Momentum 6 bulan': T.mom126.to_numpy(),
            'Volatiliti rendah (ATR%)': -T.atrp.to_numpy(), 'Volatiliti tinggi (ATR%)': T.atrp.to_numpy(),
            'Gabungan (kaedah WF + RS + industri + konsensus)': gab,
            'Kaedah statik (pandang hadapan, rujukan)': statik}


def cmd_semak(a):
    """Enjin kajian lawan enjin.portfolio (8 slot x 12.5%, susun rank) bagi beberapa kaedah: CAGR mesti hampir sama."""
    sys.path.insert(0, KOD); import enjin
    T = pd.read_pickle(f'{OUT}/calon.pkl'); fr, _ = muat()
    for mid in a.kaedah:
        Tm = T[T.mid == mid].reset_index(drop=True)
        ref = enjin.portfolio(Tm.assign(ret=Tm.ret), fr, slots=8, w=0.125)
        P = Pasar(Tm, fr, mula=pd.Timestamp(enjin.START))
        cv, _, _ = P.jalan(1, P.T['rank'].to_numpy(float), slots=8, w=0.125)
        print(mid, 'enjin.portfolio CAGR %.4f | kajian %.4f' % (cagr(ref), cagr(cv)), flush=True)


def cmd_sim(a):
    T = pd.read_pickle(f'{OUT}/calon.pkl'); fr, idx = muat(); P = Pasar(T, fr)
    rejim = P.T.spy_atas.astype(bool).to_numpy(); rows = []; kurva = {}
    for L in (1, 2):
        R = {k: v[P.pilih] for k, v in peraturan(T, L).items()}      # skor walk-forward guna sejarah sebelum MULA
        for rj in (False, True):
            tp = rejim if rj else None
            for b in range(BENIH):
                cv, npos, ambil = P.jalan(L, np.zeros(len(P.T)), tp, benih=b)
                rows.append(dict(peraturan='Rawak', benih=b, L=L, rejim=rj, slot_n=SLOT, **metrik(cv, npos, P, L, ambil)))
            for nama, sk in R.items():
                cv, npos, ambil = P.jalan(L, sk, tp)
                rows.append(dict(peraturan=nama, benih=-1, L=L, rejim=rj, slot_n=SLOT, **metrik(cv, npos, P, L, ambil)))
                kurva[(nama, L, rj)] = cv
            print('L', L, 'rejim', rj, 'siap', flush=True)
        for slots in (5, 20):
            for nama in ('Rawak', 'Kaedah walk-forward 12 bulan', 'Gabungan (kaedah WF + RS + industri + konsensus)', 'RS pasaran'):
                for b in (range(10) if nama == 'Rawak' else [0]):
                    sk = np.zeros(len(P.T)) if nama == 'Rawak' else R[nama]
                    cv, npos, ambil = P.jalan(L, sk, None, benih=b, slots=slots, w=1 / slots)
                    rows.append(dict(peraturan=nama, benih=b if nama == 'Rawak' else -1, L=L, rejim=False, slot_n=slots,
                                     **metrik(cv, npos, P, L, ambil)))
    D = pd.DataFrame(rows); D.to_pickle(f'{OUT}/portfolio.pkl')
    spy = idx['SPY'].close; spy = spy[spy.index >= MULA]; kurva[('SPY', 0, False)] = spy / spy.iloc[0]
    pickle.dump(kurva, open(f'{OUT}/kurva.pkl', 'wb'))


def cmd_tahan(a):
    """Ketahanan bias set 431 (senarai hari ini = pemenang diketahui): buang N saham pulangan tertinggi tempoh kajian
    (dipilih dengan pandang hadapan) dan ulang; tumpuan untung 5 saham teratas."""
    T = pd.read_pickle(f'{OUT}/calon.pkl'); fr, _ = muat(); P = Pasar(T, fr)
    jum = pd.Series({t: g.close.iloc[-1] / g.close[g.index >= MULA].iloc[0] - 1 for t, g in fr.items() if (g.index >= MULA).any() and t not in BERMASALAH})
    atas = list(jum.sort_values(ascending=False).index)
    print('20 saham pulangan tertinggi:', ', '.join(f'{t} {100 * jum[t]:.0f}%' for t in atas[:20]), flush=True)
    pilih = ['RS pasaran', 'Volatiliti tinggi (ATR%)', 'Momentum 6 bulan', 'Industri v2', 'Kaedah walk-forward 12 bulan',
             'Gabungan (kaedah WF + RS + industri + konsensus)']
    rows = []
    for L in (1, 2):
        R = {k: v[P.pilih] for k, v in peraturan(T, L).items() if k in pilih}
        for nb in (0, 20, 40):
            tp = ~P.T.ticker.isin(atas[:nb]).to_numpy()
            r = []
            for b in range(20):
                cv, npos, ambil = P.jalan(L, np.zeros(len(P.T)), tp, benih=b); r.append(metrik(cv, npos, P, L, ambil))
            r = pd.DataFrame(r)
            rows.append(dict(L=L, buang=nb, peraturan='Rawak (median 20 benih)', **r.median().to_dict(), tumpuan5=np.nan,
                             cagr_pct_rawak=np.nan, h1_pct_rawak=np.nan, h2_pct_rawak=np.nan))
            for nama, sk in R.items():
                cv, npos, ambil = P.jalan(L, sk, tp); m = metrik(cv, npos, P, L, ambil)
                u = pd.Series(portfolio.amaun * P.ret[L][ambil]).groupby(P.T.ticker.to_numpy()[ambil]).sum()
                rows.append(dict(L=L, buang=nb, peraturan=nama, **m, tumpuan5=u.nlargest(5).sum() / u.sum(),
                                 **{f'{k}_pct_rawak': 100 * (r[k] < m[k]).mean() for k in ('cagr', 'h1', 'h2')},
                                 atas5=', '.join(u.nlargest(5).index)))
            print('L', L, 'buang', nb, 'siap', flush=True)
    D = pd.DataFrame(rows); D.to_csv(os.path.join(BS2, 'kajian', 'portfolio', 'ketahanan.csv'), index=False, float_format='%.5f')
    pd.set_option('display.width', 250)
    for (L, nb), G in D.groupby(['L', 'buang']):
        Y = G.drop(columns=['L', 'buang']).copy()
        for c in ('cagr', 'mdd', 'h1', 'h2', 'menang', 'purata', 'lebih_spy', 'tumpuan5'): Y[c] = 100 * Y[c]
        print(f'\n== L{L}, buang {nb} saham teratas, 10 slot')
        print(Y[['peraturan', 'cagr', 'mdd', 'mar', 'h1', 'h2', 'lebih_spy', 'tumpuan5', 'cagr_pct_rawak', 'h1_pct_rawak',
                 'h2_pct_rawak', 'atas5']].set_index('peraturan').round(1).to_string())


# ---------------------------------------------------------------- 2b. PLAYBOOK_10 / RAWAK_PADAN_10 dalam sampel
def calon_playbook(T, fr, idx, PS):
    """Calon dalam sampel (pra-daftar §8): satu calon setiap (saham, sesi masuk) daripada dagangan enjin, ciri pada tutup hari
    isyarat (data_mentah), RS rs_pasaran_431, gred industri v2 daripada ind_skor (E = skor <= 20), earnings
    tarikh_pendapatan.csv, rejim SPY index_benchmark. Pulang (semua calon dengan lajur gagal, calon lulus untuk bina_pb)."""
    sys.path.insert(0, os.path.join(BS2, 'standard'))
    from gred_kumpulan import gred
    from sektor_pasaran import SEKTOR_INDUSTRI
    T = T[(T.ent >= MULA) & ~T.ticker.isin(BERMASALAH)]
    C = (T.groupby(['ticker', 'ent']).agg(sig=('sig', 'max'), buka=('buka', 'first'), rs=('rs', 'first'),
                                          ind_skor=('ind_skor', 'first'), industri=('industri', 'first'),
                                          bil_kaedah=('mid', 'nunique')).reset_index())
    F = []
    for t, g in C.groupby('ticker'):
        F.append(PS.ciri_siri(fr[t]).reindex(g.sig.to_numpy()).set_axis(g.index))
    C = C.join(pd.concat(F))
    sc = idx['SPY'].close; sa = (sc > sc.rolling(200).mean())
    C['spy_atas'] = sa.reindex(C.sig.to_numpy()).to_numpy()
    C['gred_industri'] = [gred(x) for x in C.ind_skor]
    C['industri_us'] = C.industri.fillna(''); C['sektor_us'] = [SEKTOR_INDUSTRI.get(i, '') for i in C.industri_us]
    C['jurang'] = C.buka / C.tutup - 1
    C['r_awal'] = (C.buka - (C.tutup - PS.PB['ganda'] * C.atr)) / C.buka
    C['ambil_alih'] = False
    E = pd.read_csv(os.path.join(BS2, 'data', 'pemangkin', 'tarikh_pendapatan.csv'), dtype=str)
    EV = {t: sorted(zip(g.d0.str[:10], g.masa.fillna(''))) for t, g in E.groupby('ticker')}
    sesi = [d.strftime('%Y-%m-%d') for d in sc.index]
    s5 = {s: PS.sesi_selepas(s, PS.PB['earn_sesi'], sesi) for s in {d.strftime('%Y-%m-%d') for d in C.sig}}
    st = []
    for t, s in zip(C.ticker, C.sig.dt.strftime('%Y-%m-%d')):
        if t not in EV:
            st.append('tidak diketahui'); continue
        w = s5[s]; ev = [x for x in EV[t] if s <= x[0] <= w[-1]]
        st.append('ada' if PS.earnings_dekat(s, w, ev) else 'tiada')
    C['earnings'] = st
    C = C.join(PS.tapis_pb(C).add_prefix('gagal_')); C['lulus'] = ~C[[f'gagal_{k}' for k in PS.SEBAB_PB]].any(axis=1)
    L = C[C.lulus]
    L = pd.DataFrame(dict(saham=L.ticker, tarikh_beli=L.ent.dt.strftime('%Y-%m-%d'), tarikh_isyarat=L.sig.dt.strftime('%Y-%m-%d'),
                          id_kaedah=L.bil_kaedah.astype(str), rs=L.rs, harga_beli=L.buka, r_awal=L.r_awal, sektor_us=L.sektor_us,
                          industri_us=L.industri_us)).reset_index(drop=True)
    return C, L


def metrik_pb(R, E, harga, fj):
    """Metrik satu larian bina_pb (dagangan terbuka di hujung dinilai pada tutup akhir)."""
    cv = pd.Series(E.ekuiti.to_numpy(float), pd.to_datetime(E.tarikh))
    h1 = cv[cv.index <= H1_AKHIR]; h2 = cv[cv.index > H1_AKHIR]; mdd = (cv / cv.cummax() - 1).min(); c = cagr(cv)
    kel = R.status.eq('Keluar').to_numpy()
    u = np.where(kel, R.untung_pct.to_numpy(float) / 100, R.harga_terkini.to_numpy(float) / R.harga_beli.to_numpy(float) * fj - 1)
    rm = u / R.r_awal.to_numpy(float)
    akhir = E.tarikh.iloc[-1]
    hari = [harga[s].ix.get(t if k else akhir, len(harga[s].t) - 1) - harga[s].ix[b] + 1
            for s, b, t, k in zip(R.saham, R.tarikh_beli, R.tarikh_keluar, kel)]
    x = np.r_[1.0, cv.to_numpy()]; bawah = cur = 0
    for v in x < np.maximum.accumulate(x) - 1e-12:
        cur = cur + 1 if v else 0; bawah = max(bawah, cur)
    un = pd.Series(R.amaun.to_numpy(float) * u).groupby(R.saham.to_numpy()).sum()
    sb = R.sebab_keluar.fillna('').value_counts(normalize=True)
    bk = E.tarikh[E.brek == 1]; ks = E.tarikh[E.kill_switch == 1]
    return dict(cagr=c, mdd=mdd, mar=c / abs(mdd) if mdd < 0 else np.nan, h1=cagr(h1), h2=cagr(pd.concat([h1.iloc[-1:], h2])),
                n=len(R), menang=(u > 0).mean(), purata=u.mean(), r_purata=rm.mean(), r_median=np.median(rm),
                r_2=(rm >= 2).mean(), r_neg1=(rm <= -1).mean(), hari=np.mean(hari), slot=E.bil_posisi.mean(),
                tunai=(E.tunai / E.ekuiti).mean(), heat_med=E.heat.median(), heat_p90=E.heat.quantile(0.9), heat_maks=E.heat.max(),
                brek=E.brek.mean(), brek_mula=bk.iloc[0] if len(bk) else '', brek_hujung=int(E.brek.iloc[-1]),
                bunuh=ks.iloc[0] if len(ks) else '', bawah_puncak=bawah,
                tumpuan5=un.nlargest(5).sum() / un.sum() if un.sum() > 0 else np.nan,
                k_chandelier=sb.get('chandelier', 0.0), k_masa=sb.get('masa', 0.0))


def tahunan(cv):
    cv = pd.Series(np.asarray(cv, float), pd.to_datetime(cv.index))
    y = cv.resample('YE').last(); y = pd.concat([pd.Series([1.0], [cv.index[0] - pd.Timedelta(days=1)]), y]).pct_change().dropna()
    return (100 * y).round(1).set_axis(y.index.year)


def jadual_bayang(E, PS):
    """Analisis kepekaan (BUKAN pra-daftar): brek dinilai pada lengkung bayang (portfolio sama tanpa brek/kill_switch): brek
    belian pada sesi t+1 jika kejatuhan bayang pada tutup t <= -15%, dilepaskan selepas tutup dengan kejatuhan >= -10%."""
    e = E.ekuiti.to_numpy(float); pk = np.maximum.accumulate(np.r_[1.0, e])[1:]; dd = e / pk - 1
    s, out = False, {}
    for i, t in enumerate(E.tarikh):
        s = True if dd[i] <= PS.PB['brek'] else (False if s and dd[i] >= PS.PB['pulih'] else s)
        if i + 1 < len(E):
            out[E.tarikh.iloc[i + 1]] = s
    return out


VARIAN_PB = ('asas (pra-daftar)', 'tanpa brek dan kill_switch', 'brek lengkung bayang')
_G = {}


def _pb_kerja(t):
    """Satu (set, jenis, benih): tiga varian. Asas = peraturan pra-daftar; dua lagi = analisis kepekaan."""
    PS, lab, jenis, b = _G['PS'], *t
    Ls, hari, harga, fj = _G['L'][lab], _G['hari'], _G['harga'], _G['fj']
    out, kv = [], {}
    R0, E0 = PS.bina_pb(Ls, hari, harga, jenis, benih=b, prm=dict(PS.PB, brek=-9.0, bunuh=-9.0))
    for v in VARIAN_PB:
        if v == VARIAN_PB[1]:
            R, E = R0, E0
        elif v == VARIAN_PB[2]:
            R, E = PS.bina_pb(Ls, hari, harga, jenis, benih=b, prm=dict(PS.PB, brek_luar=jadual_bayang(E0, PS)))
        else:
            R, E = PS.bina_pb(Ls, hari, harga, jenis, benih=b)
        out.append(dict(varian=v, jenis=jenis, set=lab, benih=b, **metrik_pb(R, E, harga, fj)))
        kv[(v, jenis, lab, b)] = pd.Series(E.ekuiti.to_numpy(), pd.to_datetime(E.tarikh))
    return out, kv


def cmd_playbook(a):
    sys.path.insert(0, os.path.join(BS2, 'standard'))
    import portfolio_slot as PS
    from multiprocessing import get_context
    T = pd.read_pickle(f'{OUT}/calon.pkl'); fr, idx = muat()
    C, L = calon_playbook(T, fr, idx, PS)
    fj = (1 - PS.PB['kos']) / (1 + PS.PB['kos'])
    hari = sorted({d.strftime('%Y-%m-%d') for g in fr.values() for d in g.index if d >= MULA})
    harga = {t: PS.Siri(fr[t]) for t in L.saham.unique()}
    jum = pd.Series({t: g.close.iloc[-1] / g.close[g.index >= MULA].iloc[0] - 1 for t, g in fr.items()
                     if (g.index >= MULA).any() and t not in BERMASALAH})
    atas = list(jum.sort_values(ascending=False).index[:40])
    out = os.path.join(BS2, 'kajian', 'portfolio')
    # corong penapis (calon = saham x sesi masuk; gagal tidak eksklusif)
    hc = C.groupby('ent').lulus.sum()
    cor = pd.DataFrame(dict(gagal_pct={k: 100 * C[f'gagal_{k}'].mean() for k in PS.SEBAB_PB}))
    cor.loc['lulus (semua penapis)', 'gagal_pct'] = 100 * C.lulus.mean()
    cor.loc['earnings tidak diketahui', 'gagal_pct'] = 100 * C.earnings.eq('tidak diketahui').mean()
    cor.to_csv(os.path.join(out, 'playbook_corong.csv'), float_format='%.2f')
    print('calon %d, lulus %d (%.2f%%); sesi dengan >= 1 lulus %.1f%%; lulus/sesi median %.0f p90 %.0f' % (
        len(C), C.lulus.sum(), 100 * C.lulus.mean(), 100 * (hc > 0).mean(), hc.median(), hc.quantile(.9)), flush=True)
    print(cor.round(1).to_string(), flush=True)
    _G.update(PS=PS, L={'penuh': L, 'buang 40': L[~L.saham.isin(atas)].reset_index(drop=True)}, hari=hari, harga=harga, fj=fj)
    kerja = [(lab, j, b) for lab in ('penuh', 'buang 40') for j in PS.PB_JENIS for b in range(a.benih)]
    rows, kurva = [], {}
    with get_context('fork').Pool(a.proses) as pool:
        for r, kv in pool.imap_unordered(_pb_kerja, kerja):
            rows += r; kurva.update(kv)
    print('PLAYBOOK / RAWAK_PADAN siap', flush=True)
    # rujukan: RS pasaran (seri rawak, benih 0..) dan rawak 10 x 10% lorong 2, kos 0.1% (peraturan RS_10 / RAWAK_10) dan 0.25%
    P = Pasar(T, fr); r0 = P.ret[2].copy()
    for kos in (COST, PS.PB['kos']):
        P.ret[2] = (1 + r0) * (1 + COST) / (1 - COST) * (1 - kos) / (1 + kos) - 1
        for lab, tp in (('penuh', None), ('buang 40', ~P.T.ticker.isin(atas).to_numpy())):
            for nama, sk in (('RS_10 (RS pasaran 10x10%)', P.T.rs.fillna(50).to_numpy(float)), ('RAWAK_10 (rawak 10x10%)', np.zeros(len(P.T)))):
                for b in range(a.benih):
                    cv, npos, ambil = P.jalan(2, sk, tp, benih=b); m = metrik(cv, npos, P, 2, ambil)
                    rows.append(dict(varian='rujukan', jenis=nama, set=lab, benih=b, kos=kos, cagr=m['cagr'], mdd=m['mdd'], mar=m['mar'],
                                     h1=m['h1'], h2=m['h2'], n=m['n'], menang=m['menang'], purata=m['purata'], hari=m['hari'],
                                     slot=m['slot']))
                    kurva[(f'rujukan kos {100 * kos:.2f}%', nama, lab, b)] = cv
        print('rujukan kos', kos, 'siap', flush=True)
    P.ret[2] = r0
    D = pd.DataFrame(rows); D['kos'] = D['kos'].fillna(PS.PB['kos'])
    D = D.sort_values(['varian', 'jenis', 'set', 'kos', 'benih']).reset_index(drop=True)
    D.to_csv(os.path.join(out, 'playbook.csv'), index=False, float_format='%.5f')
    # ringkasan: median benih; persentil PLAYBOOK (benih 0) lawan 20 benih RAWAK_PADAN varian sama
    S, MJ = [], {}
    for (v, j, lab, kos), G in D.groupby(['varian', 'jenis', 'set', 'kos'], sort=False):
        med = G.drop(columns=['varian', 'jenis', 'set', 'benih', 'kos', 'bunuh', 'brek_mula'], errors='ignore').median(numeric_only=True)
        x = dict(varian=v, jenis=j, set=lab, kos=kos, **med.to_dict(), cagr_p5=G.cagr.quantile(.05), cagr_p95=G.cagr.quantile(.95),
                 mdd_p5=G.mdd.quantile(.05), mdd_p50=G.mdd.quantile(.5), n_benih=len(G))
        if 'bunuh' in G and v != 'rujukan':
            x['bunuh_n'] = int(G.bunuh.fillna('').astype(str).ne('').sum())
            x['brek_n'] = int(G.brek_mula.fillna('').astype(str).ne('').sum()); x['brek_hujung_n'] = int(G.brek_hujung.sum())
            bm = G.brek_mula.fillna('').astype(str); bm = bm[bm != '']
            x['brek_mula_bulan'] = ', '.join(sorted(bm.str[:7].unique())[:6])
        S.append(x)
        if v in ('asas (pra-daftar)', 'rujukan'):
            MJ.setdefault(lab, {})[f'{j}|{kos}'] = [round(100 * G.mdd.quantile(.05), 1), round(100 * G.mdd.quantile(.5), 1)]
    S = pd.DataFrame(S)
    for v in VARIAN_PB:
        for lab in ('penuh', 'buang 40'):
            q = (S.varian == v) & (S.jenis == 'PLAYBOOK_10') & (S.set == lab)
            pb0 = D[(D.varian == v) & (D.jenis == 'PLAYBOOK_10') & (D.set == lab) & (D.benih == 0)].iloc[0]
            rp = D[(D.varian == v) & (D.jenis == 'RAWAK_PADAN_10') & (D.set == lab)]
            S.loc[q, 'pb0_cagr'] = pb0.cagr; S.loc[q, 'pb0_mdd'] = pb0.mdd
            for k in ('cagr', 'h1', 'h2', 'mar'):
                S.loc[q, f'pct_{k}'] = 100 * (rp[k] < pb0[k]).mean()
            S.loc[q, 'pct_mdd'] = 100 * (rp.mdd < pb0.mdd).mean()
            print(f'== {v} | {lab}: PLAYBOOK_10 benih 0 CAGR {100 * pb0.cagr:.1f}% MDD {100 * pb0.mdd:.1f}% | persentil lawan '
                  f'RAWAK_PADAN CAGR {100 * (rp.cagr < pb0.cagr).mean():.0f} H1 {100 * (rp.h1 < pb0.h1).mean():.0f} '
                  f'H2 {100 * (rp.h2 < pb0.h2).mean():.0f} MDD (lebih cetek) {100 * (rp.mdd < pb0.mdd).mean():.0f}', flush=True)
    S.to_csv(os.path.join(out, 'playbook_ringkas.csv'), index=False, float_format='%.5f')
    pd.set_option('display.width', 300); pd.set_option('display.max_columns', 50)
    Y = S.copy()
    for c in ('cagr', 'mdd', 'h1', 'h2', 'menang', 'purata', 'tunai', 'heat_med', 'heat_p90', 'heat_maks', 'brek', 'cagr_p5',
              'cagr_p95', 'mdd_p5', 'mdd_p50', 'tumpuan5', 'k_chandelier', 'k_masa', 'pb0_cagr', 'pb0_mdd', 'r_2', 'r_neg1'):
        if c in Y:
            Y[c] = 100 * Y[c]
    print(Y.round(2).to_string(), flush=True)
    th = {}
    spy = idx['SPY'].close; spy = spy[spy.index >= MULA]
    med = lambda key: pd.DataFrame({b: tahunan(kurva[key + (b,)]) for b in range(a.benih)}).median(axis=1)
    for lab in ('penuh', 'buang 40'):
        for v in VARIAN_PB:
            th[f'PLAYBOOK_10 benih 0 | {v} | {lab}'] = tahunan(kurva[(v, 'PLAYBOOK_10', lab, 0)])
            th[f'PLAYBOOK_10 median benih | {v} | {lab}'] = med((v, 'PLAYBOOK_10', lab))
            th[f'RAWAK_PADAN_10 median benih | {v} | {lab}'] = med((v, 'RAWAK_PADAN_10', lab))
        for nama in ('RS_10 (RS pasaran 10x10%)', 'RAWAK_10 (rawak 10x10%)'):
            th[f'{nama} kos 0.25% median benih | {lab}'] = med(('rujukan kos 0.25%', nama, lab))
    th['SPY'] = tahunan(spy / spy.iloc[0])
    th = pd.DataFrame(th).T
    th.to_csv(os.path.join(out, 'playbook_tahunan.csv'))
    print('\n== Pulangan tahunan % (2020 = Nov–Dis; 2026 hingga Okt)'); print(th.round(1).to_string())
    peta = {'PLAYBOOK_10': f'PLAYBOOK_10|{PS.PB["kos"]}', 'RAWAK_PADAN_10': f'RAWAK_PADAN_10|{PS.PB["kos"]}',
            'RS_10': f'RS_10 (RS pasaran 10x10%)|{COST}', 'RAWAK_10': f'RAWAK_10 (rawak 10x10%)|{COST}'}
    J = dict(dijana=pd.Timestamp.now(tz='Asia/Kuala_Lumpur').strftime('%Y-%m-%d %H:%M MYT'),
             sumber='kajian/portfolio/kaji_portfolio.py playbook (dalam sampel, set 431 tolak 8, masuk Nov 2020 – Okt 2026; alam penyintas)',
             takrif=f'MDD % keseluruhan tempoh Nov 2020 – Okt 2026 merentas {a.benih} benih (RAWAK: susunan; RS_10/PLAYBOOK: pecah seri): '
                    '[p5, p50]. RS_10/RAWAK_10 = 10 x 10% lorong 2 kos 0.1%; PLAYBOOK_10/RAWAK_PADAN_10 = peraturan pra-daftar kos 0.25%.',
             penuh={k: MJ['penuh'][v] for k, v in peta.items() if v in MJ['penuh']},
             buang40={k: MJ['buang 40'][v] for k, v in peta.items() if v in MJ['buang 40']})
    with open(os.path.join(out, 'mdd_jangka.json'), 'w', encoding='utf-8') as f:
        json.dump(J, f, ensure_ascii=False, indent=1)
    print(json.dumps(J, ensure_ascii=False, indent=1))


# ---------------------------------------------------------------- 3. ringkasan
def cmd_ringkas(a):
    D = pd.read_pickle(f'{OUT}/portfolio.pkl'); kurva = pickle.load(open(f'{OUT}/kurva.pkl', 'rb'))
    spy = kurva[('SPY', 0, False)]; h1 = spy[spy.index <= H1_AKHIR]
    print('SPY CAGR %.1f%% | H1 %.1f%% | H2 %.1f%% | MDD %.1f%%' % (100 * cagr(spy), 100 * cagr(h1),
          100 * cagr(spy[spy.index >= h1.index[-1]]), 100 * (spy / spy.cummax() - 1).min()))
    pd.set_option('display.width', 250)
    out = os.path.join(BS2, 'kajian', 'portfolio'); B = []
    for (L, rj, sn), G in D.groupby(['L', 'rejim', 'slot_n']):
        r = G[G.peraturan == 'Rawak']
        if r.empty: continue
        lain = G[G.peraturan != 'Rawak'].copy()
        for k in ('cagr', 'mar', 'h1', 'h2'):
            lain[f'{k}_pct_rawak'] = [100 * (r[k] < v).mean() for v in lain[k]]
        rw = r.drop(columns=['peraturan', 'benih']).median(numeric_only=True)
        rw['peraturan'] = f'Rawak (median {len(r)} benih; p5–p95 CAGR {100 * r.cagr.quantile(.05):.1f}–{100 * r.cagr.quantile(.95):.1f}%)'
        X = pd.concat([pd.DataFrame([rw]), lain], ignore_index=True)
        X['L'], X['rejim'], X['slot_n'] = L, rj, sn
        B.append(X)
        cols = ['peraturan', 'cagr', 'mdd', 'mar', 'h1', 'h2', 'n', 'menang', 'purata', 'lebih_spy', 'hari', 'slot', 'cagr_pct_rawak', 'h1_pct_rawak', 'h2_pct_rawak']
        Y = X[[c for c in cols if c in X]].copy()
        for c in ('cagr', 'mdd', 'h1', 'h2', 'menang', 'purata', 'lebih_spy'): Y[c] = 100 * Y[c]
        print(f"\n== Keluar L{L} ({'kaedah' if L == 1 else 'Chandelier'}), rejim SPY>SMA200 {'YA' if rj else 'tidak'}, {sn} slot")
        print(Y.set_index('peraturan').round(2).to_string())
    pd.concat(B, ignore_index=True).to_csv(os.path.join(out, 'keputusan.csv'), index=False, float_format='%.5f')
    th = {}
    for (nama, L, rj), cv in kurva.items():
        if nama == 'SPY' or (not rj and nama in ('Gabungan (kaedah WF + RS + industri + konsensus)', 'Kaedah walk-forward 12 bulan', 'RS pasaran', 'Kaedah statik (pandang hadapan, rujukan)')):
            y = cv.resample('YE').last(); y = pd.concat([cv.iloc[:1], y]).pct_change().dropna()
            th[f'{nama} L{L}' if nama != 'SPY' else 'SPY'] = (100 * y).round(1).set_axis(y.index.year)
    th = pd.DataFrame(th).T; print('\n== Pulangan tahunan % (2020 = Nov–Dis; 2026 hingga Okt)'); print(th.to_string())
    th.to_csv(os.path.join(out, 'tahunan.csv'))


if __name__ == '__main__':
    ap = argparse.ArgumentParser(); s = ap.add_subparsers(dest='cmd', required=True)
    x = s.add_parser('sedia'); x.add_argument('--kumpulan', default=f'{OUT}/kumpulan_harian.csv.gz'); x.set_defaults(f=cmd_sedia)
    x = s.add_parser('semak'); x.add_argument('--kaedah', nargs='+', default=['M03', 'M27', 'M119']); x.set_defaults(f=cmd_semak)
    s.add_parser('sim').set_defaults(f=cmd_sim); s.add_parser('ringkas').set_defaults(f=cmd_ringkas)
    s.add_parser('tahan').set_defaults(f=cmd_tahan)
    x = s.add_parser('playbook'); x.add_argument('--benih', type=int, default=20); x.add_argument('--proses', type=int, default=4)
    x.set_defaults(f=cmd_playbook)
    a = ap.parse_args(); a.f(a)
