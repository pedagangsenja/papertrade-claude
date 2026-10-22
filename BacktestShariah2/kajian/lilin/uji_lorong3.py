"""Lorong 3: keluar carta alternatif (Heikin-Ashi, HA dilicinkan, Renko, Kagi, Point & Figure, Line Break) lawan
Chandelier tutup 4×ATR14 lorong 2 (`standard/keluar_lorong.py`) atas kolam isyarat AUTOTUNE 2000 saham AS.

Reka bentuk dipradaftar (ditulis sebelum keputusan) dalam
`kajian/research_notes/Ujian lilin atas 2000 saham/lorong3_keluar.md`; skrip ini melaksanakannya tanpa pindaan.

Ringkas:
  - Kemasukan = dagangan laluan 1 (`dagangan_enjin`) kolam `kolam.parquet`; beli pada buka bar k (hari masuk).
    (U) unik ikut (ticker, entry_date) — analisis utama; (K) semua dagangan, pemberat 1/n kaedah dalam setiap sampel.
  - Setiap varian: isyarat pada TUTUP bar j >= k -> jual pada BUKA j+1; had 60 hari dagangan (tutup bar k+59;
    isyarat pada bar itu diutamakan, seperti enjin_at had60); data tamat -> tutup terakhir. Laporan sekunder had 120.
  - ATR14 = `keluar_lorong.atr`; "dibeku" A0 = ATR14 bar k−1.
  - Kos setiap sisi = lajur `kos` kolam; pulangan = X/e × (1−kos)/(1+kos) − 1.

Guna (dari akar repo; perlu numba; 1 proses, < 3 GB):
  python3 BacktestShariah2/kajian/lilin/uji_lorong3.py sim       -> keluar setiap varian (npz, dicheckpoint)
  python3 BacktestShariah2/kajian/lilin/uji_lorong3.py semak     -> CH4 tanpa had lawan keluar_lorong.lorong_henti
  python3 BacktestShariah2/kajian/lilin/uji_lorong3.py ringkas   -> metrik, t berkelompok, sempadan, peraturan lulus
  python3 BacktestShariah2/kajian/lilin/uji_lorong3.py jadual    -> jadual.md daripada hasil.json
Output: /tmp/claude-0/-home-user-papertrade-claude/0793050f-2ee1-522e-9bf0-b633a13089db/scratchpad/lilin/lorong3/
Tiada fail di bawah AUTOTUNE/, BacktestShariah2/kod/, standard/ atau data/ diubah (dibaca/diimport sahaja).
"""
import argparse, json, os, sys, time

os.environ.setdefault('NUMBA_CACHE_DIR', '/tmp/claude-0/-home-user-papertrade-claude/0793050f-2ee1-522e-9bf0-b633a13089db/scratchpad/numba')
import numpy as np
import pandas as pd
from numba import njit

AKAR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
for p in (os.path.join(AKAR, 'AUTOTUNE', 'teras'), os.path.join(AKAR, 'BacktestShariah2', 'standard')):
    if p not in sys.path: sys.path.insert(0, p)
import data as D            # noqa: E402  AUTOTUNE/teras/data.py
import keluar_lorong as KL  # noqa: E402  standard/keluar_lorong.py (atr, lorong_henti)

CACHE = os.path.join(AKAR, 'AUTOTUNE', '.cache')
SP = '/tmp/claude-0/-home-user-papertrade-claude/0793050f-2ee1-522e-9bf0-b633a13089db/scratchpad/lilin'
KOLAM = os.path.join(SP, 'kolam.parquet')
OUT = os.path.join(SP, 'lorong3')

# nama -> (jenis, p1, p2). Jenis: 1 Chandelier tutup ATR bergerak (paras naik); 2 Renko; 3 Kagi; 4 P&F; 5 Line Break;
# 6 HA mentah N merah berturut; 7 HA dilicinkan EMA20 tukar warna.
VARIAN = {
    'CH4': (1, 4.0, 0.0), 'CH3': (1, 3.0, 0.0), 'CH5': (1, 5.0, 0.0),
    'RENKO_1x_2': (2, 1.0, 2.0), 'RENKO_2x_2': (2, 2.0, 2.0), 'RENKO_1x_4': (2, 1.0, 4.0),
    'KAGI3': (3, 3.0, 0.0), 'KAGI4': (3, 4.0, 0.0), 'KAGI5': (3, 5.0, 0.0),
    'PF_1x_3': (4, 1.0, 3.0),
    'LB3': (5, 3.0, 0.0), 'LB4': (5, 4.0, 0.0),
    'HA2': (6, 2.0, 0.0), 'HA3': (6, 3.0, 0.0),
    'SHA20': (7, 20.0, 0.0),
}
CALON = [v for v in VARIAN if not v.startswith('CH')]
HAD = (60, 120)


# ---------------------------------------------------------------- penunjuk (rata, ikut segmen ticker)
@njit(cache=True)
def _ha(o, h, l, c, mula, akhir):
    """Heikin-Ashi mentah: HAc=(O+H+L+C)/4; HAo=(HAo₋₁+HAc₋₁)/2, benih (O+C)/2 pada bar sah pertama. Bar NaN
    -> NaN, keadaan dibawa."""
    n = len(o); hao = np.full(n, np.nan); hac = np.full(n, np.nan)
    for t in range(len(mula)):
        po = np.nan; pc = np.nan
        for i in range(mula[t], akhir[t]):
            if np.isnan(o[i]) or np.isnan(h[i]) or np.isnan(l[i]) or np.isnan(c[i]):
                continue
            hc = (o[i] + h[i] + l[i] + c[i]) / 4.0
            ho = (o[i] + c[i]) / 2.0 if np.isnan(po) else (po + pc) / 2.0
            hao[i] = ho; hac[i] = hc; po = ho; pc = hc
    return hao, hac


@njit(cache=True)
def _ema(x, mula, akhir, n):
    """EMA (alpha 2/(n+1), adjust=False), benih nilai sah pertama; NaN dilangkau (keadaan dibawa)."""
    a = 2.0 / (n + 1.0); y = np.full(len(x), np.nan)
    for t in range(len(mula)):
        s = np.nan
        for i in range(mula[t], akhir[t]):
            if np.isnan(x[i]):
                continue
            s = x[i] if np.isnan(s) else a * x[i] + (1 - a) * s
            y[i] = s
    return y


def sha(o, h, l, c, mula, akhir, n=20):
    """HA dilicinkan: O',H',L',C' = EMA n; HA atas O'..C'; kemudian EMA n bagi HAo', HAc'."""
    eo, eh, el, ec = (_ema(x, mula, akhir, n) for x in (o, h, l, c))
    ho, hc = _ha(eo, eh, el, ec, mula, akhir)
    return _ema(ho, mula, akhir, n), _ema(hc, mula, akhir, n)


# ---------------------------------------------------------------- simulasi keluar
@njit(cache=True)
def sim(o, c, atr, hao, hac, sho, shc, ks, ends, a0, jenis, p1, p2, tmax):
    """Setiap kemasukan q: bar beli ks[q], bar terakhir data ticker ends[q] (eksklusif), A0 = a0[q].
    Pulang J (bar keluar), X (harga keluar), jenis keluar (0 buka selepas isyarat, 1 tutup had masa,
    2 tutup data tamat), puncak (tutup tertinggi semasa pegang termasuk X)."""
    m = len(ks); J = np.empty(m, np.int64); X = np.empty(m); W = np.empty(m, np.int8); PK = np.empty(m)
    tops = np.empty(4096)
    for q in range(m):
        k = ks[q]; n = ends[q]; A0 = a0[q]; e = o[k]
        hc = -1e300; lv = -1e300; mc = -1e300
        T = c[k]; b = p1 * A0                       # Renko
        top = np.floor(c[k] / A0) * A0 if jenis == 4 else 0.0
        nt = 1; tops[0] = c[k]                      # Line Break: tops[0] = C_k
        merah = 0
        selesai = False
        for j in range(k, n):
            cj = c[j]
            s = False
            if not np.isnan(cj):
                if cj > mc: mc = cj
                if cj > hc: hc = cj
                if jenis == 1:
                    if not np.isnan(atr[j]):
                        v = hc - p1 * atr[j]
                        if v > lv: lv = v
                    s = cj < lv
                elif jenis == 2:
                    if cj >= T + b:
                        T += b * np.floor((cj - T) / b)
                    s = cj <= T - p2 * b
                elif jenis == 3:
                    s = cj <= hc - p1 * A0
                elif jenis == 4:
                    bx = p1 * A0
                    v = np.floor(cj / bx) * bx
                    if v > top: top = v
                    s = cj <= top - p2 * bx
                elif jenis == 5:
                    N = int(p1)
                    if cj > tops[nt - 1]:
                        if nt < 4096:
                            tops[nt] = cj; nt += 1
                    lines = nt - 1
                    if lines >= N:
                        s = cj < tops[lines - N]
                    else:
                        s = cj < e - 4.0 * A0
                elif jenis == 6:
                    if not np.isnan(hac[j]):
                        if hac[j] < hao[j]:
                            merah += 1
                        else:
                            merah = 0
                    s = merah >= int(p1)
                elif jenis == 7:
                    if j >= 1 and not np.isnan(shc[j]) and not np.isnan(shc[j - 1]):
                        s = (shc[j] < sho[j]) and not (shc[j - 1] < sho[j - 1])
            if s:
                if j + 1 < n:
                    J[q] = j + 1; X[q] = o[j + 1]; W[q] = 0
                    PK[q] = max(mc, o[j + 1])
                else:
                    J[q] = j; X[q] = cj; W[q] = 2; PK[q] = mc
                selesai = True; break
            if tmax > 0 and j - k + 1 >= tmax:
                J[q] = j; X[q] = cj; W[q] = 1; PK[q] = mc; selesai = True; break
        if not selesai:
            J[q] = n - 1; X[q] = c[n - 1]; W[q] = 2; PK[q] = mc
    return J, X, W, PK


# ---------------------------------------------------------------- penyediaan
def sedia():
    """Muat harga AUTOTUNE + kolam; bina tatasusunan rata dan senarai kemasukan unik (U) dan dagangan (K)."""
    t0 = time.time()
    fr, idx, univ = D.muat('2011-01-01', '2100-01-01', 'AB', dir=CACHE)
    kol = pd.read_parquet(KOLAM, columns=['method', 'ticker', 'signal_date', 'entry_date', 'kumpulan', 'trade_ret',
                                          'hold_days', 'kos', 'exit_date', 'exit_reason', 'dagangan_enjin'])
    kol = kol[kol.dagangan_enjin].reset_index(drop=True)
    tick = sorted(set(kol.ticker))
    spy = idx['SPY']
    O, H, L, C, SO, SC, DT = [], [], [], [], [], [], []
    mula, akhir, pos = [], [], {}
    s = 0
    for t in tick:
        g = fr[t]
        O.append(g.open.to_numpy()); H.append(g.high.to_numpy()); L.append(g.low.to_numpy()); C.append(g.close.to_numpy())
        sp = spy.reindex(g.index).ffill()
        SO.append(sp.open.to_numpy()); SC.append(sp.close.to_numpy()); DT.append(g.index.to_numpy())
        pos[t] = s; mula.append(s); s += len(g); akhir.append(s)
    del fr
    A = dict(o=np.concatenate(O), h=np.concatenate(H), l=np.concatenate(L), c=np.concatenate(C),
             so=np.concatenate(SO), sc=np.concatenate(SC), dt=np.concatenate(DT),
             mula=np.array(mula, np.int64), akhir=np.array(akhir, np.int64))
    atr = np.full(len(A['o']), np.nan)
    for a_, b_ in zip(mula, akhir):
        atr[a_:b_] = KL.atr(A['h'][a_:b_], A['l'][a_:b_], A['c'][a_:b_])
    A['atr'] = atr
    A['hao'], A['hac'] = _ha(A['o'], A['h'], A['l'], A['c'], A['mula'], A['akhir'])
    A['sho'], A['shc'] = sha(A['o'], A['h'], A['l'], A['c'], A['mula'], A['akhir'], 20)
    # indeks bar global bagi entry_date dan exit_date
    ti = {t: i for i, t in enumerate(tick)}
    kol['ti'] = kol.ticker.map(ti).astype(np.int64)

    def cari(col):
        out = np.empty(len(kol), np.int64)
        for t, ix in kol.groupby('ticker').indices.items():
            a_, b_ = pos[t], akhir[ti[t]]
            d = A['dt'][a_:b_]
            v = kol[col].to_numpy()[ix]
            r = np.searchsorted(d, v)
            assert (r < len(d)).all() and (d[r] == v).all(), (t, col)
            out[ix] = a_ + r
        return out
    kol['k'] = cari('entry_date'); kol['J0'] = cari('exit_date')
    kol['end'] = A['akhir'][kol.ti.to_numpy()]
    kol['a0'] = A['atr'][kol.k.to_numpy() - 1]
    kol.loc[kol.k.to_numpy() - 1 < A['mula'][kol.ti.to_numpy()], 'a0'] = np.nan
    U = kol.drop_duplicates(['ticker', 'entry_date']).reset_index(drop=True)
    U = U[['ticker', 'entry_date', 'kumpulan', 'kos', 'ti', 'k', 'end', 'a0']].copy()
    ukey = pd.MultiIndex.from_frame(U[['ticker', 'entry_date']])
    kol['u'] = ukey.get_indexer(pd.MultiIndex.from_frame(kol[['ticker', 'entry_date']]))
    assert (kol.u >= 0).all()
    print(f'sedia {time.time() - t0:.0f}s: bar {len(A["o"]):,}, ticker {len(tick)}, K {len(kol):,}, U {len(U):,}, '
          f'A0 NaN {int(U.a0.isna().sum())}, NaN tutup {int(np.isnan(A["c"]).sum())}', flush=True)
    return A, kol, U


def cmd_sim(a):
    os.makedirs(OUT, exist_ok=True)
    A, kol, U = sedia()
    U.to_parquet(f'{OUT}/U.parquet')
    kol[['method', 'ticker', 'entry_date', 'kumpulan', 'trade_ret', 'hold_days', 'kos', 'exit_reason', 'k', 'J0',
         'u']].to_parquet(f'{OUT}/K.parquet')
    sah = U.a0.notna().to_numpy() & (U.a0.to_numpy() > 0)
    ks = U.k.to_numpy(); ends = U.end.to_numpy(); a0 = np.where(sah, U.a0.to_numpy(), np.nan)
    # simpan siri yang diperlukan untuk ringkas (SPY, harga, tarikh) sekali
    if not os.path.exists(f'{OUT}/bar.npz'):
        np.savez(f'{OUT}/bar.npz', o=A['o'], c=A['c'], so=A['so'], sc=A['sc'], dt=A['dt'].astype('datetime64[D]'))
    for tmax in HAD:
        for v, (jn, p1, p2) in VARIAN.items():
            f = f'{OUT}/v_{v}_t{tmax}.npz'
            if os.path.exists(f): continue
            t0 = time.time()
            J, X, W, PK = sim(A['o'], A['c'], A['atr'], A['hao'], A['hac'], A['sho'], A['shc'],
                              ks[sah], ends[sah], a0[sah], jn, p1, p2, tmax)
            Jf = np.full(len(U), -1, np.int64); Xf = np.full(len(U), np.nan); Wf = np.full(len(U), -1, np.int8)
            Pf = np.full(len(U), np.nan)
            Jf[sah] = J; Xf[sah] = X; Wf[sah] = W; Pf[sah] = PK
            np.savez(f, J=Jf, X=Xf, W=Wf, PK=Pf)
            print(f'{v} t{tmax}: {time.time() - t0:.1f}s, hari purata {np.mean(J - ks[sah] + 1):.1f}', flush=True)


def cmd_semak(a):
    """CH4 tanpa had (kod sim) lawan keluar_lorong.lorong_henti atas sampel rawak kemasukan."""
    A, kol, U = sedia()
    rng = np.random.default_rng(20261022)
    U = U[U.a0.notna()].reset_index(drop=True)
    pil = rng.choice(len(U), a.n, replace=False)
    S = U.iloc[pil].reset_index(drop=True)
    J, X, W, PK = sim(A['o'], A['c'], A['atr'], A['hao'], A['hac'], A['sho'], A['shc'],
                      S.k.to_numpy(), S.end.to_numpy(), S.a0.to_numpy(), 1, 4.0, 0.0, 0)
    sama = 0; beza = []
    for i, r in enumerate(S.itertuples()):
        a_, b_ = A['mula'][r.ti], A['akhir'][r.ti]
        o, h, l, c = (A[x][a_:b_] for x in 'ohlc')
        res = KL.lorong_henti(o, h, l, c, int(r.k - a_))
        if res['jenis'] == 'keluar':
            ok = (a_ + res['j'] == J[i]) and abs(res['harga'] - X[i]) < 1e-9 and W[i] == 0
        else:   # menunggu (isyarat pada bar terakhir) atau terbuka -> sim: tutup terakhir (W=2)
            ok = W[i] == 2 and J[i] == b_ - 1
        sama += ok
        if not ok and len(beza) < 10: beza.append((r.ticker, str(r.entry_date)[:10], res, int(J[i]), float(X[i])))
    out = dict(n=int(a.n), sama=int(sama), contoh_beza=[str(x) for x in beza])
    json.dump(out, open(f'{OUT}/semak.json', 'w'), indent=1)
    print(out)


# ---------------------------------------------------------------- metrik
def _ratio_t(ex_v, d_v, ex_c, d_c, w, kl):
    """Beza lebihan sebulan (v − c) = 21×(Σw ex_v/Σw d_v − Σw ex_c/Σw d_c); ralat piawai kaedah delta,
    berkelompok ikut tarikh masuk. Pulang (beza, se, t)."""
    W_ = w.sum()
    dv = (w * d_v).sum() / W_; dc = (w * d_c).sum() / W_
    Rv = (w * ex_v).sum() / W_ / dv; Rc = (w * ex_c).sum() / W_ / dc
    z = w * ((ex_v - Rv * d_v) / dv - (ex_c - Rc * d_c) / dc)
    g = pd.Series(z).groupby(kl).sum().to_numpy()
    G = len(g)
    se = np.sqrt(G / (G - 1) * (g ** 2).sum()) / W_
    return 21 * (Rv - Rc), 21 * se, (Rv - Rc) / se if se > 0 else np.nan


def _wq(x, w, q):
    o = np.argsort(x); cw = np.cumsum(w[o]); return float(x[o][np.searchsorted(cw, q * cw[-1])])


def metrik(r, sp, d, pk_gb, w):
    """r pulangan bersih, sp SPY tempoh sama, d hari, pk_gb give-back (mata %), w pemberat."""
    W_ = w.sum()
    m = lambda x: float((w * x).sum() / W_)
    return dict(n=int(len(r)), w=float(W_), purata=100 * m(r), median=100 * _wq(r, w, 0.5), menang=100 * m(r > 0),
                buruk5=100 * _wq(r, w, 0.05), hari=m(d), lebih_sebulan=100 * m(r - sp) / m(d) * 21,
                sebulan=100 * m(r) / m(d) * 21, capai10=100 * m(r >= 0.10), give_back=100 * m(pk_gb))


def kira_varian(U, B, v, tmax):
    """Pulangan, SPY, hari, give-back bagi setiap kemasukan U bagi varian v."""
    z = np.load(f'{OUT}/v_{v}_t{tmax}.npz')
    J, X, W, PK = z['J'], z['X'], z['W'], z['PK']
    k = U.k.to_numpy(); e = B['o'][k]; kos = U.kos.to_numpy()
    ok = J >= 0
    Js = np.where(ok, J, k)
    r = X / e * (1 - kos) / (1 + kos) - 1
    s_ex = np.where(W == 0, B['so'][Js], B['sc'][Js])
    sp = s_ex / B['so'][k] - 1
    d = (Js - k + 1).astype(float)
    gb = (PK - X) / e
    return dict(r=r, sp=sp, d=d, gb=gb, ok=ok)


def kira_kaedah(Kd, B):
    """Garis dasar (0): keluar kaedah sendiri daripada kolam (K sahaja)."""
    k = Kd.k.to_numpy(); J = Kd.J0.to_numpy(); e = B['o'][k]; kos = Kd.kos.to_numpy()
    r = Kd.trade_ret.to_numpy()
    X = (1 + r) * (1 + kos) / (1 - kos) * e
    buka = (Kd.exit_reason.to_numpy() == 'isyarat keluar') | (np.abs(X / B['o'][J] - 1) < 1e-9)
    sp = np.where(buka, B['so'][J], B['sc'][J]) / B['so'][k] - 1
    d = (J - k + 1).astype(float)
    # puncak = maks(tutup k..J−1, X)
    c = B['c']; pk = np.empty(len(k))
    cm = np.where(np.isnan(c), -np.inf, c)
    for i in range(len(k)):
        pk[i] = max(cm[k[i]:J[i]].max(initial=-np.inf), X[i])
    gb = (pk - X) / e
    return dict(r=r, sp=sp, d=d, gb=gb, hari_kolam=Kd.hold_days.to_numpy())


SAMPEL = {
    'SELECT': lambda kp, y, d: (kp == 'A') & (y >= 2013) & (y <= 2021),
    'VALIDATE-B': lambda kp, y, d: (kp == 'B') & (y >= 2013) & (y <= 2021),
    'VALIDATE-T': lambda kp, y, d: y >= 2022,
}


def cmd_ringkas(a):
    B = dict(np.load(f'{OUT}/bar.npz'))
    U = pd.read_parquet(f'{OUT}/U.parquet'); Kd = pd.read_parquet(f'{OUT}/K.parquet')
    hasil = {'nota': 'lihat lorong3_keluar.md', 'U_n': len(U), 'K_n': len(Kd),
             'U_tanpa_A0': int((~(U.a0.notna() & (U.a0 > 0))).sum())}
    base0 = kira_kaedah(Kd, B)
    hasil['semak_hari_kaedah_sama_kolam'] = float(np.mean(base0['d'] == base0['hari_kolam']))
    for tmax in HAD:
        V = {v: kira_varian(U, B, v, tmax) for v in VARIAN}
        ok_u = V['CH4']['ok']
        for wt in ('U', 'K'):
            if wt == 'U':
                kp = U.kumpulan.to_numpy(); dte = U.entry_date.to_numpy().astype('datetime64[D]')
                mth = None; sel_ok = ok_u; ui = np.arange(len(U))
            else:
                kp = Kd.kumpulan.to_numpy(); dte = Kd.entry_date.to_numpy().astype('datetime64[D]')
                mth = Kd.method.to_numpy(); ui = Kd.u.to_numpy(); sel_ok = ok_u[ui]
            yr = dte.astype('datetime64[Y]').astype(int) + 1970
            for sn, f in SAMPEL.items():
                for ecl in (False, True):
                    m = f(kp, yr, dte) & sel_ok
                    if ecl: m &= ~np.isin(yr, [2020, 2025])
                    key = f'{wt}|{sn}|{"tanpa2020_2025" if ecl else "penuh"}|t{tmax}'
                    if wt == 'U':
                        w = np.ones(m.sum())
                    else:
                        cnt = pd.Series(mth[m]).value_counts()
                        w = 1.0 / pd.Series(mth[m]).map(cnt).to_numpy()
                    kl = dte[m]
                    R = {}
                    ch = {x: V['CH4'][x][ui][m] for x in ('r', 'sp', 'd')}
                    nama = list(VARIAN) + (['KAEDAH'] if (wt == 'K' and tmax == 60) else [])
                    for v in nama:
                        if v == 'KAEDAH':
                            src = {x: base0[x][m] for x in ('r', 'sp', 'd', 'gb')}
                        else:
                            src = {x: V[v][x][ui][m] for x in ('r', 'sp', 'd', 'gb')}
                        mt = metrik(src['r'], src['sp'], src['d'], src['gb'], w)
                        if v != 'CH4':
                            b_, se, t = _ratio_t(src['r'] - src['sp'], src['d'], ch['r'] - ch['sp'], ch['d'], w, kl)
                            mt.update(beza_ch4=100 * b_, se=100 * se, t=float(t))
                        R[v] = mt
                    # sempadan CH3/CH4/CH5: lebihan sebulan CH diinterpolasi pada hari pegang calon
                    fx = sorted((R[c]['hari'], R[c]['lebih_sebulan']) for c in ('CH5', 'CH4', 'CH3'))
                    hx = np.array([p[0] for p in fx]); lx = np.array([p[1] for p in fx])
                    for v in R:
                        if v.startswith('CH'): continue
                        hh = R[v]['hari']
                        if hh < hx[0]: i0 = 0
                        elif hh > hx[-1]: i0 = len(hx) - 2
                        else: i0 = min(np.searchsorted(hx, hh) - 1, len(hx) - 2); i0 = max(i0, 0)
                        sl = (lx[i0 + 1] - lx[i0]) / (hx[i0 + 1] - hx[i0])
                        fr_ = lx[i0] + sl * (hh - hx[i0])
                        R[v]['sempadan'] = fr_; R[v]['atas_sempadan'] = R[v]['lebih_sebulan'] - fr_
                        R[v]['luar_julat'] = bool(hh < hx[0] or hh > hx[-1])
                    hasil[key] = R
                    print(key, 'n', int(m.sum()), flush=True)
        # lebihan sebulan ikut tahun masuk (U, A+B) bagi CH4 dan semua calon
        yrU = U.entry_date.dt.year.to_numpy()
        T = {}
        for v in VARIAN:
            x = V[v]; mm = ok_u
            T[v] = {int(y): 100 * np.mean((x['r'] - x['sp'])[mm & (yrU == y)]) / np.mean(x['d'][mm & (yrU == y)]) * 21
                    for y in range(2013, 2027)}
        hasil[f'tahun|t{tmax}'] = T
    json.dump(hasil, open(f'{OUT}/hasil.json', 'w'), indent=1, default=float)
    lulus(hasil)


def lulus(hasil):
    """Peraturan lulus pradaftar (U, had 60): (a) lebihan sebulan > CH4 dalam ketiga-tiga sampel; (b) t > 3 SELECT;
    (c) 5% terburuk tidak lebih buruk > 1 mata dalam ketiga-tiga; (d) (a) masih benar tanpa 2020 dan 2025."""
    out = {}
    for wt in ('U', 'K'):
        for v in CALON + (['KAEDAH'] if wt == 'K' else []):
            g = lambda s, e='penuh': hasil[f'{wt}|{s}|{e}|t60']
            a_ = all(g(s)[v]['lebih_sebulan'] > g(s)['CH4']['lebih_sebulan'] for s in SAMPEL)
            b_ = g('SELECT')[v]['t'] > 3
            c_ = all(g(s)[v]['buruk5'] >= g(s)['CH4']['buruk5'] - 1 for s in SAMPEL)
            d_ = all(g(s, 'tanpa2020_2025')[v]['lebih_sebulan'] > g(s, 'tanpa2020_2025')['CH4']['lebih_sebulan']
                     for s in SAMPEL)
            out[f'{wt}|{v}'] = dict(a=a_, b=b_, c=c_, d=d_, LULUS=a_ and b_ and c_ and d_)
    json.dump(out, open(f'{OUT}/lulus.json', 'w'), indent=1)
    for k, x in out.items(): print(k, x)


def cmd_jadual(a):
    """Jadual markdown daripada hasil.json -> <OUT>/jadual.md (dipetik ke nota)."""
    H = json.load(open(f'{OUT}/hasil.json')); L = []
    L.append(f"U_n {H['U_n']} K_n {H['K_n']} U_tanpa_A0 {H['U_tanpa_A0']} hari_kaedah_sama {H['semak_hari_kaedah_sama_kolam']}")
    for wt in ('U', 'K'):
        for tm in ('t60', 't120'):
            for e in ('penuh', 'tanpa2020_2025'):
                if tm == 't120' and e != 'penuh': continue
                for sn in SAMPEL:
                    R = H[f'{wt}|{sn}|{e}|{tm}']
                    L += [f'\n### {wt} {sn} {e} {tm} n={R["CH4"]["n"]}',
                          '| Varian | Purata % | Median % | Menang % | 5% terburuk % | Hari | Lebihan SPY sebulan % | '
                          'Beza vs CH4 | t | >=+10% | Give-back mata | Atas sempadan CH |', '|' + '---|' * 12]
                    for v, m in R.items():
                        f = lambda k, d=2: (f"{m[k]:.{d}f}" if k in m else '–')
                        sem = (f"{m['atas_sempadan']:+.2f}" + ('*' if m.get('luar_julat') else '')) if 'atas_sempadan' in m else '–'
                        L.append(f"| {v} | {f('purata')} | {f('median')} | {f('menang', 1)} | {f('buruk5')} | {f('hari', 1)} | "
                                 f"{f('lebih_sebulan')} | {f('beza_ch4')} | {f('t', 1)} | {f('capai10', 1)} | {f('give_back')} | {sem} |")
    for tm in ('t60', 't120'):
        T = H[f'tahun|{tm}']; ys = sorted(next(iter(T.values())).keys())
        L += [f'\n### Tahun {tm} (U, A+B; lebihan SPY sebulan %)', '| Varian | ' + ' | '.join(ys) + ' |', '|' + '---|' * (len(ys) + 1)]
        for v, d in T.items(): L.append(f'| {v} | ' + ' | '.join(f"{d[y]:.2f}" for y in ys) + ' |')
    open(f'{OUT}/jadual.md', 'w').write('\n'.join(L) + '\n')


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('cmd', choices=['sim', 'semak', 'ringkas', 'jadual'])
    ap.add_argument('--n', type=int, default=3000)
    a = ap.parse_args()
    dict(sim=cmd_sim, semak=cmd_semak, ringkas=cmd_ringkas, jadual=cmd_jadual)[a.cmd](a)
