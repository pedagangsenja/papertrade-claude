"""CS25 (pindaan 20 Nov 2026 (al)): STOP LOSS x PEGANG x JUAL bagi SETIAP setup F, ikut untung terbesar.

Setiap kod dalam `data/registry_F.csv` dinilai dengan 4,320 cara (8 stop loss x 2 "naikkan stop loss ke harga beli" x 3 pegang
minimum x 15 "trend tamat" x 3 "jual separuh semasa naik" x 2 had masa). Peraturan masuk tidak diubah; isyarat beli dalam mod
tanpa intai. Pemilihan pada kumpulan A (saham carian), bacaan pada kumpulan B (saham yang carian tidak lihat).

Guna: python3 cs_keluar25.py kira <kerja> | kawalan <kerja> | pariti <kerja> | lapor <kerja>
Folder kerja perlukan panel_A/B, lapis_A/B, cs07_K_A/B dan benih_A/B.pkl tanpa intai (SERAHAN_CARIAN_SETUP.md par. 9v).
"""
import itertools
import json
import os
import resource
import sys
import time

import numpy as np
import pandas as pd
from numba import njit, prange

SINI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SINI)
import cs_cari as cari  # noqa: E402
import cs_teras as teras  # noqa: E402

PUS = 'CS25'
KOS = teras.KOS
BESAR = 32767
DMAX = 251                                               # indeks sesi terakhir yang dinilai (had masa terpanjang 252 sesi)
# ---- enam komponen (dikunci pindaan (al)) ----
STOP = ('s2', 's3', 's4', 's6', 'p8', 'p15', 'c3', 'c4')
S_JENIS = np.array([0, 0, 0, 0, 1, 1, 2, 2], np.int64)    # 0 = k x ATR14 sentuhan dalam hari; 1 = peratus; 2 = k x ATR14 ikut tutup
S_NILAI = np.array([2.0, 3.0, 4.0, 6.0, 0.08, 0.15, 3.0, 4.0])
BE = ('b0', 'b1')
BE_ATR = 2.0
MIN = (3, 10, 20)
MIN_A = np.array(MIN, np.int64)
TREND = tuple(f't{i}' for i in range(15))
SMA_N = (10, 20, 50, 100)
CH_K = np.array([3.0, 4.0, 6.0, 8.0])
LL_N = (10, 20)
JATUH = np.array([0.85, 0.75])
JUAL = ('j0', 'j1', 'j2')
J_NAIK = np.array([1.10, 1.20])
HAD = (126, 252)
NS_, NB, NM, NT, NJ, NH = len(STOP), len(BE), len(MIN), len(TREND), len(JUAL), len(HAD)
NT1, NJ1 = NT - 1, NJ - 1
_GRID = list(itertools.product(range(NS_), range(NB), range(NM), range(NT), range(NJ), range(NH)))
SW, BW, MW, TW, JW = (np.array([g[i] for g in _GRID], np.int64) for i in range(5))
HW = np.array([HAD[g[5]] for g in _GRID], np.int64)
W = len(_GRID)
assert W == 4320
KOD = [f'{STOP[s]}.{BE[b]}.m{MIN[m]}.{TREND[t]}.{JUAL[j]}.h{HAD[h]}' for s, b, m, t, j, h in _GRID]
SEKARANG = KOD.index('s4.b0.m20.t2.j0.h126')
STAT = ('n', 'purata', 'menang', 'rugi15', 'k50', 'sesi_med', 'sesi_purata', 'terbuka', 'n_K3', 'purata_K3', 'menang_K3')
NSTAT = len(STAT)
IX = {k: i for i, k in enumerate(STAT)}
MIN_N, MIN_K3, RUGI_MAKS, B3_MIN = 30, 20, 0.02, 0.001      # ambang pindaan (al)
N_KAWALAN, BENIH_KAWALAN = 300_000, 20261120
# tambahan post hoc (al): lima cara wakil dalam jadual setiap setup, dan kesan komponen bagi senarai kerja rasmi
TANGGA = ('s4.b0.m20.t3.j0.h126', 's4.b0.m20.t8.j0.h126', 's4.b0.m20.t13.j0.h126', 's4.b0.m20.t10.j0.h126', 's4.b0.m20.t0.j0.h126')
RASMI = 'Setiap minggu'
HASIL = os.path.join(SINI, 'hasil', PUS)
REG_F = os.path.normpath(os.path.join(SINI, '..', '..', 'data', 'registry_F.csv'))
F_ = lambda kerja, x: os.path.join(kerja, f'cs25_{x}')

T_STOP = {'s2': 'stop loss 2×ATR dari harga beli', 's3': 'stop loss 3×ATR dari harga beli', 's4': 'stop loss 4×ATR dari harga beli',
          's6': 'stop loss 6×ATR dari harga beli', 'p8': 'stop loss 8 % dari harga beli', 'p15': 'stop loss 15 % dari harga beli',
          'c3': 'stop loss 3×ATR ikut harga tutup', 'c4': 'stop loss 4×ATR ikut harga tutup'}
T_BE = {'b0': '', 'b1': 'naikkan stop loss ke harga beli selepas naik 2×ATR'}
T_TREND = {'t0': 'tiada peraturan trend (stop loss dan had masa sahaja)', 't1': 'tutup di bawah purata 10 hari',
           't2': 'tutup di bawah purata 20 hari', 't3': 'tutup di bawah purata 50 hari', 't4': 'tutup di bawah purata 100 hari',
           't5': 'dua tutup berturut-turut di bawah purata 20 hari', 't6': 'dua tutup berturut-turut di bawah purata 50 hari',
           't7': 'jatuh 3×ATR dari tutup tertinggi', 't8': 'jatuh 4×ATR dari tutup tertinggi', 't9': 'jatuh 6×ATR dari tutup tertinggi',
           't10': 'jatuh 8×ATR dari tutup tertinggi', 't11': 'tutup di bawah harga terendah 10 hari',
           't12': 'tutup di bawah harga terendah 20 hari', 't13': 'jatuh 15 % dari tutup tertinggi', 't14': 'jatuh 25 % dari tutup tertinggi'}
T_JUAL = {'j0': '', 'j1': 'jual separuh selepas naik 10 %', 'j2': 'jual separuh selepas naik 20 %'}
T_HAD = {126: 'had 6 bulan', 252: 'had 12 bulan'}


def teks(w):
    """Ayat biasa bagi satu cara."""
    s, b, m, t, j, h = _GRID[w]
    jual = 'tiada jualan ikut trend' if t == 0 else f'pegang sekurang-kurangnya {MIN[m]} hari, kemudian jual bila {T_TREND[TREND[t]]}'
    bhg = [T_STOP[STOP[s]], T_BE[BE[b]], jual, T_JUAL[JUAL[j]], T_HAD[HAD[h]]]
    return ' · '.join(x for x in bhg if x)


# ---------- enjin ----------
@njit(parallel=True, cache=True)
def atom25(ev, o, l, c, atr, akhir, M, LL):
    """Satu laluan ke hadapan (hingga 252 sesi) bagi setiap isyarat. Sesi beli = indeks 0; nilai = indeks sesi jualan.
    XS/PS[n, 8] stop loss (sesi, harga jual / harga beli); XB/PB[n] stop loss dinaikkan ke harga beli;
    XT[n, 14, 3] trend tamat t1-t14 bagi pegang minimum 3/10/20 (jual pada buka sesi itu); XJ[n, 2] jual separuh (buka sesi itu);
    nm[n] = bilangan sesi selepas sesi beli yang ada dalam data. BESAR = tidak tercetus."""
    n = ev.shape[0]
    XS = np.full((n, NS_), BESAR, np.int16)
    PS = np.full((n, NS_), np.nan, np.float32)
    XB = np.full(n, BESAR, np.int16)
    PB = np.full(n, np.nan, np.float32)
    XT = np.full((n, NT1, NM), BESAR, np.int16)
    XJ = np.full((n, NJ1), BESAR, np.int16)
    nm = np.zeros(n, np.int32)
    for k in prange(n):
        i = ev[k]
        e = i + 1
        P = o[e]
        a0 = atr[i]
        m = akhir[k] - e
        nm[k] = m
        Ls = np.empty(NS_)
        for s in range(NS_):
            Ls[s] = P * (1.0 - S_NILAI[s]) if S_JENIS[s] == 1 else P - S_NILAI[s] * a0
        hc = c[e]
        sedia = False
        cond = np.zeros(NT1, np.bool_)
        for d in range(min(m, DMAX) + 1):
            b = e + d
            cb = c[b]
            for s in range(NS_):
                if XS[k, s] != BESAR:
                    continue
                if S_JENIS[s] == 2:
                    if cb <= Ls[s] and d < m:
                        XS[k, s], PS[k, s] = d + 1, o[b + 1] / P
                elif d == 0:
                    if cb <= Ls[s] and m >= 1:
                        XS[k, s], PS[k, s] = 1, o[b + 1] / P
                elif o[b] <= Ls[s]:
                    XS[k, s], PS[k, s] = d, o[b] / P
                elif l[b] <= Ls[s]:
                    XS[k, s], PS[k, s] = d, Ls[s] / P
            if sedia and XB[k] == BESAR:
                if o[b] <= P:
                    XB[k], PB[k] = d, o[b] / P
                elif l[b] <= P:
                    XB[k], PB[k] = d, 1.0
            if cb >= P + BE_ATR * a0:
                sedia = True
            if cb > hc:
                hc = cb
            if d < 2 or d >= m or d + 1 > DMAX:
                continue
            for j in range(4):
                cond[j] = cb < M[j, b]
            cond[4] = cb < M[1, b] and c[b - 1] < M[1, b - 1]
            cond[5] = cb < M[2, b] and c[b - 1] < M[2, b - 1]
            for j in range(4):
                cond[6 + j] = cb < hc - CH_K[j] * atr[b]
            for j in range(2):
                cond[10 + j] = cb < LL[j, b]
                cond[12 + j] = cb < JATUH[j] * hc
            for j in range(NT1):
                if cond[j]:
                    for mi in range(NM):
                        if XT[k, j, mi] == BESAR and d >= MIN_A[mi] - 1:
                            XT[k, j, mi] = d + 1
            for j in range(NJ1):
                if XJ[k, j] == BESAR and cb >= P * J_NAIK[j]:
                    XJ[k, j] = d + 1
    return XS, PS, XB, PB, XT, XJ, nm


@njit(parallel=True, cache=True)
def stat25(ev, tid, tp, o, c, XS, PS, XB, PB, XT, XJ, nm, sw, bw, mw, tw, jw, hw):
    """Satu posisi setiap saham (ikut sesi jual cara itu sendiri) -> S[cara, NSTAT] (susunan STAT)."""
    n, nw = ev.shape[0], sw.shape[0]
    S = np.full((nw, NSTAT), np.nan, np.float32)
    for w in prange(nw):
        s, bq, mi, t, j, cap = sw[w], bw[w], mw[w], tw[w], jw[w], hw[w] - 1
        tutup = S_JENIS[s] == 2
        buf = np.empty(n, np.int32)
        t_akhir, b_akhir, m = -1, -1, 0
        jr = js = j3 = 0.0
        mng = r15 = k50 = tb = n3 = m3 = 0
        for k in range(n):
            if tid[k] == t_akhir and ev[k] <= b_akhir:
                continue
            e = ev[k] + 1
            P = o[e]
            x = np.int64(XS[k, s])
            px = np.float64(PS[k, s])
            if bq == 1:
                xb = np.int64(XB[k])
                if xb < x or (xb == x and not tutup and xb < BESAR):
                    x, px = xb, np.float64(PB[k])
            if t > 0:
                xt = np.int64(XT[k, t - 1, mi])
                if xt < BESAR and xt <= x:
                    x, px = xt, o[e + xt] / P
            nk = np.int64(nm[k])
            buka = False
            if x <= min(cap, nk):
                r, sk = px, x
            elif cap <= nk:
                r, sk = c[e + cap] / P, cap
            else:
                r, sk, buka = c[e + nk] / P, nk, True
            if j > 0:
                xj = np.int64(XJ[k, j - 1])
                if xj <= sk:
                    r = 0.5 * (o[e + xj] / P) + 0.5 * r
            r = r - 1.0 - KOS
            t_akhir, b_akhir = tid[k], ev[k] + 1 + sk
            buf[m] = sk + 1
            m += 1
            jr += r
            js += sk + 1
            mng += r > 0
            r15 += r <= -0.15
            k50 += r >= 0.50
            tb += buka
            if tp[k] == 2:
                n3 += 1
                j3 += r
                m3 += r > 0
        S[w, 0], S[w, 8] = m, n3
        if m == 0:
            continue
        S[w, 1], S[w, 2], S[w, 3], S[w, 4] = jr / m, mng / m, r15 / m, k50 / m
        S[w, 5], S[w, 6], S[w, 7] = np.median(buf[:m]), js / m, tb / m
        if n3 > 0:
            S[w, 9], S[w, 10] = j3 / n3, m3 / n3
    return S


def sma_panel(pan, n):
    """SMA n bar tutup dalam saham masing-masing (NaN jika kurang n bar); sama seperti cs_keluar10.sma_panel."""
    c = pan['c']
    Sm = np.concatenate([[0.0], np.cumsum(c)])
    i = np.arange(len(c))
    ok = (i - n + 1) >= pan['mula'][pan['tid']]
    return np.where(ok, (Sm[i + 1] - Sm[np.maximum(i + 1 - n, 0)]) / n, np.nan)


def rendah_panel(pan, n):
    """Rendah terendah n sesi SEBELUM bar itu, dalam saham masing-masing (NaN jika kurang n bar sebelumnya)."""
    l = pd.Series(pan['l'])
    r = l.rolling(n).min().shift(1).to_numpy()
    i = np.arange(len(l))
    return np.where((i - n) >= pan['mula'][pan['tid']], r, np.nan)


def atom_panel(pan, ev):
    ev = np.ascontiguousarray(ev, dtype=np.int64)
    akhir = (pan['mula'][pan['tid'][ev] + 1] - 1).astype(np.int64)
    M = np.stack([sma_panel(pan, n) for n in SMA_N])
    LL = np.stack([rendah_panel(pan, n) for n in LL_N])
    return atom25(ev, pan['o'], pan['l'], pan['c'], pan['atr'], akhir, M, LL)


def stat_panel(pan, ev, A, ix=None, cara=None):
    """Statistik bagi senarai isyarat `ev` (tersusun); A = atom bagi isyarat itu (atau bagi isyarat unik, dengan `ix`)."""
    if ix is not None:
        A = tuple(a[ix] for a in A)
    g = (SW, BW, MW, TW, JW, HW) if cara is None else tuple(a[cara] for a in (SW, BW, MW, TW, JW, HW))
    return stat25(ev, pan['tid'][ev].astype(np.int64), pan['tempoh'][ev].astype(np.int64), pan['o'], pan['c'], *A, *g)


# ---------- senarai setup dan isyarat ----------
def senarai():
    """Setiap kod registry F dengan peraturan masuk terurai (pencetus, q1, q2, f1, f2); -1 = tiada."""
    import cs_atom as atom
    import cs_lapis as lapis
    reg = pd.read_csv(REG_F, dtype=str).fillna('')
    kq1, kq2 = [x[:4] for x in lapis.PASARAN], [x[:4] for x in lapis.KUMPULAN]
    kf = [x[:3] for x in atom.PENAPIS]
    f23 = os.path.join(SINI, 'hasil', 'CS23', 'skor.csv.gz')
    guna = pd.read_csv(f23, usecols=['id', 'kegunaan']).set_index('id').kegunaan.to_dict() if os.path.exists(f23) else {}
    out = []
    for r in reg.itertuples():
        t = r.takrif.split('|')
        b = dict(id=r.id, pusingan=r.pusingan, nama=r.masuk, prasyarat=r.prasyarat, penapis=r.penapis, henti=r.henti, keluar=r.keluar,
                 kegunaan=guna.get(r.id, 'Tiada dalam senarai CS23'), pencetus='', q1=-1, q2=-1, f1=-1, f2=-1)
        try:
            fs = [kf.index(x) for x in t[1].split('+') if x] + [-1, -1]
            kod = [x for x in t[4].split('+') if x] if len(t) > 4 else []
            assert all(x in kq1 or x in kq2 for x in kod) and '@' not in t[0]
            b.update(pencetus=t[0], f1=fs[0], f2=fs[1], q1=next((kq1.index(x) for x in kod if x in kq1), -1),
                     q2=next((kq2.index(x) for x in kod if x in kq2), -1))
        except Exception:
            pass
        out.append(b)
    return out


def isyarat(kerja, set_, pan):
    """dict id -> isyarat (tetingkap 126 sesi lengkap, tersusun) bagi setiap kod yang isyaratnya dapat dijana pada kumpulan itu."""
    import cs_cari12 as c12
    import cs_lapis as lapis
    import cs_semak11 as s11
    L = lapis.muat(kerja, set_)
    L1, L2 = L['L1'], L['L2']
    EV = c12.semua_pencetus(kerja, set_)
    sah = s11.sah126(pan)
    out = {}
    for x in senarai():
        ev = EV.get(x['pencetus'])
        if ev is None:
            continue
        m = sah[ev]
        if x['q1'] >= 0:
            m &= L1[x['q1'], ev] > 0
        if x['q2'] >= 0:
            m &= L2[x['q2'], ev] > 0
        for f in (x['f1'], x['f2']):
            if f >= 0:
                m &= pan['F'][f, ev] > 0
        out[x['id']] = np.ascontiguousarray(ev[m], dtype=np.int64)
    return out


# ---------- larian ----------
def kira(kerja, hanya=None):
    """Statistik setiap setup x cara pada kumpulan A dan B -> cs25_A.npy, cs25_B.npy [setup, cara, NSTAT] + cs25_ids.json."""
    t0 = time.time()
    for set_ in ('A', 'B'):
        f = F_(kerja, f'{set_}.npy')
        if os.path.exists(f) and hanya is None:
            continue
        pan = cari.panel(kerja, set_)
        E = isyarat(kerja, set_, pan)
        ids = sorted(E, key=lambda i: int(i[1:]))
        if hanya is not None:
            ids = ids[:hanya]
        U = np.unique(np.concatenate([E[i] for i in ids]))
        cari.log(f'CS25 {set_}: {len(ids)} setup · {len(U):,} isyarat berbeza · {sum(len(E[i]) for i in ids):,} isyarat · {time.time() - t0:.0f}s')
        A = atom_panel(pan, U)
        cari.log(f'CS25 {set_}: atom siap · {time.time() - t0:.0f}s')
        # titik semak setiap 200 setup: kontena boleh dimulakan semula di tengah larian
        fp, fj = F_(kerja, f'{set_}.bhg.npy'), F_(kerja, f'{set_}.bhg.json')
        S, mula_j = np.full((len(ids), W, NSTAT), np.nan, np.float32), 0
        if hanya is None and os.path.exists(fp) and os.path.exists(fj):
            sedia = json.load(open(fj))
            if sedia['ids'] == ids:
                S, mula_j = np.load(fp), sedia['siap']
                cari.log(f'CS25 {set_}: sambung dari setup {mula_j}')
        for j, i in enumerate(ids):
            if j < mula_j:
                continue
            if len(E[i]):
                S[j] = stat_panel(pan, E[i], A, np.searchsorted(U, E[i]))
            if (j + 1) % 200 == 0:
                if hanya is None:
                    np.save(fp + '.tmp.npy', S)
                    os.replace(fp + '.tmp.npy', fp)
                    json.dump({'ids': ids, 'siap': j + 1}, open(fj, 'w'))
                cari.log(f'  CS25 {set_}: {j + 1}/{len(ids)} · {time.time() - t0:.0f}s · RSS {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss // 1024} MB')
        if hanya is not None:
            return ids, S
        np.save(f + '.tmp.npy', S)
        os.replace(f + '.tmp.npy', f)
        json.dump(ids, open(F_(kerja, f'ids_{set_}.json'), 'w'))
        cari.log(f'CS25 {set_}: statistik siap · {time.time() - t0:.0f}s')


def kawalan(kerja):
    """Kawalan rawak: 300,000 bar layak kumpulan B (benih tetap), setiap cara -> cs25_kawalan.npy [cara, NSTAT]."""
    import cs_semak11 as s11
    pan = cari.panel(kerja, 'B')
    sah = np.flatnonzero(s11.sah126(pan))
    ev = np.sort(np.random.default_rng(BENIH_KAWALAN).choice(sah, N_KAWALAN, replace=False)).astype(np.int64)
    S = stat_panel(pan, ev, atom_panel(pan, ev))
    np.save(F_(kerja, 'kawalan.npy'), S)
    cari.log(f"CS25 kawalan: {len(ev):,} bar rawak · cara sekarang purata {S[SEKARANG, 1]:+.4f} menang {S[SEKARANG, 2]:.3f}")
    return S


def pariti(kerja, n_setup=300):
    """Cara sekarang mesti sama dengan enjin CS14 (`r0.t1.126`) pada isyarat yang sama (kumpulan B; setiap setup ke-k)."""
    import cs_pegang14 as c14
    pan = cari.panel(kerja, 'B')
    E = isyarat(kerja, 'B', pan)
    ids = sorted(E, key=lambda i: int(i[1:]))
    ids = [i for i in ids if len(E[i])][::max(1, len(E) // n_setup)]
    w14 = c14.SEKARANG
    g14 = tuple(a[w14:w14 + 1] for a in (c14.RW, c14.TW, c14.HW))
    cur = np.array([SEKARANG])
    beza = 0.0
    for i in ids:
        ev = E[i]
        R, SK, TB = c14.hasil14(*c14.atom_panel(pan, ev), *g14)
        s14 = c14.stat14(ev, pan['tid'][ev].astype(np.int64), pan['tempoh'][ev].astype(np.int64), R, SK, TB)[0]
        s25 = stat_panel(pan, ev, atom_panel(pan, ev), cara=cur)[0]
        d = max(abs(float(s14[c14.IX[k]]) - float(s25[IX[k]])) for k in ('n', 'purata', 'menang', 'rugi15'))
        beza = max(beza, d)
    out = {'setup': len(ids), 'beza_terbesar': beza, 'lulus': bool(beza < 1e-5)}
    json.dump(out, open(F_(kerja, 'pariti.json'), 'w'))
    cari.log(f'CS25 pariti: {out}')
    return out


# ---------- bacaan ----------
def muat(kerja):
    ids = json.load(open(F_(kerja, 'ids_A.json')))
    assert ids == json.load(open(F_(kerja, 'ids_B.json')))
    return dict(ids=ids, A=np.load(F_(kerja, 'A.npy'), mmap_mode='r'), B=np.load(F_(kerja, 'B.npy'), mmap_mode='r'),
                K=np.load(F_(kerja, 'kawalan.npy')), pariti=json.load(open(F_(kerja, 'pariti.json'))))


def med(x):
    return float(np.nanmedian(x)) if np.isfinite(x).any() else float('nan')


def pilih_sejagat(SA, ok):
    """(U, S, E) dipilih pada kumpulan A: nilai tengah merentas setup bagi beza lawan cara sekarang."""
    P, R = np.asarray(SA[ok, :, IX['purata']], np.float64), np.asarray(SA[ok, :, IX['rugi15']], np.float64)
    dp = np.nanmedian(P - P[:, [SEKARANG]], axis=0)
    dr = np.nanmedian(R - R[:, [SEKARANG]], axis=0)
    per20 = np.nanmedian(P / np.asarray(SA[ok, :, IX['sesi_purata']], np.float64) * 20.0, axis=0)
    calon = np.arange(W) != SEKARANG
    U = int(np.argmax(np.where(calon, dp, -np.inf)))
    S_ = int(np.argmax(np.where(calon & (dr <= RUGI_MAKS), dp, -np.inf)))
    E_ = int(np.argmax(np.where(calon, per20, -np.inf)))
    return U, S_, E_, dp, dr, per20


def pilih_setup(SA, ok):
    """(Ui, Si)[setup]: cara tersendiri setiap setup pada kumpulan A (cara dengan >= MIN_N dagangan sahaja); -1 = tiada."""
    Ui, Si = np.full(SA.shape[0], -1), np.full(SA.shape[0], -1)
    for i in np.flatnonzero(ok):
        a = np.asarray(SA[i], np.float64)
        sah = a[:, IX['n']] >= MIN_N
        p = np.where(sah, a[:, IX['purata']], -np.inf)
        Ui[i] = int(np.argmax(p))
        Si[i] = int(np.argmax(np.where(a[:, IX['rugi15']] <= a[SEKARANG, IX['rugi15']] + RUGI_MAKS, p, -np.inf)))
    return Ui, Si


def baca(SB, K, ok, w, rujukan=SEKARANG):
    """Bacaan kumpulan B bagi satu cara lawan rujukan (lalai: cara sekarang)."""
    g = lambda k, ww: np.asarray(SB[ok, ww, IX[k]], np.float64)
    dp = g('purata', w) - g('purata', rujukan)
    k3 = (g('n_K3', w) >= MIN_K3) & (g('n_K3', rujukan) >= MIN_K3)
    d3 = (g('purata_K3', w) - g('purata_K3', rujukan))[k3]
    dk = float(K[w, IX['purata']] - K[rujukan, IX['purata']])
    out = dict(cara=KOD[w], ayat=teks(w), setup=int(ok.sum()), lebih_baik=int((dp > 0).sum()), d_purata=med(dp),
               d_menang=med(g('menang', w) - g('menang', rujukan)), d_rugi15=med(g('rugi15', w) - g('rugi15', rujukan)),
               purata=med(g('purata', w)), menang=med(g('menang', w)), rugi15=med(g('rugi15', w)), k50=med(g('k50', w)),
               sesi=med(g('sesi_med', w)), per20=med(g('purata', w) / g('sesi_purata', w) * 20.0), terbuka=med(g('terbuka', w)),
               setup_K3=int(k3.sum()), lebih_baik_K3=int((d3 > 0).sum()), d_purata_K3=med(d3) if len(d3) else float('nan'),
               kawalan_purata=float(K[w, IX['purata']]), kawalan_menang=float(K[w, IX['menang']]),
               kawalan_rugi15=float(K[w, IX['rugi15']]), d_kawalan=dk)
    out['s1'] = bool(out['lebih_baik'] > out['setup'] / 2)
    out['s2'] = bool(out['d_purata_K3'] > 0)
    out['s3'] = bool(out['d_purata'] > dk)
    out['s4'] = bool(out['d_rugi15'] <= RUGI_MAKS)
    return out


def baca_setup(SB, ok, Xi, w):
    """B3: cara tersendiri setiap setup (Xi) lawan satu cara untuk semua (w), kumpulan B."""
    ii = np.flatnonzero(ok & (Xi >= 0))
    p_i = np.array([SB[i, Xi[i], IX['purata']] for i in ii], np.float64)
    g = lambda k: np.array([SB[i, Xi[i], IX[k]] for i in ii], np.float64)
    d = p_i - np.asarray(SB[ii, w, IX['purata']], np.float64)
    ds = p_i - np.asarray(SB[ii, SEKARANG, IX['purata']], np.float64)
    out = dict(setup=int(len(ii)), lebih_baik=int((d > 0).sum()), d_purata=med(d), lebih_baik_sekarang=int((ds > 0).sum()),
               d_purata_sekarang=med(ds), purata=med(p_i), menang=med(g('menang')), rugi15=med(g('rugi15')), sesi=med(g('sesi_med')))
    out['lulus'] = bool(out['lebih_baik'] > out['setup'] / 2 and out['d_purata'] >= B3_MIN)
    return out


def komponen(SB, K, ok, asas):
    """Kesan setiap komponen satu demi satu, lima komponen lain kekal pada cara `asas` (kumpulan B; nilai tengah merentas setup)."""
    g0 = _GRID[asas]
    nama = ('Stop loss', 'Naikkan stop loss ke harga beli', 'Pegang minimum', 'Trend tamat', 'Jual separuh semasa naik', 'Had masa')
    label = (T_STOP, {'b0': 'tiada', 'b1': T_BE['b1']}, {3: '3 hari', 10: '10 hari', 20: '20 hari'}, T_TREND,
             {'j0': 'tiada', 'j1': T_JUAL['j1'], 'j2': T_JUAL['j2']}, T_HAD)
    pilihan = (STOP, BE, MIN, TREND, JUAL, HAD)
    out = []
    for dim in range(6):
        for v in range(len(pilihan[dim])):
            g = list(g0)
            g[dim] = v
            w = _GRID.index(tuple(g))
            b = baca(SB, K, ok, w)
            out.append(dict(komponen=nama[dim], pilihan=label[dim][pilihan[dim][v]], asas=KOD[asas], cara=KOD[w], sama_asas=w == asas,
                            **{k: b[k] for k in ('purata', 'menang', 'rugi15', 'k50', 'sesi', 'per20', 'd_purata', 'd_purata_K3',
                                                 'kawalan_purata', 'kawalan_menang', 'kawalan_rugi15')}))
    return pd.DataFrame(out)


def bacaan(D):
    """Semua bacaan pindaan (al). Pulangkan (B dict, jadual setup, jadual komponen, jadual semua cara)."""
    SA, SB, K, ids = D['A'], D['B'], D['K'], D['ids']
    ok = (np.asarray(SA[:, SEKARANG, 0]) >= MIN_N) & (np.asarray(SB[:, SEKARANG, 0]) >= MIN_N)
    U, S_, E_, dpA, drA, p20A = pilih_sejagat(SA, ok)
    Ui, Si = pilih_setup(SA, ok)
    L = {x['id']: x for x in senarai()}
    B = dict(pariti=D['pariti'], kod_registry=len(L), dinilai=len(ids), tidak_dinilai=len(L) - len(ids), setup_ok=int(ok.sum()),
             cara=W, n_kawalan=N_KAWALAN,
             sekarang=baca(SB, K, ok, SEKARANG), U=baca(SB, K, ok, U), S=baca(SB, K, ok, S_), E=baca(SB, K, ok, E_),
             Ui=baca_setup(SB, ok, Ui, U), Si=baca_setup(SB, ok, Si, S_))
    B['U']['lulus'] = bool(B['U']['s1'] and B['U']['s2'] and B['U']['s3'])
    B['S']['lulus'] = bool(B['S']['s1'] and B['S']['s2'] and B['S']['s3'] and B['S']['s4'])
    B['U']['d_purata_A'], B['S']['d_purata_A'], B['S']['d_rugi15_A'] = float(dpA[U]), float(dpA[S_]), float(drA[S_])
    # ikut kumpulan kegunaan CS23 (maklumat): pemilihan diulang dalam kumpulan itu sahaja
    kg = np.array([L[i]['kegunaan'] for i in ids])
    B['kumpulan'] = []
    for nama in ('Setiap minggu', 'Musim laporan kewangan', 'Keadaan tertentu', 'Lain-lain', 'Tiada dalam senarai CS23'):
        okk = ok & (kg == nama)
        if okk.sum() < 10:
            continue
        u, s_, _, _, _, _ = pilih_sejagat(SA, okk)
        bu, bs = baca(SB, K, okk, u), baca(SB, K, okk, s_)
        B['kumpulan'].append(dict(kumpulan=nama, setup=int(okk.sum()), sekarang=baca(SB, K, okk, SEKARANG), U=bu, S=bs,
                                  U_sejagat=baca(SB, K, okk, U), S_sejagat=baca(SB, K, okk, S_)))
    # taburan pilihan Ui ikut komponen
    tab = {}
    for dim, (nama, pil) in enumerate((('stop', STOP), ('be', BE), ('min', [f'm{x}' for x in MIN]), ('trend', TREND), ('jual', JUAL),
                                       ('had', [f'h{x}' for x in HAD]))):
        v = np.array([_GRID[w][dim] for w in Ui[ok & (Ui >= 0)]])
        tab[nama] = {str(pil[x]): float((v == x).mean()) for x in range(len(pil))}
    B['taburan_Ui'] = tab
    # jadual setiap setup (kumpulan B)
    baris = []
    for j, i in enumerate(ids):
        x = L[i]
        b = dict(id=i, pusingan=x['pusingan'], kegunaan=x['kegunaan'], nama=x['nama'], prasyarat=x['prasyarat'], penapis=x['penapis'],
                 henti_daftar=x['henti'], keluar_daftar=x['keluar'], cukup=bool(ok[j]))
        for tag, w in ((('sekarang', SEKARANG), ('U', U), ('S', S_), ('Ui', int(Ui[j])), ('Si', int(Si[j])))
                       + tuple((f'T{q + 1}', KOD.index(k)) for q, k in enumerate(TANGGA))):
            if w < 0:
                continue
            a = np.asarray(SB[j, w], np.float64)
            if tag in ('Ui', 'Si'):
                b[f'cara_{tag}'], b[f'ayat_{tag}'] = KOD[w], teks(w)
                b[f'purata_A_{tag}'] = float(SA[j, w, IX['purata']])
            b.update({f'{k}_{tag}': float(a[IX[k]]) for k in ('n', 'purata', 'menang', 'rugi15', 'k50', 'sesi_med', 'purata_K3')})
        baris.append(b)
    T = pd.DataFrame(baris)
    Km = pd.concat([komponen(SB, K, ok, SEKARANG).assign(kumpulan='Semua'), komponen(SB, K, ok, U).assign(kumpulan='Semua'),
                    komponen(SB, K, ok & (kg == RASMI), SEKARANG).assign(kumpulan=RASMI)], ignore_index=True)
    B['setup_rasmi'] = int((ok & (kg == RASMI)).sum())
    B['tangga'] = [dict(tag=f'T{q + 1}', **baca(SB, K, ok, KOD.index(k))) for q, k in enumerate(TANGGA)]
    B['tangga_rasmi'] = [baca(SB, K, ok & (kg == RASMI), w) for w in [SEKARANG] + [KOD.index(k) for k in TANGGA]]
    tiada = pd.Series([x['pusingan'] for i, x in L.items() if i not in set(ids)]).value_counts()
    B['tidak_dinilai_pusingan'] = {str(k): int(v) for k, v in tiada.items()}
    # jadual semua cara (nilai tengah merentas setup, kumpulan A dan B, dan kawalan)
    g = lambda S_, k: np.nanmedian(np.asarray(S_[ok, :, IX[k]], np.float64), axis=0)
    C = pd.DataFrame(dict(cara=KOD, ayat=[teks(w) for w in range(W)], d_purata_A=dpA, d_rugi15_A=drA, per20_A=p20A,
                          purata_B=g(SB, 'purata'), menang_B=g(SB, 'menang'), rugi15_B=g(SB, 'rugi15'), k50_B=g(SB, 'k50'),
                          sesi_B=g(SB, 'sesi_med'), kawalan_purata=K[:, IX['purata']], kawalan_menang=K[:, IX['menang']],
                          kawalan_rugi15=K[:, IX['rugi15']]))
    C['d_purata_B'] = C.purata_B - C.purata_B[SEKARANG]
    return B, T, Km, C


def _bersih(x):
    if isinstance(x, dict):
        return {k: _bersih(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [_bersih(v) for v in x]
    if isinstance(x, (np.floating, float)):
        return None if not np.isfinite(x) else round(float(x), 6)
    if isinstance(x, (np.integer,)):
        return int(x)
    if isinstance(x, np.bool_):
        return bool(x)
    return x


def lapor_(kerja):
    D = muat(kerja)
    B, T, Km, C = bacaan(D)
    os.makedirs(HASIL, exist_ok=True)
    json.dump(_bersih(B), open(os.path.join(HASIL, 'bacaan.json'), 'w'), indent=1, ensure_ascii=False)
    T.round(5).to_csv(os.path.join(HASIL, 'setup.csv.gz'), index=False, compression={'method': 'gzip', 'mtime': 0})
    Km.round(5).to_csv(os.path.join(HASIL, 'komponen.csv'), index=False)
    C.round(5).to_csv(os.path.join(HASIL, 'cara.csv.gz'), index=False, compression={'method': 'gzip', 'mtime': 0})
    open(os.path.join(HASIL, 'KELUAR.md'), 'w').write(teks_laporan(_bersih(B), T, Km, C))
    cari.log(f"CS25 lapor: {B['dinilai']} setup dinilai · U={B['U']['cara']} lulus={B['U']['lulus']} · S={B['S']['cara']} lulus={B['S']['lulus']}")
    return B


# ---------- laporan ----------
_p = lambda x, d=1: '–' if x is None or x != x else f'{100 * x:+.{d}f}'
_k = lambda x, d=0: '–' if x is None or x != x else f'{100 * x:.{d}f}'
_h = lambda x: '–' if x is None or x != x else f'{x:.0f}'
_yt = lambda b: 'ya' if b else 'TIDAK'


def _baris(nama, b):
    return (f"| {nama} | {_p(b['purata'])} | {_k(b['menang'])} | {_k(b['rugi15'])} | {_k(b['k50'], 1)} | {_h(b['sesi'])} | {_p(b['per20'], 2)} | "
            f"{_p(b['kawalan_purata'])} · {_k(b['kawalan_menang'])} · {_k(b['kawalan_rugi15'])} |")


_KEPALA = ('| Cara | Purata setiap dagangan % | Menang % | Rugi ≥ 15 % % | Untung ≥ 50 % % | Hari pegang (nilai tengah) | Untung setiap 20 hari pegang % | '
           'Saham rawak, cara sama: purata · menang · rugi ≥ 15 % |\n|---|---|---|---|---|---|---|---|')


def _bacaan_teks(tag, b, perlu_rugi):
    t = [f"- **Cara `{tag}`: {b['ayat']}** (`{b['cara']}`; dipilih pada saham carian). Pada saham yang carian tidak lihat, lawan cara sekarang: "
         f"(1) purata lebih tinggi bagi {b['lebih_baik']:,} daripada {b['setup']:,} setup → {_yt(b['s1'])}; "
         f"(2) belian 2025–26: beza purata {_p(b['d_purata_K3'])} mata ({b['lebih_baik_K3']:,} daripada {b['setup_K3']:,} setup lebih tinggi; perlu > 0) → {_yt(b['s2'])}; "
         f"(3) tambahan bagi setup {_p(b['d_purata'])} mata lawan tambahan bagi saham rawak {_p(b['d_kawalan'])} mata (perlu lebih besar) → {_yt(b['s3'])}"]
    if perlu_rugi:
        t.append(f"; (4) beza rugi ≥ 15 % {_p(b['d_rugi15'])} mata (perlu ≤ +2) → {_yt(b['s4'])}")
    t.append(f". **Keputusan: {'MENOLONG' if b['lulus'] else 'TIDAK menolong'}.** Beza kadar menang {_p(b['d_menang'])} mata; beza rugi ≥ 15 % {_p(b['d_rugi15'])} mata.")
    return ''.join(t)


def teks_laporan(B, T, Km, C):
    L = ['# CS25: stop loss × pegang × jual bagi SETIAP setup F, ikut untung terbesar (backtest; BUKAN bukti)', '',
         'Peraturan ditulis dahulu: `kajian/SPEC_CARIAN_SETUP.md` pindaan 20 Nov 2026 (al). Dijana `cs_keluar25.py`; jangan sunting.', '',
         f"- Permintaan pengguna 20 Nov 2026: kaji stop loss, masa pegang dan masa jual bagi SEMUA setup F, untuk untung terbesar dan rugi terkecil.",
         f"- {B['kod_registry']:,} kod dalam registry F; {B['dinilai']:,} dinilai ({B['tidak_dinilai']} tidak dapat dijana semula dalam mod tanpa intai: "
         + ', '.join(f'{k} {v}' for k, v in B['tidak_dinilai_pusingan'].items()) + '); '
         + f"{B['setup_ok']:,} ada ≥ {MIN_N} dagangan dalam kedua-dua kumpulan saham dan masuk bacaan.",
         f"- {B['cara']:,} cara setiap setup: {NS_} stop loss × {NB} \"naikkan stop loss ke harga beli\" × {NM} pegang minimum × {NT} \"trend tamat\" × "
         f"{NJ} \"jual separuh\" × {NH} had masa. Peraturan beli tidak diubah; kadar tangkap tidak terkesan.",
         f"- Cara dipilih pada saham carian; semua angka di bawah dibaca pada saham yang carian tidak lihat (nilai tengah merentas setup), kos 0.5 %.",
         f"- Semakan pariti: cara sekarang sama dengan enjin CS14 pada {B['pariti']['setup']} setup (beza terbesar {B['pariti']['beza_terbesar']:.7f}) → "
         f"{'lulus' if B['pariti']['lulus'] else 'GAGAL'}.", '',
         '## 1. Keputusan (ujian ditetapkan dahulu)', '',
         _bacaan_teks('U', B['U'], False), _bacaan_teks('S', B['S'], True),
         f"- **Cara tersendiri setiap setup (`Ui`) lawan satu cara `U` untuk semua:** purata `Ui` lebih tinggi bagi {B['Ui']['lebih_baik']:,} daripada "
         f"{B['Ui']['setup']:,} setup; nilai tengah beza {_p(B['Ui']['d_purata'], 2)} mata (perlu lebih separuh DAN ≥ +0.1) → "
         f"**{'MENOLONG' if B['Ui']['lulus'] else 'TIDAK menolong: satu cara untuk semua sama baik'}**. `Si` lawan `S`: {B['Si']['lebih_baik']:,} daripada "
         f"{B['Si']['setup']:,}; beza {_p(B['Si']['d_purata'], 2)} mata → **{'MENOLONG' if B['Si']['lulus'] else 'TIDAK menolong'}**.", '',
         '## 2. Cara sekarang lawan cara terpilih (saham yang carian tidak lihat)', '', _KEPALA,
         _baris('Cara sekarang: ' + B['sekarang']['ayat'], B['sekarang']),
         _baris('`U` untung terbesar: ' + B['U']['ayat'], B['U']),
         _baris('`S` untung terbesar tanpa menambah rugi besar: ' + B['S']['ayat'], B['S']),
         _baris('`E` untung terbesar setiap hari pegang (maklumat): ' + B['E']['ayat'], B['E']),
         f"| `Ui` cara tersendiri setiap setup (untung terbesar) | {_p(B['Ui']['purata'])} | {_k(B['Ui']['menang'])} | {_k(B['Ui']['rugi15'])} | – | {_h(B['Ui']['sesi'])} | – | – |",
         f"| `Si` cara tersendiri setiap setup (tanpa menambah rugi besar) | {_p(B['Si']['purata'])} | {_k(B['Si']['menang'])} | {_k(B['Si']['rugi15'])} | – | {_h(B['Si']['sesi'])} | – | – |",
         '', 'Lajur terakhir = 300,000 belian rawak pada saham yang sama, dijual dengan cara yang sama. Jika angka saham rawak naik sama banyak, '
         'tambahan itu datang daripada memegang saham lebih lama dalam data ini (pasaran naik, tiada saham mati), bukan daripada setup.', '']
    L += ['## 3. Tangga: jual lebih lewat = purata lebih besar, tetapi rugi besar lebih kerap (stop loss 4×ATR, pegang minimum 20 hari)', '',
          f"Kiri = semua {B['setup_ok']:,} setup; kanan = {B['setup_rasmi']:,} setup \"{RASMI}\" (senarai kerja rasmi; tambahan selepas hasil dilihat).", '',
          '| Tanda jual | Semua: purata % · menang % · rugi ≥ 15 % % · hari | Setiap minggu: purata % · menang % · rugi ≥ 15 % % · hari | Saham rawak: purata · menang · rugi ≥ 15 % |',
          '|---|---|---|---|']
    for a, r in zip([B['sekarang']] + B['tangga'], B['tangga_rasmi']):
        L.append(f"| {a['ayat'].split('jual bila ')[-1].split(' · had')[0] if 'jual bila' in a['ayat'] else 'tiada (pegang 6 bulan)'} | "
                 f"{_p(a['purata'])} · {_k(a['menang'])} · {_k(a['rugi15'])} · {_h(a['sesi'])} | {_p(r['purata'])} · {_k(r['menang'])} · {_k(r['rugi15'])} · {_h(r['sesi'])} | "
                 f"{_p(a['kawalan_purata'])} · {_k(a['kawalan_menang'])} · {_k(a['kawalan_rugi15'])} |")
    L.append('')
    for asas, kump, tajuk in ((B['sekarang']['cara'], 'Semua', '## 4. Kesan setiap komponen, satu demi satu (lima yang lain kekal seperti cara sekarang)'),
                              (B['sekarang']['cara'], RASMI, f'## 5. Sama, bagi setup "{RASMI}" sahaja (tambahan selepas hasil dilihat; maklumat)'),
                              (B['U']['cara'], 'Semua', '## 6. Kesan setiap komponen, satu demi satu (lima yang lain kekal seperti cara `U`)')):
        L += [tajuk, '', '| Komponen | Pilihan | Purata % | Menang % | Rugi ≥ 15 % % | Untung ≥ 50 % % | Hari pegang | Setiap 20 hari % | 2025–26: beza purata (mata) | '
              'Saham rawak: purata · menang · rugi ≥ 15 % |', '|---|---|---|---|---|---|---|---|---|---|']
        for r in Km[(Km.asas == asas) & (Km.kumpulan == kump)].itertuples():
            tanda = ' **(asas)**' if r.sama_asas else ''
            L.append(f"| {r.komponen} | {r.pilihan}{tanda} | {_p(r.purata)} | {_k(r.menang)} | {_k(r.rugi15)} | {_k(r.k50, 1)} | {_h(r.sesi)} | {_p(r.per20, 2)} | "
                     f"{_p(r.d_purata_K3)} | {_p(r.kawalan_purata)} · {_k(r.kawalan_menang)} · {_k(r.kawalan_rugi15)} |")
        L.append('')
    L += ['## 7. Ikut kumpulan setup (maklumat; pemilihan diulang dalam kumpulan itu pada saham carian)', '',
          '| Kumpulan | Setup | Cara | Purata % | Menang % | Rugi ≥ 15 % % | Hari pegang | Lebih baik daripada cara sekarang | 2025–26: beza purata (mata) | Saham rawak: purata |',
          '|---|---|---|---|---|---|---|---|---|---|']
    for g in B['kumpulan']:
        for tag, nama in (('sekarang', 'cara sekarang'), ('U', '`U` kumpulan ini'), ('S', '`S` kumpulan ini'), ('U_sejagat', '`U` semua setup'),
                          ('S_sejagat', '`S` semua setup')):
            b = g[tag]
            ayat = '' if tag in ('sekarang', 'U_sejagat', 'S_sejagat') else ': ' + b['ayat']
            L.append(f"| {g['kumpulan']} | {g['setup']:,} | {nama}{ayat} | {_p(b['purata'])} | {_k(b['menang'])} | {_k(b['rugi15'])} | {_h(b['sesi'])} | "
                     f"{'–' if tag == 'sekarang' else str(b['lebih_baik']) + ' / ' + str(b['setup'])} | {'–' if tag == 'sekarang' else _p(b['d_purata_K3'])} | {_p(b['kawalan_purata'])} |")
    L += ['', '## 8. Cara tersendiri setiap setup: apa yang dipilih (`Ui`, pada saham carian)', '',
          '| Komponen | Bahagian setup yang memilih setiap pilihan |', '|---|---|']
    nama = {'stop': 'Stop loss', 'be': 'Naikkan stop loss ke harga beli', 'min': 'Pegang minimum', 'trend': 'Trend tamat', 'jual': 'Jual separuh',
            'had': 'Had masa'}
    for k, v in B['taburan_Ui'].items():
        L.append(f"| {nama[k]} | " + ' · '.join(f'`{a}` {100 * x:.0f} %' for a, x in sorted(v.items(), key=lambda z: -z[1]) if x >= 0.005) + ' |')
    L += ['', f"Pada saham yang carian tidak lihat, `Ui` memberi purata {_p(B['Ui']['purata'])} % (nilai tengah), lawan cara sekarang "
          f"{_p(B['Ui']['d_purata_sekarang'], 2)} mata ({B['Ui']['lebih_baik_sekarang']:,} daripada {B['Ui']['setup']:,} setup lebih tinggi). "
          'Jadual setiap setup: `setup.csv.gz`.', '',
          '## 9. Sepuluh cara teratas pada saham carian, dan bacaannya pada saham yang carian tidak lihat', '',
          'Cara tanpa peraturan trend adalah sama bagi tiga pilihan pegang minimum; ia ditunjuk sekali.', '',
          '| Cara | Saham carian: beza purata (mata) | Tidak dilihat: purata % | Menang % | Rugi ≥ 15 % % | Hari pegang | Saham rawak: purata |',
          '|---|---|---|---|---|---|---|']
    for r in C.sort_values('d_purata_A', ascending=False).drop_duplicates('ayat').head(10).itertuples():
        L.append(f"| {r.ayat} | {_p(r.d_purata_A)} | {_p(r.purata_B)} | {_k(r.menang_B)} | {_k(r.rugi15_B)} | {_h(r.sesi_B)} | {_p(r.kawalan_purata)} |")
    L += ['', 'Semua 4,320 cara: `cara.csv.gz`.', '', '## 10. Kaveat', '',
          '- Tiada saham mati dalam data: untung daripada memegang lama condong ke atas, dan lebih condong bagi cara yang memegang lebih lama.',
          '- 4,320 cara dicuba setiap setup; cara terbaik pada saham carian condong ke atas. Sebab itu bacaan dibuat pada saham yang carian tidak lihat.',
          '- Saham yang carian tidak lihat sudah dipakai berkali-kali; 2025–26 pendek.',
          '- Stop loss ikut harga tutup boleh rugi lebih daripada parasnya; "naikkan stop loss ke harga beli" menganggap jualan tepat pada harga beli; '
          '"jual separuh" dikenakan kos sekali sahaja.',
          '- Tiada perubahan pada registry F, senarai utama, Top 100 atau dashboard: menukar stop loss atau cara jual berdaftar ialah keputusan pengguna.',
          '- Pangkat backtest, BUKAN bukti.', '']
    return '\n'.join(L)


if __name__ == '__main__':
    cmd, kerja = sys.argv[1], sys.argv[2]
    {'kira': kira, 'kawalan': kawalan, 'pariti': pariti, 'lapor': lapor_}[cmd](kerja)
