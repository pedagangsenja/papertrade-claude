"""Kohort KOMBINASI MA50 (N201-N204) - topeng masuk bagi jejak hadapan 12 Nov 2026.

Sumber: `BacktestShariah2/kajian/KAJIAN_ISYARAT_KOMBINASI.md` (tinjauan 11-12 Nov 2026) dan
pradaftar `BacktestShariah2/kajian/SPEC_JEJAK_KOMBINASI.md`. Formula di sini ialah salinan
VERBATIM formula tinjauan (`kajian/isyarat_kombinasi/panel.py`), BUKAN formula `_nxx.py`:
RSI tinjauan ialah `ewm(alpha=1/n, adjust=False, min_periods=n)` tanpa benih purata-n,
sedangkan `_nxx._wilder` berbenih. Menukar kepada `_nxx` akan menjejak peraturan yang lain
daripada yang diukur. `ujian/test_kombo_ma50.py` mengunci pariti dan ketiadaan pandang-hadapan.

STATUS BUKTI (baca sebelum memetik): tinjauan menguji ~1.35 juta gabungan; gabungan yang lulus
tapis pada set utama TIDAK lebih baik pada 498 saham lain berbanding gabungan dipilih rawak.
Empat kaedah ini ialah CALON yang tidak dapat dibezakan daripada nasib. Jejak hadapan ini
ialah ujian pertama yang jujur, bukan pengesahan.

Semua masuk mewajibkan `tutup > ma50` pada bar isyarat. Keluar lorong 1 = `X36` (dua tutup
berturut di bawah ma50) melalui `_nxx.pasang`, TANPA henti dan TANPA sasaran - sama seperti 94
kohort Nxx, supaya gate G4 kad skor (henti hari-0 sifar secara struktur) terpakai sama rata.
"""
import collections

import numpy as np
import pandas as pd

try:
    from kaedah import _nxx as NX
except ImportError:
    import _nxx as NX

KELUAR = 'X36'
GAP_MIN = 1.02          # buka > tinggi semalam x 1.02
TINGKAP_GAP = 10        # N203: gap dalam 10 bar terakhir (termasuk hari ini)
TINGKAP_LANGKAH = 5     # N204: setiap langkah dalam 5 bar selepas langkah sebelumnya
MULA_LANGSUNG = '2026-11-12'   # tarikh isyarat pertama yang dikira langsung (SPEC_KAD_SKOR pindaan 12 Nov 2026)
KOHORT = ('N201X36', 'N202X36', 'N203X36', 'N204X36')


def _wilder(s, n):
    return s.ewm(alpha=1 / n, adjust=False, min_periods=n).mean()


def _rsi(c, n):
    d = c.diff()
    naik, turun = _wilder(d.clip(lower=0), n), _wilder((-d).clip(lower=0), n)
    return 100 - 100 / (1 + naik / turun.replace(0, np.nan))


def _silang(a, b):
    return (a > b) & (a.shift() <= b.shift())


def _dalam(ev, n):
    """Benar jika `ev` benar pada mana-mana daripada `n` bar terakhir, TERMASUK bar ini."""
    return ev.fillna(False).astype(float).rolling(n, min_periods=1).max() > 0


_MEMO = collections.OrderedDict()   # sama corak dengan `_nxx._MEMO`: kunci = cap jari bait OHLCV + indeks
_MEMO_MAKS = 4096


def asas(g):
    """Lajur yang empat topeng perlukan. Hanya data <= bar semasa (tiada shift negatif).

    Dimemo ikut `_nxx._cap(g)`: empat modul memanggilnya bagi setiap ticker dalam `sedia()` dan
    sekali lagi dalam `hampir()`; tanpa memo imbasan produksi mengira set yang sama lapan kali.
    Salinan dipulangkan supaya pemanggil tidak boleh mencemarkan entri cache.
    """
    k = NX._cap(g)
    d = _MEMO.get(k)
    if d is None:
        d = _asas(g)
        _MEMO[k] = d
        if len(_MEMO) > _MEMO_MAKS:
            _MEMO.popitem(last=False)
    else:
        _MEMO.move_to_end(k)
    return d.copy()


def _asas(g):
    """Pengiraan sebenar; asas() ialah pembalut memo."""
    o, h, c = g.open, g.high, g.close
    d = pd.DataFrame(index=g.index)
    d['ma20'] = c.rolling(20).mean()
    d['ma50'] = c.rolling(50).mean()
    d['ma200'] = c.rolling(200).mean()
    d['rsi2'] = _rsi(c, 2)
    d['rsi14'] = _rsi(c, 14)
    d['atas50'] = c > d.ma50
    d['gap'] = o > h.shift(1) * GAP_MIN
    d['silang2050'] = _silang(d.ma20, d.ma50)
    d['silang_rsi50'] = _silang(d.rsi14, pd.Series(50.0, index=g.index))
    d['undur'] = (d.rsi2 < 10) & (d.rsi2.shift() >= 10)
    return d


def n201(d, g):
    """MA20 silang atas MA50, tutup > MA50."""
    return d.silang2050 & d.atas50


def n202(d, g):
    """RSI2 < 10 dalam trend naik: tutup > MA200 dan tutup > MA50 (beli masa undur)."""
    return (d.rsi2 < 10) & (g.close > d.ma200) & d.atas50


def n203(d, g):
    """Gap naik 2% dalam 10 bar terakhir, kemudian MA20 silang atas MA50; tutup > MA50."""
    return d.silang2050 & _dalam(d.gap, TINGKAP_GAP) & d.atas50


def n204(d, g):
    """Undur RSI2<10 -> gap naik 2% (dalam 5 bar) -> RSI14 silang atas 50 (dalam 5 bar); tutup > MA50."""
    langkah2 = d.gap & _dalam(d.undur, TINGKAP_LANGKAH)
    return d.silang_rsi50 & _dalam(langkah2, TINGKAP_LANGKAH) & d.atas50


TOPENG = {'n201': n201, 'n202': n202, 'n203': n203, 'n204': n204}


def _p(a, b, g):
    return (b - a).abs() / g.close.abs().replace(0, float('nan')) * 100.0


# Penguraian kepada syarat atom untuk watchlist "hampir". DAN semua syarat = topeng (dikunci ujian).
SYARAT = {
    'n201': lambda d, g: [('tutup > ma50', d.atas50, _p(g.close, d.ma50, g)),
                          ('ma20 silang atas ma50', d.silang2050, _p(d.ma20, d.ma50, g))],
    'n202': lambda d, g: [('tutup > ma50', d.atas50, _p(g.close, d.ma50, g)),
                          ('tutup > ma200', g.close > d.ma200, _p(g.close, d.ma200, g)),
                          ('rsi2 < 10', d.rsi2 < 10, d.rsi2 - 10)],
    'n203': lambda d, g: [('tutup > ma50', d.atas50, _p(g.close, d.ma50, g)),
                          ('gap naik 2% dalam 10 hari', _dalam(d.gap, TINGKAP_GAP), None),
                          ('ma20 silang atas ma50', d.silang2050, _p(d.ma20, d.ma50, g))],
    'n204': lambda d, g: [('tutup > ma50', d.atas50, _p(g.close, d.ma50, g)),
                          ('undur rsi2<10 kemudian gap 2%', _dalam(d.gap & _dalam(d.undur, TINGKAP_LANGKAH), TINGKAP_LANGKAH), None),
                          ('rsi14 silang atas 50', d.silang_rsi50, 50 - d.rsi14)],
}


def pasang(g, nama):
    """Tulis lajur enjin: sig = topeng, keluar X36, stop/tgt NaN, rank U14 (melalui `_nxx.pasang`)."""
    f = NX.indikator(g)
    d = asas(g)
    NX.pasang(g, TOPENG[nama](d, g), f, keluar=KELUAR)
    g['_rsi14'] = d.rsi14
    return d


def hampir(g, nama, cukup):
    """Calon watchlist: sebahagian syarat sudah dipenuhi. `paras` None (ambang indikator)."""
    d = asas(g)
    out = []
    for label, kon, jar in SYARAT[nama](d, g):
        ok = bool(kon.iloc[-1])
        j = None
        if jar is not None and not ok:
            v = jar.iloc[-1]
            j = None if v != v else abs(float(v))
        out.append((label, ok, j))
    return NX.hampir_syarat(out, len(g), cukup)
