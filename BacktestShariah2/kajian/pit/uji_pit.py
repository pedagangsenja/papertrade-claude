# uji_pit.py — harness ujian semula point-in-time pintu B (pra-daftar BacktestShariah2/kajian/pit/PRA_DAFTAR.md).
#
#   python3 BacktestShariah2/kajian/pit/uji_pit.py muat  --data DIR           # muat turun Release autotune-data-a02 (gh api)
#   python3 BacktestShariah2/kajian/pit/uji_pit.py bina  --data DIR           # bina cache alam PIT (DIR/pit_cache)
#   python3 BacktestShariah2/kajian/pit/uji_pit.py jalan --data DIR [--kaedah M01 M02 ... | --swing | --semua | --lain]
#                                                       [--modul FAIL.py ...] [--pekerja 3] [--paksa] [--tanpa-gabung]
#   python3 BacktestShariah2/kajian/pit/uji_pit.py gabung --data DIR          # DSR/PBO/pintu B -> ujian_pit.json + LAPORAN.md
#
# Kaedah tambahan (cth. M168 selepas kod/kaedah/M168.py wujud) — satu perintah:
#   python3 BacktestShariah2/kajian/pit/uji_pit.py jalan --data DIR --kaedah M168
# (atau --modul laluan/ke/M168.py). `jalan` membina cache jika tiada dan menjalankan `gabung` di hujung (N DSR bertambah).
# DIR lalai: $PIT_DATA atau ~/.cache/pit_a02. Data harga mentah dan hasil setiap kaedah kekal dalam DIR (bukan repo).
import argparse, importlib.util, json, math, os, sys, time, traceback, warnings
from datetime import datetime, timedelta, timezone

import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
BS2 = os.path.dirname(os.path.dirname(HERE))
KOD = os.path.join(BS2, 'kod')
sys.path.insert(0, HERE)
for p in (os.path.join(KOD, 'kaedah'), KOD):
    if p not in sys.path: sys.path.insert(1, p)
import alam as AL          # noqa: E402
import enjin_v13 as EN     # noqa: E402
import statistik as ST     # noqa: E402

MULA = pd.Timestamp('2013-01-02')
POTONG_SUB = pd.Timestamp('2018-12-31')
N_SEJARAH = 633             # varian set 431 dalam data/registry_M_gabung.csv (pra-daftar §6)
BENIH = range(20)
VERSI = ('A', 'B', 'K431')
JSON_KELUAR = os.path.join(BS2, 'data', 'analisis', 'ujian_pit.json')
PENYINTAS = os.path.join(HERE, 'penyintas_sp500.json')
# Penyimpangan daripada pra-daftar (dikemas kini jika ada; dicetak dalam LAPORAN.md §8)
PENYIMPANGAN = []
LAPORAN = os.path.join(HERE, 'LAPORAN.md')
PRA = 'BacktestShariah2/kajian/pit/PRA_DAFTAR.md'
warnings.filterwarnings('ignore')


def data_lalai():
    return os.environ.get('PIT_DATA') or os.path.expanduser('~/.cache/pit_a02')


def senarai_kaedah():
    return sorted([f[:-3] for f in os.listdir(os.path.join(KOD, 'kaedah')) if f.startswith('M') and f.endswith('.py')],
                  key=lambda x: int(x[1:]))


def senarai_swing():
    with open(os.path.join(BS2, 'data', 'analisis', 'papan.json'), encoding='utf-8') as f:
        p = json.load(f)
    return [r['id'] for r in p['rows'] if r.get('swing')]


def muat_modul(kunci):
    """kunci: ID (kod/kaedah/<ID>.py), 'PLAYBOOK', atau laluan fail .py. Pulang (id, modul, laluan)."""
    if kunci.upper() == 'PLAYBOOK':
        path = os.path.join(HERE, 'playbook.py')
    elif kunci.endswith('.py'):
        path = os.path.abspath(kunci)
    else:
        path = os.path.join(KOD, 'kaedah', f'{kunci}.py')
    nama = 'pit_' + os.path.basename(path)[:-3]
    sp = importlib.util.spec_from_file_location(nama, path)
    m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m)
    return getattr(m, 'ID', os.path.basename(path)[:-3]), m, path


# ---------------------------------------------------------------- metrik
def _ringkas_dagangan(T):
    if len(T) == 0: return dict(n=0)
    w = T.ret > 0
    return dict(n=int(len(T)), menang=round(float(w.mean()), 4), purata=round(float(T.ret.mean()), 5),
                median=round(float(T.ret.median()), 5), hari=round(float(T.days.mean()), 2),
                sebab={k: int(v) for k, v in T.why.value_counts().items()})


def _tahunan(s):
    y = s.resample('YE').last(); base = pd.concat([pd.Series([s.iloc[0]], index=[s.index[0] - pd.Timedelta(days=1)]), y])
    r = base.pct_change().dropna()
    return {str(k.year): round(float(v), 4) for k, v in r.items()}


def _bulat(d, n=5):
    if isinstance(d, dict): return {k: _bulat(v, n) for k, v in d.items()}
    if isinstance(d, list): return [_bulat(v, n) for v in d]
    if isinstance(d, (float, np.floating)):
        return None if (math.isnan(d) or math.isinf(d)) else round(float(d), n)
    if isinstance(d, (np.integer,)): return int(d)
    if isinstance(d, (np.bool_,)): return bool(d)
    return d


def nilai_versi(A, fr, s0, M, versi, spy_atas):
    """Jalankan enjin v1.3 + penanda aras bagi satu versi alam. Pulang (dict metrik, Series pulangan harian portfolio)."""
    tv = [t for t in fr if A.M[versi][:, A.col[t]].any()]
    frv = {t: fr[t] for t in tv}
    sg = {t: s0[t] & A.topeng(versi, t) for t in tv}
    out = dict(n_ticker_isyarat=0)
    if not frv:
        return dict(n_isyarat=0, n_dagangan=0), None, None
    T = EN.trades(frv, tmax=M.TMAX, warm=M.WARM, akhir_data=A.akhir_data, sig=sg)
    Ta = T[T.ent >= MULA].copy()
    out['n_ticker_isyarat'] = int(Ta.ticker.nunique()) if len(Ta) else 0
    # penanda aras rawak tempoh sama (semua isyarat)
    rr = ST.rawak(Ta, A.O, A.Cf, A.M[versi], A.tarikh, benih=BENIH, kos=EN.COST) if len(Ta) else np.array([])
    x = pd.Series(Ta.ret.values - rr, index=Ta.index) if len(Ta) else pd.Series(dtype=float)
    bln = Ta.ent.dt.to_period('M').astype(str).values if len(Ta) else np.array([])
    tb = ST.t_berkelompok(x.values, bln)
    out.update(n_isyarat=int(len(Ta)), lebihan_rawak=tb['purata'], t_rawak=tb['t'], se_rawak=tb['se'], bulan=tb['G'],
               purata_rawak=float(np.nanmean(rr)) if len(rr) else float('nan'), isyarat=_ringkas_dagangan(Ta))
    if len(Ta):
        out['jurang_b1'] = int(((Ta.why == 'henti') & (Ta.days == 1) & (Ta.jenis == 'buka')).sum())
        reg = spy_atas.reindex(pd.DatetimeIndex(Ta.sig)).values
        rj = {}
        for nm, m in (('spy_atas_sma200', reg == True), ('spy_bawah_sma200', reg == False)):   # noqa: E712
            t2 = ST.t_berkelompok(x.values[m], bln[m]); rj[nm] = dict(n=t2['n'], lebihan_rawak=t2['purata'], t=t2['t'])
        out['rejim_isyarat'] = rj
        out['tahunan_lebihan_rawak'] = {str(k): float(v) for k, v in x.groupby(Ta.ent.dt.year.values).mean().items()}
    # portfolio 8 slot
    if len(Ta) == 0:
        return out, None, x
    cv, P = EN.portfolio(T, frv, mula=MULA, pulang_dagangan=True)
    out['n_dagangan'] = int(len(P)); out['portfolio'] = _ringkas_dagangan(P)
    out['cagr'] = ST.cagr(cv); out['mdd'] = ST.mdd(cv)
    if len(P):
        xp = x.reindex(P.index); tp = ST.t_berkelompok(xp.values, P.ent.dt.to_period('M').astype(str).values)
        out['lebihan_rawak_portfolio'] = tp['purata']; out['t_rawak_portfolio'] = tp['t']
        P10 = P.drop(columns='a').copy(); top = P10.ret.nlargest(min(10, len(P10))).index; P10.loc[top, 'ret'] = 0.0
        cv10, P10b = EN.portfolio(P10, frv, mula=MULA, pulang_dagangan=True)
        out['cagr_tanpa10'] = ST.cagr(cv10); out['tanpa10_sama_slot'] = bool(len(P10b) == len(P))
        out['tanpa10_ret_dibuang'] = [round(float(v), 4) for v in P.ret.loc[top].values]
    ew_r = A.EW[versi].reindex(cv.index).fillna(0.0); ew_r.iloc[0] = 0.0
    ew = (1 + ew_r).cumprod()
    out['ew_cagr'] = ST.cagr(ew); out['ew_mdd'] = ST.mdd(ew)
    out['lebihan_ew'] = out['cagr'] - out['ew_cagr']
    out['tahunan'] = _tahunan(cv); out['tahunan_ew'] = _tahunan(ew)
    sub = {}
    for nm, a, b in (('2013_2018', MULA, POTONG_SUB), ('2019_2026', POTONG_SUB + pd.Timedelta(days=1), cv.index[-1])):
        c1, e1 = cv[(cv.index >= a) & (cv.index <= b)], ew[(ew.index >= a) & (ew.index <= b)]
        sub[nm] = dict(cagr=ST.cagr(c1), ew_cagr=ST.cagr(e1), mdd=ST.mdd(c1))
    out['subtempoh'] = sub
    rp = cv.pct_change().fillna(0.0)
    reg_d = spy_atas.reindex(cv.index).shift(1)
    out['rejim_harian'] = {nm: dict(hari=int(m.sum()), tahunan_portfolio=float(rp[m].mean() * 252),
                                     tahunan_ew=float(ew_r[m].mean() * 252))
                           for nm, m in (('spy_atas_sma200', reg_d == True), ('spy_bawah_sma200', reg_d == False))}  # noqa
    if versi == 'A':
        out['sr_lebihan_harian'] = ST.sharpe(rp - ew_r)
    return out, rp, x


def jalan_satu(A, kunci, keluar):
    mid, M, path = muat_modul(kunci)
    t0 = time.time()
    tick = A.tickers('sektor')
    fr = {t: A.fr[t].copy() for t in tick}
    idx = {k: v.copy() for k, v in A.idx.items()}
    if getattr(M, 'PERLU_RS', False):
        idx['_rs'] = pd.DataFrame(A.RS, index=A.tarikh, columns=A.tik)
        idx['_rs_skor'] = pd.DataFrame(A.SK, index=A.tarikh, columns=A.tik)
    M.sedia(fr, idx)
    t1 = time.time()
    s0 = {}
    for t, g in fr.items():
        EN.siap(g); s0[t] = g['sig'].fillna(False).astype(bool).values.copy()
    spy = A.idx['SPY'].close; spy_atas = (spy > spy.rolling(200).mean()).where(spy.rolling(200).count() >= 200)
    hasil = dict(id=mid, nama=getattr(M, 'NAMA', ''), varian=getattr(M, 'VARIAN', ''), tmax=getattr(M, 'TMAX', None),
                 warm=getattr(M, 'WARM', None), silang=bool(getattr(M, 'SILANG', False)), modul=os.path.relpath(path, BS2),
                 versi={})
    harian = {}
    for v in VERSI:
        o, rp, _ = nilai_versi(A, fr, s0, M, v, spy_atas)
        hasil['versi'][v] = _bulat(o, 6)
        if rp is not None: harian[v] = rp
    # diagnostik v1.2-setara (kos 0.1%, tanpa [B1]) atas versi A
    frA = {t: fr[t] for t in fr if A.M['A'][:, A.col[t]].any()}
    sgA = {t: s0[t] & A.topeng('A', t) for t in frA}
    T12 = EN.trades(frA, tmax=M.TMAX, warm=M.WARM, kos=EN.COST_V12, jurang=False, sig=sgA)
    if len(T12[T12.ent >= MULA]):
        cv12 = EN.portfolio(T12, frA, mula=MULA)
        hasil['v12_setara'] = _bulat(dict(cagr=ST.cagr(cv12), mdd=ST.mdd(cv12), n_isyarat=int((T12.ent >= MULA).sum())), 6)
    hasil['masa_sedia_s'] = round(t1 - t0, 1); hasil['masa_jumlah_s'] = round(time.time() - t0, 1)
    os.makedirs(keluar, exist_ok=True)
    if harian:
        H = pd.DataFrame(harian); H['ew_A'] = A.EW['A'].reindex(H.index)
        H.to_pickle(os.path.join(keluar, f'{mid}_harian.pkl'))
    sem = os.path.join(keluar, f'.{mid}.json.tmp')
    with open(sem, 'w') as f:
        json.dump(hasil, f, ensure_ascii=False)
    os.replace(sem, os.path.join(keluar, f'{mid}.json'))      # tulis atomik: JSON wujud = keputusan lengkap
    return mid, hasil['masa_jumlah_s']


_ALAM = None


def _pekerja(args):
    kunci, keluar = args
    try:
        mid, s = jalan_satu(_ALAM, kunci, keluar)
        return kunci, f'siap {s:.0f}s'
    except Exception as e:  # rekod ralat; kaedah lain diteruskan
        with open(os.path.join(keluar, f'_ralat_{os.path.basename(kunci)}.txt'), 'w') as f:
            f.write(traceback.format_exc())
        return kunci, f'RALAT {type(e).__name__}: {e}'


def jalan(data, kunci, pekerja=1, paksa=False, log=print):
    global _ALAM
    keluar = os.path.join(data, 'hasil_pit')
    if not os.path.exists(os.path.join(data, 'pit_cache', 'meta.json')):
        AL.bina_cache(data, log=log)
    tugas = []
    for k in kunci:
        nm = 'PLAYBOOK' if k.upper() == 'PLAYBOOK' else os.path.basename(k)[:-3] if k.endswith('.py') else k
        if not paksa and os.path.exists(os.path.join(keluar, f'{nm}.json')): continue
        tugas.append((k, keluar))
    log(f'{len(tugas)} kaedah untuk dijalankan ({len(kunci) - len(tugas)} sudah siap)')
    if not tugas: return
    _ALAM = AL.Alam(data)
    if pekerja <= 1:
        for t in tugas:
            log(*_pekerja(t))
    else:
        import multiprocessing as mp
        with mp.get_context('fork').Pool(pekerja, maxtasksperchild=4) as pool:
            for k, s in pool.imap_unordered(_pekerja, tugas):
                log(k, s, flush=True)


# ---------------------------------------------------------------- gabung
def rujukan_431():
    """{id: dict(cagr, mdd, n, ew_cagr, keputusan)} varian aktif set 431 (cara standard/registry_aktif.py)."""
    with open(os.path.join(BS2, 'standard', 'katalog_kaedah.json'), encoding='utf-8') as f:
        kat = {r['id']: r.get('varian_kod') or r.get('varian') for r in json.load(f)['rows']}
    r = pd.read_csv(os.path.join(BS2, 'data', 'registry_M_gabung.csv'), dtype={'set': str})
    r = r[(r['set'] == '431').values & np.array([kat.get(i) == v for i, v in zip(r['id'], r['varian'])], bool)]
    out = {}
    for x in r.to_dict('records'):
        out[x['id']] = dict(cagr=x.get('cagr'), mdd=x.get('mdd'), n=x.get('n'), ew_cagr=x.get('ew_cagr'), keputusan=x.get('keputusan'),
                            days=x.get('days'))
    return out


def pintu_b(v, dsr):
    s = []
    if (v.get('n_dagangan') or 0) < 30 or (v.get('bulan') or 0) < 24: s.append('B0 data tidak cukup')
    lr, tr = v.get('lebihan_rawak'), v.get('t_rawak')
    if lr is None or tr is None or not (lr > 0 and tr >= 3): s.append('B1 lebihan rawak (t<3 atau <=0)')
    c, e, c10 = v.get('cagr'), v.get('ew_cagr'), v.get('cagr_tanpa10')
    if c is None or e is None or not c > e: s.append('B2 CAGR <= EW')
    if dsr is None or not dsr >= 0.5: s.append('B3 DSR < 0.5')
    if c10 is None or e is None or not c10 > e: s.append('B4 tanpa 10 terbaik <= EW')
    return (len(s) == 0), s


def gabung(data, log=print):
    keluar = os.path.join(data, 'hasil_pit')
    fs = sorted(f for f in os.listdir(keluar) if f.endswith('.json'))
    H = {}
    for f in fs:
        try:
            with open(os.path.join(keluar, f), encoding='utf-8') as fh:
                H[f[:-5]] = json.load(fh)
        except (json.JSONDecodeError, OSError):   # fail sedang ditulis oleh pekerja lain
            continue
    ralat = sorted(f[7:-4] for f in os.listdir(keluar) if f.startswith('_ralat_'))
    ralat = [r for r in ralat if r not in H]
    # DSR: V = varians SR lebihan harian versi A merentas kaedah; N = 633 + K
    sr = {k: h['versi']['A'].get('sr_lebihan_harian') for k, h in H.items()}
    srv = np.array([x for x in sr.values() if x is not None and not math.isnan(x)])
    K = len(H); N = N_SEJARAH + K
    V = float(np.var(srv, ddof=1)) if len(srv) > 1 else float('nan')
    s0 = ST.sr0(V, N)
    harian = {}
    for k in H:
        p = os.path.join(keluar, f'{k}_harian.pkl')
        if os.path.exists(p):
            x = pd.read_pickle(p)
            if 'A' in x:
                e = x['ew_A'].fillna(0.0).copy(); e.iloc[0] = 0.0          # sama dengan nilai_versi (hari pertama = 0)
                harian[k] = x['A'] - e
    dsr = {k: (ST.dsr(harian[k], s0) if k in harian else None) for k in H}
    # PBO set (CSCV 16 blok)
    pbo = dict(pbo=None)
    if len(harian) >= 2:
        R = pd.DataFrame(harian).fillna(0.0)
        pbo = ST.pbo_cscv(R.values, S=16); pbo['K'] = R.shape[1]; pbo['T'] = R.shape[0]
    ref = rujukan_431()
    swing = set(senarai_swing())
    with open(os.path.join(data, 'pit_cache', 'meta.json')) as f:
        am = json.load(f)
    kaedah = {}
    for k in sorted(H, key=lambda x: (x[0] != 'M', int(x[1:]) if x[1:].isdigit() else 0, x)):
        h = H[k]; a = h['versi']['A']; d = dsr[k]
        lulus, sebab = pintu_b(a, d)
        rv = ref.get(k, {})
        kaedah[k] = _bulat(dict(
            lulus_B=lulus, lebihan_rawak=a.get('lebihan_rawak'), t_rawak=a.get('t_rawak'), lebihan_ew=a.get('lebihan_ew'),
            cagr=a.get('cagr'), mdd=a.get('mdd'), cagr_tanpa10=a.get('cagr_tanpa10'), ew_cagr=a.get('ew_cagr'), dsr=d, pbo=None,
            n_dagangan=a.get('n_dagangan'), n_isyarat=a.get('n_isyarat'), sebab_gagal=sebab, nama=h.get('nama'),
            varian=h.get('varian'), swing=k in swing or k == 'PLAYBOOK',
            lebihan_rawak_portfolio=a.get('lebihan_rawak_portfolio'), t_rawak_portfolio=a.get('t_rawak_portfolio'),
            jurang_b1=a.get('jurang_b1'), portfolio=a.get('portfolio'), isyarat=a.get('isyarat'),
            tahunan=a.get('tahunan'), tahunan_ew=a.get('tahunan_ew'), subtempoh=a.get('subtempoh'),
            rejim_isyarat=a.get('rejim_isyarat'), rejim_harian=a.get('rejim_harian'),
            versi_B={x: h['versi']['B'].get(x) for x in ('lebihan_rawak', 't_rawak', 'cagr', 'mdd', 'ew_cagr', 'cagr_tanpa10',
                                                          'n_dagangan', 'n_isyarat')},
            k431={x: h['versi']['K431'].get(x) for x in ('lebihan_rawak', 't_rawak', 'cagr', 'mdd', 'ew_cagr', 'n_dagangan')},
            v12_setara=h.get('v12_setara'),
            bt431=dict(cagr=rv.get('cagr'), mdd=rv.get('mdd'), n=rv.get('n'), ew_cagr=rv.get('ew_cagr'),
                       keputusan=rv.get('keputusan'), hari=rv.get('days')) if rv else None,
        ), 5)
    # penanda aras (EW setiap versi dan SPY) atas tarikh yang sama dengan keluk portfolio
    EWd = pd.read_pickle(os.path.join(data, 'pit_cache', 'ew.pkl'))
    EWd = EWd[EWd.index >= MULA]
    penanda = {}
    for v in VERSI:
        r = EWd[v].fillna(0.0).copy(); r.iloc[0] = 0.0; e = (1 + r).cumprod()
        penanda['ew_' + v] = dict(cagr=ST.cagr(e), mdd=ST.mdd(e), tahunan=_tahunan(e))
    ix = pd.read_parquet(os.path.join(data, 'idx.parquet'))
    spy = ix[ix.ticker == 'SPY'].set_index('date').close.astype(float)
    spy = spy[(spy.index >= MULA) & (spy.index <= EWd.index[-1])]
    penanda['spy'] = dict(cagr=ST.cagr(spy), mdd=ST.mdd(spy), tahunan=_tahunan(spy))
    penyintas = None
    if os.path.exists(PENYINTAS):
        with open(PENYINTAS, encoding='utf-8') as f:
            penyintas = {k: v for k, v in json.load(f).items() if k != 'senarai_tiada'}
    semua = set(senarai_kaedah()) | {'PLAYBOOK'}
    belum = sorted(semua - set(H), key=lambda x: (x[0] != 'M', int(x[1:]) if x[1:].isdigit() else 0))
    dibina = datetime.now(timezone(timedelta(hours=8))).strftime('%Y-%m-%d %H:%M MYT')
    J = dict(
        dibina=dibina, pra_daftar=PRA, enjin=EN.ENJIN, kos_sisi=EN.COST, mula=str(MULA.date()), akhir=am['akhir_data'],
        alam=dict(sumber=am['sumber'], ticker_data=am['ticker'], ticker_delist=am['ticker_delist'],
                  ticker_sektor_ok=am['ticker_sektor_ok'], ticker_sektor_kecuali=am['ticker_sektor_kecuali'],
                  pernah_layak=am['pernah_layak'], median_layak_setahun=am['median_layak_setahun'], syarat=am['syarat'],
                  had=['tiada saham delist (calon = senarai tersenarai Okt 2026); hasil = had atas',
                       'nisbah kewangan ikut tarikh tidak tersedia: versi A sektor sahaja, versi B + skrin Shariah semasa',
                       'peta industri semasa digunakan untuk semua tarikh']),
        dsr=_bulat(dict(N=N, N_sejarah=N_SEJARAH, K=K, V_sr_harian=V, sr0_harian=s0,
                        sr0_tahunan=s0 * math.sqrt(252) if s0 == s0 else None), 6),
        pbo_set=_bulat(pbo, 4), penanda=_bulat(penanda, 5), penyintas_sp500=penyintas, penyimpangan=PENYIMPANGAN,
        kiraan=dict(diuji=K, lulus_B=sum(1 for v in kaedah.values() if v['lulus_B']), belum_diuji=belum, ralat=ralat,
                    swing_diuji=sum(1 for v in kaedah.values() if v['swing'])),
        kaedah=kaedah)
    with open(JSON_KELUAR, 'w', encoding='utf-8') as f:
        json.dump(J, f, ensure_ascii=False, separators=(',', ':'))
    import laporan_pit as LP
    LP.tulis(J, am, LAPORAN)
    log(f'gabung: {K} kaedah, lulus B {J["kiraan"]["lulus_B"]}, belum {len(belum)}, ralat {len(ralat)}; N={N}; '
        f'PBO set {pbo.get("pbo")}')
    return J


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('perintah', choices=['muat', 'bina', 'jalan', 'gabung'])
    ap.add_argument('--data', default=data_lalai())
    ap.add_argument('--kaedah', nargs='*', default=[])
    ap.add_argument('--modul', nargs='*', default=[])
    ap.add_argument('--swing', action='store_true', help='75 kaedah swing + PLAYBOOK')
    ap.add_argument('--lain', action='store_true', help='kaedah bukan swing')
    ap.add_argument('--semua', action='store_true')
    ap.add_argument('--pekerja', type=int, default=1)
    ap.add_argument('--paksa', action='store_true')
    ap.add_argument('--tanpa-gabung', action='store_true')
    a = ap.parse_args(argv)
    if a.perintah == 'muat':
        print('\n'.join(AL.muat_release(a.data)))
    elif a.perintah == 'bina':
        AL.bina_cache(a.data)
    elif a.perintah == 'jalan':
        k = list(a.kaedah) + list(a.modul)
        sw = senarai_swing()
        if a.swing or a.semua: k += sw + ['PLAYBOOK']
        if a.lain or a.semua: k += [m for m in senarai_kaedah() if m not in sw]
        k = list(dict.fromkeys(k))
        if not k: ap.error('tiada kaedah: guna --kaedah/--modul/--swing/--lain/--semua')
        jalan(a.data, k, a.pekerja, a.paksa)
        if not a.tanpa_gabung: gabung(a.data)
    else:
        gabung(a.data)


if __name__ == '__main__':
    main()
