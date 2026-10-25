# Ujian standard/notifikasi.py: baris < 200 aksara, "tak beli" dinyatakan, sesi belum siap dikesan.
import contextlib, io, json, os, sys, tempfile, unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'standard'))
import notifikasi as N


def jalan(st, *arg):
    d = tempfile.mkdtemp()
    with open(os.path.join(d, 'status_harian.json'), 'w') as f:
        json.dump(st, f)
    out = io.StringIO()
    with contextlib.redirect_stdout(out):
        N.main(list(arg) + ['--folder', d])
    return out.getvalue().strip()


MALAM = dict(sesi='2026-10-26', keluar_baru_jumlah=dict(C=120, M=1), keluar_baru=dict(C=dict(henti=80, sasaran=10, isyarat=30)),
             menunggu=40, tidak_dibeli=['AAA M01'], senarai_beli=650, saham_unik=300)


class TestNotifikasi(unittest.TestCase):
    def test_malam_siap(self):
        s = jalan({'malam': MALAM}, 'malam', '--masa', '2026-10-27 07:17')   # Selasa 3:17 ptg MYT
        self.assertIn('Harian 2026-10-26: keluar C 120 (henti 80, isyarat 30, sasaran 10), M 1', s)
        self.assertIn('senarai beli 650 (300 saham) untuk 2026-10-27', s)
        self.assertLess(len(s), 200)

    def test_malam_belum(self):
        s = jalan({'malam': dict(MALAM, sesi='2026-10-23')}, 'malam', '--masa', '2026-10-27 07:17', '--gagal', 'harian.yml')
        self.assertTrue(s.startswith('Harian 2026-10-26 BELUM siap (sesi terakhir diproses: 2026-10-23)'))
        self.assertIn('GAGAL: harian.yml', s)

    def test_malam_sabtu(self):   # Sabtu MYT memproses sesi Jumaat
        s = jalan({'malam': dict(MALAM, sesi='2026-10-30')}, 'malam', '--masa', '2026-10-31 07:17')
        self.assertIn('untuk 2026-11-02', s)

    def test_beli(self):
        b = dict(tarikh='2026-10-27', direkod=640, saham_unik=290, dilangkau=10, buka_lewat=['X M01'],
                 sumber_buka='buka sementara yfinance 09:40 NY')
        s = jalan({'beli': b}, 'beli', '--masa', '2026-10-27 14:20', '--tambah', 'db ok')
        self.assertEqual(s, 'Beli 2026-10-27: 640 direkod (290 saham), 10 dilangkau, 1 buka lewat; '
                            'buka sementara yfinance 09:40 NY | db ok')

    def test_tak_beli(self):
        s = jalan({'beli': dict(tarikh='2026-10-27', direkod=0, nota='tak beli: senarai_beli belum dikemas kini')},
                  'beli', '--masa', '2026-10-27 14:20')
        self.assertTrue(s.startswith('Tak beli 2026-10-27: tak beli: senarai_beli'))
        s = jalan({'beli': dict(tarikh='2026-10-26', direkod=600)}, 'beli', '--masa', '2026-10-27 14:20')
        self.assertTrue(s.startswith('Tak beli 2026-10-27 (belum direkod; belian terakhir 2026-10-26)'))
        self.assertEqual(jalan({}, 'beli', '--masa', '2026-10-31 14:20'), 'Tak beli 2026-10-31: pasaran AS tutup')

    def test_had_panjang(self):
        s = jalan({'beli': dict(tarikh='2026-10-27', direkod=0, nota='x' * 400)}, 'beli', '--masa', '2026-10-27 14:20')
        self.assertEqual(len(s), N.HAD)


def tulis(p, teks):
    with open(p, 'w') as f:
        f.write(teks if isinstance(teks, str) else json.dumps(teks))


def akar_palsu(sektor='2026-10-20', edgar='2026-10-23', nasdaq='2026-10-26', lejar='2026-10-26', papan='2026-10-26'):
    """Folder BacktestShariah2 palsu: papertrade/sektor.csv, data/edgar/status.json, data/pemangkin/earnings_nasdaq.json,
    lejar/status.json, data/analisis/papan.json (None = fail tiada)."""
    d = tempfile.mkdtemp()
    for sub in ('papertrade', 'data/edgar', 'data/pemangkin', 'data/analisis', 'lejar'):
        os.makedirs(os.path.join(d, sub))
    if sektor:
        tulis(os.path.join(d, 'papertrade', 'sektor.csv'), f'tarikh,jenis,nama\n2026-10-12,Sektor,X\n{sektor},Sektor,X\n')
    if edgar:
        tulis(os.path.join(d, 'data/edgar/status.json'), {'hari_terakhir': edgar})
    if nasdaq:
        tulis(os.path.join(d, 'data/pemangkin/earnings_nasdaq.json'), {'dijana': f'{nasdaq} 12:21 UTC', 'tarikh': nasdaq})
    if lejar:
        tulis(os.path.join(d, 'lejar/status.json'), {'sesi_terakhir': lejar})
    if papan:
        tulis(os.path.join(d, 'data/analisis/papan.json'), {'kini': papan, 'lejar_sesi': papan})
    return d


class TestAmaran(unittest.TestCase):
    """Audit 25 Okt 2026 item 6: SST mati sejak 19 Okt dan EDGAR tanpa rahsia tidak kelihatan dalam notifikasi."""

    def test_tiada_amaran_jika_segar(self):
        a = akar_palsu(sektor='2026-10-26')
        s = jalan({'malam': MALAM}, 'malam', '--masa', '2026-10-27 07:17', '--amaran', '--akar', a)
        self.assertNotIn('AMARAN', s)

    def test_sst_edgar_kalendar_basi(self):
        a = akar_palsu(sektor='2026-10-19', edgar=None, nasdaq='2026-10-21')
        s = jalan({'malam': MALAM}, 'malam', '--masa', '2026-10-28 07:17', '--amaran', '--akar', a)
        self.assertIn('AMARAN: SST 9 hari, EDGAR tidak aktif, kalendar 4 sesi', s)
        self.assertLess(len(s), 200)

    def test_edgar_lewat_sesi(self):
        a = akar_palsu(sektor='2026-10-26', edgar='2026-10-21', nasdaq='2026-10-27')
        # hari_terakhir 21 Okt, sesi dijangka 27 Okt: 22, 23, 26, 27 = 4 sesi (> 2)
        self.assertEqual(N.amaran_data(a, N.pd.Timestamp('2026-10-28 07:17', tz='UTC')), ['EDGAR 4 sesi'])
        self.assertEqual(N.sesi_di_belakang(N.date(2026, 10, 27), '2026-10-27'), 0)

    def test_tanpa_bendera_tiada_amaran(self):   # keserasian: tanpa --amaran baris tidak berubah
        a = akar_palsu(sektor=None, edgar=None, nasdaq=None)
        s = jalan({'malam': MALAM}, 'malam', '--masa', '2026-10-27 07:17', '--akar', a)
        self.assertNotIn('AMARAN', s)

    def test_had_sepadan_jana_db(self):
        import bahagi_db, jana_db
        self.assertEqual((N.HAD_DB, N.AMARAN_DB), (bahagi_db.HAD_DB, jana_db.AMARAN_HAD))

    def test_db_80_peratus(self):
        db = tempfile.mkdtemp()
        os.makedirs(os.path.join(db, 'prestasi')); os.makedirs(os.path.join(db, 'papertrade'))
        tulis(os.path.join(db, 'prestasi', 'mae.json'), 'x' * int(0.91 * N.HAD_DB))
        tulis(os.path.join(db, 'papertrade', 'claude_9.json'), 'x' * 1000)
        tulis(os.path.join(db, 'batch_0.json'), 'x' * N.HAD_DB)          # bukan dokumen db
        tulis(os.path.join(db, 'ringkas.json'),
              {'ralat': ['papertrade/claude_51: 270000 bait melebihi had db 262144; dokumen dilangkau (versi lama kekal dalam db)',
                         'amaran: prestasi/mae 238000 bait = 91% had db (bahagikan sebelum melebihi)']})
        self.assertEqual(N.amaran_db(db), ['papertrade/claude_51 LEBIH had', 'prestasi/mae 91%'])
        b = dict(tarikh='2026-10-27', direkod=640, saham_unik=290, dilangkau=10, sumber_buka='yf')
        s = jalan({'beli': b}, 'beli', '--masa', '2026-10-27 14:40', '--db', db, '--tambah', 'db ok')
        self.assertTrue(s.endswith('| AMARAN: db≥80% papertrade/claude_51 LEBIH had, prestasi/mae 91% | db ok'), s)


def sedia(st, akar, *arg):
    d = tempfile.mkdtemp()
    with open(os.path.join(d, 'status_harian.json'), 'w') as f:
        json.dump(st, f)
    out = io.StringIO()
    with contextlib.redirect_stdout(out):
        kod = N.main(['sedia', '--folder', d, '--akar', akar] + list(arg))
    return kod, json.loads(out.getvalue())


class TestSedia(unittest.TestCase):
    """Kesediaan tolakan db (jadual/tolak_db.md A dan B)."""

    def test_malam_siap(self):
        kod, r = sedia({'malam': MALAM}, akar_palsu(), '--masa', '2026-10-27 06:47')
        self.assertEqual((kod, r['siap'], r['jangka'], r['belum']), (0, True, '2026-10-26', []))

    def test_malam_lejar_belum(self):
        kod, r = sedia({'malam': MALAM}, akar_palsu(lejar='2026-10-23', papan='2026-10-23'), '--masa', '2026-10-27 06:47')
        self.assertEqual(kod, 3)
        self.assertEqual(r['belum'], ['lejar.yml', 'analisis.yml'])
        self.assertEqual(r['tembak'], ['lejar.yml'])          # analisis dicetus sendiri selepas lejar.yml
        kod, r = sedia({'malam': dict(MALAM, sesi='2026-10-23')}, akar_palsu(papan='2026-10-23'), '--masa', '2026-10-27 06:47')
        self.assertEqual(r['belum'], ['harian.yml', 'analisis.yml'])
        self.assertEqual(r['tembak'], ['harian.yml', 'analisis.yml'])

    def test_sabtu_sesi_jumaat(self):
        kod, r = sedia({'malam': dict(MALAM, sesi='2026-10-30')}, akar_palsu(lejar='2026-10-30', papan='2026-10-30'),
                       '--masa', '2026-10-31 06:47')
        self.assertEqual((kod, r['jangka']), (0, '2026-10-30'))

    def test_beli(self):
        kod, r = sedia({'beli': dict(tarikh='2026-11-02')}, akar_palsu(), '--untuk', 'beli', '--masa', '2026-11-02 15:33')
        self.assertEqual((kod, r['siap']), (0, True))
        kod, r = sedia({'beli': dict(tarikh='2026-10-30')}, akar_palsu(), '--untuk', 'beli', '--masa', '2026-11-02 15:33')
        self.assertEqual((kod, r['tembak']), (3, ['beli.yml']))
        # 9:20 EST: sebelum gerbang 9:31 -> jangan tembak
        kod, r = sedia({'beli': dict(tarikh='2026-10-30')}, akar_palsu(), '--untuk', 'beli', '--masa', '2026-11-02 14:20')
        self.assertEqual((kod, r['tembak']), (3, []))
        kod, r = sedia({}, akar_palsu(), '--untuk', 'beli', '--masa', '2026-11-26 15:33')   # Kesyukuran
        self.assertEqual((kod, r['cuti']), (0, True))


if __name__ == '__main__':
    unittest.main()
