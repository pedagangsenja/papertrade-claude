"""Carian setup CS05 — peringkat LENGKAP (SPEC pindaan 14 Nov 2026 (j)): pegang + keluar + henti dipilih ikut kadar
tangkap yang DIREALISASI (`jadi` = dagangan dijual dengan R >= +10 %), bukan ikut purata R.

Guna (folder kerja: panel, benih, lapis, <pusingan>_pilihan.pkl sudah ada; CS_PUS=CS06 bagi pindaan (k)):
  python3 cs_lengkap.py asas  <kerja>    jadual asas rawak bagi SEMUA (henti x keluar), kumpulan A dan B
  python3 cs_lengkap.py pilih <kerja>    pilih (henti x keluar) pada kumpulan A; nilai pada A dan B -> <pusingan>_lengkap.pkl
Kemudian `python3 cs_cs05.py lapor <kerja>` menulis laporan dan registry F."""
import os
import pickle
import sys

import numpy as np
import pandas as pd
from numba import njit, prange

SINI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SINI)
import cs_atom as atom  # noqa: E402
import cs_cari as cari  # noqa: E402
import cs_teras as teras  # noqa: E402

JADI, RUGI = 0.10, -0.08                       # ambang dikunci pindaan (j)
K, NR = cari.K, cari.NR
KEP = 40000


@njit(parallel=True, cache=True)
def tambah_asas(Rm, g, m5, TJ, TR, TT):
    """TJ[g, lajur] += (R >= +10 %); TR[g, lajur] += (R <= -8 %); TT[g, lajur] += (R >= +10 % DAN naik >= 5 % minggu
    pertama). Selari ikut lajur (tiada perlumbaan)."""
    for j in prange(Rm.shape[1]):
        for k in range(Rm.shape[0]):
            v = Rm[k, j]
            if v >= 0.10:
                TJ[g[k], j] += 1
                if m5[k]:
                    TT[g[k], j] += 1
            elif v <= -0.08:
                TR[g[k], j] += 1


def _harga(pan):
    return pan['o'], pan['h'], pan['l'], pan['c'], pan['atr'], pan['X'], cari.JENIS, cari.PAR, cari.A1, cari.A2, cari.OP


def asas(kerja, set_):
    """Kadar `jadi`, `rugi8` dan `tp` (jadi DAN naik >= 5 % minggu pertama) semua bar layak setiap (hari x tercile ATR %)
    dan setiap (era x tercile), bagi SETIAP (henti x keluar). Simpan asasL_<set>.npz."""
    import cs_tangkap as tk
    pan = cari.panel(kerja, set_)
    ev = np.flatnonzero(pan['sah'])
    m5 = tk.label(ev, pan['o'], pan['l'], pan['c'])[:, 0] > 0
    hari = pan['hari'][ev]
    pct = pd.Series(pan['atr'][ev] / pan['c'][ev]).groupby(hari).rank(pct=True).to_numpy()
    terc = np.minimum((pct * 3).astype(np.int64), 2)
    g = hari * 3 + terc
    G = len(pan['hari_unik']) * 3
    TJ, TR, TT = np.zeros((G, K), np.uint16), np.zeros((G, K), np.uint16), np.zeros((G, K), np.uint16)
    for a in range(0, len(ev), KEP):
        tambah_asas(teras.hasil_semua(ev[a:a + KEP], *_harga(pan)), g[a:a + KEP], m5[a:a + KEP], TJ, TR, TT)
        if (a // KEP) % 20 == 0:
            cari.log(f'  asas {set_}: {a:,}/{len(ev):,}')
    n = np.bincount(g, minlength=G)
    era = pan['tempoh'][ev].astype(np.int64)
    ge = era * 3 + terc
    era_g = np.full(G, -1, np.int64)
    era_g[g] = ge
    nE = (int(era.max()) + 1) * 3
    ne = np.maximum(np.bincount(ge, minlength=nE), 1)[:, None]
    TJe = np.stack([TJ[era_g == x].sum(axis=0, dtype=np.float64) for x in range(nE)]) / ne
    TRe = np.stack([TR[era_g == x].sum(axis=0, dtype=np.float64) for x in range(nE)]) / ne
    TTe = np.stack([TT[era_g == x].sum(axis=0, dtype=np.float64) for x in range(nE)]) / ne
    gb, geb = np.full(len(pan['c']), -1, np.int32), np.full(len(pan['c']), -1, np.int32)
    gb[ev], geb[ev] = g, ge
    np.savez(os.path.join(kerja, f'asasL_{set_}.npz'), g=gb, ge=geb, n=n, TJ=TJ, TR=TR, TT=TT, TJe=TJe.astype(np.float32),
             TRe=TRe.astype(np.float32), TTe=TTe.astype(np.float32))
    cari.log(f'asas {set_} siap: {len(ev):,} bar; jadi X00/H1 semua bar = {TJ[:, 0].sum() / len(ev) * 100:.1f}%')


def muat_asas(kerja, set_):
    return dict(np.load(os.path.join(kerja, f'asasL_{set_}.npz')))


def pilih_lajur(pan, e, m5=None):
    """(henti x keluar) dengan min dua era bagi [kadar jadi - 2 ralat piawai] tertinggi; -1 jika n < 100 dalam satu era.
    m5 (bool setiap isyarat) diberi -> kadar tangkap penuh (jadi DAN naik >= 5 % minggu pertama), pindaan (k)."""
    tp = pan['tempoh'][e]
    J, N = np.zeros((2, K)), np.zeros(2)
    for a in range(0, len(e), KEP):
        jd = teras.hasil_semua(e[a:a + KEP], *_harga(pan)) >= JADI
        if m5 is not None:
            jd &= m5[a:a + KEP, None]
        for p in (0, 1):
            m = tp[a:a + KEP] == p
            J[p] += jd[m].sum(axis=0)
            N[p] += m.sum()
    if N.min() < cari.N_MIN:
        return -1
    pr = J / N[:, None]
    return int(np.argmax((pr - 2 * np.sqrt(pr * (1 - pr) / N[:, None])).min(axis=0)))


def nilai_l(pan, X, e, lajur, Tb):
    """Ukuran setup lengkap setiap tempoh (satu posisi setiap saham) + asas rawak dengan henti dan keluar yang sama."""
    s, r = divmod(int(lajur), NR)
    R, hp, sk = teras.hasil_satu(e, *_harga(pan), s, r)
    amb = teras.satu_posisi(e, sk, pan['tid'])
    e, R, hp = e[amb], R[amb], hp[amb]
    tp = pan['tempoh'][e]
    jd, rg, lr = R >= JADI, R <= RUGI, X[e, 4] > 0
    tpn = jd & (X[e, 0] > 0)                                # tangkap penuh dengan henti dan keluar setup ini sendiri
    g, ge = Tb['g'][e], Tb['ge'][e]
    ng = np.maximum(Tb['n'][g], 1)
    aj, ar, at = Tb['TJ'][g, lajur] / ng, Tb['TR'][g, lajur] / ng, Tb['TT'][g, lajur] / ng
    ej, er, et = Tb['TJe'][ge, lajur], Tb['TRe'][ge, lajur], Tb['TTe'][ge, lajur]
    out = {}
    for p in range(int(pan['tempoh'].max()) + 1):
        q = tp == p
        n = int(q.sum())
        d = {'n': n, 'hari': int(len(np.unique(pan['hari'][e[q]])))}
        if n:
            d.update(purata=float(R[q].mean()), menang=float((R[q] > 0).mean()), k10=float(jd[q].mean()),
                     rugi8=float(rg[q].mean()), pegang=float(hp[q].mean()), lari=float(lr[q].mean()),
                     n_lari=int((lr & q).sum()), k10_lari=float(jd[q & lr].mean()) if (q & lr).any() else np.nan,
                     a_k10=float(aj[q].mean()), a_rugi8=float(ar[q].mean()), e_k10=float(ej[q].mean()),
                     e_rugi8=float(er[q].mean()), tp=float(tpn[q].mean()), a_tp=float(at[q].mean()),
                     e_tp=float(et[q].mean()))
        out[p] = d
    return out


def pilih(kerja):
    import cs_cs05 as c5
    S = pickle.load(open(os.path.join(kerja, f'{c5.AWALAN}_pilihan.pkl'), 'rb'))
    P = S['P']
    P = P[P.peranan.str.startswith('papan_') | ((P.peranan == 'kelas') & P.kelas.isin(['S', 'P']))]
    lajur, L = {}, {k: {} for k in P.index}
    for set_ in ('A', 'B'):
        pan, _, EV, X, Lp = c5._sedia(kerja, set_)
        Tb = muat_asas(kerja, set_)
        T = [t[0] for t in atom.TEMPOH[set_]]
        Lr = (Lp['L1'], Lp['L2'])
        for i, (k, r) in enumerate(zip(P.index, P.itertuples())):
            if r.pencetus not in EV:
                continue
            e = EV[r.pencetus][c5.topeng(pan, Lr, EV[r.pencetus], r.q1, r.q2, r.f1, r.f2)]
            if set_ == 'A':                                      # CS05: ikut jadi (j); CS06: ikut tangkap penuh (k)
                lajur[k] = pilih_lajur(pan, e, X[e, 0] > 0 if c5.SASARAN == 'tp' else None)
            c = lajur.get(k, -1)
            if c < 0:
                continue
            uji = {'pilih': c, 'x00': (c // NR) * NR}
            if r.lajur >= 0:
                uji['lama'] = int(r.lajur)                       # (henti x keluar) pindaan (i): ikut purata R
            for nama, col in uji.items():
                L[k].setdefault(nama, {}).update(zip(T, nilai_l(pan, X, e, col, Tb).values()))
            if (i + 1) % 400 == 0:
                cari.log(f'  lengkap {set_}: {i + 1}/{len(P)}')
        del pan, EV, X, Lp, Tb
    pickle.dump({'lajur': lajur, 'L': L}, open(os.path.join(kerja, f'{c5.AWALAN}_lengkap.pkl'), 'wb'), protocol=4)
    ada = [c for c in lajur.values() if c >= 0]
    cari.log(f'lengkap siap: {len(ada)} peraturan masuk; X00 dipilih {sum(c % NR == 0 for c in ada)}; '
             f'henti ' + ' '.join(f'{atom.HENTI[s][:2]}={sum(c // NR == s for c in ada)}' for s in range(teras.NH)))


if __name__ == '__main__':
    if sys.argv[1] == 'asas':
        for s_ in ('A', 'B'):
            asas(sys.argv[2], s_)
    else:
        pilih(sys.argv[2])
