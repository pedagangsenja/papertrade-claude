# Ujian standard/peta_kumpulan.py (dokumen db `kumpulan/peta`, panel "Peta industri"; 12 Nov 2026)
import csv, json, os, sys, tempfile, unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'standard'))
import peta_kumpulan as P  # noqa: E402

LAJUR = ['tarikh', 'jenis', 'nama', 'sektor', 'n', 'skor', 'gred', 'w_rs_positif', 'w_rs_naik', 'w_trend', 'm1m_med',
         'pct_atas_sma200', 'dibina']


def tulis(path, rows):
    with open(path, 'w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=LAJUR); w.writeheader()
        for r in rows:
            w.writerow(dict(zip(LAJUR, r)))


def baris(t, nama, skor, jenis='Industri', sektor='Tech', w=(1, 1, 1)):
    return [t, jenis, nama, sektor, 10, skor, 'A', *w, 1.5, 60.0, t + ' 20:00 MYT']


class TestPangkat(unittest.TestCase):
    def test_susunan_dan_seri(self):
        r = [dict(nama='A', skor='90'), dict(nama='B', skor='90'), dict(nama='C', skor='10'), dict(nama='D', skor='')]
        self.assertEqual(P.pangkat(r), {'A': 1, 'B': 1, 'C': 3})


class TestBina(unittest.TestCase):
    def setUp(self):
        self.d = tempfile.mkdtemp()
        self.kini, self.sej = os.path.join(self.d, 'k.csv'), os.path.join(self.d, 's.csv')
        self.tarikh = [f'2026-10-{h:02d}' for h in range(1, 24)]   # 23 sesi

    def bina(self, tambahan=()):
        rows = []
        for i, t in enumerate(self.tarikh):
            akhir = i == len(self.tarikh) - 1
            # X naik dari bawah ke atas pada sesi terakhir; Y sebaliknya; Z sentiasa di tengah
            rows += [baris(t, 'X', 90 if akhir else 10), baris(t, 'Y', 10 if akhir else 90), baris(t, 'Z', 50),
                     baris(t, 'Fin', 80, 'Sektor', 'Fin', (0, 1, 1)), baris(t, 'Ten', 20, 'Sektor', 'Ten', (0, 0, 0))]
        rows += list(tambahan)
        tulis(self.sej, rows[:-5]); tulis(self.kini, rows[-5:] if not tambahan else rows[-5 - len(tambahan):])
        return P.bina(self.kini, self.sej)

    def test_tiada_data(self):
        self.assertIsNone(P.bina(os.path.join(self.d, 'tiada.csv'), os.path.join(self.d, 'tiada2.csv')))

    def test_pangkat_dan_perubahan(self):
        d = self.bina()
        self.assertEqual((d['tarikh'], d['tarikh_5'], d['tarikh_21'], d['sesi']),
                         ('2026-10-23', '2026-10-18', '2026-10-02', 23))
        r = {(x['j'], x['n']): x for x in d['rows']}
        self.assertEqual((r['I', 'X']['p'], r['I', 'X']['d5'], r['I', 'X']['d21']), (1, 2, 2))    # 3 -> 1 = naik 2
        self.assertEqual((r['I', 'Y']['p'], r['I', 'Y']['d5']), (3, -2))
        self.assertEqual((r['I', 'Z']['p'], r['I', 'Z']['d5']), (2, 0))
        self.assertEqual((r['S', 'Fin']['p'], r['S', 'Ten']['p'], r['S', 'Fin']['w']), (1, 2, [0, 1, 1]))
        self.assertEqual([x['n'] for x in d['rows'] if x['j'] == 'I'], ['X', 'Z', 'Y'])           # susun ikut pangkat
        self.assertEqual(r['I', 'X']['sp'][-2:], [10, 90])
        self.assertLessEqual(len(r['I', 'X']['sp']), P.SIRI_MAKS)

    def test_kumpulan_baharu_dan_skor_kosong(self):
        t = self.tarikh[-1]
        d = self.bina([baris(t, 'Baru', 70), baris(t, 'Kosong', '')])
        r = {x['n']: x for x in d['rows'] if x['j'] == 'I'}
        self.assertEqual((r['Baru']['p'], r['Baru']['d5'], r['Baru']['sp']), (2, None, [70]))     # tiada sejarah
        self.assertEqual((r['Kosong']['p'], r['Kosong']['sk'], r['Kosong']['d5']), (None, None, None))
        self.assertEqual([x['n'] for x in d['rows'] if x['j'] == 'I'][-1], 'Kosong')              # tanpa pangkat di bawah

    def test_sejarah_pendek(self):
        self.tarikh = self.tarikh[:3]
        d = self.bina()
        self.assertEqual((d['tarikh_5'], d['tarikh_21']), (None, None))
        self.assertTrue(all(x['d5'] is None and x['d21'] is None for x in d['rows']))

    def test_boleh_json_dan_kecil(self):
        d = self.bina()
        self.assertLess(len(json.dumps(d, allow_nan=False)), 262144)

    def test_data_sebenar(self):
        if not os.path.exists(P.KINI):
            self.skipTest('tiada data/kumpulan')
        d = P.bina()
        self.assertTrue(d['rows'])
        self.assertLess(len(json.dumps(d, ensure_ascii=False, allow_nan=False).encode()), 262144 // 2)
        self.assertEqual({x['j'] for x in d['rows']}, {'S', 'I'})


if __name__ == '__main__':
    unittest.main()
