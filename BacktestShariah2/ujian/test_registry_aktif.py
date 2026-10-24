# Ujian standard/registry_aktif.py (audit dashboard 24 Okt 2026, item 26): dokumen db registry/aktif = varian aktif sahaja,
# langkah corong selaras dengan Papan Penganalisis (s14_atasi_ew, wfo_lulus, at_lulus), swing 3–30 hari, saiz < 250,000 bait.
import csv, json, os, sys, tempfile, unittest

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'standard'))
import registry_aktif as RA  # noqa: E402

LAJUR = ['set', 'id', 'kaedah', 'varian', 'tarikh', 'keputusan', 'skor', 'cagr', 'mdd', 'h1', 'h2', 'n', 'dagangan_setahun', 'win',
         'avg', 'avgwin', 'avgloss', 'days', 'hit10', 'gate_gagal', 'ew_cagr', 'menang_ew']


def baris(st, mid, var, **k):
    r = dict(set=st, id=mid, kaedah='K ' + mid, varian=var, tarikh='2026-10-05', keputusan='SIMPAN', skor='60', cagr='0.3', mdd='-0.2',
             h1='0.1', h2='0.2', n='500', dagangan_setahun='70', win='0.5', avg='0.02', avgwin='0.08', avgloss='-0.04', days='10',
             hit10='0.3', gate_gagal='', ew_cagr='0.2191', menang_ew='False')
    r.update({a: str(b) for a, b in k.items()})
    return r


def tulis_json(p, d):
    with open(p, 'w', encoding='utf-8') as f:
        json.dump(d, f)


class UjiRegistryAktif(unittest.TestCase):
    def test_fixture(self):
        with tempfile.TemporaryDirectory() as d:
            kat = os.path.join(d, 'katalog.json')
            tulis_json(kat, dict(rows=[dict(id='M01', nama='Satu', varian_kod='V1 aktif'), dict(id='M02', nama='Dua', varian_kod='V0')]))
            reg = os.path.join(d, 'registry.csv')
            rows = [baris('431', 'M01', 'V1 aktif', days='12.34', gate_gagal='G5', tarikh='2026-10-16'),
                    baris('431', 'M01', 'V0 lama', cagr='0.9'),                       # varian tidak aktif: tidak dimuat
                    baris('431', 'M02', 'V0', days='45', keputusan='DITOLAK', skor='')]
            rows += [baris(s, 'M01', 'V1 aktif', menang_ew=m) for s, m in zip(['S1', 'S2', 'S3', 'S4'], [True, True, True, False])]
            rows += [baris(s, 'M02', 'V0', menang_ew=m) for s, m in zip(['S1', 'S2', 'S3', 'S4'], [True, True, False, False])]
            with open(reg, 'w', newline='', encoding='utf-8') as f:
                w = csv.DictWriter(f, fieldnames=LAJUR); w.writeheader(); w.writerows(rows)
            wfo = os.path.join(d, 'wfo'); os.makedirs(wfo)
            tulis_json(os.path.join(wfo, 'M01.json'), dict(id='M01', status='SIAP', oos=dict(cagr=0.2, n=50), ew=dict(cagr=0.1)))
            at = os.path.join(d, 'papan.json')
            tulis_json(at, dict(dijana='2026-10-18T05:10Z', kaedah=[
                dict(id='M01', label='RENDAH', cagr_a=0.2, spy_a=0.1, cagr_b=0.05, spy_b=0.1),
                dict(id='M02', label='TINGGI', cagr_a=0.3, spy_a=0.1, cagr_b=0.3, spy_b=0.1)]))
            doc = RA.dokumen('x', katalog=kat, registry=reg, wfo=wfo, autotune=at)
        r1, r2 = doc['rows']
        self.assertEqual(list(r1), RA.MEDAN)
        self.assertEqual((r1['varian'], r1['cagr'], r1['days'], r1['gate_gagal'], r1['h2']), ('V1 aktif', 0.3, 12.3, 'G5', 0.2))
        self.assertEqual((r1['s14_menang'], r1['s14_n'], r1['s14_atasi_ew'], r1['wfo_lulus'], r1['at_lulus']), (3, 4, True, True, False))
        self.assertTrue(r1['swing'])
        self.assertEqual((r2['s14_atasi_ew'], r2['wfo_lulus'], r2['at_lulus'], r2['swing'], r2['skor']), (False, None, True, False, None))
        self.assertEqual(doc['kiraan'], dict(kaedah=2, swing=1, s14_atasi_ew=1, wfo_lulus=1, at_lulus=1, tiada_registry=0))
        self.assertEqual((doc['tarikh_registry'], doc['tarikh_autotune'], doc['ew_cagr']), ('2026-10-16', '2026-10-18T05:10Z', 0.2191))

    def test_data_repo(self):
        if not os.path.exists(RA.PA.REGISTRY):
            self.skipTest('registry tiada')
        doc = RA.dokumen('x')
        kat = RA.PA.muat_katalog()
        self.assertEqual([(r['id'], r['varian']) for r in doc['rows']], [(i, v) for i, _, v in kat])
        self.assertTrue(all(r['id'].startswith('M') for r in doc['rows']))
        self.assertEqual(doc['kiraan']['tiada_registry'], 0)
        self.assertLess(len(RA.padat(doc).encode()), RA.HAD_BAIT)


if __name__ == '__main__':
    unittest.main()
