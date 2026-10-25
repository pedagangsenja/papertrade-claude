# STEP-2 M168 — Pulih MACD + Silang SMA10/20 (teknik manual pengguna; enjin v1.2 beku, set 431, portfolio 8 slot).
# Jalan: python3 WFO/kaedah_baru/step2_M168.py [folder_keluar] [--proses 4] [--benih 20]
# Output dalam folder_keluar (lalai: folder semasa):
#   M168.csv        baris registry (lajur LAJUR2): semua 38 varian set 431, kemudian S1–S4 bagi setiap varian
#   M168_kukuh.csv  kekukuhan setiap varian: CAGR hingga Dis 2025, tanpa 10 terbaik (buang berulang dagangan DIAMBIL portfolio,
#                   slot diisi semula), belian rawak tempoh pegang sama (>= 20 benih; R-saham: saham rawak pada tarikh masuk dan
#                   tempoh sama, melalui portfolio; R-masa: saham sama, tarikh masuk rawak, tempoh sama, purata dagangan),
#                   sebab keluar, dagangan diambil portfolio
#   m168.pkl        T dan lengkung ekuiti setiap varian (431)
# Modul: WFO/kaedah_baru/M168.py (sedia(fr, idx, varian=...); di luar kod/kaedah/ semasa moratorium); registry: BacktestShariah2/kod/registry/M168.csv.
# Enjin tidak diubah: portfolio() direplika dalam ambil() HANYA untuk mengetahui dagangan yang diambil (lengkung disemak sama).
import sys, os, argparse, time, pickle
REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path[:0] = [os.path.join(REPO, 'BacktestShariah2', 'kod'), os.path.join(REPO, 'WFO', 'kaedah_baru')]
import tambahan
from tambahan import *
tambahan.cari = lambda nama: os.path.join(REPO, 'data_mentah', nama)   # lokasi data repo; enjin tidak diubah
import enjin
try:
    from kaedah import M168 as M          # selepas diaktifkan (kod/kaedah/M168.py)
except ImportError:
    import M168 as M                      # semasa moratorium (WFO/kaedah_baru/M168.py)

FR = IDX = ASAL = None
O = C = None          # matriks buka/tutup (tarikh x saham) untuk belian rawak


def ambil(T, fr, slots=8, w=0.125):
    """Replika tepat enjin.portfolio() v1.2 yang juga memulangkan indeks baris T yang DIAMBIL (masuk portfolio)."""
    dates = sorted(set().union(*[g.index for g in fr.values()])); dates = [x for x in dates if x >= pd.Timestamp(START)]
    T = T[T.ent >= pd.Timestamp(START)].sort_values(['ent', 'rank'], ascending=[True, False])
    byent = {k: v for k, v in T.groupby('ent')}; cl = {t: g.close for t, g in fr.items()}
    eq = cash = 1.0; pos = []; curve = []; diambil = []
    for dt in dates:
        keep = []
        for p in pos:
            if p['ex'] == dt: cash += p['a'] * (1 + p['ret'])
            else: keep.append(p)
        pos = keep
        if dt in byent:
            for k, r in byent[dt].iterrows():
                if len(pos) >= slots: break
                if any(p['t'] == r.ticker for p in pos): continue
                a = min(cash, eq * w)
                if a <= 0: break
                cash -= a; pos.append(dict(t=r.ticker, ex=r.ex, ret=r.ret, a=a, ent=dt)); diambil.append(k)
        keep = []
        for p in pos:
            if p['ex'] == dt and p['ent'] == dt: cash += p['a'] * (1 + p['ret'])
            else: keep.append(p)
        pos = keep
        mv = sum(p['a'] * cl[p['t']].asof(dt) / cl[p['t']].asof(p['ent']) if p['ent'] != dt else p['a'] for p in pos)
        eq = cash + mv; curve.append((dt, eq))
    return pd.Series(dict(curve)), diambil


def tanpa_terbaik(T, fr, k=10):
    """Buang dagangan terbaik yang DIAMBIL portfolio secara berulang (slot diisi semula), k kali (konvensyen spec M-lama)."""
    T = T.reset_index(drop=True); buang = []
    for _ in range(k):
        cv, d = ambil(T, fr)
        if not d: break
        b = T.loc[d, 'ret'].idxmax(); buang.append((T.ticker[b], round(float(T.ret[b]), 3))); T = T.drop(index=b)
    cv, _ = ambil(T, fr)
    return enjin._cagr(cv), buang


def matriks(fr):
    tarikh = pd.DatetimeIndex(sorted(set().union(*[g.index for g in fr.values()])))
    tk = sorted(fr)
    o = pd.DataFrame({t: fr[t].open for t in tk}).reindex(tarikh)
    c = pd.DataFrame({t: fr[t].close for t in tk}).reindex(tarikh)
    return tarikh, tk, o.values.astype(float), c.values.astype(float)


def rawak_saham(T, benih):
    """R-saham: setiap dagangan diganti saham rawak (ada bar pada tarikh masuk dan keluar), tarikh masuk/keluar dan jenis harga
       keluar sama (buka jika 'isyarat keluar', tutup jika lain). rank asal dikekalkan supaya urutan slot sama."""
    tarikh, tk, o, c = O
    T = T[T.ent >= pd.Timestamp(START)].reset_index(drop=True)
    e = tarikh.get_indexer(T.ent); x = tarikh.get_indexer(T.ex); buka = (T.why == 'isyarat keluar').values
    rng = np.random.default_rng(benih); u = rng.integers(0, len(tk), len(T))
    for _ in range(200):
        px = np.where(buka, o[x, u], c[x, u]); pe = o[e, u]
        sah = np.isfinite(px) & np.isfinite(pe) & (pe > 0)
        if sah.all(): break
        u[~sah] = rng.integers(0, len(tk), (~sah).sum())
    px = np.where(buka, o[x, u], c[x, u]); pe = o[e, u]
    R = T.copy(); R['ticker'] = [tk[i] for i in u]; R['ret'] = px / pe * (1 - COST) / (1 + COST) - 1
    return R[np.isfinite(R.ret)]


def rawak_masa(T, benih):
    """R-masa: saham sama, tarikh masuk rawak (>= START), tempoh bar sama; purata pulangan dagangan."""
    rng = np.random.default_rng(benih); out = []
    for t, d in T[T.ent >= pd.Timestamp(START)].groupby('ticker'):
        g = FR[t]; ix = g.index; o_, c_ = g.open.values, g.close.values; p0 = ix.searchsorted(pd.Timestamp(START))
        for r in d.itertuples():
            L = ix.get_loc(r.ex) - ix.get_loc(r.ent); hi = len(ix) - 1 - L
            if hi <= p0: continue
            e = int(rng.integers(p0, hi + 1)); px = o_[e + L] if r.why == 'isyarat keluar' else c_[e + L]
            out.append(px / o_[e] * (1 - COST) / (1 + COST) - 1)
    return float(np.mean(out)) if out else np.nan


def pre20(T):
    """Median pulangan 20 hari sebelum isyarat (%; tutup hari isyarat / tutup 20 bar sebelum - 1), takrif kod/jenis_kaedah.csv."""
    v = []
    for t, d in T.groupby('ticker'):
        c = FR[t].close.values; ix = FR[t].index.get_indexer(d.sig)
        v += [c[i] / c[i - 20] - 1 for i in ix if i >= 20]
    return round(float(np.median(v)) * 100, 2) if v else np.nan


def catatan(nm):
    p = M.VARIAN_SEMUA[nm]
    if p['mod'] == 'silang':
        return 'Kawalan: beli buka esok selepas SMA10 tutup silang atas SMA20; keluar silang bawah (buka esok); tiada henti'
    asas = 'Alert = histogram MACD(12,26,9) negatif -> positif; '
    if p['mod'] == 'alert':
        s = asas + f"tanpa syarat jatuh; silang SMA10 atas SMA20 0..{p['K']} hari selepas alert"
    else:
        s = asas + (f"fasa jatuh: SMA10<SMA20 >= {p['J']} daripada {M.tetingkap(p['J'])} hari hingga hari alert, tutup alert "
                    f"<= {1 - p['D']:.2f} x maks high 60 hari; silang SMA10 atas SMA20 0..{p['K']} hari selepas alert")
    s += '; beli buka esok; keluar silang bawah SMA10/20 (buka esok); tiada sasaran, tiada tmax; rank ROC63'
    s += '; henti kecemasan 0.99 x low terendah fasa jatuh hingga hari isyarat (langkau buka <= henti)' if p['henti'] else '; tiada henti'
    return s


def kerja(nm):
    t0 = time.time(); p = M.VARIAN_SEMUA[nm]; henti = p['henti']
    fr = FR
    M.sedia(fr, IDX, varian=nm)
    T = trades(fr, tmax=M.TMAX, warm=M.WARM); cv = portfolio(T, fr)
    cat = catatan(nm)
    r431 = baris2('431', 'M168', M.NAMA, nm, T, cv, fr, IDX, henti, cat)
    cv2, d = ambil(T, fr)
    assert np.allclose(cv2.values, cv.values), 'replika portfolio tidak sama'
    sub = []
    for s in SETS:
        f = subset(fr, ASAL, s); Ts = T[T.ticker.isin(f.keys())]; cs = portfolio(Ts, f)
        sub.append(baris2(s, 'M168', M.NAMA, nm, Ts, cs, f, IDX, henti, cat))
    c10, buang = tanpa_terbaik(T, fr)
    Te = T[T.ent >= pd.Timestamp(START)]
    rs_c, rs_avg, rm_avg = [], [], []
    for b in range(NB):
        R = rawak_saham(T, 1000 + b); rs_c.append(enjin._cagr(portfolio(R, fr))); rs_avg.append(R.ret.mean())
        rm_avg.append(rawak_masa(T, 2000 + b))
    why = Te.why.value_counts(normalize=True)
    k = dict(varian=nm, mod=p['mod'], J=p['J'], D=p['D'], K=p['K'], henti=henti, cagr=r431['cagr'], mdd=r431['mdd'],
             n=r431['n'], win=r431['win'], avg=r431['avg'], days=r431['days'], keputusan=r431['keputusan'], skor=r431['skor'],
             gate_gagal=r431['gate_gagal'], ew_cagr=r431['ew_cagr'],
             spy_cagr=round(penanda(IDX, fr)['SPY']['cagr'], 4), dis25=round(enjin._cagr(cv[:'2025-12-31']), 4),
             diambil=len(d), tanpa10=round(c10, 4), tanpa10_buang=' '.join(f'{a}:{b:+.2f}' for a, b in buang),
             rawak_benih=NB, rawak_cagr_med=round(float(np.median(rs_c)), 4), rawak_cagr_p95=round(float(np.percentile(rs_c, 95)), 4),
             rawak_cagr_min=round(float(np.min(rs_c)), 4), rawak_cagr_maks=round(float(np.max(rs_c)), 4),
             lebihan_cagr=round(r431['cagr'] - float(np.median(rs_c)), 4),
             p_rawak_ge=round(float(np.mean(np.array(rs_c) >= r431['cagr'])), 3),
             rawak_saham_avg=round(float(np.mean(rs_avg)), 5), lebihan_avg_saham=round(float(Te.ret.mean() - np.mean(rs_avg)), 5),
             rawak_masa_avg=round(float(np.nanmean(rm_avg)), 5), lebihan_avg_masa=round(float(Te.ret.mean() - np.nanmean(rm_avg)), 5),
             keluar_isyarat=round(float(why.get('isyarat keluar', 0)), 4), keluar_henti=round(float(why.get('henti', 0)), 4),
             keluar_hujung=round(float(why.get('hujung', 0)), 4),
             pre20_median=pre20(Te),
             **{f'{s}_cagr': x['cagr'] for s, x in zip(SETS, sub)}, **{f'{s}_keputusan': x['keputusan'] for s, x in zip(SETS, sub)},
             **{f'{s}_ew': x['ew_cagr'] for s, x in zip(SETS, sub)})
    k['s14_atasi_ew'] = sum(x['cagr'] > x['ew_cagr'] for x in sub)
    k['s14_lulus_gate'] = sum(not x['gate_gagal'] for x in sub)
    r431['catatan'] = (cat + f"; tanpa 10 terbaik (diambil, berulang) {c10:.1%}; {NB}x belian rawak (saham rawak, tarikh & tempoh "
                       f"sama) CAGR median {k['rawak_cagr_med']:.1%} (lebihan {k['lebihan_cagr'] * 100:+.1f} mata)")
    print(f"{nm[:44]:44s} {r431['keputusan']:10s} {str(r431['skor']):5s} CAGR {r431['cagr']:.3f} MDD {r431['mdd']:.3f} n {r431['n']} "
          f"t10 {c10:.3f} rawak {k['rawak_cagr_med']:.3f} S {[x['cagr'] for x in sub]} {round(time.time() - t0)}s", flush=True)
    return nm, r431, sub, k, (T, cv)


def main(argv=None):
    global FR, IDX, ASAL, O, NB
    ap = argparse.ArgumentParser(); ap.add_argument('keluar', nargs='?', default='.')
    ap.add_argument('--proses', type=int, default=4); ap.add_argument('--benih', type=int, default=20)
    ap.add_argument('--varian', nargs='*'); a = ap.parse_args(argv)
    NB = a.benih; t0 = time.time()
    FR, IDX, ASAL = muat(); O = matriks(FR)
    FR = {t: g[['open', 'high', 'low', 'close', 'volume', 'turnover']].copy() for t, g in FR.items()}
    VAR = a.varian or list(M.VARIAN_SEMUA)
    print('data siap', len(FR), 'saham', round(time.time() - t0), 's; varian', len(VAR), flush=True)
    if a.proses > 1:
        import multiprocessing as mp
        with mp.get_context('fork').Pool(a.proses) as pool:
            hasil = pool.map(kerja, VAR, chunksize=1)
    else:
        hasil = [kerja(v) for v in VAR]
    susun = {nm: i for i, nm in enumerate(VAR)}; hasil.sort(key=lambda h: susun[h[0]])
    rows = [h[1] for h in hasil] + [x for h in hasil for x in h[2]]
    pd.DataFrame(rows, columns=LAJUR2).to_csv(os.path.join(a.keluar, 'M168.csv'), index=False)
    pd.DataFrame([h[3] for h in hasil]).to_csv(os.path.join(a.keluar, 'M168_kukuh.csv'), index=False)
    pickle.dump({h[0]: h[4] for h in hasil}, open(os.path.join(a.keluar, 'm168.pkl'), 'wb'))
    print('siap', round(time.time() - t0), 's')


NB = 20
if __name__ == '__main__':
    main()
