# Ujian standard/paparan_awal.py (13 Nov 2026): bila paparan awal dijana atau dilangkau (tanpa rangkaian, tanpa salinan).
import json, os, sys, tempfile, unittest

import pandas as pd

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'standard'))
import paparan_awal as P  # noqa: E402

# Jumaat 13 Nov 2026 06:47 MYT = Khamis 12 Nov 17:47 NY: sesi 12 Nov sudah tutup
MASA = pd.Timestamp('2026-11-12 22:47', tz='UTC')


def folder(sesi_data, sesi_rasmi):
    d = tempfile.mkdtemp()
    os.makedirs(os.path.join(d, 'data', 'harga')); os.makedirs(os.path.join(d, 'papertrade'))
    if sesi_data:
        json.dump({'terkini': {'sesi': int(sesi_data.replace('-', ''))}}, open(os.path.join(d, P.STATUS_HARGA), 'w'))
    json.dump({'malam': {'sesi': sesi_rasmi}}, open(os.path.join(d, P.STATUS_PT), 'w'))
    return d


class TestKeadaan(unittest.TestCase):
    def test_sesi_jangka(self):
        self.assertEqual(P.sesi_jangka(MASA), '2026-11-12')
        self.assertEqual(P.sesi_jangka(pd.Timestamp('2026-11-12 21:10', tz='UTC')), '2026-11-11')   # 16:10 NY: belum tutup + 20 min

    def test_jana_bila_data_baharu(self):
        self.assertEqual(P.keadaan(folder('2026-11-12', '2026-11-11'), MASA), (None, '2026-11-12', '2026-11-11', '2026-11-12'))

    def test_langkau_data_belum_ditarik(self):
        sebab = P.keadaan(folder('2026-11-11', '2026-11-11'), MASA)[0]
        self.assertTrue(sebab.startswith('harga_harian.yml'))   # paparan_awal --tunggu bergantung pada awalan ini

    def test_langkau_rasmi_sudah_proses(self):
        self.assertIn('sudah memproses', P.keadaan(folder('2026-11-12', '2026-11-12'), MASA)[0])

    def test_cuti_nyse(self):
        # Khamis Kesyukuran 26 Nov 2026 (NYSE tutup): sesi jangka kekal 25 Nov; sudah diproses -> langkau
        m = pd.Timestamp('2026-11-26 22:47', tz='UTC')
        self.assertEqual(P.sesi_jangka(m), '2026-11-25')
        self.assertIn('sudah memproses', P.keadaan(folder('2026-11-25', '2026-11-25'), m)[0])


if __name__ == '__main__':
    unittest.main()
