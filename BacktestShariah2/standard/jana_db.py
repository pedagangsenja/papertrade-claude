# jana_db.py — dokumen db dashboard daripada fail repo (tanpa LLM), untuk sesi Claude harian yang hanya MENOLAK fail ke db
# (ArtifactData batch dengan file_path; tugasan_v3 §6). Menggantikan JSON yang dibina dengan tangan oleh rutin 6:02 / 7:47 / 9:35.
#
#   python3 BacktestShariah2/standard/jana_db.py --keluar <folder> [--versi versi.json]
#   -> <folder>/<koleksi>/<doc>.json, <folder>/batch_<n>.json (senarai writes ArtifactData; <= 50 tulisan dan < 900 KB
#      setiap batch) dan <folder>/ringkas.json. --versi: {"papertrade/claude": 14, …} (daripada senarai ArtifactData list)
#      supaya setiap tulisan membawa if_version; dokumen tanpa versi = dokumen baharu.
# Dokumen: papertrade/moomoo, papertrade/claude… (1:1 dengan claude*.csv), (senarai_beli tidak ditolak sejak 19 Okt 2026),
# papertrade/watchlist(+_2…), prestasi/ringkasan, prestasi/mae, prestasi/mae_atr (dibahagi), prestasi/harian_kaedah, prestasi/portfolio_slot, analisis/papan, harian/status,
# harian/trend (trend_status.py), posisi/lorong2(+_2…; lorong2_siri.py). sektor/snapshot dijana oleh tugasan
# mingguan (data/db/sektor_snapshot.json, jika ada; medan posisi dikemas kini di sini).
# Sejak 24 Okt 2026 (audit dashboard tab demi tab; pratonton cawangan pratonton-audit): prestasi/mae dibahagi (rows senarai
# [[kunci, %]]); prestasi/maefe_l2 (MAE/MFE tempoh lorong 2); papertrade/langkau (langkauan belian 9:35 NY); medan baris db
# kualiti, sasaran_dinamik, jenis_tidak_sah, earn_kini/earn_kini_h/earn_lalu; harian/status ralat (dokumen melebihi had
# dilangkau, bukan SystemExit), mod, sumber_harga (--sumber), saluran, beli_langkau.
import argparse, csv, glob, hashlib, json, os, re, statistics as stt, sys

import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
BS2 = os.path.dirname(HERE)
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(BS2, 'kod'))
import sahkan as SH  # noqa: E402
from bahagi_db import bahagi, padat, bait, HAD_DB  # noqa: E402
from pecah_claude import nilai, nombor_fail  # noqa: E402

PT = os.path.join(BS2, 'papertrade')
STOR = os.path.join(BS2, 'data', 'harga', 'stor')
MIN_TUTUP = 20
USD_POSISI = 1000
HAD_BATCH = 900_000
STATUS_HARGA = os.path.join(BS2, 'data', 'harga', 'status.json')
HAD_BAHAGI = 200000      # saiz setiap bahagian dokumen yang dibahagi
AMARAN_HAD = 0.8         # dokumen >= 80% had db -> amaran dalam harian/status.ralat
MOD_ACTIONS = os.path.join(BS2, 'MOD_ACTIONS')
LOG_RUTIN = os.path.join(HERE, 'binaan_v2_log_tambahan.md')
LEJAR_STATUS = os.path.join(BS2, 'lejar', 'status.json')
LANGKAU_MULA = '2026-10-14'   # rekod langkauan belian 9:35 NY (Papertrade C sahaja) bermula di sini
LAJ = ['ticker', 'date', 'open', 'high', 'low', 'close', 'volume']
# Kaedah yang sasaran keluarnya BERUBAH selepas hari isyarat (disemak dengan kod 24 Okt 2026): lajur `sasaran` CSV = paras
# hari isyarat, jadi "capai sasaran" boleh berlaku pada paras lain. Gelung enjin memakai tgt bar semalam setiap hari.
# Replika dengan sasaran dikunci pada hari isyarat (M19, M20 _kunci; M26 _isi_tgt; M47 _tgt_tetap; M100 _kunci_tgt) dan
# M18 (ATH; berubah hanya apabila sasaran dicapai) BUKAN dinamik.
SASARAN_DINAMIK = {'M01': 'SMA30 bergerak (bbm)', 'M02': 'buka masuk + 3 x (buka − henti); diketahui pada buka beli',
                   'M03': 'BB atas bergerak', 'M28': 'VWAP bergerak'}

PETA_WATCH = {'Saham': 'saham', 'Nama': 'nama', 'Kaedah': 'kaedah', 'Sektor': 'sektor', 'Industri': 'industri',
              'Harga': 'harga_terkini', '% hampir': 'pct_dipenuhi', 'Pencetus': 'pencetus', 'Keadaan semasa': 'sebab',
              'Syarat belum cukup': 'syarat_belum', 'Syarat dipenuhi': 'syarat_dipenuhi', 'Paras pencetus': 'paras',
              'Jarak %': 'jarak_pct', 'Tarikh masuk watchlist': 'ditambah', 'Hari dalam watchlist': 'hari', 'Skor': 'skor',
              'Set': 'set', 'tarikh_data': 'tarikh_data', 'dibina': None, 'disentuh': 'disentuh'}


def baris_db(r, peta=None):
    """Baris CSV -> baris db: medan kosong digugurkan, nilai bertaip (sama dengan pecah_claude.nilai)."""
    out = {}
    for k, v in r.items():
        if v in ('', None) or k == 'kewangan_butiran':   # JSON butiran kekal dalam CSV sahaja (had saiz db)
            continue
        if peta is not None:
            if k in peta and peta[k] is None:
                continue
            k = peta.get(k, k)
        out[k] = nilai(v) if k not in ('saham', 'nama', 'kaedah_kongsi', 'tarikh_isyarat', 'tarikh_beli', 'tarikh_data') else v
    return out


def earn_sebenar(db, r, K):
    """Tambah tarikh earnings seterusnya SEBENAR (kalendar gabungan kalendar_earnings.py) kepada baris db (bukan CSV): earn_seb,
    earn_seb_h (hari dagangan dari sesi rujukan), earn_seb_sumber. Sesi rujukan = tarikh QR asal (gred_pada "QR pada X"),
    tarikh_isyarat / tarikh_data, atau hari bekerja sebelum tarikh_beli. Gred QR asal tidak diubah (audit 23 Okt 2026)."""
    from datetime import date, timedelta
    import kalendar_earnings as KE
    m = re.search(r'QR pada (\d{4}-\d\d-\d\d)', r.get('gred_pada') or '')
    t0 = (m.group(1) if m else None) or r.get('tarikh_isyarat') or r.get('tarikh_data')
    if t0:
        D = date.fromisoformat(t0[:10])
    elif r.get('tarikh_beli'):
        D = date.fromisoformat(r['tarikh_beli'][:10]) - timedelta(days=1)
        while D.weekday() > 4:
            D -= timedelta(days=1)
    else:
        return db
    te, sb = KE.seterusnya(K, r.get('saham') or r.get('Saham'), D)
    if te:
        db.update(earn_seb=te.isoformat(), earn_seb_h=hari_dag(D + timedelta(days=1), te + timedelta(days=1)) if te > D else 0,
                  earn_seb_sumber=sb)
    return db


_CUTI = None


def hari_dag(a, b):
    """Bilangan hari dagangan NYSE dalam [a, b) (np.busday_count dengan cuti XNYS; exchange_calendars dipin kekangan.txt).
    Tanpa exchange_calendars: hari bekerja sahaja (anggaran lama)."""
    global _CUTI
    if _CUTI is None:
        try:
            import exchange_calendars as xc
            h = xc.get_calendar('XNYS').regular_holidays.holidays(pd.Timestamp('2000-01-01'), pd.Timestamp('2035-12-31'))
            _CUTI = np.array([d.date() for d in h], dtype='datetime64[D]')
        except Exception:
            _CUTI = np.array([], dtype='datetime64[D]')
    return int(np.busday_count(a, b, holidays=_CUTI))


def earn_kini(db, t, S, K, cache=None):
    """Medan db (bukan CSV; 24 Okt 2026, ikon 📅 halaman): earn_kini = earnings seterusnya pada/selepas sesi data terakhir S
    (bukan tarikh isyarat; kalendar_earnings.seterusnya), earn_kini_h = hari dagangan dari S (0 = pada S); earn_lalu =
    earnings terakhir sebelum S jika <= 3 hari dagangan lalu (ikon "semalam"). cache: {saham: medan} (sama bagi semua baris)."""
    if not S or not t:
        return db
    if cache is not None and t in cache:
        db.update(cache[t]); return db
    from datetime import date, timedelta
    import kalendar_earnings as KE
    D = date.fromisoformat(str(S)[:10]); x = {}
    te, _ = KE.seterusnya(K, t, D)
    if te:
        x.update(earn_kini=te.isoformat(), earn_kini_h=hari_dag(D + timedelta(days=1), te + timedelta(days=1)) if te > D else 0)
    tl, _ = KE.lalu(K, t, D)
    if tl and hari_dag(tl, D) <= 3:
        x['earn_lalu'] = tl.isoformat()
    if cache is not None:
        cache[t] = x
    db.update(x)
    return db


def jenis_tidak_sah(sebab):
    """sebab_tidak_sah -> 'ambil_alih' | 'tidak_cair' | 'kelas_berganda' | 'delist' | 'lain' (label pil halaman)."""
    s = (sebab or '').lower()
    if 'diambil alih' in s or 'ambil alih' in s:
        return 'ambil_alih'
    if 'tidak cair' in s:
        return 'tidak_cair'
    if 'kelas berganda' in s:
        return 'kelas_berganda'
    if 'delist' in s:
        return 'delist'
    return 'lain'


def bar_harga(stor, lajur=tuple(LAJ), terkini=None):
    """Bar harian stor (harga_A/B.csv) + bar terkini.csv SELEPAS bar terakhir stor setiap ticker (sama dengan
    trend_status.muat_harga; stor repo boleh ketinggalan satu sesi). DataFrame lajur `lajur`, date int."""
    lajur = list(lajur)
    fail = [os.path.join(stor, f) for f in ('harga_A.csv', 'harga_B.csv') if os.path.exists(os.path.join(stor, f))]
    if not fail:
        return pd.DataFrame(columns=lajur)
    fr = pd.concat([pd.read_csv(f, usecols=lajur) for f in fail], ignore_index=True)
    if terkini and os.path.exists(terkini):
        t = pd.read_csv(terkini, usecols=lajur)
        akhir = fr.groupby('ticker').date.max()
        t = t[t.date > t.ticker.map(akhir).fillna(0)]
        fr = pd.concat([fr, t], ignore_index=True)
    fr['date'] = fr.date.astype(int)
    return fr


def aktif_pada(r, S):
    """Posisi dibeli yang harganya dikemas kini pada sesi S: belum tutup kedua-dua lorong, atau beli/keluar pada S."""
    if SH.benar(r.get('tidak_dibeli')) or not r.get('harga_beli'):
        return False
    ts = r.get('tutup_semua')
    if not SH.benar(ts if ts not in (None, '') else r.get('keluar')):
        return True
    return S in (r.get('tarikh_beli'), r.get('tarikh_keluar'), r.get('tarikh_keluar_henti'))


def kualiti(M, C, S, stor, terkini=None):
    """{(akaun, saham, kaedah, tarikh_beli): [bendera…]} — kualiti data setiap baris (medan db `kualiti`; 24 Okt 2026):
    'bar_moomoo'   posisi aktif pada S tetapi saham tiada bar S dalam yfinance data/harga/terkini.csv (harga S daripada
                   skrin/kline Moomoo rutin; atau terkini.csv belum sesi S)
    'bar_sintetik' bar S atau bar hari beli dalam stor yang dipakai: buka = tinggi = rendah = tutup dan volum 0/tiada
    'beli_ne_buka' Papertrade C: harga_beli beza > 0.3% daripada buka bar hari beli dalam stor (sahkan.beza_buka)
    'keluar_dibuka_semula' keluar lorong 1 dibatalkan semula (nota 'dibuka semula', atau 'keluar dinilai semula' oleh
                   kod/dagangan.py dan kini terbuka)"""
    Si = int(S.replace('-', '')) if S else 0
    yf = set()
    if TERKINI and os.path.exists(TERKINI):
        tk = pd.read_csv(TERKINI, usecols=['ticker', 'date'])
        yf = set(tk.ticker[tk.date == Si])
    perlu = {Si} | {int(r['tarikh_beli'].replace('-', '')) for R in (M, C) for r in R if r.get('tarikh_beli')}
    fr = bar_harga(stor, LAJ, terkini)
    fr = fr[fr.date.isin(perlu)]
    sint = {(t, d) for t, d, o, h, l, c, v in zip(fr.ticker, fr.date, fr.open, fr.high, fr.low, fr.close, fr.volume)
            if o == h == l == c and not (v > 0)}
    O, MM = SH.buka_stor(stor, {r.get('saham') for r in C})
    out = {}
    for ak, R in (('M', M), ('C', C)):
        for r in R:
            if SH.benar(r.get('tidak_dibeli')) or not r.get('harga_beli'):
                continue
            b = []
            if S and aktif_pada(r, S) and r['saham'] not in yf:
                b.append('bar_moomoo')
            tb = int(r['tarikh_beli'].replace('-', '')) if r.get('tarikh_beli') else 0
            if (r['saham'], tb) in sint or (aktif_pada(r, S) and (r['saham'], Si) in sint):
                b.append('bar_sintetik')
            if ak == 'C' and SH.beza_buka(r, O, MM):
                b.append('beli_ne_buka')
            n = r.get('nota') or ''
            if 'dibuka semula' in n or ('keluar dinilai semula' in n and not SH.benar(r.get('keluar'))):
                b.append('keluar_dibuka_semula')
            if b:
                out[(ak, r['saham'], r.get('kaedah'), r.get('tarikh_beli'))] = b
    return out


def baris_posisi(r, ak, KAL, S, kual, cache):
    """Baris CSV posisi -> baris db ringkas_c/m dengan medan db sahaja: earn_seb*, earn_kini*, earn_lalu, kualiti,
    sasaran_dinamik (True sahaja), jenis_tidak_sah (baris tidak_sah sahaja)."""
    db = earn_kini(earn_sebenar(baris_db(r), r, KAL), r.get('saham'), S, KAL, cache)
    k = kual.get((ak, r.get('saham'), r.get('kaedah'), r.get('tarikh_beli')))
    if k:
        db['kualiti'] = k
    if (r.get('id_kaedah') or r.get('kaedah')) in SASARAN_DINAMIK:
        db['sasaran_dinamik'] = True
    if SH.benar(r.get('tidak_sah')):
        db['jenis_tidak_sah'] = jenis_tidak_sah(r.get('sebab_tidak_sah'))
    return db


def baca_csv(p):
    return SH.baca(p)[1] if os.path.exists(p) else []


def sah(r):
    return not (SH.benar(r.get('tidak_dibeli')) or SH.benar(r.get('tidak_sah')) or SH.benar(r.get('luar_peraturan')))


# ---------------------------------------------------------------- prestasi (peraturan sama dengan halaman; tugasan_v3 §7)
def prestasi(M, C, mae):
    cl = lambda x: max(0, min(1, x))

    def rows(ak, R):
        out = []
        for r in R:
            if not sah(r) or r.get('harga_beli') in (None, ''):
                continue
            kel = SH.benar(r.get('keluar'))
            u = float(r['untung_akhir_pct'] if kel else r['untung_pct'] or 0)
            k = f"{ak}|{r['saham']}|{r['kaedah']}|{r['tarikh_beli']}"
            out.append(dict(saham=r['saham'], kaedah=r['kaedah'], u=u, keluar=kel, hari=int(float(r.get('hari') or 0)),
                            dd=mae.get(k, min(u, 0))))
        return out

    def kpi(T):
        if not T:
            return {}
        us = [t['u'] for t in T]; w = min(T, key=lambda t: t['u'])
        return dict(dagangan=len(T), kadar_menang=round(100 * sum(u > 0 for u in us) / len(us), 1), untung_purata=round(stt.mean(us), 2),
                    untung_median=round(stt.median(us), 2), rugi_terbesar=round(w['u'], 2), rugi_terbesar_saham=f"{w['saham']} ({w['kaedah']})",
                    hari_purata=round(stt.mean(t['hari'] for t in T), 1), kaedah=len({t['kaedah'] for t in T}), keluar=sum(t['keluar'] for t in T),
                    penurunan_maks_purata=round(stt.mean(t['dd'] for t in T), 2),
                    untung_usd_sama=round(sum(us) / 100 * USD_POSISI, 2), modal_usd_sama=len(T) * USD_POSISI)

    def kaedah(T):
        g = {}
        for t in T:
            g.setdefault(t['kaedah'], []).append(t)
        out = []
        for k, a in g.items():
            us = [t['u'] for t in a]; n = len(a); avg = stt.mean(us); win = sum(u > 0 for u in us) / n
            dd = stt.mean(t['dd'] for t in a); worst = min(us)
            U = 0.6 * cl((avg + 5) / 15) + 0.4 * win; S_ = 0.6 * cl(1 + dd / 10) + 0.4 * cl(1 + worst / 20)
            sk = 100 * U * S_ * min(1, n / 5); gagal = 1 - win
            ntutup = sum(1 for t in a if t['keluar'])
            kep = ('BELUM CUKUP DATA' if ntutup < MIN_TUTUP else
                   'HENTIKAN' if (avg <= -3 or gagal >= .75 or round(sk) < 25) else
                   'TERUSKAN' if round(sk) >= 55 and avg > 0 else 'PERHATI')
            out.append(dict(kaedah=k, n=n, menang=round(100 * win, 1), purata=round(avg, 2), median=round(stt.median(us), 2),
                            terburuk=round(worst, 2), dd=round(dd, 2), gagal=round(100 * gagal, 1),
                            keluar_rugi=sum(1 for t in a if t['keluar'] and t['u'] < 0), tutup=ntutup, skor=round(sk, 1), keputusan=kep))
        return sorted(out, key=lambda x: -x['skor'])

    res = {}
    for nm, T in [('M', rows('M', M)), ('C', rows('C', C)), ('Combine', rows('M', M) + rows('C', C))]:
        K = kaedah(T)
        res[nm] = dict(kpi=kpi(T), kaedah=K, teruskan=[x['kaedah'] for x in K if x['keputusan'] == 'TERUSKAN'],
                       hentikan=[x['kaedah'] for x in K if x['keputusan'] == 'HENTIKAN'],
                       bil={k: sum(x['keputusan'] == k for x in K) for k in ['TERUSKAN', 'PERHATI', 'HENTIKAN', 'BELUM CUKUP DATA']},
                       teruk_gagal=[(x['kaedah'], x['gagal'], x['n']) for x in sorted([x for x in K if x['n'] >= 3], key=lambda x: -x['gagal'])[:5]],
                       teruk_rugi=[(x['kaedah'], x['terburuk']) for x in sorted(K, key=lambda x: x['terburuk'])[:5]],
                       teruk_keluar_rugi=[(x['kaedah'], x['keluar_rugi']) for x in sorted(K, key=lambda x: -x['keluar_rugi'])[:5]],
                       top=[(x['kaedah'], x['skor'], x['purata'], x['menang'], x['n']) for x in K[:5]])
    return res


def penurunan_maks(M, C, stor, terkini=None):
    """prestasi/mae: (rendah terendah sejak hari beli hingga kini, atau hingga sehari sebelum keluar + harga keluar) ÷ harga beli − 1.
    terkini: bar data/harga/terkini.csv selepas stor (stor repo)."""
    fr = bar_harga(stor, ('ticker', 'date', 'low'), terkini)
    L = {t: g.set_index('date')['low'] for t, g in fr.groupby('ticker')}
    out = {}
    for ak, R in (('M', M), ('C', C)):
        for r in R:
            hbv = SH.nombor(r.get('harga_beli'))
            if hbv is None or not hbv or SH.benar(r.get('tidak_dibeli')):
                continue
            k = f"{ak}|{r['saham']}|{r['kaedah']}|{r['tarikh_beli']}"
            b = int(r['tarikh_beli'].replace('-', '')); lo = L.get(r['saham'])
            if lo is None:
                continue
            if SH.benar(r.get('keluar')) and r.get('tarikh_keluar'):
                e = int(r['tarikh_keluar'].replace('-', '')); w = lo[(lo.index >= b) & (lo.index < e)].tolist()
                if SH.nombor(r.get('harga_keluar')) is not None:
                    w.append(float(r['harga_keluar']))
            else:
                w = lo[lo.index >= b].tolist()
            if not w:
                continue
            v = round(min(0.0, (min(w) / hbv - 1) * 100), 2)
            out[k] = min(v, out.get(k, 0.0))
    return out


def atr_isyarat(M, C, stor, n=14):
    """ATR14 % pada bar terakhir sebelum hari beli (hari isyarat) bagi setiap posisi: purata julat benar 14 hari ÷ tutup × 100
    (formula enjin.atr). Dipakai skor kaedah swing v2 untuk MAE ÷ ATR. Kunci sama dengan prestasi/mae."""
    fr = pd.concat([pd.read_csv(os.path.join(stor, f), usecols=['ticker', 'date', 'high', 'low', 'close']) for f in ('harga_A.csv', 'harga_B.csv')
                    if os.path.exists(os.path.join(stor, f))])
    A = {}
    for t, g in fr.groupby('ticker'):
        g = g.drop_duplicates('date', keep='last').sort_values('date').set_index('date'); c = g.close
        tr = pd.concat([g.high - g.low, (g.high - c.shift()).abs(), (g.low - c.shift()).abs()], axis=1).max(axis=1)
        A[t] = (tr.rolling(n).mean() / c * 100).dropna()
    out = {}
    for ak, R in (('M', M), ('C', C)):
        for r in R:
            a = A.get(r.get('saham'))
            if a is None or not r.get('tarikh_beli') or SH.benar(r.get('tidak_dibeli')):
                continue
            s = a[a.index < int(r['tarikh_beli'].replace('-', ''))]
            if len(s):
                out[f"{ak}|{r['saham']}|{r['kaedah']}|{r['tarikh_beli']}"] = round(float(s.iloc[-1]), 3)
    return out


HAD_RINGKAS = 200000


def kod_lajur(R):
    """Baris db -> bentuk padat ikut lajur (dashboard v90): (kolum, jenis, kamus, rows). jenis setiap lajur:
    'b' boolean (0/1), 'k' rentetan berulang (indeks kamus + 1), 'j' senarai/campuran berulang (kamus JSON, indeks + 1),
    '' nilai asal. Medan yang tiada = 0 bagi 'k'/'j', null bagi yang lain. Kamus dikongsi semua bahagian; halaman menyahkod
    kepada objek sama seperti baris_db()."""
    cols = sorted({k for r in R for k in r})
    jenis, kamus, lajur = [], {}, []
    for c in cols:
        v = [r.get(c) for r in R]
        s = [x for x in v if x is not None]
        if s and all(isinstance(x, bool) for x in s):
            jenis.append('b'); lajur.append([None if x is None else int(x) for x in v]); continue
        if s and all(isinstance(x, (str, list)) for x in s):
            js = any(isinstance(x, list) for x in s)
            k = [None if x is None else (json.dumps(x, ensure_ascii=False) if js else x) for x in v]
            u = sorted({x for x in k if x is not None})
            if len(u) < 0.6 * len(R):
                ix = {x: i for i, x in enumerate(u)}; kamus[c] = u
                jenis.append('j' if js else 'k'); lajur.append([0 if x is None else ix[x] + 1 for x in k]); continue
        jenis.append(''); lajur.append(v)
    return cols, jenis, kamus, [list(t) for t in zip(*lajur)]


def ringkas_pt(R, nama, meta, had=HAD_RINGKAS):
    """[(doc_id, dokumen)] padat bagi papertrade/ringkas_c|m (susunan baris dikekalkan):
    <nama> = meta + kolum + jenis + bahagian {id, n, nk} + rows bahagian 1; <nama>_2.._n = {induk, bahagian, rows};
    <nama>_kamus_1.._nk = {induk, kamus: [[lajur, mula, [nilai…]], …]} (senarai panjang dipecah ikut segmen)."""
    cols, jenis, kamus, rows = kod_lajur(R)
    ident = hashlib.sha1(padat(R).encode('utf-8')).hexdigest()[:12]
    asas_kosong = bait(dict(meta, kolum=cols, jenis=jenis, bahagian=dict(id=ident, n=999, nk=999), rows=[]))
    bhg, cur, guna = [], [], asas_kosong
    for r in rows:
        sz = bait(r) + 1
        if cur and guna + sz > had:
            bhg.append(cur); cur, guna = [], 60
        cur.append(r); guna += sz
    bhg.append(cur)
    seg, cur, guna = [], [], 60
    for c, u in kamus.items():
        i = 0
        while i < len(u):
            j, sz = i, 0
            while j < len(u) and (j == i or guna + sz + bait(u[j]) + 1 < had):
                sz += bait(u[j]) + 1; j += 1
            if cur and guna + sz > had:
                seg.append(cur); cur, guna = [], 60
            cur.append([c, i, u[i:j]]); guna += sz + len(c) + 12; i = j
    if cur:
        seg.append(cur)
    out = [(nama, dict(meta, kolum=cols, jenis=jenis, bahagian=dict(id=ident, n=len(bhg), nk=len(seg)), rows=bhg[0]))]
    out += [(f'{nama}_{j}', dict(induk=ident, bahagian=j, rows=b)) for j, b in enumerate(bhg[1:], 2)]
    out += [(f'{nama}_kamus_{j}', dict(induk=ident, kamus=k)) for j, k in enumerate(seg, 1)]
    return out


SESI_GARIS = 60


def garis_harga(M, C, stor, terkini=None):
    """prestasi/garis + prestasi/mfe (pratonton dashboard v3).
    garis: tarikh (<= 60 sesi terakhir stor), tutup setiap saham yang masih ada posisi terbuka atau keluar dalam sesi
    terakhir (carta kecil, harga sesi sebelum)
    dan spy [[tarikh, buka, tutup]] sejak belian terawal (banding pasaran). mfe: [[kunci, kenaikan maks %], …] =
    (tinggi tertinggi sejak hari beli hingga kini, atau hingga sehari sebelum keluar lorong kaedah + harga keluar) ÷ harga beli − 1, minimum 0."""
    fr = bar_harga(stor, ('ticker', 'date', 'high', 'close'), terkini)
    G = {t: g.set_index('date') for t, g in fr.groupby('ticker')}
    hari = sorted(int(d) for d in fr.date.unique())[-SESI_GARIS:]
    mfe, terbuka, mula, mula_t = {}, set(), None, None
    for ak, R in (('M', M), ('C', C)):
        for r in R:
            hbv = SH.nombor(r.get('harga_beli'))
            if hbv is None or not hbv or SH.benar(r.get('tidak_dibeli')):
                continue
            b = int(r['tarikh_beli'].replace('-', '')); mula = b if mula is None else min(mula, b)
            ts = r.get('tutup_semua')
            akhir = max(r.get('tarikh_keluar') or '', r.get('tarikh_keluar_henti') or '').replace('-', '')
            # posisi terbuka, atau keluar dalam sesi terakhir (masih terbuka pada sesi sebelum: perbandingan "sejak semalam")
            if not SH.benar(ts if ts not in (None, '') else r.get('keluar')) or (akhir.isdigit() and len(hari) > 1 and int(akhir) > hari[-2]):
                terbuka.add(r['saham']); mula_t = b if mula_t is None else min(mula_t, b)
            g = G.get(r['saham'])
            if g is None:
                continue
            if SH.benar(r.get('keluar')) and r.get('tarikh_keluar'):
                e = int(r['tarikh_keluar'].replace('-', '')); w = g.high[(g.index >= b) & (g.index < e)].tolist()
                if SH.nombor(r.get('harga_keluar')) is not None:
                    w.append(float(r['harga_keluar']))
            else:
                w = g.high[g.index >= b].tolist()
            if w:
                k = f"{ak}|{r['saham']}|{r['kaedah']}|{r['tarikh_beli']}"
                mfe[k] = max(round(max(0.0, (max(w) / hbv - 1) * 100), 2), mfe.get(k, 0.0))
    hari = [d for d in hari if mula_t is None or d >= mula_t] or hari[-1:]
    rows = []
    for t in sorted(terbuka):
        g = G.get(t)
        if g is None:
            continue
        c = g.close.reindex(hari)
        if c.notna().any():
            rows.append(dict(s=t, c=[None if pd.isna(x) else round(float(x), 2) for x in c]))
    spy = []
    pi = os.path.join(stor, 'harga_idx.csv')
    if os.path.exists(pi) and mula:
        I = pd.read_csv(pi)
        I = I[(I.ticker == 'SPY') & (I.date >= mula)].sort_values('date')
        spy = [[int(d), round(float(o), 2), round(float(c), 2)] for d, o, c in zip(I.date, I.open, I.close)]
    return dict(tarikh=hari, spy=spy, rows=rows), [[k, v] for k, v in sorted(mfe.items())]


def maefe_l2(M, C, stor, terkini=None):
    """prestasi/maefe_l2 (24 Okt 2026): MAE dan MFE % sepanjang tempoh LORONG 2 (pegang selagi naik) = rendah terendah / tinggi
    tertinggi sejak hari beli hingga sehari sebelum keluar lorong 2 + harga keluar lorong 2 (atau hingga bar terakhir jika
    lorong 2 masih dipegang) ÷ harga beli − 1; MAE maksimum 0, MFE minimum 0. Pulang [[kunci, mae, mfe]] (kunci sama dengan
    prestasi/mae). prestasi/mae dan prestasi/mfe berhenti pada keluar lorong 1."""
    fr = bar_harga(stor, ('ticker', 'date', 'high', 'low'), terkini)
    G = {t: g.sort_values('date').set_index('date') for t, g in fr.groupby('ticker')}
    out = {}
    for ak, R in (('M', M), ('C', C)):
        for r in R:
            hbv = SH.nombor(r.get('harga_beli'))
            if not hbv or SH.benar(r.get('tidak_dibeli')) or not r.get('tarikh_beli'):
                continue
            g = G.get(r['saham'])
            if g is None:
                continue
            b = int(r['tarikh_beli'].replace('-', ''))
            if SH.benar(r.get('keluar_henti')) and r.get('tarikh_keluar_henti'):
                e = int(r['tarikh_keluar_henti'].replace('-', '')); w = g[(g.index >= b) & (g.index < e)]
                lo, hi = w.low.tolist(), w.high.tolist()
                hk = SH.nombor(r.get('harga_keluar_henti'))
                if hk is not None:
                    lo.append(hk); hi.append(hk)
            else:
                w = g[g.index >= b]; lo, hi = w.low.tolist(), w.high.tolist()
            if not lo:
                continue
            k = f"{ak}|{r['saham']}|{r['kaedah']}|{r['tarikh_beli']}"
            a = round(min(0.0, (min(lo) / hbv - 1) * 100), 2); f = round(max(0.0, (max(hi) / hbv - 1) * 100), 2)
            if k in out:
                a, f = min(a, out[k][0]), max(f, out[k][1])
            out[k] = (a, f)
    return [[k, a, f] for k, (a, f) in sorted(out.items())]


# ---------------------------------------------------------------- langkauan belian 9:35 NY (papertrade/langkau)
_R_KEPALA_RUTIN = re.compile(r'^## (\d{4}-\d{2}-\d{2}) \([^)]*NY\) — Beli maya')
_R_KEPALA_ACT = re.compile(r'— GitHub Actions: beli maya (\d{4}-\d{2}-\d{2})')
_R_SAHAM_KAEDAH = re.compile(r'([A-Z][A-Z0-9.\-]*) (M\d+)')


def hurai_langkau_rutin(teks):
    """'buka > buka_maks — FRPT M08, ROL M08; buka ≤ henti — COR M14, GGG M35, M117 & M149' (log rutin 9:35 NY) ->
    ([(saham, kaedah, sebab)], [token tidak dihurai]). Kaedah tanpa saham = saham token sebelumnya."""
    teks = teks.split('. ')[0].rstrip('.').strip()
    out, tak = [], []
    for kat in teks.split('; '):
        if ' — ' not in kat:
            tak.append(kat); continue
        sebab, senarai = kat.split(' — ', 1)
        t = None
        for tok in re.split(r', | & ', senarai):
            tok = tok.strip()
            m = _R_SAHAM_KAEDAH.fullmatch(tok)
            if m:
                t, mid = m.groups()
            elif re.fullmatch(r'M\d+', tok) and t:
                mid = tok
            else:
                tak.append(tok); continue
            out.append((t, mid, sebab.strip()))
    return out, tak


def hurai_langkau_actions(teks):
    """'FRPT M08: buka 67.01 > buka_maks 66.15; SSNC M23: …' (status_harian.json beli.langkau / LOG Actions) -> [(saham, kaedah, sebab)]."""
    out = []
    for x in (teks if isinstance(teks, list) else teks.rstrip('.').split('; ')):
        m = re.fullmatch(r'([A-Z][A-Z0-9.\-]*) (M\d+): (.+)', x.strip())
        if m:
            out.append(m.groups())
    return out


def langkau_beli(folder, st, log=None, mula=LANGKAU_MULA):
    """papertrade/langkau (24 Okt 2026): isyarat senarai beli yang DILANGKAU semasa belian 9:35 NY (buka > buka_maks, buka <=
    henti, belum didagangkan, isyarat batal) — tidak pernah direkod sebagai baris CSV. Sumber: log belian (rutin Claude
    `binaan_v2_log_tambahan.md` "Dilangkau N: …"; folder bayang: `bayang/LOG.md` "Dilangkau: X M: sebab; …") sejak `mula`, dan
    status_harian.json beli.langkau (senarai penuh; menggantikan log bagi tarikh itu). Pulang dict(rows, liputan)."""
    if log is None:
        d = os.path.dirname(os.path.abspath(folder))
        log = os.path.join(d, 'LOG.md') if os.path.basename(d) == 'bayang' else LOG_RUTIN
    rows, liputan, tarikh = [], {}, None
    teks = open(log, encoding='utf-8').read().splitlines() if os.path.exists(log) else []
    for baris in teks:
        if baris.startswith('## '):
            m = _R_KEPALA_RUTIN.match(baris) or _R_KEPALA_ACT.search(baris)
            tarikh = m.group(1) if m else None
            continue
        if not tarikh or tarikh < mula or not baris.startswith('- Dilangkau'):
            continue
        m = re.match(r'- Dilangkau (\d+): (.*)', baris)
        if m:
            x, tak = hurai_langkau_rutin(m.group(2)); n = int(m.group(1))
        else:
            m = re.match(r'- Dilangkau: (.*)', baris)
            if not m:
                continue
            x, tak, n = hurai_langkau_actions(m.group(1)), [], None
        rows += [dict(tarikh=tarikh, saham=t, kaedah=k, sebab=s, sumber=os.path.basename(log)) for t, k, s in x]
        liputan[tarikh] = dict(bil_log=n, bil=len(x), **({'tidak_dihurai': tak} if tak else {}))
    b = (st or {}).get('beli') or {}
    if b.get('tarikh') and b['tarikh'] >= mula and b.get('langkau') is not None:
        rows = [r for r in rows if r['tarikh'] != b['tarikh']]
        x = hurai_langkau_actions(b['langkau'])
        rows += [dict(tarikh=b['tarikh'], saham=t, kaedah=k, sebab=s, sumber='status_harian.json') for t, k, s in x]
        liputan[b['tarikh']] = dict(bil_log=b.get('dilangkau'), bil=len(x))
    rows.sort(key=lambda r: (r['tarikh'], r['kaedah'], r['saham']))
    return dict(rows=rows, liputan=dict(sorted(liputan.items())), mula=mula,
                sumber=[os.path.relpath(log, BS2)] + (['status_harian.json'] if b.get('langkau') is not None else []))


TERKINI = os.path.join(BS2, 'data', 'harga', 'terkini.csv')


def harian_kaedah(M, C, stor, terkini=None):
    """prestasi/harian_kaedah (grid prestasi harian setiap kaedah, tab Prestasi): untung harian % setiap kaedah setiap sesi =
    Σ perubahan nilai ÷ Σ nilai awal hari bagi posisi USD_POSISI yang dipegang hari itu (hari beli: tutup lawan harga beli; hari
    keluar lorong kaedah: harga keluar lawan tutup semalam; tiada bar = harga semalam). j = untung purata % (untung akhir bagi
    yang keluar, semasa bagi yang dipegang; sama dengan Prestasi). ev = [[indeks hari, beli, keluar untung, keluar rugi]].
    Akaun M, C dan G (gabung); k 'Semua' = semua kaedah akaun itu. spy = untung harian % SPY. Harga: stor + terkini.csv
    (bar harian terbaharu; stor repo boleh ketinggalan satu sesi)."""
    fail = [os.path.join(stor, f) for f in ('harga_A.csv', 'harga_B.csv', 'harga_idx.csv')] + ([terkini] if terkini else [])
    fr = pd.concat([pd.read_csv(f, usecols=['ticker', 'date', 'close']) for f in fail if os.path.exists(f)])
    fr['date'] = fr.date.astype(int)
    fr = fr.drop_duplicates(['ticker', 'date'], keep='last')
    P = {t: dict(zip(g.date, g.close.astype(float))) for t, g in fr.groupby('ticker')}
    pos = []
    for ak, R in (('M', M), ('C', C)):
        for r in R:
            hb = SH.nombor(r.get('harga_beli'))
            if not sah(r) or not hb or not r.get('tarikh_beli'):
                continue
            kel = SH.benar(r.get('keluar'))
            hk = SH.nombor(r.get('harga_keluar')) if kel else None
            e = int(r['tarikh_keluar'].replace('-', '')) if kel and hk is not None and r.get('tarikh_keluar') else None
            u = SH.nombor(r.get('untung_akhir_pct') if kel else r.get('untung_pct'))
            pos.append((ak, r['kaedah'], r['saham'], int(r['tarikh_beli'].replace('-', '')), e, hb, hk, u or 0.0))
    if not pos:
        return dict(tarikh=[], spy=[], rows=[])
    mula = min(p[3] for p in pos)
    bil = fr[fr.ticker != 'SPY'].date.value_counts()
    hari = sorted(d for d, n in bil.items() if d >= mula and n >= 0.5 * bil.max())   # sesi separa (stor belum lengkap) diabaikan
    ix = {d: i for i, d in enumerate(hari)}
    sp = sorted(P.get('SPY', {}).items())
    spy = []
    for d in hari:
        lalu = [c for t, c in sp if t < d]
        spy.append(round(100 * (P['SPY'][d] / lalu[-1] - 1), 2) if lalu and d in P.get('SPY', {}) else None)
    agg = {}
    for ak, k, s, b, e, hb, hk, u in pos:
        harga = P.get(s, {})
        kunci = ((ak, k), ('G', k), (ak, 'Semua'), ('G', 'Semua'))
        for kk in kunci:
            x = agg.setdefault(kk, dict(pnl=[0.0] * len(hari), asas=[0.0] * len(hari), n=[0] * len(hari), u=[], ev={}))
            x['u'].append(u)
            if b in ix:
                x['ev'].setdefault(ix[b], [0, 0, 0])[0] += 1
            if e in ix:
                x['ev'].setdefault(ix[e], [0, 0, 0])[1 if hk > hb else 2] += 1
        lalu = hb
        for d in hari:
            if d < b:
                continue
            if e is not None and d > e:
                break
            kini = hk if e is not None and d == e else harga.get(d, lalu)
            i = ix[d]
            for kk in kunci:
                x = agg[kk]
                x['pnl'][i] += USD_POSISI * (kini - lalu) / hb; x['asas'][i] += USD_POSISI * lalu / hb; x['n'][i] += 1
            lalu = kini
    no = lambda k: (-1 if k == 'Semua' else int(k[1:]) if k[1:].isdigit() else 9999, k)
    rows = []
    for (ak, k), x in sorted(agg.items(), key=lambda kv: ('MCG'.index(kv[0][0]), no(kv[0][1]))):
        rows.append(dict(a=ak, k=k, np=len(x['u']), j=round(stt.mean(x['u']), 2),
                         d=[round(100 * p / a, 2) if a > 0 else None for p, a in zip(x['pnl'], x['asas'])], n=x['n'],
                         ev=[[i] + v for i, v in sorted(x['ev'].items())]))
    return dict(tarikh=hari, spy=spy, rows=rows)


def pengawas(st, masa):
    """Larian Actions yang sepatutnya sudah siap tetapi belum (untuk sesi tolak db: tembak workflow sekali).
    harian.yml: sesi NYSE terakhir yang tutup >= 9 jam lalu (data Yahoo muktamad); beli.yml: hari ini NY selepas 9:45."""
    try:
        import exchange_calendars as xc
    except ImportError:
        return {}
    c = xc.get_calendar('XNYS'); ny = masa.tz_convert('America/New_York'); hari = ny.normalize().tz_localize(None)
    sesi = [s for s in c.sessions_in_range(hari - pd.Timedelta(days=10), hari)
            if pd.Timestamp(f'{s.date()} 16:00', tz='America/New_York') + pd.Timedelta(hours=9) <= ny]
    jangka = str(sesi[-1].date()) if sesi else ''
    out = dict(malam_sesi=st.get('malam', {}).get('sesi', ''), malam_jangka=jangka,
               beli_tarikh=st.get('beli', {}).get('tarikh', ''), tembak=[])
    if jangka and out['malam_sesi'] < jangka:
        out['tembak'].append('harian.yml')
    if c.is_session(hari) and ny.hour * 60 + ny.minute >= 9 * 60 + 45 and out['beli_tarikh'] != str(hari.date()):
        out['beli_jangka'] = str(hari.date()); out['tembak'].append('beli.yml')
    return out


def portfolio_slot(dibina, folder=os.path.join(BS2, 'portfolio_slot')):
    """prestasi/portfolio_slot: portfolio maya 10 slot (standard/portfolio_slot.py, daripada Lejar Penuh) untuk kad Eksperimen
    dalam tab Ringkasan dan panel Skor kaedah swing (gabungan beku). Portfolio tanpa fail dilangkau; None jika RS_10 belum dijana.
    Setiap portfolio: mula, sesi dan spy_pct tempoh sama (portfolio beku bermula pada mula_jejak)."""
    import portfolio_slot as PS
    out = {}
    for k, nama in PS.PORTFOLIO.items():
        pe, pp = os.path.join(folder, f'{k}_ekuiti.csv'), os.path.join(folder, f'{k}_posisi.csv')
        if not (os.path.exists(pe) and os.path.exists(pp)):
            continue
        E, R = pd.read_csv(pe), pd.read_csv(pp)
        if E.empty and k not in PS.BEKU_JENIS:
            continue
        kel = R[R.status == 'Keluar']
        out[k] = dict(nama=f'{k}: {nama}', pulangan_pct=round(100 * (E.ekuiti.iloc[-1] - 1), 2) if len(E) else None,
                      mdd_pct=round(100 * PS.mdd(E.ekuiti), 2) if len(E) else None,
                      dipegang=int((R.status == 'Pegang').sum()), keluar=int(len(kel)),
                      menang_pct=round(100 * float((kel.untung_pct > 0).mean()), 1) if len(kel) else None,
                      mula=E.tarikh.iloc[0] if len(E) else None, sesi=int(len(E)),
                      spy_pct=round(100 * (float(E.spy.iloc[-1]) - 1), 2) if len(E) and pd.notna(E.spy.iloc[-1]) else None,
                      ekuiti=[[t, round(float(e), 5)] for t, e in zip(E.tarikh, E.ekuiti)],
                      posisi=json.loads(R.round(4).to_json(orient='records')))
    rs = out.get('RS_10')
    if not rs or not rs['sesi']:
        return None
    beku = None
    try:
        beku = json.load(open(os.path.join(BS2, 'data', 'analisis', 'gabungan_beku.json'), encoding='utf-8'))
    except (OSError, ValueError):
        pass
    return dict(dibina=dibina, mula=rs['mula'], sesi_terakhir=rs['ekuiti'][-1][0], sesi=rs['sesi'], spy_pct=rs['spy_pct'], portfolio=out,
                beku=beku,
                nota='Rekod sahaja (kajian/KAJIAN_PORTFOLIO.md). 10 slot x 10% ekuiti, satu posisi setiap saham. RS_10 = RS pasaran '
                     'tertinggi, RAWAK_10 = kawalan rawak (lorong 2). GABUNGAN_10 / TOP1_10 / RAWAK_KAEDAH_10 = gabungan kaedah beku '
                     '(data/analisis/gabungan_beku.json) lawan #1 sahaja lawan kaedah rawak, sejak mula_jejak. Dibina semula setiap malam oleh lejar.yml.')


def sesi_stor(path=STATUS_HARGA):
    """Sesi terkini stor harga repo (status.json terkini.sesi, YYYYMMDD) sebagai YYYY-MM-DD; '' jika tiada.
    Sandaran tarikh data apabila status_harian.json tiada dalam folder (mod bayang: Actions menulis ke bayang/ sahaja)."""
    try:
        s = str(json.load(open(path, encoding='utf-8')).get('terkini', {}).get('sesi', ''))
    except (OSError, ValueError, AttributeError):
        return ''
    return f'{s[:4]}-{s[4:6]}-{s[6:8]}' if len(s) == 8 and s.isdigit() else ''


# ---------------------------------------------------------------- label jujur dan saluran (24 Okt 2026)
def baca_mod(path=MOD_ACTIONS):
    """Isi BacktestShariah2/MOD_ACTIONS ('bayang' | 'rasmi'), '' jika tiada."""
    try:
        return open(path, encoding='utf-8').read().strip()
    except OSError:
        return ''


def penulis_data(folder, st, mod):
    """Penulis fail posisi dalam `folder` (label jujur; audit 24 Okt 2026): GitHub Actions jika status_harian.json ada
    (harian_c.py), rutin Claude 6:02 jika folder rasmi dalam mod bayang, selainnya tidak diketahui."""
    if st:
        return 'GitHub Actions (standard/harian_c.py)'
    if mod == 'bayang' and os.path.abspath(folder) == os.path.abspath(PT):
        return 'rutin Claude 6:02 MYT (jadual/kemas_kini_0602.md)'
    return 'penulis tidak diketahui'


def sumber_harga(sumber, penulis, stor, path=STATUS_HARGA):
    """harian/status.sumber_harga: --sumber jika diberi; selainnya hanya fakta yang jana_db boleh tahu (tiada andaian)."""
    if sumber:
        return sumber
    try:
        tk = json.load(open(path, encoding='utf-8')).get('terkini', {})
    except (OSError, ValueError, AttributeError):
        tk = {}
    yf = (f"data/harga/terkini.csv yfinance sesi {tk.get('sesi')} (dijana {tk.get('dijana')}; "
          f"{tk.get('bil_tiada_bar_sesi', len(tk.get('tiada_bar_sesi') or []))} saham tanpa bar sesi itu)") if tk else 'terkini.csv tiada'
    ss = 'stor repo + terkini.csv' if os.path.abspath(stor) == os.path.abspath(STOR) else f'stor kerja {stor}'
    return f'{penulis}; jana_db: {ss}; {yf}; sumber bar posisi tidak dinyatakan (--sumber kosong)'


def hingga_bar(stor, terkini=None):
    """Sesi bar terakhir data harga yang dipakai (YYYY-MM-DD): tarikh terakhir yang ada bar bagi >= 50% bilangan maksimum
    saham (sesi separa diabaikan); '' jika tiada."""
    fr = bar_harga(stor, ('ticker', 'date'), terkini)
    if not len(fr):
        return ''
    n = fr.date.value_counts()
    d = str(max(x for x, k in n.items() if k >= 0.5 * n.max()))
    return f'{d[:4]}-{d[4:6]}-{d[6:]}'


def tarikh_sst(path):
    """Tarikh snapshot SST terakhir dalam papertrade/sektor.csv ('' jika tiada; SST tidak tersedia sejak 20 Okt 2026)."""
    try:
        return max((r.get('tarikh') or '' for r in csv.DictReader(open(path, newline='', encoding='utf-8'))), default='')
    except OSError:
        return ''


def sesi_lejar(path=LEJAR_STATUS):
    try:
        return json.load(open(path, encoding='utf-8')).get('sesi_terakhir', '')
    except (OSError, ValueError, AttributeError):
        return ''


def saring_saiz(semua, ralat, had=None):
    """[(koleksi, [(doc_id, dokumen)])] -> [(koleksi, doc_id, dokumen, bait)] yang boleh ditulis. Dokumen >= had db DILANGKAU
    dan dicatat dalam `ralat` (24 Okt 2026; dahulu SystemExit menghentikan SEMUA tolakan, cth. prestasi/mae dijangka melepasi
    had ~30 Okt); >= AMARAN_HAD x had -> amaran dalam `ralat`."""
    had = had or HAD_DB
    out = []
    for kol, bahagian in semua:
        for doc_id, dd in bahagian:
            sz = bait(dd)
            if sz >= had:
                ralat.append(f'{kol}/{doc_id}: {sz} bait melebihi had db {had}; dokumen dilangkau (versi lama kekal dalam db)')
                print(f'RALAT: {ralat[-1]}', file=sys.stderr)
                continue
            if sz >= AMARAN_HAD * had:
                ralat.append(f'amaran: {kol}/{doc_id} {sz} bait = {sz / had:.0%} had db (bahagikan sebelum melebihi)')
            out.append((kol, doc_id, dd, sz))
    return out


# ---------------------------------------------------------------- utama
BAHAGI = ('senarai_beli', 'watchlist', 'garis', 'mfe', 'mae', 'mae_atr', 'maefe_l2', 'harian_kaedah', 'trend', 'lorong2', 'langkau')


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument('--keluar', required=True); ap.add_argument('--folder', default=PT); ap.add_argument('--stor', default=STOR)
    ap.add_argument('--versi', help='JSON {"koleksi/doc": versi} bagi if_version'); ap.add_argument('--masa')
    ap.add_argument('--sumber', help='sumber harga sebenar larian ini (label jujur harga_pada / harian/status.sumber_harga), '
                                     'cth. "rutin Claude 6:02: yfinance 22:04 UTC + skrin Moomoo 31 saham"')
    a = ap.parse_args(argv)
    masa = (pd.Timestamp(a.masa).tz_localize('Asia/Kuala_Lumpur') if a.masa else pd.Timestamp.now(tz='Asia/Kuala_Lumpur'))
    dibina = masa.strftime('%Y-%m-%d %H:%M') + ' MYT'
    st = json.load(open(os.path.join(a.folder, 'status_harian.json'), encoding='utf-8')) if os.path.exists(os.path.join(a.folder, 'status_harian.json')) else {}
    malam = st.get('malam', {}); beli = st.get('beli', {}); S = malam.get('sesi', '') or sesi_stor()
    mod = baca_mod(); penulis = penulis_data(a.folder, st, mod)
    sumber = sumber_harga(a.sumber, penulis, a.stor)
    # label jujur (audit 24 Okt 2026): dahulu "bar harian yfinance muktamad; GitHub Actions" tanpa mengira penulis sebenar
    harga_pada = f"{S} tutup ({a.sumber or penulis + '; sumber bar tidak dinyatakan'})" if S else ''
    nota_pos = (f"Dikemas kini oleh {penulis} {malam.get('masa', '')}: harga tutup {S}; keluar dinilai dengan "
                'enjin rasmi; harga beli sementara dibetulkan kepada buka rasmi bar harian; baris keluar dibekukan; "menunggu" = '
                'isyarat keluar pada tutup terakhir, harga keluar = buka sesi seterusnya.')
    ralat = list((malam.get('ralat_kaedah') or [])[:20])
    tk = TERKINI if a.stor == STOR else None   # stor repo boleh ketinggalan satu sesi: tambah bar terkini.csv
    hingga = hingga_bar(a.stor, tk)
    hingga_teks = f'{hingga} tutup' if hingga else f'{S} tutup'
    docs = {}
    M = baca_csv(os.path.join(a.folder, 'moomoo.csv'))
    docs['papertrade/moomoo'] = dict(akaun='4135388', dibina=dibina, harga_pada=harga_pada, nota=nota_pos, rows=[baris_db(r) for r in M])
    # dokumen lama (halaman v90+ membaca papertrade/ringkas_m; ini sandaran sahaja): gugurkan medan teks panjang jika melebihi
    # had satu dokumen (23 Okt 2026: medan audit yang diisi menjadikannya 270 KB)
    gugur = []
    for k in ('gred_pada', 'pemangkin_url', 'kewangan_ringkas', 'rs_tanda', 'pemangkin', 'sumber_earnings', 'nota'):
        if bait(docs['papertrade/moomoo']) < HAD_DB - 2000:
            break
        for x in docs['papertrade/moomoo']['rows']:
            x.pop(k, None)
        gugur.append(k)
    if gugur:
        docs['papertrade/moomoo']['medan_digugurkan'] = gugur
    C = []
    fail_c = sorted(glob.glob(os.path.join(a.folder, 'claude*.csv')), key=nombor_fail)
    for p in fail_c:
        R = baca_csv(p); C += R
        n = nombor_fail(p)
        docs[f"papertrade/{'claude' if n == 1 else f'claude_{n}'}"] = dict(dibina=dibina, harga_pada=harga_pada, nota=nota_pos,
                                                                         rows=[baris_db(r) for r in R])
    # slot (panel Papertrade C) dan isyarat dibatalkan pada belian terakhir
    import importlib
    slot = {}
    for r in C:
        if not sah(r):
            continue
        x = slot.setdefault(r['kaedah'], dict(claude_jumlah=0, claude_terbuka=0, moomoo=0, moomoo_termasuk_warisan=0))
        x['claude_jumlah'] += 1
        x['claude_terbuka'] += not SH.benar(r.get('tutup_semua') if r.get('tutup_semua') else r.get('keluar'))
    for r in M:
        x = slot.setdefault(r['kaedah'], dict(claude_jumlah=0, claude_terbuka=0, moomoo=0, moomoo_termasuk_warisan=0))
        x['moomoo_termasuk_warisan'] += 1
        x['moomoo'] += r.get('sumber') == 'harian' and not SH.benar(r.get('keluar'))
    for k, x in slot.items():
        try:
            x['nama'] = importlib.import_module(f'kaedah.{k}').NAMA
        except Exception:
            x['nama'] = ''
    batal = [l.split(': ', 1)[0].split(' ')[::-1] + [l.split(': ', 1)[1]] for l in beli.get('langkau', []) if ': ' in l]
    if 'papertrade/claude' in docs:
        docs['papertrade/claude'].update(slot=dict(sorted(slot.items(), key=lambda kv: int(kv[0][1:]) if kv[0][1:].isdigit() else 9999)),
                                         batal=batal, nota_slot='claude_terbuka = posisi Papertrade C yang belum tutup kedua-dua lorong; '
                                         'moomoo = posisi Moomoo warisan (sumber harian) yang belum keluar.')
    # senarai beli: tidak ditolak ke db sejak 19 Okt 2026 (halaman tidak membacanya); kiraan untuk harian/status sahaja
    sb = baca_csv(os.path.join(a.folder, 'senarai_beli.csv'))
    lihat = {r['saham'] for r in sb}
    # watchlist (dibahagi bawah had saiz). 24 Okt 2026: % hampir dihadkan 99.9 kecuali isyarat lengkap, `disentuh` (jarak 0
    # tetapi isyarat belum lengkap; harian_c.normal_watch), tarikh_data setiap baris, earn_kini/earn_lalu
    import kalendar_earnings as KE
    from harian_c import normal_watch
    KAL = KE.muat()   # tarikh earnings sebenar (earn_sebenar, earn_kini) bagi ringkas_c/m dan watchlist
    cache_e = {}
    wl = baca_csv(os.path.join(a.folder, 'watchlist.csv'))
    wl_db = []
    for r in wl:
        x = dict(r); normal_watch(x)
        wl_db.append(earn_kini(earn_sebenar(baris_db(x, PETA_WATCH), r, KAL), r.get('Saham'), S, KAL, cache_e))
    docs['papertrade/watchlist'] = dict(
        definisi='Hampir Signal: semua syarat entry selain pencetus dipenuhi; pencetus dalam <=2% (pct_dipenuhi = 100 - jarak_pct, '
                 'maks 99.9; 100 = isyarat lengkap sahaja, syarat_belum "Tiada (isyarat sah)"; disentuh = jarak 0 tetapi isyarat '
                 'belum lengkap). Maks 5 setiap kaedah. Terkeluar signal dibuang serta-merta (tugasan_v3 §3). tarikh_data setiap '
                 'baris = sesi data harga baris itu; gred_pada baris = tarikh data gred (snapshot kumpulan/RS).',
        dibina=malam.get('masa', dibina), gred_pada=st.get('gred', {}).get('tarikh', ''), pemangkin_pada=st.get('gred', {}).get('tarikh', ''),
        tarikh_data=wl[0]['tarikh_data'] if wl else S, rows=wl_db)
    # prestasi
    mae = penurunan_maks(M, C, a.stor, tk)
    docs['prestasi/mae'] = dict(rows=[[k, v] for k, v in sorted(mae.items())], dibina=dibina, harga_hingga=hingga_teks,
                                definisi='Penurunan maksimum % = (harga rendah terendah sejak hari beli hingga hari ini, atau sehingga keluar) ÷ harga beli − 1, maksimum 0. Bagi posisi keluar: rendah hari sebelum hari keluar dan harga keluar. Kunci: akaun|saham|kaedah|tarikh_beli (akaun M=Moomoo, C=Claude). rows: [[kunci, %]] (dibahagi sejak 24 Okt 2026). ATR isyarat: prestasi/mae_atr; tempoh lorong 2: prestasi/maefe_l2.')
    # 23 Okt 2026: atr dipindah ke dokumen sendiri (dibahagi) kerana mae + atr melebihi had satu dokumen
    docs['prestasi/mae_atr'] = dict(rows=sorted([k, v] for k, v in atr_isyarat(M, C, a.stor).items()), dibina=dibina,
                                    harga_hingga=hingga_teks, definisi='ATR14 % pada hari isyarat (bar terakhir sebelum hari beli). '
                                    'rows: [akaun|saham|kaedah|tarikh_beli, %].')
    docs['prestasi/maefe_l2'] = dict(rows=maefe_l2(M, C, a.stor, tk), dibina=dibina, harga_hingga=hingga_teks,
                                     definisi='MAE/MFE % tempoh LORONG 2 (pegang selagi naik): rendah terendah / tinggi tertinggi sejak hari '
                                              'beli hingga sehari sebelum keluar lorong 2 dan harga keluar lorong 2 (atau hingga bar terakhir jika '
                                              'masih dipegang) ÷ harga beli − 1; MAE maks 0, MFE min 0. rows: [[akaun|saham|kaedah|tarikh_beli, '
                                              'mae, mfe]]. prestasi/mae dan prestasi/mfe berhenti pada keluar lorong 1.')
    docs['prestasi/ringkasan'] = dict(prestasi(M, C, mae), dibina=dibina, harga_pada=f'{S} tutup',
                                      nota='Dikira oleh standard/jana_db.py (GitHub Actions + sesi tolak db) dengan peraturan skor & keputusan P4 (sama seperti halaman).')
    # papertrade/langkau: langkauan belian 9:35 NY (tidak pernah direkod sebagai baris CSV)
    lk = langkau_beli(a.folder, st)
    docs['papertrade/langkau'] = dict(lk, dibina=dibina,
                                      definisi='Isyarat senarai beli yang DILANGKAU semasa belian 9:35 NY (buka > buka_maks, buka <= henti, '
                                               'belum didagangkan, isyarat batal pada buka). rows: {tarikh beli, saham, kaedah, sebab, sumber}. '
                                               'liputan: setiap tarikh, bil_log = bilangan dinyatakan dalam log, bil = baris dihurai. Belum '
                                               'diliputi: sebelum 14 Okt 2026 (mod Moomoo); log Actions dipotong 30 entri (status_harian.json '
                                               'lengkap bagi belian terakhir). Sejak 22 Okt 2026 saham belum didagangkan direkod dengan buka '
                                               'sementara (tidak dilangkau). Baris CSV tidak_dibeli (sedia() sig=False, mingguan) ialah rekod lain.')
    # papertrade/ringkas_c, ringkas_m: semua baris dalam bentuk padat (halaman v90 membaca ini sahaja, bukan claude*);
    # medan db sahaja (24 Okt 2026): kualiti, sasaran_dinamik, jenis_tidak_sah, earn_kini/earn_kini_h/earn_lalu
    kual = kualiti(M, C, S, a.stor, tk)
    pra = {}
    dc = docs.get('papertrade/claude', {})
    for kod, R, meta in (('c', [baris_posisi(r, 'C', KAL, S, kual, cache_e) for r in C], {k: dc[k] for k in ('dibina', 'harga_pada', 'nota', 'slot', 'batal') if k in dc}),
                         ('m', [baris_posisi(r, 'M', KAL, S, kual, cache_e) for r in M], {k: v for k, v in docs['papertrade/moomoo'].items() if k not in ('rows', 'medan_digugurkan')})):
        for doc_id, d in ringkas_pt(R, f'ringkas_{kod}', meta):
            pra[f'papertrade/{doc_id}'] = d
    garis, mfe = garis_harga(M, C, a.stor, tk)
    docs['prestasi/garis'] = dict(garis, dibina=dibina, harga_hingga=hingga_teks,
                                  definisi='rows: {s: saham, c: tutup sejajar dengan tarikh (null = tiada bar)} bagi saham yang masih ada '
                                           'posisi terbuka; spy: [tarikh, buka, tutup] sejak belian terawal.')
    docs['prestasi/mfe'] = dict(rows=mfe, dibina=dibina, harga_hingga=hingga_teks,
                                definisi='Kenaikan maksimum % (MFE) = (harga tinggi tertinggi sejak hari beli hingga hari ini, atau sehingga '
                                         'sehari sebelum keluar lorong kaedah, dan harga keluar) ÷ harga beli − 1, minimum 0. '
                                         'rows: [akaun|saham|kaedah|tarikh_beli, %].')
    docs['prestasi/harian_kaedah'] = dict(harian_kaedah(M, C, a.stor, tk), dibina=dibina, harga_hingga=f'{S} tutup',
                                          definisi='rows: {a: akaun M|C|G, k: kaedah, np: jumlah posisi, j: untung purata %, d: untung '
                                                   'harian % sejajar tarikh (null = tiada posisi), n: posisi dipegang, ev: [[indeks hari, beli, keluar untung, '
                                                   'keluar rugi]]}; k Semua = semua kaedah; spy: untung harian % SPY. Untung harian = '
                                                   'Σ perubahan nilai ÷ Σ nilai awal hari (posisi USD sama; keluar ikut lorong kaedah).')
    # harian/trend (pill Trend D10+H2, ATR14% + kuintil, rejim SPY) dan posisi/lorong2 (candlestick + paras lorong 2 setiap
    # saham|tarikh_beli); kegagalan di sini tidak menghalang dokumen lain tetapi dicatat dalam harian/status.ralat
    try:
        import trend_status as TS, lorong2_siri as L2
        H, nota_h = TS.muat_harga(a.stor, tk)
        I, _ = TS.muat_harga(a.stor, tk, fail=('harga_idx.csv',))
        lama = json.load(open(TS.FAIL, encoding='utf-8')) if a.stor == STOR and os.path.exists(TS.FAIL) else None
        docs['harian/trend'] = dict(TS.bawa_semalam(TS.dokumen(H, TS.alam(a.folder, H), nota_h, I), lama), dibina=dibina)
        docs['posisi/lorong2'] = dict(L2.dokumen(H, a.folder), dibina=dibina, harga_hingga=hingga_teks)
    except Exception as e:  # noqa: BLE001
        print(f'amaran: harian/trend / posisi/lorong2 gagal: {e!r}', file=sys.stderr)
        ralat.append(f'harian/trend / posisi/lorong2 tidak dijana: {e!r}'[:300])
    ps = portfolio_slot(dibina)
    if ps:
        docs['prestasi/portfolio_slot'] = ps
    # analisis/papan: Papan Penganalisis (standard/penganalisis.py, Actions analisis.yml selepas Lejar Penuh) untuk tab Analisis
    pa = os.path.join(BS2, 'data', 'analisis', 'papan.json')
    if os.path.exists(pa):
        docs['analisis/papan'] = json.load(open(pa, encoding='utf-8'))
    # sektor/snapshot (dijana mingguan; medan posisi dikemas kini jika fail ada)
    snap = os.path.join(BS2, 'data', 'db', 'sektor_snapshot.json')
    if os.path.exists(snap):
        docs['sektor/snapshot'] = json.load(open(snap, encoding='utf-8'))
    # saiz: dokumen >= had db dilangkau dan dicatat (24 Okt 2026; dahulu SystemExit menghentikan SEMUA tolakan); >= 80% = amaran
    os.makedirs(a.keluar, exist_ok=True)
    versi = json.load(open(a.versi)) if a.versi else {}
    semua = []
    for nama, d in docs.items():
        kol, doc = nama.split('/')
        if doc in BAHAGI:
            try:
                semua.append((kol, bahagi(d, doc, HAD_BAHAGI)))
            except SystemExit as e:
                ralat.append(f'{nama}: tidak dapat dibahagi ({e}); dokumen dilangkau (versi lama kekal dalam db)')
        else:
            semua.append((kol, [(doc, d)]))
    semua += [(nama.split('/')[0], [(nama.split('/')[1], d)]) for nama, d in pra.items()]   # sudah dibahagi (ringkas_pt)
    sedia = saring_saiz(semua, ralat)
    # harian/status: kesegaran data (halaman: kemaskini_pagi, harga_tutup_pada, tarikh_data_pagi; header "Kemas kini terakhir")
    # + lampu sistem (24 Okt 2026): ralat, mod, sumber_harga, saluran, beli_langkau
    rk = malam
    dt = lambda n: (docs.get(n) or {})
    rc = pra.get('papertrade/ringkas_c', {})
    tl = sorted(lk['liputan'])
    if beli.get('tarikh'):
        beli_langkau = int(beli.get('dilangkau') or 0)
    else:
        beli_langkau = sum(1 for r in lk['rows'] if tl and r['tarikh'] == tl[-1])
    saluran = dict(ringkas_c=rc.get('dibina', ''), trend=dt('harian/trend').get('tarikh', ''), lorong2=dt('posisi/lorong2').get('harga_hingga', ''),
                   garis=dt('prestasi/garis').get('harga_hingga', ''), mfe=dt('prestasi/mfe').get('harga_hingga', ''),
                   sektor=dt('sektor/snapshot').get('dibina', ''),
                   sst=tarikh_sst(os.path.join(a.folder, 'sektor.csv') if os.path.exists(os.path.join(a.folder, 'sektor.csv')) else os.path.join(PT, 'sektor.csv')),
                   lejar=sesi_lejar(), analisis=dt('analisis/papan').get('harga_pada', ''),
                   slot=dt('prestasi/portfolio_slot').get('sesi_terakhir', ''), watchlist=dt('papertrade/watchlist').get('tarikh_data', ''),
                   langkau=tl[-1] if tl else '')
    status = dict(
        dikemaskini=dibina, sumber=f'{penulis} + standard/jana_db.py', harga_tutup_pada=S, tarikh_data_pagi=S,
        kemaskini_pagi=rk.get('masa', ''), tarikh_data=S, scan_malam=rk.get('masa', ''),
        kemaskini_pagi_ringkas=dict(C_keluar_baru=(rk.get('keluar_baru_jumlah') or {}).get('C', 0),
                                    M_keluar_baru=(rk.get('keluar_baru_jumlah') or {}).get('M', 0), menunggu_buka=rk.get('menunggu', 0),
                                    tidak_dibeli_baru=len(rk.get('tidak_dibeli') or []), watchlist_dibuang=rk.get('watchlist_dibuang', 0)),
        senarai_beli=dict(claude=len(sb), jumlah=len(sb), moomoo=0, saham_unik=len(lihat), watchlist=len(wl)),
        beli_dirancang=len(sb), beli_pada=beli.get('masa', ''), beli_ringkas=dict(direkod=beli.get('direkod', 0), dilangkau=beli.get('dilangkau', 0)),
        gred_pada=st.get('gred', {}).get('masa', ''), ralat=ralat, mod=mod, sumber_harga=sumber, saluran=saluran, beli_langkau=beli_langkau)
    docs['harian/status'] = status
    sedia.append(('harian', 'status', status, bait(status)))
    # tulis + batch
    tulis = []
    for kol, doc_id, dd, sz in sedia:
        p = os.path.join(a.keluar, kol, doc_id + '.json'); os.makedirs(os.path.dirname(p), exist_ok=True)
        open(p, 'w', encoding='utf-8').write(padat(dd))
        w = dict(op='set', collection=kol, doc_id=doc_id, file_path=os.path.abspath(p))
        v = versi.get(f'{kol}/{doc_id}')
        if v:
            w['if_version'] = int(v)
        tulis.append((w, sz))
    batches, cur, size = [], [], 0
    for w, sz in tulis:
        if cur and (size + sz > HAD_BATCH or len(cur) >= 50):
            batches.append(cur); cur, size = [], 0
        cur.append(w); size += sz
    if cur:
        batches.append(cur)
    fail = []
    for i, bt in enumerate(batches):
        p = os.path.join(a.keluar, f'batch_{i}.json'); json.dump(bt, open(p, 'w'), indent=1); fail.append(p)
    ring = dict(dibina=dibina, sesi=S, dokumen=len(tulis), batch=fail, tanpa_versi=[f"{w['collection']}/{w['doc_id']}" for w, _ in tulis if 'if_version' not in w],
                pengawas=pengawas(st, masa), ralat=ralat)
    json.dump(ring, open(os.path.join(a.keluar, 'ringkas.json'), 'w'), ensure_ascii=False, indent=1)
    print(json.dumps(ring, ensure_ascii=False, indent=1))


if __name__ == '__main__':
    main()
