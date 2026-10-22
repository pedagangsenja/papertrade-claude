# Kolam isyarat bersama dengan ciri bar (AUTOTUNE, 2000 saham AS, 2013 – Okt 2026)

Nota ini ialah hasil pengiraan sendiri, bukan sumber web. Setiap angka dirujuk kepada skrip dan fail output. Kolam ini dibina untuk ujian veto/ranking/keluar dalam laporan [Jenis lilin dan carta alternatif](../../reports/Jenis%20lilin%20dan%20carta%20alternatif.md) (bahagian "Uji lima perkara mengikut susunan ini").

- Skrip pembina: `BacktestShariah2/kajian/lilin/bina_kolam.py`
- Skrip statistik: `BacktestShariah2/kajian/lilin/statistik_kolam.py` (output penuh: `/tmp/claude-0/-home-user-papertrade-claude/0793050f-2ee1-522e-9bf0-b633a13089db/scratchpad/lilin/statistik.md`)
- Semakan silang AUTOTUNE: `BacktestShariah2/kajian/lilin/semak_bersih.py` (output: `.../scratchpad/lilin/semak_bersih.txt`)
- Kolam: `/tmp/claude-0/-home-user-papertrade-claude/0793050f-2ee1-522e-9bf0-b633a13089db/scratchpad/lilin/kolam.parquet` (1,890,526 baris, 56 lajur, 310 MB). Cache setiap kaedah: `.../scratchpad/lilin/kaedah/<ID>.parquet`. Log larian: `.../scratchpad/lilin/log.json`.
- Larian: 946 saat (2 proses), data hingga 16 Okt 2026. Tiada fail di bawah `AUTOTUNE/`, `BacktestShariah2/kod/`, `lejar/`, `papertrade/` atau `data/` diubah. Cache numba diarahkan ke scratchpad (`NUMBA_CACHE_DIR`), kerana cache `AUTOTUNE/teras/__pycache__` dikompil sebagai pakej `teras.enjin_at` dan gagal dimuat sebagai `enjin_at`.

## Soalan 1: Kaedah asas mana yang dipilih, dan mengapa?

### Takeaway
A01 tidak melabel sebarang kaedah sebagai TINGGI atau SEDERHANA, jadi pemilihan bergantung pada status papan repo. Sebanyak 30 kaedah dipilih: 3 GUNA yang ada salinan AUTOTUNE (M30, M79, M96), M167 yang diadaptasi daripada Rangka R, dan 26 kaedah UJI KERTAS/SIMPAN berlabel RENDAH dalam A01. Tiada kaedah digugurkan kerana masa larian; yang paling lambat ialah M26 (279 s).

### Cited Findings
- AUTOTUNE A01 `kiraan_label`: TINGGI 0, SEDERHANA 0, RENDAH 70, GAGAL 64 daripada 134 kaedah. Oleh itu, kriteria "TINGGI atau SEDERHANA" memilih sifar kaedah. — [AUTOTUNE/hasil/ringkasan.json](../../../../AUTOTUNE/hasil/ringkasan.json); [AUTOTUNE/hasil/papan.json](../../../../AUTOTUNE/hasil/papan.json)
- Status papan repo (varian terbaik): GUNA 7, UJI KERTAS 31, SIMPAN 53, DITOLAK 50. Ketujuh-tujuh GUNA ialah M167, M166, M164, M96, M114, M30 dan M79. — [PAPAN_KEDUDUKAN_M.md](../../../laporan/PAPAN_KEDUDUKAN_M.md)
- Salinan AUTOTUNE hanya meliputi 134 modul hingga M161. M114, M162–M166 tiada salinan, jadi tidak dimasukkan. Selain itu, M164 memerlukan data pendapatan yang tiada dalam data AUTOTUNE. — `AUTOTUNE/kaedah/`
- Kesetaraan: 133 salinan SAMA, manakala M81 DIBAIKI, iaitu sengaja tidak sama kerana pembetulan pandang ke hadapan. M81 dikecualikan kerana syarat "lulus kesetaraan". — [AUTOTUNE/kaedah/KESETARAAN.md](../../../../AUTOTUNE/kaedah/KESETARAAN.md)
- Peraturan pemilihan (`KAEDAH` dalam `bina_kolam.py`):
  - (a) GUNA dengan salinan SAMA: M30, M79, M96.
  - (b) M167 V2 "V1 kunci OVN252", iaitu varian GUNA. Ia dibina semula daripada [WFO/kaedah_baru/step2_M167.py](../../../../WFO/kaedah_baru/step2_M167.py) dan [_rangka_r.py](../../../../WFO/kaedah_baru/_rangka_r.py).
  - (c) Kaedah UJI KERTAS atau SIMPAN berlabel RENDAH dalam A01 (CAGR OOS-A > 0), disusun ikut min(CAGR OOS-A, CAGR OOS-B), hingga jumlahnya 30: M91, M152, M135, M130, M134, M41, M146, M124, M20, M95, M48, M04, M26, M67, M137, M93, M10, M129, M139, M118, M142, M149, M05, M78, M33, M89.
  - UJI KERTAS dimasukkan walaupun arahan hanya menyebut GUNA/SIMPAN, kerana dalam hierarki repo UJI KERTAS berada di atas SIMPAN (GUNA > UJI KERTAS > SIMPAN > DITOLAK).
  - Calon RENDAH seterusnya yang tidak dimasukkan kerana had 30: M132, M74, M161, M133, M107, M158, M144, M122, M45, M123, M105, M119, M29, M99, M80, M90, M111, M46, M15.
- Semua kaedah memakai PARAM asal (`sedia(fr, idx, dict(m.PARAM))`) tanpa penalaan.
- Masa setiap kaedah (sedia + dagangan, atas 3,222 ticker × 2011–2026): median kira-kira 45 s, paling lama M26 279 s dan M124 148 s. Tiada kaedah dilangkau. — `log.json`

### Inferences
- Kolam ini mewakili isyarat yang "tidak ditolak" dalam repo dan mempunyai CAGR OOS-A positif, bukan kaedah yang sudah terbukti di 2000 saham. Ujian ciri atas kolam ini menyoal sama ada ciri bar boleh memulihkan kaedah yang lemah atau sederhana. Kolam ini tidak menyoal ciri bar atas kaedah yang sudah kuat.
- M30, M79 dan M96 berstatus GUNA dalam repo, tetapi M79 dan M96 berlabel GAGAL dalam A01. Kehadirannya memberi kontras yang berguna.

### Gaps
- M114 (RS Peneraju Pasaran Naik), M166 dan M164 tidak dapat dimasukkan tanpa salinan AUTOTUNE. M114 V4 ialah rujukan langsung bagi ujian ranking 3/4, jadi perlu dibina berasingan, contohnya melalui Rangka R seperti M167.

## Soalan 2: Bagaimana kolam dibina, dan apa formula setiap lajur?

### Takeaway
Setiap baris ialah satu isyarat yang sah universe: kaedah × ticker × hari isyarat ≥ 2013-01-02. Setiap baris membawa hasil dagangan enjin_at, pulangan hadapan mentah, SPY tempoh sama, dan 30 ciri bar pada tutup hari isyarat. Ciri hanya memakai bar ≤ t. Lajur hadapan dinamakan `fwd*`, `spy*`, `mfe20` dan `gap_masuk`, dan tidak boleh digunakan sebagai ciri.

### Cited Findings
- **Data**: `teras/data.py muat('2011-01-01', hujung, 'AB')`, iaitu 3,222 ticker yang pernah berada dalam universe 2011–2026. Harga yfinance `auto_adjust=True`. 2011–2012 menjadi pemanasan. — [AUTOTUNE/SPEC.md](../../../../AUTOTUNE/SPEC.md) §1; `bina_kolam.py main()`
- **Gating universe**: isyarat sah hanya jika `data.topeng(g, t, univ, 'AB')` benar (ticker dalam senarai 2000 bulan itu), tarikh isyarat ≥ 2013-01-01, indeks bar ≥ WARM kaedah, dan bukan bar terakhir. `kumpulan` = A/B ikut md5(ticker) % 2 (SPEC §1).
- **Dagangan** (enjin_at, SPEC §3): masuk pada buka t+1; gap hari masuk (buka ≤ henti → keluar pada buka); kos setiap sisi 0.1% + slippage ikut median nilai dagangan 20 hari (0.05% / 0.10% / 0.25%); had 60 hari (`min(TMAX, 60)`); keluar ikut henti, sasaran atau exitc kaedah. Posisi yang masih terbuka pada 16 Okt 2026 ditutup pada tutup bar terakhir (`exit_reason='hujung'`, 0.44% baris).
- **Semua isyarat, bukan hanya 8 slot**:
  - `laluan = 1` ialah dagangan enjin biasa (`dagangan_enjin = True`). Isyarat yang jatuh semasa posisi ticker sama masih dibuka dilangkau oleh enjin.
  - Isyarat yang dilangkau dijalankan semula sebagai laluan 2, 3, ... dengan keluar sendiri. Untuk setiap kaedah, laluan 1 disahkan sama dengan `Susun.dagangan` biasa (`semak_laluan1_sama = true` bagi 30/30 kaedah).
  - Kaedah yang exitc-nya ditanda oleh replika laluan enjin (M20, M26, M78 dalam kolam; M41 tiada isyarat bertindih) diberi `trade_ret = NaN` bagi laluan ≥ 2: 117,644 baris (M20 85,616; M78 30,156; M26 1,872). Lajur `ikut_laluan = True` menanda kaedah ini.
  - M167 diberi keluar sendiri sebenar bagi setiap isyarat (`_m167_satu`). Fungsi itu sama dengan laluan 1 enjin bagi semua 23,821 dagangan (`m167_keluar_sendiri_sama_laluan1 = true`).
- **`pegang8`**: dagangan laluan 1 yang dipegang portfolio 8 slot × 12.5% (`Pasaran.lengkung(pegang=True)`) bagi kumpulannya sendiri (A atau B), 2013-01-01 hingga hujung, susunan ikut `rank_value`. Bilangannya 63,544 baris.
- **M167 di 2000 saham**:
  - Kunci dan rank: OVN252 = Σ ln(O_t/C_{t−1}) 252 hari.
  - Kolam: persentil OVN252 ≥ 0.90, dikira antara ahli universe A+B hari itu. Dalam set 431 asal, persentil dikira antara semua 431 saham.
  - Penapis: purata volum 20 hari ≥ 100K dan SPY > SMA200.
  - Henti 0.88 × buka masuk. Keluar apabila tutup < maks tutup sejak masuk − 3 × ATR22 atau tutup < henti, pada buka esok. Had 60 hari ditambah supaya selaras dengan enjin_at.
- **Pulangan hadapan** (mentah, tanpa kos):
  - `fwdh = C_{t+h} / O_{t+1} − 1` bagi h ∈ {5, 10, 20} bar saham itu.
  - `spyh = SPY_C(tarikh t+h) / SPY_O(tarikh t+1) − 1`, dengan SPY di-reindex ke tarikh saham (ffill).
  - `mfe20 = maks(H_{t+1..t+20}) / O_{t+1} − 1`.
  - `gap_masuk = O_{t+1} / C_t − 1` ialah hasil, bukan ciri.
- **Ciri pada tutup t** (`ciri_saham`; ATR14 = purata mudah TR 14 hari hingga t−1, sama takrif dengan `enjin.atr`):
  - MAX: `ret1 = C_t/C_{t−1} − 1`; `max20 = maks ret1 atas t−19..t`; `gap_atr = (O_t − C_{t−1}) / ATR14_{t−1}`; `julat_atr = (H_t − L_t) / ATR14_{t−1}`; `atas1pct_1t = 1` jika ret1_t ≥ kuantil 0.99 ret1 atas t−251..t (min 200 bar).
  - Tambahan untuk ujian 1: `rcc_srs60 = ln(C_t/C_{t−1}) / σRS60_{t−1}`, dengan σRS60 = √(purata 60 hari [ln(H/C)·ln(H/O) + ln(L/C)·ln(L/O)]), iaitu Rogers-Satchell. `gap_atr_pctl252` = persentil (method='max') gap_atr_t dalam 252 hari sendiri. `on5` = Σ ln(O/C_{−1}) 5 hari.
  - Semalaman/intrahari: `onN = Σ ln(O_s/C_{s−1})` dan `idN = Σ ln(C_s/O_s)` atas N hari berakhir t, N ∈ {20, 60}; `id_shareN = idN / (|onN| + |idN|)`; `on252` (kunci M167).
  - Volum: `vol_rel50 = V_t / median(V_{t−50..t−1})`; `vol_pctl50` = bahagian V_{t−49..t} ≤ V_t (1 = tertinggi 50 hari); `naik_vol90 = (C_t > C_{t−1}) & vol_pctl50 ≥ 0.9`; `hijau_vol90 = (C_t > O_t) & vol_pctl50 ≥ 0.9`, iaitu takrif ujian 4 dalam laporan.
  - 52 minggu: `h52 = C_t / maks(H_{t−251..t})` (min 200 bar). `h52_industri` = median h52 ahli universe A+B hari itu dalam industri Moomoo yang sama, termasuk saham itu sendiri; NaN jika ahli < 3. `n_industri` = bilangan ahli.
  - Bentuk bar (NaN jika H = L): `ibs = (C−L)/(H−L)`; `badan_julat = |C−O|/(H−L)`; `badan_arah = (C−O)/(H−L)`; `bayang_atas = (H − maks(O,C))/(H−L)`; `bayang_bawah = (min(O,C) − L)/(H−L)`.
  - Heikin-Ashi: HA_C = (O+H+L+C)/4; HA_O_s = (HA_O_{s−1} + HA_C_{s−1})/2, dengan benih (O+C)/2 pada bar pertama data 2011. `ha_naik_berturut` = bilangan bar HA_C > HA_O berturut-turut yang berakhir pada t (0 jika bar t turun).
  - RS proksi: `rs6_pct` dan `rs12_pct` = persentil keratan rentas `C_t/C_{t−126} − 1` dan `C_t/C_{t−252} − 1` antara ahli universe A+B yang ada nilai pada hari itu.
  - Lain-lain: `medv20` = median 20 hari (C × V); `kos` = kos setiap sisi enjin.
- **Peta industri**: [BacktestShariah2/papertrade/peta_industri.csv](../../../papertrade/peta_industri.csv) (Moomoo, 5,634 ticker) meliputi 3,078/3,212 ticker universe 2013+ dan 1,915/2,000 ticker universe Okt 2026. Liputannya 96.1% baris kolam (144 industri), dan `h52_industri` ada bagi 94.6% baris. `kajian/industri_fmp/` hanya mengandungi siri peringkat industri tanpa peta ticker, manakala `data/kumpulan/` dan `papertrade/sektor.csv` ialah gred kumpulan semasa, jadi kedua-duanya tidak digunakan.
- **Lajur kolam**:
  - Pengenalan: `method, ticker, signal_date, entry_date, kumpulan, pos`.
  - Dagangan: `laluan, trade_ret, hold_days, mfe_dagangan, kos, rank_value, pegang8, exit_date, exit_reason, dagangan_enjin, ikut_laluan`.
  - Ciri: ciri di atas serta `industri, h52_industri, n_industri, rs6_pct, rs12_pct`.
  - Hadapan: `gap_masuk, fwd5/10/20, spy5/10/20, mfe20`.
  - `pos` ialah indeks dalaman bagi `Asas` dengan susunan `muat('2011-01-01', …)`. Kunci luaran yang disarankan ialah (`ticker`, `signal_date`).
- **Semakan silang dengan A01 "ujian bersih"** (PARAM asal, A+B, 2013–2018; `semak_bersih.py`):
  - CAGR portfolio 8 slot daripada dagangan laluan 1 kolam berkorelasi 0.93 dengan `cagr_bersih` dalam papan.json.
  - Tiga kaedah sama tepat (M129 8.73%, M135 3.28%, M142 −0.16%), dan 22/29 kaedah berbeza ≤ 3 mata.
  - Beza terbesar: M41 +7.1, M137 +4.2, M04 −3.5, M10 −3.4 mata. Puncanya pemanasan berbeza (data dari 2011 berbanding [latih − 400 hari] dalam AUTOTUNE) dan pemotongan dagangan pada 2018-12-31.

### Inferences
- Pulangan hadapan dan `trade_ret` mengikut konvensyen AUTOTUNE, iaitu beli pada buka esok. Lajur `gap_masuk` membolehkan ujian 1 mengukur "kebocoran" buka esok secara langsung.
- `h52_industri` memakai peta industri semasa, bukan titik masa. Pertukaran industri lalu dan saham delist tidak diwakili.

### Gaps
- Tiada data intrahari: `on*`/`id*` dikira daripada OHLC harian terlaras. Buka yfinance ialah buka rasmi, bukan VWAP 30 minit.
- Isyarat bertindih bagi M20, M26 dan M78 tiada hasil keluar sendiri, tetapi pulangan `fwd*` masih ada.

## Soalan 3: Apakah statistik asas isyarat dan dagangan?

### Takeaway
Kolam mengandungi 1,890,526 isyarat atas 3,194 ticker dan 970,627 dagangan enjin (laluan 1). Purata dagangan bersih +0.34%, tetapi median −2.89% dan kadar menang 36.8%. 5% terburuk −13.85% dan purata pegangan 24.9 hari. Secara purata, dagangan laluan 1 kalah kepada SPY dalam 20 hari pertama: lebihan fwd20 − spy20 ialah −0.24% (A) dan −0.37% (B). Tiada kaedah mempunyai lebihan 20 hari yang positif. Kaedah terbaik ikut purata dagangan ialah M96 (+1.66%, n 649), M10 (+1.11%), M79 (+1.00%), M134 (+0.95%) dan M152 (+0.94%). Yang negatif ialah M20, M167, M26 dan M146.

### Cited Findings
Setiap kaedah (`statistik_kolam.py`). `n` = dagangan laluan 1; `buruk5` = persentil 5%; `lebih20` = purata (fwd20 − spy20) atas dagangan laluan 1; `pegang8` = dagangan yang dipegang portfolio 8 slot; `semua_purata` = semua isyarat dengan keluar sendiri; p10_20 = peratus isyarat dengan high maksimum 20 hari ≥ +10%:

| Kaedah | Isyarat | Hari isyarat | n dagangan | Purata | Median | Menang | 5% terburuk | Hari | lebih20 | n pegang8 | Purata pegang8 | semua_purata | fwd20 | spy20 | p10_20 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| M04 | 35,351 | 3,295 | 28,802 | 0.39% | -3.07% | 32.7% | -13.47% | 27.9 | -0.37% | 1,920 | 0.89% | 0.40% | 0.68% | 1.06% | 28.0% |
| M05 | 8,301 | 2,488 | 6,317 | 0.83% | -3.00% | 43.3% | -17.57% | 40.4 | -0.34% | 1,308 | 0.30% | 0.73% | 0.72% | 1.08% | 24.5% |
| M10 | 39,486 | 3,242 | 28,986 | 1.11% | -3.26% | 35.1% | -13.27% | 34.6 | -0.05% | 1,542 | 0.94% | 1.22% | 1.01% | 1.08% | 23.9% |
| M20 | 265,599 | 3,463 | 179,983 | -0.22% | -2.29% | 38.2% | -7.21% | 7.6 | -0.27% | 7,423 | -0.18% | -0.22% | 0.77% | 1.04% | 25.4% |
| M26 | 23,828 | 3,124 | 21,956 | -0.09% | -0.28% | 48.3% | -10.52% | 16.1 | -0.33% | 3,326 | 0.03% | -0.09% | 0.68% | 1.03% | 26.1% |
| M30 | 38,206 | 3,213 | 33,429 | 0.30% | -3.11% | 34.0% | -13.75% | 30.2 | -0.30% | 1,706 | 1.56% | 0.28% | 0.71% | 1.04% | 25.6% |
| M33 | 45,006 | 3,339 | 44,964 | 0.43% | -2.74% | 39.2% | -13.44% | 31.4 | -0.32% | 1,798 | 0.44% | 0.43% | 0.85% | 1.17% | 25.7% |
| M41 | 11,890 | 700 | 11,890 | 0.79% | -3.51% | 44.0% | -17.05% | 44.2 | -0.45% | 1,201 | 0.81% | 0.79% | 0.44% | 0.89% | 26.5% |
| M48 | 23,978 | 2,836 | 16,129 | 0.27% | -3.59% | 31.7% | -12.21% | 26.9 | -0.38% | 2,017 | 0.18% | 0.28% | 0.49% | 0.81% | 24.6% |
| M67 | 15,528 | 2,737 | 15,528 | 0.29% | -2.90% | 28.5% | -9.10% | 21.8 | -0.15% | 2,412 | 0.27% | 0.29% | 0.83% | 0.99% | 23.9% |
| M78 | 46,321 | 588 | 16,165 | 0.55% | -8.28% | 32.4% | -8.95% | 30.2 | -0.25% | 1,850 | 1.13% | 0.55% | 0.53% | 0.85% | 32.2% |
| M79 | 48,431 | 3,342 | 48,337 | 1.00% | -4.27% | 41.1% | -16.46% | 36.4 | -0.63% | 1,717 | 0.76% | 1.00% | 1.32% | 1.96% | 43.6% |
| M89 | 55,756 | 3,343 | 44,515 | 0.35% | -3.29% | 32.6% | -10.53% | 24.0 | -0.15% | 2,498 | -0.08% | 0.27% | 0.83% | 1.05% | 26.3% |
| M91 | 13,733 | 2,827 | 13,273 | 0.01% | -1.74% | 38.2% | -10.65% | 17.0 | -0.36% | 3,047 | 0.42% | 0.02% | 0.68% | 1.04% | 24.2% |
| M93 | 121,654 | 3,426 | 65,130 | 0.59% | -3.80% | 37.5% | -16.10% | 35.5 | -0.43% | 1,615 | 0.06% | 0.47% | 0.51% | 0.97% | 25.0% |
| M95 | 153,997 | 3,388 | 36,006 | 0.30% | -3.52% | 30.0% | -9.88% | 26.2 | -0.26% | 2,085 | 0.70% | -0.04% | 0.47% | 0.77% | 19.1% |
| M96 | 1,014 | 165 | 649 | 1.66% | -6.20% | 35.1% | -24.61% | 31.1 | -0.16% | 649 | 1.66% | 1.50% | 1.19% | 1.14% | 46.4% |
| M118 | 25,391 | 3,067 | 23,680 | 0.13% | -2.95% | 30.3% | -11.87% | 24.8 | -0.22% | 2,251 | 0.65% | 0.16% | 0.94% | 1.16% | 28.3% |
| M124 | 99,843 | 3,433 | 93,671 | 0.25% | -2.94% | 33.7% | -10.63% | 20.7 | -0.20% | 3,083 | 0.06% | 0.24% | 1.05% | 1.24% | 28.8% |
| M129 | 15,802 | 2,481 | 12,890 | 0.49% | -4.43% | 37.1% | -15.37% | 37.3 | -0.45% | 1,411 | 0.61% | 0.40% | 0.39% | 0.83% | 22.9% |
| M130 | 3,988 | 1,580 | 3,838 | 0.44% | -5.22% | 40.4% | -15.71% | 40.5 | -0.36% | 1,211 | 0.64% | 0.38% | 0.46% | 0.86% | 24.5% |
| M134 | 18,933 | 2,549 | 16,650 | 0.95% | -3.75% | 33.0% | -11.47% | 27.5 | -0.26% | 1,939 | 0.87% | 0.93% | 0.93% | 1.17% | 28.0% |
| M135 | 5,880 | 2,240 | 5,737 | 0.57% | -2.78% | 37.8% | -13.18% | 34.3 | -0.37% | 1,452 | 0.93% | 0.64% | 0.71% | 1.04% | 21.7% |
| M137 | 77,670 | 3,421 | 41,041 | 0.79% | -3.79% | 35.2% | -11.99% | 31.0 | -0.20% | 1,902 | 0.50% | 0.68% | 0.69% | 0.94% | 22.6% |
| M139 | 34,621 | 3,355 | 34,586 | 0.27% | 0.16% | 50.7% | -15.76% | 19.7 | -0.34% | 2,971 | 0.58% | 0.27% | 0.77% | 1.10% | 28.0% |
| M142 | 11,297 | 2,695 | 10,090 | 0.68% | -3.69% | 37.9% | -15.54% | 35.5 | -0.09% | 1,505 | 0.81% | 0.64% | 0.90% | 0.98% | 30.5% |
| M146 | 24,048 | 3,014 | 20,504 | -0.06% | -4.03% | 28.5% | -8.08% | 25.1 | -0.50% | 2,279 | 0.43% | -0.07% | 0.40% | 0.88% | 25.0% |
| M149 | 71,375 | 3,336 | 46,430 | 0.63% | -4.86% | 35.0% | -14.47% | 35.3 | -0.40% | 1,676 | 0.52% | 0.61% | 0.48% | 0.90% | 24.0% |
| M152 | 88,906 | 3,361 | 25,630 | 0.94% | 0.37% | 51.3% | -16.05% | 37.8 | -0.22% | 1,586 | 0.46% | 0.81% | 0.61% | 0.82% | 21.7% |
| M167 | 464,693 | 2,960 | 23,821 | -0.21% | -6.39% | 31.9% | -12.61% | 25.6 | -0.32% | 2,164 | -0.08% | 0.05% | 0.53% | 0.94% | 40.7% |

Setiap tahun (dagangan laluan 1, semua kaedah; `isyarat` = semua baris):

| Tahun | Isyarat | n | Purata | Median | Menang | 5% terburuk | Hari | lebih20 | spy20 |
|---|---|---|---|---|---|---|---|---|---|
| 2013 | 120,774 | 57,190 | 1.99% | -1.10% | 45.9% | -9.04% | 28.5 | 0.38% | 1.65% |
| 2014 | 110,938 | 54,890 | -0.32% | -2.57% | 35.6% | -11.08% | 25.5 | -0.68% | 0.80% |
| 2015 | 100,669 | 52,390 | -1.94% | -3.34% | 28.8% | -13.48% | 23.1 | -0.38% | -0.40% |
| 2016 | 116,901 | 60,207 | 1.36% | -1.70% | 43.5% | -11.24% | 28.7 | 0.42% | 1.39% |
| 2017 | 146,036 | 70,236 | 1.21% | -1.85% | 42.3% | -10.34% | 27.5 | -0.28% | 1.69% |
| 2018 | 125,199 | 63,173 | -1.42% | -3.55% | 29.8% | -13.49% | 22.7 | -0.31% | -0.54% |
| 2019 | 144,298 | 74,032 | 0.71% | -2.19% | 40.8% | -12.30% | 27.6 | -0.69% | 1.63% |
| 2020 | 143,635 | 78,179 | 3.89% | -2.70% | 41.6% | -15.01% | 24.9 | 1.03% | 0.90% |
| 2021 | 177,391 | 87,281 | -0.65% | -3.45% | 34.7% | -15.03% | 23.3 | -1.00% | 1.45% |
| 2022 | 91,757 | 65,576 | -2.43% | -4.70% | 28.1% | -15.48% | 21.3 | -0.02% | -1.48% |
| 2023 | 151,926 | 78,780 | 0.31% | -3.09% | 36.4% | -13.80% | 25.8 | -0.77% | 1.41% |
| 2024 | 178,389 | 86,286 | 0.05% | -3.06% | 35.5% | -13.92% | 23.9 | -0.66% | 1.59% |
| 2025 | 151,204 | 77,564 | 0.99% | -3.24% | 36.3% | -14.89% | 24.8 | -0.35% | 1.18% |
| 2026 | 131,409 | 64,843 | 0.12% | -3.58% | 34.3% | -15.17% | 21.6 | -0.61% | 1.02% |

Setiap kumpulan:

| Kumpulan | Isyarat | n | Purata | Median | Menang | 5% terburuk | Hari | lebih20 |
|---|---|---|---|---|---|---|---|---|
| A | 965,193 | 496,290 | 0.37% | -2.87% | 36.8% | -13.86% | 24.9 | -0.24% |
| B | 925,333 | 474,337 | 0.30% | -2.91% | 36.8% | -13.84% | 24.9 | -0.37% |

- Purata dagangan A/B setiap kaedah biasanya dekat. Pengecualian: M05 (A 0.40% / B 1.29%), M41 (0.97% / 0.60%), M78 (0.76% / 0.34%), M146 (−0.20% / 0.09%) dan M26 (−0.23% / 0.05%). — `statistik.md`
- Jadual isyarat kaedah × tahun dan sebab keluar setiap kaedah ada dalam `statistik.md`. Ringkasan sebab keluar:
  - "isyarat keluar" mendominasi M91 (92%), M04/M30 (78%) dan M118 (74%).
  - "masa" mendominasi M139 (86%) dan M152 (79%).
  - "sasaran" hanya wujud bagi M20 (31%) dan M26 (40%).
  - "henti" paling tinggi bagi M149 (61%) dan M20 (58%).
- Taburan isyarat tidak seimbang: M167 menyumbang 464,693 baris (25% kolam), M20 265,599 dan M95 153,997. Bagi M167, hanya 23,821 baris (5.1%) ialah dagangan laluan 1, kerana isyarat berulang setiap hari selagi saham kekal dalam kolam OVN252 ≥ 0.90.
- Portfolio pegang8 memilih subset yang berbeza: purata pegang8 lebih tinggi bagi M30 (1.56% lawan 0.30%), M118 (0.65% lawan 0.13%) dan M95 (0.70% lawan 0.30%), tetapi lebih rendah bagi M93 (0.06% lawan 0.59%) dan M89 (−0.08% lawan 0.35%).

### Inferences
- Pulangan dagangan sangat condong ke kanan (purata positif, median sekitar −3%, menang 28–51%). Ujian veto/ranking wajar menilai purata, persentil 5% dan kadar +10% dalam 20 hari (`mfe20 ≥ 0.10`), bukan median sahaja.
- Lebihan fwd20 − spy20 negatif dalam 11/14 tahun (positif hanya 2013, 2016, 2020) walaupun data mempunyai bias survivorship, iaitu had atas. Ini selari dengan label RENDAH/GAGAL A01. Kelebihan yang hendak ditambah oleh ciri bar mesti melebihi garis dasar negatif ini.
- Bagi ujian ranking, setiap hari perlu dinormalkan ikut kaedah (contohnya persentil dalam kaedah), atau pemberat ikut kaedah perlu dipakai. Jika tidak, M167/M20/M95 akan menguasai statistik terkumpul.

### Gaps
- Tiada bootstrap atau ralat piawai dalam garis dasar. Ujian seterusnya perlu mengira t ikut hari beli berbeza (peraturan BELUM CUKUP / t > 3 dalam laporan).

## Soalan 4: Bagaimana taburan ciri, dan sejauh mana ciri bertindih dengan RS?

### Takeaway
Ciri bentuk bar, volum, gap dan semalaman/intrahari jangka pendek hampir tidak berkorelasi dengan RS proksi (|ρ| ≤ 0.18). h52 paling bertindih dengan RS (ρ 0.43 dengan rs6, 0.32 dengan rs12; median dalam kaedah 0.43). Ia diikuti on252/id60 (0.2–0.4), tetapi semuanya di bawah ambang 0.6 dalam laporan. Isyarat kaedah breakout kerap jatuh pada hari "perhatian": 3.4% baris unik berada dalam 1% teratas pulangan setahun sendiri (asas 1%), dan bagi M135, M04, M30, M33 dan M79 bahagian ini 21–42%.

### Cited Findings
Taburan atas 1,401,828 baris unik ticker × tarikh isyarat:

| Ciri | Ada | Purata | p5 | p25 | p50 | p75 | p95 |
|---|---|---|---|---|---|---|---|
| ret1 | 100.0% | 0.014 | -0.027 | 0.002 | 0.012 | 0.024 | 0.061 |
| max20 | 100.0% | 0.058 | 0.016 | 0.028 | 0.042 | 0.067 | 0.149 |
| gap_atr | 100.0% | 0.146 | -0.346 | -0.058 | 0.087 | 0.268 | 0.746 |
| julat_atr | 100.0% | 1.059 | 0.477 | 0.701 | 0.928 | 1.247 | 2.038 |
| atas1pct_1t | 100.0% | 0.034 | 0 | 0 | 0 | 0 | 0 |
| rcc_srs60 | 100.0% | 0.730 | -1.015 | 0.114 | 0.669 | 1.270 | 2.552 |
| gap_atr_pctl252 | 100.0% | 0.580 | 0.087 | 0.345 | 0.611 | 0.833 | 0.976 |
| on5 | 100.0% | 0.011 | -0.029 | -0.004 | 0.007 | 0.021 | 0.065 |
| on20 | 100.0% | 0.029 | -0.058 | -0.005 | 0.021 | 0.055 | 0.146 |
| id20 | 100.0% | 0.021 | -0.146 | -0.024 | 0.024 | 0.072 | 0.176 |
| id_share20 | 100.0% | 0.205 | -0.835 | -0.370 | 0.400 | 0.733 | 0.941 |
| on60 | 100.0% | 0.078 | -0.099 | 0.003 | 0.059 | 0.132 | 0.313 |
| id60 | 100.0% | 0.031 | -0.277 | -0.050 | 0.039 | 0.123 | 0.304 |
| id_share60 | 100.0% | 0.184 | -0.788 | -0.338 | 0.326 | 0.684 | 0.926 |
| on252 | 99.6% | 0.279 | -0.198 | 0.036 | 0.208 | 0.450 | 0.960 |
| vol_rel50 | 100.0% | 1.300 | 0.541 | 0.792 | 1.043 | 1.432 | 2.700 |
| vol_pctl50 | 100.0% | 0.538 | 0.060 | 0.280 | 0.560 | 0.800 | 0.980 |
| naik_vol90 | 100.0% | 0.133 | 0 | 0 | 0 | 0 | 1 |
| hijau_vol90 | 100.0% | 0.122 | 0 | 0 | 0 | 0 | 1 |
| h52 | 100.0% | 0.863 | 0.530 | 0.805 | 0.922 | 0.975 | 0.997 |
| h52_industri | 94.5% | 0.864 | 0.665 | 0.811 | 0.890 | 0.940 | 0.979 |
| ibs | 100.0% | 0.646 | 0.102 | 0.446 | 0.718 | 0.884 | 0.980 |
| badan_julat | 100.0% | 0.498 | 0.060 | 0.284 | 0.513 | 0.713 | 0.904 |
| badan_arah | 100.0% | 0.286 | -0.667 | -0.034 | 0.407 | 0.674 | 0.893 |
| bayang_atas | 100.0% | 0.248 | 0.007 | 0.086 | 0.203 | 0.371 | 0.642 |
| bayang_bawah | 100.0% | 0.254 | 0.000 | 0.083 | 0.212 | 0.386 | 0.659 |
| ha_naik_berturut | 100.0% | 3.198 | 0 | 1 | 2 | 5 | 10 |
| rs6_pct | 100.0% | 0.616 | 0.086 | 0.398 | 0.669 | 0.868 | 0.981 |
| rs12_pct | 99.6% | 0.621 | 0.088 | 0.395 | 0.676 | 0.879 | 0.983 |

Korelasi Spearman dengan RS proksi (baris unik; lajur dalam kaedah = ρ dengan rs12_pct dikira dalam setiap kaedah). ρ(rs6_pct, rs12_pct) = 0.635:

| Ciri | ρ rs6 | ρ rs12 | Median ρ rs12 dalam kaedah | Min kaedah | Maks kaedah |
|---|---|---|---|---|---|
| ret1 | -0.002 | -0.091 | 0.058 | -0.130 | 0.308 |
| max20 | 0.159 | 0.165 | 0.109 | -0.035 | 0.580 |
| gap_atr | -0.012 | -0.048 | 0.022 | -0.023 | 0.039 |
| julat_atr | -0.004 | -0.042 | 0.012 | -0.078 | 0.068 |
| atas1pct_1t | -0.030 | -0.056 | -0.005 | -0.077 | 0.060 |
| rcc_srs60 | -0.042 | -0.140 | 0.024 | -0.084 | 0.084 |
| gap_atr_pctl252 | -0.021 | -0.070 | 0.000 | -0.036 | 0.043 |
| on5 | 0.046 | 0.029 | 0.049 | 0.000 | 0.158 |
| on20 | 0.129 | 0.126 | 0.086 | 0.015 | 0.219 |
| id20 | 0.177 | 0.055 | 0.072 | -0.046 | 0.283 |
| id_share20 | 0.113 | 0.003 | -0.009 | -0.116 | 0.175 |
| on60 | 0.241 | 0.232 | 0.181 | 0.068 | 0.298 |
| id60 | 0.393 | 0.187 | 0.209 | 0.018 | 0.341 |
| id_share60 | 0.304 | 0.116 | 0.096 | -0.116 | 0.324 |
| on252 | 0.204 | 0.393 | 0.347 | 0.247 | 0.534 |
| vol_rel50 | 0.032 | 0.008 | 0.076 | -0.031 | 0.147 |
| vol_pctl50 | 0.026 | 0.002 | 0.044 | -0.061 | 0.119 |
| naik_vol90 | 0.009 | -0.029 | 0.032 | -0.080 | 0.088 |
| hijau_vol90 | 0.010 | -0.026 | 0.032 | -0.055 | 0.082 |
| h52 | 0.426 | 0.318 | 0.427 | -0.464 | 0.629 |
| h52_industri | 0.154 | 0.108 | 0.151 | -0.322 | 0.244 |
| ibs | -0.018 | -0.090 | 0.012 | -0.038 | 0.049 |
| badan_julat | -0.022 | -0.046 | 0.012 | -0.060 | 0.046 |
| badan_arah | -0.031 | -0.117 | 0.014 | -0.047 | 0.051 |
| bayang_atas | 0.003 | 0.014 | -0.008 | -0.030 | 0.033 |
| bayang_bawah | 0.025 | 0.047 | -0.004 | -0.034 | 0.046 |
| ha_naik_berturut | 0.041 | -0.037 | 0.012 | -0.124 | 0.089 |

Median ciri setiap kaedah (atas1pct_1t dan naik_vol90 = bahagian isyarat):

| Kaedah | max20 | ret1 | gap_atr | julat_atr | id_share20 | id_share60 | vol_rel50 | h52 | ibs | rs12_pct | atas1pct_1t | naik_vol90 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| M04 | 0.050 | 0.044 | 0.344 | 1.878 | 0.595 | 0.428 | 2.204 | 0.943 | 0.824 | 0.602 | 0.296 | 0.808 |
| M05 | 0.037 | 0.022 | 0.163 | 1.086 | 0.598 | -0.128 | 1.154 | 0.913 | 0.834 | 0.617 | 0.103 | 0.236 |
| M10 | 0.035 | 0.019 | 0.194 | 1.018 | 0.272 | 0.288 | 1.164 | 0.950 | 0.764 | 0.685 | 0.099 | 0.240 |
| M20 | 0.034 | 0.019 | 0.157 | 1.017 | 0.143 | 0.453 | 1.000 | 0.929 | 0.828 | 0.606 | 0.056 | 0.143 |
| M26 | 0.036 | 0.020 | 0.167 | 1.009 | 0.477 | 0.350 | 1.033 | 0.917 | 0.826 | 0.567 | 0.053 | 0.162 |
| M30 | 0.044 | 0.038 | 0.305 | 1.691 | 0.655 | 0.461 | 1.631 | 0.952 | 0.872 | 0.594 | 0.259 | 0.491 |
| M33 | 0.043 | 0.033 | 0.262 | 1.427 | 0.457 | 0.017 | 1.592 | 0.897 | 0.837 | 0.507 | 0.248 | 0.468 |
| M41 | 0.059 | 0.012 | 0.094 | 1.057 | 0.678 | 0.563 | 1.511 | 0.948 | 0.700 | 0.558 | 0.076 | 0.331 |
| M48 | 0.046 | 0.020 | 0.135 | 1.014 | 0.655 | 0.601 | 1.040 | 0.964 | 0.833 | 0.700 | 0.033 | 0.145 |
| M67 | 0.031 | 0.010 | 0.110 | 0.900 | 0.431 | 0.605 | 0.978 | 0.956 | 0.746 | 0.706 | 0.016 | 0.118 |
| M78 | 0.057 | 0.008 | 0.071 | 0.873 | 0.620 | 0.579 | 1.064 | 0.980 | 0.667 | 0.843 | 0.021 | 0.139 |
| M79 | 0.070 | 0.043 | 0.184 | 1.154 | 0.364 | -0.222 | 1.316 | 0.754 | 0.842 | 0.420 | 0.213 | 0.307 |
| M89 | 0.036 | 0.004 | 0.036 | 0.826 | 0.085 | 0.340 | 0.981 | 0.921 | 0.604 | 0.583 | 0.014 | 0.091 |
| M91 | 0.041 | 0.025 | 0.167 | 1.244 | 0.667 | 0.509 | 1.566 | 0.956 | 0.854 | 0.595 | 0.101 | 0.450 |
| M93 | 0.040 | 0.011 | 0.107 | 0.939 | 0.648 | 0.460 | 1.121 | 0.948 | 0.712 | 0.597 | 0.042 | 0.201 |
| M95 | 0.036 | 0.016 | 0.142 | 1.068 | 0.708 | 0.648 | 1.226 | 0.996 | 0.827 | 0.787 | 0.051 | 0.261 |
| M96 | 0.064 | 0.005 | 0.038 | 0.885 | 0.567 | 0.617 | 1.145 | 0.957 | 0.543 | 0.993 | 0.014 | 0.135 |
| M118 | 0.043 | 0.018 | 0.129 | 1.112 | 0.590 | 0.348 | 1.275 | 0.908 | 0.789 | 0.519 | 0.054 | 0.296 |
| M124 | 0.040 | 0.015 | 0.107 | 0.954 | 0.308 | -0.086 | 1.079 | 0.878 | 0.760 | 0.491 | 0.066 | 0.171 |
| M129 | 0.037 | 0.014 | 0.123 | 0.943 | 0.638 | 0.611 | 1.092 | 0.981 | 0.796 | 0.685 | 0.022 | 0.177 |
| M130 | 0.040 | 0.014 | -0.109 | 1.121 | 0.748 | 0.541 | 1.158 | 0.948 | 0.854 | 0.590 | 0.014 | 0.182 |
| M134 | 0.045 | 0.019 | 0.156 | 0.966 | 0.624 | 0.128 | 0.988 | 0.862 | 0.815 | 0.459 | 0.049 | 0.138 |
| M135 | 0.052 | 0.046 | 0.396 | 2.052 | 0.647 | 0.549 | 2.431 | 0.991 | 0.842 | 0.727 | 0.416 | 0.866 |
| M137 | 0.039 | 0.020 | 0.169 | 1.096 | 0.629 | 0.575 | 1.185 | 0.981 | 0.830 | 0.650 | 0.101 | 0.269 |
| M139 | 0.037 | 0.010 | 0.075 | 0.887 | 0.242 | 0.150 | 0.980 | 0.880 | 0.716 | 0.516 | 0.028 | 0.104 |
| M142 | 0.091 | -0.013 | -0.024 | 1.028 | 0.602 | 0.521 | 1.644 | 0.963 | 0.284 | 0.844 | 0.000 | 0.000 |
| M146 | 0.043 | 0.030 | 0.216 | 1.443 | 0.724 | 0.531 | 1.439 | 0.964 | 0.840 | 0.611 | 0.147 | 0.389 |
| M149 | 0.045 | 0.016 | 0.100 | 0.916 | 0.684 | 0.531 | 0.976 | 0.957 | 0.824 | 0.622 | 0.011 | 0.096 |
| M152 | 0.033 | 0.012 | 0.107 | 0.921 | 0.646 | 0.648 | 1.030 | 0.980 | 0.780 | 0.684 | 0.021 | 0.152 |
| M167 | 0.055 | 0.001 | 0.031 | 0.853 | -0.160 | -0.150 | 0.994 | 0.859 | 0.500 | 0.867 | 0.010 | 0.070 |

### Inferences
- Ujian 3 (id_share sebagai kunci ranking): id_share20 hampir ortogonal kepada RS (ρ 0.00–0.11; julat dalam kaedah −0.12 hingga 0.18). Syarat |ρ| < 0.6 dalam laporan dipenuhi dengan selesa. id_share60 sedikit lebih bertindih (0.30 dengan rs6).
- Isyarat M167 bercirikan id_share negatif (median −0.16/−0.15), iaitu didominasi pulangan semalaman, mengikut binaannya. Isyarat kaedah lain kebanyakannya intrahari-positif (median 0.4–0.7). Perbandingan "semalaman lawan intrahari" antara M167 dan kaedah lain boleh dibuat terus atas kolam ini.
- Ujian 4: h52 bertindih paling banyak dengan RS. Satu kaedah mencapai ρ 0.63 dengan rs12 dalam kaedahnya, melebihi ambang 0.6, jadi hasil h52 perlu dibaca dalam tercil RS. Bertentangan dengannya, h52_industri jauh lebih bebas (0.11–0.15).
- Ujian 1 (veto lonjakan): kaedah breakout (M135, M04, M30, M33, M79, M146) mempunyai 15–42% isyarat pada hari 1% teratas setahun, dengan julat 1.2–2.1 × ATR dan volum 1.3–2.4 × median. Veto "hari perhatian" akan membuang sebahagian besar isyarat kaedah ini, jadi bilangan yang dibuang mesti dilapor setiap kaedah.

### Gaps
- Korelasi di atas ialah Spearman terkumpul. Kebergantungan ikut masa (contohnya 2020–2021) belum diperiksa.
- RS proksi ialah persentil pulangan mentah 6/12 bulan, bukan RS rasmi `data/rs/` (yang hanya wujud sejak Sep 2026). Ia tidak dilaras untuk 1 bulan terakhir (bukan 12-1).

## Soalan 5: Batasan yang mesti diingat oleh ujian seterusnya

### Takeaway
Kolam ini mewarisi bias survivorship AUTOTUNE, peta industri statik, dan keluar replika yang bergantung laluan. Selain itu, isyarat bertindih (laluan ≥ 2) tidak bebas antara satu sama lain.

### Cited Findings
- Tiada saham delist dalam data AUTOTUNE, jadi semua keputusan ialah had atas. — [AUTOTUNE/SPEC.md](../../../../AUTOTUNE/SPEC.md) §1
- 48.7% baris (919,899) ialah laluan ≥ 2, iaitu isyarat berulang semasa posisi ticker yang sama masih dibuka. Pulangan hadapannya bertindih dengan baris laluan 1. — `kolam.parquet`
- Bagi M20, M26, M41 dan M78, exitc ditanda dalam `sedia()` oleh replika laluan v1.2. Laluan 1 di bawah enjin_at (had 60 hari, gap) boleh berbeza sedikit daripada replika, sama seperti dalam AUTOTUNE sendiri. — [CLAUDE.md](../../../../CLAUDE.md) (kaedah replika); `bina_kolam.py IKUT_LALUAN`
- Kolam mengandungi isyarat sejak 2013 tanpa pemisahan latih/sah. Laporan menetapkan bahawa pemilihan varian dibuat atas 2019–2023 dan pengesahan atas 2024–2026, S1–S4, H1/H2, dan kumpulan A lawan B. — [Jenis lilin dan carta alternatif.md](../../reports/Jenis%20lilin%20dan%20carta%20alternatif.md)

### Inferences
- Untuk statistik setiap dagangan, guna `dagangan_enjin == True`. Untuk ujian pulangan hadapan setiap isyarat, guna semua baris dengan sisihan piawai ikut kelompok hari isyarat, atau ambil satu isyarat pertama setiap (kaedah, ticker, tempoh).
- Pembahagian A/B sedia ada: kumpulan A boleh dipakai untuk memilih varian dan B untuk semakan, selaras dengan SPEC A01.

### Gaps
- Tiada senarai pemfailan pendapatan dalam data AUTOTUNE, jadi kesan isyarat yang merentas earnings tidak dapat ditanda dalam kolam ini.
