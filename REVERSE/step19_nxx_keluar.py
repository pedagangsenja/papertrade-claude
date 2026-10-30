"""Ujian registry Nxx bahagian B — 23 KELUAR x 3 masuk tetap = 69 ujian.

Pradaftar `REVERSE/SPEC_NXX.md` §3 + pembetulan §11 (komit 5acbd15). Gate 0 (jangkaan mutlak
tahan > 0) ditambah dalam §11 selepas bahagian A mendedahkan N16 x X1 lulus dengan jangkaan
negatif.

Keluar disimulasi di sini (lingkaran offset tervektor, sama gaya step17) kerana cache
`pul_kombinasi.parquet` hanya ada 4 keluar asas.

Guna: python3 REVERSE/step19_nxx_keluar.py
Output: REVERSE/NXX_KELUAR.md, REVERSE/nxx_keluar.csv
"""
import sys
import time
from pathlib import Path

import numpy as np
import pandas as pd

AKAR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(AKAR))
from REVERSE.teras import kos as K  # noqa: E402
import REVERSE.step18_nxx as S18  # noqa: E402

KELUAR = AKAR / 'REVERSE'
CACHE = KELUAR / '.cache'
TH0, TH1 = 2012, 2025
LATIH, TAHAN = (2012, 2019), (2020, 2025)
CAIR, MIN_N, IMBAS = 100_000.0, 200, 126
M_PRADAFTAR = 349

# 23 keluar (spec §11). Setiap satu: fungsi(ctx) -> (bar_keluar, harga_keluar)
# ctx memberi o/h/l/c/atr + lajur indikator sejajar, dan `masuk` = buka bar+1.
XSPEC = [
    ('X05', 'keluar bila tutup > jalur tengah BB(20) = ma20'),
    ('X07', 'keluar bila rsi2 > 60'),
    ('X08', 'keluar bila rsi2 > 80'),
    ('X09', 'keluar bila rsi2 > 65'),
    ('X10', 'sasaran untung 2% tetap'),
    ('X12', 'henti pada jalur bawah BB(20,2)'),
    ('X13', 'keluar bila rsi14 > 70'),
    ('X14', 'keluar bila rsi14 silang naik 50'),
    ('X15', 'ekori Chandelier 4 x ATR14'),
    ('X16', 'keluar bila supertrend berbalik'),
    ('X17', 'keluar bila adx14 < 20'),
    ('X18', 'henti pada rendah 20 hari'),
    ('X19', 'keluar bila tutup < ema21'),
    ('X25', 'henti 1% bawah ema21'),
    ('X26', 'ekori 4% peratus tetap'),
    ('X27', 'sasaran limit +3%'),
    ('X28', 'sasaran +4% atau tutup < ma50'),
    ('X29', 'pegang tetap 10 bar'),
    ('X30', 'keluar bila macd < macd_sig'),
    ('X33', 'keluar pada tutup sesi masuk'),
    ('X36', 'keluar selepas DUA tutup bawah ma50'),
    ('X37', 'henti bawah rendah hari masuk; gagal jika tutup < buka hari masuk'),
    ('X41', 'henti pada rendah hari masuk'),
]


def pulangan_keluar(P):
    """Pulangan setiap bar bagi 23 keluar. Satu lingkaran offset, semua keluar serentak."""
    o = P.buka.to_numpy('float64')
    h = P.tinggi.to_numpy('float64')
    lo = P.rendah.to_numpy('float64')
    c = P.tutup.to_numpy('float64')
    atr = P.atr14.to_numpy('float64')
    tk = P.ticker.to_numpy()
    m = len(c)
    akhir = np.concatenate([tk[1:] != tk[:-1], [True]])      # bar terakhir setiap ticker
    idx = np.arange(m)
    nxt = np.where(akhir, np.nan, np.concatenate([o[1:], [np.nan]]))
    masuk = nxt
    # PEPIJAT 1 (asap): o[kk+1] boleh jatuh pada ticker SETERUSNYA. Pada bar terakhir
    # setiap ticker, guna tutup bar itu sebagai harga keluar, bukan buka ticker lain.
    buka_next = np.where(akhir, c, np.concatenate([o[1:], [np.nan]]))
    ks = K.KOMISEN + np.array([K.slippage(x) for x in P.nilai20.to_numpy('float64')])
    ind = {k: P[k].to_numpy('float64') for k in
           ('ma20', 'sd20', 'rsi2', 'rsi14', 'supertrend', 'adx14', 'ema21', 'ma50',
            'macd', 'macd_sig')}
    # PEPIJAT 2 (asap): rolling mesti per-ticker, bukan merentas frame bergabung
    rl20 = P.groupby('ticker', sort=False).rendah.rolling(20).min().to_numpy()
    kod = [k for k, _ in XSPEC]
    bar = {k: np.full(m, -1) for k in kod}
    px = {k: np.full(m, np.nan) for k in kod}
    puncak = np.where(np.isfinite(masuk), masuk, -np.inf)
    bawah2 = np.zeros(m)                                     # kiraan tutup bawah ma50 (X36)
    # had: ticker berakhir -> hentikan
    hidup_akhir = idx.copy()
    for j in range(1, IMBAS + 1):
        kk = np.minimum(idx + j, m - 1)
        sah = ((idx + j) < m) & (tk[np.minimum(idx + j, m - 1)] == tk)
        ck, hk, lk = np.where(sah, c[kk], np.nan), np.where(sah, h[kk], np.nan), np.where(sah, lo[kk], np.nan)
        bk = buka_next[kk]

        def tetap(k, kena, harga):
            a, p = bar[k], px[k]
            kn = sah & (a < 0) & kena
            a[kn], p[kn] = kk[kn], harga[kn] if hasattr(harga, '__len__') else harga

        tetap('X05', ck > ind['ma20'][kk], bk)
        tetap('X07', ind['rsi2'][kk] > 60, bk)
        tetap('X08', ind['rsi2'][kk] > 80, bk)
        tetap('X09', ind['rsi2'][kk] > 65, bk)
        sas2 = masuk * 1.02
        tetap('X10', hk >= sas2, sas2)
        jb = ind['ma20'][kk] - 2.0 * ind['sd20'][kk]
        tetap('X12', lk <= jb, jb)
        tetap('X13', ind['rsi14'][kk] > 70, bk)
        tetap('X14', (ind['rsi14'][kk] > 50) & (ind['rsi14'][np.maximum(kk - 1, 0)] <= 50), bk)
        puncak = np.where(sah & np.isfinite(ck), np.maximum(puncak, ck), puncak)
        tetap('X15', np.isfinite(ck) & (ck < puncak - 4.0 * atr), bk)
        tetap('X16', ind['supertrend'][kk] <= 0, bk)
        tetap('X17', ind['adx14'][kk] < 20, bk)
        tetap('X18', lk <= rl20[kk], rl20[kk])
        tetap('X19', ck < ind['ema21'][kk], bk)
        h25 = ind['ema21'][kk] * 0.99
        tetap('X25', lk <= h25, h25)
        tetap('X26', np.isfinite(ck) & (ck < puncak * 0.96), bk)
        sas3 = masuk * 1.03
        tetap('X27', hk >= sas3, sas3)
        sas4 = masuk * 1.04
        tetap('X28', hk >= sas4, sas4)
        tetap('X28', ck < ind['ma50'][kk], bk)
        tetap('X29', np.full(m, j >= 10), bk)
        tetap('X30', ind['macd'][kk] < ind['macd_sig'][kk], bk)
        tetap('X33', np.full(m, j >= 1), np.where(sah, ck, np.nan))
        bawah2 = np.where(sah & (ck < ind['ma50'][kk]), bawah2 + 1, 0.0)
        tetap('X36', bawah2 >= 2, bk)
        # PEPIJAT 3 (asap): henti pada rendah HARI MASUK tercetus pada hari masuk itu
        # sendiri (lo <= lo selalu benar) -> kadar menang 0.0%. Disemak dari j>=2.
        h37 = np.where(np.isfinite(masuk), lo[np.minimum(idx + 1, m - 1)], np.nan)
        if j >= 2:
            tetap('X37', lk <= h37, h37)
            tetap('X41', lk <= h37, h37)
        hidup_akhir = np.where(sah, kk, hidup_akhir)
    out = {}
    for k in kod:
        a, p = bar[k], px[k]
        belum = a < 0
        a[belum] = hidup_akhir[belum]
        p[belum] = buka_next[a[belum]]
        with np.errstate(invalid='ignore', divide='ignore'):
            out[k] = (p * (1 - ks)) / (masuk * (1 + ks)) - 1.0
    return out


def main():
    t0 = time.time()
    rsf = S18.rs_persentil()
    kel = S18.kelompok_ticker()
    kod = [k for k, _ in XSPEC]
    MASUK3 = ['N115', 'N19', 'ASAS']
    AK, PERHARI = {}, {}
    print(f'1/3 {len(kel)} kelompok x 23 keluar x 3 masuk...', flush=True)
    for i, bk in enumerate(kel):
        P = S18._sedia(bk, S18.PUL, rsf)
        T = S18.topeng(P)
        PU = pulangan_keluar(P)
        th = P.date.dt.year.to_numpy()
        hari = P.date.to_numpy().astype('datetime64[D]').astype('int64')
        cair = P.nilai20.to_numpy() >= CAIR
        W = {'latih': (th >= LATIH[0]) & (th <= LATIH[1]) & cair,
             'tahan': (th >= TAHAN[0]) & (th <= TAHAN[1]) & cair}
        msk = {'N115': T['N115'], 'N19': T['N19'], 'ASAS': np.ones(len(P), bool)}
        for k in kod:
            pu = PU[k]
            ada = np.isfinite(pu)
            for w, wm in W.items():
                for nm in MASUK3:
                    sel = msk[nm] & wm & ada
                    if not sel.any():
                        continue
                    x = pu[sel]
                    ak = AK.setdefault((nm, k, w), [0.0, 0, 0, 0.0, 0.0])
                    ak[0] += float(x.sum()); ak[1] += int(x.size)
                    pos = x > 0
                    ak[2] += int(pos.sum()); ak[3] += float(x[pos].sum())
                    ak[4] += float(x[~pos].sum())
                    if w == 'tahan':
                        ph = PERHARI.setdefault((nm, k), {})
                        hh = hari[sel]
                        o = np.argsort(hh, kind='stable')
                        hs, xs = hh[o], x[o]
                        b = np.flatnonzero(np.concatenate([[True], hs[1:] != hs[:-1], [True]]))
                        sm, cn = np.add.reduceat(xs, b[:-1]), np.diff(b)
                        for d, sv, cv in zip(hs[b[:-1]], sm, cn):
                            e = ph.get(d)
                            if e is None:
                                ph[d] = [sv, int(cv)]
                            else:
                                e[0] += sv; e[1] += int(cv)
        del P, T, PU
        print(f'    [{time.time()-t0:.0f}s] kelompok {i+1}/{len(kel)}', flush=True)
    from scipy import stats as sps
    asas = {(k, w): (AK[('ASAS', k, w)][0] / AK[('ASAS', k, w)][1] * 100)
            for k in kod for w in ('latih', 'tahan') if ('ASAS', k, w) in AK}
    baris = []
    for nm in MASUK3:
        for k in kod:
            r = {'masuk': nm, 'keluar': k,
                 'peraturan': dict(XSPEC)[k]}
            for w in ('latih', 'tahan'):
                ak = AK.get((nm, k, w))
                if ak is None or ak[1] == 0:
                    r[f'n_{w}'] = 0
                    continue
                jg = ak[0] / ak[1] * 100
                r[f'n_{w}'] = ak[1]; r[f'jangkaan_{w}'] = jg
                r[f'lift_{w}'] = jg - asas[(k, w)]
                if w == 'tahan':
                    r['menang'] = ak[2] / ak[1] * 100
                    r['untung'] = ak[3] / ak[2] * 100 if ak[2] else np.nan
                    nn = ak[1] - ak[2]
                    r['rugi'] = ak[4] / nn * 100 if nn else np.nan
                    ph = PERHARI.get((nm, k), {})
                    if len(ph) >= 20:
                        km = np.array([v[0] / v[1] for v in ph.values()]) - asas[(k, w)] / 100
                        se = km.std(ddof=1) / np.sqrt(km.size)
                        t = float(km.mean() / se) if se > 0 else np.nan
                        r['t'] = t
                        r['p'] = float(sps.t.sf(t, df=km.size - 1)) if np.isfinite(t) else np.nan
                    else:
                        r['t'] = r['p'] = np.nan
            r['asas_latih'] = asas.get((k, 'latih'), np.nan)
            r['asas_tahan'] = asas.get((k, 'tahan'), np.nan)
            baris.append(r)
    H = pd.DataFrame(baris)
    H['gate0'] = H.jangkaan_tahan > 0
    H['gate1'] = (H.gate0 & (H.lift_latih > 0) & (H.lift_tahan > 0) & (H.n_tahan >= MIN_N)
                  & (H.masuk != 'ASAS'))
    lulus, amb = S18.bh_m(H.p.where(H.gate1).to_numpy(), M_PRADAFTAR, 0.05)
    H['gate2'] = lulus
    print(f'2/3 pas ekor bagi {int(H.gate2.sum())} yang lulus gate2...', flush=True)
    hidup = sorted(set(H[H.gate2][['masuk', 'keluar']].itertuples(index=False, name=None)))
    kump = {kk: [] for kk in hidup}
    if hidup:
        for i, bk in enumerate(kel):
            P = S18._sedia(bk, S18.PUL, rsf)
            T = S18.topeng(P)
            PU = pulangan_keluar(P)
            th = P.date.dt.year.to_numpy()
            wm = ((th >= TAHAN[0]) & (th <= TAHAN[1]) & (P.nilai20.to_numpy() >= CAIR))
            msk = {'N115': T['N115'], 'N19': T['N19'], 'ASAS': np.ones(len(P), bool)}
            for nm, k in hidup:
                pu = PU[k].astype('float32')
                sel = msk[nm] & wm & np.isfinite(pu)
                if sel.any():
                    kump[(nm, k)].append(pu[sel])
            del P, T, PU
    H['tanpa5_tahan'] = np.nan
    for (nm, k), lst in kump.items():
        if lst:
            u = np.sort(np.concatenate(lst))[::-1]
            H.loc[(H.masuk == nm) & (H.keluar == k), 'tanpa5_tahan'] = (
                float(u[int(np.ceil(0.05 * u.size)):].mean() * 100) if u.size > 20 else np.nan)
    H['gate3'] = H.gate2 & (H.tanpa5_tahan > 0)
    H = H.sort_values('lift_tahan', ascending=False)
    H.to_csv(KELUAR / 'nxx_keluar.csv', index=False)
    print(f'3/3 siap [{time.time()-t0:.0f}s] -> nxx_keluar.csv')
    print(f"  gate0 {int(H[H.masuk!='ASAS'].gate0.sum())}/46 | gate1 {int(H.gate1.sum())} | "
          f"gate2 {int(H.gate2.sum())} (ambang p {amb}) | gate3 {int(H.gate3.sum())}")
    print()
    print('=== asas setiap keluar (tiada penapis), tahan ===')
    A = H[H.masuk == 'ASAS'].sort_values('jangkaan_tahan', ascending=False)
    print(A[['keluar', 'peraturan', 'n_tahan', 'jangkaan_tahan', 'menang']].to_string(index=False))
    print()
    print('=== 20 teratas lift_tahan (N115 / N19) ===')
    lj = ['masuk', 'keluar', 'n_tahan', 'lift_latih', 'lift_tahan', 'jangkaan_tahan',
          'menang', 'tanpa5_tahan', 'p']
    print(H[H.masuk != 'ASAS'].head(20)[lj].to_string(index=False))
    return 0


if __name__ == '__main__':
    sys.exit(main())
