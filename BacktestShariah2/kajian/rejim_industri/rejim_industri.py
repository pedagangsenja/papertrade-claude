"""Kajian rejim QQQ dan industri (10 Nov 2026). Laporan: ../KAJIAN_REJIM_INDUSTRI.md.

Jalankan dari mana-mana: python3 BacktestShariah2/kajian/rejim_industri/rejim_industri.py
Bukan pradaftar; kajian penerokaan untuk menjawab soalan pengguna. Tiada fail ditulis.
"""
from pathlib import Path
import numpy as np
import pandas as pd

R = Path(__file__).resolve().parents[3]
S = R / 'BacktestShariah2'


# ---------- data ----------
def qqq():
    """QQQ 2019-01 .. terkini: data_mentah (2019-2024) + stor harga (Okt 2024 ke atas)."""
    b = pd.read_csv(R / 'data_mentah/index_benchmark.csv')
    h = pd.read_csv(S / 'data/harga/stor/harga_idx.csv')
    out = []
    for x in (b, h):
        x = x[x.ticker == 'QQQ'][['date', 'close']].copy()
        x['date'] = pd.to_datetime(x.date.astype(str))
        out.append(x.set_index('date').close)
    b, h = out
    ov = b.index.intersection(h.index)
    k = (h[ov] / b[ov]).median()  # bertindih 490 hari, nisbah 1.000000
    return pd.concat([b[b.index < h.index[0]] * k, h]).sort_index()


def rejim(c):
    """ON = tutup > SMA50 DAN SMA10 > SMA20 (definisi SPEC_KAD_SKOR.md)."""
    s10, s20, s50 = (c.rolling(n).mean() for n in (10, 20, 50))
    return ((c > s50) & (s10 > s20)).where(s50.notna())


def industri():
    d = pd.read_csv(S / 'kajian/industri/industri_harian.csv.gz')
    d['date'] = pd.to_datetime(d.date.astype(str))
    return d


def saham():
    a = pd.concat([pd.read_csv(S / f'data/harga/stor/harga_{x}.csv') for x in 'AB'])
    a['date'] = pd.to_datetime(a.date.astype(str))
    return a


def peta():
    return pd.read_csv(S / 'papertrade/peta_industri.csv').set_index('ticker').industri


def nw_t(x, lag):
    x = x.dropna(); n = len(x); e = x - x.mean()
    s = (e * e).sum() / n
    for L in range(1, lag + 1):
        s += 2 * (1 - L / (lag + 1)) * (e[L:].values * e[:-L].values).sum() / n
    return x.mean() / np.sqrt(s / n)


def ke_hadapan(ret, H):
    """Pulangan t+1..t+H (isyarat pada tutup t)."""
    lr = np.log1p(ret)
    return np.expm1(lr[::-1].rolling(H).sum()[::-1].shift(-1))


def prestasi(s):
    eq = (1 + s).cumprod(); yrs = len(s) / 252
    return 100 * (eq.iloc[-1] ** (1 / yrs) - 1), 100 * (eq / eq.cummax() - 1).min()


# ---------- §1 rejim QQQ ----------
def bahagian_rejim(q, rg, d):
    print('## 1. Rejim QQQ')
    print('Hari ON %.0f%% (2019-2026)' % (100 * rg.mean()))
    mk = (d.ew * d.n).groupby(d.date).sum() / d.groupby('date').n.sum()
    mk = mk[mk.index >= '2019-01-01']
    for nama, ret in [('QQQ', q.pct_change()), ('Purata saham EW luas', mk)]:
        ret = ret.dropna()
        for H in (10, 21):
            df = pd.DataFrame({'f': ke_hadapan(ret, H), 'r': rg.reindex(ret.index)}).dropna()
            for k, g in df.groupby('r'):
                print('  %s %d sesi %s: n %d min %.2f%% median %.2f%% positif %.0f%% sisihan %.2f%% t(NW) %.2f'
                      % (nama, H, 'ON' if k else 'OFF', len(g), 100 * g.f.mean(), 100 * g.f.median(),
                         100 * (g.f > 0).mean(), 100 * g.f.std(), nw_t(g.f, H)))
    ret = q.pct_change()
    pos = rg.shift(1).fillna(0)
    m = '2019-03-15'
    calon = {'Pegang QQQ 100%': ret, 'QQQ bila ON sahaja': ret * pos,
             'QQQ statik %.0f%%' % (100 * pos[m:].mean()): ret * pos[m:].mean()}
    for nm, s in calon.items():
        s = s[m:].fillna(0); c, dd = prestasi(s)
        thn = ' '.join('%d %.1f%%/%.1f%%' % ((y,) + (lambda z: (100 * ((1 + z).prod() - 1),
                       100 * ((1 + z).cumprod() / (1 + z).cumprod().cummax() - 1).min()))(s[str(y)]))
                       for y in (2020, 2022, 2025, 2026))
        print('  %s: CAGR %.1f%% MDD %.1f%% | tahun (pulangan/MDD): %s' % (nm, c, dd, thn))


# ---------- §2 pecahan pergerakan harian ----------
def bahagian_varians(q):
    print('\n## 2. Pecahan pergerakan harian saham (R^2)')
    rq = q.pct_change(); a = saham(); io = peta()
    p = a.pivot(index='date', columns='ticker', values='close').sort_index()
    rt = p.pct_change().clip(-0.5, 1.0)
    res = []
    for t in rt.columns:
        I = io.get(t)
        if not isinstance(I, str):
            continue
        peers = [x for x in rt.columns if io.get(x) == I and x != t]
        if len(peers) < 3:
            continue
        df = pd.DataFrame({'y': rt[t], 'm': rq.reindex(rt.index), 'i': rt[peers].mean(axis=1)}).dropna()
        if len(df) < 250:
            continue
        X = np.c_[np.ones(len(df)), df.m]
        e = df.y - X @ np.linalg.lstsq(X, df.y, rcond=None)[0]; r2m = 1 - e.var() / df.y.var()
        ii = df.i - X @ np.linalg.lstsq(X, df.i, rcond=None)[0]  # industri tolak QQQ
        X2 = np.c_[X, ii]
        e2 = df.y - X2 @ np.linalg.lstsq(X2, df.y, rcond=None)[0]; r2 = 1 - e2.var() / df.y.var()
        res.append((t, I, r2m, r2 - r2m, 1 - r2))
    r = pd.DataFrame(res, columns=['t', 'ind', 'pasaran', 'industri', 'sendiri'])
    print('  %d saham, %d industri, %s hingga %s' % (len(r), r.ind.nunique(), rt.index.min().date(), rt.index.max().date()))
    print('  median:', r[['pasaran', 'industri', 'sendiri']].median().round(3).to_dict())
    s = r[r.ind.str.contains('Semicon')]
    print('  semikonduktor (n %d) median:' % len(s), s[['pasaran', 'industri', 'sendiri']].median().round(3).to_dict())
    t = r.groupby('ind')[['pasaran', 'industri', 'sendiri']].median().assign(n=r.groupby('ind').size())
    print(t[t.n >= 4].sort_values('industri', ascending=False).head(6).round(2).to_string())


# ---------- §3 momentum industri ----------
def matriks_industri(d):
    w = d.pivot(index='date', columns='industri', values='ew').sort_index()
    n = d.pivot(index='date', columns='industri', values='n').sort_index()
    w = w.where(n >= 5)
    lv = (1 + w.fillna(0)).cumprod().where(w.notna())
    rank = (lv / lv.shift(21) - 1).rank(axis=1, pct=True)
    f21 = lv.shift(-22) / lv.shift(-1) - 1  # masuk esok, pegang 21 sesi
    ex = f21.sub(f21.mean(axis=1), axis=0)
    return lv, rank, ex


def bahagian_industri(rg, lv, rank, ex):
    print('\n## 3. Industri teratas 1 bulan -> lebihan 21 sesi (sampel tidak bertindih, 6 ofset)')

    def kaji(mula, akhir):
        out = []
        for off in range(0, 21, 4):
            for t in lv.index[(lv.index >= mula) & (lv.index <= akhir)][off::21]:
                rk = rank.loc[t].dropna(); e = ex.loc[t]
                if rk.empty or e.isna().all():
                    continue
                A = e[rk[rk >= 0.8].index].mean(); E = e[rk[rk < 0.2].index].mean()
                sa = e.get('Semiconductors') if rk.get('Semiconductors', 0) >= 0.8 else np.nan
                out.append((off, t, A, E, A - E, sa, rg.get(t, np.nan)))
        return pd.DataFrame(out, columns=['off', 't', 'A', 'E', 'AE', 'semiA', 'rg'])

    for nama, (m, a) in {'2005-2026': ('2005-03-01', '2026-09-10'),
                         '2019-2026': ('2019-03-15', '2026-09-10')}.items():
        o = kaji(m, a); o0 = o[o.off == 0]
        t = o0.AE.mean() / (o0.AE.std() / np.sqrt(len(o0)))
        print('  %s: A %.2f%% E %.2f%% A-E %.2f%% (t %.2f, n %d) A>E %.0f%% bulan'
              % (nama, 100 * o.A.mean(), 100 * o.E.mean(), 100 * o.AE.mean(), t, len(o0), 100 * (o0.AE > 0).mean()))
        sa = o.semiA.dropna()
        print('    Semiconductors bila 20%% teratas: lebihan purata %.2f%% median %.2f%% positif %.0f%% n %d'
              % (100 * sa.mean(), 100 * sa.median(), 100 * (sa > 0).mean(), len(sa)))
        if nama == '2019-2026':
            for k, gg in o.dropna(subset=['rg']).groupby('rg'):
                g0 = gg[gg.off == 0]
                print('    QQQ %s: A-E %.2f%% (t %.2f, n %d)' % ('ON' if k else 'OFF', 100 * gg.AE.mean(),
                      g0.AE.mean() / (g0.AE.std() / np.sqrt(len(g0))), len(g0)))
    A = rank >= 0.8
    kk = (A & A.shift(-21)).sum().sum() / A.shift(-21).where(A).notna().sum().sum()
    print('  Kekal 20%% teratas selepas 21 sesi: %.0f%%' % (100 * kk))


# ---------- §4 kes semikonduktor 2026 ----------
def bahagian_semi(q, rg, d, lv, rank):
    print('\n## 4. Kes semikonduktor 2026')
    SM = ['Semiconductors', 'Semiconductor Equipment & Materials']
    mlv = (1 + (d.ew * d.n).groupby(d.date).sum() / d.groupby('date').n.sum()).cumprod()

    def ret(ser, a, b):
        ser = ser.dropna()
        a = ser.index[ser.index >= pd.Timestamp(a)][0]; b = ser.index[ser.index <= pd.Timestamp(b)][-1]
        return 100 * (ser[b] / ser[a] - 1)

    y = lv.loc['2025-12-31':]
    for s in SM:
        x = y[s] / y[s].iloc[0]; tr = x['2026-02-01':'2026-05-15'].idxmin()
        print('  %s dasar %s, %.1f%% sejak 31 Dis' % (s, tr.date(), 100 * (x[tr] - 1)))
    qq = q['2025-12-31':] / q['2025-12-31']
    print('  QQQ dasar %s, %.1f%% sejak 31 Dis' % (qq['2026-02-01':'2026-05-15'].idxmin().date(), 100 * (qq['2026-02-01':'2026-05-15'].min() - 1)))
    prev = None
    for t, v in rg['2026-01-01':].items():
        if v != prev:
            print('    rejim %s %s' % (t.date(), 'ON' if v else 'OFF')); prev = v
    print('  Kumulatif dari 31 Mac 2026:')
    for t in ('2026-04-13', '2026-04-30', '2026-05-29', '2026-06-15', '2026-10-16'):
        print('    %s Semi %.1f%% SemiEq %.1f%% QQQ %.1f%% purata saham %.1f%%' % (
            t, ret(lv[SM[0]], '2026-03-31', t), ret(lv[SM[1]], '2026-03-31', t),
            ret(q, '2026-03-31', t), ret(mlv, '2026-03-31', t)))
    print('  Persentil pangkat 1 bulan (mingguan):')
    for t in pd.date_range('2026-03-02', '2026-07-31', freq='7D'):
        t2 = rank.index[rank.index >= t][0]
        print('    %s Semi %.0f SemiEq %.0f QQQ %s' % (t2.date(), 100 * rank.loc[t2, SM[0]],
              100 * rank.loc[t2, SM[1]], 'ON' if rg.get(t2, 0) == 1 else 'OFF'))
    for s in SM:
        f = rank.loc['2026-04-01':, s]; t0 = f[f >= 0.8].index[0]; i = lv.index.get_loc(t0)
        print('  %s masuk 20%% teratas %s: 21 sesi %.1f%% (purata saham %.1f%%), 63 sesi %.1f%% (purata %.1f%%)' % (
            s, t0.date(), ret(lv[s], t0, lv.index[i + 21]), ret(mlv, t0, lv.index[i + 21]),
            ret(lv[s], t0, lv.index[i + 63]), ret(mlv, t0, lv.index[i + 63])))
        i = lv.index.get_loc(lv.index[lv.index >= '2026-06-22'][0])
        print('    beli 22 Jun (persentil %.0f): 21 sesi %.1f%%, hingga %s %.1f%%' % (
            100 * rank.iloc[i][s], 100 * (lv[s].iloc[i + 21] / lv[s].iloc[i] - 1),
            lv.index[-1].date(), 100 * (lv[s].iloc[-1] / lv[s].iloc[i] - 1)))
    a = saham(); io = peta()
    p = a.pivot(index='date', columns='ticker', values='close').sort_index()
    for s_, e_ in (('2026-03-31', '2026-06-15'), ('2026-06-15', '2026-11-06')):
        x = p.loc[p.index[p.index <= s_][-1]]; z = p.loc[p.index[p.index <= e_][-1]]
        rr = (z / x - 1).dropna()
        sem = rr[rr.index.map(lambda t: 'Semicon' in str(io.get(t, '')))]; oth = rr.drop(sem.index)
        print('  Stor harga %s..%s: semikonduktor n %d naik %.0f%% median %.1f%% | lain n %d naik %.0f%% median %.1f%%' % (
            s_, e_, len(sem), 100 * (sem > 0).mean(), 100 * sem.median(), len(oth), 100 * (oth > 0).mean(), 100 * oth.median()))


if __name__ == '__main__':
    q = qqq(); rg = rejim(q); d = industri()
    lv, rank, ex = matriks_industri(d)
    bahagian_rejim(q, rg, d)
    bahagian_varians(q)
    bahagian_industri(rg, lv, rank, ex)
    bahagian_semi(q, rg, d, lv, rank)
