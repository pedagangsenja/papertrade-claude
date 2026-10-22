# Ujian 5: corak lilin pembalikan dalam aliran naik (AUTOTUNE 2000 saham AS)

> Bukti dalam nota ini ialah pengiraan sendiri, bukan sumber web. Setiap angka datang daripada skrip [uji_lilin_aliran.py](../../lilin/uji_lilin_aliran.py) (larian 22 Okt 2026, 65 s, puncak RAM 3.9 GB, satu proses) dan output perantaraan dalam `/tmp/claude-0/-home-user-papertrade-claude/0793050f-2ee1-522e-9bf0-b633a13089db/scratchpad/lilin/` (`hasil.json`, `isyarat.parquet`, `jadual.txt`; scratchpad ini sementara, jadi jalankan semula skrip untuk menjana semula). Semakan kewarasan ada dalam [semak_lilin.py](../../lilin/semak_lilin.py). Data AUTOTUNE tidak mengandungi saham yang telah delist, jadi semua angka ialah had atas.

## S1. Apakah reka bentuk ujian? (Ditetapkan dan ditulis dalam fail ini SEBELUM sebarang keputusan dikira.)

### Takeaway
Persediaan asas S0 ialah aliran naik, RS tinggi dan tarikan balik. Setiap varian lilin ialah S0 ditambah satu corak lilin pada hari isyarat yang sama, jadi setiap varian ialah subset tepat S0. Semua varian diuji dengan dua kaedah keluar yang sama, dan nilai tambah lilin diukur sebagai beza lebihan atas SPY berbanding S0. Peraturan lulus ditetapkan sebelum keputusan dilihat dan tidak diubah selepas itu.

### Cited Findings

**Data** — [uji_lilin_aliran.py](../../lilin/uji_lilin_aliran.py)
- Dibaca daripada `AUTOTUNE/.cache/`: 10,932,066 bar dan 3,227 saham (semua ticker yang pernah masuk universe bulanan).
- Tarikh akhir data ialah 2026-10-16.
- Penanda aras SPY daripada `idx.parquet`.

**Persediaan S0 pada hari isyarat t** (dikira pada tutup t; beli pada buka t+1)
- Aliran: tutup > SMA50 > SMA200.
- Proksi RS: persentil pulangan 126 bar antara semua saham dalam universe hari itu (kumpulan A dan B digabung). Syarat ≥ 80.
- Tarikan balik, mana-mana satu daripada empat syarat:
  - ≥ 3 tutup lebih rendah dalam 5 perubahan harian yang berakhir pada t;
  - syarat yang sama, berakhir pada t−1;
  - RSI2(t) < 10;
  - RSI2(t−1) < 10.
- Hari t−1 dimasukkan supaya bar pencetus, yang biasanya bar naik, kekal dalam S0. Inilah yang menjadikan setiap varian lilin subset tepat S0.
- Saham mesti berada dalam universe pada bulan t dan dalam kumpulan sampel.
- RSI2 dan ATR14 sama seperti `kod/enjin.py` (`rsi` EWM alfa 1/n; `atr` purata mudah julat sebenar 14 bar).

**Varian (12)**

| Kod | Syarat tambahan atas S0 |
|---|---|
| V00 | Tiada (S0 sahaja). |
| V01 engulfing | Bar t−1 merah, bar t hijau; buka t ≤ tutup t−1; tutup t ≥ buka t−1; badan t ≥ 0.6×ATR14. |
| V02 piercing | Bar t−1 merah; buka t < rendah t−1; tutup t > titik tengah badan t−1; tutup t < buka t−1. |
| V03 hammer | Julat > 0; bayang bawah ≥ 2× badan; tutup dalam pertiga atas julat. |
| V04 three-line-strike | Tiga tutup berturut-turut lebih rendah (t−3, t−2, t−1); tutup t > buka bar t−3. |
| V05 HA | Heikin-Ashi bertukar hijau pada t (merah pada t−1). |
| V06 inside-bar breakout | Bar t−1 berada di dalam julat bar t−2; tutup t > tinggi t−1. |
| V07–V11 | V01, V02, V03, V04 dan V06 masing-masing, ditambah volum t ≥ 1.5× median volum t−20..t−1. |

- HA dengan syarat volum tidak diuji kerana had 12 varian, dan M159 (HA) telah ditolak sebelum ini.

**Kawalan rawak**
- Bagi setiap varian dan sampel: 1000 cabutan sebanyak K isyarat S0 secara rawak tanpa ganti, dengan K = bilangan isyarat varian itu.
- Dilaporkan: selang 2.5–97.5% bagi min lebihan dan p empirik (bahagian cabutan dengan min ≥ min varian).

**Keluar (sama untuk semua varian)**
- (a) Chandelier tutup, sama seperti `standard/keluar_lorong.lorong_henti`:
  - puncak = tutup tertinggi sejak bar beli;
  - paras = max(paras semalam, puncak − 4×ATR14), jadi paras hanya naik;
  - jika tutup < paras, jual pada buka esok;
  - had 60 hari mengikut enjin_at: jika j − t ≥ 60, keluar pada tutup hari j.
- (b) Pegang tetap 10 hari: keluar pada tutup t+10.
- Kos: `enjin_at.kos_sisi` (0.1% ditambah slippage ikut median nilai dagangan 20 hari pada hari isyarat).
- Posisi yang masih terbuka pada akhir tetingkap ditutup pada tutup terakhir.

**Sampel**

| Sampel | Kumpulan | Tempoh masuk | Isyarat S0 |
|---|---|---|---|
| PILIH | A | 2013-01-01 – 2021-12-31 | 128,333 |
| SAH-B | B | 2013-01-01 – 2021-12-31 | 125,233 |
| SAH-22 | A+B | 2022-01-01 – 2026-10-16 | 159,334 |

**Unit dagangan dan metrik**
- Unit utama ialah peringkat isyarat: setiap isyarat ialah satu dagangan, dan dagangan bertindih dibenarkan.
- Semakan ketahanan memakai konvensyen enjin: satu posisi setiap saham, berurutan.
- Lebihan = pulangan bersih dagangan − pulangan SPY dari buka hari masuk hingga harga keluar pada masa yang sama (buka atau tutup).
- t dikira dengan SE berkelompok ikut tarikh beli (CR1).

**Ujian beza**
- Regresi atas semua isyarat S0 dalam sampel: lebihan = a + b·(lilin), dengan SE berkelompok ikut tarikh beli.
- b ialah beza lilin − bukan-lilin. Oleh itu Δ(lilin − S0) = (1 − p)·b, dan t bagi Δ sama dengan t bagi b.

**Peraturan lulus** (setiap gabungan varian × keluar; semua syarat mesti dipenuhi)
1. Min lebihan varian > S0 dalam KETIGA-TIGA sampel.
2. t beza > 3 dalam PILIH.
3. ≥ 10 hari beli berbeza dalam setiap sel.
4. Persentil 5% tidak lebih buruk daripada S0 melebihi 1 mata peratus dalam mana-mana sampel.

Lilin hanya dianggap "menambah nilai" jika ia lulus bagi KEDUA-DUA kaedah keluar.

**Semakan kewarasan** — [semak_lilin.py](../../lilin/semak_lilin.py)
- RSI2 dan ATR14 numba dibandingkan dengan formula pandas `enjin.rsi` dan `keluar_lorong.atr` pada AAPL, CROX, NVDA dan SMCI: beza maksimum 0.00e+00.
- Keluar Chandelier dibandingkan dengan `lorong_henti`: 160 dagangan rawak, 0 berbeza.
- Contoh corak disemak dengan mata. Engulfing AAPL 2014-12-09: buka 24.36 ≤ tutup semalam 24.85, dan tutup 25.23 ≥ buka semalam 25.23. Piercing CROX 2017-11-06: buka 9.05 < rendah semalam 9.13, dan tutup 9.63 > titik tengah 9.575. Three-line-strike CROX 2018-01-08: tutup 12.90, 12.70, 12.20, kemudian tutup 13.23 > buka 12.99.
- Tiada isyarat yang kehilangan harga SPY (`_spy_hilang` = 0 dalam semua sampel).

### Inferences
- Kerana setiap varian ialah subset tepat S0 dengan keluar dan kos yang sama, apa-apa beza mestilah datang daripada pilihan hari oleh lilin, bukan daripada aliran, RS atau cara keluar. Inilah soalan yang ditanya.

### Gaps
- Proksi RS di sini (persentil 6 bulan) bukan RS rating rasmi repo (`data/rs/`, `gred.py`). Universe pula ialah 2000 saham teratas ikut kecairan, bukan "kecil–sederhana, median nilai ≥ USD5 juta" seperti cadangan E1.
- Three-line-strike memakai "3 tutup lebih rendah" mengikut arahan ujian. Versi Bulkowski (tiga lilin hitam yang ditelan sepenuhnya) tidak diuji.

## S2. Adakah mana-mana corak lilin menambah nilai atas S0? (Keputusan peraturan lulus)

### Takeaway
**Tidak. 0 daripada 22 gabungan varian × keluar lulus.** t beza tertinggi dalam sampel PILIH ialah 0.54 untuk Chandelier (V03 hammer) dan 1.62 untuk pegang 10 hari (V02 piercing), jauh di bawah ambang 3. Tiada varian yang mengalahkan S0 dalam ketiga-tiga sampel bagi mana-mana keluar pada peringkat isyarat. Kesimpulannya, pencetus lilin dalam persediaan aliran naik ini GAGAL, dan tiada asas untuk menambahnya sebagai syarat beli.

### Cited Findings
- Bilangan varian lilin (daripada 11) yang mempunyai Δ lebihan > 0 berbanding S0 — [hasil.json](/tmp/claude-0/-home-user-papertrade-claude/0793050f-2ee1-522e-9bf0-b633a13089db/scratchpad/lilin/hasil.json):

  | Keluar | PILIH | SAH-B | SAH-22 |
  |---|---|---|---|
  | Chandelier | 4/11 | 2/11 | 6/11 |
  | Pegang 10 hari | 2/11 | 1/11 | 4/11 |

  Bilangan ini sekitar atau di bawah separuh, iaitu seperti lambungan syiling.
- Julat t beza dalam setiap sel:

  | Keluar | PILIH | SAH-B | SAH-22 |
  |---|---|---|---|
  | Chandelier | −1.92 hingga 0.54 | −1.36 hingga 1.15 | −3.23 hingga 1.06 |
  | Pegang 10 hari | −1.38 hingga 1.62 | −1.55 hingga 0.10 | −2.37 hingga 2.21 |

  — [hasil.json](/tmp/claude-0/-home-user-papertrade-claude/0793050f-2ee1-522e-9bf0-b633a13089db/scratchpad/lilin/hasil.json)
- Calon terbaik sampel PILIH, V02 piercing dengan pegang 10 hari:
  - PILIH: Δ +0.77 mata (t beza 1.62); kawalan rawak p = 0.004.
  - Sampel sah: SAH-B Δ −0.42; SAH-22 Δ −0.09. Keputusan: GAGAL.
  — [jadual.txt](/tmp/claude-0/-home-user-papertrade-claude/0793050f-2ee1-522e-9bf0-b633a13089db/scratchpad/lilin/jadual.txt)
- V08 piercing + volum bertukar tanda antara sampel. Ia positif dalam SAH-22 (Chandelier Δ +1.88; 10 hari Δ +1.59; 162 isyarat, 103 hari beli) tetapi negatif dalam PILIH (Δ −1.85 dan −0.29) dan dalam SAH-B (Δ −0.81 dan −0.96). Ini corak hingar bersampel kecil — [jadual.txt](/tmp/claude-0/-home-user-papertrade-claude/0793050f-2ee1-522e-9bf0-b633a13089db/scratchpad/lilin/jadual.txt)
- V11 inside-bar breakout + volum memburukkan keputusan dalam SAH-22 (Chandelier Δ −2.17, t −3.23; p5 lebih buruk 3.50 mata) — [jadual.txt](/tmp/claude-0/-home-user-papertrade-claude/0793050f-2ee1-522e-9bf0-b633a13089db/scratchpad/lilin/jadual.txt)
- Syarat volum ≥ 1.5× tidak membantu. Dalam PILIH, versi dengan volum lebih lemah daripada versi tanpa volum bagi kelima-lima corak di bawah kedua-dua keluar, dan sering memburukkan p5 melebihi 1 mata (contohnya V07 engulfing+vol: Chandelier Δp5 −2.05; 10 hari Δp5 −2.41).
- V05 HA bertukar hijau sangat kerap: 23,179 daripada 128,333 isyarat S0 dalam PILIH (18%). Ia lebih lemah daripada S0 dalam ketiga-tiga sampel bagi kedua-dua keluar. Ini sejajar dengan penolakan M159.

**Jadual penuh** (lebihan dan Δ dalam mata peratus; Δp5 = p5 varian − p5 S0; p kawalan rawak = bahagian cabutan rawak yang min lebihannya ≥ varian), dijana terus daripada `hasil.json`:

#### Keluar (a) Chandelier tutup 4×ATR14 + had 60 hari — peringkat isyarat

| Varian | PILIH n / hari beli | PILIH min % / menang % / p5 % | PILIH lebihan % (t) | PILIH Δ lawan S0 (t beza) | SAH-B lebihan % (Δ; Δp5) | SAH-22 lebihan % (Δ; Δp5) | Kawalan rawak PILIH [2.5–97.5%] (p) | Lulus |
|---|---|---|---|---|---|---|---|---|
| V00_S0 | 128333 / 2267 | 2.00 / 42.2 / -18.01 | -0.04 (-0.31) | — | -0.35 (t -3.01) | -1.15 (t -8.83) | — | rujukan |
| V01_engulf | 3644 / 1233 | 1.36 / 40.9 / -18.13 | -0.47 (-1.51) | -0.43 (-1.42) | -0.76 (-0.41; +0.35) | -0.72 (+0.43; +0.16) | [-0.57, 0.51] (0.935) | GAGAL |
| V02_piercing | 822 / 448 | 2.46 / 42.5 / -17.95 | 0.22 (0.33) | +0.26 (0.40) | -1.13 (-0.78; -0.14) | -0.83 (+0.32; +0.81) | [-1.23, 1.16] (0.322) | GAGAL |
| V03_hammer | 11124 / 2038 | 1.98 / 41.9 / -17.38 | 0.06 (0.27) | +0.10 (0.54) | -0.42 (-0.07; +0.37) | -1.19 (-0.04; +0.59) | [-0.36, 0.26] (0.268) | GAGAL |
| V04_3LS | 2003 / 1017 | 1.46 / 42.1 / -18.20 | -0.48 (-1.23) | -0.43 (-1.16) | 0.24 (+0.59; +0.36) | -1.03 (+0.12; +0.83) | [-0.78, 0.80] (0.871) | GAGAL |
| V05_HAflip | 23179 / 2176 | 1.81 / 42.2 / -17.73 | -0.27 (-1.38) | -0.23 (-1.56) | -0.50 (-0.15; +0.28) | -1.24 (-0.09; +0.00) | [-0.23, 0.17] (0.990) | GAGAL |
| V06_IBbreak | 5092 / 1625 | 2.06 / 41.9 / -18.69 | 0.05 (0.15) | +0.09 (0.30) | -0.53 (-0.17; +0.01) | -1.51 (-0.36; -1.04) | [-0.51, 0.44] (0.347) | GAGAL |
| V07_engulf_vol | 808 / 574 | 0.38 / 40.1 / -20.07 | -1.08 (-1.96) | -1.04 (-1.92) | -0.66 (-0.31; -1.48) | -1.15 (-0.00; -1.36) | [-1.21, 1.07] (0.963) | GAGAL |
| V08_piercing_vol | 118 / 94 | -0.57 / 39.8 / -19.94 | -1.89 (-1.34) | -1.85 (-1.33) | -1.16 (-0.81; -6.42) | 0.73 (+1.88; +3.55) | [-2.94, 3.42] (0.890) | GAGAL |
| V09_hammer_vol | 1674 / 964 | 1.77 / 42.9 / -18.83 | -0.35 (-0.65) | -0.31 (-0.60) | -0.45 (-0.10; -0.63) | -0.76 (+0.39; +1.22) | [-0.88, 0.84] (0.754) | GAGAL |
| V10_3LS_vol | 609 / 458 | 1.59 / 44.2 / -18.03 | -0.33 (-0.52) | -0.29 (-0.46) | 0.32 (+0.67; -0.62) | -0.57 (+0.58; -0.09) | [-1.43, 1.33] (0.650) | GAGAL |
| V11_IBbreak_vol | 1066 / 732 | 1.98 / 43.2 / -20.34 | 0.03 (0.05) | +0.07 (0.13) | -0.74 (-0.39; -1.87) | -3.32 (-2.17; -3.50) | [-1.05, 1.01] (0.432) | GAGAL |

#### Keluar (a) Chandelier tutup 4×ATR14 + had 60 hari — portfolio 8 slot × 12.5% (rank = proksi RS), CAGR % / MDD %

| Varian | PILIH | SAH-B | SAH-22 |
|---|---|---|---|
| SPY | 16.3 / -33.7 | 16.3 / -33.7 | 11.8 / -24.5 |
| V00_S0 | 9.8 / -64.8 | -3.8 / -76.8 | -23.8 / -72.9 |
| V01_engulf | 6.3 / -56.7 | 5.4 / -46.3 | 2.3 / -51.1 |
| V02_piercing | 4.9 / -36.0 | 0.6 / -39.1 | -6.2 / -60.9 |
| V03_hammer | 15.1 / -44.7 | 15.3 / -41.7 | -0.3 / -33.9 |
| V04_3LS | 11.0 / -39.8 | 13.1 / -38.7 | 12.0 / -39.4 |
| V05_HAflip | 16.4 / -39.8 | 9.5 / -47.8 | 4.8 / -44.1 |
| V06_IBbreak | 13.6 / -35.9 | 6.3 / -37.1 | 1.9 / -42.5 |
| V07_engulf_vol | -0.7 / -59.5 | 7.1 / -30.5 | -5.7 / -53.7 |
| V08_piercing_vol | -0.9 / -24.3 | 1.3 / -19.5 | 11.3 / -24.9 |
| V09_hammer_vol | 13.7 / -35.9 | 5.2 / -43.6 | -3.8 / -47.7 |
| V10_3LS_vol | 13.4 / -26.7 | 4.6 / -48.6 | 5.6 / -40.5 |
| V11_IBbreak_vol | 12.9 / -39.7 | 0.5 / -47.0 | -13.9 / -61.6 |

#### Keluar (a) Chandelier tutup 4×ATR14 + had 60 hari — semakan konvensyen enjin (satu posisi setiap saham): lebihan % (Δ lawan S0)

| Varian | PILIH n | PILIH | SAH-B | SAH-22 | Δ > 0 dalam ketiga-tiga? |
|---|---|---|---|---|---|
| V00_S0 | 10254 | -0.14 (+0.00) | -0.29 (+0.00) | -1.10 (+0.00) | — |
| V01_engulf | 2711 | -0.44 (-0.31) | -1.01 (-0.72) | -0.53 (+0.57) | tidak |
| V02_piercing | 771 | 0.07 (+0.21) | -1.28 (-0.99) | -0.95 (+0.15) | tidak |
| V03_hammer | 5323 | -0.02 (+0.11) | -0.27 (+0.02) | -1.08 (+0.02) | ya |
| V04_3LS | 1709 | -0.34 (-0.21) | 0.28 (+0.57) | -1.25 (-0.15) | tidak |
| V05_HAflip | 7930 | -0.15 (-0.02) | -0.31 (-0.02) | -1.02 (+0.08) | tidak |
| V06_IBbreak | 3546 | -0.03 (+0.10) | -0.58 (-0.29) | -1.41 (-0.31) | tidak |
| V07_engulf_vol | 763 | -1.26 (-1.12) | -0.84 (-0.55) | -0.85 (+0.25) | tidak |
| V08_piercing_vol | 118 | -1.89 (-1.75) | -1.04 (-0.76) | 0.19 (+1.28) | tidak |
| V09_hammer_vol | 1396 | -0.23 (-0.09) | -0.49 (-0.21) | -0.98 (+0.12) | tidak |
| V10_3LS_vol | 581 | -0.15 (-0.01) | 0.28 (+0.57) | -0.73 (+0.37) | tidak |
| V11_IBbreak_vol | 979 | 0.02 (+0.16) | -0.86 (-0.57) | -3.01 (-1.91) | tidak |

#### Keluar (b) pegang tetap 10 hari — peringkat isyarat

| Varian | PILIH n / hari beli | PILIH min % / menang % / p5 % | PILIH lebihan % (t) | PILIH Δ lawan S0 (t beza) | SAH-B lebihan % (Δ; Δp5) | SAH-22 lebihan % (Δ; Δp5) | Kawalan rawak PILIH [2.5–97.5%] (p) | Lulus |
|---|---|---|---|---|---|---|---|---|
| V00_S0 | 128333 / 2267 | 0.21 / 50.7 / -12.50 | -0.37 (-5.47) | — | -0.50 (t -8.49) | -0.51 (t -6.57) | — | rujukan |
| V01_engulf | 3644 / 1233 | 0.16 / 50.1 / -12.51 | -0.45 (-2.04) | -0.09 (-0.42) | -0.72 (-0.23; +0.22) | -0.62 (-0.11; +0.18) | [-0.63, -0.11] (0.735) | GAGAL |
| V02_piercing | 822 / 448 | 1.28 / 54.1 / -11.41 | 0.40 (0.83) | +0.77 (1.62) | -0.92 (-0.42; +0.47) | -0.59 (-0.09; -0.44) | [-0.89, 0.22] (0.004) | GAGAL |
| V03_hammer | 11124 / 2038 | 0.28 / 50.8 / -12.57 | -0.23 (-1.99) | +0.13 (1.33) | -0.51 (-0.01; +0.18) | -0.44 (+0.07; +0.20) | [-0.52, -0.22] (0.040) | GAGAL |
| V04_3LS | 2003 / 1017 | -0.09 / 49.8 / -12.67 | -0.62 (-3.32) | -0.26 (-1.38) | -0.59 (-0.10; -0.66) | -0.41 (+0.09; +0.31) | [-0.73, 0.02] (0.925) | GAGAL |
| V05_HAflip | 23179 / 2176 | 0.16 / 50.4 / -12.36 | -0.46 (-5.03) | -0.09 (-1.36) | -0.57 (-0.07; +0.11) | -0.59 (-0.08; -0.09) | [-0.46, -0.28] (0.965) | GAGAL |
| V06_IBbreak | 5092 / 1625 | 0.07 / 51.4 / -12.83 | -0.50 (-3.59) | -0.13 (-1.02) | -0.63 (-0.13; -0.71) | -0.68 (-0.18; -1.16) | [-0.58, -0.13] (0.869) | GAGAL |
| V07_engulf_vol | 808 / 574 | -0.39 / 46.2 / -14.91 | -0.85 (-2.09) | -0.49 (-1.22) | -0.64 (-0.14; -1.02) | -0.63 (-0.13; -1.59) | [-0.95, 0.24] (0.940) | GAGAL |
| V08_piercing_vol | 118 / 94 | 0.19 / 55.1 / -12.25 | -0.66 (-1.01) | -0.29 (-0.45) | -1.46 (-0.96; -0.89) | 1.09 (+1.59; +5.33) | [-1.80, 1.22] (0.644) | GAGAL |
| V09_hammer_vol | 1674 / 964 | 0.04 / 49.3 / -14.98 | -0.44 (-1.50) | -0.07 (-0.26) | -0.47 (+0.02; -0.92) | -0.46 (+0.05; +0.05) | [-0.76, 0.04] (0.641) | GAGAL |
| V10_3LS_vol | 609 / 458 | -0.17 / 47.8 / -13.59 | -0.64 (-1.59) | -0.27 (-0.68) | -0.59 (-0.10; -1.53) | -0.72 (-0.22; -1.83) | [-1.00, 0.36] (0.780) | GAGAL |
| V11_IBbreak_vol | 1066 / 732 | -0.04 / 50.8 / -14.54 | -0.59 (-2.05) | -0.22 (-0.78) | -0.93 (-0.43; -3.50) | -1.33 (-0.82; -2.76) | [-0.84, 0.16] (0.811) | GAGAL |

#### Keluar (b) pegang tetap 10 hari — portfolio 8 slot × 12.5% (rank = proksi RS), CAGR % / MDD %

| Varian | PILIH | SAH-B | SAH-22 |
|---|---|---|---|
| SPY | 16.3 / -33.7 | 16.3 / -33.7 | 11.8 / -24.5 |
| V00_S0 | 8.8 / -73.7 | -4.2 / -73.8 | -35.9 / -89.2 |
| V01_engulf | -2.4 / -44.4 | -7.2 / -58.9 | -18.6 / -70.5 |
| V02_piercing | 9.8 / -27.4 | -3.3 / -39.5 | -2.7 / -35.7 |
| V03_hammer | 1.4 / -63.3 | 3.3 / -47.3 | 1.0 / -45.8 |
| V04_3LS | -5.8 / -62.0 | -4.0 / -61.4 | -10.2 / -56.6 |
| V05_HAflip | 6.9 / -64.5 | -6.6 / -84.8 | -15.0 / -56.4 |
| V06_IBbreak | -1.8 / -59.7 | -9.3 / -72.1 | -13.3 / -61.8 |
| V07_engulf_vol | -5.8 / -47.3 | -1.9 / -44.7 | -11.8 / -53.5 |
| V08_piercing_vol | 0.2 / -13.8 | -1.4 / -15.0 | 6.1 / -12.8 |
| V09_hammer_vol | 0.4 / -55.0 | -0.4 / -47.7 | -0.6 / -35.0 |
| V10_3LS_vol | -3.6 / -46.2 | -2.1 / -42.9 | -0.5 / -31.2 |
| V11_IBbreak_vol | -2.6 / -40.4 | -9.2 / -66.4 | -21.3 / -74.0 |

#### Keluar (b) pegang tetap 10 hari — semakan konvensyen enjin (satu posisi setiap saham): lebihan % (Δ lawan S0)

| Varian | PILIH n | PILIH | SAH-B | SAH-22 | Δ > 0 dalam ketiga-tiga? |
|---|---|---|---|---|---|
| V00_S0 | 24544 | -0.34 (+0.00) | -0.45 (+0.00) | -0.53 (+0.00) | — |
| V01_engulf | 3318 | -0.47 (-0.13) | -0.76 (-0.31) | -0.64 (-0.11) | tidak |
| V02_piercing | 807 | 0.39 (+0.72) | -0.91 (-0.45) | -0.57 (-0.04) | tidak |
| V03_hammer | 8102 | -0.18 (+0.16) | -0.48 (-0.03) | -0.57 (-0.04) | tidak |
| V04_3LS | 1919 | -0.66 (-0.32) | -0.61 (-0.15) | -0.41 (+0.11) | tidak |
| V05_HAflip | 15313 | -0.42 (-0.09) | -0.52 (-0.07) | -0.61 (-0.08) | tidak |
| V06_IBbreak | 4617 | -0.52 (-0.18) | -0.63 (-0.17) | -0.68 (-0.16) | tidak |
| V07_engulf_vol | 792 | -0.89 (-0.56) | -0.67 (-0.21) | -0.55 (-0.03) | tidak |
| V08_piercing_vol | 118 | -0.66 (-0.32) | -1.46 (-1.01) | 1.01 (+1.54) | tidak |
| V09_hammer_vol | 1540 | -0.42 (-0.08) | -0.50 (-0.04) | -0.51 (+0.01) | tidak |
| V10_3LS_vol | 601 | -0.82 (-0.49) | -0.57 (-0.12) | -0.78 (-0.26) | tidak |
| V11_IBbreak_vol | 1043 | -0.60 (-0.27) | -1.03 (-0.58) | -1.27 (-0.74) | tidak |

### Inferences
- Lilin tidak memilih hari yang lebih baik daripada hari S0 yang lain. Purata beza berada dalam lingkungan ±0.5 mata dengan tanda yang bertukar antara sampel. Ini sama dengan dapatan literatur AS (Marshall-Young-Rose 2006; Horton 2009; Duvinage et al. 2013) seperti yang diringkaskan dalam `research_notes/Jenis lilin dan carta alternatif/pencetus_beli.md`, dan dengan dapatan dalaman bahawa M115–M161 menghasilkan 0 GUNA.
- Kawalan rawak tidak berkelompok: cabutan memperlakukan setiap isyarat sebagai bebas, jadi selangnya lebih sempit daripada hingar sebenar apabila isyarat berkelompok pada tarikh yang sama. Itulah sebabnya V02 (10 hari, PILIH) mendapat p = 0.004 sedangkan t berkelompoknya hanya 1.62, dan keputusan itu tidak berulang dalam SAH-B mahupun SAH-22. t berkelompok ialah ukuran yang betul. p rawak hanya berguna sebagai penunjuk arah.
- Dengan 22 ujian, satu atau dua sel dijangka "menonjol" secara kebetulan. Tiada satu pun sel menghampiri t > 3 dalam PILIH.

### Gaps
- Corak lilin tidak diuji dengan ambang lain (badan 0.4/0.8×ATR, volum 2×, dan sebagainya) dan tidak dalam persediaan selain S0. Tujuannya mengelak ujian berganda, jadi keputusan ini hanya terpakai pada S0 seperti yang ditakrifkan.
- Penapis earnings tidak dipakai. Bar pembalikan yang jatuh pada hari earnings mungkin berkelakuan berbeza.

## S3. Bagaimana prestasi persediaan S0 sendiri, portfolio 8 slot dan semakan ketahanan?

### Takeaway
Persediaan asas S0 tidak mempunyai kelebihan atas SPY selepas kos. Lebihannya hampir sifar dalam PILIH dan negatif secara signifikan dalam SAH-B dan SAH-22. Portfolio 8 slot yang disusun ikut proksi RS tertinggi lebih teruk lagi, kerana ia memilih saham momentum paling ekstrem. Semakan konvensyen enjin juga tidak mengubah kesimpulan: lilin tidak menambah nilai yang bermakna.

### Cited Findings
- S0 dengan Chandelier, peringkat isyarat:
  - PILIH: min bersih +2.00%, median −2.49%, menang 42.2%, p5 −18.01%, lebihan −0.04% (t −0.31), purata pegang 37.4 hari.
  - SAH-B: lebihan −0.35% (t −3.01).
  - SAH-22: lebihan −1.15% (t −8.83).
  — [jadual.txt](/tmp/claude-0/-home-user-papertrade-claude/0793050f-2ee1-522e-9bf0-b633a13089db/scratchpad/lilin/jadual.txt)
- S0 dengan pegang 10 hari: lebihan −0.37% (t −5.47) dalam PILIH, −0.50% (t −8.49) dalam SAH-B, dan −0.51% (t −6.57) dalam SAH-22 — [jadual.txt](/tmp/claude-0/-home-user-papertrade-claude/0793050f-2ee1-522e-9bf0-b633a13089db/scratchpad/lilin/jadual.txt)
- Portfolio 8 slot × 12.5% untuk S0 dengan Chandelier, CAGR / MDD — [hasil.json](/tmp/claude-0/-home-user-papertrade-claude/0793050f-2ee1-522e-9bf0-b633a13089db/scratchpad/lilin/hasil.json):

  | Sampel | S0 | SPY |
  |---|---|---|
  | PILIH | 9.8% / −64.8% | 16.3% / −33.7% |
  | SAH-B | −3.8% / −76.8% | 16.3% / −33.7% |
  | SAH-22 | −23.8% / −72.9% | 11.8% / −24.5% |

- Tiada varian lilin yang memberi portfolio mengalahkan SPY dalam ketiga-tiga sampel. Varian terbaik PILIH ialah V05 HA (Chandelier 16.4% / −39.8%), tetapi ia jatuh ke 9.5% / −47.8% dalam SAH-B dan 4.8% / −44.1% dalam SAH-22 (lihat jadual portfolio di atas).
- Diagnostik portfolio S0 dalam SAH-22 dengan Chandelier ([diag_port.py](/tmp/claude-0/-home-user-papertrade-claude/0793050f-2ee1-522e-9bf0-b633a13089db/scratchpad/lilin/diag_port.py)):
  - Dagangan yang benar-benar dipegang: 308, dengan purata proksi RS 99.7.
  - Min pulangan −2.18%, median −9.71%, menang 29.5%, pegang 45.4 hari kalendar. Sebagai perbandingan, min semua isyarat ialah +0.25%.
  - Dengan rank rawak (20 larian), CAGR median −7.4% (julat −14.5% hingga 2.5%) dan MDD median −48.4%.
- Konvensyen enjin (satu posisi setiap saham): satu-satunya varian dengan Δ > 0 dalam ketiga-tiga sampel ialah V03 hammer dengan Chandelier, dan bezanya sangat kecil: +0.11, +0.02 dan +0.02 mata. Dengan pegang 10 hari, tiada varian yang mengalahkan S0 dalam ketiga-tiga sampel. Lihat jadual konvensyen enjin di atas.

### Inferences
- Lilin hanya boleh membantu jika persediaan asasnya mempunyai kelebihan. Di sini persediaan asas sendiri (aliran + RS ≥ 80 + tarikan balik) tidak mengalahkan SPY selepas kos dalam data 2000 saham, dan ia lebih lemah dalam 2022–2026. Dalam keadaan ini, lilin cuma memilih subset rawak daripada set yang tidak menguntungkan.
- Menyusun portfolio ikut RS tertinggi (≈ persentil 99.7) memilih saham paling panas, yang berprestasi paling buruk selepas tarikan balik (median −9.71% dalam SAH-22). Keputusan portfolio di sini lebih banyak mencerminkan pilihan rank itu daripada kesan lilin, jadi metrik peringkat isyarat lebih sesuai untuk menilai lilin.
- Kelebihan V03 hammer dalam konvensyen enjin (≤ 0.11 mata) terlalu kecil untuk mengatasi hingar atau kos, dan ia tidak lulus pada peringkat isyarat (SAH-B Δ −0.07; SAH-22 Δ −0.04).

### Gaps
- Bias survivorship (tiada saham delist) bermakna angka sebenar mungkin lebih buruk. Kesimpulan "tiada nilai tambah" tidak berubah kerana bias ini menjejaskan S0 dan varian secara serupa.
- t berkelompok bagi beza dalam konvensyen enjin tidak dikira, kerana set dagangan varian dan S0 tidak bersarang dalam konvensyen itu.
- Rank portfolio selain proksi RS (contohnya RS sederhana, atau volatiliti rendah) tidak diuji. Ia di luar skop reka bentuk.
