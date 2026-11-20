# Kad skor keputusan (satu jawapan)

Dijana 2026-11-20 oleh `standard/kad_skor.py` (Actions `analisis.yml`). Gate: `standard/SPEC_KAD_SKOR.md` (pradaftar 2026-11-06; pindaan 2026-11-07). Rekod analisis sahaja: tiada order, tiada wang sebenar.

## Tiada kaedah lulus. Kematangan paling awal ~2026-11-19 dan ≥ 10 hari beli dalam setiap rejim (kini ON 1, OFF 24; bergantung pasaran); portfolio lawan SPUS pada MDD -10% ~2027-04-09

**Tindakan hari ini:** JANGAN guna wang sebenar: tiada kaedah TERBUKTI. Papertrade C dan Lejar terus mengumpul data. Rejim OFF sejak 2026-10-16 (25 sesi): saham momentum paling terjejas dalam fasa ini; data hari ini dikira dalam baldi OFF.

Penyebut: **45,100 posisi LANGSUNG** Lejar Penuh lorong 1 merentas 226 kaedah, 25 hari beli (rejim ON 1, OFF 24); 36,195 posisi isian bina semula dan 98 posisi dengan data harga dikuarantin tidak dikira (Mxx sejak isyarat 2026-10-15, Nxx/GB sejak 2026-11-03). Harga pada tutup 2026-11-19.

| Status | Bilangan |
|---|---|
| NEGATIF | 0 |
| GAGAL | 1 |
| BELUM CUKUP | 225 |
| CALON | 0 |
| TERBUKTI | 0 |

## Bila keputusan boleh dibuat

- **G1 kematangan:** ≥ 20 hari beli langsung (ada 25) **dan** ≥ 10 dalam rejim ON (ada 1) **dan** ≥ 10 dalam rejim OFF (ada 24). Rejim ON = QQQ > SMA50 dan SMA10 > SMA20. Paling awal ~2026-11-19 jika rejim ON muncul cukup lama; jika pasaran kekal OFF, G1 menunggu.
- **G6 portfolio:** 126 sesi lorong T4 (paling lama 25); ~2027-04-09. Dibanding dengan SPUS **pada MDD -10%** (toleransi anda), bukan pada MDD SPUS penuh.

## 20 kaedah teratas ikut lift masuk (calon, BUKAN pangkat sehingga status berubah)

| Kaedah | Status | Posisi / tutup | Hari beli (ON/OFF) | Jangkaan % | Jika henti tergelincir % | Buku harian % [95%] | Lift masuk | Menang % | Payoff | tanpa5 | Hari-0 | T4 sesi | T4 pada MDD -10% vs SPUS |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `M01` Bollinger Band + RSI | BELUM CUKUP | 119 / 26 | 22 (1/21) | -2.63 | -2.63 | -0.362 [-1.133, +0.410] | – | 37 | 1.01 | -4.11 | 0 | 25 | -10.00 vs -7.40 |
| `M05` MACD Divergence + Pengesahan | BELUM CUKUP | 42 / 13 | 16 (1/15) | -3.46 | -3.72 | -0.183 [-0.569, +0.201] | – | 21 | 1.44 | -5.60 | 0 | 25 | -0.88 vs -7.40 |
| `M07` Qullamaggie Breakout | BELUM CUKUP | 1 / 1 | 1 (1/0) | -2.53 | -3.60 | -0.143 [-1.539, +1.253] | – | 0 | – | – | 0 | 25 | -0.25 vs -7.40 |
| `M100` Bulkowski Segi Empat & Segi  | BELUM CUKUP | 61 / 43 | 17 (1/16) | -1.20 | -1.45 | -0.093 [-0.573, +0.386] | – | 41 | 1.04 | -2.12 | 0 | 25 | -2.39 vs -7.40 |
| `M104` High Tight Flag / Power Play | BELUM CUKUP | 1 / 0 | 1 (0/1) | +20.32 | +20.32 | +1.928 [-0.909, +4.764] | – | 100 | – | – | 0 | 10 | +2.05 vs -1.22 |
| `M106` DMI Wilder | BELUM CUKUP | 134 / 104 | 22 (1/21) | -2.35 | -2.39 | -0.193 [-0.646, +0.259] | – | 27 | 1.07 | -3.40 | 0 | 25 | -5.55 vs -7.40 |
| `M107` Golden Cross SMA50/200 | BELUM CUKUP | 47 / 10 | 22 (1/21) | -4.04 | -4.29 | -0.176 [-0.661, +0.308] | – | 17 | 1.00 | -5.10 | 0 | 25 | -7.32 vs -7.40 |
| `M121` High 2 bull flag (Brooks) | BELUM CUKUP | 6 / 3 | 4 (0/4) | -9.93 | -10.06 | -0.897 [-1.928, +0.134] | – | 17 | 0.10 | -12.15 | 0 | 21 | -5.86 vs -6.52 |
| `M126` Hidden Smash Day (beli, Larr | BELUM CUKUP | 21 / 10 | 12 (0/12) | -3.33 | -3.50 | -0.189 [-0.602, +0.224] | – | 33 | 0.45 | -4.34 | 0 | 24 | -5.73 vs -6.73 |
| `M129` Wick Play | BELUM CUKUP | 25 / 9 | 10 (1/9) | -2.96 | -3.33 | -0.074 [-0.585, +0.438] | – | 36 | 1.07 | -5.62 | 0 | 25 | +1.11 vs -7.40 |
| `M130` 多方炮 (dua lilin hijau mengapi | BELUM CUKUP | 12 / 4 | 8 (0/8) | -6.19 | -6.39 | -0.233 [-0.866, +0.400] | – | 8 | 1.89 | -8.15 | 0 | 23 | -7.16 vs -6.40 |
| `M135` 3rd Watch | BELUM CUKUP | 15 / 6 | 9 (1/8) | -10.62 | -10.82 | -0.558 [-1.286, +0.169] | – | 13 | 0.27 | -11.82 | 0 | 25 | -7.53 vs -7.40 |
| `M138` 直升机空中加油 (Helikopter isi miny | BELUM CUKUP | 4 / 0 | 4 (0/4) | -3.26 | -3.26 | -0.241 [-0.517, +0.035] | – | 0 | – | -3.83 | 0 | 18 | -1.22 vs -7.08 |
| `M139` 均线首次粘合向上发散 (MA berhimpun kal | BELUM CUKUP | 96 / 41 | 24 (1/23) | -4.52 | -4.80 | -0.208 [-0.705, +0.289] | – | 28 | 0.86 | -5.71 | 0 | 25 | -2.30 vs -7.40 |
| `M141` First Thrust (Landry) | BELUM CUKUP | 27 / 17 | 9 (1/8) | -8.48 | -9.17 | -0.728 [-1.604, +0.148] | – | 19 | 0.24 | -9.60 | 0 | 25 | -9.41 vs -7.40 |
| `M142` Pecahan volum dari dasar (底部 | BELUM CUKUP | 55 / 11 | 17 (0/17) | -3.29 | -3.53 | -0.129 [-0.732, +0.475] | – | 40 | 0.48 | -4.23 | 0 | 23 | -1.27 vs -6.40 |
| `M143` 장대양봉 이후 눌림목 / 5일선 매매 (Undur  | BELUM CUKUP | 29 / 3 | 15 (0/15) | -4.08 | -4.22 | -0.463 [-1.236, +0.311] | – | 31 | 0.25 | -4.78 | 0 | 24 | -1.81 vs -6.73 |
| `M144` Screw Bar | BELUM CUKUP | 10 / 7 | 7 (0/7) | -2.21 | -2.21 | -0.377 [-1.573, +0.819] | – | 30 | 1.03 | -3.90 | 0 | 23 | -2.14 vs -6.40 |
| `M145` Yum-Yum Continuation | BELUM CUKUP | 311 / 89 | 23 (1/22) | -3.53 | -3.79 | -0.131 [-0.560, +0.298] | – | 34 | 0.79 | -4.84 | 0 | 25 | +1.81 vs -7.40 |
| `M150` Trend Bar Failure (Brooks) | BELUM CUKUP | 111 / 71 | 22 (1/21) | -1.66 | -1.81 | -0.148 [-0.485, +0.190] | – | 23 | 1.53 | -2.63 | 0 | 25 | -6.91 vs -7.40 |

## Cara membaca

- **Satu status sahaja yang bermakna untuk wang sebenar: TERBUKTI.**
- **Lift masuk** = adakah kaedah memilih saham lebih baik daripada saham lain yang Lejar beli pada hari sama dan tahap turun-naik sama, diukur 10 sesi (bebas peraturan keluar). Disahkan plasebo: `laporan/PLASEBO_GATE.md`.
- **Buku harian** = pulangan harian purata jika setiap isyarat kaedah itu diberi modal sama dan keluar ikut peraturannya sendiri. Selang 95% Newey-West mengambil kira bahawa semua posisi bergerak bersama pasaran.
- **Jika henti tergelincir** = jangkaan jika setiap keluar henti intrahari diisi pada titik tengah antara paras henti dan harga rendah hari itu (Lejar mengandaikan isian tepat pada henti; rendah hari itu di bawah henti pada ~95% kes). Maklumat sahaja: anggaran kos realistik pelaksanaan, bukan gate.
- Menang % sentiasa dibaca bersama payoff: `X10` menang 94.1% dengan jangkaan negatif.
- `tanpa5` = jangkaan selepas membuang 5% posisi terbaik. Negatif bermaksud kelebihan hidup dalam ekor kanan.
- Jangan ubah ambang gate selepas melihat data. Ia dikunci oleh ujian unit.

