"""Carian setup CS03 — pangkat ikut KADAR TANGKAP (SPEC pindaan 13 Nov 2026 (d)).
Guna: python3 cs_tangkap.py <kerja>   (folder kerja CS02: panel_A/B dan benih_A/B sudah ada).
Keluaran: hasil/CS03/LAPORAN.md, papan.csv, senarai_kunci.csv, meta.json; kajian/CARIAN_SETUP.md; registry F."""
import json
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
import cs_lapor as lapor  # noqa: E402
import cs_teras as teras  # noqa: E402

PUS = 'CS03'
LABEL = ['m5', 't10', 't20', 'gagal', 'lari']
NL = len(LABEL)
TMAX = teras.TMAX


@njit(parallel=True, cache=True)
def label(ev, o, l, c):
    """Label setiap isyarat bar ev (beli buka bar ev + 1). Lajur: m5, t10, t20, gagal, lari."""
    out = np.zeros((ev.shape[0], 5), np.float32)
    for k in prange(ev.shape[0]):
        e = ev[k] + 1
        P = o[e]
        L = P * 0.92
        henti = 99                       # sesi pertama yang tutupnya TIDAK lagi dipegang
        if c[e] <= L:
            henti = 1
        else:
            for d in range(1, TMAX):
                if o[e + d] <= L or l[e + d] <= L:
                    henti = d
                    break
        t10 = False
        t20 = False
        for d in range(TMAX):
            if d >= henti:
                break
            if c[e + d] >= P * 1.10:
                t10 = True
            if c[e + d] >= P * 1.20:
                t20 = True
                break
        m5 = c[e + 4] >= P * 1.05
        out[k, 0] = m5
        out[k, 1] = t10
        out[k, 2] = t20
        out[k, 3] = (henti < 99) and (not t10)
        out[k, 4] = m5 and t10 and (c[e + TMAX - 1] >= P * 1.10)
    return out


def label_asas(pan):
    """X[bar, 0:5] = label; X[bar, 5:10] = asas (kadar label antara bar layak hari sama x tercile ATR % sama)."""
    ev = np.flatnonzero(pan['sah'])
    Lb = label(ev, pan['o'], pan['l'], pan['c'])
    hari = pan['hari'][ev]
    pct = pd.Series(pan['atr'][ev] / pan['c'][ev]).groupby(hari).rank(pct=True).to_numpy()
    g = hari * 3 + np.minimum((pct * 3).astype(np.int64), 2)
    bil = np.maximum(np.bincount(g), 1)
    asas = np.stack([np.bincount(g, Lb[:, j]) / bil for j in range(NL)], 1)[g]
    X = np.zeros((len(pan['c']), 2 * NL), np.float32)
    X[ev, :NL] = Lb
    X[ev, NL:] = asas
    return X


def lb_lari(n, p, p0):
    return (p - p0) - 2 * np.sqrt(np.maximum(p * (1 - p), 0) / np.maximum(n, 1))


def kadar(pan, X, ev, f1, f2):
    """Kadar label dan asas setiap tempoh, satu posisi setiap saham (pegang 20 sesi)."""
    m = np.ones(len(ev), bool)
    for f in (f1, f2):
        if f >= 0:
            m &= pan['F'][f, ev] > 0
    e = ev[m]
    e = e[teras.satu_posisi(e, np.full(len(e), TMAX - 1), pan['tid'])]
    tp = pan['tempoh'][e]
    out = {}
    for p in range(int(pan['tempoh'].max()) + 1):
        x = X[e[tp == p]]
        d = {'n': len(x)}
        for j, nama in enumerate(LABEL):
            d[nama] = float(x[:, j].mean()) if len(x) else np.nan
            d['a_' + nama] = float(x[:, NL + j].mean()) if len(x) else np.nan
        out[p] = d
    return out


def skor_tepat(v):
    if v[0]['n'] < cari.N_MIN or v[1]['n'] < cari.N_MIN:
        return np.nan
    return float(min(lb_lari(v[p]['n'], v[p]['lari'], v[p]['a_lari']) for p in (0, 1)))


def keluar_terbaik(pan, ev, f1, f2):
    """(henti x keluar) dengan min(LB E1, LB E2) purata R tertinggi bagi satu peraturan masuk (SPEC §6.1)."""
    m = np.ones(len(ev), bool)
    for f in (f1, f2):
        if f >= 0:
            m &= pan['F'][f, ev] > 0
    e = ev[m]
    tp = pan['tempoh'][e].astype(np.int64)
    S = np.zeros((1, 2, cari.K))
    Q = np.zeros((1, 2, cari.K))
    N2 = np.zeros((1, 2), np.int64)
    kos = np.zeros((len(e), 1), np.uint8)
    satu = np.array([-1], np.int64)
    for a in range(0, len(e), 40000):
        Rm = teras.hasil_semua(e[a:a + 40000], pan['o'], pan['h'], pan['l'], pan['c'], pan['atr'], pan['X'],
                               cari.JENIS, cari.PAR, cari.A1, cari.A2, cari.OP)
        teras.kumpul_tambah(Rm, tp[a:a + 40000], kos[a:a + 40000], satu, satu, S, Q, N2)
    idx, _, _, _ = teras.kumpul_skor(S, Q, N2, np.zeros(1, np.int64), 1, 1, cari.TEPI)
    return int(idx[0, 0])


def main(kerja):
    cari_set, kunci_set = cari.PUSINGAN[PUS]
    T_cari, T_kunci = lapor.tempoh(PUS)
    pan = cari.panel(kerja, cari_set)
    bn = pickle.load(open(os.path.join(kerja, f'benih_{cari_set}.pkl'), 'rb'))
    ev_semua = cari.pencetus(pan, bn)
    X = label_asas(pan)
    cari.log('label kumpulan cari siap; asas keseluruhan: '
             + ' · '.join(f'{n} {X[pan["sah"], j].mean() * 100:.1f}%' for j, n in enumerate(LABEL)))
    baris, meta = [], {'pencetus': len(ev_semua), 'masuk_dicuba': 0, 'masuk_diskor': 0}
    for nama, ev in ev_semua.items():
        tp = pan['tempoh'][ev].astype(np.int64)
        meta['masuk_dicuba'] += len(cari.F1)
        if (tp == 0).sum() < cari.N_MIN or (tp == 1).sum() < cari.N_MIN:
            continue
        S = np.zeros((len(cari.F1), 2, 2 * NL))
        N2 = np.zeros((len(cari.F1), 2), np.int64)
        teras.kumpul_tambah(np.ascontiguousarray(X[ev]), tp, np.ascontiguousarray(pan['F'][:, ev].T), cari.F1,
                            cari.F2, S, np.zeros_like(S), N2)
        ok = np.flatnonzero((N2[:, 0] >= cari.N_MIN) & (N2[:, 1] >= cari.N_MIN))
        n = N2[ok].astype(float)
        sk = np.minimum(*[lb_lari(n[:, p], S[ok, p, 4] / n[:, p], S[ok, p, NL + 4] / n[:, p]) for p in (0, 1)])
        meta['masuk_diskor'] += len(ok)
        baris += [(nama, cari.F1[c], cari.F2[c], s) for c, s in zip(ok, sk)]
    B = pd.DataFrame(baris, columns=['pencetus', 'f1', 'f2', 'skor'])
    meta['bahagian_skor_positif'] = float((B.skor > 0).mean())
    cari.log(f"besar: {meta['masuk_diskor']:,} peraturan masuk diskor; {meta['bahagian_skor_positif'] * 100:.1f}% skor > 0")

    def tepat(D):
        v = [kadar(pan, X, ev_semua[r.pencetus], r.f1, r.f2) for r in D.itertuples()]
        D = D.assign(skor_tepat=[skor_tepat(x) for x in v], _v=v)
        return D.dropna(subset=['skor_tepat'])

    A = tepat(B.sort_values('skor', ascending=False).head(cari.N_TEPAT)).sort_values('skor_tepat', ascending=False)
    A = A.reset_index(drop=True)
    A['keluarga'] = A.pencetus.map(cari.keluarga)
    A['peranan'] = np.where(A.index < cari.N_SENARAI, 'atas200', '')
    A.loc[A.drop_duplicates('keluarga').head(10).index, 'peranan'] = 'papan'
    W = tepat(B.sample(cari.N_SENARAI, random_state=atom.BENIH)).assign(peranan='rawak')
    P = pd.concat([A[A.peranan != ''], W], ignore_index=True)
    P['lajur'] = -1
    for k in P.index[P.peranan == 'papan']:
        P.loc[k, 'lajur'] = keluar_terbaik(pan, ev_semua[P.pencetus[k]], P.f1[k], P.f2[k])
    V = {k: dict(zip(T_cari, P._v[k].values())) for k in P.index}
    R = {}
    for k in P.index[P.peranan == 'papan']:
        r = P.loc[k]
        x = cari.nilai(pan, ev_semua[r.pencetus], r.f1, r.f2, r.lajur, penuh=True, asas=cari.asas_rawak(pan, r.lajur))
        R[k] = dict(zip(T_cari, x.values()))
    del pan, X
    pan = cari.panel(kerja, kunci_set)
    bn2 = pickle.load(open(os.path.join(kerja, f'benih_{kunci_set}.pkl'), 'rb'))
    perlu = {n for n in P.pencetus.unique() if not n.startswith('P')} - set(bn2['sig'])
    if perlu:
        bn2 = cari.benih(kerja, kunci_set, hanya=perlu | set(bn2['sig']))
    ev2 = cari.pencetus(pan, bn2)
    X = label_asas(pan)
    for k in P.index:
        r = P.loc[k]
        if r.pencetus not in ev2:
            continue
        V[k].update(zip(T_kunci, kadar(pan, X, ev2[r.pencetus], r.f1, r.f2).values()))
        if r.peranan == 'papan':
            x = cari.nilai(pan, ev2[r.pencetus], r.f1, r.f2, r.lajur, penuh=True, asas=cari.asas_rawak(pan, r.lajur))
            R[k].update(zip(T_kunci, x.values()))

    def gab(k, nama):                       # kadar gabungan semua tempoh Kunci
        n = sum(V[k].get(t, {}).get('n', 0) for t in T_kunci)
        return n, (sum(V[k][t]['n'] * V[k][t][nama] for t in T_kunci if V[k].get(t, {}).get('n')) / n if n else np.nan)

    for nama in LABEL:
        P['k_' + nama] = [gab(k, nama)[1] - gab(k, 'a_' + nama)[1] for k in P.index]     # kelebihan Kunci
    P['n_kunci'] = [gab(k, 'lari')[0] for k in P.index]
    for t in T_kunci:
        P[f'n_{t}'] = [V[k].get(t, {}).get('n', 0) for k in P.index]
        P[f'kl_{t}'] = [V[k][t]['lari'] - V[k][t]['a_lari'] if V[k].get(t, {}).get('n') else np.nan for k in P.index]
    rawak, atas = P[(P.peranan == 'rawak') & (P.n_kunci >= 100)], P[(P.peranan != 'rawak') & (P.n_kunci >= 100)]
    p95 = float(rawak.k_lari.quantile(0.95))
    param = bn['param']
    ringkas = []
    for kd, k in enumerate(P.index[P.peranan == 'papan'], 1):
        r = P.loc[k]
        v = {t: {**{'n': 0, 'purata': np.nan}, **R[k].get(t, {})} for t in T_cari + T_kunci}
        T1 = all(V[k].get(t, {}).get('n') and V[k][t]['t10'] > V[k][t]['a_t10'] for t in T_kunci)
        T2 = all(V[k].get(t, {}).get('n') and V[k][t]['lari'] > V[k][t]['a_lari'] for t in T_kunci)
        T3 = bool(r.n_kunci >= 100 and r.k_lari > p95)
        ringkas.append((kd, lapor.terang(r, param), r, v, T1, T2, T3, float((rawak.k_lari < r.k_lari).mean()), []))
    idf = lapor.daftar_f(ringkas, param, PUS, T_cari, T_kunci)

    d = os.path.join(SINI, 'hasil', PUS)
    os.makedirs(d, exist_ok=True)
    S = P.drop(columns=['_v']).copy()
    S['masuk'] = [lapor.nama_pencetus(n, param) for n in S.pencetus]
    S['penapis'] = [' DAN '.join(atom.PENAPIS[f] for f in (a, b) if f >= 0) or 'tiada' for a, b in zip(S.f1, S.f2)]
    S.drop(columns=['pencetus', 'f1', 'f2', 'keluarga']).to_csv(os.path.join(d, 'senarai_kunci.csv'), index=False,
                                                              float_format='%.5f')
    p = lambda x, k=1, t=False: '–' if x != x else (f'{x * 100:+.{k}f}' if t else f'{x * 100:.{k}f}')
    ya = lambda b: '✓' if b else '✗'
    era = {t: (atas[atas[f'n_{t}'] >= 50][f'kl_{t}'], rawak[rawak[f'n_{t}'] >= 50][f'kl_{t}']) for t in T_kunci}
    rho = {t: float(atas[atas[f'n_{t}'] >= 50][['skor_tepat', f'kl_{t}']].corr(method='spearman').iloc[0, 1])
           for t in T_kunci}
    try:
        sys.path.insert(0, os.path.join(lapor.BS2, 'standard'))
        import status_kad
        status = status_kad.baris()
    except Exception:
        status = '> **Status keputusan:** lihat `laporan/KAD_SKOR.md`; laporan ini BUKAN keputusan.'
    TK = lapor.KONFIG['CS02']['terang']
    A_ = [f'# Carian Setup {PUS} — papan 10 teratas ikut KADAR TANGKAP (backtest, BUKAN bukti)', '', status, '',
          'Dijana `kajian/carian_setup/cs_tangkap.py`. Pradaftar: `kajian/SPEC_CARIAN_SETUP.md` pindaan 13 Nov 2026 (d). '
          '**Jangan sunting secara manual.** Pusingan lama: `carian_setup/hasil/CS01|CS02/LAPORAN.md`.', '',
          '## 1. Apa yang dipangkatkan', '',
          'Setup yang **paling kerap menangkap saham yang mula naik kuat**. Saham "lari" = naik ≥ 5 % pada minggu '
          'pertama, mencapai ≥ 10 % sebelum henti −8 %, dan masih ≥ 10 % di atas harga beli pada minggu ke-4. '
          '"Rawak" = saham lain yang layak pada **hari yang sama dan tahap turun-naik yang sama**; kelebihan = kadar '
          'setup − rawak.', '',
          f"Carian: kumpulan A set 2000, {meta['masuk_dicuba']:,} peraturan masuk dicuba, {meta['masuk_diskor']:,} cukup "
          f"isyarat; {meta['bahagian_skor_positif'] * 100:.1f} % mempunyai had bawah kelebihan positif dalam kedua-dua era. "
          'Angka di bawah daripada **kumpulan B** (saham yang carian tidak lihat), 2010 – Ogo 2026.', '',
          '## 2. Papan 10 teratas', '',
          '| # | ID | Masuk | Penapis | Belian | **Lari %** (rawak) | Capai +10 % dahulu % (rawak) | Capai +20 % % (rawak) | '
          'Naik 5 % minggu 1 % (rawak) | Kena henti −8 % dahulu % (rawak) | T1 | T2 | T3 |',
          '|---' * 13 + '|']
    csvb = []
    for kd, dd, r, v, T1, T2, T3, pct, _ in ringkas:
        k = r.name
        g = {n: (gab(k, n)[1], gab(k, 'a_' + n)[1]) for n in LABEL}
        sel = lambda n: f'{p(g[n][0])} ({p(g[n][1])})'
        A_.append(f"| {kd} | `{idf[kd]}` | {dd['masuk']} | {dd['penapis']} | {int(r.n_kunci):,} | **{sel('lari')}** | "
                  f"{sel('t10')} | {sel('t20')} | {sel('m5')} | {sel('gagal')} | {ya(T1)} | {ya(T2)} | {ya(T3)} |")
        for t in T_cari + T_kunci:
            csvb.append({'kedudukan': kd, 'id': idf[kd], **dd, 'skor_tepat': r.skor_tepat, 'tempoh': t,
                         **V[k].get(t, {}), **{'R_' + a: b for a, b in v[t].items()}, 'T1': T1, 'T2': T2, 'T3': T3})
    pd.DataFrame(csvb).to_csv(os.path.join(d, 'papan.csv'), index=False, float_format='%.5f')
    A_ += ['', '- **T1:** kelebihan "capai +10 % dahulu" positif dalam K1, K2 dan K3. **T2:** kelebihan "lari" positif dalam '
           f'ketiga-tiganya. **T3:** kelebihan "lari" melebihi persentil ke-95 peraturan rawak ({p(p95, 2, True)} mata).', '',
           '### Cara pegang dan keluar terbaik bagi setiap masuk (dipilih pada kumpulan A; angka kumpulan B)', '',
           '| ID | Henti | Keluar | ' + ' | '.join(f'{t}: purata % / menang % / pegang' for t in T_kunci) + ' |',
           '|---' * (3 + len(T_kunci)) + '|']
    for kd, dd, r, v, *_ in ringkas:
        A_.append(f"| `{idf[kd]}` | {dd['henti']} | {dd['keluar']} | " + ' | '.join(
            f"{p(v[t]['purata'], 2, True)} / {p(v[t].get('menang', np.nan))} / {v[t].get('pegang', np.nan):.1f}"
            if v[t]['n'] else '–' for t in T_kunci) + ' |')
    baris_e = lambda tajuk, f: f'| {tajuk} | ' + ' | '.join(f(t) for t in T_kunci) + ' |'
    A_ += ['', '## 3. Semakan kejujuran', '',
           '**K3 ialah ujian sebenar** (saham lain DAN tahun yang tidak dipakai carian). Unit: mata peratus kelebihan '
           '"lari" atas rawak.', '',
           '| Ukuran | ' + ' | '.join(TK[t] for t in T_kunci) + ' |', '|---' * (1 + len(T_kunci)) + '|',
           baris_e(f'Median kelebihan, {len(atas)} peraturan teratas', lambda t: p(era[t][0].median(), 2, True)),
           baris_e(f'Median kelebihan, {len(rawak)} peraturan rawak', lambda t: p(era[t][1].median(), 2, True)),
           baris_e('Teratas dengan kelebihan positif', lambda t: f'{int((era[t][0] > 0).sum())} daripada {len(era[t][0])}'),
           baris_e('Rawak dengan kelebihan positif', lambda t: f'{int((era[t][1] > 0).sum())} daripada {len(era[t][1])}'),
           baris_e('Spearman skor lawan kelebihan', lambda t: f'{rho[t]:+.2f}'), '',
           '## 4. Kaveat', '',
           '- Backtest sahaja; tiada setup masuk papertrade tanpa keputusan pengguna. Kad skor kekal satu-satunya keputusan '
           'wang sebenar.',
           '- Tiada saham delist (condong ke atas); set 2000 bukan tapisan Shariah; data bermula 2010.',
           '- "Lari" ialah label harga, bukan untung dagangan: untung sebenar bergantung pada cara pegang dan keluar '
           '(jadual kedua) dan pada berapa isyarat yang sempat diambil portfolio.', '']
    teks = '\n'.join(A_)
    open(os.path.join(d, 'LAPORAN.md'), 'w', encoding='utf-8').write(teks)
    open(os.path.join(lapor.BS2, 'kajian', 'CARIAN_SETUP.md'), 'w', encoding='utf-8').write(teks)
    meta.update(pusingan=PUS, p95_rawak=p95, **{f'median_atas_{t}': float(era[t][0].median()) for t in T_kunci},
                **{f'median_rawak_{t}': float(era[t][1].median()) for t in T_kunci},
                **{f'spearman_{t}': rho[t] for t in T_kunci})
    json.dump(meta, open(os.path.join(d, 'meta.json'), 'w'), indent=1)
    cari.log('CS03 siap: ' + json.dumps({k: (round(v, 4) if isinstance(v, float) else v) for k, v in meta.items()}))


if __name__ == '__main__':
    main(sys.argv[1])
