# jurnal.py — jurnal mingguan automatik Papertrade C (semakan pasca-dagangan; dashboard v105 Lagi › Jurnal, audit 25 Okt 2026).
# Dokumen db `jurnal/minggu` dijana oleh jana_db.py daripada CSV sahaja (tanpa LLM, tanpa andaian):
#   belian, keluar lorong kaedah ikut sebab, keluar lorong 2, langkauan belian 9:35 NY (papertrade/langkau), gelinciran buka
#   (harga beli = buka lawan tutup hari isyarat; jurang > +5%), buka bawah henti (langkau "buka <= henti" dan keluar "kena henti
#   (buka bawah henti)"), posisi melintas earnings (kalendar gabungan kalendar_earnings.py), posisi tidak sah (tidak cair, ambil
#   alih, kelas berganda, delist) dan "pelajaran" berasaskan peraturan: teks BM ringkas dengan nombor sebenar, hanya jika data ada.
#
#   python3 BacktestShariah2/standard/jurnal.py [--folder papertrade] [--minggu 4] [--keluar <fail.json>]
#
# Minggu = Isnin–Jumaat (sesi NYSE). Belian dikira pada tarikh_beli, keluar pada tarikh_keluar / tarikh_keluar_henti.
# Rekod sahaja: tiada order, tiada wang sebenar.
import argparse, glob, json, os, re, sys
from datetime import date, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
BS2 = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import sahkan as SH  # noqa: E402

JURANG = 5.0              # jurang buka > +5% di atas tutup hari isyarat
HENTI_MIN_KELUAR = 5      # kaedah dengan >= 5 keluar seminggu untuk pelajaran "kerap kena henti"
LABEL_KELUAR = {'henti': 'kena henti', 'buka_bawah_henti': 'kena henti (buka bawah henti)', 'sasaran': 'capai sasaran',
                'isyarat': 'isyarat keluar kaedah', 'masa': 'had masa', 'ambil_alih': 'isyarat palsu (ambil alih)',
                'tidak_cair': 'tidak cair', 'delist': 'delist', 'lain': 'lain'}
LABEL_TS = {'ambil_alih': 'ambil alih', 'tidak_cair': 'tidak cair', 'kelas_berganda': 'kelas berganda', 'delist': 'delist', 'lain': 'lain'}


def _f(v):
    return SH.nombor(v)


def _pur(a):
    a = [x for x in a if x is not None]
    return round(sum(a) / len(a), 2) if a else None


def _med(a):
    a = sorted(x for x in a if x is not None)
    if not a:
        return None
    n = len(a)
    return round(a[n // 2] if n % 2 else (a[n // 2 - 1] + a[n // 2]) / 2, 2)


def _kuantil(a, q):
    a = sorted(x for x in a if x is not None)
    if not a:
        return None
    i = min(len(a) - 1, max(0, int(round(q * (len(a) - 1)))))
    return round(a[i], 2)


def kategori_langkau(s):
    s = str(s or '')
    if 'buka_maks' in s:
        return 'buka > buka_maks'
    if re.search(r'(≤|<=)\s*henti', s):
        return 'buka ≤ henti'
    if 'didagang' in s:
        return 'belum didagangkan'
    if 'batal' in s:
        return 'isyarat batal'
    return 'lain'


def _minggu(S, n):
    d = date.fromisoformat(str(S)[:10])
    isn = d - timedelta(days=d.weekday())
    return [(isn - timedelta(days=7 * i), isn - timedelta(days=7 * i) + timedelta(days=4)) for i in range(n)]


def tutup_isyarat(C, stor, terkini=None):
    """{(saham, tarikh_isyarat): tutup} daripada stor harga (+ terkini.csv), bagi gelinciran buka."""
    import jana_db as J
    perlu = {(r['saham'], r['tarikh_isyarat']) for r in C if r.get('tarikh_isyarat') and r.get('saham')}
    if not perlu:
        return {}
    fr = J.bar_harga(stor, ('ticker', 'date', 'close'), terkini)
    tik = {s for s, _ in perlu}
    fr = fr[fr.ticker.isin(tik)]
    m = {(t, int(d)): float(c) for t, d, c in zip(fr.ticker, fr.date, fr.close)}
    out = {}
    for s, t in perlu:
        c = m.get((s, int(t.replace('-', ''))))
        if c:
            out[(s, t)] = c
    return out


def jurnal(C, langkau=None, stor=None, terkini=None, S=None, minggu=4, KAL=None, dibina=''):
    """C = baris CSV papertrade/claude*.csv; langkau = papertrade/langkau rows; S = sesi data. -> dokumen jurnal/minggu."""
    import jana_db as J
    b = SH.benar
    if KAL is None:
        try:
            import kalendar_earnings as KE
            KAL = KE.muat()
        except Exception:  # noqa: BLE001
            KAL = {}
    S = str(S or max((r.get('tarikh_beli') or '' for r in C), default=''))[:10]
    if not S:
        return dict(dibina=dibina, minggu=[], nota='Tiada posisi.')
    pos = [r for r in C if r.get('harga_beli') not in (None, '') and not b(r.get('tidak_dibeli'))]
    sah = [r for r in pos if not b(r.get('tidak_sah'))]
    T = tutup_isyarat(pos, stor, terkini) if stor else {}
    hasil = lambda r: _f(r.get('untung_akhir_pct')) if b(r.get('keluar')) else _f(r.get('untung_pct'))

    def earn_dalam(r, a, z):
        """Tarikh earnings dalam (tarikh_beli, akhir pegangan] yang jatuh dalam [a, z]."""
        akhir = r.get('tarikh_keluar') if b(r.get('keluar')) and r.get('tarikh_keluar') else S
        if b(r.get('keluar_henti')) and r.get('tarikh_keluar_henti'):
            akhir = max(akhir, r['tarikh_keluar_henti'])
        elif b(r.get('keluar')) and not b(r.get('tutup_semua')):
            akhir = S          # lorong 2 masih dipegang
        tb = r.get('tarikh_beli') or ''
        x = [d.isoformat() for d in (KAL or {}).get(r.get('saham'), {}) if tb < d.isoformat() <= akhir and a <= d.isoformat() <= z]
        return min(x) if x else None

    out = []
    for isn, jum in _minggu(S, minggu):
        a, z = isn.isoformat(), min(jum.isoformat(), S)
        if a > S:
            continue
        dlm = lambda t: bool(t) and a <= t <= z
        beli = [r for r in pos if dlm(r.get('tarikh_beli'))]
        beli_s = [r for r in beli if not b(r.get('tidak_sah'))]
        kel = [r for r in sah if b(r.get('keluar')) and dlm(r.get('tarikh_keluar'))]
        kel2 = [r for r in sah if b(r.get('keluar_henti')) and dlm(r.get('tarikh_keluar_henti'))]
        lk = [r for r in (langkau or []) if dlm(r.get('tarikh'))]
        if not (beli or kel or kel2 or lk):
            continue
        sebab = {}
        for r in kel:
            j = J.jenis_keluar(r.get('isyarat_keluar'))
            x = sebab.setdefault(j, dict(n=0, u=[]))
            x['n'] += 1; x['u'].append(_f(r.get('untung_akhir_pct')))
        sebab = {k: dict(n=v['n'], purata=_pur(v['u']), label=LABEL_KELUAR.get(k, k)) for k, v in sorted(sebab.items(), key=lambda kv: -kv[1]['n'])}
        lkk = {}
        for r in lk:
            k = kategori_langkau(r.get('sebab'))
            lkk[k] = lkk.get(k, 0) + 1
        # gelinciran buka: harga beli (buka) lawan tutup hari isyarat
        gap = []
        for r in beli_s:
            c = T.get((r.get('saham'), r.get('tarikh_isyarat')))
            hb = _f(r.get('harga_beli'))
            if c and hb:
                gap.append((round((hb / c - 1) * 100, 2), r))
        g5 = [r for g, r in gap if g > JURANG]
        g5s = {id(r) for r in g5}
        lain = [r for g, r in gap if id(r) not in g5s]
        # buka bawah henti
        bbh = [r for r in kel if J.jenis_keluar(r.get('isyarat_keluar')) == 'buka_bawah_henti']
        hb_ = [r for r in kel if J.jenis_keluar(r.get('isyarat_keluar')) == 'henti']
        # lintas earnings
        le = [(r, earn_dalam(r, a, z)) for r in sah if (r.get('tarikh_beli') or '') <= z]
        le = [(r, e) for r, e in le if e]
        le_kel = [r for r, _ in le if b(r.get('keluar')) and dlm(r.get('tarikh_keluar'))]
        le_id = {id(r) for r in le_kel}
        tanpa_e = [r for r in kel if id(r) not in le_id]
        # tidak sah (dibeli minggu ini)
        tsj = {}
        for r in beli:
            if b(r.get('tidak_sah')):
                k = J.jenis_tidak_sah(r.get('sebab_tidak_sah'))
                tsj[k] = tsj.get(k, 0) + 1
        ts_tutup = [r for r in pos if b(r.get('tidak_sah')) and b(r.get('keluar')) and dlm(r.get('tarikh_keluar'))]
        # kaedah kerap kena henti
        kk = {}
        for r in kel:
            x = kk.setdefault(r.get('kaedah'), [0, 0])
            x[0] += 1; x[1] += J.jenis_keluar(r.get('isyarat_keluar')) in ('henti', 'buka_bawah_henti')
        kerap = sorted(((k, n, h) for k, (n, h) in kk.items() if n >= HENTI_MIN_KELUAR), key=lambda x: (-x[2] / x[1], -x[1]))[:3]
        per_hari = {}
        for r in beli_s:
            per_hari[r['tarikh_beli']] = per_hari.get(r['tarikh_beli'], 0) + 1
        w = dict(
            mula=a, akhir=z, sesi=len(per_hari) or None,
            belian=dict(n=len(beli_s), saham=len({r['saham'] for r in beli_s}), kaedah=len({r.get('kaedah') for r in beli_s}),
                        per_hari=dict(sorted(per_hari.items())), tidak_sah=len(beli) - len(beli_s)),
            keluar=dict(n=len(kel), purata=_pur([_f(r.get('untung_akhir_pct')) for r in kel]),
                        menang=round(100 * sum((_f(r.get('untung_akhir_pct')) or 0) > 0 for r in kel) / len(kel), 1) if kel else None, sebab=sebab),
            keluar_l2=dict(n=len(kel2), purata=_pur([_f(r.get('untung_henti_pct')) for r in kel2])),
            langkau=dict(n=len(lk), sebab=lkk),
            gelinciran=dict(n=len(gap), median=_med([g for g, _ in gap]), p10=_kuantil([g for g, _ in gap], 0.1),
                            p90=_kuantil([g for g, _ in gap], 0.9), jurang_5=len(g5),
                            jurang_5_purata=_pur([hasil(r) for r in g5]), lain_purata=_pur([hasil(r) for r in lain]),
                            tanpa_tutup=len(beli_s) - len(gap)),
            buka_bawah_henti=dict(keluar=len(bbh), purata=_pur([_f(r.get('untung_akhir_pct')) for r in bbh]),
                                  henti_biasa=len(hb_), henti_biasa_purata=_pur([_f(r.get('untung_akhir_pct')) for r in hb_]),
                                  langkau=lkk.get('buka ≤ henti', 0)),
            earnings=dict(posisi=len(le), saham=len({r['saham'] for r, _ in le}), keluar=len(le_kel), keluar_purata=_pur([_f(r.get('untung_akhir_pct')) for r in le_kel]),
                          lain_purata=_pur([_f(r.get('untung_akhir_pct')) for r in tanpa_e]), kalendar=bool(KAL)),
            tidak_sah=dict(dibeli=tsj, ditutup=len(ts_tutup)),
            kerap_henti=[dict(kaedah=k, keluar=n, henti=h) for k, n, h in kerap])
        w['pelajaran'] = pelajaran(w)
        out.append(w)
    return dict(dibina=dibina, sesi=S, minggu=out, takrif=dict(jurang_pct=JURANG, henti_min_keluar=HENTI_MIN_KELUAR),
                definisi='Jurnal mingguan Papertrade C (Isnin–Jumaat): dikira daripada CSV papertrade/claude*.csv, papertrade/langkau, '
                         'stor harga (tutup hari isyarat) dan kalendar earnings gabungan. Gelinciran buka = harga beli (buka) ÷ tutup hari '
                         'isyarat − 1. Pelajaran = peraturan tetap atas nombor minggu itu (bukan pendapat). Rekod sahaja.')


def pelajaran(w):
    """Senarai pelajaran berasaskan peraturan (teks BM ringkas, nombor sebenar) — hanya jika data minggu itu ada."""
    L = []
    k, bh = w['keluar'], w['buka_bawah_henti']
    nh = bh['keluar'] + bh['henti_biasa']
    if bh['keluar'] and nh:
        L.append(dict(tahap='amaran', teks=f"{bh['keluar']} daripada {nh} keluar kena henti ialah buka bawah henti (jurang menembusi henti): "
                      f"purata {_sg(bh['purata'])} berbanding {_sg(bh['henti_biasa_purata'])} bagi kena henti biasa. Harga henti ialah pencetus, bukan harga terjamin."))
    g = w['gelinciran']
    if g['jurang_5'] and g['n']:
        L.append(dict(tahap='amaran', teks=f"{g['jurang_5']} daripada {g['n']} belian ({100 * g['jurang_5'] / g['n']:.1f}%) dibuka > +{JURANG:g}% di atas tutup "
                      f"hari isyarat; untung semasa purata {_sg(g['jurang_5_purata'])} lawan {_sg(g['lain_purata'])} bagi belian lain."))
    if g['n'] and g['median'] is not None:
        L.append(dict(tahap='maklumat', teks=f"Gelinciran buka median {_sg(g['median'])} (p10 {_sg(g['p10'])}, p90 {_sg(g['p90'])}) atas {g['n']} belian."))
    e = w['earnings']
    if e['posisi']:
        t = f"{e['posisi']} posisi ({e['saham']} saham) melintas earnings minggu ini"
        if e['keluar']:
            t += f"; {e['keluar']} sudah keluar dengan purata {_sg(e['keluar_purata'])} lawan {_sg(e['lain_purata'])} bagi keluar lain"
        L.append(dict(tahap='maklumat', teks=t + '.'))
    lk = w['langkau']
    if lk['n']:
        s0 = max(lk['sebab'].items(), key=lambda kv: kv[1]) if lk['sebab'] else None
        L.append(dict(tahap='maklumat', teks=f"{lk['n']} isyarat dilangkau pada belian 9:35 NY" + (f"; sebab utama {s0[0]} ({s0[1]})." if s0 else '.')))
    if k['n'] and k['sebab']:
        j, x = next(iter(k['sebab'].items()))
        L.append(dict(tahap='maklumat', teks=f"{k['n']} keluar lorong kaedah (purata {_sg(k['purata'])}, menang {_fx(k['menang'])}%); terbanyak "
                      f"{x['label']} {x['n']} ({round(100 * x['n'] / k['n'])}%, purata {_sg(x['purata'])})."))
    for x in w['kerap_henti']:
        if x['henti'] and x['henti'] / x['keluar'] >= 0.6:
            L.append(dict(tahap='amaran', teks=f"{x['kaedah']}: {x['henti']} daripada {x['keluar']} keluar minggu ini kena henti."))
    ts = w['tidak_sah']
    if ts['dibeli']:
        L.append(dict(tahap='amaran', teks=f"{sum(ts['dibeli'].values())} posisi dibeli minggu ini tidak sah ("
                      + ', '.join(f"{LABEL_TS.get(a, a)} {n}" for a, n in ts['dibeli'].items()) + '); tidak dikira dalam purata.'))
    return L


def _sg(v):
    return '–' if v is None else f"{'+' if v > 0 else ''}{v:.2f}%"


def _fx(v):
    return '–' if v is None else f'{v:g}'


def main(argv=None):
    ap = argparse.ArgumentParser(description='Jurnal mingguan Papertrade C (jurnal/minggu)')
    ap.add_argument('--folder', default=os.path.join(BS2, 'papertrade'))
    ap.add_argument('--stor', default=os.path.join(BS2, 'data', 'harga', 'stor'))
    ap.add_argument('--minggu', type=int, default=4)
    ap.add_argument('--sesi')
    ap.add_argument('--keluar')
    a = ap.parse_args(argv)
    import jana_db as J
    C = []
    for p in sorted(glob.glob(os.path.join(a.folder, 'claude*.csv')), key=J.nombor_fail):
        C += J.baca_csv(p)
    st = {}
    p = os.path.join(a.folder, 'status_harian.json')
    if os.path.exists(p):
        st = json.load(open(p, encoding='utf-8'))
    lk = J.langkau_beli(a.folder, st)
    tk = J.TERKINI if os.path.abspath(a.stor) == os.path.abspath(J.STOR) else None
    S = a.sesi or (st.get('malam') or {}).get('sesi') or J.sesi_stor()
    d = jurnal(C, lk['rows'], a.stor, tk, S, a.minggu)
    s = json.dumps(d, ensure_ascii=False, indent=1)
    if a.keluar:
        open(a.keluar, 'w', encoding='utf-8').write(s)
    print(s)
    return 0


if __name__ == '__main__':
    sys.exit(main())
