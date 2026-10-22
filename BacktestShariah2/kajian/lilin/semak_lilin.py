"""Semakan kewarasan uji_lilin_aliran.py: penunjuk numba lawan enjin.rsi / enjin.atr (pandas), keluar Chandelier
lawan standard/keluar_lorong.lorong_henti, dan contoh corak lilin dicetak untuk semakan mata.
Larian: python3 BacktestShariah2/kajian/lilin/semak_lilin.py"""
import sys
from pathlib import Path

import numpy as np
import pandas as pd

AKAR = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(AKAR / 'BacktestShariah2' / 'standard'))
import uji_lilin_aliran as U  # noqa: E402
from keluar_lorong import lorong_henti, atr as atr_lorong  # noqa: E402

CACHE = AKAR / 'AUTOTUNE' / '.cache'
SC = U.LALAI_KELUAR


def main():
    tk = ['AAPL', 'NVDA', 'CROX', 'SMCI']
    d = pd.concat([pd.read_parquet(CACHE / f'harga_{y}.parquet', filters=[('ticker', 'in', tk)]) for y in range(2009, 2027)])
    d = d.sort_values(['ticker', 'date']).reset_index(drop=True)
    o, h, l, c = (d[k].to_numpy(np.float64) for k in ('open', 'high', 'low', 'close'))
    code = pd.factorize(d.ticker, sort=True)[0]
    seg = np.r_[0, np.flatnonzero(np.diff(code)) + 1]
    mula = seg.astype(np.int64); akhir = np.r_[seg[1:], len(d)].astype(np.int64)
    rsi = U._rsi(c, mula, akhir, 2); atr = U._atr(h, l, c, mula, akhir, 14)
    mx_r = mx_a = 0.0
    for s, e in zip(mula, akhir):
        cc = pd.Series(c[s:e])
        dl = cc.diff(); au = dl.clip(lower=0).ewm(alpha=1 / 2, adjust=False).mean()
        ad = (-dl.clip(upper=0)).ewm(alpha=1 / 2, adjust=False).mean(); r = (100 - 100 / (1 + au / ad)).values
        k = np.isfinite(r) & np.isfinite(rsi[s:e])
        mx_r = max(mx_r, np.abs(r[k] - rsi[s:e][k]).max())
        a2 = atr_lorong(h[s:e], l[s:e], c[s:e])
        k = np.isfinite(a2)
        mx_a = max(mx_a, np.nanmax(np.abs(a2[k] - atr[s:e][k])))
        assert (np.isfinite(a2) == np.isfinite(atr[s:e])).all()
    print(f'RSI2 beza maks {mx_r:.2e}; ATR14 beza maks {mx_a:.2e}')

    # Chandelier lawan lorong_henti (tanpa had 60 dan tanpa akhir tetingkap: tmax besar)
    rng = np.random.default_rng(1)
    salah = 0; nuji = 0
    for s, e in zip(mula, akhir):
        for r in rng.integers(s + 300, e - 200, 40):
            xr, xp, xb, why = U._simulasi(o, h, l, c, atr, np.array([r], np.int64), np.array([e], np.int64), 0, 10 ** 6)
            ref = lorong_henti(o[s:e], h[s:e], l[s:e], c[s:e], r + 1 - s)
            nuji += 1
            if ref['jenis'] == 'keluar':
                if not (xr[0] == ref['j'] + s and xp[0] == ref['harga']): salah += 1
            elif why[0] != 0: salah += 1
    print(f'Chandelier lawan lorong_henti: {nuji} dagangan, {salah} berbeza')

    T = pd.read_parquet(SC / 'isyarat.parquet', columns=['ticker', 'sig', 'ent', 'ex', 'ret', 'days', 'why', 'sampel', 'keluar',
                                                         'V01_engulf', 'V04_3LS', 'V02_piercing', 'lebih', 'spy'])
    print('jumlah baris isyarat', len(T))
    print(T[(T.keluar == 'pegang10')].days.value_counts().head(5).to_dict())
    for nm in ('V01_engulf', 'V04_3LS', 'V02_piercing'):
        x = T[T[nm] & (T.keluar == 'chandelier') & T.ticker.isin(tk)].head(2)
        for _, r in x.iterrows():
            dd = d[(d.ticker == r.ticker) & (d.date <= r.sig)].tail(5)[['date', 'open', 'high', 'low', 'close']]
            print(nm, r.ticker, str(r.sig)[:10]); print(dd.to_string(index=False))


if __name__ == '__main__':
    main()
