"""Ujian semak_terbit.py — kedua-dua arah, dan hadnya dinyatakan."""
import json
import os
import shutil
import sys
import tempfile
import unittest

AKAR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(AKAR, 'BacktestShariah2', 'standard'))
import semak_terbit as SD  # noqa: E402


class UjiSemakDashboard(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.html = os.path.join(self.tmp, 'dashboard_v2.html')
        self.man = os.path.join(self.tmp, 'dashboard_terbit.json')
        with open(self.html, 'w', encoding='utf-8') as f:
            f.write('<title>x</title><script>/* a */</script>')
        self._h, self._m = SD.HTML, SD.MANIFES
        SD.HTML, SD.MANIFES = self.html, self.man

    def tearDown(self):
        SD.HTML, SD.MANIFES = self._h, self._m
        shutil.rmtree(self.tmp, ignore_errors=True)

    def test_tiada_manifes_gagal(self):
        self.assertEqual(SD.main([]), 1)

    def test_selaras_lulus(self):
        SD.main(['--kemas', '--versi', '1-a', '--nombor', '1'])
        self.assertEqual(SD.main([]), 0)

    def test_fail_berubah_gagal(self):
        """Arah yang skrip ini MEMANG tangkap: repo disunting tanpa diterbitkan."""
        SD.main(['--kemas', '--versi', '1-a', '--nombor', '1'])
        with open(self.html, 'a', encoding='utf-8') as f:
            f.write('/* suntingan tanpa terbit */')
        self.assertEqual(SD.main([]), 1)

    def test_manifes_merekod_versi_dan_saiz(self):
        SD.main(['--kemas', '--versi', '1793412015-9909', '--nombor', '155'])
        with open(self.man, encoding='utf-8') as f:
            d = json.load(f)
        self.assertEqual(d['versi_artifact'], '1793412015-9909')
        self.assertEqual(d['nombor'], 155)
        self.assertEqual(d['bait'], os.path.getsize(self.html))
        self.assertEqual(len(d['sha256']), 64)

    def test_kemas_mengekalkan_versi_jika_tidak_diberi(self):
        """--kemas tanpa --versi tidak boleh memadamkan version id yang sudah direkod."""
        SD.main(['--kemas', '--versi', '1793412015-9909', '--nombor', '155'])
        with open(self.html, 'a', encoding='utf-8') as f:
            f.write('/* b */')
        SD.main(['--kemas'])
        with open(self.man, encoding='utf-8') as f:
            d = json.load(f)
        self.assertEqual(d['versi_artifact'], '1793412015-9909')


class UjiManifesSebenar(unittest.TestCase):
    def test_repo_selaras_dengan_terbitan(self):
        """Manifes dalam repo mesti padan dengan dashboard_v2.html yang dikomit."""
        self.assertEqual(SD.main([]), 0)


if __name__ == '__main__':
    unittest.main()
