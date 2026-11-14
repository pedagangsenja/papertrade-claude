# Tinjauan prasyarat: apa selain QQQ yang mengubah peluang saham "lari"? (backtest, BUKAN bukti)

> **Status keputusan (kad skor, harga 2026-11-12):** TERBUKTI 0 · CALON 0 · BELUM CUKUP 223 · GAGAL 0 · NEGATIF 0. Rejim QQQ OFF sejak 2026-10-16. Hanya **TERBUKTI** layak untuk wang sebenar (`laporan/KAD_SKOR.md`); nombor dalam laporan ini BUKAN keputusan dan tidak boleh dibaca sebagai pangkat untuk wang sebenar.

Dijana `kajian/carian_setup/cs_prasyarat.py`. Pradaftar: `kajian/SPEC_CARIAN_SETUP.md` pindaan 14 Nov 2026 (h). **Jangan sunting secara manual.**

Prasyarat = isyarat yang BUKAN daripada harga saham itu sendiri. "Lari" = naik ≥ 5 % minggu pertama, capai ≥ 10 % sebelum henti −8 %, masih ≥ 10 % pada minggu ke-4. Angka jadual daripada **kumpulan B** (saham yang carian tidak lihat, 2010 – Ogo 2026). "Konsisten" = bilangan kepingan (E1, E2 kumpulan A; K1, K2, K3 kumpulan B) di mana kadar lari lebih tinggi bila prasyarat BENAR.

| Prasyarat | % masa benar | Semua saham: lari % benar / palsu | Konsisten | Kena henti % benar / palsu | Kohort F: lari % benar / palsu | Konsisten (kohort) | Isyarat kohort (benar) |
|---|---|---|---|---|---|---|---|
| **A. Arah pasaran** | | | | | | | |
| QQQ ON | 60 | 4.5 / 6.9 | 0/5 | 30.8 / 33.1 | 12.0 / 13.7 | 0/5 | 15,585 |
| QQQ OFF | 40 | 6.9 / 4.5 | 5/5 | 33.1 / 30.8 | 13.7 / 12.0 | 5/5 | 12,465 |
| SPY atas SMA200 | 84 | 4.7 / 9.9 | 0/5 | 30.4 / 38.8 | 12.3 / 14.3 | 0/5 | 21,640 |
| SPY bawah SMA200 | 16 | 9.9 / 4.7 | 5/5 | 38.8 / 30.4 | 14.3 / 12.3 | 5/5 | 6,410 |
| QQQ dalam 3% dari puncak 52 minggu | 55 | 4.2 / 7.1 | 0/5 | 30.2 / 33.7 | 11.7 / 13.6 | 0/5 | 12,869 |
| QQQ >= 10% di bawah puncak | 15 | 9.7 / 4.8 | 5/5 | 39.4 / 30.4 | 14.5 / 12.3 | 3/5 | 6,056 |
| QQQ >= 20% di bawah puncak | 6 | 10.5 / 5.2 | 5/5 | 39.6 / 31.2 | 13.8 / 12.6 | 1/3 | 3,009 |
| rejim ON baharu (<= 10 sesi) | 20 | 4.6 / 5.7 | 0/5 | 30.3 / 32.1 | 10.9 / 13.2 | 0/5 | 5,006 |
| rejim OFF baharu (<= 10 sesi) | 19 | 5.5 / 5.5 | 2/5 | 33.0 / 31.4 | 12.3 / 12.9 | 2/5 | 5,943 |
| QQQ RSI14 < 35 | 4 | 11.1 / 5.3 | 5/5 | 31.1 / 31.8 | 16.6 / 12.5 | 3/5 | 1,599 |
| QQQ naik >= 3% dalam 5 sesi | 14 | 5.8 / 5.4 | 2/5 | 33.5 / 31.5 | 12.1 / 12.9 | 1/5 | 4,536 |
| **B. Turun-naik pasaran** | | | | | | | |
| turun-naik SPY 21 hari >= 25% setahun | 9 | 10.3 / 5.0 | 5/5 | 38.2 / 31.1 | 13.5 / 12.6 | 3/5 | 4,396 |
| turun-naik SPY 21 hari <= 10% setahun | 30 | 3.4 / 6.4 | 0/5 | 28.9 / 33.0 | 10.7 / 13.3 | 1/5 | 5,711 |
| turun-naik SPY menurun (21 hari < 63 hari) | 54 | 5.0 / 6.1 | 0/5 | 29.8 / 34.0 | 12.5 / 13.0 | 3/5 | 14,763 |
| **C. Keluasan pasaran** | | | | | | | |
| >= 60% saham di atas MA50 | 51 | 4.3 / 6.8 | 0/5 | 29.9 / 33.7 | 11.6 / 13.8 | 1/5 | 13,693 |
| <= 30% saham di atas MA50 | 11 | 10.5 / 4.9 | 5/5 | 36.7 / 31.1 | 15.2 / 12.4 | 3/5 | 3,476 |
| keluasan naik >= 10 mata dalam 10 sesi | 25 | 5.1 / 5.6 | 0/5 | 31.1 / 31.9 | 12.2 / 12.9 | 2/5 | 6,870 |
| >= 60% saham di atas MA200 | 65 | 4.3 / 7.8 | 0/5 | 29.6 / 35.9 | 12.2 / 13.4 | 2/5 | 15,576 |
| >= 15% saham dalam 5% dari puncak 52 minggu | 74 | 4.3 / 8.9 | 0/5 | 29.9 / 36.8 | 11.4 / 15.0 | 0/5 | 17,750 |
| **D. Sektor saham itu** | | | | | | | |
| sektor 3 teratas (pulangan 63 sesi) | 27 | 5.3 / 5.8 | 0/5 | 31.9 / 32.4 | 12.3 / 13.0 | 1/5 | 9,281 |
| sektor 3 terbawah (pulangan 63 sesi) | 23 | 6.0 / 5.5 | 5/5 | 33.6 / 31.9 | 13.1 / 12.6 | 2/5 | 5,875 |
| >= 60% saham sektor di atas MA50 | 50 | 4.4 / 6.9 | 0/5 | 30.1 / 34.5 | 12.0 / 13.4 | 1/5 | 13,464 |
| **E. Industri saham itu** | | | | | | | |
| industri 20% teratas (pulangan 63 sesi) | 19 | 5.6 / 5.5 | 3/5 | 33.5 / 31.5 | 12.8 / 12.7 | 3/5 | 8,095 |
| industri 20% teratas (pulangan 21 sesi) | 19 | 5.4 / 5.5 | 1/5 | 33.2 / 31.5 | 12.8 / 12.7 | 1/5 | 7,108 |
| industri 20% terbawah (pulangan 63 sesi) | 18 | 6.3 / 5.3 | 5/5 | 34.7 / 31.2 | 13.3 / 12.6 | 2/5 | 4,153 |
| >= 60% saham industri di atas MA50 | 51 | 4.3 / 6.8 | 0/5 | 29.7 / 34.1 | 12.3 / 13.3 | 1/5 | 14,071 |
| saham lain dalam industri sama naik >= 20% dalam 20 sesi | 36 | 6.3 / 5.1 | 5/5 | 36.4 / 29.3 | 12.6 / 12.9 | 1/5 | 15,401 |
| **F. Earnings syarikat** | | | | | | | |
| earnings dalam 1-5 sesi akan datang | 8 | 12.0 / 4.9 | 5/5 | 36.4 / 31.0 | 20.1 / 12.1 | 5/5 | 2,148 |
| 0-4 sesi selepas earnings | 8 | 5.3 / 5.5 | 2/5 | 30.1 / 31.6 | 12.9 / 12.8 | 1/5 | 3,424 |
| 5-19 sesi selepas earnings | 24 | 4.7 / 5.8 | 0/5 | 29.4 / 32.2 | 12.0 / 13.1 | 0/5 | 5,573 |
| tiada earnings dalam 20 sesi akan datang | 67 | 4.7 / 7.1 | 0/5 | 29.2 / 36.1 | 12.0 / 14.8 | 1/5 | 15,987 |
| kejutan untung terkini positif (SUE > 0) | 59 | 5.1 / 5.8 | 0/5 | 30.2 / 32.6 | 13.3 / 12.3 | 5/5 | 11,958 |
| hasil suku terkini tumbuh >= 20% | 19 | 7.6 / 4.9 | 5/5 | 39.5 / 29.2 | 13.7 / 12.4 | 5/5 | 7,888 |
| harga melompat >= 5% pada hari earnings (20 sesi lalu) | 6 | 5.9 / 5.5 | 5/5 | 34.5 / 31.3 | 12.8 / 12.9 | 2/5 | 3,486 |
| **G. Kalendar** | | | | | | | |
| Nov-Apr | 49 | 5.7 / 5.3 | 4/5 | 32.4 / 31.1 | 12.6 / 12.9 | 3/5 | 14,075 |
| Mei-Okt | 51 | 5.3 / 5.7 | 1/5 | 31.1 / 32.4 | 12.9 / 12.6 | 2/5 | 13,975 |
| 7 hari pertama bulan | 23 | 5.9 / 5.4 | 5/5 | 31.7 / 31.8 | 14.2 / 12.3 | 4/5 | 6,657 |
| Januari | 8 | 6.3 / 5.4 | 4/5 | 33.0 / 31.6 | 13.5 / 12.7 | 3/5 | 2,201 |

## Bacaan

- Menaikkan kadar lari bagi SEMUA saham dalam kelima-lima kepingan (14): QQQ OFF; SPY bawah SMA200; QQQ >= 10% di bawah puncak; QQQ >= 20% di bawah puncak; QQQ RSI14 < 35; turun-naik SPY 21 hari >= 25% setahun; <= 30% saham di atas MA50; sektor 3 terbawah (pulangan 63 sesi); industri 20% terbawah (pulangan 63 sesi); saham lain dalam industri sama naik >= 20% dalam 20 sesi; earnings dalam 1-5 sesi akan datang; hasil suku terkini tumbuh >= 20%; harga melompat >= 5% pada hari earnings (20 sesi lalu); 7 hari pertama bulan.
- Menurunkan kadar lari dalam kelima-lima kepingan (16): QQQ ON; SPY atas SMA200; QQQ dalam 3% dari puncak 52 minggu; rejim ON baharu (<= 10 sesi); turun-naik SPY 21 hari <= 10% setahun; turun-naik SPY menurun (21 hari < 63 hari); >= 60% saham di atas MA50; keluasan naik >= 10 mata dalam 10 sesi; >= 60% saham di atas MA200; >= 15% saham dalam 5% dari puncak 52 minggu; sektor 3 teratas (pulangan 63 sesi); >= 60% saham sektor di atas MA50; >= 60% saham industri di atas MA50; 5-19 sesi selepas earnings; tiada earnings dalam 20 sesi akan datang; kejutan untung terkini positif (SUE > 0).
- Menaikkan kadar lari bagi isyarat KOHORT F dalam kelima-lima kepingan (5): QQQ OFF; SPY bawah SMA200; earnings dalam 1-5 sesi akan datang; kejutan untung terkini positif (SUE > 0); hasil suku terkini tumbuh >= 20%.

## Kaveat

- Prasyarat pasaran, keluasan dan kalendar berubah ikut HARI: bar banyak tetapi pemerhatian bebas sedikit; satu tahun yang luar biasa boleh mengubah bacaan. Sebab itu lajur "Konsisten" lebih penting daripada beza peratus.
- Prasyarat yang menaikkan kadar lari selalunya turut menaikkan kadar kena henti (saham lebih meruap); baca kedua-dua lajur.
- "Earnings akan datang" memakai tarikh sebenar (pandang ke hadapan ringan). Peta sektor/industri ialah peta semasa. Tiada saham delist. Set 2000 bukan tapisan Shariah.
- Tinjauan, bukan pemilihan: 38 prasyarat diukur, jadi beberapa akan kelihatan baik secara kebetulan. Prasyarat hanya boleh dipakai selepas dimasukkan ke pusingan carian dengan pradaftar tersendiri.
