# Bina dokumen db dashboard `sektor/snapshot` daripada kekuatan SELURUH pasaran AS (sektor_pasaran.py), gred kumpulan v2
# (data/kumpulan/gred_kumpulan.csv, gred_kumpulan.py) dan pendedahan posisi aktif sah (Paper Trade M, Papertrade C).
#
# Medan SST (audit dashboard 24 Okt 2026, item 28) disalin daripada snapshot lama HANYA jika segar (<= SST_SEGAR sesi sebelum
# tarikh harga); selainnya medan itu dibuang dan tarikh data terakhirnya dilapor:
#   - per kumpulan (rs, sst, volum_relatif, aliran_institusi, aliran_beli, aliran_jual, volum_luar_biasa) -> `sst_tarikh_kumpulan`
#     (--sst-tarikh-kumpulan; jika tiada: snapshot lama; jika tiada: tarikh terakhir nilai itu berubah dalam papertrade/sektor.csv)
#   - peringkat pasaran (institusi_beli, institusi_jual, volum_luar_biasa, A/D naik/turun, adr, atas_sma50/200, rsi,
#     net_tinggi52) -> `sst_tarikh` (--sst-tarikh; jika tiada: snapshot lama; jika tiada: tidak diketahui = tidak segar)
# Rutin yang menarik SST baharu (kemas_kini_0602 langkah 5c) menulis medan itu ke snapshot lama dan memberi tarikh sesinya.
# Senarai saham (teratas, institusi, volum luar biasa): kelas berganda (data/kelas_berganda.csv) dibuang kecuali kelas paling
# cair (median nilai 20 bar stor harga, kod/tidak_layak.py; tiada data stor bagi semua kelas -> kekal yang pertama dalam senarai).
# prestasi_1d tidak lagi ditulis (tiada sumber sejak sektor_pasaran.py; sentiasa kosong).
#
# Guna: python3 snapshot_sektor_db.py --pasaran sektor_pasaran.json --lama snapshot_lama.json \
#           --peta papertrade/peta_industri.csv --papertrade papertrade --dibina "YYYY-MM-DD HH:MM MYT" --out baru.json \
#           [--sst-tarikh YYYY-MM-DD] [--sst-tarikh-kumpulan YYYY-MM-DD] [--kumpulan data/kumpulan/gred_kumpulan.csv] \
#           [--kelas data/kelas_berganda.csv] [--stor data/harga/stor]
import os, sys, csv, glob, json, argparse
from statistics import mean

import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
BS2 = os.path.dirname(HERE)
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(BS2, 'kod'))
from sektor_pasaran import SEKTOR_INDUSTRI  # noqa: E402
import tidak_layak as TL  # noqa: E402

SST_MEDAN = ['rs', 'sst', 'volum_relatif', 'aliran_institusi', 'aliran_beli', 'aliran_jual', 'volum_luar_biasa']
SST_CSV = ['rs', 'volum_relatif', 'aliran_beli', 'aliran_jual', 'aliran_institusi', 'volum_luar_biasa']   # lajur SST sektor.csv
SST_DOC = ['institusi_beli', 'institusi_jual', 'volum_luar_biasa']
SST_PASARAN = ['naik', 'turun', 'adr', 'atas_sma50', 'atas_sma200', 'rsi', 'net_tinggi52']
PASARAN_LAMA = ['r1w', 'r1m', 'r3m']   # median pasaran versi harian_sektor.py (alam 431); diganti median_1w/1m/3m
SST_SEGAR = 2          # sesi pasaran maksimum antara tarikh data SST dan tarikh harga
KUMPULAN = os.path.join(BS2, 'data', 'kumpulan', 'gred_kumpulan.csv')
STOR = os.path.join(BS2, 'data', 'harga', 'stor')


def benar(v):
    return str(v or '').strip().lower() in ('true', '1')


def posisi_aktif(folder):
    out = []
    for f in [os.path.join(folder, 'moomoo.csv')] + sorted(glob.glob(os.path.join(folder, 'claude*.csv'))):
        if not os.path.exists(f):
            continue
        ak = 'm' if f.endswith('moomoo.csv') else 'c'
        with open(f, newline='', encoding='utf-8') as fh:
            baris = list(csv.DictReader(fh))
        for r in baris:
            if benar(r.get('keluar')) or benar(r.get('tidak_sah')) or benar(r.get('tidak_dibeli')):
                continue
            try:
                u = float(r['untung_pct'])
            except (TypeError, ValueError, KeyError):
                continue
            out.append((ak, r['saham'], u))
    return out


def baca_json(path):
    with open(path, encoding='utf-8') as fh:
        return json.load(fh)


def iso(t):
    """'20261023' / '2026-10-23' / None -> '2026-10-23' / None."""
    if not t:
        return None
    s = str(t).strip().replace('-', '')
    return f'{s[:4]}-{s[4:6]}-{s[6:8]}' if len(s) == 8 and s.isdigit() else None


def sesi_antara(dari, hingga):
    """Bilangan sesi NYSE selepas `dari` hingga dan termasuk `hingga` (YYYY-MM-DD). None jika tarikh tiada."""
    if not dari or not hingga:
        return None
    a, b = pd.Timestamp(dari), pd.Timestamp(hingga)
    if a >= b:
        return 0
    try:
        import exchange_calendars as xc
        return int(len(xc.get_calendar('XNYS').sessions_in_range(a + pd.Timedelta(days=1), b)))
    except Exception:  # noqa: BLE001  (tanpa kalendar: hari bekerja)
        return int(np.busday_count((a + pd.Timedelta(days=1)).date(), (b + pd.Timedelta(days=1)).date()))


def segar(tarikh_sst, tarikh_harga):
    n = sesi_antara(tarikh_sst, tarikh_harga)
    return n is not None and n <= SST_SEGAR


def tarikh_sst_csv(path):
    """Tarikh terakhir medan SST per kumpulan dalam papertrade/sektor.csv benar-benar berubah (rutin menyalin nilai lama
    apabila SST tidak ditarik, jadi tarikh baris terakhir bukan tarikh data). None jika fail tiada."""
    if not path or not os.path.exists(path):
        return None
    d = pd.read_csv(path)
    lj = [c for c in SST_CSV if c in d.columns]
    if not len(d) or not lj:
        return None
    akhir, lama = None, None
    for t, g in d.groupby('tarikh', sort=True):
        g = g.drop_duplicates(['jenis', 'nama'], keep='last').set_index(['jenis', 'nama'])[lj]
        if g.notna().any().any():
            if lama is None:
                akhir = t
            else:
                j = g.join(lama, rsuffix='_l', how='inner')
                ubah = any(((j[c] != j[c + '_l']) & ~(j[c].isna() & j[c + '_l'].isna())).any() for c in lj)
                if ubah or not len(j):
                    akhir = t
            lama = g
    return iso(akhir)


def gred_v2(path=KUMPULAN):
    """{(jenis, nama): dict(gred_v2, skor_v2, n_v2, tarikh_v2)} bagi sesi terkini gred_kumpulan.csv."""
    if not path or not os.path.exists(path):
        return {}
    d = pd.read_csv(path)
    if not len(d):
        return {}
    d = d[d.tarikh.astype(str) == str(d.tarikh.astype(str).max())]
    out = {}
    for r in d.itertuples():
        g = r.gred.strip() if isinstance(r.gred, str) else ''
        out[(r.jenis, r.nama)] = dict(gred_v2=g if g in ('A', 'B', 'C', 'D', 'E') else None,   # '–' = tiada gred
                                      skor_v2=None if pd.isna(r.skor) else round(float(r.skor), 1),
                                      n_v2=None if pd.isna(r.n) else int(r.n), tarikh_v2=iso(r.tarikh))
    return out


def nilai_kelas(kump, stor=STOR):
    """{saham: median nilai dagangan 20 bar} bagi saham kelas berganda yang ada dalam stor harga."""
    out = {}
    if not kump:
        return out
    for nm in ('harga_A.csv', 'harga_B.csv'):
        p = os.path.join(stor, nm)
        if not os.path.exists(p):
            continue
        x = pd.read_csv(p, usecols=['ticker', 'date', 'close', 'volume'])
        for t, g in x[x.ticker.isin(set(kump))].groupby('ticker'):
            out[t] = TL.nilai_dagangan(g.sort_values('date'))
    return out


def buang_kelas_berganda(senarai, kump, nilai):
    """Kekalkan satu kelas bagi setiap syarikat kelas berganda dalam senarai [{'saham': ...}, ...]: kelas paling cair (nilai),
    atau yang pertama dalam senarai jika tiada data. Susunan asal dikekalkan."""
    ahli = {}
    for i, x in enumerate(senarai or []):
        k = kump.get(x.get('saham'))
        if k:
            ahli.setdefault(k, []).append((i, x['saham']))
    buang = set()
    for k, v in ahli.items():
        if len(v) < 2:
            continue
        simpan = max(v, key=lambda iv: (nilai.get(iv[1], -1.0), -iv[0]))
        buang |= {i for i, _ in v if i != simpan[0]}
    return [x for i, x in enumerate(senarai or []) if i not in buang]


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument('--pasaran', required=True)
    ap.add_argument('--lama', help='dokumen sektor/snapshot semasa (JSON) untuk medan SST')
    ap.add_argument('--peta', required=True)
    ap.add_argument('--papertrade', required=True)
    ap.add_argument('--dibina', required=True)
    ap.add_argument('--out', required=True)
    ap.add_argument('--sst-tarikh', help='tarikh sesi data SST peringkat pasaran dalam --lama (YYYY-MM-DD), jika baru ditarik')
    ap.add_argument('--sst-tarikh-kumpulan', help='tarikh sesi data SST per kumpulan dalam --lama (YYYY-MM-DD), jika baru ditarik')
    ap.add_argument('--sektor-csv', help='rekod SST per kumpulan (lalai: <papertrade>/sektor.csv)')
    ap.add_argument('--kumpulan', default=KUMPULAN, help='gred kumpulan v2 (gred_kumpulan.csv)')
    ap.add_argument('--kelas', default=TL.KELAS, help='senarai kelas berganda')
    ap.add_argument('--stor', default=STOR, help='stor harga (kecairan kelas berganda)')
    a = ap.parse_args(argv)
    P = baca_json(a.pasaran)
    L = {}
    if a.lama and os.path.exists(a.lama):
        L = baca_json(a.lama)
        L = L.get('data', L)
    tarikh_harga = iso(P['tarikh'])
    sst_kum = iso(a.sst_tarikh_kumpulan) or iso(L.get('sst_tarikh_kumpulan')) or \
        tarikh_sst_csv(a.sektor_csv or os.path.join(a.papertrade, 'sektor.csv'))
    sst_pas = iso(a.sst_tarikh) or iso(L.get('sst_tarikh'))
    kum_segar, pas_segar = segar(sst_kum, tarikh_harga), segar(sst_pas, tarikh_harga)
    lama = {(r.get('jenis'), r.get('nama')): r for r in L.get('rows', [])}
    with open(a.peta, newline='', encoding='utf-8') as fh:
        peta = {r['ticker']: r['industri'] for r in csv.DictReader(fh)}
    gv2 = gred_v2(a.kumpulan)
    kump = TL.kumpulan_kelas(a.kelas)
    nilai = nilai_kelas(kump, a.stor)
    pos = posisi_aktif(a.papertrade)
    kum = {}
    for ak, t, u in pos:
        i = peta.get(t)
        if not i:
            continue
        for key in [('Industri', i), ('Sektor', SEKTOR_INDUSTRI.get(i))]:
            kum.setdefault(key, {'m': [], 'c': []})[ak].append(u)
    rows = []
    for r in P['rows']:
        o = {k: r.get(k) for k in ['jenis', 'nama', 'sektor', 'n', 'prestasi_1w', 'prestasi_1m', 'prestasi_3m', 'breadth',
                                    'rel_1m', 'rel_3m', 'fasa', 'skor_panas']}
        o['n_harga'] = o['n']
        o['mcap'] = (r.get('mcap_bilion') or 0) * 1e9
        o['sampel_kecil'] = (o['n'] or 0) < 5
        o['teratas'] = buang_kelas_berganda(r.get('teratas_senarai') or [], kump, nilai)
        o.update(gv2.get((o['jenis'], o['nama']), dict(gred_v2=None, skor_v2=None, n_v2=None, tarikh_v2=None)))
        if kum_segar:
            x = lama.get((o['jenis'], o['nama'])) or {}
            for k in SST_MEDAN:
                o[k] = x.get(k)
        k = kum.get((o['jenis'], o['nama']), {'m': [], 'c': []})
        o['posisi_m'], o['posisi_c'] = len(k['m']), len(k['c'])
        o['untung_m'] = round(mean(k['m']), 2) if k['m'] else None
        o['untung_c'] = round(mean(k['c']), 2) if k['c'] else None
        al = k['m'] + k['c']
        o['untung_purata_posisi'] = round(mean(al), 2) if al else None
        rows.append(o)
    pas = {k: v for k, v in (L.get('pasaran') or {}).items() if k not in PASARAN_LAMA and (pas_segar or k not in SST_PASARAN)}
    pp = P['pasaran']
    pas.update(n_saham=pp['n'], n_harga=pp['n'], breadth_1m=pp['breadth'], median_1w=round(pp['r1w'], 2),
               median_1m=round(pp['r1m'], 2), median_3m=round(pp['r3m'], 2))
    doc = {k: L[k] for k in ['definisi_fasa'] if k in L}
    if pas_segar:
        doc.update({k: buang_kelas_berganda(L[k], kump, nilai) for k in SST_DOC if k in L})
    tv2 = sorted({x['tarikh_v2'] for x in gv2.values() if x['tarikh_v2']})
    doc.update(rows=rows, pasaran=pas, alam='US penuh', dibina=a.dibina, tarikh_harga=P['tarikh'].replace('-', ''),
               harga_kini='tutup ' + P['tarikh'], sst_tarikh=sst_pas, sst_tarikh_kumpulan=sst_kum,
               sst_segar=dict(pasaran=pas_segar, kumpulan=kum_segar, had_sesi=SST_SEGAR),
               sumber='Seluruh pasaran AS (screener Moomoo, harga >= USD5) + industri Moomoo (peta_industri.csv); '
                      'sektor = 11 sektor Morningstar. Gred kumpulan v2 (gred_v2, skor_v2, n_v2) daripada data/kumpulan/gred_kumpulan.csv'
                      + (f' sesi {tv2[-1]}' if tv2 else '') + '. Aliran institusi, RS, volum relatif, volum luar biasa dan A/D '
                      f'daripada SST Terminal hanya jika data <= {SST_SEGAR} sesi (sst_tarikh, sst_tarikh_kumpulan).',
               pemberat={'prestasi_1m': 0.30, 'prestasi_3m': 0.25, 'prestasi_1w': 0.15, 'breadth': 0.30})
    with open(a.out, 'w', encoding='utf-8') as fh:
        json.dump(doc, fh, ensure_ascii=False, separators=(',', ':'))
    print(f"{len(rows)} baris · {sum(1 for r in rows if r['posisi_m'] or r['posisi_c'])} kumpulan berposisi · "
          f"gred v2 {sum(1 for r in rows if r['gred_v2'])} · SST pasaran {sst_pas or '–'} ({'segar' if pas_segar else 'dibuang'}), "
          f"kumpulan {sst_kum or '–'} ({'segar' if kum_segar else 'dibuang'}) · {os.path.getsize(a.out) // 1024} KB")


if __name__ == '__main__':
    main()
