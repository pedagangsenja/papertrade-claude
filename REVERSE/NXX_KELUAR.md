# NXX_KELUAR — keputusan bahagian B pradaftar SPEC_NXX

Pradaftar `REVERSE/SPEC_NXX.md` §3 + §11 (komit `5acbd15`), kod `REVERSE/step19_nxx_keluar.py` (`6d1801a`). Kedua-duanya dikomit sebelum keputusan dilihat.

**23 keluar x 3 masuk tetap = 69 ujian**, pada 4,420,650 bar cair tahan (2020-2025). Ufuk maksimum 126 bar. Kos penuh ditolak.

## 1. Gate

| Gate | Syarat | Lulus | Jangkaan priori saya |
|---|---|---|---|
| 0+1 | jangkaan mutlak > 0 DAN lift positif dua tingkap | **24 / 46** | 15-35 — **betul** |
| 2 | BH-FDR q <= 0.05, m=349 | **0** | 3-10 — **SALAH** |
| 3 | tanpa5 > 0 | **0** | 0-2 — betul |

Lift tertinggi ialah `N19` x `X13` (+6.94) dengan p = 0.0036, tetapi ambang BH pada m=349 jauh lebih ketat, jadi **tiada yang bertahan**. Keputusan: paksi KELUAR juga tidak menghasilkan signal yang bertahan pembetulan pelbagai ujian.

**Saya sengaja menyesuaikan jangkaan priori ke ATAS untuk bahagian B** kerana saya salah tiga kali berturut ke arah bawah. Kali ini saya salah ke **ATAS** pada gate 2. Pelajarannya bukan "sesuaikan ke atas" — ia bahawa **jangkaan priori saya tidak bermaklumat** dan patut diabaikan memihak kepada ukuran.

## 2. DAPATAN UTAMA: pilihan keluar mengubah jangkaan ~5 mata, pilihan masuk ~0.4 mata

Asas setiap keluar bermakna **tiada penapis masuk sama sekali** — beli setiap bar, keluar ikut peraturan itu.

| # | Keluar | Peraturan | n | Jangkaan tahan | Menang |
|---|---|---|---|---|---|
| 1 | `X13` | keluar bila rsi14 > 70 | 4,420,650 | **+4.350%** | 66.2% |
| 2 | `X15` | ekori Chandelier 4 x ATR14 | 4,420,650 | **+3.706%** | 41.1% |
| 3 | `X17` | keluar bila adx14 < 20 | 4,420,650 | **+1.855%** | 45.0% |
| 4 | `X14` | keluar bila rsi14 silang naik 50 | 4,420,650 | **+0.991%** | 53.9% |
| 5 | `X12` | henti pada jalur bawah BB(20,2) | 4,143,657 | **+0.961%** | 27.5% |
| 6 | `X36` | keluar selepas DUA tutup bawah ma50 | 4,420,650 | **+0.892%** | 35.7% |
| 7 | `X41` | henti pada rendah hari masuk | 4,138,081 | **+0.839%** | 6.4% |
| 8 | `X37` | henti bawah rendah hari masuk; gagal jika tutup < buka hari masuk | 4,138,081 | **+0.839%** | 6.4% |
| 9 | `X16` | keluar bila supertrend berbalik | 4,420,650 | **+0.718%** | 37.4% |
| 10 | `X29` | pegang tetap 10 bar | 4,420,650 | **+0.294%** | 48.5% |
| 11 | `X30` | keluar bila macd < macd_sig | 4,420,650 | **+0.238%** | 37.5% |
| 12 | `X27` | sasaran limit +3% | 4,420,650 | **+0.233%** | 91.5% |
| 13 | `X08` | keluar bila rsi2 > 80 | 4,420,650 | **+0.098%** | 61.5% |
| 14 | `X05` | keluar bila tutup > jalur tengah BB(20) = ma20 | 4,420,650 | **+0.030%** | 54.3% |
| 15 | `X10` | sasaran untung 2% tetap | 4,420,650 | **-0.023%** | 94.1% |
| 16 | `X19` | keluar bila tutup < ema21 | 4,420,650 | **-0.084%** | 33.6% |
| 17 | `X09` | keluar bila rsi2 > 65 | 4,420,650 | **-0.101%** | 56.1% |
| 18 | `X26` | ekori 4% peratus tetap | 4,420,650 | **-0.126%** | 34.8% |
| 19 | `X07` | keluar bila rsi2 > 60 | 4,420,650 | **-0.172%** | 54.5% |
| 20 | `X25` | henti 1% bawah ema21 | 2,638,445 | **-0.297%** | 22.5% |
| 21 | `X28` | sasaran +4% atau tutup < ma50 | 4,420,650 | **-0.436%** | 52.6% |
| 22 | `X33` | keluar pada tutup sesi masuk | 4,420,650 | **-0.500%** | 39.0% |
| 23 | `X18` | henti pada rendah 20 hari | 4,300,516 | **-0.647%** | 23.9% |

**Sebaran: 4.997 mata peratus** (`X13` +4.350% hingga `X18` -0.647%), daripada pilihan keluar SAHAJA.

Bandingkan: lift masuk terbaik yang pernah bertahan dua tingkap ialah `N01` **+0.392 mata** (`KOMBINASI.md`). Jadi **pilihan keluar kira-kira 12x lebih berpengaruh daripada pilihan masuk** dalam alam ini.

## 3. Tiga keluar terbaik berkongsi satu sifat

| Keluar | Peraturan | Jenis |
|---|---|---|
| `X13` +4.350% | keluar bila `rsi14 > 70` | keluar atas KEKUATAN |
| `X15` +3.706% | ekori Chandelier 4 x ATR14 | ekori, tiada sasaran |
| `X17` +1.855% | keluar bila `adx14 < 20` | keluar bila TREND MATI |

Ketiga-tiganya **"pegang sampai momentum habis"**. Tiada satu pun ialah sasaran untung, dan tiada satu pun ialah henti ketat.

Sebaliknya dua terburuk ialah `X18` (henti pada rendah 20 hari, -0.647%) dan `X33` (keluar pada tutup sesi masuk, -0.500%) — kedua-duanya memotong pegangan awal.

**Ramalan saya terbalik:** saya ramal `X29` (pegang 10 bar) dan `X33` terbaik. `X29` kedudukan 10/23, `X33` kedudukan **22/23**.

## 4. Perangkap kadar menang, kali KEEMPAT secara bebas

| Keluar | Menang | Jangkaan |
|---|---|---|
| `X10` sasaran 2% tetap | **94.1%** | **-0.023%** |
| `X27` sasaran +3% | **91.5%** | +0.233% |
| `X13` keluar rsi14 > 70 | 66.2% | **+4.350%** |
| `X15` ekori Chandelier | 41.1% | **+3.706%** |

`X10` menang 94 kali daripada 100 dan masih merugikan. `X15` menang 41 kali dan memberi +3.7%.

## 5. Dua pepijat yang dibetulkan sebelum keputusan ini

Larian B pertama dibuang sepenuhnya. Sebabnya direkod dalam komit `6d1801a`:

1. **Harga keluar merentas ticker** — `o[kk+1]` pada bar terakhir ticker mengambil buka ticker SETERUSNYA. Dagangan $25 "keluar" pada $1,950,000. Memberi +104% setiap dagangan.
2. **Henti berasaskan paras boleh berada DI ATAS harga masuk** — `X25` = henti 1% bawah `ema21`; apabila masuk jauh di bawah MA (`N19` terlebih jual), paras itu **14.3% di atas masuk pada 99.8% dagangan**, jadi `rendah <= paras` benar serta-merta dan kod "menjual" di atas masuk. Ia melaporkan `N19` x `X25` dengan kadar menang **99.76%** dan jangkaan **+18.52%**, lulus ketiga-tiga gate. **Kedua-dua kelulusan gate 3 larian pertama ialah artifak.**

Pembetulan: henti mesti di BAWAH masuk; jika tidak, keluar itu tidak sah untuk dagangan itu dan pulangannya dikecualikan. Itu sebab `n` bagi `X12`, `X18`, `X25`, `X37`, `X41` kurang daripada 4,420,650 dalam jadual §2.

**Nota kaedah:** ujian asap saya menguji asas sahaja, dan `X25` pada asas memberi +2.273% yang kelihatan waras. Pepijat hanya nyata pada GABUNGAN masuk+keluar. Ujian asap mesti merangkumi kombinasi, bukan komponen.

## 6. Had

- Paksi `CARA` kekal `C01`, jadi kecacatan henti hari-0 (`KOLAM_EKOR.md` §4a) hadir.
- Ufuk 126 bar; bahagian A guna 63 bar bagi `X3`, jadi A dan B tidak boleh dibanding terus.
- Dua masuk tetap sahaja (`N115`, `N19`) selain asas.
- Alam A02 tiada saham delist.
- `X20`, `X31`, `X32` dikeluarkan (bukan keluar per-dagangan) — spec §11.
