"""Mesin keadaan kajian REVERSE (`REVERSE/strategi.py`).

Sebab ujian ini wujud: pada 31 Okt 2026 `CLAUDE.md` menyenaraikan `GB04` dan `GB08` sebagai
"calon yang belum diuji" sedangkan kedua-duanya sudah diuji dan gagal. Sumber kebenaran yang
hanyut menyebabkan eksperimen dicadangkan semula. `--semak` menangkap kelas pepijat itu pada
setiap push.
"""
import io
import os
import sys
import unittest
from contextlib import redirect_stdout

AKAR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(AKAR, 'REVERSE'))
import strategi as ST  # noqa: E402


class UjiStrategi(unittest.TestCase):
    def test_registry_tidak_hanyut(self):
        """Tiada id paksi yang muncul dalam fail keputusan tetapi registry kata belum diuji."""
        bad = ST.hanyut()
        self.assertEqual(bad, [], 'registry hanyut daripada fail keputusan: ' + repr(bad))

    def test_semak_kod_keluar_sifar(self):
        with redirect_stdout(io.StringIO()):
            self.assertEqual(ST.main(['--semak']), 0)

    def test_keadaan_meliputi_setiap_eksperimen(self):
        K = ST.keadaan()
        self.assertEqual(len(K), len(ST.EKSPERIMEN))
        for _, st, _ in K:
            self.assertIn(st, ('SELESAI', 'BELUM'))

    def test_baris_gilir_berurutan_dan_lengkap(self):
        """E1-E6 mesti wujud dan berada dalam urutan yang STRATEGI.md tetapkan."""
        gil = [e['id'] for e in ST.EKSPERIMEN if e.get('giliran')]
        self.assertEqual(gil, ['E1', 'E2', 'E3', 'E4', 'E5', 'E6'])

    def test_penanda_aras_konvensyen_tunggal(self):
        """Nisbah SPUS mesti konsisten dengan CAGR dan MDD yang sama (jangan campur konvensyen)."""
        self.assertAlmostEqual(ST.SPUS_CAGR / abs(ST.SPUS_MDD), ST.SPUS_NISBAH, places=3)

    def test_tingkat_dinilai_betul(self):
        """T1 perlu KEDUA-DUA paksi; MDD cetek sahaja tidak mencukupi."""
        R = [dict(cagr='20.0', mdd='-20.0'),    # T1 (CAGR > SPUS, MDD lebih cetek) + T2
             dict(cagr='20.0', mdd='-40.0'),    # CAGR sahaja: MDD lebih dalam -> bukan T1
             dict(cagr='5.0', mdd='-5.0'),      # MDD sahaja: CAGR terlalu rendah -> bukan T1
             dict(cagr='16.0', mdd='-12.0')]    # T3 sahaja: bawah SPUS tetapi MDD cetek
        t1, t2, t3, terbaik = ST.nilai_tingkat(R)
        self.assertEqual(t1, 1, 'T1 memerlukan KEDUA-DUA paksi')
        self.assertEqual(t2, 1)
        self.assertEqual(t3, 1, 'T3 = CAGR >= 15 DAN MDD >= -15')
        self.assertAlmostEqual(terbaik[1], 20.0)

    def test_strategi_md_wujud_dan_menyebut_syarat_berhenti(self):
        p = os.path.join(AKAR, 'REVERSE', 'STRATEGI.md')
        self.assertTrue(os.path.exists(p))
        t = open(p, encoding='utf-8').read()
        for k in ('BERHENTI–MENANG', 'BERHENTI–TUTUP', 'BERHENTI–SEPARA', 'T4'):
            self.assertIn(k, t, f'STRATEGI.md mesti menyatakan {k}')

    def test_claude_md_menunjuk_kepada_mesin_keadaan(self):
        """CLAUDE.md tidak boleh menjadi sumber kebenaran bagi 'apa yang tinggal'."""
        t = open(os.path.join(AKAR, 'CLAUDE.md'), encoding='utf-8').read()
        self.assertIn('REVERSE/strategi.py', t)


if __name__ == '__main__':
    unittest.main()
