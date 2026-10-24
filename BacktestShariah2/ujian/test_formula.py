# Ujian versi dan cap jari formula Papan Penganalisis (audit ketepatan data 24 Okt 2026, lapisan 4).
import os, sys, tempfile, unittest

UJI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(UJI), 'standard'))
import penganalisis as PA  # noqa: E402


class TestFormula(unittest.TestCase):
    def test_cap_stabil_dan_peka(self):
        p = dict(n0_maks=30, swing=[3, 30])
        a, b = PA.cap_formula(p), PA.cap_formula(dict(p))
        self.assertEqual(a, b)
        self.assertEqual(len(a), 10)
        self.assertNotEqual(a, PA.cap_formula(dict(p, n0_maks=31)))

    def test_cap_ikut_kalibrasi(self):
        with tempfile.TemporaryDirectory() as d:
            k = os.path.join(d, 'k.json')
            open(k, 'w').write('{"a": 1}')
            x = PA.cap_formula({}, k)
            open(k, 'w').write('{"a": 2}')
            self.assertNotEqual(x, PA.cap_formula({}, k))

    def test_log_terakhir(self):
        with tempfile.TemporaryDirectory() as d:
            f = os.path.join(d, 'LOG.md')
            open(f, 'w').write('# Log\n\n- v1.0 (2026-10-20): asal\n- v1.1 (2026-10-21): ubah\n')
            self.assertEqual(PA.log_formula(f), 'v1.1 (2026-10-21): ubah')
            self.assertEqual(PA.log_formula(os.path.join(d, 'tiada.md')), '')

    def test_log_ada_versi_semasa(self):
        self.assertTrue(PA.log_formula().startswith('v' + PA.VERSI_FORMULA), 'VERSI_FORMULA mesti ada baris dalam LOG_FORMULA.md')


if __name__ == '__main__':
    unittest.main()
