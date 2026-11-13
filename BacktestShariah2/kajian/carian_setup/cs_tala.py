"""Carian setup CS04 — tala parameter di sekitar pemenang CS03 (SPEC pindaan 13 Nov 2026 (e)).
Guna: python3 cs_tala.py <kerja>   (folder kerja CS02/CS03). Keluaran: hasil/CS04/, kajian/CARIAN_SETUP.md, registry F."""
import itertools
import json
import os
import pickle
import sys
from types import SimpleNamespace

import numpy as np
import pandas as pd

SINI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SINI)
import cs_atom as atom  # noqa: E402
import cs_cari as cari  # noqa: E402
import cs_lapor as lapor  # noqa: E402
import cs_tangkap as tk  # noqa: E402
import cs_teras as teras  # noqa: E402

PUS, INDUK_PUS, N_VAR = 'CS04', 'CS03', 24
# indeks penapis (0 = F01) -> (ciri, grid ambang, teks)
GRID = {15: ('rs', [50, 60, 70, 80, 90, 95], 'RS >= {}'), 16: ('rs', [50, 60, 70, 80, 90, 95], 'RS >= {}'),
        22: ('atrp', [2, 3, 4, 5, 6, 8], 'ATR% >= {}'),
        19: ('jatuh', [20, 30, 40, 50, 60], '>= {}% di bawah puncak 52 minggu')}


def ciri(pan):
    """Ciri mentah bagi ambang penapis: RS (pangkat peratus pulangan 126 hari), ATR %, % di bawah puncak 52 minggu."""
    c, h, mula = pan['c'], pan['h'], pan['mula']
    r126 = np.full(len(c), np.nan)
    h252 = np.full(len(c), np.nan)
    for t in range(len(mula) - 1):
        a, b = mula[t], mula[t + 1]
        cs = pd.Series(c[a:b])
        r126[a:b] = (cs / cs.shift(126) - 1).to_numpy()
        h252[a:b] = pd.Series(h[a:b]).rolling(252).max().to_numpy()
    rs = pd.Series(r126).groupby(pan['hari']).rank(pct=True).to_numpy() * 100
    return {'rs': rs, 'atrp': pan['atr'] / c * 100, 'jatuh': (1 - c / h252) * 100}


def topeng(pan, C, ev, f, x):
    """Topeng penapis f pada isyarat ev; x = ambang (None = penapis asal)."""
    if f < 0:
        return np.ones(len(ev), bool)
    if x is None or f not in GRID:
        return pan['F'][f, ev] > 0
    return C[GRID[f][0]][ev] >= x


def kadar(pan, X, e):
    e = e[teras.satu_posisi(e, np.full(len(e), tk.TMAX - 1), pan['tid'])]
    tp = pan['tempoh'][e]
    out = {}
    for p in range(int(pan['tempoh'].max()) + 1):
        x = X[e[tp == p]]
        d = {'n': len(x)}
        for j, nama in enumerate(tk.LABEL):
            d[nama] = float(x[:, j].mean()) if len(x) else np.nan
            d['a_' + nama] = float(x[:, tk.NL + j].mean()) if len(x) else np.nan
        out[p] = d
    return out


def dataran(G):
    """Median skor sel dan jirannya (3 x 3, atau 3 sebaris jika satu paksi tunggal)."""
    D = np.full(G.shape, np.nan)
    perlu = 4 if min(G.shape) > 1 else 2
    for a, b in itertools.product(range(G.shape[0]), range(G.shape[1])):
        j = G[max(a - 1, 0):a + 2, max(b - 1, 0):b + 2].ravel()
        j = j[~np.isnan(j)]
        if not np.isnan(G[a, b]) and len(j) >= perlu:
            D[a, b] = np.median(j)
    return D


def gab(v, T, nama):
    n = sum(v[t]['n'] for t in T)
    return n, (sum(v[t]['n'] * v[t][nama] for t in T if v[t]['n']) / n if n else np.nan)


def lebih(v, T, nama='lari'):
    return gab(v, T, nama)[1] - gab(v, T, 'a_' + nama)[1]


def isyarat(pan, bit):
    s = np.unpackbits(bit)[:len(pan['c'])].astype(bool) if bit.dtype == np.uint8 and len(bit) != len(pan['c']) else bit
    return np.flatnonzero(atom.mula_isyarat(s, pan['mula']) & pan['sah'])


def main(kerja):
    cari_set, kunci_set = cari.PUSINGAN[PUS]
    T_cari, T_kunci = lapor.tempoh(PUS)
    reg = pd.read_csv(lapor.REG_F, dtype=str).fillna('')
    induk = reg[reg.pusingan == INDUK_PUS]
    pj = pd.read_csv(os.path.join(cari.AKAR, 'AUTOTUNE', 'kaedah', 'param_julat.csv'))
    pj = pj[pj.tala == 'Y']
    bnA = pickle.load(open(os.path.join(kerja, f'benih_{cari_set}.pkl'), 'rb'))
    # ---- varian baharu bagi induk berasaskan kaedah M (±25 % nilai induk) ----
    tugas, asal = [], {}
    for r in induk.itertuples():
        pc = r.takrif.split('|')[0]
        if not pc.startswith('M'):
            continue
        mid = pc.split('.')[0]
        d = pj[pj.kaedah == mid]
        asas = json.loads(r.param) if r.param else {x.nama: x.nilai_asal for x in d.itertuples()}
        for v in range(1, N_VAR + 1):
            rng = np.random.default_rng([atom.BENIH, 4, int(mid[1:]), v])
            P = {}
            for x in d.itertuples():
                nilai = float(np.clip(asas.get(x.nama, x.nilai_asal) * rng.uniform(0.75, 1.25), x.bawah, x.atas))
                P[x.nama] = int(round(nilai)) if x.jenis == 'int' else nilai
            tugas.append((f'{mid}.t{v}', mid, P))
            asal[f'{mid}.t{v}'] = pc
    tl = cari.benih(kerja, cari_set, tugas=tugas, fail=f'benih_{cari_set}_tala.pkl')
    param = {**bnA['param'], **{n: P for n, _, P in tugas}}

    pan = cari.panel(kerja, cari_set)
    X = tk.label_asas(pan)
    C = ciri(pan)
    sah = pan['sah']
    cari.log('semak ciri lawan penapis asal (bar tidak sepadan): '
             + ', '.join(f"F{f + 1}: {int(((C[g[0]] >= {15: 70, 16: 90, 22: 4, 19: 30}[f]) != (pan['F'][f] > 0))[sah].sum())}"
                         for f, g in GRID.items()))
    pilih = []
    for r in induk.itertuples():
        pc, pen, _, _ = r.takrif.split('|')
        fs = [int(x[1:]) - 1 for x in pen.split('+')] if pen != '-' else []
        fs += [-1] * (2 - len(fs))
        calon = {pc: isyarat(pan, bnA['sig'][pc]) if not pc.startswith('P') else isyarat(pan, pan['P'][pc])}
        for n, p0 in asal.items():
            if p0 == pc and n in tl['sig']:
                calon[n] = isyarat(pan, tl['sig'][n])
        paksi = [GRID[f][1] if f in GRID else [None] for f in fs]
        terbaik = None
        for nama, ev in calon.items():
            G = np.full((len(paksi[0]), len(paksi[1])), np.nan)
            for (ia, a), (ib, b) in itertools.product(enumerate(paksi[0]), enumerate(paksi[1])):
                e = ev[topeng(pan, C, ev, fs[0], a) & topeng(pan, C, ev, fs[1], b)]
                G[ia, ib] = tk.skor_tepat(kadar(pan, X, e))
            D = dataran(G)
            if nama == pc:                                  # sel induk sendiri
                ii = tuple(paksi[k].index({15: 70, 16: 90, 22: 4, 19: 30}[fs[k]]) if fs[k] in GRID else 0 for k in (0, 1))
                induk_sel = (G[ii], D[ii])
            if np.isnan(D).all():
                continue
            ij = np.unravel_index(np.nanargmax(D), D.shape)
            if terbaik is None or D[ij] > terbaik['dataran']:
                terbaik = {'pencetus': nama, 'amb': (paksi[0][ij[0]], paksi[1][ij[1]]), 'skor': float(G[ij]),
                           'dataran': float(D[ij])}
        kekal = terbaik is None or (terbaik['pencetus'] == pc and all(
            a is None or a == {15: 70, 16: 90, 22: 4, 19: 30}[f] for a, f in zip(terbaik['amb'], fs)))
        if terbaik is None:
            terbaik = {'pencetus': pc, 'amb': (None, None), 'skor': float(induk_sel[0]), 'dataran': float(induk_sel[1])}
        ev = calon[terbaik['pencetus']]
        e = ev[topeng(pan, C, ev, fs[0], terbaik['amb'][0]) & topeng(pan, C, ev, fs[1], terbaik['amb'][1])]
        lajur = tk.keluar_terbaik(pan, e, -1, -1)
        vA = cari.nilai(pan, e, -1, -1, lajur, penuh=True, asas=cari.asas_rawak(pan, lajur))
        pilih.append({'induk': r.id, 'pc_induk': pc, 'fs': fs, 'kekal': kekal, 'calon': len(calon),
                      'skor_induk': float(induk_sel[0]), 'dataran_induk': float(induk_sel[1]), 'lajur': lajur,
                      'RA': dict(zip(T_cari, vA.values())), **terbaik})
        cari.log(f"{r.id}: {len(calon)} calon pencetus; induk dataran {induk_sel[1] * 100:+.2f} -> anak "
                 f"{terbaik['dataran'] * 100:+.2f} ({terbaik['pencetus']}, ambang {terbaik['amb']})"
                 + (' [induk kekal]' if kekal else ''))
    del pan, X, C
    # ---- Kunci: induk dan anak pada kumpulan B ----
    pan = cari.panel(kerja, kunci_set)
    X = tk.label_asas(pan)
    C = ciri(pan)
    bnB = pickle.load(open(os.path.join(kerja, f'benih_{kunci_set}.pkl'), 'rb'))
    perlu = {x['pencetus'] for x in pilih if '.t' in x['pencetus']}
    tlB = cari.benih(kerja, kunci_set, tugas=[t for t in tugas if t[0] in perlu], fail=f'benih_{kunci_set}_tala.pkl')

    def evB(n):
        if n.startswith('P'):
            return isyarat(pan, pan['P'][n])
        return isyarat(pan, (tlB if '.t' in n else bnB)['sig'][n])

    ringkas, baris = [], []
    for kd, x in enumerate(pilih, 1):
        fs = x['fs']
        ei = evB(x['pc_induk'])
        ei = ei[topeng(pan, C, ei, fs[0], None) & topeng(pan, C, ei, fs[1], None)]
        ea = evB(x['pencetus'])
        ea = ea[topeng(pan, C, ea, fs[0], x['amb'][0]) & topeng(pan, C, ea, fs[1], x['amb'][1])]
        vi = dict(zip(T_kunci, kadar(pan, X, ei).values()))
        va = dict(zip(T_kunci, kadar(pan, X, ea).values()))
        vR = dict(zip(T_kunci, cari.nilai(pan, ea, -1, -1, x['lajur'], penuh=True,
                                          asas=cari.asas_rawak(pan, x['lajur'])).values()))
        pen = [(GRID[f][2].format(a) if (f in GRID and a is not None) else atom.PENAPIS[f]) for f, a in zip(fs, x['amb'])
               if f >= 0]
        kod = '+'.join(atom.PENAPIS[f][:3] + (f'@{a}' if (f in GRID and a is not None) else '')
                       for f, a in zip(fs, x['amb']) if f >= 0) or '-'
        s, rr = divmod(x['lajur'], cari.NR)
        d = {'masuk': lapor.nama_pencetus(x['pencetus'], param) + f" [tala daripada {x['induk']}]",
             'penapis': ' DAN '.join(pen) or 'tiada', 'henti': atom.HENTI[s],
             'keluar': teras.nama_keluar(rr, cari.A1, cari.A2, cari.OP, atom.KELUAR)}
        kel = 'X00' if cari.OP[rr] == 0 else atom.KELUAR[cari.A1[rr]][:3] if cari.OP[rr] == 1 else (
            f"{atom.KELUAR[cari.A1[rr]][:3]} {'ATAU' if cari.OP[rr] == 2 else 'DAN'} {atom.KELUAR[cari.A2[rr]][:3]}")
        ro = SimpleNamespace(pencetus=x['pencetus'], lajur=x['lajur'], skor_tepat=x['skor'],
                             takrif_khas=f"{x['pencetus']}|{kod}|{atom.HENTI[s][:2]}|{kel}")
        v = {**x['RA'], **vR}
        li, la = lebih(vi, T_kunci), lebih(va, T_kunci)
        T1 = all(va[t]['n'] and va[t]['t10'] > va[t]['a_t10'] for t in T_kunci)
        T2 = all(va[t]['n'] and va[t]['lari'] > va[t]['a_lari'] for t in T_kunci)
        T3 = bool(la > li) and not x['kekal']
        if not x['kekal']:
            ringkas.append((kd, d, ro, v, T1, T2, T3, np.nan, []))
        k3 = T_kunci[-1]
        baris.append({'induk': x['induk'], 'kekal': x['kekal'], 'calon_pencetus': x['calon'], **d,
                      'dataran_induk': x['dataran_induk'], 'dataran_anak': x['dataran'], 'n_kunci': gab(va, T_kunci, 'lari')[0],
                      **{f'{n}_anak': gab(va, T_kunci, n)[1] for n in tk.LABEL},
                      **{f'{n}_rawak': gab(va, T_kunci, 'a_' + n)[1] for n in tk.LABEL},
                      'lebih_induk': li, 'lebih_anak': la,
                      'lebih_induk_K3': vi[k3]['lari'] - vi[k3]['a_lari'], 'lebih_anak_K3': va[k3]['lari'] - va[k3]['a_lari'],
                      'T1': T1, 'T2': T2, **{f'R_{t}': vR[t]['purata'] if vR[t]['n'] else np.nan for t in T_kunci},
                      **{f'menang_{t}': vR[t].get('menang', np.nan) for t in T_kunci},
                      **{f'pegang_{t}': vR[t].get('pegang', np.nan) for t in T_kunci}, '_kd': kd})
    idf = lapor.daftar_f(ringkas, param, PUS, T_cari, T_kunci) if ringkas else {}
    T = pd.DataFrame(baris)
    T['anak'] = [x['induk'] if x['kekal'] else idf[x['_kd']] for x in baris]
    d_ = os.path.join(SINI, 'hasil', PUS)
    os.makedirs(d_, exist_ok=True)
    T.drop(columns=['_kd']).to_csv(os.path.join(d_, 'papan.csv'), index=False, float_format='%.5f')
    ubah = T[~T.kekal]
    p = lambda x, k=1, t=False: '–' if x != x else (f'{x * 100:+.{k}f}' if t else f'{x * 100:.{k}f}')
    try:
        sys.path.insert(0, os.path.join(lapor.BS2, 'standard'))
        import status_kad
        status = status_kad.baris()
    except Exception:
        status = '> **Status keputusan:** lihat `laporan/KAD_SKOR.md`; laporan ini BUKAN keputusan.'
    k3 = T_kunci[-1]
    A = [f'# Carian Setup {PUS} — tala parameter di sekitar pemenang (backtest, BUKAN bukti)', '', status, '',
         'Dijana `kajian/carian_setup/cs_tala.py`. Pradaftar: `kajian/SPEC_CARIAN_SETUP.md` pindaan 13 Nov 2026 (e). '
         '**Jangan sunting secara manual.** Papan induk (CS03): `carian_setup/hasil/CS03/LAPORAN.md`.', '',
         '## 1. Apa yang dibuat', '',
         'Sepuluh masuk terbaik CS03 (`F21`–`F30`, dipangkatkan ikut kadar tangkap saham "lari") ditala: 24 varian parameter '
         '(±25 %) bagi induk berasaskan kaedah M, dan grid ambang bagi penapis RS, ATR % dan jarak dari puncak 52 minggu. '
         'Anak dipilih pada kumpulan A ikut **dataran** (median sel dan jirannya), kemudian induk dan anak dibandingkan pada '
         '**kumpulan B** (saham yang carian tidak lihat). "Lari" = naik ≥ 5 % minggu pertama, capai ≥ 10 % sebelum henti −8 %, '
         'masih ≥ 10 % pada minggu ke-4. Rawak = saham lain hari sama, tahap turun-naik sama.', '',
         '## 2. Induk lawan anak (kumpulan B, 2010 – Ogo 2026)', '',
         '| Induk | Anak | Masuk | Penapis | Belian | **Lari %** (rawak) | Capai +10 % dahulu % (rawak) | Kena henti −8 % dahulu % '
         f'(rawak) | Kelebihan lari: induk → anak | {k3} sahaja: induk → anak |', '|---' * 10 + '|']
    for x in T.itertuples():
        A.append(f"| `{x.induk}` | {'kekal' if x.kekal else '`' + x.anak + '`'} | {x.masuk.split(' [tala')[0]} | {x.penapis} | "
                 f"{int(x.n_kunci):,} | **{p(x.lari_anak)} ({p(x.lari_rawak)})** | {p(x.t10_anak)} ({p(x.t10_rawak)}) | "
                 f"{p(x.gagal_anak)} ({p(x.gagal_rawak)}) | {p(x.lebih_induk, 2, True)} → {p(x.lebih_anak, 2, True)} | "
                 f"{p(x.lebih_induk_K3, 2, True)} → {p(x.lebih_anak_K3, 2, True)} |")
    baik = int((ubah.lebih_anak > ubah.lebih_induk).sum())
    baik3 = int((ubah.lebih_anak_K3 > ubah.lebih_induk_K3).sum())
    A += ['', f'- Induk yang ditala menjadi anak baharu: {len(ubah)} daripada {len(T)}; selebihnya induk sendiri sudah berada '
          'di dataran terbaik.',
          f'- Anak yang kelebihan "lari"-nya melebihi induk pada kumpulan B: **{baik} daripada {len(ubah)}**; pada {k3} '
          f'(tahun yang tidak dipakai carian): **{baik3} daripada {len(ubah)}**.',
          f"- Median kelebihan: induk {p(T.lebih_induk.median(), 2, True)} mata → anak {p(T.lebih_anak.median(), 2, True)} mata.",
          '', '## 3. Cara pegang dan keluar terbaik bagi setiap anak (dipilih pada kumpulan A; angka kumpulan B)', '',
          '| Setup | Henti | Keluar | ' + ' | '.join(f'{t}: purata % / menang % / pegang' for t in T_kunci) + ' |',
          '|---' * (3 + len(T_kunci)) + '|']
    for x in T.itertuples():
        A.append(f"| `{x.anak}` | {x.henti} | {x.keluar} | " + ' | '.join(
            f"{p(getattr(x, 'R_' + t), 2, True)} / {p(getattr(x, 'menang_' + t))} / {getattr(x, 'pegang_' + t):.1f}"
            for t in T_kunci) + ' |')
    A += ['', '## 4. Kaveat', '',
          '- Backtest sahaja; tiada setup masuk papertrade tanpa keputusan pengguna. Kad skor kekal satu-satunya keputusan '
          'wang sebenar.',
          '- Penalaan memilih sel terbaik daripada banyak sel; sebab itu perbandingan induk lawan anak dibuat pada saham yang '
          'tidak dilihat. Anak yang tidak mengatasi induk di situ tidak patut menggantikannya.',
          '- Tiada saham delist (condong ke atas); set 2000 bukan tapisan Shariah; data bermula 2010.', '']
    teks = '\n'.join(A)
    open(os.path.join(d_, 'LAPORAN.md'), 'w', encoding='utf-8').write(teks)
    open(os.path.join(lapor.BS2, 'kajian', 'CARIAN_SETUP.md'), 'w', encoding='utf-8').write(teks)
    json.dump({'pusingan': PUS, 'induk': len(T), 'ditala': len(ubah), 'anak_lebih_baik': baik, 'anak_lebih_baik_K3': baik3,
               'varian_dijalankan': len(tl['sig']), 'varian_gagal': tl['ralat'],
               'median_lebih_induk': float(T.lebih_induk.median()), 'median_lebih_anak': float(T.lebih_anak.median())},
              open(os.path.join(d_, 'meta.json'), 'w'), indent=1)
    cari.log(f'CS04 siap: ditala {len(ubah)}/{len(T)}; anak lebih baik {baik}; pada {k3} {baik3}')


if __name__ == '__main__':
    main(sys.argv[1])
