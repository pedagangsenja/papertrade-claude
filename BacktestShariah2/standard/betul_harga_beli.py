# betul_harga_beli.py — betulkan harga_beli Papertrade C yang tidak sepadan dengan buka rasmi bar hari beli (audit 24 Okt 2026:
# DAC M80/M90 12 Okt direkod 164.162 sedangkan buka rasmi 170.19; tiada semakan yang menangkapnya). Rujukan buka = stor harga
# repo (semakan sama dengan sahkan.py beza_buka: toleransi 0.3%, buka Moomoo disahkan dalam buka_moomoo.csv diterima, baris
# "buka sementara" dan akaun M dikecualikan). Sahkan dahulu dengan kline Moomoo (autype 0) dan nyatakan dalam --sah.
#
# Yang dikira semula: harga_beli, untung_pct (harga_terkini), untung_akhir_pct (lorong 1 keluar), untung_henti_pct (lorong 2
# keluar). Tarikh/harga keluar TIDAK berubah: henti/sasaran kaedah = paras hari isyarat dan lorong 2 (Chandelier tutup) tidak
# bergantung pada harga beli. Baris dilangkau (dilapor untuk dinilai semula secara manual):
#   - kaedah yang henti/sasarannya ikut buka masuk (BERGANTUNG_BUKA);
#   - buka baharu <= henti (kaedah melangkau belian pada buka itu: perlu tidak_dibeli, bukan pembetulan harga).
#
#   python3 BacktestShariah2/standard/betul_harga_beli.py [--folder PT] [--stor DIR] [--saham DAC,SENEB] \
#       --sah "kline Moomoo autype 0 sama" [--tulis]
# Tanpa --tulis = cuba (senarai perubahan sahaja). Catat hasil dalam standard/binaan_v2_log_tambahan.md.
import argparse, json, os, sys

import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import sahkan as SH  # noqa: E402

# henti atau sasaran dikira daripada buka masuk (bar i+1), bukan paras hari isyarat — disemak 24 Okt 2026:
# M02 sasaran = buka + 3R; M06 henti = max(0.99 x low, 0.92 x buka); M52 henti = 0.60 x buka
BERGANTUNG_BUKA = {'M02', 'M06', 'M52'}


BULAN = ['Jan', 'Feb', 'Mac', 'Apr', 'Mei', 'Jun', 'Jul', 'Ogo', 'Sep', 'Okt', 'Nov', 'Dis']


def r2(x):
    return f'{x:.2f}'


def r4(x):
    return f'{x:.4f}'.rstrip('0').rstrip('.')


def betul_baris(r, baru, sah, tarikh):
    """Ubah baris r di tempat: harga_beli = baru dan untung semua lorong dikira semula. Pulang dict sebelum/selepas."""
    lama = {k: r.get(k, '') for k in ('harga_beli', 'untung_pct', 'untung_akhir_pct', 'untung_henti_pct')}
    r['harga_beli'] = r4(baru)
    ht = SH.nombor(r.get('harga_terkini'))
    if ht is not None:
        r['untung_pct'] = r2((ht / baru - 1) * 100)
    if SH.benar(r.get('keluar')) and SH.nombor(r.get('harga_keluar')) is not None:
        r['untung_akhir_pct'] = r2((float(r['harga_keluar']) / baru - 1) * 100)
    if SH.benar(r.get('keluar_henti')) and SH.nombor(r.get('harga_keluar_henti')) is not None:
        r['untung_henti_pct'] = r2((float(r['harga_keluar_henti']) / baru - 1) * 100)
    nota = f"harga_beli dibetulkan {tarikh}: {lama['harga_beli']} -> {r['harga_beli']} = buka bar {r['tarikh_beli']} (stor; {sah})"
    r['nota'] = ((r.get('nota') or '') + '; ' + nota).lstrip('; ')
    return dict(lama=lama, baru={k: r.get(k, '') for k in lama})


def jalan(folder, stor, saham=None, sah='', tulis=False, tarikh=None):
    """Pulang (diubah, dilangkau): senarai (fail, saham, kaedah, tarikh_beli, sebelum, selepas) dan (…, sebab)."""
    if not tarikh:
        d = pd.Timestamp.now(tz='Asia/Kuala_Lumpur'); tarikh = f'{d.day} {BULAN[d.month - 1]} {d.year}'
    fail = [p for p in SH.fail_posisi_dalam(folder) if os.path.basename(p) != 'moomoo.csv']
    data = {p: SH.baca(p) for p in fail}
    tc = {r.get('saham') for _, rows in data.values() for r in rows}
    O, MM = SH.buka_stor(stor, tc)
    diubah, dilangkau = [], []
    for p, (lajur, rows) in data.items():
        ubah = False
        for r in rows:
            if saham and r.get('saham') not in saham:
                continue
            x = SH.beza_buka(r, O, MM)
            if not x:
                continue
            baru = x[1]; kk = (os.path.basename(p), r['saham'], r['kaedah'], r['tarikh_beli'])
            mid = r.get('id_kaedah') or r.get('kaedah')
            henti = SH.nombor(r.get('henti'))
            if mid in BERGANTUNG_BUKA:
                dilangkau.append(kk + ('henti/sasaran kaedah ikut buka masuk: nilai semula manual',)); continue
            if henti is not None and baru <= henti:
                dilangkau.append(kk + (f'buka {baru:g} <= henti {henti:g}: kaedah melangkau belian (tidak_dibeli)',)); continue
            d = betul_baris(r, baru, sah or 'tidak disahkan sumber kedua', tarikh)
            diubah.append(kk + (d['lama'], d['baru']))
            ubah = True
        if ubah and tulis:
            SH.tulis(p, lajur, rows)
    return diubah, dilangkau


def main(argv=None):
    ap = argparse.ArgumentParser(description='Betulkan harga_beli C kepada buka bar hari beli (stor) dan kira semula untung')
    ap.add_argument('--folder', default=SH.PT)
    ap.add_argument('--stor', default=SH.STOR)
    ap.add_argument('--saham', help='senarai ticker dipisah koma (lalai: semua baris yang gagal semakan)')
    ap.add_argument('--sah', default='', help='sumber kedua yang mengesahkan buka, cth. "kline Moomoo autype 0 sama"')
    ap.add_argument('--tulis', action='store_true')
    a = ap.parse_args(argv)
    saham = set(a.saham.split(',')) if a.saham else None
    diubah, dilangkau = jalan(a.folder, a.stor, saham, a.sah, a.tulis)
    for x in diubah:
        print(*x[:4], json.dumps(x[4], ensure_ascii=False), '->', json.dumps(x[5], ensure_ascii=False), sep='\t')
    for x in dilangkau:
        print('LANGKAU', *x, sep='\t')
    print(json.dumps(dict(diubah=len(diubah), dilangkau=len(dilangkau), ditulis=bool(a.tulis)), ensure_ascii=False), file=sys.stderr)
    return 0


if __name__ == '__main__':
    sys.exit(main())
