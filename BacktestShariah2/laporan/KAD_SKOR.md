# Kad skor keputusan (satu jawapan)

Dijana 2026-11-24 oleh `standard/kad_skor.py` (Actions `analisis.yml`). Gate: `standard/SPEC_KAD_SKOR.md` (pradaftar 2026-11-06; pindaan 2026-11-07). Rekod analisis sahaja: tiada order, tiada wang sebenar.

## Tiada kaedah lulus. Kematangan paling awal ~2027-03-24 dan ≥ 10 hari beli dalam setiap rejim (kini ON 1, OFF 26; bergantung pasaran); portfolio lawan SPUS pada MDD -10% ~2027-04-09

**Tindakan hari ini:** JANGAN guna wang sebenar: tiada kaedah TERBUKTI. Papertrade C dan Lejar terus mengumpul data. Rejim OFF sejak 2026-10-16 (27 sesi): saham momentum paling terjejas dalam fasa ini; data hari ini dikira dalam baldi OFF.

Penyebut: **46,659 posisi LANGSUNG** Lejar Penuh lorong 1 merentas 227 kaedah, 27 hari beli (rejim ON 1, OFF 26); 36,200 posisi isian bina semula dan 98 posisi dengan data harga dikuarantin tidak dikira (Mxx sejak isyarat 2026-10-15, Nxx/GB sejak 2026-11-03). Harga pada tutup 2026-11-23.

| Status | Bilangan |
|---|---|
| NEGATIF | 0 |
| GAGAL | 1 |
| BELUM CUKUP | 226 |
| CALON | 0 |
| TERBUKTI | 0 |

## Bila keputusan boleh dibuat

- **G1 kematangan:** ≥ 114 hari beli langsung (ada 27) **dan** ≥ 10 dalam rejim ON (ada 1) **dan** ≥ 10 dalam rejim OFF (ada 26). Rejim ON = QQQ > SMA50 dan SMA10 > SMA20. Paling awal ~2027-03-24 jika rejim ON muncul cukup lama; jika pasaran kekal OFF, G1 menunggu.
- **G6 portfolio:** 126 sesi lorong T4 (paling lama 27); ~2027-04-09. Dibanding dengan SPUS **pada MDD -10%** (toleransi anda), bukan pada MDD SPUS penuh.

## 20 kaedah teratas ikut lift masuk (calon, BUKAN pangkat sehingga status berubah)

| Kaedah | Status | Posisi / tutup | Hari beli (ON/OFF) | Jangkaan % | Jika henti tergelincir % | Buku harian % [95%] | Lift masuk | Menang % | Payoff | tanpa5 | Hari-0 | T4 sesi | T4 pada MDD -10% vs SPUS |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `M133` Bull Hook (Crabel) | BELUM CUKUP | 54 / 45 | 16 (1/15) | -0.77 | -1.06 | +0.519 [-0.605, +1.644] | +3.90 | 35 | 1.35 | -1.89 | 1 | 27 | +2.32 vs -6.81 |
| `M146` 3-Bar Momentum Pattern | BELUM CUKUP | 80 / 47 | 20 (1/19) | -0.17 | -0.62 | +0.143 [-0.282, +0.569] | +2.60 | 39 | 1.50 | -1.32 | 4 | 27 | +4.47 vs -6.81 |
| `M46` Jurang Naik Boleh Beli (Buya | BELUM CUKUP | 36 / 27 | 13 (1/12) | -1.99 | -2.72 | -0.069 [-0.479, +0.342] | +2.41 | 25 | 1.42 | -3.30 | 13 | 27 | +1.18 vs -6.81 |
| `M117` Landry Pullback (high 2 bula | BELUM CUKUP | 162 / 42 | 21 (1/20) | -1.66 | -1.80 | +0.024 [-0.336, +0.384] | +2.40 | 30 | 1.41 | -3.44 | 1 | 27 | -6.11 vs -6.81 |
| `M93` Bollinger Kaedah II: %b + MF | BELUM CUKUP | 273 / 119 | 25 (1/24) | -1.37 | -1.68 | -0.005 [-0.388, +0.378] | +1.86 | 37 | 1.21 | -3.15 | 4 | 27 | -1.47 vs -6.81 |
| `M15` Break & Retest + Henti ATR | BELUM CUKUP | 324 / 293 | 26 (1/25) | -0.89 | -1.09 | -0.066 [-0.477, +0.346] | +1.76 | 32 | 1.52 | -2.25 | 6 | 27 | -6.12 vs -6.81 |
| `M80` Radge Saluran Purata Bergera | BELUM CUKUP | 313 / 121 | 26 (1/25) | -2.07 | -2.40 | -0.015 [-0.424, +0.395] | +1.75 | 37 | 1.00 | -3.37 | 0 | 27 | -3.56 vs -6.81 |
| `M18` EMA9/21 Pullback | BELUM CUKUP | 480 / 433 | 27 (1/26) | -0.92 | -1.30 | -0.075 [-0.450, +0.299] | +1.73 | 24 | 1.99 | -1.90 | 117 | 27 | -7.38 vs -6.81 |
| `M150` Trend Bar Failure (Brooks) | BELUM CUKUP | 111 / 95 | 22 (1/21) | -1.68 | -1.83 | -0.119 [-0.436, +0.198] | +1.68 | 27 | 1.25 | -2.58 | 0 | 27 | -6.81 vs -6.81 |
| `M158` Doubly Adaptive Profit Targe | BELUM CUKUP | 391 / 216 | 24 (1/23) | -1.16 | -1.30 | +0.056 [-0.409, +0.521] | +1.48 | 34 | 1.43 | -2.60 | 3 | 27 | -3.71 vs -6.81 |
| `M137` Livermore System | BELUM CUKUP | 184 / 97 | 25 (1/24) | -2.51 | -2.92 | -0.052 [-0.474, +0.370] | +1.15 | 32 | 1.09 | -3.88 | 4 | 27 | +4.01 vs -6.81 |
| `M25` VWAP Wave (proksi harian) | BELUM CUKUP | 201 / 173 | 25 (1/24) | -1.21 | -1.63 | +0.030 [-0.442, +0.502] | +1.13 | 26 | 1.70 | -2.44 | 30 | 27 | +3.18 vs -6.81 |
| `M145` Yum-Yum Continuation | BELUM CUKUP | 312 / 109 | 24 (1/23) | -2.86 | -3.18 | -0.080 [-0.469, +0.309] | +1.11 | 37 | 0.88 | -4.24 | 0 | 27 | +2.62 vs -6.81 |
| `M161` EMA 10/21 + Supertrend (10,3 | BELUM CUKUP | 524 / 379 | 27 (1/26) | -2.15 | -2.24 | -0.137 [-0.495, +0.221] | +1.08 | 32 | 1.17 | -3.66 | 2 | 27 | -8.47 vs -6.81 |
| `M127` Slingshot Bullish | BELUM CUKUP | 112 / 92 | 20 (1/19) | -2.21 | -2.71 | -0.200 [-0.560, +0.159] | +1.06 | 17 | 1.34 | -2.97 | 24 | 27 | -5.99 vs -6.81 |
| `M77` Undercut & Rally pada Purata | BELUM CUKUP | 56 / 44 | 19 (1/18) | -1.24 | -1.59 | -0.144 [-0.608, +0.321] | +0.94 | 27 | 1.59 | -2.30 | 11 | 27 | -2.65 vs -6.81 |
| `M119` 180 Bullish (Cooper) | BELUM CUKUP | 168 / 107 | 24 (1/23) | -2.44 | -2.99 | -0.168 [-0.522, +0.186] | +0.78 | 24 | 1.28 | -3.56 | 11 | 27 | -6.01 vs -6.81 |
| `M01` Bollinger Band + RSI | BELUM CUKUP | 139 / 27 | 24 (1/23) | -1.94 | -1.94 | -0.336 [-1.089, +0.416] | +0.76 | 37 | 1.12 | -3.33 | 0 | 27 | -7.32 vs -6.81 |
| `M35` Pocket Pivot Morales & Kache | BELUM CUKUP | 337 / 310 | 26 (1/25) | -0.75 | -1.19 | -0.064 [-0.418, +0.290] | +0.72 | 26 | 2.07 | -1.87 | 79 | 27 | -4.00 vs -6.81 |
| `M153` Range Leader | BELUM CUKUP | 1447 / 1414 | 27 (1/26) | -0.62 | -0.67 | -0.121 [-0.560, +0.319] | +0.70 | 41 | 1.10 | -1.58 | 9 | 27 | -3.61 vs -6.81 |

## Cara membaca

- **Satu status sahaja yang bermakna untuk wang sebenar: TERBUKTI.**
- **Lift masuk** = adakah kaedah memilih saham lebih baik daripada saham lain yang Lejar beli pada hari sama dan tahap turun-naik sama, diukur 10 sesi (bebas peraturan keluar). Disahkan plasebo: `laporan/PLASEBO_GATE.md`.
- **Buku harian** = pulangan harian purata jika setiap isyarat kaedah itu diberi modal sama dan keluar ikut peraturannya sendiri. Selang 95% Newey-West mengambil kira bahawa semua posisi bergerak bersama pasaran.
- **Jika henti tergelincir** = jangkaan jika setiap keluar henti intrahari diisi pada titik tengah antara paras henti dan harga rendah hari itu (Lejar mengandaikan isian tepat pada henti; rendah hari itu di bawah henti pada ~95% kes). Maklumat sahaja: anggaran kos realistik pelaksanaan, bukan gate.
- Menang % sentiasa dibaca bersama payoff: `X10` menang 94.1% dengan jangkaan negatif.
- `tanpa5` = jangkaan selepas membuang 5% posisi terbaik. Negatif bermaksud kelebihan hidup dalam ekor kanan.
- Jangan ubah ambang gate selepas melihat data. Ia dikunci oleh ujian unit.

