# Semakan data papertrade sebelum commit (peraturan dalam papertrade/SKEMA.md)
# Guna:  python3 BacktestShariah2/standard/sahkan.py            -> semak sahaja
#        python3 BacktestShariah2/standard/sahkan.py --betulkan -> susun lajur ikut skema, kemudian semak
#        ... --json [PATH]   -> tulis ringkasan ke PATH (lalai data/semakan/sahkan.json; skema dalam tulis_json)
#        ... --lorong-n N    -> saiz sampel semakan semula lorong 2 (lalai 0 = semua posisi)
# Kod keluar: 0 = lulus, 1 = ada RALAT (jangan push data), 2 = fail tiada / tidak boleh dibaca.
#
# Semakan sumber (lapisan 1, 24 Okt 2026; selain skema/aritmetik di bawah):
#   harga_beli C lawan buka bar hari beli (RALAT > 0.3%; semak_buka)
#   ambil alih (semak_ambil_alih): posisi C dibeli pada/selepas pengumuman dalam data/ambil_alih.csv tetapi tidak_sah
#       kosong = RALAT; posisi C terbuka bagi saham berharga terkunci (ambil_alih.calon_kunci / corak tapis) yang tiada
#       dalam senarai = AMARAN (sahkan dengan 8-K/berita, kemudian ambil_alih.py tambah)
#   bar sesi terakhir (semak_bar_sesi): posisi dipegang bagi saham tanpa bar sesi terakhir dalam stor + terkini.csv = AMARAN
#       (satu baris: bilangan + senarai); sesi posisi lebih baharu daripada data harga repo = AMARAN
#   lorong 2 dikira semula secara bebas (semak_lorong2): sampel berketentuan (cincangan sesi) dibanding dengan
#       keluar_henti/tarikh_keluar_henti/status_henti; beza keadaan = RALAT (AMARAN jika tutup dalam 0.5% paras keluar:
#       beza vendor boleh menterbalikkan keputusan); harga_keluar_henti ≠ buka bar keluar = AMARAN (buka yfinance boleh
#       berbeza daripada buka rasmi Moomoo; disahkan oleh standard/sampel_semak.py)
#   untung_akhir_pct / untung_henti_pct / untung_pct = harga/harga_beli − 1 (RALAT > 0.02 mata peratus; semak_posisi)
import json
import sys, os, csv, glob, re, argparse, hashlib
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
BS2 = os.path.dirname(HERE)
KOD = os.path.join(BS2, 'kod')
PT = os.path.join(os.path.dirname(HERE), 'papertrade')
STOR = os.path.join(os.path.dirname(HERE), 'data', 'harga', 'stor')
TERKINI = os.path.join(BS2, 'data', 'harga', 'terkini.csv')
SEJARAH = os.path.join(BS2, 'data', 'harga', 'sejarah.csv')
AMBIL_ALIH = os.path.join(BS2, 'data', 'ambil_alih.csv')
SEMAKAN = os.path.join(BS2, 'data', 'semakan', 'sahkan.json')
TOL_BUKA = 0.003   # harga_beli C lawan buka bar hari beli dalam stor (audit 24 Okt 2026: DAC M80/M90 164.162 lawan 170.19)
TOL_SAMBUNG = 0.003  # tutup bar bertindih (stor lawan terkini.csv / sejarah.csv) mesti sepadan sebelum bar disambung
LORONG_N = 0          # semakan semula lorong 2: 0 = semua posisi (semakan penuh +0.3 s; sampel kecil boleh terlepas kes jarang seperti VIAV/LITE)
TOL_SEMPADAN = 0.005  # beza keadaan lorong 2 apabila tutup dalam 0.5% paras keluar -> AMARAN, bukan RALAT

# Susunan lajur rasmi fail posisi (moomoo.csv, claude.csv, claude_N.csv)
POSISI = ['tarikh_beli', 'saham', 'kaedah', 'id_kaedah', 'sektor', 'industri', 'harga_beli', 'unit',
          'harga_terkini', 'untung_pct', 'hari', 'henti', 'sasaran', 'isyarat_keluar', 'keluar',
          'tarikh_keluar', 'harga_keluar', 'untung_akhir_pct', 'sumber', 'kaedah_kongsi', 'tarikh_isyarat',
          'nota', 'dikesan', 'tidak_sah', 'sebab_tidak_sah', 'tidak_dibeli', 'luar_peraturan',
          'harga_buka_rujukan', 'tarikh_beli_dirancang',
          # gred pada hari isyarat (standard/gred.py; tugasan_v3 §8)
          'gred_sektor', 'skor_sektor', 'gred_industri', 'skor_industri', 'rs_rating', 'gred_rs',
          'rs_sah', 'rs_tanda', 'rs_industri', 'rs_sumber', 'gred_pemangkin', 'mata_pemangkin', 'pemangkin', 'pemangkin_url', 'tarikh_earnings', 'hari_ke_earnings',
          'sumber_earnings', 'gred_qr', 'gred_keseluruhan', 'gred_pada',
          # dua lorong keluar (standard/keluar_lorong.py; sejak 17 Okt 2026): lorong 2 pegang selagi naik
          'keluar_henti', 'tarikh_keluar_henti', 'harga_keluar_henti', 'untung_henti_pct', 'status_henti',
          'tutup_semua']
LAJUR_GRED = ['gred_sektor', 'gred_industri', 'gred_rs', 'gred_pemangkin', 'gred_qr', 'gred_keseluruhan', 'gred_kewangan']
NILAI_GRED = {'', 'A', 'B', 'C', 'D', 'E', '–'}
WAJIB_POSISI = ['tarikh_beli', 'saham', 'kaedah', 'sektor', 'industri', 'harga_beli', 'unit',
                'harga_terkini', 'untung_pct', 'hari', 'isyarat_keluar', 'keluar', 'tarikh_keluar',
                'harga_keluar', 'untung_akhir_pct']
WAJIB_SENARAI = ['saham', 'kaedah', 'sektor', 'industri', 'pct_dipenuhi', 'harga_rujukan', 'henti',
                 'sasaran', 'tarikh_isyarat', 'tarikh_imbasan']
WAJIB_WATCH = ['Saham', 'Kaedah', 'Sektor', 'Industri', '% hampir']

TARIKH = re.compile(r'^\d{4}-\d{2}-\d{2}$')
BENAR = {'true', '1', 'ya'}
TOL = 0.02  # toleransi peratus (pembundaran 2 titik perpuluhan)


def benar(v):
    return str(v or '').strip().lower() in BENAR


def nombor(v):
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def kosong(v):
    return str(v if v is not None else '').strip() in ('', '-', 'nan', 'None')


def baca(p):
    with open(p, newline='', encoding='utf-8') as f:
        r = csv.DictReader(f)
        return list(r.fieldnames or []), list(r)


def tulis(p, lajur, rows):
    with open(p, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=lajur, extrasaction='raise')
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, '') for k in lajur})


def susun(lajur):
    """Lajur rasmi dahulu (ikut POSISI), lajur tambahan dikekalkan di hujung."""
    return POSISI + [c for c in lajur if c not in POSISI]


def fail_posisi_dalam(folder):
    c = sorted(glob.glob(os.path.join(folder, 'claude*.csv')),
               key=lambda p: int(re.search(r'claude_?(\d*)', os.path.basename(p)).group(1) or 1))
    return [os.path.join(folder, 'moomoo.csv')] + c


def fail_posisi():
    return fail_posisi_dalam(PT)


def semak_gred(nama, rows, ralat):
    for i, r in enumerate(rows, start=2):
        for c in LAJUR_GRED:
            if c in r and (r[c] or '') not in NILAI_GRED:
                ralat.append(f'{nama}:{i}: {c} tidak sah ({r[c]!r}); mesti A–E atau "–"')
        u = r.get('pemangkin_url') or ''
        if u:
            try:
                ok = all(str(x.get('url', '')).startswith('https://') and x.get('tajuk') for x in json.loads(u))
            except (ValueError, AttributeError, TypeError):
                ok = False
            if not ok:
                ralat.append(f'{nama}:{i}: pemangkin_url mesti JSON [{{"tajuk", "url" https}}]')
        for k in ('rs_rating', 'rs_industri'):
            v = nombor(r.get(k))
            if not kosong(r.get(k)) and (v is None or not 1 <= v <= 99):
                ralat.append(f'{nama}:{i}: {k} {r.get(k)!r} di luar 1–99')
        if (r.get('rs_sah') or '') not in ('', 'ya', 'tidak'):
            ralat.append(f'{nama}:{i}: rs_sah {r.get("rs_sah")!r} bukan ya/tidak')
        if (r.get('rs_sumber') or '') not in ('', 'pasaran', 'stor') and not re.fullmatch(r'anggaran sejarah pendek \(\d+ bar\)', r.get('rs_sumber') or ''):
            ralat.append(f'{nama}:{i}: rs_sumber {r.get("rs_sumber")!r} bukan pasaran/stor/anggaran sejarah pendek')


def semak_posisi(nama, lajur, rows, ralat, amaran, kunci):
    for c in WAJIB_POSISI:
        if c not in lajur:
            ralat.append(f'{nama}: lajur wajib tiada: {c}')
    if any(c not in lajur for c in WAJIB_POSISI):
        return
    akaun = 'moomoo' if nama == 'moomoo.csv' else 'claude'
    for i, r in enumerate(rows, start=2):
        t = f'{nama}:{i} {r["saham"]} {r["kaedah"]}'
        tdb = benar(r.get('tidak_dibeli'))
        if kosong(r['sektor']) or kosong(r['industri']):
            ralat.append(f'{t}: sektor/industri kosong')
        if benar(r.get('tidak_sah')) and kosong(r.get('sebab_tidak_sah')):
            ralat.append(f'{t}: tidak_sah tanpa sebab_tidak_sah (SKEMA: wajib)')
        if not TARIKH.match(r['tarikh_beli'] or '') and not tdb:
            ralat.append(f'{t}: tarikh_beli bukan YYYY-MM-DD ({r["tarikh_beli"]!r})')
        if tdb:
            # Baris TIDAK DIBELI: tiada harga beli, tidak dikemas kini, tidak dikira
            if not kosong(r['harga_beli']):
                ralat.append(f'{t}: tidak_dibeli tetapi harga_beli berisi')
            if r['isyarat_keluar'] != 'TIDAK DIBELI':
                ralat.append(f'{t}: tidak_dibeli tetapi isyarat_keluar bukan "TIDAK DIBELI"')
            if benar(r['keluar']):
                ralat.append(f'{t}: tidak_dibeli tetapi keluar=True')
            continue
        hb, ht, up = nombor(r['harga_beli']), nombor(r['harga_terkini']), nombor(r['untung_pct'])
        if hb is None or hb <= 0:
            ralat.append(f'{t}: harga_beli tidak sah ({r["harga_beli"]!r})')
            continue
        u = nombor(r['unit'])
        if u is None or u <= 0 or u != int(u):
            ralat.append(f'{t}: unit tidak sah ({r["unit"]!r})')
        elif akaun == 'claude' and u != 1:
            ralat.append(f'{t}: Papertrade C mesti 1 unit (dapat {r["unit"]})')
        if ht is not None and up is not None and abs((ht / hb - 1) * 100 - up) > TOL:
            ralat.append(f'{t}: untung_pct {up} != (harga_terkini/harga_beli-1)*100 = {(ht / hb - 1) * 100:.2f}')
        if benar(r['keluar']):
            hk, ua = nombor(r['harga_keluar']), nombor(r['untung_akhir_pct'])
            if not TARIKH.match(r['tarikh_keluar'] or '') or hk is None:
                ralat.append(f'{t}: keluar=True tetapi tarikh_keluar/harga_keluar kosong')
            else:
                if r['tarikh_keluar'] < r['tarikh_beli']:
                    ralat.append(f'{t}: tarikh_keluar {r["tarikh_keluar"]} sebelum tarikh_beli')
                if ua is None or abs((hk / hb - 1) * 100 - ua) > TOL:
                    ralat.append(f'{t}: untung_akhir_pct {ua} != (harga_keluar/harga_beli-1)*100 = {(hk / hb - 1) * 100:.2f}')
        elif not kosong(r['tarikh_keluar']) or not kosong(r['harga_keluar']):
            ralat.append(f'{t}: keluar=False tetapi tarikh_keluar/harga_keluar berisi')
        semak_lorong(t, r, hb, ralat, amaran)
        k = (akaun, r['kaedah'], r['saham'], r['tarikh_beli'])
        if k in kunci:
            ralat.append(f'{t}: bertindih dengan {kunci[k]} (kaedah+saham+tarikh_beli)')
        else:
            kunci[k] = f'{nama}:{i}'


def _baca_buka(p, D, saham=None):
    if not os.path.exists(p):
        return D
    with open(p, newline='', encoding='utf-8') as f:
        for r in csv.DictReader(f):
            t = r.get('ticker')
            if saham is not None and t not in saham:
                continue
            d, o = str(r.get('date') or ''), nombor(r.get('open'))
            if len(d) == 8 and o:
                D[(t, f'{d[:4]}-{d[4:6]}-{d[6:]}')] = o
    return D


def buka_stor(stor=STOR, saham=None):
    """(O, MM): O = {(saham, 'YYYY-MM-DD'): buka} daripada harga_A/B.csv stor (konvensyen stor; buka Moomoo rasmi sudah
    ditampal oleh lejar.py tampal_moomoo jika beza > 0.5%), MM = buka_moomoo.csv (buka rasmi kline Moomoo yang disahkan).
    saham: had kepada set ticker ini (bacaan lebih laju). Fail tiada -> {}."""
    O, MM = {}, {}
    for nm in ('harga_A.csv', 'harga_B.csv'):
        _baca_buka(os.path.join(stor, nm), O, saham)
    _baca_buka(os.path.join(stor, 'buka_moomoo.csv'), MM, saham)
    return O, MM


def isy(d):
    """20261023 / '20261023' / '2026-10-23' -> '2026-10-23'."""
    s = str(d).strip().replace('-', '')[:8]
    return f'{s[:4]}-{s[4:6]}-{s[6:]}' if len(s) == 8 and s.isdigit() else ''


def muat_bar(stor, saham, terkini=None, sejarah=None):
    """Bar harian bagi ticker dalam `saham` untuk semakan sumber (bacaan bebas; tidak memakai keluar_lorong/jana_db):
    stor harga_A/B.csv (konvensyen backtest) + sejarah.csv di hadapan bar pertama stor + terkini.csv selepas bar terakhir
    stor; sambungan hanya jika tutup bar bertindih sepadan (TOL_SAMBUNG; tidak sepadan = faktor belum dilaras, stor sahaja).
    Pulang (F, sesi, O): F = {ticker: dict(ix=['YYYY-MM-DD'], o, h, l, c, v (numpy), sumber=['stor'|'terkini'|'sejarah'])},
    sesi = tarikh bar terakhir merentas stor + terkini.csv (semua ticker) atau '', O = {(ticker, tarikh): buka} bar stor sahaja
    (sama dengan buka_stor)."""
    import numpy as np
    import pandas as pd
    L = ['ticker', 'date', 'open', 'high', 'low', 'close', 'volume']

    def baca(paths):
        d = [pd.read_csv(p, usecols=lambda c: c in L) for p in paths if p and os.path.exists(p)]
        d = [x.reindex(columns=L) for x in d if len(x.columns) >= 6]
        return pd.concat(d, ignore_index=True) if d else pd.DataFrame(columns=L)

    S = baca([os.path.join(stor, f) for f in ('harga_A.csv', 'harga_B.csv')])
    T = baca([terkini]) if terkini else S.iloc[:0]
    J = baca([sejarah]) if sejarah else S.iloc[:0]
    sesi = max([int(x.date.max()) for x in (S, T) if len(x)] or [0])
    sesi = isy(sesi) if sesi else ''
    saham = set(saham)
    S, T, J = (x[x.ticker.isin(saham)].assign(date=lambda z: z.date.astype(int)).sort_values(['ticker', 'date'])
               .drop_duplicates(['ticker', 'date'], keep='last') for x in (S, T, J))
    S = S.assign(sumber='stor')
    awal, akhir = S.groupby('ticker').date.min(), S.groupby('ticker').date.max()
    bahagian = [S]
    if len(J):   # sejarah sebelum bar pertama stor: hanya jika median nisbah tutup bertindih sepadan
        sama = S.merge(J, on=['ticker', 'date'], suffixes=('', '_j'))
        r = (sama.close / sama.close_j).groupby(sama.ticker).median()
        ok = set(r.index[(r - 1).abs() <= TOL_SAMBUNG])
        bahagian.append(J[J.ticker.isin(ok) & (J.date < J.ticker.map(awal))].assign(sumber='sejarah'))
    if len(T):   # terkini.csv selepas bar terakhir stor: hanya jika bar bertindih terakhir sepadan
        sama = S.merge(T, on=['ticker', 'date'], suffixes=('', '_k')).groupby('ticker').tail(1)
        buruk = set(sama.ticker[((sama.close_k / sama.close) - 1).abs() > TOL_SAMBUNG])
        bahagian.append(T[~T.ticker.isin(buruk) & (T.date > T.ticker.map(akhir).fillna(0))].assign(sumber='terkini'))
    G = pd.concat(bahagian, ignore_index=True).sort_values(['ticker', 'date'], kind='stable')
    peta = {d: isy(d) for d in G.date.unique()}
    ds = [peta[d] for d in G.date.to_numpy()]
    st = G.sumber.to_numpy()
    O = {(t, d): float(o) for t, d, o, s_ in zip(G.ticker.to_numpy(), ds, G.open.to_numpy(float), st) if s_ == 'stor' and o > 0}
    F = {}
    tk = G.ticker.to_numpy()
    if len(tk):
        sempadan = np.flatnonzero(tk[1:] != tk[:-1]) + 1
        mula = np.r_[0, sempadan]; tamat = np.r_[sempadan, len(tk)]
        o, h, l, c, v = (G[x].to_numpy(float) for x in ('open', 'high', 'low', 'close', 'volume'))
        for m, e in zip(mula, tamat):
            F[tk[m]] = dict(ix=ds[m:e], o=o[m:e], h=h[m:e], l=l[m:e], c=c[m:e], v=v[m:e], sumber=list(st[m:e]))
    return F, sesi, O


def frame_pd(x):
    """dict muat_bar -> DataFrame open/high/low/close/volume berindeks Timestamp (format kod/ambil_alih.py)."""
    import pandas as pd
    return pd.DataFrame(dict(open=x['o'], high=x['h'], low=x['l'], close=x['c'], volume=x['v']),
                        index=pd.to_datetime(x['ix']))


def beza_buka(r, O, MM, tol=TOL_BUKA):
    """Beza harga_beli lawan buka bar hari beli (pecahan), atau None jika tidak disemak / sepadan: baris tidak_dibeli, tanpa
    harga beli, harga beli sementara (nota 'buka sementara'), tiada bar dalam stor, atau sepadan dengan buka stor atau buka
    Moomoo disahkan (buka_moomoo.csv) dalam toleransi. Pulang (beza, buka stor)."""
    if benar(r.get('tidak_dibeli')) or 'buka sementara' in (r.get('nota') or ''):
        return None
    hb = nombor(r.get('harga_beli')); k = (r.get('saham'), r.get('tarikh_beli'))
    o = O.get(k)
    if not hb or not o:
        return None
    if abs(hb / o - 1) <= tol or (k in MM and abs(hb / MM[k] - 1) <= tol):
        return None
    return hb / o - 1, o


def semak_buka(nama, rows, O, MM, ralat):
    """Papertrade C: harga_beli = buka rasmi bar hari beli (SKEMA). Akaun M dikecualikan (harga isian sim)."""
    for i, r in enumerate(rows, start=2):
        x = beza_buka(r, O, MM)
        if x:
            ralat.append(f'{nama}:{i} {r["saham"]} {r["kaedah"]}: harga_beli {r["harga_beli"]} ≠ buka bar {r["tarikh_beli"]} '
                         f'dalam stor {x[1]:g} (beza {x[0] * 100:+.2f}% > {TOL_BUKA * 100:g}%; betulkan dengan '
                         'standard/betul_harga_beli.py)')


def semak_lorong(t, r, hb, ralat, amaran):
    """Lorong 2 (pegang selagi naik): keluar_henti=True => tarikh/harga/untung lengkap dan konsisten;
    tutup_semua = keluar & keluar_henti. Lajur kosong = belum dinilai (amaran sahaja; diisi oleh keluar_lorong.py)."""
    if 'tutup_semua' not in r:
        return
    if kosong(r.get('tutup_semua')):
        amaran.append(f'{t}: lorong 2 belum dinilai (jalankan standard/keluar_lorong.py)')
        return
    if benar(r.get('keluar_henti')):
        h, u = nombor(r.get('harga_keluar_henti')), nombor(r.get('untung_henti_pct'))
        if not TARIKH.match(r.get('tarikh_keluar_henti') or '') or h is None:
            ralat.append(f'{t}: keluar_henti=True tetapi tarikh_keluar_henti/harga_keluar_henti kosong')
        elif r['tarikh_keluar_henti'] < r['tarikh_beli']:
            ralat.append(f'{t}: tarikh_keluar_henti {r["tarikh_keluar_henti"]} sebelum tarikh_beli')
        elif u is None or abs((h / hb - 1) * 100 - u) > TOL:
            ralat.append(f'{t}: untung_henti_pct {u} != (harga_keluar_henti/harga_beli-1)*100 = {(h / hb - 1) * 100:.2f}')
    elif not kosong(r.get('tarikh_keluar_henti')) or not kosong(r.get('harga_keluar_henti')):
        ralat.append(f'{t}: keluar_henti=False tetapi tarikh_keluar_henti/harga_keluar_henti berisi')
    jangka = benar(r.get('keluar')) and benar(r.get('keluar_henti'))
    if benar(r.get('tutup_semua')) != jangka:
        ralat.append(f'{t}: tutup_semua {r.get("tutup_semua")} != keluar & keluar_henti ({jangka})')


# ---------------------------------------------------------------- semakan sumber (lapisan 1, 24 Okt 2026)
def dibeli(r):
    return not benar(r.get('tidak_dibeli')) and bool(nombor(r.get('harga_beli'))) and bool(r.get('tarikh_beli'))


def dipegang(r):
    """Posisi dibeli yang belum tutup kedua-dua lorong (tutup_semua kosong -> ikut lorong 1)."""
    ts = r.get('tutup_semua')
    return dibeli(r) and not benar(ts if not kosong(ts) else r.get('keluar'))


def semak_ambil_alih(posisi, F, ralat, amaran, senarai=AMBIL_ALIH):
    """posisi = [(nama fail, baris, r)] Papertrade C. (1) RALAT: dibeli pada/selepas tarikh_umum terawal saham dalam senarai sah
    (bayaran bukan 'bukan') tetapi tidak_sah kosong (kod/tidak_layak.py posisi --tulis belum dijalankan). (2) AMARAN: posisi
    terbuka (bukan tidak_sah) bagi saham TIADA dalam senarai yang harganya terkunci (ambil_alih.calon_kunci: median julat 10 bar
    <= 0.6% dan ATR14 <= 0.5%) atau corak ambil alih automatik (ambil_alih.tapis). Pulang senarai saham amaran."""
    sys.path.insert(0, KOD)
    import ambil_alih as AA
    sen = AA.baca_senarai(senarai)
    dalam = {r['saham'] for r in sen}
    umum = {}
    for r in sen:
        if (r.get('bayaran') or '').strip().lower() != 'bukan' and r.get('tarikh_umum'):
            umum[r['saham']] = min(umum.get(r['saham'], r['tarikh_umum']), r['tarikh_umum'])
    buka = {}
    for nama, i, r in posisi:
        if not dibeli(r):
            continue
        t = r['saham']
        if t in umum and r['tarikh_beli'] >= umum[t] and not benar(r.get('tidak_sah')):
            ralat.append(f'{nama}:{i} {t} {r["kaedah"]}: dibeli {r["tarikh_beli"]} pada/selepas pengumuman ambil alih {umum[t]} '
                         '(data/ambil_alih.csv) tetapi tidak_sah kosong; jalankan kod/tidak_layak.py posisi --tulis')
        if dipegang(r) and not benar(r.get('tidak_sah')) and t not in dalam:
            buka.setdefault(t, []).append(r)
    import numpy as np
    pra_kunci, pra_corak = set(), set()   # pra-tapis numpy (syarat perlu sahaja; keputusan tetap oleh ambil_alih.py)
    for t in buka:
        x = F.get(t)
        if not x or len(x['c']) < 15:
            continue
        o, h, l, c = x['o'], x['h'], x['l'], x['c']
        with np.errstate(invalid='ignore', divide='ignore'):
            jul = (h - l) / c
            if 0 < np.median(jul[-AA.BAR_KUNCI:]) <= 0.006:
                pra_kunci.add(t)
            w = slice(max(1, len(c) - AA.CARI_BAR), len(c))
            if len(c) >= 60 and np.any((o[w] / c[w.start - 1:-1] - 1 >= AA.JURANG_MIN) & (jul[w] <= AA.JULAT_UMUM_MAKS)):
                pra_corak.add(t)
    calon = {x['saham']: x for x in AA.calon_kunci({t: frame_pd(F[t]) for t in pra_kunci}, pra_kunci)}
    corak = {t: x for t, x in AA.tapis({t: frame_pd(F[t]) for t in pra_corak}, None, senarai=[]).items()}
    keluar = []
    for t in sorted(set(calon) | set(corak)):
        n = len(buka[t])
        if t in corak:
            u = corak[t]['tarikh_umum']; ns = sum(r['tarikh_beli'] >= u for r in buka[t])
            sebab = f'corak ambil alih automatik (umum {u}; {ns} posisi dibeli selepasnya patut tidak_sah)'
        else:
            x = calon[t]
            sebab = f"harga terkunci (median julat 10 bar {x['julat_med_pct']}%, ATR14 {x['atr_pct']}%, bar akhir {x['akhir']})"
        amaran.append(f'ambil alih? {t}: {n} posisi C terbuka; {sebab}; tiada dalam data/ambil_alih.csv — sahkan dengan '
                      '8-K/berita, kemudian kod/ambil_alih.py tambah (--bayaran tunai|saham|campuran|bukan)')
        keluar.append(t)
    return keluar


def semak_bar_sesi(posisi, F, sesi, amaran, had=40):
    """AMARAN (satu baris): posisi dipegang (M dan C) bagi saham tanpa bar sesi `sesi` dalam stor + terkini.csv — harga sesi itu
    bukan daripada sumber repo (Moomoo rutin, atau basi). Juga AMARAN jika sesi posisi (tarikh beli/keluar terkini dalam CSV)
    lebih baharu daripada `sesi`. Pulang {saham: (bar akhir, bil posisi)}."""
    if not sesi:
        return {}
    tiada = {}
    for _, _, r in posisi:
        if not dipegang(r):
            continue
        t = r['saham']; x = F.get(t)
        akhir = x['ix'][-1] if x else ''
        if akhir < sesi:
            a, n = tiada.get(t, (akhir, 0)); tiada[t] = (akhir, n + 1)
    if tiada:
        sen = [f'{t} ({a or "tiada bar"}, {n})' for t, (a, n) in sorted(tiada.items(), key=lambda z: (-z[1][1], z[0]))]
        lagi = f' … dan {len(sen) - had} lagi' if len(sen) > had else ''
        amaran.append(f'bar sesi {sesi}: {len(tiada)} saham ({sum(n for _, n in tiada.values())} posisi dipegang) tiada bar sesi '
                      f'itu dalam stor + terkini.csv; harga sesi itu bukan daripada sumber repo (semak Moomoo / tunggu '
                      f'harga_harian): ' + ', '.join(sen[:had]) + lagi)
    sp = max((r.get(k) or '' for _, _, r in posisi if dibeli(r)
              for k in ('tarikh_beli', 'tarikh_keluar', 'tarikh_keluar_henti')), default='')
    if sp > sesi:
        amaran.append(f'sesi posisi {sp} lebih baharu daripada data harga repo {sesi} (stor + terkini.csv belum dikemas kini): '
                      'semakan sumber sesi itu tidak lengkap')
    return tiada


def chandelier(o, h, l, c, k, akhir, ganda, n_atr):
    """Lorong 2 dikira semula secara bebas (bukan keluar_lorong.lorong_henti): ATR = purata mudah n_atr julat sebenar (bar
    pertama = tinggi − rendah); bagi bar j = k..akhir: puncak = tutup tertinggi k..j, paras = maks(paras, puncak − ganda × ATR[j])
    (ATR belum ada -> tiada paras); tutup[j] < paras -> jual buka j+1. Pulang (jenis 'keluar'|'menunggu'|'pegang', indeks bar
    keluar (keluar) / bar isyarat (menunggu) / None, P = paras setiap bar 0..akhir (−inf sebelum k / tanpa ATR), indeks bar
    isyarat atau None)."""
    import numpy as np
    c = np.asarray(c[:akhir + 1], float); h = np.asarray(h[:akhir + 1], float); l = np.asarray(l[:akhir + 1], float)
    pc = np.r_[c[0], c[:-1]]
    tr = np.maximum(h - l, np.maximum(np.abs(h - pc), np.abs(l - pc)))
    tr[0] = h[0] - l[0]
    cs = np.r_[0.0, np.cumsum(tr)]
    a = np.full(len(c), np.nan)
    if len(c) >= n_atr:
        a[n_atr - 1:] = (cs[n_atr:] - cs[:-n_atr]) / n_atr
    calon = np.maximum.accumulate(c[k:]) - ganda * a[k:]
    P = np.full(len(c), -np.inf)
    P[k:] = np.maximum.accumulate(np.where(np.isnan(calon), -np.inf, calon))
    kena = np.flatnonzero(c[k:] < P[k:])
    if not len(kena):
        return 'pegang', None, P, None
    j = k + int(kena[0])
    return ('keluar', j + 1, P, j) if j + 1 <= akhir else ('menunggu', j, P, j)


def margin_lorong(c, P, *bar):
    """min |tutup − paras| ÷ tutup pada bar keputusan yang berbeza (bar isyarat kiraan semula dan bar isyarat CSV)."""
    m = [abs(c[j] - P[j]) / c[j] for j in bar if j is not None and 0 <= j < len(P) and P[j] > -float('inf')]
    return min(m) if m else float('inf')


def keadaan_csv(r):
    """Keadaan lorong 2 dalam CSV: ('keluar', tarikh) | ('menunggu', 'D Mmm') | ('pegang', None)."""
    st = r.get('status_henti') or ''
    if benar(r.get('keluar_henti')):
        return 'keluar', r.get('tarikh_keluar_henti') or ''
    m = re.match(r'Tutup [\d.]+ bawah .* pada (\d{1,2} \w{3})', st)
    if m:
        return 'menunggu', m.group(1)
    return 'pegang', None


def sampel_lorong(calon, sesi, n):
    """Sampel berketentuan: separuh daripada posisi yang lorong 2 sudah keluar/menunggu, selebihnya posisi pegang; susunan
    cincangan sha1(sesi|kunci). n <= 0 -> semua."""
    if n <= 0 or len(calon) <= n:
        return list(calon)
    kunci = lambda x: hashlib.sha1(f'{sesi}|{x[0]}|{x[2]["saham"]}|{x[2]["kaedah"]}|{x[2]["tarikh_beli"]}'.encode()).hexdigest()
    ada = sorted([x for x in calon if keadaan_csv(x[2])[0] != 'pegang'], key=kunci)
    pegang = sorted([x for x in calon if keadaan_csv(x[2])[0] == 'pegang'], key=kunci)
    q = min(len(ada), n // 2)
    pilih = ada[:q] + pegang[:n - q]
    if len(pilih) < n:
        pilih += ada[q:q + n - len(pilih)]
    return pilih


def semak_lorong2(posisi, F, sesi, ralat, amaran, n=LORONG_N, rasmi=None, MM=None):
    """Kira semula lorong 2 bagi sampel posisi (M dan C; status_henti peraturan semasa; keluar paksa isyarat palsu/delist
    dilangkau) dan banding dengan CSV. Keadaan CSV mesti sama dengan pengiraan hingga bar terakhir data atau satu bar
    sebelumnya (CSV boleh ketinggalan satu sesi); CSV yang mendahului data repo (saham tanpa bar sesi terakhir) tidak disemak.
    Beza keadaan = RALAT (AMARAN jika margin < TOL_SEMPADAN atau CSV bertanda sejarah pendek). harga_keluar_henti lawan buka bar
    keluar (stor, buka_moomoo.csv atau harga_beli C 'buka rasmi' sama hari) > TOL_BUKA = AMARAN. Pulang kiraan dict."""
    sys.path.insert(0, HERE)
    import keluar_lorong as KL   # pemalar peraturan sahaja (GANDA_ATR, TEMPOH_ATR, PENANDA, hb); logik dikira di sini
    rasmi, MM = rasmi or {}, MM or {}
    calon = [x for x in posisi if dibeli(x[2]) and KL.PENANDA in (x[2].get('status_henti') or '')
             and not (x[2].get('status_henti') or '').startswith(('Keluar: isyarat palsu', 'Keluar: delist'))]
    kira = dict(calon=len(calon), disemak=0, sama=0, beza=0, sempadan=0, harga=0, tidak_disemak=0)
    for nama, i, r in sampel_lorong(calon, sesi, n):
        t = f'{nama}:{i} {r["saham"]} {r["kaedah"]} {r["tarikh_beli"]}'
        x = F.get(r['saham']); hbeli = nombor(r['harga_beli'])
        if not x or r['tarikh_beli'] not in x['ix']:
            kira['tidak_disemak'] += 1
            continue
        ix, o, h, l, c = x['ix'], x['o'], x['h'], x['l'], x['c']
        k = ix.index(r['tarikh_beli'])
        if not o[k] > 0 or abs(o[k] / hbeli - 1) > KL.BEZA_HARGA_MAKS:
            kira['tidak_disemak'] += 1
            continue
        N = len(c) - 1
        cv = keadaan_csv(r)
        R = {}
        for e in (N, N - 1):
            if e >= k:
                jn, j, P, js = chandelier(o, h, l, c, k, e, KL.GANDA_ATR, KL.TEMPOH_ATR)
                R[e] = (jn, ix[j] if jn == 'keluar' else (KL.hb(ix[j]) if jn == 'menunggu' else None), P, js)
        if any((v[0], v[1]) == cv for v in R.values()):
            kira['disemak'] += 1; kira['sama'] += 1
            if cv[0] == 'keluar':
                j = ix.index(cv[1]); hk = nombor(r.get('harga_keluar_henti')); kk = (r['saham'], cv[1])
                ok = [v for v in (o[j], MM.get(kk), rasmi.get(kk)) if v and hk and abs(hk / v - 1) <= TOL_BUKA]
                if hk and not ok:
                    kira['harga'] += 1
                    amaran.append(f'{t}: harga_keluar_henti {r["harga_keluar_henti"]} ≠ buka bar {cv[1]} {o[j]:g} ({x["sumber"][j]}; '
                                  f'beza {(hk / o[j] - 1) * 100:+.2f}%) — sahkan dengan kline Moomoo (standard/sampel_semak.py)')
            continue
        akhir = R.get(N)
        dulu = akhir and (akhir[0] == 'pegang' and (
            (cv[0] == 'menunggu' and cv[1] not in {KL.hb(d) for d in ix[k:]}) or (cv[0] == 'keluar' and cv[1] > ix[N]))
            or akhir[0] == 'menunggu' and cv[0] == 'keluar' and cv[1] > ix[N])
        if dulu:
            kira['tidak_disemak'] += 1     # CSV memakai bar selepas data repo (Moomoo rutin): tidak boleh disemak di sini
            continue
        kira['disemak'] += 1
        kira_r = akhir or next(iter(R.values()))
        if cv[0] == 'keluar' and cv[1] in ix:
            jc = ix.index(cv[1]) - 1                      # bar isyarat CSV = sehari sebelum keluar
        elif cv[0] == 'menunggu':
            jc = next((j for j in range(k, N + 1) if KL.hb(ix[j]) == cv[1]), None)
        else:
            jc = None
        m = margin_lorong(c, kira_r[2], kira_r[3], jc)
        teks = (f'{t}: lorong 2 CSV {cv[0]} {cv[1] or ""} ≠ kiraan semula {kira_r[0]} {kira_r[1] or ""} '
                f'(data hingga {ix[N]}; margin tutup–paras {m * 100:.2f}%)')
        if m < TOL_SEMPADAN or KL.TANDA_PENDEK in (r.get('status_henti') or ''):
            kira['sempadan'] += 1
            amaran.append(teks + ' — sempadan/sejarah pendek: beza data boleh menterbalikkan; semak manual')
        else:
            kira['beza'] += 1
            ralat.append(teks + ' — jalankan keluar_lorong.py --saham ' + r['saham'] + ' dengan stor lengkap')
    return kira


def semak_senarai(p, ralat, amaran):
    nama = os.path.basename(p)
    lajur, rows = baca(p)
    for c in WAJIB_SENARAI:
        if c not in lajur:
            ralat.append(f'{nama}: lajur wajib tiada: {c}')
    for c in ['nota_henti', 'buka_maks']:
        if c not in lajur:
            amaran.append(f'{nama}: lajur {c} tiada (wajib sejak 14 Okt 2026; diisi oleh imbasan 8:02 malam)')
    lihat, lain = set(), 0
    for i, r in enumerate(rows, start=2):
        t = f'{nama}:{i} {r.get("saham")} {r.get("kaedah")}'
        if kosong(r.get('sektor')) or kosong(r.get('industri')):
            ralat.append(f'{t}: sektor/industri kosong')
        if nombor(r.get('pct_dipenuhi')) != 100:
            ralat.append(f'{t}: senarai beli hanya untuk isyarat 100% (dapat {r.get("pct_dipenuhi")})')
        if r.get('destinasi') not in (None, '', 'Claude'):
            lain += 1
        k = (r.get('saham'), r.get('kaedah'), r.get('tarikh_isyarat'))
        if k in lihat:
            ralat.append(f'{t}: baris bertindih (saham+kaedah+tarikh_isyarat)')
        lihat.add(k)
    if lain:
        amaran.append(f'{nama}: {lain} baris destinasi bukan Claude (mod Papertrade C sahaja; belian tetap ke Claude)')


def semak_watch(p, ralat, amaran):
    nama = os.path.basename(p)
    lajur, rows = baca(p)
    for c in WAJIB_WATCH:
        if c not in lajur:
            ralat.append(f'{nama}: lajur wajib tiada: {c}')
    if any(c not in lajur for c in WAJIB_WATCH):
        return
    lihat = set()
    for i, r in enumerate(rows, start=2):
        t = f'{nama}:{i} {r["Saham"]} {r["Kaedah"]}'
        if kosong(r['Sektor']) or kosong(r['Industri']):
            ralat.append(f'{t}: sektor/industri kosong')
        v = nombor(r['% hampir'])
        if v is None or not 90 <= v <= 100:
            ralat.append(f'{t}: % hampir {r["% hampir"]} di luar 90–100 (terkeluar signal mesti dibuang)')
        k = (r['Saham'], r['Kaedah'])
        if k in lihat:
            ralat.append(f'{t}: baris bertindih (saham+kaedah)')
        lihat.add(k)


def tulis_json(path, tarikh, ralat, amaran, info, n_posisi):
    """Ringkasan untuk dashboard/rutin: {"tarikh": sesi data terakhir yang disemak (YYYY-MM-DD), "dibina": masa UTC,
    "status": "ok"|"amaran"|"ralat", "n_ralat", "n_amaran", "ringkas": <= 20 baris pendek}."""
    pendek = lambda s: s if len(s) <= 200 else s[:197] + '…'
    rk = [f'{len(ralat)} ralat, {len(amaran)} amaran, {n_posisi} posisi dibeli diperiksa'] + [pendek(x) for x in info]
    ruang = 20 - len(rk)
    nr = min(len(ralat), max(ruang - (1 if amaran else 0) - (1 if len(ralat) > ruang else 0), 0))
    rk += ['RALAT ' + pendek(x) for x in ralat[:nr]]
    if len(ralat) > nr:
        rk.append(f'RALAT … dan {len(ralat) - nr} lagi')
    ruang = 20 - len(rk)
    na = min(len(amaran), ruang if len(amaran) <= ruang else ruang - 1)
    rk += ['AMARAN ' + pendek(x) for x in amaran[:na]]
    if len(amaran) > na and len(rk) < 20:
        rk.append(f'AMARAN … dan {len(amaran) - na} lagi')
    out = dict(tarikh=tarikh or datetime.now(timezone.utc).strftime('%Y-%m-%d'),
               dibina=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC'),
               status='ralat' if ralat else ('amaran' if amaran else 'ok'), n_ralat=len(ralat), n_amaran=len(amaran),
               ringkas=rk[:20])
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
        f.write('\n')
    return out


def main(argv=None):
    global PT
    ap = argparse.ArgumentParser(description='Semak data papertrade ikut SKEMA.md')
    ap.add_argument('--betulkan', action='store_true', help='susun lajur fail posisi ikut skema sebelum semak')
    ap.add_argument('--folder', default=PT, help='folder papertrade (lalai: BacktestShariah2/papertrade)')
    ap.add_argument('--stor', default=STOR, help='folder stor harga (harga_A/B.csv, buka_moomoo.csv) bagi semakan harga beli C')
    ap.add_argument('--terkini', help='terkini.csv (bar selepas stor; lalai data/harga/terkini.csv jika --stor = stor repo)')
    ap.add_argument('--sejarah', help='sejarah.csv (bar sebelum stor; lalai data/harga/sejarah.csv jika --stor = stor repo)')
    ap.add_argument('--ambil-alih', default=AMBIL_ALIH, help='senarai sah ambil alih (lalai data/ambil_alih.csv)')
    ap.add_argument('--lorong-n', type=int, default=LORONG_N, help='saiz sampel lorong 2 dikira semula (0 = semua)')
    ap.add_argument('--json', nargs='?', const=SEMAKAN, help='tulis ringkasan JSON (lalai data/semakan/sahkan.json)')
    a = ap.parse_args(argv)
    PT = a.folder
    ralat, amaran, kunci, info = [], [], {}, []
    data = {}
    for p in fail_posisi():
        if os.path.exists(p):
            data[p] = baca(p)
    semua = {r.get('saham') for _, rows in data.values() for r in rows if r.get('saham')}
    ada_stor = any(os.path.exists(os.path.join(a.stor, f)) for f in ('harga_A.csv', 'harga_B.csv'))
    repo = os.path.abspath(a.stor) == os.path.abspath(STOR)
    terkini = a.terkini or (TERKINI if repo else None)
    sejarah = a.sejarah or (SEJARAH if repo else None)
    F, sesi, O, MM = {}, '', {}, {}
    if ada_stor:
        F, sesi, O = muat_bar(a.stor, semua, terkini, sejarah)
        _baca_buka(os.path.join(a.stor, 'buka_moomoo.csv'), MM, semua)
    else:
        amaran.append(f'stor harga tiada ({a.stor}): semakan harga_beli lawan buka bar hari beli dan semakan sumber dilangkau')
    for p in fail_posisi():
        if p not in data:
            print(f'TIADA: {p}')
            if a.json:
                tulis_json(a.json, sesi, [f'TIADA: {p}'] + ralat, amaran, info, len(kunci))
            return 2
        lajur, rows = data[p]
        if a.betulkan:
            baru = susun(lajur)
            if baru != lajur:
                tulis(p, baru, rows)
                print(f'Disusun semula: {os.path.basename(p)} ({len(lajur)} -> {len(baru)} lajur)')
                lajur = baru
        semak_posisi(os.path.basename(p), lajur, rows, ralat, amaran, kunci)
        semak_gred(os.path.basename(p), rows, ralat)
        if os.path.basename(p) != 'moomoo.csv':
            semak_buka(os.path.basename(p), rows, O, MM, ralat)
    for nm, fn in [('senarai_beli.csv', semak_senarai), ('watchlist.csv', semak_watch)]:
        p = os.path.join(PT, nm)
        if os.path.exists(p):
            fn(p, ralat, amaran)
            semak_gred(nm, baca(p)[1], ralat)
    # semakan sumber (lapisan 1): ambil alih, bar sesi terakhir, lorong 2 dikira semula
    posisi = [(os.path.basename(p), i, r) for p in fail_posisi() for i, r in enumerate(data[p][1], start=2)]
    posisi_c = [x for x in posisi if x[0] != 'moomoo.csv']
    sp = max((x[2].get(k) or '' for x in posisi if dibeli(x[2]) for k in ('tarikh_beli', 'tarikh_keluar', 'tarikh_keluar_henti')
              if TARIKH.match(x[2].get(k) or '')), default='')
    if ada_stor:
        aa = semak_ambil_alih(posisi_c, F, ralat, amaran, a.ambil_alih)
        tb = semak_bar_sesi(posisi, F, sesi, amaran)
        rasmi = {(r['saham'], r['tarikh_beli']): nombor(r['harga_beli']) for _, _, r in posisi_c
                 if dibeli(r) and 'buka rasmi' in (r.get('nota') or '')}
        k2 = semak_lorong2(posisi, F, sesi, ralat, amaran, a.lorong_n, rasmi, MM)
        info.append(f"sumber: data harga hingga {sesi or '-'}; lorong 2 dikira semula {k2['disemak']}/{k2['calon']} "
                    f"(sampel {'semua' if a.lorong_n <= 0 else a.lorong_n}): sama {k2['sama']}, beza {k2['beza']}, "
                    f"sempadan {k2['sempadan']}, harga keluar beza {k2['harga']}, tidak disemak {k2['tidak_disemak']}; "
                    f"tanpa bar sesi {len(tb)} saham; calon ambil alih {len(aa)}")
    for x in amaran[:40]:
        print('AMARAN', x)
    if len(amaran) > 40:
        print(f'AMARAN ... dan {len(amaran) - 40} lagi')
    for x in ralat[:200]:
        print('RALAT', x)
    for x in info:
        print('SEMAK', x)
    print(f'Ringkasan: {len(ralat)} ralat, {len(amaran)} amaran, {len(kunci)} posisi dibeli diperiksa.')
    if a.json:
        tulis_json(a.json, max(sp, sesi), ralat, amaran, info, len(kunci))
        print(f'JSON: {a.json}')
    return 1 if ralat else 0


if __name__ == '__main__':
    sys.exit(main())
