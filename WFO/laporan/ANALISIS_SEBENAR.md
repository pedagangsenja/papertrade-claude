# Analisis prestasi sebenar Papertrade C lawan jangkaan backtest

Dijana oleh `WFO/kod/analisis_sebenar.py`. Sumber: semua `papertrade/claude*.csv` (27370 posisi sah; 13070 tutup, 14300 terbuka; 2026-10-08 hingga 2026-11-20). Jangkaan = registry set 431 bagi varian modul (dalam sampel bagi M115–M161).

Ujian hanya atas posisi MATANG (dibeli >= 1.5 x hari pegang jangkaan dan >= 14 hari lalu; tutup = untung akhir, terbuka = untung semasa) untuk elak bias pemilihan (yang tutup awal kebanyakannya kena henti). Ambang: >= 10 posisi matang. AMARAN = kadar menang (z) atau purata (t) < −2 berbanding jangkaan.

**Ringkasan:** 18 AMARAN, 17 SELARI, 193 data belum cukup.

| Kaedah | Status | n | Matang | Menang matang | Menang jangka | Purata matang % | Purata jangka % | Hari jangka | Tutup (awal) | Purata tutup % | Terbuka purata % | z | t |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| M14 Walking with the Whales | AMARAN | 289 | 57 | 9% | 21% | -1.18 | 1.52 | 15 | 244 | -2.60 | 4.29 | -2.3 | -3.7 |
| M73 ADX(5) > 40 + Julat Terkecil 6 Hari | AMARAN | 294 | 195 | 60% | 63% | -0.95 | 0.18 | 5 | 233 | -0.02 | -4.92 | -1.0 | -2.3 |
| M102 Stockbee SLTB | AMARAN | 268 | 53 | 9% | 18% | -3.46 | 1.34 | 16 | 205 | -3.49 | 2.87 | -1.6 | -5.3 |
| M159 Heikin-Ashi Trend | AMARAN | 258 | 158 | 35% | 40% | -1.21 | 0.17 | 6 | 199 | -2.09 | -1.82 | -1.4 | -2.4 |
| M19 Sneaky Pivot (proksi harian) | AMARAN | 221 | 114 | 33% | 44% | -1.48 | 0.27 | 11 | 167 | -2.38 | -3.05 | -2.3 | -1.9 |
| M116 2/20 EMA Breakout (Landry) | AMARAN | 242 | 105 | 43% | 50% | -1.65 | 0.40 | 9 | 164 | -2.43 | -2.64 | -1.5 | -2.5 |
| M08 SMA20 + SMA200 | AMARAN | 215 | 73 | 21% | 32% | -2.34 | 1.07 | 12 | 162 | -3.40 | 3.19 | -2.0 | -4.9 |
| M148 Natural Number Method | AMARAN | 165 | 88 | 24% | 35% | -2.50 | 0.50 | 10 | 145 | -3.41 | 3.06 | -2.2 | -3.8 |
| M156 Single Penetration (DiNapoli) | AMARAN | 204 | 93 | 40% | 52% | -0.96 | 0.69 | 9 | 143 | -2.30 | -2.00 | -2.3 | -1.3 |
| M123 CCI Correction (Lambert, ChartSchool) | AMARAN | 158 | 91 | 20% | 28% | -2.10 | 0.92 | 10 | 139 | -2.08 | -0.17 | -1.7 | -9.0 |
| M153 Range Leader | AMARAN | 158 | 104 | 41% | 43% | -1.26 | 0.18 | 6 | 133 | -2.23 | -1.14 | -0.4 | -2.2 |
| M57 Landry Trend Knockout (TKO) | AMARAN | 177 | 19 | 11% | 21% | -4.97 | 1.55 | 18 | 131 | -4.79 | 2.70 | -1.1 | -5.6 |
| M106 DMI Wilder | AMARAN | 139 | 52 | 33% | 32% | -1.57 | 1.01 | 12 | 108 | -3.48 | 3.47 | 0.1 | -2.0 |
| M28 VWAP Separator + Kiss Pivot | AMARAN | 113 | 66 | 27% | 43% | -1.78 | 0.22 | 5 | 91 | -2.12 | -0.63 | -2.5 | -2.2 |
| M76 Undercut & Rally pada Low Penting | AMARAN | 87 | 40 | 25% | 37% | -2.72 | 0.67 | 9 | 75 | -2.91 | -0.25 | -1.5 | -4.0 |
| M50 Elder Triple Screen | AMARAN | 79 | 16 | 6% | 23% | -5.71 | 1.80 | 18 | 64 | -4.71 | 0.58 | -1.6 | -5.6 |
| M77 Undercut & Rally pada Purata Bergerak (MAU&R) | AMARAN | 61 | 14 | 21% | 25% | -0.84 | 2.69 | 15 | 45 | -3.58 | 4.06 | -0.3 | -2.8 |
| M47 Holy Grail Raschke | AMARAN | 41 | 24 | 46% | 51% | -3.29 | 0.25 | 5 | 33 | -2.54 | -1.64 | -0.5 | -2.1 |
| M49 Ichimoku (Tutup Atas Awan + Tenkan Silang Kijun) | DATA BELUM CUKUP | 245 | 0 |  | 23% |  | 3.99 | 34 | 169 | -5.32 | 1.89 |  |  |
| M12 Parabolic SAR | DATA BELUM CUKUP | 248 | 0 |  | 29% |  | 2.04 | 23 | 155 | -5.95 | 2.36 |  |  |
| M66 IBD Undur Pertama ke Purata 50 Hari | DATA BELUM CUKUP | 215 | 5 | 40% | 28% | -0.62 | 1.71 | 19 | 151 | -4.76 | 2.10 |  |  |
| M55 Guppy GMMA | DATA BELUM CUKUP | 215 | 0 |  | 26% |  | 2.71 | 28 | 149 | -6.11 | 3.02 |  |  |
| M124 'Last' Stochastic Technique (ChartSchool) | DATA BELUM CUKUP | 213 | 0 |  | 36% |  | 1.74 | 20 | 148 | -5.93 | 2.45 |  |  |
| M36 Turtle 55/20 | DATA BELUM CUKUP | 249 | 0 |  | 32% |  | 2.65 | 30 | 144 | -7.57 | 2.73 |  |  |
| M161 EMA 10/21 + Supertrend (10,3) | DATA BELUM CUKUP | 250 | 0 |  | 35% |  | 1.43 | 18 | 129 | -7.67 | 0.69 |  |  |
| M105 Supertrend tulen | DATA BELUM CUKUP | 247 | 0 |  | 39% |  | 2.44 | 32 | 124 | -8.63 | 2.60 |  |  |
| M89 Chande 65sma-3cc | DATA BELUM CUKUP | 199 | 0 |  | 34% |  | 1.83 | 26 | 123 | -6.78 | 1.98 |  |  |
| M111 Sistem Volatiliti Wilder | DATA BELUM CUKUP | 226 | 0 |  | 39% |  | 2.39 | 30 | 121 | -8.49 | 2.24 |  |  |
| M54 IBD Power Trend | DATA BELUM CUKUP | 197 | 0 |  | 30% |  | 3.37 | 37 | 116 | -6.65 | 2.14 |  |  |
| M81 Bensdorp Long Trend High Momentum | DATA BELUM CUKUP | 175 | 0 |  | 32% |  | 8.56 | 105 | 116 | -12.25 | -1.62 |  |  |
| N74X16  | DATA BELUM CUKUP | 150 | 0 |  |  |  |  |  | 115 | -2.46 | -1.64 |  |  |
| M155 Market Cycle Strategy | DATA BELUM CUKUP | 249 | 0 |  | 49% |  | 1.56 | 17 | 114 | -9.37 | -1.67 |  |  |
| M125 2-Bar Breakout | DATA BELUM CUKUP | 245 | 0 |  | 30% |  | 166.86 | 443 | 110 | -10.72 | -0.49 |  |  |
| N28X16  | DATA BELUM CUKUP | 160 | 0 |  |  |  |  |  | 109 | -2.69 | -2.17 |  |  |
| N28X36  | DATA BELUM CUKUP | 162 | 0 |  |  |  |  |  | 108 | -3.03 | -2.38 |  |  |
| M136 Short/Intermediate-term Low (Larry Williams) | DATA BELUM CUKUP | 234 | 0 |  | 24% |  | 112.90 | 343 | 105 | -10.27 | -1.05 |  |  |
| N08X16  | DATA BELUM CUKUP | 169 | 0 |  |  |  |  |  | 103 | -3.69 | -1.68 |  |  |
| N08X36  | DATA BELUM CUKUP | 169 | 0 |  |  |  |  |  | 98 | -4.39 | -1.73 |  |  |
| M80 Radge Saluran Purata Bergerak (MAC) | DATA BELUM CUKUP | 261 | 0 |  | 36% |  | 8.91 | 66 | 94 | -10.75 | 1.35 |  |  |
| M93 Bollinger Kaedah II: %b + MFI | DATA BELUM CUKUP | 235 | 0 |  | 36% |  | 8.20 | 62 | 90 | -10.46 | 2.71 |  |  |
| N76X16  | DATA BELUM CUKUP | 150 | 0 |  |  |  |  |  | 90 | -3.39 | -1.30 |  |  |
| M11 NR7 Breakout + Volume | DATA BELUM CUKUP | 125 | 5 | 60% | 36% | 3.98 | 2.86 | 20 | 89 | -2.43 | 1.60 |  |  |
| M10 EMA3 + CCI + MACD | DATA BELUM CUKUP | 152 | 0 |  | 33% |  | 4.70 | 54 | 88 | -8.41 | 4.05 |  |  |
| M74 Lulus Baharu Trend Template Minervini | DATA BELUM CUKUP | 121 | 0 |  | 24% |  | 2.72 | 20 | 87 | -3.72 | 3.55 |  |  |
| N41X16  | DATA BELUM CUKUP | 163 | 0 |  |  |  |  |  | 86 | -3.77 | -1.96 |  |  |
| M82 Arthur Hill Rotasi Sasaran 10% | DATA BELUM CUKUP | 323 | 0 |  | 61% |  | 1.84 | 38 | 85 | 2.51 | -6.42 |  |  |
| M95 Nisbah Kebaharuan High 52 Minggu (Bhootra & Hur) | DATA BELUM CUKUP | 138 | 0 |  | 32% |  | 2.68 | 29 | 85 | -6.48 | 1.57 |  |  |
| N113X36  | DATA BELUM CUKUP | 135 | 0 |  |  |  |  |  | 85 | -2.81 | -2.46 |  |  |
| N41X36  | DATA BELUM CUKUP | 163 | 0 |  |  |  |  |  | 84 | -4.40 | -1.82 |  |  |
| M31 Band Walk (BB 20/2) | DATA BELUM CUKUP | 234 | 0 |  | 43% |  | 3.30 | 32 | 82 | -12.53 | -0.08 |  |  |
| N113X16  | DATA BELUM CUKUP | 135 | 0 |  |  |  |  |  | 81 | -2.62 | -3.35 |  |  |
| M90 Pring KST | DATA BELUM CUKUP | 123 | 0 |  | 30% |  | 1.95 | 26 | 79 | -7.06 | 1.80 |  |  |
| M79 Radge: 20% Flipper | DATA BELUM CUKUP | 203 | 0 |  | 40% |  | 6.25 | 60 | 78 | -12.26 | -0.89 |  |  |
| M119 180 Bullish (Cooper) | DATA BELUM CUKUP | 129 | 0 |  | 27% |  | 1.17 | 18 | 76 | -5.59 | 2.03 |  |  |
| M158 Doubly Adaptive Profit Targets | DATA BELUM CUKUP | 213 | 0 |  | 34% |  | 2.94 | 30 | 76 | -8.40 | 0.28 |  |  |
| M131 Ross Hook (Joe Ross) | DATA BELUM CUKUP | 160 | 0 |  | 30% |  | 2.35 | 30 | 74 | -6.69 | 1.41 |  |  |
| N42X36  | DATA BELUM CUKUP | 131 | 0 |  |  |  |  |  | 72 | -2.72 | -1.61 |  |  |
| N48X36  | DATA BELUM CUKUP | 119 | 0 |  |  |  |  |  | 71 | -0.70 | -2.42 |  |  |
| N27X16  | DATA BELUM CUKUP | 150 | 0 |  |  |  |  |  | 70 | -4.24 | -2.19 |  |  |
| M122 Moving Momentum (ChartSchool) | DATA BELUM CUKUP | 111 | 0 |  | 35% |  | 1.79 | 24 | 69 | -8.54 | -0.90 |  |  |
| M151 Outside Bar Failure | DATA BELUM CUKUP | 112 | 0 |  | 27% |  | 1.93 | 26 | 69 | -3.73 | 3.79 |  |  |
| N42X16  | DATA BELUM CUKUP | 132 | 0 |  |  |  |  |  | 69 | -2.49 | -2.52 |  |  |
| N56X16  | DATA BELUM CUKUP | 162 | 0 |  |  |  |  |  | 69 | -5.53 | -1.90 |  |  |
| M137 Livermore System | DATA BELUM CUKUP | 154 | 0 |  | 35% |  | 4.22 | 37 | 68 | -8.32 | 1.00 |  |  |
| M33 Supertrend + SMA10 | DATA BELUM CUKUP | 159 | 0 |  | 40% |  | 1.65 | 33 | 67 | -10.45 | 1.04 |  |  |
| N29X16  | DATA BELUM CUKUP | 160 | 0 |  |  |  |  |  | 66 | -6.92 | -2.30 |  |  |
| M30 BB Free Bar + Himpitan 50/2.5 | DATA BELUM CUKUP | 142 | 0 |  | 37% |  | 3.80 | 34 | 65 | -9.77 | 1.29 |  |  |
| M34 Carter TTM Squeeze | DATA BELUM CUKUP | 125 | 0 |  | 34% |  | 2.38 | 30 | 65 | -7.88 | 4.63 |  |  |
| N36X36  | DATA BELUM CUKUP | 148 | 0 |  |  |  |  |  | 65 | -6.83 | -1.95 |  |  |
| M127 Slingshot Bullish | DATA BELUM CUKUP | 87 | 8 | 0% | 19% | -5.57 | 2.60 | 16 | 64 | -3.10 | 1.22 |  |  |
| N36X16  | DATA BELUM CUKUP | 149 | 0 |  |  |  |  |  | 63 | -6.21 | -2.46 |  |  |
| N76X36  | DATA BELUM CUKUP | 150 | 0 |  |  |  |  |  | 63 | -6.65 | -1.48 |  |  |
| N29X36  | DATA BELUM CUKUP | 159 | 0 |  |  |  |  |  | 60 | -8.70 | -1.99 |  |  |
| M04 BB Squeeze Breakout | DATA BELUM CUKUP | 123 | 0 |  | 36% |  | 4.96 | 32 | 59 | -9.52 | 0.81 |  |  |
| N54X36  | DATA BELUM CUKUP | 157 | 0 |  |  |  |  |  | 59 | -8.62 | -2.01 |  |  |
| N56X36  | DATA BELUM CUKUP | 163 | 0 |  |  |  |  |  | 59 | -7.09 | -1.97 |  |  |
| M26 Garis Trend Undur 3 Sentuhan + Pecahan | DATA BELUM CUKUP | 84 | 0 |  | 50% |  | 5.17 | 39 | 56 | -2.15 | -1.52 |  |  |
| N09X36  | DATA BELUM CUKUP | 138 | 0 |  |  |  |  |  | 56 | -5.28 | -2.14 |  |  |
| N24X36  | DATA BELUM CUKUP | 160 | 0 |  |  |  |  |  | 56 | -7.08 | -2.03 |  |  |
| M39 Radge Pecahan Bollinger 100 hari | DATA BELUM CUKUP | 206 | 0 |  | 37% |  | 9.11 | 96 | 55 | -17.14 | -0.25 |  |  |
| N45X16  | DATA BELUM CUKUP | 152 | 0 |  |  |  |  |  | 55 | -5.56 | -2.17 |  |  |
| M06 Minervini VCP Breakout | DATA BELUM CUKUP | 91 | 0 |  | 33% |  | 2.49 | 29 | 53 | -8.51 | 2.34 |  |  |
| M145 Yum-Yum Continuation | DATA BELUM CUKUP | 203 | 0 |  | 25% |  | 80.48 | 356 | 52 | -14.09 | -1.67 |  |  |
| M149 3-Step Pullback | DATA BELUM CUKUP | 146 | 0 |  | 19% |  | 59.37 | 273 | 51 | -7.70 | 0.62 |  |  |
| N27X36  | DATA BELUM CUKUP | 150 | 0 |  |  |  |  |  | 50 | -7.54 | -2.54 |  |  |
| N43X36  | DATA BELUM CUKUP | 141 | 0 |  |  |  |  |  | 50 | -7.04 | -1.94 |  |  |
| N07X36  | DATA BELUM CUKUP | 132 | 0 |  |  |  |  |  | 46 | -10.01 | -2.89 |  |  |
| N24X16  | DATA BELUM CUKUP | 160 | 0 |  |  |  |  |  | 45 | -8.61 | -2.21 |  |  |
| M100 Bulkowski Segi Empat & Segi Tiga Menaik | DATA BELUM CUKUP | 66 | 0 |  | 46% |  | 1.32 | 29 | 44 | -0.21 | -3.70 |  |  |
| N53X16  | DATA BELUM CUKUP | 158 | 0 |  |  |  |  |  | 44 | -8.07 | -2.14 |  |  |
| N54X16  | DATA BELUM CUKUP | 158 | 0 |  |  |  |  |  | 44 | -10.28 | -2.40 |  |  |
| M88 O'Neil Shakeout +3 | DATA BELUM CUKUP | 81 | 0 |  | 32% |  | 5.56 | 32 | 43 | -8.15 | 2.11 |  |  |
| N07X16  | DATA BELUM CUKUP | 133 | 0 |  |  |  |  |  | 43 | -9.44 | -2.71 |  |  |
| N45X36  | DATA BELUM CUKUP | 152 | 0 |  |  |  |  |  | 43 | -8.34 | -2.29 |  |  |
| N42X17  | DATA BELUM CUKUP | 133 | 0 |  |  |  |  |  | 42 | -0.01 | -4.19 |  |  |
| M132 Ascending Scallop (Bulkowski) | DATA BELUM CUKUP | 89 | 0 |  | 42% |  | 0.98 | 29 | 41 | -9.81 | 0.30 |  |  |
| M32 Momentum Burst | DATA BELUM CUKUP | 68 | 0 |  | 25% |  | 3.57 | 22 | 41 | -6.38 | 3.16 |  |  |
| N53X36  | DATA BELUM CUKUP | 158 | 0 |  |  |  |  |  | 41 | -7.72 | -2.60 |  |  |
| N33X36  | DATA BELUM CUKUP | 121 | 0 |  |  |  |  |  | 40 | -10.18 | -1.89 |  |  |
| N47X16  | DATA BELUM CUKUP | 141 | 0 |  |  |  |  |  | 40 | -7.36 | -2.91 |  |  |
| M139 均线首次粘合向上发散 (MA berhimpun kali pertama, berkipas naik) | DATA BELUM CUKUP | 93 | 0 |  | 51% |  | 1.31 | 19 | 39 | -5.50 | -3.59 |  |  |
| N25X16  | DATA BELUM CUKUP | 153 | 0 |  |  |  |  |  | 39 | -9.45 | -1.86 |  |  |
| N40X16  | DATA BELUM CUKUP | 117 | 0 |  |  |  |  |  | 39 | -5.96 | -1.08 |  |  |
| M154 HOLP (High of Low Period) | DATA BELUM CUKUP | 91 | 0 |  | 39% |  | 1.93 | 27 | 38 | -11.16 | -1.08 |  |  |
| N25X36  | DATA BELUM CUKUP | 153 | 0 |  |  |  |  |  | 38 | -9.59 | -2.12 |  |  |
| N47X36  | DATA BELUM CUKUP | 141 | 0 |  |  |  |  |  | 38 | -8.64 | -2.92 |  |  |
| M146 3-Bar Momentum Pattern | DATA BELUM CUKUP | 72 | 0 |  | 27% |  | 2.66 | 26 | 37 | -5.89 | 4.13 |  |  |
| M118 Expansion Pivot (Cooper) | DATA BELUM CUKUP | 85 | 0 |  | 33% |  | 1.56 | 27 | 36 | -7.01 | 2.14 |  |  |
| N22X36  | DATA BELUM CUKUP | 117 | 0 |  |  |  |  |  | 36 | -9.73 | -3.06 |  |  |
| M29 EMA3 + RSI75 + Stokastik | DATA BELUM CUKUP | 43 | 0 |  | 18% |  | 3.22 | 35 | 35 | -3.38 | 1.40 |  |  |
| N56X17  | DATA BELUM CUKUP | 162 | 0 |  |  |  |  |  | 35 | -2.38 | -4.98 |  |  |
| M147 Improved Three-Bar Pullback | DATA BELUM CUKUP | 96 | 0 |  | 31% |  | 91.01 | 442 | 34 | -14.18 | -1.86 |  |  |
| N22X16  | DATA BELUM CUKUP | 117 | 0 |  |  |  |  |  | 34 | -10.89 | -3.15 |  |  |
| N33X16  | DATA BELUM CUKUP | 122 | 0 |  |  |  |  |  | 34 | -11.65 | -2.45 |  |  |
| N38X36  | DATA BELUM CUKUP | 77 | 0 |  |  |  |  |  | 34 | -7.67 | -1.09 |  |  |
| M91 Stochastic Pop (Bernstein/Steckler) | DATA BELUM CUKUP | 42 | 0 |  | 42% |  | 1.63 | 18 | 33 | -6.29 | 4.24 |  |  |
| N68X16  | DATA BELUM CUKUP | 102 | 0 |  |  |  |  |  | 33 | -6.03 | -2.47 |  |  |
| N75X17  | DATA BELUM CUKUP | 149 | 0 |  |  |  |  |  | 32 | 1.24 | -7.17 |  |  |
| M01 Bollinger Band + RSI | DATA BELUM CUKUP | 115 | 0 |  | 67% |  | 2.22 | 22 | 30 | 12.27 | -6.92 |  |  |
| M101 Bulkowski: Tiga lembah menaik | DATA BELUM CUKUP | 53 | 0 |  | 35% |  | 3.46 | 33 | 30 | -10.39 | 2.37 |  |  |
| M134 First Kiss After Daylight (Landry) | DATA BELUM CUKUP | 64 | 0 |  | 34% |  | 5.41 | 35 | 30 | -6.73 | 0.46 |  |  |
| M09 Volumatic VIDYA Pivot Retest | DATA BELUM CUKUP | 42 | 0 |  | 23% |  | 1.85 | 30 | 28 | -7.34 | -2.17 |  |  |
| N40X36  | DATA BELUM CUKUP | 107 | 0 |  |  |  |  |  | 28 | -11.84 | -0.44 |  |  |
| M115 Bow Tie (Landry) | DATA BELUM CUKUP | 36 | 0 |  | 27% |  | 1.06 | 18 | 27 | -5.02 | 5.85 |  |  |
| N24X17  | DATA BELUM CUKUP | 160 | 0 |  |  |  |  |  | 27 | -3.33 | -4.72 |  |  |
| N68X36  | DATA BELUM CUKUP | 103 | 0 |  |  |  |  |  | 27 | -6.31 | -2.50 |  |  |
| N36X14  | DATA BELUM CUKUP | 148 | 0 |  |  |  |  |  | 26 | -1.11 | -6.85 |  |  |
| M67 Rayner Teo: Ujian Ketiga pada Purata 50 | DATA BELUM CUKUP | 33 | 0 |  | 30% |  | 1.90 | 24 | 25 | -6.23 | 5.32 |  |  |
| M78 Alvarez Pecahan Mingguan DTAYS | DATA BELUM CUKUP | 33 | 0 |  | 32% |  | 3.17 | 40 | 25 | -9.03 | 2.26 |  |  |
| N42X14  | DATA BELUM CUKUP | 131 | 0 |  |  |  |  |  | 24 | 4.27 | -5.09 |  |  |
| M46 Jurang Naik Boleh Beli (Buyable Gap Up) | DATA BELUM CUKUP | 33 | 0 |  | 23% |  | 2.81 | 22 | 22 | -4.19 | 3.64 |  |  |
| M48 Cooper 1-2-3-4 | DATA BELUM CUKUP | 69 | 0 |  | 34% |  | 2.79 | 30 | 22 | -9.96 | 2.80 |  |  |
| M59 Anjakan Julat RSI | DATA BELUM CUKUP | 38 | 0 |  | 34% |  | 3.10 | 37 | 22 | -11.85 | 1.33 |  |  |
| N37X16  | DATA BELUM CUKUP | 62 | 0 |  |  |  |  |  | 22 | -8.09 | -0.41 |  |  |
| N28X14  | DATA BELUM CUKUP | 162 | 0 |  |  |  |  |  | 21 | 0.74 | -6.66 |  |  |
| N37X17  | DATA BELUM CUKUP | 62 | 0 |  |  |  |  |  | 21 | -0.60 | -4.32 |  |  |
| N37X36  | DATA BELUM CUKUP | 62 | 0 |  |  |  |  |  | 21 | -6.49 | -1.23 |  |  |
| N33X14  | DATA BELUM CUKUP | 121 | 0 |  |  |  |  |  | 19 | -5.75 | -5.51 |  |  |
| N57X16  | DATA BELUM CUKUP | 85 | 0 |  |  |  |  |  | 19 | -13.90 | -3.92 |  |  |
| M117 Landry Pullback (high 2 bulan) | DATA BELUM CUKUP | 109 | 0 |  | 21% |  | 45.52 | 287 | 18 | -9.08 | 0.38 |  |  |
| M140 猎豹出击 (Serangan Cheetah) | DATA BELUM CUKUP | 39 | 0 |  | 36% |  | 5.31 | 25 | 18 | -10.96 | 2.36 |  |  |
| N22X14  | DATA BELUM CUKUP | 117 | 0 |  |  |  |  |  | 18 | -3.85 | -6.65 |  |  |
| N31X36  | DATA BELUM CUKUP | 111 | 0 |  |  |  |  |  | 18 | -16.30 | -2.74 |  |  |
| N35X36  | DATA BELUM CUKUP | 94 | 0 |  |  |  |  |  | 18 | -14.77 | -2.05 |  |  |
| N80X36  | DATA BELUM CUKUP | 86 | 0 |  |  |  |  |  | 18 | -14.65 | -1.96 |  |  |
| M141 First Thrust (Landry) | DATA BELUM CUKUP | 28 | 0 |  | 39% |  | 4.05 | 37 | 17 | -12.28 | -2.07 |  |  |
| M68 Kell Base n' Break | DATA BELUM CUKUP | 49 | 0 |  | 36% |  | 1.35 | 35 | 17 | -8.72 | -0.93 |  |  |
| N124X36  | DATA BELUM CUKUP | 45 | 0 |  |  |  |  |  | 16 | -4.34 | -1.65 |  |  |
| M05 MACD Divergence + Pengesahan | DATA BELUM CUKUP | 45 | 0 |  | 35% |  | 10.85 | 108 | 15 | -9.22 | -0.24 |  |  |
| N57X36  | DATA BELUM CUKUP | 85 | 0 |  |  |  |  |  | 15 | -15.49 | -4.24 |  |  |
| N39X36  | DATA BELUM CUKUP | 47 | 0 |  |  |  |  |  | 14 | -15.57 | -2.43 |  |  |
| N75X14  | DATA BELUM CUKUP | 149 | 0 |  |  |  |  |  | 13 | 10.66 | -7.37 |  |  |
| M120 Reversal New Highs | DATA BELUM CUKUP | 19 | 0 |  | 27% |  | 1.15 | 28 | 12 | -6.32 | 3.83 |  |  |
| N25X17  | DATA BELUM CUKUP | 153 | 0 |  |  |  |  |  | 12 | -5.34 | -4.69 |  |  |
| N64X16  | DATA BELUM CUKUP | 48 | 0 |  |  |  |  |  | 12 | -11.53 | -0.02 |  |  |
| N64X17  | DATA BELUM CUKUP | 48 | 0 |  |  |  |  |  | 12 | 1.35 | -4.12 |  |  |
| M126 Hidden Smash Day (beli, Larry Williams) | DATA BELUM CUKUP | 21 | 0 |  | 35% |  | 5.15 | 33 | 11 | -7.73 | 1.48 |  |  |
| M142 Pecahan volum dari dasar (底部放量) | DATA BELUM CUKUP | 53 | 0 |  | 41% |  | 6.85 | 44 | 11 | -14.93 | -0.13 |  |  |
| M152 Spike & Ledge | DATA BELUM CUKUP | 56 | 0 |  | 52% |  | 3.20 | 36 | 11 | -15.43 | -3.04 |  |  |
| N51X36  | DATA BELUM CUKUP | 25 | 0 |  |  |  |  |  | 11 | -6.74 | -2.30 |  |  |
| M107 Golden Cross SMA50/200 | DATA BELUM CUKUP | 48 | 0 |  | 32% |  | 15.43 | 110 | 10 | -10.93 | -2.03 |  |  |
| M129 Wick Play | DATA BELUM CUKUP | 26 | 0 |  | 38% |  | 2.60 | 38 | 10 | -13.31 | 3.42 |  |  |
| N51X16  | DATA BELUM CUKUP | 24 | 0 |  |  |  |  |  | 10 | -8.68 | -1.78 |  |  |
| N64X36  | DATA BELUM CUKUP | 48 | 0 |  |  |  |  |  | 10 | -9.20 | -1.22 |  |  |
| M87 IBD Tapak Menaik | DATA BELUM CUKUP | 13 | 0 |  | 32% |  | 3.49 | 30 | 9 | -9.18 | 7.32 |  |  |
| N201X36  | DATA BELUM CUKUP | 35 | 0 |  |  |  |  |  | 9 | -13.63 | -3.44 |  |  |
| N37X14  | DATA BELUM CUKUP | 62 | 0 |  |  |  |  |  | 9 | 1.66 | -6.20 |  |  |
| M44 Tapak Rata IBD | DATA BELUM CUKUP | 12 | 0 |  | 30% |  | 0.39 | 28 | 8 | -7.46 | 1.29 |  |  |
| M52 Radge Weekend Trend Trader | DATA BELUM CUKUP | 9 | 0 |  | 37% |  | 5.19 | 37 | 8 | -15.12 | 0.44 |  |  |
| M84 Jarak purata bergerak MAD 21/200 | DATA BELUM CUKUP | 10 | 0 |  | 37% |  | 3.71 | 26 | 8 | -9.88 | 4.63 |  |  |
| M144 Screw Bar | DATA BELUM CUKUP | 10 | 0 |  | 41% |  | 7.68 | 23 | 7 | -3.56 | 1.60 |  |  |
| N53X17  | DATA BELUM CUKUP | 158 | 0 |  |  |  |  |  | 7 | -6.98 | -4.71 |  |  |
| M135 3rd Watch | DATA BELUM CUKUP | 15 | 0 |  | 39% |  | 2.05 | 35 | 6 | -22.67 | -2.26 |  |  |
| M96 Momo India: Ranking Sharpe 3/6/12 bulan | DATA BELUM CUKUP | 6 | 0 |  | 43% |  | 12.18 | 54 | 6 | -13.20 |  |  |  |
| N50X14  | DATA BELUM CUKUP | 33 | 0 |  |  |  |  |  | 6 | 3.18 | -6.47 |  |  |
| N66X36  | DATA BELUM CUKUP | 54 | 0 |  |  |  |  |  | 6 | -23.95 | -2.48 |  |  |
| M21 Marius 3 Persediaan (Pecahan+Jurang+Kesinambungan) | DATA BELUM CUKUP | 6 | 5 | 20% | 26% | -2.96 | 2.57 | 8 | 5 | -2.96 | 0.59 |  |  |
| M41 FW Penyatuan Mingguan | DATA BELUM CUKUP | 24 | 0 |  | 36% |  | 15.03 | 117 | 5 | -15.64 | -0.72 |  |  |
| N06X36  | DATA BELUM CUKUP | 32 | 0 |  |  |  |  |  | 5 | -5.44 | -2.99 |  |  |
| N28X17  | DATA BELUM CUKUP | 162 | 0 |  |  |  |  |  | 5 | -4.28 | -6.11 |  |  |
| N50X17  | DATA BELUM CUKUP | 33 | 0 |  |  |  |  |  | 5 | -1.85 | -6.46 |  |  |
| N64X14  | DATA BELUM CUKUP | 48 | 0 |  |  |  |  |  | 5 | 3.14 | -4.18 |  |  |
| M121 High 2 bull flag (Brooks) | DATA BELUM CUKUP | 9 | 0 |  | 47% |  | 2.47 | 49 | 4 | -16.77 | -1.10 |  |  |
| M130 多方炮 (dua lilin hijau mengapit satu merah) | DATA BELUM CUKUP | 12 | 0 |  | 25% |  | 92.22 | 261 | 4 | -16.29 | -0.84 |  |  |
| N119X13  | DATA BELUM CUKUP | 150 | 0 |  |  |  |  |  | 4 | 4.96 | -7.01 |  |  |
| M143 장대양봉 이후 눌림목 / 5일선 매매 (Undur ke MA5 selepas lilin naik panjang) | DATA BELUM CUKUP | 28 | 0 |  | 52% |  | 0.83 | 18 | 3 | -11.92 | -3.32 |  |  |
| M157 Consolidation Pivot Breakout (versi angka) | DATA BELUM CUKUP | 8 | 0 |  | 14% |  | 32.05 | 179 | 3 | -8.78 | 0.66 |  |  |
| N202X36  | DATA BELUM CUKUP | 59 | 0 |  |  |  |  |  | 3 | -6.84 | -1.22 |  |  |
| N203X36  | DATA BELUM CUKUP | 19 | 0 |  |  |  |  |  | 3 | -29.60 | -4.21 |  |  |
| N65X14  | DATA BELUM CUKUP | 28 | 0 |  |  |  |  |  | 3 | -7.77 | -4.87 |  |  |
| N65X36  | DATA BELUM CUKUP | 28 | 0 |  |  |  |  |  | 3 | -31.74 | -2.34 |  |  |
| M07 Qullamaggie Breakout | DATA BELUM CUKUP | 2 | 2 | 0% | 20% | -3.04 | 1.05 | 8 | 2 | -3.04 |  |  |  |
| M45 High 52 Minggu (George & Hwang) | DATA BELUM CUKUP | 8 | 0 |  | 32% |  | 12.81 | 61 | 2 | -9.78 | 0.20 |  |  |
| M64 O'Neil Tiga Minggu Ketat | DATA BELUM CUKUP | 3 | 0 |  | 34% |  | 1.68 | 31 | 2 | -3.27 | 10.55 |  |  |
| N204X36  | DATA BELUM CUKUP | 3 | 0 |  |  |  |  |  | 2 | -7.04 | 0.00 |  |  |
| M38 Darvas Kotak | DATA BELUM CUKUP | 26 | 0 |  | 49% |  | 18.79 | 210 | 1 | -9.28 | -4.43 |  |  |
| M51 O'Neil Cawan & Pemegang | DATA BELUM CUKUP | 3 | 0 |  | 39% |  | 3.12 | 35 | 1 | -7.27 | -0.95 |  |  |
| N19X13  | DATA BELUM CUKUP | 105 | 0 |  |  |  |  |  | 1 | 52.25 | -4.07 |  |  |
| M104 High Tight Flag / Power Play | DATA BELUM CUKUP | 1 | 0 |  | 35% |  | 5.62 | 33 | 0 |  | 20.52 |  |  |
| M138 直升机空中加油 (Helikopter isi minyak di udara) | DATA BELUM CUKUP | 4 | 0 |  | 45% |  | 4.60 | 46 | 0 |  | -3.06 |  |  |
| M37 Weinstein Peringkat 2 | DATA BELUM CUKUP | 7 | 0 |  | 41% |  | 5.49 | 42 | 0 |  | -3.41 |  |  |
| M94 Pecutan Momentum (Chen, Yu & Wang) | DATA BELUM CUKUP | 12 | 0 |  | 63% |  | 24.04 | 121 | 0 |  | -16.81 |  |  |
| N119X15  | DATA BELUM CUKUP | 150 | 0 |  |  |  |  |  | 0 |  | -6.81 |  |  |
| N124X15  | DATA BELUM CUKUP | 44 | 0 |  |  |  |  |  | 0 |  | -4.29 |  |  |
| N16X13  | DATA BELUM CUKUP | 149 | 0 |  |  |  |  |  | 0 |  | -6.38 |  |  |
| N16X15  | DATA BELUM CUKUP | 149 | 0 |  |  |  |  |  | 0 |  | -6.38 |  |  |
| N42X15  | DATA BELUM CUKUP | 130 | 0 |  |  |  |  |  | 0 |  | -4.52 |  |  |
| N55X13  | DATA BELUM CUKUP | 116 | 0 |  |  |  |  |  | 0 |  | -5.33 |  |  |
| N73X13  | DATA BELUM CUKUP | 140 | 0 |  |  |  |  |  | 0 |  | -5.89 |  |  |
| N75X13  | DATA BELUM CUKUP | 149 | 0 |  |  |  |  |  | 0 |  | -6.62 |  |  |
| N75X15  | DATA BELUM CUKUP | 149 | 0 |  |  |  |  |  | 0 |  | -6.62 |  |  |
| M03 BB Break + Divergence RSI | SELARI | 278 | 175 | 66% | 56% | 0.55 | 0.58 | 8 | 233 | -0.31 | -5.02 | 2.5 | -0.1 |
| M92 CCI-50 | SELARI | 298 | 114 | 59% | 49% | 1.42 | 1.17 | 13 | 225 | -2.33 | 0.96 | 2.2 | 0.3 |
| M20 EMA10/15 Crossover + Sudut | SELARI | 256 | 181 | 38% | 39% | -0.24 | 0.22 | 7 | 223 | -1.10 | -1.04 | -0.3 | -0.9 |
| M18 EMA9/21 Pullback | SELARI | 265 | 160 | 27% | 26% | 0.00 | 0.40 | 7 | 218 | -1.67 | 4.29 | 0.3 | -0.7 |
| M70 Pecahan Hari Dalam | SELARI | 245 | 118 | 14% | 11% | 0.31 | 0.84 | 10 | 209 | -1.90 | 7.28 | 1.0 | -0.7 |
| M13 Garis Trend Action/Safety Line | SELARI | 284 | 123 | 35% | 34% | 0.48 | 0.97 | 11 | 200 | -2.79 | 0.68 | 0.1 | -0.6 |
| M15 Break & Retest + Henti ATR | SELARI | 261 | 106 | 41% | 33% | 0.44 | 1.08 | 12 | 199 | -2.91 | 6.04 | 1.6 | -0.8 |
| M35 Pocket Pivot Morales & Kacher | SELARI | 229 | 142 | 27% | 28% | 0.24 | 0.29 | 9 | 186 | -1.19 | 3.88 | -0.2 | -0.1 |
| M25 VWAP Wave (proksi harian) | SELARI | 174 | 103 | 32% | 30% | 0.95 | 0.42 | 10 | 138 | -0.63 | 0.90 | 0.5 | 0.5 |
| M99 Three Line Break | SELARI | 177 | 43 | 47% | 40% | 2.48 | 1.17 | 16 | 132 | -4.31 | 1.29 | 0.9 | 0.8 |
| M02 MACD + SMA200 | SELARI | 153 | 52 | 38% | 44% | 1.48 | 0.66 | 14 | 123 | -3.22 | -4.50 | -0.7 | 0.5 |
| M128 Inventory Retracement Bar (IRB, Rob Hoffman) | SELARI | 136 | 44 | 32% | 34% | -0.97 | 0.55 | 12 | 83 | -4.60 | 1.56 | -0.3 | -1.3 |
| M160 Measured Move Up | SELARI | 106 | 51 | 31% | 32% | -0.41 | 0.44 | 8 | 70 | -3.11 | 0.12 | -0.1 | -1.0 |
| M23 Breitstein Kapitulasi + Kesinambungan | SELARI | 99 | 38 | 18% | 22% | -0.80 | 0.55 | 10 | 67 | -2.67 | 2.91 | -0.5 | -1.7 |
| M27 Price Action 4 Tiang | SELARI | 65 | 65 | 31% | 35% | -0.34 | 0.36 | 7 | 62 | -1.17 | 16.82 | -0.8 | -0.8 |
| M150 Trend Bar Failure (Brooks) | SELARI | 90 | 30 | 30% | 37% | -1.46 | 0.54 | 13 | 56 | -3.41 | 1.44 | -0.8 | -1.9 |
| M133 Bull Hook (Crabel) | SELARI | 54 | 21 | 43% | 41% | 2.31 | 0.68 | 10 | 39 | -1.13 | -0.75 | 0.2 | 0.9 |

Nota: lajur "Tutup (awal)" dan "Purata tutup" ialah maklumat sahaja (berat sebelah ke arah kena henti), tidak dipakai dalam ujian.
