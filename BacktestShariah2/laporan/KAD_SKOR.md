# Kad skor keputusan (satu jawapan)

Dijana 2026-11-10 oleh `standard/kad_skor.py` (Actions `analisis.yml`). Gate: `standard/SPEC_KAD_SKOR.md` (pradaftar 2026-11-06; pindaan 2026-11-07). Rekod analisis sahaja: tiada order, tiada wang sebenar.

## Tiada kaedah lulus. Kematangan paling awal ~2026-11-12 dan ≥ 10 hari beli dalam setiap rejim (kini ON 1, OFF 16; bergantung pasaran); portfolio lawan SPUS pada MDD -10% ~2027-04-09

**Tindakan hari ini:** JANGAN guna wang sebenar: tiada kaedah TERBUKTI. Papertrade C dan Lejar terus mengumpul data. Rejim OFF sejak 2026-10-16 (17 sesi): saham momentum paling terjejas dalam fasa ini; data hari ini dikira dalam baldi OFF.

Penyebut: **30,522 posisi LANGSUNG** Lejar Penuh lorong 1 merentas 223 kaedah, 17 hari beli (rejim ON 1, OFF 16); 35,700 posisi isian bina semula dan 14 posisi dengan data harga dikuarantin tidak dikira (Mxx sejak isyarat 2026-10-15, Nxx/GB sejak 2026-11-03). Harga pada tutup 2026-11-09.

| Status | Bilangan |
|---|---|
| NEGATIF | 0 |
| GAGAL | 0 |
| BELUM CUKUP | 223 |
| CALON | 0 |
| TERBUKTI | 0 |

## Bila keputusan boleh dibuat

- **G1 kematangan:** ≥ 20 hari beli langsung (ada 17) **dan** ≥ 10 dalam rejim ON (ada 1) **dan** ≥ 10 dalam rejim OFF (ada 16). Rejim ON = QQQ > SMA50 dan SMA10 > SMA20. Paling awal ~2026-11-12 jika rejim ON muncul cukup lama; jika pasaran kekal OFF, G1 menunggu.
- **G6 portfolio:** 126 sesi lorong T4 (paling lama 17); ~2027-04-09. Dibanding dengan SPUS **pada MDD -10%** (toleransi anda), bukan pada MDD SPUS penuh.

## 20 kaedah teratas ikut lift masuk (calon, BUKAN pangkat sehingga status berubah)

| Kaedah | Status | Posisi / tutup | Hari beli (ON/OFF) | Jangkaan % | Jika henti tergelincir % | Buku harian % [95%] | Lift masuk | Menang % | Payoff | tanpa5 | Hari-0 | T4 sesi | T4 pada MDD -10% vs SPUS |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `M01` Bollinger Band + RSI | BELUM CUKUP | 108 / 17 | 17 (1/16) | +1.66 | +1.66 | -0.200 [-1.207, +0.808] | – | 62 | 0.97 | +0.63 | 0 | 17 | -3.38 vs -4.21 |
| `M05` MACD Divergence + Pengesahan | BELUM CUKUP | 38 / 12 | 13 (1/12) | +0.59 | +0.30 | +0.061 [-0.352, +0.474] | – | 50 | 1.17 | -1.11 | 0 | 17 | +4.61 vs -4.21 |
| `M07` Qullamaggie Breakout | BELUM CUKUP | 1 / 1 | 1 (1/0) | -2.53 | -3.60 | -0.143 [-1.539, +1.253] | – | 0 | – | – | 0 | 17 | -0.25 vs -4.21 |
| `M100` Bulkowski Segi Empat & Segi  | BELUM CUKUP | 58 / 39 | 14 (1/13) | +0.36 | +0.14 | +0.156 [-0.317, +0.628] | – | 53 | 0.97 | -0.27 | 0 | 17 | +4.05 vs -4.21 |
| `M104` High Tight Flag / Power Play | BELUM CUKUP | 1 / 0 | 1 (0/1) | +14.81 | +14.81 | +7.234 [-3.372, +17.839] | – | 100 | – | – | 0 | 2 | +1.50 vs +2.18 |
| `M106` DMI Wilder | BELUM CUKUP | 100 / 53 | 15 (1/14) | +0.61 | +0.58 | +0.128 [-0.183, +0.438] | – | 47 | 1.37 | -0.49 | 0 | 17 | -2.24 vs -4.21 |
| `M107` Golden Cross SMA50/200 | BELUM CUKUP | 28 / 7 | 14 (1/13) | -0.10 | -0.49 | +0.054 [-0.472, +0.579] | – | 54 | 0.84 | -1.52 | 0 | 17 | -0.17 vs -4.21 |
| `M121` High 2 bull flag (Brooks) | BELUM CUKUP | 5 / 3 | 3 (0/3) | -9.95 | -10.14 | -0.804 [-2.486, +0.878] | – | 40 | 0.08 | -13.07 | 0 | 13 | -4.94 vs -3.30 |
| `M126` Hidden Smash Day (beli, Larr | BELUM CUKUP | 18 / 11 | 10 (0/10) | -3.79 | -4.07 | -0.244 [-0.922, +0.435] | – | 22 | 0.80 | -4.62 | 0 | 16 | -4.54 vs -3.52 |
| `M129` Wick Play | BELUM CUKUP | 23 / 9 | 9 (1/8) | +0.50 | -0.04 | +0.200 [-0.430, +0.830] | – | 43 | 1.40 | -2.41 | 0 | 17 | +5.96 vs -4.21 |
| `M130` 多方炮 (dua lilin hijau mengapi | BELUM CUKUP | 9 / 3 | 6 (0/6) | -0.23 | -0.33 | +0.255 [-0.526, +1.035] | – | 67 | 0.48 | -2.33 | 0 | 15 | +0.03 vs -3.17 |
| `M135` 3rd Watch | BELUM CUKUP | 12 / 3 | 7 (1/6) | -5.04 | -5.22 | -0.309 [-1.095, +0.477] | – | 25 | 0.33 | -5.83 | 0 | 17 | -5.79 vs -4.21 |
| `M138` 直升机空中加油 (Helikopter isi miny | BELUM CUKUP | 2 / 0 | 2 (0/2) | -0.86 | -0.86 | -0.071 [-0.392, +0.251] | – | 50 | 0.13 | -1.98 | 0 | 10 | -0.13 vs -3.88 |
| `M139` 均线首次粘合向上发散 (MA berhimpun kal | BELUM CUKUP | 69 / 17 | 17 (1/16) | +0.16 | -0.05 | +0.119 [-0.364, +0.603] | – | 51 | 1.00 | -1.42 | 0 | 17 | +5.56 vs -4.21 |
| `M141` First Thrust (Landry) | BELUM CUKUP | 20 / 8 | 7 (1/6) | -1.99 | -2.71 | -0.217 [-0.721, +0.287] | – | 40 | 0.70 | -2.76 | 0 | 17 | -1.90 vs -4.21 |
| `M142` Pecahan volum dari dasar (底部 | BELUM CUKUP | 40 / 5 | 13 (0/13) | +3.22 | +3.09 | +0.234 [-0.322, +0.789] | – | 82 | 0.74 | +2.06 | 0 | 15 | +3.80 vs -3.17 |
| `M143` 장대양봉 이후 눌림목 / 5일선 매매 (Undur  | BELUM CUKUP | 13 / 1 | 9 (0/9) | +0.67 | +0.67 | -0.376 [-1.548, +0.796] | – | 69 | 0.58 | +0.08 | 0 | 16 | +0.74 vs -3.52 |
| `M144` Screw Bar | BELUM CUKUP | 8 / 6 | 5 (0/5) | +0.11 | +0.11 | +0.119 [-3.150, +3.388] | – | 38 | 1.71 | -1.80 | 0 | 15 | +0.10 vs -3.17 |
| `M145` Yum-Yum Continuation | BELUM CUKUP | 280 / 54 | 17 (1/16) | +0.91 | +0.73 | +0.131 [-0.235, +0.496] | – | 55 | 1.01 | -0.36 | 0 | 17 | +4.51 vs -4.21 |
| `M146` 3-Bar Momentum Pattern | BELUM CUKUP | 76 / 28 | 16 (1/15) | +2.18 | +1.83 | +0.413 [+0.073, +0.754] | – | 62 | 1.23 | +1.20 | 4 | 17 | +6.45 vs -4.21 |

## Cara membaca

- **Satu status sahaja yang bermakna untuk wang sebenar: TERBUKTI.**
- **Lift masuk** = adakah kaedah memilih saham lebih baik daripada saham lain yang Lejar beli pada hari sama dan tahap turun-naik sama, diukur 10 sesi (bebas peraturan keluar). Disahkan plasebo: `laporan/PLASEBO_GATE.md`.
- **Buku harian** = pulangan harian purata jika setiap isyarat kaedah itu diberi modal sama dan keluar ikut peraturannya sendiri. Selang 95% Newey-West mengambil kira bahawa semua posisi bergerak bersama pasaran.
- **Jika henti tergelincir** = jangkaan jika setiap keluar henti intrahari diisi pada titik tengah antara paras henti dan harga rendah hari itu (Lejar mengandaikan isian tepat pada henti; rendah hari itu di bawah henti pada ~95% kes). Maklumat sahaja: anggaran kos realistik pelaksanaan, bukan gate.
- Menang % sentiasa dibaca bersama payoff: `X10` menang 94.1% dengan jangkaan negatif.
- `tanpa5` = jangkaan selepas membuang 5% posisi terbaik. Negatif bermaksud kelebihan hidup dalam ekor kanan.
- Jangan ubah ambang gate selepas melihat data. Ia dikunci oleh ujian unit.

