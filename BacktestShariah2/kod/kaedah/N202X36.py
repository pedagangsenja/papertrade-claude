"""N202X36 = RSI2<10 dalam trend naik x X36 - kohort KOMBINASI MA50 (jejak hadapan sejak isyarat 2026-11-12).

Pradaftar `BacktestShariah2/kajian/SPEC_JEJAK_KOMBINASI.md` · tinjauan
`BacktestShariah2/kajian/KAJIAN_ISYARAT_KOMBINASI.md` · keputusan pengguna 12 Nov 2026
(`koordinator/keputusan.csv`).

MASUK  : rsi2 < 10 DAN tutup > ma200 DAN tutup > ma50
KELUAR : lorong 1 = X36 (keluar selepas DUA tutup bawah ma50)
         lorong 2 = X15 Chandelier tutup 4xATR14 (automatik, setiap posisi)
CARA   : C01 beli pada BUKA esok · HENTI TIADA · SASARAN TIADA · TMAX 126
URUTAN : rank = U14 momentum 12-1

TINJAUAN (431 saham, isyarat 2020-01..2026-03, kos 0.5%, keluar X36 tanpa henti; setiap hari
isyarat dikira, jadi bertindih - enjin produksi hanya ambil yang pertama):
  jangkaan +1.76%  ·  2020-22 +1.20%  ·  2023-26 +2.17%  ·  menang 32.1%  ·  n 13,987
  498 saham lain (isyarat 2025-09..2026-08): +1.62% (n 886)
  rujukan sama cara: mana-mana hari tutup > ma50 (= N76X36) +2.01%, saham lain +0.90%

STATUS: CALON, BUKAN bukti. ~1.35 juta gabungan diuji; yang lulus tapis tidak lebih baik pada
saham lain berbanding gabungan rawak. Jejak ini ujian pertama yang jujur.
HAD: jangkaan SETIAP DAGANGAN, bukan prestasi portfolio; alam tinjauan tiada saham delist.
"""
try:
    from kaedah import _kombo as KB
except ImportError:
    import _kombo as KB

ID = 'N202X36'
NAMA = 'RSI2<10 dalam trend naik x X36'
VARIAN = 'V1 kombinasi MA50'
TMAX = KB.NX.IMBAS
WARM = 200
ADA_HENTI = False
SILANG = False
PERLU_BAR = 300


def sedia(fr, idx):
    for g in fr.values():
        KB.pasang(g, 'n202')


def hampir(g, idx):
    """Calon watchlist: syarat masuk yang sebahagiannya sudah dipenuhi (`paras` None)."""
    return KB.hampir(g, 'n202', PERLU_BAR)
