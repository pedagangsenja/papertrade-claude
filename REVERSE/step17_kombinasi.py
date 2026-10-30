"""Gabungan daripada laman web dan forum — pradaftar `REVERSE/SPEC_KOMBINASI.md`.

Permintaan pengguna 30 Okt 2026: kaji apa yang pedagang sebenar guna, uji GABUNGAN mereka.
Setiap peraturan dinamakan dengan sumbernya; saya menguji peraturan SUMBER, bukan tafsiran saya.

Yang benar-benar baharu di sini: `ma10 x ma20` (diminta khusus, memang tiada dalam 71 lajur
sedia ada) dan **SASARAN UNTUNG** — kajian ini belum pernah menguji sasaran, hanya henti,
ufuk tetap dan ekor.

Guna: python3 REVERSE/step17_kombinasi.py [--laporan-sahaja]
Output: REVERSE/KOMBINASI.md, REVERSE/kombinasi.csv
"""
import argparse
import sys
from pathlib import Path

import numpy as np
import pandas as pd

AKAR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(AKAR))
from REVERSE.teras import kos as K  # noqa: E402

KELUAR = AKAR / 'REVERSE'
CACHE = KELUAR / '.cache'
HARGA = AKAR / 'AUTOTUNE' / '.cache_autotune-data-a02'
PUL = CACHE / 'pul_kombinasi.parquet'

TH0, TH1 = 2012, 2025
LATIH, TAHAN = (2012, 2019), (2020, 2025)
ATR_N, UFUK, IMBAS = 14, 63, 126
CAIR = 100_000.0
MIN_N = 200

# Keluar yang SUMBER tetapkan (spec §4): (henti x ATR, sasaran x ATR atau None, ufuk atau None)
XKELUAR = {'X1': (1.5, 1.0, None), 'X2': (2.0, 4.0, None),
           'X3': (2.0, None, UFUK), 'X4': (2.0, 'ekor', None)}


def _wilder(x, n):
    return pd.Series(x).ewm(alpha=1 / n, adjust=False, min_periods=n).mean().to_numpy()


def siri_ticker(g):
    """Semua indikator + 4 pulangan keluar bagi setiap bar satu ticker."""
    o = g.open.to_numpy('float64')
    h = g.high.to_numpy('float64')
    lo = g.low.to_numpy('float64')
    c = g.close.to_numpy('float64')
    v = g.volume.to_numpy('float64')
    m = len(c)
    cs, vs = pd.Series(c), pd.Series(v)
    pc = cs.shift(1)
    tr = np.maximum(h - lo, np.maximum((h - pc).abs(), (lo - pc).abs()))
    atr = _wilder(tr, ATR_N)
    d = {}
    # --- indikator BAHARU (spec §2) ---
    for n in (10, 20, 50, 200):
        d[f'ma{n}'] = cs.rolling(n).mean().to_numpy()
    for n in (20, 50):
        d[f'ema{n}'] = cs.ewm(span=n, adjust=False, min_periods=n).mean().to_numpy()
    d['sma100'] = cs.rolling(100).mean().to_numpy()
    # RSI14 Wilder + SMA14 RSI
    dl = cs.diff()
    up = _wilder(dl.clip(lower=0).to_numpy(), ATR_N)
    dn = _wilder((-dl.clip(upper=0)).to_numpy(), ATR_N)
    rs = up / (dn + 1e-12)
    d['rsi14'] = 100 - 100 / (1 + rs)
    d['rsi_sma14'] = pd.Series(d['rsi14']).rolling(ATR_N).mean().to_numpy()
    ema12 = cs.ewm(span=12, adjust=False, min_periods=12).mean().to_numpy()
    ema26 = cs.ewm(span=26, adjust=False, min_periods=26).mean().to_numpy()
    d['macd'] = ema12 - ema26
    d['vol_n50'] = v / (vs.rolling(50, min_periods=50).mean().to_numpy() + 1e-12)
    d['cerun_ma50'] = pd.Series(d['ma50']).diff(5).to_numpy()
    d['atrp'] = atr / np.where(c > 0, c, np.nan) * 100
    d['nilai20'] = (cs * vs).rolling(20, min_periods=10).median().to_numpy()
    d['tutup'] = c

    def silang(a, b):
        A, B = d[a], d[b]
        pa, pb = np.concatenate([[np.nan], A[:-1]]), np.concatenate([[np.nan], B[:-1]])
        return ((A > B) & (pa <= pb)).astype('float32')

    d['x_ma10_ma20'] = silang('ma10', 'ma20')
    d['x_ma20_ma50'] = silang('ma20', 'ma50')
    d['x_ma20_ma200'] = silang('ma20', 'ma200')
    d['x_ema20_ema50'] = silang('ema20', 'ema50')
    d['x_rsi_sma'] = silang('rsi14', 'rsi_sma14')

    # --- pulangan 4 keluar, lingkaran offset tervektor ---
    idx = np.arange(m)
    masuk = np.concatenate([o[1:], [np.nan]])
    ks = K.KOMISEN + np.array([K.slippage(x) for x in d['nilai20']])
    for kod, (hx, sx, uf) in XKELUAR.items():
        paras_h = masuk - hx * atr
        paras_s = (masuk + sx * atr) if isinstance(sx, float) else None
        lebar_t = hx * atr if sx == 'ekor' else None
        bar = np.full(m, -1)
        px = np.full(m, np.nan)
        puncak = np.where(np.isfinite(masuk), masuk, -np.inf)
        had = uf if uf else IMBAS
        for j in range(1, had + 1):
            kk = np.minimum(idx + j, m - 1)
            sah = (idx + j) < m
            if paras_s is not None:
                kena_s = sah & (bar < 0) & (h[kk] >= paras_s)
                bar[kena_s], px[kena_s] = kk[kena_s], paras_s[kena_s]
            kena_h = sah & (bar < 0) & (lo[kk] <= paras_h)
            bar[kena_h], px[kena_h] = kk[kena_h], paras_h[kena_h]
            if lebar_t is not None:
                ck = np.where(sah, c[kk], np.nan)
                puncak = np.where(sah & np.isfinite(ck), np.maximum(puncak, ck), puncak)
                kena_t = sah & (bar < 0) & np.isfinite(ck) & (ck < puncak - lebar_t)
                bar[kena_t] = kk[kena_t]
                px[kena_t] = np.where(kk + 1 < m, o[np.minimum(kk + 1, m - 1)], c[m - 1])[kena_t]
        belum = bar < 0
        bk = np.minimum(idx + had + 1, m - 1)
        bar[belum], px[belum] = bk[belum], o[bk][belum]
        with np.errstate(invalid='ignore', divide='ignore'):
            d[f'pul_{kod}'] = (px * (1 - ks)) / (masuk * (1 + ks)) - 1.0
    out = pd.DataFrame({k: v for k, v in d.items()})
    out.insert(0, 'date', g.date.to_numpy())
    out.insert(0, 'ticker', g.ticker.iloc[0])
    return out


def bina():
    """Panel indikator + 4 pulangan keluar bagi setiap bar. Cache sekali."""
    if PUL.exists():
        return pd.read_parquet(PUL)
    bhg = []
    for y in range(TH0 - 2, TH1 + 1):
        p = HARGA / f'harga_{y}.parquet'
        if p.exists():
            bhg.append(pd.read_parquet(p, columns=['ticker', 'date', 'open', 'high', 'low',
                                                   'close', 'volume']))
    df = pd.concat(bhg, ignore_index=True)
    df = df[df.date <= pd.Timestamp(f'{TH1}-12-31')].sort_values(['ticker', 'date'])
    out, n = [], 0
    for _, g in df.groupby('ticker', sort=False):
        if len(g) < 260:
            continue
        out.append(siri_ticker(g))
        n += 1
        if n % 500 == 0:
            print(f'    {n} ticker', flush=True)
    R = pd.concat(out, ignore_index=True)
    for c in R.columns:
        if R[c].dtype == 'float64':
            R[c] = R[c].astype('float32')
    CACHE.mkdir(exist_ok=True)
    R.to_parquet(PUL, index=False)
    print(f'  dicache: {len(R):,} bar -> {PUL.name}')
    return R


def gabungan(d):
    """10 gabungan MASUK, setiap satu dengan sumbernya (spec §3). Dikunci."""
    f = {c: d[c].to_numpy('float64') for c in
         ('ema20', 'ema50', 'rsi14', 'macd', 'vol_n50', 'tutup', 'cerun_ma50', 'ma50', 'sma100')}
    x = {c: d[c].fillna(0).to_numpy().astype(bool) for c in
         ('x_ma10_ma20', 'x_ma20_ma50', 'x_ma20_ma200', 'x_ema20_ema50', 'x_rsi_sma')}
    ema_atas = f['ema20'] > f['ema50']
    G = {}
    G['K1 ema20>ema50 & rsi 50-70'] = ema_atas & (f['rsi14'] >= 50) & (f['rsi14'] <= 70)
    G['K2 ema20>ema50 & rsi<=30 & macd>0 & vol>=1.5'] = (
        ema_atas & (f['rsi14'] <= 30) & (f['macd'] > 0) & (f['vol_n50'] >= 1.5))
    G['K3 tutup>ema20 & ma50 naik & rsi 40-60'] = (
        (f['tutup'] > f['ema20']) & (f['cerun_ma50'] > 0)
        & (f['rsi14'] >= 40) & (f['rsi14'] <= 60))
    G['K4 rsi 40-50 & tutup>ma50'] = (
        (f['rsi14'] >= 40) & (f['rsi14'] <= 50) & (f['tutup'] > f['ma50']))
    G['K5 ma10 silang ma20 & vol>=1.2'] = x['x_ma10_ma20'] & (f['vol_n50'] >= 1.2)
    G['K6 ma20 silang ma50'] = x['x_ma20_ma50']
    G['K7 rsi14 silang SMA14(rsi)'] = x['x_rsi_sma']
    G['K8 tutup>ema20>sma100 & vol>=1.2'] = (
        (f['tutup'] > f['ema20']) & (f['ema20'] > f['sma100']) & (f['vol_n50'] >= 1.2))
    G['K9 ma20 silang ma200'] = x['x_ma20_ma200']
    G['K10 K1 & vol>=1.5'] = G['K1 ema20>ema50 & rsi 50-70'] & (f['vol_n50'] >= 1.5)
    return G


def metrik(pul):
    pul = pul[np.isfinite(pul)]
    if pul.size == 0:
        return dict(n=0)
    w = pul > 0
    u = np.sort(pul)[::-1]
    return dict(n=int(pul.size), menang=float(w.mean() * 100),
                untung=float(pul[w].mean() * 100) if w.any() else 0.0,
                rugi=float(pul[~w].mean() * 100) if (~w).any() else 0.0,
                jangkaan=float(pul.mean() * 100),
                tanpa5=float(u[int(np.ceil(0.05 * u.size)):].mean() * 100)
                if u.size > 20 else np.nan)


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument('--laporan-sahaja', action='store_true')
    a = ap.parse_args(argv)
    f = KELUAR / 'kombinasi.csv'
    if a.laporan_sahaja and f.exists():
        return laporan(pd.read_csv(f))
    print('1/3 panel + 4 keluar setiap bar...', flush=True)
    d = bina()
    d['tahun'] = pd.to_datetime(d.date).dt.year
    d = d[(d.tahun >= TH0) & (d.tahun <= TH1) & (d.nilai20 >= CAIR)].reset_index(drop=True)
    print(f'  {len(d):,} bar cair', flush=True)
    print('2/3 10 gabungan masuk...', flush=True)
    G = gabungan(d)
    print('3/3 40 kombinasi x 2 tingkap + asas...', flush=True)
    baris = []
    for tw, (y0, y1) in (('latih', LATIH), ('tahan', TAHAN)):
        mt = ((d.tahun >= y0) & (d.tahun <= y1)).to_numpy()
        for kod in XKELUAR:
            pul = d[f'pul_{kod}'].to_numpy('float64')
            asas = metrik(pul[mt])
            baris.append(dict(masuk='ASAS beli setiap bar', keluar=kod, tingkap=tw, **asas,
                              lift=0.0))
            for nm, ada in G.items():
                r = metrik(pul[ada & mt])
                r['lift'] = r.get('jangkaan', np.nan) - asas['jangkaan']
                baris.append(dict(masuk=nm, keluar=kod, tingkap=tw, **r))
        print(f'  {tw} siap', flush=True)
    R = pd.DataFrame(baris)
    R.to_csv(f, index=False)
    return laporan(R)


def laporan(R):
    A = R[R.masuk.str.startswith('ASAS')]
    G = R[~R.masuk.str.startswith('ASAS')]
    p = G.pivot_table(index=['masuk', 'keluar'], columns='tingkap',
                      values=['jangkaan', 'lift', 'n', 'menang', 'tanpa5']).reset_index()
    p.columns = ['_'.join(c).strip('_') for c in p.columns]
    p['lulus'] = ((p.get('lift_latih', 0) > 0) & (p.get('lift_tahan', 0) > 0)
                  & (p.get('n_tahan', 0) >= MIN_N) & (p.get('tanpa5_tahan', 0) > 0))
    lulus = p[p.lulus.fillna(False)]

    L = ['# Gabungan daripada laman web dan forum: diuji', '']
    L.append(f'Dijana {pd.Timestamp.now(tz="UTC"):%Y-%m-%d %H:%M} UTC oleh '
             '`REVERSE/step17_kombinasi.py`. Pradaftar `REVERSE/SPEC_KOMBINASI.md`.')
    L.append('')
    L.append(f'## Keputusan: **{"LULUS " + str(len(lulus)) if len(lulus) else "DITOLAK"}**')
    L.append('')
    L.append('10 gabungan yang pedagang sebenar guna × 4 peraturan keluar yang **sumber itu '
             'sendiri tetapkan** = 40 kombinasi. Dua daripada keluar itu mempunyai **sasaran '
             'untung**, yang kajian ini belum pernah uji.')
    L.append('')
    L.append('### Asas: beli SETIAP bar, ikut peraturan keluar')
    L.append('')
    L.append('| Keluar | Peraturan | Jangkaan latih | Jangkaan tahan | Menang tahan |')
    L.append('|---|---|---|---|---|')
    ket = {'X1': 'henti 1.5×ATR, sasaran 1×ATR', 'X2': 'henti 2×ATR, sasaran 4×ATR',
           'X3': 'henti 2×ATR, 63 sesi', 'X4': 'ekori 2×ATR'}
    for kod in XKELUAR:
        la = A[(A.keluar == kod) & (A.tingkap == 'latih')]
        ta = A[(A.keluar == kod) & (A.tingkap == 'tahan')]
        if len(la) and len(ta):
            L.append(f'| `{kod}` | {ket[kod]} | {la.jangkaan.iloc[0]:+.3f}% | '
                     f'{ta.jangkaan.iloc[0]:+.3f}% | {ta.menang.iloc[0]:.1f}% |')
    L.append('')
    L.append('**Setiap peraturan keluar mempunyai kadar asas yang berbeza**, jadi lift mesti '
             'dikira terhadap asas keluar yang SAMA. Itu pembetulan kepada kesilapan '
             '`SPEC_SETUP.md` §4 saya.')
    L.append('')
    return laporan2(L, p, A, lulus, ket)


def laporan2(L, p, A, lulus, ket):
    L.append('## 40 kombinasi — lift atas asas keluar yang sama')
    L.append('')
    L.append('| Masuk | Keluar | n tahan | Menang | Jangkaan tahan | **Lift latih** | '
             '**Lift tahan** | Lulus |')
    L.append('|---|---|---|---|---|---|---|---|')
    for _, r in p.sort_values('lift_tahan', ascending=False).iterrows():
        L.append(f'| {r.masuk} | `{r.keluar}` | {r.get("n_tahan", 0):,.0f} | '
                 f'{r.get("menang_tahan", float("nan")):.1f}% | '
                 f'{r.get("jangkaan_tahan", float("nan")):+.3f}% | '
                 f'{r.get("lift_latih", float("nan")):+.3f} | '
                 f'**{r.get("lift_tahan", float("nan")):+.3f}** | '
                 f'{"**YA**" if r.lulus else "tidak"} |')
    L.append('')
    n_pos_t = int((p.lift_tahan > 0).sum())
    n_pos_l = int((p.lift_latih > 0).sum())
    L.append(f'Lift POSITIF: **{n_pos_l} daripada {len(p)}** pada latih, '
             f'**{n_pos_t} daripada {len(p)}** pada tahan, '
             f'**{len(lulus)}** pada kedua-duanya + syarat n dan ekor.')
    L.append('')
    L.append('## Tafsiran')
    L.append('')
    if len(lulus):
        L.append(f'**{len(lulus)} kombinasi lulus.** Jangkaan priori saya (spec §7: lift negatif '
                 'pada kesemua 40) **SALAH**.')
        L.append('')
        for _, r in lulus.iterrows():
            L.append(f'- **{r.masuk}** dengan `{r.keluar}` ({ket[r.keluar]}): n '
                     f'{r.n_tahan:,.0f}, jangkaan {r.jangkaan_tahan:+.3f}%, lift latih '
                     f'{r.lift_latih:+.3f} dan tahan {r.lift_tahan:+.3f}, jangkaan tanpa 5% '
                     f'teratas {r.tanpa5_tahan:+.3f}%')
        L.append('')
        L.append('**Ini belum bermakna ia mengalahkan SPUS.** Lift positif bermakna ia '
                 'mengalahkan "beli setiap bar dengan keluar yang sama" — ujian yang berbeza '
                 'dan lebih rendah. Langkah seterusnya ialah membina portfolio daripadanya dan '
                 'membandingkan dengan SPUS, seperti Gate C dalam `SILANG_GATE_C.md`.')
    else:
        L.append('**Tiada kombinasi lulus.** Jangkaan priori saya tepat kali ini.')
        L.append('')
        L.append('Sebabnya sama seperti `SETUP.md`: setiap gabungan ini ialah **penapis**, dan '
                 'menapis membuang bar — termasuk bar yang membawa pemenang besar.')
    L.append('')
    # Kesan sasaran untung — bahagian yang benar-benar baharu
    L.append('## Kesan SASARAN UNTUNG (yang belum pernah diuji)')
    L.append('')
    asas_t = {k: float(A[(A.keluar == k) & (A.tingkap == 'tahan')].jangkaan.iloc[0])
              for k in XKELUAR if len(A[(A.keluar == k) & (A.tingkap == 'tahan')])}
    if 'X3' in asas_t:
        L.append('| Keluar | Jangkaan asas tahan | Beza dari `X3` (tiada sasaran) |')
        L.append('|---|---|---|')
        for k in ('X3', 'X1', 'X2', 'X4'):
            if k in asas_t:
                L.append(f'| `{k}` {ket[k]} | {asas_t[k]:+.3f}% | '
                         f'{asas_t[k] - asas_t["X3"]:+.3f} |')
        L.append('')
        buruk = min(asas_t, key=asas_t.get)
        L.append(f'Keluar terburuk: `{buruk}` ({ket[buruk]}). Keluar terbaik: '
                 f'`{max(asas_t, key=asas_t.get)}`.')
        L.append('')
        if asas_t.get('X1', 0) < asas_t['X3'] and asas_t.get('X2', 0) < asas_t['X3']:
            L.append('**Kedua-dua sasaran untung merugikan.** Sasaran 1×ATR dan 4×ATR '
                     'kedua-duanya memberi jangkaan LEBIH RENDAH daripada tiada sasaran. Itu '
                     'dapatan `KOLAM_EKOR.md` lagi: memotong pemenang pada paras tetap '
                     'membuang ekor kanan, dan ekor kanan itulah yang membayar.')
            L.append('')
            L.append('Ini menjawab soalan yang sumber forum tidak pernah uji: **mengambil '
                     'untung pada 1×ATR atau 4×ATR adalah lebih buruk daripada tidak '
                     'mengambil untung sama sekali.**')
            L.append('')
    L.append('## Had')
    L.append('')
    L.append('- Sumber forum dan blog **tiada bukti bebas** tentang kelebihan. Menguji mereka '
             'bermakna menguji cadangan, bukan mengesahkan dakwaan yang sudah disahkan.')
    L.append('- Peraturan sumber **tidak diseragamkan**; versi yang diuji dinyatakan penuh dalam '
             '`SPEC_KOMBINASI.md` §3 dan §4.')
    L.append('- Lift positif ≠ mengalahkan SPUS. Ia hanya bermakna mengalahkan "beli setiap bar '
             'dengan keluar yang sama".')
    L.append('- Alam `autotune-data-a02`, bukan ditapis Syariah.')
    L.append('')
    (KELUAR / 'KOMBINASI.md').write_text('\n'.join(L), encoding='utf-8')
    c = ['masuk', 'keluar', 'n_tahan', 'jangkaan_tahan', 'lift_latih', 'lift_tahan', 'lulus']
    print('\n' + p.sort_values('lift_tahan', ascending=False)[c].head(14).round(3).to_string(index=False))
    print(f'\nlift positif: latih {int((p.lift_latih > 0).sum())}/{len(p)} | '
          f'tahan {int((p.lift_tahan > 0).sum())}/{len(p)} | LULUS {len(lulus)}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
