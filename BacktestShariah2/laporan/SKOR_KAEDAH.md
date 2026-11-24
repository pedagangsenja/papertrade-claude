# Skor Kaedah 0–100 (pangkat maklumat, BUKAN keputusan)

> **Status keputusan (kad skor, harga 2026-11-23):** TERBUKTI 0 · CALON 0 · BELUM CUKUP 226 · GAGAL 1 · NEGATIF 0. Rejim QQQ OFF sejak 2026-10-16. Hanya **TERBUKTI** layak untuk wang sebenar (`laporan/KAD_SKOR.md`); nombor dalam laporan ini BUKAN keputusan dan tidak boleh dibaca sebagai pangkat untuk wang sebenar.

Dijana 2026-11-24 oleh `standard/skor_kaedah.py` (Actions `analisis.yml`, selepas kad skor). Harga pada tutup 2026-11-23; 227 kaedah; 27 hari beli langsung (rejim ON 1, OFF 26). Pradaftar 2026-11-09: `standard/SPEC_SKOR_KAEDAH.md` (berat dan sauh dikunci `ujian/test_skor_kaedah.py::TestKunci`). Rekod analisis sahaja: tiada order, tiada wang sebenar.

## Cara membaca

- **Skor** = min geometri berberat empat tiang (Untung 35 · Tahan 30 · Bukti 25 · Konsisten 10), dikecut ke 50 mengikut data: berat data = hari beli ÷ (hari beli + 20). Kaedah dengan 2 hari beli tidak boleh menjauhi 50. 100 = unggul semua segi; 50 = neutral/tiada bukti; < 50 = lebih buruk daripada neutral.
- **Siling** ikut kad skor: NEGATIF ≤ 20, GANTUNG/BERSARA ≤ 30, GAGAL ≤ 40. Tanda ⌈ = siling terpakai.
- **Satu-satunya status yang membenarkan wang sebenar ialah TERBUKTI dalam `laporan/KAD_SKOR.md`.** Skor tinggi dengan status BELUM CUKUP bermaksud "paling menjanjikan setakat ini", bukan "selamat".
- Deflasi ujian berganda (López de Prado): sauh t Bukti C1 = maks(2.0, E[maks 227 normal]) = 2.81.
- **Semakan kebolehramalan:** skor pada 2026-11-16 lawan pulangan lorong T4 sejak itu, 226 kaedah: Spearman ρ = +0.092 (p = 0.166). Belum ada bukti skor meramal pangkat; jangan pilih kaedah dengannya.
- Metrik T4 (A2, B1, B2, D1) dikira atas lorong T4 L1 **dipotong pada sesi LANGSUNG pertama** kaedah itu (Mxx 2026-10-16, Nxx/GB 2026-11-03) dan diasas semula; sesi isian bina semula tidak dikira (pindaan 9 Nov 2026 (a)). Lajur "T4 sesi/pul" di bawah ialah potongan itu, bukan lorong penuh `T4_KAEDAH.md`.

## Semua kaedah, susun ikut Skor

| # | Kaedah | Skor | Untung | Tahan | Bukti | Konsisten | Status kad | Hari beli | Posisi/tutup | Jangkaan % | T4 sesi | T4 pul % | T4 pul/|MDD| | Ulcer | t buku | Lift | WFE |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `M146` 3-Bar Momentum Pattern | **57.7** | 65 | 65 | 57 | 95 | BELUM CUKUP | 20 | 80/47 | -0.17 | 27 | +4.47 | +0.64 | 3.2 | +0.69 | +2.60 | 1.38 |
| 2 | `M151` Outside Bar Failure | **55.3** | 54 | 77 | 52 | 54 | BELUM CUKUP | 24 | 116/79 | -1.16 | 27 | +5.75 | +1.44 | 1.2 | -0.16 | -0.30 | -0.32 |
| 3 | `M133` Bull Hook (Crabel) | **54.9** | 56 | 62 | 58 | 91 | BELUM CUKUP | 16 | 54/45 | -0.77 | 27 | +2.32 | +0.40 | 2.6 | +0.95 | +3.90 | 7.64 |
| 4 | `M159` Heikin-Ashi Trend | **52.5** | 52 | 65 | 47 | 54 | BELUM CUKUP | 27 | 1927/1871 | -0.91 | 27 | +5.08 | +0.83 | 3.5 | -0.98 | -0.37 | -6.00 |
| 5 | `M48` Cooper 1-2-3-4 | **52.2** | 47 | 61 | 52 | 70 | BELUM CUKUP | 22 | 71/27 | -1.30 | 27 | +8.50 | +1.48 | 2.5 | +0.29 | -1.18 | 0.63 |
| 6 | `N202X36` RSI2<10 dalam trend naik x X36 | **52.1** | 57 | 80 | 37 | 70 | BELUM CUKUP | 7 | 113/17 | -0.09 | 7 | +1.66 | +0.78 | 1.1 | -0.58 | – | – |
| 7 | `M25` VWAP Wave (proksi harian) | **51.9** | 52 | 58 | 56 | 40 | BELUM CUKUP | 25 | 201/173 | -1.21 | 27 | +3.19 | +0.40 | 4.0 | +0.13 | +1.13 | 0.68 |
| 8 | `M104` High Tight Flag / Power Play | **51.1** | 86 | 90 | 44 | 85 | BELUM CUKUP | 1 | 1/0 | +26.85 | 12 | +2.71 | +10.00 | 0.1 | +2.00 | – | 11.90 |
| 9 | `N204X36` Undur RSI2, gap 2%, RSI silang | **51.0** | 77 | 94 | 28 | 50 | BELUM CUKUP | 2 | 2/0 | +3.08 | 2 | +0.66 | +5.25 | 0.1 | – | – | – |
| 10 | `M118` Expansion Pivot (Cooper) | **51.0** | 44 | 56 | 53 | 72 | BELUM CUKUP | 20 | 85/46 | -1.54 | 27 | +4.23 | +0.51 | 3.1 | +0.16 | +0.52 | 0.52 |
| 11 | `M160` Measured Move Up | **51.0** | 36 | 59 | 59 | 88 | BELUM CUKUP | 25 | 134/110 | -2.23 | 27 | +1.98 | +0.34 | 2.6 | +0.55 | +0.69 | 3.70 |
| 12 | `M23` Breitstein Kapitulasi + Kesina | **50.2** | 48 | 48 | 57 | 48 | BELUM CUKUP | 23 | 130/106 | -1.12 | 27 | -1.72 | -0.26 | 3.3 | +0.35 | +0.66 | 1.24 |
| 13 | `M07` Qullamaggie Breakout | **49.3** | 33 | 64 | 27 | 15 | BELUM CUKUP | 1 | 1/1 | -2.53 | 27 | -0.25 | -0.21 | 0.9 | -0.22 | – | -1.12 |
| 14 | `M45` High 52 Minggu (George & Hwang | **49.1** | 23 | 43 | 30 | 36 | BELUM CUKUP | 1 | 2/1 | -4.22 | 16 | -0.82 | -0.45 | 0.9 | +0.14 | – | 0.32 |
| 15 | `M10` EMA3 + CCI + MACD | **49.0** | 38 | 58 | 50 | 56 | BELUM CUKUP | 22 | 127/77 | -2.81 | 27 | +9.77 | +1.48 | 2.7 | -0.34 | +0.41 | -0.97 |
| 16 | `M46` Jurang Naik Boleh Beli (Buyabl | **49.0** | 38 | 58 | 45 | 64 | BELUM CUKUP | 13 | 36/27 | -1.99 | 27 | +1.18 | +0.24 | 1.8 | -0.34 | +2.41 | -0.53 |
| 17 | `M137` Livermore System | **48.9** | 36 | 58 | 52 | 59 | BELUM CUKUP | 25 | 184/97 | -2.51 | 27 | +4.01 | +0.68 | 2.4 | -0.25 | +1.15 | -0.46 |
| 18 | `M51` O'Neil Cawan & Pemegang | **48.8** | 31 | 51 | 32 | 33 | BELUM CUKUP | 2 | 3/1 | -2.19 | 17 | -0.62 | -0.38 | 0.8 | +0.20 | – | 0.61 |
| 19 | `M84` Jarak purata bergerak MAD 21/2 | **48.6** | 23 | 13 | 34 | 15 | BELUM CUKUP | 1 | 58/43 | -4.25 | 16 | -7.69 | -0.87 | 7.0 | -0.70 | – | -1.64 |
| 20 | `M13` Garis Trend Action/Safety Line | **48.4** | 38 | 59 | 47 | 54 | BELUM CUKUP | 27 | 865/744 | -2.82 | 27 | +4.90 | +0.74 | 2.2 | -0.95 | -0.38 | -2.57 |
| 21 | `M27` Price Action 4 Tiang | **48.4** | 38 | 32 | 38 | 15 | BELUM CUKUP | 2 | 546/521 | -1.43 | 27 | -4.16 | -0.81 | 3.1 | -0.96 | – | -3.05 |
| 22 | `M74` Lulus Baharu Trend Template Mi | **48.3** | 50 | 54 | 52 | 19 | BELUM CUKUP | 27 | 110/82 | -1.39 | 27 | +0.68 | +0.09 | 3.4 | -0.24 | +0.10 | -0.40 |
| 23 | `M33` Supertrend + SMA10 | **48.2** | 34 | 55 | 54 | 58 | BELUM CUKUP | 23 | 224/126 | -2.80 | 27 | +5.31 | +0.73 | 2.7 | -0.05 | +0.67 | -0.24 |
| 24 | `M96` Momo India: Ranking Sharpe 3/6 | **48.2** | 19 | 7 | 9 | 15 | BELUM CUKUP | 1 | 6/6 | -13.71 | 16 | -8.21 | -1.00 | 7.2 | -5.92 | – | -15.55 |
| 25 | `M145` Yum-Yum Continuation | **48.0** | 34 | 57 | 51 | 59 | BELUM CUKUP | 24 | 312/109 | -2.86 | 27 | +2.62 | +0.68 | 1.6 | -0.42 | +1.11 | -0.36 |
| 26 | `M94` Pecutan Momentum (Chen, Yu & W | **47.8** | 0 | 5 | 15 | 15 | BELUM CUKUP | 1 | 33/0 | -13.34 | 16 | -16.61 | -0.76 | 10.8 | -1.41 | – | -4.12 |
| 27 | `M70` Pecahan Hari Dalam | **47.7** | 57 | 58 | 51 | 8 | BELUM CUKUP | 27 | 511/450 | -0.90 | 27 | +0.77 | +0.13 | 2.6 | -0.48 | -1.76 | -1.09 |
| 28 | `M78` Alvarez Pecahan Mingguan DTAYS | **47.5** | 20 | 20 | 38 | 15 | BELUM CUKUP | 2 | 73/47 | -3.39 | 26 | -8.85 | -0.79 | 8.1 | -0.47 | – | -1.36 |
| 29 | `N25X36` Supertrend + EMA + ADX>23 → ke | **47.4** | 34 | 52 | 40 | 70 | BELUM CUKUP | 13 | 142/57 | -2.57 | 14 | +0.77 | +0.17 | 2.0 | -0.95 | – | – |
| 30 | `M129` Wick Play | **47.3** | 36 | 44 | 43 | 55 | BELUM CUKUP | 10 | 25/13 | -2.74 | 27 | +1.50 | +0.26 | 2.1 | -0.16 | – | -0.55 |
| 31 | `M37` Weinstein Peringkat 2 | **47.1** | 22 | 50 | 25 | 15 | BELUM CUKUP | 3 | 7/1 | -2.47 | 21 | -1.61 | -0.32 | 1.6 | -0.77 | – | -1.07 |
| 32 | `M77` Undercut & Rally pada Purata B | **47.0** | 44 | 46 | 45 | 33 | BELUM CUKUP | 19 | 56/44 | -1.24 | 27 | -2.65 | -0.32 | 2.8 | -0.64 | +0.94 | -0.79 |
| 33 | `M05` MACD Divergence + Pengesahan | **47.0** | 40 | 48 | 40 | 50 | BELUM CUKUP | 16 | 42/16 | -3.05 | 27 | -0.10 | -0.01 | 2.6 | -0.78 | -1.21 | -1.38 |
| 34 | `M138` 直升机空中加油 (Helikopter isi minyak | **46.9** | 30 | 53 | 24 | 15 | BELUM CUKUP | 4 | 4/0 | -1.66 | 20 | -0.58 | -0.26 | 0.9 | -0.72 | – | -1.29 |
| 35 | `M64` O'Neil Tiga Minggu Ketat | **46.6** | 28 | 21 | 26 | 15 | BELUM CUKUP | 3 | 3/3 | -12.60 | 27 | -3.76 | -0.84 | 3.1 | -1.26 | – | -14.58 |
| 36 | `M21` Marius 3 Persediaan (Pecahan+J | **46.5** | 27 | 45 | 37 | 18 | BELUM CUKUP | 5 | 5/4 | -3.02 | 19 | -1.50 | -0.56 | 1.8 | +0.07 | – | 0.10 |
| 37 | `M158` Doubly Adaptive Profit Targets | **46.0** | 43 | 35 | 57 | 38 | BELUM CUKUP | 24 | 391/216 | -1.16 | 27 | -4.00 | -0.37 | 4.7 | +0.25 | +1.48 | 0.57 |
| 38 | `M39` Radge Pecahan Bollinger 100 ha | **46.0** | 32 | 49 | 48 | 54 | BELUM CUKUP | 23 | 244/67 | -4.20 | 27 | +3.11 | +0.48 | 2.2 | -0.64 | -0.23 | -1.25 |
| 39 | `N28X16` ADX>25 + DI+ > DI- → keluar bi | **46.0** | 34 | 47 | 36 | 62 | BELUM CUKUP | 14 | 531/428 | -1.45 | 14 | +0.19 | +0.02 | 3.9 | -1.74 | – | – |
| 40 | `M35` Pocket Pivot Morales & Kacher | **45.7** | 52 | 38 | 52 | 18 | BELUM CUKUP | 26 | 337/310 | -0.75 | 27 | -4.00 | -0.43 | 5.8 | -0.37 | +0.72 | -1.89 |
| 41 | `N53X36` Supertrend + ADX>25 → keluar s | **45.5** | 39 | 36 | 47 | 30 | BELUM CUKUP | 14 | 144/61 | -1.49 | 14 | -3.97 | -0.43 | 4.3 | -0.17 | – | – |
| 42 | `M100` Bulkowski Segi Empat & Segi Ti | **45.2** | 44 | 41 | 48 | 16 | BELUM CUKUP | 17 | 61/45 | -1.09 | 27 | -1.61 | -0.20 | 3.3 | -0.30 | – | -1.43 |
| 43 | `N28X36` ADX>25 + DI+ > DI- → keluar se | **44.9** | 38 | 36 | 42 | 30 | BELUM CUKUP | 14 | 500/388 | -0.95 | 14 | -4.89 | -0.37 | 5.9 | -0.97 | – | – |
| 44 | `M144` Screw Bar | **44.9** | 32 | 33 | 34 | 15 | BELUM CUKUP | 7 | 10/8 | -2.61 | 25 | -2.54 | -0.75 | 1.6 | -0.72 | – | -1.11 |
| 45 | `M157` Consolidation Pivot Breakout ( | **44.9** | 25 | 37 | 30 | 15 | BELUM CUKUP | 6 | 8/3 | -2.68 | 24 | -2.03 | -0.59 | 1.9 | -0.80 | – | -1.71 |
| 46 | `M87` IBD Tapak Menaik | **44.8** | 31 | 35 | 41 | 15 | BELUM CUKUP | 8 | 11/8 | -3.18 | 27 | -3.48 | -0.44 | 4.6 | -0.13 | – | -0.40 |
| 47 | `M93` Bollinger Kaedah II: %b + MFI | **44.6** | 42 | 37 | 54 | 22 | BELUM CUKUP | 25 | 273/119 | -1.37 | 27 | -1.47 | -0.15 | 4.1 | -0.03 | +1.86 | -0.04 |
| 48 | `M124` 'Last' Stochastic Technique (C | **44.4** | 33 | 42 | 50 | 41 | BELUM CUKUP | 26 | 415/335 | -2.81 | 27 | -0.72 | -0.08 | 3.8 | -0.61 | -0.32 | -1.59 |
| 49 | `M18` EMA9/21 Pullback | **44.3** | 45 | 35 | 51 | 22 | BELUM CUKUP | 27 | 480/433 | -0.92 | 27 | -7.39 | -0.74 | 5.0 | -0.41 | +1.73 | -1.35 |
| 50 | `M115` Bow Tie (Landry) | **44.3** | 34 | 36 | 48 | 14 | BELUM CUKUP | 12 | 37/30 | -2.46 | 27 | -4.23 | -0.44 | 5.4 | -0.04 | -0.25 | -0.21 |
| 51 | `M41` FW Penyatuan Mingguan | **44.3** | 22 | 23 | 41 | 18 | BELUM CUKUP | 6 | 68/13 | -1.90 | 26 | -6.78 | -0.58 | 6.3 | +0.06 | – | 0.09 |
| 52 | `M38` Darvas Kotak | **44.3** | 19 | 20 | 33 | 15 | BELUM CUKUP | 5 | 27/1 | -4.38 | 26 | -4.24 | -0.37 | 6.5 | -0.02 | – | -0.09 |
| 53 | `N203X36` Gap 2% lalu MA20 silang MA50 x | **44.3** | 12 | 33 | 25 | 30 | BELUM CUKUP | 5 | 13/3 | -5.37 | 7 | -6.69 | -0.64 | 5.7 | -1.31 | – | – |
| 54 | `M08` SMA20 + SMA200 | **44.0** | 33 | 37 | 50 | 46 | BELUM CUKUP | 25 | 268/215 | -1.84 | 27 | -3.42 | -0.64 | 3.7 | -0.60 | +0.56 | -1.42 |
| 55 | `N75X17` RSI14 < 40 tanpa penapis → kel | **44.0** | 33 | 38 | 38 | 30 | BELUM CUKUP | 14 | 559/278 | -1.20 | 14 | -4.01 | -0.31 | 5.4 | -1.46 | – | – |
| 56 | `N45X16` Undur EMA21 cerun positif → ke | **43.8** | 26 | 44 | 43 | 30 | BELUM CUKUP | 14 | 190/124 | -2.65 | 14 | +0.85 | +0.10 | 3.7 | -0.88 | – | – |
| 57 | `M153` Range Leader | **43.7** | 47 | 34 | 50 | 18 | BELUM CUKUP | 27 | 1447/1414 | -0.62 | 27 | -4.77 | -0.36 | 8.3 | -0.56 | +0.70 | -3.82 |
| 58 | `N65X36` Gap 4% + volum + hampir 52w →  | **43.7** | 21 | 19 | 26 | 30 | BELUM CUKUP | 6 | 31/6 | -4.62 | 14 | -4.98 | -0.65 | 3.9 | -1.39 | – | – |
| 59 | `N65X14` Gap 4% + volum + hampir 52w →  | **43.6** | 21 | 19 | 25 | 30 | BELUM CUKUP | 6 | 31/4 | -4.53 | 14 | -5.38 | -0.64 | 4.0 | -1.38 | – | – |
| 60 | `M121` High 2 bull flag (Brooks) | **43.6** | 18 | 17 | 22 | 15 | BELUM CUKUP | 5 | 8/3 | -7.07 | 23 | -5.54 | -0.72 | 4.9 | -1.66 | – | -15.67 |
| 61 | `M54` IBD Power Trend | **43.5** | 37 | 44 | 48 | 15 | BELUM CUKUP | 23 | 222/142 | -2.58 | 27 | +0.97 | +0.09 | 5.9 | -0.75 | -0.03 | -1.47 |
| 62 | `M132` Ascending Scallop (Bulkowski) | **43.5** | 33 | 43 | 48 | 14 | BELUM CUKUP | 18 | 96/52 | -3.26 | 27 | -0.21 | -0.03 | 3.2 | -0.36 | -0.52 | -2.31 |
| 63 | `N25X16` Supertrend + EMA + ADX>23 → ke | **43.1** | 25 | 40 | 36 | 37 | BELUM CUKUP | 13 | 125/48 | -4.44 | 14 | -1.00 | -0.21 | 2.7 | -1.42 | – | – |
| 64 | `M102` Stockbee SLTB | **43.0** | 40 | 38 | 49 | 15 | BELUM CUKUP | 27 | 448/360 | -1.65 | 27 | -3.42 | -0.29 | 6.5 | -0.67 | -0.09 | -1.55 |
| 65 | `M120` Reversal New Highs | **42.9** | 32 | 33 | 42 | 15 | BELUM CUKUP | 13 | 19/13 | -2.14 | 27 | -3.34 | -0.51 | 3.8 | -0.44 | – | -2.23 |
| 66 | `M131` Ross Hook (Joe Ross) | **42.8** | 32 | 42 | 52 | 17 | BELUM CUKUP | 24 | 273/156 | -1.99 | 27 | -2.18 | -0.25 | 4.4 | -0.27 | +0.50 | -0.60 |
| 67 | `M142` Pecahan volum dari dasar (底部放量 | **42.8** | 27 | 34 | 43 | 55 | BELUM CUKUP | 18 | 56/14 | -1.91 | 25 | +0.25 | +0.03 | 3.3 | -0.18 | – | -0.31 |
| 68 | `N201X36` MA20 silang MA50 atas MA50 x X | **42.8** | 14 | 35 | 20 | 30 | BELUM CUKUP | 7 | 26/7 | -3.92 | 7 | -5.15 | -0.69 | 4.0 | -2.19 | – | – |
| 69 | `M44` Tapak Rata IBD | **42.7** | 25 | 35 | 18 | 15 | BELUM CUKUP | 8 | 9/8 | -5.60 | 27 | -4.98 | -0.87 | 3.6 | -3.00 | – | -35.50 |
| 70 | `M15` Break & Retest + Henti ATR | **42.4** | 39 | 30 | 52 | 22 | BELUM CUKUP | 26 | 324/293 | -0.89 | 27 | -9.44 | -0.61 | 6.6 | -0.33 | +1.76 | -0.74 |
| 71 | `N64X17` Episodic pivot → keluar bila a | **42.4** | 21 | 24 | 33 | 30 | BELUM CUKUP | 9 | 52/17 | -3.46 | 14 | -3.19 | -0.39 | 3.9 | -1.20 | – | – |
| 72 | `N48X36` Inside day pecah → keluar sele | **42.3** | 32 | 24 | 40 | 38 | BELUM CUKUP | 14 | 342/265 | -0.99 | 14 | -7.29 | -0.84 | 5.8 | -1.25 | – | – |
| 73 | `N36X36` Pocket pivot → keluar selepas  | **42.3** | 27 | 29 | 35 | 48 | BELUM CUKUP | 14 | 176/113 | -3.63 | 14 | -3.03 | -0.32 | 4.2 | -1.78 | – | – |
| 74 | `N37X36` Gap and go → keluar selepas DU | **42.2** | 24 | 28 | 34 | 30 | BELUM CUKUP | 11 | 88/40 | -3.97 | 14 | -1.72 | -0.22 | 3.7 | -1.50 | – | – |
| 75 | `N64X36` Episodic pivot → keluar selepa | **42.2** | 20 | 23 | 34 | 30 | BELUM CUKUP | 9 | 52/15 | -3.44 | 14 | -3.68 | -0.42 | 4.1 | -1.01 | – | – |
| 76 | `M68` Kell Base n' Break | **42.1** | 29 | 39 | 44 | 12 | BELUM CUKUP | 16 | 52/18 | -3.73 | 27 | -1.66 | -0.21 | 3.2 | -0.35 | -0.89 | -1.97 |
| 77 | `N37X17` Gap and go → keluar bila adx14 | **42.1** | 24 | 28 | 33 | 30 | BELUM CUKUP | 11 | 88/37 | -3.81 | 14 | -1.75 | -0.20 | 4.0 | -1.59 | – | – |
| 78 | `M12` Parabolic SAR | **42.0** | 35 | 42 | 48 | 12 | BELUM CUKUP | 27 | 411/292 | -2.73 | 27 | -0.76 | -0.12 | 3.4 | -0.75 | -0.91 | -1.62 |
| 79 | `M117` Landry Pullback (high 2 bulan) | **42.0** | 31 | 30 | 52 | 29 | BELUM CUKUP | 21 | 162/42 | -1.66 | 27 | -7.21 | -0.61 | 5.8 | +0.14 | +2.40 | 0.15 |
| 80 | `N68X36` Bullish engulfing + EMA21 → ke | **42.0** | 20 | 35 | 40 | 30 | BELUM CUKUP | 13 | 131/45 | -2.50 | 14 | -3.48 | -0.39 | 4.9 | -0.82 | – | – |
| 81 | `N64X14` Episodic pivot → keluar bila r | **42.0** | 20 | 22 | 31 | 30 | BELUM CUKUP | 9 | 52/7 | -3.57 | 14 | -4.20 | -0.52 | 3.6 | -1.03 | – | – |
| 82 | `N64X16` Episodic pivot → keluar bila s | **42.0** | 18 | 22 | 35 | 30 | BELUM CUKUP | 9 | 52/22 | -3.17 | 14 | -4.25 | -0.54 | 3.5 | -0.98 | – | – |
| 83 | `N41X36` CMF20>0 + tutup>EMA20 → keluar | **41.8** | 23 | 32 | 37 | 30 | BELUM CUKUP | 13 | 274/229 | -2.73 | 14 | -5.75 | -0.67 | 4.5 | -1.60 | – | – |
| 84 | `M116` 2/20 EMA Breakout (Landry) | **41.7** | 39 | 32 | 49 | 15 | BELUM CUKUP | 27 | 617/556 | -1.23 | 27 | -1.67 | -0.12 | 8.3 | -0.67 | -0.08 | -3.18 |
| 85 | `M130` 多方炮 (dua lilin hijau mengapit  | **41.7** | 18 | 19 | 35 | 15 | BELUM CUKUP | 8 | 12/5 | -4.85 | 25 | -5.60 | -0.56 | 5.0 | -0.40 | – | -0.33 |
| 86 | `M150` Trend Bar Failure (Brooks) | **41.6** | 30 | 35 | 47 | 21 | BELUM CUKUP | 22 | 111/95 | -1.68 | 27 | -6.81 | -0.70 | 4.5 | -0.77 | +1.68 | -2.75 |
| 87 | `N37X16` Gap and go → keluar bila super | **41.6** | 21 | 26 | 34 | 30 | BELUM CUKUP | 11 | 88/48 | -4.09 | 14 | -2.64 | -0.37 | 3.3 | -1.51 | – | – |
| 88 | `N66X36` 52w tinggi + pengesahan 1% → k | **41.6** | 17 | 17 | 28 | 30 | BELUM CUKUP | 8 | 40/6 | -4.73 | 13 | -5.62 | -0.67 | 4.6 | -1.31 | – | – |
| 89 | `M88` O'Neil Shakeout +3 | **41.5** | 30 | 37 | 47 | 14 | BELUM CUKUP | 20 | 85/61 | -4.69 | 27 | -2.51 | -0.16 | 7.3 | -0.62 | -0.29 | -1.09 |
| 90 | `M127` Slingshot Bullish | **41.4** | 27 | 38 | 44 | 19 | BELUM CUKUP | 20 | 112/92 | -2.21 | 27 | -5.99 | -0.62 | 4.7 | -1.15 | +1.06 | -1.27 |
| 91 | `M32` Momentum Burst | **41.4** | 33 | 24 | 50 | 16 | BELUM CUKUP | 17 | 67/48 | -1.84 | 27 | -6.53 | -0.46 | 8.7 | -0.07 | +0.40 | -0.15 |
| 92 | `M67` Rayner Teo: Ujian Ketiga pada  | **41.3** | 33 | 31 | 41 | 15 | BELUM CUKUP | 18 | 34/27 | -2.93 | 27 | -5.34 | -0.45 | 7.3 | -0.90 | – | -3.46 |
| 93 | `N43X36` Undur EMA8 + penapis MA50 → ke | **41.3** | 24 | 28 | 37 | 30 | BELUM CUKUP | 14 | 218/106 | -3.47 | 14 | -4.63 | -0.63 | 3.7 | -1.55 | – | – |
| 94 | `N25X17` Supertrend + EMA + ADX>23 → ke | **41.3** | 22 | 32 | 33 | 30 | BELUM CUKUP | 13 | 121/27 | -4.54 | 14 | -2.92 | -0.40 | 3.5 | -1.46 | – | – |
| 95 | `M89` Chande 65sma-3cc | **41.2** | 33 | 37 | 49 | 12 | BELUM CUKUP | 24 | 197/152 | -3.34 | 27 | -1.98 | -0.18 | 5.3 | -0.63 | -0.84 | -2.04 |
| 96 | `M143` 장대양봉 이후 눌림목 / 5일선 매매 (Undur ke | **41.2** | 23 | 44 | 32 | 18 | BELUM CUKUP | 15 | 29/5 | -3.02 | 26 | -1.49 | -0.28 | 2.2 | -1.08 | – | -8.30 |
| 97 | `N19X13` Bawah jalur BB + RSI<30 → kelu | **41.2** | 18 | 27 | 26 | 30 | BELUM CUKUP | 10 | 143/0 | -2.33 | 14 | -5.83 | -0.75 | 4.0 | -0.91 | – | – |
| 98 | `M91` Stochastic Pop (Bernstein/Stec | **41.1** | 31 | 22 | 49 | 20 | BELUM CUKUP | 16 | 39/34 | -3.91 | 27 | -2.78 | -0.17 | 7.5 | -0.03 | +0.67 | -0.14 |
| 99 | `N124X36` Episodic pivot gap 8-10% → kel | **41.1** | 18 | 20 | 35 | 30 | BELUM CUKUP | 10 | 43/18 | -2.43 | 14 | -8.25 | -0.69 | 6.1 | -1.00 | – | – |
| 100 | `N35X36` Pecah 52 minggu tinggi → kelua | **41.0** | 18 | 24 | 26 | 30 | BELUM CUKUP | 10 | 51/9 | -5.84 | 14 | -3.30 | -0.52 | 2.6 | -1.81 | – | – |
| 101 | `M128` Inventory Retracement Bar (IRB | **40.9** | 34 | 29 | 52 | 16 | BELUM CUKUP | 24 | 172/140 | -1.51 | 27 | -5.28 | -0.48 | 7.4 | -0.34 | +0.38 | -1.43 |
| 102 | `M105` Supertrend tulen | **40.9** | 30 | 34 | 52 | 16 | BELUM CUKUP | 24 | 376/226 | -3.13 | 27 | -2.12 | -0.17 | 5.8 | -0.35 | +0.20 | -1.07 |
| 103 | `N36X16` Pocket pivot → keluar bila sup | **40.9** | 23 | 26 | 37 | 30 | BELUM CUKUP | 14 | 177/113 | -3.90 | 14 | -3.52 | -0.32 | 4.5 | -1.60 | – | – |
| 104 | `M111` Sistem Volatiliti Wilder | **40.8** | 31 | 35 | 52 | 12 | BELUM CUKUP | 25 | 275/171 | -2.85 | 27 | -1.40 | -0.13 | 4.9 | -0.32 | -0.79 | -0.88 |
| 105 | `N09X36` Undur EMA10 + penapis EMA50 →  | **40.8** | 22 | 27 | 37 | 30 | BELUM CUKUP | 14 | 233/120 | -3.43 | 14 | -5.24 | -0.70 | 3.9 | -1.54 | – | – |
| 106 | `N06X36` Golden cross MA50/MA200 → kelu | **40.8** | 21 | 33 | 28 | 30 | BELUM CUKUP | 13 | 31/5 | -2.24 | 14 | -5.22 | -0.69 | 4.1 | -1.48 | – | – |
| 107 | `M126` Hidden Smash Day (beli, Larry  | **40.8** | 20 | 30 | 36 | 15 | BELUM CUKUP | 12 | 21/11 | -3.08 | 26 | -5.44 | -0.67 | 5.1 | -0.83 | – | -1.01 |
| 108 | `M30` BB Free Bar + Himpitan 50/2.5 | **40.7** | 29 | 29 | 54 | 16 | BELUM CUKUP | 21 | 230/123 | -2.18 | 27 | -1.89 | -0.17 | 6.0 | -0.04 | +0.25 | -0.07 |
| 109 | `N24X36` Supertrend(10,3) + ADX>20 → ke | **40.7** | 24 | 23 | 40 | 30 | BELUM CUKUP | 14 | 182/113 | -3.20 | 14 | -6.48 | -0.68 | 4.5 | -1.27 | – | – |
| 110 | `N53X16` Supertrend + ADX>25 → keluar b | **40.7** | 19 | 26 | 40 | 30 | BELUM CUKUP | 13 | 120/49 | -4.13 | 14 | -5.65 | -0.52 | 6.3 | -0.98 | – | – |
| 111 | `N33X16` Donchian20 + penapis MA200 → k | **40.7** | 19 | 23 | 32 | 30 | BELUM CUKUP | 11 | 106/58 | -6.51 | 14 | -4.23 | -0.59 | 3.2 | -1.87 | – | – |
| 112 | `N80X36` Tinggi sepanjang masa → keluar | **40.7** | 15 | 17 | 29 | 30 | BELUM CUKUP | 9 | 40/8 | -5.99 | 14 | -5.55 | -0.79 | 3.4 | -1.40 | – | – |
| 113 | `M80` Radge Saluran Purata Bergerak  | **40.6** | 28 | 32 | 54 | 22 | BELUM CUKUP | 26 | 313/121 | -2.07 | 27 | -3.68 | -0.36 | 5.4 | -0.07 | +1.75 | -0.11 |
| 114 | `N08X36` tutup>EMA20 tidak terlalu jauh | **40.6** | 19 | 32 | 35 | 30 | BELUM CUKUP | 14 | 459/389 | -2.48 | 14 | -6.83 | -0.71 | 4.5 | -1.84 | – | – |
| 115 | `N07X16` Tiga MA tersusun → keluar bila | **40.6** | 19 | 31 | 37 | 30 | BELUM CUKUP | 14 | 174/76 | -3.74 | 14 | -3.38 | -0.56 | 3.1 | -1.51 | – | – |
| 116 | `N51X16` BB squeeze + Supertrend → kelu | **40.6** | 15 | 32 | 21 | 30 | BELUM CUKUP | 10 | 16/4 | -3.84 | 14 | -5.84 | -0.71 | 4.2 | -2.09 | – | – |
| 117 | `M139` 均线首次粘合向上发散 (MA berhimpun kali  | **40.5** | 29 | 36 | 46 | 15 | BELUM CUKUP | 24 | 96/54 | -4.53 | 27 | -0.67 | -0.06 | 5.0 | -0.74 | -0.10 | -2.55 |
| 118 | `N74X16` MACD atas garis isyarat (keada | **40.4** | 17 | 32 | 38 | 30 | BELUM CUKUP | 14 | 717/639 | -1.98 | 14 | -5.45 | -0.40 | 6.3 | -1.53 | – | – |
| 119 | `M92` CCI-50 | **40.3** | 31 | 33 | 49 | 17 | BELUM CUKUP | 27 | 588/527 | -1.54 | 27 | -6.85 | -0.51 | 5.5 | -0.74 | +0.45 | -1.61 |
| 120 | `N42X36` Lonjakan volum 2x → keluar sel | **40.3** | 22 | 22 | 40 | 30 | BELUM CUKUP | 14 | 221/136 | -1.73 | 14 | -7.91 | -0.74 | 5.8 | -1.20 | – | – |
| 121 | `N33X14` Donchian20 + penapis MA200 → k | **40.3** | 20 | 20 | 28 | 30 | BELUM CUKUP | 11 | 116/18 | -6.53 | 14 | -4.09 | -0.67 | 3.5 | -1.84 | – | – |
| 122 | `N57X36` ADX bangkit daripada <20 → kel | **40.3** | 20 | 21 | 27 | 30 | BELUM CUKUP | 11 | 77/25 | -6.64 | 14 | -4.35 | -0.53 | 4.3 | -2.09 | – | – |
| 123 | `N76X36` Tutup > MA50 (penapis trend tu | **40.2** | 20 | 25 | 37 | 30 | BELUM CUKUP | 14 | 200/150 | -3.55 | 14 | -9.41 | -0.81 | 6.1 | -1.59 | – | – |
| 124 | `N22X36` BB pecah atas + RSI → keluar s | **40.2** | 17 | 25 | 41 | 30 | BELUM CUKUP | 13 | 122/75 | -4.78 | 14 | -7.11 | -0.62 | 5.7 | -0.93 | – | – |
| 125 | `M02` MACD + SMA200 | **40.1** | 31 | 24 | 44 | 48 | BELUM CUKUP | 27 | 139/117 | -4.19 | 27 | -3.69 | -0.23 | 6.1 | -1.27 | +0.52 | -8.56 |
| 126 | `M134` First Kiss After Daylight (Lan | **40.1** | 26 | 33 | 48 | 15 | BELUM CUKUP | 21 | 69/39 | -3.09 | 27 | -4.50 | -0.40 | 5.5 | -0.33 | +0.04 | -0.44 |
| 127 | `N75X14` RSI14 < 40 tanpa penapis → kel | **40.1** | 20 | 26 | 37 | 30 | BELUM CUKUP | 14 | 391/61 | -1.77 | 14 | -7.36 | -0.78 | 4.9 | -1.42 | – | – |
| 128 | `N53X17` Supertrend + ADX>25 → keluar b | **40.1** | 19 | 24 | 36 | 30 | BELUM CUKUP | 13 | 112/16 | -4.14 | 14 | -5.82 | -0.54 | 6.1 | -0.94 | – | – |
| 129 | `N33X36` Donchian20 + penapis MA200 → k | **40.1** | 17 | 20 | 32 | 30 | BELUM CUKUP | 11 | 102/52 | -5.34 | 14 | -6.65 | -0.77 | 4.3 | -1.84 | – | – |
| 130 | `N51X36` BB squeeze + Supertrend → kelu | **40.1** | 14 | 26 | 21 | 30 | BELUM CUKUP | 10 | 16/6 | -4.04 | 14 | -6.33 | -0.74 | 4.3 | -2.27 | – | – |
| 131 | `N124X15` Episodic pivot gap 8-10% → eko | **40.0** | 16 | 20 | 25 | 30 | BELUM CUKUP | 10 | 43/0 | -4.36 | 14 | -5.79 | -0.42 | 6.0 | -0.94 | – | – |
| 132 | `N42X16` Lonjakan volum 2x → keluar bil | **39.9** | 20 | 21 | 41 | 30 | BELUM CUKUP | 14 | 225/147 | -1.81 | 14 | -7.41 | -0.69 | 6.0 | -1.13 | – | – |
| 133 | `N38X36` VCP pecah → keluar selepas DUA | **39.9** | 23 | 29 | 24 | 30 | BELUM CUKUP | 14 | 44/24 | -3.99 | 14 | -6.47 | -0.79 | 4.0 | -2.57 | – | – |
| 134 | `M140` 猎豹出击 (Serangan Cheetah) | **39.9** | 20 | 24 | 34 | 13 | BELUM CUKUP | 12 | 43/26 | -4.08 | 27 | -6.96 | -0.74 | 4.9 | -1.51 | -0.59 | -1.59 |
| 135 | `M135` 3rd Watch | **39.9** | 16 | 14 | 29 | 15 | BELUM CUKUP | 9 | 15/6 | -9.98 | 27 | -7.02 | -0.83 | 4.9 | -1.53 | – | -8.14 |
| 136 | `N68X16` Bullish engulfing + EMA21 → ke | **39.7** | 15 | 26 | 39 | 30 | BELUM CUKUP | 13 | 129/55 | -2.99 | 14 | -5.78 | -0.49 | 6.8 | -1.12 | – | – |
| 137 | `M04` BB Squeeze Breakout | **39.6** | 27 | 26 | 52 | 16 | BELUM CUKUP | 21 | 155/88 | -3.60 | 27 | -2.39 | -0.22 | 5.5 | -0.22 | +0.30 | -0.36 |
| 138 | `N45X36` Undur EMA21 cerun positif → ke | **39.6** | 16 | 24 | 38 | 30 | BELUM CUKUP | 13 | 151/94 | -3.91 | 14 | -7.11 | -0.61 | 5.1 | -1.47 | – | – |
| 139 | `M136` Short/Intermediate-term Low (L | **39.5** | 27 | 34 | 47 | 17 | BELUM CUKUP | 27 | 854/464 | -4.06 | 27 | -4.65 | -0.44 | 4.3 | -0.93 | +0.51 | -0.59 |
| 140 | `M49` Ichimoku (Tutup Atas Awan + Te | **39.5** | 30 | 34 | 45 | 12 | BELUM CUKUP | 27 | 335/240 | -2.80 | 27 | -3.80 | -0.34 | 4.8 | -1.18 | -0.81 | -1.68 |
| 141 | `N07X36` Tiga MA tersusun → keluar sele | **39.5** | 17 | 26 | 36 | 30 | BELUM CUKUP | 14 | 171/63 | -4.25 | 14 | -5.20 | -0.65 | 4.3 | -1.57 | – | – |
| 142 | `M149` 3-Step Pullback | **39.4** | 26 | 31 | 52 | 14 | BELUM CUKUP | 25 | 251/106 | -2.82 | 27 | -3.82 | -0.32 | 6.7 | -0.28 | -0.21 | -0.25 |
| 143 | `M36` Turtle 55/20 | **39.3** | 27 | 29 | 51 | 16 | BELUM CUKUP | 25 | 350/228 | -2.59 | 27 | -4.72 | -0.33 | 7.8 | -0.48 | +0.36 | -1.03 |
| 144 | `M106` DMI Wilder | **39.3** | 26 | 32 | 48 | 13 | BELUM CUKUP | 23 | 136/112 | -2.23 | 27 | -5.36 | -0.71 | 3.5 | -0.79 | -0.58 | -2.04 |
| 145 | `N08X16` tutup>EMA20 tidak terlalu jauh | **39.3** | 15 | 30 | 34 | 30 | BELUM CUKUP | 14 | 529/450 | -2.62 | 14 | -7.21 | -0.62 | 4.7 | -1.90 | – | – |
| 146 | `N41X16` CMF20>0 + tutup>EMA20 → keluar | **39.3** | 16 | 28 | 34 | 30 | BELUM CUKUP | 14 | 321/262 | -3.38 | 14 | -5.61 | -0.56 | 4.6 | -1.98 | – | – |
| 147 | `N57X16` ADX bangkit daripada <20 → kel | **39.3** | 18 | 19 | 28 | 30 | BELUM CUKUP | 12 | 75/41 | -6.63 | 14 | -5.37 | -0.60 | 4.5 | -2.16 | – | – |
| 148 | `N24X17` Supertrend(10,3) + ADX>20 → ke | **39.3** | 17 | 19 | 31 | 30 | BELUM CUKUP | 12 | 133/52 | -5.56 | 14 | -5.91 | -0.61 | 4.5 | -1.92 | – | – |
| 149 | `M34` Carter TTM Squeeze | **39.2** | 27 | 27 | 49 | 14 | BELUM CUKUP | 22 | 106/65 | -2.26 | 27 | -4.91 | -0.38 | 5.9 | -0.42 | -0.16 | -1.13 |
| 150 | `N31X36` Turtle sistem 2 → keluar selep | **39.2** | 16 | 16 | 28 | 30 | BELUM CUKUP | 11 | 105/23 | -5.93 | 14 | -6.92 | -0.70 | 4.8 | -2.01 | – | – |
| 151 | `M119` 180 Bullish (Cooper) | **39.1** | 26 | 29 | 46 | 18 | BELUM CUKUP | 24 | 168/107 | -2.44 | 27 | -6.49 | -0.60 | 6.1 | -0.98 | +0.78 | -2.59 |
| 152 | `N40X36` OBV tinggi baharu + MA50 → kel | **39.1** | 20 | 16 | 44 | 30 | BELUM CUKUP | 14 | 84/33 | -2.25 | 14 | -11.03 | -0.76 | 8.0 | -0.34 | – | – |
| 153 | `N42X14` Lonjakan volum 2x → keluar bil | **39.1** | 20 | 18 | 37 | 30 | BELUM CUKUP | 14 | 204/28 | -3.17 | 14 | -6.10 | -0.50 | 6.6 | -1.07 | – | – |
| 154 | `N56X17` RSI>50 + ADX>20 → keluar bila  | **39.1** | 18 | 19 | 32 | 30 | BELUM CUKUP | 13 | 149/63 | -5.46 | 14 | -5.90 | -0.63 | 4.4 | -1.97 | – | – |
| 155 | `N76X16` Tutup > MA50 (penapis trend tu | **39.0** | 15 | 28 | 32 | 30 | BELUM CUKUP | 14 | 361/297 | -3.00 | 14 | -5.82 | -0.63 | 3.7 | -2.18 | – | – |
| 156 | `N40X16` OBV tinggi baharu + MA50 → kel | **39.0** | 19 | 16 | 45 | 30 | BELUM CUKUP | 14 | 103/52 | -1.80 | 14 | -11.54 | -0.71 | 7.9 | -0.40 | – | – |
| 157 | `N37X14` Gap and go → keluar bila rsi14 | **39.0** | 14 | 16 | 29 | 30 | BELUM CUKUP | 11 | 87/15 | -5.46 | 14 | -7.47 | -0.56 | 6.2 | -1.66 | – | – |
| 158 | `M06` Minervini VCP Breakout | **38.9** | 26 | 32 | 44 | 15 | BELUM CUKUP | 24 | 90/58 | -3.97 | 27 | -3.95 | -0.42 | 4.2 | -1.01 | -0.11 | -2.68 |
| 159 | `N42X15` Lonjakan volum 2x → ekori Chan | **38.9** | 21 | 22 | 25 | 33 | BELUM CUKUP | 14 | 188/0 | -3.78 | 14 | -5.49 | -0.41 | 6.7 | -1.10 | – | – |
| 160 | `M148` Natural Number Method | **38.8** | 29 | 38 | 39 | 10 | BELUM CUKUP | 26 | 233/225 | -2.93 | 27 | -3.87 | -0.37 | 4.5 | -1.87 | -1.47 | -6.64 |
| 161 | `M28` VWAP Separator + Kiss Pivot | **38.8** | 28 | 28 | 44 | 12 | BELUM CUKUP | 23 | 136/123 | -1.76 | 27 | -8.31 | -0.85 | 6.1 | -1.23 | -0.76 | -9.09 |
| 162 | `N56X36` RSI>50 + ADX>20 → keluar selep | **38.8** | 16 | 21 | 34 | 30 | BELUM CUKUP | 14 | 212/143 | -3.16 | 14 | -9.81 | -0.75 | 7.3 | -1.93 | – | – |
| 163 | `N24X16` Supertrend(10,3) + ADX>20 → ke | **38.7** | 15 | 17 | 32 | 30 | BELUM CUKUP | 12 | 125/62 | -6.19 | 14 | -6.95 | -0.76 | 4.5 | -1.88 | – | – |
| 164 | `N56X16` RSI>50 + ADX>20 → keluar bila  | **38.6** | 14 | 24 | 36 | 30 | BELUM CUKUP | 14 | 236/172 | -3.30 | 14 | -6.89 | -0.66 | 5.3 | -1.64 | – | – |
| 165 | `N54X16` Supertrend + RSI>50 → keluar b | **38.6** | 14 | 14 | 29 | 30 | BELUM CUKUP | 11 | 128/71 | -7.17 | 14 | -6.71 | -0.72 | 5.8 | -2.25 | – | – |
| 166 | `M59` Anjakan Julat RSI | **38.5** | 18 | 20 | 40 | 15 | BELUM CUKUP | 14 | 36/24 | -6.70 | 27 | -5.75 | -0.55 | 5.6 | -0.89 | – | -2.89 |
| 167 | `N113X36` 80-20 bar (sisi beli) → keluar | **38.5** | 18 | 17 | 37 | 30 | BELUM CUKUP | 14 | 369/310 | -1.62 | 14 | -11.79 | -0.87 | 8.7 | -1.63 | – | – |
| 168 | `N27X16` Ichimoku atas awan → keluar bi | **38.4** | 14 | 24 | 31 | 30 | BELUM CUKUP | 14 | 191/124 | -3.11 | 14 | -7.10 | -0.75 | 4.4 | -2.29 | – | – |
| 169 | `M107` Golden Cross SMA50/200 | **38.3** | 23 | 28 | 43 | 17 | BELUM CUKUP | 22 | 47/13 | -3.24 | 27 | -6.45 | -0.62 | 4.3 | -0.55 | +0.56 | -0.84 |
| 170 | `N113X16` 80-20 bar (sisi beli) → keluar | **38.2** | 20 | 12 | 39 | 30 | BELUM CUKUP | 14 | 387/321 | -1.38 | 14 | -12.90 | -0.90 | 9.5 | -1.39 | – | – |
| 171 | `N119X15` 3 tutup turun berturut → ekori | **38.2** | 10 | 10 | 15 | 30 | BELUM CUKUP | 9 | 58/0 | -5.24 | 14 | -9.57 | -0.84 | 6.6 | -2.14 | – | – |
| 172 | `M156` Single Penetration (DiNapoli) | **38.1** | 28 | 27 | 45 | 15 | BELUM CUKUP | 27 | 304/232 | -1.73 | 27 | -5.79 | -0.40 | 8.1 | -1.12 | -0.08 | -3.23 |
| 173 | `M99` Three Line Break | **38.1** | 27 | 26 | 47 | 13 | BELUM CUKUP | 25 | 174/141 | -3.95 | 27 | -5.30 | -0.42 | 5.6 | -0.85 | -0.64 | -3.13 |
| 174 | `M26` Garis Trend Undur 3 Sentuhan + | **38.0** | 20 | 30 | 43 | 15 | BELUM CUKUP | 21 | 82/57 | -1.90 | 27 | -7.73 | -0.76 | 4.9 | -1.05 | +0.01 | -1.48 |
| 175 | `N28X17` ADX>25 + DI+ > DI- → keluar bi | **38.0** | 15 | 20 | 30 | 30 | BELUM CUKUP | 14 | 157/12 | -4.44 | 14 | -6.64 | -0.54 | 6.1 | -1.63 | – | – |
| 176 | `N39X36` NR7 kemudian pecah → keluar se | **38.0** | 4 | 5 | 19 | 30 | BELUM CUKUP | 8 | 35/12 | -6.76 | 13 | -13.15 | -0.86 | 8.6 | -2.60 | – | – |
| 177 | `N50X14` Mampat + pecah volum 1.5x → ke | **37.9** | 10 | 13 | 29 | 30 | BELUM CUKUP | 11 | 27/5 | -4.25 | 14 | -9.07 | -0.64 | 7.0 | -1.32 | – | – |
| 178 | `N28X14` ADX>25 + DI+ > DI- → keluar bi | **37.8** | 14 | 19 | 32 | 30 | BELUM CUKUP | 14 | 232/28 | -4.29 | 14 | -8.10 | -0.54 | 7.0 | -1.66 | – | – |
| 179 | `M14` Walking with the Whales | **37.7** | 29 | 23 | 46 | 15 | BELUM CUKUP | 27 | 1073/881 | -1.48 | 27 | -13.15 | -0.80 | 8.9 | -1.01 | +0.11 | -1.71 |
| 180 | `N22X16` BB pecah atas + RSI → keluar b | **37.7** | 12 | 14 | 40 | 30 | BELUM CUKUP | 13 | 123/80 | -6.41 | 14 | -8.02 | -0.76 | 5.5 | -1.06 | – | – |
| 181 | `M95` Nisbah Kebaharuan High 52 Ming | **37.6** | 21 | 26 | 47 | 14 | BELUM CUKUP | 22 | 129/81 | -2.69 | 27 | -8.98 | -0.72 | 6.7 | -0.75 | -0.14 | -1.54 |
| 182 | `M29` EMA3 + RSI75 + Stokastik | **37.6** | 27 | 27 | 41 | 4 | BELUM CUKUP | 19 | 42/34 | -2.42 | 27 | -9.57 | -0.69 | 8.5 | -1.04 | -3.05 | -4.95 |
| 183 | `N36X14` Pocket pivot → keluar bila rsi | **37.6** | 17 | 14 | 31 | 30 | BELUM CUKUP | 14 | 177/36 | -5.38 | 14 | -7.53 | -0.75 | 5.4 | -1.89 | – | – |
| 184 | `N22X14` BB pecah atas + RSI → keluar b | **37.5** | 13 | 14 | 33 | 30 | BELUM CUKUP | 13 | 129/30 | -6.38 | 14 | -8.65 | -0.71 | 6.5 | -1.52 | – | – |
| 185 | `N29X36` PSAR naik + tutup>MA50 → kelua | **37.5** | 12 | 16 | 30 | 30 | BELUM CUKUP | 13 | 170/122 | -4.73 | 14 | -12.09 | -0.83 | 9.8 | -2.41 | – | – |
| 186 | `M73` ADX(5) > 40 + Julat Terkecil 6 | **37.3** | 29 | 22 | 47 | 14 | BELUM CUKUP | 27 | 1137/926 | -0.81 | 27 | -10.44 | -0.83 | 7.6 | -0.93 | -0.31 | -5.36 |
| 187 | `M152` Spike & Ledge | **37.3** | 20 | 29 | 41 | 15 | BELUM CUKUP | 22 | 56/14 | -5.00 | 27 | -5.71 | -0.46 | 5.3 | -0.82 | +0.02 | -2.34 |
| 188 | `N42X17` Lonjakan volum 2x → keluar bil | **37.3** | 13 | 14 | 40 | 30 | BELUM CUKUP | 14 | 219/78 | -2.67 | 14 | -10.09 | -0.68 | 8.0 | -1.08 | – | – |
| 189 | `N54X36` Supertrend + RSI>50 → keluar s | **37.2** | 13 | 12 | 33 | 30 | BELUM CUKUP | 13 | 188/134 | -4.03 | 14 | -11.96 | -0.84 | 8.8 | -2.03 | – | – |
| 190 | `M55` Guppy GMMA | **37.1** | 27 | 21 | 47 | 13 | BELUM CUKUP | 25 | 246/191 | -3.15 | 27 | -9.01 | -0.78 | 6.2 | -0.93 | -0.48 | -2.34 |
| 191 | `M101` Bulkowski: Tiga lembah menaik | **37.1** | 20 | 15 | 47 | 15 | BELUM CUKUP | 17 | 46/29 | -3.73 | 27 | -9.11 | -0.61 | 9.1 | -0.29 | – | -0.70 |
| 192 | `M155` Market Cycle Strategy | **37.0** | 24 | 24 | 45 | 17 | BELUM CUKUP | 27 | 790/577 | -4.31 | 27 | -6.21 | -0.53 | 5.6 | -1.12 | +0.61 | -2.92 |
| 193 | `M57` Landry Trend Knockout (TKO) | **37.0** | 28 | 28 | 40 | 9 | BELUM CUKUP | 27 | 194/153 | -2.86 | 27 | -6.51 | -0.74 | 4.9 | -1.80 | -1.49 | -4.20 |
| 194 | `M66` IBD Undur Pertama ke Purata 50 | **37.0** | 26 | 22 | 47 | 14 | BELUM CUKUP | 26 | 270/207 | -2.66 | 27 | -7.07 | -0.54 | 8.0 | -0.93 | -0.21 | -2.23 |
| 195 | `N75X13` RSI14 < 40 tanpa penapis → kel | **37.0** | 11 | 23 | 26 | 30 | BELUM CUKUP | 14 | 207/1 | -2.94 | 14 | -9.59 | -0.82 | 5.4 | -1.28 | – | – |
| 196 | `N75X15` RSI14 < 40 tanpa penapis → eko | **37.0** | 11 | 23 | 24 | 30 | BELUM CUKUP | 14 | 201/0 | -3.01 | 14 | -9.59 | -0.82 | 5.4 | -1.25 | – | – |
| 197 | `N50X17` Mampat + pecah volum 1.5x → ke | **37.0** | 8 | 10 | 29 | 30 | BELUM CUKUP | 11 | 26/5 | -4.84 | 14 | -10.79 | -0.69 | 8.1 | -1.31 | – | – |
| 198 | `M141` First Thrust (Landry) | **37.0** | 3 | 7 | 31 | 15 | BELUM CUKUP | 9 | 27/18 | -8.07 | 27 | -16.06 | -0.86 | 8.0 | -1.61 | – | -5.67 |
| 199 | `M50` Elder Triple Screen | **36.9** | 24 | 24 | 47 | 16 | BELUM CUKUP | 27 | 658/513 | -1.87 | 27 | -11.35 | -0.84 | 7.7 | -0.89 | +0.35 | -1.50 |
| 200 | `N29X16` PSAR naik + tutup>MA50 → kelua | **36.9** | 12 | 17 | 30 | 30 | BELUM CUKUP | 14 | 229/173 | -4.75 | 14 | -8.09 | -0.68 | 6.6 | -2.36 | – | – |
| 201 | `N73X13` Tutup bawah jalur bawah BB(20, | **36.8** | 11 | 20 | 26 | 30 | BELUM CUKUP | 14 | 226/1 | -3.06 | 14 | -9.57 | -0.83 | 6.3 | -1.31 | – | – |
| 202 | `N27X36` Ichimoku atas awan → keluar se | **36.8** | 11 | 14 | 28 | 30 | BELUM CUKUP | 13 | 115/50 | -5.53 | 14 | -9.48 | -0.74 | 6.1 | -2.28 | – | – |
| 203 | `M11` NR7 Breakout + Volume | **36.0** | 22 | 21 | 44 | 12 | BELUM CUKUP | 24 | 130/99 | -1.38 | 27 | -10.84 | -0.63 | 9.4 | -1.25 | -0.76 | -1.11 |
| 204 | `N119X13` 3 tutup turun berturut → kelua | **35.9** | 8 | 16 | 34 | 30 | BELUM CUKUP | 14 | 289/65 | -2.25 | 14 | -10.90 | -0.99 | 7.4 | -1.79 | – | – |
| 205 | `N55X13` BB + RSI + ADX>20 → keluar bil | **35.9** | 11 | 18 | 18 | 30 | BELUM CUKUP | 14 | 135/0 | -2.89 | 14 | -8.74 | -0.96 | 5.4 | -1.98 | – | – |
| 206 | `N47X16` NR7 + EMA9>EMA21 → keluar bila | **35.7** | 7 | 17 | 32 | 30 | BELUM CUKUP | 14 | 208/110 | -4.03 | 14 | -11.55 | -0.83 | 7.7 | -2.16 | – | – |
| 207 | `M31` Band Walk (BB 20/2) | **35.6** | 22 | 16 | 52 | 17 | BELUM CUKUP | 25 | 404/177 | -2.52 | 27 | -7.11 | -0.43 | 9.0 | -0.32 | +0.65 | -0.58 |
| 208 | `M125` 2-Bar Breakout | **35.3** | 21 | 22 | 44 | 14 | BELUM CUKUP | 27 | 1149/660 | -4.61 | 27 | -9.05 | -0.62 | 6.2 | -1.24 | -0.41 | -0.69 |
| 209 | `M19` Sneaky Pivot (proksi harian) | **35.1** | 18 | 22 | 46 | 12 | BELUM CUKUP | 25 | 438/347 | -4.75 | 27 | -9.67 | -0.65 | 6.4 | -1.06 | -0.75 | -14.71 |
| 210 | `M47` Holy Grail Raschke | **34.6** | 10 | 17 | 32 | 15 | BELUM CUKUP | 17 | 39/33 | -2.94 | 27 | -11.00 | -0.87 | 7.3 | -2.03 | – | -17.07 |
| 211 | `N16X13` RSI2<10 tanpa penapis → keluar | **34.6** | 4 | 16 | 29 | 30 | BELUM CUKUP | 14 | 313/6 | -2.44 | 14 | -13.05 | -0.99 | 8.1 | -1.46 | – | – |
| 212 | `M154` HOLP (High of Low Period) | **34.5** | 14 | 16 | 40 | 11 | BELUM CUKUP | 19 | 100/50 | -5.26 | 27 | -12.79 | -0.83 | 8.7 | -1.37 | -0.95 | -5.47 |
| 213 | `M01` Bollinger Band + RSI | **33.3** | 17 | 12 | 42 | 18 | BELUM CUKUP | 24 | 139/27 | -1.94 | 27 | -12.27 | -0.73 | 6.8 | -0.92 | +0.76 | -3.38 |
| 214 | `M82` Arthur Hill Rotasi Sasaran 10% | **33.1** | 20 | 12 | 47 | 17 | BELUM CUKUP | 27 | 607/277 | -2.89 | 27 | -8.06 | -0.41 | 11.5 | -0.95 | +0.61 | -3.65 |
| 215 | `M81` Bensdorp Long Trend High Momen | **33.1** | 2 | 6 | 39 | 15 | BELUM CUKUP | 13 | 431/215 | -6.49 | 27 | -23.54 | -0.89 | 16.5 | -1.56 | – | -4.42 |
| 216 | `M79` Radge: 20% Flipper | **33.0** | 13 | 19 | 42 | 13 | BELUM CUKUP | 26 | 396/227 | -6.29 | 27 | -10.75 | -0.67 | 8.2 | -1.49 | -0.43 | -3.11 |
| 217 | `M03` BB Break + Divergence RSI | **32.9** | 10 | 24 | 47 | 15 | BELUM CUKUP | 27 | 449/401 | -2.39 | 27 | -10.88 | -0.73 | 5.9 | -0.92 | +0.01 | -3.81 |
| 218 | `N47X36` NR7 + EMA9>EMA21 → keluar sele | **32.9** | 0 | 11 | 28 | 30 | BELUM CUKUP | 13 | 187/81 | -4.80 | 14 | -16.47 | -0.84 | 10.8 | -2.57 | – | – |
| 219 | `M147` Improved Three-Bar Pullback | **32.7** | 6 | 17 | 35 | 10 | BELUM CUKUP | 18 | 119/58 | -6.43 | 27 | -15.61 | -0.73 | 8.6 | -1.99 | -1.38 | -1.82 |
| 220 | `M76` Undercut & Rally pada Low Pent | **32.1** | 10 | 20 | 39 | 6 | BELUM CUKUP | 23 | 85/80 | -3.33 | 27 | -12.54 | -0.85 | 8.2 | -1.70 | -2.40 | -6.25 |
| 221 | `M122` Moving Momentum (ChartSchool) | **31.9** | 14 | 17 | 34 | 11 | BELUM CUKUP | 26 | 117/80 | -5.55 | 27 | -13.69 | -0.81 | 8.1 | -2.34 | -1.11 | -6.76 |
| 222 | `N16X15` RSI2<10 tanpa penapis → ekori  | **31.9** | 1 | 11 | 21 | 30 | BELUM CUKUP | 14 | 285/0 | -2.74 | 14 | -15.53 | -1.00 | 10.3 | -1.55 | – | – |
| 223 | `M09` Volumatic VIDYA Pivot Retest | **31.3** | 2 | 11 | 28 | 15 | BELUM CUKUP | 16 | 41/31 | -6.11 | 27 | -16.80 | -0.90 | 10.5 | -2.43 | – | -12.56 |
| 224 | `M123` CCI Correction (Lambert, Chart | **30.5** | 6 | 22 | 33 | 12 | BELUM CUKUP | 25 | 194/188 | -2.12 | 27 | -16.04 | -0.95 | 8.8 | -2.49 | -0.89 | -4.94 |
| 225 | `M161` EMA 10/21 + Supertrend (10,3) | **30.1** | 8 | 11 | 48 | 19 | BELUM CUKUP | 27 | 524/379 | -2.15 | 27 | -18.71 | -0.85 | 12.2 | -0.79 | +1.08 | -1.74 |
| 226 | `M20` EMA10/15 Crossover + Sudut | **30.0**⌈ | 28 | 33 | 44 | 12 | GAGAL | 27 | 533/485 | -1.88 | 27 | -7.34 | -0.66 | 4.8 | -1.32 | -0.77 | -8.37 |
| 227 | `M90` Pring KST | **29.9** | 7 | 14 | 43 | 7 | BELUM CUKUP | 25 | 94/67 | -4.21 | 27 | -15.17 | -0.76 | 13.1 | -1.22 | -2.08 | -4.44 |

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

