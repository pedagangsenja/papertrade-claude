# PEGANG_SLOT — lengkung tempoh pegangan dan lengkung slot

Pradaftar: `REVERSE/SPEC_PEGANG_SLOT.md` (komit `3370a4f`, sebelum larian).
Skrip: `REVERSE/step24_pegang_slot.py` · Data: `REVERSE/pegang_slot.csv`,
`REVERSE/pegang_slot_ringkas.csv`

320 konfigurasi (2 masuk × 8 slot × 2 keluar × 5 had pegang × 2 urutan), `U01` 20 benih →
**3,360 larian**. Alam A02 cair, kos penuh dua sisi, sauh HARIAN, `SZ01` berat sama rata
`1/slot`, tiada margin. Masa larian 1 jam 42 minit.

## Keputusan: T1 **0**, T3 **0**, lulus keempat-empat gate **0 / 320**

**SPUS 2020–2025: CAGR 17.95% · MDD −26.82% · nisbah 0.669**

| Gate | | |
|---|---|---|
| P1 | CAGR median > SPUS | **29/320** |
| P2 | MDD median ≥ SPUS | **24/320** |
| P3 | CAGR median > persentil-95 kawalan RAWAK | **101/320** |
| P4 | nisbah > 0.669 | **9/320** |
| | **lulus semua** | **0/320** |
| **T1** | CAGR > 17.95% **DAN** MDD ≥ −26.82% | **0/320** |
| **T3** | CAGR ≥ 15% **DAN** MDD ≥ −15% | **0/320** |

`P1` dan `P2` masing-masing lulus 29 dan 24 kali, tetapi kedua-dua set itu **tidak
bertindih langsung**. Itu keseluruhan ceritanya: setiap tetapan yang menaikkan pulangan
menaikkan MDD dalam kadar yang lebih besar.

**Cabang mengikut `STRATEGI.md` §4: E1 gagal T1/T3 → teruskan ke E2.**

## Kawalan regresi lulus TEPAT

Keempat-empat sel bertindih dengan `PORTFOLIO_N.md` (`GB02_atau3` × `U01` × had `tiada`)
dihasilkan semula **identik sampai 4 titik perpuluhan**:

| slot | keluar | step22 CAGR / MDD | step24 CAGR / MDD | beza |
|---:|---|---|---|---|
| 8 | X13 | 9.4041 / −44.8187 | 9.4041 / −44.8187 | 0.0000 |
| 8 | X15 | 8.3176 / −54.9928 | 8.3176 / −54.9928 | 0.0000 |
| 40 | X13 | 13.9236 / −38.3817 | 13.9236 / −38.3817 | 0.0000 |
| 40 | X15 | 11.6877 / −45.5821 | 11.6877 / −45.5821 | 0.0000 |

Had tempoh pegangan ialah satu-satunya perkara yang berubah, dan ia disahkan oleh angka,
bukan oleh pembacaan kod.

## Q1 — had pegangan: jangkaan priori saya SALAH, dan salah dengan banyak

Saya menulis dalam spec §6: *"Had 21–42 bar ialah kes sebenar. Saya jangka ia **kalah**,
tetapi dengan jurang kecil (dalam 3 mata CAGR)."*

**Had pegangan mengalahkan "tiada had" dalam 72 daripada 128 sel**, dan jurang terbaiknya
bukan 3 mata tetapi **+27.15 mata**:

| konfigurasi | tiada had | had 42 bar | beza |
|---|---:|---:|---:|
| `X15` · 80 slot · `U01` | +12.09% | **+39.24%** | **+27.15** |
| `X13` · 80 slot · `U01` | +13.97% | +38.35% | +24.38 |
| `X13` · 160 slot · `U01` | +12.24% | +29.42% | +17.18 |

Had **42 bar** ialah yang terbaik pada kebanyakan sel — bukan 21, bukan 63. Itu **8–9
minggu**, iaitu di luar julat swing 3–30 hari yang repo takrifkan, tetapi separuh daripada
~85 bar yang setiap konfigurasi menang sebelum ini pegang.

Arah yang saya ramalkan (had memotong pemenang, jadi ia merugikan) memang berlaku pada
**had 10 bar**, tepat seperti `X29` meramalkan — tetapi hanya di sana, dan sebabnya boleh
dibaca terus daripada lajur kos:

| had | pulangan/dagangan | pusingan/slot/tahun | seretan kos/tahun |
|---:|---:|---:|---:|
| 10 bar | +2.24% | 28.1 | **14.25 mata** |
| 21 bar | +3.71% | 14.1 | 7.17 mata |
| 42 bar | **+9.43%** | 7.5 | 3.78 mata |
| 63 bar | +10.10% | 5.7 | 2.94 mata |

Pada 28 pusingan setahun, kos memakan **14.25 mata peratus setahun**. Itu bukan anggaran —
ia dikira daripada kos sebenar setiap dagangan dalam simulasi. Had 10 bar masih memberi
+31.15% CAGR pada 80 slot **selepas** membayar 14 mata itu, yang bermakna kelebihan kasarnya
besar; tetapi MDD-nya **−70.18%** dan ia gagal setiap gate.

**Nota kejujuran pada lajur `pulangan/dagangan`:** lorong tanpa had meninggalkan banyak
posisi masih terbuka pada hujung tingkap, dan posisi itu tidak dikira. Jadi
`pulangan/dagangan` lorong "tiada had" dicensor ke atas-bawah dan **tidak boleh** dibanding
terus dengan lorong berhad. CAGR dan MDD tidak mengalami masalah itu; guna kedua-dua itu.

## Q2 — lengkung slot MEMUNCAK dan MEROSOT; `SZ10` bukan jawapannya

Jangkaan priori saya: *"terus menaik sampai ~160 kemudian rata."* Separuh betul — ia menaik,
tetapi ia **memuncak pada 80–160 dan merosot selepas itu**, bukan rata.

`GB02_atau3` · `X13` · had 42 · `U01` (CAGR / MDD):

| slot | 8 | 20 | 40 | **80** | 160 | 320 | 640 | 1280 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| CAGR | +14.90 | +12.61 | +18.83 | **+38.35** | +29.42 | +22.00 | +14.48 | +11.53 |
| MDD | −52.0 | −44.8 | −43.3 | −44.7 | −70.8 | −57.7 | −44.0 | −40.3 |

Pada slot **1280** lorong berhad sudah **melepasi kapasiti kolam** (753 posisi serentak,
diukur dalam spec §3.1), jadi itulah `SZ10` — berat sama rata atas kolam penuh — diukur
**terus**. Ia memberi **+9.19% hingga +16.71%** dengan MDD −37% hingga −43%. Lebih rendah
daripada puncak pada setiap paksi. **`SZ10` DITOLAK**, dan ia adalah satu daripada dua calon
terakhir yang `CLAUDE.md` senaraikan.

Lengkung monoton yang `PORTFOLIO_N.md` dan `PEMBINAAN.md` lihat ialah **bahagian menaik
sahaja** — kedua-duanya berhenti pada 40 slot, sebelum puncak.

## Dapatan yang paling berguna: hingar pemilihan ialah separuh daripada dapatan

Sel terbaik, `X15` · 80 slot · had 42 · `U01`, mempunyai median **+39.24%** — dan jalur 20
benihnya ialah **p5 +12.22% hingga p95 +55.04% = 42.8 mata peratus**.

`KEPEKATAN_BENIH.md` mengukur hingar pemilihan **17.3 mata/tahun** pada 8 slot. Di sini,
pada 80 slot dengan had pegangan, ia **42.8 mata**. **Sesiapa yang melaporkan 39.24%
melaporkan satu cabutan daripada awan, bukan prestasi.**

Jalur itu **mengecil** apabila slot bertambah: pada 160 slot sel yang sama memberi p5 16.83
– p95 33.14 = 16.3 mata. Jadi menambah slot membeli **kebolehpercayaan**, bukan pulangan —
dan itu dapatan yang boleh diguna, berbeza daripada CAGR puncak yang tidak boleh.

## `U08` memusnahkan ekor pada slot rendah, dan sebabnya boleh dibaca

| `X13` · had 42 | 8 | 20 | 40 | 80 | 160 | 320 |
|---|---:|---:|---:|---:|---:|---:|
| `U01` rawak | +14.90 | +12.61 | +18.83 | **+38.35** | +29.42 | +22.00 |
| `U08` ATR% menaik | +3.99 | +7.39 | +6.76 | **+5.81** | +23.59 | +18.68 |

Pada 80 slot jurangnya **32.5 mata**. `U08` membeli nama paling kurang bergoyang dahulu,
dan nama paling kurang bergoyang ialah tepat nama yang **tiada ekor kanan** — `KOLAM_EKOR.md`
mengukur 5% teratas = 63.7% daripada jumlah pulangan kolam. `U08` menapis keluar bahagian
yang membayar.

Jurang itu **hilang** pada 160+ slot kerana pada bilangan slot itu `U08` terpaksa mengambil
nama ber-ATR tinggi juga. Ini mengesahkan semula mekanisme `SETUP.md` pada paksi yang
berbeza: apa-apa yang **membuang** calon membuang ekor.

Namun `U08` ialah lever MDD yang `PORTFOLIO_N.md` kenal pasti, dan ia kekal begitu: lapan
daripada sembilan sel yang melepasi `P4` memakai `U08`, dan MDD paling cetek dalam seluruh
larian (**−12.14%**) ialah `RAWAK` · 8 slot · `X15` · tiada had · `U08` — baris yang sama
yang `PORTFOLIO_N.md` temui, dihasilkan semula.

## Jangkaan priori lawan keputusan

| | Saya jangka | Berlaku | |
|---|---|---|---|
| Had 10 bar | kalah jelas | kalah pada MDD, tetapi **+31% CAGR** pada 80 slot | separa |
| Had 21–42 bar | **kalah**, jurang < 3 mata | **menang 72/128 sel**, jurang +27.15 mata | **salah** |
| Had terbaik | 42 bar dengan `X15` | **42 bar dengan `X15`** | **betul** |
| Lengkung slot | menaik ke ~160 kemudian **rata** | memuncak 80–160 kemudian **merosot** | separa |
| `P3` gagal pada slot tinggi | ya | **tidak** — `P3` lulus 101/320 | **salah** |
| `SZ10` lulus P1+P2 | **ya**, jangkaan paling kuat saya | **tidak**, 0 | **salah** |

Tiga salah, dua separa, satu betul. Corak yang sama seperti empat pradaftar terdahulu, dan
kali ini arah kesilapan **bertukar**: saya memandang rendah kesan had pegangan dan memandang
tinggi `SZ10`.

## Had

- **Hingar pemilihan 42.8 mata** pada sel terbaik. Tiada nombor tunggal dalam laporan ini
  boleh dirapatkan kepada lebih daripada ±20 mata tanpa lebih banyak benih.
- Alam A02 **tiada saham delist**; lorong slot tinggi condong **lebih banyak** kerana ia
  memegang lebih banyak saham ekor.
- Kolam 12 signal `GB02` dan keluar `X13`/`X15` dipilih daripada data yang **sama**.
  Bersyarat.
- Slot 160–1280 mengandaikan kecairan menyerap saiz pesanan; model kos melaraskan slippage
  ikut nilai dagangan 20 hari tetapi **tidak** memodelkan impak pasaran. Pada 1,280 posisi
  serentak andaian itu lemah.
- Paksi `CARA` kekal `C01`.
- `U08` ialah satu cabutan tentu (nb = 1) — tiada jalur, jadi `P3` baginya ialah satu cabutan
  lawan satu jalur.
