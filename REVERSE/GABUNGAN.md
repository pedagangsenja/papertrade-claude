# GABUNGAN — keputusan paksi GABUNGAN

Pradaftar `REVERSE/SPEC_GABUNGAN.md` (komit `86ad37e`, pindaan §7), kod `REVERSE/step20_gabungan.py` (`a6088e4`). Kedua-duanya dikomit sebelum keputusan dilihat.

14 konfigurasi pada keluar `X3` (henti 2xATR, pegang 63), 4,420,650 bar cair tahan.

## 1. Gate — DUA LULUS KESEMUA EMPAT

| Gate | Syarat | Lulus | Jangkaan priori saya |
|---|---|---|---|
| 0 | jangkaan mutlak tahan > 0 | **14 / 14** | — |
| 1 | lift positif dua tingkap | **13** | — |
| 2 | BH-FDR q <= 0.05, m=14 | **8** | — |
| 3 | tanpa5 > asas (-2.303%) | **2** | 2-5 — **betul** |

**Ini kali pertama dalam seluruh kajian ini mana-mana konfigurasi lulus setiap gate yang dipradaftar.** Bahagian A: 0 daripada 280. Bahagian B: 0 daripada 69. Di sini: 2 daripada 14.

## 2. Dua yang lulus

| Konfigurasi | n | lift latih | lift tahan | jangkaan tahan | menang | tanpa5 | lawan asas | p |
|---|---|---|---|---|---|---|---|---|
| **`GB02_atau4`** | 210,886 | +0.608 | **+2.351** | **+4.944%** | 34.1% | -1.675% | **+0.628** | 0.0186 |
| **`GB02_atau3`** | 195,681 | +0.592 | **+2.431** | **+5.025%** | 34.0% | -1.733% | **+0.570** | 0.0171 |

Asas (beli setiap bar, keluar `X3`): jangkaan **+2.594%**, tanpa5 **-2.303%**, menang 30.2%.

## 3. Apa sebenarnya `GB02_atau4`

Kesatuan EMPAT peraturan. Beli jika **mana-mana satu** menyala — bukan kesemuanya.

| ID | Nama | Peraturan | Keluarga |
|---|---|---|---|
| `N19` | Bawah jalur BB + RSI<30 | `bb_pctb < 0 DAN rsi14 < 30` | BB |
| `N37` | Gap and go | `gap_and_go` | PECAH |
| `N115` | Holy Grail (Raschke) | `adx14 > 30 DAN undur menyentuh ema20 DAN tutup > tinggi bar sebelum` | ADX |
| `N20` | Kembali masuk jalur + RSI silang 30 | `bb_pctb[-1] < 0 DAN bb_pctb > 0 DAN rsi14 silang naik 30` | BB |

`GB02_atau3` ialah tiga pertama (tanpa `N20`).

**Dua pembalikan min (`N19`, `N20`) dan dua momentum (`N37` gap-and-go, `N115` Holy Grail Raschke).** Kepelbagaian merentas KELUARGA signal, diambil secara kesatuan, mengalahkan mana-mana satu daripadanya dan mengalahkan persilangan mereka.

## 4. Mengapa kesatuan berfungsi dan persilangan tidak

`SETUP.md` mengukur 0 daripada 598 penapis dengan lift positif, dan sebabnya struktur: setiap syarat `DAN` membuang bar, dan kerana taburan saham tunggal terpencong kanan, membuang bar terutamanya membuang peluang pada ekor kanan.

Kesatuan melakukan yang bertentangan. Ia **menambah** bar. Dan kesannya kelihatan tepat di tempat yang diramalkan — **lajur `tanpa5`**:

| Konfigurasi | tanpa5 | lawan asas -2.303% |
|---|---|---|
| `GB02_atau3` | -1.733% | +0.570 |
| `GB02_atau4` | -1.675% | +0.628 |
| `GB02_atau6` | -2.381% | -0.078 |
| `GB02_atau8` | -2.468% | -0.165 |
| `GB03_undi2` | -2.367% | -0.064 |
| `GB04_pangkat5` | -2.869% | -0.566 |
| `GB04_pangkat10` | -2.853% | -0.550 |
| `GB04_pangkat20` | -2.628% | -0.325 |

Kesatuan kecil (3-4 signal) memperbaiki ekor. Kesatuan besar (6-8) mencairkannya semula ke arah asas. Agregat pangkat (`GB04`) **memburukkan** ekor pada setiap persentil — jangkaan priori saya mengatakan `GB04` paling menjanjikan, dan itu **SALAH**.

## 5. Jangkaan priori saya — kali pertama sebahagian besarnya betul

| Jangkaan | Keputusan |
|---|---|
| `GB02` lift lebih rendah daripada ahli terbaiknya tetapi `tanpa5` lebih baik | **BETUL** — `atau2` lift +3.299 lawan `N19` sendiri +3.618; dan `tanpa5` lebih baik |
| `GB03` terbaik pada k=2 | **SALAH** — terbaik k=4 (+3.036), k=2 paling lemah (+0.882) |
| `GB04` blok paling menjanjikan, persentil 5% lift tertinggi | **SALAH** — `GB02` yang terbaik; dan dalam `GB04` persentil **1%** tertinggi, bukan 5% |
| `GB08` lift kecil +0.1 hingga +0.5 | **BETUL** — +0.098, tetapi p=0.126 gagal gate 2 |
| gate 3 lulus 2-5 daripada 14 | **BETUL** — 2 |

Dua betul, dua salah, satu sebahagian. Selepas empat pradaftar dengan jangkaan yang salah, ini yang pertama di mana mekanisme yang saya ramalkan (kesatuan memperbaiki ekor) **memang berlaku**.

## 6. HAD — baca sebelum menggunakan apa-apa di atas

1. **`tanpa5` masih NEGATIF** (-1.675%). Gate 3 dipradaftar sebagai "lebih baik daripada asas", bukan "> 0", dan sebabnya diberi dalam spec §3. Jadi kelebihan itu masih sebahagian besarnya dalam ekor kanan — cuma kurang daripada apa-apa yang pernah diukur.
2. **Kolam 12 signal dipilih daripada data yang sama** (pemenang gate 1 bahagian A). Jadi keputusan ini **bersyarat** pada kolam itu. Ia bukan pemilihan baharu, tetapi ia juga bukan bebas.
3. **Ini jangkaan SETIAP DAGANGAN atas 210,886 dagangan**, bukan prestasi portfolio. `KOLAM_EKOR.md` sudah mengukur bahawa 8-10 slot mendarat dekat **median**, bukan min. Ujian portfolio (8 dan 40 slot, 20 benih, lawan SPUS) **BELUM dijalankan** dan tiada dakwaan pulangan boleh dibuat sebelum itu.
4. Paksi `CARA` kekal `C01`, jadi kecacatan henti hari-0 hadir dalam setiap nombor.
5. Diuji pada keluar `X3` sahaja. Bahagian B mengukur `X13` dan `X15` sebagai keluar asas yang **lebih baik** — tetapi gabungan `GB02_atau4` dengan `X13` **BELUM DIUJI**. Itu ujian seterusnya yang paling jelas, bukan keputusan.
6. Alam A02 tiada saham delist.
