"""Carian setup — CS09 pada LORONG TREND: keluar ikut kata pengguna pada papan T01-T12 (SPEC pindaan 15 Nov 2026 (w)).

Peraturan U_T: pada tutup sesi >= d, tutup < harga beli DAN trend patah -> jual pada buka sesi berikutnya. Posisi untung
tidak pernah dijual oleh indikator. Diukur lawan "pegang sahaja" (X00, henti terpilih setup, had 126 sesi).
Guna: python3 cs_trend9.py <kerja>   |   python3 cs_trend9.py --lapor
Keluaran: hasil/CS09/TREND.md, trend_takrif.csv, trend_setup.csv, trend_meta.json. Jangan sunting keluaran secara manual."""
import json
import os
import pickle
import sys

import numpy as np
import pandas as pd
from numba import njit, prange

SINI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SINI)
import cs_trend8 as t8  # noqa: E402

KELUAR = os.path.join(SINI, 'hasil', 'CS09')
BS2 = os.path.dirname(os.path.dirname(SINI))
D_RUGI = np.asarray([3, 10, 20, 40], np.int64)                          # dikunci pindaan (w)
SIMPAN_MIN, MIN_ERA, TOLERANSI_TB = 0.90, 30, 0.005
TREND = [a for a in range(t8.NA) if t8.JENIS[a] == 0]
NT, ND = len(TREND), len(D_RUGI)
NK = 1 + (NT + 1) * ND                                                  # 0 = X00; 1 + t * ND + j; t = NT -> "rugi sahaja"
H_MAX, NH, KOS = t8.H_MAX, t8.NH, t8.KOS
UKURAN = ('purata', 'median', 'menang', 'rugi15', 'tb', 'R_besar', 'jual')


def kol(t, j):
    return 1 + t * ND + j


def teks(t, j):
    return f'rugi (tutup < harga beli, sesi ≥ {int(D_RUGI[j])})' + ('' if t == NT else f' DAN {t8.ATOM[TREND[t]][3]}')


@njit(parallel=True, cache=True)
def hasil_rugi(ev, o, l, c, atr, XT, D, pegang_min):
    """R[isyarat, henti, lajur] dan indeks sesi jual. Lajur 1 + t * nD + j: jual pada buka selepas tutup pertama (sesi >= D[j],
    sesi >= pegang_min) yang < harga beli DAN XT[t] benar; t = nT ialah "rugi sahaja". Mekanik lain = cs_trend8.hasil_semua."""
    n, nT, nD = ev.shape[0], XT.shape[0], D.shape[0]
    nK = 1 + (nT + 1) * nD
    R = np.zeros((n, NH, nK), np.float32)
    SK = np.zeros((n, NH, nK), np.int16)
    for k in prange(n):
        i = ev[k]
        e = i + 1
        P = o[e]
        L = np.zeros(NH)
        t8._aras(P, atr[i], L)
        dx = np.full((nT + 1, nD), 999, np.int64)
        for d in range(pegang_min - 1, H_MAX - 1):
            b = e + d
            if c[b] >= P:
                continue
            for j in range(nD):
                if d + 1 < D[j]:
                    continue
                for a in range(nT):
                    if dx[a, j] == 999 and XT[a, b] != 0:
                        dx[a, j] = d + 1
                if dx[nT, j] == 999:
                    dx[nT, j] = d + 1
        for s in range(NH):
            h0 = c[e] <= L[s]
            ds, ps = 999, 0.0
            for d in range(1, H_MAX):
                b = e + d
                if o[b] <= L[s]:
                    ds, ps = d, o[b]
                    break
                if l[b] <= L[s]:
                    ds, ps = d, L[s]
                    break
            for q in range(nK):
                x = 999
                if q > 0:
                    x = dx[(q - 1) // nD, (q - 1) % nD]
                if h0:
                    R[k, s, q], SK[k, s, q] = o[e + 1] / P - 1.0 - KOS, 1
                elif x != 999 and x <= ds:
                    R[k, s, q], SK[k, s, q] = o[e + x] / P - 1.0 - KOS, x
                elif ds != 999:
                    R[k, s, q], SK[k, s, q] = ps / P - 1.0 - KOS, ds
                else:
                    R[k, s, q], SK[k, s, q] = c[e + H_MAX - 1] / P - 1.0 - KOS, H_MAX - 1
    return R, SK


def _hasil(pan, XT, ev):
    return hasil_rugi(np.ascontiguousarray(ev, dtype=np.int64), pan['o'], pan['l'], pan['c'], pan['atr'],
                      np.ascontiguousarray(XT), D_RUGI, t8.PEGANG_MIN)


def pilih(kerja, papan, KL):
    """U_T* pada kumpulan A sahaja: skor = min era (purata peraturan - purata X00), syarat simpan pelari besar >= 0.90."""
    import cs_cari as cari
    import cs_lapis as lapis
    pan = cari.panel(kerja, 'A')
    L = lapis.muat(kerja, 'A')
    Lr, XT = (L['L1'], L['L2']), np.asarray(t8.siri_set(kerja, 'A'))
    S8, _, L8, _ = t8.label_v(pan)
    D, S = [], []
    for b in papan:
        ev = t8._ev_papan(kerja, 'A', pan, Lr, S8, b)
        s = KL['pilih'][b['id']][0]
        R = _hasil(pan, XT, ev)[0][:, s, :].astype(np.float64)
        era, besar = pan['tempoh'][ev], L8[ev, 0] > 0
        d = [R[era == p].mean(axis=0) - R[era == p, 0].mean() for p in (0, 1) if (era == p).sum() >= MIN_ERA]
        if not d:
            continue
        D.append(np.min(d, axis=0))
        rb = R[besar].sum(axis=0)
        S.append(rb / rb[0] if rb[0] > 0 else np.full(NK, np.nan))
    D, S = np.nanmean(D, axis=0), np.nanmean(S, axis=0)
    calon = np.where(S >= SIMPAN_MIN, D, -np.inf)
    calon[0] = -np.inf
    calon[kol(NT, 0):] = -np.inf                                         # "rugi sahaja" bukan calon
    q = int(np.argmax(calon))
    return {'kol': q, 't': (q - 1) // ND, 'j': (q - 1) % ND, 'skor_a': D, 'simpan_a': S}


def nilai(kerja):
    import cs_cari as cari
    import cs_lapis as lapis
    import cs_teras as teras
    papan = pickle.load(open(os.path.join(kerja, 'cs08_papan.pkl'), 'rb'))
    KL = pickle.load(open(os.path.join(kerja, 'cs08_keluar.pkl'), 'rb'))
    KC = pickle.load(open(os.path.join(kerja, 'cs08_kunci.pkl'), 'rb'))
    pl = pilih(kerja, papan, KL)
    pan = cari.panel(kerja, 'B')
    L = lapis.muat(kerja, 'B')
    Lr, XT = (L['L1'], L['L2']), np.asarray(t8.siri_set(kerja, 'B'))
    S8, _, L8, _ = t8.label_v(pan)
    baris_t, baris_s = [], []
    for b in papan:
        e0 = t8._ev_papan(kerja, 'B', pan, Lr, S8, b)
        s = KL['pilih'][b['id']][0]
        R, SK = _hasil(pan, XT, e0)
        R8, SK8 = t8._hasil(pan, XT, e0)
        assert np.array_equal(R[:, :, 0], R8[:, :, 0]) and np.array_equal(SK[:, :, 0], SK8[:, :, 0])      # pariti X00
        for j, d in enumerate(D_RUGI):                                   # pariti "rugi sahaja" lawan atom jenis 3 CS08
            t3 = [a for a in range(t8.NA) if t8.JENIS[a] == 3 and t8.PAR[a] == d]
            if t3:
                assert np.array_equal(R[:, :, kol(NT, j)], R8[:, :, 1 + t3[0] * t8.NG]), (b['id'], int(d))
        sk0 = SK[:, s, 0].astype(np.int64)

        def ukur(Rr, sk):
            Rr, sk = Rr.astype(np.float64), sk.astype(np.int64)
            amb = teras.satu_posisi(e0, sk, pan['tid'])
            e, Rr = e0[amb], Rr[amb]
            bs = L8[e, 0] > 0
            return {'n': int(len(e)), 'purata': float(Rr.mean()), 'median': float(np.median(Rr)), 'menang': float((Rr > 0).mean()),
                    'rugi15': float((Rr <= -0.15).mean()), 'tb': float((Rr >= t8.TB).mean()),
                    'R_besar': float(Rr[bs].mean()) if bs.any() else np.nan, 'jual': float((sk[amb] < sk0[amb]).mean()),
                    'pegang': float(np.median(sk[amb]) + 1)}

        tolong = lambda u, x: bool(u['purata'] > x['purata'] and u['rugi15'] < x['rugi15'] and u['tb'] >= x['tb'] - TOLERANSI_TB)
        x0 = ukur(R[:, s, 0], SK[:, s, 0])
        r = {'id': b['id'], 'dipercayai': bool(KC['setup'][b['id']]['dipercayai']), 'henti': t8.HENTI[s],
             **{f'x00_{k}': v for k, v in x0.items()}}
        a_tr = 1 + TREND[pl['t']] * t8.NG
        for nama, (Rr, sk) in (('sejagat', (R[:, s, pl['kol']], SK[:, s, pl['kol']])),
                               ('rugi_sahaja', (R[:, s, kol(NT, pl['j'])], SK[:, s, kol(NT, pl['j'])])),
                               ('trend_sahaja', (R8[:, s, a_tr], SK8[:, s, a_tr]))):
            u = ukur(Rr, sk)
            r.update({f'{nama}_{k}': v for k, v in u.items()})
            r[f'{nama}_ditolong'] = tolong(u, x0)
        baris_s.append(r)
        for q in range(1, kol(NT, 0)):
            u = ukur(R[:, s, q], SK[:, s, q])
            baris_t.append({'id': b['id'], 'dipercayai': r['dipercayai'], 'kol': q, **{f'd_{k}': u[k] - x0[k] for k in UKURAN},
                            'simpan': u['R_besar'] / x0['R_besar'] if x0['R_besar'] else np.nan, 'ditolong': tolong(u, x0)})
        cari.log(f"  CS09 trend {b['id']}: {x0['n']} belian")
    T = pd.DataFrame(baris_t)
    yk = T[T.dipercayai]
    G = T.groupby('kol').agg(setup=('id', 'count'), ditolong=('ditolong', 'sum'), **{f'd_{k}': (f'd_{k}', 'median') for k in UKURAN},
                             simpan=('simpan', 'median')).reset_index()
    G['ditolong_dipercayai'] = G.kol.map(yk.groupby('kol').ditolong.sum())
    G.insert(1, 'd', [int(D_RUGI[(q - 1) % ND]) for q in G.kol])
    G.insert(2, 'trend_patah', [t8.ATOM[TREND[(q - 1) // ND]][3] for q in G.kol])
    G['skor_a'] = [float(pl['skor_a'][q]) for q in G.kol]
    os.makedirs(KELUAR, exist_ok=True)
    G.drop(columns='kol').to_csv(os.path.join(KELUAR, 'trend_takrif.csv'), index=False, float_format='%.5f')
    pd.DataFrame(baris_s).to_csv(os.path.join(KELUAR, 'trend_setup.csv'), index=False, float_format='%.5f')
    ok = np.isfinite(pl['skor_a'][1:kol(NT, 0)])
    meta = {'sejagat': {'teks': teks(pl['t'], pl['j']), 'd': int(D_RUGI[pl['j']]), 'trend_patah': t8.ATOM[TREND[pl['t']]][3],
                        'skor_a': float(pl['skor_a'][pl['kol']]), 'simpan_a': float(pl['simpan_a'][pl['kol']])},
            'peraturan': int(kol(NT, 0) - 1), 'takrif_trend': NT, 'setup': len(papan),
            'a_peraturan_skor_positif': int((pl['skor_a'][1:kol(NT, 0)][ok] > 0).sum())}
    with open(os.path.join(KELUAR, 'trend_meta.json'), 'w') as f:
        json.dump(meta, f, indent=1, ensure_ascii=False)
    cari.log(f"CS09 trend: U_T* = {meta['sejagat']['teks']} (skor A {meta['sejagat']['skor_a'] * 100:+.2f} mata)")


def lapor():
    G = pd.read_csv(os.path.join(KELUAR, 'trend_takrif.csv'))
    S = pd.read_csv(os.path.join(KELUAR, 'trend_setup.csv'))
    with open(os.path.join(KELUAR, 'trend_meta.json')) as f:
        meta = json.load(f)
    try:
        sys.path.insert(0, os.path.join(BS2, 'standard'))
        import status_kad
        status = status_kad.baris()
    except Exception:
        status = '> **Status keputusan:** lihat `laporan/KAD_SKOR.md`; laporan ini BUKAN keputusan.'
    p = lambda x, k=1, t=False: '–' if x != x else (f'{x * 100:+.{k}f}' if t else f'{x * 100:.{k}f}')
    Y = S[S.dipercayai]
    u, n, ny, nt = meta['sejagat'], len(S), len(Y), len(G)
    teguh = int((G.d_purata > 0).sum())
    menolong = bool(Y.sejagat_ditolong.sum() > ny / 2 and (Y.sejagat_purata - Y.x00_purata).median() > 0)
    A = ['# CS09 lorong TREND — keluar ikut kata pengguna pada papan T01–T12 (backtest; BUKAN bukti)', '', status, '',
         'Dijana `kajian/carian_setup/cs_trend9.py`. Pradaftar: `kajian/SPEC_CARIAN_SETUP.md` pindaan 15 Nov 2026 (w), dikomit '
         'sebelum dijalankan. **Jangan sunting secara manual.**', '',
         '## 1. Jawapan', '',
         f'- **Peraturan sejagat U_T\\*** (dipilih pada kumpulan A sahaja): **{u["teks"]}** → jual pada buka sesi berikutnya. '
         f'Skor kumpulan A {u["skor_a"] * 100:+.2f} mata purata; simpan pelari besar {u["simpan_a"]:.2f}; '
         f'{meta["a_peraturan_skor_positif"]} daripada {meta["peraturan"]} peraturan berskor positif pada kumpulan A.',
         f'- **Bacaan dikunci:** peraturan pengguna {"MENOLONG" if menolong else "TIDAK menolong"} lorong trend '
         f'({int(Y.sejagat_ditolong.sum())} daripada {ny} setup dipercayai-T ditolong pada kumpulan B; median beza purata '
         f'{p((Y.sejagat_purata - Y.x00_purata).median(), 2, True)} mata). Idea itu {"TEGUH" if teguh > nt / 2 else "TIDAK teguh"}: '
         f'{teguh} daripada {nt} peraturan mempunyai median beza purata > 0 (peringkat 1, tanpa pemilihan).', '',
         '## 2. Setiap setup: "pegang sahaja" (`X00`) → dengan U_T\\* (kumpulan B)', '',
         '| ID | perc. | henti | belian | purata % | median % | menang % | rugi ≥ 15 % | dijual ≥ +30 % | untung pelari besar % | '
         'dijual U_T\\* % | sesi pegang (median) | ditolong |', '|' + '---|' * 13]
    for r in S.itertuples():
        g = lambda k, t=False: f"{p(getattr(r, f'x00_{k}'), 1, t)} → {p(getattr(r, f'sejagat_{k}'), 1, t)}"
        A.append(f"| `{r.id}` | {'✓' if r.dipercayai else '✗'} | {r.henti} | {r.x00_n:,} | {g('purata', True)} | {g('median', True)} | "
                 f"{g('menang')} | {g('rugi15')} | {g('tb')} | {g('R_besar')} | {p(r.sejagat_jual)} | "
                 f"{r.x00_pegang:.0f} → {r.sejagat_pegang:.0f} | {'✓' if r.sejagat_ditolong else '✗'} |")
    A += ['', '## 3. Adakah gabungan DAN itu yang bekerja? (kumpulan B, median beza lawan `X00`, mata)', '',
          '| Keluar | purata | median | menang | rugi ≥ 15 % | dijual ≥ +30 % | untung pelari besar | setup ditolong |', '|' + '---|' * 8]
    for nama, t in (('sejagat', f'U_T\\* ({u["teks"]})'), ('rugi_sahaja', f'"rugi → jual" sahaja (sesi ≥ {u["d"]}, tanpa syarat trend)'),
                    ('trend_sahaja', f'"{u["trend_patah"]} → jual" sahaja (walaupun untung)')):
        dd = lambda k: (S[f'{nama}_{k}'] - S[f'x00_{k}']).median()
        A.append(f"| {t} | {p(dd('purata'), 2, True)} | {p(dd('median'), 2, True)} | {p(dd('menang'), 1, True)} | "
                 f"{p(dd('rugi15'), 1, True)} | {p(dd('tb'), 1, True)} | {p(dd('R_besar'), 1, True)} | "
                 f"{int(S[f'{nama}_ditolong'].sum())} / {n} |")
    A += ['', '## 4. Peringkat 1: setiap peraturan (kumpulan B, tanpa pemilihan)', '',
          'Median beza purata lawan `X00` merentas 12 setup (mata), ikut takrif "trend patah" × sesi mula menilai rugi; dalam '
          'kurungan: bilangan setup ditolong.', '',
          '| Trend patah | ' + ' | '.join(f'd = {int(d)}' for d in D_RUGI) + ' | rugi ≥ 15 % (d = 3) | pelari besar simpan (d = 3) |',
          '|' + '---|' * (ND + 3)]
    for nama, g in G.groupby('trend_patah', sort=False):
        g = g.set_index('d')
        A.append(f'| {nama} | ' + ' | '.join(f'{p(g.loc[int(d), "d_purata"], 2, True)} ({int(g.loc[int(d), "ditolong"])})' for d in D_RUGI)
                 + f' | {p(g.loc[3, "d_rugi15"], 1, True)} | {g.loc[3, "simpan"]:.2f} |')
    A += ['', '## 5. Kaveat', '',
          '- Papan `T` dipilih pada kumpulan A dan dibaca pada kumpulan B (CS08); 12 setup sahaja, banyak berkongsi prasyarat hasil '
          'suku tumbuh ≥ 20 %, jadi bilangan "setup ditolong" bukan 12 ujian bebas. Tiada saham delist.',
          '- Tiada perubahan papan `T`, registry atau kohort.', '']
    with open(os.path.join(KELUAR, 'TREND.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(A) + '\n')


if __name__ == '__main__':
    if sys.argv[1] != '--lapor':
        nilai(sys.argv[1])
    lapor()
