# Skor Kaedah 0–100 (pangkat maklumat, BUKAN keputusan)

> **Status keputusan (kad skor, harga 2026-11-20):** TERBUKTI 0 · CALON 0 · BELUM CUKUP 226 · GAGAL 1 · NEGATIF 0. Rejim QQQ OFF sejak 2026-10-16. Hanya **TERBUKTI** layak untuk wang sebenar (`laporan/KAD_SKOR.md`); nombor dalam laporan ini BUKAN keputusan dan tidak boleh dibaca sebagai pangkat untuk wang sebenar.

Dijana 2026-11-21 oleh `standard/skor_kaedah.py` (Actions `analisis.yml`, selepas kad skor). Harga pada tutup 2026-11-20; 227 kaedah; 26 hari beli langsung (rejim ON 1, OFF 25). Pradaftar 2026-11-09: `standard/SPEC_SKOR_KAEDAH.md` (berat dan sauh dikunci `ujian/test_skor_kaedah.py::TestKunci`). Rekod analisis sahaja: tiada order, tiada wang sebenar.

## Cara membaca

- **Skor** = min geometri berberat empat tiang (Untung 35 · Tahan 30 · Bukti 25 · Konsisten 10), dikecut ke 50 mengikut data: berat data = hari beli ÷ (hari beli + 20). Kaedah dengan 2 hari beli tidak boleh menjauhi 50. 100 = unggul semua segi; 50 = neutral/tiada bukti; < 50 = lebih buruk daripada neutral.
- **Siling** ikut kad skor: NEGATIF ≤ 20, GANTUNG/BERSARA ≤ 30, GAGAL ≤ 40. Tanda ⌈ = siling terpakai.
- **Satu-satunya status yang membenarkan wang sebenar ialah TERBUKTI dalam `laporan/KAD_SKOR.md`.** Skor tinggi dengan status BELUM CUKUP bermaksud "paling menjanjikan setakat ini", bukan "selamat".
- Deflasi ujian berganda (López de Prado): sauh t Bukti C1 = maks(2.0, E[maks 227 normal]) = 2.81.
- **Semakan kebolehramalan:** skor pada 2026-11-13 lawan pulangan lorong T4 sejak itu, 226 kaedah: Spearman ρ = +0.029 (p = 0.666). Belum ada bukti skor meramal pangkat; jangan pilih kaedah dengannya.
- Metrik T4 (A2, B1, B2, D1) dikira atas lorong T4 L1 **dipotong pada sesi LANGSUNG pertama** kaedah itu (Mxx 2026-10-16, Nxx/GB 2026-11-03) dan diasas semula; sesi isian bina semula tidak dikira (pindaan 9 Nov 2026 (a)). Lajur "T4 sesi/pul" di bawah ialah potongan itu, bukan lorong penuh `T4_KAEDAH.md`.

## Semua kaedah, susun ikut Skor

| # | Kaedah | Skor | Untung | Tahan | Bukti | Konsisten | Status kad | Hari beli | Posisi/tutup | Jangkaan % | T4 sesi | T4 pul % | T4 pul/|MDD| | Ulcer | t buku | Lift | WFE |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `M133` Bull Hook (Crabel) | **53.2** | 48 | 59 | 56 | 99 | BELUM CUKUP | 16 | 54/44 | -1.34 | 26 | +1.76 | +0.31 | 2.5 | +0.72 | +3.91 | 6.17 |
| 2 | `M151` Outside Bar Failure | **52.4** | 43 | 77 | 49 | 55 | BELUM CUKUP | 24 | 116/76 | -1.96 | 26 | +4.06 | +1.01 | 1.1 | -0.59 | -0.04 | -1.51 |
| 3 | `M146` 3-Bar Momentum Pattern | **51.3** | 47 | 56 | 53 | 68 | BELUM CUKUP | 20 | 80/44 | -1.44 | 26 | +2.33 | +0.33 | 3.1 | +0.18 | – | 0.43 |
| 4 | `M104` High Tight Flag / Power Play | **51.1** | 90 | 90 | 41 | 85 | BELUM CUKUP | 1 | 1/0 | +22.86 | 11 | +2.31 | +8.77 | 0.1 | +1.71 | – | 11.28 |
| 5 | `M160` Measured Move Up | **49.4** | 37 | 49 | 57 | 86 | BELUM CUKUP | 24 | 130/102 | -2.79 | 26 | -0.73 | -0.13 | 2.6 | +0.33 | +0.37 | 2.42 |
| 6 | `M159` Heikin-Ashi Trend | **49.4** | 50 | 54 | 43 | 47 | BELUM CUKUP | 26 | 1916/1808 | -1.12 | 26 | +2.15 | +0.35 | 3.7 | -1.35 | -0.26 | -10.52 |
| 7 | `M07` Qullamaggie Breakout | **49.4** | 36 | 64 | 27 | 15 | BELUM CUKUP | 1 | 1/1 | -2.53 | 26 | -0.25 | -0.21 | 0.9 | -0.22 | – | -1.12 |
| 8 | `N204X36` Undur RSI2, gap 2%, RSI silang | **49.2** | 32 | 40 | 27 | 50 | BELUM CUKUP | 1 | 1/0 | -1.45 | 1 | -0.12 | -1.00 | – | – | – | – |
| 9 | `M45` High 52 Minggu (George & Hwang | **49.1** | 27 | 42 | 29 | 27 | BELUM CUKUP | 1 | 2/1 | -4.75 | 15 | -0.93 | -0.51 | 0.9 | +0.01 | – | 0.02 |
| 10 | `M48` Cooper 1-2-3-4 | **49.0** | 41 | 55 | 48 | 55 | BELUM CUKUP | 21 | 70/24 | -2.86 | 26 | +4.63 | +0.81 | 2.5 | -0.11 | – | -0.29 |
| 11 | `M84` Jarak purata bergerak MAD 21/2 | **48.5** | 26 | 10 | 28 | 15 | BELUM CUKUP | 1 | 58/41 | -5.53 | 15 | -8.79 | -1.00 | 6.9 | -1.42 | – | -3.59 |
| 12 | `M27` Price Action 4 Tiang | **48.4** | 39 | 32 | 35 | 15 | BELUM CUKUP | 2 | 546/509 | -1.59 | 26 | -4.16 | -0.81 | 3.1 | -1.27 | – | -4.71 |
| 13 | `M51` O'Neil Cawan & Pemegang | **48.2** | 28 | 44 | 28 | 15 | BELUM CUKUP | 2 | 3/1 | -4.12 | 16 | -1.20 | -0.73 | 0.8 | -0.34 | – | -1.39 |
| 14 | `M96` Momo India: Ranking Sharpe 3/6 | **48.2** | 24 | 7 | 9 | 15 | BELUM CUKUP | 1 | 6/6 | -13.71 | 15 | -8.21 | -1.00 | 7.2 | -5.92 | – | -15.55 |
| 15 | `M10` EMA3 + CCI + MACD | **48.1** | 37 | 55 | 47 | 60 | BELUM CUKUP | 22 | 127/76 | -4.13 | 26 | +5.61 | +0.85 | 2.7 | -0.72 | +1.36 | -2.43 |
| 16 | `M46` Jurang Naik Boleh Beli (Buyabl | **48.1** | 42 | 49 | 42 | 55 | BELUM CUKUP | 13 | 36/26 | -2.70 | 26 | -1.27 | -0.26 | 1.8 | -0.71 | – | -1.30 |
| 17 | `M137` Livermore System | **47.9** | 38 | 51 | 49 | 59 | BELUM CUKUP | 24 | 183/95 | -3.69 | 26 | +2.09 | +0.35 | 2.4 | -0.62 | +1.16 | -1.28 |
| 18 | `M94` Pecutan Momentum (Chen, Yu & W | **47.7** | 0 | 0 | 11 | 15 | BELUM CUKUP | 1 | 33/0 | -18.35 | 15 | -21.74 | -1.00 | 10.3 | -1.80 | – | -6.44 |
| 19 | `M25` VWAP Wave (proksi harian) | **47.6** | 47 | 52 | 53 | 19 | BELUM CUKUP | 24 | 200/164 | -1.63 | 26 | +0.75 | +0.09 | 3.9 | -0.21 | +1.13 | -1.23 |
| 20 | `M78` Alvarez Pecahan Mingguan DTAYS | **47.6** | 23 | 20 | 36 | 15 | BELUM CUKUP | 2 | 73/47 | -3.94 | 25 | -8.85 | -0.79 | 8.0 | -0.69 | – | -2.15 |
| 21 | `M118` Expansion Pivot (Cooper) | **47.2** | 34 | 52 | 48 | 58 | BELUM CUKUP | 20 | 85/44 | -3.03 | 26 | +2.43 | +0.29 | 2.8 | -0.37 | +0.71 | -1.47 |
| 22 | `M13` Garis Trend Action/Safety Line | **46.9** | 37 | 52 | 44 | 53 | BELUM CUKUP | 26 | 861/717 | -3.53 | 26 | +2.69 | +0.41 | 2.1 | -1.30 | -0.47 | -4.50 |
| 23 | `M37` Weinstein Peringkat 2 | **46.9** | 30 | 37 | 18 | 15 | BELUM CUKUP | 3 | 7/0 | -5.88 | 20 | -3.97 | -0.80 | 1.6 | -1.30 | – | -2.50 |
| 24 | `M33` Supertrend + SMA10 | **46.7** | 32 | 50 | 51 | 58 | BELUM CUKUP | 23 | 224/109 | -4.24 | 26 | +3.48 | +0.48 | 2.6 | -0.40 | +0.92 | -2.39 |
| 25 | `M64` O'Neil Tiga Minggu Ketat | **46.7** | 32 | 22 | 26 | 15 | BELUM CUKUP | 3 | 3/3 | -12.60 | 26 | -3.76 | -0.84 | 3.0 | -1.26 | – | -14.58 |
| 26 | `M21` Marius 3 Persediaan (Pecahan+J | **46.4** | 29 | 44 | 35 | 15 | BELUM CUKUP | 5 | 5/4 | -3.48 | 18 | -1.72 | -0.64 | 1.7 | -0.18 | – | -0.28 |
| 27 | `M145` Yum-Yum Continuation | **46.3** | 33 | 49 | 48 | 59 | BELUM CUKUP | 23 | 311/107 | -4.49 | 26 | +1.21 | +0.31 | 1.6 | -0.79 | +1.00 | -0.79 |
| 28 | `M129` Wick Play | **46.3** | 34 | 39 | 40 | 55 | BELUM CUKUP | 10 | 25/13 | -3.86 | 26 | +0.05 | +0.01 | 2.0 | -0.48 | – | -1.82 |
| 29 | `N202X36` RSI2<10 dalam trend naik x X36 | **46.2** | 27 | 58 | 19 | 55 | BELUM CUKUP | 6 | 101/7 | -2.69 | 6 | +0.07 | +0.03 | 1.2 | -2.29 | – | – |
| 30 | `M23` Breitstein Kapitulasi + Kesina | **46.0** | 45 | 44 | 54 | 18 | BELUM CUKUP | 23 | 130/100 | -1.68 | 26 | -3.22 | -0.48 | 3.2 | -0.09 | +0.83 | -0.37 |
| 31 | `M74` Lulus Baharu Trend Template Mi | **45.8** | 42 | 47 | 49 | 22 | BELUM CUKUP | 26 | 107/82 | -2.17 | 26 | -1.77 | -0.24 | 3.3 | -0.63 | -0.07 | -1.21 |
| 32 | `M138` 直升机空中加油 (Helikopter isi minyak | **45.8** | 34 | 37 | 12 | 15 | BELUM CUKUP | 4 | 4/0 | -5.40 | 19 | -2.07 | -0.92 | 0.9 | -2.19 | – | -3.42 |
| 33 | `N25X36` Supertrend + EMA + ADX>23 → ke | **45.6** | 35 | 37 | 35 | 70 | BELUM CUKUP | 12 | 140/56 | -4.37 | 13 | -2.04 | -0.46 | 2.1 | -1.48 | – | – |
| 34 | `M05` MACD Divergence + Pengesahan | **45.5** | 39 | 39 | 37 | 55 | BELUM CUKUP | 16 | 42/15 | -5.00 | 26 | -2.50 | -0.36 | 2.5 | -1.16 | – | -2.62 |
| 35 | `M70` Pecahan Hari Dalam | **45.4** | 54 | 48 | 48 | 8 | BELUM CUKUP | 26 | 507/445 | -1.21 | 26 | -1.84 | -0.32 | 2.5 | -0.84 | -1.85 | -2.23 |
| 36 | `M87` IBD Tapak Menaik | **44.9** | 36 | 32 | 37 | 15 | BELUM CUKUP | 8 | 11/8 | -4.22 | 26 | -4.62 | -0.59 | 4.6 | -0.56 | – | -1.59 |
| 37 | `M35` Pocket Pivot Morales & Kacher | **44.8** | 52 | 34 | 49 | 17 | BELUM CUKUP | 25 | 333/294 | -0.97 | 26 | -5.26 | -0.57 | 5.7 | -0.62 | +0.61 | -3.72 |
| 38 | `M39` Radge Pecahan Bollinger 100 ha | **44.8** | 33 | 43 | 45 | 55 | BELUM CUKUP | 23 | 244/67 | -5.75 | 26 | +0.92 | +0.14 | 2.1 | -0.96 | -0.11 | -2.18 |
| 39 | `M100` Bulkowski Segi Empat & Segi Ti | **44.7** | 40 | 37 | 46 | 25 | BELUM CUKUP | 17 | 61/45 | -1.57 | 26 | -3.20 | -0.40 | 3.1 | -0.56 | – | -3.13 |
| 40 | `M157` Consolidation Pivot Breakout ( | **44.7** | 26 | 33 | 28 | 15 | BELUM CUKUP | 6 | 8/3 | -3.60 | 23 | -2.77 | -0.81 | 1.9 | -0.97 | – | -2.14 |
| 41 | `M144` Screw Bar | **44.5** | 32 | 30 | 31 | 15 | BELUM CUKUP | 7 | 10/8 | -3.10 | 24 | -3.04 | -0.89 | 1.5 | -0.98 | – | -1.61 |
| 42 | `M41` FW Penyatuan Mingguan | **44.2** | 18 | 19 | 37 | 15 | BELUM CUKUP | 5 | 67/12 | -3.87 | 25 | -9.39 | -0.80 | 6.1 | -0.37 | – | -0.64 |
| 43 | `M38` Darvas Kotak | **44.2** | 21 | 17 | 31 | 15 | BELUM CUKUP | 5 | 26/1 | -6.31 | 25 | -6.03 | -0.52 | 6.3 | -0.29 | – | -1.26 |
| 44 | `M124` 'Last' Stochastic Technique (C | **44.1** | 34 | 38 | 47 | 49 | BELUM CUKUP | 26 | 415/317 | -3.48 | 26 | -2.67 | -0.30 | 3.6 | -0.93 | -0.02 | -2.86 |
| 45 | `N203X36` Gap 2% lalu MA20 silang MA50 x | **44.0** | 20 | 21 | 17 | 30 | BELUM CUKUP | 5 | 13/3 | -8.46 | 6 | -9.98 | -0.95 | 5.3 | -2.22 | – | – |
| 46 | `M132` Ascending Scallop (Bulkowski) | **43.9** | 35 | 39 | 45 | 24 | BELUM CUKUP | 18 | 96/49 | -4.30 | 26 | -2.02 | -0.26 | 3.1 | -0.66 | – | -4.75 |
| 47 | `M77` Undercut & Rally pada Purata B | **43.8** | 32 | 38 | 42 | 37 | BELUM CUKUP | 18 | 55/42 | -2.13 | 26 | -5.79 | -0.71 | 2.7 | -1.03 | +0.36 | -1.51 |
| 48 | `M115` Bow Tie (Landry) | **43.5** | 33 | 33 | 45 | 14 | BELUM CUKUP | 12 | 37/29 | -3.03 | 26 | -5.93 | -0.62 | 5.3 | -0.36 | -0.26 | -1.85 |
| 49 | `M121` High 2 bull flag (Brooks) | **43.5** | 20 | 15 | 19 | 15 | BELUM CUKUP | 5 | 8/3 | -8.24 | 22 | -6.43 | -0.84 | 4.8 | -1.94 | – | -18.10 |
| 50 | `N201X36` MA20 silang MA50 atas MA50 x X | **43.3** | 23 | 24 | 14 | 30 | BELUM CUKUP | 6 | 25/6 | -6.22 | 6 | -7.44 | -1.00 | 3.8 | -3.31 | – | – |
| 51 | `N53X36` Supertrend + ADX>25 → keluar s | **43.2** | 32 | 28 | 43 | 30 | BELUM CUKUP | 13 | 143/58 | -3.05 | 13 | -7.10 | -0.77 | 4.1 | -0.67 | – | – |
| 52 | `M44` Tapak Rata IBD | **43.1** | 30 | 35 | 18 | 15 | BELUM CUKUP | 8 | 9/8 | -5.62 | 26 | -5.00 | -0.87 | 3.5 | -2.96 | – | -37.35 |
| 53 | `N45X16` Undur EMA21 cerun positif → ke | **42.9** | 26 | 36 | 39 | 30 | BELUM CUKUP | 13 | 187/108 | -4.08 | 13 | -1.82 | -0.22 | 3.5 | -1.37 | – | – |
| 54 | `N65X36` Gap 4% + volum + hampir 52w →  | **42.7** | 21 | 12 | 21 | 30 | BELUM CUKUP | 6 | 31/4 | -7.64 | 13 | -7.67 | -1.00 | 3.8 | -1.87 | – | – |
| 55 | `N65X14` Gap 4% + volum + hampir 52w →  | **42.7** | 20 | 12 | 21 | 30 | BELUM CUKUP | 6 | 31/4 | -7.39 | 13 | -8.45 | -1.00 | 3.9 | -1.86 | – | – |
| 56 | `M08` SMA20 + SMA200 | **42.5** | 34 | 30 | 46 | 46 | BELUM CUKUP | 24 | 265/210 | -2.46 | 26 | -5.28 | -0.99 | 3.7 | -0.99 | +0.55 | -2.65 |
| 57 | `M18` EMA9/21 Pullback | **42.4** | 42 | 30 | 48 | 21 | BELUM CUKUP | 26 | 477/421 | -1.21 | 26 | -10.02 | -1.00 | 4.9 | -0.76 | +1.71 | -2.86 |
| 58 | `M153` Range Leader | **42.3** | 46 | 29 | 47 | 16 | BELUM CUKUP | 26 | 1435/1381 | -0.74 | 26 | -7.52 | -0.56 | 8.3 | -0.87 | +0.37 | -7.41 |
| 59 | `M120` Reversal New Highs | **42.3** | 32 | 30 | 39 | 15 | BELUM CUKUP | 13 | 19/13 | -2.79 | 26 | -4.54 | -0.69 | 3.7 | -0.74 | – | -4.13 |
| 60 | `M131` Ross Hook (Joe Ross) | **42.2** | 34 | 38 | 49 | 17 | BELUM CUKUP | 24 | 273/153 | -3.04 | 26 | -4.23 | -0.48 | 4.3 | -0.68 | +0.45 | -1.78 |
| 61 | `M54` IBD Power Trend | **42.2** | 37 | 37 | 45 | 15 | BELUM CUKUP | 23 | 222/139 | -3.39 | 26 | -2.41 | -0.23 | 5.9 | -1.07 | -0.01 | -2.42 |
| 62 | `N36X36` Pocket pivot → keluar selepas  | **41.9** | 28 | 23 | 33 | 57 | BELUM CUKUP | 13 | 173/100 | -4.88 | 13 | -6.14 | -0.65 | 4.0 | -2.05 | – | – |
| 63 | `N68X36` Bullish engulfing + EMA21 → ke | **41.9** | 25 | 30 | 35 | 30 | BELUM CUKUP | 13 | 131/36 | -4.20 | 13 | -5.41 | -0.60 | 4.7 | -1.39 | – | – |
| 64 | `N51X16` BB squeeze + Supertrend → kelu | **41.6** | 24 | 27 | 16 | 30 | BELUM CUKUP | 9 | 15/3 | -5.63 | 13 | -7.78 | -0.94 | 4.0 | -2.55 | – | – |
| 65 | `M89` Chande 65sma-3cc | **41.5** | 36 | 35 | 47 | 12 | BELUM CUKUP | 23 | 194/136 | -4.11 | 26 | -3.29 | -0.30 | 5.0 | -0.90 | -0.70 | -3.33 |
| 66 | `M127` Slingshot Bullish | **41.5** | 32 | 36 | 40 | 18 | BELUM CUKUP | 20 | 112/92 | -2.69 | 26 | -7.51 | -0.78 | 4.5 | -1.61 | +0.69 | -1.97 |
| 67 | `M130` 多方炮 (dua lilin hijau mengapit  | **41.5** | 22 | 14 | 31 | 15 | BELUM CUKUP | 8 | 12/5 | -6.77 | 24 | -7.88 | -0.79 | 4.8 | -0.87 | – | -0.74 |
| 68 | `M88` O'Neil Shakeout +3 | **41.4** | 32 | 34 | 44 | 15 | BELUM CUKUP | 20 | 85/61 | -5.91 | 26 | -5.37 | -0.35 | 7.0 | -1.00 | +0.01 | -2.09 |
| 69 | `M91` Stochastic Pop (Bernstein/Stec | **41.4** | 33 | 20 | 46 | 28 | BELUM CUKUP | 16 | 39/32 | -4.48 | 26 | -4.57 | -0.28 | 7.0 | -0.31 | +0.58 | -1.38 |
| 70 | `N43X36` Undur EMA8 + penapis MA50 → ke | **41.4** | 30 | 22 | 34 | 30 | BELUM CUKUP | 13 | 216/87 | -5.00 | 13 | -6.54 | -0.90 | 3.5 | -1.88 | – | – |
| 71 | `M93` Bollinger Kaedah II: %b + MFI | **41.3** | 32 | 31 | 51 | 20 | BELUM CUKUP | 24 | 272/113 | -2.88 | 26 | -4.29 | -0.45 | 4.0 | -0.45 | +1.47 | -0.77 |
| 72 | `M142` Pecahan volum dari dasar (底部放量 | **41.3** | 26 | 28 | 39 | 55 | BELUM CUKUP | 18 | 56/12 | -4.52 | 24 | -2.41 | -0.29 | 3.1 | -0.61 | – | -1.22 |
| 73 | `N37X36` Gap and go → keluar selepas DU | **41.3** | 23 | 20 | 29 | 30 | BELUM CUKUP | 10 | 87/36 | -5.98 | 13 | -4.95 | -0.64 | 3.7 | -1.92 | – | – |
| 74 | `N51X36` BB squeeze + Supertrend → kelu | **41.3** | 24 | 23 | 16 | 30 | BELUM CUKUP | 9 | 15/4 | -5.81 | 13 | -8.03 | -0.94 | 4.0 | -2.60 | – | – |
| 75 | `N41X36` CMF20>0 + tutup>EMA20 → keluar | **41.2** | 25 | 26 | 32 | 30 | BELUM CUKUP | 13 | 274/216 | -3.46 | 13 | -7.78 | -0.90 | 4.3 | -2.14 | – | – |
| 76 | `N25X16` Supertrend + EMA + ADX>23 → ke | **41.2** | 24 | 27 | 29 | 30 | BELUM CUKUP | 12 | 124/30 | -6.77 | 13 | -3.56 | -0.74 | 2.8 | -1.96 | – | – |
| 77 | `N64X17` Episodic pivot → keluar bila a | **41.2** | 20 | 17 | 30 | 30 | BELUM CUKUP | 9 | 52/15 | -5.56 | 13 | -6.43 | -0.79 | 3.8 | -1.53 | – | – |
| 78 | `M158` Doubly Adaptive Profit Targets | **41.1** | 31 | 30 | 54 | 21 | BELUM CUKUP | 24 | 391/190 | -2.40 | 26 | -6.96 | -0.65 | 4.5 | -0.13 | +1.49 | -0.33 |
| 79 | `M68` Kell Base n' Break | **41.1** | 30 | 32 | 42 | 11 | BELUM CUKUP | 16 | 52/17 | -5.09 | 26 | -4.18 | -0.53 | 3.1 | -0.65 | -1.01 | -4.12 |
| 80 | `N64X36` Episodic pivot → keluar selepa | **41.1** | 18 | 17 | 30 | 30 | BELUM CUKUP | 9 | 52/12 | -5.98 | 13 | -6.80 | -0.78 | 3.9 | -1.37 | – | – |
| 81 | `N37X17` Gap and go → keluar bila adx14 | **41.0** | 21 | 19 | 28 | 30 | BELUM CUKUP | 10 | 87/35 | -5.86 | 13 | -5.49 | -0.64 | 3.9 | -2.04 | – | – |
| 82 | `M102` Stockbee SLTB | **40.8** | 35 | 33 | 46 | 15 | BELUM CUKUP | 26 | 444/355 | -2.19 | 26 | -6.79 | -0.58 | 6.5 | -1.02 | -0.10 | -2.67 |
| 83 | `N124X36` Episodic pivot gap 8-10% → kel | **40.8** | 18 | 15 | 30 | 30 | BELUM CUKUP | 9 | 42/17 | -4.90 | 13 | -11.90 | -1.00 | 5.9 | -1.48 | – | – |
| 84 | `N19X13` Bawah jalur BB + RSI<30 → kelu | **40.8** | 20 | 16 | 22 | 30 | BELUM CUKUP | 9 | 120/0 | -7.78 | 13 | -6.51 | -0.84 | 3.7 | -1.26 | – | – |
| 85 | `M67` Rayner Teo: Ujian Ketiga pada  | **40.7** | 34 | 27 | 37 | 15 | BELUM CUKUP | 17 | 32/27 | -4.01 | 26 | -7.86 | -0.66 | 7.2 | -1.40 | – | -5.47 |
| 86 | `N09X36` Undur EMA10 + penapis EMA50 →  | **40.7** | 27 | 20 | 34 | 30 | BELUM CUKUP | 13 | 231/101 | -5.05 | 13 | -7.50 | -1.00 | 3.8 | -1.95 | – | – |
| 87 | `N35X36` Pecah 52 minggu tinggi → kelua | **40.7** | 21 | 20 | 23 | 30 | BELUM CUKUP | 10 | 51/6 | -7.63 | 13 | -4.83 | -0.77 | 2.3 | -1.99 | – | – |
| 88 | `M134` First Kiss After Daylight (Lan | **40.6** | 31 | 29 | 45 | 15 | BELUM CUKUP | 20 | 68/38 | -4.16 | 26 | -6.66 | -0.60 | 5.3 | -0.65 | +0.00 | -1.01 |
| 89 | `M126` Hidden Smash Day (beli, Larry  | **40.6** | 21 | 29 | 33 | 15 | BELUM CUKUP | 12 | 21/10 | -3.80 | 25 | -6.26 | -0.77 | 5.0 | -1.12 | – | -1.41 |
| 90 | `N64X14` Episodic pivot → keluar bila r | **40.6** | 18 | 14 | 28 | 30 | BELUM CUKUP | 9 | 52/7 | -6.29 | 13 | -7.77 | -0.96 | 3.5 | -1.38 | – | – |
| 91 | `N64X16` Episodic pivot → keluar bila s | **40.6** | 17 | 14 | 30 | 30 | BELUM CUKUP | 9 | 52/12 | -6.03 | 13 | -7.60 | -0.96 | 3.4 | -1.40 | – | – |
| 92 | `N66X36` 52w tinggi + pengesahan 1% → k | **40.6** | 18 | 11 | 23 | 30 | BELUM CUKUP | 8 | 40/3 | -7.16 | 12 | -8.35 | -1.00 | 4.6 | -1.66 | – | – |
| 93 | `N76X36` Tutup > MA50 (penapis trend tu | **40.5** | 26 | 20 | 33 | 30 | BELUM CUKUP | 13 | 198/135 | -4.70 | 13 | -11.66 | -1.00 | 5.8 | -1.97 | – | – |
| 94 | `N07X16` Tiga MA tersusun → keluar bila | **40.5** | 21 | 26 | 32 | 30 | BELUM CUKUP | 13 | 169/57 | -5.54 | 13 | -4.58 | -0.77 | 3.0 | -1.91 | – | – |
| 95 | `N37X16` Gap and go → keluar bila super | **40.5** | 20 | 16 | 28 | 30 | BELUM CUKUP | 10 | 87/36 | -6.47 | 13 | -6.00 | -0.85 | 3.3 | -2.06 | – | – |
| 96 | `M02` MACD + SMA200 | **40.4** | 33 | 23 | 42 | 57 | BELUM CUKUP | 26 | 137/115 | -4.75 | 26 | -5.42 | -0.34 | 5.6 | -1.44 | +0.46 | -11.44 |
| 97 | `M150` Trend Bar Failure (Brooks) | **40.4** | 28 | 32 | 44 | 22 | BELUM CUKUP | 22 | 111/82 | -2.24 | 26 | -8.46 | -0.87 | 4.3 | -1.07 | +1.86 | -4.73 |
| 98 | `M32` Momentum Burst | **40.4** | 32 | 21 | 48 | 15 | BELUM CUKUP | 17 | 67/48 | -2.59 | 26 | -9.00 | -0.63 | 8.5 | -0.32 | – | -0.74 |
| 99 | `M143` 장대양봉 이후 눌림목 / 5일선 매매 (Undur ke | **40.4** | 25 | 34 | 28 | 21 | BELUM CUKUP | 15 | 29/3 | -5.41 | 25 | -3.58 | -0.67 | 2.2 | -1.38 | – | -11.08 |
| 100 | `N08X36` tutup>EMA20 tidak terlalu jauh | **40.4** | 21 | 26 | 31 | 30 | BELUM CUKUP | 13 | 456/368 | -3.10 | 13 | -9.17 | -0.96 | 4.3 | -2.22 | – | – |
| 101 | `N48X36` Inside day pecah → keluar sele | **40.4** | 22 | 19 | 36 | 47 | BELUM CUKUP | 13 | 339/256 | -1.75 | 13 | -8.71 | -1.00 | 5.7 | -1.68 | – | – |
| 102 | `N80X36` Tinggi sepanjang masa → keluar | **40.4** | 18 | 14 | 26 | 30 | BELUM CUKUP | 9 | 40/6 | -7.78 | 13 | -6.94 | -0.99 | 3.1 | -1.61 | – | – |
| 103 | `M15` Break & Retest + Henti ATR | **40.3** | 32 | 27 | 48 | 23 | BELUM CUKUP | 26 | 324/271 | -1.37 | 26 | -11.83 | -0.77 | 6.2 | -0.74 | +2.08 | -1.94 |
| 104 | `M148` Natural Number Method | **40.2** | 33 | 38 | 38 | 14 | BELUM CUKUP | 26 | 233/221 | -3.02 | 26 | -4.15 | -0.39 | 4.1 | -1.98 | -1.34 | -8.13 |
| 105 | `M105` Supertrend tulen | **40.2** | 30 | 31 | 49 | 17 | BELUM CUKUP | 24 | 376/205 | -4.31 | 26 | -4.15 | -0.34 | 5.6 | -0.68 | +0.60 | -2.41 |
| 106 | `M111` Sistem Volatiliti Wilder | **40.1** | 31 | 32 | 49 | 14 | BELUM CUKUP | 25 | 275/156 | -4.01 | 26 | -3.49 | -0.33 | 4.7 | -0.68 | -0.40 | -2.17 |
| 107 | `M80` Radge Saluran Purata Bergerak  | **40.1** | 29 | 28 | 51 | 22 | BELUM CUKUP | 25 | 311/117 | -3.72 | 26 | -5.43 | -0.52 | 5.2 | -0.48 | +1.82 | -0.84 |
| 108 | `M30` BB Free Bar + Himpitan 50/2.5 | **40.1** | 30 | 25 | 50 | 16 | BELUM CUKUP | 21 | 230/108 | -3.62 | 26 | -4.30 | -0.38 | 5.8 | -0.43 | +0.41 | -0.99 |
| 109 | `N38X36` VCP pecah → keluar selepas DUA | **40.1** | 25 | 25 | 23 | 30 | BELUM CUKUP | 13 | 43/20 | -5.05 | 13 | -8.15 | -0.99 | 3.7 | -2.57 | – | – |
| 110 | `M135` 3rd Watch | **40.1** | 20 | 12 | 28 | 15 | BELUM CUKUP | 9 | 15/6 | -10.80 | 26 | -7.75 | -0.91 | 4.8 | -1.64 | – | -9.37 |
| 111 | `M116` 2/20 EMA Breakout (Landry) | **40.0** | 35 | 28 | 47 | 15 | BELUM CUKUP | 26 | 614/547 | -1.50 | 26 | -4.98 | -0.37 | 8.2 | -0.94 | -0.06 | -5.38 |
| 112 | `N75X17` RSI14 < 40 tanpa penapis → kel | **39.9** | 17 | 25 | 36 | 30 | BELUM CUKUP | 13 | 466/235 | -2.98 | 13 | -9.78 | -0.76 | 5.2 | -1.62 | – | – |
| 113 | `N24X36` Supertrend(10,3) + ADX>20 → ke | **39.8** | 26 | 15 | 36 | 30 | BELUM CUKUP | 13 | 179/102 | -4.60 | 13 | -9.59 | -1.00 | 4.3 | -1.61 | – | – |
| 114 | `M12` Parabolic SAR | **39.7** | 34 | 31 | 45 | 12 | BELUM CUKUP | 26 | 407/271 | -3.66 | 26 | -4.34 | -0.66 | 3.4 | -1.13 | -0.87 | -2.82 |
| 115 | `N36X16` Pocket pivot → keluar bila sup | **39.7** | 23 | 18 | 34 | 30 | BELUM CUKUP | 13 | 174/96 | -5.50 | 13 | -8.26 | -0.75 | 4.3 | -1.94 | – | – |
| 116 | `M140` 猎豹出击 (Serangan Cheetah) | **39.7** | 22 | 23 | 32 | 11 | BELUM CUKUP | 12 | 43/24 | -5.62 | 26 | -7.96 | -0.85 | 4.8 | -1.79 | -1.11 | -2.27 |
| 117 | `M106` DMI Wilder | **39.6** | 28 | 29 | 45 | 16 | BELUM CUKUP | 22 | 133/107 | -2.82 | 26 | -6.58 | -0.87 | 3.3 | -1.04 | +0.26 | -3.25 |
| 118 | `N40X36` OBV tinggi baharu + MA50 → kel | **39.6** | 24 | 14 | 40 | 30 | BELUM CUKUP | 13 | 82/27 | -3.99 | 13 | -12.77 | -0.88 | 7.5 | -0.68 | – | – |
| 119 | `N68X16` Bullish engulfing + EMA21 → ke | **39.5** | 17 | 23 | 33 | 30 | BELUM CUKUP | 13 | 129/47 | -4.43 | 13 | -7.67 | -0.65 | 6.5 | -1.71 | – | – |
| 120 | `M128` Inventory Retracement Bar (IRB | **39.4** | 30 | 26 | 49 | 16 | BELUM CUKUP | 23 | 170/126 | -2.08 | 26 | -6.92 | -0.62 | 7.3 | -0.67 | +0.39 | -3.18 |
| 121 | `N22X36` BB pecah atas + RSI → keluar s | **39.4** | 18 | 19 | 37 | 30 | BELUM CUKUP | 13 | 122/67 | -6.21 | 13 | -9.72 | -0.84 | 5.3 | -1.35 | – | – |
| 122 | `N33X16` Donchian20 + penapis MA200 → k | **39.4** | 19 | 16 | 26 | 30 | BELUM CUKUP | 11 | 106/39 | -8.91 | 13 | -6.53 | -0.92 | 3.0 | -2.37 | – | – |
| 123 | `N57X36` ADX bangkit daripada <20 → kel | **39.4** | 19 | 17 | 22 | 30 | BELUM CUKUP | 11 | 77/21 | -8.80 | 13 | -6.00 | -0.73 | 4.1 | -2.63 | – | – |
| 124 | `M139` 均线首次粘合向上发散 (MA berhimpun kali  | **39.3** | 30 | 31 | 43 | 13 | BELUM CUKUP | 24 | 96/50 | -5.97 | 26 | -3.50 | -0.32 | 4.8 | -1.08 | -0.46 | -4.44 |
| 125 | `M119` 180 Bullish (Cooper) | **39.3** | 30 | 27 | 44 | 16 | BELUM CUKUP | 23 | 167/104 | -3.23 | 26 | -7.98 | -0.74 | 6.0 | -1.26 | +0.24 | -3.87 |
| 126 | `N28X36` ADX>25 + DI+ > DI- → keluar se | **39.3** | 15 | 22 | 38 | 30 | BELUM CUKUP | 13 | 469/352 | -1.95 | 13 | -13.28 | -1.00 | 6.0 | -1.42 | – | – |
| 127 | `N33X14` Donchian20 + penapis MA200 → k | **39.3** | 20 | 14 | 25 | 30 | BELUM CUKUP | 11 | 116/18 | -9.25 | 13 | -5.76 | -0.94 | 3.4 | -2.26 | – | – |
| 128 | `N07X36` Tiga MA tersusun → keluar sele | **39.2** | 18 | 20 | 31 | 30 | BELUM CUKUP | 13 | 166/45 | -6.30 | 13 | -6.60 | -0.83 | 4.1 | -1.95 | – | – |
| 129 | `N53X16` Supertrend + ADX>25 → keluar b | **39.1** | 18 | 18 | 33 | 30 | BELUM CUKUP | 13 | 120/31 | -6.30 | 13 | -8.71 | -0.81 | 6.2 | -1.55 | – | – |
| 130 | `N124X15` Episodic pivot gap 8-10% → eko | **39.1** | 13 | 11 | 21 | 30 | BELUM CUKUP | 9 | 42/0 | -9.87 | 13 | -12.04 | -0.88 | 5.9 | -1.41 | – | – |
| 131 | `N42X36` Lonjakan volum 2x → keluar sel | **39.0** | 18 | 16 | 37 | 30 | BELUM CUKUP | 13 | 217/129 | -2.81 | 13 | -10.63 | -1.00 | 5.6 | -1.50 | – | – |
| 132 | `N33X36` Donchian20 + penapis MA200 → k | **39.0** | 17 | 13 | 28 | 30 | BELUM CUKUP | 11 | 102/44 | -7.22 | 13 | -8.65 | -1.00 | 4.1 | -2.22 | – | – |
| 133 | `M92` CCI-50 | **38.9** | 27 | 31 | 46 | 17 | BELUM CUKUP | 26 | 585/507 | -1.93 | 26 | -9.02 | -0.67 | 5.1 | -1.05 | +0.42 | -2.81 |
| 134 | `M117` Landry Pullback (high 2 bulan) | **38.9** | 26 | 24 | 48 | 15 | BELUM CUKUP | 21 | 163/41 | -3.30 | 26 | -9.92 | -0.84 | 5.7 | -0.29 | – | -0.39 |
| 135 | `N75X14` RSI14 < 40 tanpa penapis → kel | **38.9** | 19 | 16 | 35 | 30 | BELUM CUKUP | 13 | 323/59 | -4.67 | 13 | -9.50 | -1.00 | 4.6 | -1.59 | – | – |
| 136 | `N25X17` Supertrend + EMA + ADX>23 → ke | **38.9** | 18 | 16 | 28 | 30 | BELUM CUKUP | 12 | 120/21 | -7.13 | 13 | -6.66 | -0.91 | 3.4 | -1.98 | – | – |
| 137 | `N06X36` Golden cross MA50/MA200 → kelu | **38.9** | 17 | 20 | 22 | 30 | BELUM CUKUP | 12 | 29/4 | -4.95 | 13 | -7.55 | -1.00 | 4.0 | -2.00 | – | – |
| 138 | `M49` Ichimoku (Tutup Atas Awan + Te | **38.8** | 31 | 29 | 42 | 12 | BELUM CUKUP | 26 | 333/237 | -3.58 | 26 | -6.79 | -0.60 | 4.6 | -1.47 | -0.68 | -2.57 |
| 139 | `M06` Minervini VCP Breakout | **38.8** | 28 | 29 | 42 | 15 | BELUM CUKUP | 24 | 90/55 | -4.82 | 26 | -5.39 | -0.58 | 4.0 | -1.26 | -0.01 | -3.75 |
| 140 | `M34` Carter TTM Squeeze | **38.8** | 29 | 24 | 46 | 15 | BELUM CUKUP | 22 | 106/59 | -3.36 | 26 | -7.04 | -0.55 | 5.6 | -0.78 | – | -2.33 |
| 141 | `N41X16` CMF20>0 + tutup>EMA20 → keluar | **38.8** | 16 | 21 | 29 | 30 | BELUM CUKUP | 13 | 320/240 | -4.23 | 13 | -8.21 | -0.82 | 4.3 | -2.48 | – | – |
| 142 | `N45X36` Undur EMA21 cerun positif → ke | **38.8** | 16 | 19 | 34 | 30 | BELUM CUKUP | 13 | 151/81 | -5.39 | 13 | -9.85 | -0.84 | 4.7 | -1.85 | – | – |
| 143 | `N28X16` ADX>25 + DI+ > DI- → keluar bi | **38.7** | 14 | 23 | 32 | 30 | BELUM CUKUP | 13 | 496/375 | -2.47 | 13 | -10.49 | -1.00 | 4.8 | -2.16 | – | – |
| 144 | `M149` 3-Step Pullback | **38.6** | 28 | 26 | 49 | 14 | BELUM CUKUP | 24 | 247/104 | -4.28 | 26 | -7.01 | -0.59 | 6.6 | -0.65 | -0.37 | -0.68 |
| 145 | `M04` BB Squeeze Breakout | **38.6** | 27 | 22 | 48 | 16 | BELUM CUKUP | 21 | 155/79 | -5.00 | 26 | -4.87 | -0.45 | 5.4 | -0.58 | +0.37 | -1.07 |
| 146 | `N57X16` ADX bangkit daripada <20 → kel | **38.6** | 18 | 17 | 22 | 30 | BELUM CUKUP | 12 | 75/23 | -8.76 | 13 | -6.72 | -0.75 | 4.2 | -2.63 | – | – |
| 147 | `M36` Turtle 55/20 | **38.4** | 28 | 25 | 48 | 17 | BELUM CUKUP | 25 | 350/223 | -3.49 | 26 | -7.97 | -0.57 | 7.6 | -0.84 | +0.52 | -2.10 |
| 148 | `M59` Anjakan Julat RSI | **38.4** | 20 | 17 | 38 | 15 | BELUM CUKUP | 14 | 36/24 | -7.36 | 26 | -7.24 | -0.70 | 5.4 | -1.11 | – | -3.89 |
| 149 | `N42X16` Lonjakan volum 2x → keluar bil | **38.4** | 17 | 14 | 38 | 30 | BELUM CUKUP | 13 | 220/130 | -3.09 | 13 | -10.67 | -1.00 | 5.9 | -1.47 | – | – |
| 150 | `N53X17` Supertrend + ADX>25 → keluar b | **38.4** | 19 | 15 | 30 | 30 | BELUM CUKUP | 13 | 112/11 | -6.87 | 13 | -8.65 | -0.81 | 6.0 | -1.55 | – | – |
| 151 | `N76X16` Tutup > MA50 (penapis trend tu | **38.3** | 15 | 20 | 27 | 30 | BELUM CUKUP | 13 | 351/264 | -4.06 | 13 | -8.79 | -0.95 | 3.5 | -2.77 | – | – |
| 152 | `N31X36` Turtle sistem 2 → keluar selep | **38.3** | 17 | 11 | 24 | 30 | BELUM CUKUP | 11 | 105/17 | -8.30 | 13 | -9.82 | -1.00 | 4.6 | -2.37 | – | – |
| 153 | `N37X14` Gap and go → keluar bila rsi14 | **38.3** | 12 | 10 | 25 | 30 | BELUM CUKUP | 10 | 86/15 | -8.47 | 13 | -11.81 | -0.89 | 5.9 | -2.11 | – | – |
| 154 | `M136` Short/Intermediate-term Low (L | **38.2** | 27 | 28 | 44 | 16 | BELUM CUKUP | 26 | 851/460 | -5.44 | 26 | -8.03 | -0.76 | 4.1 | -1.22 | +0.21 | -0.96 |
| 155 | `M28` VWAP Separator + Kiss Pivot | **38.1** | 28 | 26 | 42 | 12 | BELUM CUKUP | 23 | 136/122 | -2.06 | 26 | -9.72 | -1.00 | 6.0 | -1.50 | -0.90 | -12.02 |
| 156 | `N56X36` RSI>50 + ADX>20 → keluar selep | **38.0** | 16 | 15 | 30 | 30 | BELUM CUKUP | 13 | 210/134 | -4.30 | 13 | -13.14 | -1.00 | 7.0 | -2.36 | – | – |
| 157 | `N27X16` Ichimoku atas awan → keluar bi | **38.0** | 14 | 18 | 27 | 30 | BELUM CUKUP | 13 | 189/111 | -4.33 | 13 | -9.50 | -1.00 | 4.2 | -2.74 | – | – |
| 158 | `N39X36` NR7 kemudian pecah → keluar se | **38.0** | 6 | 4 | 17 | 30 | BELUM CUKUP | 8 | 35/11 | -8.51 | 12 | -15.16 | -1.00 | 8.1 | -3.41 | – | – |
| 159 | `N08X16` tutup>EMA20 tidak terlalu jauh | **37.9** | 12 | 21 | 30 | 30 | BELUM CUKUP | 13 | 524/422 | -3.35 | 13 | -11.52 | -0.99 | 4.4 | -2.43 | – | – |
| 160 | `N119X15` 3 tutup turun berturut → ekori | **37.9** | 12 | 8 | 11 | 30 | BELUM CUKUP | 9 | 58/0 | -7.73 | 13 | -11.36 | -1.00 | 6.3 | -2.59 | – | – |
| 161 | `M95` Nisbah Kebaharuan High 52 Ming | **37.8** | 24 | 25 | 43 | 14 | BELUM CUKUP | 22 | 129/78 | -3.67 | 26 | -10.04 | -0.80 | 6.5 | -1.16 | -0.18 | -2.62 |
| 162 | `N24X17` Supertrend(10,3) + ADX>20 → ke | **37.8** | 15 | 12 | 27 | 30 | BELUM CUKUP | 12 | 133/47 | -7.66 | 13 | -9.25 | -0.96 | 4.3 | -2.38 | – | – |
| 163 | `N24X16` Supertrend(10,3) + ADX>20 → ke | **37.7** | 15 | 12 | 26 | 30 | BELUM CUKUP | 12 | 125/35 | -8.82 | 13 | -9.09 | -0.99 | 4.2 | -2.37 | – | – |
| 164 | `N113X36` 80-20 bar (sisi beli) → keluar | **37.6** | 14 | 14 | 33 | 30 | BELUM CUKUP | 13 | 365/295 | -2.17 | 13 | -13.50 | -1.00 | 8.4 | -2.04 | – | – |
| 165 | `N36X14` Pocket pivot → keluar bila rsi | **37.6** | 20 | 10 | 29 | 30 | BELUM CUKUP | 13 | 175/36 | -7.67 | 13 | -10.02 | -1.00 | 5.1 | -2.11 | – | – |
| 166 | `N22X16` BB pecah atas + RSI → keluar b | **37.6** | 14 | 12 | 36 | 30 | BELUM CUKUP | 13 | 123/60 | -8.32 | 13 | -9.42 | -0.89 | 5.1 | -1.52 | – | – |
| 167 | `N54X16` Supertrend + RSI>50 → keluar b | **37.6** | 15 | 9 | 24 | 30 | BELUM CUKUP | 11 | 128/48 | -9.51 | 13 | -9.26 | -1.00 | 5.7 | -2.75 | – | – |
| 168 | `M26` Garis Trend Undur 3 Sentuhan + | **37.5** | 21 | 26 | 41 | 16 | BELUM CUKUP | 21 | 82/56 | -2.62 | 26 | -9.15 | -0.90 | 4.7 | -1.29 | +0.15 | -2.22 |
| 169 | `N56X16` RSI>50 + ADX>20 → keluar bila  | **37.5** | 13 | 15 | 32 | 30 | BELUM CUKUP | 13 | 233/143 | -4.76 | 13 | -10.42 | -1.00 | 5.2 | -2.15 | – | – |
| 170 | `N75X13` RSI14 < 40 tanpa penapis → kel | **37.5** | 14 | 16 | 25 | 30 | BELUM CUKUP | 13 | 180/1 | -5.58 | 13 | -11.46 | -0.98 | 4.9 | -1.41 | – | – |
| 171 | `M141` First Thrust (Landry) | **37.5** | 5 | 6 | 30 | 15 | BELUM CUKUP | 9 | 27/18 | -9.21 | 26 | -17.70 | -0.94 | 7.5 | -1.79 | – | -7.12 |
| 172 | `M29` EMA3 + RSI75 + Stokastik | **37.4** | 28 | 23 | 39 | 4 | BELUM CUKUP | 18 | 41/34 | -3.07 | 26 | -11.87 | -0.86 | 8.4 | -1.30 | -3.05 | -6.42 |
| 173 | `N75X15` RSI14 < 40 tanpa penapis → eko | **37.4** | 14 | 16 | 22 | 30 | BELUM CUKUP | 13 | 175/0 | -5.69 | 13 | -11.46 | -0.98 | 4.9 | -1.38 | – | – |
| 174 | `N73X13` Tutup bawah jalur bawah BB(20, | **37.3** | 14 | 15 | 24 | 30 | BELUM CUKUP | 13 | 203/1 | -5.86 | 13 | -10.70 | -0.93 | 5.8 | -1.49 | – | – |
| 175 | `N56X17` RSI>50 + ADX>20 → keluar bila  | **37.3** | 15 | 12 | 28 | 30 | BELUM CUKUP | 13 | 149/58 | -7.52 | 13 | -9.07 | -0.97 | 4.2 | -2.37 | – | – |
| 176 | `M152` Spike & Ledge | **37.2** | 22 | 26 | 38 | 15 | BELUM CUKUP | 22 | 56/14 | -6.80 | 26 | -8.03 | -0.64 | 5.0 | -1.08 | +0.06 | -3.51 |
| 177 | `M101` Bulkowski: Tiga lembah menaik | **37.2** | 24 | 14 | 42 | 15 | BELUM CUKUP | 17 | 46/25 | -5.08 | 26 | -10.46 | -0.70 | 8.8 | -0.72 | – | -1.80 |
| 178 | `N40X16` OBV tinggi baharu + MA50 → kel | **37.2** | 16 | 8 | 41 | 30 | BELUM CUKUP | 13 | 100/42 | -3.49 | 13 | -15.26 | -0.94 | 7.5 | -0.78 | – | – |
| 179 | `M55` Guppy GMMA | **37.1** | 29 | 19 | 44 | 12 | BELUM CUKUP | 24 | 245/186 | -3.74 | 26 | -10.50 | -0.91 | 6.0 | -1.18 | -0.68 | -3.34 |
| 180 | `N119X13` 3 tutup turun berturut → kelua | **37.1** | 12 | 14 | 30 | 30 | BELUM CUKUP | 13 | 273/65 | -4.18 | 13 | -11.07 | -1.00 | 7.1 | -2.22 | – | – |
| 181 | `N50X14` Mampat + pecah volum 1.5x → ke | **37.1** | 8 | 6 | 24 | 30 | BELUM CUKUP | 10 | 25/5 | -8.28 | 13 | -14.07 | -1.00 | 6.8 | -1.77 | – | – |
| 182 | `M156` Single Penetration (DiNapoli) | **37.0** | 26 | 24 | 43 | 14 | BELUM CUKUP | 26 | 287/230 | -2.37 | 26 | -8.60 | -0.59 | 7.9 | -1.39 | -0.14 | -4.47 |
| 183 | `M99` Three Line Break | **37.0** | 28 | 22 | 45 | 11 | BELUM CUKUP | 25 | 174/136 | -4.68 | 26 | -7.90 | -0.62 | 5.4 | -1.18 | -1.06 | -4.99 |
| 184 | `M107` Golden Cross SMA50/200 | **37.0** | 21 | 26 | 40 | 15 | BELUM CUKUP | 22 | 47/13 | -5.05 | 26 | -7.94 | -0.76 | 4.0 | -0.89 | – | -1.57 |
| 185 | `N29X36` PSAR naik + tutup>MA50 → kelua | **37.0** | 15 | 11 | 26 | 30 | BELUM CUKUP | 13 | 170/111 | -5.85 | 13 | -14.58 | -1.00 | 9.5 | -2.93 | – | – |
| 186 | `N113X16` 80-20 bar (sisi beli) → keluar | **36.9** | 13 | 10 | 35 | 30 | BELUM CUKUP | 13 | 383/301 | -2.06 | 13 | -14.28 | -1.00 | 9.2 | -1.74 | – | – |
| 187 | `M14` Walking with the Whales | **36.8** | 25 | 23 | 44 | 16 | BELUM CUKUP | 26 | 1056/858 | -1.99 | 26 | -13.86 | -0.85 | 8.6 | -1.32 | +0.14 | -2.64 |
| 188 | `N74X16` MACD atas garis isyarat (keada | **36.8** | 8 | 18 | 30 | 30 | BELUM CUKUP | 13 | 695/585 | -2.87 | 13 | -13.69 | -1.00 | 6.4 | -2.34 | – | – |
| 189 | `N50X17` Mampat + pecah volum 1.5x → ke | **36.7** | 6 | 6 | 25 | 30 | BELUM CUKUP | 10 | 24/5 | -8.82 | 13 | -14.98 | -0.95 | 7.7 | -1.70 | – | – |
| 190 | `N55X13` BB + RSI + ADX>20 → keluar bil | **36.6** | 15 | 14 | 16 | 30 | BELUM CUKUP | 13 | 115/0 | -5.79 | 13 | -8.98 | -0.99 | 5.1 | -2.14 | – | – |
| 191 | `N54X36` Supertrend + RSI>50 → keluar s | **36.6** | 16 | 8 | 31 | 30 | BELUM CUKUP | 13 | 188/122 | -5.11 | 13 | -14.28 | -1.00 | 8.5 | -2.29 | – | – |
| 192 | `M66` IBD Undur Pertama ke Purata 50 | **36.5** | 27 | 19 | 44 | 14 | BELUM CUKUP | 25 | 266/197 | -3.40 | 26 | -8.79 | -0.67 | 7.9 | -1.24 | -0.38 | -3.37 |
| 193 | `M155` Market Cycle Strategy | **36.3** | 25 | 20 | 43 | 18 | BELUM CUKUP | 26 | 779/564 | -5.48 | 26 | -8.95 | -0.76 | 5.5 | -1.38 | +0.66 | -4.72 |
| 194 | `M50` Elder Triple Screen | **36.3** | 24 | 21 | 45 | 16 | BELUM CUKUP | 26 | 651/495 | -2.48 | 26 | -13.55 | -1.00 | 7.5 | -1.20 | +0.28 | -2.45 |
| 195 | `N16X13` RSI2<10 tanpa penapis → keluar | **36.3** | 9 | 14 | 26 | 30 | BELUM CUKUP | 13 | 292/6 | -4.94 | 13 | -13.25 | -1.00 | 7.6 | -1.73 | – | – |
| 196 | `N42X14` Lonjakan volum 2x → keluar bil | **36.2** | 14 | 7 | 33 | 30 | BELUM CUKUP | 13 | 199/27 | -6.46 | 13 | -12.30 | -1.00 | 6.6 | -1.49 | – | – |
| 197 | `N42X15` Lonjakan volum 2x → ekori Chan | **36.1** | 14 | 8 | 22 | 33 | BELUM CUKUP | 13 | 184/0 | -7.67 | 13 | -12.12 | -0.90 | 6.7 | -1.48 | – | – |
| 198 | `N22X14` BB pecah atas + RSI → keluar b | **36.0** | 12 | 8 | 28 | 30 | BELUM CUKUP | 13 | 129/29 | -9.04 | 13 | -11.86 | -0.98 | 6.3 | -2.07 | – | – |
| 199 | `N27X36` Ichimoku atas awan → keluar se | **36.0** | 12 | 9 | 26 | 30 | BELUM CUKUP | 13 | 115/41 | -7.44 | 13 | -12.74 | -1.00 | 5.7 | -2.52 | – | – |
| 200 | `N28X17` ADX>25 + DI+ > DI- → keluar bi | **36.0** | 12 | 9 | 23 | 30 | BELUM CUKUP | 13 | 154/8 | -8.47 | 13 | -11.63 | -0.95 | 6.0 | -2.20 | – | – |
| 201 | `M57` Landry Trend Knockout (TKO) | **35.9** | 29 | 23 | 37 | 7 | BELUM CUKUP | 26 | 192/150 | -3.41 | 26 | -8.74 | -1.00 | 4.8 | -2.10 | -2.04 | -5.34 |
| 202 | `N29X16` PSAR naik + tutup>MA50 → kelua | **35.9** | 11 | 9 | 26 | 30 | BELUM CUKUP | 13 | 225/143 | -6.24 | 13 | -11.70 | -1.00 | 6.6 | -3.07 | – | – |
| 203 | `M19` Sneaky Pivot (proksi harian) | **35.8** | 22 | 22 | 43 | 11 | BELUM CUKUP | 25 | 438/337 | -5.59 | 26 | -10.45 | -0.70 | 5.9 | -1.32 | -1.10 | -21.32 |
| 204 | `N47X16` NR7 + EMA9>EMA21 → keluar bila | **35.7** | 8 | 12 | 26 | 30 | BELUM CUKUP | 13 | 206/85 | -5.82 | 13 | -13.83 | -1.00 | 7.3 | -2.85 | – | – |
| 205 | `N28X14` ADX>25 + DI+ > DI- → keluar bi | **35.4** | 9 | 8 | 28 | 30 | BELUM CUKUP | 13 | 222/27 | -7.87 | 13 | -14.01 | -0.93 | 6.9 | -2.13 | – | – |
| 206 | `M125` 2-Bar Breakout | **34.9** | 21 | 19 | 42 | 13 | BELUM CUKUP | 26 | 1147/647 | -5.85 | 26 | -11.48 | -0.79 | 5.9 | -1.48 | -0.44 | -1.01 |
| 207 | `M154` HOLP (High of Low Period) | **34.9** | 16 | 13 | 38 | 11 | BELUM CUKUP | 18 | 96/50 | -6.83 | 26 | -15.19 | -0.99 | 8.5 | -1.57 | -1.01 | -7.08 |
| 208 | `M47` Holy Grail Raschke | **34.9** | 12 | 14 | 27 | 15 | BELUM CUKUP | 16 | 38/34 | -3.55 | 26 | -12.95 | -0.98 | 7.5 | -2.58 | – | -20.75 |
| 209 | `N42X17` Lonjakan volum 2x → keluar bil | **34.8** | 9 | 4 | 36 | 30 | BELUM CUKUP | 13 | 215/73 | -5.20 | 13 | -14.83 | -1.00 | 7.8 | -1.51 | – | – |
| 210 | `M31` Band Walk (BB 20/2) | **34.7** | 22 | 13 | 49 | 17 | BELUM CUKUP | 25 | 404/153 | -4.12 | 26 | -9.55 | -0.58 | 8.7 | -0.71 | +0.60 | -1.55 |
| 211 | `N16X15` RSI2<10 tanpa penapis → ekori  | **34.6** | 7 | 8 | 19 | 30 | BELUM CUKUP | 13 | 264/0 | -5.33 | 13 | -14.60 | -1.00 | 9.8 | -1.82 | – | – |
| 212 | `M147` Improved Three-Bar Pullback | **33.7** | 9 | 16 | 34 | 15 | BELUM CUKUP | 18 | 119/58 | -8.02 | 26 | -17.49 | -0.82 | 7.9 | -2.08 | – | -2.48 |
| 213 | `M09` Volumatic VIDYA Pivot Retest | **33.7** | 10 | 7 | 27 | 15 | BELUM CUKUP | 15 | 40/30 | -6.75 | 26 | -19.38 | -1.00 | 10.4 | -2.58 | – | -14.85 |
| 214 | `M73` ADX(5) > 40 + Julat Terkecil 6 | **33.5** | 21 | 13 | 44 | 13 | BELUM CUKUP | 26 | 1126/918 | -1.42 | 26 | -12.63 | -1.00 | 7.4 | -1.33 | -0.48 | -9.02 |
| 215 | `M11` NR7 Breakout + Volume | **33.5** | 13 | 17 | 39 | 15 | BELUM CUKUP | 23 | 128/93 | -2.11 | 26 | -14.01 | -0.82 | 9.2 | -1.74 | – | -1.81 |
| 216 | `M03` BB Break + Divergence RSI | **33.4** | 13 | 22 | 44 | 14 | BELUM CUKUP | 26 | 447/400 | -2.87 | 26 | -12.65 | -0.85 | 5.5 | -1.24 | -0.23 | -6.35 |
| 217 | `N47X36` NR7 + EMA9>EMA21 → keluar sele | **33.2** | 0 | 5 | 25 | 30 | BELUM CUKUP | 12 | 186/68 | -6.68 | 13 | -19.57 | -1.00 | 10.3 | -3.58 | – | – |
| 218 | `M79` Radge: 20% Flipper | **33.0** | 16 | 17 | 40 | 13 | BELUM CUKUP | 26 | 396/203 | -8.03 | 26 | -12.59 | -0.79 | 7.9 | -1.76 | -0.63 | -4.58 |
| 219 | `M81` Bensdorp Long Trend High Momen | **32.2** | 1 | 4 | 37 | 15 | BELUM CUKUP | 13 | 432/211 | -7.71 | 26 | -25.69 | -0.97 | 16.1 | -1.79 | – | -5.76 |
| 220 | `M82` Arthur Hill Rotasi Sasaran 10% | **32.1** | 20 | 8 | 44 | 17 | BELUM CUKUP | 26 | 604/266 | -4.23 | 26 | -11.80 | -0.60 | 11.2 | -1.27 | +0.62 | -5.81 |
| 221 | `M122` Moving Momentum (ChartSchool) | **31.7** | 14 | 14 | 33 | 10 | BELUM CUKUP | 25 | 115/79 | -6.61 | 26 | -16.79 | -1.00 | 7.8 | -2.45 | -1.20 | -8.53 |
| 222 | `M76` Undercut & Rally pada Low Pent | **31.6** | 10 | 17 | 36 | 4 | BELUM CUKUP | 22 | 84/77 | -3.76 | 26 | -14.73 | -1.00 | 8.0 | -2.06 | -2.98 | -8.81 |
| 223 | `M123` CCI Correction (Lambert, Chart | **31.1** | 8 | 22 | 31 | 12 | BELUM CUKUP | 25 | 194/184 | -2.30 | 26 | -16.84 | -1.00 | 8.4 | -2.77 | -0.85 | -6.58 |
| 224 | `M01` Bollinger Band + RSI | **30.7** | 11 | 7 | 40 | 18 | BELUM CUKUP | 23 | 123/27 | -5.78 | 26 | -16.76 | -1.00 | 6.5 | -1.20 | +0.84 | -5.19 |
| 225 | `M20` EMA10/15 Crossover + Sudut | **30.0**⌈ | 29 | 30 | 41 | 10 | GAGAL | 26 | 532/483 | -2.16 | 26 | -9.12 | -0.82 | 4.6 | -1.62 | -1.28 | -12.06 |
| 226 | `M161` EMA 10/21 + Supertrend (10,3) | **30.0** | 9 | 9 | 46 | 18 | BELUM CUKUP | 26 | 523/323 | -3.04 | 26 | -20.75 | -0.94 | 11.8 | -1.10 | +0.72 | -2.90 |
| 227 | `M90` Pring KST | **29.7** | 8 | 12 | 40 | 6 | BELUM CUKUP | 25 | 94/58 | -5.17 | 26 | -17.03 | -0.85 | 12.8 | -1.52 | -2.54 | -5.91 |

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

