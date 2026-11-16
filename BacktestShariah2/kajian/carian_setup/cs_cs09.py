"""Carian setup — pusingan CS09: keluarga K26 "lonjak lalu undur" (zon Fibonacci sebagai parameter), SPEC pindaan 16 Nov 2026 (r).

Masuk: grid K26 (100 varian) × enjin (i) prasyarat × penapis pada kumpulan A, sasaran `terus` (sama seperti CS07 (a)).
Henti/keluar dikunci sebelum hasil dilihat: X00 + G7 5×ATR14, pegang minimum (p), satu posisi setiap saham.
Kumpulan B: takrif "dipercayai" (m); yang lulus didaftar sebagai F (pusingan CS09). Bacaan "Fibonacci istimewa?" dikunci (r).
Guna: python3 cs_cs09.py semua <kerja>     (isyarat A/B -> skor A -> papan -> kunci B -> daftar -> lapor)
Fail kerja berawalan cs09_. Jangan sunting keluaran secara manual."""
import json
import os
import pickle
import sys

import numpy as np
import pandas as pd

SINI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SINI)
import cs_akhir as ak  # noqa: E402
import cs_cari as cari  # noqa: E402
import cs_cs05 as c5  # noqa: E402
import cs_cs07 as c7  # noqa: E402
import cs_keluar7 as k7  # noqa: E402
import cs_lapis as lapis  # noqa: E402
import cs_lapor as lapor  # noqa: E402
import cs_param as kp  # noqa: E402
import cs_tala7 as t7  # noqa: E402
import cs_teras as teras  # noqa: E402

PUS = 'CS09'
N_PAPAN, MAKS_ZON, MAKS_PRA = 6, 2, 3                # dikunci pindaan (r)
HENTI_S, KOL = 6, 0                                  # G7 5xATR14, X00
ZON_IKLAN, ZON_JIRAN = (0.618, 0.786), ((0.5, 0.618), (0.786, 1.0))
D_HASIL = os.path.join(SINI, 'hasil', PUS)
TEMPOH = ('K1', 'K2', 'K3')


def _zon(p):
    return (p['za'], p['zb'])


def skor(kerja):
    f = os.path.join(kerja, 'cs09_skor.pkl')
    if os.path.exists(f):
        return pickle.load(open(f, 'rb'))
    ev = t7.keluarga_k26(kerja, 'A')['ev']
    S = t7.skor_ev(kerja, ev)
    pickle.dump(S, open(f, 'wb'), protocol=4)
    return S


def jadual(S):
    G = {n: p for n, _, p in kp.grid_k26()}
    R = []
    for nama, r in S.items():
        if not r.get('cukup') or not len(r['atas'][0]) or not np.isfinite(r['atas'][1][0]):
            continue
        q1, q2, f1, f2 = (int(x[0]) for x in c5.nyah(r['atas'][0][:1]))
        R.append(dict(nama=nama, skor=float(r['atas'][1][0]), q1=q1, q2=q2, f1=f1, f2=f2, skor0=r['skor0'],
                      n_E1=r['n_ev'][0], n_E2=r['n_ev'][1], **G[nama]))
    return pd.DataFrame(R).sort_values(['skor', 'nama'], ascending=[False, True], kind='stable').reset_index(drop=True)


def pilih(T):
    papan, bz, bp = [], {}, {}
    for r in T.itertuples():
        z, q = (r.za, r.zb), (r.q1, r.q2)
        if r.skor <= 0 or bz.get(z, 0) >= MAKS_ZON or bp.get(q, 0) >= MAKS_PRA:
            continue
        bz[z], bp[q] = bz.get(z, 0) + 1, bp.get(q, 0) + 1
        papan.append(dict(id=f'C{len(papan) + 1:02d}', pencetus=r.nama, q1=r.q1, q2=r.q2, f1=r.f1, f2=r.f2, skor=r.skor))
        if len(papan) == N_PAPAN:
            break
    return papan


def _xa_kosong(pan):
    """X00 tidak memakai atom keluar: matriks atom kosong (bentuk sama seperti cs_keluar7.siri_set)."""
    return np.zeros((int((k7.JENIS == 0).sum()), len(pan['c'])), np.uint8)


def ukur_b(kerja, papan):
    """Setiap setup papan pada kumpulan B dengan X00 + G7: dipercayai (m) dan statistik satu posisi setiap tempoh."""
    pan = cari.panel(kerja, 'B')
    L = lapis.muat(kerja, 'B')
    Lr, V, XA = (L['L1'], L['L2']), t7.label_terus(pan), _xa_kosong(pan)
    out = {}
    for b in papan:
        ev = t7.ev_satu(kerja, 'B', b['pencetus'])
        e0 = ev[c5.topeng(pan, Lr, ev, b['q1'], b['q2'], b['f1'], b['f2'])]
        if not len(e0):
            out[b['id']] = dict(belian=0, tahun=0, kl=[np.nan] * 3, ya=False, stat={})
            continue
        St = k7.sedia_pan(pan, XA, e0)
        R, sk = k7.hasil(*St[:7], k7.A1, k7.A2, k7.OP, HENTI_S, KOL)
        amb = teras.satu_posisi(e0, sk, pan['tid'])
        e, r = e0[amb], R[amb]
        tp = pan['tempoh'][e]
        lebih = V[e, 0] - V[e, 1]
        kl = [float(lebih[tp == j].mean()) if (tp == j).any() else float('nan') for j in range(3)]
        tahun = int(len(np.unique(pan['tarikh'][e] // 10000)))
        stat = {}
        for j, t in list(enumerate(TEMPOH)) + [(-1, 'semua')]:
            m = (tp == j) if j >= 0 else np.ones(len(e), bool)
            if m.any():
                stat[t] = dict(n=int(m.sum()), terus=float(V[e[m], 0].mean()), asas=float(V[e[m], 1].mean()),
                               menang=float((r[m] > 0).mean()), purata=float(r[m].mean()), jadi=float((r[m] >= 0.10).mean()),
                               rugi8=float((r[m] <= -0.08).mean()))
        out[b['id']] = dict(belian=len(e), tahun=tahun, kl=kl, stat=stat, setahun=len(e) / max(tahun, 1),
                            ya=bool(len(e) >= ak.MIN_BELIAN and tahun >= ak.MIN_TAHUN and all(x > 0 for x in kl)))
    return out


def sumbangan(kerja, papan):
    """Semakan tambahan SELEPAS hasil dilihat (tidak mengubah pendaftaran): kadar `terus` belian setup (satu posisi, pegang
    20 sesi) lawan saham LAIN yang lulus prasyarat + penapis yang sama pada hari sama dan tercile ATR % sama. Beza = sumbangan
    pencetus K26 di atas prasyaratnya. Juga: prasyarat + penapis pada saham mana-mana, dan pencetus sahaja (lawan rawak)."""
    import cs_atom as atom
    pan = cari.panel(kerja, 'B')
    L = lapis.muat(kerja, 'B')
    Lr, V = (L['L1'], L['L2']), t7.label_terus(pan)
    sah = np.flatnonzero(pan['sah'])
    pct = pd.Series(pan['atr'][sah] / pan['c'][sah]).groupby(pan['hari'][sah]).rank(pct=True).to_numpy()
    G = np.full(len(pan['c']), -1)
    G[sah] = pan['hari'][sah] * 3 + np.minimum((pct * 3).astype(int), 2)
    out = {}
    for b in papan:
        ev = t7.ev_satu(kerja, 'B', b['pencetus'])
        e = ev[c5.topeng(pan, Lr, ev, b['q1'], b['q2'], b['f1'], b['f2'])]
        e = e[teras.satu_posisi(e, np.full(len(e), atom.TMAX - 1), pan['tid'])]
        p = sah[c5.topeng(pan, Lr, sah, b['q1'], b['q2'], b['f1'], b['f2'])]
        s = pd.Series(V[p, 0]).groupby(G[p]).agg(['sum', 'size']).reindex(G[e])
        n_ = s['size'].to_numpy() - 1
        ok = n_ > 0
        x = V[e[ok], 0] - (s['sum'].to_numpy()[ok] - V[e[ok], 0]) / n_[ok]
        tp = pan['tempoh'][e[ok]]
        kp_ = t7.kadar7(pan, V, p)[-1]
        k0 = t7.kadar7(pan, V, ev)[-1]
        out[b['id']] = dict(n=int(ok.sum()), sum=float(x.mean()) if ok.any() else np.nan,
                            se2=float(2 * x.std() / np.sqrt(max(ok.sum(), 1))),
                            kl=[float(x[tp == j].mean()) if (tp == j).any() else np.nan for j in range(3)],
                            pra=(kp_[1], kp_[2]), pencetus=(k0[1], k0[2]))
    return out


def fib(kerja, set_):
    """Bacaan (r): kelebihan `terus` pencetus sahaja (satu posisi, pegang 20 sesi) setiap varian K26 pada set."""
    pan = cari.panel(kerja, set_)
    V = t7.label_terus(pan)
    ev = t7.keluarga_k26(kerja, set_)['ev']
    R = []
    for nama, _, p in kp.grid_k26():
        k = t7.kadar7(pan, V, ev[nama])[-1]
        R.append(dict(nama=nama, n=p['n'], k=p['k'], zon=f"{p['za']:.3f}-{p['zb']:.3f}", bil=k[0], terus=k[1], asas=k[2],
                      lebih=k[1] - k[2] if k[0] else np.nan))
    return pd.DataFrame(R)


def bacaan_fib(D):
    z = lambda a: f'{a[0]:.3f}-{a[1]:.3f}'
    baris = []
    for (n, k), g in D.groupby(['n', 'k']):
        g = g.set_index('zon').lebih
        baris.append(dict(n=n, k=k, iklan=g.get(z(ZON_IKLAN)), jiran=np.nanmean([g.get(z(x)) for x in ZON_JIRAN])))
    B = pd.DataFrame(baris)
    menang = int((B.iklan > B.jiran).sum())
    positif = int((B.iklan > 0).sum())
    return B, menang, positif, bool(menang > 10 and positif > 10)


def daftar(papan, U, T):
    reg = pd.read_csv(lapor.REG_F, dtype=str).fillna('').reindex(columns=lapor.LAJUR_F, fill_value='')
    G = {n: p for n, _, p in kp.grid_k26()}
    idf = {}
    for b in papan:
        u = U[b['id']]
        if not u['ya']:
            continue
        tk = c7.takrif7(b['pencetus'], b['q1'], b['q2'], b['f1'], b['f2'], HENTI_S, KOL)
        lama = reg[reg.takrif == tk]
        if len(lama):
            idf[b['id']] = lama.id.iloc[0]
            continue
        fid = f"F{max(int(x[1:]) for x in reg.id) + 1:02d}"
        baru = dict.fromkeys(lapor.LAJUR_F, '')
        baru.update(id=fid, keluarga='F', pusingan=PUS, tarikh_daftar=pd.Timestamp.now().strftime('%Y-%m-%d'), takrif=tk,
                    param=json.dumps(G[b['pencetus']], sort_keys=True), masuk=t7.nama7(b['pencetus'], {}),
                    penapis=c5.tk_pen(b['f1'], b['f2']), henti=f'G7 {k7.HENTI[HENTI_S]}', keluar=k7.nama_peraturan(KOL),
                    skor_tepat=f"{b['skor']:.5f}", status='BACKTEST',
                    prasyarat=c5.buang_kod(c5.tk_pra(b['q1'], b['q2'])).replace(' DAN ', ' + '),
                    syarat=c5.buang_kod(c5.tk_pen(b['f1'], b['f2'])).replace(' DAN ', ' + '))
        for t in TEMPOH:
            v = u['stat'].get(t)
            baru[f'n_{t}'] = str(v['n'] if v else 0)
            if v:
                baru.update({f'purata_{t}': f"{v['purata']:.5f}", f'k10_{t}': f"{v['jadi']:.4f}",
                             f'menang_{t}': f"{v['menang']:.4f}"})
        baru['menang'] = f"{u['stat']['semua']['menang']:.4f}"
        reg = pd.concat([reg, pd.DataFrame([baru])[lapor.LAJUR_F].astype(str)], ignore_index=True)
        idf[b['id']] = fid
    reg['_n'] = reg.id.str[1:].astype(int)
    reg.sort_values('_n').drop(columns='_n').to_csv(lapor.REG_F, index=False)
    return idf


def lapor_(T, papan, U, idf, DA, DB, SB):
    os.makedirs(D_HASIL, exist_ok=True)
    p = lambda x, t=True: '–' if x is None or x != x else (f'{x * 100:+.1f}' if t else f'{x * 100:.1f}')
    G = {n: f for n, f, _ in kp.grid_k26()}
    gp = {n: q for n, _, q in kp.grid_k26()}
    rows = []
    for b in papan:
        u = U[b['id']]
        s = u['stat'].get('semua', {})
        rows.append(dict(id=b['id'], F=idf.get(b['id'], ''), pencetus=b['pencetus'], teks=kp.teks(G[b['pencetus']], gp[b['pencetus']]),
                         prasyarat=c5.buang_kod(c5.tk_pra(b['q1'], b['q2'])), penapis=c5.buang_kod(c5.tk_pen(b['f1'], b['f2'])),
                         skor_A=b['skor'], belian_B=u['belian'], tahun=u['tahun'], setahun=u.get('setahun', 0),
                         kl_K1=u['kl'][0], kl_K2=u['kl'][1], kl_K3=u['kl'][2], dipercayai=u['ya'], **{
                             k: s.get(k, np.nan) for k in ('terus', 'asas', 'menang', 'purata', 'jadi', 'rugi8')}))
    P = pd.DataFrame(rows)
    P.to_csv(os.path.join(D_HASIL, 'papan.csv'), index=False)
    BA, mA, pA, _ = bacaan_fib(DA)
    BB, mB, pB, istimewa = bacaan_fib(DB)
    try:
        sys.path.insert(0, os.path.join(cari.AKAR, 'BacktestShariah2', 'standard'))
        import status_kad
        status = status_kad.baris()
    except Exception:
        status = '> **Status keputusan:** lihat `laporan/KAD_SKOR.md`; laporan ini BUKAN keputusan.'
    lulus = int(P.dipercayai.sum()) if len(P) else 0
    A = ['# CS09 — keluarga K26 "lonjak lalu undur" (zon Fibonacci sebagai parameter): backtest, BUKAN bukti', '', status, '',
         'Dijana `kajian/carian_setup/cs_cs09.py`; peraturan dikunci `kajian/SPEC_CARIAN_SETUP.md` pindaan 16 Nov 2026 (r) '
         '(POST-HOC: idea daripada tangkapan skrin pengguna dan penerokaan pada set 431). Jangan sunting secara manual.', '',
         '## Ringkasan', '',
         f'- Grid 100 varian; skor A > 0: **{int((T.skor > 0).sum())}** daripada {len(T)} varian yang cukup isyarat.',
         f'- Papan {len(P)} setup (henti/keluar dikunci: pegang 20 sesi `X00` + henti 5×ATR14); **dipercayai pada kumpulan B: '
         f'{lulus}** → kod F: {", ".join(f"`{x}`" for x in idf.values()) or "tiada"}.',
         f'- **Fibonacci istimewa? {"YA" if istimewa else "TIDAK"}** (kumpulan B): zon iklan 61.8–78.6 % mengatasi purata zon jiran '
         f'(50–61.8 %, 78.6–100 %) dalam **{mB}** daripada 20 pasangan (tempoh, saiz kaki); kelebihan zon iklan sendiri positif '
         f'dalam {pB} daripada 20. Kumpulan A (maklumat): {mA} dan {pA}.', '',
         '## Papan (kumpulan B, satu posisi setiap saham)', '',
         '| # | F | Pencetus | Prasyarat | Penapis saham | Skor A | Belian B (setahun) | Naik lagi % (rawak) | Kelebihan K1 / K2 / K3 '
         '| Menang % | Purata % | Dijual ≥ +10 % | Rugi ≥ 8 % | Dipercayai |', '|---|---|---|---|---|---|---|---|---|---|---|---|---|---|']
    for r in P.itertuples():
        A.append(f"| {r.id} | {('`' + r.F + '`') if r.F else '–'} | `{r.pencetus}` {r.teks} | {r.prasyarat or '–'} | {r.penapis or '–'} | "
                 f"{p(r.skor_A)} | {r.belian_B:,} ({r.setahun:.0f}) | {p(r.terus, False)} ({p(r.asas, False)}) | "
                 f"{p(r.kl_K1)} / {p(r.kl_K2)} / {p(r.kl_K3)} | {p(r.menang, False)} | {p(r.purata)} | {p(r.jadi, False)} | "
                 f"{p(r.rugi8, False)} | {'**ya**' if r.dipercayai else 'tidak'} |")
    A += ['', '## Sumbangan corak K26 di atas prasyarat (semakan tambahan SELEPAS hasil dilihat; tidak mengubah pendaftaran)', '',
          'Soalan: adakah corak "lonjak lalu undur" memilih saham yang lebih baik daripada saham LAIN yang lulus prasyarat dan '
          'penapis yang sama, pada hari sama dan tercile ATR % sama? Satu posisi, pegang 20 sesi; kumpulan B.', '',
          '| # | F | Naik lagi % setup | Sumbangan K26 (2 ralat piawai) | K1 / K2 / K3 | Prasyarat + penapis, saham mana-mana: naik lagi % (rawak) | Pencetus K26 sahaja: naik lagi % (rawak) |',
          '|---|---|---|---|---|---|---|']
    for b in papan:
        x, u = SB[b['id']], U[b['id']]['stat'].get('semua', {})
        A.append(f"| {b['id']} | {('`' + idf[b['id']] + '`') if b['id'] in idf else '–'} | {p(u.get('terus'), False)} | "
                 f"{p(x['sum'])} (±{x['se2'] * 100:.1f}) | {p(x['kl'][0])} / {p(x['kl'][1])} / {p(x['kl'][2])} | "
                 f"{p(x['pra'][0], False)} ({p(x['pra'][1], False)}) | {p(x['pencetus'][0], False)} ({p(x['pencetus'][1], False)}) |")
    jelas = sum(1 for b in papan if SB[b['id']]['sum'] > SB[b['id']]['se2'])
    A += ['', f'Sumbangan K26 jelas positif (melebihi 2 ralat piawai) bagi **{jelas}** daripada {len(papan)} setup papan: kelebihan '
          'setup datang terutamanya daripada prasyaratnya (earnings dalam 1–5 sesi akan datang, seperti CS05/CS06) dan '
          'pemilihan saham turun-naik tinggi, bukan daripada corak "lonjak lalu undur".']
    A += ['', '## Fibonacci: zon undur, pencetus sahaja (kumpulan B; satu posisi, pegang 20 sesi)', '',
          'Kelebihan = kadar "naik lagi" (`terus`) tolak saham rawak hari sama × tercile ATR %, mata peratus; purata semua '
          '(tempoh, saiz kaki). Zon iklan = 61.8–78.6 %.', '', '| Zon undur | Belian B (jumlah) | Kelebihan B purata | Kelebihan A purata |',
          '|---|---|---|---|']
    for zon, g in DB.groupby('zon', sort=False):
        ga = DA[DA.zon == zon]
        A.append(f"| {zon} | {int(g.bil.sum()):,} | {p(np.nanmean(g.lebih))} | {p(np.nanmean(ga.lebih))} |")
    A += ['', '| Tempoh | Kaki | Zon iklan B | Purata zon jiran B | Iklan lebih baik? |', '|---|---|---|---|---|']
    for r in BB.itertuples():
        A.append(f"| {r.n} | {r.k:.0%} | {p(r.iklan)} | {p(r.jiran)} | {'ya' if r.iklan > r.jiran else 'tidak'} |")
    A += ['', '## 10 varian teratas ikut skor A (maklumat)', '', '| Varian | Pencetus | Prasyarat | Penapis | Skor A | n E1 / E2 |',
          '|---|---|---|---|---|---|']
    for r in T.head(10).itertuples():
        A.append(f"| `{r.nama}` | {kp.teks('K26', gp[r.nama])} | {c5.buang_kod(c5.tk_pra(r.q1, r.q2)) or '–'} | "
                 f"{c5.buang_kod(c5.tk_pen(r.f1, r.f2)) or '–'} | {p(r.skor)} | {r.n_E1:,} / {r.n_E2:,} |")
    A += ['', 'Kaveat (dikunci (r)): idea post-hoc; kumpulan B sudah dilihat untuk label lain dan bertindih dengan set 431; tiada '
          'saham delist; setup di sini BUKAN calon papertrade tanpa keputusan pengguna berasingan; kedudukan akhir penuh '
          '(`hasil/KEDUDUKAN_AKHIR.md`) belum dijana semula dengan setup CS09.', '']
    open(os.path.join(D_HASIL, 'LAPORAN.md'), 'w', encoding='utf-8').write('\n'.join(A))
    DB.assign(set_='B').to_csv(os.path.join(D_HASIL, 'zon.csv'), index=False)


def semua(kerja):
    for s in ('A', 'B'):
        t7.keluarga_k26(kerja, s)
    S = skor(kerja)
    T = jadual(S)
    papan = pilih(T)
    cari.log(f'CS09: {len(T)} varian berskor, skor A > 0: {int((T.skor > 0).sum())}; papan {len(papan)}')
    U = ukur_b(kerja, papan)
    pickle.dump(dict(T=T, papan=papan, U=U), open(os.path.join(kerja, 'cs09_hasil.pkl'), 'wb'), protocol=4)
    DA, DB = fib(kerja, 'A'), fib(kerja, 'B')
    idf = daftar(papan, U, T)
    SB = sumbangan(kerja, papan)
    lapor_(T, papan, U, idf, DA, DB, SB)
    cari.log(f'CS09 siap: dipercayai {sum(u["ya"] for u in U.values())} daripada {len(papan)}; F baharu {idf}')


if __name__ == '__main__':
    if sys.argv[1] == 'semua':
        semua(sys.argv[2])
    else:
        raise SystemExit(f'arahan tidak dikenali: {sys.argv[1]}')
