"""Ringkasan boleh dibaca daripada hasil carian setup yang SUDAH dijana (tiada pengiraan baharu).

    python3 cs_ringkas.py          # tulis hasil/CS03/TOP50.md dan hasil/PRASYARAT/PEMBAHAGIAN_F.{csv,md}

Sumber: hasil/CS03/senarai_kunci.csv (cs_tangkap.py), data/registry_F.csv (cs_lapor.py / cs_tangkap.py /
cs_tala.py) dan jejak_f/kohort.json (cs_hadapan.py). Output dijana; jangan sunting secara manual.
"""
import json
import os
import re
import sys

import pandas as pd

SINI = os.path.dirname(os.path.abspath(__file__))
BS2 = os.path.dirname(os.path.dirname(SINI))
HASIL = os.path.join(SINI, 'hasil')

# Penapis yang BUKAN daripada harga saham itu sendiri (cs_atom.PENAPIS indeks 25-27).
PASARAN = {'F26': 'QQQ ON', 'F27': 'QQQ OFF', 'F28': 'SPY > SMA200'}


def _status():
    try:
        sys.path.insert(0, os.path.join(BS2, 'standard'))
        import status_kad
        return status_kad.baris()
    except Exception:
        return '> **Status keputusan:** lihat `laporan/KAD_SKOR.md`; laporan ini BUKAN keputusan.'


def nama_pendek(masuk):
    """'M84 Jarak ... (benih M, varian 1: ...)' -> 'M84 Jarak ... (ditala 1)'."""
    m = re.match(r'^(.*?) \((benih|indikator)[^)]*?(varian (\d+))?[:)]', str(masuk))
    if not m:
        return str(masuk)
    return m.group(1) + (f' (ditala {m.group(4)})' if m.group(4) else '')


def bahagi(penapis):
    """Pecahkan teks penapis kepada (prasyarat pasaran, syarat saham)."""
    pas, sah = [], []
    for bhg in [b.strip() for b in str(penapis).split(' DAN ') if b.strip() and b.strip().lower() != 'nan']:
        kod = bhg.split(' ', 1)[0]
        if kod in PASARAN:
            pas.append(PASARAN[kod])
        else:
            sah.append(bhg.split(' ', 1)[1] if ' ' in bhg and re.match(r'^F\d+$', kod) else bhg)
    return ' + '.join(pas) or '–', ' + '.join(sah) or '–'


def pembahagian():
    reg = pd.read_csv(os.path.join(BS2, 'data', 'registry_F.csv'))
    with open(os.path.join(BS2, 'jejak_f', 'kohort.json')) as f:
        kohort = {a['id'] for a in json.load(f)['ahli']}
    baris = []
    for r in reg.itertuples():
        pas, sah = bahagi(r.penapis)
        if str(getattr(r, 'prasyarat', '')).strip() not in ('', 'nan'):      # lajur registry (pindaan (i)): CS05 dan seterusnya
            pas = '–' if r.prasyarat == 'tiada' else r.prasyarat
        baris.append({'id': r.id, 'pusingan': r.pusingan, 'prasyarat_pasaran': pas, 'pencetus': nama_pendek(r.masuk),
                      'penapis_saham': sah, 'henti': r.henti, 'keluar': r.keluar,
                      'jejak_hadapan': 'ya' if r.id in kohort else ''})
    return pd.DataFrame(baris)


def tulis_pembahagian():
    t = pembahagian()
    d = os.path.join(HASIL, 'PRASYARAT')
    os.makedirs(d, exist_ok=True)
    t.to_csv(os.path.join(d, 'PEMBAHAGIAN_F.csv'), index=False)
    kira = t[~t.pusingan.isin(['CS05', 'CS06'])].prasyarat_pasaran.value_counts()
    A = ['# Setup F: prasyarat (pasaran) lawan syarat (saham itu sendiri)', '', _status(), '',
         'Dijana `kajian/carian_setup/cs_ringkas.py` daripada `data/registry_F.csv` dan `jejak_f/kohort.json`. '
         '**Jangan sunting secara manual.**', '',
         'Prasyarat = isyarat yang BUKAN daripada saham itu sendiri. Ruang carian CS01–CS04 hanya ada tiga: '
         '**QQQ ON** (QQQ di atas SMA50 dan SMA10 di atas SMA20), **QQQ OFF** (selain itu) dan **SPY > SMA200**. '
         'CS05 (pindaan (i)) menambah 33 prasyarat pasaran dan 15 prasyarat kumpulan/syarikat (`cs_lapis.py`). '
         'RS diletak di bawah syarat saham (dikira daripada harga saham itu, dipangkatkan lawan saham lain).', '',
         'Bilangan (CS01–CS04): ' + ' · '.join(f'{k} = {v}' for k, v in kira.items())
         + f' (jumlah {int(kira.sum())}); CS05: {int((t.pusingan == "CS05").sum())} setup; '
         f'CS06: {int((t.pusingan == "CS06").sum())} setup.', '',
         '| ID | Pusingan | Prasyarat (pasaran) | Syarat saham: pencetus | Syarat saham: penapis | Henti | Keluar | Jejak hadapan |',
         '|---' * 8 + '|']
    for r in t.itertuples():
        A.append(f'| {r.id} | {r.pusingan} | {r.prasyarat_pasaran} | {r.pencetus} | {r.penapis_saham} | {r.henti} | '
                 f'{r.keluar} | {r.jejak_hadapan} |')
    A += ['', '## Kaveat', '',
          '- `F23`/`F33` (benih M21) memakai harga SPY di dalam peraturan kaedah itu sendiri, selain prasyarat SPY > SMA200. '
          'Kaedah M lain belum diperiksa satu per satu pada tahap ini.',
          '- Prasyarat lain (keluasan, turun-naik, sektor, industri, earnings, kalendar, takrif pakar) masuk ruang carian '
          'mulai CS05 (`hasil/CS05/LAPORAN.md`); tinjauan asalnya dalam `LAPORAN.md` folder ini (pindaan (h)).', '']
    with open(os.path.join(d, 'PEMBAHAGIAN_F.md'), 'w') as f:
        f.write('\n'.join(A))
    return t


def top50(n=50):
    s = pd.read_csv(os.path.join(HASIL, 'CS03', 'senarai_kunci.csv'))
    return s[s.peranan != 'rawak'].head(n).reset_index(drop=True)


def tulis_top50():
    t = top50()
    mp = lambda x: '–' if x != x else f'{x * 100:+.1f}'
    A = ['# CS03: 50 peraturan masuk teratas ikut kadar tangkap (backtest, BUKAN bukti)', '', _status(), '',
         'Dijana `kajian/carian_setup/cs_ringkas.py` daripada `hasil/CS03/senarai_kunci.csv` (200 teratas + 200 rawak). '
         '**Jangan sunting secara manual.**', '',
         'Pangkat ditentukan pada kumpulan A (separuh set 2000 yang dicari). Angka di bawah daripada **kumpulan B** '
         '(saham yang tidak dilihat, 2010 – Ogo 2026), dalam MATA PERATUS melebihi saham rawak pada hari dan tercile ATR% '
         'yang sama. "Lari" = naik ≥ 5 % minggu pertama, capai ≥ 10 % sebelum henti −8 %, masih ≥ 10 % pada minggu ke-4. '
         '"Lari 2025–26" = kepingan K3 (tahun yang tidak dilihat).', '',
         '| # | Masuk | Penapis | Belian | Lebih lari | Lebih capai +10% | Lebih kena henti | Lari 2025–26 |', '|---' * 8 + '|']
    for i, r in enumerate(t.itertuples(), 1):
        pen = ' + '.join(re.sub(r'^F\d+ ', '', b.strip()) for b in str(r.penapis).split(' DAN ')) if r.penapis == r.penapis else '–'
        A.append(f'| {i} | {nama_pendek(r.masuk)} | {pen} | {int(r.n_kunci):,} | {mp(r.k_lari)} | {mp(r.k_t10)} | '
                 f'{mp(r.k_gagal)} | {mp(r.kl_K3)} |')
    A += ['', '## Bacaan', '',
          f'- Median "lebih lari" {t.k_lari.median() * 100:+.1f} mata; {int((t.kl_K3 > 0).sum())} daripada {len(t)} kekal '
          f'positif pada 2025–26; median "lebih kena henti" {t.k_gagal.median() * 100:+.1f} mata.',
          f'- Hanya {t.masuk.str.split(" ").str[0].nunique()} pencetus berbeza: banyak baris ialah kembar (pencetus sama, '
          'penapis hampir sama). Papan 10 teratas (`F21`–`F30`) mengambil satu sahaja bagi setiap pencetus.',
          '- Ini kadar tangkap, bukan untung. Untung setiap dagangan hanya dikira untuk papan dan anak-anaknya '
          '(`kajian/CARIAN_SETUP.md`, `hasil/CS03/LAPORAN.md`, `hasil/CS04/LAPORAN.md`).', '']
    with open(os.path.join(HASIL, 'CS03', 'TOP50.md'), 'w') as f:
        f.write('\n'.join(A))
    return t


KUNCI = ('K1', 'K2', 'K3')
LAJUR_MENANG = ['menang_K1', 'menang_K2', 'menang_K3', 'menang']


def kadar_menang():
    """(pusingan, id) -> {tempoh Kunci: kadar menang}, dibaca daripada fail hasil setiap pusingan (tiada pengiraan baharu)."""
    out = {}
    for pus, kol in (('CS01', 'menang'), ('CS02', 'menang'), ('CS03', 'R_menang'), ('CS05', 'R_menang'), ('CS06', 'R_menang')):
        f = os.path.join(HASIL, pus, 'papan.csv')
        if os.path.exists(f):
            d = pd.read_csv(f)
            for r in d[d.tempoh.isin(KUNCI)].itertuples():
                out.setdefault((pus, r.id), {})[r.tempoh] = getattr(r, kol)
    d = pd.read_csv(os.path.join(HASIL, 'CS04', 'papan.csv'))
    for r in d[~d.kekal].itertuples():
        out[('CS04', r.anak)] = {t: getattr(r, f'menang_{t}') for t in KUNCI}
    f = os.path.join(HASIL, 'CS06', 'tala.csv')
    if os.path.exists(f):
        d = pd.read_csv(f)
        if 'menang_anak_K1' in d:
            for r in d[(~d.kekal) & d.menang_anak_K1.notna()].itertuples():
                out[('CS06', r.anak)] = {t: getattr(r, f'menang_anak_{t}') for t in KUNCI}
    return out


def isi_menang():
    """Isi lajur menang_K1..K3 dan menang (gabungan ikut bilangan belian) dalam data/registry_F.csv. Kadar menang = bahagian
    dagangan dengan R > 0 selepas kos, pada saham Kunci (yang carian tidak lihat), dengan henti dan keluar setup itu."""
    f = os.path.join(BS2, 'data', 'registry_F.csv')
    reg = pd.read_csv(f, dtype=str).fillna('')
    for c in LAJUR_MENANG:
        if c not in reg:
            reg[c] = ''
    M = kadar_menang()
    for i in reg.index:
        m = M.get((reg.at[i, 'pusingan'], reg.at[i, 'id']), {})
        jum = bil = 0.0
        for t in KUNCI:
            x, n = m.get(t), float(reg.at[i, f'n_{t}'] or 0)
            if x is not None and x == x and n > 0:
                reg.at[i, f'menang_{t}'] = f'{x:.4f}'
                jum, bil = jum + n * x, bil + n
        if bil:
            reg.at[i, 'menang'] = f'{jum / bil:.4f}'
    reg.to_csv(f, index=False)
    return reg


def jadual_menang():
    reg = isi_menang()
    with open(os.path.join(BS2, 'jejak_f', 'kohort.json')) as f:
        kohort = {a['id'] for a in json.load(f)['ahli']}
    nom = lambda x: float(x) if str(x).strip() not in ('', 'nan') else float('nan')
    baris = []
    for r in reg.itertuples():
        n = {t: nom(getattr(r, f'n_{t}')) for t in KUNCI}
        n = {t: (0.0 if v != v else v) for t, v in n.items()}
        N = sum(n.values())
        gab_ = lambda kol: (sum(n[t] * nom(getattr(r, f'{kol}_{t}')) for t in KUNCI if n[t] and nom(getattr(r, f'{kol}_{t}')) == nom(
            getattr(r, f'{kol}_{t}'))) / N) if N else float('nan')
        pas, sah = bahagi(r.penapis)
        baris.append({'id': r.id, 'pusingan': r.pusingan, 'prasyarat': r.prasyarat if str(r.prasyarat).strip() else pas,
                      'pencetus': nama_pendek(r.masuk), 'penapis_saham': r.syarat if str(r.syarat).strip() else sah,
                      'henti': r.henti, 'keluar': r.keluar, 'belian': int(N), 'menang': nom(r.menang), 'purata': gab_('purata'),
                      'k10': gab_('k10'), **{f'menang_{t}': nom(getattr(r, f'menang_{t}')) for t in KUNCI},
                      'jejak_hadapan': 'ya' if r.id in kohort else ''})
    return pd.DataFrame(baris)


def tulis_menang():
    t = jadual_menang()
    t.to_csv(os.path.join(HASIL, 'KADAR_MENANG.csv'), index=False, float_format='%.4f')
    p = lambda x, k=0, tanda=False: '–' if x != x else (f'{x * 100:+.{k}f}' if tanda else f'{x * 100:.{k}f}')
    ada = t[t.menang.notna()]
    cukup = ada[ada.belian >= 300]
    A = ['# Kadar menang setiap setup F (backtest pada saham yang tidak dilihat; BUKAN bukti)', '', _status(), '',
         'Dijana `kajian/carian_setup/cs_ringkas.py` daripada `data/registry_F.csv` dan fail hasil setiap pusingan. '
         '**Jangan sunting secara manual.**', '',
         '**Kadar menang** = daripada semua dagangan setup itu (dengan henti dan cara keluarnya sendiri), berapa peratus dijual '
         'dengan UNTUNG selepas kos 0.5 %; selebihnya rugi. Lajur "daripada 10 dagangan" ialah angka yang sama dibundarkan. Angka '
         'daripada saham Kunci (yang carian tidak lihat): CS01 = 1,000 saham lain; CS02–CS06 = kumpulan B; 2010 – Ogo 2026.', '',
         '**Baca bersama purata setiap dagangan.** Kadar menang sahaja tidak menunjukkan saiz untung dan rugi: setup yang menang '
         '4 daripada 10 masih boleh untung jika untungnya besar, dan setup yang menang 6 daripada 10 boleh rugi jika ruginya besar '
         '(`CLAUDE.md`: kadar menang sahaja bukan ukuran).', '',
         f'Ringkasan: {len(ada)} setup; median kadar menang {p(ada.menang.median())} %; {int((ada.menang >= 0.5).sum())} setup menang '
         f'≥ 50 %; {int(((ada.menang >= 0.5) & (ada.purata > 0)).sum())} setup menang ≥ 50 % DAN purata positif; '
         f'{int(((ada.menang < 0.5) & (ada.purata > 0)).sum())} setup menang < 50 % tetapi purata positif.', '']
    if len(cukup):
        atas = cukup.sort_values('menang', ascending=False).head(5)
        A += ['Kadar menang tertinggi (≥ 300 belian): ' + '; '.join(
            f'`{r.id}` {p(r.menang)} % (purata {p(r.purata, 1, True)} %, {r.belian:,} belian)' for r in atas.itertuples()) + '.', '']
    A += ['| ID | Pusingan | Prasyarat | Pencetus | Penapis saham | Belian | **Menang %** | Daripada 10 dagangan: untung / rugi | '
          'Purata setiap dagangan % | Dijual ≥ +10 % % | Menang % K1 / K2 / K3 | Jejak hadapan |', '|---' * 12 + '|']
    for r in t.itertuples():
        u = '–' if r.menang != r.menang else f'{round(r.menang * 10)} / {10 - round(r.menang * 10)}'
        A.append(f"| `{r.id}` | {r.pusingan} | {r.prasyarat if r.prasyarat not in ('tiada', '') else '–'} | {r.pencetus} | "
                 f"{r.penapis_saham if r.penapis_saham not in ('tiada', '') else '–'} | {r.belian:,} | **{p(r.menang)}** | {u} | "
                 f"{p(r.purata, 2, True)} | {p(r.k10)} | {p(r.menang_K1)} / {p(r.menang_K2)} / {p(r.menang_K3)} | {r.jejak_hadapan} |")
    A += ['', '- K1 = 2010–2019, K2 = 2020–2024 (CS01: 2020 – Ogo 2026), K3 = 2025 – Ogo 2026 (tiada bagi CS01).',
          '- Cara pegang dan keluar setiap setup: lajur `henti` dan `keluar` dalam `KADAR_MENANG.csv` dan `data/registry_F.csv`.',
          '- Tiada saham delist dalam data (condong ke atas); backtest sahaja. Kad skor kekal satu-satunya keputusan wang sebenar.', '']
    with open(os.path.join(HASIL, 'KADAR_MENANG.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(A))
    return t


if __name__ == '__main__':
    p = tulis_pembahagian()
    t = tulis_top50()
    m = tulis_menang()
    print(f'pembahagian: {len(p)} setup F · {p.prasyarat_pasaran.value_counts().to_dict()}')
    print(f'top50: {len(t)} baris')
    print(f'kadar menang: {int(m.menang.notna().sum())} daripada {len(m)} setup F; median {m.menang.median() * 100:.0f}%')
