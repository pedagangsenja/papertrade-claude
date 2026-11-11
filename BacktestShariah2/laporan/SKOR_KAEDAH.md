# Skor Kaedah 0–100 (pangkat maklumat, BUKAN keputusan)

> **Status keputusan (kad skor, harga 2026-11-10):** TERBUKTI 0 · CALON 0 · BELUM CUKUP 223 · GAGAL 0 · NEGATIF 0. Rejim QQQ OFF sejak 2026-10-16. Hanya **TERBUKTI** layak untuk wang sebenar (`laporan/KAD_SKOR.md`); nombor dalam laporan ini BUKAN keputusan dan tidak boleh dibaca sebagai pangkat untuk wang sebenar.

Dijana 2026-11-11 oleh `standard/skor_kaedah.py` (Actions `analisis.yml`, selepas kad skor). Harga pada tutup 2026-11-10; 223 kaedah; 18 hari beli langsung (rejim ON 1, OFF 17). Pradaftar 2026-11-09: `standard/SPEC_SKOR_KAEDAH.md` (berat dan sauh dikunci `ujian/test_skor_kaedah.py::TestKunci`). Rekod analisis sahaja: tiada order, tiada wang sebenar.

## Cara membaca

- **Skor** = min geometri berberat empat tiang (Untung 35 · Tahan 30 · Bukti 25 · Konsisten 10), dikecut ke 50 mengikut data: berat data = hari beli ÷ (hari beli + 20). Kaedah dengan 2 hari beli tidak boleh menjauhi 50. 100 = unggul semua segi; 50 = neutral/tiada bukti; < 50 = lebih buruk daripada neutral.
- **Siling** ikut kad skor: NEGATIF ≤ 20, GANTUNG/BERSARA ≤ 30, GAGAL ≤ 40. Tanda ⌈ = siling terpakai.
- **Satu-satunya status yang membenarkan wang sebenar ialah TERBUKTI dalam `laporan/KAD_SKOR.md`.** Skor tinggi dengan status BELUM CUKUP bermaksud "paling menjanjikan setakat ini", bukan "selamat".
- Deflasi ujian berganda (López de Prado): sauh t Bukti C1 = maks(2.0, E[maks 223 normal]) = 2.80.
- **Semakan kebolehramalan:** belum ada snapshot skor ≥ 7 hari lalu (sejarah bermula 2026-11-10); skor dipercayai sebagai pangkat hanya selepas 8–12 minggu semakan positif.
- Metrik T4 (A2, B1, B2, D1) dikira atas lorong T4 L1 **dipotong pada sesi LANGSUNG pertama** kaedah itu (Mxx 2026-10-16, Nxx/GB 2026-11-03) dan diasas semula; sesi isian bina semula tidak dikira (pindaan 9 Nov 2026 (a)). Lajur "T4 sesi/pul" di bawah ialah potongan itu, bukan lorong penuh `T4_KAEDAH.md`.

## Semua kaedah, susun ikut Skor

| # | Kaedah | Skor | Untung | Tahan | Bukti | Konsisten | Status kad | Hari beli | Posisi/tutup | Jangkaan % | T4 sesi | T4 pul % | T4 pul/|MDD| | Ulcer | t buku | Lift | WFE |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `M33` Supertrend + SMA10 | **64.9** | 93 | 82 | 66 | 85 | BELUM CUKUP | 18 | 217/40 | +1.93 | 18 | +8.81 | +3.30 | 1.4 | +1.79 | – | 5.66 |
| 2 | `M146` 3-Bar Momentum Pattern | **64.7** | 89 | 87 | 67 | 85 | BELUM CUKUP | 17 | 77/28 | +1.66 | 18 | +6.24 | +1.01 | 2.1 | +2.09 | – | 3.39 |
| 3 | `M118` Expansion Pivot (Cooper) | **62.6** | 82 | 85 | 59 | 85 | BELUM CUKUP | 18 | 79/20 | +0.93 | 18 | +10.44 | +3.86 | 0.9 | +1.30 | – | 3.38 |
| 4 | `M133` Bull Hook (Crabel) | **62.0** | 96 | 88 | 59 | 85 | BELUM CUKUP | 12 | 47/22 | +1.80 | 18 | +7.43 | +1.79 | 1.5 | +1.43 | – | 14.28 |
| 5 | `M142` Pecahan volum dari dasar (底部放量 | **60.5** | 90 | 91 | 48 | 85 | BELUM CUKUP | 13 | 40/5 | +2.94 | 16 | +4.80 | +1.00 | 1.8 | +0.87 | – | 1.28 |
| 6 | `M25` VWAP Wave (proksi harian) | **60.4** | 77 | 80 | 60 | 80 | BELUM CUKUP | 16 | 169/85 | +0.57 | 18 | +5.95 | +1.03 | 3.0 | +0.93 | – | 5.40 |
| 7 | `M151` Outside Bar Failure | **60.1** | 73 | 83 | 56 | 85 | BELUM CUKUP | 17 | 92/47 | +0.09 | 18 | +7.47 | +6.14 | 0.5 | +0.68 | – | 1.29 |
| 8 | `M124` 'Last' Stochastic Technique (C | **59.8** | 72 | 75 | 60 | 85 | BELUM CUKUP | 18 | 366/164 | +0.30 | 18 | +6.74 | +1.47 | 2.3 | +0.74 | – | 1.31 |
| 9 | `M10` EMA3 + CCI + MACD | **59.4** | 75 | 71 | 58 | 85 | BELUM CUKUP | 18 | 112/50 | +0.49 | 18 | +9.15 | +1.74 | 1.9 | +0.74 | – | 1.92 |
| 10 | `M74` Lulus Baharu Trend Template Mi | **59.3** | 71 | 79 | 55 | 80 | BELUM CUKUP | 18 | 88/52 | +0.12 | 18 | +4.37 | +1.05 | 2.2 | +0.49 | – | 0.82 |
| 11 | `M111` Sistem Volatiliti Wilder | **59.1** | 75 | 65 | 62 | 85 | BELUM CUKUP | 18 | 250/76 | +0.74 | 18 | +4.69 | +0.70 | 3.5 | +1.06 | – | 2.07 |
| 12 | `M160` Measured Move Up | **58.9** | 65 | 79 | 62 | 85 | BELUM CUKUP | 16 | 105/46 | -0.09 | 18 | +5.17 | +1.11 | 2.1 | +1.33 | – | 10.13 |
| 13 | `M93` Bollinger Kaedah II: %b + MFI | **58.9** | 80 | 58 | 62 | 82 | BELUM CUKUP | 18 | 255/74 | +1.39 | 18 | +1.13 | +0.18 | 2.5 | +1.14 | – | 1.36 |
| 14 | `M100` Bulkowski Segi Empat & Segi Ti | **58.2** | 70 | 77 | 56 | 85 | BELUM CUKUP | 14 | 58/40 | +0.51 | 18 | +4.28 | +0.98 | 2.1 | +0.81 | – | 3.84 |
| 15 | `M137` Livermore System | **57.8** | 65 | 72 | 56 | 85 | BELUM CUKUP | 18 | 162/55 | -0.03 | 18 | +6.13 | +1.04 | 2.3 | +0.59 | – | 1.11 |
| 16 | `M23` Breitstein Kapitulasi + Kesina | **57.8** | 65 | 67 | 61 | 85 | BELUM CUKUP | 18 | 117/69 | -0.10 | 18 | +1.61 | +0.32 | 2.1 | +1.07 | – | 4.09 |
| 17 | `M145` Yum-Yum Continuation | **57.7** | 68 | 72 | 56 | 67 | BELUM CUKUP | 18 | 292/62 | +0.39 | 18 | +4.33 | +1.98 | 1.3 | +0.55 | – | 0.41 |
| 18 | `M105` Supertrend tulen | **57.6** | 73 | 59 | 62 | 76 | BELUM CUKUP | 18 | 351/94 | +0.89 | 18 | +1.86 | +0.26 | 3.1 | +1.06 | – | 2.27 |
| 19 | `M89` Chande 65sma-3cc | **57.3** | 66 | 65 | 58 | 85 | BELUM CUKUP | 18 | 155/80 | +0.03 | 18 | +3.03 | +0.58 | 2.4 | +0.68 | – | 1.67 |
| 20 | `M13` Garis Trend Action/Safety Line | **56.8** | 67 | 72 | 54 | 61 | BELUM CUKUP | 18 | 694/421 | -0.25 | 18 | +7.92 | +2.22 | 1.3 | +0.11 | – | 0.19 |
| 21 | `M30` BB Free Bar + Himpitan 50/2.5 | **56.3** | 73 | 57 | 62 | 58 | BELUM CUKUP | 18 | 226/68 | +0.72 | 18 | +3.16 | +0.42 | 4.7 | +1.10 | – | 1.86 |
| 22 | `M158` Doubly Adaptive Profit Targets | **56.2** | 78 | 56 | 63 | 45 | BELUM CUKUP | 18 | 347/126 | +1.27 | 18 | -0.52 | -0.09 | 2.6 | +1.13 | – | 2.77 |
| 23 | `M91` Stochastic Pop (Bernstein/Stec | **56.1** | 69 | 67 | 54 | 85 | BELUM CUKUP | 13 | 35/16 | +0.12 | 18 | +8.58 | +1.09 | 2.6 | +0.98 | – | 3.64 |
| 24 | `M80` Radge Saluran Purata Bergerak  | **55.7** | 78 | 52 | 63 | 45 | BELUM CUKUP | 18 | 260/55 | +1.54 | 18 | -1.16 | -0.16 | 3.7 | +1.33 | – | 1.47 |
| 25 | `M05` MACD Divergence + Pengesahan | **55.1** | 66 | 74 | 47 | 64 | BELUM CUKUP | 14 | 40/12 | +0.17 | 18 | +4.13 | +1.22 | 1.3 | +0.17 | – | 0.28 |
| 26 | `M46` Jurang Naik Boleh Beli (Buyabl | **54.7** | 64 | 71 | 50 | 79 | BELUM CUKUP | 11 | 34/17 | -0.25 | 18 | +2.38 | +0.48 | 1.7 | +0.47 | – | 0.79 |
| 27 | `M48` Cooper 1-2-3-4 | **54.7** | 64 | 58 | 53 | 85 | BELUM CUKUP | 15 | 51/16 | +0.06 | 18 | +7.72 | +1.42 | 2.1 | +0.74 | – | 1.96 |
| 28 | `M159` Heikin-Ashi Trend | **54.6** | 62 | 71 | 51 | 46 | BELUM CUKUP | 18 | 1535/1152 | -0.30 | 18 | +7.34 | +1.20 | 3.7 | -0.27 | – | -1.39 |
| 29 | `M70` Pecahan Hari Dalam | **54.6** | 66 | 68 | 56 | 35 | BELUM CUKUP | 18 | 390/306 | -0.11 | 18 | +2.16 | +0.44 | 2.3 | +0.26 | – | 0.67 |
| 30 | `M129` Wick Play | **54.4** | 75 | 61 | 49 | 85 | BELUM CUKUP | 9 | 23/9 | +0.57 | 18 | +5.85 | +2.07 | 1.0 | +0.69 | – | 2.85 |
| 31 | `M92` CCI-50 | **54.4** | 64 | 56 | 56 | 65 | BELUM CUKUP | 18 | 522/302 | +0.28 | 18 | +0.19 | +0.03 | 2.5 | +0.33 | – | 0.56 |
| 32 | `M15` Break & Retest + Henti ATR | **54.4** | 74 | 50 | 60 | 45 | BELUM CUKUP | 18 | 285/146 | +1.09 | 18 | -3.61 | -0.48 | 3.4 | +0.82 | – | 1.47 |
| 33 | `M77` Undercut & Rally pada Purata B | **54.3** | 61 | 74 | 46 | 55 | BELUM CUKUP | 16 | 53/33 | -0.37 | 18 | +2.59 | +0.82 | 1.6 | -0.39 | – | -0.56 |
| 34 | `M02` MACD + SMA200 | **54.2** | 61 | 65 | 50 | 55 | BELUM CUKUP | 18 | 113/58 | -0.51 | 18 | +10.10 | +2.29 | 1.8 | -0.18 | – | -0.87 |
| 35 | `M139` 均线首次粘合向上发散 (MA berhimpun kali  | **53.7** | 56 | 60 | 50 | 83 | BELUM CUKUP | 18 | 75/17 | -0.60 | 18 | +4.02 | +0.80 | 2.0 | +0.28 | – | 0.92 |
| 36 | `M117` Landry Pullback (high 2 bulan) | **53.6** | 75 | 48 | 57 | 45 | BELUM CUKUP | 15 | 127/17 | +1.34 | 18 | -4.55 | -0.58 | 3.6 | +1.22 | – | 1.27 |
| 37 | `M132` Ascending Scallop (Bulkowski) | **53.4** | 50 | 66 | 52 | 85 | BELUM CUKUP | 16 | 92/34 | -0.94 | 18 | +3.57 | +0.96 | 2.2 | +0.30 | – | 2.32 |
| 38 | `N53X36` Supertrend + ADX>25 → keluar s | **53.0** | 79 | 68 | 50 | 57 | BELUM CUKUP | 5 | 99/16 | +1.08 | 5 | +1.83 | +0.46 | 2.5 | +1.04 | – | – |
| 39 | `M35` Pocket Pivot Morales & Kacher | **52.8** | 64 | 50 | 57 | 45 | BELUM CUKUP | 18 | 303/204 | +0.09 | 18 | -0.98 | -0.11 | 4.9 | +0.46 | – | 2.44 |
| 40 | `M131` Ross Hook (Joe Ross) | **52.7** | 58 | 54 | 59 | 47 | BELUM CUKUP | 18 | 254/103 | -0.12 | 18 | -0.27 | -0.04 | 3.0 | +0.59 | – | 1.29 |
| 41 | `M18` EMA9/21 Pullback | **52.7** | 66 | 48 | 57 | 46 | BELUM CUKUP | 18 | 326/218 | +0.40 | 18 | -2.40 | -0.40 | 4.1 | +0.38 | – | 1.27 |
| 42 | `N40X36` OBV tinggi baharu + MA50 → kel | **52.2** | 77 | 59 | 43 | 68 | BELUM CUKUP | 5 | 44/7 | +1.07 | 5 | +0.45 | +0.09 | 2.9 | +0.58 | – | – |
| 43 | `N45X16` Undur EMA21 cerun positif → ke | **52.1** | 55 | 80 | 47 | 70 | BELUM CUKUP | 5 | 101/28 | -0.43 | 5 | +6.29 | +8.02 | 0.4 | +0.46 | – | – |
| 44 | `M21` Marius 3 Persediaan (Pecahan+J | **52.1** | 70 | 64 | 45 | 64 | BELUM CUKUP | 5 | 5/2 | +0.42 | 10 | +0.26 | +0.13 | 1.1 | +1.16 | – | 1.94 |
| 45 | `M88` O'Neil Shakeout +3 | **52.1** | 53 | 58 | 50 | 65 | BELUM CUKUP | 15 | 70/29 | -0.82 | 18 | +3.89 | +0.46 | 3.4 | +0.19 | – | 0.34 |
| 46 | `N64X36` Episodic pivot → keluar selepa | **51.9** | 75 | 70 | 33 | 70 | BELUM CUKUP | 5 | 44/2 | +1.16 | 5 | +0.85 | +0.21 | 2.4 | -0.17 | – | – |
| 47 | `M150` Trend Bar Failure (Brooks) | **51.9** | 65 | 51 | 52 | 38 | BELUM CUKUP | 17 | 98/39 | +0.57 | 18 | -2.94 | -0.53 | 2.4 | +0.26 | – | 0.77 |
| 48 | `N68X36` Bullish engulfing + EMA21 → ke | **51.8** | 58 | 76 | 41 | 70 | BELUM CUKUP | 5 | 38/7 | -0.22 | 5 | +3.10 | +1.44 | 1.4 | +0.38 | – | – |
| 49 | `N64X14` Episodic pivot → keluar bila r | **51.7** | 76 | 67 | 32 | 70 | BELUM CUKUP | 5 | 44/1 | +1.33 | 5 | -0.12 | -0.03 | 2.3 | -0.15 | – | – |
| 50 | `M37` Weinstein Peringkat 2 | **51.6** | 75 | 92 | 31 | 59 | BELUM CUKUP | 3 | 7/0 | +0.82 | 12 | +0.71 | +1.41 | 0.2 | +0.19 | – | 0.15 |
| 51 | `N64X17` Episodic pivot → keluar bila a | **51.4** | 65 | 67 | 36 | 70 | BELUM CUKUP | 5 | 44/8 | +0.59 | 5 | +0.78 | +0.20 | 2.3 | -0.35 | – | – |
| 52 | `N64X16` Episodic pivot → keluar bila s | **51.3** | 69 | 65 | 34 | 70 | BELUM CUKUP | 5 | 44/3 | +0.94 | 5 | -0.12 | -0.03 | 2.3 | -0.26 | – | – |
| 53 | `M134` First Kiss After Daylight (Lan | **51.3** | 59 | 49 | 54 | 45 | BELUM CUKUP | 15 | 53/16 | +0.03 | 18 | -1.27 | -0.18 | 3.2 | +0.87 | – | 0.99 |
| 54 | `N124X15` Episodic pivot gap 8-10% → eko | **51.2** | 77 | 63 | 28 | 70 | BELUM CUKUP | 5 | 37/0 | +1.40 | 5 | -0.76 | -0.11 | 3.6 | -0.28 | – | – |
| 55 | `N75X17` RSI14 < 40 tanpa penapis → kel | **51.2** | 58 | 66 | 39 | 70 | BELUM CUKUP | 5 | 239/104 | +0.24 | 5 | +0.56 | +0.14 | 2.4 | -0.94 | – | – |
| 56 | `M04` BB Squeeze Breakout | **51.2** | 52 | 47 | 56 | 65 | BELUM CUKUP | 17 | 148/50 | -0.61 | 18 | +2.78 | +0.35 | 4.0 | +0.61 | – | 1.01 |
| 57 | `N40X16` OBV tinggi baharu + MA50 → kel | **51.1** | 65 | 53 | 44 | 70 | BELUM CUKUP | 5 | 56/14 | +0.32 | 5 | -0.24 | -0.04 | 3.1 | +0.39 | – | – |
| 58 | `M104` High Tight Flag / Power Play | **51.0** | 78 | 90 | 51 | 65 | BELUM CUKUP | 1 | 1/0 | +14.59 | 3 | +1.48 | +10.00 | 0.0 | +3.39 | – | 27.61 |
| 59 | `N68X16` Bullish engulfing + EMA21 → ke | **50.9** | 49 | 74 | 39 | 70 | BELUM CUKUP | 5 | 39/9 | -0.67 | 5 | +2.66 | +1.29 | 1.4 | +0.06 | – | – |
| 60 | `N22X36` BB pecah atas + RSI → keluar s | **50.8** | 47 | 64 | 49 | 70 | BELUM CUKUP | 5 | 102/19 | -0.75 | 5 | +1.75 | +0.46 | 2.3 | +0.90 | – | – |
| 61 | `M116` 2/20 EMA Breakout (Landry) | **50.8** | 57 | 44 | 58 | 45 | BELUM CUKUP | 18 | 536/339 | +0.10 | 18 | -0.31 | -0.03 | 6.9 | +0.48 | – | 1.90 |
| 62 | `N25X36` Supertrend + EMA + ADX>23 → ke | **50.7** | 58 | 59 | 40 | 61 | BELUM CUKUP | 5 | 97/12 | +0.00 | 5 | +0.07 | +0.02 | 2.8 | +0.03 | – | – |
| 63 | `M153` Range Leader | **50.7** | 55 | 46 | 57 | 45 | BELUM CUKUP | 18 | 1210/917 | -0.07 | 18 | -1.30 | -0.13 | 6.0 | +0.40 | – | 2.18 |
| 64 | `M39` Radge Pecahan Bollinger 100 ha | **50.7** | 41 | 65 | 52 | 58 | BELUM CUKUP | 18 | 230/49 | -1.48 | 18 | +6.30 | +2.63 | 1.2 | +0.05 | – | 0.11 |
| 65 | `N36X16` Pocket pivot → keluar bila sup | **50.6** | 49 | 68 | 39 | 70 | BELUM CUKUP | 5 | 136/39 | -0.71 | 5 | +2.72 | +1.85 | 0.7 | -0.53 | – | – |
| 66 | `M51` O'Neil Cawan & Pemegang | **50.5** | 64 | 61 | 40 | 62 | BELUM CUKUP | 2 | 3/0 | +0.09 | 8 | +0.08 | +0.08 | 0.5 | +1.34 | – | 4.47 |
| 67 | `N45X36` Undur EMA21 cerun positif → ke | **50.5** | 48 | 69 | 40 | 67 | BELUM CUKUP | 5 | 80/21 | -0.54 | 5 | +1.42 | +0.68 | 1.3 | -0.24 | – | – |
| 68 | `N42X14` Lonjakan volum 2x → keluar bil | **50.5** | 67 | 50 | 34 | 70 | BELUM CUKUP | 5 | 150/8 | +0.93 | 5 | -2.20 | -0.20 | 6.3 | -0.48 | – | – |
| 69 | `M107` Golden Cross SMA50/200 | **50.5** | 60 | 58 | 46 | 27 | BELUM CUKUP | 15 | 30/7 | -0.02 | 18 | +0.69 | +0.20 | 1.7 | +0.24 | – | 0.40 |
| 70 | `N75X14` RSI14 < 40 tanpa penapis → kel | **50.2** | 61 | 54 | 33 | 70 | BELUM CUKUP | 5 | 179/16 | +0.64 | 5 | -2.17 | -0.39 | 3.8 | -0.91 | – | – |
| 71 | `N75X13` RSI14 < 40 tanpa penapis → kel | **50.1** | 62 | 60 | 28 | 70 | BELUM CUKUP | 5 | 118/1 | +0.52 | 5 | -0.85 | -0.23 | 2.3 | -0.67 | – | – |
| 72 | `N124X36` Episodic pivot gap 8-10% → kel | **50.1** | 67 | 52 | 36 | 40 | BELUM CUKUP | 5 | 37/9 | +0.77 | 5 | -2.46 | -0.50 | 3.3 | -0.30 | – | – |
| 73 | `N35X36` Pecah 52 minggu tinggi → kelua | **50.0** | 47 | 73 | 30 | 70 | BELUM CUKUP | 4 | 36/1 | -0.47 | 5 | +1.19 | +0.66 | 1.1 | -0.30 | – | – |
| 74 | `N75X15` RSI14 < 40 tanpa penapis → eko | **49.9** | 62 | 60 | 25 | 70 | BELUM CUKUP | 5 | 118/0 | +0.55 | 5 | -0.85 | -0.23 | 2.3 | -0.65 | – | – |
| 75 | `N42X36` Lonjakan volum 2x → keluar sel | **49.9** | 56 | 46 | 40 | 70 | BELUM CUKUP | 5 | 163/65 | +0.28 | 5 | -2.32 | -0.31 | 4.7 | -0.60 | – | – |
| 76 | `N80X36` Tinggi sepanjang masa → keluar | **49.9** | 59 | 55 | 36 | 42 | BELUM CUKUP | 4 | 28/1 | +0.36 | 5 | -0.75 | -0.22 | 1.9 | +0.44 | – | – |
| 77 | `M08` SMA20 + SMA200 | **49.8** | 53 | 42 | 52 | 53 | BELUM CUKUP | 16 | 168/89 | -0.17 | 18 | -2.16 | -0.40 | 3.8 | -0.03 | – | -0.10 |
| 78 | `N25X17` Supertrend + EMA + ADX>23 → ke | **49.7** | 51 | 60 | 31 | 66 | BELUM CUKUP | 5 | 86/1 | -0.32 | 5 | +0.13 | +0.03 | 3.0 | -0.24 | – | – |
| 79 | `N42X15` Lonjakan volum 2x → ekori Chan | **49.7** | 66 | 50 | 26 | 70 | BELUM CUKUP | 5 | 142/0 | +0.82 | 5 | -1.88 | -0.16 | 6.5 | -0.54 | – | – |
| 80 | `N42X17` Lonjakan volum 2x → keluar bil | **49.7** | 52 | 47 | 38 | 70 | BELUM CUKUP | 5 | 162/37 | +0.04 | 5 | -2.19 | -0.23 | 5.9 | -0.59 | – | – |
| 81 | `M143` 장대양봉 이후 눌림목 / 5일선 매매 (Undur ke | **49.6** | 52 | 67 | 30 | 52 | BELUM CUKUP | 10 | 19/1 | +0.08 | 17 | +0.60 | +0.20 | 1.5 | -0.72 | – | -8.23 |
| 82 | `N42X16` Lonjakan volum 2x → keluar bil | **49.6** | 54 | 44 | 40 | 69 | BELUM CUKUP | 5 | 166/64 | +0.21 | 5 | -2.77 | -0.43 | 4.4 | -0.59 | – | – |
| 83 | `N36X36` Pocket pivot → keluar selepas  | **49.6** | 49 | 49 | 38 | 70 | BELUM CUKUP | 5 | 133/42 | -0.65 | 5 | +1.14 | +0.22 | 2.8 | -0.70 | – | – |
| 84 | `N25X16` Supertrend + EMA + ADX>23 → ke | **49.4** | 48 | 58 | 32 | 59 | BELUM CUKUP | 5 | 88/2 | -0.45 | 5 | -0.26 | -0.05 | 3.0 | -0.33 | – | – |
| 85 | `N37X36` Gap and go → keluar selepas DU | **49.4** | 45 | 57 | 34 | 70 | BELUM CUKUP | 5 | 73/12 | -0.72 | 5 | +1.35 | +0.37 | 2.3 | -0.74 | – | – |
| 86 | `N28X36` ADX>25 + DI+ > DI- → keluar se | **49.3** | 52 | 39 | 42 | 69 | BELUM CUKUP | 5 | 184/74 | +0.11 | 5 | -3.46 | -0.55 | 4.4 | -0.46 | – | – |
| 87 | `N41X36` CMF20>0 + tutup>EMA20 → keluar | **49.3** | 44 | 50 | 40 | 70 | BELUM CUKUP | 5 | 154/73 | -1.00 | 5 | +0.27 | +0.05 | 2.8 | -0.68 | – | – |
| 88 | `N43X36` Undur EMA8 + penapis MA50 → ke | **49.3** | 46 | 52 | 35 | 70 | BELUM CUKUP | 5 | 123/19 | -0.63 | 5 | +0.46 | +0.12 | 2.4 | -0.72 | – | – |
| 89 | `N19X13` Bawah jalur BB + RSI<30 → kelu | **49.3** | 72 | 49 | 28 | 30 | BELUM CUKUP | 5 | 101/0 | +1.55 | 5 | -3.02 | -0.92 | 2.7 | -0.34 | – | – |
| 90 | `M34` Carter TTM Squeeze | **49.2** | 54 | 41 | 52 | 43 | BELUM CUKUP | 17 | 100/46 | -0.27 | 18 | +0.62 | +0.08 | 3.6 | +0.15 | – | 0.51 |
| 91 | `N07X16` Tiga MA tersusun → keluar bila | **49.2** | 50 | 58 | 38 | 30 | BELUM CUKUP | 5 | 93/10 | -0.30 | 5 | -0.21 | -0.05 | 2.2 | -0.19 | – | – |
| 92 | `M27` Price Action 4 Tiang | **49.2** | 49 | 42 | 45 | 15 | BELUM CUKUP | 2 | 547/434 | -0.67 | 18 | -2.31 | -0.45 | 2.9 | -0.13 | – | -0.37 |
| 93 | `M07` Qullamaggie Breakout | **49.2** | 28 | 64 | 27 | 15 | BELUM CUKUP | 1 | 1/1 | -2.53 | 18 | -0.25 | -0.21 | 0.7 | -0.22 | – | -1.12 |
| 94 | `N09X36` Undur EMA10 + penapis EMA50 →  | **49.1** | 43 | 50 | 37 | 70 | BELUM CUKUP | 5 | 135/29 | -0.76 | 5 | -0.12 | -0.03 | 2.3 | -0.62 | – | – |
| 95 | `N28X14` ADX>25 + DI+ > DI- → keluar bi | **49.1** | 50 | 50 | 33 | 60 | BELUM CUKUP | 5 | 114/7 | -0.28 | 5 | -1.36 | -0.22 | 3.8 | -0.65 | – | – |
| 96 | `N41X16` CMF20>0 + tutup>EMA20 → keluar | **49.1** | 36 | 62 | 37 | 70 | BELUM CUKUP | 5 | 187/71 | -1.30 | 5 | +0.94 | +0.44 | 1.3 | -0.98 | – | – |
| 97 | `N33X36` Donchian20 + penapis MA200 → k | **49.0** | 44 | 54 | 33 | 60 | BELUM CUKUP | 5 | 77/9 | -0.67 | 5 | -0.82 | -0.23 | 2.2 | -0.69 | – | – |
| 98 | `N37X17` Gap and go → keluar bila adx14 | **49.0** | 40 | 57 | 33 | 70 | BELUM CUKUP | 5 | 73/18 | -0.96 | 5 | +1.57 | +0.43 | 2.1 | -0.92 | – | – |
| 99 | `M45` High 52 Minggu (George & Hwang | **49.0** | 18 | 43 | 30 | 40 | BELUM CUKUP | 1 | 2/1 | -4.00 | 7 | -0.78 | -0.43 | 1.0 | +0.16 | – | 0.83 |
| 100 | `N56X17` RSI>50 + ADX>20 → keluar bila  | **48.9** | 44 | 54 | 30 | 70 | BELUM CUKUP | 5 | 102/6 | -0.63 | 5 | -0.54 | -0.11 | 3.0 | -0.90 | – | – |
| 101 | `N07X36` Tiga MA tersusun → keluar sele | **48.9** | 49 | 54 | 36 | 30 | BELUM CUKUP | 5 | 95/8 | -0.31 | 5 | -0.68 | -0.17 | 2.4 | -0.24 | – | – |
| 102 | `N37X14` Gap and go → keluar bila rsi14 | **48.9** | 46 | 50 | 31 | 70 | BELUM CUKUP | 5 | 72/5 | -0.41 | 5 | -0.24 | -0.06 | 2.1 | -0.74 | – | – |
| 103 | `N65X14` Gap 4% + volum + hampir 52w →  | **48.9** | 52 | 51 | 26 | 54 | BELUM CUKUP | 4 | 26/1 | -0.03 | 5 | -1.49 | -0.36 | 2.7 | -0.84 | – | – |
| 104 | `M106` DMI Wilder | **48.8** | 53 | 40 | 54 | 35 | BELUM CUKUP | 16 | 113/53 | -0.13 | 18 | -2.65 | -0.59 | 2.6 | +0.39 | – | 0.68 |
| 105 | `N37X16` Gap and go → keluar bila super | **48.8** | 42 | 52 | 32 | 70 | BELUM CUKUP | 5 | 73/11 | -0.74 | 5 | +0.39 | +0.10 | 2.2 | -0.85 | – | – |
| 106 | `N76X36` Tutup > MA50 (penapis trend tu | **48.8** | 50 | 38 | 37 | 62 | BELUM CUKUP | 5 | 116/32 | -0.31 | 5 | -3.26 | -0.59 | 3.9 | -0.67 | – | – |
| 107 | `N65X36` Gap 4% + volum + hampir 52w →  | **48.8** | 53 | 52 | 23 | 55 | BELUM CUKUP | 4 | 26/0 | -0.00 | 5 | -1.39 | -0.33 | 2.7 | -0.83 | – | – |
| 108 | `N66X36` 52w tinggi + pengesahan 1% → k | **48.8** | 49 | 48 | 29 | 50 | BELUM CUKUP | 4 | 31/1 | -0.24 | 4 | -1.33 | -0.32 | 3.0 | -0.42 | – | – |
| 109 | `M31` Band Walk (BB 20/2) | **48.7** | 57 | 33 | 58 | 45 | BELUM CUKUP | 18 | 391/72 | +0.30 | 18 | -2.74 | -0.25 | 6.8 | +0.60 | – | 1.01 |
| 110 | `M148` Natural Number Method | **48.7** | 38 | 60 | 44 | 55 | BELUM CUKUP | 18 | 205/125 | -1.59 | 18 | +2.25 | +0.45 | 2.2 | -1.04 | – | -3.62 |
| 111 | `M32` Momentum Burst | **48.7** | 64 | 29 | 52 | 45 | BELUM CUKUP | 12 | 53/32 | +0.39 | 18 | -3.81 | -0.35 | 6.6 | +0.44 | – | 1.26 |
| 112 | `N22X16` BB pecah atas + RSI → keluar b | **48.7** | 38 | 52 | 45 | 37 | BELUM CUKUP | 5 | 104/15 | -0.91 | 5 | -0.43 | -0.12 | 2.3 | +0.55 | – | – |
| 113 | `N73X13` Tutup bawah jalur bawah BB(20, | **48.7** | 55 | 55 | 27 | 31 | BELUM CUKUP | 5 | 134/1 | +0.19 | 5 | -1.19 | -0.19 | 3.3 | -0.71 | – | – |
| 114 | `N24X17` Supertrend(10,3) + ADX>20 → ke | **48.7** | 42 | 56 | 28 | 70 | BELUM CUKUP | 5 | 92/3 | -0.80 | 5 | -0.21 | -0.06 | 2.1 | -0.89 | – | – |
| 115 | `N24X36` Supertrend(10,3) + ADX>20 → ke | **48.7** | 53 | 37 | 39 | 45 | BELUM CUKUP | 5 | 109/26 | -0.18 | 5 | -2.38 | -0.52 | 3.1 | -0.35 | – | – |
| 116 | `N08X36` tutup>EMA20 tidak terlalu jauh | **48.6** | 41 | 44 | 38 | 70 | BELUM CUKUP | 5 | 220/108 | -0.99 | 5 | -1.35 | -0.25 | 3.3 | -1.01 | – | – |
| 117 | `N28X17` ADX>25 + DI+ > DI- → keluar bi | **48.6** | 49 | 52 | 24 | 67 | BELUM CUKUP | 5 | 73/0 | -0.36 | 5 | -1.23 | -0.17 | 4.3 | -0.77 | – | – |
| 118 | `N53X16` Supertrend + ADX>25 → keluar b | **48.6** | 49 | 48 | 37 | 30 | BELUM CUKUP | 5 | 88/2 | -0.31 | 5 | -2.10 | -0.48 | 3.1 | +0.28 | – | – |
| 119 | `N53X17` Supertrend + ADX>25 → keluar b | **48.6** | 50 | 49 | 34 | 30 | BELUM CUKUP | 5 | 82/0 | -0.24 | 5 | -1.84 | -0.45 | 3.1 | +0.35 | – | – |
| 120 | `M84` Jarak purata bergerak MAD 21/2 | **48.6** | 18 | 16 | 33 | 15 | BELUM CUKUP | 1 | 58/37 | -3.72 | 7 | -7.40 | -0.94 | 5.9 | -0.69 | – | -2.67 |
| 121 | `N33X16` Donchian20 + penapis MA200 → k | **48.5** | 38 | 55 | 30 | 70 | BELUM CUKUP | 5 | 79/6 | -1.03 | 5 | -0.04 | -0.01 | 2.0 | -0.93 | – | – |
| 122 | `M94` Pecutan Momentum (Chen, Yu & W | **48.4** | 17 | 13 | 18 | 15 | BELUM CUKUP | 1 | 33/0 | -6.92 | 7 | -6.86 | -0.58 | 7.6 | -1.08 | – | -4.65 |
| 123 | `N56X16` RSI>50 + ADX>20 → keluar bila  | **48.3** | 38 | 44 | 36 | 70 | BELUM CUKUP | 5 | 141/34 | -0.67 | 5 | -2.59 | -0.51 | 3.7 | -0.89 | – | – |
| 124 | `N74X16` MACD atas garis isyarat (keada | **48.3** | 40 | 38 | 39 | 70 | BELUM CUKUP | 5 | 267/137 | -0.58 | 5 | -4.04 | -0.55 | 5.5 | -0.89 | – | – |
| 125 | `M41` FW Penyatuan Mingguan | **48.3** | 45 | 30 | 43 | 45 | BELUM CUKUP | 4 | 63/9 | -0.14 | 17 | -5.16 | -0.62 | 4.3 | +0.58 | – | 1.05 |
| 126 | `N22X14` BB pecah atas + RSI → keluar b | **48.2** | 37 | 46 | 37 | 56 | BELUM CUKUP | 5 | 104/10 | -1.11 | 5 | -0.89 | -0.20 | 2.8 | -0.25 | – | – |
| 127 | `M144` Screw Bar | **48.2** | 52 | 47 | 37 | 15 | BELUM CUKUP | 5 | 8/6 | -0.41 | 16 | -0.31 | -0.12 | 0.9 | -0.09 | – | -0.29 |
| 128 | `N33X14` Donchian20 + penapis MA200 → k | **48.2** | 38 | 50 | 31 | 59 | BELUM CUKUP | 5 | 87/4 | -1.05 | 5 | -0.64 | -0.15 | 2.5 | -0.69 | – | – |
| 129 | `M138` 直升机空中加油 (Helikopter isi minyak | **48.2** | 30 | 53 | 22 | 15 | BELUM CUKUP | 2 | 2/0 | -1.30 | 11 | -0.22 | -0.34 | 0.3 | -0.79 | – | -1.04 |
| 130 | `M96` Momo India: Ranking Sharpe 3/6 | **48.2** | 14 | 10 | 9 | 15 | BELUM CUKUP | 1 | 6/6 | -13.40 | 7 | -8.03 | -1.00 | 5.6 | -5.74 | – | -15.35 |
| 131 | `N47X16` NR7 + EMA9>EMA21 → keluar bila | **48.1** | 38 | 53 | 28 | 57 | BELUM CUKUP | 5 | 65/11 | -0.77 | 5 | -1.20 | -0.28 | 2.7 | -1.36 | – | – |
| 132 | `N06X36` Golden cross MA50/MA200 → kelu | **48.1** | 36 | 50 | 25 | 64 | BELUM CUKUP | 4 | 10/2 | -1.20 | 5 | -1.07 | -0.26 | 2.5 | -1.01 | – | – |
| 133 | `M78` Alvarez Pecahan Mingguan DTAYS | **48.1** | 24 | 24 | 42 | 34 | BELUM CUKUP | 2 | 73/39 | -1.60 | 17 | -7.71 | -0.75 | 6.2 | +0.16 | – | 0.62 |
| 134 | `M149` 3-Step Pullback | **48.0** | 50 | 38 | 56 | 32 | BELUM CUKUP | 16 | 197/53 | -0.20 | 18 | -3.42 | -0.32 | 5.3 | +0.65 | – | 0.56 |
| 135 | `N28X16` ADX>25 + DI+ > DI- → keluar bi | **48.0** | 38 | 40 | 35 | 70 | BELUM CUKUP | 5 | 196/76 | -0.68 | 5 | -3.47 | -0.55 | 4.3 | -1.30 | – | – |
| 136 | `N76X16` Tutup > MA50 (penapis trend tu | **48.0** | 33 | 49 | 33 | 70 | BELUM CUKUP | 5 | 197/64 | -1.26 | 5 | -0.59 | -0.17 | 2.1 | -1.46 | – | – |
| 137 | `N39X36` NR7 kemudian pecah → keluar se | **48.0** | 18 | 44 | 24 | 50 | BELUM CUKUP | 2 | 18/5 | -2.98 | 4 | +0.04 | +0.01 | 2.3 | -1.17 | – | – |
| 138 | `N24X16` Supertrend(10,3) + ADX>20 → ke | **47.8** | 39 | 50 | 26 | 56 | BELUM CUKUP | 5 | 86/2 | -0.89 | 5 | -0.89 | -0.26 | 2.1 | -1.02 | – | – |
| 139 | `N50X14` Mampat + pecah volum 1.5x → ke | **47.8** | 24 | 45 | 27 | 70 | BELUM CUKUP | 3 | 12/2 | -2.01 | 5 | -2.26 | -0.24 | 5.1 | -0.69 | – | – |
| 140 | `M36` Turtle 55/20 | **47.6** | 47 | 40 | 56 | 32 | BELUM CUKUP | 18 | 322/150 | -0.64 | 18 | -1.42 | -0.12 | 6.4 | +0.24 | – | 0.58 |
| 141 | `N08X16` tutup>EMA20 tidak terlalu jauh | **47.6** | 34 | 37 | 36 | 70 | BELUM CUKUP | 5 | 273/110 | -1.18 | 5 | -2.13 | -0.68 | 2.5 | -1.24 | – | – |
| 142 | `N50X17` Mampat + pecah volum 1.5x → ke | **47.5** | 19 | 44 | 28 | 70 | BELUM CUKUP | 3 | 12/2 | -2.22 | 5 | -2.39 | -0.26 | 5.1 | -0.67 | – | – |
| 143 | `N27X16` Ichimoku atas awan → keluar bi | **47.4** | 31 | 45 | 30 | 66 | BELUM CUKUP | 5 | 110/32 | -1.23 | 5 | -1.41 | -0.48 | 1.9 | -1.56 | – | – |
| 144 | `N36X14` Pocket pivot → keluar bila rsi | **47.4** | 41 | 32 | 35 | 47 | BELUM CUKUP | 5 | 130/17 | -0.69 | 5 | -3.17 | -0.47 | 4.3 | -0.71 | – | – |
| 145 | `N38X36` VCP pecah → keluar selepas DUA | **47.3** | 35 | 46 | 27 | 43 | BELUM CUKUP | 5 | 20/5 | -0.96 | 5 | -1.03 | -0.32 | 2.1 | -1.21 | – | – |
| 146 | `N54X16` Supertrend + RSI>50 → keluar b | **47.2** | 36 | 38 | 26 | 70 | BELUM CUKUP | 5 | 101/3 | -0.80 | 5 | -3.29 | -0.41 | 5.0 | -1.19 | – | – |
| 147 | `N119X13` 3 tutup turun berturut → kelua | **47.0** | 40 | 35 | 30 | 30 | BELUM CUKUP | 5 | 136/27 | -0.12 | 5 | -6.89 | -0.84 | 7.1 | -1.48 | – | – |
| 148 | `N51X16` BB squeeze + Supertrend → kelu | **46.9** | 21 | 38 | 22 | 30 | BELUM CUKUP | 3 | 4/1 | -3.63 | 5 | -1.40 | -0.55 | 1.8 | -1.20 | – | – |
| 149 | `N51X36` BB squeeze + Supertrend → kelu | **46.9** | 21 | 37 | 22 | 30 | BELUM CUKUP | 3 | 4/2 | -3.68 | 5 | -1.44 | -0.56 | 1.9 | -1.36 | – | – |
| 150 | `N56X36` RSI>50 + ADX>20 → keluar selep | **46.8** | 35 | 30 | 34 | 47 | BELUM CUKUP | 5 | 128/38 | -0.87 | 5 | -4.93 | -0.67 | 5.6 | -1.15 | – | – |
| 151 | `M127` Slingshot Bullish | **46.7** | 44 | 54 | 46 | 15 | BELUM CUKUP | 16 | 105/72 | -1.25 | 18 | +0.05 | +0.01 | 2.9 | -0.63 | – | -0.88 |
| 152 | `N119X15` 3 tutup turun berturut → ekori | **46.7** | 37 | 38 | 16 | 36 | BELUM CUKUP | 4 | 37/0 | -0.67 | 5 | -4.48 | -0.66 | 5.2 | -1.65 | – | – |
| 153 | `M152` Spike & Ledge | **46.6** | 34 | 51 | 44 | 44 | BELUM CUKUP | 15 | 41/8 | -1.21 | 18 | +1.32 | +0.32 | 2.4 | -0.08 | – | -0.28 |
| 154 | `N55X13` BB + RSI + ADX>20 → keluar bil | **46.6** | 42 | 40 | 19 | 30 | BELUM CUKUP | 5 | 52/0 | -0.52 | 5 | -3.76 | -0.82 | 3.7 | -1.36 | – | – |
| 155 | `N31X36` Turtle sistem 2 → keluar selep | **46.6** | 28 | 42 | 27 | 45 | BELUM CUKUP | 5 | 85/3 | -1.47 | 5 | -1.49 | -0.41 | 2.4 | -1.02 | – | – |
| 156 | `M01` Bollinger Band + RSI | **46.5** | 65 | 37 | 43 | 15 | BELUM CUKUP | 18 | 110/18 | +1.03 | 18 | -4.29 | -0.40 | 4.3 | -0.51 | – | -2.29 |
| 157 | `M155` Market Cycle Strategy | **46.5** | 55 | 37 | 53 | 15 | BELUM CUKUP | 18 | 626/224 | +0.01 | 18 | -2.34 | -0.39 | 3.5 | -0.04 | – | -0.06 |
| 158 | `N54X36` Supertrend + RSI>50 → keluar s | **46.5** | 36 | 27 | 35 | 30 | BELUM CUKUP | 5 | 129/35 | -0.62 | 5 | -6.24 | -0.77 | 6.2 | -0.95 | – | – |
| 159 | `M64` O'Neil Tiga Minggu Ketat | **46.5** | 24 | 24 | 27 | 15 | BELUM CUKUP | 3 | 3/1 | -10.77 | 18 | -3.18 | -0.81 | 2.1 | -0.84 | – | -11.29 |
| 160 | `M128` Inventory Retracement Bar (IRB | **46.4** | 48 | 32 | 53 | 33 | BELUM CUKUP | 18 | 146/73 | -0.37 | 18 | -5.03 | -0.45 | 6.2 | +0.11 | – | 0.61 |
| 161 | `M136` Short/Intermediate-term Low (L | **46.4** | 48 | 42 | 54 | 16 | BELUM CUKUP | 18 | 713/254 | -0.54 | 18 | -1.50 | -0.32 | 2.5 | +0.04 | – | 0.02 |
| 162 | `N57X36` ADX bangkit daripada <20 → kel | **46.4** | 23 | 53 | 29 | 31 | BELUM CUKUP | 5 | 55/6 | -1.85 | 5 | +0.55 | +0.16 | 2.2 | -0.99 | – | – |
| 163 | `M54` IBD Power Trend | **46.3** | 46 | 44 | 52 | 15 | BELUM CUKUP | 17 | 200/103 | -0.95 | 18 | +1.12 | +0.11 | 5.5 | -0.11 | – | -0.25 |
| 164 | `N48X36` Inside day pecah → keluar sele | **46.3** | 28 | 34 | 34 | 35 | BELUM CUKUP | 5 | 238/43 | -0.91 | 5 | -5.86 | -0.70 | 6.6 | -1.21 | – | – |
| 165 | `N57X16` ADX bangkit daripada <20 → kel | **46.2** | 22 | 52 | 28 | 31 | BELUM CUKUP | 5 | 53/4 | -1.91 | 5 | +0.55 | +0.16 | 2.2 | -1.04 | – | – |
| 166 | `M20` EMA10/15 Crossover + Sudut | **46.1** | 44 | 46 | 48 | 18 | BELUM CUKUP | 18 | 435/336 | -0.87 | 18 | -1.62 | -0.28 | 2.7 | -0.65 | – | -4.69 |
| 167 | `M14` Walking with the Whales | **46.1** | 53 | 37 | 52 | 15 | BELUM CUKUP | 18 | 852/569 | -0.15 | 18 | -6.21 | -0.58 | 5.8 | -0.18 | – | -0.31 |
| 168 | `M157` Consolidation Pivot Breakout ( | **46.1** | 23 | 37 | 28 | 15 | BELUM CUKUP | 4 | 4/3 | -4.87 | 15 | -1.93 | -0.66 | 1.3 | -0.82 | – | -2.68 |
| 169 | `M38` Darvas Kotak | **46.1** | 16 | 31 | 34 | 45 | BELUM CUKUP | 4 | 23/1 | -2.49 | 17 | -2.85 | -0.29 | 4.2 | +0.17 | – | 1.00 |
| 170 | `M102` Stockbee SLTB | **46.0** | 48 | 41 | 52 | 15 | BELUM CUKUP | 18 | 357/259 | -0.89 | 18 | -2.58 | -0.24 | 5.4 | -0.16 | – | -0.48 |
| 171 | `M115` Bow Tie (Landry) | **46.0** | 29 | 40 | 48 | 45 | BELUM CUKUP | 10 | 35/20 | -1.74 | 18 | -3.93 | -0.50 | 3.5 | +0.26 | – | 1.60 |
| 172 | `N27X36` Ichimoku atas awan → keluar se | **46.0** | 28 | 36 | 27 | 30 | BELUM CUKUP | 5 | 72/6 | -1.37 | 5 | -2.73 | -0.63 | 3.1 | -1.23 | – | – |
| 173 | `N47X36` NR7 + EMA9>EMA21 → keluar sele | **46.0** | 22 | 35 | 24 | 30 | BELUM CUKUP | 4 | 58/9 | -1.54 | 5 | -4.27 | -0.62 | 5.0 | -1.71 | – | – |
| 174 | `M49` Ichimoku (Tutup Atas Awan + Te | **45.9** | 45 | 44 | 50 | 15 | BELUM CUKUP | 18 | 279/148 | -0.95 | 18 | -1.07 | -0.16 | 3.3 | -0.35 | – | -0.49 |
| 175 | `M68` Kell Base n' Break | **45.9** | 24 | 49 | 47 | 77 | BELUM CUKUP | 13 | 42/12 | -2.11 | 18 | +0.60 | +0.13 | 1.7 | +0.18 | – | 1.31 |
| 176 | `M03` BB Break + Divergence RSI | **45.8** | 41 | 47 | 52 | 15 | BELUM CUKUP | 18 | 388/303 | -0.62 | 18 | -1.20 | -0.19 | 2.7 | -0.14 | – | -0.48 |
| 177 | `M12` Parabolic SAR | **45.8** | 42 | 46 | 52 | 15 | BELUM CUKUP | 18 | 356/181 | -1.19 | 18 | +0.07 | +0.01 | 3.0 | -0.12 | – | -0.30 |
| 178 | `M121` High 2 bull flag (Brooks) | **45.8** | 17 | 17 | 22 | 15 | BELUM CUKUP | 3 | 5/4 | -13.65 | 14 | -6.81 | -0.82 | 4.0 | -1.47 | – | -27.78 |
| 179 | `N16X13` RSI2<10 tanpa penapis → keluar | **45.6** | 29 | 29 | 25 | 30 | BELUM CUKUP | 5 | 110/3 | -0.89 | 5 | -6.46 | -0.72 | 6.9 | -1.22 | – | – |
| 180 | `N113X16` 80-20 bar (sisi beli) → keluar | **45.2** | 26 | 19 | 35 | 30 | BELUM CUKUP | 5 | 225/69 | -0.99 | 5 | -7.75 | -1.00 | 6.4 | -1.29 | – | – |
| 181 | `M140` 猎豹出击 (Serangan Cheetah) | **45.1** | 39 | 41 | 37 | 15 | BELUM CUKUP | 10 | 41/12 | -0.65 | 18 | -2.68 | -0.43 | 2.6 | -0.89 | – | -1.18 |
| 182 | `M87` IBD Tapak Menaik | **45.1** | 28 | 36 | 41 | 15 | BELUM CUKUP | 7 | 10/6 | -2.35 | 18 | -2.33 | -0.40 | 3.3 | +0.00 | – | 0.00 |
| 183 | `N29X36` PSAR naik + tutup>MA50 → kelua | **45.1** | 23 | 24 | 31 | 30 | BELUM CUKUP | 5 | 113/30 | -1.43 | 5 | -7.94 | -0.82 | 7.5 | -1.41 | – | – |
| 184 | `M06` Minervini VCP Breakout | **45.0** | 37 | 51 | 48 | 15 | BELUM CUKUP | 18 | 75/34 | -1.36 | 18 | -0.71 | -0.11 | 2.7 | -0.23 | – | -0.66 |
| 185 | `N113X36` 80-20 bar (sisi beli) → keluar | **45.0** | 22 | 22 | 34 | 30 | BELUM CUKUP | 5 | 215/70 | -1.30 | 5 | -6.74 | -0.98 | 6.0 | -1.42 | – | – |
| 186 | `N29X16` PSAR naik + tutup>MA50 → kelua | **44.7** | 14 | 30 | 30 | 39 | BELUM CUKUP | 5 | 149/44 | -2.03 | 5 | -5.06 | -0.69 | 5.5 | -1.68 | – | – |
| 187 | `M50` Elder Triple Screen | **44.5** | 46 | 33 | 53 | 15 | BELUM CUKUP | 18 | 551/314 | -0.35 | 18 | -7.97 | -0.72 | 6.4 | -0.09 | – | -0.15 |
| 188 | `M141` First Thrust (Landry) | **44.4** | 24 | 45 | 34 | 15 | BELUM CUKUP | 8 | 23/8 | -1.76 | 18 | -1.69 | -0.33 | 2.0 | -0.91 | – | -1.89 |
| 189 | `M125` 2-Bar Breakout | **44.3** | 41 | 38 | 50 | 15 | BELUM CUKUP | 18 | 908/411 | -1.04 | 18 | -1.75 | -0.28 | 2.7 | -0.36 | – | -0.18 |
| 190 | `M130` 多方炮 (dua lilin hijau mengapit  | **44.2** | 18 | 28 | 38 | 21 | BELUM CUKUP | 6 | 9/3 | -2.19 | 16 | -1.75 | -0.32 | 2.5 | +0.22 | – | 0.20 |
| 191 | `N16X15` RSI2<10 tanpa penapis → ekori  | **44.0** | 18 | 20 | 19 | 30 | BELUM CUKUP | 5 | 107/0 | -1.28 | 5 | -9.56 | -0.82 | 8.9 | -1.39 | – | – |
| 192 | `M26` Garis Trend Undur 3 Sentuhan + | **43.9** | 37 | 37 | 46 | 15 | BELUM CUKUP | 15 | 68/42 | -0.62 | 18 | -4.95 | -0.61 | 3.6 | -0.45 | – | -0.75 |
| 193 | `M156` Single Penetration (DiNapoli) | **43.8** | 36 | 34 | 48 | 28 | BELUM CUKUP | 18 | 228/134 | -1.06 | 18 | -3.39 | -0.26 | 5.7 | -0.70 | – | -2.75 |
| 194 | `M55` Guppy GMMA | **43.6** | 38 | 35 | 51 | 15 | BELUM CUKUP | 18 | 200/117 | -1.27 | 18 | -3.58 | -0.41 | 4.3 | -0.29 | – | -0.92 |
| 195 | `M99` Three Line Break | **43.5** | 32 | 43 | 51 | 15 | BELUM CUKUP | 18 | 146/84 | -1.94 | 18 | +0.61 | +0.10 | 3.3 | -0.19 | – | -0.84 |
| 196 | `M73` ADX(5) > 40 + Julat Terkecil 6 | **43.4** | 40 | 33 | 49 | 15 | BELUM CUKUP | 18 | 803/669 | -0.07 | 18 | -6.54 | -0.82 | 4.7 | -0.54 | – | -3.86 |
| 197 | `M120` Reversal New Highs | **43.3** | 31 | 37 | 42 | 15 | BELUM CUKUP | 13 | 19/12 | -1.69 | 18 | -2.47 | -0.38 | 3.2 | -0.36 | – | -2.21 |
| 198 | `M66` IBD Undur Pertama ke Purata 50 | **43.2** | 38 | 33 | 51 | 15 | BELUM CUKUP | 18 | 221/132 | -1.10 | 18 | -4.17 | -0.36 | 6.0 | -0.32 | – | -0.94 |
| 199 | `M119` 180 Bullish (Cooper) | **43.1** | 37 | 34 | 48 | 15 | BELUM CUKUP | 17 | 145/61 | -0.85 | 18 | -5.71 | -0.53 | 4.6 | -0.41 | – | -1.41 |
| 200 | `M147` Improved Three-Bar Pullback | **42.9** | 24 | 43 | 36 | 42 | BELUM CUKUP | 15 | 97/33 | -2.78 | 18 | +0.25 | +0.03 | 3.9 | -1.47 | – | -1.00 |
| 201 | `M44` Tapak Rata IBD | **42.9** | 20 | 41 | 23 | 15 | BELUM CUKUP | 8 | 9/5 | -3.78 | 18 | -3.31 | -0.70 | 2.5 | -2.02 | – | -32.39 |
| 202 | `M135` 3rd Watch | **42.6** | 13 | 30 | 32 | 15 | BELUM CUKUP | 7 | 12/3 | -4.94 | 18 | -5.69 | -0.72 | 3.3 | -0.82 | – | -4.85 |
| 203 | `M19` Sneaky Pivot (proksi harian) | **42.3** | 23 | 40 | 48 | 28 | BELUM CUKUP | 17 | 348/224 | -2.70 | 18 | -0.99 | -0.13 | 3.3 | -0.61 | – | -9.88 |
| 204 | `M95` Nisbah Kebaharuan High 52 Ming | **42.0** | 28 | 36 | 49 | 15 | BELUM CUKUP | 17 | 118/62 | -1.53 | 18 | -4.22 | -0.50 | 4.1 | -0.35 | – | -0.96 |
| 205 | `M161` EMA 10/21 + Supertrend (10,3) | **41.8** | 42 | 20 | 54 | 16 | BELUM CUKUP | 18 | 447/210 | -0.10 | 18 | -10.09 | -0.73 | 8.7 | +0.02 | – | 0.05 |
| 206 | `M57` Landry Trend Knockout (TKO) | **41.7** | 31 | 35 | 43 | 15 | BELUM CUKUP | 18 | 159/102 | -1.69 | 18 | -3.58 | -0.42 | 4.0 | -1.20 | – | -3.82 |
| 207 | `M11` NR7 Breakout + Volume | **40.9** | 29 | 29 | 42 | 15 | BELUM CUKUP | 16 | 106/70 | -1.16 | 18 | -7.21 | -0.60 | 6.1 | -1.14 | – | -1.14 |
| 208 | `M126` Hidden Smash Day (beli, Larry  | **40.9** | 14 | 33 | 35 | 15 | BELUM CUKUP | 10 | 18/11 | -3.86 | 17 | -4.59 | -0.64 | 3.7 | -0.80 | – | -1.55 |
| 209 | `M123` CCI Correction (Lambert, Chart | **40.7** | 28 | 35 | 38 | 15 | BELUM CUKUP | 18 | 172/145 | -1.39 | 18 | -7.02 | -0.65 | 6.0 | -1.80 | – | -4.18 |
| 210 | `M67` Rayner Teo: Ujian Ketiga pada  | **40.5** | 18 | 31 | 37 | 15 | BELUM CUKUP | 12 | 27/18 | -3.50 | 18 | -6.21 | -0.56 | 5.8 | -1.03 | – | -5.65 |
| 211 | `M28` VWAP Separator + Kiss Pivot | **40.4** | 26 | 29 | 42 | 15 | BELUM CUKUP | 16 | 105/87 | -1.60 | 18 | -7.65 | -0.90 | 5.5 | -1.22 | – | -11.96 |
| 212 | `M29` EMA3 + RSI75 + Stokastik | **40.4** | 20 | 30 | 37 | 15 | BELUM CUKUP | 13 | 32/26 | -2.99 | 18 | -9.29 | -0.74 | 6.6 | -1.22 | – | -7.83 |
| 213 | `M79` Radge: 20% Flipper | **40.0** | 23 | 32 | 46 | 15 | BELUM CUKUP | 18 | 350/81 | -1.71 | 18 | -4.37 | -0.48 | 4.5 | -0.84 | – | -1.53 |
| 214 | `M82` Arthur Hill Rotasi Sasaran 10% | **39.5** | 30 | 19 | 50 | 15 | BELUM CUKUP | 18 | 555/197 | -0.94 | 18 | -7.40 | -0.47 | 7.7 | -0.35 | – | -1.46 |
| 215 | `M59` Anjakan Julat RSI | **39.3** | 15 | 25 | 43 | 15 | BELUM CUKUP | 13 | 35/16 | -4.54 | 18 | -4.05 | -0.51 | 3.5 | -0.36 | – | -1.65 |
| 216 | `M122` Moving Momentum (ChartSchool) | **38.7** | 21 | 28 | 40 | 15 | BELUM CUKUP | 18 | 99/58 | -2.61 | 18 | -5.47 | -0.64 | 4.7 | -1.39 | – | -4.63 |
| 217 | `M101` Bulkowski: Tiga lembah menaik | **38.1** | 12 | 23 | 45 | 15 | BELUM CUKUP | 14 | 43/20 | -3.58 | 18 | -7.43 | -0.60 | 5.8 | -0.25 | – | -0.85 |
| 218 | `M76` Undercut & Rally pada Low Pent | **37.0** | 13 | 27 | 40 | 15 | BELUM CUKUP | 17 | 65/45 | -1.73 | 18 | -8.69 | -0.79 | 6.1 | -1.18 | – | -5.15 |
| 219 | `M154` HOLP (High of Low Period) | **37.0** | 11 | 19 | 40 | 15 | BELUM CUKUP | 14 | 74/31 | -3.46 | 18 | -10.85 | -0.84 | 6.6 | -1.02 | – | -5.13 |
| 220 | `M47` Holy Grail Raschke | **36.6** | 8 | 17 | 27 | 15 | BELUM CUKUP | 12 | 28/21 | -3.48 | 18 | -9.55 | -0.92 | 5.4 | -2.29 | – | -25.15 |
| 221 | `M09` Volumatic VIDYA Pivot Retest | **36.5** | 6 | 12 | 32 | 15 | BELUM CUKUP | 11 | 28/16 | -4.42 | 18 | -10.92 | -0.93 | 7.0 | -1.60 | – | -11.73 |
| 222 | `M81` Bensdorp Long Trend High Momen | **34.8** | 3 | 8 | 43 | 15 | BELUM CUKUP | 12 | 331/140 | -4.41 | 18 | -19.26 | -0.84 | 13.1 | -1.01 | – | -3.71 |
| 223 | `M90` Pring KST | **31.8** | 3 | 14 | 42 | 15 | BELUM CUKUP | 17 | 74/42 | -3.75 | 18 | -13.17 | -0.72 | 10.1 | -0.98 | – | -5.04 |

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

