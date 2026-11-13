# Skor Kaedah 0–100 (pangkat maklumat, BUKAN keputusan)

> **Status keputusan (kad skor, harga 2026-11-12):** TERBUKTI 0 · CALON 0 · BELUM CUKUP 223 · GAGAL 0 · NEGATIF 0. Rejim QQQ OFF sejak 2026-10-16. Hanya **TERBUKTI** layak untuk wang sebenar (`laporan/KAD_SKOR.md`); nombor dalam laporan ini BUKAN keputusan dan tidak boleh dibaca sebagai pangkat untuk wang sebenar.

Dijana 2026-11-13 oleh `standard/skor_kaedah.py` (Actions `analisis.yml`, selepas kad skor). Harga pada tutup 2026-11-12; 223 kaedah; 20 hari beli langsung (rejim ON 1, OFF 19). Pradaftar 2026-11-09: `standard/SPEC_SKOR_KAEDAH.md` (berat dan sauh dikunci `ujian/test_skor_kaedah.py::TestKunci`). Rekod analisis sahaja: tiada order, tiada wang sebenar.

## Cara membaca

- **Skor** = min geometri berberat empat tiang (Untung 35 · Tahan 30 · Bukti 25 · Konsisten 10), dikecut ke 50 mengikut data: berat data = hari beli ÷ (hari beli + 20). Kaedah dengan 2 hari beli tidak boleh menjauhi 50. 100 = unggul semua segi; 50 = neutral/tiada bukti; < 50 = lebih buruk daripada neutral.
- **Siling** ikut kad skor: NEGATIF ≤ 20, GANTUNG/BERSARA ≤ 30, GAGAL ≤ 40. Tanda ⌈ = siling terpakai.
- **Satu-satunya status yang membenarkan wang sebenar ialah TERBUKTI dalam `laporan/KAD_SKOR.md`.** Skor tinggi dengan status BELUM CUKUP bermaksud "paling menjanjikan setakat ini", bukan "selamat".
- Deflasi ujian berganda (López de Prado): sauh t Bukti C1 = maks(2.0, E[maks 223 normal]) = 2.80.
- **Semakan kebolehramalan:** belum ada snapshot skor ≥ 7 hari lalu (sejarah bermula 2026-11-12); skor dipercayai sebagai pangkat hanya selepas 8–12 minggu semakan positif.
- Metrik T4 (A2, B1, B2, D1) dikira atas lorong T4 L1 **dipotong pada sesi LANGSUNG pertama** kaedah itu (Mxx 2026-10-16, Nxx/GB 2026-11-03) dan diasas semula; sesi isian bina semula tidak dikira (pindaan 9 Nov 2026 (a)). Lajur "T4 sesi/pul" di bawah ialah potongan itu, bukan lorong penuh `T4_KAEDAH.md`.

## Semua kaedah, susun ikut Skor

| # | Kaedah | Skor | Untung | Tahan | Bukti | Konsisten | Status kad | Hari beli | Posisi/tutup | Jangkaan % | T4 sesi | T4 pul % | T4 pul/|MDD| | Ulcer | t buku | Lift | WFE |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `M146` 3-Bar Momentum Pattern | **62.4** | 81 | 81 | 62 | 85 | BELUM CUKUP | 18 | 78/30 | +1.07 | 20 | +5.51 | +0.90 | 2.3 | +1.49 | – | 2.63 |
| 2 | `M133` Bull Hook (Crabel) | **61.4** | 86 | 85 | 59 | 85 | BELUM CUKUP | 14 | 50/25 | +1.13 | 20 | +6.83 | +1.65 | 1.5 | +1.30 | – | 12.13 |
| 3 | `M33` Supertrend + SMA10 | **60.3** | 73 | 75 | 59 | 85 | BELUM CUKUP | 20 | 221/42 | +0.54 | 20 | +8.71 | +3.26 | 1.5 | +0.89 | – | 3.50 |
| 4 | `M118` Expansion Pivot (Cooper) | **59.8** | 68 | 80 | 56 | 85 | BELUM CUKUP | 20 | 86/22 | +0.16 | 20 | +8.99 | +3.32 | 1.1 | +0.85 | – | 2.31 |
| 5 | `M151` Outside Bar Failure | **59.3** | 68 | 81 | 55 | 80 | BELUM CUKUP | 19 | 103/49 | -0.22 | 20 | +6.65 | +4.13 | 0.6 | +0.44 | – | 0.82 |
| 6 | `M74` Lulus Baharu Trend Template Mi | **58.6** | 67 | 78 | 55 | 73 | BELUM CUKUP | 20 | 93/56 | -0.09 | 20 | +4.17 | +1.00 | 2.2 | +0.38 | – | 0.60 |
| 7 | `M142` Pecahan volum dari dasar (底部放量 | **58.3** | 79 | 81 | 46 | 77 | BELUM CUKUP | 15 | 48/5 | +1.34 | 18 | +4.29 | +0.89 | 1.8 | +0.54 | – | 0.74 |
| 8 | `M25` VWAP Wave (proksi harian) | **58.1** | 65 | 75 | 58 | 79 | BELUM CUKUP | 18 | 180/90 | -0.22 | 20 | +5.47 | +0.95 | 3.0 | +0.57 | – | 3.25 |
| 9 | `M100` Bulkowski Segi Empat & Segi Ti | **57.0** | 65 | 73 | 55 | 85 | BELUM CUKUP | 15 | 60/40 | +0.28 | 20 | +3.48 | +0.80 | 2.0 | +0.66 | – | 2.77 |
| 10 | `M10` EMA3 + CCI + MACD | **56.8** | 62 | 67 | 55 | 85 | BELUM CUKUP | 20 | 124/53 | -0.40 | 20 | +9.59 | +1.82 | 2.0 | +0.41 | – | 0.99 |
| 11 | `M160` Measured Move Up | **55.7** | 51 | 72 | 60 | 85 | BELUM CUKUP | 18 | 113/47 | -0.80 | 20 | +3.63 | +0.78 | 2.0 | +1.09 | – | 8.00 |
| 12 | `M93` Bollinger Kaedah II: %b + MFI | **55.7** | 68 | 54 | 59 | 69 | BELUM CUKUP | 20 | 266/75 | +0.65 | 20 | +1.30 | +0.21 | 2.7 | +0.75 | – | 0.89 |
| 13 | `M13` Garis Trend Action/Safety Line | **55.0** | 59 | 71 | 52 | 55 | BELUM CUKUP | 20 | 761/453 | -0.68 | 20 | +8.34 | +2.34 | 1.3 | -0.22 | – | -0.36 |
| 14 | `M48` Cooper 1-2-3-4 | **54.9** | 63 | 58 | 53 | 85 | BELUM CUKUP | 17 | 58/16 | -0.21 | 20 | +8.56 | +1.57 | 2.0 | +0.68 | – | 1.65 |
| 15 | `M111` Sistem Volatiliti Wilder | **54.4** | 56 | 57 | 57 | 85 | BELUM CUKUP | 20 | 263/84 | -0.34 | 20 | +3.65 | +0.54 | 3.5 | +0.45 | – | 0.99 |
| 16 | `M159` Heikin-Ashi Trend | **54.4** | 58 | 68 | 51 | 55 | BELUM CUKUP | 20 | 1709/1248 | -0.36 | 20 | +5.07 | +0.83 | 3.6 | -0.34 | – | -1.58 |
| 17 | `N75X17` RSI14 < 40 tanpa penapis → kel | **54.3** | 72 | 82 | 45 | 70 | BELUM CUKUP | 7 | 276/130 | +0.94 | 7 | +3.05 | +0.76 | 2.0 | -0.35 | – | – |
| 18 | `M23` Breitstein Kapitulasi + Kesina | **54.2** | 54 | 57 | 60 | 77 | BELUM CUKUP | 20 | 126/77 | -0.52 | 20 | -0.34 | -0.07 | 2.2 | +0.77 | – | 2.78 |
| 19 | `M124` 'Last' Stochastic Technique (C | **53.7** | 52 | 67 | 55 | 60 | BELUM CUKUP | 20 | 392/184 | -0.74 | 20 | +3.71 | +0.81 | 2.3 | +0.09 | – | 0.18 |
| 20 | `M145` Yum-Yum Continuation | **53.7** | 52 | 68 | 54 | 58 | BELUM CUKUP | 20 | 308/64 | -0.61 | 20 | +4.27 | +1.96 | 1.3 | +0.14 | – | 0.11 |
| 21 | `M137` Livermore System | **53.6** | 50 | 65 | 54 | 68 | BELUM CUKUP | 20 | 174/60 | -0.91 | 20 | +4.78 | +0.81 | 2.3 | +0.24 | – | 0.44 |
| 22 | `M91` Stochastic Pop (Bernstein/Stec | **53.5** | 53 | 62 | 52 | 85 | BELUM CUKUP | 15 | 38/16 | -1.01 | 20 | +6.75 | +0.86 | 3.1 | +0.59 | – | 2.29 |
| 23 | `M02` MACD + SMA200 | **53.3** | 56 | 66 | 49 | 55 | BELUM CUKUP | 20 | 122/70 | -0.94 | 20 | +10.84 | +2.45 | 1.7 | -0.39 | – | -1.74 |
| 24 | `N75X14` RSI14 < 40 tanpa penapis → kel | **52.9** | 77 | 62 | 41 | 70 | BELUM CUKUP | 7 | 194/37 | +1.74 | 7 | -1.78 | -0.32 | 3.3 | -0.41 | – | – |
| 25 | `M89` Chande 65sma-3cc | **52.8** | 50 | 58 | 55 | 74 | BELUM CUKUP | 20 | 177/82 | -0.71 | 20 | +2.08 | +0.34 | 2.9 | +0.27 | – | 0.63 |
| 26 | `N19X13` Bawah jalur BB + RSI<30 → kelu | **52.4** | 85 | 72 | 34 | 58 | BELUM CUKUP | 5 | 101/0 | +3.89 | 7 | -0.61 | -0.18 | 2.4 | +0.39 | – | – |
| 27 | `M158` Doubly Adaptive Profit Targets | **52.4** | 62 | 46 | 61 | 45 | BELUM CUKUP | 20 | 362/130 | +0.42 | 20 | -1.79 | -0.29 | 3.0 | +0.80 | – | 1.91 |
| 28 | `N40X16` OBV tinggi baharu + MA50 → kel | **52.2** | 69 | 54 | 48 | 70 | BELUM CUKUP | 7 | 73/23 | +0.65 | 7 | +0.41 | +0.08 | 2.6 | +0.62 | – | – |
| 29 | `N124X15` Episodic pivot gap 8-10% → eko | **52.2** | 81 | 63 | 32 | 70 | BELUM CUKUP | 7 | 40/0 | +2.01 | 7 | -0.30 | -0.05 | 3.1 | -0.07 | – | – |
| 30 | `M46` Jurang Naik Boleh Beli (Buyabl | **52.2** | 51 | 66 | 48 | 64 | BELUM CUKUP | 13 | 36/20 | -0.82 | 20 | +2.11 | +0.43 | 1.6 | +0.20 | – | 0.30 |
| 31 | `N40X36` OBV tinggi baharu + MA50 → kel | **52.1** | 71 | 52 | 47 | 70 | BELUM CUKUP | 7 | 59/11 | +0.85 | 7 | -0.14 | -0.03 | 2.6 | +0.74 | – | – |
| 32 | `N53X36` Supertrend + ADX>25 → keluar s | **52.1** | 65 | 55 | 50 | 70 | BELUM CUKUP | 7 | 115/26 | +0.34 | 7 | +0.64 | +0.16 | 2.2 | +0.70 | – | – |
| 33 | `M30` BB Free Bar + Himpitan 50/2.5 | **52.1** | 55 | 49 | 58 | 62 | BELUM CUKUP | 19 | 228/71 | -0.26 | 20 | +2.02 | +0.27 | 4.7 | +0.60 | – | 1.08 |
| 34 | `N75X13` RSI14 < 40 tanpa penapis → kel | **51.9** | 78 | 59 | 33 | 70 | BELUM CUKUP | 7 | 128/1 | +1.84 | 7 | -2.21 | -0.59 | 2.2 | -0.13 | – | – |
| 35 | `M129` Wick Play | **51.9** | 52 | 61 | 46 | 85 | BELUM CUKUP | 10 | 26/10 | -0.86 | 20 | +4.84 | +1.72 | 1.0 | +0.30 | – | 1.12 |
| 36 | `M77` Undercut & Rally pada Purata B | **51.9** | 54 | 62 | 46 | 55 | BELUM CUKUP | 17 | 54/33 | -0.34 | 20 | +0.35 | +0.11 | 1.6 | -0.34 | – | -0.48 |
| 37 | `N75X15` RSI14 < 40 tanpa penapis → eko | **51.8** | 80 | 59 | 31 | 70 | BELUM CUKUP | 7 | 127/0 | +1.96 | 7 | -2.21 | -0.59 | 2.2 | -0.10 | – | – |
| 38 | `N45X16` Undur EMA21 cerun positif → ke | **51.7** | 48 | 77 | 45 | 70 | BELUM CUKUP | 7 | 131/51 | -0.88 | 7 | +5.61 | +3.93 | 0.7 | -0.07 | – | – |
| 39 | `M70` Pecahan Hari Dalam | **51.7** | 60 | 67 | 54 | 18 | BELUM CUKUP | 20 | 464/363 | -0.40 | 20 | +2.22 | +0.45 | 2.3 | -0.01 | – | -0.01 |
| 40 | `M105` Supertrend tulen | **51.6** | 52 | 49 | 58 | 59 | BELUM CUKUP | 20 | 366/105 | -0.32 | 20 | +0.93 | +0.13 | 3.6 | +0.42 | – | 1.04 |
| 41 | `N64X36` Episodic pivot → keluar selepa | **51.3** | 60 | 66 | 36 | 70 | BELUM CUKUP | 7 | 49/6 | +0.40 | 7 | +0.94 | +0.23 | 2.1 | -0.36 | – | – |
| 42 | `N64X17` Episodic pivot → keluar bila a | **51.3** | 60 | 64 | 37 | 70 | BELUM CUKUP | 7 | 49/10 | +0.30 | 7 | +0.73 | +0.18 | 2.0 | -0.41 | – | – |
| 43 | `M104` High Tight Flag / Power Play | **51.1** | 77 | 90 | 51 | 85 | BELUM CUKUP | 1 | 1/0 | +20.54 | 5 | +2.07 | +10.00 | 0.0 | +3.36 | – | 22.53 |
| 44 | `M92` CCI-50 | **51.1** | 56 | 53 | 54 | 36 | BELUM CUKUP | 20 | 552/335 | -0.11 | 20 | +0.13 | +0.02 | 2.7 | +0.04 | – | 0.07 |
| 45 | `M117` Landry Pullback (high 2 bulan) | **50.6** | 59 | 42 | 56 | 44 | BELUM CUKUP | 17 | 148/18 | +0.65 | 20 | -5.25 | -0.67 | 4.0 | +1.05 | – | 0.98 |
| 46 | `M80` Radge Saluran Purata Bergerak  | **50.6** | 58 | 44 | 58 | 40 | BELUM CUKUP | 20 | 287/57 | +0.30 | 20 | -1.93 | -0.27 | 4.1 | +0.67 | – | 0.85 |
| 47 | `N64X16` Episodic pivot → keluar bila s | **50.4** | 59 | 55 | 35 | 70 | BELUM CUKUP | 7 | 49/5 | +0.48 | 7 | -1.27 | -0.32 | 2.0 | -0.36 | – | – |
| 48 | `N48X36` Inside day pecah → keluar sele | **50.3** | 55 | 49 | 43 | 70 | BELUM CUKUP | 7 | 302/173 | +0.45 | 7 | -2.45 | -0.29 | 5.7 | -0.54 | – | – |
| 49 | `N28X36` ADX>25 + DI+ > DI- → keluar se | **50.3** | 54 | 48 | 45 | 70 | BELUM CUKUP | 7 | 269/139 | +0.13 | 7 | -1.36 | -0.22 | 3.8 | -0.32 | – | – |
| 50 | `N73X13` Tutup bawah jalur bawah BB(20, | **50.3** | 74 | 56 | 34 | 30 | BELUM CUKUP | 7 | 137/1 | +1.70 | 7 | -3.47 | -0.55 | 3.3 | -0.07 | – | – |
| 51 | `M35` Pocket Pivot Morales & Kacher | **50.2** | 55 | 44 | 56 | 45 | BELUM CUKUP | 20 | 310/213 | -0.18 | 20 | -3.23 | -0.35 | 5.0 | +0.22 | – | 1.09 |
| 52 | `M05` MACD Divergence + Pengesahan | **50.2** | 46 | 63 | 43 | 55 | BELUM CUKUP | 15 | 41/12 | -0.97 | 20 | +1.94 | +0.57 | 1.4 | -0.34 | – | -0.51 |
| 53 | `M37` Weinstein Peringkat 2 | **50.1** | 58 | 71 | 26 | 55 | BELUM CUKUP | 3 | 7/0 | +0.12 | 14 | +0.23 | +0.27 | 0.3 | -0.35 | – | -0.25 |
| 54 | `N42X15` Lonjakan volum 2x → ekori Chan | **50.1** | 68 | 51 | 28 | 70 | BELUM CUKUP | 7 | 157/0 | +0.83 | 7 | +0.18 | +0.02 | 5.5 | -0.45 | – | – |
| 55 | `M153` Range Leader | **49.9** | 52 | 43 | 58 | 45 | BELUM CUKUP | 20 | 1286/1074 | +0.03 | 20 | -2.95 | -0.30 | 6.3 | +0.43 | – | 2.17 |
| 56 | `N64X14` Episodic pivot → keluar bila r | **49.9** | 55 | 55 | 32 | 70 | BELUM CUKUP | 7 | 49/2 | +0.32 | 7 | -1.27 | -0.32 | 2.0 | -0.40 | – | – |
| 57 | `N42X14` Lonjakan volum 2x → keluar bil | **49.8** | 59 | 45 | 37 | 70 | BELUM CUKUP | 7 | 168/14 | +0.54 | 7 | -2.72 | -0.25 | 5.5 | -0.50 | – | – |
| 58 | `M01` Bollinger Band + RSI | **49.5** | 77 | 45 | 46 | 15 | BELUM CUKUP | 20 | 113/21 | +2.35 | 20 | -4.95 | -0.46 | 4.3 | -0.29 | – | -1.24 |
| 59 | `N36X36` Pocket pivot → keluar selepas  | **49.5** | 45 | 56 | 39 | 70 | BELUM CUKUP | 7 | 142/56 | -1.04 | 7 | +2.98 | +0.57 | 2.4 | -0.87 | – | – |
| 60 | `N25X36` Supertrend + EMA + ADX>23 → ke | **49.5** | 46 | 53 | 40 | 70 | BELUM CUKUP | 7 | 119/23 | -0.75 | 7 | +0.03 | +0.01 | 2.4 | -0.40 | – | – |
| 61 | `N42X17` Lonjakan volum 2x → keluar bil | **49.4** | 53 | 42 | 42 | 70 | BELUM CUKUP | 7 | 181/49 | +0.27 | 7 | -4.08 | -0.42 | 5.2 | -0.44 | – | – |
| 62 | `N42X36` Lonjakan volum 2x → keluar sel | **49.2** | 51 | 40 | 42 | 70 | BELUM CUKUP | 7 | 181/85 | +0.19 | 7 | -3.99 | -0.54 | 4.2 | -0.59 | – | – |
| 63 | `M07` Qullamaggie Breakout | **49.2** | 26 | 64 | 27 | 15 | BELUM CUKUP | 1 | 1/1 | -2.53 | 20 | -0.25 | -0.21 | 0.7 | -0.22 | – | -1.12 |
| 64 | `M132` Ascending Scallop (Bulkowski) | **49.1** | 34 | 64 | 50 | 63 | BELUM CUKUP | 17 | 94/37 | -1.73 | 20 | +3.29 | +0.88 | 2.2 | +0.04 | – | 0.28 |
| 65 | `N24X36` Supertrend(10,3) + ADX>20 → ke | **49.0** | 50 | 40 | 42 | 70 | BELUM CUKUP | 7 | 138/42 | -0.39 | 7 | -1.92 | -0.42 | 2.8 | -0.39 | – | – |
| 66 | `N36X16` Pocket pivot → keluar bila sup | **49.0** | 38 | 58 | 39 | 70 | BELUM CUKUP | 7 | 146/50 | -1.23 | 7 | +1.52 | +0.58 | 1.2 | -0.84 | – | – |
| 67 | `M45` High 52 Minggu (George & Hwang | **49.0** | 16 | 44 | 31 | 42 | BELUM CUKUP | 1 | 2/1 | -3.75 | 9 | -0.73 | -0.40 | 1.0 | +0.22 | – | 0.91 |
| 68 | `N43X36` Undur EMA8 + penapis MA50 → ke | **48.9** | 43 | 49 | 38 | 70 | BELUM CUKUP | 7 | 153/29 | -0.72 | 7 | -0.29 | -0.07 | 2.1 | -0.69 | – | – |
| 69 | `M51` O'Neil Cawan & Pemegang | **48.9** | 32 | 51 | 33 | 45 | BELUM CUKUP | 2 | 3/0 | -1.47 | 10 | -0.38 | -0.38 | 0.6 | +0.51 | – | 1.85 |
| 70 | `M27` Price Action 4 Tiang | **48.8** | 41 | 39 | 41 | 15 | BELUM CUKUP | 2 | 547/438 | -0.97 | 20 | -2.76 | -0.54 | 2.9 | -0.56 | – | -1.66 |
| 71 | `M15` Break & Retest + Henti ATR | **48.7** | 55 | 43 | 55 | 26 | BELUM CUKUP | 20 | 301/163 | +0.15 | 20 | -4.19 | -0.52 | 3.9 | +0.17 | – | 0.37 |
| 72 | `M39` Radge Pecahan Bollinger 100 ha | **48.7** | 33 | 65 | 50 | 55 | BELUM CUKUP | 20 | 239/49 | -2.02 | 20 | +6.46 | +2.70 | 1.2 | -0.13 | – | -0.27 |
| 73 | `N37X17` Gap and go → keluar bila adx14 | **48.7** | 39 | 56 | 35 | 70 | BELUM CUKUP | 7 | 82/24 | -1.05 | 7 | +1.67 | +0.45 | 1.9 | -0.92 | – | – |
| 74 | `N08X36` tutup>EMA20 tidak terlalu jauh | **48.6** | 40 | 47 | 40 | 70 | BELUM CUKUP | 7 | 326/175 | -0.76 | 7 | -1.26 | -0.23 | 2.8 | -0.89 | – | – |
| 75 | `N16X13` RSI2<10 tanpa penapis → keluar | **48.6** | 49 | 45 | 32 | 70 | BELUM CUKUP | 7 | 115/4 | +0.12 | 7 | -2.62 | -0.29 | 6.0 | -0.64 | – | – |
| 76 | `M94` Pecutan Momentum (Chen, Yu & W | **48.6** | 19 | 20 | 22 | 37 | BELUM CUKUP | 1 | 33/0 | -4.75 | 9 | -3.67 | -0.31 | 6.9 | -0.51 | – | -2.30 |
| 77 | `M84` Jarak purata bergerak MAD 21/2 | **48.5** | 16 | 16 | 34 | 15 | BELUM CUKUP | 1 | 58/37 | -3.76 | 9 | -6.77 | -0.86 | 6.1 | -0.62 | – | -2.13 |
| 78 | `M88` O'Neil Shakeout +3 | **48.4** | 40 | 49 | 49 | 57 | BELUM CUKUP | 16 | 73/30 | -1.33 | 20 | +0.79 | +0.08 | 4.3 | +0.05 | – | 0.08 |
| 79 | `N124X36` Episodic pivot gap 8-10% → kel | **48.4** | 55 | 39 | 38 | 39 | BELUM CUKUP | 7 | 40/13 | +0.40 | 7 | -3.75 | -0.76 | 3.2 | -0.40 | – | – |
| 80 | `N37X36` Gap and go → keluar selepas DU | **48.3** | 37 | 55 | 35 | 70 | BELUM CUKUP | 7 | 82/18 | -1.14 | 7 | +1.32 | +0.36 | 2.0 | -0.88 | – | – |
| 81 | `N42X16` Lonjakan volum 2x → keluar bil | **48.3** | 48 | 35 | 42 | 63 | BELUM CUKUP | 7 | 185/80 | +0.07 | 7 | -4.97 | -0.77 | 4.2 | -0.60 | – | – |
| 82 | `N09X36` Undur EMA10 + penapis EMA50 →  | **48.3** | 39 | 45 | 39 | 70 | BELUM CUKUP | 7 | 159/43 | -0.88 | 7 | -1.18 | -0.30 | 2.0 | -0.67 | – | – |
| 83 | `M131` Ross Hook (Joe Ross) | **48.2** | 45 | 50 | 55 | 27 | BELUM CUKUP | 20 | 260/112 | -0.84 | 20 | -0.26 | -0.04 | 3.2 | +0.18 | – | 0.40 |
| 84 | `N28X16` ADX>25 + DI+ > DI- → keluar bi | **48.2** | 39 | 47 | 38 | 70 | BELUM CUKUP | 7 | 279/145 | -0.59 | 7 | -1.96 | -0.31 | 3.8 | -1.20 | – | – |
| 85 | `N45X36` Undur EMA21 cerun positif → ke | **48.2** | 37 | 53 | 38 | 55 | BELUM CUKUP | 7 | 112/34 | -1.09 | 7 | -0.12 | -0.06 | 1.3 | -0.71 | – | – |
| 86 | `N22X36` BB pecah atas + RSI → keluar s | **48.2** | 29 | 54 | 46 | 70 | BELUM CUKUP | 7 | 114/34 | -1.66 | 7 | +0.80 | +0.21 | 2.0 | +0.17 | – | – |
| 87 | `N68X36` Bullish engulfing + EMA21 → ke | **48.2** | 34 | 52 | 40 | 64 | BELUM CUKUP | 7 | 65/16 | -1.28 | 7 | +0.08 | +0.02 | 1.8 | -0.22 | – | – |
| 88 | `M139` 均线首次粘合向上发散 (MA berhimpun kali  | **48.1** | 38 | 53 | 48 | 56 | BELUM CUKUP | 20 | 84/17 | -1.45 | 20 | +2.43 | +0.44 | 2.4 | +0.01 | – | 0.04 |
| 89 | `N08X16` tutup>EMA20 tidak terlalu jauh | **48.1** | 35 | 51 | 38 | 70 | BELUM CUKUP | 7 | 358/196 | -1.02 | 7 | -0.21 | -0.07 | 2.1 | -1.22 | – | – |
| 90 | `N35X36` Pecah 52 minggu tinggi → kelua | **48.1** | 32 | 71 | 26 | 70 | BELUM CUKUP | 6 | 46/1 | -1.47 | 7 | +1.53 | +0.85 | 0.9 | -0.99 | – | – |
| 91 | `M96` Momo India: Ranking Sharpe 3/6 | **48.1** | 12 | 9 | 9 | 15 | BELUM CUKUP | 1 | 6/6 | -13.40 | 9 | -8.03 | -1.00 | 6.2 | -5.74 | – | -15.35 |
| 92 | `N55X13` BB + RSI + ADX>20 → keluar bil | **48.0** | 52 | 51 | 25 | 44 | BELUM CUKUP | 7 | 58/0 | +0.11 | 7 | -2.13 | -0.46 | 3.4 | -0.82 | – | – |
| 93 | `M08` SMA20 + SMA200 | **47.7** | 43 | 40 | 51 | 55 | BELUM CUKUP | 18 | 197/95 | -0.72 | 20 | -2.46 | -0.46 | 3.7 | -0.24 | – | -0.65 |
| 94 | `N74X16` MACD atas garis isyarat (keada | **47.7** | 36 | 42 | 39 | 70 | BELUM CUKUP | 7 | 383/222 | -0.75 | 7 | -3.13 | -0.43 | 4.8 | -1.08 | – | – |
| 95 | `N41X36` CMF20>0 + tutup>EMA20 → keluar | **47.6** | 34 | 42 | 40 | 70 | BELUM CUKUP | 7 | 207/113 | -1.16 | 7 | -2.04 | -0.41 | 2.6 | -0.90 | – | – |
| 96 | `N65X14` Gap 4% + volum + hampir 52w →  | **47.6** | 40 | 47 | 26 | 68 | BELUM CUKUP | 6 | 30/1 | -0.70 | 7 | -1.80 | -0.43 | 2.5 | -0.94 | – | – |
| 97 | `N65X36` Gap 4% + volum + hampir 52w →  | **47.6** | 41 | 46 | 26 | 62 | BELUM CUKUP | 6 | 30/1 | -0.63 | 7 | -2.11 | -0.51 | 2.5 | -0.91 | – | – |
| 98 | `N50X17` Mampat + pecah volum 1.5x → ke | **47.6** | 27 | 48 | 30 | 70 | BELUM CUKUP | 4 | 13/2 | -1.90 | 7 | -1.58 | -0.17 | 4.4 | -0.53 | – | – |
| 99 | `M78` Alvarez Pecahan Mingguan DTAYS | **47.4** | 15 | 23 | 40 | 15 | BELUM CUKUP | 2 | 73/39 | -2.22 | 19 | -7.78 | -0.75 | 6.7 | -0.08 | – | -0.27 |
| 100 | `N76X16` Tutup > MA50 (penapis trend tu | **47.3** | 30 | 50 | 36 | 70 | BELUM CUKUP | 7 | 236/119 | -1.30 | 7 | -0.28 | -0.08 | 1.8 | -1.47 | – | – |
| 101 | `N50X14` Mampat + pecah volum 1.5x → ke | **47.3** | 24 | 44 | 29 | 70 | BELUM CUKUP | 4 | 14/3 | -2.39 | 7 | -3.10 | -0.34 | 4.4 | -0.69 | – | – |
| 102 | `M148` Natural Number Method | **47.2** | 33 | 61 | 43 | 55 | BELUM CUKUP | 20 | 221/142 | -1.88 | 20 | +2.51 | +0.50 | 2.4 | -1.28 | – | -4.17 |
| 103 | `M04` BB Squeeze Breakout | **47.2** | 36 | 45 | 54 | 54 | BELUM CUKUP | 19 | 153/53 | -1.52 | 20 | +1.99 | +0.25 | 4.0 | +0.29 | – | 0.48 |
| 104 | `N119X13` 3 tutup turun berturut → kelua | **47.2** | 36 | 42 | 32 | 70 | BELUM CUKUP | 7 | 186/37 | -0.76 | 7 | -3.47 | -0.42 | 6.4 | -1.45 | – | – |
| 105 | `N28X14` ADX>25 + DI+ > DI- → keluar bi | **47.2** | 34 | 47 | 31 | 70 | BELUM CUKUP | 7 | 166/10 | -1.26 | 7 | -0.31 | -0.05 | 3.2 | -1.08 | – | – |
| 106 | `N76X36` Tutup > MA50 (penapis trend tu | **47.1** | 40 | 32 | 40 | 55 | BELUM CUKUP | 7 | 164/50 | -0.56 | 7 | -4.51 | -0.82 | 3.9 | -0.69 | – | – |
| 107 | `N56X17` RSI>50 + ADX>20 → keluar bila  | **47.0** | 30 | 51 | 31 | 70 | BELUM CUKUP | 7 | 124/18 | -1.60 | 7 | +0.28 | +0.06 | 2.5 | -1.35 | – | – |
| 108 | `N37X16` Gap and go → keluar bila super | **47.0** | 33 | 43 | 33 | 70 | BELUM CUKUP | 7 | 82/16 | -1.20 | 7 | -0.88 | -0.24 | 2.0 | -1.02 | – | – |
| 109 | `N80X36` Tinggi sepanjang masa → keluar | **47.0** | 34 | 43 | 31 | 46 | BELUM CUKUP | 6 | 37/1 | -1.06 | 7 | -1.55 | -0.45 | 1.8 | -0.33 | – | – |
| 110 | `M41` FW Penyatuan Mingguan | **46.8** | 28 | 27 | 40 | 28 | BELUM CUKUP | 4 | 63/9 | -1.20 | 19 | -5.09 | -0.62 | 4.7 | +0.24 | – | 0.45 |
| 111 | `M138` 直升机空中加油 (Helikopter isi minyak | **46.8** | 25 | 43 | 18 | 15 | BELUM CUKUP | 3 | 3/0 | -2.96 | 13 | -0.83 | -0.82 | 0.4 | -1.39 | – | -2.46 |
| 112 | `N56X16` RSI>50 + ADX>20 → keluar bila  | **46.7** | 30 | 41 | 35 | 70 | BELUM CUKUP | 7 | 181/63 | -1.09 | 7 | -2.49 | -0.49 | 3.4 | -1.30 | – | – |
| 113 | `N41X16` CMF20>0 + tutup>EMA20 → keluar | **46.6** | 26 | 48 | 35 | 70 | BELUM CUKUP | 7 | 234/119 | -1.61 | 7 | -0.53 | -0.21 | 1.5 | -1.50 | – | – |
| 114 | `N66X36` 52w tinggi + pengesahan 1% → k | **46.5** | 32 | 36 | 28 | 70 | BELUM CUKUP | 6 | 37/1 | -1.19 | 6 | -3.02 | -0.73 | 2.8 | -0.76 | – | – |
| 115 | `M18` EMA9/21 Pullback | **46.4** | 52 | 38 | 54 | 17 | BELUM CUKUP | 20 | 369/246 | -0.18 | 20 | -4.92 | -0.82 | 4.1 | -0.01 | – | -0.04 |
| 116 | `M64` O'Neil Tiga Minggu Ketat | **46.4** | 22 | 23 | 27 | 15 | BELUM CUKUP | 3 | 3/2 | -11.23 | 20 | -3.34 | -0.82 | 2.4 | -0.97 | – | -11.82 |
| 117 | `M21` Marius 3 Persediaan (Pecahan+J | **46.2** | 20 | 46 | 37 | 26 | BELUM CUKUP | 5 | 5/3 | -2.59 | 12 | -1.26 | -0.57 | 1.2 | +0.18 | – | 0.36 |
| 118 | `M38` Darvas Kotak | **46.2** | 16 | 36 | 34 | 42 | BELUM CUKUP | 4 | 23/1 | -2.46 | 19 | -3.00 | -0.30 | 4.8 | +0.18 | – | 0.92 |
| 119 | `N24X17` Supertrend(10,3) + ADX>20 → ke | **46.1** | 24 | 51 | 28 | 70 | BELUM CUKUP | 7 | 115/12 | -1.82 | 7 | -0.16 | -0.04 | 1.8 | -1.50 | – | – |
| 120 | `N39X36` NR7 kemudian pecah → keluar se | **46.1** | 12 | 26 | 18 | 70 | BELUM CUKUP | 3 | 24/5 | -4.11 | 6 | -2.83 | -0.78 | 2.2 | -2.08 | – | – |
| 121 | `M34` Carter TTM Squeeze | **46.0** | 45 | 41 | 51 | 22 | BELUM CUKUP | 19 | 103/46 | -0.82 | 20 | +0.63 | +0.09 | 3.8 | -0.04 | – | -0.12 |
| 122 | `M150` Trend Bar Failure (Brooks) | **46.0** | 50 | 42 | 49 | 15 | BELUM CUKUP | 19 | 102/40 | -0.16 | 20 | -4.33 | -0.77 | 2.8 | -0.19 | – | -0.59 |
| 123 | `N113X16` 80-20 bar (sisi beli) → keluar | **46.0** | 44 | 23 | 41 | 30 | BELUM CUKUP | 7 | 280/184 | +0.28 | 7 | -8.15 | -1.00 | 6.7 | -0.78 | – | – |
| 124 | `N25X16` Supertrend + EMA + ADX>23 → ke | **45.9** | 25 | 45 | 28 | 70 | BELUM CUKUP | 7 | 109/3 | -1.61 | 7 | -1.44 | -0.30 | 2.7 | -0.99 | – | – |
| 125 | `N07X16` Tiga MA tersusun → keluar bila | **45.9** | 26 | 50 | 33 | 30 | BELUM CUKUP | 7 | 127/14 | -1.57 | 7 | -0.59 | -0.15 | 2.1 | -0.94 | – | – |
| 126 | `M157` Consolidation Pivot Breakout ( | **45.9** | 20 | 36 | 28 | 15 | BELUM CUKUP | 4 | 4/3 | -4.96 | 17 | -1.96 | -0.67 | 1.5 | -0.86 | – | -2.47 |
| 127 | `N36X14` Pocket pivot → keluar bila rsi | **45.8** | 28 | 34 | 34 | 70 | BELUM CUKUP | 7 | 140/19 | -1.62 | 7 | -1.95 | -0.29 | 3.7 | -1.05 | – | – |
| 128 | `N25X17` Supertrend + EMA + ADX>23 → ke | **45.8** | 23 | 48 | 29 | 70 | BELUM CUKUP | 7 | 104/4 | -1.79 | 7 | -0.84 | -0.18 | 2.6 | -1.03 | – | – |
| 129 | `N68X16` Bullish engulfing + EMA21 → ke | **45.7** | 22 | 48 | 36 | 39 | BELUM CUKUP | 7 | 64/11 | -1.75 | 7 | -0.23 | -0.05 | 2.3 | -0.52 | – | – |
| 130 | `M134` First Kiss After Daylight (Lan | **45.6** | 37 | 42 | 49 | 26 | BELUM CUKUP | 16 | 56/16 | -1.17 | 20 | -2.00 | -0.29 | 3.7 | +0.29 | – | 0.37 |
| 131 | `N33X36` Donchian20 + penapis MA200 → k | **45.6** | 24 | 42 | 32 | 58 | BELUM CUKUP | 7 | 91/17 | -1.60 | 7 | -2.21 | -0.61 | 2.0 | -1.17 | – | – |
| 132 | `N113X36` 80-20 bar (sisi beli) → keluar | **45.6** | 37 | 26 | 40 | 30 | BELUM CUKUP | 7 | 265/178 | -0.25 | 7 | -7.04 | -1.00 | 6.1 | -0.94 | – | – |
| 133 | `N56X36` RSI>50 + ADX>20 → keluar selep | **45.5** | 30 | 29 | 36 | 54 | BELUM CUKUP | 7 | 167/63 | -1.06 | 7 | -5.52 | -0.75 | 5.5 | -1.21 | – | – |
| 134 | `N28X17` ADX>25 + DI+ > DI- → keluar bi | **45.5** | 27 | 42 | 23 | 70 | BELUM CUKUP | 7 | 108/0 | -1.32 | 7 | -1.85 | -0.26 | 3.7 | -1.09 | – | – |
| 135 | `N119X15` 3 tutup turun berturut → ekori | **45.5** | 27 | 40 | 19 | 70 | BELUM CUKUP | 6 | 47/0 | -1.18 | 7 | -3.51 | -0.52 | 4.8 | -1.50 | – | – |
| 136 | `N07X36` Tiga MA tersusun → keluar sele | **45.4** | 26 | 43 | 32 | 30 | BELUM CUKUP | 7 | 129/8 | -1.55 | 7 | -1.51 | -0.38 | 2.5 | -0.95 | – | – |
| 137 | `N16X15` RSI2<10 tanpa penapis → ekori  | **45.4** | 38 | 32 | 26 | 30 | BELUM CUKUP | 7 | 111/0 | -0.19 | 7 | -6.45 | -0.55 | 8.4 | -0.72 | – | – |
| 138 | `M102` Stockbee SLTB | **45.3** | 43 | 44 | 50 | 15 | BELUM CUKUP | 20 | 370/271 | -1.19 | 20 | -1.09 | -0.10 | 5.5 | -0.39 | – | -1.06 |
| 139 | `M03` BB Break + Divergence RSI | **45.2** | 40 | 43 | 54 | 17 | BELUM CUKUP | 20 | 410/319 | -0.46 | 20 | -2.59 | -0.41 | 2.9 | +0.02 | – | 0.06 |
| 140 | `M106` DMI Wilder | **45.2** | 43 | 40 | 52 | 15 | BELUM CUKUP | 18 | 127/61 | -0.69 | 20 | -2.21 | -0.49 | 2.6 | +0.00 | – | 0.00 |
| 141 | `N57X36` ADX bangkit daripada <20 → kel | **45.2** | 22 | 53 | 25 | 46 | BELUM CUKUP | 7 | 67/7 | -2.97 | 7 | +0.61 | +0.18 | 2.0 | -1.70 | – | – |
| 142 | `M68` Kell Base n' Break | **45.1** | 28 | 49 | 45 | 36 | BELUM CUKUP | 14 | 43/12 | -2.81 | 20 | +0.46 | +0.10 | 1.9 | -0.02 | – | -0.15 |
| 143 | `N33X16` Donchian20 + penapis MA200 → k | **45.1** | 20 | 46 | 27 | 70 | BELUM CUKUP | 7 | 93/7 | -1.94 | 7 | -0.97 | -0.28 | 1.8 | -1.41 | – | – |
| 144 | `N22X14` BB pecah atas + RSI → keluar b | **45.1** | 20 | 39 | 33 | 70 | BELUM CUKUP | 7 | 119/11 | -2.38 | 7 | -1.59 | -0.35 | 2.5 | -0.93 | – | – |
| 145 | `N24X16` Supertrend(10,3) + ADX>20 → ke | **45.1** | 23 | 44 | 23 | 67 | BELUM CUKUP | 7 | 111/2 | -1.76 | 7 | -1.24 | -0.37 | 1.9 | -1.52 | – | – |
| 146 | `M116` 2/20 EMA Breakout (Landry) | **45.0** | 44 | 38 | 54 | 15 | BELUM CUKUP | 20 | 565/377 | -0.47 | 20 | -1.94 | -0.16 | 7.3 | -0.00 | – | -0.01 |
| 147 | `N57X16` ADX bangkit daripada <20 → kel | **45.0** | 21 | 52 | 23 | 46 | BELUM CUKUP | 7 | 65/4 | -3.05 | 7 | +0.61 | +0.18 | 2.0 | -1.73 | – | – |
| 148 | `N47X16` NR7 + EMA9>EMA21 → keluar bila | **45.0** | 22 | 41 | 27 | 53 | BELUM CUKUP | 7 | 149/22 | -1.47 | 7 | -3.10 | -0.71 | 2.6 | -1.87 | – | – |
| 149 | `M136` Short/Intermediate-term Low (L | **44.9** | 40 | 44 | 52 | 15 | BELUM CUKUP | 20 | 776/269 | -1.00 | 20 | -0.91 | -0.19 | 2.6 | -0.17 | – | -0.08 |
| 150 | `M31` Band Walk (BB 20/2) | **44.9** | 44 | 30 | 56 | 28 | BELUM CUKUP | 20 | 397/94 | -0.53 | 20 | -1.82 | -0.16 | 7.1 | +0.25 | – | 0.42 |
| 151 | `M54` IBD Power Trend | **44.9** | 38 | 47 | 50 | 15 | BELUM CUKUP | 19 | 208/105 | -1.50 | 20 | +1.99 | +0.19 | 5.4 | -0.38 | – | -0.84 |
| 152 | `N37X14` Gap and go → keluar bila rsi14 | **44.9** | 24 | 33 | 30 | 62 | BELUM CUKUP | 7 | 81/7 | -1.50 | 7 | -2.45 | -0.61 | 2.4 | -1.13 | – | – |
| 153 | `N38X36` VCP pecah → keluar selepas DUA | **44.9** | 27 | 39 | 23 | 46 | BELUM CUKUP | 7 | 28/7 | -1.56 | 7 | -2.29 | -0.71 | 2.0 | -1.88 | – | – |
| 154 | `N22X16` BB pecah atas + RSI → keluar b | **44.8** | 20 | 37 | 42 | 30 | BELUM CUKUP | 7 | 116/21 | -1.87 | 7 | -2.12 | -0.59 | 2.4 | -0.12 | – | – |
| 155 | `N53X16` Supertrend + ADX>25 → keluar b | **44.8** | 23 | 36 | 35 | 30 | BELUM CUKUP | 7 | 102/5 | -1.56 | 7 | -4.03 | -0.65 | 3.9 | -0.39 | – | – |
| 156 | `M115` Bow Tie (Landry) | **44.7** | 26 | 38 | 48 | 38 | BELUM CUKUP | 11 | 36/23 | -1.96 | 20 | -4.16 | -0.53 | 4.0 | +0.13 | – | 0.76 |
| 157 | `M49` Ichimoku (Tutup Atas Awan + Te | **44.6** | 38 | 48 | 48 | 15 | BELUM CUKUP | 20 | 297/159 | -1.53 | 20 | +0.24 | +0.04 | 3.4 | -0.73 | – | -0.98 |
| 158 | `M107` Golden Cross SMA50/200 | **44.6** | 38 | 47 | 44 | 15 | BELUM CUKUP | 17 | 37/7 | -1.23 | 20 | -0.49 | -0.14 | 1.8 | -0.10 | – | -0.16 |
| 159 | `M32` Momentum Burst | **44.6** | 43 | 25 | 50 | 26 | BELUM CUKUP | 13 | 56/34 | -0.74 | 20 | -5.63 | -0.51 | 7.1 | +0.14 | – | 0.38 |
| 160 | `N33X14` Donchian20 + penapis MA200 → k | **44.6** | 18 | 42 | 27 | 60 | BELUM CUKUP | 7 | 102/5 | -2.17 | 7 | -1.93 | -0.47 | 2.3 | -1.32 | – | – |
| 161 | `M87` IBD Tapak Menaik | **44.5** | 26 | 32 | 38 | 15 | BELUM CUKUP | 7 | 10/6 | -3.59 | 20 | -3.58 | -0.60 | 3.6 | -0.36 | – | -1.24 |
| 162 | `M20` EMA10/15 Crossover + Sudut | **44.4** | 41 | 42 | 48 | 15 | BELUM CUKUP | 20 | 459/356 | -0.94 | 20 | -2.52 | -0.43 | 2.9 | -0.73 | – | -4.82 |
| 163 | `M26` Garis Trend Undur 3 Sentuhan + | **44.4** | 39 | 41 | 47 | 15 | BELUM CUKUP | 17 | 74/45 | -0.57 | 20 | -3.62 | -0.45 | 3.7 | -0.41 | – | -0.62 |
| 164 | `M144` Screw Bar | **44.4** | 19 | 35 | 33 | 15 | BELUM CUKUP | 6 | 9/7 | -2.04 | 18 | -1.79 | -0.68 | 1.0 | -0.66 | – | -1.54 |
| 165 | `M12` Parabolic SAR | **44.3** | 32 | 45 | 51 | 23 | BELUM CUKUP | 20 | 369/187 | -1.65 | 20 | -0.35 | -0.06 | 2.9 | -0.35 | – | -0.81 |
| 166 | `N53X17` Supertrend + ADX>25 → keluar b | **44.2** | 21 | 36 | 29 | 30 | BELUM CUKUP | 7 | 95/0 | -1.70 | 7 | -3.47 | -0.61 | 3.6 | -0.38 | – | – |
| 167 | `M120` Reversal New Highs | **44.1** | 35 | 39 | 44 | 15 | BELUM CUKUP | 13 | 19/12 | -1.30 | 20 | -1.77 | -0.27 | 3.2 | -0.14 | – | -0.82 |
| 168 | `N51X36` BB squeeze + Supertrend → kelu | **44.1** | 13 | 32 | 21 | 30 | BELUM CUKUP | 5 | 8/2 | -2.90 | 7 | -2.20 | -0.81 | 2.0 | -1.66 | – | – |
| 169 | `N54X36` Supertrend + RSI>50 → keluar s | **44.0** | 26 | 21 | 37 | 30 | BELUM CUKUP | 7 | 154/58 | -1.08 | 7 | -8.22 | -1.00 | 6.5 | -1.09 | – | – |
| 170 | `N51X16` BB squeeze + Supertrend → kelu | **44.0** | 12 | 32 | 19 | 30 | BELUM CUKUP | 5 | 8/1 | -3.41 | 7 | -2.59 | -0.83 | 2.1 | -1.69 | – | – |
| 171 | `M06` Minervini VCP Breakout | **43.8** | 31 | 53 | 47 | 15 | BELUM CUKUP | 19 | 80/37 | -1.68 | 20 | +0.01 | +0.00 | 2.9 | -0.39 | – | -1.00 |
| 172 | `N27X16` Ichimoku atas awan → keluar bi | **43.8** | 19 | 31 | 30 | 35 | BELUM CUKUP | 7 | 138/56 | -1.72 | 7 | -3.16 | -1.00 | 2.0 | -1.90 | – | – |
| 173 | `M143` 장대양봉 이후 눌림목 / 5일선 매매 (Undur ke | **43.7** | 23 | 49 | 28 | 52 | BELUM CUKUP | 12 | 24/1 | -1.63 | 19 | -0.99 | -0.33 | 1.6 | -0.92 | – | -9.34 |
| 174 | `M155` Market Cycle Strategy | **43.6** | 43 | 33 | 51 | 15 | BELUM CUKUP | 20 | 705/236 | -0.63 | 20 | -2.78 | -0.47 | 3.8 | -0.37 | – | -0.52 |
| 175 | `M36` Turtle 55/20 | **43.6** | 36 | 38 | 54 | 15 | BELUM CUKUP | 20 | 340/155 | -1.26 | 20 | -1.52 | -0.13 | 6.5 | -0.04 | – | -0.10 |
| 176 | `M149` 3-Step Pullback | **43.6** | 34 | 35 | 53 | 21 | BELUM CUKUP | 18 | 208/56 | -1.23 | 20 | -2.91 | -0.27 | 5.6 | +0.22 | – | 0.19 |
| 177 | `N06X36` Golden cross MA50/MA200 → kelu | **43.6** | 11 | 36 | 24 | 47 | BELUM CUKUP | 6 | 17/2 | -2.47 | 7 | -3.42 | -0.84 | 2.5 | -1.38 | – | – |
| 178 | `N31X36` Turtle sistem 2 → keluar selep | **43.5** | 17 | 33 | 23 | 46 | BELUM CUKUP | 7 | 99/3 | -2.57 | 7 | -2.50 | -0.69 | 2.3 | -1.62 | – | – |
| 179 | `N29X16` PSAR naik + tutup>MA50 → kelua | **43.5** | 13 | 30 | 32 | 64 | BELUM CUKUP | 7 | 169/61 | -2.41 | 7 | -4.77 | -0.65 | 5.2 | -1.69 | – | – |
| 180 | `M128` Inventory Retracement Bar (IRB | **43.4** | 40 | 33 | 53 | 15 | BELUM CUKUP | 20 | 152/79 | -0.71 | 20 | -4.12 | -0.37 | 6.5 | -0.04 | – | -0.19 |
| 181 | `M19` Sneaky Pivot (proksi harian) | **43.4** | 28 | 44 | 51 | 24 | BELUM CUKUP | 19 | 408/237 | -1.65 | 20 | +0.14 | +0.02 | 3.4 | -0.31 | – | -5.17 |
| 182 | `M14` Walking with the Whales | **43.3** | 43 | 32 | 49 | 15 | BELUM CUKUP | 20 | 909/614 | -0.59 | 20 | -7.52 | -0.71 | 6.2 | -0.53 | – | -0.87 |
| 183 | `M73` ADX(5) > 40 + Julat Terkecil 6 | **43.2** | 39 | 35 | 50 | 15 | BELUM CUKUP | 20 | 984/773 | -0.10 | 20 | -6.66 | -0.83 | 4.8 | -0.50 | – | -3.30 |
| 184 | `M99` Three Line Break | **43.1** | 30 | 44 | 51 | 15 | BELUM CUKUP | 20 | 156/88 | -2.04 | 20 | +1.11 | +0.18 | 3.4 | -0.26 | – | -1.04 |
| 185 | `M44` Tapak Rata IBD | **43.1** | 25 | 38 | 21 | 15 | BELUM CUKUP | 8 | 9/5 | -4.30 | 20 | -3.76 | -0.80 | 2.8 | -2.32 | – | -33.28 |
| 186 | `N27X36` Ichimoku atas awan → keluar se | **43.1** | 16 | 32 | 25 | 31 | BELUM CUKUP | 7 | 92/9 | -2.26 | 7 | -3.15 | -0.72 | 3.0 | -1.72 | – | – |
| 187 | `M127` Slingshot Bullish | **43.0** | 29 | 46 | 43 | 15 | BELUM CUKUP | 17 | 106/77 | -1.83 | 20 | -2.66 | -0.39 | 3.0 | -1.06 | – | -1.40 |
| 188 | `N54X16` Supertrend + RSI>50 → keluar b | **42.9** | 12 | 30 | 25 | 70 | BELUM CUKUP | 7 | 117/4 | -2.08 | 7 | -4.89 | -0.61 | 4.8 | -1.53 | – | – |
| 189 | `M121` High 2 bull flag (Brooks) | **42.8** | 9 | 16 | 24 | 15 | BELUM CUKUP | 5 | 7/4 | -9.34 | 16 | -6.49 | -0.78 | 4.7 | -1.50 | – | -22.04 |
| 190 | `M152` Spike & Ledge | **42.6** | 26 | 42 | 43 | 27 | BELUM CUKUP | 17 | 46/8 | -1.75 | 20 | -0.41 | -0.08 | 2.7 | -0.23 | – | -0.71 |
| 191 | `N47X36` NR7 + EMA9>EMA21 → keluar sele | **42.6** | 8 | 31 | 22 | 30 | BELUM CUKUP | 6 | 138/15 | -2.07 | 7 | -5.98 | -0.86 | 5.0 | -2.20 | – | – |
| 192 | `M28` VWAP Separator + Kiss Pivot | **42.5** | 35 | 34 | 46 | 15 | BELUM CUKUP | 18 | 113/90 | -0.98 | 20 | -5.70 | -0.67 | 5.5 | -0.85 | – | -8.11 |
| 193 | `M141` First Thrust (Landry) | **42.5** | 18 | 37 | 33 | 15 | BELUM CUKUP | 9 | 27/9 | -2.01 | 20 | -3.46 | -0.67 | 2.3 | -1.11 | – | -2.04 |
| 194 | `M156` Single Penetration (DiNapoli) | **42.3** | 34 | 34 | 48 | 17 | BELUM CUKUP | 20 | 235/147 | -1.10 | 20 | -3.20 | -0.25 | 6.2 | -0.74 | – | -2.61 |
| 195 | `M50` Elder Triple Screen | **42.0** | 36 | 30 | 50 | 15 | BELUM CUKUP | 20 | 567/334 | -0.85 | 20 | -8.01 | -0.72 | 6.5 | -0.43 | – | -0.71 |
| 196 | `N29X36` PSAR naik + tutup>MA50 → kelua | **42.0** | 11 | 21 | 32 | 30 | BELUM CUKUP | 7 | 138/45 | -1.88 | 7 | -9.00 | -0.93 | 7.8 | -1.54 | – | – |
| 197 | `M130` 多方炮 (dua lilin hijau mengapit  | **41.9** | 12 | 21 | 34 | 15 | BELUM CUKUP | 7 | 10/3 | -4.26 | 18 | -4.02 | -0.65 | 3.0 | -0.34 | – | -0.32 |
| 198 | `M125` 2-Bar Breakout | **41.6** | 31 | 33 | 49 | 15 | BELUM CUKUP | 20 | 1053/419 | -1.40 | 20 | -3.09 | -0.47 | 3.2 | -0.56 | – | -0.26 |
| 199 | `M67` Rayner Teo: Ujian Ketiga pada  | **41.3** | 26 | 32 | 39 | 15 | BELUM CUKUP | 14 | 29/18 | -3.01 | 20 | -5.06 | -0.46 | 6.2 | -0.90 | – | -4.50 |
| 200 | `M55` Guppy GMMA | **41.1** | 30 | 31 | 51 | 15 | BELUM CUKUP | 20 | 215/123 | -1.45 | 20 | -5.72 | -0.65 | 4.5 | -0.37 | – | -1.09 |
| 201 | `M140` 猎豹出击 (Serangan Cheetah) | **41.0** | 18 | 31 | 35 | 15 | BELUM CUKUP | 11 | 42/12 | -1.68 | 20 | -5.18 | -0.78 | 3.1 | -1.16 | – | -1.39 |
| 202 | `M119` 180 Bullish (Cooper) | **40.9** | 28 | 33 | 47 | 15 | BELUM CUKUP | 19 | 151/66 | -1.44 | 20 | -5.44 | -0.50 | 5.0 | -0.65 | – | -2.06 |
| 203 | `M66` IBD Undur Pertama ke Purata 50 | **40.7** | 30 | 29 | 50 | 15 | BELUM CUKUP | 20 | 243/134 | -1.31 | 20 | -5.95 | -0.51 | 6.4 | -0.44 | – | -1.16 |
| 204 | `M135` 3rd Watch | **40.4** | 10 | 28 | 31 | 15 | BELUM CUKUP | 9 | 15/3 | -4.94 | 20 | -6.27 | -0.79 | 3.8 | -1.01 | – | -5.37 |
| 205 | `M11` NR7 Breakout + Volume | **40.3** | 28 | 28 | 44 | 15 | BELUM CUKUP | 18 | 117/78 | -1.00 | 20 | -7.83 | -0.65 | 6.7 | -1.07 | – | -0.96 |
| 206 | `M126` Hidden Smash Day (beli, Larry  | **40.2** | 12 | 31 | 33 | 15 | BELUM CUKUP | 10 | 18/11 | -4.34 | 19 | -5.13 | -0.71 | 4.1 | -1.05 | – | -1.80 |
| 207 | `M147` Improved Three-Bar Pullback | **39.8** | 17 | 33 | 34 | 34 | BELUM CUKUP | 15 | 97/33 | -3.85 | 20 | -3.48 | -0.41 | 4.2 | -1.75 | – | -1.28 |
| 208 | `M29` EMA3 + RSI75 + Stokastik | **39.7** | 20 | 29 | 39 | 15 | BELUM CUKUP | 15 | 36/28 | -2.66 | 20 | -9.12 | -0.73 | 7.1 | -1.05 | – | -6.43 |
| 209 | `M82` Arthur Hill Rotasi Sasaran 10% | **39.2** | 32 | 19 | 51 | 15 | BELUM CUKUP | 20 | 574/214 | -0.93 | 20 | -6.40 | -0.40 | 8.7 | -0.36 | – | -1.35 |
| 210 | `M57` Landry Trend Knockout (TKO) | **39.2** | 23 | 32 | 41 | 15 | BELUM CUKUP | 20 | 165/108 | -2.13 | 20 | -4.88 | -0.58 | 4.0 | -1.45 | – | -4.17 |
| 211 | `M161` EMA 10/21 + Supertrend (10,3) | **38.9** | 32 | 18 | 51 | 15 | BELUM CUKUP | 20 | 472/216 | -0.73 | 20 | -9.98 | -0.72 | 9.0 | -0.30 | – | -0.65 |
| 212 | `M95` Nisbah Kebaharuan High 52 Ming | **38.9** | 19 | 32 | 48 | 15 | BELUM CUKUP | 19 | 124/63 | -1.92 | 20 | -6.01 | -0.70 | 4.6 | -0.54 | – | -1.33 |
| 213 | `M59` Anjakan Julat RSI | **38.5** | 14 | 25 | 43 | 15 | BELUM CUKUP | 14 | 36/18 | -4.88 | 20 | -3.66 | -0.46 | 4.0 | -0.48 | – | -1.98 |
| 214 | `M79` Radge: 20% Flipper | **37.3** | 16 | 27 | 46 | 15 | BELUM CUKUP | 20 | 381/85 | -1.82 | 20 | -6.32 | -0.64 | 5.1 | -0.86 | – | -1.45 |
| 215 | `M123` CCI Correction (Lambert, Chart | **37.0** | 18 | 28 | 35 | 15 | BELUM CUKUP | 20 | 183/155 | -1.53 | 20 | -10.15 | -0.94 | 6.3 | -2.17 | – | -4.44 |
| 216 | `M101` Bulkowski: Tiga lembah menaik | **37.0** | 13 | 20 | 45 | 15 | BELUM CUKUP | 16 | 45/21 | -3.61 | 20 | -8.19 | -0.64 | 6.7 | -0.30 | – | -0.93 |
| 217 | `M76` Undercut & Rally pada Low Pent | **36.9** | 15 | 26 | 42 | 15 | BELUM CUKUP | 19 | 75/47 | -1.57 | 20 | -8.28 | -0.76 | 6.3 | -1.12 | – | -4.62 |
| 218 | `M154` HOLP (High of Low Period) | **35.3** | 8 | 20 | 42 | 15 | BELUM CUKUP | 16 | 87/32 | -2.54 | 20 | -10.22 | -0.79 | 7.0 | -0.81 | – | -3.99 |
| 219 | `M122` Moving Momentum (ChartSchool) | **35.0** | 14 | 20 | 37 | 15 | BELUM CUKUP | 20 | 106/58 | -3.07 | 20 | -9.56 | -1.00 | 5.2 | -1.70 | – | -5.04 |
| 220 | `M47` Holy Grail Raschke | **35.0** | 6 | 19 | 28 | 15 | BELUM CUKUP | 14 | 31/22 | -3.05 | 20 | -9.23 | -0.89 | 6.0 | -2.21 | – | -22.21 |
| 221 | `M81` Bensdorp Long Trend High Momen | **34.2** | 3 | 12 | 44 | 15 | BELUM CUKUP | 13 | 431/144 | -3.66 | 20 | -16.22 | -0.70 | 13.6 | -1.02 | – | -3.41 |
| 222 | `M09` Volumatic VIDYA Pivot Retest | **33.7** | 2 | 13 | 31 | 15 | BELUM CUKUP | 13 | 32/17 | -4.55 | 20 | -11.92 | -1.00 | 7.6 | -1.76 | – | -11.67 |
| 223 | `M90` Pring KST | **31.0** | 3 | 15 | 43 | 15 | BELUM CUKUP | 19 | 83/42 | -3.27 | 20 | -13.06 | -0.71 | 10.8 | -0.93 | – | -4.35 |

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

