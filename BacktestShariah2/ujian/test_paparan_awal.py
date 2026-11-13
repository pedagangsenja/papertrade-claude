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


class Respon:
    def __init__(self, d):
        self.d = d

    def json(self):
        return self.d


class Sesi:
    """Pengganti requests.Session: carta Yahoo v8 tiruan (ARW 12 Nov 2026, nilai sebenar)."""
    def __init__(self, masa_tutup='2026-11-12 16:00:02'):
        self.masa = int(pd.Timestamp(masa_tutup, tz='America/New_York').timestamp())

    def get(self, url, **kw):
        t = [int(pd.Timestamp(x, tz='America/New_York').timestamp()) for x in
             ('2026-11-11 15:55', '2026-11-12 09:30', '2026-11-12 09:35', '2026-11-12 15:55')]
        return Respon({'chart': {'result': [{
            'meta': {'regularMarketPrice': 198.2, 'regularMarketTime': self.masa, 'regularMarketDayHigh': 202.565,
                     'regularMarketDayLow': 195.467, 'regularMarketVolume': 398284},
            'timestamp': t,
            'indicators': {'quote': [{'open': [199.0, 195.31, 196.0, 198.0], 'high': [199.5, 196.2, 202.0, 198.3],
                                      'low': [198.0, 194.9, 195.9, 197.8], 'volume': [1000, 5000, 4000, 9000]}]}}]}})


class TestIsiBar(unittest.TestCase):
    def test_bar_carta(self):
        b = P.bar_carta('ARW', '2026-11-12', Sesi())
        self.assertEqual((b['open'], b['high'], b['low'], b['close'], b['volume']), (195.31, 202.565, 194.9, 198.2, 398284))
        self.assertEqual(b['date'], 20261112)

    def test_bukan_sesi_itu_atau_belum_tutup(self):
        self.assertIsNone(P.bar_carta('ARW', '2026-11-11', Sesi()))                       # meta = sesi lain
        self.assertIsNone(P.bar_carta('ARW', '2026-11-12', Sesi('2026-11-12 15:10:00')))  # harga semasa pasaran

    def test_isi_bar_hanya_yang_tiada(self):
        import unittest.mock as um
        d = tempfile.mkdtemp()
        pd.DataFrame([dict(ticker='AAA', date=20261112, open=1, high=1, low=1, close=1, volume=1)]).to_csv(
            os.path.join(d, 'terkini.csv'), index=False)
        json.dump({'terkini': {'tiada_bar_sesi': ['ARW'], 'tiada_data': []}}, open(os.path.join(d, 'status.json'), 'w'))
        with um.patch('requests.Session', Sesi), um.patch('time.sleep'):
            r = P.isi_bar(d, '2026-11-12')
        self.assertEqual(r, {'dicuba': 1, 'diisi': 1})
        x = pd.read_csv(os.path.join(d, 'terkini.csv'))
        self.assertEqual(sorted(x.ticker), ['AAA', 'ARW'])


if __name__ == '__main__':
    unittest.main()
