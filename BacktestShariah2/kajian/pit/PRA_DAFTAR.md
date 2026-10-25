# PRA-DAFTAR: Ujian semula point-in-time (PIT) — Pintu B

Ditetapkan 25 Okt 2026 dan dicommit ke cawangan `pt/pit` (pratonton, bukan `main`) SEBELUM sebarang kaedah dijalankan atas alam PIT.
Punca: audit 25 Okt 2026 (set 431 = alam penyintas dan pandang hadapan; enjin v1.2 mengira jurang bawah henti hari masuk sebagai
untung palsu; kos 0.1%/sisi tanpa gelinciran). Semua angka ialah backtest kertas; tiada order, tiada wang sebenar.

Peraturan perubahan: tiada penalaan parameter kaedah, tiada perubahan ambang atau definisi selepas keputusan dilihat. Ralat kod yang
ditemui selepas larian dibaiki dan dicatat dalam `LAPORAN.md` bahagian "Penyimpangan daripada pra-daftar" (apa, kenapa, kesan).

## 1. Soalan

Adakah mana-mana kaedah (varian aktif, PARAM asal) memberi LEBIHAN yang boleh dipercayai (a) ke atas belian rawak dengan tempoh pegang
yang sama dan (b) ke atas EW alam yang sama, apabila diuji atas alam yang dipilih ikut tarikh (bukan ikut status hari ini), dengan enjin
yang dibaiki dan kos 0.25% setiap sisi?

## 2. Data dan alam

### 2.1 Sumber
- Harga: aset Release `autotune-data-a02` repo ini (yfinance `auto_adjust=True` + lajur `faktor_split`; tarikan 2026-10-18T08:59Z;
  3260 ticker yang pernah berada dalam universe 2000 teratas A02; bar 2009-01-02 hingga 2026-10-16; QC bar A02). `SPY`/`QQQ` daripada
  `idx.parquet` aset yang sama. Muat turun: `python3 BacktestShariah2/kajian/pit/uji_pit.py muat --data DIR` (REST API GitHub).
- `tutup_mentah = close × faktor_split` (tidak dilaras split; masih dilaras dividen). `nilai = close × volume` (= nilai dagangan mentah
  × faktor dividen).
- Peta industri: `BacktestShariah2/papertrade/peta_industri.csv` (plate Moomoo, 5634 ticker); sandaran `BacktestShariah2/data/skrin/tv_us.csv`
  (TradingView). Ticker dinormalkan (`.` → `-`).

### 2.2 Had yang diketahui SEBELUM ujian (dinyatakan, bukan disembunyikan)
1. **Tiada saham delist dalam data.** Calon ticker A02 ialah senarai tersenarai nasdaqtrader 17–18 Okt 2026; 0/3260 ticker tamat sebelum
   2026-10-01. Semakan keahlian S&P 500 sejarah (`fja05680/sp500`, GitHub, MIT): 194 daripada 797 ahli sejak 2013 tiada dalam data
   (kebanyakannya diambil alih / delist; sebahagian tukar simbol). Sesi ini tidak boleh mencapai Yahoo, Stooq, Nasdaq atau EODHD
   (proksi 403); pelan FMP tidak membenarkan sejarah harga; SEC EDGAR tidak digunakan (User-Agent memerlukan e-mel pengguna; dilarang).
   Tiada sumber percuma yang boleh dicapai memberi harga saham delist 2013–2026. Maka alam ini **PIT bersyarat penyintas**: syarat masuk
   dinilai ikut tarikh, tetapi saham yang delist sebelum Okt 2026 tiada. Keputusan = HAD ATAS (bias penyintas lebih kecil daripada set 431,
   yang dipilih ikut status Shariah dan harga hari ini, tetapi tidak sifar). Enjin tetap mengendalikan delist (§4) supaya data yang lebih
   lengkap boleh dimasukkan kemudian tanpa ubah kod.
2. Universe storan A02 = ticker yang pernah dalam 2000 teratas (median 60 hari nilai dagangan). Potongan 2000 teratas ≤ USD3.5 juta hingga
   2024, tetapi ~USD5.8 juta (2025) dan ~USD12.8 juta (2026): saham baharu 2025–2026 dengan nilai dagangan USD5–13 juta yang tidak pernah
   masuk 2000 teratas mungkin tiada.
3. Harga dilaras dividen: tutup_mentah sejarah lebih rendah daripada harga sebenar bagi pembayar dividen (syarat USD10 dan USD5 juta
   sedikit lebih ketat pada tahun awal).
4. Peta industri ialah snapshot semasa, digunakan untuk semua tarikh (industri ikut tarikh tidak tersedia).

### 2.3 Syarat layak harian (alam PIT)
Pada hari isyarat `i` (isyarat dibentuk pada tutup `i`, masuk pada buka `i+1`; hanya data ≤ `i`):
- `tutup_mentah[i] ≥ USD10` (tutup semalam berbanding hari masuk);
- median 20 sesi `nilai` (sesi `i−19..i`) ≥ USD5 juta;
- ≥ 252 bar sejarah sehingga `i` (termasuk).
Isyarat kaedah pada hari yang tidak layak dibuang (`sig = sig & layak`).

### 2.4 Saringan Shariah
(a) Aktiviti perniagaan ikut industri (garis panduan biasa S&P Shariah / AAOIFI / DJIM, ikut senarai tugasan). Dikecualikan:
- Perbankan dan kewangan konvensional: Banks - Regional, Banks - Diversified, Asset Management, Capital Markets, Credit Services,
  Mortgage Finance, Financial Conglomerates, Financial Data & Stock Exchanges, REIT - Mortgage, Shell Companies (SPAC: tunai amanah berfaedah).
- Insurans: Insurance - Property & Casualty, Insurance - Life, Insurance - Specialty, Insurance - Diversified, Insurance - Reinsurance,
  Insurance Brokers.
- Alkohol: Beverages - Brewers, Beverages - Wineries & Distilleries. Perjudian: Gambling, Resorts & Casinos. Tembakau: Tobacco.
- Senjata: Aerospace & Defense (seluruh industri; konservatif, gaya DJIM).
- Babi: senarai ticker eksplisit HRL, TSN, SFD (tiada industri khusus; saringan hasil 5% tidak dibuat).
- Hiburan dewasa: tiada industri khusus dalam peta; tiada ticker dikecualikan (had).
- Sandaran TradingView (ticker tiada dalam peta Moomoo): Major Banks, Regional Banks, Savings Banks, Finance/Rental/Leasing,
  Investment Banks/Brokers, Investment Managers, Financial Conglomerates, Life/Health Insurance, Multi-Line Insurance,
  Property/Casualty Insurance, Specialty Insurance, Insurance Brokers/Services, Investment Trusts/Mutual Funds, Beverages: Alcoholic,
  Tobacco, Casinos/Gaming, Aerospace & Defense.
- Ticker tanpa industri dalam kedua-dua peta: dikecualikan (kebanyakannya dana tertutup / kelas saham).
- Tidak dikecualikan (had diakui): media/penyiaran/pengiklanan, hotel, hiburan umum; saringan hasil tidak patuh ≤ 5%.

(b) Nisbah kewangan (hutang ÷ nilai pasaran < 33%; tunai + sekuriti berfaedah ÷ nilai pasaran < 33%) IKUT TARIKH: **tidak tersedia**
untuk alam penuh. `data/kewangan/` hanya meliputi 783 ticker yang dipilih projek hari ini (memakainya memasukkan semula bias pemilihan).
Maka dua versi:
- **Versi A (UTAMA; pintu B dinilai di sini):** syarat layak §2.3 + saringan sektor (a).
- **Versi B (kepekaan):** Versi A ∩ skrin Shariah Moomoo SEMASA `BacktestShariah2/data/harga/univ.txt` (913 ticker; status Shariah dan
  harga ≥ USD10 hari ini, termasuk nisbah semasa). Pandang hadapan; dilapor sahaja.
- **Diagnostik K431:** Versi A dihadkan kepada 431 ticker set asal (`data_mentah/dataset_S1–S4.csv`) — mengasingkan kesan alam daripada
  kesan tempoh/enjin. Dilapor sahaja.

### 2.5 Tempoh
- Kemasukan 2013-01-02 hingga 2026-10-16 (hujung data). Data dimuat sejak 2010-01-01 untuk pemanasan (≥ 750 bar sebelum 2013;
  PERLU_BAR maksimum modul = 482). Dagangan yang masuk sebelum 2013 tidak dikira (tetapi menyekat isyarat ticker sama seperti v1.2).
- Merangkumi pasaran lemah 2015–16, 2018Q4, 2020 (COVID) dan pasaran beruang 2022.
- Subtempoh dilapor: 2013–2018 (kaedah tidak pernah direka atas tempoh ini) dan 2019–2026.

## 3. Kaedah yang diuji
- Semua 134 modul `BacktestShariah2/kod/kaedah/M*.py` (dibaca sahaja). Varian aktif = `VARIAN` modul = `varian_kod`
  `standard/katalog_kaedah.json` (cara `standard/registry_aktif.py`). PARAM asal, TMAX/WARM/henti asal kaedah.
- **PLAYBOOK** (kaedah tambahan; `kajian/pit/playbook.py`), satu varian. Isyarat hari `i` jika SEMUA benar:
  1. RS 80–94: skor IBD `0.4·r63 + 0.2·r(63→126) + 0.2·r(126→189) + 0.2·r(189→252)` (formula `standard/rs_pasaran.py`, harga tutup
     data), persentil 1–99 antara SEMUA ticker data A02 (bukan Shariah sahaja) dengan tutup_mentah ≥ USD5 dan ≥ 253 bar pada hari itu;
  2. Trend Template 6 syarat harga (S1–S6 `kod/kaedah/M74.py`): tutup > SMA150 dan > SMA200; SMA150 > SMA200; SMA200 > SMA200 21 sesi
     lalu; SMA50 > SMA150 dan > SMA200; tutup > SMA50; tutup ≥ 1.30 × rendah 252 sesi;
  3. tutup ≥ 0.85 × tinggi 252 sesi (≤ 15% dari tinggi 52 minggu);
  4. ATR14 (purata mudah TR, `enjin.atr`) ÷ tutup ≤ 6%.
  Masuk buka esok; tiada henti dan sasaran; keluar pada tutup apabila hari pegang = 21 (TMAX 21); rank = skor RS. Peraturan berasaskan
  keadaan (isyarat setiap hari syarat benar; enjin tidak bertindih ticker sama).
- Kaedah tambahan kemudian (cth. M168, dikod agen lain): `python3 BacktestShariah2/kajian/pit/uji_pit.py jalan --kaedah M168` (atau
  `--modul FAIL.py`) — peraturan sama; N DSR bertambah satu setiap kaedah.
- Keutamaan komputasi: 75 kaedah swing (`data/analisis/papan.json` swing = benar; purata pegang backtest 3–30 hari) + PLAYBOOK dahulu,
  kemudian 59 lain. Yang tidak sempat disenaraikan dalam laporan.

## 4. Enjin kajian v1.3 (`kajian/pit/enjin_v13.py`)
Salinan `kod/enjin.py` v1.2 (beku, tidak diubah) dengan pembaikan berlabel sahaja:
- **[B1] Jurang hari masuk:** jika buka hari masuk ≤ henti, keluar pada buka itu (sebab `henti`). v1.2 hanya menyemak rendah ≤ henti dan
  keluar pada paras henti walaupun buka di bawahnya (untung palsu).
- **[B2] Kos 0.25% setiap sisi** (formula sama `x/e·(1−k)/(1+k) − 1`).
- **[B3] Delist:** posisi yang masih terbuka pada bar terakhir ticker yang tamat sebelum tarikh akhir data → keluar pada tutup terakhir
  (sebab `delist`). Posisi terbuka pada tarikh akhir data → `hujung` (dinilai pada tutup akhir).
- **[B4] Tetingkap** `mula`/`akhir` sebagai parameter (bukan START tetap 2019-11-01); `portfolio` memulangkan juga senarai dagangan yang
  benar-benar diambil (metrik dagangan atas dagangan portfolio dan atas semua isyarat).
- **[B5] Jenis harga keluar** direkod (`buka` / `intrahari` / `tutup`) untuk penanda aras rawak.
- Tiada perubahan lain: 8 slot × 12.5%, rank tertinggi dahulu, satu posisi setiap ticker, posisi yang keluar pada hari masuk ditutup pada
  hari itu, sasaran tidak disemak pada hari masuk, `exitc` → keluar buka esok, TMAX → tutup.
- Ujian unit: dengan kos 0.1% dan data tanpa jurang hari masuk, v1.3 = v1.2 tepat (dagangan dan keluk ekuiti).

## 5. Penanda aras
- **Rawak tempoh sama (20 benih, 0–19):** bagi setiap dagangan SEMUA ISYARAT (output `trades`, masuk ≥ 2013-01-02), setiap benih memilih
  seragam satu ticker daripada alam layak versi yang sama pada hari isyarat yang mempunyai bar buka pada hari masuk; beli buka hari masuk
  dan jual pada hari keluar yang sama (buka hari keluar jika kaedah keluar pada buka; selain itu tutup; tiada bar → tutup terakhir
  ≤ hari keluar). Kos sama 0.25%/sisi bagi kedua-dua kaki. Lebihan dagangan = `ret − purata 20 benih`.
- **EW alam:** purata sama berat pulangan harian tutup-ke-tutup semua saham layak (versi sama) pada tutup semalam (kelayakan dengan data
  ≤ semalam), pulangan harian dihad ±50% (konvensyen `standard/penanda_ew.py`), tanpa kos; indeks bermula 2013-01-02.
- SPY: rujukan sahaja.

## 6. Metrik (setiap kaedah, setiap versi)
- `lebihan_rawak` (purata lebihan setiap dagangan semua isyarat) dan `t_rawak` = purata ÷ SE berkelompok ikut bulan masuk (CR1:
  `SE² = G/(G−1) · Σ_g (Σ_{k∈g} (x_k − x̄))² / n²`). Juga dikira atas dagangan portfolio (dilapor).
- Portfolio 8 slot × 12.5% (enjin v1.3): `cagr`, `mdd`; `cagr_tanpa10` = CAGR apabila pulangan 10 dagangan portfolio terbaik ditetapkan
  0 (slot dan laluan pemilihan sama); `ew_cagr`; `lebihan_ew = cagr − ew_cagr`.
- **DSR** (Bailey & López de Prado 2014) atas pulangan harian portfolio tolak EW: `SR0 = √V·((1−γ)Φ⁻¹(1−1/N) + γΦ⁻¹(1−1/(N·e)))`,
  `DSR = Φ((SR − SR0)·√(T−1) / √(1 − γ3·SR + (γ4−1)/4·SR²))`; `V` = varians SR lebihan harian merentas kaedah yang diuji dalam kajian ini
  (versi A); **N = 633 (varian set 431 dalam `data/registry_M_gabung.csv`) + bilangan kaedah dalam kajian ini** (135 sekarang). Percubaan
  Optuna WFO/AUTOTUNE tidak dimasukkan (akan menjadikan N jauh lebih besar; DSR yang dilapor ialah had atas).
- Tahun demi tahun (pulangan portfolio, EW, SPY setiap tahun kalendar); rejim SPY > / < SMA200 pada hari isyarat (lebihan rawak dan t
  setiap rejim; pulangan tahunan portfolio dan EW dalam setiap rejim harian); subtempoh 2013–2018 dan 2019–2026.
- Metrik dagangan: n, kadar menang, purata, hari pegang — atas dagangan portfolio dan atas semua isyarat; sebab keluar.
- Diagnostik v1.2-setara (kos 0.1%, tanpa [B1]) atas versi A: CAGR sahaja, untuk mengukur kesan pembaikan enjin.

## 7. Pintu B (versi A sahaja)
`lulus_B = benar` jika SEMUA syarat berikut dipenuhi; `sebab_gagal` menyenaraikan kod yang gagal:
- **B0** boleh dinilai: ≥ 30 dagangan portfolio dan ≥ 24 bulan berkelompok dalam ujian rawak (jika tidak: `B0 data tidak cukup`).
- **B1** `lebihan_rawak > 0` dan `t_rawak ≥ 3` (selepas kos, SE berkelompok ikut bulan).
- **B2** `cagr > ew_cagr`.
- **B3** `dsr ≥ 0.5`.
- **B4** `cagr_tanpa10 > ew_cagr`.
- **B5** PBO ≤ 0.5 jika boleh dikira. Setiap kaedah hanya mempunyai satu varian beku dalam kajian ini, jadi PBO setiap kaedah TIDAK
  boleh dikira (`pbo = null`; syarat tidak menggagalkan). PBO proses pemilihan "pilih kaedah terbaik" dikira sekali (CSCV, 16 blok
  bersebelahan, Sharpe pulangan lebihan harian versi A merentas semua kaedah) dan dilapor; jika > 0.5, laporan menyatakan bahawa memilih
  kaedah terbaik daripada set ini berlebihan suai.
Versi B, K431 dan v1.2-setara tidak mengubah `lulus_B`.

## 8. Output
- `BacktestShariah2/data/analisis/ujian_pit.json`: `{"dibina", "pra_daftar", "alam": {...ringkas}, "kaedah": {id: {lulus_B, lebihan_rawak,
  t_rawak, lebihan_ew, cagr, mdd, cagr_tanpa10, ew_cagr, dsr, n_dagangan, sebab_gagal, ...}}}` (medan tambahan: versi B, K431, v1.2,
  tahunan, rejim, subtempoh, rujukan registry 431).
- `BacktestShariah2/kajian/pit/LAPORAN.md` (dijana skrip; BM; perbandingan dengan set 431).
- Data harga mentah kekal di luar repo (direktori `--data`); repo hanya menerima ringkasan dan senarai alam kecil (< 5 MB).
