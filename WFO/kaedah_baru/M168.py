# M168 — Pulih MACD + Silang SMA10/20: teknik manual pengguna (DCI dan MGA, akaun Moomoo lama, 6 Okt 2026).
# Spec: spec/SPEC_SEMUA_KAEDAH.md (tanda `FAIL ASAL: spec/M168.md`); jawapan pengguna 25 Okt 2026; 00_NOTA_SERAHAN.md §6 item 5.
# Backtest STEP-2: WFO/kaedah_baru/step2_M168.py -> BacktestShariah2/kod/registry/M168.csv; laporan BacktestShariah2/laporan/M168.md.
#
# MORATORIUM (25 Okt 2026): kaedah baharu belum diaktifkan tanpa keputusan pengguna. Modul ini SENGAJA di luar
# BacktestShariah2/kod/kaedah/ (seperti calon K145+ dan M162–M167; WFO/kaedah_baru/README.md): scanner.py, standard/harian_c.py,
# standard/lejar.py serta katalog/Papan Penganalisis membaca semua kod/kaedah/M*.py. Antara muka sudah ikut kod/ANTARAMUKA.md;
# mengaktifkan = pindah ke kod/kaedah/M168.py + langkah dalam laporan/M168.md bahagian "Mengaktifkan M168".
from enjin import rsi, atr
import math
import pandas as pd, numpy as np

ID = 'M168'
NAMA = 'Pulih MACD + Silang SMA10/20 (teknik manual pengguna)'
VARIAN = 'V1 Utama J20 D10 K10 (tiada henti)'
TMAX = None
WARM = 200
ADA_HENTI = False
SILANG = False
PERLU_BAR = 150          # EMA26 + isyarat 9 (MACD) perlu ~100 bar untuk menumpu; tetingkap jatuh maks 45 + tinggi 60 hari

# ---------------------------------------------------------------- varian (grid STEP-2)
# mod: 'penuh' = alert MACD selepas fasa jatuh + silang SMA10/20; 'alert' = alert + silang (tanpa syarat jatuh);
#      'silang' = silang SMA10/20 sahaja (kawalan).
# J  = bilangan minimum hari SMA10 < SMA20 dalam tetingkap W = ceil(1.5 x J) hari dagangan berakhir pada hari alert
#      (3/4/6 minggu = 15/20/30 hari).
# D  = tutup hari alert sekurang-kurangnya D di bawah tinggi 60 hari (maks high 60 bar hingga hari alert).
# K  = silang SMA10 atas SMA20 mesti berlaku 0..K hari dagangan selepas alert yang layak.
# henti = henti kecemasan 0.99 x rendah terendah fasa jatuh (kepekaan sahaja; pengguna tidak menyatakan henti).
_GRID_J, _GRID_D, _GRID_K = (15, 20, 30), (0.10, 0.15, 0.20), (10, 20)


def _nama_grid(J, D, K):
    return f'J{J} D{int(round(D * 100))} K{K}'


def _bina_varian():
    v = {'V0a Kawalan silang SMA10/20 sahaja': dict(mod='silang', J=None, D=None, K=None, henti=False),
         'V0b Kawalan alert MACD + silang K10 (tanpa syarat jatuh)': dict(mod='alert', J=None, D=None, K=10, henti=False)}
    utama = (20, 0.10, 10)
    susun = [utama] + [(J, D, K) for J in _GRID_J for D in _GRID_D for K in _GRID_K if (J, D, K) != utama]
    for n, (J, D, K) in enumerate(susun, 1):
        asas = f'V{n} ' + ('Utama ' if n == 1 else '') + _nama_grid(J, D, K)
        v[asas + ' (tiada henti)'] = dict(mod='penuh', J=J, D=D, K=K, henti=False)
        v[f'V{n}H ' + ('Utama ' if n == 1 else '') + _nama_grid(J, D, K) + ' + henti kecemasan'] = \
            dict(mod='penuh', J=J, D=D, K=K, henti=True)
    return v


VARIAN_SEMUA = _bina_varian()


def tetingkap(J):
    """Tetingkap kiraan fasa jatuh (hari dagangan) bagi J hari minimum SMA10 < SMA20."""
    return int(math.ceil(1.5 * J))


def penunjuk(g):
    """SMA10/SMA20 tutup, histogram MACD(12,26,9) (EMA adjust=False seperti M02), tinggi 60 hari. Nilai hari i guna data <= i."""
    c = g.close
    s10, s20 = c.rolling(10).mean(), c.rolling(20).mean()
    m = c.ewm(span=12, adjust=False).mean() - c.ewm(span=26, adjust=False).mean()
    hist = m - m.ewm(span=9, adjust=False).mean()
    return s10, s20, hist, g.high.rolling(60).max()


def _henti_kecemasan(low, sig, a_akhir, W):
    """henti hari isyarat b = 0.99 x min(low[a - W + 1 .. b]); a = alert layak terkini (fasa jatuh + selepasnya hingga b)."""
    st = np.full(len(low), np.nan)
    for b in np.flatnonzero(sig):
        a = int(a_akhir[b]); mula = max(0, a - W + 1)
        st[b] = 0.99 * np.nanmin(low[mula:b + 1])
    return st


def sedia(fr, idx, varian=None):
    """Isi sig/stop/tgt/exitc/rank (ubah di tempat). varian: kunci VARIAN_SEMUA (lalai VARIAN modul; backtest STEP-2 sahaja).
       Tanpa pandang ke hadapan: nilai hari i guna data <= i (kecuali langkau 'buka esok <= henti' varian H, konvensyen enjin)."""
    p = VARIAN_SEMUA[varian or VARIAN]
    for g in fr.values():
        o, l, c = g.open, g.low, g.close
        s10, s20, hist, h60 = penunjuk(g)
        naik = (s10 > s20) & (s10.shift() <= s20.shift())          # silang atas (tutup hari i)
        turun = (s10 < s20) & (s10.shift() >= s20.shift())         # silang bawah -> jual buka esok
        alert = (hist > 0) & (hist.shift() <= 0)                    # histogram MACD negatif -> positif
        stop = pd.Series(np.nan, g.index)
        if p['mod'] == 'silang':
            sig = naik
        else:
            if p['mod'] == 'alert':
                qa = alert
            else:
                W = tetingkap(p['J'])
                bawah = (s10 < s20).astype(float).where(s10.notna() & s20.notna())
                jatuh = bawah.rolling(W).sum() >= p['J']
                dalam = c <= (1 - p['D']) * h60
                qa = alert & jatuh & dalam
            # Andaian saya: silang pada hari alert sendiri dikira (0 hari selepas alert); mana-mana silang dalam K hari layak
            baru = qa.astype(float).rolling(p['K'] + 1, min_periods=1).max() > 0
            sig = naik & baru
            if p['henti']:
                pos = pd.Series(np.where(qa.values, np.arange(len(g)), np.nan), g.index).ffill()
                sv = sig.fillna(False).values & pos.notna().values
                stop = pd.Series(_henti_kecemasan(l.values.astype(float), sv, np.nan_to_num(pos.values), tetingkap(p['J'])),
                                 g.index)
                # konvensyen projek: langkau jika buka esok <= henti (bar terakhir: buka esok belum diketahui -> dikekalkan)
                bm = o.shift(-1)
                sig = sig & ((bm > stop) | bm.isna())
            g['_qa'] = qa.fillna(False)
        sig = sig.fillna(False).astype(bool)
        g['_s10'] = s10; g['_s20'] = s20; g['_hist'] = hist; g['_h60'] = h60
        g['sig'] = sig
        g['stop'] = stop
        g['tgt'] = np.nan
        g['exitc'] = turun.fillna(False).astype(bool)
        g['rank'] = c / c.shift(63) - 1                             # ROC63, kunci keutamaan slot (konvensyen projek)


def paras_silang_bawah(g):
    """Tutup sesi berikutnya x yang menjadikan SMA10 < SMA20 (algebra tepat): x < S20' - 2 S10', dengan S10' = jumlah 9 tutup
       terakhir dan S20' = jumlah 19 tutup terakhir. Pulang None jika data < 20 bar. Dipakai untuk nota posisi manual."""
    c = g.close.values.astype(float)
    if len(c) < 20:
        return None
    return float(c[-19:].sum() - 2 * c[-9:].sum())


def hampir(g, idx):
    """Belum ditakrif (konvensyen K145+ M115 dan ke atas; ujian/test_katalog_kod.py mensyaratkan hampir() kosong bagi ID >= 115).
       Calon 'hampir' semula jadi untuk M168 = alert MACD layak sudah berlaku <= K hari lepas dan SMA10 masih <= SMA20; ditangguh."""
    return None
