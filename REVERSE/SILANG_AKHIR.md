# SILANG_AKHIR — masuk terbaik x keluar terbaik

Pradaftar `REVERSE/SPEC_SILANG_AKHIR.md` (komit `568a13f`), kod `REVERSE/step21_silang_akhir.py` (`58a42a8`). Kedua-duanya dikomit sebelum keputusan dilihat.

8 ujian: 2 masuk x 4 keluar, pada 4,420,650 bar cair tahan (2020-2025), kos penuh.

## 1. KESEMUA LAPAN LULUS KESEMUA EMPAT GATE

| Gate | Lulus | Jangkaan priori saya |
|---|---|---|
| 0+1 | **8 / 8** | — |
| 2 (BH-FDR m=8) | **8** | — |
| 3 (`tanpa5` > asas) | **8** | 1-3 — **SALAH, jauh** |

**Dan DUA daripada lapan lulus gate 3 versi ASAL juga** — `GB02_atau3` x `X13` (`tanpa5` **+2.858%**) dan `GB02_atau4` x `X13` (**+2.883%**). Itu bermakna kedua-dua gabungan `X13` **tidak bergantung** pada pelonggaran gate yang saya pradaftar dalam `SPEC_GABUNGAN` §3: ia melepasi palang mutlak `tanpa5 > 0` juga.

Enam yang lain lulus hanya pada versi "lebih baik daripada asas". Itu palang yang lebih rendah, dan saya nyatakan perbezaannya di sini supaya ia tidak dibaca sebagai sama.

## 2. Keputusan penuh

| Masuk | Keluar | n | lift latih | lift tahan | jangkaan | menang | untung | rugi | tanpa5 | asas tanpa5 | lawan asas | p |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `GB02_atau3` | **`X13`** | 195,681 | +1.818 | **+4.191** | **+8.541%** | 64.2% | +25.68% | -22.14% | **+2.858%** | +0.912% | +1.946 | 0.0068 |
| `GB02_atau4` | **`X13`** | 210,886 | +1.819 | **+4.095** | **+8.445%** | 64.2% | +25.49% | -22.12% | **+2.883%** | +0.912% | +1.971 | 0.0072 |
| `GB02_atau3` | **`X15`** | 195,681 | +0.643 | **+3.198** | **+6.903%** | 42.8% | +36.95% | -15.62% | **-1.235%** | -1.950% | +0.716 | 0.0057 |
| `GB02_atau4` | **`X15`** | 210,886 | +0.662 | **+3.104** | **+6.810%** | 42.9% | +36.59% | -15.55% | **-1.199%** | -1.950% | +0.751 | 0.0062 |
| `GB02_atau3` | **`X17`** | 195,681 | +1.688 | **+4.466** | **+6.321%** | 54.4% | +22.87% | -13.39% | **-1.548%** | -1.999% | +0.451 | 0.0036 |
| `GB02_atau4` | **`X17`** | 210,886 | +1.662 | **+4.200** | **+6.056%** | 54.8% | +22.07% | -13.32% | **-1.524%** | -1.999% | +0.475 | 0.0040 |
| `GB02_atau3` | **`X3`** | 195,681 | +0.592 | **+2.431** | **+5.025%** | 34.0% | +35.98% | -10.89% | **-1.733%** | -2.303% | +0.570 | 0.0171 |
| `GB02_atau4` | **`X3`** | 210,886 | +0.608 | **+2.351** | **+4.944%** | 34.1% | +35.43% | -10.84% | **-1.675%** | -2.303% | +0.628 | 0.0186 |

Asas (beli setiap bar, keluar sama):

| Keluar | jangkaan | menang | untung | rugi | tanpa5 |
|---|---|---|---|---|---|
| `X13` | +4.350% | 66.2% | +16.71% | -19.89% | +0.912% |
| `X15` | +3.706% | 41.1% | +27.41% | -12.82% | -1.950% |
| `X3` | +2.594% | 30.2% | +29.11% | -8.88% | -2.303% |
| `X17` | +1.855% | 45.0% | +12.18% | -6.59% | -1.999% |

## 3. Jangkaan priori saya SALAH, dan ke arah yang penting

Spec §4: saya jangka lift **TIDAK** bergabung — "saya jangka lift mengecil pada keluar yang sudah lebih baik, kerana `X13` sudah menangkap sebahagian besar pergerakan naik".

| | Lift tahan |
|---|---|
| `GB02_atau3` x `X3` | +2.431 |
| `GB02_atau3` x `X13` | **+4.191** |
| `GB02_atau3` x `X17` | **+4.466** |

**Lift BESAR, bukan mengecil.** Saya salah, dan arahnya bermakna: masuk dan keluar **bergabung secara positif** dalam alam ini. Itu dapatan, bukan andaian saya.

Saya juga ramal jangkaan tertinggi ialah `GB02_atau4` x `X13`; sebenarnya `GB02_atau3` x `X13` (+8.541% lawan +8.445%). Hampir, tetapi salah.

**Lima pradaftar, jangkaan priori saya salah dalam majoriti.** Saya rekod ini supaya penilaian saya pada ruang belum diukur tidak diberi berat yang ia tidak layak.

## 4. Pertukaran yang pengguna mesti pilih sendiri

Jangkaan tertinggi **bukan** pilihan terbaik secara automatik, kerana saiz kerugian berbeza jauh:

| Keluar | Jangkaan | Menang | Rugi purata | Untung purata |
|---|---|---|---|---|
| `X13` | +8.541% | 64.2% | **-22.14%** | +25.68% |
| `X15` | +6.903% | 42.8% | **-15.62%** | +36.95% |
| `X17` | +6.321% | 54.4% | **-13.39%** | +22.87% |

`X13` memberi jangkaan tertinggi tetapi **kerugian purata -22.1%** dan **tiada henti sama sekali** — keluar hanya berlaku bila `rsi14 > 70` atau ufuk 126 bar tamat. `X17` memberi jangkaan 2.2 mata lebih rendah tetapi kerugian purata **-13.4%**, hampir separuh.

Itu bukan soalan data. Ia soalan toleransi pengguna.

## 5. HAD — tidak berubah, dan masih menentukan

1. **Ini jangkaan SETIAP DAGANGAN atas 195,681 dagangan, BUKAN prestasi portfolio.** `KOLAM_EKOR.md` sudah mengukur bahawa 8-10 slot mendarat dekat **median**, bukan min. Ujian portfolio (8 dan 40 slot, 20 benih, lawan SPUS pada kedua-dua konvensyen) **BELUM dijalankan**, dan tiada dakwaan pulangan portfolio boleh dibuat sebelum itu.
2. **Kolam 12 signal dipilih daripada data yang sama**, jadi keputusan bersyarat padanya.
3. **Paksi `CARA` kekal `C01`** (beli pada buka esok), jadi kecacatan henti hari-0 (`KOLAM_EKOR.md` §4a: 421/1,770 posisi, menang 0.00%) hadir dalam setiap nombor.
4. **Alam A02 tiada saham delist** = bias survivorship. Ia memihak kepada SEMUA keputusan termasuk asas, jadi lift kurang terjejas daripada nombor mutlak — tetapi tiada nombor mutlak di atas boleh dibaca sebagai jangkaan dunia nyata.
5. Ufuk 126 bar. Kos: komisen 0.1% setiap sisi + slippage.
