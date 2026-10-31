"""Semak sumber dashboard selaras dengan apa yang terakhir DITERBITKAN.

Masalah yang skrip ini wujud untuk tangkap: pada 30-31 Okt 2026 repo didapati basi
terhadap artifact DUA KALI (v132-v138, kemudian v139). Puncanya sesi lain menerbitkan
terus ke artifact tanpa mengkomit `dashboard_v2.html`. Kedua-dua kali ia ditemui secara
kebetulan semasa cuba menerbit, bukan oleh semakan.

APA YANG SKRIP INI BOLEH DAN TIDAK BOLEH LIHAT — baca ini sebelum mempercayainya:

  BOLEH   repo disunting tanpa diterbitkan (hash fail != manifes)  -> ditangkap di sini
  TIDAK   diterbitkan tanpa dikomit                                -> TIDAK ditangkap

Sebabnya mekanikal: `/api/artifacts/...` dilindungi cabaran Cloudflare (403 "Just a
moment..."), dan pautan kongsi hanya memulangkan cengkerang ~34 KB, bukan halaman penuh.
Jadi GitHub Actions TIDAK boleh membaca artifact hidup, dan tiada semakan luar talian
boleh mengetahui versi hidup. Arah kedua itu hanya dapat dilihat oleh sesi Claude yang
mempunyai alat Artifact: ia disemak setiap hari dalam `jadual/tolak_db.md` langkah 7.

Guna:
  python3 BacktestShariah2/standard/semak_terbit.py           # semak (CI)
  python3 BacktestShariah2/standard/semak_terbit.py --kemas \\
      --versi 1793412015-9909 --nombor 155                       # selepas menerbit
"""
import argparse
import hashlib
import json
import os
import sys
from datetime import datetime, timezone

BS2 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HTML = os.path.join(BS2, 'standard', 'dashboard_v2.html')
MANIFES = os.path.join(BS2, 'data', 'dashboard_terbit.json')
ARTIFACT = 'https://claude.ai/code/artifact/12bb853e-34ef-4d6c-885d-10f46984437e'


def cap(path):
    with open(path, 'rb') as f:
        b = f.read()
    return hashlib.sha256(b).hexdigest(), len(b)


def baca():
    if not os.path.exists(MANIFES):
        return None
    with open(MANIFES, encoding='utf-8') as f:
        return json.load(f)


def kemas(versi, nombor, nota):
    sha, bait = cap(HTML)
    m = baca() or {}
    d = dict(artifact=ARTIFACT,
             versi_artifact=versi or m.get('versi_artifact'),
             nombor=nombor if nombor is not None else m.get('nombor'),
             sha256=sha, bait=bait,
             dikemas=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC'),
             nota=nota or m.get('nota') or '')
    os.makedirs(os.path.dirname(MANIFES), exist_ok=True)
    with open(MANIFES, 'w', encoding='utf-8') as f:
        json.dump(d, f, ensure_ascii=False, indent=2)
        f.write('\n')
    print(f'manifes dikemas: versi {d["versi_artifact"]} (#{d["nombor"]}), '
          f'{bait:,} bait, sha256 {sha[:16]}…')
    return 0


def semak():
    if not os.path.exists(HTML):
        print('RALAT: dashboard_v2.html tiada', file=sys.stderr)
        return 1
    m = baca()
    sha, bait = cap(HTML)
    if m is None:
        print('RALAT: data/dashboard_terbit.json tiada. Jalankan --kemas selepas menerbit.',
              file=sys.stderr)
        return 1
    if m.get('sha256') == sha:
        print(f'dashboard selaras dengan terbitan terakhir: versi {m.get("versi_artifact")} '
              f'(#{m.get("nombor")}), {bait:,} bait')
        print('NOTA: ini TIDAK mengesahkan artifact hidup sama. Arah "diterbitkan tanpa '
              'dikomit" hanya disemak oleh sesi harian tolak_db.md langkah 7.')
        return 0
    print('GAGAL: dashboard_v2.html BERUBAH tetapi tidak diterbitkan.', file=sys.stderr)
    print(f'  manifes : {m.get("bait", 0):,} bait, sha256 {str(m.get("sha256"))[:16]}…, '
          f'versi {m.get("versi_artifact")} (#{m.get("nombor")})', file=sys.stderr)
    print(f'  fail kini: {bait:,} bait, sha256 {sha[:16]}…', file=sys.stderr)
    print('', file=sys.stderr)
    print('Suntingan dashboard yang tidak diterbitkan bermakna papan yang pengguna lihat',
          file=sys.stderr)
    print('BUKAN kod dalam repo ini. Betulkan dengan SALAH SATU:', file=sys.stderr)
    print(f'  (a) terbitkan fail ini ke {ARTIFACT}, kemudian jalankan', file=sys.stderr)
    print('      semak_terbit.py --kemas --versi <id> --nombor <n>', file=sys.stderr)
    print('  (b) jika suntingan itu tidak sepatutnya ada: git checkout fail itu',
          file=sys.stderr)
    return 1


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument('--kemas', action='store_true', help='tulis manifes daripada fail semasa')
    ap.add_argument('--versi', help='version id artifact, cth. 1793412015-9909')
    ap.add_argument('--nombor', type=int, help='nombor versi artifact, cth. 155')
    ap.add_argument('--nota', help='nota ringkas apa yang berubah')
    a = ap.parse_args(argv)
    if a.kemas:
        return kemas(a.versi, a.nombor, a.nota)
    return semak()


if __name__ == '__main__':
    raise SystemExit(main())
