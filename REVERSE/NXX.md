# NXX — keputusan ujian registry Nxx bahagian A

Pradaftar `REVERSE/SPEC_NXX.md` (komit `2e10efc`, pembetulan §10 `15a9d4b`), kod `REVERSE/step18_nxx.py` (`3aaab3a`, pembetulan `f470d80`). **Ketiga-tiganya dikomit sebelum keputusan ini dilihat.**

70 topeng MASUK x 4 keluar asas = **280 ujian**, pada **4,420,650 bar cair** dalam tingkap TAHAN (10,468,053 bar panel; 2012-2025). Kos penuh ditolak.

## 1. Semakan pemalsuan — dibaca dahulu (spec §6)

| | Larian ini | `KOMBINASI.md` | Beza |
|---|---|---|---|
| lift latih | +0.120 | +0.123 | -0.003 |
| lift tahan | +0.399 | +0.392 | +0.007 |
| n tahan | 28,089 | 28,117 | -28 |
| jangkaan tahan | +2.993% | +2.988% | +0.005 |

**LULUS** (toleransi +/-0.02). Dan kesemua empat asas dihasilkan semula sampai 3 desimal:

| Keluar | Asas tahan larian ini | `KOMBINASI.md` |
|---|---|---|
| X1 | -0.281% | -0.281% |
| X2 | +0.952% | +0.953% |
| X3 | +2.594% | +2.595% |
| X4 | +1.153% | +1.156% |

Dua set nombor bebas dihasilkan semula. Alat ini boleh dipercayai.

## 2. Keputusan tiga gate

| Gate | Syarat | Lulus | Jangkaan priori saya |
|---|---|---|---|
| 1 | lift positif KEDUA-DUA tingkap | **52 / 280** | 8-25 — **SALAH** |
| 2 | BH-FDR q <= 0.05, m=358 dipradaftar | **7** | 0-4 — **SALAH** |
| 3 | jangkaan selepas buang 5% teratas > 0 | **0** | 0 — betul |

**Jangkaan priori saya salah pada 2 daripada 3, kedua-duanya ke arah TERLALU RENDAH.** Ini kali KETIGA berturut-turut jangkaan priori saya salah dalam pradaftar (`SPEC_SILANG` §7, `SPEC_SISTEM` §7, dan ini). Pola itu sendiri satu dapatan: saya secara sistematik memandang rendah struktur statistik dalam ruang yang belum diukur, dan memandang tinggi keupayaannya bertahan ujian ekor.

**Keputusan pradaftar (spec §8): 0 lulus ketiga-tiga gate, jadi ruang MASUK registry Nxx DITUTUP.** Berhenti menambah baris MASUK. Keutamaan beralih kepada paksi GABUNGAN, SAIZ, ALAM dan INSTRUMEN.

## 3. Jangkaan keluarga saya TERBALIK

Spec §7: saya menjangka `MA` dan `KETAT` paling baik, `KALENDAR` dan `REJIM` paling teruk.

| Keluarga | Ujian | Lulus gate1 | % | Lulus gate2 |
|---|---|---|---|---|
| RSI | 28 | **18** | 64% | 6 |
| BB | 24 | **12** | 50% | 0 |
| KALENDAR | 24 | **4** | 17% | 0 |
| ADX | 28 | **4** | 14% | 1 |
| KETAT | 28 | **4** | 14% | 0 |
| VOLUM | 12 | **3** | 25% | 0 |
| POLA | 32 | **3** | 9% | 0 |
| PECAH | 32 | **3** | 9% | 0 |
| UNDUR | 16 | **1** | 6% | 0 |
| KEKUATAN | 12 | **0** | 0% | 0 |
| MA | 20 | **0** | 0% | 0 |
| TREND | 24 | **0** | 0% | 0 |

**`RSI` 64% dan `BB` 50% — kedua-duanya PEMBALIKAN MIN. `MA` 0/20, `TREND` 0/24, `KEKUATAN` 0/12 — kesemua keluarga IKUT-TREND memberi SIFAR.**

Itu songsang daripada jangkaan saya, dan ia tidak bercanggah dengan `N01` (silang MA + volum) yang masih satu-satunya lift positif dalam `KOMBINASI.md`: liftnya +0.392 adalah kecil, dan lima peraturan `MA` lain yang diuji di sini (`N06`-`N09`, `N76`) kesemuanya gagal. Satu silang MA yang berfungsi tidak menjadikan keluarga `MA` berfungsi.

## 4. Tujuh yang bertahan FDR

| Masuk | Peraturan | Keluar | n | lift latih | lift tahan | jangkaan | menang | p |
|---|---|---|---|---|---|---|---|---|
| `N75` | RSI14 < 40 tanpa penapis | X3 | 861,071 | +0.647 | **+1.587** | +4.181% | 32.5% | 3.5e-06 |
| `N75` | RSI14 < 40 tanpa penapis | X4 | 861,071 | +0.602 | **+1.515** | +2.668% | 36.1% | 8.5e-08 |
| `N115` | Holy Grail (Raschke) | X2 | 104,014 | +0.590 | **+1.464** | +2.416% | 38.9% | 1.0e-04 |
| `N17` | RSI14 silang naik 30 | X2 | 54,073 | +0.870 | **+1.264** | +2.216% | 38.8% | 2.8e-04 |
| `N75` | RSI14 < 40 tanpa penapis | X2 | 861,071 | +0.641 | **+0.773** | +1.724% | 38.1% | 7.1e-06 |
| `N16` | RSI2<10 tanpa penapis | X2 | 567,422 | +0.211 | **+0.305** | +1.257% | 38.1% | 2.0e-05 |
| `N16` | RSI2<10 tanpa penapis | X1 | 567,422 | +0.067 | **+0.193** | -0.088% | 62.4% | 9.7e-04 |

Lima daripada tujuh ialah `RSI` pembalikan min (`N75` rsi14 < 40 tiga kali, `N16` rsi2 < 10 dua kali), satu `N17` (rsi14 silang naik 30), satu `N115` (Holy Grail Raschke: adx14 > 30 + undur ke ema20 + tutup > tinggi semalam).

## 5. PERANGKAP yang gate saya sendiri tidak nampak

`N16` x `X1` **lulus gate 1 dan gate 2** dengan lift +0.193 dan kadar menang **62.4%** — tetapi jangkaan mutlaknya **-0.088%**. Ia MERUGIKAN.

Sebabnya asas `X1` sendiri ialah **-0.281%**. Lift positif atas asas NEGATIF masih merugikan. Gate saya menguji lift, bukan keuntungan mutlak, jadi ia melepaskan ini.

**Pembetulan reka bentuk untuk pradaftar seterusnya: tambah syarat `jangkaan mutlak > 0`.** Saya catat ini sebagai kecacatan spec, bukan sebagai dapatan — dan saya tidak mengubah gate selepas melihat keputusan.

Ia juga mengukur semula perangkap kadar menang `KOMBINASI.md` secara bebas: 62.4% menang, untung purata +4.79%, rugi purata -8.19%, jangkaan negatif.

## 6. Diagnostik ekor (POST-HOC, bukan gate)

Gate 3 memerlukan `tanpa5 > 0` **mutlak**. Tetapi asasnya sendiri negatif, jadi palang itu lebih tinggi daripada lift. Perbandingan yang saksama ialah `tanpa5` lawan asas keluar yang sama. **Ini diagnostik selepas fakta; ia TIDAK mengubah keputusan §2.**

| Masuk x Keluar | tanpa5 | asas tanpa5 | beza |
|---|---|---|---|
| `N19` x X3 | -1.228% | -2.303% | **+1.075** |
| `N37` x X3 | -1.973% | -2.303% | **+0.330** |
| `N115` x X3 | -1.956% | -2.303% | **+0.347** |
| `N19` x X2 | -1.207% | -1.277% | **+0.070** |
| `N20` x X3 | -0.544% | -2.303% | **+1.759** |
| `N75` x X3 | -2.393% | -2.303% | **-0.090** |
| `N64` x X3 | -2.760% | -2.303% | **-0.457** |
| `N115` x X4 | -2.190% | -2.158% | **-0.032** |
| `N17` x X3 | -1.727% | -2.303% | **+0.576** |
| `N19` x X4 | -2.388% | -2.158% | **-0.230** |

Dapatan diagnostik yang paling berguna: **`N19` (bawah jalur BB + rsi14 < 30) memperbaiki jangkaan terpangkas-ekor sebanyak +1.08 mata atas asasnya**, dan `N115` sebanyak +0.70. Itu bermakna kelebihannya **tidak** hidup sepenuhnya dalam ekor kanan — satu-satunya kes seperti itu yang pernah diukur dalam kajian ini. Sebaliknya `N75` menjadikan ekor **lebih buruk** (-0.09 hingga -0.26).

`N19` juga mempunyai lift tahan **+3.618** — sembilan kali lebih besar daripada `N01` (+0.392), lift terbesar yang pernah diukur dalam kajian ini. Tetapi `p = 0.032` tidak melepasi ambang BH `0.00097`, jadi ia **gagal gate 2** dan tiada dakwaan dibuat untuknya.

## 7. Apa yang ini TIDAK beritahu

- Paksi `CARA` dikunci pada `C01` (beli pada buka esok), jadi **kecacatan henti hari-0 (`KOLAM_EKOR.md` §4a) hadir dalam setiap nombor di atas**.
- Paksi `GABUNGAN` dikunci pada `GB01` (`DAN`). Setiap baris ialah penapis.
- `SAIZ`, `ALAM`, `KORELASI`, `IMBANG`, `INSTRUMEN` dikunci pada asas repo.
- Alam A02 tiada saham delist (bias survivorship), jadi tiada nombor mutlak di atas boleh dibaca sebagai jangkaan dunia nyata.
- Bahagian B pradaftar (26 KELUAR x 3 masuk tetap = 78 ujian) **belum dijalankan**.

## 8. Langkah seterusnya yang spec sudah tetapkan

Spec §8 menetapkan: lift positif tanpa gate 3 bermakna kelebihan nyata tetapi hidup dalam ekor kanan, dan kesimpulannya ialah **naikkan bilangan slot** (`SZ10`, `IS02`), bukan guna signal itu pada 8-10 slot.

Diagnostik §6 menambah satu nuansa yang spec tidak jangka: `N19` dan `N115` memperbaiki ekor terpangkas atas asasnya. Itu menjadikan `GB04` (agregat pangkat) dan `SZ10` (berat sama rata kolam penuh) lebih menarik, kerana kedua-duanya tidak bergantung pada menangkap ekor dengan 8-10 slot.
