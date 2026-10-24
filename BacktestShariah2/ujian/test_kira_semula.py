# Ujian kira_semula.py (pengiraan semula bebas CSV + stor + AUTOTUNE lawan db dashboard) dan sambungannya dalam jana_db.py
# (harian/status.semakan, --semakan-sahaja). Fikstur dikongsi dengan ujian halaman: ujian/halaman/fikstur.py + jangka.json.
#   python3 -m unittest BacktestShariah2/ujian/test_kira_semula.py
import copy, io, json, os, sys, tempfile, unittest
from contextlib import redirect_stderr, redirect_stdout

HERE = os.path.dirname(os.path.abspath(__file__))
BS2 = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(BS2, 'standard'))
sys.path.insert(0, os.path.join(HERE, 'halaman'))
import fikstur as F  # noqa: E402
import kira_semula as K  # noqa: E402
import jana_db as J  # noqa: E402



def baca_json(p):
    with open(p, encoding='utf-8') as f:
        return json.load(f)


JANGKA = baca_json(os.path.join(HERE, 'halaman', 'jangka.json'))['kira_semula']
KAL = {t: {d: 'ujian' for d in L} for t, L in F.KALENDAR.items()}


class Asas(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        d = self.tmp.name
        self.pt, self.stor, self.db, self.at = (os.path.join(d, x) for x in ('pt', 'stor', 'db', 'autotune.json'))
        F.tulis_sumber(self.pt); F.tulis_stor(self.stor); F.tulis_db(self.db)
        with open(self.at, 'w') as f:
            json.dump(F.AUTOTUNE, f)

    def tearDown(self):
        self.tmp.cleanup()

    def semak(self, **k):
        return K.semak(self.db, self.pt, self.stor, None, k.get('papan'), self.at, KAL)

    def doc(self, path):
        with open(os.path.join(self.db, path + '.json'), encoding='utf-8') as f:
            return json.load(f)

    def simpan(self, path, d):
        with open(os.path.join(self.db, path + '.json'), 'w', encoding='utf-8') as f:
            json.dump(d, f, ensure_ascii=False)

    def ubah_ringkas_c(self, saham, kaedah, medan, nilai):
        """Tukar satu nilai baris papertrade/ringkas_c (bentuk padat; baris boleh berada dalam bahagian 2)."""
        asas = self.doc('papertrade/ringkas_c'); K_ = asas['kolum']
        ix = {c: i for i, c in enumerate(K_)}
        kamus = {}
        for c, mula, v in self.doc('papertrade/ringkas_c_kamus_1')['kamus']:
            for j, x in enumerate(v):
                kamus.setdefault(c, {})[mula + j] = x
        val = lambda r, c: kamus[c][r[ix[c]] - 1] if asas['jenis'][ix[c]] == 'k' and r[ix[c]] else r[ix[c]]
        for path in ['papertrade/ringkas_c'] + [f'papertrade/ringkas_c_{i}' for i in range(2, asas['bahagian']['n'] + 1)]:
            d = asas if path == 'papertrade/ringkas_c' else self.doc(path)
            for r in d['rows']:
                if val(r, 'saham') == saham and val(r, 'kaedah') == kaedah:
                    r[ix[medan]] = nilai
                    self.simpan(path, d)
                    return
        raise AssertionError('baris tiada')


class UjiFikstur(Asas):
    def test_fikstur_ok_dan_nilai_sama_dengan_jangka(self):
        sm, nilai, S = self.semak()
        self.assertEqual(sm.beza, [])
        self.assertEqual(S, F.S)
        self.assertGreater(sm.n, 150)
        for kump, d in JANGKA.items():
            for k, v in d.items():
                g = nilai[kump][k]
                if isinstance(v, float):
                    self.assertAlmostEqual(v, g, places=3, msg=f'{kump}.{k}')
                else:
                    self.assertEqual(v, g, f'{kump}.{k}')
        self.assertEqual(set(nilai['semak']), {'baris', 'earn_kini', 'agregat', 'watchlist', 'harga', 'penganalisis'})

    def test_fikstur_db_json_segar(self):
        """fikstur_db.json (dibaca uji_halaman.js) mesti sama dengan fikstur.dokumen() — jalankan fikstur.py selepas mengubah data."""
        with open(os.path.join(HERE, 'halaman', 'fikstur_db.json'), encoding='utf-8') as f:
            ada = json.load(f)
        self.assertEqual(json.loads(json.dumps(F.dokumen())), ada)

    def test_penyahkod_bahagian_dan_kamus(self):
        self.assertGreater(self.doc('papertrade/ringkas_c')['bahagian']['n'], 1)
        d, ident = K.nyahkod_ringkas(self.db, 'papertrade', 'ringkas_c')
        self.assertEqual(len(d['rows']), len(F.POSISI))
        self.assertEqual([r['saham'] for r in d['rows']], [r['saham'] for r in F.POSISI])
        aaa = d['rows'][0]
        self.assertEqual((aaa['harga_beli'], aaa['keluar'], aaa['earn_kini']), (100, False, '2026-10-28'))
        w, hilang = K.gabung_bahagian(self.db, 'papertrade/watchlist')
        self.assertEqual((len(w['rows']), hilang), (len(F.WATCH), []))


class UjiBezaDikesan(Asas):
    def test_harga_terkini_db_salah(self):
        self.ubah_ringkas_c('BBB', 'M03', 'harga_terkini', 46.5)
        sm, _, _ = self.semak()
        self.assertEqual([b['medan'] for b in sm.beza], ['C:BBB|M03|2026-10-21.harga_terkini'])
        self.assertEqual((sm.beza[0]['dijangka'], sm.beza[0]['didapati']), (45.0, 46.5))

    def test_untung_db_salah_juga_mengubah_agregat(self):
        self.ubah_ringkas_c('FFF', 'M03', 'untung_pct', 7.0)
        sm, _, _ = self.semak()
        medan = {b['medan'] for b in sm.beza}
        self.assertIn('C:FFF|M03|2026-10-23.untung_pct', medan)
        self.assertIn('pegang.belum_direalisasi', medan)
        self.assertIn('pegang.ikut_saham', medan)

    def test_baris_hilang_dalam_db(self):
        asas = self.doc('papertrade/ringkas_c')
        asas['rows'] = asas['rows'][1:]
        self.simpan('papertrade/ringkas_c', asas)
        sm, _, _ = self.semak()
        medan = [b['medan'] for b in sm.beza]
        self.assertIn('C:bilangan_baris', medan)
        self.assertIn('C:AAA|M03|2026-10-20', medan)

    def test_untung_csv_lawan_stor(self):
        """CSV dan db sepadan (keduanya salah) tetapi untung_pct tidak sepadan dengan tutup stor sesi data."""
        p = os.path.join(self.pt, 'claude.csv')
        rows = [dict(r) for r in F.POSISI]
        rows[0]['untung_pct'] = '12.0'
        F.tulis_csv(p, rows)
        self.ubah_ringkas_c('AAA', 'M03', 'untung_pct', 12.0)
        sm, nilai, _ = self.semak()
        harga = [b for b in sm.beza if b['medan'].startswith('C:AAA|M03') and b['medan'].endswith('untung_pct') and 'tutup stor' in b['nota']]
        self.assertEqual(len(harga), 1)
        self.assertEqual(harga[0]['dijangka'], 10.0)
        self.assertEqual((nilai['harga']['tanpa_bar_sesi'], nilai['harga']['saham_tanpa_bar']), (1, ['III']))  # III: bukan beza

    def test_watchlist_pct_salah(self):
        w = self.doc('papertrade/watchlist')
        for x in ([w] + [self.doc(f'papertrade/watchlist_{i}') for i in range(2, w['bahagian']['n'] + 1)]):
            for r in x['rows']:
                if r['saham'] == 'KKK':
                    r['pct_dipenuhi'] = 100.0
                    self.simpan('papertrade/watchlist' if x is w else f"papertrade/watchlist_{x['bahagian']}", x)
        sm, _, _ = self.semak()
        self.assertEqual([b['medan'] for b in sm.beza], ['W:KKK|M07|431.pct_dipenuhi'])

    def test_earn_kini_salah(self):
        self.ubah_ringkas_c('AAA', 'M07', 'earn_kini', 0)   # kod kamus 0 = tiada
        sm, _, _ = self.semak()
        self.assertEqual([b['medan'] for b in sm.beza], ['C:AAA|M07|2026-10-21.earn_kini'])

    def test_harian_kaedah_salah(self):
        hk = self.doc('prestasi/harian_kaedah')
        hk['rows'][0]['j'] = 3.5
        self.simpan('prestasi/harian_kaedah', hk)
        sm, _, _ = self.semak()
        self.assertEqual([b['medan'] for b in sm.beza], ['harian_kaedah.C.Semua.j'])

    def test_penganalisis(self):
        P = copy.deepcopy(F.PAPAN)
        P['rows'][1]['at_label'] = 'TINGGI'                   # AUTOTUNE M07 = SEDERHANA
        P['rows'][2]['at_cagr_bersih'] = 0.2                  # AUTOTUNE M12 = 0.05
        P['fasa']['jumlah_hadapan'] = 13                     # Σ h_posisi = 12
        P['rows'][0]['p_top5'] = 0.7                          # Σ p_top5 = 2.7 != 3
        P['rows'][0]['lulus'] = 3                             # lulus_subset + lulus_wfo + lulus_at = 3? (M03: semua True)
        P['rows'][1]['lulus'] = 3                             # M07: wfo + at = 2
        P['rows'][2]['ditolak'] = False                       # M12 bt_keputusan DITOLAK (papan lama tanpa medan ditolak)
        P['rows'][4]['swing'] = True                          # M99 pegang 45 hari
        self.simpan('analisis/papan', P)
        sm, nilai, _ = self.semak()
        medan = {b['medan'] for b in sm.beza}
        self.assertEqual(medan, {'M07.at_label', 'M12.at_cagr_bersih', 'fasa.jumlah_hadapan', 'Σ p_top5', 'M07.lulus',
                                 'M12.ditolak', 'M99.swing'})
        self.assertEqual((nilai['pintu']['tidak_ditolak'], nilai['pintu']['autotune']), (3, 2))

    def test_main_kod_keluar_dan_json(self):
        self.ubah_ringkas_c('CCC', 'M12', 'harga_beli', 21)
        out = os.path.join(self.tmp.name, 'semakan', 'kira_semula.json')
        argv = ['--db', self.db, '--json', out, '--folder', self.pt, '--stor', self.stor, '--terkini', '', '--autotune', self.at,
                '--pemangkin', '']
        with redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
            kod = K.main(argv)
        d = baca_json(out)
        self.assertEqual((kod, d['status'], d['tarikh']), (1, 'beza', F.S))
        self.assertEqual(set(d), {'tarikh', 'dibina', 'status', 'n_semak', 'n_beza', 'beza', 'nilai'})
        self.assertTrue(any(b['medan'] == 'C:CCC|M12|2026-10-22.harga_beli' for b in d['beza']))
        self.assertLessEqual(len(d['beza']), K.HAD_BEZA)
        # bahagian db hilang -> gagal (halaman tidak memapar data)
        os.remove(os.path.join(self.db, 'papertrade', 'ringkas_c_2.json'))
        with redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
            kod = K.main(argv)
        d = baca_json(out)
        self.assertEqual((kod, d['status']), (2, 'gagal'))
        self.assertIn('ringkas_c_2', d['beza'][0]['nota'])
        # gagal atas db INI -> jana_db melapor ralat merah, bukan lapuk
        sem, ral = J.semakan_status(os.path.dirname(out), K.tanda_db(lambda p: K.baca_doc(self.db, p)))
        self.assertFalse(sem['kira_semula']['lapuk'])
        self.assertTrue(ral[0].startswith('semakan: kira_semula gagal'))

    def test_contoh_beza_bergilir_kategori(self):
        sm = K.Semak()
        for i in range(40):
            sm.banding('baris', f'b{i}', 1, 2)
        sm.banding('harga', 'h0', 1, 2)
        c = sm.contoh(30)
        self.assertEqual((len(c), c[0]['medan'], c[1]['medan'], c[2]['medan']), (30, 'b0', 'h0', 'b1'))


class UjiJanaDbSemakan(Asas):
    def tulis(self, folder, nama, d):
        os.makedirs(folder, exist_ok=True)
        with open(os.path.join(folder, nama), 'w', encoding='utf-8') as f:
            json.dump(d, f, ensure_ascii=False)

    def test_tiada_fail(self):
        with tempfile.TemporaryDirectory() as d:
            sem, ral = J.semakan_status(d, {'ringkas_c': 'x'})
        self.assertEqual(sem, {'kira_semula': {'status': 'tiada'}, 'sumber': {'status': 'tiada'}, 'sampel': {'status': 'tiada'}})
        self.assertEqual(ral, [])

    def test_beza_ralat_dan_lapuk(self):
        sem_dir = os.path.join(self.tmp.name, 'semakan')
        tanda = K.tanda_db(lambda p: K.baca_doc(self.db, p))
        beza = [dict(medan=f'm{i}', dijangka=i, didapati=i + 1, nota='x' * 500) for i in range(25)]
        self.tulis(sem_dir, 'kira_semula.json', dict(tarikh=F.S, dibina='d', status='beza', n_semak=100, n_beza=25, beza=beza,
                                                      nilai=dict(db_tanda=tanda, semak={'baris': [90, 25]})))
        self.tulis(sem_dir, 'sahkan.json', dict(tarikh=F.S, dibina='d', status='ralat', n_ralat=2, n_amaran=1, ringkas=['claude.csv: AAA x', 'b']))
        self.tulis(sem_dir, 'sampel.json', dict(tarikh=F.S, dibina='d', status='beza', n=20, n_beza=1, beza=[
            dict(saham='AAA', kaedah='M03', tarikh_beli='2026-10-20', medan='harga_beli', csv=100, moomoo=100.5)]))
        sem, ral = J.semakan_status(sem_dir, tanda)
        self.assertEqual((sem['kira_semula']['status'], sem['kira_semula']['lapuk'], len(sem['kira_semula']['beza'])), ('beza', False, 10))
        self.assertLessEqual(len(sem['kira_semula']['beza'][0]['nota']), 160)
        self.assertEqual(len(ral), 3)
        self.assertTrue(all(x.startswith('semakan: ') for x in ral))
        self.assertIn('25 beza', ral[0]); self.assertIn('2 ralat', ral[1]); self.assertIn('1/20 beza', ral[2])
        self.assertIn('AAA M03 2026-10-20 harga_beli: csv 100, moomoo 100.5', ral[2])
        self.assertLess(J.bait(sem), 8000)
        # db lain (cap jari berbeza) -> lapuk: amaran kuning sahaja bagi kira_semula
        sem, ral = J.semakan_status(sem_dir, dict(tanda, ringkas_c='lain'))
        self.assertTrue(sem['kira_semula']['lapuk'])
        self.assertTrue(ral[0].startswith('amaran: semakan: kira_semula'))
        self.assertTrue(ral[1].startswith('semakan: sahkan.py'))

    def test_semakan_sahaja_hujung_ke_hujung(self):
        """jana_db (folder db fikstur) -> kira_semula --db -> jana_db --semakan-sahaja: status ok, tidak lapuk, ralat lain kekal."""
        sem_dir = os.path.join(self.tmp.name, 'semakan')
        st = self.doc('harian/status')
        st['ralat'] = ['amaran: papertrade/moomoo 91% had db', 'semakan: kira_semula beza: lama', 'amaran: semakan: lama']
        self.simpan('harian/status', st)
        with redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
            kod = K.main(['--db', self.db, '--json', os.path.join(sem_dir, 'kira_semula.json'), '--folder', self.pt, '--stor', self.stor,
                          '--terkini', '', '--autotune', self.at, '--pemangkin', ''])
            J.main(['--keluar', self.db, '--semakan-sahaja', '--semakan-dir', sem_dir])
        st = self.doc('harian/status')
        self.assertEqual(kod, 0)
        self.assertEqual(st['ralat'], ['amaran: papertrade/moomoo 91% had db'])
        self.assertEqual((st['semakan']['kira_semula']['status'], st['semakan']['kira_semula']['lapuk']), ('ok', False))
        self.assertEqual(st['semakan']['sumber'], {'status': 'tiada'})
        # db dijana semula dengan baris berbeza tanpa kira_semula -> lapuk (amaran)
        self.ubah_ringkas_c('AAA', 'M03', 'harga_terkini', 111)
        asas = self.doc('papertrade/ringkas_c'); asas['bahagian']['id'] = 'baharu'; self.simpan('papertrade/ringkas_c', asas)
        with redirect_stdout(io.StringIO()):
            J.main(['--keluar', self.db, '--semakan-sahaja', '--semakan-dir', sem_dir])
        st = self.doc('harian/status')
        self.assertTrue(st['semakan']['kira_semula']['lapuk'])
        self.assertEqual(len([x for x in st['ralat'] if x.startswith('amaran: semakan: ')]), 1)


if __name__ == '__main__':
    unittest.main()
