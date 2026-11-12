# peta_kumpulan.py — dokumen db `kumpulan/peta` bagi panel "Peta industri" (Rujukan → Sektor; 12 Nov 2026,
# keputusan pengguna: "saya perlu tahu sektor dan industri mana tengah hot").
#
# Sumber: data/kumpulan/gred_kumpulan.csv (snapshot sesi terakhir) + gred_kumpulan_sejarah.csv (semua sesi), kedua-duanya
# ditulis oleh standard/gred_kumpulan.py (Actions gred_kumpulan.yml). Skrip ini TIDAK mengira skor baharu: ia hanya
# menyusun skor sedia ada menjadi pangkat, perubahan pangkat (5 dan 21 sesi) dan siri skor untuk carta kecil.
#
# PAPARAN SAHAJA. Kajian (kajian/KAJIAN_REJIM_INDUSTRI.md, KAJIAN_GRED_KUMPULAN.md): industri 20% teratas hanya kekal
# teratas 23% selepas 21 sesi; lebihan pulangan hampir sifar dan terbalik ketika rejim OFF. Bukan penapis beli, bukan
# input kad skor.
#
# Guna: diimport oleh jana_db.py (`bina()`); CLI `python3 peta_kumpulan.py` mencetak ringkasan untuk semakan.
import csv, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
BS2 = os.path.dirname(HERE)
KINI = os.path.join(BS2, 'data', 'kumpulan', 'gred_kumpulan.csv')
SEJARAH = os.path.join(BS2, 'data', 'kumpulan', 'gred_kumpulan_sejarah.csv')
JENIS = {'Sektor': 'S', 'Industri': 'I'}
SESI_PENDEK, SESI_PANJANG = 5, 21   # perubahan pangkat lawan 5 dan 21 sesi lalu
SIRI_MAKS = 30                      # titik siri skor setiap kumpulan


def _nombor(x):
    try:
        v = float(x)
    except (TypeError, ValueError):
        return None
    return None if v != v else v


def muat(*fail):
    """Baris CSV daripada fail-fail (yang kemudian menimpa yang awal bagi kunci tarikh+jenis+nama sama)."""
    peta = {}
    for f in fail:
        if not f or not os.path.exists(f):
            continue
        with open(f, encoding='utf-8', newline='') as fh:
            for r in csv.DictReader(fh):
                if r.get('jenis') in JENIS and r.get('tarikh') and r.get('nama'):
                    peta[(r['tarikh'], r['jenis'], r['nama'])] = r
    return list(peta.values())


def pangkat(baris):
    """{nama: pangkat} (1 = skor tertinggi) bagi satu sesi dan satu jenis; skor kosong tiada pangkat.
    Skor sama → pangkat sama (pangkat terendah kumpulan seri)."""
    s = sorted(((_nombor(r['skor']), r['nama']) for r in baris if _nombor(r['skor']) is not None),
               key=lambda x: (-x[0], x[1]))
    out, lalu, p = {}, None, 0
    for i, (v, n) in enumerate(s, 1):
        if v != lalu:
            p, lalu = i, v
        out[n] = p
    return out


def bina(kini=KINI, sejarah=SEJARAH):
    """Dokumen `kumpulan/peta` atau None jika tiada data."""
    baris = muat(sejarah, kini)
    if not baris:
        return None
    tarikh = sorted({r['tarikh'] for r in baris})
    T = tarikh[-1]
    t5 = tarikh[-1 - SESI_PENDEK] if len(tarikh) > SESI_PENDEK else None
    t21 = tarikh[-1 - SESI_PANJANG] if len(tarikh) > SESI_PANJANG else None
    siri_t = tarikh[-SIRI_MAKS:]
    ikut = {}
    for r in baris:
        ikut.setdefault((r['tarikh'], r['jenis']), []).append(r)
    rows = []
    for jenis, j in JENIS.items():
        pk = {t: pangkat(ikut.get((t, jenis), [])) for t in (T, t5, t21) if t}
        skor_t = {t: {r['nama']: _nombor(r['skor']) for r in ikut.get((t, jenis), [])} for t in siri_t}
        for r in ikut.get((T, jenis), []):
            n = r['nama']; p = pk[T].get(n)

            def ubah(t):
                # positif = naik pangkat (nombor pangkat mengecil)
                return None if not t or p is None or pk[t].get(n) is None else pk[t][n] - p
            w = [_nombor(r.get(k)) for k in ('w_rs_positif', 'w_rs_naik', 'w_trend')]
            rows.append(dict(
                j=j, n=n, s=r.get('sektor') or '', c=int(_nombor(r.get('n')) or 0),
                sk=_nombor(r.get('skor')), g=r.get('gred') or '', p=p, d5=ubah(t5), d21=ubah(t21),
                m=_nombor(r.get('m1m_med')), a=_nombor(r.get('pct_atas_sma200')),
                w=None if any(x is None for x in w) else [int(x) for x in w],
                sp=[round(v) for v in (skor_t[t].get(n) for t in siri_t) if v is not None]))
    rows.sort(key=lambda r: (r['j'], r['p'] if r['p'] is not None else 10 ** 6, r['n']))
    dibina = max((r.get('dibina') or '' for r in ikut.get((T, 'Industri'), []) + ikut.get((T, 'Sektor'), [])), default='')
    return dict(
        tarikh=T, tarikh_5=t5, tarikh_21=t21, sesi=len(tarikh), siri_mula=siri_t[0], dibina=dibina, rows=rows,
        takrif=dict(
            industri='Skor = pangkat persentil (3 syarat Weinstein + median pulangan 1 bulan) antara industri',
            sektor='Skor = pangkat persentil % saham di atas SMA200 antara sektor',
            gred='A > 80, B > 60, C > 40, D > 20, E <= 20'),
        nota='Paparan sahaja, bukan penapis beli (kajian/KAJIAN_REJIM_INDUSTRI.md). Sumber: standard/gred_kumpulan.py.')


if __name__ == '__main__':
    d = bina()
    if not d:
        sys.exit('tiada data kumpulan')
    print(json.dumps({k: v for k, v in d.items() if k != 'rows'}, ensure_ascii=False, indent=1))
    for j in 'SI':
        x = [r for r in d['rows'] if r['j'] == j]
        print(j, len(x), 'kumpulan; teratas:', ', '.join(f"{r['n']} ({r['g']}, {r['d5']:+d})" if r['d5'] is not None
                                                          else f"{r['n']} ({r['g']})" for r in x[:5]))
    print('bait:', len(json.dumps(d, ensure_ascii=False, separators=(',', ':')).encode()))
