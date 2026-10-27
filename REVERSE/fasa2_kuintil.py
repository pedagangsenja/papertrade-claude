"""FASA 2 — laluan laju untuk membina semula populasi kuintil dan lajur indikator.

Sebab: `.cache/` tidak dicommit, dan `step1_run.py` menghabiskan hampir semua masanya pada metrik
hadapan (mfe/mae/henti, imbasan 252 bar setiap hari-saham) yang **tidak diperlukan** oleh FASA 2.
Skrip ini mengulang bahagian MURAH step1 (indikator `teras/ind.py`, run dan peristiwa sah
`teras/run.py`) dan bahagian kuintil step3 — definisi yang sama, modul yang sama, tanpa menulis
ke mana-mana fail FASA 1.

Output (nama berasingan, tidak sekali-kali menimpa cache FASA 1):
  .cache/ind2_<TAHUN>.parquet     indikator + dalam_univ + jenis_peristiwa + hasil + kumpulan_data
  .cache/kuintil2_<TAHUN>.json    sempadan kuintil (populasi: peristiwa sah kumpulan A)

Jika `.cache/kuintil_<TAHUN>.json` (laluan rasmi) ada, skrip membandingkan sempadan dan mencetak
beza maksimum — semakan bahawa laluan laju ini setara.

Guna: python3 REVERSE/fasa2_kuintil.py 2025
"""
import argparse
import json
import sys
import time
from pathlib import Path

import numpy as np
import pandas as pd

AKAR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(AKAR))
from REVERSE.teras import data as D, ind as I, run as R, signal as S  # noqa: E402

CACHE = AKAR / 'REVERSE' / '.cache'


def bina_tahun(th):
    t0 = time.time()
    univ = D.universe()
    tick = D.tickers_tahun(th, univ)
    mula, akhir = f'{th - 2}-06-01', '2026-10-16'
    fr = D.muat_harga(tick, mula, akhir)
    ix = D.muat_indeks(mula, akhir)
    spy = ix['SPY']['close']
    kal = spy.index
    peta = D.peta_sektor(list(fr))
    si = D.indeks_sektor(fr, peta, univ, kal)
    ikonteks = I.kira_indeks({k: v['close'] for k, v in ix.items()})
    ahli = D.topeng_bulan(univ)
    kump = univ.drop_duplicates('ticker').set_index('ticker')['kumpulan']
    print(f'[{time.time()-t0:.0f}s] ticker {len(fr)} | bar {len(kal)} | sektor {si.shape[1]}')
    t_awal, t_akhir = pd.Timestamp(f'{th}-01-01'), pd.Timestamp(f'{th}-12-31')
    blok = []
    for n_, (tk, g) in enumerate(fr.items()):
        if len(g) < 260:
            continue
        sek = peta.loc[tk, 'sektor']
        ind = I.kira(g, spy=spy, sektor_idx=si[sek] if sek in si.columns else None)
        ema21 = ind['ema21']
        layak, _ = R.jumpa_run(g, ema21)
        idx = g.index
        m = (idx >= t_awal) & (idx <= t_akhir)
        pos = np.flatnonzero(m)
        if pos.size == 0:
            continue
        per = {p[0]: p for p in R.peristiwa_sah(g, ema21)}
        hari_sah = {rec['i_sah']: rec for rec in layak if rec['i_sah'] >= 0}
        julat_run = [(rec['i_mula'], rec['i_tamat'], rec) for rec in layak]
        sub = ind.iloc[pos].copy()
        sub.insert(0, 'ticker', tk)
        sub.insert(1, 'tarikh', idx[pos])
        ym = idx[pos].year * 100 + idx[pos].month
        sub['dalam_univ'] = [1.0 if (tk, int(x)) in ahli else 0.0 for x in ym]
        sub['kumpulan_data'] = kump.get(tk, '?')
        jen, hasil = [], []
        for i in pos:
            if i not in per:
                jen.append('')
                hasil.append('')
                continue
            if i in hari_sah:
                rec = hari_sah[i]
                jen.append('mula_run')
            else:
                rec = None
                for i0, i1, rr in julat_run:
                    if i0 <= i <= i1:
                        rec = rr
                        break
                jen.append('dalam_run' if rec is not None else 'tiada_run')
            hasil.append('GAGAL' if rec is None else R.kelas_kumpulan(rec['naik_rendah']))
        sub['jenis_peristiwa'] = jen
        sub['hasil'] = hasil
        blok.append(sub.reset_index(drop=True))
        if n_ % 400 == 0:
            print(f'  {n_}/{len(fr)} [{time.time()-t0:.0f}s]')
    sig = pd.concat(blok, ignore_index=True)
    sig = sig.join(ikonteks.reindex(sig['tarikh']).reset_index(drop=True))
    for c in sig.columns:
        if sig[c].dtype == 'float64':
            sig[c] = sig[c].astype('float32')
    sig.to_parquet(CACHE / f'ind2_{th}.parquet', index=False)
    print(f'[{time.time()-t0:.0f}s] ind2_{th}.parquet {len(sig)} baris')
    return sig


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('tahun', type=int)
    a_ = ap.parse_args()
    th = a_.tahun
    f = CACHE / f'ind2_{th}.parquet'
    sig = pd.read_parquet(f) if f.exists() else bina_tahun(th)
    ev = sig[(sig.jenis_peristiwa != '') & (sig.dalam_univ == 1)]
    pop = ev[ev.kumpulan_data == 'A']
    print(f'peristiwa sah {len(ev)} | POPULASI KUINTIL (kumpulan A) {len(pop)}')
    simpan, buang = S.dedup(pop)
    kuin = S.kuintil(pop, simpan)
    (CACHE / f'kuintil2_{th}.json').write_text(json.dumps(
        dict(populasi='peristiwa sah kumpulan A (laluan laju FASA 2)', n=int(len(pop)),
             simpan=simpan, dibuang=[dict(buang=b, kerana=s, rho=round(r, 3))
                                     for b, s, r in buang], sempadan=kuin), indent=1))
    print(f'dedup: simpan {len(simpan)} | dibuang {len(buang)}')
    rasmi = CACHE / f'kuintil_{th}.json'
    if rasmi.exists():
        k0 = json.loads(rasmi.read_text())
        beza = []
        for k, v in kuin.items():
            w = k0['sempadan'].get(k)
            if not w:
                beza.append((k, 'tiada dalam rasmi'))
                continue
            for hj in ('q1', 'q5'):
                d = abs(v[hj] - w[hj]) / max(abs(w[hj]), 1e-9)
                beza.append((f'{k}.{hj}', d))
        num = [d for _, d in beza if isinstance(d, float)]
        print(f'SEMAKAN lawan laluan rasmi: n_pop rasmi {k0["n"]} lwn laju {len(pop)} | '
              f'beza relatif maks {max(num) if num else float("nan"):.2e} | '
              f'indikator sama: {set(kuin) == set(k0["sempadan"])}')


if __name__ == '__main__':
    main()
