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


def ftd(lo, cl, vol, aktif=20):
    """QH01: follow-through day aktif. lo, cl, vol = rendah, tutup, volum QQQ (ndarray). Pulangkan ndarray bool.
    aktif = bilangan sesi prasyarat kekal benar dari hari FTD (20 = pradaftar (i); grid tala pindaan (k))."""
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
                hingga = i + aktif - 1
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


# ---------- pindaan (k): prasyarat BERAMBANG untuk tala (CS06) ----------
# kod -> (grid ambang, nilai pradaftar (i), templat teks). Prasyarat tiada di sini tidak berambang dan kekal.
GRID_PRA = {
    'QA05': ([1, 2, 3, 5, 7], 3, 'QQQ dalam {}% dari puncak 52 minggu'),
    'QA06': ([5, 7.5, 10, 15, 20, 25], 10, 'QQQ >= {}% di bawah puncak'),
    'QA07': ([5, 7.5, 10, 15, 20, 25], 20, 'QQQ >= {}% di bawah puncak'),
    'QA08': ([5, 10, 15, 20, 30], 10, 'rejim ON baharu (<= {} sesi)'),
    'QA09': ([5, 10, 15, 20, 30], 10, 'rejim OFF baharu (<= {} sesi)'),
    'QA10': ([30, 35, 40, 45], 35, 'QQQ RSI14 < {}'),
    'QA11': ([2, 3, 4, 5], 3, 'QQQ naik >= {}% dalam 5 sesi'),
    'QB01': ([20, 25, 30, 35, 40], 25, 'turun-naik SPY 21 hari >= {}% setahun'),
    'QB02': ([8, 10, 12, 15], 10, 'turun-naik SPY 21 hari <= {}% setahun'),
    'QC01': ([50, 60, 70, 80], 60, '>= {}% saham di atas MA50'),
    'QC02': ([15, 20, 30, 40], 30, '<= {}% saham di atas MA50'),
    'QC03': ([5, 10, 15, 20], 10, 'keluasan naik >= {} mata dalam 10 sesi'),
    'QC04': ([50, 60, 70], 60, '>= {}% saham di atas MA200'),
    'QC05': ([10, 15, 20, 30], 15, '>= {}% saham dalam 5% dari puncak 52 minggu'),
    'QG03': ([5, 7, 10], 7, '{} hari pertama bulan'),
    'QH01': ([10, 20, 30], 20, 'follow-through day aktif (QQQ, {} sesi)'),
    'QH02': ([1, 2, 3], 2, 'distribution day QQQ <= {} dalam 25 sesi'),
    'QH03': ([4, 5, 6, 7], 5, 'distribution day QQQ >= {} dalam 25 sesi'),
    'QH04': ([10, 20, 30], 20, 'breadth thrust Zweig aktif ({} sesi)'),
    'QH05': ([1.5, 2, 3], 2, 'nisbah 4% (10 hari) > {}'),
    'QH06': ([0.33, 0.5, 0.67], 0.5, 'nisbah 4% (10 hari) < {}'),
    'QH10': ([10, 20, 30], 20, 'hari 90% turun kemudian naik ({} sesi)'),
    'QD01': ([2, 3, 4], 3, 'sektor {} teratas (pulangan 63 sesi)'),
    'QD02': ([2, 3, 4], 3, 'sektor {} terbawah (pulangan 63 sesi)'),
    'QD03': ([50, 60, 70], 60, '>= {}% saham sektor di atas MA50'),
    'QE01': ([10, 20, 30], 20, 'industri {}% teratas (pulangan 63 sesi)'),
    'QE02': ([10, 20, 30], 20, 'industri {}% teratas (pulangan 21 sesi)'),
    'QE03': ([10, 20, 30], 20, 'industri {}% terbawah (pulangan 63 sesi)'),
    'QE04': ([50, 60, 70], 60, '>= {}% saham industri di atas MA50'),
    'QE05': ([15, 20, 30], 20, 'saham lain dalam industri sama naik >= {}% dalam 20 sesi'),
    'QF01': ([2, 3, 5, 7, 10], 5, 'earnings dalam 1-{} sesi akan datang'),
    'QF02': ([2, 4, 7], 4, '0-{} sesi selepas earnings'),
    'QF03': ([14, 19, 29], 19, '5-{} sesi selepas earnings'),
    'QF04': ([10, 20, 30], 20, 'tiada earnings dalam {} sesi akan datang'),
    'QF06': ([10, 20, 30, 50], 20, 'hasil suku terkini tumbuh >= {}%'),
    'QF07': ([3, 5, 8], 5, 'harga melompat >= {}% pada hari earnings (20 sesi lalu)'),
}


class Mentah:
    """Ciri mentah prasyarat bagi kedua-dua kumpulan, supaya ambang boleh ditala (pindaan (k)). Formula sama seperti
    `cs_prasyarat.pasaran/kumpulan/earnings` dan `pakar()`; `semak()` mengesahkan nilai pradaftar menghasilkan lapisan (i)."""

    def __init__(self, kerja):
        import cs_cari as cari
        import cs_prasyarat as pr
        from AUTOTUNE.teras import data as D
        sys.path.insert(0, cari.AKAR)
        from REVERSE.teras import data as RD
        self.pr, self.kerja = pr, kerja
        self.pans = {s: cari.panel(kerja, s) for s in ('A', 'B')}
        peta = RD.peta_sektor(sorted(set(self.pans['A']['ticker']) | set(self.pans['B']['ticker'])))
        df = pd.concat([pr.bingkai(self.pans[s], peta, s) for s in ('A', 'B')], ignore_index=True)
        self._kumpulan(df)
        hu = self.hu = np.array(sorted(df.date.unique()))
        L = df[df.layak].groupby('date').agg(b50=('a50', 'mean'), b200=('a200', 'mean'), b5=('d5', 'mean')).reindex(hu)
        ix = pd.read_parquet(D.ambil(tag='autotune-data-a02') / 'idx.parquet')
        ix['d'] = ix.date.dt.year * 10000 + ix.date.dt.month * 100 + ix.date.dt.day
        q = ix[ix.ticker == 'QQQ'].set_index('d')[['low', 'close', 'volume']].reindex(hu).ffill()
        s = ix[ix.ticker == 'SPY'].set_index('d')[['low', 'close', 'volume']].reindex(hu).ffill()
        qc, sc = q.close, s.close
        m50 = qc.rolling(50).mean()
        on = (qc > m50) & (qc.rolling(10).mean() > qc.rolling(20).mean())
        H = harian_saham(self.pans, hu)
        nisbah = H.naik / (H.naik + H.turun).replace(0, np.nan)
        ema = nisbah.ewm(span=10, adjust=False).mean()
        turun90 = (1 - nisbah) >= 0.90
        naik = (nisbah >= 0.90) | ((nisbah >= 0.80) & (nisbah.shift(1) >= 0.80))
        self.h = dict(
            q=q, qc=qc, qmax=qc.rolling(252).max(), on=on, off=(~on) & m50.notna(),
            umur=on.groupby((on != on.shift()).cumsum()).cumcount() + 1, rsi=pr._rsi(qc), r5=qc / qc.shift(5) - 1,
            rv21=sc.pct_change().rolling(21).std() * np.sqrt(252), b50=L.b50, b200=L.b200, b5=L.b5,
            hari=pd.Series(hu % 100, index=hu),
            dd=((qc / qc.shift() - 1 <= -0.002) & (q.volume > q.volume.shift())).astype(float).rolling(25).sum(),
            thrust=(ema > 0.615) & (ema.shift(1).rolling(10).min() < 0.40),
            n4=H.n4n.rolling(10).sum() / H.n4t.rolling(10).sum().replace(0, np.nan),
            isy90=naik & (turun90.astype(float).shift(1).rolling(10).max() > 0))
        self.hi = {s: np.searchsorted(hu, self.pans[s]['tarikh']) for s in ('A', 'B')}
        self.E = {s: self._earnings(self.pans[s]) for s in ('A', 'B')}

    def _kumpulan(self, df):
        """Lajur mentah sektor/industri setiap bar (logik `cs_prasyarat.kumpulan`)."""
        L = df[df.layak]
        s = L[L.sektor >= 0].groupby(['date', 'sektor']).agg(m=('r63', 'median'), sb=('a50', 'mean')).reset_index()
        s['kd'] = s.groupby('date').m.rank(ascending=False, method='first')
        s['ns'] = s.groupby('date').m.transform('count')
        Li = L[L.industri >= 0].assign(**{f'k{x}': lambda d, x=x: d.r20 >= x / 100 for x in (15, 20, 30)})
        i = Li.groupby(['date', 'industri']).agg(m63=('r63', 'median'), m21=('r21', 'median'), ib=('a50', 'mean'),
                                                 n=('a50', 'size'), k15=('k15', 'sum'), k20=('k20', 'sum'),
                                                 k30=('k30', 'sum')).reset_index()
        i = i[i.n >= 5]
        i['p63'] = i.groupby('date').m63.rank(pct=True)
        i['p21'] = i.groupby('date').m21.rank(pct=True)
        df = df.merge(s[['date', 'sektor', 'kd', 'ns', 'sb']], on=['date', 'sektor'], how='left')
        df = df.merge(i[['date', 'industri', 'p63', 'p21', 'ib', 'k15', 'k20', 'k30']], on=['date', 'industri'], how='left')
        self.K = {}
        for p_ in ('A', 'B'):
            d = df[df.panel == p_].sort_values('bar')
            k = {c: d[c].to_numpy(np.float32) for c in ('kd', 'ns', 'sb', 'p63', 'p21', 'ib')}
            for x in (15, 20, 30):
                sendiri = ((d.r20 >= x / 100) & d.layak).to_numpy().astype(int)
                k[f'e05_{x}'] = (d[f'k{x}'].fillna(0).to_numpy() - sendiri) >= 1
            self.K[p_] = k

    def _earnings(self, pan):
        """hingga / sejak / reaksi / tumbuh hasil setiap bar (logik `cs_prasyarat.earnings`)."""
        pr = self.pr
        e = pd.read_csv(os.path.join(pr.BS2, 'data', 'sec', 'earnings_8k.csv'),
                        usecols=['saham', 'tarikh_fail', 'masa_terima', 'items'])
        e = e[e['items'].astype(str).str.contains('2.02', regex=False)]
        e['d'] = e.tarikh_fail.str.replace('-', '').astype(int)
        e['lewat'] = pd.to_datetime(e.masa_terima, errors='coerce', utc=True).dt.hour >= 20
        su = pd.read_csv(os.path.join(pr.BS2, 'data', 'sec', 'sue.csv'), usecols=['saham', 'sue', 'tumbuh_hasil', 'tarikh_umum'])
        su = su.dropna(subset=['tarikh_umum'])
        su['d'] = su.tarikh_umum.str.replace('-', '').astype(int)
        eg, sg = dict(tuple(e.groupby('saham'))), dict(tuple(su.sort_values('d').groupby('saham')))
        N = len(pan['c'])
        out = {'hingga': np.full(N, 10 ** 6, np.int64), 'sejak': np.full(N, 10 ** 6, np.int64), 'ada_n': np.zeros(N, bool),
               'reaksi': np.full(N, np.nan), 'th': np.full(N, np.nan), 'ok': np.zeros(N, bool)}
        c, tarikh, mula = pan['c'], pan['tarikh'], pan['mula']
        for t, nama in enumerate(pan['ticker']):
            a, b = mula[t], mula[t + 1]
            d = tarikh[a:b]
            T = b - a
            if nama in eg:
                g = eg[nama]
                ev = np.where(g.lewat.to_numpy(), np.searchsorted(d, g.d.to_numpy(), 'right'),
                              np.searchsorted(d, g.d.to_numpy(), 'left'))
                ev = np.unique(ev[(ev > 0) & (ev < T)])
                if len(ev):
                    i = np.arange(T)
                    kn = np.searchsorted(ev, i, 'right')
                    ada_n = kn < len(ev)
                    ada_l = kn > 0
                    lalu = ev[np.maximum(kn - 1, 0)]
                    out['hingga'][a:b] = np.where(ada_n, ev[np.minimum(kn, len(ev) - 1)] - i, 10 ** 6)
                    out['sejak'][a:b] = np.where(ada_l, i - lalu, 10 ** 6)
                    out['reaksi'][a:b] = np.where(ada_l, c[a + lalu] / c[a + np.maximum(lalu - 1, 0)] - 1, np.nan)
                    out['ada_n'][a:b] = ada_n
            if nama in sg:
                g = sg[nama]
                k = np.searchsorted(g.d.to_numpy(), d, 'left') - 1
                out['ok'][a:b] = k >= 0
                out['th'][a:b] = g.tumbuh_hasil.to_numpy()[np.maximum(k, 0)]
        return out

    def siri(self, kod, x):
        """Siri bool setiap HARI bagi prasyarat pasaran `kod` pada ambang x."""
        h = self.h
        aktif = lambda v, k: v.astype(float).rolling(int(k), min_periods=1).max() > 0
        f = {
            'QA05': lambda: h['qc'] >= (1 - x / 100) * h['qmax'], 'QA06': lambda: h['qc'] <= (1 - x / 100) * h['qmax'],
            'QA07': lambda: h['qc'] <= (1 - x / 100) * h['qmax'], 'QA08': lambda: h['on'] & (h['umur'] <= x),
            'QA09': lambda: h['off'] & (h['umur'] <= x), 'QA10': lambda: h['rsi'] < x, 'QA11': lambda: h['r5'] >= x / 100,
            'QB01': lambda: h['rv21'] >= x / 100, 'QB02': lambda: h['rv21'] <= x / 100, 'QC01': lambda: h['b50'] >= x / 100,
            'QC02': lambda: h['b50'] <= x / 100, 'QC03': lambda: h['b50'] - h['b50'].shift(10) >= x / 100,
            'QC04': lambda: h['b200'] >= x / 100, 'QC05': lambda: h['b5'] >= x / 100, 'QG03': lambda: h['hari'] <= x,
            'QH01': lambda: pd.Series(ftd(h['q'].low.to_numpy(float), h['qc'].to_numpy(float),
                                          h['q'].volume.to_numpy(float), int(x)), index=self.hu),
            'QH02': lambda: h['dd'] <= x, 'QH03': lambda: h['dd'] >= x, 'QH04': lambda: aktif(h['thrust'], x),
            'QH05': lambda: h['n4'] > x, 'QH06': lambda: h['n4'] < x, 'QH10': lambda: aktif(h['isy90'], x),
        }[kod]()
        return f.fillna(False).astype(bool).to_numpy()

    def bar(self, set_, kod, x):
        """Topeng bool setiap BAR kumpulan `set_` bagi prasyarat `kod` pada ambang x."""
        if kod[1] in 'ABCGH':
            return self.siri(kod, x)[self.hi[set_]]
        K, E = self.K[set_], self.E[set_]
        with np.errstate(invalid='ignore'):
            return {
                'QD01': lambda: K['kd'] <= x, 'QD02': lambda: K['kd'] > K['ns'] - x, 'QD03': lambda: K['sb'] >= x / 100,
                'QE01': lambda: K['p63'] >= 1 - x / 100, 'QE02': lambda: K['p21'] >= 1 - x / 100,
                'QE03': lambda: K['p63'] <= x / 100, 'QE04': lambda: K['ib'] >= x / 100, 'QE05': lambda: K[f'e05_{int(x)}'],
                'QF01': lambda: (E['hingga'] >= 1) & (E['hingga'] <= x), 'QF02': lambda: E['sejak'] <= x,
                'QF03': lambda: (E['sejak'] >= 5) & (E['sejak'] <= x), 'QF04': lambda: E['ada_n'] & (E['hingga'] > x),
                'QF06': lambda: E['ok'] & (E['th'] >= x / 100), 'QF07': lambda: (E['sejak'] <= 19) & (E['reaksi'] >= x / 100),
            }[kod]()

    def semak(self):
        """Bilangan bar SAH yang berbeza daripada lapisan (i) pada nilai pradaftar, setiap prasyarat berambang."""
        beza = {}
        for s_ in ('A', 'B'):
            Lp, sah = muat(self.kerja, s_), self.pans[s_]['sah']
            for kod, (_, asal, _) in GRID_PRA.items():
                lap, senarai = (0, PASARAN) if kod[1] in 'ABCGH' else (1, KUMPULAN)
                i = [n[:4] for n in senarai].index(kod)
                beza[f'{kod}_{s_}'] = int(((Lp['L1' if lap == 0 else 'L2'][i] > 0) != self.bar(s_, kod, asal))[sah].sum())
        return beza


if __name__ == '__main__':
    bina(sys.argv[1])
