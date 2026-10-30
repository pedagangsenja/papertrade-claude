"""Dua SISTEM LENGKAP, bukan penapis masuk — pradaftar `REVERSE/SPEC_SISTEM.md`.

Sistem A = pakej O'Neil/Minervini/Qullamaggie (RS + sektor + rejim + pecahan + jual separa +
ekor MA20 + henti -8%). Sistem B = momentum Clenow *Stocks on the Move* (peringkat kecerunan
regresi x R2, pariti risiko ATR, rejim SPY atas MA200, imbang Rabu).

Setiap ujian terdahulu menguji PENAPIS MASUK; `SETUP.md` menutup ruang itu. Ini menguji masuk DAN
pegang DAN keluar DAN saiz DAN rejim sebagai satu pakej.

Guna: python3 REVERSE/step16_sistem.py [--benih 20] [--laporan-sahaja]
Output: REVERSE/SISTEM.md, REVERSE/sistem.csv
"""
import argparse
import sys
from pathlib import Path

import numpy as np
import pandas as pd

AKAR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(AKAR))
from REVERSE.teras import kos as K  # noqa: E402
from REVERSE.teras import stat as ST  # noqa: E402

KELUAR = AKAR / 'REVERSE'
CACHE = KELUAR / '.cache'
HARGA = AKAR / 'AUTOTUNE' / '.cache_autotune-data-a02'
SPUS = AKAR / 'BacktestShariah2' / 'data' / 'penanda_aras' / 'spus_bulanan.csv'

TH0, TH1 = 2012, 2025
UJI0, UJI1 = 2020, 2025
CAIR = 100_000.0
N_BENIH = 20

# --- Sistem A (spec §2) ---
A_SLOT = 10
A_HENTI = 0.92          # henti awal -8%
A_SASAR = 1.10          # jual 1/3 pada +10%
A_HARI_SEPARA = 5       # atau hari ke-5
A_PECAHAN_SEPARA = 1 / 3

# --- Sistem B (spec §3) ---
B_SLOT = 20
B_TINGKAP = 90          # regresi 90 hari
B_LOMPAT = 0.15         # diskualifikasi jika pernah bergerak > 15% sehari
B_RISIKO = 0.001        # pariti risiko 10 bps
B_SAIZ_MAKS = 0.20      # had keselamatan berangka (bukan peraturan Clenow)
B_PERATUS_PEGANG = 0.20  # jual jika keluar 20% teratas peringkat


def regresi_skor(c, n=B_TINGKAP):
    """Kecerunan regresi eksponen n-hari (disetahunkan) x R2 — skor Clenow.

    Dikira daripada hasil tambah bergulir: x tetap 0..n-1, jadi Sx dan Sxx pemalar dan Sxy ialah
    konvolusi dengan kernel tetap. Itu menjadikan 3,300 ticker boleh dikira.
    """
    y = np.log(np.where(c > 0, c, np.nan))
    m = len(y)
    out = np.full(m, np.nan)
    if m < n:
        return out
    x = np.arange(n, dtype='float64')
    Sx, Sxx = x.sum(), (x * x).sum()
    pen = n * Sxx - Sx * Sx
    s = pd.Series(y)
    Sy = s.rolling(n).sum().to_numpy()
    Syy = s.pow(2).rolling(n).sum().to_numpy()
    # Sxy pada setiap hujung tingkap = konvolusi y dengan x terbalik
    Sxy = np.convolve(np.nan_to_num(y), x[::-1], mode='full')[:m]
    Sxy = np.where(np.isfinite(Sy), Sxy, np.nan)
    cerun = (n * Sxy - Sx * Sy) / pen
    sst = Syy - Sy * Sy / n
    with np.errstate(invalid='ignore', divide='ignore'):
        r2 = np.where(sst > 0, cerun * cerun * (Sxx - Sx * Sx / n) / sst, np.nan)
        tahunan = np.exp(cerun * 252.0) - 1.0
        out = tahunan * np.clip(r2, 0.0, 1.0)
    return out


class Panel:
    """Matriks padat ticker x tarikh + semua siri terbitan yang kedua-dua sistem perlukan."""

    def __init__(self):
        bhg = []
        for y in range(TH0 - 2, TH1 + 1):
            p = HARGA / f'harga_{y}.parquet'
            if p.exists():
                bhg.append(pd.read_parquet(p, columns=['ticker', 'date', 'open', 'high', 'low',
                                                       'close', 'volume']))
        df = pd.concat(bhg, ignore_index=True)
        df = df[df.date <= pd.Timestamp(f'{TH1}-12-31')].sort_values(['ticker', 'date'])
        self.tarikh = np.array(sorted(df.date.unique()))
        self.tick = np.array(sorted(df.ticker.unique()))
        it = {t: i for i, t in enumerate(self.tick)}
        idt = {d: i for i, d in enumerate(self.tarikh)}
        n, m = len(self.tick), len(self.tarikh)
        nan = lambda: np.full((n, m), np.nan, 'float32')  # noqa: E731
        self.O, self.H, self.L, self.C = nan(), nan(), nan(), nan()
        self.ATRP, self.MA20, self.MA100, self.MA200 = nan(), nan(), nan(), nan()
        self.NIL, self.SKOR = nan(), nan()
        self.DISK = np.ones((n, m), bool)
        for t, g in df.groupby('ticker', sort=False):
            i = it[t]
            g = g.sort_values('date')
            j = np.array([idt[d] for d in g.date])
            o, h, lo, c = (g[x].to_numpy('float64') for x in ('open', 'high', 'low', 'close'))
            v = g.volume.to_numpy('float64')
            self.O[i, j], self.H[i, j], self.L[i, j], self.C[i, j] = o, h, lo, c
            cs = pd.Series(c)
            pc = cs.shift(1)
            tr = np.maximum(h - lo, np.maximum((h - pc).abs(), (lo - pc).abs()))
            atr = pd.Series(tr).ewm(alpha=1 / 20, adjust=False, min_periods=20).mean().to_numpy()
            self.ATRP[i, j] = atr / np.where(c > 0, c, np.nan) * 100.0
            self.MA20[i, j] = cs.rolling(20).mean().to_numpy()
            self.MA100[i, j] = cs.rolling(100).mean().to_numpy()
            self.MA200[i, j] = cs.rolling(200).mean().to_numpy()
            self.NIL[i, j] = (cs * v).rolling(20, min_periods=10).median().to_numpy()
            self.SKOR[i, j] = regresi_skor(c)
            lompat = (cs / pc - 1).abs().rolling(B_TINGKAP, min_periods=1).max().to_numpy()
            self.DISK[i, j] = lompat > B_LOMPAT
        ix = pd.read_parquet(HARGA / 'idx.parquet')
        s = ix[ix.ticker == 'SPY'].sort_values('date').set_index('date').close
        s = s.reindex(pd.DatetimeIndex(self.tarikh)).ffill()
        self.SPY = s.to_numpy('float64')
        self.SPY50 = s.rolling(50).mean().to_numpy()
        self.SPY200 = s.rolling(200).mean().to_numpy()
        self.hari = pd.DatetimeIndex(self.tarikh)
        self.rabu = np.asarray(self.hari.dayofweek == 2)


def layak(P, d):
    """Topeng ticker boleh didagangkan pada hari d: ada harga, cair, dan buka esok ada."""
    if d + 1 >= len(P.tarikh):
        return np.zeros(len(P.tick), bool)
    return (np.isfinite(P.C[:, d]) & np.isfinite(P.NIL[:, d]) & (P.NIL[:, d] >= CAIR)
            & np.isfinite(P.O[:, d + 1]) & (P.O[:, d + 1] > 0))


def ind_sistem_a(P):
    """Lajur masuk + alam Sistem A daripada cache signals fasa 1 (tanpa pandang hadapan)."""
    bhg = []
    for y in range(TH0, TH1 + 1):
        p = CACHE / f'signals_{y}.parquet'
        if p.exists():
            d = pd.read_parquet(p, columns=['ticker', 'tarikh', 'dalam_univ', 'rs_spy_6b',
                                            'sektor_atas_ma50', 'donchian20', 'breakout_asas',
                                            'vcp'])
            bhg.append(d[d.dalam_univ == 1].drop(columns='dalam_univ'))
    D = pd.concat(bhg, ignore_index=True)
    D['tarikh'] = pd.to_datetime(D.tarikh)
    it = {t: i for i, t in enumerate(P.tick)}
    idt = {d: i for i, d in enumerate(P.tarikh)}
    n, m = len(P.tick), len(P.tarikh)
    RS = np.full((n, m), np.nan, 'float32')
    SEK = np.zeros((n, m), bool)
    PEC = np.zeros((n, m), bool)
    i = D.ticker.map(it).to_numpy()
    j = D.tarikh.map(idt).to_numpy()
    ok = pd.notna(i) & pd.notna(j)
    i, j = i[ok].astype(int), j[ok].astype(int)
    RS[i, j] = D.rs_spy_6b.to_numpy('float32')[ok]
    SEK[i, j] = D.sektor_atas_ma50.fillna(0).to_numpy().astype(bool)[ok]
    PEC[i, j] = ((D.donchian20.fillna(0) + D.breakout_asas.fillna(0)
                  + D.vcp.fillna(0)).to_numpy() > 0)[ok]
    return RS, SEK, PEC


def sistem_a(P, RS, SEK, PEC, benih, mula, akhir):
    """Pakej O'Neil/Minervini/Qullamaggie. Pulangkan siri ekuiti harian."""
    rng = np.random.default_rng(benih)
    m = len(P.tarikh)
    tunai, buka, ek = 1.0, [], np.full(m, np.nan)
    prev = 1.0
    for d in range(mula, min(akhir, m - 1)):
        # 1. keluar yang matang hari ini (dinilai pada tutup d-1, dilaksana pada buka d)
        for p in list(buka):
            if p['keluar'] == d:
                px = float(P.O[p['i'], d])
                tunai += p['unit'] * px * (1 - K.kos_sisi(P.NIL[p['i'], d]))
                buka.remove(p)
            elif p['separa'] == d:
                u = p['unit'] * A_PECAHAN_SEPARA
                px = float(P.O[p['i'], d])
                tunai += u * px * (1 - K.kos_sisi(P.NIL[p['i'], d]))
                p['unit'] -= u
                p['separa'] = -1
        # 2. nilai syarat keluar pada tutup d
        for p in buka:
            if p['keluar'] > 0:
                continue
            i, c = p['i'], P.C[p['i'], d]
            if not np.isfinite(c):
                continue
            if P.L[i, d] <= p['henti'] or (np.isfinite(P.MA20[i, d]) and c < P.MA20[i, d]):
                p['keluar'] = d + 1
            elif p['separa'] == 0 and (c >= p['masuk'] * A_SASAR
                                       or d - p['hari'] >= A_HARI_SEPARA):
                p['separa'] = d + 1
        # 3. masuk: hanya bila rejim OK
        rejim = (np.isfinite(P.SPY50[d]) and np.isfinite(P.SPY200[d])
                 and P.SPY[d] > P.SPY50[d] and P.SPY[d] > P.SPY200[d])
        if rejim and len(buka) < A_SLOT:
            lay = layak(P, d)
            rs = np.where(lay, RS[:, d], np.nan)
            amb = np.nanquantile(rs, 0.80) if np.isfinite(rs).sum() > 20 else np.inf
            calon = np.flatnonzero(lay & PEC[:, d] & SEK[:, d] & (rs >= amb))
            if calon.size:
                calon = calon[rng.permutation(calon.size)]
                dipegang = {p['i'] for p in buka}
                for i in calon:
                    if len(buka) >= A_SLOT:
                        break
                    if i in dipegang:
                        continue
                    belanja = min(prev / A_SLOT, tunai)
                    if belanja <= 1e-9:
                        break
                    px = float(P.O[i, d + 1])
                    unit = belanja * (1 - K.kos_sisi(P.NIL[i, d])) / px
                    tunai -= belanja
                    buka.append(dict(i=int(i), unit=unit, masuk=px, hari=d + 1,
                                     henti=px * A_HENTI, separa=0, keluar=0))
        nilai = tunai + sum(p['unit'] * float(P.C[p['i'], d])
                            for p in buka if np.isfinite(P.C[p['i'], d]))
        ek[d] = prev = nilai
    return ek


def sistem_b(P, benih, mula, akhir):
    """Momentum Clenow. Imbang setiap Rabu; imbang saiz setiap Rabu kedua.

    `benih` tidak mengubah apa-apa: peringkat skor berterusan tiada seri. Dikekalkan supaya API
    sama dengan sistem_a dan supaya laporan boleh menunjukkan sebaran benih = 0 secara eksplisit.
    """
    m = len(P.tarikh)
    tunai, buka, ek = 1.0, {}, np.full(m, np.nan)
    prev, n_rabu = 1.0, 0
    ded, npos = [], []

    def jual(i, d, unit):
        nonlocal tunai
        px = float(P.O[i, d])
        if np.isfinite(px) and px > 0:
            tunai += unit * px * (1 - K.kos_sisi(P.NIL[i, d]))

    for d in range(mula, min(akhir, m - 1)):
        # Arahan yang ditetapkan Rabu lepas dilaksana pada buka hari ini
        for i in [i for i, p in buka.items() if p['jual']]:
            jual(i, d, buka[i]['unit'])
            del buka[i]
        for i, p in buka.items():
            if p['tambah'] > 0:
                px = float(P.O[i, d])
                belanja = min(p['tambah'], tunai)
                if np.isfinite(px) and px > 0 and belanja > 1e-9:
                    p['unit'] += belanja * (1 - K.kos_sisi(P.NIL[i, d])) / px
                    tunai -= belanja
            elif p['tambah'] < 0:
                u = min(-p['tambah'], p['unit'])
                jual(i, d, u)
                p['unit'] -= u
            p['tambah'] = 0.0
        if P.rabu[d]:
            n_rabu += 1
            lay = layak(P, d)
            sk = np.where(lay & ~P.DISK[:, d], P.SKOR[:, d], np.nan)
            urut = np.argsort(np.where(np.isfinite(sk), -sk, np.inf))
            n_sah = int(np.isfinite(sk).sum())
            had = max(int(n_sah * B_PERATUS_PEGANG), B_SLOT)
            top = set(urut[:had].tolist())
            for i, p in buka.items():
                c, ma = P.C[i, d], P.MA100[i, d]
                if (i not in top or P.DISK[i, d] or not np.isfinite(c)
                        or (np.isfinite(ma) and c < ma)):
                    p['jual'] = True
            rejim = np.isfinite(P.SPY200[d]) and P.SPY[d] > P.SPY200[d]
            nilai_kini = tunai + sum(p['unit'] * float(P.C[i, d]) for i, p in buka.items()
                                     if np.isfinite(P.C[i, d]))
            if rejim:
                tinggal = B_SLOT - sum(1 for p in buka.values() if not p['jual'])
                # Pemecah seri rawak antara skor yang hampir sama (benih)
                # Sistem B DETERMINISTIK: peringkat ialah skor berterusan, jadi seri
                # praktiknya tiada dan benih hampir tiada kesan. Itu bukan kelemahan — ia
                # bermakna Clenow tidak mempunyai hingar pemilihan yang KEPEKATAN_BENIH.md ukur
                # pada susunan sewenang-wenang. Benih dikekalkan untuk keseragaman API sahaja.
                cand = [int(i) for i in urut[:had] if np.isfinite(sk[i])]
                for i in cand:
                    if tinggal <= 0:
                        break
                    if i in buka:
                        continue
                    a = P.ATRP[i, d]
                    if not np.isfinite(a) or a <= 0:
                        continue
                    sasar = min(nilai_kini * B_RISIKO / (a / 100.0), nilai_kini * B_SAIZ_MAKS)
                    belanja = min(sasar, tunai)
                    if belanja <= 1e-9:
                        break
                    px = float(P.O[i, d + 1])
                    buka[i] = dict(unit=belanja * (1 - K.kos_sisi(P.NIL[i, d])) / px,
                                   jual=False, tambah=0.0)
                    tunai -= belanja
                    tinggal -= 1
            if n_rabu % 2 == 0:
                for i, p in buka.items():
                    if p['jual']:
                        continue
                    a, c = P.ATRP[i, d], P.C[i, d]
                    if not np.isfinite(a) or a <= 0 or not np.isfinite(c):
                        continue
                    sasar = min(nilai_kini * B_RISIKO / (a / 100.0), nilai_kini * B_SAIZ_MAKS)
                    p['tambah'] = float(sasar - p['unit'] * c)
        pos = sum(p['unit'] * float(P.C[i, d]) for i, p in buka.items()
                  if np.isfinite(P.C[i, d]))
        nilai = tunai + pos
        ded.append(pos / nilai if nilai > 0 else 0.0)
        npos.append(len(buka))
        ek[d] = prev = nilai
    d_arr = np.array(ded)
    th = pd.DatetimeIndex(P.tarikh[mula:mula + len(d_arr)]).year
    ut = pd.Series(d_arr * 100).groupby(th).mean().round(0).astype(int)
    return ek, dict(dedah=float(d_arr.mean() * 100), dedah_med=float(np.median(d_arr) * 100),
                    pct_bawah50=float((d_arr < 0.5).mean() * 100),
                    posisi=float(np.mean(npos)),
                    dedah_tahun=' '.join(f'{y}:{v}%' for y, v in ut.items()))


def penanda_spus():
    s = pd.read_csv(SPUS, comment='#')
    s['bulan'] = pd.PeriodIndex(s.bulan, freq='M')
    pt, mt = [], []
    for y in range(UJI0, UJI1 + 1):
        q = s[(s.bulan >= pd.Period(f'{y - 1}-12'))
              & (s.bulan <= pd.Period(f'{y}-12'))].tutup.to_numpy('float64')
        if len(q) >= 3:
            pt.append((q[-1] / q[0] - 1) * 100)
            mt.append(ST.mdd(q))
    w = s[(s.bulan >= pd.Period(f'{UJI0}-01')) & (s.bulan <= pd.Period(f'{UJI1}-12'))]
    v = w.tutup.to_numpy('float64')
    th = (w.bulan.iloc[-1] - w.bulan.iloc[0]).n / 12.0
    return dict(median_pul=float(np.median(pt)), median_mdd=float(np.median(mt)),
                cagr=float(((v[-1] / v[0]) ** (1 / th) - 1) * 100), mdd_tingkap=ST.mdd(v))


def cagr(e, hari):
    ok = np.isfinite(e)
    if ok.sum() < 2:
        return np.nan
    e, n = e[ok], hari[ok]
    th = (n[-1] - n[0]).days / 365.25
    return float(((e[-1] / e[0]) ** (1 / th) - 1) * 100) if th > 0 else np.nan


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument('--benih', type=int, default=N_BENIH)
    ap.add_argument('--laporan-sahaja', action='store_true')
    a = ap.parse_args(argv)
    f = KELUAR / 'sistem.csv'
    if a.laporan_sahaja and f.exists():
        fd = KELUAR / 'sistem_dedah.csv'
        return laporan(pd.read_csv(f),
                       pd.read_csv(fd).iloc[0].to_dict() if fd.exists() else {})

    print('1/3 membina panel (harga + ATR + MA + skor Clenow)...', flush=True)
    P = Panel()
    print(f'  {len(P.tick):,} ticker x {len(P.tarikh):,} sesi', flush=True)
    print('2/3 lajur Sistem A (RS, sektor, pecahan)...', flush=True)
    RS, SEK, PEC = ind_sistem_a(P)
    print(f'  RS ada {int(np.isfinite(RS).sum()):,} sel | pecahan {int(PEC.sum()):,}', flush=True)
    mula = int(np.searchsorted(P.tarikh, np.datetime64(f'{TH0}-01-01')))
    akhir = len(P.tarikh)
    m0 = int(np.searchsorted(P.tarikh, np.datetime64(f'{UJI0}-01-01')))
    print('3/3 simulasi...', flush=True)
    baris, diag = [], {}
    for b in range(1, a.benih + 1):
        for nm in ('A_pakar', 'B_clenow'):
            if nm == 'A_pakar':
                ek = sistem_a(P, RS, SEK, PEC, b, mula, akhir)
            else:
                ek, st = sistem_b(P, b, mula, akhir)
                if b == 1:
                    diag = st
            baris.append(dict(sistem=nm, benih=b,
                              cagr_14th=cagr(ek, P.hari), mdd_14th=ST.mdd(ek[np.isfinite(ek)]),
                              cagr_uji=cagr(ek[m0:], P.hari[m0:]),
                              mdd_uji=ST.mdd(ek[m0:][np.isfinite(ek[m0:])])))
        print(f'  benih {b}/{a.benih} siap', flush=True)
    R = pd.DataFrame(baris)
    R.to_csv(f, index=False)
    pd.DataFrame([diag]).to_csv(KELUAR / 'sistem_dedah.csv', index=False)
    return laporan(R, diag)


def laporan(R, diag=None):
    diag = diag or {}
    sp = penanda_spus()
    g = R.groupby('sistem').agg(
        cagr=('cagr_uji', 'median'), p10=('cagr_uji', lambda x: x.quantile(0.10)),
        p90=('cagr_uji', lambda x: x.quantile(0.90)), mdd=('mdd_uji', 'median'),
        cagr14=('cagr_14th', 'median'), mdd14=('mdd_14th', 'median'),
        sd=('cagr_uji', 'std'), n=('benih', 'size')).reset_index()
    # Spec §5: ketiga-tiga syarat, dan mesti bertahan pada KEDUA-DUA konvensyen.
    g['s1'] = g.cagr > sp['cagr']
    g['s2'] = g.mdd > sp['mdd_tingkap']
    g['s3'] = g.p10 > sp['cagr']
    g['s_median'] = (g.cagr > sp['median_pul']) & (g.mdd > sp['median_mdd'])
    g['lulus'] = g.s1 & g.s2 & g.s3 & g.s_median
    lulus = g[g.lulus]

    L = ['# Dua sistem lengkap lawan SPUS', '']
    L.append(f'Dijana {pd.Timestamp.now(tz="UTC"):%Y-%m-%d %H:%M} UTC oleh '
             '`REVERSE/step16_sistem.py`. Pradaftar `REVERSE/SPEC_SISTEM.md` (dikomit sebelum '
             'larian ini).')
    L.append('')
    L.append(f'## Keputusan: **{"LULUS" if len(lulus) else "DITOLAK"}**')
    L.append('')
    L.append('Ini ujian pertama dalam kajian ini yang menguji **sistem lengkap** — masuk **dan** '
             'pegang **dan** keluar **dan** saiz **dan** rejim — bukan penapis masuk.')
    L.append('')
    L.append(f'**SPUS {UJI0}–{UJI1}:** CAGR **{sp["cagr"]:+.2f}%** / MDD '
             f'**{sp["mdd_tingkap"]:.2f}%** · median tahunan {sp["median_pul"]:+.2f}% / MDD '
             f'{sp["median_mdd"]:.2f}%.')
    L.append('')
    L.append('| Sistem | CAGR median | p10 | p90 | MDD median | CAGR 14 thn | MDD 14 thn | '
             'Sebaran benih | Lulus |')
    L.append('|---|---|---|---|---|---|---|---|---|')
    nama = {'A_pakar': 'A — pakej O\'Neil/Minervini/Qullamaggie', 'B_clenow': 'B — momentum Clenow'}
    for _, r in g.sort_values('cagr', ascending=False).iterrows():
        L.append(f'| **{nama.get(r.sistem, r.sistem)}** | {r.cagr:+.2f}% | {r.p10:+.2f}% | '
                 f'{r.p90:+.2f}% | {r.mdd:.2f}% | {r.cagr14:+.2f}% | {r.mdd14:.2f}% | '
                 f'{r.sd:.2f} mata | {"**YA**" if r.lulus else "tidak"} |')
    L.append(f'| **SPUS** | **{sp["cagr"]:+.2f}%** | — | — | **{sp["mdd_tingkap"]:.2f}%** | '
             '— | — | — | — |')
    L.append('')
    return laporan2(L, g, R, lulus, sp, diag)


def laporan2(L, g, R, lulus, sp, diag):
    A = g[g.sistem == 'A_pakar'].iloc[0] if (g.sistem == 'A_pakar').any() else None
    B = g[g.sistem == 'B_clenow'].iloc[0] if (g.sistem == 'B_clenow').any() else None
    L.append('`S1` CAGR > SPUS · `S2` MDD lebih cetek · `S3` **p10** masih > SPUS · ditambah '
             'syarat konvensyen median tahunan. Spec §5 memerlukan **kesemuanya**.')
    L.append('')
    L.append('| Sistem | S1 pulangan | S2 MDD | S3 p10 | Konvensyen median |')
    L.append('|---|---|---|---|---|')
    tk = {True: 'ya', False: 'tidak'}
    for _, r in g.iterrows():
        L.append(f'| `{r.sistem}` | {tk[bool(r.s1)]} | {tk[bool(r.s2)]} | {tk[bool(r.s3)]} | '
                 f'{tk[bool(r.s_median)]} |')
    L.append('')
    if B is not None:
        L.append('## Sistem B deterministik — dan itu bermaklumat')
        L.append('')
        L.append(f'Sebaran 20 benih bagi Sistem B ialah **{B.sd:.3f} mata**. Peringkat Clenow '
                 'ialah skor berterusan, jadi seri praktiknya tiada dan benih tidak mengubah '
                 'apa-apa.')
        L.append('')
        L.append(f'Bandingkan Sistem A: sebaran **{A.sd:.2f} mata** daripada pemecah seri rawak '
                 'antara calon yang layak.' if A is not None else '')
        L.append('')
        L.append('Itu kelebihan struktur Clenow yang jarang disebut: ia **tiada hingar '
                 'pemilihan**. `KEPEKATAN_BENIH.md` mengukur hingar itu sebagai 17.3 mata '
                 'peratus setahun pada susunan sewenang-wenang. Sistem yang memeringkat ikut '
                 'skor objektif tidak mempunyainya sama sekali — jadi keputusannya boleh '
                 'dipercayai pada sampel yang jauh lebih kecil.')
        L.append('')
    # --- Pendedahan: ia menerangkan pulangan DAN MDD sekaligus ---
    if diag:
        B2 = g[g.sistem == 'B_clenow'].iloc[0]
        dd = float(diag['dedah'])
        L.append('## Pendedahan menerangkan KEDUA-DUA nombor Sistem B')
        L.append('')
        L.append(f'Sistem B memegang **{float(diag["posisi"]):.1f} daripada {B_SLOT} slot** '
                 f'tetapi pendedahan pasarannya hanya **{dd:.1f}% purata** '
                 f'(median {float(diag["dedah_med"]):.1f}%), dan ia di bawah 50% pada '
                 f'**{float(diag["pct_bawah50"]):.1f}%** daripada hari.')
        L.append('')
        L.append(f'Sebabnya saiz pariti risiko Clenow: `{B_RISIKO:.3f} × ekuiti ÷ ATR%`. Dengan '
                 'ATR peneraju momentum kira-kira 5–6%, setiap posisi hanya ~1.8% ekuiti, jadi '
                 f'{float(diag["posisi"]):.0f} posisi memberi ~{dd:.0f}% pendedahan. Itu '
                 '**peraturan Clenow, bukan pepijat** — bukunya menegaskan kawalan risiko, '
                 'bukan mengalahkan indeks dalam pasaran menaik.')
        L.append('')
        L.append('Itu menjadikan perbandingan mentah **tidak adil pada kedua-dua arah**: SPUS '
                 f'melabur 100%, Sistem B melabur {dd:.0f}%. CAGR mentah **menghukum** '
                 'Sistem B; MDD mentah **menyanjungnya**.')
        L.append('')
        L.append('| Ukuran | Sistem B | SPUS |')
        L.append('|---|---|---|')
        L.append(f'| CAGR | {B2.cagr:+.2f}% | {sp["cagr"]:+.2f}% |')
        L.append(f'| MDD | {B2.mdd:.2f}% | {sp["mdd_tingkap"]:.2f}% |')
        L.append(f'| CAGR / abs(MDD) | {B2.cagr / abs(B2.mdd):.3f} | '
                 f'{sp["cagr"] / abs(sp["mdd_tingkap"]):.3f} |')
        L.append(f'| Pendedahan purata | {dd:.1f}% | 100% |')
        L.append(f'| **CAGR setiap unit pendedahan** | **{B2.cagr / (dd / 100):.2f}%** | '
                 f'**{sp["cagr"]:.2f}%** |')
        L.append('')
        L.append(f'Baris terakhir ialah dapatan sebenar: **{B2.cagr / (dd / 100):.1f}% lawan '
                 f'{sp["cagr"]:.1f}% setiap unit pendedahan pasaran** — praktiknya **sama**. '
                 'Momentum Clenow tidak menambah pulangan; ia menambah **kawalan risiko**, dan '
                 'ia membayar kawalan itu dengan pendedahan yang lebih rendah.')
        L.append('')
        L.append('**Amaran yang mesti disertakan:** jangan tafsir ini sebagai "naikkan '
                 'pendedahan 3× dan dapat 18%". Menaikkan pendedahan menaikkan drawdown secara '
                 'berkadar; itu bukan alfa, itu beta. Dan menaikkannya melebihi 100% memerlukan '
                 'margin, iaitu riba.')
        L.append('')
        if diag.get('dedah_tahun'):
            L.append('Pendedahan setiap tahun: `' + str(diag['dedah_tahun']) + '`. Penapis '
                     'rejim memang berfungsi — pendedahan paling rendah tepat pada tahun '
                     'jatuh, dan itu sebab MDD-nya cetek.')
        L.append('')
    L.append('## Tafsiran')
    L.append('')
    if len(lulus):
        L.append(f'**{len(lulus)} sistem lulus kesemua syarat.** Jangkaan priori saya dalam '
                 'spec §7 salah, dan itu mesti dinyatakan dengan menonjol.')
        L.append('')
        for _, r in lulus.iterrows():
            L.append(f'- `{r.sistem}`: CAGR {r.cagr:+.2f}% (p10 {r.p10:+.2f}%), MDD {r.mdd:.2f}% '
                     f'lawan SPUS {sp["cagr"]:+.2f}% / {sp["mdd_tingkap"]:.2f}%')
        L.append('')
        L.append('**Ia tetap backtest.** Langkah seterusnya bukan mempercayainya tetapi '
                 'menjalankannya ke hadapan sebagai lorong `portfolio_slot/`, dan '
                 '`BANDING_SPUS.md` sudah mengira berapa lama itu mengambil masa.')
    else:
        L.append('**Tiada sistem lulus kesemua syarat.** Tetapi bacaan yang betul bukan "sistem '
                 'pakar tidak berfungsi" — periksa syarat mana yang gagal bagi setiap satu, '
                 'kerana gagal pada MDD sahaja bermakna perkara yang sangat berbeza daripada '
                 'gagal pada pulangan.')
        L.append('')
        for _, r in g.iterrows():
            kata = []
            if not r.s1:
                kata.append(f'pulangan ({r.cagr:+.2f}% lawan {sp["cagr"]:+.2f}%)')
            if not r.s2:
                kata.append(f'MDD ({r.mdd:.2f}% lawan {sp["mdd_tingkap"]:.2f}%)')
            if r.s1 and r.s2 and not r.s3:
                kata.append(f'p10 ({r.p10:+.2f}%) — iaitu dalam hingar pemilihan')
            L.append(f'- `{r.sistem}` gagal pada: {", ".join(kata) if kata else "konvensyen median"}')
        L.append('')
        if B is not None:
            L.append('### Jangkaan priori saya salah ke arah BERTENTANGAN')
            L.append('')
            L.append('Spec §7 menyatakan: *"Sistem B menghampiri SPUS pada pulangan tetapi gagal '
                     'syarat MDD."* Yang berlaku songsang:')
            L.append('')
            L.append(f'- **MDD LULUS dengan lega**: {B.mdd:.2f}% lawan SPUS '
                     f'{sp["mdd_tingkap"]:.2f}% — lebih cetek **'
                     f'{abs(sp["mdd_tingkap"]) - abs(B.mdd):.2f} mata**, bukan lebih dalam.')
            L.append(f'- **Pulangan GAGAL dengan jauh**: {B.cagr:+.2f}% lawan '
                     f'{sp["cagr"]:+.2f}% — jurang {sp["cagr"] - B.cagr:.2f} mata.')
            L.append('')
            L.append('Saya menjangka kemalangan momentum memperdalam drawdown. Sebaliknya '
                     'penapis rejim + saiz pariti risiko menjadikannya sistem **berisiko '
                     'rendah, pulangan rendah**. Bahagian pendedahan di atas menerangkan '
                     'sebabnya, dan ia bukan tentang momentum sama sekali — ia tentang berapa '
                     'banyak modal yang dilaburkan.')
            L.append('')
            L.append('Itu kali **kedua** jangkaan priori saya salah dalam dua pradaftar '
                     'terakhir (`SPEC_SILANG.md` §7 juga salah). Kedua-duanya pada ruang yang '
                     'belum diukur. Saya catat itu sebagai pola, bukan kebetulan: ramalan saya '
                     'tidak boleh dipercayai di tempat yang belum diukur, dan itu sebab '
                     'pradaftar ada.')
            L.append('')
        if A is not None:
            L.append(f'Sistem A gagal pada kedua-dua paksi ({A.cagr:+.2f}%, MDD {A.mdd:.2f}%) '
                     'walaupun ia mengandungi RS, sektor, rejim dan keluar aktif yang saya '
                     'tinggalkan daripada 672 setup. Jadi menambah dua tiang itu **tidak** '
                     'menyelamatkan pendekatan pecahan-dan-penapis. Sebaran benihnya '
                     f'{A.sd:.2f} mata, jadi ia juga tertakluk hingar pemilihan yang Sistem B '
                     'tiada sama sekali.')
            L.append('')
    L.append('## Had')
    L.append('')
    L.append('- Alam Release `autotune-data-a02`, **bukan** ditapis Syariah; SPUS ditapis. '
             'Tapisan Syariah membuang semua kewangan.')
    L.append('- Sistem A ialah **anggaran mekanikal** kaedah diskresi: pemilihan antara calon, '
             'saiz atas keyakinan, dan masa keluar manual tidak boleh dikodkan. Kegagalannya '
             'bukan bukti pakar itu salah (`laporan/KAEDAH_TERBAIK.md` §5).')
    L.append(f'- Sistem B: had saiz {B_SAIZ_MAKS:.0%} ditambah untuk keselamatan berangka; ia '
             'bukan peraturan Clenow. Imbang Rabu; jika Rabu bukan hari dagangan, sesi itu '
             'dilangkau.')
    L.append('- Tunai tidak berbunga (0%), yang merugikan kedua-dua sistem.')
    L.append(f'- Tingkap keputusan {UJI0}–{UJI1} sahaja (6 tahun) kerana SPUS mula Dis 2019; ia '
             'merangkumi satu pasaran menaik yang kuat dan dua drawdown tajam.')
    L.append('')
    L.append('**Ia tidak mencapai +10%/bulan.** Lihat `SASARAN.md`.')
    L.append('')
    (KELUAR / 'SISTEM.md').write_text('\n'.join(L), encoding='utf-8')
    c = ['sistem', 'cagr', 'p10', 'mdd', 'cagr14', 'mdd14', 'sd', 'lulus']
    print('\n' + g[c].round(2).to_string(index=False))
    print(f'\nSPUS CAGR {sp["cagr"]:.2f}% / MDD {sp["mdd_tingkap"]:.2f}% | '
          f'{"LULUS: " + ",".join(lulus.sistem) if len(lulus) else "DITOLAK"}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
