# laporan_pit.py — jana BacktestShariah2/kajian/pit/LAPORAN.md daripada data/analisis/ujian_pit.json (dipanggil uji_pit.py gabung).
# Jangan sunting LAPORAN.md secara manual; ubah teks tetap di sini dan jana semula.
import json, math, os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))


def _p(x, d=1):
    return '–' if x is None or (isinstance(x, float) and math.isnan(x)) else f'{x * 100:.{d}f}%'


def _f(x, d=2):
    return '–' if x is None or (isinstance(x, float) and math.isnan(x)) else f'{x:.{d}f}'


def _med(v):
    v = [x for x in v if x is not None and not (isinstance(x, float) and math.isnan(x))]
    return float(np.median(v)) if v else None


def _pendek(s, n=34):
    s = (s or '').replace('|', '/')
    return s if len(s) <= n else s[:n - 1] + '…'


def _baris(k, v):
    b = v.get('bt431') or {}
    return (f"| {k} | {_pendek(v.get('nama'))} | {'Y' if v.get('swing') else ''} | {v.get('n_isyarat') or 0} | "
            f"{_p(v.get('lebihan_rawak'), 2)} | {_f(v.get('t_rawak'))} | {_p(v.get('cagr'))} | {_p(v.get('cagr_tanpa10'))} | "
            f"{_p(v.get('mdd'), 0)} | {_f(v.get('dsr'))} | {_p(b.get('cagr'))} | {'LULUS' if v.get('lulus_B') else 'gagal'} | "
            f"{', '.join(x.split(' ')[0] for x in v.get('sebab_gagal') or [])} |")


KEPALA = ('| Kaedah | Nama | Swing | Isyarat | Lebihan rawak / dagangan | t (bulan) | CAGR 8 slot | CAGR tanpa 10 terbaik | MDD | DSR | '
          'CAGR set 431 (registry) | Pintu B | Gagal |\n|---|---|---|---|---|---|---|---|---|---|---|---|---|')


def tulis(J, meta, path):
    K = J['kaedah']; ks = list(K)
    pen = J.get('penanda', {})
    ewA = pen.get('ew_A', {}); spy = pen.get('spy', {})
    lul = [k for k in ks if K[k]['lulus_B']]
    gagal = {}
    for k in ks:
        for s in K[k]['sebab_gagal']:
            gagal[s.split(' ')[0]] = gagal.get(s.split(' ')[0], 0) + 1
    n = len(ks)
    t_pos3 = [k for k in ks if (K[k].get('t_rawak') or -9) >= 3 and (K[k].get('lebihan_rawak') or 0) > 0]
    t_pos2 = [k for k in ks if (K[k].get('t_rawak') or -9) >= 2 and (K[k].get('lebihan_rawak') or 0) > 0]
    t_neg2 = [k for k in ks if (K[k].get('t_rawak') or 9) <= -2]
    ew_c = ewA.get('cagr')
    atasi_ew = [k for k in ks if (K[k].get('cagr') or -9) > (K[k].get('ew_cagr') or 9)]
    atasi_ew10 = [k for k in ks if (K[k].get('cagr_tanpa10') or -9) > (K[k].get('ew_cagr') or 9)]
    atasi_spy = [k for k in ks if spy.get('cagr') is not None and (K[k].get('cagr') or -9) > spy['cagr']]
    bt = [(k, K[k]['bt431']) for k in ks if K[k].get('bt431')]
    bt_ew = [k for k, b in bt if b.get('cagr') is not None and b.get('ew_cagr') is not None and b['cagr'] > b['ew_cagr']]
    v12 = [(K[k].get('v12_setara') or {}).get('cagr') for k in ks]
    v13 = [K[k].get('cagr') for k in ks]
    beza_enjin = _med([a - b for a, b in zip(v12, v13) if a is not None and b is not None])
    k431c = [(K[k].get('k431') or {}).get('cagr') for k in ks]
    k431_ew = [(K[k].get('k431') or {}).get('ew_cagr') for k in ks]
    k431_atasi = sum(1 for a, b in zip(k431c, k431_ew) if a is not None and b is not None and a > b)
    vb = [(K[k].get('versi_B') or {}) for k in ks]
    vb_atasi = sum(1 for x in vb if x.get('cagr') is not None and x.get('ew_cagr') is not None and x['cagr'] > x['ew_cagr'])
    vb_t3 = sum(1 for x in vb if (x.get('t_rawak') or -9) >= 3 and (x.get('lebihan_rawak') or 0) > 0)
    pbo = J.get('pbo_set') or {}
    dsr = J.get('dsr') or {}
    a = J['alam']
    L = []
    L.append('# LAPORAN: Ujian semula point-in-time (PIT) — Pintu B\n')
    L.append(f"Dijana {J['dibina']} oleh `kajian/pit/uji_pit.py gabung`. Pra-daftar: [`PRA_DAFTAR.md`](PRA_DAFTAR.md) (dicommit sebelum "
             f"larian). Data: `data/analisis/ujian_pit.json`. Cawangan pratonton `pt/pit`; tiada perubahan pada `main`, enjin v1.2, "
             f"modul kaedah, registry, penganalisis atau dashboard. Semua angka backtest kertas; tiada order, tiada wang sebenar.\n")
    L.append('## 1. Ringkasan\n')
    L.append(f"- **Pintu B: {len(lul)} daripada {n} kaedah lulus**" + (f" ({', '.join(lul)})." if lul else '.')
             + f" Kaedah diuji: {n} (swing {J['kiraan']['swing_diuji']}); belum diuji: {len(J['kiraan']['belum_diuji'])}"
             + (f" ({', '.join(J['kiraan']['belum_diuji'])})" if J['kiraan']['belum_diuji'] else '') + '; ralat: '
             + (', '.join(J['kiraan']['ralat']) if J['kiraan']['ralat'] else 'tiada') + '.')
    L.append(f"- Lebihan atas belian rawak tempoh sama (semua isyarat, selepas kos 0.25%/sisi kedua-dua kaki): t ≥ 3 dan positif "
             f"{len(t_pos3)}/{n}" + (f" ({', '.join(t_pos3)})" if t_pos3 else '') + f"; t ≥ 2 positif {len(t_pos2)}/{n}; "
             f"t ≤ −2 (lebih teruk daripada rawak) {len(t_neg2)}/{n}.")
    L.append(f"- CAGR portfolio 8 slot > EW alam ({_p(ew_c)} setahun): {len(atasi_ew)}/{n}; tanpa 10 dagangan terbaik masih > EW: "
             f"{len(atasi_ew10)}/{n}; > SPY ({_p(spy.get('cagr'))}): {len(atasi_spy)}/{n}.")
    L.append(f"- Bandingan set 431 (registry dalam sampel, enjin v1.2, 2019-11 – 2026-10): {len(bt_ew)}/{len(bt)} varian aktif "
             f"mengatasi EW 431 di sana. Atas alam PIT hanya {len(atasi_ew)}/{n} mengatasi EW alam sendiri.")
    L.append(f"- PBO proses \"pilih kaedah terbaik\" (CSCV 16 blok, {pbo.get('K')} kaedah): **{_f(pbo.get('pbo'))}**"
             + (' (> 0.5: memilih yang terbaik dalam sampel lebih kerap jatuh di bawah median luar sampel).' if (pbo.get('pbo') or 0) > 0.5
                else '.'))
    L.append('')
    sw = [k for k in ks if K[k].get('swing')]
    L.append(f"- Kaedah swing (purata pegang backtest 3–30 hari) + PLAYBOOK: {sum(1 for k in sw if K[k]['lulus_B'])}/{len(sw)} lulus; "
             f"t ≥ 3 positif {sum(1 for k in sw if k in t_pos3)}/{len(sw)}; CAGR > EW {sum(1 for k in sw if k in atasi_ew)}/{len(sw)}.")
    L.append('- Semua modul `kod/kaedah/M*.py` memakai varian aktif registry set 431 (`VARIAN` = `varian_kod` katalog bagi 134/134; '
             'disemak sebelum larian), PARAM asal, tanpa penalaan.')
    L.append('')
    L.append('## 2. Alam dan had\n')
    L.append(f"- Sumber: {a['sumber']} (yfinance auto_adjust + faktor_split). {a['ticker_data']} ticker; data "
             f"{meta['mula_data']} – {meta['akhir_data']}; kemasukan {J['mula']} – {J['akhir']}.")
    L.append(f"- Syarat layak harian (data ≤ hari isyarat): tutup_mentah ≥ USD{a['syarat']['harga_min']:.0f}, median "
             f"{a['syarat']['tetingkap_nilai']} sesi nilai dagangan ≥ USD{a['syarat']['nilai_min'] / 1e6:.0f} juta, ≥ "
             f"{a['syarat']['bar_min']} bar.")
    L.append(f"- Saringan sektor Shariah: {a['ticker_sektor_kecuali']} ticker dikecualikan (industri tidak patuh, tiada industri, "
             f"babi); {a['ticker_sektor_ok']} lulus. Pernah layak: versi A {a['pernah_layak']['A']}, versi B {a['pernah_layak']['B']}, "
             f"K431 {a['pernah_layak']['K431']} ticker.")
    sp = J.get('penyintas_sp500') or {}
    L.append(f"- **Saham delist: {a['ticker_delist']}.** Calon ticker A02 = senarai tersenarai Okt 2026. Semakan keahlian S&P 500 "
             f"sejarah (fja05680/sp500): {sp.get('tiada', '–')} daripada {sp.get('ahli_sejak_2013', '–')} ahli sejak 2013 tiada dalam "
             f"data (kebanyakan diambil alih/delist, sebahagian tukar simbol). Sumber harga saham delist tidak boleh dicapai dari "
             f"sesi ini (Yahoo/Stooq/Nasdaq disekat proksi; pelan FMP tidak membenarkan; SEC tidak digunakan). Keputusan = HAD ATAS.")
    L.append('- Nisbah kewangan ikut tarikh tidak tersedia; versi A = sektor sahaja (utama), versi B = A ∩ skrin Shariah Moomoo '
             'semasa (`data/harga/univ.txt`, pandang hadapan). Peta industri semasa dipakai untuk semua tarikh. Harga dilaras '
             'dividen (syarat USD10 sedikit ketat pada tahun awal). Storan A02 mungkin tertinggal saham baharu 2025–26 bernilai '
             'dagangan USD5–13 juta.')
    L.append('\nSaiz alam (median saham layak sehari):\n')
    L.append('| Tahun | A (utama) | B (Shariah semasa) | K431 | Tanpa sektor |\n|---|---|---|---|---|')
    for y, r in sorted(a['median_layak_setahun'].items()):
        L.append(f"| {y} | {r['A']} | {r['B']} | {r['K431']} | {r['layak_tanpa_sektor']} |")
    L.append('')
    L.append('## 3. Penanda aras\n')
    L.append('| Penanda aras | CAGR | MDD |\n|---|---|---|')
    for nm, kk in (('EW alam A (utama)', 'ew_A'), ('EW alam B', 'ew_B'), ('EW K431', 'ew_K431'), ('SPY', 'spy')):
        x = pen.get(kk, {}); L.append(f"| {nm} | {_p(x.get('cagr'))} | {_p(x.get('mdd'))} |")
    L.append('\nEW = purata sama berat pulangan harian tutup-ke-tutup saham layak pada tutup semalam (dihad ±50%, tanpa kos; '
             'konvensyen `standard/penanda_ew.py`). Belian rawak tempoh sama: 20 benih setiap dagangan, kos sama.\n')
    yrs = sorted(set(ewA.get('tahunan', {})) | set(spy.get('tahunan', {})))
    if yrs:
        L.append('| Tahun | ' + ' | '.join(yrs) + ' |\n|---|' + '---|' * len(yrs))
        L.append('| EW A | ' + ' | '.join(_p(ewA.get('tahunan', {}).get(y)) for y in yrs) + ' |')
        L.append('| SPY | ' + ' | '.join(_p(spy.get('tahunan', {}).get(y)) for y in yrs) + ' |')
        med = []
        for y in yrs:
            v = [K[k]['tahunan'].get(y) - K[k]['tahunan_ew'].get(y) for k in ks
                 if K[k].get('tahunan') and K[k].get('tahunan_ew') and K[k]['tahunan'].get(y) is not None
                 and K[k]['tahunan_ew'].get(y) is not None]
            med.append((_med(v), sum(1 for x in v if x > 0), len(v)))
        L.append('| Median kaedah − EW | ' + ' | '.join(_p(m[0]) for m in med) + ' |')
        L.append('| Kaedah > EW | ' + ' | '.join(f'{m[1]}/{m[2]}' for m in med) + ' |')
    L.append('')
    L.append('## 4. Pintu B (versi A)\n')
    L.append(f"Syarat (pra-daftar §7): B0 ≥ 30 dagangan portfolio dan ≥ 24 bulan; B1 lebihan rawak > 0 dan t ≥ 3; B2 CAGR > EW; "
             f"B3 DSR ≥ 0.5 (N = {dsr.get('N')} = {dsr.get('N_sejarah')} varian sejarah + {dsr.get('K')} kaedah kajian ini; "
             f"SR0 = {_f(dsr.get('sr0_tahunan'))} setahun atas pulangan lebihan EW); B4 CAGR tanpa 10 terbaik > EW; B5 PBO per "
             f"kaedah tidak boleh dikira (satu varian beku).\n")
    L.append('Kegagalan mengikut syarat: ' + ', '.join(f'{k} {v}' for k, v in sorted(gagal.items())) + '.\n')
    urut = sorted(ks, key=lambda k: -(K[k].get('t_rawak') if K[k].get('t_rawak') is not None else -99))
    L.append('### 4.1 Dua puluh lima teratas ikut t lebihan rawak\n')
    L.append(KEPALA)
    for k in urut[:25]: L.append(_baris(k, K[k]))
    L.append('')
    L.append('## 5. Banding dengan set 431 dan kesan setiap pembaikan\n')
    regc = [b.get('cagr') for _, b in bt]
    L.append(f"- Median CAGR varian aktif dalam registry set 431: {_p(_med(regc))} (EW 431 di sana "
             f"{_p(_med([b.get('ew_cagr') for _, b in bt]))}). Median CAGR portfolio atas alam PIT versi A: {_p(_med(v13))} "
             f"(EW alam {_p(ew_c)}).")
    L.append(f"- Kesan enjin (versi A, tempoh sama): median CAGR v1.2-setara (kos 0.1%, tanpa [B1]) tolak v1.3 = "
             f"{_p(beza_enjin)} setahun. Dagangan semua isyarat yang dicetus [B1]: "
             f"{sum((K[k].get('jurang_b1') or 0) for k in ks)} (jumlah semua kaedah).")
    L.append(f"- Kesan alam (diagnostik K431 = 431 ticker asal, syarat layak sama, 2013–2026, enjin v1.3): median CAGR "
             f"{_p(_med(k431c))} lawan EW K431 {_p(pen.get('ew_K431', {}).get('cagr'))}; {k431_atasi}/{n} mengatasi EW K431. "
             f"Bandingkan versi A (alam penuh): median {_p(_med(v13))}.")
    L.append(f"- Versi B (kepekaan, Shariah semasa): {vb_atasi}/{n} CAGR > EW B ({_p(pen.get('ew_B', {}).get('cagr'))}); "
             f"t rawak ≥ 3 positif: {vb_t3}/{n}.")
    L.append('\nPenguraian bagi 15 kaedah dengan CAGR registry set 431 tertinggi (setiap lajur menukar satu perkara; EW lajur '
             'yang sepadan dalam kurungan):\n')
    L.append('| Kaedah | Set 431 registry (v1.2, 2019-11 – 2026-10) | K431 PIT (v1.3, 2013–2026) | Alam A, v1.2-setara | Alam A, v1.3 '
             '| Lebihan rawak A (t) |\n|---|---|---|---|---|---|')
    top = sorted([k for k in ks if (K[k].get('bt431') or {}).get('cagr') is not None], key=lambda k: -K[k]['bt431']['cagr'])[:15]
    for k in top:
        b = K[k]['bt431']; q = K[k].get('k431') or {}; v2 = K[k].get('v12_setara') or {}
        L.append(f"| {k} | {_p(b.get('cagr'))} ({_p(b.get('ew_cagr'))}) | {_p(q.get('cagr'))} ({_p(q.get('ew_cagr'))}) | "
                 f"{_p(v2.get('cagr'))} | {_p(K[k].get('cagr'))} ({_p(K[k].get('ew_cagr'))}) | "
                 f"{_p(K[k].get('lebihan_rawak'), 2)} ({_f(K[k].get('t_rawak'))}) |")
    L.append('')
    L.append('## 6. Rejim pasaran dan subtempoh (versi A)\n')
    ra = [((K[k].get('rejim_isyarat') or {}).get('spy_atas_sma200') or {}).get('lebihan_rawak') for k in ks]
    rb = [((K[k].get('rejim_isyarat') or {}).get('spy_bawah_sma200') or {}).get('lebihan_rawak') for k in ks]
    s1 = [((K[k].get('subtempoh') or {}).get('2013_2018') or {}) for k in ks]
    s2 = [((K[k].get('subtempoh') or {}).get('2019_2026') or {}) for k in ks]
    L.append(f"- Median lebihan rawak setiap dagangan: SPY > SMA200 {_p(_med(ra), 2)} ({sum(1 for x in ra if x and x > 0)}/{n} "
             f"positif); SPY < SMA200 {_p(_med(rb), 2)} ({sum(1 for x in rb if x and x > 0)}/{n} positif).")
    L.append(f"- 2013–2018 (kaedah tidak pernah direka atas tempoh ini): {sum(1 for x in s1 if (x.get('cagr') or -9) > (x.get('ew_cagr') or 9))}"
             f"/{n} CAGR > EW; 2019–2026: {sum(1 for x in s2 if (x.get('cagr') or -9) > (x.get('ew_cagr') or 9))}/{n}.")
    L.append('')
    if 'PLAYBOOK' in K:
        p = K['PLAYBOOK']
        L.append('## 7. Playbook (RS 80–94 + Trend Template + ≤ 15% dari tinggi 52 minggu + ATR14% ≤ 6%; pegang 21 hari)\n')
        L.append(f"- Isyarat {p.get('n_isyarat')}; lebihan rawak {_p(p.get('lebihan_rawak'), 2)} setiap dagangan (t {_f(p.get('t_rawak'))}); "
                 f"portfolio {p.get('n_dagangan')} dagangan, CAGR {_p(p.get('cagr'))} (tanpa 10 terbaik {_p(p.get('cagr_tanpa10'))}), "
                 f"MDD {_p(p.get('mdd'))}, EW {_p(p.get('ew_cagr'))}, DSR {_f(p.get('dsr'))}. Pintu B: "
                 f"{'LULUS' if p['lulus_B'] else 'gagal (' + ', '.join(p['sebab_gagal']) + ')'}.")
        rj = p.get('rejim_isyarat') or {}
        L.append(f"- Rejim: SPY > SMA200 lebihan {_p((rj.get('spy_atas_sma200') or {}).get('lebihan_rawak'), 2)} "
                 f"(t {_f((rj.get('spy_atas_sma200') or {}).get('t'))}); SPY < SMA200 "
                 f"{_p((rj.get('spy_bawah_sma200') or {}).get('lebihan_rawak'), 2)} (t {_f((rj.get('spy_bawah_sma200') or {}).get('t'))}).")
        L.append('')
    L.append('## 8. Penyimpangan daripada pra-daftar\n')
    for x in J.get('penyimpangan') or ['Tiada.']:
        L.append(f'- {x}')
    L.append('')
    L.append('## 9. Menguji kaedah tambahan (cth. M168)\n')
    L.append('```\npython3 BacktestShariah2/kajian/pit/uji_pit.py muat  --data DIR      # sekali (Release autotune-data-a02)\n'
             'python3 BacktestShariah2/kajian/pit/uji_pit.py jalan --data DIR --kaedah M168   # atau --modul FAIL.py\n```\n'
             '`jalan` membina cache jika perlu, menjalankan kaedah dengan peraturan sama, kemudian `gabung` (N DSR bertambah, '
             'JSON dan laporan ini dijana semula).\n')
    L.append('## Lampiran: semua kaedah (ikut t lebihan rawak)\n')
    L.append(KEPALA)
    for k in urut: L.append(_baris(k, K[k]))
    L.append('')
    with open(path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(L))
