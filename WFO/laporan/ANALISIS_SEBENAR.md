# Analisis prestasi sebenar Papertrade C lawan jangkaan backtest

Dijana oleh `WFO/kod/analisis_sebenar.py`. Sumber: semua `papertrade/claude*.csv` (31699 posisi sah; 16535 tutup, 15164 terbuka; 2026-10-08 hingga 2026-11-27). Jangkaan = registry set 431 bagi varian modul (dalam sampel bagi M115–M161).

Ujian hanya atas posisi MATANG (dibeli >= 1.5 x hari pegang jangkaan dan >= 14 hari lalu; tutup = untung akhir, terbuka = untung semasa) untuk elak bias pemilihan (yang tutup awal kebanyakannya kena henti). Ambang: >= 10 posisi matang. AMARAN = kadar menang (z) atau purata (t) < −2 berbanding jangkaan.

**Ringkasan:** 25 AMARAN, 111 SELARI, 92 data belum cukup.

| Kaedah | Status | n | Matang | Menang matang | Menang jangka | Purata matang % | Purata jangka % | Hari jangka | Tutup (awal) | Purata tutup % | Terbuka purata % | z | t |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| M14 Walking with the Whales | AMARAN | 332 | 115 | 11% | 21% | -0.51 | 1.52 | 15 | 273 | -2.46 | 6.09 | -2.6 | -3.4 |
| M92 CCI-50 | AMARAN | 333 | 166 | 47% | 49% | -0.44 | 1.17 | 13 | 261 | -1.93 | 1.57 | -0.4 | -2.5 |
| M03 BB Break + Divergence RSI | AMARAN | 315 | 226 | 61% | 56% | -0.59 | 0.58 | 8 | 259 | -1.54 | -0.73 | 1.3 | -2.5 |
| M159 Heikin-Ashi Trend | AMARAN | 298 | 208 | 31% | 40% | -1.98 | 0.17 | 6 | 246 | -2.11 | 1.74 | -2.6 | -3.6 |
| M20 EMA10/15 Crossover + Sudut | AMARAN | 289 | 226 | 35% | 39% | -0.69 | 0.22 | 7 | 242 | -1.29 | 2.07 | -1.4 | -2.1 |
| M102 Stockbee SLTB | AMARAN | 305 | 101 | 12% | 18% | -2.02 | 1.34 | 16 | 225 | -3.47 | 6.31 | -1.6 | -4.3 |
| M116 2/20 EMA Breakout (Landry) | AMARAN | 272 | 154 | 42% | 50% | -1.95 | 0.40 | 9 | 204 | -2.68 | 1.37 | -2.1 | -3.7 |
| M19 Sneaky Pivot (proksi harian) | AMARAN | 250 | 150 | 33% | 44% | -2.33 | 0.27 | 11 | 188 | -3.14 | 0.91 | -2.8 | -3.4 |
| M08 SMA20 + SMA200 | AMARAN | 242 | 107 | 24% | 32% | -1.15 | 1.07 | 12 | 186 | -3.26 | 6.99 | -1.6 | -2.4 |
| M155 Market Cycle Strategy | AMARAN | 289 | 38 | 21% | 49% | -4.40 | 1.56 | 17 | 175 | -9.44 | -0.31 | -3.5 | -3.8 |
| M156 Single Penetration (DiNapoli) | AMARAN | 226 | 140 | 34% | 52% | -2.11 | 0.69 | 9 | 164 | -2.35 | 2.09 | -4.3 | -3.0 |
| M148 Natural Number Method | AMARAN | 185 | 123 | 24% | 35% | -2.18 | 0.50 | 10 | 160 | -3.18 | 4.37 | -2.5 | -4.0 |
| M153 Range Leader | AMARAN | 178 | 134 | 40% | 43% | -1.85 | 0.18 | 6 | 158 | -2.08 | 1.67 | -0.7 | -2.6 |
| M123 CCI Correction (Lambert, ChartSchool) | AMARAN | 181 | 123 | 21% | 28% | -1.91 | 0.92 | 10 | 155 | -2.15 | 1.64 | -1.6 | -9.5 |
| M57 Landry Trend Knockout (TKO) | AMARAN | 190 | 40 | 8% | 21% | -4.80 | 1.55 | 18 | 147 | -4.68 | 7.78 | -2.1 | -8.2 |
| M128 Inventory Retracement Bar (IRB, Rob Hoffman) | AMARAN | 164 | 78 | 29% | 34% | -1.56 | 0.55 | 12 | 112 | -3.35 | 4.42 | -0.8 | -2.4 |
| M28 VWAP Separator + Kiss Pivot | AMARAN | 138 | 92 | 23% | 43% | -2.12 | 0.22 | 5 | 107 | -2.34 | 2.55 | -3.9 | -3.5 |
| M74 Lulus Baharu Trend Template Minervini | AMARAN | 130 | 14 | 21% | 24% | -2.05 | 2.72 | 20 | 95 | -3.67 | 6.97 | -0.2 | -3.9 |
| M119 180 Bullish (Cooper) | AMARAN | 142 | 13 | 8% | 27% | -6.33 | 1.17 | 18 | 87 | -5.21 | 4.66 | -1.6 | -4.2 |
| M76 Undercut & Rally pada Low Penting | AMARAN | 101 | 52 | 25% | 37% | -2.92 | 0.67 | 9 | 87 | -2.78 | 1.94 | -1.8 | -5.2 |
| M23 Breitstein Kapitulasi + Kesinambungan | AMARAN | 103 | 68 | 25% | 22% | -0.96 | 0.55 | 10 | 81 | -1.93 | 7.83 | 0.6 | -2.5 |
| M50 Elder Triple Screen | AMARAN | 89 | 37 | 3% | 23% | -4.97 | 1.80 | 18 | 71 | -4.76 | 5.80 | -2.9 | -10.2 |
| M127 Slingshot Bullish | AMARAN | 87 | 37 | 11% | 19% | -1.76 | 2.60 | 16 | 69 | -3.17 | 6.60 | -1.3 | -4.9 |
| M77 Undercut & Rally pada Purata Bergerak (MAU&R) | AMARAN | 71 | 25 | 16% | 25% | -1.22 | 2.69 | 15 | 54 | -3.37 | 7.03 | -1.0 | -3.0 |
| M47 Holy Grail Raschke | AMARAN | 60 | 34 | 41% | 51% | -2.51 | 0.25 | 5 | 41 | -2.60 | 1.59 | -1.2 | -2.1 |
| M49 Ichimoku (Tutup Atas Awan + Tenkan Silang Kijun) | DATA BELUM CUKUP | 275 | 0 |  | 23% |  | 3.99 | 34 | 193 | -5.32 | 5.66 |  |  |
| M12 Parabolic SAR | DATA BELUM CUKUP | 280 | 4 | 50% | 29% | 2.60 | 2.04 | 23 | 182 | -5.80 | 6.18 |  |  |
| M124 'Last' Stochastic Technique (ChartSchool) | DATA BELUM CUKUP | 237 | 0 |  | 36% |  | 1.74 | 20 | 178 | -5.53 | 6.08 |  |  |
| M55 Guppy GMMA | DATA BELUM CUKUP | 250 | 0 |  | 26% |  | 2.71 | 28 | 176 | -6.08 | 6.33 |  |  |
| M36 Turtle 55/20 | DATA BELUM CUKUP | 264 | 0 |  | 32% |  | 2.65 | 30 | 166 | -7.35 | 6.83 |  |  |
| M105 Supertrend tulen | DATA BELUM CUKUP | 255 | 0 |  | 39% |  | 2.44 | 32 | 160 | -7.77 | 7.62 |  |  |
| M89 Chande 65sma-3cc | DATA BELUM CUKUP | 213 | 0 |  | 34% |  | 1.83 | 26 | 160 | -5.96 | 7.14 |  |  |
| M111 Sistem Volatiliti Wilder | DATA BELUM CUKUP | 234 | 0 |  | 39% |  | 2.39 | 30 | 155 | -7.53 | 6.95 |  |  |
| M136 Short/Intermediate-term Low (Larry Williams) | DATA BELUM CUKUP | 268 | 0 |  | 24% |  | 112.90 | 343 | 142 | -10.39 | 3.50 |  |  |
| M81 Bensdorp Long Trend High Momentum | DATA BELUM CUKUP | 175 | 0 |  | 32% |  | 8.56 | 105 | 131 | -12.15 | 2.25 |  |  |
| M54 IBD Power Trend | DATA BELUM CUKUP | 211 | 0 |  | 30% |  | 3.37 | 37 | 130 | -6.67 | 6.55 |  |  |
| M125 2-Bar Breakout | DATA BELUM CUKUP | 282 | 0 |  | 30% |  | 166.86 | 443 | 129 | -10.75 | 3.62 |  |  |
| M80 Radge Saluran Purata Bergerak (MAC) | DATA BELUM CUKUP | 267 | 0 |  | 36% |  | 8.91 | 66 | 122 | -10.48 | 6.59 |  |  |
| M31 Band Walk (BB 20/2) | DATA BELUM CUKUP | 241 | 0 |  | 43% |  | 3.30 | 32 | 117 | -10.93 | 5.47 |  |  |
| M79 Radge: 20% Flipper | DATA BELUM CUKUP | 221 | 0 |  | 40% |  | 6.25 | 60 | 117 | -10.92 | 3.73 |  |  |
| M82 Arthur Hill Rotasi Sasaran 10% | DATA BELUM CUKUP | 363 | 0 |  | 61% |  | 1.84 | 38 | 112 | -1.13 | -2.11 |  |  |
| M93 Bollinger Kaedah II: %b + MFI | DATA BELUM CUKUP | 240 | 0 |  | 36% |  | 8.20 | 62 | 111 | -10.09 | 7.90 |  |  |
| M158 Doubly Adaptive Profit Targets | DATA BELUM CUKUP | 226 | 0 |  | 34% |  | 2.94 | 30 | 100 | -7.49 | 4.27 |  |  |
| M10 EMA3 + CCI + MACD | DATA BELUM CUKUP | 155 | 0 |  | 33% |  | 4.70 | 54 | 96 | -8.33 | 7.78 |  |  |
| M90 Pring KST | DATA BELUM CUKUP | 127 | 0 |  | 30% |  | 1.95 | 26 | 94 | -6.54 | 6.27 |  |  |
| M95 Nisbah Kebaharuan High 52 Minggu (Bhootra & Hur) | DATA BELUM CUKUP | 148 | 0 |  | 32% |  | 2.68 | 29 | 94 | -6.50 | 5.24 |  |  |
| M33 Supertrend + SMA10 | DATA BELUM CUKUP | 161 | 0 |  | 40% |  | 1.65 | 33 | 92 | -8.79 | 5.95 |  |  |
| M131 Ross Hook (Joe Ross) | DATA BELUM CUKUP | 169 | 0 |  | 30% |  | 2.35 | 30 | 84 | -6.89 | 5.29 |  |  |
| M137 Livermore System | DATA BELUM CUKUP | 164 | 0 |  | 35% |  | 4.22 | 37 | 84 | -8.03 | 5.82 |  |  |
| M122 Moving Momentum (ChartSchool) | DATA BELUM CUKUP | 129 | 0 |  | 35% |  | 1.79 | 24 | 82 | -8.82 | 2.12 |  |  |
| M30 BB Free Bar + Himpitan 50/2.5 | DATA BELUM CUKUP | 143 | 0 |  | 37% |  | 3.80 | 34 | 81 | -9.43 | 7.78 |  |  |
| M151 Outside Bar Failure | DATA BELUM CUKUP | 136 | 0 |  | 27% |  | 1.93 | 26 | 79 | -4.05 | 5.31 |  |  |
| M34 Carter TTM Squeeze | DATA BELUM CUKUP | 128 | 0 |  | 34% |  | 2.38 | 30 | 78 | -7.14 | 9.66 |  |  |
| M145 Yum-Yum Continuation | DATA BELUM CUKUP | 208 | 0 |  | 25% |  | 80.48 | 356 | 73 | -13.30 | 3.69 |  |  |
| M04 BB Squeeze Breakout | DATA BELUM CUKUP | 127 | 0 |  | 36% |  | 4.96 | 32 | 72 | -9.25 | 6.84 |  |  |
| M88 O'Neil Shakeout +3 | DATA BELUM CUKUP | 94 | 0 |  | 32% |  | 5.56 | 32 | 68 | -8.09 | 6.70 |  |  |
| M26 Garis Trend Undur 3 Sentuhan + Pecahan | DATA BELUM CUKUP | 97 | 0 |  | 50% |  | 5.17 | 39 | 67 | -2.68 | 1.82 |  |  |
| M39 Radge Pecahan Bollinger 100 hari | DATA BELUM CUKUP | 216 | 0 |  | 37% |  | 9.11 | 96 | 64 | -16.62 | 3.30 |  |  |
| M149 3-Step Pullback | DATA BELUM CUKUP | 173 | 0 |  | 19% |  | 59.37 | 273 | 61 | -7.56 | 3.94 |  |  |
| M06 Minervini VCP Breakout | DATA BELUM CUKUP | 97 | 0 |  | 33% |  | 2.49 | 29 | 60 | -8.09 | 5.34 |  |  |
| M139 均线首次粘合向上发散 (MA berhimpun kali pertama, berkipas naik) | DATA BELUM CUKUP | 108 | 5 | 80% | 51% | 7.12 | 1.31 | 19 | 56 | -6.70 | -0.35 |  |  |
| M147 Improved Three-Bar Pullback | DATA BELUM CUKUP | 102 | 0 |  | 31% |  | 91.01 | 442 | 52 | -14.89 | 2.87 |  |  |
| M32 Momentum Burst | DATA BELUM CUKUP | 77 | 4 | 0% | 25% | -2.85 | 3.57 | 22 | 52 | -5.90 | 8.08 |  |  |
| M132 Ascending Scallop (Bulkowski) | DATA BELUM CUKUP | 93 | 0 |  | 42% |  | 0.98 | 29 | 50 | -9.32 | 4.93 |  |  |
| M154 HOLP (High of Low Period) | DATA BELUM CUKUP | 122 | 0 |  | 39% |  | 1.93 | 27 | 50 | -11.12 | 2.33 |  |  |
| M100 Bulkowski Segi Empat & Segi Tiga Menaik | DATA BELUM CUKUP | 71 | 0 |  | 46% |  | 1.32 | 29 | 48 | -0.47 | -1.31 |  |  |
| M118 Expansion Pivot (Cooper) | DATA BELUM CUKUP | 97 | 0 |  | 33% |  | 1.56 | 27 | 47 | -7.20 | 5.38 |  |  |
| M146 3-Bar Momentum Pattern | DATA BELUM CUKUP | 76 | 0 |  | 27% |  | 2.66 | 26 | 45 | -5.65 | 9.54 |  |  |
| M134 First Kiss After Daylight (Landry) | DATA BELUM CUKUP | 66 | 0 |  | 34% |  | 5.41 | 35 | 39 | -7.21 | 4.65 |  |  |
| M29 EMA3 + RSI75 + Stokastik | DATA BELUM CUKUP | 66 | 0 |  | 18% |  | 3.22 | 35 | 38 | -3.46 | 2.06 |  |  |
| M91 Stochastic Pop (Bernstein/Steckler) | DATA BELUM CUKUP | 43 | 9 | 33% | 42% | -1.34 | 1.63 | 18 | 37 | -4.70 | 3.64 |  |  |
| M101 Bulkowski: Tiga lembah menaik | DATA BELUM CUKUP | 55 | 0 |  | 35% |  | 3.46 | 33 | 36 | -9.16 | 7.22 |  |  |
| M09 Volumatic VIDYA Pivot Retest | DATA BELUM CUKUP | 53 | 0 |  | 23% |  | 1.85 | 30 | 35 | -7.16 | 0.77 |  |  |
| M01 Bollinger Band + RSI | DATA BELUM CUKUP | 129 | 0 |  | 67% |  | 2.22 | 22 | 33 | 11.75 | -6.84 |  |  |
| M115 Bow Tie (Landry) | DATA BELUM CUKUP | 36 | 5 | 20% | 27% | -1.51 | 1.06 | 18 | 30 | -5.01 | 13.10 |  |  |
| M117 Landry Pullback (high 2 bulan) | DATA BELUM CUKUP | 115 | 0 |  | 21% |  | 45.52 | 287 | 29 | -10.03 | 3.43 |  |  |
| M67 Rayner Teo: Ujian Ketiga pada Purata 50 | DATA BELUM CUKUP | 37 | 0 |  | 30% |  | 1.90 | 24 | 29 | -6.15 | 10.57 |  |  |
| M48 Cooper 1-2-3-4 | DATA BELUM CUKUP | 89 | 0 |  | 34% |  | 2.79 | 30 | 26 | -8.88 | 5.00 |  |  |
| M59 Anjakan Julat RSI | DATA BELUM CUKUP | 38 | 0 |  | 34% |  | 3.10 | 37 | 26 | -11.29 | 5.54 |  |  |
| M78 Alvarez Pecahan Mingguan DTAYS | DATA BELUM CUKUP | 33 | 0 |  | 32% |  | 3.17 | 40 | 25 | -9.03 | 8.25 |  |  |
| M46 Jurang Naik Boleh Beli (Buyable Gap Up) | DATA BELUM CUKUP | 34 | 0 |  | 23% |  | 2.81 | 22 | 24 | -4.60 | 8.59 |  |  |
| M140 猎豹出击 (Serangan Cheetah) | DATA BELUM CUKUP | 44 | 0 |  | 36% |  | 5.31 | 25 | 23 | -10.06 | 3.64 |  |  |
| M05 MACD Divergence + Pengesahan | DATA BELUM CUKUP | 46 | 0 |  | 35% |  | 10.85 | 108 | 20 | -10.53 | 3.94 |  |  |
| M68 Kell Base n' Break | DATA BELUM CUKUP | 58 | 0 |  | 36% |  | 1.35 | 35 | 20 | -8.45 | 2.90 |  |  |
| M141 First Thrust (Landry) | DATA BELUM CUKUP | 28 | 0 |  | 39% |  | 4.05 | 37 | 19 | -12.09 | 4.13 |  |  |
| M152 Spike & Ledge | DATA BELUM CUKUP | 61 | 0 |  | 52% |  | 3.20 | 36 | 15 | -15.24 | 0.51 |  |  |
| N201X36  | DATA BELUM CUKUP | 41 | 0 |  |  |  |  |  | 15 | -10.20 | -1.57 |  |  |
| M107 Golden Cross SMA50/200 | DATA BELUM CUKUP | 48 | 0 |  | 32% |  | 15.43 | 110 | 14 | -11.87 | 3.54 |  |  |
| M129 Wick Play | DATA BELUM CUKUP | 33 | 0 |  | 38% |  | 2.60 | 38 | 14 | -12.30 | 6.08 |  |  |
| M142 Pecahan volum dari dasar (底部放量) | DATA BELUM CUKUP | 53 | 0 |  | 41% |  | 6.85 | 44 | 14 | -12.97 | 3.56 |  |  |
| M120 Reversal New Highs | DATA BELUM CUKUP | 19 | 0 |  | 27% |  | 1.15 | 28 | 13 | -6.44 | 10.55 |  |  |
| M126 Hidden Smash Day (beli, Larry Williams) | DATA BELUM CUKUP | 22 | 0 |  | 35% |  | 5.15 | 33 | 11 | -7.73 | 3.88 |  |  |
| N202X36  | DATA BELUM CUKUP | 73 | 0 |  |  |  |  |  | 11 | -4.89 | 3.52 |  |  |
| M144 Screw Bar | DATA BELUM CUKUP | 12 | 0 |  | 41% |  | 7.68 | 23 | 10 | -3.92 | 3.48 |  |  |
| M44 Tapak Rata IBD | DATA BELUM CUKUP | 14 | 0 |  | 30% |  | 0.39 | 28 | 10 | -6.31 | 4.85 |  |  |
| M87 IBD Tapak Menaik | DATA BELUM CUKUP | 14 | 0 |  | 32% |  | 3.49 | 30 | 10 | -8.22 | 10.29 |  |  |
| M52 Radge Weekend Trend Trader | DATA BELUM CUKUP | 9 | 0 |  | 37% |  | 5.19 | 37 | 9 | -13.59 |  |  |  |
| M84 Jarak purata bergerak MAD 21/200 | DATA BELUM CUKUP | 10 | 0 |  | 37% |  | 3.71 | 26 | 8 | -9.88 | 13.52 |  |  |
| M135 3rd Watch | DATA BELUM CUKUP | 15 | 0 |  | 39% |  | 2.05 | 35 | 7 | -21.42 | 4.86 |  |  |
| M143 장대양봉 이후 눌림목 / 5일선 매매 (Undur ke MA5 selepas lilin naik panjang) | DATA BELUM CUKUP | 28 | 1 | 0% | 52% | -16.18 | 0.83 | 18 | 7 | -5.53 | 0.62 |  |  |
| M41 FW Penyatuan Mingguan | DATA BELUM CUKUP | 25 | 0 |  | 36% |  | 15.03 | 117 | 7 | -13.64 | 5.41 |  |  |
| M21 Marius 3 Persediaan (Pecahan+Jurang+Kesinambungan) | DATA BELUM CUKUP | 8 | 6 | 33% | 26% | -2.29 | 2.57 | 8 | 6 | -2.80 | 2.52 |  |  |
| M96 Momo India: Ranking Sharpe 3/6/12 bulan | DATA BELUM CUKUP | 6 | 0 |  | 43% |  | 12.18 | 54 | 6 | -13.20 |  |  |  |
| M130 多方炮 (dua lilin hijau mengapit satu merah) | DATA BELUM CUKUP | 12 | 0 |  | 25% |  | 92.22 | 261 | 5 | -15.15 | 7.01 |  |  |
| N203X36  | DATA BELUM CUKUP | 20 | 0 |  |  |  |  |  | 5 | -21.03 | -3.75 |  |  |
| M121 High 2 bull flag (Brooks) | DATA BELUM CUKUP | 11 | 0 |  | 47% |  | 2.47 | 49 | 4 | -16.77 | 0.60 |  |  |
| M157 Consolidation Pivot Breakout (versi angka) | DATA BELUM CUKUP | 9 | 0 |  | 14% |  | 32.05 | 179 | 3 | -8.78 | 2.67 |  |  |
| M07 Qullamaggie Breakout | DATA BELUM CUKUP | 2 | 2 | 0% | 20% | -3.04 | 1.05 | 8 | 2 | -3.04 |  |  |  |
| M45 High 52 Minggu (George & Hwang) | DATA BELUM CUKUP | 8 | 0 |  | 32% |  | 12.81 | 61 | 2 | -9.78 | 6.24 |  |  |
| M64 O'Neil Tiga Minggu Ketat | DATA BELUM CUKUP | 3 | 0 |  | 34% |  | 1.68 | 31 | 2 | -3.27 | 21.11 |  |  |
| N204X36  | DATA BELUM CUKUP | 11 | 0 |  |  |  |  |  | 2 | -7.04 | -1.27 |  |  |
| M37 Weinstein Peringkat 2 | DATA BELUM CUKUP | 7 | 0 |  | 41% |  | 5.49 | 42 | 1 | -5.87 | -0.33 |  |  |
| M38 Darvas Kotak | DATA BELUM CUKUP | 26 | 0 |  | 49% |  | 18.79 | 210 | 1 | -9.28 | -3.01 |  |  |
| M51 O'Neil Cawan & Pemegang | DATA BELUM CUKUP | 3 | 0 |  | 39% |  | 3.12 | 35 | 1 | -7.27 | 4.57 |  |  |
| M104 High Tight Flag / Power Play | DATA BELUM CUKUP | 1 | 0 |  | 35% |  | 5.62 | 33 | 0 |  | 25.96 |  |  |
| M138 直升机空中加油 (Helikopter isi minyak di udara) | DATA BELUM CUKUP | 4 | 0 |  | 45% |  | 4.60 | 46 | 0 |  | -2.68 |  |  |
| M94 Pecutan Momentum (Chen, Yu & Wang) | DATA BELUM CUKUP | 12 | 0 |  | 63% |  | 24.04 | 121 | 0 |  | -18.42 |  |  |
| M73 ADX(5) > 40 + Julat Terkecil 6 Hari | SELARI | 334 | 245 | 62% | 63% | -0.64 | 0.18 | 5 | 286 | -0.04 | -2.75 | -0.6 | -2.0 |
| M18 EMA9/21 Pullback | SELARI | 295 | 200 | 25% | 26% | -0.15 | 0.40 | 7 | 251 | -1.22 | 6.03 | -0.2 | -1.1 |
| M13 Garis Trend Action/Safety Line | SELARI | 315 | 172 | 33% | 34% | 0.08 | 0.97 | 11 | 250 | -3.25 | 5.08 | -0.4 | -1.3 |
| M15 Break & Retest + Henti ATR | SELARI | 279 | 157 | 41% | 33% | 0.99 | 1.08 | 12 | 238 | -2.21 | 10.19 | 2.0 | -0.1 |
| M70 Pecahan Hari Dalam | SELARI | 272 | 163 | 12% | 11% | 0.22 | 0.84 | 10 | 226 | -1.83 | 9.17 | 0.1 | -1.0 |
| M35 Pocket Pivot Morales & Kacher | SELARI | 261 | 184 | 28% | 28% | -0.06 | 0.29 | 9 | 219 | -0.84 | 4.52 | -0.1 | -0.7 |
| M161 EMA 10/21 + Supertrend (10,3) | SELARI | 283 | 20 | 25% | 35% | -4.60 | 1.43 | 18 | 180 | -6.65 | 5.14 | -0.9 | -1.4 |
| M66 IBD Undur Pertama ke Purata 50 Hari | SELARI | 252 | 46 | 33% | 28% | 0.78 | 1.71 | 19 | 172 | -4.77 | 5.35 | 0.7 | -0.7 |
| N74X16  | SELARI | 190 | 50 | 30% |  | -2.31 |  |  | 160 | -3.08 | 2.72 |  |  |
| M25 VWAP Wave (proksi harian) | SELARI | 184 | 133 | 31% | 30% | 0.60 | 0.42 | 10 | 154 | -0.61 | 3.73 | 0.3 | 0.2 |
| N28X16  | SELARI | 202 | 55 | 24% |  | -2.82 |  |  | 153 | -2.81 | 2.21 |  |  |
| M99 Three Line Break | SELARI | 206 | 73 | 42% | 40% | 1.40 | 1.17 | 16 | 152 | -4.41 | 3.78 | 0.5 | 0.1 |
| N28X36  | SELARI | 207 | 55 | 31% |  | -3.57 |  |  | 148 | -3.07 | 1.61 |  |  |
| M02 MACD + SMA200 | SELARI | 171 | 84 | 33% | 44% | -0.00 | 0.66 | 14 | 146 | -3.95 | -0.43 | -1.9 | -0.5 |
| N08X16  | SELARI | 213 | 52 | 19% |  | -4.26 |  |  | 141 | -3.66 | 2.12 |  |  |
| N76X16  | SELARI | 190 | 50 | 18% |  | -3.33 |  |  | 129 | -3.25 | 2.35 |  |  |
| N08X36  | SELARI | 211 | 52 | 23% |  | -4.95 |  |  | 128 | -4.36 | 2.20 |  |  |
| M106 DMI Wilder | SELARI | 160 | 72 | 33% | 32% | -0.75 | 1.01 | 12 | 121 | -3.29 | 5.64 | 0.2 | -1.6 |
| N41X16  | SELARI | 206 | 53 | 25% |  | -3.27 |  |  | 117 | -3.94 | 2.61 |  |  |
| N113X16  | SELARI | 174 | 45 | 31% |  | -3.28 |  |  | 112 | -3.08 | 1.42 |  |  |
| N41X36  | SELARI | 207 | 53 | 28% |  | -3.88 |  |  | 110 | -4.72 | 2.90 |  |  |
| N56X16  | SELARI | 203 | 55 | 31% |  | -2.64 |  |  | 106 | -4.96 | 2.38 |  |  |
| N113X36  | SELARI | 174 | 45 | 36% |  | -2.95 |  |  | 105 | -2.83 | 1.58 |  |  |
| N27X16  | SELARI | 190 | 50 | 20% |  | -2.63 |  |  | 105 | -3.58 | 1.86 |  |  |
| N29X16  | SELARI | 200 | 53 | 26% |  | -3.88 |  |  | 105 | -6.10 | 1.83 |  |  |
| N42X16  | SELARI | 168 | 53 | 43% |  | -1.35 |  |  | 98 | -3.53 | 1.27 |  |  |
| N42X36  | SELARI | 165 | 53 | 43% |  | -1.24 |  |  | 98 | -3.68 | 2.54 |  |  |
| M11 NR7 Breakout + Volume | SELARI | 139 | 22 | 45% | 36% | 0.73 | 2.86 | 20 | 97 | -2.50 | 4.69 | 0.9 | -0.8 |
| M160 Measured Move Up | SELARI | 139 | 71 | 31% | 32% | -1.20 | 0.44 | 8 | 93 | -3.10 | 4.17 | -0.2 | -2.0 |
| N45X16  | SELARI | 193 | 51 | 33% |  | -1.86 |  |  | 92 | -4.61 | 2.06 |  |  |
| N48X36  | SELARI | 154 | 41 | 37% |  | -2.81 |  |  | 90 | -1.26 | 1.19 |  |  |
| N09X36  | SELARI | 175 | 43 | 26% |  | -3.96 |  |  | 87 | -5.42 | 1.63 |  |  |
| N36X16  | SELARI | 188 | 50 | 22% |  | -4.11 |  |  | 87 | -6.02 | 1.23 |  |  |
| N36X36  | SELARI | 187 | 50 | 28% |  | -4.30 |  |  | 86 | -6.55 | 1.99 |  |  |
| N76X36  | SELARI | 190 | 50 | 24% |  | -4.37 |  |  | 86 | -6.18 | 2.57 |  |  |
| N29X36  | SELARI | 200 | 53 | 25% |  | -4.74 |  |  | 80 | -8.29 | 1.75 |  |  |
| N54X36  | SELARI | 198 | 51 | 27% |  | -4.04 |  |  | 80 | -8.54 | 2.44 |  |  |
| N43X36  | SELARI | 178 | 44 | 27% |  | -4.44 |  |  | 79 | -6.52 | 2.07 |  |  |
| N24X16  | SELARI | 200 | 56 | 29% |  | -2.71 |  |  | 78 | -7.52 | 1.85 |  |  |
| M150 Trend Bar Failure (Brooks) | SELARI | 98 | 46 | 35% | 37% | -0.37 | 0.54 | 13 | 76 | -2.28 | 3.18 | -0.3 | -0.9 |
| N56X36  | SELARI | 203 | 55 | 35% |  | -3.33 |  |  | 76 | -6.97 | 2.12 |  |  |
| N54X16  | SELARI | 199 | 51 | 27% |  | -2.94 |  |  | 74 | -8.80 | 1.80 |  |  |
| N24X36  | SELARI | 200 | 56 | 32% |  | -3.34 |  |  | 73 | -6.65 | 1.96 |  |  |
| N07X16  | SELARI | 149 | 50 | 22% |  | -5.25 |  |  | 72 | -7.72 | 1.36 |  |  |
| N53X16  | SELARI | 198 | 55 | 35% |  | -2.49 |  |  | 71 | -7.19 | 1.86 |  |  |
| N27X36  | SELARI | 190 | 50 | 24% |  | -3.85 |  |  | 69 | -7.06 | 1.96 |  |  |
| N47X16  | SELARI | 175 | 39 | 18% |  | -6.25 |  |  | 69 | -7.21 | 1.45 |  |  |
| N07X36  | SELARI | 148 | 50 | 24% |  | -5.40 |  |  | 67 | -8.68 | 1.05 |  |  |
| N25X16  | SELARI | 193 | 53 | 36% |  | -3.22 |  |  | 66 | -7.67 | 2.19 |  |  |
| N40X16  | SELARI | 136 | 43 | 35% |  | -2.65 |  |  | 64 | -5.54 | 3.13 |  |  |
| M27 Price Action 4 Tiang | SELARI | 65 | 65 | 31% | 35% | -0.08 | 0.36 | 7 | 63 | -1.05 | 30.38 | -0.8 | -0.4 |
| N42X17  | SELARI | 167 | 53 | 43% |  | -1.05 |  |  | 58 | -0.39 | -2.16 |  |  |
| N45X36  | SELARI | 192 | 51 | 35% |  | -3.11 |  |  | 58 | -7.80 | 1.90 |  |  |
| N22X16  | SELARI | 135 | 52 | 46% |  | -1.71 |  |  | 57 | -10.16 | 0.89 |  |  |
| N28X14  | SELARI | 202 | 55 | 25% |  | -7.39 |  |  | 54 | -0.39 | -4.32 |  |  |
| N47X36  | SELARI | 175 | 39 | 18% |  | -6.76 |  |  | 53 | -8.77 | 1.08 |  |  |
| N53X36  | SELARI | 198 | 55 | 38% |  | -3.09 |  |  | 53 | -8.26 | 1.57 |  |  |
| N56X17  | SELARI | 202 | 55 | 38% |  | -3.18 |  |  | 53 | -2.88 | -0.91 |  |  |
| N33X16  | SELARI | 142 | 50 | 44% |  | -2.82 |  |  | 52 | -11.01 | 1.52 |  |  |
| N68X16  | SELARI | 130 | 30 | 50% |  | -0.76 |  |  | 52 | -5.76 | 1.69 |  |  |
| N75X17  | SELARI | 189 | 49 | 18% |  | -13.32 |  |  | 52 | -0.11 | -6.83 |  |  |
| N33X36  | SELARI | 141 | 50 | 46% |  | -2.44 |  |  | 48 | -10.56 | 1.78 |  |  |
| N22X36  | SELARI | 135 | 52 | 46% |  | -1.02 |  |  | 47 | -10.56 | 0.76 |  |  |
| N36X14  | SELARI | 187 | 50 | 24% |  | -6.27 |  |  | 47 | -1.68 | -3.61 |  |  |
| M133 Bull Hook (Crabel) | SELARI | 56 | 37 | 46% | 41% | 0.74 | 0.68 | 10 | 46 | -1.20 | 2.83 | 0.6 | 0.1 |
| N42X14  | SELARI | 163 | 53 | 51% |  | -0.50 |  |  | 46 | 1.52 | -3.29 |  |  |
| N25X36  | SELARI | 193 | 53 | 38% |  | -3.87 |  |  | 45 | -9.84 | 1.59 |  |  |
| N38X36  | SELARI | 90 | 41 | 27% |  | -3.68 |  |  | 45 | -7.56 | 2.52 |  |  |
| N57X16  | SELARI | 89 | 46 | 33% |  | -4.11 |  |  | 45 | -9.81 | 0.47 |  |  |
| N24X17  | SELARI | 200 | 56 | 36% |  | -3.87 |  |  | 44 | -3.14 | -1.15 |  |  |
| N68X36  | SELARI | 130 | 30 | 57% |  | 0.07 |  |  | 43 | -7.14 | 1.92 |  |  |
| N22X14  | SELARI | 135 | 52 | 40% |  | -1.58 |  |  | 41 | -4.17 | -3.99 |  |  |
| N33X14  | SELARI | 142 | 50 | 40% |  | -2.47 |  |  | 40 | -4.63 | -2.37 |  |  |
| N40X36  | SELARI | 123 | 42 | 33% |  | -3.13 |  |  | 40 | -10.05 | 3.01 |  |  |
| N37X16  | SELARI | 71 | 34 | 41% |  | -1.37 |  |  | 36 | -7.26 | 2.52 |  |  |
| N37X36  | SELARI | 71 | 34 | 44% |  | -0.76 |  |  | 31 | -7.55 | 2.11 |  |  |
| N124X36  | SELARI | 57 | 29 | 41% |  | -1.47 |  |  | 29 | -7.19 | 3.16 |  |  |
| N37X17  | SELARI | 71 | 34 | 44% |  | -0.08 |  |  | 27 | -0.47 | -3.01 |  |  |
| N57X36  | SELARI | 89 | 46 | 37% |  | -3.66 |  |  | 25 | -12.48 | -1.20 |  |  |
| N25X17  | SELARI | 193 | 53 | 38% |  | -4.00 |  |  | 24 | -4.04 | -0.85 |  |  |
| N31X36  | SELARI | 130 | 50 | 40% |  | -3.15 |  |  | 24 | -15.57 | 0.60 |  |  |
| N80X36  | SELARI | 93 | 48 | 40% |  | -1.51 |  |  | 23 | -14.64 | 1.22 |  |  |
| N35X36  | SELARI | 104 | 50 | 42% |  | -1.19 |  |  | 22 | -14.77 | 1.24 |  |  |
| N37X14  | SELARI | 71 | 34 | 41% |  | -2.31 |  |  | 20 | -1.62 | -4.78 |  |  |
| N64X16  | SELARI | 53 | 32 | 50% |  | 0.32 |  |  | 19 | -8.49 | 3.42 |  |  |
| N75X14  | SELARI | 189 | 49 | 18% |  | -12.76 |  |  | 18 | 10.00 | -6.92 |  |  |
| N39X36  | SELARI | 49 | 25 | 20% |  | -8.38 |  |  | 16 | -15.03 | 0.67 |  |  |
| N28X17  | SELARI | 202 | 55 | 25% |  | -7.80 |  |  | 15 | -2.95 | -3.13 |  |  |
| N51X36  | SELARI | 27 | 13 | 23% |  | -2.17 |  |  | 15 | -7.84 | 2.87 |  |  |
| N53X17  | SELARI | 198 | 55 | 38% |  | -3.65 |  |  | 15 | -5.28 | -1.01 |  |  |
| N64X17  | SELARI | 53 | 32 | 50% |  | 1.01 |  |  | 15 | 1.66 | -1.37 |  |  |
| N64X36  | SELARI | 53 | 32 | 53% |  | 1.04 |  |  | 15 | -8.77 | 2.61 |  |  |
| N50X14  | SELARI | 51 | 19 | 42% |  | -5.57 |  |  | 14 | -0.98 | -2.35 |  |  |
| N64X14  | SELARI | 53 | 32 | 50% |  | -0.43 |  |  | 13 | -1.22 | -1.71 |  |  |
| N51X16  | SELARI | 26 | 13 | 23% |  | -2.84 |  |  | 11 | -8.80 | 2.01 |  |  |
| N50X17  | SELARI | 51 | 19 | 42% |  | -6.60 |  |  | 9 | -1.91 | -2.40 |  |  |
| N66X36  | SELARI | 59 | 34 | 53% |  | -0.22 |  |  | 9 | -20.96 | 1.36 |  |  |
| N65X14  | SELARI | 32 | 21 | 43% |  | 1.25 |  |  | 8 | -5.90 | -1.02 |  |  |
| N06X36  | SELARI | 35 | 11 | 55% |  | 0.11 |  |  | 6 | -7.59 | 2.47 |  |  |
| N119X13  | SELARI | 188 | 50 | 8% |  | -14.07 |  |  | 5 | 4.27 | -6.02 |  |  |
| N65X36  | SELARI | 32 | 21 | 48% |  | 1.48 |  |  | 5 | -22.78 | 1.92 |  |  |
| N19X13  | SELARI | 123 | 53 | 19% |  | -4.72 |  |  | 1 | 52.25 | -3.97 |  |  |
| N119X15  | SELARI | 187 | 50 | 8% |  | -14.11 |  |  | 0 |  | -5.89 |  |  |
| N124X15  | SELARI | 56 | 29 | 41% |  | -3.15 |  |  | 0 |  | -3.56 |  |  |
| N16X13  | SELARI | 182 | 49 | 10% |  | -13.56 |  |  | 0 |  | -5.01 |  |  |
| N16X15  | SELARI | 182 | 49 | 10% |  | -13.56 |  |  | 0 |  | -5.01 |  |  |
| N42X15  | SELARI | 160 | 53 | 42% |  | -3.41 |  |  | 0 |  | -2.92 |  |  |
| N55X13  | SELARI | 153 | 43 | 23% |  | -7.87 |  |  | 0 |  | -1.88 |  |  |
| N73X13  | SELARI | 174 | 49 | 16% |  | -9.94 |  |  | 0 |  | -4.83 |  |  |
| N75X13  | SELARI | 189 | 49 | 10% |  | -15.06 |  |  | 0 |  | -5.94 |  |  |
| N75X15  | SELARI | 189 | 49 | 10% |  | -15.06 |  |  | 0 |  | -5.94 |  |  |

Nota: lajur "Tutup (awal)" dan "Purata tutup" ialah maklumat sahaja (berat sebelah ke arah kena henti), tidak dipakai dalam ujian.
