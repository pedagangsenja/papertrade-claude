# Ujian semakan sumber (24 Okt 2026): lapisan 1 dalam standard/sahkan.py (ambil alih, bar sesi terakhir, lorong 2 dikira semula
# secara bebas, untung_akhir_pct, --json) dan lapisan 3 standard/sampel_semak.py (pilih / banding lawan kline Moomoo).
import csv, io, json, os, sys, tempfile, unittest
from contextlib import redirect_stderr, redirect_stdout

import numpy as np
import pandas as pd

UJI = os.path.dirname(os.path.abspath(__file__))
BS2 = os.path.dirname(UJI)
for p in (os.path.join(BS2, 'standard'), os.path.join(BS2, 'kod'), UJI):
    sys.path.insert(0, p)
import sahkan as SH  # noqa: E402
import keluar_lorong as KL  # noqa: E402
import sampel_semak as SS  # noqa: E402
from test_sahkan import ASAS  # noqa: E402

LAJUR_L2 = ['keluar_henti', 'tarikh_keluar_henti', 'harga_keluar_henti', 'untung_henti_pct', 'status_henti', 'tutup_semua']
LAJUR = list(ASAS) + ['henti', 'tidak_dibeli', 'tidak_sah', 'sebab_tidak_sah', 'nota'] + LAJUR_L2


def tulis_csv(d, nama, rows):
    with open(os.path.join(d, nama), 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=LAJUR, extrasaction='ignore')
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, '') for k in LAJUR})


def siri(tutup, mula='2026-08-03'):
    """Bar harian ujian: buka = tutup semalam, tinggi/rendah = tutup ± 1."""
    c = np.array(tutup, float); o = np.r_[c[0], c[:-1]]
    ix = [str(x.date()) for x in pd.bdate_range(mula, periods=len(c))]
    return ix, o, c + 1, c - 1, c


def tulis_stor(d, data, nama='harga_A.csv'):
    with open(os.path.join(d, nama), 'w') as f:
        f.write('ticker,date,open,high,low,close,volume\n')
        for t, (ix, o, h, l, c) in data.items():
            for i in range(len(ix)):
                f.write(f'{t},{ix[i].replace("-", "")},{o[i]:.6g},{h[i]:.6g},{l[i]:.6g},{c[i]:.6g},100000\n')


def baris(saham, ix, o, c, k, L2=None, **kw):
    hb = float(o[k]); ht = float(c[-1])
    r = dict(ASAS, saham=saham, tarikh_beli=ix[k], harga_beli=f'{hb:.6g}', harga_terkini=f'{ht:.6g}',
             untung_pct=f'{(ht / hb - 1) * 100:.2f}', keluar='False')
    if L2:
        r.update(L2); r['tutup_semua'] = 'False'
    r.update(kw)
    return r


def muat(p):
    with open(p, encoding='utf-8') as f:
        return json.load(f)


def jalan(*arg):
    out = io.StringIO()
    with redirect_stdout(out):
        kod = SH.main(list(arg))
    return kod, out.getvalue()


# naik ke 110 kemudian jatuh 3 setiap hari: dengan sejarah sebelum beli keluar ~bar 29; tanpa sejarah (ATR hanya pada bar
# ke-14 selepas beli, kes VIAV/LITE) keluar lewat ~bar 34
TUTUP = [100.0] * 20 + [102, 104, 106, 108, 110] + [110 - 3 * i for i in range(1, 16)]
K = 20


class UjiChandelierBebas(unittest.TestCase):
    def test_sama_dengan_keluar_lorong(self):
        rng = np.random.default_rng(7)
        for _ in range(200):
            n = int(rng.integers(20, 90))
            c = 50 * np.exp(np.cumsum(rng.normal(0, 0.03, n)))
            h = c * (1 + rng.uniform(0, 0.03, n)); l = c * (1 - rng.uniform(0, 0.03, n)); o = np.r_[c[0], c[:-1]]
            k = int(rng.integers(0, n - 1))
            a = KL.lorong_henti(o, h, l, c, k)
            jn, j, P, js = SH.chandelier(o, h, l, c, k, n - 1, KL.GANDA_ATR, KL.TEMPOH_ATR)
            self.assertEqual(jn, {'keluar': 'keluar', 'menunggu': 'menunggu', 'terbuka': 'pegang'}[a['jenis']])
            if jn != 'pegang':
                self.assertEqual(j, a['j'])

    def test_margin_bar_keputusan(self):
        c = np.array([100.0, 99.0, 98.0]); P = np.array([-np.inf, 99.5, 99.5])
        self.assertAlmostEqual(SH.margin_lorong(c, P, 1, None), 0.5 / 99)
        self.assertEqual(SH.margin_lorong(c, P, 0), float('inf'))


class UjiSahkanSumber(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(); self.d = self.tmp.name
        self.stor = os.path.join(self.d, 'stor'); os.makedirs(self.stor)
        self.aa = os.path.join(self.d, 'ambil_alih.csv')
        with open(self.aa, 'w') as f:
            f.write('saham,tarikh_umum,tarikh_tamat,pembeli,harga_tawaran,bayaran,sumber\n')
        tulis_csv(self.d, 'moomoo.csv', [dict(ASAS, saham='MMM', unit='', tidak_dibeli='True', harga_beli='', harga_terkini='',
                                              untung_pct='', isyarat_keluar='TIDAK DIBELI')])

    def tearDown(self):
        self.tmp.cleanup()

    def sahkan(self, *tambah):
        return jalan('--folder', self.d, '--stor', self.stor, '--ambil-alih', self.aa, '--lorong-n', '0', *tambah)

    # ---- lorong 2
    def test_lorong2_sama_dan_salah(self):
        ix, o, h, l, c = siri(TUTUP)
        penuh, _ = KL.nilai_baris(ix, o, h, l, c, ix[K], o[K])
        pendek, _ = KL.nilai_baris(ix[K:], o[K:], h[K:], l[K:], c[K:], ix[K], o[K])
        self.assertNotEqual(penuh['tarikh_keluar_henti'], pendek['tarikh_keluar_henti'])     # prasyarat fixture
        lama = dict(pendek, status_henti=pendek['status_henti'].replace(f' — {KL.TANDA_PENDEK}', ''))   # kod sebelum 24 Okt
        data = {t: (ix, o, h, l, c) for t in ('AAA', 'BBB', 'CCC')}
        tulis_stor(self.stor, data)
        tulis_csv(self.d, 'claude.csv', [baris('AAA', ix, o, c, K, penuh), baris('BBB', ix, o, c, K, lama),
                                         baris('CCC', ix, o, c, K, pendek)])
        kod, out = self.sahkan()
        self.assertEqual(kod, 1, out)
        self.assertIn('BBB', next(x for x in out.splitlines() if x.startswith('RALAT')))
        self.assertIn('lorong 2 CSV keluar', out)
        self.assertTrue(any(x.startswith('AMARAN') and 'CCC' in x and 'sejarah pendek' in x for x in out.splitlines()))
        self.assertFalse(any('AAA' in x for x in out.splitlines() if x.startswith(('RALAT', 'AMARAN'))))
        self.assertIn('sama 1, beza 1, sempadan 1', out)
        asal = SH.TOL_SEMPADAN
        SH.TOL_SEMPADAN = 0.5            # margin besar -> beza diturunkan ke AMARAN (beza vendor boleh menterbalikkan)
        try:
            self.assertEqual(self.sahkan()[0], 0)
        finally:
            SH.TOL_SEMPADAN = asal

    def test_lorong2_ketinggalan_dan_mendahului(self):
        ix, o, h, l, c = siri(TUTUP[:30])
        n = len(ix)
        semalam, _ = KL.nilai_baris(ix[:n - 1], o[:n - 1], h[:n - 1], l[:n - 1], c[:n - 1], ix[K], o[K])
        self.assertIn('menunggu', semalam['status_henti'])
        tulis_stor(self.stor, {'EEE': (ix, o, h, l, c), 'FFF': (ix[:n - 2], o[:n - 2], h[:n - 2], l[:n - 2], c[:n - 2])})
        r_e = baris('EEE', ix[:n - 1], o, c[:n - 1], K, semalam)       # CSV ketinggalan satu sesi: diterima
        r_f = baris('FFF', ix[:n - 2], o, c[:n - 2], K, semalam)       # CSV memakai bar selepas data repo: tidak disemak
        tulis_csv(self.d, 'claude.csv', [r_e, r_f])
        kod, out = self.sahkan()
        self.assertEqual(kod, 0, out)
        self.assertIn('sama 1, beza 0', out); self.assertIn('tidak disemak 1', out)

    def test_harga_keluar_henti(self):
        ix, o, h, l, c = siri(TUTUP)
        L2, _ = KL.nilai_baris(ix, o, h, l, c, ix[K], o[K])
        salah = float(L2['harga_keluar_henti']) * 1.02
        L2s = dict(L2, harga_keluar_henti=f'{salah:.4f}', untung_henti_pct=f'{(salah / o[K] - 1) * 100:.2f}')
        tulis_stor(self.stor, {'DDD': (ix, o, h, l, c)})
        tulis_csv(self.d, 'claude.csv', [baris('DDD', ix, o, c, K, L2s)])
        kod, out = self.sahkan()
        self.assertEqual(kod, 0, out)
        self.assertIn('harga_keluar_henti', out); self.assertIn('sampel_semak.py', out)
        with open(os.path.join(self.stor, 'buka_moomoo.csv'), 'w') as f:      # buka rasmi Moomoo disahkan = harga CSV
            f.write(f'ticker,date,open\nDDD,{L2["tarikh_keluar_henti"].replace("-", "")},{salah:.4f}\n')
        self.assertNotIn('harga_keluar_henti', self.sahkan()[1])

    def test_sampel_berketentuan(self):
        calon = [('claude.csv', i, dict(saham=f'S{i}', kaedah='M01', tarikh_beli='2026-10-01',
                                        status_henti='Keluar: tutup 1 bawah paras keluar 2' if i % 10 == 0 else 'Pegang (paras keluar 1)',
                                        keluar_henti='True' if i % 10 == 0 else 'False')) for i in range(200)]
        a = SH.sampel_lorong(calon, '2026-10-23', 20); b = SH.sampel_lorong(calon, '2026-10-23', 20)
        self.assertEqual(a, b); self.assertEqual(len(a), 20)
        self.assertEqual(sum(SH.keadaan_csv(x[2])[0] != 'pegang' for x in a), 10)
        self.assertNotEqual(a, SH.sampel_lorong(calon, '2026-10-26', 20))
        self.assertEqual(len(SH.sampel_lorong(calon, 'x', 0)), 200)

    # ---- ambil alih
    def kunci(self):
        n = 80; c = 100 + np.sin(np.arange(n)) * 0.05
        ix = [str(x.date()) for x in pd.bdate_range('2026-06-01', periods=n)]
        tulis_stor(self.stor, {'KUN': (ix, c.copy(), c + 0.1, c - 0.1, c)})
        return ix, c

    def test_ambil_alih_amaran_calon(self):
        ix, c = self.kunci()
        tulis_csv(self.d, 'claude.csv', [baris('KUN', ix, c, c, 70)])
        kod, out = self.sahkan()
        self.assertEqual(kod, 0, out)
        self.assertIn('ambil alih? KUN: 1 posisi C terbuka; harga terkunci', out)
        with open(self.aa, 'a') as f:
            f.write('KUN,2026-01-05,,,,bukan,https://x\n')        # disahkan bukan ambil alih
        self.assertNotIn('ambil alih? KUN', self.sahkan()[1])

    def test_ambil_alih_ralat_senarai(self):
        ix, c = self.kunci()
        with open(self.aa, 'a') as f:
            f.write(f'KUN,{ix[60]},,Pembeli,100,tunai,https://x\n')
        tulis_csv(self.d, 'claude.csv', [baris('KUN', ix, c, c, 70), baris('KUN', ix, c, c, 50, kaedah='M02')])
        kod, out = self.sahkan()
        self.assertEqual(kod, 1)
        r = [x for x in out.splitlines() if x.startswith('RALAT')]
        self.assertEqual(len(r), 1); self.assertIn('pengumuman ambil alih', r[0]); self.assertIn('M01', r[0])   # M02 dibeli sebelum
        self.assertNotIn('ambil alih? KUN', out)                     # dalam senarai: bukan calon lagi
        tulis_csv(self.d, 'claude.csv', [baris('KUN', ix, c, c, 70, tidak_sah='True', sebab_tidak_sah='isyarat palsu: x')])
        self.assertEqual(self.sahkan()[0], 0)

    # ---- bar sesi terakhir
    def test_bar_sesi(self):
        ix, o, h, l, c = siri([10.0] * 30)
        tulis_stor(self.stor, {'AAA': (ix, o, h, l, c), 'GGG': (ix[:-1], o[:-1], h[:-1], l[:-1], c[:-1])})
        tulis_csv(self.d, 'claude.csv', [baris('AAA', ix, o, c, 25), baris('GGG', ix[:-1], o, c[:-1], 25),
                                         baris('GGG', ix[:-1], o, c[:-1], 26, kaedah='M02'),
                                         baris('GGG', ix[:-1], o, c[:-1], 24, kaedah='M03', keluar='True', tarikh_keluar=ix[26],
                                               harga_keluar='10', untung_akhir_pct='0.00', keluar_henti='True',
                                               tarikh_keluar_henti=ix[26], harga_keluar_henti='10', untung_henti_pct='0.00',
                                               status_henti='Keluar: x', tutup_semua='True')])
        kod, out = self.sahkan()
        self.assertEqual(kod, 0, out)
        self.assertIn(f'bar sesi {ix[-1]}: 1 saham (2 posisi dipegang)', out); self.assertIn(f'GGG ({ix[-2]}, 2)', out)
        tk = os.path.join(self.d, 'terkini.csv')
        with open(tk, 'w') as f:
            f.write(f'ticker,date,open,high,low,close,volume\nGGG,{ix[-1].replace("-", "")},10,11,9,10,1000\n')
        out = self.sahkan('--terkini', tk)[1]
        self.assertNotIn('AMARAN bar sesi', out)
        tulis_csv(self.d, 'claude.csv', [baris('AAA', ix, o, c, 25), dict(baris('AAA', ix, o, c, 25, kaedah='M09'),
                                                                          tarikh_beli='2099-01-02', harga_beli='10')])
        self.assertIn('sesi posisi 2099-01-02 lebih baharu', self.sahkan()[1])

    # ---- untung_akhir_pct dan --json
    def test_untung_akhir_dan_json(self):
        ix, o, h, l, c = siri([10.0] * 30)
        tulis_stor(self.stor, {'AAA': (ix, o, h, l, c)})
        rows = [baris('AAA', ix, o, c, 25, kaedah=f'M{i:02d}', keluar='True', tarikh_keluar=ix[27], harga_keluar='11',
                      untung_akhir_pct='10.00' if i == 0 else '9.00', keluar_henti='True', tarikh_keluar_henti=ix[27],
                      harga_keluar_henti='11', untung_henti_pct='10.00', status_henti='Keluar: x', tutup_semua='True')
                for i in range(30)]
        tulis_csv(self.d, 'claude.csv', rows)
        js = os.path.join(self.d, 'semakan', 'sahkan.json')
        kod, out = self.sahkan('--json', js)
        self.assertEqual(kod, 1)
        self.assertEqual(sum('untung_akhir_pct 9.0 !=' in x for x in out.splitlines()), 29)
        j = muat(js)
        self.assertEqual(set(j), {'tarikh', 'dibina', 'status', 'n_ralat', 'n_amaran', 'ringkas'})
        self.assertEqual((j['status'], j['n_ralat'], j['tarikh']), ('ralat', 29, ix[-1]))
        self.assertLessEqual(len(j['ringkas']), 20); self.assertTrue(any('… dan' in x for x in j['ringkas']))
        tulis_csv(self.d, 'claude.csv', rows[:1])
        self.assertEqual(self.sahkan('--json', js)[0], 0)
        self.assertEqual(muat(js)['status'], 'ok')

    def test_tulis_json_had_baris(self):
        with tempfile.TemporaryDirectory() as d:
            p = os.path.join(d, 'a', 'b.json')
            j = SH.tulis_json(p, '2026-10-23', [f'r{i}' for i in range(5)], [f'a{i}' * 300 for i in range(40)], ['info'], 9)
            self.assertEqual(len(j['ringkas']), 20); self.assertEqual(j['status'], 'ralat')
            self.assertTrue(all(len(x) <= 210 for x in j['ringkas']))
            self.assertEqual(sum(x.startswith('RALAT') for x in j['ringkas']), 5)
            self.assertTrue(os.path.exists(p))
            self.assertEqual(SH.tulis_json(p, '', [], ['x'], [], 0)['status'], 'amaran')


# ---------------------------------------------------------------- lapisan 3: sampel_semak.py
D = '2026-10-23'


def c_baris(saham, kaedah, tb, hb, **kw):
    r = dict(ASAS, saham=saham, kaedah=kaedah, id_kaedah=kaedah, tarikh_beli=tb, harga_beli=str(hb), harga_terkini=str(hb),
             untung_pct='0.00', keluar='False', keluar_henti='False', tutup_semua='False',
             status_henti='Pegang (paras keluar 1; puncak 2; 1 hari)')
    r.update(kw)
    return r


KLINE = [('B1', '2026-10-23', 10, 10.5, 9.8, 10.2), ('B2', '2026-10-23', 20, 21, 19, 20.5),
         ('H1', '2026-10-20', 30, 31, 29, 30.5), ('H1', '2026-10-23', 29.8, 30, 28.5, 29),
         ('I1', '2026-10-20', 40, 41, 39, 40), ('I1', '2026-10-23', 38.5, 39, 38, 38.4),
         ('S1', '2026-10-20', 50, 51, 49, 50), ('S1', '2026-10-23', 52, 56, 51.5, 55),
         ('L1', '2026-10-14', 60, 61, 59, 60), ('L1', '2026-10-23', 66, 67, 65, 66.5),
         ('T1', '2026-10-19', 70, 71, 69, 70), ('T1', '2026-10-23', 72, 73, 71, 72.5)]


class UjiSampelSemak(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(); self.d = self.tmp.name
        tulis_csv(self.d, 'claude.csv', [
            c_baris('B1', 'M01', D, 10, harga_terkini='10.2', untung_pct='2.00'),
            c_baris('B2', 'M02', D, 20, nota='buka rasmi 2026-10-23', harga_terkini='20.5', untung_pct='2.50'),
            c_baris('H1', 'M03', '2026-10-20', 30, keluar='True', tarikh_keluar=D, harga_keluar='29', untung_akhir_pct='-3.33',
                    henti='29', isyarat_keluar='Keluar: kena henti (23 Okt @ 29.00)'),
            c_baris('I1', 'M04', '2026-10-20', 40, keluar='True', tarikh_keluar=D, harga_keluar='38.5', untung_akhir_pct='-3.75',
                    isyarat_keluar='Keluar: isyarat keluar kaedah 22 Okt (23 Okt @ 38.50)'),
            c_baris('S1', 'M05', '2026-10-20', 50, keluar='True', tarikh_keluar=D, harga_keluar='54', untung_akhir_pct='8.00',
                    isyarat_keluar='Keluar: capai sasaran (23 Okt @ 54.00)'),
            c_baris('L1', 'M06', '2026-10-14', 60, keluar_henti='True', tarikh_keluar_henti=D, harga_keluar_henti='66',
                    untung_henti_pct='10.00', status_henti='Keluar: tutup 65 bawah paras keluar 65.5 pada 22 Okt (23 Okt @ 66.00)',
                    harga_terkini='66.5'),
            c_baris('T1', 'M07', '2026-10-19', 70, harga_terkini='72.5', untung_pct='3.57'),
            c_baris('Z9', 'M08', '2026-10-01', 9, tidak_dibeli='True', harga_beli=''),
        ])
        self.kl = os.path.join(self.d, 'kline.csv')
        self.tulis_kline(KLINE)

    def tearDown(self):
        self.tmp.cleanup()

    def tulis_kline(self, rows, kepala='saham,tarikh,buka,tinggi,rendah,tutup'):
        with open(self.kl, 'w') as f:
            f.write(kepala + '\n')
            for i, (t, d, *b) in enumerate(rows):
                f.write(','.join([('US.' + t) if i % 2 else t, d.replace('-', '') if i % 3 else d] + [str(x) for x in b]) + '\n')

    def test_jenis_keluar(self):
        self.assertEqual(SS.jenis_keluar('Keluar: kena henti (buka bawah henti) (15 Okt @ 264.20)'), 'buka')
        self.assertEqual(SS.jenis_keluar('Keluar: kena henti (22 Okt @ 35.90)'), 'henti')
        self.assertEqual(SS.jenis_keluar('Keluar: capai sasaran (buka atas sasaran) (13 Okt @ 183.50)'), 'buka')
        self.assertEqual(SS.jenis_keluar('Keluar: capai sasaran (21 Okt @ 39.41)'), 'sasaran')
        self.assertEqual(SS.jenis_keluar('Keluar: isyarat palsu, saham diambil alih (umum 2026-05-18) — tutup 2026-10-20 @ 38.20'),
                         'tutup')
        self.assertEqual(SS.jenis_keluar('Keluar: had masa 30 hari (20 Okt @ 10.00)'), 'tutup')
        self.assertIsNone(SS.jenis_keluar('Pegang'))

    def test_pilih(self):
        s = SS.pilih(self.d, n=7, terkini=None)
        self.assertEqual(s['tarikh'], D); self.assertEqual(s['n'], 7)
        self.assertEqual(s, SS.pilih(self.d, n=7, terkini=None))                       # berketentuan
        kump = {p['saham']: p['kumpulan'] for p in s['posisi']}
        self.assertEqual(kump, {'B1': 'beli_baru', 'B2': 'beli_baru', 'L1': 'keluar_lorong2', 'H1': 'keluar_lorong1',
                                'I1': 'keluar_lorong1', 'S1': 'keluar_lorong1', 'T1': 'terbuka'})
        h1 = next(p for p in s['posisi'] if p['saham'] == 'H1')
        self.assertEqual((h1['jenis_keluar'], h1['kline_tarikh']), ('henti', ['2026-10-20', D]))
        self.assertEqual(next(p for p in s['posisi'] if p['saham'] == 'T1')['kline_tarikh'], ['2026-10-19', D])
        l1 = next(a for a in s['ambil'] if a['saham'] == 'L1')
        self.assertEqual((l1['simbol'], l1['mula'], l1['akhir']), ('US.L1', '2026-10-14', D))
        s3 = SS.pilih(self.d, n=3, terkini=None)
        self.assertEqual(sorted(p['kumpulan'] for p in s3['posisi']), ['beli_baru', 'keluar_lorong2', 'terbuka'])

    def test_pilih_utamakan_tanpa_sumber_kedua(self):
        tk = os.path.join(self.d, 'terkini.csv')
        with open(tk, 'w') as f:
            f.write('ticker,date,open,high,low,close,volume\nB2,20261023,20,21,19,20.5,1\n')
        s = SS.pilih(self.d, n=3, terkini=tk)
        self.assertEqual([p['saham'] for p in s['posisi'] if p['kumpulan'] == 'beli_baru'], ['B1'])   # B1 tiada bar yfinance

    def test_banding_ok_dan_beza(self):
        kel = os.path.join(self.d, 'semakan', 'sampel.json')
        with redirect_stdout(io.StringIO()):
            kod = SS.main(['banding', self.kl, '--folder', self.d, '--terkini', '', '--n', '7', '--keluar', kel])
        j = muat(kel)
        self.assertEqual((kod, j['status'], j['n'], j['n_beza'], j['tarikh']), (0, 'ok', 7, 0, D), j)
        self.assertTrue({'tarikh', 'dibina', 'status', 'n', 'n_beza', 'beza'} <= set(j))
        salah = [list(x) for x in KLINE]
        salah[0][2] = 10.5                       # buka B1 rasmi 10.5 lawan harga_beli 10
        salah[3][4] = 29.5                       # rendah H1 29.5 > henti 29: henti tidak disentuh
        salah[7][3] = 53.0                       # tinggi S1 53 < sasaran 54
        salah[9][2] = 67.0                       # buka L1 hari keluar lorong 2
        salah[11][5] = 73.5                      # tutup T1 sesi lawan harga_terkini
        self.tulis_kline([tuple(x) for x in salah])
        s = SS.pilih(self.d, n=7, terkini=None)
        j = SS.banding(self.kl, s, kel)
        medan = sorted((b['saham'], b['medan'].split(' ')[0]) for b in j['beza'])
        self.assertEqual(medan, [('B1', 'harga_beli'), ('H1', 'henti'), ('L1', 'harga_keluar_henti'), ('S1', 'sasaran'),
                                 ('T1', 'harga_terkini')])
        b1 = next(b for b in j['beza'] if b['saham'] == 'B1')
        self.assertEqual((b1['kaedah'], b1['tarikh_beli'], b1['csv'], b1['moomoo']), ('M01', D, 10.0, 10.5))
        self.assertEqual(j['status'], 'beza')
        with redirect_stdout(io.StringIO()):
            self.assertEqual(SS.main(['banding', self.kl, '--folder', self.d, '--terkini', '', '--n', '7', '--keluar', kel]), 1)

    def test_banding_henti_buka_dan_pilih_fail(self):
        salah = [list(x) for x in KLINE]
        salah[3][2] = 28.0                       # buka H1 28 < henti 29: patut keluar pada buka (buka bawah henti)
        salah[5][2] = 38.9                       # buka I1 hari keluar 38.9 lawan 38.5 (> 0.3%)
        self.tulis_kline([tuple(x) for x in salah])
        pf = os.path.join(self.d, 'pilih.json')
        with redirect_stdout(io.StringIO()):
            SS.main(['pilih', '--folder', self.d, '--terkini', '', '--n', '7', '--keluar', pf])
        j = SS.banding(self.kl, muat(pf), None)
        self.assertEqual(sorted((b['saham'], b['medan']) for b in j['beza']),
                         [('H1', 'harga_keluar (buka bawah henti: patut = buka)'), ('I1', 'harga_keluar (buka)')])

    def test_banding_belum_dan_tidak_sah(self):
        self.tulis_kline([('ZZZ', D, 1, 1, 1, 1)])
        s = SS.pilih(self.d, n=7, terkini=None)
        j = SS.banding(self.kl, s, None)
        self.assertEqual((j['status'], j['n']), ('belum', 0)); self.assertIn(f'B1 {D}', j['tiada_kline'])
        self.tulis_kline([('B1', D, 10, 10, 10)], kepala='saham,tarikh,buka,tinggi,rendah')
        err = io.StringIO()
        with redirect_stdout(io.StringIO()), redirect_stderr(err):
            self.assertEqual(SS.main(['banding', self.kl, '--folder', self.d, '--terkini', '', '--keluar', '']), 2)
        self.assertIn('lajur kline mesti', err.getvalue())


if __name__ == '__main__':
    unittest.main()
