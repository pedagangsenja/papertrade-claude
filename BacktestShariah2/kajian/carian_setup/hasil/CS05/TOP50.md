# CS05: 50 peraturan masuk teratas setiap kayu ukur, TANPA had kepelbagaian papan (backtest, BUKAN bukti)

> **Status keputusan (kad skor, harga 2026-11-12):** TERBUKTI 0 · CALON 0 · BELUM CUKUP 223 · GAGAL 0 · NEGATIF 0. Rejim QQQ OFF sejak 2026-10-16. Hanya **TERBUKTI** layak untuk wang sebenar (`laporan/KAD_SKOR.md`); nombor dalam laporan ini BUKAN keputusan dan tidak boleh dibaca sebagai pangkat untuk wang sebenar.

Dijana `kajian/carian_setup/cs_cs05.py` daripada 200 teratas (`senarai_kunci.csv`). **Jangan sunting secara manual.** Pangkat ditentukan pada kumpulan A; angka daripada kumpulan B. Papan 10 teratas menghadkan setiap prasyarat kepada 3 baris; senarai ini tidak, jadi ia menunjukkan pangkat sebenar.

## Kayu ukur PILIH (lawan saham rawak HARI SAMA)

| # | Prasyarat | Pencetus | Penapis saham | Belian (hari isyarat) | Lari % (rawak) | Kena henti % | Kelebihan lari K1 / K2 / K3 |
|---|---|---|---|---|---|---|---|
| 1 | rejim ON baharu (<= 10 sesi) + earnings dalam 1-5 sesi akan datang | M73 ADX(5) > 40 + Julat Terkecil 6 Hari (ditala 2) | tutup > MA50 + >= 30% di bawah puncak 52 minggu | 501 (242) | 21.2 (10.6) | 42.5 | +12.3 / +8.2 / +12.0 |
| 2 | rejim ON baharu (<= 10 sesi) + earnings dalam 1-5 sesi akan datang | M14 Walking with the Whales (ditala 2) | Supertrend naik + >= 30% di bawah puncak 52 minggu | 597 (262) | 21.6 (10.8) | 42.4 | +10.7 / +10.1 / +12.5 |
| 3 | QQQ dalam 3% dari puncak 52 minggu + earnings dalam 1-5 sesi akan datang | N119 3 tutup turun berturut | ADX < 20 + ATR% >= 4 | 925 (383) | 17.7 (10.2) | 55.0 | +10.5 / +8.2 / +3.0 |
| 4 | QQQ naik >= 3% dalam 5 sesi + earnings dalam 1-5 sesi akan datang | M89 Chande 65sma-3cc (ditala 1) | RS >= 70 | 283 (148) | 15.9 (6.9) | 38.9 | +12.2 / +8.2 / -0.8 |
| 5 | SPY Peringkat 2 Weinstein (atas SMA150 yang naik) + earnings dalam 1-5 sesi akan datang | P09 tutup silang atas MA20 | MA50 naik (lawan 20 bar lalu) + >= 30% di bawah puncak 52 minggu | 470 (301) | 15.7 (10.1) | 50.0 | +9.7 / +3.5 / +6.5 |
| 6 | >= 60% saham di atas MA50 + earnings dalam 1-5 sesi akan datang | M14 Walking with the Whales (ditala 2) | MACD > 0 + >= 30% di bawah puncak 52 minggu | 1,575 (633) | 17.3 (8.1) | 48.8 | +12.0 / +6.3 / +11.7 |
| 7 | >= 60% saham di atas MA50 + earnings dalam 1-5 sesi akan datang | M14 Walking with the Whales (ditala 2) | tutup > MA50 + >= 30% di bawah puncak 52 minggu | 1,579 (631) | 17.2 (8.0) | 48.8 | +12.0 / +6.4 / +11.1 |
| 8 | SPY Peringkat 2 Weinstein (atas SMA150 yang naik) + earnings dalam 1-5 sesi akan datang | M20 EMA10/15 Crossover + Sudut | >= 30% di bawah puncak 52 minggu + hari naik (tutup > buka) | 550 (327) | 17.5 (10.3) | 47.3 | +6.5 / +7.1 / +8.1 |
| 9 | >= 15% saham dalam 5% dari puncak 52 minggu + earnings dalam 1-5 sesi akan datang | M14 Walking with the Whales (ditala 1) | RS >= 90 + dalam 15% dari puncak 52 minggu | 2,162 (1,095) | 14.9 (6.1) | 47.2 | +9.3 / +7.5 / +9.1 |
| 10 | SPY atas SMA200 + earnings dalam 1-5 sesi akan datang | M20 EMA10/15 Crossover + Sudut | >= 30% di bawah puncak 52 minggu + hari naik (tutup > buka) | 577 (350) | 18.0 (10.4) | 46.6 | +6.9 / +7.3 / +9.5 |
| 11 | SPY atas SMA200 + earnings dalam 1-5 sesi akan datang | N29 PSAR naik + tutup>MA50 | >= 30% di bawah puncak 52 minggu | 981 (589) | 17.7 (8.9) | 47.9 | +9.4 / +9.7 / +5.2 |
| 12 | SPY atas SMA200 + earnings dalam 1-5 sesi akan datang | N29 PSAR naik + tutup>MA50 | tutup > MA50 + >= 30% di bawah puncak 52 minggu | 981 (589) | 17.7 (8.9) | 47.9 | +9.4 / +9.7 / +5.2 |
| 13 | >= 15% saham dalam 5% dari puncak 52 minggu + earnings dalam 1-5 sesi akan datang | M20 EMA10/15 Crossover + Sudut | >= 30% di bawah puncak 52 minggu + hari naik (tutup > buka) | 518 (314) | 16.2 (9.3) | 47.3 | +6.0 / +6.8 / +8.7 |
| 14 | >= 15% saham dalam 5% dari puncak 52 minggu + earnings dalam 1-5 sesi akan datang | M14 Walking with the Whales (ditala 1) | MA50 naik (lawan 20 bar lalu) + RS >= 90 | 2,340 (1,139) | 14.9 (6.3) | 48.8 | +9.2 / +7.9 / +7.6 |
| 15 | SPY atas SMA200 + earnings dalam 1-5 sesi akan datang | N29 PSAR naik + tutup>MA50 | >= 30% di bawah puncak 52 minggu + hari naik (tutup > buka) | 877 (542) | 17.4 (9.0) | 47.0 | +8.8 / +9.1 / +6.1 |
| 16 | SPY atas SMA200 + earnings dalam 1-5 sesi akan datang | N29 PSAR naik + tutup>MA50 | RSI14 > 50 + >= 30% di bawah puncak 52 minggu | 954 (574) | 17.6 (8.9) | 47.7 | +9.3 / +9.5 / +5.5 |
| 17 | >= 15% saham dalam 5% dari puncak 52 minggu + earnings dalam 1-5 sesi akan datang | M14 Walking with the Whales (ditala 1) | tutup > MA200 + RS >= 90 | 2,425 (1,166) | 14.8 (6.3) | 49.1 | +9.2 / +7.5 / +7.8 |
| 18 | >= 15% saham dalam 5% dari puncak 52 minggu + earnings dalam 1-5 sesi akan datang | M14 Walking with the Whales (ditala 1) | RS >= 90 | 2,427 (1,166) | 14.8 (6.3) | 49.2 | +9.2 / +7.5 / +7.7 |
| 19 | >= 15% saham dalam 5% dari puncak 52 minggu + earnings dalam 1-5 sesi akan datang | M14 Walking with the Whales (ditala 1) | RS >= 70 + RS >= 90 | 2,427 (1,166) | 14.8 (6.3) | 49.2 | +9.2 / +7.5 / +7.7 |
| 20 | >= 15% saham dalam 5% dari puncak 52 minggu + earnings dalam 1-5 sesi akan datang | M14 Walking with the Whales (ditala 1) | MA50 > MA200 + RS >= 90 | 2,405 (1,162) | 14.9 (6.3) | 48.9 | +9.2 / +7.6 / +7.8 |
| 21 | keluasan naik >= 10 mata dalam 10 sesi + earnings dalam 1-5 sesi akan datang | M161 EMA 10/21 + Supertrend (10,3) | tutup > MA200 + ATR% >= 4 | 401 (210) | 20.2 (10.1) | 50.1 | +10.8 / +8.1 / +22.0 |
| 22 | QQQ dalam 3% dari puncak 52 minggu + earnings dalam 1-5 sesi akan datang | M14 Walking with the Whales (ditala 2) | tutup > MA50 + >= 30% di bawah puncak 52 minggu | 1,086 (548) | 17.8 (7.9) | 48.8 | +11.3 / +7.7 / +10.2 |
| 23 | rejim ON baharu (<= 10 sesi) + earnings dalam 1-5 sesi akan datang | M14 Walking with the Whales | Supertrend naik + >= 30% di bawah puncak 52 minggu | 517 (243) | 19.5 (9.9) | 44.5 | +11.1 / +6.4 / +13.6 |
| 24 | SPY atas SMA200 + earnings dalam 1-5 sesi akan datang | N29 PSAR naik + tutup>MA50 | MACD > isyarat + >= 30% di bawah puncak 52 minggu | 750 (482) | 17.9 (8.7) | 47.5 | +11.6 / +8.8 / +4.5 |
| 25 | QQQ ON + earnings dalam 1-5 sesi akan datang | M14 Walking with the Whales (ditala 2) | MACD > 0 + >= 30% di bawah puncak 52 minggu | 1,761 (725) | 17.5 (8.9) | 48.6 | +10.3 / +7.1 / +9.5 |
| 26 | >= 15% saham dalam 5% dari puncak 52 minggu + earnings dalam 1-5 sesi akan datang | M14 Walking with the Whales (ditala 1) | MA20 > MA50 + RS >= 90 | 2,246 (1,107) | 14.7 (6.2) | 48.8 | +9.2 / +7.3 / +7.6 |
| 27 | >= 60% saham di atas MA200 + earnings dalam 1-5 sesi akan datang | M14 Walking with the Whales (ditala 1) | RS >= 90 + dalam 15% dari puncak 52 minggu | 1,931 (980) | 15.2 (6.2) | 47.3 | +9.4 / +7.8 / +10.0 |
| 28 | QQQ dalam 3% dari puncak 52 minggu + earnings dalam 1-5 sesi akan datang | M14 Walking with the Whales (ditala 1) | RSI14 > 50 + >= 30% di bawah puncak 52 minggu | 1,062 (547) | 17.1 (7.8) | 48.8 | +10.2 / +8.0 / +9.6 |
| 29 | QQQ ON + earnings dalam 1-5 sesi akan datang | M14 Walking with the Whales (ditala 2) | tutup > MA50 + >= 30% di bawah puncak 52 minggu | 1,753 (729) | 17.3 (8.8) | 48.3 | +10.4 / +6.9 / +9.0 |
| 30 | >= 60% saham di atas MA50 + earnings dalam 1-5 sesi akan datang | N16 RSI2<10 tanpa penapis | Supertrend naik + >= 30% di bawah puncak 52 minggu | 379 (240) | 19.8 (7.6) | 47.5 | +12.6 / +11.3 / +13.9 |
| 31 | >= 15% saham dalam 5% dari puncak 52 minggu + earnings dalam 1-5 sesi akan datang | N29 PSAR naik + tutup>MA50 | tutup > MA20 + >= 30% di bawah puncak 52 minggu | 823 (501) | 16.5 (8.0) | 48.2 | +9.6 / +8.7 / +5.4 |
| 32 | rejim ON baharu (<= 10 sesi) + earnings dalam 1-5 sesi akan datang | M50 Elder Triple Screen | MACD > isyarat + >= 30% di bawah puncak 52 minggu | 312 (144) | 19.6 (9.9) | 44.2 | +11.2 / +5.3 / +15.9 |
| 33 | SPY atas SMA200 + earnings dalam 1-5 sesi akan datang | M14 Walking with the Whales (ditala 1) | RSI14 > 50 + >= 30% di bawah puncak 52 minggu | 1,617 (811) | 17.2 (8.1) | 50.0 | +10.6 / +7.1 / +10.3 |
| 34 | QQQ ON + earnings dalam 1-5 sesi akan datang | M77 Undercut & Rally pada Purata Bergerak (MAU&R) | templat trend Minervini + dalam 15% dari puncak 52 minggu | 412 (291) | 10.7 (5.0) | 34.5 | +7.1 / +3.7 / +4.7 |
| 35 | SPY atas SMA200 + earnings dalam 1-5 sesi akan datang | P09 tutup silang atas MA20 | MA50 naik (lawan 20 bar lalu) + >= 30% di bawah puncak 52 minggu | 493 (321) | 15.8 (10.1) | 50.1 | +9.5 / +3.3 / +7.1 |
| 36 | >= 15% saham dalam 5% dari puncak 52 minggu + earnings dalam 1-5 sesi akan datang | M20 EMA10/15 Crossover + Sudut | >= 30% di bawah puncak 52 minggu | 538 (326) | 16.9 (9.3) | 47.0 | +7.9 / +7.3 / +8.2 |
| 37 | QQQ dalam 3% dari puncak 52 minggu + earnings dalam 1-5 sesi akan datang | M14 Walking with the Whales (ditala 2) | >= 30% di bawah puncak 52 minggu | 1,335 (630) | 18.6 (8.1) | 48.9 | +12.5 / +9.4 / +8.5 |
| 38 | SPY Peringkat 2 Weinstein (atas SMA150 yang naik) + earnings dalam 1-5 sesi akan datang | M14 Walking with the Whales (ditala 1) | MA50 > MA200 + RS >= 90 | 2,483 (1,200) | 15.8 (6.9) | 49.1 | +9.6 / +8.6 / +6.8 |
| 39 | >= 15% saham dalam 5% dari puncak 52 minggu + earnings dalam 1-5 sesi akan datang | M14 Walking with the Whales (ditala 1) | RSI14 > 50 + >= 30% di bawah puncak 52 minggu | 1,460 (731) | 17.0 (7.5) | 49.5 | +10.4 / +7.3 / +11.3 |
| 40 | >= 15% saham dalam 5% dari puncak 52 minggu + earnings dalam 1-5 sesi akan datang | M14 Walking with the Whales (ditala 1) | MACD > 0 + RS >= 90 | 2,328 (1,136) | 14.8 (6.2) | 49.3 | +9.2 / +7.7 / +7.3 |
| 41 | SPY Peringkat 2 Weinstein (atas SMA150 yang naik) + earnings dalam 1-5 sesi akan datang | M14 Walking with the Whales (ditala 1) | RS >= 90 + dalam 15% dari puncak 52 minggu | 2,217 (1,130) | 15.8 (6.6) | 47.5 | +9.7 / +9.0 / +7.5 |
| 42 | >= 15% saham dalam 5% dari puncak 52 minggu + earnings dalam 1-5 sesi akan datang | N29 PSAR naik + tutup>MA50 | MACD > isyarat + >= 30% di bawah puncak 52 minggu | 686 (445) | 16.8 (7.9) | 47.8 | +10.8 / +7.9 / +5.5 |
| 43 | SPY Peringkat 2 Weinstein (atas SMA150 yang naik) + earnings dalam 1-5 sesi akan datang | M14 Walking with the Whales (ditala 1) | tutup > MA200 + RS >= 90 | 2,498 (1,204) | 15.7 (6.9) | 49.3 | +9.5 / +8.5 / +7.0 |
| 44 | QQQ dalam 3% dari puncak 52 minggu + earnings dalam 1-5 sesi akan datang | N08 tutup>EMA20 tidak terlalu jauh | RSI14 > 50 + >= 30% di bawah puncak 52 minggu | 1,191 (583) | 16.0 (8.4) | 48.1 | +9.8 / +4.5 / +9.2 |
| 45 | >= 15% saham dalam 5% dari puncak 52 minggu + earnings dalam 1-5 sesi akan datang | M20 EMA10/15 Crossover + Sudut | MA50 naik (lawan 20 bar lalu) + >= 30% di bawah puncak 52 minggu | 438 (276) | 17.1 (9.4) | 45.2 | +8.4 / +7.7 / +6.5 |
| 46 | QQQ dalam 3% dari puncak 52 minggu + earnings dalam 1-5 sesi akan datang | M14 Walking with the Whales (ditala 2) | MACD > 0 + >= 30% di bawah puncak 52 minggu | 1,059 (539) | 18.7 (8.0) | 48.9 | +12.7 / +8.5 / +10.3 |
| 47 | SPY atas SMA200 + earnings dalam 1-5 sesi akan datang | M14 Walking with the Whales (ditala 1) | >= 30% di bawah puncak 52 minggu | 1,914 (911) | 17.6 (8.4) | 50.4 | +10.4 / +7.6 / +10.3 |
| 48 | SPY atas SMA200 + earnings dalam 1-5 sesi akan datang | M20 EMA10/15 Crossover + Sudut | MA50 naik (lawan 20 bar lalu) + >= 30% di bawah puncak 52 minggu | 484 (307) | 18.6 (10.4) | 44.8 | +9.3 / +7.9 / +7.3 |
| 49 | >= 15% saham dalam 5% dari puncak 52 minggu + earnings dalam 1-5 sesi akan datang | N29 PSAR naik + tutup>MA50 | >= 30% di bawah puncak 52 minggu | 887 (538) | 16.5 (8.0) | 48.8 | +9.1 / +8.8 / +5.8 |
| 50 | >= 15% saham dalam 5% dari puncak 52 minggu + earnings dalam 1-5 sesi akan datang | N29 PSAR naik + tutup>MA50 | tutup > MA50 + >= 30% di bawah puncak 52 minggu | 887 (538) | 16.5 (8.0) | 48.8 | +9.1 / +8.8 / +5.8 |

Pencetus berbeza: 12; memakai "earnings dalam 1-5 sesi akan datang": 50 daripada 50.

## Kayu ukur JUMLAH (lawan saham rawak sepanjang ERA)

| # | Prasyarat | Pencetus | Penapis saham | Belian (hari isyarat) | Lari % (rawak) | Kena henti % | Kelebihan lari K1 / K2 / K3 |
|---|---|---|---|---|---|---|---|
| 1 | QQQ >= 10% di bawah puncak + earnings dalam 1-5 sesi akan datang | N119 3 tutup turun berturut | MACD > isyarat + ATR% >= 4 | 1,068 (201) | 26.2 (9.1) | 45.5 | +18.7 / +16.2 / +21.0 |
| 2 | Januari + tiada earnings dalam 20 sesi akan datang | M105 Supertrend tulen (ditala 2) | MACD > isyarat + >= 30% di bawah puncak 52 minggu | 514 (141) | 23.0 (8.4) | 31.7 | +20.1 / +14.8 / -0.0 |
| 3 | SPY bawah SMA200 + earnings dalam 1-5 sesi akan datang | N119 3 tutup turun berturut | MACD > isyarat + ATR% >= 4 | 1,168 (224) | 24.2 (8.6) | 46.9 | +10.6 / +16.4 / +19.3 |
| 4 | Januari + tiada earnings dalam 20 sesi akan datang | M105 Supertrend tulen (ditala 1) | MACD > isyarat + >= 30% di bawah puncak 52 minggu | 506 (138) | 21.9 (8.5) | 31.6 | +16.8 / +15.2 / +0.6 |
| 5 | hari 90% turun kemudian naik (20 sesi) + earnings dalam 1-5 sesi akan datang | N119 3 tutup turun berturut | >= 30% di bawah puncak 52 minggu + ATR% >= 4 | 1,239 (327) | 27.4 (9.0) | 46.7 | +16.8 / +19.3 / +18.1 |
| 6 | SPY bawah SMA200 + earnings dalam 1-5 sesi akan datang | M73 ADX(5) > 40 + Julat Terkecil 6 Hari (ditala 2) | RSI14 < 40 + >= 30% di bawah puncak 52 minggu | 704 (256) | 25.0 (8.4) | 46.3 | +21.2 / +14.3 / +15.2 |
| 7 | QQQ >= 20% di bawah puncak | M73 ADX(5) > 40 + Julat Terkecil 6 Hari (ditala 1) | RSI14 < 40 + >= 30% di bawah puncak 52 minggu | 1,314 (144) | 30.0 (8.3) | 39.8 | +55.9 / +18.0 / +31.3 |
| 8 | SPY bawah SMA200 + earnings dalam 1-5 sesi akan datang | N16 RSI2<10 tanpa penapis | MACD > isyarat | 731 (183) | 21.1 (6.7) | 34.7 | +9.9 / +16.6 / +16.0 |
| 9 | turun-naik SPY 21 hari >= 25% setahun + sektor 3 terbawah (pulangan 63 sesi) | N16 RSI2<10 tanpa penapis | RSI14 < 40 + ADX < 20 | 580 (139) | 22.4 (7.2) | 32.2 | +15.5 / +11.1 / +25.1 |
| 10 | QQQ >= 10% di bawah puncak + earnings dalam 1-5 sesi akan datang | N119 3 tutup turun berturut | ATR% >= 4 | 1,918 (287) | 26.1 (9.2) | 45.2 | +22.8 / +14.5 / +24.1 |
| 11 | QQQ >= 20% di bawah puncak | M73 ADX(5) > 40 + Julat Terkecil 6 Hari (ditala 1) | ADX > 25 + >= 30% di bawah puncak 52 minggu | 1,411 (176) | 27.7 (8.4) | 41.7 | +55.2 / +16.0 / +31.3 |
| 12 | Januari + tiada earnings dalam 20 sesi akan datang | M105 Supertrend tulen (ditala 2) | tutup > MA20 + >= 30% di bawah puncak 52 minggu | 550 (154) | 20.7 (8.8) | 34.7 | +15.8 / +14.4 / -1.2 |
| 13 | QQQ >= 20% di bawah puncak | M73 ADX(5) > 40 + Julat Terkecil 6 Hari | RSI14 < 40 + ATR% >= 4 | 2,021 (178) | 27.7 (9.1) | 39.7 | +54.7 / +15.7 / -10.3 |
| 14 | QQQ >= 10% di bawah puncak + earnings dalam 1-5 sesi akan datang | N16 RSI2<10 tanpa penapis | MACD > isyarat | 665 (164) | 23.2 (6.9) | 32.9 | +11.1 / +17.6 / +16.0 |
| 15 | SPY bawah SMA200 + earnings dalam 1-5 sesi akan datang | N119 3 tutup turun berturut | MACD > isyarat + >= 30% di bawah puncak 52 minggu | 1,050 (222) | 25.2 (8.4) | 44.4 | +19.2 / +17.2 / +11.5 |
| 16 | SPY bawah SMA200 + earnings dalam 1-5 sesi akan datang | M155 Market Cycle Strategy | RSI14 < 40 + volum 10 hari > volum 50 hari | 320 (145) | 26.9 (6.5) | 37.5 | +16.2 / +24.9 / +23.3 |
| 17 | QQQ OFF + earnings dalam 1-5 sesi akan datang | N16 RSI2<10 tanpa penapis | MACD > isyarat + >= 30% di bawah puncak 52 minggu | 431 (194) | 23.0 (8.6) | 46.4 | +22.3 / +12.4 / +6.5 |
| 18 | hari 90% turun kemudian naik (20 sesi) + earnings dalam 1-5 sesi akan datang | N119 3 tutup turun berturut | ATR% >= 4 | 2,047 (457) | 25.3 (8.4) | 46.8 | +13.5 / +18.2 / +22.1 |
| 19 | SPY bawah SMA200 + earnings dalam 1-5 sesi akan datang | M01 Bollinger Band + RSI (ditala 2) | MACD > isyarat | 293 (117) | 20.5 (6.6) | 42.3 | +13.3 / +12.9 / +26.5 |
| 20 | SPY bawah SMA200 + earnings dalam 1-5 sesi akan datang | M01 Bollinger Band + RSI (ditala 2) | RSI14 < 40 + MACD > isyarat | 293 (117) | 20.5 (6.6) | 42.3 | +13.3 / +12.9 / +26.5 |
| 21 | turun-naik SPY 21 hari >= 25% setahun | M73 ADX(5) > 40 + Julat Terkecil 6 Hari | RSI14 < 40 + >= 30% di bawah puncak 52 minggu | 2,471 (275) | 21.4 (8.2) | 39.6 | +14.8 / +13.9 / +3.9 |
| 22 | QQQ >= 20% di bawah puncak + tiada earnings dalam 20 sesi akan datang | M73 ADX(5) > 40 + Julat Terkecil 6 Hari | RSI14 < 40 + ATR% >= 4 | 1,478 (164) | 27.3 (9.1) | 38.4 | +58.8 / +14.7 / -10.3 |
| 23 | QQQ >= 20% di bawah puncak | M73 ADX(5) > 40 + Julat Terkecil 6 Hari (ditala 1) | >= 30% di bawah puncak 52 minggu | 1,508 (179) | 26.9 (8.4) | 40.9 | +55.9 / +15.0 / +31.3 |
| 24 | SPY bawah SMA200 + earnings dalam 1-5 sesi akan datang | N119 3 tutup turun berturut | ATR% >= 4 | 1,899 (307) | 23.7 (8.7) | 47.7 | +14.4 / +14.0 / +22.0 |
| 25 | Januari + tiada earnings dalam 20 sesi akan datang | M105 Supertrend tulen (ditala 1) | >= 30% di bawah puncak 52 minggu | 569 (149) | 21.3 (8.6) | 33.0 | +16.3 / +15.0 / -1.1 |
| 26 | breadth thrust Zweig aktif (20 sesi) + earnings dalam 1-5 sesi akan datang | N119 3 tutup turun berturut | >= 30% di bawah puncak 52 minggu | 528 (162) | 25.2 (8.0) | 37.7 | +13.6 / +28.8 / +11.2 |
| 27 | QQQ OFF + earnings dalam 1-5 sesi akan datang | N16 RSI2<10 tanpa penapis | >= 30% di bawah puncak 52 minggu + volum hari isyarat >= 1.5x purata 50 | 474 (270) | 21.9 (8.7) | 45.8 | +20.5 / +10.8 / +4.5 |
| 28 | Januari + tiada earnings dalam 20 sesi akan datang | M105 Supertrend tulen (ditala 1) | >= 30% di bawah puncak 52 minggu + hari naik (tutup > buka) | 543 (149) | 21.4 (8.6) | 33.3 | +15.8 / +15.3 / -0.3 |
| 29 | Januari + tiada earnings dalam 20 sesi akan datang | M105 Supertrend tulen (ditala 2) | >= 30% di bawah puncak 52 minggu | 672 (164) | 21.6 (8.6) | 34.2 | +18.3 / +13.6 / -0.7 |
| 30 | QQQ >= 10% di bawah puncak + earnings dalam 1-5 sesi akan datang | N119 3 tutup turun berturut | MACD > isyarat + >= 30% di bawah puncak 52 minggu | 1,040 (204) | 25.6 (8.6) | 44.0 | +25.9 / +16.3 / +12.6 |
| 31 | turun-naik SPY 21 hari >= 25% setahun + kejutan untung terkini positif (SUE > 0) | M73 ADX(5) > 40 + Julat Terkecil 6 Hari | ADX > 25 + >= 30% di bawah puncak 52 minggu | 956 (195) | 25.4 (8.0) | 38.0 | +22.6 / +17.5 / +6.3 |
| 32 | rejim ON baharu (<= 10 sesi) + earnings dalam 1-5 sesi akan datang | M73 ADX(5) > 40 + Julat Terkecil 6 Hari (ditala 2) | tutup > MA20 + >= 30% di bawah puncak 52 minggu | 743 (297) | 23.0 (8.0) | 40.4 | +13.2 / +15.1 / +17.6 |
| 33 | turun-naik SPY 21 hari >= 25% setahun + kejutan untung terkini positif (SUE > 0) | M73 ADX(5) > 40 + Julat Terkecil 6 Hari | RSI14 < 40 + >= 30% di bawah puncak 52 minggu | 903 (175) | 25.5 (8.1) | 36.9 | +25.3 / +17.0 / +4.2 |
| 34 | distribution day QQQ >= 5 dalam 25 sesi + earnings dalam 1-5 sesi akan datang | N119 3 tutup turun berturut | tutup > MA20 + ATR% >= 4 | 1,460 (571) | 20.9 (9.5) | 52.4 | +9.1 / +12.6 / +10.4 |
| 35 | rejim ON baharu (<= 10 sesi) + earnings dalam 1-5 sesi akan datang | M73 ADX(5) > 40 + Julat Terkecil 6 Hari (ditala 2) | >= 30% di bawah puncak 52 minggu + ATR% >= 4 | 715 (270) | 22.4 (9.7) | 45.9 | +11.6 / +13.5 / +12.3 |
| 36 | QQQ >= 20% di bawah puncak | M73 ADX(5) > 40 + Julat Terkecil 6 Hari | ADX > 25 + >= 30% di bawah puncak 52 minggu | 2,000 (198) | 24.9 (8.4) | 39.9 | +55.3 / +14.2 / -10.3 |
| 37 | SPY bawah SMA200 + earnings dalam 1-5 sesi akan datang | M73 ADX(5) > 40 + Julat Terkecil 6 Hari (ditala 2) | RSI14 < 40 | 1,334 (325) | 21.1 (6.6) | 41.5 | +17.1 / +12.5 / +15.3 |
| 38 | follow-through day aktif (QQQ, 20 sesi) + earnings dalam 1-5 sesi akan datang | N119 3 tutup turun berturut | ADX < 20 + ATR% >= 4 | 879 (220) | 19.8 (9.1) | 52.3 | +10.1 / +11.8 / +7.8 |
| 39 | SPY bawah SMA200 + earnings dalam 1-5 sesi akan datang | M155 Market Cycle Strategy (ditala 1) | RSI14 < 40 + hari naik (tutup > buka) | 318 (136) | 24.8 (6.3) | 38.4 | +12.9 / +23.4 / +30.0 |
| 40 | follow-through day aktif (QQQ, 20 sesi) + earnings dalam 1-5 sesi akan datang | N119 3 tutup turun berturut | MACD > isyarat + ATR% >= 4 | 1,304 (256) | 22.5 (9.1) | 50.2 | +11.5 / +14.4 / +11.9 |
| 41 | SPY bawah SMA200 + earnings dalam 1-5 sesi akan datang | N16 RSI2<10 tanpa penapis | >= 30% di bawah puncak 52 minggu | 945 (257) | 24.7 (8.5) | 46.7 | +20.8 / +14.6 / +15.4 |
| 42 | <= 30% saham di atas MA50 + earnings dalam 1-5 sesi akan datang | M155 Market Cycle Strategy (ditala 1) | RSI14 < 40 + hari naik (tutup > buka) | 351 (129) | 24.2 (6.1) | 38.5 | +13.7 / +21.0 / +30.5 |
| 43 | SPY bawah SMA200 + earnings dalam 1-5 sesi akan datang | M73 ADX(5) > 40 + Julat Terkecil 6 Hari (ditala 2) | RSI14 < 40 + volum 10 hari > volum 50 hari | 849 (261) | 21.9 (6.4) | 40.5 | +16.5 / +14.4 / +15.7 |
| 44 | SPY bawah SMA200 + earnings dalam 1-5 sesi akan datang | M155 Market Cycle Strategy (ditala 2) | ADX > 25 + volum 10 hari > volum 50 hari | 560 (203) | 21.4 (6.0) | 40.7 | +15.1 / +17.2 / +11.1 |
| 45 | SPY bawah SMA200 + earnings dalam 1-5 sesi akan datang | M73 ADX(5) > 40 + Julat Terkecil 6 Hari (ditala 2) | RSI14 < 40 + hari naik (tutup > buka) | 568 (204) | 20.8 (6.5) | 44.0 | +15.3 / +12.5 / +19.7 |
| 46 | QQQ >= 10% di bawah puncak + earnings dalam 1-5 sesi akan datang | N16 RSI2<10 tanpa penapis | >= 30% di bawah puncak 52 minggu | 968 (241) | 26.8 (8.8) | 45.2 | +29.3 / +15.6 / +18.2 |
| 47 | QQQ >= 20% di bawah puncak | M73 ADX(5) > 40 + Julat Terkecil 6 Hari (ditala 1) | RSI14 < 40 + volum 10 hari > volum 50 hari | 1,452 (156) | 25.6 (7.5) | 37.5 | +44.9 / +15.2 / +40.8 |
| 48 | QQQ naik >= 3% dalam 5 sesi + earnings dalam 1-5 sesi akan datang | M89 Chande 65sma-3cc (ditala 1) | RS >= 70 | 283 (148) | 15.9 (5.5) | 38.9 | +13.0 / +10.5 / +0.9 |
| 49 | SPY bawah SMA200 + earnings dalam 1-5 sesi akan datang | M73 ADX(5) > 40 + Julat Terkecil 6 Hari (ditala 2) | RSI14 < 40 + ADX > 25 | 884 (268) | 23.6 (6.5) | 38.3 | +18.2 / +15.9 / +18.1 |
| 50 | QQQ >= 20% di bawah puncak | M73 ADX(5) > 40 + Julat Terkecil 6 Hari | RSI14 < 40 + >= 30% di bawah puncak 52 minggu | 2,187 (178) | 24.9 (8.5) | 38.9 | +57.4 / +13.5 / -10.3 |

Pencetus berbeza: 7; memakai "earnings dalam 1-5 sesi akan datang": 32 daripada 50.
