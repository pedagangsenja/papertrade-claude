# KAJIAN_M_N_SATU_PER_SATU — semua kaedah M dan N dinilai satu per satu (12 Nov 2026)

> **Status keputusan (kad skor, harga 2026-11-11):** TERBUKTI 0 · CALON 0 · BELUM CUKUP 223 · GAGAL 0 · NEGATIF 0. Rejim QQQ OFF sejak 2026-10-16. Hanya **TERBUKTI** layak untuk wang sebenar (`laporan/KAD_SKOR.md`); nombor dalam laporan ini BUKAN keputusan dan tidak boleh dibaca sebagai pangkat untuk wang sebenar.

Permintaan pengguna 12 Nov 2026: nilai SEMUA kaedah M dan N dalam papertrade satu per satu, susun datanya, dan cari
kaedah serta kombinasi terbaik bagi masuk, pegang dan keluar. Keputusan pengguna pada hari yang sama, sebelum kerja
bermula: **(1) analisa dulu, tiada Nxx baharu didaftar; (2) data langsung + backtest sedia ada, tiada backtest baharu;
(3) biar data tentukan tempoh pegang; (4) simpan hasil dalam repo.**

Ini **maklumat, bukan keputusan**. Tapis senarai pantau ditulis selepas angka kad skor dilihat (tetapi sebelum lift
5/10 sesi dan pecahan separuh hari beli dilihat), jadi ia bukan pradaftar.

## 1. Jawapan ringkas

1. **Tiada kaedah yang untungnya boleh dibezakan daripada nasib.** Daripada 184 kaedah dengan ≥ 30 posisi, 79 nampak
   untung, tetapi **0** yang had bawah selang 95 %-nya melebihi sifar, dan hanya 22 yang masih untung selepas 5 %
   posisi terbaik dibuang.
2. **Empat Mxx lulus semua tapis: `M142`, `M133`, `M146`, `M80`.** Keempat-empatnya sudah pun dijejak. Dua daripadanya
   (`M133`, `M146`) pernah kena henti pada hari beli, jadi di bawah gate G4 yang dikunci ia akan GAGAL apabila G1 lulus.
3. **Semua 94 Nxx terlalu awal (6 hari beli).** Satu tanda awal yang baik: susunan backtest Nxx setakat ini selari
   dengan data langsung (korelasi pangkat +0.52 merentas 45 isyarat masuk). Bagi Mxx korelasi itu sifar (−0.05).
4. **"Kaedah terbaik" tidak stabil.** Kaedah yang terbaik pada separuh hari beli tidak lebih baik pada separuh lagi
   (korelasi pangkat −0.08 hingga +0.07). Perkara sama bagi pasangan kaedah (−0.07).
5. **Cara keluar bergantung pada pasaran.** Nxx (6 hari, pasaran melantun): "biar lari" mendahului, sama seperti
   backtest. Mxx (19 hari, pasaran turun): keluar kaedah sendiri (ada henti) mengatasi Chandelier tanpa henti.
6. **Angka "menang 98 %" ialah ilusi** apabila hanya posisi yang sudah dijual dikira (§4).

**Cadangan: jangan daftar Nxx atau gabungan baharu sekarang.** Kaedah yang mendahului sudah pun dijejak; data belum
boleh memilih antara mereka. Langkah seterusnya dalam §11.

## 2. Data dan cara

| Perkara | Nilai |
|---|---|
| Data langsung | Lejar Penuh lorong 1, penyebut kad skor: **36,292 posisi**, 223 kaedah (129 Mxx, 94 Nxx), harga tutup 2026-11-11 |
| Hari beli | Mxx 19 (isyarat sejak 15 Okt), Nxx 6 (isyarat sejak 3 Nov); rejim QQQ ON 1 hari, OFF 18 hari |
| Jangkaan | purata semua posisi, **termasuk yang masih terbuka** (ditanda ke pasaran), kos 0.2 %; sama dengan kad skor |
| Pulangan ufuk tetap | beli pada buka → tutup sesi ke-1/3/5/10/15, kos 0.2 %; **tidak bergantung pada peraturan keluar** |
| Lift | pulangan ufuk tetap tolak saham lain yang Lejar beli pada **hari sama dan tercile ATR sama** (`standard/lift_kaedah.py`) |
| Lorong 2 | posisi yang sama, keluar ikut Chandelier tutup 4×ATR14 tanpa henti kaedah |
| Backtest sedia ada | Mxx: registry set 431 varian produksi (`data/registry_M_gabung.csv`); Nxx: tingkap tahan 2020–2025 (`REVERSE/jejak_semua.csv`) |
| Ufuk 20 sesi | **belum wujud** dalam data langsung (paling lama 19 sesi); angka 20 sesi hanya daripada backtest |

Semakan tangan: pulangan 5 sesi satu posisi (`M142` SIG, beli 20 Okt pada 117.35) dikira semula daripada bar mentah
dan sepadan (−2.20 %).

## 3. Pulangan selepas beberapa hari pegang (kadar asas)

Semua saham-hari unik yang Lejar beli, tanpa mengira kaedah:

| Pegang | Hari beli | Saham-hari | Purata | Untung | SPUS tingkap sama |
|---|---|---|---|---|---|
| 1 sesi | 19 | 9,958 | −0.31 % | 45 % | −0.13 % |
| 3 sesi | 17 | 8,736 | −0.19 % | 50 % | −0.58 % |
| 5 sesi | 15 | 7,663 | −0.58 % | 49 % | −1.34 % |
| 10 sesi | 10 | 5,151 | −0.78 % | 50 % | −2.63 % |
| 15 sesi | 5 | 2,641 | −1.15 % | 48 % | −4.21 % |

- Pada setiap tempoh pegang, belian purata **rugi sedikit**, tetapi kurang daripada SPUS dalam tingkap yang sama.
- **Hari beli lebih menentukan daripada kaedah.** Pulangan 5 sesi kolam ikut hari beli berjulat −3.43 % hingga
  +1.73 % (SD 1.82 mata); beza antara kaedah pada hari yang sama lebih kecil (SD lift 1.36 mata).
- Daripada 99 Mxx dengan ≥ 30 saham-hari dan ufuk 10 sesi, hanya **23** untung pada ketiga-tiga tempoh 3, 5 dan
  10 sesi (`hasil/lengkung_pegang.csv`). Nxx belum ada ufuk 10 sesi.

## 4. Ilusi "tutup sahaja"

`lejar/RINGKASAN.md` memaparkan kadar menang dan purata **posisi yang sudah dijual sahaja**. Bagi kaedah yang hanya
menjual apabila untung (cth. keluar `X13` = jual bila RSI14 > 70), yang dijual hampir semuanya pemenang dan yang rugi
masih terbuka:

| Kaedah | Posisi | Sudah dijual | Menang (dijual) | Purata dijual | Purata masih terbuka | **Purata semua** |
|---|---|---|---|---|---|---|
| `N16X13` | 620 | 43 | 98 % | +16.80 % | −1.92 % | **−0.62 %** |
| `N75X13` | 568 | 40 | 100 % | +21.71 % | −1.33 % | **+0.29 %** |
| `N119X13` | 1,003 | 254 | 89 % | +9.92 % | −3.03 % | **+0.25 %** |

(Angka `RINGKASAN.md` sesi 11 Nov, termasuk posisi isian bina semula; "purata semua" dikira daripada dua lajur itu.)
Dalam penyebut langsung kad skor: `M01` purata dijual +13.48 % (20 posisi) tetapi jangkaan +3.05 %; `M82` +2.43 %
lawan −0.48 %; `M73` +0.64 % lawan +0.15 % (`hasil/ilusi_tutup_sahaja.csv`). **Baca lajur jangkaan, bukan lajur
menang.**

## 5. Setiap kaedah, satu per satu

Jadual penuh 223 kaedah: **`analisa_mn/hasil/SEMUA_KAEDAH.md`** (ringkas) dan **`analisa_mn/hasil/kaedah.csv`**
(semua lajur, termasuk teks masuk / pegang / keluar / henti setiap kaedah). Label mekanikal:

| Kelas | Syarat | Mxx | Nxx |
|---|---|---|---|
| PANTAU | lulus semua tapis di bawah | 4 | 0 |
| CAMPUR | cukup data, gagal sekurang-kurangnya satu tapis | 63 | 0 |
| LEMAH | jangkaan ≤ 0 **dan** lift 5 sesi ≤ 0 | 22 | 0 |
| STRUKTUR GAGAL | henti pada hari beli ≥ 20 % posisi (G4 pasti gagal; sama dengan label cantas C1) | 10 | 0 |
| TERLALU AWAL | < 30 posisi atau < 10 hari beli | 30 | 94 |

Tapis PANTAU, dan bilangan yang lulus setiap satu daripada 89 Mxx yang cukup data dan bukan STRUKTUR GAGAL:

| Tapis | Lulus |
|---|---|
| jangkaan > 0 | 34 |
| **tanpa5 > 0** (masih untung selepas buang 5 % posisi terbaik) | **6** |
| lift 5 sesi > 0 | 63 |
| lift 10 sesi > 0 | 46 |
| lift 5 sesi > 0 pada kedua-dua separuh hari beli | 37 |
| backtest > 0 | 89 |

Tapis yang paling menapis ialah `tanpa5`: kebanyakan kaedah "untung" hanya kerana beberapa posisi besar.

## 6. Senarai pantau Mxx (BUKAN terbukti)

| | `M142` Pecahan volum dari dasar | `M133` Bull Hook | `M146` 3-Bar Momentum | `M80` Radge MAC |
|---|---|---|---|---|
| **Masuk** | pecah tinggi 20 hari > 3 % dengan volum ≥ 2×, di atas MA250 naik; beli selepas hari turun pertama yang kekal di atas paras pecah | hari "hook" (buka > tinggi semalam, tutup < tutup semalam), esoknya tutup > buka + regangan | 3 lilin hijau makin laju, tinggi baharu 20 hari | rendah di atas SMA10-tinggi selama tepat 5 hari |
| **Pegang** | tiada had | maksimum 21 sesi | tiada had | tiada had (pegangan panjang) |
| **Keluar** | Chandelier 4×ATR22 | tutup < SMA50 | tutup < SMA50 | tinggi di bawah SMA8-rendah 5 hari |
| **Henti** | 3.5×ATR14 (maks 15 %) | 2×ATR14 (maks 15 %) | tetap 6 % | 3×ATR14 |
| Posisi / dijual | 45 / 5 | 49 / 23 | 77 / 30 | 273 / 56 |
| Hari beli | 14 | 13 | 17 | 19 |
| Jangkaan | +3.31 % | +1.80 % | +1.70 % | +1.34 % |
| tanpa5 | +1.88 % | +0.49 % | +0.68 % | +0.07 % |
| Menang / payoff | 82 % / 0.83 | 55 % / 1.71 | 55 % / 1.42 | 55 % / 1.17 |
| Pegang 3 / 5 / 10 sesi | +1.94 / +1.57 / +0.52 | +2.29 / +1.46 / +5.94 | +1.77 / +2.09 / +1.69 | +0.28 / +0.47 / +3.21 |
| Lift 5 / 10 sesi | +4.10 / +2.54 | +1.78 / +5.73 | +2.12 / +2.41 | +1.00 / +3.11 |
| Lift 5 sesi, separuh A / B | +4.86 / +3.54 | +1.33 / +2.88 | +3.09 / +0.40 | +1.10 / +0.83 |
| Jika keluar Chandelier (L2) | +3.29 % | +2.67 % | +2.60 % | +1.30 % |
| Rugi terburuk | −14.7 % | −12.0 % | −31.4 % | −41.5 % |
| Had bawah 95 % buku harian | −0.25 % | −0.43 % | −0.01 % | −0.13 % |
| Lorong T4 (persentil jalur rawak) | +5.31 % (80) | +7.95 % (95) | +6.71 % (95) | −1.46 % (20) |
| Backtest: purata / menang / hari | +6.85 % / 41 % / 44 | +0.68 % / 41 % / 10 | +2.66 % / 27 % / 26 | +8.91 % / 36 % / 66 |
| Backtest: CAGR / MDD | 32 % / −28 % | 20 % / −26 % | 36 % / −41 % | 38 % / −39 % |
| **Henti pada hari beli (G4 mesti 0)** | 0 | **1** | **4** | 0 |

Bacaan:

- Keempat-empatnya sudah berada dalam kelas PANTAU `kajian/FABLE_PENILAIAN.md` §8 (9 Nov, 11 kaedah). Tujuh yang lain
  gugur di sini, kebanyakannya kerana `tanpa5` ≤ 0 (`M33` gugur kerana lift separuh B −0.02).
- **`M133` dan `M146` tidak boleh mencapai TERBUKTI seperti sedia ada**: G4 kad skor mewajibkan sifar henti pada hari
  beli, dan gate itu dikunci. Tinggal `M142` dan `M80`.
- `M142`: lift ufuk tetapnya berdiri atas 26 saham-hari (5 sesi) dan 8 (10 sesi); kadar menang 82 % dengan payoff 0.83
  datang daripada 40 posisi yang masih terbuka.
- `M80`: lorong portfolio T4-nya **negatif** dan di persentil 20, walaupun jangkaan setiap posisi positif.
- MDD backtest keempat-empat −26 % hingga −41 %: jauh melebihi toleransi −10 % pada pendedahan penuh.

## 7. Nxx: isyarat masuk × cara keluar

94 kombinasi = 45 isyarat masuk × 6 cara keluar. **Hanya 6 hari beli; lift 5 sesi wujud untuk 2 hari sahaja.**

Ikut cara keluar (posisi yang sama dikongsi antara cara keluar, jadi bandingan ini berpasangan):

| Keluar | Peraturan | Kombinasi | Langsung: jangkaan | Sudah dijual | Backtest tahan | Backtest tanpa5 | Rugi purata backtest |
|---|---|---|---|---|---|---|---|
| `X15` | ekori Chandelier 4×ATR14 | 5 | +1.69 % | 0 % | +7.09 % | −1.69 % | −14 % hingga −22 % |
| `X13` | jual bila RSI14 > 70 | 6 | +1.66 % | 6 % | +6.84 % | +1.97 % | −21 % hingga −24 % |
| `X14` | jual bila RSI14 silang naik 50 | 10 | +0.83 % | 8 % | +2.21 % | −1.88 % | −8 % hingga −14 % |
| `X17` | jual bila ADX14 < 20 | 10 | +0.53 % | 20 % | +3.85 % | −2.50 % | −9 % hingga −13 % |
| `X36` | dua tutup di bawah MA50 | 37 | +0.21 % | 32 % | +2.11 % | −2.78 % | −6 % hingga −15 % |
| `X16` | Supertrend berbalik | 26 | −0.20 % | 37 % | +1.50 % | −2.54 % | −6 % hingga −12 % |

Isyarat masuk teratas (`hasil/nxx_masuk.csv`; kombinasi penuh `hasil/nxx_semua.csv`):

| Masuk | Langsung: jangkaan | Backtest tahan | Kombinasi berpangkat backtest tertinggi | Catatan |
|---|---|---|---|---|
| `N19` di bawah jalur BB + RSI < 30 | +4.61 % | +11.29 % | `N19X13` (101 posisi, 0 dijual, tanpa5 +3.49 %) | pangkat backtest 2/94 |
| `N124` episodic pivot gap 8–10 % | +2.86 % | +11.02 % | `N124X15` (39 posisi, 0 dijual) | pangkat backtest 1/94 |
| `N40` OBV tinggi baharu + MA50 | +2.42 % | +1.70 % | `N40X36` (47 posisi, 7 dijual) | pangkat backtest 40/94; tanpa5 negatif |
| `N75` RSI14 < 40 | +2.05 % | +4.81 % | `N75X13` (124 posisi, 1 dijual) | pangkat backtest 3/94 |
| `N64` episodic pivot | +1.98 % | +3.81 % | `N64X17` (46 posisi, 10 dijual) | pangkat backtest 11/94 |
| `N73` tutup di bawah jalur bawah BB | +1.95 % | +6.89 % | `N73X13` (136 posisi, 1 dijual) | pangkat backtest 4/94 |

Bacaan:

- **Susunan backtest selari dengan data langsung setakat ini**: korelasi pangkat +0.52 merentas 45 isyarat masuk
  (p 0.0003); dalam keluar `X36` sahaja +0.34, dalam `X16` sahaja +0.53. Ini tanda awal yang baik, dan berbeza
  daripada Mxx (−0.05). **Tetapi** ia 6 hari dalam satu lantunan pasaran, posisi bertindih, dan isyarat teratas ialah
  isyarat "terlebih jual" yang memang untung apabila pasaran melantun. Jika diukur dengan lift 3 sesi (pemilihan saham
  sahaja), korelasinya +0.26 (p 0.08).
- `N19X13` mendahului pada kedua-dua ukuran, tetapi **belum menjual walau satu posisi** dan lift 3 sesinya negatif
  (−0.97): untungnya datang daripada memegang melalui lantunan, bukan daripada memilih saham.
- Harga "biar lari": rugi purata backtest `X13` −22 % setiap dagangan yang rugi, dan portfolio 8 slot gabungan yang
  mengandungi `N19` (`GB02` × `X13`) mencatat MDD −44.8 % (`REVERSE/PORTFOLIO_N.md`). Kelebihan setiap dagangan tidak
  berpindah ke akaun MDD −10 %.

## 8. Mxx: keluar kaedah sendiri lawan Chandelier

Posisi yang sama (25,776 posisi Mxx; 104 kaedah dengan ≥ 30 posisi):

| | Keluar kaedah (L1) | Chandelier tanpa henti (L2) |
|---|---|---|
| Purata semua posisi | −0.25 % | −0.55 % |
| Purata merentas kaedah | −0.39 % | −0.71 % |
| Posisi rugi lebih 15 % | 3.1 % | 9.7 % |
| Kaedah yang lebih baik dengan cara ini | 67 % | 33 % |

Dalam 19 hari pasaran menurun, henti kaedah melindungi. Ini bertentangan dengan backtest (Chandelier terbaik) dan
dengan Nxx minggu lepas — **cara keluar yang terbaik berubah ikut pasaran**, dan data langsung baru melihat satu fasa.

## 9. Bolehkah "terbaik" dipercayai?

**(a) Adakah kaedah yang baik kekal baik?** Hari beli dipecah secara rawak kepada dua separuh (500 kali); kaedah
disusun ikut lift pada separuh pertama dan dibaca pada separuh kedua:

| Ukuran (Mxx) | Korelasi pangkat A lawan B [5 %, 95 %] | 10 teratas A: lebihan pada B [5 %, 95 %] |
|---|---|---|
| Lift 3 sesi (17 hari) | −0.08 [−0.23, +0.07] | −0.17 mata [−0.82, +0.33] |
| Lift 5 sesi (15 hari) | +0.07 [−0.12, +0.24] | +0.02 mata [−0.75, +0.77] |
| Lift 10 sesi (10 hari) | +0.15 [+0.01, +0.29] | +0.32 mata [−0.84, +1.34] |

Tiada kestabilan pada 3 dan 5 sesi. Angka 10 sesi condong ke atas kerana tingkap 10 sesi bagi hari beli berjiran
bertindih 9 hari. Nxx: terlalu sedikit hari untuk diuji.

**(b) Adakah Mxx sebagai KUMPULAN memilih lebih baik daripada rawak?** 32 daripada 101 Mxx lulus tapis ufuk tetap
(lift 5 > 0, kedua-dua separuh > 0, lift 10 > 0). Jika pulangan dikocok antara saham pada hari dan tercile ATR sama
(pertindihan antara kaedah dikekalkan): purata 15.6 lulus [9, 24]. Tanpa hari beli pertama (16 Okt): 24 lulus lawan
15.1 [9, 23], p 0.03. Ada tanda lemah bahawa saham pilihan Mxx sedikit lebih baik daripada rawak, tetapi sebahagian
besarnya datang daripada satu hari, dan ujian kocok ini mengabaikan saham sesektor yang bergerak bersama. Ujian yang
sah ialah G3 kad skor, yang memerlukan ~5 minggu.

**(c) Backtest lawan langsung.** Mxx (90 kaedah, ≥ 20 dijual): −0.05 bagi jangkaan, +0.12 bagi lift 5 sesi; kedua-dua
tidak signifikan. Nxx: +0.52 (§7).

## 10. Kombinasi kaedah pada data langsung

**Berapa kaedah Mxx sepakat membeli saham yang sama pada hari yang sama** (pulangan 5 sesi):

| Kaedah sepakat | Saham-hari | Lift | t | Tanpa hari beli pertama: lift (t) |
|---|---|---|---|---|
| 1 | 2,900 | −0.28 | −1.07 | −0.14 (−0.62) |
| 2 | 1,519 | −0.14 | −0.50 | −0.06 (−0.21) |
| 3–4 | 1,505 | +0.33 | +1.28 | +0.36 (+1.24) |
| 5–9 | 1,191 | −0.02 | −0.04 | −0.21 (−0.55) |
| 10+ | 269 | +1.49 | +1.67 | +0.37 (+0.71) |

Baldi "10+" nampak baik, tetapi 94 daripada 269 saham-harinya ialah satu hari (16 Okt, hari pertama Lejar, lift
+3.58). Tanpa hari itu lift jatuh ke +0.37 (t 0.71). Selaras dengan `KAJIAN_ISYARAT_KOMBINASI.md`: lebih banyak isyarat
sepakat tidak menambah untung.

**Semua pasangan Mxx.** Daripada 8,128 pasangan, 395 membeli ≥ 30 saham-hari yang sama. 20 pasangan terbaik pada
separuh hari beli pertama: lift +3.79 di situ, **+0.42 pada separuh kedua** (semua pasangan: +0.11); arah sebaliknya:
+1.17 lawan +1.35 bagi semua pasangan. Korelasi pangkat antara dua separuh −0.07. Memilih pasangan "terbaik" daripada
data ini ialah memilih nasib. **Tiada pasangan dipilih atau disenaraikan.**

## 11. Bacaan masuk, pegang, keluar — dan langkah seterusnya

| Bahagian | Apa yang data katakan | Keyakinan |
|---|---|---|
| **Masuk** | Tiada isyarat tunggal terbukti. Mendahului: pecahan momentum (`M142`, `M133`, `M146`, `M80`) dan terlebih jual (`N19`, `N75`, `N73`); gap besar (`N124`) | rendah: 6–19 hari, satu fasa pasaran |
| **Pegang** | Tiada tempoh pendek yang untung secara purata (1–15 sesi semuanya negatif). Backtest: untung datang selepas 20–60 sesi, bukan 5–10 | sederhana (selaras `REVERSE/PEGANG_SLOT.md`) |
| **Keluar** | Pasaran naik/melantun: biar lari (RSI14 > 70 atau Chandelier). Pasaran turun: henti kaedah mengurangkan rugi besar daripada 9.7 % kepada 3.1 % posisi | sederhana bagi arah; tiada peraturan tukar yang diuji |
| **Kombinasi** | Lebih banyak kaedah sepakat dan pasangan "terbaik" tidak bertahan | tinggi (dua kajian, arah sama) |

Langkah demi langkah:

1. **Sekarang: jangan daftar Nxx atau gabungan baharu.** Tujuh kaedah yang mendahului (`M142`, `M133`, `M146`, `M80`,
   `N19X13`, `N124X15`, `N75X13`) semuanya sudah dijejak dalam Lejar, kad skor dan lorong T4. Mendaftar gabungan baharu
   sekarang hanya menambah kaedah yang lulus kerana nasib (§9a, §10).
2. **Titik semak 1 — awal Dis 2026** (Nxx ≥ 20 hari beli; G3 mula menguji lift): jalankan semula
   `python3 BacktestShariah2/kajian/analisa_mn/analisa.py`. Tiga soalan: adakah senarai pantau §6 kekal; adakah
   korelasi backtest–langsung Nxx kekal positif; adakah lift kumpulan Mxx (§9b) kekal tanpa bergantung pada satu hari.
3. **Titik semak 2 — apabila G1 lulus** (≥ 10 hari beli rejim ON): banding keluar L1 lawan L2 dalam rejim ON. Jika
   arah §8 terbalik dalam ON, itu bukti pertama bahawa keluar patut ikut rejim.
4. **Hanya jika titik semak 1 dan 2 positif:** pradaftar **satu** gabungan bertarikh (contoh hipotesis: masuk terlebih
   jual `N19`/`N75` + keluar ikut rejim) **sebelum** data hadapannya dilihat. Itu keputusan pengguna dan pengecualian
   baharu kepada peraturan "tiada baris MASUK Nxx baharu".
5. **Wang sebenar:** hanya apabila kad skor menanda TERBUKTI. Tiada apa-apa dalam laporan ini mengubahnya.

## 12. Had

- **19 hari beli (Nxx 6), satu rejim.** Kelebihan saham pemimpin bertukar tanda ikut rejim QQQ (12/17 tahun).
- **Bukan pradaftar.** Tapis §5 ditulis selepas angka kad skor dilihat. Senarai pantau ialah senarai untuk diperhati.
- **Tingkap bertindih.** Hari beli berjiran berkongsi kebanyakan hari pulangan; setiap nilai t di sini optimistik.
- **Setiap posisi, bukan portfolio.** Tiada had slot, tiada MDD akaun. Ukuran portfolio ialah lorong T4 dan G6.
- **Kolam lift** ialah saham yang Lejar beli (patuh Syariah, ≥ USD 10), bukan seluruh pasaran.
- **Ujian kocok §9b** menganggap saham dalam satu sel bebas antara satu sama lain; ia tidak.
- Posisi dengan data harga dikuarantin (14) dan posisi isian bina semula (35,700) tidak dikira, seperti kad skor.

## 13. Jana semula

`python3 BacktestShariah2/kajian/analisa_mn/analisa.py` (≈ 30 saat; benih rawak ditetapkan). Skrip hanya membaca Lejar,
stor harga, `kad_skor.json`, registry dan `jejak_semua.csv`. Keluaran dalam `kajian/analisa_mn/hasil/`:

| Fail | Kandungan |
|---|---|
| `SEMUA_KAEDAH.md`, `kaedah.csv` | setiap kaedah: kelas, angka langsung, ufuk tetap, lift, separuh, lorong 2, backtest, teks masuk/pegang/keluar/henti |
| `senarai_pantau.csv`, `tapis.csv` | §5–6 |
| `kadar_asas.csv`, `kolam_ikut_hari.csv`, `lengkung_pegang.csv` | §3 |
| `ilusi_tutup_sahaja.csv` | §4 |
| `nxx_keluar.csv`, `nxx_masuk.csv`, `nxx_semua.csv`, `nxx_masuk_x_keluar_*.csv` | §7 |
| `mxx_lorong.json` | §8 |
| `kestabilan.csv`, `plasebo_tapis.json` | §9 |
| `konsensus.csv`, `pasangan_mxx.json` | §10 |
| `log.txt` | cetakan penuh larian |
