# amaran.py — amaran ntfy terus daripada sesi Claude berjadual (13 Nov 2026).
# Sesi tugasan berjadual tiada alat GitHub (tidak boleh workflow_dispatch amaran_ntfy.yml), tetapi rangkaian persekitaran
# membenarkan ntfy.sh. Topik sama dengan amaran_ntfy.yml / notifikasi.py.
#
#   python3 BacktestShariah2/standard/amaran.py --tajuk "paparan awal gagal" --mesej "13 Nov: <sebab>"
#   Keluar 0 jika dihantar; 1 jika gagal (sesi boleh cuba amaran_ntfy.yml jika alat GitHub ada).
import argparse, os, sys, urllib.request

TOPIK = os.environ.get('NTFY_TOPIC', 'claude_azim')


def hantar(tajuk, mesej, keutamaan='high', url=None):
    req = urllib.request.Request(url or f'https://ntfy.sh/{TOPIK}', data=mesej[:1000].encode('utf-8'), method='POST',
                                 headers={'Title': f'Papertrade: {tajuk}'.encode('utf-8').decode('latin-1', 'replace'),
                                          'Tags': 'warning', 'Priority': keutamaan})
    with urllib.request.urlopen(req, timeout=20) as r:
        return r.status


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument('--tajuk', required=True); ap.add_argument('--mesej', required=True)
    ap.add_argument('--keutamaan', default='high'); ap.add_argument('--url', help='ujian: hantar ke URL lain')
    a = ap.parse_args(argv)
    try:
        print(f'ntfy {hantar(a.tajuk, a.mesej, a.keutamaan, a.url)}')
        return 0
    except Exception as e:
        print(f'ntfy gagal: {type(e).__name__}: {e}', file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
