"""Carian setup CS06 bahagian B — TALA bersama prasyarat (SPEC pindaan 14 Nov 2026 (k)).

Induk = setup papan CS06. Tiga paksi ditala serentak: varian pencetus (induk M: 24 varian ±25 %), ambang penapis saham
(grid pindaan (e)) dan ambang prasyarat (`cs_lapis.GRID_PRA`). Pilihan ikut DATARAN (median sel dan jirannya), pada
kumpulan A; induk dan anak kemudian dinilai pada kumpulan B.
Guna (CS_PUS=CS06; selepas cs_cs05.py tepat/kunci dan cs_lengkap.py pilih):
  python3 cs_tala6.py benih <kerja>    isyarat varian pencetus pada kumpulan A
  python3 cs_tala6.py tala  <kerja>    tala (A) + nilai induk dan anak (B) -> cs06_tala.pkl
  python3 cs_tala6.py lapor <kerja>    hasil/CS06/TALA.md, tala.csv, registry F (selepas cs_cs05.py lapor)"""
import json
import os
import pickle
import sys

import numpy as np
import pandas as pd

SINI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SINI)
import cs_atom as atom  # noqa: E402
import cs_cari as cari  # noqa: E402
import cs_cs05 as c5  # noqa: E402
import cs_lapis as lapis  # noqa: E402
import cs_lapor as lapor  # noqa: E402
import cs_lengkap as lg  # noqa: E402
import cs_tala as t4  # noqa: E402
import cs_tangkap as tk  # noqa: E402
import cs_teras as teras  # noqa: E402

N_VAR = 24
ASAL_PEN = {15: 70, 16: 90, 22: 4, 19: 30}           # ambang pradaftar penapis berambang (indeks PENAPIS)
NL = c5.NL


def varian(kerja):
    """(tugas, asal): 24 varian ±25 % bagi setiap pencetus induk berasaskan kaedah M (benih 20261113)."""
    S = pickle.load(open(os.path.join(kerja, f'{c5.AWALAN}_pilihan.pkl'), 'rb'))
    P, param0 = S['P'], S['meta']['besar']['param']
    pj = pd.read_csv(os.path.join(cari.AKAR, 'AUTOTUNE', 'kaedah', 'param_julat.csv'))
    pj = pj[pj.tala == 'Y']
    tugas, asal = [], {}
    for pc in sorted(set(P[P.peranan.str.startswith('papan_')].pencetus)):
        if not pc.startswith('M'):
            continue
        mid, v0 = pc.split('.')
        d = pj[pj.kaedah == mid]
        if not len(d):
            continue
        asas = param0.get(pc) or {x.nama: x.nilai_asal for x in d.itertuples()}
        for v in range(1, N_VAR + 1):
            rng = np.random.default_rng([atom.BENIH, 6, int(mid[1:]), int(v0), v])
            Pv = {}
            for x in d.itertuples():
                nilai = float(np.clip(asas.get(x.nama, x.nilai_asal) * rng.uniform(0.75, 1.25), x.bawah, x.atas))
                Pv[x.nama] = int(round(nilai)) if x.jenis == 'int' else nilai
            tugas.append((f'{pc}u{v}', mid, Pv))
            asal[f'{pc}u{v}'] = pc
    return tugas, asal


def dataran_n(G):
    """Markah dataran: median skor sel dan jirannya ±1 langkah pada setiap paksi (kotak 3^k); perlu sekurang-kurangnya
    separuh sel kotak (paling kurang 2) cukup isyarat. Tiada paksi ditala (kotak satu sel) -> skor sel itu sendiri."""
    D = np.full(G.shape, np.nan)
    for idx in np.ndindex(G.shape):
        if np.isnan(G[idx]):
            continue
        j = G[tuple(slice(max(i - 1, 0), i + 2) for i in idx)].ravel()
        ada = j[~np.isnan(j)]
        if len(j) == 1 or len(ada) >= max(2, int(np.ceil(len(j) / 2))):
            D[idx] = np.median(ada)
    return D


def skor_e(pan, X, e, aw):
    """Skor tepat CS06 bagi isyarat e (satu posisi setiap saham): min dua era [kelebihan sasaran - 2 ralat piawai]."""
    e = e[teras.satu_posisi(e, np.full(len(e), c5.TMAX - 1), pan['tid'])]
    tp = pan['tempoh'][e]
    s = np.inf
    for p in (0, 1):
        k = e[tp == p]
        if len(k) < c5.N_MIN:
            return np.nan
        s = min(s, float(tk.lb_lari(len(k), X[k, 4].mean(), X[k, aw + 4].mean())))
    return s


class Paksi:
    """Empat paksi satu induk: prasyarat pasaran, prasyarat kumpulan/syarikat, penapis 1, penapis 2."""

    def __init__(self, r):
        self.q = [(0, int(r.q1), lapis.PASARAN[r.q1][:4] if r.q1 >= 0 else None),
                  (1, int(r.q2), lapis.KUMPULAN[r.q2][:4] if r.q2 >= 0 else None)]
        self.f = [int(r.f1), int(r.f2)]
        self.grid = [lapis.GRID_PRA[kod][0] if kod in lapis.GRID_PRA else [None] for _, _, kod in self.q] + [
            t4.GRID[f][1] if f in t4.GRID else [None] for f in self.f]
        self.asal = [lapis.GRID_PRA[kod][1] if kod in lapis.GRID_PRA else None for _, _, kod in self.q] + [
            ASAL_PEN.get(f) for f in self.f]
        self.bentuk = tuple(len(g) for g in self.grid)
        self.ii = tuple(g.index(a) if a is not None else 0 for g, a in zip(self.grid, self.asal))

    def topeng_pra(self, k, x, set_, Lr, M, cache):
        lap, i, kod = self.q[k]
        if i < 0:
            return None
        if x is None:
            return Lr[lap][i] > 0
        if (kod, x, set_) not in cache:
            cache[(kod, x, set_)] = M.bar(set_, kod, x)
        return cache[(kod, x, set_)]

    def isyarat(self, pan, C, Lr, M, cache, set_, ev, amb):
        """Isyarat ev selepas prasyarat dan penapis pada ambang `amb` (4 nilai; None = takrif asal)."""
        for k in (0, 1):
            m = self.topeng_pra(k, amb[k], set_, Lr, M, cache)
            if m is not None:
                ev = ev[m[ev]]
        for k in (0, 1):
            ev = ev[t4.topeng(pan, C, ev, self.f[k], amb[2 + k])]
        return ev

    def teks(self, amb):
        pra = [(kod, lapis.GRID_PRA[kod][2].format(f'{x:g}') if x is not None else (
            lapis.PASARAN if lap == 0 else lapis.KUMPULAN)[i][5:], x) for (lap, i, kod), x in zip(self.q, amb[:2]) if i >= 0]
        pen = [(atom.PENAPIS[f][:3], t4.GRID[f][2].format(x) if x is not None else atom.PENAPIS[f][4:], x)
               for f, x in zip(self.f, amb[2:]) if f >= 0]
        kodkan = lambda b, asal: '+'.join(k if x is None else f'{k}@{x:g}' for k, _, x in b) or asal
        return {'prasyarat': ' + '.join(t for _, t, _ in pra) or 'tiada', 'syarat': ' + '.join(t for _, t, _ in pen) or 'tiada',
                'penapis': ' DAN '.join(t for _, t, _ in pen) or 'tiada', 'kod_pra': kodkan(pra, ''), 'kod_pen': kodkan(pen, '-')}


def tala(kerja):
    S = pickle.load(open(os.path.join(kerja, f'{c5.AWALAN}_pilihan.pkl'), 'rb'))
    P = S['P']
    induk = P[P.peranan.str.startswith('papan_')]
    tugas, asal = varian(kerja)
    M = lapis.Mentah(kerja)
    cari.log('semak ciri mentah lawan lapisan (i): ' + str(sum(M.semak().values())) + ' bar berbeza')
    cache, out = {}, []
    # ---------- kumpulan A: pilih anak ikut dataran ----------
    pan, bn, EV, X, L = c5._sedia(kerja, 'A')
    C, Lr, Tb = t4.ciri(pan), (L['L1'], L['L2']), lg.muat_asas(kerja, 'A')
    f = os.path.join(kerja, 'benih_A_tala6.pkl')
    tl = pickle.load(open(f, 'rb'))['sig'] if os.path.exists(f) else {}
    TA = [t[0] for t in atom.TEMPOH['A']]
    for k, r in zip(induk.index, induk.itertuples()):
        kod = r.peranan.split('_')[1]
        aw = NL if kod == 'pilih' else 2 * NL
        pk = Paksi(r)
        calon = {r.pencetus: EV[r.pencetus]}
        calon.update({n: t4.isyarat(pan, tl[n]) for n, p0 in asal.items() if p0 == r.pencetus and n in tl})
        terbaik, induk_sel, sel = None, (np.nan, np.nan), 0
        for nama, ev in calon.items():
            G = np.full(pk.bentuk, np.nan)
            for i0, a0 in enumerate(pk.grid[0]):
                m = pk.topeng_pra(0, a0, 'A', Lr, M, cache)
                e0 = ev if m is None else ev[m[ev]]
                for i1, a1 in enumerate(pk.grid[1]):
                    m = pk.topeng_pra(1, a1, 'A', Lr, M, cache)
                    e1 = e0 if m is None else e0[m[e0]]
                    for i2, a2 in enumerate(pk.grid[2]):
                        e2 = e1[t4.topeng(pan, C, e1, pk.f[0], a2)]
                        for i3, a3 in enumerate(pk.grid[3]):
                            G[i0, i1, i2, i3] = skor_e(pan, X, e2[t4.topeng(pan, C, e2, pk.f[1], a3)], aw)
            sel += int(np.isfinite(G).sum())
            D = dataran_n(G)
            if nama == r.pencetus:
                induk_sel = (float(G[pk.ii]), float(D[pk.ii]))
            if np.isnan(D).all():
                continue
            ij = np.unravel_index(np.nanargmax(D), D.shape)
            if terbaik is None or D[ij] > terbaik['dataran']:
                terbaik = {'pencetus': nama, 'ij': tuple(int(x) for x in ij), 'skor': float(G[ij]), 'dataran': float(D[ij])}
        if terbaik is None:
            terbaik = {'pencetus': r.pencetus, 'ij': pk.ii, 'skor': induk_sel[0], 'dataran': induk_sel[1]}
        kekal = terbaik['pencetus'] == r.pencetus and terbaik['ij'] == pk.ii
        amb = tuple(g[i] for g, i in zip(pk.grid, terbaik['ij']))
        amb_i = tuple(g[i] for g, i in zip(pk.grid, pk.ii))
        eA = pk.isyarat(pan, C, Lr, M, cache, 'A', calon[terbaik['pencetus']], amb)
        lajur = lg.pilih_lajur(pan, eA, X[eA, 0] > 0)
        d = {'k': k, 'kod': kod, 'pc_induk': r.pencetus, 'q1': int(r.q1), 'q2': int(r.q2), 'f1': int(r.f1), 'f2': int(r.f2),
             'kekal': bool(kekal), 'calon': len(calon), 'sel': sel, 'skor_induk': induk_sel[0], 'dataran_induk': induk_sel[1],
             'amb': amb, 'amb_induk': amb_i, 'lajur': lajur, **terbaik,
             'VA': dict(zip(TA, c5.kadar_e(pan, X, eA).values())),
             'LA': {n: dict(zip(TA, lg.nilai_l(pan, X, eA, col, Tb).values()))
                    for n, col in (('pilih', lajur), ('x00', (lajur // lg.NR) * lg.NR))} if lajur >= 0 else {}}
        out.append(d)
        cari.log(f"{r.pencetus} [{kod}]: {len(calon)} calon, {sel} sel; induk dataran {induk_sel[1] * 100:+.2f} -> anak "
                 f"{terbaik['dataran'] * 100:+.2f} ({terbaik['pencetus']}, ambang {amb})" + (' [induk kekal]' if kekal else ''))
    del pan, EV, X, L, C, Tb
    # ---------- kumpulan B: induk dan anak ----------
    pan, bnB, EV, X, L = c5._sedia(kerja, 'B')
    C, Lr, Tb = t4.ciri(pan), (L['L1'], L['L2']), lg.muat_asas(kerja, 'B')
    perlu = {d['pencetus'] for d in out if 'u' in d['pencetus'].split('.')[-1]}
    tlB = cari.benih(kerja, 'B', tugas=[t for t in tugas if t[0] in perlu], fail='benih_B_tala6.pkl')['sig'] if perlu else {}
    TB = [t[0] for t in atom.TEMPOH['B']]
    for d, r in zip(out, induk.itertuples()):
        pk = Paksi(r)
        ev = EV.get(d['pencetus']) if d['pencetus'] in EV else (
            t4.isyarat(pan, tlB[d['pencetus']]) if d['pencetus'] in tlB else None)
        if ev is None:
            continue
        eB = pk.isyarat(pan, C, Lr, M, cache, 'B', ev, d['amb'])
        d['VB'] = dict(zip(TB, c5.kadar_e(pan, X, eB).values()))
        if d['lajur'] >= 0:
            for n, col in (('pilih', d['lajur']), ('x00', (d['lajur'] // lg.NR) * lg.NR)):
                d['LA'][n].update(zip(TB, lg.nilai_l(pan, X, eB, col, Tb).values()))
        eI = pk.isyarat(pan, C, Lr, M, cache, 'B', EV[r.pencetus], d['amb_induk'])          # induk, laluan kod yang sama
        d['VB_induk'] = dict(zip(TB, c5.kadar_e(pan, X, eI).values()))
    param = {n: Pv for n, _, Pv in tugas}
    pickle.dump({'tala': out, 'param': param}, open(os.path.join(kerja, f'{c5.AWALAN}_tala.pkl'), 'wb'), protocol=4)
    cari.log(f"tala siap: {len(out)} induk; {sum(not d['kekal'] for d in out)} anak berbeza daripada induk")


def lapor_(kerja):
    S = pickle.load(open(os.path.join(kerja, f'{c5.AWALAN}_pilihan.pkl'), 'rb'))
    KV = pickle.load(open(os.path.join(kerja, f'{c5.AWALAN}_kunci.pkl'), 'rb'))
    T = pickle.load(open(os.path.join(kerja, f'{c5.AWALAN}_tala.pkl'), 'rb'))
    P = S['P']
    param = {**S['meta']['besar']['param'], **T['param']}
    TK = [t[0] for t in atom.TEMPOH['B']]
    d_ = c5.KELUAR_UJI or os.path.join(SINI, 'hasil', c5.PUS)
    reg = pd.read_csv(os.path.join(c5.KELUAR_UJI, 'registry_F.csv') if c5.KELUAR_UJI else lapor.REG_F, dtype=str).fillna('')
    masuk_ = lambda t: (t.split('|')[0], t.split('|')[1], '|'.join(t.split('|')[4:]))
    p = lambda x, k=1, t=False: '–' if x is None or x != x else (f'{x * 100:+.{k}f}' if t else f'{x * 100:.{k}f}')
    baris, daftar_b = [], {}
    for i, d in enumerate(T['tala']):
        r = P.loc[d['k']]
        aw = c5.ASAS[d['kod']]
        pk = Paksi(r)
        kunci_i = (r.pencetus, '+'.join(atom.PENAPIS[f][:3] for f in (r.f1, r.f2) if f >= 0) or '-', c5.tk_pra(r.q1, r.q2, kod=True))
        idi = reg[reg.takrif.map(lambda t: masuk_(t) == kunci_i)].id
        vi, va = d.get('VB_induk') or KV['V'][d['k']], d.get('VB', {})          # induk: laluan kod yang sama dengan anak
        kl = lambda v, T_: c5.lebih(v, T_, aw) if v else np.nan
        tx = pk.teks(d['amb'])
        b = {'induk': idi.iloc[0] if len(idi) else '?', 'kayu_ukur': d['kod'], 'kekal': d['kekal'], 'calon_pencetus': d['calon'],
             'sel_diskor': d['sel'], 'pencetus_induk': r.pencetus, 'pencetus_anak': d['pencetus'],
             'prasyarat_induk': pk.teks(d['amb_induk'])['prasyarat'], 'syarat_induk': pk.teks(d['amb_induk'])['syarat'],
             'prasyarat_anak': tx['prasyarat'], 'syarat_anak': tx['syarat'],
             'dataran_induk': d['dataran_induk'], 'dataran_anak': d['dataran'], 'skor_induk': d['skor_induk'], 'skor_anak': d['skor'],
             'n_induk': c5.gab(vi, TK, 'lari')[0], 'tpp_induk': c5.gab(vi, TK, 'lari')[1], 'asas_induk': c5.gab(vi, TK, aw + 'lari')[1],
             'lebih_induk': kl(vi, TK), 'lebih_induk_K3': kl(vi, ['K3']), 'gagal_induk': c5.gab(vi, TK, 'gagal')[1],
             'n_anak': c5.gab(va, TK, 'lari')[0], 'tpp_anak': c5.gab(va, TK, 'lari')[1], 'asas_anak': c5.gab(va, TK, aw + 'lari')[1],
             'lebih_anak': kl(va, TK), 'lebih_anak_K3': kl(va, ['K3']), 'gagal_anak': c5.gab(va, TK, 'gagal')[1],
             'n_anak_K3': va.get('K3', {}).get('n', 0)}
        b['anak_menang'] = bool(b['lebih_anak'] > b['lebih_induk'])
        b['anak_menang_K3'] = bool(b['lebih_anak_K3'] > b['lebih_induk_K3'])
        if not d['kekal'] and d['lajur'] >= 0 and va:
            LA = d['LA']['pilih']
            b.update(keluar_anak=c5.kod_keluar(d['lajur']), tp_anak=c5.gab(LA, TK, 'tp')[1], asas_tp_anak=c5.gab(LA, TK, aw + 'tp')[1],
                     rugi8_anak=c5.gab(LA, TK, 'rugi8')[1], pegang_anak=c5.gab(LA, TK, 'pegang')[1],
                     menang_anak=c5.gab(LA, TK, 'menang')[1], purata_anak=c5.gab(LA, TK, 'purata')[1],
                     **{f'menang_anak_{t}': LA.get(t, {}).get('menang', np.nan) for t in TK})
            s, x = divmod(int(d['lajur']), cari.NR)
            takrif = f"{d['pencetus']}|{tx['kod_pen']}|{atom.HENTI[s][:2]}|{c5.kod_keluar(d['lajur']).split(' · ')[1]}"
            takrif += ('|' + tx['kod_pra']) if tx['kod_pra'] else ''
            TA = [t[0] for t in atom.TEMPOH['A']]
            v0 = {t: {'n': 0, **LA.get(t, {})} for t in TA + TK}
            db = dict(_pencetus=d['pencetus'], takrif=takrif, masuk=lapor.nama_pencetus(d['pencetus'], param),
                      penapis=tx['penapis'], henti=atom.HENTI[s], keluar=teras.nama_keluar(x, cari.A1, cari.A2, cari.OP, atom.KELUAR),
                      skor_tepat=f"{d['skor']:.5f}", T1='', T2='', T3='', prasyarat=tx['prasyarat'], syarat=tx['syarat'])
            for j, t in enumerate(TA, 1):
                db[f'n_cari{j}'] = v0[t]['n']
                db[f'purata_cari{j}'] = '' if not v0[t]['n'] else f"{v0[t]['purata']:.5f}"
            for t in TK:
                db[f'n_{t}'] = v0[t]['n']
                db[f'purata_{t}'] = '' if not v0[t]['n'] else f"{v0[t]['purata']:.5f}"
                db[f'k10_{t}'] = '' if not v0[t]['n'] else f"{v0[t]['k10']:.4f}"
                db[f'menang_{t}'] = '' if not v0[t]['n'] else f"{v0[t]['menang']:.4f}"
            db['menang'] = f"{b['menang_anak']:.4f}" if b['menang_anak'] == b['menang_anak'] else ''
            daftar_b[i] = db
        baris.append(b)
    idf = c5.daftar(daftar_b, param) if daftar_b else {}
    for i, b in enumerate(baris):
        b['anak'] = idf.get(i, b['induk'] if b['kekal'] else '')
    Tt = pd.DataFrame(baris)
    Tt.to_csv(os.path.join(d_, 'tala.csv'), index=False, float_format='%.5f')
    A_ = Tt[~Tt.kekal & (Tt.n_anak >= 100)]
    A3 = A_[A_.n_anak_K3 >= 30]
    menang, menang3 = int(A_.anak_menang.sum()), int(A3.anak_menang_K3.sum())
    kedua = int((A_.anak_menang & A_.anak_menang_K3 & (A_.n_anak_K3 >= 30)).sum())
    menolong = bool(len(A_) and kedua > len(A_) / 2)
    try:
        sys.path.insert(0, os.path.join(lapor.BS2, 'standard'))
        import status_kad
        status = status_kad.baris()
    except Exception:
        status = '> **Status keputusan:** lihat `laporan/KAD_SKOR.md`; laporan ini BUKAN keputusan.'
    A = [f'# {c5.PUS}: tala bersama prasyarat — induk lawan anak pada saham yang tidak dilihat (backtest, BUKAN bukti)', '', status, '',
         'Dijana `kajian/carian_setup/cs_tala6.py`. Pradaftar: `kajian/SPEC_CARIAN_SETUP.md` pindaan 14 Nov 2026 (k) bahagian B. '
         '**Jangan sunting secara manual.**', '',
         'Induk = setup papan CS06. Tiga paksi ditala serentak pada kumpulan A: varian pencetus (induk kaedah M: 24 varian ±25 %), '
         'ambang penapis saham dan ambang prasyarat. Anak = sel dengan markah DATARAN tertinggi (median sel dan jirannya), bukan '
         'puncak. Angka di bawah daripada **kumpulan B**; "lebih" = kadar tangkap penuh tolak saham rawak (kayu ukur papan induk), '
         'mata peratus.', '',
         f"**Bacaan dikunci:** tala menolong hanya jika lebih separuh anak mengatasi induknya pada kumpulan B DAN pada K3. "
         f"Daripada {len(Tt)} induk, {int(Tt.kekal.sum())} kekal (sel induk sendiri yang terbaik) dan {len(A_)} mendapat anak yang "
         f"cukup belian. Anak mengatasi induk pada kumpulan B: {menang} daripada {len(A_)}; pada K3: {menang3} daripada {len(A3)}; "
         f"kedua-duanya: {kedua} daripada {len(A_)}. **Tala menolong: {'YA' if menolong else 'TIDAK'}.**", '',
         '| Induk | Kayu ukur | Anak | Apa yang berubah | Induk: tangkap penuh % (rawak) · lebih · lebih K3 · kena henti % | '
         'Anak: tangkap penuh % (rawak) · lebih · lebih K3 · kena henti % | Belian anak | Anak > induk (B / K3) |', '|---' * 8 + '|']
    ya = lambda x: '✓' if x else '✗'
    for b in Tt.itertuples():
        if b.kekal:
            A.append(f'| `{b.induk}` | {b.kayu_ukur} | – | induk kekal ({b.calon_pencetus} calon pencetus, {b.sel_diskor:,} sel) | '
                     f'{p(b.tpp_induk)} ({p(b.asas_induk)}) · {p(b.lebih_induk, 1, True)} · {p(b.lebih_induk_K3, 1, True)} · '
                     f'{p(b.gagal_induk)} | – | – | – |')
            continue
        ubah = []
        if b.pencetus_anak != b.pencetus_induk:
            ubah.append(f'parameter pencetus ditala (`{b.pencetus_anak}`)')
        if b.prasyarat_anak != b.prasyarat_induk:
            ubah.append(f'prasyarat: {b.prasyarat_induk} → {b.prasyarat_anak}')
        if b.syarat_anak != b.syarat_induk:
            ubah.append(f'penapis: {b.syarat_induk} → {b.syarat_anak}')
        A.append(f"| `{b.induk}` | {b.kayu_ukur} | `{b.anak}` | {'; '.join(ubah)} | "
                 f'{p(b.tpp_induk)} ({p(b.asas_induk)}) · {p(b.lebih_induk, 1, True)} · {p(b.lebih_induk_K3, 1, True)} · '
                 f'{p(b.gagal_induk)} | {p(b.tpp_anak)} ({p(b.asas_anak)}) · {p(b.lebih_anak, 1, True)} · '
                 f'{p(b.lebih_anak_K3, 1, True)} · {p(b.gagal_anak)} | {int(b.n_anak):,} | {ya(b.anak_menang)} / {ya(b.anak_menang_K3)} |')
    ada = Tt[~Tt.kekal & Tt.get('tp_anak', pd.Series(np.nan, index=Tt.index)).notna()]
    if len(ada):
        A += ['', 'Setup lengkap anak (henti × keluar dipilih ikut tangkap penuh sendiri, pindaan (k); kumpulan B):', '',
              '| Anak | Henti · keluar | Tangkap penuh % (rawak) | Rugi ≥ 8 % % | Pegang (sesi) | Menang % | Purata setiap dagangan % |',
              '|---' * 7 + '|']
        for b in ada.itertuples():
            A.append(f'| `{b.anak}` | {b.keluar_anak} | {p(b.tp_anak)} ({p(b.asas_tp_anak)}) | {p(b.rugi8_anak)} | {b.pegang_anak:.1f} | '
                     f'{p(b.menang_anak, 0)} | {p(b.purata_anak, 2, True)} |')
    A += ['', '## Kaveat', '',
          '- Tala dijalankan pada kumpulan A sahaja; kumpulan B hanya mengukur. Tetapi reka bentuk CS06 dipilih selepas hasil CS05 '
          'pada kumpulan B dilihat, jadi kumpulan B bukan lagi "tidak dilihat" bagi keluarga setup ini.',
          '- Setiap induk mempunyai ratusan hingga ribuan sel; yang terbaik sebahagiannya nasib walaupun dengan dataran. '
          'Belian anak pada K3 selalunya sedikit.',
          '- Anak didaftarkan dalam keluarga F (status BACKTEST). Tiada setup masuk jejak hadapan (keputusan pengguna 14 Nov 2026).', '']
    open(os.path.join(d_, 'TALA.md'), 'w', encoding='utf-8').write('\n'.join(A))
    json.dump({'induk': len(Tt), 'kekal': int(Tt.kekal.sum()), 'anak': len(A_), 'anak_menang_B': menang, 'anak_K3': len(A3),
               'anak_menang_K3': menang3, 'anak_menang_kedua': kedua, 'tala_menolong': menolong},
              open(os.path.join(d_, 'tala_meta.json'), 'w'), indent=1)
    cari.log(f'tala lapor: {len(Tt)} induk, {int(Tt.kekal.sum())} kekal, anak menang B {menang}/{len(A_)}, K3 {menang3}/{len(A3)}, '
             f'kedua {kedua}; menolong={menolong}')


if __name__ == '__main__':
    if sys.argv[1] == 'benih':
        tg, _ = varian(sys.argv[2])
        cari.benih(sys.argv[2], 'A', tugas=tg, fail='benih_A_tala6.pkl')
    else:
        {'tala': tala, 'lapor': lapor_}[sys.argv[1]](sys.argv[2])
