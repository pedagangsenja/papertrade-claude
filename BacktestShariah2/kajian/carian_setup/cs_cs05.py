"""Carian setup CS05 — PRASYARAT + SYARAT bagi SEMUA kaedah (SPEC pindaan 14 Nov 2026 (i)).

Peraturan masuk = [0-1 prasyarat pasaran] DAN [0-1 prasyarat kumpulan/syarikat] DAN pencetus DAN [0-2 penapis saham].
Dua skor kadar tangkap: `pilih` (lawan rawak hari sama x tercile ATR %) dan `jumlah` (lawan rawak era sama x tercile).
Guna (folder kerja: panel_A/B, benih_A/B (SEMUA modul), lapis_A/B sudah ada):
  python3 cs_cs05.py besar   <kerja>    semua peraturan masuk kumpulan A, prasyarat sebenar
  python3 cs_cs05.py plasebo <kerja>    sama, prasyarat dianjak masa (plasebo)
  python3 cs_cs05.py tepat   <kerja>    peringkat tepat, papan, pilihan setiap pencetus (kumpulan A)
  python3 cs_cs05.py kunci   <kerja>    nilai semuanya pada kumpulan B + padanan kelas x prasyarat
  python3 cs_cs05.py lapor   <kerja>    hasil/CS05/, kajian/CARIAN_SETUP.md, data/registry_F.csv
Jangan sunting keluaran secara manual."""
import json
import multiprocessing as mp
import os
import pickle
import re
import sys
import time

import numpy as np
import pandas as pd
from numba import njit

SINI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SINI)
import cs_atom as atom  # noqa: E402
import cs_cari as cari  # noqa: E402
import cs_lapis as lapis  # noqa: E402
import cs_lapor as lapor  # noqa: E402
import cs_tangkap as tk  # noqa: E402
import cs_teras as teras  # noqa: E402

PUS = 'CS05'
N_MIN = cari.N_MIN
TMAX = teras.TMAX
LABEL, NL = tk.LABEL, tk.NL                                   # m5, t10, t20, gagal, lari
SAHAM = np.asarray([i for i in range(len(atom.PENAPIS)) if i not in (25, 26, 27)], np.int64)   # 27 penapis saham
NS = len(SAHAM)
C1 = np.asarray([-1] + list(range(NS)) + [a for a in range(NS) for b in range(a + 1, NS)], np.int64)
C2 = np.asarray([-1] + [-1] * NS + [b for a in range(NS) for b in range(a + 1, NS)], np.int64)
NC = len(C1)                                                  # 379 gabungan 0-2 penapis saham
PASANG = np.zeros((NS, NS), np.int64)
for _ci in range(1 + NS, NC):
    PASANG[C1[_ci], C2[_ci]] = _ci
NQ1, NQ2 = lapis.N1 + 1, lapis.N2 + 1                         # 34 x 16; indeks 0 = tiada prasyarat
NQ = NQ1 * NQ2
N_ATAS, N_KELAS, N_KOLAM, N_SENARAI = 2000, 5, 300, 200
N_KOLAM_PRA = 20                                              # calon papan setiap pasangan prasyarat (pindaan (i) tambahan)
SKOR = ('pilih', 'jumlah')
ASAS = {'pilih': 'a_', 'jumlah': 'e_'}                        # awalan lajur asas: hari sama / era sama
MAKS_PRA, MAKS_TANPA = 3, 3                                   # had kepelbagaian papan
KELUAR_UJI = os.environ.get('CS05_KELUAR')                    # uji kering: tulis semua keluaran di sini, bukan dalam repo
_G = {}


# ---------- label dan asas ----------
def label_asas2(pan):
    """X[bar, 0:5] label; X[bar, 5:10] asas hari sama x tercile ATR %; X[bar, 10:15] asas era sama x tercile ATR %."""
    ev = np.flatnonzero(pan['sah'])
    Lb = tk.label(ev, pan['o'], pan['l'], pan['c'])
    hari = pan['hari'][ev]
    pct = pd.Series(pan['atr'][ev] / pan['c'][ev]).groupby(hari).rank(pct=True).to_numpy()
    terc = np.minimum((pct * 3).astype(np.int64), 2)
    X = np.zeros((len(pan['c']), 3 * NL), np.float32)
    X[ev, :NL] = Lb
    for a, g in ((NL, hari * 3 + terc), (2 * NL, pan['tempoh'][ev].astype(np.int64) * 3 + terc)):
        bil = np.maximum(np.bincount(g), 1)
        X[ev, a:a + NL] = np.stack([np.bincount(g, Lb[:, j]) / bil for j in range(NL)], 1)[g]
    return X


# ---------- peringkat besar ----------
@njit(cache=True)
def kumpul5(tp, V, Fm, L1, L2, pasang, Acc):
    """Acc[q, ci, era] += (1, lari, asas hari, asas era) bagi setiap isyarat dan setiap gabungan yang benar baginya.
    q = i1 * (n2 + 1) + i2 (0 = tiada prasyarat lapisan itu); ci = gabungan penapis saham (0 = tiada)."""
    nS, n1, n2 = Fm.shape[1], L1.shape[1], L2.shape[1]
    fb = np.empty(nS, np.int64)
    cb = np.empty(1 + nS + nS * (nS - 1) // 2, np.int64)
    a1 = np.empty(n1 + 1, np.int64)
    a2 = np.empty(n2 + 1, np.int64)
    for k in range(tp.shape[0]):
        p = tp[k]
        nf = 0
        for a in range(nS):
            if Fm[k, a] != 0:
                fb[nf] = a
                nf += 1
        cb[0] = 0
        nc = 1
        for i in range(nf):
            cb[nc] = 1 + fb[i]
            nc += 1
        for i in range(nf):
            for j in range(i + 1, nf):
                cb[nc] = pasang[fb[i], fb[j]]
                nc += 1
        a1[0] = 0
        m1 = 1
        for a in range(n1):
            if L1[k, a] != 0:
                a1[m1] = a + 1
                m1 += 1
        a2[0] = 0
        m2 = 1
        for a in range(n2):
            if L2[k, a] != 0:
                a2[m2] = a + 1
                m2 += 1
        v0, v1, v2 = V[k, 0], V[k, 1], V[k, 2]
        for i in range(m1):
            for j in range(m2):
                q = a1[i] * (n2 + 1) + a2[j]
                for c in range(nc):
                    ci = cb[c]
                    Acc[q, ci, p, 0] += 1.0
                    Acc[q, ci, p, 1] += v0
                    Acc[q, ci, p, 2] += v1
                    Acc[q, ci, p, 3] += v2


def skor_acc(Acc, n_min=N_MIN):
    """(cukup, skor_pilih, skor_jumlah) setiap [q, ci]: min dua era bagi (kelebihan lari - 2 ralat piawai)."""
    n = Acc[..., 0]
    ok = (n[..., 0] >= n_min) & (n[..., 1] >= n_min)
    with np.errstate(divide='ignore', invalid='ignore'):
        p = Acc[..., 1] / n
        se2 = 2 * np.sqrt(np.maximum(p * (1 - p), 0) / n)
        sp = np.min(p - Acc[..., 2] / n - se2, axis=-1)
        sj = np.min(p - Acc[..., 3] / n - se2, axis=-1)
    sp[~ok] = np.nan
    sj[~ok] = np.nan
    return ok, sp, sj


def nyah(flat):
    """Indeks rata (q * NC + ci) -> (q1, q2, f1, f2); -1 = tiada; f = indeks PENAPIS asal."""
    q, ci = np.divmod(np.asarray(flat, np.int64), NC)
    f = lambda c: np.where(c >= 0, SAHAM[np.maximum(c, 0)], -1)
    return q // NQ2 - 1, q % NQ2 - 1, f(C1[ci]), f(C2[ci])


def _atas(sm, k):
    flat = sm.ravel()
    k = min(k, int(np.isfinite(flat).sum()))
    if k == 0:
        return np.zeros(0, np.int32), np.zeros(0, np.float32)
    idx = np.argpartition(-flat, k - 1)[:k]
    idx = idx[np.lexsort((idx, -flat[idx]))]
    return idx.astype(np.int32), flat[idx].astype(np.float32)


def _satu(tugas):
    ti, nama, plasebo = tugas
    pan, ev = _G['pan'], _G['ev'][nama]
    tp = pan['tempoh'][ev].astype(np.int64)
    out = {'n_ev': (int((tp == 0).sum()), int((tp == 1).sum())),
           'rsi50': float(pan['F'][7, ev].mean()) if len(ev) else np.nan}
    if out['n_ev'][0] < N_MIN or out['n_ev'][1] < N_MIN:
        return nama, dict(out, cukup=False)
    V = np.ascontiguousarray(_G['X'][ev][:, (4, NL + 4, 2 * NL + 4)], dtype=np.float64)
    Fm = np.ascontiguousarray(_G['FS'][:, ev].T)
    L1 = np.ascontiguousarray(_G['L1p' if plasebo else 'L1'][:, ev].T)
    L2 = np.ascontiguousarray(_G['L2p' if plasebo else 'L2'][:, ev].T)
    Acc = np.zeros((NQ, NC, 2, 4))
    kumpul5(tp, V, Fm, L1, L2, PASANG, Acc)
    ok, sp, sj = skor_acc(Acc)
    out.update(cukup=True, n_ok=int(ok.sum()), n_ok_S=int(ok[0].sum()))
    for kod, s in (('pilih', sp), ('jumlah', sj)):
        sm = np.where(ok, s, -np.inf)
        out[f'pos_S_{kod}'], out[f'pos_P_{kod}'] = int((sm[0] > 0).sum()), int((sm[1:] > 0).sum())
        ci = sm.argmax(axis=1)
        out[f'q_ci_{kod}'], out[f'q_skor_{kod}'] = ci.astype(np.int16), sm[np.arange(NQ), ci].astype(np.float32)
        out[f'atas_{kod}'] = _atas(sm, N_ATAS)
        out[f'S_{kod}'] = _atas(sm[:1], N_KELAS)                               # tiada prasyarat (q = 0)
        i, v = _atas(sm[1:], N_KELAS)                                          # sekurang-kurangnya satu prasyarat
        out[f'P_{kod}'] = ((i + NC).astype(np.int32), v)
    okf = np.flatnonzero(ok.ravel())
    pilih = np.sort(np.random.default_rng([atom.BENIH, 5, ti]).choice(okf, min(len(okf), N_KOLAM), replace=False))
    out['kolam'] = (pilih.astype(np.int32), sp.ravel()[pilih].astype(np.float32), sj.ravel()[pilih].astype(np.float32))
    return nama, out


def _sedia(kerja, set_):
    pan = cari.panel(kerja, set_)
    bn = pickle.load(open(os.path.join(kerja, f'benih_{set_}.pkl'), 'rb'))
    return pan, bn, cari.pencetus(pan, bn), label_asas2(pan), lapis.muat(kerja, set_)


def besar(kerja, plasebo=False):
    mod = 'plasebo' if plasebo else 'besar'
    f = os.path.join(kerja, f'cs05_{mod}.pkl')
    siap = pickle.load(open(f + '.tmp', 'rb')) if os.path.exists(f + '.tmp') else {}
    pan, bn, ev, X, L = _sedia(kerja, 'A')
    _G.update(pan=pan, ev=ev, X=X, FS=np.ascontiguousarray(pan['F'][SAHAM]), **L)
    kumpul5(np.zeros(1, np.int64), np.zeros((1, 3)), np.zeros((1, NS), np.uint8), np.zeros((1, lapis.N1), np.uint8),
            np.zeros((1, lapis.N2), np.uint8), PASANG, np.zeros((NQ, NC, 2, 4)))            # kompil sebelum fork
    nama = list(ev)
    tugas = sorted([(ti, n, plasebo) for ti, n in enumerate(nama) if n not in siap], key=lambda t: -len(ev[t[1]]))
    cari.log(f'{mod}: {len(tugas)} pencetus (siap {len(siap)}); {sum(len(ev[n]) for n in nama):,} isyarat')
    t0 = time.time()
    with mp.get_context('fork').Pool(cari.PEKERJA) as pool:
        for k, (n, r) in enumerate(pool.imap_unordered(_satu, tugas), 1):
            siap[n] = r
            if k % 50 == 0:
                cari.log(f'  {k}/{len(tugas)} · {time.time() - t0:.0f}s')
                pickle.dump(siap, open(f + '.tmp2', 'wb'), protocol=4)
                os.replace(f + '.tmp2', f + '.tmp')
    out = {n: siap[n] for n in nama}
    out['_meta'] = {'saat': round(time.time() - t0), 'param': bn['param'], 'ralat_benih': bn['ralat']}
    pickle.dump(out, open(f, 'wb'), protocol=4)
    if os.path.exists(f + '.tmp'):
        os.remove(f + '.tmp')
    R = [r for n, r in out.items() if n != '_meta' and r.get('cukup')]
    cari.log(f"{mod} siap: {len(R)} pencetus cukup isyarat; {sum(r['n_ok'] for r in R):,} peraturan masuk diskor "
             f"daripada {len(nama) * NQ * NC:,}; " + ' · '.join(
                 f"{kod}: S>0 {sum(r['pos_S_' + kod] for r in R):,}, P>0 {sum(r['pos_P_' + kod] for r in R):,}"
                 for kod in SKOR))


# ---------- peringkat tepat ----------
def topeng(pan, Lr, ev, q1, q2, f1, f2):
    m = np.ones(len(ev), bool)
    if q1 >= 0:
        m &= Lr[0][q1, ev] > 0
    if q2 >= 0:
        m &= Lr[1][q2, ev] > 0
    for f in (f1, f2):
        if f >= 0:
            m &= pan['F'][f, ev] > 0
    return m


def kadar5(pan, X, Lr, ev, q1, q2, f1, f2):
    """Kadar label dan dua asas setiap tempoh; satu posisi setiap saham (pegang 20 sesi); bilangan hari isyarat."""
    e = ev[topeng(pan, Lr, ev, q1, q2, f1, f2)]
    e = e[teras.satu_posisi(e, np.full(len(e), TMAX - 1), pan['tid'])]
    tp = pan['tempoh'][e]
    out = {}
    for p in range(int(pan['tempoh'].max()) + 1):
        k = e[tp == p]
        x = X[k]
        d = {'n': len(k), 'hari': int(len(np.unique(pan['hari'][k])))}
        for j, nama in enumerate(LABEL):
            for aw, a in (('', 0), ('a_', NL), ('e_', 2 * NL)):
                d[aw + nama] = float(x[:, a + j].mean()) if len(k) else np.nan
        out[p] = d
    return out


def skor_tepat(v, aw):
    if v[0]['n'] < N_MIN or v[1]['n'] < N_MIN:
        return np.nan
    return float(min(tk.lb_lari(v[p]['n'], v[p]['lari'], v[p][aw + 'lari']) for p in (0, 1)))


def _bingkai(nama, flat, skor, **lain):
    q1, q2, f1, f2 = nyah(flat)
    return pd.DataFrame({'pencetus': nama, 'q1': q1, 'q2': q2, 'f1': f1, 'f2': f2, 'skor_besar': skor, **lain})


def tepat(kerja):
    pan, bn, EV, X, L = _sedia(kerja, 'A')
    T = [t[0] for t in atom.TEMPOH['A']]
    B = pickle.load(open(os.path.join(kerja, 'cs05_besar.pkl'), 'rb'))
    PB = pickle.load(open(os.path.join(kerja, 'cs05_plasebo.pkl'), 'rb'))
    meta_b, meta_p = B.pop('_meta'), PB.pop('_meta')
    Lr, Lp = (L['L1'], L['L2']), (L['L1p'], L['L2p'])
    cukup = [n for n, r in B.items() if r.get('cukup')]

    def nilai(D, plasebo):
        v = [kadar5(pan, X, Lp if plasebo else Lr, EV[r.pencetus], r.q1, r.q2, r.f1, r.f2) for r in D.itertuples()]
        return D.assign(plasebo=plasebo, skor_pilih=[skor_tepat(x, 'a_') for x in v],
                        skor_jumlah=[skor_tepat(x, 'e_') for x in v], _v=[dict(zip(T, x.values())) for x in v])

    def sejagat(res, kod):
        D = pd.concat([_bingkai(n, *res[n][f'atas_{kod}']) for n in cukup if res[n].get('cukup')], ignore_index=True)
        return D.sort_values('skor_besar', ascending=False, kind='stable').head(N_ATAS).reset_index(drop=True)

    bhg = []
    for kod in SKOR:
        A = nilai(sejagat(B, kod), False).dropna(subset=[f'skor_{kod}'])
        A = A.sort_values(f'skor_{kod}', ascending=False, kind='stable').reset_index(drop=True)
        A['atas200'] = A.index < N_SENARAI
        # kolam calon papan (pindaan (i) tambahan): + N_KOLAM_PRA teratas setiap pasangan prasyarat, merentas pencetus
        Q = pd.DataFrame({n: B[n][f'q_skor_{kod}'] for n in cukup})                     # [544, pencetus]
        tambah = []
        for q in range(NQ):
            for n in Q.loc[q][np.isfinite(Q.loc[q])].nlargest(N_KOLAM_PRA).index:
                tambah.append((n, q * NC + int(B[n][f'q_ci_{kod}'][q]), float(Q.at[q, n])))
        Tb = _bingkai([t[0] for t in tambah], np.array([t[1] for t in tambah]), [t[2] for t in tambah])
        kunci5 = ['pencetus', 'q1', 'q2', 'f1', 'f2']
        Tb = Tb.merge(A[kunci5], on=kunci5, how='left', indicator=True)
        Tb = nilai(Tb[Tb._merge == 'left_only'].drop(columns='_merge'), False).dropna(subset=[f'skor_{kod}'])
        A = pd.concat([A, Tb.assign(atas200=False)], ignore_index=True)
        A = A.sort_values(f'skor_{kod}', ascending=False, kind='stable').reset_index(drop=True)
        A['peranan'] = np.where(A.atas200, f'atas_{kod}', '')
        guna, keluarga, papan = {}, set(), []
        for i, r in enumerate(A.itertuples()):                       # papan: satu setiap keluarga + had kepelbagaian
            kunci_ = ([f'1:{r.q1}'] if r.q1 >= 0 else []) + ([f'2:{r.q2}'] if r.q2 >= 0 else []) or ['tanpa']
            had = MAKS_TANPA if kunci_ == ['tanpa'] else MAKS_PRA
            if cari.keluarga(r.pencetus) in keluarga or any(guna.get(k, 0) >= had for k in kunci_):
                continue
            keluarga.add(cari.keluarga(r.pencetus))
            for k in kunci_:
                guna[k] = guna.get(k, 0) + 1
            papan.append(i)
            if len(papan) == 10:
                break
        A.loc[papan, 'peranan'] = f'papan_{kod}'
        bhg.append(A[A.peranan != ''].assign(skor_kod=kod))
        cari.log(f'tepat {kod}: {len(A)} sah; papan {len(papan)}')
        W = nilai(sejagat(PB, kod), True).dropna(subset=[f'skor_{kod}'])
        W = W.sort_values(f'skor_{kod}', ascending=False, kind='stable').head(N_SENARAI)
        bhg.append(W.assign(peranan=f'plasebo_{kod}', skor_kod=kod, atas200=False))
    # kolam rawak: seragam atas semua peraturan yang diskor
    K = pd.concat([_bingkai(n, B[n]['kolam'][0], B[n]['kolam'][1], w=B[n]['n_ok'] / max(len(B[n]['kolam'][0]), 1))
                   for n in cukup], ignore_index=True)
    rng = np.random.default_rng(atom.BENIH)
    K = K.loc[np.sort(rng.choice(len(K), N_SENARAI, replace=False, p=(K.w / K.w.sum()).to_numpy()))]
    bhg.append(nilai(K.drop(columns='w'), False).assign(peranan='rawak', skor_kod=''))
    # setiap pencetus: kelas S (tiada prasyarat), P (>= 1 prasyarat), PL (>= 1 prasyarat plasebo)
    for kod in SKOR:
        for kelas, res, pl in (('S', B, False), ('P', B, False), ('PL', PB, True)):
            D = pd.concat([_bingkai(n, *res[n][f"{'S' if kelas == 'S' else 'P'}_{kod}"]) for n in cukup
                           if res.get(n, {}).get('cukup')], ignore_index=True)
            D = nilai(D, pl).dropna(subset=[f'skor_{kod}'])
            D = D.sort_values(f'skor_{kod}', ascending=False, kind='stable').drop_duplicates('pencetus')
            bhg.append(D.assign(peranan='kelas', kelas=kelas, skor_kod=kod))
        cari.log(f'kelas {kod}: siap')
    P = pd.concat(bhg, ignore_index=True)
    P['kelas'] = P['kelas'].fillna('') if 'kelas' in P else ''
    P['atas200'] = P['atas200'].fillna(False).astype(bool)
    # versi TANPA prasyarat (T4) bagi papan dan 200 teratas yang berprasyarat
    perlu = P[P.peranan.str.match('papan_|atas_') & ((P.q1 >= 0) | (P.q2 >= 0))]
    Tn = perlu[['pencetus', 'f1', 'f2', 'skor_kod']].drop_duplicates(['pencetus', 'f1', 'f2']).assign(
        q1=-1, q2=-1, skor_besar=np.nan)
    P = pd.concat([P, nilai(Tn, False).assign(peranan='tanpa', kelas='', skor_kod='')], ignore_index=True)
    # henti x keluar terbaik + ukuran R bagi setup papan
    P['lajur'] = -1
    R = {}
    for k in P.index[P.peranan.str.startswith('papan_')]:
        r = P.loc[k]
        e = EV[r.pencetus][topeng(pan, Lr, EV[r.pencetus], r.q1, r.q2, -1, -1)]
        P.loc[k, 'lajur'] = lj = tk.keluar_terbaik(pan, e, r.f1, r.f2)
        x = cari.nilai(pan, e, r.f1, r.f2, lj, penuh=True, asas=cari.asas_rawak(pan, lj))
        R[k] = dict(zip(T, x.values()))
    V = {k: P._v[k] for k in P.index}
    kelas = {n: ('IKUT TREND' if B[n]['rsi50'] >= 0.5 else 'PANTULAN') for n in B if B[n]['n_ev'][0] + B[n]['n_ev'][1]}
    rk = lambda res: {n: {k: v for k, v in r.items() if k.startswith(('n_', 'pos_', 'cukup', 'rsi50', 'q_'))}
                      for n, r in res.items()}
    pickle.dump({'P': P.drop(columns='_v'), 'V': V, 'R': R, 'kelas': kelas, 'besar': rk(B), 'plasebo': rk(PB),
                 'meta': {'besar': meta_b, 'plasebo': meta_p}},
                open(os.path.join(kerja, 'cs05_pilihan.pkl'), 'wb'), protocol=4)
    cari.log(f'tepat siap: {len(P)} baris; ' + ', '.join(f'{a} {b}' for a, b in P.peranan.value_counts().items()))


# ---------- Kunci (kumpulan B) ----------
def kunci(kerja):
    S = pickle.load(open(os.path.join(kerja, 'cs05_pilihan.pkl'), 'rb'))
    P, V, R = S['P'], S['V'], S['R']
    pan, bn, EV, X, L = _sedia(kerja, 'B')
    T = [t[0] for t in atom.TEMPOH['B']]
    Lr, Lp = (L['L1'], L['L2']), (L['L1p'], L['L2p'])
    for k, r in zip(P.index, P.itertuples()):
        if r.pencetus in EV:
            V[k].update(zip(T, kadar5(pan, X, Lp if r.plasebo else Lr, EV[r.pencetus], r.q1, r.q2, r.f1, r.f2).values()))
    for k in R:
        r = P.loc[k]
        if r.pencetus in EV:
            e = EV[r.pencetus][topeng(pan, Lr, EV[r.pencetus], r.q1, r.q2, -1, -1)]
            x = cari.nilai(pan, e, r.f1, r.f2, r.lajur, penuh=True, asas=cari.asas_rawak(pan, r.lajur))
            R[k].update(zip(T, x.values()))
    cari.log(f'kunci: {len(P)} peraturan dinilai pada kumpulan B')
    # (5e) rujukan: prasyarat sahaja, semua bar layak
    sah = np.flatnonzero(pan['sah'])
    # maklumat tambahan (tidak dipradaftar): setup papan TANPA pencetus = semua bar layak dengan prasyarat + penapis sama
    tp_ = {}
    for k in R:
        r = P.loc[k]
        e = sah[topeng(pan, Lr, sah, r.q1, r.q2, r.f1, r.f2)]
        x = X[e]
        tp_[k] = {'n': len(e), **{aw + n_: float(x[:, a + j].mean()) if len(e) else np.nan
                                 for j, n_ in enumerate(LABEL) for aw, a in (('', 0), ('a_', NL), ('e_', 2 * NL))}}
    k3 = pan['tempoh'][sah] == 2
    xl, xg = X[sah, 4], X[sah, 3]
    ruj = []
    for lap, nama in ((0, lapis.PASARAN), (1, lapis.KUMPULAN)):
        for i, n in enumerate(nama):
            m = Lr[lap][i, sah] > 0
            ruj.append({'prasyarat': n, 'lapisan': 'pasaran' if lap == 0 else 'kumpulan/syarikat', 'bahagian': m.mean(),
                        'bahagian_plasebo': float((Lp[lap][i, sah] > 0).mean()),
                        'hari_benar': int(len(np.unique(pan['hari'][sah[m]]))),
                        'lari_b': xl[m].mean(), 'lari_p': xl[~m].mean(), 'gagal_b': xg[m].mean(), 'gagal_p': xg[~m].mean(),
                        'lari_b_K3': xl[m & k3].mean() if (m & k3).any() else np.nan,
                        'lari_p_K3': xl[~m & k3].mean() if (~m & k3).any() else np.nan})
    # (5b) padanan: setiap pencetus x setiap prasyarat tunggal, tanpa penapis, gabungan K1+K2+K3
    J = (4, NL + 4, 3, NL + 3)                                     # lari, asas lari, gagal, asas gagal
    pad = []

    def ukur(e):
        e = e[teras.satu_posisi(e, np.full(len(e), TMAX - 1), pan['tid'])]
        return (len(e), *(X[np.ix_(e, J)].mean(axis=0) if len(e) else [np.nan] * 4))

    for n, ev in EV.items():
        if len(ev) < N_MIN:
            continue
        pad.append((n, '', False, *ukur(ev)))
        for plasebo, LL in ((False, Lr), (True, Lp)):
            for lap, senarai in ((0, lapis.PASARAN), (1, lapis.KUMPULAN)):
                for i, q in enumerate(senarai):
                    pad.append((n, q[:4], plasebo, *ukur(ev[LL[lap][i, ev] > 0])))
    pad = pd.DataFrame(pad, columns=['pencetus', 'prasyarat', 'plasebo', 'n', 'lari', 'a_lari', 'gagal', 'a_gagal'])
    pickle.dump({'V': V, 'R': R, 'tanpa_pencetus': tp_, 'rujukan': pd.DataFrame(ruj), 'padanan': pad,
                 'ralat_benih_B': bn['ralat'],
                 'param_B': bn['param']}, open(os.path.join(kerja, 'cs05_kunci.pkl'), 'wb'), protocol=4)
    cari.log(f'kunci siap: padanan {len(pad):,} baris')


# ---------- laporan ----------
def tk_pra(q1, q2, kod=False):
    b = ([lapis.PASARAN[q1]] if q1 >= 0 else []) + ([lapis.KUMPULAN[q2]] if q2 >= 0 else [])
    if kod:
        return '+'.join(x[:4] for x in b)
    return ' DAN '.join(b) if b else 'tiada'


def tk_pen(f1, f2):
    return ' DAN '.join(atom.PENAPIS[f] for f in (f1, f2) if f >= 0) or 'tiada'


def buang_kod(s):
    return re.sub(r'\b(Q[A-H]\d\d|F\d\d) ', '', str(s))


def gab(v, T, nama):
    n = sum(v.get(t, {}).get('n', 0) for t in T)
    return n, (sum(v[t]['n'] * v[t][nama] for t in T if v.get(t, {}).get('n')) / n if n else np.nan)


def lebih(v, T, aw, nama='lari'):
    return gab(v, T, nama)[1] - gab(v, T, aw + nama)[1]


def isi_prasyarat(reg):
    """Lajur `prasyarat` dan `syarat` bagi baris lama (F01-F38): F26-F28 = prasyarat pasaran; selebihnya syarat."""
    import cs_ringkas
    for i in reg.index:
        if not str(reg.at[i, 'prasyarat']).strip() and not str(reg.at[i, 'syarat']).strip():
            pas, sah = cs_ringkas.bahagi(reg.at[i, 'penapis'])
            reg.at[i, 'prasyarat'], reg.at[i, 'syarat'] = pas.replace('–', 'tiada'), sah.replace('–', 'tiada')
    return reg


def daftar(baris, param):
    """Daftar setup papan dalam keluarga F. Takrif yang sudah berdaftar mengekalkan ID dan barisnya TIDAK disentuh."""
    reg = pd.read_csv(lapor.REG_F, dtype=str).fillna('').reindex(columns=lapor.LAJUR_F, fill_value='')
    reg = isi_prasyarat(reg)
    tujuan = os.path.join(KELUAR_UJI, 'registry_F.csv') if KELUAR_UJI else lapor.REG_F
    idf = {}
    for k, b in baris.items():
        lama = reg[reg.takrif == b['takrif']]
        if len(lama):
            idf[k] = lama.id.iloc[0]
            continue
        fid = f"F{max(int(x[1:]) for x in reg.id) + 1:02d}"
        P = param.get(b.pop('_pencetus'))
        baru = dict.fromkeys(lapor.LAJUR_F, '')
        baru.update(id=fid, keluarga='F', pusingan=PUS, tarikh_daftar=pd.Timestamp.now().strftime('%Y-%m-%d'),
                    param=json.dumps({a: round(x, 6) for a, x in P.items()}, sort_keys=True) if P else '',
                    status='BACKTEST', **b)
        reg = pd.concat([reg, pd.DataFrame([baru])[lapor.LAJUR_F].astype(str)], ignore_index=True)
        idf[k] = fid
    reg.to_csv(tujuan, index=False)
    return idf


def lapor_(kerja):
    S = pickle.load(open(os.path.join(kerja, 'cs05_pilihan.pkl'), 'rb'))
    KV = pickle.load(open(os.path.join(kerja, 'cs05_kunci.pkl'), 'rb'))
    P, V, R, kelas = S['P'], KV['V'], KV['R'], S['kelas']
    param = S['meta']['besar']['param']
    TC, TK = [t[0] for t in atom.TEMPOH['A']], [t[0] for t in atom.TEMPOH['B']]
    d = KELUAR_UJI or os.path.join(SINI, 'hasil', PUS)
    os.makedirs(d, exist_ok=True)
    p = lambda x, k=1, t=False: '–' if x is None or x != x else (f'{x * 100:+.{k}f}' if t else f'{x * 100:.{k}f}')
    ya = lambda b: '–' if b is None else ('✓' if b else '✗')
    med = lambda s: float(np.nanmedian(s)) if len(s) else np.nan
    for aw in ('a_', 'e_'):
        P[f'kl_{aw}'] = [lebih(V[k], TK, aw) for k in P.index]
        P[f'kl3_{aw}'] = [lebih(V[k], ['K3'], aw) for k in P.index]
        for t in TK:
            P[f'kl_{aw}{t}'] = [lebih(V[k], [t], aw) for k in P.index]
    P['n_kunci'] = [gab(V[k], TK, 'lari')[0] for k in P.index]
    for t in TK:
        P[f'n_{t}'] = [V[k].get(t, {}).get('n', 0) for k in P.index]
    P['lari_kunci'] = [gab(V[k], TK, 'lari')[1] for k in P.index]
    P['gagal_kunci'] = [gab(V[k], TK, 'gagal')[1] for k in P.index]
    P['hari_kunci'] = [sum(V[k].get(t, {}).get('hari', 0) for t in TK) for k in P.index]
    P['prasyarat'] = [tk_pra(a, b) for a, b in zip(P.q1, P.q2)]
    P['penapis'] = [tk_pen(a, b) for a, b in zip(P.f1, P.f2)]
    P['masuk'] = [lapor.nama_pencetus(n, param) for n in P.pencetus]
    tanpa = {(r.pencetus, r.f1, r.f2): k for k, r in zip(P.index, P.itertuples()) if r.peranan == 'tanpa'}
    rawak = P[(P.peranan == 'rawak') & (P.n_kunci >= 100)]

    # ----- papan -----
    papan, daftar_b = {}, {}
    for kod in SKOR:
        aw = ASAS[kod]
        p95 = float(rawak[f'kl_{aw}'].quantile(0.95))
        for kd, k in enumerate(P.index[P.peranan == f'papan_{kod}'], 1):
            r, v = P.loc[k], V[k]
            ada = lambda nama: bool(all(v.get(t, {}).get('n') and v[t][nama] > v[t][aw + nama] for t in TK))
            T4 = None
            if r.q1 >= 0 or r.q2 >= 0:
                kt = tanpa[(r.pencetus, r.f1, r.f2)]
                T4 = bool(r[f'kl_{aw}'] > P.at[kt, f'kl_{aw}'] and r[f'kl3_{aw}'] > P.at[kt, f'kl3_{aw}'])
            s, x = divmod(int(r.lajur), cari.NR)
            a, b, op = cari.A1[x], cari.A2[x], cari.OP[x]
            kel = 'X00' if op == 0 else atom.KELUAR[a][:3] if op == 1 else (
                f"{atom.KELUAR[a][:3]} {'ATAU' if op == 2 else 'DAN'} {atom.KELUAR[b][:3]}")
            takrif = (f"{r.pencetus}|{'+'.join(atom.PENAPIS[f][:3] for f in (r.f1, r.f2) if f >= 0) or '-'}|"
                      f"{atom.HENTI[s][:2]}|{kel}")
            if r.q1 >= 0 or r.q2 >= 0:
                takrif += '|' + tk_pra(r.q1, r.q2, kod=True)
            T = dict(T1=ada('t10'), T2=ada('lari'), T3=bool(r.n_kunci >= 100 and r[f'kl_{aw}'] > p95), T4=T4)
            papan[k] = dict(kod=kod, kd=kd, henti=atom.HENTI[s],
                            keluar=teras.nama_keluar(x, cari.A1, cari.A2, cari.OP, atom.KELUAR), takrif=takrif, **T)
            rr = {t: {**{'n': 0, 'purata': np.nan}, **R[k].get(t, {})} for t in TC + TK}
            ringkas_ = lambda x: 'tiada' if x == 'tiada' else buang_kod(x).replace(' DAN ', ' + ')
            b_ = dict(_pencetus=r.pencetus, takrif=takrif, masuk=r.masuk, penapis=r.penapis, henti=atom.HENTI[s],
                      keluar=papan[k]['keluar'], skor_tepat=f"{r[f'skor_{kod}']:.5f}", T1=T['T1'], T2=T['T2'], T3=T['T3'],
                      prasyarat=ringkas_(r.prasyarat), syarat=ringkas_(r.penapis))
            for i, t in enumerate(TC, 1):
                b_[f'n_cari{i}'] = rr[t]['n']
                b_[f'purata_cari{i}'] = '' if not rr[t]['n'] else f"{rr[t]['purata']:.5f}"
            for t in TK:
                b_[f'n_{t}'] = rr[t]['n']
                b_[f'purata_{t}'] = '' if not rr[t]['n'] else f"{rr[t]['purata']:.5f}"
                b_[f'k10_{t}'] = '' if not rr[t]['n'] else f"{rr[t].get('k10', float('nan')):.4f}"
            daftar_b[k] = b_
    idf = daftar(daftar_b, param)

    # ----- setiap pencetus: S lawan P lawan PL -----
    Kl = P[P.peranan == 'kelas']
    M = []
    for n in sorted(S['besar'], key=lambda x: (x[0], int(re.sub(r'\D', '', x.split('.')[0])), x)):
        b = S['besar'][n]
        r = {'pencetus': n, 'nama': lapor.nama_pencetus(n, param), 'keluarga': cari.keluarga(n), 'kelas': kelas.get(n, ''),
             'n_E1': b['n_ev'][0], 'n_E2': b['n_ev'][1], 'cukup_isyarat': int(bool(b.get('cukup')))}
        for kod in SKOR:
            aw = ASAS[kod]
            for kl in ('S', 'P', 'PL'):
                x = Kl[(Kl.pencetus == n) & (Kl.skor_kod == kod) & (Kl.kelas == kl)]
                if not len(x):
                    continue
                x = x.iloc[0]
                a = f'{kod}_{kl}_'
                r.update({a + 'prasyarat': x.prasyarat, a + 'penapis': x.penapis, a + 'skor_A': x[f'skor_{kod}'],
                          a + 'n': int(x.n_kunci), a + 'hari': int(x.hari_kunci), a + 'lari': x.lari_kunci,
                          a + 'asas': gab(V[x.name], TK, aw + 'lari')[1], a + 'lebih': x[f'kl_{aw}'],
                          a + 'gagal': x.gagal_kunci, a + 'n_K3': int(x.n_K3), a + 'lebih_K3': x[f'kl3_{aw}']})
        M.append(r)
    M = pd.DataFrame(M)
    M.to_csv(os.path.join(d, 'SEMUA_PENCETUS.csv'), index=False, float_format='%.5f')
    bacaan = {}
    for kod in SKOR:
        g = lambda kl, kol: M.get(f'{kod}_{kl}_{kol}', pd.Series(np.nan, index=M.index))
        ok = (g('S', 'n') >= 100) & (g('P', 'n') >= 100) & (g('PL', 'n') >= 100)
        ok3 = ok & (g('S', 'n_K3') >= 50) & (g('P', 'n_K3') >= 50) & (g('PL', 'n_K3') >= 50)
        dP, dL = (g('P', 'lebih') - g('S', 'lebih'))[ok], (g('PL', 'lebih') - g('S', 'lebih'))[ok]
        dP3, dL3 = (g('P', 'lebih_K3') - g('S', 'lebih_K3'))[ok3], (g('PL', 'lebih_K3') - g('S', 'lebih_K3'))[ok3]
        bacaan[kod] = dict(
            n=int(ok.sum()), n3=int(ok3.sum()), med_P=med(dP), med_PL=med(dL), med_P3=med(dP3), med_PL3=med(dL3),
            P_atas_S=int((dP > 0).sum()), PL_atas_S=int((dL > 0).sum()), P_atas_PL=int((dP > dL).sum()),
            P_atas_S3=int((dP3 > 0).sum()), PL_atas_S3=int((dL3 > 0).sum()), P_atas_PL3=int((dP3 > dL3).sum()),
            med_lari_S=med(g('S', 'lari')[ok]), med_lari_P=med(g('P', 'lari')[ok]), med_lari_PL=med(g('PL', 'lari')[ok]),
            med_gagal_S=med(g('S', 'gagal')[ok]), med_gagal_P=med(g('P', 'gagal')[ok]),
            med_gagal_PL=med(g('PL', 'gagal')[ok]),
            med_lebih_S=med(g('S', 'lebih')[ok]), med_lebih_P=med(g('P', 'lebih')[ok]), med_lebih_PL=med(g('PL', 'lebih')[ok]))
        bacaan[kod]['menolong'] = bool(bacaan[kod]['med_P'] > 0 and bacaan[kod]['med_P'] > bacaan[kod]['med_PL'])
        bacaan[kod]['menolong_K3'] = bool(bacaan[kod]['med_P3'] > 0 and bacaan[kod]['med_P3'] > bacaan[kod]['med_PL3'])

    # ----- padanan kelas x prasyarat -----
    pad, ruj = KV['padanan'], KV['rujukan'].set_index(KV['rujukan'].prasyarat.str[:4])
    asas0 = pad[pad.prasyarat == ''].set_index('pencetus')
    pad = pad[(pad.prasyarat != '') & (pad.n >= 100)].copy()
    pad['kelas'] = pad.pencetus.map(kelas)
    for kol, f in (('d_lari', lambda x: x.lari), ('d_lebih', lambda x: x.lari - x.a_lari), ('d_gagal', lambda x: x.gagal)):
        pad[kol] = f(pad) - pad.pencetus.map(f(asas0))
    PD = pad.groupby(['prasyarat', 'plasebo', 'kelas']).agg(
        pencetus=('n', 'size'), d_lari=('d_lari', 'median'), d_lebih=('d_lebih', 'median'), d_gagal=('d_gagal', 'median'),
        naik=('d_lebih', lambda x: float((x > 0).mean()))).reset_index()
    PD.to_csv(os.path.join(d, 'PADANAN.csv'), index=False, float_format='%.5f')
    KV['rujukan'].to_csv(os.path.join(d, 'prasyarat_rujukan.csv'), index=False, float_format='%.5f')

    # ----- rekod: terbaik setiap (pencetus x pasangan prasyarat), kumpulan A -----
    bah = []
    for n, b in S['besar'].items():
        if not b.get('cukup'):
            continue
        q = np.arange(NQ)
        f = {kod: nyah(q * NC + b[f'q_ci_{kod}'].astype(np.int64)) for kod in SKOR}
        t = pd.DataFrame({'pencetus': n, 'q1': f['pilih'][0], 'q2': f['pilih'][1]})
        for kod in SKOR:
            t[f'f1_{kod}'], t[f'f2_{kod}'] = f[kod][2], f[kod][3]
            t[f'skor_{kod}'] = np.round(b[f'q_skor_{kod}'].astype(float) * 100, 3)
        bah.append(t[np.isfinite(t.skor_pilih)])
    TB = pd.concat(bah, ignore_index=True)
    TB['q1'] = [lapis.PASARAN[i][:4] if i >= 0 else '' for i in TB.q1]
    TB['q2'] = [lapis.KUMPULAN[i][:4] if i >= 0 else '' for i in TB.q2]
    TB.to_csv(os.path.join(d, 'terbaik_prasyarat.csv.gz'), index=False, compression={'method': 'gzip', 'mtime': 0})

    # ----- senarai Kunci -----
    lajur = (['peranan', 'skor_kod', 'atas200', 'kelas', 'plasebo', 'masuk', 'prasyarat', 'penapis', 'skor_besar', 'skor_pilih',
              'skor_jumlah', 'n_kunci', 'hari_kunci', 'lari_kunci', 'gagal_kunci', 'kl_a_', 'kl_e_', 'kl3_a_', 'kl3_e_']
             + [f'n_{t}' for t in TK] + [f'kl_{aw}{t}' for aw in ('a_', 'e_') for t in TK])
    P[P.peranan != 'kelas'][lajur].to_csv(os.path.join(d, 'senarai_kunci.csv'), index=False, float_format='%.5f')
    csvb = []
    for k, b in papan.items():
        for t in TC + TK:
            csvb.append({'papan': b['kod'], 'kedudukan': b['kd'], 'id': idf[k], 'masuk': P.at[k, 'masuk'],
                         'prasyarat': P.at[k, 'prasyarat'], 'penapis': P.at[k, 'penapis'], 'henti': b['henti'],
                         'keluar': b['keluar'], 'takrif': b['takrif'], 'skor_tepat': P.at[k, f"skor_{b['kod']}"],
                         'tempoh': t, **V[k].get(t, {}), **{'R_' + a: x for a, x in R[k].get(t, {}).items()},
                         **{x: b[x] for x in ('T1', 'T2', 'T3', 'T4')}})
    pd.DataFrame(csvb).to_csv(os.path.join(d, 'papan.csv'), index=False, float_format='%.5f')

    # ----- semakan kejujuran -----
    jujur = {}
    for kod in SKOR:
        aw = ASAS[kod]
        kump = {'atas': P[P.peranan.isin([f'atas_{kod}', f'papan_{kod}']) & (P.atas200 == True)],  # noqa: E712
                'rawak': P[P.peranan == 'rawak'],
                'plasebo': P[P.peranan == f'plasebo_{kod}']}
        jujur[kod] = {}
        for t in TK:
            e = {a: x[x[f'n_{t}'] >= 50][f'kl_{aw}{t}'] for a, x in kump.items()}
            xa = kump['atas'][kump['atas'][f'n_{t}'] >= 50]
            jujur[kod][t] = {**{f'med_{a}': med(x) for a, x in e.items()}, **{f'n_{a}': len(x) for a, x in e.items()},
                             **{f'pos_{a}': int((x > 0).sum()) for a, x in e.items()},
                             'rho': float(xa[[f'skor_{kod}', f'kl_{aw}{t}']].corr(method='spearman').iloc[0, 1])}
        ka = kump['atas']
        jujur[kod]['berprasyarat'] = int(((ka.q1 >= 0) | (ka.q2 >= 0)).sum())
        jujur[kod]['n_atas'] = len(ka)
        jujur[kod]['pra_kerap'] = pd.concat([ka.q1[ka.q1 >= 0].map(lambda i: lapis.PASARAN[i]),
                                             ka.q2[ka.q2 >= 0].map(lambda i: lapis.KUMPULAN[i])]).value_counts().head(6).to_dict()

    # ----- meta -----
    Bs, Ps = S['besar'], S['plasebo']
    cukup = [n for n, b in Bs.items() if b.get('cukup')]
    meta = {'pusingan': PUS, 'pencetus': len(Bs), 'pencetus_cukup': len(cukup), 'masuk_dicuba': len(Bs) * NQ * NC,
            'masuk_diskor': int(sum(Bs[n]['n_ok'] for n in cukup)),
            'masuk_diskor_tanpa_prasyarat': int(sum(Bs[n]['n_ok_S'] for n in cukup)),
            'masuk_diskor_plasebo': int(sum(Ps[n]['n_ok'] for n in cukup if Ps.get(n, {}).get('cukup'))),
            'saat_besar': S['meta']['besar']['saat'], 'saat_plasebo': S['meta']['plasebo']['saat'],
            'ikut_trend': int(sum(kelas.get(n) == 'IKUT TREND' for n in cukup)),
            'pantulan': int(sum(kelas.get(n) == 'PANTULAN' for n in cukup)),
            'ralat_benih_cari': S['meta']['besar']['ralat_benih'], 'ralat_benih_kunci': KV['ralat_benih_B']}
    for kod in SKOR:
        nS, nP = meta['masuk_diskor_tanpa_prasyarat'], meta['masuk_diskor'] - meta['masuk_diskor_tanpa_prasyarat']
        meta[f'positif_S_{kod}'] = sum(Bs[n][f'pos_S_{kod}'] for n in cukup) / max(nS, 1)
        meta[f'positif_P_{kod}'] = sum(Bs[n][f'pos_P_{kod}'] for n in cukup) / max(nP, 1)
        npl = sum(Ps[n]['n_ok'] - Ps[n]['n_ok_S'] for n in cukup if Ps.get(n, {}).get('cukup'))
        meta[f'positif_PL_{kod}'] = sum(Ps[n][f'pos_P_{kod}'] for n in cukup if Ps.get(n, {}).get('cukup')) / max(npl, 1)
        meta[f'p95_rawak_{kod}'] = float(rawak[f'kl_{ASAS[kod]}'].quantile(0.95))
        meta[f'bacaan_{kod}'] = bacaan[kod]
        meta[f'jujur_{kod}'] = jujur[kod]
    json.dump(meta, open(os.path.join(d, 'meta.json'), 'w'), indent=1, default=float)

    # ----- LAPORAN.md -----
    try:
        sys.path.insert(0, os.path.join(lapor.BS2, 'standard'))
        import status_kad
        status = status_kad.baris()
    except Exception:
        status = '> **Status keputusan:** lihat `laporan/KAD_SKOR.md`; laporan ini BUKAN keputusan.'
    import cs_ringkas
    pendek = lambda s: buang_kod(cs_ringkas.nama_pendek(s))
    nama_skor = {'pilih': 'PILIH (lawan saham rawak HARI SAMA)', 'jumlah': 'JUMLAH (lawan saham rawak sepanjang ERA)'}
    TKt = lapor.KONFIG['CS02']['terang']
    A = [f'# Carian Setup {PUS} — PRASYARAT + SYARAT bagi semua kaedah (backtest, BUKAN bukti)', '', status, '',
         'Dijana `kajian/carian_setup/cs_cs05.py`. Pradaftar: `kajian/SPEC_CARIAN_SETUP.md` pindaan 14 Nov 2026 (i), dikomit '
         'sebelum pusingan ini dijalankan. **Jangan sunting secara manual.** Pusingan lama ("syarat sahaja"): '
         '`carian_setup/hasil/CS01`–`CS04/LAPORAN.md`.', '',
         '## 1. Apa yang diuji', '',
         'Setup lengkap = **prasyarat** (pasaran; kumpulan/syarikat) → **syarat** (pencetus + penapis saham itu sendiri). '
         'Ukuran: KADAR TANGKAP saham "lari" (naik ≥ 5 % minggu pertama, capai ≥ 10 % sebelum henti −8 %, masih ≥ 10 % pada '
         'minggu ke-4). Dua kayu ukur:', '',
         '- **Pilih:** kadar lari setup tolak saham rawak pada **hari yang sama** dan tahap turun-naik sama. Mengukur '
         'kemahiran memilih saham. Prasyarat pasaran menaikkan saham rawak hari itu juga, jadi ia hanya dikira jika '
         'pencetus memilih lebih baik pada hari begitu.',
         '- **Jumlah:** kadar lari setup tolak saham rawak **sepanjang era**. Memasukkan kesan BILA membeli (sumbangan '
         'prasyarat pasaran). Hari isyarat berkelompok, jadi baca bersama plasebo dan bilangan hari isyarat.', '',
         f"Carian (kumpulan A, 2010–2024): {meta['pencetus']} pencetus ({meta['pencetus_cukup']} cukup isyarat) × 34 pilihan "
         f"prasyarat pasaran × 16 pilihan prasyarat kumpulan/syarikat × 379 gabungan penapis saham = "
         f"**{meta['masuk_dicuba']:,} peraturan masuk dicuba**, {meta['masuk_diskor']:,} cukup isyarat (≥ 100 dalam setiap era). "
         f"Carian yang sama diulang dengan prasyarat **plasebo** (dianjak 437 sesi). Angka di bawah daripada **kumpulan B** "
         '(saham yang carian tidak lihat), 2010 – Ogo 2026; **K3 = 2025 – Ogo 2026 ialah ujian sebenar**.', '',
         '## 2. Jawapan ringkas: adakah prasyarat menolong?', '',
         'Bagi setiap pencetus, tiga peraturan dipilih pada kumpulan A: terbaik **syarat sahaja** (S), terbaik **dengan '
         'prasyarat** (P) dan terbaik dengan **prasyarat plasebo** (PL); semuanya diukur pada kumpulan B. '
         'Bacaan dikunci (pindaan (i) butir 6): prasyarat "menolong" hanya jika median (P − S) positif DAN melebihi median '
         '(PL − S).', '',
         '| Kayu ukur | Pencetus dibanding | Median lari %: S / P / PL | Median kena henti %: S / P / PL | Median kelebihan: S / P / PL | '
         'Median (P − S) | Median (PL − S) | P > S | P > PL | **Menolong?** |', '|---' * 10 + '|']
    for kod in SKOR:
        b = bacaan[kod]
        for tajuk, s in ((f'{kod.capitalize()}, kumpulan B', ''), (f'{kod.capitalize()}, K3 sahaja', '3')):
            if s == '':
                A.append(f"| {tajuk} | {b['n']} | {p(b['med_lari_S'])} / {p(b['med_lari_P'])} / {p(b['med_lari_PL'])} | "
                         f"{p(b['med_gagal_S'])} / {p(b['med_gagal_P'])} / {p(b['med_gagal_PL'])} | "
                         f"{p(b['med_lebih_S'], 2, True)} / {p(b['med_lebih_P'], 2, True)} / {p(b['med_lebih_PL'], 2, True)} | "
                         f"{p(b['med_P'], 2, True)} | {p(b['med_PL'], 2, True)} | {b['P_atas_S']} / {b['n']} | "
                         f"{b['P_atas_PL']} / {b['n']} | **{'YA' if b['menolong'] else 'TIDAK'}** |")
            else:
                A.append(f"| {tajuk} | {b['n3']} | | | | {p(b['med_P3'], 2, True)} | {p(b['med_PL3'], 2, True)} | "
                         f"{b['P_atas_S3']} / {b['n3']} | {b['P_atas_PL3']} / {b['n3']} | "
                         f"**{'YA' if b['menolong_K3'] else 'TIDAK'}** |")
    A += ['', 'Unit kelebihan dan beza: mata peratus. Jadual setiap pencetus: `carian_setup/hasil/CS05/SEMUA_PENCETUS.md`.', '']
    for bil, kod in enumerate(SKOR, 3):
        aw = ASAS[kod]
        A += [f'## {bil}. Papan 10 teratas — kayu ukur {nama_skor[kod]}', '',
              '| # | ID | Prasyarat | Pencetus | Penapis saham | Belian (hari isyarat) | **Lari %** (rawak) | Capai +10 % dahulu % (rawak) | '
              'Kena henti −8 % dahulu % (rawak) | Kelebihan lari K1 / K2 / K3 | T1 | T2 | T3 | T4 |', '|---' * 14 + '|']
        for k, b in papan.items():
            if b['kod'] != kod:
                continue
            r, v = P.loc[k], V[k]
            sel = lambda n: f'{p(gab(v, TK, n)[1])} ({p(gab(v, TK, aw + n)[1])})'
            A.append(f"| {b['kd']} | `{idf[k]}` | {buang_kod(r.prasyarat)} | {pendek(r.masuk)} | {buang_kod(r.penapis)} | "
                     f"{int(r.n_kunci):,} ({int(r.hari_kunci):,}) | **{sel('lari')}** | {sel('t10')} | {sel('gagal')} | "
                     + ' / '.join(p(r[f'kl_{aw}{t}'], 1, True) for t in TK)
                     + f" | {ya(b['T1'])} | {ya(b['T2'])} | {ya(b['T3'])} | {ya(b['T4'])} |")
        A += ['', f"- \"Rawak\" = {'saham lain yang layak pada hari yang sama' if kod == 'pilih' else 'semua saham layak sepanjang era yang sama'}"
              ' dan tahap turun-naik yang sama. **T1:** kelebihan "capai +10 % dahulu" positif dalam K1, K2 dan K3. **T2:** kelebihan '
              f"\"lari\" positif dalam ketiga-tiganya. **T3:** kelebihan lari melebihi persentil ke-95 peraturan rawak "
              f"({p(meta[f'p95_rawak_{kod}'], 2, True)} mata). **T4:** kelebihan lari (kumpulan B DAN K3) melebihi setup yang sama "
              'TANPA prasyarat.', '',
              'Cara pegang dan keluar terbaik bagi setiap setup (dipilih pada kumpulan A; angka kumpulan B, kos 0.5 % ditolak, '
              'jurang melepasi henti dijual pada harga buka):', '',
              '| ID | Henti | Keluar | ' + ' | '.join(f'{t}: purata % / menang % / pegang' for t in TK)
              + ' | Dagangan ≥ +10 % / rugi ≤ −8 % (kumpulan B) |', '|---' * (4 + len(TK)) + '|']
        for k, b in papan.items():
            if b['kod'] != kod:
                continue
            rr = {t: {**{'n': 0, 'purata': np.nan}, **R[k].get(t, {})} for t in TK}
            nR = sum(rr[t]['n'] for t in TK)
            wR = lambda kol: sum(rr[t]['n'] * rr[t][kol] for t in TK if rr[t]['n']) / nR if nR else np.nan
            A.append(f"| `{idf[k]}` | {b['henti']} | {b['keluar']} | " + ' | '.join(
                f"{p(rr[t]['purata'], 2, True)} / {p(rr[t].get('menang', np.nan))} / {rr[t].get('pegang', np.nan):.1f}"
                if rr[t]['n'] else '–' for t in TK) + f" | {p(wR('k10'))} / {p(wR('rugi8'))} |")
        A += ['', 'Dari mana datangnya kadar tangkap? Setiap sel: lari % (rawak %) · kena henti %, kumpulan B. "Tanpa pencetus" = '
              'semua saham layak yang memenuhi prasyarat dan penapis yang sama (maklumat tambahan, tidak dipradaftar):', '',
              '| ID | Setup penuh | Syarat sahaja (buang prasyarat) | Prasyarat + penapis sahaja (buang pencetus) |', '|---' * 4 + '|']
        for k, b in papan.items():
            if b['kod'] != kod:
                continue
            r, v = P.loc[k], V[k]
            sel3 = lambda x: f"{p(gab(x, TK, 'lari')[1])} ({p(gab(x, TK, aw + 'lari')[1])}) · {p(gab(x, TK, 'gagal')[1])}"
            kt = tanpa.get((r.pencetus, r.f1, r.f2))
            x = KV['tanpa_pencetus'][k]
            A.append(f"| `{idf[k]}` | {sel3(v)} | {sel3(V[kt]) if kt is not None else 'sama (tiada prasyarat)'} | "
                     f"{p(x['lari'])} ({p(x[aw + 'lari'])}) · {p(x['gagal'])} |")
        j = jujur[kod]
        A += ['', f"**Semakan kejujuran ({kod}).** {j['berprasyarat']} daripada {j['n_atas']} peraturan teratas memakai "
              'sekurang-kurangnya satu prasyarat; paling kerap: '
              + '; '.join(f'{buang_kod(a)} ({b})' for a, b in j['pra_kerap'].items()) + '.', '',
              '| Ukuran (kelebihan lari, mata peratus) | ' + ' | '.join(TKt[t] for t in TK) + ' |', '|---' * (1 + len(TK)) + '|']
        for a, tajuk in (('atas', 'peraturan teratas (prasyarat sebenar)'), ('plasebo', 'peraturan teratas PLASEBO'),
                         ('rawak', 'peraturan rawak')):
            A.append(f'| Median, {tajuk} | ' + ' | '.join(
                f"{p(j[t][f'med_{a}'], 2, True)} ({j[t][f'pos_{a}']} / {j[t][f'n_{a}']} positif)" for t in TK) + ' |')
        A += ['| Spearman skor lawan kelebihan (teratas) | ' + ' | '.join(f"{j[t]['rho']:+.2f}" for t in TK) + ' |', '']
    # padanan
    A += ['## 5. Padanan jenis setup × prasyarat (kumpulan B, tanpa penapis)', '',
          f"Kelas dikunci secara mekanikal: **IKUT TREND** ({meta['ikut_trend']} pencetus) jika ≥ 50 % isyaratnya mempunyai "
          f"RSI14 > 50; selainnya **PANTULAN** ({meta['pantulan']}). Setiap sel = median merentas pencetus bagi perubahan bila "
          'prasyarat benar berbanding semua isyarat pencetus itu: **Δ lari** (kadar lari mutlak) / **Δ kelebihan** (lawan rawak '
          'hari sama) / **Δ henti** (kadar kena henti), mata peratus. "Plasebo" = Δ kelebihan dengan prasyarat dianjak masa.', '',
          '| Prasyarat | % masa benar | Semua saham: lari % benar / palsu | Semua saham: kena henti % benar / palsu | '
          'IKUT TREND: Δ lari / Δ kelebihan / Δ henti | (plasebo) | PANTULAN: Δ lari / Δ kelebihan / Δ henti | (plasebo) |',
          '|---' * 8 + '|']
    pdx = PD.set_index(['prasyarat', 'plasebo', 'kelas'])

    def sel_pad(q, kl):
        if (q, False, kl) not in pdx.index:
            return '–', '–'
        x = pdx.loc[(q, False, kl)]
        pl = pdx.loc[(q, True, kl)].d_lebih if (q, True, kl) in pdx.index else np.nan
        return f'{p(x.d_lari, 1, True)} / {p(x.d_lebih, 1, True)} / {p(x.d_gagal, 1, True)}', p(pl, 1, True)

    for tajuk, senarai in (('Pasaran', lapis.PASARAN), ('Kumpulan / syarikat', lapis.KUMPULAN)):
        A.append(f'| **{tajuk}** | | | | | | | |')
        for q in senarai:
            x = ruj.loc[q[:4]]
            a, b = sel_pad(q[:4], 'IKUT TREND'), sel_pad(q[:4], 'PANTULAN')
            A.append(f"| {q[5:]} | {p(x.bahagian, 0)} | {p(x.lari_b)} / {p(x.lari_p)} | {p(x.gagal_b)} / {p(x.gagal_p)} | "
                     f'{a[0]} | {a[1]} | {b[0]} | {b[1]} |')
    A += ['', '## 6. Kaveat', '',
          '- Backtest sahaja; papan ialah pangkat, BUKAN bukti. Kohort jejak hadapan (`jejak_f/`) TIDAK berubah; menukar kohort '
          'ialah keputusan pengguna yang berasingan. Kad skor kekal satu-satunya keputusan wang sebenar.',
          '- Lebih 100 juta peraturan dicuba: yang teratas pada kumpulan A sebahagiannya nasib. Sebab itu setiap angka di atas '
          'daripada kumpulan B, bersebelahan peraturan rawak dan plasebo.',
          '- Prasyarat pasaran berubah ikut HARI: belian banyak tetapi hari isyarat berbeza sedikit (lajur "hari isyarat"); satu '
          'episod pasaran boleh menentukan hasil. K3 hanya 20 bulan.',
          '- "Earnings akan datang" memakai tarikh sebenar (pandang ke hadapan ringan; papertrade memerlukan kalendar earnings). '
          'Peta sektor/industri ialah peta semasa. `QH07` ialah proksi (tiada VIX dalam repo).',
          '- Tiada saham delist (condong ke atas); set 2000 bukan tapisan Shariah; data bermula 2010.',
          '- Prasyarat yang menaikkan kadar lari selalunya turut menaikkan kadar kena henti: baca kedua-dua lajur.', '']
    teks = '\n'.join(A)
    open(os.path.join(d, 'LAPORAN.md'), 'w', encoding='utf-8').write(teks)
    if not KELUAR_UJI:
        open(os.path.join(lapor.BS2, 'kajian', 'CARIAN_SETUP.md'), 'w', encoding='utf-8').write(teks)

    # ----- SEMUA_PENCETUS.md -----
    g = lambda r, kol: getattr(r, kol, np.nan)
    txt = lambda x: '–' if x != x or x in ('', 'tiada') else buang_kod(x).replace(' DAN ', ' + ')
    Bm = ['# CS05: SETIAP pencetus — syarat sahaja lawan dengan prasyarat (kumpulan B; backtest, BUKAN bukti)', '', status, '',
          'Dijana `kajian/carian_setup/cs_cs05.py`. **Jangan sunting secara manual.** Lajur penuh (termasuk plasebo dan K3): '
          '`SEMUA_PENCETUS.csv`.', '',
          'Bagi setiap pencetus, peraturan terbaik dipilih pada kumpulan A (saham yang dicari) dan **diukur pada kumpulan B** '
          '(saham yang tidak dilihat, 2010 – Ogo 2026). Setiap sel: **lari %** (rawak %) · kena henti %. "Rawak" bagi kayu ukur '
          'pilih = saham lain hari yang sama; bagi jumlah = semua saham sepanjang era. "Beza" = kelebihan dengan prasyarat tolak '
          'kelebihan syarat sahaja (mata peratus); positif = prasyarat menambah.', '']
    for kod in SKOR:
        b = bacaan[kod]
        Bm += [f'## Kayu ukur {nama_skor[kod]}', '',
               f"Median beza (P − S): {p(b['med_P'], 2, True)}; plasebo (PL − S): {p(b['med_PL'], 2, True)}; P > S bagi "
               f"{b['P_atas_S']} daripada {b['n']} pencetus; P > PL bagi {b['P_atas_PL']}. K3 sahaja: {p(b['med_P3'], 2, True)} lawan "
               f"plasebo {p(b['med_PL3'], 2, True)} ({b['n3']} pencetus).", '',
               '| Pencetus | Kelas | Syarat sahaja: penapis | lari % (rawak) · henti % | Dengan prasyarat: prasyarat | penapis | '
               'lari % (rawak) · henti % | Beza | Beza plasebo |', '|---' * 9 + '|']
        for r in M.itertuples():
            if not r.cukup_isyarat or g(r, f'{kod}_S_n') != g(r, f'{kod}_S_n'):
                continue
            sel = lambda kl: (f"{p(g(r, f'{kod}_{kl}_lari'))} ({p(g(r, f'{kod}_{kl}_asas'))}) · {p(g(r, f'{kod}_{kl}_gagal'))}"
                              if g(r, f'{kod}_{kl}_n') == g(r, f'{kod}_{kl}_n') and g(r, f'{kod}_{kl}_n') >= 100 else '–')
            dz = lambda kl: p(g(r, f'{kod}_{kl}_lebih') - g(r, f'{kod}_S_lebih'), 1, True) if sel(kl) != '–' and sel('S') != '–' else '–'
            Bm.append(f"| {pendek(r.nama)} | {'T' if r.kelas == 'IKUT TREND' else 'P'} | {txt(g(r, f'{kod}_S_penapis'))} | {sel('S')} | "
                      f"{txt(g(r, f'{kod}_P_prasyarat'))} | {txt(g(r, f'{kod}_P_penapis'))} | {sel('P')} | {dz('P')} | {dz('PL')} |")
        Bm.append('')
    tak = M[M.cukup_isyarat == 0]
    Bm += [f'Kelas: T = IKUT TREND, P = PANTULAN. "–" = kurang 100 belian pada kumpulan B. **Tidak cukup isyarat ({len(tak)}):** '
           + ', '.join(tak.pencetus) + '.', '']
    open(os.path.join(d, 'SEMUA_PENCETUS.md'), 'w', encoding='utf-8').write('\n'.join(Bm))
    cari.log('CS05 lapor siap: ' + json.dumps({k: bacaan[k] for k in SKOR}, default=float)[:600])


if __name__ == '__main__':
    arahan, kerja_ = sys.argv[1], sys.argv[2]
    {'besar': besar, 'plasebo': lambda k: besar(k, True), 'tepat': tepat, 'kunci': kunci, 'lapor': lapor_}[arahan](kerja_)
