# CS03: SEMUA pencetus (kaedah M, N dan indikator) ikut kadar tangkap — asas "syarat sahaja" (backtest, BUKAN bukti)

> **Status keputusan (kad skor, harga 2026-11-12):** TERBUKTI 0 · CALON 0 · BELUM CUKUP 223 · GAGAL 0 · NEGATIF 0. Rejim QQQ OFF sejak 2026-10-16. Hanya **TERBUKTI** layak untuk wang sebenar (`laporan/KAD_SKOR.md`); nombor dalam laporan ini BUKAN keputusan dan tidak boleh dibaca sebagai pangkat untuk wang sebenar.

Dijana `kajian/carian_setup/cs_tangkap.py <kerja> semua`. **Jangan sunting secara manual.**

Setiap baris = satu pencetus (benih M asal `.0` dan dua varian parameter `.1`/`.2`, benih N, indikator `Pxx`). 500 pencetus; 465 cukup isyarat (≥ 100 dalam setiap era); 182,903 peraturan masuk (pencetus × 0–2 penapis) diskor, semuanya dalam `semua_masuk.csv.gz`.

**Angka di sini daripada KUMPULAN A (separuh yang DICARI; E1 = 2010–2019, E2 = 2020–2024), jadi condong ke atas.** Hanya 200 teratas + 200 rawak disahkan pada kumpulan B (`senarai_kunci.csv`, `TOP50.md`). Guna jadual ini sebagai ASAS: apa yang setiap kaedah capai dengan syarat saham sahaja, untuk dibandingkan dengan larian berprasyarat.

"Lebih lari" = kadar lari isyarat tolak kadar saham rawak hari sama × tercile ATR% sama, dalam mata peratus, tanpa sebarang penapis. "Skor" = min dua era bagi (lebihan lari − 2 ralat piawai), mata peratus; > 0 bermakna lebihan itu melepasi ralat dalam KEDUA-DUA era. "Syarat sahaja" = penapis saham; "dengan prasyarat" = sekurang-kurangnya satu daripada QQQ ON / QQQ OFF / SPY > SMA200.

| # | Pencetus | Isyarat E1 / E2 | Lebih lari tanpa penapis E1 / E2 | Skor terbaik: syarat sahaja | Penapis | Skor terbaik: dengan prasyarat | Penapis |
|---|---|---|---|---|---|---|---|
| 1 | M50 Elder Triple Screen (ditala 1) | 76,301 / 51,912 | -0.12 / +0.16 | +2.43 | RS >= 90 + ATR% >= 4 | +0.28 | RS >= 90 + SPY > SMA200 |
| 2 | P45 pemimpin undur ke MA20 | 21,199 / 12,435 | +0.31 / +0.87 | +2.22 | RS >= 90 + ATR% >= 4 | +1.34 | ATR% >= 4 + rejim QQQ ON |
| 3 | N40 OBV tinggi baharu + MA50 | 41,794 / 26,051 | +0.13 / +0.15 | +2.16 | tutup > MA200 + >= 30% di bawah puncak 52 minggu | +0.56 | >= 30% di bawah puncak 52 minggu + SPY > SMA200 |
| 4 | M18 EMA9/21 Pullback (ditala 2) | 58,107 / 41,282 | -0.11 / +0.17 | +2.04 | RS >= 90 + ATR% >= 4 | +0.87 | RS >= 90 + SPY > SMA200 |
| 5 | M49 Ichimoku (Tutup Atas Awan + Tenkan Silang Kijun) (ditala 2) | 36,412 / 23,652 | -0.08 / +0.37 | +2.01 | RS >= 90 + ATR% >= 4 | +0.67 | RS >= 90 + SPY > SMA200 |
| 6 | M55 Guppy GMMA (ditala 2) | 49,975 / 31,792 | -0.02 / +0.33 | +2.01 | RS >= 90 + ATR% >= 4 | +0.96 | RS >= 90 + SPY > SMA200 |
| 7 | M18 EMA9/21 Pullback (ditala 1) | 33,162 / 25,793 | +0.02 / +0.34 | +1.95 | RS >= 90 + ATR% >= 4 | +0.88 | RS >= 90 + rejim QQQ ON |
| 8 | M161 EMA 10/21 + Supertrend (10,3) | 128,810 / 77,162 | -0.06 / +0.11 | +1.82 | RS >= 90 + ATR% >= 4 | +0.95 | RS >= 90 + SPY > SMA200 |
| 9 | N73 Tutup bawah jalur bawah BB(20,2) | 47,306 / 35,893 | +0.38 / +0.19 | +1.78 | tutup > MA200 + ATR% >= 4 | +0.89 | RS >= 90 + SPY > SMA200 |
| 10 | M55 Guppy GMMA | 48,533 / 30,682 | -0.02 / +0.32 | +1.77 | RS >= 90 + ATR% >= 4 | +0.98 | RS >= 90 + SPY > SMA200 |
| 11 | M161 EMA 10/21 + Supertrend (10,3) (ditala 1) | 113,164 / 68,125 | -0.05 / +0.18 | +1.77 | RS >= 90 + ATR% >= 4 | +1.02 | RS >= 90 + SPY > SMA200 |
| 12 | M55 Guppy GMMA (ditala 1) | 47,336 / 29,861 | -0.03 / +0.29 | +1.76 | RS >= 90 + ATR% >= 4 | +0.88 | RS >= 90 + SPY > SMA200 |
| 13 | M27 Price Action 4 Tiang (ditala 1) | 130,126 / 86,953 | -0.14 / +0.04 | +1.75 | RS >= 90 + ATR% >= 4 | +0.80 | RS >= 90 + SPY > SMA200 |
| 14 | M84 Jarak purata bergerak MAD 21/200 (ditala 1) | 7,022 / 4,962 | +0.93 / +1.98 | +1.69 | MA20 > MA50 + ATR% >= 4 | +1.48 | ADX < 20 + SPY > SMA200 |
| 15 | N43 Undur EMA8 + penapis MA50 | 105,285 / 69,324 | -0.02 / +0.30 | +1.66 | RS >= 90 + ATR% >= 4 | +1.00 | RS >= 90 + SPY > SMA200 |
| 16 | M21 Marius 3 Persediaan (Pecahan+Jurang+Kesinambungan) | 339 / 883 | +5.12 / +1.56 | +1.65 | MA50 > MA200 + RS >= 90 | +2.50 | RS >= 90 + SPY > SMA200 |
| 17 | M102 Stockbee SLTB (ditala 2) | 135 / 504 | +12.60 / +3.73 | +1.60 | Supertrend naik + RS >= 90 | +2.41 | Supertrend naik + SPY > SMA200 |
| 18 | M149 3-Step Pullback (ditala 2) | 32,064 / 21,792 | -0.10 / +0.29 | +1.59 | RS >= 90 + ATR% >= 4 | +0.83 | ATR% >= 4 + rejim QQQ ON |
| 19 | P13 RSI14 silang atas 60 | 85,731 / 56,365 | -0.08 / +0.27 | +1.56 | RS >= 90 + ATR% >= 4 | +0.78 | RS >= 90 + SPY > SMA200 |
| 20 | M08 SMA20 + SMA200 | 16,795 / 17,554 | +0.14 / +0.35 | +1.56 | RS >= 90 + ATR% >= 4 | +0.67 | RS >= 90 + SPY > SMA200 |
| 21 | N08 tutup>EMA20 tidak terlalu jauh | 191,300 / 133,819 | -0.03 / +0.10 | +1.52 | RS >= 90 + ATR% >= 4 | +1.02 | RS >= 90 + SPY > SMA200 |
| 22 | M57 Landry Trend Knockout (TKO) (ditala 1) | 27,318 / 25,458 | +0.06 / -0.07 | +1.51 | RS >= 90 + ATR% >= 4 | +0.39 | RS >= 90 + SPY > SMA200 |
| 23 | M50 Elder Triple Screen (ditala 2) | 56,851 / 36,059 | +0.10 / +0.34 | +1.51 | RS >= 90 + ATR% >= 4 | +1.08 | ATR% >= 4 + rejim QQQ ON |
| 24 | P40 pocket pivot | 83,021 / 44,014 | +0.28 / +0.41 | +1.51 | RS >= 90 + ATR% >= 4 | +0.77 | RS >= 90 + SPY > SMA200 |
| 25 | M39 Radge Pecahan Bollinger 100 hari (ditala 1) | 55,798 / 35,876 | +0.23 / +0.21 | +1.47 | RS >= 90 + ATR% >= 4 | +1.15 | RS >= 90 + SPY > SMA200 |
| 26 | M84 Jarak purata bergerak MAD 21/200 (ditala 2) | 6,461 / 4,432 | +0.53 / +2.23 | +1.44 | MA50 naik (lawan 20 bar lalu) + ATR% >= 4 | +1.53 | ATR% >= 4 + rejim QQQ ON |
| 27 | N09 Undur EMA10 + penapis EMA50 | 106,209 / 69,147 | +0.02 / +0.24 | +1.42 | RS >= 90 + ATR% >= 4 | +1.13 | RS >= 90 + SPY > SMA200 |
| 28 | M20 EMA10/15 Crossover + Sudut | 82,674 / 53,935 | +0.00 / +0.23 | +1.39 | RS >= 90 + ATR% >= 4 | +0.98 | RS >= 90 + SPY > SMA200 |
| 29 | M161 EMA 10/21 + Supertrend (10,3) (ditala 2) | 183,524 / 112,856 | -0.12 / +0.06 | +1.37 | RS >= 90 + ATR% >= 4 | +0.67 | >= 30% di bawah puncak 52 minggu + SPY > SMA200 |
| 30 | P29 Holy Grail (ADX>30, undur EMA20, tutup > tinggi semalam) | 31,988 / 21,813 | -0.37 / -0.49 | +1.34 | Supertrend naik + RS >= 90 | -0.13 | RS >= 90 + rejim QQQ ON |
| 31 | M14 Walking with the Whales | 258,193 / 169,237 | -0.11 / +0.03 | +1.34 | RS >= 90 + ATR% >= 4 | +0.82 | RS >= 90 + SPY > SMA200 |
| 32 | M102 Stockbee SLTB | 67,110 / 52,281 | +0.08 / +0.18 | +1.33 | RS >= 90 + ATR% >= 4 | +0.76 | ATR% >= 4 + SPY > SMA200 |
| 33 | M20 EMA10/15 Crossover + Sudut (ditala 1) | 64,732 / 43,301 | +0.06 / +0.27 | +1.33 | RS >= 90 + ATR% >= 4 | +1.17 | RS >= 90 + SPY > SMA200 |
| 34 | M102 Stockbee SLTB (ditala 1) | 35,178 / 33,830 | +0.25 / +0.37 | +1.32 | RS >= 90 + ATR% >= 4 | +0.87 | RS >= 90 + rejim QQQ ON |
| 35 | N119 3 tutup turun berturut | 209,711 / 153,239 | +0.11 / +0.16 | +1.32 | RS >= 90 + ATR% >= 4 | +1.12 | RS >= 90 + SPY > SMA200 |
| 36 | M27 Price Action 4 Tiang | 132,487 / 89,026 | -0.07 / +0.00 | +1.29 | tutup > MA200 + >= 30% di bawah puncak 52 minggu | +0.75 | RS >= 90 + SPY > SMA200 |
| 37 | M57 Landry Trend Knockout (TKO) (ditala 2) | 27,635 / 26,182 | +0.20 / +0.26 | +1.28 | RS >= 90 + ATR% >= 4 | +0.67 | ATR% >= 4 + rejim QQQ ON |
| 38 | P48 EMA crossback | 49,005 / 30,308 | -0.06 / +0.16 | +1.28 | RS >= 90 + ATR% >= 4 | +0.98 | RS >= 90 + SPY > SMA200 |
| 39 | M12 Parabolic SAR (ditala 1) | 48,990 / 32,024 | +0.02 / +0.39 | +1.26 | RS >= 90 + ATR% >= 4 | +0.75 | ATR% >= 4 + SPY > SMA200 |
| 40 | N41 CMF20>0 + tutup>EMA20 | 105,601 / 73,571 | +0.08 / +0.08 | +1.25 | RS >= 90 + ATR% >= 4 | +1.19 | RS >= 90 + SPY > SMA200 |
| 41 | P09 tutup silang atas MA20 | 106,294 / 75,503 | +0.09 / +0.22 | +1.23 | RS >= 90 + ATR% >= 4 | +1.11 | RS >= 90 + SPY > SMA200 |
| 42 | P03 MACD silang naik atas sifar | 33,922 / 20,943 | +0.03 / +0.44 | +1.22 | RS >= 90 + ATR% >= 4 | +0.64 | ATR% >= 4 + SPY > SMA200 |
| 43 | M01 Bollinger Band + RSI (ditala 2) | 43,498 / 33,924 | +0.37 / -0.20 | +1.20 | tutup > MA200 + >= 30% di bawah puncak 52 minggu | +0.14 | >= 30% di bawah puncak 52 minggu + rejim QQQ OFF |
| 44 | M18 EMA9/21 Pullback | 59,452 / 42,492 | -0.11 / +0.16 | +1.18 | RS >= 90 + ATR% >= 4 | +0.67 | RS >= 90 + SPY > SMA200 |
| 45 | M14 Walking with the Whales (ditala 2) | 256,230 / 168,929 | -0.11 / +0.01 | +1.16 | RS >= 90 + ATR% >= 4 | +0.87 | RS >= 90 + SPY > SMA200 |
| 46 | P16 RSI2<5 atas MA200 | 28,410 / 19,044 | +0.19 / -0.01 | +1.16 | volum hari isyarat >= 1.5x purata 50 + ATR% >= 4 | +0.93 | ATR% >= 4 + rejim QQQ OFF |
| 47 | M27 Price Action 4 Tiang (ditala 2) | 142,901 / 95,777 | -0.05 / -0.09 | +1.13 | RS >= 90 + ATR% >= 4 | +0.78 | RS >= 90 + rejim QQQ ON |
| 48 | N202 | 30,366 / 19,542 | +0.13 / +0.08 | +1.10 | RS >= 90 + ATR% >= 4 | +0.76 | RS >= 90 + SPY > SMA200 |
| 49 | M73 ADX(5) > 40 + Julat Terkecil 6 Hari (ditala 2) | 335,963 / 239,271 | -0.09 / -0.12 | +1.09 | RS >= 90 + ATR% >= 4 | +0.82 | RS >= 90 + SPY > SMA200 |
| 50 | M14 Walking with the Whales (ditala 1) | 261,648 / 170,744 | -0.06 / +0.04 | +1.09 | RS >= 90 + ATR% >= 4 | +0.95 | RS >= 90 + SPY > SMA200 |
| 51 | M49 Ichimoku (Tutup Atas Awan + Tenkan Silang Kijun) | 41,951 / 27,861 | -0.24 / +0.27 | +1.08 | MA50 > MA200 + ATR% >= 4 | +0.35 | ATR% >= 4 + SPY > SMA200 |
| 52 | M153 Range Leader (ditala 1) | 149,387 / 103,786 | -0.07 / +0.11 | +1.07 | ADX < 20 + >= 30% di bawah puncak 52 minggu | +0.50 | RS >= 90 + SPY > SMA200 |
| 53 | M153 Range Leader (ditala 2) | 149,387 / 103,786 | -0.07 / +0.11 | +1.07 | ADX < 20 + >= 30% di bawah puncak 52 minggu | +0.50 | RS >= 90 + SPY > SMA200 |
| 54 | M153 Range Leader | 149,387 / 103,786 | -0.07 / +0.11 | +1.07 | ADX < 20 + >= 30% di bawah puncak 52 minggu | +0.50 | RS >= 90 + SPY > SMA200 |
| 55 | N45 Undur EMA21 cerun positif | 83,984 / 57,199 | -0.04 / +0.17 | +1.06 | RS >= 90 + ATR% >= 4 | +0.62 | RS >= 90 + SPY > SMA200 |
| 56 | N36 Pocket pivot | 113,595 / 74,105 | +0.26 / +0.45 | +1.06 | RS >= 90 + ATR% >= 4 | +1.00 | RS >= 90 + SPY > SMA200 |
| 57 | N47 NR7 + EMA9>EMA21 | 119,091 / 75,970 | -0.30 / -0.16 | +1.06 | RS >= 90 + ATR% >= 4 | +0.52 | RS >= 90 + SPY > SMA200 |
| 58 | M106 DMI Wilder (ditala 2) | 82,121 / 58,821 | +0.07 / +0.31 | +1.05 | ADX < 20 + >= 30% di bawah puncak 52 minggu | +1.00 | RS >= 90 + SPY > SMA200 |
| 59 | M50 Elder Triple Screen | 87,971 / 59,573 | -0.17 / +0.06 | +1.05 | RS >= 90 + ATR% >= 4 | +0.23 | RS >= 90 + SPY > SMA200 |
| 60 | M12 Parabolic SAR | 50,494 / 32,875 | +0.04 / +0.38 | +1.04 | RS >= 90 + ATR% >= 4 | +0.60 | ATR% >= 4 + SPY > SMA200 |
| 61 | N27 Ichimoku atas awan | 45,309 / 30,705 | -0.16 / +0.47 | +1.03 | RS >= 70 + ATR% >= 4 | +0.72 | ATR% >= 4 + SPY > SMA200 |
| 62 | M94 Pecutan Momentum (Chen, Yu & Wang) (ditala 1) | 22,866 / 16,412 | -0.25 / +0.33 | +1.03 | MACD > 0 + ATR% >= 4 | +1.07 | ATR% >= 4 + rejim QQQ ON |
| 63 | M84 Jarak purata bergerak MAD 21/200 | 6,353 / 4,294 | +0.21 / +1.38 | +1.02 | MA20 > MA50 + ATR% >= 4 | +0.17 | RS >= 90 + SPY > SMA200 |
| 64 | M90 Pring KST | 18,844 / 11,949 | +0.06 / -0.07 | +1.02 | RS >= 90 + volum hari isyarat >= 1.5x purata 50 | -0.17 | ADX < 20 + rejim QQQ ON |
| 65 | M147 Improved Three-Bar Pullback (ditala 1) | 9,482 / 7,201 | +0.22 / +0.54 | +1.02 | >= 30% di bawah puncak 52 minggu + hari naik (tutup > buka) | +0.21 | ATR% >= 4 + rejim QQQ ON |
| 66 | M20 EMA10/15 Crossover + Sudut (ditala 2) | 91,136 / 59,376 | +0.05 / +0.18 | +1.02 | RS >= 90 + ATR% >= 4 | +1.01 | RS >= 90 + SPY > SMA200 |
| 67 | N16 RSI2<10 tanpa penapis | 103,622 / 78,275 | +0.20 / +0.23 | +0.97 | RS >= 90 + ATR% >= 4 | +0.86 | >= 30% di bawah puncak 52 minggu + rejim QQQ OFF |
| 68 | M159 Heikin-Ashi Trend | 203,270 / 140,556 | -0.10 / +0.03 | +0.97 | ADX < 20 + >= 30% di bawah puncak 52 minggu | +0.81 | RS >= 90 + SPY > SMA200 |
| 69 | M57 Landry Trend Knockout (TKO) | 25,925 / 22,392 | +0.03 / -0.03 | +0.96 | RS >= 90 + ATR% >= 4 | +0.28 | RS >= 90 + SPY > SMA200 |
| 70 | M70 Pecahan Hari Dalam (ditala 1) | 74,760 / 41,867 | -0.27 / -0.34 | +0.95 | RS >= 90 + ATR% >= 4 | +0.27 | RS >= 90 + SPY > SMA200 |
| 71 | N29 PSAR naik + tutup>MA50 | 80,077 / 54,168 | +0.07 / +0.38 | +0.94 | RS >= 90 + ATR% >= 4 | +0.98 | >= 30% di bawah puncak 52 minggu + SPY > SMA200 |
| 72 | M105 Supertrend tulen (ditala 2) | 54,415 / 39,076 | -0.04 / +0.18 | +0.94 | ADX < 20 + >= 30% di bawah puncak 52 minggu | +0.54 | RS >= 90 + SPY > SMA200 |
| 73 | M159 Heikin-Ashi Trend (ditala 2) | 190,007 / 130,693 | -0.07 / -0.01 | +0.93 | ADX < 20 + >= 30% di bawah puncak 52 minggu | +0.80 | RS >= 90 + SPY > SMA200 |
| 74 | N38 VCP pecah | 38,853 / 26,667 | +0.38 / +0.42 | +0.93 | ATR% >= 4 + hari naik (tutup > buka) | +0.83 | ATR% >= 4 + rejim QQQ ON |
| 75 | M15 Break & Retest + Henti ATR (ditala 2) | 33,499 / 25,950 | +0.16 / +0.13 | +0.92 | tutup > MA200 + ATR% >= 4 | +0.22 | RS >= 90 + rejim QQQ OFF |
| 76 | M125 2-Bar Breakout | 211,434 / 146,245 | -0.15 / -0.13 | +0.92 | RS >= 90 + ATR% >= 4 | +0.54 | RS >= 90 + SPY > SMA200 |
| 77 | M159 Heikin-Ashi Trend (ditala 1) | 190,075 / 130,752 | -0.07 / -0.02 | +0.92 | ADX < 20 + >= 30% di bawah puncak 52 minggu | +0.79 | RS >= 90 + SPY > SMA200 |
| 78 | P47 undur ke MA50 yang naik | 56,975 / 31,543 | +0.04 / +0.32 | +0.91 | ATR% >= 4 + squeeze hidup | +0.51 | RS >= 90 + SPY > SMA200 |
| 79 | N76 Tutup > MA50 (penapis trend tunggal) | 63,462 / 45,753 | +0.09 / +0.41 | +0.91 | ADX < 20 + >= 30% di bawah puncak 52 minggu | +0.63 | >= 30% di bawah puncak 52 minggu + SPY > SMA200 |
| 80 | P10 tutup silang atas MA50 | 63,462 / 45,753 | +0.09 / +0.41 | +0.91 | ADX < 20 + >= 30% di bawah puncak 52 minggu | +0.63 | >= 30% di bawah puncak 52 minggu + SPY > SMA200 |
| 81 | M13 Garis Trend Action/Safety Line (ditala 1) | 106,200 / 79,949 | +0.04 / +0.07 | +0.91 | RS >= 90 + ATR% >= 4 | +0.84 | RS >= 90 + SPY > SMA200 |
| 82 | P15 RSI2<10 atas MA200 | 58,160 / 37,570 | +0.09 / +0.06 | +0.90 | RS >= 90 + ATR% >= 4 | +0.66 | RS >= 90 + SPY > SMA200 |
| 83 | M77 Undercut & Rally pada Purata Bergerak (MAU&R) (ditala 2) | 5,679 / 3,380 | +0.44 / +0.92 | +0.88 | ADX < 20 + ATR% >= 4 | +0.46 | tutup > MA20 + SPY > SMA200 |
| 84 | P02 MACD silang naik bawah sifar | 37,036 / 28,242 | +0.04 / +0.07 | +0.87 | ADX < 20 + >= 30% di bawah puncak 52 minggu | +0.75 | ATR% >= 4 + rejim QQQ ON |
| 85 | N07 Tiga MA tersusun | 37,088 / 25,174 | -0.03 / +0.15 | +0.86 | MA50 naik (lawan 20 bar lalu) + >= 30% di bawah puncak 52 minggu | +0.51 | >= 30% di bawah puncak 52 minggu + rejim QQQ ON |
| 86 | M123 CCI Correction (Lambert, ChartSchool) (ditala 2) | 25,620 / 16,597 | -0.05 / +0.14 | +0.86 | RS >= 90 + ATR% >= 4 | +0.48 | RS >= 90 + rejim QQQ ON |
| 87 | P07 MA20 silang atas MA50 | 19,511 / 13,780 | -0.02 / +0.13 | +0.85 | MACD > isyarat + >= 30% di bawah puncak 52 minggu | +0.55 | >= 30% di bawah puncak 52 minggu + rejim QQQ ON |
| 88 | M03 BB Break + Divergence RSI | 31,455 / 24,113 | +0.03 / -0.04 | +0.84 | ADX < 20 + >= 30% di bawah puncak 52 minggu | +0.04 | ATR% >= 4 + rejim QQQ ON |
| 89 | P12 RSI14 silang atas 50 | 100,031 / 72,174 | -0.01 / +0.14 | +0.83 | ADX < 20 + >= 30% di bawah puncak 52 minggu | +0.91 | RS >= 90 + rejim QQQ ON |
| 90 | M92 CCI-50 (ditala 1) | 60,503 / 43,014 | -0.01 / +0.17 | +0.80 | tutup > MA200 + >= 30% di bawah puncak 52 minggu | +0.69 | >= 30% di bawah puncak 52 minggu + SPY > SMA200 |
| 91 | M79 Radge: 20% Flipper (ditala 2) | 15,140 / 18,401 | +0.38 / +0.45 | +0.80 | templat trend Minervini + ATR% >= 4 | +0.86 | RS >= 90 + rejim QQQ ON |
| 92 | M35 Pocket Pivot Morales & Kacher | 59,042 / 29,502 | +0.21 / +0.47 | +0.80 | ATR% >= 4 + tutup dalam 25% teratas julat hari | +0.83 | ATR% >= 4 + rejim QQQ ON |
| 93 | M156 Single Penetration (DiNapoli) (ditala 1) | 55,081 / 35,174 | -0.12 / +0.01 | +0.79 | RS >= 90 + ATR% >= 4 | +0.56 | RS >= 90 + SPY > SMA200 |
| 94 | M13 Garis Trend Action/Safety Line | 74,401 / 56,376 | +0.17 / +0.18 | +0.79 | RS >= 90 + ATR% >= 4 | +0.85 | RS >= 90 + rejim QQQ ON |
| 95 | M15 Break & Retest + Henti ATR | 30,769 / 23,904 | +0.13 / +0.12 | +0.77 | tutup > MA200 + ATR% >= 4 | +0.45 | RS >= 90 + SPY > SMA200 |
| 96 | M82 Arthur Hill Rotasi Sasaran 10% (ditala 2) | 9,126 / 7,255 | -0.04 / +0.21 | +0.75 | MA50 > MA200 + ATR% >= 4 | -0.00 | MA50 > MA200 + rejim QQQ ON |
| 97 | P01 MACD silang naik | 70,958 / 49,185 | +0.04 / +0.23 | +0.74 | ADX < 20 + >= 30% di bawah puncak 52 minggu | +0.75 | ATR% >= 4 + rejim QQQ ON |
| 98 | N74 MACD atas garis isyarat (keadaan, bukan silang) | 70,958 / 49,185 | +0.04 / +0.23 | +0.74 | ADX < 20 + >= 30% di bawah puncak 52 minggu | +0.75 | ATR% >= 4 + rejim QQQ ON |
| 99 | M21 Marius 3 Persediaan (Pecahan+Jurang+Kesinambungan) (ditala 2) | 335 / 882 | +6.03 / +1.63 | +0.73 | MACD > 0 + RS >= 90 | +2.17 | RS >= 90 + SPY > SMA200 |
| 100 | N55 BB + RSI + ADX>20 | 28,490 / 19,054 | +0.23 / -0.24 | +0.72 | Supertrend naik + RS >= 90 | +0.26 | RS >= 90 + rejim QQQ ON |
| 101 | M30 BB Free Bar + Himpitan 50/2.5 (ditala 1) | 9,911 / 6,842 | +0.18 / +0.21 | +0.72 | RS >= 90 + ATR% >= 4 | -0.03 | ATR% >= 4 + SPY > SMA200 |
| 102 | M70 Pecahan Hari Dalam (ditala 2) | 80,448 / 45,766 | -0.23 / -0.26 | +0.71 | RS >= 90 + ATR% >= 4 | +0.52 | RS >= 90 + SPY > SMA200 |
| 103 | N42 Lonjakan volum 2x | 36,488 / 25,390 | +0.32 / +0.07 | +0.71 | Supertrend naik + RS >= 90 | +0.84 | RS >= 90 + SPY > SMA200 |
| 104 | N75 RSI14 < 40 tanpa penapis | 62,742 / 48,298 | +0.37 / +0.07 | +0.70 | tutup > MA200 + ATR% >= 4 | +0.59 | >= 30% di bawah puncak 52 minggu + rejim QQQ OFF |
| 105 | N201 | 17,203 / 11,978 | -0.11 / +0.19 | +0.70 | MACD > isyarat + >= 30% di bawah puncak 52 minggu | +0.34 | >= 30% di bawah puncak 52 minggu + rejim QQQ ON |
| 106 | M160 Measured Move Up (ditala 2) | 30,998 / 21,707 | -0.09 / +0.27 | +0.70 | tutup > MA20 + >= 30% di bawah puncak 52 minggu | +0.57 | >= 30% di bawah puncak 52 minggu + SPY > SMA200 |
| 107 | M92 CCI-50 | 53,940 / 38,888 | -0.02 / +0.33 | +0.70 | >= 30% di bawah puncak 52 minggu + ATR% >= 4 | +0.36 | >= 30% di bawah puncak 52 minggu + SPY > SMA200 |
| 108 | M32 Momentum Burst (ditala 1) | 4,639 / 5,333 | +0.79 / +0.96 | +0.68 | templat trend Minervini + RS >= 90 | +1.07 | RS >= 90 + SPY > SMA200 |
| 109 | M11 NR7 Breakout + Volume (ditala 2) | 9,706 / 6,076 | +0.48 / +0.66 | +0.66 | >= 30% di bawah puncak 52 minggu | +0.41 | ATR% >= 4 + rejim QQQ ON |
| 110 | P04 MA5 silang atas MA20 | 55,493 / 39,183 | -0.02 / +0.04 | +0.64 | ADX < 20 + >= 30% di bawah puncak 52 minggu | +0.41 | RS >= 90 + SPY > SMA200 |
| 111 | N113 80-20 bar (sisi beli) | 143,891 / 105,001 | -0.05 / +0.04 | +0.64 | RS >= 90 + ATR% >= 4 | +0.55 | RS >= 90 + SPY > SMA200 |
| 112 | M139 均线首次粘合向上发散 (MA berhimpun kali pertama, berkipas naik) (ditala 2) | 9,618 / 6,629 | -0.15 / -0.04 | +0.63 | MA20 > MA50 + ATR% >= 4 | -0.02 | RS >= 90 + rejim QQQ ON |
| 113 | M13 Garis Trend Action/Safety Line (ditala 2) | 57,053 / 43,319 | +0.17 / +0.29 | +0.63 | >= 30% di bawah puncak 52 minggu + hari naik (tutup > buka) | +0.53 | ATR% >= 4 + rejim QQQ ON |
| 114 | M03 BB Break + Divergence RSI (ditala 1) | 10,330 / 8,513 | +0.40 / +0.20 | +0.63 | >= 30% di bawah puncak 52 minggu + tutup dalam 25% teratas julat hari | +0.02 | ATR% >= 4 + rejim QQQ ON |
| 115 | M39 Radge Pecahan Bollinger 100 hari | 36,460 / 23,361 | -0.20 / -0.33 | +0.62 | RS >= 90 + ATR% >= 4 | +0.11 | RS >= 90 + SPY > SMA200 |
| 116 | M158 Doubly Adaptive Profit Targets (ditala 1) | 51,281 / 37,747 | -0.25 / -0.25 | +0.60 | RS >= 90 + ATR% >= 4 | -0.07 | RS >= 90 + rejim QQQ ON |
| 117 | N54 Supertrend + RSI>50 | 63,882 / 43,756 | -0.02 / +0.05 | +0.60 | ADX < 20 + >= 30% di bawah puncak 52 minggu | +0.69 | RS >= 90 + SPY > SMA200 |
| 118 | M155 Market Cycle Strategy | 76,987 / 58,091 | +0.06 / +0.06 | +0.59 | ADX < 20 + >= 30% di bawah puncak 52 minggu | +0.19 | >= 30% di bawah puncak 52 minggu + rejim QQQ ON |
| 119 | M128 Inventory Retracement Bar (IRB, Rob Hoffman) | 30,040 / 20,447 | -0.17 / -0.08 | +0.59 | RS >= 90 + ATR% >= 4 | +0.23 | RS >= 90 + SPY > SMA200 |
| 120 | M116 2/20 EMA Breakout (Landry) (ditala 2) | 104,768 / 66,924 | -0.24 / -0.02 | +0.58 | RS >= 90 + ATR% >= 4 | +0.12 | RS >= 90 + SPY > SMA200 |
| 121 | M116 2/20 EMA Breakout (Landry) (ditala 1) | 104,768 / 66,924 | -0.24 / -0.02 | +0.58 | RS >= 90 + ATR% >= 4 | +0.12 | RS >= 90 + SPY > SMA200 |
| 122 | P19 bawah jalur bawah Bollinger + RSI14<30 | 13,481 / 10,866 | +0.02 / +0.39 | +0.58 | volum 10 hari > volum 50 hari + ATR% >= 4 | +0.08 | ATR% >= 4 + rejim QQQ OFF |
| 123 | N19 Bawah jalur BB + RSI<30 | 13,481 / 10,866 | +0.02 / +0.39 | +0.58 | volum 10 hari > volum 50 hari + ATR% >= 4 | +0.08 | ATR% >= 4 + rejim QQQ OFF |
| 124 | M105 Supertrend tulen (ditala 1) | 42,671 / 31,214 | -0.08 / +0.04 | +0.58 | tutup > MA20 + >= 30% di bawah puncak 52 minggu | +0.32 | >= 30% di bawah puncak 52 minggu + SPY > SMA200 |
| 125 | P06 MA10 silang atas MA50 | 23,629 / 16,539 | +0.13 / +0.56 | +0.57 | ATR% >= 4 | +0.78 | ATR% >= 4 + SPY > SMA200 |
| 126 | M47 Holy Grail Raschke (ditala 1) | 19,096 / 12,032 | -0.03 / -0.12 | +0.56 | tutup > MA200 + ATR% >= 4 | +0.40 | RS >= 90 + SPY > SMA200 |
| 127 | M118 Expansion Pivot (Cooper) | 7,126 / 5,227 | -0.01 / -0.12 | +0.56 | >= 30% di bawah puncak 52 minggu + ATR% >= 4 | -0.12 | >= 30% di bawah puncak 52 minggu + SPY > SMA200 |
| 128 | M19 Sneaky Pivot (proksi harian) | 26,480 / 21,312 | +0.20 / -0.36 | +0.55 | ADX < 20 + >= 30% di bawah puncak 52 minggu | +0.14 | >= 30% di bawah puncak 52 minggu + rejim QQQ OFF |
| 129 | M12 Parabolic SAR (ditala 2) | 54,057 / 35,724 | +0.03 / +0.25 | +0.55 | templat trend Minervini + RS >= 90 | +0.68 | RS >= 90 + SPY > SMA200 |
| 130 | M89 Chande 65sma-3cc (ditala 2) | 17,460 / 11,869 | -0.24 / +0.03 | +0.55 | Supertrend naik + >= 30% di bawah puncak 52 minggu | -0.28 | >= 30% di bawah puncak 52 minggu + SPY > SMA200 |
| 131 | M119 180 Bullish (Cooper) (ditala 2) | 26,736 / 19,344 | -0.28 / +0.24 | +0.54 | RS >= 90 + ATR% >= 4 | +0.65 | ATR% >= 4 + rejim QQQ ON |
| 132 | M148 Natural Number Method | 10,545 / 9,427 | +0.10 / +0.02 | +0.54 | ADX < 20 + >= 30% di bawah puncak 52 minggu | +0.06 | >= 30% di bawah puncak 52 minggu + SPY > SMA200 |
| 133 | M49 Ichimoku (Tutup Atas Awan + Tenkan Silang Kijun) (ditala 1) | 41,690 / 28,279 | +0.03 / +0.13 | +0.53 | RS >= 70 + ATR% >= 4 | +0.20 | >= 30% di bawah puncak 52 minggu + SPY > SMA200 |
| 134 | M77 Undercut & Rally pada Purata Bergerak (MAU&R) | 7,540 / 4,655 | +0.27 / +0.96 | +0.53 | templat trend Minervini + ADX < 20 | +0.68 | templat trend Minervini + rejim QQQ ON |
| 135 | M154 HOLP (High of Low Period) | 15,365 / 9,907 | +0.21 / -0.22 | +0.52 | ATR% >= 4 + squeeze hidup | -0.56 | ATR% >= 4 + rejim QQQ OFF |
| 136 | M154 HOLP (High of Low Period) (ditala 1) | 15,365 / 9,907 | +0.21 / -0.22 | +0.52 | ATR% >= 4 + squeeze hidup | -0.56 | ATR% >= 4 + rejim QQQ OFF |
| 137 | M125 2-Bar Breakout (ditala 2) | 200,632 / 135,207 | -0.18 / -0.15 | +0.52 | ADX < 20 + >= 30% di bawah puncak 52 minggu | +0.33 | >= 30% di bawah puncak 52 minggu + SPY > SMA200 |
| 138 | M125 2-Bar Breakout (ditala 1) | 200,632 / 135,207 | -0.18 / -0.15 | +0.52 | ADX < 20 + >= 30% di bawah puncak 52 minggu | +0.33 | >= 30% di bawah puncak 52 minggu + SPY > SMA200 |
| 139 | M154 HOLP (High of Low Period) (ditala 2) | 15,365 / 9,907 | +0.21 / -0.22 | +0.52 | ATR% >= 4 + squeeze hidup | -0.56 | ATR% >= 4 + rejim QQQ OFF |
| 140 | M124 'Last' Stochastic Technique (ChartSchool) | 29,032 / 20,813 | -0.12 / +0.21 | +0.52 | templat trend Minervini + ATR% >= 4 | +0.30 | >= 30% di bawah puncak 52 minggu + SPY > SMA200 |
| 141 | M93 Bollinger Kaedah II: %b + MFI | 37,772 / 24,145 | -0.16 / +0.13 | +0.51 | tutup > MA200 + ATR% >= 4 | +0.50 | ATR% >= 4 + SPY > SMA200 |
| 142 | M66 IBD Undur Pertama ke Purata 50 Hari (ditala 1) | 73,746 / 47,253 | +0.00 / +0.11 | +0.51 | ATR% >= 4 + squeeze hidup | +0.38 | RS >= 90 + SPY > SMA200 |
| 143 | M01 Bollinger Band + RSI (ditala 1) | 5,433 / 4,458 | +0.12 / +0.50 | +0.51 | >= 30% di bawah puncak 52 minggu + ATR% >= 4 | +0.84 | ATR% >= 4 + rejim QQQ ON |
| 144 | M90 Pring KST (ditala 2) | 19,126 / 12,113 | -0.01 / -0.05 | +0.50 | RS >= 90 + volum hari isyarat >= 1.5x purata 50 | -0.18 | MA50 > MA200 + rejim QQQ ON |
| 145 | N22 BB pecah atas + RSI | 59,173 / 40,493 | -0.09 / +0.03 | +0.50 | tutup > MA200 + >= 30% di bawah puncak 52 minggu | +0.44 | >= 30% di bawah puncak 52 minggu + SPY > SMA200 |
| 146 | M94 Pecutan Momentum (Chen, Yu & Wang) (ditala 2) | 2,359 / 1,742 | +2.37 / +1.03 | +0.50 | MA50 naik (lawan 20 bar lalu) + volum 10 hari > volum 50 hari | +0.73 | ADX < 20 + SPY > SMA200 |
| 147 | P18 pecah atas jalur atas Bollinger | 59,262 / 40,543 | -0.08 / +0.03 | +0.49 | tutup > MA200 + >= 30% di bawah puncak 52 minggu | +0.41 | RS >= 90 + SPY > SMA200 |
| 148 | P23 Ichimoku pecah atas awan | 25,889 / 18,504 | -0.12 / +0.47 | +0.49 | ATR% >= 4 + hari naik (tutup > buka) | +0.02 | MA50 naik (lawan 20 bar lalu) + SPY > SMA200 |
| 149 | M89 Chande 65sma-3cc | 17,231 / 11,522 | -0.04 / +0.34 | +0.47 | RSI14 > 50 + ATR% >= 4 | +0.10 | RS >= 90 + SPY > SMA200 |
| 150 | M11 NR7 Breakout + Volume | 10,504 / 6,615 | +0.34 / +0.74 | +0.47 | >= 30% di bawah puncak 52 minggu + ATR% >= 4 | +0.41 | ATR% >= 4 + rejim QQQ ON |
| 151 | M31 Band Walk (BB 20/2) (ditala 1) | 10,981 / 8,713 | +0.03 / -0.20 | +0.47 | RS >= 90 + ATR% >= 4 | -0.44 | RS >= 90 + rejim QQQ ON |
| 152 | M156 Single Penetration (DiNapoli) | 35,866 / 23,452 | -0.09 / -0.21 | +0.46 | ADX > 25 + RS >= 90 | +0.64 | RS >= 90 + SPY > SMA200 |
| 153 | M155 Market Cycle Strategy (ditala 1) | 56,994 / 45,879 | +0.23 / +0.10 | +0.45 | MACD > isyarat + >= 30% di bawah puncak 52 minggu | +0.77 | ATR% >= 4 + rejim QQQ ON |
| 154 | M158 Doubly Adaptive Profit Targets (ditala 2) | 55,968 / 40,304 | -0.21 / -0.10 | +0.43 | >= 30% di bawah puncak 52 minggu | +0.31 | >= 30% di bawah puncak 52 minggu + SPY > SMA200 |
| 155 | P24 Stochastic silang naik dari bawah 20 | 71,064 / 57,221 | +0.29 / -0.08 | +0.43 | RS >= 70 + ATR% >= 4 | +0.39 | RS >= 90 + rejim QQQ ON |
| 156 | M67 Rayner Teo: Ujian Ketiga pada Purata 50 (ditala 2) | 5,337 / 3,163 | +0.10 / +0.46 | +0.42 | RS >= 90 + dalam 15% dari puncak 52 minggu | -0.33 | RS >= 70 + SPY > SMA200 |
| 157 | M94 Pecutan Momentum (Chen, Yu & Wang) | 3,015 / 2,207 | +2.01 / +0.88 | +0.41 | MA20 > MA50 + RS >= 90 | +0.35 | ADX < 20 + SPY > SMA200 |
| 158 | M07 Qullamaggie Breakout | 1,158 / 2,512 | +1.66 / +1.41 | +0.40 | ATR% >= 4 + hari naik (tutup > buka) | +0.84 | ATR% >= 4 + SPY > SMA200 |
| 159 | P44 RS baru masuk 10% teratas | 10,088 / 7,097 | +0.22 / +0.61 | +0.40 | dalam 15% dari puncak 52 minggu + ATR% >= 4 | +0.27 | ATR% >= 4 + SPY > SMA200 |
| 160 | M158 Doubly Adaptive Profit Targets | 52,801 / 38,874 | -0.19 / -0.14 | +0.39 | ADX < 20 + >= 30% di bawah puncak 52 minggu | +0.17 | >= 30% di bawah puncak 52 minggu + rejim QQQ OFF |
| 161 | M92 CCI-50 (ditala 2) | 38,810 / 28,520 | +0.12 / +0.12 | +0.39 | MACD > isyarat + >= 30% di bawah puncak 52 minggu | +1.09 | >= 30% di bawah puncak 52 minggu + rejim QQQ OFF |
| 162 | M152 Spike & Ledge (ditala 2) | 15,935 / 9,594 | -0.09 / -0.06 | +0.39 | RS >= 90 + ATR% >= 4 | +0.11 | ATR% >= 4 + SPY > SMA200 |
| 163 | M152 Spike & Ledge (ditala 1) | 15,935 / 9,594 | -0.09 / -0.06 | +0.39 | RS >= 90 + ATR% >= 4 | +0.11 | ATR% >= 4 + SPY > SMA200 |
| 164 | M152 Spike & Ledge | 15,935 / 9,594 | -0.09 / -0.06 | +0.39 | RS >= 90 + ATR% >= 4 | +0.11 | ATR% >= 4 + SPY > SMA200 |
| 165 | N48 Inside day pecah | 69,684 / 44,833 | -0.14 / +0.02 | +0.38 | RSI14 > 60 + ATR% >= 4 | +0.14 | RS >= 90 + rejim QQQ ON |
| 166 | P32 lonjakan >=4% + volum 2x | 7,852 / 7,201 | +0.68 / +0.19 | +0.34 | MA50 naik (lawan 20 bar lalu) + RS >= 90 | +0.56 | RS >= 90 + SPY > SMA200 |
| 167 | M136 Short/Intermediate-term Low (Larry Williams) (ditala 2) | 95,607 / 67,032 | -0.06 / +0.04 | +0.34 | ADX < 20 + >= 30% di bawah puncak 52 minggu | +0.35 | >= 30% di bawah puncak 52 minggu + rejim QQQ OFF |
| 168 | M136 Short/Intermediate-term Low (Larry Williams) | 95,607 / 67,032 | -0.06 / +0.04 | +0.34 | ADX < 20 + >= 30% di bawah puncak 52 minggu | +0.35 | >= 30% di bawah puncak 52 minggu + rejim QQQ OFF |
| 169 | P08 MA50 silang atas MA200 | 5,044 / 3,801 | -0.25 / +0.37 | +0.34 | >= 30% di bawah puncak 52 minggu | +0.23 | >= 30% di bawah puncak 52 minggu + SPY > SMA200 |
| 170 | M136 Short/Intermediate-term Low (Larry Williams) (ditala 1) | 95,607 / 67,032 | -0.06 / +0.04 | +0.34 | ADX < 20 + >= 30% di bawah puncak 52 minggu | +0.35 | >= 30% di bawah puncak 52 minggu + rejim QQQ OFF |
| 171 | M149 3-Step Pullback (ditala 1) | 29,163 / 19,804 | -0.01 / -0.12 | +0.34 | RS >= 90 + ATR% >= 4 | +0.34 | RS >= 90 + SPY > SMA200 |
| 172 | N06 Golden cross MA50/MA200 | 5,044 / 3,801 | -0.25 / +0.37 | +0.34 | >= 30% di bawah puncak 52 minggu | +0.23 | >= 30% di bawah puncak 52 minggu + SPY > SMA200 |
| 173 | N68 Bullish engulfing + EMA21 | 46,828 / 29,647 | -0.05 / +0.32 | +0.34 | MA50 > MA200 + ATR% >= 4 | +0.69 | ATR% >= 4 + SPY > SMA200 |
| 174 | M47 Holy Grail Raschke | 4,312 / 2,746 | -0.26 / +0.41 | +0.33 | Supertrend naik + RS >= 90 | -0.07 | ATR% >= 4 + SPY > SMA200 |
| 175 | M04 BB Squeeze Breakout | 11,253 / 6,991 | +0.42 / +0.46 | +0.33 | templat trend Minervini + RS >= 90 | +0.13 | dalam 5% dari puncak 52 minggu + SPY > SMA200 |
| 176 | M11 NR7 Breakout + Volume (ditala 1) | 5,587 / 3,491 | +0.49 / +0.68 | +0.32 | >= 30% di bawah puncak 52 minggu + ATR% >= 4 | -0.25 | MA20 > MA50 + SPY > SMA200 |
| 177 | P26 pecah tinggi 55 hari | 59,382 / 36,597 | -0.29 / -0.18 | +0.32 | RS >= 90 + volum hari isyarat >= 1.5x purata 50 | -0.10 | RS >= 90 + SPY > SMA200 |
| 178 | N31 Turtle sistem 2 | 59,382 / 36,597 | -0.29 / -0.18 | +0.32 | RS >= 90 + volum hari isyarat >= 1.5x purata 50 | -0.10 | RS >= 90 + SPY > SMA200 |
| 179 | M36 Turtle 55/20 | 59,382 / 36,597 | -0.29 / -0.18 | +0.32 | RS >= 90 + volum hari isyarat >= 1.5x purata 50 | -0.10 | RS >= 90 + SPY > SMA200 |
| 180 | M145 Yum-Yum Continuation (ditala 2) | 36,215 / 23,067 | -0.19 / -0.19 | +0.32 | RS >= 90 + tutup dalam 25% teratas julat hari | +0.13 | RS >= 90 + rejim QQQ ON |
| 181 | M128 Inventory Retracement Bar (IRB, Rob Hoffman) (ditala 1) | 40,259 / 26,829 | -0.04 / +0.04 | +0.31 | RS >= 90 + ATR% >= 4 | +0.56 | ATR% >= 4 + rejim QQQ ON |
| 182 | M32 Momentum Burst | 3,783 / 4,334 | +0.55 / +0.78 | +0.31 | MA50 > MA200 + RS >= 90 | +0.38 | RS >= 90 + SPY > SMA200 |
| 183 | M76 Undercut & Rally pada Low Penting (ditala 1) | 1,144 / 1,072 | +2.05 / +0.12 | +0.30 | volum hari isyarat >= 1.5x purata 50 + ATR% >= 4 | -0.59 | ATR% >= 4 + rejim QQQ OFF |
| 184 | M96 Momo India: Ranking Sharpe 3/6/12 bulan (ditala 2) | 644 / 363 | +2.54 / +2.92 | +0.30 | ADX > 25 + RS >= 90 | -0.06 | volum 10 hari > volum 50 hari + SPY > SMA200 |
| 185 | M78 Alvarez Pecahan Mingguan DTAYS | 8,939 / 11,504 | +0.24 / +0.06 | +0.29 | volum hari isyarat >= 1.5x purata 50 + ATR% >= 4 | +0.12 | RS >= 90 + SPY > SMA200 |
| 186 | M79 Radge: 20% Flipper | 9,578 / 12,249 | -0.07 / +0.22 | +0.28 | RSI14 > 60 + ATR% >= 4 | +0.26 | MA50 > MA200 + SPY > SMA200 |
| 187 | M09 Volumatic VIDYA Pivot Retest (ditala 1) | 10,460 / 4,780 | +0.27 / +0.40 | +0.28 | tutup > MA200 + volum hari isyarat >= 1.5x purata 50 | +0.33 | RS >= 90 + SPY > SMA200 |
| 188 | M66 IBD Undur Pertama ke Purata 50 Hari | 41,669 / 24,965 | -0.02 / +0.26 | +0.27 | MA50 > MA200 + ATR% >= 4 | +0.05 | ADX < 20 + rejim QQQ ON |
| 189 | P25 pecah tinggi 20 hari | 89,711 / 57,202 | -0.17 / -0.02 | +0.27 | >= 30% di bawah puncak 52 minggu + squeeze hidup | +0.14 | RS >= 90 + SPY > SMA200 |
| 190 | P11 tutup silang atas MA200 | 29,193 / 21,546 | -0.40 / +0.06 | +0.27 | >= 30% di bawah puncak 52 minggu | +0.19 | >= 30% di bawah puncak 52 minggu + SPY > SMA200 |
| 191 | N25 Supertrend + EMA + ADX>23 | 37,087 / 24,397 | -0.13 / -0.40 | +0.26 | ADX > 25 + RS >= 90 | +0.30 | RS >= 90 + SPY > SMA200 |
| 192 | M31 Band Walk (BB 20/2) | 40,198 / 27,950 | -0.07 / -0.03 | +0.25 | ADX < 20 + >= 30% di bawah puncak 52 minggu | +0.07 | >= 30% di bawah puncak 52 minggu + SPY > SMA200 |
| 193 | P05 MA10 silang atas MA20 | 48,072 / 34,107 | +0.03 / +0.00 | +0.25 | MA50 naik (lawan 20 bar lalu) + >= 30% di bawah puncak 52 minggu | +0.19 | ATR% >= 4 + SPY > SMA200 |
| 194 | M68 Kell Base n' Break | 10,744 / 7,362 | -0.09 / +0.28 | +0.23 | RS >= 70 + volum hari isyarat >= 1.5x purata 50 | -0.22 | RS >= 70 + SPY > SMA200 |
| 195 | M107 Golden Cross SMA50/200 | 4,676 / 3,024 | -0.15 / +0.49 | +0.23 | MA50 > MA200 + >= 30% di bawah puncak 52 minggu | +0.23 | >= 30% di bawah puncak 52 minggu + SPY > SMA200 |
| 196 | M73 ADX(5) > 40 + Julat Terkecil 6 Hari | 105,976 / 72,552 | -0.24 / -0.26 | +0.22 | RS >= 70 + >= 30% di bawah puncak 52 minggu | +0.21 | RS >= 90 + rejim QQQ ON |
| 197 | P46 O'Neil pecah 50 hari + volum + RS | 8,249 / 5,543 | +0.48 / +0.66 | +0.22 | MA50 > MA200 + tutup dalam 25% teratas julat hari | +0.34 | RS >= 90 + SPY > SMA200 |
| 198 | M04 BB Squeeze Breakout (ditala 2) | 11,876 / 7,467 | +0.66 / +0.39 | +0.22 | ADX < 20 + >= 30% di bawah puncak 52 minggu | +0.18 | rejim QQQ ON + hari naik (tutup > buka) |
| 199 | M124 'Last' Stochastic Technique (ChartSchool) (ditala 2) | 33,108 / 24,181 | -0.01 / +0.15 | +0.21 | templat trend Minervini + RS >= 90 | +0.04 | templat trend Minervini + rejim QQQ ON |
| 200 | P17 pecah atas Keltner | 52,395 / 35,919 | -0.19 / -0.06 | +0.21 | RS >= 90 + volum hari isyarat >= 1.5x purata 50 | -0.13 | volum hari isyarat >= 1.5x purata 50 + SPY > SMA200 |
| 201 | M123 CCI Correction (Lambert, ChartSchool) | 24,727 / 15,865 | -0.04 / +0.07 | +0.21 | RS >= 90 + ATR% >= 4 | +0.30 | RS >= 90 + rejim QQQ ON |
| 202 | M36 Turtle 55/20 (ditala 1) | 70,836 / 44,357 | -0.21 / -0.04 | +0.21 | RS >= 90 + volum hari isyarat >= 1.5x purata 50 | -0.06 | RS >= 90 + SPY > SMA200 |
| 203 | M01 Bollinger Band + RSI | 7,698 / 6,090 | +0.15 / +0.35 | +0.21 | ATR% >= 4 | +0.15 | ATR% >= 4 + rejim QQQ ON |
| 204 | N28 ADX>25 + DI+ > DI- | 35,319 / 24,422 | -0.04 / -0.02 | +0.20 | >= 30% di bawah puncak 52 minggu + ATR% >= 4 | +0.02 | >= 30% di bawah puncak 52 minggu + SPY > SMA200 |
| 205 | M15 Break & Retest + Henti ATR (ditala 1) | 24,507 / 19,139 | +0.12 / +0.07 | +0.20 | tutup > MA200 + ATR% >= 4 | -0.12 | ATR% >= 4 + rejim QQQ ON |
| 206 | N51 BB squeeze + Supertrend | 13,158 / 8,030 | +0.37 / +0.13 | +0.20 | >= 30% di bawah puncak 52 minggu + squeeze hidup | -0.32 | >= 30% di bawah puncak 52 minggu + SPY > SMA200 |
| 207 | M52 Radge Weekend Trend Trader (ditala 2) | 10,141 / 11,656 | +0.28 / +0.12 | +0.19 | RS >= 90 + volum hari isyarat >= 1.5x purata 50 | +0.22 | RS >= 90 + SPY > SMA200 |
| 208 | M52 Radge Weekend Trend Trader | 14,358 / 15,000 | +0.04 / +0.20 | +0.19 | templat trend Minervini + RS >= 90 | +0.11 | RS >= 90 + SPY > SMA200 |
| 209 | N33 Donchian20 + penapis MA200 | 77,941 / 46,887 | -0.21 / +0.00 | +0.19 | RS >= 90 + volum hari isyarat >= 1.5x purata 50 | +0.15 | RS >= 90 + SPY > SMA200 |
| 210 | P43 Qullamaggie | 596 / 552 | +1.34 / +1.03 | +0.18 | ADX > 25 + volum 10 hari > volum 50 hari | -0.83 | ADX > 25 + rejim QQQ ON |
| 211 | M51 O'Neil Cawan & Pemegang | 847 / 419 | +0.82 / +1.90 | +0.18 | MACD > isyarat + dalam 5% dari puncak 52 minggu | -0.53 | dalam 5% dari puncak 52 minggu + SPY > SMA200 |
| 212 | M122 Moving Momentum (ChartSchool) | 17,990 / 12,198 | -0.04 / +0.07 | +0.18 | RS >= 90 + ATR% >= 4 | -0.08 | ADX < 20 + SPY > SMA200 |
| 213 | M23 Breitstein Kapitulasi + Kesinambungan (ditala 1) | 8,279 / 4,816 | +0.30 / +0.00 | +0.17 | MACD > 0 + RS >= 90 | +0.17 | RS >= 90 + SPY > SMA200 |
| 214 | P27 pecah tinggi 126 hari | 45,024 / 26,035 | -0.33 / -0.14 | +0.17 | RS >= 90 + volum hari isyarat >= 1.5x purata 50 | -0.20 | RS >= 90 + SPY > SMA200 |
| 215 | M81 Bensdorp Long Trend High Momentum (ditala 2) | 14,982 / 10,779 | -0.07 / +0.12 | +0.17 | >= 30% di bawah puncak 52 minggu | +0.25 | ATR% >= 4 + SPY > SMA200 |
| 216 | M88 O'Neil Shakeout +3 | 2,344 / 2,996 | +1.09 / +1.60 | +0.17 | MA50 naik (lawan 20 bar lalu) + ATR% >= 4 | +0.21 | ATR% >= 4 + SPY > SMA200 |
| 217 | P35 pecah tinggi 6 bulan + volum | 15,044 / 8,900 | +0.01 / +0.22 | +0.16 | MACD > isyarat + RS >= 90 | +0.31 | RS >= 90 + SPY > SMA200 |
| 218 | M36 Turtle 55/20 (ditala 2) | 53,322 / 31,852 | -0.35 / -0.18 | +0.16 | RS >= 90 + volum hari isyarat >= 1.5x purata 50 | -0.19 | RS >= 90 + SPY > SMA200 |
| 219 | M52 Radge Weekend Trend Trader (ditala 1) | 12,347 / 13,703 | +0.09 / +0.26 | +0.16 | templat trend Minervini + RS >= 90 | +0.18 | RS >= 90 + SPY > SMA200 |
| 220 | M23 Breitstein Kapitulasi + Kesinambungan | 10,692 / 6,330 | +0.08 / +0.21 | +0.15 | MACD > isyarat + RS >= 90 | +0.11 | RS >= 90 + SPY > SMA200 |
| 221 | M68 Kell Base n' Break (ditala 1) | 11,668 / 7,126 | -0.15 / +0.31 | +0.14 | RS >= 70 + volum hari isyarat >= 1.5x purata 50 | -0.05 | volum hari isyarat >= 1.5x purata 50 + SPY > SMA200 |
| 222 | M155 Market Cycle Strategy (ditala 2) | 72,182 / 55,338 | +0.13 / -0.28 | +0.14 | RSI14 > 60 + ATR% >= 4 | -0.17 | MACD > 0 + rejim QQQ ON |
| 223 | M47 Holy Grail Raschke (ditala 2) | 10,378 / 7,468 | +0.01 / +0.08 | +0.13 | RS >= 90 + hari naik (tutup > buka) | +0.31 | RS >= 90 + SPY > SMA200 |
| 224 | M54 IBD Power Trend (ditala 2) | 49,869 / 28,778 | -0.25 / +0.07 | +0.13 | RS >= 90 + volum hari isyarat >= 1.5x purata 50 | -0.02 | volum hari isyarat >= 1.5x purata 50 + SPY > SMA200 |
| 225 | M124 'Last' Stochastic Technique (ChartSchool) (ditala 1) | 40,053 / 28,662 | -0.02 / +0.05 | +0.13 | MACD > 0 + >= 30% di bawah puncak 52 minggu | +0.16 | >= 30% di bawah puncak 52 minggu + SPY > SMA200 |
| 226 | P28 pecah tinggi 252 hari | 37,730 / 20,524 | -0.24 / -0.09 | +0.13 | RS >= 90 + volum hari isyarat >= 1.5x purata 50 | -0.17 | volum hari isyarat >= 1.5x purata 50 + SPY > SMA200 |
| 227 | M137 Livermore System | 25,078 / 15,639 | -0.07 / -0.22 | +0.12 | MA50 naik (lawan 20 bar lalu) + RS >= 90 | -0.15 | RS >= 90 + rejim QQQ ON |
| 228 | M10 EMA3 + CCI + MACD (ditala 1) | 21,263 / 13,390 | +0.01 / -0.09 | +0.12 | ADX < 20 + RS >= 90 | +0.35 | ATR% >= 4 + rejim QQQ ON |
| 229 | M80 Radge Saluran Purata Bergerak (MAC) (ditala 1) | 55,011 / 37,611 | -0.33 / +0.04 | +0.11 | >= 30% di bawah puncak 52 minggu + ATR% >= 4 | +0.15 | ATR% >= 4 + SPY > SMA200 |
| 230 | M116 2/20 EMA Breakout (Landry) | 98,950 / 63,829 | -0.23 / -0.07 | +0.11 | RS >= 90 + ATR% >= 4 | +0.07 | RS >= 90 + SPY > SMA200 |
| 231 | M06 Minervini VCP Breakout (ditala 1) | 11,889 / 6,345 | +0.39 / +0.53 | +0.10 | MA50 naik (lawan 20 bar lalu) + tutup dalam 25% teratas julat hari | +0.30 | SPY > SMA200 + tutup dalam 25% teratas julat hari |
| 232 | M48 Cooper 1-2-3-4 (ditala 2) | 4,237 / 3,288 | -0.07 / +0.20 | +0.10 | RS >= 90 + ATR% >= 4 | -0.31 | RS >= 90 + SPY > SMA200 |
| 233 | N66 52w tinggi + pengesahan 1% | 16,471 / 11,208 | -0.05 / +0.16 | +0.10 | RS >= 90 + volum hari isyarat >= 1.5x purata 50 | -0.03 | RS >= 90 + SPY > SMA200 |
| 234 | M160 Measured Move Up (ditala 1) | 11,483 / 8,445 | +0.29 / +0.32 | +0.09 | ATR% >= 4 + hari naik (tutup > buka) | +0.08 | RS >= 90 + SPY > SMA200 |
| 235 | M151 Outside Bar Failure (ditala 2) | 14,219 / 8,959 | +0.03 / -0.18 | +0.09 | templat trend Minervini + ATR% >= 4 | -0.43 | >= 30% di bawah puncak 52 minggu + SPY > SMA200 |
| 236 | M93 Bollinger Kaedah II: %b + MFI (ditala 2) | 30,551 / 20,027 | -0.14 / +0.05 | +0.09 | ADX < 20 + >= 30% di bawah puncak 52 minggu | +0.54 | >= 30% di bawah puncak 52 minggu + SPY > SMA200 |
| 237 | M70 Pecahan Hari Dalam | 72,389 / 40,899 | -0.24 / -0.33 | +0.09 | RS >= 90 + ATR% >= 4 | +0.05 | RS >= 90 + SPY > SMA200 |
| 238 | M142 Pecahan volum dari dasar (底部放量) (ditala 1) | 3,255 / 2,281 | -0.34 / +0.02 | +0.09 | volum hari isyarat >= 1.5x purata 50 + ATR% >= 4 | -0.51 | RS >= 90 + rejim QQQ ON |
| 239 | M149 3-Step Pullback | 21,829 / 14,767 | -0.04 / -0.29 | +0.09 | MACD > 0 + RS >= 90 | -0.25 | RS >= 90 + rejim QQQ OFF |
| 240 | P42 VCP | 8,688 / 3,586 | +0.38 / +0.65 | +0.09 | ATR% <= 2.5 + tutup dalam 25% teratas julat hari | -0.11 | ATR% <= 2.5 + SPY > SMA200 |
| 241 | M28 VWAP Separator + Kiss Pivot (ditala 2) | 57,652 / 45,030 | +0.07 / -0.05 | +0.08 | ADX < 20 + >= 30% di bawah puncak 52 minggu | +0.28 | RS >= 90 + rejim QQQ ON |
| 242 | M117 Landry Pullback (high 2 bulan) | 22,592 / 13,033 | -0.28 / -0.50 | +0.08 | >= 30% di bawah puncak 52 minggu + tutup dalam 25% teratas julat hari | -0.57 | Supertrend naik + rejim QQQ ON |
| 243 | M78 Alvarez Pecahan Mingguan DTAYS (ditala 1) | 14,589 / 15,586 | +0.03 / +0.00 | +0.08 | MA50 > MA200 + RS >= 90 | +0.07 | RS >= 90 + SPY > SMA200 |
| 244 | M81 Bensdorp Long Trend High Momentum (ditala 1) | 19,384 / 16,944 | +0.03 / -0.21 | +0.07 | ADX < 20 + ATR% >= 4 | +0.17 | >= 30% di bawah puncak 52 minggu + SPY > SMA200 |
| 245 | M54 IBD Power Trend | 50,062 / 29,734 | -0.22 / -0.04 | +0.06 | RS >= 90 + volum hari isyarat >= 1.5x purata 50 | -0.06 | volum hari isyarat >= 1.5x purata 50 + SPY > SMA200 |
| 246 | M23 Breitstein Kapitulasi + Kesinambungan (ditala 2) | 20,007 / 12,319 | -0.09 / +0.00 | +0.06 | RS >= 90 + ATR% >= 4 | +0.25 | RS >= 90 + SPY > SMA200 |
| 247 | N80 Tinggi sepanjang masa | 47,555 / 20,401 | -0.29 / -0.16 | +0.06 | RS >= 90 + volum hari isyarat >= 1.5x purata 50 | -0.12 | ATR% >= 4 + SPY > SMA200 |
| 248 | M147 Improved Three-Bar Pullback | 7,771 / 6,636 | +0.08 / +0.41 | +0.05 | ATR% >= 4 + hari naik (tutup > buka) | -0.29 | rejim QQQ ON + hari naik (tutup > buka) |
| 249 | M51 O'Neil Cawan & Pemegang (ditala 2) | 570 / 324 | +1.51 / +2.21 | +0.05 | MA20 > MA50 + dalam 5% dari puncak 52 minggu | -0.69 | dalam 5% dari puncak 52 minggu + SPY > SMA200 |
| 250 | M10 EMA3 + CCI + MACD | 13,151 / 7,627 | +0.05 / +0.05 | +0.05 | RS >= 90 + hari naik (tutup > buka) | +0.31 | RS >= 90 + SPY > SMA200 |
| 251 | M09 Volumatic VIDYA Pivot Retest | 6,782 / 3,009 | +0.41 / -0.72 | +0.04 | ADX < 20 + volum hari isyarat >= 1.5x purata 50 | -0.95 | volum hari isyarat >= 1.5x purata 50 + SPY > SMA200 |
| 252 | N56 RSI>50 + ADX>20 | 58,877 / 39,386 | -0.27 / -0.20 | +0.04 | MACD > 0 + RS >= 90 | +0.16 | ATR% >= 4 + rejim QQQ ON |
| 253 | M59 Anjakan Julat RSI | 7,305 / 5,044 | +0.01 / +0.66 | +0.04 | ADX > 25 + RS >= 90 | +0.03 | RS >= 90 + rejim QQQ ON |
| 254 | M25 VWAP Wave (proksi harian) | 18,814 / 11,501 | +0.00 / +0.48 | +0.03 | ATR% >= 4 + tutup dalam 25% teratas julat hari | +0.40 | ATR% >= 4 + SPY > SMA200 |
| 255 | M156 Single Penetration (DiNapoli) (ditala 2) | 59,353 / 36,289 | -0.22 / -0.22 | +0.03 | MA50 > MA200 + RS >= 90 | +0.14 | RS >= 90 + SPY > SMA200 |
| 256 | M140 猎豹出击 (Serangan Cheetah) (ditala 1) | 2,002 / 3,104 | +1.71 / +0.27 | +0.02 | >= 30% di bawah puncak 52 minggu + hari naik (tutup > buka) | -0.33 | rejim QQQ OFF + hari naik (tutup > buka) |
| 257 | M151 Outside Bar Failure | 14,126 / 8,896 | -0.04 / -0.14 | +0.01 | RSI14 > 60 + ATR% >= 4 | -0.39 | ATR% >= 4 + rejim QQQ ON |
| 258 | M93 Bollinger Kaedah II: %b + MFI (ditala 1) | 29,472 / 19,387 | -0.14 / +0.06 | +0.01 | RSI14 > 60 + ATR% >= 4 | +0.42 | ATR% >= 4 + SPY > SMA200 |
| 259 | M73 ADX(5) > 40 + Julat Terkecil 6 Hari (ditala 1) | 39,723 / 26,123 | -0.32 / -0.52 | -0.01 | >= 30% di bawah puncak 52 minggu + ATR% >= 4 | -0.57 | RS >= 90 + rejim QQQ ON |
| 260 | M95 Nisbah Kebaharuan High 52 Minggu (Bhootra & Hur) (ditala 1) | 34,912 / 18,826 | -0.26 / -0.15 | -0.01 | RS >= 90 + volum hari isyarat >= 1.5x purata 50 | -0.08 | volum hari isyarat >= 1.5x purata 50 + SPY > SMA200 |
| 261 | N50 Mampat + pecah volum 1.5x | 5,492 / 3,461 | +0.50 / +0.17 | -0.03 | tutup > MA200 + hari naik (tutup > buka) | -0.11 | tutup > MA200 + SPY > SMA200 |
| 262 | M122 Moving Momentum (ChartSchool) (ditala 1) | 17,608 / 11,898 | -0.02 / +0.03 | -0.04 | RS >= 90 + ATR% >= 4 | -0.12 | ADX < 20 + SPY > SMA200 |
| 263 | N35 Pecah 52 minggu tinggi | 57,512 / 31,537 | -0.17 / -0.19 | -0.04 | MA50 naik (lawan 20 bar lalu) + RS >= 90 | +0.07 | RS >= 90 + SPY > SMA200 |
| 264 | M151 Outside Bar Failure (ditala 1) | 14,929 / 9,651 | +0.01 / -0.11 | -0.06 | RSI14 > 60 + ATR% >= 4 | -0.42 | tutup > MA20 + rejim QQQ ON |
| 265 | M06 Minervini VCP Breakout (ditala 2) | 10,660 / 5,620 | +0.44 / +0.37 | -0.07 | ATR% <= 2.5 + tutup dalam 25% teratas julat hari | -0.18 | dalam 15% dari puncak 52 minggu + rejim QQQ ON |
| 266 | M95 Nisbah Kebaharuan High 52 Minggu (Bhootra & Hur) (ditala 2) | 35,878 / 19,312 | -0.27 / -0.19 | -0.07 | RS >= 90 + volum hari isyarat >= 1.5x purata 50 | -0.18 | volum hari isyarat >= 1.5x purata 50 + SPY > SMA200 |
| 267 | M78 Alvarez Pecahan Mingguan DTAYS (ditala 2) | 5,311 / 8,184 | +0.40 / +0.10 | -0.08 | Supertrend naik + RS >= 90 | +0.04 | RS >= 90 + SPY > SMA200 |
| 268 | M160 Measured Move Up | 19,340 / 13,945 | -0.02 / +0.23 | -0.08 | MA50 naik (lawan 20 bar lalu) + ADX < 20 | -0.14 | ADX < 20 + SPY > SMA200 |
| 269 | M48 Cooper 1-2-3-4 (ditala 1) | 6,082 / 4,538 | +0.15 / +0.14 | -0.09 | Supertrend naik + RS >= 90 | -0.61 | dalam 15% dari puncak 52 minggu + SPY > SMA200 |
| 270 | M111 Sistem Volatiliti Wilder | 20,911 / 15,042 | -0.03 / +0.14 | -0.10 | RS >= 90 + tutup dalam 25% teratas julat hari | +0.10 | >= 30% di bawah puncak 52 minggu + rejim QQQ OFF |
| 271 | M145 Yum-Yum Continuation (ditala 1) | 44,438 / 28,426 | -0.23 / -0.11 | -0.10 | MA50 > MA200 + RS >= 90 | +0.08 | RS >= 90 + SPY > SMA200 |
| 272 | M95 Nisbah Kebaharuan High 52 Minggu (Bhootra & Hur) | 34,395 / 18,560 | -0.27 / -0.20 | -0.11 | volum hari isyarat >= 1.5x purata 50 + hari naik (tutup > buka) | -0.16 | volum hari isyarat >= 1.5x purata 50 + SPY > SMA200 |
| 273 | M145 Yum-Yum Continuation | 37,663 / 24,252 | -0.22 / +0.01 | -0.12 | RS >= 90 + tutup dalam 25% teratas julat hari | +0.06 | RS >= 90 + SPY > SMA200 |
| 274 | M88 O'Neil Shakeout +3 (ditala 1) | 3,317 / 4,365 | -0.08 / +0.43 | -0.14 | RSI14 < 40 + >= 30% di bawah puncak 52 minggu | -0.38 | >= 30% di bawah puncak 52 minggu + SPY > SMA200 |
| 275 | M100 Bulkowski Segi Empat & Segi Tiga Menaik (ditala 2) | 18,071 / 8,412 | -0.22 / -0.13 | -0.14 | volum hari isyarat >= 1.5x purata 50 + ATR% <= 2.5 | -0.26 | rejim QQQ ON + tutup dalam 25% teratas julat hari |
| 276 | N24 Supertrend(10,3) + ADX>20 | 29,416 / 20,004 | -0.29 / -0.12 | -0.14 | MACD > 0 + >= 30% di bawah puncak 52 minggu | -0.10 | ATR% >= 4 + rejim QQQ ON |
| 277 | M82 Arthur Hill Rotasi Sasaran 10% (ditala 1) | 8,068 / 6,291 | -0.04 / +0.01 | -0.14 | MA50 > MA200 + MA50 naik (lawan 20 bar lalu) | -0.12 | RS >= 70 + rejim QQQ ON |
| 278 | M39 Radge Pecahan Bollinger 100 hari (ditala 2) | 24,079 / 16,522 | -0.31 / -0.39 | -0.14 | RS >= 90 + ATR% >= 4 | +0.02 | RS >= 90 + SPY > SMA200 |
| 279 | N39 NR7 kemudian pecah | 19,162 / 11,420 | -0.16 / -0.11 | -0.15 | MA50 > MA200 + volum hari isyarat >= 1.5x purata 50 | -0.26 | templat trend Minervini + SPY > SMA200 |
| 280 | M02 MACD + SMA200 | 17,333 / 11,164 | -0.20 / -0.10 | -0.15 | MA50 naik (lawan 20 bar lalu) + ADX < 20 | -0.12 | ADX < 20 + SPY > SMA200 |
| 281 | M06 Minervini VCP Breakout | 11,291 / 5,966 | +0.32 / +0.45 | -0.15 | volum hari isyarat >= 1.5x purata 50 + ATR% <= 2.5 | -0.10 | MA50 naik (lawan 20 bar lalu) + SPY > SMA200 |
| 282 | M82 Arthur Hill Rotasi Sasaran 10% | 8,191 / 6,533 | +0.05 / +0.22 | -0.16 | MA50 > MA200 | -0.13 | MA50 > MA200 + SPY > SMA200 |
| 283 | M21 Marius 3 Persediaan (Pecahan+Jurang+Kesinambungan) (ditala 1) | 249 / 688 | +6.46 / +1.16 | -0.16 | MA50 > MA200 + hari naik (tutup > buka) | +1.13 | RS >= 90 + SPY > SMA200 |
| 284 | M81 Bensdorp Long Trend High Momentum | 14,541 / 10,512 | -0.15 / +0.04 | -0.16 | ATR% >= 4 | +0.10 | ATR% >= 4 + SPY > SMA200 |
| 285 | M29 EMA3 + RSI75 + Stokastik | 7,220 / 4,344 | +0.04 / +0.09 | -0.17 | MA50 > MA200 + ATR% >= 4 | -0.60 | MA50 > MA200 + SPY > SMA200 |
| 286 | M137 Livermore System (ditala 2) | 49,238 / 32,080 | -0.20 / -0.11 | -0.18 | MA50 > MA200 + tutup dalam 25% teratas julat hari | -0.22 | MA50 > MA200 + rejim QQQ ON |
| 287 | M111 Sistem Volatiliti Wilder (ditala 2) | 20,559 / 14,818 | -0.06 / +0.14 | -0.18 | templat trend Minervini + MACD > 0 | -0.12 | templat trend Minervini + SPY > SMA200 |
| 288 | M34 Carter TTM Squeeze (ditala 1) | 20,238 / 12,316 | -0.07 / +0.02 | -0.18 | ADX < 20 + ATR% >= 4 | -0.25 | ADX < 20 + SPY > SMA200 |
| 289 | P20 squeeze lepas ke atas | 28,249 / 18,695 | -0.22 / -0.10 | -0.18 | RS >= 70 + ATR% >= 4 | -0.22 | ATR% <= 2.5 + SPY > SMA200 |
| 290 | M51 O'Neil Cawan & Pemegang (ditala 1) | 701 / 359 | +0.94 / +1.95 | -0.20 | MA20 > MA50 + dalam 5% dari puncak 52 minggu | -0.68 | dalam 5% dari puncak 52 minggu + SPY > SMA200 |
| 291 | M54 IBD Power Trend (ditala 1) | 30,690 / 19,013 | -0.22 / -0.13 | -0.20 | RS >= 90 + ATR% >= 4 | -0.18 | RS >= 90 + SPY > SMA200 |
| 292 | M44 Tapak Rata IBD (ditala 1) | 1,312 / 1,380 | -0.15 / +1.61 | -0.20 | MACD > 0 + ADX < 20 | -0.48 | ADX < 20 + SPY > SMA200 |
| 293 | M100 Bulkowski Segi Empat & Segi Tiga Menaik (ditala 1) | 24,304 / 11,889 | -0.12 / -0.23 | -0.20 | RS >= 90 + volum hari isyarat >= 1.5x purata 50 | -0.23 | ATR% <= 2.5 + SPY > SMA200 |
| 294 | M30 BB Free Bar + Himpitan 50/2.5 (ditala 2) | 10,722 / 7,282 | +0.03 / +0.19 | -0.22 | volum hari isyarat >= 1.5x purata 50 + hari naik (tutup > buka) | -0.15 | volum hari isyarat >= 1.5x purata 50 + SPY > SMA200 |
| 295 | N65 Gap 4% + volum + hampir 52w | 2,247 / 1,864 | +0.30 / +0.34 | -0.22 | Supertrend naik + RS >= 90 | +0.01 | RS >= 90 + SPY > SMA200 |
| 296 | M33 Supertrend + SMA10 (ditala 2) | 12,589 / 6,367 | -0.02 / +0.15 | -0.23 | tutup > MA200 + MA50 naik (lawan 20 bar lalu) | -0.31 | rejim QQQ ON + tutup dalam 25% teratas julat hari |
| 297 | N37 Gap and go | 4,327 / 4,716 | +0.12 / -0.17 | -0.23 | Supertrend naik + RS >= 90 | -0.53 | ATR% >= 4 + SPY > SMA200 |
| 298 | P34 pecah tapak 3 bulan + volum | 15,042 / 6,949 | -0.14 / -0.25 | -0.24 | MA50 > MA200 + ATR% <= 2.5 | -0.28 | ATR% <= 2.5 + SPY > SMA200 |
| 299 | M28 VWAP Separator + Kiss Pivot (ditala 1) | 27,819 / 22,668 | +0.13 / -0.10 | -0.25 | RSI14 < 40 + >= 30% di bawah puncak 52 minggu | -0.24 | ATR% >= 4 + rejim QQQ ON |
| 300 | M135 3rd Watch (ditala 1) | 2,867 / 1,593 | +0.03 / +0.59 | -0.25 | ATR% <= 2.5 + tutup dalam 25% teratas julat hari | -0.39 | ATR% <= 2.5 + SPY > SMA200 |
| 301 | M122 Moving Momentum (ChartSchool) (ditala 2) | 13,451 / 9,079 | -0.16 / +0.20 | -0.25 | MACD > 0 + ADX < 20 | -0.16 | ATR% >= 4 + rejim QQQ ON |
| 302 | N57 ADX bangkit daripada <20 | 18,833 / 13,186 | -0.22 / +0.10 | -0.26 | RSI14 > 60 + >= 30% di bawah puncak 52 minggu | -0.15 | >= 30% di bawah puncak 52 minggu + SPY > SMA200 |
| 303 | M02 MACD + SMA200 (ditala 1) | 19,430 / 12,141 | -0.18 / -0.21 | -0.27 | >= 30% di bawah puncak 52 minggu + volum 10 hari > volum 50 hari | -0.22 | ADX < 20 + rejim QQQ ON |
| 304 | M119 180 Bullish (Cooper) | 21,872 / 16,730 | -0.36 / +0.15 | -0.27 | MA50 naik (lawan 20 bar lalu) + RS >= 90 | -0.08 | RS >= 90 + SPY > SMA200 |
| 305 | P38 bangkit dari jatuh (silang MA50 + volum) | 494 / 837 | +1.16 / +2.71 | -0.27 | ATR% >= 4 + hari naik (tutup > buka) | -0.93 | rejim QQQ ON + SPY > SMA200 |
| 306 | P30 gap and go | 4,364 / 4,795 | +0.17 / -0.19 | -0.28 | Supertrend naik + RS >= 90 | -0.54 | ATR% >= 4 + SPY > SMA200 |
| 307 | M131 Ross Hook (Joe Ross) (ditala 1) | 31,477 / 20,749 | -0.11 / -0.09 | -0.29 | ATR% <= 2.5 + tutup dalam 25% teratas julat hari | -0.22 | rejim QQQ ON + SPY > SMA200 |
| 308 | M131 Ross Hook (Joe Ross) (ditala 2) | 31,477 / 20,749 | -0.11 / -0.09 | -0.29 | ATR% <= 2.5 + tutup dalam 25% teratas julat hari | -0.22 | rejim QQQ ON + SPY > SMA200 |
| 309 | M131 Ross Hook (Joe Ross) | 31,477 / 20,749 | -0.11 / -0.09 | -0.29 | ATR% <= 2.5 + tutup dalam 25% teratas julat hari | -0.22 | rejim QQQ ON + SPY > SMA200 |
| 310 | M150 Trend Bar Failure (Brooks) (ditala 1) | 10,683 / 6,960 | -0.14 / +0.12 | -0.29 | MA50 naik (lawan 20 bar lalu) + ATR% >= 4 | +0.04 | ATR% >= 4 + SPY > SMA200 |
| 311 | M147 Improved Three-Bar Pullback (ditala 2) | 7,183 / 6,039 | +0.07 / +0.18 | -0.30 | RSI14 > 50 + volum hari isyarat >= 1.5x purata 50 | -0.38 | SPY > SMA200 + hari naik (tutup > buka) |
| 312 | M118 Expansion Pivot (Cooper) (ditala 1) | 11,701 / 8,354 | +0.01 / +0.05 | -0.31 | RSI14 > 50 + hari naik (tutup > buka) | -0.19 | SPY > SMA200 + hari naik (tutup > buka) |
| 313 | M26 Garis Trend Undur 3 Sentuhan + Pecahan (ditala 2) | 6,885 / 4,501 | -0.10 / +0.09 | -0.31 | ADX < 20 + squeeze hidup | -0.35 | ADX < 20 + SPY > SMA200 |
| 314 | M117 Landry Pullback (high 2 bulan) (ditala 2) | 23,704 / 14,065 | -0.29 / -0.43 | -0.31 | Supertrend naik + ATR% >= 4 | -0.51 | RS >= 70 + rejim QQQ ON |
| 315 | M79 Radge: 20% Flipper (ditala 1) | 6,838 / 8,960 | +0.10 / -0.42 | -0.32 | RSI14 > 60 + ATR% >= 4 | -0.15 | MA50 > MA200 + SPY > SMA200 |
| 316 | M129 Wick Play (ditala 1) | 4,608 / 3,498 | -0.02 / +0.11 | -0.32 | templat trend Minervini + RS >= 70 | -0.33 | templat trend Minervini + SPY > SMA200 |
| 317 | M100 Bulkowski Segi Empat & Segi Tiga Menaik | 11,070 / 4,557 | -0.13 / -0.07 | -0.32 | templat trend Minervini + hari naik (tutup > buka) | -0.41 | MA50 > MA200 + rejim QQQ ON |
| 318 | M33 Supertrend + SMA10 | 13,736 / 8,956 | -0.06 / +0.00 | -0.33 | tutup > MA50 + MACD > isyarat | -0.23 | RSI14 > 60 + rejim QQQ ON |
| 319 | M119 180 Bullish (Cooper) (ditala 1) | 11,907 / 9,646 | -0.17 / +0.35 | -0.33 | RS >= 90 + hari naik (tutup > buka) | +0.14 | ATR% >= 4 + rejim QQQ ON |
| 320 | M105 Supertrend tulen | 24,727 / 17,923 | -0.16 / -0.28 | -0.35 | tutup > MA50 + MACD > isyarat | -0.25 | RSI14 > 60 + SPY > SMA200 |
| 321 | M19 Sneaky Pivot (proksi harian) (ditala 2) | 18,038 / 14,103 | -0.46 / +0.09 | -0.35 | MA50 naik (lawan 20 bar lalu) + ADX < 20 | -0.06 | ADX < 20 + SPY > SMA200 |
| 322 | P21 Supertrend bertukar naik | 24,763 / 17,943 | -0.15 / -0.28 | -0.35 | tutup > MA50 + MACD > isyarat | -0.26 | RSI14 > 60 + SPY > SMA200 |
| 323 | M134 First Kiss After Daylight (Landry) | 5,460 / 4,123 | -0.12 / +0.83 | -0.36 | MACD > isyarat + ADX < 20 | -0.34 | ADX < 20 + rejim QQQ ON |
| 324 | M150 Trend Bar Failure (Brooks) | 11,725 / 7,732 | -0.02 / +0.06 | -0.36 | tutup > MA200 + tutup dalam 25% teratas julat hari | -0.22 | SPY > SMA200 + tutup dalam 25% teratas julat hari |
| 325 | M137 Livermore System (ditala 1) | 23,600 / 14,633 | -0.13 / -0.30 | -0.36 | templat trend Minervini + tutup dalam 25% teratas julat hari | -0.25 | templat trend Minervini + rejim QQQ ON |
| 326 | M101 Bulkowski: Tiga lembah menaik | 12,907 / 7,074 | -0.21 / -0.32 | -0.37 | RS >= 90 + volum hari isyarat >= 1.5x purata 50 | -0.52 | ATR% <= 2.5 + SPY > SMA200 |
| 327 | M139 均线首次粘合向上发散 (MA berhimpun kali pertama, berkipas naik) | 10,244 / 7,019 | -0.24 / -0.08 | -0.38 | MA50 > MA200 + ATR% >= 4 | -0.07 | ATR% >= 4 + rejim QQQ ON |
| 328 | M25 VWAP Wave (proksi harian) (ditala 1) | 9,772 / 5,834 | -0.01 / +0.32 | -0.39 | tiada | -0.12 | ADX < 20 + rejim QQQ ON |
| 329 | M101 Bulkowski: Tiga lembah menaik (ditala 1) | 12,913 / 7,081 | -0.23 / -0.31 | -0.39 | RS >= 90 + volum hari isyarat >= 1.5x purata 50 | -0.52 | ATR% <= 2.5 + SPY > SMA200 |
| 330 | M101 Bulkowski: Tiga lembah menaik (ditala 2) | 12,914 / 7,081 | -0.23 / -0.31 | -0.39 | RS >= 90 + volum hari isyarat >= 1.5x purata 50 | -0.52 | ATR% <= 2.5 + SPY > SMA200 |
| 331 | M74 Lulus Baharu Trend Template Minervini (ditala 1) | 5,641 / 3,886 | -0.13 / +0.29 | -0.39 | MACD > 0 + ATR% <= 2.5 | -0.41 | ATR% <= 2.5 + SPY > SMA200 |
| 332 | M111 Sistem Volatiliti Wilder (ditala 1) | 16,755 / 11,903 | -0.16 / +0.08 | -0.40 | MACD > isyarat + hari naik (tutup > buka) | -0.26 | templat trend Minervini + rejim QQQ ON |
| 333 | M34 Carter TTM Squeeze | 15,507 / 9,600 | -0.10 / -0.05 | -0.40 | tutup > MA20 + ADX < 20 | -0.40 | MA50 naik (lawan 20 bar lalu) + SPY > SMA200 |
| 334 | M68 Kell Base n' Break (ditala 2) | 6,902 / 3,031 | -0.12 / +0.17 | -0.40 | MA50 naik (lawan 20 bar lalu) + Supertrend naik | -0.49 | tutup > MA200 + SPY > SMA200 |
| 335 | M99 Three Line Break | 20,362 / 12,962 | -0.23 / -0.09 | -0.41 | templat trend Minervini + hari naik (tutup > buka) | -0.01 | ATR% >= 4 + rejim QQQ ON |
| 336 | M30 BB Free Bar + Himpitan 50/2.5 | 11,575 / 8,080 | +0.08 / -0.08 | -0.41 | MACD > isyarat + volum hari isyarat >= 1.5x purata 50 | -0.21 | RS >= 70 + rejim QQQ ON |
| 337 | P14 RSI14 silang atas 30 | 18,476 / 14,508 | -0.15 / -0.05 | -0.42 | >= 30% di bawah puncak 52 minggu | -0.21 | >= 30% di bawah puncak 52 minggu + rejim QQQ OFF |
| 338 | M26 Garis Trend Undur 3 Sentuhan + Pecahan (ditala 1) | 7,180 / 4,760 | +0.17 / -0.06 | -0.42 | ADX < 20 + hari naik (tutup > buka) | -0.47 | ADX < 20 + SPY > SMA200 |
| 339 | M26 Garis Trend Undur 3 Sentuhan + Pecahan | 7,411 / 4,869 | -0.02 / +0.00 | -0.44 | ADX < 20 + hari naik (tutup > buka) | -0.51 | ADX < 20 + SPY > SMA200 |
| 340 | M134 First Kiss After Daylight (Landry) (ditala 2) | 5,392 / 3,805 | -0.12 / +1.01 | -0.44 | MA20 > MA50 + RS >= 70 | -0.38 | rejim QQQ ON + SPY > SMA200 |
| 341 | M46 Jurang Naik Boleh Beli (Buyable Gap Up) | 2,183 / 1,463 | +0.45 / -0.02 | -0.45 | volum 10 hari > volum 50 hari + ATR% >= 4 | -1.20 | dalam 15% dari puncak 52 minggu + SPY > SMA200 |
| 342 | M129 Wick Play | 4,509 / 3,365 | -0.13 / +0.47 | -0.46 | templat trend Minervini + ADX > 25 | -0.46 | MA50 > MA200 + SPY > SMA200 |
| 343 | M146 3-Bar Momentum Pattern (ditala 2) | 4,274 / 3,033 | +0.03 / +0.50 | -0.46 | RSI14 > 60 + Supertrend naik | -0.35 | MACD > isyarat + SPY > SMA200 |
| 344 | M80 Radge Saluran Purata Bergerak (MAC) | 32,140 / 21,750 | -0.34 / -0.36 | -0.47 | MA50 > MA200 + ADX < 20 | -0.31 | >= 30% di bawah puncak 52 minggu + SPY > SMA200 |
| 345 | M127 Slingshot Bullish (ditala 1) | 12,972 / 7,922 | -0.41 / -0.25 | -0.47 | MA50 > MA200 + ATR% <= 2.5 | -0.47 | rejim QQQ ON + SPY > SMA200 |
| 346 | M90 Pring KST (ditala 1) | 14,149 / 8,773 | -0.35 / +0.13 | -0.48 | MA50 naik (lawan 20 bar lalu) + ADX < 20 | -0.43 | ADX < 20 + rejim QQQ ON |
| 347 | P39 volum kering kemudian meletup | 5,534 / 3,857 | +0.35 / +0.01 | -0.48 | RSI14 > 50 + >= 30% di bawah puncak 52 minggu | -0.37 | >= 30% di bawah puncak 52 minggu + SPY > SMA200 |
| 348 | M67 Rayner Teo: Ujian Ketiga pada Purata 50 | 5,188 / 2,980 | -0.24 / +0.73 | -0.48 | RS >= 90 + dalam 15% dari puncak 52 minggu | -0.56 | RS >= 90 + SPY > SMA200 |
| 349 | M02 MACD + SMA200 (ditala 2) | 13,460 / 8,739 | -0.27 / -0.14 | -0.48 | RSI14 > 50 + ADX < 20 | -0.43 | RSI14 > 50 + SPY > SMA200 |
| 350 | M107 Golden Cross SMA50/200 (ditala 2) | 6,347 / 4,390 | +0.13 / +0.18 | -0.49 | tiada | -0.44 | SPY > SMA200 |
| 351 | M34 Carter TTM Squeeze (ditala 2) | 20,173 / 12,446 | -0.15 / -0.34 | -0.50 | MA50 naik (lawan 20 bar lalu) + RSI14 > 60 | -0.31 | MA50 naik (lawan 20 bar lalu) + SPY > SMA200 |
| 352 | M142 Pecahan volum dari dasar (底部放量) | 3,383 / 2,316 | -0.44 / -0.04 | -0.50 | volum hari isyarat >= 1.5x purata 50 + ATR% >= 4 | -0.66 | RS >= 90 + rejim QQQ ON |
| 353 | M33 Supertrend + SMA10 (ditala 1) | 9,011 / 5,690 | -0.34 / +0.41 | -0.50 | MACD > 0 + hari naik (tutup > buka) | -0.54 | RSI14 > 60 + SPY > SMA200 |
| 354 | N53 Supertrend + ADX>25 | 22,079 / 14,741 | -0.44 / -0.27 | -0.51 | MACD > 0 + volum hari isyarat >= 1.5x purata 50 | -0.49 | ATR% >= 4 + rejim QQQ ON |
| 355 | M106 DMI Wilder | 11,266 / 7,303 | -0.48 / -0.28 | -0.52 | MA50 naik (lawan 20 bar lalu) + hari naik (tutup > buka) | -0.37 | ATR% >= 4 + SPY > SMA200 |
| 356 | M123 CCI Correction (Lambert, ChartSchool) (ditala 1) | 17,795 / 10,978 | -0.27 / -0.44 | -0.52 | MACD > isyarat + ATR% <= 2.5 | -0.44 | RS >= 70 + SPY > SMA200 |
| 357 | M132 Ascending Scallop (Bulkowski) (ditala 1) | 8,432 / 5,399 | -0.23 / +0.22 | -0.53 | RSI14 > 60 + dalam 15% dari puncak 52 minggu | -0.47 | dalam 15% dari puncak 52 minggu + SPY > SMA200 |
| 358 | M80 Radge Saluran Purata Bergerak (MAC) (ditala 2) | 25,891 / 17,881 | -0.44 / +0.00 | -0.54 | tutup > MA50 + ATR% <= 2.5 | -0.20 | >= 30% di bawah puncak 52 minggu + SPY > SMA200 |
| 359 | M03 BB Break + Divergence RSI (ditala 2) | 25,112 / 17,911 | -0.20 / -0.41 | -0.56 | MA50 > MA200 + >= 30% di bawah puncak 52 minggu | -0.53 | >= 30% di bawah puncak 52 minggu + SPY > SMA200 |
| 360 | M127 Slingshot Bullish (ditala 2) | 11,437 / 7,012 | -0.42 / -0.24 | -0.57 | MA50 > MA200 + ATR% <= 2.5 | -0.52 | MA50 > MA200 + SPY > SMA200 |
| 361 | M46 Jurang Naik Boleh Beli (Buyable Gap Up) (ditala 1) | 2,659 / 1,807 | +0.03 / +0.52 | -0.58 | MA20 > MA50 + MACD > isyarat | -0.66 | MA20 > MA50 + SPY > SMA200 |
| 362 | M89 Chande 65sma-3cc (ditala 1) | 15,387 / 10,363 | -0.12 / -0.22 | -0.58 | tutup > MA20 + ADX < 20 | -0.72 | ADX < 20 + SPY > SMA200 |
| 363 | M127 Slingshot Bullish | 10,048 / 5,993 | -0.45 / -0.44 | -0.58 | RS >= 70 + ATR% <= 2.5 | -0.58 | MA50 > MA200 + rejim QQQ ON |
| 364 | M150 Trend Bar Failure (Brooks) (ditala 2) | 8,707 / 5,781 | -0.28 / +0.11 | -0.58 | Supertrend naik + hari naik (tutup > buka) | -0.52 | Supertrend naik + SPY > SMA200 |
| 365 | M25 VWAP Wave (proksi harian) (ditala 2) | 11,755 / 7,227 | -0.28 / -0.23 | -0.58 | ADX < 20 + tutup dalam 25% teratas julat hari | -0.44 | ADX < 20 + SPY > SMA200 |
| 366 | P22 ADX silang atas 25 & +DI>-DI | 16,731 / 11,442 | -0.35 / -0.02 | -0.58 | tutup > MA20 + tutup > MA200 | -0.49 | SPY > SMA200 |
| 367 | M48 Cooper 1-2-3-4 | 6,189 / 4,876 | -0.16 / -0.32 | -0.59 | RS >= 70 + squeeze hidup | -0.83 | RS >= 70 + SPY > SMA200 |
| 368 | N124 Episodic pivot gap 8-10% | 1,667 / 2,216 | +0.40 / -0.24 | -0.60 | tutup > MA20 + ATR% >= 4 | -0.81 | ATR% >= 4 + SPY > SMA200 |
| 369 | M99 Three Line Break (ditala 1) | 8,770 / 5,654 | -0.24 / -0.05 | -0.60 | tutup > MA50 + MA50 > MA200 | +0.30 | ATR% >= 4 + rejim QQQ ON |
| 370 | M132 Ascending Scallop (Bulkowski) (ditala 2) | 8,122 / 5,161 | -0.30 / +0.14 | -0.61 | MA50 > MA200 + dalam 15% dari puncak 52 minggu | -0.57 | dalam 15% dari puncak 52 minggu + rejim QQQ ON |
| 371 | N64 Episodic pivot | 3,355 / 3,086 | -0.03 / -0.29 | -0.61 | RSI14 > 50 + ATR% >= 4 | -0.73 | ATR% >= 4 + rejim QQQ ON |
| 372 | M148 Natural Number Method (ditala 2) | 14,537 / 12,122 | -0.31 / -0.15 | -0.61 | tiada | -0.47 | RSI14 > 60 + rejim QQQ ON |
| 373 | M96 Momo India: Ranking Sharpe 3/6/12 bulan | 681 / 390 | +1.78 / +2.25 | -0.62 | MA20 > MA50 + RSI14 > 50 | -0.07 | ADX > 25 + rejim QQQ ON |
| 374 | M146 3-Bar Momentum Pattern (ditala 1) | 3,372 / 2,379 | -0.27 / +0.05 | -0.62 | MA50 > MA200 + tutup dalam 25% teratas julat hari | -0.70 | MA50 > MA200 + SPY > SMA200 |
| 375 | M91 Stochastic Pop (Bernstein/Steckler) (ditala 1) | 2,538 / 1,636 | -0.07 / +0.90 | -0.64 | RSI14 > 60 + hari naik (tutup > buka) | -0.47 | SPY > SMA200 + hari naik (tutup > buka) |
| 376 | M96 Momo India: Ranking Sharpe 3/6/12 bulan (ditala 1) | 675 / 389 | +1.84 / +2.34 | -0.66 | ADX > 25 + RS >= 90 | -0.50 | rejim QQQ ON + hari naik (tutup > buka) |
| 377 | M128 Inventory Retracement Bar (IRB, Rob Hoffman) (ditala 2) | 8,559 / 6,206 | +0.12 / -0.43 | -0.67 | MA50 > MA200 + RS >= 70 | -0.69 | RS >= 70 + SPY > SMA200 |
| 378 | M132 Ascending Scallop (Bulkowski) | 7,545 / 4,778 | -0.43 / +0.18 | -0.68 | MA50 > MA200 + dalam 15% dari puncak 52 minggu | -0.66 | templat trend Minervini + rejim QQQ ON |
| 379 | P36 tinggi 52 minggu pertama selepas 6 bulan | 3,534 / 2,329 | -0.04 / -0.39 | -0.69 | ATR% <= 2.5 + tutup dalam 25% teratas julat hari | -0.82 | ATR% <= 2.5 + SPY > SMA200 |
| 380 | M135 3rd Watch (ditala 2) | 2,561 / 1,351 | -0.14 / -0.29 | -0.71 | MA50 naik (lawan 20 bar lalu) + dalam 5% dari puncak 52 minggu | -0.84 | dalam 5% dari puncak 52 minggu + SPY > SMA200 |
| 381 | M76 Undercut & Rally pada Low Penting | 5,471 / 3,563 | +0.10 / -0.08 | -0.71 | ADX < 20 + RS >= 70 | -0.88 | SPY > SMA200 + tutup dalam 25% teratas julat hari |
| 382 | M74 Lulus Baharu Trend Template Minervini | 7,043 / 4,791 | +0.00 / -0.35 | -0.72 | MA50 naik (lawan 20 bar lalu) + ATR% <= 2.5 | -0.75 | MACD > isyarat + rejim QQQ ON |
| 383 | M09 Volumatic VIDYA Pivot Retest (ditala 2) | 5,192 / 2,308 | +0.26 / -0.69 | -0.72 | RS >= 70 + dalam 5% dari puncak 52 minggu | -0.92 | SPY > SMA200 + tutup dalam 25% teratas julat hari |
| 384 | M91 Stochastic Pop (Bernstein/Steckler) | 4,195 / 2,751 | -0.01 / -0.07 | -0.75 | MA50 > MA200 + dalam 15% dari puncak 52 minggu | -0.60 | MA50 > MA200 + rejim QQQ ON |
| 385 | M99 Three Line Break (ditala 2) | 13,487 / 8,312 | -0.31 / -0.44 | -0.75 | MA50 naik (lawan 20 bar lalu) + dalam 15% dari puncak 52 minggu | -0.63 | MACD > isyarat + rejim QQQ ON |
| 386 | M134 First Kiss After Daylight (Landry) (ditala 1) | 5,262 / 3,980 | -0.32 / +0.00 | -0.75 | tutup > MA20 + hari naik (tutup > buka) | -0.86 | Supertrend naik + rejim QQQ ON |
| 387 | M133 Bull Hook (Crabel) (ditala 1) | 5,746 / 4,340 | -0.17 / -0.37 | -0.76 | ATR% <= 2.5 + hari naik (tutup > buka) | -0.57 | rejim QQQ ON + SPY > SMA200 |
| 388 | M133 Bull Hook (Crabel) (ditala 2) | 5,746 / 4,340 | -0.17 / -0.37 | -0.76 | ATR% <= 2.5 + hari naik (tutup > buka) | -0.57 | rejim QQQ ON + SPY > SMA200 |
| 389 | M133 Bull Hook (Crabel) | 5,745 / 4,340 | -0.17 / -0.37 | -0.76 | ATR% <= 2.5 + hari naik (tutup > buka) | -0.57 | rejim QQQ ON + SPY > SMA200 |
| 390 | M146 3-Bar Momentum Pattern | 6,865 / 4,806 | +0.03 / -0.30 | -0.76 | MA20 > MA50 + RS >= 70 | -0.61 | tutup > MA200 + rejim QQQ ON |
| 391 | M04 BB Squeeze Breakout (ditala 1) | 4,696 / 3,097 | -0.03 / -0.19 | -0.81 | MA50 naik (lawan 20 bar lalu) + dalam 5% dari puncak 52 minggu | -0.73 | volum hari isyarat >= 1.5x purata 50 + rejim QQQ ON |
| 392 | M126 Hidden Smash Day (beli, Larry Williams) (ditala 1) | 1,305 / 1,160 | +0.16 / +0.25 | -0.82 | MA20 > MA50 + hari naik (tutup > buka) | -0.70 | Supertrend naik + SPY > SMA200 |
| 393 | M77 Undercut & Rally pada Purata Bergerak (MAU&R) (ditala 1) | 3,042 / 1,807 | +0.13 / -0.23 | -0.84 | MA50 > MA200 + dalam 15% dari puncak 52 minggu | -0.86 | dalam 15% dari puncak 52 minggu + SPY > SMA200 |
| 394 | M140 猎豹出击 (Serangan Cheetah) | 1,435 / 2,234 | +0.32 / +1.33 | -0.87 | ADX < 20 + ATR% >= 4 | -0.53 | ATR% >= 4 + SPY > SMA200 |
| 395 | M129 Wick Play (ditala 2) | 3,292 / 2,557 | -0.57 / +0.22 | -0.87 | MA20 > MA50 + ATR% <= 2.5 | -0.80 | ATR% <= 2.5 + rejim QQQ ON |
| 396 | M117 Landry Pullback (high 2 bulan) (ditala 1) | 17,373 / 8,781 | -0.40 / -0.87 | -0.89 | MA20 > MA50 + ATR% <= 2.5 | -0.80 | ATR% <= 2.5 + rejim QQQ ON |
| 397 | M67 Rayner Teo: Ujian Ketiga pada Purata 50 (ditala 1) | 1,963 / 1,106 | +0.46 / +0.26 | -0.90 | RS >= 70 + hari naik (tutup > buka) | -1.05 | ATR% >= 4 + SPY > SMA200 |
| 398 | M19 Sneaky Pivot (proksi harian) (ditala 1) | 8,513 / 6,032 | -0.75 / +0.21 | -0.94 | ADX < 20 | -0.62 | ADX < 20 + SPY > SMA200 |
| 399 | M148 Natural Number Method (ditala 1) | 7,426 / 6,669 | -0.61 / -0.43 | -0.94 | tutup > MA50 + MA50 > MA200 | -0.90 | ATR% <= 2.5 + rejim QQQ ON |
| 400 | M05 MACD Divergence + Pengesahan (ditala 2) | 3,432 / 2,333 | -0.55 / +0.77 | -0.95 | tutup > MA50 + hari naik (tutup > buka) | -0.88 | MA20 > MA50 + SPY > SMA200 |
| 401 | M38 Darvas Kotak (ditala 1) | 1,991 / 1,283 | -0.45 / +0.22 | -0.96 | MA20 > MA50 + Supertrend naik | -1.02 | MA50 naik (lawan 20 bar lalu) + SPY > SMA200 |
| 402 | M28 VWAP Separator + Kiss Pivot | 9,252 / 6,998 | -0.18 / -0.31 | -0.97 | tiada | -1.01 | MA20 > MA50 + rejim QQQ OFF |
| 403 | M38 Darvas Kotak (ditala 2) | 1,307 / 986 | -0.34 / +0.92 | -0.99 | MA50 > MA200 + MACD > 0 | -0.85 | MA50 > MA200 + SPY > SMA200 |
| 404 | M120 Reversal New Highs | 1,585 / 1,222 | -0.32 / -0.46 | -0.99 | tutup dalam 25% teratas julat hari + hari naik (tutup > buka) | -1.16 | volum hari isyarat >= 1.5x purata 50 + SPY > SMA200 |
| 405 | P33 lonjakan selepas tidur (julat 60 hari <=30%) | 4,134 / 2,177 | -0.15 / -0.70 | -1.00 | RSI14 > 60 + ADX > 25 | -1.06 | RSI14 > 50 + rejim QQQ ON |
| 406 | P37 Stage 1->2 (silang MA150 mendatar + volum) | 1,962 / 1,350 | +0.05 / +0.04 | -1.01 | tutup > MA20 + tutup dalam 25% teratas julat hari | -0.80 | tutup > MA20 + SPY > SMA200 |
| 407 | M130 多方炮 (dua lilin hijau mengapit satu merah) (ditala 2) | 1,603 / 949 | +0.18 / +0.15 | -1.01 | MACD > isyarat + ADX < 20 | -0.90 | ADX < 20 + rejim QQQ ON |
| 408 | M41 FW Penyatuan Mingguan (ditala 2) | 3,976 / 2,661 | -0.75 / -0.50 | -1.02 | MA50 > MA200 + hari naik (tutup > buka) | -1.20 | SPY > SMA200 + hari naik (tutup > buka) |
| 409 | M10 EMA3 + CCI + MACD (ditala 2) | 2,687 / 1,495 | -0.29 / +0.10 | -1.02 | MACD > isyarat | -0.87 | volum 10 hari > volum 50 hari + SPY > SMA200 |
| 410 | M139 均线首次粘合向上发散 (MA berhimpun kali pertama, berkipas naik) (ditala 1) | 5,026 / 3,258 | -0.67 / -0.36 | -1.03 | MACD > 0 + Supertrend naik | -0.95 | rejim QQQ ON |
| 411 | M126 Hidden Smash Day (beli, Larry Williams) | 2,764 / 2,158 | +0.06 / -0.66 | -1.03 | MA20 > MA50 + ATR% <= 2.5 | -1.01 | ATR% <= 2.5 + SPY > SMA200 |
| 412 | M157 Consolidation Pivot Breakout (versi angka) | 2,455 / 1,866 | -0.58 / -0.15 | -1.05 | MA50 naik (lawan 20 bar lalu) + tutup dalam 25% teratas julat hari | -1.06 | rejim QQQ ON + tutup dalam 25% teratas julat hari |
| 413 | M38 Darvas Kotak | 2,022 / 1,337 | -0.12 / -0.06 | -1.06 | MA50 naik (lawan 20 bar lalu) + MACD > isyarat | -1.15 | MACD > isyarat + SPY > SMA200 |
| 414 | M126 Hidden Smash Day (beli, Larry Williams) (ditala 2) | 5,415 / 3,876 | +0.03 / -0.64 | -1.07 | MA20 > MA50 + ATR% <= 2.5 | -1.02 | ATR% <= 2.5 + SPY > SMA200 |
| 415 | M115 Bow Tie (Landry) (ditala 1) | 1,778 / 1,306 | -0.55 / -0.09 | -1.09 | MA50 > MA200 + ATR% <= 2.5 | -1.20 | MACD > isyarat + SPY > SMA200 |
| 416 | M46 Jurang Naik Boleh Beli (Buyable Gap Up) (ditala 2) | 2,210 / 1,502 | +0.04 / -0.01 | -1.09 | volum 10 hari > volum 50 hari + ATR% >= 4 | -1.26 | MACD > 0 + rejim QQQ OFF |
| 417 | M120 Reversal New Highs (ditala 2) | 842 / 818 | +0.06 / -0.73 | -1.12 | MA50 > MA200 + volum hari isyarat >= 1.5x purata 50 | -1.60 | ATR% <= 2.5 + SPY > SMA200 |
| 418 | M41 FW Penyatuan Mingguan | 3,569 / 2,528 | -0.79 / +0.17 | -1.13 | MA20 > MA50 + templat trend Minervini | -1.05 | templat trend Minervini + rejim QQQ ON |
| 419 | M120 Reversal New Highs (ditala 1) | 984 / 865 | -0.24 / +0.21 | -1.14 | MA20 > MA50 + MACD > isyarat | -1.30 | MA50 naik (lawan 20 bar lalu) + SPY > SMA200 |
| 420 | M32 Momentum Burst (ditala 2) | 356 / 235 | +1.10 / +1.17 | -1.18 | MACD > isyarat + dalam 15% dari puncak 52 minggu | -1.13 | dalam 15% dari puncak 52 minggu + rejim QQQ ON |
| 421 | M41 FW Penyatuan Mingguan (ditala 1) | 2,805 / 2,108 | -0.75 / +0.20 | -1.23 | templat trend Minervini + RS >= 70 | -1.31 | MACD > isyarat + SPY > SMA200 |
| 422 | M05 MACD Divergence + Pengesahan | 2,542 / 1,720 | -0.70 / -0.03 | -1.24 | tutup > MA50 + ADX < 20 | -0.96 | ADX < 20 + rejim QQQ ON |
| 423 | M74 Lulus Baharu Trend Template Minervini (ditala 2) | 3,729 / 2,817 | -0.32 / -0.79 | -1.25 | RSI14 > 60 + Supertrend naik | -1.03 | Supertrend naik + rejim QQQ ON |
| 424 | M44 Tapak Rata IBD (ditala 2) | 772 / 582 | -0.82 / +1.40 | -1.26 | dalam 15% dari puncak 52 minggu + ATR% <= 2.5 | -1.27 | ATR% <= 2.5 + SPY > SMA200 |
| 425 | M118 Expansion Pivot (Cooper) (ditala 2) | 3,160 / 2,471 | -0.29 / -0.49 | -1.26 | MA50 > MA200 + hari naik (tutup > buka) | -1.03 | tutup > MA200 + rejim QQQ ON |
| 426 | M107 Golden Cross SMA50/200 (ditala 1) | 2,850 / 2,064 | -0.33 / -0.74 | -1.27 | dalam 15% dari puncak 52 minggu + hari naik (tutup > buka) | -1.45 | dalam 15% dari puncak 52 minggu + SPY > SMA200 |
| 427 | M44 Tapak Rata IBD | 1,153 / 966 | -0.58 / +1.55 | -1.29 | MA50 naik (lawan 20 bar lalu) + ADX < 20 | -1.50 | ADX < 20 + SPY > SMA200 |
| 428 | M115 Bow Tie (Landry) | 1,350 / 978 | -0.05 / -0.31 | -1.31 | tutup > MA200 + tutup dalam 25% teratas julat hari | -1.43 | SPY > SMA200 |
| 429 | M141 First Thrust (Landry) | 1,277 / 778 | +0.15 / -0.39 | -1.32 | ADX < 20 | -1.50 | SPY > SMA200 + tutup dalam 25% teratas julat hari |
| 430 | M135 3rd Watch | 2,060 / 1,048 | +0.14 / -0.77 | -1.38 | MA50 naik (lawan 20 bar lalu) + dalam 5% dari puncak 52 minggu | -1.54 | MA20 > MA50 + rejim QQQ ON |
| 431 | M37 Weinstein Peringkat 2 (ditala 1) | 3,695 / 2,185 | -0.45 / -0.98 | -1.40 | templat trend Minervini + tutup dalam 25% teratas julat hari | -1.02 | RS >= 90 + SPY > SMA200 |
| 432 | M07 Qullamaggie Breakout (ditala 1) | 303 / 612 | +1.76 / +1.77 | -1.45 | tiada | -0.50 | MA50 naik (lawan 20 bar lalu) + rejim QQQ ON |
| 433 | M05 MACD Divergence + Pengesahan (ditala 1) | 2,330 / 1,490 | -0.71 / -0.43 | -1.46 | MACD > 0 + dalam 15% dari puncak 52 minggu | -1.19 | ADX < 20 + SPY > SMA200 |
| 434 | M142 Pecahan volum dari dasar (底部放量) (ditala 2) | 2,666 / 1,811 | -0.82 / -0.46 | -1.49 | RSI14 > 60 + RS >= 70 | -1.63 | RS >= 70 + SPY > SMA200 |
| 435 | M138 直升机空中加油 (Helikopter isi minyak di udara) (ditala 1) | 1,826 / 989 | -0.46 / -0.62 | -1.50 | tutup > MA200 + MA50 naik (lawan 20 bar lalu) | -1.35 | MA50 naik (lawan 20 bar lalu) + SPY > SMA200 |
| 436 | M130 多方炮 (dua lilin hijau mengapit satu merah) (ditala 1) | 1,048 / 648 | +0.50 / +0.30 | -1.53 | tutup > MA200 | -1.72 | SPY > SMA200 |
| 437 | M64 O'Neil Tiga Minggu Ketat (ditala 1) | 1,118 / 982 | -1.28 / -0.19 | -1.55 | Supertrend naik + ATR% <= 2.5 | -1.52 | ATR% <= 2.5 + SPY > SMA200 |
| 438 | M121 High 2 bull flag (Brooks) (ditala 2) | 1,719 / 708 | -0.42 / -0.77 | -1.56 | MACD > 0 + ATR% <= 2.5 | -1.62 | ATR% <= 2.5 + SPY > SMA200 |
| 439 | M130 多方炮 (dua lilin hijau mengapit satu merah) | 1,232 / 731 | -0.08 / -0.19 | -1.56 | ADX > 25 + ATR% <= 2.5 | -1.72 | tutup > MA50 + SPY > SMA200 |
| 440 | M121 High 2 bull flag (Brooks) | 2,426 / 1,014 | -0.15 / -0.79 | -1.60 | RS >= 70 + hari naik (tutup > buka) | -1.65 | ATR% <= 2.5 + rejim QQQ ON |
| 441 | M64 O'Neil Tiga Minggu Ketat | 1,017 / 898 | -1.15 / -0.09 | -1.64 | MA20 > MA50 + ATR% <= 2.5 | -1.64 | ATR% <= 2.5 + SPY > SMA200 |
| 442 | N203 | 2,126 / 2,703 | -1.69 / +0.41 | -1.64 | MA50 naik (lawan 20 bar lalu) + ADX < 20 | -1.56 | ADX < 20 + SPY > SMA200 |
| 443 | M121 High 2 bull flag (Brooks) (ditala 1) | 2,035 / 869 | -0.59 / -0.70 | -1.69 | ATR% <= 2.5 + squeeze hidup | -1.76 | ATR% <= 2.5 + SPY > SMA200 |
| 444 | P31 episodic pivot | 787 / 844 | +0.37 / +0.48 | -1.70 | tutup > MA20 + RSI14 > 50 | -1.32 | ATR% >= 4 + SPY > SMA200 |
| 445 | N204 | 1,349 / 1,849 | -0.89 / +0.49 | -1.73 | tutup > MA20 + MA20 > MA50 | -1.91 | MA20 > MA50 + rejim QQQ ON |
| 446 | M87 IBD Tapak Menaik | 727 / 1,107 | -0.11 / -0.09 | -1.76 | tutup > MA20 + hari naik (tutup > buka) | -1.83 | SPY > SMA200 + hari naik (tutup > buka) |
| 447 | M24 Rotasi Momentum ROC12 + SMA200 (ditala 1) | 210 / 150 | +2.78 / +3.54 | -1.88 | tutup > MA200 + MA50 > MA200 | +0.01 | MA50 > MA200 + SPY > SMA200 |
| 448 | M138 直升机空中加油 (Helikopter isi minyak di udara) (ditala 2) | 1,254 / 666 | -0.82 / -1.13 | -1.95 | ADX > 25 + ATR% <= 2.5 | -1.87 | tutup > MA200 + SPY > SMA200 |
| 449 | M141 First Thrust (Landry) (ditala 1) | 1,355 / 845 | -0.07 / -1.04 | -1.96 | ADX < 20 + hari naik (tutup > buka) | -1.55 | ATR% <= 2.5 + rejim QQQ ON |
| 450 | M37 Weinstein Peringkat 2 | 1,942 / 1,121 | +0.04 / -1.94 | -2.02 | RS >= 70 + volum hari isyarat >= 1.5x purata 50 | -2.51 | volum hari isyarat >= 1.5x purata 50 + rejim QQQ ON |
| 451 | M140 猎豹出击 (Serangan Cheetah) (ditala 2) | 821 / 1,274 | -0.75 / +0.50 | -2.06 | MACD > 0 + tutup dalam 25% teratas julat hari | -1.45 | SPY > SMA200 + hari naik (tutup > buka) |
| 452 | P41 squeeze panjang lepas + volum | 1,023 / 671 | +0.29 / -0.28 | -2.17 | tutup > MA50 | -1.70 | SPY > SMA200 |
| 453 | P49 pecah tinggi hari gap | 2,413 / 3,047 | -1.32 / -1.54 | -2.18 | tutup > MA50 + hari naik (tutup > buka) | -2.10 | rejim QQQ ON + hari naik (tutup > buka) |
| 454 | M141 First Thrust (Landry) (ditala 2) | 826 / 464 | -0.60 / -2.01 | -2.36 | ATR% <= 2.5 | -3.23 | dalam 15% dari puncak 52 minggu + rejim QQQ ON |
| 455 | M143 장대양봉 이후 눌림목 / 5일선 매매 (Undur ke MA5 selepas lilin naik panjang) (ditala 1) | 1,804 / 1,181 | -0.69 / -1.47 | -2.50 | tutup > MA50 + hari naik (tutup > buka) | -2.42 | SPY > SMA200 + hari naik (tutup > buka) |
| 456 | M143 장대양봉 이후 눌림목 / 5일선 매매 (Undur ke MA5 selepas lilin naik panjang) | 1,947 / 1,105 | -1.46 / -1.14 | -2.51 | RSI14 > 50 + Supertrend naik | -2.31 | Supertrend naik + SPY > SMA200 |
| 457 | M138 直升机空中加油 (Helikopter isi minyak di udara) | 620 / 286 | -0.84 / -0.48 | -2.71 | MA50 naik (lawan 20 bar lalu) + MACD > isyarat | -2.45 | MACD > isyarat + SPY > SMA200 |
| 458 | M64 O'Neil Tiga Minggu Ketat (ditala 2) | 383 / 453 | -0.05 / -0.73 | -2.83 | MA20 > MA50 + MACD > 0 | -2.92 | tutup > MA200 + SPY > SMA200 |
| 459 | M104 High Tight Flag / Power Play (ditala 2) | 246 / 243 | +0.70 / +0.01 | -3.28 | templat trend Minervini + MACD > 0 | -2.43 | SPY > SMA200 |
| 460 | M144 Screw Bar (ditala 2) | 222 / 486 | +0.16 / +0.46 | -3.42 | RSI14 > 50 + hari naik (tutup > buka) | -5.48 | SPY > SMA200 |
| 461 | M104 High Tight Flag / Power Play | 189 / 252 | +4.08 / -1.16 | -3.58 | RS >= 70 + tutup dalam 25% teratas julat hari | -4.54 | RS >= 70 + rejim QQQ ON |
| 462 | M143 장대양봉 이후 눌림목 / 5일선 매매 (Undur ke MA5 selepas lilin naik panjang) (ditala 2) | 683 / 305 | -2.23 / -1.92 | -3.71 | tutup > MA200 + MACD > 0 | -3.72 | tutup > MA200 + SPY > SMA200 |
| 463 | M37 Weinstein Peringkat 2 (ditala 2) | 450 / 281 | +0.86 / -2.11 | -3.75 | templat trend Minervini + RS >= 90 | -3.75 | RS >= 90 + SPY > SMA200 |
| 464 | M144 Screw Bar | 144 / 363 | +1.84 / +0.54 | -4.03 | hari naik (tutup > buka) | – | – |
| 465 | M104 High Tight Flag / Power Play (ditala 1) | 164 / 184 | +3.63 / -2.32 | -5.25 | MA20 > MA50 + MA50 naik (lawan 20 bar lalu) | -4.37 | MA20 > MA50 + SPY > SMA200 |

**Tidak cukup isyarat (35):** M08.1, M07.2, M08.2, M106.1, M115.2, M144.1, M157.1, M157.2, M22.1, M22.0, M22.2, M24.0, M24.2, M29.1, M29.2, M31.2, M35.1, M35.2, M40.0, M40.1, M40.2, M45.0, M45.1, M45.2, M56.0, M56.1, M56.2, M59.1, M59.2, M66.2, M76.2, M87.1, M87.2, M88.2, M91.2.

## Bacaan

- Skor terbaik syarat sahaja > 0: 258 daripada 465 pencetus. Dengan prasyarat pasaran > 0: 221.
- Daripada 182,903 peraturan masuk, 4.2% berskor > 0 (syarat sahaja 4.2%; dengan prasyarat pasaran 4.4%).
- "Skor terbaik" ialah yang terbaik daripada sehingga 466 gabungan penapis bagi setiap pencetus, jadi ia terpilih dan condong ke atas; lajur "tanpa penapis" tidak terpilih.
