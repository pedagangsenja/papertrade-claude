# CS09 lorong TREND — keluar ikut kata pengguna pada papan T01–T12 (backtest; BUKAN bukti)

> **Status keputusan (kad skor, harga 2026-11-13):** TERBUKTI 0 · CALON 0 · BELUM CUKUP 226 · GAGAL 0 · NEGATIF 0. Rejim QQQ OFF sejak 2026-10-16. Hanya **TERBUKTI** layak untuk wang sebenar (`laporan/KAD_SKOR.md`); nombor dalam laporan ini BUKAN keputusan dan tidak boleh dibaca sebagai pangkat untuk wang sebenar.

Dijana `kajian/carian_setup/cs_trend9.py`. Pradaftar: `kajian/SPEC_CARIAN_SETUP.md` pindaan 15 Nov 2026 (w), dikomit sebelum dijalankan. **Jangan sunting secara manual.**

## 1. Jawapan

- **Peraturan sejagat U_T\*** (dipilih pada kumpulan A sahaja): **rugi (tutup < harga beli, sesi ≥ 40) DAN tutup < rendah 50 hari** → jual pada buka sesi berikutnya. Skor kumpulan A -2.18 mata purata; simpan pelari besar 0.95; 0 daripada 104 peraturan berskor positif pada kumpulan A.
- **Bacaan dikunci:** peraturan pengguna TIDAK menolong lorong trend (0 daripada 11 setup dipercayai-T ditolong pada kumpulan B; median beza purata -0.20 mata). Idea itu TIDAK teguh: 3 daripada 104 peraturan mempunyai median beza purata > 0 (peringkat 1, tanpa pemilihan).

## 2. Setiap setup: "pegang sahaja" (`X00`) → dengan U_T\* (kumpulan B)

| ID | perc. | henti | belian | purata % | median % | menang % | rugi ≥ 15 % | dijual ≥ +30 % | untung pelari besar % | dijual U_T\* % | sesi pegang (median) | ditolong |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `T01` | ✓ | 6xATR14 | 308 | +16.9 → +16.7 | +5.4 → -3.6 | 54.2 → 45.2 | 33.4 → 30.1 | 32.5 → 30.4 | 64.6 → 64.9 | 42.9 | 126 → 115 | ✗ |
| `T02` | ✓ | 6xATR14 | 305 | +17.7 → +17.4 | +5.9 → -3.5 | 54.8 → 45.8 | 32.8 → 29.5 | 33.4 → 31.2 | 66.0 → 66.4 | 42.2 | 126 → 116 | ✗ |
| `T03` | ✓ | 6xATR14 | 203 | +12.0 → +12.4 | +2.4 → -4.4 | 51.7 → 42.4 | 36.9 → 27.8 | 29.1 → 27.3 | 63.0 → 64.8 | 44.9 | 126 → 104 | ✗ |
| `T04` | ✓ | 6xATR14 | 260 | +1.4 → +0.7 | -14.7 → -13.5 | 37.3 → 26.0 | 49.6 → 46.6 | 23.1 → 19.1 | 53.5 → 52.5 | 58.8 | 126 → 70 | ✗ |
| `T05` | ✓ | 6xATR14 | 358 | +3.4 → +3.4 | -12.8 → -9.2 | 40.8 → 34.3 | 46.1 → 37.3 | 18.4 → 16.4 | 57.7 → 56.3 | 41.2 | 126 → 80 | ✗ |
| `T06` | ✓ | 6xATR14 | 259 | +1.5 → +0.7 | -14.5 → -13.6 | 37.5 → 26.1 | 49.4 → 46.7 | 23.2 → 19.2 | 53.5 → 52.5 | 58.6 | 126 → 69 | ✗ |
| `T07` | ✓ | 6xATR14 | 330 | +8.1 → +6.6 | -2.7 → -7.3 | 48.8 → 38.1 | 40.3 → 37.8 | 26.1 → 23.3 | 56.2 → 52.0 | 43.5 | 126 → 85 | ✗ |
| `T08` | ✓ | 6xATR14 | 297 | +2.1 → +2.4 | -14.6 → -11.4 | 38.0 → 30.8 | 49.5 → 45.0 | 21.9 → 18.2 | 55.7 → 51.8 | 46.0 | 126 → 77 | ✗ |
| `T09` | ✗ | 6xATR14 | 207 | -1.6 → -2.3 | -15.6 → -13.6 | 37.7 → 27.5 | 50.2 → 48.8 | 20.3 → 17.4 | 43.6 → 41.8 | 51.7 | 126 → 75 | ✗ |
| `T10` | ✓ | 6xATR14 | 380 | +2.9 → +2.7 | -12.5 → -8.7 | 38.2 → 29.5 | 44.2 → 32.6 | 17.9 → 16.1 | 54.3 → 53.4 | 42.4 | 126 → 80 | ✗ |
| `T11` | ✓ | -20% | 250 | +8.2 → +7.3 | -9.3 → -9.4 | 42.4 → 31.6 | 47.2 → 38.0 | 21.2 → 20.0 | 65.8 → 63.7 | 32.4 | 126 → 79 | ✗ |
| `T12` | ✓ | 6xATR14 | 242 | +8.5 → +8.6 | -5.3 → -7.3 | 46.7 → 37.2 | 41.3 → 35.9 | 24.4 → 22.7 | 61.3 → 59.3 | 45.5 | 126 → 100 | ✗ |

## 3. Adakah gabungan DAN itu yang bekerja? (kumpulan B, median beza lawan `X00`, mata)

| Keluar | purata | median | menang | rugi ≥ 15 % | dijual ≥ +30 % | untung pelari besar | setup ditolong |
|---|---|---|---|---|---|---|---|
| U_T\* (rugi (tutup < harga beli, sesi ≥ 40) DAN tutup < rendah 50 hari) | -0.29 | +0.39 | -9.4 | -3.9 | -2.1 | -1.2 | 0 / 12 |
| "rugi → jual" sahaja (sesi ≥ 40, tanpa syarat trend) | -0.38 | +6.43 | -17.1 | -20.1 | -5.8 | -4.9 | 0 / 12 |
| "tutup < rendah 50 hari → jual" sahaja (walaupun untung) | -0.09 | +0.88 | -7.1 | -9.9 | -6.0 | -2.8 | 0 / 12 |

## 4. Peringkat 1: setiap peraturan (kumpulan B, tanpa pemilihan)

Median beza purata lawan `X00` merentas 12 setup (mata), ikut takrif "trend patah" × sesi mula menilai rugi; dalam kurungan: bilangan setup ditolong.

| Trend patah | d = 3 | d = 10 | d = 20 | d = 40 | rugi ≥ 15 % (d = 3) | pelari besar simpan (d = 3) |
|---|---|---|---|---|---|---|
| tutup < MA20 | -3.38 (0) | -2.54 (0) | -2.21 (0) | -0.49 (0) | -42.1 | 0.42 |
| tutup < MA50 | -2.88 (0) | -1.93 (0) | -1.49 (0) | -0.50 (0) | -37.9 | 0.48 |
| tutup < MA100 | -1.80 (0) | -1.83 (0) | -1.47 (0) | -0.66 (0) | -30.5 | 0.67 |
| tutup < MA150 | -1.23 (0) | -1.16 (0) | -0.83 (0) | -0.42 (0) | -17.2 | 0.83 |
| dua tutup berturut < MA20 | -3.07 (0) | -2.46 (0) | -2.12 (0) | -0.61 (0) | -40.1 | 0.47 |
| dua tutup berturut < MA50 | -2.75 (0) | -1.24 (0) | -1.37 (0) | -0.67 (0) | -36.3 | 0.52 |
| dua tutup berturut < MA100 | -1.75 (0) | -1.77 (0) | -0.97 (0) | -0.79 (0) | -26.9 | 0.70 |
| MA20 < MA50 | -2.34 (0) | -0.84 (0) | -0.56 (0) | -0.17 (0) | -29.3 | 0.62 |
| MA50 menurun (lawan 5 sesi lalu) | -2.83 (0) | -2.04 (0) | -1.44 (0) | -0.73 (0) | -28.6 | 0.64 |
| tutup < EMA20 | -3.81 (0) | -2.20 (0) | -2.17 (0) | -0.47 (0) | -42.4 | 0.39 |
| tutup < EMA50 | -2.54 (0) | -1.90 (0) | -1.74 (0) | -0.56 (0) | -38.1 | 0.47 |
| tutup < EMA100 | -1.88 (0) | -1.71 (0) | -1.10 (0) | -0.53 (0) | -29.1 | 0.67 |
| Supertrend(10, 3.0) turun | -1.91 (0) | -1.31 (0) | -1.13 (0) | -0.98 (0) | -34.8 | 0.54 |
| Supertrend(10, 4.0) turun | -1.21 (0) | -0.75 (0) | -0.87 (0) | -0.35 (0) | -28.7 | 0.73 |
| Supertrend(14, 3.0) turun | -1.70 (0) | -1.43 (0) | -1.15 (0) | -0.82 (0) | -35.0 | 0.56 |
| Supertrend(14, 4.0) turun | -1.61 (0) | -1.04 (0) | -0.87 (0) | -0.42 (0) | -28.1 | 0.69 |
| Supertrend(20, 5.0) turun | -0.77 (0) | -0.50 (0) | -0.58 (0) | -0.04 (0) | -21.9 | 0.78 |
| tutup < rendah 10 hari | -2.13 (0) | -2.11 (0) | -1.42 (0) | -0.97 (0) | -33.7 | 0.63 |
| tutup < rendah 20 hari | -1.47 (0) | -1.24 (0) | -0.99 (0) | -1.03 (0) | -23.6 | 0.74 |
| tutup < rendah 50 hari | +0.36 (0) | +0.36 (0) | +0.30 (0) | -0.29 (0) | -9.7 | 0.96 |
| MACD(12,26,9) < isyarat | -3.43 (0) | -2.54 (0) | -2.09 (0) | -0.57 (0) | -41.3 | 0.43 |
| MACD(24,52,18) < isyarat | -2.40 (0) | -1.47 (0) | -1.52 (0) | -0.76 (0) | -41.4 | 0.40 |
| RSI14 < 35 | -0.89 (0) | -1.17 (0) | -0.95 (0) | -0.57 (0) | -13.7 | 0.89 |
| RSI14 < 40 | -1.72 (0) | -1.16 (0) | -1.00 (0) | -0.62 (0) | -29.4 | 0.70 |
| RSI14 < 45 | -2.88 (0) | -2.16 (0) | -2.08 (0) | -0.59 (0) | -38.0 | 0.54 |
| RSI14 < 50 | -2.95 (0) | -2.16 (0) | -1.95 (0) | -0.45 (0) | -41.9 | 0.42 |

## 5. Kaveat

- Papan `T` dipilih pada kumpulan A dan dibaca pada kumpulan B (CS08); 12 setup sahaja, banyak berkongsi prasyarat hasil suku tumbuh ≥ 20 %, jadi bilangan "setup ditolong" bukan 12 ujian bebas. Tiada saham delist.
- Tiada perubahan papan `T`, registry atau kohort.

