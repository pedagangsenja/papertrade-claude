# semak_penyintas.py — ukur jurang penyintas alam PIT dengan keahlian S&P 500 sejarah (fja05680/sp500, GitHub, lesen MIT).
#   python3 BacktestShariah2/kajian/pit/semak_penyintas.py --data DIR [--csv FAIL_SEJARAH]
# -> kajian/pit/penyintas_sp500.json: ahli S&P 500 sejak 2013, berapa tiada dalam data A02 (ikut tahun keluar indeks), senarai.
# Ticker yang tiada = diambil alih / delist / tukar simbol (tidak dibezakan di sini). Tiada data harga dimuat turun.
import argparse, json, os, sys, urllib.parse, urllib.request

import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import alam as AL  # noqa: E402

URL = ('https://raw.githubusercontent.com/fja05680/sp500/master/'
       + urllib.parse.quote('S&P 500 Historical Components & Changes (Updated).csv'))
KELUAR = os.path.join(HERE, 'penyintas_sp500.json')


def kira(sejarah, tickers, mula='2013-01-01'):
    s = sejarah.copy(); s['date'] = pd.to_datetime(s.date); s = s[s.date >= mula]
    ahli = {}
    for d, tk in zip(s.date, s.tickers):
        for t in str(tk).split(','):
            t = AL.norm(t)
            if not t: continue
            if t not in ahli: ahli[t] = [d, d]
            ahli[t][1] = d
    A = pd.DataFrame([(t, a, b) for t, (a, b) in ahli.items()], columns=['ticker', 'mula', 'akhir'])
    A['ada'] = A.ticker.isin(set(tickers)); A['masih'] = A.akhir >= s.date.max()
    x = A[~A.ada]
    return dict(sumber='fja05680/sp500 "S&P 500 Historical Components & Changes (Updated).csv"', sejak=mula,
                tarikh_akhir_senarai=str(s.date.max().date()), ahli_sejak_2013=int(len(A)), masih_ahli=int(A.masih.sum()),
                ada_dalam_data=int(A.ada.sum()), tiada=int(len(x)), bekas_ahli=int((~A.masih).sum()),
                bekas_ahli_ada=int((A.ada & ~A.masih).sum()),
                tiada_ikut_tahun_keluar={int(k): int(v) for k, v in x.groupby(x.akhir.dt.year).size().items()},
                senarai_tiada=sorted(x.ticker))


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument('--data', required=True)
    ap.add_argument('--csv', default=None)
    a = ap.parse_args(argv)
    if a.csv:
        sej = pd.read_csv(a.csv)
    else:
        with urllib.request.urlopen(URL, timeout=60) as r:
            from io import StringIO
            sej = pd.read_csv(StringIO(r.read().decode('utf-8')))
    tk = pd.read_csv(os.path.join(a.data, 'pit_cache', 'shariah.csv')).ticker
    J = kira(sej, tk)
    with open(KELUAR, 'w', encoding='utf-8') as f:
        json.dump(J, f, indent=1)
    print({k: v for k, v in J.items() if k != 'senarai_tiada'})


if __name__ == '__main__':
    main()
