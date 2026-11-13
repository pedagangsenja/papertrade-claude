"""Carian setup — semakan portfolio pada had MDD -10 % (SPEC pindaan 13 Nov 2026 (c)).
Guna: python3 cs_portfolio.py <kerja> <pusingan>. Keluaran: hasil/<pusingan>/PORTFOLIO.md dan portfolio.csv."""
import os
import pickle
import sys

import numpy as np
import pandas as pd

SINI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SINI)
import cs_atom as atom  # noqa: E402
import cs_cari as cari  # noqa: E402
import cs_lapor as lapor  # noqa: E402
import cs_teras as teras  # noqa: E402

N_SLOT, HAD_MDD = 10, 0.10


def ukur(r):
    eq = np.cumprod(1 + r)
    mdd = float((eq / np.maximum.accumulate(eq) - 1).min())
    return float(eq[-1] ** (252 / len(r)) - 1), mdd


def pada_had(r):
    """CAGR selepas pendedahan didarab w = min(1, had / |MDD|)."""
    _, mdd = ukur(r)
    w = 1.0 if mdd == 0 else min(1.0, HAD_MDD / abs(mdd))
    c, m = ukur(r * w)
    return w, c, m


def dagangan(pan, ev, f1, f2, lajur):
    m = np.ones(len(ev), bool)
    for f in (f1, f2):
        if f >= 0:
            m &= pan['F'][f, ev] > 0
    e = ev[m]
    s, r = divmod(int(lajur), cari.NR)
    R, hp, sk = teras.hasil_satu(e, pan['o'], pan['h'], pan['l'], pan['c'], pan['atr'], pan['X'], cari.JENIS,
                                 cari.PAR, cari.A1, cari.A2, cari.OP, s, r)
    return e, R, sk


def portfolio(pan, e, R, sk, rng):
    hari = pan['hari']
    susun = np.lexsort((rng.random(len(e)), hari[e + 1]))
    amb = teras.pilih_slot(e, sk, pan['tid'], hari, susun, N_SLOT)
    jum, bil = teras.jumlah_harian(e[amb], R[amb], sk[amb], pan['o'], pan['c'], hari, len(pan['hari_unik']))
    return jum / N_SLOT, bil / N_SLOT, int(amb.sum()), len(e)


def main(kerja, pus):
    kunci_set = cari.PUSINGAN[pus][1]
    pan = cari.panel(kerja, kunci_set)
    bn = pickle.load(open(os.path.join(kerja, f'benih_{kunci_set}.pkl'), 'rb'))
    ev_semua = cari.pencetus(pan, bn)
    P = pd.read_pickle(os.path.join(kerja, 'pilihan.pkl'))
    papan = P[P.peranan == 'papan']
    reg = pd.read_csv(lapor.REG_F, dtype=str).set_index('takrif')
    hu = pan['hari_unik']
    tm = atom.TEMPOH[kunci_set]
    semua = (hu >= tm[0][1]) & (hu <= 20261231)
    akhir = (hu >= tm[-1][1]) & (hu <= 20261231)
    from AUTOTUNE.teras import data as D
    ix = pd.read_parquet(D.ambil(tag='autotune-data-a02') / 'idx.parquet')
    spy = ix[ix.ticker == 'SPY'].sort_values('date')
    spy_r = pd.Series(spy.close.pct_change().to_numpy(),
                      index=(spy.date.dt.year * 10000 + spy.date.dt.month * 100 + spy.date.dt.day).to_numpy())
    spy_r = spy_r.reindex(hu).fillna(0).to_numpy()
    baris, gab = [], []
    for r in papan.itertuples():
        tk = lapor.takrif(r)
        e, R, sk = dagangan(pan, ev_semua[r.pencetus], r.f1, r.f2, r.lajur)
        lulus3 = all(reg.loc[tk, x] == 'True' for x in ('T1', 'T2', 'T3'))
        if lulus3:
            gab.append((e, R, sk))
        baris.append((reg.loc[tk, 'id'], lulus3, e, R, sk))
    if gab:
        e, R, sk = (np.concatenate([g[i] for g in gab]) for i in range(3))
        baris.append((f'Gabungan {len(gab)} lulus', True, e, R, sk))
    out = []
    for nama, lulus3, e, R, sk in baris:
        pr, dedah, n_ambil, n_isyarat = portfolio(pan, e, R, sk, np.random.default_rng(atom.BENIH))
        c, m = ukur(pr[semua])
        w, cw, mw = pada_had(pr[semua])
        c3, m3 = ukur(pr[akhir])
        out.append({'setup': nama, 'lulus_3_tapis': lulus3, 'isyarat': n_isyarat, 'dagangan': n_ambil,
                    'pendedahan': float(dedah[semua].mean()), 'cagr': c, 'mdd': m, 'w': w, 'cagr_had': cw,
                    'mdd_had': mw, 'cagr_K3': c3, 'mdd_K3': m3})
    c, m = ukur(spy_r[semua])
    w, cw, mw = pada_had(spy_r[semua])
    c3, m3 = ukur(spy_r[akhir])
    out.append({'setup': 'SPY beli-dan-pegang', 'lulus_3_tapis': '', 'isyarat': '', 'dagangan': '', 'pendedahan': 1.0,
                'cagr': c, 'mdd': m, 'w': w, 'cagr_had': cw, 'mdd_had': mw, 'cagr_K3': c3, 'mdd_K3': m3})
    T = pd.DataFrame(out)
    d = os.path.join(SINI, 'hasil', pus)
    T.to_csv(os.path.join(d, 'portfolio.csv'), index=False, float_format='%.5f')
    p = lambda x, k=1: f'{x * 100:+.{k}f}'
    spy_had = cw
    A = [f'# Carian Setup {pus} — portfolio 10 slot pada had MDD −10 % (backtest, BUKAN bukti)', '',
         'Dijana `kajian/carian_setup/cs_portfolio.py` (SPEC pindaan 13 Nov 2026 (c)). **Jangan sunting secara manual.**',
         '', f'Kumpulan {kunci_set} (saham yang carian tidak lihat), {tm[0][1]} – {tm[-1][2]}; 10 slot × 10 %; kos 0.5 % '
         'pusingan; tunai 0 %. "Pada MDD −10 %" = pendedahan dikecilkan (baki tunai) sehingga kejatuhan terburuk '
         'kira-kira −10 %.', '',
         '| Setup | Lulus 3 tapis | Dagangan | Pendedahan purata % | CAGR % | MDD % | **CAGR pada MDD −10 %** | '
         'K3 sahaja: CAGR % / MDD % |', '|---|---|---|---|---|---|---|---|']
    for x in out:
        A.append(f"| `{x['setup']}` | {'ya' if x['lulus_3_tapis'] is True else ('' if x['lulus_3_tapis'] == '' else 'tidak')} "
                 f"| {x['dagangan'] if x['dagangan'] == '' else format(x['dagangan'], ',')} | "
                 f"{x['pendedahan'] * 100:.0f} | {p(x['cagr'])} | {p(x['mdd'])} | "
                 f"**{p(x['cagr_had'], 2)}** | {p(x['cagr_K3'])} / {p(x['mdd_K3'])} |")
    atas = [x for x in out[:-1] if x['cagr_had'] > spy_had]
    A += ['', f"Kayu ukur: SPY pada MDD −10 % = {p(spy_had, 2)} % setahun. Setup yang melebihinya: "
          + (', '.join(x['setup'] for x in atas) if atas else '**tiada**') + '.', '',
          'Kaveat: tiada saham delist (condong ke atas, terutama bagi setup yang membeli saham jatuh); bukan tapisan '
          'Shariah; isyarat berlebihan dipilih rawak dengan satu benih; tiada pasaran menurun panjang sejak 2010.', '']
    open(os.path.join(d, 'PORTFOLIO.md'), 'w', encoding='utf-8').write('\n'.join(A))
    print(T.assign(**{k: (T[k] * 100).round(2) for k in ('pendedahan', 'cagr', 'mdd', 'cagr_had', 'mdd_had', 'cagr_K3',
                                                         'mdd_K3')}).drop(columns=['w', 'isyarat']).to_string(index=False))


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
