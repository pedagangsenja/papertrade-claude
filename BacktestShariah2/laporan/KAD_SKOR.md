# Kad skor keputusan (satu jawapan)

Dijana 2026-11-13 oleh `standard/kad_skor.py` (Actions `analisis.yml`). Gate: `standard/SPEC_KAD_SKOR.md` (pradaftar 2026-11-06; pindaan 2026-11-07). Rekod analisis sahaja: tiada order, tiada wang sebenar.

## Tiada kaedah lulus. Kematangan paling awal ~2026-11-12 dan ≥ 10 hari beli dalam setiap rejim (kini ON 1, OFF 19; bergantung pasaran); portfolio lawan SPUS pada MDD -10% ~2027-04-09

**Tindakan hari ini:** JANGAN guna wang sebenar: tiada kaedah TERBUKTI. Papertrade C dan Lejar terus mengumpul data. Rejim OFF sejak 2026-10-16 (20 sesi): saham momentum paling terjejas dalam fasa ini; data hari ini dikira dalam baldi OFF.

Penyebut: **38,861 posisi LANGSUNG** Lejar Penuh lorong 1 merentas 223 kaedah, 20 hari beli (rejim ON 1, OFF 19); 35,721 posisi isian bina semula dan 14 posisi dengan data harga dikuarantin tidak dikira (Mxx sejak isyarat 2026-10-15, Nxx/GB sejak 2026-11-03). Harga pada tutup 2026-11-12.

| Status | Bilangan |
|---|---|
| NEGATIF | 0 |
| GAGAL | 0 |
| BELUM CUKUP | 223 |
| CALON | 0 |
| TERBUKTI | 0 |

## Bila keputusan boleh dibuat

- **G1 kematangan:** ≥ 20 hari beli langsung (ada 20) **dan** ≥ 10 dalam rejim ON (ada 1) **dan** ≥ 10 dalam rejim OFF (ada 19). Rejim ON = QQQ > SMA50 dan SMA10 > SMA20. Paling awal ~2026-11-12 jika rejim ON muncul cukup lama; jika pasaran kekal OFF, G1 menunggu.
- **G6 portfolio:** 126 sesi lorong T4 (paling lama 20); ~2027-04-09. Dibanding dengan SPUS **pada MDD -10%** (toleransi anda), bukan pada MDD SPUS penuh.

## 20 kaedah teratas ikut lift masuk (calon, BUKAN pangkat sehingga status berubah)

| Kaedah | Status | Posisi / tutup | Hari beli (ON/OFF) | Jangkaan % | Jika henti tergelincir % | Buku harian % [95%] | Lift masuk | Menang % | Payoff | tanpa5 | Hari-0 | T4 sesi | T4 pada MDD -10% vs SPUS |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `M104` High Tight Flag / Power Play | BELUM CUKUP | 1 / 0 | 1 (0/1) | +20.54 | +20.54 | +3.885 [+0.674, +7.095] | – | 100 | – | – | 0 | 5 | +2.07 vs +3.05 |
| `M01` Bollinger Band + RSI | BELUM CUKUP | 113 / 21 | 20 (1/19) | +2.35 | +2.35 | -0.123 [-1.011, +0.764] | – | 63 | 1.07 | +1.09 | 0 | 20 | -4.58 vs -3.40 |
| `M05` MACD Divergence + Pengesahan | BELUM CUKUP | 41 / 12 | 15 (1/14) | -0.97 | -1.24 | -0.051 [-0.371, +0.269] | – | 37 | 1.27 | -2.95 | 0 | 20 | +1.94 vs -3.40 |
| `M07` Qullamaggie Breakout | BELUM CUKUP | 1 / 1 | 1 (1/0) | -2.53 | -3.60 | -0.143 [-1.539, +1.253] | – | 0 | – | – | 0 | 20 | -0.25 vs -3.40 |
| `M100` Bulkowski Segi Empat & Segi  | BELUM CUKUP | 60 / 40 | 15 (1/14) | +0.28 | +0.07 | +0.124 [-0.272, +0.520] | – | 48 | 1.17 | -0.33 | 0 | 20 | +3.48 vs -3.40 |
| `M106` DMI Wilder | BELUM CUKUP | 127 / 61 | 18 (1/17) | -0.69 | -0.72 | +0.000 [-0.310, +0.311] | – | 39 | 1.17 | -1.75 | 0 | 20 | -2.21 vs -3.40 |
| `M107` Golden Cross SMA50/200 | BELUM CUKUP | 37 / 7 | 17 (1/16) | -1.23 | -1.53 | -0.022 [-0.484, +0.440] | – | 35 | 1.18 | -2.30 | 0 | 20 | -0.49 vs -3.40 |
| `M121` High 2 bull flag (Brooks) | BELUM CUKUP | 7 / 4 | 5 (0/5) | -9.34 | -9.56 | -1.111 [-2.690, +0.468] | – | 43 | 0.05 | -11.13 | 0 | 16 | -6.49 vs -2.48 |
| `M126` Hidden Smash Day (beli, Larr | BELUM CUKUP | 18 / 11 | 10 (0/10) | -4.34 | -4.61 | -0.278 [-0.833, +0.278] | – | 22 | 0.56 | -5.06 | 0 | 19 | -5.13 vs -2.70 |
| `M129` Wick Play | BELUM CUKUP | 26 / 10 | 10 (1/9) | -0.86 | -1.34 | +0.076 [-0.463, +0.616] | – | 38 | 1.38 | -3.64 | 0 | 20 | +4.84 vs -3.40 |
| `M130` 多方炮 (dua lilin hijau mengapi | BELUM CUKUP | 10 / 3 | 7 (0/7) | -4.26 | -4.35 | -0.114 [-0.830, +0.602] | – | 40 | 0.49 | -5.86 | 0 | 18 | -4.02 vs -2.35 |
| `M135` 3rd Watch | BELUM CUKUP | 15 / 3 | 9 (1/8) | -4.94 | -5.08 | -0.315 [-0.967, +0.338] | – | 20 | 0.35 | -5.70 | 0 | 20 | -6.27 vs -3.40 |
| `M138` 直升机空中加油 (Helikopter isi miny | BELUM CUKUP | 3 / 0 | 3 (0/3) | -2.96 | -2.96 | -0.248 [-0.638, +0.142] | – | 0 | – | -4.13 | 0 | 13 | -0.83 vs -3.07 |
| `M139` 均线首次粘合向上发散 (MA berhimpun kal | BELUM CUKUP | 84 / 17 | 20 (1/19) | -1.45 | -1.61 | +0.003 [-0.445, +0.450] | – | 39 | 1.07 | -2.75 | 0 | 20 | +2.43 vs -3.40 |
| `M141` First Thrust (Landry) | BELUM CUKUP | 27 / 9 | 9 (1/8) | -2.01 | -2.54 | -0.223 [-0.643, +0.198] | – | 37 | 0.78 | -3.05 | 0 | 20 | -3.46 vs -3.40 |
| `M142` Pecahan volum dari dasar (底部 | BELUM CUKUP | 48 / 5 | 15 (0/15) | +1.34 | +1.24 | +0.116 [-0.335, +0.567] | – | 62 | 1.05 | +0.21 | 0 | 18 | +4.29 vs -2.35 |
| `M143` 장대양봉 이후 눌림목 / 5일선 매매 (Undur  | BELUM CUKUP | 24 / 1 | 12 (0/12) | -1.63 | -1.63 | -0.426 [-1.403, +0.551] | – | 38 | 0.60 | -2.34 | 0 | 19 | -0.99 vs -2.70 |
| `M144` Screw Bar | BELUM CUKUP | 9 / 7 | 6 (0/6) | -2.04 | -2.04 | -0.504 [-2.206, +1.198] | – | 33 | 0.79 | -3.25 | 0 | 18 | -1.79 vs -2.35 |
| `M145` Yum-Yum Continuation | BELUM CUKUP | 308 / 64 | 20 (1/19) | -0.61 | -0.81 | +0.024 [-0.335, +0.383] | – | 46 | 0.98 | -1.87 | 0 | 20 | +4.27 vs -3.40 |
| `M150` Trend Bar Failure (Brooks) | BELUM CUKUP | 102 / 40 | 19 (1/18) | -0.16 | -0.25 | -0.025 [-0.300, +0.250] | – | 38 | 1.50 | -1.13 | 0 | 20 | -4.33 vs -3.40 |

## Cara membaca

- **Satu status sahaja yang bermakna untuk wang sebenar: TERBUKTI.**
- **Lift masuk** = adakah kaedah memilih saham lebih baik daripada saham lain yang Lejar beli pada hari sama dan tahap turun-naik sama, diukur 10 sesi (bebas peraturan keluar). Disahkan plasebo: `laporan/PLASEBO_GATE.md`.
- **Buku harian** = pulangan harian purata jika setiap isyarat kaedah itu diberi modal sama dan keluar ikut peraturannya sendiri. Selang 95% Newey-West mengambil kira bahawa semua posisi bergerak bersama pasaran.
- **Jika henti tergelincir** = jangkaan jika setiap keluar henti intrahari diisi pada titik tengah antara paras henti dan harga rendah hari itu (Lejar mengandaikan isian tepat pada henti; rendah hari itu di bawah henti pada ~95% kes). Maklumat sahaja: anggaran kos realistik pelaksanaan, bukan gate.
- Menang % sentiasa dibaca bersama payoff: `X10` menang 94.1% dengan jangkaan negatif.
- `tanpa5` = jangkaan selepas membuang 5% posisi terbaik. Negatif bermaksud kelebihan hidup dalam ekor kanan.
- Jangan ubah ambang gate selepas melihat data. Ia dikunci oleh ujian unit.

