"""Ujian 1, 3 dan 4 kajian lilin: ciri bar sebagai lapisan VETO atau RANKING atas isyarat kaedah sedia ada
(kolam AUTOTUNE 2000 saham AS). Reka bentuk didaftarkan dahulu dalam
`kajian/research_notes/Ujian lilin atas 2000 saham/veto_ranking.md` (tidak diubah selepas hasil).

Peringkat (setiap satu menulis fail ke DIR supaya boleh disambung selepas mula semula bekas):
  sedia      : muat data AUTOTUNE sekali; simpan matriks tutup Pasaran (2013-01-01 hingga hujung) dan SPY buka/tutup.
  dagangan   : baca lajur kolam yang perlu sahaja; kira lebih_pegang (trade_ret − SPY sepanjang pegangan), sampel,
               ambang (p90/p95 MAX20 atas SELECT; tercil dalam kaedah atas SELECT); simpan kolam ramping.
  ujian      : metrik peringkat dagangan bagi 20 varian × 3 sampel (purata sama-pemberat antara kaedah; t berkelompok
               ikut tarikh isyarat melalui fungsi pengaruh); butiran setiap kaedah.
  portfolio  : pengesahan simulator (rantai tanpa veto = laluan 1; ahli portfolio = pegang8), kemudian portfolio
               8 slot × 12.5% setiap kaedah × kumpulan × varian; keratan lengkung ikut sampel. Checkpoint setiap kaedah.
  laporan    : jadual ringkasan + peraturan lulus -> DIR/vr_jadual.md
  khusus     : t setiap kaedah bagi M167 dan kaedah breakout -> DIR/vr_khusus.md
  plasebo    : diagnostik tambahan (bukan pra-daftar): ranking rawak dan veto rawak -> DIR/vr_plasebo.md

Guna (dari akar repo): python3 BacktestShariah2/kajian/lilin/veto_ranking.py <peringkat> [--dir DIR]
Tiada fail di bawah AUTOTUNE/, BacktestShariah2/kod/, lejar/, papertrade/ atau data/ diubah.
"""
import argparse, json, os, sys, time, warnings
os.environ.setdefault('NUMBA_CACHE_DIR', '/tmp/claude-0/-home-user-papertrade-claude/0793050f-2ee1-522e-9bf0-b633a13089db/scratchpad/numba')
import numpy as np
import pandas as pd
from numba import njit

AKAR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
sys.path.insert(0, os.path.join(AKAR, 'AUTOTUNE', 'teras'))
import enjin_at as E      # noqa: E402
import objektif as OB     # noqa: E402

DIR0 = '/tmp/claude-0/-home-user-papertrade-claude/0793050f-2ee1-522e-9bf0-b633a13089db/scratchpad/lilin'
MULA = pd.Timestamp('2013-01-01')
AKHIR_SEL = pd.Timestamp('2021-12-31')
MULA_22 = pd.Timestamp('2022-01-01')
SAMPEL = ['SELECT', 'VALIDATE-B', 'VALIDATE-2022']
N_MIN = 20
BREAKOUT = ['M04', 'M30', 'M33', 'M79', 'M135']
LAJUR = ['method', 'ticker', 'signal_date', 'entry_date', 'kumpulan', 'pos', 'laluan', 'trade_ret', 'hold_days',
         'rank_value', 'pegang8', 'exit_date', 'exit_reason', 'dagangan_enjin', 'ikut_laluan',
         'atas1pct_1t', 'max20', 'gap_atr', 'rcc_srs60', 'id_share20', 'id_share60', 'rs12_pct',
         'hijau_vol90', 'vol_pctl50', 'h52', 'h52_industri', 'fwd20', 'spy20']

# Varian (pra-daftar). jenis: veto (cell a = disimpan, b = diveto) | terc (a = tercil atas, b = bawah; arah -1 =
# RENDAH dahulu -> a/b ditukar) | bendera (a = 1, b = 0). rs=True: dalam tercil RS (rs12_pct).
VARIAN = [
    dict(id='V1', uji=1, jenis='veto', nama='veto atas1pct_1t == 1'),
    dict(id='V2', uji=1, jenis='veto', nama='veto max20 >= p90 (SELECT)'),
    dict(id='V3', uji=1, jenis='veto', nama='veto max20 >= p95 (SELECT)'),
    dict(id='V4', uji=1, jenis='veto', nama='veto gap_atr >= 1'),
    dict(id='V5', uji=1, jenis='veto', nama='veto gap_atr >= 2'),
    dict(id='V6', uji=1, jenis='veto', nama='veto rcc_srs60 > 3'),
    dict(id='R1', uji=3, jenis='terc', ciri='id_share20', arah=1, rs=False, nama='id_share20 TINGGI dahulu'),
    dict(id='R2', uji=3, jenis='terc', ciri='id_share20', arah=-1, rs=False, nama='id_share20 RENDAH dahulu'),
    dict(id='R3', uji=3, jenis='terc', ciri='id_share60', arah=1, rs=False, nama='id_share60 TINGGI dahulu'),
    dict(id='R4', uji=3, jenis='terc', ciri='id_share60', arah=-1, rs=False, nama='id_share60 RENDAH dahulu'),
    dict(id='R5', uji=3, jenis='terc', ciri='id_share20', arah=None, rs=True, ikut='R1', nama='id_share20 dalam tercil RS'),
    dict(id='R6', uji=3, jenis='terc', ciri='id_share60', arah=None, rs=True, ikut='R3', nama='id_share60 dalam tercil RS'),
    dict(id='B1', uji=4, jenis='bendera', ciri='hijau_vol90', rs=False, nama='bonus hijau_vol90'),
    dict(id='B2', uji=4, jenis='terc', ciri='vol_pctl50', arah=1, rs=False, nama='vol_pctl50 TINGGI dahulu'),
    dict(id='B3', uji=4, jenis='terc', ciri='h52', arah=1, rs=False, nama='h52 TINGGI dahulu'),
    dict(id='B4', uji=4, jenis='bendera', ciri='h52_095', rs=False, nama='bonus h52 >= 0.95'),
    dict(id='B5', uji=4, jenis='terc', ciri='h52_industri', arah=1, rs=False, nama='h52_industri TINGGI dahulu'),
    dict(id='B6', uji=4, jenis='terc', ciri='h52', arah=1, rs=True, nama='h52 dalam tercil RS'),
    dict(id='B7', uji=4, jenis='terc', ciri='h52_industri', arah=1, rs=True, nama='h52_industri dalam tercil RS'),
    dict(id='B8', uji=4, jenis='bendera', ciri='hijau_vol90', rs=True, nama='hijau_vol90 dalam tercil RS'),
]
VID = {v['id']: v for v in VARIAN}


def p(dir_, f): return os.path.join(dir_, f)


def simpan_json(o, f):
    tmp = f + '.tmp'
    json.dump(o, open(tmp, 'w'), indent=1, default=float)
    os.replace(tmp, f)


# ------------------------------------------------------------------ peringkat sedia
def sedia(dir_):
    import data as D
    t0 = time.time()
    fr, idx, univ = D.muat('2011-01-01', '2100-01-01', 'AB', dir=os.path.join(AKAR, 'AUTOTUNE', '.cache'))
    pas = E.Pasaran(fr, MULA, None)
    np.savez(p(dir_, 'vr_pasaran.npz'), A=pas.A, tarikh=pas.tarikh.values, nama=np.array(list(pas.kod), object))
    spy = idx['SPY'][['open', 'close']].copy()
    spy.to_parquet(p(dir_, 'vr_spy.parquet'))
    print('sedia', pas.A.shape, round(time.time() - t0), 's', flush=True)


def muat_pasaran(dir_):
    z = np.load(p(dir_, 'vr_pasaran.npz'), allow_pickle=True)
    pas = E.Pasaran.__new__(E.Pasaran)
    pas.mula = MULA; pas.akhir = None
    pas.tarikh = pd.DatetimeIndex(z['tarikh'])
    pas.kod = {t: q for q, t in enumerate(z['nama'])}
    pas.A = z['A']
    pas.pos = pd.Series(np.arange(len(pas.tarikh)), pas.tarikh)
    return pas


# ------------------------------------------------------------------ peringkat dagangan
def tercil_kaedah(df, ciri, kunci):
    """Sempadan tercil (q1/3, q2/3) atas sampel SELECT dagangan laluan 1 bagi setiap kunci (kaedah[, tercil RS])."""
    s = df[df.sampel.eq('SELECT') & df.l1]
    q = s.groupby(kunci)[ciri].quantile([1 / 3, 2 / 3]).unstack()
    q.columns = ['q1', 'q2']
    return q


def dagangan(dir_):
    t0 = time.time()
    P = pd.read_parquet(p(dir_, 'kolam.parquet'), columns=LAJUR)
    for c in ('method', 'ticker', 'kumpulan', 'exit_reason'):
        P[c] = P[c].astype('category')
    spy = pd.read_parquet(p(dir_, 'vr_spy.parquet'))
    so = spy['open']; sc = spy['close']
    ent = P.entry_date.values; ex = P.exit_date.values
    s_ent = so.reindex(ent).values
    keluar_buka = (P.exit_reason == 'isyarat keluar').values
    s_ex = np.where(keluar_buka, so.reindex(ex).values, sc.reindex(ex).values)
    spy_hold = s_ex / s_ent - 1
    P['spy_pegang'] = spy_hold.astype(np.float32)
    P['lebih_pegang'] = (P.trade_ret - spy_hold).astype(np.float32)
    P['lebih20'] = (P.fwd20 - P.spy20).astype(np.float32)
    ada = P.trade_ret.notna()
    tiada_spy = int((ada & P.spy_pegang.isna()).sum())
    sd = P.signal_date
    P['sampel'] = np.where(sd >= MULA_22, 'VALIDATE-2022',
                           np.where(P.kumpulan.astype(str) == 'A', 'SELECT', 'VALIDATE-B'))
    P['sampel'] = P.sampel.astype('category')
    P['l1'] = P.dagangan_enjin & ada
    P['rs_t'] = np.where(P.rs12_pct.isna(), -1, np.where(P.rs12_pct < 1 / 3, 0, np.where(P.rs12_pct < 2 / 3, 1, 2))
                         ).astype(np.int8)
    P['h52_095'] = (P.h52 >= 0.95).astype(np.float32).where(P.h52.notna())
    # ambang MAX20 atas baris unik ticker x tarikh isyarat SELECT (semua isyarat)
    u = P.loc[P.sampel.eq('SELECT'), ['ticker', 'signal_date', 'max20']].drop_duplicates(['ticker', 'signal_date'])
    p90, p95 = float(u.max20.quantile(0.90)), float(u.max20.quantile(0.95))
    # bendera veto (NaN ciri -> tidak diveto)
    P['veto_V1'] = P.atas1pct_1t.eq(1)
    P['veto_V2'] = P.max20 >= p90
    P['veto_V3'] = P.max20 >= p95
    P['veto_V4'] = P.gap_atr >= 1
    P['veto_V5'] = P.gap_atr >= 2
    P['veto_V6'] = P.rcc_srs60 > 3
    # tercil dalam kaedah (dan dalam kaedah x tercil RS) atas SELECT
    sempadan = {}
    for ciri in ('id_share20', 'id_share60', 'vol_pctl50', 'h52', 'h52_industri'):
        for rs in (False, True):
            kunci = ['method', 'rs_t'] if rs else ['method']
            q = tercil_kaedah(P, ciri, kunci)
            nm = f'terc_{ciri}_{"rs" if rs else "k"}'
            m = P[kunci].merge(q, left_on=kunci, right_index=True, how='left')
            x = P[ciri].values
            sah = (m.q1 < m.q2).values
            t = np.full(len(P), -1, np.int8)
            t[sah & (x <= m.q1.values)] = 0
            t[sah & (x >= m.q2.values)] = 2
            t[sah & (x > m.q1.values) & (x < m.q2.values)] = 1
            P[nm] = t
            sempadan[nm] = q.reset_index().to_dict('records')
    P.to_parquet(p(dir_, 'vr_kolam.parquet'), index=False)
    info = dict(baris=len(P), dagangan_l1=int(P.l1.sum()), tiada_spy=tiada_spy, max20_p90=p90, max20_p95=p95,
                baris_unik_select=len(u), saat=round(time.time() - t0),
                veto_bahagian_l1={f'V{i}': float(P.loc[P.l1, f'veto_V{i}'].mean()) for i in range(1, 7)})
    simpan_json(info, p(dir_, 'vr_dagangan_info.json'))
    simpan_json(sempadan, p(dir_, 'vr_sempadan_tercil.json'))
    print(json.dumps(info), flush=True)


# ------------------------------------------------------------------ peringkat ujian (peringkat dagangan)
def sisi(df, v, arah_rs=None):
    """Pulang (sisi, strata): sisi 1 = a (disimpan/atas), 0 = b (diveto/bawah), -1 = tiada; strata = kaedah atau
    kaedah x tercil RS."""
    j = v['jenis']
    s = np.full(len(df), -1, np.int8)
    if j == 'veto':
        vt = df[f'veto_{v["id"]}'].values
        s[:] = np.where(vt, 0, 1)
    elif j == 'terc':
        t = df[f'terc_{v["ciri"]}_{"rs" if v["rs"] else "k"}'].values
        arah = v['arah'] if v['arah'] is not None else arah_rs
        atas, bawah = (2, 0) if arah > 0 else (0, 2)
        s[t == atas] = 1; s[t == bawah] = 0
    else:
        x = df[v['ciri']].values
        s[x == 1] = 1; s[x == 0] = 0
    if v.get('rs'):
        s[df.rs_t.values < 0] = -1
        strata = df.method.astype(str).values + '|' + df.rs_t.astype(str).values
    else:
        strata = df.method.astype(str).values
    return s, strata


def anggar(x, s, strata, kaedah, tarikh, min_n=N_MIN):
    """Purata sama-pemberat antara kaedah bagi (min a − min b) dalam strata; strata layak jika n_a, n_b >= min_n;
    kaedah = purata strata layaknya. SE berkelompok ikut tarikh isyarat melalui fungsi pengaruh."""
    ok = (s >= 0) & np.isfinite(x)
    d = pd.DataFrame(dict(x=x[ok], s=s[ok], st=strata[ok], k=kaedah[ok], g=tarikh[ok]))
    agg = d.groupby(['st', 's'], observed=True).x.agg(['mean', 'size']).unstack('s')
    if agg.shape[1] < 4: return None
    agg.columns = [f'{a}{b}' for a, b in agg.columns]
    agg = agg[(agg.get('size1', 0) >= min_n) & (agg.get('size0', 0) >= min_n)]
    if agg.empty: return None
    km = pd.Series([i.split('|')[0] for i in agg.index], index=agg.index)
    J = km.map(km.value_counts()); K = km.nunique()
    w = 1.0 / (J * K)
    beza = (agg.mean1 - agg.mean0)
    D = float((w * beza).sum())
    per_k = beza.groupby(km).mean()
    d = d[d.st.isin(agg.index)]
    mu = np.where(d.s.values == 1, agg.mean1.reindex(d.st).values, agg.mean0.reindex(d.st).values)
    nn = np.where(d.s.values == 1, agg.size1.reindex(d.st).values, agg.size0.reindex(d.st).values)
    sg = np.where(d.s.values == 1, 1.0, -1.0)
    inf = sg * w.reindex(d.st).values * (d.x.values - mu) / nn
    S = pd.Series(inf).groupby(d.g.values).sum().values
    G = len(S)
    se = float(np.sqrt(G / (G - 1) * (S ** 2).sum())) if G > 1 else np.nan
    return dict(D=D, se=se, t=D / se if se and se > 0 else np.nan, K=int(K), strata=agg.index.tolist(),
                per_k=per_k.to_dict(), G=G)


def ujian(dir_):
    t0 = time.time()
    P = pd.read_parquet(p(dir_, 'vr_kolam.parquet'))
    hasil_f = p(dir_, 'vr_ujian.json')
    H = json.load(open(hasil_f)) if os.path.exists(hasil_f) else {}
    L1 = P[P.l1].reset_index(drop=True)
    SEMUA = P[P.trade_ret.notna()].reset_index(drop=True)
    del P
    for v in VARIAN:
        if v['id'] in H: continue
        arah_rs = None
        if v.get('ikut'):
            arah_rs = 1 if H[v['ikut']]['SELECT']['lebih_pegang']['D'] > 0 else -1
        out = dict(arah_rs=arah_rs)
        for nm in SAMPEL:
            df = L1[L1.sampel.eq(nm)]
            s, st = sisi(df, v, arah_rs)
            km = df.method.astype(str).values; g = df.signal_date.values
            r = dict(n_a=int((s == 1).sum()), n_b=int((s == 0).sum()), n=len(df))
            for met, x in (('lebih_pegang', df.lebih_pegang.values.astype(float)),
                           ('lebih20', df.lebih20.values.astype(float)),
                           ('menang', (df.trade_ret.values > 0).astype(float)),
                           ('trade_ret', df.trade_ret.values.astype(float))):
                a = anggar(x, s, st, km, g)
                if a is None: r[met] = None; continue
                if met != 'lebih_pegang': a.pop('per_k'); a.pop('strata')
                r[met] = a
            lp = r['lebih_pegang']
            if lp is not None:
                strata = set(lp['strata']); ks = sorted(lp['per_k'])
                dalam = np.isin(st, list(strata))
                # 5% terburuk: set a (union strata layak) lawan semua dagangan kaedah itu dalam sampel
                p5a, p5b, p5s, ma, mb = [], [], [], [], []
                for k in ks:
                    mk = km == k
                    xa = df.trade_ret.values[mk & dalam & (s == 1)]
                    xb = df.trade_ret.values[mk & dalam & (s == 0)]
                    xs = df.trade_ret.values[mk]
                    p5a.append(np.percentile(xa, 5)); p5b.append(np.percentile(xb, 5)); p5s.append(np.percentile(xs, 5))
                    ma.append(df.lebih_pegang.values[mk & dalam & (s == 1)].mean())
                    mb.append(df.lebih_pegang.values[mk & dalam & (s == 0)].mean())
                r['p5_a'] = float(np.mean(p5a)); r['p5_b'] = float(np.mean(p5b)); r['p5_semua'] = float(np.mean(p5s))
                r['min_a'] = float(np.mean(ma)); r['min_b'] = float(np.mean(mb))
                r['hari_a'] = int(pd.unique(df.entry_date.values[dalam & (s == 1)]).size)
                r['hari_b'] = int(pd.unique(df.entry_date.values[dalam & (s == 0)]).size)
                r['hari_min_strata'] = int(min(
                    pd.unique(df.entry_date.values[(st == q) & (s == z)]).size for q in strata for z in (0, 1)))
                # butiran kaedah terpilih
                r['kaedah'] = {k: dict(beza=float(lp['per_k'][k]),
                                       n_a=int(((km == k) & dalam & (s == 1)).sum()),
                                       n_b=int(((km == k) & dalam & (s == 0)).sum()),
                                       bahagian_b=float(((km == k) & (s == 0)).sum() / max(1, (km == k).sum())))
                               for k in ks}
            # kepekaan: semua isyarat dengan trade_ret (metrik utama sahaja)
            dS = SEMUA[SEMUA.sampel.eq(nm)]
            s2, st2 = sisi(dS, v, arah_rs)
            a2 = anggar(dS.lebih_pegang.values.astype(float), s2, st2, dS.method.astype(str).values,
                        dS.signal_date.values)
            r['semua_isyarat'] = None if a2 is None else dict(D=a2['D'], t=a2['t'], K=a2['K'])
            out[nm] = r
        H[v['id']] = out
        simpan_json(H, hasil_f)
        print(v['id'], {nm: (round(out[nm]['lebih_pegang']['D'] * 100, 3), round(out[nm]['lebih_pegang']['t'], 2))
                        if out[nm].get('lebih_pegang') else None for nm in SAMPEL}, round(time.time() - t0), 's',
              flush=True)


# ------------------------------------------------------------------ peringkat portfolio
@njit(cache=True)
def _rantai(kod_t, sd, ed, ok):
    """Rantai isyarat setiap ticker (disusun ikut ticker, tarikh isyarat): isyarat diambil jika ok dan tarikh
    isyarat > tarikh keluar dagangan sebelumnya (peraturan enjin_at._trades: i = j + 1)."""
    n = len(kod_t); ambil = np.zeros(n, np.bool_)
    prev = -1; last = np.int64(-9223372036854775807)
    for r in range(n):
        if kod_t[r] != prev:
            prev = kod_t[r]; last = np.int64(-9223372036854775807)
        if ok[r] and sd[r] > last:
            ambil[r] = True; last = ed[r]
    return ambil


def keratan(cv, a, b):
    """Metrik keratan lengkung [a, b] dinormalkan pada ekuiti hari sebelum a (1.0 jika tiada)."""
    sebelum = cv[cv.index < a]
    asas = float(sebelum.iloc[-1]) if len(sebelum) else 1.0
    k = cv[(cv.index >= a) & (cv.index <= b)] / asas
    return OB.cagr(k), OB.mdd(k)


def metrik_lengkung(cv):
    s1 = keratan(cv, MULA, AKHIR_SEL)
    s2 = keratan(cv, MULA_22, pd.Timestamp('2100-01-01'))
    return dict(cagr_1321=s1[0], mdd_1321=s1[1], cagr_22=s2[0], mdd_22=s2[1], cagr_penuh=OB.cagr(cv),
                mdd_penuh=OB.mdd(cv))


def kunci_rank(T, v, arah_rs, kawalan=False):
    """Susun semula calon setiap hari masuk ikut kunci varian; pulang T dengan rank = −kedudukan."""
    T = T.copy()
    neg = lambda s: -s
    if kawalan:
        keys = [T.rs_t.where(T.rs_t >= 0), T.rank_value]
    elif v['jenis'] == 'terc':
        arah = v['arah'] if v['arah'] is not None else arah_rs
        f = T[v['ciri']].astype(float) * arah
        keys = ([T.rs_t.where(T.rs_t >= 0)] if v['rs'] else []) + [f, T.rank_value]
    else:  # bendera
        keys = ([T.rs_t.where(T.rs_t >= 0)] if v['rs'] else []) + [T[v['ciri']].astype(float), T.rank_value]
    K = pd.DataFrame({f'k{i}': k.values for i, k in enumerate(keys)}, index=T.index)
    K['ent'] = T.ent.values
    K = K.sort_values(['ent'] + [f'k{i}' for i in range(len(keys))], ascending=[True] + [False] * len(keys),
                      na_position='last', kind='mergesort')
    T = T.loc[K.index]
    T['rank'] = -np.arange(len(T), dtype=float)
    return T


def portfolio(dir_, hanya=None):
    t0 = time.time()
    pas = muat_pasaran(dir_)
    H = json.load(open(p(dir_, 'vr_ujian.json')))
    arah_rs = {'R5': H['R5']['arah_rs'], 'R6': H['R6']['arah_rs']}
    lajur = ['method', 'ticker', 'signal_date', 'entry_date', 'exit_date', 'kumpulan', 'pos', 'laluan', 'trade_ret',
             'rank_value', 'pegang8', 'l1', 'rs_t', 'id_share20', 'id_share60', 'hijau_vol90', 'vol_pctl50', 'h52',
             'h52_095', 'h52_industri'] + [f'veto_V{i}' for i in range(1, 7)]
    P = pd.read_parquet(p(dir_, 'vr_kolam.parquet'), columns=lajur)
    P = P[P.trade_ret.notna()]
    os.makedirs(p(dir_, 'vr_port'), exist_ok=True)
    sah_f = p(dir_, 'vr_sah.json')
    SAH = json.load(open(sah_f)) if os.path.exists(sah_f) else {}
    for mid, Pm in P.groupby('method', observed=True):
        if hanya and mid not in hanya: continue
        f_out = p(dir_, f'vr_port/{mid}.json')
        if os.path.exists(f_out): continue
        Pm = Pm.sort_values(['ticker', 'signal_date', 'pos']).reset_index(drop=True)
        kod_t = Pm.ticker.cat.codes.values.astype(np.int64)
        sd = Pm.signal_date.values.astype(np.int64); ed = Pm.exit_date.values.astype(np.int64)
        T_all = Pm.rename(columns={'entry_date': 'ent', 'exit_date': 'ex', 'trade_ret': 'ret'})
        T_all['ticker'] = T_all.ticker.astype(str)
        res = {}
        # --- pengesahan
        ambil0 = _rantai(kod_t, sd, ed, np.ones(len(Pm), np.bool_))
        rantai_sama = bool(np.array_equal(ambil0, Pm.l1.values))
        sah = dict(rantai_sama_laluan1=rantai_sama)
        for g in ('A', 'B'):
            T = T_all[(T_all.l1) & (T_all.kumpulan.astype(str) == g)].sort_values('pos')
            T = T.assign(rank=T.rank_value)
            cv, dp = pas.lengkung(T[['ticker', 'ent', 'ex', 'ret', 'rank']], pegang=True)
            pg = set(T.index[T.pegang8.values]); dp_i = set(dp.index)
            sah[f'pegang8_sama_{g}'] = pg == dp_i
            sah[f'pegang8_beza_{g}'] = len(pg ^ dp_i)
            res[('ASAS', g)] = metrik_lengkung(cv)
            # rantai dibina semula tanpa veto -> lengkung mesti sama
            Tc = T_all[ambil0 & (T_all.kumpulan.astype(str) == g).values].sort_values('pos')
            cv2 = pas.lengkung(Tc.assign(rank=Tc.rank_value)[['ticker', 'ent', 'ex', 'ret', 'rank']])
            sah[f'cagr_beza_maks_{g}'] = float(np.nanmax(np.abs(cv2.values - cv.values)))
        SAH[mid] = sah
        simpan_json(SAH, sah_f)
        if not (rantai_sama and sah['pegang8_sama_A'] and sah['pegang8_sama_B']):
            print(mid, 'PENGESAHAN GAGAL', sah, flush=True)
        # --- veto: rantai dibina semula tanpa isyarat diveto
        for i in range(1, 7):
            ok = ~Pm[f'veto_V{i}'].values
            ambil = _rantai(kod_t, sd, ed, ok)
            for g in ('A', 'B'):
                Tc = T_all[ambil & (T_all.kumpulan.astype(str) == g).values].sort_values('pos')
                cv = pas.lengkung(Tc.assign(rank=Tc.rank_value)[['ticker', 'ent', 'ex', 'ret', 'rank']])
                res[(f'V{i}', g)] = metrik_lengkung(cv)
        # --- ranking: rantai laluan 1 tetap, kunci susunan baharu
        for g in ('A', 'B'):
            T = T_all[(T_all.l1) & (T_all.kumpulan.astype(str) == g)].sort_values('pos')
            Tk = kunci_rank(T, None, None, kawalan=True)
            res[('KAWALAN_RS', g)] = metrik_lengkung(pas.lengkung(Tk[['ticker', 'ent', 'ex', 'ret', 'rank']]))
            for v in VARIAN:
                if v['jenis'] == 'veto': continue
                Tk = kunci_rank(T, v, arah_rs.get(v['id']))
                res[(v['id'], g)] = metrik_lengkung(pas.lengkung(Tk[['ticker', 'ent', 'ex', 'ret', 'rank']]))
        simpan_json({f'{a}|{b}': m for (a, b), m in res.items()}, f_out)
        print(mid, 'siap', sah, round(time.time() - t0), 's', flush=True)


# ------------------------------------------------------------------ peringkat laporan
def laporan(dir_):
    H = json.load(open(p(dir_, 'vr_ujian.json')))
    SAH = json.load(open(p(dir_, 'vr_sah.json')))
    info = json.load(open(p(dir_, 'vr_dagangan_info.json')))
    PT = {}
    for f in sorted(os.listdir(p(dir_, 'vr_port'))):
        PT[f[:-5]] = json.load(open(os.path.join(dir_, 'vr_port', f)))
    kaedah = sorted(PT)
    baris = []
    out = ['# Jadual veto/ranking (dijana `veto_ranking.py laporan`)', '',
           f'max20 p90 = {info["max20_p90"]:.4f}, p95 = {info["max20_p95"]:.4f} (baris unik SELECT {info["baris_unik_select"]:,}); '
           f'dagangan laluan 1 = {info["dagangan_l1"]:,}; tanpa SPY = {info["tiada_spy"]}.', '',
           '## Pengesahan simulator', '',
           '| Kaedah | rantai = laluan 1 | pegang8 A sama (beza) | pegang8 B sama (beza) | maks |Δ ekuiti| A | B |',
           '|---|---|---|---|---|---|']
    for k in kaedah:
        s = SAH[k]
        out.append(f'| {k} | {s["rantai_sama_laluan1"]} | {s["pegang8_sama_A"]} ({s["pegang8_beza_A"]}) | '
                   f'{s["pegang8_sama_B"]} ({s["pegang8_beza_B"]}) | {s["cagr_beza_maks_A"]:.2e} | {s["cagr_beza_maks_B"]:.2e} |')
    # portfolio delta
    def delta(vid, rujukan):
        d = {}
        for k in kaedah:
            a = PT[k][f'{vid}|A']; b = PT[k][f'{vid}|B']; ra = PT[k][f'{rujukan}|A']; rb = PT[k][f'{rujukan}|B']
            d[k] = dict(
                SELECT=(a['cagr_1321'] - ra['cagr_1321'], a['mdd_1321'] - ra['mdd_1321']),
                **{'VALIDATE-B': (b['cagr_1321'] - rb['cagr_1321'], b['mdd_1321'] - rb['mdd_1321'])},
                **{'VALIDATE-2022': ((a['cagr_22'] - ra['cagr_22'] + b['cagr_22'] - rb['cagr_22']) / 2,
                                     (a['mdd_22'] - ra['mdd_22'] + b['mdd_22'] - rb['mdd_22']) / 2)})
        return d
    pf = {}
    for v in VARIAN:
        refs = ['ASAS'] + (['KAWALAN_RS'] if v.get('rs') else [])
        pf[v['id']] = {r: delta(v['id'], r) for r in refs}
    out += ['', '## Peringkat dagangan (lebih_pegang; purata sama-pemberat kaedah; beza a − b dalam mata peratus)', '',
            '| Varian | Sampel | K | n a | n b | min a | min b | beza | t | beza lebih20 | beza menang | p5 a | p5 semua | p5 b | hari a | hari b | hari min strata | semua isyarat beza (t) |',
            '|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|']
    keputusan = {}
    for v in VARIAN:
        h = H[v['id']]
        syarat = dict(i=True, ii=False, iii=True, iv=True, v=True)
        for nm in SAMPEL:
            r = h[nm]; lp = r.get('lebih_pegang')
            if lp is None:
                out.append(f'| {v["id"]} | {nm} | – | {r["n_a"]} | {r["n_b"]} | tiada sel layak |||||||||||||')
                syarat['i'] = False; syarat['iii'] = False
                continue
            l20 = r['lebih20']; mn = r['menang']; sa = r['semua_isyarat']
            out.append(
                f'| {v["id"]} | {nm} | {lp["K"]} | {r["n_a"]:,} | {r["n_b"]:,} | {r["min_a"]*100:.2f} | {r["min_b"]*100:.2f} | '
                f'{lp["D"]*100:+.2f} | {lp["t"]:.2f} | {(l20["D"]*100 if l20 else float("nan")):+.2f} | '
                f'{(mn["D"]*100 if mn else float("nan")):+.1f} | {r["p5_a"]*100:.2f} | {r["p5_semua"]*100:.2f} | '
                f'{r["p5_b"]*100:.2f} | {r["hari_a"]} | {r["hari_b"]} | {r["hari_min_strata"]} | '
                f'{(sa["D"]*100 if sa else float("nan")):+.2f} ({(sa["t"] if sa else float("nan")):.1f}) |')
            if lp['D'] <= 0: syarat['i'] = False
            if nm == 'SELECT' and lp['t'] > 3: syarat['ii'] = True
            if min(r['hari_a'], r['hari_b']) < 10: syarat['iii'] = False
            if r['p5_a'] - r['p5_semua'] < -0.01: syarat['iv'] = False
        rj = 'KAWALAN_RS' if v.get('rs') else 'ASAS'
        for nm in SAMPEL:
            n_baik = sum(1 for k in kaedah if pf[v['id']][rj][k][nm][0] > 0)
            if not n_baik > len(kaedah) / 2: syarat['v'] = False
        keputusan[v['id']] = syarat
    out += ['', '## Portfolio 8 slot (Δ berbanding garis dasar; Δ VALIDATE-2022 = purata ΔA dan ΔB)', '',
            '| Varian | Rujukan | Sampel | median ΔCAGR (mata) | median ΔMDD (mata) | kaedah CAGR naik / turun / sama | MDD lebih baik |',
            '|---|---|---|---|---|---|---|']
    for v in VARIAN:
        for rj, d in pf[v['id']].items():
            for nm in SAMPEL:
                dc = np.array([d[k][nm][0] for k in kaedah]); dm = np.array([d[k][nm][1] for k in kaedah])
                out.append(f'| {v["id"]} | {rj} | {nm} | {np.median(dc)*100:+.2f} | {np.median(dm)*100:+.2f} | '
                           f'{(dc > 0).sum()} / {(dc < 0).sum()} / {(dc == 0).sum()} | {(dm > 0).sum()} |')
    # kawalan RS lawan asas
    out += ['', '## Kawalan RS (tercil RS dahulu, kemudian rank_value) lawan garis dasar', '',
            '| Sampel | median ΔCAGR | median ΔMDD | naik / turun |', '|---|---|---|---|']
    dk = delta('KAWALAN_RS', 'ASAS')
    for nm in SAMPEL:
        dc = np.array([dk[k][nm][0] for k in kaedah]); dm = np.array([dk[k][nm][1] for k in kaedah])
        out.append(f'| {nm} | {np.median(dc)*100:+.2f} | {np.median(dm)*100:+.2f} | {(dc > 0).sum()} / {(dc < 0).sum()} |')
    out += ['', '## Peraturan lulus', '', '| Varian | Nama | (i) beza > 0 ketiga-tiga | (ii) t > 3 SELECT | (iii) ≥ 10 hari | (iv) p5 | (v) majoriti portfolio | KEPUTUSAN |',
            '|---|---|---|---|---|---|---|---|']
    for v in VARIAN:
        s = keputusan[v['id']]
        lulus = all(s.values())
        nama = v['nama'] + (f' (arah {"TINGGI" if H[v["id"]]["arah_rs"] > 0 else "RENDAH"})' if v.get('ikut') else '')
        out.append(f'| {v["id"]} | {nama} | {s["i"]} | {s["ii"]} | {s["iii"]} | {s["iv"]} | {s["v"]} | '
                   f'{"LULUS" if lulus else "GAGAL"} |')
    # kaedah khusus
    out += ['', '## M167 dan kaedah breakout (beza lebih_pegang a − b, mata; ΔCAGR portfolio, mata)', '',
            '| Varian | Kaedah | beza SELECT | beza V-B | beza V-2022 | bahagian b SELECT | ΔCAGR SELECT | ΔCAGR V-B | ΔCAGR V-2022 |',
            '|---|---|---|---|---|---|---|---|---|']
    for v in VARIAN:
        rj = 'KAWALAN_RS' if v.get('rs') else 'ASAS'
        for k in ['M167'] + BREAKOUT:
            bz = []
            for nm in SAMPEL:
                kk = (H[v['id']][nm].get('kaedah') or {}).get(k)
                bz.append(f'{kk["beza"]*100:+.2f}' if kk else '–')
            kk = (H[v['id']]['SELECT'].get('kaedah') or {}).get(k)
            bb = f'{kk["bahagian_b"]*100:.0f}%' if kk else '–'
            dc = [f'{pf[v["id"]][rj][k][nm][0]*100:+.2f}' for nm in SAMPEL]
            out.append(f'| {v["id"]} | {k} | {bz[0]} | {bz[1]} | {bz[2]} | {bb} | {dc[0]} | {dc[1]} | {dc[2]} |')
    # garis dasar portfolio
    out += ['', '## Garis dasar portfolio setiap kaedah (CAGR / MDD, %)', '',
            '| Kaedah | A 2013–21 | B 2013–21 | A 2022+ | B 2022+ |', '|---|---|---|---|---|']
    for k in kaedah:
        a = PT[k]['ASAS|A']; b = PT[k]['ASAS|B']
        out.append(f'| {k} | {a["cagr_1321"]*100:.1f} / {a["mdd_1321"]*100:.1f} | {b["cagr_1321"]*100:.1f} / {b["mdd_1321"]*100:.1f} | '
                   f'{a["cagr_22"]*100:.1f} / {a["mdd_22"]*100:.1f} | {b["cagr_22"]*100:.1f} / {b["mdd_22"]*100:.1f} |')
    open(p(dir_, 'vr_jadual.md'), 'w').write('\n'.join(out) + '\n')
    simpan_json(dict(keputusan=keputusan, portfolio_delta=pf), p(dir_, 'vr_ringkas.json'))
    print('\n'.join(out))


# ------------------------------------------------------------------ peringkat khusus (M167 + breakout, t setiap kaedah)
def khusus(dir_):
    """t berkelompok ikut tarikh bagi setiap kaedah M167 dan breakout secara berasingan (K = 1)."""
    H = json.load(open(p(dir_, 'vr_ujian.json')))
    P = pd.read_parquet(p(dir_, 'vr_kolam.parquet'))
    P = P[P.l1 & P.method.isin(['M167'] + BREAKOUT)].reset_index(drop=True)
    P['method'] = P.method.astype(str)
    out = ['| Varian | Kaedah | ' + ' | '.join(f'{nm} beza (t) [hari a/b]' for nm in SAMPEL) + ' |',
           '|---|---|---|---|---|']
    R = {}
    for v in VARIAN:
        for k in ['M167'] + BREAKOUT:
            sel = []
            for nm in SAMPEL:
                df = P[(P.method == k) & P.sampel.eq(nm)]
                s, st = sisi(df, v, H[v['id']]['arah_rs'])
                a = anggar(df.lebih_pegang.values.astype(float), s, st, df.method.values, df.signal_date.values)
                if a is None: sel.append('–'); continue
                dalam = np.isin(st, a['strata'])
                ha = pd.unique(df.entry_date.values[dalam & (s == 1)]).size
                hb = pd.unique(df.entry_date.values[dalam & (s == 0)]).size
                R[f'{v["id"]}|{k}|{nm}'] = dict(D=a['D'], t=a['t'], hari_a=int(ha), hari_b=int(hb))
                sel.append(f'{a["D"]*100:+.2f} ({a["t"]:.2f}) [{ha}/{hb}]')
            out.append(f'| {v["id"]} | {k} | ' + ' | '.join(sel) + ' |')
    simpan_json(R, p(dir_, 'vr_khusus.json'))
    open(p(dir_, 'vr_khusus.md'), 'w').write('\n'.join(out) + '\n')
    print('\n'.join(out))


# ------------------------------------------------------------------ peringkat plasebo (diagnostik tambahan, bukan pra-daftar)
def plasebo(dir_, benih=(1, 2, 3, 4, 5)):
    """Portfolio dengan kunci ranking RAWAK (rantai laluan 1 tetap) dan veto RAWAK dengan bahagian isyarat diveto
    sama seperti V2/V3 dalam setiap kaedah. Menjawab: berapa kaedah 'bertambah baik' secara kebetulan?"""
    pas = muat_pasaran(dir_)
    lajur = ['method', 'ticker', 'signal_date', 'entry_date', 'exit_date', 'kumpulan', 'pos', 'trade_ret',
             'rank_value', 'l1', 'veto_V2', 'veto_V3']
    P = pd.read_parquet(p(dir_, 'vr_kolam.parquet'), columns=lajur)
    P = P[P.trade_ret.notna()]
    f_out = p(dir_, 'vr_plasebo.json')
    R = json.load(open(f_out)) if os.path.exists(f_out) else {}
    for mid, Pm in P.groupby('method', observed=True):
        if mid in R: continue
        Pm = Pm.sort_values(['ticker', 'signal_date', 'pos']).reset_index(drop=True)
        kod_t = Pm.ticker.cat.codes.values.astype(np.int64)
        sd = Pm.signal_date.values.astype(np.int64); ed = Pm.exit_date.values.astype(np.int64)
        T_all = Pm.rename(columns={'entry_date': 'ent', 'exit_date': 'ex', 'trade_ret': 'ret'})
        T_all['ticker'] = T_all.ticker.astype(str)
        res = {}
        for b in benih:
            rng = np.random.default_rng(1000 + b)
            T_all['rawak'] = rng.random(len(T_all))
            for g in ('A', 'B'):
                T = T_all[(T_all.l1) & (T_all.kumpulan.astype(str) == g)].sort_values('pos')
                res[f'RANK_RAWAK{b}|{g}'] = metrik_lengkung(pas.lengkung(
                    T.assign(rank=T.rawak)[['ticker', 'ent', 'ex', 'ret', 'rank']]))
            for vv in ('V2', 'V3'):
                # veto rawak: bahagian isyarat diveto = bahagian sebenar dalam kaedah ini
                q = float(Pm[f'veto_{vv}'].mean())
                ok = rng.random(len(Pm)) >= q
                ambil = _rantai(kod_t, sd, ed, ok)
                for g in ('A', 'B'):
                    Tc = T_all[ambil & (T_all.kumpulan.astype(str) == g).values].sort_values('pos')
                    res[f'VETO_RAWAK_{vv}_{b}|{g}'] = metrik_lengkung(pas.lengkung(
                        Tc.assign(rank=Tc.rank_value)[['ticker', 'ent', 'ex', 'ret', 'rank']]))
        R[mid] = res
        simpan_json(R, f_out)
        print(mid, 'plasebo siap', flush=True)
    # ringkasan: bilangan kaedah naik CAGR lawan ASAS, setiap benih dan sampel
    PT = {k[:-5]: json.load(open(os.path.join(dir_, 'vr_port', k))) for k in os.listdir(p(dir_, 'vr_port'))}
    out = ['| Plasebo | Benih | SELECT naik | VALIDATE-B naik | VALIDATE-2022 naik | median ΔCAGR SELECT / V-B / V-2022 | median ΔMDD SELECT / V-B / V-2022 |',
           '|---|---|---|---|---|---|---|']
    for nm_p in ['RANK_RAWAK', 'VETO_RAWAK_V2_', 'VETO_RAWAK_V3_']:
        for b in benih:
            dc = {s: [] for s in SAMPEL}; dm = {s: [] for s in SAMPEL}
            for k in R:
                a = R[k][f'{nm_p}{b}|A']; bb = R[k][f'{nm_p}{b}|B']; ra = PT[k]['ASAS|A']; rb = PT[k]['ASAS|B']
                dc['SELECT'].append(a['cagr_1321'] - ra['cagr_1321']); dm['SELECT'].append(a['mdd_1321'] - ra['mdd_1321'])
                dc['VALIDATE-B'].append(bb['cagr_1321'] - rb['cagr_1321']); dm['VALIDATE-B'].append(bb['mdd_1321'] - rb['mdd_1321'])
                dc['VALIDATE-2022'].append((a['cagr_22'] - ra['cagr_22'] + bb['cagr_22'] - rb['cagr_22']) / 2)
                dm['VALIDATE-2022'].append((a['mdd_22'] - ra['mdd_22'] + bb['mdd_22'] - rb['mdd_22']) / 2)
            out.append(f'| {nm_p.rstrip("_")} | {b} | ' + ' | '.join(str(int((np.array(dc[s]) > 0).sum())) for s in SAMPEL)
                       + ' | ' + ' / '.join(f'{np.median(dc[s])*100:+.2f}' for s in SAMPEL)
                       + ' | ' + ' / '.join(f'{np.median(dm[s])*100:+.2f}' for s in SAMPEL) + ' |')
    open(p(dir_, 'vr_plasebo.md'), 'w').write('\n'.join(out) + '\n')
    print('\n'.join(out))


def main():
    a = argparse.ArgumentParser()
    a.add_argument('peringkat', choices=['sedia', 'dagangan', 'ujian', 'portfolio', 'laporan', 'khusus', 'plasebo'])
    a.add_argument('--dir', default=DIR0)
    a.add_argument('--kaedah', default='')
    x = a.parse_args()
    warnings.filterwarnings('ignore')
    if x.peringkat == 'portfolio':
        portfolio(x.dir, [k for k in x.kaedah.split(',') if k])
    else:
        dict(sedia=sedia, dagangan=dagangan, ujian=ujian, laporan=laporan, khusus=khusus, plasebo=plasebo)[x.peringkat](x.dir)


if __name__ == '__main__':
    main()
