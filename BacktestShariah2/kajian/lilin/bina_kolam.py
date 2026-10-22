"""Kolam isyarat bersama (AUTOTUNE 2000 saham AS) dengan ciri bar pada tutup hari isyarat.

Untuk ujian veto/ranking/keluar kajian lilin (`kajian/reports/Jenis lilin dan carta alternatif.md`, bahagian
"Uji lima perkara mengikut susunan ini"). Nota: `kajian/research_notes/Ujian lilin atas 2000 saham/kolam_isyarat.md`.

Langkah:
  1. Data AUTOTUNE (teras/data.py) 2011-01-01 hingga hujung data, kumpulan A+B (pemanasan 2 tahun).
  2. Setiap kaedah: sedia(fr, idx) dengan PARAM asal (salinan AUTOTUNE/kaedah; M167 = Rangka R V2 OVN252 diadaptasi
     ke universe 2000). Isyarat sah = ticker dalam universe bulan itu (A atau B; SPEC A01 §1, §3.4) dan tarikh
     isyarat >= 2013-01-01.
  3. Dagangan enjin_at (gap, kos + slippage, had 60 hari, keluar kaedah/henti/sasaran) bagi SETIAP isyarat:
     laluan 1 = dagangan enjin biasa (isyarat yang jatuh semasa posisi ticker sama dibuka dilangkau); laluan 2, 3, ...
     = isyarat yang dilangkau dijalankan semula (keluar sendiri). Kaedah yang exitc bergantung laluan (replika enjin)
     tidak diberi hasil bagi laluan >= 2 (NaN). Bendera pegang8 = dipegang portfolio 8 slot kumpulannya sendiri.
  4. Pulangan hadapan mentah (buka esok -> tutup +5/+10/+20 bar) dan SPY tempoh sama; ciri bar (tiada pandang ke
     hadapan; formula dalam nota).
Output: <keluar>/kolam.parquet, <keluar>/kaedah/<ID>.parquet (cache setiap kaedah), <keluar>/log.json.

Guna (dari akar repo):
  python3 BacktestShariah2/kajian/lilin/bina_kolam.py [--proses 2] [--keluar DIR] [--kaedah M30,M91]
Tiada fail di bawah AUTOTUNE/, BacktestShariah2/kod/ atau WFO/ diubah (dibaca/diimport sahaja).
"""
import argparse, json, os, sys, time, types, warnings
# Cache numba berasingan: cache AUTOTUNE/teras/__pycache__ mungkin dikompil sebagai pakej `teras.enjin_at`
# (ModuleNotFoundError 'teras' apabila dimuat sebagai `enjin_at`); juga elak menulis ke AUTOTUNE/.
os.environ.setdefault('NUMBA_CACHE_DIR', '/tmp/claude-0/-home-user-papertrade-claude/0793050f-2ee1-522e-9bf0-b633a13089db/scratchpad/numba')
from multiprocessing import get_context

import numpy as np
import pandas as pd
from numba import njit

AKAR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
for p in (os.path.join(AKAR, 'BacktestShariah2', 'kod'), os.path.join(AKAR, 'WFO', 'kaedah_baru'),
          os.path.join(AKAR, 'AUTOTUNE', 'teras'), os.path.join(AKAR, 'AUTOTUNE', 'tala')):
    if p not in sys.path: sys.path.insert(0, p)
import data as D          # noqa: E402  AUTOTUNE/teras/data.py
import enjin_at as E      # noqa: E402
import tala as T          # noqa: E402  (muat_kaedah, salin)

CACHE = os.path.join(AKAR, 'AUTOTUNE', '.cache')
KELUAR = '/tmp/claude-0/-home-user-papertrade-claude/0793050f-2ee1-522e-9bf0-b633a13089db/scratchpad/lilin'
MULA_DATA = '2011-01-01'
MULA = pd.Timestamp('2013-01-01')
PETA_INDUSTRI = os.path.join(AKAR, 'BacktestShariah2', 'papertrade', 'peta_industri.csv')

# Pilihan kaedah (lihat nota): GUNA dengan salinan AUTOTUNE + M167; kemudian 26 kaedah UJI KERTAS/SIMPAN berlabel
# RENDAH dalam A01, disusun ikut min(CAGR OOS-A, CAGR OOS-B).
KAEDAH = ['M30', 'M79', 'M96', 'M167',
          'M91', 'M152', 'M135', 'M130', 'M134', 'M41', 'M146', 'M124', 'M20', 'M95', 'M48', 'M04', 'M26', 'M67',
          'M137', 'M93', 'M10', 'M129', 'M139', 'M118', 'M142', 'M149', 'M05', 'M78', 'M33', 'M89']
# exitc ditanda oleh replika laluan enjin dalam sedia() -> hasil keluar sah bagi laluan 1 sahaja.
IKUT_LALUAN = {'M20', 'M26', 'M41', 'M78', 'M167', 'M02', 'M19', 'M31', 'M38', 'M47', 'M76', 'M81', 'M82', 'M100'}
_G = {}


# ---------------------------------------------------------------- M167 (Rangka R V2, OVN252) atas universe 2000
def kaedah_m167():
    import _rangka_r as R   # WFO/kaedah_baru/_rangka_r.py (import enjin.atr daripada BacktestShariah2/kod)

    def sedia(f, idx, P=None):
        tp = _G['tp_dict']
        ovn = {t: np.log(g.open / g.close.shift()).rolling(252, min_periods=252).sum() for t, g in f.items()}
        F = pd.DataFrame(ovn)
        ahli = pd.DataFrame({t: pd.Series(tp[t], index=f[t].index) for t in f}).reindex(F.index)
        ahli = ahli.fillna(False).astype(bool)
        Pc = F.where(ahli).rank(axis=1, pct=True)        # persentil antara ahli universe (A+B) hari itu
        for t, g in f.items():
            p = Pc[t].reindex(g.index)
            s = ((p >= 0.90) & (g.volume.rolling(20).mean() >= 1e5) & ovn[t].notna()
                 & R.spy_atas_sma200(g, idx) & pd.Series(tp[t], index=g.index) & (g.index >= MULA))
            g['sig'] = s.fillna(False).astype(bool)
            g['stop'] = g.open.shift(-1) * 0.88
            g['tgt'] = np.nan
            g['rank'] = ovn[t].astype(float)
            R.tandai_keluar(g, warm=200, k=3.0, n_atr=22, tmax=E.HAD_HARI)   # had 60 hari = enjin_at
    return types.SimpleNamespace(ID='M167', NAMA='Momentum Semalaman (Rangka R V2 OVN252)', TMAX=None, WARM=200,
                                 SILANG=True, PARAM={}, sedia=sedia)


@njit(cache=True)
def _m167_satu(o, h, l, c, a, kos, pos, akhir_t, tmax):
    """Keluar sendiri M167 bagi setiap isyarat (pos global; akhir_t = indeks hujung ticker, eksklusif): masuk buka
    pos+1, henti 0.88 x masuk (buka <= henti -> keluar buka; rendah <= henti -> keluar henti), chandelier tutup <
    maks tutup sejak masuk - 3 x ATR22 atau tutup < henti -> keluar buka esok, had tmax hari -> tutup. Sama dengan
    laluan enjin_at + _rangka_r.tandai_keluar (disahkan atas laluan 1)."""
    m = len(pos)
    ret = np.full(m, np.nan); hari = np.full(m, np.nan); why = np.full(m, np.nan)
    xp = np.full(m, np.nan); mfe = np.full(m, np.nan)
    for r in range(m):
        i = pos[r]; n = akhir_t[r]
        e = o[i + 1]; sp = 0.88 * e
        j = i + 1; mx = -np.inf; x = 0.0; w = 0; jumpa = False
        while j < n:
            if o[j] <= sp:
                x = o[j]; w = 1; jumpa = True; break
            if l[j] <= sp:
                x = sp; w = 1; jumpa = True; break
            if c[j] > mx: mx = c[j]
            kena = c[j] < sp
            if not np.isnan(a[j]) and c[j] < mx - 3.0 * a[j]: kena = True
            if kena and j + 1 < n:
                j += 1; x = o[j]; w = 3; jumpa = True; break
            if (j - i) >= tmax:
                x = c[j]; w = 4; jumpa = True; break
            j += 1
        if not jumpa:
            j = n - 1; x = c[j]; w = 0
        mh = -np.inf; adanan = False
        for q in range(i + 1, j + 1):
            v = h[q]
            if np.isnan(v): adanan = True
            elif v > mh: mh = v
        k = kos[i]
        ret[r] = x / e * (1 - k) / (1 + k) - 1; hari[r] = j - i; why[r] = w; xp[r] = j
        mfe[r] = np.nan if adanan else mh / e - 1
    return ret, hari, why, xp, mfe


def muat_kaedah(mid):
    return kaedah_m167() if mid == 'M167' else T.muat_kaedah(mid)


# ---------------------------------------------------------------- pekerja: isyarat + dagangan satu kaedah
def jalan(mid):
    warnings.filterwarnings('ignore')
    f_out = os.path.join(_G['keluar'], 'kaedah', f'{mid}.parquet')
    if os.path.exists(f_out): return mid, 'cache', None
    t0 = time.time()
    try:
        m = muat_kaedah(mid)
        f = T.salin(_G['fr'])
        m.sedia(f, _G['idx'], dict(m.PARAM))
        t_sedia = time.time() - t0
        S = E.Susun(f, asas=_G['asas'])
        if S.nama != _G['asas'].nama or len(S.sig) != len(_G['asas'].o): raise RuntimeError('susunan tidak sejajar')
        warm = int(m.WARM); tm = int(m.TMAX or 0); tm = E.HAD_HARI if tm <= 0 else min(tm, E.HAD_HARI)
        sig = S.sig & _G['tp'] & _G['sah_tarikh'] & (_G['loc'] >= warm) & (_G['loc'] < _G['n_t'] - 1)
        n_sig = int(sig.sum())
        kos = E.kos_sisi(S.medv)
        i0 = np.zeros(len(S.mula), np.int64); n1 = (S.akhir - S.mula).astype(np.int64)
        baki = sig.copy(); bah = []; pas = 0
        while baki.any():
            pas += 1
            t, i, j, ret, w, mfe, kk = E._trades(S.o, S.h, S.l, S.c, baki, S.st, S.tg, S.ex, kos, S.mula, S.akhir,
                                                 i0, n1, tm, warm, True, 0.0)
            if len(t) == 0: raise RuntimeError('laluan tanpa dagangan tetapi isyarat berbaki')
            pos = S.mula[t] + i
            baki[pos] = False
            bah.append(pd.DataFrame(dict(pos=pos, pas=np.full(len(t), pas, np.int16), ret=ret, days=(j - i),
                                         why=w.astype(np.int8), xpos=S.mula[t] + j, mfe=mfe, kos=kk)))
        R = pd.concat(bah, ignore_index=True) if bah else pd.DataFrame(
            columns=['pos', 'pas', 'ret', 'days', 'why', 'xpos', 'mfe', 'kos'])
        R['rank'] = S.rank[R.pos.values]
        # semakan: laluan 1 = Susun.dagangan biasa (enjin_at tanpa ubah suai)
        S.sig = sig
        Tb = S.dagangan(m.TMAX, warm)
        p1 = R[R.pas == 1].sort_values('pos')
        sama = (len(Tb) == len(p1)) and np.allclose(np.sort(Tb.ret.values), np.sort(p1.ret.values), equal_nan=True)
        # pegang8: portfolio 8 slot x 12.5% bagi kumpulan sendiri (rank kaedah, tertinggi dahulu)
        R['pegang8'] = False
        tk = np.asarray(_G['asas'].nama, object)[_G['q'][p1.pos.values]]
        Tp = pd.DataFrame(dict(ticker=tk, ent=_G['tarikh'][p1.pos.values + 1], ex=_G['tarikh'][p1.xpos.values],
                               ret=p1.ret.values, rank=p1['rank'].values), index=p1.index)
        grp = _G['kump_q'][_G['q'][p1.pos.values]]
        for k in ('A', 'B'):
            Tk = Tp[grp == k]
            if len(Tk):
                _, dp = _G['pasaran'].lengkung(Tk, pegang=True)
                R.loc[dp.index, 'pegang8'] = True
        R[['days', 'why', 'xpos']] = R[['days', 'why', 'xpos']].astype(float)
        m167_sama = None
        if mid == 'M167':   # keluar sendiri sebenar bagi setiap isyarat (bukan NaN bagi laluan >= 2)
            from enjin import atr
            a22 = np.concatenate([atr(g, 22).values for g in f.values()])
            pv = R.pos.values.astype(np.int64)
            akhir_t = S.akhir[_G['q'][pv]].astype(np.int64)
            rr, hh, ww, xx, mm = _m167_satu(S.o, S.h, S.l, S.c, a22, kos, pv, akhir_t, tm)
            k1 = (R.pas == 1).values
            m167_sama = bool(np.allclose(rr[k1], R.ret.values[k1]) and np.array_equal(hh[k1], R.days.values[k1])
                             and np.array_equal(ww[k1], R.why.values[k1]))
            if not m167_sama: raise RuntimeError('M167: keluar sendiri tidak sama dengan laluan 1 enjin')
            R['ret'], R['days'], R['why'], R['xpos'], R['mfe'] = rr, hh, ww, xx, mm
        del f
        if mid in IKUT_LALUAN and mid != 'M167':
            k2 = R.pas > 1
            R.loc[k2, ['ret', 'days', 'why', 'xpos', 'mfe']] = np.nan
        R.insert(0, 'kaedah', mid)
        R.to_parquet(f_out, index=False)
        info = dict(kaedah=mid, saat_sedia=round(t_sedia, 1), saat=round(time.time() - t0, 1), isyarat=n_sig,
                    dagangan_enjin=int((R.pas == 1).sum()), laluan=pas, semak_laluan1_sama=bool(sama),
                    tmax=tm, warm=warm, ikut_laluan=mid in IKUT_LALUAN,
                    m167_keluar_sendiri_sama_laluan1=m167_sama)
        print(json.dumps(info), flush=True)
        return mid, 'siap', info
    except Exception as e:  # rekod dan teruskan kaedah lain
        import traceback
        print(mid, 'RALAT', repr(e), traceback.format_exc()[-800:], flush=True)
        return mid, 'ralat', dict(kaedah=mid, ralat=repr(e), saat=round(time.time() - t0, 1))


# ---------------------------------------------------------------- ciri bar
@njit(cache=True)
def _ha_kiraan(o, h, l, c):
    """Bilangan bar Heikin-Ashi naik berturut-turut berakhir pada setiap bar (0 jika bar HA itu turun)."""
    n = len(o); out = np.zeros(n, np.int32)
    if n == 0: return out
    hc = (o[0] + h[0] + l[0] + c[0]) / 4.0; ho = (o[0] + c[0]) / 2.0
    out[0] = 1 if hc > ho else 0
    for k in range(1, n):
        ho = (ho + hc) / 2.0
        hc = (o[k] + h[k] + l[k] + c[k]) / 4.0
        out[k] = out[k - 1] + 1 if hc > ho else 0
    return out


def ciri_saham(g, spy):
    """Semua ciri satu saham (indeks = tarikh). Nilai pada bar t hanya guna bar <= t; hadapan dilabel fwd*/spy*."""
    O, H, L, C, V = (g[k].astype(float) for k in ('open', 'high', 'low', 'close', 'volume'))
    pc = C.shift(1)
    r = C / pc - 1
    tr = pd.concat([H - L, (H - pc).abs(), (L - pc).abs()], axis=1).max(axis=1)
    atr_s = tr.rolling(14, min_periods=14).mean().shift(1)            # ATR14 hingga t-1
    x = {}
    x['ret1'] = r
    x['max20'] = r.rolling(20, min_periods=20).max()
    x['gap_atr'] = (O - pc) / atr_s
    x['julat_atr'] = (H - L) / atr_s
    q99 = r.rolling(252, min_periods=200).quantile(0.99)
    x['atas1pct_1t'] = (r >= q99).astype(float).where(q99.notna())
    lh, ll = np.log(H), np.log(L); lo_, lc = np.log(O), np.log(C)
    rsv = (lh - lc) * (lh - lo_) + (ll - lc) * (ll - lo_)
    srs = np.sqrt(rsv.rolling(60, min_periods=60).mean()).shift(1)    # sigma Rogers-Satchell 60 hari hingga t-1
    x['rcc_srs60'] = np.log(C / pc) / srs
    x['gap_atr_pctl252'] = x['gap_atr'].rolling(252, min_periods=200).rank(method='max', pct=True)
    on = np.log(O / pc); idr = np.log(C / O)
    x['on5'] = on.rolling(5, min_periods=5).sum()
    for n in (20, 60):
        a = on.rolling(n, min_periods=n).sum(); b = idr.rolling(n, min_periods=n).sum()
        x[f'on{n}'] = a; x[f'id{n}'] = b; x[f'id_share{n}'] = b / (a.abs() + b.abs())
    x['on252'] = on.rolling(252, min_periods=252).sum()
    vmed = V.rolling(50, min_periods=50).median().shift(1)
    x['vol_rel50'] = (V / vmed).replace([np.inf, -np.inf], np.nan)
    x['vol_pctl50'] = V.rolling(50, min_periods=50).rank(method='max', pct=True)
    x['naik_vol90'] = ((C > pc) & (x['vol_pctl50'] >= 0.9)).astype(float).where(x['vol_pctl50'].notna())
    x['hijau_vol90'] = ((C > O) & (x['vol_pctl50'] >= 0.9)).astype(float).where(x['vol_pctl50'].notna())
    x['h52'] = C / H.rolling(252, min_periods=200).max()
    rg = (H - L).where(H > L)
    x['ibs'] = (C - L) / rg
    x['badan_julat'] = (C - O).abs() / rg
    x['badan_arah'] = (C - O) / rg
    x['bayang_atas'] = (H - np.maximum(O, C)) / rg
    x['bayang_bawah'] = (np.minimum(O, C) - L) / rg
    x['ha_naik_berturut'] = pd.Series(_ha_kiraan(O.values, H.values, L.values, C.values), index=g.index).astype(float)
    x['ret126'] = C / C.shift(126) - 1
    x['ret252'] = C / C.shift(252) - 1
    x['medv20'] = (C * V).rolling(20).median()
    # hadapan (hasil, bukan ciri): masuk = buka t+1
    o1 = O.shift(-1)
    x['gap_masuk'] = o1 / C - 1
    so = spy['open'].reindex(g.index, method='ffill'); sc = spy['close'].reindex(g.index, method='ffill')
    for hh in (5, 10, 20):
        x[f'fwd{hh}'] = C.shift(-hh) / o1 - 1
        x[f'spy{hh}'] = sc.shift(-hh) / so.shift(-1) - 1
    mx = H[::-1].rolling(20, min_periods=20).max()[::-1].shift(-1)      # maks high t+1..t+20
    x['mfe20'] = mx / o1 - 1
    return pd.DataFrame(x)


LAJUR_CIRI = None


def bina_ciri(pool, fr, idx, univ, tp_dict):
    """Ciri pada kedudukan isyarat (pos unik) + RS proksi keratan rentas + H52 industri."""
    asas = _G['asas']; q_all = _G['q']; loc_all = _G['loc']
    pos_u = np.unique(pool.pos.values)
    qs = q_all[pos_u]; locs = loc_all[pos_u]
    nama = asas.nama
    tarikh_u = pd.DatetimeIndex(np.unique(asas.tarikh))
    tarikh_u = tarikh_u[tarikh_u >= pd.Timestamp(MULA_DATA)]
    r6 = np.full((len(tarikh_u), len(nama)), np.nan, np.float32); r12 = r6.copy(); h52 = r6.copy()
    ahli = np.zeros((len(tarikh_u), len(nama)), bool)
    bah = []
    spy = idx['SPY']
    sempadan = np.searchsorted(qs, np.arange(len(nama) + 1))
    for qi, t in enumerate(nama):
        g = fr[t]
        X = ciri_saham(g, spy)
        di = tarikh_u.get_indexer(g.index)
        r6[di, qi] = X['ret126'].values; r12[di, qi] = X['ret252'].values; h52[di, qi] = X['h52'].values
        ahli[di, qi] = tp_dict[t]
        a, b = sempadan[qi], sempadan[qi + 1]
        if b > a:
            Y = X.iloc[locs[a:b]].reset_index(drop=True)
            Y.insert(0, 'pos', pos_u[a:b])
            bah.append(Y)
        if qi % 500 == 0: print('ciri', qi, len(nama), flush=True)
    F = pd.concat(bah, ignore_index=True)
    # RS proksi: persentil keratan rentas ret126 / ret252 antara ahli universe (A+B) yang ada nilai hari itu
    def pctl(Mx):
        return pd.DataFrame(np.where(ahli, Mx, np.nan)).rank(axis=1, pct=True).values.astype(np.float32)
    P6, P12 = pctl(r6), pctl(r12)
    di = tarikh_u.get_indexer(asas.tarikh[F.pos.values]); qq = q_all[F.pos.values]
    F['rs6_pct'] = P6[di, qq]; F['rs12_pct'] = P12[di, qq]
    # H52 industri: median H52 ahli universe dalam industri Moomoo sama (peta_industri.csv, peta semasa), n >= 3
    pi = pd.read_csv(PETA_INDUSTRI).drop_duplicates('ticker').set_index('ticker')['industri']
    ind = pd.Series([pi.get(t, np.nan) for t in nama])
    kod_ind, nama_ind = pd.factorize(ind)          # -1 = tiada peta
    Hm = np.where(ahli, h52, np.nan)
    med = np.full((len(tarikh_u), len(nama_ind)), np.nan, np.float32); bil = np.zeros_like(med)
    for k in range(len(nama_ind)):
        kol = Hm[:, kod_ind == k]
        bil[:, k] = np.isfinite(kol).sum(axis=1)
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            med[:, k] = np.nanmedian(kol, axis=1) if kol.shape[1] else np.nan
    ki = kod_ind[qq]
    ok = ki >= 0
    F['industri'] = np.where(ok, np.asarray(nama_ind, object)[np.where(ok, ki, 0)], None)
    F['h52_industri'] = np.where(ok, med[di, np.where(ok, ki, 0)], np.nan)
    F['n_industri'] = np.where(ok, bil[di, np.where(ok, ki, 0)], np.nan)
    F.loc[F.n_industri < 3, 'h52_industri'] = np.nan
    F = F.drop(columns=['ret126', 'ret252'])
    for c in F.columns:
        if F[c].dtype == np.float64 and c not in ('pos',): F[c] = F[c].astype(np.float32)
    return F


# ---------------------------------------------------------------- utama
def main(argv=None):
    a = argparse.ArgumentParser()
    a.add_argument('--proses', type=int, default=2)
    a.add_argument('--keluar', default=KELUAR)
    a.add_argument('--kaedah', default=','.join(KAEDAH))
    x = a.parse_args(argv)
    warnings.filterwarnings('ignore')
    os.makedirs(os.path.join(x.keluar, 'kaedah'), exist_ok=True)
    t0 = time.time()
    fr, idx, univ = D.muat(MULA_DATA, '2100-01-01', 'AB', dir=CACHE)
    akhir_data = max(g.index.max() for g in fr.values())
    print('data', len(fr), 'ticker; hujung', akhir_data.date(), round(time.time() - t0), 's', flush=True)
    asas = E.Asas(fr)
    tp_dict = {t: D.topeng(g, t, univ, 'AB').values for t, g in fr.items()}
    panjang = np.array(asas.panjang, np.int64); mula = np.cumsum(panjang) - panjang
    q = np.repeat(np.arange(len(panjang)), panjang)
    kump = univ.drop_duplicates('ticker').set_index('ticker')['kumpulan']
    _G.update(fr=fr, idx=idx, univ=univ, asas=asas, tp_dict=tp_dict, keluar=x.keluar,
              tp=np.concatenate([tp_dict[t] for t in fr]),
              tarikh=asas.tarikh, sah_tarikh=asas.tarikh >= np.datetime64(MULA, 'ns'),
              q=q, loc=np.arange(len(q)) - mula[q], n_t=panjang[q],
              kump_q=np.array([kump.get(t, '?') for t in fr]),
              pasaran=E.Pasaran(fr, MULA, None))
    senarai = [k.strip() for k in x.kaedah.split(',') if k.strip()]
    log_f = os.path.join(x.keluar, 'log.json')
    log = json.load(open(log_f)) if os.path.exists(log_f) else {}
    with get_context('fork').Pool(x.proses, maxtasksperchild=1) as p:
        for mid, st, info in p.imap_unordered(jalan, senarai):
            if info is not None: log[mid] = info
            json.dump(log, open(log_f, 'w'), indent=1)
    # himpun
    bah = [pd.read_parquet(os.path.join(x.keluar, 'kaedah', f'{m}.parquet')) for m in senarai
           if os.path.exists(os.path.join(x.keluar, 'kaedah', f'{m}.parquet'))]
    P = pd.concat(bah, ignore_index=True)
    print('kolam', len(P), 'baris', round(time.time() - t0), 's', flush=True)
    F = bina_ciri(P, fr, idx, univ, tp_dict)
    P = P.merge(F, on='pos', how='left')
    nama = np.asarray(asas.nama, object)
    P.insert(1, 'ticker', nama[q[P.pos.values]])
    P.insert(2, 'signal_date', asas.tarikh[P.pos.values])
    P.insert(3, 'entry_date', asas.tarikh[P.pos.values + 1])
    P.insert(4, 'kumpulan', _G['kump_q'][q[P.pos.values]])
    xp = P.xpos.values
    okx = np.isfinite(xp)
    ed = np.full(len(P), np.datetime64('NaT'), 'datetime64[ns]')
    ed[okx] = asas.tarikh[xp[okx].astype(np.int64)]
    P['exit_date'] = ed
    P['exit_reason'] = pd.Series(P.why).map(lambda w: E.SEBAB[int(w)] if np.isfinite(w) else None)
    P = P.rename(columns={'kaedah': 'method', 'rank': 'rank_value', 'ret': 'trade_ret', 'days': 'hold_days',
                          'pas': 'laluan', 'mfe': 'mfe_dagangan'})
    P['dagangan_enjin'] = P.laluan == 1
    P['ikut_laluan'] = P.method.isin(IKUT_LALUAN - {'M167'})   # True: trade_ret laluan >= 2 = NaN
    P = P.drop(columns=['why', 'xpos']).sort_values(['method', 'signal_date', 'ticker']).reset_index(drop=True)
    P.to_parquet(os.path.join(x.keluar, 'kolam.parquet'), index=False)
    log['_kolam'] = dict(baris=len(P), lajur=list(P.columns), hujung_data=str(akhir_data.date()),
                         saat=round(time.time() - t0))
    json.dump(log, open(log_f, 'w'), indent=1)
    print('siap', len(P), 'baris', round(time.time() - t0), 's', flush=True)


if __name__ == '__main__':
    main()
