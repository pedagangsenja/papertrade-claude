# Ujian standard/snapshot_sektor_db.py (audit dashboard 24 Okt 2026, item 28): gred kumpulan v2, medan SST hanya jika segar,
# tanpa prestasi_1d, kelas berganda dibuang daripada senarai saham, pendedahan posisi C.
import csv, json, os, sys, tempfile, unittest

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'standard'))
import snapshot_sektor_db as S  # noqa: E402


def tulis_csv(p, lajur, rows):
    with open(p, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=lajur)
        w.writeheader()
        w.writerows(rows)


def tulis_json(p, d):
    with open(p, 'w', encoding='utf-8') as f:
        json.dump(d, f)


class UjiSnapshotSektor(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        d = self.d = self.tmp.name
        teratas = [dict(saham='BF.A', r1m=9.0, r1w=1.0), dict(saham='BF.B', r1m=8.0, r1w=1.0), dict(saham='STZ', r1m=7.0, r1w=1.0)]
        self.pasaran = os.path.join(d, 'pasaran.json')
        tulis_json(self.pasaran, dict(tarikh='2026-10-23', pasaran=dict(n=100, breadth=55.0, r1w=0.5, r1m=1.234, r3m=-2.0), rows=[
            dict(jenis='Sektor', nama='Consumer Defensive', sektor='Consumer Defensive', n=40, prestasi_1w=1, prestasi_1m=2,
                 prestasi_3m=3, breadth=60, rel_1m=1, rel_3m=1, fasa='Leading', skor_panas=70, mcap_bilion=10.0, teratas_senarai=teratas),
            dict(jenis='Industri', nama='Beverages - Wineries & Distilleries', sektor='Consumer Defensive', n=4, prestasi_1w=1,
                 prestasi_1m=2, prestasi_3m=3, breadth=50, rel_1m=1, rel_3m=1, fasa='Leading', skor_panas=60, mcap_bilion=5.0,
                 teratas_senarai=teratas)]))
        sst = dict(rs=55.0, sst=60, volum_relatif=1.2, aliran_institusi=3, aliran_beli=4, aliran_jual=1, volum_luar_biasa=2)
        self.lama = os.path.join(d, 'lama.json')
        tulis_json(self.lama, dict(rows=[dict(jenis='Sektor', nama='Consumer Defensive', **sst),
                                         dict(jenis='Industri', nama='Beverages - Wineries & Distilleries', **sst)],
                                   pasaran=dict(naik=403, turun=342, adr=1.18, rsi=49.3, r1m=1.06, n_saham=1),
                                   institusi_beli=[dict(saham='BF.A', ubah=5), dict(saham='BF.B', ubah=4)], institusi_jual=[],
                                   volum_luar_biasa=[dict(saham='X', rv=3.0, ubah=1.0)], definisi_fasa='fasa'))
        self.peta = os.path.join(d, 'peta.csv')
        tulis_csv(self.peta, ['ticker', 'industri'], [dict(ticker='BF.B', industri='Beverages - Wineries & Distilleries'),
                                                      dict(ticker='STZ', industri='Beverages - Wineries & Distilleries')])
        self.pt = os.path.join(d, 'papertrade'); os.makedirs(self.pt)
        lj = ['saham', 'kaedah', 'keluar', 'tidak_sah', 'tidak_dibeli', 'untung_pct']
        tulis_csv(os.path.join(self.pt, 'claude.csv'), lj, [
            dict(saham='STZ', kaedah='M01', keluar='False', tidak_sah='False', tidak_dibeli='False', untung_pct='2.0'),
            dict(saham='BF.B', kaedah='M02', keluar='False', tidak_sah='False', tidak_dibeli='False', untung_pct='-1.0'),
            dict(saham='STZ', kaedah='M03', keluar='True', tidak_sah='False', tidak_dibeli='False', untung_pct='9.0')])
        tulis_csv(os.path.join(self.pt, 'sektor.csv'), ['tarikh', 'jenis', 'nama'] + S.SST_CSV, [
            dict(tarikh='2026-10-12', jenis='Sektor', nama='Consumer Defensive', rs=50, volum_relatif=1.0, aliran_beli=1,
                 aliran_jual=1, aliran_institusi=0, volum_luar_biasa=1),
            dict(tarikh='2026-10-13', jenis='Sektor', nama='Consumer Defensive', rs=55, volum_relatif=1.2, aliran_beli=4,
                 aliran_jual=1, aliran_institusi=3, volum_luar_biasa=2),
            dict(tarikh='2026-10-14', jenis='Sektor', nama='Consumer Defensive', rs=55, volum_relatif=1.2, aliran_beli=4,
                 aliran_jual=1, aliran_institusi=3, volum_luar_biasa=2)])
        self.kum = os.path.join(d, 'gred_kumpulan.csv')
        lk = ['tarikh', 'jenis', 'nama', 'sektor', 'n', 'skor', 'gred']
        tulis_csv(self.kum, lk, [
            dict(tarikh='2026-10-21', jenis='Sektor', nama='Consumer Defensive', sektor='Consumer Defensive', n=39, skor=10.0, gred='E'),
            dict(tarikh='2026-10-22', jenis='Sektor', nama='Consumer Defensive', sektor='Consumer Defensive', n=41, skor=85.04, gred='A'),
            dict(tarikh='2026-10-22', jenis='Industri', nama='Beverages - Wineries & Distilleries', sektor='Consumer Defensive', n=4,
                 skor=50.0, gred='C')])
        self.kelas = os.path.join(d, 'kelas.csv')
        tulis_csv(self.kelas, ['kumpulan', 'saham'], [dict(kumpulan='Brown-Forman', saham='BF.A'), dict(kumpulan='Brown-Forman', saham='BF.B')])
        self.stor = os.path.join(d, 'stor'); os.makedirs(self.stor)
        tulis_csv(os.path.join(self.stor, 'harga_A.csv'), ['ticker', 'date', 'open', 'high', 'low', 'close', 'volume'],
                  [dict(ticker=t, date=20261001 + i, open=10, high=11, low=9, close=10, volume=v)
                   for t, v in [('BF.A', 1000), ('BF.B', 900000)] for i in range(20)])
        self.out = os.path.join(d, 'baru.json')

    def tearDown(self):
        self.tmp.cleanup()

    def jalan(self, *tambah):
        S.main(['--pasaran', self.pasaran, '--lama', self.lama, '--peta', self.peta, '--papertrade', self.pt, '--dibina', 'x',
                '--out', self.out, '--kumpulan', self.kum, '--kelas', self.kelas, '--stor', self.stor, *tambah])
        return S.baca_json(self.out)

    def test_sst_lapuk_dibuang_dengan_tarikh(self):
        d = self.jalan('--sst-tarikh', '2026-10-19')
        self.assertEqual(d['sst_tarikh'], '2026-10-19')
        self.assertEqual(d['sst_tarikh_kumpulan'], '2026-10-13')     # tarikh terakhir nilai berubah dalam sektor.csv
        self.assertEqual(d['sst_segar'], dict(pasaran=False, kumpulan=False, had_sesi=2))
        for r in d['rows']:
            for k in S.SST_MEDAN + ['prestasi_1d']:
                self.assertNotIn(k, r)
        for k in S.SST_DOC:
            self.assertNotIn(k, d)
        for k in S.SST_PASARAN + S.PASARAN_LAMA:
            self.assertNotIn(k, d['pasaran'])
        self.assertEqual(d['pasaran']['median_1m'], 1.23)
        self.assertEqual(d['pasaran']['n_saham'], 100)

    def test_sst_segar_disertakan(self):
        d = self.jalan('--sst-tarikh', '2026-10-21', '--sst-tarikh-kumpulan', '2026-10-22')
        self.assertEqual(d['sst_segar'], dict(pasaran=True, kumpulan=True, had_sesi=2))
        r = d['rows'][0]
        self.assertEqual((r['rs'], r['volum_relatif'], r['aliran_institusi']), (55.0, 1.2, 3))
        self.assertEqual((d['pasaran']['naik'], d['pasaran']['turun']), (403, 342))
        self.assertNotIn('r1m', d['pasaran'])
        self.assertEqual([x['saham'] for x in d['institusi_beli']], ['BF.B'])
        self.assertEqual(len(d['volum_luar_biasa']), 1)
        # tarikh dibawa daripada snapshot lama pada larian seterusnya
        tulis_json(self.lama, d)
        d2 = self.jalan()
        self.assertEqual((d2['sst_tarikh'], d2['sst_tarikh_kumpulan']), ('2026-10-21', '2026-10-22'))

    def test_gred_v2_dan_posisi(self):
        d = self.jalan()
        s, i = d['rows']
        self.assertEqual((s['gred_v2'], s['skor_v2'], s['n_v2'], s['tarikh_v2']), ('A', 85.0, 41, '2026-10-22'))
        self.assertEqual((i['gred_v2'], i['n_v2']), ('C', 4))
        self.assertEqual((s['posisi_c'], s['untung_c']), (2, 0.5))   # posisi lorong kaedah keluar tidak dikira
        self.assertEqual((i['posisi_c'], i['posisi_m'], i['untung_m']), (2, 0, None))
        self.assertIsNone(d['sst_tarikh'])

    def test_kelas_berganda_paling_cair(self):
        d = self.jalan()
        for r in d['rows']:
            self.assertEqual([x['saham'] for x in r['teratas']], ['BF.B', 'STZ'])

    def test_kelas_tanpa_data_kekal_pertama(self):
        kump = {'BF.A': 'B', 'BF.B': 'B'}
        senarai = [dict(saham='X'), dict(saham='BF.B'), dict(saham='BF.A')]
        self.assertEqual([x['saham'] for x in S.buang_kelas_berganda(senarai, kump, {})], ['X', 'BF.B'])
        self.assertEqual([x['saham'] for x in S.buang_kelas_berganda(senarai, kump, {'BF.A': 5.0})], ['X', 'BF.A'])
        self.assertEqual(S.buang_kelas_berganda([], kump, {}), [])

    def test_sesi_antara(self):
        self.assertEqual(S.sesi_antara('2026-10-19', '2026-10-23'), 4)
        self.assertEqual(S.sesi_antara('2026-10-22', '2026-10-26'), 2)   # merentas hujung minggu
        self.assertTrue(S.segar('2026-10-21', '2026-10-23'))
        self.assertFalse(S.segar('2026-10-20', '2026-10-23'))
        self.assertFalse(S.segar(None, '2026-10-23'))


if __name__ == '__main__':
    unittest.main()
