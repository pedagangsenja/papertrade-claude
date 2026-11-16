# CS15 — keluarga K26 "lonjak lalu undur" (zon Fibonacci): setup F baharu (backtest, BUKAN bukti)

> **Status keputusan (kad skor, harga 2026-11-13):** TERBUKTI 0 · CALON 0 · BELUM CUKUP 226 · GAGAL 0 · NEGATIF 0. Rejim QQQ OFF sejak 2026-10-16. Hanya **TERBUKTI** layak untuk wang sebenar (`laporan/KAD_SKOR.md`); nombor dalam laporan ini BUKAN keputusan dan tidak boleh dibaca sebagai pangkat untuk wang sebenar.

Dijana `kajian/carian_setup/cs_cs15.py`; peraturan `kajian/SPEC_CARIAN_SETUP.md` pindaan 16 Nov 2026 (y) = peraturan pendaftaran CS13 (pindaan (v)). Idea daripada tangkapan skrin pengguna (POST-HOC). Jangan sunting secara manual.

## Ringkasan

- Calon (sehingga 5 setiap varian, skor A > 0): **262**; cukup belian untuk dinilai: 234; lulus pada saham yang carian tidak lihat: **112**.
- B1 kadar lulus: calon **47.9 %** lawan kawalan rawak CS13 18.1 % → lulus. B2 lebih baik daripada rawak pada 2025–26: calon **60.7 %** lawan kawalan 52.4 % → GAGAL. Anggaran bahagian lulus kerana nasib: ~37.7 %.
- Kembar (beli saham sama pada hari sama, pertindihan ≥ 80 %, antara calon K26): 44.
- **Tiada kod F baharu**: syarat pendaftaran (B1 DAN B2) TIDAK lulus. 68 calon lulus yang bukan kembar disenaraikan di bawah sebagai REKOD sahaja (tanpa kod).
- **Sumbangan corak K26 di atas prasyarat** (lawan saham lain yang lulus prasyarat dan penapis yang sama, hari dan turun-naik sama): jelas positif (melebihi 2 ralat piawai) bagi **5** daripada 68 calon lulus; median +1.0 mata.
- **Fibonacci istimewa? YA** — zon iklan 61.8–78.6 % mengatasi purata zon jiran dalam 13 daripada 20 pasangan (tempoh, saiz kaki) dan positif dalam 17 (saham yang carian tidak lihat; kumpulan carian: 13 dan 14).

## Calon lulus — REKOD sahaja, tiada kod F (saham yang carian tidak lihat; stop loss 4 × ATR14 + cara pegang B; satu posisi setiap saham)

Disusun ikut kadar tangkap (naik ≥ 5 % minggu pertama DAN naik lagi hingga minggu ke-4), seperti senarai utama.

| Kod / calon | Pencetus | Prasyarat | Penapis saham | Tangkap % (rawak) | Naik ≥ 5 % minggu 1 % | Longgar `naik` % (rawak) | Menang % | Purata % | Rugi ≥ 15 % | Hari pegang | Belian setahun (Shariah) | Lebih rawak 2025–26 | Sumbangan K26 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| K0222 | K26.008 lonjak >= 30% dalam 10 hari lalu undur ke zon 61.8%-78.6% kaki | QQQ OFF | volum 10 hari > volum 50 hari + ATR% >= 4 | 21.6 (19.4) | 43.8 | 40.3 (42.3) | 55.8 | +7.8 | 17.5 | 22 | 41 (23) | +1.8 | +2.0 (±2.8) |
| K0133 | K26.082 lonjak >= 20% dalam 40 hari lalu undur ke zon 50.0%-61.8% kaki | QQQ OFF + earnings dalam 1-5 sesi akan datang | MA20 > MA50 + MA50 > MA200 | 18.6 (10.7) | 33.2 | 39.3 (42.4) | 52.0 | +3.0 | 13.4 | 22 | 23 (15) | +0.0 | +2.0 (±4.0) |
| K0046 | K26.083 lonjak >= 20% dalam 40 hari lalu undur ke zon 61.8%-78.6% kaki | Mei-Okt + earnings dalam 1-5 sesi akan datang | MA50 > MA200 + MA50 naik (lawan 20 bar lalu) | 17.8 (11.2) | 31.0 | 41.9 (41.4) | 52.3 | +4.8 | 10.6 | 22 | 24 (17) | +0.9 | +0.5 (±3.8) |
| K0120 | K26.087 lonjak >= 30% dalam 40 hari lalu undur ke zon 50.0%-61.8% kaki | turun-naik SPY menurun (21 hari < 63 hari) + earnings dalam 1-5 sesi akan datang | – | 17.4 (9.6) | 32.2 | 30.2 (34.9) | 42.7 | -0.3 | 18.7 | 21 | 22 (13) | +1.9 | +3.6 (±3.9) |
| K0199 | K26.094 lonjak >= 40% dalam 40 hari lalu undur ke zon 78.6%-100.0% kaki | distribution day QQQ >= 5 dalam 25 sesi + tiada earnings dalam 20 sesi akan datang | RSI14 < 40 + ADX < 20 | 17.3 (15.8) | 33.0 | 35.5 (37.6) | 49.3 | +4.8 | 19.4 | 21 | 26 (14) | +2.7 | +0.5 (±3.1) |
| K0010 | K26.021 lonjak >= 20% dalam 15 hari lalu undur ke zon 38.2%-50.0% kaki | SPY Peringkat 2 Weinstein (atas SMA150 yang naik) + earnings dalam 1-5 sesi akan datang | tutup > MA200 + MA20 > MA50 | 17.1 (10.6) | 30.7 | 37.1 (37.6) | 50.9 | +1.4 | 16.5 | 21 | 23 (15) | +14.0 | +2.0 (±3.9) |
| K0005 | K26.021 lonjak >= 20% dalam 15 hari lalu undur ke zon 38.2%-50.0% kaki | Mei-Okt + earnings dalam 1-5 sesi akan datang | – | 16.9 (12.4) | 35.1 | 39.1 (40.9) | 54.0 | +2.1 | 14.3 | 21 | 22 (15) | +10.8 | +0.6 (±3.9) |
| K0111 | K26.027 lonjak >= 30% dalam 15 hari lalu undur ke zon 50.0%-61.8% kaki | QQQ OFF + kejutan untung terkini positif (SUE > 0) | MACD > 0 + Supertrend naik | 15.9 (13.2) | 29.1 | 38.1 (38.7) | 47.6 | +2.2 | 17.2 | 22 | 28 (16) | +5.7 | +2.0 (±3.3) |
| K0007 | K26.021 lonjak >= 20% dalam 15 hari lalu undur ke zon 38.2%-50.0% kaki | SPY Peringkat 2 Weinstein (atas SMA150 yang naik) + earnings dalam 1-5 sesi akan datang | tutup > MA50 + Supertrend naik | 15.6 (10.5) | 29.4 | 34.9 (37.4) | 48.4 | +0.1 | 18.8 | 21 | 28 (17) | +8.9 | +0.6 (±3.5) |
| K0191 | K26.022 lonjak >= 20% dalam 15 hari lalu undur ke zon 50.0%-61.8% kaki | QQQ OFF + kejutan untung terkini positif (SUE > 0) | Supertrend naik + ATR% >= 4 | 15.6 (12.7) | 28.0 | 40.9 (39.4) | 51.1 | +3.0 | 15.4 | 22 | 58 (36) | +5.9 | +1.4 (±2.2) |
| K0100 | K26.083 lonjak >= 20% dalam 40 hari lalu undur ke zon 61.8%-78.6% kaki | distribution day QQQ >= 5 dalam 25 sesi + earnings dalam 1-5 sesi akan datang | – | 15.6 (11.0) | 30.5 | 36.9 (38.1) | 48.8 | +1.7 | 16.0 | 21 | 58 (40) | +2.7 | +0.4 (±2.2) |
| K0054 | K26.041 lonjak >= 20% dalam 20 hari lalu undur ke zon 38.2%-50.0% kaki | earnings dalam 1-5 sesi akan datang | tutup > MA50 | 15.4 (10.2) | 30.0 | 35.1 (37.5) | 48.7 | +0.5 | 14.2 | 21 | 52 (34) | +7.5 | +0.4 (±2.6) |
| K0056 | K26.061 lonjak >= 20% dalam 30 hari lalu undur ke zon 38.2%-50.0% kaki | distribution day QQQ >= 5 dalam 25 sesi + earnings dalam 1-5 sesi akan datang | RSI14 > 50 + Supertrend naik | 15.0 (10.8) | 29.7 | 36.1 (37.9) | 49.7 | +0.5 | 17.3 | 21 | 28 (20) | +6.0 | -0.5 (±3.5) |
| K0038 | K26.047 lonjak >= 30% dalam 20 hari lalu undur ke zon 50.0%-61.8% kaki | kejutan untung terkini positif (SUE > 0) | templat trend Minervini + RS >= 70 | 14.8 (11.2) | 28.2 | 36.4 (36.7) | 47.5 | +2.5 | 16.7 | 21 | 48 (31) | +5.5 | +2.3 (±2.4) |
| K0194 | K26.022 lonjak >= 20% dalam 15 hari lalu undur ke zon 50.0%-61.8% kaki | distribution day QQQ >= 5 dalam 25 sesi + kejutan untung terkini positif (SUE > 0) | RS >= 70 + ATR% >= 4 | 14.7 (12.2) | 29.8 | 36.9 (35.8) | 49.1 | +1.7 | 19.9 | 21 | 71 (47) | +1.4 | +0.8 (±2.0) |
| K0097 | K26.062 lonjak >= 20% dalam 30 hari lalu undur ke zon 50.0%-61.8% kaki | QQQ ON + hasil suku terkini tumbuh >= 20% | RS >= 70 + ATR% >= 4 | 14.6 (10.0) | 29.3 | 32.3 (33.5) | 43.0 | +0.8 | 19.6 | 21 | 37 (24) | +2.1 | +2.1 (±2.8) |
| K0113 | K26.047 lonjak >= 30% dalam 20 hari lalu undur ke zon 50.0%-61.8% kaki | SPY atas SMA200 + kejutan untung terkini positif (SUE > 0) | templat trend Minervini + ADX > 25 | 14.5 (11.2) | 27.5 | 38.4 (37.2) | 48.2 | +2.2 | 15.9 | 22 | 37 (21) | +5.5 | +2.1 (±2.7) |
| K0159 | K26.022 lonjak >= 20% dalam 15 hari lalu undur ke zon 50.0%-61.8% kaki | kejutan untung terkini positif (SUE > 0) | RS >= 70 + ATR% >= 4 | 14.5 (11.7) | 28.5 | 36.9 (36.2) | 49.1 | +2.0 | 19.9 | 21 | 89 (57) | +0.7 | +1.0 (±1.8) |
| K0256 | K26.052 lonjak >= 40% dalam 20 hari lalu undur ke zon 50.0%-61.8% kaki | distribution day QQQ >= 5 dalam 25 sesi | Supertrend naik | 14.5 (13.4) | 31.2 | 30.3 (34.3) | 47.3 | +1.1 | 22.0 | 21 | 91 (44) | +1.0 | +0.7 (±1.7) |
| K0150 | K26.004 lonjak >= 20% dalam 10 hari lalu undur ke zon 78.6%-100.0% kaki | SPY atas SMA200 | tutup > MA50 + RS >= 70 | 14.4 (10.3) | 30.8 | 32.4 (34.8) | 47.5 | +2.5 | 20.5 | 21 | 64 (31) | +4.6 | +3.2 (±2.1) |
| K0203 | K26.046 lonjak >= 30% dalam 20 hari lalu undur ke zon 38.2%-50.0% kaki | turun-naik SPY menurun (21 hari < 63 hari) + >= 60% saham sektor di atas MA50 | MA50 > MA200 + RS >= 90 | 14.1 (9.9) | 27.3 | 37.0 (35.6) | 49.5 | +3.1 | 17.1 | 21 | 34 (20) | +2.7 | +1.4 (±2.8) |
| K0060 | K26.061 lonjak >= 20% dalam 30 hari lalu undur ke zon 38.2%-50.0% kaki | earnings dalam 1-5 sesi akan datang | RSI14 > 50 + MACD > 0 | 13.9 (9.9) | 28.6 | 36.2 (36.4) | 49.8 | +0.4 | 15.4 | 21 | 39 (26) | +4.2 | -0.5 (±2.9) |
| K0071 | K26.041 lonjak >= 20% dalam 20 hari lalu undur ke zon 38.2%-50.0% kaki | QQQ ON + earnings dalam 1-5 sesi akan datang | RSI14 > 50 + Supertrend naik | 13.9 (8.9) | 29.3 | 32.4 (34.4) | 47.5 | -0.2 | 17.3 | 21 | 27 (18) | +3.6 | +0.7 (±3.5) |
| K0001 | K26.025 lonjak >= 20% dalam 15 hari lalu undur ke zon 38.2%-78.6% kaki | SPY Peringkat 2 Weinstein (atas SMA150 yang naik) + earnings dalam 1-5 sesi akan datang | – | 13.9 (10.0) | 29.2 | 32.7 (36.4) | 46.7 | -0.0 | 18.8 | 21 | 37 (22) | +7.2 | -0.8 (±2.8) |
| K0105 | K26.047 lonjak >= 30% dalam 20 hari lalu undur ke zon 50.0%-61.8% kaki | SPY atas SMA200 + kejutan untung terkini positif (SUE > 0) | MACD > 0 + RS >= 70 | 13.8 (11.1) | 27.6 | 35.6 (36.7) | 45.9 | +1.5 | 18.2 | 21 | 59 (34) | +4.1 | +1.5 (±2.1) |
| K0108 | K26.026 lonjak >= 30% dalam 15 hari lalu undur ke zon 38.2%-50.0% kaki | turun-naik SPY menurun (21 hari < 63 hari) | Supertrend naik + RS >= 90 | 13.8 (10.7) | 29.7 | 32.5 (35.2) | 44.4 | +2.8 | 22.4 | 21 | 38 (20) | +0.3 | +1.9 (±2.7) |
| K0140 | K26.007 lonjak >= 30% dalam 10 hari lalu undur ke zon 50.0%-61.8% kaki | >= 60% saham sektor di atas MA50 | tutup > MA200 + RS >= 90 | 13.8 (10.5) | 29.2 | 29.7 (34.5) | 41.5 | +4.8 | 23.4 | 21 | 23 (11) | +3.7 | +1.6 (±3.4) |
| K0028 | K26.045 lonjak >= 20% dalam 20 hari lalu undur ke zon 38.2%-78.6% kaki | QQQ ON + earnings dalam 1-5 sesi akan datang | tutup > MA50 | 13.7 (8.8) | 28.9 | 32.7 (34.0) | 45.7 | -0.6 | 16.0 | 21 | 38 (26) | +3.0 | +0.7 (±2.9) |
| K0077 | K26.061 lonjak >= 20% dalam 30 hari lalu undur ke zon 38.2%-50.0% kaki | Mei-Okt + earnings dalam 1-5 sesi akan datang | tutup > MA50 + Supertrend naik | 13.7 (10.1) | 28.6 | 37.1 (38.9) | 47.6 | +0.5 | 13.6 | 21 | 30 (20) | +5.4 | -0.7 (±3.1) |
| K0149 | K26.092 lonjak >= 40% dalam 40 hari lalu undur ke zon 50.0%-61.8% kaki | turun-naik SPY menurun (21 hari < 63 hari) | MA50 > MA200 + ATR% >= 4 | 13.6 (10.4) | 25.3 | 36.1 (36.0) | 45.4 | +2.0 | 18.3 | 22 | 87 (50) | +1.9 | +2.0 (±1.7) |
| K0089 | K26.002 lonjak >= 20% dalam 10 hari lalu undur ke zon 50.0%-61.8% kaki | – | Supertrend naik + RS >= 90 | 13.6 (10.4) | 27.7 | 33.7 (35.5) | 45.3 | +1.8 | 20.8 | 21 | 90 (53) | +0.8 | +1.8 (±1.7) |
| K0098 | K26.087 lonjak >= 30% dalam 40 hari lalu undur ke zon 50.0%-61.8% kaki | turun-naik SPY menurun (21 hari < 63 hari) | RS >= 70 + ATR% >= 4 | 13.6 (10.2) | 25.4 | 35.2 (35.5) | 45.1 | +1.6 | 19.5 | 21 | 87 (52) | +2.7 | +1.7 (±1.7) |
| K0179 | K26.004 lonjak >= 20% dalam 10 hari lalu undur ke zon 78.6%-100.0% kaki | – | MA50 > MA200 + ATR% >= 4 | 13.6 (11.8) | 30.3 | 32.0 (35.5) | 45.6 | +2.2 | 20.4 | 21 | 176 (93) | +0.8 | +0.9 (±1.2) |
| K0195 | K26.097 lonjak >= 50% dalam 40 hari lalu undur ke zon 50.0%-61.8% kaki | – | MA50 > MA200 + RSI14 < 40 | 13.5 (11.1) | 26.5 | 40.3 (37.5) | 49.1 | +2.3 | 15.4 | 22 | 45 (27) | +1.3 | +2.5 (±2.4) |
| K0011 | K26.081 lonjak >= 20% dalam 40 hari lalu undur ke zon 38.2%-50.0% kaki | SPY atas SMA200 + earnings dalam 1-5 sesi akan datang | hari naik (tutup > buka) | 13.4 (9.8) | 27.0 | 33.9 (38.3) | 48.1 | +0.2 | 9.8 | 21 | 18 (14) | +2.7 | -0.4 (±4.0) |
| K0138 | K26.092 lonjak >= 40% dalam 40 hari lalu undur ke zon 50.0%-61.8% kaki | – | RS >= 70 + ATR% >= 4 | 13.3 (11.2) | 27.6 | 36.3 (36.4) | 47.6 | +2.4 | 18.4 | 22 | 133 (75) | +2.0 | +0.6 (±1.4) |
| K0086 | K26.002 lonjak >= 20% dalam 10 hari lalu undur ke zon 50.0%-61.8% kaki | QQQ ON + >= 60% saham sektor di atas MA50 | RS >= 90 + ATR% >= 4 | 13.3 (9.9) | 29.0 | 31.5 (34.4) | 43.1 | +3.0 | 23.0 | 21 | 33 (17) | +1.8 | +0.5 (±2.9) |
| K0074 | K26.065 lonjak >= 20% dalam 30 hari lalu undur ke zon 38.2%-78.6% kaki | earnings dalam 1-5 sesi akan datang | ADX > 25 + dalam 15% dari puncak 52 minggu | 13.3 (8.3) | 26.8 | 41.3 (37.2) | 50.1 | +0.8 | 10.2 | 21 | 29 (20) | +5.0 | +0.2 (±3.4) |
| K0261 | K26.052 lonjak >= 40% dalam 20 hari lalu undur ke zon 50.0%-61.8% kaki | – | MACD > 0 + RS >= 70 | 13.3 (11.6) | 29.9 | 31.6 (35.7) | 45.3 | +1.3 | 22.5 | 21 | 78 (41) | +2.9 | +0.5 (±1.8) |
| K0249 | K26.052 lonjak >= 40% dalam 20 hari lalu undur ke zon 50.0%-61.8% kaki | – | MA50 > MA200 + MACD > 0 | 13.2 (11.2) | 28.5 | 32.1 (36.1) | 44.3 | +1.1 | 21.3 | 21 | 87 (45) | +1.7 | +1.0 (±1.7) |
| K0175 | K26.004 lonjak >= 20% dalam 10 hari lalu undur ke zon 78.6%-100.0% kaki | SPY atas SMA200 | tutup > MA200 + RS >= 70 | 13.2 (10.3) | 29.9 | 30.8 (34.7) | 44.2 | +1.9 | 21.7 | 21 | 100 (48) | +1.9 | +1.9 (±1.6) |
| K0131 | K26.042 lonjak >= 20% dalam 20 hari lalu undur ke zon 50.0%-61.8% kaki | nisbah 4% (10 hari) > 2 + >= 60% saham sektor di atas MA50 | tutup > MA200 + RSI14 > 50 | 13.1 (10.4) | 22.0 | 40.3 (38.6) | 52.9 | +3.6 | 13.4 | 22 | 21 (14) | +8.6 | +2.1 (±3.6) |
| K0102 | K26.083 lonjak >= 20% dalam 40 hari lalu undur ke zon 61.8%-78.6% kaki | turun-naik SPY menurun (21 hari < 63 hari) + earnings dalam 1-5 sesi akan datang | MA20 > MA50 + MA50 naik (lawan 20 bar lalu) | 13.1 (8.8) | 26.8 | 37.5 (35.8) | 51.4 | +3.1 | 12.0 | 21 | 22 (15) | +4.8 | -0.3 (±3.7) |
| K0144 | K26.027 lonjak >= 30% dalam 15 hari lalu undur ke zon 50.0%-61.8% kaki | distribution day QQQ >= 5 dalam 25 sesi + kejutan untung terkini positif (SUE > 0) | tutup > MA200 + RS >= 70 | 13.0 (12.0) | 29.6 | 33.6 (35.4) | 45.9 | +0.5 | 20.8 | 21 | 44 (27) | +1.4 | +0.1 (±2.4) |
| K0122 | K26.067 lonjak >= 30% dalam 30 hari lalu undur ke zon 50.0%-61.8% kaki | hasil suku terkini tumbuh >= 20% | MACD > 0 + RS >= 70 | 13.0 (10.7) | 28.0 | 33.6 (35.4) | 44.1 | +1.3 | 18.7 | 21 | 61 (41) | +4.2 | +1.0 (±2.1) |
| K0137 | K26.042 lonjak >= 20% dalam 20 hari lalu undur ke zon 50.0%-61.8% kaki | hasil suku terkini tumbuh >= 20% | MA50 > MA200 + RS >= 70 | 13.0 (10.3) | 25.2 | 38.5 (36.9) | 48.6 | +1.9 | 15.1 | 22 | 96 (69) | +4.5 | +1.2 (±1.7) |
| K0134 | K26.092 lonjak >= 40% dalam 40 hari lalu undur ke zon 50.0%-61.8% kaki | SPY atas SMA200 | MACD > 0 + RS >= 70 | 13.0 (10.5) | 27.1 | 35.0 (36.1) | 46.3 | +1.8 | 17.8 | 21 | 93 (47) | +2.8 | +1.7 (±1.7) |
| K0210 | K26.066 lonjak >= 30% dalam 30 hari lalu undur ke zon 38.2%-50.0% kaki | >= 60% saham sektor di atas MA50 | RSI14 > 50 + RS >= 90 | 12.9 (9.7) | 26.4 | 34.9 (34.6) | 47.7 | +2.1 | 18.6 | 21 | 40 (25) | +0.1 | +0.6 (±2.6) |
| K0104 | K26.026 lonjak >= 30% dalam 15 hari lalu undur ke zon 38.2%-50.0% kaki | >= 60% saham di atas MA50 | Supertrend naik + RS >= 90 | 12.9 (8.9) | 27.1 | 32.2 (34.0) | 44.0 | +2.9 | 22.6 | 21 | 33 (18) | +2.2 | +1.8 (±2.9) |
| K0130 | K26.042 lonjak >= 20% dalam 20 hari lalu undur ke zon 50.0%-61.8% kaki | – | Supertrend naik + RS >= 90 | 12.7 (10.4) | 26.9 | 35.9 (36.7) | 47.0 | +1.3 | 18.1 | 21 | 122 (78) | +1.2 | +0.6 (±1.4) |
| K0109 | K26.067 lonjak >= 30% dalam 30 hari lalu undur ke zon 50.0%-61.8% kaki | QQQ SMA10 > SMA20 + hasil suku terkini tumbuh >= 20% | MA50 > MA200 + RS >= 70 | 12.6 (9.1) | 26.5 | 31.7 (33.9) | 41.8 | +0.5 | 20.3 | 21 | 43 (28) | +5.7 | +2.1 (±2.4) |
| K0116 | K26.062 lonjak >= 20% dalam 30 hari lalu undur ke zon 50.0%-61.8% kaki | QQQ ON | RS >= 70 + ATR% >= 4 | 12.6 (10.2) | 26.4 | 34.4 (34.3) | 45.2 | +0.9 | 20.8 | 21 | 111 (68) | +1.2 | +0.3 (±1.5) |
| K0126 | K26.067 lonjak >= 30% dalam 30 hari lalu undur ke zon 50.0%-61.8% kaki | QQQ SMA10 > SMA20 + kejutan untung terkini positif (SUE > 0) | RS >= 70 + ATR% >= 4 | 12.5 (10.2) | 25.6 | 33.3 (34.3) | 43.4 | +1.3 | 21.0 | 21 | 49 (29) | +4.9 | +0.4 (±2.3) |
| K0121 | K26.063 lonjak >= 20% dalam 30 hari lalu undur ke zon 61.8%-78.6% kaki | regangan turun-naik SPY (proksi VIX) + SPY > SMA200 + industri 20% terbawah (pulangan 63 sesi) | tutup > MA200 + MA50 > MA200 | 12.5 (10.7) | 23.1 | 38.3 (41.3) | 48.3 | +2.0 | 11.3 | 22 | 20 (14) | +2.0 | +0.4 (±3.4) |
| K0094 | K26.002 lonjak >= 20% dalam 10 hari lalu undur ke zon 50.0%-61.8% kaki | QQQ ON + >= 60% saham industri di atas MA50 | Supertrend naik + RS >= 90 | 12.5 (9.8) | 27.6 | 31.5 (34.4) | 41.7 | +2.4 | 20.2 | 21 | 36 (19) | +0.8 | +1.5 (±2.6) |
| K0173 | K26.097 lonjak >= 50% dalam 40 hari lalu undur ke zon 50.0%-61.8% kaki | – | MA20 > MA50 + RS >= 70 | 12.4 (11.1) | 27.9 | 34.5 (35.6) | 47.1 | +2.5 | 20.3 | 22 | 87 (46) | +1.9 | +0.7 (±1.7) |
| K0170 | K26.088 lonjak >= 30% dalam 40 hari lalu undur ke zon 61.8%-78.6% kaki | Nov-Apr | RS >= 70 + volum hari isyarat >= 1.5x purata 50 | 12.2 (10.1) | 23.7 | 32.7 (35.1) | 42.2 | +0.2 | 18.5 | 21 | 33 (20) | +2.4 | +1.6 (±2.7) |
| K0031 | K26.001 lonjak >= 20% dalam 10 hari lalu undur ke zon 38.2%-50.0% kaki | nisbah 4% (10 hari) > 2 | tutup > MA50 + Supertrend naik | 12.2 (10.5) | 22.6 | 41.4 (40.6) | 51.4 | +3.3 | 13.8 | 22 | 49 (32) | +0.6 | +1.5 (±2.2) |
| K0162 | K26.069 lonjak >= 30% dalam 30 hari lalu undur ke zon 78.6%-100.0% kaki | Nov-Apr | MA50 naik (lawan 20 bar lalu) + MACD > 0 | 12.1 (10.2) | 28.7 | 27.9 (31.5) | 38.5 | -1.6 | 26.0 | 21 | 31 (14) | +0.2 | +1.7 (±2.8) |
| K0238 | K26.024 lonjak >= 20% dalam 15 hari lalu undur ke zon 78.6%-100.0% kaki | >= 60% saham di atas MA200 | ADX < 20 | 12.0 (10.5) | 24.9 | 32.9 (35.5) | 42.6 | +2.0 | 18.9 | 21 | 99 (49) | +0.5 | +1.1 (±1.5) |
| K0062 | K26.082 lonjak >= 20% dalam 40 hari lalu undur ke zon 50.0%-61.8% kaki | QQQ ON | RS >= 70 + ATR% >= 4 | 12.0 (9.7) | 25.3 | 34.4 (33.9) | 43.9 | +1.2 | 20.4 | 21 | 99 (57) | +1.0 | +0.4 (±1.5) |
| K0103 | K26.062 lonjak >= 20% dalam 30 hari lalu undur ke zon 50.0%-61.8% kaki | SPY atas SMA200 + hasil suku terkini tumbuh >= 20% | MA20 > MA50 + RS >= 70 | 12.0 (9.4) | 23.2 | 36.7 (36.6) | 46.2 | +1.3 | 13.7 | 21 | 88 (60) | +4.9 | +1.3 (±1.7) |
| K0184 | K26.022 lonjak >= 20% dalam 15 hari lalu undur ke zon 50.0%-61.8% kaki | kejutan untung terkini positif (SUE > 0) | tutup > MA50 + RS >= 70 | 11.8 (10.5) | 23.0 | 38.0 (36.9) | 47.5 | +1.3 | 13.8 | 21 | 115 (76) | +0.4 | +0.7 (±1.4) |
| K0082 | K26.062 lonjak >= 20% dalam 30 hari lalu undur ke zon 50.0%-61.8% kaki | QQQ ON + hasil suku terkini tumbuh >= 20% | MA20 > MA50 + RS >= 70 | 11.5 (8.8) | 23.4 | 34.1 (34.3) | 44.5 | +0.3 | 14.6 | 21 | 58 (40) | +2.0 | +1.3 (±2.0) |
| K0088 | K26.082 lonjak >= 20% dalam 40 hari lalu undur ke zon 50.0%-61.8% kaki | >= 60% saham di atas MA50 | RS >= 70 + ATR% >= 4 | 11.4 (9.0) | 23.7 | 34.3 (33.7) | 43.5 | +2.3 | 18.2 | 21 | 73 (40) | +3.6 | +0.4 (±1.8) |
| K0205 | K26.024 lonjak >= 20% dalam 15 hari lalu undur ke zon 78.6%-100.0% kaki | >= 15% saham dalam 5% dari puncak 52 minggu | ADX < 20 | 11.0 (9.9) | 24.0 | 31.4 (34.5) | 39.6 | -0.0 | 21.4 | 21 | 114 (56) | +1.0 | +0.8 (±1.4) |
| K0189 | K26.071 lonjak >= 40% dalam 30 hari lalu undur ke zon 38.2%-50.0% kaki | turun-naik SPY 21 hari <= 10% setahun | templat trend Minervini + ATR% >= 4 | 10.6 (8.2) | 26.6 | 28.9 (31.8) | 38.6 | -0.5 | 23.0 | 21 | 23 (13) | +1.6 | +0.5 (±2.9) |
| K0236 | K26.071 lonjak >= 40% dalam 30 hari lalu undur ke zon 38.2%-50.0% kaki | turun-naik SPY 21 hari <= 10% setahun | templat trend Minervini + RS >= 70 | 9.5 (7.9) | 23.8 | 30.2 (31.9) | 38.8 | -1.1 | 20.7 | 21 | 26 (17) | +0.9 | +1.4 (±2.6) |

## Fibonacci: zon undur, pencetus sahaja (saham yang carian tidak lihat; satu posisi, pegang 20 sesi)

| Zon undur | Belian | Lebih rawak (purata, mata) |
|---|---|---|
| 0.382-0.500 | 125,539 | +1.0 |
| 0.500-0.618 | 122,635 | +1.0 |
| 0.618-0.786 | 109,597 | +0.8 |
| 0.786-1.000 | 78,951 | +0.7 |
| 0.382-0.786 | 135,762 | +0.9 |

Kaveat (dikunci (y)): idea post-hoc dan hasil ukuran lain sudah dilihat; saham "tidak dilihat" sudah dipakai pusingan terdahulu dan bertindih dengan set 431; tiada saham delist; kembar hanya disemak antara calon K26; kod ini belum dimasukkan ke `hasil/CS13/SENARAI_UTAMA.md` dan dashboard (perlu binaan penuh); BUKAN calon papertrade tanpa keputusan pengguna.
