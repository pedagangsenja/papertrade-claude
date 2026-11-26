# Skor Kaedah 0–100 (pangkat maklumat, BUKAN keputusan)

> **Status keputusan (kad skor, harga 2026-11-25):** TERBUKTI 0 · CALON 0 · BELUM CUKUP 225 · GAGAL 2 · NEGATIF 0. Rejim QQQ OFF sejak 2026-10-16. Hanya **TERBUKTI** layak untuk wang sebenar (`laporan/KAD_SKOR.md`); nombor dalam laporan ini BUKAN keputusan dan tidak boleh dibaca sebagai pangkat untuk wang sebenar.

Dijana 2026-11-26 oleh `standard/skor_kaedah.py` (Actions `analisis.yml`, selepas kad skor). Harga pada tutup 2026-11-25; 227 kaedah; 29 hari beli langsung (rejim ON 1, OFF 28). Pradaftar 2026-11-09: `standard/SPEC_SKOR_KAEDAH.md` (berat dan sauh dikunci `ujian/test_skor_kaedah.py::TestKunci`). Rekod analisis sahaja: tiada order, tiada wang sebenar.

## Cara membaca

- **Skor** = min geometri berberat empat tiang (Untung 35 · Tahan 30 · Bukti 25 · Konsisten 10), dikecut ke 50 mengikut data: berat data = hari beli ÷ (hari beli + 20). Kaedah dengan 2 hari beli tidak boleh menjauhi 50. 100 = unggul semua segi; 50 = neutral/tiada bukti; < 50 = lebih buruk daripada neutral.
- **Siling** ikut kad skor: NEGATIF ≤ 20, GANTUNG/BERSARA ≤ 30, GAGAL ≤ 40. Tanda ⌈ = siling terpakai.
- **Satu-satunya status yang membenarkan wang sebenar ialah TERBUKTI dalam `laporan/KAD_SKOR.md`.** Skor tinggi dengan status BELUM CUKUP bermaksud "paling menjanjikan setakat ini", bukan "selamat".
- Deflasi ujian berganda (López de Prado): sauh t Bukti C1 = maks(2.0, E[maks 227 normal]) = 2.81.
- **Semakan kebolehramalan:** skor pada 2026-11-18 lawan pulangan lorong T4 sejak itu, 226 kaedah: Spearman ρ = +0.114 (p = 0.088). Belum ada bukti skor meramal pangkat; jangan pilih kaedah dengannya.
- Metrik T4 (A2, B1, B2, D1) dikira atas lorong T4 L1 **dipotong pada sesi LANGSUNG pertama** kaedah itu (Mxx 2026-10-16, Nxx/GB 2026-11-03) dan diasas semula; sesi isian bina semula tidak dikira (pindaan 9 Nov 2026 (a)). Lajur "T4 sesi/pul" di bawah ialah potongan itu, bukan lorong penuh `T4_KAEDAH.md`.

## Semua kaedah, susun ikut Skor

| # | Kaedah | Skor | Untung | Tahan | Bukti | Konsisten | Status kad | Hari beli | Posisi/tutup | Jangkaan % | T4 sesi | T4 pul % | T4 pul/|MDD| | Ulcer | t buku | Lift | WFE |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `M146` 3-Bar Momentum Pattern | **63.5** | 85 | 76 | 61 | 95 | BELUM CUKUP | 21 | 81/48 | +1.05 | 29 | +7.12 | +1.01 | 3.2 | +1.08 | +2.68 | 2.20 |
| 2 | `M48` Cooper 1-2-3-4 | **58.3** | 69 | 64 | 56 | 83 | BELUM CUKUP | 24 | 89/27 | +0.39 | 29 | +8.83 | +1.54 | 2.5 | +0.64 | -0.48 | 1.40 |
| 3 | `M151` Outside Bar Failure | **58.0** | 61 | 77 | 55 | 62 | BELUM CUKUP | 26 | 134/85 | -0.56 | 29 | +6.92 | +1.73 | 1.2 | +0.13 | -0.20 | 0.26 |
| 4 | `N202X36` RSI2<10 dalam trend naik x X36 | **56.8** | 89 | 91 | 46 | 70 | BELUM CUKUP | 8 | 114/19 | +1.65 | 9 | +1.93 | +0.91 | 1.0 | +0.30 | – | – |
| 5 | `M160` Measured Move Up | **56.8** | 51 | 68 | 62 | 88 | BELUM CUKUP | 27 | 188/119 | -0.82 | 29 | +3.89 | +0.68 | 2.6 | +0.78 | +0.70 | 4.94 |
| 6 | `M133` Bull Hook (Crabel) | **55.0** | 56 | 65 | 59 | 78 | BELUM CUKUP | 16 | 54/45 | -0.72 | 29 | +3.52 | +0.58 | 2.8 | +0.98 | +3.73 | 7.45 |
| 7 | `M118` Expansion Pivot (Cooper) | **54.8** | 55 | 60 | 55 | 90 | BELUM CUKUP | 21 | 87/46 | -0.83 | 29 | +6.35 | +0.76 | 3.3 | +0.42 | +1.40 | 1.32 |
| 8 | `M25` VWAP Wave (proksi harian) | **54.7** | 59 | 60 | 59 | 50 | BELUM CUKUP | 25 | 201/176 | -0.81 | 29 | +3.93 | +0.49 | 4.1 | +0.53 | +1.19 | 2.82 |
| 9 | `M23` Breitstein Kapitulasi + Kesina | **54.1** | 63 | 52 | 61 | 46 | BELUM CUKUP | 25 | 133/108 | -0.57 | 29 | -1.00 | -0.15 | 3.4 | +0.76 | +0.33 | 2.79 |
| 10 | `M159` Heikin-Ashi Trend | **52.7** | 52 | 68 | 45 | 53 | BELUM CUKUP | 29 | 2131/1944 | -0.89 | 29 | +7.75 | +1.26 | 3.4 | -1.19 | -0.54 | -6.78 |
| 11 | `M137` Livermore System | **52.4** | 44 | 64 | 56 | 64 | BELUM CUKUP | 27 | 187/101 | -1.49 | 29 | +6.71 | +1.14 | 2.3 | +0.09 | +0.94 | 0.17 |
| 12 | `M145` Yum-Yum Continuation | **52.2** | 46 | 63 | 55 | 58 | BELUM CUKUP | 25 | 313/112 | -1.27 | 29 | +5.99 | +1.55 | 1.5 | +0.02 | +0.67 | 0.02 |
| 13 | `M74` Lulus Baharu Trend Template Mi | **51.9** | 59 | 60 | 55 | 24 | BELUM CUKUP | 29 | 114/83 | -0.87 | 29 | +3.03 | +0.41 | 3.4 | +0.03 | +0.12 | 0.06 |
| 14 | `M46` Jurang Naik Boleh Beli (Buyabl | **51.6** | 49 | 65 | 48 | 58 | BELUM CUKUP | 14 | 37/27 | -1.41 | 29 | +2.75 | +0.56 | 1.8 | +0.02 | +0.53 | 0.02 |
| 15 | `M158` Doubly Adaptive Profit Targets | **51.6** | 65 | 38 | 60 | 50 | BELUM CUKUP | 26 | 395/220 | -0.18 | 29 | -2.75 | -0.25 | 4.9 | +0.55 | +1.44 | 1.22 |
| 16 | `M104` High Tight Flag / Power Play | **51.2** | 92 | 90 | 43 | 85 | BELUM CUKUP | 1 | 1/0 | +25.76 | 14 | +2.60 | +9.87 | 0.1 | +1.86 | – | 9.85 |
| 17 | `M33` Supertrend + SMA10 | **51.0** | 37 | 60 | 56 | 87 | BELUM CUKUP | 23 | 224/127 | -1.93 | 29 | +7.59 | +1.04 | 2.7 | +0.22 | +0.56 | 1.10 |
| 18 | `M51` O'Neil Cawan & Pemegang | **50.6** | 77 | 60 | 38 | 45 | BELUM CUKUP | 2 | 3/1 | +0.42 | 19 | +0.16 | +0.10 | 0.8 | +0.81 | – | 2.80 |
| 19 | `M70` Pecahan Hari Dalam | **50.5** | 63 | 66 | 54 | 10 | BELUM CUKUP | 29 | 530/462 | -0.61 | 29 | +2.78 | +0.48 | 2.5 | -0.14 | -1.41 | -0.33 |
| 20 | `M93` Bollinger Kaedah II: %b + MFI | **50.5** | 64 | 39 | 58 | 37 | BELUM CUKUP | 26 | 276/124 | -0.15 | 29 | -0.44 | -0.05 | 4.3 | +0.35 | +1.82 | 0.49 |
| 21 | `M45` High 52 Minggu (George & Hwang | **50.0** | 54 | 51 | 36 | 85 | BELUM CUKUP | 1 | 2/1 | -0.63 | 18 | -0.10 | -0.06 | 0.9 | +0.81 | – | 2.15 |
| 22 | `M08` SMA20 + SMA200 | **49.8** | 50 | 45 | 52 | 58 | BELUM CUKUP | 27 | 302/221 | -1.19 | 29 | -1.45 | -0.27 | 3.6 | -0.28 | +0.72 | -0.68 |
| 23 | `M10` EMA3 + CCI + MACD | **49.7** | 40 | 58 | 52 | 56 | BELUM CUKUP | 23 | 128/78 | -2.36 | 29 | +9.71 | +1.47 | 2.7 | -0.18 | +0.40 | -0.51 |
| 24 | `M41` FW Penyatuan Mingguan | **49.7** | 70 | 35 | 46 | 42 | BELUM CUKUP | 6 | 68/14 | +0.50 | 28 | -2.66 | -0.23 | 6.2 | +0.53 | – | 0.90 |
| 25 | `M07` Qullamaggie Breakout | **49.4** | 36 | 64 | 27 | 15 | BELUM CUKUP | 1 | 1/1 | -2.53 | 29 | -0.25 | -0.21 | 0.9 | -0.22 | – | -1.12 |
| 26 | `N25X36` Supertrend + EMA + ADX>23 → ke | **49.2** | 41 | 54 | 45 | 70 | BELUM CUKUP | 15 | 144/63 | -1.87 | 16 | +1.16 | +0.26 | 1.9 | -0.52 | – | – |
| 27 | `M13` Garis Trend Action/Safety Line | **48.9** | 38 | 63 | 47 | 53 | BELUM CUKUP | 29 | 927/786 | -2.65 | 29 | +6.71 | +1.01 | 2.3 | -0.97 | -0.63 | -2.45 |
| 28 | `M27` Price Action 4 Tiang | **48.8** | 47 | 31 | 45 | 15 | BELUM CUKUP | 2 | 546/521 | -1.27 | 29 | -4.16 | -0.81 | 3.3 | -0.18 | – | -0.68 |
| 29 | `M84` Jarak purata bergerak MAD 21/2 | **48.7** | 29 | 13 | 36 | 15 | BELUM CUKUP | 1 | 58/43 | -3.93 | 18 | -7.60 | -0.87 | 7.1 | -0.45 | – | -1.04 |
| 30 | `M35` Pocket Pivot Morales & Kacher | **48.5** | 64 | 41 | 55 | 18 | BELUM CUKUP | 28 | 365/324 | -0.52 | 29 | -2.72 | -0.30 | 5.9 | -0.04 | +0.77 | -0.19 |
| 31 | `M100` Bulkowski Segi Empat & Segi Ti | **48.5** | 56 | 49 | 51 | 18 | BELUM CUKUP | 18 | 64/45 | -0.63 | 29 | +0.52 | +0.06 | 3.4 | -0.02 | +0.92 | -0.08 |
| 32 | `M37` Weinstein Peringkat 2 | **48.5** | 47 | 53 | 29 | 15 | BELUM CUKUP | 3 | 7/1 | -1.32 | 23 | -0.81 | -0.16 | 1.7 | -0.36 | – | -0.53 |
| 33 | `M131` Ross Hook (Joe Ross) | **48.3** | 50 | 47 | 56 | 24 | BELUM CUKUP | 26 | 276/161 | -1.15 | 29 | -0.04 | -0.00 | 4.5 | +0.11 | +0.48 | 0.24 |
| 34 | `M96` Momo India: Ranking Sharpe 3/6 | **48.2** | 25 | 7 | 9 | 15 | BELUM CUKUP | 1 | 6/6 | -13.71 | 18 | -8.21 | -1.00 | 7.4 | -5.92 | – | -15.55 |
| 35 | `M30` BB Free Bar + Himpitan 50/2.5 | **48.0** | 52 | 36 | 57 | 37 | BELUM CUKUP | 22 | 231/125 | -0.95 | 29 | +1.89 | +0.17 | 6.0 | +0.35 | +0.25 | 0.70 |
| 36 | `N204X36` Undur RSI2, gap 2%, RSI silang | **48.0** | 27 | 46 | 31 | 50 | BELUM CUKUP | 3 | 8/0 | -1.63 | 4 | -1.15 | -0.56 | 1.4 | +0.15 | – | – |
| 37 | `M18` EMA9/21 Pullback | **47.9** | 58 | 40 | 55 | 21 | BELUM CUKUP | 29 | 501/447 | -0.64 | 29 | -5.23 | -0.54 | 5.1 | -0.06 | +1.61 | -0.21 |
| 38 | `M39` Radge Pecahan Bollinger 100 ha | **47.9** | 33 | 59 | 51 | 54 | BELUM CUKUP | 24 | 247/71 | -2.75 | 29 | +6.25 | +0.96 | 2.2 | -0.26 | -0.37 | -0.50 |
| 39 | `N53X36` Supertrend + ADX>25 → keluar s | **47.9** | 55 | 38 | 50 | 30 | BELUM CUKUP | 15 | 145/65 | -0.71 | 16 | -3.15 | -0.34 | 4.4 | +0.13 | – | – |
| 40 | `M129` Wick Play | **47.9** | 39 | 48 | 45 | 47 | BELUM CUKUP | 11 | 31/13 | -1.73 | 29 | +2.18 | +0.38 | 2.3 | -0.02 | – | -0.06 |
| 41 | `M78` Alvarez Pecahan Mingguan DTAYS | **47.8** | 27 | 19 | 41 | 15 | BELUM CUKUP | 2 | 73/47 | -2.46 | 28 | -8.85 | -0.79 | 8.4 | -0.06 | – | -0.16 |
| 42 | `M94` Pecutan Momentum (Chen, Yu & W | **47.8** | 3 | 3 | 13 | 15 | BELUM CUKUP | 1 | 33/0 | -15.26 | 18 | -18.95 | -0.87 | 12.0 | -1.65 | – | -4.28 |
| 43 | `M128` Inventory Retracement Bar (IRB | **47.5** | 56 | 35 | 56 | 31 | BELUM CUKUP | 26 | 202/146 | -0.60 | 29 | -3.40 | -0.31 | 7.4 | +0.11 | +0.53 | 0.46 |
| 44 | `N06X36` Golden cross MA50/MA200 → kelu | **47.5** | 60 | 44 | 34 | 30 | BELUM CUKUP | 14 | 32/5 | +0.19 | 16 | -2.86 | -0.38 | 4.0 | -0.78 | – | – |
| 45 | `M142` Pecahan volum dari dasar (底部放量 | **47.3** | 48 | 37 | 45 | 57 | BELUM CUKUP | 18 | 56/14 | -0.82 | 27 | +1.56 | +0.19 | 3.4 | +0.03 | – | 0.06 |
| 46 | `N68X36` Bullish engulfing + EMA21 → ke | **47.3** | 48 | 43 | 46 | 30 | BELUM CUKUP | 15 | 141/48 | -0.96 | 16 | -0.23 | -0.03 | 4.9 | -0.22 | – | – |
| 47 | `M05` MACD Divergence + Pengesahan | **47.2** | 40 | 48 | 42 | 50 | BELUM CUKUP | 16 | 42/18 | -2.59 | 29 | +1.52 | +0.22 | 2.7 | -0.62 | -1.39 | -1.05 |
| 48 | `M102` Stockbee SLTB | **47.1** | 56 | 44 | 53 | 15 | BELUM CUKUP | 29 | 470/367 | -1.07 | 29 | -0.43 | -0.04 | 6.5 | -0.24 | +0.04 | -0.58 |
| 49 | `M80` Radge Saluran Purata Bergerak  | **47.1** | 53 | 34 | 57 | 33 | BELUM CUKUP | 28 | 317/130 | -0.82 | 29 | -2.36 | -0.22 | 5.7 | +0.27 | +1.70 | 0.39 |
| 50 | `M64` O'Neil Tiga Minggu Ketat | **46.8** | 34 | 21 | 26 | 15 | BELUM CUKUP | 3 | 3/3 | -12.60 | 29 | -3.76 | -0.84 | 3.2 | -1.26 | – | -14.58 |
| 51 | `M157` Consolidation Pivot Breakout ( | **46.6** | 46 | 42 | 32 | 15 | BELUM CUKUP | 7 | 9/3 | -1.35 | 26 | -1.10 | -0.32 | 1.9 | -0.58 | – | -1.19 |
| 52 | `M153` Range Leader | **46.5** | 58 | 38 | 52 | 18 | BELUM CUKUP | 29 | 1586/1448 | -0.48 | 29 | -2.50 | -0.19 | 8.3 | -0.37 | +0.71 | -2.36 |
| 53 | `M77` Undercut & Rally pada Purata B | **46.5** | 54 | 41 | 47 | 18 | BELUM CUKUP | 21 | 63/48 | -0.99 | 29 | -4.35 | -0.53 | 3.1 | -0.56 | +0.91 | -0.66 |
| 54 | `M138` 直升机空中加油 (Helikopter isi minyak | **46.5** | 29 | 49 | 20 | 15 | BELUM CUKUP | 4 | 4/0 | -2.88 | 22 | -1.07 | -0.47 | 0.9 | -1.19 | – | -1.72 |
| 55 | `M117` Landry Pullback (high 2 bulan) | **46.4** | 54 | 28 | 56 | 38 | BELUM CUKUP | 23 | 168/45 | -0.36 | 29 | -7.42 | -0.63 | 6.1 | +0.47 | +2.06 | 0.50 |
| 56 | `N28X16` ADX>25 + DI+ > DI- → keluar bi | **46.4** | 39 | 40 | 40 | 70 | BELUM CUKUP | 16 | 639/516 | -1.07 | 16 | -3.83 | -0.46 | 3.7 | -1.35 | – | – |
| 57 | `M124` 'Last' Stochastic Technique (C | **46.3** | 38 | 48 | 53 | 36 | BELUM CUKUP | 28 | 432/336 | -2.27 | 29 | +1.81 | +0.21 | 4.0 | -0.29 | -0.45 | -0.74 |
| 58 | `M68` Kell Base n' Break | **46.1** | 38 | 46 | 48 | 27 | BELUM CUKUP | 17 | 57/20 | -1.72 | 29 | +1.34 | +0.17 | 3.2 | +0.08 | -0.88 | 0.50 |
| 59 | `M120` Reversal New Highs | **46.1** | 50 | 38 | 46 | 16 | BELUM CUKUP | 13 | 19/13 | -1.27 | 29 | -1.71 | -0.26 | 3.8 | +0.01 | – | 0.03 |
| 60 | `M21` Marius 3 Persediaan (Pecahan+J | **46.1** | 30 | 45 | 37 | 15 | BELUM CUKUP | 6 | 7/5 | -2.23 | 21 | -1.52 | -0.57 | 1.9 | -0.08 | – | -0.10 |
| 61 | `M143` 장대양봉 이후 눌림목 / 5일선 매매 (Undur ke | **46.0** | 47 | 46 | 36 | 23 | BELUM CUKUP | 15 | 29/7 | -1.07 | 28 | -0.55 | -0.10 | 2.2 | -0.75 | – | -5.82 |
| 62 | `M115` Bow Tie (Landry) | **46.0** | 40 | 36 | 49 | 26 | BELUM CUKUP | 12 | 37/31 | -2.25 | 29 | -4.03 | -0.42 | 5.6 | +0.09 | -0.13 | 0.40 |
| 63 | `N203X36` Gap 2% lalu MA20 silang MA50 x | **45.9** | 25 | 35 | 30 | 30 | BELUM CUKUP | 5 | 13/3 | -4.39 | 9 | -5.42 | -0.52 | 5.9 | -0.64 | – | – |
| 64 | `N25X16` Supertrend + EMA + ADX>23 → ke | **45.7** | 33 | 43 | 42 | 55 | BELUM CUKUP | 14 | 127/48 | -3.46 | 16 | -0.18 | -0.04 | 2.6 | -0.76 | – | – |
| 65 | `M38` Darvas Kotak | **45.3** | 27 | 20 | 34 | 26 | BELUM CUKUP | 5 | 27/1 | -3.33 | 28 | -4.96 | -0.43 | 6.8 | +0.10 | – | 0.37 |
| 66 | `M54` IBD Power Trend | **45.2** | 41 | 48 | 52 | 15 | BELUM CUKUP | 24 | 225/143 | -1.82 | 29 | +3.36 | +0.32 | 5.8 | -0.31 | +0.07 | -0.65 |
| 67 | `N45X16` Undur EMA21 cerun positif → ke | **45.2** | 32 | 48 | 46 | 30 | BELUM CUKUP | 16 | 226/140 | -1.91 | 16 | +2.19 | +0.26 | 3.8 | -0.65 | – | – |
| 68 | `N28X36` ADX>25 + DI+ > DI- → keluar se | **45.1** | 43 | 34 | 44 | 30 | BELUM CUKUP | 16 | 593/473 | -0.70 | 16 | -7.05 | -0.53 | 5.9 | -0.84 | – | – |
| 69 | `M87` IBD Tapak Menaik | **45.1** | 36 | 36 | 42 | 15 | BELUM CUKUP | 9 | 12/8 | -2.57 | 29 | -3.06 | -0.39 | 4.7 | -0.02 | – | -0.06 |
| 70 | `M32` Momentum Burst | **45.0** | 51 | 28 | 52 | 23 | BELUM CUKUP | 18 | 73/50 | -1.11 | 29 | -4.78 | -0.33 | 8.8 | +0.10 | +0.56 | 0.21 |
| 71 | `M127` Slingshot Bullish | **44.9** | 42 | 40 | 49 | 19 | BELUM CUKUP | 20 | 112/92 | -1.78 | 29 | -4.92 | -0.51 | 4.9 | -0.54 | +1.09 | -0.68 |
| 72 | `N48X36` Inside day pecah → keluar sele | **44.8** | 46 | 30 | 44 | 30 | BELUM CUKUP | 16 | 405/280 | -0.35 | 16 | -6.82 | -0.78 | 6.0 | -0.79 | – | – |
| 73 | `M44` Tapak Rata IBD | **44.8** | 40 | 37 | 31 | 15 | BELUM CUKUP | 9 | 10/8 | -4.47 | 29 | -4.38 | -0.76 | 3.7 | -1.38 | – | -22.15 |
| 74 | `N75X17` RSI14 < 40 tanpa penapis → kel | **44.7** | 42 | 36 | 40 | 30 | BELUM CUKUP | 16 | 602/355 | -0.87 | 16 | -5.79 | -0.45 | 6.0 | -1.24 | – | – |
| 75 | `N201X36` MA20 silang MA50 atas MA50 x X | **44.6** | 26 | 37 | 33 | 30 | BELUM CUKUP | 8 | 30/8 | -2.38 | 9 | -4.36 | -0.58 | 4.2 | -0.83 | – | – |
| 76 | `M15` Break & Retest + Henti ATR | **44.5** | 50 | 29 | 56 | 24 | BELUM CUKUP | 28 | 334/295 | -0.60 | 29 | -9.26 | -0.60 | 7.2 | +0.05 | +1.58 | 0.11 |
| 77 | `M150` Trend Bar Failure (Brooks) | **44.4** | 43 | 36 | 52 | 21 | BELUM CUKUP | 24 | 120/96 | -1.26 | 29 | -5.82 | -0.60 | 4.8 | -0.28 | +1.60 | -1.05 |
| 78 | `M132` Ascending Scallop (Bulkowski) | **44.4** | 36 | 48 | 52 | 13 | BELUM CUKUP | 20 | 99/52 | -2.15 | 29 | +1.57 | +0.20 | 3.4 | -0.01 | -0.47 | -0.06 |
| 79 | `N65X14` Gap 4% + volum + hampir 52w →  | **44.4** | 29 | 24 | 33 | 30 | BELUM CUKUP | 7 | 34/10 | -2.83 | 16 | -3.19 | -0.38 | 4.1 | -0.87 | – | – |
| 80 | `N65X36` Gap 4% + volum + hampir 52w →  | **44.4** | 29 | 25 | 32 | 30 | BELUM CUKUP | 7 | 34/6 | -2.49 | 16 | -2.80 | -0.36 | 3.9 | -0.82 | – | – |
| 81 | `M12` Parabolic SAR | **43.9** | 39 | 49 | 52 | 12 | BELUM CUKUP | 29 | 449/299 | -1.94 | 29 | +1.09 | +0.17 | 3.3 | -0.37 | -0.87 | -0.83 |
| 82 | `N64X17` Episodic pivot → keluar bila a | **43.9** | 31 | 29 | 37 | 30 | BELUM CUKUP | 10 | 56/18 | -2.00 | 16 | -1.22 | -0.15 | 4.0 | -0.72 | – | – |
| 83 | `M106` DMI Wilder | **43.8** | 43 | 40 | 52 | 13 | BELUM CUKUP | 25 | 147/113 | -1.56 | 29 | -2.43 | -0.32 | 3.5 | -0.35 | -0.63 | -0.90 |
| 84 | `M130` 多方炮 (dua lilin hijau mengapit  | **43.8** | 29 | 24 | 40 | 18 | BELUM CUKUP | 8 | 12/5 | -2.43 | 27 | -2.71 | -0.27 | 5.0 | +0.11 | – | 0.11 |
| 85 | `N64X14` Episodic pivot → keluar bila r | **43.7** | 30 | 28 | 37 | 30 | BELUM CUKUP | 10 | 56/19 | -2.51 | 16 | -1.90 | -0.23 | 3.6 | -0.74 | – | – |
| 86 | `N43X36` Undur EMA8 + penapis MA50 → ke | **43.5** | 32 | 35 | 43 | 30 | BELUM CUKUP | 16 | 289/115 | -1.74 | 16 | -2.92 | -0.40 | 3.7 | -0.93 | – | – |
| 87 | `N68X16` Bullish engulfing + EMA21 → ke | **43.5** | 34 | 31 | 45 | 30 | BELUM CUKUP | 15 | 139/56 | -1.54 | 16 | -2.87 | -0.24 | 6.9 | -0.44 | – | – |
| 88 | `N64X16` Episodic pivot → keluar bila s | **43.5** | 28 | 28 | 38 | 30 | BELUM CUKUP | 10 | 56/22 | -2.19 | 16 | -1.98 | -0.25 | 3.6 | -0.68 | – | – |
| 89 | `N36X36` Pocket pivot → keluar selepas  | **43.4** | 35 | 32 | 39 | 38 | BELUM CUKUP | 16 | 195/120 | -2.88 | 16 | -1.88 | -0.20 | 4.5 | -1.37 | – | – |
| 90 | `N37X17` Gap and go → keluar bila adx14 | **43.4** | 34 | 31 | 38 | 30 | BELUM CUKUP | 13 | 94/40 | -2.95 | 16 | -0.43 | -0.05 | 4.1 | -1.13 | – | – |
| 91 | `N64X36` Episodic pivot → keluar selepa | **43.4** | 29 | 27 | 37 | 30 | BELUM CUKUP | 10 | 56/16 | -2.22 | 16 | -1.86 | -0.21 | 4.2 | -0.69 | – | – |
| 92 | `M121` High 2 bull flag (Brooks) | **43.3** | 24 | 18 | 24 | 15 | BELUM CUKUP | 6 | 9/3 | -5.61 | 25 | -4.94 | -0.64 | 5.0 | -1.39 | – | -13.28 |
| 93 | `M107` Golden Cross SMA50/200 | **43.1** | 40 | 34 | 47 | 19 | BELUM CUKUP | 22 | 47/14 | -1.29 | 29 | -3.25 | -0.31 | 4.5 | -0.08 | +1.04 | -0.12 |
| 94 | `N119X13` 3 tutup turun berturut → kelua | **43.1** | 38 | 25 | 40 | 30 | BELUM CUKUP | 14 | 289/73 | -0.78 | 16 | -7.83 | -0.71 | 7.6 | -1.12 | – | – |
| 95 | `N66X36` 52w tinggi + pengesahan 1% → k | **43.1** | 27 | 23 | 34 | 30 | BELUM CUKUP | 9 | 42/7 | -3.03 | 15 | -3.25 | -0.39 | 4.5 | -0.76 | – | – |
| 96 | `M149` 3-Step Pullback | **43.0** | 41 | 33 | 56 | 17 | BELUM CUKUP | 27 | 275/113 | -1.44 | 29 | -2.86 | -0.24 | 6.8 | +0.08 | -0.08 | 0.07 |
| 97 | `M116` 2/20 EMA Breakout (Landry) | **42.9** | 47 | 31 | 52 | 15 | BELUM CUKUP | 29 | 640/573 | -1.00 | 29 | -2.33 | -0.17 | 8.5 | -0.35 | -0.09 | -1.63 |
| 98 | `N75X14` RSI14 < 40 tanpa penapis → kel | **42.9** | 37 | 28 | 40 | 30 | BELUM CUKUP | 16 | 402/80 | -1.12 | 16 | -5.71 | -0.60 | 5.1 | -1.21 | – | – |
| 99 | `N37X36` Gap and go → keluar selepas DU | **42.9** | 32 | 29 | 37 | 30 | BELUM CUKUP | 13 | 94/44 | -3.31 | 16 | -1.17 | -0.15 | 3.8 | -1.19 | – | – |
| 100 | `M105` Supertrend tulen | **42.8** | 37 | 37 | 54 | 15 | BELUM CUKUP | 25 | 379/230 | -2.32 | 29 | -0.06 | -0.00 | 6.0 | -0.05 | +0.02 | -0.16 |
| 101 | `N07X16` Tiga MA tersusun → keluar bila | **42.8** | 28 | 35 | 44 | 30 | BELUM CUKUP | 16 | 182/79 | -2.61 | 16 | -2.36 | -0.39 | 3.2 | -0.75 | – | – |
| 102 | `N16X13` RSI2<10 tanpa penapis → keluar | **42.8** | 40 | 26 | 35 | 30 | BELUM CUKUP | 15 | 314/7 | -0.51 | 16 | -9.70 | -0.72 | 8.6 | -0.87 | – | – |
| 103 | `N53X17` Supertrend + ADX>25 → keluar b | **42.8** | 29 | 30 | 41 | 30 | BELUM CUKUP | 13 | 112/21 | -3.09 | 16 | -2.47 | -0.23 | 6.1 | -0.52 | – | – |
| 104 | `M126` Hidden Smash Day (beli, Larry  | **42.7** | 30 | 35 | 40 | 15 | BELUM CUKUP | 13 | 21/11 | -2.11 | 28 | -3.67 | -0.46 | 5.2 | -0.35 | – | -0.45 |
| 105 | `N09X36` Undur EMA10 + penapis EMA50 →  | **42.6** | 29 | 34 | 42 | 30 | BELUM CUKUP | 16 | 304/134 | -1.98 | 16 | -3.26 | -0.43 | 3.8 | -1.04 | – | – |
| 106 | `N22X36` BB pecah atas + RSI → keluar s | **42.6** | 30 | 29 | 43 | 30 | BELUM CUKUP | 15 | 124/76 | -4.46 | 16 | -4.33 | -0.37 | 5.9 | -0.76 | – | – |
| 107 | `M144` Screw Bar | **42.6** | 19 | 29 | 33 | 15 | BELUM CUKUP | 8 | 29/26 | -5.60 | 27 | -8.43 | -0.96 | 2.5 | -1.31 | – | -2.00 |
| 108 | `M49` Ichimoku (Tutup Atas Awan + Te | **42.4** | 40 | 39 | 49 | 13 | BELUM CUKUP | 29 | 373/263 | -2.00 | 29 | -1.34 | -0.12 | 5.0 | -0.76 | -0.62 | -1.12 |
| 109 | `M111` Sistem Volatiliti Wilder | **42.4** | 36 | 38 | 55 | 12 | BELUM CUKUP | 27 | 280/174 | -2.11 | 29 | +0.51 | +0.05 | 5.1 | -0.03 | -0.70 | -0.09 |
| 110 | `M36` Turtle 55/20 | **42.4** | 39 | 32 | 54 | 16 | BELUM CUKUP | 26 | 353/230 | -1.90 | 29 | -2.29 | -0.16 | 7.9 | -0.12 | +0.29 | -0.27 |
| 111 | `N25X17` Supertrend + EMA + ADX>23 → ke | **42.4** | 27 | 29 | 38 | 30 | BELUM CUKUP | 13 | 121/37 | -3.81 | 16 | -3.48 | -0.48 | 3.6 | -0.98 | – | – |
| 112 | `M119` 180 Bullish (Cooper) | **42.3** | 39 | 31 | 50 | 19 | BELUM CUKUP | 25 | 193/111 | -1.49 | 29 | -5.53 | -0.51 | 6.3 | -0.58 | +0.98 | -1.56 |
| 113 | `M135` 3rd Watch | **42.3** | 27 | 21 | 35 | 15 | BELUM CUKUP | 9 | 15/7 | -7.61 | 29 | -3.72 | -0.44 | 4.9 | -0.89 | – | -5.19 |
| 114 | `M04` BB Squeeze Breakout | **42.2** | 35 | 31 | 54 | 18 | BELUM CUKUP | 22 | 157/90 | -2.62 | 29 | +0.30 | +0.03 | 5.6 | +0.08 | -0.30 | 0.12 |
| 115 | `N51X16` BB squeeze + Supertrend → kelu | **42.2** | 22 | 34 | 26 | 30 | BELUM CUKUP | 10 | 16/4 | -3.14 | 16 | -5.13 | -0.62 | 4.4 | -1.54 | – | – |
| 116 | `M34` Carter TTM Squeeze | **42.1** | 42 | 28 | 52 | 14 | BELUM CUKUP | 23 | 108/66 | -1.70 | 29 | -3.45 | -0.27 | 6.2 | -0.17 | -0.20 | -0.45 |
| 117 | `N33X36` Donchian20 + penapis MA200 → k | **42.1** | 27 | 22 | 36 | 30 | BELUM CUKUP | 11 | 102/53 | -4.79 | 16 | -5.56 | -0.64 | 4.5 | -1.29 | – | – |
| 118 | `M67` Rayner Teo: Ujian Ketiga pada  | **42.0** | 39 | 31 | 43 | 15 | BELUM CUKUP | 20 | 36/28 | -2.62 | 29 | -4.98 | -0.42 | 7.5 | -0.79 | – | -2.95 |
| 119 | `N40X36` OBV tinggi baharu + MA50 → kel | **41.9** | 42 | 17 | 48 | 30 | BELUM CUKUP | 16 | 92/35 | -0.74 | 16 | -10.20 | -0.70 | 8.5 | +0.06 | – | – |
| 120 | `N33X16` Donchian20 + penapis MA200 → k | **41.9** | 26 | 22 | 36 | 30 | BELUM CUKUP | 11 | 106/58 | -6.07 | 16 | -4.29 | -0.60 | 3.4 | -1.35 | – | – |
| 121 | `M89` Chande 65sma-3cc | **41.8** | 38 | 34 | 51 | 12 | BELUM CUKUP | 25 | 199/153 | -3.01 | 29 | -3.04 | -0.28 | 5.8 | -0.42 | -0.67 | -1.30 |
| 122 | `N38X36` VCP pecah → keluar selepas DUA | **41.8** | 27 | 34 | 36 | 30 | BELUM CUKUP | 16 | 52/26 | -2.35 | 16 | -4.49 | -0.55 | 4.1 | -1.26 | – | – |
| 123 | `N57X36` ADX bangkit daripada <20 → kel | **41.8** | 28 | 26 | 35 | 30 | BELUM CUKUP | 13 | 80/26 | -5.36 | 16 | -2.03 | -0.25 | 4.4 | -1.21 | – | – |
| 124 | `N124X36` Episodic pivot gap 8-10% → kel | **41.8** | 28 | 23 | 34 | 30 | BELUM CUKUP | 12 | 56/30 | -3.13 | 16 | -6.58 | -0.55 | 6.2 | -1.38 | – | – |
| 125 | `M88` O'Neil Shakeout +3 | **41.7** | 36 | 35 | 45 | 14 | BELUM CUKUP | 22 | 101/77 | -5.10 | 29 | -3.52 | -0.23 | 7.9 | -0.97 | -0.27 | -1.62 |
| 126 | `M92` CCI-50 | **41.6** | 39 | 32 | 50 | 16 | BELUM CUKUP | 29 | 634/538 | -1.35 | 29 | -6.75 | -0.50 | 6.1 | -0.63 | +0.38 | -1.29 |
| 127 | `M91` Stochastic Pop (Bernstein/Stec | **41.6** | 37 | 21 | 50 | 17 | BELUM CUKUP | 16 | 39/34 | -3.79 | 29 | -2.14 | -0.13 | 8.1 | +0.06 | -1.33 | 0.22 |
| 128 | `N08X36` tutup>EMA20 tidak terlalu jauh | **41.6** | 26 | 33 | 36 | 30 | BELUM CUKUP | 16 | 519/412 | -2.17 | 16 | -5.79 | -0.61 | 4.8 | -1.69 | – | – |
| 129 | `N24X36` Supertrend(10,3) + ADX>20 → ke | **41.6** | 31 | 24 | 43 | 30 | BELUM CUKUP | 16 | 190/122 | -2.66 | 16 | -5.60 | -0.58 | 4.7 | -0.92 | – | – |
| 130 | `M50` Elder Triple Screen | **41.5** | 42 | 28 | 52 | 16 | BELUM CUKUP | 29 | 678/527 | -1.36 | 29 | -9.01 | -0.65 | 7.9 | -0.44 | +0.30 | -0.77 |
| 131 | `N40X16` OBV tinggi baharu + MA50 → kel | **41.5** | 40 | 16 | 49 | 30 | BELUM CUKUP | 16 | 111/55 | -0.67 | 16 | -11.08 | -0.68 | 8.5 | -0.01 | – | – |
| 132 | `N41X36` CMF20>0 + tutup>EMA20 → keluar | **41.5** | 27 | 29 | 38 | 30 | BELUM CUKUP | 15 | 294/235 | -2.55 | 16 | -6.89 | -0.80 | 5.0 | -1.55 | – | – |
| 133 | `N33X14` Donchian20 + penapis MA200 → k | **41.4** | 29 | 19 | 36 | 30 | BELUM CUKUP | 12 | 117/41 | -5.78 | 16 | -4.13 | -0.68 | 3.6 | -1.29 | – | – |
| 134 | `M136` Short/Intermediate-term Low (L | **41.3** | 34 | 36 | 48 | 17 | BELUM CUKUP | 29 | 961/539 | -3.43 | 29 | -3.49 | -0.33 | 4.5 | -0.85 | +0.49 | -0.51 |
| 135 | `M26` Garis Trend Undur 3 Sentuhan + | **41.3** | 35 | 32 | 46 | 17 | BELUM CUKUP | 23 | 94/64 | -1.35 | 29 | -6.15 | -0.60 | 5.1 | -0.86 | +0.55 | -1.14 |
| 136 | `N07X36` Tiga MA tersusun → keluar sele | **41.3** | 26 | 28 | 42 | 30 | BELUM CUKUP | 16 | 177/66 | -3.06 | 16 | -4.17 | -0.52 | 4.5 | -0.83 | – | – |
| 137 | `N55X13` BB + RSI + ADX>20 → keluar bil | **41.1** | 42 | 24 | 25 | 30 | BELUM CUKUP | 16 | 151/0 | -0.63 | 16 | -7.61 | -0.84 | 5.8 | -1.14 | – | – |
| 138 | `M156` Single Penetration (DiNapoli) | **41.0** | 43 | 27 | 50 | 15 | BELUM CUKUP | 28 | 309/240 | -1.13 | 29 | -5.98 | -0.41 | 8.4 | -0.65 | +0.03 | -1.93 |
| 139 | `M14` Walking with the Whales | **40.9** | 45 | 25 | 50 | 16 | BELUM CUKUP | 29 | 1142/910 | -0.98 | 29 | -11.22 | -0.68 | 9.3 | -0.56 | +0.14 | -0.98 |
| 140 | `M134` First Kiss After Daylight (Lan | **40.9** | 31 | 31 | 50 | 16 | BELUM CUKUP | 22 | 70/41 | -2.71 | 29 | -4.68 | -0.42 | 5.8 | -0.19 | +0.13 | -0.24 |
| 141 | `N35X36` Pecah 52 minggu tinggi → kelua | **40.9** | 24 | 22 | 32 | 30 | BELUM CUKUP | 12 | 56/11 | -4.41 | 16 | -3.63 | -0.58 | 3.0 | -1.27 | – | – |
| 142 | `N57X16` ADX bangkit daripada <20 → kel | **40.8** | 25 | 23 | 38 | 30 | BELUM CUKUP | 14 | 78/41 | -5.41 | 16 | -3.47 | -0.39 | 4.8 | -1.08 | – | – |
| 143 | `N31X36` Turtle sistem 2 → keluar selep | **40.8** | 25 | 19 | 36 | 30 | BELUM CUKUP | 12 | 107/27 | -4.49 | 16 | -5.63 | -0.57 | 4.9 | -1.11 | – | – |
| 144 | `N42X36` Lonjakan volum 2x → keluar sel | **40.7** | 31 | 20 | 41 | 30 | BELUM CUKUP | 16 | 243/160 | -1.54 | 16 | -8.23 | -0.77 | 6.2 | -1.15 | – | – |
| 145 | `N53X16` Supertrend + ADX>25 → keluar b | **40.7** | 23 | 22 | 44 | 30 | BELUM CUKUP | 14 | 121/50 | -3.27 | 16 | -7.33 | -0.68 | 6.7 | -0.50 | – | – |
| 146 | `N19X13` Bawah jalur BB + RSI<30 → kelu | **40.7** | 24 | 26 | 25 | 30 | BELUM CUKUP | 12 | 145/0 | -3.35 | 16 | -5.17 | -0.67 | 4.4 | -1.06 | – | – |
| 147 | `N51X36` BB squeeze + Supertrend → kelu | **40.7** | 19 | 24 | 21 | 30 | BELUM CUKUP | 10 | 16/6 | -4.38 | 16 | -6.88 | -0.81 | 4.7 | -2.27 | – | – |
| 148 | `M73` ADX(5) > 40 + Julat Terkecil 6 | **40.6** | 41 | 26 | 50 | 15 | BELUM CUKUP | 29 | 1236/1080 | -0.48 | 29 | -9.24 | -0.74 | 7.7 | -0.62 | +0.04 | -3.63 |
| 149 | `M148` Natural Number Method | **40.6** | 35 | 38 | 46 | 9 | BELUM CUKUP | 28 | 242/224 | -2.59 | 29 | -3.19 | -0.30 | 5.1 | -1.01 | -1.52 | -4.11 |
| 150 | `N24X17` Supertrend(10,3) + ADX>20 → ke | **40.5** | 25 | 22 | 37 | 30 | BELUM CUKUP | 14 | 136/61 | -4.96 | 16 | -4.27 | -0.44 | 4.6 | -1.40 | – | – |
| 151 | `N75X13` RSI14 < 40 tanpa penapis → kel | **40.4** | 32 | 23 | 30 | 30 | BELUM CUKUP | 16 | 214/1 | -1.26 | 16 | -7.79 | -0.67 | 5.9 | -0.89 | – | – |
| 152 | `N113X36` 80-20 bar (sisi beli) → keluar | **40.4** | 32 | 18 | 41 | 30 | BELUM CUKUP | 16 | 437/331 | -1.02 | 16 | -11.74 | -0.87 | 9.2 | -1.15 | – | – |
| 153 | `M57` Landry Trend Knockout (TKO) | **40.3** | 39 | 32 | 45 | 11 | BELUM CUKUP | 29 | 203/158 | -2.22 | 29 | -4.74 | -0.54 | 4.9 | -1.22 | -1.07 | -3.10 |
| 154 | `M152` Spike & Ledge | **40.3** | 29 | 35 | 43 | 16 | BELUM CUKUP | 23 | 57/15 | -3.86 | 29 | -2.03 | -0.16 | 5.4 | -0.60 | +0.13 | -1.66 |
| 155 | `M140` 猎豹出击 (Serangan Cheetah) | **40.3** | 27 | 26 | 35 | 14 | BELUM CUKUP | 14 | 46/26 | -3.98 | 29 | -6.17 | -0.66 | 5.2 | -1.56 | -0.24 | -1.54 |
| 156 | `N37X16` Gap and go → keluar bila super | **40.3** | 24 | 19 | 37 | 30 | BELUM CUKUP | 13 | 94/52 | -3.68 | 16 | -4.97 | -0.70 | 3.7 | -1.31 | – | – |
| 157 | `N37X14` Gap and go → keluar bila rsi14 | **40.3** | 25 | 18 | 36 | 30 | BELUM CUKUP | 13 | 93/33 | -4.57 | 16 | -5.62 | -0.42 | 6.5 | -1.28 | – | – |
| 158 | `M139` 均线首次粘合向上发散 (MA berhimpun kali  | **40.2** | 30 | 35 | 47 | 13 | BELUM CUKUP | 25 | 102/58 | -4.09 | 29 | -0.78 | -0.07 | 5.3 | -0.67 | -0.59 | -2.20 |
| 159 | `N24X16` Supertrend(10,3) + ADX>20 → ke | **40.2** | 23 | 20 | 38 | 30 | BELUM CUKUP | 14 | 128/62 | -5.42 | 16 | -4.74 | -0.51 | 4.7 | -1.24 | – | – |
| 160 | `N80X36` Tinggi sepanjang masa → keluar | **40.2** | 21 | 16 | 32 | 30 | BELUM CUKUP | 11 | 42/9 | -5.18 | 16 | -5.74 | -0.82 | 3.8 | -1.16 | – | – |
| 161 | `N76X36` Tutup > MA50 (penapis trend tu | **40.1** | 23 | 24 | 41 | 30 | BELUM CUKUP | 16 | 245/154 | -2.53 | 16 | -9.57 | -0.82 | 6.7 | -1.21 | – | – |
| 162 | `N16X15` RSI2<10 tanpa penapis → ekori  | **40.1** | 33 | 20 | 27 | 30 | BELUM CUKUP | 15 | 286/0 | -0.74 | 16 | -11.76 | -0.75 | 10.8 | -0.93 | – | – |
| 163 | `M66` IBD Undur Pertama ke Purata 50 | **40.0** | 38 | 27 | 50 | 13 | BELUM CUKUP | 28 | 321/212 | -1.70 | 29 | -4.92 | -0.38 | 8.2 | -0.59 | -0.44 | -1.42 |
| 164 | `N113X16` 80-20 bar (sisi beli) → keluar | **40.0** | 35 | 14 | 42 | 30 | BELUM CUKUP | 16 | 467/352 | -0.80 | 16 | -12.01 | -0.84 | 9.9 | -1.06 | – | – |
| 165 | `N36X16` Pocket pivot → keluar bila sup | **40.0** | 25 | 22 | 39 | 30 | BELUM CUKUP | 16 | 202/123 | -3.22 | 16 | -5.72 | -0.52 | 5.1 | -1.35 | – | – |
| 166 | `N119X15` 3 tutup turun berturut → ekori | **40.0** | 18 | 13 | 21 | 30 | BELUM CUKUP | 9 | 58/0 | -3.26 | 16 | -7.77 | -0.68 | 6.8 | -1.37 | – | – |
| 167 | `N75X15` RSI14 < 40 tanpa penapis → eko | **39.9** | 31 | 23 | 28 | 30 | BELUM CUKUP | 16 | 208/0 | -1.38 | 16 | -7.79 | -0.67 | 5.9 | -0.89 | – | – |
| 168 | `N54X16` Supertrend + RSI>50 → keluar b | **39.8** | 21 | 16 | 34 | 30 | BELUM CUKUP | 12 | 130/72 | -6.73 | 16 | -5.53 | -0.60 | 5.9 | -1.76 | – | – |
| 169 | `M06` Minervini VCP Breakout | **39.6** | 31 | 31 | 46 | 12 | BELUM CUKUP | 25 | 93/60 | -3.50 | 29 | -4.38 | -0.47 | 4.6 | -0.83 | -0.90 | -2.12 |
| 170 | `N56X36` RSI>50 + ADX>20 → keluar selep | **39.5** | 23 | 21 | 39 | 30 | BELUM CUKUP | 16 | 223/150 | -2.70 | 16 | -9.51 | -0.72 | 7.6 | -1.38 | – | – |
| 171 | `N73X13` Tutup bawah jalur bawah BB(20, | **39.5** | 26 | 23 | 29 | 30 | BELUM CUKUP | 16 | 230/1 | -1.68 | 16 | -7.42 | -0.64 | 6.6 | -0.93 | – | – |
| 172 | `N124X15` Episodic pivot gap 8-10% → eko | **39.5** | 23 | 17 | 25 | 30 | BELUM CUKUP | 12 | 55/0 | -4.27 | 16 | -6.72 | -0.49 | 6.5 | -1.05 | – | – |
| 173 | `M99` Three Line Break | **39.3** | 33 | 29 | 49 | 12 | BELUM CUKUP | 27 | 204/145 | -3.11 | 29 | -3.78 | -0.30 | 5.9 | -0.70 | -0.89 | -2.50 |
| 174 | `M95` Nisbah Kebaharuan High 52 Ming | **39.3** | 28 | 27 | 50 | 15 | BELUM CUKUP | 23 | 134/83 | -2.03 | 29 | -8.17 | -0.65 | 7.1 | -0.42 | +0.08 | -0.88 |
| 175 | `N56X17` RSI>50 + ADX>20 → keluar bila  | **39.3** | 23 | 19 | 36 | 30 | BELUM CUKUP | 15 | 154/75 | -5.01 | 16 | -5.54 | -0.59 | 4.6 | -1.58 | – | – |
| 176 | `N27X16` Ichimoku atas awan → keluar bi | **39.2** | 20 | 22 | 40 | 30 | BELUM CUKUP | 16 | 221/135 | -2.00 | 16 | -8.05 | -0.83 | 5.1 | -1.26 | – | – |
| 177 | `N76X16` Tutup > MA50 (penapis trend tu | **39.2** | 19 | 26 | 37 | 30 | BELUM CUKUP | 16 | 450/344 | -2.16 | 16 | -7.09 | -0.77 | 4.3 | -1.60 | – | – |
| 178 | `N22X14` BB pecah atas + RSI → keluar b | **39.2** | 23 | 17 | 39 | 30 | BELUM CUKUP | 15 | 131/55 | -5.83 | 16 | -7.70 | -0.63 | 6.7 | -1.15 | – | – |
| 179 | `M29` EMA3 + RSI75 + Stokastik | **39.1** | 39 | 26 | 43 | 4 | BELUM CUKUP | 21 | 65/38 | -1.17 | 29 | -9.91 | -0.72 | 8.7 | -0.90 | -2.81 | -4.10 |
| 180 | `N45X36` Undur EMA21 cerun positif → ke | **39.1** | 20 | 20 | 40 | 30 | BELUM CUKUP | 15 | 168/98 | -3.36 | 16 | -8.66 | -0.74 | 6.1 | -1.25 | – | – |
| 181 | `N41X16` CMF20>0 + tutup>EMA20 → keluar | **39.0** | 20 | 23 | 38 | 30 | BELUM CUKUP | 16 | 347/273 | -2.98 | 16 | -7.13 | -0.71 | 5.3 | -1.52 | – | – |
| 182 | `N42X16` Lonjakan volum 2x → keluar bil | **39.0** | 24 | 16 | 41 | 30 | BELUM CUKUP | 16 | 248/168 | -1.76 | 16 | -9.49 | -0.89 | 6.5 | -1.17 | – | – |
| 183 | `N56X16` RSI>50 + ADX>20 → keluar bila  | **38.9** | 18 | 22 | 42 | 30 | BELUM CUKUP | 16 | 270/186 | -2.50 | 16 | -7.75 | -0.74 | 5.7 | -1.06 | – | – |
| 184 | `M31` Band Walk (BB 20/2) | **38.7** | 38 | 16 | 55 | 20 | BELUM CUKUP | 26 | 405/204 | -1.45 | 29 | -6.49 | -0.40 | 9.4 | +0.04 | +0.79 | 0.08 |
| 185 | `M141` First Thrust (Landry) | **38.7** | 12 | 7 | 35 | 15 | BELUM CUKUP | 9 | 27/18 | -6.95 | 29 | -14.27 | -0.76 | 8.8 | -1.15 | – | -4.23 |
| 186 | `N39X36` NR7 kemudian pecah → keluar se | **38.7** | 12 | 6 | 30 | 30 | BELUM CUKUP | 9 | 36/12 | -5.22 | 15 | -11.75 | -0.77 | 9.2 | -1.42 | – | – |
| 187 | `M02` MACD + SMA200 | **38.6** | 34 | 21 | 45 | 26 | BELUM CUKUP | 29 | 146/128 | -3.99 | 29 | -4.66 | -0.29 | 7.2 | -1.24 | -0.03 | -7.88 |
| 188 | `M55` Guppy GMMA | **38.6** | 31 | 25 | 49 | 14 | BELUM CUKUP | 27 | 320/200 | -1.88 | 29 | -7.75 | -0.67 | 6.4 | -0.66 | -0.34 | -1.63 |
| 189 | `M11` NR7 Breakout + Volume | **38.6** | 35 | 22 | 50 | 13 | BELUM CUKUP | 26 | 141/101 | -0.83 | 29 | -11.72 | -0.68 | 9.9 | -0.62 | -0.48 | -0.64 |
| 190 | `N36X14` Pocket pivot → keluar bila rsi | **38.6** | 24 | 16 | 37 | 30 | BELUM CUKUP | 16 | 197/74 | -4.19 | 16 | -6.38 | -0.63 | 5.7 | -1.47 | – | – |
| 191 | `M59` Anjakan Julat RSI | **38.6** | 26 | 21 | 43 | 3 | BELUM CUKUP | 14 | 36/24 | -6.02 | 29 | -4.90 | -0.47 | 5.8 | -0.59 | -3.13 | -1.87 |
| 192 | `N22X16` BB pecah atas + RSI → keluar b | **38.5** | 20 | 13 | 41 | 30 | BELUM CUKUP | 14 | 124/81 | -6.31 | 16 | -7.80 | -0.74 | 6.0 | -0.99 | – | – |
| 193 | `N08X16` tutup>EMA20 tidak terlalu jauh | **38.3** | 16 | 24 | 37 | 30 | BELUM CUKUP | 16 | 611/496 | -2.22 | 16 | -10.03 | -0.86 | 5.5 | -1.63 | – | – |
| 194 | `N42X14` Lonjakan volum 2x → keluar bil | **38.3** | 24 | 14 | 41 | 30 | BELUM CUKUP | 16 | 220/59 | -2.67 | 16 | -8.09 | -0.66 | 6.9 | -0.94 | – | – |
| 195 | `N29X36` PSAR naik + tutup>MA50 → kelua | **37.9** | 19 | 16 | 35 | 30 | BELUM CUKUP | 15 | 191/124 | -3.98 | 16 | -12.12 | -0.83 | 10.2 | -1.89 | – | – |
| 196 | `N28X17` ADX>25 + DI+ > DI- → keluar bi | **37.7** | 20 | 17 | 32 | 30 | BELUM CUKUP | 16 | 175/19 | -4.01 | 16 | -6.70 | -0.55 | 6.4 | -1.51 | – | – |
| 197 | `M155` Market Cycle Strategy | **37.5** | 30 | 24 | 44 | 16 | BELUM CUKUP | 29 | 814/631 | -4.63 | 29 | -5.81 | -0.50 | 5.9 | -1.35 | +0.15 | -3.34 |
| 198 | `N74X16` MACD atas garis isyarat (keada | **37.4** | 14 | 20 | 36 | 30 | BELUM CUKUP | 16 | 811/706 | -1.91 | 16 | -12.36 | -0.90 | 7.0 | -1.77 | – | – |
| 199 | `M101` Bulkowski: Tiga lembah menaik | **37.3** | 24 | 15 | 49 | 12 | BELUM CUKUP | 18 | 47/29 | -3.11 | 29 | -8.69 | -0.58 | 9.4 | -0.07 | -0.84 | -0.18 |
| 200 | `N27X36` Ichimoku atas awan → keluar se | **37.3** | 18 | 13 | 36 | 30 | BELUM CUKUP | 15 | 131/53 | -4.09 | 16 | -10.06 | -0.79 | 6.8 | -1.50 | – | – |
| 201 | `N50X14` Mampat + pecah volum 1.5x → ke | **37.3** | 17 | 10 | 32 | 30 | BELUM CUKUP | 13 | 37/11 | -3.07 | 16 | -10.70 | -0.76 | 7.6 | -1.25 | – | – |
| 202 | `M125` 2-Bar Breakout | **37.2** | 30 | 23 | 47 | 13 | BELUM CUKUP | 29 | 1176/685 | -3.93 | 29 | -7.36 | -0.50 | 6.6 | -0.96 | -0.61 | -0.53 |
| 203 | `N47X16` NR7 + EMA9>EMA21 → keluar bila | **37.2** | 15 | 17 | 40 | 30 | BELUM CUKUP | 16 | 213/111 | -3.26 | 16 | -11.10 | -0.80 | 8.2 | -1.25 | – | – |
| 204 | `N42X15` Lonjakan volum 2x → ekori Chan | **37.0** | 21 | 15 | 26 | 30 | BELUM CUKUP | 16 | 204/0 | -3.27 | 16 | -9.17 | -0.68 | 7.4 | -1.02 | – | – |
| 205 | `N28X14` ADX>25 + DI+ > DI- → keluar bi | **36.9** | 16 | 14 | 38 | 30 | BELUM CUKUP | 16 | 254/71 | -3.68 | 16 | -9.62 | -0.64 | 7.6 | -1.40 | – | – |
| 206 | `M47` Holy Grail Raschke | **36.8** | 21 | 21 | 34 | 15 | BELUM CUKUP | 19 | 51/37 | -1.98 | 29 | -9.84 | -0.78 | 7.6 | -1.85 | – | -15.24 |
| 207 | `M19` Sneaky Pivot (proksi harian) | **36.6** | 24 | 25 | 46 | 13 | BELUM CUKUP | 27 | 503/361 | -4.11 | 29 | -6.98 | -0.47 | 6.9 | -1.07 | -0.58 | -13.93 |
| 208 | `N50X17` Mampat + pecah volum 1.5x → ke | **36.4** | 14 | 8 | 32 | 30 | BELUM CUKUP | 13 | 36/8 | -3.07 | 16 | -11.64 | -0.74 | 8.8 | -1.17 | – | – |
| 209 | `N54X36` Supertrend + RSI>50 → keluar s | **35.8** | 16 | 8 | 35 | 30 | BELUM CUKUP | 15 | 207/143 | -3.61 | 16 | -13.86 | -0.97 | 9.6 | -1.82 | – | – |
| 210 | `N29X16` PSAR naik + tutup>MA50 → kelua | **35.7** | 13 | 12 | 35 | 30 | BELUM CUKUP | 16 | 258/183 | -4.01 | 16 | -11.27 | -0.95 | 7.2 | -1.85 | – | – |
| 211 | `M154` HOLP (High of Low Period) | **35.4** | 18 | 18 | 42 | 13 | BELUM CUKUP | 21 | 128/53 | -3.30 | 29 | -11.05 | -0.72 | 8.9 | -1.11 | -0.56 | -4.34 |
| 212 | `M79` Radge: 20% Flipper | **35.2** | 23 | 21 | 43 | 12 | BELUM CUKUP | 28 | 430/256 | -5.75 | 29 | -8.34 | -0.52 | 8.6 | -1.44 | -0.78 | -2.86 |
| 213 | `N42X17` Lonjakan volum 2x → keluar bil | **35.1** | 14 | 7 | 43 | 30 | BELUM CUKUP | 16 | 238/89 | -2.10 | 16 | -13.52 | -0.91 | 8.9 | -0.92 | – | – |
| 214 | `N47X36` NR7 + EMA9>EMA21 → keluar sele | **35.1** | 9 | 11 | 37 | 30 | BELUM CUKUP | 15 | 192/83 | -3.98 | 16 | -16.08 | -0.82 | 11.6 | -1.58 | – | – |
| 215 | `M161` EMA 10/21 + Supertrend (10,3) | **35.0** | 26 | 14 | 52 | 18 | BELUM CUKUP | 29 | 570/392 | -1.36 | 29 | -16.42 | -0.74 | 12.7 | -0.33 | +0.85 | -0.76 |
| 216 | `M122` Moving Momentum (ChartSchool) | **33.9** | 24 | 18 | 37 | 9 | BELUM CUKUP | 28 | 124/84 | -4.97 | 29 | -12.21 | -0.73 | 8.5 | -2.08 | -1.48 | -5.95 |
| 217 | `M03` BB Break + Divergence RSI | **33.8** | 16 | 22 | 46 | 14 | BELUM CUKUP | 29 | 502/421 | -2.44 | 29 | -10.98 | -0.74 | 6.7 | -1.11 | -0.23 | -4.29 |
| 218 | `M76` Undercut & Rally pada Low Pent | **33.6** | 18 | 19 | 42 | 7 | BELUM CUKUP | 25 | 99/85 | -2.69 | 29 | -12.27 | -0.83 | 8.6 | -1.44 | -2.15 | -5.31 |
| 219 | `M147` Improved Three-Bar Pullback | **33.6** | 13 | 13 | 36 | 10 | BELUM CUKUP | 19 | 125/64 | -5.96 | 29 | -15.82 | -0.74 | 9.8 | -1.86 | -1.38 | -1.65 |
| 220 | `M81` Bensdorp Long Trend High Momen | **33.4** | 2 | 6 | 43 | 16 | BELUM CUKUP | 13 | 432/224 | -5.52 | 29 | -22.69 | -0.86 | 17.1 | -1.12 | +0.37 | -3.29 |
| 221 | `M82` Arthur Hill Rotasi Sasaran 10% | **33.2** | 23 | 11 | 50 | 18 | BELUM CUKUP | 29 | 609/302 | -2.03 | 29 | -9.13 | -0.47 | 11.9 | -0.56 | +0.68 | -2.21 |
| 222 | `M90` Pring KST | **32.8** | 16 | 16 | 45 | 10 | BELUM CUKUP | 26 | 97/68 | -3.76 | 29 | -13.55 | -0.68 | 13.4 | -1.01 | -1.42 | -3.63 |
| 223 | `M123` CCI Correction (Lambert, Chart | **32.2** | 13 | 21 | 35 | 11 | BELUM CUKUP | 27 | 209/191 | -1.95 | 29 | -16.06 | -0.95 | 9.4 | -2.35 | -1.15 | -4.53 |
| 224 | `M09` Volumatic VIDYA Pivot Retest | **32.1** | 7 | 10 | 29 | 6 | BELUM CUKUP | 17 | 45/35 | -5.69 | 29 | -17.41 | -0.93 | 11.1 | -2.40 | -2.32 | -11.80 |
| 225 | `M01` Bollinger Band + RSI | **31.8** | 18 | 8 | 42 | 18 | BELUM CUKUP | 25 | 140/29 | -2.83 | 29 | -14.18 | -0.85 | 7.6 | -1.03 | +0.81 | -3.54 |
| 226 | `M20` EMA10/15 Crossover + Sudut | **30.0**⌈ | 42 | 36 | 46 | 12 | GAGAL | 29 | 653/527 | -1.29 | 29 | -5.84 | -0.53 | 5.1 | -1.04 | -0.77 | -6.55 |
| 227 | `M28` VWAP Separator + Kiss Pivot | **30.0**⌈ | 41 | 32 | 46 | 13 | GAGAL | 25 | 151/130 | -1.37 | 29 | -6.63 | -0.68 | 6.2 | -1.00 | -0.43 | -7.29 |

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

