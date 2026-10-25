# ENJIN KAJIAN v1.3 (kajian PIT, 25 Okt 2026) — salinan `kod/enjin.py` v1.2 dengan pembaikan BERLABEL sahaja.
# v1.2 kekal BEKU dan tidak diubah; enjin ini hanya untuk kajian `kajian/pit/` (pra-daftar: PRA_DAFTAR.md §4).
#   [B1] Jurang hari masuk: jika buka hari masuk <= henti, keluar pada buka itu (sebab 'henti'). v1.2 hanya menyemak
#        rendah <= henti pada hari masuk dan keluar pada paras henti walaupun buka di bawahnya (untung palsu).
#   [B2] Kos 0.25% setiap sisi (formula sama dengan v1.2: x/e*(1-k)/(1+k)-1).
#   [B3] Delist: posisi yang masih terbuka pada bar terakhir ticker yang tamat SEBELUM tarikh akhir data -> keluar pada
#        tutup terakhir (sebab 'delist'); posisi terbuka pada tarikh akhir data -> 'hujung' (dinilai pada tutup akhir).
#   [B4] Tetingkap mula/akhir sebagai parameter (bukan START tetap); portfolio() boleh memulangkan senarai dagangan yang
#        benar-benar diambil (metrik dagangan atas dagangan portfolio dan atas semua isyarat).
#   [B5] Jenis harga keluar direkod dalam lajur 'jenis' ('buka' / 'intrahari' / 'tutup') untuk penanda aras rawak.
# Selain itu logik sama dengan v1.2: 8 slot x 12.5%, rank tertinggi dahulu, satu posisi setiap ticker, posisi yang keluar
# pada hari masuk ditutup pada hari itu, sasaran tidak disemak pada hari masuk, exitc -> buka esok, TMAX -> tutup.
# Kesetaraan: trades(kos=0.001, jurang=False) dan portfolio(mula=v1.2 START) = v1.2 tepat (ujian/test_pit_enjin.py);
# dengan jurang=True hasil juga sama apabila tiada jurang hari masuk di bawah henti.
import numpy as np, pandas as pd

COST = 0.0025                      # [B2]
COST_V12 = 0.001                   # kos v1.2 (mod setara / diagnostik)
START_V12 = '2019-11-01'
ENJIN = 'v1.3-kajian'
LAJUR_T = ['ticker', 'sig', 'ent', 'ex', 'ret', 'days', 'why', 'rank', 'mfe', 'jenis']


def rsi(c, n=14):
    dl = c.diff(); au = dl.clip(lower=0).ewm(alpha=1 / n, adjust=False).mean()
    ad = (-dl.clip(upper=0)).ewm(alpha=1 / n, adjust=False).mean(); return 100 - 100 / (1 + au / ad)


def atr(g, n=14):
    c = g.close; tr = pd.concat([g.high - g.low, (g.high - c.shift()).abs(), (g.low - c.shift()).abs()], axis=1).max(axis=1)
    return tr.rolling(n).mean()


def siap(g):
    for k, v in [('sig', False), ('stop', np.nan), ('tgt', np.nan), ('exitc', False), ('rank', 0.0)]:
        if k not in g: g[k] = v
    return g


def trades(fr, tmax=None, warm=200, kos=COST, jurang=True, akhir_data=None, sig=None):
    """Dagangan semua isyarat (tidak bertindih bagi ticker sama), seperti v1.2 + [B1][B2][B3][B5].
    akhir_data: tarikh akhir data global (Timestamp); ticker yang bar terakhirnya lebih awal dianggap delist [B3].
    sig: pilihan dict ticker -> ndarray bool menggantikan g.sig (topeng alam; tanpa mengubah bingkai). Ticker dalam fr
    yang tiada dalam sig dilangkau."""
    out = []
    akhir_data = None if akhir_data is None else pd.Timestamp(akhir_data)
    gs = sig
    for t, g in fr.items():
        if gs is not None and t not in gs: continue
        g = siap(g); o, h, l, c = g.open.values, g.high.values, g.low.values, g.close.values
        sig = g.sig.fillna(False).astype(bool).values if gs is None else gs[t]
        st = g.stop.astype(float).values; tg = g.tgt.astype(float).values
        ex = g.exitc.fillna(False).astype(bool).values; rk = g['rank'].astype(float).values; ix = g.index; n = len(g); i = warm
        delist = akhir_data is not None and n > 0 and ix[n - 1] < akhir_data
        while i < n - 1:
            if not sig[i]: i += 1; continue
            e = o[i + 1]; sp = st[i] if not np.isnan(st[i]) else -np.inf
            j = i + 1; x = None; why = 'hujung'; jenis = 'tutup'
            if jurang and o[i + 1] <= sp:                       # [B1] buka hari masuk sudah di bawah henti
                x, why, jenis = o[i + 1], 'henti', 'buka'
            else:
                while j < n:
                    tgt = tg[j - 1] if j > i + 1 else np.nan
                    if j > i + 1 and o[j] <= sp: x, why, jenis = o[j], 'henti', 'buka'; break
                    if l[j] <= sp: x, why, jenis = sp, 'henti', 'intrahari'; break
                    if not np.isnan(tgt):
                        if j > i + 1 and o[j] >= tgt: x, why, jenis = o[j], 'sasaran', 'buka'; break
                        if h[j] >= tgt: x, why, jenis = tgt, 'sasaran', 'intrahari'; break
                    if ex[j] and j + 1 < n: j += 1; x, why, jenis = o[j], 'isyarat keluar', 'buka'; break
                    if tmax and (j - i) >= tmax: x, why, jenis = c[j], 'masa', 'tutup'; break
                    j += 1
            if x is None:
                j = n - 1; x = c[j]; jenis = 'tutup'
                if delist: why = 'delist'                       # [B3]
            out.append(dict(ticker=t, sig=ix[i], ent=ix[i + 1], ex=ix[j], ret=x / e * (1 - kos) / (1 + kos) - 1, days=j - i,
                            why=why, rank=rk[i], mfe=h[i + 1:j + 1].max() / e - 1, jenis=jenis))
            i = j + 1
    return pd.DataFrame(out, columns=LAJUR_T)


def portfolio(T, fr, slots=8, w=0.125, mula=START_V12, akhir=None, pulang_dagangan=False):
    """Logik v1.2 (8 slot x 12.5%, rank tertinggi dahulu, satu posisi setiap ticker) dengan tetingkap [B4].
    Harga penilaian = tutup terakhir <= tarikh (setara Series.asof v1.2), dipraKira sekali bagi kelajuan.
    pulang_dagangan=True -> (keluk, DataFrame dagangan yang diambil: baris T asal + lajur 'a' (amaun masuk))."""
    mula = pd.Timestamp(mula)
    # = sorted(set().union(*indeks)) v1.2 (kesatuan tarikh semua ticker), dikira dengan np.unique
    D = pd.DatetimeIndex(np.unique(np.concatenate([g.index.values for g in fr.values()]))) if fr else pd.DatetimeIndex([])
    D = D[D >= mula]
    if akhir is not None:
        D = D[D <= pd.Timestamp(akhir)]
    T = T[T.ent >= mula]
    if akhir is not None:
        T = T[T.ent <= pd.Timestamp(akhir)]
    T = T.sort_values(['ent', 'rank'], ascending=[True, False])
    byent = {k: v for k, v in T.groupby('ent')}
    perlu = set(T.ticker); cl = {}
    # asof v1.2: nilai terakhir <= tarikh walaupun tarikh itu bukan bar ticker (ffill atas indeks gabungan) — sama.
    for t in perlu:
        s = fr[t].close.astype(float).dropna()
        cl[t] = s.reindex(D, method='ffill').values
    eq = cash = 1.0; pos = []; curve = []; diambil = []
    for k, dt in enumerate(D):
        keep = []
        for p in pos:
            if p['ex'] == dt: cash += p['a'] * (1 + p['ret'])
            else: keep.append(p)
        pos = keep
        if dt in byent:
            for r in byent[dt].itertuples():
                if len(pos) >= slots: break
                if any(p['t'] == r.ticker for p in pos): continue
                a = min(cash, eq * w)
                if a <= 0: break
                cash -= a; pos.append(dict(t=r.ticker, ex=r.ex, ret=r.ret, a=a, ent=dt, ke=k))
                diambil.append((r.Index, a))
        keep = []
        for p in pos:                      # v1.2: tutup posisi yang keluar pada hari masuk
            if p['ex'] == dt and p['ent'] == dt: cash += p['a'] * (1 + p['ret'])
            else: keep.append(p)
        pos = keep
        mv = sum(p['a'] * cl[p['t']][k] / cl[p['t']][p['ke']] if p['ent'] != dt else p['a'] for p in pos)
        eq = cash + mv; curve.append((dt, eq))
    cv = pd.Series(dict(curve))
    if not pulang_dagangan:
        return cv
    if diambil:
        ii, aa = zip(*diambil)
        P = T.loc[list(ii)].copy(); P['a'] = list(aa)
    else:
        P = T.iloc[0:0].copy(); P['a'] = []
    return cv, P


def _cagr(s):
    y = (s.index[-1] - s.index[0]).days / 365.25; return (s.iloc[-1] / s.iloc[0]) ** (1 / y) - 1


def _mdd(s): return (s / s.cummax() - 1).min()
