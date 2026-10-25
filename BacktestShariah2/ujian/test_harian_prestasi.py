# Ujian standard/harian_prestasi.py (cadangan 25 Okt 2026): label §7 dibersarakan (medan lama dikekalkan untuk keserasian,
# rujukan pintu Papan Penganalisis), Combine = Papertrade C sahaja, Papertrade M kekal berasingan; KPI/skor tidak berubah.
import json, os, sys, tempfile, unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'standard'))
import harian_prestasi as HP


def r(saham, kaedah, u, keluar=True, hari=5, tarikh='2026-10-20'):
    return dict(saham=saham, kaedah=kaedah, tarikh_beli=tarikh, keluar=keluar, hari=hari,
                untung_akhir_pct=u if keluar else None, untung_pct=u)


M = [r('AAA', 'M01', -10.0), r('BBB', 'M01', -8.0)]
C = [r('CCC', 'M01', 4.0), r('DDD', 'M01', 2.0), r('EEE', 'M02', -1.0, keluar=False)]


class TestHarianPrestasi(unittest.TestCase):
    def test_combine_tanpa_moomoo(self):
        res = HP.prestasi(M, C, {})
        self.assertEqual(res['Combine']['kpi'], res['C']['kpi'])
        self.assertEqual(res['Combine']['kpi']['dagangan'], 3)
        self.assertEqual(res['M']['kpi']['dagangan'], 2)          # sejarah Moomoo kekal dipapar berasingan
        self.assertIn('Papertrade C sahaja', res['Combine']['nota'])

    def test_label_dibersarakan_medan_kekal(self):
        res = HP.prestasi(M, C, {}, {'M01': ('OK', 'PERHATI')})
        for nm in ('M', 'C', 'Combine'):
            x = res[nm]
            self.assertIn('teruskan', x); self.assertIn('hentikan', x); self.assertIn('bil', x)
            self.assertIsNone(x['teruskan']); self.assertIsNone(x['hentikan']); self.assertIsNone(x['bil'])
            self.assertEqual({k['keputusan'] for k in x['kaedah']}, {HP.DIBERSARAKAN})
        m01 = next(k for k in res['C']['kaedah'] if k['kaedah'] == 'M01')
        self.assertEqual((m01['pantau_penganalisis'], m01['status_penganalisis']), ('OK', 'PERHATI'))
        m02 = next(k for k in res['C']['kaedah'] if k['kaedah'] == 'M02')
        self.assertIsNone(m02['pantau_penganalisis'])

    def test_kpi_skor_tidak_berubah(self):
        res = HP.prestasi(M, C, {'C|CCC|M01|2026-10-20': -2.0})
        k = res['C']['kpi']
        self.assertEqual((k['kadar_menang'], k['untung_purata'], k['rugi_terbesar_saham']), (66.7, 1.67, 'EEE (M02)'))
        m01 = next(x for x in res['C']['kaedah'] if x['kaedah'] == 'M01')
        # U = 0.6*cl((3+5)/15) + 0.4*1 ; S = 0.6*cl(1 + (-1)/10) + 0.4*cl(1 + 2/20 -> 1) ; skor = 100*U*S*min(1, 2/5)
        U = 0.6 * (8 / 15) + 0.4; S = 0.6 * 0.9 + 0.4
        self.assertAlmostEqual(m01['skor'], round(100 * U * S * 0.4, 1))

    def test_cli(self):
        d = tempfile.mkdtemp()
        for nm, rows in (('out_moomoo.json', M), ('out_claude.json', C), ('out_mae.json', {})):
            with open(os.path.join(d, nm), 'w') as f:
                json.dump({'rows': rows}, f)
        papan = os.path.join(d, 'papan.json')
        with open(papan, 'w') as f:
            json.dump({'rows': [{'id': 'M01', 'pantau': 'BELUM CUKUP', 'status': 'BELUM CUKUP'}]}, f)
        import contextlib, io
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(HP.main([d, '--papan', papan]), 0)
        with open(os.path.join(d, 'out_prestasi.json')) as f:
            out = json.load(f)
        self.assertIn('dibersarakan', out['label_s7'])
        self.assertEqual(out['Combine']['kpi']['dagangan'], 3)
        self.assertEqual(out['C']['kaedah'][0]['keputusan'], 'dibersarakan')


if __name__ == '__main__':
    unittest.main()
