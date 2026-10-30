"""Ujian registry Nxx — keluarga kedua selari dengan Mxx."""
import csv
import os
import sys
import tempfile
import unittest

AKAR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(AKAR, 'BacktestShariah2', 'standard'))

import registry_n as R  # noqa: E402


class TestStruktur(unittest.TestCase):
    def test_semak_bersih(self):
        self.assertEqual(R.semak(), [])

    def test_bilangan(self):
        # jumlah dipradaftar; menambah baris mesti kemas kini ujian ini dengan sengaja
        self.assertEqual(len(R.MASUK), 130)
        self.assertEqual(len(R.KELUAR), 41)
        self.assertEqual(len(R.CARA), 10)
        self.assertEqual(len(R.URUTAN), 11)

    def test_id_berturutan(self):
        self.assertEqual([b[0] for b in R.MASUK], [f'N{i:02d}' for i in range(1, 131)])
        self.assertEqual([b[0] for b in R.KELUAR], [f'X{i:02d}' for i in range(1, 42)])
        self.assertEqual([b[0] for b in R.CARA], [f'C{i:02d}' for i in range(1, 11)])
        self.assertEqual([b[0] for b in R.URUTAN], [f'U{i:02d}' for i in range(1, 12)])

    def test_medan_penuh(self):
        for b in R.MASUK:
            self.assertEqual(len(b), 8, b[0])
            for medan in b[:7]:        # nota dibenarkan kosong
                self.assertTrue(str(medan).strip(), b[0])
        for b in list(R.KELUAR) + list(R.CARA) + list(R.URUTAN):
            self.assertEqual(len(b), 6, b[0])
            for medan in b[:5]:
                self.assertTrue(str(medan).strip(), b[0])

    def test_lajur_sepadan(self):
        self.assertEqual(len(R.LAJUR), 8)

    def test_nama_unik(self):
        nama = [b[2] for b in R.MASUK]
        self.assertEqual(len(set(nama)), len(nama))

    def test_peraturan_masuk_unik(self):
        aturan = [b[3] for b in R.MASUK]
        self.assertEqual(len(set(aturan)), len(aturan))

    def test_peraturan_keluar_unik(self):
        aturan = [b[1] for b in R.KELUAR]
        self.assertEqual(len(set(aturan)), len(aturan))


class TestStatus(unittest.TestCase):
    def test_status_sah(self):
        for st in ([b[6] for b in R.MASUK] + [b[4] for b in R.KELUAR] +
                   [b[4] for b in R.CARA] + [b[4] for b in R.URUTAN]):
            self.assertTrue(st in ('DIUJI', 'SEDIA') or st.startswith('PERLU:'), st)

    def test_diuji_ada_nota(self):
        # DIUJI tanpa angka tidak berguna
        for b in R.MASUK:
            if b[6] == 'DIUJI':
                self.assertTrue(b[7].strip(), b[0])
        for b in list(R.KELUAR) + list(R.CARA) + list(R.URUTAN):
            if b[4] == 'DIUJI':
                self.assertTrue(b[5].strip(), b[0])

    def test_perlu_ada_nama_indikator(self):
        for b in R.MASUK:
            if b[6].startswith('PERLU:'):
                self.assertTrue(b[6].split(':', 1)[1].strip(), b[0])

    def test_n01_adalah_dapatan_pengguna(self):
        n01 = R.MASUK[0]
        self.assertEqual(n01[0], 'N01')
        self.assertIn('ma10', n01[3])
        self.assertIn('ma20', n01[3])
        self.assertIn('vol_n50', n01[3])
        self.assertEqual(n01[6], 'DIUJI')

    def test_c01_adalah_asas_repo(self):
        c01 = R.CARA[0]
        self.assertEqual(c01[0], 'C01')
        self.assertEqual(c01[4], 'DIUJI')
        self.assertIn('buka', c01[1])
        self.assertIn('KOLAM_EKOR', c01[5])

    def test_cara_lain_belum_diuji(self):
        # hanya C01 pernah diuji; jika ini gagal, seseorang menanda DIUJI tanpa hasil
        self.assertEqual([b[0] for b in R.CARA if b[4] == 'DIUJI'], ['C01'])

    def test_u05_papan_ditanda_jangan_guna(self):
        # KAEDAH_TERBAIK.md: pangkat backtest tiada kuasa ramalan; nota mesti menyatakannya
        u05 = [b for b in R.URUTAN if b[0] == 'U05'][0]
        self.assertIn('JANGAN', u05[5])

    def test_u03_clenow_sebaran_sifar(self):
        u03 = [b for b in R.URUTAN if b[0] == 'U03'][0]
        self.assertEqual(u03[4], 'DIUJI')
        self.assertIn('0.00', u03[5])

    def test_pandas_ta_bukan_kebergantungan(self):
        # pandas_ta memaksa numpy<2.3; ia rujukan spesifikasi sahaja
        import os
        req = os.path.join(R.AKAR, 'requirements-kajian.txt')
        teks = open(req, encoding='utf-8').read()
        self.assertNotIn('pandas-ta==', teks)
        self.assertNotIn('pandas_ta==', teks)

    def test_rejim_kalendar_ada_amaran_pendedahan(self):
        # N101-N110 memilih MASA bukan saham = peruntukan tunai; spec mesti menyatakannya
        kel = {b[1] for b in R.MASUK if b[0] in
               ('N101', 'N105', 'N107', 'N108', 'N110')}
        self.assertEqual(kel, {'KALENDAR', 'REJIM'})

    def test_n122_pembetulan_ambang_direkod(self):
        # saya tersilap ingat $20 juta; sumber beri $10 juta. Pembetulan mesti kekal direkod.
        n122 = [b for b in R.MASUK if b[0] == 'N122'][0]
        self.assertIn('10 juta', n122[3])
        self.assertIn('PEMBETULAN', n122[7])

    def test_n130_orb_amaran_kos(self):
        n130 = [b for b in R.MASUK if b[0] == 'N130'][0]
        self.assertEqual(n130[6], 'PERLU:intraday')
        self.assertIn('SIFAR', n130[7])

    def test_kira(self):
        km = R._kira(R.MASUK, 6)
        self.assertEqual(sum(km.values()), len(R.MASUK))
        self.assertGreater(km['SEDIA'], 0)


class TestSemakTangkapRalat(unittest.TestCase):
    def _dengan(self, masuk):
        asal = R.MASUK
        try:
            R.MASUK = masuk
            return R.semak()
        finally:
            R.MASUK = asal

    def test_tangkap_id_terlangkau(self):
        m = [('N01', 'MA', 'a', 'x', 's', 'p', 'SEDIA', ''),
             ('N03', 'MA', 'b', 'y', 's', 'p', 'SEDIA', '')]
        self.assertTrue(any('tidak berturutan' in x for x in self._dengan(m)))

    def test_tangkap_status_tidak_dikenali(self):
        m = [('N01', 'MA', 'a', 'x', 's', 'p', 'MUNGKIN', '')]
        self.assertTrue(any('tidak dikenali' in x for x in self._dengan(m)))

    def test_tangkap_cara_tidak_berturutan(self):
        asal = R.CARA
        try:
            R.CARA = [('C02', 'a', 's', 'p', 'SEDIA', '')]
            self.assertTrue(any('tidak berturutan' in x for x in R.semak()))
        finally:
            R.CARA = asal

    def test_tangkap_urutan_tidak_berturutan(self):
        asal = R.URUTAN
        try:
            R.URUTAN = [('U02', 'a', 's', 'p', 'SEDIA', '')]
            self.assertTrue(any('tidak berturutan' in x for x in R.semak()))
        finally:
            R.URUTAN = asal

    def test_tangkap_medan_kurang(self):
        m = [('N01', 'MA', 'a', 'x', 's', 'p', 'SEDIA')]
        self.assertTrue(any('medan' in x for x in self._dengan(m)))


class TestKeluaran(unittest.TestCase):
    def test_csv_dan_spec_ditulis(self):
        asal_csv, asal_spec = R.CSV, R.SPEC
        with tempfile.TemporaryDirectory() as d:
            try:
                R.CSV = os.path.join(d, 'registry_N.csv')
                R.SPEC = os.path.join(d, 'SPEC_SEMUA_N.md')
                n = R.tulis_csv()
                R.tulis_spec()
                self.assertEqual(n, len(R.MASUK) + len(R.KELUAR) + len(R.CARA) +
                                 len(R.URUTAN))
                with open(R.CSV, encoding='utf-8') as f:
                    baris = list(csv.DictReader(f))
                self.assertEqual(len(baris), n)
                self.assertEqual(baris[0]['id'], 'N01')
                self.assertEqual(baris[len(R.MASUK)]['keluarga'], 'KELUAR')
                self.assertEqual(baris[-1]['keluarga'], 'URUTAN')
                teks = open(R.SPEC, encoding='utf-8').read()
                self.assertIn('SPEC SEMUA N', teks)
                self.assertIn('N130', teks)
                self.assertIn('X41', teks)
                self.assertIn('C10', teks)
                self.assertIn('U11', teks)
                self.assertIn('peruntukan tunai yang disamarkan', teks)
                self.assertIn('Sempadan K / M / N', teks)
                self.assertIn('Saluran rangkaian', teks)
                self.assertIn('Jangan sunting fail ini secara manual', teks)
            finally:
                R.CSV, R.SPEC = asal_csv, asal_spec

    def test_fail_repo_segerak(self):
        """Fail yang dikomit mesti sepadan dengan senarai dalam skrip."""
        with open(R.CSV, encoding='utf-8') as f:
            baris = list(csv.DictReader(f))
        self.assertEqual(len(baris),
                         len(R.MASUK) + len(R.KELUAR) + len(R.CARA) + len(R.URUTAN))
        self.assertEqual([b['id'] for b in baris[:len(R.MASUK)]], [b[0] for b in R.MASUK])

    def test_main_pulang_sifar(self):
        asal_csv, asal_spec = R.CSV, R.SPEC
        with tempfile.TemporaryDirectory() as d:
            try:
                R.CSV = os.path.join(d, 'a.csv')
                R.SPEC = os.path.join(d, 'b.md')
                self.assertEqual(R.main(), 0)
            finally:
                R.CSV, R.SPEC = asal_csv, asal_spec


if __name__ == '__main__':
    unittest.main()
