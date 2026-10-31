# SPEC — Portfolio Nxx dan paksi CARA (pradaftar)

**Ditulis dan dikomit SEBELUM larian.** Jangan sunting selepas keputusan dilihat; jika ada
pembetulan pra-larian, tambah sebagai §9 bertarikh dan nyatakan ia dibuat sebelum sebarang
nombor dipandang.

Dua kajian berasingan, dua skrip, dua fail keputusan:

| | Soalan | Skrip | Keputusan |
|---|---|---|---|
| Kajian 1 | Adakah `GB02_atau3 × X13` menjadi **portfolio** yang mengalahkan SPUS? | `REVERSE/step22_portfolio_n.py` | `REVERSE/PORTFOLIO_N.md` |
| Kajian 2 | Adakah **cara pesanan diisi** (paksi CARA) mengubah keputusan, dan membetulkan kecacatan henti hari-0? | `REVERSE/step23_cara.py` | `REVERSE/CARA.md` |

---

## 1. Mengapa dua kajian ini, dan bukan yang lain

`REVERSE/SILANG_AKHIR.md` mengukur `GB02_atau3 × X13` memberi **+8.541% setiap dagangan**
pada tingkap tahan, menang 64.2%, `tanpa5` **+2.858%** (asas +0.912%), p 0.0068. Lapan
daripada lapan kombinasi lulus keempat-empat gate.

Dua perkara menghalang nombor itu daripada bermakna apa-apa kepada pengguna:

1. **Ia jangkaan setiap DAGANGAN, bukan portfolio.** `KOLAM_EKOR.md` §1 mengukur saham
   median kolam A02 memberi +0.82%/bulan sedangkan portfolio berat sama rata SELURUH kolam
   memberi +1.64%. Maka 8–10 slot mendarat dekat **median**, bukan min. Jangkaan setiap
   dagangan yang tinggi boleh runtuh sepenuhnya apabila dihadkan kepada 8 slot.
2. **Paksi CARA dikunci `C01`.** Setiap nombor dalam seluruh kajian memakai "beli pada buka
   esok", dan `C01` ialah punca kecacatan henti hari-0 (`KOLAM_EKOR.md` §4a): 421 daripada
   1,770 posisi C dibeli DAN dihentikan pada hari masuk dengan kadar menang **0.00%**,
   bernilai 19.5% jumlah kerugian.

Kajian 1 menjawab (1). Kajian 2 menjawab (2).

**Had yang tidak boleh dihilangkan oleh mana-mana larian ini:** kolam 12 signal `GB02` dan
keluar `X13` dipilih daripada data yang SAMA seperti yang akan diuji di sini. Maka setiap
keputusan di bawah adalah **BERSYARAT** kepada pemilihan itu. Satu-satunya cara menghapus
syarat ini ialah tingkap data baharu yang belum wujud. Ini dinyatakan dalam laporan, bukan
dalam nota kaki.

---

## 2. Alam, kos dan tingkap (sama untuk kedua-dua kajian)

- **Alam**: `AUTOTUNE/.cache_autotune-data-a02` — sama seperti seluruh REVERSE. Ia **tiada
  saham delist** (bias survivorship ke atas); itu `AL01`, dan `AL02` (alam SPUS sebenar)
  kekal belum diuji.
- **Kecairan**: median nilai dagangan 20 bar ≥ USD100,000 (`CAIR`, sama seperti
  `kod/tidak_layak.py`).
- **Kos**: `REVERSE/teras/kos.py` — komisen 0.1% + slippage ikut nilai20 (0.05% / 0.10% /
  0.25%), dikenakan pada **kedua-dua** sisi.
- **Tingkap keputusan**: 2020-01-01 – 2025-12-31 (tingkap TAHAN; SPUS bermula Dis 2019).
- **Tingkap diagnostik (bukan gate)**: 2012–2019, dilapor bersama SPY kerana SPUS tiada.

---

## 3. Kajian 1 — portfolio

### 3.1 Enjin

Guna semula `REVERSE/pembinaan.py` (`Panel`, `kos`, `mdd`, `cagr`, `penanda_aras`) supaya
tiada enjin kedua. Perbezaan daripada `pembinaan.py`:

- **Sauh HARIAN, bukan bulanan.** Isyarat `GB02` ialah isyarat harian; sauh bulanan membuang
  kebanyakannya. Setiap sesi `d`: keluar diselesaikan dahulu, kemudian slot kosong diisi
  daripada isyarat pada tutup `d−1`, dibeli pada **buka `d`**. Itu konvensyen `C01` yang sama
  seperti setiap nombor setiap-dagangan dalam kajian ini.
- **Masuk daripada topeng isyarat**, bukan rawak (kecuali lorong kawalan).

### 3.2 Grid TETAP — jangan lebarkan selepas melihat keputusan

- **Masuk**: `GB02_atau3` (N19 ∪ N37 ∪ N115), `GB02_atau4` (+ N20), `RAWAK` (kawalan).
- **Slot**: 8, 40.
- **Keluar**: `X13` (tutup `rsi14 > 70` → jual buka esok) dan `X15` (ekori Chandelier
  4×ATR14 → jual buka esok).
- **Urutan** apabila isyarat melebihi slot kosong: `U01` rawak (20 benih), `U02` persentil RS
  menurun, `U08` ATR% menaik (songsang).

3 masuk × 2 slot × 2 keluar × 3 urutan = **36 konfigurasi**; `U01` dijalankan 20 benih, maka
3 × 2 × 2 × (20 + 1 + 1) = **264 larian simulasi**.

### 3.3 Peraturan pelaksanaan yang mesti ditetapkan SEKARANG

- **Had imbasan keluar**: 504 bar (2 tahun) bagi `X13` dan `X15`. Tanpa had, saham yang tidak
  pernah mencapai `rsi14 > 70` dipegang sehingga hujung data dan mengunci slot selama-lamanya.
  Jika had dicapai, keluar pada buka bar berikutnya.
- **Tiada bar sah pada hari keluar**: guna tutup bar sah terakhir.
- **Satu posisi setiap ticker** pada satu masa.
- **Saiz**: `1/slot` daripada ekuiti pada tutup sesi sebelum (`SZ01` berat sama rata). Tiada
  leverage, tiada margin (riba). Tunai tidak berbunga.
- **Isyarat melebihi slot kosong**: susun ikut paksi URUTAN, ambil dari atas.
- **Isyarat kurang daripada slot kosong**: baki kekal TUNAI. Pendedahan yang terhasil
  dilapor — ia yang menjatuhkan Sistem B Clenow dalam `SISTEM.md`, dan gate P4 wujud khusus
  untuk menangkapnya.

### 3.4 Gate — ditetapkan sekarang

Keempat-empat mesti lulus untuk mendakwa konfigurasi itu mengalahkan memegang SPUS.

| Gate | Syarat |
|---|---|
| **P1 pulangan** | CAGR median (20 benih) **>** SPUS CAGR 2020–2025 |
| **P2 MDD** | MDD median **tidak lebih teruk** daripada SPUS MDD 2020–2025 |
| **P3 isyarat berguna** | CAGR median masuk-isyarat **>** persentil ke-95 kawalan `RAWAK` pada slot dan keluar yang sama |
| **P4 nisbah** | CAGR ÷ \|MDD\| **> 0.669** |

Nota setiap gate:

- **P1/P2** memakai konvensyen **CAGR seluruh tingkap** (SPUS 17.95% / −26.82%). Konvensyen
  kedua (median setiap tahun, 26.09% / −10.14%) dilapor bersebelahan tetapi **tidak dicampur**
  — `PEMBINAAN.md` sudah menetapkan kedua-duanya betul daripada data sama dan mencampurkannya
  adalah ralat.
- **P3** sengaja ketat: persentil ke-95 kawalan, bukan medannya. Sebabnya `KEPEKATAN_BENIH.md`
  mengukur hingar pemilihan merentas susunan sewenang-wenang ialah **17.3 mata peratus
  setahun** pada 8 slot. Mengalahkan median rawak boleh berlaku dengan nasib sahaja; isyarat
  yang benar-benar menambah nilai mesti mengalahkan cabutan rawak yang BERTUAH.
- **P4** ambang 0.669 datang daripada `SISTEM.md`: nisbah `CAGR ÷ |MDD|` bagi campuran
  SPUS + tunai hampir pemalar **0.642–0.669** merentas setiap berat. Sistem yang hanya
  mengurangkan pendedahan bergerak di sepanjang garis itu dan tidak mencipta apa-apa.
  Melepasi 0.669 bermakna sistem berada DI ATAS garis campuran, bukan di atasnya.

### 3.5 Jangkaan priori (direkod sebelum larian)

- **P1: saya jangka GAGAL pada 8 slot, mungkin lulus pada 40.** Sebab: `KOLAM_EKOR.md` §1 —
  8 slot mendarat dekat median kolam, bukan min. Hujah balas yang nyata: `tanpa5` SILANG_AKHIR
  **positif** (+2.858%), iaitu kelebihan itu TIDAK hidup sepenuhnya dalam ekor kanan. Itu
  satu-satunya kes sedemikian dalam seluruh kajian, dan ia sebab tunggal kajian ini berbaloi.
- **P2: saya jangka LULUS pada 8 slot gagal, 40 slot lulus.** Pemusatan 8 slot sepatutnya
  memberi MDD lebih dalam daripada SPUS.
- **P3: saya jangka LULUS.** Lift setiap dagangan +4.19 mata adalah besar.
- **P4: saya jangka GAGAL.** Tiada apa-apa dalam kajian ini pernah melepasi 0.669.

**Rekod kejujuran:** jangkaan priori saya salah pada 2 daripada 3 gate dalam `SPEC_SILANG` §7,
`SPEC_SISTEM` §7 dan `SPEC_NXX`. Tiga pradaftar berturut-turut. Corak kesilapan: saya
memandang **rendah** struktur statistik dalam ruang belum diukur dan memandang **tinggi**
keupayaannya bertahan ujian ekor. Jangkaan di atas hendaklah dibaca dengan rekod itu.

---

## 4. Kajian 2 — paksi CARA

### 4.1 Grid TETAP

Masuk `GB02_atau3`, keluar `X13`, kedua-dua tingkap (latih 2012–2019, tahan 2020–2025).
Enam cara pengisian, `m = 6` dipradaftar untuk BH-FDR:

| id | Mekanik |
|---|---|
| `C01` | pasaran pada buka esok (**asas**, tingkah laku repo sekarang) |
| `C02` | buy-stop pada `tinggi20 × 1.002`, sah 5 bar, kemudian batal |
| `C03` | buy-limit pada `tutup_isyarat × 0.985`, sah 3 bar |
| `C04` | buy-limit pada `tutup_isyarat × 0.99`, sah 3 bar |
| `C05` | OCO: buy-limit `×0.98` lawan buy-stop `×1.02`, sah 5 bar, yang disentuh dahulu menang |
| `C06` | bracket: pasaran buka esok + sasaran `+6%` + henti `−3%` (OCO), jika tidak `X13` |

Pengisian dinilai pada bar `e = isyarat + 1 … isyarat + N`: stop diisi jika `tinggi ≥ paras`
(harga isian = maks(paras, buka)), limit diisi jika `rendah ≤ paras` (harga isian =
min(paras, buka)). Jika kedua-dua sentuh dalam bar sama bagi `C05`/`C06`, andaikan yang
**merugikan kita** berlaku dahulu — jurang mesti diambil terhadap kita, bukan memihak.

### 4.2 Metrik

- **Kadar isi**: berapa % isyarat benar-benar menjadi posisi.
- **Jangkaan setiap SIGNAL** (isyarat tidak terisi = 0%) — ini penyebut yang jujur.
- **Jangkaan setiap DAGANGAN TERISI** — dilapor, tetapi bukan asas gate.
- **Kadar henti hari-0**: % dagangan yang dihentikan pada bar masuk. Ini nombor yang kajian
  ini wujud untuk menjawab.
- Harga masuk purata relatif kepada `C01`.

### 4.3 Gate

| Gate | Syarat |
|---|---|
| **CARA1** | jangkaan setiap SIGNAL melebihi `C01` pada **kedua-dua** tingkap |
| **CARA2** | BH-FDR q ≤ 0.05 dengan **m = 6**, ralat piawai berkelompok ikut hari beli |
| **CARA3** | jangkaan mutlak setiap SIGNAL **> 0** pada tingkap tahan |

`CARA3` ditambah kerana `SPEC_NXX` §gagal: `N16 × X1` lulus gate1 + gate2 dengan lift +0.193
dan menang 62.4% tetapi jangkaan mutlak **−0.088%** — lift positif atas asas NEGATIF masih
rugi. Pelajaran itu dikuatkuasakan di sini.

### 4.4 Jangkaan priori (direkod sebelum larian)

- `C02` (pengesahan) menaikkan jangkaan setiap dagangan terisi tetapi menurunkan kadar isi
  cukup banyak sehingga jangkaan setiap SIGNAL rata atau lebih teruk.
- `C03`/`C04` (limit) lebih teruk: membeli penurunan yang terus turun.
- `C06` (bracket) **jelas lebih teruk** — `KOMBINASI.md` sudah mengukur sasaran untung
  memusnahkan jangkaan (`X1` sasaran 1×ATR menukar asas +2.595% menjadi **−0.281%**).
- Kadar henti hari-0 `C01` dijangka sepadan dengan ~24% yang `KOLAM_EKOR.md` §4a ukur pada
  data hadapan.

---

## 5. Apa yang larian ini TIDAK boleh buktikan

- Bukan bukti tidak bersyarat: signal dan keluar dipilih atas data sama (§1).
- Alam tiada delist (`AL01`), jadi setiap CAGR condong ke atas.
- Tiada bar intrahari: setiap sentuhan stop/limit dianggarkan daripada tinggi/rendah harian.
- `+10%/bulan` kekal tertutup secara aritmetik (`SASARAN.md`): 3.14×/tahun, 8,994,377× atas
  14 tahun. Tiada konfigurasi di sini akan menghampirinya, dan tiada dakwaan sedemikian akan
  dibuat.

---

## 6. Keluaran

- `REVERSE/PORTFOLIO_N.md` + `REVERSE/portfolio_n.csv`
- `REVERSE/CARA.md` + `REVERSE/cara.csv`
- Jika gate gagal: ia dilapor sebagai gagal. Tiada gate dilonggarkan selepas keputusan dilihat,
  tiada konfigurasi ditambah, tiada tingkap ditukar.
