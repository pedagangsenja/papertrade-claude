"""Carian setup — semakan peringkat AKAUN bagi dua lorong + subset Shariah lorong trend (SPEC pindaan 14 Nov 2026 (s)).

Soalan: kadar tangkap bukan hasil akaun. Jika akaun hanya ada 10 slot (10 % setiap satu), apakah CAGR dan MDD buku setiap
setup dan buku gabungan, dan adakah ia mengatasi jalur rawak (saham rawak hari sama x tercile ATR %, henti dan keluar sama)?
Lorong swing: 8 setup dipercayai teratas (pegang minimum (p)). Lorong trend: 11 setup Dipercayai-T (pegang hingga 126 sesi).
Guna: python3 cs_akaun9.py <kerja>. Keluaran: hasil/AKAUN.md, AKAUN.csv, AKAUN_shariah.csv. Jangan sunting secara manual."""
import os
import pickle
import sys

import numpy as np
import pandas as pd

SINI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SINI)
import cs_atom as atom  # noqa: E402
import cs_cari as cari  # noqa: E402
import cs_keluar7 as k7  # noqa: E402
import cs_lapis as lapis  # noqa: E402
import cs_lapor as lapor  # noqa: E402
import cs_lengkap as lg  # noqa: E402
import cs_portfolio6 as p6  # noqa: E402
import cs_sahkan as sh  # noqa: E402
import cs_teras as teras  # noqa: E402
import cs_trend8 as t8  # noqa: E402

SWING = ['F43', 'F63', 'F65', 'F51', 'F50', 'F56', 'F39', 'F91']          # dikunci pindaan (s)
TREND = ['T01', 'T02', 'T03', 'T04', 'T05', 'T06', 'T07', 'T08', 'T10', 'T11', 'T12']
N_SLOT, HAD_MDD, N_ULANG = 10, 0.10, 200
TK40 = (4, 1 + [a[3] for a in t8.ATOM].index('tiada kemajuan (selepas 40 sesi, tutup < harga beli)') * t8.NG)


def satu(pan, e, R, sk, lab, rugi_had, rng, topeng, tahun, bulan):
    """Satu larian buku 10 slot: ukuran akaun dan ukuran dagangan yang DIAMBIL."""
    hari = pan['hari']
    amb = teras.pilih_slot(e, sk, pan['tid'], hari, np.lexsort((rng.random(len(e)), hari[e + 1])), N_SLOT)
    jum, bil = teras.jumlah_harian(e[amb], R[amb], sk[amb], pan['o'], pan['c'], hari, len(pan['hari_unik']))
    pr, dedah = jum / N_SLOT, bil / N_SLOT
    c, m = p6.ukur(pr[topeng['semua']])
    w = 1.0 if m == 0 else min(1.0, HAD_MDD / abs(m))
    c3, m3 = p6.ukur(pr[topeng['K3']])
    th = pd.Series(pr[topeng['semua']]).groupby(tahun[topeng['semua']]).apply(lambda x: float(np.prod(1 + x) - 1))
    Ra = R[amb]
    return {'isyarat': len(e), 'diambil': int(amb.sum()), 'bulan_beli': len(np.unique(bulan[hari[e[amb] + 1]])),
            'pendedahan': float(dedah[topeng['semua']].mean()), 'cagr': c, 'mdd': m,
            'cagr_had': p6.ukur(pr[topeng['semua']] * w)[0], 'cagr_K3': c3, 'mdd_K3': m3,
            'tahun_positif': int((th > 0).sum()), 'tahun': len(th), 'tahun_terburuk': float(th.min()),
            'tangkap': float(lab[amb].mean()), 'menang': float((Ra > 0).mean()), 'rugi_besar': float((Ra <= -rugi_had).mean()),
            'purata': float(Ra.mean()), 'pegang': float(np.median(sk[amb]) + 1)}


def buku(nama, lorong, pan, e, R, sk, lab, rugi_had, rawak, topeng, tahun, bulan):
    """Median 200 ulangan + jalur rawak. rawak(rng) -> (er, Rr, skr, labr): saham rawak hari sama x tercile, keluar sama."""
    S, W = [], []
    for i in range(N_ULANG):
        S.append(satu(pan, e, R, sk, lab, rugi_had, np.random.default_rng([atom.BENIH, 21, i]), topeng, tahun, bulan))
        rng = np.random.default_rng([atom.BENIH, 22, i])
        W.append(satu(pan, *rawak(rng), rugi_had, rng, topeng, tahun, bulan))
    S, W = pd.DataFrame(S), pd.DataFrame(W)
    b = {'buku': nama, 'lorong': lorong, **{k: float(S[k].median()) for k in S}}
    for k in ('cagr_had', 'cagr', 'mdd', 'tangkap', 'menang', 'rugi_besar', 'purata'):
        b.update({f'rawak_{k}': float(W[k].median()), f'rawak5_{k}': float(W[k].quantile(0.05)),
                  f'rawak95_{k}': float(W[k].quantile(0.95))})
    b['persentil'] = float((W.cagr_had < b['cagr_had']).mean())
    b['menambah'] = bool(b['cagr_had'] > 0 and b['cagr_had'] > b['rawak95_cagr_had'])
    cari.log(f"{nama}: diambil {b['diambil']:.0f}/{b['isyarat']:.0f}; CAGR pada MDD -10% {b['cagr_had'] * 100:+.2f} (rawak "
             f"{b['rawak_cagr_had'] * 100:+.2f}, p95 {b['rawak95_cagr_had'] * 100:+.2f}); MDD {b['mdd'] * 100:.1f}")
    return b


def _urut(sah, g):
    """Susunan bar layak ikut kumpulan (hari x tercile) untuk mencabut saham rawak kumpulan yang sama."""
    n_g = np.bincount(g[sah])
    return sah[np.argsort(g[sah], kind='stable')], n_g, np.cumsum(n_g) - n_g


def main(kerja):
    pan = cari.panel(kerja, 'B')
    L = lapis.muat(kerja, 'B')
    Lr = (L['L1'], L['L2'])
    hu, tm = pan['hari_unik'], atom.TEMPOH['B']
    topeng = {'semua': (hu >= tm[0][1]) & (hu <= tm[-1][2]), 'K3': (hu >= tm[-1][1]) & (hu <= tm[-1][2])}
    tahun, bulan = hu // 10000, hu // 100
    n_bulan, n_tahun = len(np.unique(bulan[topeng['semua']])), topeng['semua'].sum() / 252
    baris = []
    # ---------- lorong swing ----------
    XA, Tb = k7.siri_set(kerja, 'B'), lg.muat_asas(kerja, 'B')
    urut, n_g, mula_g = _urut(np.flatnonzero(pan['sah']), Tb['g'])
    D = {fid: (e0, s, kol) for fid, _, _, e0, s, kol in sh.setup_f(kerja, pan, Lr) if fid in SWING}
    assert sorted(D) == sorted(SWING), sorted(D)

    def swing(ev, kunci_):
        """(R, sk, tangkap penuh) bagi isyarat ev dengan (henti, lajur) setiap isyarat dalam kunci_."""
        R, sk, lab = np.zeros(len(ev)), np.zeros(len(ev), np.int64), np.zeros(len(ev), bool)
        for c_ in sorted(set(kunci_)):
            m = np.asarray([x == c_ for x in kunci_])
            St = k7.sedia_pan(pan, XA, ev[m])
            R[m], sk[m] = k7.hasil(*St[:7], k7.A1, k7.A2, k7.OP, c_[0], c_[1])
            lab[m] = (St[7][:, 0] > 0) & (R[m] >= lg.JADI)
        return R, sk, lab
    for nama, ahli in [(f, [f]) for f in SWING] + [('SWING8', SWING)]:
        e = np.concatenate([D[f][0] for f in ahli])
        kc = [D[f][1:] for f in ahli for _ in range(len(D[f][0]))]
        R, sk, lab = swing(e, kc)

        def rawak(rng, e=e, kc=kc):
            g = Tb['g'][e]
            er = urut[mula_g[g] + (rng.random(len(e)) * n_g[g]).astype(np.int64)]
            return (er, *swing(er, kc))
        baris.append(buku(nama, 'swing', pan, e, R, sk, lab, 0.08, rawak, topeng, tahun, bulan))
    # ---------- lorong trend ----------
    papan = {b['id']: b for b in pickle.load(open(os.path.join(kerja, 'cs08_papan.pkl'), 'rb'))}
    KL = pickle.load(open(os.path.join(kerja, 'cs08_keluar.pkl'), 'rb'))['pilih']
    XT = t8.siri_set(kerja, 'B')
    S8, V8, L8, G = t8.label_v(pan)
    urut8, n_g8, mula_g8 = _urut(np.flatnonzero(S8), G)
    E8 = {i: t8._ev_papan(kerja, 'B', pan, Lr, S8, papan[i]) for i in TREND}

    def trend(ev, kunci_):
        Ra, SK = t8._hasil(pan, XT, ev)
        ix = np.arange(len(ev))
        s_, k_ = np.asarray([c_[0] for c_ in kunci_]), np.asarray([c_[1] for c_ in kunci_])
        return Ra[ix, s_, k_].astype(np.float64), SK[ix, s_, k_].astype(np.int64), L8[ev, 0] > 0
    for nama, ahli, tetap in [(i, [i], None) for i in TREND] + [('TREND11', TREND, None), ('TREND11_TK40', TREND, TK40)]:
        e = np.concatenate([E8[i] for i in ahli])
        kc = [tetap or tuple(KL[i]) for i in ahli for _ in range(len(E8[i]))]
        R, sk, lab = trend(e, kc)

        def rawak(rng, e=e, kc=kc):
            g = G[e]
            er = urut8[mula_g8[g] + (rng.random(len(e)) * n_g8[g]).astype(np.int64)]
            return (er, *trend(er, kc))
        baris.append(buku(nama, 'trend', pan, e, R, sk, lab, 0.15, rawak, topeng, tahun, bulan))
    T = pd.DataFrame(baris)
    d_ = os.path.join(SINI, 'hasil')
    T.to_csv(os.path.join(d_, 'AKAUN.csv'), index=False, float_format='%.5f')
    # ---------- subset Shariah lorong trend ----------
    shar = set(open(os.path.join(lapor.BS2, 'data', 'harga', 'univ.txt')).read().split())
    shariah = np.asarray([t in shar for t in pan['ticker']])[pan['tid']]
    sb = []
    for i in sorted(papan):
        e0 = t8._ev_papan(kerja, 'B', pan, Lr, S8, papan[i])
        R, sk, _ = trend(e0, [tuple(KL[i])] * len(e0))
        amb = teras.satu_posisi(e0, sk, pan['tid'])
        e, R = e0[amb], R[amb]
        m = shariah[e]
        ok = m.sum() >= 30
        sb.append(dict(id=i, n=len(e), n_shariah=int(m.sum()), besar=float(L8[e, 0].mean()),
                       besar_shariah=float(L8[e[m], 0].mean()) if ok else np.nan,
                       a_besar_shariah=float(V8[e[m], 1].mean()) if ok else np.nan,
                       tb_shariah=float((R[m] >= t8.TB).mean()) if ok else np.nan,
                       menang_shariah=float((R[m] > 0).mean()) if ok else np.nan,
                       rugi15_shariah=float((R[m] <= -0.15).mean()) if ok else np.nan,
                       purata_shariah=float(R[m].mean()) if ok else np.nan))
    SB = pd.DataFrame(sb)
    SB.to_csv(os.path.join(d_, 'AKAUN_shariah.csv'), index=False, float_format='%.5f')
    # ---------- SPY (maklumat) ----------
    from AUTOTUNE.teras import data as Dt
    ix = pd.read_parquet(Dt.ambil(tag='autotune-data-a02') / 'idx.parquet')
    spy = ix[ix.ticker == 'SPY'].sort_values('date')
    sr = pd.Series(spy.close.pct_change().to_numpy(), index=(spy.date.dt.year * 10000 + spy.date.dt.month * 100
                                                              + spy.date.dt.day).to_numpy()).reindex(hu).fillna(0).to_numpy()
    cs_, ms_ = p6.ukur(sr[topeng['semua']])
    spy_had = p6.ukur(sr[topeng['semua']] * min(1.0, HAD_MDD / abs(ms_)))[0]
    try:
        sys.path.insert(0, os.path.join(lapor.BS2, 'standard'))
        import status_kad
        status = status_kad.baris()
    except Exception:
        status = '> **Status keputusan:** lihat `laporan/KAD_SKOR.md`; laporan ini BUKAN keputusan.'
    p = lambda x, k=1, t=False: '–' if x != x else (f'{x * 100:+.{k}f}' if t else f'{x * 100:.{k}f}')
    A = ['# Semakan peringkat AKAUN: buku 10 slot bagi lorong swing dan lorong trend (backtest; BUKAN bukti)', '', status, '',
         'Dijana `kajian/carian_setup/cs_akaun9.py`. Pradaftar: `kajian/SPEC_CARIAN_SETUP.md` pindaan 14 Nov 2026 (s), dikomit '
         'sebelum dijalankan. **Jangan sunting secara manual.**', '',
         f'Soalan: kadar tangkap bukan hasil akaun. Akaun 10 slot (10 % setiap satu), kumpulan B, {tm[0][1]} – {tm[-1][2]} '
         f'({n_tahun:.1f} tahun), kos 0.5 % pusingan, tunai 0 %; isyarat berlebihan dipilih rawak, {N_ULANG} ulangan (angka = median). '
         '**Jalur rawak** = isyarat yang sama digantikan saham rawak pada hari dan tahap turun-naik yang sama, dengan henti dan '
         'keluar yang sama. **"CAGR pada MDD −10 %"** = pendedahan dikecilkan (baki tunai) sehingga kejatuhan terburuk akaun '
         'kira-kira −10 %, iaitu toleransi pengguna. **Bacaan dikunci:** buku "menambah" hanya jika angka itu positif DAN melebihi '
         f'persentil ke-95 jalur rawak. Maklumat sahaja: SPY beli-dan-pegang pada MDD −10 % = {p(spy_had, 2, True)} % setahun '
         f'(CAGR {p(cs_, 1, True)} %, MDD {p(ms_, 1, True)} %).', '']
    for lorong, tajuk, tk, rb in (('swing', '## 1. Lorong swing (pegang hingga 4 minggu; pegang minimum 3 sesi)', 'Tangkap penuh', '8'),
                                  ('trend', '## 2. Lorong trend (pegang hingga 6 bulan)', 'Pelari besar', '15')):
        A += [tajuk, '',
              f'| Buku | Isyarat | Diambil | Dagangan setahun | Bulan tanpa belian | Pendedahan % | CAGR % | MDD % | **CAGR pada MDD −10 %** | '
              f'Jalur rawak: median (p5 – p95) | Tahun positif | Tahun terburuk % | K3: CAGR / MDD % | {tk} % diambil (rawak) | Menang % | '
              f'Rugi ≥ {rb} % % | Menambah? |', '|---' * 17 + '|']
        for b in T[T.lorong == lorong].itertuples():
            A.append(f"| `{b.buku}` | {b.isyarat:,.0f} | {b.diambil:,.0f} ({p(b.diambil / b.isyarat, 0)} %) | {b.diambil / n_tahun:.0f} | "
                     f"{p(1 - b.bulan_beli / n_bulan, 0)} % | {p(b.pendedahan, 0)} | {p(b.cagr, 1, True)} | {p(b.mdd, 1, True)} | "
                     f"**{p(b.cagr_had, 2, True)}** | {p(b.rawak_cagr_had, 2, True)} ({p(b.rawak5_cagr_had, 2, True)} – "
                     f"{p(b.rawak95_cagr_had, 2, True)}) | {b.tahun_positif:.0f} / {b.tahun:.0f} | {p(b.tahun_terburuk, 1, True)} | "
                     f"{p(b.cagr_K3, 1, True)} / {p(b.mdd_K3, 1, True)} | {p(b.tangkap)} ({p(b.rawak_tangkap)}) | {p(b.menang, 0)} | "
                     f"{p(b.rugi_besar, 0)} | **{'YA' if b.menambah else 'TIDAK'}** |")
        A.append('')
    Sw, Tr = T[(T.lorong == 'swing') & (T.buku != 'SWING8')], T[(T.lorong == 'trend') & ~T.buku.str.startswith('TREND11')]
    g_ = lambda n: T[T.buku == n].iloc[0]
    ys = SB[SB.besar_shariah.notna()]
    A += ['## 3. Bacaan', '',
          f"- Lorong swing: {int(Sw.menambah.sum())} daripada {len(Sw)} setup menambah di peringkat akaun; buku gabungan `SWING8` "
          f"{p(g_('SWING8').cagr_had, 2, True)} % setahun pada MDD −10 % (jalur rawak p95 {p(g_('SWING8').rawak95_cagr_had, 2, True)} %) → "
          f"**{'menambah' if g_('SWING8').menambah else 'TIDAK menambah'}**; MDD tanpa dikecilkan {p(g_('SWING8').mdd, 1, True)} %.",
          f"- Lorong trend: {int(Tr.menambah.sum())} daripada {len(Tr)} setup menambah; buku gabungan `TREND11` "
          f"{p(g_('TREND11').cagr_had, 2, True)} % setahun pada MDD −10 % (jalur rawak p95 {p(g_('TREND11').rawak95_cagr_had, 2, True)} %) → "
          f"**{'menambah' if g_('TREND11').menambah else 'TIDAK menambah'}**; MDD tanpa dikecilkan {p(g_('TREND11').mdd, 1, True)} %, "
          f"tahun terburuk {p(g_('TREND11').tahun_terburuk, 1, True)} %.",
          f"- `TREND11` dengan keluar \"tiada kemajuan selepas 40 sesi\": {p(g_('TREND11_TK40').cagr_had, 2, True)} % pada MDD −10 % "
          f"(MDD asal {p(g_('TREND11_TK40').mdd, 1, True)} %).",
          f'- Semua angka "pada MDD −10 %" mengandaikan akaun hanya sebahagian dilaburkan; baki tunai tidak mendapat faedah.', '',
          '## 4. Lorong trend pada saham Shariah (senarai semasa; maklumat)', '',
          '| ID | Belian | Belian Shariah | Pelari besar %: semua → Shariah (rawak) | Dijual ≥ +30 % % | Menang % | Rugi ≥ 15 % % | Purata % |',
          '|---' * 8 + '|']
    for r in SB.itertuples():
        A.append(f"| `{r.id}` | {r.n} | {r.n_shariah} | {p(r.besar)} → {p(r.besar_shariah)} ({p(r.a_besar_shariah)}) | "
                 f"{p(r.tb_shariah)} | {p(r.menang_shariah, 0)} | {p(r.rugi15_shariah, 0)} | {p(r.purata_shariah, 1, True)} |")
    A += ['', f"- Cukup belian Shariah (≥ 30): {len(ys)} daripada {len(SB)} setup; kadar pelari besar pada saham Shariah mengatasi rawak "
          f"bagi {int((ys.besar_shariah > ys.a_besar_shariah).sum())} daripadanya.", '',
          'Kaveat: tiada saham delist (bias lebih besar bagi pegang 6 bulan); kumpulan B sudah dilihat; K3 lorong trend pendek '
          '(isyarat selepas ~April 2026 tiada); senarai Shariah bukan titik-masa. Backtest sahaja.', '']
    open(os.path.join(d_, 'AKAUN.md'), 'w', encoding='utf-8').write('\n'.join(A))
    cari.log(f'akaun: {len(T)} buku; laporan ditulis')
    return T, SB


if __name__ == '__main__':
    main(sys.argv[1])
