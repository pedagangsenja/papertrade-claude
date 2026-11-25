# Skor Kaedah 0–100 (pangkat maklumat, BUKAN keputusan)

> **Status keputusan (kad skor, harga 2026-11-24):** TERBUKTI 0 · CALON 0 · BELUM CUKUP 226 · GAGAL 1 · NEGATIF 0. Rejim QQQ OFF sejak 2026-10-16. Hanya **TERBUKTI** layak untuk wang sebenar (`laporan/KAD_SKOR.md`); nombor dalam laporan ini BUKAN keputusan dan tidak boleh dibaca sebagai pangkat untuk wang sebenar.

Dijana 2026-11-25 oleh `standard/skor_kaedah.py` (Actions `analisis.yml`, selepas kad skor). Harga pada tutup 2026-11-24; 227 kaedah; 28 hari beli langsung (rejim ON 1, OFF 27). Pradaftar 2026-11-09: `standard/SPEC_SKOR_KAEDAH.md` (berat dan sauh dikunci `ujian/test_skor_kaedah.py::TestKunci`). Rekod analisis sahaja: tiada order, tiada wang sebenar.

## Cara membaca

- **Skor** = min geometri berberat empat tiang (Untung 35 · Tahan 30 · Bukti 25 · Konsisten 10), dikecut ke 50 mengikut data: berat data = hari beli ÷ (hari beli + 20). Kaedah dengan 2 hari beli tidak boleh menjauhi 50. 100 = unggul semua segi; 50 = neutral/tiada bukti; < 50 = lebih buruk daripada neutral.
- **Siling** ikut kad skor: NEGATIF ≤ 20, GANTUNG/BERSARA ≤ 30, GAGAL ≤ 40. Tanda ⌈ = siling terpakai.
- **Satu-satunya status yang membenarkan wang sebenar ialah TERBUKTI dalam `laporan/KAD_SKOR.md`.** Skor tinggi dengan status BELUM CUKUP bermaksud "paling menjanjikan setakat ini", bukan "selamat".
- Deflasi ujian berganda (López de Prado): sauh t Bukti C1 = maks(2.0, E[maks 227 normal]) = 2.81.
- **Semakan kebolehramalan:** skor pada 2026-11-17 lawan pulangan lorong T4 sejak itu, 226 kaedah: Spearman ρ = +0.137 (p = 0.039). Positif dan p < 0.05: skor meramal pangkat.
- Metrik T4 (A2, B1, B2, D1) dikira atas lorong T4 L1 **dipotong pada sesi LANGSUNG pertama** kaedah itu (Mxx 2026-10-16, Nxx/GB 2026-11-03) dan diasas semula; sesi isian bina semula tidak dikira (pindaan 9 Nov 2026 (a)). Lajur "T4 sesi/pul" di bawah ialah potongan itu, bukan lorong penuh `T4_KAEDAH.md`.

## Semua kaedah, susun ikut Skor

| # | Kaedah | Skor | Untung | Tahan | Bukti | Konsisten | Status kad | Hari beli | Posisi/tutup | Jangkaan % | T4 sesi | T4 pul % | T4 pul/|MDD| | Ulcer | t buku | Lift | WFE |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `M146` 3-Bar Momentum Pattern | **61.0** | 76 | 72 | 60 | 95 | BELUM CUKUP | 20 | 80/47 | +0.57 | 28 | +6.14 | +0.87 | 3.2 | +0.96 | +2.60 | 1.91 |
| 2 | `M151` Outside Bar Failure | **56.1** | 56 | 77 | 54 | 55 | BELUM CUKUP | 25 | 122/82 | -0.95 | 28 | +7.26 | +1.81 | 1.2 | -0.06 | -0.04 | -0.11 |
| 3 | `M48` Cooper 1-2-3-4 | **56.0** | 61 | 62 | 54 | 81 | BELUM CUKUP | 23 | 81/27 | -0.25 | 28 | +9.42 | +1.64 | 2.5 | +0.51 | -1.09 | 1.12 |
| 4 | `N202X36` RSI2<10 dalam trend naik x X36 | **55.2** | 76 | 87 | 44 | 70 | BELUM CUKUP | 8 | 114/19 | +1.01 | 8 | +1.77 | +0.84 | 1.1 | +0.08 | – | – |
| 5 | `M133` Bull Hook (Crabel) | **54.8** | 55 | 64 | 58 | 81 | BELUM CUKUP | 16 | 54/45 | -0.78 | 28 | +3.37 | +0.56 | 2.7 | +0.96 | +3.89 | 7.52 |
| 6 | `M25` VWAP Wave (proksi harian) | **53.8** | 56 | 60 | 58 | 49 | BELUM CUKUP | 25 | 201/174 | -0.98 | 28 | +3.93 | +0.49 | 4.0 | +0.38 | +1.17 | 1.98 |
| 7 | `M160` Measured Move Up | **53.6** | 43 | 63 | 61 | 87 | BELUM CUKUP | 26 | 157/112 | -1.49 | 28 | +3.12 | +0.54 | 2.6 | +0.68 | +0.64 | 4.41 |
| 8 | `M23` Breitstein Kapitulasi + Kesina | **53.4** | 60 | 53 | 60 | 46 | BELUM CUKUP | 24 | 131/106 | -0.74 | 28 | -0.65 | -0.10 | 3.3 | +0.66 | +0.21 | 2.42 |
| 9 | `M118` Expansion Pivot (Cooper) | **53.2** | 50 | 59 | 54 | 90 | BELUM CUKUP | 20 | 85/46 | -1.17 | 28 | +5.48 | +0.66 | 3.2 | +0.31 | +1.49 | 0.98 |
| 10 | `M159` Heikin-Ashi Trend | **52.6** | 52 | 68 | 45 | 54 | BELUM CUKUP | 28 | 2005/1880 | -0.95 | 28 | +6.75 | +1.10 | 3.4 | -1.20 | -0.30 | -7.07 |
| 11 | `M104` High Tight Flag / Power Play | **51.2** | 88 | 90 | 44 | 85 | BELUM CUKUP | 1 | 1/0 | +28.08 | 13 | +2.83 | +10.00 | 0.1 | +2.07 | – | 11.42 |
| 12 | `M137` Livermore System | **50.6** | 39 | 64 | 54 | 58 | BELUM CUKUP | 26 | 186/98 | -1.87 | 28 | +6.54 | +1.11 | 2.4 | -0.03 | +0.73 | -0.05 |
| 13 | `M46` Jurang Naik Boleh Beli (Buyabl | **50.5** | 46 | 62 | 47 | 56 | BELUM CUKUP | 13 | 36/27 | -1.65 | 28 | +1.97 | +0.40 | 1.8 | -0.11 | +0.25 | -0.16 |
| 14 | `M45` High 52 Minggu (George & Hwang | **50.3** | 75 | 54 | 37 | 78 | BELUM CUKUP | 1 | 2/1 | +0.81 | 17 | +0.18 | +0.10 | 0.9 | +0.93 | – | 2.98 |
| 15 | `M51` O'Neil Cawan & Pemegang | **50.0** | 60 | 57 | 36 | 45 | BELUM CUKUP | 2 | 3/1 | -0.55 | 18 | -0.13 | -0.08 | 0.8 | +0.63 | – | 2.08 |
| 16 | `M70` Pecahan Hari Dalam | **49.9** | 61 | 65 | 53 | 10 | BELUM CUKUP | 28 | 526/455 | -0.73 | 28 | +2.54 | +0.44 | 2.5 | -0.29 | -1.39 | -0.67 |
| 17 | `M33` Supertrend + SMA10 | **49.8** | 35 | 59 | 55 | 73 | BELUM CUKUP | 23 | 224/126 | -2.32 | 28 | +6.81 | +0.94 | 2.7 | +0.10 | +0.61 | 0.53 |
| 18 | `M74` Lulus Baharu Trend Template Mi | **49.8** | 56 | 56 | 54 | 19 | BELUM CUKUP | 28 | 112/82 | -1.11 | 28 | +1.57 | +0.21 | 3.4 | -0.09 | +0.14 | -0.15 |
| 19 | `M10` EMA3 + CCI + MACD | **49.5** | 39 | 58 | 51 | 57 | BELUM CUKUP | 22 | 127/77 | -2.64 | 28 | +9.63 | +1.46 | 2.7 | -0.27 | +0.55 | -0.77 |
| 20 | `M07` Qullamaggie Breakout | **49.4** | 36 | 64 | 27 | 15 | BELUM CUKUP | 1 | 1/1 | -2.53 | 28 | -0.25 | -0.21 | 0.9 | -0.22 | – | -1.12 |
| 21 | `M145` Yum-Yum Continuation | **49.1** | 34 | 63 | 53 | 58 | BELUM CUKUP | 25 | 313/109 | -2.02 | 28 | +5.31 | +1.37 | 1.6 | -0.19 | +0.91 | -0.16 |
| 22 | `M158` Doubly Adaptive Profit Targets | **48.8** | 54 | 35 | 58 | 48 | BELUM CUKUP | 25 | 393/218 | -0.63 | 28 | -3.75 | -0.35 | 4.8 | +0.42 | +1.44 | 0.94 |
| 23 | `M13` Garis Trend Action/Safety Line | **48.6** | 38 | 61 | 46 | 54 | BELUM CUKUP | 28 | 899/756 | -2.83 | 28 | +5.84 | +0.88 | 2.3 | -1.06 | -0.31 | -2.74 |
| 24 | `M27` Price Action 4 Tiang | **48.6** | 42 | 32 | 42 | 15 | BELUM CUKUP | 2 | 546/521 | -1.34 | 28 | -4.16 | -0.81 | 3.2 | -0.49 | – | -1.68 |
| 25 | `M84` Jarak purata bergerak MAD 21/2 | **48.6** | 25 | 13 | 35 | 15 | BELUM CUKUP | 1 | 58/43 | -4.06 | 17 | -7.73 | -0.88 | 7.0 | -0.55 | – | -1.28 |
| 26 | `M96` Momo India: Ranking Sharpe 3/6 | **48.2** | 22 | 7 | 9 | 15 | BELUM CUKUP | 1 | 6/6 | -13.71 | 17 | -8.21 | -1.00 | 7.3 | -5.92 | – | -15.55 |
| 27 | `N25X36` Supertrend + EMA + ADX>23 → ke | **48.1** | 38 | 52 | 42 | 70 | BELUM CUKUP | 14 | 143/62 | -2.31 | 15 | +0.73 | +0.16 | 2.0 | -0.79 | – | – |
| 28 | `M93` Bollinger Kaedah II: %b + MFI | **47.9** | 54 | 38 | 56 | 29 | BELUM CUKUP | 25 | 273/122 | -0.74 | 28 | -0.98 | -0.10 | 4.2 | +0.18 | +1.87 | 0.25 |
| 29 | `M08` SMA20 + SMA200 | **47.9** | 43 | 45 | 51 | 52 | BELUM CUKUP | 26 | 292/217 | -1.47 | 28 | -1.53 | -0.29 | 3.7 | -0.43 | +0.36 | -1.03 |
| 30 | `M35` Pocket Pivot Morales & Kacher | **47.8** | 60 | 41 | 54 | 18 | BELUM CUKUP | 27 | 350/315 | -0.58 | 28 | -2.61 | -0.28 | 5.8 | -0.09 | +0.76 | -0.44 |
| 31 | `M41` FW Penyatuan Mingguan | **47.8** | 52 | 30 | 44 | 34 | BELUM CUKUP | 6 | 68/14 | -0.39 | 27 | -3.47 | -0.29 | 6.2 | +0.38 | – | 0.62 |
| 32 | `M94` Pecutan Momentum (Chen, Yu & W | **47.8** | 1 | 3 | 12 | 15 | BELUM CUKUP | 1 | 33/0 | -15.43 | 17 | -18.84 | -0.87 | 11.4 | -1.69 | – | -4.59 |
| 33 | `N53X36` Supertrend + ADX>25 → keluar s | **47.6** | 51 | 40 | 49 | 30 | BELUM CUKUP | 15 | 145/64 | -1.02 | 15 | -2.24 | -0.24 | 4.3 | +0.01 | – | – |
| 34 | `M78` Alvarez Pecahan Mingguan DTAYS | **47.6** | 23 | 19 | 40 | 15 | BELUM CUKUP | 2 | 73/47 | -2.87 | 27 | -8.85 | -0.79 | 8.3 | -0.23 | – | -0.67 |
| 35 | `M77` Undercut & Rally pada Purata B | **47.5** | 52 | 46 | 46 | 22 | BELUM CUKUP | 20 | 61/45 | -0.98 | 28 | -2.79 | -0.34 | 2.9 | -0.54 | +0.91 | -0.65 |
| 36 | `M129` Wick Play | **47.5** | 37 | 47 | 44 | 51 | BELUM CUKUP | 10 | 25/13 | -2.60 | 28 | +2.25 | +0.39 | 2.2 | -0.12 | – | -0.40 |
| 37 | `M37` Weinstein Peringkat 2 | **47.5** | 27 | 51 | 26 | 15 | BELUM CUKUP | 3 | 7/1 | -2.10 | 22 | -1.34 | -0.27 | 1.7 | -0.63 | – | -0.87 |
| 38 | `M05` MACD Divergence + Pengesahan | **47.4** | 41 | 49 | 41 | 50 | BELUM CUKUP | 16 | 42/16 | -2.90 | 28 | +0.88 | +0.12 | 2.6 | -0.73 | -1.25 | -1.26 |
| 39 | `N28X16` ADX>25 + DI+ > DI- → keluar bi | **47.3** | 39 | 48 | 37 | 70 | BELUM CUKUP | 15 | 585/461 | -1.27 | 15 | +0.07 | +0.01 | 3.7 | -1.57 | – | – |
| 40 | `M39` Radge Pecahan Bollinger 100 ha | **47.2** | 33 | 55 | 50 | 53 | BELUM CUKUP | 24 | 247/68 | -3.21 | 28 | +4.92 | +0.75 | 2.2 | -0.39 | -0.43 | -0.76 |
| 41 | `M100` Bulkowski Segi Empat & Segi Ti | **47.2** | 53 | 46 | 50 | 15 | BELUM CUKUP | 17 | 61/45 | -0.80 | 28 | -0.30 | -0.04 | 3.4 | -0.09 | – | -0.44 |
| 42 | `N204X36` Undur RSI2, gap 2%, RSI silang | **46.9** | 13 | 44 | 29 | 50 | BELUM CUKUP | 3 | 8/0 | -1.97 | 3 | -1.42 | -0.69 | 1.2 | -0.07 | – | – |
| 43 | `M142` Pecahan volum dari dasar (底部放量 | **46.7** | 43 | 39 | 45 | 55 | BELUM CUKUP | 18 | 56/14 | -1.05 | 26 | +2.13 | +0.26 | 3.3 | -0.01 | – | -0.02 |
| 44 | `M64` O'Neil Tiga Minggu Ketat | **46.7** | 30 | 21 | 26 | 15 | BELUM CUKUP | 3 | 3/3 | -12.60 | 28 | -3.76 | -0.84 | 3.1 | -1.26 | – | -14.58 |
| 45 | `M138` 直升机空中加油 (Helikopter isi minyak | **46.4** | 33 | 45 | 16 | 15 | BELUM CUKUP | 4 | 4/0 | -3.84 | 21 | -1.45 | -0.65 | 0.9 | -1.64 | – | -2.28 |
| 46 | `M131` Ross Hook (Joe Ross) | **46.3** | 45 | 46 | 54 | 17 | BELUM CUKUP | 25 | 275/157 | -1.47 | 28 | -0.30 | -0.03 | 4.5 | -0.03 | +0.54 | -0.07 |
| 47 | `M21` Marius 3 Persediaan (Pecahan+J | **46.3** | 27 | 44 | 35 | 15 | BELUM CUKUP | 5 | 5/4 | -3.41 | 20 | -1.69 | -0.63 | 1.8 | -0.13 | – | -0.19 |
| 48 | `M157` Consolidation Pivot Breakout ( | **46.1** | 36 | 41 | 31 | 15 | BELUM CUKUP | 6 | 8/3 | -1.71 | 25 | -1.27 | -0.37 | 1.9 | -0.61 | – | -1.30 |
| 49 | `N28X36` ADX>25 + DI+ > DI- → keluar se | **46.0** | 44 | 39 | 43 | 30 | BELUM CUKUP | 15 | 553/420 | -0.83 | 15 | -3.67 | -0.28 | 5.8 | -0.92 | – | – |
| 50 | `M18` EMA9/21 Pullback | **45.8** | 51 | 37 | 53 | 21 | BELUM CUKUP | 28 | 494/435 | -0.77 | 28 | -6.63 | -0.68 | 5.0 | -0.23 | +1.70 | -0.74 |
| 51 | `M102` Stockbee SLTB | **45.6** | 51 | 42 | 52 | 15 | BELUM CUKUP | 28 | 461/363 | -1.30 | 28 | -1.58 | -0.13 | 6.6 | -0.41 | -0.10 | -0.96 |
| 52 | `M153` Range Leader | **45.4** | 53 | 37 | 51 | 18 | BELUM CUKUP | 28 | 1486/1421 | -0.58 | 28 | -2.79 | -0.21 | 8.3 | -0.49 | +0.68 | -3.21 |
| 53 | `M117` Landry Pullback (high 2 bulan) | **45.4** | 46 | 31 | 54 | 35 | BELUM CUKUP | 22 | 167/43 | -0.79 | 28 | -6.46 | -0.55 | 6.0 | +0.37 | +2.28 | 0.39 |
| 54 | `M30` BB Free Bar + Himpitan 50/2.5 | **45.4** | 44 | 33 | 56 | 28 | BELUM CUKUP | 21 | 230/124 | -1.46 | 28 | +0.43 | +0.04 | 6.0 | +0.20 | +0.25 | 0.40 |
| 55 | `M124` 'Last' Stochastic Technique (C | **45.2** | 37 | 42 | 51 | 36 | BELUM CUKUP | 27 | 419/335 | -2.62 | 28 | -0.36 | -0.04 | 4.0 | -0.48 | -0.37 | -1.22 |
| 56 | `M87` IBD Tapak Menaik | **45.2** | 34 | 35 | 41 | 15 | BELUM CUKUP | 8 | 11/8 | -3.06 | 28 | -3.35 | -0.43 | 4.7 | -0.09 | – | -0.26 |
| 57 | `M38` Darvas Kotak | **45.2** | 25 | 21 | 34 | 26 | BELUM CUKUP | 5 | 27/1 | -3.36 | 27 | -3.55 | -0.31 | 6.6 | +0.10 | – | 0.37 |
| 58 | `N06X36` Golden cross MA50/MA200 → kelu | **44.9** | 43 | 38 | 32 | 30 | BELUM CUKUP | 13 | 31/5 | -0.59 | 15 | -3.79 | -0.50 | 4.1 | -0.98 | – | – |
| 59 | `M115` Bow Tie (Landry) | **44.9** | 37 | 37 | 48 | 16 | BELUM CUKUP | 12 | 37/30 | -2.37 | 28 | -3.98 | -0.42 | 5.5 | +0.02 | -0.25 | 0.07 |
| 60 | `N45X16` Undur EMA21 cerun positif → ke | **44.8** | 31 | 47 | 43 | 30 | BELUM CUKUP | 15 | 207/126 | -2.42 | 15 | +1.96 | +0.23 | 3.8 | -0.86 | – | – |
| 61 | `N203X36` Gap 2% lalu MA20 silang MA50 x | **44.7** | 15 | 33 | 26 | 30 | BELUM CUKUP | 5 | 13/3 | -5.35 | 8 | -6.46 | -0.61 | 5.8 | -1.18 | – | – |
| 62 | `M32` Momentum Burst | **44.4** | 47 | 28 | 52 | 22 | BELUM CUKUP | 18 | 73/49 | -1.17 | 28 | -4.58 | -0.32 | 8.7 | +0.09 | +0.40 | 0.18 |
| 63 | `N68X36` Bullish engulfing + EMA21 → ke | **44.4** | 32 | 40 | 43 | 30 | BELUM CUKUP | 14 | 134/46 | -1.85 | 15 | -1.30 | -0.15 | 4.9 | -0.53 | – | – |
| 64 | `N25X16` Supertrend + EMA + ADX>23 → ke | **44.4** | 29 | 41 | 38 | 45 | BELUM CUKUP | 13 | 125/48 | -4.02 | 15 | -0.75 | -0.16 | 2.7 | -1.08 | – | – |
| 65 | `M128` Inventory Retracement Bar (IRB | **44.3** | 48 | 33 | 55 | 17 | BELUM CUKUP | 25 | 195/140 | -0.84 | 28 | -3.86 | -0.35 | 7.4 | -0.01 | +0.53 | -0.05 |
| 66 | `M44` Tapak Rata IBD | **44.2** | 32 | 36 | 27 | 15 | BELUM CUKUP | 8 | 9/8 | -5.20 | 28 | -4.62 | -0.81 | 3.7 | -1.78 | – | -25.69 |
| 67 | `M121` High 2 bull flag (Brooks) | **44.2** | 21 | 20 | 24 | 15 | BELUM CUKUP | 5 | 8/3 | -5.66 | 24 | -4.46 | -0.58 | 4.9 | -1.31 | – | -13.14 |
| 68 | `M120` Reversal New Highs | **44.1** | 39 | 35 | 43 | 15 | BELUM CUKUP | 13 | 19/13 | -1.85 | 28 | -2.78 | -0.42 | 3.8 | -0.28 | – | -1.42 |
| 69 | `M132` Ascending Scallop (Bulkowski) | **44.0** | 36 | 44 | 50 | 13 | BELUM CUKUP | 19 | 97/52 | -2.60 | 28 | +0.21 | +0.03 | 3.3 | -0.14 | -0.47 | -0.89 |
| 70 | `M144` Screw Bar | **44.0** | 28 | 34 | 32 | 15 | BELUM CUKUP | 8 | 29/8 | -2.70 | 26 | -5.11 | -0.93 | 1.9 | -0.99 | – | -1.43 |
| 71 | `N65X36` Gap 4% + volum + hampir 52w →  | **44.0** | 24 | 19 | 28 | 30 | BELUM CUKUP | 6 | 31/6 | -4.09 | 15 | -5.10 | -0.67 | 4.0 | -1.19 | – | – |
| 72 | `M54` IBD Power Trend | **43.9** | 37 | 45 | 50 | 15 | BELUM CUKUP | 23 | 220/143 | -2.17 | 28 | +1.83 | +0.18 | 5.8 | -0.49 | -0.11 | -0.98 |
| 73 | `N65X14` Gap 4% + volum + hampir 52w →  | **43.8** | 23 | 18 | 30 | 30 | BELUM CUKUP | 6 | 31/10 | -4.09 | 15 | -5.93 | -0.70 | 4.2 | -1.22 | – | – |
| 74 | `M80` Radge Saluran Purata Bergerak  | **43.7** | 40 | 32 | 56 | 27 | BELUM CUKUP | 27 | 315/126 | -1.42 | 28 | -3.29 | -0.31 | 5.6 | +0.11 | +1.82 | 0.16 |
| 75 | `M150` Trend Bar Failure (Brooks) | **43.7** | 38 | 37 | 51 | 21 | BELUM CUKUP | 23 | 116/96 | -1.39 | 28 | -5.75 | -0.59 | 4.7 | -0.39 | +1.68 | -1.43 |
| 76 | `M143` 장대양봉 이후 눌림목 / 5일선 매매 (Undur ke | **43.6** | 31 | 48 | 34 | 22 | BELUM CUKUP | 15 | 29/6 | -1.87 | 27 | -0.12 | -0.02 | 2.2 | -0.89 | – | -6.86 |
| 77 | `N201X36` MA20 silang MA50 atas MA50 x X | **43.6** | 18 | 34 | 26 | 30 | BELUM CUKUP | 7 | 26/8 | -3.63 | 8 | -5.38 | -0.72 | 4.2 | -1.54 | – | – |
| 78 | `M12` Parabolic SAR | **43.4** | 39 | 46 | 50 | 12 | BELUM CUKUP | 28 | 414/293 | -2.41 | 28 | +0.43 | +0.07 | 3.4 | -0.54 | -0.90 | -1.18 |
| 79 | `M68` Kell Base n' Break | **43.4** | 32 | 44 | 47 | 12 | BELUM CUKUP | 16 | 52/18 | -2.66 | 28 | +0.26 | +0.03 | 3.2 | -0.08 | -0.88 | -0.45 |
| 80 | `M130` 多方炮 (dua lilin hijau mengapit  | **43.4** | 29 | 22 | 38 | 15 | BELUM CUKUP | 8 | 12/5 | -3.39 | 26 | -3.85 | -0.39 | 5.0 | -0.06 | – | -0.06 |
| 81 | `M15` Break & Retest + Henti ATR | **43.3** | 45 | 29 | 54 | 21 | BELUM CUKUP | 27 | 331/294 | -0.74 | 28 | -9.52 | -0.62 | 6.9 | -0.13 | +1.69 | -0.28 |
| 82 | `M116` 2/20 EMA Breakout (Landry) | **42.7** | 44 | 33 | 51 | 15 | BELUM CUKUP | 28 | 624/557 | -1.09 | 28 | -1.46 | -0.11 | 8.4 | -0.45 | -0.09 | -2.09 |
| 83 | `N66X36` 52w tinggi + pengesahan 1% → k | **42.7** | 23 | 20 | 31 | 30 | BELUM CUKUP | 8 | 40/7 | -3.99 | 14 | -4.38 | -0.52 | 4.6 | -1.04 | – | – |
| 84 | `M127` Slingshot Bullish | **42.6** | 32 | 39 | 46 | 19 | BELUM CUKUP | 20 | 112/92 | -2.02 | 28 | -5.58 | -0.58 | 4.8 | -0.86 | +1.07 | -0.99 |
| 85 | `N64X17` Episodic pivot → keluar bila a | **42.6** | 24 | 23 | 34 | 30 | BELUM CUKUP | 9 | 52/18 | -3.12 | 15 | -3.70 | -0.45 | 4.0 | -1.06 | – | – |
| 86 | `N48X36` Inside day pecah → keluar sele | **42.4** | 35 | 24 | 41 | 30 | BELUM CUKUP | 15 | 360/269 | -0.88 | 15 | -7.39 | -0.85 | 5.9 | -1.15 | – | – |
| 87 | `N75X17` RSI14 < 40 tanpa penapis → kel | **42.4** | 29 | 32 | 37 | 30 | BELUM CUKUP | 15 | 580/347 | -1.39 | 15 | -6.16 | -0.48 | 5.7 | -1.56 | – | – |
| 88 | `N64X36` Episodic pivot → keluar selepa | **42.4** | 22 | 22 | 34 | 30 | BELUM CUKUP | 9 | 52/15 | -3.27 | 15 | -4.00 | -0.46 | 4.2 | -0.95 | – | – |
| 89 | `N43X36` Undur EMA8 + penapis MA50 → ke | **42.3** | 27 | 33 | 40 | 30 | BELUM CUKUP | 15 | 256/113 | -2.65 | 15 | -3.17 | -0.44 | 3.7 | -1.32 | – | – |
| 90 | `N07X16` Tiga MA tersusun → keluar bila | **42.3** | 25 | 36 | 41 | 30 | BELUM CUKUP | 15 | 177/77 | -3.12 | 15 | -2.04 | -0.34 | 3.2 | -1.05 | – | – |
| 91 | `N64X16` Episodic pivot → keluar bila s | **42.3** | 21 | 22 | 36 | 30 | BELUM CUKUP | 9 | 52/22 | -3.11 | 15 | -4.46 | -0.56 | 3.6 | -0.95 | – | – |
| 92 | `M105` Supertrend tulen | **42.2** | 35 | 35 | 53 | 16 | BELUM CUKUP | 24 | 376/228 | -2.74 | 28 | -1.28 | -0.10 | 6.0 | -0.20 | +0.19 | -0.61 |
| 93 | `N36X36` Pocket pivot → keluar selepas  | **42.2** | 30 | 28 | 36 | 40 | BELUM CUKUP | 15 | 184/116 | -3.40 | 15 | -3.44 | -0.37 | 4.4 | -1.69 | – | – |
| 94 | `N37X36` Gap and go → keluar selepas DU | **42.2** | 27 | 28 | 34 | 30 | BELUM CUKUP | 12 | 91/40 | -3.82 | 15 | -1.80 | -0.24 | 3.8 | -1.45 | – | – |
| 95 | `N64X14` Episodic pivot → keluar bila r | **42.2** | 22 | 21 | 34 | 30 | BELUM CUKUP | 9 | 52/17 | -3.50 | 15 | -4.85 | -0.60 | 3.7 | -1.00 | – | – |
| 96 | `N37X17` Gap and go → keluar bila adx14 | **42.1** | 27 | 27 | 34 | 30 | BELUM CUKUP | 12 | 91/39 | -3.68 | 15 | -2.09 | -0.25 | 4.1 | -1.53 | – | – |
| 97 | `M111` Sistem Volatiliti Wilder | **42.0** | 36 | 37 | 53 | 12 | BELUM CUKUP | 26 | 276/172 | -2.46 | 28 | -0.55 | -0.05 | 5.0 | -0.16 | -0.67 | -0.44 |
| 98 | `M126` Hidden Smash Day (beli, Larry  | **42.0** | 26 | 31 | 37 | 15 | BELUM CUKUP | 12 | 20/11 | -2.86 | 27 | -4.61 | -0.57 | 5.1 | -0.63 | – | -0.77 |
| 99 | `N124X36` Episodic pivot gap 8-10% → kel | **41.9** | 25 | 24 | 34 | 30 | BELUM CUKUP | 11 | 55/18 | -2.35 | 15 | -6.87 | -0.58 | 6.2 | -1.13 | – | – |
| 100 | `N09X36` Undur EMA10 + penapis EMA50 →  | **41.8** | 25 | 32 | 39 | 30 | BELUM CUKUP | 15 | 274/126 | -2.74 | 15 | -3.76 | -0.50 | 3.9 | -1.38 | – | – |
| 101 | `N41X36` CMF20>0 + tutup>EMA20 → keluar | **41.8** | 26 | 31 | 36 | 30 | BELUM CUKUP | 14 | 283/230 | -2.73 | 15 | -6.18 | -0.72 | 4.7 | -1.76 | – | – |
| 102 | `M106` DMI Wilder | **41.7** | 34 | 37 | 50 | 13 | BELUM CUKUP | 24 | 139/113 | -1.92 | 28 | -3.33 | -0.44 | 3.5 | -0.56 | -0.51 | -1.41 |
| 103 | `N51X16` BB squeeze + Supertrend → kelu | **41.7** | 19 | 34 | 24 | 30 | BELUM CUKUP | 10 | 16/4 | -3.34 | 15 | -5.08 | -0.61 | 4.3 | -1.73 | – | – |
| 104 | `M04` BB Squeeze Breakout | **41.6** | 34 | 30 | 54 | 14 | BELUM CUKUP | 21 | 155/89 | -2.96 | 28 | -0.21 | -0.02 | 5.6 | -0.02 | -0.26 | -0.03 |
| 105 | `M88` O'Neil Shakeout +3 | **41.6** | 32 | 37 | 45 | 14 | BELUM CUKUP | 21 | 100/68 | -4.86 | 28 | -2.66 | -0.17 | 7.6 | -0.87 | -0.28 | -1.50 |
| 106 | `M135` 3rd Watch | **41.6** | 23 | 20 | 34 | 15 | BELUM CUKUP | 9 | 15/7 | -7.97 | 28 | -4.31 | -0.51 | 4.9 | -1.01 | – | -5.78 |
| 107 | `M89` Chande 65sma-3cc | **41.5** | 35 | 35 | 50 | 12 | BELUM CUKUP | 24 | 197/152 | -3.12 | 28 | -2.83 | -0.26 | 5.6 | -0.48 | -0.66 | -1.50 |
| 108 | `M67` Rayner Teo: Ujian Ketiga pada  | **41.4** | 34 | 31 | 42 | 15 | BELUM CUKUP | 19 | 35/27 | -2.69 | 28 | -5.19 | -0.43 | 7.4 | -0.79 | – | -3.04 |
| 109 | `M91` Stochastic Pop (Bernstein/Stec | **41.3** | 34 | 22 | 50 | 18 | BELUM CUKUP | 16 | 39/34 | -3.78 | 28 | -2.25 | -0.14 | 7.8 | +0.06 | -1.17 | 0.24 |
| 110 | `N40X36` OBV tinggi baharu + MA50 → kel | **41.3** | 34 | 18 | 47 | 30 | BELUM CUKUP | 15 | 87/34 | -1.24 | 15 | -9.21 | -0.63 | 8.2 | -0.06 | – | – |
| 111 | `N33X16` Donchian20 + penapis MA200 → k | **41.3** | 22 | 23 | 34 | 30 | BELUM CUKUP | 11 | 106/58 | -6.29 | 15 | -4.20 | -0.59 | 3.3 | -1.59 | – | – |
| 112 | `N68X16` Bullish engulfing + EMA21 → ke | **41.2** | 21 | 29 | 42 | 30 | BELUM CUKUP | 14 | 132/56 | -2.37 | 15 | -3.85 | -0.33 | 6.9 | -0.78 | – | – |
| 113 | `N53X17` Supertrend + ADX>25 → keluar b | **41.2** | 24 | 25 | 38 | 30 | BELUM CUKUP | 13 | 112/17 | -3.72 | 15 | -4.29 | -0.40 | 6.1 | -0.76 | – | – |
| 114 | `M49` Ichimoku (Tutup Atas Awan + Te | **41.1** | 36 | 37 | 47 | 12 | BELUM CUKUP | 28 | 361/249 | -2.34 | 28 | -2.62 | -0.23 | 4.9 | -0.98 | -0.68 | -1.39 |
| 115 | `N08X36` tutup>EMA20 tidak terlalu jauh | **41.1** | 24 | 33 | 34 | 30 | BELUM CUKUP | 15 | 488/393 | -2.42 | 15 | -6.16 | -0.64 | 4.7 | -1.94 | – | – |
| 116 | `N22X36` BB pecah atas + RSI → keluar s | **41.1** | 22 | 27 | 42 | 30 | BELUM CUKUP | 14 | 123/76 | -4.79 | 15 | -5.71 | -0.49 | 5.8 | -0.95 | – | – |
| 117 | `N33X36` Donchian20 + penapis MA200 → k | **41.1** | 22 | 22 | 34 | 30 | BELUM CUKUP | 11 | 102/53 | -5.15 | 15 | -5.73 | -0.66 | 4.4 | -1.62 | – | – |
| 118 | `N24X36` Supertrend(10,3) + ADX>20 → ke | **41.0** | 28 | 23 | 40 | 30 | BELUM CUKUP | 15 | 186/119 | -3.07 | 15 | -6.03 | -0.63 | 4.6 | -1.21 | – | – |
| 119 | `N25X17` Supertrend + EMA + ADX>23 → ke | **41.0** | 22 | 27 | 35 | 30 | BELUM CUKUP | 13 | 121/30 | -4.35 | 15 | -4.03 | -0.55 | 3.6 | -1.30 | – | – |
| 120 | `N53X16` Supertrend + ADX>25 → keluar b | **41.0** | 21 | 24 | 42 | 30 | BELUM CUKUP | 13 | 120/49 | -3.61 | 15 | -6.66 | -0.62 | 6.5 | -0.67 | – | – |
| 121 | `N38X36` VCP pecah → keluar selepas DUA | **40.9** | 25 | 32 | 31 | 30 | BELUM CUKUP | 15 | 47/26 | -3.09 | 15 | -5.19 | -0.63 | 4.1 | -1.76 | – | – |
| 122 | `N35X36` Pecah 52 minggu tinggi → kelua | **40.9** | 21 | 23 | 29 | 30 | BELUM CUKUP | 11 | 53/10 | -5.17 | 15 | -3.45 | -0.55 | 2.8 | -1.56 | – | – |
| 123 | `N51X36` BB squeeze + Supertrend → kelu | **40.9** | 18 | 27 | 23 | 30 | BELUM CUKUP | 10 | 16/6 | -3.74 | 15 | -5.87 | -0.69 | 4.5 | -1.99 | – | – |
| 124 | `M34` Carter TTM Squeeze | **40.8** | 34 | 28 | 51 | 14 | BELUM CUKUP | 22 | 107/66 | -1.82 | 28 | -4.32 | -0.34 | 6.1 | -0.22 | -0.14 | -0.58 |
| 125 | `N57X36` ADX bangkit daripada <20 → kel | **40.8** | 23 | 23 | 31 | 30 | BELUM CUKUP | 12 | 78/26 | -6.14 | 15 | -3.40 | -0.41 | 4.4 | -1.67 | – | – |
| 126 | `N33X14` Donchian20 + penapis MA200 → k | **40.8** | 24 | 18 | 31 | 30 | BELUM CUKUP | 11 | 116/36 | -6.56 | 15 | -4.40 | -0.72 | 3.6 | -1.78 | – | – |
| 127 | `M92` CCI-50 | **40.6** | 33 | 32 | 49 | 17 | BELUM CUKUP | 28 | 616/533 | -1.48 | 28 | -7.09 | -0.53 | 5.8 | -0.74 | +0.47 | -1.56 |
| 128 | `N07X36` Tiga MA tersusun → keluar sele | **40.6** | 22 | 28 | 39 | 30 | BELUM CUKUP | 15 | 173/66 | -3.78 | 15 | -4.28 | -0.54 | 4.4 | -1.25 | – | – |
| 129 | `N40X16` OBV tinggi baharu + MA50 → kel | **40.6** | 31 | 16 | 47 | 30 | BELUM CUKUP | 15 | 106/54 | -1.17 | 15 | -10.64 | -0.66 | 8.2 | -0.18 | – | – |
| 130 | `N37X16` Gap and go → keluar bila super | **40.6** | 22 | 21 | 34 | 30 | BELUM CUKUP | 12 | 91/49 | -4.11 | 15 | -4.34 | -0.61 | 3.5 | -1.57 | – | – |
| 131 | `M149` 3-Step Pullback | **40.5** | 30 | 33 | 54 | 15 | BELUM CUKUP | 26 | 264/107 | -1.99 | 28 | -3.06 | -0.26 | 6.8 | -0.06 | -0.12 | -0.05 |
| 132 | `M134` First Kiss After Daylight (Lan | **40.5** | 29 | 32 | 49 | 15 | BELUM CUKUP | 22 | 70/39 | -2.89 | 28 | -4.71 | -0.42 | 5.7 | -0.27 | +0.05 | -0.34 |
| 133 | `N31X36` Turtle sistem 2 → keluar selep | **40.5** | 21 | 18 | 32 | 30 | BELUM CUKUP | 11 | 105/25 | -5.20 | 15 | -5.81 | -0.59 | 4.9 | -1.48 | – | – |
| 134 | `M139` 均线首次粘合向上发散 (MA berhimpun kali  | **40.4** | 31 | 35 | 46 | 13 | BELUM CUKUP | 24 | 96/55 | -4.68 | 28 | -0.92 | -0.08 | 5.2 | -0.80 | -0.60 | -2.65 |
| 135 | `M136` Short/Intermediate-term Low (L | **40.3** | 30 | 35 | 47 | 17 | BELUM CUKUP | 28 | 947/497 | -3.74 | 28 | -4.20 | -0.40 | 4.4 | -0.96 | +0.52 | -0.59 |
| 136 | `M36` Turtle 55/20 | **40.3** | 31 | 29 | 52 | 16 | BELUM CUKUP | 25 | 348/228 | -2.23 | 28 | -4.22 | -0.30 | 7.9 | -0.28 | +0.27 | -0.60 |
| 137 | `N42X36` Lonjakan volum 2x → keluar sel | **40.3** | 26 | 20 | 41 | 30 | BELUM CUKUP | 15 | 236/143 | -1.63 | 15 | -8.61 | -0.81 | 6.0 | -1.19 | – | – |
| 138 | `N80X36` Tinggi sepanjang masa → keluar | **40.3** | 18 | 17 | 30 | 30 | BELUM CUKUP | 10 | 41/8 | -5.61 | 15 | -5.70 | -0.81 | 3.6 | -1.30 | – | – |
| 139 | `M156` Single Penetration (DiNapoli) | **40.2** | 37 | 28 | 48 | 15 | BELUM CUKUP | 28 | 309/235 | -1.35 | 28 | -5.05 | -0.35 | 8.3 | -0.84 | -0.03 | -2.41 |
| 140 | `M28` VWAP Separator + Kiss Pivot | **40.2** | 34 | 30 | 45 | 14 | BELUM CUKUP | 24 | 145/127 | -1.54 | 28 | -7.51 | -0.77 | 6.2 | -1.11 | -0.39 | -8.11 |
| 141 | `M119` 180 Bullish (Cooper) | **40.2** | 29 | 30 | 48 | 19 | BELUM CUKUP | 24 | 168/109 | -2.15 | 28 | -5.76 | -0.53 | 6.2 | -0.80 | +0.99 | -2.09 |
| 142 | `N36X16` Pocket pivot → keluar bila sup | **40.2** | 24 | 24 | 38 | 30 | BELUM CUKUP | 15 | 187/114 | -3.67 | 15 | -4.99 | -0.45 | 4.8 | -1.54 | – | – |
| 143 | `N19X13` Bawah jalur BB + RSI<30 → kelu | **40.1** | 19 | 23 | 23 | 30 | BELUM CUKUP | 11 | 144/0 | -4.36 | 15 | -5.88 | -0.76 | 4.3 | -1.21 | – | – |
| 144 | `N76X36` Tutup > MA50 (penapis trend tu | **39.9** | 23 | 23 | 36 | 30 | BELUM CUKUP | 15 | 211/153 | -3.49 | 15 | -10.16 | -0.87 | 6.5 | -1.68 | – | – |
| 145 | `N57X16` ADX bangkit daripada <20 → kel | **39.7** | 20 | 20 | 35 | 30 | BELUM CUKUP | 13 | 76/41 | -5.95 | 15 | -4.74 | -0.53 | 4.7 | -1.44 | – | – |
| 146 | `M50` Elder Triple Screen | **39.6** | 34 | 26 | 49 | 16 | BELUM CUKUP | 28 | 675/517 | -1.59 | 28 | -9.99 | -0.72 | 7.8 | -0.67 | +0.34 | -1.12 |
| 147 | `M148` Natural Number Method | **39.6** | 32 | 37 | 43 | 10 | BELUM CUKUP | 27 | 232/222 | -2.83 | 28 | -4.02 | -0.38 | 4.8 | -1.44 | -1.38 | -5.27 |
| 148 | `M140` 猎豹出击 (Serangan Cheetah) | **39.6** | 22 | 23 | 34 | 13 | BELUM CUKUP | 13 | 45/26 | -4.25 | 28 | -7.30 | -0.78 | 5.1 | -1.64 | -0.58 | -1.66 |
| 149 | `M14` Walking with the Whales | **39.4** | 37 | 24 | 49 | 15 | BELUM CUKUP | 28 | 1124/887 | -1.19 | 28 | -12.13 | -0.74 | 9.2 | -0.76 | +0.03 | -1.29 |
| 150 | `M26` Garis Trend Undur 3 Sentuhan + | **39.4** | 27 | 30 | 44 | 15 | BELUM CUKUP | 22 | 90/59 | -1.62 | 28 | -7.10 | -0.70 | 5.0 | -0.99 | +0.09 | -1.33 |
| 151 | `N42X16` Lonjakan volum 2x → keluar bil | **39.3** | 22 | 18 | 41 | 30 | BELUM CUKUP | 15 | 240/153 | -1.82 | 15 | -8.62 | -0.81 | 6.2 | -1.19 | – | – |
| 152 | `N75X14` RSI14 < 40 tanpa penapis → kel | **39.3** | 19 | 24 | 37 | 30 | BELUM CUKUP | 15 | 398/70 | -2.12 | 15 | -7.20 | -0.76 | 5.1 | -1.50 | – | – |
| 153 | `N119X13` 3 tutup turun berturut → kelua | **39.3** | 21 | 18 | 37 | 30 | BELUM CUKUP | 14 | 289/69 | -1.51 | 15 | -9.41 | -0.85 | 7.6 | -1.44 | – | – |
| 154 | `N24X17` Supertrend(10,3) + ADX>20 → ke | **39.3** | 19 | 19 | 33 | 30 | BELUM CUKUP | 13 | 135/55 | -5.48 | 15 | -5.70 | -0.59 | 4.6 | -1.82 | – | – |
| 155 | `N119X15` 3 tutup turun berturut → ekori | **39.3** | 15 | 12 | 18 | 30 | BELUM CUKUP | 9 | 58/0 | -4.19 | 15 | -8.35 | -0.73 | 6.7 | -1.71 | – | – |
| 156 | `M06` Minervini VCP Breakout | **39.2** | 29 | 31 | 45 | 12 | BELUM CUKUP | 24 | 90/60 | -3.68 | 28 | -4.11 | -0.44 | 4.4 | -0.87 | -0.90 | -2.26 |
| 157 | `M152` Spike & Ledge | **39.2** | 26 | 34 | 42 | 15 | BELUM CUKUP | 23 | 57/14 | -4.06 | 28 | -2.89 | -0.23 | 5.4 | -0.65 | -0.05 | -1.83 |
| 158 | `N124X15` Episodic pivot gap 8-10% → eko | **39.2** | 18 | 16 | 23 | 30 | BELUM CUKUP | 11 | 54/0 | -5.48 | 15 | -7.76 | -0.57 | 6.3 | -1.24 | – | – |
| 159 | `M99` Three Line Break | **39.1** | 32 | 28 | 48 | 13 | BELUM CUKUP | 26 | 183/143 | -3.75 | 28 | -4.11 | -0.32 | 5.8 | -0.84 | -0.59 | -2.99 |
| 160 | `N41X16` CMF20>0 + tutup>EMA20 → keluar | **39.1** | 18 | 25 | 36 | 30 | BELUM CUKUP | 15 | 332/260 | -3.19 | 15 | -6.62 | -0.66 | 4.9 | -1.72 | – | – |
| 161 | `N24X16` Supertrend(10,3) + ADX>20 → ke | **39.1** | 18 | 18 | 35 | 30 | BELUM CUKUP | 13 | 126/62 | -5.90 | 15 | -6.25 | -0.68 | 4.7 | -1.59 | – | – |
| 162 | `M57` Landry Trend Knockout (TKO) | **39.0** | 34 | 31 | 44 | 10 | BELUM CUKUP | 28 | 201/154 | -2.31 | 28 | -5.37 | -0.61 | 4.9 | -1.31 | -1.37 | -3.31 |
| 163 | `M107` Golden Cross SMA50/200 | **39.0** | 23 | 31 | 45 | 18 | BELUM CUKUP | 22 | 47/13 | -2.14 | 28 | -4.75 | -0.46 | 4.4 | -0.27 | +0.78 | -0.42 |
| 164 | `N76X16` Tutup > MA50 (penapis trend tu | **39.0** | 17 | 27 | 34 | 30 | BELUM CUKUP | 15 | 399/307 | -2.68 | 15 | -6.43 | -0.70 | 4.0 | -1.98 | – | – |
| 165 | `N113X36` 80-20 bar (sisi beli) → keluar | **38.9** | 23 | 16 | 38 | 30 | BELUM CUKUP | 15 | 390/315 | -1.43 | 15 | -12.22 | -0.91 | 9.0 | -1.45 | – | – |
| 166 | `N54X16` Supertrend + RSI>50 → keluar b | **38.9** | 16 | 13 | 30 | 30 | BELUM CUKUP | 11 | 128/71 | -7.16 | 15 | -7.03 | -0.76 | 5.9 | -2.12 | – | – |
| 167 | `N39X36` NR7 kemudian pecah → keluar se | **38.9** | 8 | 6 | 26 | 30 | BELUM CUKUP | 8 | 35/12 | -6.02 | 14 | -12.36 | -0.81 | 9.0 | -1.87 | – | – |
| 168 | `N08X16` tutup>EMA20 tidak terlalu jauh | **38.8** | 15 | 27 | 36 | 30 | BELUM CUKUP | 15 | 571/454 | -2.42 | 15 | -8.64 | -0.74 | 5.0 | -1.78 | – | – |
| 169 | `N56X36` RSI>50 + ADX>20 → keluar selep | **38.8** | 20 | 20 | 35 | 30 | BELUM CUKUP | 15 | 216/147 | -3.09 | 15 | -10.08 | -0.77 | 7.5 | -1.83 | – | – |
| 170 | `N45X36` Undur EMA21 cerun positif → ke | **38.8** | 17 | 20 | 37 | 30 | BELUM CUKUP | 14 | 161/97 | -3.87 | 15 | -8.95 | -0.77 | 5.7 | -1.58 | – | – |
| 171 | `N37X14` Gap and go → keluar bila rsi14 | **38.8** | 17 | 15 | 32 | 30 | BELUM CUKUP | 12 | 90/28 | -5.37 | 15 | -8.06 | -0.61 | 6.5 | -1.64 | – | – |
| 172 | `M02` MACD + SMA200 | **38.6** | 31 | 21 | 44 | 36 | BELUM CUKUP | 28 | 144/126 | -4.11 | 28 | -5.29 | -0.33 | 6.7 | -1.31 | +0.29 | -8.54 |
| 173 | `N113X16` 80-20 bar (sisi beli) → keluar | **38.6** | 26 | 12 | 40 | 30 | BELUM CUKUP | 15 | 416/325 | -1.15 | 15 | -12.82 | -0.90 | 9.8 | -1.25 | – | – |
| 174 | `N56X17` RSI>50 + ADX>20 → keluar bila  | **38.6** | 20 | 18 | 32 | 30 | BELUM CUKUP | 14 | 150/69 | -5.64 | 15 | -6.20 | -0.66 | 4.5 | -2.02 | – | – |
| 175 | `M73` ADX(5) > 40 + Julat Terkecil 6 | **38.5** | 34 | 24 | 47 | 14 | BELUM CUKUP | 28 | 1194/1009 | -0.75 | 28 | -9.39 | -0.75 | 7.6 | -0.90 | -0.16 | -5.03 |
| 176 | `M95` Nisbah Kebaharuan High 52 Ming | **38.5** | 24 | 26 | 49 | 15 | BELUM CUKUP | 22 | 128/82 | -2.26 | 28 | -8.69 | -0.70 | 6.9 | -0.49 | +0.07 | -1.04 |
| 177 | `N27X16` Ichimoku atas awan → keluar bi | **38.5** | 17 | 21 | 35 | 30 | BELUM CUKUP | 15 | 205/126 | -2.64 | 15 | -8.39 | -0.87 | 4.9 | -1.80 | – | – |
| 178 | `N74X16` MACD atas garis isyarat (keada | **38.4** | 14 | 26 | 34 | 30 | BELUM CUKUP | 15 | 761/661 | -2.08 | 15 | -9.13 | -0.67 | 6.5 | -1.94 | – | – |
| 179 | `M66` IBD Undur Pertama ke Purata 50 | **38.2** | 30 | 24 | 49 | 13 | BELUM CUKUP | 27 | 288/206 | -2.21 | 28 | -5.86 | -0.45 | 8.1 | -0.75 | -0.48 | -1.78 |
| 180 | `N56X16` RSI>50 + ADX>20 → keluar bila  | **38.2** | 14 | 22 | 39 | 30 | BELUM CUKUP | 15 | 249/175 | -2.95 | 15 | -8.02 | -0.77 | 5.5 | -1.35 | – | – |
| 181 | `N16X13` RSI2<10 tanpa penapis → keluar | **38.2** | 18 | 19 | 32 | 30 | BELUM CUKUP | 15 | 314/6 | -1.46 | 15 | -11.02 | -0.82 | 8.5 | -1.16 | – | – |
| 182 | `M59` Anjakan Julat RSI | **38.1** | 22 | 20 | 42 | 3 | BELUM CUKUP | 14 | 36/24 | -6.07 | 28 | -5.15 | -0.50 | 5.7 | -0.61 | -3.13 | -2.00 |
| 183 | `M141` First Thrust (Landry) | **37.9** | 7 | 7 | 33 | 15 | BELUM CUKUP | 9 | 27/18 | -7.52 | 28 | -15.30 | -0.82 | 8.5 | -1.40 | – | -4.93 |
| 184 | `N73X13` Tutup bawah jalur bawah BB(20, | **37.8** | 17 | 21 | 27 | 30 | BELUM CUKUP | 15 | 228/1 | -2.80 | 15 | -8.02 | -0.70 | 6.5 | -1.24 | – | – |
| 185 | `N75X13` RSI14 < 40 tanpa penapis → kel | **37.8** | 16 | 22 | 27 | 30 | BELUM CUKUP | 15 | 212/1 | -2.36 | 15 | -8.57 | -0.73 | 5.7 | -1.16 | – | – |
| 186 | `M29` EMA3 + RSI75 + Stokastik | **37.7** | 28 | 28 | 42 | 4 | BELUM CUKUP | 20 | 48/34 | -1.87 | 28 | -9.14 | -0.66 | 8.6 | -0.95 | -2.94 | -4.43 |
| 187 | `N36X14` Pocket pivot → keluar bila rsi | **37.7** | 20 | 14 | 33 | 30 | BELUM CUKUP | 15 | 186/59 | -5.05 | 15 | -7.59 | -0.74 | 5.6 | -1.82 | – | – |
| 188 | `N22X14` BB pecah atas + RSI → keluar b | **37.7** | 17 | 14 | 35 | 30 | BELUM CUKUP | 14 | 130/49 | -6.40 | 15 | -8.21 | -0.68 | 6.6 | -1.50 | – | – |
| 189 | `N75X15` RSI14 < 40 tanpa penapis → eko | **37.6** | 16 | 22 | 25 | 30 | BELUM CUKUP | 15 | 206/0 | -2.43 | 15 | -8.57 | -0.73 | 5.7 | -1.14 | – | – |
| 190 | `N22X16` BB pecah atas + RSI → keluar b | **37.6** | 15 | 13 | 40 | 30 | BELUM CUKUP | 14 | 124/80 | -6.45 | 15 | -8.06 | -0.77 | 5.8 | -1.10 | – | – |
| 191 | `M55` Guppy GMMA | **37.2** | 26 | 23 | 48 | 13 | BELUM CUKUP | 26 | 290/192 | -2.34 | 28 | -8.51 | -0.74 | 6.3 | -0.77 | -0.43 | -1.91 |
| 192 | `M101` Bulkowski: Tiga lembah menaik | **37.2** | 22 | 15 | 48 | 11 | BELUM CUKUP | 17 | 46/29 | -3.25 | 28 | -8.95 | -0.60 | 9.3 | -0.10 | -1.08 | -0.25 |
| 193 | `M155` Market Cycle Strategy | **37.1** | 27 | 24 | 44 | 17 | BELUM CUKUP | 28 | 804/591 | -4.73 | 28 | -6.31 | -0.54 | 5.8 | -1.36 | +0.47 | -3.51 |
| 194 | `N42X14` Lonjakan volum 2x → keluar bil | **37.1** | 18 | 11 | 38 | 30 | BELUM CUKUP | 15 | 213/49 | -3.49 | 15 | -9.30 | -0.76 | 6.8 | -1.18 | – | – |
| 195 | `N50X14` Mampat + pecah volum 1.5x → ke | **37.1** | 12 | 10 | 30 | 30 | BELUM CUKUP | 12 | 34/7 | -3.67 | 15 | -10.89 | -0.77 | 7.3 | -1.34 | – | – |
| 196 | `N55X13` BB + RSI + ADX>20 → keluar bil | **37.0** | 17 | 19 | 21 | 30 | BELUM CUKUP | 15 | 143/0 | -1.85 | 15 | -7.89 | -0.87 | 5.6 | -1.60 | – | – |
| 197 | `N29X36` PSAR naik + tutup>MA50 → kelua | **36.9** | 15 | 13 | 28 | 30 | BELUM CUKUP | 14 | 175/124 | -4.81 | 15 | -13.52 | -0.93 | 10.0 | -2.59 | – | – |
| 198 | `M125` 2-Bar Breakout | **36.7** | 26 | 24 | 45 | 13 | BELUM CUKUP | 28 | 1159/671 | -4.39 | 28 | -7.33 | -0.50 | 6.4 | -1.16 | -0.57 | -0.63 |
| 199 | `M11` NR7 Breakout + Volume | **36.7** | 27 | 20 | 46 | 12 | BELUM CUKUP | 25 | 132/100 | -1.18 | 28 | -11.84 | -0.69 | 9.7 | -0.96 | -0.73 | -0.90 |
| 200 | `N47X16` NR7 + EMA9>EMA21 → keluar bila | **36.7** | 11 | 17 | 37 | 30 | BELUM CUKUP | 15 | 209/110 | -3.69 | 15 | -10.67 | -0.77 | 7.9 | -1.66 | – | – |
| 201 | `N27X36` Ichimoku atas awan → keluar se | **36.7** | 16 | 11 | 31 | 30 | BELUM CUKUP | 14 | 123/52 | -5.04 | 15 | -11.25 | -0.88 | 6.5 | -2.07 | – | – |
| 202 | `N28X17` ADX>25 + DI+ > DI- → keluar bi | **36.6** | 15 | 15 | 29 | 30 | BELUM CUKUP | 15 | 165/15 | -4.92 | 15 | -7.79 | -0.64 | 6.3 | -1.84 | – | – |
| 203 | `N29X16` PSAR naik + tutup>MA50 → kelua | **36.4** | 13 | 15 | 31 | 30 | BELUM CUKUP | 15 | 237/177 | -4.67 | 15 | -9.39 | -0.79 | 6.8 | -2.32 | – | – |
| 204 | `N42X15` Lonjakan volum 2x → ekori Chan | **36.3** | 17 | 13 | 24 | 30 | BELUM CUKUP | 15 | 197/0 | -4.40 | 15 | -9.60 | -0.71 | 7.1 | -1.25 | – | – |
| 205 | `M31` Band Walk (BB 20/2) | **36.2** | 26 | 15 | 54 | 18 | BELUM CUKUP | 26 | 405/198 | -1.98 | 28 | -7.09 | -0.43 | 9.2 | -0.14 | +0.72 | -0.26 |
| 206 | `M19` Sneaky Pivot (proksi harian) | **36.1** | 22 | 24 | 45 | 12 | BELUM CUKUP | 26 | 453/353 | -4.83 | 28 | -7.90 | -0.53 | 6.7 | -1.17 | -0.66 | -15.68 |
| 207 | `N28X14` ADX>25 + DI+ > DI- → keluar bi | **36.0** | 12 | 12 | 34 | 30 | BELUM CUKUP | 15 | 240/56 | -4.59 | 15 | -9.87 | -0.66 | 7.4 | -1.79 | – | – |
| 208 | `N54X36` Supertrend + RSI>50 → keluar s | **35.9** | 14 | 8 | 32 | 30 | BELUM CUKUP | 14 | 198/137 | -4.03 | 15 | -13.84 | -0.97 | 9.2 | -2.15 | – | – |
| 209 | `N50X17` Mampat + pecah volum 1.5x → ke | **35.8** | 8 | 7 | 30 | 30 | BELUM CUKUP | 12 | 33/6 | -3.89 | 15 | -12.63 | -0.80 | 8.5 | -1.29 | – | – |
| 210 | `N16X15` RSI2<10 tanpa penapis → ekori  | **35.6** | 11 | 15 | 24 | 30 | BELUM CUKUP | 15 | 286/0 | -1.71 | 15 | -13.12 | -0.83 | 10.7 | -1.23 | – | – |
| 211 | `M47` Holy Grail Raschke | **35.5** | 15 | 19 | 33 | 15 | BELUM CUKUP | 18 | 47/33 | -2.39 | 28 | -10.48 | -0.83 | 7.5 | -1.97 | – | -16.27 |
| 212 | `M154` HOLP (High of Low Period) | **34.6** | 15 | 16 | 41 | 12 | BELUM CUKUP | 20 | 109/51 | -4.50 | 28 | -12.01 | -0.78 | 8.8 | -1.26 | -0.83 | -4.93 |
| 213 | `N42X17` Lonjakan volum 2x → keluar bil | **34.6** | 11 | 6 | 40 | 30 | BELUM CUKUP | 15 | 230/83 | -2.78 | 15 | -13.62 | -0.92 | 8.5 | -1.15 | – | – |
| 214 | `N47X36` NR7 + EMA9>EMA21 → keluar sele | **34.3** | 5 | 10 | 32 | 30 | BELUM CUKUP | 14 | 188/83 | -4.49 | 15 | -16.05 | -0.82 | 11.3 | -2.06 | – | – |
| 215 | `M03` BB Break + Divergence RSI | **33.6** | 14 | 23 | 46 | 15 | BELUM CUKUP | 28 | 493/405 | -2.46 | 28 | -10.72 | -0.72 | 6.3 | -1.09 | -0.04 | -4.38 |
| 216 | `M79` Radge: 20% Flipper | **33.5** | 17 | 18 | 42 | 13 | BELUM CUKUP | 27 | 428/234 | -5.96 | 28 | -10.88 | -0.68 | 8.5 | -1.54 | -0.46 | -3.10 |
| 217 | `M81` Bensdorp Long Trend High Momen | **33.3** | 2 | 6 | 41 | 15 | BELUM CUKUP | 13 | 432/217 | -6.05 | 28 | -23.07 | -0.87 | 16.8 | -1.36 | – | -3.87 |
| 218 | `M82` Arthur Hill Rotasi Sasaran 10% | **32.8** | 20 | 11 | 49 | 18 | BELUM CUKUP | 28 | 608/286 | -2.44 | 28 | -9.06 | -0.46 | 11.7 | -0.75 | +0.66 | -2.88 |
| 219 | `M122` Moving Momentum (ChartSchool) | **32.8** | 18 | 18 | 35 | 10 | BELUM CUKUP | 27 | 120/80 | -5.33 | 28 | -12.92 | -0.77 | 8.3 | -2.26 | -1.32 | -6.41 |
| 220 | `M147` Improved Three-Bar Pullback | **32.8** | 9 | 14 | 34 | 10 | BELUM CUKUP | 19 | 125/58 | -6.26 | 28 | -16.79 | -0.79 | 9.3 | -2.03 | -1.38 | -1.80 |
| 221 | `M161` EMA 10/21 + Supertrend (10,3) | **32.5** | 16 | 12 | 50 | 18 | BELUM CUKUP | 28 | 534/392 | -1.79 | 28 | -17.41 | -0.79 | 12.5 | -0.56 | +0.86 | -1.23 |
| 222 | `M76` Undercut & Rally pada Low Pent | **32.2** | 12 | 18 | 40 | 7 | BELUM CUKUP | 24 | 98/82 | -2.85 | 28 | -13.37 | -0.91 | 8.5 | -1.63 | -2.23 | -5.91 |
| 223 | `M90` Pring KST | **31.5** | 11 | 15 | 44 | 9 | BELUM CUKUP | 25 | 94/67 | -4.03 | 28 | -14.87 | -0.74 | 13.3 | -1.10 | -1.69 | -3.98 |
| 224 | `M09` Volumatic VIDYA Pivot Retest | **31.5** | 4 | 10 | 28 | 15 | BELUM CUKUP | 17 | 45/33 | -5.72 | 28 | -17.41 | -0.93 | 10.8 | -2.46 | – | -12.28 |
| 225 | `M123` CCI Correction (Lambert, Chart | **31.1** | 9 | 22 | 33 | 11 | BELUM CUKUP | 26 | 198/189 | -2.09 | 28 | -16.02 | -0.95 | 9.1 | -2.54 | -1.01 | -4.84 |
| 226 | `M01` Bollinger Band + RSI | **30.9** | 14 | 8 | 41 | 18 | BELUM CUKUP | 25 | 140/28 | -3.60 | 28 | -14.71 | -0.88 | 7.3 | -1.12 | +0.77 | -4.04 |
| 227 | `M20` EMA10/15 Crossover + Sudut | **30.0**⌈ | 36 | 36 | 45 | 12 | GAGAL | 28 | 601/495 | -1.53 | 28 | -5.96 | -0.54 | 5.0 | -1.17 | -0.77 | -7.30 |

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

