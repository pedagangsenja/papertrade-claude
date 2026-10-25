# Ujian statistik dan alam kajian PIT (kajian/pit/statistik.py, alam.py, playbook.py, uji_pit.pintu_b).
import math, os, sys, tempfile, unittest

import numpy as np
import pandas as pd

BS2 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BS2, 'kajian', 'pit'))
import statistik as ST    # noqa: E402
import alam as AL         # noqa: E402
import playbook as PB     # noqa: E402
import uji_pit as U       # noqa: E402


class TestStatistik(unittest.TestCase):
    def test_t_berkelompok(self):
        x = np.array([1.0, 3.0, 2.0, 6.0]); g = np.array(['a', 'a', 'b', 'b'])
        r = ST.t_berkelompok(x, g)
        # purata 3; baki kelompok a: (-2)+0 = -2, b: (-1)+3 = 2; SE^2 = 2/1*(4+4)/16 = 1
        self.assertAlmostEqual(r['purata'], 3.0); self.assertAlmostEqual(r['se'], 1.0); self.assertAlmostEqual(r['t'], 3.0)
        self.assertEqual((r['n'], r['G']), (4, 2))
        self.assertTrue(math.isnan(ST.t_berkelompok([1.0, 2.0], ['a', 'a'])['t']))

    def test_kelompok_lebih_ketat_daripada_iid(self):
        rng = np.random.default_rng(1)
        g = np.repeat(np.arange(40), 50); x = np.repeat(rng.normal(0, 1, 40), 50) + rng.normal(0, 0.1, 2000)
        r = ST.t_berkelompok(x, g)
        se_iid = x.std(ddof=1) / math.sqrt(len(x))
        self.assertGreater(r['se'], 3 * se_iid)

    def test_sr0_dan_dsr(self):
        self.assertEqual(ST.sr0(0.0, 100), 0.0)
        a, b = ST.sr0(0.01, 10), ST.sr0(0.01, 1000)
        self.assertGreater(b, a)
        rng = np.random.default_rng(2)
        r = pd.Series(rng.normal(0.001, 0.01, 2500))
        self.assertGreater(ST.dsr(r, 0.0), 0.99)
        self.assertLess(ST.dsr(r, 0.2), 0.01)

    def test_pbo(self):
        rng = np.random.default_rng(3)
        R = rng.normal(0, 0.01, (800, 20))                     # tiada kemahiran: PBO sekitar 0.5
        p = ST.pbo_cscv(R, S=8)['pbo']
        self.assertTrue(0.2 < p < 0.8)
        R2 = R.copy(); R2[:, 0] += 0.003                       # satu calon benar-benar baik: PBO rendah
        self.assertLess(ST.pbo_cscv(R2, S=8)['pbo'], 0.1)

    def test_rawak_tepat_dan_berbenih(self):
        t = pd.bdate_range('2020-01-01', periods=6)
        O = np.array([[10, 20], [10, 20], [11, 22], [12, 24], [13, 26], [14, 28]], float)
        Cf = O + 0.5
        E = np.ones((6, 2), bool); E[:, 1] = False                # hanya ticker 0 layak
        T = pd.DataFrame(dict(sig=[t[0], t[1]], ent=[t[1], t[2]], ex=[t[3], t[4]], jenis=['tutup', 'buka']))
        r = ST.rawak(T, O, Cf, E, t, benih=range(3), kos=0.0)
        self.assertAlmostEqual(r[0], 12.5 / 10 - 1); self.assertAlmostEqual(r[1], 13 / 11 - 1)
        E2 = np.ones((6, 2), bool)
        a = ST.rawak(T, O, Cf, E2, t, benih=range(20)); b = ST.rawak(T, O, Cf, E2, t, benih=range(20))
        np.testing.assert_array_equal(a, b)

    def test_cagr_mdd(self):
        s = pd.Series([1.0, 1.21], index=pd.to_datetime(['2020-01-01', '2022-01-01']))
        self.assertAlmostEqual(ST.cagr(s), 1.21 ** (365.25 / 731) - 1, places=6)
        self.assertAlmostEqual(ST.mdd(pd.Series([1, 2, 1, 3.0])), -0.5)


class TestAlam(unittest.TestCase):
    def _panjang(self):
        d = pd.bdate_range('2020-01-01', periods=300)
        rows = []
        for t, harga, vol in (('AAA', 12.0, 1e6), ('BBB', 8.0, 1e7), ('CCC', 50.0, 1e4)):
            for k, x in enumerate(d):
                rows.append((t, x, harga, harga, harga, harga, vol, 1.0))
        return pd.DataFrame(rows, columns=['ticker', 'date', 'open', 'high', 'low', 'close', 'volume', 'faktor_split'])

    def test_syarat_layak_ikut_tarikh(self):
        d = AL.ciri_layak(self._panjang())
        a = d[d.ticker == 'AAA']
        # AAA: USD12 x 1 juta = 12 juta nilai; layak bermula bar ke-252 (sejarah >= 252), bukan sebelum
        self.assertFalse(a.layak.iloc[250]); self.assertTrue(a.layak.iloc[251])
        self.assertFalse(d[d.ticker == 'BBB'].layak.any())    # < USD10
        self.assertFalse(d[d.ticker == 'CCC'].layak.any())    # nilai 0.5 juta < 5 juta

    def test_faktor_split_harga_mentah(self):
        x = self._panjang(); x.loc[x.ticker == 'BBB', 'faktor_split'] = 2.0    # tutup dilaras 8 = mentah 16
        d = AL.ciri_layak(x)
        self.assertTrue(d[d.ticker == 'BBB'].layak.iloc[260])

    def test_saringan_sektor(self):
        with tempfile.TemporaryDirectory() as td:
            pd.DataFrame(dict(ticker=['AAA', 'BAN.K', 'BEER'], industri=['Semiconductors', 'Banks - Regional', 'Beverages - Brewers'],
                              plate_code='x')).to_csv(os.path.join(td, 'p.csv'), index=False)
            pd.DataFrame(dict(ticker=['TVX', 'TVB'], industry=['Semiconductors', 'Major Banks'])).to_csv(os.path.join(td, 't.csv'),
                                                                                                   index=False)
            s = AL.peta_shariah(['AAA', 'BAN-K', 'BEER', 'TVX', 'TVB', 'ZZZ', 'HRL'], os.path.join(td, 'p.csv'),
                                os.path.join(td, 't.csv'))
            self.assertEqual(s.ok.to_dict(), dict(AAA=True, **{'BAN-K': False}, BEER=False, TVX=True, TVB=False, ZZZ=False,
                                                  HRL=False))
            self.assertEqual(s.loc['ZZZ', 'sebab'], 'tiada industri'); self.assertEqual(s.loc['HRL', 'sebab'], 'babi')

    def test_ew_tutup_semalam(self):
        d = pd.bdate_range('2020-01-01', periods=3)
        C = pd.DataFrame({'A': [10, 11, 12.1], 'B': [10, 5, 5.0]}, index=d)
        M = pd.DataFrame({'A': [True, True, True], 'B': [False, True, True]}, index=d)
        r, n = AL.ew_harian(C, M)
        self.assertAlmostEqual(r.iloc[1], 0.10)               # B tidak layak pada tutup semalam (hari 0)
        self.assertAlmostEqual(r.iloc[2], (0.10 + 0.0) / 2)
        self.assertEqual(list(n), [0, 1, 2])

    def test_ew_had_50(self):
        d = pd.bdate_range('2020-01-01', periods=2)
        C = pd.DataFrame({'A': [10, 40.0]}, index=d); M = pd.DataFrame({'A': [True, True]}, index=d)
        self.assertAlmostEqual(AL.ew_harian(C, M)[0].iloc[1], 0.5)


class TestPlaybookDanPintu(unittest.TestCase):
    def test_playbook_tanpa_pandang_hadapan(self):
        rng = np.random.default_rng(5)
        d = pd.bdate_range('2018-01-01', periods=700)
        fr = {}
        for k in range(12):
            c = 30 * np.exp(np.cumsum(rng.normal(0.0008 * (k % 4), 0.012, 700)))
            fr[f'S{k}'] = pd.DataFrame(dict(open=c, high=c * 1.01, low=c * 0.99, close=c, volume=1e6, turnover=c * 1e6), index=d)
        penuh = {t: g.copy() for t, g in fr.items()}; PB.sedia(penuh, {})
        potong = {t: g.iloc[:600].copy() for t, g in fr.items()}; PB.sedia(potong, {})
        for t in fr:
            pd.testing.assert_series_equal(penuh[t].sig.iloc[:600], potong[t].sig, check_names=False)
        self.assertTrue(any(g.sig.any() for g in penuh.values()))

    def test_pintu_b(self):
        v = dict(n_dagangan=100, bulan=60, lebihan_rawak=0.004, t_rawak=3.2, cagr=0.2, ew_cagr=0.1, cagr_tanpa10=0.15)
        self.assertEqual(U.pintu_b(v, 0.7), (True, []))
        ok, s = U.pintu_b(dict(v, t_rawak=2.9, cagr_tanpa10=0.09), 0.4)
        self.assertFalse(ok); self.assertEqual([x.split(' ')[0] for x in s], ['B1', 'B3', 'B4'])
        self.assertIn('B0 data tidak cukup', U.pintu_b(dict(v, n_dagangan=10), 0.7)[1])


if __name__ == '__main__':
    unittest.main()
