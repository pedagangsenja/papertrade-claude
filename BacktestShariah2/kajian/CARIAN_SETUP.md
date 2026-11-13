# Carian Setup CS04 — tala parameter di sekitar pemenang (backtest, BUKAN bukti)

> **Status keputusan (kad skor, harga 2026-11-12):** TERBUKTI 0 · CALON 0 · BELUM CUKUP 223 · GAGAL 0 · NEGATIF 0. Rejim QQQ OFF sejak 2026-10-16. Hanya **TERBUKTI** layak untuk wang sebenar (`laporan/KAD_SKOR.md`); nombor dalam laporan ini BUKAN keputusan dan tidak boleh dibaca sebagai pangkat untuk wang sebenar.

Dijana `kajian/carian_setup/cs_tala.py`. Pradaftar: `kajian/SPEC_CARIAN_SETUP.md` pindaan 13 Nov 2026 (e). **Jangan sunting secara manual.** Papan induk (CS03): `carian_setup/hasil/CS03/LAPORAN.md`.

## 1. Apa yang dibuat

Sepuluh masuk terbaik CS03 (`F21`–`F30`, dipangkatkan ikut kadar tangkap saham "lari") ditala: 24 varian parameter (±25 %) bagi induk berasaskan kaedah M, dan grid ambang bagi penapis RS, ATR % dan jarak dari puncak 52 minggu. Anak dipilih pada kumpulan A ikut **dataran** (median sel dan jirannya), kemudian induk dan anak dibandingkan pada **kumpulan B** (saham yang carian tidak lihat). "Lari" = naik ≥ 5 % minggu pertama, capai ≥ 10 % sebelum henti −8 %, masih ≥ 10 % pada minggu ke-4. Rawak = saham lain hari sama, tahap turun-naik sama.

## 2. Induk lawan anak (kumpulan B, 2010 – Ogo 2026)

| Induk | Anak | Masuk | Penapis | Belian | **Lari %** (rawak) | Capai +10 % dahulu % (rawak) | Kena henti −8 % dahulu % (rawak) | Kelebihan lari: induk → anak | K3 sahaja: induk → anak |
|---|---|---|---|---|---|---|---|---|---|
| `F21` | `F31` | N40 OBV tinggi baharu + MA50 (benih N) | F03 tutup > MA200 DAN >= 20% di bawah puncak 52 minggu | 2,469 | **9.5 (8.0)** | 29.8 (27.5) | 46.9 (41.8) | +1.72 → +1.46 | +4.14 → +2.77 |
| `F22` | `F32` | M84 Jarak purata bergerak MAD 21/200 (benih M, varian t4: close_ambang_5=2, rma_atr_14=16, rma_atr_kali_3=2.01, rolling_200=317, rolling_21=23, rolling_50=89) | ATR% >= 4 DAN F26 rejim QQQ ON | 2,534 | **13.9 (10.4)** | 36.0 (31.1) | 56.1 (49.1) | +3.49 → +3.51 | +2.68 → +2.65 |
| `F23` | `F33` | M21 Marius 3 Persediaan (Pecahan+Jurang+Kesinambungan) (benih M, varian t8: atr_14=15, c_ambang_0_75=0.568, o_ambang_0_05=0.045, rolling_20=21, rolling_50=48, run_ambang_0_3=0.24) | RS >= 95 DAN F28 SPY > SMA200 | 491 | **15.5 (9.7)** | 36.5 (31.5) | 58.9 (47.6) | +4.30 → +5.76 | +0.14 → +1.36 |
| `F24` | `F34` | M49 Ichimoku (Tutup Atas Awan + Tenkan Silang Kijun) (benih M, varian t7: rolling_26=32, rolling_52=104, rolling_9=8, shift_26=48) | RS >= 95 DAN ATR% >= 4 | 1,550 | **13.8 (9.9)** | 35.9 (31.8) | 56.1 (47.1) | +3.12 → +3.88 | +2.02 → +2.22 |
| `F25` | `F35` | M57 Landry Trend Knockout (TKO) (benih M, varian t17: aliran_lag_2=4, c_ambang_0_15=0.178, rolling_10=15, rolling_50=44, rolling_63=62, shift_63=41) | RS >= 95 DAN ATR% >= 4 | 2,051 | **12.3 (9.5)** | 34.1 (30.8) | 58.2 (49.0) | +2.45 → +2.77 | +0.51 → +1.59 |
| `F26` | `F36` | M50 Elder Triple Screen (benih M, varian 2: ewm_span_12=24, ewm_span_2=3, ewm_span_26=17, ewm_span_9=10, rolling_50=39) | RS >= 95 DAN ATR% >= 6 | 902 | **13.5 (10.7)** | 36.5 (33.0) | 62.3 (51.3) | +2.36 → +2.78 | -0.54 → -2.09 |
| `F27` | kekal | N73 Tutup bawah jalur bawah BB(20,2) (benih N) | RS >= 70 DAN ATR% >= 4 | 4,818 | **14.6 (12.1)** | 38.5 (34.2) | 49.0 (48.3) | +2.55 → +2.55 | +3.24 → +3.24 |
| `F28` | `F37` | M92 CCI-50 (benih M, varian 2: cci_50=91, rma_atr_14=15, rma_atr_kali_2=2.496) | >= 20% di bawah puncak 52 minggu DAN F27 rejim QQQ OFF | 5,691 | **10.4 (9.0)** | 31.4 (28.9) | 44.6 (41.4) | +1.70 → +1.43 | +2.51 → +0.92 |
| `F29` | `F38` | P13 RSI14 silang atas 60 | RS >= 95 DAN ATR% >= 4 | 2,529 | **13.2 (9.8)** | 35.3 (31.5) | 55.2 (47.9) | +1.99 → +3.36 | -0.49 → +1.23 |
| `F30` | kekal | N43 Undur EMA8 + penapis MA50 (benih N) | F15 Supertrend naik DAN ATR% >= 4 | 10,715 | **11.5 (10.1)** | 34.7 (32.1) | 52.3 (48.0) | +1.43 → +1.43 | +1.61 → +1.61 |

- Induk yang ditala menjadi anak baharu: 8 daripada 10; selebihnya induk sendiri sudah berada di dataran terbaik.
- Anak yang kelebihan "lari"-nya melebihi induk pada kumpulan B: **6 daripada 8**; pada K3 (tahun yang tidak dipakai carian): **4 daripada 8**.
- Median kelebihan: induk +2.40 mata → anak +2.78 mata.

## 3. Cara pegang dan keluar terbaik bagi setiap anak (dipilih pada kumpulan A; angka kumpulan B)

| Setup | Henti | Keluar | K1: purata % / menang % / pegang | K2: purata % / menang % / pegang | K3: purata % / menang % / pegang |
|---|---|---|---|---|---|
| `F31` | H2 -10% | X09 MACD < isyarat ATAU X10 histogram MACD turun 3 hari | -0.47 / 36.9 / 3.6 | -0.51 / 36.3 / 3.7 | -0.10 / 37.5 / 4.2 |
| `F32` | H3 3xATR14 | X11 RSI14 < 50 ATAU X21 Stochastic silang turun di atas 80 | -0.57 / 38.2 / 4.3 | +0.81 / 39.9 / 4.6 | +0.41 / 43.8 / 3.8 |
| `F33` | H2 -10% | X13 RSI14 > 80 ATAU X21 Stochastic silang turun di atas 80 | +0.61 / 48.2 / 3.4 | -0.35 / 43.4 / 2.6 | -1.62 / 40.3 / 2.4 |
| `F34` | H4 4xATR14 | X21 Stochastic silang turun di atas 80 ATAU X22 hari turun dengan volum >= 1.5x | +0.07 / 48.0 / 7.6 | -0.77 / 44.7 / 7.0 | -0.83 / 44.3 / 8.0 |
| `F35` | H4 4xATR14 | X08 MA10 < MA20 DAN X24 +DI < -DI | -1.07 / 36.6 / 13.0 | +1.07 / 39.1 / 13.5 | -0.62 / 38.5 / 13.3 |
| `F36` | H4 4xATR14 | X12 RSI14 silang turun bawah 70 ATAU X21 Stochastic silang turun di atas 80 | -0.45 / 50.7 / 14.1 | +1.00 / 52.3 / 13.3 | -3.49 / 43.3 / 13.8 |
| `F27` | H4 4xATR14 | X07 dua tutup berturut < MA20 DAN X21 Stochastic silang turun di atas 80 | +1.66 / 53.4 / 18.9 | +1.44 / 52.7 / 18.3 | +3.22 / 55.9 / 19.4 |
| `F37` | H4 4xATR14 | X20 tutup < 92% tutup tertinggi sejak beli DAN X21 Stochastic silang turun di atas 80 | +0.46 / 52.6 / 18.4 | +1.46 / 52.1 / 18.0 | -0.31 / 46.1 / 18.2 |
| `F38` | H2 -10% | X14 Supertrend turun ATAU X18 Chandelier 3xATR14 (dari tutup tertinggi sejak beli) | -0.59 / 38.2 / 12.1 | +1.27 / 36.4 / 11.5 | -0.43 / 34.4 / 10.4 |
| `F30` | H4 4xATR14 | X21 Stochastic silang turun di atas 80 DAN X22 hari turun dengan volum >= 1.5x | +0.00 / 50.5 / 18.1 | +1.42 / 51.7 / 18.0 | +1.25 / 51.8 / 18.1 |

## 4. Kaveat

- Backtest sahaja; tiada setup masuk papertrade tanpa keputusan pengguna. Kad skor kekal satu-satunya keputusan wang sebenar.
- Penalaan memilih sel terbaik daripada banyak sel; sebab itu perbandingan induk lawan anak dibuat pada saham yang tidak dilihat. Anak yang tidak mengatasi induk di situ tidak patut menggantikannya.
- Tiada saham delist (condong ke atas); set 2000 bukan tapisan Shariah; data bermula 2010.
