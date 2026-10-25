# Ujian Papan Penganalisis (standard/penganalisis.py): kos bersih sama dengan enjin, posisi matang sahaja dikira, kohort C
# sebelum Lejar sahaja (tiada kiraan berganda), pengecutan skor, status, semakan luar sampel, dan larian penuh atas data repo.
# 24 Okt 2026 (audit dashboard tab demi tab item 6/16/17/18): ranking tunggal (susun tanpa bundar, peluang pangkat Monte Carlo,
# meter bukti, tarikh status sebenar, kelompok, fasa, nota gabungan beku) dan pantau v3 (sasaran winsor, pengawal bukti,
# ujian sintetik M32/M84 dengan parameter kalibrasi sebenar), serta kalibrasi_skor.py v3 (bootstrap blok, ekor, kelompok).
# 25 Okt 2026 (v4): lebihan EW, n berkesan dua hala, Holm, SPRT, pintu A–F, corong, bendera, isi semula, umur tetap, ramalan.
import json, math, os, sys, tempfile, unittest
from fractions import Fraction
import numpy as np
import pandas as pd

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'standard'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'kod'))
import penganalisis as pg
import enjin

LAJUR = pg.LAJUR_POS


def pos(rows):
    return pd.DataFrame(rows, columns=LAJUR)


class TestPenganalisis(unittest.TestCase):
    def test_bersih_sama_enjin(self):
        x, e = 110.0, 100.0
        self.assertAlmostEqual(pg.bersih((x / e - 1) * 100), (x / e * (1 - enjin.COST) / (1 + enjin.COST) - 1) * 100)

    def test_umur_matang(self):
        self.assertEqual(pg.umur_matang(5), 14)          # minimum 14 hari kalendar
        self.assertEqual(pg.umur_matang(30), 63)         # 1.5 x 30 x 7/5
        self.assertEqual(pg.umur_matang(None), 21)       # tiada data: anggap 10 hari

    def test_hanya_posisi_matang(self):
        P = pos([['M01', 'A', '2026-09-30', '2026-10-01', '2026-10-02', True, -5.0, -5.0, 'C'],
                 ['M01', 'B', '2026-09-30', '2026-10-01', '', False, 8.0, 8.0, 'C'],      # terbuka tetapi matang: untung semasa
                 ['M01', 'C', '2026-10-14', '2026-10-15', '2026-10-16', True, -6.0, -6.0, 'lejar']])  # belum matang
        h = pg.ringkas_hadapan(P, 5, '2026-10-20')
        self.assertEqual((h['posisi'], h['tutup'], h['matang']), (3, 2, 2))
        self.assertAlmostEqual(h['purata'], 1.5)
        self.assertAlmostEqual(h['menang'], 0.5)
        self.assertEqual(h['matang_mula'], '2026-10-15')
        self.assertIsNone(h['matang_20'])

    def test_c_sebelum_lejar_sahaja(self):
        L = pos([['M01', 'A', '2026-10-15', '2026-10-16', '', False, 1.0, 1.0, 'lejar']])
        C = pos([['M01', 'X', '2026-10-08', '2026-10-09', '2026-10-12', True, 2.0, 2.0, 'C'],
                 ['M01', 'A', '2026-10-15', '2026-10-16', '', False, 1.1, 1.1, 'C']])      # isyarat sama dengan Lejar
        H, mula, tindih = pg.gabung_hadapan(L, C)
        self.assertEqual((mula, tindih), ('2026-10-16', 0))
        self.assertEqual(sorted(zip(H.saham, H.sumber)), [('A', 'lejar'), ('X', 'C')])

    def test_lejar_bertindih_c_dibuang(self):
        # C pra-Lejar masih memegang M01 W (atau keluar pada hari isyarat Lejar): enjin mengabaikan isyarat Lejar itu
        L = pos([['M01', 'W', '2026-10-15', '2026-10-16', '', False, 1.0, 1.0, 'lejar'],
                 ['M01', 'Y', '2026-10-15', '2026-10-16', '', False, 1.0, 1.0, 'lejar'],
                 ['M01', 'Z', '2026-10-15', '2026-10-16', '', False, 1.0, 1.0, 'lejar'],
                 ['M02', 'W', '2026-10-15', '2026-10-16', '', False, 1.0, 1.0, 'lejar']])   # kaedah lain: kekal
        C = pos([['M01', 'W', '2026-10-09', '2026-10-12', '', False, 3.0, 3.0, 'C'],
                 ['M01', 'Y', '2026-10-09', '2026-10-12', '2026-10-15', True, -2.0, -2.0, 'C'],
                 ['M01', 'Z', '2026-10-09', '2026-10-12', '2026-10-14', True, -2.0, -2.0, 'C']])  # keluar sebelum isyarat: kekal
        H, mula, tindih = pg.gabung_hadapan(L, C)
        self.assertEqual(tindih, 2)
        self.assertEqual(sorted(zip(H.id, H.saham, H.sumber)),
                         [('M01', 'W', 'C'), ('M01', 'Y', 'C'), ('M01', 'Z', 'C'), ('M01', 'Z', 'lejar'), ('M02', 'W', 'lejar')])

    def test_laras_beli_split(self):
        buka = {('S', '2026-10-16'): 50.0, ('T', '2026-10-16'): 100.2}
        self.assertEqual(pg.laras_beli(100.0, 'S', '2026-10-16', buka, pg.TOL_LARAS), 50.0)    # split 2:1 dalam stor
        self.assertEqual(pg.laras_beli(100.0, 'T', '2026-10-16', buka, pg.TOL_LARAS), 100.0)   # beza 0.2% < toleransi
        self.assertEqual(pg.laras_beli(100.0, 'U', '2026-10-16', buka, pg.TOL_LARAS), 100.0)   # tiada bar

    def test_c_lorong2_harga_semasa(self):
        with tempfile.TemporaryDirectory() as d:
            lajur = ['tarikh_beli', 'saham', 'kaedah', 'id_kaedah', 'harga_beli', 'untung_pct', 'keluar', 'untung_akhir_pct',
                     'tarikh_keluar', 'tarikh_isyarat', 'tidak_sah', 'tidak_dibeli', 'keluar_henti', 'untung_henti_pct']
            pd.DataFrame([['2026-10-09', 'Q', 'M01', 'M01', '10', '-5', 'True', '-5', '2026-10-13', '2026-10-08', '', '', 'False', '']],
                         columns=lajur).to_csv(os.path.join(d, 'claude.csv'), index=False)
            C = pg.muat_c(d, akhir={'Q': 12.0}, buka={})
            self.assertAlmostEqual(C.hasil1.iloc[0], pg.bersih(-5.0))     # lorong 1: untung akhir C
            self.assertAlmostEqual(C.hasil2.iloc[0], pg.bersih(20.0))     # lorong 2 masih dipegang: tutup terakhir, bukan harga beku
            self.assertEqual(C.tarikh_keluar.iloc[0], '2026-10-13')

    def test_berat_dan_skor(self):
        self.assertAlmostEqual(pg.berat_backtest(10 ** 9), pg.N0, places=3)
        self.assertAlmostEqual(pg.berat_backtest(30), 15.0)
        mu, lo, hi = pg.skor(2.0, 10.0, 0, 0.0, None)
        self.assertEqual(mu, 2.0)
        self.assertAlmostEqual(hi - mu, 1.96 * 10 / math.sqrt(pg.N0))
        mu, lo, hi = pg.skor(2.0, 10.0, 970, -1.0, 8.0)      # data hadapan banyak menguasai jangkaan
        self.assertAlmostEqual(mu, (30 * 2.0 + 970 * -1.0) / 1000)
        self.assertAlmostEqual(hi - mu, 1.96 * 8.0 / math.sqrt(1000))

    def test_status(self):
        self.assertEqual(pg.status_kaedah(5, -9.0, 4.0, 2.0, -1, 3), 'BELUM CUKUP')
        self.assertEqual(pg.status_kaedah(12, -3.0, 4.0, 2.0, -1, 3), 'AMARAN')   # t = -5/(4/√12) < -2
        self.assertEqual(pg.status_kaedah(25, 1.0, 9.0, 1.0, 0.2, 2.0), 'KUAT')
        self.assertEqual(pg.status_kaedah(25, 0.5, 9.0, 0.5, -3.0, -0.1), 'LEMAH')
        self.assertEqual(pg.status_kaedah(25, 0.5, 9.0, 0.5, -1.0, 2.0), 'PERHATI')

    def test_kukuh_pangkas_kluster_hari(self):
        # 22 Okt 2026 (R5–R7): satu squeeze tidak menguasai; posisi hari sama = sedikit maklumat bebas; < 10 hari beli -> BELUM CUKUP
        import numpy as np
        x = [1.0] * 39 + [300.0]
        self.assertAlmostEqual(pg.purata_pangkas(x), 1.0)
        self.assertGreater(sum(x) / len(x), 8)
        self.assertEqual(pg.n_berkesan(np.arange(40.0), ['2026-10-16'] * 40), 1.0)          # satu hari beli
        r = np.random.default_rng(3)
        hari = np.repeat(np.arange(10), 20); kesan = r.normal(0, 5, 10)[hari]               # 10 hari, kesan pasaran kuat setiap hari
        nb = pg.n_berkesan(kesan + r.normal(0, 1, 200), hari.astype(str))
        self.assertLess(nb, 40)
        self.assertGreater(pg.n_berkesan(r.normal(0, 1, 200), hari.astype(str)), 100)    # tiada kesan hari: hampir n
        self.assertEqual(pg.status_kaedah(25, 1.0, 9.0, 1.0, 0.2, 2.0, hari=9), 'BELUM CUKUP')
        self.assertEqual(pg.status_kaedah(25, 1.0, 9.0, 1.0, 0.2, 2.0, hari=10), 'KUAT')

    def test_pantau(self):
        # 22 Okt 2026 (Fasa 4 item 15): kohort matang harian -> CUSUM bawah, kejatuhan/tempoh lawan backtest, P(purata <= 0)
        import numpy as np
        kal = dict(winsor=[-3.0, 9.0], mu_winsor=0.0, mu_kohort=0.8, sd_winsor=3.0, h=1.6, dd_maks=100.0, dd_tempoh=400)
        hari = list(pd.bdate_range('2026-01-01', periods=60).strftime('%Y-%m-%d'))
        rugi = pd.DataFrame(dict(tarikh_beli=hari, hasil1=[-2.5] * 60))
        x = pg.pantau_kaedah(rugi, 14, '2026-12-31', kal, 0.25, -1.0, -2.0, 0.0, 60)
        self.assertEqual(x['pantau'], 'BERSARA'); self.assertGreaterEqual(x['p_amaran'], 2); self.assertGreater(x['p_rugi'], 0.9)
        self.assertAlmostEqual(x['p_dd'], 150.0)
        baik = pd.DataFrame(dict(tarikh_beli=hari, hasil1=np.random.default_rng(1).normal(1.0, 3, 60)))
        self.assertEqual(pg.pantau_kaedah(baik, 14, '2026-12-31', kal, 0.25, 1.0, 0.2, 1.8, 60, k=0.5)['pantau'], pg.PANTAU_OK)
        jatuh = pd.DataFrame(dict(tarikh_beli=hari, hasil1=[3.0] * 20 + [-4.0] * 40))      # kejatuhan 160 > 1.5 x 100
        y = pg.pantau_kaedah(jatuh, 14, '2026-12-31', dict(kal, h=1e9), 0.25, 0.5, -1.0, 2.0, 60)
        self.assertEqual(y['pantau'], 'GANTUNG'); self.assertIn('kejatuhan', y['p_sebab'])
        # brek hadapan (v3, winsor dengan winsor): purata 20 hari beli terakhir (diwinsor) < p5 bergulir backtest - (purata winsor -
        # sasaran); sasaran = min(0.8, 0.25 x 0.8) = 0.2 -> had = -1.5 - 0.6 = -2.1
        kb = dict(kal, mu_winsor=0.8, h=1e9, dd_maks=1e6, dd_tempoh=10 ** 6, p5_bergulir=-1.5, n_bergulir=20)
        lemah = pd.DataFrame(dict(tarikh_beli=hari, hasil1=[1.0] * 40 + [-2.3] * 20))
        z = pg.pantau_kaedah(lemah, 14, '2026-12-31', kb, 0.25, 0.5, -1.0, 2.0, 60)
        self.assertEqual(z['pantau'], 'GANTUNG'); self.assertAlmostEqual(z['p_bergulir_had'], -2.1); self.assertIn('purata 20 hari beli', z['p_sebab'])
        sedang = pd.DataFrame(dict(tarikh_beli=hari, hasil1=[1.0] * 40 + [-1.9] * 20))
        self.assertEqual(pg.pantau_kaedah(sedang, 14, '2026-12-31', kb, 0.25, 0.5, -1.0, 2.0, 60)['pantau'], pg.PANTAU_OK)
        self.assertIsNone(pg.pantau_kaedah(lemah.iloc[-19:], 14, '2026-12-31', kb, 0.25, 0.5, -1.0, 2.0, 19)['p_bergulir'])   # < 20 hari beli
        muda = pd.DataFrame(dict(tarikh_beli=['2026-12-30'], hasil1=[-9.0]))                # belum matang
        self.assertEqual(pg.pantau_kaedah(muda, 14, '2026-12-31', kal, 0.25, 0.5, -1.0, 2.0, 1)['pantau'], 'BELUM CUKUP')
        self.assertEqual(pg.pantau_kaedah(baik, 14, '2026-12-31', None, 0.25, 1.0, 0.2, 1.8, 60)['p_dd'], None)

    def test_lintas_earnings(self):
        P = pos([dict(id='M01', saham='A', tarikh_isyarat='2026-10-14', tarikh_beli='2026-10-15', tarikh_keluar='2026-10-20', tutup1=True,
                      hasil1=1.0, hasil2=1.0, sumber='lejar'),
                 dict(id='M01', saham='A', tarikh_isyarat='2026-10-21', tarikh_beli='2026-10-22', tarikh_keluar='', tutup1=False,
                      hasil1=1.0, hasil2=1.0, sumber='lejar'),
                 dict(id='M01', saham='B', tarikh_isyarat='2026-10-14', tarikh_beli='2026-10-15', tarikh_keluar='', tutup1=False,
                      hasil1=1.0, hasil2=1.0, sumber='lejar')])
        E = {'A': ['2026-10-16'], 'B': ['2026-10-15']}     # B: kesan pada hari beli (jurang sebelum buka) -> bukan lintas
        self.assertEqual(list(pg.lintas_earnings(P, E, '2026-10-30')), [True, False, False])
        with tempfile.TemporaryDirectory() as d:
            f = os.path.join(d, 'tv.csv')
            pd.DataFrame(dict(ticker=['A', 'B'], earnings_release_date=['1792526400', ''],          # 2026-10-20 16:00 NY -> 21 Okt
                              earnings_release_next_date=['1793109600', '1792497600'])).to_csv(f, index=False)  # 27 Okt 10:00; 20 Okt 08:00
            e = pg.muat_earnings(f, os.path.join(d, 'tiada.csv'))
            self.assertEqual(e, {'A': ['2026-10-21', '2026-10-27'], 'B': ['2026-10-20']})

    def test_semakan(self):
        reg = dict(subset_menang=3, subset_n=4)
        wfo = dict(cagr=0.40, ew=0.326)
        at = dict(cagr_a=0.16, spy_a=0.146, cagr_b=0.10, spy_b=0.146)
        self.assertEqual(pg.semakan(reg, wfo, at), (True, True, False))
        self.assertEqual(pg.semakan({}, None, None), (None, None, None))

    def test_harga_sandaran_stor(self):
        with tempfile.TemporaryDirectory() as d:
            tk, st = os.path.join(d, 'terkini.csv'), os.path.join(d, 'stor')
            os.makedirs(st)
            pd.DataFrame([['A', '20261016', 10.0], ['A', '20261019', 11.0]], columns=['ticker', 'date', 'close']).to_csv(tk, index=False)
            pd.DataFrame([['A', '20261019', 99.0], ['B', '20261016', 5.0], ['B', '20261019', 6.0], ['B', '20261020', 7.0]],
                         columns=['ticker', 'date', 'close']).to_csv(os.path.join(st, 'harga_A.csv'), index=False)
            akhir, t = pg.harga_akhir(tk, st)
            self.assertEqual(t, '2026-10-19')
            self.assertEqual(akhir, {'A': 11.0, 'B': 6.0})      # terkini didahulukan; stor hanya bagi saham tiada, hingga tarikh sama

    def test_larian_penuh(self):
        with tempfile.TemporaryDirectory() as d:
            md, js = os.path.join(d, 'P.md'), os.path.join(d, 'p.json')
            pg.main(['--md', md, '--json', js])
            doc = json.load(open(js, encoding='utf-8'))
            kat = json.load(open(pg.KATALOG, encoding='utf-8'))['rows']
            self.assertEqual(len(doc['rows']), len(kat))
            # v4: papan.json boleh melebihi had satu dokumen db; jana_db membahagi (bahagi_db) setiap bahagian < had
            from bahagi_db import bahagi, bait, HAD_DB
            self.assertTrue(all(bait(x) < HAD_DB for _, x in bahagi(doc, 'papan', 200000)))
            self.assertTrue(os.path.exists(os.path.join(d, 'sejarah_skor.csv')))   # sebelah --json, bukan fail repo
            self.assertTrue(os.path.exists(os.path.join(d, 'bendera_kaedah.csv')))
            self.assertEqual(len(doc['penemuan']), 3)
            self.assertTrue(set(r['status'] for r in doc['rows']) <= set(pg.STATUS))
            k = [r['kedudukan'] for r in doc['rows'] if r['kedudukan']]
            self.assertEqual(k, list(range(1, len(k) + 1)))
            self.assertTrue(all(r['swing'] and not r['sampel_kecil'] for r in doc['rows'] if r['kedudukan']))
            self.assertIn('## 3 penemuan utama', open(md, encoding='utf-8').read())
            # ranking tunggal (24 Okt 2026): medan baharu setiap baris
            medan = ('p_top1', 'p_top5', 'pangkat_p5', 'pangkat_p95', 'lb_bulan', 'g_matang', 'g_perlu', 'nb', 'nb_perlu',
                     'tarikh_sebenar', 'ditolak', 'lejar_n', 'median_bt', 'pangkas5_bt', 'pct_top1', 'kelompok', 'kelompok_wakil',
                     'pantau', 'p_sebab', 'pantau_sasaran', 'pantau_ambang')
            for r in doc['rows']:
                self.assertTrue(all(m in r for m in medan), r['id'])
                self.assertNotIn('_kb', r)
                self.assertEqual(r['g_perlu'], 10)
                self.assertIsInstance(r['ditolak'], bool)
                self.assertTrue(set(r['pantau'] for r in doc['rows']) <= set(pg.PANTAU_STATUS))
            ked = sorted((r for r in doc['rows'] if r['kedudukan']), key=lambda r: r['kedudukan'])
            self.assertAlmostEqual(sum(r['p_top1'] for r in ked), 1.0, places=2)
            self.assertAlmostEqual(sum(r['p_top5'] for r in ked), 5.0, places=2)
            self.assertTrue(all(1 <= r['pangkat_p5'] <= r['pangkat_p95'] <= len(ked) for r in ked))
            self.assertTrue(all(a['skor_bulan'] >= b['skor_bulan'] for a, b in zip(ked, ked[1:])))
            self.assertTrue(all(r['p_top1'] is None for r in doc['rows'] if not r['kedudukan']))
            f = doc['fasa']
            self.assertEqual(set(f), {'matang_hadapan', 'jumlah_hadapan', 'kaedah_bukti', 'tarikh_sebenar_pertama', 'tarikh_top5', 'teks',
                                      'swing', 'bukan_swing'})
            self.assertEqual(f['swing']['matang'] + f['bukan_swing']['matang'], f['matang_hadapan'])
            self.assertEqual(f['matang_hadapan'], sum(r['h_matang'] for r in doc['rows']))
            self.assertEqual(f['kaedah_bukti'], sum(r['status'] != 'BELUM CUKUP' for r in doc['rows']))
            self.assertEqual(len(f['tarikh_top5']), 2)
            self.assertEqual(set(doc['label_semakan']), {'s14', 'wfo', 'at'})
            self.assertTrue(doc['gabungan_beku_nota'].startswith('SEMENTARA — dipilih atas data C belum matang; kedudukan kini #'))
            with open(os.path.join(pg.LEJAR, 'status.json'), encoding='utf-8') as fh:
                st = json.load(fh)
            self.assertEqual(doc['kini'], st['sesi_terakhir'])                    # tarikh papan = sesi Lejar (bukan terkini.csv)
            self.assertLessEqual(doc['harga_pada'], doc['kini'])
            for r in doc['rows']:                                                  # kelompok: wakil ialah ahli kelompok sama
                if r['kelompok']:
                    w = next(x for x in doc['rows'] if x['id'] == r['kelompok_wakil'])
                    self.assertEqual(w['kelompok'], r['kelompok'])


def baris(i, kb, swing=True, bt_n=500, **kw):
    return dict(id=i, _kb=kb, _se=1.0, swing=swing, bt_n=bt_n, **kw)


class TestRankingTunggal(unittest.TestCase):
    def test_susun_tanpa_bundar(self):
        # 0.678 dan 0.684 sama-sama 0.68 jika dibundar: susunan mesti ikut nilai sebenar, bukan susunan katalog
        rows = [baris('M46', 0.678), baris('M119', 0.684), baris('M01', 2.0, swing=False), baris('M22', 9.0, bt_n=42)]
        sw, kecil, lain = pg.susun_kedudukan(rows)
        self.assertEqual([r['id'] for r in sw], ['M119', 'M46'])
        self.assertEqual([r['kedudukan'] for r in sw], [1, 2])
        self.assertEqual(([r['id'] for r in kecil], [r['id'] for r in lain]), (['M22'], ['M01']))
        self.assertIsNone(kecil[0]['kedudukan'])

    def test_peluang_pangkat(self):
        p1, p5, q5, q95 = pg.peluang_pangkat([10.0, 0.0, 0.0, 0.0], [0.1, 1.0, 1.0, 1.0], cabutan=4000, top=2)
        self.assertGreater(p1[0], 0.999)                                       # jauh di atas: hampir pasti #1
        self.assertEqual((q5[0], q95[0]), (1, 1))
        self.assertTrue(all(abs(x - 1 / 3) < 0.05 for x in p5[1:]))          # tiga kaedah sama: P(#2) = 1/3 setiap satu
        self.assertAlmostEqual(float(p1.sum()), 1.0); self.assertAlmostEqual(float(p5.sum()), 2.0)
        a = pg.peluang_pangkat([1.0, 0.9, 0.5], [1.0, 1.0, 1.0])
        b = pg.peluang_pangkat([1.0, 0.9, 0.5], [1.0, 1.0, 1.0])
        self.assertTrue(all((x == y).all() for x, y in zip(a, b)))            # berbiji: boleh diulang
        self.assertGreaterEqual(pg.MC_CABUTAN, 2000)
        self.assertTrue(all(1 <= x <= y <= 3 for x, y in zip(a[2], a[3])))

    def test_nb_perlu(self):
        # v4: z 3.0 (sama dengan KUAT); dahulu 1.96
        self.assertEqual(pg.nb_perlu(2.0, 10.0, 30.0), math.ceil((3.0 * 10 / 2) ** 2 - 30))     # 225 - 30 -> 195
        self.assertEqual(pg.nb_perlu(-2.0, 10.0, 30.0), 195)                                      # simetri (bukti LEMAH)
        self.assertEqual(pg.nb_perlu(2.0, 10.0, 30.0, z=1.96), 67)                                # z 1.96 lama
        self.assertEqual(pg.nb_perlu(20.0, 5.0, 30.0), pg.NB_MIN)                                # lantai pengawal bukti
        self.assertEqual(pg.nb_perlu(2.0, 1.0, 0.0), math.ceil((3.0 * pg.SD_MIN / 2) ** 2))        # SD minimum SD_MIN -> 57
        self.assertIsNone(pg.nb_perlu(0.0, 10.0, 30.0))

    def test_sesi_nyse(self):
        s = pg.sesi_nyse('2026-11-20', '2026-12-31')
        self.assertNotIn('2026-11-21', s)                                      # Sabtu
        self.assertNotIn('2026-12-26', s)
        try:
            import exchange_calendars  # noqa: F401
            self.assertNotIn('2026-11-26', s); self.assertNotIn('2026-12-25', s)   # Kesyukuran, Krismas
        except ImportError:
            pass
        jauh = pg.sesi_nyse('2040-01-01', '2040-01-10')                        # di luar julat kalendar -> hari bekerja
        self.assertEqual(jauh[0], '2040-01-02')

    def test_tarikh_bukti(self):
        sesi = pg.sesi_nyse('2026-10-01', '2027-12-31')
        depan = [x for x in sesi if x > '2026-10-23']
        # data sedia ada sudah cukup: 10 hari beli x 2 posisi -> hari beli ke-10 + umur 14 hari, sesi pertama selepas itu
        hari = sesi[:10]
        t = pg.tarikh_bukti({h: 2 for h in hari}, 14, None, None, depan, sesi)
        self.assertEqual(t, next(x for x in sesi if x >= str((pd.Timestamp(hari[-1]) + pd.Timedelta(days=14)).date())))
        # unjuran: tiada posisi, separuh sesi berbelian, 1 posisi sehari -> 20 hari beli = sesi depan ke-40
        t = pg.tarikh_bukti({}, 14, Fraction(1, 2), Fraction(1), depan, sesi)
        self.assertEqual(t, next(x for x in sesi if x >= str((pd.Timestamp(depan[39]) + pd.Timedelta(days=14)).date())))
        # syarat 10 hari beli mengikat walaupun posisi banyak: 5 posisi sehari, setiap sesi -> hari beli ke-10 = depan[9]
        t = pg.tarikh_bukti({}, 14, Fraction(1), Fraction(5), depan, sesi)
        self.assertEqual(t, next(x for x in sesi if x >= str((pd.Timestamp(depan[9]) + pd.Timedelta(days=14)).date())))
        # 8 hari beli sedia ada (16 posisi) + kadar 1/3 -> 2 hari beli lagi (ceil(2 / (1/3)) = sesi ke-6)
        t = pg.tarikh_bukti({h: 2 for h in sesi[:8]}, 20, Fraction(1, 3), Fraction(2), depan, sesi)
        self.assertEqual(t, next(x for x in sesi if x >= str((pd.Timestamp(depan[5]) + pd.Timedelta(days=20)).date())))
        self.assertIsNone(pg.tarikh_bukti({}, 14, None, None, depan, sesi))  # tiada kadar isyarat

    def test_kelompok_dan_fasa(self):
        rows = [dict(id='A', _kb=1.0, kedudukan=2), dict(id='B', _kb=2.0, kedudukan=1), dict(id='C', _kb=0.5, kedudukan=3),
                dict(id='D', _kb=5.0, kedudukan=None)]
        KALL = {'A': dict(kelompok='A'), 'B': dict(kelompok='C'), 'C': dict(kelompok='C'), 'D': dict(kelompok='A')}
        pg.kelompok_rows(rows, KALL)
        k = {r['id']: (r['kelompok'], r['kelompok_wakil']) for r in rows}
        self.assertEqual(k, {'B': (1, 'B'), 'C': (1, 'B'), 'A': (2, 'A'), 'D': (2, 'A')})   # wakil: berkedudukan dahulu
        f = [dict(id=f'M{i}', kedudukan=i, h_matang=0, h_posisi=10, status='BELUM CUKUP', tarikh_sebenar=t)
             for i, t in enumerate(['2026-12-01', '2026-11-20', None, '2026-12-10', '2026-11-30', '2026-11-04'], 1)]
        x = pg.fasa_papan(f)
        self.assertEqual(x['tarikh_sebenar_pertama'], dict(id='M6', kedudukan=6, tarikh='2026-11-04'))
        self.assertEqual(x['tarikh_top5'], ['2026-11-20', None])            # satu dalam 5 teratas tiada tarikh -> maks None
        self.assertEqual((x['kaedah_bukti'], x['matang_hadapan'], x['jumlah_hadapan']), (0, 0, 60))
        self.assertTrue(x['teks'].startswith('Fasa 0'))
        with tempfile.TemporaryDirectory() as d:
            g = os.path.join(d, 'g.json')
            with open(g, 'w', encoding='utf-8') as fh:
                json.dump(dict(kaedah=[dict(id='M2'), dict(id='M9')]), fh)
            self.assertEqual(pg.nota_gabungan(f, g), 'SEMENTARA — dipilih atas data C belum matang; kedudukan kini #2/– '
                                                     'dalam ranking ini (M2/M9)')

    def test_harga_hingga_sesi_lejar(self):
        with tempfile.TemporaryDirectory() as d:
            tk, st = os.path.join(d, 'terkini.csv'), os.path.join(d, 'stor')
            os.makedirs(st)
            pd.DataFrame([['A', '20261022', 10.0], ['A', '20261023', 11.0]], columns=['ticker', 'date', 'close']).to_csv(tk, index=False)
            pd.DataFrame([['B', '20261022', 5.0], ['B', '20261023', 6.0]],
                         columns=['ticker', 'date', 'close']).to_csv(os.path.join(st, 'harga_A.csv'), index=False)
            self.assertEqual(pg.harga_akhir(tk, st, hingga='2026-10-22'), ({'A': 10.0, 'B': 5.0}, '2026-10-22'))
            self.assertEqual(pg.harga_akhir(tk, st), ({'A': 11.0, 'B': 6.0}, '2026-10-23'))


class TestPantauV3(unittest.TestCase):
    """Item 18: sasaran CUSUM winsor dengan winsor, pengawal bukti minimum, parameter kalibrasi sebenar (bootstrap blok)."""
    KAL, K, KALL = pg.muat_kalibrasi(semua=True)

    def kohort(self, n, x, mula='2026-01-05'):
        hari = list(pd.bdate_range(mula, periods=n).strftime('%Y-%m-%d'))
        return pd.DataFrame(dict(tarikh_beli=hari, hasil1=[x] * n))

    def test_sasaran_winsor(self):
        self.assertAlmostEqual(pg.sasaran_cusum(dict(mu_winsor=0.6467, mu_kohort=5.87), 0.5), 0.32335)  # bukan 0.65 - 0.5 x 5.87
        self.assertAlmostEqual(pg.sasaran_cusum(dict(mu_winsor=-0.4, mu_kohort=3.0), 0.25), -0.4)       # potongan tidak menaikkan
        for m, kal in self.KAL.items():          # tanda sasaran = tanda purata winsor (dahulu negatif bagi 114/133 kaedah)
            self.assertEqual(pg.sasaran_cusum(kal, 0.25) < 0, kal['mu_winsor'] < 0, m)

    def test_m32_25_hari_rugi_5(self):
        kal = self.KAL['M32']
        x = pg.pantau_kaedah(self.kohort(25, -5.0), 14, '2026-12-31', kal, 0.5, 1.0, -2.0, 4.0, 25, self.K)
        self.assertIn(x['pantau'], ('AMARAN', 'GANTUNG'), x)
        # parameter seakan M32 (tetap, tidak bergantung pada fail): kohort winsor sd 10.4, purata winsor 0.65, h 6.29 (k 0.25)
        m32 = dict(winsor=[-8.73, 30.42], mu_winsor=0.6467, mu_kohort=5.87, sd_winsor=10.39, h=6.29, arl_bootstrap=261.3,
                   dd_maks=433.8, dd_tempoh=1008, p5_bergulir=-5.05, p5_bergulir_winsor=-4.84, n_bergulir=20)
        y = pg.pantau_kaedah(self.kohort(25, -5.0), 14, '2026-12-31', m32, 0.5, 1.0, -2.0, 4.0, 25, 0.25)
        self.assertIn(y['pantau'], ('AMARAN', 'GANTUNG'), y)
        z = pg.pantau_kaedah(self.kohort(25, -5.0), 14, '2026-12-31', dict(m32, h=1.19), 0.5, 1.0, -2.0, 4.0, 25, 0.5)
        self.assertEqual(z['pantau'], pg.PANTAU_OK)     # kalibrasi v2 (k 0.5): buta terhadap rugi berterusan -5% (dapatan audit)

    def test_4_kohort_tidak_bersara(self):
        for m in ('M84', 'M22', 'M24'):
            kal = self.KAL.get(m)
            if not kal:
                continue
            x = pg.pantau_kaedah(self.kohort(4, -10.0), 14, '2026-12-31', kal, 0.5, -5.0, -9.0, -1.0, 4, self.K)
            self.assertEqual(x['pantau'], 'BELUM CUKUP', (m, x))
        kal = dict(winsor=[-3.0, 9.0], mu_winsor=0.5, mu_kohort=0.8, sd_winsor=3.0, h=1.0, dd_maks=1.0, dd_tempoh=1)
        x = pg.pantau_kaedah(self.kohort(4, -10.0), 14, '2026-12-31', kal, 0.5, -5.0, -9.0, -1.0, 25, 0.25)
        self.assertEqual(x['pantau'], 'BELUM CUKUP')
        self.assertGreaterEqual(x['p_amaran'], 2)                              # pencetus dikira tetapi belum dinilai
        self.assertIn('belum dinilai', x['p_sebab'])
        # nb minimum: 12 hari beli tetapi n berkesan < NB_MIN -> BELUM CUKUP
        self.assertEqual(pg.pantau_kaedah(self.kohort(12, -10.0), 14, '2026-12-31', kal, 0.5, -5.0, -9.0, -1.0, 12, 0.25,
                                          nb=5.0)['pantau'], 'BELUM CUKUP')
        # status kaedah: AMARAN juga memerlukan >= 10 hari beli
        self.assertEqual(pg.status_kaedah(12, -3.0, 4.0, 2.0, -1, 3, hari=4, nb=12), 'BELUM CUKUP')

    def test_teks_pantau(self):
        s, a = pg.teks_pantau(self.KAL['M32'], 0.5, self.K)
        self.assertIn('%', s); self.assertIn('GANTUNG', a); self.assertIn('AMARAN', a)
        self.assertEqual(pg.teks_pantau(None, 0.5), (None, None))


class TestKalibrasiV3(unittest.TestCase):
    def setUp(self):
        import kalibrasi_skor as K
        self.K = K

    def test_kelompok_pautan_lengkap(self):
        R = pd.DataFrame([[1, .8, .75, .1], [.8, 1, .65, .2], [.75, .65, 1, 0], [.1, .2, 0, 1]], index=list('ABCD'), columns=list('ABCD'))
        self.assertEqual(self.K.kelompok(R), {'A': 'A', 'B': 'A', 'C': 'C', 'D': 'D'})   # C-B 0.65 < 0.7: tidak bergabung
        R.loc['B', 'C'] = R.loc['C', 'B'] = 0.72
        self.assertEqual(self.K.kelompok(R), {'A': 'A', 'B': 'A', 'C': 'A', 'D': 'D'})
        R.loc['A', 'D'] = R.loc['D', 'A'] = np.nan
        self.assertEqual(self.K.kelompok(R)['D'], 'D')

    def test_ekor_dan_blok(self):
        self.assertAlmostEqual(self.K.pct_teratas([10, 1, 1, 1, -2]), 100 * 10 / 11)
        self.assertIsNone(self.K.pct_teratas([-1, -2]))
        z = np.arange(12.0); blok = np.repeat(['a', 'b', 'c'], 4)
        b = self.K.sampel_blok(z, blok, 40)
        self.assertGreaterEqual(len(b), 40)
        for i in range(0, 40, 4):                                              # blok bulan kekal utuh (urutan dalam blok)
            self.assertEqual(b[i:i + 4], list(z[int(b[i]):int(b[i]) + 4]))

    def test_fail_kalibrasi_v3(self):
        d = json.load(open(pg.KALIBRASI, encoding='utf-8'))
        self.assertEqual(d['pantau'].get('bootstrap'), 'blok bulanan')
        self.assertEqual(d['pantau']['k'], 0.25)
        self.assertEqual(d['kelompok']['ambang'], 0.7)
        for m, r in d['kaedah'].items():
            self.assertIn('median', r, m); self.assertIn('kelompok', r, m)
            if r.get('pantau'):
                self.assertIn('p5_bergulir_winsor', r['pantau'], m)


class TestKedudukanSebelum(unittest.TestCase):
    def test_sesi_baharu_dan_larian_semula(self):
        rows = [dict(id='M01', kedudukan=1), dict(id='M02', kedudukan=2), dict(id='M09', kedudukan=3)]
        lama = dict(kini='2026-10-19', rows=[dict(id='M01', kedudukan=2, kedudukan_sebelum=5), dict(id='M02', kedudukan=1)])
        pg.kedudukan_sebelum(rows, '2026-10-20', lama)          # sesi baharu: rujukan = kedudukan lama
        self.assertEqual([r.get('kedudukan_sebelum') for r in rows], [2, 1, None])
        rows2 = [dict(id='M01', kedudukan=1)]
        pg.kedudukan_sebelum(rows2, '2026-10-19', lama)         # larian semula data sama: rujukan lama kekal
        self.assertEqual(rows2[0]['kedudukan_sebelum'], 5)
        rows3 = [dict(id='M01', kedudukan=1)]
        pg.kedudukan_sebelum(rows3, '2026-10-20', None)         # tiada fail lama
        self.assertNotIn('kedudukan_sebelum', rows3[0])


class TestPenganalisisV4(unittest.TestCase):
    """25 Okt 2026 (Penganalisis v4, audit pratonton): lebihan EW, n berkesan dua hala, Holm, SPRT, pintu A–F, corong, bendera,
    kohort isi semula, umur tetap, sejarah skor + ramalan, kredit AUTOTUNE sahaja."""

    def ew(self, n=8):
        t = list(pd.bdate_range('2026-10-12', periods=n).strftime('%Y-%m-%d'))
        cc = [0.01, -0.02, 0.005, 0.0, 0.03, -0.01, 0.002, 0.004][:n]
        oc = [0.004, -0.01, 0.001, 0.002, 0.01, -0.004, 0.0, 0.001][:n]
        e = pd.DataFrame(dict(n=100, ew_cc=cc, ew_oc=oc), index=pd.Index(t, name='tarikh'))
        e['ew_indeks'] = (1 + e.ew_cc).cumprod(); e['ew_co'] = (1 + e.ew_cc) / (1 + e.ew_oc) - 1
        return e

    def test_ew_tempoh_sama_penanda(self):
        import penanda_ew
        e = self.ew()
        t = list(e.index)
        r = pg.ew_tempoh(e, [t[0], t[2], t[1], '2026-10-11'], [t[4], t[2], '2026-10-24', t[3]])
        self.assertAlmostEqual(r[0], penanda_ew.tempoh(e, t[0], t[4]))                     # buka t0 -> tutup t4
        self.assertAlmostEqual(r[1], e.ew_oc.iloc[2])                                        # beli dan nilai hari sama
        self.assertAlmostEqual(r[2], penanda_ew.tempoh(e, t[1], t[-1]))                     # akhir di luar siri -> sesi terakhir
        self.assertTrue(np.isnan(r[3]))                                                      # mula bukan sesi
        b = pg.ew_tempoh(e, [t[0]], [t[3]], [True])[0]                                       # keluar pada BUKA t3
        self.assertAlmostEqual(b, (1 + penanda_ew.tempoh(e, t[0], t[2])) * (1 + e.ew_co.iloc[3]) - 1)

    def test_tambah_lebihan(self):
        e = self.ew(); t = list(e.index)
        P = pd.DataFrame([dict(id='M01', saham='A', tarikh_isyarat=t[0], tarikh_beli=t[1], tarikh_keluar=t[3], tutup1=True, hasil1=5.0,
                               hasil2=5.0, sumber='lejar', buka_keluar=True, hb=10.0, kohort='lejar'),
                          dict(id='M01', saham='B', tarikh_isyarat=t[0], tarikh_beli=t[1], tarikh_keluar='', tutup1=False, hasil1=-1.0,
                               hasil2=-1.0, sumber='lejar', buka_keluar=False, hb=10.0, kohort='lejar')])
        X = pg.tambah_lebihan(P, e, t[5])
        self.assertAlmostEqual(X.ew.iloc[0], 100 * pg.ew_tempoh(e, [t[1]], [t[3]], [True])[0])
        self.assertAlmostEqual(X.ew.iloc[1], 100 * pg.ew_tempoh(e, [t[1]], [t[5]])[0])      # terbuka: hingga kini
        self.assertAlmostEqual(X.lebihan.iloc[0], 5.0 - X.ew.iloc[0])
        self.assertTrue(pg.tambah_lebihan(P, None, t[5]).lebihan.isna().all())

    def test_buka_keluar(self):
        self.assertTrue(pg.buka_keluar_lejar('isyarat keluar', '10', '', ''))
        self.assertTrue(pg.buka_keluar_lejar('henti', '9.5', '10', ''))                     # jurang bawah henti
        self.assertFalse(pg.buka_keluar_lejar('henti', '10', '10', ''))                     # tepat pada henti: dalam hari
        self.assertTrue(pg.buka_keluar_lejar('sasaran', '12', '', '11'))
        self.assertFalse(pg.buka_keluar_lejar('masa', '12', '', ''))
        self.assertTrue(pg.buka_keluar_c('Keluar: isyarat keluar (jual pada buka 12 Okt)'))
        self.assertTrue(pg.buka_keluar_c('Keluar: kena henti (buka bawah henti) (22 Okt @ 73.11)'))
        self.assertFalse(pg.buka_keluar_c('Keluar: kena henti'))

    def test_se_dua_hala(self):
        r = np.random.default_rng(7)
        hari = np.repeat([f'd{i}' for i in range(20)], 10); saham = np.tile([f's{i}' for i in range(10)], 20)
        x = r.normal(0, 1, 200)
        self.assertGreater(pg.se_dua_hala(x, hari, saham)['nb'], 100)                     # tiada kesan kelompok: hampir n
        y = r.normal(0, 3, 10)[np.tile(np.arange(10), 20)] + r.normal(0, 1, 200)          # kesan saham kuat merentas hari
        d2 = pg.se_dua_hala(y, hari, saham)
        self.assertLess(d2['nb'], 40)
        self.assertLess(d2['nb'], pg.n_berkesan(y, hari))                                   # sehala ikut hari terlepas kesan saham
        self.assertEqual((d2['g_hari'], d2['g_saham']), (20, 10))
        k = pg.se_dua_hala(np.arange(12.0), ['a'] * 6 + ['b'] * 6, [f's{i}' for i in range(12)])
        self.assertEqual(k['nb'], 2.0)                                                       # < 5 hari beli: nb = bilangan hari
        self.assertAlmostEqual(k['se'], float(np.std(np.arange(12.0), ddof=1)) / math.sqrt(2))
        self.assertIsNone(pg.se_dua_hala([1.0], ['a'], ['s'])['se'])

    def test_holm_dan_z(self):
        self.assertEqual(pg.holm([0.01, 0.04, 0.03, None]), [0.03, 0.06, 0.06, None])
        self.assertEqual(pg.holm([0.5, 0.9]), [1.0, 1.0])
        self.assertAlmostEqual(pg.z_daripada_p(0.00135), 3.0, places=2)
        self.assertIsNone(pg.z_daripada_p(None))
        self.assertGreater(pg.z_daripada_p(0.0), 7.9); self.assertLess(pg.z_daripada_p(1.0), -7.9)

    def test_sprt(self):
        t = [f'2026-11-{i:02d}' for i in range(1, 31)]
        x = pg.sprt(np.full(9, 5.0), 1.0, 2.0, t[:9])
        self.assertEqual(x['status'], 'TERUSKAN'); self.assertIn('belum diputuskan', x['nota'])   # < 10 kohort walau llr besar
        self.assertAlmostEqual(x['llr'], 9 * (1.0 * 5.0 - 0.5) / 4.0)
        y = pg.sprt(np.full(30, 5.0), 1.0, 2.0, t)
        self.assertEqual((y['status'], y['pada']), ('H1', t[9]))                          # lintasan pertama selepas pengawal
        z = pg.sprt(np.full(30, -1.0), 1.0, 2.0, t)
        self.assertEqual(z['status'], 'H0')
        self.assertEqual(z['had'], [round(math.log(0.1 / (1 - pg.SPRT_ALFA)), 2), round(math.log(0.9 / pg.SPRT_ALFA), 2)])
        w = pg.sprt(np.full(12, 0.5), 0.5, 20.0)                                            # hingar besar: belum cukup
        self.assertEqual(w['status'], 'TERUSKAN')
        v = pg.sprt(np.full(12, 3.0), -0.2, 2.0)
        self.assertEqual((v['status'], v['llr']), ('H0', None)); self.assertIn('tiada H1', v['nota'])
        self.assertEqual(pg.sprt([], None, None)['status'], 'H0')
        # teguh (winsor): squeeze +100% dihad pada hi, jadi satu kohort tidak memutuskan H1
        wz = dict(lo=-5.0, hi=5.0, h0=-0.3, h1=0.2, sd=2.0)
        u = pg.sprt([100.0, 0.0], 0.4, 30.0, None, wz)
        self.assertEqual(u['skala'], 'winsor')
        self.assertAlmostEqual(u['llr'], (0.5 * (5.0 + 0.05) + 0.5 * (0.0 + 0.05)) / 4.0, places=3)
        self.assertEqual(pg.sprt([1.0], 0.4, 3.0, None, dict(wz, h1=-0.4))['skala'], 'mentah')   # h1 <= h0: sandaran mentah

    def test_kredit_autotune_sahaja(self):
        self.assertEqual(pg.kekal(True), 0.5); self.assertEqual(pg.kekal(False), 0.25); self.assertEqual(pg.kekal(None), 0.25)
        self.assertTrue(pg.kredit_at(dict(label='SEDERHANA'))); self.assertTrue(pg.kredit_at(dict(label='TINGGI')))
        self.assertFalse(pg.kredit_at(dict(label='RENDAH', cagr_a=0.3, spy_a=0.1, cagr_b=0.3, spy_b=0.1)))   # MDD gagal: label RENDAH
        self.assertFalse(pg.kredit_at(None))
        reg, wfo = dict(subset_menang=4, subset_n=4), dict(cagr=0.9, ew=0.3)
        s = pg.semakan(reg, wfo, dict(label='GAGAL'))
        self.assertEqual(s[:2], (True, True))
        self.assertEqual(pg.kekal(pg.kredit_at(dict(label='GAGAL'))), 0.25)                 # S1–S4 + WFO lulus: tiada kredit

    def test_pisah_backfill(self):
        C = pos([['M01', 'A', '2026-10-07', '2026-10-08', '', False, 1.0, 1.0, 'C'],
                 ['M01', 'B', '2026-10-12', '2026-10-13', '', False, 1.0, 1.0, 'C'],
                 ['M01', 'C', '2026-10-13', '2026-10-14', '', False, 1.0, 1.0, 'C'],
                 ['M01', 'D', '2026-10-14', '2026-10-15', '', False, 1.0, 1.0, 'C']])
        b, f = pg.pisah_backfill(C)
        self.assertEqual((list(b.saham), list(f.saham)), (['C', 'D'], ['A', 'B']))
        C['kohort'] = ['', '', 'backfill', 'hadapan']
        b, f = pg.pisah_backfill(C)
        self.assertEqual(list(b.saham), ['D'])                                               # label kohort juga dihormati

    def test_umur_tetap(self):
        e = self.ew(); t = list(e.index)
        P = pd.DataFrame([dict(id='M01', saham='A', tarikh_isyarat=t[0], tarikh_beli=t[1], tarikh_keluar='', tutup1=False, hasil1=0.0,
                               hasil2=0.0, sumber='lejar', buka_keluar=False, hb=10.0, kohort='lejar'),
                          dict(id='M01', saham='B', tarikh_isyarat=t[0], tarikh_beli=t[1], tarikh_keluar=t[2], tutup1=True, hasil1=-3.0,
                               hasil2=-3.0, sumber='lejar', buka_keluar=False, hb=10.0, kohort='lejar'),
                          dict(id='M01', saham='A', tarikh_isyarat=t[3], tarikh_beli=t[4], tarikh_keluar='', tutup1=False, hasil1=0.0,
                               hasil2=0.0, sumber='lejar', buka_keluar=False, hb=10.0, kohort='lejar')])
        tutup = {('A', t[6]): 11.0}
        X = pg.tambah_umur_tetap(P, e, tutup, t, t[7], ks=(5,))
        self.assertAlmostEqual(X.x5.iloc[0], pg.bersih(10.0) - 100 * pg.ew_tempoh(e, [t[1]], [t[6]])[0])   # tutup sesi beli + 5
        self.assertAlmostEqual(X.x5.iloc[1], -3.0 - 100 * pg.ew_tempoh(e, [t[1]], [t[2]])[0])              # keluar lebih awal
        self.assertTrue(np.isnan(X.x5.iloc[2]))                                              # umur belum cukup (t9 > kini)

    def test_pintu_dan_corong(self):
        r = dict(id='M05', at_label='SEDERHANA', h_hari_beli=45, h_z_terlaras=3.4, h_lebihan=0.8)
        p, n, k = pg.pintu_kaedah(r, [], {'M05': {}}, None, (130, 0.12), None)
        self.assertEqual(p, dict(A=True, B=True, C=True, D=True, E=None, F=False))
        self.assertEqual(n, 4)                                                               # E tiada: berhenti pada E
        self.assertTrue(any(x.startswith('E: tiada portfolio') for x in k)); self.assertTrue(any(x.startswith('F:') for x in k))
        p, n, k = pg.pintu_kaedah(r, ['HAMPIR_PENDUA:M03'], None, None, (130, 0.05), None)
        self.assertEqual((p['A'], p['B'], p['D'], n), (False, False, False, 0))              # pendua tidak boleh lulus B
        self.assertTrue(any('HAMPIR_PENDUA:M03 tidak boleh lulus' in x for x in k))
        self.assertTrue(any('tiada pra_daftar.json' in x for x in k))
        p, _, _ = pg.pintu_kaedah(dict(r, at_label='RENDAH'), [], None, {'M05': {'lulus_B': True}}, (0, None), None)
        self.assertTrue(p['B'])                                                              # ujian PIT lulus_B
        p, _, _ = pg.pintu_kaedah(dict(r, h_z_terlaras=2.9), [], None, None, (0, None), None)
        self.assertFalse(p['C'])
        sl = dict(portfolio='TOP1_10', sesi=130, pulangan=9.0, kawalan_pulangan=5.0, spy=6.0, ew=8.0)
        self.assertTrue(pg.pintu_kaedah(r, [], None, None, (0, None), sl)[0]['E'])
        self.assertFalse(pg.pintu_kaedah(r, [], None, None, (0, None), dict(sl, sesi=2))[0]['E'])
        self.assertFalse(pg.pintu_kaedah(r, [], None, None, (0, None), dict(sl, ew=10.0))[0]['E'])
        rows = [dict(swing=True, bendera=[], pintu=dict(A=False, B=True, C=False, D=False, E=None, F=False)),
                dict(swing=True, bendera=['DITOLAK'], pintu=dict(A=False, B=True, C=True, D=False, E=None, F=False)),
                dict(swing=False, bendera=[], pintu=dict(A=True, B=True, C=True, D=True, E=True, F=False)),
                dict(swing=True, bendera=['CIRI:PANTULAN'], pintu=dict(A=False, B=False, C=False, D=False, E=None, F=False))]
        self.assertEqual([x['n'] for x in pg.corong(rows)], [4, 3, 2, 1, 0, 0, 0])
        self.assertEqual([x['peringkat'] for x in pg.corong(rows)], pg.CORONG)

    def test_pendua_dan_ciri(self):
        with tempfile.TemporaryDirectory() as d:
            A = [(f'S{i}', '2026-10-20') for i in range(30)]
            rows = [dict(tarikh_data=t, kaedah='M02', saham=s) for s, t in A[:25] + [('X1', '2026-10-21')] * 1]   # 25/26 dalam M01
            rows += [dict(tarikh_data=t, kaedah='M01', saham=s) for s, t in A]
            rows += [dict(tarikh_data=t, kaedah='M03', saham=s) for s, t in A]                                 # sama dengan M01
            rows += [dict(tarikh_data='2026-10-20', kaedah='M04', saham=s) for s in ('S1', 'S2')]              # < 20 isyarat
            pd.DataFrame(rows).to_csv(os.path.join(d, '2026-10-20_malam.csv.gz'), index=False)
            x = pg.pendua_isyarat(d, ['M01', 'M02', 'M03', 'M04'])
            self.assertEqual(set(x), {'M02', 'M03'})
            self.assertEqual(x['M03'][0], 'M01')                                                # sama besar: lebih awal = induk
            self.assertEqual(x['M02'][0], 'M01'); self.assertAlmostEqual(x['M02'][1], 25 / 26)
        self.assertEqual(pg.kelas_ciri(dict(jenis='pantulan', tinggi52=True, rs=True, volum=True, ketat=True, adr=False, rejim=False)), 'PANTULAN')
        self.assertEqual(pg.kelas_ciri(dict(jenis='momentum', tinggi52=True, rs=False, volum=True, ketat=True, adr=False, rejim=False)), 'MOMENTUM_PRO')
        self.assertEqual(pg.kelas_ciri(dict(jenis='momentum', tinggi52=False, rs=False, volum=True, ketat=True, adr=False, rejim=True)), 'PENUNJUK')
        self.assertIsNone(pg.kelas_ciri(None))
        c = pg.ciri_kaedah()
        self.assertGreater(len(c), 100); self.assertIn(c['M01']['jenis'], ('momentum', 'pantulan'))

    def test_bendera_tarikh_dikekal(self):
        with tempfile.TemporaryDirectory() as d:
            f = os.path.join(d, 'b.csv')
            b = [dict(id='M81', bendera='ARTIFAK', sebab='x', sumber='y'), dict(id='M02', bendera='DITOLAK', sebab='x', sumber='y')]
            pg.tulis_bendera(b, '2026-10-23', f)
            x = pg.tulis_bendera(b + [dict(id='M09', bendera='HAMPIR_PENDUA:M01', sebab='x', sumber='y')], '2026-10-30', f)
            self.assertEqual(dict(zip(x.id, x.tarikh)), {'M81': '2026-10-23', 'M02': '2026-10-23', 'M09': '2026-10-30'})
            self.assertEqual(list(x.columns), ['id', 'bendera', 'sebab', 'sumber', 'tarikh'])

    def test_sejarah_dan_ramalan(self):
        with tempfile.TemporaryDirectory() as d:
            f = os.path.join(d, 's.csv')
            ids = [f'M{i:02d}' for i in range(1, 7)]
            pg.tulis_sejarah([dict(id=i, skor=0.0) for i in ids], '2026-10-23', f)
            s = pg.tulis_sejarah([dict(id=i, skor=float(k)) for k, i in enumerate(ids)], '2026-10-23', f)   # larian semula: ganti
            self.assertEqual(len(s), 6); self.assertEqual(list(s.skor), [0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
            H = pd.DataFrame(dict(id=ids, tarikh_beli='2026-10-27', x5=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6]))
            self.assertIsNone(pg.ramalan(s, H, ids))                                          # < 2 minggu sejarah
            s = pg.tulis_sejarah([dict(id=i, skor=float(k)) for k, i in enumerate(ids)], '2026-10-30', f)
            r = pg.ramalan(s, H, ids)
            self.assertEqual((r['spearman'], r['n_minggu']), (1.0, 1))                       # skor 23 Okt lawan belian minggu 27 Okt
            self.assertEqual(r['pasangan'][0]['minggu_hadapan'], '2026-W44')
            self.assertEqual(pg.ramalan(s, H.assign(x5=np.nan), ids)['n_minggu'], 0)

    def test_ringkas_hadapan_lebihan(self):
        hari = list(pd.bdate_range('2026-10-01', periods=12).strftime('%Y-%m-%d'))
        P = pd.DataFrame([dict(id='M01', saham=f'S{i % 4}', tarikh_isyarat=h, tarikh_beli=h, tarikh_keluar='', tutup1=False,
                               hasil1=2.0 + i % 3, hasil2=2.0, sumber='lejar', lebihan=0.5 + (i % 3), x5=0.25)
                          for i, h in enumerate(hari * 2)])
        h = pg.ringkas_hadapan(P, 5, '2026-12-31')
        self.assertEqual(h['matang'], 24); self.assertAlmostEqual(h['lebihan'], float(P.lebihan.mean()))
        self.assertEqual(h['g_saham'], 4); self.assertAlmostEqual(h['r5'], 0.25); self.assertEqual(h['n_r5'], 24)
        self.assertAlmostEqual(h['lebihan_saham'], float(P.groupby('saham').lebihan.mean().mean()))
        self.assertEqual(len(h['kohort_lebihan']), 12)
        self.assertGreater(h['z'], 0); self.assertLess(h['p'], 0.5)


class TestKalibrasiLebihan(unittest.TestCase):
    def test_ew_tempoh_dagangan(self):
        import kalibrasi_skor as K
        ix = pd.bdate_range('2020-01-06', periods=6)
        fr = {'A': pd.DataFrame(dict(open=[10, 11, 12, 13, 14, 15.0], close=[10.5, 11.5, 12.5, 13.5, 14.5, 15.5]), index=ix),
              'B': pd.DataFrame(dict(open=[20, 20, 20, 20, 20, 20.0], close=[20, 20, 20, 20, 20, 20.0]), index=ix)}
        ew = K.ew_harian(fr)
        self.assertAlmostEqual(ew.oc.iloc[0], (0.05 + 0.0) / 2)
        x_buka = 13 / 11 * (1 - K.COST) / (1 + K.COST) - 1          # keluar pada buka hari ke-3
        x_tutup = 13.5 / 11 * (1 - K.COST) / (1 + K.COST) - 1       # keluar pada tutup hari ke-3
        T = pd.DataFrame(dict(ticker=['A', 'A'], ent=[ix[1], ix[1]], ex=[ix[3], ix[3]], ret=[x_buka, x_tutup]))
        R = K.ew_tempoh_dagangan(T, fr, ew)
        a = 0.5 * (13 / 12.5 - 1)                                      # buka t3 / tutup t2, B rata
        oc1, cc2 = 0.5 * (11.5 / 11 - 1), 0.5 * (12.5 / 11.5 - 1)
        self.assertAlmostEqual(R.iloc[0], (1 + oc1) * (1 + cc2) * (1 + a) - 1)
        self.assertAlmostEqual(R.iloc[1], (1 + oc1) * (1 + cc2) * (1 + 0.5 * (13.5 / 12.5 - 1)) - 1)
        lb = K.lebihan(T, fr, ew)
        self.assertAlmostEqual(lb['lebihan_rawak'], float(np.mean((T.ret.values - R.values) * 100)))
        self.assertEqual(lb['lebihan_n'], 2); self.assertEqual(lb['lebihan_kohort_n'], 1)

    def test_sprt_winsor(self):
        import kalibrasi_skor as K
        c = np.random.default_rng(5).normal(0.4, 3.0, 300); c[:5] = 80.0                  # ekor squeeze
        w = K.sprt_winsor(c)
        self.assertEqual(set(w), {'lebihan_winsor', 'lebihan_sd_winsor', 'lebihan_h0_winsor', 'lebihan_h1_winsor'})
        self.assertGreater(w['lebihan_h1_winsor']['0.5'], w['lebihan_h1_winsor']['0.25'])
        self.assertGreater(w['lebihan_h1_winsor']['0.25'], w['lebihan_h0_winsor'])
        self.assertLess(w['lebihan_sd_winsor'], float(np.std(c)))
        self.assertEqual(K.sprt_winsor(c[:10]), {})

    def test_fail_kalibrasi_lebihan(self):
        d = json.load(open(pg.KALIBRASI, encoding='utf-8'))
        self.assertEqual(d['lebihan']['kos_pusingan'], 0.2)
        ada = [m for m, r in d['kaedah'].items() if 'lebihan_rawak' in r]
        self.assertGreaterEqual(len(ada), len(d['kaedah']) - len(d['lebihan'].get('gagal') or {}))


class TestJanaDbPapanDibahagi(unittest.TestCase):
    """jana_db.py (bahagian analisis/papan sahaja, 25 Okt 2026): papan.json > HAD_BAHAGI dibahagi seperti watchlist; setiap
    bahagian < had db dan gabungan baris = papan penuh (halaman: subBhg)."""

    def test_papan_dibahagi(self):
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        import io
        from contextlib import redirect_stdout
        import jana_db as jd
        from bahagi_db import bait, HAD_DB
        from test_audit_24okt import tulis_stor
        from test_sahkan import ASAS, tulis
        papan = json.load(open(os.path.join(pg.BS2, 'data', 'analisis', 'papan.json'), encoding='utf-8'))
        with tempfile.TemporaryDirectory() as d:
            pt, stor, kel = (os.path.join(d, x) for x in ('pt', 'stor', 'db'))
            os.makedirs(pt); os.makedirs(stor)
            tulis_stor(stor, [('AAA', 20261013, 100, 106, 99, 105, 1000), ('AAA', 20261014, 105, 107, 104, 106, 1000)])
            tulis_stor(stor, [('SPY', 20261013, 600, 601, 599, 600, 1), ('SPY', 20261014, 600, 601, 599, 600, 1)], 'harga_idx.csv')
            tulis(pt, 'moomoo.csv', [dict(ASAS, saham='MMM')])
            tulis(pt, 'claude.csv', [dict(ASAS, kaedah='M03', id_kaedah='M03', harga_terkini='106', untung_pct='6.0', hari='1')])
            tulis(pt, 'watchlist.csv', [{'Saham': 'BBB', 'Kaedah': 'M02', 'Sektor': 'Energy', 'Industri': 'Oil', '% hampir': '100.0',
                                         'Jarak %': '0.0', 'Syarat belum cukup': 'Tutup esok > 20', 'tarikh_data': '2026-10-14'}])
            with redirect_stdout(io.StringIO()):
                jd.main(['--keluar', kel, '--folder', pt, '--stor', stor, '--masa', '2026-10-15 06:30', '--sumber', 'ujian'])
            asas = json.load(open(os.path.join(kel, 'analisis', 'papan.json'), encoding='utf-8'))
            st = json.load(open(os.path.join(kel, 'harian', 'status.json'), encoding='utf-8'))
            if bait(papan) <= jd.HAD_BAHAGI:
                self.assertNotIn('bahagian', asas); return
            b = asas['bahagian']; rows = list(asas['rows'])
            self.assertGreaterEqual(b['n'], 2)
            for k in range(2, b['n'] + 1):
                x = json.load(open(os.path.join(kel, 'analisis', f'papan_{k}.json'), encoding='utf-8'))
                self.assertEqual((x['induk'], x['bahagian']), (b['id'], k)); self.assertLess(bait(x), HAD_DB)
                rows += x['rows']
            self.assertLess(bait(asas), HAD_DB)
            self.assertEqual([r['id'] for r in rows], [r['id'] for r in papan['rows']])
            self.assertEqual(asas['corong'], papan['corong'])                     # meta penuh dalam dokumen asas
            self.assertEqual(st['saluran']['analisis'], papan['harga_pada'])
            self.assertFalse([x for x in st['ralat'] if 'analisis/papan' in x])


if __name__ == '__main__':
    unittest.main()
