# CS25: stop loss × pegang × jual bagi SETIAP setup F, ikut untung terbesar (backtest; BUKAN bukti)

Peraturan ditulis dahulu: `kajian/SPEC_CARIAN_SETUP.md` pindaan 20 Nov 2026 (al). Dijana `cs_keluar25.py`; jangan sunting.

- Permintaan pengguna 20 Nov 2026: kaji stop loss, masa pegang dan masa jual bagi SEMUA setup F, untuk untung terbesar dan rugi terkecil.
- 2,802 kod dalam registry F; 2,745 dinilai (57 tidak dapat dijana semula dalam mod tanpa intai: CS13 25, CS06 18, CS04 8, CS07 6); 2,745 ada ≥ 30 dagangan dalam kedua-dua kumpulan saham dan masuk bacaan.
- 4,320 cara setiap setup: 8 stop loss × 2 "naikkan stop loss ke harga beli" × 3 pegang minimum × 15 "trend tamat" × 3 "jual separuh" × 2 had masa. Peraturan beli tidak diubah; kadar tangkap tidak terkesan.
- Cara dipilih pada saham carian; semua angka di bawah dibaca pada saham yang carian tidak lihat (nilai tengah merentas setup), kos 0.5 %.
- Semakan pariti: cara sekarang sama dengan enjin CS14 pada 305 setup (beza terbesar 0.0000000) → lulus.

## 1. Keputusan (ujian ditetapkan dahulu)

- **Cara `U`: stop loss 6×ATR dari harga beli · tiada jualan ikut trend · had 12 bulan** (`s6.b0.m3.t0.j0.h252`; dipilih pada saham carian). Pada saham yang carian tidak lihat, lawan cara sekarang: (1) purata lebih tinggi bagi 2,742 daripada 2,745 setup → ya; (2) belian 2025–26: beza purata +12.1 mata (2,537 daripada 2,615 setup lebih tinggi; perlu > 0) → ya; (3) tambahan bagi setup +7.7 mata lawan tambahan bagi saham rawak +9.7 mata (perlu lebih besar) → TIDAK. **Keputusan: TIDAK menolong.** Beza kadar menang -3.7 mata; beza rugi ≥ 15 % +25.8 mata.
- **Cara `S`: stop loss 8 % dari harga beli · tiada jualan ikut trend · had 12 bulan** (`p8.b0.m3.t0.j0.h252`; dipilih pada saham carian). Pada saham yang carian tidak lihat, lawan cara sekarang: (1) purata lebih tinggi bagi 2,717 daripada 2,745 setup → ya; (2) belian 2025–26: beza purata +5.1 mata (2,441 daripada 2,620 setup lebih tinggi; perlu > 0) → ya; (3) tambahan bagi setup +3.7 mata lawan tambahan bagi saham rawak +4.2 mata (perlu lebih besar) → TIDAK; (4) beza rugi ≥ 15 % -5.2 mata (perlu ≤ +2) → ya. **Keputusan: TIDAK menolong.** Beza kadar menang -23.4 mata; beza rugi ≥ 15 % -5.2 mata.
- **Cara tersendiri setiap setup (`Ui`) lawan satu cara `U` untuk semua:** purata `Ui` lebih tinggi bagi 351 daripada 2,745 setup; nilai tengah beza +0.00 mata (perlu lebih separuh DAN ≥ +0.1) → **TIDAK menolong: satu cara untuk semua sama baik**. `Si` lawan `S`: 1,182 daripada 2,745; beza +0.00 mata → **TIDAK menolong**.

## 2. Cara sekarang lawan cara terpilih (saham yang carian tidak lihat)

| Cara | Purata setiap dagangan % | Menang % | Rugi ≥ 15 % % | Untung ≥ 50 % % | Hari pegang (nilai tengah) | Untung setiap 20 hari pegang % | Saham rawak, cara sama: purata · menang · rugi ≥ 15 % |
|---|---|---|---|---|---|---|---|
| Cara sekarang: stop loss 4×ATR dari harga beli · pegang sekurang-kurangnya 20 hari, kemudian jual bila tutup di bawah purata 20 hari · had 6 bulan | +0.8 | 47 | 7 | 1.0 | 21 | +0.63 | +0.7 · 47 · 6 |
| `U` untung terbesar: stop loss 6×ATR dari harga beli · tiada jualan ikut trend · had 12 bulan | +8.4 | 43 | 34 | 12.6 | 222 | +1.02 | +10.4 · 46 · 34 |
| `S` untung terbesar tanpa menambah rugi besar: stop loss 8 % dari harga beli · tiada jualan ikut trend · had 12 bulan | +4.3 | 24 | 2 | 7.5 | 40 | +0.96 | +4.9 · 22 · 2 |
| `E` untung terbesar setiap hari pegang (maklumat): stop loss 3×ATR dari harga beli · naikkan stop loss ke harga beli selepas naik 2×ATR · tiada jualan ikut trend · had 12 bulan | +3.2 | 13 | 7 | 5.9 | 27 | +0.99 | +4.2 · 15 · 9 |
| `Ui` cara tersendiri setiap setup (untung terbesar) | +8.3 | 43 | 42 | – | 220 | – | – |
| `Si` cara tersendiri setiap setup (tanpa menambah rugi besar) | +4.5 | 25 | 5 | – | 42 | – | – |

Lajur terakhir = 300,000 belian rawak pada saham yang sama, dijual dengan cara yang sama. Jika angka saham rawak naik sama banyak, tambahan itu datang daripada memegang saham lebih lama dalam data ini (pasaran naik, tiada saham mati), bukan daripada setup.

## 3. Tangga: jual lebih lewat = purata lebih besar, tetapi rugi besar lebih kerap (stop loss 4×ATR, pegang minimum 20 hari)

Kiri = semua 2,745 setup; kanan = 757 setup "Setiap minggu" (senarai kerja rasmi; tambahan selepas hasil dilihat).

| Tanda jual | Semua: purata % · menang % · rugi ≥ 15 % % · hari | Setiap minggu: purata % · menang % · rugi ≥ 15 % % · hari | Saham rawak: purata · menang · rugi ≥ 15 % |
|---|---|---|---|
| tutup di bawah purata 20 hari | +0.8 · 47 · 7 · 21 | +1.1 · 46 · 15 · 21 | +0.7 · 47 · 6 |
| tutup di bawah purata 50 hari | +1.2 · 41 · 7 · 24 | +1.5 · 41 · 15 · 23 | +1.1 · 45 · 6 |
| jatuh 4×ATR dari tutup tertinggi | +2.1 · 39 · 10 · 41 | +2.8 · 39 · 23 · 42 | +2.4 · 41 · 11 |
| jatuh 15 % dari tutup tertinggi | +2.5 · 39 · 10 · 48 | +2.7 · 39 · 21 · 38 | +2.8 · 41 · 12 |
| jatuh 8×ATR dari tutup tertinggi | +3.5 · 39 · 15 · 81 | +4.5 · 39 · 35 · 87 | +3.8 · 42 · 17 |
| tiada (pegang 6 bulan) | +3.6 · 40 · 17 · 93 | +5.0 · 41 · 39 · 110 | +4.1 · 43 · 18 |

## 4. Kesan setiap komponen, satu demi satu (lima yang lain kekal seperti cara sekarang)

| Komponen | Pilihan | Purata % | Menang % | Rugi ≥ 15 % % | Untung ≥ 50 % % | Hari pegang | Setiap 20 hari % | 2025–26: beza purata (mata) | Saham rawak: purata · menang · rugi ≥ 15 % |
|---|---|---|---|---|---|---|---|---|---|
| Stop loss | stop loss 2×ATR dari harga beli | +0.4 | 39 | 2 | 0.8 | 21 | +0.49 | -0.2 | +0.4 · 40 · 2 |
| Stop loss | stop loss 3×ATR dari harga beli | +0.6 | 45 | 5 | 0.9 | 21 | +0.58 | -0.0 | +0.6 · 45 · 4 |
| Stop loss | stop loss 4×ATR dari harga beli **(asas)** | +0.8 | 47 | 7 | 1.0 | 21 | +0.63 | +0.0 | +0.7 · 47 · 6 |
| Stop loss | stop loss 6×ATR dari harga beli | +0.9 | 48 | 9 | 1.0 | 22 | +0.65 | +0.0 | +0.8 · 48 · 7 |
| Stop loss | stop loss 8 % dari harga beli | +0.5 | 42 | 1 | 0.8 | 21 | +0.46 | -0.2 | +0.4 · 42 · 1 |
| Stop loss | stop loss 15 % dari harga beli | +0.7 | 46 | 17 | 0.9 | 21 | +0.57 | -0.0 | +0.6 · 47 · 14 |
| Stop loss | stop loss 3×ATR ikut harga tutup | +0.7 | 46 | 7 | 0.9 | 21 | +0.62 | -0.1 | +0.7 · 46 · 5 |
| Stop loss | stop loss 4×ATR ikut harga tutup | +0.8 | 47 | 8 | 1.0 | 22 | +0.65 | +0.0 | +0.7 · 47 · 6 |
| Naikkan stop loss ke harga beli | tiada **(asas)** | +0.8 | 47 | 7 | 1.0 | 21 | +0.63 | +0.0 | +0.7 · 47 · 6 |
| Naikkan stop loss ke harga beli | naikkan stop loss ke harga beli selepas naik 2×ATR | +0.7 | 41 | 7 | 0.9 | 21 | +0.60 | -0.0 | +0.6 · 41 · 6 |
| Pegang minimum | 3 hari | -0.0 | 38 | 3 | 0.4 | 7 | -0.04 | -0.4 | -0.1 · 37 · 1 |
| Pegang minimum | 10 hari | +0.3 | 43 | 5 | 0.7 | 13 | +0.38 | -0.3 | +0.2 · 42 · 3 |
| Pegang minimum | 20 hari **(asas)** | +0.8 | 47 | 7 | 1.0 | 21 | +0.63 | +0.0 | +0.7 · 47 · 6 |
| Trend tamat | tiada peraturan trend (stop loss dan had masa sahaja) | +3.6 | 40 | 17 | 5.6 | 93 | +0.93 | +7.1 | +4.1 · 43 · 18 |
| Trend tamat | tutup di bawah purata 10 hari | +0.7 | 49 | 7 | 0.7 | 21 | +0.63 | -0.0 | +0.5 · 49 · 6 |
| Trend tamat | tutup di bawah purata 20 hari **(asas)** | +0.8 | 47 | 7 | 1.0 | 21 | +0.63 | +0.0 | +0.7 · 47 · 6 |
| Trend tamat | tutup di bawah purata 50 hari | +1.2 | 41 | 7 | 2.0 | 24 | +0.75 | +1.1 | +1.1 · 45 · 6 |
| Trend tamat | tutup di bawah purata 100 hari | +1.9 | 37 | 8 | 3.1 | 30 | +0.88 | +2.4 | +1.4 · 44 · 7 |
| Trend tamat | dua tutup berturut-turut di bawah purata 20 hari | +0.8 | 45 | 7 | 1.1 | 23 | +0.63 | +0.3 | +0.8 · 46 · 6 |
| Trend tamat | dua tutup berturut-turut di bawah purata 50 hari | +1.4 | 40 | 8 | 2.3 | 27 | +0.76 | +1.6 | +1.3 · 43 · 6 |
| Trend tamat | jatuh 3×ATR dari tutup tertinggi | +1.5 | 41 | 8 | 2.3 | 30 | +0.77 | +1.7 | +1.5 · 42 · 8 |
| Trend tamat | jatuh 4×ATR dari tutup tertinggi | +2.1 | 39 | 10 | 3.6 | 41 | +0.84 | +3.8 | +2.4 · 41 · 11 |
| Trend tamat | jatuh 6×ATR dari tutup tertinggi | +3.1 | 38 | 14 | 5.1 | 65 | +0.90 | +5.8 | +3.5 · 41 · 15 |
| Trend tamat | jatuh 8×ATR dari tutup tertinggi | +3.5 | 39 | 15 | 5.5 | 81 | +0.92 | +6.7 | +3.8 · 42 · 17 |
| Trend tamat | tutup di bawah harga terendah 10 hari | +1.1 | 44 | 9 | 1.7 | 29 | +0.64 | +0.9 | +1.2 · 46 · 8 |
| Trend tamat | tutup di bawah harga terendah 20 hari | +1.8 | 40 | 9 | 2.9 | 36 | +0.80 | +2.8 | +1.9 · 41 · 9 |
| Trend tamat | jatuh 15 % dari tutup tertinggi | +2.5 | 39 | 10 | 3.6 | 48 | +0.84 | +2.3 | +2.8 · 41 · 12 |
| Trend tamat | jatuh 25 % dari tutup tertinggi | +3.4 | 39 | 14 | 5.2 | 71 | +0.93 | +5.7 | +3.8 · 42 · 17 |
| Jual separuh semasa naik | tiada **(asas)** | +0.8 | 47 | 7 | 1.0 | 21 | +0.63 | +0.0 | +0.7 · 47 · 6 |
| Jual separuh semasa naik | jual separuh selepas naik 10 % | +0.6 | 50 | 7 | 0.3 | 21 | +0.50 | -0.4 | +0.6 · 49 · 6 |
| Jual separuh semasa naik | jual separuh selepas naik 20 % | +0.7 | 47 | 7 | 0.4 | 21 | +0.56 | -0.3 | +0.7 · 47 · 6 |
| Had masa | had 6 bulan **(asas)** | +0.8 | 47 | 7 | 1.0 | 21 | +0.63 | +0.0 | +0.7 · 47 · 6 |
| Had masa | had 12 bulan | +0.8 | 47 | 7 | 1.0 | 21 | +0.63 | +0.0 | +0.7 · 47 · 6 |

## 5. Sama, bagi setup "Setiap minggu" sahaja (tambahan selepas hasil dilihat; maklumat)

| Komponen | Pilihan | Purata % | Menang % | Rugi ≥ 15 % % | Untung ≥ 50 % % | Hari pegang | Setiap 20 hari % | 2025–26: beza purata (mata) | Saham rawak: purata · menang · rugi ≥ 15 % |
|---|---|---|---|---|---|---|---|---|---|
| Stop loss | stop loss 2×ATR dari harga beli | +0.7 | 40 | 5 | 1.7 | 21 | +0.69 | -0.6 | +0.4 · 40 · 2 |
| Stop loss | stop loss 3×ATR dari harga beli | +0.9 | 45 | 13 | 1.9 | 21 | +0.80 | -0.2 | +0.6 · 45 · 4 |
| Stop loss | stop loss 4×ATR dari harga beli **(asas)** | +1.1 | 46 | 15 | 2.0 | 21 | +0.89 | +0.0 | +0.7 · 47 · 6 |
| Stop loss | stop loss 6×ATR dari harga beli | +1.2 | 47 | 14 | 2.0 | 22 | +0.94 | +0.1 | +0.8 · 48 · 7 |
| Stop loss | stop loss 8 % dari harga beli | +0.6 | 37 | 1 | 1.5 | 19 | +0.62 | -0.9 | +0.4 · 42 · 1 |
| Stop loss | stop loss 15 % dari harga beli | +0.9 | 45 | 27 | 1.8 | 21 | +0.74 | -0.2 | +0.6 · 47 · 14 |
| Stop loss | stop loss 3×ATR ikut harga tutup | +1.1 | 46 | 14 | 2.0 | 21 | +0.86 | -0.1 | +0.7 · 46 · 5 |
| Stop loss | stop loss 4×ATR ikut harga tutup | +1.2 | 47 | 15 | 2.0 | 22 | +0.91 | +0.1 | +0.7 · 47 · 6 |
| Naikkan stop loss ke harga beli | tiada **(asas)** | +1.1 | 46 | 15 | 2.0 | 21 | +0.89 | +0.0 | +0.7 · 47 · 6 |
| Naikkan stop loss ke harga beli | naikkan stop loss ke harga beli selepas naik 2×ATR | +1.0 | 41 | 14 | 1.9 | 21 | +0.81 | -0.2 | +0.6 · 41 · 6 |
| Pegang minimum | 3 hari | +0.0 | 37 | 2 | 0.6 | 5 | +0.08 | -1.8 | -0.1 · 37 · 1 |
| Pegang minimum | 10 hari | +0.4 | 41 | 8 | 1.1 | 12 | +0.50 | -1.1 | +0.2 · 42 · 3 |
| Pegang minimum | 20 hari **(asas)** | +1.1 | 46 | 15 | 2.0 | 21 | +0.89 | +0.0 | +0.7 · 47 · 6 |
| Trend tamat | tiada peraturan trend (stop loss dan had masa sahaja) | +5.0 | 41 | 39 | 9.7 | 110 | +1.17 | +9.1 | +4.1 · 43 · 18 |
| Trend tamat | tutup di bawah purata 10 hari | +1.0 | 49 | 15 | 1.4 | 21 | +0.86 | -0.3 | +0.5 · 49 · 6 |
| Trend tamat | tutup di bawah purata 20 hari **(asas)** | +1.1 | 46 | 15 | 2.0 | 21 | +0.89 | +0.0 | +0.7 · 47 · 6 |
| Trend tamat | tutup di bawah purata 50 hari | +1.5 | 41 | 15 | 2.8 | 23 | +0.92 | +1.6 | +1.1 · 45 · 6 |
| Trend tamat | tutup di bawah purata 100 hari | +2.1 | 38 | 16 | 4.4 | 26 | +1.09 | +3.1 | +1.4 · 44 · 7 |
| Trend tamat | dua tutup berturut-turut di bawah purata 20 hari | +1.2 | 45 | 16 | 2.4 | 23 | +0.84 | +0.5 | +0.8 · 46 · 6 |
| Trend tamat | dua tutup berturut-turut di bawah purata 50 hari | +1.7 | 39 | 16 | 3.2 | 25 | +0.98 | +2.0 | +1.3 · 43 · 6 |
| Trend tamat | jatuh 3×ATR dari tutup tertinggi | +1.8 | 41 | 18 | 4.1 | 31 | +0.94 | +2.1 | +1.5 · 42 · 8 |
| Trend tamat | jatuh 4×ATR dari tutup tertinggi | +2.8 | 39 | 23 | 6.0 | 42 | +1.05 | +4.8 | +2.4 · 41 · 11 |
| Trend tamat | jatuh 6×ATR dari tutup tertinggi | +4.0 | 38 | 31 | 8.7 | 68 | +1.12 | +7.3 | +3.5 · 41 · 15 |
| Trend tamat | jatuh 8×ATR dari tutup tertinggi | +4.5 | 39 | 35 | 9.4 | 87 | +1.14 | +8.5 | +3.8 · 42 · 17 |
| Trend tamat | tutup di bawah harga terendah 10 hari | +1.4 | 44 | 19 | 3.1 | 30 | +0.79 | +1.2 | +1.2 · 46 · 8 |
| Trend tamat | tutup di bawah harga terendah 20 hari | +2.3 | 40 | 21 | 5.0 | 38 | +0.99 | +3.7 | +1.9 · 41 · 9 |
| Trend tamat | jatuh 15 % dari tutup tertinggi | +2.7 | 39 | 21 | 5.7 | 38 | +1.01 | +2.8 | +2.8 · 41 · 12 |
| Trend tamat | jatuh 25 % dari tutup tertinggi | +4.3 | 39 | 33 | 8.8 | 70 | +1.16 | +6.9 | +3.8 · 42 · 17 |
| Jual separuh semasa naik | tiada **(asas)** | +1.1 | 46 | 15 | 2.0 | 21 | +0.89 | +0.0 | +0.7 · 47 · 6 |
| Jual separuh semasa naik | jual separuh selepas naik 10 % | +0.9 | 51 | 14 | 0.6 | 21 | +0.69 | -0.8 | +0.6 · 49 · 6 |
| Jual separuh semasa naik | jual separuh selepas naik 20 % | +1.0 | 47 | 15 | 0.9 | 21 | +0.80 | -0.6 | +0.7 · 47 · 6 |
| Had masa | had 6 bulan **(asas)** | +1.1 | 46 | 15 | 2.0 | 21 | +0.89 | +0.0 | +0.7 · 47 · 6 |
| Had masa | had 12 bulan | +1.1 | 46 | 15 | 2.0 | 21 | +0.89 | +0.0 | +0.7 · 47 · 6 |

## 6. Kesan setiap komponen, satu demi satu (lima yang lain kekal seperti cara `U`)

| Komponen | Pilihan | Purata % | Menang % | Rugi ≥ 15 % % | Untung ≥ 50 % % | Hari pegang | Setiap 20 hari % | 2025–26: beza purata (mata) | Saham rawak: purata · menang · rugi ≥ 15 % |
|---|---|---|---|---|---|---|---|---|---|
| Stop loss | stop loss 2×ATR dari harga beli | +3.7 | 18 | 4 | 7.0 | 22 | +1.01 | +5.0 | +5.0 · 21 · 6 |
| Stop loss | stop loss 3×ATR dari harga beli | +5.2 | 26 | 11 | 9.1 | 52 | +1.02 | +7.3 | +6.9 · 29 · 16 |
| Stop loss | stop loss 4×ATR dari harga beli | +6.5 | 32 | 20 | 10.7 | 94 | +1.03 | +9.2 | +8.3 · 36 · 24 |
| Stop loss | stop loss 6×ATR dari harga beli **(asas)** | +8.4 | 43 | 34 | 12.6 | 222 | +1.02 | +12.1 | +10.4 · 46 · 34 |
| Stop loss | stop loss 8 % dari harga beli | +4.3 | 24 | 2 | 7.5 | 40 | +0.96 | +5.1 | +4.9 · 22 · 2 |
| Stop loss | stop loss 15 % dari harga beli | +6.9 | 39 | 58 | 10.6 | 152 | +0.98 | +8.7 | +8.0 · 37 · 60 |
| Stop loss | stop loss 3×ATR ikut harga tutup | +6.1 | 30 | 17 | 10.2 | 72 | +1.06 | +8.5 | +7.6 · 33 · 21 |
| Stop loss | stop loss 4×ATR ikut harga tutup | +7.3 | 36 | 25 | 11.5 | 125 | +1.06 | +10.3 | +9.0 · 39 · 28 |
| Naikkan stop loss ke harga beli | tiada **(asas)** | +8.4 | 43 | 34 | 12.6 | 222 | +1.02 | +12.1 | +10.4 · 46 · 34 |
| Naikkan stop loss ke harga beli | naikkan stop loss ke harga beli selepas naik 2×ATR | +4.7 | 17 | 17 | 7.3 | 56 | +1.01 | +7.0 | +5.8 · 20 · 17 |
| Pegang minimum | 3 hari **(asas)** | +8.4 | 43 | 34 | 12.6 | 222 | +1.02 | +12.1 | +10.4 · 46 · 34 |
| Pegang minimum | 10 hari | +8.4 | 43 | 34 | 12.6 | 222 | +1.02 | +12.1 | +10.4 · 46 · 34 |
| Pegang minimum | 20 hari | +8.4 | 43 | 34 | 12.6 | 222 | +1.02 | +12.1 | +10.4 · 46 · 34 |
| Trend tamat | tiada peraturan trend (stop loss dan had masa sahaja) **(asas)** | +8.4 | 43 | 34 | 12.6 | 222 | +1.02 | +12.1 | +10.4 · 46 · 34 |
| Trend tamat | tutup di bawah purata 10 hari | -0.1 | 40 | 3 | 0.3 | 6 | -0.31 | -0.8 | -0.2 · 36 · 1 |
| Trend tamat | tutup di bawah purata 20 hari | -0.0 | 39 | 3 | 0.4 | 7 | -0.05 | -0.5 | -0.1 · 37 · 1 |
| Trend tamat | tutup di bawah purata 50 hari | +0.4 | 37 | 4 | 1.2 | 10 | +0.39 | +0.4 | +0.0 · 38 · 1 |
| Trend tamat | tutup di bawah purata 100 hari | +1.2 | 36 | 5 | 2.5 | 19 | +0.64 | +1.9 | +0.3 · 39 · 2 |
| Trend tamat | dua tutup berturut-turut di bawah purata 20 hari | +0.1 | 39 | 3 | 0.6 | 9 | +0.10 | -0.1 | -0.1 · 37 · 1 |
| Trend tamat | dua tutup berturut-turut di bawah purata 50 hari | +0.6 | 37 | 4 | 1.5 | 15 | +0.47 | +1.0 | +0.1 · 38 · 2 |
| Trend tamat | jatuh 3×ATR dari tutup tertinggi | +1.3 | 40 | 8 | 2.2 | 29 | +0.71 | +1.1 | +1.4 · 41 · 7 |
| Trend tamat | jatuh 4×ATR dari tutup tertinggi | +2.5 | 40 | 13 | 4.0 | 44 | +0.88 | +4.6 | +2.7 · 42 · 12 |
| Trend tamat | jatuh 6×ATR dari tutup tertinggi | +5.1 | 40 | 21 | 7.8 | 82 | +0.98 | +9.6 | +5.7 · 42 · 21 |
| Trend tamat | jatuh 8×ATR dari tutup tertinggi | +6.8 | 40 | 27 | 10.4 | 120 | +1.01 | +12.5 | +7.8 · 42 · 27 |
| Trend tamat | tutup di bawah harga terendah 10 hari | +0.6 | 38 | 6 | 1.3 | 19 | +0.50 | +0.2 | +0.5 · 35 · 3 |
| Trend tamat | tutup di bawah harga terendah 20 hari | +1.5 | 37 | 8 | 2.6 | 30 | +0.73 | +2.3 | +1.4 · 34 · 5 |
| Trend tamat | jatuh 15 % dari tutup tertinggi | +3.3 | 39 | 15 | 5.5 | 63 | +0.82 | +3.0 | +3.5 · 40 · 17 |
| Trend tamat | jatuh 25 % dari tutup tertinggi | +6.4 | 40 | 28 | 9.9 | 118 | +0.95 | +9.7 | +7.5 · 42 · 31 |
| Jual separuh semasa naik | tiada **(asas)** | +8.4 | 43 | 34 | 12.6 | 222 | +1.02 | +12.1 | +10.4 · 46 · 34 |
| Jual separuh semasa naik | jual separuh selepas naik 10 % | +5.1 | 48 | 21 | 4.7 | 222 | +0.62 | +6.6 | +6.1 · 51 · 21 |
| Jual separuh semasa naik | jual separuh selepas naik 20 % | +5.9 | 51 | 27 | 6.0 | 222 | +0.71 | +7.6 | +7.0 · 53 · 27 |
| Had masa | had 6 bulan | +4.6 | 49 | 26 | 6.1 | 126 | +0.95 | +9.4 | +5.0 · 51 · 25 |
| Had masa | had 12 bulan **(asas)** | +8.4 | 43 | 34 | 12.6 | 222 | +1.02 | +12.1 | +10.4 · 46 · 34 |

## 7. Ikut kumpulan setup (maklumat; pemilihan diulang dalam kumpulan itu pada saham carian)

| Kumpulan | Setup | Cara | Purata % | Menang % | Rugi ≥ 15 % % | Hari pegang | Lebih baik daripada cara sekarang | 2025–26: beza purata (mata) | Saham rawak: purata |
|---|---|---|---|---|---|---|---|---|---|
| Setiap minggu | 757 | cara sekarang | +1.1 | 46 | 15 | 21 | – | – | +0.7 |
| Setiap minggu | 757 | `U` kumpulan ini: stop loss 6×ATR dari harga beli · tiada jualan ikut trend · had 12 bulan | +11.6 | 44 | 43 | 252 | 757 / 757 | +14.9 | +10.4 |
| Setiap minggu | 757 | `S` kumpulan ini: stop loss 2×ATR dari harga beli · tiada jualan ikut trend · had 12 bulan | +5.4 | 19 | 10 | 25 | 757 / 757 | +7.1 | +5.0 |
| Setiap minggu | 757 | `U` semua setup | +11.6 | 44 | 43 | 252 | 757 / 757 | +14.9 | +10.4 |
| Setiap minggu | 757 | `S` semua setup | +4.5 | 17 | 2 | 18 | 757 / 757 | +5.5 | +4.9 |
| Musim laporan kewangan | 1,847 | cara sekarang | +0.4 | 47 | 6 | 21 | – | – | +0.7 |
| Musim laporan kewangan | 1,847 | `U` kumpulan ini: stop loss 6×ATR dari harga beli · tiada jualan ikut trend · had 12 bulan | +7.1 | 42 | 30 | 197 | 1846 / 1847 | +10.3 | +10.4 |
| Musim laporan kewangan | 1,847 | `S` kumpulan ini: stop loss 8 % dari harga beli · tiada jualan ikut trend · had 12 bulan | +4.2 | 26 | 2 | 49 | 1838 / 1847 | +5.0 | +4.9 |
| Musim laporan kewangan | 1,847 | `U` semua setup | +7.1 | 42 | 30 | 197 | 1846 / 1847 | +10.3 | +10.4 |
| Musim laporan kewangan | 1,847 | `S` semua setup | +4.2 | 26 | 2 | 49 | 1838 / 1847 | +5.0 | +4.9 |
| Keadaan tertentu | 86 | cara sekarang | +1.4 | 46 | 18 | 21 | – | – | +0.7 |
| Keadaan tertentu | 86 | `U` kumpulan ini: stop loss 6×ATR dari harga beli · tiada jualan ikut trend · had 12 bulan | +10.5 | 42 | 51 | 252 | 84 / 86 | +12.6 | +10.4 |
| Keadaan tertentu | 86 | `S` kumpulan ini: stop loss 2×ATR dari harga beli · tiada jualan ikut trend · had 12 bulan | +5.3 | 19 | 16 | 30 | 73 / 86 | +6.4 | +5.0 |
| Keadaan tertentu | 86 | `U` semua setup | +10.5 | 42 | 51 | 252 | 84 / 86 | +12.6 | +10.4 |
| Keadaan tertentu | 86 | `S` semua setup | +4.2 | 15 | 2 | 15 | 73 / 86 | +4.1 | +4.9 |
| Lain-lain | 28 | cara sekarang | +1.6 | 47 | 17 | 22 | – | – | +0.7 |
| Lain-lain | 28 | `U` kumpulan ini: stop loss 6×ATR dari harga beli · tiada jualan ikut trend · had 12 bulan | +11.0 | 46 | 46 | 252 | 28 / 28 | +17.4 | +10.4 |
| Lain-lain | 28 | `S` kumpulan ini: stop loss 8 % dari harga beli · tiada jualan ikut trend · had 12 bulan | +4.2 | 15 | 2 | 16 | 24 / 28 | +4.1 | +4.9 |
| Lain-lain | 28 | `U` semua setup | +11.0 | 46 | 46 | 252 | 28 / 28 | +17.4 | +10.4 |
| Lain-lain | 28 | `S` semua setup | +4.2 | 15 | 2 | 16 | 24 / 28 | +4.1 | +4.9 |
| Tiada dalam senarai CS23 | 27 | cara sekarang | +3.8 | 55 | 13 | 23 | – | – | +0.7 |
| Tiada dalam senarai CS23 | 27 | `U` kumpulan ini: stop loss 6×ATR dari harga beli · tiada jualan ikut trend · had 12 bulan | +19.2 | 53 | 38 | 252 | 27 / 27 | +17.5 | +10.4 |
| Tiada dalam senarai CS23 | 27 | `S` kumpulan ini: stop loss 2×ATR dari harga beli · tiada jualan ikut trend · had 12 bulan | +12.3 | 28 | 14 | 41 | 25 / 27 | +7.7 | +5.0 |
| Tiada dalam senarai CS23 | 27 | `U` semua setup | +19.2 | 53 | 38 | 252 | 27 / 27 | +17.5 | +10.4 |
| Tiada dalam senarai CS23 | 27 | `S` semua setup | +8.4 | 20 | 2 | 25 | 25 / 27 | +4.9 | +4.9 |

## 8. Cara tersendiri setiap setup: apa yang dipilih (`Ui`, pada saham carian)

| Komponen | Bahagian setup yang memilih setiap pilihan |
|---|---|
| Stop loss | `s6` 68 % · `p15` 28 % · `c4` 3 % · `c3` 1 % |
| Naikkan stop loss ke harga beli | `b0` 100 % |
| Pegang minimum | `m3` 97 % · `m20` 2 % · `m10` 1 % |
| Trend tamat | `t0` 94 % · `t14` 5 % · `t13` 1 % · `t10` 1 % |
| Jual separuh | `j0` 100 % |
| Had masa | `h252` 99 % · `h126` 1 % |

Pada saham yang carian tidak lihat, `Ui` memberi purata +8.3 % (nilai tengah), lawan cara sekarang +7.61 mata (2,738 daripada 2,745 setup lebih tinggi). Jadual setiap setup: `setup.csv.gz`.

## 9. Sepuluh cara teratas pada saham carian, dan bacaannya pada saham yang carian tidak lihat

Cara tanpa peraturan trend adalah sama bagi tiga pilihan pegang minimum; ia ditunjuk sekali.

| Cara | Saham carian: beza purata (mata) | Tidak dilihat: purata % | Menang % | Rugi ≥ 15 % % | Hari pegang | Saham rawak: purata |
|---|---|---|---|---|---|---|
| stop loss 6×ATR dari harga beli · tiada jualan ikut trend · had 12 bulan | +7.1 | +8.4 | 43 | 34 | 222 | +10.4 |
| stop loss 4×ATR ikut harga tutup · tiada jualan ikut trend · had 12 bulan | +6.3 | +7.3 | 36 | 25 | 125 | +9.0 |
| stop loss 15 % dari harga beli · tiada jualan ikut trend · had 12 bulan | +6.3 | +6.9 | 39 | 58 | 152 | +8.0 |
| stop loss 6×ATR dari harga beli · pegang sekurang-kurangnya 20 hari, kemudian jual bila jatuh 25 % dari tutup tertinggi · had 12 bulan | +5.7 | +6.4 | 41 | 28 | 119 | +7.6 |
| stop loss 6×ATR dari harga beli · pegang sekurang-kurangnya 10 hari, kemudian jual bila jatuh 25 % dari tutup tertinggi · had 12 bulan | +5.6 | +6.4 | 41 | 28 | 118 | +7.5 |
| stop loss 4×ATR dari harga beli · tiada jualan ikut trend · had 12 bulan | +5.6 | +6.5 | 32 | 20 | 94 | +8.3 |
| stop loss 6×ATR dari harga beli · pegang sekurang-kurangnya 3 hari, kemudian jual bila jatuh 25 % dari tutup tertinggi · had 12 bulan | +5.5 | +6.4 | 40 | 28 | 118 | +7.5 |
| stop loss 6×ATR dari harga beli · pegang sekurang-kurangnya 3 hari, kemudian jual bila jatuh 8×ATR dari tutup tertinggi · had 12 bulan | +5.5 | +6.8 | 40 | 27 | 120 | +7.8 |
| stop loss 6×ATR dari harga beli · pegang sekurang-kurangnya 20 hari, kemudian jual bila jatuh 8×ATR dari tutup tertinggi · had 12 bulan | +5.5 | +6.8 | 40 | 27 | 120 | +7.8 |
| stop loss 6×ATR dari harga beli · pegang sekurang-kurangnya 10 hari, kemudian jual bila jatuh 8×ATR dari tutup tertinggi · had 12 bulan | +5.5 | +6.8 | 40 | 27 | 120 | +7.8 |

Semua 4,320 cara: `cara.csv.gz`.

## 10. Kaveat

- Tiada saham mati dalam data: untung daripada memegang lama condong ke atas, dan lebih condong bagi cara yang memegang lebih lama.
- 4,320 cara dicuba setiap setup; cara terbaik pada saham carian condong ke atas. Sebab itu bacaan dibuat pada saham yang carian tidak lihat.
- Saham yang carian tidak lihat sudah dipakai berkali-kali; 2025–26 pendek.
- Stop loss ikut harga tutup boleh rugi lebih daripada parasnya; "naikkan stop loss ke harga beli" menganggap jualan tepat pada harga beli; "jual separuh" dikenakan kos sekali sahaja.
- Tiada perubahan pada registry F, senarai utama, Top 100 atau dashboard: menukar stop loss atau cara jual berdaftar ialah keputusan pengguna.
- Pangkat backtest, BUKAN bukti.
