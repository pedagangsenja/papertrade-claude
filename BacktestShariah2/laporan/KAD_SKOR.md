# Kad skor keputusan (satu jawapan)

Dijana 2026-11-14 oleh `standard/kad_skor.py` (Actions `analisis.yml`). Gate: `standard/SPEC_KAD_SKOR.md` (pradaftar 2026-11-06; pindaan 2026-11-07). Rekod analisis sahaja: tiada order, tiada wang sebenar.

## Tiada kaedah lulus. Kematangan paling awal ~2026-11-13 dan ≥ 10 hari beli dalam setiap rejim (kini ON 1, OFF 20; bergantung pasaran); portfolio lawan SPUS pada MDD -10% ~2027-04-09

**Tindakan hari ini:** JANGAN guna wang sebenar: tiada kaedah TERBUKTI. Papertrade C dan Lejar terus mengumpul data. Rejim OFF sejak 2026-10-16 (21 sesi): saham momentum paling terjejas dalam fasa ini; data hari ini dikira dalam baldi OFF.

Penyebut: **40,250 posisi LANGSUNG** Lejar Penuh lorong 1 merentas 226 kaedah, 21 hari beli (rejim ON 1, OFF 20); 36,202 posisi isian bina semula dan 55 posisi dengan data harga dikuarantin tidak dikira (Mxx sejak isyarat 2026-10-15, Nxx/GB sejak 2026-11-03). Harga pada tutup 2026-11-13.

| Status | Bilangan |
|---|---|
| NEGATIF | 0 |
| GAGAL | 0 |
| BELUM CUKUP | 226 |
| CALON | 0 |
| TERBUKTI | 0 |

## Bila keputusan boleh dibuat

- **G1 kematangan:** ≥ 20 hari beli langsung (ada 21) **dan** ≥ 10 dalam rejim ON (ada 1) **dan** ≥ 10 dalam rejim OFF (ada 20). Rejim ON = QQQ > SMA50 dan SMA10 > SMA20. Paling awal ~2026-11-13 jika rejim ON muncul cukup lama; jika pasaran kekal OFF, G1 menunggu.
- **G6 portfolio:** 126 sesi lorong T4 (paling lama 21); ~2027-04-09. Dibanding dengan SPUS **pada MDD -10%** (toleransi anda), bukan pada MDD SPUS penuh.

## 20 kaedah teratas ikut lift masuk (calon, BUKAN pangkat sehingga status berubah)

| Kaedah | Status | Posisi / tutup | Hari beli (ON/OFF) | Jangkaan % | Jika henti tergelincir % | Buku harian % [95%] | Lift masuk | Menang % | Payoff | tanpa5 | Hari-0 | T4 sesi | T4 pada MDD -10% vs SPUS |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `M01` Bollinger Band + RSI | BELUM CUKUP | 113 / 24 | 20 (1/19) | +2.40 | +2.40 | -0.115 [-0.962, +0.733] | – | 59 | 1.23 | +0.85 | 0 | 21 | -5.81 vs -5.15 |
| `M05` MACD Divergence + Pengesahan | BELUM CUKUP | 41 / 12 | 15 (1/14) | -0.77 | -1.04 | -0.036 [-0.335, +0.262] | – | 39 | 1.21 | -2.81 | 0 | 21 | +2.29 vs -5.15 |
| `M07` Qullamaggie Breakout | BELUM CUKUP | 1 / 1 | 1 (1/0) | -2.53 | -3.60 | -0.143 [-1.539, +1.253] | – | 0 | – | – | 0 | 21 | -0.25 vs -5.15 |
| `M100` Bulkowski Segi Empat & Segi  | BELUM CUKUP | 60 / 41 | 15 (1/14) | +0.08 | -0.13 | +0.090 [-0.293, +0.474] | – | 48 | 1.10 | -0.54 | 0 | 21 | +2.64 vs -5.15 |
| `M104` High Tight Flag / Power Play | BELUM CUKUP | 1 / 0 | 1 (0/1) | +20.61 | +20.61 | +3.247 [-0.011, +6.505] | – | 100 | – | – | 0 | 6 | +2.08 vs +1.18 |
| `M106` DMI Wilder | BELUM CUKUP | 129 / 72 | 19 (1/18) | -0.63 | -0.66 | +0.004 [-0.288, +0.297] | – | 36 | 1.36 | -1.75 | 0 | 21 | -1.29 vs -5.15 |
| `M107` Golden Cross SMA50/200 | BELUM CUKUP | 39 / 7 | 18 (1/17) | -0.90 | -1.18 | -0.006 [-0.440, +0.428] | – | 41 | 1.04 | -1.91 | 0 | 21 | -0.79 vs -5.15 |
| `M121` High 2 bull flag (Brooks) | BELUM CUKUP | 7 / 4 | 5 (0/5) | -9.37 | -9.60 | -1.051 [-2.536, +0.434] | – | 29 | 0.09 | -11.24 | 0 | 17 | -6.51 vs -4.25 |
| `M126` Hidden Smash Day (beli, Larr | BELUM CUKUP | 19 / 11 | 10 (0/10) | -4.06 | -4.32 | -0.244 [-0.762, +0.274] | – | 26 | 0.53 | -4.73 | 0 | 20 | -5.52 vs -4.46 |
| `M129` Wick Play | BELUM CUKUP | 26 / 10 | 10 (1/9) | -1.10 | -1.59 | +0.054 [-0.465, +0.574] | – | 38 | 1.31 | -3.69 | 0 | 21 | +4.33 vs -5.15 |
| `M130` 多方炮 (dua lilin hijau mengapi | BELUM CUKUP | 10 / 3 | 7 (0/7) | -3.80 | -3.89 | -0.074 [-0.731, +0.582] | – | 50 | 0.37 | -5.41 | 0 | 19 | -3.57 vs -4.12 |
| `M135` 3rd Watch | BELUM CUKUP | 15 / 3 | 9 (1/8) | -4.17 | -4.31 | -0.252 [-0.887, +0.383] | – | 27 | 0.42 | -4.86 | 0 | 21 | -5.15 vs -5.15 |
| `M138` 直升机空中加油 (Helikopter isi miny | BELUM CUKUP | 3 / 0 | 3 (0/3) | -3.38 | -3.38 | -0.261 [-0.635, +0.113] | – | 0 | – | -4.54 | 0 | 14 | -0.95 vs -4.82 |
| `M139` 均线首次粘合向上发散 (MA berhimpun kal | BELUM CUKUP | 86 / 24 | 21 (1/20) | -1.94 | -2.19 | -0.036 [-0.464, +0.391] | – | 36 | 1.10 | -3.27 | 0 | 21 | +0.38 vs -5.15 |
| `M141` First Thrust (Landry) | BELUM CUKUP | 26 / 11 | 8 (1/7) | -3.04 | -3.64 | -0.314 [-0.719, +0.091] | – | 38 | 0.49 | -4.08 | 0 | 21 | -5.31 vs -5.15 |
| `M142` Pecahan volum dari dasar (底部 | BELUM CUKUP | 54 / 5 | 16 (0/16) | +1.44 | +1.35 | +0.125 [-0.299, +0.548] | – | 63 | 1.14 | +0.51 | 0 | 19 | +3.70 vs -4.12 |
| `M143` 장대양봉 이후 눌림목 / 5일선 매매 (Undur  | BELUM CUKUP | 25 / 1 | 13 (0/13) | -1.48 | -1.48 | -0.400 [-1.326, +0.526] | – | 44 | 0.41 | -2.04 | 0 | 20 | -0.38 vs -4.46 |
| `M144` Screw Bar | BELUM CUKUP | 9 / 7 | 6 (0/6) | -1.79 | -1.79 | -0.372 [-1.954, +1.210] | – | 33 | 0.93 | -2.91 | 0 | 19 | -1.57 vs -4.12 |
| `M145` Yum-Yum Continuation | BELUM CUKUP | 308 / 65 | 21 (1/20) | -0.34 | -0.54 | +0.038 [-0.296, +0.372] | – | 49 | 0.95 | -1.63 | 0 | 21 | +4.92 vs -5.15 |
| `M150` Trend Bar Failure (Brooks) | BELUM CUKUP | 103 / 45 | 19 (1/18) | -0.02 | -0.10 | -0.012 [-0.267, +0.243] | – | 41 | 1.44 | -0.99 | 0 | 21 | -4.54 vs -5.15 |

## Cara membaca

- **Satu status sahaja yang bermakna untuk wang sebenar: TERBUKTI.**
- **Lift masuk** = adakah kaedah memilih saham lebih baik daripada saham lain yang Lejar beli pada hari sama dan tahap turun-naik sama, diukur 10 sesi (bebas peraturan keluar). Disahkan plasebo: `laporan/PLASEBO_GATE.md`.
- **Buku harian** = pulangan harian purata jika setiap isyarat kaedah itu diberi modal sama dan keluar ikut peraturannya sendiri. Selang 95% Newey-West mengambil kira bahawa semua posisi bergerak bersama pasaran.
- **Jika henti tergelincir** = jangkaan jika setiap keluar henti intrahari diisi pada titik tengah antara paras henti dan harga rendah hari itu (Lejar mengandaikan isian tepat pada henti; rendah hari itu di bawah henti pada ~95% kes). Maklumat sahaja: anggaran kos realistik pelaksanaan, bukan gate.
- Menang % sentiasa dibaca bersama payoff: `X10` menang 94.1% dengan jangkaan negatif.
- `tanpa5` = jangkaan selepas membuang 5% posisi terbaik. Negatif bermaksud kelebihan hidup dalam ekor kanan.
- Jangan ubah ambang gate selepas melihat data. Ia dikunci oleh ujian unit.

