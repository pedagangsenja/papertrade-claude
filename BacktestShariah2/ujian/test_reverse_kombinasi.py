"""Ujian unit bagi REVERSE/step17_kombinasi.py (silang MA, RSI, sasaran untung, grid dikunci)."""
import sys
import unittest
from pathlib import Path

import numpy as np
import pandas as pd

AKAR = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(AKAR))
from REVERSE import step17_kombinasi as KB  # noqa: E402


def rangka(c, n_bar=None):
    c = np.asarray(c, dtype='float64')
    n = len(c)
    return pd.DataFrame({'ticker': 'T',
                         'date': pd.bdate_range('2012-01-02', periods=n),
                         'open': c, 'high': c * 1.01, 'low': c * 0.99,
                         'close': c, 'volume': 1e8})


class TestGridDikunci(unittest.TestCase):
    """Spec §3/§4: 10 masuk x 4 keluar; melebarkannya memerlukan pradaftar baharu."""

    def test_empat_keluar(self):
        self.assertEqual(sorted(KB.XKELUAR), ['X1', 'X2', 'X3', 'X4'])

    def test_dua_keluar_ada_sasaran_untung(self):
        """Bahagian yang benar-benar baharu: kajian belum pernah uji sasaran untung."""
        sasar = [k for k, (h, s, u) in KB.XKELUAR.items() if isinstance(s, float)]
        self.assertEqual(sorted(sasar), ['X1', 'X2'])
        self.assertEqual(KB.XKELUAR['X1'], (1.5, 1.0, None))
        self.assertEqual(KB.XKELUAR['X2'], (2.0, 4.0, None))

    def test_x3_ialah_asas_kajian(self):
        self.assertEqual(KB.XKELUAR['X3'], (2.0, None, KB.UFUK))

    def test_x4_ekor(self):
        self.assertEqual(KB.XKELUAR['X4'], (2.0, 'ekor', None))

    def test_sepuluh_gabungan_masuk(self):
        d = KB.siri_ticker(rangka(100 + 0.1 * np.arange(400)))
        self.assertEqual(len(KB.gabungan(d)), 10)

    def test_ma10_ma20_ada(self):
        """Pengguna meminta MA10 x MA20 secara khusus; ia memang tiada dalam 71 lajur lama."""
        d = KB.siri_ticker(rangka(100 + 0.1 * np.arange(400)))
        self.assertIn('x_ma10_ma20', d.columns)
        self.assertTrue(any('ma10 silang ma20' in k for k in KB.gabungan(d)))

    def test_pecahan_tidak_bertindih(self):
        self.assertLess(KB.LATIH[1], KB.TAHAN[0])


class TestSilang(unittest.TestCase):
    def test_silang_dikesan_sekali_sahaja(self):
        # Turun 120 bar kemudian naik tajam: MA10 melintasi MA20 sekali.
        c = np.concatenate([np.linspace(200, 100, 160), np.linspace(100, 260, 160)])
        d = KB.siri_ticker(rangka(c))
        self.assertEqual(int(d.x_ma10_ma20.sum()), 1)

    def test_tiada_silang_bila_menaik_tetap(self):
        d = KB.siri_ticker(rangka(100 * np.exp(0.002 * np.arange(400))))
        self.assertEqual(int(d.x_ma10_ma20.sum()), 0)

    def test_ma_tersusun_betul_dalam_trend(self):
        d = KB.siri_ticker(rangka(100 + 0.3 * np.arange(400)))
        r = d.iloc[-1]
        self.assertGreater(r.ma10, r.ma20)
        self.assertGreater(r.ma20, r.ma50)
        self.assertGreater(r.ma50, r.ma200)


class TestRsi(unittest.TestCase):
    def test_rsi_menaik_tulen_hampir_100(self):
        d = KB.siri_ticker(rangka(100 + np.arange(400)))
        self.assertGreater(float(d.rsi14.iloc[-1]), 95)

    def test_rsi_menurun_tulen_hampir_0(self):
        d = KB.siri_ticker(rangka(500 - np.arange(400)))
        self.assertLess(float(d.rsi14.iloc[-1]), 5)

    def test_rsi_dalam_julat_sah(self):
        rng = np.random.default_rng(2)
        d = KB.siri_ticker(rangka(100 + np.cumsum(rng.normal(0, 1, 400))))
        v = d.rsi14.dropna().to_numpy()
        self.assertTrue(((v >= 0) & (v <= 100)).all())


class TestSasaranUntung(unittest.TestCase):
    def test_sasaran_memotong_pulangan_dalam_trend_menaik(self):
        """Dalam trend menaik berterusan, sasaran 1xATR mesti memberi KURANG daripada 63 sesi."""
        d = KB.siri_ticker(rangka(100 * np.exp(0.004 * np.arange(500))))
        x1 = float(np.nanmean(d.pul_X1.to_numpy()[100:300]))
        x3 = float(np.nanmean(d.pul_X3.to_numpy()[100:300]))
        self.assertLess(x1, x3)

    def test_sasaran_4atr_antara_1atr_dan_tiada(self):
        d = KB.siri_ticker(rangka(100 * np.exp(0.004 * np.arange(500))))
        a = [float(np.nanmean(d[f'pul_{k}'].to_numpy()[100:300])) for k in ('X1', 'X2', 'X3')]
        self.assertLess(a[0], a[1])
        self.assertLess(a[1], a[2])

    def test_harga_tetap_memberi_kos_sahaja(self):
        d = KB.siri_ticker(rangka(np.full(400, 100.0)))
        for k in KB.XKELUAR:
            v = d[f'pul_{k}'].to_numpy()[50:300]
            v = v[np.isfinite(v)]
            self.assertTrue((v < 0).all(), k)
            self.assertTrue((v > -0.05).all(), k)

    def test_tiada_pandang_hadapan(self):
        c = 100 * np.exp(0.002 * np.arange(400))
        a = KB.siri_ticker(rangka(c))
        c2 = c.copy()
        c2[-1] = 99999.0
        b = KB.siri_ticker(rangka(c2))
        for k in KB.XKELUAR:
            np.testing.assert_allclose(a[f'pul_{k}'].to_numpy()[:200],
                                       b[f'pul_{k}'].to_numpy()[:200], rtol=1e-6)


class TestMetrik(unittest.TestCase):
    def test_jangkaan_dan_kadar_menang(self):
        m = KB.metrik(np.array([0.02] * 30 + [-0.01] * 70))
        self.assertAlmostEqual(m['menang'], 30.0, places=6)
        self.assertAlmostEqual(m['jangkaan'], -0.1, places=6)

    def test_kosong(self):
        self.assertEqual(KB.metrik(np.array([np.nan]))['n'], 0)


if __name__ == '__main__':
    unittest.main()
