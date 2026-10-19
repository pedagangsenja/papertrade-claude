# Ujian luar sampel kajian portfolio 10 slot (19 Okt 2026; laporan kajian/KAJIAN_PORTFOLIO.md, bahagian "Ujian luar sampel").
# Soalan: adakah peraturan pemilihan isyarat (terutama RS pasaran + keluar Chandelier) masih mengatasi pemilihan rawak
# atas saham AS yang BUKAN set 431 (tiada bias pemilihan senarai Shariah hari ini) dan dalam tempoh lebih panjang (2011–2026,
# termasuk 2011–2019 sebelum kaedah-kaedah ini direka)?
# Alam: saham dalam data/skrin/tv_us.csv tolak set 431, tanpa ETF/saham keutamaan/SPAC/waran/unit (lihat BUANG). Data yfinance
# sejak 2009 (auto_adjust=False), SPY dan QQQ untuk `idx`. Calon = dagangan enjin v1.2 134 kaedah; isyarat layak hanya jika
# tutup hari isyarat >= USD10 dan purata nilai dagangan 50 hari >= USD5 juta. Keluar L1 = kaedah, L2 = Chandelier tutup 4xATR14
# paras naik tanpa henti kaedah. Enjin portfolio, metrik, skor walk-forward dan peraturan diimport daripada kaji_portfolio.py.
# Kawalan: `--alam 431` mengulang semuanya atas set 431 dengan data yfinance dan tempoh yang sama (kawalan_431/), supaya
# beza alam luar lawan set 431 tidak dikelirukan oleh beza sumber data atau tempoh.
# Dijalankan oleh GitHub Actions `.github/workflows/kajian_portfolio_luar.yml` (sesi Claude tidak boleh capai Yahoo):
#   python3 kaji_luar.py tarik --keluar <folder>                       -> <folder>/harga.pkl (artifact, tidak dicommit)
#   python3 kaji_luar.py jana  --data <folder>/harga.pkl --alam luar --bahagian i/n --keluar <folder>/T   (matriks; artifact)
#   python3 kaji_luar.py ciri  --data <folder>/harga.pkl --alam luar --dagangan <folder>/T --keluar <folder>   -> calon_luar.pkl
#   python3 kaji_luar.py sim   --data <folder>/harga.pkl --alam luar --calon <folder>/calon_luar.pkl --keluar BacktestShariah2/kajian/portfolio_luar
#   python3 kaji_luar.py ringkas --keluar BacktestShariah2/kajian/portfolio_luar
# Ujian setempat (data set 431 sebagai alam luar): tarik --dataset data_mentah ... ; sim --mula 2020-11-02 --h1 2023-10-31.
import argparse, glob, importlib, json, os, pickle, sys, time
import numpy as np, pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
BS2 = os.path.abspath(os.path.join(HERE, '..', '..'))
AKAR = os.path.dirname(BS2)
KOD = os.path.join(BS2, 'kod')
for p in ('standard', os.path.join('kajian', 'portfolio'), os.path.join('kajian', 'lorong2')):
    sys.path.insert(0, os.path.join(BS2, p))
import kajian_rs                                           # noqa: E402  set_431, bersih, persentil

MULA_DATA = '2009-01-01'
MULA = pd.Timestamp('2011-01-03')                          # portfolio; dagangan 2009–2010 hanya sejarah skor walk-forward
H1_AKHIR = pd.Timestamp('2019-12-31')                      # era 1 = 2011–2019 (sebelum kaedah direka), era 2 = 2020–2026
HARGA_MIN, NILAI_MIN = 10.0, 5e6                           # tutup hari isyarat >= USD10; purata nilai dagangan 50 hari >= USD5 juta
BENIH = 30
BUANG = (r'ETF|\bFund\b|Depositary|Preferred|\bPfd\b|Warrant|\bRights?\b|\bUnits?\b|Acquisition|\bNotes\b|Debenture|SPAC'
         r'|Closed[- ]End|Bond\b')
PILIH = ['Konsensus kaedah', 'RS pasaran', 'RS disahkan dahulu', 'Kaedah walk-forward 12 bulan', 'Momentum 6 bulan',
         'Volatiliti rendah (ATR%)', 'Volatiliti tinggi (ATR%)']
TAHAN = ['RS pasaran', 'Volatiliti tinggi (ATR%)', 'Momentum 6 bulan']


# ---------------------------------------------------------------- 1. alam dan data
def alam():
    tv = pd.read_csv(os.path.join(BS2, 'data', 'skrin', 'tv_us.csv'), usecols=['ticker', 'description']).dropna(subset=['ticker'])
    tv['ticker'] = tv.ticker.astype(str)
    pelik = tv.description.fillna('').str.contains(BUANG, case=False, regex=True) | tv.ticker.str.contains('/', regex=False)
    ok = tv.ticker.str.replace('.', '', regex=False).str.replace('-', '', regex=False).str.isalnum()
    s431 = kajian_rs.set_431()
    luar = sorted(set(tv.ticker[ok & ~pelik]) - s431)
    return luar, sorted(s431), int(pelik.sum())


def cmd_tarik(a):
    os.makedirs(a.keluar, exist_ok=True); f = os.path.join(a.keluar, 'harga.pkl')
    if a.dataset:                                           # ujian setempat: set 431 dijadikan alam
        ix = pd.read_csv(os.path.join(a.dataset, 'index_benchmark.csv'))
        ix['date'] = pd.to_datetime(ix.date.astype(str))
        d = pd.concat([pd.read_csv(g) for g in sorted(glob.glob(os.path.join(a.dataset, 'dataset_S*.csv')))]).drop_duplicates(['ticker', 'date'])
        d['date'] = pd.to_datetime(d.date.astype(str)); d = pd.concat([d, ix])
        p = lambda k: d.pivot(index='date', columns='ticker', values=k).sort_index().astype('float32')
        D = {'o': p('open'), 'h': p('high'), 'l': p('low'), 'c': p('close'), 'v': p('volume')}
        D.update(luar=sorted(set(d.ticker) - {'SPY', 'QQQ'}), s431=[], gagal=[], pelik=0)
        pd.to_pickle(D, f); print(json.dumps({'saham': len(D['luar']), 'bar': len(D['c'])})); return
    import yfinance as yf
    luar, s431, pelik = alam()
    tk = luar + [t for t in s431 if t not in set(luar)] + ['SPY', 'QQQ']
    O, H, L, C, V, gagal = [], [], [], [], [], []
    for i in range(0, len(tk), 200):
        ks = [t.replace('.', '-') for t in tk[i:i + 200]]
        df = None
        for n in range(3):
            try:
                df = yf.download(ks, start=MULA_DATA, interval='1d', auto_adjust=False, actions=False,
                                 group_by='column', threads=True, progress=False)
                break
            except Exception as e:
                print(f'kumpulan {i}: cuba {n + 1} gagal ({e})', file=sys.stderr, flush=True); time.sleep(20 * (n + 1))
        if df is None or df.empty:
            gagal += ks; continue
        for nm, out in (('Open', O), ('High', H), ('Low', L), ('Close', C), ('Volume', V)):
            x = df[nm].copy(); x.columns = [c.replace('-', '.') for c in x.columns]; out.append(x.astype('float32'))
        print(f'{i + len(ks)}/{len(tk)}', flush=True); time.sleep(2)
    D = {k: pd.concat(x, axis=1) for k, x in zip('ohlcv', (O, H, L, C, V))}
    for x in D.values():
        x.index = pd.to_datetime(x.index).tz_localize(None)
    ada = D['c'].columns[D['c'].notna().sum() > 0]; D = {k: x[ada].sort_index() for k, x in D.items()}; s = set(ada)
    D.update(luar=[t for t in luar if t in s], s431=[t for t in s431 if t in s], gagal=gagal, pelik=pelik)
    pd.to_pickle(D, f)
    print(json.dumps({'luar': len(D['luar']), 's431': len(D['s431']), 'bar': len(D['c']), 'dari': str(D['c'].index[0].date()),
                      'hingga': str(D['c'].index[-1].date()), 'gagal': len(gagal), 'pelik_dibuang': pelik}))


def muat_data(path, alam='luar'):
    """Bersihkan data (lonjakan sehari `kajian_rs.bersih`, OHLC tidak konsisten) dan bina fr/idx seperti dataset_S.
    alam = 'luar' (saham bukan set 431) atau '431' (kawalan: set 431 dengan data dan tempoh yang sama).
    Pulang fr (saham alam sahaja), idx (SPY, QQQ), c (tutup bersih semua saham untuk RS), v (volum), meta."""
    D = pd.read_pickle(path); senarai = D['luar'] if alam == 'luar' else D['s431']
    c0 = D['c'].astype('float64'); c = kajian_rs.bersih(c0); lonjak = (c0.notna() & c.isna()).sum()
    o, h, l, v = (D[k].astype('float64')[c.columns] for k in 'ohlv')
    ok = (c.notna() & o.notna() & h.notna() & l.notna() & (l > 0) & (h >= l) & (c <= h * 1.002) & (c >= l * 0.998)
          & (o <= h * 1.002) & (o >= l * 0.998))
    tak_konsisten = (c.notna() & ~ok).sum(); nbar = ok.sum()
    rosak = (lonjak > 5) | (tak_konsisten > 0.01 * nbar.clip(lower=1)) | (nbar < 300)
    rosak = sorted(c.columns[rosak & ~c.columns.isin(['SPY', 'QQQ'])])
    c, o, h, l = (x.where(ok) for x in (c, o, h, l)); v = v.where(ok).fillna(0.0)
    dates = c.index; on, hn, ln, cn, vn, okn = (x.to_numpy() for x in (o, h, l, c, v, ok))
    def bina(t):
        j = c.columns.get_loc(t); m = okn[:, j]
        g = pd.DataFrame({'open': on[m, j], 'high': hn[m, j], 'low': ln[m, j], 'close': cn[m, j], 'volume': vn[m, j]}, index=dates[m])
        g['turnover'] = g.close * g.volume; return g
    buang = set(rosak); fr = {t: bina(t) for t in senarai if t not in buang}
    idx = {k: bina(k) for k in ('SPY', 'QQQ') if k in c.columns}
    saham = [t for t in c.columns if t not in buang and t not in ('SPY', 'QQQ')]
    meta = {'alam': alam, 'saham_alam': len(fr), 'luar': len([t for t in D['luar'] if t not in buang]),
            's431': len([t for t in D['s431'] if t not in buang]), 'rosak': rosak, 'gagal_tarik': len(D.get('gagal', [])),
            'pelik_dibuang': int(D.get('pelik', 0)), 'bar': int(len(dates)), 'dari': str(dates[0].date()), 'hingga': str(dates[-1].date())}
    return fr, idx, c[saham], v[saham], meta


def layak_siri(close, volume):
    """Syarat isyarat layak (seperti lejar): tutup >= USD10 dan purata nilai dagangan 50 hari >= USD5 juta."""
    return (close >= HARGA_MIN) & ((close * volume).rolling(50, min_periods=40).mean() >= NILAI_MIN)


# ---------------------------------------------------------------- 2. dagangan kaedah (matriks Actions)
FR = IDX = LAYAK = OUT = None


def _kerja(mid):
    f = f'{OUT}/{mid}.pkl'
    if os.path.exists(f): return mid, 'ada', 0, 0.0
    t0 = time.time()
    from enjin import trades
    m = importlib.import_module(f'kaedah.{mid}')
    perlu = getattr(m, 'PERLU_BAR', 0); silang = getattr(m, 'SILANG', False)     # seperti lejar.py: bar mencukupi (atau kaedah silang)
    fr = {t: g[['open', 'high', 'low', 'close', 'volume', 'turnover']].copy() for t, g in FR.items() if len(g) >= perlu or silang}
    try:
        m.sedia(fr, {k: v.copy() for k, v in IDX.items()})
        T = trades(fr, tmax=m.TMAX, warm=m.WARM)
    except Exception as e:                                  # rekod kegagalan; kaedah ini kosong (dilaporkan dalam log)
        print(f'{mid} GAGAL: {type(e).__name__}: {e}', file=sys.stderr, flush=True)
        T = pd.DataFrame(columns=['ticker', 'sig', 'ent', 'ex', 'ret', 'days', 'why', 'rank'])
    del fr; n0 = len(T)
    if n0:
        ok = np.zeros(n0, bool)
        for t, G in T.groupby('ticker'):
            ok[G.index.to_numpy()] = LAYAK[t][FR[t].index.get_indexer(G.sig)]
        T = T[ok].drop(columns=['mfe'], errors='ignore').reset_index(drop=True)
    T['mid'] = mid
    pickle.dump(T, open(f, 'wb')); return mid, len(T), n0, time.time() - t0


def cmd_jana(a):
    global FR, IDX, LAYAK, OUT
    from multiprocessing import get_context
    OUT = a.keluar; os.makedirs(OUT, exist_ok=True); sys.path.insert(0, KOD)
    i, n = (int(x) for x in a.bahagian.split('/'))
    mids = sorted(os.path.basename(p)[:-3] for p in glob.glob(f'{KOD}/kaedah/M*.py'))[i::n]
    FR, IDX, _, _, meta = muat_data(a.data, a.alam)
    LAYAK = {t: layak_siri(g.close, g.volume).to_numpy() for t, g in FR.items()}
    print('alam', a.alam, 'bahagian', a.bahagian, 'kaedah', mids, '| saham', len(FR), '| rosak', len(meta['rosak']), flush=True)
    with get_context('fork').Pool(a.proses) as p:
        for mid, n1, n0, s in p.imap_unordered(_kerja, mids): print(f'{mid}: {n1} layak / {n0} dagangan, {s:.0f}s', flush=True)


# ---------------------------------------------------------------- 3. calon + ukuran pada hari isyarat (seperti kaji_portfolio.cmd_sedia)
def rs_pasaran(c):
    """RS lawan seluruh pasaran AS (formula kajian_rs): 40% r63 + 20% tiga suku sebelumnya, persentil 1–99 setiap hari antara
    saham dengan tutup >= USD5 dan >= 253 bar. Tanpa pandang hadapan (nilai hari isyarat sahaja)."""
    q = [c.shift(k) for k in (63, 126, 189, 252)]
    sk = 0.4 * (c / q[0] - 1) + 0.2 * (q[0] / q[1] - 1) + 0.2 * (q[1] / q[2] - 1) + 0.2 * (q[2] / q[3] - 1)
    return kajian_rs.persentil(sk.replace([np.inf, -np.inf], np.nan), (c >= kajian_rs.HARGA_MIN) & q[3].notna())


def cmd_ciri(a):
    from kaji_lorong2 import COST, sim, tatasusunan
    T = pd.concat([pd.read_pickle(f) for f in sorted(glob.glob(f'{a.dagangan}/*.pkl'))], ignore_index=True)
    fr, idx, c_all, _, meta = muat_data(a.data, a.alam); so, sc = idx['SPY'].open, idx['SPY'].close
    n = len(T); print('dagangan', n, 'kaedah', T.mid.nunique(), 'saham', T.ticker.nunique(), flush=True)
    F = {k: np.full(n, np.nan) for k in ('buka', 'ret2', 'mom126', 'mutlak12', 'mansfield', 'atrp')}
    ex2 = np.empty(n, 'datetime64[ns]'); akhir2 = np.zeros(n, bool)
    for t, G in T.groupby('ticker'):
        g = fr[t]; dts = g.index; o, h, l, c, A, we, pwc = tatasusunan(g)
        ks = dts.get_indexer(G.ent).astype(np.int64); ss = dts.get_indexer(G.sig); ix = G.index.to_numpy()
        J, X, Wk = sim(o, h, l, c, A['atr14'], we, pwc, ks, np.full(len(ks), np.nan), 6, 4.0, 1)
        F['buka'][ix] = o[ks]; F['ret2'][ix] = X / o[ks] * (1 - COST) / (1 + COST) - 1
        ex2[ix] = dts[J].values; akhir2[ix] = Wk == 2
        cl = g.close; rl = cl / sc.reindex(dts).ffill()
        F['mom126'][ix] = (cl / cl.shift(126) - 1).to_numpy()[ss]
        F['mutlak12'][ix] = (cl / cl.shift(252) - 1).to_numpy()[ss]
        F['mansfield'][ix] = (rl / rl.rolling(252).mean() - 1).to_numpy()[ss]
        pc = cl.shift(1); tr = pd.concat([g.high - g.low, (g.high - pc).abs(), (g.low - pc).abs()], axis=1).max(axis=1)
        F['atrp'][ix] = (tr.rolling(14).mean() / cl).to_numpy()[ss]
    for k, v in F.items(): T[k] = v
    T['ex2'] = ex2; T['akhir2'] = akhir2; T['akhir1'] = T.why.eq('hujung')
    cf = lambda d: sc.reindex(pd.DatetimeIndex(d), method='ffill').to_numpy()
    T['spy1'] = cf(T.ex) / so.reindex(T.ent).to_numpy() - 1
    T['spy2'] = cf(T.ex2) / so.reindex(T.ent).to_numpy() - 1
    T['spy_atas'] = (sc > sc.rolling(200).mean()).reindex(T.sig).to_numpy()
    rs = rs_pasaran(c_all); di = rs.index.get_indexer(T.sig); tj = rs.columns.get_indexer(T.ticker)
    v = rs.to_numpy()[np.maximum(di, 0), np.maximum(tj, 0)]; v[(di < 0) | (tj < 0)] = np.nan; T['rs'] = v
    T['ind_skor'] = np.nan                                  # tiada gred industri sejarah bagi alam luar
    T['konsensus'] = T.groupby(['ticker', 'sig']).mid.transform('nunique')
    os.makedirs(a.keluar, exist_ok=True); T.to_pickle(os.path.join(a.keluar, f'calon_{a.alam}.pkl'))
    print('liputan: rs %.1f%%, mansfield %.1f%%, spy_atas %.1f%%' % tuple(100 * T[k].notna().mean() for k in ('rs', 'mansfield', 'spy_atas')))


def dagangan_ikut_rs(P, h1_akhir):
    """Diagnostik: hasil setiap dagangan calon (tempoh portfolio) mengikut gred RS pasaran hari isyarat, L1 dan L2, kedua-dua era."""
    T = P.T; gred = pd.cut(T.rs, [0, 59, 79, 89, 94, 99], labels=['01-59', '60-79', '80-89', '90-94', '95-99'])
    era = np.where(T.ent <= h1_akhir, 'era 1', 'era 2'); rows = []
    for L in (1, 2):
        r = P.ret[L]; x = r - T[f'spy{L}'].to_numpy(); d = P.ex_i[L] - P.ent_i + 1
        for (e, g), ix in pd.Series(np.arange(len(T))).groupby([era, gred], observed=True).indices.items():
            rows.append(dict(L=L, era=e, rs=g, n=len(ix), purata=r[ix].mean(), median=np.median(r[ix]), menang=(r[ix] > 0).mean(),
                             p5=np.percentile(r[ix], 5), lebih_spy=np.nanmean(x[ix]), hari=d[ix].mean(), rugi50=(r[ix] <= -0.5).mean()))
    return pd.DataFrame(rows)


# ---------------------------------------------------------------- 4. simulasi portfolio (enjin kaji_portfolio)
def sama_rata(c, v, hari, mula):
    """Penanda aras: (a) beli dan pegang sama rata semua saham layak pada hari pertama;
    (b) sama rata saham layak, imbang semula setiap 21 hari dagangan (saham tersenarai kemudian masuk apabila layak)."""
    L = layak_siri(c, v).reindex(hari).fillna(False).to_numpy(); C = c.reindex(hari).ffill().to_numpy(); n = len(hari)
    a0 = L[0] & np.isfinite(C[0]); bh = np.nanmean(C[:, a0] / C[0, a0], axis=1)
    out = np.ones(n); nilai = 1.0; bil = []
    for k in range(0, n - 1, 21):
        t1 = min(k + 21, n - 1); pick = L[k] & np.isfinite(C[k]); bil.append(int(pick.sum()))
        rel = np.nanmean(C[k:t1 + 1][:, pick] / C[k, pick], axis=1); out[k:t1 + 1] = nilai * rel; nilai = out[t1]
    return pd.Series(bh, hari), pd.Series(out, hari), int(a0.sum()), float(np.mean(bil))


def ukur(cv, h1_akhir):
    h1 = cv[cv.index <= h1_akhir]; h2 = cv[cv.index > h1_akhir]
    import kaji_portfolio as kp
    return dict(cagr=kp.cagr(cv), mdd=(cv / cv.cummax() - 1).min(), h1=kp.cagr(h1), h2=kp.cagr(pd.concat([h1.iloc[-1:], h2])))


def tahunan(cv):
    y = cv.resample('YE').last(); y = pd.concat([cv.iloc[:1], y]).pct_change().dropna()
    return (100 * y).set_axis(y.index.year)


def cmd_sim(a):
    import kaji_portfolio as kp
    mula, h1_akhir = pd.Timestamp(a.mula), pd.Timestamp(a.h1); kp.H1_AKHIR = h1_akhir
    T = pd.read_pickle(a.calon); fr, idx, c_all, v_all, meta = muat_data(a.data, a.alam)
    P = kp.Pasar(T, fr, mula=mula); os.makedirs(a.keluar, exist_ok=True)
    print('alam', a.alam, 'calon portfolio', len(P.T), 'hari', len(P.hari), P.hari[0].date(), '->', P.hari[-1].date(), flush=True)
    dagangan_ikut_rs(P, h1_akhir).to_csv(os.path.join(a.keluar, 'dagangan_rs.csv'), index=False, float_format='%.5f')
    rows, thn, pct = [], {}, {}
    def rekod(nama, L, slots, benih, cv, npos, ambil):
        m = kp.metrik(cv, npos, P, L, ambil); rows.append(dict(peraturan=nama, benih=benih, L=L, slot_n=slots, **m)); return m, cv
    for L in (1, 2):
        R = {k: v[P.pilih] for k, v in kp.peraturan(T, L).items() if k in PILIH}   # skor walk-forward guna sejarah sebelum mula
        raw = []
        for b in range(BENIH):
            m, cv = rekod('Rawak', L, 10, b, *P.jalan(L, np.zeros(len(P.T)), benih=b)); raw.append(tahunan(cv))
        thn[f'Rawak (median {BENIH} benih) L{L}'] = pd.concat(raw, axis=1).median(axis=1)
        for nama, sk in R.items():
            m, cv = rekod(nama, L, 10, -1, *P.jalan(L, sk)); thn[f'{nama} L{L}'] = tahunan(cv)
        for b in range(10): rekod('Rawak', L, 20, b, *P.jalan(L, np.zeros(len(P.T)), benih=b, slots=20, w=0.05))
        rekod('RS pasaran', L, 20, -1, *P.jalan(L, R['RS pasaran'], slots=20, w=0.05))
        print('L', L, 'siap', flush=True)
    D = pd.DataFrame(rows); B = []
    for (L, sn), G in D.groupby(['L', 'slot_n']):
        r = G[G.peraturan == 'Rawak']; lain = G[G.peraturan != 'Rawak'].copy()
        for k in ('cagr', 'mar', 'h1', 'h2'): lain[f'{k}_pct_rawak'] = [100 * (r[k] < x).mean() for x in lain[k]]
        rw = r.drop(columns=['peraturan', 'benih']).median(numeric_only=True); rw['peraturan'] = f'Rawak (median {len(r)} benih)'
        rw['rawak_p5'], rw['rawak_p95'] = r.cagr.quantile(.05), r.cagr.quantile(.95)
        X = pd.concat([pd.DataFrame([rw]), lain], ignore_index=True); X['L'], X['slot_n'] = L, sn; B.append(X)
    pd.concat(B, ignore_index=True).to_csv(os.path.join(a.keluar, 'keputusan.csv'), index=False, float_format='%.5f')
    # penanda aras
    spy = idx['SPY'].close.reindex(P.hari).ffill(); spy = spy / spy.iloc[0]
    bh, ir, n_bh, n_ir = sama_rata(c_all[[t for t in c_all.columns if t in fr]], v_all[[t for t in c_all.columns if t in fr]], P.hari, mula)
    pen = {'SPY': spy, f'Beli dan pegang sama rata ({n_bh} saham layak {mula.date()})': bh,
           f'Sama rata saham layak, imbang semula 21 hari (purata {n_ir:.0f} saham)': ir}
    pd.DataFrame([dict(penanda=k, **ukur(s, h1_akhir)) for k, s in pen.items()]).to_csv(os.path.join(a.keluar, 'penanda.csv'), index=False, float_format='%.5f')
    for k, s in pen.items(): thn[k.split(' (')[0]] = tahunan(s)
    pd.DataFrame(thn).T.round(1).to_csv(os.path.join(a.keluar, 'tahunan.csv'))
    # ketahanan: buang N saham pulangan tertinggi tempoh portfolio (pandang hadapan), ulang
    jum = pd.Series({t: g.close.iloc[-1] / g.close[g.index >= mula].iloc[0] - 1 for t, g in fr.items() if (g.index >= mula).any()})
    atas = list(jum.sort_values(ascending=False).index); rows = []
    for L in (1, 2):
        R = {k: v[P.pilih] for k, v in kp.peraturan(T, L).items() if k in TAHAN}
        for nb in (0, 40, 100):
            tp = ~P.T.ticker.isin(atas[:nb]).to_numpy(); r = []
            for b in range(20):
                cv, npos, ambil = P.jalan(L, np.zeros(len(P.T)), tp, benih=b); r.append(kp.metrik(cv, npos, P, L, ambil))
            r = pd.DataFrame(r)
            rows.append(dict(L=L, buang=nb, peraturan='Rawak (median 20 benih)', **r.median().to_dict()))
            for nama, sk in R.items():
                cv, npos, ambil = P.jalan(L, sk, tp); m = kp.metrik(cv, npos, P, L, ambil)
                u = pd.Series(kp.portfolio.amaun * P.ret[L][ambil]).groupby(P.T.ticker.to_numpy()[ambil]).sum()
                rows.append(dict(L=L, buang=nb, peraturan=nama, **m, tumpuan5=u.nlargest(5).sum() / u.sum(),
                                 **{f'{k}_pct_rawak': 100 * (r[k] < m[k]).mean() for k in ('cagr', 'h1', 'h2')},
                                 atas5=', '.join(u.nlargest(5).index), bawah5=', '.join(u.nsmallest(5).index),
                                 untung_atas5=u.nlargest(5).sum(), rugi_bawah5=u.nsmallest(5).sum(), untung_bersih=u.sum()))
            print('ketahanan L', L, 'buang', nb, 'siap', flush=True)
    pd.DataFrame(rows).to_csv(os.path.join(a.keluar, 'ketahanan.csv'), index=False, float_format='%.5f')
    meta.update(dagangan=int(len(T)), calon_portfolio=int(len(P.T)), kaedah=int(T.mid.nunique()), saham_dagangan=int(P.T.ticker.nunique()),
                mula=str(mula.date()), h1_akhir=str(h1_akhir.date()), hingga_portfolio=str(P.hari[-1].date()),
                pemenang_40=', '.join(f'{t} {100 * jum[t]:.0f}%' for t in atas[:40]), harga_min=HARGA_MIN, nilai_min=NILAI_MIN,
                rugi50_pct={f'L{L}': round(100 * float((P.ret[L] <= -0.5).mean()), 3) for L in (1, 2)},
                dijana=pd.Timestamp.now('UTC').strftime('%Y-%m-%d %H:%M UTC'))
    json.dump(meta, open(os.path.join(a.keluar, 'meta.json'), 'w'), indent=1)
    cmd_ringkas(a)


def cmd_ringkas(a):
    pd.set_option('display.width', 250)
    meta = json.load(open(os.path.join(a.keluar, 'meta.json')))
    print(json.dumps({k: v for k, v in meta.items() if k != 'rosak'}, indent=1))
    D = pd.read_csv(os.path.join(a.keluar, 'keputusan.csv')); pen = pd.read_csv(os.path.join(a.keluar, 'penanda.csv'))
    print('\n== Penanda aras'); Y = pen.copy()
    for c in ('cagr', 'mdd', 'h1', 'h2'): Y[c] = 100 * Y[c]
    print(Y.round(1).to_string(index=False))
    cols = ['peraturan', 'cagr', 'mdd', 'mar', 'h1', 'h2', 'n', 'menang', 'purata', 'lebih_spy', 'hari', 'slot', 'rawak_p5', 'rawak_p95',
            'cagr_pct_rawak', 'h1_pct_rawak', 'h2_pct_rawak']
    for (L, sn), G in D.groupby(['L', 'slot_n']):
        Y = G[[c for c in cols if c in G]].copy()
        for c in ('cagr', 'mdd', 'h1', 'h2', 'menang', 'purata', 'lebih_spy', 'rawak_p5', 'rawak_p95'): Y[c] = 100 * Y[c]
        print(f"\n== Keluar L{L} ({'kaedah' if L == 1 else 'Chandelier'}), {sn} slot"); print(Y.set_index('peraturan').round(1).to_string())
    K = pd.read_csv(os.path.join(a.keluar, 'ketahanan.csv'))
    for (L, nb), G in K.groupby(['L', 'buang']):
        Y = G.drop(columns=['L', 'buang']).copy()
        for c in ('cagr', 'mdd', 'h1', 'h2', 'menang', 'purata', 'lebih_spy', 'tumpuan5'): Y[c] = 100 * Y[c]
        print(f'\n== Ketahanan L{L}, buang {nb} saham teratas')
        print(Y[['peraturan', 'cagr', 'mdd', 'mar', 'h1', 'h2', 'n', 'tumpuan5', 'cagr_pct_rawak', 'h1_pct_rawak', 'h2_pct_rawak', 'atas5', 'bawah5']].set_index('peraturan').round(1).to_string())
    print('\n== Pulangan tahunan %'); print(pd.read_csv(os.path.join(a.keluar, 'tahunan.csv'), index_col=0).to_string())
    R = pd.read_csv(os.path.join(a.keluar, 'dagangan_rs.csv'))
    for c in ('purata', 'median', 'menang', 'p5', 'lebih_spy', 'rugi50'): R[c] = 100 * R[c]
    print('\n== Dagangan calon ikut gred RS pasaran (%)'); print(R.round(2).to_string(index=False))


if __name__ == '__main__':
    ap = argparse.ArgumentParser(); s = ap.add_subparsers(dest='cmd', required=True)
    x = s.add_parser('tarik'); x.add_argument('--keluar', required=True); x.add_argument('--dataset'); x.set_defaults(f=cmd_tarik)
    x = s.add_parser('jana'); x.add_argument('--data', required=True); x.add_argument('--bahagian', default='0/1'); x.add_argument('--alam', default='luar', choices=['luar', '431'])
    x.add_argument('--keluar', required=True); x.add_argument('--proses', type=int, default=4); x.set_defaults(f=cmd_jana)
    x = s.add_parser('ciri'); x.add_argument('--data', required=True); x.add_argument('--dagangan', required=True); x.add_argument('--alam', default='luar', choices=['luar', '431'])
    x.add_argument('--keluar', required=True); x.set_defaults(f=cmd_ciri)
    x = s.add_parser('sim'); x.add_argument('--data', required=True); x.add_argument('--calon', required=True); x.add_argument('--alam', default='luar', choices=['luar', '431'])
    x.add_argument('--keluar', default=HERE); x.add_argument('--mula', default=str(MULA.date())); x.add_argument('--h1', default=str(H1_AKHIR.date()))
    x.set_defaults(f=cmd_sim)
    x = s.add_parser('ringkas'); x.add_argument('--keluar', default=HERE); x.set_defaults(f=cmd_ringkas)
    a = ap.parse_args(); a.f(a)
