# Kad skor keputusan (satu jawapan)

Dijana 2026-11-25 oleh `standard/kad_skor.py` (Actions `analisis.yml`). Gate: `standard/SPEC_KAD_SKOR.md` (pradaftar 2026-11-06; pindaan 2026-11-07). Rekod analisis sahaja: tiada order, tiada wang sebenar.

## Tiada kaedah lulus. Kematangan paling awal ~2027-04-06 dan ≥ 10 hari beli dalam setiap rejim (kini ON 1, OFF 27; bergantung pasaran); portfolio lawan SPUS pada MDD -10% ~2027-04-09

**Tindakan hari ini:** JANGAN guna wang sebenar: tiada kaedah TERBUKTI. Papertrade C dan Lejar terus mengumpul data. Rejim OFF sejak 2026-10-16 (28 sesi): saham momentum paling terjejas dalam fasa ini; data hari ini dikira dalam baldi OFF.

Penyebut: **48,464 posisi LANGSUNG** Lejar Penuh lorong 1 merentas 227 kaedah, 28 hari beli (rejim ON 1, OFF 27); 36,194 posisi isian bina semula dan 98 posisi dengan data harga dikuarantin tidak dikira (Mxx sejak isyarat 2026-10-15, Nxx/GB sejak 2026-11-03). Harga pada tutup 2026-11-24.

| Status | Bilangan |
|---|---|
| NEGATIF | 0 |
| GAGAL | 1 |
| BELUM CUKUP | 226 |
| CALON | 0 |
| TERBUKTI | 0 |

## Bila keputusan boleh dibuat

- **G1 kematangan:** ≥ 123 hari beli langsung (ada 28) **dan** ≥ 10 dalam rejim ON (ada 1) **dan** ≥ 10 dalam rejim OFF (ada 27). Rejim ON = QQQ > SMA50 dan SMA10 > SMA20. Paling awal ~2027-04-06 jika rejim ON muncul cukup lama; jika pasaran kekal OFF, G1 menunggu.
- **G6 portfolio:** 126 sesi lorong T4 (paling lama 28); ~2027-04-09. Dibanding dengan SPUS **pada MDD -10%** (toleransi anda), bukan pada MDD SPUS penuh.

## 20 kaedah teratas ikut lift masuk (calon, BUKAN pangkat sehingga status berubah)

| Kaedah | Status | Posisi / tutup | Hari beli (ON/OFF) | Jangkaan % | Jika henti tergelincir % | Buku harian % [95%] | Lift masuk | Menang % | Payoff | tanpa5 | Hari-0 | T4 sesi | T4 pada MDD -10% vs SPUS |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `M133` Bull Hook (Crabel) | BELUM CUKUP | 54 / 45 | 16 (1/15) | -0.78 | -1.08 | +0.512 [-0.584, +1.608] | +3.89 | 37 | 1.24 | -1.92 | 1 | 28 | +3.37 vs -8.36 |
| `M146` 3-Bar Momentum Pattern | BELUM CUKUP | 80 / 47 | 20 (1/19) | +0.57 | +0.12 | +0.197 [-0.226, +0.621] | +2.60 | 44 | 1.50 | -0.83 | 4 | 28 | +6.14 vs -8.36 |
| `M117` Landry Pullback (high 2 bula | BELUM CUKUP | 167 / 43 | 22 (1/21) | -0.79 | -0.92 | +0.062 [-0.286, +0.410] | +2.28 | 39 | 1.25 | -2.56 | 1 | 28 | -5.47 vs -8.36 |
| `M93` Bollinger Kaedah II: %b + MF | BELUM CUKUP | 273 / 122 | 25 (1/24) | -0.74 | -1.06 | +0.033 [-0.344, +0.409] | +1.87 | 40 | 1.26 | -2.58 | 4 | 28 | -0.98 vs -8.36 |
| `M80` Radge Saluran Purata Bergera | BELUM CUKUP | 315 / 126 | 27 (1/26) | -1.42 | -1.74 | +0.022 [-0.379, +0.423] | +1.82 | 40 | 1.06 | -2.88 | 0 | 28 | -3.09 vs -8.36 |
| `M18` EMA9/21 Pullback | BELUM CUKUP | 494 / 435 | 28 (1/27) | -0.77 | -1.14 | -0.041 [-0.408, +0.326] | +1.70 | 26 | 1.94 | -1.76 | 118 | 28 | -6.63 vs -8.36 |
| `M15` Break & Retest + Henti ATR | BELUM CUKUP | 331 / 294 | 27 (1/26) | -0.74 | -0.93 | -0.025 [-0.435, +0.384] | +1.69 | 33 | 1.60 | -2.19 | 6 | 28 | -6.18 vs -8.36 |
| `M150` Trend Bar Failure (Brooks) | BELUM CUKUP | 116 / 96 | 23 (1/22) | -1.39 | -1.54 | -0.062 [-0.388, +0.264] | +1.68 | 30 | 1.24 | -2.26 | 0 | 28 | -5.75 vs -8.36 |
| `M118` Expansion Pivot (Cooper) | BELUM CUKUP | 85 / 46 | 20 (1/19) | -1.17 | -1.33 | +0.057 [-0.319, +0.432] | +1.49 | 36 | 1.28 | -2.69 | 1 | 28 | +5.48 vs -8.36 |
| `M158` Doubly Adaptive Profit Targe | BELUM CUKUP | 393 / 218 | 25 (1/24) | -0.63 | -0.77 | +0.093 [-0.359, +0.544] | +1.44 | 36 | 1.48 | -2.14 | 3 | 28 | -3.48 vs -8.36 |
| `M25` VWAP Wave (proksi harian) | BELUM CUKUP | 201 / 174 | 25 (1/24) | -0.98 | -1.40 | +0.087 [-0.381, +0.554] | +1.17 | 28 | 1.74 | -2.27 | 30 | 28 | +3.93 vs -8.36 |
| `M127` Slingshot Bullish | BELUM CUKUP | 112 / 92 | 20 (1/19) | -2.02 | -2.52 | -0.157 [-0.531, +0.218] | +1.07 | 18 | 1.55 | -2.82 | 24 | 28 | -5.58 vs -8.36 |
| `M119` 180 Bullish (Cooper) | BELUM CUKUP | 168 / 109 | 24 (1/23) | -2.15 | -2.70 | -0.136 [-0.484, +0.212] | +0.99 | 27 | 1.23 | -3.30 | 11 | 28 | -5.33 vs -8.36 |
| `M145` Yum-Yum Continuation | BELUM CUKUP | 313 / 109 | 25 (1/24) | -2.02 | -2.35 | -0.036 [-0.423, +0.351] | +0.91 | 42 | 0.89 | -3.55 | 0 | 28 | +5.31 vs -8.36 |
| `M77` Undercut & Rally pada Purata | BELUM CUKUP | 61 / 45 | 20 (1/19) | -0.98 | -1.37 | -0.118 [-0.569, +0.332] | +0.91 | 26 | 1.84 | -2.25 | 12 | 28 | -2.79 vs -8.36 |
| `M161` EMA 10/21 + Supertrend (10,3 | BELUM CUKUP | 534 / 392 | 28 (1/27) | -1.79 | -1.89 | -0.097 [-0.452, +0.258] | +0.86 | 33 | 1.25 | -3.39 | 2 | 28 | -7.88 vs -8.36 |
| `M107` Golden Cross SMA50/200 | BELUM CUKUP | 47 / 13 | 22 (1/21) | -2.14 | -2.47 | -0.059 [-0.497, +0.380] | +0.78 | 47 | 0.57 | -3.19 | 0 | 28 | -4.57 vs -8.36 |
| `M01` Bollinger Band + RSI | BELUM CUKUP | 140 / 28 | 25 (1/24) | -3.60 | -3.60 | -0.402 [-1.138, +0.333] | +0.77 | 34 | 0.92 | -5.06 | 0 | 28 | -8.77 vs -8.36 |
| `M35` Pocket Pivot Morales & Kache | BELUM CUKUP | 350 / 315 | 27 (1/26) | -0.58 | -1.01 | -0.015 [-0.356, +0.327] | +0.76 | 28 | 2.06 | -1.72 | 81 | 28 | -2.61 vs -8.36 |
| `M137` Livermore System | BELUM CUKUP | 186 / 98 | 26 (1/25) | -1.87 | -2.28 | -0.006 [-0.427, +0.415] | +0.73 | 34 | 1.18 | -3.28 | 4 | 28 | +6.54 vs -8.36 |

## Cara membaca

- **Satu status sahaja yang bermakna untuk wang sebenar: TERBUKTI.**
- **Lift masuk** = adakah kaedah memilih saham lebih baik daripada saham lain yang Lejar beli pada hari sama dan tahap turun-naik sama, diukur 10 sesi (bebas peraturan keluar). Disahkan plasebo: `laporan/PLASEBO_GATE.md`.
- **Buku harian** = pulangan harian purata jika setiap isyarat kaedah itu diberi modal sama dan keluar ikut peraturannya sendiri. Selang 95% Newey-West mengambil kira bahawa semua posisi bergerak bersama pasaran.
- **Jika henti tergelincir** = jangkaan jika setiap keluar henti intrahari diisi pada titik tengah antara paras henti dan harga rendah hari itu (Lejar mengandaikan isian tepat pada henti; rendah hari itu di bawah henti pada ~95% kes). Maklumat sahaja: anggaran kos realistik pelaksanaan, bukan gate.
- Menang % sentiasa dibaca bersama payoff: `X10` menang 94.1% dengan jangkaan negatif.
- `tanpa5` = jangkaan selepas membuang 5% posisi terbaik. Negatif bermaksud kelebihan hidup dalam ekor kanan.
- Jangan ubah ambang gate selepas melihat data. Ia dikunci oleh ujian unit.

