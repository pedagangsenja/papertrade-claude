"""E3 — INSTRUMEN `IS02`: putaran bakul sektor. Pradaftar `REVERSE/SPEC_INSTRUMEN.md`.

11 bakul sektor sintetik berat sama rata, dibina daripada alam `AL02` (SPUS) dengan harga
yang sudah ada di cakera — setiap hos data pasaran langsung disekat dalam sesi ini (spec §2).

Mekanik BERBEZA daripada E1/E2 (spec §3): 11 instrumen dengan imbang berkala, bukan
pemilihan daripada ribuan saham dengan peraturan keluar setiap posisi. Maka `step24.simulasi`
TIDAK diguna dan kawalan regresi E1/E2 tidak terpakai; ganti­nya enjin ini membawa kawalannya
sendiri (pegang-semua dan pilihan rawak) pada enjin yang sama.

Guna: python3 REVERSE/step26_instrumen.py [--benih 20] [--laporan-sahaja]
"""
import argparse
import collections
import csv
import re
import sys
import time
from pathlib import Path

import numpy as np
import pandas as pd

AKAR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(AKAR))
import REVERSE.pembinaan as PB  # noqa: E402
import REVERSE.step25_alam as S25  # noqa: E402
from REVERSE.teras import kos as K  # noqa: E402

KELUAR = AKAR / 'REVERSE'
SKRIN = AKAR / 'BacktestShariah2' / 'data' / 'skrin'

UJI0 = '2020-01-01'
LATIH0, LATIH1 = '2012-01-01', '2019-12-31'
N_BENIH = 20
MIN_AHLI = 7                      # spec §2 — sektor dengan >= 7 ahli SPUS
T1_CAGR, T1_MDD = 17.95, -26.82   # SPUS, konvensyen CAGR-seluruh-tingkap
T3_CAGR, T3_MDD = 15.0, -15.0
AMBANG_NISBAH = 0.669

# spec §4 — grid tetap
URUT = ['U11', 'U14', 'U03', 'RAWAK']
KK = [1, 2, 3, 5, 11]
IMBANG = [21, 63]


def peta_sektor():
    """(sektor -> senarai ticker SPUS). SPTE dibuang; sektor < MIN_AHLI dibuang."""
    sp = [r['ticker'] for r in csv.DictReader(open(SKRIN / 'etf_shariah.csv',
                                                   encoding='utf-8'))
          if r['etf'] == 'SPUS']
    sp = sorted({x for x in sp if re.fullmatch(r'[A-Z]{1,5}', x)})
    tv = {r['ticker']: r['sector']
          for r in csv.DictReader(open(SKRIN / 'tv_us.csv', encoding='utf-8'))}
    c = collections.Counter(tv[t] for t in sp if tv.get(t))
    return {s: [t for t in sp if tv.get(t) == s]
            for s, n in sorted(c.items(), key=lambda x: -x[1]) if n >= MIN_AHLI}


def bina_bakul(P, ahli):
    """(nama, aras_tutup, aras_buka, nilai20) bagi setiap bakul.

    Aras ialah indeks pulangan berat sama rata diimbang HARIAN:
      tutup_t = tutup_{t-1} x (1 + purata(C_t / C_{t-1} - 1))
      buka_t  = tutup_{t-1} x (1 + purata(O_t / C_{t-1} - 1))
    Purata hanya merentas ahli yang mempunyai KEDUA-DUA bar (t-1 dan t); hari tanpa ahli sah
    membawa pulangan 0 supaya siri tidak putus.
    """
    it = {t: i for i, t in enumerate(P.tick)}
    m = len(P.tarikh)
    nama, TU, BU, NI = [], [], [], []
    for s, tk in ahli.items():
        idx = np.array([it[t] for t in tk if t in it], dtype='int64')
        if idx.size < 5:
            continue
        # float64: panel disimpan float32, dan aras dikompaun 3,772 langkah — dalam
        # float32 itu terkumpul kepada ~3e-7 ralat relatif (disahkan dalam ujian asap).
        C = P.C[idx].astype('float64')    # (ahli, hari)
        O = P.O[idx].astype('float64')
        rc = np.full((idx.size, m), np.nan)
        ro = np.full((idx.size, m), np.nan)
        rc[:, 1:] = C[:, 1:] / C[:, :-1] - 1.0
        ro[:, 1:] = O[:, 1:] / C[:, :-1] - 1.0
        # Ahli sah = mempunyai KEDUA-DUA pulangan, supaya siri tutup dan siri buka memakai
        # keanggotaan yang SAMA (bakul yang tidak boleh didagang tidak boleh diindeks).
        # Ujian asap mengukur 0 bar dengan tutup sah tetapi buka hilang, jadi ini tidak
        # mengubah apa-apa nombor; ia menutup kemungkinan sahaja.
        sah = np.isfinite(rc) & np.isfinite(ro)
        n_sah = sah.sum(0)
        mc = np.where(n_sah > 0, np.where(sah, rc, 0.0).sum(0) / np.maximum(n_sah, 1), 0.0)
        mo = np.where(n_sah > 0, np.where(sah, ro, 0.0).sum(0) / np.maximum(n_sah, 1), 0.0)
        tu = np.empty(m)
        tu[0] = 100.0
        for j in range(1, m):
            tu[j] = tu[j - 1] * (1.0 + mc[j])
        bu = np.empty(m)
        bu[0] = 100.0
        bu[1:] = tu[:-1] * (1.0 + mo[1:])
        ni = np.nansum(P.N[idx].astype('float64'), axis=0)   # nilai bakul = jumlah ahli
        nama.append(s); TU.append(tu); BU.append(bu); NI.append(ni)
    return nama, np.array(TU), np.array(BU), np.array(NI)


def skor(TU, a, cara):
    """Skor momentum pada sauh `a` (guna maklumat sampai hari `a` sahaja)."""
    if cara == 'U11':                      # pulangan gabungan 1 + 3 + 6 bulan
        return sum(TU[:, a] / TU[:, max(0, a - n)] - 1.0 for n in (21, 63, 126))
    if cara == 'U14':                      # momentum 12 - 1 bulan
        return TU[:, max(0, a - 21)] / TU[:, max(0, a - 252)] - 1.0
    # U03 Clenow: cerun regresi log 90 hari x R^2
    n = 90
    j0 = max(0, a - n + 1)
    y = np.log(np.maximum(TU[:, j0:a + 1], 1e-12))
    x = np.arange(y.shape[1], dtype='float64')
    xm, ym = x.mean(), y.mean(axis=1, keepdims=True)
    sxx = ((x - xm) ** 2).sum()
    b = ((x - xm) * (y - ym)).sum(axis=1) / sxx
    sse = ((y - ym - b[:, None] * (x - xm)) ** 2).sum(axis=1)
    sst = ((y - ym) ** 2).sum(axis=1)
    r2 = np.where(sst > 0, 1.0 - sse / sst, 0.0)
    return (np.exp(b * 252) - 1.0) * r2


def simulasi(TU, BU, NI, k, imbang, cara, benih, m0, hari):
    """Ekuiti harian putaran bakul. Imbang setiap `imbang` sesi, beli pada BUKA esok."""
    rng = np.random.default_rng(benih)
    nb, m = TU.shape
    unit = np.zeros(nb)
    tunai, prev = 1.0, 1.0
    ek = np.full(m, np.nan)
    pul, n_dag, kos_jum = [], 0, 0.0
    pilih_lepas = np.zeros(nb, bool)
    masuk_px = np.zeros(nb)
    kos_wang, ekuiti_jum, n_hari = 0.0, 0.0, 0
    for d in range(1, m):
        a = d - 1
        if a >= 252 and (a - 252) % imbang == 0:
            if k >= nb:
                pilih = np.ones(nb, bool)
            elif cara == 'RAWAK':
                pilih = np.zeros(nb, bool)
                pilih[rng.choice(nb, k, replace=False)] = True
            else:
                sc = np.nan_to_num(skor(TU, a, cara), nan=-9e9)
                pilih = np.zeros(nb, bool)
                pilih[np.argsort(-sc, kind='stable')[:k]] = True
            # jual yang keluar pada BUKA hari d
            for i in np.flatnonzero(pilih_lepas & ~pilih):
                ks = K.kos_sisi(NI[i, a])
                kasar = unit[i] * BU[i, d]
                tunai += kasar * (1 - ks)
                if a >= m0 and masuk_px[i] > 0:
                    pul.append(BU[i, d] * (1 - ks) / masuk_px[i] - 1.0)
                kos_wang += kasar * ks
                unit[i] = 0.0
            # imbang semula yang kekal + beli yang masuk, berat sama rata 1/k
            nilai = tunai + float((unit * BU[:, d]).sum())
            sasar = nilai / max(1, int(pilih.sum()))
            for i in np.flatnonzero(pilih):
                ks = K.kos_sisi(NI[i, a])
                semasa = unit[i] * BU[i, d]
                beza = sasar - semasa
                if abs(beza) < 1e-12:
                    continue
                if beza > 0:
                    belanja = min(beza, tunai)
                    if belanja <= 1e-12:
                        continue
                    tambah = belanja * (1 - ks) / BU[i, d]
                    if unit[i] <= 0:
                        masuk_px[i] = BU[i, d] / (1 - ks)
                        n_dag += 1
                    unit[i] += tambah
                    tunai -= belanja
                    kos_wang += belanja * ks
                else:
                    kurang = min(-beza / BU[i, d], unit[i])
                    unit[i] -= kurang
                    tunai += kurang * BU[i, d] * (1 - ks)
                    kos_wang += kurang * BU[i, d] * ks
            pilih_lepas = pilih
        ek[d] = prev = tunai + float((unit * TU[:, d]).sum())
        if d >= m0:
            ekuiti_jum += ek[d]
            n_hari += 1
    # seretan kos = jumlah kos dibayar sebagai % purata ekuiti dalam tingkap keputusan
    purata_ek = ekuiti_jum / n_hari if n_hari else 1.0
    return ek, pul, n_dag, kos_wang / purata_ek * 100.0


def ringkas(R):
    g = (R.groupby(['urutan', 'k', 'imbang'])
          .agg(cagr=('cagr', 'median'), mdd=('mdd', 'median'),
               cagr_p5=('cagr', lambda x: float(np.percentile(x, 5))),
               cagr_p95=('cagr', lambda x: float(np.percentile(x, 95))),
               cagr_latih=('cagr_latih', 'median'), mdd_latih=('mdd_latih', 'median'),
               n_dag=('n_dagangan', 'median'), kos_tahun=('kos_tahun', 'median'),
               nb=('benih', 'size')).reset_index())
    g['nisbah'] = g.cagr / g.mdd.abs()
    ctl = {(r.k, r.imbang): r.cagr_p95
           for r in g[g.urutan == 'RAWAK'].itertuples()}
    g['ctl_p95'] = [ctl.get((r.k, r.imbang), np.nan) for r in g.itertuples()]
    g['P1'] = g.cagr > T1_CAGR
    g['P2'] = g.mdd >= T1_MDD
    # spec §8: pada k = 11 tiada pemilihan berlaku, jadi P3 tidak dinilai di sana
    g['P3'] = np.where((g.urutan == 'RAWAK') | (g.k >= 11), False, g.cagr > g.ctl_p95)
    g['P4'] = g.nisbah > AMBANG_NISBAH
    g['T1'] = g.P1 & g.P2
    g['T3'] = (g.cagr >= T3_CAGR) & (g.mdd >= T3_MDD)
    return g.sort_values('cagr', ascending=False)


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument('--benih', type=int, default=N_BENIH)
    ap.add_argument('--laporan-sahaja', action='store_true')
    a = ap.parse_args(argv)
    f = KELUAR / 'instrumen.csv'
    if a.laporan_sahaja and f.exists():
        return laporan(pd.read_csv(f))

    t0 = time.time()
    print('1/3 panel + bakul...', flush=True)
    P = PB.Panel()
    ahli = peta_sektor()
    nama, TU, BU, NI = bina_bakul(P, ahli)
    print(f'  {len(nama)} bakul daripada {sum(len(v) for v in ahli.values())} ticker '
          f'[{time.time() - t0:.0f}s]', flush=True)
    for s in nama:
        print(f'    {len(ahli[s]):3d}  {s}', flush=True)

    hari = pd.DatetimeIndex(P.tarikh)
    m0 = int(np.searchsorted(P.tarikh, np.datetime64(UJI0)))
    l0 = int(np.searchsorted(P.tarikh, np.datetime64(LATIH0)))
    l1 = int(np.searchsorted(P.tarikh, np.datetime64(LATIH1)))
    tahun = (hari[-1] - hari[m0]).days / 365.25

    print('2/3 beli-dan-pegang setiap bakul...', flush=True)
    bh = []
    for i, s in enumerate(nama):
        bh.append(dict(bakul=s, n_ahli=len(ahli[s]),
                       cagr=PB.cagr(TU[i, m0:], hari[m0:]), mdd=PB.mdd(TU[i, m0:]),
                       cagr_latih=PB.cagr(TU[i, l0:l1], hari[l0:l1])))
    pd.DataFrame(bh).to_csv(KELUAR / 'instrumen_bakul.csv', index=False,
                            float_format='%.4f')

    print('3/3 simulasi putaran...', flush=True)
    baris = []
    for cara in URUT:
        for k in KK:
            for imb in IMBANG:
                benih = range(1, a.benih + 1) if cara == 'RAWAK' and k < len(nama) else [0]
                for bn in benih:
                    ek, pul, nd, kj = simulasi(TU, BU, NI, k, imb, cara, bn, m0, hari)
                    e5, t5 = (S25.ekor_bahagian(pul) if len(pul) >= 20
                              else (np.nan, np.nan))
                    baris.append(dict(
                        urutan=cara, k=k, imbang=imb, benih=bn,
                        cagr=PB.cagr(ek[m0:], hari[m0:]), mdd=PB.mdd(ek[m0:]),
                        cagr_latih=PB.cagr(ek[l0:l1], hari[l0:l1]),
                        mdd_latih=PB.mdd(ek[l0:l1]),
                        n_dagangan=nd, kos_tahun=kj / tahun,
                        pul_dag=float(np.mean(pul) * 100) if pul else np.nan,
                        ekor5=e5, tanpa5=t5))
        print(f'  {cara}: siap [{time.time() - t0:.0f}s]', flush=True)
    R = pd.DataFrame(baris)
    R.to_csv(f, index=False, float_format='%.4f')
    return laporan(R)


def laporan(R):
    g = ringkas(R)
    g.to_csv(KELUAR / 'instrumen_ringkas.csv', index=False, float_format='%.4f')
    print()
    print(f'SPUS 2020-2025: CAGR {T1_CAGR:.2f}%  MDD {T1_MDD:.2f}%')
    print(f'{len(g)} konfigurasi · T1 {int(g.T1.sum())} · T3 {int(g.T3.sum())} · '
          f'P3 {int(g.P3.sum())} · P4 {int(g.P4.sum())}')
    menang = g[(g.T1 | g.T3)]
    if len(menang):
        print()
        print('Sel yang mencapai T1 atau T3 (spec §5 jadual keputusan):')
        for r in menang.itertuples():
            kes = ('BERHENTI-MENANG (pemilihan berfungsi)' if r.P3
                   else ('PEGANG SEMUA = kepelbagaian bukan pemilihan, T4 dalam samaran'
                         if r.k >= 11 else 'kepelbagaian bukan pemilihan'))
            print(f'  {r.urutan:6s} k={r.k:2d} imbang {r.imbang:2d}: '
                  f'CAGR {r.cagr:+.2f}% MDD {r.mdd:.2f}% nisbah {r.nisbah:.2f} '
                  f'T1={r.T1} T3={r.T3} P3={r.P3}  -> {kes}')
    else:
        print('  Tiada sel mencapai T1 atau T3 -> teruskan ke E4.')
    pb = KELUAR / 'instrumen_bakul.csv'
    if pb.exists():
        print()
        print('Beli-dan-pegang setiap bakul (2020-2025):')
        print(pd.read_csv(pb).sort_values('cagr', ascending=False).to_string(
            index=False, float_format=lambda v: f'{v:.2f}'))
    print()
    kol = ['urutan', 'k', 'imbang', 'nb', 'cagr', 'cagr_p5', 'cagr_p95', 'mdd', 'nisbah',
           'n_dag', 'kos_tahun', 'T1', 'T3', 'P3', 'P4']
    print(g.head(20)[kol].to_string(index=False, float_format=lambda v: f'{v:.2f}'))
    print()
    e = R[(R.k.isin([1, 3, 11])) & (R.imbang == 21)].groupby(['urutan', 'k'])[
        ['pul_dag', 'ekor5', 'tanpa5']].median().reset_index()
    print('Diagnostik ekor bakul (spec §6; banding E2: AL01 saham 101.67%/-0.081%, '
          'AL02 saham 47.92%/+2.682%):')
    print(e.to_string(index=False, float_format=lambda v: f'{v:.2f}'))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
