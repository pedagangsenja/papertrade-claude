# bina_pratonton.py — bina SATU fail HTML pratonton dashboard dengan db tiruan (untuk Artifact pratonton; dashboard v105).
#
#   python3 BacktestShariah2/standard/bina_pratonton.py --asas <db.json | folder db live> --db <folder output jana_db --keluar> \
#       --html BacktestShariah2/standard/dashboard_v2.html --tajuk "Pratonton Papan v105" --keluar <fail.html>
#
# db asas (salinan db live: fail JSON {"koleksi/doc": dokumen} atau folder <koleksi>/<doc>.json) DITINDIH dokumen output
# jana_db.py (folder <koleksi>/<doc>.json; batch_*.json dan ringkas.json diabaikan). Halaman disuntik dengan
#   <title>…</title><script>window.__DB={…};window.__mockDb=function(D){…}</script>
# dan baris pemuat db diganti supaya membaca window.__DB (sama dengan pratonton v104 dan ujian/halaman/uji_halaman.js).
# Dokumen lama yang tidak dibaca halaman apabila papertrade/ringkas_c|m ada (papertrade/claude*, moomoo, moomoo_peta,
# senarai_beli*) dibuang (--simpan-lama untuk mengekalkannya). Laporan: saiz (ralat > 16 MB, amaran > 12 MB), dokumen yang
# diperlukan halaman tetapi tiada atau bahagiannya tidak lengkap (senarai amaran), dan saiz db yang dimuat tab Hari Ini.
# Tiada tulisan ke db, tiada penerbitan: fail tempatan sahaja.
import argparse, glob, json, os, re, sys

SAMBUNG = "const db=window.claude?.use?await window.claude.use('db'):null;"
TIRUAN = "const db=window.__DB?window.__mockDb(window.__DB):(window.claude?.use?await window.claude.use('db'):null);"
MOCK = ("window.__mockDb=function(D){const snap=p=>({exists:p in D,id:p.split('/').pop(),data:()=>D[p]});\n"
        " return {doc:p=>({onSnapshot:cb=>{setTimeout(()=>cb(snap(p)),0);return ()=>{};}}),\n"
        "   collection:c=>{const o={limit:()=>o,onSnapshot:cb=>{setTimeout(()=>cb({docs:Object.keys(D).filter(k=>k.startsWith(c+'/')"
        "&&k.split('/').length===2).map(snap)}),0);return ()=>{};}};return o;}};};")
HAD = 16 * 1024 * 1024
AMARAN = 12 * 1024 * 1024
# dokumen yang dilanggan halaman v105 (connect + KUMP); B = dibahagi (bahagian {id,n}), R = ringkas_pt (bahagian + kamus)
PERLU = [('harian/status', ''), ('harian/hari_ini', ''), ('analisis/papan', 'B'), ('prestasi/portfolio_slot', ''),
         ('papertrade/ringkas_c', 'R'), ('papertrade/ringkas_m', 'R'), ('harian/trend', 'B'), ('posisi/lorong2', 'B'),
         ('prestasi/garis', 'B'), ('prestasi/mae', 'B'), ('prestasi/mfe', 'B'), ('prestasi/mae_atr', 'B'), ('prestasi/maefe_l2', 'B'),
         ('papertrade/langkau', 'B'), ('papertrade/watchlist', 'B'), ('prestasi/harian_kaedah', 'B'), ('kaedah/katalog', ''),
         ('registry/aktif', ''), ('meta/info', ''), ('sektor/snapshot', ''), ('jurnal/minggu', '')]
HARI_INI = ['harian/status', 'harian/hari_ini', 'prestasi/portfolio_slot', 'jurnal/minggu']   # analisis/papan dimuat bila Kaedah dibuka
LAMA = re.compile(r'^papertrade/(claude(_\d+)?|moomoo|moomoo_peta|senarai_beli(_\d+)?)$')


def padat(x):
    return json.dumps(x, ensure_ascii=False, separators=(',', ':'))


def baca_folder(d):
    out = {}
    for p in glob.glob(os.path.join(d, '*', '*.json')):
        kol, doc = os.path.basename(os.path.dirname(p)), os.path.splitext(os.path.basename(p))[0]
        with open(p, encoding='utf-8') as f:
            x = json.load(f)
        # format out_dir ArtifactData (jika dibalut): {data: {...}, version: n}
        if isinstance(x, dict) and isinstance(x.get('data'), dict) and set(x) <= {'data', 'version', 'id', 'doc_id', 'collection', 'updated_at', 'created_at'}:
            x = x['data']
        out[f'{kol}/{doc}'] = x
    return out


def baca_asas(p):
    if os.path.isdir(p):
        return baca_folder(p)
    with open(p, encoding='utf-8') as f:
        return json.load(f)


def semak(D):
    """Senarai amaran: dokumen diperlukan halaman yang tiada, atau bahagian/kamus yang induknya tidak sepadan."""
    am = []
    for nama, jenis in PERLU:
        d = D.get(nama)
        if d is None:
            am.append(f'{nama}: tiada (halaman memapar "tiada data" / mengira sendiri)')
            continue
        b = d.get('bahagian') if isinstance(d, dict) else None
        if jenis in ('B', 'R') and isinstance(b, dict):
            for i in range(2, int(b.get('n') or 1) + 1):
                c = D.get(f'{nama}_{i}')
                if not c or c.get('induk') != b.get('id'):
                    am.append(f'{nama}_{i}: tiada atau induk tidak sepadan (bahagian {i}/{b.get("n")})')
            for i in range(1, int(b.get('nk') or 0) + 1):
                c = D.get(f'{nama}_kamus_{i}')
                if not c or c.get('induk') != b.get('id'):
                    am.append(f'{nama}_kamus_{i}: tiada atau induk tidak sepadan')
    if not any(k.startswith('registry/') and k != 'registry/aktif' for k in D):
        am.append('registry/*: tiada (Lagi › Backtest kosong)')
    return am


def saiz_kumpulan(D, nama):
    """Bait JSON padat dokumen `nama` termasuk bahagian/kamus yang sepadan."""
    d = D.get(nama)
    if d is None:
        return 0
    n = len(padat(d).encode('utf-8'))
    b = d.get('bahagian') if isinstance(d, dict) else None
    if isinstance(b, dict):
        for k, v in D.items():
            if (k.startswith(nama + '_')) and isinstance(v, dict) and v.get('induk') == b.get('id'):
                n += len(padat(v).encode('utf-8'))
    return n


def bina(asas, db, html, tajuk, simpan_lama=False, kekal=()):
    D = {}
    for x in ([asas] if isinstance(asas, str) else (asas or [])):
        D.update(baca_asas(x))
    baru = baca_folder(db) if db else {}
    for k in list(baru):
        # --kekal-asas: dokumen (dan bahagiannya) yang dikekalkan daripada asas walaupun jana_db menghasilkannya
        if any(p in D and (k == p or re.fullmatch(re.escape(p) + r'_\d+', k)) for p in kekal):
            del baru[k]
    D.update(baru)
    buang = []
    if not simpan_lama and 'papertrade/ringkas_c' in D:
        for k in list(D):
            if LAMA.match(k) and (not k.startswith('papertrade/moomoo') or 'papertrade/ringkas_m' in D):
                buang.append(k)
                del D[k]
    with open(html, encoding='utf-8') as f:
        t = f.read()
    if t.count(SAMBUNG) != 1:
        raise SystemExit(f'baris pemuat db tidak ditemui tepat sekali dalam {html}')
    t = t.replace(SAMBUNG, TIRUAN)
    t = re.sub(r'^<title>[^<]*</title>\n?', '', t, count=1)
    js = padat(D).replace('</', '<\\/')
    out = f'<title>{tajuk}</title>\n<script>window.__DB={js};\n{MOCK}</script>\n' + t
    return out, D, baru, buang


def main(argv=None):
    ap = argparse.ArgumentParser(description='Bina fail HTML pratonton dashboard dengan db tiruan')
    ap.add_argument('--asas', nargs='+', help='db asas: fail JSON {"koleksi/doc": dokumen} atau folder <koleksi>/<doc>.json (salinan db live); '
                                            'beberapa asas = yang kemudian menindih yang awal')
    ap.add_argument('--kekal-asas', nargs='*', default=[], help='dokumen yang dikekalkan daripada asas (cth. analisis/papan yang lebih baharu)')
    ap.add_argument('--db', help='folder output jana_db.py --keluar (menindih asas)')
    ap.add_argument('--html', default=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dashboard_v2.html'))
    ap.add_argument('--tajuk', default='Pratonton Papan')
    ap.add_argument('--keluar', required=True)
    ap.add_argument('--simpan-lama', action='store_true', help='kekalkan papertrade/claude*, moomoo, senarai_beli* (tidak dibaca halaman)')
    a = ap.parse_args(argv)
    if not a.asas and not a.db:
        raise SystemExit('perlu --asas dan/atau --db')
    out, D, baru, buang = bina(a.asas, a.db, a.html, a.tajuk, a.simpan_lama, a.kekal_asas)
    with open(a.keluar, 'w', encoding='utf-8') as f:
        f.write(out)
    sz = len(out.encode('utf-8'))
    am = semak(D)
    hari = {k: saiz_kumpulan(D, k) for k in HARI_INI}
    lapor = dict(keluar=os.path.abspath(a.keluar), bait=sz, mb=round(sz / 1048576, 2), dokumen=len(D), dari_db=len(baru),
                 dibuang_lama=len(buang), amaran_saiz=(f'> 12 MB ({sz / 1048576:.1f} MB)' if sz > AMARAN else None),
                 hari_ini_bait=hari, hari_ini_jumlah=sum(hari.values()), amaran=am)
    print(json.dumps(lapor, ensure_ascii=False, indent=1))
    if sz > HAD:
        print(f'RALAT: {sz} bait melebihi had 16 MB Artifact', file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
