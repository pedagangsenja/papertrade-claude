"""E4 — KELUAR peringkat PORTFOLIO (`X31`, `X32`). Pradaftar
`REVERSE/SPEC_KELUAR_PORTFOLIO.md`.

Putaran berpangkat pada saham alam `AL02`: pada setiap tarikh imbang, portfolio menjadi
k teratas mengikut metrik pangkat, dipilih daripada (pegangan semasa + calon berisyarat).
Pegangan dijual HANYA apabila ia keluar daripada k teratas — tiada henti, tiada sasaran.

`X31` ialah kes khas dengan metrik dikunci kepada pulangan 252 hari (spec §2).

Mekanik berbeza daripada `step24` (jam imbang, bukan keluar setiap posisi), jadi kawalan
regresi E1/E2 tidak terpakai; enjin membawa kawalannya sendiri (masuk `RAWAK`, pangkat
`U01` 20 benih).

Guna: python3 REVERSE/step27_keluar_portfolio.py [--benih 20] [--laporan-sahaja]
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
import REVERSE.step25_alam as S25  # noqa: E402
from REVERSE.teras import kos as K  # noqa: E402

KELUAR = AKAR / 'REVERSE'

UJI0 = '2020-01-01'
LATIH0, LATIH1 = '2012-01-01', '2019-12-31'
N_BENIH = 20
T1_CAGR, T1_MDD = 17.95, -26.82
T3_CAGR, T3_MDD = 15.0, -15.0
AMBANG_NISBAH = 0.669
RUJUK_E2 = 21.01          # spec §3 — CAGR terbaik keluar setiap posisi pada AL02

MASUK = ['GB02_atau3', 'RAWAK']
SLOT = [8, 20, 40]
IMBANG = [21, 63]
URUT = ['U02', 'U14', 'U01']     # X32 sahaja; X31 mengunci metriknya sendiri


def skor_pangkat(P, RSP, a, cara, rng=None):
    """Skor pangkat setiap ticker pada sauh `a`. Hanya maklumat sampai `a` diguna."""
    if cara == 'U01':
        return rng.random(len(P.tick))
    if cara == 'U02':
        return np.nan_to_num(RSP[:, a], nan=-1.0)
    # Hanya DUA lajur diambil: menyalin seluruh P.C ke float64 pada setiap imbang ialah
    # 98 MB setiap panggilan (ditangkap semasa menulis, bukan selepas larian).
    if cara == 'U14':                       # momentum 12 - 1 bulan
        a1, a2 = max(0, a - 21), max(0, a - 252)
    else:                                   # X31: pulangan 252 hari
        a1, a2 = a, max(0, a - 252)
    with np.errstate(invalid='ignore', divide='ignore'):
        s = P.C[:, a1].astype('float64') / P.C[:, a2].astype('float64') - 1.0
    return np.nan_to_num(s, nan=-9e9, posinf=-9e9, neginf=-9e9)


def simulasi(P, RSP, CAL, LAYAK, slot, imbang, cara, benih, m0):
    """Ekuiti harian putaran berpangkat. Imbang setiap `imbang` sesi, dagang pada BUKA."""
    rng = np.random.default_rng(benih)
    m = len(P.tarikh)
    tunai = 1.0
    unit = {}                 # ti -> unit
    masuk_px = {}
    ek = np.full(m, np.nan)
    dz = np.full(m, np.nan)
    nb = np.zeros(m)
    pul, n_dag, kos_wang = [], 0, 0.0
    for d in range(1, m):
        a = d - 1
        if a >= 252 and (a - 252) % imbang == 0:
            cal = CAL.get(a)
            lay = LAYAK.get(a)
            sc = None
            if lay is not None:
                boleh = set(int(x) for x in lay)
                kolam = set(int(x) for x in (cal if cal is not None else []))
                kolam |= {t for t in unit if t in boleh}
                if kolam:
                    sc = skor_pangkat(P, RSP, a, cara, rng)
                    urut = sorted(kolam, key=lambda t: -sc[t])
                    sah = [t for t in urut
                           if np.isfinite(P.O[t, d]) and P.O[t, d] > 0]
                    pilih = set(sah[:slot])
                else:
                    pilih = set()
                # jual yang keluar daripada k teratas
                for ti in [t for t in list(unit) if t not in pilih]:
                    if not (np.isfinite(P.O[ti, d]) and P.O[ti, d] > 0):
                        continue
                    ks = K.kos_sisi(P.N[ti, a])
                    kasar = unit[ti] * float(P.O[ti, d])
                    tunai += kasar * (1 - ks)
                    kos_wang += kasar * ks
                    if a >= m0 and masuk_px.get(ti, 0) > 0:
                        pul.append(float(P.O[ti, d]) * (1 - ks) / masuk_px[ti] - 1.0)
                    del unit[ti]
                    masuk_px.pop(ti, None)
                # imbang semula kepada berat sama rata 1/slot
                nilai = tunai + sum(u * float(P.O[t, d]) for t, u in unit.items()
                                    if np.isfinite(P.O[t, d]))
                sasar = nilai / slot
                for ti in (sorted(pilih, key=lambda t: -sc[t]) if sc is not None else []):
                    px = float(P.O[ti, d])
                    ks = K.kos_sisi(P.N[ti, a])
                    semasa = unit.get(ti, 0.0) * px
                    beza = sasar - semasa
                    if beza > 1e-12:
                        belanja = min(beza, tunai)
                        if belanja <= 1e-12:
                            continue
                        if ti not in unit:
                            masuk_px[ti] = px / (1 - ks)
                            n_dag += 1
                        unit[ti] = unit.get(ti, 0.0) + belanja * (1 - ks) / px
                        tunai -= belanja
                        kos_wang += belanja * ks
                    elif beza < -1e-12:
                        kurang = min(-beza / px, unit[ti])
                        unit[ti] -= kurang
                        tunai += kurang * px * (1 - ks)
                        kos_wang += kurang * px * ks
        nilai = tunai
        for ti, u in unit.items():
            c = P.C[ti, d]
            if np.isfinite(c):
                nilai += u * float(c)
        ek[d] = nilai
        dz[d] = 1.0 - (tunai / nilai if nilai > 0 else 1.0)
        nb[d] = len(unit)
    e5, t5 = (S25.ekor_bahagian(pul) if len(pul) >= 20 else (np.nan, np.nan))
    diag = dict(n_tutup=len(pul), kos_wang=kos_wang,
                pul_dag=float(np.mean(pul) * 100) if pul else np.nan,
                ekor5=e5, tanpa5=t5,
                dedah=float(np.nanmean(dz[m0:]) * 100),
                buka_purata=float(np.mean(nb[m0:])))
    return ek, n_dag, diag


def ringkas(R):
    g = (R.groupby(['masuk', 'keluar', 'urutan', 'slot', 'imbang'])
          .agg(cagr=('cagr', 'median'), mdd=('mdd', 'median'),
               cagr_p5=('cagr', lambda x: float(np.percentile(x, 5))),
               cagr_p95=('cagr', lambda x: float(np.percentile(x, 95))),
               cagr_latih=('cagr_latih', 'median'), dedah=('dedah', 'median'),
               n_dag=('n_dagangan', 'median'), kos_tahun=('kos_tahun', 'median'),
               pul_dag=('pul_dag', 'median'), ekor5=('ekor5', 'median'),
               tanpa5=('tanpa5', 'median'), buka=('buka_purata', 'median'),
               nb=('benih', 'size')).reset_index())
    g['nisbah'] = g.cagr / g.mdd.abs()
    ctl = {(r.masuk, r.slot, r.imbang): r.cagr_p95
           for r in g[g.urutan == 'U01'].itertuples()}
    g['ctl_p95'] = [ctl.get((r.masuk, r.slot, r.imbang), np.nan) for r in g.itertuples()]
    g['P1'] = g.cagr > T1_CAGR
    g['P2'] = g.mdd >= T1_MDD
    g['P3'] = np.where(g.urutan == 'U01', False, g.cagr > g.ctl_p95)
    g['P4'] = g.nisbah > AMBANG_NISBAH
    g['T1'] = g.P1 & g.P2
    g['T3'] = (g.cagr >= T3_CAGR) & (g.mdd >= T3_MDD)
    return g.sort_values('cagr', ascending=False)


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument('--benih', type=int, default=N_BENIH)
    ap.add_argument('--laporan-sahaja', action='store_true')
    a = ap.parse_args(argv)
    f = KELUAR / 'keluar_portfolio.csv'
    if a.laporan_sahaja and f.exists():
        return laporan(pd.read_csv(f))

    t0 = time.time()
    print('1/3 panel + alam AL02...', flush=True)
    S = S22.bina_isyarat()
    P = PB.Panel()
    S18.rs_persentil()
    RSP = S22._matriks(P, S22.RSPF, 'rs_pst')
    it = {t: i for i, t in enumerate(P.tick)}
    idx_sp = np.array(sorted(it[t] for t in S25.alam_spus() if t in it), dtype='int64')
    LAYAK = S25.potong(S22.peta_layak(P), idx_sp)
    print(f'  {len(idx_sp)} ticker SPUS  [{time.time() - t0:.0f}s]', flush=True)

    print('2/3 calon berisyarat...', flush=True)
    idt = {d: i for i, d in enumerate(P.tarikh)}
    S = S[S.ticker.isin(it)]
    ii = S.ticker.map(it).to_numpy()
    jj = np.array([idt.get(d, -1) for d in S.date.to_numpy()])
    ok = jj >= 0
    ii, jj = ii[ok], jj[ok]
    msk = S.a3.to_numpy()[ok]
    d = {}
    o = np.argsort(jj[msk], kind='stable')
    js, iss = jj[msk][o], ii[msk][o]
    b = np.flatnonzero(np.concatenate([[True], js[1:] != js[:-1], [True]]))
    for s_, e_ in zip(b[:-1], b[1:]):
        aa = int(js[s_])
        lay = LAYAK.get(aa)
        if lay is None:
            continue
        v = np.intersect1d(iss[s_:e_], lay, assume_unique=False)
        if v.size:
            d[aa] = v.astype('int64')
    CAL = {'GB02_atau3': d, 'RAWAK': LAYAK}
    print(f'  GB02_atau3 {sum(v.size for v in d.values()):,} calon  '
          f'[{time.time() - t0:.0f}s]', flush=True)

    hari = pd.DatetimeIndex(P.tarikh)
    m0 = int(np.searchsorted(P.tarikh, np.datetime64(UJI0)))
    l0 = int(np.searchsorted(P.tarikh, np.datetime64(LATIH0)))
    l1 = int(np.searchsorted(P.tarikh, np.datetime64(LATIH1)))
    tahun = (hari[-1] - hari[m0]).days / 365.25

    print('3/3 simulasi...', flush=True)
    baris = []
    kombo = [('X32', u) for u in URUT] + [('X31', 'tetap252')]
    for kel, cara in kombo:
        for mk in MASUK:
            for slot in SLOT:
                for imb in IMBANG:
                    for bn in (range(1, a.benih + 1) if cara == 'U01' else [0]):
                        ek, nd, dg = simulasi(P, RSP, CAL[mk], LAYAK, slot, imb, cara,
                                              bn, m0)
                        purata_ek = float(np.nanmean(ek[m0:]))
                        baris.append(dict(
                            masuk=mk, keluar=kel, urutan=cara, slot=slot, imbang=imb,
                            benih=bn,
                            cagr=PB.cagr(ek[m0:], hari[m0:]), mdd=PB.mdd(ek[m0:]),
                            cagr_latih=PB.cagr(ek[l0:l1], hari[l0:l1]),
                            n_dagangan=nd,
                            kos_tahun=dg['kos_wang'] / max(purata_ek, 1e-9) * 100 / tahun,
                            **{k: v for k, v in dg.items() if k != 'kos_wang'}))
        print(f'  {kel} {cara}: siap [{time.time() - t0:.0f}s]', flush=True)
    R = pd.DataFrame(baris)
    R.to_csv(f, index=False, float_format='%.4f')
    return laporan(R)


def laporan(R):
    g = ringkas(R)
    g.to_csv(KELUAR / 'keluar_portfolio_ringkas.csv', index=False, float_format='%.4f')
    terbaik = float(g.cagr.max())
    print()
    print(f'SPUS 2020-2025: CAGR {T1_CAGR:.2f}%  MDD {T1_MDD:.2f}%')
    print(f'{len(g)} konfigurasi · T1 {int(g.T1.sum())} · T3 {int(g.T3.sum())} · '
          f'P1 {int(g.P1.sum())} · P2 {int(g.P2.sum())} · P3 {int(g.P3.sum())} · '
          f'P4 {int(g.P4.sum())}')
    print(f'E4a keluar portfolio > keluar setiap posisi terbaik AL02 ({RUJUK_E2:.2f}%): '
          f'terbaik {terbaik:.2f}% -> {"LULUS" if terbaik > RUJUK_E2 else "GAGAL"}')
    print()
    kol = ['masuk', 'keluar', 'urutan', 'slot', 'imbang', 'nb', 'cagr', 'cagr_p5',
           'cagr_p95', 'mdd', 'nisbah', 'dedah', 'buka', 'n_dag', 'kos_tahun', 'pul_dag',
           'ekor5', 'tanpa5', 'T1', 'T3', 'P3', 'P4']
    print(g.head(18)[kol].to_string(index=False, float_format=lambda v: f'{v:.2f}'))
    print()
    print('Pendedahan terendah (spec §6: runtuhnya pendedahan ialah penjelasan, '
          'bukan pulangan):')
    print(g.sort_values('dedah').head(8)[
        ['masuk', 'keluar', 'urutan', 'slot', 'imbang', 'cagr', 'mdd', 'dedah', 'buka']
    ].to_string(index=False, float_format=lambda v: f'{v:.2f}'))
    print()
    print('X31 lawan X32/U14 pada sel sepadan (spec §7 jangkaan 5):')
    k = ['masuk', 'slot', 'imbang']
    x31 = g[g.keluar == 'X31'][k + ['cagr', 'mdd']]
    x32 = g[(g.keluar == 'X32') & (g.urutan == 'U14')][k + ['cagr', 'mdd']]
    m = x31.merge(x32, on=k, suffixes=('_X31', '_U14'))
    m['d_cagr'] = m.cagr_X31 - m.cagr_U14
    print(m.to_string(index=False, float_format=lambda v: f'{v:.2f}'))
    print(f'  median |beza| = {m.d_cagr.abs().median():.2f} mata (jangkaan < 3)')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
