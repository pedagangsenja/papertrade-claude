"""Carian setup — pusingan CS09: KELUAR ikut kata pengguna (SPEC pindaan 15 Nov 2026 (v)).

"Pegang selagi untung; henti rugi wajib; rugi sedikit tetapi trend masih naik -> terus pegang." Peraturan U: pada tutup
sesi >= d, tutup < harga beli DAN trend patah -> jual pada buka sesi berikutnya. Posisi untung tidak pernah dijual oleh
indikator. Diukur lawan "pegang sahaja" (X00, henti yang sama) bagi setiap setup `KEDUDUKAN_AKHIR.csv`.
  peringkat 1  idea tanpa pemilihan: 45 takrif "trend patah" pada d = 3, kumpulan B;
  peringkat 2  pemilihan pada kumpulan A sahaja (Acc CS07 sedia ada): satu peraturan sejagat U* dan pilihan setiap setup;
               dilaporkan pada kumpulan B;
  rujukan      "rugi -> jual" sahaja, "trend patah -> jual" sahaja, keluar berdaftar.
Guna: python3 cs_keluar9.py <kerja>   |   python3 cs_keluar9.py --lapor
Keluaran: hasil/CS09/LAPORAN.md, takrif.csv, setup.csv, meta.json. Jangan sunting keluaran secara manual."""
import json
import os
import pickle
import sys

import numpy as np
import pandas as pd

SINI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SINI)
import cs_keluar7 as k7  # noqa: E402

HASIL = os.path.join(SINI, 'hasil')
KELUAR = os.path.join(HASIL, 'CS09')
BS2 = os.path.dirname(os.path.dirname(SINI))
REG_F = os.path.join(BS2, 'data', 'registry_F.csv')

FAM_TREND = ('Y01', 'Y02', 'Y03', 'Y04', 'Y05', 'Y07', 'Y10', 'Y11', 'Y15')      # dikunci pindaan (v)
D_RUGI = (3, 5, 8, 10)
SIMPAN_MIN, MIN_ERA, TOLERANSI_TP = 0.90, 30, 0.005
TREND = [a for a, x in enumerate(k7.ATOM) if x[0].split('.')[0] in FAM_TREND]
RUGI = {int(x[2]['k']): a for a, x in enumerate(k7.ATOM) if x[0].startswith('Y19.')}
UKURAN = ('purata', 'menang', 'rugi8', 'rugi15', 'tp', 'R_pelari', 'jual', 'pegang')


def kol_tunggal(a):
    return int(np.flatnonzero((k7.OP == 1) & (k7.A1 == a))[0]) * k7.NG


def kol_dan(a, b):
    a, b = min(a, b), max(a, b)
    return int(np.flatnonzero((k7.OP == 3) & (k7.A1 == a) & (k7.A2 == b))[0]) * k7.NG


def peraturan():
    """Senarai (kol, atom trend, d) bagi 180 peraturan U."""
    return [(kol_dan(a, RUGI[d]), a, d) for d in D_RUGI for a in TREND]


def teks(a, d):
    return f'rugi (tutup < harga beli, sesi ≥ {d}) DAN {k7.ATOM[a][3]}'


# ---------- peringkat 2: pemilihan pada kumpulan A ----------
def skor_a(acc, s, kols):
    """acc[henti, lajur, era, stat] satu setup. Pulangkan (skor = min era beza purata lawan X00, nisbah simpan pelari) bagi
    setiap lajur dalam kols; era dengan < MIN_ERA isyarat diabaikan; NaN jika tiada era yang cukup."""
    n = acc[s, 0, :, 0]
    ok = n >= MIN_ERA
    if not ok.any():
        return np.full(len(kols), np.nan), np.full(len(kols), np.nan)
    pur = acc[s][:, ok, 5] / n[ok]
    d = (pur[kols] - pur[0]).min(axis=1)
    rt = acc[s][:, :, 7].sum(axis=1)
    simpan = rt[kols] / rt[0] if rt[0] > 0 else np.full(len(kols), np.nan)
    return d, simpan


def pilih(kerja, setups):
    """U* sejagat dan pilihan setiap setup, pada kumpulan A sahaja. setups: senarai (id, s)."""
    P = peraturan()
    kols = np.asarray([p[0] for p in P])
    with open(os.path.join(kerja, 'cs07_idf.pkl'), 'rb') as f:
        songsang = {v: k for k, v in pickle.load(f).items()}
    D, S, sendiri = [], [], {}
    for i, s in setups:
        f = os.path.join(kerja, 'cs07_keluar', f'{songsang.get(i, i)}_A.npy')
        d, simpan = skor_a(np.load(f), s, kols)
        if np.isnan(d).all():
            sendiri[i] = None
            continue
        D.append(d)
        S.append(simpan)
        lulus = (simpan >= SIMPAN_MIN) & (d > 0)
        sendiri[i] = int(np.argmax(np.where(lulus, d, -np.inf))) if lulus.any() else None
    D, S = np.asarray(D), np.asarray(S)
    purata_d, purata_s = np.nanmean(D, axis=0), np.nanmean(S, axis=0)
    j = int(np.argmax(np.where(purata_s >= SIMPAN_MIN, purata_d, -np.inf)))
    return {'P': P, 'sejagat': j, 'sendiri': sendiri, 'skor_a': purata_d, 'simpan_a': purata_s, 'n_setup_a': len(D),
            'positif_a': (D > 0).sum(axis=0)}


# ---------- penilaian pada kumpulan B ----------
def nilai(kerja):
    import cs_cari as cari
    import cs_cs05 as c5
    import cs_cs07 as c7
    import cs_pegang as pg
    import cs_portfolio6 as p6
    import cs_tala7 as t7
    import cs_teras as teras
    pan, _, EV, _, L = c5._sedia(kerja, 'B')
    Lr, XA = (L['L1'], L['L2']), k7.siri_set(kerja, 'B')
    akhir = pd.read_csv(os.path.join(HASIL, 'KEDUDUKAN_AKHIR.csv')).set_index('id')
    reg = pd.read_csv(REG_F, dtype=str).fillna('').set_index('id')
    S = []
    for i in akhir.index:
        r = reg.loc[i]
        if r.pusingan == 'CS07':
            d = c7.dari_takrif7(r.takrif)
            ev = t7.ev_satu(kerja, 'B', d['pencetus'])
        else:
            d = p6.dari_takrif5(r.takrif)
            ev = EV[d['pencetus']]
            d['s'], d['kol'] = pg.lama_ke_baharu(d['lajur'])
        S.append((i, d, ev[c5.topeng(pan, Lr, ev, d['q1'], d['q2'], d['f1'], d['f2'])]))
    pl = pilih(kerja, [(i, d['s']) for i, d, _ in S])
    P = pl['P']
    j3 = [j for j, p in enumerate(P) if p[2] == 3]                      # peringkat 1: 45 takrif pada d = 3
    a_s = P[pl['sejagat']][1]
    rujukan = {'rugi_sahaja': kol_tunggal(RUGI[3]), 'trend_sahaja': kol_tunggal(a_s)}
    baris_t, baris_s = [], []
    for i, d, e0 in S:
        St = k7.sedia_pan(pan, XA, e0)
        m5, trs = St[7][:, 0] > 0, St[7][:, 1] > 0
        sk0 = k7.hasil(*St[:7], k7.A1, k7.A2, k7.OP, d['s'], 0)[1]

        def ukur(kol):
            R, sk = k7.hasil(*St[:7], k7.A1, k7.A2, k7.OP, d['s'], kol)
            amb = teras.satu_posisi(e0, sk, pan['tid'])
            R, t = R[amb], trs[amb]
            return {'n': int(len(R)), 'purata': float(R.mean()), 'menang': float((R > 0).mean()),
                    'rugi8': float((R <= -0.08).mean()), 'rugi15': float((R <= -0.15).mean()),
                    'tp': float((m5[amb] & (R >= 0.10)).mean()), 'R_pelari': float(R[t].mean()) if t.any() else np.nan,
                    'jual': float((sk[amb] < sk0[amb]).mean()), 'pegang': float(sk[amb].mean() + 1)}

        x0 = ukur(0)
        b = {'id': i, 'kedudukan': int(akhir.loc[i, 'kedudukan']), 'dipercayai': bool(akhir.loc[i, 'dipercayai']),
             'henti': k7.HENTI[d['s']], **{f'x00_{k}': v for k, v in x0.items()}}
        calon = {'daftar': d['kol'], 'sejagat': P[pl['sejagat']][0], **rujukan,
                 'sendiri': P[pl['sendiri'][i]][0] if pl['sendiri'][i] is not None else 0}
        for nama, kol in calon.items():
            u = x0 if kol == 0 else ukur(kol)
            b.update({f'{nama}_{k}': v for k, v in u.items()})
            b[f'{nama}_ditolong'] = bool(u['purata'] > x0['purata'] and u['rugi8'] < x0['rugi8']
                                         and u['tp'] >= x0['tp'] - TOLERANSI_TP)
        b['sendiri_peraturan'] = teks(*P[pl['sendiri'][i]][1:]) if pl['sendiri'][i] is not None else 'X00 (pegang sahaja)'
        baris_s.append(b)
        for j in j3:
            u = ukur(P[j][0])
            baris_t.append({'id': i, 'dipercayai': b['dipercayai'], 'j': j, **{f'd_{k}': u[k] - x0[k] for k in UKURAN},
                            'simpan': u['R_pelari'] / x0['R_pelari'] if x0['R_pelari'] else np.nan,
                            'ditolong': bool(u['purata'] > x0['purata'] and u['rugi8'] < x0['rugi8']
                                             and u['tp'] >= x0['tp'] - TOLERANSI_TP)})
    os.makedirs(KELUAR, exist_ok=True)
    T = pd.DataFrame(baris_t)
    yk = T[T.dipercayai]
    G = T.groupby('j').agg(setup=('id', 'count'), ditolong=('ditolong', 'sum'), **{f'd_{k}': (f'd_{k}', 'median') for k in UKURAN},
                           d_purata_min=('d_purata', 'mean'), simpan=('simpan', 'median')).reset_index()
    G['ditolong_dipercayai'] = G.j.map(yk.groupby('j').ditolong.sum())
    G['d_purata_dipercayai'] = G.j.map(yk.groupby('j').d_purata.median())
    G.insert(1, 'atom', [k7.ATOM[P[j][1]][0] for j in G.j])
    G.insert(2, 'trend_patah', [k7.ATOM[P[j][1]][3] for j in G.j])
    G['skor_a'] = [float(pl['skor_a'][j]) for j in G.j]
    G.drop(columns='j').to_csv(os.path.join(KELUAR, 'takrif.csv'), index=False, float_format='%.5f')
    pd.DataFrame(baris_s).to_csv(os.path.join(KELUAR, 'setup.csv'), index=False, float_format='%.5f')
    js = pl['sejagat']
    meta = {'sejagat': {'atom': k7.ATOM[P[js][1]][0], 'd': P[js][2], 'teks': teks(*P[js][1:]), 'skor_a': float(pl['skor_a'][js]),
                        'simpan_a': float(pl['simpan_a'][js]), 'positif_a': int(pl['positif_a'][js]), 'n_setup_a': pl['n_setup_a']},
            'peraturan': len(P), 'takrif_trend': len(TREND), 'setup': len(S),
            'a_peraturan_skor_positif': int((pl['skor_a'] > 0).sum()),
            'sendiri_x00': int(sum(v is None for v in pl['sendiri'].values()))}
    with open(os.path.join(KELUAR, 'meta.json'), 'w') as f:
        json.dump(meta, f, indent=1, ensure_ascii=False)
    cari.log(f"CS09: {len(S)} setup; U* = {meta['sejagat']['teks']} (skor A {meta['sejagat']['skor_a'] * 100:+.2f} mata)")


# ---------- laporan ----------
def lapor():
    G = pd.read_csv(os.path.join(KELUAR, 'takrif.csv'))
    S = pd.read_csv(os.path.join(KELUAR, 'setup.csv'))
    with open(os.path.join(KELUAR, 'meta.json')) as f:
        meta = json.load(f)
    try:
        sys.path.insert(0, os.path.join(BS2, 'standard'))
        import status_kad
        status = status_kad.baris()
    except Exception:
        status = '> **Status keputusan:** lihat `laporan/KAD_SKOR.md`; laporan ini BUKAN keputusan.'
    p = lambda x, k=1, t=False: '–' if x != x else (f'{x * 100:+.{k}f}' if t else f'{x * 100:.{k}f}')
    Y = S[S.dipercayai]
    u = meta['sejagat']
    n, ny, nt = len(S), len(Y), len(G)

    def ringkas(nama, D):
        return (f"| {nama} | {p(D['x00_purata'].median(), 2, True)} → {p(D['sejagat_purata'].median(), 2, True)} | "
                f"{p(D['x00_menang'].median())} → {p(D['sejagat_menang'].median())} | "
                f"{p(D['x00_rugi8'].median())} → {p(D['sejagat_rugi8'].median())} | "
                f"{p(D['x00_rugi15'].median())} → {p(D['sejagat_rugi15'].median())} | "
                f"{p(D['x00_tp'].median())} → {p(D['sejagat_tp'].median())} | "
                f"{p(D['x00_R_pelari'].median())} → {p(D['sejagat_R_pelari'].median())} | "
                f"{p(D['sejagat_jual'].median())} | {D['x00_pegang'].median():.1f} → {D['sejagat_pegang'].median():.1f} | "
                f"{int(D['sejagat_ditolong'].sum())} / {len(D)} |")

    teguh = int((G.d_purata > 0).sum())
    menolong = bool(Y.sejagat_ditolong.sum() > ny / 2 and (Y.sejagat_purata - Y.x00_purata).median() > 0)
    A = ['# CS09 — keluar ikut kata pengguna: pegang selagi untung; jual hanya jika RUGI dan trend PATAH (backtest; BUKAN bukti)',
         '', status, '',
         'Dijana `kajian/carian_setup/cs_keluar9.py`. Pradaftar: `kajian/SPEC_CARIAN_SETUP.md` pindaan 15 Nov 2026 (v), dikomit '
         'sebelum dijalankan. **Jangan sunting secara manual.**', '',
         '## 1. Jawapan', '',
         f'- **Peraturan sejagat U\\*** (dipilih pada kumpulan A sahaja): **{u["teks"]}** → jual pada buka sesi berikutnya. '
         f'Skor kumpulan A {u["skor_a"] * 100:+.2f} mata purata; positif bagi {u["positif_a"]} daripada {u["n_setup_a"]} setup; '
         f'simpan pelari {u["simpan_a"]:.2f}.',
         f'- **Bacaan dikunci:** peraturan pengguna {"MENOLONG" if menolong else "TIDAK menolong"} '
         f'({int(Y.sejagat_ditolong.sum())} daripada {ny} setup dipercayai ditolong pada kumpulan B; median beza purata '
         f'{p((Y.sejagat_purata - Y.x00_purata).median(), 2, True)} mata). Idea itu {"TEGUH" if teguh > nt / 2 else "TIDAK teguh"}: '
         f'{teguh} daripada {nt} takrif "trend patah" mempunyai median beza purata > 0 (peringkat 1, tanpa pemilihan).', '',
         'Kumpulan B, median merentas setup: "pegang sahaja" (`X00`, henti sama) → dengan U\\*.', '',
         '| Setup | purata % | menang % | rugi ≥ 8 % | rugi ≥ 15 % | tangkap penuh % | untung pelari % | dijual oleh U\\* % | '
         'sesi pegang | ditolong |', '|' + '---|' * 10,
         ringkas(f'semua ({n})', S), ringkas(f'dipercayai ({ny})', Y), '',
         '## 2. Adakah gabungan DAN itu yang bekerja? (kumpulan B, median beza lawan `X00`, mata)', '',
         '| Keluar | purata | menang | rugi ≥ 8 % | rugi ≥ 15 % | tangkap penuh | untung pelari | setup ditolong |', '|' + '---|' * 8]
    for nama, t in (('sejagat', f'U\\* ({u["teks"]})'), ('rugi_sahaja', '"rugi → jual" sahaja (tanpa syarat trend)'),
                    ('trend_sahaja', '"trend patah → jual" sahaja (walaupun untung)'), ('daftar', 'keluar berdaftar setup'),
                    ('sendiri', 'pilihan setiap setup (kumpulan A)')):
        dd = lambda k: (S[f'{nama}_{k}'] - S[f'x00_{k}']).median()
        A.append(f"| {t} | {p(dd('purata'), 2, True)} | {p(dd('menang'), 1, True)} | {p(dd('rugi8'), 1, True)} | "
                 f"{p(dd('rugi15'), 1, True)} | {p(dd('tp'), 1, True)} | {p(dd('R_pelari'), 1, True)} | "
                 f"{int(S[f'{nama}_ditolong'].sum())} / {n} |")
    A += ['', f'Pilihan setiap setup: {meta["sendiri_x00"]} daripada {n} setup memilih `X00` pada kumpulan A (tiada peraturan dengan '
          'skor > 0 dan simpan ≥ 0.90).', '',
          '## 3. Peringkat 1: setiap takrif "trend patah" pada d = 3 (kumpulan B, tanpa pemilihan)', '',
          'Median beza lawan `X00` merentas setup (mata). simpan = untung pelari ÷ "pegang sahaja".', '',
          '| Trend patah | purata | purata (dipercayai) | menang | rugi ≥ 8 % | rugi ≥ 15 % | tangkap penuh | simpan | dijual % | '
          f'ditolong / {n} | dipercayai ditolong / {ny} | skor A |', '|' + '---|' * 12]
    for r in G.sort_values('d_purata', ascending=False).itertuples():
        A.append(f'| {r.trend_patah} | {p(r.d_purata, 2, True)} | {p(r.d_purata_dipercayai, 2, True)} | {p(r.d_menang, 1, True)} | '
                 f'{p(r.d_rugi8, 1, True)} | {p(r.d_rugi15, 1, True)} | {p(r.d_tp, 1, True)} | {r.simpan:.2f} | {p(r.d_jual)} | '
                 f'{int(r.ditolong)} | {int(r.ditolong_dipercayai)} | {p(r.skor_a, 2, True)} |')
    A += ['', '## 4. Setiap setup dengan U\\* (kumpulan B)', '',
          '| ID | ked. | henti | belian | purata % X00 → U\\* | menang % | rugi ≥ 8 % | rugi ≥ 15 % | tangkap penuh % | '
          'untung pelari % | dijual U\\* % | ditolong |', '|' + '---|' * 12]
    for r in S.sort_values('kedudukan').itertuples():
        g = lambda k: f"{p(getattr(r, f'x00_{k}'), 1)} → {p(getattr(r, f'sejagat_{k}'), 1)}"
        A.append(f"| `{r.id}` | {r.kedudukan} | {r.henti} | {r.x00_n:,} | {p(r.x00_purata, 2, True)} → {p(r.sejagat_purata, 2, True)} | "
                 f"{g('menang')} | {g('rugi8')} | {g('rugi15')} | {g('tp')} | {g('R_pelari')} | {p(r.sejagat_jual)} | "
                 f"{'✓' if r.sejagat_ditolong else '✗'} |")
    A += ['', '## 5. Kaveat', '',
          '- Asas perbandingan ialah "pegang sahaja" dengan henti yang sama; angka `X00` di sini boleh berbeza sedikit daripada '
          '`KEDUDUKAN_AKHIR` bagi setup yang berdaftar dengan indikator keluar.',
          '- Kumpulan B sudah dipakai untuk memilih setup (audit (u)); bacaan peringkat 1 tidak memilih apa-apa, tetapi setup itu '
          'sendiri dipilih. Tiada saham delist. Ujian bersih = jejak hadapan.',
          '- Tiada kod F baharu dan tiada perubahan pangkat dalam pusingan ini.', '']
    with open(os.path.join(KELUAR, 'LAPORAN.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(A) + '\n')


if __name__ == '__main__':
    if sys.argv[1] != '--lapor':
        nilai(sys.argv[1])
    lapor()
