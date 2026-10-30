"""Ujian registry Nxx bahagian A — pradaftar `REVERSE/SPEC_NXX.md` (komit 2e10efc, §10 15a9d4b).

70 topeng MASUK x 4 keluar asas = 280 ujian. Keluar asas dibaca daripada cache
`pul_kombinasi.parquet` supaya lift dikira terhadap asas keluar YANG SAMA seperti
`KOMBINASI.md` — itu syarat perbandingan terus.

Takrif indikator datang daripada `REVERSE/teras/ind.py` (satu sumber kebenaran); 12 lajur
terbitan spec §4 ditambah di sini.

Guna: python3 REVERSE/step18_nxx.py [--laporan-sahaja]
Output: REVERSE/NXX.md, REVERSE/nxx.csv
"""
import argparse
import sys
import time
from pathlib import Path

import numpy as np
import pandas as pd

AKAR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(AKAR))
from REVERSE.teras import data as D  # noqa: E402
from REVERSE.teras import ind as I  # noqa: E402

KELUAR = AKAR / 'REVERSE'
CACHE = KELUAR / '.cache'
HARGA = AKAR / 'AUTOTUNE' / '.cache_autotune-data-a02'
PUL = CACHE / 'pul_kombinasi.parquet'
PANEL = CACHE / 'panel_nxx.parquet'

TH0, TH1 = 2012, 2025
LATIH, TAHAN = (2012, 2019), (2020, 2025)
CAIR = 100_000.0
MIN_N = 200
XK = ['X1', 'X2', 'X3', 'X4']

# lajur ind.kira yang diperlukan 66 peraturan (spec §4)
DARI_IND = ['ma50', 'ma150', 'ma200', 'ema9', 'ema21', 'rsi2', 'rsi14', 'bb_pctb', 'bb_lebar',
            'bb_squeeze', 'supertrend', 'adx14', 'pdi', 'mdi', 'atas_awan', 'tenkan_atas',
            'psar_arah', 'donchian20', 'donchian55', 'breakout_52w', 'pocket_pivot',
            'gap_and_go', 'vcp', 'nr7', 'inside_day', 'obv_tinggi_baru', 'cmf20', 'vol_n50',
            'cerun_ema21', 'julat10', 'julat20', 'j_ma200', 'j_52w_tinggi', 'hammer',
            'bullish_engulfing', 'rs_spy_6b', 'garis_rs_tinggi', 'sektor_atas_ma50',
            'macd', 'macd_sig', 'atr14']


def tambahan(g):
    """12 lajur terbitan spec §4 + yang ind.py tidak sediakan."""
    o, h, lo = g['open'], g['high'], g['low']
    c, v = g['close'], g['volume']
    d = pd.DataFrame(index=g.index)
    d['buka'], d['tinggi'], d['rendah'] = o, h, lo
    for n in (10, 20):
        d[f'ma{n}'] = c.rolling(n).mean()
    for n in (10, 20, 50):
        d[f'ema{n}'] = c.ewm(span=n, adjust=False, min_periods=n).mean()
    d['sd20'] = c.rolling(20).std(ddof=0)
    d['tinggi20'] = h.rolling(20).max().shift(1)
    d['tinggi_sepanjang'] = c.cummax().shift(1)
    d['tinggi_52w'] = h.rolling(252, min_periods=200).max().shift(1)
    d['rendah_52w'] = lo.rolling(252, min_periods=200).min()
    d['hari_minggu'] = np.asarray(g.index.dayofweek)
    d['bulan'] = np.asarray(g.index.month)
    julat = (h - lo).replace(0, np.nan)
    d['pos_buka'] = (o - lo) / julat
    d['pos_tutup'] = (c - lo) / julat
    d['julat4_min'] = (h - lo) <= (h - lo).rolling(4).min()
    d['turun_4d5'] = (c < c.shift(1)).rolling(5).sum() >= 4
    d['cerun_ma200_21'] = c.rolling(200).mean() > c.rolling(200).mean().shift(21)
    d['gap'] = o / c.shift(1) - 1.0
    d['sentuh_ema20'] = lo <= d['ema20']
    d['nilai20'] = (c * v).rolling(20, min_periods=10).median()
    return d


def bina_sektor(df, peta):
    """Indeks sektor berat sama rata: kumul min pulangan harian setiap sektor."""
    x = df[['ticker', 'date', 'close']].copy()
    x['sektor'] = x.ticker.map(peta.sektor)
    x = x[x.sektor.notna() & (x.sektor != 'Lain-lain')]
    x = x.sort_values(['ticker', 'date'])
    x['pul'] = x.groupby('ticker', sort=False).close.pct_change()
    m = x.groupby(['sektor', 'date']).pul.mean().unstack(0)
    return (1.0 + m.fillna(0.0)).cumprod()


def bina_panel():
    """Panel indikator setiap bar. Cache sekali (~60 minit)."""
    if PANEL.exists():
        return pd.read_parquet(PANEL)
    t0 = time.time()
    bhg = []
    for y in range(TH0 - 3, TH1 + 1):
        p = HARGA / f'harga_{y}.parquet'
        if p.exists():
            bhg.append(pd.read_parquet(p, columns=['ticker', 'date', 'open', 'high', 'low',
                                                   'close', 'volume']))
    df = pd.concat(bhg, ignore_index=True)
    df = df[df.date <= pd.Timestamp(f'{TH1}-12-31')].sort_values(['ticker', 'date'])
    print(f'  [{time.time()-t0:.0f}s] bar mentah {len(df):,} | ticker {df.ticker.nunique():,}',
          flush=True)
    ix = pd.read_parquet(HARGA / 'idx.parquet')
    spy = ix[ix.ticker == 'SPY'].sort_values('date').set_index('date')['close'].astype('float64')
    peta = D.peta_sektor(sorted(df.ticker.unique()))
    si = bina_sektor(df, peta)
    print(f'  [{time.time()-t0:.0f}s] SPY {len(spy):,} bar | sektor {si.shape[1]}', flush=True)
    bhgn = CACHE / 'panel_nxx_parts'
    bhgn.mkdir(parents=True, exist_ok=True)
    for old in bhgn.glob('*.parquet'):
        old.unlink()

    def _tulis(buf, j):
        R = pd.concat(buf, ignore_index=True)
        for c in R.columns:
            if R[c].dtype == 'float64':
                R[c] = R[c].astype('float32')
            elif R[c].dtype == 'bool':
                R[c] = R[c].astype('int8')
        R.to_parquet(bhgn / f'p{j:03d}.parquet', index=False)
        return len(R)

    out, n, j, jum = [], 0, 0, 0
    for tk, g in df.groupby('ticker', sort=False):
        if len(g) < 320:
            continue
        g = g.set_index('date')
        sek = peta.at[tk, 'sektor'] if tk in peta.index else 'Lain-lain'
        sx = si[sek].reindex(g.index) if sek in si.columns else None
        ind = I.kira(g, spy=spy.reindex(g.index).ffill(), sektor_idx=sx)
        a = ind[[c for c in DARI_IND if c in ind.columns]]
        b = tambahan(g)
        r = pd.concat([a, b], axis=1)
        r.insert(0, 'tutup', g['close'].to_numpy())
        r.insert(0, 'date', g.index)
        r.insert(0, 'ticker', tk)
        out.append(r.reset_index(drop=True))
        n += 1
        if len(out) >= 500:
            jum += _tulis(out, j)
            out, j = [], j + 1
            print(f'    [{time.time()-t0:.0f}s] {n} ticker | {jum:,} bar ditulis', flush=True)
    if out:
        jum += _tulis(out, j)
    del df
    R = pd.read_parquet(bhgn)
    CACHE.mkdir(exist_ok=True)
    R.to_parquet(PANEL, index=False)
    for old in bhgn.glob('*.parquet'):
        old.unlink()
    bhgn.rmdir()
    print(f'  [{time.time()-t0:.0f}s] panel dicache: {len(R):,} bar x {R.shape[1]} lajur',
          flush=True)
    return R


def _lag(a, n=1):
    return np.concatenate([np.full(n, np.nan), a[:-n]]) if n else a


def topeng(P):
    """70 topeng MASUK (spec §3 + §10). Dikunci: tiada pelarasan selepas keputusan dilihat."""
    f = {}
    for c in P.columns:
        if c not in ('ticker', 'date'):
            f[c] = P[c].to_numpy('float64')
    # lag per ticker: sempadan ticker ditanda supaya lag tidak melintas ticker
    tk = P.ticker.to_numpy()
    baru = np.concatenate([[True], tk[1:] != tk[:-1]])

    def L(nama, n=1):
        a = _lag(f[nama], n).copy()
        bad = baru.copy()
        for k in range(1, n):
            bad |= np.concatenate([[True] * (k + 1), tk[k + 1:] != tk[:-k - 1]])
        a[bad] = np.nan
        return a

    def silang(a, b):
        A, B = f[a], f[b]
        return (A > B) & (L(a) <= L(b))

    def naik(a, amb):
        return (f[a] > amb) & (L(a) <= amb)

    T = {}
    T['N06'] = silang('ma50', 'ma200')
    tiga = (f['ma10'] > f['ma20']) & (f['ma20'] > f['ma50'])
    T['N07'] = tiga & ~((L('ma10') > L('ma20')) & (L('ma20') > L('ma50')))
    T['N08'] = (f['tutup'] > f['ema20']) & ((f['tutup'] - f['ema20']) <= 1.5 * f['atr14'])
    T['N09'] = (f['tutup'] > f['ema10']) & (L('tutup') < L('ema10')) & (f['tutup'] > f['ema50'])
    T['N15'] = (f['rsi2'] < 10) & (f['tutup'] > f['ma200'])
    T['N16'] = f['rsi2'] < 10
    T['N17'] = naik('rsi14', 30)
    T['N18'] = (f['rsi14'] >= 30) & (f['rsi14'] <= 50) & (f['tutup'] > f['ma200'])
    T['N19'] = (f['bb_pctb'] < 0) & (f['rsi14'] < 30)
    T['N20'] = (L('bb_pctb') < 0) & (f['bb_pctb'] > 0) & naik('rsi14', 30)
    T['N21'] = (f['bb_pctb'] < 20) & (f['rsi14'] > 40)
    T['N22'] = (f['bb_pctb'] > 100) & (f['rsi14'] > 50)
    T['N23'] = (L('bb_squeeze') > 0) & (f['tutup'] > f['ema20'])
    T['N24'] = (f['supertrend'] > 0) & (f['adx14'] > 20)
    T['N25'] = (f['supertrend'] > 0) & (f['tutup'] > f['ema20']) & (f['adx14'] > 23)
    T['N27'] = (f['atas_awan'] > 0) & (f['tenkan_atas'] > 0)
    T['N28'] = (f['adx14'] > 25) & (f['mdi'] < f['adx14'])
    T['N29'] = (f['psar_arah'] > 0) & (f['tutup'] > f['ma50'])
    T['N31'] = f['donchian55'] > 0
    T['N33'] = (f['donchian20'] > 0) & (f['j_ma200'] > 0)
    T['N35'] = f['breakout_52w'] > 0
    T['N36'] = f['pocket_pivot'] > 0
    T['N37'] = f['gap_and_go'] > 0
    T['N38'] = f['vcp'] > 0
    T['N39'] = (L('nr7') > 0) & (f['donchian20'] > 0)
    T['N40'] = (f['obv_tinggi_baru'] > 0) & (f['tutup'] > f['ma50'])
    T['N41'] = (f['cmf20'] > 0) & (f['tutup'] > f['ema20'])
    T['N42'] = (f['vol_n50'] >= 2.0) & (f['tutup'] > L('tutup'))
    T['N43'] = (L('tutup') < L('ema9')) & (f['tutup'] > f['ema9']) & (f['tutup'] > f['ma50'])
    T['N44'] = ((f['tutup'] > f['ema21']) & (L('tutup') < L('ema21'))
                & (f['ema21'] > f['ma50']))
    T['N45'] = ((f['tutup'] > f['ema21']) & (f['cerun_ema21'] > 0)
                & (f['julat10'] < f['julat20']))
    T['N46'] = (L('rendah') <= L('ema21')) & (f['tutup'] > L('tinggi'))
    T['N47'] = (f['nr7'] > 0) & (f['ema9'] > f['ema21']) & (f['tutup'] > f['ema21'])
    T['N48'] = (L('inside_day') > 0) & (f['tutup'] > L('tinggi'))
    T['N49'] = (f['nr7'] > 0) & (f['inside_day'] > 0)
    T['N50'] = ((f['julat10'] < 0.5 * f['julat20']) & (f['vol_n50'] >= 1.5)
                & (f['tutup'] > L('tinggi')))
    T['N51'] = (f['bb_squeeze'] > 0) & (f['supertrend'] > 0)
    T['N52'] = (L('bb_squeeze') > 0) & (f['bb_lebar'] > L('bb_lebar')) & (f['j_ma200'] > 0)
    T['N53'] = (f['supertrend'] > 0) & (f['adx14'] > 25)
    T['N54'] = (f['supertrend'] > 0) & (f['rsi14'] > 50)
    T['N55'] = (f['bb_pctb'] < 20) & (f['rsi14'] > 40) & (f['adx14'] > 20)
    T['N56'] = (f['rsi14'] > 50) & (f['adx14'] > 20)
    T['N57'] = (f['adx14'] > 20) & (L('adx14') <= 20) & (f['tutup'] > f['ma50'])
    T['N58'] = silang('pdi', 'mdi') & (f['adx14'] > 20)
    T['N62'] = (f['julat20'] <= 0.08 * f['tutup']) & (f['tutup'] > f['tinggi20'])
    T['N64'] = (f['gap_and_go'] > 0) & (f['vol_n50'] >= 2.0)
    # UNIT: j_52w_tinggi dalam PERATUS (ind.py _pct), jadi -0.05 registry = -5.0 di sini
    T['N65'] = ((f['gap_and_go'] > 0) & (f['vol_n50'] >= 1.5) & (f['j_52w_tinggi'] >= -5.0))
    T['N66'] = f['tutup'] > 1.01 * f['tinggi_52w']
    T['N67'] = (f['hammer'] > 0) & (f['rendah'] <= f['ma50']) & (f['tutup'] > f['ma50'])
    T['N68'] = (f['bullish_engulfing'] > 0) & (f['tutup'] > f['ema21'])
    T['N69'] = (f['rs_pst'] >= 80) & (f['sektor_atas_ma50'] > 0)
    T['N70'] = f['garis_rs_tinggi'] > 0
    T['N73'] = f['tutup'] < (f['ma20'] - 2.0 * f['sd20'])
    T['N74'] = f['macd'] > f['macd_sig']
    T['N75'] = f['rsi14'] < 40
    T['N76'] = f['tutup'] > f['ma50']
    T['N80'] = f['tutup'] >= f['tinggi_sepanjang']
    for i, nm in enumerate(['Isn', 'Sel', 'Rab', 'Kha', 'Jum']):
        T[f'N104{nm}'] = f['hari_minggu'] == i
    T['N106'] = np.isin(f['bulan'], [11, 12, 1, 2, 3, 4])
    T['N113'] = (f['pos_buka'] <= 0.2) & (f['pos_tutup'] >= 0.8)
    T['N115'] = (f['adx14'] > 30) & (f['sentuh_ema20'] > 0) & (f['tutup'] > L('tinggi'))
    T['N116'] = (f['inside_day'] > 0) & (f['julat4_min'] > 0)
    T['N118'] = (f['tutup'] > f['ma200']) & (f['turun_4d5'] > 0)
    T['N119'] = (L('tutup', 2) > L('tutup')) & (L('tutup') > f['tutup'])
    T['N120'] = ((f['tutup'] > f['ma150']) & (f['tutup'] > f['ma200'])
                 & (f['ma150'] > f['ma200']) & (f['cerun_ma200_21'] > 0)
                 & (f['ma50'] > f['ma150']) & (f['ma50'] > f['ma200'])
                 & (f['tutup'] > f['ma50'])
                 & (f['tutup'] >= 1.30 * f['rendah_52w'])
                 & (f['tutup'] >= 0.75 * f['tinggi_52w']) & (f['rs_pst'] >= 70))
    T['N124'] = (f['gap'] >= 0.08) & (f['vol_n50'] >= 2.0)
    # SEMAKAN PEMALSUAN (spec §6): bukan hipotesis baharu, tidak dikira dalam FDR
    T['N01_semak'] = silang('ma10', 'ma20') & (f['vol_n50'] >= 1.2)
    return {k: np.nan_to_num(v, nan=0.0).astype(bool) for k, v in T.items()}


def t_kelompok(x, hari):
    """t dengan SE berkelompok ikut hari beli (spec §5 gate 2). Satu hujung."""
    ok = np.isfinite(x)
    if ok.sum() < MIN_N:
        return np.nan, np.nan, 0
    x, hari = x[ok], hari[ok]
    o = np.argsort(hari, kind='stable')
    x, hari = x[o], hari[o]
    sempadan = np.flatnonzero(np.concatenate([[True], hari[1:] != hari[:-1], [True]]))
    k = sempadan.size - 1
    if k < 20:
        return np.nan, np.nan, k
    km = np.add.reduceat(x, sempadan[:-1]) / np.diff(sempadan)
    se = km.std(ddof=1) / np.sqrt(k)
    if not np.isfinite(se) or se <= 0:
        return np.nan, np.nan, k
    t = float(x.mean() / se)
    from scipy import stats as sps
    return t, float(sps.t.sf(t, df=k - 1)), k


def metrik(pul):
    pul = pul[np.isfinite(pul)]
    if pul.size == 0:
        return dict(n=0, menang=np.nan, untung=np.nan, rugi=np.nan,
                    jangkaan=np.nan, tanpa5=np.nan)
    w = pul > 0
    u = np.sort(pul)[::-1]
    return dict(n=int(pul.size), menang=float(w.mean() * 100),
                untung=float(pul[w].mean() * 100) if w.any() else 0.0,
                rugi=float(pul[~w].mean() * 100) if (~w).any() else 0.0,
                jangkaan=float(pul.mean() * 100),
                tanpa5=float(u[int(np.ceil(0.05 * u.size)):].mean() * 100)
                if u.size > 20 else np.nan)


def bh_m(p, m, q=0.05):
    """BH-FDR dengan m DIPRADAFTAR (358), bukan bilangan p yang terhingga."""
    p = np.asarray(p, dtype='float64')
    lulus = np.zeros(p.size, dtype=bool)
    idx = np.flatnonzero(np.isfinite(p))
    if idx.size == 0:
        return lulus, np.nan
    srt = idx[np.argsort(p[idx])]
    amb = np.nan
    for i in range(srt.size - 1, -1, -1):
        if p[srt[i]] <= q * (i + 1) / m:
            amb = p[srt[i]]
            lulus[srt[:i + 1]] = True
            break
    return lulus, amb


M_PRADAFTAR = 358


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument('--laporan-sahaja', action='store_true')
    a = ap.parse_args(argv)
    t0 = time.time()
    csvp = KELUAR / 'nxx.csv'
    if a.laporan_sahaja and csvp.exists():
        H = pd.read_csv(csvp)
    else:
        print('1/4 panel indikator...', flush=True)
        P = bina_panel()
        print('2/4 gabung dengan cache keluar asas...', flush=True)
        pul = pd.read_parquet(PUL, columns=['ticker', 'date'] + [f'pul_{k}' for k in XK])
        P = P.merge(pul, on=['ticker', 'date'], how='inner')
        P = P[P.nilai20 >= CAIR].copy()
        P['tahun'] = P.date.dt.year
        P = P[(P.tahun >= TH0) & (P.tahun <= TH1)].sort_values(['ticker', 'date'])
        # persentil RS keratan rentas dalam tarikh (spec §10)
        P['rs_pst'] = P.groupby('date').rs_spy_6b.rank(pct=True) * 100.0
        print(f'  [{time.time()-t0:.0f}s] bar cair dengan pulangan: {len(P):,}', flush=True)
        print('3/4 topeng x 4 keluar x 2 tingkap...', flush=True)
        T = topeng(P)
        hari = P.date.to_numpy().astype('datetime64[D]').astype('int64')
        tahun = P.tahun.to_numpy()
        win = {'latih': (tahun >= LATIH[0]) & (tahun <= LATIH[1]),
               'tahan': (tahun >= TAHAN[0]) & (tahun <= TAHAN[1])}
        PU = {k: P[f'pul_{k}'].to_numpy('float64') for k in XK}
        asas = {(k, w): float(np.nanmean(PU[k][win[w]])) * 100 for k in XK for w in win}
        baris = []
        for nm, msk in T.items():
            for k in XK:
                r = {'masuk': nm, 'keluar': k}
                for w in win:
                    sel = msk & win[w]
                    mt = metrik(PU[k][sel])
                    r[f'n_{w}'] = mt['n']
                    r[f'jangkaan_{w}'] = mt['jangkaan']
                    r[f'tanpa5_{w}'] = mt['tanpa5']
                    r[f'lift_{w}'] = mt['jangkaan'] - asas[(k, w)]
                    if w == 'tahan':
                        r['menang'], r['untung'], r['rugi'] = (mt['menang'], mt['untung'],
                                                               mt['rugi'])
                        x = PU[k][sel] - asas[(k, w)] / 100.0
                        t, p, kk = t_kelompok(x, hari[sel])
                        r['t'], r['p'], r['n_hari'] = t, p, kk
                baris.append(r)
        H = pd.DataFrame(baris)
        for k in XK:
            for w in win:
                H.loc[H.keluar == k, f'asas_{w}'] = asas[(k, w)]
        H.to_csv(csvp, index=False)
        print(f'  [{time.time()-t0:.0f}s] {len(H)} ujian -> {csvp.name}', flush=True)
    # --- gate ---
    print('4/4 gate...', flush=True)
    semak = H.masuk == 'N01_semak'
    H['gate1'] = ((H.lift_latih > 0) & (H.lift_tahan > 0) & (H.n_tahan >= MIN_N)
                  & ~semak)
    lulus, amb = bh_m(H.p.where(H.gate1).to_numpy(), M_PRADAFTAR, 0.05)
    H['gate2'] = lulus
    H['gate3'] = H.gate2 & (H.tanpa5_tahan > 0)
    H = H.sort_values('lift_tahan', ascending=False)
    print(f"  gate1 {int(H.gate1.sum())}/{len(H)} | gate2 {int(H.gate2.sum())} "
          f"(ambang p {amb}) | gate3 {int(H.gate3.sum())}")
    print()
    # SEMAKAN PEMALSUAN DILAPOR DAHULU (spec §6)
    n01 = H[(H.masuk == 'N01_semak') & (H.keluar == 'X3')]
    print('=== SEMAKAN PEMALSUAN N01 (X3) — dibaca SEBELUM keputusan lain ===')
    if n01.empty:
        print('  GAGAL: topeng N01_semak tidak dijumpai')
    else:
        r = n01.iloc[0]
        dl, dt = r.lift_latih - 0.123, r.lift_tahan - 0.392
        ok = abs(dl) <= 0.02 and abs(dt) <= 0.02
        print(f'  lift latih {r.lift_latih:+.3f} (jangka +0.123, beza {dl:+.3f})')
        print(f'  lift tahan {r.lift_tahan:+.3f} (jangka +0.392, beza {dt:+.3f})')
        print(f'  n tahan {int(r.n_tahan):,} (jangka 28,117) | jangkaan tahan '
              f'{r.jangkaan_tahan:+.3f}% (jangka +2.988%)')
        print(f'  >>> {"LULUS" if ok else "GAGAL — alat tidak boleh dipercayai"}')
    print()
    lajur = ['masuk', 'keluar', 'n_tahan', 'lift_latih', 'lift_tahan', 'jangkaan_tahan',
             'tanpa5_tahan', 'p']
    print('=== 15 lift_tahan teratas yang lulus gate1 ===')
    print(H[H.gate1].head(15)[lajur].to_string(index=False) if H.gate1.any() else '  (tiada)')
    print()
    print('=== asas setiap keluar (beli SETIAP bar) ===')
    for k in XK:
        b = H[H.keluar == k].iloc[0]
        print(f'  {k}: latih {b.asas_latih:+.3f}%  tahan {b.asas_tahan:+.3f}%')
    return 0


if __name__ == '__main__':
    sys.exit(main())
