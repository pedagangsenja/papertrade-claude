# Semakan peringkat AKAUN: buku 10 slot bagi lorong swing dan lorong trend (backtest; BUKAN bukti)

> **Status keputusan (kad skor, harga 2026-11-13):** TERBUKTI 0 · CALON 0 · BELUM CUKUP 226 · GAGAL 0 · NEGATIF 0. Rejim QQQ OFF sejak 2026-10-16. Hanya **TERBUKTI** layak untuk wang sebenar (`laporan/KAD_SKOR.md`); nombor dalam laporan ini BUKAN keputusan dan tidak boleh dibaca sebagai pangkat untuk wang sebenar.

Dijana `kajian/carian_setup/cs_akaun9.py`. Pradaftar: `kajian/SPEC_CARIAN_SETUP.md` pindaan 14 Nov 2026 (s), dikomit sebelum dijalankan. **Jangan sunting secara manual.**

Soalan: kadar tangkap bukan hasil akaun. Akaun 10 slot (10 % setiap satu), kumpulan B, 20100104 – 20260828 (16.6 tahun), kos 0.5 % pusingan, tunai 0 %; isyarat berlebihan dipilih rawak, 200 ulangan (angka = median). **Jalur rawak** = isyarat yang sama digantikan saham rawak pada hari dan tahap turun-naik yang sama, dengan henti dan keluar yang sama. **"CAGR pada MDD −10 %"** = pendedahan dikecilkan (baki tunai) sehingga kejatuhan terburuk akaun kira-kira −10 %, iaitu toleransi pengguna. **Bacaan dikunci:** buku "menambah" hanya jika angka itu positif DAN melebihi persentil ke-95 jalur rawak. Maklumat sahaja: SPY beli-dan-pegang pada MDD −10 % = +4.37 % setahun (CAGR +14.3 %, MDD -33.7 %).

## 1. Lorong swing (pegang hingga 4 minggu; pegang minimum 3 sesi)

| Buku | Isyarat | Diambil | Dagangan setahun | Bulan tanpa belian | Pendedahan % | CAGR % | MDD % | **CAGR pada MDD −10 %** | Jalur rawak: median (p5 – p95) | Tahun positif | Tahun terburuk % | K3: CAGR / MDD % | Tangkap penuh % diambil (rawak) | Menang % | Rugi ≥ 8 % % | Menambah? |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `F43` | 527 | 148 (28 %) | 9 | 91 % | 7 | +2.6 | -13.6 | **+1.98** | +0.99 (+0.19 – +1.89) | 8 / 17 | -8.6 | -0.8 / -12.1 | 16.2 (14.1) | 61 | 21 | **YA** |
| `F63` | 440 | 283 (64 %) | 17 | 62 % | 12 | +6.9 | -29.2 | **+2.46** | +1.12 (+0.24 – +2.55) | 12 / 17 | -9.7 | +6.6 / -22.6 | 24.7 (13.7) | 61 | 26 | **TIDAK** |
| `F65` | 464 | 204 (44 %) | 12 | 80 % | 8 | +2.5 | -16.1 | **+1.66** | +1.56 (+0.67 – +2.81) | 12 / 17 | -4.2 | +3.9 / -11.2 | 19.1 (14.1) | 62 | 25 | **TIDAK** |
| `F51` | 747 | 250 (33 %) | 15 | 82 % | 10 | +5.6 | -17.0 | **+3.32** | +1.96 (+0.81 – +3.52) | 10 / 17 | -2.8 | +2.7 / -13.9 | 21.9 (12.6) | 63 | 20 | **TIDAK** |
| `F50` | 789 | 268 (34 %) | 16 | 78 % | 12 | +4.4 | -23.8 | **+2.07** | +1.22 (+0.51 – +2.24) | 9 / 17 | -6.6 | +0.1 / -22.2 | 23.7 (16.5) | 56 | 27 | **TIDAK** |
| `F56` | 2,553 | 383 (15 %) | 23 | 75 % | 18 | +8.5 | -31.9 | **+2.86** | +1.70 (+0.82 – +2.63) | 10 / 17 | -16.7 | +12.7 / -20.5 | 19.5 (16.9) | 61 | 22 | **YA** |
| `F39` | 547 | 332 (61 %) | 20 | 64 % | 12 | +0.5 | -29.7 | **+0.28** | +0.49 (-0.26 – +1.68) | 8 / 17 | -12.6 | -13.8 / -24.7 | 18.4 (7.8) | 47 | 38 | **TIDAK** |
| `F91` | 404 | 274 (68 %) | 16 | 57 % | 12 | +2.5 | -27.3 | **+1.02** | +0.02 (-0.48 – +1.07) | 12 / 17 | -13.6 | +0.8 / -17.7 | 19.0 (9.0) | 51 | 32 | **TIDAK** |
| `SWING8` | 6,471 | 1,094 (17 %) | 66 | 16 % | 46 | +10.2 | -51.3 | **+2.32** | +0.78 (+0.07 – +1.80) | 13 / 17 | -23.9 | +6.7 / -34.3 | 18.5 (10.1) | 53 | 29 | **YA** |

## 2. Lorong trend (pegang hingga 6 bulan)

| Buku | Isyarat | Diambil | Dagangan setahun | Bulan tanpa belian | Pendedahan % | CAGR % | MDD % | **CAGR pada MDD −10 %** | Jalur rawak: median (p5 – p95) | Tahun positif | Tahun terburuk % | K3: CAGR / MDD % | Pelari besar % diambil (rawak) | Menang % | Rugi ≥ 15 % % | Menambah? |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `T01` | 499 | 139 (28 %) | 8 | 84 % | 35 | +4.2 | -39.8 | **+1.35** | +1.55 (+0.47 – +3.26) | 10 / 17 | -13.4 | +6.8 / -32.6 | 26.2 (15.1) | 45 | 43 | **TIDAK** |
| `T02` | 493 | 140 (28 %) | 8 | 84 % | 35 | +4.4 | -41.4 | **+1.31** | +1.51 (+0.36 – +2.93) | 11 / 17 | -13.6 | +7.1 / -34.7 | 26.4 (14.9) | 45 | 43 | **TIDAK** |
| `T03` | 437 | 107 (24 %) | 6 | 85 % | 26 | +0.4 | -40.5 | **+0.30** | +1.03 (+0.06 – +2.22) | 7 / 17 | -19.7 | +5.8 / -23.0 | 17.8 (14.8) | 43 | 46 | **TIDAK** |
| `T04` | 452 | 176 (39 %) | 11 | 66 % | 44 | +2.8 | -42.6 | **+1.10** | +0.73 (-0.10 – +1.96) | 9 / 17 | -24.6 | +24.4 / -27.1 | 24.4 (13.9) | 39 | 49 | **TIDAK** |
| `T05` | 543 | 240 (44 %) | 14 | 48 % | 55 | +0.3 | -45.1 | **+0.45** | +0.96 (+0.01 – +2.45) | 8 / 17 | -29.1 | +16.4 / -25.8 | 14.2 (11.5) | 39 | 46 | **TIDAK** |
| `T06` | 452 | 176 (39 %) | 11 | 67 % | 44 | +3.0 | -41.4 | **+1.15** | +0.74 (-0.09 – +1.96) | 9 / 17 | -24.6 | +24.5 / -27.1 | 24.4 (13.5) | 39 | 48 | **TIDAK** |
| `T07` | 771 | 219 (28 %) | 13 | 44 % | 54 | +8.3 | -41.5 | **+2.34** | +1.08 (+0.22 – +2.55) | 10 / 17 | -23.9 | +55.9 / -15.7 | 27.4 (14.5) | 50 | 39 | **TIDAK** |
| `T08` | 509 | 199 (39 %) | 12 | 55 % | 49 | +2.0 | -46.9 | **+0.85** | +0.74 (-0.16 – +2.10) | 8 / 17 | -21.0 | +54.6 / -26.4 | 22.7 (14.1) | 40 | 46 | **TIDAK** |
| `T10` | 1,024 | 228 (22 %) | 14 | 60 % | 52 | +4.5 | -42.3 | **+1.38** | +1.13 (+0.07 – +2.46) | 11 / 17 | -12.6 | +43.1 / -23.8 | 17.5 (11.6) | 40 | 44 | **TIDAK** |
| `T11` | 342 | 209 (61 %) | 13 | 54 % | 46 | +7.2 | -60.0 | **+1.36** | +1.06 (+0.17 – +2.07) | 13 / 17 | -42.4 | +11.1 / -19.0 | 22.1 (11.4) | 44 | 44 | **TIDAK** |
| `T12` | 426 | 179 (42 %) | 11 | 60 % | 45 | +6.0 | -59.4 | **+1.27** | +1.22 (+0.30 – +2.64) | 9 / 17 | -22.4 | +41.3 / -21.6 | 22.3 (15.0) | 46 | 40 | **TIDAK** |
| `TREND11` | 5,948 | 364 (6 %) | 22 | 32 % | 87 | +13.1 | -54.8 | **+2.87** | +1.79 (+0.71 – +3.47) | 12 / 17 | -35.0 | +54.8 / -26.1 | 21.8 (13.6) | 47 | 40 | **TIDAK** |
| `TREND11_TK40` | 5,948 | 526 (9 %) | 32 | 18 % | 82 | +8.8 | -68.8 | **+1.67** | +1.79 (+0.70 – +3.58) | 12 / 17 | -40.4 | +51.0 / -24.9 | 20.2 (13.6) | 25 | 23 | **TIDAK** |

## 3. Bacaan

- Lorong swing: 2 daripada 8 setup menambah di peringkat akaun; buku gabungan `SWING8` +2.32 % setahun pada MDD −10 % (jalur rawak p95 +1.80 %) → **menambah**; MDD tanpa dikecilkan -51.3 %.
- Lorong trend: 0 daripada 11 setup menambah; buku gabungan `TREND11` +2.87 % setahun pada MDD −10 % (jalur rawak p95 +3.47 %) → **TIDAK menambah**; MDD tanpa dikecilkan -54.8 %, tahun terburuk -35.0 %.
- `TREND11` dengan keluar "tiada kemajuan selepas 40 sesi": +1.67 % pada MDD −10 % (MDD asal -68.8 %).
- Semua angka "pada MDD −10 %" mengandaikan akaun hanya sebahagian dilaburkan; baki tunai tidak mendapat faedah.

## 4. Lorong trend pada saham Shariah (senarai semasa; maklumat)

| ID | Belian | Belian Shariah | Pelari besar %: semua → Shariah (rawak) | Dijual ≥ +30 % % | Menang % | Rugi ≥ 15 % % | Purata % |
|---|---|---|---|---|---|---|---|
| `T01` | 308 | 92 | 33.1 → 35.9 (20.2) | 35.9 | 55 | 33 | +19.9 |
| `T02` | 305 | 92 | 33.8 → 35.9 (20.1) | 37.0 | 55 | 32 | +20.3 |
| `T03` | 203 | 58 | 28.6 → 32.8 (23.6) | 34.5 | 59 | 28 | +17.7 |
| `T04` | 260 | 65 | 19.6 → 26.2 (14.5) | 38.5 | 51 | 40 | +14.4 |
| `T05` | 358 | 121 | 17.3 → 23.1 (11.8) | 22.3 | 49 | 37 | +11.3 |
| `T06` | 259 | 65 | 19.7 → 26.2 (14.5) | 38.5 | 51 | 40 | +14.4 |
| `T07` | 330 | 103 | 26.1 → 33.0 (17.6) | 40.8 | 65 | 25 | +19.9 |
| `T08` | 297 | 87 | 20.5 → 24.1 (14.3) | 28.7 | 46 | 46 | +6.6 |
| `T09` | 207 | 56 | 20.8 → 25.0 (12.5) | 26.8 | 46 | 36 | +7.6 |
| `T10` | 380 | 134 | 17.1 → 20.9 (10.8) | 21.6 | 43 | 39 | +7.5 |
| `T11` | 250 | 91 | 20.8 → 14.3 (9.9) | 17.6 | 41 | 52 | +2.5 |
| `T12` | 242 | 73 | 25.2 → 28.8 (17.5) | 26.0 | 47 | 44 | +11.7 |

- Cukup belian Shariah (≥ 30): 12 daripada 12 setup; kadar pelari besar pada saham Shariah mengatasi rawak bagi 12 daripadanya.

Kaveat: tiada saham delist (bias lebih besar bagi pegang 6 bulan); kumpulan B sudah dilihat; K3 lorong trend pendek (isyarat selepas ~April 2026 tiada); senarai Shariah bukan titik-masa. Backtest sahaja.
