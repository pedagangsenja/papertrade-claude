"""Silang masuk-terbaik x keluar-terbaik — pradaftar `REVERSE/SPEC_SILANG_AKHIR.md` (568a13f).

2 masuk (GB02_atau3, GB02_atau4) x 4 keluar (X3, X13, X15, X17) = 8 ujian.
X3 daripada cache; X13/X15/X17 disimulasi oleh step19.

Guna: python3 REVERSE/step21_silang_akhir.py
Output: REVERSE/SILANG_AKHIR.md, REVERSE/silang_akhir.csv
"""
import sys
import time
from pathlib import Path

import numpy as np
import pandas as pd

AKAR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(AKAR))
import REVERSE.step18_nxx as S18  # noqa: E402
import REVERSE.step19_nxx_keluar as S19  # noqa: E402
from REVERSE.step20_gabungan import KOLAM  # noqa: E402

KELUAR = AKAR / 'REVERSE'
LATIH, TAHAN = (2012, 2019), (2020, 2025)
CAIR, MIN_N, M_PRADAFTAR = 100_000.0, 200, 8
XK = ['X3', 'X13', 'X15', 'X17']
MASUK = ['GB02_atau3', 'GB02_atau4']


def main():
    t0 = time.time()
    rsf = S18.rs_persentil()
    kel = S18.kelompok_ticker()
    AK, PERHARI, EKOR = {}, {}, {}
    print(f'1/2 {len(kel)} kelompok x 2 masuk x 4 keluar...', flush=True)
    for i, bk in enumerate(kel):
        P = S18._sedia(bk, S18.PUL, rsf)
        T = S18.topeng(P)
        PU19 = S19.pulangan_keluar(P)
        pul = {'X3': P.pul_X3.to_numpy('float64')}
        for k in ('X13', 'X15', 'X17'):
            pul[k] = PU19[k]
        M = [T[k] for k in KOLAM]
        msk = {'GB02_atau3': np.logical_or.reduce(M[:3]),
               'GB02_atau4': np.logical_or.reduce(M[:4]),
               'ASAS': np.ones(len(P), bool)}
        th = P.date.dt.year.to_numpy()
        hari = P.date.to_numpy().astype('datetime64[D]').astype('int64')
        cair = P.nilai20.to_numpy() >= CAIR
        W = {'latih': (th >= LATIH[0]) & (th <= LATIH[1]) & cair,
             'tahan': (th >= TAHAN[0]) & (th <= TAHAN[1]) & cair}
        for k in XK:
            pu = pul[k]
            ada = np.isfinite(pu)
            for w, wm in W.items():
                for nm, mk in msk.items():
                    sel = mk & wm & ada
                    if not sel.any():
                        continue
                    x = pu[sel]
                    ak = AK.setdefault((nm, k, w), [0.0, 0, 0, 0.0, 0.0])
                    ak[0] += float(x.sum()); ak[1] += int(x.size)
                    pos = x > 0
                    ak[2] += int(pos.sum()); ak[3] += float(x[pos].sum())
                    ak[4] += float(x[~pos].sum())
                    if w == 'tahan':
                        EKOR.setdefault((nm, k), []).append(x.astype('float32'))
                        ph = PERHARI.setdefault((nm, k), {})
                        hh = hari[sel]
                        o = np.argsort(hh, kind='stable')
                        hs, xs = hh[o], x[o]
                        b = np.flatnonzero(np.concatenate([[True], hs[1:] != hs[:-1], [True]]))
                        for dd, sv, cv in zip(hs[b[:-1]], np.add.reduceat(xs, b[:-1]),
                                              np.diff(b)):
                            e = ph.get(dd)
                            if e is None:
                                ph[dd] = [sv, int(cv)]
                            else:
                                e[0] += sv; e[1] += int(cv)
        del P, T, PU19, pul
        print(f'    [{time.time()-t0:.0f}s] kelompok {i+1}/{len(kel)}', flush=True)
    from scipy import stats as sps

    def tanpa5(lst):
        u = np.sort(np.concatenate(lst))[::-1]
        return float(u[int(np.ceil(0.05 * u.size)):].mean() * 100) if u.size > 20 else np.nan

    asas = {(k, w): AK[('ASAS', k, w)][0] / AK[('ASAS', k, w)][1] * 100
            for k in XK for w in ('latih', 'tahan')}
    asas5 = {k: tanpa5(EKOR[('ASAS', k)]) for k in XK}
    baris = []
    for nm in MASUK + ['ASAS']:
        for k in XK:
            r = {'masuk': nm, 'keluar': k}
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
                    r['tanpa5'] = tanpa5(EKOR[(nm, k)])
                    r['asas5'] = asas5[k]
                    r['tanpa5_lawan_asas'] = r['tanpa5'] - asas5[k]
                    ph = PERHARI.get((nm, k), {})
                    if len(ph) >= 20:
                        km = np.array([v[0] / v[1] for v in ph.values()]) - asas[(k, w)] / 100
                        se = km.std(ddof=1) / np.sqrt(km.size)
                        t = float(km.mean() / se) if se > 0 else np.nan
                        r['t'] = t
                        r['p'] = float(sps.t.sf(t, df=km.size - 1)) if np.isfinite(t) else np.nan
            r['asas_latih'] = asas[(k, 'latih')]
            r['asas_tahan'] = asas[(k, 'tahan')]
            baris.append(r)
    S = pd.DataFrame(baris)
    S['gate0'] = S.jangkaan_tahan > 0
    S['gate1'] = (S.gate0 & (S.lift_latih > 0) & (S.lift_tahan > 0) & (S.n_tahan >= MIN_N)
                  & (S.masuk != 'ASAS'))
    lulus, amb = S18.bh_m(S.p.where(S.gate1).to_numpy(), M_PRADAFTAR, 0.05)
    S['gate2'] = lulus
    S['gate3'] = S.gate2 & (S.tanpa5 > S.asas5)
    S = S.sort_values('jangkaan_tahan', ascending=False)
    S.to_csv(KELUAR / 'silang_akhir.csv', index=False)
    print(f'siap [{time.time()-t0:.0f}s]')
    print(f"  gate1 {int(S.gate1.sum())}/8 | gate2 {int(S.gate2.sum())} (ambang {amb}) | "
          f"gate3 {int(S.gate3.sum())}")
    print()
    lj = ['masuk', 'keluar', 'n_tahan', 'lift_latih', 'lift_tahan', 'jangkaan_tahan', 'menang',
          'untung', 'rugi', 'tanpa5', 'asas5', 'tanpa5_lawan_asas', 'p', 'gate3']
    print(S[lj].to_string(index=False))
    return 0


if __name__ == '__main__':
    sys.exit(main())
