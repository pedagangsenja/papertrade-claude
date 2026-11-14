# Analisis prestasi sebenar Papertrade C lawan jangkaan backtest

Dijana oleh `WFO/kod/analisis_sebenar.py`. Sumber: semua `papertrade/claude*.csv` (22565 posisi sah; 9006 tutup, 13559 terbuka; 2026-10-08 hingga 2026-11-13). Jangkaan = registry set 431 bagi varian modul (dalam sampel bagi M115–M161).

Ujian hanya atas posisi MATANG (dibeli >= 1.5 x hari pegang jangkaan dan >= 14 hari lalu; tutup = untung akhir, terbuka = untung semasa) untuk elak bias pemilihan (yang tutup awal kebanyakannya kena henti). Ambang: >= 10 posisi matang. AMARAN = kadar menang (z) atau purata (t) < −2 berbanding jangkaan.

**Ringkasan:** 5 AMARAN, 24 SELARI, 199 data belum cukup.

| Kaedah | Status | n | Matang | Menang matang | Menang jangka | Purata matang % | Purata jangka % | Hari jangka | Tutup (awal) | Purata tutup % | Terbuka purata % | z | t |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| M123 CCI Correction (Lambert, ChartSchool) | AMARAN | 148 | 47 | 21% | 28% | -1.43 | 0.92 | 10 | 121 | -1.95 | 2.12 | -1.0 | -5.5 |
| M08 SMA20 + SMA200 | AMARAN | 179 | 42 | 17% | 32% | -2.99 | 1.07 | 12 | 106 | -3.88 | 3.47 | -2.1 | -6.8 |
| M28 VWAP Separator + Kiss Pivot | AMARAN | 92 | 47 | 21% | 43% | -2.25 | 0.22 | 5 | 67 | -2.23 | 2.81 | -3.0 | -2.4 |
| M128 Inventory Retracement Bar (IRB, Rob Hoffman) | AMARAN | 121 | 10 | 10% | 34% | -5.78 | 0.55 | 12 | 63 | -4.90 | 2.92 | -1.6 | -2.4 |
| M76 Undercut & Rally pada Low Penting | AMARAN | 79 | 26 | 19% | 37% | -1.78 | 0.67 | 9 | 51 | -3.15 | 2.67 | -1.9 | -2.8 |
| M102 Stockbee SLTB | DATA BELUM CUKUP | 231 | 9 | 11% | 18% | 0.79 | 1.34 | 16 | 161 | -3.65 | 4.39 |  |  |
| M49 Ichimoku (Tutup Atas Awan + Tenkan Silang Kijun) | DATA BELUM CUKUP | 219 | 0 |  | 23% |  | 3.99 | 34 | 126 | -5.10 | 3.36 |  |  |
| M66 IBD Undur Pertama ke Purata 50 Hari | DATA BELUM CUKUP | 199 | 0 |  | 28% |  | 1.71 | 19 | 113 | -4.48 | 3.19 |  |  |
| M12 Parabolic SAR | DATA BELUM CUKUP | 224 | 0 |  | 29% |  | 2.04 | 23 | 112 | -6.18 | 3.31 |  |  |
| M36 Turtle 55/20 | DATA BELUM CUKUP | 230 | 0 |  | 32% |  | 2.65 | 30 | 112 | -7.28 | 4.15 |  |  |
| M55 Guppy GMMA | DATA BELUM CUKUP | 193 | 0 |  | 26% |  | 2.71 | 28 | 110 | -5.85 | 4.41 |  |  |
| M81 Bensdorp Long Trend High Momentum | DATA BELUM CUKUP | 175 | 0 |  | 32% |  | 8.56 | 105 | 105 | -12.73 | 2.69 |  |  |
| M99 Three Line Break | DATA BELUM CUKUP | 163 | 5 | 80% | 40% | 10.61 | 1.17 | 16 | 101 | -4.91 | 5.08 |  |  |
| M57 Landry Trend Knockout (TKO) | DATA BELUM CUKUP | 152 | 0 |  | 21% |  | 1.55 | 18 | 100 | -4.97 | 3.75 |  |  |
| M54 IBD Power Trend | DATA BELUM CUKUP | 180 | 0 |  | 30% |  | 3.37 | 37 | 92 | -6.73 | 3.97 |  |  |
| M89 Chande 65sma-3cc | DATA BELUM CUKUP | 189 | 0 |  | 34% |  | 1.83 | 26 | 91 | -6.27 | 4.34 |  |  |
| M111 Sistem Volatiliti Wilder | DATA BELUM CUKUP | 218 | 0 |  | 39% |  | 2.39 | 30 | 88 | -8.04 | 3.65 |  |  |
| M161 EMA 10/21 + Supertrend (10,3) | DATA BELUM CUKUP | 201 | 0 |  | 35% |  | 1.43 | 18 | 85 | -8.26 | 2.91 |  |  |
| M124 'Last' Stochastic Technique (ChartSchool) | DATA BELUM CUKUP | 201 | 0 |  | 36% |  | 1.74 | 20 | 84 | -6.23 | 3.21 |  |  |
| M105 Supertrend tulen | DATA BELUM CUKUP | 237 | 0 |  | 39% |  | 2.44 | 32 | 83 | -7.70 | 3.88 |  |  |
| M11 NR7 Breakout + Volume | DATA BELUM CUKUP | 114 | 0 |  | 36% |  | 2.86 | 20 | 78 | -2.62 | 3.81 |  |  |
| M95 Nisbah Kebaharuan High 52 Minggu (Bhootra & Hur) | DATA BELUM CUKUP | 132 | 0 |  | 32% |  | 2.68 | 29 | 74 | -6.61 | 3.35 |  |  |
| M125 2-Bar Breakout | DATA BELUM CUKUP | 201 | 0 |  | 30% |  | 166.86 | 443 | 71 | -9.91 | 1.45 |  |  |
| M10 EMA3 + CCI + MACD | DATA BELUM CUKUP | 151 | 0 |  | 33% |  | 4.70 | 54 | 70 | -7.65 | 5.69 |  |  |
| M136 Short/Intermediate-term Low (Larry Williams) | DATA BELUM CUKUP | 190 | 0 |  | 24% |  | 112.90 | 343 | 70 | -9.33 | 2.09 |  |  |
| M155 Market Cycle Strategy | DATA BELUM CUKUP | 206 | 0 |  | 49% |  | 1.56 | 17 | 69 | -10.61 | 2.67 |  |  |
| M93 Bollinger Kaedah II: %b + MFI | DATA BELUM CUKUP | 228 | 0 |  | 36% |  | 8.20 | 62 | 69 | -10.31 | 4.79 |  |  |
| M80 Radge Saluran Purata Bergerak (MAC) | DATA BELUM CUKUP | 239 | 0 |  | 36% |  | 8.91 | 66 | 67 | -10.89 | 3.66 |  |  |
| M90 Pring KST | DATA BELUM CUKUP | 114 | 0 |  | 30% |  | 1.95 | 26 | 67 | -7.28 | 3.49 |  |  |
| M74 Lulus Baharu Trend Template Minervini | DATA BELUM CUKUP | 110 | 0 |  | 24% |  | 2.72 | 20 | 66 | -3.34 | 4.86 |  |  |
| M82 Arthur Hill Rotasi Sasaran 10% | DATA BELUM CUKUP | 273 | 0 |  | 61% |  | 1.84 | 38 | 65 | 5.98 | -3.40 |  |  |
| M31 Band Walk (BB 20/2) | DATA BELUM CUKUP | 221 | 0 |  | 43% |  | 3.30 | 32 | 60 | -13.27 | 2.28 |  |  |
| N74X16  | DATA BELUM CUKUP | 100 | 0 |  |  |  |  |  | 60 | -2.49 | 1.01 |  |  |
| M34 Carter TTM Squeeze | DATA BELUM CUKUP | 122 | 0 |  | 34% |  | 2.38 | 30 | 57 | -8.03 | 6.94 |  |  |
| M127 Slingshot Bullish | DATA BELUM CUKUP | 82 | 0 |  | 19% |  | 2.60 | 16 | 56 | -3.07 | 2.97 |  |  |
| M119 180 Bullish (Cooper) | DATA BELUM CUKUP | 114 | 0 |  | 27% |  | 1.17 | 18 | 55 | -6.05 | 2.85 |  |  |
| M122 Moving Momentum (ChartSchool) | DATA BELUM CUKUP | 105 | 0 |  | 35% |  | 1.79 | 24 | 55 | -8.40 | 2.94 |  |  |
| M131 Ross Hook (Joe Ross) | DATA BELUM CUKUP | 144 | 0 |  | 30% |  | 2.35 | 30 | 55 | -6.59 | 3.02 |  |  |
| N28X36  | DATA BELUM CUKUP | 110 | 0 |  |  |  |  |  | 55 | -3.91 | -0.14 |  |  |
| N08X16  | DATA BELUM CUKUP | 115 | 0 |  |  |  |  |  | 54 | -3.17 | -0.63 |  |  |
| N08X36  | DATA BELUM CUKUP | 115 | 0 |  |  |  |  |  | 54 | -5.17 | 0.57 |  |  |
| N28X16  | DATA BELUM CUKUP | 109 | 0 |  |  |  |  |  | 54 | -2.80 | 0.08 |  |  |
| M158 Doubly Adaptive Profit Targets | DATA BELUM CUKUP | 188 | 0 |  | 34% |  | 2.94 | 30 | 51 | -8.79 | 2.37 |  |  |
| M50 Elder Triple Screen | DATA BELUM CUKUP | 68 | 0 |  | 23% |  | 1.80 | 18 | 51 | -5.11 | 4.04 |  |  |
| M137 Livermore System | DATA BELUM CUKUP | 143 | 0 |  | 35% |  | 4.22 | 37 | 50 | -7.27 | 2.81 |  |  |
| M79 Radge: 20% Flipper | DATA BELUM CUKUP | 188 | 0 |  | 40% |  | 6.25 | 60 | 50 | -12.65 | 1.70 |  |  |
| N113X36  | DATA BELUM CUKUP | 96 | 0 |  |  |  |  |  | 50 | -1.53 | -0.86 |  |  |
| M26 Garis Trend Undur 3 Sentuhan + Pecahan | DATA BELUM CUKUP | 76 | 0 |  | 50% |  | 5.17 | 39 | 49 | -1.67 | 0.42 |  |  |
| N76X16  | DATA BELUM CUKUP | 100 | 0 |  |  |  |  |  | 49 | -3.27 | 0.31 |  |  |
| N27X16  | DATA BELUM CUKUP | 100 | 0 |  |  |  |  |  | 48 | -3.30 | -0.19 |  |  |
| N48X36  | DATA BELUM CUKUP | 85 | 0 |  |  |  |  |  | 48 | -0.60 | 1.09 |  |  |
| M151 Outside Bar Failure | DATA BELUM CUKUP | 101 | 0 |  | 27% |  | 1.93 | 26 | 47 | -3.27 | 3.10 |  |  |
| N113X16  | DATA BELUM CUKUP | 96 | 0 |  |  |  |  |  | 47 | -0.57 | -1.49 |  |  |
| N41X36  | DATA BELUM CUKUP | 113 | 0 |  |  |  |  |  | 47 | -4.89 | 0.17 |  |  |
| M39 Radge Pecahan Bollinger 100 hari | DATA BELUM CUKUP | 195 | 0 |  | 37% |  | 9.11 | 96 | 46 | -16.35 | 2.44 |  |  |
| N41X16  | DATA BELUM CUKUP | 113 | 0 |  |  |  |  |  | 45 | -3.15 | -0.68 |  |  |
| M04 BB Squeeze Breakout | DATA BELUM CUKUP | 121 | 0 |  | 36% |  | 4.96 | 32 | 43 | -8.41 | 3.03 |  |  |
| M30 BB Free Bar + Himpitan 50/2.5 | DATA BELUM CUKUP | 140 | 0 |  | 37% |  | 3.80 | 34 | 42 | -8.34 | 2.49 |  |  |
| N42X36  | DATA BELUM CUKUP | 101 | 0 |  |  |  |  |  | 42 | -0.68 | 0.39 |  |  |
| M06 Minervini VCP Breakout | DATA BELUM CUKUP | 83 | 0 |  | 33% |  | 2.49 | 29 | 40 | -6.96 | 3.77 |  |  |
| M100 Bulkowski Segi Empat & Segi Tiga Menaik | DATA BELUM CUKUP | 64 | 0 |  | 46% |  | 1.32 | 29 | 40 | 0.60 | -0.68 |  |  |
| M149 3-Step Pullback | DATA BELUM CUKUP | 116 | 0 |  | 19% |  | 59.37 | 273 | 39 | -7.20 | 3.05 |  |  |
| N42X16  | DATA BELUM CUKUP | 101 | 0 |  |  |  |  |  | 39 | -0.75 | -0.13 |  |  |
| M145 Yum-Yum Continuation | DATA BELUM CUKUP | 200 | 0 |  | 25% |  | 80.48 | 356 | 38 | -12.89 | 1.30 |  |  |
| M77 Undercut & Rally pada Purata Bergerak (MAU&R) | DATA BELUM CUKUP | 60 | 3 | 0% | 25% | -1.43 | 2.69 | 15 | 37 | -3.73 | 5.38 |  |  |
| N56X36  | DATA BELUM CUKUP | 113 | 0 |  |  |  |  |  | 36 | -5.62 | -0.07 |  |  |
| M132 Ascending Scallop (Bulkowski) | DATA BELUM CUKUP | 87 | 0 |  | 42% |  | 0.98 | 29 | 35 | -9.92 | 2.93 |  |  |
| M150 Trend Bar Failure (Brooks) | DATA BELUM CUKUP | 82 | 5 | 40% | 37% | 0.62 | 0.54 | 13 | 35 | -4.51 | 3.00 |  |  |
| M32 Momentum Burst | DATA BELUM CUKUP | 58 | 0 |  | 25% |  | 3.57 | 22 | 35 | -6.47 | 6.31 |  |  |
| N27X36  | DATA BELUM CUKUP | 100 | 0 |  |  |  |  |  | 35 | -5.71 | -0.38 |  |  |
| N36X36  | DATA BELUM CUKUP | 100 | 0 |  |  |  |  |  | 35 | -5.37 | -0.72 |  |  |
| M33 Supertrend + SMA10 | DATA BELUM CUKUP | 156 | 0 |  | 40% |  | 1.65 | 33 | 33 | -10.03 | 2.52 |  |  |
| N36X16  | DATA BELUM CUKUP | 100 | 0 |  |  |  |  |  | 32 | -4.04 | -1.19 |  |  |
| N56X16  | DATA BELUM CUKUP | 112 | 0 |  |  |  |  |  | 32 | -3.67 | -0.50 |  |  |
| N76X36  | DATA BELUM CUKUP | 100 | 0 |  |  |  |  |  | 32 | -8.38 | 0.92 |  |  |
| M29 EMA3 + RSI75 + Stokastik | DATA BELUM CUKUP | 39 | 0 |  | 18% |  | 3.22 | 35 | 30 | -3.33 | 0.70 |  |  |
| M88 O'Neil Shakeout +3 | DATA BELUM CUKUP | 71 | 0 |  | 32% |  | 5.56 | 32 | 30 | -8.20 | 5.04 |  |  |
| N24X36  | DATA BELUM CUKUP | 110 | 0 |  |  |  |  |  | 30 | -6.64 | -0.01 |  |  |
| N54X36  | DATA BELUM CUKUP | 106 | 0 |  |  |  |  |  | 30 | -8.42 | -0.34 |  |  |
| M146 3-Bar Momentum Pattern | DATA BELUM CUKUP | 70 | 0 |  | 27% |  | 2.66 | 26 | 29 | -5.61 | 5.40 |  |  |
| M154 HOLP (High of Low Period) | DATA BELUM CUKUP | 82 | 0 |  | 39% |  | 1.93 | 27 | 29 | -11.78 | 3.02 |  |  |
| M101 Bulkowski: Tiga lembah menaik | DATA BELUM CUKUP | 52 | 0 |  | 35% |  | 3.46 | 33 | 28 | -9.87 | 2.80 |  |  |
| N29X36  | DATA BELUM CUKUP | 109 | 0 |  |  |  |  |  | 28 | -8.77 | -0.12 |  |  |
| N29X16  | DATA BELUM CUKUP | 110 | 0 |  |  |  |  |  | 27 | -5.58 | -0.75 |  |  |
| N45X16  | DATA BELUM CUKUP | 101 | 0 |  |  |  |  |  | 27 | -4.73 | 0.20 |  |  |
| M147 Improved Three-Bar Pullback | DATA BELUM CUKUP | 75 | 0 |  | 31% |  | 91.01 | 442 | 26 | -14.33 | 1.69 |  |  |
| N09X36  | DATA BELUM CUKUP | 94 | 0 |  |  |  |  |  | 26 | -5.19 | 0.77 |  |  |
| M01 Bollinger Band + RSI | DATA BELUM CUKUP | 102 | 0 |  | 67% |  | 2.22 | 22 | 25 | 10.72 | -0.99 |  |  |
| N24X16  | DATA BELUM CUKUP | 110 | 0 |  |  |  |  |  | 24 | -5.84 | -0.16 |  |  |
| N25X36  | DATA BELUM CUKUP | 103 | 0 |  |  |  |  |  | 24 | -10.45 | 0.20 |  |  |
| N42X17  | DATA BELUM CUKUP | 100 | 0 |  |  |  |  |  | 24 | -0.23 | 1.35 |  |  |
| N53X36  | DATA BELUM CUKUP | 108 | 0 |  |  |  |  |  | 24 | -8.44 | -0.37 |  |  |
| N40X16  | DATA BELUM CUKUP | 87 | 0 |  |  |  |  |  | 23 | -3.15 | 0.75 |  |  |
| M115 Bow Tie (Landry) | DATA BELUM CUKUP | 35 | 0 |  | 27% |  | 1.06 | 18 | 22 | -5.22 | 4.14 |  |  |
| M118 Expansion Pivot (Cooper) | DATA BELUM CUKUP | 85 | 0 |  | 33% |  | 1.56 | 27 | 22 | -6.18 | 2.60 |  |  |
| N07X16  | DATA BELUM CUKUP | 100 | 0 |  |  |  |  |  | 22 | -9.39 | -0.83 |  |  |
| M78 Alvarez Pecahan Mingguan DTAYS | DATA BELUM CUKUP | 33 | 0 |  | 32% |  | 3.17 | 40 | 21 | -9.28 | 3.03 |  |  |
| N33X36  | DATA BELUM CUKUP | 99 | 0 |  |  |  |  |  | 21 | -8.16 | -0.19 |  |  |
| N38X36  | DATA BELUM CUKUP | 62 | 0 |  |  |  |  |  | 21 | -7.66 | 0.75 |  |  |
| N43X36  | DATA BELUM CUKUP | 96 | 0 |  |  |  |  |  | 21 | -8.83 | 0.97 |  |  |
| N45X36  | DATA BELUM CUKUP | 101 | 0 |  |  |  |  |  | 21 | -7.27 | -0.29 |  |  |
| N47X16  | DATA BELUM CUKUP | 90 | 0 |  |  |  |  |  | 21 | -6.22 | -0.18 |  |  |
| N53X16  | DATA BELUM CUKUP | 108 | 0 |  |  |  |  |  | 21 | -6.48 | -0.51 |  |  |
| N54X16  | DATA BELUM CUKUP | 106 | 0 |  |  |  |  |  | 21 | -7.54 | -0.78 |  |  |
| M59 Anjakan Julat RSI | DATA BELUM CUKUP | 38 | 0 |  | 34% |  | 3.10 | 37 | 20 | -12.21 | 3.19 |  |  |
| N22X36  | DATA BELUM CUKUP | 102 | 0 |  |  |  |  |  | 20 | -7.30 | -0.30 |  |  |
| M67 Rayner Teo: Ujian Ketiga pada Purata 50 | DATA BELUM CUKUP | 30 | 0 |  | 30% |  | 1.90 | 24 | 19 | -7.24 | 4.51 |  |  |
| M91 Stochastic Pop (Bernstein/Steckler) | DATA BELUM CUKUP | 41 | 0 |  | 42% |  | 1.63 | 18 | 19 | -5.66 | 2.94 |  |  |
| N07X36  | DATA BELUM CUKUP | 100 | 0 |  |  |  |  |  | 19 | -11.20 | -0.78 |  |  |
| N25X16  | DATA BELUM CUKUP | 103 | 0 |  |  |  |  |  | 19 | -9.11 | -0.11 |  |  |
| M09 Volumatic VIDYA Pivot Retest | DATA BELUM CUKUP | 33 | 0 |  | 23% |  | 1.85 | 30 | 17 | -8.10 | 0.29 |  |  |
| M139 均线首次粘合向上发散 (MA berhimpun kali pertama, berkipas naik) | DATA BELUM CUKUP | 83 | 0 |  | 51% |  | 1.31 | 19 | 17 | -15.72 | 2.44 |  |  |
| M46 Jurang Naik Boleh Beli (Buyable Gap Up) | DATA BELUM CUKUP | 33 | 0 |  | 23% |  | 2.81 | 22 | 17 | -3.36 | 3.27 |  |  |
| N22X16  | DATA BELUM CUKUP | 102 | 0 |  |  |  |  |  | 17 | -5.53 | -1.01 |  |  |
| N33X16  | DATA BELUM CUKUP | 100 | 0 |  |  |  |  |  | 17 | -8.32 | -0.53 |  |  |
| N47X36  | DATA BELUM CUKUP | 90 | 0 |  |  |  |  |  | 17 | -8.21 | -0.55 |  |  |
| M134 First Kiss After Daylight (Landry) | DATA BELUM CUKUP | 52 | 0 |  | 34% |  | 5.41 | 35 | 16 | -7.33 | 2.02 |  |  |
| N40X36  | DATA BELUM CUKUP | 84 | 0 |  |  |  |  |  | 16 | -10.73 | 1.81 |  |  |
| N68X36  | DATA BELUM CUKUP | 73 | 0 |  |  |  |  |  | 16 | -5.92 | 0.50 |  |  |
| M48 Cooper 1-2-3-4 | DATA BELUM CUKUP | 57 | 0 |  | 34% |  | 2.79 | 30 | 15 | -10.50 | 4.69 |  |  |
| M05 MACD Divergence + Pengesahan | DATA BELUM CUKUP | 44 | 0 |  | 35% |  | 10.85 | 108 | 14 | -9.43 | 3.26 |  |  |
| N42X14  | DATA BELUM CUKUP | 101 | 0 |  |  |  |  |  | 14 | 4.93 | 0.22 |  |  |
| M117 Landry Pullback (high 2 bulan) | DATA BELUM CUKUP | 93 | 0 |  | 21% |  | 45.52 | 287 | 13 | -9.46 | 3.25 |  |  |
| N31X36  | DATA BELUM CUKUP | 90 | 0 |  |  |  |  |  | 13 | -12.33 | -0.16 |  |  |
| N37X17  | DATA BELUM CUKUP | 58 | 0 |  |  |  |  |  | 13 | 1.04 | 1.21 |  |  |
| N68X16  | DATA BELUM CUKUP | 72 | 0 |  |  |  |  |  | 13 | -3.79 | -0.46 |  |  |
| M120 Reversal New Highs | DATA BELUM CUKUP | 19 | 0 |  | 27% |  | 1.15 | 28 | 12 | -6.32 | 7.83 |  |  |
| M68 Kell Base n' Break | DATA BELUM CUKUP | 40 | 0 |  | 36% |  | 1.35 | 35 | 12 | -8.69 | 0.83 |  |  |
| N124X36  | DATA BELUM CUKUP | 43 | 0 |  |  |  |  |  | 12 | -2.26 | 1.63 |  |  |
| N35X36  | DATA BELUM CUKUP | 82 | 0 |  |  |  |  |  | 12 | -11.19 | 0.46 |  |  |
| N36X14  | DATA BELUM CUKUP | 100 | 0 |  |  |  |  |  | 12 | 0.10 | -2.59 |  |  |
| M126 Hidden Smash Day (beli, Larry Williams) | DATA BELUM CUKUP | 18 | 0 |  | 35% |  | 5.15 | 33 | 11 | -7.73 | 1.51 |  |  |
| M140 猎豹出击 (Serangan Cheetah) | DATA BELUM CUKUP | 38 | 0 |  | 36% |  | 5.31 | 25 | 11 | -9.82 | 1.84 |  |  |
| N80X36  | DATA BELUM CUKUP | 77 | 0 |  |  |  |  |  | 11 | -11.11 | 0.56 |  |  |
| M129 Wick Play | DATA BELUM CUKUP | 26 | 0 |  | 38% |  | 2.60 | 38 | 10 | -13.31 | 7.25 |  |  |
| N37X16  | DATA BELUM CUKUP | 58 | 0 |  |  |  |  |  | 10 | -1.41 | 1.49 |  |  |
| N37X36  | DATA BELUM CUKUP | 58 | 0 |  |  |  |  |  | 10 | 0.14 | 1.43 |  |  |
| M141 First Thrust (Landry) | DATA BELUM CUKUP | 27 | 0 |  | 39% |  | 4.05 | 37 | 9 | -7.83 | 1.20 |  |  |
| N51X36  | DATA BELUM CUKUP | 18 | 0 |  |  |  |  |  | 9 | -7.39 | 0.56 |  |  |
| N75X17  | DATA BELUM CUKUP | 99 | 0 |  |  |  |  |  | 9 | 1.05 | 1.37 |  |  |
| M152 Spike & Ledge | DATA BELUM CUKUP | 47 | 0 |  | 52% |  | 3.20 | 36 | 8 | -15.88 | 1.46 |  |  |
| N28X14  | DATA BELUM CUKUP | 110 | 0 |  |  |  |  |  | 8 | 0.90 | -2.38 |  |  |
| N51X16  | DATA BELUM CUKUP | 17 | 0 |  |  |  |  |  | 8 | -9.26 | 0.01 |  |  |
| N56X17  | DATA BELUM CUKUP | 112 | 0 |  |  |  |  |  | 8 | -0.95 | -1.33 |  |  |
| N64X17  | DATA BELUM CUKUP | 45 | 0 |  |  |  |  |  | 8 | 2.31 | 1.79 |  |  |
| M107 Golden Cross SMA50/200 | DATA BELUM CUKUP | 40 | 0 |  | 32% |  | 15.43 | 110 | 7 | -10.47 | 1.18 |  |  |
| M144 Screw Bar | DATA BELUM CUKUP | 9 | 0 |  | 41% |  | 7.68 | 23 | 7 | -3.56 | 4.19 |  |  |
| M52 Radge Weekend Trend Trader | DATA BELUM CUKUP | 9 | 0 |  | 37% |  | 5.19 | 37 | 7 | -16.13 | 0.48 |  |  |
| M84 Jarak purata bergerak MAD 21/200 | DATA BELUM CUKUP | 10 | 0 |  | 37% |  | 3.71 | 26 | 7 | -7.69 | 3.01 |  |  |
| M87 IBD Tapak Menaik | DATA BELUM CUKUP | 12 | 0 |  | 32% |  | 3.49 | 30 | 7 | -10.03 | 5.99 |  |  |
| N24X17  | DATA BELUM CUKUP | 109 | 0 |  |  |  |  |  | 7 | -2.10 | -1.47 |  |  |
| N39X36  | DATA BELUM CUKUP | 37 | 0 |  |  |  |  |  | 7 | -12.15 | -1.36 |  |  |
| M44 Tapak Rata IBD | DATA BELUM CUKUP | 12 | 0 |  | 30% |  | 0.39 | 28 | 6 | -7.61 | 2.11 |  |  |
| M96 Momo India: Ranking Sharpe 3/6/12 bulan | DATA BELUM CUKUP | 6 | 0 |  | 43% |  | 12.18 | 54 | 6 | -13.20 |  |  |  |
| N22X14  | DATA BELUM CUKUP | 102 | 0 |  |  |  |  |  | 6 | -4.31 | -1.60 |  |  |
| N33X14  | DATA BELUM CUKUP | 99 | 0 |  |  |  |  |  | 6 | -4.72 | -1.52 |  |  |
| N57X36  | DATA BELUM CUKUP | 79 | 0 |  |  |  |  |  | 6 | -9.73 | -1.35 |  |  |
| N64X36  | DATA BELUM CUKUP | 45 | 0 |  |  |  |  |  | 6 | 1.40 | 1.68 |  |  |
| N75X14  | DATA BELUM CUKUP | 99 | 0 |  |  |  |  |  | 6 | 14.24 | 0.62 |  |  |
| M142 Pecahan volum dari dasar (底部放量) | DATA BELUM CUKUP | 51 | 0 |  | 41% |  | 6.85 | 44 | 5 | -5.11 | 1.89 |  |  |
| M41 FW Penyatuan Mingguan | DATA BELUM CUKUP | 20 | 0 |  | 36% |  | 15.03 | 117 | 5 | -15.64 | 3.29 |  |  |
| N50X14  | DATA BELUM CUKUP | 23 | 0 |  |  |  |  |  | 5 | 3.71 | -2.38 |  |  |
| N57X16  | DATA BELUM CUKUP | 79 | 0 |  |  |  |  |  | 5 | -10.24 | -1.42 |  |  |
| N64X16  | DATA BELUM CUKUP | 45 | 0 |  |  |  |  |  | 5 | -0.65 | 1.80 |  |  |
| M121 High 2 bull flag (Brooks) | DATA BELUM CUKUP | 7 | 0 |  | 47% |  | 2.47 | 49 | 4 | -16.77 | 1.05 |  |  |
| M21 Marius 3 Persediaan (Pecahan+Jurang+Kesinambungan) | DATA BELUM CUKUP | 6 | 1 | 100% | 26% | 2.42 | 2.57 | 8 | 4 | -3.10 | 1.43 |  |  |
| N37X14  | DATA BELUM CUKUP | 58 | 0 |  |  |  |  |  | 4 | 8.23 | 0.05 |  |  |
| M130 多方炮 (dua lilin hijau mengapit satu merah) | DATA BELUM CUKUP | 10 | 0 |  | 25% |  | 92.22 | 261 | 3 | -18.49 | 2.13 |  |  |
| M135 3rd Watch | DATA BELUM CUKUP | 15 | 0 |  | 39% |  | 2.05 | 35 | 3 | -12.00 | -2.92 |  |  |
| M157 Consolidation Pivot Breakout (versi angka) | DATA BELUM CUKUP | 4 | 0 |  | 14% |  | 32.05 | 179 | 3 | -8.78 | 7.28 |  |  |
| N06X36  | DATA BELUM CUKUP | 22 | 0 |  |  |  |  |  | 3 | -5.31 | -1.52 |  |  |
| N50X17  | DATA BELUM CUKUP | 23 | 0 |  |  |  |  |  | 3 | -2.07 | -1.46 |  |  |
| N66X36  | DATA BELUM CUKUP | 49 | 0 |  |  |  |  |  | 3 | -12.82 | -0.31 |  |  |
| M07 Qullamaggie Breakout | DATA BELUM CUKUP | 2 | 2 | 0% | 20% | -3.04 | 1.05 | 8 | 2 | -3.04 |  |  |  |
| M45 High 52 Minggu (George & Hwang) | DATA BELUM CUKUP | 8 | 0 |  | 32% |  | 12.81 | 61 | 2 | -9.78 | 2.84 |  |  |
| N119X13  | DATA BELUM CUKUP | 100 | 0 |  |  |  |  |  | 2 | 6.14 | -0.69 |  |  |
| N25X17  | DATA BELUM CUKUP | 103 | 0 |  |  |  |  |  | 2 | -4.49 | -2.03 |  |  |
| N64X14  | DATA BELUM CUKUP | 45 | 0 |  |  |  |  |  | 2 | 14.87 | 0.81 |  |  |
| M143 장대양봉 이후 눌림목 / 5일선 매매 (Undur ke MA5 selepas lilin naik panjang) | DATA BELUM CUKUP | 24 | 0 |  | 52% |  | 0.83 | 18 | 1 | -16.18 | -1.17 |  |  |
| M38 Darvas Kotak | DATA BELUM CUKUP | 23 | 0 |  | 49% |  | 18.79 | 210 | 1 | -9.28 | -1.93 |  |  |
| N19X13  | DATA BELUM CUKUP | 77 | 0 |  |  |  |  |  | 1 | 52.25 | 2.29 |  |  |
| N65X14  | DATA BELUM CUKUP | 28 | 0 |  |  |  |  |  | 1 | -4.93 | 0.31 |  |  |
| M104 High Tight Flag / Power Play | DATA BELUM CUKUP | 1 | 0 |  | 35% |  | 5.62 | 33 | 0 |  | 20.74 |  |  |
| M138 直升机空中加油 (Helikopter isi minyak di udara) | DATA BELUM CUKUP | 3 | 0 |  | 45% |  | 4.60 | 46 | 0 |  | -2.76 |  |  |
| M37 Weinstein Peringkat 2 | DATA BELUM CUKUP | 7 | 0 |  | 41% |  | 5.49 | 42 | 0 |  | 0.32 |  |  |
| M51 O'Neil Cawan & Pemegang | DATA BELUM CUKUP | 3 | 0 |  | 39% |  | 3.12 | 35 | 0 |  | -1.27 |  |  |
| M64 O'Neil Tiga Minggu Ketat | DATA BELUM CUKUP | 3 | 0 |  | 34% |  | 1.68 | 31 | 0 |  | 8.27 |  |  |
| M94 Pecutan Momentum (Chen, Yu & Wang) | DATA BELUM CUKUP | 12 | 0 |  | 63% |  | 24.04 | 121 | 0 |  | -3.87 |  |  |
| N119X15  | DATA BELUM CUKUP | 100 | 0 |  |  |  |  |  | 0 |  | -0.59 |  |  |
| N124X15  | DATA BELUM CUKUP | 42 | 0 |  |  |  |  |  | 0 |  | 1.81 |  |  |
| N16X13  | DATA BELUM CUKUP | 99 | 0 |  |  |  |  |  | 0 |  | 0.18 |  |  |
| N16X15  | DATA BELUM CUKUP | 99 | 0 |  |  |  |  |  | 0 |  | 0.18 |  |  |
| N201X36  | DATA BELUM CUKUP | 17 | 0 |  |  |  |  |  | 0 |  | -0.88 |  |  |
| N202X36  | DATA BELUM CUKUP | 11 | 0 |  |  |  |  |  | 0 |  | -0.39 |  |  |
| N203X36  | DATA BELUM CUKUP | 10 | 0 |  |  |  |  |  | 0 |  | -0.97 |  |  |
| N204X36  | DATA BELUM CUKUP | 2 | 0 |  |  |  |  |  | 0 |  | 1.96 |  |  |
| N28X17  | DATA BELUM CUKUP | 110 | 0 |  |  |  |  |  | 0 |  | -2.16 |  |  |
| N42X15  | DATA BELUM CUKUP | 100 | 0 |  |  |  |  |  | 0 |  | 0.88 |  |  |
| N53X17  | DATA BELUM CUKUP | 108 | 0 |  |  |  |  |  | 0 |  | -1.94 |  |  |
| N55X13  | DATA BELUM CUKUP | 79 | 0 |  |  |  |  |  | 0 |  | -0.89 |  |  |
| N65X36  | DATA BELUM CUKUP | 28 | 0 |  |  |  |  |  | 0 |  | 0.13 |  |  |
| N73X13  | DATA BELUM CUKUP | 97 | 0 |  |  |  |  |  | 0 |  | 2.25 |  |  |
| N75X13  | DATA BELUM CUKUP | 99 | 0 |  |  |  |  |  | 0 |  | 1.47 |  |  |
| N75X15  | DATA BELUM CUKUP | 99 | 0 |  |  |  |  |  | 0 |  | 1.47 |  |  |
| M03 BB Break + Divergence RSI | SELARI | 252 | 126 | 67% | 56% | 0.63 | 0.58 | 8 | 206 | 0.51 | -0.72 | 2.4 | 0.1 |
| M73 ADX(5) > 40 + Julat Terkecil 6 Hari | SELARI | 245 | 152 | 64% | 63% | -0.51 | 0.18 | 5 | 205 | -0.20 | -2.97 | 0.1 | -1.5 |
| M14 Walking with the Whales | SELARI | 255 | 16 | 12% | 21% | -0.61 | 1.52 | 15 | 195 | -2.43 | 4.73 | -0.9 | -1.4 |
| M20 EMA10/15 Crossover + Sudut | SELARI | 226 | 142 | 39% | 39% | -0.08 | 0.22 | 7 | 177 | -0.32 | 0.78 | -0.1 | -0.5 |
| M92 CCI-50 | SELARI | 264 | 63 | 67% | 49% | 2.45 | 1.17 | 13 | 169 | -2.67 | 4.44 | 2.9 | 1.4 |
| M70 Pecahan Hari Dalam | SELARI | 213 | 75 | 23% | 11% | 1.58 | 0.84 | 10 | 162 | -1.87 | 6.51 | 3.0 | 0.6 |
| M18 EMA9/21 Pullback | SELARI | 220 | 122 | 26% | 26% | 0.37 | 0.40 | 7 | 156 | -1.94 | 4.57 | 0.1 | -0.0 |
| M35 Pocket Pivot Morales & Kacher | SELARI | 204 | 98 | 31% | 28% | 0.89 | 0.29 | 9 | 145 | -1.66 | 5.37 | 0.5 | 0.7 |
| M13 Garis Trend Action/Safety Line | SELARI | 245 | 70 | 33% | 34% | 1.27 | 0.97 | 11 | 144 | -3.17 | 4.14 | -0.3 | 0.3 |
| M19 Sneaky Pivot (proksi harian) | SELARI | 203 | 65 | 46% | 44% | 1.06 | 0.27 | 11 | 139 | -1.87 | 1.85 | 0.4 | 0.7 |
| M15 Break & Retest + Henti ATR | SELARI | 239 | 56 | 43% | 33% | 0.67 | 1.08 | 12 | 127 | -3.64 | 5.12 | 1.5 | -0.4 |
| M159 Heikin-Ashi Trend | SELARI | 208 | 108 | 35% | 40% | -1.17 | 0.17 | 6 | 126 | -1.71 | -0.09 | -1.1 | -1.8 |
| M116 2/20 EMA Breakout (Landry) | SELARI | 204 | 58 | 53% | 50% | 0.17 | 0.40 | 9 | 123 | -2.74 | 0.04 | 0.5 | -0.2 |
| M156 Single Penetration (DiNapoli) | SELARI | 166 | 51 | 41% | 52% | 0.15 | 0.69 | 9 | 111 | -2.59 | 0.78 | -1.5 | -0.4 |
| M153 Range Leader | SELARI | 136 | 86 | 44% | 43% | -0.84 | 0.18 | 6 | 105 | -1.47 | 1.17 | 0.2 | -1.4 |
| M148 Natural Number Method | SELARI | 156 | 43 | 35% | 35% | 0.08 | 0.50 | 10 | 101 | -4.38 | 2.85 | -0.0 | -0.3 |
| M02 MACD + SMA200 | SELARI | 147 | 22 | 41% | 44% | 0.32 | 0.66 | 14 | 94 | -1.92 | 0.72 | -0.3 | -0.2 |
| M25 VWAP Wave (proksi harian) | SELARI | 157 | 64 | 36% | 30% | 2.41 | 0.42 | 10 | 93 | -0.66 | 3.04 | 1.1 | 1.3 |
| M106 DMI Wilder | SELARI | 131 | 25 | 32% | 32% | -0.19 | 1.01 | 12 | 68 | -3.73 | 2.97 | -0.0 | -1.2 |
| M27 Price Action 4 Tiang | SELARI | 65 | 65 | 31% | 35% | -0.05 | 0.36 | 7 | 58 | -2.18 | 17.61 | -0.8 | -0.4 |
| M23 Breitstein Kapitulasi + Kesinambungan | SELARI | 95 | 18 | 17% | 22% | -0.28 | 0.55 | 10 | 54 | -2.24 | 3.25 | -0.6 | -0.5 |
| M160 Measured Move Up | SELARI | 90 | 27 | 30% | 32% | 0.65 | 0.44 | 8 | 40 | -2.52 | 0.84 | -0.3 | 0.1 |
| M47 Holy Grail Raschke | SELARI | 34 | 16 | 56% | 51% | -2.93 | 0.25 | 5 | 25 | -3.05 | 0.97 | 0.4 | -1.4 |
| M133 Bull Hook (Crabel) | SELARI | 52 | 11 | 55% | 41% | 5.93 | 0.68 | 10 | 24 | -1.94 | 4.00 | 0.9 | 1.4 |

Nota: lajur "Tutup (awal)" dan "Purata tutup" ialah maklumat sahaja (berat sebelah ke arah kena henti), tidak dipakai dalam ujian.
