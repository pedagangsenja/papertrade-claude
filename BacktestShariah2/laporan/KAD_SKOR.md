# Kad skor keputusan (satu jawapan)

Dijana 2026-11-11 oleh `standard/kad_skor.py` (Actions `analisis.yml`). Gate: `standard/SPEC_KAD_SKOR.md` (pradaftar 2026-11-06; pindaan 2026-11-07). Rekod analisis sahaja: tiada order, tiada wang sebenar.

## Tiada kaedah lulus. Kematangan paling awal ~2026-11-12 dan ≥ 10 hari beli dalam setiap rejim (kini ON 1, OFF 17; bergantung pasaran); portfolio lawan SPUS pada MDD -10% ~2027-04-09

**Tindakan hari ini:** JANGAN guna wang sebenar: tiada kaedah TERBUKTI. Papertrade C dan Lejar terus mengumpul data. Rejim OFF sejak 2026-10-16 (18 sesi): saham momentum paling terjejas dalam fasa ini; data hari ini dikira dalam baldi OFF.

Penyebut: **34,553 posisi LANGSUNG** Lejar Penuh lorong 1 merentas 223 kaedah, 18 hari beli (rejim ON 1, OFF 17); 35,700 posisi isian bina semula dan 14 posisi dengan data harga dikuarantin tidak dikira (Mxx sejak isyarat 2026-10-15, Nxx/GB sejak 2026-11-03). Harga pada tutup 2026-11-10.

| Status | Bilangan |
|---|---|
| NEGATIF | 0 |
| GAGAL | 0 |
| BELUM CUKUP | 223 |
| CALON | 0 |
| TERBUKTI | 0 |

## Bila keputusan boleh dibuat

- **G1 kematangan:** ≥ 20 hari beli langsung (ada 18) **dan** ≥ 10 dalam rejim ON (ada 1) **dan** ≥ 10 dalam rejim OFF (ada 17). Rejim ON = QQQ > SMA50 dan SMA10 > SMA20. Paling awal ~2026-11-12 jika rejim ON muncul cukup lama; jika pasaran kekal OFF, G1 menunggu.
- **G6 portfolio:** 126 sesi lorong T4 (paling lama 18); ~2027-04-09. Dibanding dengan SPUS **pada MDD -10%** (toleransi anda), bukan pada MDD SPUS penuh.

## 20 kaedah teratas ikut lift masuk (calon, BUKAN pangkat sehingga status berubah)

| Kaedah | Status | Posisi / tutup | Hari beli (ON/OFF) | Jangkaan % | Jika henti tergelincir % | Buku harian % [95%] | Lift masuk | Menang % | Payoff | tanpa5 | Hari-0 | T4 sesi | T4 pada MDD -10% vs SPUS |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `M01` Bollinger Band + RSI | BELUM CUKUP | 110 / 18 | 18 (1/17) | +1.03 | +1.03 | -0.228 [-1.164, +0.708] | – | 58 | 0.94 | -0.12 | 0 | 18 | -3.97 vs -4.81 |
| `M05` MACD Divergence + Pengesahan | BELUM CUKUP | 40 / 12 | 14 (1/13) | +0.17 | -0.10 | +0.028 [-0.326, +0.383] | – | 50 | 1.05 | -1.46 | 0 | 18 | +4.13 vs -4.81 |
| `M07` Qullamaggie Breakout | BELUM CUKUP | 1 / 1 | 1 (1/0) | -2.53 | -3.60 | -0.143 [-1.539, +1.253] | – | 0 | – | – | 0 | 18 | -0.25 vs -4.81 |
| `M100` Bulkowski Segi Empat & Segi  | BELUM CUKUP | 58 / 40 | 14 (1/13) | +0.51 | +0.29 | +0.172 [-0.276, +0.620] | – | 53 | 1.01 | -0.11 | 0 | 18 | +4.27 vs -4.81 |
| `M104` High Tight Flag / Power Play | BELUM CUKUP | 1 / 0 | 1 (0/1) | +14.59 | +14.59 | +4.759 [-1.285, +10.803] | – | 100 | – | – | 0 | 3 | +1.48 vs +1.54 |
| `M106` DMI Wilder | BELUM CUKUP | 113 / 53 | 16 (1/15) | -0.13 | -0.16 | +0.055 [-0.241, +0.351] | – | 42 | 1.29 | -1.22 | 0 | 18 | -2.65 vs -4.81 |
| `M107` Golden Cross SMA50/200 | BELUM CUKUP | 30 / 7 | 15 (1/14) | -0.02 | -0.38 | +0.057 [-0.437, +0.550] | – | 43 | 1.30 | -1.35 | 0 | 18 | +0.69 vs -4.81 |
| `M121` High 2 bull flag (Brooks) | BELUM CUKUP | 5 / 4 | 3 (0/3) | -13.65 | -13.97 | -1.400 [-3.457, +0.656] | – | 0 | – | -16.97 | 0 | 14 | -6.81 vs -3.91 |
| `M126` Hidden Smash Day (beli, Larr | BELUM CUKUP | 18 / 11 | 10 (0/10) | -3.86 | -4.14 | -0.240 [-0.876, +0.396] | – | 33 | 0.43 | -4.61 | 0 | 17 | -4.59 vs -4.12 |
| `M129` Wick Play | BELUM CUKUP | 23 / 9 | 9 (1/8) | +0.57 | +0.02 | +0.195 [-0.397, +0.786] | – | 43 | 1.42 | -2.43 | 0 | 18 | +5.85 vs -4.81 |
| `M130` 多方炮 (dua lilin hijau mengapi | BELUM CUKUP | 9 / 3 | 6 (0/6) | -2.19 | -2.29 | +0.070 [-0.614, +0.755] | – | 56 | 0.52 | -4.37 | 0 | 16 | -1.75 vs -3.78 |
| `M135` 3rd Watch | BELUM CUKUP | 12 / 3 | 7 (1/6) | -4.94 | -5.12 | -0.284 [-1.015, +0.447] | – | 25 | 0.38 | -5.86 | 0 | 18 | -5.69 vs -4.81 |
| `M138` 直升机空中加油 (Helikopter isi miny | BELUM CUKUP | 2 / 0 | 2 (0/2) | -1.30 | -1.30 | -0.104 [-0.398, +0.189] | – | 50 | 0.06 | -2.77 | 0 | 11 | -0.22 vs -4.49 |
| `M139` 均线首次粘合向上发散 (MA berhimpun kal | BELUM CUKUP | 75 / 17 | 18 (1/17) | -0.60 | -0.79 | +0.062 [-0.404, +0.528] | – | 41 | 1.24 | -2.05 | 0 | 18 | +4.02 vs -4.81 |
| `M141` First Thrust (Landry) | BELUM CUKUP | 23 / 8 | 8 (1/7) | -1.76 | -2.39 | -0.206 [-0.684, +0.272] | – | 43 | 0.64 | -2.93 | 0 | 18 | -1.69 vs -4.81 |
| `M142` Pecahan volum dari dasar (底部 | BELUM CUKUP | 40 / 5 | 13 (0/13) | +2.94 | +2.81 | +0.200 [-0.291, +0.690] | – | 78 | 0.96 | +1.72 | 0 | 16 | +4.80 vs -3.78 |
| `M143` 장대양봉 이후 눌림목 / 5일선 매매 (Undur  | BELUM CUKUP | 19 / 1 | 10 (0/10) | +0.08 | +0.08 | -0.375 [-1.472, +0.722] | – | 63 | 0.61 | -0.22 | 0 | 17 | +0.60 vs -4.12 |
| `M144` Screw Bar | BELUM CUKUP | 8 / 6 | 5 (0/5) | -0.41 | -0.41 | -0.095 [-2.657, +2.466] | – | 38 | 1.48 | -2.22 | 0 | 16 | -0.31 vs -3.78 |
| `M145` Yum-Yum Continuation | BELUM CUKUP | 292 / 62 | 18 (1/17) | +0.39 | +0.19 | +0.092 [-0.260, +0.444] | – | 53 | 0.99 | -0.90 | 0 | 18 | +4.32 vs -4.81 |
| `M150` Trend Bar Failure (Brooks) | BELUM CUKUP | 98 / 39 | 17 (1/16) | +0.57 | +0.49 | +0.033 [-0.242, +0.309] | – | 45 | 1.55 | -0.40 | 0 | 18 | -2.94 vs -4.81 |

## Cara membaca

- **Satu status sahaja yang bermakna untuk wang sebenar: TERBUKTI.**
- **Lift masuk** = adakah kaedah memilih saham lebih baik daripada saham lain yang Lejar beli pada hari sama dan tahap turun-naik sama, diukur 10 sesi (bebas peraturan keluar). Disahkan plasebo: `laporan/PLASEBO_GATE.md`.
- **Buku harian** = pulangan harian purata jika setiap isyarat kaedah itu diberi modal sama dan keluar ikut peraturannya sendiri. Selang 95% Newey-West mengambil kira bahawa semua posisi bergerak bersama pasaran.
- **Jika henti tergelincir** = jangkaan jika setiap keluar henti intrahari diisi pada titik tengah antara paras henti dan harga rendah hari itu (Lejar mengandaikan isian tepat pada henti; rendah hari itu di bawah henti pada ~95% kes). Maklumat sahaja: anggaran kos realistik pelaksanaan, bukan gate.
- Menang % sentiasa dibaca bersama payoff: `X10` menang 94.1% dengan jangkaan negatif.
- `tanpa5` = jangkaan selepas membuang 5% posisi terbaik. Negatif bermaksud kelebihan hidup dalam ekor kanan.
- Jangan ubah ambang gate selepas melihat data. Ia dikunci oleh ujian unit.

