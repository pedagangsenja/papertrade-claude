# Skor Kaedah 0–100 (pangkat maklumat, BUKAN keputusan)

> **Status keputusan (kad skor, harga 2026-11-19):** TERBUKTI 0 · CALON 0 · BELUM CUKUP 225 · GAGAL 1 · NEGATIF 0. Rejim QQQ OFF sejak 2026-10-16. Hanya **TERBUKTI** layak untuk wang sebenar (`laporan/KAD_SKOR.md`); nombor dalam laporan ini BUKAN keputusan dan tidak boleh dibaca sebagai pangkat untuk wang sebenar.

Dijana 2026-11-20 oleh `standard/skor_kaedah.py` (Actions `analisis.yml`, selepas kad skor). Harga pada tutup 2026-11-19; 226 kaedah; 25 hari beli langsung (rejim ON 1, OFF 24). Pradaftar 2026-11-09: `standard/SPEC_SKOR_KAEDAH.md` (berat dan sauh dikunci `ujian/test_skor_kaedah.py::TestKunci`). Rekod analisis sahaja: tiada order, tiada wang sebenar.

## Cara membaca

- **Skor** = min geometri berberat empat tiang (Untung 35 · Tahan 30 · Bukti 25 · Konsisten 10), dikecut ke 50 mengikut data: berat data = hari beli ÷ (hari beli + 20). Kaedah dengan 2 hari beli tidak boleh menjauhi 50. 100 = unggul semua segi; 50 = neutral/tiada bukti; < 50 = lebih buruk daripada neutral.
- **Siling** ikut kad skor: NEGATIF ≤ 20, GANTUNG/BERSARA ≤ 30, GAGAL ≤ 40. Tanda ⌈ = siling terpakai.
- **Satu-satunya status yang membenarkan wang sebenar ialah TERBUKTI dalam `laporan/KAD_SKOR.md`.** Skor tinggi dengan status BELUM CUKUP bermaksud "paling menjanjikan setakat ini", bukan "selamat".
- Deflasi ujian berganda (López de Prado): sauh t Bukti C1 = maks(2.0, E[maks 226 normal]) = 2.81.
- **Semakan kebolehramalan:** skor pada 2026-11-12 lawan pulangan lorong T4 sejak itu, 223 kaedah: Spearman ρ = -0.013 (p = 0.845). Belum ada bukti skor meramal pangkat; jangan pilih kaedah dengannya.
- Metrik T4 (A2, B1, B2, D1) dikira atas lorong T4 L1 **dipotong pada sesi LANGSUNG pertama** kaedah itu (Mxx 2026-10-16, Nxx/GB 2026-11-03) dan diasas semula; sesi isian bina semula tidak dikira (pindaan 9 Nov 2026 (a)). Lajur "T4 sesi/pul" di bawah ialah potongan itu, bukan lorong penuh `T4_KAEDAH.md`.

## Semua kaedah, susun ikut Skor

| # | Kaedah | Skor | Untung | Tahan | Bukti | Konsisten | Status kad | Hari beli | Posisi/tutup | Jangkaan % | T4 sesi | T4 pul % | T4 pul/|MDD| | Ulcer | t buku | Lift | WFE |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `M151` Outside Bar Failure | **55.0** | 54 | 78 | 51 | 55 | BELUM CUKUP | 23 | 115/72 | -1.25 | 25 | +5.57 | +2.14 | 0.8 | -0.28 | – | -0.58 |
| 2 | `M146` 3-Bar Momentum Pattern | **54.4** | 54 | 63 | 54 | 82 | BELUM CUKUP | 20 | 80/40 | -0.84 | 25 | +3.81 | +0.62 | 2.9 | +0.41 | – | 0.90 |
| 3 | `M133` Bull Hook (Crabel) | **53.6** | 50 | 62 | 57 | 85 | BELUM CUKUP | 16 | 54/39 | -1.08 | 25 | +2.18 | +0.41 | 2.2 | +0.81 | – | 6.99 |
| 4 | `M159` Heikin-Ashi Trend | **51.2** | 52 | 59 | 44 | 55 | BELUM CUKUP | 25 | 1880/1765 | -0.95 | 25 | +3.42 | +0.56 | 3.6 | -1.23 | – | -7.60 |
| 5 | `M104` High Tight Flag / Power Play | **51.0** | 83 | 90 | 40 | 85 | BELUM CUKUP | 1 | 1/0 | +20.32 | 10 | +2.05 | +7.81 | 0.1 | +1.54 | – | 11.18 |
| 6 | `N28X36` ADX>25 + DI+ > DI- → keluar se | **50.6** | 46 | 68 | 39 | 70 | BELUM CUKUP | 12 | 436/309 | -1.34 | 12 | +58.73 | +9.37 | 3.6 | -1.26 | – | – |
| 7 | `M48` Cooper 1-2-3-4 | **49.9** | 40 | 60 | 50 | 61 | BELUM CUKUP | 20 | 69/23 | -2.08 | 25 | +6.82 | +1.25 | 2.3 | +0.09 | – | 0.21 |
| 8 | `M160` Measured Move Up | **49.6** | 34 | 55 | 58 | 85 | BELUM CUKUP | 23 | 129/89 | -2.41 | 25 | +0.63 | +0.13 | 2.4 | +0.48 | – | 3.48 |
| 9 | `M13` Garis Trend Action/Safety Line | **49.4** | 39 | 66 | 45 | 55 | BELUM CUKUP | 25 | 855/626 | -2.56 | 25 | +4.69 | +0.97 | 1.7 | -1.15 | – | -2.99 |
| 10 | `M118` Expansion Pivot (Cooper) | **49.3** | 39 | 59 | 50 | 55 | BELUM CUKUP | 20 | 85/35 | -1.81 | 25 | +3.89 | +0.55 | 2.4 | -0.03 | – | -0.11 |
| 11 | `M07` Qullamaggie Breakout | **49.3** | 32 | 64 | 27 | 15 | BELUM CUKUP | 1 | 1/1 | -2.53 | 25 | -0.25 | -0.21 | 0.9 | -0.22 | – | -1.12 |
| 12 | `M25` VWAP Wave (proksi harian) | **49.2** | 49 | 57 | 54 | 22 | BELUM CUKUP | 23 | 199/148 | -1.34 | 25 | +2.13 | +0.32 | 3.7 | -0.04 | – | -0.23 |
| 13 | `M45` High 52 Minggu (George & Hwang | **49.2** | 22 | 44 | 32 | 54 | BELUM CUKUP | 1 | 2/1 | -3.49 | 14 | -0.68 | -0.37 | 0.9 | +0.32 | – | 0.82 |
| 14 | `M10` EMA3 + CCI + MACD | **48.7** | 38 | 59 | 48 | 55 | BELUM CUKUP | 22 | 127/71 | -3.33 | 25 | +7.43 | +1.41 | 2.4 | -0.55 | – | -1.71 |
| 15 | `M27` Price Action 4 Tiang | **48.4** | 35 | 33 | 36 | 15 | BELUM CUKUP | 2 | 546/492 | -1.51 | 25 | -3.95 | -0.77 | 3.0 | -1.18 | – | -4.27 |
| 16 | `M84` Jarak purata bergerak MAD 21/2 | **48.4** | 19 | 11 | 28 | 15 | BELUM CUKUP | 1 | 58/40 | -5.22 | 14 | -8.76 | -1.00 | 6.8 | -1.29 | – | -3.37 |
| 17 | `M96` Momo India: Ranking Sharpe 3/6 | **48.2** | 18 | 7 | 9 | 15 | BELUM CUKUP | 1 | 6/6 | -13.71 | 14 | -8.21 | -1.00 | 7.1 | -5.92 | – | -15.55 |
| 18 | `M51` O'Neil Cawan & Pemegang | **48.0** | 22 | 45 | 30 | 15 | BELUM CUKUP | 2 | 3/1 | -3.26 | 15 | -0.94 | -0.68 | 0.7 | -0.14 | – | -0.52 |
| 19 | `M137` Livermore System | **47.8** | 37 | 52 | 50 | 55 | BELUM CUKUP | 24 | 183/83 | -3.16 | 25 | +2.36 | +0.40 | 2.3 | -0.49 | – | -0.99 |
| 20 | `M94` Pecutan Momentum (Chen, Yu & W | **47.8** | 0 | 2 | 13 | 15 | BELUM CUKUP | 1 | 33/0 | -14.18 | 14 | -17.42 | -1.00 | 8.9 | -1.65 | – | -5.16 |
| 21 | `N28X16` ADX>25 + DI+ > DI- → keluar bi | **47.6** | 33 | 68 | 31 | 70 | BELUM CUKUP | 12 | 461/322 | -1.86 | 12 | +61.58 | +9.82 | 3.1 | -2.18 | – | – |
| 22 | `M46` Jurang Naik Boleh Beli (Buyabl | **47.4** | 34 | 54 | 43 | 55 | BELUM CUKUP | 13 | 36/25 | -2.21 | 25 | -0.39 | -0.08 | 1.7 | -0.52 | – | -0.86 |
| 23 | `N202X36` RSI2<10 dalam trend naik x X36 | **47.4** | 31 | 65 | 19 | 70 | BELUM CUKUP | 5 | 80/5 | -1.66 | 5 | +0.56 | +0.34 | 0.9 | -2.11 | – | – |
| 24 | `M78` Alvarez Pecahan Mingguan DTAYS | **47.4** | 16 | 20 | 36 | 15 | BELUM CUKUP | 2 | 73/45 | -3.78 | 24 | -8.85 | -0.79 | 7.8 | -0.63 | – | -2.02 |
| 25 | `M70` Pecahan Hari Dalam | **47.2** | 52 | 52 | 49 | 15 | BELUM CUKUP | 25 | 500/433 | -1.00 | 25 | -1.17 | -0.23 | 2.3 | -0.66 | – | -1.62 |
| 26 | `M74` Lulus Baharu Trend Template Mi | **47.2** | 41 | 50 | 50 | 35 | BELUM CUKUP | 25 | 106/76 | -1.78 | 25 | -0.85 | -0.13 | 3.0 | -0.47 | – | -0.85 |
| 27 | `M129` Wick Play | **46.8** | 34 | 45 | 41 | 55 | BELUM CUKUP | 10 | 25/9 | -2.96 | 25 | +1.11 | +0.24 | 1.7 | -0.30 | – | -1.08 |
| 28 | `M145` Yum-Yum Continuation | **46.7** | 32 | 55 | 49 | 55 | BELUM CUKUP | 23 | 311/89 | -3.53 | 25 | +1.81 | +0.55 | 1.4 | -0.63 | – | -0.58 |
| 29 | `M23` Breitstein Kapitulasi + Kesina | **46.7** | 44 | 46 | 54 | 21 | BELUM CUKUP | 23 | 130/93 | -1.45 | 25 | -2.21 | -0.38 | 2.9 | +0.05 | – | 0.19 |
| 30 | `M37` Weinstein Peringkat 2 | **46.6** | 20 | 44 | 19 | 15 | BELUM CUKUP | 3 | 7/0 | -3.61 | 19 | -2.38 | -0.70 | 1.1 | -1.19 | – | -1.69 |
| 31 | `M64` O'Neil Tiga Minggu Ketat | **46.5** | 27 | 22 | 25 | 15 | BELUM CUKUP | 3 | 3/3 | -12.60 | 25 | -3.76 | -0.84 | 2.9 | -1.26 | – | -14.58 |
| 32 | `M33` Supertrend + SMA10 | **46.4** | 32 | 48 | 52 | 55 | BELUM CUKUP | 23 | 224/86 | -3.17 | 25 | +2.52 | +0.35 | 2.3 | -0.20 | – | -1.10 |
| 33 | `N25X36` Supertrend + EMA + ADX>23 → ke | **46.2** | 32 | 45 | 36 | 70 | BELUM CUKUP | 11 | 138/50 | -3.12 | 12 | -0.93 | -0.21 | 2.0 | -1.32 | – | – |
| 34 | `M100` Bulkowski Segi Empat & Segi Ti | **46.1** | 40 | 39 | 47 | 42 | BELUM CUKUP | 17 | 61/43 | -1.20 | 25 | -2.40 | -0.33 | 2.7 | -0.40 | – | -2.09 |
| 35 | `M21` Marius 3 Persediaan (Pecahan+J | **45.9** | 23 | 44 | 35 | 15 | BELUM CUKUP | 5 | 5/4 | -3.52 | 17 | -1.74 | -0.65 | 1.7 | -0.20 | – | -0.33 |
| 36 | `M138` 直升机空中加油 (Helikopter isi minyak | **45.9** | 30 | 41 | 14 | 15 | BELUM CUKUP | 4 | 4/0 | -3.26 | 18 | -1.22 | -0.86 | 0.7 | -1.84 | – | -2.40 |
| 37 | `M39` Radge Pecahan Bollinger 100 ha | **45.6** | 32 | 48 | 46 | 55 | BELUM CUKUP | 23 | 244/59 | -4.84 | 25 | +1.96 | +0.35 | 1.7 | -0.82 | – | -1.75 |
| 38 | `M05` MACD Divergence + Pengesahan | **45.6** | 34 | 46 | 38 | 55 | BELUM CUKUP | 16 | 42/13 | -3.46 | 25 | -0.88 | -0.16 | 2.1 | -0.98 | – | -1.82 |
| 39 | `M77` Undercut & Rally pada Purata B | **45.4** | 35 | 41 | 43 | 55 | BELUM CUKUP | 18 | 55/39 | -1.64 | 25 | -4.03 | -0.62 | 2.2 | -0.89 | – | -1.21 |
| 40 | `N203X36` Gap 2% lalu MA20 silang MA50 x | **45.4** | 19 | 33 | 14 | 30 | BELUM CUKUP | 4 | 12/1 | -5.34 | 5 | -5.76 | -0.91 | 3.5 | -2.15 | – | – |
| 41 | `M35` Pocket Pivot Morales & Kacher | **45.1** | 51 | 37 | 51 | 15 | BELUM CUKUP | 24 | 330/282 | -0.77 | 25 | -4.16 | -0.45 | 5.5 | -0.43 | – | -2.33 |
| 42 | `M157` Consolidation Pivot Breakout ( | **44.8** | 26 | 33 | 29 | 15 | BELUM CUKUP | 6 | 8/3 | -3.08 | 22 | -2.35 | -0.78 | 1.8 | -0.88 | – | -2.03 |
| 43 | `M87` IBD Tapak Menaik | **44.7** | 32 | 33 | 39 | 15 | BELUM CUKUP | 8 | 11/8 | -3.86 | 25 | -4.22 | -0.54 | 4.4 | -0.42 | – | -1.23 |
| 44 | `M144` Screw Bar | **44.6** | 28 | 34 | 34 | 15 | BELUM CUKUP | 7 | 10/7 | -2.21 | 23 | -2.14 | -0.71 | 1.4 | -0.67 | – | -1.15 |
| 45 | `M132` Ascending Scallop (Bulkowski) | **44.5** | 31 | 42 | 46 | 40 | BELUM CUKUP | 18 | 96/43 | -3.82 | 25 | -0.89 | -0.13 | 2.7 | -0.56 | – | -3.92 |
| 46 | `M121` High 2 bull flag (Brooks) | **44.4** | 15 | 16 | 20 | 15 | BELUM CUKUP | 4 | 6/3 | -9.93 | 21 | -5.86 | -0.82 | 4.6 | -1.82 | – | -17.80 |
| 47 | `M38` Darvas Kotak | **44.2** | 18 | 19 | 32 | 15 | BELUM CUKUP | 5 | 26/1 | -4.89 | 24 | -5.17 | -0.48 | 6.0 | -0.14 | – | -0.59 |
| 48 | `M124` 'Last' Stochastic Technique (C | **44.1** | 30 | 41 | 48 | 55 | BELUM CUKUP | 25 | 413/284 | -2.79 | 25 | -1.83 | -0.23 | 3.3 | -0.73 | – | -1.97 |
| 49 | `N53X36` Supertrend + ADX>25 → keluar s | **44.0** | 30 | 33 | 44 | 30 | BELUM CUKUP | 12 | 142/51 | -1.97 | 12 | -4.77 | -0.68 | 3.3 | -0.40 | – | – |
| 50 | `M41` FW Penyatuan Mingguan | **43.9** | 13 | 20 | 38 | 15 | BELUM CUKUP | 5 | 67/11 | -3.06 | 24 | -8.61 | -0.78 | 5.8 | -0.21 | – | -0.35 |
| 51 | `N201X36` MA20 silang MA50 atas MA50 x X | **43.9** | 14 | 34 | 13 | 30 | BELUM CUKUP | 5 | 24/4 | -3.87 | 5 | -4.19 | -0.99 | 2.4 | -4.83 | – | – |
| 52 | `N45X16` Undur EMA21 cerun positif → ke | **43.7** | 24 | 44 | 40 | 30 | BELUM CUKUP | 12 | 176/95 | -3.14 | 12 | +0.31 | +0.05 | 2.7 | -1.18 | – | – |
| 53 | `M115` Bow Tie (Landry) | **43.6** | 30 | 36 | 46 | 15 | BELUM CUKUP | 12 | 37/28 | -2.55 | 25 | -4.55 | -0.52 | 5.1 | -0.13 | – | -0.67 |
| 54 | `N37X36` Gap and go → keluar selepas DU | **43.1** | 23 | 27 | 30 | 51 | BELUM CUKUP | 9 | 85/32 | -4.52 | 12 | -1.68 | -0.33 | 3.1 | -1.78 | – | – |
| 55 | `N48X36` Inside day pecah → keluar sele | **43.0** | 28 | 24 | 37 | 70 | BELUM CUKUP | 12 | 338/243 | -1.17 | 12 | -7.23 | -0.86 | 5.3 | -1.50 | – | – |
| 56 | `M153` Range Leader | **42.9** | 45 | 32 | 49 | 15 | BELUM CUKUP | 25 | 1435/1314 | -0.54 | 25 | -6.30 | -0.51 | 8.0 | -0.64 | – | -4.45 |
| 57 | `N36X36` Pocket pivot → keluar selepas  | **42.9** | 26 | 27 | 33 | 70 | BELUM CUKUP | 12 | 168/93 | -3.98 | 12 | -3.22 | -0.49 | 3.1 | -1.92 | – | – |
| 58 | `N37X17` Gap and go → keluar bila adx14 | **42.9** | 23 | 26 | 29 | 42 | BELUM CUKUP | 9 | 85/34 | -4.36 | 12 | -1.95 | -0.35 | 3.3 | -1.92 | – | – |
| 59 | `N75X17` RSI14 < 40 tanpa penapis → kel | **42.8** | 22 | 33 | 38 | 48 | BELUM CUKUP | 12 | 399/216 | -1.88 | 12 | -4.96 | -0.60 | 3.9 | -1.46 | – | – |
| 60 | `N65X14` Gap 4% + volum + hampir 52w →  | **42.8** | 19 | 14 | 23 | 30 | BELUM CUKUP | 6 | 31/4 | -5.55 | 12 | -5.50 | -1.00 | 3.2 | -1.66 | – | – |
| 61 | `N65X36` Gap 4% + volum + hampir 52w →  | **42.8** | 19 | 14 | 23 | 30 | BELUM CUKUP | 6 | 31/4 | -5.80 | 12 | -5.21 | -1.00 | 3.2 | -1.68 | – | – |
| 62 | `M02` MACD + SMA200 | **42.6** | 34 | 31 | 44 | 55 | BELUM CUKUP | 25 | 136/103 | -3.96 | 25 | -1.34 | -0.11 | 4.7 | -1.30 | – | -8.85 |
| 63 | `N19X13` Bawah jalur BB + RSI<30 → kelu | **42.6** | 21 | 27 | 24 | 31 | BELUM CUKUP | 8 | 113/0 | -3.31 | 12 | -4.00 | -0.76 | 3.1 | -1.02 | – | – |
| 64 | `M158` Doubly Adaptive Profit Targets | **42.4** | 33 | 33 | 55 | 21 | BELUM CUKUP | 23 | 384/172 | -1.67 | 25 | -4.47 | -0.53 | 4.1 | +0.08 | – | 0.20 |
| 65 | `M44` Tapak Rata IBD | **42.4** | 22 | 36 | 18 | 15 | BELUM CUKUP | 8 | 9/7 | -5.66 | 25 | -5.01 | -0.87 | 3.3 | -2.83 | – | -39.23 |
| 66 | `N64X17` Episodic pivot → keluar bila a | **42.4** | 20 | 20 | 31 | 30 | BELUM CUKUP | 8 | 50/15 | -3.92 | 12 | -3.57 | -0.67 | 3.2 | -1.34 | – | – |
| 67 | `M148` Natural Number Method | **42.3** | 30 | 43 | 38 | 35 | BELUM CUKUP | 25 | 232/207 | -2.89 | 25 | -1.93 | -0.23 | 3.6 | -1.91 | – | -7.43 |
| 68 | `M88` O'Neil Shakeout +3 | **42.3** | 28 | 37 | 45 | 28 | BELUM CUKUP | 19 | 84/45 | -4.10 | 25 | -3.27 | -0.24 | 6.5 | -0.72 | – | -1.26 |
| 69 | `N25X16` Supertrend + EMA + ADX>23 → ke | **42.3** | 21 | 35 | 28 | 44 | BELUM CUKUP | 11 | 122/20 | -5.00 | 12 | -2.27 | -0.47 | 2.6 | -1.89 | – | – |
| 70 | `N64X36` Episodic pivot → keluar selepa | **42.1** | 18 | 20 | 30 | 32 | BELUM CUKUP | 8 | 50/9 | -4.02 | 12 | -3.72 | -0.66 | 3.2 | -1.18 | – | – |
| 71 | `M130` 多方炮 (dua lilin hijau mengapit  | **42.1** | 27 | 16 | 32 | 15 | BELUM CUKUP | 8 | 12/4 | -6.19 | 23 | -7.16 | -0.77 | 4.5 | -0.76 | – | -0.66 |
| 72 | `M08` SMA20 + SMA200 | **42.0** | 28 | 31 | 47 | 54 | BELUM CUKUP | 23 | 262/173 | -2.15 | 25 | -5.25 | -0.98 | 3.7 | -0.87 | – | -2.30 |
| 73 | `M68` Kell Base n' Break | **42.0** | 30 | 35 | 43 | 15 | BELUM CUKUP | 16 | 52/17 | -4.37 | 25 | -2.90 | -0.43 | 2.7 | -0.51 | – | -3.14 |
| 74 | `N68X36` Bullish engulfing + EMA21 → ke | **42.0** | 21 | 34 | 36 | 30 | BELUM CUKUP | 12 | 130/27 | -3.12 | 12 | -4.36 | -0.55 | 4.1 | -1.16 | – | – |
| 75 | `M18` EMA9/21 Pullback | **41.9** | 40 | 30 | 49 | 15 | BELUM CUKUP | 25 | 473/382 | -1.01 | 25 | -9.02 | -1.00 | 4.6 | -0.62 | – | -2.23 |
| 76 | `M120` Reversal New Highs | **41.8** | 28 | 30 | 39 | 15 | BELUM CUKUP | 13 | 19/12 | -2.78 | 25 | -4.52 | -0.69 | 3.6 | -0.73 | – | -4.24 |
| 77 | `N35X36` Pecah 52 minggu tinggi → kelua | **41.7** | 19 | 25 | 23 | 44 | BELUM CUKUP | 9 | 50/5 | -6.32 | 12 | -2.26 | -0.60 | 1.6 | -1.88 | – | – |
| 78 | `N43X36` Undur EMA8 + penapis MA50 → ke | **41.6** | 25 | 25 | 34 | 30 | BELUM CUKUP | 12 | 213/73 | -3.87 | 12 | -4.80 | -0.86 | 3.0 | -1.75 | – | – |
| 79 | `N37X16` Gap and go → keluar bila super | **41.6** | 20 | 20 | 28 | 30 | BELUM CUKUP | 9 | 85/33 | -4.75 | 12 | -2.94 | -0.72 | 2.7 | -1.97 | – | – |
| 80 | `N64X14` Episodic pivot → keluar bila r | **41.6** | 18 | 16 | 30 | 30 | BELUM CUKUP | 8 | 50/7 | -4.12 | 12 | -4.65 | -0.93 | 2.7 | -1.17 | – | – |
| 81 | `M116` 2/20 EMA Breakout (Landry) | **41.5** | 38 | 32 | 48 | 15 | BELUM CUKUP | 25 | 611/527 | -1.20 | 25 | -2.60 | -0.21 | 8.0 | -0.72 | – | -3.54 |
| 82 | `N64X16` Episodic pivot → keluar bila s | **41.5** | 17 | 16 | 31 | 30 | BELUM CUKUP | 8 | 50/11 | -3.91 | 12 | -4.72 | -0.93 | 2.8 | -1.20 | – | – |
| 83 | `M15` Break & Retest + Henti ATR | **41.4** | 37 | 31 | 50 | 15 | BELUM CUKUP | 25 | 322/252 | -0.98 | 25 | -8.92 | -0.71 | 5.5 | -0.52 | – | -1.25 |
| 84 | `N41X36` CMF20>0 + tutup>EMA20 → keluar | **41.4** | 22 | 30 | 32 | 30 | BELUM CUKUP | 12 | 272/196 | -2.76 | 12 | -6.66 | -0.88 | 3.7 | -2.08 | – | – |
| 85 | `M91` Stochastic Pop (Bernstein/Stec | **41.3** | 27 | 22 | 47 | 38 | BELUM CUKUP | 16 | 39/30 | -4.24 | 25 | -3.98 | -0.25 | 6.4 | -0.22 | – | -0.99 |
| 86 | `N51X16` BB squeeze + Supertrend → kelu | **41.3** | 13 | 29 | 18 | 30 | BELUM CUKUP | 8 | 14/3 | -4.84 | 12 | -6.26 | -0.93 | 3.5 | -2.29 | – | – |
| 87 | `M142` Pecahan volum dari dasar (底部放量 | **41.2** | 22 | 31 | 40 | 55 | BELUM CUKUP | 17 | 55/11 | -3.29 | 23 | -1.27 | -0.18 | 2.7 | -0.44 | – | -0.83 |
| 88 | `N51X36` BB squeeze + Supertrend → kelu | **41.2** | 13 | 29 | 17 | 30 | BELUM CUKUP | 8 | 14/3 | -4.83 | 12 | -6.28 | -0.93 | 3.4 | -2.37 | – | – |
| 89 | `M111` Sistem Volatiliti Wilder | **41.1** | 28 | 34 | 50 | 24 | BELUM CUKUP | 25 | 275/133 | -3.18 | 25 | -2.30 | -0.24 | 4.3 | -0.50 | – | -1.47 |
| 90 | `M89` Chande 65sma-3cc | **41.1** | 30 | 37 | 48 | 15 | BELUM CUKUP | 23 | 194/118 | -3.62 | 25 | -3.19 | -0.29 | 4.6 | -0.78 | – | -2.76 |
| 91 | `M54` IBD Power Trend | **41.1** | 30 | 37 | 46 | 15 | BELUM CUKUP | 23 | 222/132 | -2.97 | 25 | -2.91 | -0.28 | 5.7 | -0.95 | – | -2.07 |
| 92 | `M143` 장대양봉 이후 눌림목 / 5일선 매매 (Undur ke | **41.1** | 21 | 38 | 29 | 38 | BELUM CUKUP | 15 | 29/3 | -4.08 | 24 | -1.81 | -0.47 | 1.9 | -1.24 | – | -10.14 |
| 93 | `N08X36` tutup>EMA20 tidak terlalu jauh | **41.0** | 19 | 29 | 31 | 33 | BELUM CUKUP | 12 | 446/330 | -2.52 | 12 | -6.94 | -0.95 | 3.5 | -2.17 | – | – |
| 94 | `N36X16` Pocket pivot → keluar bila sup | **41.0** | 23 | 23 | 34 | 30 | BELUM CUKUP | 12 | 169/84 | -4.25 | 12 | -3.88 | -0.57 | 3.1 | -1.85 | – | – |
| 95 | `N76X36` Tutup > MA50 (penapis trend tu | **41.0** | 23 | 24 | 34 | 30 | BELUM CUKUP | 12 | 193/123 | -3.71 | 12 | -9.48 | -1.00 | 5.0 | -1.90 | – | – |
| 96 | `N80X36` Tinggi sepanjang masa → keluar | **41.0** | 15 | 15 | 26 | 30 | BELUM CUKUP | 8 | 40/5 | -6.44 | 12 | -4.62 | -0.99 | 2.6 | -1.49 | – | – |
| 97 | `M131` Ross Hook (Joe Ross) | **40.9** | 27 | 39 | 50 | 15 | BELUM CUKUP | 24 | 273/144 | -2.42 | 25 | -3.86 | -0.46 | 4.0 | -0.50 | – | -1.20 |
| 98 | `M93` Bollinger Kaedah II: %b + MFI | **40.8** | 29 | 34 | 52 | 15 | BELUM CUKUP | 23 | 271/100 | -1.97 | 25 | -3.17 | -0.37 | 3.6 | -0.24 | – | -0.37 |
| 99 | `N24X36` Supertrend(10,3) + ADX>20 → ke | **40.8** | 25 | 18 | 37 | 30 | BELUM CUKUP | 12 | 175/90 | -3.42 | 12 | -6.89 | -1.00 | 3.5 | -1.47 | – | – |
| 100 | `N09X36` Undur EMA10 + penapis EMA50 →  | **40.8** | 22 | 22 | 34 | 30 | BELUM CUKUP | 12 | 229/88 | -3.89 | 12 | -6.05 | -1.00 | 3.3 | -1.83 | – | – |
| 101 | `M102` Stockbee SLTB | **40.7** | 32 | 34 | 47 | 15 | BELUM CUKUP | 25 | 442/338 | -1.92 | 25 | -6.09 | -0.55 | 6.1 | -0.89 | – | -2.27 |
| 102 | `M150` Trend Bar Failure (Brooks) | **40.7** | 31 | 33 | 45 | 15 | BELUM CUKUP | 22 | 111/71 | -1.66 | 25 | -6.91 | -0.84 | 4.0 | -0.90 | – | -3.42 |
| 103 | `N124X36` Episodic pivot gap 8-10% → kel | **40.6** | 14 | 16 | 31 | 30 | BELUM CUKUP | 9 | 42/15 | -3.23 | 12 | -10.12 | -1.00 | 5.1 | -1.30 | – | – |
| 104 | `N66X36` 52w tinggi + pengesahan 1% → k | **40.6** | 16 | 12 | 24 | 30 | BELUM CUKUP | 8 | 40/3 | -5.73 | 11 | -6.96 | -1.00 | 4.0 | -1.50 | – | – |
| 105 | `M92` CCI-50 | **40.5** | 31 | 34 | 47 | 15 | BELUM CUKUP | 25 | 579/466 | -1.51 | 25 | -6.63 | -0.59 | 4.5 | -0.87 | – | -2.00 |
| 106 | `M127` Slingshot Bullish | **40.5** | 28 | 36 | 40 | 15 | BELUM CUKUP | 20 | 112/85 | -2.45 | 25 | -6.91 | -0.76 | 4.1 | -1.50 | – | -1.80 |
| 107 | `N07X16` Tiga MA tersusun → keluar bila | **40.5** | 17 | 29 | 32 | 30 | BELUM CUKUP | 12 | 163/43 | -4.23 | 12 | -3.54 | -0.71 | 2.6 | -1.80 | – | – |
| 108 | `N38X36` VCP pecah → keluar selepas DUA | **40.4** | 21 | 29 | 22 | 30 | BELUM CUKUP | 12 | 41/16 | -4.20 | 12 | -6.56 | -0.99 | 3.0 | -2.55 | – | – |
| 109 | `M67` Rayner Teo: Ujian Ketiga pada  | **40.3** | 29 | 28 | 38 | 15 | BELUM CUKUP | 17 | 32/24 | -3.54 | 25 | -6.94 | -0.62 | 7.0 | -1.21 | – | -4.76 |
| 110 | `N75X14` RSI14 < 40 tanpa penapis → kel | **40.2** | 18 | 22 | 36 | 30 | BELUM CUKUP | 12 | 276/57 | -2.80 | 12 | -6.58 | -1.00 | 3.9 | -1.41 | – | – |
| 111 | `N25X17` Supertrend + EMA + ADX>23 → ke | **40.2** | 18 | 23 | 27 | 30 | BELUM CUKUP | 11 | 118/18 | -5.17 | 12 | -4.05 | -0.84 | 2.9 | -1.93 | – | – |
| 112 | `N124X15` Episodic pivot gap 8-10% → eko | **40.2** | 16 | 15 | 23 | 30 | BELUM CUKUP | 9 | 42/0 | -4.75 | 12 | -5.72 | -0.77 | 4.7 | -1.18 | – | – |
| 113 | `N42X15` Lonjakan volum 2x → ekori Chan | **40.1** | 19 | 23 | 23 | 60 | BELUM CUKUP | 12 | 182/0 | -4.35 | 12 | -5.42 | -0.47 | 5.8 | -1.28 | – | – |
| 114 | `N53X16` Supertrend + ADX>25 → keluar b | **40.1** | 17 | 24 | 33 | 30 | BELUM CUKUP | 12 | 119/20 | -4.66 | 12 | -6.37 | -0.75 | 5.6 | -1.36 | – | – |
| 115 | `M139` 均线首次粘合向上发散 (MA berhimpun kali  | **40.0** | 27 | 35 | 44 | 19 | BELUM CUKUP | 24 | 96/41 | -4.52 | 25 | -2.30 | -0.23 | 4.4 | -0.86 | – | -3.06 |
| 116 | `N22X36` BB pecah atas + RSI → keluar s | **40.0** | 15 | 24 | 39 | 30 | BELUM CUKUP | 12 | 121/64 | -4.79 | 12 | -7.96 | -0.81 | 4.5 | -1.08 | – | – |
| 117 | `N40X36` OBV tinggi baharu + MA50 → kel | **40.0** | 21 | 15 | 41 | 30 | BELUM CUKUP | 12 | 80/25 | -2.73 | 12 | -10.67 | -0.85 | 6.5 | -0.45 | – | – |
| 118 | `M12` Parabolic SAR | **39.9** | 29 | 33 | 46 | 15 | BELUM CUKUP | 25 | 404/251 | -3.13 | 25 | -3.84 | -0.63 | 3.2 | -0.98 | – | -2.28 |
| 119 | `M32` Momentum Burst | **39.8** | 27 | 22 | 48 | 15 | BELUM CUKUP | 17 | 67/40 | -2.08 | 25 | -8.40 | -0.61 | 8.2 | -0.20 | – | -0.46 |
| 120 | `M126` Hidden Smash Day (beli, Larry  | **39.8** | 16 | 29 | 34 | 15 | BELUM CUKUP | 12 | 21/10 | -3.33 | 24 | -5.73 | -0.76 | 4.8 | -0.95 | – | -1.22 |
| 121 | `M134` First Kiss After Daylight (Lan | **39.7** | 23 | 33 | 46 | 15 | BELUM CUKUP | 20 | 68/31 | -3.22 | 25 | -5.74 | -0.56 | 4.9 | -0.43 | – | -0.60 |
| 122 | `N57X36` ADX bangkit daripada <20 → kel | **39.7** | 15 | 19 | 21 | 30 | BELUM CUKUP | 10 | 76/18 | -7.08 | 12 | -4.78 | -0.68 | 3.5 | -2.62 | – | – |
| 123 | `M140` 猎豹出击 (Serangan Cheetah) | **39.6** | 18 | 24 | 32 | 15 | BELUM CUKUP | 12 | 43/20 | -3.87 | 25 | -7.09 | -0.81 | 4.5 | -1.64 | – | -1.76 |
| 124 | `N07X36` Tiga MA tersusun → keluar sele | **39.6** | 15 | 24 | 31 | 30 | BELUM CUKUP | 12 | 163/40 | -4.72 | 12 | -5.40 | -0.79 | 3.6 | -1.85 | – | – |
| 125 | `N45X36` Undur EMA21 cerun positif → ke | **39.6** | 15 | 22 | 34 | 30 | BELUM CUKUP | 12 | 140/76 | -4.38 | 12 | -7.05 | -0.79 | 3.5 | -1.76 | – | – |
| 126 | `N53X17` Supertrend + ADX>25 → keluar b | **39.6** | 17 | 21 | 31 | 30 | BELUM CUKUP | 12 | 111/10 | -5.00 | 12 | -6.90 | -0.76 | 5.4 | -1.35 | – | – |
| 127 | `N06X36` Golden cross MA50/MA200 → kelu | **39.6** | 15 | 24 | 24 | 30 | BELUM CUKUP | 11 | 27/4 | -4.26 | 12 | -6.62 | -1.00 | 3.5 | -1.82 | – | – |
| 128 | `N37X14` Gap and go → keluar bila rsi14 | **39.6** | 12 | 13 | 25 | 30 | BELUM CUKUP | 9 | 84/15 | -6.36 | 12 | -8.13 | -0.84 | 4.8 | -2.03 | – | – |
| 129 | `N08X16` tutup>EMA20 tidak terlalu jauh | **39.5** | 14 | 26 | 29 | 30 | BELUM CUKUP | 12 | 517/373 | -2.70 | 12 | -6.61 | -0.98 | 3.1 | -2.44 | – | – |
| 130 | `N41X16` CMF20>0 + tutup>EMA20 → keluar | **39.5** | 14 | 26 | 28 | 30 | BELUM CUKUP | 12 | 318/218 | -3.45 | 12 | -5.52 | -0.75 | 3.4 | -2.52 | – | – |
| 131 | `N42X36` Lonjakan volum 2x → keluar sel | **39.5** | 16 | 18 | 39 | 30 | BELUM CUKUP | 12 | 215/121 | -2.08 | 12 | -8.69 | -1.00 | 5.0 | -1.34 | – | – |
| 132 | `N33X16` Donchian20 + penapis MA200 → k | **39.5** | 17 | 19 | 24 | 30 | BELUM CUKUP | 11 | 106/27 | -6.69 | 12 | -4.71 | -0.89 | 2.4 | -2.44 | – | – |
| 133 | `M135` 3rd Watch | **39.5** | 14 | 13 | 28 | 15 | BELUM CUKUP | 9 | 15/6 | -10.62 | 25 | -7.53 | -0.91 | 4.6 | -1.58 | – | -9.53 |
| 134 | `N42X14` Lonjakan volum 2x → keluar bil | **39.4** | 17 | 17 | 34 | 38 | BELUM CUKUP | 12 | 197/25 | -3.91 | 12 | -6.92 | -0.62 | 5.9 | -1.28 | – | – |
| 135 | `N40X16` OBV tinggi baharu + MA50 → kel | **39.4** | 18 | 14 | 42 | 30 | BELUM CUKUP | 12 | 97/38 | -2.12 | 12 | -11.26 | -0.92 | 6.2 | -0.50 | – | – |
| 136 | `N33X14` Donchian20 + penapis MA200 → k | **39.4** | 18 | 16 | 24 | 30 | BELUM CUKUP | 11 | 116/18 | -6.87 | 12 | -4.17 | -0.87 | 3.0 | -2.28 | – | – |
| 137 | `M80` Radge Saluran Purata Bergerak  | **39.3** | 25 | 31 | 52 | 15 | BELUM CUKUP | 24 | 309/93 | -2.58 | 25 | -4.54 | -0.48 | 4.9 | -0.25 | – | -0.39 |
| 138 | `N68X16` Bullish engulfing + EMA21 → ke | **39.3** | 12 | 25 | 34 | 30 | BELUM CUKUP | 12 | 128/34 | -3.52 | 12 | -6.71 | -0.62 | 5.8 | -1.49 | – | – |
| 139 | `N76X16` Tutup > MA50 (penapis trend tu | **39.3** | 14 | 24 | 26 | 36 | BELUM CUKUP | 12 | 339/237 | -3.32 | 12 | -5.34 | -0.92 | 2.4 | -2.76 | – | – |
| 140 | `N33X36` Donchian20 + penapis MA200 → k | **39.3** | 15 | 18 | 28 | 30 | BELUM CUKUP | 11 | 102/41 | -5.50 | 12 | -7.05 | -1.00 | 3.4 | -2.21 | – | – |
| 141 | `M117` Landry Pullback (high 2 bulan) | **39.2** | 24 | 28 | 49 | 15 | BELUM CUKUP | 21 | 163/27 | -2.07 | 25 | -8.05 | -0.81 | 5.3 | -0.03 | – | -0.03 |
| 142 | `M49` Ichimoku (Tutup Atas Awan + Te | **39.1** | 27 | 33 | 43 | 15 | BELUM CUKUP | 25 | 331/214 | -2.97 | 25 | -4.89 | -0.52 | 4.1 | -1.35 | – | -2.07 |
| 143 | `M28` VWAP Separator + Kiss Pivot | **39.1** | 29 | 28 | 43 | 15 | BELUM CUKUP | 23 | 136/113 | -1.74 | 25 | -7.78 | -0.92 | 5.8 | -1.35 | – | -10.69 |
| 144 | `M119` 180 Bullish (Cooper) | **39.1** | 25 | 30 | 45 | 15 | BELUM CUKUP | 22 | 166/95 | -2.62 | 25 | -6.43 | -0.60 | 5.7 | -1.09 | – | -3.14 |
| 145 | `M106` DMI Wilder | **39.1** | 25 | 30 | 47 | 15 | BELUM CUKUP | 22 | 134/104 | -2.35 | 25 | -5.55 | -0.85 | 3.0 | -0.88 | – | -2.39 |
| 146 | `M149` 3-Step Pullback | **39.0** | 25 | 29 | 50 | 15 | BELUM CUKUP | 23 | 246/87 | -3.34 | 25 | -5.16 | -0.48 | 6.3 | -0.46 | – | -0.44 |
| 147 | `M29` EMA3 + RSI75 + Stokastik | **39.0** | 24 | 24 | 40 | 15 | BELUM CUKUP | 17 | 40/33 | -2.76 | 25 | -10.40 | -0.83 | 8.1 | -1.15 | – | -5.83 |
| 148 | `N56X36` RSI>50 + ADX>20 → keluar selep | **39.0** | 16 | 19 | 30 | 30 | BELUM CUKUP | 12 | 207/122 | -3.36 | 12 | -9.69 | -1.00 | 6.3 | -2.34 | – | – |
| 149 | `N42X16` Lonjakan volum 2x → keluar bil | **39.0** | 15 | 16 | 39 | 30 | BELUM CUKUP | 12 | 218/119 | -2.14 | 12 | -8.91 | -1.00 | 5.3 | -1.29 | – | – |
| 150 | `N74X16` MACD atas garis isyarat (keada | **39.0** | 13 | 22 | 30 | 33 | BELUM CUKUP | 12 | 662/526 | -2.21 | 12 | -7.08 | -0.97 | 5.3 | -2.37 | – | – |
| 151 | `N57X16` ADX bangkit daripada <20 → kel | **39.0** | 15 | 19 | 21 | 30 | BELUM CUKUP | 11 | 74/19 | -6.89 | 12 | -4.76 | -0.68 | 3.5 | -2.69 | – | – |
| 152 | `M30` BB Free Bar + Himpitan 50/2.5 | **38.8** | 23 | 26 | 52 | 15 | BELUM CUKUP | 21 | 230/101 | -2.89 | 25 | -4.06 | -0.37 | 5.5 | -0.26 | – | -0.57 |
| 153 | `M128` Inventory Retracement Bar (IRB | **38.7** | 26 | 26 | 49 | 15 | BELUM CUKUP | 23 | 170/106 | -1.84 | 25 | -6.67 | -0.60 | 7.1 | -0.58 | – | -2.73 |
| 154 | `N113X36` 80-20 bar (sisi beli) → keluar | **38.7** | 14 | 16 | 34 | 30 | BELUM CUKUP | 12 | 362/256 | -1.66 | 12 | -13.22 | -1.00 | 7.8 | -1.84 | – | – |
| 155 | `N27X16` Ichimoku atas awan → keluar bi | **38.7** | 13 | 21 | 27 | 30 | BELUM CUKUP | 12 | 184/96 | -3.46 | 12 | -7.17 | -1.00 | 3.4 | -2.68 | – | – |
| 156 | `N75X15` RSI14 < 40 tanpa penapis → eko | **38.7** | 15 | 21 | 24 | 30 | BELUM CUKUP | 12 | 153/0 | -4.00 | 12 | -8.36 | -0.97 | 3.9 | -1.22 | – | – |
| 157 | `N75X13` RSI14 < 40 tanpa penapis → kel | **38.7** | 14 | 21 | 26 | 30 | BELUM CUKUP | 12 | 155/1 | -3.97 | 12 | -8.36 | -0.97 | 3.9 | -1.24 | – | – |
| 158 | `M105` Supertrend tulen | **38.6** | 23 | 30 | 50 | 15 | BELUM CUKUP | 24 | 376/171 | -3.34 | 25 | -4.83 | -0.39 | 5.2 | -0.48 | – | -1.57 |
| 159 | `N113X16` 80-20 bar (sisi beli) → keluar | **38.6** | 17 | 12 | 37 | 30 | BELUM CUKUP | 12 | 380/255 | -1.43 | 12 | -14.29 | -1.00 | 8.6 | -1.55 | – | – |
| 160 | `N56X16` RSI>50 + ADX>20 → keluar bila  | **38.5** | 12 | 19 | 31 | 30 | BELUM CUKUP | 12 | 232/127 | -3.47 | 12 | -6.91 | -1.00 | 4.4 | -2.21 | – | – |
| 161 | `N24X17` Supertrend(10,3) + ADX>20 → ke | **38.5** | 14 | 14 | 26 | 30 | BELUM CUKUP | 11 | 131/43 | -5.85 | 12 | -6.88 | -0.94 | 3.5 | -2.43 | – | – |
| 162 | `M34` Carter TTM Squeeze | **38.4** | 24 | 26 | 47 | 15 | BELUM CUKUP | 22 | 106/53 | -2.78 | 25 | -5.58 | -0.49 | 5.1 | -0.64 | – | -1.85 |
| 163 | `M26` Garis Trend Undur 3 Sentuhan + | **38.3** | 22 | 29 | 42 | 15 | BELUM CUKUP | 21 | 82/52 | -1.80 | 25 | -7.03 | -0.86 | 4.3 | -1.11 | – | -1.60 |
| 164 | `N56X17` RSI>50 + ADX>20 → keluar bila  | **38.2** | 16 | 14 | 27 | 30 | BELUM CUKUP | 12 | 147/52 | -5.68 | 12 | -6.35 | -0.96 | 3.4 | -2.40 | – | – |
| 165 | `N24X16` Supertrend(10,3) + ADX>20 → ke | **38.2** | 13 | 15 | 24 | 30 | BELUM CUKUP | 11 | 124/24 | -6.39 | 12 | -6.67 | -0.98 | 3.5 | -2.49 | – | – |
| 166 | `N50X14` Mampat + pecah volum 1.5x → ke | **38.2** | 7 | 8 | 25 | 30 | BELUM CUKUP | 9 | 23/4 | -6.51 | 12 | -10.18 | -1.00 | 5.8 | -1.57 | – | – |
| 167 | `M99` Three Line Break | **38.1** | 25 | 26 | 46 | 15 | BELUM CUKUP | 24 | 173/123 | -3.99 | 25 | -5.89 | -0.54 | 4.9 | -1.04 | – | -3.96 |
| 168 | `N36X14` Pocket pivot → keluar bila rsi | **38.1** | 17 | 11 | 29 | 32 | BELUM CUKUP | 12 | 170/36 | -5.82 | 12 | -7.49 | -1.00 | 4.5 | -2.02 | – | – |
| 169 | `N73X13` Tutup bawah jalur bawah BB(20, | **38.1** | 12 | 19 | 25 | 30 | BELUM CUKUP | 12 | 176/1 | -3.97 | 12 | -8.40 | -0.91 | 5.1 | -1.32 | – | – |
| 170 | `N22X16` BB pecah atas + RSI → keluar b | **38.1** | 12 | 14 | 36 | 30 | BELUM CUKUP | 12 | 122/45 | -6.51 | 12 | -7.76 | -0.87 | 4.3 | -1.33 | – | – |
| 171 | `N31X36` Turtle sistem 2 → keluar selep | **38.1** | 14 | 12 | 23 | 30 | BELUM CUKUP | 11 | 105/13 | -6.38 | 12 | -6.87 | -0.99 | 3.9 | -2.35 | – | – |
| 172 | `M136` Short/Intermediate-term Low (L | **38.0** | 23 | 30 | 46 | 15 | BELUM CUKUP | 25 | 848/380 | -3.98 | 25 | -6.50 | -0.72 | 3.7 | -1.05 | – | -0.67 |
| 173 | `N50X17` Mampat + pecah volum 1.5x → ke | **38.0** | 6 | 8 | 26 | 30 | BELUM CUKUP | 9 | 22/4 | -7.01 | 12 | -11.00 | -0.93 | 6.6 | -1.51 | – | – |
| 174 | `M06` Minervini VCP Breakout | **37.9** | 22 | 31 | 42 | 15 | BELUM CUKUP | 23 | 89/52 | -4.42 | 25 | -4.70 | -0.54 | 3.7 | -1.16 | – | -3.41 |
| 175 | `M04` BB Squeeze Breakout | **37.9** | 22 | 23 | 49 | 15 | BELUM CUKUP | 21 | 155/73 | -4.21 | 25 | -4.24 | -0.42 | 5.1 | -0.42 | – | -0.74 |
| 176 | `M59` Anjakan Julat RSI | **37.9** | 16 | 18 | 39 | 15 | BELUM CUKUP | 14 | 36/20 | -6.58 | 25 | -6.65 | -0.68 | 5.1 | -0.93 | – | -3.20 |
| 177 | `N119X15` 3 tutup turun berturut → ekori | **37.9** | 9 | 9 | 13 | 30 | BELUM CUKUP | 9 | 58/0 | -6.09 | 12 | -9.17 | -1.00 | 5.6 | -2.37 | – | – |
| 178 | `N29X36` PSAR naik + tutup>MA50 → kelua | **37.8** | 14 | 14 | 26 | 30 | BELUM CUKUP | 12 | 165/100 | -4.89 | 12 | -12.15 | -1.00 | 9.0 | -2.96 | – | – |
| 179 | `N54X16` Supertrend + RSI>50 → keluar b | **37.7** | 12 | 12 | 23 | 30 | BELUM CUKUP | 11 | 128/35 | -7.37 | 12 | -6.93 | -0.87 | 5.3 | -2.70 | – | – |
| 180 | `N28X14` ADX>25 + DI+ > DI- → keluar bi | **37.6** | 12 | 14 | 27 | 30 | BELUM CUKUP | 12 | 210/27 | -5.46 | 12 | -9.25 | -0.90 | 5.7 | -2.15 | – | – |
| 181 | `M36` Turtle 55/20 | **37.5** | 22 | 26 | 49 | 15 | BELUM CUKUP | 25 | 350/202 | -2.92 | 25 | -7.07 | -0.53 | 7.2 | -0.68 | – | -1.59 |
| 182 | `M107` Golden Cross SMA50/200 | **37.5** | 22 | 28 | 40 | 15 | BELUM CUKUP | 22 | 47/10 | -4.04 | 25 | -7.32 | -0.75 | 3.5 | -0.75 | – | -1.26 |
| 183 | `N54X36` Supertrend + RSI>50 → keluar s | **37.5** | 14 | 11 | 31 | 30 | BELUM CUKUP | 12 | 184/108 | -4.02 | 12 | -11.58 | -1.00 | 7.8 | -2.22 | – | – |
| 184 | `M14` Walking with the Whales | **37.4** | 26 | 24 | 44 | 15 | BELUM CUKUP | 25 | 1052/818 | -1.66 | 25 | -12.84 | -0.83 | 8.1 | -1.19 | – | -2.18 |
| 185 | `N119X13` 3 tutup turun berturut → kelua | **37.4** | 8 | 16 | 31 | 38 | BELUM CUKUP | 12 | 269/64 | -3.18 | 12 | -9.76 | -1.00 | 6.7 | -2.00 | – | – |
| 186 | `N42X17` Lonjakan volum 2x → keluar bil | **37.4** | 12 | 10 | 38 | 30 | BELUM CUKUP | 12 | 213/72 | -3.23 | 12 | -9.98 | -1.00 | 6.9 | -1.31 | – | – |
| 187 | `N39X36` NR7 kemudian pecah → keluar se | **37.4** | 2 | 6 | 17 | 30 | BELUM CUKUP | 8 | 35/11 | -7.20 | 11 | -13.86 | -1.00 | 7.2 | -3.15 | – | – |
| 188 | `N27X36` Ichimoku atas awan → keluar se | **37.2** | 13 | 11 | 24 | 30 | BELUM CUKUP | 12 | 113/34 | -5.76 | 12 | -9.32 | -1.00 | 4.7 | -2.56 | – | – |
| 189 | `M95` Nisbah Kebaharuan High 52 Ming | **37.1** | 19 | 27 | 44 | 15 | BELUM CUKUP | 22 | 129/74 | -3.21 | 25 | -9.34 | -0.79 | 6.1 | -1.02 | – | -2.26 |
| 190 | `N28X17` ADX>25 + DI+ > DI- → keluar bi | **37.1** | 12 | 13 | 22 | 30 | BELUM CUKUP | 12 | 144/6 | -5.71 | 12 | -8.32 | -0.93 | 5.2 | -2.21 | – | – |
| 191 | `N29X16` PSAR naik + tutup>MA50 → kelua | **37.1** | 11 | 12 | 26 | 30 | BELUM CUKUP | 12 | 218/128 | -5.15 | 12 | -8.25 | -1.00 | 6.0 | -2.98 | – | – |
| 192 | `N16X13` RSI2<10 tanpa penapis → keluar | **37.0** | 7 | 18 | 28 | 30 | BELUM CUKUP | 12 | 264/6 | -3.55 | 12 | -10.80 | -1.00 | 6.9 | -1.55 | – | – |
| 193 | `N55X13` BB + RSI + ADX>20 → keluar bil | **37.0** | 10 | 18 | 17 | 30 | BELUM CUKUP | 12 | 98/0 | -4.73 | 12 | -8.16 | -0.99 | 4.6 | -2.02 | – | – |
| 194 | `N22X14` BB pecah atas + RSI → keluar b | **36.9** | 10 | 11 | 29 | 30 | BELUM CUKUP | 12 | 128/29 | -6.89 | 12 | -9.68 | -0.97 | 5.5 | -2.00 | – | – |
| 195 | `M156` Single Penetration (DiNapoli) | **36.8** | 22 | 25 | 44 | 15 | BELUM CUKUP | 25 | 271/200 | -2.15 | 25 | -7.63 | -0.56 | 7.6 | -1.27 | – | -4.02 |
| 196 | `M19` Sneaky Pivot (proksi harian) | **36.8** | 20 | 26 | 45 | 15 | BELUM CUKUP | 24 | 432/297 | -4.37 | 25 | -8.33 | -0.65 | 5.2 | -1.13 | – | -15.52 |
| 197 | `M55` Guppy GMMA | **36.8** | 24 | 20 | 46 | 15 | BELUM CUKUP | 24 | 245/167 | -3.19 | 25 | -9.50 | -0.90 | 5.6 | -1.02 | – | -2.77 |
| 198 | `M66` IBD Undur Pertama ke Purata 50 | **36.4** | 22 | 21 | 45 | 15 | BELUM CUKUP | 24 | 265/182 | -2.92 | 25 | -8.83 | -0.67 | 7.6 | -1.10 | – | -2.82 |
| 199 | `M57` Landry Trend Knockout (TKO) | **36.3** | 24 | 24 | 38 | 15 | BELUM CUKUP | 25 | 190/140 | -3.15 | 25 | -8.26 | -0.98 | 4.6 | -1.99 | – | -5.07 |
| 200 | `M141` First Thrust (Landry) | **36.3** | 1 | 8 | 30 | 15 | BELUM CUKUP | 9 | 27/17 | -8.48 | 25 | -16.74 | -0.94 | 6.6 | -1.72 | – | -6.67 |
| 201 | `M155` Market Cycle Strategy | **35.9** | 21 | 22 | 44 | 15 | BELUM CUKUP | 25 | 777/458 | -3.89 | 25 | -8.54 | -0.75 | 5.2 | -1.27 | – | -3.14 |
| 202 | `M50` Elder Triple Screen | **35.9** | 20 | 22 | 46 | 15 | BELUM CUKUP | 25 | 648/450 | -1.99 | 25 | -12.26 | -1.00 | 7.2 | -1.05 | – | -1.91 |
| 203 | `M73` ADX(5) > 40 + Julat Terkecil 6 | **35.7** | 22 | 18 | 45 | 15 | BELUM CUKUP | 25 | 1119/913 | -0.97 | 25 | -12.12 | -1.00 | 7.1 | -1.08 | – | -6.79 |
| 204 | `M101` Bulkowski: Tiga lembah menaik | **35.7** | 14 | 15 | 43 | 15 | BELUM CUKUP | 17 | 46/23 | -4.57 | 25 | -9.89 | -0.69 | 8.5 | -0.58 | – | -1.48 |
| 205 | `M125` 2-Bar Breakout | **35.6** | 19 | 23 | 43 | 15 | BELUM CUKUP | 25 | 1139/550 | -4.50 | 25 | -9.45 | -0.75 | 5.2 | -1.35 | – | -0.77 |
| 206 | `M152` Spike & Ledge | **35.3** | 14 | 27 | 39 | 15 | BELUM CUKUP | 22 | 56/11 | -5.69 | 25 | -7.87 | -0.64 | 4.4 | -0.96 | – | -3.00 |
| 207 | `N47X16` NR7 + EMA9>EMA21 → keluar bila | **35.3** | 3 | 16 | 25 | 30 | BELUM CUKUP | 12 | 204/66 | -4.53 | 12 | -13.02 | -1.00 | 6.5 | -2.86 | – | – |
| 208 | `M03` BB Break + Divergence RSI | **35.2** | 14 | 27 | 46 | 15 | BELUM CUKUP | 25 | 445/368 | -2.04 | 25 | -7.98 | -0.78 | 4.7 | -1.01 | – | -3.94 |
| 209 | `M154` HOLP (High of Low Period) | **35.0** | 14 | 14 | 38 | 15 | BELUM CUKUP | 18 | 96/41 | -5.53 | 25 | -13.11 | -0.98 | 8.1 | -1.42 | – | -6.10 |
| 210 | `M31` Band Walk (BB 20/2) | **34.6** | 18 | 15 | 50 | 15 | BELUM CUKUP | 24 | 403/133 | -3.14 | 25 | -8.51 | -0.55 | 8.3 | -0.53 | – | -1.05 |
| 211 | `M147` Improved Three-Bar Pullback | **34.4** | 10 | 20 | 32 | 15 | BELUM CUKUP | 18 | 119/43 | -6.23 | 25 | -14.32 | -0.79 | 6.8 | -2.15 | – | -2.02 |
| 212 | `N47X36` NR7 + EMA9>EMA21 → keluar sele | **34.4** | 0 | 9 | 24 | 30 | BELUM CUKUP | 11 | 184/59 | -5.33 | 12 | -17.33 | -1.00 | 9.1 | -3.50 | – | – |
| 213 | `N16X15` RSI2<10 tanpa penapis → ekori  | **34.3** | 2 | 12 | 20 | 30 | BELUM CUKUP | 12 | 242/0 | -3.88 | 12 | -13.79 | -1.00 | 9.3 | -1.64 | – | – |
| 214 | `M11` NR7 Breakout + Volume | **34.2** | 13 | 20 | 40 | 15 | BELUM CUKUP | 22 | 127/91 | -1.78 | 25 | -11.85 | -0.79 | 8.8 | -1.64 | – | -1.56 |
| 215 | `M47` Holy Grail Raschke | **34.0** | 8 | 15 | 28 | 15 | BELUM CUKUP | 16 | 38/30 | -3.29 | 25 | -12.01 | -0.98 | 7.2 | -2.44 | – | -20.45 |
| 216 | `M76` Undercut & Rally pada Low Pent | **33.0** | 10 | 19 | 36 | 15 | BELUM CUKUP | 22 | 84/71 | -3.19 | 25 | -12.43 | -0.99 | 7.6 | -1.94 | – | -7.03 |
| 217 | `M82` Arthur Hill Rotasi Sasaran 10% | **32.7** | 18 | 10 | 45 | 15 | BELUM CUKUP | 25 | 602/255 | -3.39 | 25 | -8.96 | -0.48 | 10.8 | -1.14 | – | -4.73 |
| 218 | `M81` Bensdorp Long Trend High Momen | **32.6** | 2 | 4 | 38 | 15 | BELUM CUKUP | 13 | 431/186 | -6.69 | 25 | -23.84 | -1.00 | 16.8 | -1.72 | – | -5.14 |
| 219 | `M79` Radge: 20% Flipper | **32.1** | 10 | 19 | 40 | 15 | BELUM CUKUP | 25 | 395/152 | -5.93 | 25 | -12.17 | -0.78 | 7.3 | -1.70 | – | -3.42 |
| 220 | `M01` Bollinger Band + RSI | **32.1** | 14 | 8 | 41 | 15 | BELUM CUKUP | 22 | 119/26 | -2.63 | 25 | -12.66 | -1.00 | 5.8 | -0.97 | – | -3.63 |
| 221 | `M122` Moving Momentum (ChartSchool) | **31.9** | 11 | 16 | 32 | 15 | BELUM CUKUP | 24 | 113/71 | -5.62 | 25 | -13.95 | -1.00 | 7.2 | -2.47 | – | -7.35 |
| 222 | `M123` CCI Correction (Lambert, Chart | **31.2** | 7 | 24 | 30 | 15 | BELUM CUKUP | 24 | 191/174 | -2.10 | 25 | -15.07 | -1.00 | 7.8 | -2.84 | – | -5.87 |
| 223 | `M09` Volumatic VIDYA Pivot Retest | **30.9** | 0 | 8 | 27 | 15 | BELUM CUKUP | 15 | 40/27 | -6.23 | 25 | -17.54 | -1.00 | 9.7 | -2.48 | – | -13.74 |
| 224 | `M20` EMA10/15 Crossover + Sudut | **30.0**⌈ | 27 | 32 | 42 | 15 | GAGAL | 25 | 530/456 | -1.89 | 25 | -7.74 | -0.79 | 4.1 | -1.51 | – | -10.20 |
| 225 | `M161` EMA 10/21 + Supertrend (10,3) | **29.9** | 8 | 10 | 47 | 15 | BELUM CUKUP | 25 | 521/300 | -2.41 | 25 | -20.08 | -0.94 | 11.2 | -0.95 | – | -2.28 |
| 226 | `M90` Pring KST | **29.7** | 5 | 13 | 41 | 15 | BELUM CUKUP | 24 | 93/53 | -4.49 | 25 | -15.37 | -0.83 | 12.5 | -1.35 | – | -5.25 |

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

