# Setup F: prasyarat (pasaran) lawan syarat (saham itu sendiri)

> **Status keputusan (kad skor, harga 2026-11-12):** TERBUKTI 0 · CALON 0 · BELUM CUKUP 223 · GAGAL 0 · NEGATIF 0. Rejim QQQ OFF sejak 2026-10-16. Hanya **TERBUKTI** layak untuk wang sebenar (`laporan/KAD_SKOR.md`); nombor dalam laporan ini BUKAN keputusan dan tidak boleh dibaca sebagai pangkat untuk wang sebenar.

Dijana `kajian/carian_setup/cs_ringkas.py` daripada `data/registry_F.csv` dan `jejak_f/kohort.json`. **Jangan sunting secara manual.**

Prasyarat = isyarat yang BUKAN daripada saham itu sendiri. Ruang carian CS01–CS04 hanya ada tiga: **QQQ ON** (QQQ di atas SMA50 dan SMA10 di atas SMA20), **QQQ OFF** (selain itu) dan **SPY > SMA200**. RS diletak di bawah syarat saham (dikira daripada harga saham itu, dipangkatkan lawan saham lain).

Bilangan: – = 20 · QQQ OFF = 14 · QQQ ON = 2 · SPY > SMA200 = 2 (jumlah 38).

| ID | Pusingan | Prasyarat (pasaran) | Syarat saham: pencetus | Syarat saham: penapis | Henti | Keluar | Jejak hadapan |
|---|---|---|---|---|---|---|---|
| F01 | CS01 | – | N203 | Supertrend naik + ATR% >= 4 | H4 4xATR14 | X03 tutup < MA50 DAN X22 hari turun dengan volum >= 1.5x |  |
| F02 | CS01 | QQQ OFF | M111 Sistem Volatiliti Wilder (ditala 2) | >= 30% di bawah puncak 52 minggu | H4 4xATR14 | X08 MA10 < MA20 DAN X22 hari turun dengan volum >= 1.5x |  |
| F03 | CS01 | – | M01 Bollinger Band + RSI (ditala 2) | RS >= 70 + >= 30% di bawah puncak 52 minggu | H4 4xATR14 | X20 tutup < 92% tutup tertinggi sejak beli DAN X21 Stochastic silang turun di atas 80 |  |
| F04 | CS01 | QQQ OFF | M79 Radge: 20% Flipper (ditala 1) | volum hari isyarat >= 1.5x purata 50 | H4 4xATR14 | X12 RSI14 silang turun bawah 70 DAN X20 tutup < 92% tutup tertinggi sejak beli |  |
| F05 | CS01 | – | P07 MA20 silang atas MA50 | Supertrend naik + ATR% >= 4 | H4 4xATR14 | X14 Supertrend turun DAN X22 hari turun dengan volum >= 1.5x |  |
| F06 | CS01 | – | N07 Tiga MA tersusun | ADX < 20 + ATR% >= 4 | H4 4xATR14 | X18 Chandelier 3xATR14 (dari tutup tertinggi sejak beli) DAN X22 hari turun dengan volum >= 1.5x |  |
| F07 | CS01 | QQQ OFF | M30 BB Free Bar + Himpitan 50/2.5 | ATR% >= 4 | H4 4xATR14 | X13 RSI14 > 80 |  |
| F08 | CS01 | – | N201 | Supertrend naik + ATR% >= 4 | H4 4xATR14 | X18 Chandelier 3xATR14 (dari tutup tertinggi sejak beli) DAN X22 hari turun dengan volum >= 1.5x |  |
| F09 | CS01 | – | M140 猎豹出击 (Serangan Cheetah) (ditala 1) | ATR% >= 4 + hari naik (tutup > buka) | H4 4xATR14 | X14 Supertrend turun DAN X22 hari turun dengan volum >= 1.5x |  |
| F10 | CS01 | – | P16 RSI2<5 atas MA200 | volum hari isyarat >= 1.5x purata 50 + ATR% >= 4 | H3 3xATR14 | X12 RSI14 silang turun bawah 70 ATAU X19 Chandelier 2xATR14 |  |
| F11 | CS02 | QQQ OFF | M01 Bollinger Band + RSI (ditala 2) | >= 30% di bawah puncak 52 minggu | H4 4xATR14 | X04 tutup < EMA10 DAN X12 RSI14 silang turun bawah 70 |  |
| F12 | CS02 | QQQ OFF | M88 O'Neil Shakeout +3 (ditala 1) | >= 30% di bawah puncak 52 minggu | H4 4xATR14 | X12 RSI14 silang turun bawah 70 ATAU X13 RSI14 > 80 |  |
| F13 | CS02 | QQQ OFF | M02 MACD + SMA200 | RSI14 > 60 | H4 4xATR14 | X08 MA10 < MA20 DAN X20 tutup < 92% tutup tertinggi sejak beli |  |
| F14 | CS02 | QQQ OFF | N28 ADX>25 + DI+ > DI- | >= 30% di bawah puncak 52 minggu | H4 4xATR14 | X09 MACD < isyarat DAN X21 Stochastic silang turun di atas 80 |  |
| F15 | CS02 | QQQ OFF | M73 ADX(5) > 40 + Julat Terkecil 6 Hari (ditala 1) | >= 30% di bawah puncak 52 minggu | H4 4xATR14 | X04 tutup < EMA10 DAN X12 RSI14 silang turun bawah 70 |  |
| F16 | CS02 | – | N38 VCP pecah | ATR% >= 4 + tutup dalam 25% teratas julat hari | H4 4xATR14 | X21 Stochastic silang turun di atas 80 DAN X22 hari turun dengan volum >= 1.5x |  |
| F17 | CS02 | QQQ OFF | P14 RSI14 silang atas 30 | >= 30% di bawah puncak 52 minggu | H4 4xATR14 | X13 RSI14 > 80 |  |
| F18 | CS02 | QQQ OFF | N75 RSI14 < 40 tanpa penapis | >= 30% di bawah puncak 52 minggu | H4 4xATR14 | X13 RSI14 > 80 DAN X21 Stochastic silang turun di atas 80 |  |
| F19 | CS02 | QQQ OFF | P02 MACD silang naik bawah sifar | RSI14 > 60 | H4 4xATR14 | X14 Supertrend turun DAN X23 tutup < buka dan < rendah semalam |  |
| F20 | CS02 | QQQ OFF | M141 First Thrust (Landry) (ditala 1) | MACD > isyarat | H4 4xATR14 | X18 Chandelier 3xATR14 (dari tutup tertinggi sejak beli) DAN X22 hari turun dengan volum >= 1.5x |  |
| F21 | CS03 | – | N40 OBV tinggi baharu + MA50 | tutup > MA200 + >= 30% di bawah puncak 52 minggu | H2 -10% | X09 MACD < isyarat ATAU X10 histogram MACD turun 3 hari | ya |
| F22 | CS03 | QQQ ON | M84 Jarak purata bergerak MAD 21/200 (ditala 1) | ATR% >= 4 | H2 -10% | X11 RSI14 < 50 ATAU X21 Stochastic silang turun di atas 80 | ya |
| F23 | CS03 | SPY > SMA200 | M21 Marius 3 Persediaan (Pecahan+Jurang+Kesinambungan) | RS >= 90 | H2 -10% | X12 RSI14 silang turun bawah 70 DAN X16 tutup < rendah 5 hari |  |
| F24 | CS03 | – | M49 Ichimoku (Tutup Atas Awan + Tenkan Silang Kijun) (ditala 2) | RS >= 90 + ATR% >= 4 | H4 4xATR14 | X11 RSI14 < 50 DAN X22 hari turun dengan volum >= 1.5x | ya |
| F25 | CS03 | – | M57 Landry Trend Knockout (TKO) (ditala 1) | RS >= 90 + ATR% >= 4 | H4 4xATR14 | X22 hari turun dengan volum >= 1.5x DAN X24 +DI < -DI |  |
| F26 | CS03 | – | M50 Elder Triple Screen (ditala 2) | RS >= 90 + ATR% >= 4 | H4 4xATR14 | X12 RSI14 silang turun bawah 70 ATAU X22 hari turun dengan volum >= 1.5x |  |
| F27 | CS03 | – | N73 Tutup bawah jalur bawah BB(20,2) | RS >= 70 + ATR% >= 4 | H4 4xATR14 | X07 dua tutup berturut < MA20 DAN X21 Stochastic silang turun di atas 80 | ya |
| F28 | CS03 | QQQ OFF | M92 CCI-50 (ditala 2) | >= 30% di bawah puncak 52 minggu | H4 4xATR14 | X20 tutup < 92% tutup tertinggi sejak beli DAN X21 Stochastic silang turun di atas 80 | ya |
| F29 | CS03 | – | P13 RSI14 silang atas 60 | RS >= 90 + ATR% >= 4 | H2 -10% | X21 Stochastic silang turun di atas 80 DAN X22 hari turun dengan volum >= 1.5x |  |
| F30 | CS03 | – | N43 Undur EMA8 + penapis MA50 | Supertrend naik + ATR% >= 4 | H4 4xATR14 | X21 Stochastic silang turun di atas 80 DAN X22 hari turun dengan volum >= 1.5x | ya |
| F31 | CS04 | – | N40 OBV tinggi baharu + MA50 | tutup > MA200 + >= 20% di bawah puncak 52 minggu | H2 -10% | X09 MACD < isyarat ATAU X10 histogram MACD turun 3 hari |  |
| F32 | CS04 | QQQ ON | M84 Jarak purata bergerak MAD 21/200 | ATR% >= 4 | H3 3xATR14 | X11 RSI14 < 50 ATAU X21 Stochastic silang turun di atas 80 |  |
| F33 | CS04 | SPY > SMA200 | M21 Marius 3 Persediaan (Pecahan+Jurang+Kesinambungan) | RS >= 95 | H2 -10% | X13 RSI14 > 80 ATAU X21 Stochastic silang turun di atas 80 |  |
| F34 | CS04 | – | M49 Ichimoku (Tutup Atas Awan + Tenkan Silang Kijun) | RS >= 95 + ATR% >= 4 | H4 4xATR14 | X21 Stochastic silang turun di atas 80 ATAU X22 hari turun dengan volum >= 1.5x | ya |
| F35 | CS04 | – | M57 Landry Trend Knockout (TKO) | RS >= 95 + ATR% >= 4 | H4 4xATR14 | X08 MA10 < MA20 DAN X24 +DI < -DI |  |
| F36 | CS04 | – | M50 Elder Triple Screen (ditala 2) | RS >= 95 + ATR% >= 6 | H4 4xATR14 | X12 RSI14 silang turun bawah 70 ATAU X21 Stochastic silang turun di atas 80 |  |
| F37 | CS04 | QQQ OFF | M92 CCI-50 (ditala 2) | >= 20% di bawah puncak 52 minggu | H4 4xATR14 | X20 tutup < 92% tutup tertinggi sejak beli DAN X21 Stochastic silang turun di atas 80 |  |
| F38 | CS04 | – | P13 RSI14 silang atas 60 [tala daripada F29] | RS >= 95 + ATR% >= 4 | H2 -10% | X14 Supertrend turun ATAU X18 Chandelier 3xATR14 (dari tutup tertinggi sejak beli) | ya |

## Kaveat

- `F23`/`F33` (benih M21) memakai harga SPY di dalam peraturan kaedah itu sendiri, selain prasyarat SPY > SMA200. Kaedah M lain belum diperiksa satu per satu pada tahap ini.
- Prasyarat lain (keluasan, turun-naik, sektor, industri, earnings, kalendar) BELUM ada dalam ruang carian; ukurannya dalam `LAPORAN.md` folder ini (pindaan (h)).
