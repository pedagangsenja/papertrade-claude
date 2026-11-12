# KAJIAN_ISYARAT_KOMBINASI — indikator, kombinasi dan cara keluar (tinjauan 11–12 Nov 2026)

Tinjauan atas permintaan pengguna: "cari kaedah entry, hold dan exit yang membolehkan beli kemudian untung", termasuk
indikator Moomoo beliau (MACD, Keltner, MA10/MA20, RSI, squeeze), cadangan pakar momentum swing, gabungan serentak dan
berturutan. **Ini tinjauan, BUKAN kajian pradaftar**: tiada gate ditetapkan sebelum data dilihat, dan bilangan ujian
sangat besar. Bacaannya di bawah mengambil kira hal itu.

Keputusan pengguna 12 Nov 2026: simpan kajian ini dan jejak empat calon dalam Papertrade C / Lejar
(`kajian/SPEC_JEJAK_KOMBINASI.md`). Kad skor kekal satu-satunya keputusan.

## Ringkasan

1. **Tiada isyarat beli yang menjadikan saham "naik terus".** 53 % belian naik selepas 10 sesi; hanya 12 % naik tanpa
   pernah turun lebih 1 % di bawah harga beli. Antara yang naik ≥ 10 % dalam 10 sesi, 71 % turun lebih 1 % dahulu.
2. **Cara pegang dan jual menentukan untung; isyarat beli hampir tidak.** Dengan peraturan "saham di atas ma50, jual
   selepas dua tutup di bawah ma50, henti −8 %", 45 isyarat beli memberi +0.1 % hingga +4.9 % setiap dagangan, dan
   "beli mana-mana hari" memberi +1.36 %. Kebanyakan isyarat berada di sekitar paras itu.
3. **Menjual awal membuang untung.** Keluar ikut MACD silang turun, EMA10 atau 10 hari memberi lebih kurang 0 %.
   Sasaran untung kalah kepada "biar lari".
4. **Henti −8 % ialah harga perlindungan, bukan sumber untung.** Ia memotong jangkaan (Chandelier +4.6 % → +2.3 %;
   keluar ma50 +2.0 % → +1.4 %) tetapi mengurangkan dagangan yang rugi lebih 15 % daripada 4.1 % kepada 0.5 %.
5. **Lebih banyak isyarat sepakat tidak menambah untung**, dan susunan isyarat tidak penting.
6. **Kombinasi "terbaik" dalam data lama tidak dapat dibezakan daripada nasib.** Daripada ~1.35 juta gabungan, yang
   lulus tapis ketat tidak lebih baik pada 498 saham lain berbanding gabungan dipilih rawak.

## 1. Data dan kaedah

| Perkara | Nilai |
|---|---|
| Set utama | `data_mentah/dataset_S1..S4.csv`: 431 saham (421 dengan sejarah cukup), bar harian 2019-01 hingga 2026-10 |
| Isyarat | 2020-01-02 hingga 2026-03-31 (252 bar pemanasan, 126 bar ke hadapan); 550,327 saham-hari layak |
| Layak | tutup ≥ USD 10 dan nilai dagangan purata 20 hari ≥ USD 1 juta |
| Set kedua ("saham lain") | 498 saham dalam `data/harga/stor` yang TIADA dalam set 431; isyarat 2025-09-26 hingga 2026-08-13; ufuk 60 bar |
| Masuk | isyarat dikira pada TUTUP bar *i* (data ≤ *i* sahaja); beli pada BUKA bar *i*+1 |
| Kos | 0.5 % pusingan |
| Henti | −8 % dari harga beli; kena dalam hari → keluar pada paras henti, atau pada buka jika buka di bawahnya |
| Keluar isyarat | syarat pada tutup → jual pada buka esok; ufuk maksimum 126 bar |

Kawalan yang dipakai, mengikut bahagian:

- **Lift terkawal** (§3): hasil ditolak purata semua saham layak pada **hari yang sama dan tercile ATR % yang sama**,
  mengikut reka bentuk `standard/lift_kaedah.py`. Tanpa padanan ATR, isyarat terlebih jual kelihatan baik hanya kerana
  ia memilih saham meruap.
- **Dua separuh tempoh** (2020–22, 2023–26) dan **kiraan tahun** yang positif.
- **Plasebo anjak-masa**: tarikh isyarat setiap saham dianjak secara rawak (≥ 60 bar), mengekalkan saham dan kekerapan
  tetapi memusnahkan pemasaan.
- **Saham lain**: semakan pada 498 saham berbeza. Hadnya: hanya 11 bulan, dan tempoh itu lemah bagi saham trend.
- **Kadar asas rawak** (§6): hasil pada saham lain bagi gabungan yang LULUS tapis dibandingkan dengan gabungan yang
  DIPILIH RAWAK daripada keluarga yang sama. Inilah semakan yang menentukan bacaan keseluruhan.

Semakan kod: contoh dagangan dikira semula dengan tangan daripada bar mentah (r5, r20, kejatuhan terdalam, nisbah
volum) dan sepadan. Dua artifak dikenal pasti dan dielakkan: (a) "lift" bagi keluar yang syaratnya sudah benar pada hari
beli (cth. beli rawak + jual bila MA10 < MA20) bersifat mekanikal; (b) kelebihan "MA20 silang MA50" terhadap semua saham
hilang apabila dibandingkan dengan "mana-mana hari di atas ma50".

## 2. Kadar asas: adakah entry "naik terus"?

Stor harga, 947 saham, Sep 2024 – Okt 2026, beli pada buka, 10 sesi (413,978 saham-hari):

| Ukuran | Nilai |
|---|---|
| Naik selepas 10 sesi | 53.5 % |
| Naik dan tidak pernah turun > 1 % di bawah harga beli | 12.4 % |
| Naik dan setiap tutup ≥ harga beli | 17.9 % |
| Kejatuhan terdalam median | −4.4 % (antara yang naik: −2.4 %) |
| Antara yang naik ≥ 10 %: turun > 1 % dahulu | 71 % |

Toleransi turun (10 sesi): dalam 1 % → 12 % naik dan kekal dalam had; 3 % → 32 %; 5 % → 43 %; 8 % → 50 %. Ini sepadan
dengan kadar menang 45–50 % yang dilaporkan pedagang momentum (Minervini; laporan sendiri, sumber sekunder).

Lejar langsung (16–28 Okt 2026, 144 kaedah dengan ≥ 50 belian): "naik tanpa turun > 1 %" purata 11.0 %, sama dengan
saham lain pada tarikh sama (11.5 %); kaedah tertinggi 27.6 %. Lejar baru 9 hari beli; angka setiap kaedah kasar.

## 3. Isyarat tunggal (45), lift terkawal

Asas semua saham-hari: untung selepas 20 hari 52.1 %, purata +0.92 %; capai +16 % sebelum −8 % (dalam 60 bar) 31.9 %;
kena −8 % dalam 60 bar 59.1 %.

Isyarat dengan lift 20 hari positif pada kedua-dua separuh dan ≥ 5 daripada 7 tahun:

| Isyarat | n | Lift r20 (mata) | 2020–22 / 2023–26 | Tahun | p plasebo |
|---|---|---|---|---|---|
| Lonjakan ≥ 4 % + volum 2× selepas "tidur" (ADX < 20, Bollinger sempit) | 553 | +2.29 | +1.93 / +2.51 | 6/7 | < 0.003 |
| RS ≥ 90 dan di atas ma50 (keadaan) | 45,254 | +0.90 | +0.56 / +1.17 | 6/7 | 0.01 |
| Templat trend Minervini (keadaan) | 150,190 | +0.43 | +0.16 / +0.67 | 6/7 | < 0.003 |
| RSI2 < 10 di atas ma200 | 30,114 | +0.24 | +0.23 / +0.25 | 6/7 | 0.06 |

Tiada kelebihan (lift ≈ 0 atau negatif): MACD silang naik (−0.04), MA10 silang MA20 (0.00), RSI silang 50 (+0.11),
Keltner (+0.23, satu separuh sahaja), squeeze lepas (−0.01), Supertrend (−0.08), Stochastic (−0.23), pecah tinggi 20/55
hari (+0.15 / +0.13), VCP (+0.27, satu separuh), gap and go (+0.07), episodic pivot (+0.14, n 429), Holy Grail (−0.72).
Jadual penuh: `isyarat_kombinasi/hasil/isyarat_tunggal.csv`, log `log/analisa.txt`.

**"Saham tidur yang melonjak"** teguh merentas 36 daripada 36 variasi tetapan pada set utama (lift purata +1.9 mata;
lonjakan yang sama pada saham yang sudah trending, ADX ≥ 25: −0.4), dan kelebihannya membesar dengan ufuk (5 hari +0.2,
20 hari +1.5, 60 hari +1.9). **Tetapi ia gagal pada saham lain** (n 114: 43 % untung selepas 20 hari, lift −0.2, selang
95 % [−3.0, +3.0]) dan lemah pada set utama sejak Sep 2025 (+0.2). Log `log/teguh.txt`, `log/sah.txt`.

## 4. Cara pegang dan jual

Beli setiap bar (tiada penapis), semua dengan henti −8 % kecuali dinyatakan:

| Cara jual | Jangkaan | Menang | Purata menang / rugi | Hari |
|---|---|---|---|---|
| Biar lari (henti −8 % sahaja, 126 bar) | +3.61 % | 29 % | +33 / −9 | 59 |
| TANPA henti: Chandelier 4×ATR | +3.03 % | 40 % | +21 / −9 | 46 |
| Chandelier 4×ATR | +1.68 % | 34 % | +20 / −7 | 36 |
| Sasaran +24 % | +1.47 % | 34 % | +21 / −9 | 40 |
| Tutup di bawah rendah 20 hari | +1.44 % | 29 % | +20 / −6 | 30 |
| TANPA henti: dua tutup di bawah ma50 | +1.09 % | 37 % | +12 / −5 | 22 |
| Dua tutup di bawah ma50 | +0.71 % | 35 % | +11 / −5 | 19 |
| Pegang 20 hari | +0.39 % | 45 % | +10 / −7 | 16 |
| MA10 di bawah MA20 | +0.04 % | 39 % | +6 / −4 | 10 |
| MACD silang turun | −0.17 % | 37 % | +5 / −4 | 7 |
| Tutup di bawah EMA10 | −0.30 % | 34 % | +5 / −3 | 6 |

Kepekaan paras henti ("henti sahaja"): 5 % → +3.0 %, 8 % → +4.7 %, 12 % → +6.7 %, 20 % → +9.3 % (angka ini daripada
larian `keluar8.py` dengan argumen 0.05 / 0.08 / 0.12 / 0.20, tanpa tapis harga ≥ USD 10; `log/baca8.txt` bagi 0.08). Pegang 126 hari tanpa apa-apa keluar: +14.5 %, mengatasi semua cara
jual setiap hari pegang — alam ini 431 saham yang terselamat dalam tempoh pasaran naik.

"Tanpa 5 %": jangkaan selepas membuang 5 % dagangan terbaik adalah negatif bagi hampir setiap cara jual. Untung datang
daripada segelintir pemenang besar, selaras dengan gate 3 kajian REVERSE.

## 5. Kaedah MA50 dan isyarat beli

Peraturan: saham di atas ma50 pada hari isyarat · henti −8 % · jual selepas dua tutup di bawah ma50.

| Isyarat beli | Jangkaan | Menang | Tahun untung | Saham lain |
|---|---|---|---|---|
| **Mana-mana hari (kawalan)** | **+1.36 %** | 31 % | 5/7 | +0.26 % |
| Golden cross ma50/ma200 | +2.03 % | 33 % | 4/7 | +1.67 % (n 116) |
| MA20 silang ma50 | +1.65 % | 32 % | 5/7 | +1.12 % (n 380) |
| RSI2 < 10 di atas ma200 | +1.41 % | 31 % | 4/7 | +1.01 % (n 886) |
| Supertrend naik | +1.60 % | 31 % | 6/7 | −0.47 % |
| MACD silang naik | +1.39 % | 30 % | 5/7 | +0.19 % |
| Keltner | +1.37 % | 33 % | 4/7 | −0.48 % |
| MA10 silang MA20 | +1.29 % | 30 % | 5/7 | −0.10 % |
| RSI silang 50 | +1.18 % | 28 % | 5/7 | +0.03 % |
| Squeeze lepas | +1.03 % | 30 % | 5/7 | −0.37 % |
| Episodic pivot | +4.89 % | 35 % | 5/7 | +0.33 % (n 51) |
| Saham tidur melonjak | +2.65 % | 33 % | 5/7 | −3.28 % (n 102) |

Kawalan ikut tahun (2020..2026): +5.2, −0.7, −2.3, +0.5, +0.2, +4.6, +1.7. Tahun lemah lemah bagi semua isyarat: kaedah
ini ikut-trend. Jadual penuh 45 isyarat: `log/kombo.txt`; 940 gabungan masuk × jual: `hasil/matriks_masuk_keluar.csv`.

## 6. Kombinasi serentak dan berturutan

Pusingan 1 (17 keadaan, 15 peristiwa): 20,082 gabungan serentak 4–6 dan 1,945 turutan 2–3 langkah (`log/turutan.txt`).
Pusingan 2 (31 keadaan, 29 peristiwa; indikator tambahan OBV, MFI, CCI, Williams %R, PSAR, Aroon, EMA8/21, CMF, trend
dan MACD mingguan, engulfing, hammer, NR7, inside day, gap): **1,345,507 gabungan** (`log/habis.txt`).

| Keluarga | Diuji | Purata | Korelasi pangkat 2020–22 lawan 2023–26 | Lulus tapis utama |
|---|---|---|---|---|
| Serentak 2 / 3 / 4 / 5 / 6 (31 keadaan) | 465 / 4,495 / 31,446 / 169,402 / 730,199 | +1.41 … +1.34 % | 0.00 … −0.21 | 3 / 14 / 164 / 1,138 / 6,075 |
| Serentak 7 / 8 / 9 (17 keadaan asal) | 17,197 / 19,490 / 16,961 | +1.21 / +1.15 / +1.10 % | −0.20 / −0.20 / −0.21 | 349 / 364 / 275 |
| Turutan 2 langkah (5 / 10 / 20 hari) | 755 / 787 / 809 | +1.45 / +1.49 / +1.51 % | +0.04 / +0.01 / −0.03 | 21 / 15 / 4 |
| Turutan 3 langkah (5 / 10 / 20 hari) | 12,925 / 17,769 / 20,922 | +1.53 / +1.56 / +1.58 % | +0.09 / +0.12 / +0.08 | 614 / 637 / 354 |
| Turutan 4 langkah (10 hari) | 301,885 | +1.63 % | +0.12 | 13,883 |

Tapis utama = n ≥ 300, lebihan atas kawalan > 0.3 mata pada kedua-dua separuh, untung ≥ 6 daripada 7 tahun. Kawalan +1.36 %.

**Semakan penentu: adakah lulus tapis meramal hasil pada saham lain?**

| Keluarga | Dipilih rawak: purata / mengatasi kawalan | Lulus tapis: purata / mengatasi kawalan |
|---|---|---|
| Serentak 4 | −0.10 % / 32 % | −0.36 % / 13 % |
| Serentak 6 | −0.65 % / 16 % | −0.90 % / 9 % |
| Turutan 3 langkah (10 hari) | −0.33 % / 31 % | −0.25 % / 36 % |
| Turutan 4 langkah | −0.35 % / 33 % | −0.29 % / 38 % |
| Turutan 3 langkah (20 hari) | +0.02 % / 43 % | +0.08 % / 44 % |

Lulus tapis tidak meramal hasil pada saham lain. Semakan kasar kedua: apabila hasil dikocok (anjak-masa), **lebih banyak**
gabungan lulus tapis utama (102,929) berbanding data sebenar (23,910) — tapis itu tidak memisahkan isyarat daripada
hingar. (Plasebo ini kasar: asas hasil terkocok berbeza daripada asas sebenar, jadi ia petunjuk, bukan ujian.)

Dapatan lain:

- **Bilangan keadaan hijau serentak** (daripada 17): 9–10 → +1.42 %, 11–12 → +1.58 %, 13–14 → +1.13 %, 15–17 → +1.04 %.
  Pada saham lain, lebih hijau lebih buruk.
- **Susunan tidak penting**: korelasi kesan susunan antara dua separuh = 0.00 (1,634 turutan dalam 306 set).
- **Contoh pengguna** (MACD silang naik → squeeze ON → MA10 silang MA20): +0.82 %, di bawah kawalan; saham lain −0.92 %.
- Senarai 4,361 gabungan pusingan 2 yang lulus tapis utama DAN positif pada saham lain disimpan dalam
  `isyarat_kombinasi/hasil/pusingan2_lulus_semua.csv` sebagai **rekod sahaja**. Jadual di atas menunjukkan kelulusan itu
  tidak bermaklumat; senarai itu bukan senarai cadangan.

### Pembetulan kepada bacaan awal

Selepas pusingan 1, tiga "corak yang bertahan" dilaporkan kepada pengguna (squeeze kedua; pecah–undur–sambung; golden
cross selepas momentum). Pusingan 2 menunjukkan bacaan itu terlalu yakin: "squeeze kedua" versi asas (squeeze ON +
squeeze lepas dalam 10 hari + ma50 > ma200) memberi −0.22 % pada saham lain; variasi yang dilaporkan positif ialah
pilihan daripada banyak variasi. Ketiga-tiganya tidak dibawa ke jejak hadapan.

## 7. Empat calon yang dijejak

Dipilih kerana ringkas, n besar atau menonjol pada kedua-dua set; **bukan** kerana terbukti. Angka di bawah ialah versi
yang dijejak (tanpa henti, keluar X36, di atas ma50); butiran dan sebab tiada henti dalam `SPEC_JEJAK_KOMBINASI.md`.

| ID | Masuk | Jangkaan (n) | Saham lain (n) |
|---|---|---|---|
| `N201X36` | MA20 silang ma50 | +2.40 % (5,254) | +1.20 % (380) |
| `N202X36` | RSI2 < 10, di atas ma200 | +1.76 % (13,987) | +1.62 % (886) |
| `N203X36` | gap naik 2 % dalam 10 hari, kemudian MA20 silang ma50 | +6.01 % (1,424) | +0.46 % (83) |
| `N204X36` | undur RSI2 < 10 → gap naik 2 % → RSI14 silang 50 (5 hari setiap langkah) | +4.68 % (922) | +3.38 % (68) |
| `N76X36` (kawalan sedia ada) | mana-mana hari di atas ma50 | +2.01 % (310,876) | +0.90 % (22,377) |
| `N06X36` (sedia ada) | golden cross | +2.69 % (1,725) | +3.13 % (120) |

`N203X36`: MA20 silang ma50 **tanpa** gap dalam 20 hari memberi +0.12 % pada set utama tetapi +1.37 % pada saham lain,
iaitu arah bertentangan — sebab ia dianggap calon paling lemah walaupun angkanya paling tinggi.

## 8. Pandangan pakar (sumber sekunder, laporan sendiri)

Minervini: kadar menang lebih kurang 45–50 %, rugi dihadkan 5–8 %. Qullamaggie: 25–35 %, pemenang berkali ganda risiko.
O'Neil: jual tanpa pengecualian pada −7 hingga −8 %; "tiga daripada sepuluh sudah hebat". Bulkowski: breakout bervolum
tinggi kerap berpatah balik ke paras breakout. Tiada yang mendakwa entry tanpa turun; semuanya bergantung pada rugi kecil
dan menang besar. Pautan dalam sejarah sesi; angka tidak diaudit.

## 9. Had

- **Bukan pradaftar; ~1.35 juta ujian.** Setiap "terbaik" di sini dipilih selepas melihat data.
- **Survivorship**: 431 saham set utama semuanya masih wujud; jangkaan dan "purata menang" condong ke atas.
- **Setiap dagangan, bukan portfolio**: tiada had slot, tiada MDD akaun, tiada perbandingan SPUS. Kajian portfolio repo
  (`REVERSE/SISTEM.md`) mendapati tiada sistem mengalahkan SPUS + tunai pada pendedahan sama.
- **Isyarat bertindih**: setiap hari isyarat dikira; tiada ujian signifikan dua hala (saham, minggu) dibuat.
- **Saham lain** hanya 11 bulan dalam satu fasa pasaran.
- **Tidak diliputi**: tetapan indikator lain, ≥ 7 keadaan daripada 31, turutan ≥ 5 langkah, cara jual lain bagi setiap
  gabungan, data asas, berita, earnings.

## 10. Jana semula

`bash kajian/isyarat_kombinasi/jalan_semua.sh <folder kerja di luar repo>` (≈ 10 minit; `HABIS=1` menambah pusingan 2,
≈ 35 minit). Fail perantaraan `*.pkl` (sehingga ~1 GB) ditulis ke folder kerja dan tidak dikomit. Benih rawak ditetapkan.

| Skrip | Bahagian |
|---|---|
| `panel.py` | isyarat, keadaan, peristiwa dan hasil setiap saham-hari (set utama dan saham lain) |
| `analisa.py`, `teguh.py`, `sah.py` | §3: lift terkawal, keteguhan tetapan, saham lain, plasebo |
| `keluar8.py`, `baca8.py` | §4: henti × cara jual × isyarat (larian pertama) |
| `moomoo5.py` | lima isyarat Moomoo dan gabungannya |
| `matriks.py`, `kombo.py` | §5: 940 gabungan masuk × jual; 45 isyarat dan 890 pasangan dengan kaedah MA50 |
| `turutan.py`, `habis.py` | §6: pusingan 1 dan 2 |
| `semak2.py`, `semak3.py` | §6: teras calon dan kadar asas rawak pada saham lain |
| `pradaftar.py` | §7 dan angka `SPEC_JEJAK_KOMBINASI.md` |
| `simpan_hasil.py` | eksport jadual kecil ke `hasil/` (dikomit); log setiap skrip dalam `log/` |

Jana semula 12 Nov 2026 daripada skrip dalam repo menghasilkan log pusingan 1 yang identik dengan larian asal. Log
`log/habis.txt` ialah larian asal pusingan 2 (tidak dijana semula kerana ≈ 35 minit).
