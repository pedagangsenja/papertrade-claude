# SPEC_SILANG_AKHIR — pradaftar silang masuk-terbaik x keluar-terbaik

**Dikomit sebelum keputusan dilihat.** 31 Okt 2026 00:50 MY.

## 1. Soalan

`GABUNGAN.md` mendapati `GB02_atau3` dan `GB02_atau4` lulus kesemua empat gate — tetapi
**pada keluar `X3` sahaja**. `NXX_KELUAR.md` mendapati `X3` **bukan** keluar terbaik: asas
`X13` (+4.350%) dan `X15` (+3.706%) kedua-duanya lebih tinggi daripada `X3` (+2.594%).

Adakah masuk terbaik dan keluar terbaik **bergabung**, atau adakah kelebihan masuk hilang
apabila keluar ditukar?

Itu persoalan yang jelas dan belum diuji. `KOMBINASI.md` sudah menunjukkan bahawa lift
bergantung pada keluar (`K5` memberi lift pada `X3` dan `X2` tetapi negatif pada `X4`), jadi
tiada sebab menganggap ia bergabung.

## 2. Ujian — 8, dikunci

2 masuk (`GB02_atau3`, `GB02_atau4`) x 4 keluar (`X3`, `X13`, `X15`, `X17`) = **8 ujian**.

`X17` disertakan kerana ia keluar ketiga terbaik dalam bahagian B dan satu-satunya yang
berasaskan **kematian trend** (`adx14 < 20`) — relevan kepada gaya pengguna.

Asas setiap keluar dikira semula dalam larian yang sama supaya lift dibanding terhadap asas
keluar **yang sama**.

## 3. Gate

Sama seperti `SPEC_GABUNGAN` §3: (0) jangkaan mutlak tahan > 0; (1) lift positif kedua-dua
tingkap; (2) BH-FDR q <= 0.05 merentas **8**; (3) `tanpa5` > asas `tanpa5` keluar yang sama.

## 4. Jangkaan priori saya

| | Jangkaan |
|---|---|
| Lift bergabung (lift pada X13/X15 serupa dengan pada X3) | **TIDAK** — saya jangka lift mengecil pada keluar yang sudah lebih baik |
| Jangkaan mutlak tertinggi | `GB02_atau4` x `X13` |
| Lulus gate 3 | **1-3 daripada 8** |

Alasan jangkaan pertama: `X13` (keluar bila rsi14 > 70) sudah menangkap sebahagian besar
pergerakan naik, jadi ruang untuk signal masuk menambah nilai lebih kecil. Ini jangkaan
**penurunan pulangan bertambah**, bukan jangkaan kegagalan.

## 5. Had yang kekal

Paksi `CARA` kekal `C01`. Kolam 12 signal masih dipilih daripada data sama. Ujian portfolio
(8/40 slot lawan SPUS) masih **belum** dijalankan, jadi tiada dakwaan pulangan portfolio
dibuat daripada larian ini.
