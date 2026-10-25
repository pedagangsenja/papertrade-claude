# playbook.py — peraturan pemilihan "playbook" sebagai satu kaedah kajian PIT (pra-daftar PRA_DAFTAR.md §3).
# Antara muka sama dengan kod/kaedah/Mxx.py (ID, NAMA, VARIAN, TMAX, WARM, ADA_HENTI, SILANG, PERLU_BAR, sedia(fr, idx)).
# Isyarat hari i jika SEMUA benar (hanya data <= i):
#   1. RS 80–94: persentil 1–99 skor IBD 40/20/20/20 (standard/rs_pasaran.py) merentas SELURUH pasaran dalam data.
#      Harness memberi idx['_rs'] (DataFrame tarikh x ticker, dibina alam.bina_cache). Tanpa idx['_rs'] (cth. ujian),
#      RS dipangkat antara saham dalam fr dengan tutup >= USD5 dan >= 253 bar.
#   2. Trend Template S1–S6 (kod/kaedah/M74.py): tutup > SMA150 & SMA200; SMA150 > SMA200; SMA200 > SMA200 21 sesi lalu;
#      SMA50 > SMA150 & SMA200; tutup > SMA50; tutup >= 1.30 x rendah 252 sesi.
#   3. tutup >= 0.85 x tinggi 252 sesi (<= 15% dari tinggi 52 minggu).
#   4. ATR14 (purata mudah TR, enjin.atr) / tutup <= 6%.
# Masuk buka esok; tiada henti/sasaran; keluar tutup hari pegang ke-21 (TMAX); rank = skor RS mentah.
import numpy as np
import pandas as pd

ID = 'PLAYBOOK'
NAMA = 'Playbook: RS 80–94 + Trend Template + <= 15% dari tinggi 52 minggu + ATR14% <= 6%'
VARIAN = 'P1 pegang 21 hari (tanpa henti)'
TMAX = 21
WARM = 260
ADA_HENTI = False
SILANG = True
PERLU_BAR = 260
PERLU_RS = True
RS_BAWAH, RS_ATAS = 80, 94
JARAK_TINGGI = 0.85
ATR_MAKS = 0.06


def _atr(g, n=14):
    c = g.close
    tr = pd.concat([g.high - g.low, (g.high - c.shift()).abs(), (g.low - c.shift()).abs()], axis=1).max(axis=1)
    return tr.rolling(n).mean()


def _skor(c):
    q = [c.shift(k) for k in (63, 126, 189, 252)]
    s = 0.4 * (c / q[0] - 1) + 0.2 * (q[0] / q[1] - 1) + 0.2 * (q[1] / q[2] - 1) + 0.2 * (q[2] / q[3] - 1)
    return s.replace([np.inf, -np.inf], np.nan)


def sedia(fr, idx):
    rs = idx.get('_rs') if isinstance(idx, dict) else None
    sk_pasaran = idx.get('_rs_skor') if isinstance(idx, dict) else None
    if rs is None:
        S = {}
        for t, g in fr.items():
            ok = (g.close >= 5) & (np.arange(len(g)) + 1 >= 253)
            S[t] = _skor(g.close).where(ok)
        S = pd.DataFrame(S)
        rs = (S.rank(axis=1, pct=True) * 98 + 1).round(); sk_pasaran = S
    for t, g in fr.items():
        c = g.close
        s50 = c.rolling(50).mean(); s150 = c.rolling(150).mean(); s200 = c.rolling(200).mean()
        h252 = g.high.rolling(252).max(); l252 = g.low.rolling(252).min()
        tt = ((c > s150) & (c > s200) & (s150 > s200) & (s200 > s200.shift(21)) & (s50 > s150) & (s50 > s200) & (c > s50)
              & (c >= 1.30 * l252))
        r = rs[t].reindex(g.index) if t in rs.columns else pd.Series(np.nan, index=g.index)
        sk = sk_pasaran[t].reindex(g.index) if (sk_pasaran is not None and t in sk_pasaran.columns) else _skor(c)
        atrp = _atr(g) / c
        g['_rs'] = r; g['_tt'] = tt; g['_atrp'] = atrp
        g['sig'] = (tt & (r >= RS_BAWAH) & (r <= RS_ATAS) & (c >= JARAK_TINGGI * h252) & (atrp <= ATR_MAKS)).fillna(False)
        g['stop'] = np.nan
        g['tgt'] = np.nan
        g['exitc'] = False
        g['rank'] = sk.fillna(0.0)
