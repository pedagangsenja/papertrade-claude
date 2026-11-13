"""Carian setup CS01 — teras numba: mekanik dagangan (SPEC §4) dan pengumpulan skor (SPEC §6).

Sesi 0 = hari beli (bar e = bar isyarat + 1), harga beli P = buka[e].
- Henti aktif intrahari mulai sesi 1; pada sesi 0 hanya TUTUP <= paras yang mencetus jualan pada buka sesi 1.
- Keluar indikator dinilai pada tutup sesi 0..18 -> jual pada BUKA sesi berikutnya.
- Tiada keluar -> jual pada TUTUP sesi 19 (sesi ke-20).
Hari pegang: jual pada buka sesi d -> d; henti intrahari sesi d -> d + 1; had masa -> 20.
"""
import numpy as np
from numba import njit, prange

TMAX = 20
KOS = 0.005
TIADA = 99
NH = 4                       # bilangan pilihan henti


def peraturan_keluar(n_atom):
    """Senarai peraturan keluar: X00 (tiada), tunggal, pasangan ATAU, pasangan DAN.
    Pulangkan (a1, a2, op) int16; op: 0 tiada, 1 tunggal, 2 ATAU, 3 DAN."""
    a1, a2, op = [0], [0], [0]
    for a in range(n_atom):
        a1.append(a); a2.append(a); op.append(1)
    for o in (2, 3):
        for a in range(n_atom):
            for b in range(a + 1, n_atom):
                a1.append(a); a2.append(b); op.append(o)
    return np.asarray(a1, np.int16), np.asarray(a2, np.int16), np.asarray(op, np.int16)


def nama_keluar(r, a1, a2, op, senarai):
    if op[r] == 0:
        return 'X00 tiada keluar indikator (henti + 20 sesi)'
    if op[r] == 1:
        return senarai[a1[r]]
    return f"{senarai[a1[r]]} {'ATAU' if op[r] == 2 else 'DAN'} {senarai[a2[r]]}"


@njit(cache=True)
def _ctz(x):
    n = 0
    while (x & 1) == 0:
        x >>= 1
        n += 1
    return n


@njit(cache=True)
def _satu(i, o, h, l, c, atr, X, jenis, par, m, L, ds, ps, h0):
    """Isi topeng atom m[a] (bit d = benar pada tutup sesi d, d = 0..18) dan keadaan henti bagi isyarat bar i."""
    e = i + 1
    P = o[e]
    L[0] = P * 0.92
    L[1] = P * 0.90
    L[2] = P - 3.0 * atr[i]
    L[3] = P - 4.0 * atr[i]
    for a in range(m.shape[0]):
        m[a] = 0
    hc = c[e]
    for d in range(TMAX - 1):
        b = e + d
        if c[b] > hc:
            hc = c[b]
        for a in range(m.shape[0]):
            if jenis[a] == 0:
                ya = X[a, b] != 0
            elif jenis[a] == 1:
                ya = c[b] < hc - par[a] * atr[b]
            else:
                ya = c[b] < par[a] * hc
            if ya:
                m[a] |= (1 << d)
    for s in range(NH):
        h0[s] = c[e] <= L[s]
        ds[s] = TIADA
        ps[s] = 0.0
        for d in range(1, TMAX):
            b = e + d
            if o[b] <= L[s]:
                ds[s] = d
                ps[s] = o[b]
                break
            if l[b] <= L[s]:
                ds[s] = d
                ps[s] = L[s]
                break
    return P


@njit(cache=True)
def _hasil(e, P, mr, s, o, c, ds, ps, h0):
    """(R, hari pegang, sesi keluar) bagi topeng keluar mr dan henti s."""
    if h0[s]:
        mr |= 1
    dx = TIADA
    if mr != 0:
        dx = _ctz(mr) + 1
    if dx != TIADA and dx <= ds[s]:
        return o[e + dx] / P - 1.0 - KOS, dx, dx
    if ds[s] != TIADA:
        return ps[s] / P - 1.0 - KOS, ds[s] + 1, ds[s]
    return c[e + TMAX - 1] / P - 1.0 - KOS, TMAX, TMAX - 1


@njit(cache=True)
def _topeng_peraturan(m, a1, a2, op, r):
    if op[r] == 0:
        return 0
    if op[r] == 1:
        return m[a1[r]]
    if op[r] == 2:
        return m[a1[r]] | m[a2[r]]
    return m[a1[r]] & m[a2[r]]


@njit(parallel=True, cache=True)
def hasil_semua(ev, o, h, l, c, atr, X, jenis, par, a1, a2, op):
    """R (float32) bagi setiap isyarat dalam ev x setiap (henti, peraturan keluar). Lajur = s * nR + r."""
    nR = a1.shape[0]
    out = np.empty((ev.shape[0], NH * nR), np.float32)
    for k in prange(ev.shape[0]):
        m = np.zeros(X.shape[0], np.int64)
        L = np.zeros(NH)
        ds = np.zeros(NH, np.int64)
        ps = np.zeros(NH)
        h0 = np.zeros(NH, np.bool_)
        i = ev[k]
        P = _satu(i, o, h, l, c, atr, X, jenis, par, m, L, ds, ps, h0)
        for r in range(nR):
            mr = _topeng_peraturan(m, a1, a2, op, r)
            for s in range(NH):
                out[k, s * nR + r] = _hasil(i + 1, P, mr, s, o, c, ds, ps, h0)[0]
    return out


@njit(parallel=True, cache=True)
def hasil_satu(ev, o, h, l, c, atr, X, jenis, par, a1, a2, op, s, r):
    """(R, hari pegang, sesi keluar, harga jual) bagi satu (henti s, peraturan keluar r)."""
    n = ev.shape[0]
    R = np.empty(n)
    hp = np.empty(n, np.int64)
    sk = np.empty(n, np.int64)
    for k in prange(n):
        m = np.zeros(X.shape[0], np.int64)
        L = np.zeros(NH)
        ds = np.zeros(NH, np.int64)
        ps = np.zeros(NH)
        h0 = np.zeros(NH, np.bool_)
        i = ev[k]
        P = _satu(i, o, h, l, c, atr, X, jenis, par, m, L, ds, ps, h0)
        R[k], hp[k], sk[k] = _hasil(i + 1, P, _topeng_peraturan(m, a1, a2, op, r), s, o, c, ds, ps, h0)
    return R, hp, sk


@njit(cache=True)
def _lb(n, s, q):
    """Had bawah = purata - 2 sd / sqrt(n); pulangkan (lb, purata, sd)."""
    mu = s / n
    v = q / n - mu * mu
    sd = np.sqrt(v) if v > 0 else 0.0
    return mu - 2.0 * sd / np.sqrt(n), mu, sd


@njit(parallel=True, cache=True)
def kumpul_tambah(Rm, tp, Fm, f1, f2, S, Q, N2):
    """Tambah jumlah dan jumlah kuasa dua R setiap lajur ke S/Q [gabungan penapis, tempoh, lajur] dan bilangan N2.
    Gabungan penapis (f1, f2): -1 = tiada."""
    K = Rm.shape[1]
    for ci in prange(f1.shape[0]):
        a, b = f1[ci], f2[ci]
        for k in range(Rm.shape[0]):
            if a >= 0 and Fm[k, a] == 0:
                continue
            if b >= 0 and Fm[k, b] == 0:
                continue
            p = tp[k]
            N2[ci, p] += 1
            for j in range(K):
                v = Rm[k, j]
                S[ci, p, j] += v
                Q[ci, p, j] += v * v


@njit(parallel=True, cache=True)
def kumpul_skor(S, Q, N2, rawak, n_min, n_atas, tepi):
    """Skor setiap lajur = min(LB Latih, LB Sah) bagi gabungan dengan n >= n_min dalam kedua-dua tempoh.
    Pulangkan n_atas lajur terbaik + statistik, statistik satu lajur rawak, dan histogram skor.
    Statistik: [skor, purata L, sd L, purata S, sd S]."""
    nC, K = S.shape[0], S.shape[2]
    idx = np.full((nC, n_atas), -1, np.int64)
    st = np.zeros((nC, n_atas, 5), np.float32)
    stw = np.zeros((nC, 5), np.float32)
    hist = np.zeros((nC, tepi.shape[0] + 1), np.int64)
    for ci in prange(nC):
        if N2[ci, 0] < n_min or N2[ci, 1] < n_min:
            continue
        skor = np.empty(K)
        for j in range(K):
            l0 = _lb(N2[ci, 0], S[ci, 0, j], Q[ci, 0, j])[0]
            l1 = _lb(N2[ci, 1], S[ci, 1, j], Q[ci, 1, j])[0]
            skor[j] = l0 if l0 < l1 else l1
            hist[ci, np.searchsorted(tepi, skor[j])] += 1
        j = rawak[ci]
        _, m0, d0 = _lb(N2[ci, 0], S[ci, 0, j], Q[ci, 0, j])
        _, m1, d1 = _lb(N2[ci, 1], S[ci, 1, j], Q[ci, 1, j])
        stw[ci, 0] = skor[j]; stw[ci, 1] = m0; stw[ci, 2] = d0; stw[ci, 3] = m1; stw[ci, 4] = d1
        for t in range(n_atas):
            j = np.argmax(skor)
            _, m0, d0 = _lb(N2[ci, 0], S[ci, 0, j], Q[ci, 0, j])
            _, m1, d1 = _lb(N2[ci, 1], S[ci, 1, j], Q[ci, 1, j])
            idx[ci, t] = j
            st[ci, t, 0] = skor[j]; st[ci, t, 1] = m0; st[ci, t, 2] = d0; st[ci, t, 3] = m1; st[ci, t, 4] = d1
            skor[j] = -np.inf
    return idx, st, stw, hist


@njit(cache=True)
def satu_posisi(ev, sk, tid):
    """Peraturan satu posisi setiap saham: isyarat semasa saham masih dipegang diabaikan.
    ev tersusun menaik; sk = sesi keluar (bar keluar = ev + 1 + sk). Pulangkan topeng boolean."""
    ambil = np.zeros(ev.shape[0], np.bool_)
    t_akhir = -1
    b_akhir = -1
    for k in range(ev.shape[0]):
        if tid[ev[k]] != t_akhir or ev[k] > b_akhir:
            ambil[k] = True
            t_akhir = tid[ev[k]]
            b_akhir = ev[k] + 1 + sk[k]
    return ambil


@njit(cache=True)
def buku_harian(ev, R, sk, hp, o, c, hari, n_hari):
    """Pulangan harian buku sama berat semua posisi terbuka (kos dibahagi dua: hari beli dan hari jual)."""
    jum = np.zeros(n_hari)
    bil = np.zeros(n_hari)
    for k in range(ev.shape[0]):
        e = ev[k] + 1
        P = o[e]
        jual = (R[k] + KOS + 1.0) * P
        dulu = P
        for d in range(sk[k] + 1):
            b = e + d
            if d == sk[k]:
                # jual pada buka (hp == sk), henti intrahari, atau tutup sesi akhir: harga jual sebenar
                r = jual / dulu - 1.0 - KOS / 2
            else:
                r = c[b] / dulu - 1.0
                dulu = c[b]
            if d == 0:
                r -= KOS / 2
            jum[hari[b]] += r
            bil[hari[b]] += 1
    out = np.zeros(n_hari)
    for i in range(n_hari):
        if bil[i] > 0:
            out[i] = jum[i] / bil[i]
    return out
