"""Jejak hadapan portfolio maya 10 slot (sejak 19 Okt 2026; kajian kajian/KAJIAN_PORTFOLIO.md). Rekod sahaja: tiada order,
tiada wang sebenar. Dibina semula sepenuhnya daripada Lejar Penuh pada setiap larian (deterministik, tanpa LLM):
  RS_10    — setiap sesi beli, slot kosong diisi dengan posisi lejar baharu yang RS pasarannya (data/rs/rs_pasaran.csv pada
             tarikh isyarat) tertinggi; RS tiada -> paling akhir.
  RAWAK_10 — kawalan: susunan rawak tetap (benih = tarikh beli), supaya kelebihan RS boleh diukur ke hadapan.
Gabungan beku (22 Okt 2026, Fasa 4 item 13; data/analisis/gabungan_beku.json; hanya posisi dibeli >= mula_jejak):
  GABUNGAN_10     — kaedah gabungan beku, kuota slot setiap kaedah (slot tidak terpakai dikongsi), keluar ikut lorong
                    terbaik setiap kaedah (kaedah = keluar lorong 1 Lejar, tunai sesi berikutnya; henti = lorong 2).
  TOP1_10         — kaedah #1 sahaja, 10 slot, lorongnya.
  RAWAK_KAEDAH_10 — kawalan: kaedah rawak beku (bilangan sama, benih tetap), kuota sama, lorong 2.
  Kaedah beku yang Papan Penganalisis tandakan GANTUNG/BERSARA tidak dibeli lagi mulai sesi selepas status dilihat (log
  portfolio_slot/gantung.csv; posisi sedia ada kekal hingga keluar). Susunan dalam sesi = rawak tetap (benih = tarikh beli).
Peraturan sama dengan kajian: 10 slot; saiz = min(tunai, ekuiti semalam x 10%); satu posisi bagi setiap saham; keluar =
lorong 2 lejar (Chandelier tutup 4xATR14, jual pada buka esok; lajur *_henti), direalisasi sebelum belian hari sama;
nilai pasaran = saiz x tutup / harga beli; kos 0.1% setiap belah (seperti enjin). Calon = posisi yang lejar beli (isyarat
100% semua kaedah, seluruh alam Shariah >= USD10; tiada bias kemandirian set 431).
Rangka risiko (pra-daftar 25 Okt 2026, kajian/portfolio/PRA_DAFTAR_PLAYBOOK.md; audit risiko 25 Okt 2026):
  PLAYBOOK_10     — calon lejar yang lulus penapis P1–P11 (harga, kecairan, sejarah, sah data, RS 80–94, Trend Template, industri
                    v2 bukan E, ATR14% <= 6%, jurang buka <= +3%, earnings, rejim SPY), susun RS menurun (seri rawak berbenih);
                    saiz risiko 1% ekuiti ke paras Chandelier awal (had 15%), <= 20 posisi, heat <= 10%, <= 3 sektor / 2 industri,
                    <= 3 belian sehari; keluar Chandelier 4xATR14 + henti masa (bar ke-20 < +1R); brek 15%/pulih 10%, kill_switch
                    25%; kos 0.25% setiap belah (enjin bina_pb, dikongsi dengan kajian dalam sampel kaji_portfolio.py playbook).
  RAWAK_PADAN_10  — kawalan: peraturan sama tepat, susunan calon rawak (benih tetap 1).
  Keputusan penapis setiap sesi beli dibekukan dalam PLAYBOOK_calon.csv / PLAYBOOK_tapis.csv (tambah sahaja).
Semua portfolio: lajur posisi tambahan amaun, nilai_semasa, paras_keluar, jarak_pct, jarak_atr, risiko_pct, sektor_us,
industri_us, hari (perinci()); heat = sigma nilai x jarak ke paras keluar / ekuiti. Isu diketahui RS_10 (tidak diubah,
eksperimen beku): seri RS dipecah ikut abjad saham (susun stabil atas calon yang diisih saham), dan 10 slot diisi pada sesi pertama.
  python3 BacktestShariah2/standard/portfolio_slot.py   -> BacktestShariah2/portfolio_slot/ (dijalankan oleh lejar.yml)
"""
import bisect, os, sys, json
from collections import Counter
from datetime import date, timedelta

import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
BS2 = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(BS2, 'kod')); sys.path.insert(0, HERE)
from stor import muat, frames_dict  # noqa: E402
import keluar_lorong as KL  # noqa: E402

LEJAR = os.environ.get('LEJAR_DIR', os.path.join(BS2, 'lejar'))
STOR = os.environ.get('LEJAR_STOR', os.path.join(BS2, 'data', 'harga', 'stor'))
RS = os.path.join(BS2, 'data', 'rs', 'rs_pasaran.csv')
KELUAR = os.environ.get('PORTFOLIO_SLOT_DIR', os.path.join(BS2, 'portfolio_slot'))
BEKU = os.environ.get('GABUNGAN_BEKU', os.path.join(BS2, 'data', 'analisis', 'gabungan_beku.json'))
PAPAN = os.environ.get('PAPAN_ANALISIS', os.path.join(BS2, 'data', 'analisis', 'papan.json'))
KUMPULAN = os.environ.get('GRED_KUMPULAN_SEJARAH', os.path.join(BS2, 'data', 'kumpulan', 'gred_kumpulan_sejarah.csv'))
PETA = os.environ.get('PETA_INDUSTRI', os.path.join(BS2, 'papertrade', 'peta_industri.csv'))
PEMANGKIN = os.environ.get('PEMANGKIN_DIR', os.path.join(BS2, 'data', 'pemangkin'))
AMBIL_ALIH = os.environ.get('AMBIL_ALIH', os.path.join(BS2, 'data', 'ambil_alih.csv'))
SLOT, W, KOS = 10, 0.10, 0.001
PORTFOLIO = {'RS_10': 'RS pasaran tertinggi', 'RAWAK_10': 'Rawak (kawalan)', 'GABUNGAN_10': 'Gabungan kaedah beku',
             'TOP1_10': 'Kaedah #1 sahaja', 'RAWAK_KAEDAH_10': 'Kaedah rawak (kawalan gabungan)',
             'PLAYBOOK_10': 'Playbook rangka risiko (RS 80–94)', 'RAWAK_PADAN_10': 'Rawak padan (kawalan rangka risiko)'}
BEKU_JENIS = ('GABUNGAN_10', 'TOP1_10', 'RAWAK_KAEDAH_10')
L_POSISI = ['saham', 'id_kaedah', 'tarikh_isyarat', 'rs', 'tarikh_beli', 'harga_beli', 'saiz_pct', 'status', 'tarikh_keluar',
            'harga_keluar', 'untung_pct', 'harga_terkini', 'untung_semasa_pct', 'lorong']
L_EKUITI = ['tarikh', 'ekuiti', 'tunai', 'bil_posisi', 'spy']
# lajur tambahan setiap posisi (25 Okt 2026; perinci()): amaun = pecahan ekuiti mula yang dibelanjakan; nilai_semasa = amaun x
# tutup / harga beli; paras_keluar = paras lorong (Chandelier 4xATR14, atau henti kaedah bagi lorong kaedah); risiko_pct =
# nilai x max(0, jarak) / ekuiti (tiada paras = nilai penuh); hari = bilangan bar saham sejak beli (hari beli = 1)
L_PERINCI = ['amaun', 'nilai_semasa', 'paras_keluar', 'jarak_pct', 'jarak_atr', 'risiko_pct', 'sektor_us', 'industri_us', 'hari']


def calon_lejar():
    """Semua posisi lejar yang dibeli (terbuka + tutup) dengan lorong 2 dan RS pada tarikh isyarat."""
    import lejar
    T, O = lejar.semua_posisi()
    P = pd.concat([T, O], ignore_index=True)
    P = P[(P.tarikh_beli != '') & (P.harga_beli != '')].copy()
    P['harga_beli'] = P.harga_beli.astype(float)
    P['keluar'] = P.keluar_henti.astype(str).str.lower().eq('true') & P.tarikh_keluar_henti.ne('')
    P['harga_keluar_henti'] = pd.to_numeric(P.harga_keluar_henti, errors='coerce')
    P['harga_keluar1'] = pd.to_numeric(P.harga_keluar, errors='coerce')
    P['keluar1'] = P.tarikh_keluar.ne('') & P.harga_keluar1.notna()
    if os.path.exists(RS):
        r = pd.read_csv(RS, usecols=['tarikh', 'ticker', 'rs']).rename(columns={'tarikh': 'tarikh_isyarat', 'ticker': 'saham'})
        P = P.merge(r.drop_duplicates(['tarikh_isyarat', 'saham']), on=['tarikh_isyarat', 'saham'], how='left')
    else:
        P['rs'] = np.nan
    return P.sort_values(['tarikh_beli', 'saham', 'id_kaedah']).reset_index(drop=True)


def susun(G, jenis, tarikh):
    """Susunan calon satu sesi beli. G diisih saham, id_kaedah (tetap)."""
    if jenis == 'RS_10':
        return G.assign(_k=G.rs.fillna(-1.0)).sort_values('_k', ascending=False, kind='stable')
    rng = np.random.default_rng(int(tarikh.replace('-', '')))
    return G.iloc[rng.permutation(len(G))]


def konfigurasi(beku):
    """{jenis: dict(mula, kuota {id: slot}, lorong {id: 'kaedah'|'henti'})} daripada gabungan_beku.json; {} jika tiada."""
    if not beku:
        return {}
    K, ruj = beku['kaedah'], beku.get('rujukan', {})
    out = {'GABUNGAN_10': dict(kuota={k['id']: int(k['slot']) for k in K}, lorong={k['id']: k['lorong'] for k in K})}
    t = ruj.get('TOP1_10')
    if t:
        out['TOP1_10'] = dict(kuota={t['id']: SLOT}, lorong={t['id']: t['lorong']})
    r = ruj.get('RAWAK_KAEDAH_10')
    if r:
        out['RAWAK_KAEDAH_10'] = dict(kuota=dict(zip(r['id'], (int(x) for x in r['slot']))), lorong={i: r['lorong'] for i in r['id']})
    for v in out.values():
        v['mula'] = beku['mula_jejak']
    return out


def keluar_pada(p, d, sebelum_beli):
    """(tarikh, harga) keluar posisi p yang direalisasi pada sesi d: lorong 2 (jual buka) sebelum belian hari itu; lorong
    kaedah sebelum belian jika keluar sebelum d, selepas belian jika keluar pada d (harga keluar intrahari/tutup)."""
    if p.get('lorong', 'henti') == 'henti':
        if sebelum_beli and p['keluar'] and p['tarikh_keluar_henti'] <= d:
            return p['tarikh_keluar_henti'], p['harga_keluar_henti']
    elif p.get('keluar1'):
        t = p['tarikh_keluar']
        if (t < d) if sebelum_beli else (t <= d):
            return t, p['harga_keluar1']
    return None


def bina(P, jenis, hari, tutup, cfg=None, gantung=None):
    """hari: senarai tarikh 'YYYY-MM-DD' (sesi dagangan); tutup(saham, tarikh) -> harga tutup atau None. cfg (portfolio beku):
    dict(mula, kuota, lorong); gantung: {id_kaedah: tarikh mula tiada belian}. Pulang (posisi DataFrame, ekuiti DataFrame)."""
    tunai = eq = 1.0; pos = {}; rekod = []; kurva = []; gantung = gantung or {}
    if cfg:
        P = P[P.id_kaedah.isin(list(cfg['kuota'])) & (P.tarikh_beli >= cfg['mula'])]
        hari = [d for d in hari if d >= cfg['mula']]
    ikut_beli = {d: g for d, g in P.groupby('tarikh_beli')}

    def realisasi(sebelum_beli):
        nonlocal tunai
        for s in list(pos):
            k = keluar_pada(pos[s], d, sebelum_beli)
            if k is None:
                continue
            p = pos.pop(s); t, hk = k
            tunai += p['amaun'] * hk / p['harga_beli'] * (1 - KOS) / (1 + KOS)
            rekod.append(dict(p, status='Keluar', tarikh_keluar=t, harga_keluar=hk,
                              untung_pct=100 * (hk / p['harga_beli'] * (1 - KOS) / (1 + KOS) - 1)))

    def beli(r):
        nonlocal tunai
        am = min(tunai, eq * W)
        if am <= 1e-12:
            return False
        lor = cfg['lorong'][r['id_kaedah']] if cfg else 'henti'
        tunai -= am; pos[r['saham']] = dict(r, amaun=am, saiz_pct=100 * am / eq, lorong=lor)
        return True

    for d in hari:
        realisasi(True)
        if d in ikut_beli:
            G = susun(ikut_beli[d], 'RAWAK_10' if cfg else jenis, d).to_dict('records')
            if cfg:
                G = [r for r in G if not (r['id_kaedah'] in gantung and gantung[r['id_kaedah']] <= d)]
                kini = {}
                for p in pos.values():
                    kini[p['id_kaedah']] = kini.get(p['id_kaedah'], 0) + 1
                for r in G:   # 1: dalam kuota setiap kaedah
                    if len(pos) >= SLOT: break
                    if r['saham'] in pos or kini.get(r['id_kaedah'], 0) >= cfg['kuota'][r['id_kaedah']]: continue
                    if not beli(r): break
                    kini[r['id_kaedah']] = kini.get(r['id_kaedah'], 0) + 1
            for r in G:       # RS/RAWAK: semua; beku: 2 = slot tidak terpakai dikongsi
                if len(pos) >= SLOT: break
                if r['saham'] in pos: continue
                if not beli(r): break
        realisasi(False)
        mv = 0.0
        for s, p in pos.items():
            c = tutup(s, d)
            mv += p['amaun'] * (c / p['harga_beli'] if c else 1.0)
        eq = tunai + mv; kurva.append(dict(tarikh=d, ekuiti=eq, tunai=tunai, bil_posisi=len(pos)))
    akhir = hari[-1] if hari else ''
    for s, p in pos.items():
        c = tutup(s, akhir)
        rekod.append(dict(p, status='Pegang', harga_terkini=c, tarikh_keluar='', harga_keluar=np.nan, untung_pct=np.nan,
                          untung_semasa_pct=100 * (c / p['harga_beli'] - 1) if c else np.nan))
    R = pd.DataFrame(rekod).reindex(columns=L_POSISI + ['amaun', 'henti'])
    return R.sort_values(['tarikh_beli', 'saham']).reset_index(drop=True), pd.DataFrame(kurva, columns=L_EKUITI[:-1])


def muat_json(path):
    try:
        with open(path, encoding='utf-8') as f:
            return json.load(f)
    except (OSError, ValueError):
        return None


def log_gantung(CFG, sesi, papan=PAPAN, path=None):
    """{id: tarikh mula tiada belian}: log portfolio_slot/gantung.csv (tambah sahaja). Kaedah beku yang papan.json tandakan
    GANTUNG/BERSARA dan belum dilog ditambah dengan tarikh = sesi selepas sesi terakhir (status dilihat selepas sesi itu)."""
    path = path or os.path.join(KELUAR, 'gantung.csv')
    L = pd.read_csv(path, dtype=str) if os.path.exists(path) else pd.DataFrame(columns=['tarikh', 'id_kaedah', 'pantau', 'sebab'])
    beku = {i for c in CFG.values() for i in c['kuota']}
    A = muat_json(papan) or {}
    baru = [dict(tarikh=str((pd.Timestamp(sesi) + pd.offsets.BDay(1)).date()), id_kaedah=r['id'], pantau=r.get('pantau'),
                 sebab=r.get('p_sebab', '')) for r in A.get('rows', [])
            if sesi and r.get('id') in beku and r.get('pantau') in ('GANTUNG', 'BERSARA') and r['id'] not in set(L.id_kaedah)]
    if baru:
        L = pd.concat([L, pd.DataFrame(baru)], ignore_index=True); L.to_csv(path, index=False)
    return dict(zip(L.id_kaedah, L.tarikh))


def mdd(x):
    x = pd.Series(np.r_[1.0, np.asarray(x, float)]); return float((x / x.cummax() - 1).min())   # ekuiti mula = 1 (buka hari pertama)


# ---------------------------------------------------------------- PLAYBOOK_10 / RAWAK_PADAN_10 (pra-daftar 25 Okt 2026)
# Peraturan tepat: kajian/portfolio/PRA_DAFTAR_PLAYBOOK.md. Enjin bina_pb dan penapis tapis_pb dikongsi dengan kajian dalam
# sampel (kajian/portfolio/kaji_portfolio.py playbook) supaya ujian dan jejak hadapan memakai kod yang sama.
PB_JENIS = ('PLAYBOOK_10', 'RAWAK_PADAN_10')
PB_BENIH = {'PLAYBOOK_10': 0, 'RAWAK_PADAN_10': 1}
PB_MULA = '2026-10-16'          # sesi beli pertama Lejar Penuh
PB_PRA_DAFTAR = '2026-10-23'    # tutup sesi terakhir sebelum pra-daftar (25 Okt 2026); tempoh hadapan bersih bermula selepasnya
PB = dict(harga_min=10.0, nilai_min=20e6, nilai_bar=20, sejarah_min=252, rs_min=80, rs_maks=94, sma200_lalu=21,
          tinggi_bar=252, dari_tinggi=0.15, atr_maks=0.06, jurang_maks=0.03, earn_sesi=5, earn_lalu_hari=40, lompat=0.40,
          lompat_bar=60, risiko=0.01, had=0.15, maks_posisi=20, heat_maks=0.10, maks_sektor=3, maks_industri=2,
          beli_sehari=3, ganda=KL.GANDA_ATR, masa_sesi=20, masa_r=1.0, brek=-0.15, pulih=-0.10, bunuh=-0.25, kos=0.0025,
          min_amaun=0.01, delist_sesi=10, tangguh_sesi=5)
SEBAB_PB = ['harga', 'kecairan', 'sejarah', 'sah', 'rs', 'trend', 'industri', 'atr', 'jurang', 'earnings', 'rejim', 'paras']
GRED_LULUS = ('A', 'B', 'C', 'D')
L_CALON_PB = ['tarikh_beli', 'saham', 'tarikh_isyarat', 'id_kaedah', 'harga_beli', 'tutup', 'rs', 'gred_industri', 'sektor_us',
              'industri_us', 'nilai_med', 'n_bar', 'atr_pct', 'dari_tinggi', 'jurang', 'r_awal', 'earnings', 'dinilai']
L_POSISI_PB = L_POSISI + ['amaun', 'r_awal', 'sebab_keluar', 'r_multiple', 'keluar_esok', 'paras_keluar', 'sektor_us', 'industri_us']
L_EKUITI_PB = ['tarikh', 'ekuiti', 'tunai', 'bil_posisi', 'heat', 'brek', 'kill_switch']


def ciri_siri(g, prm=PB):
    """Ciri penapis PLAYBOOK pada tutup setiap bar satu saham (g: DataFrame open/high/low/close/volume menaik berindeks tarikh).
    Tiada pandang hadapan: setiap nilai hanya memakai bar <= bar itu."""
    c = g.close.astype(float); h = g.high.astype(float)
    a = pd.Series(KL.atr(h.to_numpy(), g.low.astype(float).to_numpy(), c.to_numpy()), index=g.index)
    s200 = c.rolling(200).mean(); lomp = (c / c.shift(1) - 1).abs()
    return pd.DataFrame(dict(
        tutup=c, n_bar=np.arange(1, len(c) + 1, dtype=float),
        nilai_med=(c * g.volume.astype(float)).rolling(prm['nilai_bar']).median(),
        sma50=c.rolling(50).mean(), sma150=c.rolling(150).mean(), sma200=s200, sma200_lalu=s200.shift(prm['sma200_lalu']),
        tinggi52=h.rolling(prm['tinggi_bar']).max(), atr=a, atr_pct=a / c,
        semak_data=lomp.rolling(prm['lompat_bar'], min_periods=1).max().gt(prm['lompat'])), index=g.index)


def tapis_pb(X, prm=PB):
    """X: DataFrame ciri calon (ciri_siri pada bar isyarat + rs, gred_industri, jurang, r_awal, earnings, spy_atas, ambil_alih).
    Pulang DataFrame bool: gagal setiap penapis SEBAB_PB (nilai tiada = gagal)."""
    f = lambda k: pd.to_numeric(X[k], errors='coerce') if k in X else pd.Series(np.nan, index=X.index)
    c, rs = f('tutup'), f('rs')
    G = pd.DataFrame(index=X.index)
    G['harga'] = ~(c >= prm['harga_min'])
    G['kecairan'] = ~(f('nilai_med') >= prm['nilai_min'])
    G['sejarah'] = ~(f('n_bar') >= prm['sejarah_min'])
    aa = X['ambil_alih'].fillna(False).astype(bool) if 'ambil_alih' in X else False
    G['sah'] = ~(X['semak_data'].eq(False) & ~aa)
    G['rs'] = ~((rs >= prm['rs_min']) & (rs <= prm['rs_maks']))
    G['trend'] = ~((c > f('sma50')) & (f('sma50') > f('sma150')) & (f('sma150') > f('sma200')) & (f('sma200') > f('sma200_lalu'))
                   & (c >= (1 - prm['dari_tinggi']) * f('tinggi52')))
    G['industri'] = ~X['gred_industri'].isin(GRED_LULUS)
    G['atr'] = ~(f('atr_pct') <= prm['atr_maks'])
    G['jurang'] = ~(f('jurang') <= prm['jurang_maks'])
    G['earnings'] = ~X['earnings'].eq('tiada')
    G['rejim'] = ~X['spy_atas'].eq(True)
    G['paras'] = ~(f('r_awal') > 0)
    return G


def masa_earnings(m):
    """'pra' | 'lepas' | '' (tidak diketahui). Teks Nasdaq time-pre-market / time-after-hours; HH:MM < 09:30 pra, >= 16:00 lepas."""
    m = str(m or '').lower()
    if 'pre' in m or 'bmo' in m:
        return 'pra'
    if 'after' in m or 'amc' in m:
        return 'lepas'
    hh, mm = m[:2], m[3:5]
    if len(m) >= 5 and m[2] == ':' and hh.isnumeric() and mm.isnumeric():
        hm = int(hh) * 60 + int(mm)
        return 'pra' if hm < 9 * 60 + 30 else 'lepas' if hm >= 16 * 60 else ''
    return ''


def earnings_dekat(isyarat, sesi5, peristiwa):
    """True jika ada sesi reaksi earnings dalam sesi5 (5 sesi dagangan selepas tarikh isyarat; 'YYYY-MM-DD').
    peristiwa: [(tarikh earnings, masa)]. Reaksi: pra -> sesi pertama >= tarikh; lepas -> sesi pertama > tarikh; tidak
    diketahui -> kedua-duanya."""
    if not sesi5:
        return False
    hari = [isyarat] + list(sesi5); dalam = set(sesi5)
    for d0, m in peristiwa:
        if not (isyarat <= d0 <= sesi5[-1]):
            continue
        k = masa_earnings(m); R = set()
        if k != 'lepas':
            R.add(next((s for s in hari if s >= d0), None))
        if k != 'pra':
            R.add(next((s for s in hari if s > d0), None))
        if R & dalam:
            return True
    return False


_CUTI = None


def cuti_nyse():
    """Cuti biasa XNYS (exchange_calendars dipin kekangan.txt); tiada pustaka -> tiada cuti (hari bekerja sahaja)."""
    global _CUTI
    if _CUTI is None:
        try:
            import exchange_calendars as xc
            h = xc.get_calendar('XNYS').regular_holidays.holidays(pd.Timestamp('2000-01-01'), pd.Timestamp('2035-12-31'))
            _CUTI = np.array([d.date() for d in h], dtype='datetime64[D]')
        except Exception:  # noqa: BLE001
            _CUTI = np.array([], dtype='datetime64[D]')
    return _CUTI


def sesi_selepas(t, n, sesi):
    """n sesi dagangan selepas tarikh t: daripada `sesi` (senarai tarikh SPY menaik), disambung dengan kalendar XNYS."""
    i = bisect.bisect_right(sesi, t); out = list(sesi[i:i + n])
    d = np.datetime64(out[-1] if out else t, 'D')
    while len(out) < n:
        d = np.busday_offset(d, 1, roll='forward', holidays=cuti_nyse()); out.append(str(d))
    return out


class Siri:
    """Tatasusunan harga satu saham bagi enjin PLAYBOOK dan perinci(): t (tarikh str), ix {tarikh: indeks bar}, o, c,
    a (ATR14 seperti keluar_lorong.atr)."""
    def __init__(self, g):
        self.t = [d.strftime('%Y-%m-%d') for d in g.index]; self.ix = {d: j for j, d in enumerate(self.t)}
        self.o = g.open.to_numpy(float); self.c = g.close.to_numpy(float)
        self.a = KL.atr(g.high.to_numpy(float), g.low.to_numpy(float), self.c)


def susun_pb(G, jenis, tarikh, benih=None):
    """Susunan calon satu sesi (pra-daftar §3): PLAYBOOK = RS menurun, seri rawak berbenih; RAWAK_PADAN = permutasi rawak."""
    benih = PB_BENIH[jenis] if benih is None else benih
    G = G.sort_values('saham', kind='stable')
    G = G.iloc[np.random.default_rng([int(benih), int(tarikh.replace('-', ''))]).permutation(len(G))]
    if jenis == 'PLAYBOOK_10':
        G = G.assign(_k=pd.to_numeric(G.rs, errors='coerce').fillna(-1.0)).sort_values('_k', ascending=False, kind='stable')
    return G


def bina_pb(C, hari, harga, jenis, benih=None, prm=PB):
    """Enjin PLAYBOOK_10 / RAWAK_PADAN_10 (pra-daftar §4–5). C: calon LULUS (saham, tarikh_beli, tarikh_isyarat, id_kaedah, rs,
    harga_beli, r_awal, sektor_us, industri_us); hari: sesi 'YYYY-MM-DD' menaik; harga: {saham: Siri}.
    Susunan sesi: jual pada buka (dicetus tutup semalam) -> beli pada buka -> nilai pada tutup -> semak Chandelier, henti masa,
    brek dan kill_switch. Pulang (posisi, ekuiti); ekuiti mula 1.0. bina_pb.bunuh = tarikh kill_switch ('' jika tiada)."""
    fj = (1 - prm['kos']) / (1 + prm['kos'])
    tunai = eq = puncak = 1.0; pos = {}; rekod = []; kurva = []; brek = False; bunuh = ''
    ikut = {d: g for d, g in C.groupby('tarikh_beli')} if len(C) else {}
    luar = prm.get('brek_luar')       # analisis kepekaan sahaja (bukan peraturan pra-daftar): {tarikh: brek belian pada sesi itu}

    def jual(s, t, hk, sebab):
        nonlocal tunai
        p = pos.pop(s); u = hk / p['harga_beli'] * fj
        tunai += p['amaun'] * u
        rekod.append(dict(p, status='Keluar', tarikh_keluar=t, harga_keluar=hk, untung_pct=100 * (u - 1), sebab_keluar=sebab,
                          r_multiple=(u - 1) / p['r_awal'], keluar_esok=''))

    for d in hari:
        for s in list(pos):                                   # 1. jualan pada buka
            p = pos[s]; sr = harga[s]; j = sr.ix.get(d)
            if j is None:
                p['tiada'] += 1
                if p['tiada'] >= prm['delist_sesi']:
                    jual(s, sr.t[p['j']], float(sr.c[p['j']]), 'delist')
                continue
            p['tiada'] = 0
            if p['keluar_esok']:
                jual(s, d, float(sr.o[j]), p['keluar_esok'])
        blok = brek if luar is None else bool(luar.get(d, False))
        if not bunuh and not blok and d in ikut:              # 2. belian pada buka
            hs = sum(p['amaun'] * p['c'] / p['harga_beli'] * p['jarak'] for p in pos.values())
            ns = Counter(p['sektor_us'] for p in pos.values()); ni = Counter(p['industri_us'] for p in pos.values()); nb = 0
            for r in susun_pb(ikut[d], jenis, d, benih).to_dict('records'):
                if nb >= prm['beli_sehari'] or len(pos) >= prm['maks_posisi']:
                    break
                s = r['saham']; sr = harga.get(s)
                if s in pos or sr is None or sr.ix.get(d) is None:
                    continue
                if ns[r['sektor_us']] >= prm['maks_sektor'] or ni[r['industri_us']] >= prm['maks_industri']:
                    continue
                rf = float(r['r_awal']); am = min(tunai, eq * min(prm['had'], prm['risiko'] / rf))
                if am < prm['min_amaun'] * eq:
                    break                                     # tunai tidak cukup
                if (hs + am * rf) / eq > prm['heat_maks']:
                    continue                                  # heat > 10%: tolak, calon seterusnya dinilai
                tunai -= am; hs += am * rf; nb += 1; ns[r['sektor_us']] += 1; ni[r['industri_us']] += 1
                pos[s] = dict(r, amaun=am, saiz_pct=100 * am / eq, lorong='playbook', j=sr.ix[d], c=float(r['harga_beli']),
                              puncak=-np.inf, paras=-np.inf, sesi=0, tiada=0, keluar_esok='', jarak=rf,
                              R=rf * float(r['harga_beli']))
        mv = ht = 0.0                                         # 3. nilai pada tutup + semakan keluar
        for s, p in pos.items():
            sr = harga[s]; j = sr.ix.get(d)
            if j is not None:
                c = float(sr.c[j]); p['c'] = c; p['j'] = j; p['sesi'] += 1; p['puncak'] = max(p['puncak'], c)
                if np.isfinite(sr.a[j]):
                    p['paras'] = max(p['paras'], p['puncak'] - prm['ganda'] * sr.a[j])
                if not p['keluar_esok']:
                    if c < p['paras']:
                        p['keluar_esok'] = 'chandelier'
                    elif p['sesi'] == prm['masa_sesi'] and c < p['harga_beli'] + prm['masa_r'] * p['R']:
                        p['keluar_esok'] = 'masa'
                p['jarak'] = min(1.0, max(0.0, (c - p['paras']) / c)) if np.isfinite(p['paras']) else 1.0
            nilai = p['amaun'] * p['c'] / p['harga_beli']; mv += nilai; ht += nilai * p['jarak']
        eq = tunai + mv; puncak = max(puncak, eq); dd = eq / puncak - 1
        if not bunuh and dd <= prm['bunuh']:
            bunuh = d
            for p in pos.values():
                p['keluar_esok'] = p['keluar_esok'] or 'kill_switch'
        elif not bunuh:
            brek = True if dd <= prm['brek'] else (False if brek and dd >= prm['pulih'] else brek)
        kurva.append(dict(tarikh=d, ekuiti=eq, tunai=tunai, bil_posisi=len(pos), heat=ht / eq,
                          brek=int((brek if luar is None else blok) and not bunuh),
                          kill_switch=int(bool(bunuh))))
    for s, p in pos.items():
        rekod.append(dict(p, status='Pegang', harga_terkini=p['c'], tarikh_keluar='', harga_keluar=np.nan, untung_pct=np.nan,
                          untung_semasa_pct=100 * (p['c'] / p['harga_beli'] - 1),
                          paras_keluar=p['paras'] if np.isfinite(p['paras']) else np.nan))
    R = pd.DataFrame(rekod).reindex(columns=L_POSISI_PB)
    bina_pb.bunuh = bunuh
    return R.sort_values(['tarikh_beli', 'saham']).reset_index(drop=True), pd.DataFrame(kurva, columns=L_EKUITI_PB)


# ------------------------------------------- calon hadapan (Lejar Penuh) + rekod beku PLAYBOOK_calon.csv / PLAYBOOK_tapis.csv
def peta_industri(path=PETA):
    """{ticker: (industri_us, sektor_us)} (sektor = sektor_pasaran.SEKTOR_INDUSTRI)."""
    from sektor_pasaran import SEKTOR_INDUSTRI
    if not os.path.exists(path):
        return {}
    p = pd.read_csv(path, dtype=str).drop_duplicates('ticker')
    return {t: (i, SEKTOR_INDUSTRI.get(i, '')) for t, i in zip(p.ticker, p.industri.fillna(''))}


def masa_kalendar(folder=PEMANGKIN):
    """({(ticker, 'YYYY-MM-DD'): masa}, json Nasdaq) daripada tarikh_pendapatan.csv dan earnings_nasdaq.json."""
    M = {}
    p = os.path.join(folder, 'tarikh_pendapatan.csv')
    if os.path.exists(p):
        d = pd.read_csv(p, dtype=str)
        M.update({(t, x): m for t, x, m in zip(d.ticker, d.d0.str[:10], d.masa.fillna(''))})
    nas = muat_json(os.path.join(folder, 'earnings_nasdaq.json')) or {}
    for t, e in (nas.get('saham') or {}).items():
        for k in ('lalu', 'seterusnya'):
            if e.get(k):
                M.setdefault((t, str(e[k])[:10]), e.get(f'{k}_masa', ''))
    return M, nas


def status_earnings(t, isyarat, sesi5, K, M, nas, prm=PB):
    """'ada' (reaksi dalam 5 sesi) | 'tiada' (liputan diketahui, tiada) | 'tidak diketahui' (pra-daftar P10)."""
    import kalendar_earnings as KE
    ev = [(x.isoformat(), M.get((t, x.isoformat()), '')) for x in K.get(t, {})]
    if earnings_dekat(isyarat, sesi5, ev):
        return 'ada'
    D = date.fromisoformat(isyarat)
    te, _ = KE.seterusnya(K, t, D)
    if te and te.isoformat() > sesi5[-1]:
        return 'tiada'
    tl, _ = KE.lalu(K, t, D + timedelta(days=1))
    if tl and (D - tl).days <= prm['earn_lalu_hari']:
        return 'tiada'
    if t in (nas.get('saham') or {}) and str(nas.get('dari', '9')) <= sesi5[0] and str(nas.get('hingga', '0')) >= sesi5[-1]:
        return 'tiada'
    return 'tidak diketahui'


def calon_pb(P, fr, idx, rs_path=RS, kump_path=KUMPULAN, folder_pem=PEMANGKIN, aa_path=AMBIL_ALIH, peta=None, prm=PB):
    """Satu calon setiap (tarikh_beli, saham) daripada posisi lejar P (calon_lejar), dengan ciri pada tarikh isyarat,
    lajur gagal_<SEBAB_PB> dan `lulus`; `data_tiada` = sumber RS / gred industri belum ada bagi tarikh isyarat itu."""
    import kalendar_earnings as KE
    import ambil_alih as AA
    if P.empty:
        return pd.DataFrame(columns=L_CALON_PB + [f'gagal_{k}' for k in SEBAB_PB] + ['lulus', 'data_tiada'])
    G = (P.groupby(['tarikh_beli', 'saham'], sort=True)
         .agg(tarikh_isyarat=('tarikh_isyarat', 'max'), harga_beli=('harga_beli', 'first'), rs=('rs', 'first'),
              id_kaedah=('id_kaedah', lambda x: ','.join(sorted(set(x))))).reset_index())
    F = []
    for t, g in G.groupby('saham'):
        if t in fr:
            f = ciri_siri(fr[t], prm); f.index = [x.strftime('%Y-%m-%d') for x in f.index]
            F.append(f.reindex(g.tarikh_isyarat).set_axis(g.index))
    if F:
        G = G.join(pd.concat(F))
    for k in ('tutup', 'atr', 'tinggi52', 'nilai_med', 'n_bar', 'atr_pct', 'semak_data'):
        if k not in G:
            G[k] = np.nan
    peta = peta_industri() if peta is None else peta
    G['industri_us'] = [peta.get(t, ('', ''))[0] for t in G.saham]; G['sektor_us'] = [peta.get(t, ('', ''))[1] for t in G.saham]
    rs_tarikh = set(pd.read_csv(rs_path, usecols=['tarikh']).tarikh) if os.path.exists(rs_path) else set()
    gi, k_tarikh = {}, set()
    if os.path.exists(kump_path):
        K = pd.read_csv(kump_path, dtype=str); K = K[K.jenis == 'Industri']
        gi = dict(zip(zip(K.tarikh, K.nama), K.gred)); k_tarikh = set(K.tarikh)
    G['gred_industri'] = [gi.get((d, i), '') for d, i in zip(G.tarikh_isyarat, G.industri_us)]
    G['data_tiada'] = [not (d in rs_tarikh and d in k_tarikh) for d in G.tarikh_isyarat]
    s = idx['SPY'].close; sa = s > s.rolling(200).mean(); sa.index = [x.strftime('%Y-%m-%d') for x in sa.index]
    G['spy_atas'] = G.tarikh_isyarat.map(sa.to_dict())
    G['jurang'] = G.harga_beli / G.tutup - 1
    G['r_awal'] = (G.harga_beli - (G.tutup - prm['ganda'] * G.atr)) / G.harga_beli
    G['dari_tinggi'] = 1 - G.tutup / G.tinggi52
    umum = {r['saham']: r.get('tarikh_umum', '') for r in AA.baca_senarai(aa_path)}
    G['ambil_alih'] = [bool(umum.get(t)) and umum[t] <= d for t, d in zip(G.saham, G.tarikh_isyarat)]
    Kal = KE.muat(folder_pem); M, nas = masa_kalendar(folder_pem); sesi = sorted(sa.index)
    G['earnings'] = [status_earnings(t, d, sesi_selepas(d, prm['earn_sesi'], sesi), Kal, M, nas, prm)
                     for t, d in zip(G.saham, G.tarikh_isyarat)]
    G = G.join(tapis_pb(G, prm).add_prefix('gagal_')); G['lulus'] = ~G[[f'gagal_{k}' for k in SEBAB_PB]].any(axis=1)
    return G


def log_pb(C, sesi, folder=None, dinilai=None, prm=PB):
    """Bekukan keputusan penapis (pra-daftar §6): sesi beli >= PB_MULA yang belum ada dalam PLAYBOOK_tapis.csv ditambah ke
    PLAYBOOK_calon.csv (calon lulus) dan PLAYBOOK_tapis.csv (bilangan gagal setiap penapis). Sesi dengan data_tiada ditangguh
    selagi < tangguh_sesi sesi berlalu (kemudian calon itu gagal 'data tiada'). Pulang (calon lulus beku, tapis, ditangguh)."""
    folder = folder or KELUAR
    pc, pt = os.path.join(folder, 'PLAYBOOK_calon.csv'), os.path.join(folder, 'PLAYBOOK_tapis.csv')
    baca = lambda: pd.read_csv(pc, dtype={'tarikh_beli': str, 'saham': str, 'tarikh_isyarat': str, 'id_kaedah': str},
                               keep_default_na=False)
    L = baca() if os.path.exists(pc) else pd.DataFrame(columns=L_CALON_PB)
    T = pd.read_csv(pt, dtype={'tarikh_beli': str}) if os.path.exists(pt) else pd.DataFrame(columns=['tarikh_beli'])
    sudah = set(T.tarikh_beli)
    dinilai = dinilai or pd.Timestamp.now(tz='Asia/Kuala_Lumpur').strftime('%Y-%m-%d %H:%M MYT')
    baru_c, baru_t, tangguh = [], [], []
    for d, g in (C[C.tarikh_beli >= PB_MULA].groupby('tarikh_beli') if len(C) else []):
        if d in sudah:
            continue
        if g.data_tiada.any() and sum(1 for x in sesi if x > d) < prm['tangguh_sesi']:
            tangguh.append(d); continue
        lul = g[g.lulus & ~g.data_tiada]
        baru_c.append(lul.assign(dinilai=dinilai).reindex(columns=L_CALON_PB))
        baru_t.append(dict(tarikh_beli=d, calon=len(g), lulus=len(lul), data_tiada=int(g.data_tiada.sum()),
                           **{f'gagal_{k}': int(g[f'gagal_{k}'].sum()) for k in SEBAB_PB}, dinilai=dinilai))
    if baru_t:
        L = pd.concat([x for x in [L] + baru_c if len(x)] or [L], ignore_index=True).reindex(columns=L_CALON_PB)
        T = pd.concat([T, pd.DataFrame(baru_t)], ignore_index=True) if len(T) else pd.DataFrame(baru_t)
        os.makedirs(folder, exist_ok=True)
        L.sort_values(['tarikh_beli', 'saham']).to_csv(pc, index=False, float_format='%.6g')
        T.sort_values('tarikh_beli').to_csv(pt, index=False)
        L = baca()                     # larian pertama = larian seterusnya (nilai seperti dalam rekod beku)
    return L, T, tangguh


def pool_pb(L, P, aa_path=AMBIL_ALIH):
    """Calon beku yang masih sah sekarang: masih posisi Lejar (saham, tarikh_beli) dan bukan ambil alih yang diumum <= tarikh
    isyarat; harga beli = Lejar semasa (selepas sebarang pelarasan)."""
    import ambil_alih as AA
    L = L.copy()
    for k in ('r_awal', 'rs', 'harga_beli'):
        L[k] = pd.to_numeric(L[k], errors='coerce') if k in L else pd.Series(dtype=float)
    if L.empty:
        return L
    hb = P.groupby(['tarikh_beli', 'saham']).harga_beli.first().to_dict()
    L = L[[k in hb for k in zip(L.tarikh_beli, L.saham)]].copy()
    umum = {r['saham']: r.get('tarikh_umum', '') for r in AA.baca_senarai(aa_path)}
    L = L[[not (bool(umum.get(t)) and umum[t] <= d) for t, d in zip(L.saham, L.tarikh_isyarat)]].copy()
    L['harga_beli'] = [float(hb[k]) for k in zip(L.tarikh_beli, L.saham)]
    return L.reset_index(drop=True)


# ---------------------------------------------------------------- perincian risiko setiap posisi (semua portfolio)
def paras_chandelier(sr, k):
    """Paras lorong 2 semasa (keluar_lorong.lorong_henti) bagi posisi dibeli pada bar k: max(puncak tutup − 4 × ATR14), naik."""
    puncak = pv = -np.inf
    for j in range(k, len(sr.c)):
        puncak = max(puncak, sr.c[j])
        if np.isfinite(sr.a[j]):
            pv = max(pv, puncak - KL.GANDA_ATR * sr.a[j])
    return pv if np.isfinite(pv) else np.nan


def perinci(R, E, harga, peta=None):
    """Tambah lajur L_PERINCI pada posisi R. Paras keluar posisi dipegang: paras enjin (PLAYBOOK), henti kaedah Lejar (lorong
    kaedah) atau Chandelier lorong 2 (lorong henti). risiko_pct = nilai x max(0, jarak) / ekuiti; tiada paras = nilai penuh."""
    R = R.copy(); peta = peta_industri() if peta is None else peta
    eq = float(E.ekuiti.iloc[-1]) if len(E) else 1.0; akhir = E.tarikh.iloc[-1] if len(E) else ''
    for k in L_PERINCI:
        if k not in R:
            R[k] = np.nan
    R['industri_us'] = [peta.get(t, ('', ''))[0] for t in R.saham]; R['sektor_us'] = [peta.get(t, ('', ''))[1] for t in R.saham]
    for i, r in R.iterrows():
        sr = harga.get(r.saham)
        tk = r.tarikh_keluar if r.status == 'Keluar' and isinstance(r.tarikh_keluar, str) and r.tarikh_keluar else akhir
        if sr is not None:
            R.at[i, 'hari'] = sum(1 for x in sr.t if r.tarikh_beli <= x <= tk)
        if r.status != 'Pegang':
            continue
        c = r.harga_terkini
        nilai = r.amaun * c / r.harga_beli if pd.notna(c) and pd.notna(r.amaun) else np.nan
        R.at[i, 'nilai_semasa'] = nilai
        if r.lorong == 'playbook':
            paras = r.paras_keluar
        elif r.lorong == 'kaedah':
            paras = pd.to_numeric(r.get('henti'), errors='coerce')
        else:
            paras = paras_chandelier(sr, sr.ix[r.tarikh_beli]) if sr is not None and r.tarikh_beli in sr.ix else np.nan
        R.at[i, 'paras_keluar'] = paras
        if pd.notna(paras) and pd.notna(c) and c > 0:
            jr = (c - paras) / c; R.at[i, 'jarak_pct'] = 100 * jr
            a = sr.a[-1] if sr is not None else np.nan
            R.at[i, 'jarak_atr'] = (c - paras) / a if np.isfinite(a) and a > 0 else np.nan
            R.at[i, 'risiko_pct'] = 100 * nilai * min(1.0, max(0.0, jr)) / eq if pd.notna(nilai) else np.nan
        elif pd.notna(nilai):
            R.at[i, 'risiko_pct'] = 100 * nilai / eq
    return R


def ringkas_risiko(R, E):
    """dict tunai_pct, heat_pct (= Σ risiko_pct posisi dipegang), sektor {sektor_us: bil dipegang}, bawah_puncak_sesi (sesi
    sejak puncak ekuiti terakhir; 0 = di puncak) bagi posisi (selepas perinci) + ekuiti."""
    if not len(E):
        return dict(tunai_pct=100.0, heat_pct=0.0, sektor={}, bawah_puncak_sesi=0)
    H = R[R.status == 'Pegang']; x = np.r_[1.0, E.ekuiti.to_numpy(float)]
    pk = int(np.flatnonzero(x >= np.maximum.accumulate(x) - 1e-12)[-1])
    return dict(tunai_pct=round(100 * float(E.tunai.iloc[-1]) / float(x[-1]), 2),
                heat_pct=round(float(pd.to_numeric(H.risiko_pct, errors='coerce').fillna(0).sum()), 2),
                sektor={k: int(v) for k, v in H.sektor_us.fillna('').replace('', 'Tiada').value_counts().items()},
                bawah_puncak_sesi=len(x) - 1 - pk)


def _f(x, f='{:+.2f}'):
    return '' if x is None or pd.isna(x) else f.format(x)


def ringkasan(hasil, spy_mula, spy_akhir, hari, CFG=None, pb=None):
    """RINGKASAN.md. pb: dict(tapis, tangguh, bunuh {jenis: tarikh}) bagi PLAYBOOK_10 / RAWAK_PADAN_10 (None = tiada)."""
    L = [f'# Portfolio maya (jejak hadapan; rekod sahaja)', '',
         'Dibina semula daripada Lejar Penuh oleh `standard/portfolio_slot.py`; kajian `kajian/KAJIAN_PORTFOLIO.md`. '
         'Tiada order, tiada wang sebenar. Jangan ubah secara manual.', '',
         f'Tempoh: {hari[0] if hari else "-"} hingga {hari[-1] if hari else "-"} ({len(hari)} sesi). '
         f'SPY dalam tempoh sama: {100 * (spy_akhir / spy_mula - 1):+.2f}%.' if spy_mula else 'SPY: tiada data.', '',
         '| Portfolio | Pulangan % | MDD % | Posisi dipegang | Dagangan keluar | Kadar menang % | Purata untung keluar % |',
         '|---|---|---|---|---|---|---|']
    for k, (R, E) in hasil.items():
        k_ = R[R.status == 'Keluar']; ret = 100 * (E.ekuiti.iloc[-1] - 1) if len(E) else 0.0
        L.append(f'| {k} — {PORTFOLIO[k]} | {ret:+.2f} | {100 * mdd(E.ekuiti):.2f} | {(R.status == "Pegang").sum()} | {len(k_)} | '
                 + (f'{100 * (k_.untung_pct > 0).mean():.0f} | {k_.untung_pct.mean():+.2f} |' if len(k_) else '– | – |'))
    L += ['', '## Risiko semasa (tutup sesi terakhir)', '',
          'Heat = Σ nilai × jarak ke paras keluar ÷ ekuiti (posisi tanpa paras keluar = nilai penuh). Paras: Chandelier 4×ATR14 '
          '(lorong 2 / PLAYBOOK) atau henti kaedah (lorong kaedah).', '',
          '| Portfolio | Tunai % | Heat % | Sesi di bawah puncak | Sektor terbanyak (bil.) |', '|---|---|---|---|---|']
    for k, (R, E) in hasil.items():
        x = ringkas_risiko(R, E); sk = sorted(x['sektor'].items(), key=lambda v: -v[1])
        L.append(f"| {k} | {x['tunai_pct']:.1f} | {x['heat_pct']:.1f} | {x['bawah_puncak_sesi']} | "
                 + (', '.join(f'{a} {b}' for a, b in sk[:3]) or '–') + ' |')
    for k, (R, _) in hasil.items():
        H = R[R.status == 'Pegang']
        L += ['', f'## {k} — posisi dipegang', '',
              '| Saham | Kaedah | RS | Beli | Harga beli | Terkini | Untung % | Paras keluar | Jarak ATR | Risiko % ekuiti | Sektor |',
              '|---|---|---|---|---|---|---|---|---|---|---|']
        for r in H.itertuples():
            km = str(r.id_kaedah).split(','); km = ','.join(km[:3]) + (f' (+{len(km) - 3})' if len(km) > 3 else '')
            L.append(f'| {r.saham} | {km} | {"" if pd.isna(r.rs) else int(r.rs)} | {r.tarikh_beli} | {r.harga_beli:.2f} | '
                     f'{_f(r.harga_terkini, "{:.2f}")} | {_f(r.untung_semasa_pct)} | {_f(r.paras_keluar, "{:.2f}")} | '
                     f'{_f(r.jarak_atr, "{:.1f}")} | {_f(r.risiko_pct, "{:.2f}")} | {r.sektor_us or "–"} |')
    if CFG:
        L += ['', '## Gabungan beku (jejak hadapan sejak ' + next(iter(CFG.values()))['mula'] + '; data/analisis/gabungan_beku.json)', '',
              '| Portfolio | Kaedah (slot, lorong) | Sesi | Pulangan % | SPY tempoh sama % |', '|---|---|---|---|---|']
        for k, c in CFG.items():
            R, E = hasil.get(k, (None, pd.DataFrame()))
            kl = ', '.join('%s (%s, %s)' % (i, n, c['lorong'][i]) for i, n in c['kuota'].items())   # serasi Python 3.11
            L.append(f"| {k} | {kl} | {len(E)} | "
                     + (f"{100 * (E.ekuiti.iloc[-1] - 1):+.2f} | {100 * (E.spy.iloc[-1] - 1):+.2f} |" if len(E) else '– | – |'))
    if pb is not None:
        L += ['', f'## Rangka risiko: PLAYBOOK_10 lawan RAWAK_PADAN_10 (pra-daftar 25 Okt 2026; jejak sejak {PB_MULA})', '',
              'Peraturan: `kajian/portfolio/PRA_DAFTAR_PLAYBOOK.md`. Calon = posisi Lejar yang lulus P1–P11; saiz risiko 1% ekuiti ke '
              'paras Chandelier awal (had 15%), heat ≤ 10%, ≤ 20 posisi, ≤ 3 sektor / ≤ 2 industri, ≤ 3 belian sehari; keluar '
              'Chandelier 4×ATR14 + henti masa bar ke-20 (< +1R); brek 15% (pulih −10%), kill_switch 25%; kos 0.25% setiap belah. '
              f'Sesi hingga {PB_PRA_DAFTAR} dibina semula selepas berlaku; tempoh hadapan bersih bermula sesi selepasnya.', '',
              '| Portfolio | Sesi | Pulangan % | Sejak pra-daftar % | Heat % | Brek | kill_switch |', '|---|---|---|---|---|---|---|']
        for k in PB_JENIS:
            if k not in hasil:
                continue
            R, E = hasil[k]; e0 = E.ekuiti[E.tarikh <= PB_PRA_DAFTAR]
            sp = 100 * (E.ekuiti.iloc[-1] / e0.iloc[-1] - 1) if len(e0) and len(E) else None
            L.append(f"| {k} | {len(E)} | {_f(100 * (E.ekuiti.iloc[-1] - 1) if len(E) else None)} | {_f(sp)} | "
                     f"{ringkas_risiko(R, E)['heat_pct']:.1f} | {'ya' if len(E) and E.brek.iloc[-1] else 'tidak'} | "
                     f"{pb['bunuh'].get(k) or 'tidak'} |")
        T = pb['tapis']
        if len(T):
            L += ['', 'Corong penapis (rekod beku `PLAYBOOK_tapis.csv`; gagal tidak eksklusif), 10 sesi beli terakhir:', '',
                  '| Sesi beli | Calon | Lulus | ' + ' | '.join(SEBAB_PB) + ' |', '|---|---|---|' + '---|' * len(SEBAB_PB)]
            for r in T.sort_values('tarikh_beli').tail(10).to_dict('records'):
                L.append(f"| {r['tarikh_beli']} | {int(r['calon'])} | {int(r['lulus'])} | "
                         + ' | '.join(str(int(r.get(f'gagal_{s}', 0))) for s in SEBAB_PB) + ' |')
        if pb['tangguh']:
            L += ['', 'Sesi beli ditangguh (sumber RS / gred industri belum ada bagi tarikh isyarat): ' + ', '.join(pb['tangguh']) + '.']
        L += ['', 'Amaran kajian dalam sampel (KAJIAN_PORTFOLIO.md, 25 Okt 2026): brek 15% seperti didaftar menjadi kekal apabila '
              'tercetus — tanpa belian baharu, ekuiti tunai tidak boleh pulih ke −10% selepas posisi sedia ada keluar (20/20 benih '
              'dalam sampel berhenti antara 2021 dan 2024). Peraturan tidak diubah; keputusan pengguna diperlukan.']
    L += ['', 'Isu diketahui RS_10 (eksperimen beku, tidak diubah): RS ialah integer, jadi seri kerap; susunan stabil atas calon yang '
          'diisih ikut saham menyebabkan seri dipecah ikut ABJAD saham, dan semua 10 slot diisi pada sesi pertama (16 Okt 2026). '
          'PLAYBOOK_10 memecah seri secara rawak berbenih dan menghadkan 3 belian sehari.',
          '', 'Penilaian adil memerlukan sekurang-kurangnya 6–12 bulan (KAJIAN_PORTFOLIO.md). Kelebihan yang dicari: RS_10 mengatasi '
          'RAWAK_10 dan SPY dengan MDD yang setanding; GABUNGAN_10 mengatasi TOP1_10, RAWAK_KAEDAH_10 dan SPY; PLAYBOOK_10 '
          'mengatasi RAWAK_PADAN_10 (nilai pemilihan) dengan MDD lebih kecil daripada RS_10 (nilai rangka risiko).']
    return '\n'.join(L) + '\n'


def main():
    P = calon_lejar()
    fr, idx = frames_dict(muat(STOR))
    if 'SPY' not in idx or P.empty:
        print('tiada calon lejar atau SPY: portfolio tidak dibina'); return 0
    spy = idx['SPY'].close
    hari = [d.strftime('%Y-%m-%d') for d in spy.index if d.strftime('%Y-%m-%d') >= P.tarikh_beli.min()]
    cl = {t: g.close for t, g in fr.items()}

    def tutup(s, d):
        c = cl.get(s)
        if c is None: return None
        v = c.asof(pd.Timestamp(d)); return float(v) if pd.notna(v) and v > 0 else None

    harga = {}

    def siri(t):
        if t not in harga and t in fr:
            harga[t] = Siri(fr[t])
        return harga.get(t)

    os.makedirs(KELUAR, exist_ok=True); hasil = {}; peta = peta_industri()
    s0 = float(idx['SPY'].open.asof(pd.Timestamp(hari[0]))) if hari else None   # belian pertama pada buka
    CFG = konfigurasi(muat_json(BEKU))
    GT = log_gantung(CFG, hari[-1] if hari else None)
    pb = None
    for k in PORTFOLIO:
        if k in PB_JENIS:
            if pb is None:
                pt = os.path.join(KELUAR, 'PLAYBOOK_tapis.csv')
                sudah = set(pd.read_csv(pt, dtype={'tarikh_beli': str}).tarikh_beli) if os.path.exists(pt) else set()
                C = calon_pb(P[(P.tarikh_beli >= PB_MULA) & ~P.tarikh_beli.isin(sudah)], fr, idx, peta=peta)
                L, T, tangguh = log_pb(C, [d.strftime('%Y-%m-%d') for d in spy.index])
                pb = dict(pool=pool_pb(L, P), tapis=T, tangguh=tangguh, bunuh={})
                for t in pb['pool'].saham.unique():
                    siri(t)
            R, E = bina_pb(pb['pool'], [d for d in hari if d >= PB_MULA], harga, k); pb['bunuh'][k] = bina_pb.bunuh
        else:
            if k in BEKU_JENIS and k not in CFG:
                continue
            R, E = bina(P, k, hari, tutup, CFG.get(k), GT)
        a = float(idx['SPY'].open.asof(pd.Timestamp(E.tarikh.iloc[0]))) if len(E) else None   # SPY tempoh sama (buka hari pertama)
        E['spy'] = [float(spy.asof(pd.Timestamp(d))) / a for d in E.tarikh] if a else np.nan
        for t in R.saham.unique():
            siri(t)
        R = perinci(R, E, harga, peta)
        R.to_csv(os.path.join(KELUAR, f'{k}_posisi.csv'), index=False, float_format='%.4f')
        E.to_csv(os.path.join(KELUAR, f'{k}_ekuiti.csv'), index=False, float_format='%.6f')
        hasil[k] = (R, E)
    s1 = float(spy.asof(pd.Timestamp(hari[-1]))) if hari else None
    open(os.path.join(KELUAR, 'RINGKASAN.md'), 'w').write(ringkasan(hasil, s0, s1, hari, CFG, pb))
    st = {}
    for k, (R, E) in hasil.items():
        st[k] = dict(sesi_terakhir=E.tarikh.iloc[-1] if len(E) else None, ekuiti=round(float(E.ekuiti.iloc[-1]), 6) if len(E) else 1.0,
                     dipegang=int((R.status == 'Pegang').sum()), keluar=int((R.status == 'Keluar').sum()))
        x = ringkas_risiko(R, E); st[k].update(tunai_pct=x['tunai_pct'], heat_pct=x['heat_pct'], bawah_puncak_sesi=x['bawah_puncak_sesi'])
        if k in PB_JENIS:
            st[k].update(brek=bool(len(E) and E.brek.iloc[-1]), kill_switch=pb['bunuh'].get(k) or None, tangguh=pb['tangguh'])
    json.dump(st, open(os.path.join(KELUAR, 'status.json'), 'w'), indent=1)
    for k, (R, E) in hasil.items():
        print(k, 'ekuiti %.4f' % (E.ekuiti.iloc[-1] if len(E) else 1.0), 'dipegang', (R.status == 'Pegang').sum(),
              'keluar', (R.status == 'Keluar').sum(), 'heat %.1f%%' % st[k]['heat_pct'])
    return 0


if __name__ == '__main__':
    sys.exit(main())
