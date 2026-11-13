"""Carian setup — laporan setiap pusingan: `carian_setup/hasil/<pusingan>/` (LAPORAN.md, papan.csv,
senarai_kunci.csv, meta.json), `data/registry_F.csv` dan, kecuali `arkib`, `kajian/CARIAN_SETUP.md` (pusingan terkini).
Guna: python3 cs_lapor.py <kerja> <pusingan> [arkib]   (selepas cs_cari.py besar, tepat, kunci).
Jangan sunting keluaran secara manual."""
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
REG_F = os.path.join(BS2, 'data', 'registry_F.csv')
LAJUR_F = ['id', 'keluarga', 'pusingan', 'tarikh_daftar', 'takrif', 'param', 'masuk', 'penapis', 'henti', 'keluar',
           'skor_tepat', 'n_cari1', 'purata_cari1', 'n_cari2', 'purata_cari2', 'n_K1', 'purata_K1', 'n_K2',
           'purata_K2', 'n_K3', 'purata_K3', 'k10_K1', 'k10_K2', 'k10_K3', 'T1', 'T2', 'T3', 'status']
# Setiap pusingan: penerangan tempoh, tempoh Kunci yang TAHUNNYA tidak dipakai carian (`bebas`), dan kaveat khusus.
KONFIG = {
    'CS01': {
        'terang': {'Latih': 'Latih (set 431, 2020 – Jun 2023)', 'Sah': 'Sah (set 431, Jul 2023 – Ogo 2026)',
                   'K1': 'Kunci K1 (saham lain, 2010–2019)', 'K2': 'Kunci K2 (saham lain, 2020 – Ogo 2026)'},
        'cari': 'set 431', 'kunci': '1,000 saham lain yang carian tidak pernah lihat', 'bebas': ['K1'],
        'nota_bebas': '**K1 ialah ujian sebenar** (saham lain DAN tahun lain). K2 berkongsi tahun 2020–2026 dengan '
                      'carian, jadi ia hanya menunjukkan setup itu berfungsi pada saham lain dalam pasaran yang sama.',
        'kaveat': ['Tiada saham delist dalam kedua-dua set: semua angka condong ke atas. K2 berkongsi tahun dengan '
                   'Latih/Sah (saham berbeza, pasaran sama); K1 berbeza saham dan tahun.'],
    },
    'CS02': {
        'terang': {'E1': 'Cari E1 (kumpulan A, 2010–2019)', 'E2': 'Cari E2 (kumpulan A, 2020–2024)',
                   'K1': 'Kunci K1 (kumpulan B, 2010–2019)', 'K2': 'Kunci K2 (kumpulan B, 2020–2024)',
                   'K3': 'Kunci K3 (kumpulan B, 2025 – Ogo 2026)'},
        'cari': 'kumpulan A set 2000 (dua era: 2010–2019 dan 2020–2024)',
        'kunci': 'kumpulan B set 2000: saham yang carian tidak pernah lihat', 'bebas': ['K3'],
        'nota_bebas': '**K3 ialah ujian sebenar** (saham lain DAN tahun yang tidak dipakai carian: 2025 – Ogo 2026). '
                      'K1 dan K2 berkongsi tahun dengan carian, jadi ia hanya menunjukkan setup itu berfungsi pada '
                      'saham lain dalam pasaran yang sama.',
        'kaveat': ['Tiada saham delist dalam set 2000: semua angka condong ke atas. Set ini bukan tapisan Shariah.',
                   'Reka bentuk dua era dipilih selepas melihat CS01. Kumpulan A dan B merangkumi saham set 431 dan '
                   'saham Kunci CS01, dan K3 bertindih dengan tempoh Sah CS01; K3 bersih bagi pemilihan CS02 sahaja.'],
    },
}


def tempoh(pus):
    c, k = cari.PUSINGAN[pus]
    return [t[0] for t in atom.TEMPOH[c]], [t[0] for t in atom.TEMPOH[k]]


def nama_pencetus(n, param):
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
    P = param.get(n) or {}
    return f"{asas} (benih M, varian {v}: " + ', '.join(f'{k}={round(x, 3)}' for k, x in P.items()) + ')'


def terang(r, param):
    s, x = divmod(int(r.lajur), cari.NR)
    pen = [atom.PENAPIS[f] for f in (r.f1, r.f2) if f >= 0]
    return {'masuk': nama_pencetus(r.pencetus, param), 'penapis': ' DAN '.join(pen) if pen else 'tiada',
            'henti': atom.HENTI[s], 'keluar': teras.nama_keluar(x, cari.A1, cari.A2, cari.OP, atom.KELUAR)}


def takrif(r):
    """Takrif kanonik satu setup (boleh dibaca mesin): pencetus|penapis|henti|keluar."""
    s, x = divmod(int(r.lajur), cari.NR)
    pen = '+'.join(atom.PENAPIS[f][:3] for f in (r.f1, r.f2) if f >= 0) or '-'
    a, b, op = cari.A1[x], cari.A2[x], cari.OP[x]
    kel = 'X00' if op == 0 else atom.KELUAR[a][:3] if op == 1 else (
        f"{atom.KELUAR[a][:3]} {'ATAU' if op == 2 else 'DAN'} {atom.KELUAR[b][:3]}")
    return f'{r.pencetus}|{pen}|{atom.HENTI[s][:2]}|{kel}'


def daftar_f(ringkas, param, pus, T_cari, T_kunci):
    """Keluarga F (keputusan pengguna 13 Nov 2026): setiap setup papan mendapat ID Fxx yang KEKAL.
    Takrif yang sudah berdaftar mengekalkan ID dan tarikhnya (ukuran dikemas kini ke pusingan ini); takrif baharu
    mendapat nombor seterusnya ikut kedudukan papan. Status BACKTEST = belum papertrade."""
    if os.path.exists(REG_F):
        reg = pd.read_csv(REG_F, dtype=str).fillna('').rename(columns={
            'n_Latih': 'n_cari1', 'purata_Latih': 'purata_cari1', 'n_Sah': 'n_cari2', 'purata_Sah': 'purata_cari2'})
        reg = reg.reindex(columns=LAJUR_F, fill_value='')
    else:
        reg = pd.DataFrame(columns=LAJUR_F)
    idf = {}
    for kd, d, r, v, T1, T2, T3, pct, t1 in ringkas:
        tk = takrif(r)
        lama = reg[reg.takrif == tk]
        if len(lama):
            fid, tarikh = lama.id.iloc[0], lama.tarikh_daftar.iloc[0]
            reg = reg[reg.takrif != tk]
        else:
            n = max([int(x[1:]) for x in list(reg.id) + list(idf.values())] or [0]) + 1
            fid, tarikh = f'F{n:02d}', pd.Timestamp.now().strftime('%Y-%m-%d')
        idf[kd] = fid
        P = param.get(r.pencetus)
        b = dict.fromkeys(LAJUR_F, '')
        b.update(id=fid, keluarga='F', pusingan=pus, tarikh_daftar=tarikh, takrif=tk,
                 param=json.dumps({k: round(x, 6) for k, x in P.items()}, sort_keys=True) if P else '',
                 **d, skor_tepat=f'{r.skor_tepat:.5f}', T1=T1, T2=T2, T3=T3, status='BACKTEST')
        for i, t in enumerate(T_cari, 1):
            b[f'n_cari{i}'] = v[t]['n']
            b[f'purata_cari{i}'] = '' if not v[t]['n'] else f"{v[t]['purata']:.5f}"
        for t in T_kunci:
            b[f'n_{t}'] = v[t]['n']
            b[f'purata_{t}'] = '' if not v[t]['n'] else f"{v[t]['purata']:.5f}"
            b[f'k10_{t}'] = '' if not v[t]['n'] else f"{v[t].get('k10', float('nan')):.4f}"
        reg = pd.concat([reg, pd.DataFrame([b])[LAJUR_F].astype(str)], ignore_index=True)
    reg['_n'] = reg.id.str[1:].astype(int)
    reg.sort_values('_n').drop(columns='_n').to_csv(REG_F, index=False)
    return idf


def p(x, d=1, tanda=False):
    if x is None or (isinstance(x, float) and np.isnan(x)):
        return '–'
    return f'{x * 100:+.{d}f}' if tanda else f'{x * 100:.{d}f}'


def main(kerja, pus, arkib=False):
    K = KONFIG[pus]
    T_cari, T_kunci = tempoh(pus)
    TEMPOH = T_cari + T_kunci
    P = pd.read_pickle(os.path.join(kerja, 'pilihan.pkl'))
    KV = pickle.load(open(os.path.join(kerja, 'kunci.pkl'), 'rb'))
    meta = json.load(open(os.path.join(kerja, 'besar_meta.json')))
    param = pickle.load(open(os.path.join(kerja, f'benih_{cari.PUSINGAN[pus][0]}.pkl'), 'rb'))['param']
    ralat_kunci = KV.pop('_ralat_benih_kunci', {})
    kosong = {'n': 0, 'purata': float('nan')}
    for k in range(len(P)):
        for t in TEMPOH:
            KV.setdefault(k, {}).setdefault(t, dict(kosong))
    for t in T_kunci:
        P[f'n_{t}'] = [KV[k][t]['n'] for k in range(len(P))]
        P[f'pur_{t}'] = [KV[k][t]['purata'] for k in range(len(P))]
    P['n_kunci'] = sum(P[f'n_{t}'] for t in T_kunci)
    P['pur_kunci'] = sum(P[f'n_{t}'] * P[f'pur_{t}'].fillna(0) for t in T_kunci) / P.n_kunci.replace(0, np.nan)
    rawak = P[(P.peranan == 'rawak') & (P.n_kunci >= 30)]
    atas = P[(P.peranan != 'rawak') & (P.n_kunci >= 30)]
    p95 = float(rawak.pur_kunci.quantile(0.95))
    rho = float(atas[['skor_tepat', 'pur_kunci']].corr(method='spearman').iloc[0, 1])
    papan = P[P.peranan == 'papan']

    keluar_dir = os.path.join(SINI, 'hasil', pus)
    os.makedirs(keluar_dir, exist_ok=True)
    baris_csv, ringkas = [], []
    for kedudukan, (k, r) in enumerate(papan.iterrows(), 1):
        d, v = terang(r, param), KV[k]
        t1 = v.get('t1', [])
        T1 = bool(t1) and all(x == x and x > 0 for x in t1)
        T2 = all(v[t]['n'] > 0 and v[t]['purata'] > 0 for t in T_kunci)
        T3 = bool(r.n_kunci >= 30 and r.pur_kunci > p95)
        pct = float((rawak.pur_kunci < r.pur_kunci).mean()) if r.n_kunci >= 30 else np.nan
        ringkas.append((kedudukan, d, r, v, T1, T2, T3, pct, t1))
        for t in TEMPOH:
            baris_csv.append({'kedudukan': kedudukan, **d, 'skor_tepat': r.skor_tepat, 'tempoh': t, **v[t],
                              'T1': T1, 'T2': T2, 'T3': T3, 'persentil_lawan_rawak': pct})
    idf = daftar_f(ringkas, param, pus, T_cari, T_kunci)
    for x in baris_csv:
        x['id'] = idf[x['kedudukan']]
    pd.DataFrame(baris_csv).to_csv(os.path.join(keluar_dir, 'papan.csv'), index=False, float_format='%.5f')
    S = P.copy()
    for kol in ('masuk', 'penapis', 'henti', 'keluar'):
        S[kol] = [terang(r, param)[kol] for r in P.itertuples()]
    S[['peranan', 'masuk', 'penapis', 'henti', 'keluar', 'skor_tepat', 'nt_L', 'purt_L', 'nt_S', 'purt_S']
      + [f'{a}_{t}' for t in T_kunci for a in ('n', 'pur')] + ['n_kunci', 'pur_kunci']].to_csv(
        os.path.join(keluar_dir, 'senarai_kunci.csv'), index=False, float_format='%.5f')

    def era(t):
        ka, kr = atas[atas[f'n_{t}'] >= 30], rawak[rawak[f'n_{t}'] >= 30]
        return {'atas': ka[f'pur_{t}'], 'rawak': kr[f'pur_{t}'], 'p95': float(kr[f'pur_{t}'].quantile(0.95)),
                'rho': float(ka[['skor_tepat', f'pur_{t}']].corr(method='spearman').iloc[0, 1])}

    E = {t: era(t) for t in T_kunci}
    hist = np.asarray(meta['hist'])
    positif = float(hist[np.searchsorted(cari.TEPI, 0.0) + 1:].sum() / max(hist.sum(), 1))
    h4 = int(atas.lajur.map(lambda x: int(x) // cari.NR == 3).sum())
    atr4 = int(atas.apply(lambda r: 22 in (r.f1, r.f2), axis=1).sum())
    pegang = float(np.mean([v[t]['pegang'] for _, _, _, v, *_ in ringkas for t in T_kunci if v[t]['n']]))
    tahan = all(float(E[t]['atas'].median()) > max(E[t]['p95'], 0) for t in K['bebas'])
    ringkas_meta = {k: meta[k] for k in ('pencetus', 'pencetus_cukup', 'masuk_dicuba', 'masuk_diskor', 'K',
                                         'kombinasi_dicuba', 'kombinasi_diskor', 'saat')}
    ringkas_meta.update(pusingan=pus, bahagian_skor_positif=positif, spearman_skor_lawan_kunci=rho,
                        p95_rawak_kunci=p95, median_rawak_kunci=float(rawak.pur_kunci.median()),
                        median_atas_kunci=float(atas.pur_kunci.median()), atas_henti_H4=h4, atas_penapis_ATR4=atr4,
                        tahan_tempoh_bebas=tahan,
                        **{f'median_atas_{t}': float(E[t]['atas'].median()) for t in T_kunci},
                        **{f'median_rawak_{t}': float(E[t]['rawak'].median()) for t in T_kunci},
                        **{f'spearman_{t}': E[t]['rho'] for t in T_kunci},
                        ralat_benih_cari=meta.get('ralat_benih', {}), ralat_benih_kunci=ralat_kunci)
    json.dump(ringkas_meta, open(os.path.join(keluar_dir, 'meta.json'), 'w'), indent=1)

    try:
        import status_kad
        status = status_kad.baris()
    except Exception:
        status = '> **Status keputusan:** lihat `laporan/KAD_SKOR.md`; laporan ini BUKAN keputusan.'
    ya = lambda b: '✓' if b else '✗'
    A = [f'# Carian Setup {pus} — papan 10 teratas (backtest, BUKAN bukti)', '', status, '',
         'Dijana `kajian/carian_setup/cs_lapor.py`. Pradaftar: `kajian/SPEC_CARIAN_SETUP.md` (13 Nov 2026, dikomit '
         'sebelum keputusan pusingan ini dilihat). **Jangan sunting secara manual.** Arkib setiap pusingan: '
         '`kajian/carian_setup/hasil/<pusingan>/LAPORAN.md`.', '',
         '## 1. Apa yang dicari', '',
         'Setup lengkap (masuk, pegang, keluar) yang menangkap saham ketika ia mula naik kuat dan memegangnya '
         'selagi naik. Syarat wajib: swing paling lama 20 sesi, tiada jual pada hari beli, henti rugi longgar, '
         'tiada sasaran untung tetap, keluar ikut indikator. Kos 0.5 % pusingan sudah ditolak.', '',
         f"Carian: {K['cari']}. Kunci: {K['kunci']}.", '',
         '## 2. Saiz carian', '',
         f"- Pencetus masuk: {meta['pencetus']} (49 indikator + benih M asal dan dua varian parameter + benih N); "
         f"{meta['pencetus_cukup']} cukup isyarat.",
         f"- Peraturan masuk (pencetus × 0–2 penapis): {meta['masuk_dicuba']:,} dicuba, "
         f"{meta['masuk_diskor']:,} cukup dagangan (≥ 100 dalam kedua-dua tempoh carian).",
         f"- Setiap satu × {meta['K']:,} gabungan henti × keluar: **{meta['kombinasi_diskor']:,} kombinasi diskor** "
         f"(daripada {meta['kombinasi_dicuba']:,} dicuba) dalam {meta['saat'] / 60:.0f} minit.",
         f'- {positif * 100:.1f} % kombinasi diskor mempunyai had bawah positif dalam kedua-dua tempoh carian.', '',
         '## 3. Papan 10 teratas', '',
         f'Pangkat ikut `skor tepat` (had bawah purata untung, yang lebih rendah antara {T_cari[0]} dan {T_cari[1]}). '
         '**Kunci** dilaporkan sahaja dan tidak mengubah pangkat.', '',
         'Setiap setup papan didaftarkan dalam keluarga **F** (`data/registry_F.csv`, ID kekal; status BACKTEST = '
         'belum papertrade).', '',
         '| # | ID | Masuk | Penapis | Henti | Keluar | Skor | '
         + ' | '.join(f'{t}: purata %' for t in T_kunci) + ' | Lawan rawak | T1 | T2 | T3 |',
         '|---' * (10 + len(T_kunci)) + '|']
    for kd, d, r, v, T1, T2, T3, pct, t1 in ringkas:
        A.append(f"| {kd} | `{idf[kd]}` | {d['masuk']} | {d['penapis']} | {d['henti']} | {d['keluar']} | "
                 f"{p(r.skor_tepat, 2, True)} | " + ' | '.join(p(v[t]['purata'], 2, True) for t in T_kunci)
                 + f" | persentil {p(pct, 0)} | {ya(T1)} | {ya(T2)} | {ya(T3)} |")
    A += ['', '- **T1 tahan:** skor positif pada keempat-empat pilihan henti. **T2 tidak dilihat:** purata positif '
          'dalam setiap tempoh Kunci. **T3 kalahkan rawak:** purata Kunci (semua tempoh) melebihi persentil ke-95 '
          f'setup rawak ({p(p95, 2, True)} %).',
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
                A.append(f"| {K['terang'][t]} | 0 | – | – | – | – | – | – | – | – | – | – |")
                continue
            A.append(f"| {K['terang'][t]} | {x['n']:,} | {p(x['purata'], 2, True)} | {p(x.get('menang'))} | "
                     f"{p(x.get('k10'))} | {p(x.get('k20'))} | {p(x.get('rugi8'))} | {p(x.get('k5m1'))} | "
                     f"{x.get('pegang', float('nan')):.1f} | {p(x.get('seminggu'), 2, True)} | "
                     f"{p(x.get('lebihan'), 2, True)} | {p(x.get('mdd'), 1)} |")
        A += ['', 'Skor pada empat pilihan henti (H1–H4): ' + ' · '.join(p(x, 2, True) for x in t1), '']
    baris = lambda tajuk, f: f'| {tajuk} | ' + ' | '.join(f(E[t]) for t in T_kunci) + ' |'
    A += ['## 4. Semakan kejujuran', '', K['nota_bebas'], '',
          '| Ukuran | ' + ' | '.join(K['terang'][t] for t in T_kunci) + ' |', '|---' * (1 + len(T_kunci)) + '|',
          baris(f'Median purata setiap dagangan, {len(atas)} setup teratas', lambda e: p(e['atas'].median(), 2, True) + ' %'),
          baris(f'Median purata setiap dagangan, {len(rawak)} setup rawak', lambda e: p(e['rawak'].median(), 2, True) + ' %'),
          baris('Setup teratas dengan purata positif', lambda e: f"{int((e['atas'] > 0).sum())} daripada {len(e['atas'])}"),
          baris('Setup rawak dengan purata positif', lambda e: f"{int((e['rawak'] > 0).sum())} daripada {len(e['rawak'])}"),
          baris('Setup teratas melebihi persentil ke-95 rawak',
                lambda e: f"{int((e['atas'] > e['p95']).sum())} daripada {len(e['atas'])}"),
          baris('Spearman `skor tepat` lawan purata', lambda e: f"{e['rho']:+.2f}"), '',
          ('Bacaan: pada tempoh yang tahunnya tidak dipakai carian (' + ', '.join(K['bebas']) + '), setup teratas '
           '**mengatasi** setup rawak. Ini masih backtest tanpa saham delist; hakim sebenar ialah papertrade.'
           if tahan else
           'Bacaan: **kelebihan hanya muncul pada tahun yang sama dengan carian.** Pada tempoh yang tahunnya tidak '
           'dipakai carian (' + ', '.join(K['bebas']) + ') setup teratas tidak mengatasi setup rawak. Papan ini '
           'menggambarkan pasaran tempoh carian, bukan kaedah yang terbukti tahan merentas era.'), '',
          f'Gabungan semua tempoh Kunci (ukuran pradaftar T3): Spearman {rho:+.2f}; median teratas '
          f'{p(atas.pur_kunci.median(), 2, True)} % lawan rawak {p(rawak.pur_kunci.median(), 2, True)} %; '
          f'{int((atas.pur_kunci > p95).sum())} daripada {len(atas)} melebihi persentil ke-95 rawak '
          f'({p(p95, 2, True)} %).', '',
          '### Apa yang carian pilih', '',
          f'- {h4} daripada {len(atas)} setup teratas memakai henti paling longgar (`H4`), dan {atr4} memakai '
          'penapis saham meruap (`F23` ATR % ≥ 4).',
          f'- Purata pegang 10 teratas pada Kunci ialah {pegang:.1f} sesi daripada had 20.',
          '- MDD buku = semua posisi sama berat dan sentiasa melabur penuh, bukan portfolio berslot; bandingkan '
          'dengan toleransi MDD akaun −10 %.', '',
          '## 5. Kaveat', '',
          '- Backtest sahaja. Tiada setup di sini masuk papertrade tanpa keputusan pengguna yang berasingan; kad '
          'skor kekal satu-satunya keputusan wang sebenar.',
          *[f'- {x}' for x in K['kaveat']],
          '- Peringkat besar membenarkan isyarat bertindih; angka papan dikira semula dengan satu posisi setiap '
          'saham.',
          '- Benih M yang bergantung pada saham lain (persentil RS) dikira dalam alam masing-masing.',
          *(['- `N201` (MA20 silang atas MA50 DAN tutup > MA50) dan `P07` (MA20 silang atas MA50) hampir sama; '
             'pradaftar mengira keluarga ikut ID, jadi kedua-duanya boleh muncul dalam papan.']
            if {'N201', 'P07'} <= set(papan.pencetus) else []),
          f"- Benih gagal dijalankan: set carian {len(meta.get('ralat_benih', {}))}, Kunci {len(ralat_kunci)} "
          f'(senarai dalam `carian_setup/hasil/{pus}/meta.json`).', '',
          '## 6. Jana semula', '',
          '```', 'W=<folder kerja di luar repo, satu setiap pusingan>', 'cd BacktestShariah2/kajian/carian_setup',
          f"C={cari.PUSINGAN[pus][0]}; K={cari.PUSINGAN[pus][1]}; P={pus}",
          'python3 cs_cari.py panel $W $C && python3 cs_cari.py benih $W $C && python3 cs_cari.py besar $W $P',
          'python3 cs_cari.py tepat $W $P && python3 cs_cari.py panel $W $K && python3 cs_cari.py kunci $W $P',
          'python3 cs_lapor.py $W $P', '```', '']
    teks = '\n'.join(A)
    open(os.path.join(keluar_dir, 'LAPORAN.md'), 'w', encoding='utf-8').write(teks)
    if not arkib:
        open(os.path.join(BS2, 'kajian', 'CARIAN_SETUP.md'), 'w', encoding='utf-8').write(teks)
    print(f'laporan {pus}:', len(papan), 'setup papan; rho', round(rho, 3), '; tahan tempoh bebas:', tahan)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], arkib=len(sys.argv) > 3 and sys.argv[3] == 'arkib')
