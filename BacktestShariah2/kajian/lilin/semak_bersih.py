"""Semakan silang kolam dengan AUTOTUNE A01 "ujian bersih" (2013-01-01 – 2018-12-31, PARAM asal, A+B).

Portfolio 8 slot × 12.5% (enjin_at.Pasaran) atas dagangan laluan 1 kolam yang masuk dalam tetingkap; dagangan yang
keluar selepas 2018-12-31 dipotong kepada tutup 2018-12-31 (seperti 'hujung' enjin). Banding dengan cagr_bersih
dalam AUTOTUNE/hasil/papan.json. Beza kecil dijangka (pemanasan data 2011 lawan 400 hari; pemotongan).
Guna: python3 BacktestShariah2/kajian/lilin/semak_bersih.py [dir_kolam]
"""
import json, os, sys, warnings
import numpy as np, pandas as pd

os.environ.setdefault('NUMBA_CACHE_DIR', '/tmp/claude-0/-home-user-papertrade-claude/0793050f-2ee1-522e-9bf0-b633a13089db/scratchpad/numba')
AKAR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
sys.path[:0] = [os.path.join(AKAR, 'AUTOTUNE', 'teras')]
import data as D, enjin_at as E, objektif as O  # noqa: E402

DIR = sys.argv[1] if len(sys.argv) > 1 else \
    '/tmp/claude-0/-home-user-papertrade-claude/0793050f-2ee1-522e-9bf0-b633a13089db/scratchpad/lilin'
B0, B1 = pd.Timestamp('2013-01-01'), pd.Timestamp('2018-12-31')


def main():
    warnings.filterwarnings('ignore')
    P = pd.read_parquet(os.path.join(DIR, 'kolam.parquet'),
                        columns=['method', 'ticker', 'entry_date', 'exit_date', 'trade_ret', 'rank_value',
                                 'dagangan_enjin', 'pos', 'kos'])
    P = P[P.dagangan_enjin & (P.entry_date <= B1)]
    fr, idx, univ = D.muat('2011-01-01', B1, 'AB', dir=os.path.join(AKAR, 'AUTOTUNE', '.cache'))
    pas = E.Pasaran(fr, B0, B1)
    papan = {x['id']: x for x in json.load(open(os.path.join(AKAR, 'AUTOTUNE', 'hasil', 'papan.json')))['kaedah']}
    out = []
    for m, T in P.groupby('method'):
        T = T.copy()
        lewat = T.exit_date > B1
        # potong: keluar pada tutup 2018-12-31 (pulangan semula dikira daripada harga, kos dua sisi)
        for r in T[lewat].itertuples():
            g = fr[r.ticker]
            e = g.open.loc[r.entry_date]; x = g.close.loc[:B1].iloc[-1]
            T.loc[r.Index, 'trade_ret'] = x / e * (1 - r.kos) / (1 + r.kos) - 1
            T.loc[r.Index, 'exit_date'] = g.index[g.index <= B1][-1]
        T = T.rename(columns={'entry_date': 'ent', 'exit_date': 'ex', 'trade_ret': 'ret', 'rank_value': 'rank'})
        cv = pas.lengkung(T[['ticker', 'ent', 'ex', 'ret', 'rank']])
        cagr = O.cagr(cv)
        out.append(dict(kaedah=m, cagr_kolam=round(cagr, 4), cagr_bersih_autotune=papan.get(m, {}).get('cagr_bersih'),
                        n=len(T)))
    R = pd.DataFrame(out)
    R['beza'] = R.cagr_kolam - R.cagr_bersih_autotune
    print(R.to_string(index=False))
    print('korelasi', R[['cagr_kolam', 'cagr_bersih_autotune']].corr().iloc[0, 1])


if __name__ == '__main__':
    main()
