# Ujian harian/hari_ini (dashboard v105; jana_db.hari_ini), tolakan dokumen berubah sahaja (--lama) dan prestasi/ringkasan
# selepas label §7 dibersarakan. Fikstur dikongsi dengan ujian halaman (ujian/halaman/fikstur.py): uji_halaman.js memapar Hari
# Ini dengan dan tanpa dokumen ini dan menjangka angka yang sama.
import json, os, sys, tempfile, unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'standard'))
sys.path.insert(0, os.path.join(HERE, 'halaman'))
import jana_db as J  # noqa: E402
import fikstur as F  # noqa: E402


class TestHariIniFikstur(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.H = F.hari_ini_doc()

    def test_esok_tahap(self):
        E = self.H['esok']
        self.assertEqual(E['buka'], '2026-10-26')
        self.assertEqual(E['sebelum'], '2026-10-22')
        j = E['wajib']['jual']
        self.assertEqual((j['n'], j['saham']), (2, 2))
        sb = {c['s']: c for c in j['cip']}
        self.assertEqual(sb['BBB']['l'], 'K')
        self.assertEqual(sb['BBB']['sb'], ['isyarat kaedah (tutup)'])
        self.assertEqual(sb['CCC']['l'], '2')
        self.assertEqual(sb['CCC']['sb'], ['lorong 2: tutup 21 < paras 21.5'])
        self.assertEqual([c['s'] for c in j['cip']], ['BBB', 'CCC'])          # rugi terbesar dahulu
        ts = E['semak']['tidak_sah_baru']
        self.assertEqual((ts['n'], ts['cip'][0]['s'], ts['cip'][0]['jenis']), (1, 'GGG', 'tidak_cair'))
        self.assertEqual(E['semak']['earn_buka']['n'], 0)
        m = E['maklumat']
        self.assertEqual((m['earn']['n'], m['earn']['saham'], m['earn']['cip'][0]['eh']), (2, 1, 3))
        self.assertEqual((m['calon']['n'], m['calon']['cip'][0]['s'], m['calon']['kaedah_watchlist']), (1, 'JJJ', 3))
        self.assertEqual(E['tanpa_earnings'], 4)

    def test_buku_berubah_aktiviti(self):
        B = self.H['buku']
        self.assertEqual((B['posisi'], B['saham'], B['lorong_kaedah'], B['lorong2_sahaja']), (7, 6, 6, 1))
        self.assertEqual((B['pnl']['c'], B['pnl']['spy'], B['pnl']['ew']), (-0.2, -0.1, None))
        self.assertIsNone(B['breadth']['pct'])          # tiada harian/trend dalam fikstur -> "tiada data", bukan 0
        self.assertIsNone(B['liputan'])
        R = self.H['berubah']
        self.assertEqual((R['beli']['n'], R['beli']['tarikh']), (1, '2026-10-23'))
        self.assertEqual((R['keluar']['n'], R['keluar']['sebab']), (1, {'masa': 1}))
        self.assertEqual((R['langkau']['n'], R['keluar_l2']['n']), (1, 1))
        self.assertIsNone(R['watchlist']['n'])          # tiada tarikh_imbasan -> tidak diketahui
        self.assertEqual(self.H['aktiviti']['langkau'], {'tarikh': '2026-10-23', 'n': 1})
        self.assertEqual((self.H['matang']['n'], self.H['matang']['G']), (0, 0))

    def test_fikstur_hari_ini_json_segar(self):
        """fikstur_hari_ini.json (dibaca uji_halaman.js) = fikstur.hari_ini_doc() — jalankan fikstur.py selepas mengubah data."""
        with open(os.path.join(HERE, 'halaman', 'fikstur_hari_ini.json'), encoding='utf-8') as f:
            self.assertEqual(json.load(f), json.loads(json.dumps(self.H)))

    def test_saiz_bawah_had(self):
        self.assertLess(J.bait(self.H), J.HAD_DB)


class TestTakrif(unittest.TestCase):
    def test_jarak_dan_status(self):
        t = dict(atr_pct=2.0, c=100.0)                     # 1 ATR = 2.0
        x = J.norm_pt(dict(saham='X', harga_terkini=101, henti=100, isyarat_keluar='Pegang (henti 100)',
                           status_henti='Pegang (paras keluar 95; puncak 104; 3 hari)'))
        o = J.jarak_lorong(x, t)
        self.assertAlmostEqual(o['kaedah'], 0.5)
        self.assertAlmostEqual(o['henti'], 3.0)
        self.assertEqual(J.status_pos(x, o), 'h')
        y = J.norm_pt(dict(saham='X', harga_terkini=99, henti=100, isyarat_keluar='Isyarat keluar 23 Okt — jual pada buka esok (menunggu)'))
        self.assertEqual(J.status_pos(y, J.jarak_lorong(y, t)), ('m', True, False))
        z = J.norm_pt(dict(saham='X', keluar='True', tarikh_keluar='2026-10-20', harga_keluar=50, harga_terkini=60,
                           status_henti='Pegang (paras keluar 98; puncak 110; 3 hari)'))
        self.assertAlmostEqual(J.jarak_lorong(z, t)['henti'], 1.0)   # lorong 2 sahaja: tutup terakhir trend (100), bukan harga keluar
        self.assertIsNone(J.jarak_lorong(z, None))

    def test_jenis_keluar(self):
        self.assertEqual(J.jenis_keluar('Keluar: kena henti (buka bawah henti) (14 Okt @ 9.10)'), 'buka_bawah_henti')
        self.assertEqual(J.jenis_keluar('Keluar: kena henti (23 Okt @ 88.09)'), 'henti')
        self.assertEqual(J.jenis_keluar('Keluar: isyarat keluar kaedah 22 Okt (23 Okt @ 4.00)'), 'isyarat')
        self.assertEqual(J.jenis_keluar('Keluar: capai sasaran (buka atas sasaran)'), 'sasaran')
        self.assertEqual(J.jenis_keluar('Keluar: isyarat palsu, saham diambil alih (CRH)'), 'ambil_alih')
        self.assertEqual(J.jenis_keluar('Keluar: had masa (2026-10-23 @ 38)'), 'masa')

    def test_selang_k(self):
        c = J.selang_k([(1.0, 'a'), (3.0, 'a'), (2.0, 'b')])
        self.assertEqual((c['n'], c['G']), (3, 2))
        self.assertAlmostEqual(c['m'], 2.0)
        self.assertIsNone(J.selang_k([(1.0, 'a')])['lo'])

    def test_siri_ew(self):
        with tempfile.TemporaryDirectory() as d:
            p = os.path.join(d, 'ew.csv')
            with open(p, 'w') as f:
                f.write('tarikh,n,ew_cc,ew_oc,ew_indeks,spy_cc,spy_oc,spy_indeks\n2025-09-30,10,0.01,0,1,0,0,1\n2026-10-23,912,-0.001,0.002,1.4,0.003,0.001,1.3\n')
            e = J.siri_ew(p, '2025-10-01')
            self.assertEqual(e['rows'], [['2026-10-23', 912, -0.001, 0.002, 1.4, 0.003, 0.001, 1.3]])
            self.assertIsNone(J.siri_ew(os.path.join(d, 'tiada.csv')))


class TestTolakBerubah(unittest.TestCase):
    def test_tidak_berubah(self):
        sedia = [('papertrade', 'watchlist', dict(dibina='B', bahagian=dict(id='baru', n=2), rows=[1]), 0),
                 ('papertrade', 'watchlist_2', dict(induk='baru', bahagian=2, rows=[2]), 0),
                 ('prestasi', 'mae', dict(dibina='B', rows=[[1, 2]]), 0),
                 ('harian', 'status', dict(dibina='B'), 0)]
        with tempfile.TemporaryDirectory() as d:
            for kol, doc, dd in (('papertrade', 'watchlist', dict(dibina='A', bahagian=dict(id='lama', n=2), rows=[1])),
                                 ('papertrade', 'watchlist_2', dict(induk='lama', bahagian=2, rows=[2])),
                                 ('prestasi', 'mae', dict(dibina='A', rows=[[1, 3]])), ('harian', 'status', dict(dibina='B'))):
                os.makedirs(os.path.join(d, kol), exist_ok=True)
                with open(os.path.join(d, kol, doc + '.json'), 'w') as f:
                    json.dump(dd, f)
            sama = J.tidak_berubah(sedia, d)
        self.assertEqual(sama, {'papertrade/watchlist', 'papertrade/watchlist_2'})   # mae berubah; status sentiasa ditolak


class TestPrestasiDibersarakan(unittest.TestCase):
    def test_label_s7_dibersarakan_dan_combine_c(self):
        C = [dict(saham='A', kaedah='M03', tarikh_beli='2026-10-20', harga_beli='10', untung_pct='5', keluar='False', hari='2')]
        M = [dict(saham='B', kaedah='M07', tarikh_beli='2026-10-08', harga_beli='10', untung_pct='-5', keluar='False', hari='9')]
        r = J.prestasi(M, C, {}, {'M03': ('BELUM CUKUP', 'BELUM CUKUP')})
        self.assertEqual(r['Combine']['kpi'], r['C']['kpi'])
        self.assertIsNone(r['C']['teruskan'])
        k = r['C']['kaedah'][0]
        self.assertEqual((k['keputusan'], k['pantau_penganalisis']), ('dibersarakan', 'BELUM CUKUP'))


if __name__ == '__main__':
    unittest.main()
