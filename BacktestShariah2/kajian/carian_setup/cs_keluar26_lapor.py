"""CS26: bacaan dan laporan (pindaan 20 Nov 2026 (am)). Dipanggil oleh `cs_keluar26.py lapor <kerja>`; menulis `hasil/CS26/`."""
import json
import os

import numpy as np
import pandas as pd

import cs_cari as cari
import cs_keluar25 as c25
import cs_keluar26 as c26

IX, F_ = c26.IX, c26.F_
UKUR = ('nisbah', 'purata', 'menang', 'rugi15', 'k50', 'sesi', 'untung_purata', 'rugi_purata')


def muat(kerja):
    meta = json.load(open(F_(kerja, 'cara.json')))
    return dict(meta=meta, cara=[c26.dari_kod(k) for k in meta['cara']], A=np.load(F_(kerja, 'A.npy'), mmap_mode='r'),
                B=np.load(F_(kerja, 'B.npy'), mmap_mode='r'), K=np.load(F_(kerja, 'kawalan.npy')), pariti=json.load(open(F_(kerja, 'pariti.json'))))


def ukuran(S):
    """dict ukuran -> array [..., cara] daripada statistik [..., cara, NSTAT]."""
    S = np.asarray(S, np.float64)
    n, u, g, mn = S[..., IX['n']], S[..., IX['untung']], S[..., IX['rugi']], S[..., IX['menang']]
    with np.errstate(divide='ignore', invalid='ignore'):
        return dict(nisbah=c26.nisbah(S), purata=(u - g) / n, menang=mn, rugi15=S[..., IX['rugi15']], k50=S[..., IX['k50']],
                    sesi=S[..., IX['sesi_med']], untung_purata=u / (mn * n), rugi_purata=g / ((1 - mn) * n), n=n)


def nisbah_K3(S):
    S = np.asarray(S, np.float64)
    u, g = S[..., IX['untung_K3']], S[..., IX['rugi_K3']]
    with np.errstate(divide='ignore', invalid='ignore'):
        return np.where(g > 0, np.minimum(u / g, c26.NISBAH_MAKS), np.where(u > 0, c26.NISBAH_MAKS, np.nan))


def med(x, axis=None):
    with np.errstate(all='ignore'):
        import warnings
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            return np.nanmedian(x, axis=axis)


def ringkas(S, mask):
    """Nilai tengah merentas setup (mask) bagi setiap cara -> dict ukuran -> [cara]."""
    out = {k: [] for k in UKUR}
    ii = np.flatnonzero(mask)
    for a in range(0, S.shape[1], 1000):                      # berkeping: jimat memori
        U = ukuran(S[ii, a:a + 1000])
        for k in UKUR:
            out[k].append(med(U[k], axis=0))
    return {k: np.concatenate(v) for k, v in out.items()}


def baca(D, UB, K3B, KU, mask, w, cur=0, ikut='nisbah'):
    """Bacaan kumpulan B bagi cara w lawan cara sekarang. UB = ukuran setiap setup x cara (kumpulan B) bagi cara yang diminta."""
    g = lambda k, q: UB[k][q][mask]
    d = g(ikut, w) - g(ikut, cur)
    dn = g('nisbah', w) - g('nisbah', cur)
    k3 = mask & (D['nK3'][w] >= c26.MIN_K3) & (D['nK3'][cur] >= c26.MIN_K3)
    d3 = (K3B[w] - K3B[cur])[k3]
    dk = float(KU['nisbah'][w] - KU['nisbah'][cur])
    out = dict(cara=c26.kod(D['cara'][w]), ayat=c26.teks(D['cara'][w]), setup=int(mask.sum()), lebih_baik=int(np.nansum(d > 0)),
               d_nisbah=float(med(dn)), setup_K3=int(k3.sum()), lebih_baik_K3=int(np.nansum(d3 > 0)),
               d_nisbah_K3=float(med(d3)) if k3.any() else float('nan'), d_kawalan=dk)
    out.update({k: float(med(g(k, w))) for k in UKUR})
    out.update({f'kawalan_{k}': float(KU[k][w]) for k in ('nisbah', 'purata', 'menang', 'rugi15')})
    out.update(s1=bool(out['lebih_baik'] > out['setup'] / 2), s2=bool(out['d_nisbah_K3'] > 0), s3=bool(out['d_nisbah'] > dk),
               s4=bool(out['nisbah'] >= c26.SASARAN))
    out['lulus'] = bool(out['s1'] and out['s2'] and out['s3'])
    return out


def bacaan(D):
    SA, SB, K, cara, meta = D['A'], D['B'], D['K'], D['cara'], D['meta']
    ids, W = meta['ids'], len(cara)
    n1, ns = meta['n_tahap1'], meta['n_satu']
    ok = (np.asarray(SA[:, 0, 0]) >= c26.MIN_N) & (np.asarray(SB[:, 0, 0]) >= c26.MIN_N)
    L = {x['id']: x for x in c25.senarai()}
    kg = np.array([L[i]['kegunaan'] for i in ids])
    rasmi = ok & (kg == c26.RASMI)
    RA, RB, RBr = ringkas(SA, ok), ringkas(SB, ok), ringkas(SB, rasmi)
    KU = {k: v for k, v in ukuran(K).items()}
    F = int(np.nanargmax(RA['nisbah']))
    layak = RA['nisbah'] >= c26.SASARAN
    G = int(np.nanargmax(np.where(layak, RA['purata'], -np.inf))) if layak.any() else -1
    # cara tersendiri setiap setup: nisbah tertinggi pada kumpulan A antara cara peringkat (i) + (ii) dengan >= 30 dagangan
    Fi = np.full(len(ids), -1)
    for j in np.flatnonzero(ok):
        u = ukuran(SA[j, :n1])
        Fi[j] = int(np.nanargmax(np.where(u['n'] >= c26.MIN_N, u['nisbah'], -np.inf)))
    # ukuran setiap setup bagi cara yang dibaca
    perlu = sorted({0, F} | ({G} if G >= 0 else set()))
    UBs = {w: ukuran(SB[:, w]) for w in perlu}
    UB = {k: {w: UBs[w][k] for w in perlu} for k in UKUR}
    D['nK3'] = {w: np.asarray(SB[:, w, IX['n_K3']]) for w in perlu}
    K3B = {w: nisbah_K3(SB[:, w]) for w in perlu}
    B = dict(pariti=D['pariti'], kod_registry=len(L), dinilai=len(ids), tidak_dinilai=len(L) - len(ids), setup_ok=int(ok.sum()),
             setup_rasmi=int(rasmi.sum()), ruang=c26.RUANG, cara_dinilai=W, n_satu=ns, n_rawak=n1 - ns, n_naik_bukit=W - n1,
             n_kawalan=c26.N_KAWALAN, laluan=meta['laluan'],
             sekarang=baca(D, UB, K3B, KU, ok, 0), F=baca(D, UB, K3B, KU, ok, F))
    B['F']['nisbah_A'] = float(RA['nisbah'][F])
    B['bil_capai_sasaran_A'], B['bil_capai_sasaran_B'] = int(layak.sum()), int((RB['nisbah'] >= c26.SASARAN).sum())
    if G >= 0:
        B['G'] = baca(D, UB, K3B, KU, ok, G, ikut='purata')
        B['G']['nisbah_A'], B['G']['purata_A'] = float(RA['nisbah'][G]), float(RA['purata'][G])
    else:
        B['G'] = None
    # B3
    ii = np.flatnonzero(ok & (Fi >= 0))
    fi = np.array([ukuran(SB[j, Fi[j]])['nisbah'] for j in ii], np.float64)
    d = fi - UB['nisbah'][F][ii]
    B['Fi'] = dict(setup=int(len(ii)), lebih_baik=int(np.nansum(d > 0)), d_nisbah=float(med(d)), nisbah=float(med(fi)),
                   lebih_baik_sekarang=int(np.nansum(fi - UB['nisbah'][0][ii] > 0)))
    B['Fi']['lulus'] = bool(B['Fi']['lebih_baik'] > B['Fi']['setup'] / 2 and B['Fi']['d_nisbah'] >= c26.B3_MIN)
    # jadual semua cara
    tahap = ['satu demi satu'] * ns + ['rawak'] * (n1 - ns) + ['naik bukit'] * (W - n1)
    C = pd.DataFrame(dict(cara=[c26.kod(g) for g in cara], ayat=[c26.teks(g) for g in cara], tahap=tahap, nisbah_A=RA['nisbah'], purata_A=RA['purata']))
    for k in UKUR:
        C[f'{k}_B'] = RB[k]
    for k in ('nisbah', 'purata', 'menang', 'rugi15'):
        C[f'{k}_rasmi'] = RBr[k]
        C[f'kawalan_{k}'] = KU[k]
    # satu demi satu
    asas = c26.kanon(c26.ASAS)
    baris = []
    for q in range(ns):
        g = cara[q]
        beza = [i for i in range(c26.NK) if g[i] != asas[i]]
        if q and (len(beza) != 1 or (g[2] == 0 and beza != [2])):
            beza = [2] if g[2] == 0 else beza[:1]              # t0 dipiawaikan (komponen "bila mula" diabaikan)
        for i in (beza if q else range(c26.NK)):
            r = C.iloc[q]
            baris.append(dict(komponen=c26.NAMA_K[i], pilihan=c26.T_[i][c26.KOMPONEN[i][g[i]]], kod=c26.KOMPONEN[i][g[i]], asas=q == 0, cara=r.cara,
                              **{k: r[k] for k in C.columns if k.endswith('_B') or k.endswith('_rasmi') or k.startswith('kawalan_')}))
    Km = pd.DataFrame(baris)
    Km['_k'] = Km.komponen.map({n: i for i, n in enumerate(c26.NAMA_K)})
    Km['_p'] = [c26.KOMPONEN[int(k)].index(x) for k, x in zip(Km._k, Km.kod)]
    Km = Km.sort_values(['_k', '_p']).drop(columns=['_k', '_p']).reset_index(drop=True)
    # kesan purata setiap pilihan merentas cara rawak
    R = C.iloc[ns:n1]
    gr = np.array(cara[ns:n1])
    baris = []
    for i in range(c26.NK):
        for v, kd in enumerate(c26.KOMPONEN[i]):
            m = gr[:, i] == v
            if i == 3:
                m &= gr[:, 2] != 0
            x = R[m]
            baris.append(dict(komponen=c26.NAMA_K[i], pilihan=c26.T_[i][kd], kod=kd, bil_cara=int(m.sum()), nisbah_B=float(x.nisbah_B.median()),
                              purata_B=float(x.purata_B.median()), menang_B=float(x.menang_B.median()), rugi15_B=float(x.rugi15_B.median()),
                              bhg_capai_sasaran=float((x.nisbah_B >= c26.SASARAN).mean()), kawalan_nisbah=float(x.kawalan_nisbah.median())))
    Ef = pd.DataFrame(baris)
    # jadual setiap setup (kumpulan B)
    baris = []
    for j, i in enumerate(ids):
        x = L[i]
        b = dict(id=i, pusingan=x['pusingan'], kegunaan=x['kegunaan'], nama=x['nama'], prasyarat=x['prasyarat'], penapis=x['penapis'], cukup=bool(ok[j]))
        for tag, w in (('sekarang', 0), ('F', F), ('G', G), ('Fi', int(Fi[j]))):
            if w < 0:
                continue
            u = ukuran(SB[j, w])
            if tag == 'Fi':
                b['cara_Fi'], b['ayat_Fi'] = c26.kod(cara[w]), c26.teks(cara[w])
                b['nisbah_A_Fi'] = float(ukuran(SA[j, w])['nisbah'])
            b.update({f'{k}_{tag}': float(u[k]) for k in ('n', 'nisbah', 'purata', 'menang', 'rugi15', 'sesi')})
        baris.append(b)
    T = pd.DataFrame(baris)
    # laluan naik bukit dengan bacaan B
    for x in B['laluan']:
        r = C[C.cara == x['cara']].iloc[0]
        x.update(ayat=r.ayat, nisbah_B=float(r.nisbah_B), purata_B=float(r.purata_B), menang_B=float(r.menang_B), rugi15_B=float(r.rugi15_B),
                 kawalan_nisbah=float(r.kawalan_nisbah))
    return B, T, Km, Ef, C


def _bersih(x):
    if isinstance(x, dict):
        return {k: _bersih(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [_bersih(v) for v in x]
    if isinstance(x, (np.floating, float)):
        return None if not np.isfinite(x) else round(float(x), 6)
    if isinstance(x, np.integer):
        return int(x)
    if isinstance(x, np.bool_):
        return bool(x)
    return x


_p = lambda x, d=1: '–' if x is None or x != x else f'{100 * x:+.{d}f}'
_k = lambda x, d=0: '–' if x is None or x != x else f'{100 * x:.{d}f}'
_n = lambda x: '–' if x is None or x != x else f'{x:.2f}'
_h = lambda x: '–' if x is None or x != x else f'{x:.0f}'
_yt = lambda b: 'ya' if b else 'TIDAK'


def _bacaan_teks(tag, nama, b, ikut):
    return (f"- **Cara `{tag}` ({nama}): {b['ayat']}** (`{b['cara']}`). Pada saham yang carian tidak lihat, lawan cara sekarang: "
            f"(1) {ikut} lebih tinggi bagi {b['lebih_baik']:,} daripada {b['setup']:,} setup → {_yt(b['s1'])}; "
            f"(2) belian 2025–26: beza nisbah {b['d_nisbah_K3']:+.2f} ({b['lebih_baik_K3']:,} daripada {b['setup_K3']:,} setup lebih tinggi; perlu > 0) → {_yt(b['s2'])}; "
            f"(3) tambahan nisbah bagi setup {b['d_nisbah']:+.2f} lawan tambahan bagi saham rawak {b['d_kawalan']:+.2f} (perlu lebih besar) → {_yt(b['s3'])}. "
            f"**Keputusan: {'MENOLONG' if b['lulus'] else 'TIDAK menolong'}.** (4) Sasaran pengguna (nisbah ≥ 2): nisbah {_n(b['nisbah'])} → "
            f"**{'TERCAPAI' if b['s4'] else 'TIDAK tercapai'}** (saham rawak dengan cara sama: {_n(b['kawalan_nisbah'])}).")


_KEPALA = ('| Cara | Untung : rugi | Purata % | Menang % | Rugi ≥ 15 % | Purata untung (menang) % | Purata rugi (kalah) % | Hari pegang | '
           'Saham rawak: untung : rugi · purata % |\n|---|---|---|---|---|---|---|---|---|')


def _baris(nama, b):
    return (f"| {nama} | {_n(b['nisbah'])} | {_p(b['purata'])} | {_k(b['menang'])} | {_k(b['rugi15'])} | {_p(b['untung_purata'])} | "
            f"−{_k(b['rugi_purata'], 1)} | {_h(b['sesi'])} | {_n(b['kawalan_nisbah'])} · {_p(b['kawalan_purata'])} |")


def teks_laporan(B, T, Km, Ef, C):
    G = B['G']
    L = ['# CS26: stop loss × pegang × jual HABIS-HABISAN bagi setiap setup F, ikut "untung berbanding rugi" (backtest; BUKAN bukti)', '',
         'Peraturan ditulis dahulu: `kajian/SPEC_CARIAN_SETUP.md` pindaan 20 Nov 2026 (am). Dijana `cs_keluar26.py` / `cs_keluar26_lapor.py`; jangan sunting.', '',
         '- Soalan pengguna 20 Nov 2026: "betul ke method ni sahaja utk stop loss, hold dan exit? anda sudah lakukan kajian habis habisan?" '
         'Ukuran pilihan pengguna: jumlah untung jauh lebih besar daripada jumlah rugi (sasaran: sekurang-kurangnya 2 kali).',
         f"- {B['kod_registry']:,} kod dalam registry F; {B['dinilai']:,} dinilai; {B['setup_ok']:,} masuk bacaan ({B['setup_rasmi']:,} daripadanya \"{c26.RASMI}\").",
         f"- Ruang cara: {B['ruang']:,} gabungan daripada 10 komponen (13 stop loss × 5 \"potong awal\" × 34 tanda trend × 8 \"bila mula\" × 4 \"ketatkan\" × "
         f"8 \"ambil untung\" × 3 \"naik stop ke harga beli\" × 3 pasaran × 2 laporan kewangan × 4 had masa). Dinilai: {B['cara_dinilai']:,} cara "
         f"({B['n_satu']} satu demi satu, {B['n_rawak']:,} rawak, {B['n_naik_bukit']} naik bukit).",
         '- **Untung : rugi** = jumlah untung semua dagangan ÷ jumlah rugi semua dagangan sesuatu setup, selepas kos 0.5 %. 1.00 = pulang modal; 2.00 = untung dua kali rugi.',
         '- Cara dipilih pada saham carian; angka dibaca pada saham yang carian tidak lihat (nilai tengah merentas setup).',
         f"- Pariti dengan CS25: {B['pariti']['cara']} cara × {B['pariti']['setup']} setup, beza terbesar {B['pariti']['beza_terbesar']:.7f} → "
         f"{'lulus' if B['pariti']['lulus'] else 'GAGAL'}.", '',
         '## 1. Keputusan (ujian ditetapkan dahulu)', '',
         _bacaan_teks('F', 'untung : rugi tertinggi', B['F'], 'nisbah')]
    if G:
        L.append(_bacaan_teks('G', 'purata tertinggi antara cara dengan untung : rugi ≥ 2 pada saham carian', G, 'purata'))
    else:
        L.append('- **Cara `G` tidak wujud:** tiada satu pun cara yang dinilai mencapai nilai tengah untung : rugi ≥ 2 pada saham carian.')
    L += [f"- **Berapa cara mencapai sasaran ≥ 2 (nilai tengah merentas setup):** {B['bil_capai_sasaran_A']:,} daripada {B['cara_dinilai']:,} pada saham carian; "
          f"{B['bil_capai_sasaran_B']:,} pada saham yang carian tidak lihat.",
          f"- **Cara tersendiri setiap setup (`Fi`) lawan satu cara `F` untuk semua:** nisbah `Fi` lebih tinggi bagi {B['Fi']['lebih_baik']:,} daripada "
          f"{B['Fi']['setup']:,} setup; nilai tengah beza {B['Fi']['d_nisbah']:+.2f} (perlu lebih separuh DAN ≥ +0.05) → "
          f"**{'MENOLONG' if B['Fi']['lulus'] else 'TIDAK menolong: satu cara untuk semua sama baik'}** (nisbah `Fi` {_n(B['Fi']['nisbah'])}).", '',
          '## 2. Cara sekarang lawan cara terpilih', '', _KEPALA, _baris('Cara sekarang: ' + B['sekarang']['ayat'], B['sekarang']),
          _baris('`F`: ' + B['F']['ayat'], B['F'])]
    if G:
        L.append(_baris('`G`: ' + G['ayat'], G))
    L += ['', 'Lajur terakhir = 300,000 belian rawak pada saham yang sama, dijual dengan cara yang sama. Jika saham rawak mendapat nisbah yang sama, '
          'kelebihan itu datang daripada cara jual dan pasaran, bukan daripada setup.', '',
          '## 3. Setiap komponen, satu demi satu (sembilan yang lain kekal seperti cara sekarang)', '',
          '| Komponen | Pilihan | Untung : rugi | Purata % | Menang % | Rugi ≥ 15 % | Purata untung % | Purata rugi % | Hari | Setiap minggu: untung : rugi · purata % · rugi ≥ 15 % | '
          'Saham rawak: untung : rugi · purata % |', '|---|---|---|---|---|---|---|---|---|---|---|']
    for r in Km.itertuples():
        L.append(f"| {r.komponen} | {r.pilihan}{' **(sekarang)**' if r.asas else ''} | {_n(r.nisbah_B)} | {_p(r.purata_B)} | {_k(r.menang_B)} | {_k(r.rugi15_B)} | "
                 f"{_p(r.untung_purata_B)} | −{_k(r.rugi_purata_B, 1)} | {_h(r.sesi_B)} | {_n(r.nisbah_rasmi)} · {_p(r.purata_rasmi)} · {_k(r.rugi15_rasmi)} | "
                 f"{_n(r.kawalan_nisbah)} · {_p(r.kawalan_purata)} |")
    L += ['', f"## 4. Kesan setiap pilihan merentas {B['n_rawak']:,} cara rawak (nilai tengah bagi semua cara yang mengandungi pilihan itu)", '',
          'Jadual §3 menukar satu perkara daripada cara sekarang; jadual ini menunjukkan sama ada pilihan itu baik secara umum, apa pun sembilan komponen lain.', '',
          '| Komponen | Pilihan | Bilangan cara | Untung : rugi | Purata % | Menang % | Rugi ≥ 15 % | Bahagian cara yang mencapai ≥ 2 | Saham rawak: untung : rugi |',
          '|---|---|---|---|---|---|---|---|---|']
    for r in Ef.itertuples():
        L.append(f"| {r.komponen} | {r.pilihan} | {r.bil_cara:,} | {_n(r.nisbah_B)} | {_p(r.purata_B)} | {_k(r.menang_B)} | {_k(r.rugi15_B)} | "
                 f"{_k(r.bhg_capai_sasaran)} % | {_n(r.kawalan_nisbah)} |")
    L += ['', '## 5. Naik bukit pada saham carian (setiap langkah menukar satu komponen)', '',
          '| Langkah | Cara | Saham carian: untung : rugi | Tidak dilihat: untung : rugi | Purata % | Menang % | Rugi ≥ 15 % | Saham rawak: untung : rugi |',
          '|---|---|---|---|---|---|---|---|']
    for x in B['laluan']:
        L.append(f"| {x['pusingan']} | {x['ayat']} | {_n(x['nisbah_A'])} | {_n(x['nisbah_B'])} | {_p(x['purata_B'])} | {_k(x['menang_B'])} | {_k(x['rugi15_B'])} | "
                 f"{_n(x['kawalan_nisbah'])} |")
    L += ['', '## 6. Dua puluh cara teratas pada saham carian, dan bacaannya pada saham yang carian tidak lihat', '',
          '| Cara | Saham carian: untung : rugi | Tidak dilihat: untung : rugi | Purata % | Menang % | Rugi ≥ 15 % | Hari | Saham rawak: untung : rugi · purata % |',
          '|---|---|---|---|---|---|---|---|']
    for r in C.sort_values('nisbah_A', ascending=False).head(20).itertuples():
        L.append(f"| {r.ayat} | {_n(r.nisbah_A)} | {_n(r.nisbah_B)} | {_p(r.purata_B)} | {_k(r.menang_B)} | {_k(r.rugi15_B)} | {_h(r.sesi_B)} | "
                 f"{_n(r.kawalan_nisbah)} · {_p(r.kawalan_purata)} |")
    L += ['', 'Semua cara yang dinilai: `cara.csv.gz`. Setiap setup: `setup.csv.gz`.', '', '## 7. Kaveat', '',
          f"- {B['cara_dinilai']:,} cara dinilai daripada {B['ruang']:,}; \"terbaik\" di sini bermaksud terbaik antara yang dinilai.",
          '- Tiada saham mati dalam data: untung : rugi condong ke atas, lebih-lebih lagi bagi cara yang memegang lama.',
          '- Ribuan cara dicuba; yang terbaik pada saham carian condong ke atas. Sebab itu bacaan dibuat pada saham yang carian tidak lihat.',
          '- Saham yang carian tidak lihat sudah dipakai berkali-kali; 2025–26 pendek.',
          '- Jualan stop loss dianggap tepat pada parasnya; tanda "laporan kewangan" memakai tarikh laporan sebenar.',
          '- Tiada perubahan pada registry F, senarai utama, Top 100 atau dashboard: menukar cara berdaftar ialah keputusan pengguna.',
          '- Pangkat backtest, BUKAN bukti.', '']
    return '\n'.join(L)


def lapor_(kerja):
    D = muat(kerja)
    B, T, Km, Ef, C = bacaan(D)
    os.makedirs(c26.HASIL, exist_ok=True)
    B = _bersih(B)
    json.dump(B, open(os.path.join(c26.HASIL, 'bacaan.json'), 'w'), indent=1, ensure_ascii=False)
    gz = {'method': 'gzip', 'mtime': 0}
    T.round(5).to_csv(os.path.join(c26.HASIL, 'setup.csv.gz'), index=False, compression=gz)
    Km.round(5).to_csv(os.path.join(c26.HASIL, 'komponen.csv'), index=False)
    Ef.round(5).to_csv(os.path.join(c26.HASIL, 'kesan.csv'), index=False)
    C.round(5).to_csv(os.path.join(c26.HASIL, 'cara.csv.gz'), index=False, compression=gz)
    open(os.path.join(c26.HASIL, 'KELUAR.md'), 'w').write(teks_laporan(B, T, Km, Ef, C))
    cari.log(f"CS26 lapor: {B['dinilai']} setup · {B['cara_dinilai']} cara · F={B['F']['cara']} nisbah {B['F']['nisbah']} lulus={B['F']['lulus']} sasaran={B['F']['s4']}")
    return B
