"""Carian setup CS05 — lapisan PRASYARAT (SPEC pindaan 14 Nov 2026 (i)).

Dua lapisan, kedua-duanya BUKAN daripada harga saham itu sendiri:
- PASARAN (33; sama bagi semua saham pada hari itu): QA/QB/QC/QG = prasyarat A/B/C/G pindaan (h) (takrif
  `cs_prasyarat.pasaran`), QH01-QH10 = takrif pakar (`pakar()` di bawah).
- KUMPULAN/SYARIKAT (15; berbeza antara saham): QD/QE/QF = prasyarat D/E/F pindaan (h) (`cs_prasyarat.kumpulan`,
  `cs_prasyarat.earnings`). Tanpa data -> PALSU.
Plasebo: siri yang sama dianjak ANJAK sesi/bar secara membulat (peratus masa benar dan kelompok kekal).
Guna: python3 cs_lapis.py <kerja>   (panel_A.pkl dan panel_B.pkl sudah ada) -> lapis_A.pkl, lapis_B.pkl.
Senarai dan ambang di bawah ialah sebahagian daripada pradaftar: jangan ubah tanpa pindaan bertarikh pada spec."""
import os
import pickle
import sys

import numpy as np
import pandas as pd

SINI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SINI)

ANJAK = 437
PASARAN = [
    'QA01 QQQ ON', 'QA02 QQQ OFF', 'QA03 SPY atas SMA200', 'QA04 SPY bawah SMA200',
    'QA05 QQQ dalam 3% dari puncak 52 minggu', 'QA06 QQQ >= 10% di bawah puncak', 'QA07 QQQ >= 20% di bawah puncak',
    'QA08 rejim ON baharu (<= 10 sesi)', 'QA09 rejim OFF baharu (<= 10 sesi)', 'QA10 QQQ RSI14 < 35',
    'QA11 QQQ naik >= 3% dalam 5 sesi',
    'QB01 turun-naik SPY 21 hari >= 25% setahun', 'QB02 turun-naik SPY 21 hari <= 10% setahun',
    'QB03 turun-naik SPY menurun (21 hari < 63 hari)',
    'QC01 >= 60% saham di atas MA50', 'QC02 <= 30% saham di atas MA50', 'QC03 keluasan naik >= 10 mata dalam 10 sesi',
    'QC04 >= 60% saham di atas MA200', 'QC05 >= 15% saham dalam 5% dari puncak 52 minggu',
    'QG01 Nov-Apr', 'QG02 Mei-Okt', 'QG03 7 hari pertama bulan', 'QG04 Januari',
    'QH01 follow-through day aktif (QQQ, 20 sesi)', 'QH02 distribution day QQQ <= 2 dalam 25 sesi',
    'QH03 distribution day QQQ >= 5 dalam 25 sesi', 'QH04 breadth thrust Zweig aktif (20 sesi)',
    'QH05 nisbah 4% (10 hari) > 2', 'QH06 nisbah 4% (10 hari) < 0.5',
    'QH07 regangan turun-naik SPY (proksi VIX) + SPY > SMA200', 'QH08 QQQ SMA10 > SMA20',
    'QH09 SPY Peringkat 2 Weinstein (atas SMA150 yang naik)', 'QH10 hari 90% turun kemudian naik (20 sesi)',
]
KUMPULAN = [
    'QD01 sektor 3 teratas (pulangan 63 sesi)', 'QD02 sektor 3 terbawah (pulangan 63 sesi)',
    'QD03 >= 60% saham sektor di atas MA50',
    'QE01 industri 20% teratas (pulangan 63 sesi)', 'QE02 industri 20% teratas (pulangan 21 sesi)',
    'QE03 industri 20% terbawah (pulangan 63 sesi)', 'QE04 >= 60% saham industri di atas MA50',
    'QE05 saham lain dalam industri sama naik >= 20% dalam 20 sesi',
    'QF01 earnings dalam 1-5 sesi akan datang', 'QF02 0-4 sesi selepas earnings', 'QF03 5-19 sesi selepas earnings',
    'QF04 tiada earnings dalam 20 sesi akan datang', 'QF05 kejutan untung terkini positif (SUE > 0)',
    'QF06 hasil suku terkini tumbuh >= 20%', 'QF07 harga melompat >= 5% pada hari earnings (20 sesi lalu)',
]
N1, N2 = len(PASARAN), len(KUMPULAN)


def ftd(lo, cl, vol):
    """QH01: follow-through day aktif. lo, cl, vol = rendah, tutup, volum QQQ (ndarray). Pulangkan ndarray bool."""
    n = len(cl)
    out = np.zeros(n, bool)
    min20 = pd.Series(lo).rolling(20).min().to_numpy()
    max252 = pd.Series(cl).rolling(252).max().to_numpy()
    i_rendah, paras, hingga = -1, np.nan, -1
    for i in range(1, n):
        if min20[i] == min20[i] and max252[i] == max252[i] and lo[i] <= min20[i] and cl[i] <= 0.93 * max252[i]:
            i_rendah, paras, hingga = i, lo[i], -1                    # hari rendah baharu: cubaan rali bermula semula
        elif i_rendah >= 0:
            if cl[i] < paras:                                        # tutup di bawah rendah hari rendah: terbatal
                i_rendah, hingga = -1, -1
            elif 4 <= i - i_rendah <= 12 and cl[i] / cl[i - 1] - 1 >= 0.015 and vol[i] > vol[i - 1]:
                hingga = i + 19
        out[i] = i <= hingga
    return out


def pakar(q, s, harian):
    """QH01-QH10. q, s: DataFrame QQQ / SPY (low, close, volume) berindeks hari; harian: DataFrame naik, turun, n4n,
    n4t (bilangan saham layak) berindeks hari yang sama. Pulangkan dict nama -> Series bool."""
    qc, sc = q.close, s.close
    dd = ((qc / qc.shift() - 1 <= -0.002) & (q.volume > q.volume.shift())).astype(float).rolling(25).sum()
    nisbah = harian.naik / (harian.naik + harian.turun).replace(0, np.nan)
    ema = nisbah.ewm(span=10, adjust=False).mean()
    thrust = (ema > 0.615) & (ema.shift(1).rolling(10).min() < 0.40)
    n4 = harian.n4n.rolling(10).sum() / harian.n4t.rolling(10).sum().replace(0, np.nan)
    rv10 = sc.pct_change().rolling(10).std()
    regang = rv10 >= 1.05 * rv10.rolling(10).mean()
    m150 = sc.rolling(150).mean()
    turun90 = (1 - nisbah) >= 0.90
    naik = (nisbah >= 0.90) | ((nisbah >= 0.80) & (nisbah.shift(1) >= 0.80))
    isy90 = naik & (turun90.astype(float).shift(1).rolling(10).max() > 0)
    aktif = lambda x, k=20: x.astype(float).rolling(k, min_periods=1).max() > 0
    P = {
        'QH01': pd.Series(ftd(q.low.to_numpy(float), qc.to_numpy(float), q.volume.to_numpy(float)), index=q.index),
        'QH02': dd <= 2, 'QH03': dd >= 5, 'QH04': aktif(thrust), 'QH05': n4 > 2, 'QH06': n4 < 0.5,
        'QH07': regang & regang.shift(1, fill_value=False) & regang.shift(2, fill_value=False) & (sc > sc.rolling(200).mean()),
        'QH08': qc.rolling(10).mean() > qc.rolling(20).mean(),
        'QH09': (sc > m150) & (m150 > m150.shift(20)), 'QH10': aktif(isy90),
    }
    return {n: v.fillna(False).astype(bool) for n, v in P.items()}


def harian_saham(pans, hu):
    """Bilangan saham layak (kedua-dua panel) setiap hari: naik, turun, naik >= 4 %, turun >= 4 %."""
    out = {k: np.zeros(len(hu)) for k in ('naik', 'turun', 'n4n', 'n4t')}
    for pan in pans.values():
        c = pan['c']
        r = np.full(len(c), np.nan)
        r[1:] = c[1:] / c[:-1] - 1
        r[pan['mula'][:-1]] = np.nan                                 # bar pertama setiap saham
        ly = pan['layak'] & ~np.isnan(r)
        d = np.searchsorted(hu, pan['tarikh'][ly])
        rr = r[ly]
        for k, m in (('naik', rr > 0), ('turun', rr < 0), ('n4n', rr >= 0.04), ('n4t', rr <= -0.04)):
            out[k] += np.bincount(d[m], minlength=len(hu))
    return pd.DataFrame(out, index=hu)


def siri_pasaran(pans, df):
    """DataFrame bool [hari x 33 prasyarat pasaran], lajur = kod PASARAN."""
    import cs_prasyarat as pr
    from AUTOTUNE.teras import data as D
    hu = np.array(sorted(df.date.unique()))
    L = df[df.layak].groupby('date').agg(b50=('a50', 'mean'), b200=('a200', 'mean'), b5=('d5', 'mean'))
    PM = {'Q' + k: v for k, v in pr.pasaran(hu, L).items()}
    ix = pd.read_parquet(D.ambil(tag='autotune-data-a02') / 'idx.parquet')
    ix['d'] = ix.date.dt.year * 10000 + ix.date.dt.month * 100 + ix.date.dt.day
    q = ix[ix.ticker == 'QQQ'].set_index('d')[['low', 'close', 'volume']].reindex(hu).ffill()
    s = ix[ix.ticker == 'SPY'].set_index('d')[['low', 'close', 'volume']].reindex(hu).ffill()
    PM.update(pakar(q, s, harian_saham(pans, hu)))
    return pd.DataFrame({n[:4]: PM[n[:4]].to_numpy() for n in PASARAN}, index=hu)


def anjak_saham(a, mula, k=ANJAK):
    """Anjak membulat k bar dalam setiap saham (plasebo lapisan kumpulan/syarikat)."""
    out = np.empty_like(a)
    for t in range(len(mula) - 1):
        out[..., mula[t]:mula[t + 1]] = np.roll(a[..., mula[t]:mula[t + 1]], k, axis=-1)
    return out


def bina(kerja):
    import cs_cari as cari
    import cs_prasyarat as pr
    sys.path.insert(0, cari.AKAR)
    from REVERSE.teras import data as RD
    pans = {s: cari.panel(kerja, s) for s in ('A', 'B')}
    peta = RD.peta_sektor(sorted(set(pans['A']['ticker']) | set(pans['B']['ticker'])))
    df = pr.kumpulan(pd.concat([pr.bingkai(pans[s], peta, s) for s in ('A', 'B')], ignore_index=True))
    H = siri_pasaran(pans, df)
    hu = H.index.to_numpy()
    Hm = H.to_numpy().T.astype(np.uint8)                              # [33, hari]
    Hp = np.roll(Hm, ANJAK, axis=1)
    H.astype(int).to_csv(os.path.join(kerja, 'prasyarat_harian.csv'))
    for s, pan in pans.items():
        d = df[df.panel == s].sort_values('bar')
        E = pr.earnings(pan)
        L2 = np.stack([d[n[1:4]].to_numpy() if n[1] in 'DE' else E[n[1:4]] for n in KUMPULAN]).astype(np.uint8)
        hi = np.searchsorted(hu, pan['tarikh'])
        out = {'L1': np.ascontiguousarray(Hm[:, hi]), 'L1p': np.ascontiguousarray(Hp[:, hi]), 'L2': L2,
               'L2p': anjak_saham(L2, pan['mula'])}
        pickle.dump(out, open(os.path.join(kerja, f'lapis_{s}.pkl'), 'wb'), protocol=4)
        sah = pan['sah']
        cari.log(f'lapis {s}: % bar sah benar — pasaran '
                 + ' '.join(f'{n[:4]}={out["L1"][i, sah].mean() * 100:.0f}' for i, n in enumerate(PASARAN)))
        cari.log(f'lapis {s}: kumpulan/syarikat '
                 + ' '.join(f'{n[:4]}={L2[i, sah].mean() * 100:.0f}' for i, n in enumerate(KUMPULAN)))


def muat(kerja, set_):
    return pickle.load(open(os.path.join(kerja, f'lapis_{set_}.pkl'), 'rb'))


if __name__ == '__main__':
    bina(sys.argv[1])
