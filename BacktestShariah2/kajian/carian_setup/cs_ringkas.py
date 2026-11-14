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
        baris.append({'id': r.id, 'pusingan': r.pusingan, 'prasyarat_pasaran': pas, 'pencetus': nama_pendek(r.masuk),
                      'penapis_saham': sah, 'henti': r.henti, 'keluar': r.keluar,
                      'jejak_hadapan': 'ya' if r.id in kohort else ''})
    return pd.DataFrame(baris)


def tulis_pembahagian():
    t = pembahagian()
    d = os.path.join(HASIL, 'PRASYARAT')
    os.makedirs(d, exist_ok=True)
    t.to_csv(os.path.join(d, 'PEMBAHAGIAN_F.csv'), index=False)
    kira = t.prasyarat_pasaran.value_counts()
    A = ['# Setup F: prasyarat (pasaran) lawan syarat (saham itu sendiri)', '', _status(), '',
         'Dijana `kajian/carian_setup/cs_ringkas.py` daripada `data/registry_F.csv` dan `jejak_f/kohort.json`. '
         '**Jangan sunting secara manual.**', '',
         'Prasyarat = isyarat yang BUKAN daripada saham itu sendiri. Ruang carian CS01–CS04 hanya ada tiga: '
         '**QQQ ON** (QQQ di atas SMA50 dan SMA10 di atas SMA20), **QQQ OFF** (selain itu) dan **SPY > SMA200**. '
         'RS diletak di bawah syarat saham (dikira daripada harga saham itu, dipangkatkan lawan saham lain).', '',
         'Bilangan: ' + ' · '.join(f'{k} = {v}' for k, v in kira.items()) + f' (jumlah {len(t)}).', '',
         '| ID | Pusingan | Prasyarat (pasaran) | Syarat saham: pencetus | Syarat saham: penapis | Henti | Keluar | Jejak hadapan |',
         '|---' * 8 + '|']
    for r in t.itertuples():
        A.append(f'| {r.id} | {r.pusingan} | {r.prasyarat_pasaran} | {r.pencetus} | {r.penapis_saham} | {r.henti} | '
                 f'{r.keluar} | {r.jejak_hadapan} |')
    A += ['', '## Kaveat', '',
          '- `F23`/`F33` (benih M21) memakai harga SPY di dalam peraturan kaedah itu sendiri, selain prasyarat SPY > SMA200. '
          'Kaedah M lain belum diperiksa satu per satu pada tahap ini.',
          '- Prasyarat lain (keluasan, turun-naik, sektor, industri, earnings, kalendar) BELUM ada dalam ruang carian; '
          'ukurannya dalam `LAPORAN.md` folder ini (pindaan (h)).', '']
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


if __name__ == '__main__':
    p = tulis_pembahagian()
    t = tulis_top50()
    print(f'pembahagian: {len(p)} setup F · {p.prasyarat_pasaran.value_counts().to_dict()}')
    print(f'top50: {len(t)} baris')
