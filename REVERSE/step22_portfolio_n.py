"""Kajian 1 — portfolio `GB02_atau3/4 × X13/X15` lawan SPUS. Pradaftar `REVERSE/SPEC_PORTFOLIO_N.md`.

3 masuk x 2 slot x 2 keluar x 3 urutan = 36 konfigurasi; U01 20 benih -> 264 larian simulasi.
Enjin portfolio diguna semula daripada `REVERSE/pembinaan.py` supaya tiada enjin kedua.
Topeng isyarat datang daripada `REVERSE/step18_nxx.topeng()` — satu sumber kebenaran.

Guna: python3 REVERSE/step22_portfolio_n.py [--benih 20] [--laporan-sahaja]
Output: REVERSE/PORTFOLIO_N.md, REVERSE/portfolio_n.csv
"""
import argparse
import sys
import time
from pathlib import Path

import numpy as np
import pandas as pd

AKAR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(AKAR))
import REVERSE.pembinaan as PB  # noqa: E402
import REVERSE.step18_nxx as S18  # noqa: E402
from REVERSE.teras import kos as K  # noqa: E402

KELUAR = AKAR / 'REVERSE'
CACHE = KELUAR / '.cache'
SIGF = CACHE / 'sig_gb02.parquet'
RSPF = CACHE / 'rs_pst_nxx.parquet'

UJI0, UJI1 = '2020-01-01', '2025-12-31'
LATIH0, LATIH1 = '2012-01-01', '2019-12-31'
HAD_IMBAS = 504          # spec §3.3 — had imbasan keluar
RSI_KELUAR = 70.0        # X13
TRAIL_ATR = 4.0          # X15
N_BENIH = 20
AMBANG_NISBAH = 0.669    # spec §3.4 P4 (SISTEM.md)

MASUK = ['GB02_atau3', 'GB02_atau4', 'RAWAK']
SLOT = [8, 40]
RULE = ['X13', 'X15']
URUT = ['U01', 'U02', 'U08']
KOLAM3 = ['N19', 'N37', 'N115']
KOLAM4 = KOLAM3 + ['N20']


# ---------------------------------------------------------------- prasedia
def bina_isyarat():
    """(ticker, date, a3, a4) bagi setiap bar yang mana-mana signal kolam benar."""
    if SIGF.exists():
        return pd.read_parquet(SIGF)
    rsf = S18.rs_persentil()
    kel = S18.kelompok_ticker()
    out, t0 = [], time.time()
    for i, bk in enumerate(kel):
        P = S18._sedia(bk, S18.PUL, rsf)
        T = S18.topeng(P)
        a3 = np.logical_or.reduce([T[k] for k in KOLAM3])
        a4 = np.logical_or.reduce([T[k] for k in KOLAM4])
        sel = a3 | a4
        if sel.any():
            out.append(pd.DataFrame({'ticker': P.ticker.to_numpy()[sel],
                                     'date': P.date.to_numpy()[sel],
                                     'a3': a3[sel], 'a4': a4[sel]}))
        del P, T
        print(f'    [{time.time() - t0:.0f}s] isyarat kelompok {i + 1}/{len(kel)}', flush=True)
    d = pd.concat(out, ignore_index=True)
    CACHE.mkdir(parents=True, exist_ok=True)
    d.to_parquet(SIGF, index=False)
    return d


def _matriks(P, fail, lajur):
    """Matriks ticker x tarikh bagi satu lajur, dialirkan ikut kelompok ticker."""
    import pyarrow.parquet as pq
    it = {t: i for i, t in enumerate(P.tick)}
    idt = {d: i for i, d in enumerate(P.tarikh)}
    M = np.full((len(P.tick), len(P.tarikh)), np.nan, 'float32')
    for bk in S18.kelompok_ticker():
        x = pq.read_table(fail, columns=['ticker', 'date', lajur],
                          filters=[('ticker', 'in', set(bk))]).to_pandas()
        x = x[x.ticker.isin(it)]
        if x.empty:
            continue
        ii = x.ticker.map(it).to_numpy()
        jj = np.array([idt.get(d, -1) for d in x.date.to_numpy()])
        ok = jj >= 0
        M[ii[ok], jj[ok]] = x[lajur].to_numpy('float32')[ok]
        del x
    return M


def peta_layak(P):
    """LAYAK[a] = indeks ticker yang boleh dimasuki pada sauh a (beli buka a+1)."""
    m = len(P.tarikh)
    out = {}
    for a in range(m - 1):
        ok = (np.isfinite(P.C[:, a]) & np.isfinite(P.A[:, a]) &
              np.isfinite(P.N[:, a]) & (P.N[:, a] >= PB.CAIR) &
              np.isfinite(P.O[:, a + 1]) & (P.O[:, a + 1] > 0))
        idx = np.flatnonzero(ok)
        if idx.size:
            out[a] = idx.astype('int64')
    return out


# ---------------------------------------------------------------- keluar
def keluar(P, RSI, ti, a, rule, cache):
    """(idx_keluar, harga_masuk, harga_keluar). Masuk buka a+1; keluar buka bar BERIKUTNYA."""
    kunci = (ti, a, rule)
    if kunci in cache:
        return cache[kunci]
    e = a + 1
    akhir = len(P.tarikh) - 1
    masuk = float(P.O[ti, e])
    hi = min(e + HAD_IMBAS, akhir)

    def harga_pada(k):
        if k <= akhir and np.isfinite(P.O[ti, k]) and P.O[ti, k] > 0:
            return int(k), float(P.O[ti, k])
        sah = np.flatnonzero(np.isfinite(P.C[ti, e:akhir + 1]))
        k2 = e + int(sah[-1]) if sah.size else e
        return k2, float(P.C[ti, k2])

    if rule == 'X13':
        w = RSI[ti, e:hi + 1]
        kena = np.flatnonzero(np.isfinite(w) & (w > RSI_KELUAR))
    else:                                     # X15 Chandelier 4xATR14
        atr = float(P.A[ti, a])
        c = P.C[ti, e:hi + 1].astype('float64')
        sah = np.isfinite(c)
        puncak = np.maximum.accumulate(np.where(sah, c, -np.inf))
        kena = np.flatnonzero(sah & (c < puncak - TRAIL_ATR * atr))
    bar = e + int(kena[0]) if kena.size else hi
    k, px = harga_pada(min(bar + 1, akhir))
    hasil = (k, masuk, px)
    cache[kunci] = hasil
    return hasil


# ---------------------------------------------------------------- simulasi
def simulasi(P, RSI, ATRP, RSP, CAL, slot, rule, urut, benih):
    """Ekuiti harian, pendedahan harian dan bilangan dagangan bagi satu larian."""
    rng = np.random.default_rng(benih)
    m = len(P.tarikh)
    cache = {}
    tunai, prev, n_dag = 1.0, 1.0, 0
    buka = []                                  # (ti, unit, idx_keluar, px_keluar)
    ek = np.full(m, np.nan)
    dz = np.full(m, np.nan)
    for d in range(1, m):
        if buka:
            for p in [x for x in buka if x[2] == d]:
                tunai += p[1] * p[3] * (1 - K.kos_sisi(P.N[p[0], d]))
                buka.remove(p)
        a = d - 1
        cal = CAL.get(a)
        if cal is not None and cal.size and len(buka) < slot:
            if urut == 'U01':
                cal = cal[rng.permutation(cal.size)]
            elif urut == 'U02':
                cal = cal[np.argsort(-np.nan_to_num(RSP[cal, a], nan=-1.0), kind='stable')]
            else:
                cal = cal[np.argsort(np.nan_to_num(ATRP[cal, a], nan=9e9), kind='stable')]
            pegang = {x[0] for x in buka}
            for t in cal:
                if len(buka) >= slot:
                    break
                ti = int(t)
                if ti in pegang:
                    continue
                belanja = min(prev / slot, tunai)
                if belanja <= 1e-12:
                    break
                kx, _, pkeluar = keluar(P, RSI, ti, a, rule, cache)
                if kx <= d:
                    continue
                unit = belanja * (1 - K.kos_sisi(P.N[ti, a])) / float(P.O[ti, d])
                tunai -= belanja
                buka.append((ti, unit, kx, pkeluar))
                pegang.add(ti)
                n_dag += 1
        nilai = tunai
        for ti, unit, _, _ in buka:
            c = P.C[ti, d]
            if np.isfinite(c):
                nilai += unit * float(c)
        ek[d] = prev = nilai
        dz[d] = 1.0 - (tunai / nilai if nilai > 0 else 1.0)
    return ek, dz, n_dag


# ---------------------------------------------------------------- larian
def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument('--benih', type=int, default=N_BENIH)
    ap.add_argument('--laporan-sahaja', action='store_true')
    a = ap.parse_args(argv)
    f = KELUAR / 'portfolio_n.csv'
    if a.laporan_sahaja and f.exists():
        return laporan(pd.read_csv(f))

    t0 = time.time()
    print('1/5 isyarat GB02...', flush=True)
    S = bina_isyarat()
    print(f'  {len(S):,} bar berisyarat  [{time.time() - t0:.0f}s]', flush=True)

    print('2/5 panel harga...', flush=True)
    P = PB.Panel()
    print(f'  {len(P.tick):,} ticker x {len(P.tarikh):,} sesi  [{time.time() - t0:.0f}s]',
          flush=True)

    print('3/5 matriks rsi14 + rs_pst...', flush=True)
    RSI = _matriks(P, S18.PANEL, 'rsi14')
    S18.rs_persentil()
    RSP = _matriks(P, RSPF, 'rs_pst')
    ATRP = P.A / np.where(P.C > 0, P.C, np.nan)
    print(f'  siap  [{time.time() - t0:.0f}s]', flush=True)

    print('4/5 calon setiap sauh...', flush=True)
    LAYAK = peta_layak(P)
    it = {t: i for i, t in enumerate(P.tick)}
    idt = {d: i for i, d in enumerate(P.tarikh)}
    S = S[S.ticker.isin(it)]
    ii = S.ticker.map(it).to_numpy()
    jj = np.array([idt.get(d, -1) for d in S.date.to_numpy()])
    ok = jj >= 0
    ii, jj = ii[ok], jj[ok]
    CAL = {'RAWAK': LAYAK}
    for nama, msk in (('GB02_atau3', S.a3.to_numpy()[ok]), ('GB02_atau4', S.a4.to_numpy()[ok])):
        d = {}
        o = np.argsort(jj[msk], kind='stable')
        js, iss = jj[msk][o], ii[msk][o]
        b = np.flatnonzero(np.concatenate([[True], js[1:] != js[:-1], [True]]))
        for s, e in zip(b[:-1], b[1:]):
            aa = int(js[s])
            lay = LAYAK.get(aa)
            if lay is None:
                continue
            v = np.intersect1d(iss[s:e], lay, assume_unique=False)
            if v.size:
                d[aa] = v.astype('int64')
        CAL[nama] = d
        print(f'  {nama}: {sum(v.size for v in d.values()):,} calun layak merentas '
              f'{len(d):,} sesi', flush=True)

    hari = pd.DatetimeIndex(P.tarikh)
    m0 = int(np.searchsorted(P.tarikh, np.datetime64(UJI0)))
    l0 = int(np.searchsorted(P.tarikh, np.datetime64(LATIH0)))
    l1 = int(np.searchsorted(P.tarikh, np.datetime64(LATIH1)))

    print('5/5 simulasi...', flush=True)
    baris = []
    for mk in MASUK:
        for slot in SLOT:
            for rule in RULE:
                for urut in URUT:
                    for b in (range(1, a.benih + 1) if urut == 'U01' else [0]):
                        ek, dz, nd = simulasi(P, RSI, ATRP, RSP, CAL[mk],
                                              slot, rule, urut, b)
                        baris.append(dict(
                            masuk=mk, slot=slot, keluar=rule, urutan=urut, benih=b,
                            cagr=PB.cagr(ek[m0:], hari[m0:]), mdd=PB.mdd(ek[m0:]),
                            dedah=float(np.nanmean(dz[m0:]) * 100), n_dagangan=nd,
                            cagr_latih=PB.cagr(ek[l0:l1], hari[l0:l1]),
                            mdd_latih=PB.mdd(ek[l0:l1])))
                    print(f'  {mk} slot{slot} {rule} {urut}: siap '
                          f'[{time.time() - t0:.0f}s]', flush=True)
    R = pd.DataFrame(baris)
    R.to_csv(f, index=False, float_format='%.4f')
    return laporan(R)


def laporan(R):
    pa = PB.penanda_aras()
    sp_c, sp_m, _ = pa['SPUS']
    g = (R.groupby(['masuk', 'slot', 'keluar', 'urutan'])
          .agg(cagr=('cagr', 'median'), mdd=('mdd', 'median'),
               cagr_p5=('cagr', lambda x: float(np.percentile(x, 5))),
               cagr_p95=('cagr', lambda x: float(np.percentile(x, 95))),
               dedah=('dedah', 'median'), n=('n_dagangan', 'median'),
               cagr_latih=('cagr_latih', 'median'), mdd_latih=('mdd_latih', 'median'),
               nb=('benih', 'size')).reset_index())
    g['nisbah'] = g.cagr / g.mdd.abs()
    ctl = {(r.slot, r.keluar, r.urutan): r.cagr_p95
           for r in g[g.masuk == 'RAWAK'].itertuples()}
    g['ctl_p95'] = [ctl.get((r.slot, r.keluar, r.urutan), np.nan) for r in g.itertuples()]
    g['P1'] = g.cagr > sp_c
    g['P2'] = g.mdd >= sp_m
    g['P3'] = np.where(g.masuk == 'RAWAK', False, g.cagr > g.ctl_p95)
    g['P4'] = g.nisbah > AMBANG_NISBAH
    g['lulus'] = g.P1 & g.P2 & g.P3 & g.P4
    g = g.sort_values('cagr', ascending=False)
    g.to_csv(KELUAR / 'portfolio_n_ringkas.csv', index=False, float_format='%.4f')
    print()
    print(f'SPUS 2020-2025: CAGR {sp_c:.2f}%  MDD {sp_m:.2f}%  nisbah {sp_c / abs(sp_m):.3f}')
    print(f'gate: P1 {int(g.P1.sum())}  P2 {int(g.P2.sum())}  P3 {int(g.P3.sum())}  '
          f'P4 {int(g.P4.sum())}  ->  LULUS SEMUA {int(g.lulus.sum())} / {len(g)}')
    print()
    kol = ['masuk', 'slot', 'keluar', 'urutan', 'nb', 'cagr', 'cagr_p5', 'cagr_p95',
           'mdd', 'nisbah', 'dedah', 'n', 'P1', 'P2', 'P3', 'P4']
    print(g[kol].to_string(index=False, float_format=lambda v: f'{v:.2f}'))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
