# Skor Kaedah 0–100 (pangkat maklumat, BUKAN keputusan)

> **Status keputusan (kad skor, harga 2026-11-09):** TERBUKTI 0 · CALON 0 · BELUM CUKUP 223 · GAGAL 0 · NEGATIF 0. Rejim QQQ OFF sejak 2026-10-16. Hanya **TERBUKTI** layak untuk wang sebenar (`laporan/KAD_SKOR.md`); nombor dalam laporan ini BUKAN keputusan dan tidak boleh dibaca sebagai pangkat untuk wang sebenar.

Dijana 2026-11-10 oleh `standard/skor_kaedah.py` (Actions `analisis.yml`, selepas kad skor). Harga pada tutup 2026-11-09; 223 kaedah; 17 hari beli langsung (rejim ON 1, OFF 16). Pradaftar 2026-11-09: `standard/SPEC_SKOR_KAEDAH.md` (berat dan sauh dikunci `ujian/test_skor_kaedah.py::TestKunci`). Rekod analisis sahaja: tiada order, tiada wang sebenar.

## Cara membaca

- **Skor** = min geometri berberat empat tiang (Untung 35 · Tahan 30 · Bukti 25 · Konsisten 10), dikecut ke 50 mengikut data: berat data = hari beli ÷ (hari beli + 20). Kaedah dengan 2 hari beli tidak boleh menjauhi 50. 100 = unggul semua segi; 50 = neutral/tiada bukti; < 50 = lebih buruk daripada neutral.
- **Siling** ikut kad skor: NEGATIF ≤ 20, GANTUNG/BERSARA ≤ 30, GAGAL ≤ 40. Tanda ⌈ = siling terpakai.
- **Satu-satunya status yang membenarkan wang sebenar ialah TERBUKTI dalam `laporan/KAD_SKOR.md`.** Skor tinggi dengan status BELUM CUKUP bermaksud "paling menjanjikan setakat ini", bukan "selamat".
- Deflasi ujian berganda (López de Prado): sauh t Bukti C1 = maks(2.0, E[maks 223 normal]) = 2.80.
- **Semakan kebolehramalan:** belum ada snapshot skor ≥ 7 hari lalu (sejarah bermula 2026-11-09); skor dipercayai sebagai pangkat hanya selepas 8–12 minggu semakan positif.
- Metrik T4 (A2, B1, B2, D1) dikira atas lorong T4 L1 **dipotong pada sesi LANGSUNG pertama** kaedah itu (Mxx 2026-10-16, Nxx/GB 2026-11-03) dan diasas semula; sesi isian bina semula tidak dikira (pindaan 9 Nov 2026 (a)). Lajur "T4 sesi/pul" di bawah ialah potongan itu, bukan lorong penuh `T4_KAEDAH.md`.

## Semua kaedah, susun ikut Skor

| # | Kaedah | Skor | Untung | Tahan | Bukti | Konsisten | Status kad | Hari beli | Posisi/tutup | Jangkaan % | T4 sesi | T4 pul % | T4 pul/|MDD| | Ulcer | t buku | Lift | WFE |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `M33` Supertrend + SMA10 | **66.0** | 95 | 88 | 70 | 85 | BELUM CUKUP | 17 | 204/37 | +2.99 | 17 | +8.34 | +3.12 | 1.4 | +2.31 | – | 7.19 |
| 2 | `M146` 3-Bar Momentum Pattern | **65.8** | 94 | 90 | 71 | 85 | BELUM CUKUP | 16 | 76/28 | +2.18 | 17 | +6.45 | +1.05 | 2.0 | +2.57 | – | 4.00 |
| 3 | `M118` Expansion Pivot (Cooper) | **64.3** | 90 | 88 | 62 | 85 | BELUM CUKUP | 17 | 73/20 | +1.69 | 17 | +10.93 | +4.04 | 0.9 | +1.65 | – | 4.39 |
| 4 | `M133` Bull Hook (Crabel) | **62.8** | 99 | 92 | 59 | 85 | BELUM CUKUP | 12 | 47/19 | +2.23 | 17 | +6.49 | +1.56 | 1.6 | +1.51 | – | 15.72 |
| 5 | `M25` VWAP Wave (proksi harian) | **61.6** | 83 | 81 | 61 | 80 | BELUM CUKUP | 16 | 169/82 | +0.84 | 17 | +5.74 | +0.99 | 3.0 | +1.04 | – | 6.38 |
| 6 | `M124` 'Last' Stochastic Technique (C | **61.6** | 80 | 78 | 63 | 85 | BELUM CUKUP | 17 | 344/163 | +0.90 | 17 | +6.36 | +1.39 | 2.4 | +1.11 | – | 2.00 |
| 7 | `M111` Sistem Volatiliti Wilder | **60.7** | 84 | 66 | 64 | 85 | BELUM CUKUP | 17 | 232/72 | +1.48 | 17 | +3.92 | +0.58 | 3.5 | +1.38 | – | 2.80 |
| 8 | `M151` Outside Bar Failure | **60.4** | 75 | 84 | 58 | 85 | BELUM CUKUP | 16 | 82/45 | +0.41 | 17 | +8.39 | +6.90 | 0.5 | +0.91 | – | 1.76 |
| 9 | `M105` Supertrend tulen | **60.4** | 85 | 62 | 66 | 85 | BELUM CUKUP | 17 | 320/88 | +1.79 | 17 | +1.31 | +0.18 | 2.9 | +1.50 | – | 3.13 |
| 10 | `M91` Stochastic Pop (Bernstein/Stec | **60.3** | 93 | 78 | 58 | 85 | BELUM CUKUP | 12 | 34/12 | +1.67 | 17 | +10.08 | +1.29 | 2.4 | +1.54 | – | 5.22 |
| 11 | `M142` Pecahan volum dari dasar (底部放量 | **59.6** | 85 | 88 | 48 | 85 | BELUM CUKUP | 13 | 40/5 | +3.22 | 15 | +3.80 | +0.79 | 1.9 | +0.90 | – | 1.50 |
| 12 | `M10` EMA3 + CCI + MACD | **59.6** | 78 | 71 | 58 | 85 | BELUM CUKUP | 17 | 102/47 | +0.71 | 17 | +9.74 | +1.85 | 1.8 | +0.79 | – | 2.20 |
| 13 | `M13` Garis Trend Action/Safety Line | **59.6** | 74 | 74 | 58 | 85 | BELUM CUKUP | 17 | 662/407 | +0.29 | 17 | +8.69 | +2.44 | 1.3 | +0.52 | – | 1.02 |
| 14 | `M145` Yum-Yum Continuation | **59.3** | 76 | 75 | 58 | 72 | BELUM CUKUP | 17 | 280/54 | +0.91 | 17 | +4.51 | +2.07 | 1.4 | +0.76 | – | 0.58 |
| 15 | `M93` Bollinger Kaedah II: %b + MFI | **58.8** | 81 | 59 | 62 | 85 | BELUM CUKUP | 17 | 247/69 | +1.55 | 17 | +0.71 | +0.11 | 2.3 | +1.19 | – | 1.50 |
| 16 | `M23` Breitstein Kapitulasi + Kesina | **58.4** | 67 | 71 | 61 | 84 | BELUM CUKUP | 17 | 111/66 | +0.02 | 17 | +2.56 | +0.50 | 2.1 | +1.12 | – | 4.60 |
| 17 | `M137` Livermore System | **58.1** | 68 | 73 | 56 | 85 | BELUM CUKUP | 17 | 151/53 | +0.06 | 17 | +6.09 | +1.03 | 2.4 | +0.62 | – | 1.24 |
| 18 | `M15` Break & Retest + Henti ATR | **57.9** | 87 | 59 | 64 | 45 | BELUM CUKUP | 17 | 265/145 | +1.88 | 17 | -1.60 | -0.22 | 2.9 | +1.27 | – | 2.36 |
| 19 | `M89` Chande 65sma-3cc | **57.9** | 67 | 70 | 58 | 85 | BELUM CUKUP | 17 | 151/79 | +0.08 | 17 | +3.64 | +0.76 | 2.1 | +0.70 | – | 1.83 |
| 20 | `M74` Lulus Baharu Trend Template Mi | **57.6** | 68 | 74 | 54 | 77 | BELUM CUKUP | 17 | 82/50 | -0.02 | 17 | +3.29 | +0.79 | 2.3 | +0.41 | – | 0.73 |
| 21 | `M160` Measured Move Up | **57.3** | 61 | 75 | 61 | 85 | BELUM CUKUP | 15 | 85/44 | -0.40 | 17 | +4.63 | +0.99 | 2.2 | +1.28 | – | 10.26 |
| 22 | `M100` Bulkowski Segi Empat & Segi Ti | **57.2** | 66 | 75 | 55 | 85 | BELUM CUKUP | 14 | 58/39 | +0.36 | 17 | +4.05 | +0.93 | 2.1 | +0.70 | – | 3.48 |
| 23 | `M80` Radge Saluran Purata Bergerak  | **56.6** | 82 | 54 | 65 | 45 | BELUM CUKUP | 17 | 252/50 | +2.06 | 17 | -1.47 | -0.21 | 3.5 | +1.60 | – | 1.79 |
| 24 | `M158` Doubly Adaptive Profit Targets | **56.6** | 80 | 57 | 64 | 45 | BELUM CUKUP | 17 | 335/123 | +1.50 | 17 | -0.55 | -0.09 | 2.4 | +1.20 | – | 3.08 |
| 25 | `M139` 均线首次粘合向上发散 (MA berhimpun kali  | **56.5** | 66 | 67 | 52 | 85 | BELUM CUKUP | 17 | 69/17 | +0.16 | 17 | +5.56 | +1.11 | 1.8 | +0.52 | – | 1.76 |
| 26 | `M05` MACD Divergence + Pengesahan | **56.4** | 72 | 76 | 48 | 73 | BELUM CUKUP | 13 | 38/12 | +0.59 | 17 | +4.61 | +1.36 | 1.4 | +0.31 | – | 0.61 |
| 27 | `M92` CCI-50 | **56.4** | 68 | 60 | 58 | 82 | BELUM CUKUP | 17 | 471/296 | +0.57 | 17 | +0.93 | +0.16 | 2.3 | +0.52 | – | 0.92 |
| 28 | `M88` O'Neil Shakeout +3 | **56.0** | 70 | 65 | 52 | 82 | BELUM CUKUP | 14 | 54/27 | +0.28 | 17 | +5.27 | +0.63 | 3.0 | +0.48 | – | 0.89 |
| 29 | `M30` BB Free Bar + Himpitan 50/2.5 | **55.7** | 75 | 53 | 63 | 53 | BELUM CUKUP | 17 | 217/67 | +1.11 | 17 | +0.91 | +0.12 | 4.8 | +1.27 | – | 2.21 |
| 30 | `M70` Pecahan Hari Dalam | **55.4** | 66 | 71 | 56 | 41 | BELUM CUKUP | 17 | 372/291 | -0.05 | 17 | +2.76 | +0.57 | 2.4 | +0.32 | – | 0.87 |
| 31 | `M159` Heikin-Ashi Trend | **54.5** | 65 | 72 | 53 | 35 | BELUM CUKUP | 17 | 1414/1137 | -0.11 | 17 | +6.32 | +1.03 | 3.8 | +0.01 | – | 0.04 |
| 32 | `M46` Jurang Naik Boleh Beli (Buyabl | **54.4** | 65 | 70 | 50 | 77 | BELUM CUKUP | 10 | 33/16 | -0.05 | 17 | +1.96 | +0.40 | 1.7 | +0.53 | – | 1.00 |
| 33 | `M129` Wick Play | **54.3** | 74 | 61 | 49 | 85 | BELUM CUKUP | 9 | 23/9 | +0.50 | 17 | +5.96 | +2.11 | 1.0 | +0.67 | – | 2.93 |
| 34 | `M02` MACD + SMA200 | **54.3** | 63 | 65 | 50 | 55 | BELUM CUKUP | 17 | 105/54 | -0.30 | 17 | +10.49 | +2.37 | 1.7 | -0.07 | – | -0.38 |
| 35 | `M48` Cooper 1-2-3-4 | **53.9** | 62 | 56 | 52 | 85 | BELUM CUKUP | 14 | 45/15 | -0.08 | 17 | +8.12 | +1.49 | 2.1 | +0.70 | – | 1.96 |
| 36 | `N68X36` Bullish engulfing + EMA21 → ke | **53.8** | 86 | 90 | 53 | 50 | BELUM CUKUP | 4 | 35/5 | +1.61 | 4 | +3.88 | +1.80 | 1.5 | +1.89 | – | – |
| 37 | `M117` Landry Pullback (high 2 bulan) | **53.6** | 79 | 47 | 56 | 45 | BELUM CUKUP | 14 | 81/17 | +1.79 | 17 | -4.67 | -0.59 | 3.3 | +1.14 | – | 1.25 |
| 38 | `M131` Ross Hook (Joe Ross) | **53.6** | 61 | 54 | 60 | 54 | BELUM CUKUP | 17 | 247/102 | +0.19 | 17 | -0.90 | -0.14 | 2.8 | +0.77 | – | 1.72 |
| 39 | `M21` Marius 3 Persediaan (Pecahan+J | **53.5** | 88 | 71 | 46 | 58 | BELUM CUKUP | 5 | 5/2 | +1.58 | 9 | +0.83 | +0.41 | 1.2 | +1.37 | – | 2.78 |
| 40 | `N68X16` Bullish engulfing + EMA21 → ke | **53.4** | 80 | 89 | 50 | 50 | BELUM CUKUP | 4 | 36/6 | +1.32 | 4 | +4.65 | +2.25 | 1.3 | +1.52 | – | – |
| 41 | `M132` Ascending Scallop (Bulkowski) | **52.6** | 47 | 65 | 52 | 85 | BELUM CUKUP | 15 | 88/34 | -1.07 | 17 | +3.53 | +0.94 | 2.1 | +0.27 | – | 2.25 |
| 42 | `M18` EMA9/21 Pullback | **52.6** | 66 | 48 | 57 | 45 | BELUM CUKUP | 17 | 315/207 | +0.54 | 17 | -2.79 | -0.46 | 4.1 | +0.49 | – | 1.69 |
| 43 | `M150` Trend Bar Failure (Brooks) | **52.3** | 67 | 50 | 52 | 43 | BELUM CUKUP | 16 | 81/39 | +0.78 | 17 | -3.06 | -0.55 | 2.3 | +0.29 | – | 0.93 |
| 44 | `M35` Pocket Pivot Morales & Kacher | **52.2** | 62 | 48 | 57 | 45 | BELUM CUKUP | 17 | 291/200 | +0.12 | 17 | -1.74 | -0.19 | 4.8 | +0.48 | – | 2.68 |
| 45 | `N45X16` Undur EMA21 cerun positif → ke | **52.1** | 64 | 82 | 48 | 50 | BELUM CUKUP | 4 | 74/26 | +0.01 | 4 | +7.13 | +10.00 | 0.0 | +0.77 | – | – |
| 46 | `M37` Weinstein Peringkat 2 | **52.0** | 74 | 94 | 34 | 70 | BELUM CUKUP | 3 | 7/0 | +1.32 | 11 | +1.07 | +2.11 | 0.2 | +0.49 | – | 0.50 |
| 47 | `N64X36` Episodic pivot → keluar selepa | **51.9** | 85 | 74 | 33 | 50 | BELUM CUKUP | 4 | 39/2 | +1.65 | 4 | +1.13 | +0.28 | 2.7 | -0.08 | – | – |
| 48 | `N53X36` Supertrend + ADX>25 → keluar s | **51.8** | 72 | 66 | 47 | 50 | BELUM CUKUP | 4 | 79/13 | +1.06 | 4 | +0.73 | +0.18 | 2.8 | +0.88 | – | – |
| 49 | `N64X14` Episodic pivot → keluar bila r | **51.8** | 89 | 73 | 30 | 50 | BELUM CUKUP | 4 | 39/0 | +2.10 | 4 | +0.35 | +0.09 | 2.5 | +0.00 | – | – |
| 50 | `M106` DMI Wilder | **51.8** | 64 | 45 | 58 | 45 | BELUM CUKUP | 15 | 100/53 | +0.61 | 17 | -2.24 | -0.49 | 2.5 | +0.87 | – | 1.58 |
| 51 | `M77` Undercut & Rally pada Purata B | **51.8** | 52 | 68 | 44 | 55 | BELUM CUKUP | 15 | 49/33 | -0.74 | 17 | +1.95 | +0.62 | 1.6 | -0.61 | – | -0.85 |
| 52 | `N124X15` Episodic pivot gap 8-10% → eko | **51.7** | 89 | 72 | 31 | 50 | BELUM CUKUP | 4 | 36/0 | +2.83 | 4 | +0.12 | +0.02 | 4.0 | +0.04 | – | – |
| 53 | `N64X17` Episodic pivot → keluar bila a | **51.7** | 77 | 73 | 36 | 50 | BELUM CUKUP | 4 | 39/7 | +1.05 | 4 | +1.44 | +0.36 | 2.6 | -0.21 | – | – |
| 54 | `N64X16` Episodic pivot → keluar bila s | **51.6** | 82 | 70 | 34 | 50 | BELUM CUKUP | 4 | 39/3 | +1.50 | 4 | +0.35 | +0.09 | 2.5 | -0.13 | – | – |
| 55 | `M134` First Kiss After Daylight (Lan | **51.5** | 58 | 48 | 55 | 56 | BELUM CUKUP | 14 | 39/16 | +0.30 | 17 | -1.35 | -0.19 | 3.0 | +0.96 | – | 1.14 |
| 56 | `M04` BB Squeeze Breakout | **51.4** | 54 | 46 | 57 | 62 | BELUM CUKUP | 16 | 142/47 | -0.30 | 17 | +1.42 | +0.18 | 4.0 | +0.72 | – | 1.24 |
| 57 | `N124X36` Episodic pivot gap 8-10% → kel | **51.3** | 82 | 60 | 36 | 50 | BELUM CUKUP | 4 | 36/5 | +1.70 | 4 | -1.79 | -0.36 | 3.5 | -0.00 | – | – |
| 58 | `N53X17` Supertrend + ADX>25 → keluar b | **51.3** | 70 | 69 | 37 | 50 | BELUM CUKUP | 4 | 66/0 | +1.02 | 4 | +0.80 | +0.21 | 2.8 | +0.83 | – | – |
| 59 | `M153` Range Leader | **51.3** | 57 | 47 | 58 | 45 | BELUM CUKUP | 17 | 1053/905 | +0.08 | 17 | -0.97 | -0.10 | 5.9 | +0.56 | – | 3.25 |
| 60 | `N45X36` Undur EMA21 cerun positif → ke | **51.2** | 58 | 76 | 43 | 50 | BELUM CUKUP | 4 | 67/18 | +0.16 | 4 | +1.88 | +0.90 | 1.4 | +0.26 | – | – |
| 61 | `N53X16` Supertrend + ADX>25 → keluar b | **51.2** | 66 | 67 | 40 | 50 | BELUM CUKUP | 4 | 71/2 | +0.76 | 4 | +0.55 | +0.15 | 2.7 | +0.74 | – | – |
| 62 | `M51` O'Neil Cawan & Pemegang | **51.0** | 77 | 66 | 42 | 54 | BELUM CUKUP | 2 | 3/0 | +1.02 | 7 | +0.36 | +0.36 | 0.5 | +1.64 | – | 6.56 |
| 63 | `M116` 2/20 EMA Breakout (Landry) | **50.9** | 58 | 43 | 59 | 45 | BELUM CUKUP | 17 | 512/325 | +0.32 | 17 | -1.69 | -0.14 | 6.7 | +0.66 | – | 2.71 |
| 64 | `N07X16` Tiga MA tersusun → keluar bila | **50.7** | 60 | 63 | 40 | 50 | BELUM CUKUP | 4 | 76/8 | +0.53 | 4 | +0.12 | +0.03 | 2.3 | +0.27 | – | – |
| 65 | `N22X36` BB pecah atas + RSI → keluar s | **50.7** | 53 | 61 | 50 | 50 | BELUM CUKUP | 4 | 68/16 | -0.33 | 4 | +1.13 | +0.30 | 2.5 | +1.16 | – | – |
| 66 | `M104` High Tight Flag / Power Play | **50.5** | 78 | 90 | 27 | 65 | BELUM CUKUP | 1 | 1/0 | +14.81 | 2 | +1.50 | +10.00 | 0.0 | – | – | 41.96 |
| 67 | `N37X14` Gap and go → keluar bila rsi14 | **50.5** | 67 | 65 | 31 | 50 | BELUM CUKUP | 4 | 63/2 | +0.60 | 4 | +1.67 | +0.45 | 2.2 | -0.37 | – | – |
| 68 | `N56X17` RSI>50 + ADX>20 → keluar bila  | **50.4** | 66 | 59 | 34 | 50 | BELUM CUKUP | 4 | 76/6 | +0.75 | 4 | -0.86 | -0.17 | 3.3 | -0.33 | – | – |
| 69 | `N19X13` Bawah jalur BB + RSI<30 → kelu | **50.4** | 79 | 55 | 29 | 50 | BELUM CUKUP | 4 | 98/0 | +2.01 | 4 | -2.83 | -0.86 | 2.6 | -0.19 | – | – |
| 70 | `N25X17` Supertrend + EMA + ADX>23 → ke | **50.4** | 64 | 63 | 32 | 50 | BELUM CUKUP | 4 | 69/0 | +0.63 | 4 | -0.15 | -0.03 | 3.3 | +0.18 | – | – |
| 71 | `N28X14` ADX>25 + DI+ > DI- → keluar bi | **50.3** | 68 | 56 | 33 | 50 | BELUM CUKUP | 4 | 95/2 | +1.10 | 4 | -1.63 | -0.27 | 4.2 | -0.12 | – | – |
| 72 | `N36X16` Pocket pivot → keluar bila sup | **50.3** | 50 | 70 | 38 | 50 | BELUM CUKUP | 4 | 114/37 | -0.76 | 4 | +4.25 | +6.13 | 0.4 | -0.51 | – | – |
| 73 | `N24X17` Supertrend(10,3) + ADX>20 → ke | **50.3** | 61 | 63 | 33 | 50 | BELUM CUKUP | 4 | 72/3 | +0.30 | 4 | +0.04 | +0.01 | 2.4 | -0.26 | – | – |
| 74 | `M155` Market Cycle Strategy | **50.3** | 65 | 40 | 56 | 32 | BELUM CUKUP | 17 | 599/214 | +0.74 | 17 | -2.43 | -0.41 | 3.4 | +0.33 | – | 0.58 |
| 75 | `M39` Radge Pecahan Bollinger 100 ha | **50.3** | 39 | 65 | 51 | 58 | BELUM CUKUP | 17 | 215/48 | -1.60 | 17 | +5.57 | +2.32 | 1.2 | +0.05 | – | 0.11 |
| 76 | `N07X36` Tiga MA tersusun → keluar sele | **50.2** | 58 | 56 | 39 | 50 | BELUM CUKUP | 4 | 78/7 | +0.51 | 4 | -0.78 | -0.20 | 2.5 | +0.19 | – | – |
| 77 | `N42X14` Lonjakan volum 2x → keluar bil | **50.2** | 71 | 53 | 31 | 50 | BELUM CUKUP | 4 | 129/3 | +1.23 | 4 | -2.16 | -0.20 | 7.0 | -0.47 | – | – |
| 78 | `N80X36` Tinggi sepanjang masa → keluar | **50.1** | 65 | 54 | 34 | 50 | BELUM CUKUP | 3 | 23/0 | +0.82 | 4 | -0.81 | -0.24 | 2.1 | +0.55 | – | – |
| 79 | `N25X16` Supertrend + EMA + ADX>23 → ke | **50.1** | 58 | 60 | 35 | 50 | BELUM CUKUP | 4 | 72/2 | +0.32 | 4 | -0.62 | -0.13 | 3.3 | +0.07 | – | – |
| 80 | `M143` 장대양봉 이후 눌림목 / 5일선 매매 (Undur ke | **50.1** | 60 | 69 | 30 | 43 | BELUM CUKUP | 9 | 13/1 | +0.67 | 16 | +0.74 | +0.25 | 1.6 | -0.68 | – | -8.24 |
| 81 | `N25X36` Supertrend + EMA + ADX>23 → ke | **50.1** | 54 | 58 | 39 | 50 | BELUM CUKUP | 4 | 75/11 | -0.00 | 4 | -0.56 | -0.13 | 3.2 | +0.02 | – | – |
| 82 | `M08` SMA20 + SMA200 | **50.0** | 55 | 44 | 52 | 47 | BELUM CUKUP | 15 | 156/86 | -0.05 | 17 | -1.68 | -0.31 | 3.9 | +0.02 | – | 0.06 |
| 83 | `M148` Natural Number Method | **49.9** | 42 | 63 | 46 | 55 | BELUM CUKUP | 17 | 181/119 | -1.39 | 17 | +3.06 | +0.62 | 1.9 | -0.79 | – | -2.89 |
| 84 | `N22X16` BB pecah atas + RSI → keluar b | **49.9** | 47 | 55 | 47 | 50 | BELUM CUKUP | 4 | 66/15 | -0.51 | 4 | -0.14 | -0.04 | 2.5 | +0.83 | – | – |
| 85 | `N41X16` CMF20>0 + tutup>EMA20 → keluar | **49.9** | 42 | 70 | 41 | 50 | BELUM CUKUP | 4 | 129/66 | -1.01 | 4 | +2.01 | +0.94 | 1.4 | -0.47 | – | – |
| 86 | `N37X36` Gap and go → keluar selepas DU | **49.9** | 55 | 60 | 33 | 50 | BELUM CUKUP | 4 | 63/9 | -0.37 | 4 | +1.94 | +0.53 | 2.6 | -0.60 | – | – |
| 87 | `N37X17` Gap and go → keluar bila adx14 | **49.9** | 51 | 64 | 34 | 50 | BELUM CUKUP | 4 | 62/16 | -0.62 | 4 | +2.86 | +0.77 | 2.3 | -0.72 | – | – |
| 88 | `N75X17` RSI14 < 40 tanpa penapis → kel | **49.8** | 53 | 57 | 36 | 50 | BELUM CUKUP | 4 | 225/91 | +0.14 | 4 | -1.23 | -0.31 | 2.7 | -1.17 | – | – |
| 89 | `N28X17` ADX>25 + DI+ > DI- → keluar bi | **49.8** | 65 | 56 | 27 | 50 | BELUM CUKUP | 4 | 57/0 | +0.83 | 4 | -1.02 | -0.14 | 4.7 | -0.39 | – | – |
| 90 | `N37X16` Gap and go → keluar bila super | **49.7** | 54 | 56 | 34 | 50 | BELUM CUKUP | 4 | 63/11 | -0.21 | 4 | +1.17 | +0.32 | 2.4 | -0.61 | – | – |
| 91 | `N42X15` Lonjakan volum 2x → ekori Chan | **49.7** | 70 | 53 | 26 | 50 | BELUM CUKUP | 4 | 123/0 | +1.15 | 4 | -1.77 | -0.15 | 7.2 | -0.52 | – | – |
| 92 | `N24X16` Supertrend(10,3) + ADX>20 → ke | **49.7** | 58 | 57 | 31 | 50 | BELUM CUKUP | 4 | 65/2 | +0.22 | 4 | -0.49 | -0.15 | 2.3 | -0.41 | – | – |
| 93 | `N42X36` Lonjakan volum 2x → keluar sel | **49.7** | 57 | 47 | 38 | 50 | BELUM CUKUP | 4 | 138/38 | +0.43 | 4 | -2.15 | -0.29 | 5.1 | -0.60 | – | – |
| 94 | `N42X17` Lonjakan volum 2x → keluar bil | **49.6** | 55 | 48 | 38 | 50 | BELUM CUKUP | 4 | 137/30 | +0.30 | 4 | -2.62 | -0.27 | 6.5 | -0.54 | – | – |
| 95 | `N33X36` Donchian20 + penapis MA200 → k | **49.6** | 53 | 55 | 34 | 50 | BELUM CUKUP | 4 | 51/7 | -0.27 | 4 | -0.76 | -0.21 | 2.4 | -0.45 | – | – |
| 96 | `N56X16` RSI>50 + ADX>20 → keluar bila  | **49.6** | 53 | 47 | 40 | 50 | BELUM CUKUP | 4 | 102/29 | +0.16 | 4 | -2.31 | -0.45 | 4.0 | -0.29 | – | – |
| 97 | `N65X14` Gap 4% + volum + hampir 52w →  | **49.6** | 67 | 55 | 23 | 50 | BELUM CUKUP | 3 | 24/0 | +0.59 | 4 | -1.18 | -0.28 | 3.0 | -0.71 | – | – |
| 98 | `N65X36` Gap 4% + volum + hampir 52w →  | **49.6** | 67 | 55 | 23 | 50 | BELUM CUKUP | 3 | 24/0 | +0.59 | 4 | -1.18 | -0.28 | 3.0 | -0.71 | – | – |
| 99 | `M31` Band Walk (BB 20/2) | **49.5** | 61 | 34 | 58 | 45 | BELUM CUKUP | 17 | 373/65 | +0.68 | 17 | -3.57 | -0.32 | 6.6 | +0.76 | – | 1.30 |
| 100 | `M144` Screw Bar | **49.5** | 61 | 51 | 38 | 26 | BELUM CUKUP | 5 | 8/6 | +0.11 | 15 | +0.10 | +0.04 | 0.9 | +0.09 | – | 0.36 |
| 101 | `N75X14` RSI14 < 40 tanpa penapis → kel | **49.5** | 62 | 52 | 28 | 50 | BELUM CUKUP | 4 | 176/4 | +0.84 | 4 | -2.80 | -0.51 | 4.1 | -0.92 | – | – |
| 102 | `N42X16` Lonjakan volum 2x → keluar bil | **49.5** | 55 | 45 | 38 | 50 | BELUM CUKUP | 4 | 141/37 | +0.37 | 4 | -2.92 | -0.45 | 4.7 | -0.57 | – | – |
| 103 | `N50X14` Mampat + pecah volum 1.5x → ke | **49.5** | 58 | 54 | 27 | 50 | BELUM CUKUP | 3 | 12/0 | +0.31 | 4 | -0.38 | -0.04 | 5.6 | -0.30 | – | – |
| 104 | `N35X36` Pecah 52 minggu tinggi → kelua | **49.5** | 46 | 67 | 28 | 50 | BELUM CUKUP | 3 | 30/0 | -0.39 | 4 | +0.98 | +0.54 | 1.2 | -0.21 | – | – |
| 105 | `N50X17` Mampat + pecah volum 1.5x → ke | **49.3** | 51 | 52 | 29 | 50 | BELUM CUKUP | 3 | 12/1 | -0.29 | 4 | +0.13 | +0.01 | 5.6 | -0.33 | – | – |
| 106 | `M136` Short/Intermediate-term Low (L | **49.2** | 57 | 48 | 56 | 20 | BELUM CUKUP | 17 | 629/243 | +0.03 | 17 | -0.69 | -0.15 | 2.4 | +0.29 | – | 0.17 |
| 107 | `M03` BB Break + Divergence RSI | **49.2** | 47 | 55 | 54 | 27 | BELUM CUKUP | 17 | 333/294 | -0.39 | 17 | +1.07 | +0.17 | 2.7 | +0.10 | – | 0.39 |
| 108 | `N28X36` ADX>25 + DI+ > DI- → keluar se | **49.2** | 50 | 42 | 40 | 50 | BELUM CUKUP | 4 | 137/60 | +0.19 | 4 | -2.69 | -0.43 | 4.6 | -0.47 | – | – |
| 109 | `N33X16` Donchian20 + penapis MA200 → k | **49.2** | 47 | 57 | 31 | 50 | BELUM CUKUP | 4 | 51/5 | -0.61 | 4 | -0.10 | -0.03 | 2.3 | -0.59 | – | – |
| 110 | `N22X14` BB pecah atas + RSI → keluar b | **49.2** | 47 | 49 | 37 | 50 | BELUM CUKUP | 4 | 73/4 | -0.44 | 4 | -0.83 | -0.18 | 3.1 | +0.19 | – | – |
| 111 | `N66X36` 52w tinggi + pengesahan 1% → k | **49.2** | 53 | 48 | 29 | 50 | BELUM CUKUP | 3 | 28/1 | +0.10 | 3 | -1.55 | -0.37 | 3.4 | -0.31 | – | – |
| 112 | `M07` Qullamaggie Breakout | **49.2** | 27 | 64 | 27 | 15 | BELUM CUKUP | 1 | 1/1 | -2.53 | 17 | -0.25 | -0.21 | 0.6 | -0.22 | – | -1.12 |
| 113 | `N73X13` Tutup bawah jalur bawah BB(20, | **49.1** | 56 | 56 | 24 | 50 | BELUM CUKUP | 4 | 131/0 | +0.30 | 4 | -1.05 | -0.17 | 3.6 | -0.70 | – | – |
| 114 | `N75X13` RSI14 < 40 tanpa penapis → kel | **49.1** | 54 | 61 | 22 | 50 | BELUM CUKUP | 4 | 115/0 | +0.15 | 4 | -0.20 | -0.05 | 2.5 | -0.94 | – | – |
| 115 | `N75X15` RSI14 < 40 tanpa penapis → eko | **49.1** | 54 | 61 | 22 | 50 | BELUM CUKUP | 4 | 115/0 | +0.15 | 4 | -0.20 | -0.05 | 2.5 | -0.94 | – | – |
| 116 | `M27` Price Action 4 Tiang | **49.1** | 49 | 41 | 46 | 15 | BELUM CUKUP | 2 | 547/432 | -0.61 | 17 | -2.69 | -0.52 | 2.9 | -0.03 | – | -0.09 |
| 117 | `N33X14` Donchian20 + penapis MA200 → k | **49.0** | 47 | 54 | 30 | 50 | BELUM CUKUP | 4 | 60/1 | -0.57 | 4 | -0.46 | -0.11 | 2.8 | -0.33 | – | – |
| 118 | `N39X36` NR7 kemudian pecah → keluar se | **49.0** | 20 | 42 | 22 | 50 | BELUM CUKUP | 1 | 16/4 | -3.11 | 3 | -0.08 | -0.02 | 2.6 | -1.17 | – | – |
| 119 | `N57X36` ADX bangkit daripada <20 → kel | **48.9** | 41 | 58 | 32 | 50 | BELUM CUKUP | 4 | 46/3 | -0.95 | 4 | +1.21 | +0.36 | 2.3 | -0.38 | – | – |
| 120 | `N40X36` OBV tinggi baharu + MA50 → kel | **48.9** | 43 | 48 | 37 | 50 | BELUM CUKUP | 4 | 25/7 | -0.77 | 4 | -1.09 | -0.23 | 3.3 | -0.09 | – | – |
| 121 | `N57X16` ADX bangkit daripada <20 → kel | **48.9** | 41 | 57 | 32 | 50 | BELUM CUKUP | 4 | 44/4 | -0.96 | 4 | +1.21 | +0.36 | 2.3 | -0.40 | – | – |
| 122 | `N28X16` ADX>25 + DI+ > DI- → keluar bi | **48.9** | 46 | 44 | 38 | 50 | BELUM CUKUP | 4 | 144/60 | -0.13 | 4 | -2.64 | -0.42 | 4.5 | -0.74 | – | – |
| 123 | `N74X16` MACD atas garis isyarat (keada | **48.9** | 46 | 40 | 42 | 50 | BELUM CUKUP | 4 | 200/118 | -0.13 | 4 | -3.88 | -0.53 | 5.8 | -0.52 | – | – |
| 124 | `M107` Golden Cross SMA50/200 | **48.8** | 52 | 52 | 46 | 26 | BELUM CUKUP | 14 | 28/7 | -0.10 | 17 | -0.17 | -0.05 | 1.6 | +0.22 | – | 0.38 |
| 125 | `N40X16` OBV tinggi baharu + MA50 → kel | **48.8** | 41 | 47 | 38 | 50 | BELUM CUKUP | 4 | 33/14 | -1.05 | 4 | -0.91 | -0.17 | 3.4 | -0.14 | – | – |
| 126 | `M45` High 52 Minggu (George & Hwang | **48.8** | 17 | 41 | 29 | 15 | BELUM CUKUP | 1 | 2/1 | -4.72 | 6 | -0.92 | -0.51 | 1.1 | -0.02 | – | -0.13 |
| 127 | `M01` Bollinger Band + RSI | **48.7** | 74 | 44 | 44 | 15 | BELUM CUKUP | 17 | 108/17 | +1.66 | 17 | -3.66 | -0.34 | 4.4 | -0.42 | – | -2.01 |
| 128 | `M41` FW Penyatuan Mingguan | **48.7** | 48 | 35 | 44 | 45 | BELUM CUKUP | 4 | 63/8 | +0.35 | 16 | -5.21 | -0.63 | 4.0 | +0.78 | – | 1.39 |
| 129 | `N24X36` Supertrend(10,3) + ADX>20 → ke | **48.7** | 48 | 38 | 38 | 50 | BELUM CUKUP | 4 | 83/22 | -0.34 | 4 | -2.23 | -0.49 | 3.3 | -0.42 | – | – |
| 130 | `N36X36` Pocket pivot → keluar selepas  | **48.7** | 43 | 45 | 36 | 50 | BELUM CUKUP | 4 | 113/38 | -0.92 | 4 | +0.09 | +0.02 | 3.2 | -0.87 | – | – |
| 131 | `N76X36` Tutup > MA50 (penapis trend tu | **48.7** | 46 | 40 | 36 | 50 | BELUM CUKUP | 4 | 82/28 | -0.35 | 4 | -2.79 | -0.51 | 4.1 | -0.70 | – | – |
| 132 | `N54X16` Supertrend + RSI>50 → keluar b | **48.5** | 51 | 41 | 27 | 50 | BELUM CUKUP | 4 | 70/3 | +0.16 | 4 | -3.02 | -0.38 | 5.4 | -0.92 | – | – |
| 133 | `N08X36` tutup>EMA20 tidak terlalu jauh | **48.5** | 37 | 45 | 38 | 50 | BELUM CUKUP | 4 | 165/94 | -1.11 | 4 | -0.35 | -0.06 | 3.6 | -0.96 | – | – |
| 134 | `M138` 直升机空中加油 (Helikopter isi minyak | **48.5** | 36 | 56 | 24 | 15 | BELUM CUKUP | 2 | 2/0 | -0.86 | 10 | -0.13 | -0.20 | 0.2 | -0.50 | – | -0.70 |
| 135 | `M84` Jarak purata bergerak MAD 21/2 | **48.5** | 15 | 17 | 33 | 15 | BELUM CUKUP | 1 | 58/35 | -3.70 | 6 | -7.13 | -0.91 | 5.6 | -0.71 | – | -3.04 |
| 136 | `N08X16` tutup>EMA20 tidak terlalu jauh | **48.4** | 39 | 41 | 39 | 50 | BELUM CUKUP | 4 | 192/100 | -0.88 | 4 | -1.45 | -0.46 | 2.6 | -0.82 | – | – |
| 137 | `N47X16` NR7 + EMA9>EMA21 → keluar bila | **48.4** | 39 | 51 | 29 | 50 | BELUM CUKUP | 4 | 41/9 | -0.42 | 4 | -1.64 | -0.38 | 3.0 | -1.12 | – | – |
| 138 | `N27X16` Ichimoku atas awan → keluar bi | **48.3** | 37 | 53 | 29 | 50 | BELUM CUKUP | 4 | 88/21 | -1.01 | 4 | -0.36 | -0.12 | 2.0 | -1.41 | – | – |
| 139 | `M94` Pecutan Momentum (Chen, Yu & W | **48.3** | 13 | 13 | 16 | 15 | BELUM CUKUP | 1 | 33/0 | -6.98 | 6 | -7.08 | -0.60 | 7.7 | -1.21 | – | -5.48 |
| 140 | `M32` Momentum Burst | **48.2** | 60 | 29 | 51 | 45 | BELUM CUKUP | 11 | 51/32 | +0.19 | 17 | -4.31 | -0.39 | 6.4 | +0.38 | – | 1.15 |
| 141 | `N41X36` CMF20>0 + tutup>EMA20 → keluar | **48.2** | 34 | 44 | 39 | 50 | BELUM CUKUP | 4 | 108/64 | -1.34 | 4 | -0.48 | -0.10 | 3.2 | -0.69 | – | – |
| 142 | `N36X14` Pocket pivot → keluar bila rsi | **48.2** | 44 | 37 | 31 | 50 | BELUM CUKUP | 4 | 113/6 | -0.54 | 4 | -2.91 | -0.43 | 4.5 | -0.66 | – | – |
| 143 | `M96` Momo India: Ranking Sharpe 3/6 | **48.2** | 14 | 11 | 9 | 15 | BELUM CUKUP | 1 | 6/5 | -12.74 | 6 | -7.61 | -1.00 | 5.1 | -5.12 | – | -14.74 |
| 144 | `N38X36` VCP pecah → keluar selepas DUA | **48.1** | 39 | 47 | 28 | 50 | BELUM CUKUP | 4 | 15/4 | -0.84 | 4 | -1.32 | -0.41 | 2.3 | -0.96 | – | – |
| 145 | `N76X16` Tutup > MA50 (penapis trend tu | **48.1** | 34 | 48 | 33 | 50 | BELUM CUKUP | 4 | 129/57 | -1.32 | 4 | -0.31 | -0.09 | 2.3 | -1.35 | – | – |
| 146 | `M36` Turtle 55/20 | **48.0** | 47 | 39 | 56 | 40 | BELUM CUKUP | 17 | 304/145 | -0.48 | 17 | -2.57 | -0.22 | 6.3 | +0.33 | – | 0.82 |
| 147 | `M127` Slingshot Bullish | **47.8** | 48 | 57 | 48 | 15 | BELUM CUKUP | 15 | 94/69 | -1.14 | 17 | +0.84 | +0.12 | 2.9 | -0.46 | – | -0.69 |
| 148 | `M68` Kell Base n' Break | **47.7** | 30 | 53 | 47 | 85 | BELUM CUKUP | 12 | 41/11 | -1.88 | 17 | +1.25 | +0.28 | 1.6 | +0.26 | – | 1.97 |
| 149 | `M130` 多方炮 (dua lilin hijau mengapit  | **47.7** | 44 | 35 | 42 | 37 | BELUM CUKUP | 6 | 9/3 | -0.23 | 15 | +0.03 | +0.01 | 2.4 | +0.70 | – | 0.72 |
| 150 | `M78` Alvarez Pecahan Mingguan DTAYS | **47.7** | 18 | 25 | 42 | 24 | BELUM CUKUP | 2 | 73/39 | -1.83 | 16 | -7.77 | -0.75 | 5.9 | +0.07 | – | 0.29 |
| 151 | `N27X36` Ichimoku atas awan → keluar se | **47.6** | 36 | 38 | 28 | 50 | BELUM CUKUP | 4 | 59/5 | -0.90 | 4 | -2.61 | -0.60 | 3.2 | -0.95 | – | – |
| 152 | `N31X36` Turtle sistem 2 → keluar selep | **47.6** | 36 | 43 | 24 | 50 | BELUM CUKUP | 4 | 71/0 | -1.11 | 4 | -1.21 | -0.33 | 2.6 | -0.75 | – | – |
| 153 | `M149` 3-Step Pullback | **47.5** | 49 | 35 | 56 | 33 | BELUM CUKUP | 15 | 151/52 | -0.16 | 17 | -4.20 | -0.39 | 5.0 | +0.67 | – | 0.61 |
| 154 | `N09X36` Undur EMA10 + penapis EMA50 →  | **47.5** | 26 | 45 | 34 | 50 | BELUM CUKUP | 4 | 88/25 | -1.63 | 4 | -0.65 | -0.17 | 2.6 | -0.94 | – | – |
| 155 | `N06X36` Golden cross MA50/MA200 → kelu | **47.5** | 23 | 48 | 22 | 50 | BELUM CUKUP | 3 | 8/2 | -1.78 | 4 | -1.33 | -0.33 | 2.8 | -1.25 | – | – |
| 156 | `M115` Bow Tie (Landry) | **47.4** | 35 | 44 | 48 | 45 | BELUM CUKUP | 9 | 33/18 | -1.48 | 17 | -3.12 | -0.40 | 3.1 | +0.38 | – | 2.39 |
| 157 | `N55X13` BB + RSI + ADX>20 → keluar bil | **47.3** | 40 | 42 | 18 | 50 | BELUM CUKUP | 4 | 45/0 | -0.40 | 4 | -3.53 | -0.77 | 3.7 | -1.42 | – | – |
| 158 | `N56X36` RSI>50 + ADX>20 → keluar selep | **47.2** | 32 | 31 | 33 | 50 | BELUM CUKUP | 4 | 93/31 | -0.84 | 4 | -4.76 | -0.65 | 5.8 | -1.07 | – | – |
| 159 | `M140` 猎豹出击 (Serangan Cheetah) | **47.1** | 50 | 47 | 38 | 15 | BELUM CUKUP | 9 | 38/12 | -0.10 | 17 | -1.69 | -0.27 | 2.5 | -0.72 | – | -1.04 |
| 160 | `N54X36` Supertrend + RSI>50 → keluar s | **47.1** | 33 | 29 | 32 | 50 | BELUM CUKUP | 4 | 90/28 | -0.94 | 4 | -4.60 | -0.57 | 6.2 | -1.11 | – | – |
| 161 | `N51X36` BB squeeze + Supertrend → kelu | **47.1** | 20 | 38 | 23 | 50 | BELUM CUKUP | 3 | 4/2 | -3.38 | 4 | -1.32 | -0.52 | 1.9 | -1.22 | – | – |
| 162 | `N47X36` NR7 + EMA9>EMA21 → keluar sele | **47.0** | 20 | 34 | 24 | 50 | BELUM CUKUP | 3 | 37/8 | -1.34 | 4 | -4.35 | -0.63 | 5.2 | -1.47 | – | – |
| 163 | `M147` Improved Three-Bar Pullback | **46.9** | 36 | 53 | 42 | 39 | BELUM CUKUP | 14 | 95/29 | -1.52 | 17 | +4.77 | +0.56 | 3.8 | -0.80 | – | -0.55 |
| 164 | `N43X36` Undur EMA8 + penapis MA50 → ke | **46.9** | 23 | 42 | 30 | 50 | BELUM CUKUP | 4 | 76/16 | -1.86 | 4 | -0.65 | -0.17 | 2.7 | -1.24 | – | – |
| 165 | `N119X13` 3 tutup turun berturut → kelua | **46.9** | 35 | 33 | 22 | 50 | BELUM CUKUP | 4 | 129/6 | -0.10 | 4 | -7.37 | -0.89 | 7.2 | -1.74 | – | – |
| 166 | `N51X16` BB squeeze + Supertrend → kelu | **46.9** | 16 | 41 | 25 | 50 | BELUM CUKUP | 3 | 4/1 | -2.63 | 4 | -1.00 | -0.39 | 1.8 | -0.78 | – | – |
| 167 | `M14` Walking with the Whales | **46.6** | 54 | 38 | 53 | 15 | BELUM CUKUP | 17 | 820/547 | -0.00 | 17 | -6.14 | -0.58 | 5.5 | -0.05 | – | -0.10 |
| 168 | `N29X36` PSAR naik + tutup>MA50 → kelua | **46.6** | 28 | 25 | 32 | 50 | BELUM CUKUP | 4 | 83/26 | -1.08 | 4 | -7.15 | -0.74 | 7.4 | -1.11 | – | – |
| 169 | `M20` EMA10/15 Crossover + Sudut | **46.5** | 42 | 48 | 47 | 23 | BELUM CUKUP | 17 | 381/323 | -1.04 | 17 | -1.00 | -0.17 | 2.6 | -0.71 | – | -5.29 |
| 170 | `M49` Ichimoku (Tutup Atas Awan + Te | **46.5** | 48 | 45 | 51 | 15 | BELUM CUKUP | 17 | 253/138 | -0.81 | 17 | -1.14 | -0.17 | 3.1 | -0.22 | – | -0.32 |
| 171 | `M125` 2-Bar Breakout | **46.5** | 49 | 42 | 52 | 15 | BELUM CUKUP | 17 | 895/403 | -0.50 | 17 | -0.58 | -0.09 | 2.5 | -0.08 | – | -0.05 |
| 172 | `N119X15` 3 tutup turun berturut → ekori | **46.5** | 33 | 38 | 14 | 50 | BELUM CUKUP | 4 | 37/0 | -0.42 | 4 | -4.60 | -0.68 | 5.4 | -1.85 | – | – |
| 173 | `M64` O'Neil Tiga Minggu Ketat | **46.5** | 23 | 24 | 27 | 15 | BELUM CUKUP | 3 | 3/1 | -10.36 | 17 | -3.06 | -0.80 | 2.0 | -0.79 | – | -11.27 |
| 174 | `M34` Carter TTM Squeeze | **46.2** | 44 | 36 | 50 | 34 | BELUM CUKUP | 16 | 94/46 | -0.79 | 17 | -1.19 | -0.16 | 3.4 | -0.02 | – | -0.07 |
| 175 | `M38` Darvas Kotak | **46.1** | 16 | 32 | 34 | 49 | BELUM CUKUP | 4 | 23/1 | -2.25 | 16 | -2.21 | -0.22 | 3.8 | +0.20 | – | 1.24 |
| 176 | `M157` Consolidation Pivot Breakout ( | **46.0** | 21 | 37 | 28 | 15 | BELUM CUKUP | 4 | 4/3 | -4.95 | 14 | -1.96 | -0.67 | 1.1 | -0.83 | – | -2.99 |
| 177 | `N16X13` RSI2<10 tanpa penapis → keluar | **46.0** | 25 | 24 | 23 | 50 | BELUM CUKUP | 4 | 109/3 | -0.94 | 4 | -8.13 | -0.90 | 7.0 | -1.45 | – | – |
| 178 | `M102` Stockbee SLTB | **45.8** | 46 | 41 | 52 | 15 | BELUM CUKUP | 17 | 319/237 | -0.93 | 17 | -2.64 | -0.25 | 5.3 | -0.13 | – | -0.39 |
| 179 | `M54` IBD Power Trend | **45.8** | 43 | 43 | 52 | 15 | BELUM CUKUP | 16 | 195/100 | -0.98 | 17 | -0.12 | -0.01 | 5.4 | -0.11 | – | -0.28 |
| 180 | `N113X36` 80-20 bar (sisi beli) → keluar | **45.8** | 18 | 23 | 32 | 50 | BELUM CUKUP | 4 | 111/51 | -1.72 | 4 | -4.84 | -0.70 | 5.8 | -1.41 | – | – |
| 181 | `N29X16` PSAR naik + tutup>MA50 → kelua | **45.7** | 15 | 29 | 29 | 50 | BELUM CUKUP | 4 | 105/41 | -2.18 | 4 | -4.81 | -0.65 | 5.6 | -1.62 | – | – |
| 182 | `N48X36` Inside day pecah → keluar sele | **45.7** | 17 | 24 | 31 | 50 | BELUM CUKUP | 4 | 80/37 | -2.56 | 4 | -5.93 | -0.70 | 6.7 | -1.41 | – | – |
| 183 | `M121` High 2 bull flag (Brooks) | **45.7** | 12 | 21 | 25 | 15 | BELUM CUKUP | 3 | 5/3 | -9.95 | 13 | -4.94 | -0.67 | 3.5 | -1.04 | – | -15.94 |
| 184 | `M06` Minervini VCP Breakout | **45.6** | 37 | 49 | 48 | 21 | BELUM CUKUP | 17 | 71/34 | -1.29 | 17 | -1.41 | -0.22 | 2.6 | -0.18 | – | -0.54 |
| 185 | `M87` IBD Tapak Menaik | **45.6** | 26 | 38 | 42 | 30 | BELUM CUKUP | 7 | 10/6 | -1.93 | 17 | -1.92 | -0.33 | 3.2 | +0.12 | – | 0.49 |
| 186 | `M152` Spike & Ledge | **45.4** | 28 | 48 | 43 | 49 | BELUM CUKUP | 14 | 40/7 | -1.49 | 17 | +0.66 | +0.16 | 2.3 | -0.14 | – | -0.49 |
| 187 | `N113X16` 80-20 bar (sisi beli) → keluar | **45.4** | 15 | 20 | 31 | 50 | BELUM CUKUP | 4 | 112/50 | -1.84 | 4 | -5.34 | -0.76 | 6.0 | -1.48 | – | – |
| 188 | `M12` Parabolic SAR | **45.0** | 41 | 40 | 53 | 15 | BELUM CUKUP | 17 | 335/177 | -1.10 | 17 | -1.50 | -0.26 | 3.0 | -0.05 | – | -0.13 |
| 189 | `M50` Elder Triple Screen | **44.9** | 47 | 32 | 54 | 17 | BELUM CUKUP | 17 | 496/300 | -0.19 | 17 | -8.80 | -0.80 | 6.3 | +0.03 | – | 0.06 |
| 190 | `M128` Inventory Retracement Bar (IRB | **44.8** | 44 | 29 | 53 | 29 | BELUM CUKUP | 17 | 128/73 | -0.50 | 17 | -6.16 | -0.56 | 6.0 | +0.08 | – | 0.46 |
| 191 | `N16X15` RSI2<10 tanpa penapis → ekori  | **44.7** | 15 | 17 | 16 | 50 | BELUM CUKUP | 4 | 106/0 | -1.30 | 4 | -10.85 | -0.93 | 8.7 | -1.66 | – | – |
| 192 | `M99` Three Line Break | **44.3** | 32 | 44 | 52 | 19 | BELUM CUKUP | 17 | 133/84 | -1.98 | 17 | +1.06 | +0.17 | 3.2 | -0.14 | – | -0.65 |
| 193 | `M73` ADX(5) > 40 + Julat Terkecil 6 | **44.3** | 42 | 36 | 50 | 15 | BELUM CUKUP | 17 | 729/556 | +0.08 | 17 | -5.79 | -0.72 | 4.5 | -0.44 | – | -3.34 |
| 194 | `M141` First Thrust (Landry) | **44.3** | 21 | 42 | 34 | 15 | BELUM CUKUP | 7 | 20/8 | -1.99 | 17 | -1.90 | -0.37 | 1.9 | -0.91 | – | -1.99 |
| 195 | `M19` Sneaky Pivot (proksi harian) | **44.1** | 26 | 43 | 48 | 37 | BELUM CUKUP | 16 | 266/219 | -3.44 | 17 | +0.53 | +0.07 | 3.0 | -0.60 | – | -10.15 |
| 196 | `M156` Single Penetration (DiNapoli) | **44.0** | 33 | 34 | 47 | 36 | BELUM CUKUP | 17 | 226/121 | -1.10 | 17 | -4.17 | -0.32 | 5.4 | -0.70 | – | -2.94 |
| 197 | `M55` Guppy GMMA | **43.8** | 38 | 35 | 51 | 15 | BELUM CUKUP | 17 | 183/114 | -1.32 | 17 | -3.51 | -0.40 | 4.3 | -0.26 | – | -0.90 |
| 198 | `M26` Garis Trend Undur 3 Sentuhan + | **43.5** | 34 | 35 | 45 | 15 | BELUM CUKUP | 14 | 56/39 | -0.77 | 17 | -5.33 | -0.66 | 3.3 | -0.47 | – | -0.82 |
| 199 | `M119` 180 Bullish (Cooper) | **43.3** | 37 | 33 | 48 | 15 | BELUM CUKUP | 16 | 114/58 | -0.94 | 17 | -5.17 | -0.48 | 4.3 | -0.38 | – | -1.37 |
| 200 | `M66` IBD Undur Pertama ke Purata 50 | **42.9** | 36 | 32 | 50 | 15 | BELUM CUKUP | 17 | 197/129 | -1.23 | 17 | -4.47 | -0.39 | 5.8 | -0.32 | – | -1.00 |
| 201 | `M44` Tapak Rata IBD | **42.9** | 19 | 42 | 24 | 15 | BELUM CUKUP | 8 | 9/5 | -3.57 | 17 | -3.12 | -0.66 | 2.4 | -1.90 | – | -32.31 |
| 202 | `M161` EMA 10/21 + Supertrend (10,3) | **42.5** | 43 | 20 | 54 | 22 | BELUM CUKUP | 17 | 421/200 | +0.04 | 17 | -10.51 | -0.76 | 8.5 | +0.09 | – | 0.22 |
| 203 | `M95` Nisbah Kebaharuan High 52 Ming | **42.4** | 28 | 37 | 48 | 15 | BELUM CUKUP | 16 | 112/61 | -1.61 | 17 | -3.99 | -0.47 | 3.9 | -0.35 | – | -1.02 |
| 204 | `M120` Reversal New Highs | **42.4** | 27 | 34 | 39 | 15 | BELUM CUKUP | 12 | 18/12 | -2.38 | 17 | -3.54 | -0.54 | 3.1 | -0.73 | – | -4.40 |
| 205 | `M135` 3rd Watch | **42.4** | 12 | 31 | 32 | 15 | BELUM CUKUP | 7 | 12/3 | -5.04 | 17 | -5.79 | -0.73 | 3.1 | -0.83 | – | -5.27 |
| 206 | `M79` Radge: 20% Flipper | **42.1** | 31 | 34 | 47 | 15 | BELUM CUKUP | 17 | 277/74 | -1.23 | 17 | -3.60 | -0.40 | 4.1 | -0.56 | – | -1.11 |
| 207 | `M67` Rayner Teo: Ujian Ketiga pada  | **41.9** | 23 | 32 | 37 | 15 | BELUM CUKUP | 11 | 25/18 | -3.80 | 17 | -6.34 | -0.57 | 5.3 | -1.04 | – | -6.04 |
| 208 | `M82` Arthur Hill Rotasi Sasaran 10% | **41.8** | 34 | 24 | 51 | 21 | BELUM CUKUP | 17 | 544/184 | -0.79 | 17 | -4.95 | -0.31 | 7.0 | -0.28 | – | -1.24 |
| 209 | `M126` Hidden Smash Day (beli, Larry  | **41.6** | 17 | 34 | 35 | 15 | BELUM CUKUP | 10 | 18/11 | -3.79 | 16 | -4.54 | -0.63 | 3.4 | -0.77 | – | -1.58 |
| 210 | `M11` NR7 Breakout + Volume | **41.4** | 29 | 29 | 43 | 15 | BELUM CUKUP | 15 | 95/69 | -1.14 | 17 | -7.04 | -0.59 | 5.7 | -1.02 | – | -1.06 |
| 211 | `M57` Landry Trend Knockout (TKO) | **41.0** | 26 | 34 | 42 | 15 | BELUM CUKUP | 17 | 144/101 | -2.01 | 17 | -3.65 | -0.43 | 4.0 | -1.29 | – | -4.29 |
| 212 | `M28` VWAP Separator + Kiss Pivot | **40.8** | 24 | 30 | 42 | 15 | BELUM CUKUP | 15 | 91/82 | -1.74 | 17 | -6.99 | -0.83 | 5.3 | -1.17 | – | -12.16 |
| 213 | `M123` CCI Correction (Lambert, Chart | **40.7** | 26 | 34 | 39 | 15 | BELUM CUKUP | 17 | 160/142 | -1.41 | 17 | -7.45 | -0.69 | 5.9 | -1.69 | – | -4.17 |
| 214 | `M29` EMA3 + RSI75 + Stokastik | **40.3** | 18 | 32 | 38 | 15 | BELUM CUKUP | 13 | 32/26 | -2.72 | 17 | -8.48 | -0.68 | 6.3 | -1.07 | – | -7.38 |
| 215 | `M122` Moving Momentum (ChartSchool) | **39.5** | 22 | 30 | 41 | 15 | BELUM CUKUP | 17 | 94/56 | -2.36 | 17 | -4.84 | -0.56 | 4.7 | -1.17 | – | -4.29 |
| 216 | `M59` Anjakan Julat RSI | **39.5** | 16 | 25 | 43 | 15 | BELUM CUKUP | 13 | 35/16 | -4.61 | 17 | -4.04 | -0.50 | 3.2 | -0.38 | – | -1.85 |
| 217 | `M101` Bulkowski: Tiga lembah menaik | **38.8** | 14 | 26 | 45 | 15 | BELUM CUKUP | 14 | 43/19 | -3.40 | 17 | -6.89 | -0.56 | 5.2 | -0.20 | – | -0.72 |
| 218 | `M154` HOLP (High of Low Period) | **37.8** | 11 | 20 | 40 | 15 | BELUM CUKUP | 13 | 68/30 | -3.54 | 17 | -10.49 | -0.81 | 6.2 | -0.97 | – | -5.17 |
| 219 | `M09` Volumatic VIDYA Pivot Retest | **37.7** | 7 | 13 | 32 | 15 | BELUM CUKUP | 10 | 26/15 | -4.49 | 17 | -10.49 | -0.89 | 6.7 | -1.54 | – | -11.90 |
| 220 | `M47` Holy Grail Raschke | **36.8** | 6 | 17 | 27 | 15 | BELUM CUKUP | 11 | 22/20 | -4.67 | 17 | -10.11 | -0.98 | 5.1 | -2.29 | – | -27.58 |
| 221 | `M76` Undercut & Rally pada Low Pent | **36.6** | 10 | 27 | 40 | 15 | BELUM CUKUP | 16 | 53/43 | -2.12 | 17 | -8.56 | -0.78 | 5.9 | -1.21 | – | -5.47 |
| 222 | `M81` Bensdorp Long Trend High Momen | **34.6** | 3 | 8 | 44 | 15 | BELUM CUKUP | 12 | 331/135 | -4.11 | 17 | -19.31 | -0.84 | 12.5 | -0.92 | – | -3.58 |
| 223 | `M90` Pring KST | **33.0** | 4 | 12 | 42 | 15 | BELUM CUKUP | 16 | 67/41 | -4.02 | 17 | -13.43 | -0.73 | 9.7 | -0.95 | – | -5.16 |

## Metrik dan sauh (0 · 50 · 100)

| Metrik | Berat | Apa | Sauh | Pakar |
|---|---|---|---|---|
| A1 | 20 | Jangkaan % setiap posisi, ditanda-ke-pasaran, kos ditolak | (-2.0, 0.0, 2.0) | Tharp, Minervini, Radge |
| A2 | 10 | Lebihan mata lorong T4 L1 (potongan LANGSUNG) lawan SPUS, tingkap sama | (-10.0, 0.0, 10.0) | Penanda aras SPUS (repo) |
| A3 | 5 | Payoff untung purata ÷ rugi purata | (0.5, 1.0, 2.0) | Minervini 2:1 |
| B1 | 12 | Pulangan ÷ |MDD| lorong T4 L1 (MAR) | (-1.0, 0.0, 1.0) | Schwager, Radge, Faith |
| B2 | 6 | Ulcer Index ekuiti T4 L1 (%) — kecil lebih baik | (10.0, 5.0, 0.0) | Martin |
| B3 | 6 | CVaR10: purata 10% posisi terburuk (%) | (-24.0, -16.0, -8.0) | Ekor kiri |
| B4 | 6 | tanpa5: jangkaan tanpa 5% posisi terbaik | (-2.0, 0.0, 2.0) | Davey (buang pemenang terbesar) |
| C1 | 12 | t Newey-West buku harian ÷ sauh t (≥ 2.0, dideflasi N ujian) | 0 → 50, sauh → 100 | Carver, Harvey-Liu, López de Prado |
| C2 | 8 | ½ log-skala hari beli (penuh 60) + ½ log-skala posisi ditutup (penuh 100) | – | Tharp 100 dagangan, Radge |
| C3 | 5 | min(hari beli ON, OFF) ÷ 10 | – | Clenow; rejim QQQ (repo) |
| D1 | 4 | K-ratio: t cerun log-ekuiti T4 ÷ √n | (-0.2, 0.0, 0.2) | Kestner |
| D2 | 3 | Lift masuk (lulus BH-FDR → 100/0; selain itu ±4 mata) | – | Plasebo gate (repo) |
| D3 | 3 | Kecekapan jalan-ke-depan: purata harian hadapan ÷ backtest | (0.0, 0.5, 1.0) | Pardo ≥ 50%, Davey |

Metrik tiada data = 50 (neutral). Kadar menang, median, rugi purata dan rugi terbesar sengaja TIDAK dimasukkan (pengiraan dua kali; pelajaran laporan KPI lama). Jangan ubah berat atau sauh selepas melihat data: dikunci oleh ujian unit dan memerlukan pradaftar bertarikh baharu.

