"""Kajian — lengkung TEMPOH PEGANG dan lengkung SLOT. Pradaftar `REVERSE/SPEC_PEGANG_SLOT.md`.

2 masuk x 8 slot x 2 keluar x 5 had-pegang x 2 urutan = 320 konfigurasi;
`U01` 20 benih -> 3,360 larian simulasi.

Enjin, panel harga, topeng isyarat dan model kos diguna semula daripada
`REVERSE/step22_portfolio_n.py` dan `REVERSE/pembinaan.py` — tiada enjin kedua.
Yang baharu di sini hanya dua perkara: had tempoh pegangan dalam peraturan keluar, dan
diagnostik setiap dagangan (pulangan, tempoh, pusing ganti, posisi terbuka) yang diperlukan
untuk membaca lengkung.

Guna: python3 REVERSE/step24_pegang_slot.py [--benih 20] [--laporan-sahaja]
Output: REVERSE/pegang_slot.csv, REVERSE/pegang_slot_ringkas.csv
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
import REVERSE.step22_portfolio_n as S22  # noqa: E402
from REVERSE.teras import kos as K  # noqa: E402

KELUAR = AKAR / 'REVERSE'

UJI0, UJI1 = '2020-01-01', '2025-12-31'
LATIH0, LATIH1 = '2012-01-01', '2019-12-31'
HAD_IMBAS = 504
RSI_KELUAR = 70.0
TRAIL_ATR = 4.0
N_BENIH = 20
AMBANG_NISBAH = 0.669          # spec §4 P4

# spec §3 — grid tetap, tiada penambahan selepas melihat keputusan
MASUK = ['GB02_atau3', 'RAWAK']
SLOT = [8, 20, 40, 80, 160, 320, 640, 1280]   # spec §3.1: kapasiti kolam 753-1,739
RULE = ['X13', 'X15']
CAP = [None, 63, 42, 21, 10]   # had tempoh pegangan dalam bar; None = tiada had
URUT = ['U01', 'U08']


# ---------------------------------------------------------------- keluar
def keluar(P, RSI, ti, a, rule, cap, cache):
    """(idx_keluar, harga_masuk, harga_keluar) dengan had tempoh pegangan.

    Sama seperti `step22.keluar`, tetapi `cap` memotong bar keluar kepada paling lewat
    `e + cap - 1` (harga diambil pada buka bar berikutnya), jadi tempoh pegangan paling
    panjang ialah `cap` bar. Had hanya MEMOTONG; ia tidak pernah melanjutkan pegangan.
    """
    kunci = (ti, a, rule, cap)
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
    if cap is not None:
        bar = min(bar, e + cap - 1)
    k, px = harga_pada(min(bar + 1, akhir))
    hasil = (k, masuk, px)
    cache[kunci] = hasil
    return hasil


# ---------------------------------------------------------------- simulasi
def simulasi(P, RSI, ATRP, RSP, CAL, slot, rule, cap, urut, benih, cache, m0):
    """Ekuiti harian, pendedahan harian dan diagnostik setiap dagangan bagi satu larian.

    Diagnostik dikumpul hanya bagi dagangan yang DIMASUKI dalam tingkap keputusan
    (indeks sauh >= m0), supaya purata tidak dicampur dengan tingkap latih.
    """
    rng = np.random.default_rng(benih)
    m = len(P.tarikh)
    tunai, prev, n_dag = 1.0, 1.0, 0
    buka = []                      # (ti, unit, idx_keluar, px_keluar, idx_masuk, belanja)
    ek = np.full(m, np.nan)
    dz = np.full(m, np.nan)
    nb = np.zeros(m)
    pul, pgg, kos_pp = [], [], []
    for d in range(1, m):
        if buka:
            for p in [x for x in buka if x[2] == d]:
                ko = K.kos_sisi(P.N[p[0], d])
                tunai += p[1] * p[3] * (1 - ko)
                if p[4] >= m0:
                    pul.append(p[1] * p[3] * (1 - ko) / p[5] - 1.0)
                    pgg.append(d - p[4])
                    kos_pp.append(ko + K.kos_sisi(P.N[p[0], p[4] - 1]))
                buka.remove(p)
        a = d - 1
        cal = CAL.get(a)
        if cal is not None and cal.size and len(buka) < slot:
            if urut == 'U01':
                cal = cal[rng.permutation(cal.size)]
            else:                                   # U08 ATR% menaik
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
                kx, _, pkeluar = keluar(P, RSI, ti, a, rule, cap, cache)
                if kx <= d:
                    continue
                unit = belanja * (1 - K.kos_sisi(P.N[ti, a])) / float(P.O[ti, d])
                tunai -= belanja
                buka.append((ti, unit, kx, pkeluar, d, belanja))
                pegang.add(ti)
                n_dag += 1
        nilai = tunai
        for ti, unit, _, _, _, _ in buka:
            c = P.C[ti, d]
            if np.isfinite(c):
                nilai += unit * float(c)
        ek[d] = prev = nilai
        dz[d] = 1.0 - (tunai / nilai if nilai > 0 else 1.0)
        nb[d] = len(buka)
    diag = dict(n_tutup=len(pul),
                pulangan_dagangan=float(np.mean(pul) * 100) if pul else np.nan,
                pegang_purata=float(np.mean(pgg)) if pgg else np.nan,
                kos_pp=float(np.mean(kos_pp) * 100) if kos_pp else np.nan,
                buka_purata=float(np.mean(nb[m0:])))
    return ek, dz, n_dag, diag


# ---------------------------------------------------------------- larian
def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument('--benih', type=int, default=N_BENIH)
    ap.add_argument('--laporan-sahaja', action='store_true')
    a = ap.parse_args(argv)
    f = KELUAR / 'pegang_slot.csv'
    if a.laporan_sahaja and f.exists():
        return laporan(pd.read_csv(f))

    t0 = time.time()
    print('1/5 isyarat GB02...', flush=True)
    S = S22.bina_isyarat()
    print(f'  {len(S):,} bar berisyarat  [{time.time() - t0:.0f}s]', flush=True)

    print('2/5 panel harga...', flush=True)
    P = PB.Panel()
    print(f'  {len(P.tick):,} ticker x {len(P.tarikh):,} sesi  [{time.time() - t0:.0f}s]',
          flush=True)

    print('3/5 matriks rsi14 + rs_pst...', flush=True)
    RSI = S22._matriks(P, S18.PANEL, 'rsi14')
    S18.rs_persentil()
    RSP = S22._matriks(P, S22.RSPF, 'rs_pst')
    ATRP = P.A / np.where(P.C > 0, P.C, np.nan)
    print(f'  siap  [{time.time() - t0:.0f}s]', flush=True)

    print('4/5 calon setiap sauh...', flush=True)
    LAYAK = S22.peta_layak(P)
    it = {t: i for i, t in enumerate(P.tick)}
    idt = {d: i for i, d in enumerate(P.tarikh)}
    S = S[S.ticker.isin(it)]
    ii = S.ticker.map(it).to_numpy()
    jj = np.array([idt.get(d, -1) for d in S.date.to_numpy()])
    ok = jj >= 0
    ii, jj = ii[ok], jj[ok]
    CAL = {'RAWAK': LAYAK}
    msk = S.a3.to_numpy()[ok]
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
    CAL['GB02_atau3'] = d
    print(f'  GB02_atau3: {sum(v.size for v in d.values()):,} calon layak merentas '
          f'{len(d):,} sesi', flush=True)

    hari = pd.DatetimeIndex(P.tarikh)
    m0 = int(np.searchsorted(P.tarikh, np.datetime64(UJI0)))
    l0 = int(np.searchsorted(P.tarikh, np.datetime64(LATIH0)))
    l1 = int(np.searchsorted(P.tarikh, np.datetime64(LATIH1)))
    tahun = (hari[-1] - hari[m0]).days / 365.25

    print('5/5 simulasi...', flush=True)
    baris = []
    for rule in RULE:
        for cap in CAP:
            # cache keluar dikongsi dalam kumpulan (keluar, had) ini sahaja. Kuncinya
            # membawa `rule` dan `cap` juga supaya salah guna merentas kumpulan tidak boleh
            # memulangkan jawapan yang salah secara senyap.
            cache = {}
            for mk in MASUK:
                # pagar OOM (pelajaran 31 Okt 2026: larian terdahulu meledak ke 13.97 GB)
                if len(cache) > 4_000_000:
                    cache.clear()
                for slot in SLOT:
                    for urut in URUT:
                        for bn in (range(1, a.benih + 1) if urut == 'U01' else [0]):
                            ek, dz, nd, dg = simulasi(P, RSI, ATRP, RSP, CAL[mk], slot,
                                                      rule, cap, urut, bn, cache, m0)
                            baris.append(dict(
                                masuk=mk, slot=slot, keluar=rule,
                                pegang='tiada' if cap is None else str(cap),
                                urutan=urut, benih=bn,
                                cagr=PB.cagr(ek[m0:], hari[m0:]), mdd=PB.mdd(ek[m0:]),
                                dedah=float(np.nanmean(dz[m0:]) * 100), n_dagangan=nd,
                                cagr_latih=PB.cagr(ek[l0:l1], hari[l0:l1]),
                                mdd_latih=PB.mdd(ek[l0:l1]),
                                pusing_slot_tahun=dg['n_tutup'] / slot / tahun,
                                kos_tahun=dg['n_tutup'] / slot / tahun * dg['kos_pp']
                                if dg['kos_pp'] == dg['kos_pp'] else np.nan,
                                **dg))
            print(f'  {rule} had {cap}: siap  [{time.time() - t0:.0f}s] '
                  f'({len(cache):,} keluar dicache)', flush=True)
            del cache
    R = pd.DataFrame(baris)
    R.to_csv(f, index=False, float_format='%.4f')
    return laporan(R)


def laporan(R):
    pa = PB.penanda_aras()
    sp_c, sp_m, _ = pa['SPUS']
    kunci = ['masuk', 'slot', 'keluar', 'pegang', 'urutan']
    g = (R.groupby(kunci)
          .agg(cagr=('cagr', 'median'), mdd=('mdd', 'median'),
               cagr_p5=('cagr', lambda x: float(np.percentile(x, 5))),
               cagr_p95=('cagr', lambda x: float(np.percentile(x, 95))),
               dedah=('dedah', 'median'), n=('n_dagangan', 'median'),
               cagr_latih=('cagr_latih', 'median'), mdd_latih=('mdd_latih', 'median'),
               pul_dag=('pulangan_dagangan', 'median'),
               pegang_bar=('pegang_purata', 'median'),
               pusing=('pusing_slot_tahun', 'median'),
               kos_tahun=('kos_tahun', 'median'),
               buka=('buka_purata', 'median'),
               nb=('benih', 'size')).reset_index())
    g['nisbah'] = g.cagr / g.mdd.abs()
    ctl = {(r.slot, r.keluar, r.pegang, r.urutan): r.cagr_p95
           for r in g[g.masuk == 'RAWAK'].itertuples()}
    g['ctl_p95'] = [ctl.get((r.slot, r.keluar, r.pegang, r.urutan), np.nan)
                    for r in g.itertuples()]
    g['P1'] = g.cagr > sp_c
    g['P2'] = g.mdd >= sp_m
    g['P3'] = np.where(g.masuk == 'RAWAK', False, g.cagr > g.ctl_p95)
    g['P4'] = g.nisbah > AMBANG_NISBAH
    g['lulus'] = g.P1 & g.P2 & g.P3 & g.P4
    # spec §5: slot tidak mengikat apabila posisi terbuka purata < slot -> itulah kolam penuh
    g['tepu'] = g.buka < g.slot * 0.95
    g = g.sort_values('cagr', ascending=False)
    g.to_csv(KELUAR / 'pegang_slot_ringkas.csv', index=False, float_format='%.4f')

    print()
    print(f'SPUS 2020-2025: CAGR {sp_c:.2f}%  MDD {sp_m:.2f}%  '
          f'nisbah {sp_c / abs(sp_m):.3f}')
    print(f'gate: P1 {int(g.P1.sum())}  P2 {int(g.P2.sum())}  P3 {int(g.P3.sum())}  '
          f'P4 {int(g.P4.sum())}  ->  LULUS SEMUA {int(g.lulus.sum())} / {len(g)}')

    # Q1 — lengkung had pegangan: beza CAGR lawan `tiada had` pada sel yang sama
    print()
    print('Q1  lengkung HAD PEGANGAN (CAGR median, mata beza lawan "tiada")')
    base = {(r.masuk, r.slot, r.keluar, r.urutan): r.cagr
            for r in g[g.pegang == 'tiada'].itertuples()}
    q1 = g[g.masuk == 'GB02_atau3'].copy()
    q1['d_tiada'] = [r.cagr - base.get((r.masuk, r.slot, r.keluar, r.urutan), np.nan)
                     for r in q1.itertuples()]
    piv = q1.pivot_table(index=['keluar', 'urutan', 'slot'], columns='pegang',
                         values='cagr', aggfunc='median')
    print(piv.to_string(float_format=lambda v: f'{v:7.2f}'))
    menang = q1[(q1.pegang != 'tiada') & (q1.d_tiada > 0)]
    print(f'  sel di mana had MENGALAHKAN "tiada": {len(menang)} / '
          f'{len(q1[q1.pegang != "tiada"])}')

    # Q2 — lengkung slot
    print()
    print('Q2  lengkung SLOT (GB02_atau3; CAGR / MDD / nisbah / posisi terbuka purata)')
    for (rule, cap, urut), sub in g[g.masuk == 'GB02_atau3'].groupby(
            ['keluar', 'pegang', 'urutan']):
        sub = sub.sort_values('slot')
        s = '  '.join(f'{int(r.slot):>3d}:{r.cagr:+6.2f}/{r.mdd:+6.1f}/{r.nisbah:4.2f}'
                      f'/{r.buka:5.1f}' for r in sub.itertuples())
        print(f'  {rule} had {cap:5s} {urut}  {s}')

    print()
    kol = ['masuk', 'slot', 'keluar', 'pegang', 'urutan', 'nb', 'cagr', 'cagr_p5',
           'cagr_p95', 'mdd', 'nisbah', 'dedah', 'pul_dag', 'pegang_bar', 'pusing',
           'kos_tahun', 'buka', 'P1', 'P2', 'P3', 'P4']
    print(g.head(30)[kol].to_string(index=False, float_format=lambda v: f'{v:.2f}'))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
