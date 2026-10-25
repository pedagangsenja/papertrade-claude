# Ujian jurnal mingguan (standard/jurnal.py; dokumen db jurnal/minggu, dashboard v105 Lagi › Jurnal) dan bina_pratonton.py.
import json, os, sys, tempfile, unittest
from datetime import date

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'standard'))
import jurnal as JR  # noqa: E402
import bina_pratonton as BP  # noqa: E402


def _p(**k):
    d = dict(unit='1', keluar='False', keluar_henti='False', tutup_semua='False', henti='9')
    d.update(k)
    return d


# minggu Isnin 19 Okt – Jumaat 23 Okt 2026; tutup hari isyarat dalam stor
C = [
    _p(saham='AAA', kaedah='M03', tarikh_isyarat='2026-10-19', tarikh_beli='2026-10-20', harga_beli='10.6', untung_pct='-8', keluar='True',
       tarikh_keluar='2026-10-22', harga_keluar='9.2', untung_akhir_pct='-13.2', isyarat_keluar='Keluar: kena henti (buka bawah henti) (22 Okt @ 9.20)'),
    _p(saham='BBB', kaedah='M03', tarikh_isyarat='2026-10-19', tarikh_beli='2026-10-20', harga_beli='20', untung_pct='-5', keluar='True',
       tarikh_keluar='2026-10-21', harga_keluar='19', untung_akhir_pct='-5', isyarat_keluar='Keluar: kena henti (21 Okt @ 19.00)'),
    _p(saham='CCC', kaedah='M07', tarikh_isyarat='2026-10-20', tarikh_beli='2026-10-21', harga_beli='30', untung_pct='4', keluar='True',
       tarikh_keluar='2026-10-23', harga_keluar='31.2', untung_akhir_pct='4', isyarat_keluar='Keluar: capai sasaran (23 Okt @ 31.20)'),
    _p(saham='DDD', kaedah='M07', tarikh_isyarat='2026-10-21', tarikh_beli='2026-10-22', harga_beli='40', untung_pct='2'),
    _p(saham='EEE', kaedah='M12', tarikh_isyarat='2026-10-21', tarikh_beli='2026-10-22', harga_beli='5', untung_pct='-1', tidak_sah='True',
       sebab_tidak_sah='isyarat palsu: saham tidak cair (20 bar) pada 2026-10-22'),
    _p(saham='FFF', kaedah='M12', tarikh_beli='2026-10-23', tidak_dibeli='True', harga_beli=''),
]
LANGKAU = [dict(tarikh='2026-10-21', saham='GGG', kaedah='M03', sebab='buka 11.00 > buka_maks 10.50'),
           dict(tarikh='2026-10-22', saham='HHH', kaedah='M07', sebab='buka 8.00 ≤ henti 8.10'),
           dict(tarikh='2026-10-12', saham='III', kaedah='M07', sebab='buka ≤ henti')]
STOR = [('AAA', 20261019, 10.0), ('BBB', 20261019, 20.0), ('CCC', 20261020, 30.0), ('DDD', 20261021, 40.0)]
KAL = {'DDD': {date(2026, 10, 22): 'Nasdaq'}, 'AAA': {date(2026, 10, 21): 'Nasdaq'}}


class TestJurnal(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.d = tempfile.mkdtemp()
        with open(os.path.join(cls.d, 'harga_A.csv'), 'w') as f:
            f.write('ticker,date,open,high,low,close,volume\n')
            for t, dt, c in STOR:
                f.write(f'{t},{dt},{c},{c},{c},{c},1000\n')
        cls.J = JR.jurnal(C, LANGKAU, cls.d, None, '2026-10-23', minggu=2, KAL=KAL, dibina='ujian')
        cls.w = cls.J['minggu'][0]

    def test_minggu(self):
        self.assertEqual((self.w['mula'], self.w['akhir']), ('2026-10-19', '2026-10-23'))
        self.assertEqual(len(self.J['minggu']), 2)                 # minggu 12–16 Okt: satu langkauan sahaja
        b = self.w['belian']
        self.assertEqual((b['n'], b['saham'], b['tidak_sah']), (4, 4, 1))   # FFF tidak dibeli tidak dikira
        k = self.w['keluar']
        self.assertEqual(k['n'], 3)
        self.assertEqual(set(k['sebab']), {'buka_bawah_henti', 'henti', 'sasaran'})
        self.assertEqual(self.w['langkau'], dict(n=2, sebab={'buka > buka_maks': 1, 'buka ≤ henti': 1}))

    def test_gelinciran_dan_henti(self):
        g = self.w['gelinciran']
        self.assertEqual((g['n'], g['jurang_5']), (4, 1))           # AAA 10.6 lawan tutup isyarat 10.0 = +6%
        bh = self.w['buka_bawah_henti']
        self.assertEqual((bh['keluar'], bh['henti_biasa'], bh['langkau']), (1, 1, 1))
        self.assertEqual(self.w['earnings']['posisi'], 1)           # AAA (21 Okt); DDD melapor pada hari beli (bukan selepas) -> tidak dikira
        self.assertEqual(self.w['tidak_sah']['dibeli'], {'tidak_cair': 1})

    def test_pelajaran_bernombor(self):
        t = ' '.join(p['teks'] for p in self.w['pelajaran'])
        self.assertIn('1 daripada 2 keluar kena henti ialah buka bawah henti', t)
        self.assertIn('1 daripada 4 belian (25.0%) dibuka > +5%', t)
        self.assertIn('2 isyarat dilangkau', t)
        self.assertIn('1 posisi dibeli minggu ini tidak sah (tidak cair 1)', t)

    def test_pelajaran_kosong_tanpa_data(self):
        J = JR.jurnal([], [], None, None, '2026-10-23', KAL={})
        self.assertEqual(J['minggu'], [])


class TestBinaPratonton(unittest.TestCase):
    def test_bina(self):
        with tempfile.TemporaryDirectory() as d:
            html = os.path.join(d, 'h.html')
            with open(html, 'w', encoding='utf-8') as f:
                f.write("<title>Papan</title>\n<div>x</div><script>(async()=>{" + BP.SAMBUNG + "})();</script>\n")
            asas = os.path.join(d, 'asas.json')
            with open(asas, 'w') as f:
                json.dump({'analisis/papan': {'rows': [], 'v': 'asas'}, 'papertrade/claude': {'rows': []}, 'harian/status': {'v': 1}}, f)
            db = os.path.join(d, 'db')
            for p, x in (('harian/status', {'v': 2}), ('analisis/papan', {'rows': [], 'v': 'baru'}),
                         ('papertrade/ringkas_c', {'bahagian': {'id': 'a', 'n': 2, 'nk': 0}, 'rows': []})):
                os.makedirs(os.path.join(db, p.split('/')[0]), exist_ok=True)
                with open(os.path.join(db, p + '.json'), 'w') as f:
                    json.dump(x, f)
            out, D, baru, buang = BP.bina([asas], db, html, 'Pratonton', kekal=['analisis/papan'])
            self.assertTrue(out.startswith('<title>Pratonton</title>\n<script>window.__DB='))
            self.assertIn(BP.TIRUAN, out)
            self.assertNotIn(BP.SAMBUNG, out)
            self.assertNotIn('<title>Papan</title>', out)
            self.assertEqual(D['harian/status'], {'v': 2})              # db menindih asas
            self.assertEqual(D['analisis/papan']['v'], 'asas')          # --kekal-asas
            self.assertEqual(buang, ['papertrade/claude'])              # dokumen lama tidak dibaca halaman
            am = BP.semak(D)
            self.assertTrue(any(a.startswith('papertrade/ringkas_c_2') for a in am))
            self.assertTrue(any(a.startswith('harian/hari_ini') for a in am))


if __name__ == '__main__':
    unittest.main()
