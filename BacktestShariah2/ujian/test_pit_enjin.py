# Ujian enjin kajian v1.3 (kajian/pit/enjin_v13.py) lawan enjin v1.2 (kod/enjin.py, beku).
import os, sys, unittest

import numpy as np
import pandas as pd

BS2 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BS2, 'kod'))
sys.path.insert(0, os.path.join(BS2, 'kajian', 'pit'))
import enjin as V12        # noqa: E402
import enjin_v13 as V13    # noqa: E402


def _data(seed=0, n_t=6, n=420, mula='2019-06-03', jurang_bawah=False):
    """Bingkai sintetik: rawak berjalan; isyarat/henti/sasaran/keluar rawak. jurang_bawah=False -> buka hari masuk sentiasa
    > henti (pembaikan [B1] tidak tercetus)."""
    rng = np.random.default_rng(seed)
    fr = {}
    d = pd.bdate_range(mula, periods=n)
    for k in range(n_t):
        c = 50 * np.exp(np.cumsum(rng.normal(0, 0.02, n)))
        o = c * np.exp(rng.normal(0, 0.01, n))
        h = np.maximum(o, c) * (1 + rng.uniform(0, 0.02, n)); l = np.minimum(o, c) * (1 - rng.uniform(0, 0.02, n))
        g = pd.DataFrame(dict(open=o, high=h, low=l, close=c, volume=1e6), index=d)
        g['sig'] = rng.random(n) < 0.05
        # henti di bawah rendah hari ini; buka esok mesti > henti jika jurang_bawah False
        st = l * (1 - rng.uniform(0.0, 0.08, n))
        nxt = np.r_[o[1:], o[-1]]
        if not jurang_bawah:
            st = np.minimum(st, nxt * 0.97)
        else:
            st = np.where(rng.random(n) < 0.3, nxt * 1.02, st)
        g['stop'] = np.where(rng.random(n) < 0.8, st, np.nan)
        g['tgt'] = np.where(rng.random(n) < 0.5, c * (1 + rng.uniform(0.03, 0.15, n)), np.nan)
        g['exitc'] = rng.random(n) < 0.03
        g['rank'] = rng.random(n)
        fr[f'T{k}'] = g
    return fr


class TestKesetaraan(unittest.TestCase):
    def test_trades_portfolio_sama_v12(self):
        for seed in range(4):
            for tmax in (None, 10):
                fr = _data(seed)
                a = V12.trades({t: g.copy() for t, g in fr.items()}, tmax=tmax, warm=5)
                b = V13.trades({t: g.copy() for t, g in fr.items()}, tmax=tmax, warm=5, kos=V13.COST_V12, jurang=False)
                pd.testing.assert_frame_equal(a.reset_index(drop=True), b.drop(columns='jenis').reset_index(drop=True))
                # jurang=True juga sama kerana buka hari masuk sentiasa > henti
                c = V13.trades({t: g.copy() for t, g in fr.items()}, tmax=tmax, warm=5, kos=V13.COST_V12, jurang=True)
                pd.testing.assert_frame_equal(b, c)
                ca = V12.portfolio(a, fr)
                cb, P = V13.portfolio(b.drop(columns='jenis'), fr, mula=V13.START_V12, pulang_dagangan=True)
                pd.testing.assert_series_equal(ca, cb, check_exact=True)
                self.assertTrue(len(P) > 0)
                self.assertTrue(set(P.index) <= set(b.index))

    def test_jurang_hari_masuk_b1(self):
        d = pd.bdate_range('2020-01-01', periods=6)
        g = pd.DataFrame(dict(open=[10, 8, 9, 9, 9, 9.0], high=[10, 9.5, 9.5, 9.5, 9.5, 9.5], low=[9.8, 7.5, 8.8, 8.8, 8.8, 8.8],
                              close=[10, 9, 9, 9, 9, 9.0], volume=1.0), index=d)
        g['sig'] = [True, False, False, False, False, False]; g['stop'] = 9.0
        a = V12.trades({'X': g.copy()}, warm=0)
        b = V13.trades({'X': g.copy()}, warm=0, kos=V13.COST_V12)
        # v1.2: keluar pada paras henti 9 walaupun buka 8 (untung palsu); v1.3: keluar pada buka 8
        self.assertAlmostEqual(a.ret.iloc[0], 9 / 8 * 0.999 / 1.001 - 1)
        self.assertAlmostEqual(b.ret.iloc[0], 0.999 / 1.001 - 1)
        self.assertEqual((b.why.iloc[0], b.jenis.iloc[0], int(b.days.iloc[0])), ('henti', 'buka', 1))

    def test_kos_dan_delist(self):
        d = pd.bdate_range('2020-01-01', periods=5)
        g = pd.DataFrame(dict(open=[10, 10, 11, 12, 13.0], high=13.0, low=9.0, close=[10, 11, 12, 13, 14.0], volume=1.0), index=d)
        g['sig'] = [True, False, False, False, False]
        t = V13.trades({'X': g.copy()}, warm=0, akhir_data=d[-1] + pd.Timedelta(days=30))
        self.assertEqual(t.why.iloc[0], 'delist')
        self.assertAlmostEqual(t.ret.iloc[0], 14 / 10 * (1 - 0.0025) / (1 + 0.0025) - 1)
        t2 = V13.trades({'X': g.copy()}, warm=0, akhir_data=d[-1])
        self.assertEqual(t2.why.iloc[0], 'hujung')

    def test_jenis_keluar(self):
        fr = _data(7, jurang_bawah=True)
        t = V13.trades(fr, warm=5)
        ok = {'buka', 'intrahari', 'tutup'}
        self.assertTrue(set(t.jenis) <= ok)
        self.assertTrue((t[t.why == 'isyarat keluar'].jenis == 'buka').all())
        self.assertTrue((t[t.why == 'masa'].jenis == 'tutup').all() if len(t[t.why == 'masa']) else True)
        # [B1] tercetus sekurang-kurangnya sekali dengan jurang_bawah
        self.assertTrue(((t.why == 'henti') & (t.days == 1) & (t.jenis == 'buka')).any())


if __name__ == '__main__':
    unittest.main()
