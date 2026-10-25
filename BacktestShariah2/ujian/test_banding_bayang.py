# Ujian standard/banding_bayang.py `belum` (audit 25 Okt 2026): semua tarikh MYT yang belum dibanding dipilih (termasuk
# Sabtu, iaitu kemas kini sesi Jumaat), Ahad dilangkau, dan rutin yang tidak dijadualkan menjadi nota, bukan ralat.
import os, sys, tempfile, unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'standard'))
import banding_bayang as BB


class TestBandingBelum(unittest.TestCase):
    def test_tarikh_belum_termasuk_sabtu(self):
        wujud = {'2026-10-16', '2026-10-17', '2026-10-19', '2026-10-20', '2026-10-21', '2026-10-22', '2026-10-23'}
        # 18 Okt = Ahad (dilangkau); 24 Okt = Sabtu (kemas kini 6:02 sesi Jumaat 23 Okt) mesti dipilih
        self.assertEqual(BB.tarikh_belum('2026-10-16', '2026-10-24', wujud), ['2026-10-24'])
        self.assertEqual(BB.tarikh_belum('2026-10-23', '2026-10-27', {'2026-10-23'}), ['2026-10-24', '2026-10-26', '2026-10-27'])
        self.assertEqual(BB.tarikh_belum('2026-10-25', '2026-10-25', set()), [])

    def test_tarikh_laporan(self):
        d = tempfile.mkdtemp()
        for f in ('BANDING_2026-10-22.md', 'BANDING_2026-10-22.json', 'BANDING_2026-10-23.md', 'LOG.md'):
            open(os.path.join(d, f), 'w').close()
        self.assertEqual(BB.tarikh_laporan(d), {'2026-10-22', '2026-10-23'})
        self.assertEqual(BB.tarikh_laporan(os.path.join(d, 'tiada')), set())

    def test_dijadual(self):
        # Sabtu 24 Okt: kemas kini sahaja (sesi Jumaat); Isnin 26 Okt: imbas + beli (tiada kemas kini 6:02 Isnin)
        self.assertEqual(BB.dijadual('2026-10-24'), {'kemas': True, 'imbas': False, 'beli': False})
        self.assertEqual(BB.dijadual('2026-10-26'), {'kemas': False, 'imbas': True, 'beli': True})
        self.assertEqual(BB.dijadual('2026-10-27'), {'kemas': True, 'imbas': True, 'beli': True})
        # Khamis 26 Nov 2026 cuti Kesyukuran: tiada imbas/beli; Jumaat 27 Nov: tiada kemas kini (sesi 26 Nov cuti)
        self.assertEqual(BB.dijadual('2026-11-26'), {'kemas': True, 'imbas': False, 'beli': False})
        self.assertFalse(BB.dijadual('2026-11-27')['kemas'])

    def test_ada_rutin(self):
        self.assertFalse(BB.ada_rutin({'imbas': []}))
        self.assertTrue(BB.ada_rutin({'imbas': [], 'kemas': 'abc'}))
        self.assertTrue(BB.ada_rutin({'imbas': ['abc']}))


if __name__ == '__main__':
    unittest.main()
