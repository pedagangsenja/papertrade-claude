"""Statistik asas kolam isyarat (output bina_kolam.py) -> jadual Markdown untuk nota kolam_isyarat.md.

Guna: python3 BacktestShariah2/kajian/lilin/statistik_kolam.py [kolam.parquet] [> keluar.md]
Dagangan = baris laluan 1 (dagangan enjin_at biasa; isyarat semasa posisi ticker sama dibuka dikecualikan).
"""
import sys, json, os
import numpy as np
import pandas as pd

KOLAM = (sys.argv[1] if len(sys.argv) > 1 else
         '/tmp/claude-0/-home-user-papertrade-claude/0793050f-2ee1-522e-9bf0-b633a13089db/scratchpad/lilin/kolam.parquet')
CIRI = ['ret1', 'max20', 'gap_atr', 'julat_atr', 'atas1pct_1t', 'rcc_srs60', 'gap_atr_pctl252', 'on5',
        'on20', 'id20', 'id_share20', 'on60', 'id60', 'id_share60', 'on252', 'vol_rel50', 'vol_pctl50', 'naik_vol90',
        'hijau_vol90', 'h52', 'h52_industri', 'ibs', 'badan_julat', 'badan_arah', 'bayang_atas', 'bayang_bawah',
        'ha_naik_berturut', 'rs6_pct', 'rs12_pct']


def jadual(df, fmt=None):
    fmt = fmt or {}
    cols = list(df.columns)
    out = ['| ' + ' | '.join(str(c) for c in cols) + ' |', '|' + '---|' * len(cols)]
    for _, r in df.iterrows():
        sel = []
        for c in cols:
            v = r[c]
            f = fmt.get(c)
            if f and isinstance(v, (int, float, np.integer, np.floating)) and np.isfinite(v): sel.append(f.format(v))
            else: sel.append('' if (isinstance(v, float) and not np.isfinite(v)) else str(v))
        out.append('| ' + ' | '.join(sel) + ' |')
    return '\n'.join(out)


def ringkas(g):
    r = g.trade_ret.dropna()
    return pd.Series(dict(n=len(r), purata=r.mean(), median=r.median(), menang=(r > 0).mean(),
                          buruk5=r.quantile(0.05) if len(r) else np.nan, hari=g.hold_days.dropna().mean(),
                          lebih20=(g.fwd20 - g.spy20).mean()))


def main():
    P = pd.read_parquet(KOLAM)
    P['tahun'] = P.signal_date.dt.year
    T = P[P.dagangan_enjin]
    print(f'# Statistik kolam\n\nBaris {len(P):,}; dagangan enjin (laluan 1) {len(T):,}; '
          f'isyarat {P.signal_date.min().date()} hingga {P.signal_date.max().date()}; ticker {P.ticker.nunique():,}.\n')
    # 1. setiap kaedah
    a = P.groupby('method').agg(isyarat=('ticker', 'size'), hari_isyarat=('signal_date', 'nunique'),
                                ticker=('ticker', 'nunique'))
    b = T.groupby('method').apply(ringkas, include_groups=False)
    c = T[T.pegang8].groupby('method').apply(ringkas, include_groups=False)[['n', 'purata', 'menang']]
    c.columns = ['n_pegang8', 'purata_pegang8', 'menang_pegang8']
    d = P.groupby('method').apply(lambda g: pd.Series(dict(
        semua_n=g.trade_ret.notna().sum(), semua_purata=g.trade_ret.mean(), fwd5=g.fwd5.mean(), fwd10=g.fwd10.mean(),
        fwd20=g.fwd20.mean(), spy20=g.spy20.mean(), p10_20=(g.mfe20 >= 0.10).mean())), include_groups=False)
    M = a.join(b).join(c).join(d).reset_index()
    M['_k'] = M.method.str[1:].astype(int); M = M.sort_values('_k').drop(columns='_k')
    print('## Setiap kaedah\n')
    print('Dagangan = laluan 1 (enjin_at). `semua_*` = semua isyarat dengan keluar sendiri (laluan >= 1; kaedah ikut '
          'laluan hanya laluan 1). fwd/spy = purata mentah buka esok -> tutup +h; p10_20 = peratus isyarat dengan '
          'high maksimum 20 hari >= +10% atas harga masuk.\n')
    pct = '{:.2%}'; f3 = '{:.3f}'
    print(jadual(M, dict(purata=pct, median=pct, menang='{:.1%}', buruk5=pct, hari='{:.1f}', lebih20=pct,
                         purata_pegang8=pct, menang_pegang8='{:.1%}', semua_purata=pct, fwd5=pct, fwd10=pct,
                         fwd20=pct, spy20=pct, p10_20='{:.1%}', n='{:,.0f}', n_pegang8='{:,.0f}', semua_n='{:,.0f}',
                         isyarat='{:,.0f}', hari_isyarat='{:,.0f}', ticker='{:,.0f}')))
    # jumlah
    tot = ringkas(T)
    print(f"\nSemua kaedah (dagangan laluan 1): n {tot.n:,.0f}, purata {tot.purata:.2%}, median {tot['median']:.2%}, "
          f"menang {tot.menang:.1%}, 5% terburuk {tot.buruk5:.2%}, purata hari {tot.hari:.1f}.\n")
    # 2. setiap tahun
    print('## Setiap tahun (dagangan laluan 1, semua kaedah)\n')
    Y = T.groupby('tahun').apply(ringkas, include_groups=False)
    Y['isyarat'] = P.groupby('tahun').size()
    Y['spy20'] = P.groupby('tahun').spy20.mean()
    print(jadual(Y.reset_index()[['tahun', 'isyarat', 'n', 'purata', 'median', 'menang', 'buruk5', 'hari', 'lebih20', 'spy20']],
                 dict(purata=pct, median=pct, menang='{:.1%}', buruk5=pct, hari='{:.1f}', lebih20=pct, spy20=pct,
                      n='{:,.0f}', isyarat='{:,.0f}', tahun='{:.0f}')))
    # isyarat setiap kaedah x tahun
    print('\n### Isyarat setiap kaedah setiap tahun\n')
    X = P.pivot_table(index='method', columns='tahun', values='ticker', aggfunc='size', fill_value=0)
    X = X.loc[sorted(X.index, key=lambda s: int(s[1:]))].reset_index()
    X.columns = [str(c) for c in X.columns]
    print(jadual(X))
    # 3. kumpulan
    print('\n## Setiap kumpulan (A/B)\n')
    G = T.groupby('kumpulan').apply(ringkas, include_groups=False)
    G['isyarat'] = P.groupby('kumpulan').size()
    print(jadual(G.reset_index()[['kumpulan', 'isyarat', 'n', 'purata', 'median', 'menang', 'buruk5', 'hari', 'lebih20']],
                 dict(purata=pct, median=pct, menang='{:.1%}', buruk5=pct, hari='{:.1f}', lebih20=pct,
                      n='{:,.0f}', isyarat='{:,.0f}')))
    GM = T.groupby(['method', 'kumpulan']).trade_ret.mean().unstack()
    GM = GM.loc[sorted(GM.index, key=lambda s: int(s[1:]))]
    print('\nPurata dagangan setiap kaedah ikut kumpulan: ' + '; '.join(
        f'{m} A {r.A:.2%} / B {r.B:.2%}' for m, r in GM.iterrows()) + '.\n')
    # 4. sebab keluar
    print('## Sebab keluar (dagangan laluan 1)\n')
    S = T.groupby(['method', 'exit_reason']).size().unstack(fill_value=0)
    S = (S.div(S.sum(axis=1), axis=0))
    S = S.loc[sorted(S.index, key=lambda s: int(s[1:]))].reset_index()
    print(jadual(S, {c: '{:.0%}' for c in S.columns if c != 'method'}))
    # 5. taburan ciri (baris unik ticker-tarikh)
    print('\n## Taburan ciri (baris unik ticker × tarikh isyarat)\n')
    U = P.drop_duplicates(['ticker', 'signal_date'])
    rows = []
    for c in CIRI:
        v = U[c].astype(float)
        q = v.quantile([0.05, 0.25, 0.5, 0.75, 0.95])
        rows.append(dict(ciri=c, ada=v.notna().mean(), purata=v.mean(), p5=q[0.05], p25=q[0.25], p50=q[0.5],
                         p75=q[0.75], p95=q[0.95]))
    print(f'Baris unik: {len(U):,}.\n')
    print(jadual(pd.DataFrame(rows), {k: '{:.3f}' for k in ('purata', 'p5', 'p25', 'p50', 'p75', 'p95')} | {'ada': '{:.1%}'}))
    # 6. korelasi dengan RS proksi
    print('\n## Korelasi Spearman ciri dengan RS proksi (baris unik)\n')
    rows = []
    for c in CIRI:
        if c in ('rs6_pct', 'rs12_pct'): continue
        k = U[[c, 'rs6_pct', 'rs12_pct']].astype(float).dropna()
        r6 = k[c].corr(k.rs6_pct, method='spearman'); r12 = k[c].corr(k.rs12_pct, method='spearman')
        # median korelasi dalam kaedah (setiap kaedah, baris kaedah itu)
        mk = P.groupby('method').apply(lambda g: g[c].astype(float).corr(g.rs12_pct.astype(float), method='spearman'),
                                       include_groups=False)
        rows.append(dict(ciri=c, n=len(k), rho_rs6=r6, rho_rs12=r12, median_rho_rs12_dalam_kaedah=mk.median(),
                         min_kaedah=mk.min(), maks_kaedah=mk.max()))
    k = U[['rs6_pct', 'rs12_pct']].astype(float).dropna()
    print(f"rho(rs6_pct, rs12_pct) = {k.rs6_pct.corr(k.rs12_pct, method='spearman'):.3f}.\n")
    print(jadual(pd.DataFrame(rows), {k: '{:.3f}' for k in ('rho_rs6', 'rho_rs12', 'median_rho_rs12_dalam_kaedah',
                                                              'min_kaedah', 'maks_kaedah')} | {'n': '{:,.0f}'}))
    # 7. taburan ciri setiap kaedah (median)
    print('\n## Median ciri utama setiap kaedah\n')
    K = ['max20', 'ret1', 'gap_atr', 'julat_atr', 'id_share20', 'id_share60', 'vol_rel50', 'h52', 'ibs', 'rs12_pct',
         'atas1pct_1t', 'naik_vol90']
    Q = P.groupby('method')[K].agg(lambda s: s.astype(float).mean() if s.name in ('atas1pct_1t', 'naik_vol90')
                                   else s.astype(float).median())
    Q = Q.loc[sorted(Q.index, key=lambda s: int(s[1:]))].reset_index()
    print('(atas1pct_1t dan naik_vol90 = peratus isyarat; lain = median.)\n')
    print(jadual(Q, {c: '{:.3f}' for c in K}))


if __name__ == '__main__':
    main()
