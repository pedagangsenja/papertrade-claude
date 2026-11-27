# Kad skor keputusan (satu jawapan)

Dijana 2026-11-27 oleh `standard/kad_skor.py` (Actions `analisis.yml`). Gate: `standard/SPEC_KAD_SKOR.md` (pradaftar 2026-11-06; pindaan 2026-11-07). Rekod analisis sahaja: tiada order, tiada wang sebenar.

## Tiada kaedah lulus. Kematangan paling awal ~2027-04-01 dan ≥ 10 hari beli dalam setiap rejim (kini ON 1, OFF 28; bergantung pasaran); portfolio lawan SPUS pada MDD -10% ~2027-04-09

**Tindakan hari ini:** JANGAN guna wang sebenar: tiada kaedah TERBUKTI. Papertrade C dan Lejar terus mengumpul data. Rejim OFF sejak 2026-10-16 (29 sesi): saham momentum paling terjejas dalam fasa ini; data hari ini dikira dalam baldi OFF.

Penyebut: **50,403 posisi LANGSUNG** Lejar Penuh lorong 1 merentas 227 kaedah, 29 hari beli (rejim ON 1, OFF 28); 36,194 posisi isian bina semula dan 98 posisi dengan data harga dikuarantin tidak dikira (Mxx sejak isyarat 2026-10-15, Nxx/GB sejak 2026-11-03). Harga pada tutup 2026-11-25.

| Status | Bilangan |
|---|---|
| NEGATIF | 0 |
| GAGAL | 2 |
| BELUM CUKUP | 225 |
| CALON | 0 |
| TERBUKTI | 0 |

## Bila keputusan boleh dibuat

- **G1 kematangan:** ≥ 120 hari beli langsung (ada 29) **dan** ≥ 10 dalam rejim ON (ada 1) **dan** ≥ 10 dalam rejim OFF (ada 28). Rejim ON = QQQ > SMA50 dan SMA10 > SMA20. Paling awal ~2027-04-01 jika rejim ON muncul cukup lama; jika pasaran kekal OFF, G1 menunggu.
- **G6 portfolio:** 126 sesi lorong T4 (paling lama 29); ~2027-04-09. Dibanding dengan SPUS **pada MDD -10%** (toleransi anda), bukan pada MDD SPUS penuh.

## 20 kaedah teratas ikut lift masuk (calon, BUKAN pangkat sehingga status berubah)

| Kaedah | Status | Posisi / tutup | Hari beli (ON/OFF) | Jangkaan % | Jika henti tergelincir % | Buku harian % [95%] | Lift masuk | Menang % | Payoff | tanpa5 | Hari-0 | T4 sesi | T4 pada MDD -10% vs SPUS |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `M133` Bull Hook (Crabel) | BELUM CUKUP | 54 / 45 | 16 (1/15) | -0.72 | -1.01 | +0.507 [-0.549, +1.562] | +3.73 | 37 | 1.28 | -1.88 | 1 | 29 | +3.52 vs -9.54 |
| `M146` 3-Bar Momentum Pattern | BELUM CUKUP | 81 / 48 | 21 (1/20) | +1.05 | +0.58 | +0.227 [-0.202, +0.656] | +2.68 | 42 | 1.80 | -0.74 | 4 | 29 | +7.12 vs -9.54 |
| `M117` Landry Pullback (high 2 bula | BELUM CUKUP | 168 / 45 | 23 (1/22) | -0.36 | -0.50 | +0.079 [-0.264, +0.422] | +2.06 | 42 | 1.24 | -2.17 | 1 | 29 | -6.28 vs -9.54 |
| `M93` Bollinger Kaedah II: %b + MF | BELUM CUKUP | 276 / 124 | 26 (1/25) | -0.15 | -0.47 | +0.066 [-0.318, +0.449] | +1.82 | 43 | 1.30 | -2.08 | 4 | 29 | -0.44 vs -9.54 |
| `M80` Radge Saluran Purata Bergera | BELUM CUKUP | 317 / 130 | 28 (1/27) | -0.82 | -1.15 | +0.053 [-0.351, +0.458] | +1.70 | 45 | 1.03 | -2.35 | 0 | 29 | -2.22 vs -9.54 |
| `M18` EMA9/21 Pullback | BELUM CUKUP | 501 / 447 | 29 (1/28) | -0.64 | -1.02 | -0.011 [-0.382, +0.359] | +1.61 | 26 | 2.11 | -1.69 | 120 | 29 | -5.23 vs -9.54 |
| `M150` Trend Bar Failure (Brooks) | BELUM CUKUP | 120 / 96 | 24 (1/23) | -1.26 | -1.40 | -0.045 [-0.372, +0.281] | +1.60 | 32 | 1.18 | -2.11 | 0 | 29 | -5.82 vs -9.54 |
| `M15` Break & Retest + Henti ATR | BELUM CUKUP | 334 / 295 | 28 (1/27) | -0.60 | -0.79 | +0.009 [-0.409, +0.427] | +1.58 | 34 | 1.61 | -2.09 | 6 | 29 | -6.01 vs -9.54 |
| `M158` Doubly Adaptive Profit Targe | BELUM CUKUP | 395 / 220 | 26 (1/25) | -0.18 | -0.33 | +0.121 [-0.330, +0.572] | +1.44 | 39 | 1.51 | -1.75 | 3 | 29 | -2.55 vs -9.54 |
| `M118` Expansion Pivot (Cooper) | BELUM CUKUP | 87 / 46 | 21 (1/20) | -0.83 | -0.99 | +0.076 [-0.296, +0.449] | +1.40 | 38 | 1.32 | -2.28 | 1 | 29 | +6.35 vs -9.54 |
| `M25` VWAP Wave (proksi harian) | BELUM CUKUP | 201 / 176 | 25 (1/24) | -0.81 | -1.24 | +0.123 [-0.351, +0.598] | +1.19 | 28 | 1.89 | -2.19 | 30 | 29 | +3.93 vs -9.54 |
| `M127` Slingshot Bullish | BELUM CUKUP | 112 / 92 | 20 (1/19) | -1.78 | -2.29 | -0.108 [-0.516, +0.301] | +1.09 | 16 | 2.16 | -2.68 | 24 | 29 | -4.92 vs -9.54 |
| `M107` Golden Cross SMA50/200 | BELUM CUKUP | 47 / 14 | 22 (1/21) | -1.29 | -1.65 | -0.017 [-0.472, +0.437] | +1.04 | 51 | 0.67 | -2.40 | 0 | 29 | -3.13 vs -9.54 |
| `M119` 180 Bullish (Cooper) | BELUM CUKUP | 193 / 111 | 25 (1/24) | -1.49 | -1.98 | -0.101 [-0.459, +0.257] | +0.98 | 35 | 1.10 | -2.60 | 12 | 29 | -5.12 vs -9.54 |
| `M137` Livermore System | BELUM CUKUP | 187 / 101 | 27 (1/26) | -1.49 | -1.90 | +0.019 [-0.404, +0.443] | +0.94 | 38 | 1.15 | -2.95 | 4 | 29 | +6.71 vs -9.54 |
| `M100` Bulkowski Segi Empat & Segi  | BELUM CUKUP | 64 / 45 | 18 (1/17) | -0.63 | -0.91 | -0.004 [-0.423, +0.416] | +0.92 | 44 | 1.07 | -1.46 | 0 | 29 | +0.52 vs -9.54 |
| `M77` Undercut & Rally pada Purata | BELUM CUKUP | 63 / 48 | 21 (1/20) | -0.99 | -1.37 | -0.119 [-0.554, +0.315] | +0.91 | 24 | 2.15 | -2.39 | 12 | 29 | -4.35 vs -9.54 |
| `M161` EMA 10/21 + Supertrend (10,3 | BELUM CUKUP | 570 / 392 | 29 (1/28) | -1.36 | -1.44 | -0.060 [-0.428, +0.309] | +0.85 | 37 | 1.18 | -2.97 | 2 | 29 | -7.43 vs -9.54 |
| `M01` Bollinger Band + RSI | BELUM CUKUP | 140 / 29 | 25 (1/24) | -2.83 | -2.83 | -0.353 [-1.056, +0.351] | +0.81 | 37 | 0.94 | -4.25 | 0 | 29 | -8.46 vs -9.54 |
| `M31` Band Walk (BB 20/2) | BELUM CUKUP | 405 / 204 | 26 (1/25) | -1.45 | -1.45 | +0.008 [-0.383, +0.399] | +0.79 | 40 | 1.11 | -3.00 | 0 | 29 | -3.95 vs -9.54 |

## Cara membaca

- **Satu status sahaja yang bermakna untuk wang sebenar: TERBUKTI.**
- **Lift masuk** = adakah kaedah memilih saham lebih baik daripada saham lain yang Lejar beli pada hari sama dan tahap turun-naik sama, diukur 10 sesi (bebas peraturan keluar). Disahkan plasebo: `laporan/PLASEBO_GATE.md`.
- **Buku harian** = pulangan harian purata jika setiap isyarat kaedah itu diberi modal sama dan keluar ikut peraturannya sendiri. Selang 95% Newey-West mengambil kira bahawa semua posisi bergerak bersama pasaran.
- **Jika henti tergelincir** = jangkaan jika setiap keluar henti intrahari diisi pada titik tengah antara paras henti dan harga rendah hari itu (Lejar mengandaikan isian tepat pada henti; rendah hari itu di bawah henti pada ~95% kes). Maklumat sahaja: anggaran kos realistik pelaksanaan, bukan gate.
- Menang % sentiasa dibaca bersama payoff: `X10` menang 94.1% dengan jangkaan negatif.
- `tanpa5` = jangkaan selepas membuang 5% posisi terbaik. Negatif bermaksud kelebihan hidup dalam ekor kanan.
- Jangan ubah ambang gate selepas melihat data. Ia dikunci oleh ujian unit.

