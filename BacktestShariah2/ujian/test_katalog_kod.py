# Ujian penyegerakan katalog kaedah (standard/katalog_kaedah.json = db kaedah/katalog) dengan kod kod/kaedah/Mxx.py
# (audit dashboard 24 Okt 2026, item 27): VARIAN, TMAX (teks pegang), ADA_HENTI/HENTI_TUTUP (teks henti) dan tiada_keluar_had
# (tiada isyarat keluar, tiada sasaran, TMAX None: disemak dengan menjalankan sedia() atas sampel stor harga repo), serta
# angka dalam jalur "Sama untuk semua" (sama_semua) lawan pemalar kod.
import ast, glob, importlib, json, os, re, sys, unittest, warnings

import pandas as pd

BS2 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KOD = os.path.join(BS2, 'kod')
sys.path.insert(0, KOD)
KATALOG = os.path.join(BS2, 'standard', 'katalog_kaedah.json')
HARIAN_C = os.path.join(BS2, 'standard', 'harian_c.py')
STOR = os.path.join(BS2, 'data', 'harga', 'stor')
SAMPEL = (15, 80)      # saham sampel (>= 400 bar, susunan abjad): kecil dahulu; besar jika tiada keluar dilihat atau untuk mengesahkan tiada
BAR_MIN = 400


def nombor_id(mid):
    return int(mid[1:])


def modul(mid):
    return importlib.import_module('kaedah.' + mid)


def senarai_modul():
    return sorted((os.path.basename(p)[:-3] for p in glob.glob(os.path.join(KOD, 'kaedah', 'M*.py'))), key=nombor_id)


def hampir_kosong(mid):
    """True jika hampir() modul hanya `return None` (tiada calon watchlist), disemak daripada sumber."""
    with open(os.path.join(KOD, 'kaedah', mid + '.py'), encoding='utf-8') as f:
        t = ast.parse(f.read())
    fn = [n for n in t.body if isinstance(n, ast.FunctionDef) and n.name == 'hampir']
    if not fn:
        return True
    b = [s for s in fn[0].body if not (isinstance(s, ast.Expr) and isinstance(s.value, ast.Constant) and isinstance(s.value.value, str))]
    return len(b) == 1 and isinstance(b[0], ast.Return) and (b[0].value is None or (isinstance(b[0].value, ast.Constant) and b[0].value.value is None))


def pemalar_harian_c():
    """MAKS_KAEDAH dan MINGGUAN daripada sumber harian_c.py (tanpa import: modul itu memuat banyak kebergantungan)."""
    with open(HARIAN_C, encoding='utf-8') as f:
        s = f.read()
    maks = int(re.search(r'^MAKS_KAEDAH\s*=\s*(\d+)', s, re.M).group(1))
    ming = set(re.findall(r"'(M\d+)'", re.search(r'^MINGGUAN\s*=\s*\{([^}]*)\}', s, re.M).group(1)))
    return maks, ming


def ids_dalam(teks):
    return set(re.findall(r'\bM\d+\b', teks))


class TestKatalogKod(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open(KATALOG, encoding='utf-8') as f:
            cls.doc = json.load(f)
        cls.rows = {r['id']: r for r in cls.doc['rows']}
        cls._fr = None

    @classmethod
    def frames(cls):
        if cls._fr is None:
            p = os.path.join(STOR, 'harga_A.csv')
            if not os.path.exists(p):
                raise unittest.SkipTest('stor harga repo tiada')
            from stor import frames_dict
            fr, idx = frames_dict({'harga_A.csv': pd.read_csv(p), 'harga_idx.csv': pd.read_csv(os.path.join(STOR, 'harga_idx.csv'))})
            cls._fr = ({t: g for t, g in sorted(fr.items()) if len(g) >= BAR_MIN}, idx)
        return cls._fr

    def keluar_dilihat(self, m, n):
        """Ada sekurang-kurangnya satu isyarat keluar (exitc) atau sasaran (tgt) atas n saham sampel?"""
        fr0, idx = self.frames()
        fr = {t: g.copy() for t, g in list(fr0.items())[:n]}
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            m.sedia(fr, idx)
        for g in fr.values():
            if 'exitc' in g and bool(g['exitc'].fillna(False).astype(bool).any()):
                return True
            if 'tgt' in g and bool(pd.to_numeric(g['tgt'], errors='coerce').notna().any()):
                return True
        return False

    def test_varian_sama_dengan_kod(self):
        for mid in senarai_modul():
            self.assertIn(mid, self.rows, mid)
            self.assertEqual(self.rows[mid]['varian_kod'], modul(mid).VARIAN, mid)

    def test_tmax_dalam_teks_pegang(self):
        for mid in senarai_modul():
            T, peg = getattr(modul(mid), 'TMAX', None), self.rows[mid]['pegang']
            if T:
                self.assertRegex(peg, re.compile(rf'maks(?:imum)?\s+{T}\b', re.I), mid)
            else:
                self.assertNotRegex(peg, re.compile(r'maks(?:imum)?\s+\d', re.I), mid)

    def test_henti_sama_dengan_kod(self):
        for mid in senarai_modul():
            m, r = modul(mid), self.rows[mid]
            tiada = bool(re.match(r'tiada henti', r['henti'].strip(), re.I))
            self.assertEqual(tiada, not m.ADA_HENTI, f'{mid}: ADA_HENTI={m.ADA_HENTI} lawan teks henti "{r["henti"][:60]}"')
            if not m.ADA_HENTI:
                self.assertNotRegex(r['pegang'], re.compile(r'henti', re.I), f'{mid}: tiada henti tetapi teks pegang menyebut henti')
            if getattr(m, 'HENTI_TUTUP', None):
                self.assertRegex(r['henti'], re.compile(r'^henti ikut tutup', re.I), mid)

    def test_tiada_keluar_had(self):
        for r in self.doc['rows']:
            self.assertIsInstance(r.get('tiada_keluar_had'), bool, r['id'])
        for mid in senarai_modul():
            m, r = modul(mid), self.rows[mid]
            if getattr(m, 'TMAX', None):
                self.assertFalse(r['tiada_keluar_had'], f'{mid}: ada TMAX')
                continue
            ada = self.keluar_dilihat(m, SAMPEL[0]) or self.keluar_dilihat(m, SAMPEL[1])
            self.assertEqual(r['tiada_keluar_had'], not ada, f'{mid}: keluar/sasaran dilihat = {ada}')
            if r['tiada_keluar_had']:
                self.assertRegex(r['keluar'], re.compile(r'^tiada\b', re.I), mid)
                self.assertRegex(r['pegang'], re.compile(r'tiada isyarat keluar dan tiada had masa', re.I), mid)
        tanda = sorted((i for i, r in self.rows.items() if r['tiada_keluar_had']), key=nombor_id)
        self.assertEqual(len(tanda), 8, tanda)

    def test_sama_untuk_semua(self):
        s = {x['tajuk']: x['teks'] for x in self.doc['sama_semua']}
        maks, ming = pemalar_harian_c()
        self.assertIn(f'maksimum {maks} isyarat baharu setiap kaedah', s['Had isyarat'])
        self.assertEqual(ids_dalam(s['Kaedah mingguan']), ming)
        import dagangan
        self.assertEqual(ids_dalam(s['Kaedah replika']), set(dagangan.REPLIKA))
        tanda = {i for i, r in self.rows.items() if r['tiada_keluar_had']}
        self.assertEqual(ids_dalam(s['Tiada keluar, tiada had masa']), tanda)
        kosong = [mid for mid in senarai_modul() if hampir_kosong(mid)]
        k145 = [mid for mid in kosong if nombor_id(mid) >= 115]
        self.assertEqual(len([mid for mid in senarai_modul() if nombor_id(mid) >= 115]), len(k145), 'ada K145+ dengan hampir()')
        self.assertIn(f'{len(kosong)} kaedah tiada calon', s['Watchlist'])
        self.assertIn(f'{len(k145)} kaedah K145+', s['Watchlist'])
        self.assertEqual(ids_dalam(s['Watchlist']) - {k145[0], k145[-1]}, set(kosong) - set(k145))
        import tidak_layak as TL
        t = s['Saham tidak layak']
        self.assertIn(f'≥ {TL.JULAT0_MAKS} bar tanpa julat', t)
        self.assertIn(f'≥ {TL.VOL0_MAKS} bar tanpa volum', t)
        self.assertIn(f'USD{int(TL.NILAI_MIN // 1000)} ribu', t)
        self.assertIn(f'{TL.BAR_CAIR} bar terakhir', t)
        self.assertIn(f'≥ {TL.DELIST_SESI} sesi', t)

    def test_saiz_dokumen_db(self):
        self.assertLess(len(json.dumps(self.doc, ensure_ascii=False, separators=(',', ':')).encode()), 250_000)


if __name__ == '__main__':
    unittest.main()
