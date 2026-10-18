# Kajian gred sektor/industri (18 Okt 2026): sejarah kekuatan kumpulan SELURUH pasaran AS untuk menguji formula gred.
# Dijalankan oleh GitHub Actions (.github/workflows/kajian_gred.yml, cawangan kajian-gred sahaja); bukan sebahagian rutin harian.
# Sumber: yfinance, semua ticker papertrade/peta_industri.csv (industri plate Moomoo; sektor = SEKTOR_INDUSTRI).
# Bias diketahui: saham yang sudah dinyahsenarai tiada (survivorship).
#
# Keluaran (BacktestShariah2/kajian/data/):
#   kumpulan_harian.csv.gz — setiap (tarikh, jenis Sektor/Industri, nama): n saham layak (tutup >= USD5), indeks sama rata,
#     median pulangan 1M/1W/3M/6M/12M, segmen suku q2–q4 (gaya IBD), breadth 1M, % > SMA50 / SMA200, median pangkat RS saham.
#   meta_saham.csv — ticker, industri, sektor, bar, tarikh pertama/akhir (audit); gagal.txt — ticker tanpa data.
# Guna: python3 gred_pasaran.py [--mula 2017-06-01] [--had N]
import argparse, os, sys, time
import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
BS2 = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(BS2, 'standard'))
from sektor_pasaran import SEKTOR_INDUSTRI  # noqa: E402

OUT = os.path.join(HERE, 'data')
HARGA_MIN = 5.0
MIN_SAHAM = 3


def muat_turun(tickers, mula, saiz=200, rehat=2.0):
    import yfinance as yf
    C, V, gagal = [], [], []
    for i in range(0, len(tickers), saiz):
        kump = tickers[i:i + saiz]
        for cuba in range(3):
            try:
                d = yf.download([t.replace('.', '-') for t in kump], start=mula, auto_adjust=True, progress=False,
                                threads=True, group_by='column')
                break
            except Exception as e:  # noqa: BLE001
                print('ralat', i, e, flush=True); time.sleep(10 * (cuba + 1)); d = None
        if d is None or d.empty:
            gagal += kump; continue
        c, v = d['Close'], d['Volume']
        c.columns = [x.replace('-', '.') for x in c.columns]; v.columns = c.columns
        kosong = [t for t in kump if t not in c.columns or c[t].notna().sum() == 0]
        gagal += kosong
        C.append(c.drop(columns=[t for t in kosong if t in c.columns]).astype('float32'))
        V.append(v.drop(columns=[t for t in kosong if t in v.columns]).astype('float32'))
        print(f'{i + len(kump)}/{len(tickers)} gagal {len(gagal)}', flush=True)
        time.sleep(rehat)
    C = pd.concat(C, axis=1).sort_index(); V = pd.concat(V, axis=1).sort_index()
    C = C.loc[:, ~C.columns.duplicated()]; V = V.loc[:, ~V.columns.duplicated()]
    return C, V, gagal


def kira(C, peta):
    C = C.dropna(how='all')
    R = C.pct_change(fill_method=None).clip(-0.5, 1.0)
    layak = C.shift(1) >= HARGA_MIN                      # tapis harga pada tutup semalam
    ret = {n: C / C.shift(n) - 1 for n in [5, 21, 63, 126, 252]}
    q = {2: C.shift(63) / C.shift(126) - 1, 3: C.shift(126) / C.shift(189) - 1, 4: C.shift(189) / C.shift(252) - 1}
    for d in list(ret.values()) + list(q.values()):
        d[d.abs() > 10] = np.nan
    a50 = C > C.rolling(50).mean(); a200 = C > C.rolling(200).mean()
    skor_rs = 0.4 * ret[63] + 0.2 * q[2] + 0.2 * q[3] + 0.2 * q[4]
    pangkat = skor_rs.where(layak).rank(axis=1, pct=True) * 98 + 1          # RS 1–99 seluruh pasaran
    out = []
    for jenis, kol in [('Sektor', 'sektor'), ('Industri', 'industri')]:
        for nama, g in peta.groupby(kol):
            c = [t for t in g.index if t in C.columns]
            if len(c) < MIN_SAHAM:
                continue
            L = layak[c]
            m = lambda X: X[c].where(L).median(axis=1)
            n = L.sum(axis=1)
            idx = (1 + R[c].where(L).mean(axis=1).fillna(0)).cumprod()
            r21 = ret[21][c].where(L)
            df = pd.DataFrame({'n': n, 'indeks': idx, 'm1w': m(ret[5]), 'm1m': m(ret[21]), 'm3m': m(ret[63]),
                               'm6m': m(ret[126]), 'm12m': m(ret[252]), 'q2': m(q[2]), 'q3': m(q[3]), 'q4': m(q[4]),
                               'br1m': (r21 > 0).sum(axis=1) / r21.notna().sum(axis=1).replace(0, np.nan),
                               'a50': a50[c].where(L).sum(axis=1) / n.replace(0, np.nan),
                               'a200': a200[c].where(L).sum(axis=1) / n.replace(0, np.nan),
                               'rs_med': pangkat[c].median(axis=1)})
            df.insert(0, 'nama', nama); df.insert(0, 'jenis', jenis)
            out.append(df[df.n >= MIN_SAHAM])
    K = pd.concat(out).rename_axis('tarikh').reset_index()
    K['tarikh'] = pd.to_datetime(K.tarikh).dt.strftime('%Y-%m-%d')
    return K


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument('--mula', default='2017-06-01')
    ap.add_argument('--had', type=int, default=0)
    a = ap.parse_args(argv)
    peta = pd.read_csv(os.path.join(BS2, 'papertrade', 'peta_industri.csv')).drop_duplicates('ticker').set_index('ticker')
    peta['sektor'] = peta.industri.map(SEKTOR_INDUSTRI).fillna('Lain-lain')
    tickers = sorted(peta.index.astype(str))[: a.had or None]
    C, V, gagal = muat_turun(tickers, a.mula)
    os.makedirs(OUT, exist_ok=True)
    K = kira(C, peta.loc[[t for t in peta.index if t in C.columns]])
    K.round(5).to_csv(os.path.join(OUT, 'kumpulan_harian.csv.gz'), index=False, compression='gzip')
    meta = pd.DataFrame({'industri': peta.industri, 'sektor': peta.sektor}).loc[list(C.columns)]
    meta['bar'] = C.notna().sum().values
    meta['mula'] = [C[t].first_valid_index() for t in C.columns]; meta['akhir'] = [C[t].last_valid_index() for t in C.columns]
    meta['nilai_dagangan_med'] = (C * V).tail(63).median().round(0).values
    meta.rename_axis('ticker').to_csv(os.path.join(OUT, 'meta_saham.csv'))
    open(os.path.join(OUT, 'gagal.txt'), 'w').write('\n'.join(gagal) + '\n')
    C.to_parquet(os.path.join(HERE, 'harga_penuh.parquet'))   # artifact Actions sahaja (tidak di-commit)
    print(f'saham {C.shape[1]} gagal {len(gagal)} hari {C.shape[0]} baris kumpulan {len(K)}', flush=True)


if __name__ == '__main__':
    main()
