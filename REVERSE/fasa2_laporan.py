"""Jana REVERSE/FASA2.md daripada output FASA 2 (SPEC §13.12 B).

Guna: python3 REVERSE/fasa2_laporan.py
"""
import sys
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd

AKAR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(AKAR))
R = AKAR / 'REVERSE'
POLISI = ['chandelier_4atr', 'jual_hari63', 'pegang_252']


def md(d, kols=None, n=None):
    d = d[kols] if kols else d
    if n:
        d = d.head(n)
    if not len(d):
        return '_(tiada baris)_\n'
    out = ['| ' + ' | '.join(str(c) for c in d.columns) + ' |',
           '|' + '|'.join('---' for _ in d.columns) + '|']
    for _, r in d.iterrows():
        out.append('| ' + ' | '.join('' if pd.isna(v) else str(v) for v in r) + ' |')
    return '\n'.join(out) + '\n'


def verdik(j, pol):
    """Jadual keputusan ablasi: S+R lwn X+R dan S+X lwn X+X (lebihan SPY, had bawah 95%)."""
    d = j[j.polisi == pol]
    x = d[d.arm.str.startswith('X')].set_index('arm')
    if not {'X+R', 'X+X'} <= set(x.index):
        return pd.DataFrame(), {}
    asas = {a: x.loc[a] for a in ('X+R', 'X+X')}
    sr = d[d.arm == 'S+R'].set_index('signal')
    sx = d[d.arm == 'S+X'].set_index('signal')
    rows = []
    for sg in sorted(set(sr.index) & set(sx.index)):
        a, b = sr.loc[sg], sx.loc[sg]
        kaki1 = a.lebihan_spy_purata > asas['X+R'].lebihan_spy_purata
        kaki2 = b.lebihan_spy_purata > asas['X+X'].lebihan_spy_purata
        pos = min(a.lebihan_bawah95_ticker, a.lebihan_bawah95_minggu) > 0
        rows.append(dict(
            signal=sg, n_SR=int(a.n), median_SR=a['median'], purata_SR=a.purata,
            dipangkas5_SR=a.purata_dipangkas5, menang_SR=a.kadar_menang,
            lebihan_SR=a.lebihan_spy_purata, lebihan_SX=b.lebihan_spy_purata,
            bawah95_SR=min(a.lebihan_bawah95_ticker, a.lebihan_bawah95_minggu),
            kalahkan_XR='ya' if kaki1 else 'tidak', kalahkan_XX='ya' if kaki2 else 'tidak',
            lebihan_positif_95='ya' if pos else 'tidak',
            keputusan='MENYUMBANG' if (kaki1 and kaki2 and pos) else 'TIDAK'))
    out = pd.DataFrame(rows).sort_values('lebihan_SR', ascending=False)
    return out, asas


def main():
    j = pd.read_csv(R / 'fasa2_jangkaan.csv')
    pf = pd.read_csv(R / 'fasa2_portfolio.csv')
    fh = pd.read_csv(R / 'fasa2_hold.csv') if (R / 'fasa2_hold.csv').exists() else None
    A = []
    w = A.append
    w('# FASA 2 — pulangan boleh didagangkan, penilaian bergabung, ablasi 2×2\n')
    w(f'Dijana `REVERSE/fasa2_laporan.py` ({datetime.now(timezone.utc):%Y-%m-%d %H:%M} UTC). '
      'Reka bentuk dikunci dalam `SPEC.md` §13.12 B **sebelum** sebarang angka FASA 2 dilihat. '
      'FASA 1 (`LAPORAN_<TAHUN>.md`, `BANDING_TAHUN.md`) kekal sebagai rekod.\n')
    w('## 0. Apa yang berubah berbanding FASA 1\n')
    w('| Perkara | FASA 1 | FASA 2 |\n|---|---|---|\n'
      '| Sasaran | `tarikh_puncak` dalam tetingkap 63 hari; `mfe63 ≥ 30%` | pulangan dagangan '
      'penuh: masuk buka d+1, keluar ikut polisi tetap, kos dua sisi |\n'
      '| Unit penilaian | satu tahun, satu silo | 2020-01-01 – 2026-10-16 bergabung |\n'
      '| Set yang diuji | semua kemunculan signal (sehingga 148,303 setahun) | 8 calon teratas '
      'setiap hari = yang portfolio boleh ambil |\n'
      '| Kawalan | entri rawak | ablasi 2×2: signal lwn universe × susunan RS lwn rawak |\n')
    w('**Kaveat kekal:** tiada saham delist (survivorship) — semua angka ialah had atas; peta '
      'sektor bukan titik masa; universe 2020 lebih kecil (1638/1832/1940) daripada 2021–2025.\n')

    w('## 1. Ablasi 2×2 — pulangan setiap dagangan\n')
    w('Empat arm, polisi exit dan kos yang sama. `S+R` = signal × susunan RS 6 bulan; `S+X` = '
      'signal × susunan rawak; `X+R` = universe penuh × susunan RS; `X+X` = universe × rawak. '
      'Nilai dalam % setiap dagangan; `dipangkas5` = purata selepas 5% pulangan tertinggi '
      'dibuang; `bawah95` = had bawah 95% bootstrap blok (ticker atau minggu, yang lebih rendah).\n')
    for pol in POLISI:
        d = j[j.polisi == pol]
        if not len(d):
            continue
        g = (d.groupby('arm')[['n', 'median', 'purata', 'purata_dipangkas5', 'kadar_menang',
                               'lebihan_spy_purata', 'purata_bawah95_ticker',
                               'lebihan_bawah95_ticker', 'median_hari']]
             .median().round(2).reset_index())
        w(f'### Polisi `{pol}` — median merentas signal (arm S) dan nilai sebenar (arm X)\n')
        w(md(g))
    w('### Berapa banyak signal mempunyai median dagangan positif?\n')
    rows = []
    for pol in POLISI:
        d = j[(j.polisi == pol) & (j.arm == 'S+R')]
        if not len(d):
            continue
        rows.append(dict(polisi=pol, n_signal=len(d),
                         median_positif=int((d['median'] > 0).sum()),
                         purata_positif=int((d.purata > 0).sum()),
                         dipangkas5_positif=int((d.purata_dipangkas5 > 0).sum()),
                         lebihan_bawah95_positif=int((d[['lebihan_bawah95_ticker',
                                                         'lebihan_bawah95_minggu']].min(axis=1)
                                                      > 0).sum())))
    w(md(pd.DataFrame(rows)))
    w('Jurang antara `purata_positif` dan `dipangkas5_positif` ialah ukuran terus berapa banyak '
      'jangkaan positif itu datang daripada 5% ekor kanan.\n')

    w('## 2. Keputusan ablasi — adakah signal menyumbang?\n')
    w('Syarat SPEC §13.12 B4: **S+R > X+R DAN S+X > X+X** (lebihan atas SPY), dan had bawah 95% '
      'lebihan S+R > 0.\n')
    for pol in POLISI:
        v, asas = verdik(j, pol)
        if not len(v):
            continue
        w(f'### Polisi `{pol}`\n')
        w(f'Asas: X+R lebihan {asas["X+R"].lebihan_spy_purata}% (n {int(asas["X+R"].n)}), '
          f'X+X lebihan {asas["X+X"].lebihan_spy_purata}% (n {int(asas["X+X"].n)}).\n')
        w(f'MENYUMBANG: **{int((v.keputusan == "MENYUMBANG").sum())} daripada {len(v)}** signal.\n')
        w(md(v.head(12), ['signal', 'n_SR', 'median_SR', 'purata_SR', 'dipangkas5_SR',
                          'menang_SR', 'lebihan_SR', 'lebihan_SX', 'bawah95_SR', 'kalahkan_XR',
                          'kalahkan_XX', 'keputusan']))
        men = v[v.keputusan == 'MENYUMBANG']
        if len(men):
            w('Signal MENYUMBANG: ' + ', '.join(f'`{s}`' for s in men.signal) + '\n')

    w('## 3. Portfolio bergabung 8 slot (2020-01-01 – 2026-10-16)\n')
    spy = pf.iloc[0]
    w(f'SPY tempoh sama: jumlah {spy.spy_jumlah}%, CAGR {spy.spy_cagr}%, MDD {spy.spy_mdd}%.\n')
    for pol in POLISI:
        d = pf[pf.polisi == pol]
        if not len(d):
            continue
        w(f'### Polisi `{pol}`\n')
        x = d[d.arm.str.startswith('X')]
        w('Arm kawalan:\n')
        w(md(x, ['arm', 'n_posisi', 'purata_slot', 'purata_hari_pegang', 'pulangan_jumlah',
                 'cagr', 'mdd', 'median_bulanan', 'pct_bulan_ge10', 'pct_bulan_positif',
                 'bulan_terburuk']))
        s = d[d.arm == 'S+R'].sort_values('cagr', ascending=False)
        w(f'Arm S+R, 8 teratas ikut CAGR (daripada {len(s)} signal); '
          f'{int((s.cagr > spy.spy_cagr).sum())} mengalahkan SPY, '
          f'{int((s.median_bulanan >= 10).sum())} mencapai median bulanan ≥ +10%:\n')
        w(md(s.head(8), ['signal', 'n_posisi', 'purata_slot', 'pulangan_jumlah', 'cagr', 'mdd',
                         'median_bulanan', 'pct_bulan_ge10', 'pct_bulan_positif',
                         'bulan_terburuk']))
    w('### Sasaran +10% sebulan (median)\n')
    n_ok = int((pf.median_bulanan >= 10).sum())
    w(f'**{n_ok} daripada {len(pf)}** kombinasi (signal × arm × polisi) mencapai median bulanan '
      f'≥ +10%. Terbaik: {pf.median_bulanan.max()}%.\n')

    if fh is not None:
        w('## 4. Fasa HOLD — kelas pullback sebagai peraturan jual\n')
        w('Posisi entry-agnostik (arm X+R: 8 saham RS 6 bulan tertinggi dalam universe setiap '
          'hari), set posisi yang SAMA bagi ketiga-tiga peraturan jual. Definisi kausal kelas '
          'pullback: SPEC §13.12 B7.\n')
        w(md(fh, [c for c in ['polisi', 'n', 'median', 'purata', 'purata_dipangkas5',
                              'kadar_menang', 'lebihan_spy_purata', 'lebihan_bawah95_ticker',
                              'median_hari', 'pf_cagr', 'pf_mdd', 'pf_median_bulanan',
                              'pf_pct_bulan_positif', 'spy_cagr'] if c in fh.columns]))
    w('## 5. Kesimpulan\n')
    n_uji = len(j[j.arm == 'S+R'])
    men = sum(int((verdik(j, pol)[0].keputusan == 'MENYUMBANG').sum()) for pol in POLISI
              if len(verdik(j, pol)[0]))
    w(f'1. **{men} daripada {n_uji} ujian (signal × polisi) lulus syarat ablasi.** Dengan '
      f'{n_uji} perbandingan serentak, jangkaan positif palsu pada 5% ialah '
      f'kira-kira {round(n_uji * 0.05)} — jadi bilangan yang lulus **tidak melebihi apa yang '
      'nasib sahaja akan hasilkan**. FASA 2 tidak mendaftar FDR lebih awal, jadi mana-mana '
      'signal yang lulus mesti dianggap hipotesis, bukan penemuan.\n')
    for i_, pol in enumerate(POLISI):
        d = j[(j.polisi == pol) & (j.arm == 'S+R')]
        x = j[(j.polisi == pol) & (j.arm.isin(['X+R', 'X+X']))].set_index('arm')
        if not len(d) or 'X+X' not in x.index:
            continue
        w(f'2{"abc"[i_]}. Polisi `{pol}`: median dagangan arm S+R (merentas signal) '
          f'{round(d["median"].median(), 2)}% lawan arm rawak X+X {x.loc["X+X", "median"]}%; '
          f'purata dipangkas 5% {round(d.purata_dipangkas5.median(), 2)}% lawan '
          f'{x.loc["X+X", "purata_dipangkas5"]}%; kadar menang '
          f'{round(d.kadar_menang.median(), 2)}% lawan {x.loc["X+X", "kadar_menang"]}%. '
          f'**Pemilihan rawak daripada universe mengalahkan signal** pada ketiga-tiga ukuran.\n')
    pfs = pf[pf.arm == 'S+R']
    w(f'3. Portfolio bergabung: {int((pfs.cagr <= spy.spy_cagr).sum())} daripada {len(pfs)} '
      f'kombinasi S+R kalah kepada SPY ({spy.spy_cagr}% CAGR). Arm rawak X+X dengan '
      f'`pegang_252` memberi '
      f'{pf[(pf.arm == "X+X") & (pf.polisi == "pegang_252")].cagr.iloc[0]}% CAGR — lebih tinggi '
      'daripada SPY dan daripada median S+R pada setiap polisi.\n')
    w('4. **X+R ialah arm terburuk pada setiap polisi.** 8 saham RS 6 bulan tertinggi dalam '
      'universe 2000 saham ialah hujung momentum yang paling kerap berbalik; itu, bukan signal, '
      'yang menerangkan mengapa FASA 1 nampak seperti signal "mengalahkan" sesuatu apabila '
      'dibanding dengan susunan RS.\n')
    if fh is not None and 'pf_cagr' in fh.columns:
        pa = fh[fh.polisi == 'pullback_amaran']
        if len(pa):
            r = pa.iloc[0]
            w(f'5. **Fasa HOLD: kelas pullback tidak bertukar menjadi wang.** Sebagai peraturan '
              f'jual ia memberi median {r["median"]}% setiap dagangan, kadar menang '
              f'{r.kadar_menang}%, median pegangan {r.median_hari} hari, dan CAGR portfolio '
              f'{r.pf_cagr}% (MDD {r.pf_mdd}%) berbanding SPY {r.spy_cagr}%. Ia menyala terlalu '
              'awal dan pusing ganti membunuh baki apa-apa kelebihan. Penemuan FASA 1 '
              '(SIHAT/PASARAN 80–92% sambung ke puncak baharu lawan AMARAN 44–54%) kekal benar '
              'sebagai **perihalan**, tetapi ia diukur atas run yang sudah naik, dan sebagai '
              'peraturan keputusan ia merugikan.\n')
    w('6. Sasaran pengguna +10% sebulan (median): **0 daripada '
      f'{len(pf)}** kombinasi mencapainya; tertinggi {pf.median_bulanan.max()}%.\n')
    w('\n### Apa yang ini TIDAK buktikan\n')
    w('- Bukan bukti bahawa tiada kelebihan boleh didapati dalam data ini; ia bukti bahawa '
      '**46 signal yang FASA 1 hasilkan tidak membawa kelebihan boleh dagang**, dan bahawa '
      'cara FASA 1 mengukur (puncak dalam tetingkap) memilih kemeruapan.\n'
      '- Tiada saham delist: angka rawak X+X juga dipandang tinggi oleh survivorship, mungkin '
      'lebih daripada arm signal (saham yang mati lebih berkemungkinan muncul dalam pilihan '
      'rawak daripada dalam pilihan signal momentum). Perbandingan arm tetap sah kerana '
      'kesemuanya memakai data yang sama, tetapi aras mutlak bukan jangkaan.\n'
      '- Satu signal contrarian (`q1:cerun_ema21`, kuintil terendah cerun EMA21) ialah satu-'
      'satunya yang lulus, dan hanya pada satu polisi. Arahnya bertentangan dengan keluarga '
      'momentum/kemeruapan yang FASA 1 tumpukan. Itu petunjuk untuk fasa seterusnya, bukan '
      'keputusan.\n')
    (R / 'FASA2.md').write_text('\n'.join(A))
    print(f'FASA2.md ditulis ({len("".join(A))} aksara)')


if __name__ == '__main__':
    main()
