"""Carian setup — simulasi portfolio 10 slot bagi setup berprasyarat (SPEC pindaan 14 Nov 2026 (l)).

Soalan: hari isyarat berkelompok; adakah satu akaun 10 slot sempat mengambil belian itu, dan adakah kadar tangkap kekal
pada belian yang benar-benar diambil? Kawalan = jalur rawak (saham rawak hari sama x tercile ATR % sama, henti dan keluar
sama). Guna: python3 cs_portfolio6.py <kerja>   (panel_B, benih_B, lapis_B, asasL_B sudah ada; CS_PUS tidak perlu).
Keluaran: hasil/CS06/PORTFOLIO.md dan portfolio.csv. Jangan sunting keluaran secara manual."""
import os
import sys

import numpy as np
import pandas as pd

SINI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SINI)
import cs_atom as atom  # noqa: E402
import cs_cari as cari  # noqa: E402
import cs_cs05 as c5  # noqa: E402
import cs_hadapan as hadapan  # noqa: E402
import cs_lapis as lapis  # noqa: E402
import cs_lapor as lapor  # noqa: E402
import cs_lengkap as lg  # noqa: E402
import cs_teras as teras  # noqa: E402

SETUP = ['F39', 'F40', 'F58', 'F49']
GABUNGAN = {'PILIH3': ['F39', 'F40', 'F58'], 'SEMUA4': ['F39', 'F40', 'F58', 'F49']}
N_SLOT, HAD_MDD, N_ULANG = 10, 0.10, 200


def dari_takrif5(tk_):
    """'M73.2|F02+F20|H3|X09 DAN X21|QA08+QF01' -> pencetus, f1, f2, lajur, q1, q2 (tanpa ambang '@')."""
    b = tk_.split('|')
    assert '@' not in tk_, tk_
    d = hadapan.dari_takrif('|'.join(b[:4]))
    q1 = q2 = -1
    for kod in (b[4].split('+') if len(b) > 4 and b[4] else []):
        if kod in [x[:4] for x in lapis.PASARAN]:
            q1 = [x[:4] for x in lapis.PASARAN].index(kod)
        else:
            q2 = [x[:4] for x in lapis.KUMPULAN].index(kod)
    return {'pencetus': d['pencetus'], 'f1': d['fs'][0], 'f2': d['fs'][1], 'lajur': int(d['lajur']), 'q1': q1, 'q2': q2}


def hasil(pan, e, lajur):
    s, r = divmod(int(lajur), cari.NR)
    R, _, sk = teras.hasil_satu(e, pan['o'], pan['h'], pan['l'], pan['c'], pan['atr'], pan['X'], cari.JENIS, cari.PAR,
                                cari.A1, cari.A2, cari.OP, s, r)
    return R, sk


def ukur(r):
    eq = np.cumprod(1 + r)
    return float(eq[-1] ** (252 / len(r)) - 1), float((eq / np.maximum.accumulate(eq) - 1).min())


def satu(pan, X, e, R, sk, rng, topeng, tahun, bulan):
    """Satu larian portfolio 10 slot. Pulangkan dict ukuran akaun dan ukuran dagangan yang DIAMBIL."""
    hari = pan['hari']
    amb = teras.pilih_slot(e, sk, pan['tid'], hari, np.lexsort((rng.random(len(e)), hari[e + 1])), N_SLOT)
    jum, bil = teras.jumlah_harian(e[amb], R[amb], sk[amb], pan['o'], pan['c'], hari, len(pan['hari_unik']))
    pr, dedah = jum / N_SLOT, bil / N_SLOT
    c, m = ukur(pr[topeng['semua']])
    w = 1.0 if m == 0 else min(1.0, HAD_MDD / abs(m))
    c3, m3 = ukur(pr[topeng['K3']])
    th = pd.Series(pr[topeng['semua']]).groupby(tahun[topeng['semua']]).apply(lambda x: float(np.prod(1 + x) - 1))
    Ra, ea = R[amb], e[amb]
    jd = Ra >= lg.JADI
    bln = np.unique(bulan[hari[ea + 1]])
    return {'isyarat': len(e), 'diambil': int(amb.sum()), 'bulan_beli': len(bln), 'pendedahan': float(dedah[topeng['semua']].mean()),
            'cagr': c, 'mdd': m, 'cagr_had': ukur(pr[topeng['semua']] * w)[0], 'cagr_K3': c3, 'mdd_K3': m3,
            'tahun_positif': int((th > 0).sum()), 'tahun': len(th), 'tahun_terburuk': float(th.min()),
            'tp': float((jd & (X[ea, 0] > 0)).mean()), 'jadi': float(jd.mean()), 'menang': float((Ra > 0).mean()),
            'rugi8': float((Ra <= lg.RUGI).mean()), 'purata': float(Ra.mean())}


def main(kerja):
    pan, _, EV, X, L = c5._sedia(kerja, 'B')
    Lr, Tb = (L['L1'], L['L2']), lg.muat_asas(kerja, 'B')
    reg = pd.read_csv(lapor.REG_F, dtype=str).fillna('').set_index('id')
    hu = pan['hari_unik']
    tm = atom.TEMPOH['B']
    topeng = {'semua': (hu >= tm[0][1]) & (hu <= tm[-1][2]), 'K3': (hu >= tm[-1][1]) & (hu <= tm[-1][2])}
    tahun, bulan = hu // 10000, hu // 100
    n_bulan = len(np.unique(bulan[topeng['semua']]))
    n_tahun = topeng['semua'].sum() / 252
    # indeks saham rawak: bar layak tersusun ikut (hari x tercile ATR %)
    sah = np.flatnonzero(pan['sah'])
    gs = Tb['g'][sah]
    sah_urut = sah[np.argsort(gs, kind='stable')]
    n_g = np.bincount(gs, minlength=len(Tb['n']))
    mula_g = np.cumsum(n_g) - n_g
    D = {}
    for fid in SETUP:
        d = dari_takrif5(reg.takrif[fid])
        e = EV[d['pencetus']][c5.topeng(pan, Lr, EV[d['pencetus']], d['q1'], d['q2'], d['f1'], d['f2'])]
        D[fid] = (e, d['lajur'])
        cari.log(f"{fid}: {reg.takrif[fid]} -> {len(e):,} isyarat")
    senarai = {**{f: [f] for f in SETUP}, **GABUNGAN}
    baris, lajur_csv = [], []
    for nama, ahli in senarai.items():
        e = np.concatenate([D[f][0] for f in ahli])
        lj = np.concatenate([np.full(len(D[f][0]), D[f][1]) for f in ahli])
        R, sk = np.zeros(len(e)), np.zeros(len(e), np.int64)
        for c in np.unique(lj):
            R[lj == c], sk[lj == c] = hasil(pan, e[lj == c], c)
        S, W = [], []
        for i in range(N_ULANG):
            S.append(satu(pan, X, e, R, sk, np.random.default_rng([atom.BENIH, 12, i]), topeng, tahun, bulan))
            rng = np.random.default_rng([atom.BENIH, 13, i])          # jalur rawak: saham lain, hari dan tercile ATR % sama
            g = Tb['g'][e]
            er = sah_urut[mula_g[g] + (rng.random(len(e)) * n_g[g]).astype(np.int64)]
            Rr, skr = np.zeros(len(e)), np.zeros(len(e), np.int64)
            for c in np.unique(lj):
                Rr[lj == c], skr[lj == c] = hasil(pan, er[lj == c], c)
            W.append(satu(pan, X, er, Rr, skr, rng, topeng, tahun, bulan))
        S, W = pd.DataFrame(S), pd.DataFrame(W)
        b = {'setup': nama, **{k: float(S[k].median()) for k in S}}
        for k in ('cagr_had', 'cagr', 'mdd', 'tp', 'jadi', 'menang', 'rugi8', 'purata', 'cagr_K3'):
            b.update({f'rawak_{k}': float(W[k].median()), f'rawak5_{k}': float(W[k].quantile(0.05)),
                      f'rawak95_{k}': float(W[k].quantile(0.95)), f'persentil_{k}': float((W[k] < b[k]).mean())})
        b['menambah'] = bool(b['cagr_had'] > 0 and b['cagr_had'] > b['rawak95_cagr_had'])
        baris.append(b)
        cari.log(f"{nama}: diambil {b['diambil']:.0f}/{b['isyarat']:.0f}; CAGR pada MDD -10% {b['cagr_had'] * 100:+.2f} "
                 f"(rawak {b['rawak_cagr_had'] * 100:+.2f}, p95 {b['rawak95_cagr_had'] * 100:+.2f}); tp {b['tp'] * 100:.1f}")
    from AUTOTUNE.teras import data as Dt
    ix = pd.read_parquet(Dt.ambil(tag='autotune-data-a02') / 'idx.parquet')
    spy = ix[ix.ticker == 'SPY'].sort_values('date')
    sr = pd.Series(spy.close.pct_change().to_numpy(), index=(spy.date.dt.year * 10000 + spy.date.dt.month * 100
                                                              + spy.date.dt.day).to_numpy()).reindex(hu).fillna(0).to_numpy()
    cs, ms = ukur(sr[topeng['semua']])
    spy_had = ukur(sr[topeng['semua']] * min(1.0, HAD_MDD / abs(ms)))[0]
    T = pd.DataFrame(baris)
    d_ = os.path.join(SINI, 'hasil', 'CS06')
    T.to_csv(os.path.join(d_, 'portfolio.csv'), index=False, float_format='%.5f')
    try:
        sys.path.insert(0, os.path.join(lapor.BS2, 'standard'))
        import status_kad
        status = status_kad.baris()
    except Exception:
        status = '> **Status keputusan:** lihat `laporan/KAD_SKOR.md`; laporan ini BUKAN keputusan.'
    p = lambda x, k=1, t=False: f'{x * 100:+.{k}f}' if t else f'{x * 100:.{k}f}'
    A = ['# Portfolio 10 slot bagi setup berprasyarat (backtest pada saham yang tidak dilihat; BUKAN bukti)', '', status, '',
         'Dijana `kajian/carian_setup/cs_portfolio6.py`. Pradaftar: `kajian/SPEC_CARIAN_SETUP.md` pindaan 14 Nov 2026 (l), dikomit '
         'sebelum dijalankan. **Jangan sunting secara manual.**', '',
         f'Soalan: isyarat setup berprasyarat datang berkelompok. Jika akaun hanya ada **10 slot** (10 % setiap satu), berapa banyak '
         f'isyarat yang sempat diambil, dan bagaimana hasil akaun? Kumpulan B, {tm[0][1]} – {tm[-1][2]} ({n_tahun:.1f} tahun); kos '
         f'0.5 % pusingan; tunai 0 %; isyarat berlebihan dipilih rawak, diulang {N_ULANG} kali (angka = median). **Jalur rawak** = '
         'isyarat yang sama digantikan saham rawak pada hari dan tahap turun-naik yang sama, dengan henti dan keluar yang sama.', '',
         '## 1. Akaun', '',
         '| Setup | Isyarat | Diambil | Dagangan setahun | Bulan tanpa belian | Pendedahan purata % | CAGR % | MDD % | '
         '**CAGR pada MDD −10 %** | Jalur rawak: median (p5 – p95) | Kedudukan dalam jalur | Tahun positif | Tahun terburuk % | '
         'K3: CAGR % / MDD % | Menambah di peringkat akaun? |', '|---' * 15 + '|']
    for b in baris:
        A.append(f"| `{b['setup']}` | {b['isyarat']:,.0f} | {b['diambil']:,.0f} ({p(b['diambil'] / b['isyarat'], 0)} %) | "
                 f"{b['diambil'] / n_tahun:.0f} | {p(1 - b['bulan_beli'] / n_bulan, 0)} % | {p(b['pendedahan'], 0)} | "
                 f"{p(b['cagr'], 1, True)} | {p(b['mdd'], 1, True)} | **{p(b['cagr_had'], 2, True)}** | "
                 f"{p(b['rawak_cagr_had'], 2, True)} ({p(b['rawak5_cagr_had'], 2, True)} – {p(b['rawak95_cagr_had'], 2, True)}) | "
                 f"persentil ke-{b['persentil_cagr_had'] * 100:.0f} | {b['tahun_positif']:.0f} / {b['tahun']:.0f} | "
                 f"{p(b['tahun_terburuk'], 1, True)} | {p(b['cagr_K3'], 1, True)} / {p(b['mdd_K3'], 1, True)} | "
                 f"**{'YA' if b['menambah'] else 'TIDAK'}** |")
    A += ['', f'- "CAGR pada MDD −10 %" = pendedahan dikecilkan (baki tunai) sehingga kejatuhan terburuk akaun kira-kira −10 %, iaitu '
          'toleransi pengguna. **Bacaan dikunci:** "menambah" hanya jika angka itu positif DAN melebihi persentil ke-95 jalur rawak.',
          f'- Maklumat sahaja (bukan kayu ukur): SPY beli-dan-pegang pada MDD −10 % = {p(spy_had, 2, True)} % setahun '
          f'(CAGR {p(cs, 1, True)} %, MDD {p(ms, 1, True)} %).', '',
          '## 2. Dagangan yang benar-benar diambil akaun', '',
          'Setiap sel: setup (jalur rawak, median). Tangkap penuh = naik ≥ 5 % minggu pertama DAN dijual dengan untung ≥ 10 %.', '',
          '| Setup | Tangkap penuh % | Jadi (dijual ≥ +10 %) % | Menang % | Rugi ≥ 8 % % | Purata setiap dagangan % |', '|---' * 6 + '|']
    for b in baris:
        A.append(f"| `{b['setup']}` | **{p(b['tp'])}** ({p(b['rawak_tp'])}) | {p(b['jadi'])} ({p(b['rawak_jadi'])}) | "
                 f"{p(b['menang'], 0)} ({p(b['rawak_menang'], 0)}) | {p(b['rugi8'])} ({p(b['rawak_rugi8'])}) | "
                 f"{p(b['purata'], 2, True)} ({p(b['rawak_purata'], 2, True)}) |")
    ya = [b['setup'] for b in baris if b['menambah']]
    A += ['', '## 3. Bacaan', '',
          f"- Menambah di peringkat akaun (bacaan dikunci): {', '.join(f'`{x}`' for x in ya) if ya else '**tiada**'}.",
          '- Kadar tangkap pada belian yang diambil lawan jalur rawak menunjukkan sama ada kelebihan memilih saham kekal selepas '
          'had slot; lajur akaun menunjukkan sama ada kelebihan itu cukup besar untuk kelihatan pada wang.', '',
          '## 4. Kaveat', '',
          '- Tiada saham delist (condong ke atas); set 2000 bukan tapisan Shariah; prasyarat earnings memakai tarikh sebenar.',
          '- Kumpulan B sudah dilihat dalam CS05 dan CS06; setup ini dipilih kerana kedudukannya di papan, jadi angka ini bukan '
          'ujian bebas. Satu akaun 10 slot ialah satu cara membina portfolio, bukan satu-satunya.',
          '- Backtest sahaja. Tiada jejak hadapan, tiada order; kad skor kekal satu-satunya keputusan wang sebenar.', '']
    open(os.path.join(d_, 'PORTFOLIO.md'), 'w', encoding='utf-8').write('\n'.join(A))
    cari.log('portfolio siap: menambah = ' + (', '.join(ya) or 'tiada'))


if __name__ == '__main__':
    main(sys.argv[1])
