# Carian Setup CS01 — papan 10 teratas (backtest, BUKAN bukti)

> **Status keputusan (kad skor, harga 2026-11-11):** TERBUKTI 0 · CALON 0 · BELUM CUKUP 223 · GAGAL 0 · NEGATIF 0. Rejim QQQ OFF sejak 2026-10-16. Hanya **TERBUKTI** layak untuk wang sebenar (`laporan/KAD_SKOR.md`); nombor dalam laporan ini BUKAN keputusan dan tidak boleh dibaca sebagai pangkat untuk wang sebenar.

Dijana `kajian/carian_setup/cs_lapor.py`. Pradaftar: `kajian/SPEC_CARIAN_SETUP.md` (13 Nov 2026, dikomit sebelum keputusan pusingan ini dilihat). **Jangan sunting secara manual.** Arkib setiap pusingan: `kajian/carian_setup/hasil/<pusingan>/LAPORAN.md`.

## 1. Apa yang dicari

Setup lengkap (masuk, pegang, keluar) yang menangkap saham ketika ia mula naik kuat dan memegangnya selagi naik. Syarat wajib: swing paling lama 20 sesi, tiada jual pada hari beli, henti rugi longgar, tiada sasaran untung tetap, keluar ikut indikator. Kos 0.5 % pusingan sudah ditolak.

Carian: set 431. Kunci: 1,000 saham lain yang carian tidak pernah lihat.

## 2. Saiz carian

- Pencetus masuk: 500 (49 indikator + benih M asal dan dua varian parameter + benih N); 455 cukup isyarat.
- Peraturan masuk (pencetus × 0–2 penapis): 233,000 dicuba, 159,203 cukup dagangan (≥ 100 dalam kedua-dua tempoh carian).
- Setiap satu × 2,308 gabungan henti × keluar: **367,440,524 kombinasi diskor** (daripada 537,764,000 dicuba) dalam 10 minit.
- 4.4 % kombinasi diskor mempunyai had bawah positif dalam kedua-dua tempoh carian.

## 3. Papan 10 teratas

Pangkat ikut `skor tepat` (had bawah purata untung, yang lebih rendah antara Latih dan Sah). **Kunci** dilaporkan sahaja dan tidak mengubah pangkat.

Setiap setup papan didaftarkan dalam keluarga **F** (`data/registry_F.csv`, ID kekal; status BACKTEST = belum papertrade).

| # | ID | Masuk | Penapis | Henti | Keluar | Skor | K1: purata % | K2: purata % | Lawan rawak | T1 | T2 | T3 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `F01` | N203 (benih N) | F15 Supertrend naik DAN F23 ATR% >= 4 | H4 4xATR14 | X03 tutup < MA50 DAN X22 hari turun dengan volum >= 1.5x | +3.09 | -0.29 | +3.23 | persentil 100 | ✗ | ✗ | ✓ |
| 2 | `F02` | M111 Sistem Volatiliti Wilder (benih M, varian 2: close_kali_0_88=0.631, m=3.248, n=9, rolling_50=44, sistem_mula_199=259) | F20 >= 30% di bawah puncak 52 minggu DAN F27 rejim QQQ OFF | H4 4xATR14 | X08 MA10 < MA20 DAN X22 hari turun dengan volum >= 1.5x | +3.09 | +1.51 | +1.86 | persentil 100 | ✓ | ✓ | ✓ |
| 3 | `F03` | M01 Bollinger Band + RSI (benih M, varian 2: r13_ambang_25=38, rolling_30=58, rsi_13=10, sd_kali_2=1.436) | F16 RS >= 70 DAN F20 >= 30% di bawah puncak 52 minggu | H4 4xATR14 | X20 tutup < 92% tutup tertinggi sejak beli DAN X21 Stochastic silang turun di atas 80 | +3.09 | -0.18 | +3.28 | persentil 100 | ✓ | ✗ | ✓ |
| 4 | `F04` | M79 Radge: 20% Flipper (benih M, varian 1: a=0.18) | F21 volum hari isyarat >= 1.5x purata 50 DAN F27 rejim QQQ OFF | H4 4xATR14 | X12 RSI14 silang turun bawah 70 DAN X20 tutup < 92% tutup tertinggi sejak beli | +2.72 | +0.76 | +2.73 | persentil 100 | ✗ | ✓ | ✓ |
| 5 | `F05` | P07 MA20 silang atas MA50 | F15 Supertrend naik DAN F23 ATR% >= 4 | H4 4xATR14 | X14 Supertrend turun DAN X22 hari turun dengan volum >= 1.5x | +2.67 | -0.44 | +2.05 | persentil 100 | ✓ | ✗ | ✓ |
| 6 | `F06` | N07 Tiga MA tersusun (benih N) | F14 ADX < 20 DAN F23 ATR% >= 4 | H4 4xATR14 | X18 Chandelier 3xATR14 (dari tutup tertinggi sejak beli) DAN X22 hari turun dengan volum >= 1.5x | +2.40 | +0.04 | +2.11 | persentil 100 | ✓ | ✓ | ✓ |
| 7 | `F07` | M30 BB Free Bar + Himpitan 50/2.5 (benih M, parameter asal) | F23 ATR% >= 4 DAN F27 rejim QQQ OFF | H4 4xATR14 | X13 RSI14 > 80 | +2.34 | -1.87 | +1.99 | persentil 100 | ✗ | ✗ | ✓ |
| 8 | `F08` | N201 (benih N) | F15 Supertrend naik DAN F23 ATR% >= 4 | H4 4xATR14 | X18 Chandelier 3xATR14 (dari tutup tertinggi sejak beli) DAN X22 hari turun dengan volum >= 1.5x | +2.32 | -0.77 | +1.90 | persentil 100 | ✓ | ✗ | ✓ |
| 9 | `F09` | M140 猎豹出击 (Serangan Cheetah) (benih M, varian 1: float_ambang_40=20, had_henti=0.581, henti_atr=3.237, keluar_sma=99, rolling_60=61, sma_60=71) | F23 ATR% >= 4 DAN F30 hari naik (tutup > buka) | H4 4xATR14 | X14 Supertrend turun DAN X22 hari turun dengan volum >= 1.5x | +2.32 | -0.19 | +2.07 | persentil 100 | ✗ | ✗ | ✓ |
| 10 | `F10` | P16 RSI2<5 atas MA200 | F21 volum hari isyarat >= 1.5x purata 50 DAN F23 ATR% >= 4 | H3 3xATR14 | X12 RSI14 silang turun bawah 70 ATAU X19 Chandelier 2xATR14 | +2.32 | -0.47 | +0.89 | persentil 98 | ✓ | ✗ | ✓ |

- **T1 tahan:** skor positif pada keempat-empat pilihan henti. **T2 tidak dilihat:** purata positif dalam setiap tempoh Kunci. **T3 kalahkan rawak:** purata Kunci (semua tempoh) melebihi persentil ke-95 setup rawak (+0.24 %).
- "Lawan rawak" = peratus daripada 200 setup yang dipilih rawak daripada ruang yang sama yang puratanya pada Kunci lebih rendah.

### Butiran setiap setup

**#1. `F01` — N203 (benih N)**

Penapis: F15 Supertrend naik DAN F23 ATR% >= 4 · Henti: H4 4xATR14 · Keluar: X03 tutup < MA50 DAN X22 hari turun dengan volum >= 1.5x

| Tempoh | Dagangan | Purata % | Menang % | ≥ +10 % | ≥ +20 % | Rugi ≤ −8 % | Naik 5 % minggu 1 | Pegang (sesi) | Purata seminggu % | Lebihan atas rawak hari sama | MDD buku % |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Latih (set 431, 2020 – Jun 2023) | 361 | +4.92 | 60.7 | 31.9 | 16.9 | 19.9 | 27.7 | 18.4 | +1.34 | +2.57 | -53.9 |
| Sah (set 431, Jul 2023 – Ogo 2026) | 303 | +6.50 | 60.7 | 30.7 | 16.8 | 24.4 | 28.1 | 18.3 | +1.78 | +5.07 | -48.6 |
| Kunci K1 (saham lain, 2010–2019) | 220 | -0.29 | 45.9 | 20.5 | 6.4 | 29.5 | 17.7 | 18.2 | -0.08 | +0.18 | -68.5 |
| Kunci K2 (saham lain, 2020 – Ogo 2026) | 907 | +3.23 | 53.0 | 30.8 | 15.7 | 25.8 | 26.1 | 18.4 | +0.88 | +1.42 | -79.4 |

Skor pada empat pilihan henti (H1–H4): -0.02 · +0.25 · +2.50 · +3.09

**#2. `F02` — M111 Sistem Volatiliti Wilder (benih M, varian 2: close_kali_0_88=0.631, m=3.248, n=9, rolling_50=44, sistem_mula_199=259)**

Penapis: F20 >= 30% di bawah puncak 52 minggu DAN F27 rejim QQQ OFF · Henti: H4 4xATR14 · Keluar: X08 MA10 < MA20 DAN X22 hari turun dengan volum >= 1.5x

| Tempoh | Dagangan | Purata % | Menang % | ≥ +10 % | ≥ +20 % | Rugi ≤ −8 % | Naik 5 % minggu 1 | Pegang (sesi) | Purata seminggu % | Lebihan atas rawak hari sama | MDD buku % |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Latih (set 431, 2020 – Jun 2023) | 323 | +4.83 | 57.9 | 36.2 | 16.1 | 19.2 | 24.5 | 17.9 | +1.34 | +2.25 | -40.9 |
| Sah (set 431, Jul 2023 – Ogo 2026) | 159 | +6.93 | 61.6 | 35.2 | 20.8 | 15.1 | 35.2 | 18.4 | +1.88 | +5.79 | -43.9 |
| Kunci K1 (saham lain, 2010–2019) | 403 | +1.51 | 57.6 | 24.3 | 5.7 | 21.8 | 15.1 | 17.7 | +0.43 | +0.42 | -80.1 |
| Kunci K2 (saham lain, 2020 – Ogo 2026) | 781 | +1.86 | 52.4 | 28.6 | 9.7 | 25.6 | 22.3 | 17.6 | +0.53 | +0.77 | -75.3 |

Skor pada empat pilihan henti (H1–H4): +1.44 · +1.58 · +2.08 · +3.09

**#3. `F03` — M01 Bollinger Band + RSI (benih M, varian 2: r13_ambang_25=38, rolling_30=58, rsi_13=10, sd_kali_2=1.436)**

Penapis: F16 RS >= 70 DAN F20 >= 30% di bawah puncak 52 minggu · Henti: H4 4xATR14 · Keluar: X20 tutup < 92% tutup tertinggi sejak beli DAN X21 Stochastic silang turun di atas 80

| Tempoh | Dagangan | Purata % | Menang % | ≥ +10 % | ≥ +20 % | Rugi ≤ −8 % | Naik 5 % minggu 1 | Pegang (sesi) | Purata seminggu % | Lebihan atas rawak hari sama | MDD buku % |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Latih (set 431, 2020 – Jun 2023) | 140 | +8.18 | 69.3 | 50.0 | 27.9 | 22.9 | 34.3 | 18.4 | +2.22 | +2.20 | -68.3 |
| Sah (set 431, Jul 2023 – Ogo 2026) | 128 | +7.23 | 60.2 | 38.3 | 25.8 | 27.3 | 43.8 | 19.1 | +1.89 | +4.13 | -82.6 |
| Kunci K1 (saham lain, 2010–2019) | 173 | -0.18 | 48.0 | 24.3 | 10.4 | 31.2 | 31.8 | 18.2 | -0.05 | -0.79 | -79.3 |
| Kunci K2 (saham lain, 2020 – Ogo 2026) | 586 | +3.28 | 53.4 | 35.0 | 18.8 | 30.2 | 32.3 | 18.9 | +0.87 | +0.73 | -89.2 |

Skor pada empat pilihan henti (H1–H4): +0.40 · +1.08 · +2.45 · +3.09

**#4. `F04` — M79 Radge: 20% Flipper (benih M, varian 1: a=0.18)**

Penapis: F21 volum hari isyarat >= 1.5x purata 50 DAN F27 rejim QQQ OFF · Henti: H4 4xATR14 · Keluar: X12 RSI14 silang turun bawah 70 DAN X20 tutup < 92% tutup tertinggi sejak beli

| Tempoh | Dagangan | Purata % | Menang % | ≥ +10 % | ≥ +20 % | Rugi ≤ −8 % | Naik 5 % minggu 1 | Pegang (sesi) | Purata seminggu % | Lebihan atas rawak hari sama | MDD buku % |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Latih (set 431, 2020 – Jun 2023) | 365 | +4.96 | 60.5 | 34.5 | 13.7 | 20.5 | 28.5 | 19.3 | +1.29 | -0.36 | -40.0 |
| Sah (set 431, Jul 2023 – Ogo 2026) | 263 | +5.19 | 60.5 | 29.7 | 14.8 | 22.1 | 24.0 | 19.0 | +1.36 | +2.75 | -30.0 |
| Kunci K1 (saham lain, 2010–2019) | 470 | +0.76 | 54.3 | 19.1 | 4.7 | 22.1 | 16.0 | 18.8 | +0.20 | -0.29 | -57.3 |
| Kunci K2 (saham lain, 2020 – Ogo 2026) | 1,070 | +2.73 | 55.3 | 29.7 | 13.7 | 27.5 | 27.2 | 18.9 | +0.72 | -0.33 | -75.9 |

Skor pada empat pilihan henti (H1–H4): -0.03 · +0.52 · +2.55 · +2.72

**#5. `F05` — P07 MA20 silang atas MA50**

Penapis: F15 Supertrend naik DAN F23 ATR% >= 4 · Henti: H4 4xATR14 · Keluar: X14 Supertrend turun DAN X22 hari turun dengan volum >= 1.5x

| Tempoh | Dagangan | Purata % | Menang % | ≥ +10 % | ≥ +20 % | Rugi ≤ −8 % | Naik 5 % minggu 1 | Pegang (sesi) | Purata seminggu % | Lebihan atas rawak hari sama | MDD buku % |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Latih (set 431, 2020 – Jun 2023) | 913 | +3.74 | 56.4 | 30.9 | 15.9 | 24.9 | 27.8 | 18.1 | +1.03 | +1.48 | -64.0 |
| Sah (set 431, Jul 2023 – Ogo 2026) | 599 | +5.34 | 56.3 | 29.7 | 16.2 | 26.0 | 25.5 | 18.0 | +1.49 | +3.90 | -63.0 |
| Kunci K1 (saham lain, 2010–2019) | 808 | -0.44 | 47.0 | 19.8 | 6.2 | 30.7 | 20.0 | 17.8 | -0.12 | -0.55 | -67.5 |
| Kunci K2 (saham lain, 2020 – Ogo 2026) | 2,290 | +2.05 | 50.5 | 28.1 | 13.4 | 29.7 | 25.4 | 18.0 | +0.57 | +0.58 | -80.9 |

Skor pada empat pilihan henti (H1–H4): +0.61 · +0.93 · +2.40 · +2.67

**#6. `F06` — N07 Tiga MA tersusun (benih N)**

Penapis: F14 ADX < 20 DAN F23 ATR% >= 4 · Henti: H4 4xATR14 · Keluar: X18 Chandelier 3xATR14 (dari tutup tertinggi sejak beli) DAN X22 hari turun dengan volum >= 1.5x

| Tempoh | Dagangan | Purata % | Menang % | ≥ +10 % | ≥ +20 % | Rugi ≤ −8 % | Naik 5 % minggu 1 | Pegang (sesi) | Purata seminggu % | Lebihan atas rawak hari sama | MDD buku % |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Latih (set 431, 2020 – Jun 2023) | 923 | +3.43 | 59.0 | 30.8 | 14.1 | 23.6 | 26.3 | 18.5 | +0.93 | +1.28 | -39.5 |
| Sah (set 431, Jul 2023 – Ogo 2026) | 584 | +4.49 | 55.1 | 30.8 | 15.9 | 27.4 | 28.6 | 18.6 | +1.21 | +3.07 | -42.4 |
| Kunci K1 (saham lain, 2010–2019) | 752 | +0.04 | 50.0 | 20.3 | 6.0 | 29.5 | 21.4 | 18.5 | +0.01 | -0.37 | -82.1 |
| Kunci K2 (saham lain, 2020 – Ogo 2026) | 2,189 | +2.11 | 51.6 | 29.1 | 13.1 | 30.3 | 25.4 | 18.5 | +0.57 | +0.44 | -75.6 |

Skor pada empat pilihan henti (H1–H4): +0.75 · +1.13 · +2.16 · +2.40

**#7. `F07` — M30 BB Free Bar + Himpitan 50/2.5 (benih M, parameter asal)**

Penapis: F23 ATR% >= 4 DAN F27 rejim QQQ OFF · Henti: H4 4xATR14 · Keluar: X13 RSI14 > 80

| Tempoh | Dagangan | Purata % | Menang % | ≥ +10 % | ≥ +20 % | Rugi ≤ −8 % | Naik 5 % minggu 1 | Pegang (sesi) | Purata seminggu % | Lebihan atas rawak hari sama | MDD buku % |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Latih (set 431, 2020 – Jun 2023) | 183 | +4.67 | 60.1 | 35.0 | 15.3 | 20.2 | 27.9 | 17.5 | +1.33 | +2.99 | -19.4 |
| Sah (set 431, Jul 2023 – Ogo 2026) | 127 | +6.13 | 59.8 | 37.8 | 24.4 | 22.8 | 37.0 | 16.0 | +1.91 | +4.28 | -53.0 |
| Kunci K1 (saham lain, 2010–2019) | 143 | -1.87 | 47.6 | 21.7 | 7.0 | 36.4 | 20.3 | 16.6 | -0.56 | -2.58 | -91.6 |
| Kunci K2 (saham lain, 2020 – Ogo 2026) | 435 | +1.99 | 53.6 | 30.1 | 12.0 | 27.4 | 25.1 | 17.0 | +0.58 | +0.33 | -82.2 |

Skor pada empat pilihan henti (H1–H4): -0.25 · +0.43 · +1.30 · +2.34

**#8. `F08` — N201 (benih N)**

Penapis: F15 Supertrend naik DAN F23 ATR% >= 4 · Henti: H4 4xATR14 · Keluar: X18 Chandelier 3xATR14 (dari tutup tertinggi sejak beli) DAN X22 hari turun dengan volum >= 1.5x

| Tempoh | Dagangan | Purata % | Menang % | ≥ +10 % | ≥ +20 % | Rugi ≤ −8 % | Naik 5 % minggu 1 | Pegang (sesi) | Purata seminggu % | Lebihan atas rawak hari sama | MDD buku % |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Latih (set 431, 2020 – Jun 2023) | 825 | +3.45 | 56.8 | 30.3 | 15.4 | 24.5 | 26.9 | 18.6 | +0.93 | +1.16 | -64.4 |
| Sah (set 431, Jul 2023 – Ogo 2026) | 544 | +5.59 | 57.7 | 30.5 | 16.7 | 25.2 | 25.6 | 18.6 | +1.50 | +4.00 | -62.9 |
| Kunci K1 (saham lain, 2010–2019) | 713 | -0.77 | 47.0 | 19.6 | 5.9 | 31.4 | 19.6 | 18.5 | -0.21 | -0.92 | -70.0 |
| Kunci K2 (saham lain, 2020 – Ogo 2026) | 2,052 | +1.90 | 50.6 | 28.1 | 13.5 | 30.2 | 25.0 | 18.5 | +0.51 | +0.26 | -83.6 |

Skor pada empat pilihan henti (H1–H4): +0.39 · +0.60 · +2.11 · +2.32

**#9. `F09` — M140 猎豹出击 (Serangan Cheetah) (benih M, varian 1: float_ambang_40=20, had_henti=0.581, henti_atr=3.237, keluar_sma=99, rolling_60=61, sma_60=71)**

Penapis: F23 ATR% >= 4 DAN F30 hari naik (tutup > buka) · Henti: H4 4xATR14 · Keluar: X14 Supertrend turun DAN X22 hari turun dengan volum >= 1.5x

| Tempoh | Dagangan | Purata % | Menang % | ≥ +10 % | ≥ +20 % | Rugi ≤ −8 % | Naik 5 % minggu 1 | Pegang (sesi) | Purata seminggu % | Lebihan atas rawak hari sama | MDD buku % |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Latih (set 431, 2020 – Jun 2023) | 470 | +4.02 | 57.9 | 28.9 | 14.3 | 22.3 | 23.8 | 17.7 | +1.13 | +1.96 | -38.7 |
| Sah (set 431, Jul 2023 – Ogo 2026) | 291 | +5.15 | 56.4 | 36.4 | 17.5 | 25.8 | 33.3 | 18.4 | +1.40 | +3.76 | -41.8 |
| Kunci K1 (saham lain, 2010–2019) | 477 | -0.19 | 49.9 | 21.8 | 6.9 | 28.9 | 24.1 | 17.8 | -0.05 | -0.86 | -96.1 |
| Kunci K2 (saham lain, 2020 – Ogo 2026) | 1,287 | +2.07 | 50.2 | 26.5 | 12.9 | 29.1 | 25.0 | 17.6 | +0.59 | +0.77 | -80.5 |

Skor pada empat pilihan henti (H1–H4): -0.01 · +0.52 · +1.90 · +2.32

**#10. `F10` — P16 RSI2<5 atas MA200**

Penapis: F21 volum hari isyarat >= 1.5x purata 50 DAN F23 ATR% >= 4 · Henti: H3 3xATR14 · Keluar: X12 RSI14 silang turun bawah 70 ATAU X19 Chandelier 2xATR14

| Tempoh | Dagangan | Purata % | Menang % | ≥ +10 % | ≥ +20 % | Rugi ≤ −8 % | Naik 5 % minggu 1 | Pegang (sesi) | Purata seminggu % | Lebihan atas rawak hari sama | MDD buku % |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Latih (set 431, 2020 – Jun 2023) | 277 | +4.23 | 54.5 | 33.2 | 16.6 | 22.7 | 33.9 | 15.3 | +1.38 | +3.35 | -44.6 |
| Sah (set 431, Jul 2023 – Ogo 2026) | 303 | +4.70 | 54.5 | 28.4 | 14.5 | 22.4 | 31.0 | 14.7 | +1.59 | +4.03 | -36.8 |
| Kunci K1 (saham lain, 2010–2019) | 484 | -0.47 | 41.9 | 19.2 | 6.8 | 32.2 | 25.0 | 14.3 | -0.17 | +0.05 | -72.4 |
| Kunci K2 (saham lain, 2020 – Ogo 2026) | 819 | +0.89 | 44.9 | 22.8 | 10.1 | 27.6 | 27.2 | 14.8 | +0.30 | +0.82 | -61.3 |

Skor pada empat pilihan henti (H1–H4): +1.68 · +2.34 · +2.32 · +2.24

## 4. Semakan kejujuran

**K1 ialah ujian sebenar** (saham lain DAN tahun lain). K2 berkongsi tahun 2020–2026 dengan carian, jadi ia hanya menunjukkan setup itu berfungsi pada saham lain dalam pasaran yang sama.

| Ukuran | Kunci K1 (saham lain, 2010–2019) | Kunci K2 (saham lain, 2020 – Ogo 2026) |
|---|---|---|
| Median purata setiap dagangan, 200 setup teratas | -0.26 % | +2.05 % |
| Median purata setiap dagangan, 200 setup rawak | -0.23 % | -0.30 % |
| Setup teratas dengan purata positif | 79 daripada 200 | 199 daripada 200 |
| Setup rawak dengan purata positif | 40 daripada 200 | 35 daripada 200 |
| Setup teratas melebihi persentil ke-95 rawak | 63 daripada 200 | 195 daripada 200 |
| Spearman `skor tepat` lawan purata | -0.25 | +0.43 |

Bacaan: **kelebihan hanya muncul pada tahun yang sama dengan carian.** Pada tempoh yang tahunnya tidak dipakai carian (K1) setup teratas tidak mengatasi setup rawak. Papan ini menggambarkan pasaran tempoh carian, bukan kaedah yang terbukti tahan merentas era.

Gabungan semua tempoh Kunci (ukuran pradaftar T3): Spearman +0.41; median teratas +1.41 % lawan rawak -0.25 %; 195 daripada 200 melebihi persentil ke-95 rawak (+0.24 %).

### Apa yang carian pilih

- 186 daripada 200 setup teratas memakai henti paling longgar (`H4`), dan 155 memakai penapis saham meruap (`F23` ATR % ≥ 4).
- 62 daripada 200 memakai penapis `F27` (rejim QQQ OFF) dan 25 memakai `F20` (saham ≥ 30 % di bawah puncak 52 minggu).
- Purata pegang 10 teratas pada Kunci ialah 17.7 sesi daripada had 20.
- Lebihan 10 teratas atas "beli mana-mana saham layak pada hari yang sama" (henti dan keluar sama): K1 -0.47 % · K2 +0.53 %. Jika lebihan ini kecil berbanding purata dagangan, sebahagian besar untung datang daripada BILA membeli (keadaan pasaran pada hari itu), bukan saham MANA yang dipilih.
- MDD buku = semua posisi sama berat dan sentiasa melabur penuh, bukan portfolio berslot; bandingkan dengan toleransi MDD akaun −10 %.

## 5. Kaveat

- Backtest sahaja. Tiada setup di sini masuk papertrade tanpa keputusan pengguna yang berasingan; kad skor kekal satu-satunya keputusan wang sebenar.
- Tiada saham delist dalam kedua-dua set: semua angka condong ke atas. K2 berkongsi tahun dengan Latih/Sah (saham berbeza, pasaran sama); K1 berbeza saham dan tahun.
- Peringkat besar membenarkan isyarat bertindih; angka papan dikira semula dengan satu posisi setiap saham.
- Benih M yang bergantung pada saham lain (persentil RS) dikira dalam alam masing-masing.
- `N201` (MA20 silang atas MA50 DAN tutup > MA50) dan `P07` (MA20 silang atas MA50) hampir sama; pradaftar mengira keluarga ikut ID, jadi kedua-duanya boleh muncul dalam papan.
- Benih gagal dijalankan: set carian 0, Kunci 0 (senarai dalam `carian_setup/hasil/CS01/meta.json`).

## 6. Jana semula

```
W=<folder kerja di luar repo, satu setiap pusingan>
cd BacktestShariah2/kajian/carian_setup
C=431; K=kunci; P=CS01
python3 cs_cari.py panel $W $C && python3 cs_cari.py benih $W $C && python3 cs_cari.py besar $W $P
python3 cs_cari.py tepat $W $P && python3 cs_cari.py panel $W $K && python3 cs_cari.py kunci $W $P
python3 cs_lapor.py $W $P
```
