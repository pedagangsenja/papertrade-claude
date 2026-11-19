# Skor Kaedah 0–100 (pangkat maklumat, BUKAN keputusan)

> **Status keputusan (kad skor, harga 2026-11-18):** TERBUKTI 0 · CALON 0 · BELUM CUKUP 225 · GAGAL 1 · NEGATIF 0. Rejim QQQ OFF sejak 2026-10-16. Hanya **TERBUKTI** layak untuk wang sebenar (`laporan/KAD_SKOR.md`); nombor dalam laporan ini BUKAN keputusan dan tidak boleh dibaca sebagai pangkat untuk wang sebenar.

Dijana 2026-11-19 oleh `standard/skor_kaedah.py` (Actions `analisis.yml`, selepas kad skor). Harga pada tutup 2026-11-18; 226 kaedah; 24 hari beli langsung (rejim ON 1, OFF 23). Pradaftar 2026-11-09: `standard/SPEC_SKOR_KAEDAH.md` (berat dan sauh dikunci `ujian/test_skor_kaedah.py::TestKunci`). Rekod analisis sahaja: tiada order, tiada wang sebenar.

## Cara membaca

- **Skor** = min geometri berberat empat tiang (Untung 35 · Tahan 30 · Bukti 25 · Konsisten 10), dikecut ke 50 mengikut data: berat data = hari beli ÷ (hari beli + 20). Kaedah dengan 2 hari beli tidak boleh menjauhi 50. 100 = unggul semua segi; 50 = neutral/tiada bukti; < 50 = lebih buruk daripada neutral.
- **Siling** ikut kad skor: NEGATIF ≤ 20, GANTUNG/BERSARA ≤ 30, GAGAL ≤ 40. Tanda ⌈ = siling terpakai.
- **Satu-satunya status yang membenarkan wang sebenar ialah TERBUKTI dalam `laporan/KAD_SKOR.md`.** Skor tinggi dengan status BELUM CUKUP bermaksud "paling menjanjikan setakat ini", bukan "selamat".
- Deflasi ujian berganda (López de Prado): sauh t Bukti C1 = maks(2.0, E[maks 226 normal]) = 2.81.
- **Semakan kebolehramalan:** skor pada 2026-11-11 lawan pulangan lorong T4 sejak itu, 223 kaedah: Spearman ρ = -0.091 (p = 0.177). Belum ada bukti skor meramal pangkat; jangan pilih kaedah dengannya.
- Metrik T4 (A2, B1, B2, D1) dikira atas lorong T4 L1 **dipotong pada sesi LANGSUNG pertama** kaedah itu (Mxx 2026-10-16, Nxx/GB 2026-11-03) dan diasas semula; sesi isian bina semula tidak dikira (pindaan 9 Nov 2026 (a)). Lajur "T4 sesi/pul" di bawah ialah potongan itu, bukan lorong penuh `T4_KAEDAH.md`.

## Semua kaedah, susun ikut Skor

| # | Kaedah | Skor | Untung | Tahan | Bukti | Konsisten | Status kad | Hari beli | Posisi/tutup | Jangkaan % | T4 sesi | T4 pul % | T4 pul/|MDD| | Ulcer | t buku | Lift | WFE |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `M146` 3-Bar Momentum Pattern | **60.1** | 73 | 75 | 59 | 85 | BELUM CUKUP | 19 | 79/36 | +0.42 | 24 | +5.74 | +0.93 | 2.7 | +0.99 | – | 1.80 |
| 2 | `M151` Outside Bar Failure | **59.1** | 66 | 80 | 56 | 72 | BELUM CUKUP | 22 | 110/65 | -0.32 | 24 | +8.14 | +5.05 | 0.6 | +0.35 | – | 0.57 |
| 3 | `M133` Bull Hook (Crabel) | **56.1** | 60 | 68 | 58 | 85 | BELUM CUKUP | 16 | 54/36 | -0.47 | 24 | +2.93 | +0.60 | 2.0 | +0.97 | – | 8.40 |
| 4 | `M25` VWAP Wave (proksi harian) | **55.8** | 61 | 65 | 57 | 60 | BELUM CUKUP | 22 | 195/135 | -0.66 | 24 | +3.80 | +0.63 | 3.5 | +0.34 | – | 1.76 |
| 5 | `M118` Expansion Pivot (Cooper) | **55.0** | 54 | 67 | 53 | 85 | BELUM CUKUP | 20 | 85/31 | -0.75 | 24 | +5.13 | +0.87 | 1.9 | +0.36 | – | 1.05 |
| 6 | `M48` Cooper 1-2-3-4 | **54.8** | 59 | 60 | 53 | 85 | BELUM CUKUP | 19 | 64/20 | -0.55 | 24 | +8.74 | +1.60 | 2.2 | +0.55 | – | 1.18 |
| 7 | `M23` Breitstein Kapitulasi + Kesina | **53.1** | 58 | 56 | 58 | 45 | BELUM CUKUP | 22 | 128/88 | -0.76 | 24 | +0.17 | +0.03 | 2.8 | +0.53 | – | 1.81 |
| 8 | `M159` Heikin-Ashi Trend | **52.7** | 54 | 65 | 46 | 55 | BELUM CUKUP | 24 | 1863/1736 | -0.81 | 24 | +5.02 | +0.82 | 3.5 | -1.01 | – | -5.19 |
| 9 | `M74` Lulus Baharu Trend Template Mi | **52.5** | 55 | 59 | 52 | 47 | BELUM CUKUP | 24 | 103/70 | -1.09 | 24 | +1.51 | +0.30 | 2.8 | -0.15 | – | -0.24 |
| 10 | `M100` Bulkowski Segi Empat & Segi Ti | **52.2** | 56 | 55 | 50 | 62 | BELUM CUKUP | 16 | 60/41 | -0.38 | 24 | +0.84 | +0.18 | 2.4 | +0.05 | – | 0.23 |
| 11 | `M70` Pecahan Hari Dalam | **52.0** | 61 | 64 | 52 | 21 | BELUM CUKUP | 24 | 498/420 | -0.65 | 24 | +1.55 | +0.33 | 2.1 | -0.28 | – | -0.63 |
| 12 | `M160` Measured Move Up | **51.5** | 38 | 62 | 59 | 85 | BELUM CUKUP | 22 | 121/82 | -1.97 | 24 | +1.82 | +0.39 | 2.3 | +0.68 | – | 4.82 |
| 13 | `M77` Undercut & Rally pada Purata B | **51.2** | 57 | 52 | 46 | 55 | BELUM CUKUP | 17 | 54/38 | -0.62 | 24 | -0.80 | -0.21 | 1.8 | -0.46 | – | -0.55 |
| 14 | `M104` High Tight Flag / Power Play | **51.1** | 84 | 90 | 44 | 85 | BELUM CUKUP | 1 | 1/0 | +23.01 | 9 | +2.32 | +10.00 | 0.0 | +2.00 | – | 13.83 |
| 15 | `N202X36` RSI2<10 dalam trend naik x X36 | **51.1** | 67 | 88 | 28 | 50 | BELUM CUKUP | 4 | 69/0 | +0.39 | 4 | +2.23 | +1.68 | 0.7 | -0.22 | – | – |
| 16 | `M33` Supertrend + SMA10 | **50.9** | 38 | 63 | 54 | 74 | BELUM CUKUP | 22 | 222/72 | -1.72 | 24 | +5.70 | +1.30 | 1.9 | +0.13 | – | 0.64 |
| 17 | `M13` Garis Trend Action/Safety Line | **50.2** | 40 | 68 | 47 | 55 | BELUM CUKUP | 24 | 826/593 | -1.93 | 24 | +6.52 | +1.83 | 1.4 | -0.91 | – | -2.01 |
| 18 | `M51` O'Neil Cawan & Pemegang | **50.1** | 58 | 57 | 39 | 45 | BELUM CUKUP | 2 | 3/1 | -0.49 | 14 | -0.11 | -0.11 | 0.6 | +0.94 | – | 2.62 |
| 19 | `M46` Jurang Naik Boleh Beli (Buyabl | **50.1** | 44 | 61 | 46 | 55 | BELUM CUKUP | 13 | 36/24 | -1.61 | 24 | +1.28 | +0.26 | 1.6 | -0.23 | – | -0.34 |
| 20 | `M145` Yum-Yum Continuation | **49.5** | 37 | 64 | 51 | 55 | BELUM CUKUP | 22 | 309/79 | -1.83 | 24 | +3.93 | +1.80 | 1.2 | -0.25 | – | -0.19 |
| 21 | `M129` Wick Play | **49.4** | 44 | 56 | 44 | 58 | BELUM CUKUP | 10 | 25/9 | -1.62 | 24 | +2.62 | +0.77 | 1.4 | +0.02 | – | 0.08 |
| 22 | `M10` EMA3 + CCI + MACD | **49.3** | 38 | 60 | 51 | 55 | BELUM CUKUP | 21 | 126/68 | -2.17 | 24 | +10.20 | +1.94 | 2.2 | -0.23 | – | -0.64 |
| 23 | `M07` Qullamaggie Breakout | **49.3** | 32 | 64 | 27 | 15 | BELUM CUKUP | 1 | 1/1 | -2.53 | 24 | -0.25 | -0.21 | 0.8 | -0.22 | – | -1.12 |
| 24 | `M45` High 52 Minggu (George & Hwang | **49.3** | 24 | 46 | 34 | 54 | BELUM CUKUP | 1 | 2/1 | -2.47 | 13 | -0.47 | -0.26 | 0.9 | +0.55 | – | 1.57 |
| 25 | `M158` Doubly Adaptive Profit Targets | **49.2** | 54 | 38 | 58 | 45 | BELUM CUKUP | 23 | 384/164 | -0.46 | 24 | -2.65 | -0.36 | 3.8 | +0.47 | – | 1.05 |
| 26 | `M05` MACD Divergence + Pengesahan | **48.9** | 42 | 59 | 40 | 55 | BELUM CUKUP | 15 | 41/13 | -1.93 | 24 | +1.90 | +0.44 | 1.8 | -0.64 | – | -0.97 |
| 27 | `M137` Livermore System | **48.8** | 37 | 58 | 52 | 55 | BELUM CUKUP | 23 | 177/77 | -2.00 | 24 | +3.98 | +0.67 | 2.2 | -0.15 | – | -0.28 |
| 28 | `M27` Price Action 4 Tiang | **48.7** | 43 | 37 | 38 | 15 | BELUM CUKUP | 2 | 546/488 | -1.26 | 24 | -2.79 | -0.54 | 2.9 | -0.91 | – | -2.75 |
| 29 | `M84` Jarak purata bergerak MAD 21/2 | **48.5** | 21 | 11 | 32 | 15 | BELUM CUKUP | 1 | 58/40 | -4.29 | 13 | -7.93 | -0.99 | 6.6 | -0.90 | – | -2.19 |
| 30 | `N25X36` Supertrend + EMA + ADX>23 → ke | **48.4** | 38 | 55 | 38 | 70 | BELUM CUKUP | 10 | 135/41 | -1.77 | 11 | +1.01 | +0.23 | 2.0 | -0.96 | – | – |
| 31 | `M39` Radge Pecahan Bollinger 100 ha | **48.3** | 34 | 62 | 48 | 55 | BELUM CUKUP | 22 | 241/56 | -3.16 | 24 | +5.26 | +2.10 | 1.3 | -0.47 | – | -0.86 |
| 32 | `N75X17` RSI14 < 40 tanpa penapis → kel | **48.2** | 42 | 47 | 39 | 70 | BELUM CUKUP | 11 | 369/186 | -1.01 | 11 | -1.05 | -0.17 | 3.2 | -1.25 | – | – |
| 33 | `M96` Momo India: Ranking Sharpe 3/6 | **48.2** | 19 | 8 | 9 | 15 | BELUM CUKUP | 1 | 6/6 | -13.71 | 13 | -8.21 | -1.00 | 7.0 | -5.92 | – | -15.55 |
| 34 | `M35` Pocket Pivot Morales & Kacher | **48.1** | 60 | 44 | 54 | 15 | BELUM CUKUP | 23 | 319/259 | -0.39 | 24 | -1.86 | -0.20 | 5.3 | -0.06 | – | -0.28 |
| 35 | `M93` Bollinger Kaedah II: %b + MFI | **48.0** | 56 | 40 | 56 | 24 | BELUM CUKUP | 23 | 271/88 | -0.45 | 24 | -0.76 | -0.12 | 3.3 | +0.23 | – | 0.29 |
| 36 | `N53X36` Supertrend + ADX>25 → keluar s | **48.0** | 53 | 39 | 48 | 30 | BELUM CUKUP | 11 | 137/43 | -0.63 | 11 | -2.39 | -0.51 | 2.7 | +0.10 | – | – |
| 37 | `M94` Pecutan Momentum (Chen, Yu & W | **48.0** | 7 | 4 | 14 | 15 | BELUM CUKUP | 1 | 33/0 | -11.13 | 13 | -12.72 | -1.00 | 7.9 | -1.43 | – | -4.24 |
| 38 | `M78` Alvarez Pecahan Mingguan DTAYS | **47.5** | 20 | 21 | 38 | 15 | BELUM CUKUP | 2 | 73/43 | -2.92 | 23 | -8.70 | -0.78 | 7.6 | -0.34 | – | -1.02 |
| 39 | `M144` Screw Bar | **47.3** | 49 | 44 | 38 | 15 | BELUM CUKUP | 7 | 10/7 | -0.72 | 22 | -0.67 | -0.22 | 1.3 | -0.14 | – | -0.27 |
| 40 | `M37` Weinstein Peringkat 2 | **47.3** | 28 | 49 | 21 | 18 | BELUM CUKUP | 3 | 7/0 | -1.64 | 18 | -1.00 | -0.45 | 0.8 | -0.94 | – | -0.94 |
| 41 | `M142` Pecahan volum dari dasar (底部放量 | **46.8** | 40 | 44 | 42 | 55 | BELUM CUKUP | 17 | 55/9 | -1.22 | 22 | +2.04 | +0.42 | 2.3 | -0.10 | – | -0.15 |
| 42 | `M132` Ascending Scallop (Bulkowski) | **46.6** | 32 | 50 | 48 | 55 | BELUM CUKUP | 17 | 94/41 | -2.56 | 24 | +0.94 | +0.19 | 2.4 | -0.22 | – | -1.40 |
| 43 | `M115` Bow Tie (Landry) | **46.6** | 37 | 39 | 49 | 44 | BELUM CUKUP | 12 | 37/27 | -1.88 | 24 | -3.27 | -0.37 | 4.9 | +0.19 | – | 0.96 |
| 44 | `N48X36` Inside day pecah → keluar sele | **46.6** | 41 | 34 | 39 | 70 | BELUM CUKUP | 11 | 325/234 | -0.59 | 11 | -4.60 | -0.55 | 5.1 | -1.22 | – | – |
| 45 | `M64` O'Neil Tiga Minggu Ketat | **46.6** | 27 | 22 | 25 | 15 | BELUM CUKUP | 3 | 3/3 | -12.60 | 24 | -3.76 | -0.84 | 2.8 | -1.26 | – | -14.58 |
| 46 | `M124` 'Last' Stochastic Technique (C | **46.5** | 34 | 47 | 51 | 55 | BELUM CUKUP | 24 | 410/266 | -2.05 | 24 | +0.30 | +0.05 | 2.9 | -0.45 | – | -1.08 |
| 47 | `N45X16` Undur EMA21 cerun positif → ke | **46.5** | 29 | 51 | 42 | 55 | BELUM CUKUP | 11 | 169/84 | -2.13 | 11 | +1.71 | +0.34 | 2.0 | -0.87 | – | – |
| 48 | `M117` Landry Pullback (high 2 bulan) | **46.2** | 51 | 32 | 53 | 29 | BELUM CUKUP | 20 | 156/23 | -0.43 | 24 | -6.52 | -0.71 | 5.0 | +0.49 | – | 0.47 |
| 49 | `M157` Consolidation Pivot Breakout ( | **46.1** | 37 | 40 | 31 | 15 | BELUM CUKUP | 6 | 8/3 | -1.80 | 21 | -1.34 | -0.46 | 1.7 | -0.65 | – | -1.59 |
| 50 | `M138` 直升机空中加油 (Helikopter isi minyak | **46.1** | 24 | 48 | 19 | 15 | BELUM CUKUP | 4 | 4/0 | -2.15 | 17 | -0.78 | -0.55 | 0.7 | -1.33 | – | -1.88 |
| 51 | `M21` Marius 3 Persediaan (Pecahan+J | **46.0** | 24 | 44 | 35 | 15 | BELUM CUKUP | 5 | 5/4 | -3.50 | 16 | -1.73 | -0.65 | 1.6 | -0.18 | – | -0.33 |
| 52 | `M41` FW Penyatuan Mingguan | **45.6** | 27 | 24 | 41 | 23 | BELUM CUKUP | 5 | 67/10 | -1.48 | 23 | -5.98 | -0.63 | 5.4 | +0.16 | – | 0.26 |
| 53 | `N203X36` Gap 2% lalu MA20 silang MA50 x | **45.6** | 17 | 39 | 16 | 50 | BELUM CUKUP | 4 | 12/0 | -2.82 | 4 | -2.97 | -0.83 | 2.3 | -1.66 | – | – |
| 54 | `M80` Radge Saluran Purata Bergerak  | **45.3** | 45 | 36 | 55 | 23 | BELUM CUKUP | 24 | 309/79 | -0.93 | 24 | -2.20 | -0.28 | 4.6 | +0.20 | – | 0.26 |
| 55 | `M08` SMA20 + SMA200 | **45.3** | 37 | 36 | 49 | 55 | BELUM CUKUP | 22 | 222/150 | -1.53 | 24 | -3.73 | -0.70 | 3.6 | -0.61 | – | -1.48 |
| 56 | `N28X16` ADX>25 + DI+ > DI- → keluar bi | **45.3** | 33 | 38 | 32 | 70 | BELUM CUKUP | 11 | 418/286 | -1.19 | 11 | -3.63 | -0.58 | 3.5 | -2.02 | – | – |
| 57 | `M143` 장대양봉 이후 눌림목 / 5일선 매매 (Undur ke | **45.2** | 32 | 54 | 32 | 48 | BELUM CUKUP | 15 | 29/3 | -1.73 | 23 | +0.93 | +0.24 | 1.8 | -0.95 | – | -8.07 |
| 58 | `N28X36` ADX>25 + DI+ > DI- → keluar se | **45.2** | 42 | 29 | 42 | 33 | BELUM CUKUP | 11 | 395/272 | -0.64 | 11 | -6.02 | -0.96 | 4.3 | -0.95 | – | – |
| 59 | `N36X36` Pocket pivot → keluar selepas  | **45.2** | 31 | 37 | 34 | 70 | BELUM CUKUP | 11 | 161/82 | -2.91 | 11 | -0.41 | -0.07 | 2.6 | -1.72 | – | – |
| 60 | `N201X36` MA20 silang MA50 atas MA50 x X | **45.2** | 17 | 37 | 10 | 50 | BELUM CUKUP | 4 | 23/2 | -2.12 | 4 | -2.68 | -0.99 | 1.7 | -6.62 | – | – |
| 61 | `M38` Darvas Kotak | **45.1** | 21 | 24 | 34 | 25 | BELUM CUKUP | 5 | 26/1 | -3.08 | 23 | -2.94 | -0.29 | 5.7 | +0.07 | – | 0.32 |
| 62 | `M15` Break & Retest + Henti ATR | **45.0** | 50 | 36 | 53 | 15 | BELUM CUKUP | 24 | 315/243 | -0.54 | 24 | -5.27 | -0.53 | 5.0 | -0.23 | – | -0.50 |
| 63 | `N19X13` Bawah jalur BB + RSI<30 → kelu | **45.0** | 30 | 31 | 25 | 48 | BELUM CUKUP | 7 | 105/0 | -1.32 | 11 | -3.65 | -0.74 | 2.8 | -0.79 | – | – |
| 64 | `M131` Ross Hook (Joe Ross) | **44.9** | 41 | 44 | 54 | 15 | BELUM CUKUP | 23 | 267/134 | -1.37 | 24 | -1.70 | -0.24 | 3.7 | -0.07 | – | -0.15 |
| 65 | `N37X36` Gap and go → keluar selepas DU | **44.9** | 26 | 34 | 31 | 60 | BELUM CUKUP | 8 | 84/29 | -3.11 | 11 | +0.09 | +0.02 | 3.0 | -1.52 | – | – |
| 66 | `M111` Sistem Volatiliti Wilder | **44.8** | 33 | 42 | 53 | 39 | BELUM CUKUP | 24 | 272/122 | -2.07 | 24 | +0.60 | +0.09 | 3.9 | -0.20 | – | -0.52 |
| 67 | `M88` O'Neil Shakeout +3 | **44.7** | 32 | 41 | 47 | 40 | BELUM CUKUP | 18 | 79/42 | -2.94 | 24 | -1.35 | -0.11 | 6.0 | -0.42 | – | -0.69 |
| 68 | `M18` EMA9/21 Pullback | **44.6** | 52 | 33 | 52 | 15 | BELUM CUKUP | 24 | 426/346 | -0.53 | 24 | -6.19 | -0.96 | 4.3 | -0.28 | – | -0.90 |
| 69 | `M32` Momentum Burst | **44.6** | 49 | 25 | 51 | 24 | BELUM CUKUP | 16 | 59/39 | -0.80 | 24 | -5.43 | -0.43 | 7.9 | +0.14 | – | 0.31 |
| 70 | `M121` High 2 bull flag (Brooks) | **44.6** | 16 | 17 | 21 | 15 | BELUM CUKUP | 4 | 6/3 | -9.32 | 20 | -5.51 | -0.77 | 4.5 | -1.69 | – | -17.47 |
| 71 | `M148` Natural Number Method | **44.5** | 33 | 47 | 39 | 49 | BELUM CUKUP | 24 | 228/203 | -2.69 | 24 | -0.33 | -0.05 | 3.2 | -1.82 | – | -6.24 |
| 72 | `N37X17` Gap and go → keluar bila adx14 | **44.5** | 26 | 32 | 30 | 52 | BELUM CUKUP | 8 | 84/31 | -3.30 | 11 | -0.44 | -0.08 | 3.1 | -1.71 | – | – |
| 73 | `N35X36` Pecah 52 minggu tinggi → kelua | **44.5** | 23 | 41 | 22 | 70 | BELUM CUKUP | 8 | 48/3 | -4.45 | 11 | +0.57 | +0.20 | 1.2 | -1.74 | – | – |
| 74 | `M02` MACD + SMA200 | **44.4** | 37 | 36 | 44 | 55 | BELUM CUKUP | 24 | 133/97 | -3.51 | 24 | +0.98 | +0.09 | 4.1 | -1.18 | – | -7.49 |
| 75 | `M102` Stockbee SLTB | **44.3** | 44 | 40 | 50 | 15 | BELUM CUKUP | 24 | 415/326 | -1.36 | 24 | -3.30 | -0.31 | 5.9 | -0.53 | – | -1.24 |
| 76 | `M153` Range Leader | **44.2** | 49 | 34 | 52 | 15 | BELUM CUKUP | 24 | 1365/1302 | -0.35 | 24 | -5.67 | -0.48 | 7.8 | -0.32 | – | -1.78 |
| 77 | `N42X36` Lonjakan volum 2x → keluar sel | **44.1** | 36 | 24 | 41 | 40 | BELUM CUKUP | 11 | 209/111 | -0.94 | 11 | -6.02 | -0.81 | 4.5 | -1.04 | – | – |
| 78 | `N75X14` RSI14 < 40 tanpa penapis → kel | **44.1** | 33 | 28 | 37 | 45 | BELUM CUKUP | 11 | 258/48 | -1.21 | 11 | -4.79 | -0.87 | 3.6 | -1.18 | – | – |
| 79 | `N25X16` Supertrend + EMA + ADX>23 → ke | **44.1** | 25 | 41 | 29 | 51 | BELUM CUKUP | 10 | 120/14 | -3.32 | 11 | -0.97 | -0.20 | 2.6 | -1.62 | – | – |
| 80 | `M87` IBD Tapak Menaik | **44.1** | 26 | 33 | 38 | 15 | BELUM CUKUP | 8 | 11/8 | -3.96 | 24 | -4.35 | -0.55 | 4.3 | -0.46 | – | -1.41 |
| 81 | `M150` Trend Bar Failure (Brooks) | **44.0** | 45 | 36 | 48 | 15 | BELUM CUKUP | 21 | 107/65 | -0.85 | 24 | -5.17 | -0.71 | 3.7 | -0.55 | – | -1.66 |
| 82 | `N68X36` Bullish engulfing + EMA21 → ke | **44.0** | 26 | 39 | 39 | 30 | BELUM CUKUP | 11 | 87/25 | -2.17 | 11 | -2.07 | -0.33 | 3.6 | -0.68 | – | – |
| 83 | `M116` 2/20 EMA Breakout (Landry) | **43.9** | 45 | 36 | 51 | 15 | BELUM CUKUP | 24 | 595/521 | -0.94 | 24 | -0.20 | -0.02 | 7.8 | -0.42 | – | -1.82 |
| 84 | `N08X36` tutup>EMA20 tidak terlalu jauh | **43.8** | 24 | 35 | 32 | 68 | BELUM CUKUP | 11 | 411/310 | -2.00 | 11 | -3.98 | -0.73 | 2.9 | -2.04 | – | – |
| 85 | `M30` BB Free Bar + Himpitan 50/2.5 | **43.7** | 37 | 34 | 54 | 21 | BELUM CUKUP | 20 | 229/92 | -1.59 | 24 | -0.35 | -0.04 | 5.2 | +0.10 | – | 0.19 |
| 86 | `M92` CCI-50 | **43.6** | 42 | 38 | 49 | 15 | BELUM CUKUP | 24 | 572/444 | -1.05 | 24 | -4.06 | -0.46 | 4.0 | -0.61 | – | -1.17 |
| 87 | `N43X36` Undur EMA8 + penapis MA50 → ke | **43.6** | 28 | 31 | 35 | 44 | BELUM CUKUP | 11 | 189/56 | -2.66 | 11 | -2.45 | -0.59 | 2.6 | -1.51 | – | – |
| 88 | `M68` Kell Base n' Break | **43.5** | 32 | 41 | 45 | 15 | BELUM CUKUP | 15 | 47/15 | -3.09 | 24 | -0.72 | -0.15 | 2.4 | -0.15 | – | -0.89 |
| 89 | `N37X16` Gap and go → keluar bila super | **43.5** | 23 | 29 | 29 | 38 | BELUM CUKUP | 8 | 84/27 | -3.55 | 11 | -1.27 | -0.31 | 2.6 | -1.75 | – | – |
| 90 | `N64X36` Episodic pivot → keluar selepa | **43.5** | 21 | 26 | 32 | 48 | BELUM CUKUP | 8 | 50/8 | -2.03 | 11 | -2.03 | -0.41 | 2.9 | -0.91 | – | – |
| 91 | `N65X36` Gap 4% + volum + hampir 52w →  | **43.4** | 20 | 19 | 24 | 30 | BELUM CUKUP | 6 | 31/3 | -3.91 | 11 | -3.79 | -0.77 | 3.0 | -1.43 | – | – |
| 92 | `M26` Garis Trend Undur 3 Sentuhan + | **43.3** | 40 | 37 | 46 | 15 | BELUM CUKUP | 20 | 77/52 | -0.94 | 24 | -3.83 | -0.47 | 4.1 | -0.70 | – | -0.89 |
| 93 | `N64X17` Episodic pivot → keluar bila a | **43.3** | 22 | 25 | 32 | 41 | BELUM CUKUP | 8 | 50/13 | -2.71 | 11 | -2.31 | -0.46 | 2.9 | -1.15 | – | – |
| 94 | `N40X16` OBV tinggi baharu + MA50 → kel | **43.2** | 36 | 19 | 45 | 30 | BELUM CUKUP | 11 | 94/36 | -0.83 | 11 | -9.58 | -0.82 | 5.3 | -0.10 | – | – |
| 95 | `N65X14` Gap 4% + volum + hampir 52w →  | **43.2** | 20 | 18 | 22 | 30 | BELUM CUKUP | 6 | 31/1 | -3.84 | 11 | -3.93 | -0.80 | 2.9 | -1.42 | – | – |
| 96 | `M89` Chande 65sma-3cc | **43.1** | 34 | 42 | 50 | 16 | BELUM CUKUP | 23 | 194/107 | -2.61 | 24 | -0.80 | -0.09 | 4.2 | -0.52 | – | -1.58 |
| 97 | `M54` IBD Power Trend | **43.1** | 35 | 42 | 49 | 16 | BELUM CUKUP | 22 | 217/119 | -1.96 | 24 | -0.44 | -0.04 | 5.5 | -0.60 | – | -1.15 |
| 98 | `N36X16` Pocket pivot → keluar bila sup | **43.1** | 27 | 28 | 34 | 43 | BELUM CUKUP | 11 | 163/74 | -3.13 | 11 | -2.32 | -0.44 | 2.5 | -1.68 | – | – |
| 99 | `N25X17` Supertrend + EMA + ADX>23 → ke | **43.1** | 23 | 35 | 29 | 40 | BELUM CUKUP | 10 | 116/14 | -3.44 | 11 | -2.06 | -0.43 | 2.7 | -1.64 | – | – |
| 100 | `N51X16` BB squeeze + Supertrend → kelu | **43.1** | 17 | 35 | 20 | 30 | BELUM CUKUP | 7 | 12/2 | -3.61 | 11 | -4.04 | -0.75 | 3.0 | -1.80 | – | – |
| 101 | `M91` Stochastic Pop (Bernstein/Stec | **43.0** | 30 | 25 | 47 | 54 | BELUM CUKUP | 15 | 38/27 | -4.21 | 24 | -3.08 | -0.20 | 5.6 | -0.18 | – | -0.84 |
| 102 | `N41X36` CMF20>0 + tutup>EMA20 → keluar | **43.0** | 25 | 32 | 33 | 43 | BELUM CUKUP | 11 | 252/180 | -2.31 | 11 | -5.24 | -0.86 | 3.2 | -1.91 | – | – |
| 103 | `N06X36` Golden cross MA50/MA200 → kelu | **43.0** | 24 | 38 | 28 | 30 | BELUM CUKUP | 10 | 26/4 | -1.81 | 11 | -3.44 | -0.70 | 3.1 | -1.33 | – | – |
| 104 | `M44` Tapak Rata IBD | **43.0** | 28 | 36 | 18 | 15 | BELUM CUKUP | 8 | 9/7 | -5.15 | 24 | -4.55 | -0.86 | 3.2 | -2.72 | – | -34.16 |
| 105 | `M127` Slingshot Bullish | **42.8** | 32 | 42 | 44 | 15 | BELUM CUKUP | 19 | 108/84 | -1.82 | 24 | -3.91 | -0.50 | 3.8 | -1.04 | – | -1.16 |
| 106 | `M120` Reversal New Highs | **42.8** | 31 | 34 | 41 | 15 | BELUM CUKUP | 13 | 19/12 | -2.09 | 24 | -3.24 | -0.49 | 3.4 | -0.49 | – | -2.65 |
| 107 | `N40X36` OBV tinggi baharu + MA50 → kel | **42.8** | 32 | 19 | 44 | 30 | BELUM CUKUP | 11 | 77/23 | -1.28 | 11 | -9.21 | -0.74 | 5.7 | -0.07 | – | – |
| 108 | `N51X36` BB squeeze + Supertrend → kelu | **42.8** | 16 | 32 | 20 | 30 | BELUM CUKUP | 7 | 12/3 | -3.81 | 11 | -4.35 | -0.85 | 2.9 | -2.01 | – | – |
| 109 | `N42X16` Lonjakan volum 2x → keluar bil | **42.7** | 33 | 19 | 41 | 30 | BELUM CUKUP | 11 | 213/106 | -1.01 | 11 | -7.40 | -1.00 | 4.9 | -1.00 | – | – |
| 110 | `N80X36` Tinggi sepanjang masa → keluar | **42.7** | 20 | 26 | 27 | 30 | BELUM CUKUP | 8 | 40/3 | -4.30 | 11 | -1.96 | -0.49 | 2.3 | -1.26 | – | – |
| 111 | `M130` 多方炮 (dua lilin hijau mengapit  | **42.5** | 26 | 19 | 33 | 15 | BELUM CUKUP | 8 | 12/3 | -4.81 | 22 | -5.49 | -0.62 | 4.2 | -0.52 | – | -0.45 |
| 112 | `M128` Inventory Retracement Bar (IRB | **42.4** | 40 | 30 | 52 | 15 | BELUM CUKUP | 22 | 157/100 | -1.11 | 24 | -5.00 | -0.45 | 6.9 | -0.25 | – | -1.07 |
| 113 | `N07X16` Tiga MA tersusun → keluar bila | **42.4** | 22 | 33 | 34 | 30 | BELUM CUKUP | 11 | 159/39 | -2.64 | 11 | -2.38 | -0.59 | 2.2 | -1.42 | – | – |
| 114 | `N42X15` Lonjakan volum 2x → ekori Chan | **42.4** | 24 | 30 | 25 | 68 | BELUM CUKUP | 11 | 177/0 | -2.00 | 11 | -3.95 | -0.34 | 5.7 | -0.98 | – | – |
| 115 | `N22X36` BB pecah atas + RSI → keluar s | **42.4** | 22 | 27 | 42 | 30 | BELUM CUKUP | 11 | 119/60 | -3.69 | 11 | -5.54 | -0.74 | 3.6 | -0.72 | – | – |
| 116 | `N113X16` 80-20 bar (sisi beli) → keluar | **42.3** | 35 | 16 | 39 | 30 | BELUM CUKUP | 11 | 330/248 | -0.59 | 11 | -9.83 | -0.93 | 7.9 | -1.24 | – | – |
| 117 | `M12` Parabolic SAR | **42.2** | 33 | 39 | 49 | 17 | BELUM CUKUP | 24 | 391/236 | -2.35 | 24 | -1.87 | -0.32 | 3.0 | -0.69 | – | -1.44 |
| 118 | `N113X36` 80-20 bar (sisi beli) → keluar | **42.2** | 29 | 21 | 37 | 30 | BELUM CUKUP | 11 | 313/244 | -1.04 | 11 | -8.93 | -0.90 | 7.1 | -1.51 | – | – |
| 119 | `N64X16` Episodic pivot → keluar bila s | **42.2** | 19 | 20 | 32 | 30 | BELUM CUKUP | 8 | 50/8 | -2.27 | 11 | -3.10 | -0.77 | 2.4 | -0.97 | – | – |
| 120 | `N64X14` Episodic pivot → keluar bila r | **42.2** | 20 | 20 | 29 | 30 | BELUM CUKUP | 8 | 50/3 | -2.38 | 11 | -3.10 | -0.77 | 2.4 | -0.94 | – | – |
| 121 | `N66X36` 52w tinggi + pengesahan 1% → k | **42.2** | 19 | 14 | 25 | 30 | BELUM CUKUP | 7 | 38/2 | -3.72 | 10 | -4.91 | -0.92 | 3.6 | -1.23 | – | – |
| 122 | `M139` 均线首次粘合向上发散 (MA berhimpun kali  | **42.1** | 28 | 39 | 46 | 31 | BELUM CUKUP | 23 | 91/38 | -3.58 | 24 | -0.70 | -0.08 | 4.0 | -0.62 | – | -2.02 |
| 123 | `N76X16` Tutup > MA50 (penapis trend tu | **42.1** | 20 | 31 | 28 | 70 | BELUM CUKUP | 11 | 322/210 | -2.69 | 11 | -2.53 | -0.73 | 1.8 | -2.55 | – | – |
| 124 | `N124X36` Episodic pivot gap 8-10% → kel | **42.1** | 24 | 18 | 34 | 30 | BELUM CUKUP | 9 | 42/14 | -1.43 | 11 | -7.75 | -1.00 | 4.4 | -0.99 | – | – |
| 125 | `M126` Hidden Smash Day (beli, Larry  | **42.0** | 23 | 33 | 36 | 15 | BELUM CUKUP | 11 | 20/10 | -2.75 | 23 | -4.12 | -0.56 | 4.7 | -0.65 | – | -0.91 |
| 126 | `N76X36` Tutup > MA50 (penapis trend tu | **42.0** | 24 | 25 | 35 | 30 | BELUM CUKUP | 11 | 185/106 | -2.97 | 11 | -7.36 | -1.00 | 4.4 | -1.73 | – | – |
| 127 | `M106` DMI Wilder | **41.9** | 34 | 33 | 49 | 15 | BELUM CUKUP | 21 | 133/101 | -1.76 | 24 | -3.20 | -0.71 | 2.7 | -0.58 | – | -1.30 |
| 128 | `N53X17` Supertrend + ADX>25 → keluar b | **41.9** | 22 | 29 | 33 | 30 | BELUM CUKUP | 11 | 110/7 | -3.19 | 11 | -3.83 | -0.54 | 4.9 | -0.96 | – | – |
| 129 | `N53X16` Supertrend + ADX>25 → keluar b | **41.9** | 21 | 29 | 35 | 30 | BELUM CUKUP | 11 | 118/15 | -2.94 | 11 | -4.45 | -0.56 | 5.2 | -0.98 | – | – |
| 130 | `N24X36` Supertrend(10,3) + ADX>20 → ke | **41.8** | 26 | 19 | 38 | 34 | BELUM CUKUP | 11 | 167/78 | -2.40 | 11 | -4.94 | -1.00 | 3.0 | -1.24 | – | – |
| 131 | `N08X16` tutup>EMA20 tidak terlalu jauh | **41.8** | 20 | 28 | 30 | 46 | BELUM CUKUP | 11 | 481/350 | -2.09 | 11 | -3.96 | -0.96 | 2.5 | -2.31 | – | – |
| 132 | `N45X36` Undur EMA21 cerun positif → ke | **41.8** | 22 | 27 | 35 | 30 | BELUM CUKUP | 11 | 136/67 | -3.35 | 11 | -3.62 | -0.65 | 2.5 | -1.59 | – | – |
| 133 | `M134` First Kiss After Daylight (Lan | **41.7** | 28 | 37 | 49 | 15 | BELUM CUKUP | 19 | 63/27 | -2.13 | 24 | -3.86 | -0.46 | 4.6 | -0.07 | – | -0.08 |
| 134 | `N09X36` Undur EMA10 + penapis EMA50 →  | **41.7** | 24 | 23 | 35 | 30 | BELUM CUKUP | 11 | 199/73 | -2.84 | 11 | -4.62 | -1.00 | 2.9 | -1.62 | – | – |
| 135 | `N42X14` Lonjakan volum 2x → keluar bil | **41.7** | 22 | 22 | 35 | 46 | BELUM CUKUP | 11 | 192/16 | -1.96 | 11 | -5.80 | -0.52 | 5.8 | -1.01 | – | – |
| 136 | `N33X16` Donchian20 + penapis MA200 → k | **41.7** | 22 | 24 | 24 | 55 | BELUM CUKUP | 10 | 104/20 | -4.98 | 11 | -2.70 | -0.76 | 1.9 | -2.34 | – | – |
| 137 | `M119` 180 Bullish (Cooper) | **41.6** | 34 | 33 | 47 | 15 | BELUM CUKUP | 21 | 163/80 | -1.61 | 24 | -4.93 | -0.46 | 5.5 | -0.75 | – | -2.01 |
| 138 | `N74X16` MACD atas garis isyarat (keada | **41.5** | 18 | 27 | 31 | 50 | BELUM CUKUP | 11 | 616/467 | -1.86 | 11 | -5.96 | -0.81 | 5.1 | -2.16 | – | – |
| 139 | `N07X36` Tiga MA tersusun → keluar sele | **41.5** | 20 | 27 | 32 | 30 | BELUM CUKUP | 11 | 159/28 | -2.98 | 11 | -4.10 | -0.74 | 3.1 | -1.50 | – | – |
| 140 | `M105` Supertrend tulen | **41.4** | 30 | 36 | 53 | 15 | BELUM CUKUP | 23 | 373/156 | -2.13 | 24 | -1.58 | -0.16 | 4.7 | -0.18 | – | -0.53 |
| 141 | `M149` 3-Step Pullback | **41.4** | 31 | 33 | 53 | 15 | BELUM CUKUP | 22 | 225/75 | -1.86 | 24 | -3.05 | -0.28 | 6.1 | -0.01 | – | -0.01 |
| 142 | `M34` Carter TTM Squeeze | **41.4** | 35 | 30 | 49 | 15 | BELUM CUKUP | 22 | 106/51 | -1.57 | 24 | -3.06 | -0.34 | 4.7 | -0.29 | – | -0.77 |
| 143 | `M67` Rayner Teo: Ujian Ketiga pada  | **41.4** | 32 | 31 | 39 | 15 | BELUM CUKUP | 16 | 31/22 | -3.17 | 24 | -5.72 | -0.52 | 6.7 | -1.03 | – | -4.20 |
| 144 | `N41X16` CMF20>0 + tutup>EMA20 → keluar | **41.4** | 20 | 30 | 29 | 30 | BELUM CUKUP | 11 | 301/202 | -2.86 | 11 | -3.91 | -0.67 | 2.7 | -2.44 | – | – |
| 145 | `N75X13` RSI14 < 40 tanpa penapis → kel | **41.4** | 21 | 30 | 27 | 30 | BELUM CUKUP | 11 | 149/1 | -2.04 | 11 | -4.82 | -0.79 | 3.1 | -1.03 | – | – |
| 146 | `N38X36` VCP pecah → keluar selepas DUA | **41.3** | 23 | 31 | 20 | 30 | BELUM CUKUP | 11 | 35/14 | -3.04 | 11 | -3.67 | -0.96 | 2.4 | -2.63 | – | – |
| 147 | `N75X15` RSI14 < 40 tanpa penapis → eko | **41.3** | 22 | 30 | 25 | 30 | BELUM CUKUP | 11 | 147/0 | -2.01 | 11 | -4.82 | -0.79 | 3.1 | -1.00 | – | – |
| 148 | `M49` Ichimoku (Tutup Atas Awan + Te | **41.2** | 32 | 37 | 45 | 15 | BELUM CUKUP | 24 | 314/196 | -2.23 | 24 | -2.46 | -0.35 | 3.8 | -1.09 | – | -1.43 |
| 149 | `M06` Minervini VCP Breakout | **41.2** | 30 | 38 | 44 | 15 | BELUM CUKUP | 22 | 88/47 | -3.33 | 24 | -1.36 | -0.21 | 3.3 | -0.93 | – | -2.42 |
| 150 | `N68X16` Bullish engulfing + EMA21 → ke | **41.2** | 16 | 29 | 36 | 30 | BELUM CUKUP | 11 | 86/26 | -2.79 | 11 | -5.69 | -0.58 | 5.1 | -1.03 | – | – |
| 151 | `N124X15` Episodic pivot gap 8-10% → eko | **41.2** | 17 | 21 | 25 | 36 | BELUM CUKUP | 9 | 42/0 | -2.23 | 11 | -3.69 | -0.53 | 4.3 | -0.89 | – | – |
| 152 | `N57X36` ADX bangkit daripada <20 → kel | **41.1** | 18 | 23 | 21 | 30 | BELUM CUKUP | 9 | 75/11 | -5.38 | 11 | -2.88 | -0.56 | 3.0 | -2.39 | – | – |
| 153 | `N37X14` Gap and go → keluar bila rsi14 | **41.1** | 16 | 16 | 25 | 30 | BELUM CUKUP | 8 | 83/9 | -4.73 | 11 | -5.84 | -0.79 | 4.1 | -1.85 | – | – |
| 154 | `N33X14` Donchian20 + penapis MA200 → k | **41.0** | 21 | 24 | 23 | 30 | BELUM CUKUP | 10 | 112/9 | -5.40 | 11 | -2.82 | -0.59 | 2.9 | -2.15 | – | – |
| 155 | `N73X13` Tutup bawah jalur bawah BB(20, | **40.9** | 19 | 29 | 27 | 30 | BELUM CUKUP | 11 | 167/1 | -2.06 | 11 | -5.03 | -0.68 | 4.5 | -1.10 | – | – |
| 156 | `N36X14` Pocket pivot → keluar bila rsi | **40.9** | 22 | 17 | 30 | 58 | BELUM CUKUP | 11 | 160/29 | -4.30 | 11 | -5.42 | -0.73 | 4.1 | -1.84 | – | – |
| 157 | `N33X36` Donchian20 + penapis MA200 → k | **40.9** | 20 | 19 | 28 | 30 | BELUM CUKUP | 10 | 100/36 | -4.18 | 11 | -5.52 | -1.00 | 2.9 | -2.05 | – | – |
| 158 | `N50X14` Mampat + pecah volum 1.5x → ke | **40.9** | 12 | 18 | 26 | 30 | BELUM CUKUP | 8 | 19/4 | -5.66 | 11 | -7.61 | -0.82 | 5.2 | -1.36 | – | – |
| 159 | `M140` 猎豹出击 (Serangan Cheetah) | **40.8** | 19 | 27 | 34 | 15 | BELUM CUKUP | 11 | 42/19 | -2.73 | 24 | -5.99 | -0.68 | 4.2 | -1.37 | – | -1.43 |
| 160 | `M50` Elder Triple Screen | **40.5** | 36 | 27 | 48 | 15 | BELUM CUKUP | 24 | 609/419 | -1.30 | 24 | -8.85 | -0.80 | 6.9 | -0.71 | – | -1.11 |
| 161 | `M28` VWAP Separator + Kiss Pivot | **40.5** | 33 | 30 | 44 | 15 | BELUM CUKUP | 22 | 128/105 | -1.51 | 24 | -6.97 | -0.82 | 5.7 | -1.21 | – | -9.79 |
| 162 | `N56X17` RSI>50 + ADX>20 → keluar bila  | **40.5** | 20 | 20 | 28 | 39 | BELUM CUKUP | 11 | 141/47 | -4.43 | 11 | -3.74 | -0.75 | 3.0 | -2.24 | – | – |
| 163 | `N57X16` ADX bangkit daripada <20 → kel | **40.5** | 18 | 23 | 23 | 30 | BELUM CUKUP | 10 | 73/17 | -5.28 | 11 | -2.99 | -0.57 | 3.0 | -2.42 | – | – |
| 164 | `N22X16` BB pecah atas + RSI → keluar b | **40.4** | 17 | 19 | 37 | 30 | BELUM CUKUP | 11 | 121/37 | -4.84 | 11 | -5.58 | -0.83 | 3.6 | -1.05 | – | – |
| 165 | `M29` EMA3 + RSI75 + Stokastik | **40.3** | 27 | 27 | 40 | 15 | BELUM CUKUP | 16 | 37/31 | -2.55 | 24 | -8.95 | -0.71 | 7.8 | -1.01 | – | -5.30 |
| 166 | `N27X16` Ichimoku atas awan → keluar bi | **40.3** | 18 | 23 | 29 | 30 | BELUM CUKUP | 11 | 172/90 | -2.50 | 11 | -5.26 | -1.00 | 2.8 | -2.39 | – | – |
| 167 | `N119X13` 3 tutup turun berturut → kelua | **40.3** | 14 | 20 | 34 | 63 | BELUM CUKUP | 11 | 250/56 | -1.78 | 11 | -8.60 | -1.00 | 6.3 | -1.65 | – | – |
| 168 | `N56X36` RSI>50 + ADX>20 → keluar selep | **40.3** | 19 | 20 | 31 | 30 | BELUM CUKUP | 11 | 201/107 | -2.56 | 11 | -7.83 | -1.00 | 5.8 | -2.16 | – | – |
| 169 | `N24X17` Supertrend(10,3) + ADX>20 → ke | **40.3** | 18 | 18 | 26 | 30 | BELUM CUKUP | 10 | 126/37 | -4.65 | 11 | -4.26 | -0.84 | 2.9 | -2.30 | – | – |
| 170 | `M135` 3rd Watch | **40.3** | 17 | 16 | 29 | 15 | BELUM CUKUP | 9 | 15/6 | -9.52 | 24 | -6.01 | -0.76 | 4.3 | -1.47 | – | -8.62 |
| 171 | `M156` Single Penetration (DiNapoli) | **40.2** | 33 | 29 | 46 | 15 | BELUM CUKUP | 24 | 260/184 | -1.52 | 24 | -4.75 | -0.37 | 7.2 | -0.99 | – | -2.98 |
| 172 | `M04` BB Squeeze Breakout | **40.1** | 28 | 28 | 52 | 15 | BELUM CUKUP | 21 | 155/68 | -2.99 | 24 | -2.08 | -0.23 | 4.7 | -0.12 | – | -0.20 |
| 173 | `N56X16` RSI>50 + ADX>20 → keluar bila  | **40.1** | 16 | 22 | 32 | 30 | BELUM CUKUP | 11 | 224/116 | -2.58 | 11 | -5.70 | -0.90 | 4.1 | -2.05 | – | – |
| 174 | `N50X17` Mampat + pecah volum 1.5x → ke | **40.1** | 9 | 15 | 26 | 30 | BELUM CUKUP | 8 | 18/3 | -6.28 | 11 | -9.29 | -0.92 | 5.9 | -1.32 | – | – |
| 175 | `M14` Walking with the Whales | **39.9** | 36 | 25 | 47 | 15 | BELUM CUKUP | 24 | 1008/764 | -1.11 | 24 | -11.68 | -0.82 | 7.7 | -0.89 | – | -1.41 |
| 176 | `M36` Turtle 55/20 | **39.9** | 28 | 30 | 52 | 15 | BELUM CUKUP | 24 | 347/187 | -1.92 | 24 | -4.29 | -0.37 | 6.9 | -0.33 | – | -0.69 |
| 177 | `N28X14` ADX>25 + DI+ > DI- → keluar bi | **39.9** | 18 | 20 | 27 | 30 | BELUM CUKUP | 11 | 197/17 | -3.65 | 11 | -6.96 | -0.82 | 5.0 | -1.94 | – | – |
| 178 | `M99` Three Line Break | **39.8** | 30 | 29 | 48 | 15 | BELUM CUKUP | 23 | 166/116 | -3.39 | 24 | -4.15 | -0.45 | 4.4 | -0.77 | – | -2.80 |
| 179 | `N24X16` Supertrend(10,3) + ADX>20 → ke | **39.8** | 17 | 17 | 24 | 30 | BELUM CUKUP | 10 | 121/18 | -4.78 | 11 | -5.16 | -0.96 | 3.1 | -2.34 | – | – |
| 180 | `M136` Short/Intermediate-term Low (L | **39.7** | 27 | 33 | 48 | 15 | BELUM CUKUP | 24 | 811/347 | -2.79 | 24 | -4.38 | -0.63 | 3.2 | -0.79 | – | -0.43 |
| 181 | `N28X17` ADX>25 + DI+ > DI- → keluar bi | **39.6** | 17 | 22 | 22 | 30 | BELUM CUKUP | 11 | 134/3 | -3.74 | 11 | -5.57 | -0.78 | 4.7 | -1.94 | – | – |
| 182 | `M107` Golden Cross SMA50/200 | **39.5** | 25 | 32 | 43 | 15 | BELUM CUKUP | 21 | 46/10 | -1.93 | 24 | -5.45 | -0.68 | 3.0 | -0.35 | – | -0.51 |
| 183 | `N31X36` Turtle sistem 2 → keluar selep | **39.5** | 17 | 14 | 23 | 30 | BELUM CUKUP | 10 | 104/9 | -4.26 | 11 | -5.40 | -0.97 | 3.5 | -2.12 | – | – |
| 184 | `N39X36` NR7 kemudian pecah → keluar se | **39.5** | 5 | 9 | 16 | 30 | BELUM CUKUP | 7 | 31/10 | -6.61 | 10 | -12.19 | -0.94 | 6.1 | -2.84 | – | – |
| 185 | `N42X17` Lonjakan volum 2x → keluar bil | **39.4** | 16 | 14 | 39 | 30 | BELUM CUKUP | 11 | 207/64 | -1.90 | 11 | -9.42 | -0.97 | 6.5 | -1.07 | – | – |
| 186 | `N16X13` RSI2<10 tanpa penapis → keluar | **39.4** | 13 | 21 | 29 | 32 | BELUM CUKUP | 11 | 245/5 | -1.77 | 11 | -9.75 | -1.00 | 6.4 | -1.28 | – | – |
| 187 | `N54X16` Supertrend + RSI>50 → keluar b | **39.4** | 15 | 16 | 23 | 32 | BELUM CUKUP | 10 | 124/24 | -5.62 | 11 | -5.72 | -0.72 | 5.1 | -2.47 | – | – |
| 188 | `N119X15` 3 tutup turun berturut → ekori | **39.4** | 12 | 10 | 15 | 30 | BELUM CUKUP | 8 | 57/0 | -4.09 | 11 | -7.66 | -1.00 | 5.2 | -2.06 | – | – |
| 189 | `N54X36` Supertrend + RSI>50 → keluar s | **39.3** | 17 | 13 | 32 | 30 | BELUM CUKUP | 11 | 174/96 | -3.11 | 11 | -9.04 | -0.96 | 7.4 | -2.04 | – | – |
| 190 | `M59` Anjakan Julat RSI | **39.1** | 19 | 21 | 42 | 15 | BELUM CUKUP | 14 | 36/19 | -5.43 | 24 | -4.74 | -0.55 | 4.8 | -0.62 | – | -2.15 |
| 191 | `N22X14` BB pecah atas + RSI → keluar b | **39.1** | 16 | 15 | 29 | 30 | BELUM CUKUP | 11 | 126/21 | -5.44 | 11 | -7.53 | -0.93 | 4.9 | -1.80 | – | – |
| 192 | `N29X16` PSAR naik + tutup>MA50 → kelua | **39.0** | 15 | 16 | 27 | 30 | BELUM CUKUP | 11 | 211/110 | -4.27 | 11 | -6.89 | -0.86 | 5.7 | -2.68 | – | – |
| 193 | `N29X36` PSAR naik + tutup>MA50 → kelua | **39.0** | 16 | 16 | 25 | 30 | BELUM CUKUP | 11 | 158/87 | -4.15 | 11 | -10.32 | -0.97 | 8.7 | -2.78 | – | – |
| 194 | `M31` Band Walk (BB 20/2) | **38.9** | 32 | 20 | 53 | 15 | BELUM CUKUP | 23 | 401/125 | -1.61 | 24 | -4.40 | -0.37 | 7.8 | -0.13 | – | -0.22 |
| 195 | `M55` Guppy GMMA | **38.9** | 29 | 25 | 48 | 15 | BELUM CUKUP | 23 | 231/151 | -2.50 | 24 | -6.92 | -0.72 | 5.3 | -0.77 | – | -1.99 |
| 196 | `M57` Landry Trend Knockout (TKO) | **38.8** | 29 | 30 | 40 | 15 | BELUM CUKUP | 24 | 181/131 | -2.62 | 24 | -6.08 | -0.72 | 4.3 | -1.76 | – | -4.30 |
| 197 | `M95` Nisbah Kebaharuan High 52 Ming | **38.8** | 23 | 29 | 47 | 15 | BELUM CUKUP | 21 | 128/68 | -2.27 | 24 | -7.60 | -0.70 | 5.8 | -0.69 | – | -1.46 |
| 198 | `N27X36` Ichimoku atas awan → keluar se | **38.8** | 17 | 14 | 24 | 30 | BELUM CUKUP | 11 | 105/26 | -4.37 | 11 | -6.00 | -0.92 | 4.0 | -2.42 | – | – |
| 199 | `M73` ADX(5) > 40 + Julat Terkecil 6 | **38.7** | 31 | 24 | 47 | 15 | BELUM CUKUP | 24 | 1106/852 | -0.61 | 24 | -10.79 | -0.95 | 6.9 | -0.91 | – | -5.11 |
| 200 | `M141` First Thrust (Landry) | **38.6** | 4 | 10 | 30 | 15 | BELUM CUKUP | 8 | 26/16 | -7.72 | 24 | -14.85 | -0.93 | 5.7 | -1.65 | – | -5.98 |
| 201 | `N55X13` BB + RSI + ADX>20 → keluar bil | **38.4** | 13 | 20 | 18 | 30 | BELUM CUKUP | 11 | 90/0 | -2.88 | 11 | -6.46 | -0.98 | 4.1 | -1.87 | – | – |
| 202 | `M152` Spike & Ledge | **38.3** | 21 | 32 | 40 | 15 | BELUM CUKUP | 21 | 52/10 | -3.98 | 24 | -3.99 | -0.46 | 3.7 | -0.70 | – | -1.98 |
| 203 | `M19` Sneaky Pivot (proksi harian) | **38.2** | 23 | 29 | 46 | 15 | BELUM CUKUP | 23 | 426/282 | -3.80 | 24 | -6.29 | -0.58 | 4.6 | -0.95 | – | -13.07 |
| 204 | `M66` IBD Undur Pertama ke Purata 50 | **38.1** | 26 | 24 | 47 | 15 | BELUM CUKUP | 23 | 253/170 | -2.32 | 24 | -6.37 | -0.55 | 7.3 | -0.86 | – | -2.07 |
| 205 | `M11` NR7 Breakout + Volume | **38.0** | 26 | 22 | 43 | 15 | BELUM CUKUP | 21 | 124/89 | -1.18 | 24 | -10.15 | -0.72 | 8.4 | -1.22 | – | -1.02 |
| 206 | `N47X16` NR7 + EMA9>EMA21 → keluar bila | **37.7** | 7 | 20 | 26 | 30 | BELUM CUKUP | 11 | 200/58 | -3.06 | 11 | -11.56 | -0.98 | 5.5 | -2.60 | – | – |
| 207 | `M125` 2-Bar Breakout | **37.6** | 24 | 26 | 45 | 15 | BELUM CUKUP | 24 | 1137/514 | -3.38 | 24 | -6.88 | -0.68 | 4.7 | -1.16 | – | -0.58 |
| 208 | `M155` Market Cycle Strategy | **37.5** | 24 | 24 | 45 | 15 | BELUM CUKUP | 24 | 753/426 | -2.96 | 24 | -6.48 | -0.69 | 4.8 | -1.08 | – | -2.24 |
| 209 | `M03` BB Break + Divergence RSI | **37.3** | 20 | 29 | 47 | 15 | BELUM CUKUP | 24 | 433/360 | -1.78 | 24 | -6.75 | -0.73 | 4.4 | -0.86 | – | -3.15 |
| 210 | `M147` Improved Three-Bar Pullback | **37.0** | 17 | 23 | 32 | 15 | BELUM CUKUP | 17 | 108/43 | -5.20 | 24 | -10.36 | -0.72 | 5.9 | -2.13 | – | -1.64 |
| 211 | `M101` Bulkowski: Tiga lembah menaik | **36.8** | 17 | 16 | 45 | 15 | BELUM CUKUP | 17 | 46/23 | -3.72 | 24 | -8.95 | -0.64 | 8.2 | -0.34 | – | -0.88 |
| 212 | `M154` HOLP (High of Low Period) | **36.7** | 18 | 17 | 40 | 15 | BELUM CUKUP | 17 | 90/36 | -4.19 | 24 | -11.26 | -0.87 | 7.8 | -1.19 | – | -4.89 |
| 213 | `N16X15` RSI2<10 tanpa penapis → ekori  | **36.7** | 6 | 15 | 22 | 30 | BELUM CUKUP | 11 | 229/0 | -2.10 | 11 | -12.14 | -1.00 | 8.7 | -1.38 | – | – |
| 214 | `M01` Bollinger Band + RSI | **36.6** | 33 | 12 | 42 | 15 | BELUM CUKUP | 21 | 117/25 | -1.07 | 24 | -9.49 | -0.88 | 5.3 | -0.79 | – | -2.90 |
| 215 | `N47X36` NR7 + EMA9>EMA21 → keluar sele | **36.0** | 2 | 15 | 23 | 30 | BELUM CUKUP | 10 | 181/47 | -3.86 | 11 | -14.98 | -0.93 | 7.9 | -3.03 | – | – |
| 216 | `M47` Holy Grail Raschke | **35.4** | 10 | 16 | 29 | 15 | BELUM CUKUP | 15 | 33/29 | -3.31 | 24 | -10.65 | -0.94 | 6.9 | -2.25 | – | -19.71 |
| 217 | `M123` CCI Correction (Lambert, Chart | **35.1** | 17 | 26 | 31 | 15 | BELUM CUKUP | 23 | 190/173 | -1.80 | 24 | -11.72 | -0.96 | 7.4 | -2.70 | – | -4.71 |
| 218 | `M79` Radge: 20% Flipper | **34.5** | 15 | 21 | 42 | 15 | BELUM CUKUP | 24 | 386/139 | -4.59 | 24 | -9.88 | -0.74 | 6.8 | -1.52 | – | -2.68 |
| 219 | `M09` Volumatic VIDYA Pivot Retest | **34.1** | 6 | 9 | 28 | 15 | BELUM CUKUP | 14 | 35/22 | -5.55 | 24 | -15.20 | -0.96 | 9.2 | -2.21 | – | -12.23 |
| 220 | `M122` Moving Momentum (ChartSchool) | **33.8** | 16 | 18 | 33 | 15 | BELUM CUKUP | 23 | 112/68 | -4.63 | 24 | -12.39 | -0.97 | 6.8 | -2.34 | – | -6.24 |
| 221 | `M76` Undercut & Rally pada Low Pent | **33.8** | 11 | 20 | 37 | 15 | BELUM CUKUP | 21 | 78/66 | -3.10 | 24 | -11.82 | -0.95 | 7.4 | -1.80 | – | -6.45 |
| 222 | `M82` Arthur Hill Rotasi Sasaran 10% | **33.5** | 19 | 11 | 47 | 15 | BELUM CUKUP | 24 | 596/247 | -2.31 | 24 | -8.55 | -0.46 | 10.4 | -0.90 | – | -3.23 |
| 223 | `M81` Bensdorp Long Trend High Momen | **33.2** | 3 | 4 | 40 | 15 | BELUM CUKUP | 13 | 431/167 | -5.45 | 24 | -22.15 | -0.96 | 15.1 | -1.46 | – | -4.24 |
| 224 | `M161` EMA 10/21 + Supertrend (10,3) | **32.6** | 16 | 10 | 49 | 15 | BELUM CUKUP | 24 | 498/272 | -1.49 | 24 | -17.74 | -0.91 | 10.5 | -0.64 | – | -1.32 |
| 225 | `M90` Pring KST | **31.8** | 9 | 14 | 42 | 15 | BELUM CUKUP | 23 | 90/50 | -3.71 | 24 | -13.35 | -0.72 | 12.2 | -1.10 | – | -4.39 |
| 226 | `M20` EMA10/15 Crossover + Sudut | **30.0**⌈ | 34 | 34 | 43 | 15 | GAGAL | 24 | 495/436 | -1.61 | 24 | -5.47 | -0.73 | 3.7 | -1.32 | – | -7.97 |

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

