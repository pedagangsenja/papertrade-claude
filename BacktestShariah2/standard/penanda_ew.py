# penanda_ew.py — penanda aras EW hadapan (audit 25 Okt 2026: EW saham Shariah ialah syarat kejayaan pemilik, tetapi tidak
# pernah dijejak ke hadapan; semua perbandingan hadapan memakai SPY).
#
#   python3 BacktestShariah2/standard/penanda_ew.py [--stor <folder stor>] [--univ <univ.txt>] [--keluar <csv>]
#   -> data/analisis/ew_harian.csv: tarikh, n, ew_cc (tutup semalam -> tutup), ew_oc (buka -> tutup hari sama),
#      ew_indeks (indeks tutup-ke-tutup, 1.0 pada sesi pertama), spy_cc, spy_oc, spy_indeks.
#
# Alam = ticker univ.txt (skrin Shariah Moomoo, harga >= USD10) yang ada dalam stor. Saham dikira pada sesi t jika tutup
# semalam >= USD10 dan kedua-dua bar wujud (tiada pandang hadapan: kelayakan ditentukan oleh tutup semalam). Pulangan harian
# dihad +-50% (ralat data / peristiwa korporat tidak terlaras tidak menguasai purata sama berat). univ.txt ialah senarai
# Shariah SEMASA: sejarah sebelum Okt 2026 berbias penyintas (rujukan sahaja); siri hadapan sejak Okt 2026 tidak.
# Pulangan tempoh posisi yang dibeli pada BUKA d0 dan dinilai pada TUTUP d1 = (1 + oc[d0]) x prod(1 + cc[t], d0 < t <= d1) - 1
# (fungsi `tempoh`), sama dengan cara posisi C dan Lejar diukur.
import argparse, os, sys

import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
BS2 = os.path.dirname(HERE)
STOR = os.path.join(BS2, 'data', 'harga', 'stor')
UNIV = os.path.join(BS2, 'data', 'harga', 'univ.txt')
KELUAR = os.path.join(BS2, 'data', 'analisis', 'ew_harian.csv')
HARGA_MIN = 10.0
HAD_PULANGAN = 0.5
N_MIN = 50            # sesi dengan < 50 saham layak (hujung awal stor) tidak dikira


def baca_univ(path=UNIV):
    with open(path, encoding='utf-8') as f:
        return {t.strip() for t in f if t.strip()}


def bina(stor=STOR, univ=UNIV):
    """DataFrame ew_harian (lihat kepala fail)."""
    tik = baca_univ(univ)
    fr = [pd.read_csv(os.path.join(stor, nm)) for nm in ('harga_A.csv', 'harga_B.csv') if os.path.exists(os.path.join(stor, nm))]
    d = pd.concat(fr, ignore_index=True)
    d = d[d.ticker.isin(tik)].sort_values(['ticker', 'date']).drop_duplicates(['ticker', 'date'], keep='last')
    d['tutup_semalam'] = d.groupby('ticker').close.shift(1)
    d = d[d.tutup_semalam >= HARGA_MIN].copy()
    d['cc'] = (d.close / d.tutup_semalam - 1).clip(-HAD_PULANGAN, HAD_PULANGAN)
    d['oc'] = (d.close / d.open - 1).where(d.open > 0).clip(-HAD_PULANGAN, HAD_PULANGAN)
    g = d.groupby('date')
    ew = pd.DataFrame({'n': g.size(), 'ew_cc': g.cc.mean(), 'ew_oc': g.oc.mean()})
    ew = ew[ew.n >= N_MIN]
    idx = pd.read_csv(os.path.join(stor, 'harga_idx.csv'))
    spy = idx[idx.ticker == 'SPY'].sort_values('date').set_index('date')
    spy_cc = spy.close / spy.close.shift(1) - 1
    spy_oc = spy.close / spy.open - 1
    ew = ew.join(pd.DataFrame({'spy_cc': spy_cc, 'spy_oc': spy_oc}), how='left')
    ew['ew_indeks'] = (1 + ew.ew_cc).cumprod()
    ew['spy_indeks'] = (1 + ew.spy_cc.fillna(0)).cumprod()
    ew.index = [f'{s[:4]}-{s[4:6]}-{s[6:8]}' for s in ew.index.astype(str)]
    ew.index.name = 'tarikh'
    return ew[['n', 'ew_cc', 'ew_oc', 'ew_indeks', 'spy_cc', 'spy_oc', 'spy_indeks']]


def tempoh(ew, mula, akhir, lajur='ew'):
    """Pulangan (pecahan) beli pada BUKA `mula`, nilai pada TUTUP `akhir` (YYYY-MM-DD); None jika tarikh di luar siri."""
    if mula not in ew.index or akhir not in ew.index or akhir < mula:
        return None
    s = ew.loc[mula:akhir]
    return float((1 + s[f'{lajur}_oc'].iloc[0]) * np.prod(1 + s[f'{lajur}_cc'].iloc[1:].values) - 1)


def main(argv=None):
    ap = argparse.ArgumentParser(description='Penanda aras EW hadapan alam Shariah (univ.txt)')
    ap.add_argument('--stor', default=STOR); ap.add_argument('--univ', default=UNIV); ap.add_argument('--keluar', default=KELUAR)
    a = ap.parse_args(argv)
    ew = bina(a.stor, a.univ)
    os.makedirs(os.path.dirname(a.keluar), exist_ok=True)
    ew.to_csv(a.keluar, float_format='%.6g')
    print(f'{a.keluar}: {len(ew)} sesi {ew.index[0]}..{ew.index[-1]}, n median {int(ew.n.median())}, '
          f'EW {100 * (ew.ew_indeks.iloc[-1] - 1):+.1f}% lawan SPY {100 * (ew.spy_indeks.iloc[-1] - 1):+.1f}%', file=sys.stderr)


if __name__ == '__main__':
    main()
