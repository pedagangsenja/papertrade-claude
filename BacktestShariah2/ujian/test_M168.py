# Ujian modul M168 (Pulih MACD + Silang SMA10/20, teknik manual pengguna; pratonton 25 Okt 2026): rujukan gelung bebas bagi
# sig/henti, tiada pandang depan (sedia() atas data dipotong = data penuh hingga tarikh potong), modul di luar imbasan harian
# semasa moratorium, laluan enjin v1.2 (masuk buka esok, keluar buka esok selepas silang bawah) dan status posisi manual DCI/MGA
# (moomoo.csv). Modul: WFO/kaedah_baru/M168.py (moratorium) atau kod/kaedah/M168.py (selepas diaktifkan).
import csv, json, math, os, sys, unittest
import numpy as np, pandas as pd

BS2 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO = os.path.dirname(BS2)
sys.path.insert(0, os.path.join(BS2, 'kod'))
sys.path.insert(1, os.path.join(REPO, 'WFO', 'kaedah_baru'))
import enjin  # noqa: E402
try:
    from kaedah import M168 as M  # noqa: E402
except ImportError:
    import M168 as M  # noqa: E402

V1 = 'V1 Utama J20 D10 K10 (tiada henti)'
V1H = 'V1H Utama J20 D10 K10 + henti kecemasan'


def jalan_rawak(benih, n=700, vol=0.022):
    r = np.random.default_rng(benih)
    c = 50 * np.cumprod(1 + r.normal(0.0004, vol, n)); o = np.r_[c[0], c[:-1]] * (1 + r.normal(0, 0.004, n))
    h = np.maximum(o, c) * (1 + np.abs(r.normal(0, 0.008, n))); l = np.minimum(o, c) * (1 - np.abs(r.normal(0, 0.008, n)))
    return pd.DataFrame(dict(open=o, high=h, low=l, close=c, volume=1e6, turnover=5e7), index=pd.bdate_range('2023-01-02', periods=n))


def rujukan(g, J, D, K, henti):
    """Pelaksanaan gelung bebas (tanpa rolling pandas) bagi varian 'penuh'. Pulang (sig, stop)."""
    o, h, l, c = (g[k].values.astype(float) for k in ('open', 'high', 'low', 'close'))
    n = len(c); W = math.ceil(1.5 * J)
    s10 = [np.nan if i < 9 else sum(c[i - 9:i + 1]) / 10 for i in range(n)]
    s20 = [np.nan if i < 19 else sum(c[i - 19:i + 1]) / 20 for i in range(n)]

    def ema(x, k):
        a = 2 / (k + 1); out = [x[0]]
        for v in x[1:]:
            out.append(a * v + (1 - a) * out[-1])
        return out
    e12, e26 = ema(list(c), 12), ema(list(c), 26)
    m = [a - b for a, b in zip(e12, e26)]; s = ema(m, 9); hist = [a - b for a, b in zip(m, s)]
    qa = [False] * n
    for i in range(1, n):
        if not (hist[i] > 0 and hist[i - 1] <= 0) or i < 59 or i - W + 1 < 19:
            continue
        bawah = sum(1 for j in range(i - W + 1, i + 1) if s10[j] < s20[j])
        qa[i] = bawah >= J and c[i] <= (1 - D) * max(h[i - 59:i + 1])
    sig = [False] * n; stop = [np.nan] * n
    for b in range(20, n):
        if not (s10[b] > s20[b] and s10[b - 1] <= s20[b - 1]):
            continue
        a = [i for i in range(max(0, b - K), b + 1) if qa[i]]
        if not a:
            continue
        sig[b] = True
        if henti:
            stop[b] = 0.99 * min(l[max(0, a[-1] - W + 1):b + 1])
            if b + 1 < n and o[b + 1] <= stop[b]:
                sig[b] = False
    return np.array(sig), np.array(stop)


class TestM168(unittest.TestCase):
    def test_varian(self):
        self.assertEqual(len(M.VARIAN_SEMUA), 38)
        self.assertIn(M.VARIAN, M.VARIAN_SEMUA)
        p = M.VARIAN_SEMUA[M.VARIAN]
        self.assertEqual((p['mod'], p['J'], p['D'], p['K'], p['henti']), ('penuh', 20, 0.10, 10, False))
        self.assertFalse(M.ADA_HENTI); self.assertIsNone(M.TMAX)
        self.assertEqual([M.tetingkap(j) for j in (15, 20, 30)], [23, 30, 45])
        self.assertIsNone(M.hampir(jalan_rawak(1), {}))

    def test_rujukan_gelung(self):
        jumlah = 0
        for benih in range(6):
            for nm, (J, D, K, henti) in [(V1, (20, 0.10, 10, False)), (V1H, (20, 0.10, 10, True)),
                                         ('V7 J15 D20 K20 (tiada henti)', (15, 0.20, 20, False)),
                                         ('V16H J30 D15 K20 + henti kecemasan', (30, 0.15, 20, True))]:
                self.assertEqual(M.VARIAN_SEMUA[nm], dict(mod='penuh', J=J, D=D, K=K, henti=henti), nm)
                g = jalan_rawak(benih); M.sedia({'X': g}, {}, varian=nm)
                sig, stop = rujukan(g, J, D, K, henti)
                np.testing.assert_array_equal(g.sig.values, sig, err_msg=f'{nm} benih {benih}')
                if henti:
                    np.testing.assert_allclose(g.stop.values[sig], stop[sig], rtol=1e-12)
                else:
                    self.assertTrue(g.stop.isna().all())
                jumlah += int(sig.sum())
        self.assertGreater(jumlah, 10)      # data rawak benar-benar menghasilkan isyarat

    def test_tiada_pandang_depan(self):
        for nm in [V1, V1H, 'V0a Kawalan silang SMA10/20 sahaja', 'V0b Kawalan alert MACD + silang K10 (tanpa syarat jatuh)']:
            penuh = jalan_rawak(3); M.sedia({'X': penuh}, {}, varian=nm)
            for k in (260, 333, 401, 555, 699):
                g = jalan_rawak(3).iloc[:k + 1].copy(); M.sedia({'X': g}, {}, varian=nm)
                ref = penuh.iloc[:k + 1]
                # sig bar terakhir data dipotong: buka esok belum diketahui, jadi langkau 'buka <= henti' belum dinilai
                np.testing.assert_array_equal(g.sig.values[:-1], ref.sig.values[:-1], err_msg=f'{nm} @ {k}')
                if not M.VARIAN_SEMUA[nm]['henti']:
                    self.assertEqual(bool(g.sig.iloc[-1]), bool(ref.sig.iloc[-1]))
                elif ref.sig.iloc[-1]:
                    self.assertTrue(g.sig.iloc[-1])
                for kol in ('exitc', 'stop', 'rank', '_s10', '_s20', '_hist'):
                    np.testing.assert_array_equal(g[kol].values, ref[kol].values, err_msg=f'{nm} {kol} @ {k}')

    def test_moratorium_di_luar_imbasan(self):
        """Selagi katalog tiada M168, modul mesti di luar kod/kaedah/ (scanner/harian_c/lejar mengimbas semua kaedah/M*.py)."""
        with open(os.path.join(BS2, 'standard', 'katalog_kaedah.json'), encoding='utf-8') as f:
            dalam_katalog = any(r['id'] == 'M168' for r in json.load(f)['rows'])
        self.assertEqual(os.path.exists(os.path.join(BS2, 'kod', 'kaedah', 'M168.py')), dalam_katalog)
        g = jalan_rawak(2); M.sedia({'X': g}, {})
        self.assertTrue(g.sig.any()); self.assertTrue(g.exitc.any())

    def test_enjin_masuk_dan_keluar_buka_esok(self):
        g = jalan_rawak(4); M.sedia({'X': g}, {}, varian=V1)
        T = enjin.trades({'X': g}, tmax=M.TMAX, warm=M.WARM)
        self.assertGreater(len(T), 0)
        ix = g.index
        for r in T.itertuples():
            i = ix.get_loc(r.sig); j = ix.get_loc(r.ex)
            self.assertTrue(g.sig.iloc[i]); self.assertEqual(ix[i + 1], r.ent)
            if r.why == 'isyarat keluar':
                self.assertTrue(g.exitc.iloc[j - 1])            # silang bawah pada tutup j-1 -> jual buka j
                self.assertFalse(g.exitc.iloc[i + 1:j - 1].any())
                e = g.open.iloc[i + 1]; x = g.open.iloc[j]
                self.assertAlmostEqual(r.ret, x / e * (1 - enjin.COST) / (1 + enjin.COST) - 1)
            else:
                self.assertEqual(r.why, 'hujung')

    def test_paras_silang_bawah(self):
        g = jalan_rawak(5, n=60)
        x = M.paras_silang_bawah(g)
        for d in (-1e-6, 1e-6):
            c = np.r_[g.close.values, x + d]
            s10, s20 = c[-10:].mean(), c[-20:].mean()
            self.assertEqual(s10 < s20, d < 0)
        self.assertIsNone(M.paras_silang_bawah(g.iloc[:19]))

    def test_posisi_manual_dci_mga(self):
        """Tutup harian DCI dan MGA 8 Sep – 23 Okt 2026 (stor repo = kline Moomoo terlaras hadapan, disemak 25 Okt 2026).
           Peraturan keluar M168: SMA10 tutup silang bawah SMA20 -> jual buka esok. DCI: silang bawah 20 Okt (jual buka 21 Okt
           88.09); MGA: tiada silang bawah sejak beli 6 Okt hingga 23 Okt."""
        tarikh = pd.bdate_range('2026-09-08', '2026-10-23')       # tiada cuti bursa AS dalam tempoh ini
        self.assertEqual(len(tarikh), 34)
        dci = [90.99, 89.81, 88.18, 89.25, 87.93, 87.06, 86.33, 86.05, 86.44, 86.07,
               86.05, 86.74, 86.6, 87.41, 87.48, 87.31, 87.04, 87.76, 88.65, 89.19, 90.11, 87.26, 87.16, 86.93, 86.47, 87.16, 87.21,
               87.77, 87.97, 87.32, 87.6, 88.65, 86.12, 84.79]
        mga = [66.56, 65.47, 65.14, 66.13, 64.89, 63.42, 63.74, 64.82, 63.15, 63.01,
               63.79, 63.73, 62.22, 65.0, 64.64, 64.56, 63.67, 64.46, 64.57, 64.92, 65.66, 65.03, 63.82, 63.99, 63.56, 65.31, 64.45,
               66.41, 65.99, 65.43, 66.39, 63.83, 64.72, 63.97]
        for nama, c, jangka in [('DCI', dci, ['2026-10-20']), ('MGA', mga, [])]:
            g = pd.DataFrame(dict(open=c, high=c, low=c, close=c, volume=1e6, turnover=1e8), index=tarikh)
            M.sedia({nama: g}, {})
            self.assertFalse(np.isnan(g._s20.loc['2026-10-05']))   # SMA20 sah sebelum hari beli
            x = g.exitc[g.index >= '2026-10-06']
            self.assertEqual([str(d.date()) for d in x.index[x]], jangka, nama)
        # moomoo.csv: baris MANUAL kekal "Pegang (luar M ..." (status_pegang harian_c.py mengekalkan awalan ini) dan nota mencatat
        # status peraturan keluar M168
        p = os.path.join(BS2, 'papertrade', 'moomoo.csv')
        if not os.path.exists(p):
            self.skipTest('moomoo.csv tiada')
        rows = {r['saham']: r for r in csv.DictReader(open(p, newline='', encoding='utf-8')) if r['kaedah'] == 'MANUAL'}
        for t in ('DCI', 'MGA'):
            self.assertTrue(rows[t]['isyarat_keluar'].startswith('Pegang (luar'), t)
            self.assertIn('M168', rows[t]['nota'], t)
        self.assertIn('2026-10-21', rows['DCI']['isyarat_keluar'])
        self.assertIn('88.09', rows['DCI']['isyarat_keluar'])


if __name__ == '__main__':
    unittest.main()
