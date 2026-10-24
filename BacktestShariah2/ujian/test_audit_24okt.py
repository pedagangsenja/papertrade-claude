# Ujian pembetulan audit dashboard tab demi tab (24 Okt 2026; cawangan pratonton-audit): semakan harga beli lawan buka
# (sahkan.py, betul_harga_beli.py), ambil alih (tambah rekod, calon harga terkunci), lorong 2 (sejarah sebelum beli, --saham),
# jana_db (saring saiz, mae dibahagi, maefe_l2, kualiti, langkau, earn_kini, label jujur), watchlist (normal_watch) dan
# gred_pada tarikh data (gred.py).
import csv, io, json, os, sys, tempfile, unittest
from contextlib import redirect_stdout
from datetime import date

import numpy as np
import pandas as pd

UJI = os.path.dirname(os.path.abspath(__file__))
BS2 = os.path.dirname(UJI)
for p in (os.path.join(BS2, 'standard'), os.path.join(BS2, 'kod'), UJI):
    sys.path.insert(0, p)
import sahkan  # noqa: E402
import betul_harga_beli as BHB  # noqa: E402
import ambil_alih as AA  # noqa: E402
import keluar_lorong as KL  # noqa: E402
import jana_db as jd  # noqa: E402
import harian_c as HC  # noqa: E402
import gred as G  # noqa: E402
from bahagi_db import bahagi  # noqa: E402
from test_sahkan import ASAS, tulis  # noqa: E402


def tulis_stor(d, baris, nama='harga_A.csv'):
    with open(os.path.join(d, nama), 'w') as f:
        f.write('ticker,date,open,high,low,close,volume\n' + ''.join(','.join(map(str, b)) + '\n' for b in baris))


class UjiSahkanBuka(unittest.TestCase):
    """sahkan.py: harga_beli C lawan buka bar hari beli dalam stor (toleransi 0.3%; M dan 'buka sementara' dikecualikan)."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(); self.d = self.tmp.name
        self.stor = os.path.join(self.d, 'stor'); os.makedirs(self.stor)
        tulis_stor(self.stor, [('AAA', 20261013, 100, 106, 99, 105, 1000), ('MMM', 20261013, 50, 51, 49, 50, 1000)])
        tulis(self.d, 'moomoo.csv', [dict(ASAS, saham='MMM', harga_beli='52', harga_terkini='54.6', untung_pct='5.0')])
        tulis(self.d, 'watchlist.csv', [{'Saham': 'BBB', 'Kaedah': 'M02', 'Sektor': 'Energy', 'Industri': 'Oil', '% hampir': '95'}])

    def tearDown(self):
        self.tmp.cleanup()

    def jalan(self, hb, **kw):
        ht = round(hb * 1.05, 4)
        tulis(self.d, 'claude.csv', [dict(ASAS, harga_beli=str(hb), harga_terkini=str(ht), untung_pct=f'{(ht / hb - 1) * 100:.2f}',
                                          **kw)])
        out = io.StringIO()
        with redirect_stdout(out):
            kod = sahkan.main(['--folder', self.d, '--stor', self.stor])
        return kod, out.getvalue()

    def test_dalam_toleransi(self):
        self.assertEqual(self.jalan(100.2)[0], 0)          # 0.2% <= 0.3%; M (52 lawan buka 50) dikecualikan

    def test_ralat_beza_besar(self):
        kod, out = self.jalan(96.458)                       # cth. DAC 164.162 lawan buka 170.19 (−3.5%)
        self.assertEqual(kod, 1); self.assertIn('≠ buka bar 2026-10-13', out); self.assertIn('betul_harga_beli.py', out)

    def test_buka_sementara_dikecualikan(self):
        self.assertEqual(self.jalan(103, nota='buka sementara = tutup isyarat; buka_lewat: belum didagangkan')[0], 0)

    def test_buka_moomoo_disahkan_diterima(self):
        with open(os.path.join(self.stor, 'buka_moomoo.csv'), 'w') as f:
            f.write('ticker,date,open\nAAA,20261013,100.4\n')    # beza 0.4% dengan stor yfinance; buka Moomoo rasmi
        self.assertEqual(self.jalan(100.4)[0], 0)

    def test_tiada_bar_dilangkau(self):
        self.assertEqual(self.jalan(120, tarikh_beli='2026-10-14')[0], 0)


class UjiBetulHargaBeli(unittest.TestCase):
    def test_betul_dan_langkau(self):
        with tempfile.TemporaryDirectory() as d:
            stor = os.path.join(d, 'stor'); os.makedirs(stor)
            tulis_stor(stor, [('DAC', 20261012, 170.19, 172.76, 169.25, 169.39, 1), ('YYY', 20261012, 20, 21, 19, 20, 1)])
            asas = dict(ASAS, saham='DAC', tarikh_beli='2026-10-12', harga_beli='164.162', henti='157.1557',
                        harga_terkini='157.1555', untung_pct='-4.27', keluar='True', tarikh_keluar='2026-10-16',
                        harga_keluar='157.1555', untung_akhir_pct='-4.27', keluar_henti='False', nota='')
            tulis(d, 'moomoo.csv', [dict(ASAS, saham='MMM')])
            tulis(d, 'claude.csv', [dict(asas, kaedah='M80', id_kaedah='M80'), dict(asas, kaedah='M06', id_kaedah='M06'),
                                    dict(asas, saham='YYY', kaedah='M80', id_kaedah='M80', harga_beli='22', henti='20.5', keluar='False',
                                         tarikh_keluar='', harga_keluar='', untung_akhir_pct='', harga_terkini='21', untung_pct='-4.55')])
            ubah, langkau = BHB.jalan(d, stor, sah='kline Moomoo sama', tulis=True, tarikh='24 Okt 2026')
            rows = list(csv.DictReader(open(os.path.join(d, 'claude.csv'))))
        self.assertEqual([x[2] for x in ubah], ['M80'])
        self.assertEqual(rows[0]['harga_beli'], '170.19')
        self.assertEqual((rows[0]['untung_pct'], rows[0]['untung_akhir_pct']), ('-7.66', '-7.66'))
        self.assertIn('harga_beli dibetulkan 24 Okt 2026: 164.162 -> 170.19', rows[0]['nota'])
        self.assertEqual(rows[1]['harga_beli'], '164.162')                 # M06: henti ikut buka masuk
        self.assertEqual(rows[2]['harga_beli'], '22')                      # buka 20 <= henti 20.5: kaedah melangkau
        self.assertEqual(sorted(x[2] for x in langkau), ['M06', 'M80'])


def siri_kunci(n=80, harga=100.0, jurang=True):
    ix = pd.bdate_range('2026-06-01', periods=n)
    c = np.full(n, harga) + np.sin(np.arange(n)) * 0.05
    return pd.DataFrame(dict(open=c, high=c + 0.1, low=c - 0.1, close=c, volume=1e5), index=ix)


class UjiAmbilAlih(unittest.TestCase):
    def test_tambah_rekod(self):
        with tempfile.TemporaryDirectory() as d:
            p = os.path.join(d, 'ambil_alih.csv')
            with open(p, 'w') as f:
                f.write(','.join(AA.LAJUR) + '\n')
            self.assertTrue(AA.tambah_rekod('ACA', '2026-06-22', 'CRH', 'tunai', 'https://x', tamat='2026-10-23', harga='150', path=p))
            self.assertFalse(AA.tambah_rekod('ACA', '2026-06-22', 'CRH', 'tunai', 'https://x', path=p))   # pendua
            with self.assertRaises(SystemExit):
                AA.tambah_rekod('XXX', '2026-06-22', 'Y', 'hutang', 'https://x', path=p)
            r = AA.baca_senarai(p)
        self.assertEqual([(x['saham'], x['tarikh_tamat'], x['harga_tawaran']) for x in r], [('ACA', '2026-10-23', '150')])

    def test_calon_kunci(self):
        rng = np.random.default_rng(0)
        bebas = siri_kunci(); c = 100 * np.exp(np.cumsum(rng.normal(0, 0.02, len(bebas))))
        bebas = bebas.assign(close=c, open=c, high=c * 1.02, low=c * 0.98)
        rata = siri_kunci().assign(high=lambda x: x.close, low=lambda x: x.close)    # julat 0 = tidak cair, bukan kunci
        x = AA.calon_kunci({'KUNCI': siri_kunci(), 'BEBAS': bebas, 'RATA': rata}, {'KUNCI', 'BEBAS', 'RATA'})
        self.assertEqual([y['saham'] for y in x], ['KUNCI'])
        self.assertLessEqual(x[0]['julat_med_pct'], 0.6); self.assertLessEqual(x[0]['atr_pct'], 0.5)


def langkah(tutup, mula='2026-08-03'):
    c = np.array(tutup, float); o = np.r_[c[0], c[:-1]]
    ix = pd.bdate_range(mula, periods=len(c))
    return pd.DataFrame(dict(open=o, high=c + 1, low=c - 1, close=c, volume=1.0), index=ix)


class UjiLorong2Sejarah(unittest.TestCase):
    def test_sambung_sejarah(self):
        penuh = langkah([100.0] * 20 + list(range(101, 121)))
        kerja = {'X': penuh.iloc[20:].copy(), 'Y': penuh.iloc[20:].copy()}
        sumber = {'X': penuh, 'Y': penuh * 1.1}                    # Y: konvensyen pelarasan lain -> tidak disambung
        t = KL.sambung_sejarah(kerja, sumber)
        self.assertEqual(t, {'X': 20}); self.assertEqual(len(kerja['X']), 40); self.assertEqual(len(kerja['Y']), 20)

    def test_sejarah_pendek_tidak_dibeku(self):
        # tutup naik 10 bar kemudian jatuh: tanpa sejarah sebelum beli ATR hanya wujud pada bar ke-14 (keluar lewat)
        g = langkah(list(range(101, 111)) + list(range(109, 80, -1)))
        ix = [str(x.date()) for x in g.index]
        L2, _ = KL.nilai_baris(ix, g.open.values, g.high.values, g.low.values, g.close.values, ix[0], 101.0)
        self.assertEqual(L2['keluar_henti'], 'True'); self.assertIn(KL.TANDA_PENDEK, L2['status_henti'])
        r = dict(saham='X', kaedah='S04V2', tarikh_beli=ix[20], harga_beli='100', keluar='False', **L2)
        # sejarah penuh kini ada (20 bar sebelum beli): baris bertanda TANDA_PENDEK dinilai semula, bukan dibekukan
        penuh = langkah([100.0] * 20 + list(range(101, 111)) + list(range(109, 80, -1)), mula='2026-07-06')
        r['tarikh_beli'] = str(penuh.index[20].date())
        H = {'X': ([str(x.date()) for x in penuh.index], penuh.open.values, penuh.high.values, penuh.low.values, penuh.close.values)}
        KL.kemas_baris(r, H, [])
        self.assertNotIn(KL.TANDA_PENDEK, r['status_henti']); self.assertIn(KL.PENANDA, r['status_henti'])

    def test_saham_sahaja(self):
        g = langkah([100.0] * 20 + list(range(101, 111)))
        H = {t: ([str(x.date()) for x in g.index], g.open.values, g.high.values, g.low.values, g.close.values) for t in ('X', 'Y')}
        with tempfile.TemporaryDirectory() as d:
            with open(os.path.join(d, 'claude.csv'), 'w', newline='') as f:
                w = csv.writer(f); w.writerow(['tarikh_beli', 'saham', 'kaedah', 'harga_beli', 'keluar'])
                for t in ('X', 'Y'):
                    w.writerow([str(g.index[20].date()), t, 'M01', '101', 'False'])
            asal = KL.muat_harga; KL.muat_harga = lambda stor: H
            try:
                with redirect_stdout(io.StringIO()):
                    KL.main(['--folder', d, '--stor', d, '--saham', 'X'])
            finally:
                KL.muat_harga = asal
            r = {x['saham']: x for x in csv.DictReader(open(os.path.join(d, 'claude.csv')))}
        self.assertEqual(r['X']['keluar_henti'], 'False'); self.assertEqual(r['Y']['keluar_henti'], '')


class UjiJanaDb(unittest.TestCase):
    def stor(self, d):
        tulis_stor(d, [('AAA', 20261001, 10, 10.5, 9.8, 10, 100), ('AAA', 20261002, 10, 12, 9.0, 11, 100),
                       ('AAA', 20261005, 11, 13, 10.5, 12, 100), ('BBB', 20261001, 20, 21, 19, 20, 100),
                       ('BBB', 20261002, 20, 20, 20, 20, 0), ('BBB', 20261005, 20, 20, 20, 20, 0)])
        with open(os.path.join(d, 'harga_idx.csv'), 'w') as f:
            f.write('ticker,date,open,high,low,close,volume\nSPY,20261001,600,601,599,600,1\n')

    def test_saring_saiz(self):
        ralat = []
        semua = [('a', [('kecil', {'x': 'y' * 10})]), ('a', [('besar', {'x': 'y' * 2000})]), ('a', [('hampir', {'x': 'y' * 850})])]
        out = jd.saring_saiz(semua, ralat, had=1000)
        self.assertEqual([x[1] for x in out], ['kecil', 'hampir'])
        self.assertTrue(any('a/besar' in r and 'melebihi had' in r for r in ralat))
        self.assertTrue(any(r.startswith('amaran: a/hampir') for r in ralat))

    def test_mae_senarai_dibahagi(self):
        rows = [[f'C|S{i:04d}|M01|2026-10-01', -1.5] for i in range(300)]
        bhg = bahagi(dict(rows=rows, dibina='x'), 'mae', 4000)
        self.assertGreater(len(bhg), 1)
        self.assertEqual(sum((d['rows'] for _, d in bhg), []), rows)
        self.assertIn('mae', jd.BAHAGI); self.assertIn('maefe_l2', jd.BAHAGI); self.assertIn('langkau', jd.BAHAGI)

    def test_maefe_l2(self):
        C = [dict(saham='AAA', kaedah='M01', tarikh_beli='2026-10-01', harga_beli='10', keluar='True', tarikh_keluar='2026-10-01',
                  harga_keluar='9.9', keluar_henti='False'),
             dict(saham='AAA', kaedah='M02', tarikh_beli='2026-10-01', harga_beli='10', keluar='True', keluar_henti='True',
                  tarikh_keluar_henti='2026-10-05', harga_keluar_henti='11.5')]
        with tempfile.TemporaryDirectory() as d:
            self.stor(d)
            m = {k: (a, b) for k, a, b in jd.maefe_l2([], C, d)}
        self.assertEqual(m['C|AAA|M01|2026-10-01'], (-10.0, 30.0))   # lorong 2 masih dipegang: rendah 9.0, tinggi 13
        self.assertEqual(m['C|AAA|M02|2026-10-01'], (-10.0, 20.0))   # hingga sebelum 5 Okt + harga keluar 11.5

    def test_kualiti(self):
        with tempfile.TemporaryDirectory() as d:
            self.stor(d)
            tk = os.path.join(d, 'terkini.csv')
            with open(tk, 'w') as f:
                f.write('ticker,date,open,high,low,close,volume\nAAA,20261005,11,13,10.5,12,100\n')
            asal = jd.TERKINI; jd.TERKINI = tk
            try:
                C = [dict(saham='AAA', kaedah='M01', tarikh_beli='2026-10-01', harga_beli='10.2', keluar='False'),
                     dict(saham='BBB', kaedah='M01', tarikh_beli='2026-10-01', harga_beli='20', keluar='False'),
                     dict(saham='AAA', kaedah='M82', tarikh_beli='2026-10-02', harga_beli='10', keluar='False',
                          nota='keluar dinilai semula 22 Oct 2026 (dagangan sendiri, kod/dagangan.py)'),
                     dict(saham='AAA', kaedah='M20', tarikh_beli='2026-10-01', harga_beli='10', keluar='True', tutup_semua='True',
                          tarikh_keluar='2026-10-02', nota='keluar dinilai semula 22 Oct 2026 (dagangan sendiri, kod/dagangan.py)')]
                M = [dict(saham='AAA', kaedah='M01', tarikh_beli='2026-10-01', harga_beli='10.5', keluar='False')]
                k = jd.kualiti(M, C, '2026-10-05', d)
            finally:
                jd.TERKINI = asal
        self.assertEqual(k[('C', 'AAA', 'M01', '2026-10-01')], ['beli_ne_buka'])             # 10.2 lawan buka 10
        self.assertEqual(k[('C', 'BBB', 'M01', '2026-10-01')], ['bar_moomoo', 'bar_sintetik'])  # tiada bar yfinance; bar rata volum 0
        self.assertEqual(k[('C', 'AAA', 'M82', '2026-10-02')], ['keluar_dibuka_semula'])
        self.assertNotIn(('C', 'AAA', 'M20', '2026-10-01'), k)                                # keluar dibetulkan, bukan dibuka
        self.assertNotIn(('M', 'AAA', 'M01', '2026-10-01'), k)                                # M: harga isian sim

    def test_baris_posisi(self):
        kual = {('C', 'AAA', 'M03', '2026-10-01'): ['bar_moomoo']}
        r = dict(saham='AAA', kaedah='M03', id_kaedah='M03', tarikh_beli='2026-10-01', harga_beli='10', tidak_sah='True',
                 sebab_tidak_sah='isyarat palsu: saham diambil alih (umum 2026-06-22, CRH; senarai)')
        db = jd.baris_posisi(r, 'C', {}, '2026-10-05', kual, {})
        self.assertEqual((db['kualiti'], db['sasaran_dinamik'], db['jenis_tidak_sah']), (['bar_moomoo'], True, 'ambil_alih'))
        db = jd.baris_posisi(dict(r, kaedah='M19', id_kaedah='M19', tidak_sah=''), 'C', {}, '2026-10-05', {}, {})
        self.assertNotIn('sasaran_dinamik', db); self.assertNotIn('jenis_tidak_sah', db); self.assertNotIn('kualiti', db)

    def test_jenis_tidak_sah(self):
        self.assertEqual(jd.jenis_tidak_sah('isyarat palsu: saham tidak cair (20 bar: …) pada 2026-10-14'), 'tidak_cair')
        self.assertEqual(jd.jenis_tidak_sah('isyarat berganda: kelas berganda Fox (…)'), 'kelas_berganda')
        self.assertEqual(jd.jenis_tidak_sah('Keluar: delist / tiada data 10 sesi'), 'delist')
        self.assertEqual(jd.jenis_tidak_sah('sedia() sig=False pada 2026-10-22'), 'lain')

    def test_earn_kini(self):
        K = {'AAA': {date(2026, 10, 21): 'Nasdaq', date(2026, 10, 28): 'Nasdaq'}, 'BBB': {date(2026, 10, 14): 'Nasdaq'}}
        a = jd.earn_kini({}, 'AAA', '2026-10-23', K)
        self.assertEqual(a, dict(earn_kini='2026-10-28', earn_kini_h=3, earn_lalu='2026-10-21'))
        self.assertEqual(jd.earn_kini({}, 'BBB', '2026-10-23', K), {})      # lalu 7 hari dagangan: tiada ikon semalam

    def test_langkau(self):
        x, tak = jd.hurai_langkau_rutin('buka > buka_maks — FRPT M08, ROL M08; buka ≤ henti — COR M14, GGG M35, M117 & M149, '
                                        'B M20 & M123. Tiada bertindih.')
        self.assertEqual(tak, [])
        self.assertEqual([(t, k) for t, k, _ in x], [('FRPT', 'M08'), ('ROL', 'M08'), ('COR', 'M14'), ('GGG', 'M35'),
                                                     ('GGG', 'M117'), ('GGG', 'M149'), ('B', 'M20'), ('B', 'M123')])
        with tempfile.TemporaryDirectory() as d:
            log = os.path.join(d, 'log.md')
            with open(log, 'w', encoding='utf-8') as f:
                f.write('## 2026-10-13 (9:36 NY) — Beli maya 9:35 NY\n- Dilangkau 1: buka ≤ henti — OLD M01.\n'
                        '## 2026-10-22 (9:38 NY) — Beli maya 9:35 NY\n- Dilangkau 2: buka ≤ henti — IAG M13; buka > buka_maks — APPN M06. Tiada bertindih.\n'
                        '## 2026-10-23 22:15 MYT — GitHub Actions: beli maya 2026-10-23 (isyarat 2026-10-22)\n'
                        '- Dilangkau: FRPT M08: buka 67.01 > buka_maks 66.15; PEGA M153: isyarat batal pada buka (peraturan kaedah).\n')
            lk = jd.langkau_beli(d, {}, log=log)
            self.assertEqual([(r['tarikh'], r['saham']) for r in lk['rows']],
                             [('2026-10-22', 'APPN'), ('2026-10-22', 'IAG'), ('2026-10-23', 'FRPT'), ('2026-10-23', 'PEGA')])
            self.assertEqual(lk['liputan']['2026-10-22'], dict(bil_log=2, bil=2))
            st = dict(beli=dict(tarikh='2026-10-23', dilangkau=3, langkau=['A M01: x', 'B M02: y', 'C M03: z']))
            lk = jd.langkau_beli(d, st, log=log)
            self.assertEqual(sum(r['tarikh'] == '2026-10-23' for r in lk['rows']), 3)
            self.assertEqual(lk['liputan']['2026-10-23'], dict(bil_log=3, bil=3))

    def test_label_jujur(self):
        self.assertEqual(jd.penulis_data(jd.PT, {}, 'bayang'), 'rutin Claude 6:02 MYT (jadual/kemas_kini_0602.md)')
        self.assertEqual(jd.penulis_data('/x', {'malam': {}}, 'bayang'), 'GitHub Actions (standard/harian_c.py)')
        self.assertEqual(jd.sumber_harga('rutin: yfinance + Moomoo', 'p', jd.STOR), 'rutin: yfinance + Moomoo')
        with tempfile.TemporaryDirectory() as d:
            p = os.path.join(d, 'status.json')
            json.dump(dict(terkini=dict(sesi=20261023, dijana='2026-10-23 23:59 UTC', bil_tiada_bar_sesi=47)), open(p, 'w'))
            t = jd.sumber_harga(None, 'rutin X', jd.STOR, path=p)
        self.assertIn('47 saham tanpa bar', t); self.assertIn('--sumber kosong', t); self.assertNotIn('muktamad', t)


class UjiJanaDbMain(unittest.TestCase):
    """jana_db.main hujung ke hujung atas folder kecil: dokumen baharu dan medan harian/status (lampu sistem)."""

    def test_main(self):
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
            st = json.load(open(os.path.join(kel, 'harian', 'status.json')))
            mae = json.load(open(os.path.join(kel, 'prestasi', 'mae.json')))
            wl = json.load(open(os.path.join(kel, 'papertrade', 'watchlist.json')))
            ada = {os.path.relpath(x, kel) for x in __import__('glob').glob(os.path.join(kel, '*', '*.json'))}
            pos = json.load(open(os.path.join(kel, 'papertrade', 'claude.json')))
        for k in ('ralat', 'mod', 'sumber_harga', 'saluran', 'beli_langkau'):
            self.assertIn(k, st)
        self.assertIsInstance(st['ralat'], list); self.assertEqual(st['sumber_harga'], 'ujian')
        self.assertTrue({'ringkas_c', 'trend', 'lorong2', 'garis', 'mfe', 'sektor', 'sst', 'lejar', 'analisis', 'slot',
                         'watchlist'} <= set(st['saluran']))
        self.assertEqual(mae['rows'], [['C|AAA|M03|2026-10-13', -1.0]]); self.assertIn('bahagian', mae)
        self.assertTrue({'prestasi/maefe_l2.json', 'papertrade/langkau.json', 'papertrade/ringkas_c.json'} <= ada)
        self.assertEqual((wl['rows'][0]['pct_dipenuhi'], wl['rows'][0]['disentuh'], wl['rows'][0]['tarikh_data']),
                         (99.9, True, '2026-10-14'))
        self.assertIn('(ujian)', pos['harga_pada']); self.assertNotIn('muktamad', pos['harga_pada'])


class UjiWatchlist(unittest.TestCase):
    def test_normal_watch(self):
        lengkap = {'% hampir': '100.0', 'Jarak %': '0.0', 'Syarat belum cukup': HC.LENGKAP}
        sentuh = {'% hampir': '100.0', 'Jarak %': '0.0', 'Syarat belum cukup': 'Tutup esok > 20.27'}
        biasa = {'% hampir': '98.5', 'Jarak %': '1.5', 'Syarat belum cukup': 'Tutup esok > 20.27'}
        for r in (lengkap, sentuh, biasa):
            HC.normal_watch(r)
        self.assertEqual((lengkap['% hampir'], lengkap['disentuh']), ('100.0', ''))
        self.assertEqual((sentuh['% hampir'], sentuh['disentuh']), ('99.9', 'True'))
        self.assertEqual((biasa['% hampir'], biasa['disentuh']), ('98.5', ''))
        self.assertFalse(HC.normal_watch(sentuh))                          # idempoten
        self.assertIn('disentuh', HC.WATCH_LAJUR)


class UjiGredPada(unittest.TestCase):
    def test_tarikh_gred(self):
        self.assertEqual(G.tarikh_gred('2026-10-22', '2026-10-22', '2026-10-23'), '2026-10-22 (imbasan 2026-10-23)')
        self.assertEqual(G.tarikh_gred('2026-10-21', '2026-10-22', '2026-10-23'),
                         '2026-10-21 (S/I 2026-10-21; RS 2026-10-22; imbasan 2026-10-23)')
        self.assertEqual(G.tarikh_gred('2026-10-23', None, '2026-10-23'), '2026-10-23')
        self.assertTrue(G.tarikh_gred(None, None, '2026-10-23').startswith('2026-10-23 (tarikh imbasan'))

    def test_pada_data(self):
        kpeta = {'2026-10-21': ({'Tech': (50.0, 'C')}, {'Soft': (60.0, 'C')}), '2026-10-22': ({'Tech': (55.0, 'C')}, {'Soft': (61.0, 'B')})}
        rs = pd.DataFrame(dict(tarikh=['2026-10-21', '2026-10-22'], ticker=['X', 'X'], rs=[70, 80]))
        rows = [dict(Saham='X', sektor_us='Tech', industri_us='Soft', skor_sektor='55.0', skor_industri='61.0', rs_rating='80',
                     rs_sumber='pasaran', gred_pada='2026-10-23'),
                dict(Saham='X', sektor_us='Tech', industri_us='Soft', skor_sektor='99', skor_industri='99', rs_rating='99',
                     rs_sumber='pasaran', gred_pada='2026-10-23'),
                dict(Saham='X', gred_pada='2026-10-22 (imbasan 2026-10-23)')]
        ubah, tak = G.pada_data(rows, kpeta, rs)
        self.assertEqual((ubah, tak), (1, 1))
        self.assertEqual([r['gred_pada'] for r in rows], ['2026-10-22 (imbasan 2026-10-23)', '2026-10-23', '2026-10-22 (imbasan 2026-10-23)'])



class TestHariDagNyse(unittest.TestCase):
    """Audit swing trader P0 #4: hari dagangan ke earnings mengikut cuti NYSE (Thanksgiving, Krismas)."""
    def test_cuti(self):
        try:
            import exchange_calendars  # noqa: F401
        except ImportError:
            self.skipTest('exchange_calendars tiada')
        self.assertEqual(jd.hari_dag(date(2026, 11, 24), date(2026, 11, 30)), 3)    # 26 Nov Thanksgiving
        self.assertEqual(jd.hari_dag(date(2026, 12, 21), date(2026, 12, 29)), 5)    # 25 Dis Krismas
        self.assertEqual(jd.hari_dag(date(2026, 10, 26), date(2026, 10, 31)), 5)

if __name__ == '__main__':
    unittest.main()
