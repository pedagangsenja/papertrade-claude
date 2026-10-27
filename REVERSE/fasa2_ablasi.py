"""FASA 2 — ablasi 2x2 dan portfolio bergabung (SPEC §13.12 B).

Menukar sasaran daripada MFE/puncak (FASA 1) kepada **pulangan boleh didagangkan**, dan unit
penilaian daripada silo setahun kepada **tempoh bergabung 2020-01-01 – 2026-10-16**.

Empat arm, kos dan polisi exit yang sama (SPEC §13.12 B4):
  S+R  signal          x susunan rs_spy_6b        S+X  signal          x susunan rawak (benih 42)
  X+R  universe penuh  x susunan rs_spy_6b        X+X  universe penuh  x susunan rawak
Signal menyumbang hanya jika S+R > X+R DAN S+X > X+X.

Had calon 8 setiap hari = bilangan slot: set yang diuji ialah set yang portfolio boleh ambil.
Tiada signal baharu, tiada penalaan; senarai signal = union corong 2020-2025 (keputusan_*.csv).

Guna: python3 REVERSE/fasa2_ablasi.py [--tahun 2020 2021 ...]
Output: REVERSE/fasa2_jangkaan.csv, REVERSE/fasa2_portfolio.csv, .cache/fasa2_dagangan.parquet
"""
import argparse
import hashlib
import json
import sys
import time
from pathlib import Path

import numpy as np
import pandas as pd

AKAR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(AKAR))
from REVERSE.teras import data as D, signal as S, stat as T  # noqa: E402
from REVERSE.teras.kos import kos_sisi  # noqa: E402

CACHE = AKAR / 'REVERSE' / '.cache'
KELUAR = AKAR / 'REVERSE'
TAHUN = [2020, 2021, 2022, 2023, 2024, 2025]
SLOT, BAHAGIAN, UFUK = 8, 0.125, 252
HUJUNG = '2026-10-16'
POLISI = ['chandelier_4atr', 'jual_hari63', 'pegang_252']
BENIH = 42


def kunci_rawak(tk, d):
    """Kunci susunan rawak deterministik (benih 42 tetap, bebas susunan baris)."""
    return int(hashlib.md5(f'{BENIH}|{tk}|{d}'.encode()).hexdigest()[:12], 16)


def senarai_signal():
    """Union semua signal yang pernah masuk corong 2020-2025 — ditetapkan sebelum larian."""
    u = set()
    for f in sorted(KELUAR.glob('keputusan_*.csv')):
        u |= set(pd.read_csv(f).signal)
    return sorted(u)


def _ambil8(b, kol):
    """8 calon teratas setiap hari ikut `kol` menurun."""
    b = b[np.isfinite(b[kol].to_numpy('float64'))]
    if not len(b):
        return b[['ticker', 'tarikh']].assign(urutan=0)
    h = (b.sort_values(['tarikh', kol], ascending=[True, False], kind='stable')
          .groupby('tarikh', sort=False).head(SLOT)[['ticker', 'tarikh']].copy())
    h['urutan'] = h.groupby('tarikh', sort=False).cumcount()
    return h


def pilihan_tahun(th, signals):
    """Pilihan harian setiap arm bagi satu tahun kajian."""
    fk = CACHE / f'kuintil_{th}.json'
    if not fk.exists():
        fk = CACHE / f'kuintil2_{th}.json'   # laluan laju fasa2_kuintil.py
    kuin = json.loads(fk.read_text())['sempadan']
    perlu = (set(['ticker', 'tarikh', 'dalam_univ', 'rs_spy_6b']) | set(kuin)
             | set(S.BINARI) | set(S.BINARI_TANDA) | set(S.PEMICU))
    import pyarrow.parquet as pq
    f = CACHE / f'signals_{th}.parquet'
    if not f.exists():
        f = CACHE / f'ind2_{th}.parquet'
    ada = set(pq.ParquetFile(f).schema.names)
    sig = pd.read_parquet(f, columns=sorted(perlu & ada))
    sig = sig.loc[sig.dalam_univ == 1].reset_index(drop=True)
    sg = S.bina(sig, kuin)
    base = pd.DataFrame(dict(
        ticker=sig.ticker.to_numpy(), tarikh=sig.tarikh.to_numpy(),
        rs=sig.rs_spy_6b.to_numpy('float64'),
        rk=np.array([kunci_rawak(t, d) for t, d in zip(sig.ticker, sig.tarikh)], dtype='float64')))
    out = [_ambil8(base, 'rs').assign(arm='X+R', signal='-'),
           _ambil8(base, 'rk').assign(arm='X+X', signal='-')]
    for nm in signals:
        if nm not in sg or not sg[nm].any():
            continue
        b = base[sg[nm]]
        out.append(_ambil8(b, 'rs').assign(arm='S+R', signal=nm))
        out.append(_ambil8(b, 'rk').assign(arm='S+X', signal=nm))
    p = pd.concat(out, ignore_index=True)
    p['tahun'] = th
    print(f'  {th}: {len(sig)} hari-saham dalam universe -> pilihan {len(p)}')
    return p


def siri_ticker(g):
    c = g['close'].to_numpy('float64')
    o = g['open'].to_numpy('float64')
    h, l = g['high'], g['low']
    tr = pd.concat([h - l, (h - g['close'].shift(1)).abs(),
                    (l - g['close'].shift(1)).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1 / 14, adjust=False, min_periods=14).mean().to_numpy('float64')
    to = (g['close'] * g['volume']).rolling(20, min_periods=10).median().to_numpy('float64')
    return c, o, atr, to


def keluar3(c, o, atr, i, n):
    """{polisi: (bar keluar, harga kasar, hari pegang)} — konvensyen step9 (jual pada buka)."""
    i0 = i + 1
    b = min(i + UFUK, n - 1)
    if i0 >= n or b <= i0:
        return None
    cw = c[i0:b + 1]
    puncak = np.maximum.accumulate(np.where(np.isfinite(cw), cw, -np.inf))
    ipk = np.maximum.accumulate(np.where(cw >= puncak, np.arange(cw.size), 0))
    i63 = min(i + 63, n - 1)
    out = {'pegang_252': (b, c[b], b - i0 + 1),
           'jual_hari63': (i63, o[i63] if np.isfinite(o[i63]) else c[i63], i63 - i0 + 1)}
    fire = cw <= puncak - 4.0 * atr[i0:b + 1][ipk]
    if fire.any():
        k = min(i0 + int(np.argmax(fire)) + 1, n - 1)
        out['chandelier_4atr'] = (k, o[k] if np.isfinite(o[k]) else c[k], k - i0 + 1)
    else:
        out['chandelier_4atr'] = (b, c[b], b - i0 + 1)
    return out


def kira_dagangan(pilih, spy):
    """Pulangan boleh dagang setiap (ticker, tarikh) unik x tiga polisi, kos penuh dua sisi."""
    unik = pilih[['ticker', 'tarikh']].drop_duplicates()
    per_tk = {tk: g.tarikh.to_numpy() for tk, g in unik.groupby('ticker', sort=False)}
    t0 = time.time()
    fr = D.muat_harga(sorted(per_tk), '2018-06-01', HUJUNG)
    print(f'[{time.time()-t0:.0f}s] harga {len(fr)} ticker')
    sp = spy.to_numpy('float64')
    spi = {d: k for k, d in enumerate(spy.index)}
    rows = []
    for n_, (tk, g) in enumerate(fr.items()):
        c, o, atr, to = siri_ticker(g)
        n, pos = c.size, g.index
        for d in per_tk.get(tk, ()):
            if d not in pos:
                continue
            i = int(pos.get_loc(d))
            if i + 1 >= n:
                continue
            ks = kos_sisi(to[i])
            masuk = o[i + 1] * (1 + ks)
            if not np.isfinite(masuk) or masuk <= 0:
                continue
            kel = keluar3(c, o, atr, i, n)
            if kel is None:
                continue
            d_masuk = pos[i + 1]
            a = spi.get(d_masuk)
            for pol, (k, harga, hari) in kel.items():
                if not np.isfinite(harga) or harga <= 0:
                    continue
                jual = harga * (1 - ks)
                d_keluar = pos[k]
                bq = spi.get(d_keluar)
                spul = (sp[bq] / sp[a] - 1.0) if (a is not None and bq is not None) else np.nan
                rows.append((tk, d, pol, float(jual / masuk - 1.0) * 100,
                             float(jual / masuk - 1.0 - spul) * 100, int(hari),
                             d_masuk, d_keluar, float(masuk), float(jual), int(k >= n - 1)))
        if n_ % 500 == 0:
            print(f'  dagangan {n_}/{len(fr)} [{time.time()-t0:.0f}s]')
    return pd.DataFrame(rows, columns=['ticker', 'tarikh', 'polisi', 'pulangan', 'lebihan_spy',
                                       'hari', 'tarikh_masuk', 'tarikh_keluar', 'harga_masuk',
                                       'harga_jual', 'terpotong'])


def boot_blok(nilai, blok, n=1000, benih=BENIH):
    """Bootstrap blok, vektor. Indeks blok sama seperti `teras/stat.py bootstrap_blok`
    (rng dan urutan panggilan yang sama), tetapi purata dikira daripada jumlah dan bilangan
    setiap blok supaya 1,000 ulangan tidak perlu menyalin nilai. Disemak dengan --semak-boot."""
    nilai = np.asarray(nilai, dtype='float64')
    ok = np.isfinite(nilai)
    nilai, blok = nilai[ok], np.asarray(blok)[ok]
    if nilai.size == 0:
        return (np.nan,) * 3
    unik, inv = np.unique(blok, return_inverse=True)
    b = unik.size
    jum = np.bincount(inv, weights=nilai, minlength=b)
    bil = np.bincount(inv, minlength=b).astype('float64')
    rng = np.random.default_rng(benih)
    ix = np.empty((n, b), dtype='int64')
    for k in range(n):
        ix[k] = rng.integers(0, b, b)
    out = jum[ix].sum(1) / np.maximum(bil[ix].sum(1), 1e-12)
    return (float(np.quantile(out, 0.05)), float(np.quantile(out, 0.50)),
            float(np.quantile(out, 0.95)))


def stat_arm(d):
    """Statistik satu (signal, arm, polisi): median, purata, purata dipangkas, bootstrap blok."""
    r = d.pulangan.to_numpy('float64')
    ex = d.lebihan_spy.to_numpy('float64')
    jk, km, pm, pk = T.jangkaan(r)
    pangkas = r[r <= np.quantile(r, 0.95)] if r.size >= 20 else r
    blok_t = d.ticker.to_numpy()
    blok_w = pd.to_datetime(pd.Series(d.tarikh.to_numpy())).dt.strftime('%G-W%V').to_numpy()
    bt = boot_blok(r, blok_t)
    bw = boot_blok(r, blok_w)
    et = boot_blok(ex, blok_t)
    ew = boot_blok(ex, blok_w)
    return dict(
        n=int(r.size), median=round(float(np.median(r)), 3), purata=round(float(np.mean(r)), 3),
        purata_dipangkas5=round(float(np.mean(pangkas)), 3),
        kadar_menang=round(km * 100, 2), jangkaan=round(jk, 3),
        purata_menang=round(pm, 2), purata_kalah=round(pk, 2),
        lebihan_spy_purata=round(float(np.nanmean(ex)), 3),
        lebihan_spy_median=round(float(np.nanmedian(ex)), 3),
        purata_bawah95_ticker=round(bt[0], 3), purata_bawah95_minggu=round(bw[0], 3),
        lebihan_bawah95_ticker=round(et[0], 3), lebihan_bawah95_minggu=round(ew[0], 3),
        median_hari=round(float(d.hari.median()), 1),
        pct_terpotong=round(float(d.terpotong.mean() * 100), 1))


def portfolio(pilih, dpol, tutup, kal):
    """Portfolio bergabung 8 slot x 12.5%, berterusan, nilai ditanda pasar setiap tutup."""
    if isinstance(tutup, pd.DataFrame):
        tutup = (tutup.to_numpy('float64'), {c: i for i, c in enumerate(tutup.columns)},
                 {d: i for i, d in enumerate(tutup.index)})
    px, kol_i, bar_i = tutup
    out = {}
    for pol, dd in dpol.items():
        # masuk pada TARIKH MASUK sebenar (buka d+1), bukan tarikh signal
        m = dd.merge(pilih[['ticker', 'tarikh', 'urutan']], on=['ticker', 'tarikh'], how='inner')
        peta = {}
        for tk, dm, u, hm, hj, dk, hr in zip(m.ticker, m.tarikh_masuk, m.urutan, m.harga_masuk,
                                             m.harga_jual, m.tarikh_keluar, m.hari):
            peta.setdefault(dm, []).append((u, tk, hm, hj, dk, hr))
        for d in peta:
            peta[d].sort()
        tunai, buka = 1.0, {}
        siri, n_masuk, n_tutup, slot_hari, hari_pegang = [], 0, 0, [], []
        for hari in kal:
            for t in [t for t, v in buka.items() if v['keluar'] <= hari]:
                v = buka.pop(t)
                tunai += v['unit'] * v['jual']
                n_tutup += 1
                hari_pegang.append(v['hari'])
            nilai = tunai
            bi = bar_i.get(hari)
            for t, v in buka.items():
                ki = kol_i.get(t)
                if ki is not None and bi is not None:
                    x = px[bi, ki]
                    if np.isfinite(x):
                        v['akhir'] = x
                nilai += v['unit'] * v['akhir']
            for _, t, hm, hj, dk, hr in peta.get(hari, ()):
                if len(buka) >= SLOT or t in buka or dk <= hari:
                    continue
                pos = min(nilai * BAHAGIAN, tunai)
                if pos <= 0:
                    break
                tunai -= pos
                buka[t] = dict(unit=pos / hm, jual=hj, keluar=dk, hari=hr, akhir=hm)
                n_masuk += 1
            siri.append((hari, tunai + sum(v['unit'] * v['akhir'] for v in buka.values())))
            slot_hari.append(len(buka))
        s = pd.Series([e for _, e in siri], index=pd.DatetimeIndex([d for d, _ in siri]))
        bl = s.resample('ME').last()
        bulan = pd.concat([pd.Series([bl.iloc[0] / 1.0 - 1]), bl.pct_change().dropna()]) * 100
        tn = max((s.index[-1] - s.index[0]).days / 365.25, 1e-9)
        out[pol] = dict(
            polisi=pol, n_posisi=n_masuk, n_tutup=n_tutup,
            purata_slot=round(float(np.mean(slot_hari)), 2),
            purata_hari_pegang=round(float(np.mean(hari_pegang)), 1) if hari_pegang else '',
            pulangan_jumlah=round((float(s.iloc[-1]) - 1) * 100, 2),
            cagr=round((max(float(s.iloc[-1]), 1e-9) ** (1 / tn) - 1) * 100, 2),
            mdd=round(T.mdd(s.to_numpy()), 2),
            median_bulanan=round(float(bulan.median()), 2),
            purata_bulanan=round(float(bulan.mean()), 2),
            pct_bulan_ge10=round(float((bulan >= 10).mean() * 100), 1),
            pct_bulan_positif=round(float((bulan > 0).mean() * 100), 1),
            bulan_terburuk=round(float(bulan.min()), 2))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--tahun', type=int, nargs='*', default=TAHUN)
    a_ = ap.parse_args()
    t0 = time.time()
    signals = senarai_signal()
    print(f'signal corong (union): {len(signals)} | tahun {a_.tahun}')
    fp = CACHE / f'fasa2_pilihan_{min(a_.tahun)}-{max(a_.tahun)}.parquet'
    if fp.exists():
        pil = pd.read_parquet(fp)
        if sorted(pil.tahun.unique()) != sorted(a_.tahun):
            pil = None
    else:
        pil = None
    if pil is None:
        pil = pd.concat([pilihan_tahun(th, signals) for th in a_.tahun], ignore_index=True)
        pil.to_parquet(fp, index=False)
    print(f'[{time.time()-t0:.0f}s] pilihan {len(pil)} | (ticker,tarikh) unik '
          f'{len(pil[["ticker","tarikh"]].drop_duplicates())}')
    ix = D.muat_indeks('2018-06-01', HUJUNG)
    spy = ix['SPY']['close']
    f = CACHE / f'fasa2_dagangan_{min(a_.tahun)}-{max(a_.tahun)}.parquet'
    if f.exists():
        dag = pd.read_parquet(f)
    else:
        dag = kira_dagangan(pil, spy)
        dag.to_parquet(f, index=False)
    print(f'[{time.time()-t0:.0f}s] dagangan {len(dag)}')

    dpol = {pol: g.reset_index(drop=True) for pol, g in dag.groupby('polisi')}
    rows = []
    for (sg, arm), p in pil.groupby(['signal', 'arm'], sort=False):
        kp_ = p[['ticker', 'tarikh']]
        for pol, dd in dpol.items():
            d = kp_.merge(dd, on=['ticker', 'tarikh'], how='inner')
            if len(d) < 30:
                continue
            rows.append(dict(signal=sg, arm=arm, polisi=pol, **stat_arm(d)))
        if len(rows) % 60 == 0:
            print(f'  statistik {len(rows)} baris')
    pd.DataFrame(rows).to_csv(KELUAR / 'fasa2_jangkaan.csv', index=False)
    print(f'[{time.time()-t0:.0f}s] fasa2_jangkaan.csv {len(rows)} baris')

    kal = spy.index[(spy.index >= pd.Timestamp(f'{min(a_.tahun)}-01-01'))
                    & (spy.index <= pd.Timestamp(HUJUNG))]
    tick = sorted(dag.ticker.unique())
    fr = D.muat_harga(tick, f'{min(a_.tahun)-1}-01-01', HUJUNG)
    tt = pd.DataFrame({t: g['close'] for t, g in fr.items()}).reindex(kal).ffill()
    tutup = (tt.to_numpy('float64'), {c: i for i, c in enumerate(tt.columns)},
             {d: i for i, d in enumerate(tt.index)})
    del fr, tt
    kp = {pol: g[['ticker', 'tarikh', 'tarikh_masuk', 'tarikh_keluar', 'harga_masuk',
                  'harga_jual', 'hari']].reset_index(drop=True)
          for pol, g in dag.groupby('polisi')}
    prow = []
    for (sg, arm), p in pil.groupby(['signal', 'arm'], sort=False):
        for pol, r in portfolio(p, kp, tutup, kal).items():
            prow.append(dict(signal=sg, arm=arm, **r))
    pf = pd.DataFrame(prow)
    spy_k = spy.reindex(kal).ffill()
    tn = max((kal[-1] - kal[0]).days / 365.25, 1e-9)
    pf['spy_jumlah'] = round(float(spy_k.iloc[-1] / spy_k.iloc[0] - 1) * 100, 2)
    pf['spy_cagr'] = round((float(spy_k.iloc[-1] / spy_k.iloc[0]) ** (1 / tn) - 1) * 100, 2)
    pf['spy_mdd'] = round(T.mdd(spy_k.to_numpy()), 2)
    pf.to_csv(KELUAR / 'fasa2_portfolio.csv', index=False)
    print(f'[{time.time()-t0:.0f}s] fasa2_portfolio.csv {len(pf)} baris')


if __name__ == '__main__':
    main()
