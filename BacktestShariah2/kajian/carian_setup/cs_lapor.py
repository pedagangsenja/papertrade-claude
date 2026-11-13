"""Carian setup CS01 — laporan: `kajian/CARIAN_SETUP.md` + `carian_setup/hasil/*.csv`.
Guna: python3 cs_lapor.py <kerja>   (selepas cari.py besar, tepat, kunci). Jangan sunting keluaran secara manual."""
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
import cs_teras as teras  # noqa: E402

BS2 = os.path.normpath(os.path.join(SINI, '..', '..'))
sys.path.insert(0, os.path.join(BS2, 'standard'))
TEMPOH = ['Latih', 'Sah', 'K1', 'K2']
TERANG = {'Latih': 'Latih (set 431, 2020 – Jun 2023)', 'Sah': 'Sah (set 431, Jul 2023 – Ogo 2026)',
          'K1': 'Kunci K1 (saham lain, 2010–2019)', 'K2': 'Kunci K2 (saham lain, 2020 – Ogo 2026)'}


def nama_pencetus(n, kerja):
    if n.startswith('P'):
        return next(x for x in atom.PENCETUS if x.startswith(n))
    if n.startswith('N'):
        reg = pd.read_csv(os.path.join(BS2, 'data', 'registry_N.csv')).set_index('id')
        return f"{n} {reg.nama.get(n, '')} (benih N)".replace('  ', ' ')
    mid, v = n.split('.')
    reg = pd.read_csv(os.path.join(BS2, 'data', 'registry_M_gabung.csv')).drop_duplicates('id').set_index('id')
    asas = f"{mid} {reg.kaedah.get(mid, '')}"
    if v == '0':
        return f'{asas} (benih M, parameter asal)'
    P = pickle.load(open(os.path.join(kerja, 'benih_431.pkl'), 'rb'))['param'].get(n) or {}
    return f"{asas} (benih M, varian {v}: " + ', '.join(f'{k}={round(x, 3)}' for k, x in P.items()) + ')'


def terang(r, kerja):
    s, x = divmod(int(r.lajur), cari.NR)
    pen = [atom.PENAPIS[f] for f in (r.f1, r.f2) if f >= 0]
    return {'masuk': nama_pencetus(r.pencetus, kerja), 'penapis': ' DAN '.join(pen) if pen else 'tiada',
            'henti': atom.HENTI[s], 'keluar': teras.nama_keluar(x, cari.A1, cari.A2, cari.OP, atom.KELUAR)}


REG_F = os.path.join(BS2, 'data', 'registry_F.csv')
LAJUR_F = ['id', 'keluarga', 'pusingan', 'tarikh_daftar', 'takrif', 'param', 'masuk', 'penapis', 'henti', 'keluar',
           'skor_tepat', 'n_Latih', 'purata_Latih', 'n_Sah', 'purata_Sah', 'n_K1', 'purata_K1', 'n_K2', 'purata_K2',
           'k10_K1', 'k10_K2', 'T1', 'T2', 'T3', 'status']


def takrif(r):
    """Takrif kanonik satu setup (boleh dibaca mesin): pencetus|penapis|henti|keluar."""
    s, x = divmod(int(r.lajur), cari.NR)
    pen = '+'.join(atom.PENAPIS[f][:3] for f in (r.f1, r.f2) if f >= 0) or '-'
    a, b, op = cari.A1[x], cari.A2[x], cari.OP[x]
    kel = 'X00' if op == 0 else atom.KELUAR[a][:3] if op == 1 else (
        f"{atom.KELUAR[a][:3]} {'ATAU' if op == 2 else 'DAN'} {atom.KELUAR[b][:3]}")
    return f'{r.pencetus}|{pen}|{atom.HENTI[s][:2]}|{kel}'


def daftar_f(ringkas, kerja, pusingan='CS01'):
    """Keluarga F (keputusan pengguna 13 Nov 2026): setiap setup papan mendapat ID Fxx yang KEKAL.
    Takrif yang sudah berdaftar mengekalkan ID-nya; takrif baharu mendapat nombor seterusnya ikut kedudukan papan.
    Status BACKTEST = belum papertrade (tiada modul `kod/kaedah/`, tiada dalam Lejar)."""
    reg = pd.read_csv(REG_F, dtype=str).fillna('') if os.path.exists(REG_F) else pd.DataFrame(columns=LAJUR_F)
    param = pickle.load(open(os.path.join(kerja, 'benih_431.pkl'), 'rb'))['param']
    idf = {}
    for kd, d, r, v, T1, T2, T3, pct, t1 in ringkas:
        tk = takrif(r)
        lama = reg[reg.takrif == tk]
        if len(lama):
            fid = lama.id.iloc[0]
            reg = reg[reg.takrif != tk]
            tarikh = lama.tarikh_daftar.iloc[0]
        else:
            n = max([int(x[1:]) for x in list(reg.id) + list(idf.values())] or [0]) + 1
            fid, tarikh = f'F{n:02d}', pd.Timestamp.now().strftime('%Y-%m-%d')
        idf[kd] = fid
        P = param.get(r.pencetus)
        b = {'id': fid, 'keluarga': 'F', 'pusingan': pusingan, 'tarikh_daftar': tarikh, 'takrif': tk,
             'param': json.dumps({k: round(x, 6) for k, x in P.items()}, sort_keys=True) if P else '',
             **d, 'skor_tepat': f'{r.skor_tepat:.5f}', 'T1': T1, 'T2': T2, 'T3': T3, 'status': 'BACKTEST'}
        for t in TEMPOH:
            b[f'n_{t}'] = v[t]['n']
            b[f'purata_{t}'] = '' if not v[t]['n'] else f"{v[t]['purata']:.5f}"
        for t in ('K1', 'K2'):
            b[f'k10_{t}'] = '' if not v[t]['n'] else f"{v[t].get('k10', float('nan')):.4f}"
        reg = pd.concat([reg, pd.DataFrame([b])[LAJUR_F].astype(str)], ignore_index=True)
    reg['_n'] = reg.id.str[1:].astype(int)
    reg.sort_values('_n').drop(columns='_n').to_csv(REG_F, index=False)
    return idf


def gabung_kunci(v):
    n = v['K1']['n'] + v['K2']['n']  # K1 dan K2 sentiasa hadir bersama
    if n == 0:
        return 0, np.nan
    return n, sum(v[k]['n'] * v[k]['purata'] for k in ('K1', 'K2') if v[k]['n']) / n


def p(x, d=1, tanda=False):
    if x is None or (isinstance(x, float) and np.isnan(x)):
        return '–'
    return f'{x * 100:+.{d}f}' if tanda else f'{x * 100:.{d}f}'


def main(kerja):
    P = pd.read_pickle(os.path.join(kerja, 'pilihan.pkl'))
    KV = pickle.load(open(os.path.join(kerja, 'kunci.pkl'), 'rb'))
    meta = json.load(open(os.path.join(kerja, 'besar_meta.json')))
    ralat_kunci = KV.pop('_ralat_benih_kunci', {})
    P['n_kunci'], P['pur_kunci'] = zip(*[gabung_kunci(KV[k]) if k in KV and 'K1' in KV[k] else (0, np.nan)
                                         for k in range(len(P))])
    for t in ('K1', 'K2'):
        P[f'n_{t}'] = [KV.get(k, {}).get(t, {}).get('n', 0) for k in range(len(P))]
        P[f'pur_{t}'] = [KV.get(k, {}).get(t, {}).get('purata', np.nan) for k in range(len(P))]
    rawak = P[(P.peranan == 'rawak') & (P.n_kunci >= 30)]
    atas = P[(P.peranan != 'rawak') & (P.n_kunci >= 30)]
    p95 = float(rawak.pur_kunci.quantile(0.95))
    rho = float(atas[['skor_tepat', 'pur_kunci']].corr(method='spearman').iloc[0, 1])
    papan = P[P.peranan == 'papan']

    os.makedirs(os.path.join(SINI, 'hasil'), exist_ok=True)
    baris_csv, ringkas = [], []
    for kedudukan, (k, r) in enumerate(papan.iterrows(), 1):
        d, v = terang(r, kerja), KV[k]
        for t in TEMPOH:
            v.setdefault(t, {'n': 0, 'purata': float('nan')})
        t1 = v.get('t1', [])
        T1 = bool(t1) and all(x == x and x > 0 for x in t1)
        T2 = v['K1']['n'] > 0 and v['K2']['n'] > 0 and v['K1']['purata'] > 0 and v['K2']['purata'] > 0
        T3 = r.n_kunci >= 30 and r.pur_kunci > p95
        pct = float((rawak.pur_kunci < r.pur_kunci).mean()) if r.n_kunci >= 30 else np.nan
        ringkas.append((kedudukan, d, r, v, T1, T2, T3, pct, t1))
        for t in TEMPOH:
            baris_csv.append({'kedudukan': kedudukan, **d, 'skor_tepat': r.skor_tepat, 'tempoh': t, **v[t],
                              'T1': T1, 'T2': T2, 'T3': T3, 'persentil_lawan_rawak': pct})
    idf = daftar_f(ringkas, kerja)
    for x in baris_csv:
        x['id'] = idf[x['kedudukan']]
    pd.DataFrame(baris_csv).to_csv(os.path.join(SINI, 'hasil', 'papan.csv'), index=False, float_format='%.5f')
    S = P.copy()
    for kol in ('masuk', 'penapis', 'henti', 'keluar'):
        S[kol] = [terang(r, kerja)[kol] for r in P.itertuples()]
    S[['peranan', 'masuk', 'penapis', 'henti', 'keluar', 'skor_tepat', 'nt_L', 'purt_L', 'nt_S', 'purt_S', 'n_K1',
       'pur_K1', 'n_K2', 'pur_K2', 'n_kunci', 'pur_kunci']].to_csv(
        os.path.join(SINI, 'hasil', 'senarai_kunci.csv'), index=False, float_format='%.5f')
    hist = np.asarray(meta['hist'])
    positif = float(hist[np.searchsorted(cari.TEPI, 0.0) + 1:].sum() / max(hist.sum(), 1))
    ringkas_meta = {k: meta[k] for k in ('pencetus', 'pencetus_cukup', 'masuk_dicuba', 'masuk_diskor', 'K',
                                         'kombinasi_dicuba', 'kombinasi_diskor', 'saat')}
    ringkas_meta.update(bahagian_skor_positif=positif, spearman_skor_lawan_kunci=rho, p95_rawak_kunci=p95,
                        median_rawak_kunci=float(rawak.pur_kunci.median()),
                        median_atas200_kunci=float(atas.pur_kunci.median()),
                        ralat_benih_431=meta.get('ralat_benih', {}), ralat_benih_kunci=ralat_kunci)
    json.dump(ringkas_meta, open(os.path.join(SINI, 'hasil', 'meta.json'), 'w'), indent=1)

    try:
        import status_kad
        status = status_kad.baris()
    except Exception:
        status = '> **Status keputusan:** lihat `laporan/KAD_SKOR.md`; laporan ini BUKAN keputusan.'
    A = ['# Carian Setup CS01 — papan 10 teratas (backtest, BUKAN bukti)', '', status, '',
         'Dijana `kajian/carian_setup/cs_lapor.py`. Pradaftar: `kajian/SPEC_CARIAN_SETUP.md` (13 Nov 2026, dikomit '
         'sebelum keputusan dilihat). **Jangan sunting secara manual.**', '',
         '## 1. Apa yang dicari', '',
         'Setup lengkap (masuk, pegang, keluar) yang menangkap saham ketika ia mula naik kuat dan memegangnya '
         'selagi naik. Syarat wajib: swing paling lama 20 sesi, tiada jual pada hari beli, henti rugi longgar, '
         'tiada sasaran untung tetap, keluar ikut indikator. Kos 0.5 % pusingan sudah ditolak.', '',
         '## 2. Saiz carian', '',
         f"- Pencetus masuk: {meta['pencetus']} (49 indikator + benih M asal dan dua varian parameter + benih N); "
         f"{meta['pencetus_cukup']} cukup isyarat.",
         f"- Peraturan masuk (pencetus × 0–2 penapis): {meta['masuk_dicuba']:,} dicuba, "
         f"{meta['masuk_diskor']:,} cukup dagangan (≥ 100 dalam Latih dan Sah).",
         f"- Setiap satu × {meta['K']:,} gabungan henti × keluar: **{meta['kombinasi_diskor']:,} kombinasi diskor** "
         f"(daripada {meta['kombinasi_dicuba']:,} dicuba) dalam {meta['saat'] / 60:.0f} minit.",
         f'- {positif * 100:.1f} % kombinasi diskor mempunyai had bawah positif dalam Latih DAN Sah.', '',
         '## 3. Papan 10 teratas', '',
         'Pangkat ikut `skor tepat` (had bawah purata untung, yang lebih rendah antara Latih dan Sah). **Kunci** ialah '
         '1,000 saham lain yang carian tidak pernah lihat; ia dilaporkan sahaja dan tidak mengubah pangkat.', '',
         'Setiap setup papan didaftarkan dalam keluarga **F** (`data/registry_F.csv`, ID kekal; status BACKTEST = '
         'belum papertrade).', '',
         '| # | ID | Masuk | Penapis | Henti | Keluar | Skor | Kunci: dagangan | Kunci: purata % | Lawan rawak | T1 | T2 | T3 |',
         '|---|---|---|---|---|---|---|---|---|---|---|---|---|']
    ya = lambda b: '✓' if b else '✗'
    for kd, d, r, v, T1, T2, T3, pct, t1 in ringkas:
        A.append(f"| {kd} | `{idf[kd]}` | {d['masuk']} | {d['penapis']} | {d['henti']} | {d['keluar']} | {p(r.skor_tepat, 2, True)} "
                 f"| {r.n_kunci:,} | {p(r.pur_kunci, 2, True)} | persentil {p(pct, 0)} | {ya(T1)} | {ya(T2)} | {ya(T3)} |")
    A += ['', '- **T1 tahan:** skor positif pada keempat-empat pilihan henti. **T2 tidak dilihat:** purata positif '
          'dalam K1 dan K2. **T3 kalahkan rawak:** purata Kunci melebihi persentil ke-95 setup rawak '
          f'({p(p95, 2, True)} %).',
          '- "Lawan rawak" = peratus daripada 200 setup yang dipilih rawak daripada ruang yang sama yang puratanya '
          'pada Kunci lebih rendah.', '', '### Butiran setiap setup', '']
    for kd, d, r, v, T1, T2, T3, pct, t1 in ringkas:
        A += [f"**#{kd}. `{idf[kd]}` — {d['masuk']}**", '',
              f"Penapis: {d['penapis']} · Henti: {d['henti']} · Keluar: {d['keluar']}", '',
              '| Tempoh | Dagangan | Purata % | Menang % | ≥ +10 % | ≥ +20 % | Rugi ≤ −8 % | Naik 5 % minggu 1 | '
              'Pegang (sesi) | Purata seminggu % | Lebihan atas rawak hari sama | MDD buku % |',
              '|---|---|---|---|---|---|---|---|---|---|---|---|']
        for t in TEMPOH:
            x = v[t]
            if not x['n']:
                A.append(f'| {TERANG[t]} | 0 | – | – | – | – | – | – | – | – | – | – |')
                continue
            A.append(f"| {TERANG[t]} | {x['n']:,} | {p(x['purata'], 2, True)} | {p(x.get('menang'))} | "
                     f"{p(x.get('k10'))} | {p(x.get('k20'))} | {p(x.get('rugi8'))} | {p(x.get('k5m1'))} | "
                     f"{x.get('pegang', float('nan')):.1f} | {p(x.get('seminggu'), 2, True)} | "
                     f"{p(x.get('lebihan'), 2, True)} | {p(x.get('mdd'), 1)} |")
        A += ['', 'Skor pada empat pilihan henti (H1–H4): ' + ' · '.join(p(x, 2, True) for x in t1), '']
    A += ['## 4. Semakan kejujuran', '',
          '| Ukuran | Nilai |', '|---|---|',
          f'| Spearman `skor tepat` lawan purata Kunci, {len(atas)} setup teratas | {rho:+.2f} |',
          f'| Median purata Kunci, setup teratas | {p(atas.pur_kunci.median(), 2, True)} % |',
          f'| Median purata Kunci, {len(rawak)} setup rawak | {p(rawak.pur_kunci.median(), 2, True)} % |',
          f'| Persentil ke-95 purata Kunci, setup rawak | {p(p95, 2, True)} % |',
          f"| Setup teratas yang purata Kunci-nya melebihi persentil ke-95 rawak | "
          f"{int((atas.pur_kunci > p95).sum())} daripada {len(atas)} |",
          f"| Setup teratas dengan purata Kunci positif | {int((atas.pur_kunci > 0).sum())} daripada {len(atas)} |",
          f"| Setup rawak dengan purata Kunci positif | {int((rawak.pur_kunci > 0).sum())} daripada {len(rawak)} |",
          '',
          'Bacaan: Spearman positif dan median teratas melebihi median rawak bermakna pangkat carian membawa '
          'maklumat ke saham yang tidak dilihat. Spearman sekitar sifar atau median yang sama bermakna papan ini '
          'tidak dapat dibezakan daripada pilihan rawak.', '',
          '## 5. Kaveat', '',
          '- Backtest sahaja. Tiada setup di sini masuk papertrade tanpa keputusan pengguna yang berasingan; kad '
          'skor kekal satu-satunya keputusan wang sebenar.',
          '- Tiada saham delist dalam kedua-dua set: semua angka condong ke atas. K2 berkongsi tahun dengan '
          'Latih/Sah (saham berbeza, pasaran sama); K1 berbeza saham dan tahun.',
          '- Peringkat besar membenarkan isyarat bertindih; angka papan dikira semula dengan satu posisi setiap '
          'saham. MDD buku = semua posisi sama berat, bukan portfolio berslot.',
          '- Benih M yang bergantung pada saham lain (persentil RS) dikira dalam alam masing-masing.',
          f"- Benih gagal dijalankan: set 431 {len(meta.get('ralat_benih', {}))}, Kunci {len(ralat_kunci)} "
          '(senarai dalam `carian_setup/hasil/meta.json`).', '',
          '## 6. Jana semula', '',
          '```', 'W=<folder kerja di luar repo>', 'cd BacktestShariah2/kajian/carian_setup',
          'python3 cs_cari.py panel $W 431 && python3 cs_cari.py benih $W 431 && python3 cs_cari.py besar $W',
          'python3 cs_cari.py tepat $W && python3 cs_cari.py panel $W kunci && python3 cs_cari.py kunci $W',
          'python3 cs_lapor.py $W', '```', '']
    open(os.path.join(BS2, 'kajian', 'CARIAN_SETUP.md'), 'w', encoding='utf-8').write('\n'.join(A))
    print('laporan ditulis:', len(papan), 'setup papan; rho', round(rho, 3), 'p95 rawak', round(p95, 4))


if __name__ == '__main__':
    main(sys.argv[1])
