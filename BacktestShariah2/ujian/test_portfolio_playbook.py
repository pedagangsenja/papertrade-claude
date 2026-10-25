# Ujian PLAYBOOK_10 / RAWAK_PADAN_10 (standard/portfolio_slot.py; pra-daftar kajian/portfolio/PRA_DAFTAR_PLAYBOOK.md):
# penapis P1–P11, earnings, susunan RS + seri rawak berbenih, saiz risiko 1% (had 15%), heat, had sektor/industri/belian
# sehari, Chandelier, henti masa, brek, kill_switch, delist, kos 0.25%, rekod beku, perincian risiko semua portfolio.
import os, sys, tempfile, unittest
import numpy as np, pandas as pd

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'standard'))
import portfolio_slot as ps

FJ = (1 - 0.0025) / (1 + 0.0025)
HARI = [d.strftime('%Y-%m-%d') for d in pd.bdate_range('2026-09-01', periods=80)]
B0 = 30                                     # sesi beli pertama dalam ujian (sejarah 30 bar untuk ATR14)


def siri(tutup, mula=0, julat=1.0, buka=None):
    """Siri harga: tutup[i] bagi HARI[mula + i]; tinggi/rendah = tutup ± julat/2 (ATR14 = julat apabila tutup rata)."""
    c = np.asarray(tutup, float); ix = pd.to_datetime(HARI[mula:mula + len(c)])
    o = c if buka is None else np.asarray(buka, float)
    return ps.Siri(pd.DataFrame(dict(open=o, high=np.maximum(o, c) + julat / 2, low=np.minimum(o, c) - julat / 2, close=c), index=ix))


def rata(n=80, v=100.0):
    return [v] * n


def calon(rows):
    """rows: dict(saham, beli (indeks HARI), r (r_awal), rs, sektor, industri)."""
    out = []
    for r in rows:
        b = HARI[r.get('beli', B0)]
        out.append(dict(saham=r['saham'], tarikh_beli=b, tarikh_isyarat=HARI[r.get('beli', B0) - 1], id_kaedah='M01',
                        rs=r.get('rs', 90), harga_beli=r.get('hb', 100.0), r_awal=r.get('r', 0.04),
                        sektor_us=r.get('sektor', r['saham']), industri_us=r.get('industri', r['saham'])))
    return pd.DataFrame(out)


class TestPenapis(unittest.TestCase):
    def lulus(self):
        return dict(tutup=50.0, nilai_med=30e6, n_bar=300, semak_data=False, ambil_alih=False, rs=85, sma50=48, sma150=45,
                    sma200=40, sma200_lalu=39, tinggi52=55, gred_industri='C', atr_pct=0.03, jurang=0.01, earnings='tiada',
                    spy_atas=True, r_awal=0.1)

    def test_setiap_penapis(self):
        ubah = {'harga': dict(tutup=9.99, sma50=9, sma150=8, sma200=7, sma200_lalu=6, tinggi52=10),
                'kecairan': dict(nilai_med=19.9e6), 'sejarah': dict(n_bar=251), 'sah': dict(semak_data=True),
                'rs': dict(rs=95), 'trend': dict(sma200_lalu=41), 'industri': dict(gred_industri='E'),
                'atr': dict(atr_pct=0.061), 'jurang': dict(jurang=0.031), 'earnings': dict(earnings='tidak diketahui'),
                'rejim': dict(spy_atas=False), 'paras': dict(r_awal=0.0)}
        X = pd.DataFrame([self.lulus()] + [dict(self.lulus(), **v) for v in ubah.values()])
        G = ps.tapis_pb(X)
        self.assertFalse(G.iloc[0].any())
        for i, k in enumerate(ubah, 1):
            self.assertEqual(list(G.columns[G.iloc[i]]), [k], k)

    def test_had_sempadan_dan_nilai_tiada(self):
        X = pd.DataFrame([dict(self.lulus(), rs=80), dict(self.lulus(), rs=94), dict(self.lulus(), tinggi52=58.8),   # 50 >= 0.85 x 58.8
                          dict(self.lulus(), tinggi52=58.9), dict(self.lulus(), ambil_alih=True), dict(self.lulus(), gred_industri=''),
                          dict(self.lulus(), atr_pct=np.nan, semak_data=np.nan)])
        G = ps.tapis_pb(X)
        self.assertEqual([bool(x) for x in G.any(axis=1)], [False, False, False, True, True, True, True])
        self.assertTrue(G.loc[3, 'trend'] and G.loc[4, 'sah'] and G.loc[5, 'industri'] and G.loc[6, 'atr'] and G.loc[6, 'sah'])

    def test_ciri_siri(self):
        n = 300; c = np.linspace(50, 80, n)
        g = pd.DataFrame(dict(open=c, high=c + 1, low=c - 1, close=c, volume=1e6), index=pd.bdate_range('2025-01-01', periods=n))
        f = ps.ciri_siri(g)
        self.assertAlmostEqual(f.sma50.iloc[-1], c[-50:].mean()); self.assertAlmostEqual(f.tinggi52.iloc[-1], c[-252:].max() + 1)
        self.assertEqual(f.n_bar.iloc[-1], n); self.assertFalse(f.semak_data.iloc[-1])
        self.assertAlmostEqual(f.nilai_med.iloc[-1], np.median(c[-20:] * 1e6))
        c2 = c.copy(); c2[-30] = c2[-31] * 1.5
        self.assertTrue(ps.ciri_siri(g.assign(close=c2)).semak_data.iloc[-1])    # lonjakan > 40% dalam 60 sesi


class TestEarnings(unittest.TestCase):
    S5 = ['2026-10-16', '2026-10-19', '2026-10-20', '2026-10-21', '2026-10-22']

    def test_masa(self):
        self.assertEqual([ps.masa_earnings(m) for m in ('time-pre-market', 'time-after-hours', 'time-not-supplied', '06:00',
                                                         '16:00', '12:00', None)], ['pra', 'lepas', '', 'pra', 'lepas', '', ''])

    def test_tetingkap_reaksi(self):
        f = lambda d, m: ps.earnings_dekat('2026-10-15', self.S5, [(d, m)])
        self.assertFalse(f('2026-10-15', 'time-pre-market'))      # sudah dalam bar isyarat
        self.assertTrue(f('2026-10-15', 'time-after-hours'))      # reaksi pada sesi beli
        self.assertTrue(f('2026-10-15', 'time-not-supplied'))     # tidak diketahui: kedua-duanya
        self.assertTrue(f('2026-10-22', 'time-pre-market'))
        self.assertFalse(f('2026-10-22', 'time-after-hours'))     # reaksi sesi ke-6
        self.assertTrue(f('2026-10-18', 'time-after-hours'))      # hujung minggu -> Isnin
        self.assertFalse(f('2026-10-14', 'time-after-hours'))

    def test_status_liputan(self):
        from datetime import date
        K = {'A': {date(2026, 11, 20): 'Nasdaq', date(2026, 8, 20): 'Nasdaq'}, 'B': {date(2026, 9, 25): 'Nasdaq'},
             'C': {}, 'D': {date(2026, 10, 19): 'Nasdaq'}}
        nas = dict(dari='2026-07-20', hingga='2026-11-27', saham={'C': {}})
        st = lambda t, n=nas: ps.status_earnings(t, '2026-10-15', self.S5, K, {}, n)
        self.assertEqual([st('A'), st('B'), st('C'), st('C', {}), st('D')], ['tiada', 'tiada', 'tiada', 'tidak diketahui', 'ada'])

    def test_sesi_selepas_sambung_kalendar(self):
        s = ['2026-11-20', '2026-11-23', '2026-11-24']
        x = ps.sesi_selepas('2026-11-20', 5, s)
        self.assertEqual(x[:2], ['2026-11-23', '2026-11-24']); self.assertEqual(len(x), 5)
        if len(ps.cuti_nyse()):
            self.assertEqual(x[2:], ['2026-11-25', '2026-11-27', '2026-11-30'])   # 26 Nov Thanksgiving


class TestEnjin(unittest.TestCase):
    def test_saiz_risiko_dan_had(self):
        C = calon([dict(saham='A', r=0.04), dict(saham='B', r=0.10, rs=88)])
        R, E = ps.bina_pb(C, HARI[B0:B0 + 1], {'A': siri(rata()), 'B': siri(rata())}, 'PLAYBOOK_10')
        a, b = R.set_index('saham').loc['A'], R.set_index('saham').loc['B']
        self.assertAlmostEqual(a.saiz_pct, 15.0)                  # 1% / 4% = 25% -> had 15%
        self.assertAlmostEqual(b.saiz_pct, 10.0)                  # 1% / 10%
        self.assertAlmostEqual(E.tunai.iloc[0], 0.75)
        self.assertEqual(list(R.saham), ['A', 'B'])

    def test_susunan_rs_seri_rawak_tetap(self):
        C = calon([dict(saham=s, rs=rs) for s, rs in [('A', 85), ('B', 90), ('C', 90), ('D', 90), ('E', 92)]])
        G = ps.susun_pb(C, 'PLAYBOOK_10', HARI[B0])
        self.assertEqual(G.saham.iloc[0], 'E'); self.assertEqual(G.saham.iloc[-1], 'A')
        self.assertEqual(set(G.saham.iloc[1:4]), {'B', 'C', 'D'})
        self.assertEqual(list(G.saham), list(ps.susun_pb(C.iloc[::-1], 'PLAYBOOK_10', HARI[B0]).saham))   # tidak bergantung susunan input
        tertib = {tuple(ps.susun_pb(C, 'PLAYBOOK_10', HARI[B0], benih=b).saham.iloc[1:4]) for b in range(30)}
        self.assertGreater(len(tertib), 1)                         # seri dipecah rawak (bukan abjad)
        r = [tuple(ps.susun_pb(C, 'RAWAK_PADAN_10', HARI[B0]).saham) for _ in range(2)]
        self.assertEqual(r[0], r[1])

    def test_had_belian_sehari_sektor_industri_posisi(self):
        rows = [dict(saham=f'S{i}', rs=94 - i, sektor='Tek' if i < 5 else f'X{i}', industri='Semi' if i < 3 else f'I{i}', r=0.5)
                for i in range(8)]
        H = {r['saham']: siri(rata()) for r in rows}
        prm = dict(ps.PB, beli_sehari=50)
        R, _ = ps.bina_pb(calon(rows), HARI[B0:B0 + 1], H, 'PLAYBOOK_10', prm=prm)
        self.assertEqual(list(R.saham), ['S0', 'S1', 'S3', 'S5', 'S6', 'S7'])   # S2: industri Semi ke-3; S4: sektor Tek ke-4
        self.assertEqual((R.sektor_us == 'Tek').sum(), 3); self.assertEqual((R.industri_us == 'Semi').sum(), 2)
        R, _ = ps.bina_pb(calon(rows), HARI[B0:B0 + 2], H, 'PLAYBOOK_10')
        self.assertEqual(len(R), 3)                                 # <= 3 belian sehari
        rows = [dict(saham=f'T{i:02d}', beli=B0 + i // 3, r=0.9) for i in range(66)]
        R, E = ps.bina_pb(calon(rows), HARI[B0:B0 + 30], {r['saham']: siri(rata()) for r in rows}, 'RAWAK_PADAN_10')
        self.assertEqual(E.bil_posisi.max(), 20)                    # maksimum 20 posisi serentak
        self.assertEqual(list(E.bil_posisi[:8]), [3, 6, 9, 12, 15, 18, 20, 20])

    def test_heat_tolak_dan_teruskan(self):
        rows = [dict(saham=f'S{i}', rs=94 - i, r=0.10) for i in range(5)] + [dict(saham='KECIL', rs=80, r=0.002)]
        prm = dict(ps.PB, beli_sehari=50, heat_maks=0.035)
        R, E = ps.bina_pb(calon(rows), HARI[B0:B0 + 1], {r['saham']: siri(rata()) for r in rows}, 'PLAYBOOK_10', prm=prm)
        self.assertEqual(list(R.saham), ['KECIL', 'S0', 'S1', 'S2'])   # S3, S4 melepasi heat; KECIL (risiko 0.03%) masih dibeli
        self.assertAlmostEqual(R.set_index('saham').loc['KECIL'].saiz_pct, 15.0)

    def test_chandelier_sama_lorong2_dan_kos(self):
        c = np.r_[rata(B0), [100, 101, 103, 106, 108, 107, 105, 103, 101, 99, 97, 96, 95, 94, 93, 92]]
        o = np.r_[c[:1], c[:-1]] + 0.3                              # buka berbeza daripada tutup
        sr = siri(c, buka=o); n = len(c)
        R, E = ps.bina_pb(calon([dict(saham='A')]), HARI[B0:n], {'A': sr}, 'PLAYBOOK_10', prm=dict(ps.PB, masa_sesi=999))
        x = ps.KL.lorong_henti(sr.o, sr.c + 0.5 + np.maximum(sr.o - sr.c, 0), sr.c - 0.5 - np.maximum(sr.c - sr.o, 0), sr.c, B0)
        k = R.iloc[0]
        self.assertEqual(x['jenis'], 'keluar')
        self.assertEqual((k.status, k.sebab_keluar, k.tarikh_keluar), ('Keluar', 'chandelier', HARI[x['j']]))
        self.assertAlmostEqual(k.harga_keluar, x['harga'])
        hb = 100.0
        self.assertAlmostEqual(k.untung_pct, 100 * (x['harga'] / hb * FJ - 1))
        self.assertAlmostEqual(k.r_multiple, (x['harga'] / hb * FJ - 1) / 0.04)
        self.assertAlmostEqual(E.ekuiti.iloc[-1], 1 - 0.15 + 0.15 * x['harga'] / hb * FJ)

    def test_henti_masa(self):
        prm = dict(ps.PB, ganda=50.0)
        R, _ = ps.bina_pb(calon([dict(saham='A', r=0.04)]), HARI[B0:B0 + 25], {'A': siri(rata())}, 'PLAYBOOK_10', prm=prm)
        k = R.iloc[0]
        self.assertEqual((k.sebab_keluar, k.tarikh_keluar), ('masa', HARI[B0 + 20]))   # tutup bar ke-20 < 104 -> buka bar ke-21
        naik = rata(B0) + list(np.linspace(100, 106, 25))
        R, _ = ps.bina_pb(calon([dict(saham='A', r=0.04)]), HARI[B0:B0 + 25], {'A': siri(naik)}, 'PLAYBOOK_10', prm=prm)
        self.assertEqual(R.iloc[0].status, 'Pegang')                # >= +1R pada bar ke-20

    def test_brek_dan_pulih(self):
        prm = dict(ps.PB, had=0.5, risiko=1.0, ganda=1000.0, masa_sesi=999, heat_maks=10.0)
        a = rata(B0) + [100, 60, 84, 84, 84]
        rows = [dict(saham='A', r=0.04), dict(saham='B', beli=B0 + 2), dict(saham='C', beli=B0 + 3)]
        R, E = ps.bina_pb(calon(rows), HARI[B0:B0 + 5], {'A': siri(a), 'B': siri(rata()), 'C': siri(rata())}, 'PLAYBOOK_10', prm=prm)
        self.assertEqual(list(E.brek), [0, 1, 0, 0, 0])
        self.assertEqual(set(R.saham), {'A', 'C'})                  # B ditolak (brek), C dibeli selepas pulih ke -8%

    def test_brek_luar_kepekaan_sahaja(self):
        rows = [dict(saham='A'), dict(saham='B', beli=B0 + 1), dict(saham='C', beli=B0 + 2)]
        H = {r['saham']: siri(rata()) for r in rows}
        R, E = ps.bina_pb(calon(rows), HARI[B0:B0 + 3], H, 'PLAYBOOK_10', prm=dict(ps.PB, brek_luar={HARI[B0 + 1]: True}))
        self.assertEqual(set(R.saham), {'A', 'C'}); self.assertEqual(list(E.brek), [0, 1, 0])
        R, _ = ps.bina_pb(calon(rows), HARI[B0:B0 + 3], H, 'PLAYBOOK_10')       # lalai: brek dalaman sahaja
        self.assertEqual(set(R.saham), {'A', 'B', 'C'})

    def test_kill_switch(self):
        prm = dict(ps.PB, had=0.5, risiko=1.0, ganda=1000.0, masa_sesi=999, heat_maks=10.0)
        a = rata(B0) + [100, 40, 50, 60, 70]
        rows = [dict(saham='A', r=0.04), dict(saham='B', beli=B0 + 3)]
        R, E = ps.bina_pb(calon(rows), HARI[B0:B0 + 5], {'A': siri(a, buka=rata(B0) + [100, 40, 45, 60, 70]), 'B': siri(rata())},
                          'PLAYBOOK_10', prm=prm)
        self.assertEqual(ps.bina_pb.bunuh, HARI[B0 + 1])
        k = R.set_index('saham').loc['A']
        self.assertEqual((k.sebab_keluar, k.tarikh_keluar, k.harga_keluar), ('kill_switch', HARI[B0 + 2], 45.0))
        self.assertNotIn('B', set(R.saham)); self.assertEqual(list(E.kill_switch), [0, 1, 1, 1, 1])
        self.assertAlmostEqual(E.ekuiti.iloc[-1], E.tunai.iloc[-1])

    def test_delist(self):
        pendek = siri(rata(B0 + 3))                                 # tiada bar selepas HARI[B0 + 2]
        R, _ = ps.bina_pb(calon([dict(saham='A')]), HARI[B0:B0 + 14], {'A': pendek}, 'PLAYBOOK_10')
        k = R.iloc[0]
        self.assertEqual((k.sebab_keluar, k.tarikh_keluar, k.harga_keluar), ('delist', HARI[B0 + 2], 100.0))


class TestRekodBeku(unittest.TestCase):
    def C(self, d, n=3, tiada=False):
        return pd.DataFrame([dict(tarikh_beli=d, saham=f'S{i}', tarikh_isyarat='2026-10-15', id_kaedah='M01', harga_beli=50.0,
                                  tutup=50.0, r_awal=0.1, lulus=i < 2, data_tiada=tiada, **{f'gagal_{k}': i >= 2 and k == 'rs'
                                  for k in ps.SEBAB_PB}) for i in range(n)])

    def test_log_beku_dan_tangguh(self):
        sesi = ['2026-10-16', '2026-10-19', '2026-10-20']
        with tempfile.TemporaryDirectory() as d:
            C = pd.concat([self.C('2026-10-16'), self.C('2026-10-19', tiada=True)])
            L, T, tg = ps.log_pb(C, sesi, folder=d, dinilai='x')
            self.assertEqual(tg, ['2026-10-19']); self.assertEqual(list(T.tarikh_beli), ['2026-10-16'])
            self.assertEqual(list(L.saham), ['S0', 'S1']); self.assertEqual(int(T.gagal_rs.iloc[0]), 1)
            C2 = pd.concat([self.C('2026-10-16', n=1), self.C('2026-10-19', tiada=True)])   # data berubah: rekod lama kekal
            L, T, tg = ps.log_pb(C2, sesi + ['2026-10-21', '2026-10-22', '2026-10-23', '2026-10-26'], folder=d, dinilai='y')
            self.assertEqual(tg, []); self.assertEqual(list(T.tarikh_beli), ['2026-10-16', '2026-10-19'])
            self.assertEqual(list(L.saham), ['S0', 'S1'])          # 19 Okt: data_tiada -> tiada calon lulus
            self.assertEqual(int(T.data_tiada.iloc[1]), 3)

    def test_pool_lejar_dan_ambil_alih(self):
        L = pd.DataFrame([dict(tarikh_beli='2026-10-16', saham=s, tarikh_isyarat='2026-10-15', rs='85', r_awal='0.1',
                               harga_beli='50') for s in ('A', 'B', 'C')])
        P = pd.DataFrame([dict(tarikh_beli='2026-10-16', saham=s, harga_beli=hb) for s, hb in (('A', 25.0), ('B', 51.0))])
        with tempfile.TemporaryDirectory() as d:
            aa = os.path.join(d, 'aa.csv')
            pd.DataFrame([dict(saham='B', tarikh_umum='2026-10-14')]).to_csv(aa, index=False)
            X = ps.pool_pb(L, P, aa)
        self.assertEqual(list(X.saham), ['A']); self.assertEqual(X.harga_beli.iloc[0], 25.0)   # harga Lejar semasa (laras)


class TestPerinci(unittest.TestCase):
    def test_paras_risiko_heat_sektor(self):
        c = rata(B0) + [100, 110, 108]
        H = {'A': siri(c), 'B': siri(rata(B0 + 3))}
        sa = H['A']; x = ps.KL.lorong_henti(sa.o, sa.c + 0.5, sa.c - 0.5, sa.c, B0)   # paras lorong 2 semasa
        R = pd.DataFrame([dict(saham='A', status='Pegang', tarikh_beli=HARI[B0], harga_beli=100.0, harga_terkini=108.0, amaun=0.1,
                               lorong='henti', tarikh_keluar='', henti=np.nan),
                          dict(saham='B', status='Pegang', tarikh_beli=HARI[B0], harga_beli=100.0, harga_terkini=100.0, amaun=0.1,
                               lorong='kaedah', tarikh_keluar='', henti=''),
                          dict(saham='A', status='Keluar', tarikh_beli=HARI[B0 - 5], harga_beli=100.0, harga_terkini=np.nan,
                               amaun=0.1, lorong='henti', tarikh_keluar=HARI[B0 - 1], henti=np.nan)])
        E = pd.DataFrame(dict(tarikh=HARI[B0:B0 + 3], ekuiti=[1.0, 1.01, 1.008], tunai=[0.8, 0.8, 0.8]))
        X = ps.perinci(R, E, H, peta={'A': ('Semiconductors', 'Technology')})
        a = X.iloc[0]
        self.assertAlmostEqual(a.paras_keluar, x['paras']); self.assertEqual(a.hari, 3)
        self.assertAlmostEqual(a.jarak_atr, (108 - x['paras']) / sa.a[-1])
        self.assertAlmostEqual(a.risiko_pct, 100 * 0.108 * ((108 - x['paras']) / 108) / 1.008)
        self.assertAlmostEqual(X.iloc[1].risiko_pct, 100 * 0.1 / 1.008)   # lorong kaedah tanpa henti: nilai penuh
        self.assertEqual(X.iloc[2].hari, 5); self.assertTrue(pd.isna(X.iloc[2].risiko_pct))
        s = ps.ringkas_risiko(X, E)
        self.assertEqual(s['sektor'], {'Technology': 1, 'Tiada': 1}); self.assertEqual(s['bawah_puncak_sesi'], 1)
        self.assertAlmostEqual(s['heat_pct'], round(a.risiko_pct + X.iloc[1].risiko_pct, 2))
        self.assertAlmostEqual(s['tunai_pct'], round(100 * 0.8 / 1.008, 2))


class TestJanaDb(unittest.TestCase):
    """jana_db.portfolio_slot(): medan risiko baharu, siri [tarikh, ekuiti, spy, ew], mdd_jangka, ringkasan posisi Keluar."""
    def test_medan_dan_potong(self):
        import json
        import jana_db as jd
        with tempfile.TemporaryDirectory() as d:
            t = ['2026-10-16', '2026-10-19', '2026-10-20']
            for k in ('RS_10', 'PLAYBOOK_10'):
                pd.DataFrame(dict(tarikh=t, ekuiti=[0.99, 1.02, 1.01], tunai=[0.1, 0.1, 0.2], bil_posisi=[9, 9, 8],
                                  spy=[1.0, 1.01, 1.02])).to_csv(os.path.join(d, f'{k}_ekuiti.csv'), index=False)
                rows = [dict(saham='A', id_kaedah='M01', status='Pegang', tarikh_beli=t[0], harga_beli=10.0, harga_terkini=11.0,
                             untung_pct=np.nan, paras_keluar=10.0, jarak_atr=2.0, risiko_pct=1.2, sektor_us='Technology',
                             industri_us='Semiconductors', hari=3, tarikh_keluar='')]
                rows += [dict(saham=f'K{i:03d}', id_kaedah='M01', status='Keluar', tarikh_beli=t[0], harga_beli=10.0, untung_pct=1.0,
                              tarikh_keluar=f'2026-10-{16 + i % 3:02d}', sektor_us='Energy', hari=2) for i in range(80)]
                pd.DataFrame(rows).to_csv(os.path.join(d, f'{k}_posisi.csv'), index=False)
            ew = os.path.join(d, 'ew.csv')
            pd.DataFrame(dict(tarikh=t, ew_oc=[0.01, 0.0, 0.0], ew_cc=[0.0, 0.02, -0.01])).to_csv(ew, index=False)
            kj = os.path.join(d, 'mdd.json')
            with open(kj, 'w') as f:
                json.dump(dict(takrif='x', sumber='y', penuh={'RS_10': [-48.0, -45.0]}), f)
            doc = jd.portfolio_slot('kini', folder=d, ew_path=ew, kajian=kj)
            p = doc['portfolio']['RS_10']
            self.assertEqual(p['ekuiti'][1][:3], ['2026-10-19', 1.02, 1.01])
            self.assertAlmostEqual(p['ekuiti'][2][3], 1.01 * 1.02 * 0.99, places=5)
            self.assertEqual(p['mdd_jangka'], [-48.0, -45.0]); self.assertIsNone(doc['portfolio']['PLAYBOOK_10']['mdd_jangka'])
            self.assertEqual((p['heat_pct'], p['sektor'], p['bawah_puncak_sesi']), (1.2, {'Technology': 1}, 1))
            self.assertAlmostEqual(p['tunai_pct'], round(100 * 0.2 / 1.01, 2))
            a = next(r for r in p['posisi'] if r['status'] == 'Pegang')
            self.assertEqual((a['paras_keluar'], a['jarak_atr'], a['sektor_us'], a['hari']), (10.0, 2.0, 'Technology', 3))
            self.assertEqual(len([r for r in p['posisi'] if r['status'] == 'Keluar']), 80)
            kecil = jd.portfolio_slot('kini', folder=d, ew_path=ew, kajian=kj, had=1000)
            q = kecil['portfolio']['RS_10']
            K = [r for r in q['posisi'] if r['status'] == 'Keluar']
            self.assertEqual((len(K), q['posisi_keluar_dipotong']), (50, 30))
            self.assertTrue(all(r['tarikh_keluar'] >= '2026-10-17' for r in K))   # 50 terakhir ikut tarikh keluar
            self.assertEqual(sum(r['status'] == 'Pegang' for r in q['posisi']), 1)


if __name__ == '__main__':
    unittest.main()
