"""Paksi GABUNGAN — pradaftar `REVERSE/SPEC_GABUNGAN.md` (komit 86ad37e, §7 pindaan).

14 ujian: GB02 kesatuan (6), GB03 undi k-dari-n (3), GB04 agregat pangkat (4),
GB08 penapis terbalik (1). Semuanya pada keluar X3 daripada cache.

Guna: python3 REVERSE/step20_gabungan.py
Output: REVERSE/GABUNGAN.md, REVERSE/gabungan.csv
"""
import sys
import time
from pathlib import Path

import numpy as np
import pandas as pd

AKAR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(AKAR))
import REVERSE.step18_nxx as S18  # noqa: E402

KELUAR = AKAR / 'REVERSE'
LATIH, TAHAN = (2012, 2019), (2020, 2025)
CAIR, MIN_N = 100_000.0, 200
M_PRADAFTAR = 14
ASAS5_X3 = -2.303          # asas tanpa5 tahan X3, diukur dalam NXX.md §6

# kolam 12 signal, DITETAPKAN dalam spec §2 sebelum larian ini
KOLAM = ['N19', 'N37', 'N115', 'N20', 'N75', 'N64', 'N17', 'N42', 'N73', 'N16', 'N51', 'N54']


def konfig(T, skor_pst, buruk):
    """14 konfigurasi dipradaftar. Kunci -> topeng boolean."""
    M = [T[k] for k in KOLAM]
    C = {}
    for n in (2, 3, 4, 6, 8, 12):
        C[f'GB02_atau{n}'] = np.logical_or.reduce(M[:n])
    undi = np.add.reduce([m.astype('int8') for m in M])
    for k in (2, 3, 4):
        C[f'GB03_undi{k}'] = undi >= k
    for q in (1, 5, 10, 20):
        C[f'GB04_pangkat{q}'] = skor_pst >= (100 - q)
    C['GB08_buang_buruk'] = ~buruk
    return C


def main():
    t0 = time.time()
    rsf = S18.rs_persentil()
    kel = S18.kelompok_ticker()
    # --- pas 1: cari 12 MASUK dengan lift LATIH paling negatif (spec §7) ---
    H = pd.read_csv(KELUAR / 'nxx.csv')
    hx = H[(H.keluar == 'X3') & (H.masuk != 'N01_semak')].dropna(subset=['lift_latih'])
    BURUK = list(hx.nsmallest(12, 'lift_latih').masuk)
    print(f'GB08 buang (dipilih pada LATIH sahaja): {" ".join(BURUK)}', flush=True)
    AK, PERHARI = {}, {}
    print(f'1/2 {len(kel)} kelompok x 14 konfigurasi + asas...', flush=True)
    for i, bk in enumerate(kel):
        P = S18._sedia(bk, S18.PUL, rsf)
        T = S18.topeng(P)
        # skor agregat pangkat: purata pangkat persentil 12 signal dalam tarikh
        n = len(P)
        tanda = np.add.reduce([T[k].astype('float32') for k in KOLAM])
        d = pd.DataFrame({'date': P.date.to_numpy(), 's': tanda})
        skor_pst = d.groupby('date').s.rank(pct=True).to_numpy() * 100.0
        buruk = np.logical_or.reduce([T[k] for k in BURUK])
        C = konfig(T, skor_pst, buruk)
        C['ASAS'] = np.ones(n, bool)
        pu = P.pul_X3.to_numpy('float64')
        ada = np.isfinite(pu)
        th = P.date.dt.year.to_numpy()
        hari = P.date.to_numpy().astype('datetime64[D]').astype('int64')
        cair = P.nilai20.to_numpy() >= CAIR
        W = {'latih': (th >= LATIH[0]) & (th <= LATIH[1]) & cair,
             'tahan': (th >= TAHAN[0]) & (th <= TAHAN[1]) & cair}
        for nm, msk in C.items():
            for w, wm in W.items():
                sel = msk & wm & ada
                if not sel.any():
                    continue
                x = pu[sel]
                ak = AK.setdefault((nm, w), [0.0, 0, 0, 0.0, 0.0])
                ak[0] += float(x.sum()); ak[1] += int(x.size)
                pos = x > 0
                ak[2] += int(pos.sum()); ak[3] += float(x[pos].sum())
                ak[4] += float(x[~pos].sum())
                if w == 'tahan':
                    ph = PERHARI.setdefault(nm, {})
                    hh = hari[sel]
                    o = np.argsort(hh, kind='stable')
                    hs, xs = hh[o], x[o]
                    b = np.flatnonzero(np.concatenate([[True], hs[1:] != hs[:-1], [True]]))
                    for dd, sv, cv in zip(hs[b[:-1]], np.add.reduceat(xs, b[:-1]), np.diff(b)):
                        e = ph.get(dd)
                        if e is None:
                            ph[dd] = [sv, int(cv)]
                        else:
                            e[0] += sv; e[1] += int(cv)
        del P, T, C
        print(f'    [{time.time()-t0:.0f}s] kelompok {i+1}/{len(kel)}', flush=True)
    from scipy import stats as sps
    asas = {w: AK[('ASAS', w)][0] / AK[('ASAS', w)][1] * 100 for w in ('latih', 'tahan')}
    baris = []
    nama = sorted({k for k, _ in AK})
    for nm in nama:
        r = {'konfig': nm}
        for w in ('latih', 'tahan'):
            ak = AK.get((nm, w))
            if ak is None or ak[1] == 0:
                r[f'n_{w}'] = 0
                continue
            jg = ak[0] / ak[1] * 100
            r[f'n_{w}'] = ak[1]; r[f'jangkaan_{w}'] = jg
            r[f'lift_{w}'] = jg - asas[w]
            if w == 'tahan':
                r['menang'] = ak[2] / ak[1] * 100
                r['untung'] = ak[3] / ak[2] * 100 if ak[2] else np.nan
                nn = ak[1] - ak[2]
                r['rugi'] = ak[4] / nn * 100 if nn else np.nan
                ph = PERHARI.get(nm, {})
                if len(ph) >= 20:
                    km = np.array([v[0] / v[1] for v in ph.values()]) - asas[w] / 100
                    se = km.std(ddof=1) / np.sqrt(km.size)
                    t = float(km.mean() / se) if se > 0 else np.nan
                    r['t'] = t
                    r['p'] = float(sps.t.sf(t, df=km.size - 1)) if np.isfinite(t) else np.nan
                else:
                    r['t'] = r['p'] = np.nan
        baris.append(r)
    G = pd.DataFrame(baris)
    G['gate0'] = G.jangkaan_tahan > 0
    G['gate1'] = (G.gate0 & (G.lift_latih > 0) & (G.lift_tahan > 0)
                  & (G.n_tahan >= MIN_N) & (G.konfig != 'ASAS'))
    lulus, amb = S18.bh_m(G.p.where(G.gate1).to_numpy(), M_PRADAFTAR, 0.05)
    G['gate2'] = lulus
    # --- pas 2: ekor bagi yang lulus gate2 ---
    hidup = list(G[G.gate2].konfig)
    print(f'2/2 pas ekor bagi {len(hidup)}...', flush=True)
    kump = {k: [] for k in hidup}
    if hidup:
        for bk in kel:
            P = S18._sedia(bk, S18.PUL, rsf)
            T = S18.topeng(P)
            tanda = np.add.reduce([T[k].astype('float32') for k in KOLAM])
            d = pd.DataFrame({'date': P.date.to_numpy(), 's': tanda})
            skor_pst = d.groupby('date').s.rank(pct=True).to_numpy() * 100.0
            buruk = np.logical_or.reduce([T[k] for k in BURUK])
            C = konfig(T, skor_pst, buruk)
            th = P.date.dt.year.to_numpy()
            wm = (th >= TAHAN[0]) & (th <= TAHAN[1]) & (P.nilai20.to_numpy() >= CAIR)
            pu = P.pul_X3.to_numpy('float32')
            for nm in hidup:
                sel = C[nm] & wm & np.isfinite(pu)
                if sel.any():
                    kump[nm].append(pu[sel])
            del P, T, C
    G['tanpa5_tahan'] = np.nan
    for nm, lst in kump.items():
        if lst:
            u = np.sort(np.concatenate(lst))[::-1]
            G.loc[G.konfig == nm, 'tanpa5_tahan'] = (
                float(u[int(np.ceil(0.05 * u.size)):].mean() * 100) if u.size > 20 else np.nan)
    G['gate3'] = G.gate2 & (G.tanpa5_tahan > ASAS5_X3)
    G = G.sort_values('lift_tahan', ascending=False)
    G.to_csv(KELUAR / 'gabungan.csv', index=False)
    print(f'siap [{time.time()-t0:.0f}s] -> gabungan.csv')
    print(f"  gate0 {int(G[G.konfig!='ASAS'].gate0.sum())}/14 | gate1 {int(G.gate1.sum())} | "
          f"gate2 {int(G.gate2.sum())} (ambang p {amb}) | gate3 {int(G.gate3.sum())}")
    print(f"  asas X3: latih {asas['latih']:+.3f}%  tahan {asas['tahan']:+.3f}%  "
          f"tanpa5 tahan {ASAS5_X3:+.3f}%")
    print()
    lj = ['konfig', 'n_tahan', 'lift_latih', 'lift_tahan', 'jangkaan_tahan', 'menang',
          'tanpa5_tahan', 'p']
    print(G[lj].to_string(index=False))
    return 0


if __name__ == '__main__':
    sys.exit(main())
