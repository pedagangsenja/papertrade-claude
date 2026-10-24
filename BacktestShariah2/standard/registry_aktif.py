# registry_aktif.py — dokumen db dashboard `registry/aktif` (audit dashboard 24 Okt 2026, item 26): satu dokumen kecil bagi tab
# Backtest yang hanya memuat VARIAN AKTIF (katalog_kaedah.json varian_kod) bagi setiap kaedah M yang didagang, tanpa 32 dokumen
# indikator I dan tanpa varian lain. Halaman memuat dokumen ini di depan; papan penuh `registry/<ID>` dimuat atas permintaan.
# Langkah corong 6–7 diselaraskan dengan Papan Penganalisis (penganalisis.semakan atas sumber yang sama, baca sahaja):
#   s14_atasi_ew  varian sama atasi EW dalam >= 3/4 subset S1–S4 (registry; kestabilan DALAM sampel, subset 431 saham)
#   wfo_lulus     WFO W01: CAGR luar sampel 2023–2026 > EW 423 tempoh sama (WFO/data/hasil; versi ditala dalam tempoh pemilihan)
#   at_lulus      AUTOTUNE A01: CAGR > SPY dalam kumpulan A dan B (2000 saham AS lain, 2013–2024; satu-satunya ujian bebas)
# None = tiada data. Langkah 1–5 kekal daripada gate_gagal registry (G2, G3, G4, G1, G5). Swing = purata pegang backtest 3–30 hari
# (penganalisis.SWING). Data beku: registry set 431 (tarikh_registry) dan AUTOTUNE (tarikh_autotune).
#
#   python3 BacktestShariah2/standard/registry_aktif.py [--out FAIL] [--dibina "YYYY-MM-DD HH:MM MYT"]
#   -> JSON padat (lalai: hanya cetak ringkasan). Tolak sebagai db registry/aktif.
import argparse, json, os, sys
from datetime import datetime, timedelta, timezone

import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import penganalisis as PA  # noqa: E402

HAD_BAIT = 250_000
MEDAN = ['id', 'nama', 'varian', 'keputusan', 'skor', 'cagr', 'mdd', 'win', 'avg', 'days', 'n', 'h1', 'h2', 'gate_gagal', 'swing',
         's14_menang', 's14_n', 's14_atasi_ew', 'wfo_lulus', 'at_lulus', 'at_label', 'tarikh']
BULAT = dict(skor=1, cagr=4, mdd=4, win=4, avg=5, days=1, h1=4, h2=4)


def nombor(v, d):
    x = PA.nombor(v)
    return None if x is None else round(float(x), d)


def baris_431(varian, path=PA.REGISTRY):
    """{id: baris registry set 431 varian aktif} (lajur yang tidak dibaca penganalisis.muat_registry: h1, h2, gate_gagal, tarikh)."""
    r = pd.read_csv(path, dtype={'set': str})
    aktif = pd.Series([varian.get(i) == v for i, v in zip(r['id'], r['varian'])], index=r.index)
    r = r[(r['set'] == '431') & aktif]
    return {x['id']: x for x in r.to_dict('records')}


def dokumen(dibina=None, katalog=PA.KATALOG, registry=PA.REGISTRY, wfo=None, autotune=PA.AUTOTUNE):
    kat = PA.muat_katalog(katalog)
    varian = {i: v for i, _, v in kat}
    REG = PA.muat_registry(varian, registry)
    B = baris_431(varian, registry)
    WF = PA.muat_wfo() if wfo is None else PA.muat_wfo(wfo)
    AT = PA.muat_autotune(autotune)
    rows, tarikh = [], []
    for mid, nama, var in kat:
        r, b = REG.get(mid) or {}, B.get(mid) or {}
        s, w, a = PA.semakan(r, WF.get(mid), AT.get(mid))
        hari = r.get('days')
        o = dict(id=mid, nama=nama, varian=var, keputusan=r.get('keputusan'),
                 **{k: nombor(r.get(k), d) for k, d in BULAT.items() if k not in ('h1', 'h2')},
                 n=r.get('n') if r else None, h1=nombor(b.get('h1'), BULAT['h1']), h2=nombor(b.get('h2'), BULAT['h2']),
                 gate_gagal=b.get('gate_gagal') if isinstance(b.get('gate_gagal'), str) else '',
                 swing=bool(hari is not None and PA.SWING[0] <= hari <= PA.SWING[1]),
                 s14_menang=r.get('subset_menang') if r else None, s14_n=r.get('subset_n') if r else None,
                 s14_atasi_ew=s, wfo_lulus=w, at_lulus=a, at_label=(AT.get(mid) or {}).get('label'),
                 tarikh=b.get('tarikh') if isinstance(b.get('tarikh'), str) else None)
        if o['tarikh']:
            tarikh.append(o['tarikh'])
        rows.append({k: o[k] for k in MEDAN})
    ew = pd.Series([x.get('ew_cagr') for x in B.values()]).dropna()
    at_dijana = None
    if os.path.exists(autotune):
        with open(autotune, encoding='utf-8') as f:
            at_dijana = json.load(f).get('dijana')
    kira = lambda k: sum(1 for x in rows if x[k] is True)   # noqa: E731
    return dict(
        dibina=dibina or datetime.now(timezone(timedelta(hours=8))).strftime('%Y-%m-%d %H:%M MYT'),
        sumber='Varian aktif (standard/katalog_kaedah.json varian_kod) dalam data/registry_M_gabung.csv set 431; semakan luar '
               'sampel ikut standard/penganalisis.py (registry S1–S4, WFO/data/hasil W01, AUTOTUNE/hasil/papan.json A01).',
        nota='Backtest beku (dalam sampel, selepas pemilihan varian), bukan data langsung. Papan penuh semua varian: registry/<ID>.',
        tarikh_registry=max(tarikh) if tarikh else None, tarikh_autotune=at_dijana,
        ew_cagr=round(float(ew.mode().iloc[0]), 4) if len(ew) else None, swing_hari=list(PA.SWING),
        label=getattr(PA, 'LABEL_SEMAKAN', None),
        kiraan=dict(kaedah=len(rows), swing=kira('swing'), s14_atasi_ew=kira('s14_atasi_ew'), wfo_lulus=kira('wfo_lulus'),
                    at_lulus=kira('at_lulus'), tiada_registry=sum(1 for x in rows if x['keputusan'] is None)),
        lajur=MEDAN, rows=rows)


def padat(doc):
    return json.dumps(doc, ensure_ascii=False, separators=(',', ':'), allow_nan=False)


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument('--out')
    ap.add_argument('--dibina')
    a = ap.parse_args(argv)
    doc = dokumen(a.dibina)
    s = padat(doc)
    if len(s.encode()) >= HAD_BAIT:
        raise SystemExit(f'registry/aktif {len(s.encode())} bait >= had {HAD_BAIT}')
    if a.out:
        with open(a.out, 'w', encoding='utf-8') as f:
            f.write(s)
    k = doc['kiraan']
    print(f"registry/aktif: {k['kaedah']} kaedah · swing {k['swing']} · S1–S4 atasi EW {k['s14_atasi_ew']} · WFO {k['wfo_lulus']} · "
          f"AUTOTUNE {k['at_lulus']} · {len(s.encode()):,} bait · registry {doc['tarikh_registry']} · AUTOTUNE {doc['tarikh_autotune']}")


if __name__ == '__main__':
    main()
