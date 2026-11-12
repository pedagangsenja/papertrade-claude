# Kad skor keputusan (satu jawapan)

Dijana 2026-11-12 oleh `standard/kad_skor.py` (Actions `analisis.yml`). Gate: `standard/SPEC_KAD_SKOR.md` (pradaftar 2026-11-06; pindaan 2026-11-07). Rekod analisis sahaja: tiada order, tiada wang sebenar.

## Tiada kaedah lulus. Kematangan paling awal ~2026-11-12 dan ≥ 10 hari beli dalam setiap rejim (kini ON 1, OFF 18; bergantung pasaran); portfolio lawan SPUS pada MDD -10% ~2027-04-09

**Tindakan hari ini:** JANGAN guna wang sebenar: tiada kaedah TERBUKTI. Papertrade C dan Lejar terus mengumpul data. Rejim OFF sejak 2026-10-16 (19 sesi): saham momentum paling terjejas dalam fasa ini; data hari ini dikira dalam baldi OFF.

Penyebut: **36,292 posisi LANGSUNG** Lejar Penuh lorong 1 merentas 223 kaedah, 19 hari beli (rejim ON 1, OFF 18); 35,700 posisi isian bina semula dan 14 posisi dengan data harga dikuarantin tidak dikira (Mxx sejak isyarat 2026-10-15, Nxx/GB sejak 2026-11-03). Harga pada tutup 2026-11-11.

| Status | Bilangan |
|---|---|
| NEGATIF | 0 |
| GAGAL | 0 |
| BELUM CUKUP | 223 |
| CALON | 0 |
| TERBUKTI | 0 |

## Bila keputusan boleh dibuat

- **G1 kematangan:** ≥ 20 hari beli langsung (ada 19) **dan** ≥ 10 dalam rejim ON (ada 1) **dan** ≥ 10 dalam rejim OFF (ada 18). Rejim ON = QQQ > SMA50 dan SMA10 > SMA20. Paling awal ~2026-11-12 jika rejim ON muncul cukup lama; jika pasaran kekal OFF, G1 menunggu.
- **G6 portfolio:** 126 sesi lorong T4 (paling lama 19); ~2027-04-09. Dibanding dengan SPUS **pada MDD -10%** (toleransi anda), bukan pada MDD SPUS penuh.

## 20 kaedah teratas ikut lift masuk (calon, BUKAN pangkat sehingga status berubah)

| Kaedah | Status | Posisi / tutup | Hari beli (ON/OFF) | Jangkaan % | Jika henti tergelincir % | Buku harian % [95%] | Lift masuk | Menang % | Payoff | tanpa5 | Hari-0 | T4 sesi | T4 pada MDD -10% vs SPUS |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `M104` High Tight Flag / Power Play | BELUM CUKUP | 1 / 0 | 1 (0/1) | +19.60 | +19.60 | +4.659 [+1.207, +8.111] | – | 100 | – | – | 0 | 4 | +1.98 vs +2.67 |
| `M01` Bollinger Band + RSI | BELUM CUKUP | 112 / 20 | 19 (1/18) | +3.05 | +3.05 | -0.087 [-1.052, +0.878] | – | 62 | 1.34 | +1.85 | 0 | 19 | -3.01 vs -3.75 |
| `M05` MACD Divergence + Pengesahan | BELUM CUKUP | 40 / 12 | 14 (1/13) | +0.12 | -0.16 | +0.023 [-0.308, +0.354] | – | 50 | 1.04 | -1.52 | 0 | 19 | +3.87 vs -3.75 |
| `M07` Qullamaggie Breakout | BELUM CUKUP | 1 / 1 | 1 (1/0) | -2.53 | -3.60 | -0.143 [-1.539, +1.253] | – | 0 | – | – | 0 | 19 | -0.25 vs -3.75 |
| `M100` Bulkowski Segi Empat & Segi  | BELUM CUKUP | 58 / 40 | 14 (1/13) | +0.52 | +0.31 | +0.166 [-0.255, +0.586] | – | 53 | 1.02 | -0.10 | 0 | 19 | +4.38 vs -3.75 |
| `M106` DMI Wilder | BELUM CUKUP | 116 / 59 | 17 (1/16) | +0.18 | +0.15 | +0.081 [-0.194, +0.355] | – | 45 | 1.31 | -0.92 | 0 | 19 | -1.12 vs -3.75 |
| `M107` Golden Cross SMA50/200 | BELUM CUKUP | 34 / 7 | 16 (1/15) | -0.18 | -0.50 | +0.043 [-0.422, +0.509] | – | 47 | 1.06 | -1.32 | 0 | 19 | +0.46 vs -3.75 |
| `M121` High 2 bull flag (Brooks) | BELUM CUKUP | 6 / 4 | 4 (0/4) | -10.61 | -10.88 | -1.151 [-2.857, +0.555] | – | 33 | 0.12 | -13.24 | 0 | 15 | -6.35 vs -2.84 |
| `M126` Hidden Smash Day (beli, Larr | BELUM CUKUP | 18 / 11 | 10 (0/10) | -4.06 | -4.34 | -0.254 [-0.848, +0.340] | – | 28 | 0.48 | -4.82 | 0 | 18 | -4.86 vs -3.05 |
| `M129` Wick Play | BELUM CUKUP | 26 / 10 | 10 (1/9) | +0.06 | -0.43 | +0.152 [-0.403, +0.707] | – | 42 | 1.38 | -2.64 | 0 | 19 | +5.91 vs -3.75 |
| `M130` 多方炮 (dua lilin hijau mengapi | BELUM CUKUP | 9 / 3 | 6 (0/6) | -2.60 | -2.70 | +0.032 [-0.619, +0.684] | – | 56 | 0.47 | -4.61 | 0 | 17 | -2.12 vs -2.71 |
| `M135` 3rd Watch | BELUM CUKUP | 14 / 3 | 8 (1/7) | -3.81 | -3.96 | -0.239 [-0.929, +0.451] | – | 36 | 0.31 | -4.69 | 0 | 19 | -5.01 vs -3.75 |
| `M138` 直升机空中加油 (Helikopter isi miny | BELUM CUKUP | 3 / 0 | 3 (0/3) | -0.81 | -0.81 | -0.088 [-0.352, +0.175] | – | 33 | 0.58 | -1.72 | 0 | 12 | -0.18 vs -3.42 |
| `M139` 均线首次粘合向上发散 (MA berhimpun kal | BELUM CUKUP | 82 / 17 | 19 (1/18) | -0.24 | -0.41 | +0.079 [-0.356, +0.515] | – | 46 | 1.09 | -1.68 | 0 | 19 | +3.78 vs -3.75 |
| `M141` First Thrust (Landry) | BELUM CUKUP | 23 / 8 | 8 (1/7) | -1.92 | -2.54 | -0.208 [-0.658, +0.243] | – | 35 | 0.91 | -3.22 | 0 | 19 | -1.90 vs -3.75 |
| `M142` Pecahan volum dari dasar (底部 | BELUM CUKUP | 45 / 5 | 14 (0/14) | +3.31 | +3.20 | +0.233 [-0.247, +0.714] | – | 82 | 0.83 | +1.88 | 0 | 17 | +5.31 vs -2.71 |
| `M143` 장대양봉 이후 눌림목 / 5일선 매매 (Undur  | BELUM CUKUP | 21 / 1 | 11 (0/11) | +0.16 | +0.16 | -0.349 [-1.388, +0.691] | – | 57 | 0.82 | -0.38 | 0 | 18 | +0.36 vs -3.05 |
| `M144` Screw Bar | BELUM CUKUP | 9 / 6 | 6 (0/6) | -0.42 | -0.42 | -0.100 [-2.357, +2.157] | – | 33 | 1.77 | -2.13 | 0 | 17 | -0.34 vs -2.71 |
| `M145` Yum-Yum Continuation | BELUM CUKUP | 300 / 62 | 19 (1/18) | +0.42 | +0.22 | +0.089 [-0.243, +0.423] | – | 54 | 0.95 | -0.85 | 0 | 19 | +5.27 vs -3.75 |
| `M150` Trend Bar Failure (Brooks) | BELUM CUKUP | 99 / 39 | 18 (1/17) | +0.56 | +0.47 | +0.031 [-0.229, +0.291] | – | 47 | 1.39 | -0.40 | 0 | 19 | -2.71 vs -3.75 |

## Cara membaca

- **Satu status sahaja yang bermakna untuk wang sebenar: TERBUKTI.**
- **Lift masuk** = adakah kaedah memilih saham lebih baik daripada saham lain yang Lejar beli pada hari sama dan tahap turun-naik sama, diukur 10 sesi (bebas peraturan keluar). Disahkan plasebo: `laporan/PLASEBO_GATE.md`.
- **Buku harian** = pulangan harian purata jika setiap isyarat kaedah itu diberi modal sama dan keluar ikut peraturannya sendiri. Selang 95% Newey-West mengambil kira bahawa semua posisi bergerak bersama pasaran.
- **Jika henti tergelincir** = jangkaan jika setiap keluar henti intrahari diisi pada titik tengah antara paras henti dan harga rendah hari itu (Lejar mengandaikan isian tepat pada henti; rendah hari itu di bawah henti pada ~95% kes). Maklumat sahaja: anggaran kos realistik pelaksanaan, bukan gate.
- Menang % sentiasa dibaca bersama payoff: `X10` menang 94.1% dengan jangkaan negatif.
- `tanpa5` = jangkaan selepas membuang 5% posisi terbaik. Negatif bermaksud kelebihan hidup dalam ekor kanan.
- Jangan ubah ambang gate selepas melihat data. Ia dikunci oleh ujian unit.

