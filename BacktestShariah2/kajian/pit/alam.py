# alam.py — alam point-in-time (PIT) kajian pintu B (pra-daftar PRA_DAFTAR.md §2).
# Data: aset Release `autotune-data-a02` (yfinance auto_adjust + faktor_split; 3260 ticker; 2009-01-02 – 2026-10-16).
# Syarat layak hari i (hanya data <= i): tutup_mentah >= USD10, median 20 bar nilai dagangan >= USD5 juta, >= 252 bar.
# Saringan Shariah sektor (a): peta industri Moomoo (papertrade/peta_industri.csv) + sandaran TradingView (data/skrin/tv_us.csv).
# Versi: A = layak & sektor (UTAMA); B = A & skrin Shariah Moomoo semasa (data/harga/univ.txt; kepekaan pandang hadapan);
#        K431 = A & 431 ticker set asal (diagnostik).
# Cache (dalam --data, BUKAN repo): pit_cache/fr.pkl (dict ticker -> DataFrame), pit_cache/mat.npz (matriks tarikh x ticker),
# pit_cache/meta.json. Bina: python3 BacktestShariah2/kajian/pit/uji_pit.py bina --data DIR
import glob, json, os, pickle, subprocess

import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
BS2 = os.path.dirname(os.path.dirname(HERE))
AKAR = os.path.dirname(BS2)
REPO_API = 'repos/pedagangsenja/papertrade-claude'
TAG = 'autotune-data-a02'
MULA_DATA = '2010-01-01'
HARGA_MIN = 10.0
NILAI_MIN = 5e6
BAR_MIN = 252
TETINGKAP_NILAI = 20
HAD_EW = 0.5
RS_HARGA_MIN = 5.0
RS_BAR_MIN = 253

# --- saringan Shariah sektor (pra-daftar §2.4) ---
INDUSTRI_KECUALI = {
    # perbankan & kewangan konvensional
    'Banks - Regional', 'Banks - Diversified', 'Asset Management', 'Capital Markets', 'Credit Services', 'Mortgage Finance',
    'Financial Conglomerates', 'Financial Data & Stock Exchanges', 'REIT - Mortgage', 'Shell Companies',
    # insurans
    'Insurance - Property & Casualty', 'Insurance - Life', 'Insurance - Specialty', 'Insurance - Diversified',
    'Insurance - Reinsurance', 'Insurance Brokers',
    # alkohol, perjudian, tembakau, senjata
    'Beverages - Brewers', 'Beverages - Wineries & Distilleries', 'Gambling', 'Resorts & Casinos', 'Tobacco', 'Aerospace & Defense',
}
INDUSTRI_KECUALI_TV = {
    'Major Banks', 'Regional Banks', 'Savings Banks', 'Finance/Rental/Leasing', 'Investment Banks/Brokers', 'Investment Managers',
    'Financial Conglomerates', 'Life/Health Insurance', 'Multi-Line Insurance', 'Property/Casualty Insurance', 'Specialty Insurance',
    'Insurance Brokers/Services', 'Investment Trusts/Mutual Funds', 'Beverages: Alcoholic', 'Tobacco', 'Casinos/Gaming',
    'Aerospace & Defense',
}
TICKER_KECUALI = {'HRL': 'babi', 'TSN': 'babi', 'SFD': 'babi'}


def norm(t):
    return str(t).strip().upper().replace('.', '-').replace(' ', '-')


def muat_release(keluar, tag=TAG):
    """Muat turun aset Release melalui REST API GitHub (gh api). Pulang senarai fail."""
    j = json.loads(subprocess.run(['gh', 'api', f'{REPO_API}/releases/tags/{tag}'], capture_output=True, text=True,
                                  check=True).stdout)
    os.makedirs(keluar, exist_ok=True); fail = []
    for a in j['assets']:
        p = os.path.join(keluar, a['name']); fail.append(p)
        if os.path.exists(p) and os.path.getsize(p) == a['size']: continue
        with open(p, 'wb') as f:
            subprocess.run(['gh', 'api', '-H', 'Accept: application/octet-stream', f'{REPO_API}/releases/assets/{a["id"]}'],
                           stdout=f, check=True)
    return fail


def peta_shariah(tickers, peta=None, tv=None, kecuali_ticker=None):
    """DataFrame index ticker: industri, sumber ('moomoo'/'tv'/'tiada'), ok (lulus saringan sektor), sebab."""
    peta = os.path.join(BS2, 'papertrade', 'peta_industri.csv') if peta is None else peta
    tv = os.path.join(BS2, 'data', 'skrin', 'tv_us.csv') if tv is None else tv
    kt = TICKER_KECUALI if kecuali_ticker is None else kecuali_ticker
    p = pd.read_csv(peta); p['t'] = p.ticker.map(norm); P = p.drop_duplicates('t').set_index('t').industri
    v = pd.read_csv(tv); v['t'] = v.ticker.map(norm); V = v.drop_duplicates('t').set_index('t').industry
    rows = []
    for t in tickers:
        if t in P.index and isinstance(P[t], str):
            ind, sb = P[t], 'moomoo'; ok = ind not in INDUSTRI_KECUALI
        elif t in V.index and isinstance(V[t], str):
            ind, sb = V[t], 'tv'; ok = ind not in INDUSTRI_KECUALI_TV
        else:
            ind, sb, ok = '', 'tiada', False
        sebab = '' if ok else ('industri' if sb != 'tiada' else 'tiada industri')
        if t in kt:
            ok, sebab = False, kt[t]
        rows.append((t, ind, sb, ok, sebab))
    return pd.DataFrame(rows, columns=['ticker', 'industri', 'sumber', 'ok', 'sebab']).set_index('ticker')


def senarai_univ(path=None):
    path = os.path.join(BS2, 'data', 'harga', 'univ.txt') if path is None else path
    with open(path, encoding='utf-8') as f:
        return {norm(x) for x in f if x.strip()}


def senarai_431():
    s = set()
    for f in sorted(glob.glob(os.path.join(AKAR, 'data_mentah', 'dataset_S*.csv'))):
        s |= set(pd.read_csv(f, usecols=['ticker']).ticker.map(norm))
    return s


def baca_harga(data, mula=MULA_DATA):
    fs = sorted(glob.glob(os.path.join(data, 'harga_*.parquet')))
    fs = [f for f in fs if int(os.path.basename(f)[6:10]) >= pd.Timestamp(mula).year]
    d = pd.concat([pd.read_parquet(f) for f in fs], ignore_index=True)
    d = d[d.date >= pd.Timestamp(mula)]
    d['ticker'] = d.ticker.map(norm)
    return d.sort_values(['ticker', 'date']).reset_index(drop=True)


def ciri_layak(d):
    """Tambah lajur pada data panjang (diisih ticker, date): mentah, nilai, med20, nbar, layak (syarat §2.3 tanpa sektor)."""
    d = d.copy()
    d['mentah'] = d.close.astype('float64') * d.faktor_split.astype('float64')
    d['nilai'] = d.close.astype('float64') * d.volume.astype('float64')
    g = d.groupby('ticker', sort=False)
    d['med20'] = g.nilai.transform(lambda s: s.rolling(TETINGKAP_NILAI, min_periods=TETINGKAP_NILAI).median())
    d['nbar'] = g.cumcount() + 1
    d['layak'] = (d.mentah >= HARGA_MIN) & (d.med20 >= NILAI_MIN) & (d.nbar >= BAR_MIN)
    return d


def skor_rs(d):
    """Skor IBD 40/20/20/20 (formula standard/rs_pasaran.py) atas bar ticker sendiri + kelayakan pangkat RS."""
    g = d.groupby('ticker', sort=False).close
    q = [g.shift(k) for k in (63, 126, 189, 252)]
    c = d.close.astype('float64')
    sk = 0.4 * (c / q[0] - 1) + 0.2 * (q[0] / q[1] - 1) + 0.2 * (q[1] / q[2] - 1) + 0.2 * (q[2] / q[3] - 1)
    sk = sk.replace([np.inf, -np.inf], np.nan)
    ok = (d.mentah >= RS_HARGA_MIN) & (d.nbar >= RS_BAR_MIN) & q[3].notna()
    return sk.where(ok)


def ew_harian(C, M):
    """C: DataFrame tutup (tarikh x ticker, NaN = tiada bar). M: DataFrame bool layak (sama bentuk).
    Pulangan harian EW: purata (tutup_t / tutup_{t-1} - 1) bagi saham layak pada t-1 dengan bar pada t-1 dan t, dihad +-50%."""
    r = (C / C.shift(1) - 1).clip(-HAD_EW, HAD_EW)
    m = M.shift(1, fill_value=False) & C.notna() & C.shift(1).notna()
    r = r.where(m)
    return r.mean(axis=1), m.sum(axis=1)


def bina_cache(data, keluar=None, mula=MULA_DATA, log=print):
    """Bina cache alam PIT dalam data/pit_cache (lihat kepala fail). Pulang meta (dict)."""
    keluar = os.path.join(data, 'pit_cache') if keluar is None else keluar
    os.makedirs(keluar, exist_ok=True)
    d = ciri_layak(baca_harga(data, mula))
    d['rs_skor'] = skor_rs(d)
    tik = sorted(d.ticker.unique()); log(f'harga: {len(d)} bar, {len(tik)} ticker')
    piv = lambda k: d.pivot(index='date', columns='ticker', values=k).reindex(columns=tik)  # noqa: E731
    O, C, L, SK = piv('open').astype('float64'), piv('close').astype('float64'), piv('layak'), piv('rs_skor')
    L = L.fillna(False).astype(bool)
    tarikh = C.index
    sh = peta_shariah(tik)
    u = senarai_univ(); k431 = senarai_431()
    ok = sh.ok.reindex(tik).values
    MA = L & ok[None, :]
    MB = MA & np.array([t in u for t in tik])[None, :]
    MK = MA & np.array([t in k431 for t in tik])[None, :]
    # RS persentil 1-99 merentas semua ticker data (seluruh pasaran dalam data)
    RS = (SK.rank(axis=1, pct=True) * 98 + 1).round()
    # EW setiap versi
    ew = {}
    for v, M in (('A', MA), ('B', MB), ('K431', MK)):
        r, n = ew_harian(C, M); ew[v] = r; ew['n_' + v] = n
    EW = pd.DataFrame(ew)
    # bingkai kaedah (format kod/kaedah: open high low close volume turnover)
    fr = {}
    for t, g in d.groupby('ticker', sort=True):
        x = g.set_index('date')[['open', 'high', 'low', 'close', 'volume']].astype('float64')
        x['turnover'] = x.close * x.volume
        x.index.name = None
        fr[t] = x
    ix = pd.read_parquet(os.path.join(data, 'idx.parquet'))
    ix = ix[ix.date >= pd.Timestamp(mula)]
    idx = {}
    for t, g in ix.groupby('ticker'):
        x = g.set_index('date')[['open', 'high', 'low', 'close', 'volume']].astype('float64'); x['turnover'] = x.close * x.volume
        x.index.name = None; idx[t] = x
    with open(os.path.join(keluar, 'fr.pkl'), 'wb') as f:
        pickle.dump(dict(fr=fr, idx=idx), f, protocol=pickle.HIGHEST_PROTOCOL)
    np.savez_compressed(os.path.join(keluar, 'mat.npz'), O=O.values, C=C.values, Cf=C.ffill().values, MA=MA.values,
                        MB=MB.values, MK=MK.values, RS=RS.values.astype('float32'), SK=SK.values.astype('float32'))
    EW.to_pickle(os.path.join(keluar, 'ew.pkl'))
    pd.Series(tarikh).to_pickle(os.path.join(keluar, 'tarikh.pkl'))
    sh.to_csv(os.path.join(keluar, 'shariah.csv'))
    # ringkasan alam
    akhir = d.groupby('ticker').date.max(); mula_t = d.groupby('ticker').date.min()
    akhir_data = d.date.max()
    tahun = pd.DataFrame({'A': MA.sum(axis=1), 'B': MB.sum(axis=1), 'K431': MK.sum(axis=1), 'layak_tanpa_sektor': L.sum(axis=1)})
    tahun = tahun[tahun.index >= '2013-01-01'].groupby(tahun.index[tahun.index >= '2013-01-01'].year).median()
    meta = dict(
        sumber=f'Release {TAG}', mula_data=str(tarikh[0].date()), akhir_data=str(akhir_data.date()), ticker=len(tik),
        ticker_delist=int((akhir < akhir_data - pd.Timedelta(days=14)).sum()),
        ticker_sektor_ok=int(sh.ok.sum()), ticker_sektor_kecuali=int((~sh.ok).sum()),
        sumber_industri=sh.sumber.value_counts().to_dict(),
        pernah_layak=dict(A=int(MA.any().sum()), B=int(MB.any().sum()), K431=int(MK.any().sum()),
                          tanpa_sektor=int(L.any().sum())),
        median_layak_setahun={int(k): {c: int(v) for c, v in r.items()} for k, r in tahun.iterrows()},
        syarat=dict(harga_min=HARGA_MIN, nilai_min=NILAI_MIN, bar_min=BAR_MIN, tetingkap_nilai=TETINGKAP_NILAI),
    )
    with open(os.path.join(keluar, 'meta.json'), 'w') as f:
        json.dump(meta, f, indent=1)
    # senarai alam kecil (untuk repo): ticker, industri, sumber, ok, sebab, mula, akhir, hari layak A
    sen = sh.copy(); sen['mula'] = mula_t.reindex(sen.index).dt.strftime('%Y-%m-%d')
    sen['akhir'] = akhir.reindex(sen.index).dt.strftime('%Y-%m-%d')
    sen['hari_layak_A'] = MA.sum(axis=0).reindex(sen.index).astype(int)
    sen['dalam_univ_semasa'] = [t in u for t in sen.index]; sen['dalam_431'] = [t in k431 for t in sen.index]
    sen.to_csv(os.path.join(keluar, 'senarai_alam.csv'))
    log(json.dumps(meta)[:600])
    return meta


class Alam:
    """Muat cache alam PIT (dibina bina_cache)."""

    def __init__(self, data):
        k = os.path.join(data, 'pit_cache')
        with open(os.path.join(k, 'fr.pkl'), 'rb') as f:
            x = pickle.load(f)
        self.fr, self.idx = x['fr'], x['idx']
        z = np.load(os.path.join(k, 'mat.npz'))
        self.O, self.C, self.Cf = z['O'], z['C'], z['Cf']
        self.M = {'A': z['MA'], 'B': z['MB'], 'K431': z['MK']}
        self.RS, self.SK = z['RS'], z['SK']
        self.tarikh = pd.DatetimeIndex(pd.read_pickle(os.path.join(k, 'tarikh.pkl')))
        self.EW = pd.read_pickle(os.path.join(k, 'ew.pkl'))
        self.sh = pd.read_csv(os.path.join(k, 'shariah.csv'), index_col=0)
        self.tik = list(self.sh.index)
        self.col = {t: i for i, t in enumerate(self.tik)}
        with open(os.path.join(k, 'meta.json')) as f:
            self.meta = json.load(f)
        self.akhir_data = pd.Timestamp(self.meta['akhir_data'])

    def topeng(self, versi, t):
        """Siri bool layak (versi) bagi ticker t atas indeks bar ticker itu sendiri (dicache)."""
        if not hasattr(self, '_tp'): self._tp = {}
        k = (versi, t)
        if k not in self._tp:
            if not hasattr(self, '_pos'): self._pos = pd.Series(np.arange(len(self.tarikh)), index=self.tarikh)
            ii = self._pos.reindex(self.fr[t].index).values
            ok = ~np.isnan(ii)
            m = np.zeros(len(ii), bool); m[ok] = self.M[versi][ii[ok].astype(int), self.col[t]]
            self._tp[k] = m
        return self._tp[k]

    def tickers(self, versi):
        return [t for t in self.tik if self.M[versi][:, self.col[t]].any()] if versi != 'sektor' else \
            [t for t in self.tik if bool(self.sh.ok.get(t, False))]
