# CS06: tala bersama prasyarat — induk lawan anak pada saham yang tidak dilihat (backtest, BUKAN bukti)

> **Status keputusan (kad skor, harga 2026-11-12):** TERBUKTI 0 · CALON 0 · BELUM CUKUP 223 · GAGAL 0 · NEGATIF 0. Rejim QQQ OFF sejak 2026-10-16. Hanya **TERBUKTI** layak untuk wang sebenar (`laporan/KAD_SKOR.md`); nombor dalam laporan ini BUKAN keputusan dan tidak boleh dibaca sebagai pangkat untuk wang sebenar.

Dijana `kajian/carian_setup/cs_tala6.py`. Pradaftar: `kajian/SPEC_CARIAN_SETUP.md` pindaan 14 Nov 2026 (k) bahagian B. **Jangan sunting secara manual.**

Induk = setup papan CS06. Tiga paksi ditala serentak pada kumpulan A: varian pencetus (induk kaedah M: 24 varian ±25 %), ambang penapis saham dan ambang prasyarat. Anak = sel dengan markah DATARAN tertinggi (median sel dan jirannya), bukan puncak. Angka di bawah daripada **kumpulan B**; "lebih" = kadar tangkap penuh tolak saham rawak (kayu ukur papan induk), mata peratus.

**Bacaan dikunci:** tala menolong hanya jika lebih separuh anak mengatasi induknya pada kumpulan B DAN pada K3. Daripada 20 induk, 2 kekal (sel induk sendiri yang terbaik) dan 18 mendapat anak yang cukup belian. Anak mengatasi induk pada kumpulan B: 6 daripada 18; pada K3: 4 daripada 17; kedua-duanya: 3 daripada 18. **Tala menolong: TIDAK.**

| Induk | Kayu ukur | Anak | Apa yang berubah | Induk: tangkap penuh % (rawak) · lebih · lebih K3 · kena henti % | Anak: tangkap penuh % (rawak) · lebih · lebih K3 · kena henti % | Belian anak | Anak > induk (B / K3) |
|---|---|---|---|---|---|---|---|
| `F39` | pilih | `F70` | parameter pencetus ditala (`M73.2u4`); prasyarat: rejim ON baharu (<= 10 sesi) + earnings dalam 1-5 sesi akan datang → rejim ON baharu (<= 30 sesi) + earnings dalam 1-3 sesi akan datang; penapis: tutup > MA50 + >= 30% di bawah puncak 52 minggu → tutup > MA50 + >= 20% di bawah puncak 52 minggu | 21.2 (10.5) · +10.6 · +12.0 · 42.5 | 16.2 (7.4) · +8.8 · +6.3 · 46.4 | 1,175 | ✗ / ✗ |
| `F40` | pilih | `F71` | parameter pencetus ditala (`M14.2u5`); prasyarat: rejim ON baharu (<= 10 sesi) + earnings dalam 1-5 sesi akan datang → rejim ON baharu (<= 30 sesi) + earnings dalam 1-5 sesi akan datang; penapis: Supertrend naik + >= 30% di bawah puncak 52 minggu → Supertrend naik + >= 40% di bawah puncak 52 minggu | 21.9 (10.6) · +11.3 · +13.5 · 42.4 | 20.0 (10.9) · +9.1 · +9.3 · 51.6 | 644 | ✗ / ✗ |
| `F58` | pilih | `F72` | prasyarat: >= 60% saham di atas MA50 + earnings dalam 1-5 sesi akan datang → >= 50% saham di atas MA50 + earnings dalam 1-5 sesi akan datang; penapis: Supertrend naik + >= 30% di bawah puncak 52 minggu → Supertrend naik + >= 20% di bawah puncak 52 minggu | 19.8 (7.6) · +12.2 · +15.8 · 47.5 | 18.3 (9.3) · +9.1 · +9.7 · 45.1 | 1,130 | ✗ / ✗ |
| `F42` | pilih | `F73` | parameter pencetus ditala (`M159.1u4`); prasyarat: distribution day QQQ <= 2 dalam 25 sesi + >= 60% saham industri di atas MA50 → distribution day QQQ <= 3 dalam 25 sesi + >= 50% saham industri di atas MA50; penapis: RS >= 90 + ATR% >= 4 → RS >= 80 + ATR% >= 5 | 15.5 (8.1) · +7.4 · +1.7 · 48.8 | 14.8 (9.0) · +5.7 · +1.0 · 57.7 | 610 | ✗ / ✗ |
| `F45` | pilih | `F74` | parameter pencetus ditala (`M94.1u10`) | 17.0 (12.2) · +4.9 · +4.8 · 47.7 | 17.4 (12.2) · +5.2 · +5.0 · 47.9 | 754 | ✓ / ✓ |
| `F59` | pilih | `F75` | prasyarat: distribution day QQQ <= 2 dalam 25 sesi → distribution day QQQ <= 3 dalam 25 sesi; penapis: RS >= 70 + ATR% >= 4 → RS >= 70 + ATR% >= 5 | 13.6 (9.0) · +4.6 · -7.0 · 46.9 | 14.4 (9.7) · +4.7 · -7.2 · 56.3 | 458 | ✓ / ✗ |
| `F44` | pilih | `F76` | parameter pencetus ditala (`M79.2u20`) | 14.0 (10.0) · +3.9 · +4.8 · 53.8 | 14.2 (9.9) · +4.4 · +3.6 · 53.6 | 632 | ✓ / ✗ |
| `F60` | pilih | `F77` | prasyarat: SPY atas SMA200 + >= 60% saham sektor di atas MA50 → SPY atas SMA200 + >= 70% saham sektor di atas MA50; penapis: RS >= 90 + ATR% >= 4 → RS >= 95 + ATR% >= 5 | 13.6 (9.0) · +4.6 · +5.5 · 53.2 | 14.6 (8.7) · +6.0 · +2.2 · 56.9 | 847 | ✓ / ✗ |
| `F61` | pilih | – | induk kekal (1 calon pencetus, 3 sel) | 12.2 (9.6) · +2.6 · +2.2 · 53.6 | – | – | – |
| `F47` | pilih | `F78` | parameter pencetus ditala (`M124.2u13`); prasyarat: regangan turun-naik SPY (proksi VIX) + SPY > SMA200 + hasil suku terkini tumbuh >= 20% → regangan turun-naik SPY (proksi VIX) + SPY > SMA200 + hasil suku terkini tumbuh >= 10% | 9.9 (8.2) · +1.7 · -0.3 · 38.3 | 7.7 (7.3) · +0.4 · -1.9 · 34.0 | 712 | ✗ / ✗ |
| `F62` | jumlah | `F79` | parameter pencetus ditala (`M73.1u15`); penapis: RSI14 < 40 + >= 30% di bawah puncak 52 minggu → RSI14 < 40 + >= 20% di bawah puncak 52 minggu | 37.1 (8.4) · +28.7 · +31.2 · 39.8 | 35.9 (8.0) · +28.0 · +33.5 · 38.3 | 1,152 | ✗ / ✓ |
| `F49` | jumlah | `F80` | prasyarat: QQQ >= 10% di bawah puncak + earnings dalam 1-5 sesi akan datang → QQQ >= 7.5% di bawah puncak + earnings dalam 1-7 sesi akan datang; penapis: MACD > isyarat + ATR% >= 4 → MACD > isyarat + ATR% >= 5 | 29.4 (9.2) · +20.2 · +22.7 · 45.5 | 29.3 (9.6) · +19.7 · +22.5 · 48.7 | 1,059 | ✗ / ✗ |
| `F63` | jumlah | `F81` | penapis: MACD > isyarat + >= 30% di bawah puncak 52 minggu → MACD > isyarat + >= 20% di bawah puncak 52 minggu | 25.5 (8.6) · +16.9 · +10.2 · 46.4 | 22.2 (7.5) · +14.7 · +15.7 · 42.0 | 681 | ✗ / ✓ |
| `F43` | jumlah | `F82` | parameter pencetus ditala (`M105.2u22`); penapis: MACD > isyarat + >= 30% di bawah puncak 52 minggu → MACD > isyarat + >= 40% di bawah puncak 52 minggu | 22.8 (8.4) · +14.3 · +0.9 · 31.7 | 23.3 (9.4) · +13.9 · +0.1 · 35.3 | 292 | ✗ / ✗ |
| `F64` | jumlah | `F83` | parameter pencetus ditala (`M01.2u11`); prasyarat: turun-naik SPY 21 hari >= 25% setahun + kejutan untung terkini positif (SUE > 0) → turun-naik SPY 21 hari >= 20% setahun + kejutan untung terkini positif (SUE > 0); penapis: ADX > 25 + >= 30% di bawah puncak 52 minggu → ADX > 25 + >= 40% di bawah puncak 52 minggu | 26.2 (8.2) · +18.0 · +21.6 · 41.5 | 24.6 (9.3) · +15.4 · +0.2 · 50.4 | 593 | ✗ / ✗ |
| `F65` | jumlah | – | induk kekal (1 calon pencetus, 3 sel) | 21.8 (6.0) · +15.8 · +11.8 · 37.1 | – | – | – |
| `F66` | jumlah | `F84` | parameter pencetus ditala (`M79.2u14`); prasyarat: <= 30% saham di atas MA50 + kejutan untung terkini positif (SUE > 0) → <= 40% saham di atas MA50 + kejutan untung terkini positif (SUE > 0); penapis: >= 30% di bawah puncak 52 minggu + tutup dalam 25% teratas julat hari → >= 40% di bawah puncak 52 minggu + tutup dalam 25% teratas julat hari | 22.1 (8.8) · +13.4 · -2.7 · 53.5 | 24.1 (9.8) · +14.3 · +0.8 · 57.8 | 640 | ✓ / ✓ |
| `F67` | jumlah | `F85` | prasyarat: turun-naik SPY 21 hari >= 25% setahun + kejutan untung terkini positif (SUE > 0) → turun-naik SPY 21 hari >= 20% setahun + kejutan untung terkini positif (SUE > 0) | 26.8 (8.5) · +18.3 · +30.3 · 39.2 | 18.5 (8.2) · +10.3 · +10.0 · 47.3 | 1,001 | ✗ / ✗ |
| `F68` | jumlah | `F86` | penapis: ADX < 20 + >= 30% di bawah puncak 52 minggu → ADX < 20 + >= 20% di bawah puncak 52 minggu | 18.4 (8.1) · +10.3 · +2.8 · 42.8 | 16.6 (7.0) · +9.5 · +1.7 · 37.6 | 1,202 | ✗ / ✗ |
| `F69` | jumlah | `F87` | parameter pencetus ditala (`M28.2u12`); prasyarat: turun-naik SPY 21 hari >= 25% setahun → turun-naik SPY 21 hari >= 20% setahun; penapis: >= 30% di bawah puncak 52 minggu + volum hari isyarat >= 1.5x purata 50 → >= 50% di bawah puncak 52 minggu + volum hari isyarat >= 1.5x purata 50 | 22.3 (8.5) · +13.8 · +15.4 · 52.1 | 26.2 (10.3) · +15.9 · +21.6 · 57.2 | 703 | ✓ / ✓ |

Setup lengkap anak (henti × keluar dipilih ikut tangkap penuh sendiri, pindaan (k); kumpulan B):

| Anak | Henti · keluar | Tangkap penuh % (rawak) | Rugi ≥ 8 % % | Pegang (sesi) | Menang % | Purata setiap dagangan % |
|---|---|---|---|---|---|---|
| `F70` | H2 · X13 ATAU X18 | 16.1 (7.1) | 38.2 | 12.8 | 44 | -0.04 |
| `F71` | H3 · X12 DAN X23 | 21.9 (11.2) | 38.9 | 13.8 | 49 | +0.72 |
| `F72` | H4 · X12 | 20.0 (9.0) | 28.6 | 16.0 | 52 | +1.45 |
| `F73` | H3 · X13 | 14.3 (9.0) | 36.8 | 16.0 | 50 | +1.14 |
| `F74` | H3 · X12 DAN X15 | 16.8 (12.1) | 30.0 | 16.8 | 52 | +2.90 |
| `F75` | H3 · X12 DAN X23 | 14.4 (9.2) | 38.1 | 17.1 | 48 | +0.87 |
| `F76` | H2 · X09 DAN X21 | 13.5 (9.4) | 48.6 | 13.4 | 39 | +0.75 |
| `F77` | H3 · X12 ATAU X13 | 15.8 (8.8) | 32.0 | 14.0 | 49 | +1.65 |
| `F78` | H2 · X00 | 7.4 (7.2) | 29.4 | 16.8 | 52 | +0.58 |
| `F79` | H3 · X21 | 34.9 (6.5) | 15.9 | 15.9 | 73 | +10.14 |
| `F80` | H2 · X10 DAN X21 | 25.4 (9.1) | 48.9 | 12.6 | 45 | +2.42 |
| `F81` | H3 · X08 DAN X21 | 21.7 (7.4) | 27.9 | 16.0 | 60 | +3.20 |
| `F82` | H3 · X00 | 23.1 (9.4) | 23.1 | 18.3 | 67 | +5.50 |
| `F83` | H3 · X00 | 25.0 (9.3) | 24.6 | 18.1 | 63 | +6.99 |
| `F84` | H3 · X12 DAN X22 | 23.7 (9.8) | 29.0 | 18.3 | 58 | +3.98 |
| `F85` | H3 · X12 | 18.7 (8.0) | 27.7 | 17.5 | 59 | +4.24 |
| `F86` | H3 · X21 | 15.9 (5.5) | 23.7 | 15.1 | 59 | +3.23 |
| `F87` | H3 · X21 | 28.9 (9.0) | 24.6 | 15.5 | 64 | +6.54 |

## Kaveat

- Tala dijalankan pada kumpulan A sahaja; kumpulan B hanya mengukur. Tetapi reka bentuk CS06 dipilih selepas hasil CS05 pada kumpulan B dilihat, jadi kumpulan B bukan lagi "tidak dilihat" bagi keluarga setup ini.
- Setiap induk mempunyai ratusan hingga ribuan sel; yang terbaik sebahagiannya nasib walaupun dengan dataran. Belian anak pada K3 selalunya sedikit.
- Anak didaftarkan dalam keluarga F (status BACKTEST). Tiada setup masuk jejak hadapan (keputusan pengguna 14 Nov 2026).
