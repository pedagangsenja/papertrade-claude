"""CS26 (pindaan 20 Nov 2026 (am)): stop loss x pegang x jual HABIS-HABISAN bagi setiap setup F, disusun ikut nisbah untung : rugi.

Sepuluh komponen (40.7 juta gabungan): stop loss awal, potong belian yang tidak menjadi, tanda trend tamat, bila tanda itu mula
dipakai, ketatkan selepas untung besar, ambil untung, naikkan stop loss ke harga beli, pasaran, laporan kewangan berikutnya, had
masa. Carian tiga peringkat: satu demi satu, 8,000 cara rawak, naik bukit pada kumpulan A. Bacaan pada kumpulan B.

Guna: python3 cs_keluar26.py kira <kerja> | pariti <kerja> | lapor <kerja>
Folder kerja seperti CS25 (panel_A/B, lapis_A/B, cs07_K_A/B, benih_A/B.pkl tanpa intai).
"""
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
import cs_keluar25 as c25  # noqa: E402
import cs_teras as teras  # noqa: E402

PUS = 'CS26'
KOS = teras.KOS
BESAR = 32767
DMAX = 251
# ---- sepuluh komponen (dikunci pindaan (am)) ----
STOP = ('s2', 's3', 's4', 's6', 'p5', 'p8', 'p10', 'p15', 'c3', 'c4', 'g1', 'g10', 'g20')
S_JENIS = np.array([0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 3, 3, 3], np.int64)   # 0 k x ATR; 1 peratus; 2 k x ATR ikut tutup; 3 ikut carta
S_NILAI = np.array([2.0, 3.0, 4.0, 6.0, 0.05, 0.08, 0.10, 0.15, 3.0, 4.0, 0.0, 1.0, 2.0])   # jenis 3: indeks paras carta
G_LANTAI = 0.5
POTONG = ('n0', 'n5', 'n10', 'n10a', 'n20')
HARIAN = ('ma10', 'ma20', 'ma50', 'ma100', '2ma20', '2ma50', 'ema10', 'ema20', 'ma20-1a', 'ma50-1a', 'x1020', 'x2050', 'll5', 'll10',
          'll20', 'piv', '3dn', 'sar', 'st', 'macd', 'rsi50', 'di', 'vol')
LALUAN = ('ch2', 'ch3', 'ch4', 'ch6', 'ch8', 'hh3', 'tr10', 'tr15', 'tr20', 'tr25')
TREND = ('t0',) + HARIAN + LALUAN
NG, NT1 = len(HARIAN), len(HARIAN) + len(LALUAN)
CH_K = np.array([2.0, 3.0, 4.0, 6.0, 8.0])
HH_K = 3.0
TR_X = np.array([0.90, 0.85, 0.80, 0.75])
AKTIF = ('m3', 'm10', 'm20', 'm40', 'a5', 'a10', 'a20', 'a50')
A_HARI = np.array([2, 9, 19, 39], np.int64)                  # indeks sesi (sesi beli = 0) bagi m3, m10, m20, m40
A_NAIK = np.array([1.05, 1.10, 1.20, 1.50])
A_M40 = AKTIF.index('m40')
KETAT = ('k0', 'k1', 'k2', 'k3')
K_T = np.array([-1, HARIAN.index('ma10'), NG + LALUAN.index('ch2'), HARIAN.index('ma10')], np.int64)
K_A = np.array([-1, AKTIF.index('a20'), AKTIF.index('a20'), AKTIF.index('a50')], np.int64)
UNTUNG = ('j0', 'j1', 'j2', 'j3', 'j4', 'j5', 'j6', 'j7')
J_NAIK = np.array([1.10, 1.20, 1.50])
J_EXT, ONEIL_SESI = 4.0, 15
BE = ('b0', 'b1', 'b2')
BE_ATR, BE_PCT = 2.0, 1.10
PASAR = ('q0', 'q1', 'q2')
LAPOR = ('e0', 'e1')
E_MULA = 19
HAD = (20, 60, 126, 252)
KOMPONEN = (STOP, POTONG, TREND, AKTIF, KETAT, UNTUNG, BE, PASAR, LAPOR, tuple(f'h{x}' for x in HAD))
NAMA_K = ('Stop loss awal', 'Potong belian yang tidak menjadi', 'Tanda trend tamat', 'Bila tanda trend mula dipakai',
          'Ketatkan selepas untung besar', 'Ambil untung', 'Naikkan stop loss ke harga beli', 'Pasaran', 'Laporan kewangan berikutnya',
          'Had masa')
NK = len(KOMPONEN)
RUANG = int(np.prod([len(k) for k in KOMPONEN]))
assert RUANG == 40_734_720
ASAS = tuple(k.index(x) for k, x in zip(KOMPONEN, ('s4', 'n0', 'ma20', 'm20', 'k0', 'j0', 'b0', 'q0', 'e0', 'h126')))
N_RAWAK, BENIH_RAWAK = 8000, 20261121
TAMAK_MIN, TAMAK_MAKS = 0.005, 8
STAT = ('n', 'untung', 'rugi', 'menang', 'rugi15', 'k50', 'sesi_med', 'sesi_purata', 'terbuka', 'n_K3', 'untung_K3', 'rugi_K3')
NSTAT = len(STAT)
IX = {k: i for i, k in enumerate(STAT)}
MIN_N, MIN_K3, SASARAN, B3_MIN, NISBAH_MAKS = 30, 20, 2.0, 0.05, 99.0
N_KAWALAN, BENIH_KAWALAN = c25.N_KAWALAN, c25.BENIH_KAWALAN
RASMI = c25.RASMI
HASIL = os.path.join(SINI, 'hasil', PUS)
F_ = lambda kerja, x: os.path.join(kerja, f'cs26_{x}')

T_ = [
    {'s2': 'stop loss 2×ATR', 's3': 'stop loss 3×ATR', 's4': 'stop loss 4×ATR', 's6': 'stop loss 6×ATR', 'p5': 'stop loss 5 %',
     'p8': 'stop loss 8 %', 'p10': 'stop loss 10 %', 'p15': 'stop loss 15 %', 'c3': 'stop loss 3×ATR ikut harga tutup',
     'c4': 'stop loss 4×ATR ikut harga tutup', 'g1': 'stop loss di bawah harga terendah hari isyarat',
     'g10': 'stop loss di bawah harga terendah 10 hari sebelum beli', 'g20': 'stop loss di bawah harga terendah 20 hari sebelum beli'},
    {'n0': 'tiada', 'n5': 'jual jika hari ke-5 masih rugi', 'n10': 'jual jika hari ke-10 masih rugi',
     'n10a': 'jual jika hari ke-10 belum naik 1×ATR', 'n20': 'jual jika hari ke-20 masih rugi'},
    {'t0': 'tiada tanda trend', 'ma10': 'tutup di bawah purata 10 hari', 'ma20': 'tutup di bawah purata 20 hari',
     'ma50': 'tutup di bawah purata 50 hari', 'ma100': 'tutup di bawah purata 100 hari', '2ma20': 'dua tutup berturut-turut di bawah purata 20 hari',
     '2ma50': 'dua tutup berturut-turut di bawah purata 50 hari', 'ema10': 'tutup di bawah EMA 10 hari', 'ema20': 'tutup di bawah EMA 20 hari',
     'ma20-1a': 'tutup lebih 1×ATR di bawah purata 20 hari', 'ma50-1a': 'tutup lebih 1×ATR di bawah purata 50 hari',
     'x1020': 'purata 10 hari di bawah purata 20 hari', 'x2050': 'purata 20 hari di bawah purata 50 hari',
     'll5': 'tutup di bawah harga terendah 5 hari', 'll10': 'tutup di bawah harga terendah 10 hari', 'll20': 'tutup di bawah harga terendah 20 hari',
     'piv': 'tutup di bawah lembah (swing low) terakhir', '3dn': 'tiga tutup turun berturut-turut', 'sar': 'Parabolic SAR bertukar turun',
     'st': 'Supertrend bertukar turun', 'macd': 'MACD di bawah garis isyarat', 'rsi50': 'RSI14 di bawah 50', 'di': '+DI di bawah −DI',
     'vol': 'hari turun dengan volum ≥ 1.5× biasa', 'ch2': 'jatuh 2×ATR dari tutup tertinggi', 'ch3': 'jatuh 3×ATR dari tutup tertinggi',
     'ch4': 'jatuh 4×ATR dari tutup tertinggi', 'ch6': 'jatuh 6×ATR dari tutup tertinggi', 'ch8': 'jatuh 8×ATR dari tutup tertinggi',
     'hh3': 'jatuh 3×ATR dari harga tertinggi (Chandelier asal)', 'tr10': 'jatuh 10 % dari tutup tertinggi', 'tr15': 'jatuh 15 % dari tutup tertinggi',
     'tr20': 'jatuh 20 % dari tutup tertinggi', 'tr25': 'jatuh 25 % dari tutup tertinggi'},
    {'m3': 'mulai hari ke-3', 'm10': 'mulai hari ke-10', 'm20': 'mulai hari ke-20', 'm40': 'mulai hari ke-40', 'a5': 'hanya selepas naik 5 %',
     'a10': 'hanya selepas naik 10 %', 'a20': 'hanya selepas naik 20 %', 'a50': 'hanya selepas naik 50 %'},
    {'k0': 'tiada', 'k1': 'selepas naik 20 %: jual bila tutup di bawah purata 10 hari', 'k2': 'selepas naik 20 %: jual bila jatuh 2×ATR dari tutup tertinggi',
     'k3': 'selepas naik 50 %: jual bila tutup di bawah purata 10 hari'},
    {'j0': 'tiada', 'j1': 'jual separuh selepas naik 10 %', 'j2': 'jual separuh selepas naik 20 %', 'j3': 'jual semua selepas naik 20 %',
     'j4': 'jual semua selepas naik 50 %', 'j5': 'jual semua bila RSI14 melebihi 80', 'j6': 'jual semua bila tutup lebih 4×ATR di atas purata 20 hari',
     'j7': 'jual semua pada +20 %, kecuali jika dicapai dalam 3 minggu (maka pegang 8 minggu)'},
    {'b0': 'tiada', 'b1': 'selepas naik 2×ATR', 'b2': 'selepas naik 10 %'},
    {'q0': 'tiada', 'q1': 'jual bila QQQ OFF', 'q2': 'jual bila SPY di bawah purata 200 hari'},
    {'e0': 'tiada', 'e1': 'jual sebelum laporan kewangan berikutnya'},
    {'h20': 'jual hari ke-20', 'h60': 'had 3 bulan', 'h126': 'had 6 bulan', 'h252': 'had 12 bulan'},
]


def kod(g):
    return '|'.join(KOMPONEN[i][g[i]] for i in range(NK))


def dari_kod(k):
    return tuple(KOMPONEN[i].index(x) for i, x in enumerate(k.split('|')))


def kanon(g):
    """Bentuk piawai: tanpa tanda trend, komponen "bila mula dipakai" tidak bermakna -> m3."""
    g = list(g)
    if g[2] == 0:
        g[3] = 0
    return tuple(int(x) for x in g)


def teks(g):
    """Ayat biasa bagi satu cara."""
    s, n, t, a, k, j, b, p, e, h = g
    bhg = [T_[0][STOP[s]]]
    if b:
        bhg.append('naikkan stop loss ke harga beli ' + T_[6][BE[b]])
    if n:
        bhg.append(T_[1][POTONG[n]])
    if t:
        bhg.append(f'jual bila {T_[2][TREND[t]]} ({T_[3][AKTIF[a]]})')
    for i, v, K in ((4, k, KETAT), (5, j, UNTUNG), (7, p, PASAR), (8, e, LAPOR)):
        if v:
            bhg.append(T_[i][K[v]])
    bhg.append(T_[9][f'h{HAD[h]}'])
    return ' · '.join(bhg)


# ---------- siri harian setiap bar ----------
@njit(cache=True)
def sar_turun(h, l, mula):
    """Parabolic SAR Wilder (0.02, 0.2) dalam setiap saham; True = SAR di atas harga (trend turun) selepas tutup bar itu."""
    out = np.zeros(h.shape[0], np.bool_)
    for t in range(mula.shape[0] - 1):
        s, e = mula[t], mula[t + 1]
        if e - s < 3:
            continue
        naik = h[s + 1] + l[s + 1] >= h[s] + l[s]
        ep = max(h[s], h[s + 1]) if naik else min(l[s], l[s + 1])
        sar = min(l[s], l[s + 1]) if naik else max(h[s], h[s + 1])
        af = 0.02
        out[s + 1] = not naik
        for b in range(s + 2, e):
            sar += af * (ep - sar)
            if naik:
                sar = min(sar, l[b - 1], l[b - 2])
                if l[b] < sar:
                    naik, sar, ep, af = False, ep, l[b], 0.02
                elif h[b] > ep:
                    ep, af = h[b], min(af + 0.02, 0.2)
            else:
                sar = max(sar, h[b - 1], h[b - 2])
                if h[b] > sar:
                    naik, sar, ep, af = True, ep, h[b], 0.02
                elif l[b] < ep:
                    ep, af = l[b], min(af + 0.02, 0.2)
            out[b] = not naik
    return out


@njit(cache=True)
def lembah(l, mula):
    """Paras rendah ayunan terakhir yang sudah disahkan (rendah < 2 bar di kiri dan kanan; diketahui 2 bar kemudian); NaN jika tiada."""
    out = np.full(l.shape[0], np.nan)
    for t in range(mula.shape[0] - 1):
        s, e = mula[t], mula[t + 1]
        akhir = np.nan
        for b in range(s, e):
            p = b - 2
            if p - 2 >= s and l[p] < l[p - 1] and l[p] < l[p - 2] and l[p] < l[p + 1] and l[p] < l[p + 2]:
                akhir = l[p]
            out[b] = akhir
    return out


def siri(pan, L):
    """(G[23, bar], D[5, bar], LI[2, bar]): tanda trend harian (susunan HARIAN); [RSI > 80, terlalu jauh di atas purata, QQQ OFF,
    SPY bawah SMA200, laporan dalam 1-5 sesi]; rendah terendah 10 / 20 sesi TERMASUK bar itu (untuk stop loss ikut carta)."""
    import cs_atom as atom
    c, l, h, atr, mula, tid = pan['c'], pan['l'], pan['h'], pan['atr'], pan['mula'], pan['tid']
    n = len(c)
    i = np.arange(n)
    awal = mula[tid]
    X = lambda nama: pan['X'][[x[:3] for x in atom.KELUAR].index(nama)] > 0
    M = {k: c25.sma_panel(pan, k) for k in (10, 20, 50, 100)}
    lepas = lambda a, k=1: np.where(i - k >= awal, np.concatenate([np.full(k, np.nan), a[:-k]]), np.nan)
    bawah = lambda k: c < M[k]
    G = np.zeros((NG, n), np.uint8)
    turun3 = (c < lepas(c)) & (lepas(c) < lepas(c, 2)) & (lepas(c, 2) < lepas(c, 3))
    with np.errstate(invalid='ignore'):
        baris = {'ma10': bawah(10), 'ma20': bawah(20), 'ma50': bawah(50), 'ma100': bawah(100),
                 '2ma20': bawah(20) & (lepas(c) < lepas(M[20])), '2ma50': bawah(50) & (lepas(c) < lepas(M[50])),
                 'ema10': X('X04'), 'ema20': X('X05'), 'ma20-1a': c < M[20] - atr, 'ma50-1a': c < M[50] - atr,
                 'x1020': M[10] < M[20], 'x2050': M[20] < M[50], 'll5': c < c25.rendah_panel(pan, 5), 'll10': c < c25.rendah_panel(pan, 10),
                 'll20': c < c25.rendah_panel(pan, 20), 'piv': c < lembah(l, mula), '3dn': turun3, 'sar': sar_turun(h, l, mula),
                 'st': X('X14'), 'macd': X('X09'), 'rsi50': X('X11'), 'di': X('X24'), 'vol': X('X22')}
        for j, k in enumerate(HARIAN):
            G[j] = baris[k]
        D = np.stack([X('X13'), c > M[20] + J_EXT * atr, L['L1'][1] > 0, L['L1'][3] > 0, L['L2'][8] > 0]).astype(np.uint8)
    ls = pd.Series(l)
    LI = np.stack([np.where(i - k + 1 >= awal, ls.rolling(k).min().to_numpy(), np.nan) for k in (10, 20)])
    return G, D, LI


# ---------- enjin ----------
@njit(parallel=True, cache=True)
def atom26(ev, o, h, l, c, atr, akhir, G, D, LI):
    """Satu laluan ke hadapan (hingga 252 sesi) bagi setiap isyarat; sesi beli = indeks 0, nilai = indeks sesi jualan (BESAR = tiada).
    XS/PS[n, 13] stop loss; XB/PB[n, 2] stop loss dinaikkan ke harga beli; XN[n, 4] potong belian yang tidak menjadi;
    XT[n, 33, 8] tanda trend x bila mula dipakai; XJ[n, 5] tutup >= +10 / +20 / +50 %, RSI > 80, terlalu jauh di atas purata;
    XP[n, 2] pasaran; XE[n] laporan kewangan berikutnya; nm[n] sesi selepas sesi beli yang ada dalam data."""
    n = ev.shape[0]
    ns = S_JENIS.shape[0]
    XS = np.full((n, ns), BESAR, np.int16)
    PS = np.full((n, ns), np.nan, np.float32)
    XB = np.full((n, 2), BESAR, np.int16)
    PB = np.full((n, 2), np.nan, np.float32)
    XN = np.full((n, 4), BESAR, np.int16)
    XT = np.full((n, NT1, 8), BESAR, np.int16)
    XJ = np.full((n, 5), BESAR, np.int16)
    XP = np.full((n, 2), BESAR, np.int16)
    XE = np.full(n, BESAR, np.int16)
    nm = np.zeros(n, np.int32)
    for k in prange(n):
        i = ev[k]
        e = i + 1
        P = o[e]
        a0 = atr[i]
        m = akhir[k] - e
        nm[k] = m
        Ls = np.empty(ns)
        for s in range(ns):
            if S_JENIS[s] == 1:
                Ls[s] = P * (1.0 - S_NILAI[s])
            elif S_JENIS[s] == 3:
                q = int(S_NILAI[s])
                paras = l[i] if q == 0 else LI[q - 1, i]
                lantai = P - G_LANTAI * a0
                Ls[s] = lantai if (np.isnan(paras) or paras > lantai) else paras
            else:
                Ls[s] = P - S_NILAI[s] * a0
        akt = np.full(8, BESAR, np.int64)
        for a in range(4):
            akt[a] = A_HARI[a]
        hc = c[e]
        hh = h[e]
        sedia = np.zeros(2, np.bool_)
        cond = np.zeros(NT1, np.bool_)
        for d in range(min(m, DMAX) + 1):
            b = e + d
            cb = c[b]
            for s in range(ns):
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
            for q in range(2):
                if sedia[q] and XB[k, q] == BESAR:
                    if o[b] <= P:
                        XB[k, q], PB[k, q] = d, o[b] / P
                    elif l[b] <= P:
                        XB[k, q], PB[k, q] = d, 1.0
            if cb >= P + BE_ATR * a0:
                sedia[0] = True
            if cb >= P * BE_PCT:
                sedia[1] = True
            if cb > hc:
                hc = cb
            if h[b] > hh:
                hh = h[b]
            for a in range(4):
                if akt[4 + a] == BESAR and cb >= P * A_NAIK[a]:
                    akt[4 + a] = d
            if d < m:
                if d == 4 and cb < P:
                    XN[k, 0] = 5
                if d == 9:
                    if cb < P:
                        XN[k, 1] = 10
                    if cb < P + a0:
                        XN[k, 2] = 10
                if d == 19 and cb < P:
                    XN[k, 3] = 20
            if d < 2 or d >= m or d + 1 > DMAX:
                continue
            for j in range(NG):
                cond[j] = G[j, b] > 0
            for j in range(5):
                cond[NG + j] = cb < hc - CH_K[j] * atr[b]
            cond[NG + 5] = cb < hh - HH_K * atr[b]
            for j in range(4):
                cond[NG + 6 + j] = cb < TR_X[j] * hc
            for j in range(NT1):
                if cond[j]:
                    for a in range(8):
                        if XT[k, j, a] == BESAR and d >= akt[a]:
                            XT[k, j, a] = d + 1
            for j in range(3):
                if XJ[k, j] == BESAR and cb >= P * J_NAIK[j]:
                    XJ[k, j] = d + 1
            for j in range(2):
                if XJ[k, 3 + j] == BESAR and D[j, b] > 0:
                    XJ[k, 3 + j] = d + 1
                if XP[k, j] == BESAR and D[2 + j, b] > 0:
                    XP[k, j] = d + 1
            if XE[k] == BESAR and d >= E_MULA and D[4, b] > 0:
                XE[k] = d + 1
    return XS, PS, XB, PB, XN, XT, XJ, XP, XE, nm


@njit(parallel=True, cache=True)
def stat26(ev, tid, tp, o, c, XS, PS, XB, PB, XN, XT, XJ, XP, XE, nm, C):
    """Satu posisi setiap saham (ikut sesi jual cara itu sendiri) -> S[cara, NSTAT]. C[cara, 10] = indeks pilihan setiap komponen."""
    n, nw = ev.shape[0], C.shape[0]
    S = np.full((nw, NSTAT), np.nan, np.float32)
    for w in prange(nw):
        s, pn, t, a, kq, j, bq, p, eq = C[w, 0], C[w, 1], C[w, 2], C[w, 3], C[w, 4], C[w, 5], C[w, 6], C[w, 7], C[w, 8]
        cap = HAD_A[C[w, 9]] - 1
        tutup = S_JENIS[s] == 2
        buf = np.empty(n, np.int32)
        t_akhir, b_akhir, m = -1, -1, 0
        ju = jg = js = u3 = g3 = 0.0
        mng = r15 = k50 = tb = n3 = 0
        for k in range(n):
            if tid[k] == t_akhir and ev[k] <= b_akhir:
                continue
            e = ev[k] + 1
            P = o[e]
            x = np.int64(XS[k, s])
            px = np.float64(PS[k, s])
            if bq > 0:
                xb = np.int64(XB[k, bq - 1])
                if xb < x or (xb == x and not tutup and xb < BESAR):
                    x, px = xb, np.float64(PB[k, bq - 1])
            x20 = np.int64(XJ[k, 1])
            xo = np.int64(BESAR)
            if pn > 0:
                xo = min(xo, np.int64(XN[k, pn - 1]))
            if t > 0:
                xo = min(xo, np.int64(XT[k, t - 1, a]))
            if kq > 0:
                xo = min(xo, np.int64(XT[k, K_T[kq], K_A[kq]]))
            xpe = np.int64(BESAR)
            if p > 0:
                xpe = min(xpe, np.int64(XP[k, p - 1]))
            if eq > 0:
                xpe = min(xpe, np.int64(XE[k]))
            xo = min(xo, xpe)
            if j == 7:
                if x20 <= ONEIL_SESI:
                    if not xo < x20:                          # masih dipegang apabila +20 % dicapai dalam 3 minggu: pegang 8 minggu
                        xo = xpe
                        if t > 0:
                            xo = min(xo, np.int64(XT[k, t - 1, A_M40]))
                else:
                    xo = min(xo, x20)
            elif j == 3:
                xo = min(xo, x20)
            elif j == 4:
                xo = min(xo, np.int64(XJ[k, 2]))
            elif j == 5:
                xo = min(xo, np.int64(XJ[k, 3]))
            elif j == 6:
                xo = min(xo, np.int64(XJ[k, 4]))
            if xo < BESAR and xo <= x:
                x, px = xo, o[e + xo] / P
            nk = np.int64(nm[k])
            buka = False
            if x <= min(cap, nk):
                r, sk = px, x
            elif cap <= nk:
                r, sk = c[e + cap] / P, cap
            else:
                r, sk, buka = c[e + nk] / P, nk, True
            if j == 1 or j == 2:
                xj = np.int64(XJ[k, j - 1])
                if xj <= sk:
                    r = 0.5 * (o[e + xj] / P) + 0.5 * r
            r = r - 1.0 - KOS
            t_akhir, b_akhir = tid[k], ev[k] + 1 + sk
            buf[m] = sk + 1
            m += 1
            js += sk + 1
            if r > 0:
                ju += r
                mng += 1
            else:
                jg -= r
            r15 += r <= -0.15
            k50 += r >= 0.50
            tb += buka
            if tp[k] == 2:
                n3 += 1
                if r > 0:
                    u3 += r
                else:
                    g3 -= r
        S[w, 0], S[w, 9] = m, n3
        if m == 0:
            continue
        S[w, 1], S[w, 2], S[w, 3], S[w, 4], S[w, 5] = ju, jg, mng / m, r15 / m, k50 / m
        S[w, 6], S[w, 7], S[w, 8], S[w, 10], S[w, 11] = np.median(buf[:m]), js / m, tb / m, u3, g3
    return S


HAD_A = np.array(HAD, np.int64)


# ---------- konteks satu kumpulan saham ----------
class Konteks:
    def __init__(self, kerja, set_, rawak=False):
        import cs_lapis as lapis
        import cs_semak11 as s11
        t0 = time.time()
        self.set, self.pan = set_, cari.panel(kerja, set_)
        pan = self.pan
        G, D, LI = siri(pan, lapis.muat(kerja, set_))
        if rawak:                                             # kawalan: bar layak rawak, benih tetap (sama seperti CS25)
            sah = np.flatnonzero(s11.sah126(pan))
            self.E = {'RAWAK': np.sort(np.random.default_rng(BENIH_KAWALAN).choice(sah, N_KAWALAN, replace=False)).astype(np.int64)}
        else:
            self.E = c25.isyarat(kerja, set_, pan)
        self.ids = sorted(self.E, key=lambda i: int(i[1:]) if i[1:].isdigit() else 0)
        self.U = np.unique(np.concatenate([self.E[i] for i in self.ids]))
        akhir = (pan['mula'][pan['tid'][self.U] + 1] - 1).astype(np.int64)
        self.A = atom26(self.U, pan['o'], pan['h'], pan['l'], pan['c'], pan['atr'], akhir, G, D, LI)
        cari.log(f'CS26 {set_}{" rawak" if rawak else ""}: {len(self.ids)} setup · {len(self.U):,} isyarat berbeza · atom siap {time.time() - t0:.0f}s')

    def stat(self, i, C):
        ev, pan = self.E[i], self.pan
        if not len(ev):
            return np.full((len(C), NSTAT), np.nan, np.float32)
        ix = np.searchsorted(self.U, ev)
        return stat26(ev, pan['tid'][ev].astype(np.int64), pan['tempoh'][ev].astype(np.int64), pan['o'], pan['c'],
                      *(a[ix] for a in self.A), np.ascontiguousarray(C, dtype=np.int64))

    def nilai(self, C, fail=None):
        """S[setup, cara, NSTAT]; dengan `fail`, titik semak setiap 200 setup (larian boleh disambung)."""
        C = np.ascontiguousarray(C, dtype=np.int64)
        S, mula_j, t0 = np.full((len(self.ids), len(C), NSTAT), np.nan, np.float32), 0, time.time()
        fj = fail + '.json' if fail else None
        if fail and os.path.exists(fail) and os.path.exists(fj):
            sedia = json.load(open(fj))
            if sedia['ids'] == self.ids and sedia['cara'] == len(C):
                S, mula_j = np.load(fail), sedia['siap']
                cari.log(f'CS26 {self.set}: sambung dari setup {mula_j}')
        for j, i in enumerate(self.ids):
            if j < mula_j:
                continue
            S[j] = self.stat(i, C)
            if fail and ((j + 1) % 200 == 0 or j + 1 == len(self.ids)):
                np.save(fail + '.tmp.npy', S)
                os.replace(fail + '.tmp.npy', fail)
                json.dump({'ids': self.ids, 'cara': len(C), 'siap': j + 1}, open(fj, 'w'))
                cari.log(f'  CS26 {self.set}: {j + 1}/{len(self.ids)} · {time.time() - t0:.0f}s · RSS {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss // 1024} MB')
        return S


# ---------- ruang carian ----------
def jiran(g):
    """Semua cara yang berbeza SATU komponen daripada g (bentuk piawai, tanpa g sendiri)."""
    out = []
    for i in range(NK):
        for v in range(len(KOMPONEN[i])):
            if v != g[i]:
                x = list(g)
                x[i] = v
                x = kanon(x)
                if x != kanon(g) and x not in out:
                    out.append(x)
    return out


def tahap1():
    """Peringkat (i) + (ii): cara sekarang, satu demi satu, kemudian 8,000 cara rawak (benih tetap). Senarai tuple piawai, tanpa ulangan."""
    out = [kanon(ASAS)] + jiran(ASAS)
    n_satu = len(out)
    ada = set(out)
    rng = np.random.default_rng(BENIH_RAWAK)
    while len(out) < n_satu + N_RAWAK:
        g = kanon(tuple(int(rng.integers(len(k))) for k in KOMPONEN))
        if g not in ada:
            ada.add(g)
            out.append(g)
    return out, n_satu


def nisbah(S):
    """Nisbah untung : rugi daripada statistik [..., NSTAT] (rugi 0 -> NISBAH_MAKS; tiada dagangan -> NaN)."""
    u, g = np.asarray(S[..., IX['untung']], np.float64), np.asarray(S[..., IX['rugi']], np.float64)
    with np.errstate(divide='ignore', invalid='ignore'):
        r = np.where(g > 0, np.minimum(u / g, NISBAH_MAKS), np.where(u > 0, NISBAH_MAKS, np.nan))
    return r


def purata(S):
    with np.errstate(divide='ignore', invalid='ignore'):
        return (np.asarray(S[..., IX['untung']], np.float64) - np.asarray(S[..., IX['rugi']], np.float64)) / np.asarray(S[..., IX['n']], np.float64)


def tamak(K, cara, SA, ok):
    """Peringkat (iii): naik bukit pada kumpulan A. Pulangkan (cara tambahan, statistik A tambahan, laluan)."""
    indeks = {g: q for q, g in enumerate(cara)}
    semua = [SA]
    med = lambda S_: np.nanmedian(nisbah(S_[ok]), axis=0)
    nilai = list(med(SA))
    kini = int(np.nanargmax(nilai))
    laluan = [dict(pusingan=0, cara=kod(cara[kini]), nisbah_A=float(nilai[kini]))]
    for pus in range(1, TAMAK_MAKS + 1):
        J = jiran(cara[kini])
        baharu = [g for g in J if g not in indeks]
        if baharu:
            Sx = K.nilai(np.array(baharu))
            semua.append(Sx)
            for g, v in zip(baharu, med(Sx)):
                indeks[g] = len(cara)
                cara.append(g)
                nilai.append(float(v))
        terbaik = max((indeks[g] for g in J), key=lambda q: -np.inf if np.isnan(nilai[q]) else nilai[q])
        cari.log(f'CS26 naik bukit {pus}: {kod(cara[kini])} {nilai[kini]:.4f} -> {kod(cara[terbaik])} {nilai[terbaik]:.4f} ({len(baharu)} cara baharu)')
        if not nilai[terbaik] >= nilai[kini] + TAMAK_MIN:
            break
        kini = terbaik
        laluan.append(dict(pusingan=pus, cara=kod(cara[kini]), nisbah_A=float(nilai[kini])))
    return cara, np.concatenate(semua, axis=1), laluan


def kira(kerja):
    """A: peringkat (i) + (ii) dan naik bukit -> cs26_A.npy, cs26_cara.json; B: semua cara -> cs26_B.npy; kawalan -> cs26_kawalan.npy."""
    fc = F_(kerja, 'cara.json')
    cara, n_satu = tahap1()
    if not os.path.exists(fc):
        KB = Konteks(kerja, 'B')                              # hanya untuk bilangan dagangan cara sekarang (syarat >= 30 dalam kedua-dua kumpulan)
        nB = KB.nilai(np.array([kanon(ASAS)]))[:, 0, 0]
        ids_B = KB.ids
        del KB
        KA = Konteks(kerja, 'A')
        assert KA.ids == ids_B
        SA = KA.nilai(np.array(cara), F_(kerja, 'A1.npy'))
        ok = (SA[:, 0, 0] >= MIN_N) & (nB >= MIN_N)
        cara, SA, laluan = tamak(KA, cara, SA, ok)
        np.save(F_(kerja, 'A.npy'), SA)
        json.dump(dict(ids=KA.ids, cara=[kod(g) for g in cara], n_satu=n_satu, n_tahap1=n_satu + N_RAWAK, laluan=laluan), open(fc, 'w'))
        del KA, SA
    meta = json.load(open(fc))
    C = np.array([dari_kod(k) for k in meta['cara']])
    if not os.path.exists(F_(kerja, 'B.npy')):
        KB = Konteks(kerja, 'B')
        assert KB.ids == meta['ids']
        np.save(F_(kerja, 'B.npy'), KB.nilai(C, F_(kerja, 'B1.npy')))
        del KB
    if not os.path.exists(F_(kerja, 'kawalan.npy')):
        KR = Konteks(kerja, 'B', rawak=True)
        np.save(F_(kerja, 'kawalan.npy'), KR.nilai(C)[0])
    cari.log(f"CS26 kira: {len(C)} cara ({meta['n_satu']} satu demi satu, {N_RAWAK} rawak, {len(C) - meta['n_tahap1']} naik bukit) · siap")


# CS25 -> CS26: cara yang wujud dalam kedua-dua pusingan
_T25 = {'t0': 't0', 't1': 'ma10', 't2': 'ma20', 't3': 'ma50', 't4': 'ma100', 't5': '2ma20', 't6': '2ma50', 't7': 'ch3', 't8': 'ch4', 't9': 'ch6',
        't10': 'ch8', 't11': 'll10', 't12': 'll20', 't13': 'tr15', 't14': 'tr25'}


def dari25(k):
    s, b, m, t, j, h = k.split('.')
    return kanon(dari_kod('|'.join([s, 'n0', _T25[t], m, 'k0', j, b, 'q0', 'e0', h])))


def pariti(kerja, n_setup=120, n_cara=150):
    """Cara yang wujud dalam CS25 mesti memberi angka CS25 yang sama (kumpulan B; enjin CS25 dijalankan semula)."""
    K = Konteks(kerja, 'B')
    rng = np.random.default_rng(26)
    w25 = np.unique(np.concatenate([[c25.SEKARANG], rng.choice(c25.W, n_cara, replace=False)]))
    C = np.array([dari25(c25.KOD[w]) for w in w25])
    ids = [i for i in K.ids if len(K.E[i])][::max(1, len(K.ids) // n_setup)]
    beza = 0.0
    for i in ids:
        ev = K.E[i]
        a = c25.stat_panel(K.pan, ev, c25.atom_panel(K.pan, ev), cara=w25).astype(np.float64)
        b = K.stat(i, C)
        d = np.nanmax(np.abs(np.stack([b[:, 0] - a[:, 0], purata(b) - a[:, c25.IX['purata']], b[:, IX['menang']] - a[:, c25.IX['menang']],
                                       b[:, IX['rugi15']] - a[:, c25.IX['rugi15']], b[:, IX['sesi_med']] - a[:, c25.IX['sesi_med']]])))
        beza = max(beza, float(d))
    out = {'setup': len(ids), 'cara': len(w25), 'beza_terbesar': beza, 'lulus': bool(beza < 2e-5)}
    json.dump(out, open(F_(kerja, 'pariti.json'), 'w'))
    cari.log(f'CS26 pariti: {out}')
    return out


if __name__ == '__main__':
    cmd, kerja = sys.argv[1], sys.argv[2]
    if cmd == 'lapor':
        import cs_keluar26_lapor as lp
        lp.lapor_(kerja)
    else:
        {'kira': kira, 'pariti': pariti}[cmd](kerja)
