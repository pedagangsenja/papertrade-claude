# SOP — kombinasi signal terukur untuk pedagang swing momentum

Dijana 31 Okt 2026 daripada **371 ujian dipradaftar** yang dijalankan malam itu. Setiap spec
dan setiap kod dikomit ke `main` **sebelum** keputusan dilihat.

Bukti: `REVERSE/NXX.md` (280 ujian masuk) · `REVERSE/NXX_KELUAR.md` (69 keluar) ·
`REVERSE/GABUNGAN.md` (14 gabungan) · `REVERSE/SILANG_AKHIR.md` (8 silang).

---

## BAHAGIAN 1 — Peraturan

### Masuk: beli jika **mana-mana SATU** menyala

Bukan kesemuanya. Kesatuan, bukan persilangan. Ini yang diukur dan ini sebab ia berfungsi.

| | Peraturan | Jenis |
|---|---|---|
| **1** | `gap_and_go` — gap naik dengan volum | **momentum** |
| **2** | `adx14 > 30` **DAN** rendah hari ini sentuh `ema20` **DAN** tutup > tinggi semalam | **momentum** (Holy Grail, Raschke) |
| **3** | `bb_pctb < 0` **DAN** `rsi14 < 30` | pembalikan min |

Pilihan: tambah peraturan ke-4 — `bb_pctb[-1] < 0` **DAN** `bb_pctb > 0` **DAN** `rsi14` silang
naik 30. Ia menambah 15,205 dagangan dan hampir tidak mengubah jangkaan (+8.445% lawan
+8.541%).

**Beli pada buka sesi berikutnya.**

### Keluar: pilih SATU, ikut toleransi anda

| Keluar | Peraturan | Jangkaan/dagangan | Menang | Untung purata | **Rugi purata** |
|---|---|---|---|---|---|
| **A** | jual bila `rsi14 > 70` | **+8.54%** | 64.2% | +25.68% | **−22.14%** |
| **B** | ekori Chandelier 4×ATR14 | +6.90% | 42.8% | +36.95% | **−15.62%** |
| **C** | jual bila `adx14 < 20` | +6.32% | 54.4% | +22.87% | **−13.39%** |

Had masa: jual selepas 126 sesi jika keluar belum tercetus.

**TIADA sasaran untung. TIADA henti peratus.** Diukur empat kali secara bebas: sasaran untung
merugikan. Sasaran 2% memberi kadar menang **94.1%** dan jangkaan **−0.023%**.

### Mengapa A bukan automatik pilihan terbaik

`A` memberi jangkaan tertinggi tetapi **tiada henti sama sekali** dan kerugian purata
**−22.1%**. `C` memberi 2.2 mata lebih rendah dengan kerugian purata **−13.4%**, hampir separuh.

Itu bukan soalan data. Ia soalan berapa banyak kesakitan anda boleh tanggung pada satu posisi.

---

## BAHAGIAN 2 — Nombor, dan apa ia sebenarnya bermaksud

Tingkap **TAHAN 2020–2025** — tempoh yang **tidak dilihat** ketika signal dipilih. Kos penuh
ditolak (komisen 0.1% setiap sisi + slippage).

| | Kesatuan 3 + keluar A | Asas: beli SETIAP bar, keluar A |
|---|---|---|
| Dagangan | 195,681 | 4,420,650 |
| Jangkaan setiap dagangan | **+8.541%** | +4.350% |
| Lift atas asas | **+4.191 mata** | — |
| Kadar menang | 64.2% | 66.2% |
| Jangkaan selepas buang 5% pemenang teratas | **+2.858%** | +0.912% |
| p (t berkelompok ikut hari beli) | 0.0068 | — |

Baris terakhir itu yang paling penting, dan ia **positif** — yang pertama dalam seluruh kajian
ini. Setiap konfigurasi lain yang pernah diukur menjadi **negatif** selepas pemenang 5% teratas
dibuang, bermakna kelebihannya hidup sepenuhnya dalam beberapa kemenangan besar. Yang ini tidak.

---

## BAHAGIAN 3 — Apa yang nombor ini TIDAK beritahu

Baca bahagian ini sebelum meletakkan wang.

**1. Ini jangkaan SETIAP DAGANGAN atas 195,681 dagangan, bukan prestasi portfolio anda.**
Dengan 8–10 slot anda tidak mengambil 195,681 dagangan; anda mengambil beberapa ratus setahun.
`REVERSE/KOLAM_EKOR.md` sudah mengukur bahawa 8–10 slot mendarat dekat **median**, bukan min.
**Ujian portfolio belum dijalankan.** Sampai ia dijalankan, +8.5% setiap dagangan **bukan**
+8.5% kepada akaun anda.

**2. Kecacatan henti hari-0 hadir dalam setiap nombor di atas.** `KOLAM_EKOR.md` §4a: 421
daripada 1,770 posisi Papertrade C dibeli **dan** dihentikan pada hari masuk, kadar menang
**0.00%**, bernilai 19.5% jumlah kerugian. Semua ujian ini menganggap belian pada buka esok
tanpa pengesahan harga.

**3. Tiga signal itu dipilih daripada data yang sama** yang kemudian mengukur kesatuan mereka.
Keputusan ini **bersyarat** pada pilihan itu, bukan bebas sepenuhnya.

**4. Alam data tiada saham delist.** Bias survivorship. Ia memihak kepada asas juga, jadi
**lift** kurang terjejas daripada nombor **mutlak** — tetapi jangan baca +8.5% sebagai jangkaan
dunia nyata.

**5. SPUS masih belum dikalahkan.** `REVERSE/SISTEM.md` mengukur campuran SPUS + tunai sebagai
mengalahkan setiap sistem yang pernah diuji pada pendedahan yang sama. Kombinasi ini **belum**
diuji terhadapnya pada peringkat portfolio.

**6. +10% sebulan masih tertutup.** `REVERSE/SASARAN.md`: 0% bulan mencapainya dalam 36
sistem-tahun. Tiada apa-apa malam ini mengubah itu.

---

## BAHAGIAN 4 — Rutin harian

1. Imbas alam cair (nilai dolar median 20 hari ≥ USD100 ribu).
2. Tanda saham yang mana-mana satu daripada tiga peraturan masuk menyala.
3. Beli pada buka esok. Saiz sama rata merentas slot.
4. Untuk setiap posisi terbuka, periksa syarat keluar yang anda pilih. Jual pada buka esok jika
   tercetus.
5. Jual apa-apa yang sudah 126 sesi.
6. **Jangan letak sasaran untung.** Diukur empat kali: ia merugikan.

---

## BAHAGIAN 5 — Dua langkah seterusnya yang akan mengubah keyakinan

**Langkah 1 — ujian portfolio.** 8 slot dan 40 slot, 20 benih, lawan SPUS pada kedua-dua
konvensyen penanda aras. Ini menukar "+8.5% setiap dagangan" menjadi "X% setahun pada akaun"
dan ia **satu-satunya** nombor yang menentukan sama ada SOP ini berguna. Sampai ia selesai, SOP
ini ialah peraturan terukur **tanpa** nombor portfolio.

**Langkah 2 — betulkan kecacatan henti hari-0.** Uji `C02` (buy-stop pengesahan harga) lawan
`C01`. Ia menyentuh 19.5% jumlah kerugian dan ia mencemari setiap nombor di atas.

---

## Nota kejujuran tentang malam ini

**Lima pepijat ditangkap** sebelum sebarang nombor dilaporkan: OOM; penapis dipakai sebelum
topeng (18 peraturan terjejas); harga keluar merentas ticker (+104%/dagangan); henti degenerat
hari-masuk (menang 0.0%); dan henti berasaskan paras **di atas** harga masuk, yang melaporkan
kadar menang **99.76%** dengan jangkaan **+18.52%** dan lulus semua gate — artifak sepenuhnya,
larian itu dibuang.

**Jangkaan priori saya salah dalam majoriti lima pradaftar**, termasuk malam ini (saya jangka
lift mengecil apabila keluar ditukar; ia **membesar**). Nombor dalam dokumen ini datang daripada
ukuran, bukan daripada penilaian saya — dan itu memang tujuan pradaftar.
