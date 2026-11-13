# Carian Setup CS03 — papan 10 teratas ikut KADAR TANGKAP (backtest, BUKAN bukti)

> **Status keputusan (kad skor, harga 2026-11-12):** TERBUKTI 0 · CALON 0 · BELUM CUKUP 223 · GAGAL 0 · NEGATIF 0. Rejim QQQ OFF sejak 2026-10-16. Hanya **TERBUKTI** layak untuk wang sebenar (`laporan/KAD_SKOR.md`); nombor dalam laporan ini BUKAN keputusan dan tidak boleh dibaca sebagai pangkat untuk wang sebenar.

Dijana `kajian/carian_setup/cs_tangkap.py`. Pradaftar: `kajian/SPEC_CARIAN_SETUP.md` pindaan 13 Nov 2026 (d). **Jangan sunting secara manual.** Pusingan lama: `carian_setup/hasil/CS01|CS02/LAPORAN.md`.

## 1. Apa yang dipangkatkan

Setup yang **paling kerap menangkap saham yang mula naik kuat**. Saham "lari" = naik ≥ 5 % pada minggu pertama, mencapai ≥ 10 % sebelum henti −8 %, dan masih ≥ 10 % di atas harga beli pada minggu ke-4. "Rawak" = saham lain yang layak pada **hari yang sama dan tahap turun-naik yang sama**; kelebihan = kadar setup − rawak.

Carian: kumpulan A set 2000, 233,000 peraturan masuk dicuba, 182,903 cukup isyarat; 4.2 % mempunyai had bawah kelebihan positif dalam kedua-dua era. Angka di bawah daripada **kumpulan B** (saham yang carian tidak lihat), 2010 – Ogo 2026.

## 2. Papan 10 teratas

| # | ID | Masuk | Penapis | Belian | **Lari %** (rawak) | Capai +10 % dahulu % (rawak) | Capai +20 % % (rawak) | Naik 5 % minggu 1 % (rawak) | Kena henti −8 % dahulu % (rawak) | T1 | T2 | T3 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `F21` | N40 OBV tinggi baharu + MA50 (benih N) | F03 tutup > MA200 DAN F20 >= 30% di bawah puncak 52 minggu | 851 | **11.3 (9.6)** | 33.1 (31.0) | 12.7 (11.4) | 22.1 (20.0) | 52.1 (45.3) | ✓ | ✓ | ✓ |
| 2 | `F22` | M84 Jarak purata bergerak MAD 21/200 (benih M, varian 1: close_ambang_5=2, rma_atr_14=19, rma_atr_kali_3=2.188, rolling_200=350, rolling_21=19, rolling_50=85) | F23 ATR% >= 4 DAN F26 rejim QQQ ON | 2,480 | **14.0 (10.5)** | 36.4 (31.5) | 17.1 (11.8) | 27.1 (22.9) | 55.8 (48.5) | ✓ | ✓ | ✓ |
| 3 | `F23` | M21 Marius 3 Persediaan (Pecahan+Jurang+Kesinambungan) (benih M, parameter asal) | F17 RS >= 90 DAN F28 SPY > SMA200 | 630 | **14.6 (10.3)** | 36.8 (32.5) | 19.8 (12.5) | 29.2 (21.7) | 57.8 (47.6) | ✗ | ✓ | ✓ |
| 4 | `F24` | M49 Ichimoku (Tutup Atas Awan + Tenkan Silang Kijun) (benih M, varian 2: rolling_26=33, rolling_52=93, rolling_9=8, shift_26=40) | F17 RS >= 90 DAN F23 ATR% >= 4 | 2,405 | **13.3 (10.2)** | 36.0 (32.1) | 16.6 (11.8) | 25.7 (21.4) | 54.7 (47.7) | ✓ | ✓ | ✓ |
| 5 | `F25` | M57 Landry Trend Knockout (TKO) (benih M, varian 1: aliran_lag_2=4, c_ambang_0_15=0.157, rolling_10=16, rolling_50=40, rolling_63=52, shift_63=51) | F17 RS >= 90 DAN F23 ATR% >= 4 | 3,166 | **12.2 (9.8)** | 33.8 (31.6) | 15.4 (11.8) | 24.5 (21.5) | 57.2 (48.4) | ✗ | ✓ | ✓ |
| 6 | `F26` | M50 Elder Triple Screen (benih M, varian 2: ewm_span_12=24, ewm_span_2=3, ewm_span_26=17, ewm_span_9=10, rolling_50=39) | F17 RS >= 90 DAN F23 ATR% >= 4 | 3,388 | **12.0 (9.7)** | 36.5 (31.4) | 16.4 (11.6) | 25.2 (21.4) | 55.3 (48.7) | ✓ | ✗ | ✓ |
| 7 | `F27` | N73 Tutup bawah jalur bawah BB(20,2) (benih N) | F16 RS >= 70 DAN F23 ATR% >= 4 | 4,816 | **14.6 (12.1)** | 38.5 (34.2) | 16.8 (13.1) | 27.5 (24.4) | 49.0 (48.3) | ✓ | ✓ | ✓ |
| 8 | `F28` | M92 CCI-50 (benih M, varian 2: cci_50=91, rma_atr_14=15, rma_atr_kali_2=2.496) | F20 >= 30% di bawah puncak 52 minggu DAN F27 rejim QQQ OFF | 2,704 | **11.9 (10.2)** | 35.5 (31.9) | 14.2 (10.9) | 22.2 (20.1) | 47.7 (44.2) | ✓ | ✓ | ✓ |
| 9 | `F29` | P13 RSI14 silang atas 60 | F17 RS >= 90 DAN F23 ATR% >= 4 | 4,009 | **11.9 (10.0)** | 34.5 (31.9) | 15.3 (11.8) | 25.0 (21.2) | 54.7 (48.0) | ✗ | ✗ | ✓ |
| 10 | `F30` | N43 Undur EMA8 + penapis MA50 (benih N) | F15 Supertrend naik DAN F23 ATR% >= 4 | 10,715 | **11.5 (10.1)** | 34.7 (32.1) | 14.3 (12.0) | 24.2 (21.6) | 52.3 (48.0) | ✓ | ✓ | ✓ |

- **T1:** kelebihan "capai +10 % dahulu" positif dalam K1, K2 dan K3. **T2:** kelebihan "lari" positif dalam ketiga-tiganya. **T3:** kelebihan "lari" melebihi persentil ke-95 peraturan rawak (+1.39 mata).

### Cara pegang dan keluar terbaik bagi setiap masuk (dipilih pada kumpulan A; angka kumpulan B)

| ID | Henti | Keluar | K1: purata % / menang % / pegang | K2: purata % / menang % / pegang | K3: purata % / menang % / pegang |
|---|---|---|---|---|---|
| `F21` | H2 -10% | X09 MACD < isyarat ATAU X10 histogram MACD turun 3 hari | -1.02 / 36.1 / 3.3 | -0.79 / 34.6 / 3.6 | +0.11 / 39.9 / 3.8 |
| `F22` | H2 -10% | X11 RSI14 < 50 ATAU X21 Stochastic silang turun di atas 80 | -0.62 / 37.8 / 4.3 | +0.45 / 39.1 / 4.4 | +0.28 / 43.3 / 3.8 |
| `F23` | H2 -10% | X12 RSI14 silang turun bawah 70 DAN X16 tutup < rendah 5 hari | +0.30 / 35.9 / 12.8 | +0.52 / 37.0 / 11.3 | -1.87 / 30.5 / 10.6 |
| `F24` | H4 4xATR14 | X11 RSI14 < 50 DAN X22 hari turun dengan volum >= 1.5x | +0.79 / 47.0 / 16.2 | +1.19 / 46.5 / 16.0 | +0.50 / 43.0 / 16.7 |
| `F25` | H4 4xATR14 | X22 hari turun dengan volum >= 1.5x DAN X24 +DI < -DI | -1.10 / 41.5 / 16.2 | +0.98 / 44.8 / 16.6 | -0.05 / 43.2 / 16.6 |
| `F26` | H4 4xATR14 | X12 RSI14 silang turun bawah 70 ATAU X22 hari turun dengan volum >= 1.5x | +0.17 / 47.4 / 11.8 | +0.28 / 46.3 / 12.1 | -1.25 / 42.5 / 12.4 |
| `F27` | H4 4xATR14 | X07 dua tutup berturut < MA20 DAN X21 Stochastic silang turun di atas 80 | +1.67 / 53.5 / 18.9 | +1.45 / 52.7 / 18.3 | +3.22 / 55.9 / 19.4 |
| `F28` | H4 4xATR14 | X20 tutup < 92% tutup tertinggi sejak beli DAN X21 Stochastic silang turun di atas 80 | +0.61 / 52.4 / 18.1 | +1.71 / 52.7 / 17.8 | +0.16 / 44.9 / 18.1 |
| `F29` | H2 -10% | X21 Stochastic silang turun di atas 80 DAN X22 hari turun dengan volum >= 1.5x | -0.16 / 42.9 / 13.5 | +0.35 / 38.3 / 11.9 | -0.33 / 37.2 / 11.6 |
| `F30` | H4 4xATR14 | X21 Stochastic silang turun di atas 80 DAN X22 hari turun dengan volum >= 1.5x | +0.00 / 50.5 / 18.1 | +1.42 / 51.7 / 18.0 | +1.25 / 51.8 / 18.1 |

## 3. Semakan kejujuran

**K3 ialah ujian sebenar** (saham lain DAN tahun yang tidak dipakai carian). Unit: mata peratus kelebihan "lari" atas rawak.

| Ukuran | Kunci K1 (kumpulan B, 2010–2019) | Kunci K2 (kumpulan B, 2020–2024) | Kunci K3 (kumpulan B, 2025 – Ogo 2026) |
|---|---|---|---|
| Median kelebihan, 200 peraturan teratas | +2.15 | +2.12 | +1.38 |
| Median kelebihan, 200 peraturan rawak | -0.03 | +0.13 | +0.41 |
| Teratas dengan kelebihan positif | 199 daripada 200 | 197 daripada 200 | 173 daripada 200 |
| Rawak dengan kelebihan positif | 96 daripada 200 | 115 daripada 200 | 128 daripada 197 |
| Spearman skor lawan kelebihan | +0.28 | +0.36 | -0.04 |

## 4. Kaveat

- Backtest sahaja; tiada setup masuk papertrade tanpa keputusan pengguna. Kad skor kekal satu-satunya keputusan wang sebenar.
- Tiada saham delist (condong ke atas); set 2000 bukan tapisan Shariah; data bermula 2010.
- "Lari" ialah label harga, bukan untung dagangan: untung sebenar bergantung pada cara pegang dan keluar (jadual kedua) dan pada berapa isyarat yang sempat diambil portfolio.
