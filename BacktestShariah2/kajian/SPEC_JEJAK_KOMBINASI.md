# SPEC_JEJAK_KOMBINASI — pradaftar jejak hadapan kohort KOMBINASI MA50

**Dipradaftar 12 Nov 2026**, dikomit bersama modul `kod/kaedah/N201X36.py`–`N204X36.py` dan **sebelum mana-mana
isyaratnya dibeli**. Keputusan pengguna 12 Nov 2026: "ya, simpan kajian ke repo dan jejak dalam papertrade"
(`koordinator/keputusan.csv`). Tinjauan sumber: `kajian/KAJIAN_ISYARAT_KOMBINASI.md`.

## 1. Apa ini, dan apa ia BUKAN

Ini **bukan** pengesahan kelebihan yang sudah diukur. Tinjauan menguji lebih kurang 1.35 juta gabungan isyarat pada data
lama dan mendapati:

- purata setiap keluarga gabungan hampir sama dengan "beli mana-mana hari saham di atas ma50";
- gabungan yang lulus tapis ketat pada set utama **tidak lebih baik** pada 498 saham lain berbanding gabungan yang
  dipilih rawak (jadual §6 tinjauan);
- pangkat gabungan pada 2020–22 tidak meramal pangkatnya pada 2023–26 (korelasi pangkat −0.21 hingga +0.12).

Maka empat kaedah di bawah ialah **calon yang tidak dapat dibezakan daripada nasib**. Jejak ini ialah **ujian pertama
yang jujur** bagi mereka. Ia juga satu pengecualian yang diluluskan pengguna kepada peraturan "jangan tambah baris MASUK
Nxx baharu" (`CLAUDE.md`); pengecualian itu terhad kepada empat modul ini.

## 2. Kohort

Semua: beli pada BUKA esok (C01) · **tiada henti, tiada sasaran** · lorong 1 = `X36` (keluar selepas DUA tutup berturut di
bawah `ma50`, jual pada buka esok) · lorong 2 = `X15` Chandelier tutup 4×ATR14 (automatik) · `TMAX` 126 · `rank` = U14.
Setiap masuk mewajibkan `tutup > ma50` pada bar isyarat. Formula dalam `kod/kaedah/_kombo.py` (salinan formula tinjauan).

| ID | Masuk (pada tutup bar isyarat) | Sebab dipilih |
|---|---|---|
| `N201X36` | `ma20` silang naik `ma50` | isyarat tunggal yang untung pada kedua-dua set saham |
| `N202X36` | `rsi2 < 10` DAN `tutup > ma200` | sama; "beli masa undur dalam trend naik" |
| `N203X36` | `buka > tinggi[-1] × 1.02` pada mana-mana daripada 10 bar terakhir, DAN `ma20` silang naik `ma50` | turutan paling menonjol pusingan 2 |
| `N204X36` | `rsi2` silang ke bawah 10, kemudian (dalam 5 bar) `buka > tinggi[-1] × 1.02`, kemudian (dalam 5 bar) `rsi14` silang naik 50 | turutan paling menonjol pusingan 2 |

Dua kaedah **sedia ada** dibaca bersebelahan sebagai rujukan, tanpa modul baharu:

| ID | Peranan |
|---|---|
| `N76X36` (`tutup > ma50` × X36) | **kawalan**: "beli mana-mana hari saham di atas ma50" dengan cara keluar yang sama |
| `N06X36` (golden cross `ma50`/`ma200` × X36) | isyarat tunggal ketiga yang untung pada kedua-dua set; sudah dijejak sejak 3 Nov 2026 |

## 3. Kenapa tiada henti −8%

Pengguna meminta toleransi turun −8%. Tinjauan mengukur kedua-dua versi. Jejak ini memakai versi **tanpa henti** kerana:

1. Gate G4 kad skor ialah "henti pada hari beli = sifar secara struktur" (`SPEC_KAD_SKOR.md`, pindaan 6 Nov 2026). Henti
   −8% dari harga beli boleh kena pada hari beli; satu kejadian sahaja menjadikan kaedah itu GAGAL selama-lamanya.
2. 94 kohort Nxx sedia ada semuanya tanpa henti; memakai konfigurasi sama menjadikan `N76X36` kawalan yang sah.
3. Versi henti −8% **masih boleh dibaca kemudian** daripada rekod yang sama: Lejar menyimpan `mae_pct` setiap posisi.

Harga keputusan ini, daripada tinjauan (rujukan `N76X36`): tanpa henti jangkaan lebih tinggi (+2.01 % lawan +1.36 %)
tetapi 4.1 % dagangan rugi lebih 15 % (dengan henti: 0.5 %).

## 4. Angka tinjauan (jangkaan priori, BUKAN janji)

431 saham (`data_mentah/dataset_S1..S4`), isyarat 2020-01 hingga 2026-03, kos 0.5 % pusingan, keluar X36 tanpa henti,
ufuk 126 bar. "Saham lain" = 498 saham stor yang tiada dalam set 431, isyarat 2025-09 hingga 2026-08.

| ID | n | Jangkaan | 2020–22 | 2023–26 | Menang | Purata menang / rugi | Rugi > 15 % | Saham lain (n) |
|---|---|---|---|---|---|---|---|---|
| `N201X36` | 5,254 | +2.40 % | +2.06 | +2.66 | 35.9 % | +19.4 / −7.1 | 4.5 % | +1.20 % (380) |
| `N202X36` | 13,987 | +1.76 % | +1.20 | +2.17 | 32.1 % | +16.6 / −5.3 | 2.3 % | +1.62 % (886) |
| `N203X36` | 1,424 | +6.01 % | +6.37 | +5.73 | 43.4 % | +24.8 / −8.4 | 6.7 % | +0.46 % (83) |
| `N204X36` | 922 | +4.68 % | +4.42 | +4.88 | 32.5 % | +27.7 / −6.4 | 3.5 % | +3.38 % (68) |
| `N06X36` (rujukan) | 1,725 | +2.69 % | +3.32 | +2.28 | 36.0 % | +19.1 / −6.5 | 4.1 % | +3.13 % (120) |
| `N76X36` (kawalan) | 310,876 | +2.01 % | +1.39 | +2.49 | 33.7 % | +18.9 / −6.6 | 4.1 % | +0.90 % (22,377) |

Ikut tahun (2020..2026), jangkaan %: `N201X36` 10.9, −0.0, −2.4, 1.6, 0.5, 4.8, 8.6 · `N202X36` 4.7, −0.0, −1.1, −0.4,
1.3, 5.5, 3.5 · `N203X36` 18.5, 0.0, −1.4, 3.9, 1.0, 8.6, 21.0 · `N204X36` 9.2, −1.1, 1.1, 1.6, 4.2, 6.5, 9.7 ·
`N76X36` 6.8, −0.7, −2.3, 0.5, 0.4, 6.1, 4.0. **Tahun lemah (2021, 2022, 2024) lemah bagi semua, termasuk kawalan**: ini
kaedah ikut-trend dan untungnya datang daripada pasaran yang naik.

**Jangkaan priori saya, ditulis sebelum data hadapan:** paling banyak satu daripada empat akan menunjukkan lift masuk
positif (G3) yang lulus; jangkaan langsung keempat-empatnya akan berada dalam ±1 mata `N76X36`; `N203X36` akan mengecut
paling banyak kerana ia dipilih daripada carian terbesar dan paling lemah pada saham lain. Priori saya dalam repo ini
terbukti tidak bermaklumat (`REVERSE/NXX_KELUAR.md` §1); ia direkod supaya boleh disemak, bukan untuk dipercayai.

## 5. Beza antara tinjauan dan produksi (sebab nombor tidak akan sepadan)

1. Tinjauan mengira **setiap hari isyarat** (bertindih); enjin produksi mengambil yang pertama dan mengabaikan isyarat
   semasa memegang. Paling terkesan: `N202X36` (keadaan, bukan peristiwa).
2. Alam tinjauan = 431 saham yang masih wujud hari ini (tiada delist): setiap jangkaan condong ke atas.
3. Tinjauan menolak kos 0.5 % pusingan; Lejar memakai kosnya sendiri.
4. Papertrade C mengehadkan 10 isyarat baharu setiap kaedah setiap imbasan, dipilih ikut `rank` U14; tinjauan tidak
   memilih.
5. Tinjauan ialah jangkaan SETIAP DAGANGAN; ia tidak mengukur portfolio, MDD akaun atau perbandingan dengan SPUS.

## 6. Bagaimana keputusan dibuat

- **Satu-satunya keputusan ialah kad skor** (`laporan/KAD_SKOR.md`, gate G1–G6 tidak berubah). Tiada gate baharu, tiada
  ambang khas untuk kohort ini.
- **Penyebut**: hanya isyarat bertarikh ≥ **2026-11-12** dikira LANGSUNG (`lift_kaedah.MULA_KOHORT`; `SPEC_KAD_SKOR.md`
  pindaan 12 Nov 2026). Baris lebih awal (hanya boleh wujud melalui bina semula Lejar) ialah isian.
- **Bacaan maklumat (bukan gate)**: jangkaan setiap kaedah dibaca bersebelahan `N76X36` pada tempoh yang sama. Kaedah
  yang tidak mengatasi `N76X36` tidak menambah apa-apa kepada peraturan pegang dan jual.
- Label cantas C1–C5 (`laporan/CANTAS.md`) terpakai seperti kaedah lain.

## 7. Yang dikunci

Parameter (`GAP_MIN` 1.02, `TINGKAP_GAP` 10, `TINGKAP_LANGKAH` 5, `rsi2 < 10`, keluar `X36`, tarikh 2026-11-12) dikunci
`ujian/test_kombo_ma50.py`. Mengubah mana-mana daripadanya menghasilkan kaedah LAIN dan memerlukan ID baharu serta
pradaftar baharu. **Tiada kohort tambahan boleh diambil daripada tinjauan ini**: tinjauan itu sudah menunjukkan bahawa
memilih lebih banyak "pemenang" daripadanya hanya menambah bilangan yang lulus kerana nasib.

## 8. Yang belum dibuat

- Dokumen db dashboard `kaedah/katalog` belum ditolak; buat selepas modul berada di `main` (`standard/dashboard.md` §4).
- Ujian portfolio (10 slot, MDD akaun −10 %, lawan SPUS) belum dibuat bagi mana-mana kaedah ini.
