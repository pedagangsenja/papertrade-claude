"""Ujian unit bagi REVERSE/step16_sistem.py (skor Clenow, parameter dikunci, pariti risiko)."""
import sys
import unittest
from pathlib import Path

import numpy as np

AKAR = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(AKAR))
from REVERSE import step16_sistem as SS  # noqa: E402


class TestSkorClenow(unittest.TestCase):
    def test_eksponen_tulen_tepat(self):
        """Kenaikan eksponen tulen: skor = exp(cerun x 252) - 1 kerana R2 = 1."""
        for k in (0.0005, 0.001, 0.002):
            c = 100 * np.exp(k * np.arange(200))
            self.assertAlmostEqual(float(SS.regresi_skor(c)[-1]), np.exp(k * 252) - 1, places=3)

    def test_menurun_memberi_negatif(self):
        c = 100 * np.exp(-0.001 * np.arange(200))
        self.assertLess(float(SS.regresi_skor(c)[-1]), 0)

    def test_hingar_rata_hampir_sifar(self):
        c = 100 + np.random.default_rng(1).normal(0, 5, 300)
        self.assertLess(abs(float(SS.regresi_skor(c)[-1])), 0.05)

    def test_r2_menghukum_laluan_bergelora(self):
        """Dua saham dengan hanyutan SAMA: yang lebih bergelora mesti mendapat skor LEBIH RENDAH."""
        n = 300
        licin = 100 * np.exp(0.001 * np.arange(n))
        gelora = licin * np.exp(np.random.default_rng(3).normal(0, 0.05, n))
        self.assertGreater(float(SS.regresi_skor(licin)[-1]), float(SS.regresi_skor(gelora)[-1]))

    def test_nan_sebelum_tingkap_penuh(self):
        c = 100 * np.exp(0.001 * np.arange(200))
        sk = SS.regresi_skor(c)
        self.assertTrue(np.all(np.isnan(sk[:SS.B_TINGKAP - 1])))
        self.assertTrue(np.isfinite(sk[SS.B_TINGKAP - 1]))

    def test_siri_terlalu_pendek_semua_nan(self):
        self.assertTrue(np.all(np.isnan(SS.regresi_skor(np.full(10, 100.0)))))

    def test_tiada_pandang_hadapan(self):
        """Mengubah bar TERAKHIR tidak boleh menukar skor bar sebelumnya."""
        c = 100 * np.exp(0.001 * np.arange(250))
        a = SS.regresi_skor(c)
        c2 = c.copy()
        c2[-1] = 9999.0
        b = SS.regresi_skor(c2)
        np.testing.assert_allclose(a[:-1], b[:-1], rtol=1e-9)


class TestParameterDikunci(unittest.TestCase):
    """Spec §6: grid TETAP, tiada varian, tiada parameter ditala."""

    def test_sistem_a(self):
        self.assertEqual(SS.A_SLOT, 10)
        self.assertAlmostEqual(SS.A_HENTI, 0.92)       # henti awal -8%
        self.assertAlmostEqual(SS.A_SASAR, 1.10)       # jual 1/3 pada +10%
        self.assertEqual(SS.A_HARI_SEPARA, 5)
        self.assertAlmostEqual(SS.A_PECAHAN_SEPARA, 1 / 3)

    def test_sistem_b(self):
        self.assertEqual(SS.B_SLOT, 20)
        self.assertEqual(SS.B_TINGKAP, 90)
        self.assertAlmostEqual(SS.B_LOMPAT, 0.15)
        self.assertAlmostEqual(SS.B_RISIKO, 0.001)
        self.assertAlmostEqual(SS.B_PERATUS_PEGANG, 0.20)

    def test_tingkap_keputusan(self):
        self.assertEqual((SS.UJI0, SS.UJI1), (2020, 2025))
        self.assertEqual((SS.TH0, SS.TH1), (2012, 2025))


class TestParitiRisiko(unittest.TestCase):
    def test_atr_tinggi_memberi_saiz_kecil(self):
        """Pariti risiko Clenow: saiz = risiko / ATR%. ATR 2x lebih tinggi -> saiz 2x lebih kecil."""
        def saiz(atrp):
            return min(SS.B_RISIKO / (atrp / 100.0), SS.B_SAIZ_MAKS)
        self.assertAlmostEqual(saiz(2.0) / saiz(4.0), 2.0, places=6)

    def test_atr_2pct_memberi_5pct_ekuiti(self):
        self.assertAlmostEqual(SS.B_RISIKO / (2.0 / 100.0), 0.05, places=6)

    def test_had_keselamatan_mengikat_pada_atr_sangat_rendah(self):
        # ATR 0.1% akan memberi 100% ekuiti tanpa had; had mesti mengikat.
        self.assertAlmostEqual(min(SS.B_RISIKO / 0.001, SS.B_SAIZ_MAKS), SS.B_SAIZ_MAKS)

    def test_atr_peneraju_momentum_memberi_pendedahan_rendah(self):
        """Mengapa Sistem B melabur ~35%: ATR peneraju ~5-6% memberi ~1.8% setiap posisi."""
        s = SS.B_RISIKO / (5.5 / 100.0)
        self.assertLess(s, 0.02)
        self.assertLess(s * SS.B_SLOT, 0.40)


if __name__ == '__main__':
    unittest.main()
