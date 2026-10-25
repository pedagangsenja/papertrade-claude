# Prestasi M / C / Combine (tugasan_v3 §7; kiraan KPI dan skor U×S sama dengan halaman dashboard)
# Guna: python3 harian_prestasi.py <folder> [--papan data/analisis/papan.json]
#       (folder mengandungi out_moomoo.json, out_claude.json, out_mae.json; output out_prestasi.json)
#
# Cadangan 25 Okt 2026 (audit operasi item 8–9; tugasan_v3 §12, menunggu kelulusan pengguna):
# - Label §7 TERUSKAN / PERHATI / HENTIKAN DIBERSARAKAN: set HENTIKAN berubah 3 kali dalam 5 hari (label atas purata posisi
#   belum matang). Keputusan kaedah = pintu Papan Penganalisis (data/analisis/papan.json `pantau`/`status`; tugasan_v3 §11).
#   Medan lama dikekalkan untuk keserasian: `keputusan` = 'dibersarakan', `teruskan`/`hentikan`/`bil` = None; medan baharu
#   `pantau_penganalisis`/`status_penganalisis` setiap kaedah (None jika papan.json tiada).
# - Combine = Papertrade C SAHAJA: 200 posisi Moomoo lama sah (4 hari beli, 1–8 Okt 2026) tidak lagi dicampur. Papertrade M kekal
#   dikira berasingan sebagai sejarah (`M`).
import argparse, json, os, sys, statistics as st

HERE = os.path.dirname(os.path.abspath(__file__))
PAPAN = os.path.join(os.path.dirname(HERE), 'data', 'analisis', 'papan.json')
MIN_TUTUP = 20      # (sejarah) label lama hanya selepas >= 20 dagangan tertutup setiap kaedah
USD_POSISI = 1000   # metrik portfolio: setiap posisi dianggap USD1,000 (sama berat)
DIBERSARAKAN = 'dibersarakan'
NOTA_LABEL = ('Label §7 TERUSKAN/PERHATI/HENTIKAN dibersarakan (cadangan 25 Okt 2026, tugasan_v3 §12): keputusan kaedah ikut '
              'pintu Papan Penganalisis (analisis/papan: pantau BELUM CUKUP/OK/AMARAN/GANTUNG/BERSARA).')
NOTA_COMBINE = 'Combine = Papertrade C sahaja (posisi Moomoo lama dikecualikan sejak 25 Okt 2026); M = sejarah Moomoo lama.'


def cl(x):
    return max(0, min(1, x))


def rows(ak, R, mae):
    out = []
    for r in R:
        u = r['untung_akhir_pct'] if r.get('keluar') else r['untung_pct']
        k = f"{ak}|{r['saham']}|{r['kaedah']}|{r['tarikh_beli']}"
        out.append(dict(ak=ak, saham=r['saham'], kaedah=r['kaedah'], u=u, keluar=bool(r.get('keluar')), hari=r.get('hari') or 0,
                        dd=mae.get(k, min(u, 0))))
    return out


def kpi(T):
    if not T:
        return {}
    us = [t['u'] for t in T]
    w = min(T, key=lambda t: t['u'])
    return dict(dagangan=len(T), kadar_menang=round(100 * sum(u > 0 for u in us) / len(us), 1), untung_purata=round(st.mean(us), 2),
                untung_median=round(st.median(us), 2), rugi_terbesar=round(w['u'], 2), rugi_terbesar_saham=f"{w['saham']} ({w['kaedah']})",
                hari_purata=round(st.mean(t['hari'] for t in T), 1), kaedah=len({t['kaedah'] for t in T}), keluar=sum(t['keluar'] for t in T),
                penurunan_maks_purata=round(st.mean(t['dd'] for t in T), 2),
                untung_usd_sama=round(sum(us) / 100 * USD_POSISI, 2), modal_usd_sama=len(T) * USD_POSISI)


def kaedah(T, pantau=None):
    """Statistik setiap kaedah + skor U×S (paparan). pantau: {id: (pantau, status)} daripada Papan Penganalisis."""
    pantau = pantau or {}
    g = {}
    for t in T:
        g.setdefault(t['kaedah'], []).append(t)
    out = []
    for k, a in g.items():
        us = [t['u'] for t in a]; n = len(a); avg = st.mean(us); win = sum(u > 0 for u in us) / n
        dd = st.mean(t['dd'] for t in a); worst = min(us)
        U = 0.6 * cl((avg + 5) / 15) + 0.4 * win; S = 0.6 * cl(1 + dd / 10) + 0.4 * cl(1 + worst / 20)
        sk = 100 * U * S * min(1, n / 5); gagal = 1 - win
        pn = pantau.get(k) or (None, None)
        out.append(dict(kaedah=k, n=n, menang=round(100 * win, 1), purata=round(avg, 2), median=round(st.median(us), 2), terburuk=round(worst, 2),
                        dd=round(dd, 2), gagal=round(100 * gagal, 1), keluar_rugi=sum(1 for t in a if t['keluar'] and t['u'] < 0),
                        tutup=sum(1 for t in a if t['keluar']), skor=round(sk, 1), keputusan=DIBERSARAKAN,
                        pantau_penganalisis=pn[0], status_penganalisis=pn[1]))
    return sorted(out, key=lambda x: -x['skor'])


def baca_pantau(papan=PAPAN):
    """{id kaedah: (pantau, status)} daripada data/analisis/papan.json (penganalisis.py); {} jika tiada."""
    try:
        with open(papan, encoding='utf-8') as f:
            P = json.load(f)
    except (OSError, ValueError):
        return {}
    return {r['id']: (r.get('pantau'), r.get('status')) for r in P.get('rows') or [] if r.get('id')}


def ringkasan(T, pantau=None):
    K = kaedah(T, pantau)
    return dict(kpi=kpi(T), kaedah=K,
                teruskan=None, hentikan=None, bil=None, label_s7=DIBERSARAKAN,      # keserasian: label §7 dibersarakan
                teruk_gagal=[(x['kaedah'], x['gagal'], x['n']) for x in sorted([x for x in K if x['n'] >= 3], key=lambda x: -x['gagal'])[:5]],
                teruk_rugi=[(x['kaedah'], x['terburuk']) for x in sorted(K, key=lambda x: x['terburuk'])[:5]],
                teruk_keluar_rugi=[(x['kaedah'], x['keluar_rugi']) for x in sorted(K, key=lambda x: -x['keluar_rugi'])[:5]],
                top=[(x['kaedah'], x['skor'], x['purata'], x['menang'], x['n']) for x in K[:5]])


def prestasi(M, C, mae, pantau=None):
    """M, C: baris posisi sah (out_moomoo/out_claude rows); mae: {kunci: %}. -> {'M', 'C', 'Combine'}."""
    TM, TC = rows('M', M, mae), rows('C', C, mae)
    res = {'M': dict(ringkasan(TM, pantau), nota='Papertrade M: posisi Moomoo lama (sejarah; tiada belian baharu sejak 13 Okt 2026).'),
           'C': ringkasan(TC, pantau)}
    res['Combine'] = dict(ringkasan(TC, pantau), nota=NOTA_COMBINE)
    return res


def main(argv=None):
    ap = argparse.ArgumentParser(description='Prestasi M / C / Combine (tugasan_v3 §7)')
    ap.add_argument('folder', nargs='?', default='.')
    ap.add_argument('--papan', default=PAPAN, help='Papan Penganalisis (rujukan pintu kaedah)')
    a = ap.parse_args(argv)
    SP = os.path.join(a.folder, '')
    with open(SP + 'out_moomoo.json') as f:
        M = json.load(f)['rows']
    with open(SP + 'out_claude.json') as f:
        C = json.load(f)['rows']
    with open(SP + 'out_mae.json') as f:
        mae = json.load(f)['rows']
    res = prestasi(M, C, mae, baca_pantau(a.papan))
    with open(SP + 'out_prestasi.json', 'w') as f:
        json.dump(dict(res, dibina=os.environ.get('DIBINA', ''), harga_pada=os.environ.get('HARGA_PADA', ''), label_s7=NOTA_LABEL,
                       nota='Dikira semula dengan skor U×S (sama seperti halaman). Halaman mengira sendiri daripada papertrade/moomoo + '
                            'claude + prestasi/mae; dokumen ini rekod ringkasan. ' + NOTA_COMBINE),
                  f, ensure_ascii=False, separators=(',', ':'))
    for nm in res:
        r = res[nm]; print(nm, r['kpi']); print(' top', r['top'])
        print(' teruk', r['teruk_gagal'], r['teruk_rugi'], r['teruk_keluar_rugi'])
    return 0


if __name__ == '__main__':
    sys.exit(main())
