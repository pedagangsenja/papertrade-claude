# Skor Kaedah 0–100 (pangkat maklumat, BUKAN keputusan)

> **Status keputusan (kad skor, harga 2026-11-11):** TERBUKTI 0 · CALON 0 · BELUM CUKUP 223 · GAGAL 0 · NEGATIF 0. Rejim QQQ OFF sejak 2026-10-16. Hanya **TERBUKTI** layak untuk wang sebenar (`laporan/KAD_SKOR.md`); nombor dalam laporan ini BUKAN keputusan dan tidak boleh dibaca sebagai pangkat untuk wang sebenar.

Dijana 2026-11-12 oleh `standard/skor_kaedah.py` (Actions `analisis.yml`, selepas kad skor). Harga pada tutup 2026-11-11; 223 kaedah; 19 hari beli langsung (rejim ON 1, OFF 18). Pradaftar 2026-11-09: `standard/SPEC_SKOR_KAEDAH.md` (berat dan sauh dikunci `ujian/test_skor_kaedah.py::TestKunci`). Rekod analisis sahaja: tiada order, tiada wang sebenar.

## Cara membaca

- **Skor** = min geometri berberat empat tiang (Untung 35 · Tahan 30 · Bukti 25 · Konsisten 10), dikecut ke 50 mengikut data: berat data = hari beli ÷ (hari beli + 20). Kaedah dengan 2 hari beli tidak boleh menjauhi 50. 100 = unggul semua segi; 50 = neutral/tiada bukti; < 50 = lebih buruk daripada neutral.
- **Siling** ikut kad skor: NEGATIF ≤ 20, GANTUNG/BERSARA ≤ 30, GAGAL ≤ 40. Tanda ⌈ = siling terpakai.
- **Satu-satunya status yang membenarkan wang sebenar ialah TERBUKTI dalam `laporan/KAD_SKOR.md`.** Skor tinggi dengan status BELUM CUKUP bermaksud "paling menjanjikan setakat ini", bukan "selamat".
- Deflasi ujian berganda (López de Prado): sauh t Bukti C1 = maks(2.0, E[maks 223 normal]) = 2.80.
- **Semakan kebolehramalan:** belum ada snapshot skor ≥ 7 hari lalu (sejarah bermula 2026-11-11); skor dipercayai sebagai pangkat hanya selepas 8–12 minggu semakan positif.
- Metrik T4 (A2, B1, B2, D1) dikira atas lorong T4 L1 **dipotong pada sesi LANGSUNG pertama** kaedah itu (Mxx 2026-10-16, Nxx/GB 2026-11-03) dan diasas semula; sesi isian bina semula tidak dikira (pindaan 9 Nov 2026 (a)). Lajur "T4 sesi/pul" di bawah ialah potongan itu, bukan lorong penuh `T4_KAEDAH.md`.

## Semua kaedah, susun ikut Skor

| # | Kaedah | Skor | Untung | Tahan | Bukti | Konsisten | Status kad | Hari beli | Posisi/tutup | Jangkaan % | T4 sesi | T4 pul % | T4 pul/|MDD| | Ulcer | t buku | Lift | WFE |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `M146` 3-Bar Momentum Pattern | **65.0** | 92 | 86 | 67 | 85 | BELUM CUKUP | 17 | 77/30 | +1.70 | 19 | +6.71 | +1.09 | 2.2 | +2.05 | – | 3.24 |
| 2 | `M33` Supertrend + SMA10 | **64.9** | 91 | 82 | 65 | 85 | BELUM CUKUP | 19 | 218/40 | +1.88 | 19 | +8.89 | +3.32 | 1.4 | +1.71 | – | 5.32 |
| 3 | `M118` Expansion Pivot (Cooper) | **63.6** | 84 | 85 | 60 | 85 | BELUM CUKUP | 19 | 84/20 | +1.13 | 19 | +10.30 | +3.81 | 0.9 | +1.44 | – | 3.50 |
| 4 | `M133` Bull Hook (Crabel) | **62.5** | 95 | 88 | 60 | 85 | BELUM CUKUP | 13 | 49/23 | +1.80 | 19 | +7.95 | +1.92 | 1.5 | +1.43 | – | 13.63 |
| 5 | `M74` Lulus Baharu Trend Template Mi | **61.4** | 77 | 80 | 58 | 85 | BELUM CUKUP | 19 | 90/53 | +0.60 | 19 | +4.27 | +1.02 | 2.2 | +0.74 | – | 1.21 |
| 6 | `M142` Pecahan volum dari dasar (底部放量 | **61.2** | 88 | 94 | 50 | 85 | BELUM CUKUP | 14 | 45/5 | +3.31 | 17 | +5.31 | +1.11 | 1.8 | +1.03 | – | 1.50 |
| 7 | `M151` Outside Bar Failure | **60.9** | 74 | 83 | 58 | 85 | BELUM CUKUP | 18 | 96/48 | +0.19 | 19 | +7.47 | +6.14 | 0.5 | +0.77 | – | 1.37 |
| 8 | `M25` VWAP Wave (proksi harian) | **60.4** | 75 | 79 | 60 | 80 | BELUM CUKUP | 17 | 173/87 | +0.48 | 19 | +5.74 | +0.99 | 3.0 | +0.89 | – | 4.94 |
| 9 | `M124` 'Last' Stochastic Technique (C | **59.9** | 70 | 76 | 60 | 85 | BELUM CUKUP | 19 | 380/170 | +0.26 | 19 | +5.84 | +1.27 | 2.3 | +0.70 | – | 1.20 |
| 10 | `M10` EMA3 + CCI + MACD | **59.9** | 76 | 71 | 58 | 85 | BELUM CUKUP | 19 | 113/50 | +0.55 | 19 | +10.29 | +1.96 | 2.0 | +0.77 | – | 1.89 |
| 11 | `M93` Bollinger Kaedah II: %b + MFI | **59.6** | 82 | 60 | 63 | 78 | BELUM CUKUP | 19 | 258/75 | +1.57 | 19 | +1.68 | +0.27 | 2.6 | +1.23 | – | 1.39 |
| 12 | `M111` Sistem Volatiliti Wilder | **59.5** | 75 | 66 | 62 | 85 | BELUM CUKUP | 19 | 253/78 | +0.83 | 19 | +4.65 | +0.69 | 3.5 | +1.10 | – | 2.05 |
| 13 | `M160` Measured Move Up | **58.8** | 63 | 79 | 62 | 85 | BELUM CUKUP | 17 | 107/47 | -0.15 | 19 | +5.13 | +1.10 | 2.1 | +1.30 | – | 9.50 |
| 14 | `M23` Breitstein Kapitulasi + Kesina | **58.3** | 66 | 68 | 62 | 85 | BELUM CUKUP | 19 | 121/74 | +0.05 | 19 | +1.71 | +0.33 | 2.1 | +1.15 | – | 4.19 |
| 15 | `M100` Bulkowski Segi Empat & Segi Ti | **58.1** | 69 | 78 | 56 | 85 | BELUM CUKUP | 14 | 58/40 | +0.52 | 19 | +4.38 | +1.00 | 2.0 | +0.83 | – | 3.70 |
| 16 | `M13` Garis Trend Action/Safety Line | **58.0** | 69 | 73 | 56 | 68 | BELUM CUKUP | 19 | 711/426 | -0.08 | 19 | +9.99 | +2.80 | 1.2 | +0.26 | – | 0.42 |
| 17 | `M145` Yum-Yum Continuation | **57.9** | 68 | 73 | 57 | 67 | BELUM CUKUP | 19 | 300/62 | +0.42 | 19 | +5.27 | +2.42 | 1.3 | +0.56 | – | 0.40 |
| 18 | `M137` Livermore System | **57.6** | 63 | 71 | 56 | 84 | BELUM CUKUP | 19 | 166/57 | -0.16 | 19 | +6.51 | +1.10 | 2.3 | +0.54 | – | 0.97 |
| 19 | `M105` Supertrend tulen | **57.1** | 71 | 58 | 63 | 68 | BELUM CUKUP | 19 | 355/97 | +0.90 | 19 | +1.80 | +0.25 | 3.4 | +1.06 | – | 2.17 |
| 20 | `M89` Chande 65sma-3cc | **57.0** | 64 | 63 | 59 | 85 | BELUM CUKUP | 19 | 165/80 | +0.11 | 19 | +2.68 | +0.49 | 2.6 | +0.73 | – | 1.70 |
| 21 | `M91` Stochastic Pop (Bernstein/Stec | **56.9** | 72 | 66 | 55 | 85 | BELUM CUKUP | 14 | 37/16 | +0.18 | 19 | +9.30 | +1.19 | 2.8 | +0.98 | – | 3.51 |
| 22 | `M48` Cooper 1-2-3-4 | **56.8** | 75 | 59 | 54 | 85 | BELUM CUKUP | 16 | 52/16 | +0.62 | 19 | +10.99 | +2.02 | 2.0 | +0.90 | – | 2.30 |
| 23 | `M30` BB Free Bar + Himpitan 50/2.5 | **56.4** | 71 | 58 | 62 | 62 | BELUM CUKUP | 18 | 226/70 | +0.70 | 19 | +3.44 | +0.45 | 4.7 | +1.08 | – | 1.75 |
| 24 | `M158` Doubly Adaptive Profit Targets | **56.3** | 76 | 56 | 63 | 45 | BELUM CUKUP | 19 | 349/127 | +1.24 | 19 | -0.17 | -0.03 | 2.7 | +1.11 | – | 2.60 |
| 25 | `M77` Undercut & Rally pada Purata B | **56.1** | 68 | 76 | 49 | 55 | BELUM CUKUP | 17 | 54/33 | +0.20 | 19 | +2.36 | +0.74 | 1.6 | -0.08 | – | -0.13 |
| 26 | `M70` Pecahan Hari Dalam | **56.1** | 67 | 75 | 56 | 38 | BELUM CUKUP | 19 | 441/332 | -0.05 | 19 | +3.65 | +0.75 | 2.3 | +0.30 | – | 0.75 |
| 27 | `M159` Heikin-Ashi Trend | **56.1** | 64 | 72 | 53 | 55 | BELUM CUKUP | 19 | 1570/1209 | -0.15 | 19 | +7.29 | +1.19 | 3.6 | -0.06 | – | -0.31 |
| 28 | `M92` CCI-50 | **55.7** | 67 | 58 | 58 | 66 | BELUM CUKUP | 19 | 527/313 | +0.50 | 19 | +0.86 | +0.15 | 2.6 | +0.51 | – | 0.82 |
| 29 | `M46` Jurang Naik Boleh Beli (Buyabl | **55.6** | 65 | 73 | 51 | 82 | BELUM CUKUP | 12 | 35/17 | -0.03 | 19 | +2.82 | +0.57 | 1.6 | +0.56 | – | 0.91 |
| 30 | `M15` Break & Retest + Henti ATR | **55.2** | 73 | 54 | 60 | 45 | BELUM CUKUP | 19 | 291/155 | +1.04 | 19 | -1.67 | -0.22 | 3.5 | +0.79 | – | 1.36 |
| 31 | `M02` MACD + SMA200 | **55.1** | 65 | 66 | 52 | 55 | BELUM CUKUP | 19 | 117/60 | -0.19 | 19 | +11.76 | +2.66 | 1.7 | -0.03 | – | -0.15 |
| 32 | `N53X36` Supertrend + ADX>25 → keluar s | **54.8** | 88 | 69 | 54 | 70 | BELUM CUKUP | 6 | 106/19 | +1.82 | 6 | +2.16 | +0.54 | 2.3 | +1.39 | – | – |
| 33 | `M80` Radge Saluran Purata Bergerak  | **54.8** | 74 | 50 | 62 | 45 | BELUM CUKUP | 19 | 273/56 | +1.34 | 19 | -1.46 | -0.20 | 3.9 | +1.23 | – | 1.34 |
| 34 | `N75X17` RSI14 < 40 tanpa penapis → kel | **54.7** | 80 | 87 | 46 | 70 | BELUM CUKUP | 6 | 267/110 | +1.27 | 6 | +3.64 | +0.91 | 2.2 | -0.21 | – | – |
| 35 | `M05` MACD Divergence + Pengesahan | **54.6** | 63 | 74 | 47 | 62 | BELUM CUKUP | 14 | 40/12 | +0.12 | 19 | +3.87 | +1.14 | 1.3 | +0.15 | – | 0.23 |
| 36 | `N40X36` OBV tinggi baharu + MA50 → kel | **54.5** | 91 | 69 | 47 | 70 | BELUM CUKUP | 6 | 47/7 | +2.82 | 6 | +2.08 | +0.43 | 2.7 | +1.01 | – | – |
| 37 | `M139` 均线首次粘合向上发散 (MA berhimpun kali  | **54.5** | 58 | 61 | 51 | 85 | BELUM CUKUP | 19 | 82/17 | -0.24 | 19 | +3.77 | +0.75 | 2.2 | +0.38 | – | 1.17 |
| 38 | `N64X36` Episodic pivot → keluar selepa | **54.2** | 88 | 81 | 38 | 70 | BELUM CUKUP | 6 | 46/4 | +2.25 | 6 | +2.08 | +0.52 | 2.2 | +0.15 | – | – |
| 39 | `N40X16` OBV tinggi baharu + MA50 → kel | **54.1** | 90 | 62 | 50 | 70 | BELUM CUKUP | 6 | 61/21 | +2.01 | 6 | +1.14 | +0.21 | 2.8 | +0.89 | – | – |
| 40 | `M117` Landry Pullback (high 2 bulan) | **54.0** | 75 | 49 | 58 | 45 | BELUM CUKUP | 16 | 132/17 | +1.49 | 19 | -4.41 | -0.56 | 3.8 | +1.29 | – | 1.28 |
| 41 | `M129` Wick Play | **53.9** | 67 | 61 | 49 | 85 | BELUM CUKUP | 10 | 26/10 | +0.06 | 19 | +5.91 | +2.10 | 1.0 | +0.58 | – | 2.23 |
| 42 | `N124X15` Episodic pivot gap 8-10% → eko | **53.8** | 91 | 80 | 34 | 70 | BELUM CUKUP | 6 | 39/0 | +3.79 | 6 | +2.15 | +0.33 | 3.2 | +0.26 | – | – |
| 43 | `N45X16` Undur EMA21 cerun positif → ke | **53.8** | 64 | 83 | 52 | 70 | BELUM CUKUP | 6 | 117/44 | +0.15 | 6 | +6.47 | +8.25 | 0.4 | +0.87 | – | – |
| 44 | `N64X17` Episodic pivot → keluar bila a | **53.5** | 80 | 76 | 40 | 70 | BELUM CUKUP | 6 | 46/10 | +1.51 | 6 | +1.90 | +0.47 | 2.1 | +0.02 | – | – |
| 45 | `N75X14` RSI14 < 40 tanpa penapis → kel | **53.5** | 86 | 69 | 40 | 70 | BELUM CUKUP | 6 | 188/21 | +2.36 | 6 | -0.67 | -0.12 | 3.5 | -0.26 | – | – |
| 46 | `N64X16` Episodic pivot → keluar bila s | **53.3** | 84 | 70 | 38 | 70 | BELUM CUKUP | 6 | 46/5 | +2.00 | 6 | +0.02 | +0.01 | 2.1 | +0.09 | – | – |
| 47 | `N75X13` RSI14 < 40 tanpa penapis → kel | **53.3** | 88 | 74 | 34 | 70 | BELUM CUKUP | 6 | 124/1 | +2.24 | 6 | +0.25 | +0.07 | 2.1 | -0.04 | – | – |
| 48 | `M88` O'Neil Shakeout +3 | **53.3** | 58 | 57 | 52 | 73 | BELUM CUKUP | 15 | 70/29 | -0.23 | 19 | +3.41 | +0.41 | 3.7 | +0.37 | – | 0.61 |
| 49 | `N75X15` RSI14 < 40 tanpa penapis → eko | **53.0** | 88 | 74 | 31 | 70 | BELUM CUKUP | 6 | 124/0 | +2.32 | 6 | +0.25 | +0.07 | 2.1 | -0.02 | – | – |
| 50 | `N64X14` Episodic pivot → keluar bila r | **53.0** | 84 | 72 | 35 | 70 | BELUM CUKUP | 6 | 46/1 | +2.14 | 6 | +0.02 | +0.01 | 2.1 | +0.10 | – | – |
| 51 | `M132` Ascending Scallop (Bulkowski) | **52.9** | 46 | 67 | 52 | 85 | BELUM CUKUP | 17 | 94/36 | -1.08 | 19 | +3.83 | +1.03 | 2.2 | +0.25 | – | 1.83 |
| 52 | `N42X14` Lonjakan volum 2x → keluar bil | **52.8** | 87 | 60 | 38 | 70 | BELUM CUKUP | 6 | 159/9 | +2.19 | 6 | -0.17 | -0.02 | 5.8 | -0.12 | – | – |
| 53 | `M35` Pocket Pivot Morales & Kacher | **52.8** | 63 | 50 | 58 | 45 | BELUM CUKUP | 19 | 307/207 | +0.17 | 19 | -1.17 | -0.13 | 4.9 | +0.53 | – | 2.65 |
| 54 | `N25X36` Supertrend + EMA + ADX>23 → ke | **52.4** | 69 | 64 | 44 | 70 | BELUM CUKUP | 6 | 108/16 | +0.58 | 6 | +1.05 | +0.24 | 2.6 | +0.34 | – | – |
| 55 | `N22X36` BB pecah atas + RSI → keluar s | **52.3** | 56 | 69 | 53 | 70 | BELUM CUKUP | 6 | 107/23 | -0.16 | 6 | +2.35 | +0.62 | 2.1 | +1.27 | – | – |
| 56 | `N42X15` Lonjakan volum 2x → ekori Chan | **52.3** | 90 | 62 | 30 | 70 | BELUM CUKUP | 6 | 148/0 | +2.33 | 6 | +1.53 | +0.13 | 5.9 | -0.14 | – | – |
| 57 | `N124X36` Episodic pivot gap 8-10% → kel | **52.2** | 84 | 57 | 41 | 52 | BELUM CUKUP | 6 | 39/10 | +1.93 | 6 | -2.04 | -0.41 | 3.1 | +0.13 | – | – |
| 58 | `N68X36` Bullish engulfing + EMA21 → ke | **52.2** | 58 | 76 | 43 | 70 | BELUM CUKUP | 6 | 50/7 | -0.02 | 6 | +2.82 | +1.31 | 1.3 | +0.50 | – | – |
| 59 | `M04` BB Squeeze Breakout | **52.2** | 54 | 50 | 57 | 70 | BELUM CUKUP | 18 | 151/52 | -0.45 | 19 | +3.22 | +0.40 | 4.0 | +0.65 | – | 1.03 |
| 60 | `N42X17` Lonjakan volum 2x → keluar bil | **52.1** | 74 | 56 | 44 | 70 | BELUM CUKUP | 6 | 172/44 | +1.29 | 6 | -0.88 | -0.09 | 5.4 | -0.13 | – | – |
| 61 | `N73X13` Tutup bawah jalur bawah BB(20, | **52.1** | 84 | 66 | 34 | 47 | BELUM CUKUP | 6 | 136/1 | +1.95 | 6 | -0.66 | -0.10 | 3.1 | +0.00 | – | – |
| 62 | `N36X16` Pocket pivot → keluar bila sup | **52.1** | 61 | 68 | 44 | 70 | BELUM CUKUP | 6 | 139/47 | -0.01 | 6 | +4.17 | +2.84 | 0.7 | -0.12 | – | – |
| 63 | `N45X36` Undur EMA21 cerun positif → ke | **52.1** | 55 | 78 | 44 | 70 | BELUM CUKUP | 6 | 97/27 | -0.10 | 6 | +2.07 | +1.00 | 1.2 | +0.04 | – | – |
| 64 | `M131` Ross Hook (Joe Ross) | **52.1** | 54 | 54 | 58 | 45 | BELUM CUKUP | 19 | 257/106 | -0.23 | 19 | -0.02 | -0.00 | 3.1 | +0.52 | – | 1.09 |
| 65 | `M153` Range Leader | **52.1** | 59 | 48 | 60 | 45 | BELUM CUKUP | 19 | 1242/1026 | +0.28 | 19 | -1.20 | -0.12 | 6.1 | +0.79 | – | 4.26 |
| 66 | `M18` EMA9/21 Pullback | **52.0** | 61 | 46 | 56 | 53 | BELUM CUKUP | 19 | 348/227 | +0.30 | 19 | -3.10 | -0.51 | 4.0 | +0.33 | – | 1.05 |
| 67 | `M39` Radge Pecahan Bollinger 100 ha | **51.8** | 45 | 65 | 52 | 62 | BELUM CUKUP | 19 | 233/49 | -1.28 | 19 | +7.60 | +3.17 | 1.2 | +0.11 | – | 0.23 |
| 68 | `N36X36` Pocket pivot → keluar selepas  | **51.7** | 64 | 61 | 43 | 70 | BELUM CUKUP | 6 | 135/49 | +0.11 | 6 | +3.83 | +0.73 | 2.6 | -0.29 | – | – |
| 69 | `M106` DMI Wilder | **51.6** | 58 | 49 | 57 | 45 | BELUM CUKUP | 17 | 116/59 | +0.18 | 19 | -1.12 | -0.25 | 2.6 | +0.62 | – | 1.00 |
| 70 | `M150` Trend Bar Failure (Brooks) | **51.6** | 62 | 52 | 52 | 36 | BELUM CUKUP | 18 | 99/39 | +0.56 | 19 | -2.71 | -0.49 | 2.5 | +0.25 | – | 0.71 |
| 71 | `M37` Weinstein Peringkat 2 | **51.5** | 72 | 91 | 32 | 60 | BELUM CUKUP | 3 | 7/0 | +0.89 | 13 | +0.76 | +1.51 | 0.2 | +0.24 | – | 0.18 |
| 72 | `N19X13` Bawah jalur BB + RSI<30 → kelu | **51.5** | 86 | 66 | 35 | 30 | BELUM CUKUP | 5 | 101/0 | +4.61 | 6 | -1.39 | -0.42 | 2.6 | +0.51 | – | – |
| 73 | `N28X36` ADX>25 + DI+ > DI- → keluar se | **51.5** | 66 | 51 | 48 | 70 | BELUM CUKUP | 6 | 222/106 | +0.88 | 6 | -1.30 | -0.21 | 4.0 | +0.04 | – | – |
| 74 | `N37X36` Gap and go → keluar selepas DU | **51.5** | 59 | 70 | 38 | 70 | BELUM CUKUP | 6 | 76/16 | +0.12 | 6 | +2.95 | +0.80 | 2.1 | -0.36 | – | – |
| 75 | `M01` Bollinger Band + RSI | **51.5** | 82 | 55 | 47 | 15 | BELUM CUKUP | 19 | 112/20 | +3.05 | 19 | -3.26 | -0.30 | 4.3 | -0.19 | – | -0.87 |
| 76 | `N42X36` Lonjakan volum 2x → keluar sel | **51.4** | 67 | 52 | 44 | 70 | BELUM CUKUP | 6 | 171/78 | +0.93 | 6 | -1.07 | -0.14 | 4.3 | -0.27 | – | – |
| 77 | `N37X17` Gap and go → keluar bila adx14 | **51.3** | 55 | 70 | 39 | 70 | BELUM CUKUP | 6 | 76/24 | -0.15 | 6 | +3.32 | +0.90 | 1.9 | -0.45 | – | – |
| 78 | `M03` BB Break + Divergence RSI | **51.3** | 51 | 55 | 56 | 45 | BELUM CUKUP | 19 | 395/311 | -0.06 | 19 | +0.28 | +0.04 | 2.7 | +0.31 | – | 1.22 |
| 79 | `N48X36` Inside day pecah → keluar sele | **51.2** | 64 | 51 | 45 | 70 | BELUM CUKUP | 6 | 256/158 | +1.04 | 6 | -2.68 | -0.32 | 6.1 | -0.32 | – | – |
| 80 | `N43X36` Undur EMA8 + penapis MA50 → ke | **51.1** | 60 | 59 | 40 | 70 | BELUM CUKUP | 6 | 136/21 | +0.26 | 6 | +1.08 | +0.28 | 2.2 | -0.27 | – | – |
| 81 | `M104` High Tight Flag / Power Play | **51.0** | 78 | 90 | 51 | 65 | BELUM CUKUP | 1 | 1/0 | +19.60 | 4 | +1.98 | +10.00 | 0.0 | +4.30 | – | 27.03 |
| 82 | `M21` Marius 3 Persediaan (Pecahan+J | **50.9** | 59 | 58 | 43 | 64 | BELUM CUKUP | 5 | 5/2 | -0.06 | 11 | +0.01 | +0.01 | 1.1 | +0.98 | – | 1.55 |
| 83 | `N42X16` Lonjakan volum 2x → keluar bil | **50.9** | 64 | 48 | 44 | 70 | BELUM CUKUP | 6 | 175/76 | +0.84 | 6 | -2.40 | -0.37 | 4.1 | -0.26 | – | – |
| 84 | `N28X14` ADX>25 + DI+ > DI- → keluar bi | **50.7** | 58 | 61 | 35 | 70 | BELUM CUKUP | 6 | 132/8 | +0.08 | 6 | +1.20 | +0.19 | 3.5 | -0.46 | – | – |
| 85 | `N41X16` CMF20>0 + tutup>EMA20 → keluar | **50.6** | 43 | 74 | 42 | 70 | BELUM CUKUP | 6 | 207/107 | -0.88 | 6 | +2.01 | +0.94 | 1.2 | -0.66 | – | – |
| 86 | `N41X36` CMF20>0 + tutup>EMA20 → keluar | **50.6** | 52 | 55 | 45 | 70 | BELUM CUKUP | 6 | 182/91 | -0.35 | 6 | +0.94 | +0.19 | 2.6 | -0.29 | – | – |
| 87 | `N08X36` tutup>EMA20 tidak terlalu jauh | **50.5** | 54 | 54 | 44 | 70 | BELUM CUKUP | 6 | 270/145 | -0.23 | 6 | +0.43 | +0.08 | 3.0 | -0.48 | – | – |
| 88 | `N09X36` Undur EMA10 + penapis EMA50 →  | **50.5** | 55 | 54 | 42 | 70 | BELUM CUKUP | 6 | 146/36 | -0.01 | 6 | +0.14 | +0.03 | 2.1 | -0.23 | – | – |
| 89 | `N68X16` Bullish engulfing + EMA21 → ke | **50.5** | 44 | 73 | 39 | 70 | BELUM CUKUP | 6 | 50/10 | -0.77 | 6 | +2.71 | +1.31 | 1.5 | -0.07 | – | – |
| 90 | `N76X36` Tutup > MA50 (penapis trend tu | **50.5** | 63 | 45 | 43 | 70 | BELUM CUKUP | 6 | 144/35 | +0.70 | 6 | -2.80 | -0.51 | 3.7 | -0.15 | – | – |
| 91 | `M08` SMA20 + SMA200 | **50.5** | 54 | 46 | 53 | 55 | BELUM CUKUP | 17 | 181/92 | -0.10 | 19 | -1.50 | -0.28 | 3.8 | -0.01 | – | -0.02 |
| 92 | `N24X36` Supertrend(10,3) + ADX>20 → ke | **50.4** | 66 | 41 | 44 | 62 | BELUM CUKUP | 6 | 121/31 | +0.75 | 6 | -1.82 | -0.40 | 3.0 | +0.08 | – | – |
| 93 | `N25X17` Supertrend + EMA + ADX>23 → ke | **50.4** | 52 | 63 | 36 | 70 | BELUM CUKUP | 6 | 95/4 | -0.21 | 6 | +0.72 | +0.15 | 2.7 | -0.19 | – | – |
| 94 | `N37X16` Gap and go → keluar bila super | **50.4** | 54 | 58 | 37 | 70 | BELUM CUKUP | 6 | 76/16 | -0.00 | 6 | +0.90 | +0.24 | 2.0 | -0.47 | – | – |
| 95 | `N35X36` Pecah 52 minggu tinggi → kelua | **50.3** | 47 | 79 | 31 | 70 | BELUM CUKUP | 5 | 42/1 | -0.48 | 6 | +1.80 | +1.00 | 1.0 | -0.33 | – | – |
| 96 | `M134` First Kiss After Daylight (Lan | **50.3** | 55 | 48 | 54 | 42 | BELUM CUKUP | 15 | 53/16 | -0.09 | 19 | -1.40 | -0.20 | 3.4 | +0.80 | – | 0.88 |
| 97 | `N50X17` Mampat + pecah volum 1.5x → ke | **50.2** | 63 | 56 | 32 | 70 | BELUM CUKUP | 3 | 12/2 | +0.14 | 6 | +0.88 | +0.10 | 4.7 | -0.19 | – | – |
| 98 | `N25X16` Supertrend + EMA + ADX>23 → ke | **50.2** | 52 | 62 | 34 | 70 | BELUM CUKUP | 6 | 99/2 | -0.17 | 6 | +0.39 | +0.08 | 2.7 | -0.18 | – | – |
| 99 | `N33X36` Donchian20 + penapis MA200 → k | **50.1** | 53 | 57 | 36 | 70 | BELUM CUKUP | 6 | 81/10 | -0.16 | 6 | -0.57 | -0.16 | 2.0 | -0.39 | – | – |
| 100 | `M143` 장대양봉 이후 눌림목 / 5일선 매매 (Undur ke | **50.0** | 55 | 67 | 30 | 55 | BELUM CUKUP | 11 | 21/1 | +0.16 | 18 | +0.36 | +0.12 | 1.5 | -0.71 | – | -7.64 |
| 101 | `M148` Natural Number Method | **50.0** | 41 | 66 | 45 | 55 | BELUM CUKUP | 19 | 210/129 | -1.47 | 19 | +3.77 | +0.76 | 2.2 | -0.98 | – | -3.22 |
| 102 | `M51` O'Neil Cawan & Pemegang | **50.0** | 52 | 57 | 37 | 59 | BELUM CUKUP | 2 | 3/0 | -0.46 | 9 | -0.08 | -0.08 | 0.5 | +1.02 | – | 3.31 |
| 103 | `N56X17` RSI>50 + ADX>20 → keluar bila  | **50.0** | 51 | 58 | 35 | 70 | BELUM CUKUP | 6 | 110/11 | -0.12 | 6 | +0.25 | +0.05 | 2.7 | -0.61 | – | – |
| 104 | `N80X36` Tinggi sepanjang masa → keluar | **50.0** | 56 | 55 | 37 | 53 | BELUM CUKUP | 5 | 32/1 | +0.20 | 6 | -0.77 | -0.23 | 1.8 | +0.39 | – | – |
| 105 | `M116` 2/20 EMA Breakout (Landry) | **49.9** | 53 | 42 | 58 | 45 | BELUM CUKUP | 19 | 539/353 | +0.06 | 19 | -1.27 | -0.10 | 7.1 | +0.44 | – | 1.66 |
| 106 | `N22X16` BB pecah atas + RSI → keluar b | **49.9** | 47 | 54 | 50 | 47 | BELUM CUKUP | 6 | 109/20 | -0.32 | 6 | -0.31 | -0.09 | 2.2 | +0.88 | – | – |
| 107 | `N28X16` ADX>25 + DI+ > DI- → keluar bi | **49.9** | 50 | 51 | 42 | 70 | BELUM CUKUP | 6 | 233/115 | -0.01 | 6 | -1.60 | -0.26 | 4.0 | -0.61 | – | – |
| 108 | `N65X14` Gap 4% + volum + hampir 52w →  | **49.9** | 61 | 56 | 28 | 68 | BELUM CUKUP | 5 | 28/1 | +0.58 | 6 | -1.14 | -0.27 | 2.5 | -0.61 | – | – |
| 109 | `N50X14` Mampat + pecah volum 1.5x → ke | **49.9** | 57 | 55 | 31 | 70 | BELUM CUKUP | 3 | 12/2 | -0.08 | 6 | -0.35 | -0.04 | 4.6 | -0.28 | – | – |
| 110 | `M31` Band Walk (BB 20/2) | **49.8** | 59 | 36 | 59 | 45 | BELUM CUKUP | 19 | 392/84 | +0.46 | 19 | -1.44 | -0.13 | 6.9 | +0.67 | – | 1.05 |
| 111 | `N37X14` Gap and go → keluar bila rsi14 | **49.8** | 53 | 54 | 34 | 70 | BELUM CUKUP | 6 | 75/5 | +0.14 | 6 | +0.03 | +0.01 | 2.1 | -0.47 | – | – |
| 112 | `N76X16` Tutup > MA50 (penapis trend tu | **49.8** | 44 | 59 | 40 | 70 | BELUM CUKUP | 6 | 216/105 | -0.58 | 6 | +0.49 | +0.14 | 1.9 | -0.93 | – | – |
| 113 | `N28X17` ADX>25 + DI+ > DI- → keluar bi | **49.7** | 57 | 60 | 27 | 70 | BELUM CUKUP | 6 | 85/0 | +0.04 | 6 | +0.69 | +0.10 | 3.9 | -0.58 | – | – |
| 114 | `N33X16` Donchian20 + penapis MA200 → k | **49.7** | 48 | 60 | 34 | 70 | BELUM CUKUP | 6 | 83/7 | -0.50 | 6 | +0.64 | +0.18 | 1.9 | -0.59 | – | – |
| 115 | `N08X16` tutup>EMA20 tidak terlalu jauh | **49.7** | 45 | 55 | 41 | 70 | BELUM CUKUP | 6 | 303/181 | -0.61 | 6 | +0.17 | +0.05 | 2.3 | -0.76 | – | – |
| 116 | `N24X17` Supertrend(10,3) + ADX>20 → ke | **49.7** | 47 | 61 | 33 | 70 | BELUM CUKUP | 6 | 101/6 | -0.36 | 6 | +0.47 | +0.13 | 2.0 | -0.61 | – | – |
| 117 | `M34` Carter TTM Squeeze | **49.6** | 54 | 44 | 52 | 42 | BELUM CUKUP | 18 | 102/46 | -0.24 | 19 | +1.64 | +0.23 | 3.7 | +0.16 | – | 0.52 |
| 118 | `N22X14` BB pecah atas + RSI → keluar b | **49.6** | 45 | 54 | 41 | 70 | BELUM CUKUP | 6 | 111/11 | -0.54 | 6 | +0.33 | +0.07 | 2.6 | +0.06 | – | – |
| 119 | `N74X16` MACD atas garis isyarat (keada | **49.6** | 48 | 48 | 42 | 70 | BELUM CUKUP | 6 | 320/180 | -0.21 | 6 | -1.72 | -0.23 | 5.1 | -0.61 | – | – |
| 120 | `N56X16` RSI>50 + ADX>20 → keluar bila  | **49.6** | 47 | 49 | 41 | 70 | BELUM CUKUP | 6 | 157/54 | -0.16 | 6 | -1.76 | -0.34 | 3.5 | -0.48 | – | – |
| 121 | `N65X36` Gap 4% + volum + hampir 52w →  | **49.6** | 62 | 55 | 26 | 65 | BELUM CUKUP | 5 | 28/0 | +0.64 | 6 | -1.42 | -0.34 | 2.6 | -0.59 | – | – |
| 122 | `N66X36` 52w tinggi + pengesahan 1% → k | **49.6** | 54 | 52 | 31 | 70 | BELUM CUKUP | 5 | 33/1 | +0.15 | 5 | -1.15 | -0.28 | 2.8 | -0.27 | – | – |
| 123 | `M107` Golden Cross SMA50/200 | **49.4** | 54 | 57 | 46 | 24 | BELUM CUKUP | 16 | 34/7 | -0.18 | 19 | +0.46 | +0.13 | 1.7 | +0.20 | – | 0.31 |
| 124 | `N36X14` Pocket pivot → keluar bila rsi | **49.2** | 54 | 40 | 38 | 70 | BELUM CUKUP | 6 | 133/17 | -0.03 | 6 | -1.34 | -0.20 | 3.9 | -0.40 | – | – |
| 125 | `M07` Qullamaggie Breakout | **49.2** | 26 | 64 | 27 | 15 | BELUM CUKUP | 1 | 1/1 | -2.53 | 19 | -0.25 | -0.21 | 0.7 | -0.22 | – | -1.12 |
| 126 | `N07X16` Tiga MA tersusun → keluar bila | **49.1** | 49 | 58 | 39 | 30 | BELUM CUKUP | 6 | 113/11 | -0.23 | 6 | -0.46 | -0.11 | 2.2 | -0.16 | – | – |
| 127 | `N33X14` Donchian20 + penapis MA200 → k | **49.1** | 45 | 53 | 34 | 70 | BELUM CUKUP | 6 | 90/5 | -0.60 | 6 | -0.48 | -0.12 | 2.4 | -0.42 | – | – |
| 128 | `M27` Price Action 4 Tiang | **49.1** | 46 | 42 | 44 | 15 | BELUM CUKUP | 2 | 547/434 | -0.73 | 19 | -2.41 | -0.47 | 2.8 | -0.22 | – | -0.62 |
| 129 | `M45` High 52 Minggu (George & Hwang | **49.1** | 18 | 46 | 33 | 45 | BELUM CUKUP | 1 | 2/1 | -2.77 | 8 | -0.53 | -0.29 | 1.0 | +0.41 | – | 2.11 |
| 130 | `N53X16` Supertrend + ADX>25 → keluar b | **49.0** | 52 | 48 | 41 | 30 | BELUM CUKUP | 6 | 94/4 | -0.03 | 6 | -2.16 | -0.49 | 3.4 | +0.44 | – | – |
| 131 | `M136` Short/Intermediate-term Low (L | **48.9** | 55 | 49 | 56 | 19 | BELUM CUKUP | 19 | 725/259 | -0.10 | 19 | -0.27 | -0.06 | 2.6 | +0.24 | – | 0.12 |
| 132 | `N53X17` Supertrend + ADX>25 → keluar b | **48.9** | 54 | 51 | 36 | 30 | BELUM CUKUP | 6 | 87/0 | -0.03 | 6 | -1.46 | -0.36 | 3.2 | +0.46 | – | – |
| 133 | `N47X16` NR7 + EMA9>EMA21 → keluar bila | **48.8** | 43 | 55 | 31 | 70 | BELUM CUKUP | 6 | 110/13 | -0.37 | 6 | -1.31 | -0.30 | 2.6 | -1.15 | – | – |
| 134 | `N07X36` Tiga MA tersusun → keluar sele | **48.8** | 49 | 53 | 38 | 30 | BELUM CUKUP | 6 | 115/8 | -0.18 | 6 | -0.94 | -0.24 | 2.4 | -0.17 | – | – |
| 135 | `N24X16` Supertrend(10,3) + ADX>20 → ke | **48.8** | 46 | 53 | 29 | 69 | BELUM CUKUP | 6 | 96/2 | -0.39 | 6 | -0.59 | -0.17 | 2.0 | -0.70 | – | – |
| 136 | `M94` Pecutan Momentum (Chen, Yu & W | **48.7** | 23 | 22 | 24 | 24 | BELUM CUKUP | 1 | 33/0 | -3.79 | 8 | -2.42 | -0.21 | 7.2 | -0.37 | – | -1.96 |
| 137 | `N16X13` RSI2<10 tanpa penapis → keluar | **48.6** | 54 | 46 | 32 | 45 | BELUM CUKUP | 6 | 113/3 | +0.48 | 6 | -3.54 | -0.39 | 6.4 | -0.55 | – | – |
| 138 | `N119X13` 3 tutup turun berturut → kelua | **48.6** | 48 | 43 | 34 | 66 | BELUM CUKUP | 6 | 144/33 | +0.14 | 6 | -4.71 | -0.57 | 6.8 | -1.19 | – | – |
| 139 | `N55X13` BB + RSI + ADX>20 → keluar bil | **48.6** | 59 | 54 | 26 | 30 | BELUM CUKUP | 6 | 57/0 | +0.67 | 6 | -2.23 | -0.48 | 3.5 | -0.61 | – | – |
| 140 | `M84` Jarak purata bergerak MAD 21/2 | **48.6** | 19 | 17 | 38 | 15 | BELUM CUKUP | 1 | 58/37 | -3.09 | 8 | -6.86 | -0.87 | 6.0 | -0.22 | – | -0.93 |
| 141 | `N113X36` 80-20 bar (sisi beli) → keluar | **48.4** | 52 | 35 | 43 | 47 | BELUM CUKUP | 6 | 244/148 | +0.46 | 6 | -5.28 | -0.77 | 5.9 | -0.57 | – | – |
| 142 | `M36` Turtle 55/20 | **48.2** | 48 | 42 | 56 | 33 | BELUM CUKUP | 19 | 330/152 | -0.57 | 19 | -0.22 | -0.02 | 6.4 | +0.27 | – | 0.60 |
| 143 | `N113X16` 80-20 bar (sisi beli) → keluar | **48.1** | 58 | 31 | 43 | 30 | BELUM CUKUP | 6 | 256/162 | +0.97 | 6 | -6.42 | -0.83 | 6.4 | -0.49 | – | – |
| 144 | `M41` FW Penyatuan Mingguan | **48.1** | 42 | 31 | 43 | 43 | BELUM CUKUP | 4 | 63/9 | -0.24 | 18 | -4.62 | -0.56 | 4.5 | +0.54 | – | 0.94 |
| 145 | `N39X36` NR7 kemudian pecah → keluar se | **48.1** | 18 | 43 | 25 | 70 | BELUM CUKUP | 2 | 18/5 | -3.09 | 5 | -0.18 | -0.05 | 2.0 | -1.14 | – | – |
| 146 | `M96` Momo India: Ranking Sharpe 3/6 | **48.1** | 13 | 10 | 9 | 15 | BELUM CUKUP | 1 | 6/6 | -13.40 | 8 | -8.03 | -1.00 | 6.0 | -5.74 | – | -15.35 |
| 147 | `M155` Market Cycle Strategy | **48.0** | 58 | 39 | 55 | 21 | BELUM CUKUP | 19 | 654/228 | +0.31 | 19 | -2.17 | -0.36 | 3.6 | +0.14 | – | 0.20 |
| 148 | `M32` Momentum Burst | **48.0** | 60 | 29 | 51 | 45 | BELUM CUKUP | 12 | 53/32 | +0.20 | 19 | -4.05 | -0.37 | 6.8 | +0.39 | – | 1.05 |
| 149 | `N27X16` Ichimoku atas awan → keluar bi | **48.0** | 36 | 47 | 34 | 70 | BELUM CUKUP | 6 | 127/44 | -0.87 | 6 | -1.21 | -0.41 | 1.8 | -1.22 | – | – |
| 150 | `N56X36` RSI>50 + ADX>20 → keluar selep | **48.0** | 46 | 33 | 40 | 58 | BELUM CUKUP | 6 | 145/51 | -0.04 | 6 | -4.83 | -0.66 | 5.5 | -0.55 | – | – |
| 151 | `M144` Screw Bar | **48.0** | 53 | 47 | 38 | 15 | BELUM CUKUP | 6 | 9/6 | -0.42 | 17 | -0.34 | -0.13 | 0.9 | -0.10 | – | -0.30 |
| 152 | `M115` Bow Tie (Landry) | **47.9** | 40 | 43 | 50 | 45 | BELUM CUKUP | 10 | 35/23 | -1.37 | 19 | -2.40 | -0.31 | 3.7 | +0.40 | – | 2.26 |
| 153 | `M138` 直升机空中加油 (Helikopter isi minyak | **47.9** | 37 | 55 | 23 | 15 | BELUM CUKUP | 3 | 3/0 | -0.81 | 12 | -0.18 | -0.29 | 0.3 | -0.74 | – | -0.88 |
| 154 | `M78` Alvarez Pecahan Mingguan DTAYS | **47.9** | 21 | 24 | 42 | 28 | BELUM CUKUP | 2 | 73/39 | -1.71 | 18 | -7.62 | -0.74 | 6.5 | +0.12 | – | 0.43 |
| 155 | `N38X36` VCP pecah → keluar selepas DUA | **47.8** | 37 | 50 | 30 | 62 | BELUM CUKUP | 6 | 22/6 | -0.79 | 6 | -0.67 | -0.21 | 1.9 | -1.02 | – | – |
| 156 | `N54X16` Supertrend + RSI>50 → keluar b | **47.6** | 41 | 40 | 29 | 70 | BELUM CUKUP | 6 | 107/4 | -0.43 | 6 | -3.03 | -0.38 | 4.7 | -0.97 | – | – |
| 157 | `N06X36` Golden cross MA50/MA200 → kelu | **47.5** | 30 | 52 | 27 | 70 | BELUM CUKUP | 5 | 14/2 | -0.95 | 6 | -1.25 | -0.30 | 2.3 | -0.95 | – | – |
| 158 | `M49` Ichimoku (Tutup Atas Awan + Te | **47.4** | 49 | 52 | 51 | 15 | BELUM CUKUP | 19 | 289/152 | -0.89 | 19 | +1.45 | +0.21 | 3.3 | -0.33 | – | -0.44 |
| 159 | `N31X36` Turtle sistem 2 → keluar selep | **47.3** | 36 | 44 | 30 | 57 | BELUM CUKUP | 6 | 91/3 | -1.01 | 6 | -1.26 | -0.35 | 2.3 | -0.73 | – | – |
| 160 | `M102` Stockbee SLTB | **47.1** | 51 | 46 | 53 | 15 | BELUM CUKUP | 19 | 359/265 | -0.80 | 19 | -0.17 | -0.02 | 5.4 | -0.10 | – | -0.28 |
| 161 | `M149` 3-Step Pullback | **47.1** | 46 | 38 | 56 | 29 | BELUM CUKUP | 17 | 201/53 | -0.36 | 19 | -2.82 | -0.26 | 5.4 | +0.58 | – | 0.48 |
| 162 | `N54X36` Supertrend + RSI>50 → keluar s | **47.1** | 47 | 29 | 40 | 30 | BELUM CUKUP | 6 | 140/42 | +0.10 | 6 | -6.34 | -0.78 | 6.2 | -0.55 | – | – |
| 163 | `N119X15` 3 tutup turun berturut → ekori | **47.0** | 39 | 44 | 19 | 57 | BELUM CUKUP | 5 | 40/0 | -0.58 | 6 | -3.59 | -0.53 | 5.0 | -1.42 | – | – |
| 164 | `M12` Parabolic SAR | **46.9** | 43 | 48 | 53 | 21 | BELUM CUKUP | 19 | 362/185 | -1.01 | 19 | +0.52 | +0.09 | 2.9 | -0.04 | – | -0.10 |
| 165 | `M68` Kell Base n' Break | **46.9** | 26 | 54 | 47 | 75 | BELUM CUKUP | 13 | 42/12 | -2.03 | 19 | +1.59 | +0.35 | 1.8 | +0.20 | – | 1.40 |
| 166 | `M20` EMA10/15 Crossover + Sudut | **46.8** | 47 | 49 | 50 | 16 | BELUM CUKUP | 19 | 443/344 | -0.68 | 19 | -1.07 | -0.18 | 2.7 | -0.45 | – | -3.31 |
| 167 | `M54` IBD Power Trend | **46.7** | 46 | 48 | 52 | 15 | BELUM CUKUP | 18 | 201/105 | -1.00 | 19 | +2.62 | +0.25 | 5.4 | -0.13 | – | -0.30 |
| 168 | `N57X36` ADX bangkit daripada <20 → kel | **46.6** | 25 | 56 | 30 | 46 | BELUM CUKUP | 6 | 60/6 | -1.66 | 6 | +1.14 | +0.34 | 2.1 | -0.94 | – | – |
| 169 | `N27X36` Ichimoku atas awan → keluar se | **46.5** | 34 | 39 | 30 | 36 | BELUM CUKUP | 6 | 85/7 | -0.92 | 6 | -2.27 | -0.52 | 3.0 | -0.98 | – | – |
| 170 | `N51X36` BB squeeze + Supertrend → kelu | **46.5** | 25 | 38 | 24 | 30 | BELUM CUKUP | 4 | 6/2 | -2.25 | 6 | -1.27 | -0.50 | 1.9 | -1.13 | – | – |
| 171 | `M64` O'Neil Tiga Minggu Ketat | **46.5** | 22 | 24 | 28 | 15 | BELUM CUKUP | 3 | 3/2 | -10.59 | 19 | -3.15 | -0.80 | 2.3 | -0.83 | – | -10.47 |
| 172 | `M128` Inventory Retracement Bar (IRB | **46.4** | 46 | 34 | 54 | 34 | BELUM CUKUP | 19 | 151/74 | -0.35 | 19 | -4.31 | -0.39 | 6.4 | +0.12 | – | 0.62 |
| 173 | `N57X16` ADX bangkit daripada <20 → kel | **46.4** | 24 | 56 | 29 | 46 | BELUM CUKUP | 6 | 58/4 | -1.70 | 6 | +1.14 | +0.34 | 2.1 | -0.98 | – | – |
| 174 | `N51X16` BB squeeze + Supertrend → kelu | **46.4** | 25 | 38 | 23 | 30 | BELUM CUKUP | 4 | 6/1 | -2.34 | 6 | -1.31 | -0.51 | 1.8 | -1.09 | – | – |
| 175 | `M38` Darvas Kotak | **46.4** | 18 | 35 | 35 | 45 | BELUM CUKUP | 4 | 23/1 | -2.00 | 18 | -2.32 | -0.23 | 4.5 | +0.23 | – | 1.26 |
| 176 | `M06` Minervini VCP Breakout | **46.2** | 41 | 55 | 48 | 15 | BELUM CUKUP | 19 | 80/34 | -1.14 | 19 | +0.61 | +0.10 | 2.8 | -0.18 | – | -0.48 |
| 177 | `N16X15` RSI2<10 tanpa penapis → ekori  | **46.2** | 42 | 32 | 26 | 30 | BELUM CUKUP | 6 | 109/0 | +0.17 | 6 | -7.69 | -0.66 | 8.7 | -0.64 | – | – |
| 178 | `N29X16` PSAR naik + tutup>MA50 → kelua | **46.0** | 25 | 34 | 36 | 62 | BELUM CUKUP | 6 | 157/57 | -1.43 | 6 | -3.92 | -0.53 | 5.3 | -1.19 | – | – |
| 179 | `N47X36` NR7 + EMA9>EMA21 → keluar sele | **46.0** | 26 | 40 | 26 | 34 | BELUM CUKUP | 5 | 100/10 | -1.05 | 6 | -4.09 | -0.59 | 4.9 | -1.59 | – | – |
| 180 | `M14` Walking with the Whales | **45.8** | 52 | 37 | 52 | 15 | BELUM CUKUP | 19 | 882/587 | -0.15 | 19 | -5.97 | -0.56 | 6.0 | -0.18 | – | -0.29 |
| 181 | `M157` Consolidation Pivot Breakout ( | **45.8** | 19 | 36 | 27 | 15 | BELUM CUKUP | 4 | 4/3 | -5.16 | 16 | -2.04 | -0.70 | 1.4 | -0.93 | – | -2.88 |
| 182 | `M127` Slingshot Bullish | **45.7** | 39 | 53 | 46 | 15 | BELUM CUKUP | 16 | 105/75 | -1.36 | 19 | -0.34 | -0.05 | 2.9 | -0.71 | – | -0.94 |
| 183 | `M26` Garis Trend Undur 3 Sentuhan + | **45.7** | 44 | 43 | 49 | 15 | BELUM CUKUP | 16 | 69/43 | -0.21 | 19 | -3.11 | -0.39 | 3.6 | -0.18 | – | -0.30 |
| 184 | `N29X36` PSAR naik + tutup>MA50 → kelua | **45.7** | 33 | 26 | 36 | 30 | BELUM CUKUP | 6 | 126/32 | -0.64 | 6 | -7.72 | -0.80 | 7.6 | -0.87 | – | – |
| 185 | `M19` Sneaky Pivot (proksi harian) | **45.3** | 33 | 46 | 52 | 28 | BELUM CUKUP | 18 | 377/231 | -1.47 | 19 | +1.17 | +0.15 | 3.3 | -0.23 | – | -4.07 |
| 186 | `M152` Spike & Ledge | **45.3** | 31 | 49 | 44 | 38 | BELUM CUKUP | 16 | 42/8 | -1.39 | 19 | +1.05 | +0.25 | 2.5 | -0.13 | – | -0.42 |
| 187 | `M73` ADX(5) > 40 + Julat Terkecil 6 | **45.1** | 45 | 40 | 51 | 15 | BELUM CUKUP | 19 | 877/699 | +0.15 | 19 | -5.07 | -0.63 | 4.7 | -0.33 | – | -2.34 |
| 188 | `M87` IBD Tapak Menaik | **45.0** | 30 | 33 | 39 | 15 | BELUM CUKUP | 7 | 10/6 | -3.09 | 19 | -3.07 | -0.53 | 3.4 | -0.22 | – | -0.77 |
| 189 | `M140` 猎豹出击 (Serangan Cheetah) | **44.9** | 39 | 38 | 37 | 15 | BELUM CUKUP | 10 | 41/12 | -0.62 | 19 | -3.35 | -0.54 | 2.8 | -0.87 | – | -1.11 |
| 190 | `M125` 2-Bar Breakout | **44.6** | 43 | 37 | 52 | 15 | BELUM CUKUP | 19 | 959/414 | -0.75 | 19 | -1.79 | -0.28 | 2.9 | -0.24 | – | -0.12 |
| 191 | `M50` Elder Triple Screen | **44.6** | 46 | 34 | 53 | 15 | BELUM CUKUP | 19 | 558/324 | -0.34 | 19 | -7.13 | -0.65 | 6.4 | -0.09 | – | -0.14 |
| 192 | `M120` Reversal New Highs | **44.4** | 37 | 39 | 44 | 15 | BELUM CUKUP | 13 | 19/12 | -1.24 | 19 | -1.65 | -0.25 | 3.2 | -0.10 | – | -0.65 |
| 193 | `M99` Three Line Break | **44.3** | 34 | 46 | 52 | 15 | BELUM CUKUP | 19 | 147/85 | -1.80 | 19 | +1.62 | +0.27 | 3.3 | -0.14 | – | -0.59 |
| 194 | `M141` First Thrust (Landry) | **44.3** | 24 | 44 | 34 | 15 | BELUM CUKUP | 8 | 23/8 | -1.92 | 19 | -1.90 | -0.37 | 2.1 | -0.97 | – | -1.90 |
| 195 | `M121` High 2 bull flag (Brooks) | **44.1** | 9 | 17 | 23 | 15 | BELUM CUKUP | 4 | 6/4 | -10.61 | 15 | -6.35 | -0.76 | 4.4 | -1.45 | – | -22.83 |
| 196 | `M55` Guppy GMMA | **44.0** | 42 | 34 | 52 | 15 | BELUM CUKUP | 19 | 205/120 | -0.91 | 19 | -4.19 | -0.48 | 4.3 | -0.15 | – | -0.47 |
| 197 | `M156` Single Penetration (DiNapoli) | **43.8** | 38 | 35 | 48 | 23 | BELUM CUKUP | 19 | 229/145 | -0.91 | 19 | -2.84 | -0.22 | 6.0 | -0.63 | – | -2.36 |
| 198 | `M119` 180 Bullish (Cooper) | **43.8** | 40 | 36 | 49 | 15 | BELUM CUKUP | 18 | 147/63 | -0.70 | 19 | -4.17 | -0.39 | 4.7 | -0.36 | – | -1.16 |
| 199 | `M130` 多方炮 (dua lilin hijau mengapit  | **43.7** | 15 | 27 | 37 | 18 | BELUM CUKUP | 6 | 9/3 | -2.60 | 17 | -2.12 | -0.39 | 2.7 | +0.11 | – | 0.09 |
| 200 | `M66` IBD Undur Pertama ke Purata 50 | **43.3** | 40 | 32 | 52 | 15 | BELUM CUKUP | 19 | 229/134 | -0.83 | 19 | -4.21 | -0.36 | 6.2 | -0.21 | – | -0.58 |
| 201 | `M79` Radge: 20% Flipper | **43.1** | 39 | 33 | 50 | 15 | BELUM CUKUP | 19 | 353/82 | -0.64 | 19 | -4.05 | -0.44 | 4.7 | -0.40 | – | -0.77 |
| 202 | `M28` VWAP Separator + Kiss Pivot | **42.8** | 34 | 35 | 45 | 15 | BELUM CUKUP | 17 | 112/88 | -1.00 | 19 | -5.10 | -0.60 | 5.4 | -0.87 | – | -8.61 |
| 203 | `M67` Rayner Teo: Ujian Ketiga pada  | **42.7** | 29 | 36 | 41 | 15 | BELUM CUKUP | 13 | 28/18 | -2.33 | 19 | -3.32 | -0.30 | 5.9 | -0.63 | – | -3.49 |
| 204 | `M44` Tapak Rata IBD | **42.5** | 18 | 40 | 22 | 15 | BELUM CUKUP | 8 | 9/5 | -4.03 | 19 | -3.52 | -0.75 | 2.7 | -2.17 | – | -32.75 |
| 205 | `M11` NR7 Breakout + Volume | **42.1** | 34 | 31 | 46 | 15 | BELUM CUKUP | 17 | 108/77 | -0.81 | 19 | -6.48 | -0.54 | 6.4 | -0.77 | – | -0.75 |
| 206 | `M95` Nisbah Kebaharuan High 52 Ming | **42.0** | 29 | 36 | 49 | 15 | BELUM CUKUP | 18 | 120/62 | -1.39 | 19 | -4.18 | -0.49 | 4.3 | -0.29 | – | -0.77 |
| 207 | `M147` Improved Three-Bar Pullback | **42.0** | 21 | 40 | 36 | 42 | BELUM CUKUP | 15 | 97/33 | -2.75 | 19 | -0.85 | -0.10 | 4.0 | -1.48 | – | -0.93 |
| 208 | `M135` 3rd Watch | **41.9** | 12 | 32 | 33 | 15 | BELUM CUKUP | 8 | 14/3 | -3.81 | 19 | -5.01 | -0.63 | 3.5 | -0.73 | – | -4.08 |
| 209 | `M57` Landry Trend Knockout (TKO) | **41.7** | 31 | 37 | 44 | 15 | BELUM CUKUP | 19 | 160/102 | -1.68 | 19 | -2.75 | -0.33 | 3.9 | -1.19 | – | -3.62 |
| 210 | `M161` EMA 10/21 + Supertrend (10,3) | **41.6** | 42 | 21 | 54 | 16 | BELUM CUKUP | 19 | 458/210 | -0.12 | 19 | -9.23 | -0.66 | 8.8 | +0.01 | – | 0.02 |
| 211 | `M29` EMA3 + RSI75 + Stokastik | **41.3** | 24 | 33 | 41 | 15 | BELUM CUKUP | 14 | 33/26 | -2.15 | 19 | -6.86 | -0.55 | 6.8 | -0.80 | – | -5.40 |
| 212 | `M82` Arthur Hill Rotasi Sasaran 10% | **41.2** | 38 | 22 | 52 | 15 | BELUM CUKUP | 19 | 565/208 | -0.48 | 19 | -5.97 | -0.38 | 8.2 | -0.15 | – | -0.62 |
| 213 | `M126` Hidden Smash Day (beli, Larry  | **40.4** | 12 | 32 | 34 | 15 | BELUM CUKUP | 10 | 18/11 | -4.06 | 18 | -4.86 | -0.67 | 3.9 | -0.90 | – | -1.65 |
| 214 | `M123` CCI Correction (Lambert, Chart | **39.8** | 25 | 34 | 39 | 15 | BELUM CUKUP | 19 | 175/151 | -1.36 | 19 | -7.95 | -0.74 | 6.1 | -1.72 | – | -3.95 |
| 215 | `M76` Undercut & Rally pada Low Pent | **39.7** | 23 | 30 | 43 | 15 | BELUM CUKUP | 18 | 71/45 | -1.15 | 19 | -7.99 | -0.73 | 6.2 | -0.87 | – | -3.99 |
| 216 | `M59` Anjakan Julat RSI | **38.7** | 15 | 25 | 43 | 15 | BELUM CUKUP | 14 | 36/16 | -4.46 | 19 | -3.83 | -0.48 | 3.8 | -0.37 | – | -1.62 |
| 217 | `M101` Bulkowski: Tiga lembah menaik | **38.0** | 14 | 23 | 46 | 15 | BELUM CUKUP | 15 | 44/21 | -3.24 | 19 | -7.01 | -0.57 | 6.2 | -0.18 | – | -0.57 |
| 218 | `M154` HOLP (High of Low Period) | **37.4** | 13 | 21 | 44 | 15 | BELUM CUKUP | 15 | 79/32 | -2.00 | 19 | -9.31 | -0.72 | 6.7 | -0.63 | – | -3.41 |
| 219 | `M122` Moving Momentum (ChartSchool) | **37.2** | 18 | 25 | 40 | 15 | BELUM CUKUP | 19 | 102/58 | -2.49 | 19 | -6.87 | -0.80 | 4.9 | -1.33 | – | -4.32 |
| 220 | `M47` Holy Grail Raschke | **35.5** | 6 | 17 | 28 | 15 | BELUM CUKUP | 13 | 29/22 | -3.31 | 19 | -9.41 | -0.91 | 5.7 | -2.27 | – | -23.60 |
| 221 | `M81` Bensdorp Long Trend High Momen | **35.2** | 4 | 10 | 45 | 15 | BELUM CUKUP | 12 | 331/140 | -3.94 | 19 | -17.01 | -0.74 | 13.4 | -0.84 | – | -3.01 |
| 222 | `M09` Volumatic VIDYA Pivot Retest | **35.2** | 4 | 11 | 32 | 15 | BELUM CUKUP | 12 | 29/16 | -4.35 | 19 | -10.97 | -0.93 | 7.3 | -1.60 | – | -11.26 |
| 223 | `M90` Pring KST | **31.9** | 4 | 15 | 44 | 15 | BELUM CUKUP | 18 | 78/42 | -3.10 | 19 | -12.25 | -0.67 | 10.5 | -0.82 | – | -4.08 |

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

