# Carian Setup CS02 — papan 10 teratas (backtest, BUKAN bukti)

> **Status keputusan (kad skor, harga 2026-11-11):** TERBUKTI 0 · CALON 0 · BELUM CUKUP 223 · GAGAL 0 · NEGATIF 0. Rejim QQQ OFF sejak 2026-10-16. Hanya **TERBUKTI** layak untuk wang sebenar (`laporan/KAD_SKOR.md`); nombor dalam laporan ini BUKAN keputusan dan tidak boleh dibaca sebagai pangkat untuk wang sebenar.

Dijana `kajian/carian_setup/cs_lapor.py`. Pradaftar: `kajian/SPEC_CARIAN_SETUP.md` (13 Nov 2026, dikomit sebelum keputusan pusingan ini dilihat). **Jangan sunting secara manual.** Arkib setiap pusingan: `kajian/carian_setup/hasil/<pusingan>/LAPORAN.md`.

## 1. Apa yang dicari

Setup lengkap (masuk, pegang, keluar) yang menangkap saham ketika ia mula naik kuat dan memegangnya selagi naik. Syarat wajib: swing paling lama 20 sesi, tiada jual pada hari beli, henti rugi longgar, tiada sasaran untung tetap, keluar ikut indikator. Kos 0.5 % pusingan sudah ditolak.

Carian: kumpulan A set 2000 (dua era: 2010–2019 dan 2020–2024). Kunci: kumpulan B set 2000: saham yang carian tidak pernah lihat.

## 2. Saiz carian

- Pencetus masuk: 500 (49 indikator + benih M asal dan dua varian parameter + benih N); 465 cukup isyarat.
- Peraturan masuk (pencetus × 0–2 penapis): 233,000 dicuba, 182,903 cukup dagangan (≥ 100 dalam kedua-dua tempoh carian).
- Setiap satu × 2,308 gabungan henti × keluar: **422,140,124 kombinasi diskor** (daripada 537,764,000 dicuba) dalam 59 minit.
- 2.4 % kombinasi diskor mempunyai had bawah positif dalam kedua-dua tempoh carian.

## 3. Papan 10 teratas

Pangkat ikut `skor tepat` (had bawah purata untung, yang lebih rendah antara E1 dan E2). **Kunci** dilaporkan sahaja dan tidak mengubah pangkat.

Setiap setup papan didaftarkan dalam keluarga **F** (`data/registry_F.csv`, ID kekal; status BACKTEST = belum papertrade).

| # | ID | Masuk | Penapis | Henti | Keluar | Skor | K1: purata % | K2: purata % | K3: purata % | Lawan rawak | T1 | T2 | T3 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `F11` | M01 Bollinger Band + RSI (benih M, varian 2: r13_ambang_25=38, rolling_30=58, rsi_13=10, sd_kali_2=1.436) | F20 >= 30% di bawah puncak 52 minggu DAN F27 rejim QQQ OFF | H4 4xATR14 | X04 tutup < EMA10 DAN X12 RSI14 silang turun bawah 70 | +2.09 | +2.02 | +2.92 | +2.51 | persentil 100 | ✓ | ✓ | ✓ |
| 2 | `F12` | M88 O'Neil Shakeout +3 (benih M, varian 1: bm_kali_0_92=0.613, d2_tolak_40=65, d2_tolak_5=3, l1_kali_0_9=0.512, l1_kali_1_1=0.952, rolling_20=14) | F20 >= 30% di bawah puncak 52 minggu DAN F27 rejim QQQ OFF | H4 4xATR14 | X12 RSI14 silang turun bawah 70 ATAU X13 RSI14 > 80 | +2.09 | +3.10 | +3.74 | +2.53 | persentil 100 | ✗ | ✓ | ✓ |
| 3 | `F13` | M02 MACD + SMA200 (benih M, parameter asal) | F09 RSI14 > 60 DAN F27 rejim QQQ OFF | H4 4xATR14 | X08 MA10 < MA20 DAN X20 tutup < 92% tutup tertinggi sejak beli | +1.76 | +1.88 | +0.49 | +2.23 | persentil 100 | ✓ | ✓ | ✓ |
| 4 | `F14` | N28 ADX>25 + DI+ > DI- (benih N) | F20 >= 30% di bawah puncak 52 minggu DAN F27 rejim QQQ OFF | H4 4xATR14 | X09 MACD < isyarat DAN X21 Stochastic silang turun di atas 80 | +1.68 | +2.41 | +2.71 | +1.75 | persentil 100 | ✗ | ✓ | ✓ |
| 5 | `F15` | M73 ADX(5) > 40 + Julat Terkecil 6 Hari (benih M, varian 1: adx_5=6, adx_ambang_40=55, rolling_5=3) | F20 >= 30% di bawah puncak 52 minggu DAN F27 rejim QQQ OFF | H4 4xATR14 | X04 tutup < EMA10 DAN X12 RSI14 silang turun bawah 70 | +1.59 | +2.31 | +3.95 | +1.06 | persentil 100 | ✓ | ✓ | ✓ |
| 6 | `F16` | N38 VCP pecah (benih N) | F23 ATR% >= 4 DAN F29 tutup dalam 25% teratas julat hari | H4 4xATR14 | X21 Stochastic silang turun di atas 80 DAN X22 hari turun dengan volum >= 1.5x | +1.54 | +1.96 | +2.32 | +1.16 | persentil 100 | ✓ | ✓ | ✓ |
| 7 | `F17` | P14 RSI14 silang atas 30 | F20 >= 30% di bawah puncak 52 minggu DAN F27 rejim QQQ OFF | H4 4xATR14 | X13 RSI14 > 80 | +1.50 | +2.50 | +2.74 | +0.86 | persentil 100 | ✗ | ✓ | ✓ |
| 8 | `F18` | N75 RSI14 < 40 tanpa penapis (benih N) | F20 >= 30% di bawah puncak 52 minggu DAN F27 rejim QQQ OFF | H4 4xATR14 | X13 RSI14 > 80 DAN X21 Stochastic silang turun di atas 80 | +1.49 | +1.72 | +2.08 | +1.32 | persentil 100 | ✓ | ✓ | ✓ |
| 9 | `F19` | P02 MACD silang naik bawah sifar | F09 RSI14 > 60 DAN F27 rejim QQQ OFF | H4 4xATR14 | X14 Supertrend turun DAN X23 tutup < buka dan < rendah semalam | +1.48 | +1.64 | +0.94 | +0.74 | persentil 100 | ✓ | ✓ | ✓ |
| 10 | `F20` | M141 First Thrust (Landry) (benih M, varian 1: a_kali_3=2.907, atr_14=23, had_henti=0.907, henti_atr=2.626, rolling_60=69) | F11 MACD > isyarat DAN F27 rejim QQQ OFF | H4 4xATR14 | X18 Chandelier 3xATR14 (dari tutup tertinggi sejak beli) DAN X22 hari turun dengan volum >= 1.5x | +1.41 | +2.26 | +1.03 | +0.77 | persentil 100 | ✓ | ✓ | ✓ |

- **T1 tahan:** skor positif pada keempat-empat pilihan henti. **T2 tidak dilihat:** purata positif dalam setiap tempoh Kunci. **T3 kalahkan rawak:** purata Kunci (semua tempoh) melebihi persentil ke-95 setup rawak (+0.30 %).
- "Lawan rawak" = peratus daripada 200 setup yang dipilih rawak daripada ruang yang sama yang puratanya pada Kunci lebih rendah.

### Butiran setiap setup

**#1. `F11` — M01 Bollinger Band + RSI (benih M, varian 2: r13_ambang_25=38, rolling_30=58, rsi_13=10, sd_kali_2=1.436)**

Penapis: F20 >= 30% di bawah puncak 52 minggu DAN F27 rejim QQQ OFF · Henti: H4 4xATR14 · Keluar: X04 tutup < EMA10 DAN X12 RSI14 silang turun bawah 70

| Tempoh | Dagangan | Purata % | Menang % | ≥ +10 % | ≥ +20 % | Rugi ≤ −8 % | Naik 5 % minggu 1 | Pegang (sesi) | Purata seminggu % | Lebihan atas rawak hari sama | MDD buku % |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Cari E1 (kumpulan A, 2010–2019) | 3,799 | +2.55 | 57.7 | 28.0 | 9.3 | 22.7 | 24.7 | 18.8 | +0.68 | +0.82 | -42.2 |
| Cari E2 (kumpulan A, 2020–2024) | 5,141 | +2.66 | 56.0 | 30.8 | 13.5 | 26.5 | 26.7 | 18.8 | +0.71 | +0.38 | -44.8 |
| Kunci K1 (kumpulan B, 2010–2019) | 3,762 | +2.02 | 56.2 | 26.1 | 8.6 | 24.7 | 23.8 | 18.7 | +0.54 | +0.35 | -43.6 |
| Kunci K2 (kumpulan B, 2020–2024) | 4,914 | +2.92 | 56.0 | 30.0 | 13.5 | 25.5 | 27.7 | 18.8 | +0.78 | +0.80 | -40.8 |
| Kunci K3 (kumpulan B, 2025 – Ogo 2026) | 1,585 | +2.51 | 56.6 | 29.1 | 11.9 | 25.3 | 28.6 | 19.0 | +0.66 | +0.76 | -31.0 |

Skor pada empat pilihan henti (H1–H4): +0.79 · +0.94 · +1.79 · +2.09

**#2. `F12` — M88 O'Neil Shakeout +3 (benih M, varian 1: bm_kali_0_92=0.613, d2_tolak_40=65, d2_tolak_5=3, l1_kali_0_9=0.512, l1_kali_1_1=0.952, rolling_20=14)**

Penapis: F20 >= 30% di bawah puncak 52 minggu DAN F27 rejim QQQ OFF · Henti: H4 4xATR14 · Keluar: X12 RSI14 silang turun bawah 70 ATAU X13 RSI14 > 80

| Tempoh | Dagangan | Purata % | Menang % | ≥ +10 % | ≥ +20 % | Rugi ≤ −8 % | Naik 5 % minggu 1 | Pegang (sesi) | Purata seminggu % | Lebihan atas rawak hari sama | MDD buku % |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Cari E1 (kumpulan A, 2010–2019) | 980 | +2.98 | 57.2 | 29.7 | 10.0 | 22.4 | 27.3 | 19.3 | +0.77 | +0.92 | -55.2 |
| Cari E2 (kumpulan A, 2020–2024) | 1,751 | +3.18 | 58.4 | 33.3 | 14.6 | 24.2 | 32.3 | 18.7 | +0.85 | -0.26 | -61.1 |
| Kunci K1 (kumpulan B, 2010–2019) | 1,037 | +3.10 | 58.2 | 30.3 | 9.9 | 21.2 | 28.8 | 19.2 | +0.81 | +1.07 | -44.0 |
| Kunci K2 (kumpulan B, 2020–2024) | 1,577 | +3.74 | 58.0 | 34.8 | 16.4 | 24.4 | 31.6 | 18.8 | +1.00 | +0.03 | -41.7 |
| Kunci K3 (kumpulan B, 2025 – Ogo 2026) | 568 | +2.53 | 57.2 | 29.2 | 10.6 | 22.2 | 18.8 | 19.5 | +0.65 | +0.02 | -32.7 |

Skor pada empat pilihan henti (H1–H4): -0.49 · -0.26 · +1.91 · +2.09

**#3. `F13` — M02 MACD + SMA200 (benih M, parameter asal)**

Penapis: F09 RSI14 > 60 DAN F27 rejim QQQ OFF · Henti: H4 4xATR14 · Keluar: X08 MA10 < MA20 DAN X20 tutup < 92% tutup tertinggi sejak beli

| Tempoh | Dagangan | Purata % | Menang % | ≥ +10 % | ≥ +20 % | Rugi ≤ −8 % | Naik 5 % minggu 1 | Pegang (sesi) | Purata seminggu % | Lebihan atas rawak hari sama | MDD buku % |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Cari E1 (kumpulan A, 2010–2019) | 299 | +2.91 | 62.5 | 18.4 | 5.4 | 10.4 | 15.4 | 18.6 | +0.78 | +1.33 | -41.8 |
| Cari E2 (kumpulan A, 2020–2024) | 171 | +3.53 | 62.6 | 25.1 | 8.2 | 15.2 | 19.9 | 17.8 | +0.99 | +0.92 | -40.8 |
| Kunci K1 (kumpulan B, 2010–2019) | 314 | +1.88 | 59.9 | 14.6 | 2.2 | 11.8 | 12.4 | 18.8 | +0.50 | +0.69 | -26.1 |
| Kunci K2 (kumpulan B, 2020–2024) | 189 | +0.49 | 58.7 | 15.3 | 4.2 | 22.2 | 10.6 | 17.5 | +0.14 | -1.23 | -61.3 |
| Kunci K3 (kumpulan B, 2025 – Ogo 2026) | 48 | +2.23 | 62.5 | 20.8 | 6.2 | 22.9 | 20.8 | 17.8 | +0.63 | +2.40 | -30.5 |

Skor pada empat pilihan henti (H1–H4): +0.74 · +1.24 · +1.58 · +1.76

**#4. `F14` — N28 ADX>25 + DI+ > DI- (benih N)**

Penapis: F20 >= 30% di bawah puncak 52 minggu DAN F27 rejim QQQ OFF · Henti: H4 4xATR14 · Keluar: X09 MACD < isyarat DAN X21 Stochastic silang turun di atas 80

| Tempoh | Dagangan | Purata % | Menang % | ≥ +10 % | ≥ +20 % | Rugi ≤ −8 % | Naik 5 % minggu 1 | Pegang (sesi) | Purata seminggu % | Lebihan atas rawak hari sama | MDD buku % |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Cari E1 (kumpulan A, 2010–2019) | 2,534 | +2.23 | 56.8 | 27.1 | 9.2 | 23.2 | 25.3 | 19.0 | +0.59 | +0.65 | -33.9 |
| Cari E2 (kumpulan A, 2020–2024) | 3,099 | +2.79 | 56.6 | 31.0 | 15.2 | 26.2 | 29.7 | 18.6 | +0.75 | +0.07 | -46.6 |
| Kunci K1 (kumpulan B, 2010–2019) | 2,635 | +2.41 | 57.8 | 27.4 | 8.6 | 22.9 | 25.1 | 19.0 | +0.63 | +0.74 | -58.5 |
| Kunci K2 (kumpulan B, 2020–2024) | 2,919 | +2.71 | 55.6 | 30.0 | 14.3 | 25.9 | 28.2 | 18.7 | +0.73 | +0.01 | -36.7 |
| Kunci K3 (kumpulan B, 2025 – Ogo 2026) | 996 | +1.75 | 54.0 | 27.1 | 11.6 | 24.2 | 24.9 | 19.2 | +0.45 | +0.19 | -28.0 |

Skor pada empat pilihan henti (H1–H4): -0.05 · +0.17 · +1.50 · +1.68

**#5. `F15` — M73 ADX(5) > 40 + Julat Terkecil 6 Hari (benih M, varian 1: adx_5=6, adx_ambang_40=55, rolling_5=3)**

Penapis: F20 >= 30% di bawah puncak 52 minggu DAN F27 rejim QQQ OFF · Henti: H4 4xATR14 · Keluar: X04 tutup < EMA10 DAN X12 RSI14 silang turun bawah 70

| Tempoh | Dagangan | Purata % | Menang % | ≥ +10 % | ≥ +20 % | Rugi ≤ −8 % | Naik 5 % minggu 1 | Pegang (sesi) | Purata seminggu % | Lebihan atas rawak hari sama | MDD buku % |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Cari E1 (kumpulan A, 2010–2019) | 2,400 | +2.13 | 57.0 | 25.9 | 7.8 | 21.8 | 25.3 | 19.0 | +0.56 | +0.33 | -46.0 |
| Cari E2 (kumpulan A, 2020–2024) | 2,761 | +3.73 | 56.7 | 32.6 | 16.0 | 25.3 | 31.5 | 18.6 | +1.00 | +0.48 | -58.8 |
| Kunci K1 (kumpulan B, 2010–2019) | 2,392 | +2.31 | 58.3 | 26.1 | 8.4 | 21.7 | 25.0 | 18.9 | +0.61 | +0.42 | -40.8 |
| Kunci K2 (kumpulan B, 2020–2024) | 2,638 | +3.95 | 57.0 | 33.5 | 16.9 | 24.5 | 31.7 | 18.7 | +1.06 | +0.65 | -40.3 |
| Kunci K3 (kumpulan B, 2025 – Ogo 2026) | 770 | +1.06 | 50.8 | 25.8 | 10.0 | 29.1 | 23.0 | 19.1 | +0.28 | +0.58 | -28.8 |

Skor pada empat pilihan henti (H1–H4): +0.54 · +0.70 · +1.40 · +1.59

**#6. `F16` — N38 VCP pecah (benih N)**

Penapis: F23 ATR% >= 4 DAN F29 tutup dalam 25% teratas julat hari · Henti: H4 4xATR14 · Keluar: X21 Stochastic silang turun di atas 80 DAN X22 hari turun dengan volum >= 1.5x

| Tempoh | Dagangan | Purata % | Menang % | ≥ +10 % | ≥ +20 % | Rugi ≤ −8 % | Naik 5 % minggu 1 | Pegang (sesi) | Purata seminggu % | Lebihan atas rawak hari sama | MDD buku % |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Cari E1 (kumpulan A, 2010–2019) | 1,177 | +2.43 | 57.5 | 27.7 | 9.9 | 23.5 | 27.4 | 17.8 | +0.68 | +0.97 | -70.0 |
| Cari E2 (kumpulan A, 2020–2024) | 2,675 | +3.06 | 55.5 | 31.0 | 13.8 | 26.2 | 25.2 | 18.1 | +0.85 | +0.49 | -64.8 |
| Kunci K1 (kumpulan B, 2010–2019) | 1,209 | +1.96 | 54.7 | 27.0 | 9.3 | 24.0 | 23.2 | 17.9 | +0.55 | +0.67 | -69.9 |
| Kunci K2 (kumpulan B, 2020–2024) | 2,544 | +2.32 | 52.9 | 29.7 | 13.8 | 28.6 | 24.3 | 17.9 | +0.65 | +0.17 | -77.9 |
| Kunci K3 (kumpulan B, 2025 – Ogo 2026) | 730 | +1.16 | 49.2 | 27.7 | 12.9 | 30.3 | 31.1 | 17.7 | +0.33 | +0.49 | -34.2 |

Skor pada empat pilihan henti (H1–H4): +0.62 · +0.72 · +1.51 · +1.54

**#7. `F17` — P14 RSI14 silang atas 30**

Penapis: F20 >= 30% di bawah puncak 52 minggu DAN F27 rejim QQQ OFF · Henti: H4 4xATR14 · Keluar: X13 RSI14 > 80

| Tempoh | Dagangan | Purata % | Menang % | ≥ +10 % | ≥ +20 % | Rugi ≤ −8 % | Naik 5 % minggu 1 | Pegang (sesi) | Purata seminggu % | Lebihan atas rawak hari sama | MDD buku % |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Cari E1 (kumpulan A, 2010–2019) | 2,912 | +2.24 | 56.7 | 27.7 | 8.3 | 23.3 | 22.7 | 19.1 | +0.59 | +0.31 | -43.3 |
| Cari E2 (kumpulan A, 2020–2024) | 3,610 | +2.06 | 55.9 | 29.4 | 12.5 | 26.1 | 27.7 | 18.7 | +0.55 | -0.55 | -39.6 |
| Kunci K1 (kumpulan B, 2010–2019) | 3,001 | +2.50 | 58.0 | 27.2 | 8.3 | 21.5 | 23.0 | 19.0 | +0.66 | +0.67 | -46.7 |
| Kunci K2 (kumpulan B, 2020–2024) | 3,386 | +2.74 | 56.5 | 30.4 | 13.2 | 25.3 | 28.2 | 18.8 | +0.73 | +0.04 | -37.8 |
| Kunci K3 (kumpulan B, 2025 – Ogo 2026) | 1,086 | +0.86 | 54.1 | 24.4 | 8.7 | 25.3 | 18.0 | 19.2 | +0.22 | -0.23 | -30.6 |

Skor pada empat pilihan henti (H1–H4): -0.11 · +0.01 · +1.16 · +1.50

**#8. `F18` — N75 RSI14 < 40 tanpa penapis (benih N)**

Penapis: F20 >= 30% di bawah puncak 52 minggu DAN F27 rejim QQQ OFF · Henti: H4 4xATR14 · Keluar: X13 RSI14 > 80 DAN X21 Stochastic silang turun di atas 80

| Tempoh | Dagangan | Purata % | Menang % | ≥ +10 % | ≥ +20 % | Rugi ≤ −8 % | Naik 5 % minggu 1 | Pegang (sesi) | Purata seminggu % | Lebihan atas rawak hari sama | MDD buku % |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Cari E1 (kumpulan A, 2010–2019) | 4,002 | +1.93 | 56.2 | 27.5 | 8.3 | 24.2 | 24.5 | 18.7 | +0.51 | +0.37 | -55.3 |
| Cari E2 (kumpulan A, 2020–2024) | 5,676 | +2.12 | 54.5 | 29.8 | 13.1 | 27.8 | 25.7 | 18.8 | +0.56 | +0.10 | -46.3 |
| Kunci K1 (kumpulan B, 2010–2019) | 3,973 | +1.72 | 55.0 | 25.5 | 8.3 | 24.9 | 23.1 | 18.7 | +0.46 | +0.16 | -39.4 |
| Kunci K2 (kumpulan B, 2020–2024) | 5,589 | +2.08 | 53.5 | 28.2 | 12.6 | 26.6 | 24.5 | 18.9 | +0.55 | +0.19 | -44.3 |
| Kunci K3 (kumpulan B, 2025 – Ogo 2026) | 1,784 | +1.32 | 52.8 | 25.3 | 11.3 | 29.9 | 26.1 | 18.8 | +0.35 | +0.03 | -32.9 |

Skor pada empat pilihan henti (H1–H4): +0.47 · +0.68 · +1.21 · +1.49

**#9. `F19` — P02 MACD silang naik bawah sifar**

Penapis: F09 RSI14 > 60 DAN F27 rejim QQQ OFF · Henti: H4 4xATR14 · Keluar: X14 Supertrend turun DAN X23 tutup < buka dan < rendah semalam

| Tempoh | Dagangan | Purata % | Menang % | ≥ +10 % | ≥ +20 % | Rugi ≤ −8 % | Naik 5 % minggu 1 | Pegang (sesi) | Purata seminggu % | Lebihan atas rawak hari sama | MDD buku % |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Cari E1 (kumpulan A, 2010–2019) | 372 | +2.55 | 57.5 | 16.9 | 5.1 | 11.3 | 14.5 | 17.3 | +0.74 | +1.70 | -36.7 |
| Cari E2 (kumpulan A, 2020–2024) | 236 | +3.05 | 60.2 | 25.0 | 7.6 | 17.4 | 21.2 | 17.4 | +0.88 | +1.52 | -51.7 |
| Kunci K1 (kumpulan B, 2010–2019) | 377 | +1.64 | 58.4 | 13.8 | 1.9 | 11.7 | 11.9 | 17.9 | +0.46 | +0.94 | -26.2 |
| Kunci K2 (kumpulan B, 2020–2024) | 244 | +0.94 | 55.7 | 15.6 | 5.3 | 17.6 | 12.3 | 17.5 | +0.27 | +0.20 | -47.3 |
| Kunci K3 (kumpulan B, 2025 – Ogo 2026) | 63 | +0.74 | 54.0 | 17.5 | 3.2 | 20.6 | 20.6 | 16.4 | +0.23 | +1.30 | -18.9 |

Skor pada empat pilihan henti (H1–H4): +0.37 · +1.20 · +1.23 · +1.48

**#10. `F20` — M141 First Thrust (Landry) (benih M, varian 1: a_kali_3=2.907, atr_14=23, had_henti=0.907, henti_atr=2.626, rolling_60=69)**

Penapis: F11 MACD > isyarat DAN F27 rejim QQQ OFF · Henti: H4 4xATR14 · Keluar: X18 Chandelier 3xATR14 (dari tutup tertinggi sejak beli) DAN X22 hari turun dengan volum >= 1.5x

| Tempoh | Dagangan | Purata % | Menang % | ≥ +10 % | ≥ +20 % | Rugi ≤ −8 % | Naik 5 % minggu 1 | Pegang (sesi) | Purata seminggu % | Lebihan atas rawak hari sama | MDD buku % |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Cari E1 (kumpulan A, 2010–2019) | 683 | +2.11 | 63.1 | 15.8 | 3.4 | 13.3 | 12.2 | 18.7 | +0.57 | -0.04 | -46.4 |
| Cari E2 (kumpulan A, 2020–2024) | 351 | +3.02 | 62.1 | 23.1 | 6.8 | 17.4 | 16.2 | 18.8 | +0.80 | -0.49 | -44.8 |
| Kunci K1 (kumpulan B, 2010–2019) | 632 | +2.26 | 62.8 | 16.1 | 3.0 | 14.1 | 10.8 | 18.6 | +0.61 | +0.19 | -39.6 |
| Kunci K2 (kumpulan B, 2020–2024) | 370 | +1.03 | 53.2 | 20.8 | 4.9 | 22.2 | 15.7 | 18.6 | +0.28 | -1.55 | -39.8 |
| Kunci K3 (kumpulan B, 2025 – Ogo 2026) | 142 | +0.77 | 52.1 | 19.0 | 7.0 | 23.9 | 14.1 | 18.8 | +0.20 | +0.27 | -20.4 |

Skor pada empat pilihan henti (H1–H4): +0.21 · +0.22 · +1.31 · +1.41

## 4. Semakan kejujuran

**K3 ialah ujian sebenar** (saham lain DAN tahun yang tidak dipakai carian: 2025 – Ogo 2026). K1 dan K2 berkongsi tahun dengan carian, jadi ia hanya menunjukkan setup itu berfungsi pada saham lain dalam pasaran yang sama.

| Ukuran | Kunci K1 (kumpulan B, 2010–2019) | Kunci K2 (kumpulan B, 2020–2024) | Kunci K3 (kumpulan B, 2025 – Ogo 2026) |
|---|---|---|---|
| Median purata setiap dagangan, 200 setup teratas | +1.68 % | +2.16 % | +0.95 % |
| Median purata setiap dagangan, 200 setup rawak | -0.23 % | -0.33 % | -0.27 % |
| Setup teratas dengan purata positif | 200 daripada 200 | 200 daripada 200 | 136 daripada 200 |
| Setup rawak dengan purata positif | 50 daripada 200 | 43 daripada 200 | 68 daripada 200 |
| Setup teratas melebihi persentil ke-95 rawak | 199 daripada 200 | 190 daripada 200 | 92 daripada 200 |
| Spearman `skor tepat` lawan purata | +0.49 | +0.25 | +0.44 |

Bacaan: pada tempoh yang tahunnya tidak dipakai carian (K3), setup teratas **masih mengatasi setup rawak, tetapi lebih lemah** daripada pada tahun carian: K3 median +0.95 % lawan -0.27 %, dan 92 daripada 200 melebihi persentil ke-95 rawak (kira-kira 10 dijangka jika tiada kelebihan). Ini masih backtest tanpa saham delist; hakim sebenar ialah papertrade.

Gabungan semua tempoh Kunci (ukuran pradaftar T3): Spearman +0.46; median teratas +1.75 % lawan rawak -0.24 %; 199 daripada 200 melebihi persentil ke-95 rawak (+0.30 %).

### Apa yang carian pilih

- 175 daripada 200 setup teratas memakai henti paling longgar (`H4`), dan 31 memakai penapis saham meruap (`F23` ATR % ≥ 4).
- 149 daripada 200 memakai penapis `F27` (rejim QQQ OFF) dan 74 memakai `F20` (saham ≥ 30 % di bawah puncak 52 minggu).
- Purata pegang 10 teratas pada Kunci ialah 18.5 sesi daripada had 20.
- Lebihan 10 teratas atas "beli mana-mana saham layak pada hari yang sama" (henti dan keluar sama): K1 +0.49 % · K2 +0.27 % · K3 +0.29 %. Jika lebihan ini kecil berbanding purata dagangan, sebahagian besar untung datang daripada BILA membeli (keadaan pasaran pada hari itu), bukan saham MANA yang dipilih.
- MDD buku = semua posisi sama berat dan sentiasa melabur penuh, bukan portfolio berslot; bandingkan dengan toleransi MDD akaun −10 %.

## 5. Kaveat

- Backtest sahaja. Tiada setup di sini masuk papertrade tanpa keputusan pengguna yang berasingan; kad skor kekal satu-satunya keputusan wang sebenar.
- Tiada saham delist dalam set 2000: semua angka condong ke atas. Set ini bukan tapisan Shariah.
- Setup yang membeli saham yang sudah jatuh jauh (`F20`) paling terdedah kepada ketiadaan saham delist: saham yang jatuh lalu dinyahsenarai tiada dalam data, jadi setiap saham jatuh dalam data ini "terselamat".
- Data bermula 2010: tiada pasaran menurun panjang seperti 2000–2002 atau 2008. Membeli semasa rejim QQQ OFF untung dalam tempoh ini kerana setiap kejatuhan pulih; itu belum diuji dalam pasaran menurun yang berpanjangan.
- Reka bentuk dua era dipilih selepas melihat CS01. Kumpulan A dan B merangkumi saham set 431 dan saham Kunci CS01, dan K3 bertindih dengan tempoh Sah CS01; K3 bersih bagi pemilihan CS02 sahaja.
- Peringkat besar membenarkan isyarat bertindih; angka papan dikira semula dengan satu posisi setiap saham.
- Benih M yang bergantung pada saham lain (persentil RS) dikira dalam alam masing-masing.
- Benih gagal dijalankan: set carian 0, Kunci 0 (senarai dalam `carian_setup/hasil/CS02/meta.json`).

## 6. Jana semula

```
W=<folder kerja di luar repo, satu setiap pusingan>
cd BacktestShariah2/kajian/carian_setup
C=A; K=B; P=CS02
python3 cs_cari.py panel $W $C && python3 cs_cari.py benih $W $C && python3 cs_cari.py besar $W $P
python3 cs_cari.py tepat $W $P && python3 cs_cari.py panel $W $K && python3 cs_cari.py kunci $W $P
python3 cs_lapor.py $W $P
```
