# Kad skor keputusan (satu jawapan)

Dijana 2026-11-21 oleh `standard/kad_skor.py` (Actions `analisis.yml`). Gate: `standard/SPEC_KAD_SKOR.md` (pradaftar 2026-11-06; pindaan 2026-11-07). Rekod analisis sahaja: tiada order, tiada wang sebenar.

## Tiada kaedah lulus. Kematangan paling awal ~2027-03-15 dan ≥ 10 hari beli dalam setiap rejim (kini ON 1, OFF 25; bergantung pasaran); portfolio lawan SPUS pada MDD -10% ~2027-04-09

**Tindakan hari ini:** JANGAN guna wang sebenar: tiada kaedah TERBUKTI. Papertrade C dan Lejar terus mengumpul data. Rejim OFF sejak 2026-10-16 (26 sesi): saham momentum paling terjejas dalam fasa ini; data hari ini dikira dalam baldi OFF.

Penyebut: **45,885 posisi LANGSUNG** Lejar Penuh lorong 1 merentas 227 kaedah, 26 hari beli (rejim ON 1, OFF 25); 36,196 posisi isian bina semula dan 98 posisi dengan data harga dikuarantin tidak dikira (Mxx sejak isyarat 2026-10-15, Nxx/GB sejak 2026-11-03). Harga pada tutup 2026-11-20.

| Status | Bilangan |
|---|---|
| NEGATIF | 0 |
| GAGAL | 1 |
| BELUM CUKUP | 226 |
| CALON | 0 |
| TERBUKTI | 0 |

## Bila keputusan boleh dibuat

- **G1 kematangan:** ≥ 107 hari beli langsung (ada 26) **dan** ≥ 10 dalam rejim ON (ada 1) **dan** ≥ 10 dalam rejim OFF (ada 25). Rejim ON = QQQ > SMA50 dan SMA10 > SMA20. Paling awal ~2027-03-15 jika rejim ON muncul cukup lama; jika pasaran kekal OFF, G1 menunggu.
- **G6 portfolio:** 126 sesi lorong T4 (paling lama 26); ~2027-04-09. Dibanding dengan SPUS **pada MDD -10%** (toleransi anda), bukan pada MDD SPUS penuh.

## 20 kaedah teratas ikut lift masuk (calon, BUKAN pangkat sehingga status berubah)

| Kaedah | Status | Posisi / tutup | Hari beli (ON/OFF) | Jangkaan % | Jika henti tergelincir % | Buku harian % [95%] | Lift masuk | Menang % | Payoff | tanpa5 | Hari-0 | T4 sesi | T4 pada MDD -10% vs SPUS |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `M133` Bull Hook (Crabel) | BELUM CUKUP | 54 / 44 | 16 (1/15) | -1.34 | -1.63 | +0.419 [-0.777, +1.615] | +3.91 | 30 | 1.39 | -2.49 | 1 | 26 | +1.76 vs -9.51 |
| `M15` Break & Retest + Henti ATR | BELUM CUKUP | 324 / 271 | 26 (1/25) | -1.37 | -1.57 | -0.172 [-0.654, +0.310] | +2.08 | 32 | 1.28 | -2.58 | 6 | 26 | -7.68 vs -9.51 |
| `M150` Trend Bar Failure (Brooks) | BELUM CUKUP | 111 / 82 | 22 (1/21) | -2.24 | -2.39 | -0.204 [-0.599, +0.190] | +1.86 | 22 | 1.28 | -3.16 | 0 | 26 | -8.46 vs -9.51 |
| `M80` Radge Saluran Purata Bergera | BELUM CUKUP | 311 / 117 | 25 (1/24) | -3.72 | -4.04 | -0.114 [-0.607, +0.379] | +1.82 | 28 | 0.93 | -4.94 | 0 | 26 | -5.25 vs -9.51 |
| `M18` EMA9/21 Pullback | BELUM CUKUP | 477 / 421 | 26 (1/25) | -1.21 | -1.59 | -0.159 [-0.590, +0.272] | +1.71 | 20 | 2.08 | -2.13 | 117 | 26 | -10.00 vs -9.51 |
| `M158` Doubly Adaptive Profit Targe | BELUM CUKUP | 391 / 190 | 24 (1/23) | -2.40 | -2.54 | -0.032 [-0.563, +0.498] | +1.49 | 27 | 1.37 | -3.75 | 3 | 26 | -6.45 vs -9.51 |
| `M93` Bollinger Kaedah II: %b + MF | BELUM CUKUP | 272 / 113 | 24 (1/23) | -2.88 | -3.18 | -0.102 [-0.566, +0.362] | +1.47 | 31 | 1.10 | -4.55 | 4 | 26 | -4.29 vs -9.51 |
| `M10` EMA3 + CCI + MACD | BELUM CUKUP | 127 / 76 | 22 (1/21) | -4.13 | -4.72 | -0.212 [-0.817, +0.393] | +1.36 | 23 | 1.18 | -5.70 | 9 | 26 | +5.61 vs -9.51 |
| `M137` Livermore System | BELUM CUKUP | 183 / 95 | 24 (1/23) | -3.69 | -4.10 | -0.144 [-0.628, +0.339] | +1.16 | 21 | 1.28 | -4.94 | 4 | 26 | +2.09 vs -9.51 |
| `M25` VWAP Wave (proksi harian) | BELUM CUKUP | 200 / 164 | 24 (1/23) | -1.63 | -2.06 | -0.054 [-0.586, +0.479] | +1.13 | 21 | 1.82 | -2.75 | 30 | 26 | +0.75 vs -9.51 |
| `M145` Yum-Yum Continuation | BELUM CUKUP | 311 / 107 | 23 (1/22) | -4.49 | -4.81 | -0.177 [-0.641, +0.286] | +1.00 | 30 | 0.78 | -5.78 | 0 | 26 | +1.20 vs -9.51 |
| `M33` Supertrend + SMA10 | BELUM CUKUP | 224 / 109 | 23 (1/22) | -4.24 | -4.56 | -0.118 [-0.731, +0.494] | +0.92 | 30 | 0.76 | -5.60 | 1 | 26 | +3.47 vs -9.51 |
| `M01` Bollinger Band + RSI | BELUM CUKUP | 123 / 27 | 23 (1/22) | -5.78 | -5.78 | -0.517 [-1.407, +0.373] | +0.84 | 32 | 0.79 | -7.59 | 0 | 26 | -10.00 vs -9.51 |
| `M23` Breitstein Kapitulasi + Kesi | BELUM CUKUP | 130 / 100 | 23 (1/22) | -1.68 | -2.26 | -0.020 [-0.478, +0.437] | +0.83 | 15 | 1.95 | -2.49 | 48 | 26 | -3.22 vs -9.51 |
| `M161` EMA 10/21 + Supertrend (10,3 | BELUM CUKUP | 523 / 323 | 26 (1/25) | -3.04 | -3.13 | -0.228 [-0.656, +0.200] | +0.72 | 26 | 1.13 | -4.40 | 2 | 26 | -9.39 vs -9.51 |
| `M118` Expansion Pivot (Cooper) | BELUM CUKUP | 85 / 44 | 20 (1/19) | -3.03 | -3.19 | -0.085 [-0.560, +0.390] | +0.71 | 31 | 0.89 | -4.45 | 1 | 26 | +2.43 vs -9.51 |
| `M127` Slingshot Bullish | BELUM CUKUP | 112 / 92 | 20 (1/19) | -2.69 | -3.20 | -0.311 [-0.709, +0.086] | +0.69 | 9 | 1.72 | -3.39 | 24 | 26 | -7.51 vs -9.51 |
| `M155` Market Cycle Strategy | BELUM CUKUP | 779 / 564 | 26 (1/25) | -5.48 | -6.01 | -0.426 [-1.059, +0.207] | +0.66 | 23 | 1.00 | -7.05 | 14 | 26 | -7.64 vs -9.51 |
| `M82` Arthur Hill Rotasi Sasaran 1 | BELUM CUKUP | 604 / 266 | 26 (1/25) | -4.23 | -4.23 | -0.278 [-0.730, +0.173] | +0.62 | 31 | 0.94 | -5.60 | 0 | 26 | -6.03 vs -9.51 |
| `M35` Pocket Pivot Morales & Kache | BELUM CUKUP | 333 / 294 | 25 (1/24) | -0.97 | -1.42 | -0.125 [-0.542, +0.292] | +0.61 | 24 | 2.11 | -2.05 | 78 | 26 | -5.26 vs -9.51 |

## Cara membaca

- **Satu status sahaja yang bermakna untuk wang sebenar: TERBUKTI.**
- **Lift masuk** = adakah kaedah memilih saham lebih baik daripada saham lain yang Lejar beli pada hari sama dan tahap turun-naik sama, diukur 10 sesi (bebas peraturan keluar). Disahkan plasebo: `laporan/PLASEBO_GATE.md`.
- **Buku harian** = pulangan harian purata jika setiap isyarat kaedah itu diberi modal sama dan keluar ikut peraturannya sendiri. Selang 95% Newey-West mengambil kira bahawa semua posisi bergerak bersama pasaran.
- **Jika henti tergelincir** = jangkaan jika setiap keluar henti intrahari diisi pada titik tengah antara paras henti dan harga rendah hari itu (Lejar mengandaikan isian tepat pada henti; rendah hari itu di bawah henti pada ~95% kes). Maklumat sahaja: anggaran kos realistik pelaksanaan, bukan gate.
- Menang % sentiasa dibaca bersama payoff: `X10` menang 94.1% dengan jangkaan negatif.
- `tanpa5` = jangkaan selepas membuang 5% posisi terbaik. Negatif bermaksud kelebihan hidup dalam ekor kanan.
- Jangan ubah ambang gate selepas melihat data. Ia dikunci oleh ujian unit.

