import os, sys, tempfile, unittest

import pandas as pd

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'standard'))
import penanda_ew as PE  # noqa: E402


def _stor(folder):
    a = pd.DataFrame([
        ('AAA', 20261020, 10, 11, 9, 10, 1), ('AAA', 20261021, 10, 12, 10, 11, 1), ('AAA', 20261022, 11, 12, 10, 11, 1),
        ('BBB', 20261020, 20, 21, 19, 20, 1), ('BBB', 20261021, 20, 21, 17, 18, 1), ('BBB', 20261022, 18, 20, 18, 19.8, 1),
        ('CCC', 20261020, 5, 5, 5, 5, 1), ('CCC', 20261021, 5, 9, 5, 9, 1), ('CCC', 20261022, 9, 9, 9, 9, 1),   # < USD10
        ('ZZZ', 20261020, 50, 50, 50, 50, 1), ('ZZZ', 20261021, 50, 99, 50, 99, 1), ('ZZZ', 20261022, 99, 99, 99, 99, 1),  # bukan univ
    ], columns=PE.pd.Index(['ticker', 'date', 'open', 'high', 'low', 'close', 'volume']))
    a.to_csv(os.path.join(folder, 'harga_A.csv'), index=False)
    pd.DataFrame([('SPY', 20261020, 100, 100, 100, 100, 1), ('SPY', 20261021, 100, 102, 100, 101, 1),
                  ('SPY', 20261022, 101, 102, 100, 100, 1)], columns=a.columns).to_csv(os.path.join(folder, 'harga_idx.csv'), index=False)
    with open(os.path.join(folder, 'univ.txt'), 'w') as f:
        f.write('AAA\nBBB\nCCC\n')


class TestPenandaEw(unittest.TestCase):
    def test_bina_dan_tempoh(self):
        with tempfile.TemporaryDirectory() as d:
            _stor(d)
            PE.N_MIN = 1
            ew = PE.bina(d, os.path.join(d, 'univ.txt'))
            # 21 Okt: AAA +10%, BBB -10%; CCC tutup semalam < 10 (tidak dikira); ZZZ bukan alam
            self.assertAlmostEqual(ew.loc['2026-10-21', 'ew_cc'], 0.0)
            self.assertEqual(int(ew.loc['2026-10-21', 'n']), 2)
            # 22 Okt: AAA 0%, BBB +10%, CCC tutup semalam 9 < 10 (tidak dikira)
            self.assertAlmostEqual(ew.loc['2026-10-22', 'ew_cc'], 0.05)
            # beli buka 21 Okt, nilai tutup 22 Okt: oc 21 Okt = mean(+10%, -10%) = 0; cc 22 Okt = +5%
            self.assertAlmostEqual(PE.tempoh(ew, '2026-10-21', '2026-10-22'), 0.05)
            self.assertAlmostEqual(PE.tempoh(ew, '2026-10-21', '2026-10-22', 'spy'), (1 + 0.01) * (1 + (100 / 101 - 1)) - 1)
            self.assertIsNone(PE.tempoh(ew, '2026-10-22', '2026-10-21'))


if __name__ == '__main__':
    unittest.main()
