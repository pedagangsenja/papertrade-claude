"""Carian setup — pusingan CS15 (SPEC pindaan 16 Nov 2026 (y)): keluarga pencetus K26 "lonjak lalu undur" (zon Fibonacci
sebagai parameter), dinilai dan didaftar dengan peraturan CS13 (pindaan (v)).

Skor A (label `terus`) -> sehingga 5 peraturan masuk berskor > 0 bagi setiap varian -> setup lengkap stop loss 4xATR14 + cara
pegang B -> "lulus" pada kumpulan B -> bacaan B1/B2 lawan kawalan rawak CS13 yang direkod -> kembar antara calon K26 ->
kod F baharu (selepas kod terakhir registry). Dilaporkan juga: sumbangan K26 di atas prasyarat, dan bacaan "Fibonacci istimewa".
Guna: python3 cs_cs15.py semua <kerja>      (perlukan panel A/B dan lapisan prasyarat; < 5 min)
Fail kerja berawalan cs15_. Jangan sunting keluaran secara manual."""
import json
import os
import pickle
import sys

import numpy as np
import pandas as pd

SINI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SINI)
import cs_atom as atom  # noqa: E402
import cs_cari as cari  # noqa: E402
import cs_cs05 as c5  # noqa: E402
import cs_daftar13 as c13  # noqa: E402
import cs_keluar7 as k7  # noqa: E402
import cs_lapis as lapis  # noqa: E402
import cs_param as kp  # noqa: E402
import cs_semak11 as s11  # noqa: E402
import cs_tala7 as t7  # noqa: E402
import cs_teras as teras  # noqa: E402

PUS = 'CS15'
ZON_IKLAN, ZON_JIRAN = (0.618, 0.786), ((0.5, 0.618), (0.786, 1.0))
D_HASIL = os.path.join(SINI, 'hasil', PUS)
F_ = lambda kerja, nama: os.path.join(kerja, f'cs15_{nama}.pkl')


def kawalan_cs13():
    """Kadar kawalan rawak CS13 yang direkod (ruang dan takrif sama; pindaan (y))."""
    b = json.load(open(os.path.join(SINI, 'hasil', 'CS13', 'bacaan.json')))
    return b['lulus_kawalan'], b['k3_kawalan'], b['kawalan_layak']


# ---------- skor dan calon (kumpulan A) ----------
def skor(kerja):
    f = F_(kerja, 'skor')
    if os.path.exists(f):
        return pickle.load(open(f, 'rb'))
    S = t7.skor_ev(kerja, t7.keluarga_k26(kerja, 'A')['ev'])
    pickle.dump(S, open(f, 'wb'), protocol=4)
    return S


def calon(S):
    """Sama seperti cs_daftar13.calon: sehingga N_ATAS peraturan berskor > 0 bagi setiap varian, tiada had bilangan."""
    R = []
    for nama, r in S.items():
        if not r.get('cukup') or not len(r['atas'][0]):
            continue
        idx, sk = r['atas']
        q1, q2, f1, f2 = c5.nyah(idx)
        for j in range(min(c13.N_ATAS, len(idx))):
            if np.isfinite(sk[j]) and sk[j] > 0:
                R.append(dict(pencetus=nama, induk='K26', ke=j + 1, skor=float(sk[j]), q1=int(q1[j]), q2=int(q2[j]),
                              f1=int(f1[j]), f2=int(f2[j]), skor0=r['skor0'], n_E1=r['n_ev'][0], n_E2=r['n_ev'][1]))
    T = pd.DataFrame(R).sort_values(['skor', 'pencetus', 'ke'], ascending=[False, True, True], kind='stable').reset_index(drop=True)
    T.insert(0, 'id', [f'K{i + 1:04d}' for i in range(len(T))])
    return T


# ---------- semakan (kumpulan B; belian A untuk kembar dan kekerapan Shariah) ----------
def kunci(kerja, T):
    """Struktur sama seperti cs_daftar13.kunci bagi calon K26 -> cs15_kunci.pkl."""
    import cs_lapor as lapor
    f = F_(kerja, 'kunci')
    if os.path.exists(f):
        return pickle.load(open(f, 'rb'))
    shar = set(open(os.path.join(lapor.BS2, 'data', 'harga', 'univ.txt')).read().split())
    out = {}
    for set_ in ('B', 'A'):
        pan = cari.panel(kerja, set_)
        L = lapis.muat(kerja, set_)
        Lr = (L['L1'], L['L2'])
        EV = t7.keluarga_k26(kerja, set_)['ev']
        Lab, As = s11.asas(pan)
        Bt = s11.siri_trend(pan) if set_ == 'B' else None
        sh = np.asarray([t in shar for t in pan['ticker']])
        for r in T.itertuples():
            ev = EV[r.pencetus]
            ev = ev[c5.topeng(pan, Lr, ev, r.q1, r.q2, r.f1, r.f2)]
            d, e = s11.ukur_tangkap(pan, Lab, As, ev, c13.S_HENTI)
            o = out.setdefault(r.id, {})
            es = e[sh[pan['tid'][e]]]
            o['e_' + set_], o['es_' + set_] = e.astype(np.int32), es.astype(np.int32)
            o['ms_' + set_] = (pan['tarikh'][es + 1] // 100).astype(np.int32)
            if set_ == 'B':
                o.update(d=d, L=c13.lengkap(pan, Bt, ev), nama=t7.nama7(r.pencetus, {}),
                         prasyarat=c13.teks_pra(r.q1, r.q2), penapis=c13.teks_pen(r.f1, r.f2))
    out['_n'] = {s: len(cari.panel(kerja, s)['c']) for s in ('A', 'B')}
    pickle.dump(out, open(f, 'wb'), protocol=4)
    return out


def jadual(T, K):
    rows = [c13._baris('calon', r.id, K[r.id], pencetus=r.pencetus, induk=r.induk, q1=r.q1, q2=r.q2, f1=r.f1, f2=r.f2,
                       skor_A=r.skor, prasyarat=c13.teks_pra(r.q1, r.q2), penapis=c13.teks_pen(r.f1, r.f2)) for r in T.itertuples()]
    J = pd.DataFrame(rows)
    kb = c13.kembar(J, K)                                    # tiada baris 'F': kembar antara calon K26 sahaja (pindaan (y))
    J['kembar_kepada'] = [kb.get(i, '') for i in J.id]
    J['takrif'] = [c13.takrif13(r.pencetus, int(r.q1), int(r.q2), int(r.f1), int(r.f2)) for r in J.itertuples()]
    J['untuk_daftar'] = J.lulus & (J.kembar_kepada == '')
    return J


def bacaan(J):
    lk, k3k, nk = kawalan_cs13()
    c = J[J.layak]
    o = dict(n_calon=len(J), calon_layak=len(c), n_lulus=int(c.lulus.sum()), lulus_calon=float(c.lulus.mean()) if len(c) else np.nan,
             lulus_kawalan=lk, k3_calon=float((c.kl_terus_K3 > 0).mean()) if len(c) else np.nan, k3_kawalan=k3k, kawalan_layak=nk)
    o['b1'] = bool(o['lulus_calon'] >= lk + c13.B1_BEZA)
    o['b2'] = bool(o['k3_calon'] >= c13.B2_MIN and o['k3_calon'] >= k3k + c13.B2_BEZA)
    o['ya'] = bool(o['b1'] and o['b2'])
    o['nasib'] = float(lk / o['lulus_calon']) if o['lulus_calon'] else np.nan
    return o


def daftar(J, B):
    """Kod F baharu bagi setiap calon lulus yang bukan kembar, HANYA jika bacaan lulus (seperti cs_daftar13.daftar)."""
    import cs_lapor as lapor
    reg = pd.read_csv(lapor.REG_F, dtype=str).fillna('').reindex(columns=lapor.LAJUR_F, fill_value='')
    peta = dict(zip(reg.takrif, reg.id))
    if not B['ya']:
        return {}
    seterusnya, baharu, idf = max(int(x[1:]) for x in reg.id) + 1, [], {}
    G = {n: p for n, _, p in kp.grid_k26()}
    for r in J[J.untuk_daftar].sort_values('skor_A', ascending=False, kind='stable').itertuples():
        if r.takrif in peta:
            idf[r.id] = peta[r.takrif]
            continue
        q1, q2, f1, f2 = int(r.q1), int(r.q2), int(r.f1), int(r.f2)
        b = dict.fromkeys(lapor.LAJUR_F, '')
        b.update(id=f'F{seterusnya:02d}', keluarga='F', pusingan=PUS, tarikh_daftar='2026-11-16', takrif=r.takrif,
                 param=json.dumps(G[r.pencetus], sort_keys=True), masuk=t7.nama7(r.pencetus, {}), penapis=c5.tk_pen(f1, f2),
                 henti=f'{c13.KOD_HENTI} {k7.HENTI[c13.S_HENTI]}', keluar=c13.TEKS_PEGANG, skor_tepat=f'{r.skor_A:.5f}',
                 status='BACKTEST', prasyarat=c5.buang_kod(c5.tk_pra(q1, q2)).replace(' DAN ', ' + '),
                 syarat=c5.buang_kod(c5.tk_pen(f1, f2)).replace(' DAN ', ' + '))
        jum = bil = 0.0
        for j, t in enumerate(('K1', 'K2', 'K3'), 1):
            n = int(getattr(r, f'n_B_K{j}'))
            b[f'n_{t}'] = str(n)
            if n:
                m = float(getattr(r, f'menang_B_K{j}'))
                b.update({f'purata_{t}': f"{getattr(r, f'purata_B_K{j}'):.5f}", f'k10_{t}': f"{getattr(r, f'k10_B_K{j}'):.4f}",
                          f'menang_{t}': f'{m:.4f}'})
                jum, bil = jum + n * float(f'{m:.4f}'), bil + n
        b['menang'] = f'{jum / bil:.4f}' if bil else ''
        baharu.append(b)
        peta[r.takrif] = idf[r.id] = b['id']
        seterusnya += 1
    if baharu:
        reg = pd.concat([reg, pd.DataFrame(baharu)[lapor.LAJUR_F].astype(str)], ignore_index=True)
        reg['_n'] = reg.id.str[1:].astype(int)
        reg.sort_values('_n').drop(columns='_n').to_csv(lapor.REG_F, index=False)
    return idf


# ---------- semakan tambahan (dilaporkan, bukan syarat) ----------
def sumbangan(kerja, J):
    """Kadar `terus` belian setup (satu posisi, pegang 20 sesi) lawan saham LAIN yang lulus prasyarat + penapis yang sama pada
    hari sama dan tercile ATR % sama (kumpulan B). Beza = sumbangan corak K26 di atas prasyaratnya."""
    pan = cari.panel(kerja, 'B')
    L = lapis.muat(kerja, 'B')
    Lr, V = (L['L1'], L['L2']), t7.label_terus(pan)
    EV = t7.keluarga_k26(kerja, 'B')['ev']
    sah = np.flatnonzero(pan['sah'])
    pct = pd.Series(pan['atr'][sah] / pan['c'][sah]).groupby(pan['hari'][sah]).rank(pct=True).to_numpy()
    G = np.full(len(pan['c']), -1)
    G[sah] = pan['hari'][sah] * 3 + np.minimum((pct * 3).astype(int), 2)
    cache, out = {}, {}
    for r in J.itertuples():
        q = (int(r.q1), int(r.q2), int(r.f1), int(r.f2))
        if q not in cache:
            p = sah[c5.topeng(pan, Lr, sah, *q)]
            cache[q] = pd.Series(V[p, 0]).groupby(G[p]).agg(['sum', 'size'])
        ev = EV[r.pencetus]
        e = ev[c5.topeng(pan, Lr, ev, *q)]
        e = e[teras.satu_posisi(e, np.full(len(e), atom.TMAX - 1), pan['tid'])]
        s = cache[q].reindex(G[e])
        n_ = s['size'].to_numpy() - 1
        ok = n_ > 0
        x = V[e[ok], 0] - (s['sum'].to_numpy()[ok] - V[e[ok], 0]) / n_[ok]
        out[r.id] = (float(x.mean()) if ok.any() else np.nan, float(2 * x.std() / np.sqrt(max(ok.sum(), 1))) if ok.any() else np.nan)
    return out


def fib(kerja, set_):
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
    B = pd.DataFrame([dict(n=n, k=k, iklan=g.set_index('zon').lebih.get(z(ZON_IKLAN)),
                           jiran=np.nanmean([g.set_index('zon').lebih.get(z(x)) for x in ZON_JIRAN])) for (n, k), g in D.groupby(['n', 'k'])])
    m, pz = int((B.iklan > B.jiran).sum()), int((B.iklan > 0).sum())
    return B, m, pz, bool(m > 10 and pz > 10)


# ---------- laporan ----------
def lapor_(J, B, idf, SB, DA, DB):
    os.makedirs(D_HASIL, exist_ok=True)
    p = lambda x, t=True: '–' if x is None or x != x else (f'{x * 100:+.1f}' if t else f'{x * 100:.1f}')
    J = J.copy()
    J['id_F'] = J.id.map(idf).fillna('')
    J['sumbangan'] = J.id.map(lambda i: SB[i][0])
    J['sumbangan_2se'] = J.id.map(lambda i: SB[i][1])
    J.drop(columns=[c for c in J.columns if c.startswith('_')]).to_csv(os.path.join(D_HASIL, 'calon.csv'), index=False)
    _, mA, pA, _ = bacaan_fib(DA)
    BB, mB, pB, istimewa = bacaan_fib(DB)
    DB.to_csv(os.path.join(D_HASIL, 'zon.csv'), index=False)
    json.dump({k: (v if not isinstance(v, float) or v == v else None) for k, v in dict(B, fib_ya=istimewa, fib_menang=mB, fib_positif=pB,
              n_daftar=len(idf)).items()}, open(os.path.join(D_HASIL, 'bacaan.json'), 'w'), indent=1, sort_keys=True)
    try:
        sys.path.insert(0, os.path.join(cari.AKAR, 'BacktestShariah2', 'standard'))
        import status_kad
        status = status_kad.baris()
    except Exception:
        status = '> **Status keputusan:** lihat `laporan/KAD_SKOR.md`; laporan ini BUKAN keputusan.'
    F = J[J.id_F != ''].sort_values('terus', ascending=False, kind='stable')
    kode = sorted(F.id_F, key=lambda x: int(x[1:]))
    Lu = J[J.lulus & (J.kembar_kepada == '')].sort_values('terus', ascending=False, kind='stable')
    X = F if len(F) else Lu                                   # tiada kod: calon lulus bukan kembar dipaparkan sebagai rekod
    jelas = int((X.sumbangan > X.sumbangan_2se).sum())
    A = ['# CS15 — keluarga K26 "lonjak lalu undur" (zon Fibonacci): setup F baharu (backtest, BUKAN bukti)', '', status, '',
         'Dijana `kajian/carian_setup/cs_cs15.py`; peraturan `kajian/SPEC_CARIAN_SETUP.md` pindaan 16 Nov 2026 (y) = peraturan '
         'pendaftaran CS13 (pindaan (v)). Idea daripada tangkapan skrin pengguna (POST-HOC). Jangan sunting secara manual.', '',
         '## Ringkasan', '',
         f"- Calon (sehingga 5 setiap varian, skor A > 0): **{B['n_calon']}**; cukup belian untuk dinilai: {B['calon_layak']}; "
         f"lulus pada saham yang carian tidak lihat: **{B['n_lulus']}**.",
         f"- B1 kadar lulus: calon **{p(B['lulus_calon'], False)} %** lawan kawalan rawak CS13 {p(B['lulus_kawalan'], False)} % "
         f"→ {'lulus' if B['b1'] else 'GAGAL'}. B2 lebih baik daripada rawak pada 2025–26: calon **{p(B['k3_calon'], False)} %** "
         f"lawan kawalan {p(B['k3_kawalan'], False)} % → {'lulus' if B['b2'] else 'GAGAL'}. Anggaran bahagian lulus kerana nasib: "
         f"~{p(B['nasib'], False)} %.",
         f"- Kembar (beli saham sama pada hari sama, pertindihan ≥ 80 %, antara calon K26): {int((J.lulus & (J.kembar_kepada != '')).sum())}.",
         f"- **Kod F baharu: {len(kode)}** ({kode[0]}–{kode[-1]})." if kode else
         f"- **Tiada kod F baharu**: syarat pendaftaran (B1 DAN B2) {'lulus' if B['ya'] else 'TIDAK lulus'}. "
         f"{len(Lu)} calon lulus yang bukan kembar disenaraikan di bawah sebagai REKOD sahaja (tanpa kod).",
         f"- **Sumbangan corak K26 di atas prasyarat** (lawan saham lain yang lulus prasyarat dan penapis yang sama, hari dan "
         f"turun-naik sama): jelas positif (melebihi 2 ralat piawai) bagi **{jelas}** daripada {len(X)} "
         f"{'kod' if len(F) else 'calon lulus'}; median {p(X.sumbangan.median())} mata.",
         f"- **Fibonacci istimewa? {'YA' if istimewa else 'TIDAK'}** — zon iklan 61.8–78.6 % mengatasi purata zon jiran dalam "
         f"{mB} daripada 20 pasangan (tempoh, saiz kaki) dan positif dalam {pB} (saham yang carian tidak lihat; kumpulan carian: "
         f"{mA} dan {pA}).", '',
         ('## Setup F baharu' if len(F) else '## Calon lulus — REKOD sahaja, tiada kod F') +
         ' (saham yang carian tidak lihat; stop loss 4 × ATR14 + cara pegang B; satu posisi setiap saham)', '',
         'Disusun ikut kadar tangkap (naik ≥ 5 % minggu pertama DAN naik lagi hingga minggu ke-4), seperti senarai utama.', '',
         '| Kod / calon | Pencetus | Prasyarat | Penapis saham | Tangkap % (rawak) | Naik ≥ 5 % minggu 1 % | Longgar `naik` % (rawak) | '
         'Menang % | Purata % | Rugi ≥ 15 % | Hari pegang | Belian setahun (Shariah) | Lebih rawak 2025–26 | Sumbangan K26 |',
         '|---|---|---|---|---|---|---|---|---|---|---|---|---|---|']
    for r in X.itertuples():
        A.append(f"| {('`' + r.id_F + '`') if r.id_F else r.id} | {r.nama} | {r.prasyarat or '–'} | {r.penapis or '–'} | {p(r.terus, False)} ({p(r.a_terus, False)}) | "
                 f"{p(r.m5, False)} | {p(r.naik, False)} ({p(r.a_naik, False)}) | {p(r.menang_B, False)} | {p(r.purata_B)} | "
                 f"{p(r.rugi15_B, False)} | {r.hari_B:.0f} | {r.setahun:.0f} ({r.shariah_setahun:.0f}) | {p(r.kl_terus_K3)} | "
                 f"{p(r.sumbangan)} (±{r.sumbangan_2se * 100:.1f}) |")
    A += ['', '## Fibonacci: zon undur, pencetus sahaja (saham yang carian tidak lihat; satu posisi, pegang 20 sesi)', '',
          '| Zon undur | Belian | Lebih rawak (purata, mata) |', '|---|---|---|']
    for zon, g in DB.groupby('zon', sort=False):
        A.append(f"| {zon} | {int(g.bil.sum()):,} | {p(np.nanmean(g.lebih))} |")
    A += ['', 'Kaveat (dikunci (y)): idea post-hoc dan hasil ukuran lain sudah dilihat; saham "tidak dilihat" sudah dipakai '
          'pusingan terdahulu dan bertindih dengan set 431; tiada saham delist; kembar hanya disemak antara calon K26; kod ini '
          'belum dimasukkan ke `hasil/CS13/SENARAI_UTAMA.md` dan dashboard (perlu binaan penuh); BUKAN calon papertrade tanpa '
          'keputusan pengguna.', '']
    open(os.path.join(D_HASIL, 'LAPORAN.md'), 'w', encoding='utf-8').write('\n'.join(x for x in A if x is not None))


def semua(kerja):
    for s in ('A', 'B'):
        t7.keluarga_k26(kerja, s)
    T = calon(skor(kerja))
    cari.log(f'CS15: {len(T)} calon berskor > 0 daripada {T.pencetus.nunique()} varian K26')
    K = kunci(kerja, T)
    J = jadual(T, K)
    B = bacaan(J)
    idf = daftar(J, B)
    SB = sumbangan(kerja, J)
    lapor_(J, B, idf, SB, fib(kerja, 'A'), fib(kerja, 'B'))
    cari.log(f"CS15 siap: lulus {B['n_lulus']}/{B['calon_layak']}, B1 {B['b1']}, B2 {B['b2']}; kod F baharu {len(idf)}")


if __name__ == '__main__':
    if sys.argv[1] == 'semua':
        semua(sys.argv[2])
    else:
        raise SystemExit(f'arahan tidak dikenali: {sys.argv[1]}')
