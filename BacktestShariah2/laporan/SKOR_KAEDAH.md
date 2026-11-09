# Skor Kaedah 0–100 (pangkat maklumat, BUKAN keputusan)

> **Status keputusan (kad skor, harga 2026-11-06):** TERBUKTI 0 · CALON 0 · BELUM CUKUP 223 · GAGAL 0 · NEGATIF 0. Rejim QQQ OFF sejak 2026-10-16. Hanya **TERBUKTI** layak untuk wang sebenar (`laporan/KAD_SKOR.md`); nombor dalam laporan ini BUKAN keputusan dan tidak boleh dibaca sebagai pangkat untuk wang sebenar.

Dijana 2026-11-09 oleh `standard/skor_kaedah.py` (Actions `analisis.yml`, selepas kad skor). Harga pada tutup 2026-11-06; 223 kaedah; 16 hari beli langsung (rejim ON 1, OFF 15). Pradaftar 2026-11-09: `standard/SPEC_SKOR_KAEDAH.md` (berat dan sauh dikunci `ujian/test_skor_kaedah.py::TestKunci`). Rekod analisis sahaja: tiada order, tiada wang sebenar.

## Cara membaca

- **Skor** = min geometri berberat empat tiang (Untung 35 · Tahan 30 · Bukti 25 · Konsisten 10), dikecut ke 50 mengikut data: berat data = hari beli ÷ (hari beli + 20). Kaedah dengan 2 hari beli tidak boleh menjauhi 50. 100 = unggul semua segi; 50 = neutral/tiada bukti; < 50 = lebih buruk daripada neutral.
- **Siling** ikut kad skor: NEGATIF ≤ 20, GANTUNG/BERSARA ≤ 30, GAGAL ≤ 40. Tanda ⌈ = siling terpakai.
- **Satu-satunya status yang membenarkan wang sebenar ialah TERBUKTI dalam `laporan/KAD_SKOR.md`.** Skor tinggi dengan status BELUM CUKUP bermaksud "paling menjanjikan setakat ini", bukan "selamat".
- Deflasi ujian berganda (López de Prado): sauh t Bukti C1 = maks(2.0, E[maks 223 normal]) = 2.80.
- **Semakan kebolehramalan:** belum ada snapshot skor ≥ 7 hari lalu (sejarah bermula 2026-11-06); skor dipercayai sebagai pangkat hanya selepas 8–12 minggu semakan positif.

## Semua kaedah, susun ikut Skor

| # | Kaedah | Skor | Untung | Tahan | Bukti | Konsisten | Status kad | Hari beli | Posisi/tutup | Jangkaan % | T4 pul/|MDD| | Ulcer | t buku | Lift | WFE |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `M133` Bull Hook (Crabel) | **61.1** | 94 | 89 | 58 | 85 | BELUM CUKUP | 11 | 38/19 | +1.69 | +1.31 | 1.6 | +1.39 | – | 15.39 |
| 2 | `M33` Supertrend + SMA10 | **60.5** | 79 | 78 | 59 | 85 | BELUM CUKUP | 16 | 195/35 | +0.93 | +2.96 | 1.4 | +1.15 | – | 4.53 |
| 3 | `M146` 3-Bar Momentum Pattern | **59.2** | 73 | 73 | 60 | 85 | BELUM CUKUP | 16 | 76/27 | +0.70 | +0.53 | 1.9 | +1.38 | – | 2.92 |
| 4 | `M118` Expansion Pivot (Cooper) | **57.1** | 62 | 79 | 52 | 85 | BELUM CUKUP | 16 | 69/19 | -0.19 | +3.22 | 0.9 | +0.59 | – | 2.00 |
| 5 | `M25` VWAP Wave (proksi harian) | **56.5** | 64 | 69 | 57 | 80 | BELUM CUKUP | 15 | 138/81 | -0.34 | +0.73 | 2.9 | +0.54 | – | 3.77 |
| 6 | `M151` Outside Bar Failure | **56.4** | 64 | 80 | 51 | 67 | BELUM CUKUP | 15 | 81/44 | -0.43 | +5.23 | 0.5 | +0.16 | – | 0.41 |
| 7 | `M124` 'Last' Stochastic Technique (C | **54.8** | 59 | 66 | 55 | 69 | BELUM CUKUP | 16 | 328/156 | -0.42 | +0.73 | 2.5 | +0.21 | – | 0.48 |
| 8 | `M100` Bulkowski Segi Empat & Segi Ti | **54.5** | 60 | 66 | 50 | 81 | BELUM CUKUP | 14 | 58/37 | -0.36 | +0.67 | 2.2 | +0.15 | – | 0.87 |
| 9 | `M105` Supertrend tulen | **53.9** | 59 | 53 | 57 | 85 | BELUM CUKUP | 16 | 307/85 | +0.01 | +0.08 | 2.5 | +0.50 | – | 1.40 |
| 10 | `M111` Sistem Volatiliti Wilder | **53.7** | 58 | 54 | 55 | 85 | BELUM CUKUP | 16 | 223/70 | -0.30 | +0.41 | 3.5 | +0.42 | – | 1.08 |
| 11 | `M74` Lulus Baharu Trend Template Mi | **53.3** | 57 | 64 | 51 | 58 | BELUM CUKUP | 16 | 76/48 | -0.68 | +0.44 | 2.2 | +0.05 | – | 0.11 |
| 12 | `M13` Garis Trend Action/Safety Line | **53.2** | 55 | 70 | 49 | 55 | BELUM CUKUP | 16 | 650/399 | -0.95 | +1.67 | 1.3 | -0.52 | – | -1.07 |
| 13 | `M91` Stochastic Pop (Bernstein/Stec | **52.9** | 54 | 64 | 50 | 85 | BELUM CUKUP | 11 | 33/10 | -0.93 | +0.68 | 2.3 | +0.68 | – | 3.16 |
| 14 | `M160` Measured Move Up | **52.4** | 47 | 58 | 58 | 85 | BELUM CUKUP | 14 | 81/39 | -1.31 | +0.18 | 2.2 | +1.01 | – | 9.08 |
| 15 | `M15` Break & Retest + Henti ATR | **52.3** | 66 | 49 | 56 | 42 | BELUM CUKUP | 16 | 254/138 | +0.59 | -0.47 | 2.7 | +0.32 | – | 0.69 |
| 16 | `M145` Yum-Yum Continuation | **52.3** | 49 | 67 | 51 | 56 | BELUM CUKUP | 16 | 276/53 | -0.87 | +1.01 | 1.4 | +0.02 | – | 0.02 |
| 17 | `M89` Chande 65sma-3cc | **52.1** | 48 | 67 | 51 | 55 | BELUM CUKUP | 16 | 148/77 | -1.24 | +0.73 | 1.8 | -0.09 | – | -0.30 |
| 18 | `M10` EMA3 + CCI + MACD | **52.0** | 48 | 67 | 50 | 55 | BELUM CUKUP | 16 | 99/46 | -1.19 | +1.35 | 1.7 | +0.00 | – | 0.01 |
| 19 | `M142` Pecahan volum dari dasar (底部放量 | **51.7** | 61 | 63 | 40 | 55 | BELUM CUKUP | 12 | 37/4 | +0.04 | +0.26 | 1.8 | -0.00 | – | -0.00 |
| 20 | `M158` Doubly Adaptive Profit Targets | **51.6** | 60 | 46 | 59 | 47 | BELUM CUKUP | 16 | 330/111 | +0.12 | -0.34 | 2.2 | +0.67 | – | 2.02 |
| 21 | `M93` Bollinger Kaedah II: %b + MFI | **51.5** | 55 | 46 | 54 | 70 | BELUM CUKUP | 16 | 239/69 | -0.17 | -0.14 | 2.0 | +0.31 | – | 0.52 |
| 22 | `M21` Marius 3 Persediaan (Pecahan+J | **51.3** | 69 | 60 | 44 | 45 | BELUM CUKUP | 5 | 5/2 | +0.33 | +0.10 | 1.2 | +1.09 | – | 2.36 |
| 23 | `M137` Livermore System | **51.2** | 47 | 60 | 51 | 59 | BELUM CUKUP | 16 | 148/52 | -1.40 | +0.55 | 2.5 | +0.05 | – | 0.13 |
| 24 | `M129` Wick Play | **51.0** | 48 | 61 | 44 | 77 | BELUM CUKUP | 9 | 23/9 | -1.19 | +1.26 | 1.0 | +0.14 | – | 0.74 |
| 25 | `M80` Radge Saluran Purata Bergerak  | **50.9** | 60 | 45 | 56 | 43 | BELUM CUKUP | 16 | 241/46 | +0.29 | -0.29 | 3.2 | +0.61 | – | 0.93 |
| 26 | `M48` Cooper 1-2-3-4 | **50.5** | 46 | 53 | 48 | 80 | BELUM CUKUP | 14 | 45/15 | -1.36 | +0.85 | 2.2 | +0.27 | – | 0.82 |
| 27 | `M23` Breitstein Kapitulasi + Kesina | **50.5** | 44 | 50 | 54 | 77 | BELUM CUKUP | 16 | 107/65 | -1.22 | -0.31 | 2.1 | +0.34 | – | 1.62 |
| 28 | `M104` High Tight Flag / Power Play | **50.4** | 79 | 80 | 27 | 50 | BELUM CUKUP | 1 | 1/0 | +10.02 | +10.00 | – | – | – | – |
| 29 | `M30` BB Free Bar + Himpitan 50/2.5 | **50.4** | 52 | 44 | 56 | 56 | BELUM CUKUP | 16 | 212/57 | -0.51 | +0.01 | 4.6 | +0.54 | – | 1.17 |
| 30 | `M92` CCI-50 | **50.2** | 50 | 49 | 50 | 55 | BELUM CUKUP | 16 | 458/264 | -0.54 | -0.17 | 2.1 | -0.29 | – | -0.69 |
| 31 | `M70` Pecahan Hari Dalam | **50.0** | 59 | 60 | 52 | 15 | BELUM CUKUP | 16 | 352/289 | -0.50 | +0.10 | 2.4 | -0.14 | – | -0.46 |
| 32 | `N39X36` NR7 kemudian pecah → keluar se | **49.7** | 36 | 67 | 27 | 70 | BELUM CUKUP | 1 | 16/0 | -5.64 | +2.72 | 0.7 | – | – | – |
| 33 | `M02` MACD + SMA200 | **49.4** | 40 | 65 | 44 | 55 | BELUM CUKUP | 16 | 102/52 | -1.92 | +1.75 | 1.7 | -0.78 | – | -4.61 |
| 34 | `M159` Heikin-Ashi Trend | **49.4** | 54 | 58 | 46 | 23 | BELUM CUKUP | 16 | 1396/1102 | -0.67 | +0.47 | 3.9 | -0.83 | – | -5.38 |
| 35 | `M07` Qullamaggie Breakout | **49.2** | 29 | 65 | 27 | 15 | BELUM CUKUP | 1 | 1/1 | -2.53 | -0.21 | 0.6 | -0.22 | – | -1.12 |
| 36 | `M37` Weinstein Peringkat 2 | **48.8** | 45 | 58 | 20 | 25 | BELUM CUKUP | 2 | 3/0 | -0.78 | -0.34 | 0.2 | -1.01 | – | -0.76 |
| 37 | `M27` Price Action 4 Tiang | **48.8** | 42 | 39 | 41 | 15 | BELUM CUKUP | 2 | 547/427 | -1.09 | -0.53 | 2.8 | -0.66 | – | -2.65 |
| 38 | `M39` Radge Pecahan Bollinger 100 ha | **48.7** | 34 | 65 | 47 | 55 | BELUM CUKUP | 16 | 213/44 | -3.29 | +1.66 | 1.3 | -0.42 | – | -1.25 |
| 39 | `M51` O'Neil Cawan & Pemegang | **48.7** | 27 | 48 | 32 | 45 | BELUM CUKUP | 2 | 3/0 | -2.03 | -0.55 | 0.6 | +0.45 | – | 1.93 |
| 40 | `M05` MACD Divergence + Pengesahan | **48.6** | 41 | 59 | 39 | 55 | BELUM CUKUP | 13 | 38/12 | -1.57 | +0.38 | 1.4 | -0.77 | – | -1.27 |
| 41 | `M45` High 52 Minggu (George & Hwang | **48.6** | 25 | 35 | 9 | 15 | BELUM CUKUP | 1 | 2/1 | -7.63 | -0.83 | 1.1 | -2.31 | – | -5.78 |
| 42 | `N50X17` Mampat + pecah volum 1.5x → ke | **48.4** | 36 | 66 | 8 | 70 | BELUM CUKUP | 2 | 11/1 | -6.09 | +1.29 | 1.7 | -2.59 | – | – |
| 43 | `M84` Jarak purata bergerak MAD 21/2 | **48.4** | 17 | 15 | 15 | 15 | BELUM CUKUP | 1 | 58/35 | -4.85 | -1.00 | 5.3 | -3.06 | – | -7.55 |
| 44 | `M134` First Kiss After Daylight (Lan | **48.3** | 45 | 41 | 49 | 55 | BELUM CUKUP | 13 | 38/16 | -0.79 | -0.33 | 2.6 | +0.33 | – | 0.51 |
| 45 | `N68X16` Bullish engulfing + EMA21 → ke | **48.3** | 39 | 37 | 38 | 30 | BELUM CUKUP | 3 | 15/5 | -0.58 | -0.71 | 4.0 | +0.26 | – | – |
| 46 | `M132` Ascending Scallop (Bulkowski) | **48.2** | 34 | 58 | 48 | 55 | BELUM CUKUP | 15 | 88/32 | -2.32 | +0.59 | 2.1 | -0.11 | – | -1.09 |
| 47 | `M88` O'Neil Shakeout +3 | **48.2** | 37 | 55 | 45 | 55 | BELUM CUKUP | 13 | 48/27 | -2.55 | +0.32 | 2.7 | -0.34 | – | -0.82 |
| 48 | `N57X16` ADX bangkit daripada <20 → kel | **48.2** | 30 | 62 | 19 | 70 | BELUM CUKUP | 3 | 37/2 | -3.66 | +0.78 | 1.8 | -1.70 | – | – |
| 49 | `N50X14` Mampat + pecah volum 1.5x → ke | **48.2** | 36 | 67 | 7 | 70 | BELUM CUKUP | 2 | 11/0 | -5.94 | +2.92 | 1.2 | -2.47 | – | – |
| 50 | `N66X36` 52w tinggi + pengesahan 1% → k | **48.2** | 20 | 44 | 28 | 50 | BELUM CUKUP | 2 | 27/0 | -2.81 | -0.33 | 2.9 | – | – | – |
| 51 | `M96` Momo India: Ranking Sharpe 3/6 | **48.2** | 17 | 12 | 9 | 15 | BELUM CUKUP | 1 | 6/5 | -12.54 | -1.00 | 4.5 | -3.78 | – | -16.54 |
| 52 | `N57X36` ADX bangkit daripada <20 → kel | **48.1** | 30 | 68 | 15 | 70 | BELUM CUKUP | 3 | 39/0 | -3.64 | +4.44 | 0.9 | -1.65 | – | – |
| 53 | `M131` Ross Hook (Joe Ross) | **48.0** | 42 | 46 | 53 | 39 | BELUM CUKUP | 16 | 241/102 | -1.12 | -0.28 | 2.5 | +0.04 | – | 0.12 |
| 54 | `N68X36` Bullish engulfing + EMA21 → ke | **48.0** | 36 | 32 | 38 | 30 | BELUM CUKUP | 3 | 14/3 | -0.42 | -0.89 | 6.3 | +0.45 | – | – |
| 55 | `M138` 直升机空中加油 (Helikopter isi minyak | **48.0** | 28 | 45 | 19 | 15 | BELUM CUKUP | 2 | 2/0 | -2.53 | -0.72 | 0.2 | -1.09 | – | -2.67 |
| 56 | `M94` Pecutan Momentum (Chen, Yu & W | **47.9** | 12 | 4 | 3 | 15 | BELUM CUKUP | 1 | 33/0 | -11.42 | -1.00 | 7.8 | -3.54 | – | -11.60 |
| 57 | `N80X36` Tinggi sepanjang masa → keluar | **47.8** | 34 | 68 | 10 | 70 | BELUM CUKUP | 3 | 23/0 | -1.84 | +0.78 | 1.3 | -2.23 | – | – |
| 58 | `M139` 均线首次粘合向上发散 (MA berhimpun kali  | **47.7** | 34 | 56 | 46 | 55 | BELUM CUKUP | 16 | 65/16 | -1.70 | +0.59 | 1.7 | -0.05 | – | -0.19 |
| 59 | `N07X36` Tiga MA tersusun → keluar sele | **47.6** | 25 | 45 | 21 | 70 | BELUM CUKUP | 3 | 58/2 | -2.36 | -0.27 | 1.6 | -1.45 | – | – |
| 60 | `M78` Alvarez Pecahan Mingguan DTAYS | **47.6** | 18 | 25 | 40 | 15 | BELUM CUKUP | 2 | 73/38 | -2.41 | -0.76 | 5.5 | -0.14 | – | -0.65 |
| 61 | `N124X36` Episodic pivot gap 8-10% → kel | **47.5** | 31 | 52 | 12 | 68 | BELUM CUKUP | 3 | 28/5 | -2.19 | -0.19 | 1.7 | -2.69 | – | – |
| 62 | `N22X36` BB pecah atas + RSI → keluar s | **47.5** | 21 | 42 | 35 | 30 | BELUM CUKUP | 3 | 62/5 | -2.74 | -0.37 | 3.0 | -0.10 | – | – |
| 63 | `M117` Landry Pullback (high 2 bulan) | **47.4** | 53 | 36 | 50 | 28 | BELUM CUKUP | 14 | 81/17 | -0.00 | -0.75 | 3.0 | +0.38 | – | 0.45 |
| 64 | `N22X16` BB pecah atas + RSI → keluar b | **47.4** | 20 | 42 | 35 | 30 | BELUM CUKUP | 3 | 59/14 | -2.59 | -0.40 | 3.3 | -0.47 | – | – |
| 65 | `N64X36` Episodic pivot → keluar selepa | **47.3** | 30 | 58 | 9 | 70 | BELUM CUKUP | 3 | 36/2 | -2.17 | +0.06 | 1.9 | -4.29 | – | – |
| 66 | `N64X17` Episodic pivot → keluar bila a | **47.3** | 28 | 52 | 12 | 70 | BELUM CUKUP | 3 | 36/5 | -1.89 | -0.26 | 1.7 | -3.62 | – | – |
| 67 | `N42X36` Lonjakan volum 2x → keluar sel | **47.3** | 23 | 46 | 17 | 70 | BELUM CUKUP | 3 | 102/27 | -2.62 | -0.17 | 2.1 | -3.86 | – | – |
| 68 | `M148` Natural Number Method | **47.2** | 33 | 58 | 42 | 55 | BELUM CUKUP | 16 | 176/114 | -2.22 | +0.37 | 1.7 | -1.24 | – | -5.56 |
| 69 | `N07X16` Tiga MA tersusun → keluar bila | **47.2** | 22 | 40 | 24 | 50 | BELUM CUKUP | 3 | 56/5 | -2.19 | -0.58 | 2.4 | -1.37 | – | – |
| 70 | `M41` FW Penyatuan Mingguan | **47.2** | 23 | 26 | 39 | 37 | BELUM CUKUP | 3 | 33/6 | -1.73 | -0.70 | 3.6 | +0.32 | – | 0.74 |
| 71 | `N64X16` Episodic pivot → keluar bila s | **47.1** | 27 | 52 | 9 | 70 | BELUM CUKUP | 3 | 36/2 | -2.00 | -0.20 | 1.8 | -3.87 | – | – |
| 72 | `N37X36` Gap and go → keluar selepas DU | **47.1** | 25 | 42 | 13 | 70 | BELUM CUKUP | 3 | 58/9 | -3.61 | -0.13 | 1.6 | -11.07 | – | – |
| 73 | `N37X17` Gap and go → keluar bila adx14 | **47.0** | 23 | 41 | 14 | 70 | BELUM CUKUP | 3 | 57/12 | -3.27 | -0.20 | 1.4 | -9.27 | – | – |
| 74 | `N40X36` OBV tinggi baharu + MA50 → kel | **47.0** | 24 | 37 | 22 | 30 | BELUM CUKUP | 3 | 23/3 | -2.67 | -0.73 | 2.5 | -1.46 | – | – |
| 75 | `N37X16` Gap and go → keluar bila super | **47.0** | 24 | 43 | 13 | 70 | BELUM CUKUP | 3 | 58/7 | -3.32 | -0.08 | 2.0 | -9.33 | – | – |
| 76 | `M115` Bow Tie (Landry) | **46.9** | 31 | 42 | 46 | 50 | BELUM CUKUP | 8 | 31/18 | -2.29 | -0.54 | 2.7 | +0.13 | – | 0.98 |
| 77 | `N40X16` OBV tinggi baharu + MA50 → kel | **46.9** | 24 | 35 | 20 | 30 | BELUM CUKUP | 3 | 30/13 | -2.56 | -0.83 | 2.5 | -2.14 | – | – |
| 78 | `N124X15` Episodic pivot gap 8-10% → eko | **46.9** | 29 | 45 | 11 | 30 | BELUM CUKUP | 3 | 28/0 | -2.01 | -0.45 | 1.6 | -2.13 | – | – |
| 79 | `N37X14` Gap and go → keluar bila rsi14 | **46.8** | 24 | 45 | 9 | 70 | BELUM CUKUP | 3 | 58/2 | -3.10 | +0.04 | 1.9 | -7.98 | – | – |
| 80 | `N06X36` Golden cross MA50/MA200 → kelu | **46.7** | 25 | 64 | 5 | 70 | BELUM CUKUP | 3 | 8/0 | -4.44 | +0.70 | 1.1 | -3.83 | – | – |
| 81 | `M38` Darvas Kotak | **46.7** | 16 | 29 | 32 | 35 | BELUM CUKUP | 3 | 15/1 | -6.14 | -0.43 | 3.3 | -0.02 | – | -0.13 |
| 82 | `M46` Jurang Naik Boleh Beli (Buyabl | **46.6** | 33 | 52 | 43 | 30 | BELUM CUKUP | 10 | 33/16 | -1.73 | -0.22 | 1.7 | -0.30 | – | -0.51 |
| 83 | `M64` O'Neil Tiga Minggu Ketat | **46.6** | 25 | 25 | 27 | 15 | BELUM CUKUP | 3 | 3/1 | -10.28 | -0.80 | 1.8 | -0.78 | – | -11.82 |
| 84 | `N31X36` Turtle sistem 2 → keluar selep | **46.6** | 27 | 54 | 5 | 70 | BELUM CUKUP | 3 | 65/0 | -3.83 | +0.16 | 1.5 | -5.00 | – | – |
| 85 | `N45X16` Undur EMA21 cerun positif → ke | **46.6** | 18 | 22 | 36 | 30 | BELUM CUKUP | 3 | 61/23 | -1.64 | -1.00 | 6.4 | -0.52 | – | – |
| 86 | `N64X14` Episodic pivot → keluar bila r | **46.6** | 27 | 52 | 5 | 70 | BELUM CUKUP | 3 | 36/0 | -1.91 | -0.26 | 1.7 | -3.63 | – | – |
| 87 | `N47X36` NR7 + EMA9>EMA21 → keluar sele | **46.6** | 8 | 26 | 8 | 30 | BELUM CUKUP | 2 | 21/2 | -6.32 | -1.00 | 4.0 | -4.02 | – | – |
| 88 | `N22X14` BB pecah atas + RSI → keluar b | **46.5** | 19 | 36 | 17 | 30 | BELUM CUKUP | 3 | 64/0 | -3.08 | -0.48 | 3.5 | -1.48 | – | – |
| 89 | `N35X36` Pecah 52 minggu tinggi → kelua | **46.5** | 24 | 54 | 5 | 70 | BELUM CUKUP | 3 | 30/0 | -2.43 | +0.17 | 1.4 | -2.86 | – | – |
| 90 | `N42X16` Lonjakan volum 2x → keluar bil | **46.4** | 17 | 34 | 17 | 34 | BELUM CUKUP | 3 | 104/31 | -2.58 | -0.73 | 2.7 | -3.87 | – | – |
| 91 | `N42X17` Lonjakan volum 2x → keluar bil | **46.4** | 18 | 34 | 17 | 33 | BELUM CUKUP | 3 | 108/24 | -2.88 | -0.63 | 2.9 | -3.74 | – | – |
| 92 | `N33X16` Donchian20 + penapis MA200 → k | **46.3** | 18 | 43 | 10 | 30 | BELUM CUKUP | 3 | 46/3 | -3.02 | -0.44 | 2.8 | -4.14 | – | – |
| 93 | `M153` Range Leader | **46.2** | 49 | 40 | 52 | 15 | BELUM CUKUP | 16 | 1040/855 | -0.35 | -0.37 | 5.8 | -0.12 | – | -0.90 |
| 94 | `M35` Pocket Pivot Morales & Kacher | **46.2** | 50 | 39 | 52 | 15 | BELUM CUKUP | 16 | 281/191 | -0.59 | -0.54 | 4.8 | -0.10 | – | -0.67 |
| 95 | `N33X14` Donchian20 + penapis MA200 → k | **46.1** | 20 | 46 | 5 | 52 | BELUM CUKUP | 3 | 53/0 | -3.23 | -0.36 | 2.0 | -2.85 | – | – |
| 96 | `M121` High 2 bull flag (Brooks) | **46.1** | 20 | 19 | 24 | 15 | BELUM CUKUP | 3 | 5/3 | -11.65 | -0.79 | 3.1 | -1.20 | – | -24.49 |
| 97 | `M18` EMA9/21 Pullback | **46.0** | 55 | 33 | 53 | 15 | BELUM CUKUP | 16 | 271/202 | -0.12 | -1.00 | 4.2 | -0.04 | – | -0.18 |
| 98 | `M150` Trend Bar Failure (Brooks) | **46.0** | 49 | 42 | 46 | 15 | BELUM CUKUP | 15 | 79/33 | -0.39 | -0.76 | 2.1 | -0.41 | – | -1.75 |
| 99 | `N33X36` Donchian20 + penapis MA200 → k | **46.0** | 20 | 45 | 5 | 42 | BELUM CUKUP | 3 | 46/0 | -2.97 | -0.38 | 2.2 | -3.99 | – | – |
| 100 | `N36X16` Pocket pivot → keluar bila sup | **46.0** | 14 | 26 | 17 | 30 | BELUM CUKUP | 3 | 98/31 | -3.08 | -0.74 | 3.3 | -6.14 | – | – |
| 101 | `N36X36` Pocket pivot → keluar selepas  | **46.0** | 15 | 27 | 16 | 30 | BELUM CUKUP | 3 | 98/19 | -3.37 | -0.75 | 2.9 | -6.20 | – | – |
| 102 | `N65X14` Gap 4% + volum + hampir 52w →  | **45.9** | 20 | 43 | 5 | 30 | BELUM CUKUP | 3 | 24/0 | -2.63 | -0.64 | 1.7 | -4.02 | – | – |
| 103 | `N65X36` Gap 4% + volum + hampir 52w →  | **45.9** | 20 | 43 | 5 | 30 | BELUM CUKUP | 3 | 24/0 | -2.63 | -0.65 | 1.7 | -4.02 | – | – |
| 104 | `N48X36` Inside day pecah → keluar sele | **45.9** | 15 | 22 | 17 | 30 | BELUM CUKUP | 3 | 75/26 | -4.17 | -0.69 | 7.2 | -7.95 | – | – |
| 105 | `M32` Momentum Burst | **45.8** | 47 | 28 | 49 | 24 | BELUM CUKUP | 11 | 51/32 | -0.77 | -0.46 | 6.1 | +0.10 | – | 0.31 |
| 106 | `N47X16` NR7 + EMA9>EMA21 → keluar bila | **45.8** | 12 | 30 | 13 | 30 | BELUM CUKUP | 3 | 23/7 | -4.46 | -0.98 | 3.9 | -4.25 | – | – |
| 107 | `M68` Kell Base n' Break | **45.7** | 28 | 43 | 43 | 55 | BELUM CUKUP | 11 | 40/10 | -3.52 | -0.14 | 1.5 | -0.14 | – | -1.31 |
| 108 | `M157` Consolidation Pivot Breakout ( | **45.7** | 19 | 35 | 27 | 15 | BELUM CUKUP | 4 | 4/3 | -5.75 | -0.78 | 0.9 | -0.91 | – | -4.55 |
| 109 | `N113X36` 80-20 bar (sisi beli) → keluar | **45.7** | 12 | 19 | 18 | 30 | BELUM CUKUP | 3 | 74/43 | -4.38 | -0.79 | 5.2 | -4.70 | – | – |
| 110 | `N75X17` RSI14 < 40 tanpa penapis → kel | **45.7** | 10 | 23 | 18 | 30 | BELUM CUKUP | 3 | 193/32 | -1.56 | -0.83 | 12.2 | -4.61 | – | – |
| 111 | `N42X15` Lonjakan volum 2x → ekori Chan | **45.6** | 18 | 30 | 5 | 33 | BELUM CUKUP | 3 | 96/0 | -2.69 | -0.80 | 2.8 | -3.18 | – | – |
| 112 | `N42X14` Lonjakan volum 2x → keluar bil | **45.5** | 16 | 31 | 5 | 30 | BELUM CUKUP | 3 | 100/0 | -2.62 | -0.67 | 3.5 | -3.13 | – | – |
| 113 | `N113X16` 80-20 bar (sisi beli) → keluar | **45.5** | 11 | 17 | 19 | 30 | BELUM CUKUP | 3 | 72/47 | -5.07 | -0.79 | 5.3 | -6.64 | – | – |
| 114 | `N45X36` Undur EMA21 cerun positif → ke | **45.5** | 8 | 17 | 26 | 30 | BELUM CUKUP | 3 | 53/7 | -2.18 | -1.00 | 7.8 | -1.29 | – | – |
| 115 | `N76X36` Tutup > MA50 (penapis trend tu | **45.4** | 10 | 19 | 13 | 30 | BELUM CUKUP | 3 | 63/8 | -2.99 | -0.98 | 7.5 | -4.31 | – | – |
| 116 | `M04` BB Squeeze Breakout | **45.3** | 30 | 39 | 52 | 48 | BELUM CUKUP | 15 | 138/38 | -1.83 | -0.06 | 4.0 | +0.25 | – | 0.52 |
| 117 | `M107` Golden Cross SMA50/200 | **45.3** | 35 | 49 | 42 | 21 | BELUM CUKUP | 14 | 28/7 | -1.35 | -0.11 | 1.5 | -0.16 | – | -0.32 |
| 118 | `M143` 장대양봉 이후 눌림목 / 5일선 매매 (Undur ke | **45.3** | 31 | 46 | 27 | 29 | BELUM CUKUP | 8 | 11/1 | -1.23 | -0.39 | 1.6 | -0.94 | – | -11.52 |
| 119 | `N74X16` MACD atas garis isyarat (keada | **45.3** | 7 | 18 | 21 | 30 | BELUM CUKUP | 3 | 170/80 | -1.66 | -0.97 | 9.6 | -2.92 | – | – |
| 120 | `N53X36` Supertrend + ADX>25 → keluar s | **45.3** | 5 | 20 | 30 | 30 | BELUM CUKUP | 3 | 65/8 | -2.14 | -1.00 | 8.6 | -0.88 | – | – |
| 121 | `N36X14` Pocket pivot → keluar bila rsi | **45.3** | 10 | 22 | 9 | 30 | BELUM CUKUP | 3 | 96/2 | -3.84 | -0.86 | 3.3 | -5.09 | – | – |
| 122 | `N53X16` Supertrend + ADX>25 → keluar b | **45.3** | 5 | 22 | 26 | 30 | BELUM CUKUP | 3 | 58/1 | -1.96 | -1.00 | 8.0 | -0.69 | – | – |
| 123 | `N38X36` VCP pecah → keluar selepas DUA | **45.3** | 9 | 30 | 8 | 30 | BELUM CUKUP | 3 | 11/1 | -2.93 | -1.00 | 3.7 | -3.63 | – | – |
| 124 | `N28X16` ADX>25 + DI+ > DI- → keluar bi | **45.2** | 6 | 20 | 18 | 30 | BELUM CUKUP | 3 | 118/35 | -1.84 | -0.89 | 8.7 | -5.28 | – | – |
| 125 | `N53X17` Supertrend + ADX>25 → keluar b | **45.2** | 5 | 18 | 23 | 30 | BELUM CUKUP | 3 | 54/0 | -1.99 | -0.99 | 10.4 | -0.70 | – | – |
| 126 | `M116` 2/20 EMA Breakout (Landry) | **45.1** | 44 | 36 | 52 | 15 | BELUM CUKUP | 16 | 508/318 | -0.52 | -0.31 | 6.4 | -0.06 | – | -0.32 |
| 127 | `M87` IBD Tapak Menaik | **45.1** | 31 | 33 | 38 | 15 | BELUM CUKUP | 7 | 10/6 | -3.32 | -0.57 | 3.1 | -0.30 | – | -1.24 |
| 128 | `M144` Screw Bar | **45.1** | 24 | 32 | 26 | 15 | BELUM CUKUP | 5 | 8/6 | -2.88 | -0.86 | 1.0 | -1.33 | – | -4.71 |
| 129 | `N51X16` BB squeeze + Supertrend → kelu | **45.1** | 4 | 24 | 18 | 30 | BELUM CUKUP | 3 | 4/1 | -3.94 | -0.87 | 5.4 | -1.55 | – | – |
| 130 | `N19X13` Bawah jalur BB + RSI<30 → kelu | **45.0** | 8 | 27 | 5 | 30 | BELUM CUKUP | 3 | 87/0 | -1.62 | -0.80 | 8.7 | -4.95 | – | – |
| 131 | `N56X16` RSI>50 + ADX>20 → keluar bila  | **44.9** | 4 | 17 | 16 | 30 | BELUM CUKUP | 3 | 80/23 | -1.90 | -1.00 | 8.2 | -4.11 | – | – |
| 132 | `N27X36` Ichimoku atas awan → keluar se | **44.9** | 6 | 20 | 9 | 30 | BELUM CUKUP | 3 | 50/2 | -3.96 | -0.98 | 5.6 | -6.86 | – | – |
| 133 | `N41X16` CMF20>0 + tutup>EMA20 → keluar | **44.9** | 4 | 13 | 20 | 30 | BELUM CUKUP | 3 | 112/57 | -2.68 | -1.00 | 10.2 | -5.44 | – | – |
| 134 | `M106` DMI Wilder | **44.8** | 44 | 34 | 49 | 15 | BELUM CUKUP | 14 | 99/49 | -0.69 | -0.77 | 2.4 | -0.10 | – | -0.22 |
| 135 | `N76X16` Tutup > MA50 (penapis trend tu | **44.8** | 4 | 15 | 19 | 30 | BELUM CUKUP | 3 | 103/47 | -2.98 | -0.95 | 8.9 | -5.12 | – | – |
| 136 | `N41X36` CMF20>0 + tutup>EMA20 → keluar | **44.8** | 5 | 11 | 18 | 30 | BELUM CUKUP | 3 | 94/42 | -3.11 | -1.00 | 10.0 | -4.86 | – | – |
| 137 | `N43X36` Undur EMA8 + penapis MA50 → ke | **44.8** | 5 | 19 | 10 | 30 | BELUM CUKUP | 3 | 60/3 | -4.83 | -1.00 | 4.8 | -4.13 | – | – |
| 138 | `N08X16` tutup>EMA20 tidak terlalu jauh | **44.8** | 3 | 16 | 21 | 30 | BELUM CUKUP | 3 | 161/86 | -2.47 | -1.00 | 8.5 | -5.76 | – | – |
| 139 | `N08X36` tutup>EMA20 tidak terlalu jauh | **44.8** | 3 | 16 | 20 | 30 | BELUM CUKUP | 3 | 141/60 | -2.82 | -1.00 | 8.6 | -6.45 | – | – |
| 140 | `N51X36` BB squeeze + Supertrend → kelu | **44.8** | 3 | 22 | 15 | 30 | BELUM CUKUP | 3 | 4/0 | -4.20 | -0.87 | 5.8 | -1.65 | – | – |
| 141 | `M152` Spike & Ledge | **44.7** | 24 | 48 | 40 | 55 | BELUM CUKUP | 13 | 39/6 | -2.91 | +0.16 | 2.1 | -0.41 | – | -1.65 |
| 142 | `N25X36` Supertrend + EMA + ADX>23 → ke | **44.7** | 2 | 22 | 18 | 30 | BELUM CUKUP | 3 | 60/8 | -2.57 | -1.00 | 8.1 | -2.25 | – | – |
| 143 | `M77` Undercut & Rally pada Purata B | **44.6** | 29 | 44 | 37 | 55 | BELUM CUKUP | 14 | 44/32 | -2.12 | -0.51 | 1.7 | -1.40 | – | -2.04 |
| 144 | `N24X36` Supertrend(10,3) + ADX>20 → ke | **44.6** | 3 | 12 | 15 | 30 | BELUM CUKUP | 3 | 66/15 | -3.27 | -1.00 | 9.0 | -4.14 | – | – |
| 145 | `N28X36` ADX>25 + DI+ > DI- → keluar se | **44.6** | 2 | 16 | 18 | 30 | BELUM CUKUP | 3 | 114/32 | -1.96 | -0.94 | 10.1 | -5.12 | – | – |
| 146 | `N24X16` Supertrend(10,3) + ADX>20 → ke | **44.6** | 4 | 16 | 9 | 30 | BELUM CUKUP | 3 | 50/2 | -2.37 | -1.00 | 8.1 | -3.25 | – | – |
| 147 | `N28X14` ADX>25 + DI+ > DI- → keluar bi | **44.6** | 3 | 20 | 8 | 30 | BELUM CUKUP | 3 | 74/1 | -2.50 | -0.84 | 8.3 | -3.20 | – | – |
| 148 | `N27X16` Ichimoku atas awan → keluar bi | **44.5** | 2 | 20 | 15 | 30 | BELUM CUKUP | 3 | 67/15 | -3.30 | -0.94 | 7.6 | -7.89 | – | – |
| 149 | `N28X17` ADX>25 + DI+ > DI- → keluar bi | **44.5** | 3 | 19 | 5 | 30 | BELUM CUKUP | 3 | 50/0 | -2.56 | -0.86 | 7.9 | -3.62 | – | – |
| 150 | `N25X17` Supertrend + EMA + ADX>23 → ke | **44.5** | 2 | 22 | 11 | 30 | BELUM CUKUP | 3 | 55/0 | -2.37 | -1.00 | 8.2 | -2.11 | – | – |
| 151 | `N24X17` Supertrend(10,3) + ADX>20 → ke | **44.4** | 3 | 14 | 8 | 30 | BELUM CUKUP | 3 | 58/1 | -2.30 | -1.00 | 11.8 | -2.78 | – | – |
| 152 | `N25X16` Supertrend + EMA + ADX>23 → ke | **44.4** | 1 | 22 | 13 | 30 | BELUM CUKUP | 3 | 57/1 | -2.52 | -1.00 | 8.1 | -2.19 | – | – |
| 153 | `N56X17` RSI>50 + ADX>20 → keluar bila  | **44.4** | 2 | 14 | 11 | 30 | BELUM CUKUP | 3 | 60/4 | -2.39 | -1.00 | 9.9 | -4.17 | – | – |
| 154 | `N09X36` Undur EMA10 + penapis EMA50 →  | **44.3** | 0 | 16 | 15 | 30 | BELUM CUKUP | 3 | 72/14 | -4.31 | -0.99 | 7.8 | -4.92 | – | – |
| 155 | `N29X16` PSAR naik + tutup>MA50 → kelua | **44.3** | 0 | 14 | 18 | 30 | BELUM CUKUP | 3 | 86/38 | -3.96 | -1.00 | 8.9 | -5.07 | – | – |
| 156 | `N56X36` RSI>50 + ADX>20 → keluar selep | **44.3** | 1 | 10 | 16 | 30 | BELUM CUKUP | 3 | 74/20 | -3.04 | -1.00 | 9.9 | -7.27 | – | – |
| 157 | `N75X13` RSI14 < 40 tanpa penapis → kel | **44.3** | 1 | 22 | 5 | 30 | BELUM CUKUP | 3 | 100/0 | -2.18 | -0.85 | 14.7 | -4.43 | – | – |
| 158 | `N75X15` RSI14 < 40 tanpa penapis → eko | **44.3** | 1 | 22 | 5 | 30 | BELUM CUKUP | 3 | 100/0 | -2.18 | -0.85 | 14.7 | -4.43 | – | – |
| 159 | `N75X14` RSI14 < 40 tanpa penapis → kel | **44.3** | 1 | 23 | 8 | 30 | BELUM CUKUP | 3 | 153/1 | -2.03 | -0.81 | 10.6 | -4.70 | – | – |
| 160 | `N119X13` 3 tutup turun berturut → kelua | **44.2** | 0 | 15 | 12 | 30 | BELUM CUKUP | 3 | 36/5 | -4.79 | -0.82 | 15.0 | -4.45 | – | – |
| 161 | `N16X13` RSI2<10 tanpa penapis → keluar | **44.2** | 0 | 16 | 10 | 30 | BELUM CUKUP | 3 | 90/3 | -3.24 | -0.82 | 15.0 | -6.63 | – | – |
| 162 | `N29X36` PSAR naik + tutup>MA50 → kelua | **44.2** | 0 | 13 | 12 | 30 | BELUM CUKUP | 3 | 68/6 | -3.58 | -1.00 | 11.6 | -4.63 | – | – |
| 163 | `N55X13` BB + RSI + ADX>20 → keluar bil | **44.2** | 0 | 23 | 5 | 30 | BELUM CUKUP | 3 | 32/0 | -2.29 | -0.77 | 11.8 | -3.36 | – | – |
| 164 | `N54X36` Supertrend + RSI>50 → keluar s | **44.2** | 1 | 9 | 15 | 30 | BELUM CUKUP | 3 | 74/14 | -3.27 | -1.00 | 10.2 | -5.13 | – | – |
| 165 | `N73X13` Tutup bawah jalur bawah BB(20, | **44.2** | 0 | 19 | 5 | 30 | BELUM CUKUP | 3 | 114/0 | -2.36 | -0.87 | 13.7 | -3.68 | – | – |
| 166 | `M34` Carter TTM Squeeze | **44.1** | 29 | 37 | 46 | 50 | BELUM CUKUP | 16 | 94/44 | -2.18 | -0.16 | 3.0 | -0.47 | – | -2.05 |
| 167 | `M06` Minervini VCP Breakout | **44.1** | 26 | 46 | 44 | 36 | BELUM CUKUP | 16 | 70/31 | -2.51 | -0.36 | 2.2 | -0.57 | – | -2.09 |
| 168 | `M127` Slingshot Bullish | **44.1** | 32 | 47 | 43 | 15 | BELUM CUKUP | 14 | 91/68 | -1.95 | -0.37 | 3.0 | -1.00 | – | -1.79 |
| 169 | `N119X15` 3 tutup turun berturut → ekori | **44.1** | 0 | 18 | 5 | 30 | BELUM CUKUP | 3 | 14/0 | -4.84 | -0.82 | 15.0 | -4.91 | – | – |
| 170 | `N54X16` Supertrend + RSI>50 → keluar b | **44.1** | 1 | 10 | 10 | 30 | BELUM CUKUP | 3 | 57/3 | -2.38 | -1.00 | 10.8 | -3.11 | – | – |
| 171 | `N16X15` RSI2<10 tanpa penapis → ekori  | **44.1** | 0 | 14 | 5 | 30 | BELUM CUKUP | 3 | 88/0 | -3.64 | -0.82 | 15.0 | -8.19 | – | – |
| 172 | `M08` SMA20 + SMA200 | **44.0** | 36 | 28 | 48 | 32 | BELUM CUKUP | 14 | 128/84 | -1.32 | -0.90 | 4.0 | -0.43 | – | -1.51 |
| 173 | `M14` Walking with the Whales | **43.8** | 42 | 32 | 48 | 15 | BELUM CUKUP | 16 | 774/536 | -0.79 | -0.75 | 5.2 | -0.61 | – | -1.38 |
| 174 | `M49` Ichimoku (Tutup Atas Awan + Te | **43.7** | 30 | 42 | 46 | 24 | BELUM CUKUP | 16 | 241/134 | -2.03 | -0.31 | 2.9 | -0.76 | – | -1.59 |
| 175 | `M03` BB Break + Divergence RSI | **43.7** | 34 | 41 | 46 | 15 | BELUM CUKUP | 16 | 323/281 | -1.01 | -0.40 | 2.7 | -0.81 | – | -2.78 |
| 176 | `M102` Stockbee SLTB | **43.6** | 36 | 37 | 48 | 15 | BELUM CUKUP | 16 | 313/236 | -1.57 | -0.47 | 5.0 | -0.54 | – | -2.03 |
| 177 | `M130` 多方炮 (dua lilin hijau mengapit  | **43.6** | 17 | 24 | 34 | 15 | BELUM CUKUP | 6 | 9/3 | -3.73 | -0.58 | 2.4 | -0.22 | – | -0.25 |
| 178 | `M20` EMA10/15 Crossover + Sudut | **43.5** | 33 | 37 | 41 | 26 | BELUM CUKUP | 16 | 369/316 | -1.57 | -0.64 | 2.6 | -1.39 | – | -10.80 |
| 179 | `M99` Three Line Break | **43.5** | 32 | 37 | 47 | 22 | BELUM CUKUP | 16 | 129/84 | -3.19 | -0.15 | 3.1 | -0.58 | – | -3.17 |
| 180 | `M155` Market Cycle Strategy | **43.3** | 38 | 33 | 47 | 15 | BELUM CUKUP | 16 | 591/211 | -1.19 | -0.50 | 3.2 | -0.72 | – | -1.35 |
| 181 | `M141` First Thrust (Landry) | **43.3** | 18 | 34 | 30 | 15 | BELUM CUKUP | 7 | 20/8 | -3.61 | -0.77 | 1.8 | -1.34 | – | -3.66 |
| 182 | `M136` Short/Intermediate-term Low (L | **43.1** | 31 | 40 | 48 | 15 | BELUM CUKUP | 16 | 625/236 | -1.79 | -0.43 | 2.3 | -0.54 | – | -0.36 |
| 183 | `M44` Tapak Rata IBD | **43.1** | 26 | 38 | 20 | 15 | BELUM CUKUP | 8 | 9/4 | -4.57 | -0.84 | 2.3 | -2.36 | – | -42.45 |
| 184 | `M54` IBD Power Trend | **43.0** | 29 | 39 | 48 | 15 | BELUM CUKUP | 15 | 193/100 | -1.93 | -0.18 | 5.3 | -0.51 | – | -1.56 |
| 185 | `M147` Improved Three-Bar Pullback | **43.0** | 28 | 46 | 35 | 18 | BELUM CUKUP | 14 | 95/27 | -3.15 | +0.22 | 4.0 | -1.49 | – | -1.27 |
| 186 | `M149` 3-Step Pullback | **43.0** | 31 | 30 | 51 | 19 | BELUM CUKUP | 14 | 150/50 | -1.39 | -0.55 | 4.6 | +0.13 | – | 0.14 |
| 187 | `M120` Reversal New Highs | **43.0** | 32 | 34 | 38 | 15 | BELUM CUKUP | 12 | 18/12 | -2.49 | -0.56 | 2.9 | -0.79 | – | -5.15 |
| 188 | `M31` Band Walk (BB 20/2) | **42.8** | 36 | 27 | 51 | 20 | BELUM CUKUP | 16 | 369/47 | -1.10 | -0.35 | 6.2 | +0.07 | – | 0.17 |
| 189 | `M19` Sneaky Pivot (proksi harian) | **42.6** | 24 | 36 | 41 | 41 | BELUM CUKUP | 15 | 265/215 | -4.35 | -0.27 | 2.9 | -1.36 | – | -22.43 |
| 190 | `M67` Rayner Teo: Ujian Ketiga pada  | **42.5** | 26 | 34 | 36 | 15 | BELUM CUKUP | 11 | 25/16 | -4.15 | -0.59 | 4.8 | -1.10 | – | -7.15 |
| 191 | `M140` 猎豹出击 (Serangan Cheetah) | **42.5** | 18 | 32 | 29 | 15 | BELUM CUKUP | 8 | 37/11 | -2.59 | -0.76 | 2.5 | -1.66 | – | -2.10 |
| 192 | `M36` Turtle 55/20 | **42.3** | 29 | 34 | 51 | 15 | BELUM CUKUP | 16 | 297/144 | -1.70 | -0.40 | 6.1 | -0.20 | – | -0.64 |
| 193 | `M135` 3rd Watch | **42.2** | 12 | 28 | 30 | 15 | BELUM CUKUP | 7 | 12/2 | -6.23 | -0.91 | 2.7 | -0.95 | – | -7.18 |
| 194 | `M125` 2-Bar Breakout | **41.8** | 26 | 36 | 46 | 15 | BELUM CUKUP | 16 | 872/400 | -2.09 | -0.37 | 2.4 | -0.77 | – | -0.49 |
| 195 | `M128` Inventory Retracement Bar (IRB | **41.7** | 32 | 27 | 49 | 15 | BELUM CUKUP | 16 | 126/70 | -1.33 | -0.63 | 5.6 | -0.28 | – | -1.92 |
| 196 | `M12` Parabolic SAR | **41.4** | 25 | 33 | 48 | 15 | BELUM CUKUP | 16 | 325/164 | -2.35 | -0.61 | 3.0 | -0.54 | – | -1.75 |
| 197 | `M156` Single Penetration (DiNapoli) | **41.4** | 20 | 31 | 46 | 48 | BELUM CUKUP | 16 | 196/115 | -2.09 | -0.53 | 5.0 | -0.88 | – | -4.39 |
| 198 | `M26` Garis Trend Undur 3 Sentuhan + | **41.4** | 24 | 31 | 42 | 15 | BELUM CUKUP | 13 | 54/39 | -1.44 | -0.84 | 3.0 | -0.89 | – | -1.86 |
| 199 | `M126` Hidden Smash Day (beli, Larry  | **41.2** | 16 | 32 | 33 | 15 | BELUM CUKUP | 10 | 18/11 | -4.64 | -0.74 | 3.1 | -1.07 | – | -2.62 |
| 200 | `M50` Elder Triple Screen | **41.1** | 31 | 24 | 48 | 15 | BELUM CUKUP | 16 | 478/295 | -1.17 | -1.00 | 6.1 | -0.57 | – | -1.36 |
| 201 | `M55` Guppy GMMA | **40.5** | 26 | 27 | 47 | 15 | BELUM CUKUP | 16 | 177/110 | -2.64 | -0.81 | 4.2 | -0.72 | – | -2.90 |
| 202 | `M73` ADX(5) > 40 + Julat Terkecil 6 | **40.5** | 30 | 23 | 45 | 15 | BELUM CUKUP | 16 | 643/549 | -0.65 | -1.00 | 4.4 | -0.97 | – | -8.27 |
| 203 | `M66` IBD Undur Pertama ke Purata 50 | **40.3** | 24 | 27 | 47 | 15 | BELUM CUKUP | 16 | 193/125 | -2.08 | -0.63 | 5.6 | -0.68 | – | -2.52 |
| 204 | `M95` Nisbah Kebaharuan High 52 Ming | **40.3** | 20 | 33 | 44 | 15 | BELUM CUKUP | 15 | 110/60 | -2.85 | -0.70 | 3.7 | -0.77 | – | -2.80 |
| 205 | `M28` VWAP Separator + Kiss Pivot | **40.0** | 21 | 27 | 40 | 15 | BELUM CUKUP | 14 | 88/82 | -2.02 | -1.00 | 5.2 | -1.37 | – | -16.12 |
| 206 | `M29` EMA3 + RSI75 + Stokastik | **40.0** | 16 | 30 | 36 | 15 | BELUM CUKUP | 12 | 31/26 | -3.30 | -0.79 | 5.9 | -1.32 | – | -9.59 |
| 207 | `M57` Landry Trend Knockout (TKO) | **39.6** | 24 | 26 | 40 | 15 | BELUM CUKUP | 16 | 140/99 | -2.77 | -0.82 | 4.0 | -1.52 | – | -6.10 |
| 208 | `M119` 180 Bullish (Cooper) | **39.6** | 19 | 28 | 44 | 15 | BELUM CUKUP | 15 | 113/57 | -2.09 | -0.77 | 4.0 | -0.82 | – | -3.58 |
| 209 | `M11` NR7 Breakout + Volume | **39.3** | 19 | 27 | 40 | 15 | BELUM CUKUP | 15 | 95/68 | -1.70 | -0.72 | 5.3 | -1.30 | – | -1.96 |
| 210 | `M59` Anjakan Julat RSI | **39.2** | 16 | 24 | 41 | 15 | BELUM CUKUP | 13 | 35/15 | -5.66 | -0.60 | 2.7 | -0.61 | – | -3.35 |
| 211 | `M79` Radge: 20% Flipper | **39.1** | 18 | 30 | 41 | 15 | BELUM CUKUP | 16 | 254/71 | -3.60 | -0.60 | 3.9 | -1.25 | – | -2.86 |
| 212 | `M82` Arthur Hill Rotasi Sasaran 10% | **38.8** | 18 | 20 | 47 | 32 | BELUM CUKUP | 16 | 507/172 | -2.21 | -0.47 | 6.4 | -0.72 | – | -3.87 |
| 213 | `M101` Bulkowski: Tiga lembah menaik | **38.7** | 14 | 26 | 43 | 15 | BELUM CUKUP | 14 | 43/17 | -4.56 | -0.62 | 4.5 | -0.45 | – | -1.92 |
| 214 | `M47` Holy Grail Raschke | **38.3** | 9 | 18 | 27 | 15 | BELUM CUKUP | 10 | 21/18 | -4.70 | -0.98 | 4.5 | -2.16 | – | -27.83 |
| 215 | `M09` Volumatic VIDYA Pivot Retest | **38.3** | 6 | 12 | 29 | 15 | BELUM CUKUP | 9 | 23/14 | -5.47 | -1.00 | 6.4 | -1.76 | – | -14.83 |
| 216 | `M161` EMA 10/21 + Supertrend (10,3) | **38.0** | 23 | 14 | 49 | 15 | BELUM CUKUP | 16 | 393/168 | -1.28 | -0.89 | 8.2 | -0.44 | – | -1.35 |
| 217 | `M122` Moving Momentum (ChartSchool) | **37.2** | 17 | 22 | 33 | 15 | BELUM CUKUP | 16 | 92/56 | -3.86 | -1.00 | 4.7 | -2.11 | – | -7.38 |
| 218 | `M154` HOLP (High of Low Period) | **37.1** | 8 | 18 | 35 | 15 | BELUM CUKUP | 12 | 63/30 | -5.92 | -0.98 | 5.8 | -1.47 | – | -8.51 |
| 219 | `M01` Bollinger Band + RSI | **37.0** | 17 | 18 | 38 | 15 | BELUM CUKUP | 16 | 101/12 | -2.45 | -0.67 | 4.4 | -0.96 | – | -5.04 |
| 220 | `M123` CCI Correction (Lambert, Chart | **36.5** | 11 | 28 | 31 | 15 | BELUM CUKUP | 16 | 154/139 | -1.91 | -1.00 | 5.8 | -2.59 | – | -6.56 |
| 221 | `M76` Undercut & Rally pada Low Pent | **35.9** | 9 | 21 | 34 | 15 | BELUM CUKUP | 15 | 46/42 | -3.11 | -1.00 | 5.7 | -1.81 | – | -8.33 |
| 222 | `M81` Bensdorp Long Trend High Momen | **34.0** | 2 | 5 | 41 | 15 | BELUM CUKUP | 12 | 331/131 | -5.64 | -0.96 | 11.9 | -1.25 | – | -5.77 |
| 223 | `M90` Pring KST | **33.1** | 4 | 12 | 40 | 15 | BELUM CUKUP | 15 | 64/38 | -5.20 | -0.83 | 9.1 | -1.17 | – | -7.32 |

## Metrik dan sauh (0 · 50 · 100)

| Metrik | Berat | Apa | Sauh | Pakar |
|---|---|---|---|---|
| A1 | 20 | Jangkaan % setiap posisi, ditanda-ke-pasaran, kos ditolak | (-2.0, 0.0, 2.0) | Tharp, Minervini, Radge |
| A2 | 10 | Lebihan mata lorong T4 L1 lawan SPUS, tingkap sama | (-10.0, 0.0, 10.0) | Penanda aras SPUS (repo) |
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

