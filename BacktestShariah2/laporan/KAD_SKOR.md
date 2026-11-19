# Kad skor keputusan (satu jawapan)

Dijana 2026-11-19 oleh `standard/kad_skor.py` (Actions `analisis.yml`). Gate: `standard/SPEC_KAD_SKOR.md` (pradaftar 2026-11-06; pindaan 2026-11-07). Rekod analisis sahaja: tiada order, tiada wang sebenar.

## Tiada kaedah lulus. Kematangan paling awal ~2026-11-18 dan ≥ 10 hari beli dalam setiap rejim (kini ON 1, OFF 23; bergantung pasaran); portfolio lawan SPUS pada MDD -10% ~2027-04-09

**Tindakan hari ini:** JANGAN guna wang sebenar: tiada kaedah TERBUKTI. Papertrade C dan Lejar terus mengumpul data. Rejim OFF sejak 2026-10-16 (24 sesi): saham momentum paling terjejas dalam fasa ini; data hari ini dikira dalam baldi OFF.

Penyebut: **43,349 posisi LANGSUNG** Lejar Penuh lorong 1 merentas 226 kaedah, 24 hari beli (rejim ON 1, OFF 23); 36,195 posisi isian bina semula dan 98 posisi dengan data harga dikuarantin tidak dikira (Mxx sejak isyarat 2026-10-15, Nxx/GB sejak 2026-11-03). Harga pada tutup 2026-11-18.

| Status | Bilangan |
|---|---|
| NEGATIF | 0 |
| GAGAL | 1 |
| BELUM CUKUP | 225 |
| CALON | 0 |
| TERBUKTI | 0 |

## Bila keputusan boleh dibuat

- **G1 kematangan:** ≥ 20 hari beli langsung (ada 24) **dan** ≥ 10 dalam rejim ON (ada 1) **dan** ≥ 10 dalam rejim OFF (ada 23). Rejim ON = QQQ > SMA50 dan SMA10 > SMA20. Paling awal ~2026-11-18 jika rejim ON muncul cukup lama; jika pasaran kekal OFF, G1 menunggu.
- **G6 portfolio:** 126 sesi lorong T4 (paling lama 24); ~2027-04-09. Dibanding dengan SPUS **pada MDD -10%** (toleransi anda), bukan pada MDD SPUS penuh.

## 20 kaedah teratas ikut lift masuk (calon, BUKAN pangkat sehingga status berubah)

| Kaedah | Status | Posisi / tutup | Hari beli (ON/OFF) | Jangkaan % | Jika henti tergelincir % | Buku harian % [95%] | Lift masuk | Menang % | Payoff | tanpa5 | Hari-0 | T4 sesi | T4 pada MDD -10% vs SPUS |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `M01` Bollinger Band + RSI | BELUM CUKUP | 117 / 25 | 21 (1/20) | -1.07 | -1.07 | -0.289 [-1.042, +0.464] | – | 42 | 1.10 | -2.50 | 0 | 24 | -8.78 vs -7.78 |
| `M05` MACD Divergence + Pengesahan | BELUM CUKUP | 41 / 13 | 15 (1/14) | -1.93 | -2.20 | -0.098 [-0.413, +0.217] | – | 24 | 1.82 | -4.21 | 0 | 24 | +1.90 vs -7.78 |
| `M07` Qullamaggie Breakout | BELUM CUKUP | 1 / 1 | 1 (1/0) | -2.53 | -3.60 | -0.143 [-1.539, +1.253] | – | 0 | – | – | 0 | 24 | -0.25 vs -7.78 |
| `M100` Bulkowski Segi Empat & Segi  | BELUM CUKUP | 60 / 41 | 16 (1/15) | -0.38 | -0.60 | +0.010 [-0.384, +0.404] | – | 48 | 0.96 | -1.03 | 0 | 24 | +0.84 vs -7.78 |
| `M104` High Tight Flag / Power Play | BELUM CUKUP | 1 / 0 | 1 (0/1) | +23.01 | +23.01 | +2.384 [-0.368, +5.135] | – | 100 | – | – | 0 | 9 | +2.32 vs -1.63 |
| `M106` DMI Wilder | BELUM CUKUP | 133 / 101 | 21 (1/20) | -1.76 | -1.80 | -0.105 [-0.477, +0.267] | – | 28 | 1.36 | -2.90 | 0 | 24 | -3.20 vs -7.78 |
| `M107` Golden Cross SMA50/200 | BELUM CUKUP | 46 / 10 | 21 (1/20) | -1.93 | -2.19 | -0.071 [-0.489, +0.347] | – | 35 | 0.96 | -3.09 | 0 | 24 | -5.45 vs -7.78 |
| `M121` High 2 bull flag (Brooks) | BELUM CUKUP | 6 / 3 | 4 (0/4) | -9.32 | -9.45 | -0.881 [-1.974, +0.213] | – | 33 | 0.13 | -11.80 | 0 | 20 | -5.51 vs -6.91 |
| `M126` Hidden Smash Day (beli, Larr | BELUM CUKUP | 20 / 10 | 11 (0/11) | -2.75 | -2.93 | -0.140 [-0.588, +0.307] | – | 30 | 0.81 | -3.41 | 0 | 23 | -4.11 vs -7.11 |
| `M129` Wick Play | BELUM CUKUP | 25 / 9 | 10 (1/9) | -1.62 | -2.00 | +0.006 [-0.475, +0.486] | – | 36 | 1.36 | -4.37 | 0 | 24 | +2.62 vs -7.78 |
| `M130` 多方炮 (dua lilin hijau mengapi | BELUM CUKUP | 12 / 3 | 8 (0/8) | -4.81 | -4.89 | -0.160 [-0.798, +0.478] | – | 17 | 1.40 | -7.03 | 0 | 22 | -5.49 vs -6.78 |
| `M135` 3rd Watch | BELUM CUKUP | 15 / 6 | 9 (1/8) | -9.52 | -9.72 | -0.505 [-1.212, +0.203] | – | 27 | 0.21 | -10.78 | 0 | 24 | -6.01 vs -7.78 |
| `M138` 直升机空中加油 (Helikopter isi miny | BELUM CUKUP | 4 / 0 | 4 (0/4) | -2.15 | -2.15 | -0.189 [-0.490, +0.112] | – | 25 | 0.33 | -3.22 | 0 | 17 | -0.78 vs -7.46 |
| `M139` 均线首次粘合向上发散 (MA berhimpun kal | BELUM CUKUP | 91 / 38 | 23 (1/22) | -3.58 | -3.85 | -0.137 [-0.594, +0.319] | – | 36 | 0.74 | -4.81 | 0 | 24 | -0.70 vs -7.78 |
| `M141` First Thrust (Landry) | BELUM CUKUP | 26 / 16 | 8 (1/7) | -7.72 | -8.43 | -0.652 [-1.471, +0.166] | – | 27 | 0.29 | -9.00 | 0 | 24 | -9.33 vs -7.78 |
| `M142` Pecahan volum dari dasar (底部 | BELUM CUKUP | 55 / 9 | 17 (0/17) | -1.22 | -1.41 | -0.024 [-0.538, +0.490] | – | 53 | 0.61 | -2.15 | 0 | 22 | +2.04 vs -6.78 |
| `M143` 장대양봉 이후 눌림목 / 5일선 매매 (Undur  | BELUM CUKUP | 29 / 3 | 15 (0/15) | -1.73 | -1.86 | -0.368 [-1.170, +0.434] | – | 41 | 0.65 | -2.51 | 0 | 23 | +0.93 vs -7.11 |
| `M144` Screw Bar | BELUM CUKUP | 10 / 7 | 7 (0/7) | -0.72 | -0.72 | -0.090 [-1.520, +1.340] | – | 40 | 1.14 | -2.02 | 0 | 22 | -0.67 vs -6.78 |
| `M145` Yum-Yum Continuation | BELUM CUKUP | 309 / 79 | 22 (1/21) | -1.83 | -2.08 | -0.043 [-0.403, +0.316] | – | 41 | 0.91 | -3.23 | 0 | 24 | +3.93 vs -7.78 |
| `M150` Trend Bar Failure (Brooks) | BELUM CUKUP | 107 / 65 | 21 (1/20) | -0.85 | -1.01 | -0.072 [-0.343, +0.199] | – | 33 | 1.44 | -1.96 | 0 | 24 | -5.17 vs -7.78 |

## Cara membaca

- **Satu status sahaja yang bermakna untuk wang sebenar: TERBUKTI.**
- **Lift masuk** = adakah kaedah memilih saham lebih baik daripada saham lain yang Lejar beli pada hari sama dan tahap turun-naik sama, diukur 10 sesi (bebas peraturan keluar). Disahkan plasebo: `laporan/PLASEBO_GATE.md`.
- **Buku harian** = pulangan harian purata jika setiap isyarat kaedah itu diberi modal sama dan keluar ikut peraturannya sendiri. Selang 95% Newey-West mengambil kira bahawa semua posisi bergerak bersama pasaran.
- **Jika henti tergelincir** = jangkaan jika setiap keluar henti intrahari diisi pada titik tengah antara paras henti dan harga rendah hari itu (Lejar mengandaikan isian tepat pada henti; rendah hari itu di bawah henti pada ~95% kes). Maklumat sahaja: anggaran kos realistik pelaksanaan, bukan gate.
- Menang % sentiasa dibaca bersama payoff: `X10` menang 94.1% dengan jangkaan negatif.
- `tanpa5` = jangkaan selepas membuang 5% posisi terbaik. Negatif bermaksud kelebihan hidup dalam ekor kanan.
- Jangan ubah ambang gate selepas melihat data. Ia dikunci oleh ujian unit.

