# FASA 2 — pulangan boleh didagangkan, penilaian bergabung, ablasi 2×2

Dijana `REVERSE/fasa2_laporan.py` (2026-10-27 14:32 UTC). Reka bentuk dikunci dalam `SPEC.md` §13.12 B **sebelum** sebarang angka FASA 2 dilihat. FASA 1 (`LAPORAN_<TAHUN>.md`, `BANDING_TAHUN.md`) kekal sebagai rekod.

## 0. Apa yang berubah berbanding FASA 1

| Perkara | FASA 1 | FASA 2 |
|---|---|---|
| Sasaran | `tarikh_puncak` dalam tetingkap 63 hari; `mfe63 ≥ 30%` | pulangan dagangan penuh: masuk buka d+1, keluar ikut polisi tetap, kos dua sisi |
| Unit penilaian | satu tahun, satu silo | 2020-01-01 – 2026-10-16 bergabung |
| Set yang diuji | semua kemunculan signal (sehingga 148,303 setahun) | 8 calon teratas setiap hari = yang portfolio boleh ambil |
| Kawalan | entri rawak | ablasi 2×2: signal lwn universe × susunan RS lwn rawak |

**Kaveat kekal:** tiada saham delist (survivorship) — semua angka ialah had atas; peta sektor bukan titik masa; universe 2020 lebih kecil (1638/1832/1940) daripada 2021–2025.

## 1. Ablasi 2×2 — pulangan setiap dagangan

Empat arm, polisi exit dan kos yang sama. `S+R` = signal × susunan RS 6 bulan; `S+X` = signal × susunan rawak; `X+R` = universe penuh × susunan RS; `X+X` = universe × rawak. Nilai dalam % setiap dagangan; `dipangkas5` = purata selepas 5% pulangan tertinggi dibuang; `bawah95` = had bawah 95% bootstrap blok (ticker atau minggu, yang lebih rendah).

### Polisi `chandelier_4atr` — median merentas signal (arm S) dan nilai sebenar (arm X)

| arm | n | median | purata | purata_dipangkas5 | kadar_menang | lebihan_spy_purata | purata_bawah95_ticker | lebihan_bawah95_ticker | median_hari |
|---|---|---|---|---|---|---|---|---|---|
| S+R | 9758.5 | -7.08 | 2.62 | -4.5 | 36.63 | -0.84 | 0.93 | -2.07 | 44.0 |
| S+X | 9758.5 | -5.56 | 2.51 | -3.84 | 37.55 | -1.06 | 1.49 | -1.95 | 43.0 |
| X+R | 12064.0 | -12.99 | -1.6 | -11.1 | 32.06 | -4.78 | -6.37 | -9.47 | 44.0 |
| X+X | 12064.0 | -3.37 | 2.94 | -1.63 | 40.46 | -0.6 | 2.46 | -1.02 | 44.0 |

### Polisi `jual_hari63` — median merentas signal (arm S) dan nilai sebenar (arm X)

| arm | n | median | purata | purata_dipangkas5 | kadar_menang | lebihan_spy_purata | purata_bawah95_ticker | lebihan_bawah95_ticker | median_hari |
|---|---|---|---|---|---|---|---|---|---|
| S+R | 9758.5 | -1.18 | 2.95 | -2.71 | 48.17 | -1.02 | 1.62 | -2.48 | 63.0 |
| S+X | 9758.5 | 0.01 | 2.56 | -2.34 | 49.99 | -1.6 | 1.72 | -2.25 | 63.0 |
| X+R | 12064.0 | -9.19 | -0.42 | -8.62 | 39.8 | -4.46 | -4.9 | -8.86 | 63.0 |
| X+X | 12064.0 | 1.97 | 3.14 | 0.05 | 54.75 | -0.9 | 2.78 | -1.22 | 63.0 |

### Polisi `pegang_252` — median merentas signal (arm S) dan nilai sebenar (arm X)

| arm | n | median | purata | purata_dipangkas5 | kadar_menang | lebihan_spy_purata | purata_bawah95_ticker | lebihan_bawah95_ticker | median_hari |
|---|---|---|---|---|---|---|---|---|---|
| S+R | 9758.5 | -3.06 | 14.31 | 0.01 | 47.84 | -2.73 | 10.57 | -6.64 | 252.0 |
| S+X | 9758.5 | 2.51 | 14.27 | 2.49 | 52.02 | -3.16 | 11.33 | -5.7 | 252.0 |
| X+R | 12064.0 | -17.57 | 13.74 | -5.83 | 40.19 | -3.77 | 0.78 | -16.08 | 252.0 |
| X+X | 12064.0 | 7.83 | 15.03 | 6.47 | 58.94 | -2.49 | 13.97 | -3.49 | 252.0 |

### Berapa banyak signal mempunyai median dagangan positif?

| polisi | n_signal | median_positif | purata_positif | dipangkas5_positif | lebihan_bawah95_positif |
|---|---|---|---|---|---|
| chandelier_4atr | 46 | 0 | 41 | 0 | 0 |
| jual_hari63 | 46 | 10 | 45 | 2 | 1 |
| pegang_252 | 46 | 17 | 46 | 23 | 0 |

Jurang antara `purata_positif` dan `dipangkas5_positif` ialah ukuran terus berapa banyak jangkaan positif itu datang daripada 5% ekor kanan.

## 2. Keputusan ablasi — adakah signal menyumbang?

Syarat SPEC §13.12 B4: **S+R > X+R DAN S+X > X+X** (lebihan atas SPY), dan had bawah 95% lebihan S+R > 0.

### Polisi `chandelier_4atr`

Asas: X+R lebihan -4.784% (n 12064), X+X lebihan -0.605% (n 12064).

MENYUMBANG: **0 daripada 46** signal.

| signal | n_SR | median_SR | purata_SR | dipangkas5_SR | menang_SR | lebihan_SR | lebihan_SX | bawah95_SR | kalahkan_XR | kalahkan_XX | keputusan |
|---|---|---|---|---|---|---|---|---|---|---|---|
| q5:rs_spy_3b | 6032 | -9.407 | 6.829 | -6.71 | 38.53 | 3.872 | 3.995 | -4.992 | ya | ya | TIDAK |
| q1:cerun_ema21 | 4032 | -7.099 | 5.234 | -4.52 | 38.86 | 2.232 | 3.522 | -1.947 | ya | ya | TIDAK |
| ema_crossback&q5:atr_pct | 8004 | -8.938 | 4.053 | -4.665 | 35.94 | 0.484 | 1.113 | -1.261 | ya | ya | TIDAK |
| ema_crossback&q5:j_ma200 | 9563 | -6.054 | 2.997 | -3.654 | 36.97 | 0.113 | -0.221 | -1.077 | ya | ya | TIDAK |
| pocket_pivot&q5:bb_lebar | 11715 | -7.685 | 3.156 | -4.481 | 36.62 | 0.106 | -1.048 | -1.598 | ya | tidak | TIDAK |
| ema_crossback&q5:cerun_ma50 | 9996 | -6.08 | 2.728 | -3.869 | 36.5 | -0.027 | -0.158 | -1.174 | ya | ya | TIDAK |
| ema_crossback&q5:rs_spy_6b | 9619 | -5.857 | 3.224 | -3.471 | 37.48 | -0.029 | -0.093 | -1.204 | ya | ya | TIDAK |
| ema_crossback&q5:bb_lebar | 7340 | -8.016 | 3.464 | -4.653 | 36.34 | -0.141 | -0.224 | -1.636 | ya | ya | TIDAK |
| ema_crossback&q5:julat20 | 7846 | -8.494 | 3.349 | -4.884 | 35.64 | -0.148 | 0.01 | -1.724 | ya | ya | TIDAK |
| rsi_lintas50&q5:j_ma200 | 9562 | -6.303 | 2.755 | -4.121 | 37.36 | -0.163 | -0.097 | -1.334 | ya | ya | TIDAK |
| rsi_lintas50&q5:cerun_ma50 | 9309 | -6.015 | 2.637 | -3.89 | 36.99 | -0.182 | -0.119 | -1.332 | ya | ya | TIDAK |
| pocket_pivot&q5:rs_spy_6b | 11802 | -7.17 | 2.68 | -4.618 | 36.43 | -0.311 | -0.709 | -2.021 | ya | tidak | TIDAK |

### Polisi `jual_hari63`

Asas: X+R lebihan -4.465% (n 12064), X+X lebihan -0.904% (n 12064).

MENYUMBANG: **1 daripada 46** signal.

| signal | n_SR | median_SR | purata_SR | dipangkas5_SR | menang_SR | lebihan_SR | lebihan_SX | bawah95_SR | kalahkan_XR | kalahkan_XX | keputusan |
|---|---|---|---|---|---|---|---|---|---|---|---|
| q1:cerun_ema21 | 4032 | 0.199 | 8.651 | 0.683 | 50.3 | 5.978 | 2.144 | 2.141 | ya | ya | MENYUMBANG |
| q5:rs_spy_3b | 6032 | -3.197 | 7.316 | -2.843 | 47.03 | 4.113 | 3.834 | -2.787 | ya | ya | TIDAK |
| rsi_lintas50&q5:j_ma200 | 9562 | -0.052 | 4.31 | -1.227 | 49.9 | 0.6 | 0.392 | -0.567 | ya | ya | TIDAK |
| pocket_pivot&q5:rs_spy_6b | 11802 | -0.965 | 4.552 | -2.279 | 48.58 | 0.552 | -0.666 | -1.225 | ya | ya | TIDAK |
| ema_crossback&q5:j_ma200 | 9563 | 0.05 | 4.22 | -1.059 | 50.17 | 0.536 | 0.218 | -0.595 | ya | ya | TIDAK |
| pocket_pivot&q5:bb_lebar | 11715 | -1.397 | 4.491 | -2.416 | 48.01 | 0.504 | -1.447 | -1.246 | ya | tidak | TIDAK |
| rsi_lintas50&q5:rs_spy_6b | 10017 | -0.04 | 4.39 | -1.108 | 49.93 | 0.285 | -0.244 | -0.891 | ya | ya | TIDAK |
| pocket_pivot&q5:julat20 | 11620 | -1.679 | 4.292 | -2.719 | 47.61 | 0.256 | -1.555 | -1.541 | ya | tidak | TIDAK |
| ema_crossback&q5:rs_spy_6b | 9619 | 0.096 | 4.162 | -1.128 | 50.28 | 0.206 | -0.145 | -0.921 | ya | ya | TIDAK |
| ema_crossback&q5:cerun_ma50 | 9996 | -0.313 | 3.297 | -1.805 | 49.4 | -0.187 | -0.428 | -1.361 | ya | ya | TIDAK |
| rsi_lintas50&q5:cerun_ma50 | 9309 | -0.452 | 3.202 | -1.877 | 49.18 | -0.269 | -0.399 | -1.364 | ya | ya | TIDAK |
| q5:j_ema9 | 12021 | -4.404 | 3.582 | -4.656 | 45.09 | -0.432 | -1.461 | -3.321 | ya | tidak | TIDAK |

Signal MENYUMBANG: `q1:cerun_ema21`

### Polisi `pegang_252`

Asas: X+R lebihan -3.772% (n 12064), X+X lebihan -2.489% (n 12064).

MENYUMBANG: **0 daripada 46** signal.

| signal | n_SR | median_SR | purata_SR | dipangkas5_SR | menang_SR | lebihan_SR | lebihan_SX | bawah95_SR | kalahkan_XR | kalahkan_XX | keputusan |
|---|---|---|---|---|---|---|---|---|---|---|---|
| q5:julat10 | 4016 | -6.54 | 39.273 | 16.64 | 47.44 | 17.049 | -7.994 | -6.889 | ya | tidak | TIDAK |
| q1:cerun_ema21 | 4032 | -0.74 | 23.245 | 3.891 | 49.23 | 1.805 | 5.091 | -7.647 | ya | ya | TIDAK |
| pocket_pivot&q5:bb_lebar | 11715 | -4.023 | 19.038 | 2.881 | 47.33 | 1.663 | 0.854 | -2.82 | ya | ya | TIDAK |
| q5:j_ema9 | 12021 | -10.839 | 18.964 | 0.774 | 44.16 | 1.517 | -0.789 | -6.554 | ya | ya | TIDAK |
| pocket_pivot&q5:rs_spy_6b | 11802 | -3.393 | 18.812 | 3.499 | 47.66 | 1.293 | 0.092 | -3.683 | ya | ya | TIDAK |
| pocket_pivot&q5:julat20 | 11620 | -5.85 | 18.239 | 2.003 | 46.42 | 0.865 | 0.371 | -3.771 | ya | ya | TIDAK |
| ema_crossback&q5:j_ma200 | 9563 | 2.487 | 17.817 | 5.027 | 51.93 | 0.331 | -1.273 | -2.465 | ya | ya | TIDAK |
| ema_crossback&q5:rs_spy_6b | 9619 | 1.944 | 17.519 | 4.631 | 51.58 | -0.199 | -1.141 | -2.93 | ya | ya | TIDAK |
| rsi_lintas50&q5:j_ma200 | 9562 | 1.869 | 17.344 | 3.819 | 51.61 | -0.275 | -2.126 | -3.42 | ya | ya | TIDAK |
| ema_crossback&q5:cerun_ma50 | 9996 | 2.119 | 16.289 | 3.866 | 51.77 | -0.454 | -1.516 | -2.651 | ya | ya | TIDAK |
| gap_and_go&q5:vol_n50 | 6742 | 3.705 | 17.561 | 5.154 | 53.4 | -0.535 | -1.397 | -2.761 | ya | ya | TIDAK |
| b:gap_and_go | 6742 | 3.705 | 17.561 | 5.154 | 53.4 | -0.535 | -1.397 | -2.761 | ya | ya | TIDAK |

## 3. Portfolio bergabung 8 slot (2020-01-01 – 2026-10-16)

SPY tempoh sama: jumlah 158.39%, CAGR 15.01%, MDD -33.72%.

### Polisi `chandelier_4atr`

Arm kawalan:

| arm | n_posisi | purata_slot | purata_hari_pegang | pulangan_jumlah | cagr | mdd | median_bulanan | pct_bulan_ge10 | pct_bulan_positif | bulan_terburuk |
|---|---|---|---|---|---|---|---|---|---|---|
| X+R | 198 | 7.22 | 63.2 | -61.01 | -12.96 | -87.27 | -1.28 | 18.3 | 39.0 | -30.74 |
| X+X | 232 | 7.33 | 54.9 | -5.37 | -0.81 | -45.49 | -0.03 | 4.9 | 45.1 | -18.49 |

Arm S+R, 8 teratas ikut CAGR (daripada 46 signal); 1 mengalahkan SPY, 0 mencapai median bulanan ≥ +10%:

| signal | n_posisi | purata_slot | pulangan_jumlah | cagr | mdd | median_bulanan | pct_bulan_ge10 | pct_bulan_positif | bulan_terburuk |
|---|---|---|---|---|---|---|---|---|---|
| ema_crossback&q5:atr_pct | 215 | 7.18 | 178.28 | 16.28 | -59.31 | 0.0 | 20.7 | 47.6 | -21.59 |
| rsi_lintas50&q1:j_52w_tinggi | 217 | 7.26 | 148.06 | 14.32 | -65.8 | -0.09 | 19.5 | 45.1 | -19.67 |
| ema_crossback&q5:julat20 | 224 | 7.33 | 101.61 | 10.88 | -65.59 | -0.37 | 14.6 | 46.3 | -24.46 |
| gap_and_go&q5:vol_n50 | 220 | 7.24 | 89.17 | 9.85 | -59.61 | 0.0 | 20.7 | 48.8 | -27.63 |
| b:gap_and_go | 220 | 7.24 | 89.17 | 9.85 | -59.61 | 0.0 | 20.7 | 48.8 | -27.63 |
| ema_crossback&q1:vol_n50 | 229 | 7.2 | 76.3 | 8.71 | -72.35 | 0.0 | 17.1 | 46.3 | -21.4 |
| macd_cross&q1:j_ma200 | 220 | 7.27 | 71.38 | 8.26 | -39.54 | 0.92 | 9.8 | 53.7 | -19.19 |
| ema_crossback&q5:j_ma200 | 218 | 7.33 | 71.3 | 8.25 | -76.0 | 0.0 | 15.9 | 46.3 | -22.54 |

### Polisi `jual_hari63`

Arm kawalan:

| arm | n_posisi | purata_slot | purata_hari_pegang | pulangan_jumlah | cagr | mdd | median_bulanan | pct_bulan_ge10 | pct_bulan_positif | bulan_terburuk |
|---|---|---|---|---|---|---|---|---|---|---|
| X+R | 200 | 7.26 | 63.0 | -62.14 | -13.33 | -87.75 | 0.0 | 19.5 | 42.7 | -32.95 |
| X+X | 200 | 7.26 | 63.0 | 38.2 | 4.88 | -53.74 | 0.0 | 11.0 | 46.3 | -18.94 |

Arm S+R, 8 teratas ikut CAGR (daripada 46 signal); 1 mengalahkan SPY, 0 mencapai median bulanan ≥ +10%:

| signal | n_posisi | purata_slot | pulangan_jumlah | cagr | mdd | median_bulanan | pct_bulan_ge10 | pct_bulan_positif | bulan_terburuk |
|---|---|---|---|---|---|---|---|---|---|
| q1:j_ma200 | 200 | 7.26 | 174.71 | 16.05 | -62.97 | 0.88 | 19.5 | 54.9 | -23.0 |
| ema_crossback&q5:atr_pct | 200 | 7.26 | 137.61 | 13.6 | -58.6 | 0.04 | 19.5 | 50.0 | -25.18 |
| ema_crossback&q1:vol_n50 | 200 | 7.26 | 128.18 | 12.92 | -41.89 | 0.0 | 13.4 | 48.8 | -16.37 |
| q1:roc20 | 200 | 7.26 | 110.95 | 11.63 | -74.48 | 0.0 | 20.7 | 48.8 | -28.02 |
| ema_crossback&q5:rs_spy_6b | 200 | 7.26 | 84.73 | 9.46 | -64.9 | 0.28 | 19.5 | 51.2 | -25.96 |
| ema_crossback&q5:bb_lebar | 200 | 7.26 | 55.38 | 6.71 | -66.59 | 1.58 | 13.4 | 56.1 | -23.73 |
| pocket_pivot&q1:lapis | 200 | 7.26 | 53.1 | 6.48 | -47.56 | 0.0 | 7.3 | 47.6 | -19.51 |
| macd_cross&q1:j_ma200 | 200 | 7.26 | 46.04 | 5.74 | -46.52 | 0.26 | 13.4 | 50.0 | -22.8 |

### Polisi `pegang_252`

Arm kawalan:

| arm | n_posisi | purata_slot | purata_hari_pegang | pulangan_jumlah | cagr | mdd | median_bulanan | pct_bulan_ge10 | pct_bulan_positif | bulan_terburuk |
|---|---|---|---|---|---|---|---|---|---|---|
| X+R | 56 | 7.99 | 244.6 | 86.81 | 9.64 | -56.3 | 1.18 | 22.0 | 58.5 | -26.7 |
| X+X | 56 | 7.99 | 244.6 | 186.46 | 16.77 | -44.76 | 1.28 | 13.4 | 59.8 | -18.94 |

Arm S+R, 8 teratas ikut CAGR (daripada 46 signal); 17 mengalahkan SPY, 0 mencapai median bulanan ≥ +10%:

| signal | n_posisi | purata_slot | pulangan_jumlah | cagr | mdd | median_bulanan | pct_bulan_ge10 | pct_bulan_positif | bulan_terburuk |
|---|---|---|---|---|---|---|---|---|---|
| ema_crossback&q5:j_ma200 | 48 | 7.06 | 510.47 | 30.54 | -54.42 | 0.04 | 20.7 | 50.0 | -21.54 |
| rsi_lintas50&q5:j_ma200 | 50 | 7.29 | 457.15 | 28.8 | -54.43 | 0.71 | 23.2 | 56.1 | -20.3 |
| ema_crossback&q5:rs_spy_6b | 50 | 7.29 | 413.49 | 27.26 | -54.37 | 1.02 | 19.5 | 56.1 | -20.88 |
| pocket_pivot&q5:bb_lebar | 53 | 7.64 | 384.38 | 26.17 | -55.16 | 1.58 | 25.6 | 59.8 | -18.47 |
| q5:j_ema9 | 56 | 7.99 | 355.04 | 25.01 | -72.7 | 2.63 | 32.9 | 52.4 | -26.17 |
| q5:bb_lebar | 56 | 7.99 | 327.21 | 23.86 | -62.43 | 1.59 | 29.3 | 58.5 | -26.94 |
| pocket_pivot&q5:rs_spy_6b | 51 | 7.41 | 322.4 | 23.65 | -55.62 | 2.32 | 22.0 | 56.1 | -21.29 |
| rsi_lintas50&q5:rs_spy_6b | 51 | 7.41 | 299.47 | 22.64 | -55.27 | 0.31 | 18.3 | 51.2 | -25.98 |

### Sasaran +10% sebulan (median)

**0 daripada 282** kombinasi (signal × arm × polisi) mencapai median bulanan ≥ +10%. Terbaik: 2.63%.

## 4. Fasa HOLD — kelas pullback sebagai peraturan jual

Posisi entry-agnostik (arm X+R: 8 saham RS 6 bulan tertinggi dalam universe setiap hari), set posisi yang SAMA bagi ketiga-tiga peraturan jual. Definisi kausal kelas pullback: SPEC §13.12 B7.

| polisi | n | median | purata | purata_dipangkas5 | kadar_menang | lebihan_spy_purata | lebihan_bawah95_ticker | median_hari | pf_cagr | pf_mdd | pf_median_bulanan | pf_pct_bulan_positif | spy_cagr |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| chandelier_4atr | 12064 | -12.99 | -1.601 | -11.105 | 32.06 | -4.784 | -9.473 | 44.0 | -12.96 | -87.27 | -1.28 | 39.0 | 15.01 |
| pegang_252 | 12064 | -17.572 | 13.742 | -5.829 | 40.19 | -3.772 | -16.079 | 252.0 | 9.64 | -56.3 | 1.18 | 58.5 | 15.01 |
| pullback_amaran | 12064 | -4.947 | -0.597 | -4.399 | 29.39 | -1.167 | -2.165 | 6.0 | -22.98 | -94.2 | -1.14 | 36.6 | 15.01 |

## 5. Kesimpulan

1. **1 daripada 138 ujian (signal × polisi) lulus syarat ablasi.** Dengan 138 perbandingan serentak, jangkaan positif palsu pada 5% ialah kira-kira 7 — jadi bilangan yang lulus **tidak melebihi apa yang nasib sahaja akan hasilkan**. FASA 2 tidak mendaftar FDR lebih awal, jadi mana-mana signal yang lulus mesti dianggap hipotesis, bukan penemuan.

2a. Polisi `chandelier_4atr`: median dagangan arm S+R (merentas signal) -7.08% lawan arm rawak X+X -3.374%; purata dipangkas 5% -4.5% lawan -1.627%; kadar menang 36.63% lawan 40.46%. **Pemilihan rawak daripada universe mengalahkan signal** pada ketiga-tiga ukuran.

2b. Polisi `jual_hari63`: median dagangan arm S+R (merentas signal) -1.18% lawan arm rawak X+X 1.968%; purata dipangkas 5% -2.71% lawan 0.05%; kadar menang 48.17% lawan 54.75%. **Pemilihan rawak daripada universe mengalahkan signal** pada ketiga-tiga ukuran.

2c. Polisi `pegang_252`: median dagangan arm S+R (merentas signal) -3.06% lawan arm rawak X+X 7.83%; purata dipangkas 5% 0.01% lawan 6.472%; kadar menang 47.84% lawan 58.94%. **Pemilihan rawak daripada universe mengalahkan signal** pada ketiga-tiga ukuran.

3. Portfolio bergabung: 119 daripada 138 kombinasi S+R kalah kepada SPY (15.01% CAGR). Arm rawak X+X dengan `pegang_252` memberi 16.77% CAGR — lebih tinggi daripada SPY dan daripada median S+R pada setiap polisi.

4. **X+R ialah arm terburuk pada setiap polisi.** 8 saham RS 6 bulan tertinggi dalam universe 2000 saham ialah hujung momentum yang paling kerap berbalik; itu, bukan signal, yang menerangkan mengapa FASA 1 nampak seperti signal "mengalahkan" sesuatu apabila dibanding dengan susunan RS.

5. **Fasa HOLD: kelas pullback tidak bertukar menjadi wang.** Sebagai peraturan jual ia memberi median -4.947% setiap dagangan, kadar menang 29.39%, median pegangan 6.0 hari, dan CAGR portfolio -22.98% (MDD -94.2%) berbanding SPY 15.01%. Ia menyala terlalu awal dan pusing ganti membunuh baki apa-apa kelebihan. Penemuan FASA 1 (SIHAT/PASARAN 80–92% sambung ke puncak baharu lawan AMARAN 44–54%) kekal benar sebagai **perihalan**, tetapi ia diukur atas run yang sudah naik, dan sebagai peraturan keputusan ia merugikan.

6. Sasaran pengguna +10% sebulan (median): **0 daripada 282** kombinasi mencapainya; tertinggi 2.63%.


### Apa yang ini TIDAK buktikan

- Bukan bukti bahawa tiada kelebihan boleh didapati dalam data ini; ia bukti bahawa **46 signal yang FASA 1 hasilkan tidak membawa kelebihan boleh dagang**, dan bahawa cara FASA 1 mengukur (puncak dalam tetingkap) memilih kemeruapan.
- Tiada saham delist: angka rawak X+X juga dipandang tinggi oleh survivorship, mungkin lebih daripada arm signal (saham yang mati lebih berkemungkinan muncul dalam pilihan rawak daripada dalam pilihan signal momentum). Perbandingan arm tetap sah kerana kesemuanya memakai data yang sama, tetapi aras mutlak bukan jangkaan.
- Satu signal contrarian (`q1:cerun_ema21`, kuintil terendah cerun EMA21) ialah satu-satunya yang lulus, dan hanya pada satu polisi. Arahnya bertentangan dengan keluarga momentum/kemeruapan yang FASA 1 tumpukan. Itu petunjuk untuk fasa seterusnya, bukan keputusan.
