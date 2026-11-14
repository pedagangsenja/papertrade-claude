# Carian Setup CS05 — PRASYARAT + SYARAT bagi semua kaedah (backtest, BUKAN bukti)

> **Status keputusan (kad skor, harga 2026-11-12):** TERBUKTI 0 · CALON 0 · BELUM CUKUP 223 · GAGAL 0 · NEGATIF 0. Rejim QQQ OFF sejak 2026-10-16. Hanya **TERBUKTI** layak untuk wang sebenar (`laporan/KAD_SKOR.md`); nombor dalam laporan ini BUKAN keputusan dan tidak boleh dibaca sebagai pangkat untuk wang sebenar.

Dijana `kajian/carian_setup/cs_cs05.py`. Pradaftar: `kajian/SPEC_CARIAN_SETUP.md` pindaan 14 Nov 2026 (i), dikomit sebelum pusingan ini dijalankan. **Jangan sunting secara manual.** Pusingan lama ("syarat sahaja"): `carian_setup/hasil/CS01`–`CS04/LAPORAN.md`.

## 1. Apa yang diuji

Setup lengkap = **prasyarat** (pasaran; kumpulan/syarikat) → **syarat** (pencetus + penapis saham itu sendiri). Ukuran: KADAR TANGKAP saham "lari" (naik ≥ 5 % minggu pertama, capai ≥ 10 % sebelum henti −8 %, masih ≥ 10 % pada minggu ke-4). Dua kayu ukur:

- **Pilih:** kadar lari setup tolak saham rawak pada **hari yang sama** dan tahap turun-naik sama. Mengukur kemahiran memilih saham. Prasyarat pasaran menaikkan saham rawak hari itu juga, jadi ia hanya dikira jika pencetus memilih lebih baik pada hari begitu.
- **Jumlah:** kadar lari setup tolak saham rawak **sepanjang era**. Memasukkan kesan BILA membeli (sumbangan prasyarat pasaran). Hari isyarat berkelompok, jadi baca bersama plasebo dan bilangan hari isyarat.

Carian (kumpulan A, 2010–2024): 500 pencetus (465 cukup isyarat) × 34 pilihan prasyarat pasaran × 16 pilihan prasyarat kumpulan/syarikat × 379 gabungan penapis saham = **103,088,000 peraturan masuk dicuba**, 43,784,217 cukup isyarat (≥ 100 dalam setiap era). Carian yang sama diulang dengan prasyarat **plasebo** (dianjak 437 sesi). Angka di bawah daripada **kumpulan B** (saham yang carian tidak lihat), 2010 – Ogo 2026; **K3 = 2025 – Ogo 2026 ialah ujian sebenar**.

## 2. Jawapan ringkas: adakah prasyarat menolong?

Bagi setiap pencetus, tiga peraturan dipilih pada kumpulan A: terbaik **syarat sahaja** (S), terbaik **dengan prasyarat** (P) dan terbaik dengan **prasyarat plasebo** (PL); semuanya diukur pada kumpulan B. Bacaan dikunci (pindaan (i) butir 6): prasyarat "menolong" hanya jika median (P − S) positif DAN melebihi median (PL − S).

| Kayu ukur | Pencetus dibanding | Median lari %: S / P / PL | Median kena henti %: S / P / PL | Median kelebihan: S / P / PL | Median (P − S) | Median (PL − S) | P > S | P > PL | **Menolong?** |
|---|---|---|---|---|---|---|---|---|---|
| Pilih, kumpulan B | 463 | 8.4 / 11.2 / 9.9 | 44.2 / 39.2 / 45.9 | +0.78 / +5.51 / +1.41 | +4.65 | +0.62 | 430 / 463 | 413 / 463 | **YA** |
| Pilih, K3 sahaja | 305 | | | | +5.61 | +0.51 | 273 / 305 | 255 / 305 | **YA** |
| Jumlah, kumpulan B | 457 | 11.4 / 12.1 / 11.9 | 51.8 / 37.8 / 39.6 | +2.00 / +6.51 / +4.37 | +4.71 | +2.16 | 419 / 457 | 329 / 457 | **YA** |
| Jumlah, K3 sahaja | 186 | | | | +6.06 | +0.57 | 152 / 186 | 143 / 186 | **YA** |

Unit kelebihan dan beza: mata peratus. Jadual setiap pencetus: `carian_setup/hasil/CS05/SEMUA_PENCETUS.md`.

## 3. Papan 10 teratas — kayu ukur PILIH (lawan saham rawak HARI SAMA)

| # | ID | Prasyarat | Pencetus | Penapis saham | Belian (hari isyarat) | **Lari %** (rawak) | Capai +10 % dahulu % (rawak) | Kena henti −8 % dahulu % (rawak) | Kelebihan lari K1 / K2 / K3 | T1 | T2 | T3 | T4 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `F39` | rejim ON baharu (<= 10 sesi) DAN earnings dalam 1-5 sesi akan datang | M73 ADX(5) > 40 + Julat Terkecil 6 Hari (ditala 2) | tutup > MA50 DAN >= 30% di bawah puncak 52 minggu | 501 (242) | **21.2 (10.6)** | 41.7 (33.9) | 42.5 (35.0) | +12.3 / +8.2 / +12.0 | ✓ | ✓ | ✓ | ✓ |
| 2 | `F40` | rejim ON baharu (<= 10 sesi) DAN earnings dalam 1-5 sesi akan datang | M14 Walking with the Whales (ditala 2) | Supertrend naik DAN >= 30% di bawah puncak 52 minggu | 597 (262) | **21.6 (10.8)** | 44.6 (34.7) | 42.4 (36.5) | +10.7 / +10.1 / +12.5 | ✓ | ✓ | ✓ | ✓ |
| 3 | `F41` | QQQ dalam 3% dari puncak 52 minggu DAN earnings dalam 1-5 sesi akan datang | N119 3 tutup turun berturut | ADX < 20 DAN ATR% >= 4 | 925 (383) | **17.7 (10.2)** | 37.7 (30.9) | 55.0 (49.3) | +10.5 / +8.2 / +3.0 | ✓ | ✓ | ✓ | ✓ |
| 4 | `F42` | distribution day QQQ <= 2 dalam 25 sesi DAN >= 60% saham industri di atas MA50 | M159 Heikin-Ashi Trend (ditala 1) | RS >= 90 DAN ATR% >= 4 | 303 (137) | **14.5 (8.2)** | 38.0 (29.6) | 48.8 (39.9) | +6.3 / +7.4 / +1.6 | ✓ | ✓ | ✓ | ✓ |
| 5 | `F43` | Januari DAN tiada earnings dalam 20 sesi akan datang | M105 Supertrend tulen (ditala 2) | MACD > isyarat DAN >= 30% di bawah puncak 52 minggu | 514 (141) | **23.0 (18.9)** | 48.2 (44.6) | 31.7 (31.1) | +5.7 / +3.8 / +0.7 | ✗ | ✓ | ✗ | ✓ |
| 6 | `F44` | turun-naik SPY menurun (21 hari < 63 hari) DAN kejutan untung terkini positif (SUE > 0) | M79 Radge: 20% Flipper (ditala 2) | templat trend Minervini DAN ATR% >= 4 | 602 (400) | **13.6 (10.0)** | 35.2 (32.0) | 53.8 (47.8) | +4.4 / +3.9 / +2.7 | ✓ | ✓ | ✗ | ✓ |
| 7 | `F45` | turun-naik SPY menurun (21 hari < 63 hari) DAN hasil suku terkini tumbuh >= 20% | M94 Pecutan Momentum (Chen, Yu & Wang) (ditala 1) | MACD > 0 DAN ATR% >= 4 | 786 (92) | **16.3 (12.1)** | 41.9 (36.0) | 47.7 (43.8) | +2.4 / +5.0 / +4.2 | ✓ | ✓ | ✗ | ✓ |
| 8 | `F46` | regangan turun-naik SPY (proksi VIX) + SPY > SMA200 DAN hasil suku terkini tumbuh >= 20% | N124 Episodic pivot gap 8-10% | tutup > MA20 DAN RSI14 > 50 | 278 (185) | **10.8 (8.9)** | 28.8 (28.7) | 40.3 (43.6) | +0.7 / +1.0 / +5.5 | ✗ | ✓ | ✗ | ✓ |
| 9 | `F47` | regangan turun-naik SPY (proksi VIX) + SPY > SMA200 DAN hasil suku terkini tumbuh >= 20% | M124 'Last' Stochastic Technique (ChartSchool) (ditala 2) | Supertrend naik DAN volum hari isyarat >= 1.5x purata 50 | 392 (262) | **10.2 (8.3)** | 25.5 (26.7) | 38.3 (38.1) | +3.0 / +1.5 / -0.5 | ✗ | ✗ | ✗ | ✗ |
| 10 | `F48` | >= 60% saham di atas MA50 DAN >= 60% saham sektor di atas MA50 | M84 Jarak purata bergerak MAD 21/200 (ditala 2) | dalam 15% dari puncak 52 minggu DAN ATR% >= 4 | 1,152 (100) | **13.5 (9.2)** | 35.2 (29.6) | 53.3 (46.6) | +3.7 / +4.1 / +6.4 | ✓ | ✓ | ✗ | ✓ |

- "Rawak" = saham lain yang layak pada hari yang sama dan tahap turun-naik yang sama. **T1:** kelebihan "capai +10 % dahulu" positif dalam K1, K2 dan K3. **T2:** kelebihan "lari" positif dalam ketiga-tiganya. **T3:** kelebihan lari melebihi persentil ke-95 peraturan rawak (+5.51 mata). **T4:** kelebihan lari (kumpulan B DAN K3) melebihi setup yang sama TANPA prasyarat.

**Setup lengkap: henti, pegang dan keluar dipilih ikut kadar tangkap yang direalisasi** (pindaan (j); dipilih pada kumpulan A, angka kumpulan B). **Jadi** = dagangan DIJUAL dengan untung bersih ≥ 10 % (kos 0.5 % ditolak; jurang melepasi henti dijual pada harga buka). "Rawak" = saham rawak (asas papan ini) dengan henti dan keluar yang sama. **Tangkap penuh** = saham itu lari (≥ 5 % minggu pertama, capai 10 %, kekal ≥ 10 % minggu ke-4) DAN dagangannya dijual dengan untung ≥ 10 %. "Pelari dipegang" = daripada saham yang lari, berapa % dijual dengan untung ≥ 10 %.

| ID | Henti | Keluar | Pegang (sesi) | **Tangkap penuh %** | **Jadi %** (rawak) | Kelebihan jadi K1 / K2 / K3 | Rugi ≥ 8 % % (rawak) | Pelari dipegang % | Jadi % tanpa keluar indikator | Jadi % dengan keluar lama (ikut purata) | **Menang %** (K1 / K2 / K3) | Purata setiap dagangan % K1 / K2 / K3 (maklumat) | L1 | L2 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `F39` | H3 3xATR14 | X09 MACD < isyarat DAN X21 Stochastic silang turun di atas 80 | 15.8 | **20.8** | **27.3 (20.3)** | +4.9 / +7.7 / +9.6 | 32.9 (23.6) | 98.1 | 27.1 | 20.3 | **51** (53 / 52 / 48) | +1.13 / +2.49 / +1.71 | ✓ | ✓ |
| `F40` | H3 3xATR14 | X14 Supertrend turun DAN X21 Stochastic silang turun di atas 80 | 16.4 | **20.9** | **28.0 (18.8)** | +8.1 / +8.5 / +12.4 | 32.0 (24.7) | 96.9 | 28.0 | 25.4 | **51** (51 / 51 / 49) | +1.84 / +2.53 / +1.88 | ✓ | ✓ |
| `F41` | H3 3xATR14 | X12 RSI14 silang turun bawah 70 | 14.7 | **16.7** | **26.9 (19.6)** | +10.9 / +9.1 / -0.4 | 39.6 (31.9) | 94.5 | 25.1 | 24.6 | **46** (47 / 51 / 39) | +0.09 / +1.53 / -3.52 | ✗ | ✓ |
| `F42` | H3 3xATR14 | X00 tiada keluar indikator (henti + 20 sesi) | 18.1 | **14.8** | **27.9 (18.9)** | +8.2 / +11.5 / +1.6 | 29.2 (26.5) | 100.0 | 27.9 | 26.9 | **53** (47 / 63 / 50) | -0.06 / +9.04 / +2.57 | ✓ | ✓ |
| `F43` | H4 4xATR14 | X00 tiada keluar indikator (henti + 20 sesi) | 19.4 | **22.5** | **36.5 (33.8)** | +3.3 / +5.1 / -3.5 | 16.5 (17.8) | 98.3 | 36.5 | 32.4 | **70** (79 / 78 / 32) | +7.83 / +8.42 / -4.45 | ✗ | ✓ |
| `F44` | H3 3xATR14 | X00 tiada keluar indikator (henti + 20 sesi) | 17.6 | **13.2** | **26.3 (22.2)** | +8.9 / +1.3 / +5.2 | 35.6 (32.1) | 97.6 | 26.3 | 18.8 | **48** (52 / 48 / 45) | +1.89 / +0.99 / +0.77 | ✓ | ✓ |
| `F45` | H4 4xATR14 | X12 RSI14 silang turun bawah 70 DAN X19 Chandelier 2xATR14 | 18.7 | **15.4** | **29.0 (22.7)** | +7.4 / +7.0 / +3.4 | 26.0 (25.6) | 95.3 | 29.2 | 26.7 | **54** (47 / 58 / 53) | -0.01 / +4.93 / +3.17 | ✓ | ✗ |
| `F46` | H3 3xATR14 | X04 tutup < EMA10 DAN X12 RSI14 silang turun bawah 70 | 17.4 | **10.1** | **21.9 (18.9)** | -3.2 / +5.6 / +7.3 | 25.5 (30.3) | 93.3 | 22.3 | 18.7 | **55** (51 / 61 / 51) | -0.04 / +1.91 / +1.32 | ✗ | ✗ |
| `F47` | H3 3xATR14 | X04 tutup < EMA10 DAN X12 RSI14 silang turun bawah 70 | 17.3 | **9.4** | **20.1 (17.6)** | +2.0 / +4.1 / -1.7 | 26.0 (25.1) | 92.5 | 20.4 | 19.8 | **53** (51 / 56 / 50) | +0.30 / +1.32 / -0.26 | ✗ | ✗ |
| `F48` | H3 3xATR14 | X13 RSI14 > 80 DAN X21 Stochastic silang turun di atas 80 | 16.7 | **13.2** | **25.8 (18.9)** | +8.5 / +5.5 / +7.8 | 35.0 (31.3) | 99.4 | 25.5 | 12.0 | **48** (45 / 50 / 53) | -0.26 / +1.19 / +4.71 | ✓ | ✓ |

- **Menang %** = daripada 100 dagangan, berapa yang dijual dengan untung selepas kos (selebihnya rugi); baca bersama purata setiap dagangan, kerana kadar menang sahaja tidak menunjukkan saiz untung dan rugi.
- **L1:** kelebihan "jadi" atas rawak positif dalam K1, K2 dan K3. **L2:** "jadi" dengan keluar terpilih tidak kurang daripada tanpa keluar indikator (henti sama, pegang 20 sesi).

Dari mana datangnya kadar tangkap? Setiap sel: lari % (rawak %) · kena henti %, kumpulan B. "Tanpa pencetus" = semua saham layak yang memenuhi prasyarat dan penapis yang sama (maklumat tambahan, tidak dipradaftar):

| ID | Setup penuh | Syarat sahaja (buang prasyarat) | Prasyarat + penapis sahaja (buang pencetus) |
|---|---|---|---|
| `F39` | 21.2 (10.6) · 42.5 | 9.1 (8.6) · 47.5 | 20.1 (9.8) · 43.5 |
| `F40` | 21.6 (10.8) · 42.4 | 10.0 (9.0) · 47.9 | 21.1 (10.7) · 41.8 |
| `F41` | 17.7 (10.2) · 55.0 | 12.5 (11.3) · 50.8 | 18.0 (10.1) · 54.5 |
| `F42` | 14.5 (8.2) · 48.8 | 12.0 (9.8) · 54.2 | 13.0 (7.8) · 50.3 |
| `F43` | 23.0 (18.9) · 31.7 | 10.1 (9.4) · 47.0 | 14.6 (13.5) · 40.0 |
| `F44` | 13.6 (10.0) · 53.8 | 12.4 (9.7) · 55.6 | 12.1 (9.8) · 51.9 |
| `F45` | 16.3 (12.1) · 47.7 | 14.1 (11.8) · 51.8 | 11.9 (9.8) · 53.2 |
| `F46` | 10.8 (8.9) · 40.3 | 9.5 (9.0) · 42.0 | 6.3 (5.6) · 35.1 |
| `F47` | 10.2 (8.3) · 38.3 | 6.7 (6.7) · 34.1 | 8.5 (7.0) · 35.6 |
| `F48` | 13.5 (9.2) · 53.3 | 13.5 (11.0) · 54.8 | 10.8 (9.0) · 51.6 |

**Semakan kejujuran (pilih).** 200 daripada 200 peraturan teratas memakai sekurang-kurangnya satu prasyarat; paling kerap: earnings dalam 1-5 sesi akan datang (200); >= 15% saham dalam 5% dari puncak 52 minggu (45); SPY atas SMA200 (32); SPY Peringkat 2 Weinstein (atas SMA150 yang naik) (25); QQQ dalam 3% dari puncak 52 minggu (19); QQQ ON (17).

| Ukuran (kelebihan lari, mata peratus) | Kunci K1 (kumpulan B, 2010–2019) | Kunci K2 (kumpulan B, 2020–2024) | Kunci K3 (kumpulan B, 2025 – Ogo 2026) |
|---|---|---|---|
| Median, peraturan teratas (prasyarat sebenar) | +9.28 (200 / 200 positif) | +7.59 (200 / 200 positif) | +8.14 (193 / 193 positif) |
| Median, peraturan teratas PLASEBO | +3.81 (200 / 200 positif) | +3.90 (189 / 200 positif) | +3.04 (147 / 181 positif) |
| Median, peraturan rawak | +0.16 (109 / 200 positif) | +0.13 (107 / 200 positif) | +0.83 (108 / 177 positif) |
| Spearman skor lawan kelebihan (teratas) | +0.15 | +0.07 | +0.00 |

## 4. Papan 10 teratas — kayu ukur JUMLAH (lawan saham rawak sepanjang ERA)

| # | ID | Prasyarat | Pencetus | Penapis saham | Belian (hari isyarat) | **Lari %** (rawak) | Capai +10 % dahulu % (rawak) | Kena henti −8 % dahulu % (rawak) | Kelebihan lari K1 / K2 / K3 | T1 | T2 | T3 | T4 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `F49` | QQQ >= 10% di bawah puncak DAN earnings dalam 1-5 sesi akan datang | N119 3 tutup turun berturut | MACD > isyarat DAN ATR% >= 4 | 1,068 (201) | **26.2 (9.1)** | 47.0 (29.9) | 45.5 (45.4) | +18.7 / +16.2 / +21.0 | ✓ | ✓ | ✓ | ✓ |
| 2 | `F43` | Januari DAN tiada earnings dalam 20 sesi akan datang | M105 Supertrend tulen (ditala 2) | MACD > isyarat DAN >= 30% di bawah puncak 52 minggu | 514 (141) | **23.0 (8.4)** | 48.2 (28.5) | 31.7 (43.0) | +20.1 / +14.8 / -0.0 | ✗ | ✗ | ✓ | ✓ |
| 3 | `F50` | SPY bawah SMA200 DAN earnings dalam 1-5 sesi akan datang | M73 ADX(5) > 40 + Julat Terkecil 6 Hari (ditala 2) | RSI14 < 40 DAN >= 30% di bawah puncak 52 minggu | 704 (256) | **25.0 (8.4)** | 46.6 (28.3) | 46.3 (43.1) | +21.2 / +14.3 / +15.2 | ✓ | ✓ | ✓ | ✓ |
| 4 | `F51` | SPY bawah SMA200 DAN earnings dalam 1-5 sesi akan datang | N16 RSI2<10 tanpa penapis | MACD > isyarat | 731 (183) | **21.1 (6.7)** | 41.9 (23.7) | 34.7 (36.4) | +9.9 / +16.6 / +16.0 | ✓ | ✓ | ✓ | ✓ |
| 5 | `F52` | Januari DAN tiada earnings dalam 20 sesi akan datang | M159 Heikin-Ashi Trend (ditala 2) | >= 30% di bawah puncak 52 minggu DAN ATR% >= 4 | 692 (161) | **24.3 (9.6)** | 47.3 (31.1) | 40.6 (47.2) | +20.7 / +17.8 / -5.6 | ✗ | ✗ | ✓ | ✗ |
| 6 | `F53` | Januari DAN tiada earnings dalam 20 sesi akan datang | M79 Radge: 20% Flipper (ditala 2) | RSI14 > 50 DAN >= 30% di bawah puncak 52 minggu | 340 (131) | **20.3 (9.1)** | 49.7 (29.9) | 33.8 (45.4) | +13.5 / +14.8 / -3.1 | ✗ | ✗ | ✓ | ✗ |
| 7 | `F54` | breadth thrust Zweig aktif (20 sesi) DAN sektor 3 terbawah (pulangan 63 sesi) | N73 Tutup bawah jalur bawah BB(20,2) | RSI14 < 40 DAN >= 30% di bawah puncak 52 minggu | 548 (183) | **19.5 (7.9)** | 43.2 (27.5) | 43.4 (41.8) | +14.9 / +6.0 / +3.6 | ✓ | ✓ | ✓ | ✓ |
| 8 | `F55` | turun-naik SPY 21 hari >= 25% setahun DAN sektor 3 terbawah (pulangan 63 sesi) | N75 RSI14 < 40 tanpa penapis | ADX < 20 DAN >= 30% di bawah puncak 52 minggu | 484 (115) | **22.3 (8.6)** | 44.8 (28.8) | 44.2 (43.6) | +21.4 / +9.7 / +17.0 | ✓ | ✓ | ✓ | ✓ |
| 9 | `F56` | QQQ >= 10% di bawah puncak | M01 Bollinger Band + RSI (ditala 2) | MACD > isyarat DAN >= 30% di bawah puncak 52 minggu | 1,926 (332) | **20.2 (8.4)** | 43.5 (28.2) | 44.3 (42.9) | +14.0 / +12.6 / +3.8 | ✗ | ✓ | ✓ | ✓ |
| 10 | `F57` | turun-naik SPY 21 hari >= 25% setahun DAN kejutan untung terkini positif (SUE > 0) | M94 Pecutan Momentum (Chen, Yu & Wang) (ditala 1) | ATR% >= 4 | 542 (15) | **21.2 (7.4)** | 48.5 (26.0) | 39.5 (39.3) | +12.3 / +15.5 / +4.6 | ✓ | ✓ | ✓ | ✓ |

- "Rawak" = semua saham layak sepanjang era yang sama dan tahap turun-naik yang sama. **T1:** kelebihan "capai +10 % dahulu" positif dalam K1, K2 dan K3. **T2:** kelebihan "lari" positif dalam ketiga-tiganya. **T3:** kelebihan lari melebihi persentil ke-95 peraturan rawak (+5.66 mata). **T4:** kelebihan lari (kumpulan B DAN K3) melebihi setup yang sama TANPA prasyarat.

**Setup lengkap: henti, pegang dan keluar dipilih ikut kadar tangkap yang direalisasi** (pindaan (j); dipilih pada kumpulan A, angka kumpulan B). **Jadi** = dagangan DIJUAL dengan untung bersih ≥ 10 % (kos 0.5 % ditolak; jurang melepasi henti dijual pada harga buka). "Rawak" = saham rawak (asas papan ini) dengan henti dan keluar yang sama. **Tangkap penuh** = saham itu lari (≥ 5 % minggu pertama, capai 10 %, kekal ≥ 10 % minggu ke-4) DAN dagangannya dijual dengan untung ≥ 10 %. "Pelari dipegang" = daripada saham yang lari, berapa % dijual dengan untung ≥ 10 %.

| ID | Henti | Keluar | Pegang (sesi) | **Tangkap penuh %** | **Jadi %** (rawak) | Kelebihan jadi K1 / K2 / K3 | Rugi ≥ 8 % % (rawak) | Pelari dipegang % | Jadi % tanpa keluar indikator | Jadi % dengan keluar lama (ikut purata) | **Menang %** (K1 / K2 / K3) | Purata setiap dagangan % K1 / K2 / K3 (maklumat) | L1 | L2 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `F49` | H4 4xATR14 | X12 RSI14 silang turun bawah 70 | 17.1 | **25.3** | **38.7 (19.4)** | +30.5 / +17.8 / +19.5 | 21.0 (25.3) | 96.4 | 37.9 | 38.4 | **65** (69 / 63 / 70) | +7.71 / +4.46 / +6.51 | ✓ | ✓ |
| `F43` | H4 4xATR14 | X00 tiada keluar indikator (henti + 20 sesi) | 19.4 | **22.5** | **36.5 (19.3)** | +25.1 / +19.6 / -6.6 | 16.5 (26.1) | 98.3 | 36.5 | 32.4 | **70** (79 / 78 / 32) | +7.83 / +8.42 / -4.45 | ✗ | ✓ |
| `F50` | H4 4xATR14 | X00 tiada keluar indikator (henti + 20 sesi) | 18.0 | **24.9** | **34.9 (19.1)** | +18.9 / +14.3 / +13.9 | 26.0 (26.2) | 98.9 | 34.9 | 34.9 | **58** (65 / 55 / 53) | +5.01 / +3.66 / +2.36 | ✓ | ✓ |
| `F51` | H4 4xATR14 | X10 histogram MACD turun 3 hari DAN X21 Stochastic silang turun di atas 80 | 17.5 | **19.4** | **29.7 (14.9)** | +10.1 / +17.7 / +12.2 | 18.6 (21.1) | 92.2 | 30.6 | 29.7 | **65** (63 / 65 / 63) | +3.05 / +5.89 / +4.16 | ✓ | ✗ |
| `F52` | H4 4xATR14 | X12 RSI14 silang turun bawah 70 DAN X20 tutup < 92% tutup tertinggi sejak beli | 19.3 | **23.6** | **37.5 (21.3)** | +23.9 / +19.7 / -9.0 | 20.1 (28.1) | 97.0 | 37.6 | 37.7 | **64** (72 / 67 / 40) | +6.70 / +8.02 / -4.54 | ✗ | ✗ |
| `F53` | H3 3xATR14 | X00 tiada keluar indikator (henti + 20 sesi) | 18.7 | **20.3** | **35.0 (20.1)** | +19.9 / +19.7 / -7.8 | 21.2 (30.9) | 100.0 | 35.0 | 34.5 | **65** (69 / 72 / 37) | +5.44 / +7.48 / -3.20 | ✗ | ✓ |
| `F54` | H4 4xATR14 | X12 RSI14 silang turun bawah 70 | 19.1 | **19.5** | **35.9 (17.2)** | +22.4 / +13.7 / +2.4 | 19.0 (23.3) | 100.0 | 35.9 | 35.2 | **63** (64 / 60 / 65) | +5.49 / +5.30 / +2.97 | ✓ | ✓ |
| `F55` | H4 4xATR14 | X10 histogram MACD turun 3 hari DAN X21 Stochastic silang turun di atas 80 | 19.3 | **21.7** | **42.4 (18.7)** | +26.7 / +19.4 / +34.0 | 12.0 (25.3) | 97.2 | 42.8 | 42.8 | **74** (76 / 69 / 87) | +8.44 / +6.13 / +12.10 | ✓ | ✗ |
| `F56` | H4 4xATR14 | X00 tiada keluar indikator (henti + 20 sesi) | 19.0 | **20.0** | **36.1 (19.1)** | +18.1 / +18.7 / +6.6 | 23.3 (26.1) | 98.0 | 36.1 | 35.2 | **60** (57 / 63 / 52) | +3.31 / +6.75 / -0.44 | ✓ | ✓ |
| `F57` | H3 3xATR14 | X12 RSI14 silang turun bawah 70 | 17.0 | **18.8** | **41.1 (15.6)** | +11.3 / +30.1 / +18.1 | 19.2 (23.7) | 88.7 | 42.3 | 35.8 | **70** (52 / 73 / 76) | +0.96 / +7.91 / +8.32 | ✓ | ✗ |

- **Menang %** = daripada 100 dagangan, berapa yang dijual dengan untung selepas kos (selebihnya rugi); baca bersama purata setiap dagangan, kerana kadar menang sahaja tidak menunjukkan saiz untung dan rugi.
- **L1:** kelebihan "jadi" atas rawak positif dalam K1, K2 dan K3. **L2:** "jadi" dengan keluar terpilih tidak kurang daripada tanpa keluar indikator (henti sama, pegang 20 sesi).

Dari mana datangnya kadar tangkap? Setiap sel: lari % (rawak %) · kena henti %, kumpulan B. "Tanpa pencetus" = semua saham layak yang memenuhi prasyarat dan penapis yang sama (maklumat tambahan, tidak dipradaftar):

| ID | Setup penuh | Syarat sahaja (buang prasyarat) | Prasyarat + penapis sahaja (buang pencetus) |
|---|---|---|---|
| `F49` | 26.2 (9.1) · 45.5 | 12.8 (9.4) · 51.0 | 23.1 (9.2) · 45.8 |
| `F43` | 23.0 (8.4) · 31.7 | 10.1 (8.5) · 47.0 | 14.6 (8.7) · 40.0 |
| `F50` | 25.0 (8.4) · 46.3 | 11.6 (8.5) · 45.9 | 24.1 (8.3) · 47.9 |
| `F51` | 21.1 (6.7) · 34.7 | 6.9 (5.9) · 34.6 | 17.5 (5.8) · 35.0 |
| `F52` | 24.3 (9.6) · 40.6 | 12.2 (9.6) · 52.7 | 14.2 (9.8) · 51.6 |
| `F53` | 20.3 (9.1) · 33.8 | 10.7 (8.9) · 48.6 | 13.2 (8.8) · 37.2 |
| `F54` | 19.5 (7.9) · 43.4 | 12.2 (8.5) · 47.7 | 15.0 (8.1) · 45.5 |
| `F55` | 22.3 (8.6) · 44.2 | 11.9 (8.7) · 47.9 | 16.0 (8.7) · 44.4 |
| `F56` | 20.2 (8.4) · 44.3 | 13.6 (8.4) · 46.9 | 14.7 (8.5) · 45.9 |
| `F57` | 21.2 (7.4) · 39.5 | 14.4 (9.4) · 51.6 | 16.8 (8.0) · 44.7 |

**Semakan kejujuran (jumlah).** 200 daripada 200 peraturan teratas memakai sekurang-kurangnya satu prasyarat; paling kerap: earnings dalam 1-5 sesi akan datang (159); SPY bawah SMA200 (68); tiada earnings dalam 20 sesi akan datang (18); QQQ >= 10% di bawah puncak (17); Januari (15); hari 90% turun kemudian naik (20 sesi) (15).

| Ukuran (kelebihan lari, mata peratus) | Kunci K1 (kumpulan B, 2010–2019) | Kunci K2 (kumpulan B, 2020–2024) | Kunci K3 (kumpulan B, 2025 – Ogo 2026) |
|---|---|---|---|
| Median, peraturan teratas (prasyarat sebenar) | +16.30 (200 / 200 positif) | +14.02 (200 / 200 positif) | +14.67 (127 / 141 positif) |
| Median, peraturan teratas PLASEBO | +8.35 (191 / 200 positif) | +10.77 (200 / 200 positif) | +0.62 (102 / 181 positif) |
| Median, peraturan rawak | -0.54 (74 / 200 positif) | -0.44 (77 / 200 positif) | +0.08 (89 / 177 positif) |
| Spearman skor lawan kelebihan (teratas) | +0.08 | +0.22 | -0.05 |

## 5. Setup lengkap bagi SETIAP kaedah: pegang dan keluar ikut kadar tangkap (kumpulan B)

Bagi setiap kaedah, peraturan masuk terbaik (syarat sahaja **S**, dan dengan prasyarat **P**) dipasangkan dengan henti × keluar yang paling kerap menghasilkan dagangan **jadi** (dijual dengan untung bersih ≥ 10 %), dipilih pada kumpulan A (pindaan (j)). Angka = median merentas kaedah, kumpulan B. Jadual setiap kaedah: `carian_setup/hasil/CS05/SEMUA_PENCETUS_LENGKAP.md`.

**Tangkap penuh** = saham itu lari (corak yang dicari: ≥ 5 % minggu pertama, capai 10 %, kekal ≥ 10 % minggu ke-4) DAN dijual dengan untung ≥ 10 %. **Jadi** lebih luas: apa-apa dagangan yang dijual dengan untung ≥ 10 %, termasuk yang naik perlahan.

| Kayu ukur masuk | Kaedah | Tangkap penuh %: S / P | Beza (P − S) · P > S | K3: beza · P > S | Jadi % (rawak): S / P | P > S (jadi) | Rugi ≥ 8 %: S / P | Pegang (sesi): S / P | Keluar terpilih tanpa indikator (X00): S / P | Keluar terpilih mengatasi X00: S / P |
|---|---|---|---|---|---|---|---|---|---|---|
| Pilih | 463 | 8.1 / 10.3 | +2.5 · 358 / 463 | +4.2 · 278 / 347 | 18.4 (16.9) / 16.1 (12.7) | 204 / 463 | 27.6 / 28.5 | 18.2 / 16.0 | 134 / 83 | 181 / 120 |
| Jumlah | 462 | 10.7 / 11.4 | +1.8 · 323 / 462 | +3.2 · 229 / 317 | 24.4 (20.6) / 17.4 (13.3) | 184 / 462 | 29.6 / 26.2 | 18.1 / 16.3 | 91 / 139 | 198 / 82 |

- Henti terpilih (dengan prasyarat): pilih: H1 56, H2 70, H3 87, H4 250; jumlah: H1 69, H2 66, H3 110, H4 217.
- Peraturan keluar terpilih berbentuk "DAN" (dua indikator mesti menyala serentak, jadi jarang menjual): pilih: S 197, P 292 daripada 463; jumlah: S 228, P 239 daripada 462.
- Median jadi tanpa keluar indikator (X00, henti sama): pilih: S 18.4 %, P 16.3 %; jumlah: S 24.4 %, P 17.6 %. Purata setiap dagangan (maklumat): pilih: S +0.26 %, P +0.11 %; jumlah: S +0.58 %, P +0.57 %.

## 6. Padanan jenis setup × prasyarat (kumpulan B, tanpa penapis)

Kelas dikunci secara mekanikal: **IKUT TREND** (434 pencetus) jika ≥ 50 % isyaratnya mempunyai RSI14 > 50; selainnya **PANTULAN** (31). Setiap sel = median merentas pencetus bagi perubahan bila prasyarat benar berbanding semua isyarat pencetus itu: **Δ lari** (kadar lari mutlak) / **Δ kelebihan** (lawan rawak hari sama) / **Δ henti** (kadar kena henti), mata peratus. "Plasebo" = Δ kelebihan dengan prasyarat dianjak masa.

| Prasyarat | % masa benar | Semua saham: lari % benar / palsu | Semua saham: kena henti % benar / palsu | IKUT TREND: Δ lari / Δ kelebihan / Δ henti | (plasebo) | PANTULAN: Δ lari / Δ kelebihan / Δ henti | (plasebo) |
|---|---|---|---|---|---|---|---|
| **Pasaran** | | | | | | | |
| QQQ ON | 60 | 4.5 / 6.9 | 30.8 / 33.1 | -0.4 / +0.1 / -0.3 | -0.0 | -1.6 / -0.1 / -1.1 | +0.0 |
| QQQ OFF | 40 | 6.9 / 4.5 | 33.1 / 30.8 | +0.7 / -0.2 / +0.3 | +0.1 | +1.0 / +0.1 / +1.0 | -0.1 |
| SPY atas SMA200 | 84 | 4.7 / 9.9 | 30.4 / 38.8 | -0.3 / +0.1 / -0.5 | -0.0 | -1.3 / -0.0 / -1.4 | +0.0 |
| SPY bawah SMA200 | 16 | 9.9 / 4.7 | 38.8 / 30.4 | +2.4 / -0.5 / +5.7 | +0.1 | +3.9 / +0.2 / +6.3 | -0.0 |
| QQQ dalam 3% dari puncak 52 minggu | 55 | 4.2 / 7.1 | 30.2 / 33.7 | -0.5 / +0.1 / -0.7 | +0.0 | -1.9 / -0.2 / -1.3 | +0.1 |
| QQQ >= 10% di bawah puncak | 15 | 9.7 / 4.8 | 39.4 / 30.4 | +2.0 / -0.4 / +7.6 | +0.1 | +4.0 / +0.1 / +4.0 | -0.2 |
| QQQ >= 20% di bawah puncak | 6 | 10.5 / 5.2 | 39.6 / 31.2 | +1.9 / -0.6 / +8.9 | +0.1 | +5.6 / +0.0 / +9.7 | +0.1 |
| rejim ON baharu (<= 10 sesi) | 20 | 4.6 / 5.7 | 30.3 / 32.1 | -0.5 / +0.1 / -1.9 | -0.0 | -1.7 / -0.0 / -0.6 | +0.1 |
| rejim OFF baharu (<= 10 sesi) | 19 | 5.5 / 5.5 | 33.0 / 31.4 | -0.1 / -0.2 / +0.5 | +0.3 | -0.2 / +0.1 / +2.0 | -0.2 |
| QQQ RSI14 < 35 | 4 | 11.1 / 5.3 | 31.1 / 31.8 | +3.0 / -1.3 / -1.9 | -0.1 | +4.2 / +0.1 / -1.3 | -0.2 |
| QQQ naik >= 3% dalam 5 sesi | 14 | 5.8 / 5.4 | 33.5 / 31.5 | +0.2 / -0.2 / +1.1 | +0.0 | +0.1 / +0.2 / +0.8 | -0.1 |
| turun-naik SPY 21 hari >= 25% setahun | 9 | 10.3 / 5.0 | 38.2 / 31.1 | +1.9 / -0.1 / +8.0 | -0.1 | +4.2 / +0.1 / +7.8 | +0.3 |
| turun-naik SPY 21 hari <= 10% setahun | 30 | 3.4 / 6.4 | 28.9 / 33.0 | -1.3 / +0.1 / -1.5 | +0.0 | -2.5 / -0.2 / -2.8 | +0.1 |
| turun-naik SPY menurun (21 hari < 63 hari) | 54 | 5.0 / 6.1 | 29.8 / 34.0 | -0.2 / +0.0 / -1.1 | +0.1 | -0.6 / -0.0 / -2.0 | +0.0 |
| >= 60% saham di atas MA50 | 51 | 4.3 / 6.8 | 29.9 / 33.7 | -0.5 / +0.0 / -1.1 | -0.1 | -1.6 / -0.2 / -1.5 | +0.0 |
| <= 30% saham di atas MA50 | 11 | 10.5 / 4.9 | 36.7 / 31.1 | +2.3 / -0.7 / +5.8 | -0.2 | +2.9 / +0.1 / +2.8 | -0.1 |
| keluasan naik >= 10 mata dalam 10 sesi | 25 | 5.1 / 5.6 | 31.1 / 31.9 | -0.1 / +0.1 / -1.3 | -0.0 | -0.7 / -0.2 / +1.1 | -0.0 |
| >= 60% saham di atas MA200 | 65 | 4.3 / 7.8 | 29.6 / 35.9 | -0.5 / +0.1 / -1.2 | -0.0 | -1.4 / -0.1 / -3.3 | +0.0 |
| >= 15% saham dalam 5% dari puncak 52 minggu | 74 | 4.3 / 8.9 | 29.9 / 36.8 | -0.5 / +0.1 / -0.9 | -0.1 | -1.6 / -0.1 / -1.7 | +0.0 |
| Nov-Apr | 49 | 5.7 / 5.3 | 32.4 / 31.1 | +0.3 / -0.0 / +0.1 | -0.1 | +0.3 / -0.0 / +1.8 | +0.1 |
| Mei-Okt | 51 | 5.3 / 5.7 | 31.1 / 32.4 | -0.2 / +0.0 / -0.2 | +0.1 | -0.2 / +0.0 / -1.5 | -0.0 |
| 7 hari pertama bulan | 23 | 5.9 / 5.4 | 31.7 / 31.8 | +0.6 / -0.0 / -0.7 | -0.1 | +0.8 / +0.0 / +0.8 | -0.0 |
| Januari | 8 | 6.3 / 5.4 | 33.0 / 31.6 | +1.3 / -0.1 / +0.2 | -0.2 | +0.5 / +0.2 / +2.2 | +0.1 |
| follow-through day aktif (QQQ, 20 sesi) | 17 | 6.2 / 5.3 | 34.8 / 31.1 | +0.5 / -0.1 / +1.8 | +0.0 | +0.4 / -0.1 / +3.0 | -0.1 |
| distribution day QQQ <= 2 dalam 25 sesi | 6 | 3.8 / 5.6 | 23.8 / 32.3 | -1.1 / +0.1 / -7.4 | +0.1 | -2.5 / -0.2 / -5.9 | -0.3 |
| distribution day QQQ >= 5 dalam 25 sesi | 69 | 6.1 / 4.1 | 33.7 / 27.4 | +0.4 / -0.1 / +1.6 | +0.0 | +0.6 / +0.0 / +1.1 | -0.0 |
| breadth thrust Zweig aktif (20 sesi) | 11 | 6.1 / 5.4 | 27.2 / 32.3 | +0.1 / -0.2 / -5.6 | +0.0 | +2.1 / -0.3 / -4.6 | +0.2 |
| nisbah 4% (10 hari) > 2 | 16 | 4.9 / 5.6 | 28.8 / 32.3 | -0.1 / +0.0 / -1.3 | -0.0 | -1.2 / -0.4 / -3.9 | +0.1 |
| nisbah 4% (10 hari) < 0.5 | 9 | 8.0 / 5.2 | 32.5 / 31.7 | +0.3 / -0.6 / -3.5 | +0.3 | +1.8 / +0.1 / +0.0 | -0.2 |
| regangan turun-naik SPY (proksi VIX) + SPY > SMA200 | 25 | 5.0 / 5.7 | 29.1 / 32.6 | +0.1 / +0.1 / -1.6 | +0.0 | -0.7 / +0.0 / -2.9 | -0.0 |
| QQQ SMA10 > SMA20 | 67 | 4.7 / 7.1 | 31.3 / 32.7 | -0.3 / +0.1 / -0.2 | -0.0 | -1.3 / -0.1 / +0.1 | +0.0 |
| SPY Peringkat 2 Weinstein (atas SMA150 yang naik) | 79 | 4.6 / 8.6 | 30.1 / 37.9 | -0.2 / +0.1 / -0.8 | +0.0 | -1.2 / -0.0 / -1.9 | -0.0 |
| hari 90% turun kemudian naik (20 sesi) | 28 | 6.9 / 4.9 | 31.8 / 31.7 | +0.4 / -0.3 / -1.2 | +0.0 | +1.3 / +0.2 / +0.6 | -0.0 |
| **Kumpulan / syarikat** | | | | | | | |
| sektor 3 teratas (pulangan 63 sesi) | 26 | 5.3 / 5.6 | 31.9 / 31.7 | +0.1 / +0.1 / +0.8 | +0.2 | -0.1 / -0.0 / -0.1 | +0.3 |
| sektor 3 terbawah (pulangan 63 sesi) | 22 | 6.0 / 5.3 | 33.6 / 31.2 | +0.2 / +0.1 / +0.7 | -0.1 | +0.2 / +0.0 / +2.4 | -0.3 |
| >= 60% saham sektor di atas MA50 | 48 | 4.4 / 6.5 | 30.1 / 33.3 | -0.3 / +0.1 / -0.7 | +0.1 | -1.5 / -0.2 / -1.7 | +0.2 |
| industri 20% teratas (pulangan 63 sesi) | 18 | 5.6 / 5.5 | 33.5 / 31.4 | +0.5 / +0.2 / +2.4 | +0.3 | +0.6 / +0.3 / +1.0 | +0.2 |
| industri 20% teratas (pulangan 21 sesi) | 18 | 5.4 / 5.5 | 33.2 / 31.4 | +0.3 / +0.0 / +1.8 | +0.1 | +0.6 / +0.2 / +0.9 | +0.4 |
| industri 20% terbawah (pulangan 63 sesi) | 17 | 6.3 / 5.3 | 34.7 / 31.1 | +0.1 / -0.1 / +1.8 | +0.0 | +0.5 / +0.0 / +2.2 | -0.2 |
| >= 60% saham industri di atas MA50 | 49 | 4.3 / 6.6 | 29.7 / 33.7 | -0.3 / +0.0 / -0.8 | -0.0 | -1.4 / -0.0 / -1.9 | +0.1 |
| saham lain dalam industri sama naik >= 20% dalam 20 sesi | 34 | 6.3 / 5.1 | 36.4 / 29.4 | +1.0 / +0.2 / +4.4 | +0.2 | +0.7 / +0.3 / +4.5 | +0.2 |
| earnings dalam 1-5 sesi akan datang | 7 | 12.0 / 5.0 | 36.4 / 31.4 | +5.9 / +5.3 / +5.0 | +0.7 | +6.9 / +5.6 / +4.3 | +1.0 |
| 0-4 sesi selepas earnings | 7 | 5.3 / 5.5 | 30.2 / 31.9 | +0.1 / -1.1 / -1.4 | +0.2 | -0.3 / -1.4 / -1.8 | +0.4 |
| 5-19 sesi selepas earnings | 21 | 4.6 / 5.7 | 29.6 / 32.3 | -0.6 / -0.7 / -2.2 | -0.2 | -1.0 / -0.8 / -1.4 | -0.4 |
| tiada earnings dalam 20 sesi akan datang | 60 | 4.7 / 6.6 | 29.3 / 35.4 | -0.6 / -0.6 / -2.5 | -0.1 | -0.7 / -0.6 / -1.8 | -0.1 |
| kejutan untung terkini positif (SUE > 0) | 46 | 5.1 / 5.8 | 30.2 / 33.1 | -0.2 / -0.1 / -1.5 | -0.1 | -0.3 / -0.1 / -1.5 | -0.1 |
| hasil suku terkini tumbuh >= 20% | 16 | 7.7 / 5.1 | 39.8 / 30.2 | +2.0 / +0.7 / +8.0 | +0.4 | +2.1 / +0.5 / +7.4 | +0.4 |
| harga melompat >= 5% pada hari earnings (20 sesi lalu) | 5 | 5.9 / 5.5 | 34.7 / 31.6 | +1.1 / -0.8 / +3.0 | +0.6 | +1.2 / -0.6 / +7.8 | +0.5 |

## 7. Kaveat

- Backtest sahaja; papan ialah pangkat, BUKAN bukti. Kohort jejak hadapan (`jejak_f/`) TIDAK berubah; menukar kohort ialah keputusan pengguna yang berasingan. Kad skor kekal satu-satunya keputusan wang sebenar.
- Lebih 100 juta peraturan dicuba: yang teratas pada kumpulan A sebahagiannya nasib. Sebab itu setiap angka di atas daripada kumpulan B, bersebelahan peraturan rawak dan plasebo.
- Prasyarat pasaran berubah ikut HARI: belian banyak tetapi hari isyarat berbeza sedikit (lajur "hari isyarat"); satu episod pasaran boleh menentukan hasil. K3 hanya 20 bulan.
- "Earnings akan datang" memakai tarikh sebenar (pandang ke hadapan ringan; papertrade memerlukan kalendar earnings). Peta sektor/industri ialah peta semasa. `QH07` ialah proksi (tiada VIX dalam repo).
- Tiada saham delist (condong ke atas); set 2000 bukan tapisan Shariah; data bermula 2010.
- Prasyarat yang menaikkan kadar lari selalunya turut menaikkan kadar kena henti: baca kedua-dua lajur.
