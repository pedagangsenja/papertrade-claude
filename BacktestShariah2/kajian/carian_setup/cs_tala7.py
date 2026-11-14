"""Carian setup — pusingan CS07 bahagian (a): tala parameter masuk SEMUA kaedah (SPEC pindaan 14 Nov 2026 (n)).

Kaedah M: varian rawak julat penuh (v3-v10) dan varian setempat ±25 %; indikator dan kaedah N: keluarga berparameter K01-K25
(`cs_param.py`). Setiap varian diskor dengan enjin (i) pada kumpulan A, sasaran `terus`; kumpulan B untuk laporan sahaja.
Guna: python3 cs_tala7.py benih1|keluarga|skor|benih2|skor2|pilih|kunci|lapor <kerja>
Fail kerja berawalan cs07_. Jangan sunting keluaran secara manual."""
import os
import pickle
import sys

import numpy as np
import pandas as pd

SINI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SINI)
import multiprocessing as mp  # noqa: E402
import time  # noqa: E402

import cs_akhir as ak  # noqa: E402
import cs_atom as atom  # noqa: E402
import cs_cari as cari  # noqa: E402
import cs_cs05 as c5  # noqa: E402
import cs_lapis as lapis  # noqa: E402
import cs_param as kp  # noqa: E402

V_RAWAK = tuple(range(3, 11))          # 8 varian rawak julat penuh setiap kaedah M (v1, v2 sudah ada dalam benih asal)
N_M_SETEMPAT, N_SETEMPAT = 50, 8       # 50 kaedah M teratas x 8 varian setempat ±25 %
FAIL_M = 'benih_{}_cs07.pkl'


def _pj():
    pj = pd.read_csv(os.path.join(cari.AKAR, 'AUTOTUNE', 'kaedah', 'param_julat.csv'))
    return pj[pj.tala == 'Y']


def varian_m1():
    """Tugas (nama, modul, P): varian rawak v3-v10 bagi setiap kaedah M yang ada parameter boleh tala."""
    pj = pd.read_csv(os.path.join(cari.AKAR, 'AUTOTUNE', 'kaedah', 'param_julat.csv'))
    tugas = []
    for mid in sorted({t[1] for t in cari.senarai_benih() if t[1].startswith('M')}):
        for v in V_RAWAK:
            P = cari.param_varian(pj, mid, v)
            if P:
                tugas.append((f'{mid}.{v}', mid, P))
    return tugas


def varian_m2(terbaik, param):
    """Varian setempat: terbaik = {mid: nama varian terbaik}; param = {nama: dict parameter atau None (lalai)}."""
    pj = _pj()
    tugas, asal = [], {}
    for mid, nama in sorted(terbaik.items()):
        d = pj[pj.kaedah == mid]
        asas = param.get(nama) or {x.nama: x.nilai_asal for x in d.itertuples()}
        for v in range(1, N_SETEMPAT + 1):
            rng = np.random.default_rng([atom.BENIH, 7, int(mid[1:]), v])
            Pv = {}
            for x in d.itertuples():
                nilai = float(np.clip(asas.get(x.nama, x.nilai_asal) * rng.uniform(0.75, 1.25), x.bawah, x.atas))
                Pv[x.nama] = int(round(nilai)) if x.jenis == 'int' else nilai
            tugas.append((f'{nama}s{v}', mid, Pv))
            asal[f'{nama}s{v}'] = nama
    return tugas, asal


# ---------- keluarga K: isyarat (hari pertama, layak) setiap varian ----------
_W = {}


def _k_satu(julat):
    a, b = julat
    G, out = _W['G'], [[] for _ in _W['G']]
    for ti in range(a, b):
        g = _W['fr'][_W['tick'][ti]]
        m0, m1 = int(_W['mula'][ti]), int(_W['mula'][ti + 1])
        assert len(g) == m1 - m0, _W['tick'][ti]
        M = kp.kira(g, _W['RS'][_W['tick'][ti]].reindex(g.index), G)
        dulu = np.zeros_like(M)
        dulu[:, 1:] = M[:, :-1]
        M &= ~dulu
        M &= _W['sah'][m0:m1][None, :]
        for i in range(len(G)):
            ix = np.flatnonzero(M[i])
            if len(ix):
                out[i].append((ix + m0).astype(np.int32))
    return out


def keluarga(kerja, set_):
    """Isyarat keluarga K pada set (A/B): cs07_K_<set>.pkl = {'ev': {nama: indeks bar}, 'grid': [...]}."""
    f = os.path.join(kerja, f'cs07_K_{set_}.pkl')
    if os.path.exists(f):
        return pickle.load(open(f, 'rb'))
    pan = cari.panel(kerja, set_)
    fr, _, _ = cari.muat_set(set_)
    tick = sorted(fr)
    assert list(pan['ticker']) == tick
    px = pd.DataFrame({t: fr[t].close for t in tick})
    G = kp.grid()
    _W.update(G=G, fr=fr, tick=tick, mula=pan['mula'], sah=pan['sah'], RS=(px / px.shift(126) - 1).rank(axis=1, pct=True) * 100)
    julat = [(a, min(a + 25, len(tick))) for a in range(0, len(tick), 25)]
    t0, bah = time.time(), [[] for _ in G]
    with mp.get_context('fork').Pool(cari.PEKERJA) as pool:
        for k, out in enumerate(pool.imap(_k_satu, julat), 1):
            for i, x in enumerate(out):
                bah[i] += x
            if k % 20 == 0:
                cari.log(f'  keluarga {set_}: {k}/{len(julat)} · {time.time() - t0:.0f}s')
    ev = {G[i][0]: (np.sort(np.concatenate(x)) if x else np.zeros(0, np.int32)) for i, x in enumerate(bah)}
    out = {'ev': ev, 'grid': G}
    pickle.dump(out, open(f, 'wb'), protocol=4)
    cari.log(f"keluarga {set_}: {len(G)} varian, {sum(len(v) for v in ev.values()):,} isyarat, {time.time() - t0:.0f}s")
    return out


# ---------- label sasaran `terus` + skor enjin (i) ----------
def label_terus(pan):
    """V[bar] = (terus, asas hari sama x tercile ATR %, asas era x tercile); Lb = [m10, terus, puncak] bagi bar sah."""
    sah = np.flatnonzero(pan['sah'])
    Lb = ak.label2(sah, pan['o'], pan['l'], pan['c'])
    hari = pan['hari'][sah]
    pct = pd.Series(pan['atr'][sah] / pan['c'][sah]).groupby(hari).rank(pct=True).to_numpy()
    terc = np.minimum((pct * 3).astype(np.int64), 2)
    V = np.zeros((len(pan['c']), 3))
    V[sah, 0] = Lb[:, 1]
    for a, g in ((1, hari * 3 + terc), (2, pan['tempoh'][sah].astype(np.int64) * 3 + terc)):
        V[sah, a] = (np.bincount(g, Lb[:, 1]) / np.maximum(np.bincount(g), 1))[g]
    return V


def semua_ev(kerja, set_, bahagian):
    """dict nama -> indeks bar isyarat bagi satu bahagian: asal | K | M1 | M2."""
    pan = cari.panel(kerja, set_)
    if bahagian == 'asal':
        return cari.pencetus(pan, pickle.load(open(os.path.join(kerja, f'benih_{set_}.pkl'), 'rb')))
    if bahagian == 'K':
        return keluarga(kerja, set_)['ev']
    bn = pickle.load(open(os.path.join(kerja, FAIL_M.format(set_)), 'rb'))
    N = len(pan['c'])
    mula = lambda bit: np.flatnonzero(atom.mula_isyarat(np.unpackbits(bit)[:N].astype(bool), pan['mula']) & pan['sah'])
    ya = (lambda n: 's' in n) if bahagian == 'M2' else (lambda n: 's' not in n)
    return {n: mula(bit) for n, bit in bn['sig'].items() if ya(n)}


def _skor_satu(nama):
    pan, ev = c5._G['pan'], c5._G['ev'][nama]
    tp = pan['tempoh'][ev].astype(np.int64)
    out = {'n_ev': (int((tp == 0).sum()), int((tp == 1).sum()))}
    if min(out['n_ev']) < c5.N_MIN:
        return nama, dict(out, cukup=False)
    V = np.ascontiguousarray(c5._G['V'][ev])
    Acc = np.zeros((c5.NQ, c5.NC, 2, 4))
    c5.kumpul5(tp, V, np.ascontiguousarray(c5._G['FS'][:, ev].T), np.ascontiguousarray(c5._G['L1'][:, ev].T),
               np.ascontiguousarray(c5._G['L2'][:, ev].T), c5.PASANG, Acc)
    ok, sp, sj = c5.skor_acc(Acc)
    sm = np.where(ok, sp, -np.inf)
    a0 = Acc[0, 0]                                                # pencetus sahaja
    with np.errstate(divide='ignore', invalid='ignore'):
        out.update(cukup=True, n_ok=int(ok.sum()), atas=c5._atas(sm, 5), atas_S=c5._atas(sm[:1], 5),
                   mentah=(a0[:, 1] / a0[:, 0]).tolist(), mentah_asas=(a0[:, 2] / a0[:, 0]).tolist(),
                   skor0=float(sp[0, 0]) if ok[0, 0] else np.nan)
    return nama, out


def skor(kerja, bahagian):
    """Skor setiap pencetus bahagian itu pada kumpulan A (sasaran `terus`): cs07_skor_<bahagian>.pkl."""
    f = os.path.join(kerja, f'cs07_skor_{bahagian}.pkl')
    siap = pickle.load(open(f, 'rb')) if os.path.exists(f) else {}
    pan = cari.panel(kerja, 'A')
    ev = semua_ev(kerja, 'A', bahagian)
    tugas = sorted([n for n in ev if n not in siap], key=lambda n: -len(ev[n]))
    if not tugas:
        return siap
    L = lapis.muat(kerja, 'A')
    c5._G.update(pan=pan, ev=ev, V=label_terus(pan), FS=np.ascontiguousarray(pan['F'][c5.SAHAM]), L1=L['L1'], L2=L['L2'])
    c5.kumpul5(np.zeros(1, np.int64), np.zeros((1, 3)), np.zeros((1, c5.NS), np.uint8), np.zeros((1, lapis.N1), np.uint8),
               np.zeros((1, lapis.N2), np.uint8), c5.PASANG, np.zeros((c5.NQ, c5.NC, 2, 4)))       # kompil sebelum fork
    cari.log(f'skor {bahagian}: {len(tugas)} pencetus (siap {len(siap)})')
    t0 = time.time()
    with mp.get_context('fork').Pool(cari.PEKERJA) as pool:
        for k, (n, r) in enumerate(pool.imap_unordered(_skor_satu, tugas), 1):
            siap[n] = r
            if k % 100 == 0:
                cari.log(f'  {k}/{len(tugas)} · {time.time() - t0:.0f}s')
                pickle.dump(siap, open(f + '.tmp', 'wb'), protocol=4)
                os.replace(f + '.tmp', f)
    pickle.dump(siap, open(f, 'wb'), protocol=4)
    cari.log(f"skor {bahagian} siap: {sum(1 for r in siap.values() if r.get('cukup'))} cukup isyarat daripada {len(siap)}; "
             f'{time.time() - t0:.0f}s')
    return siap


def benih1(kerja, set_='A', hanya=None):
    tugas = varian_m1()
    cari.log(f'CS07 benih1 {set_}: {len(tugas)} varian M')
    return cari.benih(kerja, set_, hanya=hanya, tugas=tugas, fail=FAIL_M.format(set_))


if __name__ == '__main__':
    cmd, kerja = sys.argv[1], sys.argv[2]
    if cmd == 'benih1':
        b = benih1(kerja)
        pickle.dump({'siap': len(b['sig']), 'ralat': len(b['ralat'])}, open(os.path.join(kerja, 'cs07_benih1.siap'), 'wb'))
    elif cmd == 'keluarga':
        keluarga(kerja, sys.argv[3] if len(sys.argv) > 3 else 'A')
    elif cmd == 'skor':
        skor(kerja, sys.argv[3])
    else:
        raise SystemExit(f'arahan tidak dikenali: {cmd}')
