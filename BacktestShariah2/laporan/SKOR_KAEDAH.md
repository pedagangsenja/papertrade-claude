# Skor Kaedah 0–100 (pangkat maklumat, BUKAN keputusan)

> **Status keputusan (kad skor, harga 2026-11-09):** TERBUKTI 0 · CALON 0 · BELUM CUKUP 223 · GAGAL 0 · NEGATIF 0. Rejim QQQ OFF sejak 2026-10-16. Hanya **TERBUKTI** layak untuk wang sebenar (`laporan/KAD_SKOR.md`); nombor dalam laporan ini BUKAN keputusan dan tidak boleh dibaca sebagai pangkat untuk wang sebenar.

Dijana 2026-11-11 oleh `standard/skor_kaedah.py` (Actions `analisis.yml`, selepas kad skor). Harga pada tutup 2026-11-09; 223 kaedah; 17 hari beli langsung (rejim ON 1, OFF 16). Pradaftar 2026-11-09: `standard/SPEC_SKOR_KAEDAH.md` (berat dan sauh dikunci `ujian/test_skor_kaedah.py::TestKunci`). Rekod analisis sahaja: tiada order, tiada wang sebenar.

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
| 1 | `M33` Supertrend + SMA10 | **66.0** | 95 | 88 | 70 | 85 | BELUM CUKUP | 17 | 204/37 | +2.99 | 18 | +8.81 | +3.30 | 1.4 | +2.31 | – | 7.19 |
| 2 | `M146` 3-Bar Momentum Pattern | **65.7** | 94 | 89 | 71 | 85 | BELUM CUKUP | 16 | 76/28 | +2.18 | 18 | +6.01 | +0.98 | 2.1 | +2.57 | – | 4.00 |
| 3 | `M118` Expansion Pivot (Cooper) | **64.3** | 90 | 88 | 62 | 85 | BELUM CUKUP | 17 | 73/20 | +1.69 | 18 | +10.44 | +3.86 | 0.9 | +1.65 | – | 4.39 |
| 4 | `M133` Bull Hook (Crabel) | **62.8** | 99 | 92 | 59 | 85 | BELUM CUKUP | 12 | 47/19 | +2.23 | 18 | +7.43 | +1.79 | 1.5 | +1.51 | – | 15.72 |
| 5 | `M25` VWAP Wave (proksi harian) | **61.6** | 83 | 81 | 61 | 80 | BELUM CUKUP | 16 | 169/82 | +0.84 | 18 | +5.95 | +1.03 | 3.0 | +1.04 | – | 6.38 |
| 6 | `M124` 'Last' Stochastic Technique (C | **61.6** | 80 | 78 | 63 | 85 | BELUM CUKUP | 17 | 344/163 | +0.90 | 18 | +6.74 | +1.47 | 2.3 | +1.11 | – | 2.00 |
| 7 | `M111` Sistem Volatiliti Wilder | **61.3** | 86 | 68 | 64 | 85 | BELUM CUKUP | 17 | 232/72 | +1.48 | 18 | +4.69 | +0.70 | 3.5 | +1.38 | – | 2.80 |
| 8 | `M151` Outside Bar Failure | **60.4** | 75 | 84 | 58 | 85 | BELUM CUKUP | 16 | 82/45 | +0.41 | 18 | +7.91 | +6.50 | 0.5 | +0.91 | – | 1.76 |
| 9 | `M91` Stochastic Pop (Bernstein/Stec | **60.3** | 93 | 77 | 58 | 85 | BELUM CUKUP | 12 | 34/12 | +1.67 | 18 | +8.65 | +1.10 | 2.6 | +1.54 | – | 5.22 |
| 10 | `M142` Pecahan volum dari dasar (底部放量 | **60.3** | 87 | 92 | 48 | 85 | BELUM CUKUP | 13 | 40/5 | +3.22 | 16 | +4.80 | +1.00 | 1.8 | +0.90 | – | 1.50 |
| 11 | `M105` Supertrend tulen | **60.2** | 86 | 63 | 66 | 75 | BELUM CUKUP | 17 | 320/88 | +1.79 | 18 | +1.58 | +0.22 | 3.2 | +1.50 | – | 3.13 |
| 12 | `M10` EMA3 + CCI + MACD | **59.6** | 78 | 70 | 58 | 85 | BELUM CUKUP | 17 | 102/47 | +0.71 | 18 | +8.94 | +1.70 | 1.9 | +0.79 | – | 2.20 |
| 13 | `M13` Garis Trend Action/Safety Line | **59.6** | 74 | 75 | 58 | 85 | BELUM CUKUP | 17 | 662/407 | +0.29 | 18 | +8.33 | +2.34 | 1.3 | +0.52 | – | 1.02 |
| 14 | `M145` Yum-Yum Continuation | **59.4** | 76 | 75 | 58 | 72 | BELUM CUKUP | 17 | 280/54 | +0.91 | 18 | +4.33 | +1.98 | 1.3 | +0.76 | – | 0.58 |
| 15 | `M93` Bollinger Kaedah II: %b + MFI | **59.1** | 82 | 60 | 62 | 82 | BELUM CUKUP | 17 | 247/69 | +1.55 | 18 | +1.13 | +0.18 | 2.5 | +1.19 | – | 1.50 |
| 16 | `M74` Lulus Baharu Trend Template Mi | **58.5** | 70 | 78 | 54 | 77 | BELUM CUKUP | 17 | 82/50 | -0.02 | 18 | +4.37 | +1.05 | 2.2 | +0.41 | – | 0.73 |
| 17 | `M137` Livermore System | **58.1** | 68 | 73 | 56 | 85 | BELUM CUKUP | 17 | 151/53 | +0.06 | 18 | +6.13 | +1.04 | 2.3 | +0.62 | – | 1.24 |
| 18 | `M23` Breitstein Kapitulasi + Kesina | **57.9** | 67 | 68 | 61 | 85 | BELUM CUKUP | 17 | 111/66 | +0.02 | 18 | +1.61 | +0.32 | 2.1 | +1.12 | – | 4.60 |
| 19 | `M100` Bulkowski Segi Empat & Segi Ti | **57.6** | 68 | 77 | 55 | 85 | BELUM CUKUP | 14 | 58/39 | +0.36 | 18 | +4.37 | +1.00 | 2.1 | +0.70 | – | 3.48 |
| 20 | `M160` Measured Move Up | **57.6** | 62 | 76 | 61 | 85 | BELUM CUKUP | 15 | 85/44 | -0.40 | 18 | +5.25 | +1.12 | 2.1 | +1.28 | – | 10.26 |
| 21 | `M89` Chande 65sma-3cc | **57.6** | 68 | 67 | 58 | 85 | BELUM CUKUP | 17 | 151/79 | +0.08 | 18 | +3.27 | +0.66 | 2.4 | +0.70 | – | 1.83 |
| 22 | `M30` BB Free Bar + Himpitan 50/2.5 | **57.0** | 78 | 58 | 63 | 56 | BELUM CUKUP | 17 | 217/67 | +1.11 | 18 | +2.58 | +0.34 | 4.8 | +1.27 | – | 2.21 |
| 23 | `M15` Break & Retest + Henti ATR | **56.8** | 86 | 53 | 64 | 45 | BELUM CUKUP | 17 | 265/145 | +1.88 | 18 | -3.42 | -0.46 | 3.3 | +1.27 | – | 2.36 |
| 24 | `M80` Radge Saluran Purata Bergerak  | **56.7** | 83 | 54 | 65 | 45 | BELUM CUKUP | 17 | 252/50 | +2.06 | 18 | -1.36 | -0.19 | 3.7 | +1.60 | – | 1.79 |
| 25 | `M158` Doubly Adaptive Profit Targets | **56.7** | 80 | 57 | 64 | 45 | BELUM CUKUP | 17 | 335/123 | +1.50 | 18 | -0.46 | -0.07 | 2.6 | +1.20 | – | 3.08 |
| 26 | `M05` MACD Divergence + Pengesahan | **56.4** | 73 | 76 | 48 | 73 | BELUM CUKUP | 13 | 38/12 | +0.59 | 18 | +4.46 | +1.31 | 1.3 | +0.31 | – | 0.61 |
| 27 | `M139` 均线首次粘合向上发散 (MA berhimpun kali  | **56.1** | 66 | 65 | 52 | 85 | BELUM CUKUP | 17 | 69/17 | +0.16 | 18 | +4.49 | +0.90 | 1.9 | +0.52 | – | 1.76 |
| 28 | `M92` CCI-50 | **55.7** | 68 | 57 | 58 | 75 | BELUM CUKUP | 17 | 471/296 | +0.57 | 18 | +0.18 | +0.03 | 2.5 | +0.52 | – | 0.92 |
| 29 | `M88` O'Neil Shakeout +3 | **55.4** | 69 | 61 | 52 | 82 | BELUM CUKUP | 14 | 54/27 | +0.28 | 18 | +4.14 | +0.49 | 3.3 | +0.48 | – | 0.89 |
| 30 | `M159` Heikin-Ashi Trend | **55.4** | 65 | 72 | 53 | 48 | BELUM CUKUP | 17 | 1414/1137 | -0.11 | 18 | +7.34 | +1.20 | 3.7 | +0.01 | – | 0.04 |
| 31 | `M70` Pecahan Hari Dalam | **55.2** | 66 | 69 | 56 | 41 | BELUM CUKUP | 17 | 372/291 | -0.05 | 18 | +2.26 | +0.46 | 2.3 | +0.32 | – | 0.87 |
| 32 | `M46` Jurang Naik Boleh Beli (Buyabl | **55.0** | 67 | 72 | 50 | 85 | BELUM CUKUP | 10 | 33/16 | -0.05 | 18 | +2.38 | +0.48 | 1.7 | +0.53 | – | 1.00 |
| 33 | `M129` Wick Play | **54.3** | 74 | 61 | 49 | 85 | BELUM CUKUP | 9 | 23/9 | +0.50 | 18 | +5.85 | +2.07 | 1.0 | +0.67 | – | 2.93 |
| 34 | `M02` MACD + SMA200 | **54.3** | 63 | 65 | 50 | 55 | BELUM CUKUP | 17 | 105/54 | -0.30 | 18 | +10.10 | +2.29 | 1.8 | -0.07 | – | -0.38 |
| 35 | `N68X36` Bullish engulfing + EMA21 → ke | **54.2** | 86 | 90 | 53 | 70 | BELUM CUKUP | 4 | 35/5 | +1.61 | 5 | +3.02 | +1.40 | 1.4 | +1.89 | – | – |
| 36 | `M48` Cooper 1-2-3-4 | **53.9** | 62 | 56 | 52 | 85 | BELUM CUKUP | 14 | 45/15 | -0.08 | 18 | +8.03 | +1.47 | 2.1 | +0.70 | – | 1.96 |
| 37 | `N68X16` Bullish engulfing + EMA21 → ke | **53.7** | 78 | 89 | 50 | 70 | BELUM CUKUP | 4 | 36/6 | +1.32 | 5 | +2.63 | +1.27 | 1.4 | +1.52 | – | – |
| 38 | `M131` Ross Hook (Joe Ross) | **53.7** | 62 | 56 | 60 | 47 | BELUM CUKUP | 17 | 247/102 | +0.19 | 18 | -0.27 | -0.04 | 3.0 | +0.77 | – | 1.72 |
| 39 | `M117` Landry Pullback (high 2 bulan) | **53.6** | 80 | 46 | 56 | 45 | BELUM CUKUP | 14 | 81/17 | +1.79 | 18 | -4.62 | -0.59 | 3.6 | +1.14 | – | 1.25 |
| 40 | `M21` Marius 3 Persediaan (Pecahan+J | **53.3** | 88 | 65 | 46 | 64 | BELUM CUKUP | 5 | 5/2 | +1.58 | 10 | +0.26 | +0.13 | 1.1 | +1.37 | – | 2.78 |
| 41 | `M18` EMA9/21 Pullback | **53.0** | 67 | 49 | 57 | 46 | BELUM CUKUP | 17 | 315/207 | +0.54 | 18 | -2.40 | -0.40 | 4.1 | +0.49 | – | 1.69 |
| 42 | `M132` Ascending Scallop (Bulkowski) | **52.8** | 48 | 66 | 52 | 85 | BELUM CUKUP | 15 | 88/34 | -1.07 | 18 | +3.58 | +0.96 | 2.2 | +0.27 | – | 2.25 |
| 43 | `M35` Pocket Pivot Morales & Kacher | **52.7** | 64 | 50 | 57 | 45 | BELUM CUKUP | 17 | 291/200 | +0.12 | 18 | -0.96 | -0.10 | 4.9 | +0.48 | – | 2.68 |
| 44 | `M77` Undercut & Rally pada Purata B | **52.5** | 54 | 72 | 44 | 55 | BELUM CUKUP | 15 | 49/33 | -0.74 | 18 | +2.59 | +0.82 | 1.6 | -0.61 | – | -0.85 |
| 45 | `N45X16` Undur EMA21 cerun positif → ke | **52.4** | 64 | 81 | 48 | 70 | BELUM CUKUP | 4 | 74/26 | +0.01 | 5 | +6.29 | +8.02 | 0.4 | +0.77 | – | – |
| 46 | `M04` BB Squeeze Breakout | **52.3** | 57 | 49 | 57 | 64 | BELUM CUKUP | 16 | 142/47 | -0.30 | 18 | +2.55 | +0.32 | 4.0 | +0.72 | – | 1.24 |
| 47 | `N64X36` Episodic pivot → keluar selepa | **52.2** | 86 | 74 | 33 | 70 | BELUM CUKUP | 4 | 39/2 | +1.65 | 5 | +0.85 | +0.21 | 2.4 | -0.08 | – | – |
| 48 | `M150` Trend Bar Failure (Brooks) | **52.1** | 67 | 48 | 52 | 43 | BELUM CUKUP | 16 | 81/39 | +0.78 | 18 | -3.36 | -0.60 | 2.5 | +0.29 | – | 0.93 |
| 49 | `M37` Weinstein Peringkat 2 | **52.0** | 75 | 94 | 34 | 70 | BELUM CUKUP | 3 | 7/0 | +1.32 | 12 | +0.71 | +1.41 | 0.2 | +0.49 | – | 0.50 |
| 50 | `N64X14` Episodic pivot → keluar bila r | **52.0** | 89 | 71 | 30 | 70 | BELUM CUKUP | 4 | 39/0 | +2.10 | 5 | -0.12 | -0.03 | 2.3 | +0.00 | – | – |
| 51 | `N124X15` Episodic pivot gap 8-10% → eko | **52.0** | 88 | 71 | 31 | 70 | BELUM CUKUP | 4 | 36/0 | +2.83 | 5 | -0.76 | -0.11 | 3.6 | +0.04 | – | – |
| 52 | `N64X16` Episodic pivot → keluar bila s | **51.9** | 82 | 68 | 34 | 70 | BELUM CUKUP | 4 | 39/3 | +1.50 | 5 | -0.12 | -0.03 | 2.3 | -0.13 | – | – |
| 53 | `N64X17` Episodic pivot → keluar bila a | **51.9** | 77 | 70 | 36 | 70 | BELUM CUKUP | 4 | 39/7 | +1.05 | 5 | +0.78 | +0.20 | 2.3 | -0.21 | – | – |
| 54 | `M116` 2/20 EMA Breakout (Landry) | **51.6** | 61 | 45 | 59 | 45 | BELUM CUKUP | 17 | 512/325 | +0.32 | 18 | -0.31 | -0.03 | 6.9 | +0.66 | – | 2.71 |
| 55 | `N53X36` Supertrend + ADX>25 → keluar s | **51.5** | 73 | 65 | 47 | 38 | BELUM CUKUP | 4 | 79/13 | +1.06 | 5 | +0.52 | +0.13 | 2.7 | +0.88 | – | – |
| 56 | `M106` DMI Wilder | **51.5** | 64 | 43 | 58 | 45 | BELUM CUKUP | 15 | 100/53 | +0.61 | 18 | -2.65 | -0.59 | 2.6 | +0.87 | – | 1.58 |
| 57 | `M153` Range Leader | **51.5** | 58 | 47 | 58 | 45 | BELUM CUKUP | 17 | 1053/905 | +0.08 | 18 | -0.69 | -0.07 | 5.9 | +0.56 | – | 3.25 |
| 58 | `N22X36` BB pecah atas + RSI → keluar s | **51.3** | 55 | 65 | 50 | 70 | BELUM CUKUP | 4 | 68/16 | -0.33 | 5 | +1.85 | +0.49 | 2.3 | +1.16 | – | – |
| 59 | `N45X36` Undur EMA21 cerun positif → ke | **51.2** | 58 | 69 | 43 | 62 | BELUM CUKUP | 4 | 67/18 | +0.16 | 5 | +1.18 | +0.57 | 1.3 | +0.26 | – | – |
| 60 | `M134` First Kiss After Daylight (Lan | **51.2** | 59 | 48 | 55 | 46 | BELUM CUKUP | 14 | 39/16 | +0.30 | 18 | -1.18 | -0.17 | 3.2 | +0.96 | – | 1.14 |
| 61 | `N124X36` Episodic pivot gap 8-10% → kel | **51.0** | 82 | 58 | 36 | 40 | BELUM CUKUP | 4 | 36/5 | +1.70 | 5 | -2.45 | -0.50 | 3.3 | -0.00 | – | – |
| 62 | `M51` O'Neil Cawan & Pemegang | **50.9** | 77 | 61 | 42 | 62 | BELUM CUKUP | 2 | 3/0 | +1.02 | 8 | +0.08 | +0.08 | 0.5 | +1.64 | – | 6.56 |
| 63 | `N56X17` RSI>50 + ADX>20 → keluar bila  | **50.9** | 67 | 61 | 34 | 70 | BELUM CUKUP | 4 | 76/6 | +0.75 | 5 | -0.54 | -0.11 | 3.0 | -0.33 | – | – |
| 64 | `N25X17` Supertrend + EMA + ADX>23 → ke | **50.8** | 66 | 65 | 32 | 67 | BELUM CUKUP | 4 | 69/0 | +0.63 | 5 | +0.23 | +0.05 | 3.0 | +0.18 | – | – |
| 65 | `N28X14` ADX>25 + DI+ > DI- → keluar bi | **50.6** | 69 | 58 | 33 | 60 | BELUM CUKUP | 4 | 95/2 | +1.10 | 5 | -1.39 | -0.23 | 3.8 | -0.12 | – | – |
| 66 | `N42X14` Lonjakan volum 2x → keluar bil | **50.6** | 72 | 55 | 31 | 70 | BELUM CUKUP | 4 | 129/3 | +1.23 | 5 | -2.00 | -0.18 | 6.3 | -0.47 | – | – |
| 67 | `N24X17` Supertrend(10,3) + ADX>20 → ke | **50.6** | 61 | 62 | 33 | 70 | BELUM CUKUP | 4 | 72/3 | +0.30 | 5 | -0.21 | -0.06 | 2.1 | -0.26 | – | – |
| 68 | `M104` High Tight Flag / Power Play | **50.5** | 78 | 90 | 27 | 65 | BELUM CUKUP | 1 | 1/0 | +14.81 | 3 | +1.48 | +10.00 | 0.0 | – | – | 41.96 |
| 69 | `N36X16` Pocket pivot → keluar bila sup | **50.5** | 49 | 70 | 38 | 70 | BELUM CUKUP | 4 | 114/37 | -0.76 | 5 | +2.86 | +2.14 | 0.7 | -0.51 | – | – |
| 70 | `N25X36` Supertrend + EMA + ADX>23 → ke | **50.5** | 55 | 62 | 39 | 61 | BELUM CUKUP | 4 | 75/11 | -0.00 | 5 | +0.04 | +0.01 | 2.9 | +0.02 | – | – |
| 71 | `N75X17` RSI14 < 40 tanpa penapis → kel | **50.5** | 56 | 62 | 36 | 70 | BELUM CUKUP | 4 | 225/91 | +0.14 | 5 | -0.15 | -0.04 | 2.4 | -1.17 | – | – |
| 72 | `N25X16` Supertrend + EMA + ADX>23 → ke | **50.5** | 60 | 62 | 35 | 60 | BELUM CUKUP | 4 | 72/2 | +0.32 | 5 | -0.24 | -0.05 | 3.0 | +0.07 | – | – |
| 73 | `M143` 장대양봉 이후 눌림목 / 5일선 매매 (Undur ke | **50.5** | 60 | 68 | 30 | 52 | BELUM CUKUP | 9 | 13/1 | +0.67 | 17 | +0.60 | +0.20 | 1.5 | -0.68 | – | -8.24 |
| 74 | `M155` Market Cycle Strategy | **50.4** | 66 | 40 | 56 | 32 | BELUM CUKUP | 17 | 599/214 | +0.74 | 18 | -2.34 | -0.39 | 3.5 | +0.33 | – | 0.58 |
| 75 | `N37X14` Gap and go → keluar bila rsi14 | **50.3** | 66 | 55 | 31 | 70 | BELUM CUKUP | 4 | 63/2 | +0.60 | 5 | -0.14 | -0.04 | 2.1 | -0.37 | – | – |
| 76 | `N07X16` Tiga MA tersusun → keluar bila | **50.3** | 61 | 63 | 40 | 30 | BELUM CUKUP | 4 | 76/8 | +0.53 | 5 | -0.04 | -0.01 | 2.2 | +0.27 | – | – |
| 77 | `M39` Radge Pecahan Bollinger 100 ha | **50.3** | 39 | 65 | 51 | 58 | BELUM CUKUP | 17 | 215/48 | -1.60 | 18 | +6.30 | +2.63 | 1.2 | +0.05 | – | 0.11 |
| 78 | `M08` SMA20 + SMA200 | **50.2** | 55 | 42 | 52 | 55 | BELUM CUKUP | 15 | 156/86 | -0.05 | 18 | -2.16 | -0.40 | 3.8 | +0.02 | – | 0.06 |
| 79 | `N80X36` Tinggi sepanjang masa → keluar | **50.1** | 66 | 55 | 34 | 43 | BELUM CUKUP | 3 | 23/0 | +0.82 | 5 | -0.69 | -0.20 | 1.9 | +0.55 | – | – |
| 80 | `N42X15` Lonjakan volum 2x → ekori Chan | **50.1** | 71 | 54 | 26 | 70 | BELUM CUKUP | 4 | 123/0 | +1.15 | 5 | -1.88 | -0.16 | 6.5 | -0.52 | – | – |
| 81 | `N53X17` Supertrend + ADX>25 → keluar b | **50.1** | 68 | 56 | 37 | 30 | BELUM CUKUP | 4 | 66/0 | +1.02 | 5 | -1.84 | -0.45 | 3.1 | +0.83 | – | – |
| 82 | `M148` Natural Number Method | **50.1** | 43 | 62 | 46 | 55 | BELUM CUKUP | 17 | 181/119 | -1.39 | 18 | +3.06 | +0.62 | 2.1 | -0.79 | – | -2.89 |
| 83 | `N28X17` ADX>25 + DI+ > DI- → keluar bi | **50.0** | 65 | 57 | 27 | 67 | BELUM CUKUP | 4 | 57/0 | +0.83 | 5 | -1.23 | -0.17 | 4.3 | -0.39 | – | – |
| 84 | `N37X36` Gap and go → keluar selepas DU | **50.0** | 55 | 58 | 33 | 70 | BELUM CUKUP | 4 | 63/9 | -0.37 | 5 | +1.35 | +0.37 | 2.3 | -0.60 | – | – |
| 85 | `M31` Band Walk (BB 20/2) | **50.0** | 63 | 35 | 58 | 45 | BELUM CUKUP | 17 | 373/65 | +0.68 | 18 | -2.66 | -0.24 | 6.8 | +0.76 | – | 1.30 |
| 86 | `N42X17` Lonjakan volum 2x → keluar bil | **50.0** | 56 | 50 | 38 | 70 | BELUM CUKUP | 4 | 137/30 | +0.30 | 5 | -2.37 | -0.24 | 5.9 | -0.54 | – | – |
| 87 | `N53X16` Supertrend + ADX>25 → keluar b | **50.0** | 63 | 54 | 40 | 30 | BELUM CUKUP | 4 | 71/2 | +0.76 | 5 | -2.08 | -0.48 | 3.1 | +0.74 | – | – |
| 88 | `N75X14` RSI14 < 40 tanpa penapis → kel | **50.0** | 64 | 54 | 28 | 70 | BELUM CUKUP | 4 | 176/4 | +0.84 | 5 | -2.27 | -0.41 | 3.8 | -0.92 | – | – |
| 89 | `N19X13` Bawah jalur BB + RSI<30 → kelu | **49.9** | 80 | 54 | 29 | 30 | BELUM CUKUP | 4 | 98/0 | +2.01 | 5 | -3.02 | -0.92 | 2.7 | -0.19 | – | – |
| 90 | `N42X36` Lonjakan volum 2x → keluar sel | **49.9** | 58 | 47 | 38 | 70 | BELUM CUKUP | 4 | 138/38 | +0.43 | 5 | -2.73 | -0.37 | 4.7 | -0.60 | – | – |
| 91 | `N56X16` RSI>50 + ADX>20 → keluar bila  | **49.9** | 54 | 47 | 40 | 70 | BELUM CUKUP | 4 | 102/29 | +0.16 | 5 | -2.47 | -0.48 | 3.7 | -0.29 | – | – |
| 92 | `N07X36` Tiga MA tersusun → keluar sele | **49.8** | 59 | 56 | 39 | 30 | BELUM CUKUP | 4 | 78/7 | +0.51 | 5 | -0.86 | -0.22 | 2.4 | +0.19 | – | – |
| 93 | `N37X16` Gap and go → keluar bila super | **49.8** | 54 | 53 | 34 | 70 | BELUM CUKUP | 4 | 63/11 | -0.21 | 5 | +0.39 | +0.10 | 2.2 | -0.61 | – | – |
| 94 | `N41X16` CMF20>0 + tutup>EMA20 → keluar | **49.8** | 41 | 61 | 41 | 70 | BELUM CUKUP | 4 | 129/66 | -1.01 | 5 | +0.95 | +0.44 | 1.3 | -0.47 | – | – |
| 95 | `N35X36` Pecah 52 minggu tinggi → kelua | **49.8** | 48 | 70 | 28 | 70 | BELUM CUKUP | 3 | 30/0 | -0.39 | 5 | +1.19 | +0.66 | 1.1 | -0.21 | – | – |
| 96 | `N33X36` Donchian20 + penapis MA200 → k | **49.7** | 53 | 55 | 34 | 60 | BELUM CUKUP | 4 | 51/7 | -0.27 | 5 | -0.86 | -0.24 | 2.2 | -0.45 | – | – |
| 97 | `N37X17` Gap and go → keluar bila adx14 | **49.7** | 50 | 56 | 34 | 70 | BELUM CUKUP | 4 | 62/16 | -0.62 | 5 | +1.34 | +0.36 | 2.1 | -0.72 | – | – |
| 98 | `N24X16` Supertrend(10,3) + ADX>20 → ke | **49.7** | 58 | 55 | 31 | 56 | BELUM CUKUP | 4 | 65/2 | +0.22 | 5 | -0.89 | -0.26 | 2.1 | -0.41 | – | – |
| 99 | `N42X16` Lonjakan volum 2x → keluar bil | **49.7** | 56 | 44 | 38 | 64 | BELUM CUKUP | 4 | 141/37 | +0.37 | 5 | -3.18 | -0.49 | 4.4 | -0.57 | – | – |
| 100 | `N22X16` BB pecah atas + RSI → keluar b | **49.7** | 48 | 54 | 47 | 37 | BELUM CUKUP | 4 | 66/15 | -0.51 | 5 | -0.43 | -0.12 | 2.3 | +0.83 | – | – |
| 101 | `N65X14` Gap 4% + volum + hampir 52w →  | **49.7** | 68 | 55 | 23 | 55 | BELUM CUKUP | 3 | 24/0 | +0.59 | 5 | -1.39 | -0.33 | 2.7 | -0.71 | – | – |
| 102 | `N65X36` Gap 4% + volum + hampir 52w →  | **49.7** | 68 | 55 | 23 | 55 | BELUM CUKUP | 3 | 24/0 | +0.59 | 5 | -1.39 | -0.33 | 2.7 | -0.71 | – | – |
| 103 | `N22X14` BB pecah atas + RSI → keluar b | **49.6** | 48 | 52 | 37 | 63 | BELUM CUKUP | 4 | 73/4 | -0.44 | 5 | -0.32 | -0.07 | 2.8 | +0.19 | – | – |
| 104 | `N40X36` OBV tinggi baharu + MA50 → kel | **49.6** | 46 | 54 | 37 | 66 | BELUM CUKUP | 4 | 25/7 | -0.77 | 5 | +0.17 | +0.04 | 2.9 | -0.09 | – | – |
| 105 | `M107` Golden Cross SMA50/200 | **49.5** | 54 | 56 | 46 | 26 | BELUM CUKUP | 14 | 28/7 | -0.10 | 18 | +0.50 | +0.14 | 1.7 | +0.22 | – | 0.38 |
| 106 | `N28X36` ADX>25 + DI+ > DI- → keluar se | **49.5** | 51 | 42 | 40 | 70 | BELUM CUKUP | 4 | 137/60 | +0.19 | 5 | -3.02 | -0.48 | 4.3 | -0.47 | – | – |
| 107 | `N33X16` Donchian20 + penapis MA200 → k | **49.5** | 47 | 56 | 31 | 70 | BELUM CUKUP | 4 | 51/5 | -0.61 | 5 | -0.33 | -0.09 | 2.0 | -0.59 | – | – |
| 108 | `N50X14` Mampat + pecah volum 1.5x → ke | **49.5** | 56 | 50 | 27 | 70 | BELUM CUKUP | 3 | 12/0 | +0.31 | 5 | -2.56 | -0.28 | 5.1 | -0.30 | – | – |
| 109 | `N66X36` 52w tinggi + pengesahan 1% → k | **49.4** | 54 | 50 | 29 | 50 | BELUM CUKUP | 3 | 28/1 | +0.10 | 4 | -1.33 | -0.32 | 3.0 | -0.31 | – | – |
| 110 | `M144` Screw Bar | **49.3** | 62 | 48 | 38 | 26 | BELUM CUKUP | 5 | 8/6 | +0.11 | 16 | -0.31 | -0.12 | 0.9 | +0.09 | – | 0.36 |
| 111 | `N40X16` OBV tinggi baharu + MA50 → kel | **49.3** | 43 | 50 | 38 | 70 | BELUM CUKUP | 4 | 33/14 | -1.05 | 5 | -0.27 | -0.05 | 3.1 | -0.14 | – | – |
| 112 | `N33X14` Donchian20 + penapis MA200 → k | **49.3** | 48 | 55 | 30 | 63 | BELUM CUKUP | 4 | 60/1 | -0.57 | 5 | -0.29 | -0.07 | 2.5 | -0.33 | – | – |
| 113 | `N75X13` RSI14 < 40 tanpa penapis → kel | **49.2** | 54 | 58 | 22 | 70 | BELUM CUKUP | 4 | 115/0 | +0.15 | 5 | -0.85 | -0.23 | 2.3 | -0.94 | – | – |
| 114 | `N75X15` RSI14 < 40 tanpa penapis → eko | **49.2** | 54 | 58 | 22 | 70 | BELUM CUKUP | 4 | 115/0 | +0.15 | 5 | -0.85 | -0.23 | 2.3 | -0.94 | – | – |
| 115 | `N36X36` Pocket pivot → keluar selepas  | **49.2** | 45 | 48 | 36 | 70 | BELUM CUKUP | 4 | 113/38 | -0.92 | 5 | +0.62 | +0.12 | 2.8 | -0.87 | – | – |
| 116 | `N28X16` ADX>25 + DI+ > DI- → keluar bi | **49.2** | 46 | 43 | 38 | 70 | BELUM CUKUP | 4 | 144/60 | -0.13 | 5 | -2.97 | -0.47 | 4.2 | -0.74 | – | – |
| 117 | `M27` Price Action 4 Tiang | **49.2** | 50 | 43 | 46 | 15 | BELUM CUKUP | 2 | 547/432 | -0.61 | 18 | -2.31 | -0.45 | 2.9 | -0.03 | – | -0.09 |
| 118 | `M07` Qullamaggie Breakout | **49.2** | 28 | 64 | 27 | 15 | BELUM CUKUP | 1 | 1/1 | -2.53 | 18 | -0.25 | -0.21 | 0.7 | -0.22 | – | -1.12 |
| 119 | `N74X16` MACD atas garis isyarat (keada | **49.1** | 46 | 39 | 42 | 70 | BELUM CUKUP | 4 | 200/118 | -0.13 | 5 | -4.23 | -0.58 | 5.5 | -0.52 | – | – |
| 120 | `N50X17` Mampat + pecah volum 1.5x → ke | **49.1** | 48 | 46 | 29 | 70 | BELUM CUKUP | 3 | 12/1 | -0.29 | 5 | -2.75 | -0.30 | 5.2 | -0.33 | – | – |
| 121 | `N39X36` NR7 kemudian pecah → keluar se | **49.0** | 22 | 45 | 22 | 50 | BELUM CUKUP | 1 | 16/4 | -3.11 | 4 | +0.23 | +0.06 | 2.3 | -1.17 | – | – |
| 122 | `N08X16` tutup>EMA20 tidak terlalu jauh | **48.8** | 40 | 43 | 39 | 70 | BELUM CUKUP | 4 | 192/100 | -0.88 | 5 | -1.16 | -0.37 | 2.4 | -0.82 | – | – |
| 123 | `N41X36` CMF20>0 + tutup>EMA20 → keluar | **48.8** | 36 | 48 | 39 | 70 | BELUM CUKUP | 4 | 108/64 | -1.34 | 5 | +0.46 | +0.09 | 2.8 | -0.69 | – | – |
| 124 | `N08X36` tutup>EMA20 tidak terlalu jauh | **48.8** | 38 | 46 | 38 | 70 | BELUM CUKUP | 4 | 165/94 | -1.11 | 5 | -0.41 | -0.07 | 3.2 | -0.96 | – | – |
| 125 | `N47X16` NR7 + EMA9>EMA21 → keluar bila | **48.8** | 41 | 55 | 29 | 61 | BELUM CUKUP | 4 | 41/9 | -0.42 | 5 | -0.86 | -0.20 | 2.7 | -1.12 | – | – |
| 126 | `M41` FW Penyatuan Mingguan | **48.8** | 49 | 34 | 44 | 45 | BELUM CUKUP | 4 | 63/8 | +0.35 | 17 | -5.16 | -0.62 | 4.3 | +0.78 | – | 1.39 |
| 127 | `N54X16` Supertrend + RSI>50 → keluar b | **48.8** | 52 | 41 | 27 | 70 | BELUM CUKUP | 4 | 70/3 | +0.16 | 5 | -3.28 | -0.41 | 5.0 | -0.92 | – | – |
| 128 | `N73X13` Tutup bawah jalur bawah BB(20, | **48.8** | 56 | 55 | 24 | 30 | BELUM CUKUP | 4 | 131/0 | +0.30 | 5 | -1.31 | -0.21 | 3.3 | -0.70 | – | – |
| 129 | `M45` High 52 Minggu (George & Hwang | **48.8** | 18 | 43 | 29 | 15 | BELUM CUKUP | 1 | 2/1 | -4.72 | 7 | -0.78 | -0.43 | 1.0 | -0.02 | – | -0.13 |
| 130 | `M36` Turtle 55/20 | **48.7** | 50 | 41 | 56 | 40 | BELUM CUKUP | 17 | 304/145 | -0.48 | 18 | -1.35 | -0.11 | 6.4 | +0.33 | – | 0.82 |
| 131 | `N24X36` Supertrend(10,3) + ADX>20 → ke | **48.7** | 49 | 38 | 38 | 46 | BELUM CUKUP | 4 | 83/22 | -0.34 | 5 | -2.36 | -0.52 | 3.1 | -0.42 | – | – |
| 132 | `M136` Short/Intermediate-term Low (L | **48.6** | 56 | 44 | 56 | 20 | BELUM CUKUP | 17 | 629/243 | +0.03 | 18 | -1.50 | -0.32 | 2.5 | +0.29 | – | 0.17 |
| 133 | `M01` Bollinger Band + RSI | **48.6** | 74 | 43 | 44 | 15 | BELUM CUKUP | 17 | 108/17 | +1.66 | 18 | -4.29 | -0.40 | 4.3 | -0.42 | – | -2.01 |
| 134 | `N76X36` Tutup > MA50 (penapis trend tu | **48.6** | 46 | 38 | 36 | 57 | BELUM CUKUP | 4 | 82/28 | -0.35 | 5 | -3.52 | -0.64 | 4.0 | -0.70 | – | – |
| 135 | `N57X36` ADX bangkit daripada <20 → kel | **48.5** | 41 | 54 | 32 | 31 | BELUM CUKUP | 4 | 46/3 | -0.95 | 5 | +0.55 | +0.16 | 2.2 | -0.38 | – | – |
| 136 | `M138` 直升机空中加油 (Helikopter isi minyak | **48.5** | 37 | 53 | 24 | 15 | BELUM CUKUP | 2 | 2/0 | -0.86 | 11 | -0.22 | -0.34 | 0.3 | -0.50 | – | -0.70 |
| 137 | `M84` Jarak purata bergerak MAD 21/2 | **48.5** | 16 | 16 | 33 | 15 | BELUM CUKUP | 1 | 58/35 | -3.70 | 7 | -7.40 | -0.94 | 5.9 | -0.71 | – | -3.04 |
| 138 | `M32` Momentum Burst | **48.4** | 61 | 29 | 51 | 45 | BELUM CUKUP | 11 | 51/32 | +0.19 | 18 | -3.78 | -0.34 | 6.6 | +0.38 | – | 1.15 |
| 139 | `N57X16` ADX bangkit daripada <20 → kel | **48.4** | 41 | 54 | 32 | 31 | BELUM CUKUP | 4 | 44/4 | -0.96 | 5 | +0.55 | +0.16 | 2.2 | -0.40 | – | – |
| 140 | `N76X16` Tutup > MA50 (penapis trend tu | **48.3** | 34 | 47 | 33 | 70 | BELUM CUKUP | 4 | 129/57 | -1.32 | 5 | -0.51 | -0.15 | 2.1 | -1.35 | – | – |
| 141 | `N27X16` Ichimoku atas awan → keluar bi | **48.3** | 36 | 48 | 29 | 70 | BELUM CUKUP | 4 | 88/21 | -1.01 | 5 | -1.13 | -0.39 | 1.8 | -1.41 | – | – |
| 142 | `N36X14` Pocket pivot → keluar bila rsi | **48.3** | 45 | 38 | 31 | 51 | BELUM CUKUP | 4 | 113/6 | -0.54 | 5 | -2.78 | -0.41 | 4.2 | -0.66 | – | – |
| 143 | `M94` Pecutan Momentum (Chen, Yu & W | **48.3** | 14 | 13 | 16 | 15 | BELUM CUKUP | 1 | 33/0 | -6.98 | 7 | -6.86 | -0.58 | 7.6 | -1.21 | – | -5.48 |
| 144 | `M96` Momo India: Ranking Sharpe 3/6 | **48.2** | 15 | 10 | 9 | 15 | BELUM CUKUP | 1 | 6/5 | -12.74 | 7 | -7.86 | -1.00 | 5.6 | -5.12 | – | -14.74 |
| 145 | `M03` BB Break + Divergence RSI | **48.0** | 45 | 48 | 54 | 27 | BELUM CUKUP | 17 | 333/294 | -0.39 | 18 | -1.02 | -0.16 | 2.7 | +0.10 | – | 0.39 |
| 146 | `N38X36` VCP pecah → keluar selepas DUA | **48.0** | 40 | 47 | 28 | 36 | BELUM CUKUP | 4 | 15/4 | -0.84 | 5 | -1.39 | -0.43 | 2.1 | -0.96 | – | – |
| 147 | `M149` 3-Step Pullback | **47.9** | 51 | 36 | 56 | 33 | BELUM CUKUP | 15 | 151/52 | -0.16 | 18 | -3.56 | -0.33 | 5.3 | +0.67 | – | 0.61 |
| 148 | `N09X36` Undur EMA10 + penapis EMA50 →  | **47.9** | 28 | 48 | 34 | 70 | BELUM CUKUP | 4 | 88/25 | -1.63 | 5 | -0.14 | -0.04 | 2.3 | -0.94 | – | – |
| 149 | `M78` Alvarez Pecahan Mingguan DTAYS | **47.8** | 19 | 24 | 42 | 24 | BELUM CUKUP | 2 | 73/39 | -1.83 | 17 | -7.71 | -0.75 | 6.2 | +0.07 | – | 0.29 |
| 150 | `N06X36` Golden cross MA50/MA200 → kelu | **47.7** | 24 | 50 | 22 | 64 | BELUM CUKUP | 3 | 8/2 | -1.78 | 5 | -1.06 | -0.26 | 2.5 | -1.25 | – | – |
| 151 | `M127` Slingshot Bullish | **47.5** | 48 | 54 | 48 | 15 | BELUM CUKUP | 15 | 94/69 | -1.14 | 18 | +0.05 | +0.01 | 2.9 | -0.46 | – | -0.69 |
| 152 | `N31X36` Turtle sistem 2 → keluar selep | **47.5** | 36 | 42 | 24 | 44 | BELUM CUKUP | 4 | 71/0 | -1.11 | 5 | -1.53 | -0.42 | 2.5 | -0.75 | – | – |
| 153 | `N43X36` Undur EMA8 + penapis MA50 → ke | **47.5** | 25 | 47 | 30 | 70 | BELUM CUKUP | 4 | 76/16 | -1.86 | 5 | +0.15 | +0.04 | 2.4 | -1.24 | – | – |
| 154 | `M68` Kell Base n' Break | **47.3** | 30 | 50 | 47 | 78 | BELUM CUKUP | 12 | 41/11 | -1.88 | 18 | +0.69 | +0.15 | 1.7 | +0.26 | – | 1.97 |
| 155 | `N27X36` Ichimoku atas awan → keluar se | **47.3** | 36 | 37 | 28 | 30 | BELUM CUKUP | 4 | 59/5 | -0.90 | 5 | -2.76 | -0.63 | 3.1 | -0.95 | – | – |
| 156 | `M115` Bow Tie (Landry) | **47.2** | 35 | 41 | 48 | 45 | BELUM CUKUP | 9 | 33/18 | -1.48 | 18 | -3.83 | -0.49 | 3.5 | +0.38 | – | 2.39 |
| 157 | `N56X36` RSI>50 + ADX>20 → keluar selep | **47.2** | 33 | 30 | 33 | 48 | BELUM CUKUP | 4 | 93/31 | -0.84 | 5 | -4.91 | -0.67 | 5.6 | -1.07 | – | – |
| 158 | `M130` 多方炮 (dua lilin hijau mengapit  | **47.1** | 43 | 29 | 42 | 37 | BELUM CUKUP | 6 | 9/3 | -0.23 | 16 | -1.67 | -0.31 | 2.5 | +0.70 | – | 0.72 |
| 159 | `N55X13` BB + RSI + ADX>20 → keluar bil | **47.0** | 40 | 40 | 18 | 30 | BELUM CUKUP | 4 | 45/0 | -0.40 | 5 | -3.76 | -0.82 | 3.7 | -1.42 | – | – |
| 160 | `N47X36` NR7 + EMA9>EMA21 → keluar sele | **47.0** | 22 | 36 | 24 | 30 | BELUM CUKUP | 3 | 37/8 | -1.34 | 5 | -3.62 | -0.52 | 4.9 | -1.47 | – | – |
| 161 | `N51X36` BB squeeze + Supertrend → kelu | **46.9** | 21 | 37 | 23 | 30 | BELUM CUKUP | 3 | 4/2 | -3.38 | 5 | -1.44 | -0.56 | 1.9 | -1.22 | – | – |
| 162 | `M140` 猎豹出击 (Serangan Cheetah) | **46.8** | 50 | 44 | 38 | 15 | BELUM CUKUP | 9 | 38/12 | -0.10 | 18 | -2.68 | -0.43 | 2.6 | -0.72 | – | -1.04 |
| 163 | `N119X13` 3 tutup turun berturut → kelua | **46.8** | 36 | 34 | 22 | 30 | BELUM CUKUP | 4 | 129/6 | -0.10 | 5 | -6.89 | -0.84 | 7.1 | -1.74 | – | – |
| 164 | `M49` Ichimoku (Tutup Atas Awan + Te | **46.7** | 49 | 45 | 51 | 15 | BELUM CUKUP | 17 | 253/138 | -0.81 | 18 | -0.94 | -0.14 | 3.3 | -0.22 | – | -0.32 |
| 165 | `N51X16` BB squeeze + Supertrend → kelu | **46.7** | 16 | 38 | 25 | 30 | BELUM CUKUP | 3 | 4/1 | -2.63 | 5 | -1.40 | -0.55 | 1.8 | -0.78 | – | – |
| 166 | `N54X36` Supertrend + RSI>50 → keluar s | **46.6** | 31 | 25 | 32 | 33 | BELUM CUKUP | 4 | 90/28 | -0.94 | 5 | -6.03 | -0.74 | 6.1 | -1.11 | – | – |
| 167 | `M64` O'Neil Tiga Minggu Ketat | **46.5** | 24 | 24 | 27 | 15 | BELUM CUKUP | 3 | 3/1 | -10.36 | 18 | -3.18 | -0.81 | 2.1 | -0.79 | – | -11.27 |
| 168 | `M14` Walking with the Whales | **46.4** | 55 | 37 | 53 | 15 | BELUM CUKUP | 17 | 820/547 | -0.00 | 18 | -6.62 | -0.62 | 5.8 | -0.05 | – | -0.10 |
| 169 | `M54` IBD Power Trend | **46.4** | 46 | 45 | 52 | 15 | BELUM CUKUP | 16 | 195/100 | -0.98 | 18 | +1.12 | +0.11 | 5.5 | -0.11 | – | -0.28 |
| 170 | `N119X15` 3 tutup turun berturut → ekori | **46.4** | 34 | 38 | 14 | 36 | BELUM CUKUP | 4 | 37/0 | -0.42 | 5 | -4.48 | -0.66 | 5.2 | -1.85 | – | – |
| 171 | `M12` Parabolic SAR | **46.3** | 44 | 46 | 53 | 15 | BELUM CUKUP | 17 | 335/177 | -1.10 | 18 | +0.12 | +0.02 | 3.0 | -0.05 | – | -0.13 |
| 172 | `N29X36` PSAR naik + tutup>MA50 → kelua | **46.2** | 28 | 23 | 32 | 30 | BELUM CUKUP | 4 | 83/26 | -1.08 | 5 | -8.00 | -0.83 | 7.6 | -1.11 | – | – |
| 173 | `M102` Stockbee SLTB | **46.1** | 47 | 41 | 52 | 15 | BELUM CUKUP | 17 | 319/237 | -0.93 | 18 | -2.30 | -0.21 | 5.4 | -0.13 | – | -0.39 |
| 174 | `N16X13` RSI2<10 tanpa penapis → keluar | **46.1** | 28 | 28 | 23 | 30 | BELUM CUKUP | 4 | 109/3 | -0.94 | 5 | -6.46 | -0.72 | 6.9 | -1.45 | – | – |
| 175 | `M157` Consolidation Pivot Breakout ( | **46.1** | 22 | 37 | 28 | 15 | BELUM CUKUP | 4 | 4/3 | -4.95 | 15 | -1.93 | -0.66 | 1.3 | -0.83 | – | -2.99 |
| 176 | `M34` Carter TTM Squeeze | **46.0** | 45 | 37 | 50 | 24 | BELUM CUKUP | 16 | 94/46 | -0.79 | 18 | -0.64 | -0.09 | 3.7 | -0.02 | – | -0.07 |
| 177 | `M152` Spike & Ledge | **46.0** | 31 | 51 | 43 | 45 | BELUM CUKUP | 14 | 40/7 | -1.49 | 18 | +1.50 | +0.36 | 2.3 | -0.14 | – | -0.49 |
| 178 | `M38` Darvas Kotak | **46.0** | 16 | 30 | 34 | 45 | BELUM CUKUP | 4 | 23/1 | -2.25 | 17 | -2.89 | -0.29 | 4.2 | +0.20 | – | 1.24 |
| 179 | `M125` 2-Bar Breakout | **45.9** | 49 | 38 | 52 | 15 | BELUM CUKUP | 17 | 895/403 | -0.50 | 18 | -1.62 | -0.26 | 2.7 | -0.08 | – | -0.05 |
| 180 | `N29X16` PSAR naik + tutup>MA50 → kelua | **45.8** | 16 | 30 | 29 | 44 | BELUM CUKUP | 4 | 105/41 | -2.18 | 5 | -4.77 | -0.65 | 5.5 | -1.62 | – | – |
| 181 | `N48X36` Inside day pecah → keluar sele | **45.8** | 18 | 25 | 31 | 37 | BELUM CUKUP | 4 | 80/37 | -2.56 | 5 | -5.65 | -0.67 | 6.5 | -1.41 | – | – |
| 182 | `M20` EMA10/15 Crossover + Sudut | **45.7** | 42 | 45 | 47 | 18 | BELUM CUKUP | 17 | 381/323 | -1.04 | 18 | -1.66 | -0.28 | 2.7 | -0.71 | – | -5.29 |
| 183 | `M06` Minervini VCP Breakout | **45.5** | 39 | 51 | 48 | 15 | BELUM CUKUP | 17 | 71/34 | -1.29 | 18 | -0.67 | -0.11 | 2.7 | -0.18 | – | -0.54 |
| 184 | `M128` Inventory Retracement Bar (IRB | **45.5** | 46 | 30 | 53 | 29 | BELUM CUKUP | 17 | 128/73 | -0.50 | 18 | -5.03 | -0.45 | 6.2 | +0.08 | – | 0.46 |
| 185 | `M87` IBD Tapak Menaik | **45.5** | 26 | 36 | 42 | 30 | BELUM CUKUP | 7 | 10/6 | -1.93 | 18 | -2.33 | -0.40 | 3.3 | +0.12 | – | 0.49 |
| 186 | `N113X36` 80-20 bar (sisi beli) → keluar | **45.5** | 17 | 20 | 32 | 45 | BELUM CUKUP | 4 | 111/51 | -1.72 | 5 | -5.92 | -0.86 | 5.8 | -1.41 | – | – |
| 187 | `M121` High 2 bull flag (Brooks) | **45.5** | 11 | 17 | 25 | 15 | BELUM CUKUP | 3 | 5/3 | -9.95 | 14 | -6.39 | -0.81 | 4.0 | -1.04 | – | -15.94 |
| 188 | `M50` Elder Triple Screen | **45.3** | 49 | 32 | 54 | 17 | BELUM CUKUP | 17 | 496/300 | -0.19 | 18 | -8.13 | -0.74 | 6.4 | +0.03 | – | 0.06 |
| 189 | `M147` Improved Three-Bar Pullback | **45.0** | 31 | 43 | 42 | 42 | BELUM CUKUP | 14 | 95/29 | -1.52 | 18 | +0.25 | +0.03 | 3.9 | -0.80 | – | -0.55 |
| 190 | `N113X16` 80-20 bar (sisi beli) → keluar | **44.8** | 14 | 15 | 31 | 30 | BELUM CUKUP | 4 | 112/50 | -1.84 | 5 | -6.94 | -0.99 | 6.2 | -1.48 | – | – |
| 191 | `N16X15` RSI2<10 tanpa penapis → ekori  | **44.8** | 18 | 19 | 16 | 30 | BELUM CUKUP | 4 | 106/0 | -1.30 | 5 | -9.56 | -0.82 | 8.9 | -1.66 | – | – |
| 192 | `M141` First Thrust (Landry) | **44.6** | 22 | 44 | 34 | 15 | BELUM CUKUP | 7 | 20/8 | -1.99 | 18 | -1.45 | -0.28 | 2.0 | -0.91 | – | -1.99 |
| 193 | `M55` Guppy GMMA | **43.9** | 39 | 35 | 51 | 15 | BELUM CUKUP | 17 | 183/114 | -1.32 | 18 | -3.58 | -0.41 | 4.3 | -0.26 | – | -0.90 |
| 194 | `M99` Three Line Break | **43.8** | 33 | 42 | 52 | 15 | BELUM CUKUP | 17 | 133/84 | -1.98 | 18 | +0.61 | +0.10 | 3.3 | -0.14 | – | -0.65 |
| 195 | `M26` Garis Trend Undur 3 Sentuhan + | **43.8** | 36 | 36 | 45 | 15 | BELUM CUKUP | 14 | 56/39 | -0.77 | 18 | -4.87 | -0.61 | 3.5 | -0.47 | – | -0.82 |
| 196 | `M73` ADX(5) > 40 + Julat Terkecil 6 | **43.7** | 42 | 32 | 50 | 15 | BELUM CUKUP | 17 | 729/556 | +0.08 | 18 | -6.98 | -0.87 | 4.7 | -0.44 | – | -3.34 |
| 197 | `M156` Single Penetration (DiNapoli) | **43.7** | 34 | 34 | 47 | 27 | BELUM CUKUP | 17 | 226/121 | -1.10 | 18 | -4.01 | -0.31 | 5.8 | -0.70 | – | -2.94 |
| 198 | `M66` IBD Undur Pertama ke Purata 50 | **43.1** | 37 | 32 | 50 | 15 | BELUM CUKUP | 17 | 197/129 | -1.23 | 18 | -4.17 | -0.36 | 6.0 | -0.32 | – | -1.00 |
| 199 | `M120` Reversal New Highs | **42.9** | 29 | 36 | 39 | 15 | BELUM CUKUP | 12 | 18/12 | -2.38 | 18 | -2.77 | -0.42 | 3.2 | -0.73 | – | -4.40 |
| 200 | `M44` Tapak Rata IBD | **42.9** | 20 | 41 | 24 | 15 | BELUM CUKUP | 8 | 9/5 | -3.57 | 18 | -3.31 | -0.70 | 2.5 | -1.90 | – | -32.31 |
| 201 | `M161` EMA 10/21 + Supertrend (10,3) | **42.7** | 44 | 20 | 54 | 22 | BELUM CUKUP | 17 | 421/200 | +0.04 | 18 | -10.09 | -0.72 | 8.7 | +0.09 | – | 0.22 |
| 202 | `M135` 3rd Watch | **42.6** | 13 | 30 | 32 | 15 | BELUM CUKUP | 7 | 12/3 | -5.04 | 18 | -5.69 | -0.72 | 3.3 | -0.83 | – | -5.27 |
| 203 | `M119` 180 Bullish (Cooper) | **42.4** | 35 | 29 | 48 | 15 | BELUM CUKUP | 16 | 114/58 | -0.94 | 18 | -7.03 | -0.65 | 4.7 | -0.38 | – | -1.37 |
| 204 | `M19` Sneaky Pivot (proksi harian) | **42.4** | 24 | 37 | 48 | 26 | BELUM CUKUP | 16 | 266/219 | -3.44 | 18 | -1.57 | -0.21 | 3.3 | -0.60 | – | -10.15 |
| 205 | `M95` Nisbah Kebaharuan High 52 Ming | **42.4** | 29 | 36 | 48 | 15 | BELUM CUKUP | 16 | 112/61 | -1.61 | 18 | -4.22 | -0.50 | 4.1 | -0.35 | – | -1.02 |
| 206 | `M79` Radge: 20% Flipper | **42.0** | 31 | 32 | 47 | 15 | BELUM CUKUP | 17 | 277/74 | -1.23 | 18 | -4.03 | -0.44 | 4.4 | -0.56 | – | -1.11 |
| 207 | `M67` Rayner Teo: Ujian Ketiga pada  | **42.0** | 24 | 31 | 37 | 15 | BELUM CUKUP | 11 | 25/18 | -3.80 | 18 | -6.25 | -0.56 | 5.8 | -1.04 | – | -6.04 |
| 208 | `M126` Hidden Smash Day (beli, Larry  | **41.7** | 18 | 33 | 35 | 15 | BELUM CUKUP | 10 | 18/11 | -3.79 | 17 | -4.59 | -0.64 | 3.7 | -0.77 | – | -1.58 |
| 209 | `M11` NR7 Breakout + Volume | **41.3** | 29 | 28 | 43 | 15 | BELUM CUKUP | 15 | 95/69 | -1.14 | 18 | -7.35 | -0.61 | 6.1 | -1.02 | – | -1.06 |
| 210 | `M123` CCI Correction (Lambert, Chart | **41.1** | 28 | 36 | 39 | 15 | BELUM CUKUP | 17 | 160/142 | -1.41 | 18 | -6.86 | -0.64 | 5.9 | -1.69 | – | -4.17 |
| 211 | `M57` Landry Trend Knockout (TKO) | **41.1** | 27 | 34 | 42 | 15 | BELUM CUKUP | 17 | 144/101 | -2.01 | 18 | -3.65 | -0.43 | 4.0 | -1.29 | – | -4.29 |
| 212 | `M28` VWAP Separator + Kiss Pivot | **40.4** | 24 | 28 | 42 | 15 | BELUM CUKUP | 15 | 91/82 | -1.74 | 18 | -7.88 | -0.93 | 5.5 | -1.17 | – | -12.16 |
| 213 | `M82` Arthur Hill Rotasi Sasaran 10% | **40.1** | 32 | 19 | 51 | 15 | BELUM CUKUP | 17 | 544/184 | -0.79 | 18 | -7.25 | -0.46 | 7.7 | -0.28 | – | -1.24 |
| 214 | `M29` EMA3 + RSI75 + Stokastik | **40.1** | 18 | 30 | 38 | 15 | BELUM CUKUP | 13 | 32/26 | -2.72 | 18 | -9.29 | -0.74 | 6.6 | -1.07 | – | -7.38 |
| 215 | `M59` Anjakan Julat RSI | **39.7** | 17 | 26 | 43 | 15 | BELUM CUKUP | 13 | 35/16 | -4.61 | 18 | -3.73 | -0.46 | 3.5 | -0.38 | – | -1.85 |
| 216 | `M122` Moving Momentum (ChartSchool) | **39.3** | 22 | 29 | 41 | 15 | BELUM CUKUP | 17 | 94/56 | -2.36 | 18 | -5.47 | -0.64 | 4.7 | -1.17 | – | -4.29 |
| 217 | `M101` Bulkowski: Tiga lembah menaik | **38.6** | 14 | 24 | 45 | 15 | BELUM CUKUP | 14 | 43/19 | -3.40 | 18 | -7.38 | -0.60 | 5.8 | -0.20 | – | -0.72 |
| 218 | `M154` HOLP (High of Low Period) | **37.7** | 12 | 19 | 40 | 15 | BELUM CUKUP | 13 | 68/30 | -3.54 | 18 | -10.85 | -0.84 | 6.6 | -0.97 | – | -5.17 |
| 219 | `M09` Volumatic VIDYA Pivot Retest | **37.6** | 7 | 12 | 32 | 15 | BELUM CUKUP | 10 | 26/15 | -4.49 | 18 | -10.86 | -0.92 | 7.0 | -1.54 | – | -11.90 |
| 220 | `M76` Undercut & Rally pada Low Pent | **37.0** | 11 | 27 | 40 | 15 | BELUM CUKUP | 16 | 53/43 | -2.12 | 18 | -8.26 | -0.76 | 6.0 | -1.21 | – | -5.47 |
| 221 | `M47` Holy Grail Raschke | **37.0** | 7 | 16 | 27 | 15 | BELUM CUKUP | 11 | 22/20 | -4.67 | 18 | -10.14 | -0.98 | 5.5 | -2.29 | – | -27.58 |
| 222 | `M81` Bensdorp Long Trend High Momen | **34.6** | 3 | 8 | 44 | 15 | BELUM CUKUP | 12 | 331/135 | -4.11 | 18 | -19.26 | -0.84 | 13.1 | -0.92 | – | -3.58 |
| 223 | `M90` Pring KST | **33.3** | 5 | 12 | 42 | 15 | BELUM CUKUP | 16 | 67/41 | -4.02 | 18 | -13.39 | -0.73 | 10.2 | -0.95 | – | -5.16 |

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

