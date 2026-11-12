# Semua kaedah M dan N, satu per satu (data langsung; maklumat, BUKAN keputusan)

> **Status keputusan (kad skor, harga 2026-11-11):** TERBUKTI 0 · CALON 0 · BELUM CUKUP 223 · GAGAL 0 · NEGATIF 0. Rejim QQQ OFF sejak 2026-10-16. Hanya **TERBUKTI** layak untuk wang sebenar (`laporan/KAD_SKOR.md`); nombor dalam laporan ini BUKAN keputusan dan tidak boleh dibaca sebagai pangkat untuk wang sebenar.

Dijana `kajian/analisa_mn/analisa.py` atas kad skor harga 2026-11-11. Jangan ubah manual. Penjelasan lajur dan bacaan: `kajian/KAJIAN_M_N_SATU_PER_SATU.md`. Jadual penuh (semua lajur, teks masuk / pegang / keluar): `hasil/kaedah.csv`.

Lajur: **Jangkaan** = purata semua posisi termasuk yang masih terbuka (ditanda ke pasaran), ikut keluar kaedah. **r3/r5/r10** = pulangan purata selepas 3/5/10 sesi tanpa mengira peraturan keluar. **Lift 5** = r5 tolak saham lain yang Lejar beli pada hari dan tahap turun-naik sama. **A/B** = lift 5 pada dua separuh hari beli. **L2** = jangkaan jika keluar ikut Chandelier. **Backtest** = purata setiap dagangan (Mxx set 431; Nxx tingkap tahan).

## Kaedah Mxx

| Kaedah | Kelas | Posisi/tutup | Hari beli | Jangkaan % | tanpa5 % | r3 | r5 | r10 | Lift 5 | A / B | L2 % | Hari-0 % | Backtest % | Sebab |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `M142` Pecahan volum dari dasar (底部放量) | PANTAU | 45/5 | 14 | +3.31 | +1.88 | +1.94 | +1.57 | +0.52 | +4.10 | +4.86 / +3.54 | +3.29 | 0 | +6.85 | lulus semua tapis (BUKAN terbukti) |
| `M133` Bull Hook (Crabel) | PANTAU | 49/23 | 13 | +1.80 | +0.49 | +2.29 | +1.46 | +5.94 | +1.78 | +1.33 / +2.88 | +2.67 | 2 | +0.68 | lulus semua tapis (BUKAN terbukti) |
| `M146` 3-Bar Momentum Pattern | PANTAU | 77/30 | 17 | +1.70 | +0.68 | +1.77 | +2.09 | +1.69 | +2.12 | +3.09 / +0.40 | +2.60 | 5 | +2.66 | lulus semua tapis (BUKAN terbukti) |
| `M80` Radge Saluran Purata Bergerak (MAC) | PANTAU | 273/56 | 19 | +1.34 | +0.07 | +0.28 | +0.47 | +3.21 | +1.00 | +1.10 / +0.83 | +1.30 | 0 | +8.91 | lulus semua tapis (BUKAN terbukti) |
| `M01` Bollinger Band + RSI | CAMPUR | 112/20 | 19 | +3.05 | +1.85 | +1.96 | +1.96 | -3.40 | +2.95 | +1.52 / +3.92 | +2.28 | 0 | +2.22 | lift 10 sesi <= 0 |
| `M33` Supertrend + SMA10 | CAMPUR | 218/40 | 19 | +1.88 | +0.56 | +0.18 | +1.19 | +3.31 | +1.68 | +2.73 / -0.02 | +1.97 | 0 | +1.65 | lift tidak positif pada kedua-dua separuh hari beli |
| `M93` Bollinger Kaedah II: %b + MFI | CAMPUR | 258/75 | 19 | +1.57 | -0.18 | +0.47 | +0.91 | +2.83 | +0.91 | +0.77 / +1.09 | +1.36 | 2 | +8.20 | tanpa5 <= 0 |
| `M117` Landry Pullback (high 2 bulan) | CAMPUR | 132/17 | 16 | +1.49 | -0.05 | +0.70 | +1.57 | +1.84 | +2.09 | +1.75 / +2.54 | +1.57 | 1 | +45.52 | tanpa5 <= 0 |
| `M158` Doubly Adaptive Profit Targets | CAMPUR | 349/127 | 19 | +1.24 | -0.22 | +1.74 | +1.94 | +2.03 | +2.27 | +0.57 / +3.54 | +1.25 | 1 | +2.94 | tanpa5 <= 0 |
| `M118` Expansion Pivot (Cooper) | CAMPUR | 84/20 | 19 | +1.13 | -0.29 | +0.49 | -0.11 | -0.23 | +0.49 | +0.48 / +0.49 | +0.94 | 1 | +1.56 | tanpa5 <= 0 |
| `M15` Break & Retest + Henti ATR | CAMPUR | 291/155 | 19 | +1.04 | -0.25 | +0.35 | +1.65 | +2.92 | +1.95 | +1.41 / +2.69 | +1.73 | 2 | +1.08 | tanpa5 <= 0 |
| `M105` Supertrend tulen | CAMPUR | 355/97 | 19 | +0.90 | -0.41 | +0.00 | +0.47 | +1.73 | +0.94 | +2.00 / -0.47 | +0.95 | 1 | +2.44 | tanpa5 <= 0; lift tidak positif pada kedua-dua separuh hari beli |
| `M111` Sistem Volatiliti Wilder | CAMPUR | 253/78 | 19 | +0.83 | -0.58 | -0.19 | +0.43 | +0.53 | +0.87 | +1.32 / +0.24 | +0.60 | 2 | +2.39 | tanpa5 <= 0 |
| `M30` BB Free Bar + Himpitan 50/2.5 | CAMPUR | 226/70 | 18 | +0.70 | -0.59 | -0.04 | +0.79 | +1.99 | +1.21 | +1.80 / +0.31 | +0.79 | 0 | +3.80 | tanpa5 <= 0 |
| `M48` Cooper 1-2-3-4 | CAMPUR | 52/16 | 16 | +0.62 | -1.86 | -1.89 | -0.97 | -5.12 | +0.38 | -1.58 / +2.43 | -0.43 | 4 | +2.79 | tanpa5 <= 0; lift 10 sesi <= 0; lift tidak positif pada kedua-dua separuh hari beli |
| `M150` Trend Bar Failure (Brooks) | CAMPUR | 99/39 | 18 | +0.56 | -0.40 | +0.57 | +1.34 | +2.07 | +1.33 | +1.48 / +1.21 | -0.05 | 0 | +0.54 | tanpa5 <= 0 |
| `M10` EMA3 + CCI + MACD | CAMPUR | 113/50 | 19 | +0.55 | -1.23 | +0.61 | +0.92 | +0.47 | +1.13 | +1.10 / +1.17 | +0.55 | 8 | +4.70 | tanpa5 <= 0 |
| `M100` Bulkowski Segi Empat & Segi Tiga Menai | CAMPUR | 58/40 | 14 | +0.52 | -0.10 | +0.56 | +0.98 | -0.36 | +1.31 | +3.50 / -1.50 | +0.86 | 0 | +1.32 | tanpa5 <= 0; lift 10 sesi <= 0; lift tidak positif pada kedua-dua separuh hari beli |
| `M92` CCI-50 | CAMPUR | 527/313 | 19 | +0.50 | -1.04 | +0.12 | +0.23 | +0.47 | +0.52 | +0.47 / +0.60 | +0.35 | 3 | +1.17 | tanpa5 <= 0 |
| `M25` VWAP Wave (proksi harian) | CAMPUR | 173/87 | 17 | +0.48 | -0.64 | +0.60 | +0.88 | +1.32 | +1.25 | +1.41 / +1.04 | +0.28 | 16 | +0.42 | tanpa5 <= 0 |
| `M31` Band Walk (BB 20/2) | CAMPUR | 392/84 | 19 | +0.46 | -0.79 | +0.26 | +0.84 | +1.28 | +0.92 | +1.54 / +0.00 | +0.42 | 0 | +3.30 | tanpa5 <= 0 |
| `M145` Yum-Yum Continuation | CAMPUR | 300/62 | 19 | +0.42 | -0.85 | +0.74 | +0.30 | +1.05 | +0.45 | +0.45 / +0.45 | +0.28 | 0 | +80.48 | tanpa5 <= 0 |
| `M155` Market Cycle Strategy | CAMPUR | 654/228 | 19 | +0.31 | -1.32 | +0.02 | +0.20 | +0.74 | +0.07 | -0.01 / +0.17 | +0.45 | 2 | +1.56 | tanpa5 <= 0; lift tidak positif pada kedua-dua separuh hari beli |
| `M18` EMA9/21 Pullback | CAMPUR | 348/227 | 19 | +0.30 | -0.79 | +0.49 | +1.28 | +1.73 | +1.74 | +2.03 / +1.43 | +0.24 | 20 | +0.40 | tanpa5 <= 0 |
| `M153` Range Leader | CAMPUR | 1242/1026 | 19 | +0.28 | -0.73 | -0.33 | -0.17 | -0.21 | +0.81 | +1.23 / -0.02 | +0.14 | 1 | +0.18 | tanpa5 <= 0; lift tidak positif pada kedua-dua separuh hari beli |
| `M124` 'Last' Stochastic Technique (ChartScho | CAMPUR | 380/170 | 19 | +0.26 | -1.05 | -0.72 | -0.73 | +0.42 | -0.03 | +0.28 / -0.40 | +0.23 | 4 | +1.74 | tanpa5 <= 0; lift 5 sesi <= 0; lift tidak positif pada kedua-dua separuh hari beli |
| `M32` Momentum Burst | CAMPUR | 53/32 | 12 | +0.20 | -2.30 | +0.07 | +1.59 | -0.70 | +2.78 | +4.72 / -3.53 | -2.09 | 17 | +3.57 | tanpa5 <= 0; lift 10 sesi <= 0; lift tidak positif pada kedua-dua separuh hari beli |
| `M151` Outside Bar Failure | CAMPUR | 96/48 | 18 | +0.19 | -1.20 | +0.01 | -0.75 | -1.05 | -0.24 | +0.08 / -0.95 | -0.67 | 14 | +1.93 | tanpa5 <= 0; lift 5 sesi <= 0; lift 10 sesi <= 0; lift tidak positif pada kedua-dua separuh hari beli |
| `M106` DMI Wilder | CAMPUR | 116/59 | 17 | +0.18 | -0.92 | +0.64 | +1.35 | +0.15 | +1.84 | +2.00 / +1.62 | +0.16 | 0 | +1.01 | tanpa5 <= 0 |
| `M91` Stochastic Pop (Bernstein/Steckler) | CAMPUR | 37/16 | 14 | +0.18 | -2.02 | -0.38 | +1.05 | +2.69 | +1.65 | +0.81 / +3.58 | +0.07 | 3 | +1.63 | tanpa5 <= 0 |
| `M73` ADX(5) > 40 + Julat Terkecil 6 Hari | CAMPUR | 877/699 | 19 | +0.15 | -0.42 | -0.11 | -0.90 | -1.51 | -0.91 | -0.60 / -1.38 | -0.56 | 0 | +0.18 | tanpa5 <= 0; lift 5 sesi <= 0; lift 10 sesi <= 0; lift tidak positif pada kedua-dua separuh hari beli |
| `M05` MACD Divergence + Pengesahan | CAMPUR | 40/12 | 14 | +0.12 | -1.52 | -0.74 | -1.74 | -2.40 | -1.19 | -1.17 / -1.22 | -0.36 | 0 | +10.85 | tanpa5 <= 0; lift 5 sesi <= 0; lift 10 sesi <= 0; lift tidak positif pada kedua-dua separuh hari beli |
| `M89` Chande 65sma-3cc | CAMPUR | 165/80 | 19 | +0.11 | -1.49 | -0.78 | -0.35 | -1.48 | +0.22 | -0.56 / +1.08 | -0.76 | 10 | +1.83 | tanpa5 <= 0; lift 10 sesi <= 0; lift tidak positif pada kedua-dua separuh hari beli |
| `M116` 2/20 EMA Breakout (Landry) | CAMPUR | 539/353 | 19 | +0.06 | -0.96 | -0.22 | +0.46 | +0.36 | +0.84 | +1.40 / -0.08 | -0.20 | 1 | +0.40 | tanpa5 <= 0; lift 10 sesi <= 0; lift tidak positif pada kedua-dua separuh hari beli |
| `M03` BB Break + Divergence RSI | CAMPUR | 395/311 | 19 | -0.06 | -0.88 | -0.23 | -0.19 | +0.19 | +0.29 | +0.47 / -0.03 | +0.95 | 3 | +0.58 | jangkaan <= 0; tanpa5 <= 0; lift tidak positif pada kedua-dua separuh hari beli |
| `M13` Garis Trend Action/Safety Line | CAMPUR | 711/426 | 19 | -0.08 | -1.49 | -0.60 | -0.45 | -0.34 | +0.14 | +0.45 / -0.30 | -0.06 | 13 | +0.97 | jangkaan <= 0; tanpa5 <= 0; lift tidak positif pada kedua-dua separuh hari beli |
| `M134` First Kiss After Daylight (Landry) | CAMPUR | 53/16 | 15 | -0.09 | -1.37 | +0.12 | +1.45 | -1.06 | +2.04 | +2.25 / +1.72 | -0.82 | 6 | +5.41 | jangkaan <= 0; tanpa5 <= 0; lift 10 sesi <= 0 |
| `M08` SMA20 + SMA200 | CAMPUR | 181/92 | 17 | -0.10 | -1.45 | -0.75 | -0.38 | -1.40 | +0.40 | +0.74 / -0.24 | -1.05 | 8 | +1.07 | jangkaan <= 0; tanpa5 <= 0; lift 10 sesi <= 0; lift tidak positif pada kedua-dua separuh hari beli |
| `M136` Short/Intermediate-term Low (Larry Wil | CAMPUR | 725/259 | 19 | -0.10 | -1.55 | -0.82 | -0.15 | +0.02 | +0.16 | +0.61 / -0.57 | +0.10 | 4 | +112.90 | jangkaan <= 0; tanpa5 <= 0; lift tidak positif pada kedua-dua separuh hari beli |
| `M161` EMA 10/21 + Supertrend (10,3) | CAMPUR | 458/210 | 19 | -0.12 | -1.57 | +0.42 | +1.31 | +0.41 | +1.79 | +2.19 / +1.25 | -0.25 | 0 | +1.43 | jangkaan <= 0; tanpa5 <= 0 |
| `M14` Walking with the Whales | CAMPUR | 882/587 | 19 | -0.15 | -1.43 | +0.27 | +0.07 | +0.51 | +0.35 | +0.58 / +0.03 | -1.04 | 20 | +1.52 | jangkaan <= 0; tanpa5 <= 0 |
| `M159` Heikin-Ashi Trend | CAMPUR | 1570/1209 | 19 | -0.15 | -1.15 | -0.55 | -0.46 | -1.26 | +0.46 | +0.56 / +0.27 | -0.48 | 1 | +0.17 | jangkaan <= 0; tanpa5 <= 0; lift 10 sesi <= 0 |
| `M160` Measured Move Up | CAMPUR | 107/47 | 17 | -0.15 | -1.30 | -0.38 | +0.57 | -0.73 | +1.24 | +1.19 / +1.33 | -1.39 | 9 | +0.44 | jangkaan <= 0; tanpa5 <= 0 |
| `M137` Livermore System | CAMPUR | 166/57 | 19 | -0.16 | -1.59 | +0.45 | +0.64 | +0.27 | +0.97 | +0.86 / +1.14 | +0.05 | 1 | +4.22 | jangkaan <= 0; tanpa5 <= 0 |
| `M26` Garis Trend Undur 3 Sentuhan + Pecahan | CAMPUR | 69/43 | 16 | -0.21 | -1.24 | -0.81 | +0.13 | -4.15 | +0.77 | +1.00 / +0.35 | -2.37 | 9 | +5.17 | jangkaan <= 0; tanpa5 <= 0; lift 10 sesi <= 0 |
| `M131` Ross Hook (Joe Ross) | CAMPUR | 257/106 | 19 | -0.23 | -1.27 | +0.11 | +0.20 | +1.01 | +0.40 | +0.95 / -0.47 | +0.02 | 5 | +2.35 | jangkaan <= 0; tanpa5 <= 0; lift tidak positif pada kedua-dua separuh hari beli |
| `M88` O'Neil Shakeout +3 | CAMPUR | 70/29 | 15 | -0.23 | -1.71 | -0.98 | -2.07 | -0.74 | +0.16 | +0.93 / -0.81 | +0.44 | 11 | +5.56 | jangkaan <= 0; tanpa5 <= 0; lift tidak positif pada kedua-dua separuh hari beli |
| `M34` Carter TTM Squeeze | CAMPUR | 102/46 | 18 | -0.24 | -1.94 | +0.22 | +0.29 | -1.07 | +0.42 | +0.54 / +0.30 | -1.09 | 0 | +2.38 | jangkaan <= 0; tanpa5 <= 0; lift 10 sesi <= 0 |
| `M50` Elder Triple Screen | CAMPUR | 558/324 | 19 | -0.34 | -1.44 | -0.25 | +0.36 | +0.50 | +0.77 | +1.12 / +0.32 | -0.77 | 15 | +1.80 | jangkaan <= 0; tanpa5 <= 0 |
| `M128` Inventory Retracement Bar (IRB, Rob Ho | CAMPUR | 151/74 | 19 | -0.35 | -1.50 | -0.26 | +0.44 | +0.29 | +0.68 | +0.84 / +0.52 | -1.02 | 1 | +0.55 | jangkaan <= 0; tanpa5 <= 0 |
| `M149` 3-Step Pullback | CAMPUR | 201/53 | 17 | -0.36 | -1.61 | -0.70 | -0.54 | -1.18 | +0.31 | +1.11 / -0.64 | -0.74 | 2 | +59.37 | jangkaan <= 0; tanpa5 <= 0; lift 10 sesi <= 0; lift tidak positif pada kedua-dua separuh hari beli |
| `M04` BB Squeeze Breakout | CAMPUR | 151/52 | 18 | -0.45 | -1.76 | -0.40 | +0.07 | -0.44 | +1.30 | +1.36 / +1.16 | -0.34 | 1 | +4.96 | jangkaan <= 0; tanpa5 <= 0 |
| `M36` Turtle 55/20 | CAMPUR | 330/152 | 19 | -0.57 | -1.76 | +0.42 | -0.01 | +0.01 | +0.20 | +0.73 / -0.52 | -0.67 | 4 | +2.65 | jangkaan <= 0; tanpa5 <= 0; lift 10 sesi <= 0; lift tidak positif pada kedua-dua separuh hari beli |
| `M119` 180 Bullish (Cooper) | CAMPUR | 147/63 | 18 | -0.70 | -1.84 | +0.40 | +0.07 | -0.64 | +0.53 | +1.79 / -0.66 | -1.41 | 6 | +1.17 | jangkaan <= 0; tanpa5 <= 0; lift 10 sesi <= 0; lift tidak positif pada kedua-dua separuh hari beli |
| `M125` 2-Bar Breakout | CAMPUR | 959/414 | 19 | -0.75 | -2.32 | -0.59 | +0.03 | -0.91 | +0.29 | +1.17 / -0.78 | -0.58 | 1 | +166.86 | jangkaan <= 0; tanpa5 <= 0; lift 10 sesi <= 0; lift tidak positif pada kedua-dua separuh hari beli |
| `M66` IBD Undur Pertama ke Purata 50 Hari | CAMPUR | 229/134 | 19 | -0.83 | -2.36 | -0.48 | +0.28 | -2.16 | +0.63 | +0.74 / +0.44 | -1.94 | 8 | +1.71 | jangkaan <= 0; tanpa5 <= 0; lift 10 sesi <= 0 |
| `M49` Ichimoku (Tutup Atas Awan + Tenkan Sil | CAMPUR | 289/152 | 19 | -0.89 | -1.97 | -0.12 | -0.42 | -1.73 | +0.23 | +0.36 / +0.02 | -2.18 | 20 | +3.99 | jangkaan <= 0; tanpa5 <= 0; lift 10 sesi <= 0 |
| `M55` Guppy GMMA | CAMPUR | 205/120 | 19 | -0.91 | -2.76 | +0.03 | +0.87 | -2.51 | +1.05 | +0.88 / +1.46 | -1.81 | 11 | +2.71 | jangkaan <= 0; tanpa5 <= 0; lift 10 sesi <= 0 |
| `M54` IBD Power Trend | CAMPUR | 201/105 | 18 | -1.00 | -2.20 | +0.42 | +0.36 | -0.72 | +0.75 | +1.52 / -0.65 | -1.34 | 3 | +3.37 | jangkaan <= 0; tanpa5 <= 0; lift 10 sesi <= 0; lift tidak positif pada kedua-dua separuh hari beli |
| `M12` Parabolic SAR | CAMPUR | 362/185 | 19 | -1.01 | -2.27 | -0.31 | -0.98 | -3.58 | +0.06 | -0.07 / +0.33 | -2.20 | 3 | +2.04 | jangkaan <= 0; tanpa5 <= 0; lift 10 sesi <= 0; lift tidak positif pada kedua-dua separuh hari beli |
| `M132` Ascending Scallop (Bulkowski) | CAMPUR | 94/36 | 17 | -1.08 | -2.51 | +0.18 | +0.31 | -1.43 | +0.34 | +1.21 / -0.40 | -1.61 | 1 | +0.98 | jangkaan <= 0; tanpa5 <= 0; lift 10 sesi <= 0; lift tidak positif pada kedua-dua separuh hari beli |
| `M06` Minervini VCP Breakout | CAMPUR | 80/34 | 19 | -1.14 | -2.53 | -0.78 | -0.40 | -0.15 | +0.35 | +1.06 / -0.56 | -1.44 | 1 | +2.49 | jangkaan <= 0; tanpa5 <= 0; lift 10 sesi <= 0; lift tidak positif pada kedua-dua separuh hari beli |
| `M152` Spike & Ledge | CAMPUR | 42/8 | 16 | -1.39 | -2.81 | +0.33 | +1.15 | -0.02 | +1.22 | +1.71 / +0.15 | -0.81 | 0 | +3.20 | jangkaan <= 0; tanpa5 <= 0; lift 10 sesi <= 0 |
| `M95` Nisbah Kebaharuan High 52 Minggu (Bhoo | CAMPUR | 120/62 | 18 | -1.39 | -2.35 | +0.57 | -0.03 | -0.71 | +0.26 | +1.02 / -0.58 | -1.54 | 2 | +2.68 | jangkaan <= 0; tanpa5 <= 0; lift 10 sesi <= 0; lift tidak positif pada kedua-dua separuh hari beli |
| `M147` Improved Three-Bar Pullback | CAMPUR | 97/33 | 15 | -2.75 | -4.12 | -0.72 | -0.02 | -2.85 | +0.71 | +0.47 / +1.25 | -0.87 | 1 | +91.01 | jangkaan <= 0; tanpa5 <= 0; lift 10 sesi <= 0 |
| `M90` Pring KST | CAMPUR | 78/42 | 18 | -3.10 | -4.11 | +0.31 | -0.54 | -5.65 | +0.27 | -0.05 / +0.71 | -3.74 | 4 | +1.95 | jangkaan <= 0; tanpa5 <= 0; lift 10 sesi <= 0; lift tidak positif pada kedua-dua separuh hari beli |
| `M101` Bulkowski: Tiga lembah menaik | CAMPUR | 44/21 | 15 | -3.24 | -4.64 | +0.83 | +0.38 | -1.94 | +0.41 | +1.00 / -0.18 | -3.16 | 2 | +3.46 | jangkaan <= 0; tanpa5 <= 0; lift 10 sesi <= 0; lift tidak positif pada kedua-dua separuh hari beli |
| `M104` High Tight Flag / Power Play | TERLALU AWAL | 1/0 | 1 | +19.60 | – | +14.59 | – | – | – | – / – | +19.60 | 0 | +5.62 | 1 posisi, 1 hari beli |
| `M37` Weinstein Peringkat 2 | TERLALU AWAL | 7/0 | 3 | +0.89 | +0.31 | +1.24 | -0.85 | -0.38 | +1.29 | -0.92 / +2.39 | +0.89 | 0 | +5.49 | 7 posisi, 3 hari beli |
| `M143` 장대양봉 이후 눌림목 / 5일선 매매 (Undur ke MA5 sel | TERLALU AWAL | 21/1 | 11 | +0.16 | -0.38 | +0.89 | +1.47 | -1.41 | +2.30 | +3.11 / +1.98 | +0.32 | 0 | +0.83 | 21 posisi, 11 hari beli |
| `M129` Wick Play | TERLALU AWAL | 26/10 | 10 | +0.06 | -2.64 | +0.45 | +2.03 | -0.74 | +1.51 | +2.57 / -0.91 | -0.61 | 0 | +2.60 | 26 posisi, 10 hari beli |
| `M21` Marius 3 Persediaan (Pecahan+Jurang+Ke | TERLALU AWAL | 5/2 | 5 | -0.06 | -1.92 | +1.61 | -0.96 | -16.56 | +3.61 | +4.22 / +1.78 | -2.43 | 0 | +2.57 | 5 posisi, 5 hari beli |
| `M41` FW Penyatuan Mingguan | TERLALU AWAL | 63/9 | 4 | -0.24 | -1.49 | +0.62 | +1.08 | -1.48 | +2.24 | +2.50 / +1.97 | -0.50 | 0 | +15.03 | 63 posisi, 4 hari beli |
| `M144` Screw Bar | TERLALU AWAL | 9/6 | 6 | -0.42 | -2.13 | +2.21 | -2.54 | -11.16 | -2.34 | -2.08 / -3.90 | -3.09 | 0 | +7.68 | 9 posisi, 6 hari beli |
| `M51` O'Neil Cawan & Pemegang | TERLALU AWAL | 3/0 | 2 | -0.46 | -4.63 | -1.99 | -2.01 | – | +0.14 | +0.14 / – | -0.46 | 0 | +3.12 | 3 posisi, 2 hari beli |
| `M27` Price Action 4 Tiang | TERLALU AWAL | 547/434 | 2 | -0.73 | -1.80 | -0.98 | -0.22 | +0.04 | +0.44 | +0.22 / +0.57 | -1.90 | 4 | +0.36 | 547 posisi, 2 hari beli |
| `M138` 直升机空中加油 (Helikopter isi minyak di udar | TERLALU AWAL | 3/0 | 3 | -0.81 | -1.72 | -2.52 | -1.46 | +0.26 | -0.81 | – / -0.81 | -0.81 | 0 | +4.60 | 3 posisi, 3 hari beli |
| `M120` Reversal New Highs | TERLALU AWAL | 19/12 | 13 | -1.24 | -2.75 | -1.77 | -3.30 | -0.21 | -2.95 | -4.97 / -0.35 | -1.49 | 5 | +1.15 | 19 posisi, 13 hari beli |
| `M78` Alvarez Pecahan Mingguan DTAYS | TERLALU AWAL | 73/39 | 2 | -1.71 | -3.04 | +0.82 | +1.20 | -2.20 | +0.64 | -1.50 / +3.70 | -2.73 | 0 | +3.17 | 73 posisi, 2 hari beli |
| `M141` First Thrust (Landry) | TERLALU AWAL | 23/8 | 8 | -1.92 | -3.22 | -1.62 | -0.27 | +0.42 | +0.14 | +0.41 / -0.27 | -3.83 | 0 | +4.05 | 23 posisi, 8 hari beli |
| `M38` Darvas Kotak | TERLALU AWAL | 23/1 | 4 | -2.00 | -2.98 | -0.60 | +1.05 | -1.69 | +1.69 | +6.47 / -2.50 | -2.56 | 0 | +18.79 | 23 posisi, 4 hari beli |
| `M67` Rayner Teo: Ujian Ketiga pada Purata 5 | TERLALU AWAL | 28/18 | 13 | -2.33 | -4.97 | -1.50 | -2.03 | -1.05 | -1.73 | +0.43 / -4.07 | -4.21 | 7 | +1.90 | 28 posisi, 13 hari beli |
| `M07` Qullamaggie Breakout | TERLALU AWAL | 1/1 | 1 | -2.53 | – | +4.46 | +1.85 | +9.31 | +0.99 | +0.99 / – | +22.73 | 0 | +1.05 | 1 posisi, 1 hari beli |
| `M130` 多方炮 (dua lilin hijau mengapit satu mer | TERLALU AWAL | 9/3 | 6 | -2.60 | -4.61 | +0.74 | -0.67 | -6.15 | -0.84 | +1.96 / -3.07 | -3.62 | 0 | +92.22 | 9 posisi, 6 hari beli |
| `M45` High 52 Minggu (George & Hwang) | TERLALU AWAL | 2/1 | 1 | -2.77 | -13.13 | -2.90 | -8.47 | – | -3.20 | – / -3.20 | -2.44 | 0 | +12.81 | 2 posisi, 1 hari beli |
| `M84` Jarak purata bergerak MAD 21/200 | TERLALU AWAL | 58/37 | 1 | -3.09 | -5.29 | -2.62 | -8.55 | – | -4.99 | – / -4.99 | -5.05 | 0 | +3.71 | 58 posisi, 1 hari beli |
| `M87` IBD Tapak Menaik | TERLALU AWAL | 10/6 | 7 | -3.09 | -5.92 | -1.54 | -2.30 | -2.44 | -1.57 | -0.10 / -3.40 | -4.01 | 0 | +3.49 | 10 posisi, 7 hari beli |
| `M47` Holy Grail Raschke | TERLALU AWAL | 29/22 | 13 | -3.31 | -3.88 | -4.70 | -4.71 | -8.80 | -3.35 | -5.04 / +0.87 | -6.27 | 7 | +0.25 | 29 posisi, 13 hari beli |
| `M94` Pecutan Momentum (Chen, Yu & Wang) | TERLALU AWAL | 33/0 | 1 | -3.79 | -6.17 | -2.61 | -11.42 | – | -7.59 | – / -7.59 | -4.68 | 0 | +24.04 | 33 posisi, 1 hari beli |
| `M135` 3rd Watch | TERLALU AWAL | 14/3 | 8 | -3.81 | -4.69 | -2.73 | -4.00 | -3.15 | -1.88 | -1.19 / -4.98 | -3.84 | 0 | +2.05 | 14 posisi, 8 hari beli |
| `M44` Tapak Rata IBD | TERLALU AWAL | 9/5 | 8 | -4.03 | -5.70 | -0.51 | -0.87 | -5.04 | -0.71 | -1.52 / +0.32 | -6.30 | 0 | +0.39 | 9 posisi, 8 hari beli |
| `M126` Hidden Smash Day (beli, Larry Williams | TERLALU AWAL | 18/11 | 10 | -4.06 | -4.82 | -0.68 | -1.35 | +1.65 | -0.93 | -2.69 / +0.83 | -3.47 | 0 | +5.15 | 18 posisi, 10 hari beli |
| `M09` Volumatic VIDYA Pivot Retest | TERLALU AWAL | 29/16 | 12 | -4.35 | -5.10 | -2.59 | -3.83 | -3.74 | -3.27 | -5.43 / +1.38 | -4.22 | 3 | +1.85 | 29 posisi, 12 hari beli |
| `M157` Consolidation Pivot Breakout (versi an | TERLALU AWAL | 4/3 | 4 | -5.16 | -8.98 | -0.98 | -7.89 | -0.56 | -7.53 | -9.44 / -1.79 | -4.98 | 0 | +32.05 | 4 posisi, 4 hari beli |
| `M64` O'Neil Tiga Minggu Ketat | TERLALU AWAL | 3/2 | 3 | -10.59 | -13.64 | -1.97 | +0.76 | -12.12 | +1.39 | +0.91 / +2.36 | -12.54 | 0 | +1.68 | 3 posisi, 3 hari beli |
| `M121` High 2 bull flag (Brooks) | TERLALU AWAL | 6/4 | 4 | -10.61 | -13.24 | +3.49 | +1.08 | -7.94 | +0.06 | +0.56 / -0.67 | -13.61 | 0 | +2.47 | 6 posisi, 4 hari beli |
| `M96` Momo India: Ranking Sharpe 3/6/12 bula | TERLALU AWAL | 6/6 | 1 | -13.40 | -14.14 | -5.11 | -16.29 | – | -12.46 | – / -12.46 | -14.01 | 0 | +12.18 | 6 posisi, 1 hari beli |
| `M107` Golden Cross SMA50/200 | LEMAH | 34/7 | 16 | -0.18 | -1.32 | +0.00 | -1.22 | +1.29 | -0.80 | +0.90 / -2.64 | -0.43 | 0 | +15.43 | jangkaan <= 0; tanpa5 <= 0; lift 5 sesi <= 0; lift tidak positif pada kedua-dua separuh hari beli |
| `M02` MACD + SMA200 | LEMAH | 117/60 | 19 | -0.19 | -2.16 | -1.19 | -2.28 | -0.64 | -1.47 | -1.79 / -0.72 | +0.36 | 9 | +0.66 | jangkaan <= 0; tanpa5 <= 0; lift 5 sesi <= 0; lift tidak positif pada kedua-dua separuh hari beli |
| `M139` 均线首次粘合向上发散 (MA berhimpun kali pertama, | LEMAH | 82/17 | 19 | -0.24 | -1.68 | +0.06 | -0.57 | -0.82 | -0.47 | -0.23 / -0.75 | -0.42 | 0 | +1.31 | jangkaan <= 0; tanpa5 <= 0; lift 5 sesi <= 0; lift tidak positif pada kedua-dua separuh hari beli |
| `M82` Arthur Hill Rotasi Sasaran 10% | LEMAH | 565/208 | 19 | -0.48 | -1.67 | -0.45 | -0.51 | +1.35 | -0.43 | -0.33 / -0.97 | -1.30 | 0 | +1.84 | jangkaan <= 0; tanpa5 <= 0; lift 5 sesi <= 0; lift tidak positif pada kedua-dua separuh hari beli |
| `M140` 猎豹出击 (Serangan Cheetah) | LEMAH | 41/12 | 10 | -0.62 | -1.70 | -2.29 | -2.12 | +1.34 | -1.67 | -0.98 / -3.48 | -0.19 | 2 | +5.31 | jangkaan <= 0; tanpa5 <= 0; lift 5 sesi <= 0; lift tidak positif pada kedua-dua separuh hari beli |
| `M79` Radge: 20% Flipper | LEMAH | 353/82 | 19 | -0.64 | -1.75 | -1.28 | -1.56 | -3.34 | -0.13 | +0.88 / -1.69 | -0.11 | 3 | +6.25 | jangkaan <= 0; tanpa5 <= 0; lift 5 sesi <= 0; lift 10 sesi <= 0; lift tidak positif pada kedua-dua separuh hari beli |
| `M20` EMA10/15 Crossover + Sudut | LEMAH | 443/344 | 19 | -0.68 | -1.66 | -0.71 | -0.60 | -2.83 | -0.14 | -0.21 / +0.00 | -1.98 | 17 | +0.22 | jangkaan <= 0; tanpa5 <= 0; lift 5 sesi <= 0; lift 10 sesi <= 0; lift tidak positif pada kedua-dua separuh hari beli |
| `M11` NR7 Breakout + Volume | LEMAH | 108/77 | 17 | -0.81 | -1.67 | -1.32 | -2.00 | -0.02 | -1.53 | -1.42 / -1.62 | -0.66 | 7 | +2.86 | jangkaan <= 0; tanpa5 <= 0; lift 5 sesi <= 0; lift tidak positif pada kedua-dua separuh hari beli |
| `M156` Single Penetration (DiNapoli) | LEMAH | 229/145 | 19 | -0.91 | -2.23 | -0.89 | -1.68 | +0.28 | -1.18 | -2.48 / +0.38 | -1.86 | 0 | +0.69 | jangkaan <= 0; tanpa5 <= 0; lift 5 sesi <= 0; lift tidak positif pada kedua-dua separuh hari beli |
| `M28` VWAP Separator + Kiss Pivot | LEMAH | 112/88 | 17 | -1.00 | -1.92 | -0.37 | -3.13 | -3.76 | -1.71 | -1.91 / -1.25 | -3.66 | 20 | +0.22 | jangkaan <= 0; tanpa5 <= 0; lift 5 sesi <= 0; lift 10 sesi <= 0; lift tidak positif pada kedua-dua separuh hari beli |
| `M76` Undercut & Rally pada Low Penting | LEMAH | 71/45 | 18 | -1.15 | -1.75 | +0.40 | -2.16 | -6.78 | -1.38 | -1.75 / -0.89 | -2.76 | 11 | +0.67 | jangkaan <= 0; tanpa5 <= 0; lift 5 sesi <= 0; lift 10 sesi <= 0; lift tidak positif pada kedua-dua separuh hari beli |
| `M39` Radge Pecahan Bollinger 100 hari | LEMAH | 233/49 | 19 | -1.28 | -2.70 | -0.71 | -1.05 | -1.11 | -0.70 | -0.48 / -1.02 | -1.36 | 0 | +9.11 | jangkaan <= 0; tanpa5 <= 0; lift 5 sesi <= 0; lift 10 sesi <= 0; lift tidak positif pada kedua-dua separuh hari beli |
| `M115` Bow Tie (Landry) | LEMAH | 35/23 | 10 | -1.37 | -2.72 | +1.42 | -0.48 | +1.47 | -0.31 | -0.89 / +0.48 | -1.84 | 9 | +1.06 | jangkaan <= 0; tanpa5 <= 0; lift 5 sesi <= 0; lift tidak positif pada kedua-dua separuh hari beli |
| `M148` Natural Number Method | LEMAH | 210/129 | 19 | -1.47 | -2.57 | -0.82 | -1.13 | -2.13 | -0.64 | +0.36 / -2.10 | -1.30 | 8 | +0.50 | jangkaan <= 0; tanpa5 <= 0; lift 5 sesi <= 0; lift 10 sesi <= 0; lift tidak positif pada kedua-dua separuh hari beli |
| `M19` Sneaky Pivot (proksi harian) | LEMAH | 377/231 | 18 | -1.47 | -2.59 | -1.21 | -2.57 | -3.86 | -0.88 | +0.97 / -2.52 | -0.85 | 3 | +0.27 | jangkaan <= 0; tanpa5 <= 0; lift 5 sesi <= 0; lift 10 sesi <= 0; lift tidak positif pada kedua-dua separuh hari beli |
| `M57` Landry Trend Knockout (TKO) | LEMAH | 160/102 | 19 | -1.68 | -3.04 | -1.43 | -1.42 | -2.74 | -0.45 | -2.15 / +1.07 | -2.95 | 18 | +1.55 | jangkaan <= 0; tanpa5 <= 0; lift 5 sesi <= 0; lift 10 sesi <= 0; lift tidak positif pada kedua-dua separuh hari beli |
| `M99` Three Line Break | LEMAH | 147/85 | 19 | -1.80 | -3.56 | -1.00 | -1.80 | -3.11 | -0.90 | -0.72 / -1.30 | -2.58 | 8 | +1.17 | jangkaan <= 0; tanpa5 <= 0; lift 5 sesi <= 0; lift 10 sesi <= 0; lift tidak positif pada kedua-dua separuh hari beli |
| `M154` HOLP (High of Low Period) | LEMAH | 79/32 | 15 | -2.00 | -3.60 | -1.29 | -1.36 | -4.96 | -0.67 | -0.28 / -1.93 | -3.33 | 3 | +1.93 | jangkaan <= 0; tanpa5 <= 0; lift 5 sesi <= 0; lift 10 sesi <= 0; lift tidak positif pada kedua-dua separuh hari beli |
| `M68` Kell Base n' Break | LEMAH | 42/12 | 13 | -2.03 | -3.51 | -2.20 | -1.99 | +1.35 | -1.31 | -1.25 / -1.53 | -1.23 | 2 | +1.35 | jangkaan <= 0; tanpa5 <= 0; lift 5 sesi <= 0; lift tidak positif pada kedua-dua separuh hari beli |
| `M122` Moving Momentum (ChartSchool) | LEMAH | 102/58 | 19 | -2.49 | -3.96 | -1.65 | -3.21 | -3.05 | -2.12 | -3.02 / -0.36 | -1.61 | 6 | +1.79 | jangkaan <= 0; tanpa5 <= 0; lift 5 sesi <= 0; lift 10 sesi <= 0; lift tidak positif pada kedua-dua separuh hari beli |
| `M81` Bensdorp Long Trend High Momentum | LEMAH | 331/140 | 12 | -3.94 | -5.19 | -1.03 | -1.36 | +0.27 | -0.68 | -0.74 / -0.21 | -4.49 | 1 | +8.56 | jangkaan <= 0; tanpa5 <= 0; lift 5 sesi <= 0; lift 10 sesi <= 0; lift tidak positif pada kedua-dua separuh hari beli |
| `M59` Anjakan Julat RSI | LEMAH | 36/16 | 14 | -4.46 | -5.78 | -1.26 | -2.79 | -7.34 | -2.32 | -6.58 / +1.93 | -4.87 | 0 | +3.10 | jangkaan <= 0; tanpa5 <= 0; lift 5 sesi <= 0; lift 10 sesi <= 0; lift tidak positif pada kedua-dua separuh hari beli |
| `M74` Lulus Baharu Trend Template Minervini | STRUKTUR GAGAL | 90/53 | 19 | +0.60 | -0.94 | -0.15 | -0.07 | +1.52 | +0.70 | +0.83 / +0.55 | +1.34 | 27 | +2.72 | henti hari-0 27% posisi (G4 pasti gagal) |
| `M77` Undercut & Rally pada Purata Bergerak  | STRUKTUR GAGAL | 54/33 | 17 | +0.20 | -0.69 | -0.52 | -0.85 | -1.39 | -0.13 | -0.14 / -0.11 | -1.04 | 20 | +2.69 | henti hari-0 20% posisi (G4 pasti gagal) |
| `M35` Pocket Pivot Morales & Kacher | STRUKTUR GAGAL | 307/207 | 19 | +0.17 | -1.08 | +0.07 | +0.25 | +1.01 | +0.55 | +0.09 / +1.38 | +0.24 | 23 | +0.29 | henti hari-0 23% posisi (G4 pasti gagal) |
| `M23` Breitstein Kapitulasi + Kesinambungan | STRUKTUR GAGAL | 121/74 | 19 | +0.05 | -1.00 | -0.34 | -0.99 | +1.16 | +0.14 | -0.39 / +1.35 | -0.51 | 36 | +0.55 | henti hari-0 36% posisi (G4 pasti gagal) |
| `M46` Jurang Naik Boleh Beli (Buyable Gap Up | STRUKTUR GAGAL | 35/17 | 12 | -0.03 | -1.07 | +0.34 | -1.69 | +3.28 | +0.01 | -0.98 / +2.50 | +1.00 | 34 | +2.81 | henti hari-0 34% posisi (G4 pasti gagal) |
| `M70` Pecahan Hari Dalam | STRUKTUR GAGAL | 441/332 | 19 | -0.05 | -1.15 | +0.38 | -0.37 | -2.75 | -0.22 | +1.02 / -2.11 | -1.74 | 46 | +0.84 | henti hari-0 46% posisi (G4 pasti gagal) |
| `M102` Stockbee SLTB | STRUKTUR GAGAL | 359/265 | 19 | -0.80 | -2.14 | -0.29 | -0.03 | -0.95 | +0.51 | +0.90 / -0.12 | -1.89 | 31 | +1.34 | henti hari-0 31% posisi (G4 pasti gagal) |
| `M123` CCI Correction (Lambert, ChartSchool) | STRUKTUR GAGAL | 175/151 | 19 | -1.36 | -1.89 | -0.33 | -0.81 | -0.80 | -0.44 | +0.25 / -1.48 | -0.13 | 29 | +0.92 | henti hari-0 29% posisi (G4 pasti gagal) |
| `M127` Slingshot Bullish | STRUKTUR GAGAL | 105/75 | 16 | -1.36 | -2.19 | -0.53 | -0.44 | +2.35 | +0.24 | -0.39 / +1.05 | -0.81 | 21 | +2.60 | henti hari-0 21% posisi (G4 pasti gagal) |
| `M29` EMA3 + RSI75 + Stokastik | STRUKTUR GAGAL | 33/26 | 14 | -2.15 | -3.42 | -1.30 | -0.32 | -6.36 | -0.55 | +0.25 / -3.28 | -3.44 | 36 | +3.22 | henti hari-0 36% posisi (G4 pasti gagal) |

## Kombinasi Nxx (masuk × keluar)

| Kaedah | Kelas | Posisi/tutup | Hari beli | Jangkaan % | tanpa5 % | r3 | r5 | r10 | Lift 5 | A / B | L2 % | Hari-0 % | Backtest % | Sebab |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `N19X13` Bawah jalur BB + RSI<30 → keluar bila  | TERLALU AWAL | 101/0 | 5 | +4.61 | +3.49 | +1.59 | +0.20 | – | +1.23 | +1.95 / -0.00 | +4.61 | 0 | +11.29 | 101 posisi, 5 hari beli |
| `N124X15` Episodic pivot gap 8-10% → ekori Chand | TERLALU AWAL | 39/0 | 6 | +3.79 | +2.77 | +2.66 | -1.32 | – | -0.17 | -0.27 / +0.10 | +3.79 | 0 | +16.13 | 39 posisi, 6 hari beli |
| `N40X36` OBV tinggi baharu + MA50 → keluar sele | TERLALU AWAL | 47/7 | 6 | +2.82 | -0.37 | -1.06 | -0.43 | – | +1.38 | -0.12 / +2.74 | +3.56 | 0 | +2.14 | 47 posisi, 6 hari beli |
| `N75X14` RSI14 < 40 tanpa penapis → keluar bila | TERLALU AWAL | 188/21 | 6 | +2.36 | +1.64 | +0.40 | -0.07 | – | +1.01 | +1.42 / -0.33 | +2.71 | 0 | +1.62 | 188 posisi, 6 hari beli |
| `N42X15` Lonjakan volum 2x → ekori Chandelier 4 | TERLALU AWAL | 148/0 | 6 | +2.33 | +0.56 | +0.83 | -0.72 | – | +0.86 | +0.93 / +0.65 | +2.33 | 0 | +5.46 | 148 posisi, 6 hari beli |
| `N75X15` RSI14 < 40 tanpa penapis → ekori Chand | TERLALU AWAL | 124/0 | 6 | +2.32 | +1.36 | +0.10 | +0.00 | – | +1.13 | +1.31 / +0.54 | +2.32 | 0 | +5.61 | 124 posisi, 6 hari beli |
| `N64X36` Episodic pivot → keluar selepas DUA tu | TERLALU AWAL | 46/4 | 6 | +2.25 | +1.01 | +1.83 | -1.80 | – | -0.05 | -0.53 / +3.51 | +2.35 | 0 | +4.11 | 46 posisi, 6 hari beli |
| `N75X13` RSI14 < 40 tanpa penapis → keluar bila | TERLALU AWAL | 124/1 | 6 | +2.24 | +1.36 | +0.10 | +0.00 | – | +1.13 | +1.31 / +0.54 | +2.32 | 0 | +7.47 | 124 posisi, 6 hari beli |
| `N42X14` Lonjakan volum 2x → keluar bila rsi14  | TERLALU AWAL | 159/9 | 6 | +2.19 | +0.59 | +0.89 | -0.67 | – | +0.93 | +0.96 / +0.84 | +2.26 | 0 | +2.60 | 159 posisi, 6 hari beli |
| `N64X14` Episodic pivot → keluar bila rsi14 sil | TERLALU AWAL | 46/1 | 6 | +2.14 | +1.12 | +1.83 | -1.80 | – | -0.05 | -0.53 / +3.51 | +2.35 | 0 | +3.20 | 46 posisi, 6 hari beli |
| `N40X16` OBV tinggi baharu + MA50 → keluar bila | TERLALU AWAL | 61/21 | 6 | +2.01 | -0.73 | -1.29 | -0.02 | – | +1.70 | +2.24 / +1.33 | +3.24 | 0 | +1.27 | 61 posisi, 6 hari beli |
| `N64X16` Episodic pivot → keluar bila supertren | TERLALU AWAL | 46/5 | 6 | +2.00 | +0.74 | +1.83 | -1.80 | – | -0.05 | -0.53 / +3.51 | +2.35 | 0 | +3.12 | 46 posisi, 6 hari beli |
| `N73X13` Tutup bawah jalur bawah BB(20,2) → kel | TERLALU AWAL | 136/1 | 6 | +1.95 | +1.05 | -0.09 | -0.79 | – | +0.24 | +0.44 / -0.17 | +1.99 | 0 | +6.89 | 136 posisi, 6 hari beli |
| `N124X36` Episodic pivot gap 8-10% → keluar sele | TERLALU AWAL | 39/10 | 6 | +1.93 | +0.81 | +2.66 | -1.32 | – | -0.17 | -0.27 / +0.10 | +3.79 | 0 | +5.91 | 39 posisi, 6 hari beli |
| `N53X36` Supertrend + ADX>25 → keluar selepas D | TERLALU AWAL | 106/19 | 6 | +1.82 | -1.21 | +2.70 | +1.69 | – | +3.55 | +1.15 / +9.27 | +3.83 | 0 | +2.42 | 106 posisi, 6 hari beli |
| `N64X17` Episodic pivot → keluar bila adx14 < 2 | TERLALU AWAL | 46/10 | 6 | +1.51 | +0.23 | +1.83 | -1.80 | – | -0.05 | -0.53 / +3.51 | +2.35 | 0 | +4.82 | 46 posisi, 6 hari beli |
| `N42X17` Lonjakan volum 2x → keluar bila adx14  | TERLALU AWAL | 172/44 | 6 | +1.29 | -0.27 | +0.76 | -0.61 | – | +1.04 | +0.85 / +1.54 | +2.06 | 0 | +3.93 | 172 posisi, 6 hari beli |
| `N75X17` RSI14 < 40 tanpa penapis → keluar bila | TERLALU AWAL | 267/110 | 6 | +1.27 | +0.55 | +0.84 | -0.06 | – | +1.00 | +1.54 / -0.35 | +2.71 | 0 | +4.53 | 267 posisi, 6 hari beli |
| `N48X36` Inside day pecah → keluar selepas DUA  | TERLALU AWAL | 256/158 | 6 | +1.04 | +0.33 | -1.93 | -2.76 | – | -1.31 | -2.26 / +2.77 | +1.55 | 0 | +1.28 | 256 posisi, 6 hari beli |
| `N113X16` 80-20 bar (sisi beli) → keluar bila su | TERLALU AWAL | 256/162 | 6 | +0.97 | -0.53 | -2.07 | -0.59 | – | +1.02 | -2.69 / +5.68 | +1.92 | 0 | +0.82 | 256 posisi, 6 hari beli |
| `N42X36` Lonjakan volum 2x → keluar selepas DUA | TERLALU AWAL | 171/78 | 6 | +0.93 | -0.58 | +1.25 | -0.48 | – | +1.13 | +1.02 / +1.45 | +2.58 | 0 | +2.59 | 171 posisi, 6 hari beli |
| `N28X36` ADX>25 + DI+ > DI- → keluar selepas DU | TERLALU AWAL | 222/106 | 6 | +0.88 | -0.88 | +1.26 | -0.38 | – | +1.48 | -0.35 / +4.09 | +2.40 | 0 | +1.74 | 222 posisi, 6 hari beli |
| `N42X16` Lonjakan volum 2x → keluar bila supert | TERLALU AWAL | 175/76 | 6 | +0.84 | -0.64 | +1.23 | -0.49 | – | +1.14 | +0.98 / +1.58 | +2.50 | 0 | +1.82 | 175 posisi, 6 hari beli |
| `N24X36` Supertrend(10,3) + ADX>20 → keluar sel | TERLALU AWAL | 121/31 | 6 | +0.75 | -1.91 | +1.13 | +0.25 | – | +1.62 | -1.09 / +6.47 | +2.85 | 0 | +2.12 | 121 posisi, 6 hari beli |
| `N76X36` Tutup > MA50 (penapis trend tunggal) → | TERLALU AWAL | 144/35 | 6 | +0.70 | -0.96 | -0.47 | -0.15 | – | +1.30 | +0.70 / +3.14 | +1.52 | 0 | +1.76 | 144 posisi, 6 hari beli |
| `N55X13` BB + RSI + ADX>20 → keluar bila rsi14  | TERLALU AWAL | 57/0 | 6 | +0.67 | +0.04 | -0.17 | -1.86 | – | -0.91 | -0.21 / -3.95 | +0.67 | 0 | +4.45 | 57 posisi, 6 hari beli |
| `N65X36` Gap 4% + volum + hampir 52w → keluar s | TERLALU AWAL | 28/0 | 5 | +0.64 | -0.63 | +0.34 | -2.37 | – | -0.37 | -0.53 / +2.49 | +0.64 | 0 | +3.74 | 28 posisi, 5 hari beli |
| `N25X36` Supertrend + EMA + ADX>23 → keluar sel | TERLALU AWAL | 108/16 | 6 | +0.58 | -1.11 | -1.19 | +1.18 | – | +3.20 | +0.26 / +8.28 | +2.41 | 0 | +2.31 | 108 posisi, 6 hari beli |
| `N65X14` Gap 4% + volum + hampir 52w → keluar b | TERLALU AWAL | 28/1 | 5 | +0.58 | -0.69 | +0.34 | -2.37 | – | -0.37 | -0.53 / +2.49 | +0.64 | 0 | +3.23 | 28 posisi, 5 hari beli |
| `N16X13` RSI2<10 tanpa penapis → keluar bila rs | TERLALU AWAL | 113/3 | 6 | +0.48 | -0.30 | -1.46 | -2.56 | – | -1.25 | +0.82 / -4.30 | +0.17 | 0 | +5.86 | 113 posisi, 6 hari beli |
| `N113X36` 80-20 bar (sisi beli) → keluar selepas | TERLALU AWAL | 244/148 | 6 | +0.46 | -0.44 | -1.84 | +0.01 | – | +1.83 | -1.24 / +5.54 | +2.05 | 0 | +0.97 | 244 posisi, 6 hari beli |
| `N43X36` Undur EMA8 + penapis MA50 → keluar sel | TERLALU AWAL | 136/21 | 6 | +0.26 | -1.32 | -1.76 | -3.64 | – | -2.10 | -2.37 / -1.36 | +0.27 | 0 | +1.66 | 136 posisi, 6 hari beli |
| `N80X36` Tinggi sepanjang masa → keluar selepas | TERLALU AWAL | 32/1 | 5 | +0.20 | -0.72 | -0.03 | -0.75 | – | +1.06 | -0.52 / +6.96 | +0.13 | 0 | +0.99 | 32 posisi, 5 hari beli |
| `N16X15` RSI2<10 tanpa penapis → ekori Chandeli | TERLALU AWAL | 109/0 | 6 | +0.17 | -0.66 | -1.66 | -2.56 | – | -1.25 | +0.82 / -4.30 | +0.02 | 0 | +4.35 | 109 posisi, 6 hari beli |
| `N45X16` Undur EMA21 cerun positif → keluar bil | TERLALU AWAL | 117/44 | 6 | +0.15 | -0.75 | -0.34 | -0.20 | – | +1.58 | -0.24 / +3.63 | +0.71 | 0 | +1.32 | 117 posisi, 6 hari beli |
| `N66X36` 52w tinggi + pengesahan 1% → keluar se | TERLALU AWAL | 33/1 | 5 | +0.15 | -0.94 | +0.47 | -2.09 | – | +0.02 | +0.02 / – | +0.43 | 0 | +1.84 | 33 posisi, 5 hari beli |
| `N119X13` 3 tutup turun berturut → keluar bila r | TERLALU AWAL | 144/33 | 6 | +0.14 | -0.44 | -0.70 | -5.55 | – | -4.12 | -1.97 / -4.95 | -0.18 | 0 | +5.09 | 144 posisi, 6 hari beli |
| `N37X14` Gap and go → keluar bila rsi14 silang  | TERLALU AWAL | 75/5 | 6 | +0.14 | -0.75 | +0.67 | -3.57 | – | -1.92 | -2.31 / +3.51 | +0.37 | 0 | +3.45 | 75 posisi, 6 hari beli |
| `N50X17` Mampat + pecah volum 1.5x → keluar bil | TERLALU AWAL | 12/2 | 3 | +0.14 | -1.38 | -3.16 | -2.87 | – | -1.61 | -2.47 / -0.12 | +0.76 | 0 | +3.98 | 12 posisi, 3 hari beli |
| `N37X36` Gap and go → keluar selepas DUA tutup  | TERLALU AWAL | 76/16 | 6 | +0.12 | -0.91 | +0.67 | -3.57 | – | -1.92 | -2.31 / +3.51 | +0.34 | 0 | +4.15 | 76 posisi, 6 hari beli |
| `N36X36` Pocket pivot → keluar selepas DUA tutu | TERLALU AWAL | 135/49 | 6 | +0.11 | -1.75 | -0.56 | -1.33 | – | +0.38 | -0.54 / +2.61 | +0.86 | 0 | +2.13 | 135 posisi, 6 hari beli |
| `N54X36` Supertrend + RSI>50 → keluar selepas D | TERLALU AWAL | 140/42 | 6 | +0.10 | -1.38 | -1.55 | -0.16 | – | +1.56 | +0.08 / +4.76 | +1.68 | 0 | +1.90 | 140 posisi, 6 hari beli |
| `N28X14` ADX>25 + DI+ > DI- → keluar bila rsi14 | TERLALU AWAL | 132/8 | 6 | +0.08 | -0.97 | +1.10 | -2.04 | – | -0.37 | -0.30 / -0.61 | +1.27 | 0 | +1.60 | 132 posisi, 6 hari beli |
| `N28X17` ADX>25 + DI+ > DI- → keluar bila adx14 | TERLALU AWAL | 85/0 | 6 | +0.04 | -0.92 | -0.42 | -1.11 | – | +0.66 | +0.98 / -0.31 | +0.00 | 0 | +4.59 | 85 posisi, 6 hari beli |
| `N37X16` Gap and go → keluar bila supertrend be | TERLALU AWAL | 76/16 | 6 | -0.00 | -1.04 | +0.67 | -3.57 | – | -1.92 | -2.31 / +3.51 | +0.34 | 0 | +3.39 | 76 posisi, 6 hari beli |
| `N09X36` Undur EMA10 + penapis EMA50 → keluar s | TERLALU AWAL | 146/36 | 6 | -0.01 | -1.59 | -1.16 | -3.17 | – | -1.74 | -2.13 / -0.13 | +0.06 | 0 | +1.54 | 146 posisi, 6 hari beli |
| `N28X16` ADX>25 + DI+ > DI- → keluar bila super | TERLALU AWAL | 233/115 | 6 | -0.01 | -0.75 | -0.26 | -2.22 | – | -0.52 | -0.50 / -0.53 | +0.60 | 0 | +1.31 | 233 posisi, 6 hari beli |
| `N36X16` Pocket pivot → keluar bila supertrend  | TERLALU AWAL | 139/47 | 6 | -0.01 | -1.79 | -0.16 | -1.39 | – | +0.33 | -0.72 / +2.80 | +1.04 | 0 | +1.53 | 139 posisi, 6 hari beli |
| `N68X36` Bullish engulfing + EMA21 → keluar sel | TERLALU AWAL | 50/7 | 6 | -0.02 | -1.54 | -0.63 | +5.88 | – | +7.22 | +4.22 / +9.09 | +0.57 | 0 | +1.57 | 50 posisi, 6 hari beli |
| `N36X14` Pocket pivot → keluar bila rsi14 silan | TERLALU AWAL | 133/17 | 6 | -0.03 | -1.77 | -1.26 | -2.27 | – | -0.60 | -1.51 / +1.77 | +0.24 | 0 | +1.44 | 133 posisi, 6 hari beli |
| `N53X16` Supertrend + ADX>25 → keluar bila supe | TERLALU AWAL | 94/4 | 6 | -0.03 | -0.91 | +0.11 | -1.32 | – | +0.53 | +0.77 / -0.18 | -0.01 | 0 | +2.16 | 94 posisi, 6 hari beli |
| `N53X17` Supertrend + ADX>25 → keluar bila adx1 | TERLALU AWAL | 87/0 | 6 | -0.03 | -0.98 | +0.19 | -1.10 | – | +0.82 | +1.20 / -0.18 | -0.04 | 0 | +3.81 | 87 posisi, 6 hari beli |
| `N56X36` RSI>50 + ADX>20 → keluar selepas DUA t | TERLALU AWAL | 145/51 | 6 | -0.04 | -1.48 | -1.64 | -0.55 | – | +1.13 | -2.45 / +5.57 | +1.53 | 0 | +2.17 | 145 posisi, 6 hari beli |
| `N50X14` Mampat + pecah volum 1.5x → keluar bil | TERLALU AWAL | 12/2 | 3 | -0.08 | -1.00 | -3.16 | -2.87 | – | -1.61 | -2.47 / -0.12 | +0.76 | 0 | +2.20 | 12 posisi, 3 hari beli |
| `N45X36` Undur EMA21 cerun positif → keluar sel | TERLALU AWAL | 97/27 | 6 | -0.10 | -1.16 | -0.62 | -1.02 | – | +0.83 | +0.15 / +1.44 | +0.03 | 0 | +1.93 | 97 posisi, 6 hari beli |
| `N56X17` RSI>50 + ADX>20 → keluar bila adx14 <  | TERLALU AWAL | 110/11 | 6 | -0.12 | -0.91 | -0.83 | -1.21 | – | +0.53 | +0.12 / +1.08 | -0.06 | 0 | +2.37 | 110 posisi, 6 hari beli |
| `N37X17` Gap and go → keluar bila adx14 < 20 | TERLALU AWAL | 76/24 | 6 | -0.15 | -1.20 | +0.62 | -3.76 | – | -2.15 | -2.56 / +3.51 | +0.24 | 0 | +4.87 | 76 posisi, 6 hari beli |
| `N22X36` BB pecah atas + RSI → keluar selepas D | TERLALU AWAL | 107/23 | 6 | -0.16 | -1.18 | -0.23 | -1.94 | – | -0.12 | -0.30 / +2.12 | -0.07 | 0 | +2.09 | 107 posisi, 6 hari beli |
| `N33X36` Donchian20 + penapis MA200 → keluar se | TERLALU AWAL | 81/10 | 6 | -0.16 | -1.21 | -0.33 | -1.94 | – | -0.07 | -0.27 / +1.70 | -0.31 | 0 | +2.09 | 81 posisi, 6 hari beli |
| `N56X16` RSI>50 + ADX>20 → keluar bila supertre | TERLALU AWAL | 157/54 | 6 | -0.16 | -0.80 | -0.35 | -1.16 | – | +0.70 | -0.28 / +1.95 | +0.48 | 0 | +1.48 | 157 posisi, 6 hari beli |
| `N25X16` Supertrend + EMA + ADX>23 → keluar bil | TERLALU AWAL | 99/2 | 6 | -0.17 | -0.79 | -0.86 | -1.21 | – | +0.78 | +0.27 / +1.70 | -0.12 | 0 | +1.81 | 99 posisi, 6 hari beli |
| `N07X36` Tiga MA tersusun → keluar selepas DUA  | TERLALU AWAL | 115/8 | 6 | -0.18 | -1.04 | -0.48 | -1.33 | – | +0.26 | +0.03 / +0.51 | -0.13 | 0 | +1.89 | 115 posisi, 6 hari beli |
| `N25X17` Supertrend + EMA + ADX>23 → keluar bil | TERLALU AWAL | 95/4 | 6 | -0.21 | -0.84 | -0.78 | -0.95 | – | +1.10 | +0.74 / +1.70 | -0.16 | 0 | +2.73 | 95 posisi, 6 hari beli |
| `N74X16` MACD atas garis isyarat (keadaan, buka | TERLALU AWAL | 320/180 | 6 | -0.21 | -0.97 | -0.00 | -0.82 | – | +0.55 | +1.48 / -0.84 | +0.52 | 0 | +1.15 | 320 posisi, 6 hari beli |
| `N07X16` Tiga MA tersusun → keluar bila supertr | TERLALU AWAL | 113/11 | 6 | -0.23 | -0.95 | -0.57 | -1.37 | – | +0.18 | -0.16 / +0.51 | -0.12 | 0 | +1.48 | 113 posisi, 6 hari beli |
| `N08X36` tutup>EMA20 tidak terlalu jauh → kelua | TERLALU AWAL | 270/145 | 6 | -0.23 | -1.49 | -1.27 | -0.70 | – | +1.09 | +1.06 / +1.11 | +0.87 | 0 | +1.40 | 270 posisi, 6 hari beli |
| `N22X16` BB pecah atas + RSI → keluar bila supe | TERLALU AWAL | 109/20 | 6 | -0.32 | -1.21 | -0.14 | -1.79 | – | +0.14 | +0.01 / +1.42 | +0.21 | 0 | +1.40 | 109 posisi, 6 hari beli |
| `N41X36` CMF20>0 + tutup>EMA20 → keluar selepas | TERLALU AWAL | 182/91 | 6 | -0.35 | -1.85 | -1.04 | +0.01 | – | +1.82 | +0.21 / +4.61 | +1.22 | 0 | +1.57 | 182 posisi, 6 hari beli |
| `N24X17` Supertrend(10,3) + ADX>20 → keluar bil | TERLALU AWAL | 101/6 | 6 | -0.36 | -1.16 | -1.01 | -1.95 | – | -0.42 | -0.83 / +0.24 | -0.48 | 0 | +2.85 | 101 posisi, 6 hari beli |
| `N47X16` NR7 + EMA9>EMA21 → keluar bila supertr | TERLALU AWAL | 110/13 | 6 | -0.37 | -0.82 | -2.29 | -3.60 | – | -2.02 | -2.09 / -2.01 | -0.39 | 0 | +1.30 | 110 posisi, 6 hari beli |
| `N24X16` Supertrend(10,3) + ADX>20 → keluar bil | TERLALU AWAL | 96/2 | 6 | -0.39 | -1.13 | -0.82 | -1.79 | – | -0.21 | -0.55 / +0.40 | -0.25 | 0 | +1.98 | 96 posisi, 6 hari beli |
| `N54X16` Supertrend + RSI>50 → keluar bila supe | TERLALU AWAL | 107/4 | 6 | -0.43 | -1.15 | -0.84 | -1.90 | – | -0.37 | -0.32 / -0.53 | -0.17 | 0 | +1.58 | 107 posisi, 6 hari beli |
| `N35X36` Pecah 52 minggu tinggi → keluar selepa | TERLALU AWAL | 42/1 | 5 | -0.48 | -1.35 | -0.95 | -1.87 | – | +0.15 | -1.29 / +6.96 | -0.53 | 0 | +1.34 | 42 posisi, 5 hari beli |
| `N33X16` Donchian20 + penapis MA200 → keluar bi | TERLALU AWAL | 83/7 | 6 | -0.50 | -1.43 | -0.43 | -2.22 | – | -0.31 | -0.54 / +1.70 | -0.27 | 0 | +1.16 | 83 posisi, 6 hari beli |
| `N22X14` BB pecah atas + RSI → keluar bila rsi1 | TERLALU AWAL | 111/11 | 6 | -0.54 | -1.51 | -0.46 | -2.49 | – | -0.63 | -0.73 / +2.16 | -0.28 | 0 | +1.44 | 111 posisi, 6 hari beli |
| `N119X15` 3 tutup turun berturut → ekori Chandel | TERLALU AWAL | 40/0 | 5 | -0.58 | -1.07 | -1.09 | -3.75 | – | -2.68 | +0.46 / -5.30 | -0.58 | 0 | +3.93 | 40 posisi, 5 hari beli |
| `N76X16` Tutup > MA50 (penapis trend tunggal) → | TERLALU AWAL | 216/105 | 6 | -0.58 | -1.28 | -1.34 | -2.14 | – | -0.69 | -1.71 / +1.03 | +0.52 | 0 | +1.14 | 216 posisi, 6 hari beli |
| `N33X14` Donchian20 + penapis MA200 → keluar bi | TERLALU AWAL | 90/5 | 6 | -0.60 | -1.58 | -0.62 | -2.21 | – | -0.23 | -0.53 / +2.12 | -0.48 | 0 | +1.30 | 90 posisi, 6 hari beli |
| `N08X16` tutup>EMA20 tidak terlalu jauh → kelua | TERLALU AWAL | 303/181 | 6 | -0.61 | -1.51 | -0.77 | -1.65 | – | +0.02 | +1.49 / -1.74 | +0.27 | 0 | +1.18 | 303 posisi, 6 hari beli |
| `N29X36` PSAR naik + tutup>MA50 → keluar selepa | TERLALU AWAL | 126/32 | 6 | -0.64 | -1.59 | -1.40 | -1.61 | – | -0.19 | -0.21 / -0.12 | -0.03 | 0 | +1.78 | 126 posisi, 6 hari beli |
| `N68X16` Bullish engulfing + EMA21 → keluar bil | TERLALU AWAL | 50/10 | 6 | -0.77 | -1.74 | -0.56 | +5.77 | – | +7.18 | +4.22 / +8.82 | +0.69 | 0 | +1.15 | 50 posisi, 6 hari beli |
| `N38X36` VCP pecah → keluar selepas DUA tutup d | TERLALU AWAL | 22/6 | 6 | -0.79 | -2.12 | -1.20 | -1.02 | – | +0.98 | +0.93 / +1.09 | -0.67 | 0 | +2.29 | 22 posisi, 6 hari beli |
| `N27X16` Ichimoku atas awan → keluar bila super | TERLALU AWAL | 127/44 | 6 | -0.87 | -1.61 | -1.04 | -3.93 | – | -2.14 | -1.60 / -5.08 | -0.67 | 0 | +1.10 | 127 posisi, 6 hari beli |
| `N41X16` CMF20>0 + tutup>EMA20 → keluar bila su | TERLALU AWAL | 207/107 | 6 | -0.88 | -1.67 | -0.55 | -1.07 | – | +0.73 | +0.56 / +1.01 | +0.11 | 0 | +1.05 | 207 posisi, 6 hari beli |
| `N27X36` Ichimoku atas awan → keluar selepas DU | TERLALU AWAL | 85/7 | 6 | -0.92 | -1.83 | -1.18 | -3.55 | – | -1.67 | -1.92 / +0.11 | -0.86 | 0 | +1.83 | 85 posisi, 6 hari beli |
| `N06X36` Golden cross MA50/MA200 → keluar selep | TERLALU AWAL | 14/2 | 5 | -0.95 | -1.37 | -3.04 | -5.53 | – | -3.31 | +2.07 / -6.90 | -1.40 | 0 | +2.90 | 14 posisi, 5 hari beli |
| `N31X36` Turtle sistem 2 → keluar selepas DUA t | TERLALU AWAL | 91/3 | 6 | -1.01 | -2.02 | -1.39 | -3.39 | – | -1.67 | -1.84 / -0.43 | -1.03 | 0 | +1.79 | 91 posisi, 6 hari beli |
| `N47X36` NR7 + EMA9>EMA21 → keluar selepas DUA  | TERLALU AWAL | 100/10 | 5 | -1.05 | -1.43 | -2.91 | -4.22 | – | -2.53 | -2.55 / -2.53 | -0.99 | 0 | +1.77 | 100 posisi, 5 hari beli |
| `N29X16` PSAR naik + tutup>MA50 → keluar bila s | TERLALU AWAL | 157/57 | 6 | -1.43 | -2.16 | -1.70 | -2.12 | – | -0.65 | -0.70 / -0.54 | +0.11 | 0 | +1.23 | 157 posisi, 6 hari beli |
| `N57X36` ADX bangkit daripada <20 → keluar sele | TERLALU AWAL | 60/6 | 6 | -1.66 | -2.39 | -2.02 | -3.95 | – | -2.43 | -5.02 / +0.95 | -1.89 | 0 | +1.90 | 60 posisi, 6 hari beli |
| `N57X16` ADX bangkit daripada <20 → keluar bila | TERLALU AWAL | 58/4 | 6 | -1.70 | -2.45 | -1.93 | -3.81 | – | -2.21 | -4.94 / +0.95 | -1.76 | 0 | +1.26 | 58 posisi, 6 hari beli |
| `N51X36` BB squeeze + Supertrend → keluar selep | TERLALU AWAL | 6/2 | 4 | -2.25 | -3.76 | -2.77 | -6.03 | – | -5.21 | -3.02 / -6.31 | -2.34 | 0 | +0.95 | 6 posisi, 4 hari beli |
| `N51X16` BB squeeze + Supertrend → keluar bila  | TERLALU AWAL | 6/1 | 4 | -2.34 | -3.88 | -2.77 | -6.03 | – | -5.21 | -3.02 / -6.31 | -2.34 | 0 | +0.84 | 6 posisi, 4 hari beli |
| `N39X36` NR7 kemudian pecah → keluar selepas DU | TERLALU AWAL | 18/5 | 2 | -3.09 | -3.68 | -2.83 | -3.94 | – | -2.21 | -2.21 / – | -3.39 | 0 | +1.50 | 18 posisi, 2 hari beli |
