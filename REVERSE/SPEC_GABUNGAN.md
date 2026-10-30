# SPEC_GABUNGAN — pradaftar paksi GABUNGAN (GB02 · GB03 · GB04 · GB08)

**Dikomit sebelum sebarang keputusan dilihat.** 31 Okt 2026 00:30 MY. Permintaan pengguna:
data backtest lengkap sebelum 6 pagi, dan keputusan akhir ialah kombinasi signal.

## 1. Mengapa paksi ini, bukan baris MASUK lagi

`NXX.md` (bahagian A) menutup ruang MASUK: 280 ujian, 0 lulus ketiga-tiga gate. Dan sebabnya
**struktur**: setiap baris MASUK ialah syarat `DAN` = penapis, setiap penapis membuang bar, dan
`SETUP.md` sudah ukur bahawa membuang bar terutamanya membuang peluang pada ekor kanan.

Paksi `GABUNGAN` ialah **operasi**, bukan signal. Ia menukar cara signal disatukan:

| ID | Operasi | Kesan pada bilangan bar |
|---|---|---|
| `GB01` | `DAN` (persilangan) — asas semua 280 ujian A | **membuang** |
| `GB02` | `ATAU` (kesatuan) | **menambah** |
| `GB03` | undi k-daripada-n | antara dua |
| `GB04` | agregat pangkat -> satu skor | **tidak membuang apa-apa** |
| `GB08` | penapis terbalik (buang yang terbukti rugi) | membuang ekor KIRI sahaja |

## 2. Reka bentuk

**Kolam signal:** 12 MASUK yang lulus gate 1 bahagian A dengan lift tahan tertinggi, DITETAPKAN
di sini daripada `nxx.csv` sebelum larian ini:

```
N19 N37 N115 N20 N75 N64 N17 N42 N73 N16 N51 N54
```

Ini bukan pemilihan baharu — ia pemenang gate 1 yang sudah dilaporkan. Memilihnya semula
daripada data yang sama **tidak** menambah ujian berganda baharu kepada pemilihan MASUK,
tetapi ia **memang** bermakna kolam ini dipilih pada data yang sama, jadi keputusan GABUNGAN
mesti dibaca sebagai **bersyarat** pada kolam itu.

**Ujian (semuanya pada keluar `X3` = henti 2xATR, pegang 63, kerana `KOMBINASI.md` mengukurnya
sebagai keluar asas terbaik):**

| Blok | Konfigurasi | Ujian |
|---|---|---|
| `GB01` | setiap 12 secara individu (rujukan, sudah dilapor) | 12 |
| `GB02` | kesatuan: 2 teratas, 3, 4, 6, 8, 12 | 6 |
| `GB03` | undi k daripada 12, k = 2, 3, 4 | 3 |
| `GB04` | agregat pangkat 12 skor, ambil persentil teratas 1%, 5%, 10%, 20% | 4 |
| `GB08` | asas tanpa penapis TOLAK kesatuan 25 kaedah Mxx terbukti negatif | 1 |
| | **Jumlah ujian baharu** | **14** |

`GB08` menggunakan senarai yang **sudah ada**: 25 kaedah Mxx yang `KAEDAH_TERBAIK.md` buktikan
NEGATIF pada BH-FDR q <= 0.05. Topengnya ialah "mana-mana daripada 25 itu menyala" dan ujiannya
ialah membuangnya daripada alam.

## 3. Gate (empat, bukan tiga)

Gate 0 dibawa daripada `SPEC_NXX` §11 selepas bahagian A mendedahkan kecacatannya:

0. **jangkaan mutlak tahan > 0**
1. **lift positif KEDUA-DUA tingkap** terhadap asas `X3` yang sama
2. **BH-FDR q <= 0.05 merentas 14** (bukan 358 — ini pradaftar berasingan dengan 14 ujian)
3. **jangkaan selepas buang 5% teratas > asas tanpa5 `X3`** (-2.303%)

**Gate 3 diubah secara sengaja daripada `> 0` kepada `> asas`.** Sebabnya diberi dalam
`NXX.md` §6: asas sendiri -2.303%, jadi `> 0` ialah palang yang lebih tinggi daripada lift dan
ia menolak apa-apa yang memperbaiki ekor tanpa menjadikannya positif. Perubahan ini dibuat
**sebelum** larian ini dan dinyatakan di sini; ia **tidak** digunakan ke belakang pada
bahagian A yang sudah dilaporkan.

## 4. Jangkaan priori saya

Jangkaan saya salah tiga kali berturut-turut. Saya rekod lagi:

| Blok | Jangkaan |
|---|---|
| `GB02` kesatuan | lift **lebih rendah** daripada ahli terbaiknya, tetapi `tanpa5` **lebih baik** |
| `GB03` undi | terbaik pada k = 2 |
| `GB04` agregat pangkat | **blok paling menjanjikan**; persentil 5% memberi lift tertinggi |
| `GB08` penapis terbalik | lift kecil positif (+0.1 hingga +0.5) dan `tanpa5` lebih baik daripada asas |
| Gate 3 lulus | **2-5 daripada 14** |

Alasan: kesatuan mencairkan purata tetapi menambah kepelbagaian ekor; agregat pangkat tidak
membuang bar sama sekali, jadi ia satu-satunya yang boleh mengekalkan ekor sambil memilih.

## 5. Apa yang akan disimpulkan

| Keputusan | Kesimpulan |
|---|---|
| `GB04` atau `GB02` lulus gate 3 | Arah yang betul ialah **operasi**, bukan signal. Deliverable pengguna dibina atas yang itu. |
| Hanya `GB08` lulus | Kelebihan datang daripada **membuang yang rugi**, bukan memilih yang untung. |
| 0 lulus | Paksi GABUNGAN juga ditutup. Deliverable pengguna mesti berasaskan SPUS + tunai, dengan satu setup momentum sebagai satelit kecil sahaja. |

## 6. Had yang mesti dinyatakan dalam laporan

- Paksi `CARA` kekal `C01`, jadi kecacatan henti hari-0 hadir.
- Semua pada satu keluar (`X3`) sahaja, ufuk 63 bar.
- Kolam 12 signal dipilih daripada data yang sama, jadi keputusan bersyarat padanya.
- Alam A02 tiada saham delist.
