"""Ujian carian setup CS01 (`kajian/carian_setup/`, pradaftar `kajian/SPEC_CARIAN_SETUP.md`):
ruang carian dikunci, tiada pandang ke hadapan, mekanik dagangan SPEC §4 dan pengumpulan skor SPEC §6."""
import os
import sys
import unittest

import numpy as np
import pandas as pd

SINI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(SINI, '..', 'kajian', 'carian_setup'))
import cs_atom as atom  # noqa: E402
import cs_teras as teras  # noqa: E402

A1, A2, OP = teras.peraturan_keluar(len(atom.KELUAR))
NR = len(A1)
JENIS = np.zeros(len(atom.KELUAR), np.int64)
PAR = np.zeros(len(atom.KELUAR))
for _a, (_j, _v) in atom.LALUAN.items():
    JENIS[_a] = 1 if _j == 'chand' else 2
    PAR[_a] = _v


def _saham(n, benih):
    rng = np.random.default_rng(benih)
    c = 50 * np.exp(np.cumsum(rng.normal(0.0005, 0.02, n)))
    o = c * (1 + rng.normal(0, 0.005, n))
    h = np.maximum(o, c) * (1 + np.abs(rng.normal(0, 0.006, n)))
    l = np.minimum(o, c) * (1 - np.abs(rng.normal(0, 0.006, n)))
    ix = pd.bdate_range('2019-01-02', periods=n)
    return pd.DataFrame({'open': o, 'high': h, 'low': l, 'close': c, 'volume': rng.integers(2e5, 3e6, n).astype(float)},
                        index=ix)


def _peraturan(a, b=None, op=1):
    """Indeks peraturan keluar bagi atom a (tunggal) atau pasangan (a, b) dengan op 2 = ATAU, 3 = DAN."""
    for r in range(NR):
        if b is None and OP[r] == 1 and A1[r] == a:
            return r
        if b is not None and OP[r] == op and A1[r] == a and A2[r] == b:
            return r
    raise KeyError((a, b, op))


class TestKunci(unittest.TestCase):
    def test_ruang_carian_dikunci(self):
        self.assertEqual((len(atom.PENCETUS), len(atom.PENAPIS), len(atom.KELUAR), len(atom.HENTI)), (49, 30, 24, 4))
        self.assertEqual(NR, 1 + 24 + 2 * 276)
        self.assertEqual(teras.NH * NR, 2308)
        self.assertEqual((atom.TMAX, teras.TMAX, atom.KOS, teras.KOS), (20, 20, 0.005, 0.005))
        self.assertEqual(atom.TEMPOH['431'], (('Latih', 20200102, 20230630), ('Sah', 20230703, 20260828)))
        self.assertEqual(atom.TEMPOH['kunci'], (('K1', 20100104, 20191231), ('K2', 20200102, 20260828)))

    def test_tempoh_cs02_dikunci(self):
        # Pindaan 13 Nov 2026 (b): pemenang mesti untung dalam dua era; K3 tidak dipakai carian.
        self.assertEqual(atom.TEMPOH['A'], (('E1', 20100104, 20191231), ('E2', 20200102, 20241231)))
        self.assertEqual(atom.TEMPOH['B'], (('K1', 20100104, 20191231), ('K2', 20200102, 20241231),
                                            ('K3', 20250102, 20260828)))
        self.assertLess(atom.TEMPOH['A'][1][2], atom.TEMPOH['B'][2][1])


class TestTiadaPandangHadapan(unittest.TestCase):
    def test_bar_lama_tidak_berubah_bila_data_masa_depan_ditambah(self):
        g = _saham(700, 1)
        rs = pd.Series(np.random.default_rng(2).uniform(0, 100, 700), index=g.index)
        satu = pd.Series(1.0, index=g.index)
        penuh = atom.indikator(g, rs, satu, satu)
        pendek = atom.indikator(g.iloc[:560], rs.iloc[:560], satu.iloc[:560], satu.iloc[:560])
        for kump_p, kump_s in zip(penuh[:3], pendek[:3]):
            for nama in kump_p:
                self.assertTrue(np.array_equal(kump_p[nama][:560], kump_s[nama]), nama)
        self.assertTrue(np.allclose(penuh[3][:560], pendek[3], equal_nan=True))

    def test_mula_isyarat_tidak_merentas_saham(self):
        sig = np.array([1, 1, 0, 1, 1, 1, 0, 1], bool)
        self.assertEqual(atom.mula_isyarat(sig, np.array([0, 4, 8])).tolist(),
                         [True, False, False, True, True, False, False, True])


class TestMekanik(unittest.TestCase):
    def setUp(self):
        n = 40
        self.o = np.full(n, 100.0)
        self.h = np.full(n, 101.0)
        self.l = np.full(n, 99.0)
        self.c = np.full(n, 100.0)
        self.atr = np.full(n, 2.0)
        self.X = np.zeros((len(atom.KELUAR), n), np.uint8)

    def jalan(self, s, r, i=5):
        R, hp, sk = teras.hasil_satu(np.array([i]), self.o, self.h, self.l, self.c, self.atr, self.X, JENIS, PAR,
                                     A1, A2, OP, s, r)
        return R[0], hp[0], sk[0]

    def test_tiada_keluar_jual_tutup_sesi_20(self):
        self.c[6 + 19] = 110.0
        self.h[6 + 19] = 111.0
        R, hp, _ = self.jalan(0, 0)
        self.assertAlmostEqual(R, 0.10 - 0.005)
        self.assertEqual(hp, 20)

    def test_keluar_indikator_hari_beli_dijual_buka_esok_bukan_hari_sama(self):
        self.X[0, 6] = 1                       # X01 benar pada tutup hari beli
        self.o[7] = 103.0
        R, hp, sk = self.jalan(0, _peraturan(0))
        self.assertAlmostEqual(R, 0.03 - 0.005)
        self.assertEqual((hp, sk), (1, 1))

    def test_henti_tidak_aktif_intrahari_pada_hari_beli(self):
        self.l[6] = 80.0                       # rendah hari beli jauh di bawah henti, tutup kekal 100
        R, hp, _ = self.jalan(0, 0)
        self.assertAlmostEqual(R, -0.005)
        self.assertEqual(hp, 20)

    def test_tutup_hari_beli_bawah_henti_jual_buka_esok(self):
        self.c[6] = 90.0
        self.l[6] = 89.0
        self.o[7] = 91.0
        R, hp, _ = self.jalan(0, 0)
        self.assertAlmostEqual(R, -0.09 - 0.005)
        self.assertEqual(hp, 1)

    def test_henti_intrahari_sesi_kedua_pada_paras(self):
        self.l[7] = 91.0                       # H1 = 92
        R, hp, _ = self.jalan(0, 0)
        self.assertAlmostEqual(R, -0.08 - 0.005)
        self.assertEqual(hp, 2)

    def test_jurang_bawah_henti_jual_pada_buka(self):
        self.o[8] = 85.0
        self.l[8] = 84.0
        R, hp, _ = self.jalan(1, 0)            # H2 = 90
        self.assertAlmostEqual(R, -0.15 - 0.005)
        self.assertEqual(hp, 3)

    def test_henti_atr(self):
        self.l[7] = 93.5                       # H3 = 100 - 3 x 2 = 94; H4 = 92
        self.assertAlmostEqual(self.jalan(2, 0)[0], -0.06 - 0.005)
        self.assertAlmostEqual(self.jalan(3, 0)[0], -0.005)

    def test_pasangan_atau_dan(self):
        self.X[0, 8] = 1                       # X01 pada sesi 2
        self.X[1, 10] = 1                      # X02 pada sesi 4
        self.X[0, 10] = 1
        self.o[9], self.o[11] = 104.0, 107.0
        self.assertEqual(self.jalan(0, _peraturan(0, 1, 2))[1], 3)      # ATAU: sesi 2 -> jual buka sesi 3
        self.assertAlmostEqual(self.jalan(0, _peraturan(0, 1, 2))[0], 0.04 - 0.005)
        self.assertEqual(self.jalan(0, _peraturan(0, 1, 3))[1], 5)      # DAN: sesi 4 -> jual buka sesi 5
        self.assertAlmostEqual(self.jalan(0, _peraturan(0, 1, 3))[0], 0.07 - 0.005)

    def test_chandelier_ikut_tutup_tertinggi_sejak_beli(self):
        self.c[6:12] = [100, 105, 110, 115, 108.5, 108.5]               # X18: 115 - 3 x 2 = 109 > 108.5 pada sesi 4
        self.h[6:12] = 116
        self.o[11] = 108.0
        R, hp, _ = self.jalan(1, _peraturan(17))
        self.assertAlmostEqual(R, 0.08 - 0.005)
        self.assertEqual(hp, 5)

    def test_satu_posisi_setiap_saham(self):
        ev = np.array([5, 8, 30, 31, 45])
        sk = np.array([19, 19, 3, 3, 3])
        tid = np.zeros(60, np.int32)
        tid[40:] = 1
        self.assertEqual(teras.satu_posisi(ev, sk, tid).tolist(), [True, False, True, False, True])

    def test_pilih_slot_had_slot_dan_saham_sedang_dipegang(self):
        # dua saham (tid 0: bar 0-59, tid 1: bar 60-119), hari = indeks bar dalam saham
        tid = np.repeat([0, 1], 60).astype(np.int32)
        hari = np.tile(np.arange(60), 2)
        ev = np.array([5, 8, 65, 30, 95])          # saham0 hari5, saham0 hari8, saham1 hari5, saham0 hari30, saham1 hari35
        sk = np.array([10, 3, 10, 3, 3])
        susun = np.lexsort((np.arange(5), hari[ev + 1]))
        satu = teras.pilih_slot(ev, sk, tid, hari, susun, 1)
        self.assertEqual(satu.tolist(), [True, False, False, True, True])    # 1 slot: isyarat serentak ditolak
        dua = teras.pilih_slot(ev, sk, tid, hari, susun, 2)
        self.assertEqual(dua.tolist(), [True, False, True, True, True])      # saham sedang dipegang tidak dibeli lagi

    def test_jumlah_harian_dibahagi_slot(self):
        self.c[6:9] = [102, 104, 106]
        ev = np.array([5])
        R, hp, sk = teras.hasil_satu(ev, self.o, self.h, self.l, self.c, self.atr, self.X, JENIS, PAR, A1, A2, OP, 0, 0)
        jum, bil = teras.jumlah_harian(ev, R, sk, self.o, self.c, np.arange(40), 40)
        self.assertEqual(int(bil.sum()), 20)
        self.assertAlmostEqual(float(jum.sum()), float(np.log1p(R[0])), delta=0.01)

    def test_buku_harian_menyamai_pulangan_dagangan(self):
        self.c[6:9] = [102, 104, 106]
        self.X[0, 8] = 1
        self.o[9] = 105.0
        ev = np.array([5])
        R, hp, sk = teras.hasil_satu(ev, self.o, self.h, self.l, self.c, self.atr, self.X, JENIS, PAR, A1, A2, OP, 0,
                                     _peraturan(0))
        bk = teras.buku_harian(ev, R, sk, hp, self.o, self.c, np.arange(40), 40)
        self.assertEqual(np.count_nonzero(bk), 4)
        self.assertAlmostEqual(float(np.prod(1 + bk) - 1), R[0], delta=5e-4)   # kos dibahagi dua hari, dikompaun


class TestLabelTangkap(unittest.TestCase):
    """SPEC pindaan (d): label kadar tangkap."""

    def setUp(self):
        import cs_tangkap
        self.label = cs_tangkap.label
        self.o = np.full(40, 100.0)
        self.l = np.full(40, 99.0)
        self.c = np.full(40, 100.0)

    def jalan(self):
        return self.label(np.array([5]), self.o, self.l, self.c)[0].tolist()

    def test_lari_naik_minggu_pertama_capai_10_dan_kekal(self):
        self.c[6:26] = np.linspace(102, 125, 20)          # sesi 5 = 106.8, sesi 20 = 125
        self.assertEqual(self.jalan(), [1, 1, 1, 0, 1])

    def test_henti_dahulu_bermakna_gagal_walaupun_naik_kemudian(self):
        self.l[8] = 91.0                                  # henti -8 % pada sesi 3
        self.c[12:26] = 130.0
        m5, t10, t20, gagal, lari = self.jalan()
        self.assertEqual((t10, t20, gagal, lari), (0, 0, 1, 0))

    def test_capai_10_tetapi_jatuh_semula_bukan_lari(self):
        self.c[6:12] = [103, 106, 108, 110, 112, 111]     # m5 dan t10 benar
        self.c[25] = 104.0                                # tutup sesi 20 di bawah +10 %
        self.assertEqual(self.jalan(), [1, 1, 0, 0, 0])


class TestHadapan(unittest.TestCase):
    """SPEC pindaan (f): penjejak hadapan mesti memakai mekanik yang sama dengan backtest."""

    def setUp(self):
        import cs_hadapan
        self.H = cs_hadapan
        rng = np.random.default_rng(7)
        n = 400
        c = 50 * np.exp(np.cumsum(rng.normal(0, 0.03, n)))
        o = c * (1 + rng.normal(0, 0.01, n))
        self.pan = {'o': o, 'h': np.maximum(o, c) * 1.01, 'l': np.minimum(o, c) * (1 - np.abs(rng.normal(0, 0.02, n))),
                    'c': c, 'atr': 0.03 * c, 'X': (rng.random((len(atom.KELUAR), n)) < 0.15).astype(np.uint8),
                    'mula': np.array([0, n]), 'tid': np.zeros(n, np.int32)}

    def test_simulasi_menyamai_teras_bagi_tetingkap_lengkap(self):
        p = self.pan
        ev = np.arange(30, 360)
        for s, r in [(0, 0), (1, 5), (2, 18), (3, 19), (0, 20), (1, 300), (2, 400), (3, NR - 1)]:
            R, hp, sk = teras.hasil_satu(ev, p['o'], p['h'], p['l'], p['c'], p['atr'], p['X'], JENIS, PAR, A1, A2, OP, s, r)
            for k, i in enumerate(ev):
                x = self.H.simulasi(p, int(i), s, r)
                self.assertEqual(x['status'], 'TUTUP')
                self.assertAlmostEqual(x['R'], R[k], places=10, msg=(s, r, i))
                self.assertEqual((x['sesi'], x['bar_keluar']), (hp[k], i + 1 + sk[k]), (s, r, i))

    def test_status_tetingkap_belum_lengkap(self):
        p = dict(self.pan)
        p['X'] = np.zeros_like(p['X'])
        p['l'] = p['c'] * 0.999                                        # tiada henti
        p['o'] = p['c'].copy()
        n = len(p['c'])
        self.assertEqual(self.H.simulasi(p, n - 1, 0, 0)['status'], 'TUNGGU_BELI')
        p['c'] = np.linspace(50, 60, n)                                # naik perlahan: tiada henti tutup hari beli
        p['o'] = p['c'].copy()
        p['l'] = p['c'] * 0.999
        x = self.H.simulasi(p, n - 4, 0, 0)
        self.assertEqual((x['status'], x['sesi']), ('TERBUKA', 3))
        p['X'][0, n - 1] = 1                                           # isyarat keluar pada bar terakhir
        self.assertEqual(self.H.simulasi(p, n - 4, 0, _peraturan(0))['status'], 'JUAL_ESOK')

    def test_takrif_boleh_dibaca_semula(self):
        import cs_cari
        self.assertEqual(self.H.dari_takrif('M84.t7|F23@5+F26|H2|X11 ATAU X21'),
                         {'pencetus': 'M84.t7', 'fs': [22, 25], 'amb': [5.0, None],
                          'lajur': 1 * cs_cari.NR + _peraturan(10, 20, 2)})
        self.assertEqual(self.H.dari_takrif('N73|F16+F23|H4|X07 DAN X21')['lajur'], 3 * cs_cari.NR + _peraturan(6, 20, 3))
        self.assertEqual(self.H.dari_takrif('P13|-|H1|X00'), {'pencetus': 'P13', 'fs': [-1, -1], 'amb': [None, None], 'lajur': 0})


class TestKumpul(unittest.TestCase):
    def test_skor_menyamai_kiraan_terus(self):
        rng = np.random.default_rng(3)
        n, K = 900, 12
        Rm = rng.normal(0.01, 0.08, (n, K)).astype(np.float32)
        tp = rng.integers(0, 2, n)
        Fm = (rng.random((n, 3)) < 0.6).astype(np.uint8)
        f1 = np.array([-1, 0, 0, 2], np.int64)
        f2 = np.array([-1, -1, 1, -1], np.int64)
        S = np.zeros((4, 2, K))
        Q = np.zeros((4, 2, K))
        N2 = np.zeros((4, 2), np.int64)
        teras.kumpul_tambah(Rm[:500], tp[:500], Fm[:500], f1, f2, S, Q, N2)
        teras.kumpul_tambah(Rm[500:], tp[500:], Fm[500:], f1, f2, S, Q, N2)
        tepi = np.round(np.arange(-0.10, 0.1001, 0.001), 4)
        idx, st, stw, hist = teras.kumpul_skor(S, Q, N2, np.array([0, 1, 2, 3]), 50, 3, tepi)
        for ci in range(4):
            m = np.ones(n, bool)
            for f in (f1[ci], f2[ci]):
                if f >= 0:
                    m &= Fm[:, f] > 0
            skor = np.full(K, np.inf)
            for p in (0, 1):
                x = Rm[m & (tp == p)].astype(float)
                self.assertEqual(N2[ci, p], len(x))
                skor = np.minimum(skor, x.mean(0) - 2 * x.std(0) / np.sqrt(len(x)))
            self.assertEqual(idx[ci, 0], int(np.argmax(skor)))
            self.assertAlmostEqual(float(st[ci, 0, 0]), float(skor.max()), places=5)
            self.assertAlmostEqual(float(stw[ci, 0]), float(skor[ci]), places=5)
            self.assertEqual(int(hist[ci].sum()), K)

    def test_gabungan_kurang_n_min_tidak_diskor(self):
        S = np.zeros((1, 2, 4))
        Q = np.zeros((1, 2, 4))
        N2 = np.array([[120, 99]])
        idx, _, _, hist = teras.kumpul_skor(S, Q, N2, np.array([0]), 100, 2, np.array([0.0]))
        self.assertEqual(idx[0].tolist(), [-1, -1])
        self.assertEqual(int(hist.sum()), 0)


class TestRingkas(unittest.TestCase):
    """cs_ringkas: pecahan prasyarat/syarat dan nama pendek (tiada pengiraan baharu)."""

    def test_bahagi(self):
        import cs_ringkas
        self.assertEqual(cs_ringkas.bahagi('F20 >= 30% di bawah puncak 52 minggu DAN F27 rejim QQQ OFF'),
                         ('QQQ OFF', '>= 30% di bawah puncak 52 minggu'))
        self.assertEqual(cs_ringkas.bahagi('F17 RS >= 90 DAN F28 SPY > SMA200'), ('SPY > SMA200', 'RS >= 90'))
        self.assertEqual(cs_ringkas.bahagi('RS >= 95 DAN ATR% >= 4'), ('–', 'RS >= 95 + ATR% >= 4'))
        self.assertEqual(cs_ringkas.bahagi(float('nan')), ('–', '–'))

    def test_pasaran_sepadan_ruang_carian(self):
        import cs_ringkas
        # Tiga penapis peringkat pasaran dalam ruang carian (cs_atom.PENAPIS indeks 25-27).
        for kod, nama in cs_ringkas.PASARAN.items():
            i = int(kod[1:]) - 1
            self.assertIn(i, (25, 26, 27))
            self.assertTrue(str(atom.PENAPIS[i]).startswith(kod + ' '))
            self.assertIn(nama, str(atom.PENAPIS[i]))

    def test_nama_pendek(self):
        import cs_ringkas
        self.assertEqual(cs_ringkas.nama_pendek('M92 CCI-50 (benih M, varian 2: cci_50=91, rma_atr_14=15)'), 'M92 CCI-50 (ditala 2)')
        self.assertEqual(cs_ringkas.nama_pendek('N40 OBV tinggi baharu + MA50 (benih N)'), 'N40 OBV tinggi baharu + MA50')

    def test_registry_semua_dipecah(self):
        import cs_ringkas
        t = cs_ringkas.pembahagian()
        self.assertEqual(t.id.tolist()[:3], ['F01', 'F02', 'F03'])
        self.assertTrue(set(t.prasyarat_pasaran) <= {'–', 'QQQ ON', 'QQQ OFF', 'SPY > SMA200'})
        self.assertEqual(int((t.jejak_hadapan == 'ya').sum()), 8)


if __name__ == '__main__':
    unittest.main()
