"""FASA 2 — fasa HOLD: kelas pullback sebagai peraturan JUAL (SPEC §13.12 B7).

Penemuan FASA 1 yang replikasi pada 6/6 tahun ialah kelas pullback, bukan mana-mana signal ENTRY.
Di sini ia diuji sebagai peraturan jual, atas posisi **entry-agnostik** (arm X+R: 8 saham RS 6 bulan
tertinggi dalam universe setiap hari), dibanding `chandelier_4atr` dan `pegang_252` atas set posisi
yang SAMA. Definisi kausal kelas pullback: SPEC §13.12 B7.

Guna: python3 REVERSE/fasa2_hold.py [--tahun 2020 ...]
Output: REVERSE/fasa2_hold.csv, .cache/fasa2_hold_dagangan.parquet
"""
import argparse
import sys
import time
from pathlib import Path

import numpy as np
import pandas as pd

AKAR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(AKAR))
from REVERSE.teras import data as D, stat as T  # noqa: E402
from REVERSE.teras.kos import kos_sisi  # noqa: E402
from REVERSE.fasa2_ablasi import (CACHE, KELUAR, TAHUN, UFUK, HUJUNG, BENIH, SLOT,  # noqa: E402
                                  pilihan_tahun, senarai_signal, siri_ticker, keluar3,
                                  stat_arm, portfolio)

AMARAN = 'pullback_amaran'


def pasaran(ix):
    """pas (pasaran naik) dan jat (SPY jatuh > 2% / 5 hari) — sama seperti step5_6_hold_exit.py."""
    spy, qqq = ix['SPY']['close'], ix['QQQ']['close']
    pas = ((spy > spy.rolling(50, min_periods=50).mean())
           & (spy > spy.rolling(200, min_periods=200).mean())
           & (qqq > qqq.rolling(50, min_periods=50).mean())
           & (qqq > qqq.rolling(200, min_periods=200).mean())
           & (spy.rolling(50, min_periods=50).mean().pct_change(10) > 0))
    jat = spy.pct_change(5) < -0.02
    return pas, jat


def keluar_amaran(c, o, lo, ma50, cerun, pas_a, jat_a, i, n):
    """Hari keluar bagi peraturan 'jual apabila kelas pullback = AMARAN' (kausal, SPEC §13.12 B7)."""
    i0 = i + 1
    b = min(i + UFUK, n - 1)
    if i0 >= n or b <= i0:
        return None
    puncak = c[i0]
    palung_lepas = lo[i0]
    dalam, palung, i_palung = False, np.inf, -1
    for d in range(i0 + 1, b + 1):
        x = c[d]
        if not np.isfinite(x):
            continue
        if not dalam:
            if np.isfinite(puncak) and x <= puncak * 0.95:
                dalam, palung, i_palung = True, x, d
        else:
            if x < palung:
                palung, i_palung = x, d
        if dalam and i_palung >= 0:
            trend = (np.isfinite(ma50[i_palung]) and c[i_palung] > ma50[i_palung]
                     and np.isfinite(cerun[i_palung]) and cerun[i_palung] > 0
                     and palung > palung_lepas)
            if not (trend and (pas_a[i_palung] or jat_a[i_palung])):
                k = min(d + 1, n - 1)
                return k, (o[k] if np.isfinite(o[k]) else c[k]), k - i0 + 1
        if np.isfinite(x) and x > puncak:
            if dalam:
                palung_lepas = palung
            dalam, palung, i_palung = False, np.inf, -1
            puncak = x
    return b, c[b], b - i0 + 1


def kira(pilih, spy, ix):
    unik = pilih[['ticker', 'tarikh']].drop_duplicates()
    per_tk = {tk: g.tarikh.to_numpy() for tk, g in unik.groupby('ticker', sort=False)}
    t0 = time.time()
    fr = D.muat_harga(sorted(per_tk), '2018-06-01', HUJUNG)
    pas, jat = pasaran(ix)
    sp = spy.to_numpy('float64')
    spi = {d: k for k, d in enumerate(spy.index)}
    rows = []
    for n_, (tk, g) in enumerate(fr.items()):
        c, o, atr, to = siri_ticker(g)
        lo = g['low'].to_numpy('float64')
        ma50 = g['close'].rolling(50, min_periods=50).mean()
        cerun = (ma50 / ma50.shift(10) - 1.0).to_numpy('float64')
        ma50 = ma50.to_numpy('float64')
        pas_a = pas.reindex(g.index).fillna(False).to_numpy()
        jat_a = jat.reindex(g.index).fillna(False).to_numpy()
        n, pos = c.size, g.index
        for d in per_tk.get(tk, ()):
            if d not in pos:
                continue
            i = int(pos.get_loc(d))
            if i + 1 >= n:
                continue
            ks = kos_sisi(to[i])
            masuk = o[i + 1] * (1 + ks)
            if not np.isfinite(masuk) or masuk <= 0:
                continue
            kel = keluar3(c, o, atr, i, n) or {}
            ka = keluar_amaran(c, o, lo, ma50, cerun, pas_a, jat_a, i, n)
            if ka is not None:
                kel[AMARAN] = ka
            d_masuk = pos[i + 1]
            a = spi.get(d_masuk)
            for pol, (k, harga, hari) in kel.items():
                if pol == 'jual_hari63' or not np.isfinite(harga) or harga <= 0:
                    continue
                jual = harga * (1 - ks)
                bq = spi.get(pos[k])
                spul = (sp[bq] / sp[a] - 1.0) if (a is not None and bq is not None) else np.nan
                rows.append((tk, d, pol, float(jual / masuk - 1.0) * 100,
                             float(jual / masuk - 1.0 - spul) * 100, int(hari), d_masuk,
                             pos[k], float(masuk), float(jual), int(k >= n - 1)))
        if n_ % 300 == 0:
            print(f'  {n_}/{len(fr)} [{time.time()-t0:.0f}s]')
    return pd.DataFrame(rows, columns=['ticker', 'tarikh', 'polisi', 'pulangan', 'lebihan_spy',
                                       'hari', 'tarikh_masuk', 'tarikh_keluar', 'harga_masuk',
                                       'harga_jual', 'terpotong'])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--tahun', type=int, nargs='*', default=TAHUN)
    a_ = ap.parse_args()
    t0 = time.time()
    fp = CACHE / f'fasa2_pilihan_{min(a_.tahun)}-{max(a_.tahun)}.parquet'
    if fp.exists():
        pil = pd.read_parquet(fp)
    else:
        pil = pd.concat([pilihan_tahun(th, senarai_signal()) for th in a_.tahun],
                        ignore_index=True)
        pil.to_parquet(fp, index=False)
    pil = pil[pil.arm == 'X+R'].reset_index(drop=True)
    print(f'posisi entry-agnostik (X+R): {len(pil)}')
    ix = D.muat_indeks('2018-06-01', HUJUNG)
    spy = ix['SPY']['close']
    f = CACHE / f'fasa2_hold_dagangan_{min(a_.tahun)}-{max(a_.tahun)}.parquet'
    dag = pd.read_parquet(f) if f.exists() else kira(pil, spy, ix)
    if not f.exists():
        dag.to_parquet(f, index=False)
    print(f'[{time.time()-t0:.0f}s] dagangan {len(dag)}')
    rows = []
    for pol, d in dag.groupby('polisi'):
        rows.append(dict(polisi=pol, **stat_arm(d.reset_index(drop=True))))
    kal = spy.index[(spy.index >= pd.Timestamp(f'{min(a_.tahun)}-01-01'))
                    & (spy.index <= pd.Timestamp(HUJUNG))]
    fr = D.muat_harga(sorted(dag.ticker.unique()), f'{min(a_.tahun)-1}-01-01', HUJUNG)
    tutup = pd.DataFrame({t: g['close'] for t, g in fr.items()}).reindex(kal).ffill()
    del fr
    kp = {pol: g[['ticker', 'tarikh', 'tarikh_masuk', 'tarikh_keluar', 'harga_masuk',
                  'harga_jual', 'hari']].reset_index(drop=True)
          for pol, g in dag.groupby('polisi')}
    pf = portfolio(pil, kp, tutup, kal)
    out = pd.DataFrame(rows).merge(
        pd.DataFrame(pf.values()).rename(columns={c: f'pf_{c}' for c in
                                                  ('n_posisi', 'n_tutup', 'purata_slot',
                                                   'purata_hari_pegang', 'pulangan_jumlah',
                                                   'cagr', 'mdd', 'median_bulanan',
                                                   'purata_bulanan', 'pct_bulan_ge10',
                                                   'pct_bulan_positif', 'bulan_terburuk')}),
        on='polisi', how='left')
    spy_k = spy.reindex(kal).ffill()
    tn = max((kal[-1] - kal[0]).days / 365.25, 1e-9)
    out['spy_cagr'] = round((float(spy_k.iloc[-1] / spy_k.iloc[0]) ** (1 / tn) - 1) * 100, 2)
    out['spy_mdd'] = round(T.mdd(spy_k.to_numpy()), 2)
    out.to_csv(KELUAR / 'fasa2_hold.csv', index=False)
    print(out.to_string(index=False))
    print(f'[{time.time()-t0:.0f}s] fasa2_hold.csv')


if __name__ == '__main__':
    main()
