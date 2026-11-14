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

Cara pegang dan keluar terbaik bagi setiap setup (dipilih pada kumpulan A; angka kumpulan B, kos 0.5 % ditolak, jurang melepasi henti dijual pada harga buka):

| ID | Henti | Keluar | K1: purata % / menang % / pegang | K2: purata % / menang % / pegang | K3: purata % / menang % / pegang | Dagangan ≥ +10 % / rugi ≤ −8 % (kumpulan B) |
|---|---|---|---|---|---|---|
| `F39` | H2 -10% | X09 MACD < isyarat DAN X15 tutup < rendah 3 hari | +0.97 / 46.2 / 11.7 | +0.70 / 38.6 / 10.4 | +1.28 / 37.7 / 9.5 | 20.3 / 26.5 |
| `F40` | H4 4xATR14 | X08 MA10 < MA20 | +1.77 / 46.8 / 13.6 | +3.04 / 51.3 / 13.5 | +2.47 / 45.4 / 12.2 | 25.4 / 20.8 |
| `F41` | H2 -10% | X12 RSI14 silang turun bawah 70 | +0.17 / 41.3 / 12.4 | +1.57 / 45.3 / 11.9 | -3.47 / 31.5 / 9.9 | 24.6 / 53.0 |
| `F42` | H4 4xATR14 | X03 tutup < MA50 DAN X23 tutup < buka dan < rendah semalam | +0.05 / 43.0 / 15.3 | +8.80 / 59.1 / 16.1 | +3.18 / 45.5 / 17.3 | 26.9 / 27.2 |
| `F43` | H4 4xATR14 | X21 Stochastic silang turun di atas 80 DAN X24 +DI < -DI | +6.56 / 71.8 / 15.7 | +7.98 / 75.1 / 18.3 | -3.81 / 31.6 / 16.0 | 32.4 / 13.3 |
| `F44` | H2 -10% | X05 tutup < EMA20 DAN X16 tutup < rendah 5 hari | +0.67 / 38.0 / 12.9 | +0.80 / 33.3 / 11.6 | -0.72 / 32.4 / 11.1 | 18.8 / 38.6 |
| `F45` | H3 3xATR14 | X08 MA10 < MA20 DAN X20 tutup < 92% tutup tertinggi sejak beli | -0.18 / 40.6 / 15.0 | +3.58 / 50.6 / 15.6 | +3.39 / 44.0 / 14.9 | 26.7 / 30.1 |
| `F46` | H3 3xATR14 | X01 tutup < MA10 DAN X09 MACD < isyarat | +0.09 / 49.5 / 12.8 | +1.40 / 51.6 / 13.5 | +0.43 / 44.1 / 13.8 | 18.7 / 21.6 |
| `F47` | H4 4xATR14 | X04 tutup < EMA10 DAN X21 Stochastic silang turun di atas 80 | +0.72 / 50.3 / 17.6 | +0.86 / 54.4 / 16.9 | +0.85 / 51.9 / 17.8 | 19.8 / 20.4 |
| `F48` | H4 4xATR14 | X21 Stochastic silang turun di atas 80 ATAU X24 +DI < -DI | -0.03 / 43.2 / 5.4 | -0.63 / 40.2 / 5.3 | +2.84 / 50.7 / 5.6 | 12.0 / 16.2 |

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

Cara pegang dan keluar terbaik bagi setiap setup (dipilih pada kumpulan A; angka kumpulan B, kos 0.5 % ditolak, jurang melepasi henti dijual pada harga buka):

| ID | Henti | Keluar | K1: purata % / menang % / pegang | K2: purata % / menang % / pegang | K3: purata % / menang % / pegang | Dagangan ≥ +10 % / rugi ≤ −8 % (kumpulan B) |
|---|---|---|---|---|---|---|
| `F49` | H4 4xATR14 | X10 histogram MACD turun 3 hari DAN X12 RSI14 silang turun bawah 70 | +7.96 / 68.8 / 18.5 | +4.39 / 62.1 / 18.4 | +6.81 / 70.1 / 18.1 | 38.4 / 21.8 |
| `F43` | H4 4xATR14 | X21 Stochastic silang turun di atas 80 DAN X24 +DI < -DI | +6.56 / 71.8 / 15.7 | +7.98 / 75.1 / 18.3 | -3.81 / 31.6 / 16.0 | 32.4 / 13.3 |
| `F50` | H4 4xATR14 | X07 dua tutup berturut < MA20 DAN X21 Stochastic silang turun di atas 80 | +5.01 / 64.7 / 18.3 | +3.66 / 55.4 / 17.8 | +2.36 / 53.3 / 17.9 | 34.9 / 26.0 |
| `F51` | H4 4xATR14 | X10 histogram MACD turun 3 hari DAN X21 Stochastic silang turun di atas 80 | +3.05 / 63.2 / 17.1 | +5.89 / 65.4 / 17.8 | +4.16 / 62.9 / 16.7 | 29.7 / 18.6 |
| `F52` | H4 4xATR14 | X12 RSI14 silang turun bawah 70 DAN X23 tutup < buka dan < rendah semalam | +6.73 / 72.9 / 18.9 | +7.30 / 65.9 / 18.2 | -3.84 / 41.7 / 18.5 | 37.7 / 19.7 |
| `F53` | H3 3xATR14 | X20 tutup < 92% tutup tertinggi sejak beli DAN X22 hari turun dengan volum >= 1.5x | +5.45 / 70.3 / 18.3 | +6.91 / 70.2 / 17.9 | -3.30 / 38.3 / 16.8 | 34.5 / 20.8 |
| `F54` | H4 4xATR14 | X06 dua tutup berturut < MA10 DAN X18 Chandelier 3xATR14 (dari tutup tertinggi sejak beli) | +5.12 / 61.8 / 18.1 | +5.91 / 58.2 / 18.8 | +2.98 / 65.4 / 19.6 | 35.2 / 21.9 |
| `F55` | H4 4xATR14 | X12 RSI14 silang turun bawah 70 ATAU X13 RSI14 > 80 | +8.46 / 75.9 / 19.6 | +6.80 / 68.9 / 19.0 | +12.59 / 87.2 / 19.7 | 42.8 / 12.0 |
| `F56` | H4 4xATR14 | X08 MA10 < MA20 DAN X21 Stochastic silang turun di atas 80 | +3.39 / 59.5 / 18.3 | +6.71 / 63.2 / 18.8 | -0.36 / 52.4 / 16.9 | 35.2 / 22.4 |
| `F57` | H2 -10% | X12 RSI14 silang turun bawah 70 ATAU X18 Chandelier 3xATR14 (dari tutup tertinggi sejak beli) | +2.50 / 48.5 / 16.6 | +5.04 / 60.5 / 13.7 | +7.27 / 72.5 / 13.6 | 35.8 / 32.8 |

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

## 5. Padanan jenis setup × prasyarat (kumpulan B, tanpa penapis)

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

## 6. Kaveat

- Backtest sahaja; papan ialah pangkat, BUKAN bukti. Kohort jejak hadapan (`jejak_f/`) TIDAK berubah; menukar kohort ialah keputusan pengguna yang berasingan. Kad skor kekal satu-satunya keputusan wang sebenar.
- Lebih 100 juta peraturan dicuba: yang teratas pada kumpulan A sebahagiannya nasib. Sebab itu setiap angka di atas daripada kumpulan B, bersebelahan peraturan rawak dan plasebo.
- Prasyarat pasaran berubah ikut HARI: belian banyak tetapi hari isyarat berbeza sedikit (lajur "hari isyarat"); satu episod pasaran boleh menentukan hasil. K3 hanya 20 bulan.
- "Earnings akan datang" memakai tarikh sebenar (pandang ke hadapan ringan; papertrade memerlukan kalendar earnings). Peta sektor/industri ialah peta semasa. `QH07` ialah proksi (tiada VIX dalam repo).
- Tiada saham delist (condong ke atas); set 2000 bukan tapisan Shariah; data bermula 2010.
- Prasyarat yang menaikkan kadar lari selalunya turut menaikkan kadar kena henti: baca kedua-dua lajur.
