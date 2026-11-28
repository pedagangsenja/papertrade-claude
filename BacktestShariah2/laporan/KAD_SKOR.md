# Kad skor keputusan (satu jawapan)

Dijana 2026-11-28 oleh `standard/kad_skor.py` (Actions `analisis.yml`). Gate: `standard/SPEC_KAD_SKOR.md` (pradaftar 2026-11-06; pindaan 2026-11-07). Rekod analisis sahaja: tiada order, tiada wang sebenar.

## Tiada kaedah lulus. Kematangan paling awal ~2027-03-31 dan ≥ 10 hari beli dalam setiap rejim (kini ON 1, OFF 29; bergantung pasaran); portfolio lawan SPUS pada MDD -10% ~2027-04-12

**Tindakan hari ini:** JANGAN guna wang sebenar: tiada kaedah TERBUKTI. Papertrade C dan Lejar terus mengumpul data. Rejim OFF sejak 2026-10-16 (30 sesi): saham momentum paling terjejas dalam fasa ini; data hari ini dikira dalam baldi OFF.

Penyebut: **52,559 posisi LANGSUNG** Lejar Penuh lorong 1 merentas 227 kaedah, 30 hari beli (rejim ON 1, OFF 29); 36,194 posisi isian bina semula dan 98 posisi dengan data harga dikuarantin tidak dikira (Mxx sejak isyarat 2026-10-15, Nxx/GB sejak 2026-11-03). Harga pada tutup 2026-11-27.

| Status | Bilangan |
|---|---|
| NEGATIF | 0 |
| GAGAL | 4 |
| BELUM CUKUP | 223 |
| CALON | 0 |
| TERBUKTI | 0 |

## Bila keputusan boleh dibuat

- **G1 kematangan:** ≥ 118 hari beli langsung (ada 30) **dan** ≥ 10 dalam rejim ON (ada 1) **dan** ≥ 10 dalam rejim OFF (ada 29). Rejim ON = QQQ > SMA50 dan SMA10 > SMA20. Paling awal ~2027-03-31 jika rejim ON muncul cukup lama; jika pasaran kekal OFF, G1 menunggu.
- **G6 portfolio:** 126 sesi lorong T4 (paling lama 30); ~2027-04-12. Dibanding dengan SPUS **pada MDD -10%** (toleransi anda), bukan pada MDD SPUS penuh.

## 20 kaedah teratas ikut lift masuk (calon, BUKAN pangkat sehingga status berubah)

| Kaedah | Status | Posisi / tutup | Hari beli (ON/OFF) | Jangkaan % | Jika henti tergelincir % | Buku harian % [95%] | Lift masuk | Menang % | Payoff | tanpa5 | Hari-0 | T4 sesi | T4 pada MDD -10% vs SPUS |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `M133` Bull Hook (Crabel) | BELUM CUKUP | 55 / 45 | 17 (1/16) | -0.51 | -0.80 | +0.524 [-0.498, +1.546] | +3.57 | 42 | 1.14 | -1.69 | 1 | 30 | +3.88 vs -7.49 |
| `M146` 3-Bar Momentum Pattern | BELUM CUKUP | 84 / 50 | 22 (1/21) | +1.46 | +1.00 | +0.251 [-0.183, +0.685] | +2.68 | 44 | 1.82 | -0.30 | 4 | 30 | +8.30 vs -7.49 |
| `M117` Landry Pullback (high 2 bula | BELUM CUKUP | 168 / 45 | 23 (1/22) | +0.41 | +0.27 | +0.111 [-0.241, +0.462] | +2.07 | 45 | 1.35 | -1.49 | 1 | 30 | -5.50 vs -7.49 |
| `M93` Bollinger Kaedah II: %b + MF | BELUM CUKUP | 277 / 126 | 27 (1/26) | +0.50 | +0.18 | +0.100 [-0.300, +0.499] | +1.85 | 46 | 1.29 | -1.47 | 4 | 30 | +2.36 vs -7.49 |
| `M80` Radge Saluran Purata Bergera | BELUM CUKUP | 317 / 131 | 28 (1/27) | -0.16 | -0.49 | +0.086 [-0.331, +0.503] | +1.67 | 49 | 1.02 | -1.74 | 0 | 30 | -1.17 vs -7.49 |
| `M18` EMA9/21 Pullback | BELUM CUKUP | 547 / 450 | 30 (1/29) | -0.45 | -0.80 | +0.014 [-0.363, +0.390] | +1.62 | 29 | 1.96 | -1.46 | 121 | 30 | -4.40 vs -7.49 |
| `M150` Trend Bar Failure (Brooks) | BELUM CUKUP | 120 / 97 | 24 (1/23) | -1.07 | -1.21 | -0.013 [-0.358, +0.331] | +1.60 | 32 | 1.31 | -1.92 | 0 | 30 | -4.92 vs -7.49 |
| `M15` Break & Retest + Henti ATR | BELUM CUKUP | 340 / 297 | 29 (1/28) | -0.45 | -0.63 | +0.043 [-0.389, +0.474] | +1.56 | 35 | 1.62 | -1.96 | 6 | 30 | -5.03 vs -7.49 |
| `M158` Doubly Adaptive Profit Targe | BELUM CUKUP | 399 / 225 | 27 (1/26) | +0.28 | +0.13 | +0.149 [-0.306, +0.604] | +1.47 | 40 | 1.58 | -1.34 | 3 | 30 | +0.97 vs -7.49 |
| `M118` Expansion Pivot (Cooper) | BELUM CUKUP | 97 / 47 | 22 (1/21) | -0.14 | -0.29 | +0.111 [-0.274, +0.495] | +1.40 | 43 | 1.26 | -1.52 | 1 | 30 | +6.76 vs -7.49 |
| `M25` VWAP Wave (proksi harian) | BELUM CUKUP | 209 / 176 | 26 (1/25) | -0.60 | -1.01 | +0.157 [-0.328, +0.641] | +1.21 | 31 | 1.80 | -1.96 | 30 | 30 | +5.60 vs -7.49 |
| `M127` Slingshot Bullish | BELUM CUKUP | 112 / 92 | 20 (1/19) | -1.58 | -2.09 | -0.070 [-0.504, +0.364] | +1.06 | 18 | 2.20 | -2.53 | 24 | 30 | -4.51 vs -7.49 |
| `M107` Golden Cross SMA50/200 | BELUM CUKUP | 47 / 14 | 22 (1/21) | -0.46 | -0.82 | +0.021 [-0.453, +0.495] | +0.98 | 57 | 0.66 | -1.58 | 0 | 30 | -2.48 vs -7.49 |
| `M119` 180 Bullish (Cooper) | BELUM CUKUP | 195 / 113 | 26 (1/25) | -0.97 | -1.45 | -0.060 [-0.442, +0.322] | +0.98 | 39 | 1.14 | -2.15 | 12 | 30 | -4.14 vs -7.49 |
| `M137` Livermore System | BELUM CUKUP | 191 / 102 | 28 (1/27) | -0.95 | -1.35 | +0.052 [-0.383, +0.488] | +0.94 | 40 | 1.21 | -2.42 | 4 | 30 | +8.02 vs -7.49 |
| `M100` Bulkowski Segi Empat & Segi  | BELUM CUKUP | 66 / 45 | 19 (1/18) | -0.35 | -0.62 | +0.025 [-0.397, +0.447] | +0.92 | 48 | 0.96 | -1.14 | 0 | 30 | +1.84 vs -7.49 |
| `M77` Undercut & Rally pada Purata | BELUM CUKUP | 64 / 50 | 22 (1/21) | -0.72 | -1.11 | -0.083 [-0.521, +0.354] | +0.91 | 27 | 2.11 | -2.23 | 12 | 30 | -3.12 vs -7.49 |
| `M161` EMA 10/21 + Supertrend (10,3 | BELUM CUKUP | 592 / 397 | 30 (1/29) | -0.90 | -0.98 | -0.020 [-0.413, +0.373] | +0.85 | 40 | 1.19 | -2.58 | 2 | 30 | -6.97 vs -7.49 |
| `M01` Bollinger Band + RSI | BELUM CUKUP | 140 / 33 | 25 (1/24) | -0.96 | -0.96 | -0.257 [-0.970, +0.457] | +0.81 | 49 | 0.86 | -2.29 | 0 | 30 | -7.48 vs -7.49 |
| `M31` Band Walk (BB 20/2) | BELUM CUKUP | 405 / 209 | 26 (1/25) | -0.86 | -0.86 | +0.044 [-0.364, +0.453] | +0.79 | 43 | 1.11 | -2.47 | 0 | 30 | -3.14 vs -7.49 |

## Cara membaca

- **Satu status sahaja yang bermakna untuk wang sebenar: TERBUKTI.**
- **Lift masuk** = adakah kaedah memilih saham lebih baik daripada saham lain yang Lejar beli pada hari sama dan tahap turun-naik sama, diukur 10 sesi (bebas peraturan keluar). Disahkan plasebo: `laporan/PLASEBO_GATE.md`.
- **Buku harian** = pulangan harian purata jika setiap isyarat kaedah itu diberi modal sama dan keluar ikut peraturannya sendiri. Selang 95% Newey-West mengambil kira bahawa semua posisi bergerak bersama pasaran.
- **Jika henti tergelincir** = jangkaan jika setiap keluar henti intrahari diisi pada titik tengah antara paras henti dan harga rendah hari itu (Lejar mengandaikan isian tepat pada henti; rendah hari itu di bawah henti pada ~95% kes). Maklumat sahaja: anggaran kos realistik pelaksanaan, bukan gate.
- Menang % sentiasa dibaca bersama payoff: `X10` menang 94.1% dengan jangkaan negatif.
- `tanpa5` = jangkaan selepas membuang 5% posisi terbaik. Negatif bermaksud kelebihan hidup dalam ekor kanan.
- Jangan ubah ambang gate selepas melihat data. Ia dikunci oleh ujian unit.

