# KAJIAN_M_N_SATU_PER_SATU — analisa berstruktur kaedah M dan N, langkah demi langkah (12 Nov 2026)

> **Status keputusan (kad skor, harga 2026-11-11):** TERBUKTI 0 · CALON 0 · BELUM CUKUP 223 · GAGAL 0 · NEGATIF 0. Rejim QQQ OFF sejak 2026-10-16. Hanya **TERBUKTI** layak untuk wang sebenar (`laporan/KAD_SKOR.md`); nombor dalam laporan ini BUKAN keputusan dan tidak boleh dibaca sebagai pangkat untuk wang sebenar.

Permintaan pengguna 12 Nov 2026: nilai SEMUA kaedah M dan N dalam papertrade satu per satu (masuk, pegang, keluar),
susun datanya, dan cari yang terbaik, **secara berstruktur, langkah demi langkah**. Keputusan pengguna pada hari yang
sama: analisa dulu (tiada Nxx baharu didaftar) · data langsung + backtest sedia ada (tiada backtest baharu) · biar data
tentukan tempoh pegang · simpan dalam repo · kaedah M dan N sahaja · semua langkah dijalankan terus · tiada skill
baharu (guna skill yang sudah dipasang: `validate-data`, `residual-edge-analyzer`, `backtest-expert`).

Ini **maklumat, bukan keputusan**. Tapis langkah 11 ditulis selepas angka kad skor dilihat, jadi ia bukan pradaftar.

## Jawapan ringkas

1. **Tiada kaedah yang untungnya boleh dibezakan daripada nasib.** Corong langkah 11: 223 kaedah → **4 Mxx** lulus
   semua tapis (`M142`, `M133`, `M146`, `M80`) → **2** yang masih boleh mencapai TERBUKTI (`M142`, `M80`).
2. **Semua 94 Nxx terlalu awal (6 hari beli).** Tanda awal yang baik: 10 kombinasi berpangkat backtest tertinggi
   memberi purata +1.96 % langsung (9 daripada 10 positif) lawan +0.25 % bagi semua 94.
3. **Masuk:** tiada isyarat terbukti. Mendahului: pecahan momentum (Mxx) dan terlebih jual / gap besar (`N19`, `N75`,
   `N73`, `N124`).
4. **Pegang:** tiada tempoh pendek yang untung secara purata. Atas hari beli yang sama: −0.08 % (1 sesi), −0.05 % (3),
   +0.06 % (5), −0.78 % (10). Dalam backtest untung datang selepas 20–60 hari.
5. **Keluar:** bergantung pada pasaran. "Biar lari" mendahului Nxx (backtest dan langsung); henti kaedah melindungi
   Mxx semasa pasaran turun.
6. **Dua amaran data:** purata "sudah dijual sahaja" mengelirukan (langkah 5), dan satu saham tidak cair (`TANH`,
   purata +135 %) menaikkan angka beberapa Nxx (langkah 1 dan 6).

**Cadangan: jangan daftar Nxx atau gabungan baharu sekarang.** Semua yang mendahului sudah dijejak.

## Peta langkah

| Langkah | Soalan | Hasil satu baris | Fail dalam `analisa_mn/hasil/` |
|---|---|---|---|
| 1 Data | Bolehkah data dipercayai? | Lulus; sepadan kad skor (36,292 posisi). Satu saham tidak cair ditanda | `L01_data.json` |
| 2 Kad kaedah | Apa keadaan setiap kaedah? | 4 PANTAU · 63 CAMPUR · 22 LEMAH · 10 STRUKTUR GAGAL · 124 TERLALU AWAL | `L02_SEMUA_KAEDAH.md`, `L02_kaedah.csv` |
| 3 Masuk | Adakah kaedah memilih saham lebih baik? | 70 daripada 101 Mxx positif, tetapi hanya 40 pada kedua-dua separuh | `L03_masuk.csv`, `L03_masuk_nxx.csv` |
| 4 Pegang | Berapa lama patut dipegang? | Tiada tempoh 1–15 sesi yang untung secara purata | `L04_*.csv` |
| 5 Keluar | Cara keluar mana lebih baik? | Nxx: biar lari. Mxx: keluar kaedah mengatasi Chandelier dalam pasaran turun | `L05_*` |
| 6 Risiko | Berapa teruk rugi boleh jadi? | Tiada backtest Mxx dengan MDD dalam −10 % (terbaik −17 %) | `L06_risiko.csv`, `L06_kecairan.csv` |
| 7 Pasaran lawan kaedah | Untung datang daripada kaedah atau pasaran? | 74 % pergerakan harian kaedah = pergerakan kolam; sampel belum cukup | `L07_pasaran_lawan_kaedah.csv` |
| 8 Kualiti backtest | Bolehkah backtest dipercayai? | 0 daripada 129 Mxx layak: slippage belum diuji tekanan | `L08_kualiti_backtest.csv` |
| 9 Kombinasi | Gabungan mana yang terbaik? | Nxx: pangkat backtest selari dengan langsung. Pasangan Mxx: tidak bertahan | `L09_*` |
| 10 Kebolehpercayaan | Adakah "terbaik" kekal terbaik? | Tidak (korelasi pangkat −0.08 hingga +0.07) | `L10_*` |
| 11 Corong | Apa yang tinggal? | 129 Mxx → 4; 94 Nxx → 0 | `L11_*` |

## Langkah 1 — Data dan semakan kualiti

**Soalan:** bolehkah data dipercayai sebelum apa-apa dikira? **Cara:** senarai semak skill `validate-data`.

| Semakan | Hasil |
|---|---|
| Posisi Lejar semua / langsung | 72,006 / **36,292** (sama dengan kad skor) |
| Tidak dikira | 35,700 posisi isian bina semula, 14 posisi data dikuarantin |
| Kaedah | 223 (129 Mxx, 94 Nxx); 890 saham unik |
| Pendua (kaedah, saham, hari beli) | 0 |
| Harga beli tidak sah / pulangan kosong | 0 / 0 |
| Jangkaan dikira semula lawan kad skor | beza maksimum 0.005 mata (pembundaran) |
| Mxx | 25,776 posisi, 19 hari beli (16 Okt – 11 Nov) |
| Nxx | 10,516 posisi, **6 hari beli** (4 – 11 Nov) |
| Rejim hari beli | ON 1, OFF 18 |
| Masih terbuka | 54 % posisi (ditanda ke pasaran) |
| Semakan tangan | pulangan 5 sesi satu posisi (`M142` SIG) dikira daripada bar mentah: sepadan (−2.20 %) |

**Tanda merah:** 32 posisi mencatat lebih +60 %, dalam empat saham. Tiga cair (`APP`, `AXGN`, `XERS`). Satu tidak:
**`TANH`**, 25 posisi (22 daripadanya Nxx), purata **+135 %**, nilai dagangan median kira-kira USD 0.7 juta sehari.
Saham begini tidak boleh dibeli dengan wang sebenar (had USD 10 juta, `kajian/FABLE_CADANGAN.md` §2). 15.6 % posisi
langsung berada dalam saham di bawah had itu. Kesannya diukur dalam langkah 6.

## Langkah 2 — Kad setiap kaedah

**Soalan:** apa keadaan setiap kaedah, satu per satu? **Hasil:** `L02_SEMUA_KAEDAH.md` (ringkas) dan `L02_kaedah.csv`
(semua lajur, termasuk teks masuk / pegang / keluar / henti).

| Kelas | Syarat | Mxx | Nxx |
|---|---|---|---|
| PANTAU | lulus semua tapis langkah 11 | 4 | 0 |
| CAMPUR | cukup data, gagal sekurang-kurangnya satu tapis | 63 | 0 |
| LEMAH | jangkaan ≤ 0 **dan** lift 5 sesi ≤ 0 | 22 | 0 |
| STRUKTUR GAGAL | henti pada hari beli ≥ 20 % posisi (G4 pasti gagal) | 10 | 0 |
| TERLALU AWAL | < 30 posisi atau < 10 hari beli | 30 | 94 |

Daripada 184 kaedah dengan ≥ 30 posisi: 79 berjangkaan positif, **0** dengan had bawah selang 95 % melebihi sifar,
22 masih positif selepas 5 % posisi terbaik dibuang. Median jangkaan: Mxx −0.35 %, Nxx −0.01 %.

## Langkah 3 — Masuk

**Soalan:** adakah kaedah memilih saham yang lebih baik daripada saham lain yang dibeli pada hari sama? **Cara:**
pulangan 5 sesi tolak purata saham lain pada hari dan tahap turun-naik sama ("lift"), tanpa mengira peraturan keluar.

- **Mxx** (101 kaedah dengan ≥ 30 saham-hari): 70 mempunyai lift positif, median +0.40 mata. Hanya **40** positif
  pada kedua-dua separuh hari beli.
- **Antara teratas ikut lift 5 sesi:** `M01` +2.95 (tetapi −1.80 pada 10 sesi), `M32` +2.78 (separuh kedua −3.53),
  `M158` +2.27, `M146` +2.12, `M117` +2.09. Dua yang pertama tidak konsisten (senarai penuh `L03_masuk.csv`).
- **Nxx:** lift 5 sesi wujud untuk 2 hari beli sahaja. Ikut jangkaan langsung, isyarat teratas ialah `N19` (di bawah
  jalur BB + RSI < 30) +4.61 %, `N124` (gap 8–10 %) +2.86 %, `N75` (RSI14 < 40) +2.05 %, `N64`, `N73`.
- **Backtest lawan langsung (Nxx):** korelasi pangkat +0.52 merentas 45 isyarat masuk (p 0.0003). Diukur dengan lift
  3 sesi sahaja: +0.26 (p 0.08).

**Bacaan:** sebagai kumpulan, Mxx memilih sedikit lebih baik daripada rawak (langkah 10), tetapi kaedah mana yang
terbaik tidak stabil. Nxx selari dengan backtest, dalam 6 hari satu lantunan pasaran.

## Langkah 4 — Pegang

**Soalan:** berapa lama patut dipegang? **Cara:** beli pada buka → tutup sesi ke-h, tanpa peraturan keluar.

| Pegang | Semua hari beli yang ada | Hari beli | SPUS tingkap sama | **Kohort sama (10 hari beli, 5,151 saham-hari)** | Untung |
|---|---|---|---|---|---|
| 1 sesi | −0.31 % | 19 | −0.13 % | **−0.08 %** | 47 % |
| 3 sesi | −0.19 % | 17 | −0.58 % | **−0.05 %** | 50 % |
| 5 sesi | −0.58 % | 15 | −1.34 % | **+0.06 %** | 54 % |
| 10 sesi | −0.78 % | 10 | −2.63 % | **−0.78 %** | 50 % |
| 15 sesi | −1.15 % | 5 | −4.21 % | – | – |

- Lajur "kohort sama" ialah bandingan yang adil antara tempoh: saham-hari yang sama pada setiap tempoh. Tiada tempoh
  yang untung secara bermakna.
- **Hari beli lebih menentukan daripada kaedah:** pulangan 5 sesi kolam ikut hari beli berjulat −3.43 % hingga
  +1.73 % (SD 1.82 mata); beza antara kaedah pada hari sama lebih kecil (SD 1.36 mata).
- Hanya **23 daripada 99** Mxx untung pada ketiga-tiga tempoh 3, 5 dan 10 sesi.
- **Backtest Mxx (129 kaedah), median pulangan purata:** +0.30 % (5 hari), +0.80 % (10), +1.80 % (20), +5.60 % (60).
  Bagi semua 129 kaedah, 60 hari lebih tinggi daripada 20 hari.

**Bacaan:** data langsung tidak menyokong pegangan pendek; backtest menunjukkan untung membesar dengan masa. Ufuk 20
sesi belum wujud dalam data langsung.

## Langkah 5 — Keluar

**Soalan:** bagaimana posisi ditutup, dan cara keluar mana lebih baik atas belian yang sama?

**(a) Sebab keluar** (`L05_sebab_keluar.csv`):

| Mxx | Bahagian | Purata | | Nxx | Bahagian | Purata |
|---|---|---|---|---|---|---|
| Masih terbuka | 46 % | +4.37 % | | Masih terbuka | 73 % | +1.16 % |
| Henti | 23 % | −8.64 % | | Isyarat keluar | 27 % | −1.94 % |
| Isyarat keluar | 19 % | −2.17 % | | | | |
| Henti pada hari beli | 6 % | −3.29 % | | | | |
| Had masa | 3 % | +5.80 % | | | | |
| Sasaran | 2 % | +6.46 % | | | | |

Yang sudah ditutup kebanyakannya rugi; yang untung masih terbuka. Sebab itu **purata "sudah dijual sahaja"
mengelirukan ke dua-dua arah**. Bagi kaedah yang hanya menjual bila untung, ia nampak terlalu cantik: `N16X13` dalam
`lejar/RINGKASAN.md` menunjukkan menang 98 % dan +16.80 % atas 43 posisi dijual, tetapi 577 lagi terbuka pada −1.92 %,
jadi purata semua −0.62 % (`N75X13` +0.29 %, `N119X13` +0.25 %). **Baca jangkaan, bukan kadar menang.**

**(b) Nxx: enam cara keluar atas isyarat masuk yang sama** (`L05_keluar_nxx.csv`):

| Keluar | Peraturan | Langsung | Sudah dijual | Backtest tahan | Backtest tanpa5 | Rugi purata backtest |
|---|---|---|---|---|---|---|
| `X15` | ekori Chandelier 4×ATR14 | +1.69 % | 0 % | +7.09 % | −1.69 % | −14 % hingga −22 % |
| `X13` | jual bila RSI14 > 70 | +1.66 % | 6 % | +6.84 % | +1.97 % | −21 % hingga −24 % |
| `X14` | RSI14 silang naik 50 | +0.83 % | 8 % | +2.21 % | −1.88 % | −8 % hingga −13 % |
| `X17` | ADX14 < 20 | +0.53 % | 20 % | +3.85 % | −2.50 % | −9 % hingga −13 % |
| `X36` | dua tutup di bawah MA50 | +0.21 % | 32 % | +2.11 % | −2.78 % | −6 % hingga −15 % |
| `X16` | Supertrend berbalik | −0.20 % | 37 % | +1.50 % | −2.54 % | −6 % hingga −12 % |

**(c) Mxx: keluar kaedah (L1) lawan Chandelier tanpa henti (L2), 25,776 posisi yang sama:** purata −0.25 % lawan
−0.55 %; posisi rugi lebih 15 %: 3.1 % lawan 9.7 %; L1 lebih baik bagi 67 % kaedah.

**Bacaan:** "biar lari" mendahului dalam backtest dan dalam lantunan minggu lepas, tetapi dalam 19 hari pasaran turun
henti kaedah yang melindungi. Cara keluar terbaik berubah ikut pasaran; data langsung baru melihat satu fasa.

## Langkah 6 — Risiko

**Soalan:** berapa teruk rugi boleh jadi, dan adakah angka bergantung pada saham yang tidak boleh dibeli?

| | Mxx | Nxx |
|---|---|---|
| Posisi rugi lebih 8 % / 15 % / 25 % | 14.4 % / 3.1 % / 0.55 % | 6.6 % / 1.4 % / 0.2 % |
| Posisi terburuk | −52.5 % | −36.5 % |
| Kaedah dengan posisi terburuk di bawah −25 % | 59 daripada 104 | 19 daripada 85 |
| Kaedah yang pernah kena henti pada hari beli | 84 daripada 104 | 0 (tiada henti) |
| MDD lorong T4: median / terburuk / melebihi −10 % | −6.9 % / −23.1 % / 26 lorong | −4.4 % / −11.7 % / 3 lorong |
| MDD backtest (129 Mxx): median / terbaik / dalam −10 % | −34.6 % / −17.4 % / **0 kaedah** | tiada MDD setiap kombinasi |

**Kecairan** (`L06_kecairan.csv`; hanya saham dengan nilai dagangan ≥ USD 10 juta):

| | Semua posisi | Saham cair sahaja | Saham tidak cair |
|---|---|---|---|
| Mxx | −0.25 % | −0.15 % | −0.78 % |
| Nxx | +0.32 % | **+0.04 %** | +1.75 % |

Hampir semua untung keluarga Nxx datang daripada saham tidak cair (`TANH`). Contoh: `N40X36` +2.82 % menjadi
+0.02 %; `N53X36` +1.82 % menjadi −0.46 %. Senarai akhir langkah 11 **tidak** bergantung padanya (semak lajur
"saham cair sahaja" di sana).

**Bacaan:** tiada kaedah yang backtestnya mematuhi MDD −10 % pada pendedahan penuh. Toleransi itu hanya boleh
dicapai dengan saiz pendedahan, bukan dengan memilih kaedah.

## Langkah 7 — Pasaran lawan kaedah

**Soalan:** adakah untung harian kaedah datang daripada kaedah itu, atau sekadar pasaran? **Cara:** skill
`residual-edge-analyzer`. Buku harian setiap kaedah diregres atas kolam Lejar (asas utama) dan SPUS (asas kedua);
kedua-dua asas ditetapkan sebelum hasil dilihat.

- 118 Mxx mempunyai ≥ 15 sesi. **Status penganalisis bagi kesemuanya: `INSUFFICIENT_EVIDENCE`** (19 sesi; minimum 60).
- Median 74 % pergerakan harian kaedah diterangkan oleh kolam (beta 1.03); 33 % oleh SPUS.
- Baki kelebihan dengan t > 2: **1 kaedah** (`M146`, t 2.04); t < −2: 3 kaedah. Dengan 118 ujian, kira-kira 7
  dijangka melepasi ±2 secara kebetulan; ambang selepas pembetulan ujian berganda ialah 3.52.

**Bacaan:** belum ada kaedah yang menunjukkan kelebihan sendiri di luar pasaran. Nxx belum boleh diuji (6 sesi).

## Langkah 8 — Kualiti backtest

**Soalan:** bolehkah backtest sedia ada dipercayai? **Cara:** skill `backtest-expert` (`evaluate_backtest.py`) atas
registry set 431 varian produksi (129 Mxx, 6.9 tahun). Skor 0–100 tidak dilaporkan kerana bilangan parameter tidak
direkod; hanya keputusan dan sebab sekatan.

| Keputusan | Kaedah | Sebab |
|---|---|---|
| `VALIDATION_REQUIRED` | 126 | slippage belum diuji tekanan (enjin memakai kos 0.1 % setiap belah) |
| `REJECT` | 3 | MDD ≥ 50 % |
| `DEPLOY` | **0** | – |
| Dengan had MDD −10 % pengguna | 126 `RISK_LIMIT_EXCEEDED` + 3 `REJECT` | setiap kaedah melebihi had |

115 daripada 129 positif pada kedua-dua separuh tempoh backtest. Nxx tidak dinilai: `jejak_semua.csv` tiada MDD setiap
kombinasi.

**Bacaan:** backtest Mxx konsisten merentas masa tetapi belum diuji dengan kos yang lebih teruk, dan tiada yang
mematuhi MDD −10 %. Ini selaras dengan langkah 10: pangkat backtest Mxx tidak meramal data langsung.

## Langkah 9 — Kombinasi

**(a) Nxx, masuk × keluar** (94 kombinasi; `L09_nxx_semua_kombinasi.csv`). Sepuluh kombinasi berpangkat backtest
tertinggi: jangkaan langsung purata **+1.96 %**, 9 daripada 10 positif; semua 94: +0.25 %. Korelasi pangkat +0.53.

| Kombinasi | Posisi / dijual | Langsung | Saham cair sahaja | Pangkat backtest | Backtest tahan | Rugi purata backtest |
|---|---|---|---|---|---|---|
| `N124X15` gap 8–10 % → Chandelier | 39 / 0 | +3.79 % | +3.77 % | 1 | +16.13 % | −21.9 % |
| `N19X13` bawah BB + RSI < 30 → RSI14 > 70 | 101 / 0 | +4.61 % | +5.80 % | 2 | +11.29 % | −22.6 % |
| `N75X13` RSI14 < 40 → RSI14 > 70 | 124 / 1 | +2.24 % | +2.04 % | 3 | +7.47 % | −24.0 % |
| `N73X13` bawah jalur BB → RSI14 > 70 | 136 / 1 | +1.95 % | +2.21 % | 4 | +6.89 % | −21.8 % |

Hampir tiada yang sudah dijual: angka ini ialah posisi terbuka dalam satu lantunan. Lift 3 sesi `N19X13` negatif
(−0.97), jadi untungnya datang daripada memegang, bukan daripada memilih saham.

**(b) Berapa kaedah Mxx sepakat atas saham yang sama** (lift 5 sesi): 1 kaedah −0.28 · 2 kaedah −0.14 · 3–4 kaedah
+0.33 · 5–9 kaedah −0.02 · 10+ kaedah +1.49 (t 1.67). Tetapi 94 daripada 269 saham-hari "10+" ialah satu hari
(16 Okt); tanpa hari itu +0.37 (t 0.71).

**(c) Semua pasangan Mxx:** 8,128 pasangan, 395 dengan ≥ 30 saham-hari bersama. 20 pasangan terbaik pada separuh
pertama: +3.79 di situ, **+0.42 pada separuh kedua** (semua pasangan +0.11). Korelasi pangkat −0.07. Tiada pasangan
dipilih atau disenaraikan.

**Bacaan:** satu-satunya kombinasi yang konsisten antara backtest dan data langsung ialah "masuk terlebih jual atau
gap besar × keluar biar lari" dalam keluarga Nxx, dan ia terlalu awal. Menggabungkan kaedah Mxx tidak menambah apa-apa.

## Langkah 10 — Kebolehpercayaan

**(a) Kestabilan.** Hari beli dipecah rawak kepada dua separuh (500 kali); kaedah disusun pada separuh pertama dan
dibaca pada separuh kedua:

| Ukuran (Mxx) | Korelasi pangkat [5 %, 95 %] | 10 teratas: lebihan pada separuh kedua |
|---|---|---|
| Lift 3 sesi | −0.08 [−0.23, +0.07] | −0.17 mata [−0.82, +0.33] |
| Lift 5 sesi | +0.07 [−0.12, +0.24] | +0.02 mata [−0.75, +0.77] |
| Lift 10 sesi | +0.15 [+0.01, +0.29] | +0.32 mata [−0.84, +1.34] (tingkap bertindih; condong ke atas) |

**(b) Plasebo.** 32 daripada 101 Mxx lulus tapis ufuk tetap. Jika pulangan dikocok antara saham pada hari dan ATR
sama: purata 15.6 [9, 24]. Tanpa hari beli pertama: 24 lawan 15.1 [9, 23], p 0.03. Tanda lemah bahawa Mxx sebagai
kumpulan memilih sedikit lebih baik daripada rawak; ujian yang sah ialah G3 kad skor.

**(c) Backtest lawan langsung.** Mxx: −0.05 (jangkaan), +0.12 (lift); tidak signifikan. Nxx: +0.52 (langkah 3).

## Langkah 11 — Corong dan senarai akhir

Tapis dipakai satu demi satu (`L11_corong.csv`):

| Tahap | Tapis | Mxx | Nxx |
|---|---|---|---|
| 0 | Semua kaedah | 129 | 94 |
| 1 | Cukup data: ≥ 30 posisi dan ≥ 10 hari beli | 99 | 0 |
| 2 | Bukan struktur gagal (henti hari beli < 20 % posisi) | 89 | – |
| 3 | Jangkaan > 0 | 34 | – |
| 4 | tanpa5 > 0 | 6 | – |
| 5 | Lift 5 dan 10 sesi > 0 | 5 | – |
| 6 | Lift 5 sesi > 0 pada kedua-dua separuh | 4 | – |
| 7 | Backtest > 0 | **4** | – |
| 8 | Maklumat: sifar henti pada hari beli (gate G4) | **2** | – |

**Senarai pantau Mxx** (`L11_senarai_pantau.csv`; BUKAN terbukti):

| | `M142` Pecahan volum dari dasar | `M133` Bull Hook | `M146` 3-Bar Momentum | `M80` Radge MAC |
|---|---|---|---|---|
| **Masuk** | pecah tinggi 20 hari > 3 % dengan volum ≥ 2×, di atas MA250 naik; beli selepas hari turun pertama yang kekal di atas paras pecah | hari "hook", esoknya tutup > buka + regangan | 3 lilin hijau makin laju, tinggi baharu 20 hari | rendah di atas SMA10-tinggi tepat 5 hari |
| **Pegang** | tiada had | maksimum 21 sesi | tiada had | tiada had |
| **Keluar** | Chandelier 4×ATR22 | tutup < SMA50 | tutup < SMA50 | tinggi di bawah SMA8-rendah 5 hari |
| **Henti** | 3.5×ATR14 (maks 15 %) | 2×ATR14 (maks 15 %) | tetap 6 % | 3×ATR14 |
| Posisi / dijual / hari beli | 45 / 5 / 14 | 49 / 23 / 13 | 77 / 30 / 17 | 273 / 56 / 19 |
| Jangkaan / tanpa5 | +3.31 % / +1.88 % | +1.80 % / +0.49 % | +1.70 % / +0.68 % | +1.34 % / +0.07 % |
| Saham cair sahaja | +3.31 % / +1.91 % | +2.37 % / +0.90 % | +1.42 % / +0.18 % | +1.53 % / +0.26 % |
| Pegang 3 / 5 / 10 sesi | +1.94 / +1.57 / +0.52 | +2.29 / +1.46 / +5.94 | +1.77 / +2.09 / +1.69 | +0.28 / +0.47 / +3.21 |
| Lift 5 / 10 sesi (saham-hari) | +4.10 / +2.54 (26 / 8) | +1.78 / +5.73 (38 / 23) | +2.12 / +2.41 (72 / 41) | +1.00 / +3.11 (223 / 169) |
| Rugi terburuk / posisi rugi > 15 % | −14.7 % / 0 % | −12.0 % / 0 % | −31.4 % / 1.3 % | −41.5 % / 2.9 % |
| Lorong T4: pulangan / MDD | +5.31 % / −4.8 % | +7.95 % / −4.2 % | +6.71 % / −6.2 % | −1.46 % / −7.1 % |
| Langkah 7: bahagian kolam / t kelebihan | 54 % / 0.36 | 6 % / 1.41 | 72 % / 2.04 | 66 % / 0.83 |
| Langkah 8: backtest purata / MDD | +6.85 % / −28 % | +0.68 % / −26 % | +2.66 % / −41 % | +8.91 % / −39 % |
| **Henti pada hari beli (G4 mesti 0)** | 0 | **1** | **4** | 0 |

- `M133` dan `M146` akan GAGAL G4 apabila G1 lulus; gate itu dikunci. Tinggal `M142` dan `M80`.
- `M142`: lift berdiri atas 26 dan 8 saham-hari sahaja. `M80`: lorong portfolionya negatif.
- Tiada satu pun mempunyai had bawah selang 95 % melebihi sifar, dan semua MDD backtest melebihi −10 %.

**Nxx awal** (`L11_nxx_awal.csv`; pangkat backtest ≤ 10, jangkaan dan tanpa5 langsung > 0; kelas TERLALU AWAL):
`N124X15`, `N19X13`, `N75X13`, `N73X13`, `N124X36`, `N75X15`, `N42X15`.

## Jawapan akhir: masuk, pegang, keluar

| Bahagian | Apa yang data katakan | Keyakinan |
|---|---|---|
| **Masuk** | Tiada isyarat tunggal terbukti. Mendahului: pecahan momentum (`M142`, `M133`, `M146`, `M80`); terlebih jual (`N19`, `N75`, `N73`); gap besar (`N124`) | rendah: 6–19 hari, satu fasa pasaran |
| **Pegang** | Tiada tempoh 1–15 sesi yang untung secara purata. Backtest: untung membesar hingga 60 hari | sederhana |
| **Keluar** | Pasaran naik/melantun: biar lari (RSI14 > 70 atau Chandelier). Pasaran turun: henti kaedah memotong posisi rugi besar daripada 9.7 % kepada 3.1 % | sederhana bagi arah; tiada peraturan tukar yang diuji |
| **Kombinasi** | Nxx "terlebih jual atau gap × biar lari" konsisten backtest dan langsung, tetapi terlalu awal dan rugi puratanya −22 %. Pasangan dan kaedah sepakat Mxx tidak bertahan | Nxx rendah; Mxx tinggi |

## Langkah seterusnya

1. **Sekarang: jangan daftar Nxx atau gabungan baharu.** Empat Mxx dan tujuh Nxx di atas semuanya sudah dijejak dalam
   Lejar, kad skor dan lorong T4.
2. **Titik semak 1 — awal Dis 2026** (Nxx ≥ 20 hari beli): jalankan semula skrip ini. Soalan: adakah corong memberi
   kaedah yang sama; adakah korelasi backtest–langsung Nxx kekal positif **pada saham cair**; adakah lift kumpulan
   Mxx kekal tanpa bergantung pada satu hari.
3. **Titik semak 2 — apabila G1 lulus** (≥ 10 hari beli rejim ON): ulang langkah 5 dalam rejim ON, dan langkah 7
   apabila ada ≥ 60 sesi.
4. **Hanya jika kedua-dua titik semak positif:** pradaftar **satu** gabungan bertarikh sebelum data hadapannya
   dilihat. Itu keputusan pengguna dan pengecualian baharu kepada "tiada baris MASUK Nxx baharu".
5. **Wang sebenar:** hanya apabila kad skor menanda TERBUKTI.

## Semakan kualiti analisa ini (skill `validate-data`)

**Penilaian: boleh dikongsi dengan kaveat.**

| Perangkap | Cara ditangani |
|---|---|
| Kiraan | jumlah posisi dan jangkaan sepadan dengan kad skor; satu pulangan dikira tangan |
| Bandingan tempoh tidak lengkap | langkah 4 memakai kohort hari beli yang sama |
| "Yang selamat sahaja" | langkah 5 membaca semua posisi, bukan yang dijual sahaja; alam backtest tiada saham delist (condong ke atas) |
| Nilai melampau | `tanpa5` (langkah 2, 11) dan "saham cair sahaja" (langkah 6, 11) |
| Ujian berganda | 223 kaedah dan 8,128 pasangan diuji; langkah 7 dan 10 melaporkan jangkaan kebetulan |
| Memilih selepas melihat | tapis langkah 11 bukan pradaftar; kestabilan dan plasebo langkah 10 mengukur kesannya |
| Purata kepada purata | jadual keluarga memakai purata semua posisi, kecuali di mana dinyatakan "merentas kaedah" |

Kaveat yang mesti dibawa bersama: 19 hari beli (Nxx 6) dalam satu rejim; tingkap pulangan bertindih, jadi setiap
nilai t optimistik; ukuran setiap posisi, bukan portfolio (portfolio = lorong T4 dan G6); kolam lift ialah saham yang
Lejar beli, bukan seluruh pasaran; langkah 7 di bawah sampel minimum; langkah 8 menilai metrik ringkasan registry.

## Jana semula

`python3 BacktestShariah2/kajian/analisa_mn/analisa.py` (≈ 30 saat; benih rawak ditetapkan). Skrip hanya membaca
Lejar, stor harga, `kad_skor.json`, registry dan `REVERSE/jejak_semua.csv`; ia memanggil skrip dua skill dalam
`.claude/skills/`. Setiap fail dalam `kajian/analisa_mn/hasil/` berawalan nombor langkahnya; `ringkasan.json`
mengandungi angka utama setiap langkah dan `log.txt` cetakan penuh.
