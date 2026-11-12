"""Kohort KOMBINASI MA50 (N201X36-N204X36): kontrak jejak hadapan 12 Nov 2026.

Pradaftar `kajian/SPEC_JEJAK_KOMBINASI.md`. Kohort ini BUKAN daripada grid REVERSE, jadi ujian
pariti `test_nxx_sepadan.py` (terhadap `step18`) tidak meliputinya. Ujian ini mengunci perkara
yang sama dengan cara lain:

1. PARITI - topeng produksi sama bit-untuk-bit dengan transkripsi bebas formula tinjauan
   (ditulis semula di sini tanpa mengimport `_kombo`), pada harga sebenar.
2. TIADA PANDANG-HADAPAN - isyarat pada bar t tidak berubah apabila bar selepas t dibuang.
3. STRUKTUR - tiada henti, tiada sasaran, keluar = X36 yang sama dengan 94 kohort Nxx,
   `tutup > ma50` pada setiap isyarat, rank berterusan.
4. PENYEBUT KAD SKOR - tarikh LANGSUNG kohort ialah 2026-11-12, bukan tarikh keluarga N.
"""
import importlib
import os
import sys
import unittest

import numpy as np
import pandas as pd

BS2 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BS2, 'kod'))
sys.path.insert(0, os.path.join(BS2, 'kod', 'kaedah'))
sys.path.insert(0, os.path.join(BS2, 'standard'))

import kaedah._kombo as KB       # noqa: E402
import kaedah._nxx as NX         # noqa: E402

STOR = os.path.join(BS2, 'data', 'harga', 'stor', 'harga_A.csv')
KOHORT = ('N201X36', 'N202X36', 'N203X36', 'N204X36')
N_TICKER = 30
MIN_BAR = 300


def _harga():
    H = pd.read_csv(STOR)
    H['date'] = pd.to_datetime(H.date.astype(str), format='%Y%m%d')
    out = []
    for t in sorted(H.ticker.unique()):
        g = (H[H.ticker == t].sort_values('date').set_index('date')
             [['open', 'high', 'low', 'close', 'volume']].astype('float64'))
        if len(g) >= MIN_BAR:
            out.append((t, g))
        if len(out) >= N_TICKER:
            break
    return out


def _rujukan(g):
    """Transkripsi BEBAS formula tinjauan (`kajian/isyarat_kombinasi/panel.py`), gelung numpy.

    Sengaja ditulis dengan cara berbeza daripada `_kombo` (gelung tingkap eksplisit, bukan
    `rolling().max()`), supaya kesilapan yang sama tidak boleh berada dalam kedua-duanya.
    """
    o, h, c = g.open.to_numpy(), g.high.to_numpy(), g.close.to_numpy()
    n = len(g)
    cs = pd.Series(c)

    def rsi(k):
        d = cs.diff()
        up = d.clip(lower=0).ewm(alpha=1 / k, adjust=False, min_periods=k).mean()
        dn = (-d).clip(lower=0).ewm(alpha=1 / k, adjust=False, min_periods=k).mean()
        return (100 - 100 / (1 + up / dn.replace(0, np.nan))).to_numpy()

    ma = {k: cs.rolling(k).mean().to_numpy() for k in (20, 50, 200)}
    r2, r14 = rsi(2), rsi(14)
    atas50 = c > ma[50]
    gap = np.zeros(n, bool); s2050 = np.zeros(n, bool); s50 = np.zeros(n, bool); undur = np.zeros(n, bool)
    for i in range(1, n):
        gap[i] = o[i] > h[i - 1] * 1.02
        s2050[i] = ma[20][i] > ma[50][i] and ma[20][i - 1] <= ma[50][i - 1]
        s50[i] = r14[i] > 50 and r14[i - 1] <= 50
        undur[i] = r2[i] < 10 and r2[i - 1] >= 10

    def dalam(ev, k):
        return np.array([ev[max(0, i - k + 1):i + 1].any() for i in range(n)])

    l2 = gap & dalam(undur, 5)
    with np.errstate(invalid='ignore'):
        return {'n201': s2050 & atas50,
                'n202': (r2 < 10) & (c > ma[200]) & atas50,
                'n203': s2050 & dalam(gap, 10) & atas50,
                'n204': s50 & dalam(l2, 5) & atas50}


@unittest.skipUnless(os.path.exists(STOR), 'stor harga tiada')
class TestKomboMA50(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.H = _harga()
        if not cls.H:
            raise unittest.SkipTest('tiada ticker dengan bar cukup')

    def test_topeng_identik_dengan_transkripsi_bebas(self):
        jum = {k: 0 for k in KB.TOPENG}
        for t, g in self.H:
            d = KB.asas(g); ref = _rujukan(g)
            for k, fn in KB.TOPENG.items():
                x = fn(d, g).fillna(False).astype(bool).to_numpy()
                self.assertEqual(int((x != ref[k]).sum()), 0, f'{t} {k}: topeng terpesong')
                jum[k] += int(x.sum())
        for k, v in jum.items():
            self.assertGreater(v, 0, f'{k}: SIFAR isyarat rujukan - ujian sia-sia')

    def test_tiada_pandang_hadapan(self):
        """Isyarat pada bar t mesti sama sama ada bar selepas t wujud atau tidak."""
        for t, g in self.H[:10]:
            penuh = {k: fn(KB.asas(g), g).fillna(False).astype(bool) for k, fn in KB.TOPENG.items()}
            for potong in (len(g) - 1, len(g) - 7, len(g) - 40):
                gp = g.iloc[:potong]
                dp = KB.asas(gp)
                for k, fn in KB.TOPENG.items():
                    a = fn(dp, gp).fillna(False).astype(bool)
                    self.assertTrue(bool(a.equals(penuh[k].iloc[:potong])), f'{t} {k} potong {potong}')

    def test_syarat_terurai_sama_dengan_topeng(self):
        """DAN semua syarat atom watchlist = topeng masuk, pada setiap bar."""
        for t, g in self.H:
            d = KB.asas(g)
            for k, fn in KB.TOPENG.items():
                dan = pd.Series(True, index=g.index)
                for _, kon, _ in KB.SYARAT[k](d, g):
                    dan &= kon.fillna(False).astype(bool)
                x = fn(d, g).fillna(False).astype(bool)
                self.assertEqual(int((dan != x).sum()), 0, f'{t} {k}: penguraian terpesong')

    def test_modul_tiada_henti_keluar_x36(self):
        fr0 = {t: g for t, g in self.H}
        for mid in KOHORT:
            m = importlib.import_module(f'kaedah.{mid}')
            self.assertEqual(m.ID, mid)
            self.assertFalse(m.ADA_HENTI, mid)
            self.assertFalse(m.SILANG, mid)
            self.assertEqual(m.TMAX, NX.IMBAS, mid)
            fr = {t: g.copy() for t, g in fr0.items()}
            m.sedia(fr, {})
            n = 0
            for t, g in fr.items():
                self.assertTrue(bool(g.stop.isna().all()), f'{mid} {t}: stop bukan NaN')
                self.assertTrue(bool(g.tgt.isna().all()), f'{mid} {t}: tgt bukan NaN')
                f = NX.indikator(fr0[t])
                x36 = NX.x36(f, fr0[t]).fillna(False).astype(bool)
                self.assertTrue(bool(g.exitc.astype(bool).equals(x36)), f'{mid} {t}: keluar bukan X36')
                sig = g.sig.astype(bool)
                self.assertTrue(bool((fr0[t].close[sig] > f.ma50[sig]).all()), f'{mid} {t}: isyarat bawah ma50')
                rk = g['rank'][sig & (g['rank'] > -9e8)]
                self.assertTrue(bool(np.isfinite(rk).all()), f'{mid} {t}: rank tidak terhingga')
                n += int(sig.sum())
            self.assertGreater(n, 0, f'{mid}: tiada isyarat pada {len(fr)} ticker')

    def test_hampir_tidak_pernah_melaporkan_isyarat(self):
        """hampir() = sebahagian syarat sahaja; bar yang sudah isyarat mesti pulang None."""
        for mid in KOHORT:
            m = importlib.import_module(f'kaedah.{mid}')
            for t, g in self.H[:12]:
                d = KB.asas(g)
                sig = bool(KB.TOPENG[mid[:4].lower()](d, g).fillna(False).iloc[-1])
                r = m.hampir(g, {})
                if sig:
                    self.assertIsNone(r, f'{mid} {t}')
                elif r is not None:
                    self.assertIsNone(r['paras'], f'{mid} {t}')
                    self.assertIn('/', r['syarat_dipenuhi'])

    def test_bingkai_pendek_selamat(self):
        t, g = self.H[0]
        for n in (1, 2, 30, 199, 201, 253):
            for mid in KOHORT:
                m = importlib.import_module(f'kaedah.{mid}')
                fr = {t: g.iloc[:n].copy()}
                m.sedia(fr, {})
                self.assertEqual(len(fr[t]), n)
                self.assertLess(n, m.PERLU_BAR)
                self.assertIsNone(m.hampir(g.iloc[:n], {}), f'{mid} n={n}')


class TestKunciKohort(unittest.TestCase):
    """Parameter pradaftar `kajian/SPEC_JEJAK_KOMBINASI.md`; mengubahnya = kaedah lain."""

    def test_parameter(self):
        self.assertEqual(KB.KOHORT, KOHORT)
        self.assertEqual(KB.KELUAR, 'X36')
        self.assertEqual(KB.GAP_MIN, 1.02)
        self.assertEqual(KB.TINGKAP_GAP, 10)
        self.assertEqual(KB.TINGKAP_LANGKAH, 5)
        self.assertEqual(KB.MULA_LANGSUNG, '2026-11-12')

    def test_tarikh_langsung_kohort(self):
        import lift_kaedah as LK
        self.assertEqual(LK.MULA_KOHORT, {m: '2026-11-12' for m in KOHORT})
        for mid in KOHORT:
            self.assertEqual(LK.mula_langsung(mid), KB.MULA_LANGSUNG, mid)
        # keluarga sedia ada tidak tersentuh
        self.assertEqual(LK.mula_langsung('N19X13'), '2026-11-03')
        self.assertEqual(LK.mula_langsung('N06X36'), '2026-11-03')
        self.assertEqual(LK.mula_langsung('M15'), '2026-10-15')
        P = pd.DataFrame(dict(id_kaedah=['N203X36', 'N203X36', 'N76X36'],
                              tarikh_isyarat=['2026-11-05', '2026-11-12', '2026-11-05']))
        self.assertEqual(list(LK.langsung(P)), [False, True, True])

    def test_spec_dan_keputusan_wujud(self):
        with open(os.path.join(BS2, 'kajian', 'SPEC_JEJAK_KOMBINASI.md'), encoding='utf-8') as f:
            s = f.read()
        for t in KOHORT + ('Dipradaftar 12 Nov 2026', 'X36', 'N76X36', 'N06X36', '2026-11-12'):
            self.assertIn(t, s)
        with open(os.path.join(BS2, 'standard', 'SPEC_KAD_SKOR.md'), encoding='utf-8') as f:
            self.assertIn('Pindaan 12 Nov 2026', f.read())
        with open(os.path.join(BS2, 'koordinator', 'keputusan.csv'), encoding='utf-8') as f:
            self.assertIn('N201X36', f.read())


if __name__ == '__main__':
    unittest.main()
