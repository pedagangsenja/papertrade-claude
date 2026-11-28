# Skor Kaedah 0–100 (pangkat maklumat, BUKAN keputusan)

> **Status keputusan (kad skor, harga 2026-11-27):** TERBUKTI 0 · CALON 0 · BELUM CUKUP 223 · GAGAL 4 · NEGATIF 0. Rejim QQQ OFF sejak 2026-10-16. Hanya **TERBUKTI** layak untuk wang sebenar (`laporan/KAD_SKOR.md`); nombor dalam laporan ini BUKAN keputusan dan tidak boleh dibaca sebagai pangkat untuk wang sebenar.

Dijana 2026-11-28 oleh `standard/skor_kaedah.py` (Actions `analisis.yml`, selepas kad skor). Harga pada tutup 2026-11-27; 227 kaedah; 30 hari beli langsung (rejim ON 1, OFF 29). Pradaftar 2026-11-09: `standard/SPEC_SKOR_KAEDAH.md` (berat dan sauh dikunci `ujian/test_skor_kaedah.py::TestKunci`). Rekod analisis sahaja: tiada order, tiada wang sebenar.

## Cara membaca

- **Skor** = min geometri berberat empat tiang (Untung 35 · Tahan 30 · Bukti 25 · Konsisten 10), dikecut ke 50 mengikut data: berat data = hari beli ÷ (hari beli + 20). Kaedah dengan 2 hari beli tidak boleh menjauhi 50. 100 = unggul semua segi; 50 = neutral/tiada bukti; < 50 = lebih buruk daripada neutral.
- **Siling** ikut kad skor: NEGATIF ≤ 20, GANTUNG/BERSARA ≤ 30, GAGAL ≤ 40. Tanda ⌈ = siling terpakai.
- **Satu-satunya status yang membenarkan wang sebenar ialah TERBUKTI dalam `laporan/KAD_SKOR.md`.** Skor tinggi dengan status BELUM CUKUP bermaksud "paling menjanjikan setakat ini", bukan "selamat".
- Deflasi ujian berganda (López de Prado): sauh t Bukti C1 = maks(2.0, E[maks 227 normal]) = 2.81.
- **Semakan kebolehramalan:** skor pada 2026-11-20 lawan pulangan lorong T4 sejak itu, 227 kaedah: Spearman ρ = -0.200 (p = 0.003). Belum ada bukti skor meramal pangkat; jangan pilih kaedah dengannya.
- Metrik T4 (A2, B1, B2, D1) dikira atas lorong T4 L1 **dipotong pada sesi LANGSUNG pertama** kaedah itu (Mxx 2026-10-16, Nxx/GB 2026-11-03) dan diasas semula; sesi isian bina semula tidak dikira (pindaan 9 Nov 2026 (a)). Lajur "T4 sesi/pul" di bawah ialah potongan itu, bukan lorong penuh `T4_KAEDAH.md`.

## Semua kaedah, susun ikut Skor

| # | Kaedah | Skor | Untung | Tahan | Bukti | Konsisten | Status kad | Hari beli | Posisi/tutup | Jangkaan % | T4 sesi | T4 pul % | T4 pul/|MDD| | Ulcer | t buku | Lift | WFE |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `M146` 3-Bar Momentum Pattern | **65.3** | 91 | 78 | 62 | 95 | BELUM CUKUP | 22 | 84/50 | +1.46 | 30 | +8.29 | +1.18 | 3.2 | +1.18 | +2.68 | 2.42 |
| 2 | `M48` Cooper 1-2-3-4 | **60.9** | 78 | 68 | 57 | 83 | BELUM CUKUP | 25 | 90/27 | +1.17 | 30 | +11.05 | +1.93 | 2.4 | +0.78 | -0.48 | 1.75 |
| 3 | `M151` Outside Bar Failure | **60.3** | 66 | 79 | 57 | 75 | BELUM CUKUP | 27 | 144/86 | -0.11 | 30 | +7.93 | +1.98 | 1.2 | +0.33 | -0.14 | 0.69 |
| 4 | `M160` Measured Move Up | **60.2** | 59 | 77 | 62 | 88 | BELUM CUKUP | 28 | 197/125 | -0.42 | 30 | +6.79 | +1.18 | 2.5 | +0.86 | +0.73 | 5.32 |
| 5 | `N202X36` RSI2<10 dalam trend naik x X36 | **58.1** | 96 | 98 | 48 | 70 | BELUM CUKUP | 8 | 114/19 | +2.72 | 10 | +4.26 | +2.01 | 1.0 | +0.56 | – | – |
| 6 | `M118` Expansion Pivot (Cooper) | **57.5** | 64 | 64 | 57 | 90 | BELUM CUKUP | 22 | 97/47 | -0.14 | 30 | +6.76 | +0.81 | 3.3 | +0.59 | +1.40 | 1.92 |
| 7 | `M74` Lulus Baharu Trend Template Mi | **56.2** | 66 | 64 | 57 | 42 | BELUM CUKUP | 30 | 116/83 | -0.37 | 30 | +4.28 | +0.58 | 3.3 | +0.26 | +0.13 | 0.45 |
| 8 | `M25` VWAP Wave (proksi harian) | **56.1** | 61 | 64 | 60 | 50 | BELUM CUKUP | 26 | 209/176 | -0.60 | 30 | +5.60 | +0.70 | 4.1 | +0.66 | +1.21 | 3.58 |
| 9 | `M70` Pecahan Hari Dalam | **56.0** | 66 | 77 | 56 | 24 | BELUM CUKUP | 30 | 542/465 | -0.38 | 30 | +5.81 | +1.01 | 2.5 | +0.09 | -1.39 | 0.23 |
| 10 | `M133` Bull Hook (Crabel) | **55.8** | 58 | 67 | 60 | 76 | BELUM CUKUP | 17 | 55/45 | -0.51 | 30 | +3.88 | +0.64 | 2.8 | +1.05 | +3.57 | 7.71 |
| 11 | `M23` Breitstein Kapitulasi + Kesina | **55.3** | 65 | 56 | 62 | 46 | BELUM CUKUP | 26 | 134/110 | -0.38 | 30 | -0.11 | -0.02 | 3.4 | +0.87 | +0.33 | 3.25 |
| 12 | `M158` Doubly Adaptive Profit Targets | **55.1** | 72 | 47 | 61 | 50 | BELUM CUKUP | 27 | 399/225 | +0.28 | 30 | +1.05 | +0.10 | 4.8 | +0.67 | +1.47 | 1.51 |
| 13 | `M137` Livermore System | **55.1** | 52 | 64 | 57 | 72 | BELUM CUKUP | 28 | 191/102 | -0.95 | 30 | +8.02 | +1.36 | 2.3 | +0.25 | +0.94 | 0.46 |
| 14 | `M145` Yum-Yum Continuation | **55.0** | 56 | 63 | 56 | 63 | BELUM CUKUP | 25 | 313/112 | -0.54 | 30 | +5.92 | +1.53 | 1.5 | +0.19 | +0.65 | 0.17 |
| 15 | `M93` Bollinger Kaedah II: %b + MFI | **54.7** | 74 | 48 | 59 | 44 | BELUM CUKUP | 27 | 277/126 | +0.50 | 30 | +2.36 | +0.25 | 4.3 | +0.51 | +1.85 | 0.75 |
| 16 | `M46` Jurang Naik Boleh Beli (Buyabl | **54.5** | 58 | 72 | 50 | 71 | BELUM CUKUP | 14 | 37/27 | -0.92 | 30 | +4.50 | +0.91 | 1.7 | +0.27 | +0.53 | 0.46 |
| 17 | `N25X36` Supertrend + EMA + ADX>23 → ke | **53.7** | 57 | 66 | 49 | 70 | BELUM CUKUP | 16 | 147/64 | -0.86 | 17 | +3.58 | +0.80 | 1.9 | -0.08 | – | – |
| 18 | `M33` Supertrend + SMA10 | **53.0** | 44 | 60 | 58 | 87 | BELUM CUKUP | 24 | 226/127 | -1.42 | 30 | +8.05 | +1.11 | 2.7 | +0.35 | +0.51 | 1.77 |
| 19 | `N204X36` Undur RSI2, gap 2%, RSI silang | **52.6** | 70 | 85 | 45 | 62 | BELUM CUKUP | 4 | 9/1 | +1.36 | 5 | +1.39 | +0.67 | 1.2 | +1.41 | – | – |
| 20 | `M35` Pocket Pivot Morales & Kacher | **52.2** | 63 | 44 | 57 | 46 | BELUM CUKUP | 29 | 376/325 | -0.35 | 30 | -1.77 | -0.19 | 5.9 | +0.18 | +0.73 | 0.93 |
| 21 | `M08` SMA20 + SMA200 | **52.1** | 56 | 49 | 55 | 58 | BELUM CUKUP | 28 | 307/221 | -0.78 | 30 | -0.44 | -0.08 | 3.6 | -0.06 | +0.77 | -0.16 |
| 22 | `M142` Pecahan volum dari dasar (底部放量 | **51.7** | 66 | 44 | 47 | 67 | BELUM CUKUP | 18 | 56/14 | +0.31 | 28 | +2.23 | +0.27 | 3.4 | +0.23 | – | 0.39 |
| 23 | `M131` Ross Hook (Joe Ross) | **51.6** | 58 | 49 | 57 | 37 | BELUM CUKUP | 27 | 280/162 | -0.66 | 30 | +1.12 | +0.13 | 4.4 | +0.29 | +0.47 | 0.68 |
| 24 | `M100` Bulkowski Segi Empat & Segi Ti | **51.4** | 59 | 54 | 52 | 35 | BELUM CUKUP | 19 | 66/45 | -0.35 | 30 | +1.83 | +0.23 | 3.4 | +0.12 | +0.92 | 0.56 |
| 25 | `M104` High Tight Flag / Power Play | **51.2** | 88 | 90 | 45 | 85 | BELUM CUKUP | 1 | 1/0 | +29.82 | 15 | +3.00 | +10.00 | 0.1 | +2.14 | – | 10.44 |
| 26 | `M51` O'Neil Cawan & Pemegang | **50.9** | 87 | 63 | 39 | 45 | BELUM CUKUP | 2 | 3/1 | +1.16 | 20 | +0.39 | +0.24 | 0.7 | +0.92 | – | 3.24 |
| 27 | `M41` FW Penyatuan Mingguan | **50.9** | 80 | 41 | 46 | 45 | BELUM CUKUP | 6 | 68/14 | +1.21 | 29 | -1.45 | -0.12 | 6.2 | +0.63 | – | 1.09 |
| 28 | `M128` Inventory Retracement Bar (IRB | **50.4** | 59 | 40 | 57 | 47 | BELUM CUKUP | 27 | 215/148 | -0.25 | 30 | -1.98 | -0.18 | 7.4 | +0.26 | +0.53 | 1.17 |
| 29 | `M10` EMA3 + CCI + MACD | **50.3** | 42 | 58 | 54 | 56 | BELUM CUKUP | 24 | 130/78 | -1.78 | 30 | +11.10 | +1.68 | 2.7 | -0.00 | +0.25 | -0.00 |
| 30 | `M30` BB Free Bar + Himpitan 50/2.5 | **50.3** | 60 | 38 | 58 | 46 | BELUM CUKUP | 22 | 231/126 | -0.37 | 30 | +2.60 | +0.23 | 6.0 | +0.49 | +0.25 | 1.02 |
| 31 | `M45` High 52 Minggu (George & Hwang | **50.2** | 66 | 53 | 37 | 85 | BELUM CUKUP | 1 | 2/1 | +0.26 | 19 | +0.07 | +0.04 | 0.8 | +0.94 | – | 2.43 |
| 32 | `M143` 장대양봉 이후 눌림목 / 5일선 매매 (Undur ke | **50.2** | 66 | 56 | 38 | 30 | BELUM CUKUP | 16 | 30/8 | +0.29 | 29 | +0.53 | +0.10 | 2.2 | -0.53 | – | -4.32 |
| 33 | `N68X36` Bullish engulfing + EMA21 → ke | **50.2** | 60 | 51 | 48 | 30 | BELUM CUKUP | 16 | 157/49 | -0.10 | 17 | +1.17 | +0.13 | 4.7 | -0.01 | – | – |
| 34 | `M80` Radge Saluran Purata Bergerak  | **49.8** | 60 | 37 | 59 | 40 | BELUM CUKUP | 28 | 317/131 | -0.16 | 30 | -1.24 | -0.12 | 5.7 | +0.42 | +1.67 | 0.64 |
| 35 | `N53X36` Supertrend + ADX>25 → keluar s | **49.8** | 65 | 40 | 53 | 30 | BELUM CUKUP | 16 | 148/65 | +0.13 | 17 | -2.01 | -0.22 | 4.4 | +0.40 | – | – |
| 36 | `N06X36` Golden cross MA50/MA200 → kelu | **49.6** | 69 | 50 | 35 | 30 | BELUM CUKUP | 14 | 32/5 | +0.94 | 17 | -2.11 | -0.28 | 3.9 | -0.62 | – | – |
| 37 | `M18` EMA9/21 Pullback | **49.5** | 58 | 44 | 56 | 28 | BELUM CUKUP | 30 | 547/450 | -0.45 | 30 | -4.40 | -0.45 | 5.0 | +0.07 | +1.62 | 0.25 |
| 38 | `M129` Wick Play | **49.4** | 49 | 48 | 46 | 55 | BELUM CUKUP | 12 | 32/13 | -1.12 | 30 | +2.25 | +0.39 | 2.3 | +0.12 | – | 0.38 |
| 39 | `M07` Qullamaggie Breakout | **49.3** | 35 | 64 | 27 | 15 | BELUM CUKUP | 1 | 1/1 | -2.53 | 30 | -0.25 | -0.21 | 0.9 | -0.22 | – | -1.12 |
| 40 | `M117` Landry Pullback (high 2 bulan) | **49.2** | 63 | 32 | 57 | 44 | BELUM CUKUP | 23 | 168/45 | +0.41 | 30 | -6.50 | -0.55 | 6.2 | +0.64 | +2.07 | 0.70 |
| 41 | `M13` Garis Trend Action/Safety Line | **49.1** | 37 | 64 | 49 | 53 | BELUM CUKUP | 30 | 989/791 | -2.22 | 30 | +8.22 | +1.24 | 2.3 | -0.73 | -0.65 | -1.89 |
| 42 | `N75X14` RSI14 < 40 tanpa penapis → kel | **49.0** | 62 | 44 | 45 | 30 | BELUM CUKUP | 17 | 404/100 | +0.57 | 17 | -3.79 | -0.40 | 5.0 | -0.71 | – | – |
| 43 | `M37` Weinstein Peringkat 2 | **49.0** | 57 | 55 | 30 | 15 | BELUM CUKUP | 3 | 7/1 | -0.71 | 24 | -0.38 | -0.08 | 1.7 | -0.18 | – | -0.28 |
| 44 | `M68` Kell Base n' Break | **48.7** | 45 | 50 | 50 | 42 | BELUM CUKUP | 18 | 59/20 | -1.21 | 30 | +2.53 | +0.32 | 3.2 | +0.18 | -0.88 | 1.08 |
| 45 | `M27` Price Action 4 Tiang | **48.7** | 44 | 31 | 46 | 15 | BELUM CUKUP | 2 | 546/521 | -1.23 | 30 | -4.16 | -0.81 | 3.3 | -0.07 | – | -0.28 |
| 46 | `M84` Jarak purata bergerak MAD 21/2 | **48.7** | 27 | 14 | 39 | 15 | BELUM CUKUP | 1 | 58/43 | -3.36 | 19 | -7.08 | -0.81 | 7.1 | -0.11 | – | -0.27 |
| 47 | `M39` Radge Pecahan Bollinger 100 ha | **48.6** | 35 | 60 | 53 | 54 | BELUM CUKUP | 25 | 251/71 | -1.88 | 30 | +6.98 | +1.07 | 2.2 | -0.05 | -0.37 | -0.10 |
| 48 | `N28X16` ADX>25 + DI+ > DI- → keluar bi | **48.6** | 45 | 46 | 44 | 70 | BELUM CUKUP | 17 | 684/569 | -0.73 | 17 | -1.94 | -0.23 | 3.7 | -0.89 | – | – |
| 49 | `N75X17` RSI14 < 40 tanpa penapis → kel | **48.5** | 56 | 45 | 45 | 30 | BELUM CUKUP | 17 | 619/372 | -0.05 | 17 | -3.12 | -0.24 | 6.0 | -0.73 | – | – |
| 50 | `M102` Stockbee SLTB | **48.4** | 60 | 46 | 55 | 15 | BELUM CUKUP | 30 | 483/367 | -0.79 | 30 | +0.92 | +0.08 | 6.5 | -0.07 | +0.09 | -0.18 |
| 51 | `M12` Parabolic SAR | **48.3** | 46 | 54 | 54 | 25 | BELUM CUKUP | 30 | 484/303 | -1.39 | 30 | +2.73 | +0.42 | 3.2 | -0.18 | -0.89 | -0.41 |
| 52 | `M132` Ascending Scallop (Bulkowski) | **48.3** | 42 | 50 | 53 | 38 | BELUM CUKUP | 21 | 100/52 | -1.66 | 30 | +2.67 | +0.35 | 3.4 | +0.13 | -0.46 | 0.84 |
| 53 | `M54` IBD Power Trend | **48.2** | 48 | 51 | 54 | 23 | BELUM CUKUP | 25 | 233/144 | -1.30 | 30 | +4.52 | +0.43 | 5.7 | -0.10 | +0.10 | -0.22 |
| 54 | `M120` Reversal New Highs | **48.2** | 54 | 40 | 46 | 37 | BELUM CUKUP | 13 | 19/13 | -0.97 | 30 | -1.15 | -0.17 | 3.8 | +0.13 | – | 0.72 |
| 55 | `M96` Momo India: Ranking Sharpe 3/6 | **48.2** | 21 | 7 | 9 | 15 | BELUM CUKUP | 1 | 6/6 | -13.71 | 19 | -8.21 | -1.00 | 7.4 | -5.92 | – | -15.55 |
| 56 | `N45X16` Undur EMA21 cerun positif → ke | **48.1** | 44 | 53 | 49 | 30 | BELUM CUKUP | 17 | 235/155 | -1.14 | 17 | +3.97 | +0.47 | 3.8 | -0.25 | – | – |
| 57 | `M124` 'Last' Stochastic Technique (C | **48.0** | 39 | 53 | 54 | 41 | BELUM CUKUP | 29 | 451/337 | -1.87 | 30 | +4.15 | +0.47 | 3.9 | -0.11 | -0.53 | -0.28 |
| 58 | `N25X16` Supertrend + EMA + ADX>23 → ke | **47.9** | 34 | 54 | 46 | 70 | BELUM CUKUP | 15 | 129/48 | -2.25 | 17 | +2.24 | +0.47 | 2.5 | -0.28 | – | – |
| 59 | `N201X36` MA20 silang MA50 atas MA50 x X | **47.9** | 46 | 50 | 39 | 30 | BELUM CUKUP | 9 | 31/8 | -0.62 | 10 | -2.27 | -0.30 | 4.1 | -0.17 | – | – |
| 60 | `M94` Pecutan Momentum (Chen, Yu & W | **47.9** | 3 | 4 | 17 | 15 | BELUM CUKUP | 1 | 33/0 | -12.79 | 19 | -16.85 | -0.77 | 12.3 | -1.19 | – | -3.28 |
| 61 | `M32` Momentum Burst | **47.8** | 61 | 31 | 54 | 34 | BELUM CUKUP | 19 | 75/50 | -0.47 | 30 | -2.34 | -0.16 | 8.8 | +0.27 | +0.79 | 0.55 |
| 62 | `M21` Marius 3 Persediaan (Pecahan+J | **47.8** | 42 | 48 | 39 | 22 | BELUM CUKUP | 6 | 7/5 | -1.56 | 22 | -1.06 | -0.39 | 1.9 | +0.16 | – | 0.22 |
| 63 | `M78` Alvarez Pecahan Mingguan DTAYS | **47.7** | 23 | 19 | 42 | 20 | BELUM CUKUP | 2 | 73/47 | -2.16 | 29 | -8.85 | -0.79 | 8.5 | +0.06 | – | 0.17 |
| 64 | `M77` Undercut & Rally pada Purata B | **47.4** | 56 | 44 | 48 | 18 | BELUM CUKUP | 22 | 64/50 | -0.72 | 30 | -3.12 | -0.38 | 3.2 | -0.39 | +0.91 | -0.46 |
| 65 | `N48X36` Inside day pecah → keluar sele | **47.3** | 53 | 38 | 46 | 33 | BELUM CUKUP | 17 | 429/309 | +0.03 | 17 | -4.39 | -0.50 | 5.9 | -0.55 | – | – |
| 66 | `M153` Range Leader | **47.1** | 57 | 41 | 53 | 17 | BELUM CUKUP | 30 | 1639/1492 | -0.40 | 30 | -0.92 | -0.07 | 8.3 | -0.26 | +0.64 | -1.65 |
| 67 | `M149` 3-Step Pullback | **47.1** | 53 | 39 | 57 | 22 | BELUM CUKUP | 28 | 277/113 | -0.71 | 30 | +0.40 | +0.03 | 6.7 | +0.27 | -0.01 | 0.24 |
| 68 | `M05` MACD Divergence + Pengesahan | **47.0** | 37 | 50 | 44 | 50 | BELUM CUKUP | 17 | 43/18 | -1.96 | 30 | +2.00 | +0.28 | 2.7 | -0.39 | -1.39 | -0.70 |
| 69 | `M157` Consolidation Pivot Breakout ( | **47.0** | 48 | 46 | 33 | 15 | BELUM CUKUP | 7 | 9/3 | -0.68 | 27 | -0.50 | -0.15 | 1.9 | -0.46 | – | -0.94 |
| 70 | `M138` 直升机空中加油 (Helikopter isi minyak | **46.8** | 30 | 52 | 23 | 15 | BELUM CUKUP | 4 | 4/0 | -2.03 | 23 | -0.73 | -0.32 | 0.9 | -0.81 | – | -1.27 |
| 71 | `N16X13` RSI2<10 tanpa penapis → keluar | **46.7** | 58 | 37 | 38 | 30 | BELUM CUKUP | 16 | 315/9 | +0.66 | 17 | -7.89 | -0.59 | 8.5 | -0.58 | – | – |
| 72 | `N43X36` Undur EMA8 + penapis MA50 → ke | **46.6** | 46 | 41 | 46 | 30 | BELUM CUKUP | 17 | 316/121 | -0.80 | 17 | -1.00 | -0.14 | 3.6 | -0.57 | – | – |
| 73 | `M115` Bow Tie (Landry) | **46.6** | 37 | 37 | 50 | 44 | BELUM CUKUP | 12 | 37/31 | -2.03 | 30 | -3.53 | -0.37 | 5.7 | +0.24 | -0.13 | 1.06 |
| 74 | `N64X17` Episodic pivot → keluar bila a | **46.6** | 50 | 34 | 41 | 30 | BELUM CUKUP | 11 | 57/18 | -0.76 | 17 | +0.36 | +0.04 | 3.9 | -0.37 | – | – |
| 75 | `N28X36` ADX>25 + DI+ > DI- → keluar se | **46.4** | 47 | 38 | 47 | 30 | BELUM CUKUP | 17 | 633/513 | -0.39 | 17 | -5.86 | -0.44 | 5.9 | -0.52 | – | – |
| 76 | `N119X13` 3 tutup turun berturut → kelua | **46.3** | 51 | 34 | 43 | 30 | BELUM CUKUP | 15 | 290/77 | +0.09 | 17 | -5.97 | -0.54 | 7.5 | -0.82 | – | – |
| 77 | `N65X36` Gap 4% + volum + hampir 52w →  | **46.2** | 42 | 30 | 35 | 30 | BELUM CUKUP | 7 | 34/6 | -1.01 | 17 | -0.76 | -0.10 | 3.8 | -0.49 | – | – |
| 78 | `M15` Break & Retest + Henti ATR | **46.1** | 51 | 31 | 57 | 35 | BELUM CUKUP | 29 | 340/297 | -0.45 | 30 | -7.75 | -0.50 | 7.4 | +0.20 | +1.56 | 0.48 |
| 79 | `N36X36` Pocket pivot → keluar selepas  | **45.8** | 37 | 41 | 44 | 49 | BELUM CUKUP | 17 | 208/123 | -2.02 | 17 | +2.00 | +0.21 | 4.4 | -0.90 | – | – |
| 80 | `M38` Darvas Kotak | **45.8** | 27 | 24 | 36 | 41 | BELUM CUKUP | 5 | 27/1 | -2.07 | 29 | -3.74 | -0.32 | 6.9 | +0.24 | – | 0.87 |
| 81 | `M107` Golden Cross SMA50/200 | **45.7** | 49 | 37 | 48 | 23 | BELUM CUKUP | 22 | 47/14 | -0.46 | 30 | -2.58 | -0.25 | 4.5 | +0.09 | +0.98 | 0.15 |
| 82 | `N09X36` Undur EMA10 + penapis EMA50 →  | **45.7** | 41 | 40 | 46 | 30 | BELUM CUKUP | 17 | 323/139 | -1.08 | 17 | -1.25 | -0.17 | 3.7 | -0.64 | – | – |
| 83 | `N68X16` Bullish engulfing + EMA21 → ke | **45.7** | 43 | 36 | 47 | 30 | BELUM CUKUP | 16 | 155/60 | -0.73 | 17 | -1.74 | -0.15 | 6.9 | -0.22 | – | – |
| 84 | `N64X16` Episodic pivot → keluar bila s | **45.7** | 43 | 32 | 42 | 30 | BELUM CUKUP | 11 | 57/22 | -1.03 | 17 | -0.22 | -0.03 | 3.5 | -0.33 | – | – |
| 85 | `M87` IBD Tapak Menaik | **45.7** | 34 | 37 | 44 | 26 | BELUM CUKUP | 9 | 12/8 | -2.03 | 30 | -2.42 | -0.31 | 4.7 | +0.13 | – | 0.37 |
| 86 | `N203X36` Gap 2% lalu MA20 silang MA50 x | **45.7** | 22 | 42 | 36 | 30 | BELUM CUKUP | 6 | 14/3 | -2.06 | 10 | -2.79 | -0.27 | 5.7 | -0.06 | – | – |
| 87 | `M111` Sistem Volatiliti Wilder | **45.6** | 42 | 41 | 56 | 24 | BELUM CUKUP | 28 | 283/174 | -1.61 | 30 | +1.82 | +0.17 | 5.1 | +0.14 | -0.77 | 0.39 |
| 88 | `N64X36` Episodic pivot → keluar selepa | **45.6** | 45 | 32 | 40 | 30 | BELUM CUKUP | 11 | 57/16 | -0.98 | 17 | -0.14 | -0.02 | 4.1 | -0.38 | – | – |
| 89 | `N64X14` Episodic pivot → keluar bila r | **45.6** | 42 | 33 | 41 | 30 | BELUM CUKUP | 11 | 57/21 | -1.32 | 17 | +0.04 | +0.00 | 3.5 | -0.38 | – | – |
| 90 | `N65X14` Gap 4% + volum + hampir 52w →  | **45.6** | 36 | 30 | 36 | 30 | BELUM CUKUP | 7 | 34/12 | -1.66 | 17 | -1.07 | -0.13 | 4.0 | -0.54 | – | – |
| 91 | `M64` O'Neil Tiga Minggu Ketat | **45.5** | 23 | 22 | 27 | 15 | BELUM CUKUP | 4 | 5/3 | -7.03 | 30 | -3.47 | -0.77 | 3.2 | -1.18 | – | -12.83 |
| 92 | `N55X13` BB + RSI + ADX>20 → keluar bil | **45.3** | 60 | 36 | 29 | 30 | BELUM CUKUP | 17 | 156/0 | +0.73 | 17 | -6.17 | -0.68 | 5.8 | -0.75 | – | – |
| 93 | `M150` Trend Bar Failure (Brooks) | **45.2** | 44 | 38 | 54 | 21 | BELUM CUKUP | 24 | 120/97 | -1.07 | 30 | -4.92 | -0.51 | 4.8 | -0.08 | +1.60 | -0.31 |
| 94 | `M127` Slingshot Bullish | **45.2** | 42 | 41 | 51 | 19 | BELUM CUKUP | 20 | 112/92 | -1.58 | 30 | -4.51 | -0.47 | 5.0 | -0.33 | +1.06 | -0.44 |
| 95 | `M130` 多方炮 (dua lilin hijau mengapit  | **45.2** | 38 | 27 | 41 | 23 | BELUM CUKUP | 8 | 12/5 | -1.39 | 28 | -1.48 | -0.15 | 5.0 | +0.27 | – | 0.27 |
| 96 | `N37X17` Gap and go → keluar bila adx14 | **45.0** | 38 | 36 | 42 | 34 | BELUM CUKUP | 14 | 95/41 | -1.79 | 17 | +1.46 | +0.17 | 4.0 | -0.61 | – | – |
| 97 | `N75X13` RSI14 < 40 tanpa penapis → kel | **44.9** | 53 | 34 | 33 | 30 | BELUM CUKUP | 17 | 216/1 | +0.23 | 17 | -6.11 | -0.52 | 5.9 | -0.55 | – | – |
| 98 | `M105` Supertrend tulen | **44.7** | 39 | 39 | 56 | 25 | BELUM CUKUP | 26 | 384/231 | -1.82 | 30 | +1.31 | +0.11 | 6.1 | +0.11 | -0.04 | 0.32 |
| 99 | `N53X17` Supertrend + ADX>25 → keluar b | **44.7** | 35 | 36 | 45 | 30 | BELUM CUKUP | 14 | 113/23 | -1.66 | 17 | -0.47 | -0.04 | 5.9 | -0.11 | – | – |
| 100 | `M106` DMI Wilder | **44.6** | 44 | 42 | 53 | 13 | BELUM CUKUP | 26 | 152/119 | -1.30 | 30 | -1.61 | -0.21 | 3.5 | -0.21 | -0.52 | -0.55 |
| 101 | `M36` Turtle 55/20 | **44.2** | 44 | 34 | 55 | 19 | BELUM CUKUP | 27 | 359/231 | -1.50 | 30 | -0.66 | -0.05 | 7.9 | +0.04 | +0.25 | 0.09 |
| 102 | `N38X36` VCP pecah → keluar selepas DUA | **44.1** | 35 | 41 | 40 | 30 | BELUM CUKUP | 17 | 55/27 | -1.57 | 17 | -1.86 | -0.23 | 4.0 | -0.82 | – | – |
| 103 | `N75X15` RSI14 < 40 tanpa penapis → eko | **44.1** | 52 | 32 | 30 | 30 | BELUM CUKUP | 17 | 210/0 | +0.11 | 17 | -6.11 | -0.52 | 5.9 | -0.56 | – | – |
| 104 | `M116` 2/20 EMA Breakout (Landry) | **44.0** | 48 | 35 | 54 | 15 | BELUM CUKUP | 30 | 651/578 | -0.83 | 30 | -0.46 | -0.03 | 8.5 | -0.13 | -0.08 | -0.62 |
| 105 | `M49` Ichimoku (Tutup Atas Awan + Te | **44.0** | 45 | 42 | 51 | 13 | BELUM CUKUP | 30 | 388/266 | -1.62 | 30 | -0.07 | -0.01 | 5.0 | -0.53 | -0.58 | -0.82 |
| 106 | `N19X13` Bawah jalur BB + RSI<30 → kelu | **44.0** | 42 | 34 | 29 | 30 | BELUM CUKUP | 13 | 146/0 | -0.80 | 17 | -3.64 | -0.47 | 4.5 | -0.59 | – | – |
| 107 | `M04` BB Squeeze Breakout | **43.9** | 37 | 34 | 56 | 27 | BELUM CUKUP | 23 | 159/90 | -1.92 | 30 | +1.83 | +0.17 | 5.5 | +0.25 | -0.30 | 0.42 |
| 108 | `N73X13` Tutup bawah jalur bawah BB(20, | **43.9** | 48 | 32 | 33 | 30 | BELUM CUKUP | 17 | 233/1 | -0.17 | 17 | -6.16 | -0.53 | 6.6 | -0.57 | – | – |
| 109 | `N25X17` Supertrend + EMA + ADX>23 → ke | **43.8** | 29 | 38 | 44 | 30 | BELUM CUKUP | 14 | 122/39 | -2.43 | 17 | -1.59 | -0.22 | 3.5 | -0.39 | – | – |
| 110 | `M119` 180 Bullish (Cooper) | **43.7** | 45 | 33 | 52 | 19 | BELUM CUKUP | 26 | 195/113 | -0.97 | 30 | -4.47 | -0.41 | 6.3 | -0.32 | +0.98 | -0.92 |
| 111 | `M34` Carter TTM Squeeze | **43.7** | 47 | 30 | 54 | 17 | BELUM CUKUP | 24 | 109/68 | -1.14 | 30 | -2.34 | -0.18 | 6.3 | +0.03 | -0.14 | 0.09 |
| 112 | `N08X36` tutup>EMA20 tidak terlalu jauh | **43.7** | 32 | 40 | 41 | 30 | BELUM CUKUP | 17 | 564/427 | -1.64 | 17 | -3.10 | -0.32 | 4.7 | -1.15 | – | – |
| 113 | `N16X15` RSI2<10 tanpa penapis → ekori  | **43.7** | 51 | 30 | 30 | 30 | BELUM CUKUP | 16 | 287/0 | +0.48 | 17 | -10.25 | -0.65 | 10.7 | -0.63 | – | – |
| 114 | `N37X36` Gap and go → keluar selepas DU | **43.7** | 32 | 34 | 41 | 35 | BELUM CUKUP | 14 | 95/44 | -2.41 | 17 | +0.45 | +0.06 | 3.8 | -0.75 | – | – |
| 115 | `N66X36` 52w tinggi + pengesahan 1% → k | **43.6** | 32 | 26 | 37 | 30 | BELUM CUKUP | 10 | 44/7 | -1.74 | 16 | -2.17 | -0.26 | 4.4 | -0.45 | – | – |
| 116 | `N113X36` 80-20 bar (sisi beli) → keluar | **43.5** | 41 | 28 | 44 | 30 | BELUM CUKUP | 17 | 602/363 | -0.35 | 17 | -9.12 | -0.68 | 9.2 | -0.91 | – | – |
| 117 | `N40X16` OBV tinggi baharu + MA50 → kel | **43.5** | 49 | 20 | 51 | 30 | BELUM CUKUP | 17 | 116/56 | +0.13 | 17 | -9.01 | -0.56 | 8.6 | +0.22 | – | – |
| 118 | `N24X36` Supertrend(10,3) + ADX>20 → ke | **43.5** | 34 | 32 | 48 | 30 | BELUM CUKUP | 17 | 194/126 | -1.87 | 17 | -1.99 | -0.21 | 4.6 | -0.43 | – | – |
| 119 | `N113X16` 80-20 bar (sisi beli) → keluar | **43.3** | 43 | 25 | 44 | 30 | BELUM CUKUP | 17 | 636/399 | -0.19 | 17 | -9.32 | -0.65 | 9.9 | -0.85 | – | – |
| 120 | `M26` Garis Trend Undur 3 Sentuhan + | **43.2** | 42 | 35 | 49 | 17 | BELUM CUKUP | 24 | 95/67 | -0.87 | 30 | -4.83 | -0.47 | 5.2 | -0.53 | +0.55 | -0.75 |
| 121 | `N40X36` OBV tinggi baharu + MA50 → kel | **43.2** | 51 | 18 | 50 | 30 | BELUM CUKUP | 17 | 97/35 | +0.08 | 17 | -9.04 | -0.62 | 8.7 | +0.24 | – | – |
| 122 | `N07X16` Tiga MA tersusun → keluar bila | **43.0** | 27 | 38 | 47 | 30 | BELUM CUKUP | 17 | 183/81 | -1.96 | 17 | -1.42 | -0.24 | 3.2 | -0.43 | – | – |
| 123 | `N41X36` CMF20>0 + tutup>EMA20 → keluar | **42.9** | 28 | 36 | 43 | 30 | BELUM CUKUP | 16 | 310/241 | -1.98 | 17 | -3.78 | -0.44 | 5.0 | -0.90 | – | – |
| 124 | `M44` Tapak Rata IBD | **42.9** | 25 | 38 | 33 | 15 | BELUM CUKUP | 10 | 11/8 | -3.89 | 30 | -4.18 | -0.73 | 3.8 | -1.18 | – | -19.90 |
| 125 | `M121` High 2 bull flag (Brooks) | **42.7** | 21 | 21 | 27 | 15 | BELUM CUKUP | 7 | 10/3 | -3.99 | 26 | -3.91 | -0.51 | 5.0 | -1.19 | – | -11.62 |
| 126 | `M156` Single Penetration (DiNapoli) | **42.6** | 47 | 30 | 52 | 15 | BELUM CUKUP | 29 | 316/244 | -0.77 | 30 | -3.82 | -0.26 | 8.5 | -0.39 | +0.09 | -1.24 |
| 127 | `N27X16` Ichimoku atas awan → keluar bi | **42.6** | 33 | 29 | 45 | 30 | BELUM CUKUP | 17 | 228/149 | -1.27 | 17 | -4.90 | -0.51 | 5.1 | -0.75 | – | – |
| 128 | `N42X36` Lonjakan volum 2x → keluar sel | **42.4** | 38 | 24 | 44 | 30 | BELUM CUKUP | 17 | 251/164 | -1.00 | 17 | -6.56 | -0.62 | 6.2 | -0.79 | – | – |
| 129 | `N33X36` Donchian20 + penapis MA200 → k | **42.4** | 26 | 27 | 41 | 30 | BELUM CUKUP | 12 | 103/54 | -3.84 | 17 | -3.69 | -0.43 | 4.5 | -0.75 | – | – |
| 130 | `M126` Hidden Smash Day (beli, Larry  | **42.3** | 28 | 35 | 40 | 15 | BELUM CUKUP | 13 | 21/11 | -1.98 | 29 | -3.62 | -0.45 | 5.2 | -0.29 | – | -0.38 |
| 131 | `M144` Screw Bar | **42.3** | 16 | 30 | 34 | 15 | BELUM CUKUP | 8 | 29/26 | -5.35 | 28 | -7.72 | -0.88 | 2.9 | -1.16 | – | -1.56 |
| 132 | `M92` CCI-50 | **42.2** | 40 | 34 | 52 | 16 | BELUM CUKUP | 30 | 657/542 | -1.09 | 30 | -5.50 | -0.41 | 6.3 | -0.38 | +0.30 | -0.82 |
| 133 | `M73` ADX(5) > 40 + Julat Terkecil 6 | **42.2** | 44 | 30 | 53 | 15 | BELUM CUKUP | 30 | 1251/1151 | -0.21 | 30 | -7.92 | -0.63 | 7.7 | -0.28 | +0.12 | -1.78 |
| 134 | `M67` Rayner Teo: Ujian Ketiga pada  | **42.2** | 37 | 34 | 45 | 15 | BELUM CUKUP | 20 | 36/28 | -2.20 | 30 | -3.59 | -0.30 | 7.5 | -0.55 | – | -2.13 |
| 135 | `N42X14` Lonjakan volum 2x → keluar bil | **42.2** | 37 | 23 | 45 | 30 | BELUM CUKUP | 17 | 226/66 | -1.19 | 17 | -5.15 | -0.42 | 6.8 | -0.52 | – | – |
| 136 | `N76X36` Tutup > MA50 (penapis trend tu | **42.2** | 29 | 30 | 45 | 30 | BELUM CUKUP | 17 | 271/159 | -1.63 | 17 | -6.27 | -0.54 | 6.7 | -0.76 | – | – |
| 137 | `N124X36` Episodic pivot gap 8-10% → kel | **42.2** | 27 | 26 | 38 | 30 | BELUM CUKUP | 12 | 56/30 | -2.27 | 17 | -5.34 | -0.45 | 6.2 | -0.95 | – | – |
| 138 | `M135` 3rd Watch | **42.2** | 24 | 23 | 36 | 15 | BELUM CUKUP | 9 | 15/7 | -7.06 | 30 | -3.13 | -0.37 | 4.9 | -0.75 | – | -4.47 |
| 139 | `N33X14` Donchian20 + penapis MA200 → k | **42.1** | 27 | 25 | 42 | 30 | BELUM CUKUP | 13 | 123/46 | -4.10 | 17 | -3.26 | -0.53 | 3.6 | -0.66 | – | – |
| 140 | `N124X15` Episodic pivot gap 8-10% → eko | **42.1** | 37 | 21 | 30 | 30 | BELUM CUKUP | 12 | 55/0 | -1.18 | 17 | -4.33 | -0.32 | 6.4 | -0.50 | – | – |
| 141 | `M88` O'Neil Shakeout +3 | **42.0** | 35 | 37 | 48 | 14 | BELUM CUKUP | 23 | 103/77 | -4.32 | 30 | -1.12 | -0.07 | 8.1 | -0.66 | -0.31 | -1.07 |
| 142 | `N51X16` BB squeeze + Supertrend → kelu | **42.0** | 20 | 36 | 29 | 30 | BELUM CUKUP | 11 | 17/4 | -2.18 | 17 | -3.95 | -0.48 | 4.4 | -1.16 | – | – |
| 143 | `M50` Elder Triple Screen | **41.9** | 43 | 29 | 53 | 16 | BELUM CUKUP | 30 | 681/528 | -1.13 | 30 | -8.35 | -0.60 | 7.9 | -0.24 | +0.33 | -0.44 |
| 144 | `N22X36` BB pecah atas + RSI → keluar s | **41.9** | 25 | 30 | 48 | 30 | BELUM CUKUP | 16 | 128/78 | -3.40 | 17 | -3.56 | -0.31 | 5.8 | -0.30 | – | – |
| 145 | `N37X14` Gap and go → keluar bila rsi14 | **41.9** | 30 | 24 | 42 | 30 | BELUM CUKUP | 14 | 94/35 | -2.98 | 17 | -2.18 | -0.16 | 6.4 | -0.64 | – | – |
| 146 | `N33X16` Donchian20 + penapis MA200 → k | **41.9** | 24 | 25 | 41 | 30 | BELUM CUKUP | 12 | 109/58 | -5.01 | 17 | -3.44 | -0.48 | 3.5 | -0.79 | – | – |
| 147 | `N76X16` Tutup > MA50 (penapis trend tu | **41.8** | 26 | 34 | 41 | 30 | BELUM CUKUP | 17 | 478/392 | -1.68 | 17 | -3.40 | -0.37 | 4.3 | -1.16 | – | – |
| 148 | `M91` Stochastic Pop (Bernstein/Stec | **41.7** | 33 | 22 | 51 | 29 | BELUM CUKUP | 17 | 40/34 | -3.51 | 30 | -1.34 | -0.08 | 8.4 | +0.16 | -1.33 | 0.63 |
| 149 | `N36X16` Pocket pivot → keluar bila sup | **41.7** | 27 | 30 | 44 | 30 | BELUM CUKUP | 17 | 217/131 | -2.31 | 17 | -1.94 | -0.18 | 5.1 | -0.87 | – | – |
| 150 | `M89` Chande 65sma-3cc | **41.6** | 34 | 36 | 53 | 13 | BELUM CUKUP | 26 | 221/154 | -2.32 | 30 | -1.88 | -0.17 | 6.0 | -0.21 | -0.60 | -0.67 |
| 151 | `N53X16` Supertrend + ADX>25 → keluar b | **41.6** | 24 | 28 | 48 | 30 | BELUM CUKUP | 15 | 123/50 | -2.22 | 17 | -4.57 | -0.42 | 6.7 | -0.11 | – | – |
| 152 | `N57X36` ADX bangkit daripada <20 → kel | **41.6** | 25 | 28 | 40 | 30 | BELUM CUKUP | 14 | 81/27 | -4.30 | 17 | -1.22 | -0.15 | 4.4 | -0.75 | – | – |
| 153 | `M136` Short/Intermediate-term Low (L | **41.4** | 32 | 38 | 50 | 17 | BELUM CUKUP | 30 | 1000/541 | -2.66 | 30 | -2.31 | -0.22 | 4.5 | -0.58 | +0.48 | -0.36 |
| 154 | `M55` Guppy GMMA | **41.4** | 40 | 30 | 51 | 14 | BELUM CUKUP | 28 | 335/201 | -1.29 | 30 | -4.87 | -0.42 | 6.4 | -0.45 | -0.35 | -1.16 |
| 155 | `N35X36` Pecah 52 minggu tinggi → kelua | **41.4** | 23 | 28 | 36 | 30 | BELUM CUKUP | 13 | 60/11 | -3.14 | 17 | -1.73 | -0.27 | 3.0 | -0.85 | – | – |
| 156 | `N07X36` Tiga MA tersusun → keluar sele | **41.3** | 24 | 30 | 46 | 30 | BELUM CUKUP | 17 | 178/68 | -2.23 | 17 | -3.29 | -0.41 | 4.5 | -0.46 | – | – |
| 157 | `N24X17` Supertrend(10,3) + ADX>20 → ke | **41.3** | 25 | 26 | 43 | 30 | BELUM CUKUP | 15 | 137/63 | -3.76 | 17 | -3.04 | -0.31 | 4.6 | -0.72 | – | – |
| 158 | `M14` Walking with the Whales | **41.2** | 45 | 25 | 53 | 16 | BELUM CUKUP | 30 | 1182/913 | -0.70 | 30 | -10.97 | -0.67 | 9.5 | -0.32 | +0.22 | -0.61 |
| 159 | `M31` Band Walk (BB 20/2) | **41.1** | 45 | 17 | 57 | 31 | BELUM CUKUP | 26 | 405/209 | -0.86 | 30 | -5.14 | -0.31 | 9.5 | +0.22 | +0.79 | 0.43 |
| 160 | `M66` IBD Undur Pertama ke Purata 50 | **41.0** | 42 | 28 | 52 | 13 | BELUM CUKUP | 29 | 345/215 | -1.19 | 30 | -4.59 | -0.35 | 8.2 | -0.41 | -0.46 | -1.02 |
| 161 | `M139` 均线首次粘合向上发散 (MA berhimpun kali  | **41.0** | 30 | 40 | 49 | 12 | BELUM CUKUP | 26 | 111/59 | -3.13 | 30 | +1.98 | +0.18 | 5.4 | -0.43 | -0.68 | -1.46 |
| 162 | `N56X36` RSI>50 + ADX>20 → keluar selep | **41.0** | 25 | 27 | 45 | 30 | BELUM CUKUP | 17 | 230/156 | -1.97 | 17 | -5.80 | -0.44 | 7.5 | -0.75 | – | – |
| 163 | `N37X16` Gap and go → keluar bila super | **41.0** | 24 | 24 | 42 | 30 | BELUM CUKUP | 14 | 95/52 | -2.78 | 17 | -3.14 | -0.44 | 3.7 | -0.76 | – | – |
| 164 | `M134` First Kiss After Daylight (Lan | **40.9** | 29 | 32 | 51 | 15 | BELUM CUKUP | 22 | 70/41 | -2.33 | 30 | -3.73 | -0.34 | 5.9 | -0.04 | +0.12 | -0.04 |
| 165 | `N31X36` Turtle sistem 2 → keluar selep | **40.8** | 24 | 21 | 40 | 30 | BELUM CUKUP | 13 | 110/27 | -3.34 | 17 | -4.36 | -0.44 | 4.9 | -0.68 | – | – |
| 166 | `N119X15` 3 tutup turun berturut → ekori | **40.8** | 19 | 17 | 24 | 30 | BELUM CUKUP | 9 | 58/0 | -1.95 | 17 | -5.88 | -0.52 | 6.7 | -1.03 | – | – |
| 167 | `M57` Landry Trend Knockout (TKO) | **40.7** | 38 | 34 | 48 | 11 | BELUM CUKUP | 30 | 204/158 | -1.90 | 30 | -3.96 | -0.45 | 4.8 | -0.92 | -0.97 | -2.51 |
| 168 | `M29` EMA3 + RSI75 + Stokastik | **40.7** | 46 | 31 | 44 | 5 | BELUM CUKUP | 22 | 72/39 | -0.60 | 30 | -8.68 | -0.63 | 8.8 | -0.80 | -2.70 | -3.61 |
| 169 | `N42X15` Lonjakan volum 2x → ekori Chan | **40.7** | 36 | 24 | 30 | 30 | BELUM CUKUP | 17 | 209/0 | -1.15 | 17 | -6.21 | -0.46 | 7.4 | -0.57 | – | – |
| 170 | `N56X17` RSI>50 + ADX>20 → keluar bila  | **40.7** | 25 | 25 | 42 | 30 | BELUM CUKUP | 16 | 158/77 | -3.85 | 17 | -3.60 | -0.39 | 4.6 | -0.92 | – | – |
| 171 | `M148` Natural Number Method | **40.6** | 33 | 41 | 48 | 9 | BELUM CUKUP | 29 | 250/225 | -2.43 | 30 | -1.83 | -0.17 | 5.2 | -0.82 | -1.53 | -3.50 |
| 172 | `N42X16` Lonjakan volum 2x → keluar bil | **40.6** | 32 | 20 | 45 | 30 | BELUM CUKUP | 17 | 256/173 | -1.20 | 17 | -7.97 | -0.75 | 6.6 | -0.78 | – | – |
| 173 | `N45X36` Undur EMA21 cerun positif → ke | **40.6** | 22 | 26 | 46 | 30 | BELUM CUKUP | 16 | 175/105 | -2.31 | 17 | -4.99 | -0.43 | 6.1 | -0.65 | – | – |
| 174 | `N54X16` Supertrend + RSI>50 → keluar b | **40.5** | 21 | 22 | 40 | 30 | BELUM CUKUP | 13 | 135/72 | -5.49 | 17 | -3.07 | -0.33 | 5.7 | -1.11 | – | – |
| 175 | `M95` Nisbah Kebaharuan High 52 Ming | **40.4** | 32 | 28 | 52 | 15 | BELUM CUKUP | 24 | 138/83 | -1.49 | 30 | -7.54 | -0.60 | 7.2 | -0.19 | +0.08 | -0.43 |
| 176 | `N80X36` Tinggi sepanjang masa → keluar | **40.4** | 20 | 22 | 35 | 30 | BELUM CUKUP | 12 | 46/9 | -3.75 | 17 | -3.84 | -0.55 | 3.8 | -0.80 | – | – |
| 177 | `N51X36` BB squeeze + Supertrend → kelu | **40.4** | 17 | 27 | 26 | 30 | BELUM CUKUP | 11 | 17/6 | -3.34 | 17 | -5.82 | -0.68 | 4.8 | -1.72 | – | – |
| 178 | `N24X16` Supertrend(10,3) + ADX>20 → ke | **40.3** | 22 | 24 | 44 | 30 | BELUM CUKUP | 15 | 130/62 | -4.23 | 17 | -3.50 | -0.38 | 4.6 | -0.65 | – | – |
| 179 | `N56X16` RSI>50 + ADX>20 → keluar bila  | **40.2** | 21 | 27 | 46 | 30 | BELUM CUKUP | 17 | 284/204 | -1.82 | 17 | -5.68 | -0.54 | 5.7 | -0.60 | – | – |
| 180 | `M140` 猎豹出击 (Serangan Cheetah) | **40.2** | 26 | 27 | 38 | 14 | BELUM CUKUP | 15 | 47/26 | -3.10 | 30 | -5.59 | -0.59 | 5.3 | -1.17 | -0.24 | -1.22 |
| 181 | `N57X16` ADX bangkit daripada <20 → kel | **40.1** | 22 | 23 | 42 | 30 | BELUM CUKUP | 15 | 79/42 | -4.60 | 17 | -3.09 | -0.35 | 4.8 | -0.66 | – | – |
| 182 | `M11` NR7 Breakout + Volume | **40.0** | 38 | 24 | 52 | 14 | BELUM CUKUP | 27 | 143/106 | -0.55 | 30 | -10.44 | -0.61 | 10.1 | -0.37 | -0.36 | -0.41 |
| 183 | `M152` Spike & Ledge | **39.9** | 26 | 36 | 44 | 16 | BELUM CUKUP | 24 | 61/15 | -2.82 | 30 | -1.30 | -0.10 | 5.4 | -0.43 | +0.32 | -1.20 |
| 184 | `N41X16` CMF20>0 + tutup>EMA20 → keluar | **39.8** | 20 | 28 | 43 | 30 | BELUM CUKUP | 17 | 371/287 | -2.41 | 17 | -4.85 | -0.48 | 5.4 | -1.00 | – | – |
| 185 | `N42X17` Lonjakan volum 2x → keluar bil | **39.6** | 33 | 14 | 47 | 30 | BELUM CUKUP | 17 | 245/92 | -0.84 | 17 | -11.13 | -0.75 | 9.0 | -0.50 | – | – |
| 186 | `N74X16` MACD atas garis isyarat (keada | **39.5** | 22 | 24 | 41 | 30 | BELUM CUKUP | 17 | 876/754 | -1.48 | 17 | -9.89 | -0.72 | 7.2 | -1.21 | – | – |
| 187 | `M06` Minervini VCP Breakout | **39.3** | 29 | 33 | 48 | 10 | BELUM CUKUP | 26 | 96/61 | -2.96 | 30 | -3.38 | -0.36 | 4.7 | -0.61 | -1.19 | -1.62 |
| 188 | `N08X16` tutup>EMA20 tidak terlalu jauh | **39.3** | 19 | 27 | 41 | 30 | BELUM CUKUP | 17 | 661/533 | -1.78 | 17 | -8.33 | -0.71 | 5.7 | -1.19 | – | – |
| 189 | `N22X14` BB pecah atas + RSI → keluar b | **39.3** | 20 | 21 | 45 | 30 | BELUM CUKUP | 16 | 139/58 | -4.09 | 17 | -7.06 | -0.58 | 6.8 | -0.51 | – | – |
| 190 | `N50X14` Mampat + pecah volum 1.5x → ke | **39.3** | 22 | 18 | 35 | 30 | BELUM CUKUP | 14 | 43/11 | -1.47 | 17 | -9.04 | -0.64 | 7.7 | -0.97 | – | – |
| 191 | `M99` Three Line Break | **39.2** | 30 | 31 | 51 | 12 | BELUM CUKUP | 28 | 220/146 | -2.49 | 30 | -2.68 | -0.21 | 6.0 | -0.52 | -0.93 | -1.89 |
| 192 | `N36X14` Pocket pivot → keluar bila rsi | **39.2** | 23 | 20 | 42 | 30 | BELUM CUKUP | 17 | 212/83 | -2.91 | 17 | -4.66 | -0.46 | 5.6 | -0.98 | – | – |
| 193 | `N28X17` ADX>25 + DI+ > DI- → keluar bi | **38.8** | 20 | 23 | 38 | 30 | BELUM CUKUP | 17 | 181/21 | -2.18 | 17 | -4.99 | -0.41 | 6.3 | -0.88 | – | – |
| 194 | `N29X36` PSAR naik + tutup>MA50 → kelua | **38.8** | 19 | 20 | 41 | 30 | BELUM CUKUP | 16 | 207/129 | -2.89 | 17 | -8.86 | -0.61 | 10.1 | -1.14 | – | – |
| 195 | `M59` Anjakan Julat RSI | **38.7** | 25 | 22 | 44 | 3 | BELUM CUKUP | 14 | 36/24 | -5.55 | 30 | -4.22 | -0.41 | 5.9 | -0.38 | -3.13 | -1.26 |
| 196 | `N22X16` BB pecah atas + RSI → keluar b | **38.6** | 18 | 17 | 46 | 30 | BELUM CUKUP | 15 | 129/81 | -5.24 | 17 | -5.89 | -0.56 | 6.1 | -0.50 | – | – |
| 197 | `N28X14` ADX>25 + DI+ > DI- → keluar bi | **38.5** | 18 | 22 | 43 | 30 | BELUM CUKUP | 17 | 283/77 | -1.99 | 17 | -7.01 | -0.47 | 7.6 | -0.81 | – | – |
| 198 | `N50X17` Mampat + pecah volum 1.5x → ke | **38.5** | 20 | 16 | 34 | 30 | BELUM CUKUP | 14 | 42/9 | -1.46 | 17 | -10.18 | -0.65 | 8.9 | -0.94 | – | – |
| 199 | `N39X36` NR7 kemudian pecah → keluar se | **38.5** | 9 | 7 | 32 | 30 | BELUM CUKUP | 9 | 36/12 | -4.61 | 16 | -11.04 | -0.73 | 9.3 | -1.13 | – | – |
| 200 | `N27X36` Ichimoku atas awan → keluar se | **38.4** | 19 | 18 | 41 | 30 | BELUM CUKUP | 16 | 136/54 | -2.93 | 17 | -6.80 | -0.53 | 6.8 | -0.92 | – | – |
| 201 | `M141` First Thrust (Landry) | **38.4** | 9 | 7 | 36 | 15 | BELUM CUKUP | 9 | 27/18 | -6.73 | 30 | -13.64 | -0.73 | 9.1 | -1.06 | – | -3.90 |
| 202 | `M155` Market Cycle Strategy | **37.9** | 29 | 27 | 47 | 14 | BELUM CUKUP | 30 | 836/649 | -4.01 | 30 | -3.96 | -0.34 | 5.9 | -0.98 | -0.13 | -2.48 |
| 203 | `M101` Bulkowski: Tiga lembah menaik | **37.9** | 24 | 16 | 51 | 22 | BELUM CUKUP | 19 | 48/29 | -2.38 | 30 | -7.88 | -0.53 | 9.5 | +0.13 | -0.83 | 0.33 |
| 204 | `M02` MACD + SMA200 | **37.8** | 31 | 22 | 47 | 18 | BELUM CUKUP | 30 | 158/128 | -3.43 | 30 | -3.35 | -0.21 | 7.6 | -1.03 | -0.37 | -6.60 |
| 205 | `M125` 2-Bar Breakout | **37.6** | 28 | 26 | 50 | 12 | BELUM CUKUP | 30 | 1240/686 | -3.12 | 30 | -5.24 | -0.36 | 6.7 | -0.68 | -0.68 | -0.40 |
| 206 | `M47` Holy Grail Raschke | **37.3** | 24 | 22 | 36 | 15 | BELUM CUKUP | 20 | 56/39 | -1.55 | 30 | -9.17 | -0.73 | 7.6 | -1.72 | – | -14.18 |
| 207 | `N47X16` NR7 + EMA9>EMA21 → keluar bila | **36.8** | 13 | 18 | 45 | 30 | BELUM CUKUP | 17 | 214/112 | -2.53 | 17 | -10.22 | -0.74 | 8.3 | -0.76 | – | – |
| 208 | `N29X16` PSAR naik + tutup>MA50 → kelua | **36.8** | 15 | 17 | 40 | 30 | BELUM CUKUP | 17 | 278/199 | -3.19 | 17 | -8.45 | -0.71 | 7.3 | -1.34 | – | – |
| 209 | `M19` Sneaky Pivot (proksi harian) | **36.7** | 23 | 27 | 48 | 13 | BELUM CUKUP | 28 | 525/363 | -3.48 | 30 | -5.30 | -0.36 | 7.0 | -0.88 | -0.65 | -11.50 |
| 210 | `M79` Radge: 20% Flipper | **36.6** | 25 | 26 | 46 | 12 | BELUM CUKUP | 29 | 436/256 | -5.01 | 30 | -4.40 | -0.28 | 8.6 | -1.07 | -0.76 | -2.27 |
| 211 | `N54X36` Supertrend + RSI>50 → keluar s | **36.4** | 15 | 12 | 41 | 30 | BELUM CUKUP | 16 | 217/146 | -2.77 | 17 | -11.09 | -0.78 | 9.7 | -1.15 | – | – |
| 212 | `M161` EMA 10/21 + Supertrend (10,3) | **36.2** | 30 | 15 | 54 | 18 | BELUM CUKUP | 30 | 592/397 | -0.90 | 30 | -15.39 | -0.70 | 12.9 | -0.11 | +0.85 | -0.26 |
| 213 | `M154` HOLP (High of Low Period) | **35.8** | 18 | 21 | 45 | 13 | BELUM CUKUP | 22 | 136/53 | -2.18 | 30 | -9.09 | -0.59 | 8.9 | -0.86 | -0.56 | -3.51 |
| 214 | `M76` Undercut & Rally pada Low Pent | **35.6** | 21 | 24 | 47 | 8 | BELUM CUKUP | 26 | 101/85 | -2.17 | 30 | -9.14 | -0.62 | 8.7 | -0.88 | -1.74 | -3.78 |
| 215 | `N47X36` NR7 + EMA9>EMA21 → keluar sele | **35.6** | 8 | 13 | 42 | 30 | BELUM CUKUP | 15 | 192/87 | -3.04 | 17 | -14.29 | -0.73 | 11.8 | -1.00 | – | – |
| 216 | `M82` Arthur Hill Rotasi Sasaran 10% | **35.2** | 30 | 13 | 53 | 17 | BELUM CUKUP | 30 | 613/310 | -1.45 | 30 | -7.07 | -0.36 | 12.1 | -0.32 | +0.61 | -1.35 |
| 217 | `M01` Bollinger Band + RSI | **34.6** | 30 | 9 | 45 | 18 | BELUM CUKUP | 25 | 140/33 | -0.96 | 30 | -12.53 | -0.75 | 7.8 | -0.74 | +0.81 | -2.58 |
| 218 | `M147` Improved Three-Bar Pullback | **34.1** | 13 | 15 | 40 | 10 | BELUM CUKUP | 19 | 125/64 | -5.21 | 30 | -13.32 | -0.63 | 10.2 | -1.40 | -1.42 | -1.36 |
| 219 | `M81` Bensdorp Long Trend High Momen | **33.9** | 3 | 7 | 44 | 16 | BELUM CUKUP | 13 | 432/225 | -5.04 | 30 | -22.03 | -0.83 | 17.3 | -0.91 | +0.37 | -2.78 |
| 220 | `M123` CCI Correction (Lambert, Chart | **33.1** | 16 | 22 | 38 | 11 | BELUM CUKUP | 28 | 221/194 | -1.74 | 30 | -14.80 | -0.88 | 9.7 | -2.01 | -1.15 | -4.10 |
| 221 | `M122` Moving Momentum (ChartSchool) | **32.8** | 17 | 20 | 42 | 9 | BELUM CUKUP | 29 | 139/85 | -3.69 | 30 | -10.52 | -0.63 | 8.5 | -1.54 | -1.57 | -4.92 |
| 222 | `M90` Pring KST | **32.7** | 15 | 17 | 47 | 10 | BELUM CUKUP | 27 | 98/68 | -3.31 | 30 | -12.73 | -0.64 | 13.5 | -0.79 | -1.45 | -2.92 |
| 223 | `M09` Volumatic VIDYA Pivot Retest | **30.4** | 3 | 10 | 31 | 6 | BELUM CUKUP | 18 | 50/33 | -4.66 | 30 | -17.51 | -0.92 | 11.5 | -2.14 | -2.37 | -11.33 |
| 224 | `M159` Heikin-Ashi Trend | **30.0**⌈ | 54 | 69 | 47 | 53 | GAGAL | 30 | 2196/1978 | -0.77 | 30 | +11.22 | +1.83 | 3.3 | -0.99 | -0.57 | -5.62 |
| 225 | `M20` EMA10/15 Crossover + Sudut | **30.0**⌈ | 44 | 39 | 48 | 12 | GAGAL | 30 | 685/539 | -1.04 | 30 | -4.49 | -0.40 | 5.2 | -0.86 | -0.78 | -5.54 |
| 226 | `M28` VWAP Separator + Kiss Pivot | **30.0**⌈ | 43 | 34 | 47 | 14 | GAGAL | 26 | 172/134 | -1.00 | 30 | -6.12 | -0.63 | 6.2 | -0.87 | -0.33 | -6.39 |
| 227 | `M03` BB Break + Divergence RSI | **30.0**⌈ | 15 | 23 | 47 | 14 | GAGAL | 30 | 548/423 | -1.93 | 30 | -9.73 | -0.66 | 6.9 | -0.93 | -0.27 | -3.54 |

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

