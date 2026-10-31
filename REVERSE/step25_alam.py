"""E2 — ALAM `AL02`: kelebihan pada alam yang repo benar-benar dagang. Pradaftar
`REVERSE/SPEC_ALAM.md`.

2 masuk x 5 slot x 2 keluar x 4 had-pegang x 2 urutan = 160 konfigurasi pada `AL02`;
`U01` 20 benih -> 1,680 larian. Nombor `AL01` TIDAK dijana semula — ia dibaca daripada
`pegang_slot_ringkas.csv` (E1), supaya perbandingan memakai angka yang sudah dikomit.

Enjin: `step24.keluar` dan `step24.simulasi` diimport TERUS. Tiada enjin kedua. Alam
dikenakan dengan memotong peta calon kepada indeks ticker SPUS sahaja — tiada perubahan
kepada enjin, jadi kawalan regresi E1 kekal sah.

Guna: python3 REVERSE/step25_alam.py [--benih 20] [--laporan-sahaja]
"""
import argparse
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
import REVERSE.step18_nxx as S18  # noqa: E402
import REVERSE.step22_portfolio_n as S22  # noqa: E402
import REVERSE.step24_pegang_slot as S24  # noqa: E402

KELUAR = AKAR / 'REVERSE'
SKRIN = AKAR / 'BacktestShariah2' / 'data' / 'skrin' / 'etf_shariah.csv'

UJI0 = '2020-01-01'
LATIH0, LATIH1 = '2012-01-01', '2019-12-31'
N_BENIH = 20
AMBANG_NISBAH = 0.669
T1_CAGR, T1_MDD = 17.95, -26.82          # SPUS, konvensyen CAGR-seluruh-tingkap
T3_CAGR, T3_MDD = 15.0, -15.0

# spec §3 — grid tetap
MASUK = ['GB02_atau3', 'RAWAK']
SLOT = [8, 20, 40, 80, 160]
RULE = ['X13', 'X15']
CAP = [None, 63, 42, 21]
URUT = ['U01', 'U08']

# spec §5 — ambang keputusan, ditetapkan sebelum larian
AMBANG_P3 = 0.25      # (a) bahagian sel AL02 yang mesti mengalahkan kawalan p95
AMBANG_HAD = 0.50     # (b) bahagian sel yang had 42/63 mesti mengalahkan `tiada`


def alam_spus():
    """214 ticker SPUS yang wujud dalam panel. SPTE DIBUANG — ia ETF global (spec §2a)."""
    R = [r for r in csv.DictReader(open(SKRIN, encoding='utf-8')) if r['etf'] == 'SPUS']
    return sorted({r['ticker'] for r in R if re.fullmatch(r'[A-Z]{1,5}', r['ticker'])})


def potong(peta, sah):
    """Peta calon dipotong kepada indeks ticker dalam `sah` (set indeks panel)."""
    out = {}
    for a, v in peta.items():
        w = v[np.isin(v, sah)]
        if w.size:
            out[a] = w
    return out


def pulangan_setiap_dagangan(P, RSI, CAL, m0, rule='X13', cap=42):
    """Pulangan bersih SETIAP isyarat dalam tingkap keputusan, melalui `step24.keluar`.

    Ukuran setiap dagangan (bukan portfolio), supaya setanding dengan 63.7% yang
    `KOLAM_EKOR.md` ukur. Enjin keluar yang sama diguna, jadi tiada mekanik kedua.

    TIADA had bilangan: memotong pada N pertama memotong mengikut URUTAN SAUH, jadi sampel
    AL01 akan terdiri daripada awal 2020 sahaja (kejatuhan COVID) manakala AL02 merentas
    seluruh tingkap — itu bias masa, bukan perbezaan alam. Pepijat itu ditangkap dalam ujian
    asap sebelum larian.

    Konvensyen kos sama seperti enjin portfolio `step24.simulasi`: (1-ki)(1-ko)px/masuk - 1.
    """
    from REVERSE.teras import kos as K
    cache, out = {}, []
    for a in sorted(CAL):
        if a < m0:
            continue
        for t in CAL[a]:
            ti = int(t)
            kx, masuk, px = S24.keluar(P, RSI, ti, a, rule, cap, cache)
            if not (masuk > 0 and px > 0):
                continue
            ki = K.kos_sisi(P.N[ti, a])
            ko = K.kos_sisi(P.N[ti, kx])
            out.append((1 - ki) * (1 - ko) * px / masuk - 1.0)
    return out


def ekor_bahagian(pul):
    """(bahagian 5% teratas %, purata tanpa 5% teratas %).

    Bahagian jumlah pulangan hanya bermakna apabila jumlah itu POSITIF; jika tidak ia
    dilapor NaN. `tanpa5` tertakrif pada kedua-dua tanda dan itulah metrik yang seluruh
    kajian ini guna, jadi ia yang dibandingkan merentas alam.
    """
    if len(pul) < 20:
        return np.nan, np.nan
    x = np.sort(np.asarray(pul))[::-1]
    k = max(1, int(round(0.05 * len(x))))
    jum = x.sum()
    bhg = float(x[:k].sum() / jum * 100) if jum > 0 else np.nan
    return bhg, float(x[k:].mean() * 100)


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument('--benih', type=int, default=N_BENIH)
    ap.add_argument('--laporan-sahaja', action='store_true')
    a = ap.parse_args(argv)
    f = KELUAR / 'alam.csv'
    if a.laporan_sahaja and f.exists():
        return laporan(pd.read_csv(f))

    t0 = time.time()
    print('1/4 isyarat + panel...', flush=True)
    S = S22.bina_isyarat()
    P = PB.Panel()
    RSI = S22._matriks(P, S18.PANEL, 'rsi14')
    S18.rs_persentil()
    RSP = S22._matriks(P, S22.RSPF, 'rs_pst')
    ATRP = P.A / np.where(P.C > 0, P.C, np.nan)
    print(f'  {len(P.tick):,} ticker x {len(P.tarikh):,} sesi  [{time.time() - t0:.0f}s]',
          flush=True)

    print('2/4 alam SPUS...', flush=True)
    it = {t: i for i, t in enumerate(P.tick)}
    sp = alam_spus()
    idx_sp = np.array(sorted(it[t] for t in sp if t in it), dtype='int64')
    print(f'  {len(sp)} ticker SPUS, {len(idx_sp)} dalam panel', flush=True)

    print('3/4 calon setiap sauh...', flush=True)
    LAYAK = S22.peta_layak(P)
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
    CAL = {'GB02_atau3': potong(d, idx_sp), 'RAWAK': potong(LAYAK, idx_sp)}
    for k, v in CAL.items():
        print(f'  {k}: {sum(x.size for x in v.values()):,} calon layak merentas '
              f'{len(v):,} sesi', flush=True)

    hari = pd.DatetimeIndex(P.tarikh)
    m0 = int(np.searchsorted(P.tarikh, np.datetime64(UJI0)))
    l0 = int(np.searchsorted(P.tarikh, np.datetime64(LATIH0)))
    l1 = int(np.searchsorted(P.tarikh, np.datetime64(LATIH1)))
    tahun = (hari[-1] - hari[m0]).days / 365.25

    # spec §7 — diagnostik ekor SETIAP DAGANGAN (bukan gate), enjin keluar yang sama
    ek_baris = []
    for nama, peta in (('AL01', d), ('AL02', CAL['GB02_atau3'])):
        pul = pulangan_setiap_dagangan(P, RSI, peta, m0)
        bhg, tanpa5 = ekor_bahagian(pul)
        ek_baris.append(dict(alam=nama, n=len(pul),
                             min_pulangan=float(np.mean(pul) * 100) if pul else np.nan,
                             ekor5_pct=bhg, tanpa5=tanpa5))
        print(f'  ekor {nama}: n {len(pul):,} · min {ek_baris[-1]["min_pulangan"]:+.3f}% · '
              f'5% teratas = {bhg:.1f}% jumlah · tanpa5 {tanpa5:+.3f}%', flush=True)
    pd.DataFrame(ek_baris).to_csv(KELUAR / 'alam_ekor.csv', index=False,
                                  float_format='%.4f')

    print('4/4 simulasi AL02...', flush=True)
    baris = []
    for rule in RULE:
        for cap in CAP:
            cache = {}
            for mk in MASUK:
                for slot in SLOT:
                    for urut in URUT:
                        for bn in (range(1, a.benih + 1) if urut == 'U01' else [0]):
                            ek, dz, nd, dg = S24.simulasi(P, RSI, ATRP, RSP, CAL[mk], slot,
                                                          rule, cap, urut, bn, cache, m0)
                            baris.append(dict(
                                alam='AL02', masuk=mk, slot=slot, keluar=rule,
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
            print(f'  {rule} had {cap}: siap  [{time.time() - t0:.0f}s]', flush=True)
            del cache
    R = pd.DataFrame(baris)
    R.to_csv(f, index=False, float_format='%.4f')
    return laporan(R)


def _ringkas(R):
    R = R.copy()
    R['pegang'] = R.pegang.astype(str)
    kunci = ['alam', 'masuk', 'slot', 'keluar', 'pegang', 'urutan']
    g = (R.groupby(kunci)
          .agg(cagr=('cagr', 'median'), mdd=('mdd', 'median'),
               cagr_p5=('cagr', lambda x: float(np.percentile(x, 5))),
               cagr_p95=('cagr', lambda x: float(np.percentile(x, 95))),
               dedah=('dedah', 'median'), n=('n_dagangan', 'median'),
               cagr_latih=('cagr_latih', 'median'),
               pul_dag=('pulangan_dagangan', 'median'),
               pegang_bar=('pegang_purata', 'median'),
               pusing=('pusing_slot_tahun', 'median'),
               kos_tahun=('kos_tahun', 'median'), buka=('buka_purata', 'median'),
               nb=('benih', 'size')).reset_index())
    g['nisbah'] = g.cagr / g.mdd.abs()
    ctl = {(r.alam, r.slot, r.keluar, r.pegang, r.urutan): r.cagr_p95
           for r in g[g.masuk == 'RAWAK'].itertuples()}
    g['ctl_p95'] = [ctl.get((r.alam, r.slot, r.keluar, r.pegang, r.urutan), np.nan)
                    for r in g.itertuples()]
    g['P1'] = g.cagr > T1_CAGR
    g['P2'] = g.mdd >= T1_MDD
    g['P3'] = np.where(g.masuk == 'RAWAK', False, g.cagr > g.ctl_p95)
    g['P4'] = g.nisbah > AMBANG_NISBAH
    g['T1'] = g.P1 & g.P2
    g['T3'] = (g.cagr >= T3_CAGR) & (g.mdd >= T3_MDD)
    g['lulus'] = g.P1 & g.P2 & g.P3 & g.P4
    return g


def laporan(R):
    g2 = _ringkas(R)
    # AL01 TIDAK dijana semula (spec §3): dibaca daripada larian E1 yang sudah dikomit,
    # dipotong kepada sel yang sepadan dengan grid E2.
    e1 = pd.read_csv(KELUAR / 'pegang_slot.csv')
    e1['pegang'] = e1.pegang.astype(str)
    sah_cap = ['tiada'] + [str(c) for c in CAP if c]
    e1 = e1[e1.slot.isin(SLOT) & e1.pegang.isin(sah_cap) & e1.masuk.isin(MASUK)
            & e1.keluar.isin(RULE) & e1.urutan.isin(URUT)]
    g1 = _ringkas(e1.assign(alam='AL01'))
    g = pd.concat([g1, g2], ignore_index=True).sort_values(['alam', 'cagr'],
                                                           ascending=[True, False])
    g.to_csv(KELUAR / 'alam_ringkas.csv', index=False, float_format='%.4f')

    sig2 = g2[g2.masuk == 'GB02_atau3']
    a_lulus = int(sig2.P3.sum())
    a_kadar = a_lulus / len(sig2) if len(sig2) else 0.0
    sig1 = g1[g1.masuk == 'GB02_atau3']
    b1_kadar = int(sig1.P3.sum()) / len(sig1) if len(sig1) else 0.0

    # (b) had 42/63 lawan `tiada` pada sel yang sepadan
    def kadar_had(gg):
        base = {(r.masuk, r.slot, r.keluar, r.urutan): r.cagr
                for r in gg[gg.pegang == 'tiada'].itertuples()}
        sub = gg[(gg.masuk == 'GB02_atau3') & (gg.pegang.isin(['42', '63']))]
        men = sum(1 for r in sub.itertuples()
                  if r.cagr > base.get((r.masuk, r.slot, r.keluar, r.urutan), 9e9))
        return men, len(sub)

    m2, n2 = kadar_had(g2)
    m1, n1 = kadar_had(g1)

    print()
    print(f'SPUS 2020-2025: CAGR {T1_CAGR:.2f}%  MDD {T1_MDD:.2f}%')
    print(f'AL02: {len(g2)} konfigurasi · T1 {int(g2.T1.sum())} · T3 {int(g2.T3.sum())} · '
          f'lulus semua gate {int(g2.lulus.sum())}')
    print(f'AL01: {len(g1)} konfigurasi · T1 {int(g1.T1.sum())} · T3 {int(g1.T3.sum())} · '
          f'lulus semua gate {int(g1.lulus.sum())}')
    print()
    print(f'GATE (a) isyarat > kawalan p95:  AL02 {a_lulus}/{len(sig2)} = {a_kadar:.1%}  '
          f'(ambang {AMBANG_P3:.0%})   [AL01 {b1_kadar:.1%}]')
    print(f'GATE (b) had 42/63 > tiada:      AL02 {m2}/{n2} = '
          f'{(m2 / n2 if n2 else 0):.1%}  (ambang {AMBANG_HAD:.0%})   '
          f'[AL01 {(m1 / n1 if n1 else 0):.1%}]')
    kekal = a_kadar >= AMBANG_P3 and (m2 / n2 if n2 else 0) >= AMBANG_HAD
    print()
    if int(g2.T1.sum()) or int(g2.T3.sum()):
        if a_kadar >= AMBANG_P3:
            print('-> BERHENTI-MENANG: T1/T3 tercapai DAN isyarat mengalahkan kawalan.')
        else:
            print('-> SPEC §6: T1/T3 tercapai TETAPI gate (a) GAGAL. Itu BETA bukan '
                  'ISYARAT — T4 dalam samaran, BUKAN BERHENTI-MENANG.')
    print(f'-> E2 {"KEKAL (teruskan E3)" if kekal else "MATI (BERHENTI-TUTUP dipercepat)"}')

    print()
    print('Perbandingan sel sepadan (CAGR / MDD), GB02_atau3:')
    k = ['masuk', 'slot', 'keluar', 'pegang', 'urutan']
    m = sig1.merge(sig2, on=k, suffixes=('_AL01', '_AL02'))
    m['d_cagr'] = m.cagr_AL02 - m.cagr_AL01
    m['d_mdd'] = m.mdd_AL02 - m.mdd_AL01
    print(f'  median beza CAGR  AL02 - AL01 = {m.d_cagr.median():+.2f} mata')
    print(f'  median beza MDD   AL02 - AL01 = {m.d_mdd.median():+.2f} mata '
          f'(positif = lebih cetek)   sel MDD lebih cetek: '
          f'{int((m.d_mdd > 0).sum())}/{len(m)}')
    print()
    pe = KELUAR / 'alam_ekor.csv'
    if pe.exists():
        print('Diagnostik ekor setiap dagangan (GB02_atau3 x X13 x had 42):')
        print(pd.read_csv(pe).to_string(index=False, float_format=lambda v: f'{v:.2f}'))
        print()
    kol = ['alam', 'masuk', 'slot', 'keluar', 'pegang', 'urutan', 'nb', 'cagr', 'cagr_p5',
           'cagr_p95', 'mdd', 'nisbah', 'dedah', 'pul_dag', 'pegang_bar', 'pusing',
           'kos_tahun', 'buka', 'T1', 'T3', 'P3']
    print('AL02 — 15 CAGR teratas:')
    print(g2.sort_values('cagr', ascending=False).head(15)[kol].to_string(
        index=False, float_format=lambda v: f'{v:.2f}'))
    print()
    print('AL02 — MDD paling cetek:')
    print(g2.sort_values('mdd', ascending=False).head(8)[kol].to_string(
        index=False, float_format=lambda v: f'{v:.2f}'))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
