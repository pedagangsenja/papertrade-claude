# CS05: 50 peraturan masuk teratas setiap kayu ukur, TANPA had kepelbagaian papan (backtest, BUKAN bukti)

> **Status keputusan (kad skor, harga 2026-11-12):** TERBUKTI 0 · CALON 0 · BELUM CUKUP 223 · GAGAL 0 · NEGATIF 0. Rejim QQQ OFF sejak 2026-10-16. Hanya **TERBUKTI** layak untuk wang sebenar (`laporan/KAD_SKOR.md`); nombor dalam laporan ini BUKAN keputusan dan tidak boleh dibaca sebagai pangkat untuk wang sebenar.

Dijana `kajian/carian_setup/cs_cs05.py` daripada 200 teratas (`senarai_kunci.csv`). **Jangan sunting secara manual.** Pangkat ditentukan pada kumpulan A; angka daripada kumpulan B. Papan 10 teratas menghadkan setiap prasyarat kepada 3 baris; senarai ini tidak, jadi ia menunjukkan pangkat sebenar.

## Kayu ukur PILIH (lawan saham rawak HARI SAMA)

| # | Prasyarat | Pencetus | Penapis saham | Belian (hari isyarat) | Tangkap penuh % (rawak) | Kena henti % | Kelebihan tangkap penuh K1 / K2 / K3 |
|---|---|---|---|---|---|---|---|
| 1 | rejim ON baharu (<= 10 sesi) + earnings dalam 1-5 sesi akan datang | M73 ADX(5) > 40 + Julat Terkecil 6 Hari (ditala 2) | tutup > MA50 + >= 30% di bawah puncak 52 minggu | 501 (242) | 21.2 (10.5) | 42.5 | +11.4 / +9.2 / +12.0 |
| 2 | rejim ON baharu (<= 10 sesi) + earnings dalam 1-5 sesi akan datang | M14 Walking with the Whales (ditala 2) | Supertrend naik + >= 30% di bawah puncak 52 minggu | 597 (262) | 21.9 (10.6) | 42.4 | +11.3 / +10.3 / +13.5 |
| 3 | QQQ dalam 3% dari puncak 52 minggu + earnings dalam 1-5 sesi akan datang | M14 Walking with the Whales (ditala 2) | tutup > MA50 + >= 30% di bawah puncak 52 minggu | 1,086 (548) | 18.2 (7.9) | 48.8 | +11.4 / +8.6 / +10.9 |
| 4 | >= 60% saham di atas MA50 + earnings dalam 1-5 sesi akan datang | N16 RSI2<10 tanpa penapis | Supertrend naik + >= 30% di bawah puncak 52 minggu | 379 (240) | 19.8 (7.6) | 47.5 | +12.7 / +10.5 / +15.8 |
| 5 | QQQ dalam 3% dari puncak 52 minggu + earnings dalam 1-5 sesi akan datang | N119 3 tutup turun berturut | ADX < 20 + ATR% >= 4 | 925 (383) | 17.7 (10.2) | 55.0 | +10.3 / +8.4 / +2.7 |
| 6 | >= 60% saham di atas MA50 + earnings dalam 1-5 sesi akan datang | M14 Walking with the Whales (ditala 2) | MACD > 0 + >= 30% di bawah puncak 52 minggu | 1,575 (633) | 17.5 (8.1) | 48.8 | +11.9 / +6.6 / +12.5 |
| 7 | SPY Peringkat 2 Weinstein (atas SMA150 yang naik) + earnings dalam 1-5 sesi akan datang | M20 EMA10/15 Crossover + Sudut | >= 30% di bawah puncak 52 minggu + hari naik (tutup > buka) | 550 (327) | 18.0 (10.3) | 47.3 | +6.7 / +7.8 / +8.9 |
| 8 | >= 15% saham dalam 5% dari puncak 52 minggu + earnings dalam 1-5 sesi akan datang | N29 PSAR naik + tutup>MA50 | MACD > isyarat + >= 30% di bawah puncak 52 minggu | 686 (445) | 16.5 (7.8) | 47.8 | +10.6 / +7.2 / +6.3 |
| 9 | >= 60% saham di atas MA50 + earnings dalam 1-5 sesi akan datang | M14 Walking with the Whales (ditala 2) | tutup > MA50 + >= 30% di bawah puncak 52 minggu | 1,579 (631) | 17.5 (8.0) | 48.8 | +11.9 / +6.9 / +11.9 |
| 10 | SPY atas SMA200 + earnings dalam 1-5 sesi akan datang | M20 EMA10/15 Crossover + Sudut | >= 30% di bawah puncak 52 minggu + hari naik (tutup > buka) | 577 (350) | 18.4 (10.3) | 46.6 | +7.1 / +7.7 / +10.3 |
| 11 | QQQ dalam 3% dari puncak 52 minggu + earnings dalam 1-5 sesi akan datang | M14 Walking with the Whales (ditala 1) | RSI14 > 50 + >= 30% di bawah puncak 52 minggu | 1,062 (547) | 17.1 (7.8) | 48.8 | +9.9 / +8.3 / +9.9 |
| 12 | rejim ON baharu (<= 10 sesi) + earnings dalam 1-5 sesi akan datang | M73 ADX(5) > 40 + Julat Terkecil 6 Hari (ditala 2) | MACD > 0 + >= 30% di bawah puncak 52 minggu | 493 (236) | 21.3 (10.6) | 43.2 | +10.4 / +9.7 / +12.8 |
| 13 | QQQ dalam 3% dari puncak 52 minggu + earnings dalam 1-5 sesi akan datang | M14 Walking with the Whales (ditala 2) | MA20 > MA50 + >= 30% di bawah puncak 52 minggu | 794 (440) | 17.4 (7.9) | 50.1 | +9.3 / +7.1 / +12.9 |
| 14 | SPY atas SMA200 + earnings dalam 1-5 sesi akan datang | M14 Walking with the Whales (ditala 2) | tutup > MA50 + >= 30% di bawah puncak 52 minggu | 1,693 (830) | 17.9 (8.2) | 49.5 | +11.9 / +7.1 / +11.0 |
| 15 | SPY atas SMA200 + earnings dalam 1-5 sesi akan datang | N29 PSAR naik + tutup>MA50 | >= 30% di bawah puncak 52 minggu | 981 (589) | 17.8 (8.9) | 47.9 | +9.3 / +9.7 / +6.2 |
| 16 | SPY atas SMA200 + earnings dalam 1-5 sesi akan datang | N29 PSAR naik + tutup>MA50 | tutup > MA50 + >= 30% di bawah puncak 52 minggu | 981 (589) | 17.8 (8.9) | 47.9 | +9.3 / +9.7 / +6.2 |
| 17 | SPY atas SMA200 + earnings dalam 1-5 sesi akan datang | N29 PSAR naik + tutup>MA50 | >= 30% di bawah puncak 52 minggu + hari naik (tutup > buka) | 877 (542) | 17.4 (8.9) | 47.0 | +8.6 / +9.1 / +6.7 |
| 18 | >= 15% saham dalam 5% dari puncak 52 minggu + earnings dalam 1-5 sesi akan datang | M20 EMA10/15 Crossover + Sudut | >= 30% di bawah puncak 52 minggu + hari naik (tutup > buka) | 518 (314) | 16.8 (9.2) | 47.3 | +6.2 / +7.6 / +9.5 |
| 19 | QQQ dalam 3% dari puncak 52 minggu + earnings dalam 1-5 sesi akan datang | M14 Walking with the Whales (ditala 2) | MACD > 0 + >= 30% di bawah puncak 52 minggu | 1,059 (539) | 19.2 (7.9) | 48.9 | +12.6 / +9.7 / +11.0 |
| 20 | SPY atas SMA200 + earnings dalam 1-5 sesi akan datang | N29 PSAR naik + tutup>MA50 | RSI14 > 50 + >= 30% di bawah puncak 52 minggu | 954 (574) | 17.7 (8.9) | 47.7 | +9.2 / +9.5 / +6.5 |
| 21 | SPY atas SMA200 + earnings dalam 1-5 sesi akan datang | M14 Walking with the Whales (ditala 1) | RSI14 > 50 + >= 30% di bawah puncak 52 minggu | 1,617 (811) | 17.2 (8.1) | 50.0 | +10.5 / +7.1 / +10.8 |
| 22 | rejim ON baharu (<= 10 sesi) + earnings dalam 1-5 sesi akan datang | M14 Walking with the Whales (ditala 2) | >= 30% di bawah puncak 52 minggu + hari naik (tutup > buka) | 524 (221) | 21.6 (11.6) | 43.7 | +11.1 / +8.2 / +12.2 |
| 23 | SPY Peringkat 2 Weinstein (atas SMA150 yang naik) + earnings dalam 1-5 sesi akan datang | M128 Inventory Retracement Bar (IRB, Rob Hoffman) (ditala 1) | RS >= 90 + tutup dalam 25% teratas julat hari | 468 (356) | 14.7 (6.9) | 50.9 | +8.3 / +7.7 / +6.7 |
| 24 | >= 15% saham dalam 5% dari puncak 52 minggu + earnings dalam 1-5 sesi akan datang | M14 Walking with the Whales (ditala 2) | tutup > MA50 + >= 30% di bawah puncak 52 minggu | 1,516 (744) | 17.9 (7.6) | 49.0 | +11.7 / +7.7 / +11.6 |
| 25 | Mei-Okt + earnings dalam 1-5 sesi akan datang | M14 Walking with the Whales (ditala 1) | Supertrend naik + >= 30% di bawah puncak 52 minggu | 1,045 (461) | 19.8 (10.2) | 47.9 | +11.1 / +7.5 / +12.2 |
| 26 | SPY atas SMA200 + earnings dalam 1-5 sesi akan datang | M20 EMA10/15 Crossover + Sudut | MA50 naik (lawan 20 bar lalu) + >= 30% di bawah puncak 52 minggu | 484 (307) | 18.8 (10.4) | 44.8 | +8.8 / +8.3 / +8.2 |
| 27 | >= 60% saham di atas MA200 + earnings dalam 1-5 sesi akan datang | M14 Walking with the Whales (ditala 2) | tutup > MA50 + >= 30% di bawah puncak 52 minggu | 1,287 (640) | 17.6 (7.5) | 51.1 | +10.9 / +8.1 / +12.8 |
| 28 | SPY Peringkat 2 Weinstein (atas SMA150 yang naik) + earnings dalam 1-5 sesi akan datang | M20 EMA10/15 Crossover + Sudut | MA50 naik (lawan 20 bar lalu) + >= 30% di bawah puncak 52 minggu | 463 (289) | 18.8 (10.4) | 45.1 | +8.6 / +8.7 / +7.3 |
| 29 | keluasan naik >= 10 mata dalam 10 sesi + earnings dalam 1-5 sesi akan datang | M161 EMA 10/21 + Supertrend (10,3) | tutup > MA200 + ATR% >= 4 | 401 (210) | 20.9 (10.3) | 50.1 | +10.1 / +9.6 / +19.4 |
| 30 | SPY atas SMA200 + earnings dalam 1-5 sesi akan datang | M80 Radge Saluran Purata Bergerak (MAC) (ditala 1) | tutup > MA50 + ATR% >= 4 | 559 (370) | 20.8 (9.5) | 54.7 | +19.8 / +5.2 / +14.6 |
| 31 | QQQ dalam 3% dari puncak 52 minggu + earnings dalam 1-5 sesi akan datang | M14 Walking with the Whales (ditala 2) | >= 30% di bawah puncak 52 minggu | 1,335 (630) | 19.1 (8.0) | 48.9 | +12.5 / +10.7 / +9.1 |
| 32 | >= 15% saham dalam 5% dari puncak 52 minggu + earnings dalam 1-5 sesi akan datang | N29 PSAR naik + tutup>MA50 | tutup > MA20 + >= 30% di bawah puncak 52 minggu | 823 (501) | 16.4 (7.9) | 48.2 | +9.5 / +8.5 / +5.9 |
| 33 | QQQ ON + earnings dalam 1-5 sesi akan datang | M14 Walking with the Whales (ditala 2) | MACD > 0 + >= 30% di bawah puncak 52 minggu | 1,761 (725) | 17.9 (9.0) | 48.6 | +10.2 / +7.7 / +10.1 |
| 34 | earnings dalam 1-5 sesi akan datang | M20 EMA10/15 Crossover + Sudut | ADX < 20 + >= 30% di bawah puncak 52 minggu | 461 (300) | 20.2 (10.6) | 46.4 | +7.7 / +9.3 / +13.3 |
| 35 | SPY Peringkat 2 Weinstein (atas SMA150 yang naik) + earnings dalam 1-5 sesi akan datang | M20 EMA10/15 Crossover + Sudut | >= 30% di bawah puncak 52 minggu | 568 (338) | 18.5 (10.2) | 47.0 | +7.7 / +8.4 / +8.5 |
| 36 | SPY atas SMA200 + earnings dalam 1-5 sesi akan datang | M20 EMA10/15 Crossover + Sudut | >= 30% di bawah puncak 52 minggu | 598 (362) | 18.9 (10.3) | 46.5 | +8.3 / +8.2 / +10.0 |
| 37 | QQQ SMA10 > SMA20 + earnings dalam 1-5 sesi akan datang | M14 Walking with the Whales (ditala 2) | MA20 > MA50 + >= 30% di bawah puncak 52 minggu | 1,323 (642) | 17.0 (8.4) | 50.5 | +8.6 / +7.7 / +11.2 |
| 38 | >= 15% saham dalam 5% dari puncak 52 minggu + earnings dalam 1-5 sesi akan datang | M14 Walking with the Whales (ditala 1) | RSI14 > 50 + >= 30% di bawah puncak 52 minggu | 1,460 (731) | 17.0 (7.5) | 49.5 | +10.1 / +7.3 / +12.3 |
| 39 | >= 15% saham dalam 5% dari puncak 52 minggu + earnings dalam 1-5 sesi akan datang | N36 Pocket pivot | >= 30% di bawah puncak 52 minggu + ATR% >= 4 | 685 (408) | 17.5 (9.5) | 56.1 | +7.4 / +8.1 / +9.0 |
| 40 | >= 15% saham dalam 5% dari puncak 52 minggu + earnings dalam 1-5 sesi akan datang | M14 Walking with the Whales (ditala 1) | RS >= 90 + dalam 15% dari puncak 52 minggu | 2,162 (1,095) | 14.9 (6.0) | 47.2 | +8.6 / +8.5 / +11.5 |
| 41 | >= 15% saham dalam 5% dari puncak 52 minggu + earnings dalam 1-5 sesi akan datang | M14 Walking with the Whales (ditala 1) | MA50 naik (lawan 20 bar lalu) + RS >= 90 | 2,340 (1,139) | 15.0 (6.2) | 48.8 | +8.6 / +8.6 / +10.0 |
| 42 | >= 15% saham dalam 5% dari puncak 52 minggu + earnings dalam 1-5 sesi akan datang | N29 PSAR naik + tutup>MA50 | >= 30% di bawah puncak 52 minggu | 887 (538) | 16.5 (8.0) | 48.8 | +9.0 / +8.5 / +7.0 |
| 43 | >= 15% saham dalam 5% dari puncak 52 minggu + earnings dalam 1-5 sesi akan datang | N29 PSAR naik + tutup>MA50 | tutup > MA50 + >= 30% di bawah puncak 52 minggu | 887 (538) | 16.5 (8.0) | 48.8 | +9.0 / +8.5 / +7.0 |
| 44 | QQQ dalam 3% dari puncak 52 minggu + earnings dalam 1-5 sesi akan datang | M128 Inventory Retracement Bar (IRB, Rob Hoffman) (ditala 1) | RS >= 90 + tutup dalam 25% teratas julat hari | 360 (273) | 13.1 (6.5) | 49.2 | +6.3 / +7.1 / +6.2 |
| 45 | QQQ dalam 3% dari puncak 52 minggu + earnings dalam 1-5 sesi akan datang | M14 Walking with the Whales (ditala 2) | Supertrend naik + >= 30% di bawah puncak 52 minggu | 986 (533) | 18.8 (7.6) | 50.0 | +11.5 / +10.7 / +11.2 |
| 46 | QQQ dalam 3% dari puncak 52 minggu + earnings dalam 1-5 sesi akan datang | M14 Walking with the Whales (ditala 2) | RSI14 > 50 + >= 30% di bawah puncak 52 minggu | 1,212 (599) | 18.9 (7.8) | 49.0 | +13.0 / +10.3 / +8.7 |
| 47 | QQQ ON + earnings dalam 1-5 sesi akan datang | M14 Walking with the Whales (ditala 2) | tutup > MA50 + >= 30% di bawah puncak 52 minggu | 1,753 (729) | 17.7 (8.8) | 48.3 | +10.4 / +7.5 / +9.4 |
| 48 | >= 15% saham dalam 5% dari puncak 52 minggu + earnings dalam 1-5 sesi akan datang | M14 Walking with the Whales (ditala 2) | MACD > 0 + >= 30% di bawah puncak 52 minggu | 1,492 (733) | 18.4 (7.6) | 49.2 | +12.4 / +8.2 / +11.9 |
| 49 | >= 15% saham dalam 5% dari puncak 52 minggu + earnings dalam 1-5 sesi akan datang | N29 PSAR naik + tutup>MA50 | >= 30% di bawah puncak 52 minggu + hari naik (tutup > buka) | 799 (498) | 16.0 (8.0) | 47.9 | +8.3 / +8.0 / +7.2 |
| 50 | >= 15% saham dalam 5% dari puncak 52 minggu + earnings dalam 1-5 sesi akan datang | M14 Walking with the Whales (ditala 1) | tutup > MA200 + RS >= 90 | 2,425 (1,166) | 14.8 (6.2) | 49.1 | +8.5 / +8.2 / +10.1 |

Pencetus berbeza: 10; memakai "earnings dalam 1-5 sesi akan datang": 50 daripada 50.

## Kayu ukur JUMLAH (lawan saham rawak sepanjang ERA)

| # | Prasyarat | Pencetus | Penapis saham | Belian (hari isyarat) | Tangkap penuh % (rawak) | Kena henti % | Kelebihan tangkap penuh K1 / K2 / K3 |
|---|---|---|---|---|---|---|---|
| 1 | QQQ >= 20% di bawah puncak | M73 ADX(5) > 40 + Julat Terkecil 6 Hari (ditala 1) | RSI14 < 40 + >= 30% di bawah puncak 52 minggu | 1,314 (144) | 37.1 (8.4) | 39.8 | +54.5 / +26.0 / +31.2 |
| 2 | QQQ >= 20% di bawah puncak | M73 ADX(5) > 40 + Julat Terkecil 6 Hari (ditala 1) | ADX > 25 + >= 30% di bawah puncak 52 minggu | 1,411 (176) | 34.4 (8.4) | 41.7 | +53.7 / +23.3 / +31.2 |
| 3 | QQQ >= 20% di bawah puncak | M73 ADX(5) > 40 + Julat Terkecil 6 Hari (ditala 1) | >= 30% di bawah puncak 52 minggu | 1,508 (179) | 33.1 (8.5) | 40.9 | +54.5 / +21.9 / +31.2 |
| 4 | QQQ >= 20% di bawah puncak | M73 ADX(5) > 40 + Julat Terkecil 6 Hari (ditala 1) | RSI14 < 40 + volum 10 hari > volum 50 hari | 1,452 (156) | 31.7 (7.6) | 37.5 | +44.3 / +21.9 / +40.8 |
| 5 | QQQ >= 10% di bawah puncak + earnings dalam 1-5 sesi akan datang | N119 3 tutup turun berturut | MACD > isyarat + ATR% >= 4 | 1,068 (201) | 29.4 (9.2) | 45.5 | +21.6 / +19.5 / +22.7 |
| 6 | QQQ >= 20% di bawah puncak | M73 ADX(5) > 40 + Julat Terkecil 6 Hari | RSI14 < 40 + ATR% >= 4 | 2,021 (178) | 31.1 (9.2) | 39.7 | +54.8 / +19.3 / -10.4 |
| 7 | QQQ >= 20% di bawah puncak + tiada earnings dalam 20 sesi akan datang | M73 ADX(5) > 40 + Julat Terkecil 6 Hari | RSI14 < 40 + ATR% >= 4 | 1,478 (164) | 30.4 (9.2) | 38.4 | +59.0 / +18.0 / -10.4 |
| 8 | QQQ >= 20% di bawah puncak + tiada earnings dalam 20 sesi akan datang | M73 ADX(5) > 40 + Julat Terkecil 6 Hari (ditala 1) | RSI14 < 40 + ADX > 25 | 1,252 (147) | 30.7 (7.6) | 35.9 | +48.6 / +20.3 / -10.4 |
| 9 | QQQ >= 20% di bawah puncak | M73 ADX(5) > 40 + Julat Terkecil 6 Hari (ditala 1) | RSI14 < 40 + ADX > 25 | 1,668 (164) | 30.9 (7.4) | 37.1 | +47.9 / +20.5 / +40.4 |
| 10 | QQQ OFF + earnings dalam 1-5 sesi akan datang | N16 RSI2<10 tanpa penapis | MACD > isyarat + >= 30% di bawah puncak 52 minggu | 431 (194) | 25.5 (8.6) | 46.4 | +21.6 / +16.1 / +10.2 |
| 11 | SPY bawah SMA200 + earnings dalam 1-5 sesi akan datang | N16 RSI2<10 tanpa penapis | MACD > isyarat | 731 (183) | 22.4 (6.6) | 34.7 | +10.5 / +18.4 / +17.6 |
| 12 | QQQ >= 10% di bawah puncak + earnings dalam 1-5 sesi akan datang | N119 3 tutup turun berturut | ATR% >= 4 | 1,918 (287) | 28.6 (9.4) | 45.2 | +23.0 / +17.4 / +25.7 |
| 13 | SPY bawah SMA200 + earnings dalam 1-5 sesi akan datang | N119 3 tutup turun berturut | MACD > isyarat + ATR% >= 4 | 1,168 (224) | 27.2 (8.7) | 46.9 | +11.6 / +20.0 / +21.7 |
| 14 | SPY bawah SMA200 + earnings dalam 1-5 sesi akan datang | N119 3 tutup turun berturut | MACD > isyarat + >= 30% di bawah puncak 52 minggu | 1,050 (222) | 28.3 (8.4) | 44.4 | +21.8 / +20.3 / +14.5 |
| 15 | QQQ >= 20% di bawah puncak | M73 ADX(5) > 40 + Julat Terkecil 6 Hari | ADX > 25 + >= 30% di bawah puncak 52 minggu | 2,000 (198) | 28.3 (8.5) | 39.9 | +55.5 / +17.6 / -10.4 |
| 16 | QQQ >= 20% di bawah puncak + tiada earnings dalam 20 sesi akan datang | M73 ADX(5) > 40 + Julat Terkecil 6 Hari (ditala 1) | RSI14 < 40 | 1,328 (146) | 29.9 (7.5) | 35.6 | +48.3 / +19.4 / -10.4 |
| 17 | Januari + tiada earnings dalam 20 sesi akan datang | M105 Supertrend tulen (ditala 2) | MACD > isyarat + >= 30% di bawah puncak 52 minggu | 514 (141) | 22.8 (8.4) | 31.7 | +19.9 / +14.1 / +0.9 |
| 18 | QQQ >= 20% di bawah puncak | M73 ADX(5) > 40 + Julat Terkecil 6 Hari (ditala 1) | RSI14 < 40 | 1,773 (165) | 30.1 (7.4) | 36.4 | +48.0 / +19.5 / +40.4 |
| 19 | turun-naik SPY 21 hari >= 25% setahun + kejutan untung terkini positif (SUE > 0) | M73 ADX(5) > 40 + Julat Terkecil 6 Hari | RSI14 < 40 + >= 30% di bawah puncak 52 minggu | 903 (175) | 28.9 (8.1) | 36.9 | +27.2 / +21.1 / +5.4 |
| 20 | QQQ >= 10% di bawah puncak + earnings dalam 1-5 sesi akan datang | N119 3 tutup turun berturut | MACD > isyarat + >= 30% di bawah puncak 52 minggu | 1,040 (204) | 28.4 (8.7) | 44.0 | +29.2 / +18.9 / +14.9 |
| 21 | QQQ >= 20% di bawah puncak | M73 ADX(5) > 40 + Julat Terkecil 6 Hari | RSI14 < 40 + >= 30% di bawah puncak 52 minggu | 2,187 (178) | 27.6 (8.6) | 38.9 | +57.6 / +16.3 / -10.4 |
| 22 | SPY bawah SMA200 + earnings dalam 1-5 sesi akan datang | N16 RSI2<10 tanpa penapis | >= 30% di bawah puncak 52 minggu | 945 (257) | 26.6 (8.6) | 46.7 | +21.4 / +16.6 / +19.8 |
| 23 | hari 90% turun kemudian naik (20 sesi) + earnings dalam 1-5 sesi akan datang | N119 3 tutup turun berturut | >= 30% di bawah puncak 52 minggu + ATR% >= 4 | 1,239 (327) | 30.0 (9.1) | 46.7 | +17.0 / +23.1 / +21.1 |
| 24 | SPY bawah SMA200 + earnings dalam 1-5 sesi akan datang | N16 RSI2<10 tanpa penapis | RSI14 < 40 + >= 30% di bawah puncak 52 minggu | 646 (210) | 25.9 (8.5) | 50.0 | +22.2 / +14.7 / +22.6 |
| 25 | QQQ >= 10% di bawah puncak + earnings dalam 1-5 sesi akan datang | N16 RSI2<10 tanpa penapis | MACD > isyarat | 665 (164) | 24.4 (6.9) | 32.9 | +11.2 / +19.1 / +17.6 |
| 26 | SPY bawah SMA200 + earnings dalam 1-5 sesi akan datang | N119 3 tutup turun berturut | >= 30% di bawah puncak 52 minggu + ATR% >= 4 | 1,258 (250) | 28.3 (9.5) | 49.1 | +21.6 / +17.7 / +20.8 |
| 27 | SPY bawah SMA200 + earnings dalam 1-5 sesi akan datang | N119 3 tutup turun berturut | >= 30% di bawah puncak 52 minggu | 1,645 (298) | 27.6 (8.4) | 45.8 | +23.7 / +17.8 / +18.1 |
| 28 | QQQ >= 20% di bawah puncak | M73 ADX(5) > 40 + Julat Terkecil 6 Hari | >= 30% di bawah puncak 52 minggu + volum 10 hari > volum 50 hari | 2,109 (196) | 26.2 (8.6) | 40.1 | +57.0 / +15.8 / -10.4 |
| 29 | QQQ >= 20% di bawah puncak + tiada earnings dalam 20 sesi akan datang | M73 ADX(5) > 40 + Julat Terkecil 6 Hari | RSI14 < 40 + >= 30% di bawah puncak 52 minggu | 1,587 (163) | 27.5 (8.7) | 37.7 | +59.1 / +15.7 / -10.4 |
| 30 | turun-naik SPY 21 hari >= 25% setahun + kejutan untung terkini positif (SUE > 0) | M01 Bollinger Band + RSI (ditala 2) | ADX > 25 + >= 30% di bawah puncak 52 minggu | 687 (148) | 26.2 (8.2) | 41.5 | +16.7 / +17.3 / +21.6 |
| 31 | QQQ >= 20% di bawah puncak | M73 ADX(5) > 40 + Julat Terkecil 6 Hari | RSI14 < 40 + ADX > 25 | 2,175 (184) | 27.0 (7.5) | 34.5 | +47.1 / +17.3 / -10.4 |
| 32 | SPY bawah SMA200 + earnings dalam 1-5 sesi akan datang | N119 3 tutup turun berturut | ATR% >= 4 | 1,899 (307) | 26.4 (8.8) | 47.7 | +14.6 / +17.5 / +24.6 |
| 33 | QQQ >= 20% di bawah puncak + tiada earnings dalam 20 sesi akan datang | M73 ADX(5) > 40 + Julat Terkecil 6 Hari | RSI14 < 40 + ADX > 25 | 1,579 (166) | 26.3 (7.6) | 32.7 | +49.2 / +16.2 / -10.4 |
| 34 | QQQ >= 10% di bawah puncak + earnings dalam 1-5 sesi akan datang | N16 RSI2<10 tanpa penapis | >= 30% di bawah puncak 52 minggu | 968 (241) | 28.2 (8.9) | 45.2 | +28.9 / +17.2 / +21.1 |
| 35 | QQQ >= 10% di bawah puncak + earnings dalam 1-5 sesi akan datang | N16 RSI2<10 tanpa penapis | RSI14 < 40 + >= 30% di bawah puncak 52 minggu | 660 (206) | 28.2 (8.7) | 46.8 | +29.2 / +16.2 / +23.9 |
| 36 | SPY bawah SMA200 + earnings dalam 1-5 sesi akan datang | M73 ADX(5) > 40 + Julat Terkecil 6 Hari (ditala 2) | RSI14 < 40 + >= 30% di bawah puncak 52 minggu | 704 (256) | 26.6 (8.4) | 46.3 | +21.4 / +16.5 / +16.8 |
| 37 | QQQ >= 20% di bawah puncak | M73 ADX(5) > 40 + Julat Terkecil 6 Hari (ditala 1) | ADX > 25 + volum 10 hari > volum 50 hari | 1,848 (191) | 25.3 (7.3) | 37.7 | +44.3 / +15.9 / +40.8 |
| 38 | QQQ >= 10% di bawah puncak + earnings dalam 1-5 sesi akan datang | N119 3 tutup turun berturut | >= 30% di bawah puncak 52 minggu + ATR% >= 4 | 1,308 (235) | 29.4 (9.8) | 47.3 | +28.4 / +17.3 / +23.8 |
| 39 | SPY bawah SMA200 + earnings dalam 1-5 sesi akan datang | M01 Bollinger Band + RSI (ditala 2) | ADX > 25 + >= 30% di bawah puncak 52 minggu | 288 (142) | 25.7 (8.0) | 48.3 | +20.3 / +15.3 / +25.8 |
| 40 | QQQ >= 10% di bawah puncak + earnings dalam 1-5 sesi akan datang | M01 Bollinger Band + RSI (ditala 2) | >= 30% di bawah puncak 52 minggu | 611 (194) | 25.7 (8.8) | 45.8 | +22.9 / +14.3 / +30.9 |
| 41 | QQQ OFF + earnings dalam 1-5 sesi akan datang | N16 RSI2<10 tanpa penapis | RSI14 < 40 + >= 30% di bawah puncak 52 minggu | 1,175 (436) | 22.5 (8.7) | 48.9 | +16.2 / +13.7 / +8.9 |
| 42 | turun-naik SPY 21 hari >= 25% setahun + kejutan untung terkini positif (SUE > 0) | M73 ADX(5) > 40 + Julat Terkecil 6 Hari | >= 30% di bawah puncak 52 minggu + volum 10 hari > volum 50 hari | 970 (218) | 27.4 (8.1) | 37.1 | +21.7 / +20.4 / +7.6 |
| 43 | turun-naik SPY 21 hari >= 25% setahun + sektor 3 terbawah (pulangan 63 sesi) | N16 RSI2<10 tanpa penapis | RSI14 < 40 + ADX < 20 | 580 (139) | 23.8 (7.2) | 32.2 | +16.1 / +12.1 / +28.8 |
| 44 | QQQ >= 10% di bawah puncak + earnings dalam 1-5 sesi akan datang | M73 ADX(5) > 40 + Julat Terkecil 6 Hari (ditala 2) | RSI14 < 40 + >= 30% di bawah puncak 52 minggu | 687 (244) | 26.3 (8.9) | 44.5 | +28.1 / +13.9 / +16.7 |
| 45 | SPY bawah SMA200 + earnings dalam 1-5 sesi akan datang | N119 3 tutup turun berturut | RSI14 < 40 + >= 30% di bawah puncak 52 minggu | 691 (205) | 27.4 (8.4) | 50.1 | +26.2 / +15.3 / +19.7 |
| 46 | hari 90% turun kemudian naik (20 sesi) + earnings dalam 1-5 sesi akan datang | N16 RSI2<10 tanpa penapis | >= 30% di bawah puncak 52 minggu + ATR% >= 4 | 673 (251) | 27.9 (9.0) | 48.3 | +16.9 / +19.5 / +24.4 |
| 47 | SPY bawah SMA200 + earnings dalam 1-5 sesi akan datang | M73 ADX(5) > 40 + Julat Terkecil 6 Hari (ditala 2) | RSI14 < 40 + ADX > 25 | 884 (268) | 24.0 (6.4) | 38.3 | +17.9 / +17.1 / +18.2 |
| 48 | QQQ >= 10% di bawah puncak + earnings dalam 1-5 sesi akan datang | N16 RSI2<10 tanpa penapis | RSI14 < 40 + ATR% >= 4 | 647 (199) | 28.9 (9.6) | 47.0 | +24.8 / +16.4 / +31.2 |
| 49 | follow-through day aktif (QQQ, 20 sesi) + earnings dalam 1-5 sesi akan datang | N119 3 tutup turun berturut | MACD > isyarat + ATR% >= 4 | 1,304 (256) | 25.5 (9.2) | 50.2 | +12.5 / +17.9 / +14.2 |
| 50 | QQQ >= 10% di bawah puncak + earnings dalam 1-5 sesi akan datang | M73 ADX(5) > 40 + Julat Terkecil 6 Hari (ditala 2) | RSI14 < 40 + ATR% >= 4 | 735 (251) | 27.9 (9.3) | 42.7 | +29.4 / +14.3 / +19.9 |

Pencetus berbeza: 5; memakai "earnings dalam 1-5 sesi akan datang": 28 daripada 50.
