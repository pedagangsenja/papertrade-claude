# CS26: stop loss × pegang × jual HABIS-HABISAN bagi setiap setup F, ikut "untung berbanding rugi" (backtest; BUKAN bukti)

Peraturan ditulis dahulu: `kajian/SPEC_CARIAN_SETUP.md` pindaan 20 Nov 2026 (am). Dijana `cs_keluar26.py` / `cs_keluar26_lapor.py`; jangan sunting.

- Soalan pengguna 20 Nov 2026: "betul ke method ni sahaja utk stop loss, hold dan exit? anda sudah lakukan kajian habis habisan?" Ukuran pilihan pengguna: jumlah untung jauh lebih besar daripada jumlah rugi (sasaran: sekurang-kurangnya 2 kali).
- 2,802 kod dalam registry F; 2,745 dinilai; 2,745 masuk bacaan (757 daripadanya "Setiap minggu").
- Ruang cara: 40,734,720 gabungan daripada 10 komponen (13 stop loss × 5 "potong awal" × 34 tanda trend × 8 "bila mula" × 4 "ketatkan" × 8 "ambil untung" × 3 "naik stop ke harga beli" × 3 pasaran × 2 laporan kewangan × 4 had masa). Dinilai: 8,280 cara (75 satu demi satu, 8,000 rawak, 205 naik bukit).
- **Untung : rugi** = jumlah untung semua dagangan ÷ jumlah rugi semua dagangan sesuatu setup, selepas kos 0.5 %. 1.00 = pulang modal; 2.00 = untung dua kali rugi.
- Cara dipilih pada saham carian; angka dibaca pada saham yang carian tidak lihat (nilai tengah merentas setup).
- Pariti dengan CS25: 151 cara × 125 setup, beza terbesar 0.0000000 → lulus.

## 1. Keputusan (ujian ditetapkan dahulu)

- **Cara `F` (untung : rugi tertinggi): stop loss 15 % · naikkan stop loss ke harga beli selepas naik 10 % · had 12 bulan** (`p15|n0|t0|m3|k0|j0|b2|q0|e0|h252`). Pada saham yang carian tidak lihat, lawan cara sekarang: (1) nisbah lebih tinggi bagi 2,709 daripada 2,745 setup → ya; (2) belian 2025–26: beza nisbah +0.75 (2,379 daripada 2,619 setup lebih tinggi; perlu > 0) → ya; (3) tambahan nisbah bagi setup +0.61 lawan tambahan bagi saham rawak +0.64 (perlu lebih besar) → TIDAK. **Keputusan: TIDAK menolong.** (4) Sasaran pengguna (nisbah ≥ 2): nisbah 1.74 → **TIDAK tercapai** (saham rawak dengan cara sama: 1.82).
- **Cara `G` tidak wujud:** tiada satu pun cara yang dinilai mencapai nilai tengah untung : rugi ≥ 2 pada saham carian.
- **Berapa cara mencapai sasaran ≥ 2 (nilai tengah merentas setup):** 0 daripada 8,280 pada saham carian; 0 pada saham yang carian tidak lihat.
- **Cara tersendiri setiap setup (`Fi`) lawan satu cara `F` untuk semua:** nisbah `Fi` lebih tinggi bagi 461 daripada 2,745 setup; nilai tengah beza -0.16 (perlu lebih separuh DAN ≥ +0.05) → **TIDAK menolong: satu cara untuk semua sama baik** (nisbah `Fi` 1.60).

## 2. Cara sekarang lawan cara terpilih

| Cara | Untung : rugi | Purata % | Menang % | Rugi ≥ 15 % | Purata untung (menang) % | Purata rugi (kalah) % | Hari pegang | Saham rawak: untung : rugi · purata % |
|---|---|---|---|---|---|---|---|---|
| Cara sekarang: stop loss 4×ATR · jual bila tutup di bawah purata 20 hari (mulai hari ke-20) · had 6 bulan | 1.16 | +0.8 | 47 | 7 | +11.2 | −8.6 | 21 | 1.17 · +0.7 |
| `F`: stop loss 15 % · naikkan stop loss ke harga beli selepas naik 10 % · had 12 bulan | 1.74 | +4.8 | 23 | 37 | +48.6 | −8.1 | 69 | 1.82 · +5.3 |

Lajur terakhir = 300,000 belian rawak pada saham yang sama, dijual dengan cara yang sama. Jika saham rawak mendapat nisbah yang sama, kelebihan itu datang daripada cara jual dan pasaran, bukan daripada setup.

## 3. Setiap komponen, satu demi satu (sembilan yang lain kekal seperti cara sekarang)

| Komponen | Pilihan | Untung : rugi | Purata % | Menang % | Rugi ≥ 15 % | Purata untung % | Purata rugi % | Hari | Setiap minggu: untung : rugi · purata % · rugi ≥ 15 % | Saham rawak: untung : rugi · purata % |
|---|---|---|---|---|---|---|---|---|---|---|
| Stop loss awal | stop loss 2×ATR | 1.10 | +0.4 | 39 | 2 | +11.6 | −6.8 | 21 | 1.13 · +0.7 · 5 | 1.10 · +0.4 |
| Stop loss awal | stop loss 3×ATR | 1.13 | +0.6 | 45 | 5 | +11.3 | −8.0 | 21 | 1.17 · +0.9 · 13 | 1.15 · +0.6 |
| Stop loss awal | stop loss 4×ATR **(sekarang)** | 1.16 | +0.8 | 47 | 7 | +11.2 | −8.6 | 21 | 1.19 · +1.1 · 15 | 1.17 · +0.7 |
| Stop loss awal | stop loss 6×ATR | 1.17 | +0.9 | 48 | 9 | +11.2 | −8.9 | 22 | 1.22 · +1.2 · 14 | 1.19 · +0.8 |
| Stop loss awal | stop loss 5 % | 1.06 | +0.2 | 35 | 1 | +11.1 | −5.8 | 13 | 1.08 · +0.3 · 1 | 1.06 · +0.2 |
| Stop loss awal | stop loss 8 % | 1.10 | +0.5 | 42 | 1 | +11.0 | −7.3 | 21 | 1.12 · +0.6 · 1 | 1.10 · +0.4 |
| Stop loss awal | stop loss 10 % | 1.11 | +0.5 | 44 | 1 | +10.9 | −7.9 | 21 | 1.13 · +0.7 · 1 | 1.12 · +0.5 |
| Stop loss awal | stop loss 15 % | 1.14 | +0.7 | 46 | 17 | +11.0 | −8.7 | 21 | 1.16 · +0.9 · 27 | 1.16 · +0.6 |
| Stop loss awal | stop loss 3×ATR ikut harga tutup | 1.15 | +0.7 | 46 | 7 | +11.2 | −8.4 | 21 | 1.19 · +1.1 · 14 | 1.17 · +0.7 |
| Stop loss awal | stop loss 4×ATR ikut harga tutup | 1.17 | +0.8 | 47 | 8 | +11.2 | −8.7 | 22 | 1.21 · +1.2 · 15 | 1.18 · +0.7 |
| Stop loss awal | stop loss di bawah harga terendah hari isyarat | 1.02 | +0.1 | 25 | 1 | +12.3 | −4.1 | 4 | 1.04 · +0.1 · 1 | 0.96 · -0.1 |
| Stop loss awal | stop loss di bawah harga terendah 10 hari sebelum beli | 1.08 | +0.3 | 37 | 3 | +11.7 | −6.1 | 19 | 1.10 · +0.4 · 3 | 1.07 · +0.2 |
| Stop loss awal | stop loss di bawah harga terendah 20 hari sebelum beli | 1.10 | +0.4 | 40 | 4 | +11.6 | −6.8 | 21 | 1.12 · +0.6 · 5 | 1.08 · +0.3 |
| Potong belian yang tidak menjadi | tiada **(sekarang)** | 1.16 | +0.8 | 47 | 7 | +11.2 | −8.6 | 21 | 1.19 · +1.1 · 15 | 1.17 · +0.7 |
| Potong belian yang tidak menjadi | jual jika hari ke-5 masih rugi | 1.08 | +0.3 | 37 | 4 | +11.4 | −6.2 | 16 | 1.11 · +0.5 · 7 | 1.07 · +0.2 |
| Potong belian yang tidak menjadi | jual jika hari ke-10 masih rugi | 1.11 | +0.5 | 40 | 5 | +11.4 | −6.9 | 21 | 1.15 · +0.7 · 9 | 1.11 · +0.4 |
| Potong belian yang tidak menjadi | jual jika hari ke-10 belum naik 1×ATR | 1.09 | +0.4 | 44 | 5 | +9.4 | −6.8 | 11 | 1.11 · +0.5 · 8 | 1.07 · +0.2 |
| Potong belian yang tidak menjadi | jual jika hari ke-20 masih rugi | 1.16 | +0.7 | 46 | 7 | +11.2 | −8.3 | 21 | 1.19 · +1.1 · 15 | 1.17 · +0.7 |
| Tanda trend tamat | tiada tanda trend | 1.45 | +3.6 | 40 | 17 | +29.0 | −13.1 | 93 | 1.48 · +5.0 · 39 | 1.53 · +4.1 |
| Tanda trend tamat | tutup di bawah purata 10 hari | 1.14 | +0.7 | 49 | 7 | +10.5 | −8.8 | 21 | 1.17 · +1.0 · 15 | 1.14 · +0.5 |
| Tanda trend tamat | tutup di bawah purata 20 hari **(sekarang)** | 1.16 | +0.8 | 47 | 7 | +11.2 | −8.6 | 21 | 1.19 · +1.1 · 15 | 1.17 · +0.7 |
| Tanda trend tamat | tutup di bawah purata 50 hari | 1.24 | +1.2 | 41 | 7 | +14.3 | −8.4 | 24 | 1.26 · +1.5 · 15 | 1.26 · +1.1 |
| Tanda trend tamat | tutup di bawah purata 100 hari | 1.34 | +1.9 | 37 | 8 | +18.6 | −8.9 | 30 | 1.35 · +2.1 · 16 | 1.32 · +1.4 |
| Tanda trend tamat | dua tutup berturut-turut di bawah purata 20 hari | 1.17 | +0.8 | 45 | 7 | +12.0 | −8.6 | 23 | 1.20 · +1.2 · 16 | 1.19 · +0.8 |
| Tanda trend tamat | dua tutup berturut-turut di bawah purata 50 hari | 1.27 | +1.4 | 40 | 8 | +15.4 | −8.5 | 27 | 1.29 · +1.7 · 16 | 1.29 · +1.3 |
| Tanda trend tamat | tutup di bawah EMA 10 hari | 1.14 | +0.7 | 48 | 7 | +10.6 | −8.7 | 21 | 1.18 · +1.0 · 15 | 1.15 · +0.6 |
| Tanda trend tamat | tutup di bawah EMA 20 hari | 1.16 | +0.8 | 46 | 7 | +11.3 | −8.5 | 21 | 1.19 · +1.1 · 15 | 1.17 · +0.7 |
| Tanda trend tamat | tutup lebih 1×ATR di bawah purata 20 hari | 1.20 | +1.1 | 43 | 8 | +14.1 | −8.9 | 27 | 1.22 · +1.4 · 17 | 1.25 · +1.2 |
| Tanda trend tamat | tutup lebih 1×ATR di bawah purata 50 hari | 1.31 | +1.7 | 38 | 8 | +17.8 | −8.7 | 33 | 1.34 · +2.1 · 16 | 1.34 · +1.6 |
| Tanda trend tamat | purata 10 hari di bawah purata 20 hari | 1.19 | +0.9 | 45 | 8 | +12.3 | −8.6 | 22 | 1.22 · +1.3 · 16 | 1.21 · +0.9 |
| Tanda trend tamat | purata 20 hari di bawah purata 50 hari | 1.29 | +1.6 | 40 | 9 | +16.8 | −9.2 | 33 | 1.29 · +1.8 · 17 | 1.30 · +1.4 |
| Tanda trend tamat | tutup di bawah harga terendah 5 hari | 1.16 | +0.8 | 47 | 8 | +12.0 | −9.2 | 25 | 1.19 · +1.1 · 18 | 1.19 · +0.8 |
| Tanda trend tamat | tutup di bawah harga terendah 10 hari | 1.19 | +1.1 | 44 | 9 | +13.9 | −9.4 | 29 | 1.21 · +1.4 · 19 | 1.25 · +1.2 |
| Tanda trend tamat | tutup di bawah harga terendah 20 hari | 1.30 | +1.8 | 40 | 9 | +18.3 | −9.6 | 36 | 1.32 · +2.3 · 21 | 1.36 · +1.9 |
| Tanda trend tamat | tutup di bawah lembah (swing low) terakhir | 1.19 | +1.0 | 45 | 8 | +13.5 | −9.2 | 27 | 1.21 · +1.3 · 18 | 1.23 · +1.1 |
| Tanda trend tamat | tiga tutup turun berturut-turut | 1.16 | +0.9 | 47 | 9 | +12.3 | −9.5 | 26 | 1.18 · +1.1 · 18 | 1.19 · +0.9 |
| Tanda trend tamat | Parabolic SAR bertukar turun | 1.14 | +0.7 | 48 | 7 | +10.8 | −8.8 | 21 | 1.16 · +0.9 · 16 | 1.14 · +0.6 |
| Tanda trend tamat | Supertrend bertukar turun | 1.24 | +1.2 | 42 | 8 | +14.6 | −8.7 | 24 | 1.27 · +1.6 · 16 | 1.28 · +1.2 |
| Tanda trend tamat | MACD di bawah garis isyarat | 1.14 | +0.7 | 48 | 8 | +10.8 | −8.9 | 21 | 1.17 · +1.0 · 16 | 1.16 · +0.7 |
| Tanda trend tamat | RSI14 di bawah 50 | 1.18 | +0.9 | 45 | 7 | +11.9 | −8.4 | 22 | 1.20 · +1.1 · 15 | 1.20 · +0.8 |
| Tanda trend tamat | +DI di bawah −DI | 1.19 | +0.9 | 45 | 7 | +12.1 | −8.5 | 22 | 1.22 · +1.2 · 15 | 1.20 · +0.8 |
| Tanda trend tamat | hari turun dengan volum ≥ 1.5× biasa | 1.23 | +1.3 | 47 | 10 | +14.4 | −10.3 | 31 | 1.26 · +1.8 · 22 | 1.28 · +1.4 |
| Tanda trend tamat | jatuh 2×ATR dari tutup tertinggi | 1.17 | +0.9 | 45 | 8 | +12.5 | −8.7 | 23 | 1.20 · +1.2 · 16 | 1.20 · +0.9 |
| Tanda trend tamat | jatuh 3×ATR dari tutup tertinggi | 1.26 | +1.5 | 41 | 8 | +16.2 | −9.1 | 30 | 1.28 · +1.8 · 18 | 1.30 · +1.5 |
| Tanda trend tamat | jatuh 4×ATR dari tutup tertinggi | 1.34 | +2.1 | 39 | 10 | +20.8 | −9.9 | 41 | 1.36 · +2.8 · 23 | 1.40 · +2.4 |
| Tanda trend tamat | jatuh 6×ATR dari tutup tertinggi | 1.42 | +3.1 | 38 | 14 | +27.2 | −11.6 | 65 | 1.44 · +4.0 · 31 | 1.50 · +3.5 |
| Tanda trend tamat | jatuh 8×ATR dari tutup tertinggi | 1.44 | +3.5 | 39 | 15 | +28.7 | −12.5 | 81 | 1.46 · +4.5 · 35 | 1.51 · +3.8 |
| Tanda trend tamat | jatuh 3×ATR dari harga tertinggi (Chandelier asal) | 1.21 | +1.1 | 43 | 8 | +14.2 | −8.8 | 26 | 1.23 · +1.5 · 17 | 1.25 · +1.2 |
| Tanda trend tamat | jatuh 10 % dari tutup tertinggi | 1.27 | +1.6 | 41 | 8 | +17.8 | −9.4 | 33 | 1.26 · +1.7 · 17 | 1.32 · +1.8 |
| Tanda trend tamat | jatuh 15 % dari tutup tertinggi | 1.36 | +2.5 | 39 | 10 | +22.9 | −10.6 | 48 | 1.35 · +2.7 · 21 | 1.42 · +2.8 |
| Tanda trend tamat | jatuh 20 % dari tutup tertinggi | 1.42 | +3.1 | 39 | 12 | +26.1 | −11.6 | 61 | 1.43 · +3.7 · 28 | 1.47 · +3.4 |
| Tanda trend tamat | jatuh 25 % dari tutup tertinggi | 1.44 | +3.4 | 39 | 14 | +27.6 | −12.3 | 71 | 1.47 · +4.3 · 33 | 1.51 · +3.8 |
| Bila tanda trend mula dipakai | mulai hari ke-3 | 0.99 | -0.0 | 38 | 3 | +8.4 | −5.4 | 7 | 1.01 · +0.0 · 2 | 0.93 · -0.1 |
| Bila tanda trend mula dipakai | mulai hari ke-10 | 1.08 | +0.3 | 43 | 5 | +9.9 | −6.8 | 13 | 1.10 · +0.4 · 8 | 1.07 · +0.2 |
| Bila tanda trend mula dipakai | mulai hari ke-20 **(sekarang)** | 1.16 | +0.8 | 47 | 7 | +11.2 | −8.6 | 21 | 1.19 · +1.1 · 15 | 1.17 · +0.7 |
| Bila tanda trend mula dipakai | mulai hari ke-40 | 1.21 | +1.2 | 47 | 10 | +14.6 | −10.6 | 41 | 1.25 · +1.8 · 24 | 1.27 · +1.4 |
| Bila tanda trend mula dipakai | hanya selepas naik 5 % | 1.17 | +0.8 | 55 | 9 | +9.5 | −10.5 | 22 | 1.19 · +1.0 · 17 | 1.21 · +0.9 |
| Bila tanda trend mula dipakai | hanya selepas naik 10 % | 1.22 | +1.4 | 54 | 11 | +13.2 | −12.5 | 31 | 1.23 · +1.5 · 24 | 1.27 · +1.6 |
| Bila tanda trend mula dipakai | hanya selepas naik 20 % | 1.29 | +2.2 | 46 | 14 | +20.2 | −13.0 | 48 | 1.30 · +2.6 · 32 | 1.36 · +2.5 |
| Bila tanda trend mula dipakai | hanya selepas naik 50 % | 1.38 | +3.1 | 40 | 16 | +27.1 | −13.1 | 75 | 1.40 · +3.9 · 38 | 1.47 · +3.7 |
| Ketatkan selepas untung besar | tiada **(sekarang)** | 1.16 | +0.8 | 47 | 7 | +11.2 | −8.6 | 21 | 1.19 · +1.1 · 15 | 1.17 · +0.7 |
| Ketatkan selepas untung besar | selepas naik 20 %: jual bila tutup di bawah purata 10 hari | 1.12 | +0.6 | 47 | 7 | +10.8 | −8.6 | 21 | 1.15 · +0.9 · 15 | 1.15 · +0.6 |
| Ketatkan selepas untung besar | selepas naik 20 %: jual bila jatuh 2×ATR dari tutup tertinggi | 1.14 | +0.7 | 47 | 7 | +11.0 | −8.6 | 21 | 1.17 · +1.0 · 15 | 1.16 · +0.7 |
| Ketatkan selepas untung besar | selepas naik 50 %: jual bila tutup di bawah purata 10 hari | 1.15 | +0.7 | 47 | 7 | +11.2 | −8.6 | 21 | 1.18 · +1.1 · 15 | 1.17 · +0.7 |
| Ambil untung | tiada **(sekarang)** | 1.16 | +0.8 | 47 | 7 | +11.2 | −8.6 | 21 | 1.19 · +1.1 · 15 | 1.17 · +0.7 |
| Ambil untung | jual separuh selepas naik 10 % | 1.13 | +0.6 | 50 | 7 | +9.9 | −8.6 | 21 | 1.16 · +0.9 · 14 | 1.15 · +0.6 |
| Ambil untung | jual separuh selepas naik 20 % | 1.14 | +0.7 | 47 | 7 | +10.8 | −8.6 | 21 | 1.18 · +1.0 · 15 | 1.17 · +0.7 |
| Ambil untung | jual semua selepas naik 20 % | 1.12 | +0.6 | 47 | 7 | +10.6 | −8.6 | 21 | 1.15 · +0.9 · 15 | 1.16 · +0.7 |
| Ambil untung | jual semua selepas naik 50 % | 1.14 | +0.7 | 47 | 7 | +11.1 | −8.6 | 21 | 1.18 · +1.0 · 15 | 1.17 · +0.7 |
| Ambil untung | jual semua bila RSI14 melebihi 80 | 1.13 | +0.6 | 47 | 7 | +10.7 | −8.6 | 21 | 1.17 · +0.9 · 15 | 1.16 · +0.6 |
| Ambil untung | jual semua bila tutup lebih 4×ATR di atas purata 20 hari | 1.12 | +0.6 | 47 | 7 | +10.5 | −8.6 | 21 | 1.17 · +1.0 · 15 | 1.16 · +0.6 |
| Ambil untung | jual semua pada +20 %, kecuali jika dicapai dalam 3 minggu (maka pegang 8 minggu) | 1.16 | +0.8 | 46 | 8 | +11.5 | −8.6 | 21 | 1.20 · +1.2 · 16 | 1.18 · +0.7 |
| Naikkan stop loss ke harga beli | tiada **(sekarang)** | 1.16 | +0.8 | 47 | 7 | +11.2 | −8.6 | 21 | 1.19 · +1.1 · 15 | 1.17 · +0.7 |
| Naikkan stop loss ke harga beli | selepas naik 2×ATR | 1.15 | +0.7 | 41 | 7 | +12.0 | −7.2 | 21 | 1.19 · +1.0 · 14 | 1.16 · +0.6 |
| Naikkan stop loss ke harga beli | selepas naik 10 % | 1.14 | +0.7 | 43 | 7 | +11.4 | −7.9 | 21 | 1.18 · +0.9 · 14 | 1.16 · +0.6 |
| Pasaran | tiada **(sekarang)** | 1.16 | +0.8 | 47 | 7 | +11.2 | −8.6 | 21 | 1.19 · +1.1 · 15 | 1.17 · +0.7 |
| Pasaran | jual bila QQQ OFF | 0.98 | -0.1 | 46 | 4 | +7.5 | −6.6 | 9 | 1.03 · +0.1 · 6 | 0.96 · -0.1 |
| Pasaran | jual bila SPY di bawah purata 200 hari | 1.07 | +0.3 | 46 | 6 | +9.7 | −7.7 | 21 | 1.09 · +0.4 · 10 | 1.04 · +0.1 |
| Laporan kewangan berikutnya | tiada **(sekarang)** | 1.16 | +0.8 | 47 | 7 | +11.2 | −8.6 | 21 | 1.19 · +1.1 · 15 | 1.17 · +0.7 |
| Laporan kewangan berikutnya | jual sebelum laporan kewangan berikutnya | 1.15 | +0.7 | 47 | 7 | +10.9 | −8.6 | 21 | 1.18 · +1.0 · 15 | 1.16 · +0.6 |
| Had masa | jual hari ke-20 | 1.12 | +0.5 | 50 | 7 | +9.6 | −8.8 | 20 | 1.14 · +0.7 · 14 | 1.11 · +0.4 |
| Had masa | had 3 bulan | 1.16 | +0.8 | 47 | 7 | +11.2 | −8.6 | 21 | 1.19 · +1.1 · 15 | 1.17 · +0.7 |
| Had masa | had 6 bulan **(sekarang)** | 1.16 | +0.8 | 47 | 7 | +11.2 | −8.6 | 21 | 1.19 · +1.1 · 15 | 1.17 · +0.7 |
| Had masa | had 12 bulan | 1.16 | +0.8 | 47 | 7 | +11.2 | −8.6 | 21 | 1.19 · +1.1 · 15 | 1.17 · +0.7 |

## 4. Kesan setiap pilihan merentas 8,000 cara rawak (nilai tengah bagi semua cara yang mengandungi pilihan itu)

Jadual §3 menukar satu perkara daripada cara sekarang; jadual ini menunjukkan sama ada pilihan itu baik secara umum, apa pun sembilan komponen lain.

| Komponen | Pilihan | Bilangan cara | Untung : rugi | Purata % | Menang % | Rugi ≥ 15 % | Bahagian cara yang mencapai ≥ 2 | Saham rawak: untung : rugi |
|---|---|---|---|---|---|---|---|---|
| Stop loss awal | stop loss 2×ATR | 634 | 1.01 | +0.0 | 37 | 2 | 0 % | 0.99 |
| Stop loss awal | stop loss 3×ATR | 609 | 1.02 | +0.1 | 40 | 3 | 0 % | 0.99 |
| Stop loss awal | stop loss 4×ATR | 572 | 1.03 | +0.1 | 42 | 4 | 0 % | 1.00 |
| Stop loss awal | stop loss 6×ATR | 628 | 1.04 | +0.1 | 41 | 5 | 0 % | 1.01 |
| Stop loss awal | stop loss 5 % | 604 | 0.99 | -0.0 | 35 | 1 | 0 % | 0.96 |
| Stop loss awal | stop loss 8 % | 647 | 1.01 | +0.0 | 39 | 1 | 0 % | 0.98 |
| Stop loss awal | stop loss 10 % | 593 | 1.02 | +0.1 | 40 | 1 | 0 % | 0.99 |
| Stop loss awal | stop loss 15 % | 605 | 1.03 | +0.1 | 41 | 9 | 0 % | 1.01 |
| Stop loss awal | stop loss 3×ATR ikut harga tutup | 618 | 1.03 | +0.1 | 41 | 4 | 0 % | 1.01 |
| Stop loss awal | stop loss 4×ATR ikut harga tutup | 627 | 1.04 | +0.1 | 42 | 5 | 0 % | 1.02 |
| Stop loss awal | stop loss di bawah harga terendah hari isyarat | 584 | 0.95 | -0.1 | 27 | 1 | 0 % | 0.88 |
| Stop loss awal | stop loss di bawah harga terendah 10 hari sebelum beli | 626 | 0.99 | -0.0 | 35 | 2 | 0 % | 0.95 |
| Stop loss awal | stop loss di bawah harga terendah 20 hari sebelum beli | 653 | 1.00 | +0.0 | 38 | 3 | 0 % | 0.97 |
| Potong belian yang tidak menjadi | tiada | 1,611 | 1.03 | +0.1 | 41 | 3 | 0 % | 1.01 |
| Potong belian yang tidak menjadi | jual jika hari ke-5 masih rugi | 1,661 | 0.99 | -0.0 | 36 | 2 | 0 % | 0.96 |
| Potong belian yang tidak menjadi | jual jika hari ke-10 masih rugi | 1,572 | 1.00 | +0.0 | 38 | 2 | 0 % | 0.97 |
| Potong belian yang tidak menjadi | jual jika hari ke-10 belum naik 1×ATR | 1,595 | 0.99 | -0.0 | 40 | 2 | 0 % | 0.96 |
| Potong belian yang tidak menjadi | jual jika hari ke-20 masih rugi | 1,561 | 1.02 | +0.1 | 39 | 3 | 0 % | 1.00 |
| Tanda trend tamat | tiada tanda trend | 239 | 1.02 | +0.1 | 37 | 3 | 0 % | 1.00 |
| Tanda trend tamat | tutup di bawah purata 10 hari | 221 | 0.99 | -0.0 | 40 | 2 | 0 % | 0.96 |
| Tanda trend tamat | tutup di bawah purata 20 hari | 247 | 0.98 | -0.1 | 40 | 2 | 0 % | 0.95 |
| Tanda trend tamat | tutup di bawah purata 50 hari | 225 | 1.01 | +0.0 | 38 | 2 | 0 % | 0.97 |
| Tanda trend tamat | tutup di bawah purata 100 hari | 210 | 1.01 | +0.0 | 37 | 3 | 0 % | 0.98 |
| Tanda trend tamat | dua tutup berturut-turut di bawah purata 20 hari | 246 | 0.98 | -0.1 | 39 | 2 | 0 % | 0.95 |
| Tanda trend tamat | dua tutup berturut-turut di bawah purata 50 hari | 241 | 1.02 | +0.1 | 38 | 3 | 0 % | 0.99 |
| Tanda trend tamat | tutup di bawah EMA 10 hari | 246 | 0.98 | -0.1 | 40 | 2 | 0 % | 0.95 |
| Tanda trend tamat | tutup di bawah EMA 20 hari | 266 | 0.99 | -0.0 | 39 | 2 | 0 % | 0.96 |
| Tanda trend tamat | tutup lebih 1×ATR di bawah purata 20 hari | 247 | 1.02 | +0.1 | 38 | 3 | 0 % | 1.00 |
| Tanda trend tamat | tutup lebih 1×ATR di bawah purata 50 hari | 222 | 1.03 | +0.1 | 37 | 3 | 0 % | 1.00 |
| Tanda trend tamat | purata 10 hari di bawah purata 20 hari | 223 | 0.99 | -0.0 | 41 | 3 | 0 % | 0.96 |
| Tanda trend tamat | purata 20 hari di bawah purata 50 hari | 257 | 1.00 | +0.0 | 39 | 3 | 0 % | 0.97 |
| Tanda trend tamat | tutup di bawah harga terendah 5 hari | 211 | 0.99 | -0.0 | 39 | 2 | 0 % | 0.96 |
| Tanda trend tamat | tutup di bawah harga terendah 10 hari | 218 | 1.03 | +0.1 | 38 | 3 | 0 % | 1.00 |
| Tanda trend tamat | tutup di bawah harga terendah 20 hari | 241 | 1.02 | +0.1 | 38 | 3 | 0 % | 1.00 |
| Tanda trend tamat | tutup di bawah lembah (swing low) terakhir | 213 | 1.00 | -0.0 | 39 | 2 | 0 % | 0.97 |
| Tanda trend tamat | tiga tutup turun berturut-turut | 235 | 0.99 | -0.0 | 40 | 3 | 0 % | 0.96 |
| Tanda trend tamat | Parabolic SAR bertukar turun | 229 | 0.97 | -0.1 | 40 | 2 | 0 % | 0.95 |
| Tanda trend tamat | Supertrend bertukar turun | 235 | 1.01 | +0.0 | 38 | 3 | 0 % | 0.98 |
| Tanda trend tamat | MACD di bawah garis isyarat | 254 | 0.99 | -0.0 | 40 | 2 | 0 % | 0.96 |
| Tanda trend tamat | RSI14 di bawah 50 | 235 | 0.99 | -0.0 | 38 | 2 | 0 % | 0.96 |
| Tanda trend tamat | +DI di bawah −DI | 246 | 1.00 | -0.0 | 39 | 3 | 0 % | 0.97 |
| Tanda trend tamat | hari turun dengan volum ≥ 1.5× biasa | 238 | 1.01 | +0.0 | 39 | 2 | 0 % | 0.99 |
| Tanda trend tamat | jatuh 2×ATR dari tutup tertinggi | 241 | 1.01 | +0.0 | 39 | 2 | 0 % | 0.98 |
| Tanda trend tamat | jatuh 3×ATR dari tutup tertinggi | 250 | 1.03 | +0.1 | 38 | 2 | 0 % | 1.01 |
| Tanda trend tamat | jatuh 4×ATR dari tutup tertinggi | 236 | 1.03 | +0.1 | 38 | 3 | 0 % | 1.01 |
| Tanda trend tamat | jatuh 6×ATR dari tutup tertinggi | 209 | 1.02 | +0.1 | 38 | 3 | 0 % | 1.00 |
| Tanda trend tamat | jatuh 8×ATR dari tutup tertinggi | 222 | 1.04 | +0.2 | 37 | 3 | 0 % | 1.02 |
| Tanda trend tamat | jatuh 3×ATR dari harga tertinggi (Chandelier asal) | 242 | 1.01 | +0.0 | 38 | 3 | 0 % | 0.99 |
| Tanda trend tamat | jatuh 10 % dari tutup tertinggi | 207 | 1.02 | +0.1 | 37 | 3 | 0 % | 0.99 |
| Tanda trend tamat | jatuh 15 % dari tutup tertinggi | 259 | 1.02 | +0.1 | 38 | 3 | 0 % | 1.01 |
| Tanda trend tamat | jatuh 20 % dari tutup tertinggi | 238 | 1.02 | +0.1 | 38 | 3 | 0 % | 0.99 |
| Tanda trend tamat | jatuh 25 % dari tutup tertinggi | 251 | 1.04 | +0.1 | 38 | 3 | 0 % | 1.01 |
| Bila tanda trend mula dipakai | mulai hari ke-3 | 934 | 0.97 | -0.1 | 39 | 2 | 0 % | 0.92 |
| Bila tanda trend mula dipakai | mulai hari ke-10 | 965 | 1.00 | -0.0 | 39 | 2 | 0 % | 0.96 |
| Bila tanda trend mula dipakai | mulai hari ke-20 | 948 | 1.01 | +0.0 | 39 | 3 | 0 % | 0.98 |
| Bila tanda trend mula dipakai | mulai hari ke-40 | 949 | 1.01 | +0.0 | 38 | 2 | 0 % | 0.99 |
| Bila tanda trend mula dipakai | hanya selepas naik 5 % | 997 | 1.00 | +0.0 | 40 | 3 | 0 % | 0.98 |
| Bila tanda trend mula dipakai | hanya selepas naik 10 % | 941 | 1.01 | +0.0 | 39 | 3 | 0 % | 0.99 |
| Bila tanda trend mula dipakai | hanya selepas naik 20 % | 1,011 | 1.03 | +0.1 | 37 | 3 | 0 % | 1.01 |
| Bila tanda trend mula dipakai | hanya selepas naik 50 % | 1,016 | 1.03 | +0.1 | 37 | 3 | 0 % | 1.01 |
| Ketatkan selepas untung besar | tiada | 2,016 | 1.01 | +0.0 | 39 | 3 | 0 % | 0.98 |
| Ketatkan selepas untung besar | selepas naik 20 %: jual bila tutup di bawah purata 10 hari | 2,015 | 1.00 | +0.0 | 39 | 2 | 0 % | 0.98 |
| Ketatkan selepas untung besar | selepas naik 20 %: jual bila jatuh 2×ATR dari tutup tertinggi | 2,013 | 1.00 | +0.0 | 39 | 2 | 0 % | 0.98 |
| Ketatkan selepas untung besar | selepas naik 50 %: jual bila tutup di bawah purata 10 hari | 1,956 | 1.01 | +0.0 | 38 | 2 | 0 % | 0.98 |
| Ambil untung | tiada | 1,081 | 1.01 | +0.1 | 38 | 2 | 0 % | 0.98 |
| Ambil untung | jual separuh selepas naik 10 % | 996 | 1.00 | -0.0 | 41 | 3 | 0 % | 0.97 |
| Ambil untung | jual separuh selepas naik 20 % | 1,002 | 1.01 | +0.0 | 38 | 2 | 0 % | 0.98 |
| Ambil untung | jual semua selepas naik 20 % | 969 | 1.00 | -0.0 | 39 | 2 | 0 % | 0.98 |
| Ambil untung | jual semua selepas naik 50 % | 1,010 | 1.01 | +0.0 | 38 | 3 | 0 % | 0.98 |
| Ambil untung | jual semua bila RSI14 melebihi 80 | 1,002 | 1.00 | -0.0 | 39 | 2 | 0 % | 0.97 |
| Ambil untung | jual semua bila tutup lebih 4×ATR di atas purata 20 hari | 959 | 0.99 | -0.0 | 39 | 2 | 0 % | 0.97 |
| Ambil untung | jual semua pada +20 %, kecuali jika dicapai dalam 3 minggu (maka pegang 8 minggu) | 981 | 1.03 | +0.1 | 37 | 3 | 0 % | 0.99 |
| Naikkan stop loss ke harga beli | tiada | 2,679 | 1.01 | +0.0 | 40 | 3 | 0 % | 0.99 |
| Naikkan stop loss ke harga beli | selepas naik 2×ATR | 2,638 | 1.00 | +0.0 | 37 | 2 | 0 % | 0.97 |
| Naikkan stop loss ke harga beli | selepas naik 10 % | 2,683 | 1.01 | +0.0 | 39 | 2 | 0 % | 0.98 |
| Pasaran | tiada | 2,683 | 1.07 | +0.3 | 36 | 3 | 0 % | 1.07 |
| Pasaran | jual bila QQQ OFF | 2,691 | 0.95 | -0.1 | 41 | 2 | 0 % | 0.92 |
| Pasaran | jual bila SPY di bawah purata 200 hari | 2,626 | 1.02 | +0.1 | 37 | 2 | 0 % | 1.00 |
| Laporan kewangan berikutnya | tiada | 3,938 | 1.01 | +0.0 | 38 | 3 | 0 % | 0.98 |
| Laporan kewangan berikutnya | jual sebelum laporan kewangan berikutnya | 4,062 | 1.00 | +0.0 | 39 | 3 | 0 % | 0.98 |
| Had masa | jual hari ke-20 | 1,997 | 0.98 | -0.1 | 41 | 2 | 0 % | 0.95 |
| Had masa | had 3 bulan | 2,062 | 1.02 | +0.1 | 38 | 3 | 0 % | 0.99 |
| Had masa | had 6 bulan | 1,982 | 1.02 | +0.1 | 38 | 3 | 0 % | 1.00 |
| Had masa | had 12 bulan | 1,959 | 1.02 | +0.1 | 38 | 2 | 0 % | 1.00 |

## 5. Naik bukit pada saham carian (setiap langkah menukar satu komponen)

| Langkah | Cara | Saham carian: untung : rugi | Tidak dilihat: untung : rugi | Purata % | Menang % | Rugi ≥ 15 % | Saham rawak: untung : rugi |
|---|---|---|---|---|---|---|---|
| 0 | stop loss 15 % · naikkan stop loss ke harga beli selepas naik 2×ATR · jual bila jatuh 20 % dari tutup tertinggi (mulai hari ke-20) · had 12 bulan | 1.61 | 1.55 | +3.0 | 23 | 30 | 1.61 |
| 1 | stop loss 15 % · naikkan stop loss ke harga beli selepas naik 2×ATR · had 12 bulan | 1.78 | 1.72 | +3.9 | 16 | 30 | 1.81 |
| 2 | stop loss 15 % · naikkan stop loss ke harga beli selepas naik 10 % · had 12 bulan | 1.81 | 1.74 | +4.8 | 23 | 37 | 1.82 |

## 6. Dua puluh cara teratas pada saham carian, dan bacaannya pada saham yang carian tidak lihat

| Cara | Saham carian: untung : rugi | Tidak dilihat: untung : rugi | Purata % | Menang % | Rugi ≥ 15 % | Hari | Saham rawak: untung : rugi · purata % |
|---|---|---|---|---|---|---|---|
| stop loss 15 % · naikkan stop loss ke harga beli selepas naik 10 % · had 12 bulan | 1.81 | 1.74 | +4.8 | 23 | 37 | 69 | 1.82 · +5.3 |
| stop loss 6×ATR · naikkan stop loss ke harga beli selepas naik 10 % · had 12 bulan | 1.81 | 1.81 | +5.5 | 22 | 20 | 77 | 1.98 · +6.5 |
| stop loss 6×ATR · naikkan stop loss ke harga beli selepas naik 2×ATR · had 12 bulan | 1.79 | 1.80 | +4.7 | 17 | 17 | 56 | 2.00 · +5.8 |
| stop loss 15 % · naikkan stop loss ke harga beli selepas naik 2×ATR · had 12 bulan | 1.78 | 1.72 | +3.9 | 16 | 30 | 45 | 1.81 · +4.6 |
| stop loss 4×ATR ikut harga tutup · naikkan stop loss ke harga beli selepas naik 10 % · had 12 bulan | 1.78 | 1.75 | +4.8 | 19 | 14 | 58 | 1.89 · +5.8 |
| stop loss 4×ATR ikut harga tutup · naikkan stop loss ke harga beli selepas naik 2×ATR · had 12 bulan | 1.75 | 1.74 | +4.1 | 16 | 13 | 42 | 1.91 · +5.1 |
| stop loss 4×ATR · naikkan stop loss ke harga beli selepas naik 10 % · had 12 bulan | 1.75 | 1.70 | +4.4 | 18 | 11 | 50 | 1.86 · +5.4 |
| stop loss 3×ATR ikut harga tutup · naikkan stop loss ke harga beli selepas naik 10 % · had 12 bulan | 1.74 | 1.69 | +4.1 | 17 | 10 | 41 | 1.82 · +5.0 |
| stop loss 4×ATR · naikkan stop loss ke harga beli selepas naik 2×ATR · had 12 bulan | 1.73 | 1.69 | +3.8 | 15 | 11 | 37 | 1.87 · +4.9 |
| stop loss 15 % · had 12 bulan | 1.73 | 1.71 | +6.9 | 39 | 58 | 152 | 1.81 · +8.0 |
| stop loss 15 % · naikkan stop loss ke harga beli selepas naik 10 % · jual jika hari ke-20 masih rugi · had 12 bulan | 1.73 | 1.66 | +3.7 | 17 | 22 | 21 | 1.76 · +4.1 |
| stop loss 15 % · naikkan stop loss ke harga beli selepas naik 10 % · jual bila jatuh 25 % dari tutup tertinggi (mulai hari ke-3) · had 12 bulan | 1.73 | 1.65 | +4.2 | 26 | 37 | 68 | 1.71 · +4.6 |
| stop loss 3×ATR ikut harga tutup · naikkan stop loss ke harga beli selepas naik 2×ATR · had 12 bulan | 1.73 | 1.67 | +3.6 | 14 | 10 | 32 | 1.82 · +4.5 |
| stop loss 15 % · naikkan stop loss ke harga beli selepas naik 10 % · jual jika hari ke-10 masih rugi · had 12 bulan | 1.72 | 1.66 | +3.3 | 16 | 18 | 13 | 1.73 · +3.7 |
| stop loss 15 % · naikkan stop loss ke harga beli selepas naik 10 % · jual bila jatuh 8×ATR dari tutup tertinggi (mulai hari ke-3) · had 12 bulan | 1.72 | 1.65 | +4.2 | 26 | 33 | 67 | 1.73 · +4.6 |
| stop loss 15 % · naikkan stop loss ke harga beli selepas naik 10 % · jual jika hari ke-5 masih rugi · had 12 bulan | 1.71 | 1.63 | +3.0 | 15 | 16 | 9 | 1.70 · +3.2 |
| stop loss 10 % · naikkan stop loss ke harga beli selepas naik 10 % · had 12 bulan | 1.71 | 1.66 | +3.8 | 18 | 2 | 44 | 1.71 · +4.0 |
| stop loss di bawah harga terendah 20 hari sebelum beli · naikkan stop loss ke harga beli selepas naik 10 % · had 12 bulan | 1.70 | 1.66 | +3.3 | 14 | 6 | 28 | 1.71 · +3.1 |
| stop loss 15 % · naikkan stop loss ke harga beli selepas naik 2×ATR · jual jika hari ke-20 masih rugi · had 12 bulan | 1.70 | 1.64 | +3.1 | 13 | 18 | 21 | 1.74 · +3.6 |
| stop loss 3×ATR · naikkan stop loss ke harga beli selepas naik 10 % · had 12 bulan | 1.70 | 1.64 | +3.6 | 16 | 7 | 34 | 1.79 · +4.6 |

Semua cara yang dinilai: `cara.csv.gz`. Setiap setup: `setup.csv.gz`.

## 7. Kaveat

- 8,280 cara dinilai daripada 40,734,720; "terbaik" di sini bermaksud terbaik antara yang dinilai.
- Tiada saham mati dalam data: untung : rugi condong ke atas, lebih-lebih lagi bagi cara yang memegang lama.
- Ribuan cara dicuba; yang terbaik pada saham carian condong ke atas. Sebab itu bacaan dibuat pada saham yang carian tidak lihat.
- Saham yang carian tidak lihat sudah dipakai berkali-kali; 2025–26 pendek.
- Jualan stop loss dianggap tepat pada parasnya; tanda "laporan kewangan" memakai tarikh laporan sebenar.
- Tiada perubahan pada registry F, senarai utama, Top 100 atau dashboard: menukar cara berdaftar ialah keputusan pengguna.
- Pangkat backtest, BUKAN bukti.
