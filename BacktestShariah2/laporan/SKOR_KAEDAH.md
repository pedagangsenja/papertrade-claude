# Skor Kaedah 0–100 (pangkat maklumat, BUKAN keputusan)

> **Status keputusan (kad skor, harga 2026-11-13):** TERBUKTI 0 · CALON 0 · BELUM CUKUP 226 · GAGAL 0 · NEGATIF 0. Rejim QQQ OFF sejak 2026-10-16. Hanya **TERBUKTI** layak untuk wang sebenar (`laporan/KAD_SKOR.md`); nombor dalam laporan ini BUKAN keputusan dan tidak boleh dibaca sebagai pangkat untuk wang sebenar.

Dijana 2026-11-14 oleh `standard/skor_kaedah.py` (Actions `analisis.yml`, selepas kad skor). Harga pada tutup 2026-11-13; 226 kaedah; 21 hari beli langsung (rejim ON 1, OFF 20). Pradaftar 2026-11-09: `standard/SPEC_SKOR_KAEDAH.md` (berat dan sauh dikunci `ujian/test_skor_kaedah.py::TestKunci`). Rekod analisis sahaja: tiada order, tiada wang sebenar.

## Cara membaca

- **Skor** = min geometri berberat empat tiang (Untung 35 · Tahan 30 · Bukti 25 · Konsisten 10), dikecut ke 50 mengikut data: berat data = hari beli ÷ (hari beli + 20). Kaedah dengan 2 hari beli tidak boleh menjauhi 50. 100 = unggul semua segi; 50 = neutral/tiada bukti; < 50 = lebih buruk daripada neutral.
- **Siling** ikut kad skor: NEGATIF ≤ 20, GANTUNG/BERSARA ≤ 30, GAGAL ≤ 40. Tanda ⌈ = siling terpakai.
- **Satu-satunya status yang membenarkan wang sebenar ialah TERBUKTI dalam `laporan/KAD_SKOR.md`.** Skor tinggi dengan status BELUM CUKUP bermaksud "paling menjanjikan setakat ini", bukan "selamat".
- Deflasi ujian berganda (López de Prado): sauh t Bukti C1 = maks(2.0, E[maks 226 normal]) = 2.81.
- **Semakan kebolehramalan:** skor pada 2026-11-06 lawan pulangan lorong T4 sejak itu, 223 kaedah: Spearman ρ = -0.198 (p = 0.003). Belum ada bukti skor meramal pangkat; jangan pilih kaedah dengannya.
- Metrik T4 (A2, B1, B2, D1) dikira atas lorong T4 L1 **dipotong pada sesi LANGSUNG pertama** kaedah itu (Mxx 2026-10-16, Nxx/GB 2026-11-03) dan diasas semula; sesi isian bina semula tidak dikira (pindaan 9 Nov 2026 (a)). Lajur "T4 sesi/pul" di bawah ialah potongan itu, bukan lorong penuh `T4_KAEDAH.md`.

## Semua kaedah, susun ikut Skor

| # | Kaedah | Skor | Untung | Tahan | Bukti | Konsisten | Status kad | Hari beli | Posisi/tutup | Jangkaan % | T4 sesi | T4 pul % | T4 pul/|MDD| | Ulcer | t buku | Lift | WFE |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `M146` 3-Bar Momentum Pattern | **64.2** | 88 | 84 | 64 | 85 | BELUM CUKUP | 18 | 78/31 | +1.51 | 21 | +5.75 | +0.93 | 2.4 | +1.74 | – | 2.81 |
| 2 | `M133` Bull Hook (Crabel) | **61.3** | 82 | 85 | 59 | 85 | BELUM CUKUP | 15 | 53/25 | +0.90 | 21 | +6.60 | +1.59 | 1.5 | +1.25 | – | 11.35 |
| 3 | `M151` Outside Bar Failure | **61.2** | 73 | 82 | 58 | 85 | BELUM CUKUP | 20 | 105/51 | +0.14 | 21 | +8.29 | +5.14 | 0.6 | +0.70 | – | 1.18 |
| 4 | `M118` Expansion Pivot (Cooper) | **61.2** | 74 | 81 | 57 | 85 | BELUM CUKUP | 20 | 85/22 | +0.49 | 21 | +9.42 | +3.48 | 1.1 | +1.00 | – | 2.57 |
| 5 | `M33` Supertrend + SMA10 | **60.5** | 72 | 75 | 59 | 85 | BELUM CUKUP | 21 | 221/44 | +0.58 | 21 | +9.07 | +3.39 | 1.5 | +0.90 | – | 3.44 |
| 6 | `M142` Pecahan volum dari dasar (底部放量 | **59.4** | 83 | 82 | 46 | 79 | BELUM CUKUP | 16 | 54/5 | +1.44 | 19 | +3.70 | +0.77 | 1.9 | +0.62 | – | 0.80 |
| 7 | `M25` VWAP Wave (proksi harian) | **57.9** | 66 | 71 | 59 | 74 | BELUM CUKUP | 19 | 183/96 | -0.13 | 21 | +4.44 | +0.77 | 3.1 | +0.61 | – | 3.28 |
| 8 | `M93` Bollinger Kaedah II: %b + MFI | **57.2** | 74 | 56 | 60 | 68 | BELUM CUKUP | 21 | 267/77 | +0.86 | 21 | +1.70 | +0.27 | 2.7 | +0.85 | – | 0.95 |
| 9 | `M160` Measured Move Up | **56.7** | 56 | 70 | 61 | 85 | BELUM CUKUP | 19 | 114/52 | -0.60 | 21 | +3.09 | +0.66 | 2.0 | +1.13 | – | 7.91 |
| 10 | `M74` Lulus Baharu Trend Template Mi | **56.6** | 64 | 67 | 54 | 68 | BELUM CUKUP | 21 | 96/59 | -0.27 | 21 | +2.66 | +0.57 | 2.5 | +0.27 | – | 0.42 |
| 11 | `M48` Cooper 1-2-3-4 | **56.1** | 70 | 59 | 54 | 85 | BELUM CUKUP | 17 | 58/17 | +0.11 | 21 | +8.46 | +1.55 | 2.0 | +0.77 | – | 1.79 |
| 12 | `M100` Bulkowski Segi Empat & Segi Ti | **55.9** | 63 | 68 | 54 | 85 | BELUM CUKUP | 15 | 60/41 | +0.08 | 21 | +2.65 | +0.58 | 2.1 | +0.49 | – | 2.02 |
| 13 | `M10` EMA3 + CCI + MACD | **55.7** | 58 | 67 | 54 | 76 | BELUM CUKUP | 21 | 126/55 | -0.67 | 21 | +10.16 | +1.93 | 2.1 | +0.29 | – | 0.69 |
| 14 | `M145` Yum-Yum Continuation | **55.5** | 59 | 69 | 55 | 60 | BELUM CUKUP | 21 | 308/65 | -0.34 | 21 | +4.92 | +2.26 | 1.2 | +0.24 | – | 0.17 |
| 15 | `M137` Livermore System | **55.1** | 56 | 66 | 55 | 71 | BELUM CUKUP | 21 | 175/64 | -0.70 | 21 | +4.97 | +0.84 | 2.2 | +0.32 | – | 0.54 |
| 16 | `M111` Sistem Volatiliti Wilder | **55.1** | 58 | 58 | 57 | 82 | BELUM CUKUP | 21 | 267/87 | -0.40 | 21 | +4.18 | +0.62 | 3.5 | +0.42 | – | 0.88 |
| 17 | `N75X17` RSI14 < 40 tanpa penapis → kel | **54.9** | 74 | 80 | 46 | 70 | BELUM CUKUP | 8 | 282/142 | +0.98 | 8 | +2.60 | +0.65 | 1.9 | -0.31 | – | – |
| 18 | `M159` Heikin-Ashi Trend | **54.7** | 60 | 68 | 50 | 55 | BELUM CUKUP | 21 | 1787/1442 | -0.40 | 21 | +5.07 | +0.83 | 3.5 | -0.42 | – | -1.88 |
| 19 | `M23` Breitstein Kapitulasi + Kesina | **54.4** | 58 | 56 | 60 | 68 | BELUM CUKUP | 20 | 126/78 | -0.37 | 21 | -0.74 | -0.14 | 2.3 | +0.86 | – | 2.96 |
| 20 | `M124` 'Last' Stochastic Technique (C | **54.4** | 54 | 68 | 54 | 59 | BELUM CUKUP | 21 | 404/199 | -0.78 | 21 | +4.02 | +0.88 | 2.3 | +0.06 | – | 0.12 |
| 21 | `M13` Garis Trend Action/Safety Line | **54.2** | 56 | 70 | 50 | 55 | BELUM CUKUP | 21 | 768/484 | -0.94 | 21 | +8.79 | +2.47 | 1.3 | -0.42 | – | -0.70 |
| 22 | `N75X14` RSI14 < 40 tanpa penapis → kel | **53.9** | 80 | 66 | 42 | 70 | BELUM CUKUP | 8 | 199/41 | +1.81 | 8 | -1.06 | -0.19 | 3.1 | -0.37 | – | – |
| 23 | `M77` Undercut & Rally pada Purata B | **53.9** | 62 | 66 | 48 | 55 | BELUM CUKUP | 17 | 54/35 | -0.10 | 21 | +1.07 | +0.34 | 1.6 | -0.22 | – | -0.31 |
| 24 | `M158` Doubly Adaptive Profit Targets | **53.6** | 68 | 48 | 62 | 45 | BELUM CUKUP | 21 | 373/133 | +0.63 | 21 | -1.71 | -0.28 | 3.1 | +0.87 | – | 1.97 |
| 25 | `N75X13` RSI14 < 40 tanpa penapis → kel | **53.2** | 82 | 68 | 34 | 70 | BELUM CUKUP | 8 | 130/1 | +1.95 | 8 | -0.76 | -0.20 | 2.0 | -0.09 | – | – |
| 26 | `M30` BB Free Bar + Himpitan 50/2.5 | **53.2** | 60 | 50 | 59 | 61 | BELUM CUKUP | 19 | 228/75 | -0.03 | 21 | +1.84 | +0.24 | 4.8 | +0.69 | – | 1.16 |
| 27 | `N19X13` Bawah jalur BB + RSI<30 → kelu | **53.1** | 88 | 82 | 32 | 70 | BELUM CUKUP | 5 | 101/0 | +2.89 | 8 | +1.32 | +0.40 | 2.2 | +0.14 | – | – |
| 28 | `M91` Stochastic Pop (Bernstein/Stec | **53.1** | 53 | 61 | 52 | 85 | BELUM CUKUP | 15 | 38/18 | -1.21 | 21 | +6.14 | +0.78 | 3.4 | +0.53 | – | 2.01 |
| 29 | `N75X15` RSI14 < 40 tanpa penapis → eko | **53.0** | 83 | 68 | 32 | 70 | BELUM CUKUP | 8 | 129/0 | +2.10 | 8 | -0.76 | -0.20 | 2.0 | -0.06 | – | – |
| 30 | `M89` Chande 65sma-3cc | **53.0** | 52 | 56 | 56 | 72 | BELUM CUKUP | 21 | 184/86 | -0.72 | 21 | +1.98 | +0.32 | 3.1 | +0.24 | – | 0.55 |
| 31 | `M80` Radge Saluran Purata Bergerak  | **53.0** | 65 | 48 | 59 | 43 | BELUM CUKUP | 21 | 288/58 | +0.58 | 21 | -0.64 | -0.09 | 4.2 | +0.79 | – | 0.93 |
| 32 | `N53X36` Supertrend + ADX>25 → keluar s | **52.9** | 68 | 56 | 51 | 70 | BELUM CUKUP | 8 | 122/29 | +0.41 | 8 | +0.75 | +0.19 | 2.2 | +0.75 | – | – |
| 33 | `M46` Jurang Naik Boleh Beli (Buyabl | **52.6** | 52 | 66 | 49 | 65 | BELUM CUKUP | 13 | 36/20 | -0.76 | 21 | +1.98 | +0.40 | 1.6 | +0.23 | – | 0.34 |
| 34 | `N45X16` Undur EMA21 cerun positif → ke | **52.4** | 52 | 77 | 46 | 70 | BELUM CUKUP | 8 | 147/58 | -0.73 | 8 | +5.83 | +4.09 | 0.8 | -0.02 | – | – |
| 35 | `N64X36` Episodic pivot → keluar selepa | **51.8** | 66 | 63 | 37 | 70 | BELUM CUKUP | 7 | 49/7 | +0.76 | 8 | -0.25 | -0.06 | 2.1 | -0.23 | – | – |
| 36 | `N40X16` OBV tinggi baharu + MA50 → kel | **51.8** | 66 | 49 | 49 | 70 | BELUM CUKUP | 8 | 80/29 | +0.36 | 8 | -0.69 | -0.13 | 2.5 | +0.53 | – | – |
| 37 | `M117` Landry Pullback (high 2 bulan) | **51.8** | 66 | 42 | 58 | 45 | BELUM CUKUP | 18 | 149/19 | +0.87 | 21 | -5.25 | -0.67 | 4.2 | +1.13 | – | 1.01 |
| 38 | `M35` Pocket Pivot Morales & Kacher | **51.8** | 61 | 46 | 57 | 45 | BELUM CUKUP | 21 | 311/222 | -0.00 | 21 | -2.48 | -0.27 | 5.1 | +0.37 | – | 1.75 |
| 39 | `M70` Pecahan Hari Dalam | **51.8** | 62 | 65 | 54 | 18 | BELUM CUKUP | 21 | 471/377 | -0.37 | 21 | +1.67 | +0.34 | 2.3 | +0.01 | – | 0.03 |
| 40 | `N40X36` OBV tinggi baharu + MA50 → kel | **51.7** | 69 | 48 | 47 | 70 | BELUM CUKUP | 8 | 65/11 | +0.59 | 8 | -0.92 | -0.19 | 2.7 | +0.68 | – | – |
| 41 | `M132` Ascending Scallop (Bulkowski) | **51.6** | 41 | 66 | 51 | 80 | BELUM CUKUP | 17 | 94/37 | -1.47 | 21 | +3.71 | +0.99 | 2.2 | +0.12 | – | 0.85 |
| 42 | `M105` Supertrend tulen | **51.5** | 53 | 50 | 57 | 51 | BELUM CUKUP | 21 | 367/111 | -0.40 | 21 | +1.43 | +0.20 | 3.8 | +0.39 | – | 0.94 |
| 43 | `N64X16` Episodic pivot → keluar bila s | **51.4** | 66 | 59 | 37 | 70 | BELUM CUKUP | 7 | 49/6 | +0.81 | 8 | -1.17 | -0.29 | 2.0 | -0.24 | – | – |
| 44 | `M129` Wick Play | **51.4** | 50 | 61 | 46 | 79 | BELUM CUKUP | 10 | 26/10 | -1.10 | 21 | +4.33 | +1.54 | 1.0 | +0.22 | – | 0.80 |
| 45 | `M05` MACD Divergence + Pengesahan | **51.3** | 51 | 65 | 44 | 55 | BELUM CUKUP | 15 | 41/12 | -0.77 | 21 | +2.29 | +0.67 | 1.5 | -0.25 | – | -0.36 |
| 46 | `N64X14` Episodic pivot → keluar bila r | **51.2** | 67 | 59 | 34 | 70 | BELUM CUKUP | 7 | 49/2 | +0.88 | 8 | -1.17 | -0.29 | 2.0 | -0.22 | – | – |
| 47 | `M104` High Tight Flag / Power Play | **51.1** | 80 | 90 | 49 | 85 | BELUM CUKUP | 1 | 1/0 | +20.61 | 6 | +2.08 | +10.00 | 0.0 | +2.56 | – | 18.84 |
| 48 | `N64X17` Episodic pivot → keluar bila a | **51.0** | 60 | 60 | 37 | 70 | BELUM CUKUP | 7 | 49/11 | +0.31 | 8 | -0.41 | -0.10 | 2.1 | -0.40 | – | – |
| 49 | `M51` O'Neil Cawan & Pemegang | **50.7** | 70 | 63 | 39 | 58 | BELUM CUKUP | 2 | 3/0 | +0.47 | 11 | +0.20 | +0.20 | 0.5 | +1.22 | – | 3.66 |
| 50 | `N28X36` ADX>25 + DI+ > DI- → keluar se | **50.5** | 56 | 46 | 46 | 70 | BELUM CUKUP | 8 | 308/178 | +0.22 | 8 | -2.44 | -0.39 | 3.6 | -0.25 | – | – |
| 51 | `M37` Weinstein Peringkat 2 | **50.4** | 61 | 77 | 28 | 55 | BELUM CUKUP | 3 | 7/0 | +0.38 | 15 | +0.41 | +0.49 | 0.3 | -0.16 | – | -0.10 |
| 52 | `N203X36` Gap 2% lalu MA20 silang MA50 x | **50.3** | 73 | 82 | 27 | 50 | BELUM CUKUP | 1 | 4/0 | +1.34 | 1 | +0.62 | +10.00 | – | – | – | – |
| 53 | `N25X36` Supertrend + EMA + ADX>23 → ke | **50.2** | 51 | 55 | 41 | 70 | BELUM CUKUP | 8 | 125/26 | -0.69 | 8 | +0.29 | +0.06 | 2.3 | -0.38 | – | – |
| 54 | `N48X36` Inside day pecah → keluar sele | **50.2** | 54 | 48 | 43 | 70 | BELUM CUKUP | 8 | 308/203 | +0.26 | 8 | -2.52 | -0.30 | 5.4 | -0.66 | – | – |
| 55 | `N73X13` Tutup bawah jalur bawah BB(20, | **50.2** | 72 | 56 | 34 | 30 | BELUM CUKUP | 8 | 141/1 | +1.47 | 8 | -2.79 | -0.44 | 3.4 | -0.12 | – | – |
| 56 | `M02` MACD + SMA200 | **50.0** | 45 | 58 | 47 | 55 | BELUM CUKUP | 21 | 130/78 | -1.69 | 21 | +5.05 | +0.74 | 2.2 | -0.76 | – | -3.46 |
| 57 | `M131` Ross Hook (Joe Ross) | **50.0** | 51 | 52 | 56 | 31 | BELUM CUKUP | 21 | 261/114 | -0.68 | 21 | +0.32 | +0.05 | 3.3 | +0.26 | – | 0.54 |
| 58 | `M39` Radge Pecahan Bollinger 100 ha | **49.9** | 38 | 65 | 51 | 55 | BELUM CUKUP | 20 | 239/51 | -1.73 | 21 | +7.97 | +3.32 | 1.1 | -0.04 | – | -0.08 |
| 59 | `N202X36` RSI2<10 dalam trend naik x X36 | **49.9** | 49 | 79 | 27 | 50 | BELUM CUKUP | 1 | 9/0 | -0.09 | 1 | +0.10 | +10.00 | – | – | – | – |
| 60 | `N201X36` MA20 silang MA50 atas MA50 x X | **49.9** | 46 | 76 | 27 | 50 | BELUM CUKUP | 1 | 7/0 | -0.14 | 1 | +0.04 | +10.00 | – | – | – | – |
| 61 | `M153` Range Leader | **49.8** | 54 | 42 | 58 | 45 | BELUM CUKUP | 21 | 1325/1134 | +0.01 | 21 | -3.52 | -0.36 | 6.5 | +0.41 | – | 1.96 |
| 62 | `N42X36` Lonjakan volum 2x → keluar sel | **49.8** | 55 | 43 | 43 | 70 | BELUM CUKUP | 8 | 188/92 | +0.17 | 8 | -2.80 | -0.38 | 4.1 | -0.59 | – | – |
| 63 | `N124X15` Episodic pivot gap 8-10% → eko | **49.8** | 62 | 51 | 30 | 70 | BELUM CUKUP | 8 | 41/0 | +0.80 | 8 | -1.70 | -0.26 | 3.2 | -0.33 | – | – |
| 64 | `M92` CCI-50 | **49.7** | 56 | 49 | 54 | 26 | BELUM CUKUP | 21 | 557/353 | -0.17 | 21 | -0.66 | -0.11 | 2.9 | -0.02 | – | -0.03 |
| 65 | `N42X14` Lonjakan volum 2x → keluar bil | **49.7** | 61 | 42 | 38 | 70 | BELUM CUKUP | 8 | 174/15 | +0.64 | 8 | -4.51 | -0.41 | 5.4 | -0.46 | – | – |
| 66 | `M15` Break & Retest + Henti ATR | **49.6** | 60 | 44 | 56 | 27 | BELUM CUKUP | 21 | 303/186 | +0.21 | 21 | -3.78 | -0.47 | 4.1 | +0.19 | – | 0.39 |
| 67 | `N42X15` Lonjakan volum 2x → ekori Chan | **49.4** | 64 | 46 | 28 | 70 | BELUM CUKUP | 8 | 163/0 | +0.66 | 8 | -2.38 | -0.21 | 5.3 | -0.47 | – | – |
| 68 | `N24X36` Supertrend(10,3) + ADX>20 → ke | **49.2** | 50 | 42 | 42 | 70 | BELUM CUKUP | 8 | 150/46 | -0.56 | 8 | -1.48 | -0.33 | 2.7 | -0.51 | – | – |
| 69 | `M07` Qullamaggie Breakout | **49.2** | 28 | 64 | 27 | 15 | BELUM CUKUP | 1 | 1/1 | -2.53 | 21 | -0.25 | -0.21 | 0.8 | -0.22 | – | -1.12 |
| 70 | `N42X16` Lonjakan volum 2x → keluar bil | **49.1** | 54 | 39 | 44 | 60 | BELUM CUKUP | 8 | 192/89 | +0.20 | 8 | -4.04 | -0.62 | 4.2 | -0.53 | – | – |
| 71 | `M08` SMA20 + SMA200 | **49.0** | 48 | 42 | 52 | 55 | BELUM CUKUP | 19 | 201/107 | -0.61 | 21 | -2.08 | -0.39 | 3.6 | -0.21 | – | -0.52 |
| 72 | `N36X36` Pocket pivot → keluar selepas  | **49.0** | 43 | 53 | 38 | 70 | BELUM CUKUP | 8 | 147/59 | -1.25 | 8 | +2.30 | +0.44 | 2.3 | -0.98 | – | – |
| 73 | `N42X17` Lonjakan volum 2x → keluar bil | **49.0** | 53 | 37 | 43 | 70 | BELUM CUKUP | 8 | 187/55 | +0.28 | 8 | -5.90 | -0.61 | 5.3 | -0.43 | – | – |
| 74 | `M27` Price Action 4 Tiang | **49.0** | 46 | 40 | 43 | 15 | BELUM CUKUP | 2 | 546/450 | -0.85 | 21 | -2.72 | -0.53 | 2.9 | -0.40 | – | -1.09 |
| 75 | `M45` High 52 Minggu (George & Hwang | **49.0** | 18 | 44 | 31 | 43 | BELUM CUKUP | 1 | 2/1 | -3.79 | 10 | -0.74 | -0.41 | 0.9 | +0.22 | – | 0.79 |
| 76 | `N16X13` RSI2<10 tanpa penapis → keluar | **48.9** | 52 | 46 | 33 | 70 | BELUM CUKUP | 8 | 138/4 | +0.25 | 8 | -2.99 | -0.33 | 5.7 | -0.57 | – | – |
| 77 | `M01` Bollinger Band + RSI | **48.8** | 79 | 40 | 47 | 15 | BELUM CUKUP | 20 | 113/24 | +2.40 | 21 | -6.28 | -0.58 | 4.4 | -0.28 | – | -1.15 |
| 78 | `N119X13` 3 tutup turun berturut → kelua | **48.8** | 47 | 48 | 35 | 70 | BELUM CUKUP | 8 | 205/39 | -0.36 | 8 | -2.37 | -0.29 | 6.1 | -1.21 | – | – |
| 79 | `N65X14` Gap 4% + volum + hampir 52w →  | **48.8** | 50 | 50 | 27 | 69 | BELUM CUKUP | 6 | 31/1 | -0.24 | 8 | -1.74 | -0.42 | 2.4 | -0.77 | – | – |
| 80 | `N36X16` Pocket pivot → keluar bila sup | **48.7** | 39 | 55 | 39 | 70 | BELUM CUKUP | 8 | 152/54 | -1.32 | 8 | +1.36 | +0.49 | 1.5 | -0.91 | – | – |
| 81 | `N43X36` Undur EMA8 + penapis MA50 → ke | **48.7** | 45 | 46 | 39 | 70 | BELUM CUKUP | 8 | 162/29 | -0.67 | 8 | -0.91 | -0.23 | 2.1 | -0.67 | – | – |
| 82 | `N28X16` ADX>25 + DI+ > DI- → keluar bi | **48.7** | 43 | 47 | 40 | 70 | BELUM CUKUP | 8 | 324/186 | -0.42 | 8 | -2.37 | -0.38 | 3.6 | -1.04 | – | – |
| 83 | `N55X13` BB + RSI + ADX>20 → keluar bil | **48.5** | 54 | 52 | 26 | 57 | BELUM CUKUP | 8 | 62/0 | +0.15 | 8 | -1.88 | -0.41 | 3.2 | -0.76 | – | – |
| 84 | `M84` Jarak purata bergerak MAD 21/2 | **48.5** | 18 | 14 | 34 | 15 | BELUM CUKUP | 1 | 58/38 | -3.80 | 10 | -7.26 | -0.93 | 6.2 | -0.64 | – | -1.99 |
| 85 | `M94` Pecutan Momentum (Chen, Yu & W | **48.5** | 17 | 17 | 20 | 38 | BELUM CUKUP | 1 | 33/0 | -6.26 | 10 | -5.84 | -0.50 | 6.8 | -0.75 | – | -2.87 |
| 86 | `N65X36` Gap 4% + volum + hampir 52w →  | **48.4** | 50 | 48 | 27 | 60 | BELUM CUKUP | 6 | 31/1 | -0.25 | 8 | -2.10 | -0.50 | 2.5 | -0.77 | – | – |
| 87 | `N124X36` Episodic pivot gap 8-10% → kel | **48.3** | 55 | 41 | 38 | 34 | BELUM CUKUP | 8 | 41/13 | +0.28 | 8 | -3.42 | -0.69 | 3.3 | -0.44 | – | – |
| 88 | `M21` Marius 3 Persediaan (Pecahan+J | **48.2** | 34 | 51 | 41 | 45 | BELUM CUKUP | 5 | 5/3 | -1.45 | 13 | -0.70 | -0.32 | 1.3 | +0.61 | – | 0.99 |
| 89 | `M96` Momo India: Ranking Sharpe 3/6 | **48.2** | 15 | 9 | 9 | 15 | BELUM CUKUP | 1 | 6/6 | -13.40 | 10 | -8.03 | -1.00 | 6.4 | -5.74 | – | -15.35 |
| 90 | `N08X36` tutup>EMA20 tidak terlalu jauh | **48.0** | 38 | 46 | 38 | 70 | BELUM CUKUP | 8 | 359/217 | -1.06 | 8 | -1.49 | -0.27 | 2.7 | -1.18 | – | – |
| 91 | `N07X16` Tiga MA tersusun → keluar bila | **47.9** | 37 | 57 | 36 | 47 | BELUM CUKUP | 8 | 136/19 | -1.24 | 8 | +0.54 | +0.13 | 2.0 | -0.83 | – | – |
| 92 | `N37X17` Gap and go → keluar bila adx14 | **47.9** | 38 | 46 | 36 | 70 | BELUM CUKUP | 7 | 83/27 | -1.09 | 8 | -0.08 | -0.02 | 2.1 | -0.92 | – | – |
| 93 | `M18` EMA9/21 Pullback | **47.8** | 57 | 40 | 54 | 20 | BELUM CUKUP | 21 | 379/264 | -0.09 | 21 | -4.39 | -0.73 | 4.1 | +0.05 | – | 0.17 |
| 94 | `M04` BB Squeeze Breakout | **47.8** | 40 | 43 | 55 | 53 | BELUM CUKUP | 19 | 153/56 | -1.31 | 21 | +1.22 | +0.15 | 4.0 | +0.36 | – | 0.55 |
| 95 | `N09X36` Undur EMA10 + penapis EMA50 →  | **47.8** | 39 | 42 | 39 | 70 | BELUM CUKUP | 8 | 167/44 | -1.04 | 8 | -1.48 | -0.38 | 2.0 | -0.78 | – | – |
| 96 | `N35X36` Pecah 52 minggu tinggi → kelua | **47.8** | 36 | 62 | 26 | 70 | BELUM CUKUP | 7 | 47/1 | -1.28 | 8 | +0.81 | +0.45 | 0.9 | -1.03 | – | – |
| 97 | `M41` FW Penyatuan Mingguan | **47.8** | 39 | 30 | 42 | 36 | BELUM CUKUP | 4 | 63/9 | -0.62 | 20 | -4.09 | -0.49 | 4.8 | +0.40 | – | 0.69 |
| 98 | `N37X36` Gap and go → keluar selepas DU | **47.7** | 36 | 44 | 36 | 70 | BELUM CUKUP | 7 | 83/22 | -1.09 | 8 | -0.58 | -0.16 | 2.3 | -0.84 | – | – |
| 99 | `N66X36` 52w tinggi + pengesahan 1% → k | **47.7** | 43 | 39 | 30 | 70 | BELUM CUKUP | 6 | 37/1 | -0.56 | 7 | -2.85 | -0.69 | 2.8 | -0.50 | – | – |
| 100 | `M78` Alvarez Pecahan Mingguan DTAYS | **47.6** | 18 | 22 | 41 | 17 | BELUM CUKUP | 2 | 73/39 | -1.96 | 20 | -8.00 | -0.77 | 7.0 | +0.02 | – | 0.08 |
| 101 | `N08X16` tutup>EMA20 tidak terlalu jauh | **47.3** | 34 | 46 | 36 | 70 | BELUM CUKUP | 8 | 418/247 | -1.16 | 8 | -1.06 | -0.34 | 2.0 | -1.44 | – | – |
| 102 | `N45X36` Undur EMA21 cerun positif → ke | **47.1** | 36 | 50 | 37 | 36 | BELUM CUKUP | 8 | 120/36 | -1.29 | 8 | -0.19 | -0.09 | 1.5 | -0.92 | – | – |
| 103 | `N41X36` CMF20>0 + tutup>EMA20 → keluar | **47.1** | 33 | 42 | 38 | 70 | BELUM CUKUP | 8 | 218/129 | -1.41 | 8 | -1.96 | -0.40 | 2.7 | -1.17 | – | – |
| 104 | `M134` First Kiss After Daylight (Lan | **47.0** | 44 | 42 | 50 | 30 | BELUM CUKUP | 16 | 56/16 | -0.83 | 21 | -1.94 | -0.28 | 3.8 | +0.43 | – | 0.50 |
| 105 | `N68X36` Bullish engulfing + EMA21 → ke | **47.0** | 34 | 47 | 40 | 39 | BELUM CUKUP | 8 | 73/16 | -1.27 | 8 | -0.45 | -0.11 | 2.3 | -0.28 | – | – |
| 106 | `M106` DMI Wilder | **46.8** | 49 | 44 | 53 | 17 | BELUM CUKUP | 19 | 129/72 | -0.63 | 21 | -1.29 | -0.29 | 2.6 | +0.03 | – | 0.06 |
| 107 | `N76X16` Tutup > MA50 (penapis trend tu | **46.8** | 29 | 50 | 34 | 70 | BELUM CUKUP | 8 | 276/134 | -1.47 | 8 | -0.31 | -0.09 | 1.7 | -1.66 | – | – |
| 108 | `N37X16` Gap and go → keluar bila super | **46.8** | 33 | 39 | 34 | 70 | BELUM CUKUP | 7 | 83/19 | -1.20 | 8 | -1.46 | -0.39 | 2.1 | -0.99 | – | – |
| 109 | `M138` 直升机空中加油 (Helikopter isi minyak | **46.8** | 27 | 42 | 16 | 15 | BELUM CUKUP | 3 | 3/0 | -3.38 | 14 | -0.95 | -0.84 | 0.5 | -1.51 | – | -2.59 |
| 110 | `M116` 2/20 EMA Breakout (Landry) | **46.7** | 48 | 39 | 55 | 24 | BELUM CUKUP | 21 | 571/398 | -0.36 | 21 | -1.69 | -0.14 | 7.5 | +0.08 | – | 0.30 |
| 111 | `M54` IBD Power Trend | **46.7** | 45 | 48 | 51 | 20 | BELUM CUKUP | 20 | 209/106 | -1.32 | 21 | +2.60 | +0.25 | 5.3 | -0.30 | – | -0.63 |
| 112 | `M150` Trend Bar Failure (Brooks) | **46.7** | 54 | 42 | 50 | 15 | BELUM CUKUP | 19 | 103/45 | -0.02 | 21 | -4.54 | -0.77 | 3.0 | -0.10 | – | -0.28 |
| 113 | `M68` Kell Base n' Break | **46.7** | 31 | 52 | 46 | 50 | BELUM CUKUP | 14 | 43/13 | -2.42 | 21 | +1.22 | +0.27 | 1.9 | +0.08 | – | 0.54 |
| 114 | `M38` Darvas Kotak | **46.7** | 20 | 38 | 34 | 45 | BELUM CUKUP | 4 | 23/1 | -2.18 | 20 | -2.46 | -0.25 | 5.1 | +0.21 | – | 1.03 |
| 115 | `M148` Natural Number Method | **46.5** | 33 | 56 | 42 | 55 | BELUM CUKUP | 21 | 223/157 | -2.01 | 21 | +1.67 | +0.32 | 2.6 | -1.38 | – | -4.34 |
| 116 | `N50X14` Mampat + pecah volum 1.5x → ke | **46.5** | 23 | 42 | 30 | 70 | BELUM CUKUP | 5 | 15/3 | -2.53 | 8 | -3.56 | -0.39 | 4.3 | -0.73 | – | – |
| 117 | `N41X16` CMF20>0 + tutup>EMA20 → keluar | **46.4** | 26 | 51 | 33 | 70 | BELUM CUKUP | 8 | 258/142 | -1.74 | 8 | -0.12 | -0.05 | 1.6 | -1.77 | – | – |
| 118 | `N28X14` ADX>25 + DI+ > DI- → keluar bi | **46.4** | 34 | 38 | 32 | 70 | BELUM CUKUP | 8 | 179/11 | -1.19 | 8 | -2.64 | -0.43 | 3.3 | -1.07 | – | – |
| 119 | `N119X15` 3 tutup turun berturut → ekori | **46.4** | 34 | 43 | 20 | 70 | BELUM CUKUP | 6 | 47/0 | -1.08 | 8 | -3.35 | -0.49 | 4.6 | -1.36 | – | – |
| 120 | `M64` O'Neil Tiga Minggu Ketat | **46.4** | 24 | 23 | 25 | 15 | BELUM CUKUP | 3 | 3/2 | -12.32 | 21 | -3.66 | -0.83 | 2.5 | -1.19 | – | -14.38 |
| 121 | `M31` Band Walk (BB 20/2) | **46.3** | 51 | 30 | 57 | 32 | BELUM CUKUP | 21 | 399/99 | -0.26 | 21 | -2.12 | -0.19 | 7.2 | +0.35 | – | 0.55 |
| 122 | `M88` O'Neil Shakeout +3 | **46.3** | 31 | 49 | 48 | 55 | BELUM CUKUP | 17 | 75/35 | -2.01 | 21 | +1.41 | +0.14 | 4.7 | -0.15 | – | -0.24 |
| 123 | `N76X36` Tutup > MA50 (penapis trend tu | **46.3** | 35 | 34 | 38 | 53 | BELUM CUKUP | 8 | 174/53 | -1.07 | 8 | -3.78 | -0.69 | 3.9 | -0.99 | – | – |
| 124 | `N50X17` Mampat + pecah volum 1.5x → ke | **46.3** | 20 | 43 | 29 | 70 | BELUM CUKUP | 5 | 14/2 | -2.59 | 8 | -2.96 | -0.32 | 4.4 | -0.67 | – | – |
| 125 | `N74X16` MACD atas garis isyarat (keada | **46.2** | 31 | 37 | 36 | 70 | BELUM CUKUP | 8 | 460/277 | -1.10 | 8 | -4.32 | -0.59 | 4.8 | -1.44 | – | – |
| 126 | `N38X36` VCP pecah → keluar selepas DUA | **46.2** | 36 | 45 | 26 | 50 | BELUM CUKUP | 8 | 30/7 | -1.33 | 8 | -1.37 | -0.42 | 1.9 | -1.63 | – | – |
| 127 | `N56X16` RSI>50 + ADX>20 → keluar bila  | **46.2** | 30 | 39 | 36 | 70 | BELUM CUKUP | 8 | 202/76 | -1.08 | 8 | -3.15 | -0.62 | 3.3 | -1.39 | – | – |
| 128 | `N25X16` Supertrend + EMA + ADX>23 → ke | **46.2** | 30 | 45 | 30 | 66 | BELUM CUKUP | 8 | 113/4 | -1.51 | 8 | -1.50 | -0.31 | 2.6 | -0.98 | – | – |
| 129 | `M157` Consolidation Pivot Breakout ( | **46.2** | 24 | 37 | 28 | 15 | BELUM CUKUP | 4 | 4/3 | -4.78 | 18 | -1.89 | -0.64 | 1.6 | -0.77 | – | -2.12 |
| 130 | `N22X36` BB pecah atas + RSI → keluar s | **46.1** | 23 | 43 | 44 | 70 | BELUM CUKUP | 8 | 116/37 | -2.23 | 8 | -1.09 | -0.29 | 2.2 | -0.15 | – | – |
| 131 | `N16X15` RSI2<10 tanpa penapis → ekori  | **46.1** | 44 | 35 | 27 | 43 | BELUM CUKUP | 8 | 133/0 | +0.05 | 8 | -6.09 | -0.52 | 8.2 | -0.63 | – | – |
| 132 | `M102` Stockbee SLTB | **46.0** | 48 | 44 | 51 | 15 | BELUM CUKUP | 21 | 376/276 | -1.10 | 21 | -0.83 | -0.08 | 5.5 | -0.34 | – | -0.86 |
| 133 | `M12` Parabolic SAR | **46.0** | 37 | 47 | 51 | 28 | BELUM CUKUP | 21 | 381/194 | -1.50 | 21 | +0.21 | +0.04 | 2.9 | -0.31 | – | -0.68 |
| 134 | `N36X14` Pocket pivot → keluar bila rsi | **46.0** | 32 | 35 | 34 | 70 | BELUM CUKUP | 8 | 146/19 | -1.48 | 8 | -1.79 | -0.26 | 3.5 | -0.99 | – | – |
| 135 | `N07X36` Tiga MA tersusun → keluar sele | **46.0** | 33 | 46 | 32 | 30 | BELUM CUKUP | 8 | 136/8 | -1.38 | 8 | -1.15 | -0.29 | 2.5 | -0.92 | – | – |
| 136 | `M49` Ichimoku (Tutup Atas Awan + Te | **45.9** | 43 | 51 | 48 | 15 | BELUM CUKUP | 21 | 301/165 | -1.42 | 21 | +1.16 | +0.17 | 3.4 | -0.68 | – | -0.86 |
| 137 | `N25X17` Supertrend + EMA + ADX>23 → ke | **45.9** | 26 | 47 | 29 | 70 | BELUM CUKUP | 8 | 109/4 | -1.73 | 8 | -0.89 | -0.18 | 2.5 | -1.05 | – | – |
| 138 | `N80X36` Tinggi sepanjang masa → keluar | **45.9** | 36 | 38 | 30 | 30 | BELUM CUKUP | 7 | 38/1 | -0.98 | 8 | -2.44 | -0.70 | 1.9 | -0.55 | – | – |
| 139 | `M120` Reversal New Highs | **45.8** | 43 | 41 | 45 | 17 | BELUM CUKUP | 13 | 19/12 | -1.01 | 21 | -1.22 | -0.19 | 3.2 | +0.01 | – | 0.08 |
| 140 | `N113X16` 80-20 bar (sisi beli) → keluar | **45.4** | 44 | 22 | 42 | 30 | BELUM CUKUP | 8 | 293/205 | +0.14 | 8 | -8.39 | -1.00 | 6.9 | -0.83 | – | – |
| 141 | `N33X16` Donchian20 + penapis MA200 → k | **45.4** | 23 | 53 | 26 | 70 | BELUM CUKUP | 8 | 98/7 | -2.35 | 8 | +0.20 | +0.06 | 1.7 | -1.66 | – | – |
| 142 | `N56X36` RSI>50 + ADX>20 → keluar selep | **45.4** | 31 | 30 | 36 | 54 | BELUM CUKUP | 8 | 187/72 | -1.10 | 8 | -5.29 | -0.72 | 5.5 | -1.28 | – | – |
| 143 | `N28X17` ADX>25 + DI+ > DI- → keluar bi | **45.3** | 33 | 36 | 24 | 70 | BELUM CUKUP | 8 | 120/0 | -1.15 | 8 | -3.42 | -0.48 | 3.8 | -1.05 | – | – |
| 144 | `M144` Screw Bar | **45.3** | 27 | 37 | 34 | 15 | BELUM CUKUP | 6 | 9/7 | -1.79 | 19 | -1.57 | -0.60 | 1.1 | -0.52 | – | -1.13 |
| 145 | `M139` 均线首次粘合向上发散 (MA berhimpun kali  | **45.2** | 31 | 44 | 48 | 55 | BELUM CUKUP | 21 | 86/24 | -1.94 | 21 | +0.38 | +0.05 | 2.9 | -0.18 | – | -0.54 |
| 146 | `M107` Golden Cross SMA50/200 | **45.2** | 44 | 45 | 44 | 15 | BELUM CUKUP | 18 | 39/7 | -0.90 | 21 | -0.79 | -0.22 | 1.9 | -0.03 | – | -0.04 |
| 147 | `N56X17` RSI>50 + ADX>20 → keluar bila  | **45.2** | 22 | 44 | 30 | 70 | BELUM CUKUP | 8 | 134/21 | -1.87 | 8 | -1.25 | -0.25 | 2.4 | -1.55 | – | – |
| 148 | `N37X14` Gap and go → keluar bila rsi14 | **45.2** | 29 | 32 | 30 | 44 | BELUM CUKUP | 7 | 82/7 | -1.39 | 8 | -2.62 | -0.62 | 2.7 | -1.05 | – | – |
| 149 | `M34` Carter TTM Squeeze | **45.1** | 46 | 39 | 51 | 16 | BELUM CUKUP | 20 | 104/47 | -0.93 | 21 | -0.01 | -0.00 | 3.9 | -0.08 | – | -0.24 |
| 150 | `M32` Momentum Burst | **45.1** | 48 | 25 | 50 | 28 | BELUM CUKUP | 14 | 57/35 | -0.63 | 21 | -5.30 | -0.48 | 7.3 | +0.17 | – | 0.43 |
| 151 | `N68X16` Bullish engulfing + EMA21 → ke | **45.1** | 24 | 45 | 37 | 30 | BELUM CUKUP | 8 | 72/14 | -1.64 | 8 | -0.86 | -0.16 | 2.8 | -0.55 | – | – |
| 152 | `N51X36` BB squeeze + Supertrend → kelu | **45.1** | 19 | 34 | 24 | 30 | BELUM CUKUP | 5 | 8/2 | -2.41 | 8 | -1.81 | -0.67 | 2.1 | -1.25 | – | – |
| 153 | `M136` Short/Intermediate-term Low (L | **45.0** | 40 | 45 | 52 | 15 | BELUM CUKUP | 21 | 777/278 | -1.16 | 21 | -0.57 | -0.12 | 2.7 | -0.25 | – | -0.11 |
| 154 | `M115` Bow Tie (Landry) | **45.0** | 29 | 37 | 48 | 33 | BELUM CUKUP | 11 | 36/25 | -2.02 | 21 | -4.60 | -0.56 | 4.3 | +0.11 | – | 0.60 |
| 155 | `M128` Inventory Retracement Bar (IRB | **44.9** | 45 | 34 | 54 | 20 | BELUM CUKUP | 20 | 152/81 | -0.54 | 21 | -4.11 | -0.37 | 6.6 | +0.04 | – | 0.18 |
| 156 | `N47X16` NR7 + EMA9>EMA21 → keluar bila | **44.9** | 28 | 39 | 30 | 35 | BELUM CUKUP | 8 | 170/30 | -1.27 | 8 | -3.71 | -0.86 | 2.7 | -1.68 | – | – |
| 157 | `N39X36` NR7 kemudian pecah → keluar se | **44.9** | 13 | 24 | 18 | 48 | BELUM CUKUP | 4 | 27/5 | -4.01 | 7 | -3.32 | -0.92 | 2.4 | -2.20 | – | – |
| 158 | `N113X36` 80-20 bar (sisi beli) → keluar | **44.8** | 36 | 24 | 40 | 30 | BELUM CUKUP | 8 | 277/196 | -0.45 | 8 | -7.23 | -1.00 | 6.2 | -1.06 | – | – |
| 159 | `N51X16` BB squeeze + Supertrend → kelu | **44.8** | 18 | 34 | 22 | 30 | BELUM CUKUP | 5 | 8/1 | -2.83 | 8 | -2.13 | -0.68 | 2.2 | -1.32 | – | – |
| 160 | `M26` Garis Trend Undur 3 Sentuhan + | **44.7** | 41 | 41 | 47 | 15 | BELUM CUKUP | 17 | 74/47 | -0.57 | 21 | -3.57 | -0.44 | 3.8 | -0.41 | – | -0.59 |
| 161 | `N53X16` Supertrend + ADX>25 → keluar b | **44.7** | 27 | 34 | 36 | 30 | BELUM CUKUP | 8 | 107/6 | -1.37 | 8 | -4.43 | -0.67 | 4.3 | -0.34 | – | – |
| 162 | `N57X36` ADX bangkit daripada <20 → kel | **44.7** | 21 | 52 | 27 | 43 | BELUM CUKUP | 8 | 72/7 | -2.53 | 8 | +0.38 | +0.11 | 2.0 | -1.52 | – | – |
| 163 | `N33X36` Donchian20 + penapis MA200 → k | **44.6** | 21 | 42 | 31 | 49 | BELUM CUKUP | 8 | 96/20 | -1.98 | 8 | -2.16 | -0.59 | 2.0 | -1.43 | – | – |
| 164 | `N27X16` Ichimoku atas awan → keluar bi | **44.6** | 26 | 36 | 33 | 30 | BELUM CUKUP | 8 | 154/60 | -1.40 | 8 | -2.60 | -0.82 | 2.1 | -1.62 | – | – |
| 165 | `M87` IBD Tapak Menaik | **44.5** | 27 | 31 | 37 | 15 | BELUM CUKUP | 7 | 10/6 | -3.92 | 21 | -3.90 | -0.62 | 3.8 | -0.45 | – | -1.50 |
| 166 | `M149` 3-Step Pullback | **44.4** | 40 | 34 | 54 | 23 | BELUM CUKUP | 19 | 209/58 | -0.98 | 21 | -3.47 | -0.32 | 5.7 | +0.30 | – | 0.25 |
| 167 | `M143` 장대양봉 이후 눌림목 / 5일선 매매 (Undur ke | **44.4** | 28 | 51 | 29 | 51 | BELUM CUKUP | 13 | 25/1 | -1.48 | 20 | -0.38 | -0.13 | 1.7 | -0.90 | – | -8.77 |
| 168 | `N22X16` BB pecah atas + RSI → keluar b | **44.4** | 20 | 39 | 41 | 30 | BELUM CUKUP | 8 | 118/22 | -2.22 | 8 | -1.79 | -0.50 | 2.5 | -0.31 | – | – |
| 169 | `N57X16` ADX bangkit daripada <20 → kel | **44.4** | 20 | 51 | 25 | 43 | BELUM CUKUP | 8 | 70/5 | -2.61 | 8 | +0.38 | +0.11 | 2.0 | -1.56 | – | – |
| 170 | `M36` Turtle 55/20 | **44.3** | 40 | 38 | 54 | 16 | BELUM CUKUP | 21 | 341/160 | -1.10 | 21 | -1.93 | -0.16 | 6.6 | +0.02 | – | 0.04 |
| 171 | `N24X17` Supertrend(10,3) + ADX>20 → ke | **44.3** | 19 | 42 | 27 | 70 | BELUM CUKUP | 8 | 121/14 | -2.03 | 8 | -1.68 | -0.45 | 1.9 | -1.71 | – | – |
| 172 | `N33X14` Donchian20 + penapis MA200 → k | **44.3** | 21 | 42 | 26 | 55 | BELUM CUKUP | 8 | 107/5 | -2.41 | 8 | -1.77 | -0.43 | 2.3 | -1.49 | – | – |
| 173 | `M20` EMA10/15 Crossover + Sudut | **44.2** | 42 | 41 | 47 | 15 | BELUM CUKUP | 21 | 464/363 | -1.02 | 21 | -2.67 | -0.46 | 3.0 | -0.82 | – | -5.12 |
| 174 | `M06` Minervini VCP Breakout | **44.2** | 32 | 54 | 47 | 15 | BELUM CUKUP | 20 | 82/39 | -1.83 | 21 | +0.54 | +0.09 | 2.9 | -0.46 | – | -1.13 |
| 175 | `M127` Slingshot Bullish | **43.8** | 34 | 47 | 44 | 15 | BELUM CUKUP | 18 | 107/77 | -1.65 | 21 | -2.31 | -0.34 | 3.1 | -0.95 | – | -1.16 |
| 176 | `N24X16` Supertrend(10,3) + ADX>20 → ke | **43.8** | 20 | 39 | 23 | 57 | BELUM CUKUP | 8 | 117/3 | -1.93 | 8 | -1.84 | -0.54 | 1.9 | -1.67 | – | – |
| 177 | `N53X17` Supertrend + ADX>25 → keluar b | **43.8** | 23 | 34 | 29 | 30 | BELUM CUKUP | 8 | 100/0 | -1.58 | 8 | -4.04 | -0.65 | 4.1 | -0.37 | – | – |
| 178 | `M28` VWAP Separator + Kiss Pivot | **43.7** | 41 | 37 | 48 | 15 | BELUM CUKUP | 19 | 116/94 | -0.75 | 21 | -5.22 | -0.62 | 5.4 | -0.70 | – | -6.74 |
| 179 | `N31X36` Turtle sistem 2 → keluar selep | **43.7** | 19 | 33 | 26 | 34 | BELUM CUKUP | 7 | 99/3 | -2.20 | 8 | -2.81 | -0.77 | 2.4 | -1.33 | – | – |
| 180 | `M44` Tapak Rata IBD | **43.6** | 29 | 38 | 22 | 15 | BELUM CUKUP | 8 | 9/5 | -4.19 | 21 | -3.67 | -0.78 | 2.9 | -2.21 | – | -30.87 |
| 181 | `N06X36` Golden cross MA50/MA200 → kelu | **43.5** | 16 | 38 | 25 | 36 | BELUM CUKUP | 7 | 19/2 | -1.96 | 8 | -3.09 | -0.76 | 2.6 | -1.23 | – | – |
| 182 | `M14` Walking with the Whales | **43.3** | 45 | 31 | 49 | 15 | BELUM CUKUP | 21 | 940/641 | -0.58 | 21 | -7.76 | -0.73 | 6.5 | -0.54 | – | -0.84 |
| 183 | `M03` BB Break + Divergence RSI | **43.3** | 36 | 38 | 52 | 15 | BELUM CUKUP | 21 | 416/322 | -0.76 | 21 | -3.52 | -0.56 | 3.1 | -0.25 | – | -0.76 |
| 184 | `N54X36` Supertrend + RSI>50 → keluar s | **43.2** | 24 | 21 | 36 | 30 | BELUM CUKUP | 8 | 159/63 | -1.42 | 8 | -8.01 | -0.97 | 6.7 | -1.28 | – | – |
| 185 | `M121` High 2 bull flag (Brooks) | **43.1** | 11 | 16 | 24 | 15 | BELUM CUKUP | 5 | 7/4 | -9.37 | 17 | -6.51 | -0.78 | 5.0 | -1.50 | – | -20.85 |
| 186 | `M50` Elder Triple Screen | **43.0** | 42 | 31 | 51 | 15 | BELUM CUKUP | 21 | 577/349 | -0.73 | 21 | -7.53 | -0.68 | 6.6 | -0.36 | – | -0.57 |
| 187 | `M73` ADX(5) > 40 + Julat Terkecil 6 | **43.0** | 41 | 33 | 50 | 15 | BELUM CUKUP | 21 | 1022/798 | -0.10 | 21 | -7.31 | -0.91 | 4.9 | -0.51 | – | -3.17 |
| 188 | `N29X16` PSAR naik + tutup>MA50 → kelua | **43.0** | 15 | 29 | 32 | 61 | BELUM CUKUP | 8 | 190/67 | -2.57 | 8 | -5.11 | -0.69 | 5.2 | -1.82 | – | – |
| 189 | `M155` Market Cycle Strategy | **42.9** | 40 | 33 | 49 | 15 | BELUM CUKUP | 21 | 734/289 | -1.05 | 21 | -2.79 | -0.47 | 3.9 | -0.59 | – | -0.84 |
| 190 | `M152` Spike & Ledge | **42.7** | 30 | 42 | 43 | 18 | BELUM CUKUP | 18 | 47/8 | -1.72 | 21 | -0.27 | -0.05 | 2.8 | -0.24 | – | -0.68 |
| 191 | `N27X36` Ichimoku atas awan → keluar se | **42.7** | 18 | 31 | 28 | 30 | BELUM CUKUP | 8 | 98/9 | -1.94 | 8 | -3.49 | -0.80 | 3.1 | -1.51 | – | – |
| 192 | `N22X14` BB pecah atas + RSI → keluar b | **42.7** | 17 | 26 | 31 | 39 | BELUM CUKUP | 8 | 122/11 | -2.87 | 8 | -4.62 | -0.94 | 2.9 | -1.18 | – | – |
| 193 | `N54X16` Supertrend + RSI>50 → keluar b | **42.5** | 14 | 30 | 24 | 70 | BELUM CUKUP | 8 | 119/5 | -2.59 | 8 | -4.79 | -0.60 | 4.8 | -1.67 | – | – |
| 194 | `M130` 多方炮 (dua lilin hijau mengapit  | **42.4** | 15 | 22 | 35 | 15 | BELUM CUKUP | 7 | 10/3 | -3.80 | 19 | -3.57 | -0.58 | 3.2 | -0.24 | – | -0.21 |
| 195 | `M140` 猎豹出击 (Serangan Cheetah) | **42.1** | 26 | 30 | 35 | 15 | BELUM CUKUP | 11 | 42/12 | -1.47 | 21 | -5.16 | -0.77 | 3.4 | -1.10 | – | -1.26 |
| 196 | `M119` 180 Bullish (Cooper) | **42.0** | 34 | 33 | 48 | 15 | BELUM CUKUP | 19 | 151/66 | -1.17 | 21 | -5.56 | -0.51 | 5.2 | -0.54 | – | -1.63 |
| 197 | `M67` Rayner Teo: Ujian Ketiga pada  | **42.0** | 29 | 32 | 40 | 15 | BELUM CUKUP | 14 | 29/19 | -2.88 | 21 | -4.66 | -0.42 | 6.3 | -0.84 | – | -4.08 |
| 198 | `M99` Three Line Break | **41.9** | 29 | 39 | 51 | 15 | BELUM CUKUP | 21 | 160/92 | -2.20 | 21 | -0.55 | -0.09 | 3.5 | -0.34 | – | -1.30 |
| 199 | `M19` Sneaky Pivot (proksi harian) | **41.9** | 25 | 42 | 50 | 20 | BELUM CUKUP | 20 | 420/237 | -2.00 | 21 | -0.26 | -0.03 | 3.5 | -0.44 | – | -6.63 |
| 200 | `M141` First Thrust (Landry) | **41.9** | 14 | 32 | 29 | 15 | BELUM CUKUP | 8 | 26/11 | -3.04 | 21 | -5.31 | -0.78 | 3.4 | -1.62 | – | -2.88 |
| 201 | `M66` IBD Undur Pertama ke Purata 50 | **41.8** | 36 | 31 | 50 | 15 | BELUM CUKUP | 21 | 249/139 | -1.30 | 21 | -4.77 | -0.41 | 6.6 | -0.45 | – | -1.13 |
| 202 | `M156` Single Penetration (DiNapoli) | **41.8** | 36 | 32 | 48 | 15 | BELUM CUKUP | 21 | 240/154 | -1.05 | 21 | -4.17 | -0.33 | 6.4 | -0.72 | – | -2.44 |
| 203 | `N47X36` NR7 + EMA9>EMA21 → keluar sele | **41.5** | 8 | 27 | 24 | 30 | BELUM CUKUP | 7 | 155/20 | -2.04 | 8 | -8.59 | -1.00 | 5.5 | -2.12 | – | – |
| 204 | `M135` 3rd Watch | **41.4** | 14 | 31 | 33 | 15 | BELUM CUKUP | 9 | 15/3 | -4.17 | 21 | -5.15 | -0.65 | 3.9 | -0.83 | – | -4.31 |
| 205 | `M125` 2-Bar Breakout | **41.3** | 32 | 33 | 48 | 15 | BELUM CUKUP | 21 | 1107/425 | -1.55 | 21 | -3.30 | -0.49 | 3.4 | -0.66 | – | -0.29 |
| 206 | `N29X36` PSAR naik + tutup>MA50 → kelua | **40.9** | 10 | 19 | 30 | 30 | BELUM CUKUP | 8 | 148/48 | -2.37 | 8 | -9.11 | -0.94 | 8.0 | -1.85 | – | – |
| 207 | `M55` Guppy GMMA | **40.7** | 31 | 29 | 50 | 15 | BELUM CUKUP | 21 | 219/128 | -1.51 | 21 | -6.30 | -0.72 | 4.7 | -0.41 | – | -1.14 |
| 208 | `M126` Hidden Smash Day (beli, Larry  | **40.5** | 13 | 30 | 34 | 15 | BELUM CUKUP | 10 | 19/11 | -4.06 | 20 | -5.52 | -0.75 | 4.3 | -0.99 | – | -1.58 |
| 209 | `M147` Improved Three-Bar Pullback | **40.4** | 21 | 32 | 34 | 26 | BELUM CUKUP | 15 | 97/34 | -3.69 | 21 | -3.83 | -0.45 | 4.5 | -1.75 | – | -1.17 |
| 210 | `M11` NR7 Breakout + Volume | **40.2** | 30 | 26 | 45 | 15 | BELUM CUKUP | 19 | 117/85 | -0.92 | 21 | -8.90 | -0.71 | 7.4 | -0.91 | – | -0.87 |
| 211 | `M29` EMA3 + RSI75 + Stokastik | **40.1** | 24 | 30 | 40 | 15 | BELUM CUKUP | 16 | 37/28 | -2.41 | 21 | -8.45 | -0.67 | 7.3 | -0.96 | – | -5.74 |
| 212 | `M95` Nisbah Kebaharuan High 52 Ming | **40.0** | 24 | 32 | 48 | 15 | BELUM CUKUP | 19 | 124/63 | -1.77 | 21 | -5.88 | -0.69 | 4.9 | -0.47 | – | -1.12 |
| 213 | `M57` Landry Trend Knockout (TKO) | **39.6** | 26 | 32 | 42 | 15 | BELUM CUKUP | 21 | 169/113 | -2.11 | 21 | -4.75 | -0.56 | 4.0 | -1.46 | – | -4.00 |
| 214 | `M59` Anjakan Julat RSI | **39.3** | 17 | 26 | 43 | 15 | BELUM CUKUP | 14 | 36/18 | -4.80 | 21 | -3.05 | -0.38 | 4.2 | -0.46 | – | -1.80 |
| 215 | `M82` Arthur Hill Rotasi Sasaran 10% | **39.1** | 34 | 18 | 51 | 15 | BELUM CUKUP | 21 | 580/224 | -0.81 | 21 | -6.94 | -0.44 | 9.1 | -0.31 | – | -1.11 |
| 216 | `M161` EMA 10/21 + Supertrend (10,3) | **39.0** | 36 | 16 | 52 | 15 | BELUM CUKUP | 21 | 473/219 | -0.57 | 21 | -10.47 | -0.75 | 9.1 | -0.22 | – | -0.45 |
| 217 | `M101` Bulkowski: Tiga lembah menaik | **37.7** | 17 | 20 | 46 | 15 | BELUM CUKUP | 16 | 45/21 | -3.49 | 21 | -7.96 | -0.62 | 7.1 | -0.27 | – | -0.78 |
| 218 | `M123` CCI Correction (Lambert, Chart | **36.9** | 20 | 28 | 34 | 15 | BELUM CUKUP | 21 | 184/163 | -1.60 | 21 | -9.99 | -0.93 | 6.6 | -2.29 | – | -4.46 |
| 219 | `M154` HOLP (High of Low Period) | **36.8** | 13 | 21 | 42 | 15 | BELUM CUKUP | 16 | 87/33 | -2.63 | 21 | -9.44 | -0.73 | 7.1 | -0.83 | – | -3.89 |
| 220 | `M79` Radge: 20% Flipper | **36.6** | 16 | 27 | 44 | 15 | BELUM CUKUP | 21 | 382/89 | -2.57 | 21 | -6.33 | -0.64 | 5.4 | -1.14 | – | -1.84 |
| 221 | `M09` Volumatic VIDYA Pivot Retest | **35.9** | 5 | 18 | 29 | 15 | BELUM CUKUP | 12 | 30/16 | -4.48 | 21 | -11.95 | -1.00 | 6.3 | -1.96 | – | -10.13 |
| 222 | `M47` Holy Grail Raschke | **35.8** | 8 | 19 | 30 | 15 | BELUM CUKUP | 14 | 31/25 | -3.01 | 21 | -9.17 | -0.89 | 6.2 | -2.14 | – | -21.05 |
| 223 | `M76` Undercut & Rally pada Low Pent | **35.3** | 12 | 24 | 40 | 15 | BELUM CUKUP | 20 | 76/48 | -1.87 | 21 | -9.43 | -0.86 | 6.5 | -1.27 | – | -4.94 |
| 224 | `M122` Moving Momentum (ChartSchool) | **34.8** | 15 | 20 | 35 | 15 | BELUM CUKUP | 21 | 109/59 | -3.56 | 21 | -10.29 | -1.00 | 5.6 | -1.98 | – | -5.56 |
| 225 | `M81` Bensdorp Long Trend High Momen | **34.3** | 3 | 11 | 44 | 15 | BELUM CUKUP | 13 | 431/149 | -3.59 | 21 | -16.92 | -0.73 | 13.8 | -0.99 | – | -3.19 |
| 226 | `M90` Pring KST | **31.8** | 6 | 15 | 43 | 15 | BELUM CUKUP | 20 | 85/42 | -3.24 | 21 | -13.28 | -0.72 | 11.2 | -0.93 | – | -4.20 |

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

