# Carian Setup CS06 — pangkat ikut TANGKAP PENUH; prasyarat + syarat bagi semua kaedah (backtest, BUKAN bukti)

> **Status keputusan (kad skor, harga 2026-11-12):** TERBUKTI 0 · CALON 0 · BELUM CUKUP 223 · GAGAL 0 · NEGATIF 0. Rejim QQQ OFF sejak 2026-10-16. Hanya **TERBUKTI** layak untuk wang sebenar (`laporan/KAD_SKOR.md`); nombor dalam laporan ini BUKAN keputusan dan tidak boleh dibaca sebagai pangkat untuk wang sebenar.

Dijana `kajian/carian_setup/cs_cs05.py` (`CS_PUS=CS06`). Pradaftar: `kajian/SPEC_CARIAN_SETUP.md` pindaan 14 Nov 2026 (k), dikomit sebelum pusingan ini dijalankan. **Jangan sunting secara manual.** Pusingan lama: `carian_setup/hasil/CS01`–`CS05/LAPORAN.md`; hasil tala: `carian_setup/hasil/CS06/TALA.md`.

## 1. Apa yang diuji

Setup lengkap = **prasyarat** (pasaran; kumpulan/syarikat) → **syarat** (pencetus + penapis saham itu sendiri) → **pegang**. Ukuran: KADAR TANGKAP PENUH = saham naik ≥ 5 % pada minggu pertama DAN dagangan DIJUAL dengan untung bersih ≥ 10 % selepas dipegang hingga 20 sesi dengan henti 4×ATR14 (pegang piawai: tiada sasaran untung, tiada jual awal). CS05 memangkatkan ikut label "lari" (henti −8 % tetap); CS06 memangkatkan terus ikut hasil dagangan. Dua kayu ukur:

- **Pilih:** kadar tangkap penuh setup tolak saham rawak pada **hari yang sama** dan tahap turun-naik sama. Mengukur kemahiran memilih saham. Prasyarat pasaran menaikkan saham rawak hari itu juga, jadi ia hanya dikira jika pencetus memilih lebih baik pada hari begitu.
- **Jumlah:** kadar tangkap penuh setup tolak saham rawak **sepanjang era**. Memasukkan kesan BILA membeli (sumbangan prasyarat pasaran). Hari isyarat berkelompok, jadi baca bersama plasebo dan bilangan hari isyarat.

Carian (kumpulan A, 2010–2024): 500 pencetus (465 cukup isyarat) × 34 pilihan prasyarat pasaran × 16 pilihan prasyarat kumpulan/syarikat × 379 gabungan penapis saham = **103,088,000 peraturan masuk dicuba**, 43,784,217 cukup isyarat (≥ 100 dalam setiap era). Carian yang sama diulang dengan prasyarat **plasebo** (dianjak 437 sesi). Angka di bawah daripada **kumpulan B** (saham yang carian tidak lihat), 2010 – Ogo 2026; **K3 = 2025 – Ogo 2026 ialah ujian sebenar**.

## 2. Jawapan ringkas: adakah prasyarat menolong?

Bagi setiap pencetus, tiga peraturan dipilih pada kumpulan A: terbaik **syarat sahaja** (S), terbaik **dengan prasyarat** (P) dan terbaik dengan **prasyarat plasebo** (PL); semuanya diukur pada kumpulan B. Bacaan dikunci (pindaan (i) butir 6): prasyarat "menolong" hanya jika median (P − S) positif DAN melebihi median (PL − S).

| Kayu ukur | Pencetus dibanding | Median tangkap penuh %: S / P / PL | Median kena henti %: S / P / PL | Median kelebihan: S / P / PL | Median (P − S) | Median (PL − S) | P > S | P > PL | **Menolong?** |
|---|---|---|---|---|---|---|---|---|---|
| Pilih, kumpulan B | 461 | 9.3 / 11.1 / 10.7 | 45.9 / 39.8 / 48.1 | +1.07 / +5.52 / +1.69 | +4.50 | +0.57 | 432 / 461 | 413 / 461 | **YA** |
| Pilih, K3 sahaja | 304 | | | | +5.54 | +0.49 | 264 / 304 | 250 / 304 | **YA** |
| Jumlah, kumpulan B | 453 | 11.8 / 12.7 / 12.3 | 52.1 / 39.1 / 38.9 | +2.20 / +6.82 / +4.60 | +4.83 | +2.12 | 403 / 453 | 324 / 453 | **YA** |
| Jumlah, K3 sahaja | 191 | | | | +5.30 | +0.40 | 158 / 191 | 147 / 191 | **YA** |

Unit kelebihan dan beza: mata peratus. Jadual setiap pencetus: `carian_setup/hasil/CS06/SEMUA_PENCETUS.md`.

**Banding dengan CS05 (yang memangkatkan ikut label "lari"):** kayu ukur pilih: 115 daripada 200 peraturan teratas CS06 juga berada dalam 200 teratas CS05 (Spearman skor antara yang sama +0.47); 6 daripada 10 setup papan mempunyai peraturan masuk yang sama; kayu ukur jumlah: 118 daripada 200 peraturan teratas CS06 juga berada dalam 200 teratas CS05 (Spearman skor antara yang sama +0.44); 2 daripada 10 setup papan mempunyai peraturan masuk yang sama.

## 3. Papan 10 teratas — kayu ukur PILIH (lawan saham rawak HARI SAMA)

| # | ID | Prasyarat | Pencetus | Penapis saham | Belian (hari isyarat) | **Tangkap penuh %** (rawak) | Capai +10 % dahulu % (rawak) | Kena henti −8 % dahulu % (rawak) | Kelebihan tangkap penuh K1 / K2 / K3 | T1 | T2 | T3 | T4 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `F39` | rejim ON baharu (<= 10 sesi) DAN earnings dalam 1-5 sesi akan datang | M73 ADX(5) > 40 + Julat Terkecil 6 Hari (ditala 2) | tutup > MA50 DAN >= 30% di bawah puncak 52 minggu | 501 (242) | **21.2 (10.5)** | 41.7 (33.9) | 42.5 (35.0) | +11.4 / +9.2 / +12.0 | ✓ | ✓ | ✓ | ✓ |
| 2 | `F40` | rejim ON baharu (<= 10 sesi) DAN earnings dalam 1-5 sesi akan datang | M14 Walking with the Whales (ditala 2) | Supertrend naik DAN >= 30% di bawah puncak 52 minggu | 597 (262) | **21.9 (10.6)** | 44.6 (34.7) | 42.4 (36.5) | +11.3 / +10.3 / +13.5 | ✓ | ✓ | ✓ | ✓ |
| 3 | `F58` | >= 60% saham di atas MA50 DAN earnings dalam 1-5 sesi akan datang | N16 RSI2<10 tanpa penapis | Supertrend naik DAN >= 30% di bawah puncak 52 minggu | 379 (240) | **19.8 (7.6)** | 38.5 (26.3) | 47.5 (46.4) | +12.7 / +10.5 / +15.8 | ✓ | ✓ | ✓ | ✓ |
| 4 | `F42` | distribution day QQQ <= 2 dalam 25 sesi DAN >= 60% saham industri di atas MA50 | M159 Heikin-Ashi Trend (ditala 1) | RS >= 90 DAN ATR% >= 4 | 303 (137) | **15.5 (8.1)** | 38.0 (29.6) | 48.8 (39.9) | +7.0 / +9.1 / +1.7 | ✓ | ✓ | ✓ | ✗ |
| 5 | `F45` | turun-naik SPY menurun (21 hari < 63 hari) DAN hasil suku terkini tumbuh >= 20% | M94 Pecutan Momentum (Chen, Yu & Wang) (ditala 1) | MACD > 0 DAN ATR% >= 4 | 786 (92) | **17.0 (12.2)** | 41.9 (36.0) | 47.7 (43.8) | +2.5 / +6.1 / +4.8 | ✓ | ✓ | ✗ | ✓ |
| 6 | `F59` | distribution day QQQ <= 2 dalam 25 sesi | P09 tutup silang atas MA20 | RS >= 70 DAN ATR% >= 4 | 308 (140) | **13.6 (9.0)** | 40.3 (31.1) | 46.8 (40.6) | +5.0 / +5.6 / -7.0 | ✓ | ✗ | ✗ | ✗ |
| 7 | `F44` | turun-naik SPY menurun (21 hari < 63 hari) DAN kejutan untung terkini positif (SUE > 0) | M79 Radge: 20% Flipper (ditala 2) | templat trend Minervini DAN ATR% >= 4 | 602 (400) | **14.0 (10.0)** | 35.2 (32.0) | 53.8 (47.8) | +4.6 / +3.1 / +4.8 | ✓ | ✓ | ✗ | ✓ |
| 8 | `F60` | SPY atas SMA200 DAN >= 60% saham sektor di atas MA50 | N119 3 tutup turun berturut | RS >= 90 DAN ATR% >= 4 | 3,099 (1,442) | **13.5 (9.0)** | 37.4 (30.1) | 53.3 (47.3) | +4.8 / +4.1 / +5.3 | ✓ | ✓ | ✗ | ✓ |
| 9 | `F61` | turun-naik SPY menurun (21 hari < 63 hari) DAN kejutan untung terkini positif (SUE > 0) | N29 PSAR naik + tutup>MA50 | templat trend Minervini DAN ATR% >= 4 | 1,415 (752) | **12.2 (9.6)** | 33.4 (30.6) | 53.6 (48.3) | +4.9 / +1.9 / +2.2 | ✓ | ✓ | ✗ | ✓ |
| 10 | `F47` | regangan turun-naik SPY (proksi VIX) + SPY > SMA200 DAN hasil suku terkini tumbuh >= 20% | M124 'Last' Stochastic Technique (ChartSchool) (ditala 2) | Supertrend naik DAN volum hari isyarat >= 1.5x purata 50 | 392 (262) | **9.9 (8.2)** | 25.5 (26.7) | 38.3 (38.1) | +2.6 / +1.6 / -0.3 | ✗ | ✗ | ✗ | ✓ |

- "Rawak" = saham lain yang layak pada hari yang sama dan tahap turun-naik yang sama. **T1:** kelebihan "capai +10 % dahulu" positif dalam K1, K2 dan K3. **T2:** kelebihan "tangkap penuh" positif dalam ketiga-tiganya. **T3:** kelebihan tangkap penuh melebihi persentil ke-95 peraturan rawak (+5.47 mata). **T4:** kelebihan tangkap penuh (kumpulan B DAN K3) melebihi setup yang sama TANPA prasyarat.

**Setup lengkap: henti, pegang dan keluar dipilih ikut kadar tangkap penuh setup itu sendiri** (pindaan (k); dipilih pada kumpulan A, angka kumpulan B). **Tangkap penuh** = naik ≥ 5 % minggu pertama DAN dagangan DIJUAL dengan untung bersih ≥ 10 % mengikut henti dan keluar setup ini (kos 0.5 % ditolak; jurang melepasi henti dijual pada harga buka). **Jadi** = apa-apa dagangan yang dijual dengan untung ≥ 10 %. "Rawak" = saham rawak (asas papan ini) dengan henti dan keluar yang sama.

| ID | Henti | Keluar | Pegang (sesi) | **Tangkap penuh %** (rawak) | Kelebihan K1 / K2 / K3 | Jadi % (rawak) | Rugi ≥ 8 % % (rawak) | Tangkap penuh % tanpa keluar indikator | Purata setiap dagangan % K1 / K2 / K3 (maklumat) | L1 | L2 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `F39` | H3 3xATR14 | X09 MACD < isyarat DAN X21 Stochastic silang turun di atas 80 | 15.8 | **21.4 (10.4)** | +11.5 / +9.8 / +12.2 | 27.3 (20.3) | 32.9 (23.6) | 21.2 | +1.13 / +2.49 / +1.71 | ✓ | ✓ |
| `F40` | H3 3xATR14 | X13 RSI14 > 80 | 15.2 | **22.9 (10.7)** | +12.4 / +11.2 / +14.3 | 29.0 (20.6) | 32.0 (26.0) | 21.9 | +2.06 / +2.68 / +1.42 | ✓ | ✓ |
| `F58` | H3 3xATR14 | X12 RSI14 silang turun bawah 70 | 14.4 | **22.1 (7.4)** | +15.1 / +13.2 / +18.6 | 29.7 (16.5) | 36.1 (29.1) | 19.8 | +1.77 / -0.90 / +2.53 | ✓ | ✓ |
| `F42` | H1 -8% | X00 tiada keluar indikator (henti + 20 sesi) | 13.4 | **13.7 (7.6)** | +6.0 / +6.9 / +1.6 | 23.2 (16.9) | 52.4 (42.1) | 13.7 | -0.02 / +6.37 / +1.64 | ✓ | ✓ |
| `F45` | H2 -10% | X12 RSI14 silang turun bawah 70 | 10.9 | **14.3 (12.3)** | +0.7 / +2.6 / +2.0 | 22.4 (20.5) | 37.9 (37.1) | 16.1 | -1.00 / +2.45 / +2.43 | ✓ | ✗ |
| `F59` | H2 -10% | X01 tutup < MA10 DAN X12 RSI14 silang turun bawah 70 | 15.0 | **13.6 (8.7)** | +5.4 / +5.5 / -6.5 | 25.9 (18.1) | 44.6 (33.5) | 13.6 | +0.44 / +3.58 / +1.05 | ✗ | ✓ |
| `F44` | H1 -8% | X09 MACD < isyarat DAN X21 Stochastic silang turun di atas 80 | 11.6 | **12.4 (9.3)** | +3.7 / +3.5 / +1.8 | 20.4 (18.0) | 58.0 (49.3) | 12.6 | +0.96 / +0.81 / -1.61 | ✓ | ✗ |
| `F60` | H3 3xATR14 | X12 RSI14 silang turun bawah 70 DAN X22 hari turun dengan volum >= 1.5x | 16.9 | **13.7 (9.0)** | +4.8 / +4.5 / +5.1 | 26.7 (19.7) | 33.5 (32.5) | 13.6 | +0.25 / +1.80 / +2.14 | ✓ | ✓ |
| `F61` | H3 3xATR14 | X13 RSI14 > 80 | 16.4 | **12.3 (9.6)** | +5.1 / +2.1 / +2.1 | 24.4 (21.1) | 34.7 (31.7) | 12.2 | +0.85 / +0.81 / -0.20 | ✓ | ✓ |
| `F47` | H3 3xATR14 | X04 tutup < EMA10 DAN X12 RSI14 silang turun bawah 70 | 17.3 | **9.7 (8.0)** | +2.1 / +1.8 / -0.1 | 20.1 (17.6) | 26.0 (25.1) | 9.9 | +0.30 / +1.32 / -0.26 | ✗ | ✗ |

- **L1:** kelebihan tangkap penuh atas rawak positif dalam K1, K2 dan K3. **L2:** tangkap penuh dengan keluar terpilih tidak kurang daripada tanpa keluar indikator (henti sama, pegang 20 sesi).

Dari mana datangnya kadar tangkap? Setiap sel: tangkap penuh % (rawak %) · kena henti %, kumpulan B. "Tanpa pencetus" = semua saham layak yang memenuhi prasyarat dan penapis yang sama (maklumat tambahan, tidak dipradaftar):

| ID | Setup penuh | Syarat sahaja (buang prasyarat) | Prasyarat + penapis sahaja (buang pencetus) |
|---|---|---|---|
| `F39` | 21.2 (10.5) · 42.5 | 9.3 (8.6) · 47.5 | 20.2 (9.6) · 43.5 |
| `F40` | 21.9 (10.6) · 42.4 | 10.1 (9.0) · 47.9 | 21.1 (10.6) · 41.8 |
| `F58` | 19.8 (7.6) · 47.5 | 11.7 (10.2) · 46.3 | 16.3 (7.7) · 49.3 |
| `F42` | 15.5 (8.1) · 48.8 | 12.4 (9.9) · 54.2 | 13.4 (7.7) · 50.3 |
| `F45` | 17.0 (12.2) · 47.7 | 14.5 (11.8) · 51.8 | 12.1 (9.8) · 53.2 |
| `F59` | 13.6 (9.0) · 46.8 | 11.6 (10.5) · 52.7 | 13.1 (8.7) · 45.2 |
| `F44` | 14.0 (10.0) · 53.8 | 12.6 (9.7) · 55.6 | 12.3 (9.9) · 51.9 |
| `F60` | 13.5 (9.0) · 53.3 | 13.8 (10.5) · 53.4 | 12.7 (8.8) · 55.5 |
| `F61` | 12.2 (9.6) · 53.6 | 10.8 (9.6) · 54.8 | 12.3 (9.9) · 51.9 |
| `F47` | 9.9 (8.2) · 38.3 | 6.5 (6.6) · 34.1 | 8.4 (6.8) · 35.6 |

Taburan belian mengikut tahun (kumpulan B, 2010 – Ogo 2026; maklumat tambahan). Setup yang beliannya tertumpu pada satu dua tahun bergantung pada beberapa episod pasaran sahaja:

| ID | Belian | Hari isyarat | Tahun dengan belian | Dua tahun terbanyak: % belian | Tahun terbanyak: belian / hari / kadar % | Kadar % setiap tahun (≥ 30 belian): terendah – tertinggi |
|---|---|---|---|---|---|---|
| `F39` | 501 | 242 | 17 | 35 | 2022: 99 / 17 / 23 | 13 – 27 (8 tahun) |
| `F40` | 597 | 262 | 17 | 31 | 2022: 105 / 21 / 21 | 10 – 40 (9 tahun) |
| `F58` | 379 | 240 | 17 | 23 | 2016: 45 / 20 / 18 | 12 – 30 (5 tahun) |
| `F42` | 303 | 137 | 13 | 33 | 2020: 57 / 15 / 21 | 6 – 21 (4 tahun) |
| `F45` | 786 | 92 | 17 | 37 | 2020: 203 / 7 / 25 | 4 – 25 (8 tahun) |
| `F59` | 308 | 140 | 13 | 40 | 2020: 69 / 18 / 23 | 3 – 23 (5 tahun) |
| `F44` | 602 | 400 | 17 | 38 | 2021: 129 / 66 / 16 | 12 – 18 (6 tahun) |
| `F60` | 3,099 | 1,442 | 17 | 26 | 2020: 435 / 128 / 20 | 6 – 20 (17 tahun) |
| `F61` | 1,415 | 752 | 17 | 36 | 2021: 302 / 99 / 14 | 5 – 17 (14 tahun) |
| `F47` | 392 | 262 | 17 | 27 | 2021: 55 / 31 / 4 | 4 – 14 (4 tahun) |

**Semakan kejujuran (pilih).** 200 daripada 200 peraturan teratas memakai sekurang-kurangnya satu prasyarat; paling kerap: earnings dalam 1-5 sesi akan datang (200); >= 15% saham dalam 5% dari puncak 52 minggu (42); SPY atas SMA200 (29); SPY Peringkat 2 Weinstein (atas SMA150 yang naik) (27); QQQ dalam 3% dari puncak 52 minggu (22); >= 60% saham di atas MA200 (17).

| Ukuran (kelebihan tangkap penuh, mata peratus) | Kunci K1 (kumpulan B, 2010–2019) | Kunci K2 (kumpulan B, 2020–2024) | Kunci K3 (kumpulan B, 2025 – Ogo 2026) |
|---|---|---|---|
| Median, peraturan teratas (prasyarat sebenar) | +9.79 (200 / 200 positif) | +8.19 (200 / 200 positif) | +10.21 (192 / 193 positif) |
| Median, peraturan teratas PLASEBO | +3.95 (196 / 200 positif) | +4.15 (189 / 200 positif) | +2.40 (158 / 188 positif) |
| Median, peraturan rawak | +0.16 (109 / 200 positif) | +0.04 (103 / 200 positif) | +0.85 (108 / 177 positif) |
| Spearman skor lawan kelebihan (teratas) | +0.10 | +0.01 | +0.05 |

## 4. Papan 10 teratas — kayu ukur JUMLAH (lawan saham rawak sepanjang ERA)

| # | ID | Prasyarat | Pencetus | Penapis saham | Belian (hari isyarat) | **Tangkap penuh %** (rawak) | Capai +10 % dahulu % (rawak) | Kena henti −8 % dahulu % (rawak) | Kelebihan tangkap penuh K1 / K2 / K3 | T1 | T2 | T3 | T4 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `F62` | QQQ >= 20% di bawah puncak | M73 ADX(5) > 40 + Julat Terkecil 6 Hari (ditala 1) | RSI14 < 40 DAN >= 30% di bawah puncak 52 minggu | 1,314 (144) | **37.1 (8.4)** | 48.9 (28.0) | 39.8 (43.0) | +54.5 / +26.0 / +31.2 | ✓ | ✓ | ✓ | ✓ |
| 2 | `F49` | QQQ >= 10% di bawah puncak DAN earnings dalam 1-5 sesi akan datang | N119 3 tutup turun berturut | MACD > isyarat DAN ATR% >= 4 | 1,068 (201) | **29.4 (9.2)** | 47.0 (29.9) | 45.5 (45.4) | +21.6 / +19.5 / +22.7 | ✓ | ✓ | ✓ | ✓ |
| 3 | `F63` | QQQ OFF DAN earnings dalam 1-5 sesi akan datang | N16 RSI2<10 tanpa penapis | MACD > isyarat DAN >= 30% di bawah puncak 52 minggu | 431 (194) | **25.5 (8.6)** | 44.1 (28.7) | 46.4 (43.7) | +21.6 / +16.1 / +10.2 | ✓ | ✓ | ✓ | ✓ |
| 4 | `F43` | Januari DAN tiada earnings dalam 20 sesi akan datang | M105 Supertrend tulen (ditala 2) | MACD > isyarat DAN >= 30% di bawah puncak 52 minggu | 514 (141) | **22.8 (8.4)** | 48.2 (28.5) | 31.7 (43.0) | +19.9 / +14.1 / +0.9 | ✗ | ✓ | ✓ | ✓ |
| 5 | `F64` | turun-naik SPY 21 hari >= 25% setahun DAN kejutan untung terkini positif (SUE > 0) | M01 Bollinger Band + RSI (ditala 2) | ADX > 25 DAN >= 30% di bawah puncak 52 minggu | 687 (148) | **26.2 (8.2)** | 47.6 (27.9) | 41.5 (42.1) | +16.7 / +17.3 / +21.6 | ✓ | ✓ | ✓ | ✓ |
| 6 | `F65` | SPY bawah SMA200 DAN earnings dalam 1-5 sesi akan datang | P14 RSI14 silang atas 30 | RSI14 < 40 DAN volum 10 hari > volum 50 hari | 426 (144) | **21.8 (6.0)** | 43.2 (22.3) | 37.1 (34.3) | +18.4 / +12.5 / +11.8 | ✓ | ✓ | ✓ | ✓ |
| 7 | `F66` | <= 30% saham di atas MA50 DAN kejutan untung terkini positif (SUE > 0) | M79 Radge: 20% Flipper (ditala 2) | >= 30% di bawah puncak 52 minggu DAN tutup dalam 25% teratas julat hari | 709 (134) | **22.1 (8.8)** | 40.2 (29.1) | 53.5 (44.1) | +16.7 / +15.9 / -2.7 | ✓ | ✗ | ✓ | ✗ |
| 8 | `F67` | turun-naik SPY 21 hari >= 25% setahun DAN kejutan untung terkini positif (SUE > 0) | N75 RSI14 < 40 tanpa penapis | MACD > isyarat DAN >= 30% di bawah puncak 52 minggu | 609 (135) | **26.8 (8.5)** | 47.5 (28.5) | 39.2 (43.1) | +15.3 / +16.3 / +30.3 | ✓ | ✓ | ✓ | ✓ |
| 9 | `F68` | breadth thrust Zweig aktif (20 sesi) | N73 Tutup bawah jalur bawah BB(20,2) | ADX < 20 DAN >= 30% di bawah puncak 52 minggu | 636 (197) | **18.4 (8.1)** | 42.1 (27.8) | 42.8 (42.3) | +10.2 / +11.5 / +2.8 | ✓ | ✓ | ✓ | ✗ |
| 10 | `F69` | turun-naik SPY 21 hari >= 25% setahun | M28 VWAP Separator + Kiss Pivot (ditala 2) | >= 30% di bawah puncak 52 minggu DAN volum hari isyarat >= 1.5x purata 50 | 1,489 (225) | **22.3 (8.5)** | 37.3 (28.5) | 52.1 (43.1) | +14.2 / +13.1 / +15.4 | ✓ | ✓ | ✓ | ✓ |

- "Rawak" = semua saham layak sepanjang era yang sama dan tahap turun-naik yang sama. **T1:** kelebihan "capai +10 % dahulu" positif dalam K1, K2 dan K3. **T2:** kelebihan "tangkap penuh" positif dalam ketiga-tiganya. **T3:** kelebihan tangkap penuh melebihi persentil ke-95 peraturan rawak (+5.54 mata). **T4:** kelebihan tangkap penuh (kumpulan B DAN K3) melebihi setup yang sama TANPA prasyarat.

**Setup lengkap: henti, pegang dan keluar dipilih ikut kadar tangkap penuh setup itu sendiri** (pindaan (k); dipilih pada kumpulan A, angka kumpulan B). **Tangkap penuh** = naik ≥ 5 % minggu pertama DAN dagangan DIJUAL dengan untung bersih ≥ 10 % mengikut henti dan keluar setup ini (kos 0.5 % ditolak; jurang melepasi henti dijual pada harga buka). **Jadi** = apa-apa dagangan yang dijual dengan untung ≥ 10 %. "Rawak" = saham rawak (asas papan ini) dengan henti dan keluar yang sama.

| ID | Henti | Keluar | Pegang (sesi) | **Tangkap penuh %** (rawak) | Kelebihan K1 / K2 / K3 | Jadi % (rawak) | Rugi ≥ 8 % % (rawak) | Tangkap penuh % tanpa keluar indikator | Purata setiap dagangan % K1 / K2 / K3 (maklumat) | L1 | L2 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `F62` | H3 3xATR14 | X21 Stochastic silang turun di atas 80 | 15.9 | **35.5 (7.0)** | +56.1 / +25.9 / +32.7 | 48.2 (12.8) | 16.1 (21.1) | 36.5 | +15.42 / +9.28 / +17.73 | ✓ | ✗ |
| `F49` | H4 4xATR14 | X12 RSI14 silang turun bawah 70 | 17.1 | **30.1 (9.0)** | +24.7 / +20.5 / +21.8 | 38.7 (19.4) | 21.0 (25.3) | 29.4 | +7.71 / +4.46 / +6.51 | ✓ | ✓ |
| `F63` | H4 4xATR14 | X00 tiada keluar indikator (henti + 20 sesi) | 17.9 | **25.5 (8.6)** | +21.6 / +16.1 / +10.2 | 34.3 (19.5) | 26.5 (26.4) | 25.5 | +6.01 / +4.21 / +2.39 | ✓ | ✓ |
| `F43` | H3 3xATR14 | X00 tiada keluar indikator (henti + 20 sesi) | 18.6 | **22.7 (8.4)** | +19.9 / +14.0 / +0.8 | 36.4 (18.9) | 18.2 (29.4) | 22.7 | +7.73 / +7.90 / -3.70 | ✓ | ✓ |
| `F64` | H3 3xATR14 | X00 tiada keluar indikator (henti + 20 sesi) | 18.3 | **27.3 (8.3)** | +16.3 / +19.1 / +21.6 | 46.3 (18.6) | 19.4 (28.6) | 27.3 | +6.54 / +8.76 / +13.17 | ✓ | ✓ |
| `F65` | H3 3xATR14 | X12 RSI14 silang turun bawah 70 | 16.9 | **21.7 (5.7)** | +18.7 / +12.7 / +12.2 | 29.2 (13.0) | 25.0 (19.5) | 21.7 | +3.14 / +2.23 / +3.29 | ✓ | ✓ |
| `F66` | H3 3xATR14 | X00 tiada keluar indikator (henti + 20 sesi) | 18.7 | **22.6 (8.8)** | +16.4 / +16.6 / -2.2 | 42.3 (19.6) | 22.2 (30.2) | 22.6 | +2.51 / +6.56 / +9.13 | ✗ | ✓ |
| `F67` | H2 -10% | X20 tutup < 92% tutup tertinggi sejak beli DAN X21 Stochastic silang turun di atas 80 | 14.8 | **23.6 (8.3)** | +14.7 / +13.2 / +26.2 | 35.7 (17.4) | 34.4 (37.4) | 24.4 | +1.95 / +4.66 / +10.71 | ✓ | ✗ |
| `F68` | H3 3xATR14 | X20 tutup < 92% tutup tertinggi sejak beli DAN X21 Stochastic silang turun di atas 80 | 17.5 | **18.5 (8.0)** | +10.5 / +11.6 / +2.9 | 34.5 (18.1) | 28.4 (28.6) | 18.5 | +2.67 / +8.82 / +3.77 | ✓ | ✓ |
| `F69` | H3 3xATR14 | X00 tiada keluar indikator (henti + 20 sesi) | 17.5 | **23.7 (8.6)** | +14.4 / +15.2 / +15.3 | 38.9 (19.1) | 24.0 (29.4) | 23.7 | +2.32 / +4.20 / +12.17 | ✓ | ✓ |

- **L1:** kelebihan tangkap penuh atas rawak positif dalam K1, K2 dan K3. **L2:** tangkap penuh dengan keluar terpilih tidak kurang daripada tanpa keluar indikator (henti sama, pegang 20 sesi).

Dari mana datangnya kadar tangkap? Setiap sel: tangkap penuh % (rawak %) · kena henti %, kumpulan B. "Tanpa pencetus" = semua saham layak yang memenuhi prasyarat dan penapis yang sama (maklumat tambahan, tidak dipradaftar):

| ID | Setup penuh | Syarat sahaja (buang prasyarat) | Prasyarat + penapis sahaja (buang pencetus) |
|---|---|---|---|
| `F62` | 37.1 (8.4) · 39.8 | 13.7 (8.5) · 44.2 | 22.2 (8.8) · 43.2 |
| `F49` | 29.4 (9.2) · 45.5 | 13.2 (9.5) · 51.0 | 24.5 (9.3) · 45.8 |
| `F63` | 25.5 (8.6) · 46.4 | 12.6 (8.6) · 47.3 | 21.9 (8.4) · 48.6 |
| `F43` | 22.8 (8.4) · 31.7 | 10.1 (8.5) · 47.0 | 14.4 (8.7) · 40.0 |
| `F64` | 26.2 (8.2) · 41.5 | 14.0 (8.3) · 45.7 | 23.3 (8.2) · 43.1 |
| `F65` | 21.8 (6.0) · 37.1 | 7.1 (6.4) · 36.2 | 21.9 (6.2) · 40.8 |
| `F66` | 22.1 (8.8) · 53.5 | 12.6 (9.2) · 52.3 | 17.8 (8.0) · 47.0 |
| `F67` | 26.8 (8.5) · 39.2 | 12.6 (8.5) · 47.2 | 18.6 (8.2) · 42.1 |
| `F68` | 18.4 (8.1) · 42.8 | 12.7 (8.8) · 47.0 | 13.1 (8.0) · 45.9 |
| `F69` | 22.3 (8.5) · 52.1 | 13.1 (8.7) · 49.9 | 22.5 (8.7) · 49.7 |

Taburan belian mengikut tahun (kumpulan B, 2010 – Ogo 2026; maklumat tambahan). Setup yang beliannya tertumpu pada satu dua tahun bergantung pada beberapa episod pasaran sahaja:

| ID | Belian | Hari isyarat | Tahun dengan belian | Dua tahun terbanyak: % belian | Tahun terbanyak: belian / hari / kadar % | Kadar % setiap tahun (≥ 30 belian): terendah – tertinggi |
|---|---|---|---|---|---|---|
| `F62` | 1,314 | 144 | 5 | 86 | 2022: 603 / 117 / 15 | 12 – 60 (4 tahun) |
| `F49` | 1,068 | 201 | 13 | 68 | 2022: 423 / 89 / 21 | 20 – 41 (5 tahun) |
| `F63` | 431 | 194 | 15 | 48 | 2022: 164 / 42 / 24 | 7 – 43 (5 tahun) |
| `F43` | 514 | 141 | 16 | 50 | 2019: 134 / 11 / 32 | 10 – 43 (5 tahun) |
| `F64` | 687 | 148 | 7 | 65 | 2020: 230 / 23 / 41 | 7 – 56 (5 tahun) |
| `F65` | 426 | 144 | 13 | 39 | 2022: 84 / 46 / 13 | 13 – 52 (5 tahun) |
| `F66` | 709 | 134 | 14 | 61 | 2020: 273 / 17 / 37 | 4 – 49 (5 tahun) |
| `F67` | 609 | 135 | 7 | 68 | 2022: 253 / 55 / 9 | 9 – 55 (5 tahun) |
| `F68` | 636 | 197 | 14 | 36 | 2020: 120 / 16 / 38 | 0 – 38 (9 tahun) |
| `F69` | 1,489 | 225 | 8 | 61 | 2020: 502 / 44 / 31 | 0 – 31 (6 tahun) |

**Semakan kejujuran (jumlah).** 200 daripada 200 peraturan teratas memakai sekurang-kurangnya satu prasyarat; paling kerap: earnings dalam 1-5 sesi akan datang (143); SPY bawah SMA200 (58); QQQ >= 20% di bawah puncak (33); QQQ >= 10% di bawah puncak (24); tiada earnings dalam 20 sesi akan datang (18); hari 90% turun kemudian naik (20 sesi) (16).

| Ukuran (kelebihan tangkap penuh, mata peratus) | Kunci K1 (kumpulan B, 2010–2019) | Kunci K2 (kumpulan B, 2020–2024) | Kunci K3 (kumpulan B, 2025 – Ogo 2026) |
|---|---|---|---|
| Median, peraturan teratas (prasyarat sebenar) | +18.93 (200 / 200 positif) | +15.86 (200 / 200 positif) | +15.42 (117 / 124 positif) |
| Median, peraturan teratas PLASEBO | +7.94 (200 / 200 positif) | +13.02 (200 / 200 positif) | +2.07 (120 / 182 positif) |
| Median, peraturan rawak | -0.56 (72 / 200 positif) | -0.60 (76 / 200 positif) | -0.06 (85 / 177 positif) |
| Spearman skor lawan kelebihan (teratas) | +0.34 | +0.27 | +0.18 |

## 5. Setup lengkap bagi SETIAP kaedah: pegang dan keluar ikut kadar tangkap (kumpulan B)

Bagi setiap kaedah, peraturan masuk terbaik (syarat sahaja **S**, dan dengan prasyarat **P**) dipasangkan dengan henti × keluar yang paling kerap menghasilkan **tangkap penuh**, dipilih pada kumpulan A (pindaan (k)). Angka = median merentas kaedah, kumpulan B. Jadual setiap kaedah: `carian_setup/hasil/CS06/SEMUA_PENCETUS_LENGKAP.md`.

**Tangkap penuh** = naik ≥ 5 % minggu pertama DAN dijual dengan untung ≥ 10 % mengikut henti dan keluar setup itu. **Jadi** lebih luas: apa-apa dagangan yang dijual dengan untung ≥ 10 %, termasuk yang naik perlahan.

| Kayu ukur masuk | Kaedah | Tangkap penuh %: S / P | Beza (P − S) · P > S | K3: beza · P > S | Jadi % (rawak): S / P | P > S (jadi) | Rugi ≥ 8 %: S / P | Pegang (sesi): S / P | Keluar terpilih tanpa indikator (X00): S / P | Keluar terpilih mengatasi X00: S / P |
|---|---|---|---|---|---|---|---|---|---|---|
| Pilih | 462 | 9.3 / 10.7 | +2.7 · 342 / 462 | +4.4 · 268 / 341 | 19.1 (16.8) / 15.1 (12.2) | 194 / 462 | 30.4 / 34.0 | 16.9 / 14.5 | 84 / 96 | 192 / 138 |
| Jumlah | 460 | 11.8 / 12.2 | +1.8 · 320 / 460 | +3.0 · 236 / 331 | 23.5 (19.5) / 17.5 (13.0) | 191 / 460 | 32.8 / 32.4 | 16.5 / 14.9 | 57 / 131 | 223 / 112 |

- Henti terpilih (dengan prasyarat): pilih: H1 200, H2 127, H3 86, H4 49; jumlah: H1 188, H2 114, H3 121, H4 37.
- Peraturan keluar terpilih berbentuk "DAN" (dua indikator mesti menyala serentak, jadi jarang menjual): pilih: S 224, P 252 daripada 462; jumlah: S 219, P 223 daripada 460.
- Median tangkap penuh tanpa keluar indikator (X00, henti sama): pilih: S 9.1 %, P 10.9 %; jumlah: S 11.8 %, P 12.3 %. Purata setiap dagangan (maklumat): pilih: S +0.13 %, P -0.06 %; jumlah: S +0.38 %, P +0.39 %.

## 6. Padanan jenis setup × prasyarat (kumpulan B, tanpa penapis)

Kelas dikunci secara mekanikal: **IKUT TREND** (434 pencetus) jika ≥ 50 % isyaratnya mempunyai RSI14 > 50; selainnya **PANTULAN** (31). Setiap sel = median merentas pencetus bagi perubahan bila prasyarat benar berbanding semua isyarat pencetus itu: **Δ tangkap penuh** (kadar tangkap penuh mutlak) / **Δ kelebihan** (lawan rawak hari sama) / **Δ henti** (kadar kena henti), mata peratus. "Plasebo" = Δ kelebihan dengan prasyarat dianjak masa.

| Prasyarat | % masa benar | Semua saham: tangkap penuh % benar / palsu | Semua saham: kena henti % benar / palsu | IKUT TREND: Δ tangkap penuh / Δ kelebihan / Δ henti | (plasebo) | PANTULAN: Δ tangkap penuh / Δ kelebihan / Δ henti | (plasebo) |
|---|---|---|---|---|---|---|---|
| **Pasaran** | | | | | | | |
| QQQ ON | 60 | 4.4 / 6.9 | 30.8 / 33.1 | -0.4 / +0.1 / -0.3 | -0.0 | -1.6 / -0.1 / -1.1 | +0.0 |
| QQQ OFF | 40 | 6.9 / 4.4 | 33.1 / 30.8 | +0.7 / -0.2 / +0.3 | +0.1 | +1.0 / +0.1 / +1.0 | -0.1 |
| SPY atas SMA200 | 84 | 4.5 / 10.1 | 30.4 / 38.8 | -0.3 / +0.1 / -0.5 | -0.0 | -1.3 / -0.0 / -1.4 | -0.0 |
| SPY bawah SMA200 | 16 | 10.1 / 4.5 | 38.8 / 30.4 | +2.4 / -0.5 / +5.7 | +0.1 | +4.1 / +0.2 / +6.3 | +0.0 |
| QQQ dalam 3% dari puncak 52 minggu | 55 | 4.0 / 7.1 | 30.2 / 33.7 | -0.4 / +0.1 / -0.7 | +0.0 | -1.8 / -0.2 / -1.3 | +0.0 |
| QQQ >= 10% di bawah puncak | 15 | 9.8 / 4.6 | 39.4 / 30.4 | +2.0 / -0.5 / +7.6 | +0.1 | +4.5 / +0.1 / +4.0 | -0.3 |
| QQQ >= 20% di bawah puncak | 6 | 10.9 / 5.0 | 39.6 / 31.2 | +1.8 / -0.7 / +8.9 | -0.0 | +7.3 / -0.0 / +9.7 | +0.2 |
| rejim ON baharu (<= 10 sesi) | 20 | 4.4 / 5.6 | 30.3 / 32.1 | -0.4 / +0.1 / -1.9 | -0.0 | -1.7 / -0.0 / -0.6 | +0.1 |
| rejim OFF baharu (<= 10 sesi) | 19 | 5.3 / 5.4 | 33.0 / 31.4 | -0.1 / -0.2 / +0.5 | +0.3 | -0.4 / +0.1 / +2.0 | -0.2 |
| QQQ RSI14 < 35 | 4 | 11.0 / 5.2 | 31.1 / 31.8 | +3.0 / -1.1 / -1.9 | -0.1 | +4.3 / +0.1 / -1.3 | -0.2 |
| QQQ naik >= 3% dalam 5 sesi | 14 | 5.7 / 5.3 | 33.5 / 31.5 | +0.2 / -0.2 / +1.1 | +0.0 | -0.0 / +0.2 / +0.8 | -0.0 |
| turun-naik SPY 21 hari >= 25% setahun | 9 | 10.6 / 4.9 | 38.2 / 31.1 | +1.9 / -0.2 / +8.0 | -0.1 | +4.7 / +0.1 / +7.8 | +0.2 |
| turun-naik SPY 21 hari <= 10% setahun | 30 | 3.3 / 6.3 | 28.9 / 33.0 | -1.3 / +0.1 / -1.5 | +0.0 | -2.5 / -0.1 / -2.8 | +0.1 |
| turun-naik SPY menurun (21 hari < 63 hari) | 54 | 4.8 / 6.0 | 29.8 / 34.0 | -0.2 / +0.0 / -1.1 | +0.1 | -0.6 / -0.1 / -2.0 | -0.0 |
| >= 60% saham di atas MA50 | 51 | 4.1 / 6.7 | 29.9 / 33.7 | -0.5 / +0.0 / -1.1 | -0.1 | -1.6 / -0.2 / -1.5 | +0.0 |
| <= 30% saham di atas MA50 | 11 | 10.6 / 4.7 | 36.7 / 31.1 | +2.2 / -0.8 / +5.8 | -0.2 | +3.1 / +0.1 / +2.8 | -0.1 |
| keluasan naik >= 10 mata dalam 10 sesi | 25 | 4.9 / 5.5 | 31.1 / 31.9 | -0.1 / +0.1 / -1.3 | -0.0 | -0.7 / -0.2 / +1.1 | -0.1 |
| >= 60% saham di atas MA200 | 65 | 4.1 / 7.8 | 29.6 / 35.9 | -0.5 / +0.1 / -1.2 | -0.0 | -1.4 / -0.1 / -3.3 | +0.0 |
| >= 15% saham dalam 5% dari puncak 52 minggu | 74 | 4.1 / 9.0 | 29.9 / 36.8 | -0.5 / +0.1 / -0.9 | -0.0 | -1.7 / -0.1 / -1.7 | +0.0 |
| Nov-Apr | 49 | 5.6 / 5.2 | 32.4 / 31.1 | +0.3 / -0.0 / +0.1 | -0.1 | +0.4 / -0.0 / +1.8 | +0.1 |
| Mei-Okt | 51 | 5.2 / 5.6 | 31.1 / 32.4 | -0.2 / +0.0 / -0.2 | +0.1 | -0.2 / +0.0 / -1.5 | -0.1 |
| 7 hari pertama bulan | 23 | 5.8 / 5.3 | 31.7 / 31.8 | +0.6 / -0.0 / -0.7 | -0.1 | +0.8 / +0.0 / +0.8 | -0.0 |
| Januari | 8 | 6.1 / 5.3 | 33.0 / 31.6 | +1.2 / -0.1 / +0.2 | -0.2 | +0.5 / +0.3 / +2.2 | +0.1 |
| follow-through day aktif (QQQ, 20 sesi) | 17 | 6.1 / 5.2 | 34.8 / 31.1 | +0.5 / -0.0 / +1.8 | +0.0 | +0.3 / -0.0 / +3.0 | -0.1 |
| distribution day QQQ <= 2 dalam 25 sesi | 6 | 3.6 / 5.5 | 23.8 / 32.3 | -1.1 / +0.1 / -7.4 | +0.0 | -2.6 / -0.2 / -5.9 | -0.3 |
| distribution day QQQ >= 5 dalam 25 sesi | 69 | 6.0 / 3.9 | 33.7 / 27.4 | +0.4 / -0.1 / +1.6 | +0.0 | +0.6 / +0.0 / +1.1 | -0.0 |
| breadth thrust Zweig aktif (20 sesi) | 11 | 5.9 / 5.3 | 27.2 / 32.3 | +0.1 / -0.1 / -5.6 | +0.0 | +2.0 / -0.3 / -4.6 | +0.2 |
| nisbah 4% (10 hari) > 2 | 16 | 4.7 / 5.5 | 28.8 / 32.3 | -0.1 / +0.0 / -1.3 | +0.0 | -1.3 / -0.4 / -3.9 | +0.0 |
| nisbah 4% (10 hari) < 0.5 | 9 | 8.0 / 5.1 | 32.5 / 31.7 | +0.3 / -0.6 / -3.5 | +0.3 | +1.8 / +0.1 / +0.0 | -0.0 |
| regangan turun-naik SPY (proksi VIX) + SPY > SMA200 | 25 | 4.8 / 5.6 | 29.1 / 32.6 | +0.1 / +0.1 / -1.6 | +0.0 | -0.8 / +0.0 / -2.9 | -0.0 |
| QQQ SMA10 > SMA20 | 67 | 4.6 / 7.0 | 31.3 / 32.7 | -0.3 / +0.1 / -0.2 | -0.0 | -1.3 / -0.1 / +0.1 | +0.0 |
| SPY Peringkat 2 Weinstein (atas SMA150 yang naik) | 79 | 4.5 / 8.7 | 30.1 / 37.9 | -0.2 / +0.1 / -0.8 | +0.0 | -1.3 / -0.0 / -1.9 | +0.0 |
| hari 90% turun kemudian naik (20 sesi) | 28 | 6.9 / 4.8 | 31.8 / 31.7 | +0.4 / -0.3 / -1.2 | +0.0 | +1.5 / +0.1 / +0.6 | +0.0 |
| **Kumpulan / syarikat** | | | | | | | |
| sektor 3 teratas (pulangan 63 sesi) | 26 | 5.2 / 5.5 | 31.9 / 31.7 | +0.1 / +0.0 / +0.8 | +0.3 | -0.1 / +0.0 / -0.1 | +0.3 |
| sektor 3 terbawah (pulangan 63 sesi) | 22 | 6.0 / 5.2 | 33.6 / 31.2 | +0.2 / +0.2 / +0.7 | -0.1 | +0.3 / +0.1 / +2.4 | -0.3 |
| >= 60% saham sektor di atas MA50 | 48 | 4.2 / 6.4 | 30.1 / 33.3 | -0.3 / +0.1 / -0.7 | +0.1 | -1.5 / -0.1 / -1.7 | +0.2 |
| industri 20% teratas (pulangan 63 sesi) | 18 | 5.5 / 5.4 | 33.5 / 31.4 | +0.5 / +0.2 / +2.4 | +0.3 | +0.6 / +0.3 / +1.0 | +0.3 |
| industri 20% teratas (pulangan 21 sesi) | 18 | 5.3 / 5.4 | 33.2 / 31.4 | +0.4 / +0.0 / +1.8 | +0.1 | +0.7 / +0.1 / +0.9 | +0.4 |
| industri 20% terbawah (pulangan 63 sesi) | 17 | 6.3 / 5.2 | 34.7 / 31.1 | +0.1 / -0.0 / +1.8 | +0.0 | +0.6 / +0.1 / +2.2 | -0.2 |
| >= 60% saham industri di atas MA50 | 49 | 4.2 / 6.5 | 29.7 / 33.7 | -0.3 / +0.0 / -0.8 | +0.0 | -1.5 / +0.0 / -1.9 | +0.1 |
| saham lain dalam industri sama naik >= 20% dalam 20 sesi | 34 | 6.2 / 5.0 | 36.4 / 29.4 | +1.1 / +0.2 / +4.4 | +0.2 | +0.7 / +0.2 / +4.5 | +0.2 |
| earnings dalam 1-5 sesi akan datang | 7 | 11.8 / 4.9 | 36.4 / 31.4 | +5.8 / +5.2 / +5.0 | +0.7 | +6.9 / +5.7 / +4.3 | +1.0 |
| 0-4 sesi selepas earnings | 7 | 5.2 / 5.4 | 30.2 / 31.9 | +0.0 / -1.2 / -1.4 | +0.2 | -0.4 / -1.5 / -1.8 | +0.4 |
| 5-19 sesi selepas earnings | 21 | 4.6 / 5.6 | 29.6 / 32.3 | -0.6 / -0.6 / -2.2 | -0.2 | -0.9 / -0.7 / -1.4 | -0.4 |
| tiada earnings dalam 20 sesi akan datang | 60 | 4.6 / 6.5 | 29.3 / 35.4 | -0.6 / -0.6 / -2.5 | -0.1 | -0.7 / -0.6 / -1.8 | -0.1 |
| kejutan untung terkini positif (SUE > 0) | 46 | 5.0 / 5.7 | 30.2 / 33.1 | -0.2 / -0.1 / -1.5 | -0.1 | -0.3 / -0.1 / -1.5 | -0.1 |
| hasil suku terkini tumbuh >= 20% | 16 | 7.6 / 5.0 | 39.8 / 30.2 | +2.0 / +0.7 / +8.0 | +0.4 | +2.1 / +0.5 / +7.4 | +0.4 |
| harga melompat >= 5% pada hari earnings (20 sesi lalu) | 5 | 5.8 / 5.4 | 34.7 / 31.6 | +1.1 / -0.9 / +3.0 | +0.6 | +1.1 / -0.8 / +7.8 | +0.4 |

## 7. Kaveat

- Backtest sahaja; papan ialah pangkat, BUKAN bukti. Kohort jejak hadapan (`jejak_f/`) TIDAK berubah; menukar kohort ialah keputusan pengguna yang berasingan. Kad skor kekal satu-satunya keputusan wang sebenar.
- Lebih 100 juta peraturan dicuba: yang teratas pada kumpulan A sebahagiannya nasib. Sebab itu setiap angka di atas daripada kumpulan B, bersebelahan peraturan rawak dan plasebo.
- Prasyarat pasaran berubah ikut HARI: belian banyak tetapi hari isyarat berbeza sedikit (lajur "hari isyarat"); satu episod pasaran boleh menentukan hasil. K3 hanya 20 bulan.
- "Earnings akan datang" memakai tarikh sebenar (pandang ke hadapan ringan; papertrade memerlukan kalendar earnings). Peta sektor/industri ialah peta semasa. `QH07` ialah proksi (tiada VIX dalam repo).
- Tiada saham delist (condong ke atas); set 2000 bukan tapisan Shariah; data bermula 2010.
- Prasyarat yang menaikkan kadar tangkap penuh selalunya turut menaikkan kadar kena henti: baca kedua-dua lajur.
