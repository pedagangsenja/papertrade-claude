# Lorong 3: keluar carta alternatif lawan Chandelier lorong 2 (AUTOTUNE, 2000 saham AS, 2013 – Okt 2026)

Nota ini ialah hasil pengiraan sendiri, bukan sumber web. Bukti = skrip dan fail output yang dinyatakan.

## Pradaftar (ditulis 22 Okt 2026 SEBELUM sebarang keputusan dikira)

Soalan: adakah keluar berasaskan carta alternatif (Heikin-Ashi, HA dilicinkan, Renko, Kagi, Point & Figure, Line Break) mengatasi keluar lorong 2 (Chandelier tutup 4×ATR14, paras hanya naik, tanpa henti kaedah; `standard/keluar_lorong.py`) untuk memegang pemenang?

**Set kemasukan.** Dagangan laluan 1 (`dagangan_enjin == True`) dalam kolam `kolam.parquet` (970,627 dagangan, 30 kaedah). Beli pada buka hari masuk (bar k). Dua pemberat:
- (U) **Unik**: satu baris setiap (ticker, entry_date) — 741,341 kemasukan; keluar dinilai bebas daripada kaedah masuk. Analisis utama.
- (K) **Ternormal kaedah**: semua dagangan laluan 1, pemberat 1/n kaedah dalam setiap sampel (setiap kaedah sama berat). Garis dasar (0) hanya wujud di sini.

**Varian (16; had ≤ 20).** Semua isyarat dinilai pada TUTUP bar j ≥ k; jual pada BUKA j+1; tiada susunan intrabar; tiada henti kaedah. ATR14 = `keluar_lorong.atr` (purata mudah 14 TR, TR bar pertama = H−L, termasuk bar j). "Dibeku" = ATR14 pada bar k−1 (tutup hari isyarat, diketahui sebelum beli), A0.
- (0) Keluar kaedah sendiri = `trade_ret` kolam (enjin_at: henti/sasaran/isyarat/had 60).
- (1) CH4: Chandelier tutup, paras = max(paras semalam, tutup tertinggi k..j − 4×ATR14[j]); tutup < paras → jual buka esok. Sama seperti `keluar_lorong.lorong_henti`.
- (1b) CH3, CH5: sama, gandaan 3 dan 5 (sempadan longgar–ketat).
- RENKO k/r: bata b = k×A0; asas T = tutup k; bata naik: jika C ≥ T + b, T += b×floor((C−T)/b); keluar bila C ≤ T − r×b. Varian (k=1,r=2), (k=2,r=2), (k=1,r=4) [(1,4) dan (2,2) mempunyai jarak nominal 4×ATR yang sama; beza = saiz langkah].
- KAGI m: R = m×A0, m ∈ {3,4,5}; keluar pada pusingan pertama: C ≤ tutup tertinggi sejak k − R (= Chandelier dengan ATR dibeku; kawalan ATR dibeku lawan bergerak).
- PF: kotak b = 1×A0, grid mutlak (gandaan b dari sifar); lajur X atas = floor(C/b)×b tertinggi sejak k (bermula floor(C_k/b)×b); lajur O pertama bila C ≤ atas − 3b → keluar.
- LB N (Line Break, tutup): garis putih baharu bila C > atas garis terakhir (garis pertama bermula dari C_k); keluar (garis hitam pertama) bila C < rendah terendah N garis putih terakhir. Sebelum N garis putih wujud: henti awal C < buka beli − 4×A0. N ∈ {3,4}.
- HA2, HA3: HAc = (O+H+L+C)/4, HAo = (HAo₋₁ + HAc₋₁)/2 (rekursi sebab-akibat sejak bar pertama data 2011; pemanasan ≫ 20 bar). Merah = HAc < HAo. Keluar selepas 2 / 3 bar merah berturut-turut yang dikira dari bar k.
- SHA20: O',H',L',C' = EMA20 bagi O,H,L,C; HA atas O'..C'; HAo'', HAc'' = EMA20 bagi HAo', HAc'. Keluar pada pertukaran warna hijau → merah pertama (bar j ≥ k dengan HAc'' < HAo'' dan bar j−1 hijau). Jika masuk semasa merah, tunggu hijau dahulu.
- Had pegangan 60 hari dagangan (keluar pada tutup bar k+59, sama seperti had60 enjin_at; isyarat pada bar itu diutamakan seperti enjin_at). Laporan sekunder: had 120 hari. Data tamat (16 Okt 2026) → dinilai pada tutup terakhir.

**Kos.** Kos setiap sisi = lajur `kos` kolam (enjin_at: 0.1% + slippage 0.05/0.10/0.25% ikut median nilai dagangan 20 hari). Pulangan = X/e × (1−kos)/(1+kos) − 1.

**Sampel.** SELECT = kumpulan A, masuk 2013-01-01 – 2021-12-31. VALIDATE-B = kumpulan B tempoh sama. VALIDATE-T = A+B masuk 2022-01-01 – hujung. Setiap satu juga dengan tahun kalendar masuk 2020 dan 2025 dikecualikan.

**Metrik** (seperti KAJIAN_LORONG2): purata dan median pulangan bersih, kadar menang (> 0), 5% terburuk (persentil 5), purata hari pegang (J−k+1), lebihan SPY sebulan = purata(pulangan − SPY tempoh sama) ÷ purata hari × 21 (SPY: buka hari masuk → buka hari keluar bagi keluar buka, tutup bagi keluar tutup), bahagian dagangan dengan pulangan bersih ≥ +10%, give-back = (tutup tertinggi semasa pegang, termasuk harga keluar) ÷ e − pulangan kasar, dalam mata %. t perbezaan lawan CH4 bagi lebihan SPY sebulan (kaedah delta atas nisbah, ralat piawai berkelompok ikut tarikh masuk).

**Peraturan lulus.** Calon lulus hanya jika: (a) lebihan SPY sebulan > CH4 dalam KETIGA-TIGA sampel; (b) t > 3 dalam SELECT; (c) 5% terburuk tidak lebih buruk daripada CH4 > 1 mata dalam ketiga-tiga sampel; (d) (a) masih benar apabila 2020 dan 2025 dikecualikan. Selain itu: GAGAL. Kedudukan setiap calon pada sempadan CH3/CH4/CH5 dilapor (interpolasi lebihan sebulan CH pada hari pegang calon).

**Semakan kewarasan.** CH4 (tanpa had) dibanding dengan `keluar_lorong.lorong_henti` atas sampel rawak kemasukan; bilangan sepadan dilapor.

Skrip: `BacktestShariah2/kajian/lilin/uji_lorong3.py`. Output perantaraan: `/tmp/claude-0/-home-user-papertrade-claude/0793050f-2ee1-522e-9bf0-b633a13089db/scratchpad/lilin/lorong3/`.

> Pradaftar di atas tidak diubah selepas keputusan dikira. Larian pertama terhenti kerana container dimulakan semula sebelum skrip ditulis. Skrip dan semua angka di bawah datang daripada larian semula pada 22 Okt 2026 (bab "Butiran pelaksanaan" menerangkan tafsiran yang tidak dinyatakan secara eksplisit dalam pradaftar).

Sumber angka (semua hasil pengiraan sendiri):
- Skrip: [`BacktestShariah2/kajian/lilin/uji_lorong3.py`](../../lilin/uji_lorong3.py). Arahan `sim`, `semak`, `ringkas` dan `jadual`.
- Output: `/tmp/claude-0/-home-user-papertrade-claude/0793050f-2ee1-522e-9bf0-b633a13089db/scratchpad/lilin/lorong3/`:
  - `hasil.json`: semua metrik setiap pemberat, sampel dan had.
  - `lulus.json`: peraturan lulus.
  - `semak.json`: semakan kewarasan.
  - `jadual.md`: semua jadual penuh, termasuk pemberat K dan had 120.
  - `had_masa.txt`: bahagian keluar kerana had masa.
  - `v_<varian>_t<had>.npz`: keluar setiap kemasukan.
  - `U.parquet`, `K.parquet`: set kemasukan.
- Masa larian: penyediaan data 26–44 s, setiap varian 0.2–1.3 s (numba, 1 proses), ringkas kira-kira 3 minit.

## Soalan 1: Adakah mana-mana keluar carta alternatif lulus peraturan pradaftar lawan Chandelier tutup 4×ATR14?

### Takeaway
**Tidak. Tiada calon lulus. Semua 12 calon GAGAL** dengan pemberat U (analisis utama) dan juga pemberat K.
- Dua calon hampir lulus, iaitu RENKO 2×ATR/2 bata dan KAGI 5×ATR. Kedua-duanya mengatasi CH4 dalam ketiga-tiga sampel dengan t > 3 dalam SELECT, dan kekal mengatasi tanpa 2020 dan 2025.
- Namun kedua-duanya gagal syarat (c). 5% terburuk lebih buruk 2.7–4.8 mata, iaitu jauh melebihi had 1 mata.
- Kelebihannya kecil, hanya +0.03 hingga +0.06 mata % sebulan. Kelebihan itu datang daripada henti yang lebih longgar, bukan daripada carta.
- Heikin-Ashi mentah (2 atau 3 bar merah) paling teruk, kerana keluar terlalu awal (8.5–12.7 hari).

### Cited Findings
Pemberat U (satu baris setiap ticker + tarikh masuk), had 60 hari.

Lebihan SPY sebulan (%) bagi CH4 dalam setiap sampel:

| Sampel | n | Lebihan SPY sebulan CH4 (%) | 5% terburuk CH4 (%) | Hari pegang CH4 |
|---|---|---|---|---|
| SELECT (A, 2013–2021) | 234,654 | −0.30 | −16.08 | 38.0 |
| VALIDATE-B (B, 2013–2021) | 222,986 | −0.36 | −16.05 | 38.0 |
| VALIDATE-T (A+B, 2022–16 Okt 2026) | 283,701 | −0.80 | −19.84 | 35.1 |

Setiap varian berbanding CH4. Dalam setiap sel, tiga angka ialah SELECT / VALIDATE-B / VALIDATE-T:
- **Beza lebihan** = beza lebihan SPY sebulan berbanding CH4, dalam mata %.
- **t** = t SELECT, berkelompok ikut tarikh masuk.
- **Δ5% terburuk** = 5% terburuk varian − CH4, dalam mata. Nilai negatif bermaksud lebih buruk.

| Varian | Beza lebihan | t | Δ5% terburuk | Hari (SELECT) | Keputusan (a/b/c/d) |
|---|---|---|---|---|---|
| CH3 (sempadan) | −0.10 / −0.12 / −0.08 | −7.5 | +2.26 / +2.31 / +2.86 | 29.8 | – |
| CH5 (sempadan) | +0.05 / +0.04 / +0.04 | 5.9 | −2.15 / −2.12 / −2.54 | 44.1 | – |
| RENKO 1×ATR, 2 bata | −0.19 / −0.21 / −0.17 | −7.8 | +3.26 / +3.32 / +4.18 | 26.4 | GAGAL (a,b,d) |
| RENKO 2×ATR, 2 bata | +0.05 / +0.04 / +0.03 | 3.5 | −2.74 / −2.72 / −3.73 | 45.6 | GAGAL (c) |
| RENKO 1×ATR, 4 bata | +0.03 / +0.02 / +0.02 | 2.8 | −2.16 / −2.14 / −3.01 | 43.8 | GAGAL (b,c) |
| KAGI 3×ATR | −0.07 / −0.11 / −0.06 | −4.6 | +1.24 / +1.30 / +1.48 | 32.8 | GAGAL (a,b,d) |
| KAGI 4×ATR (dibeku) | +0.01 / −0.01 / +0.01 | 0.5 | −1.40 / −1.38 / −1.94 | 41.3 | GAGAL (a,b,c) |
| KAGI 5×ATR | +0.06 / +0.05 / +0.04 | 3.9 | −3.44 / −3.52 / −4.76 | 47.2 | GAGAL (c) |
| P&F 1×ATR, 3 kotak | −0.02 / −0.05 / −0.01 | −1.8 | −0.09 / −0.11 / −0.30 | 37.3 | GAGAL (a,b,d) |
| Line Break 3 | −0.22 / −0.23 / −0.13 | −9.0 | −0.27 / −0.35 / −1.09 | 25.4 | GAGAL (a,b,c,d) |
| Line Break 4 | −0.10 / −0.10 / −0.09 | −6.4 | −1.47 / −1.45 / −2.44 | 31.9 | GAGAL (a,b,c,d) |
| HA 2 merah | −1.12 / −1.05 / −0.79 | −13.7 | +8.27 / +8.31 / +10.48 | 8.5 | GAGAL (a,b,d) |
| HA 3 merah | −0.66 / −0.67 / −0.61 | −11.0 | +6.66 / +6.63 / +8.46 | 12.7 | GAGAL (a,b,d) |
| HA dilicinkan EMA20 | −0.02 / −0.05 / +0.01 | −1.8 | +0.23 / +0.16 / +0.42 | 38.4 | GAGAL (a,b,d) |

Sumber: `hasil.json` kunci `U|<sampel>|penuh|t60`; `lulus.json` kunci `U|<varian>`; [uji_lorong3.py](../../lilin/uji_lorong3.py) `cmd_ringkas`, `lulus`.

Metrik penuh SELECT (U, had 60):

| Varian | Purata % | Median % | Menang % | 5% terburuk % | Hari | Lebihan SPY sebulan % | ≥ +10% | Give-back (mata) |
|---|---|---|---|---|---|---|---|---|
| CH4 | 1.46 | −2.12 | 42.4 | −16.08 | 38.0 | −0.30 | 20.1 | 9.93 |
| CH3 | 0.96 | −2.04 | 40.2 | −13.82 | 29.8 | −0.41 | 15.7 | 8.91 |
| CH5 | 1.89 | −1.41 | 46.1 | −18.23 | 44.1 | −0.25 | 23.3 | 10.36 |
| RENKO_1x_2 | 0.73 | −2.10 | 39.6 | −12.82 | 26.4 | −0.50 | 14.9 | 8.05 |
| RENKO_2x_2 | 2.00 | −0.47 | 48.7 | −18.82 | 45.6 | −0.26 | 24.2 | 10.13 |
| RENKO_1x_4 | 1.87 | −0.88 | 47.6 | −18.24 | 43.8 | −0.27 | 23.4 | 10.07 |
| KAGI3 | 1.14 | −1.92 | 42.3 | −14.84 | 32.8 | −0.37 | 18.0 | 9.08 |
| KAGI4 | 1.67 | −1.32 | 46.0 | −17.48 | 41.3 | −0.30 | 22.1 | 9.94 |
| KAGI5 | 2.11 | −0.04 | 49.9 | −19.52 | 47.2 | −0.25 | 24.7 | 10.23 |
| PF_1x_3 | 1.42 | −1.71 | 44.1 | −16.17 | 37.3 | −0.33 | 20.1 | 9.57 |
| LB3 | 0.78 | 0.33 | 52.7 | −16.35 | 25.4 | −0.52 | 12.7 | 7.18 |
| LB4 | 1.13 | 0.36 | 52.5 | −17.55 | 31.9 | −0.40 | 15.7 | 8.47 |
| HA2 | −0.16 | −1.11 | 36.8 | −7.81 | 8.5 | −1.43 | 5.2 | 3.39 |
| HA3 | 0.03 | −1.32 | 38.0 | −9.42 | 12.7 | −0.97 | 7.6 | 4.73 |
| SHA20 | 1.49 | −2.16 | 40.2 | −15.85 | 38.4 | −0.33 | 19.8 | 9.38 |

Sumber: `jadual.md` bahagian "U SELECT penuh t60". Jadual VALIDATE-B dan VALIDATE-T ada dalam fail yang sama, dengan susunan kedudukan yang sama.

Syarat (d), iaitu tanpa tahun masuk 2020 dan 2025. Lebihan SPY sebulan CH4 / RENKO_2x_2 / KAGI5:
- SELECT: −0.69 / −0.63 / −0.62. t beza ialah 5.8 bagi RENKO_2x_2 dan 6.5 bagi KAGI5.
- VALIDATE-B: −0.65 / −0.61 / −0.60.
- VALIDATE-T: −1.00 / −0.95 / −0.93.

Kedua-dua calon kekal mengatasi CH4, tetapi semua varian masih di bawah SPY. Sumber: `jadual.md` "U … tanpa2020_2025 t60".

### Inferences
- Satu-satunya "kemenangan" konsisten datang daripada keluar yang lebih longgar daripada 4×ATR: RENKO 2×ATR/2 bata (jarak nominal 4×ATR, tetapi langkah 2×ATR) dan KAGI 5×ATR. Kemenangan itu dibayar dengan ekor kiri yang lebih buruk.
- Gambaran yang sama berlaku pada CH5 sendiri. CH5 juga akan memenuhi (a), (b) dan (d), tetapi gagal (c) sebanyak 2.15–2.54 mata. Oleh itu, tiada carta alternatif menambah apa-apa yang tidak boleh diperoleh dengan melonggarkan gandaan Chandelier.
- Line Break memberi kadar menang tertinggi (52–53%) dan median positif. Namun pulangan purata dan lebihan SPY lebih rendah, jadi ia memotong pemenang lebih awal. Kadar menang yang tinggi di sini tidak bermaksud keluar yang lebih baik.
- Heikin-Ashi mentah ialah keluar "lilin" yang paling popular, tetapi paling teruk: lebihan SPY sebulan kira-kira −1.0 hingga −1.4%. Give-back rendah (3.4–4.7 mata) hanya kerana posisi dijual sebelum sempat naik.

### Gaps
- Pradaftar tidak menetapkan ujian statistik bagi syarat (c) 5% terburuk, jadi ia dinilai sebagai perbandingan titik sahaja. Bagi dua calon yang hampir lulus, beza 2.7–4.8 mata cukup jauh daripada had 1 mata sehingga keputusan tidak bergantung pada ralat sampel.

## Soalan 2: Di manakah setiap calon pada sempadan Chandelier 3×/4×/5×?

### Takeaway
Semua calon berada pada atau sedikit di bawah sempadan CH3–CH4–CH5 (lebihan sebulan berbanding hari pegang). Jaraknya antara −0.06 dan +0.01 mata % sebulan bagi calon bertaraf Chandelier, dan −0.3 hingga −0.75 bagi HA mentah. Tiada calon berada jelas di atas sempadan. Renko, Kagi, P&F, Line Break dan HA dilicinkan hanyalah titik lain pada keluk "longgar lawan ketat" yang sama.

### Cited Findings
Atas sempadan = lebihan sebulan calon − lebihan sebulan CH yang diinterpolasi linear pada hari pegang calon. Tanda * bermaksud ekstrapolasi, iaitu hari pegang di luar julat CH3–CH5 (29.8–44.1 hari dalam SELECT). Nilai di bawah ialah SELECT / VALIDATE-B / VALIDATE-T (U, had 60):

| Varian | SELECT | VALIDATE-B | VALIDATE-T |
|---|---|---|---|
| RENKO_1x_2 | −0.05* | −0.04* | −0.05* |
| RENKO_2x_2 | −0.02* | −0.00* | −0.02* |
| RENKO_1x_4 | −0.01 | −0.01 | −0.02 |
| KAGI3 | −0.01 | −0.03 | −0.00 |
| KAGI4 | −0.02 | −0.02 | −0.01 |
| KAGI5 | −0.02* | −0.00* | −0.02* |
| PF_1x_3 | −0.01 | −0.04 | −0.00 |
| LB3 | −0.06* | −0.05* | −0.02* |
| LB4 | −0.02 | −0.02 | −0.05 |
| HA2 | −0.75* | −0.63* | −0.51* |
| HA3 | −0.35* | −0.31* | −0.37* |
| SHA20 | −0.02 | −0.06 | +0.01 |

Tanpa 2020 dan 2025, jarak calon Renko, Kagi dan P&F berada antara −0.05 dan +0.03 (U dan K). Ini masih dalam hingar, kerana t KAGI4 lawan CH4 hanya 0.5 dalam sampel penuh. Sumber: `jadual.md`, lajur "Atas sempadan CH".

Titik sempadan (SELECT, U, had 60), dalam bentuk hari / lebihan sebulan / 5% terburuk:
- CH3: 29.8 / −0.41 / −13.82.
- CH4: 38.0 / −0.30 / −16.08.
- CH5: 44.1 / −0.25 / −18.23.

Lebihan sebulan naik secara monoton dengan kelonggaran, dan ekor kiri memburuk secara monoton.

Bahagian keluar kerana had masa 60 hari (U, semua tahun; `had_masa.txt`):

| Varian | Keluar pada had 60 hari |
|---|---|
| CH3 | 10.6% |
| CH4 | 23.9% |
| CH5 | 37.7% |
| KAGI4 | 32.3% |
| KAGI5 | 48.0% |
| RENKO_2x_2 | 45.0% |
| RENKO_1x_4 | 39.3% |
| SHA20 | 27.3% |
| LB3 | 5.9% |
| HA2 | 0.0% |

### Inferences
- KAGI4 ialah Chandelier tutup 4× dengan ATR dibeku pada hari isyarat. Ia hampir sama dengan CH4 (beza +0.01, t 0.5), jadi ATR bergerak berbanding dibeku tidak penting.
- Hampir separuh dagangan KAGI5 dan RENKO_2x_2 tamat kerana had 60 hari, bukan kerana isyarat carta. "Kelebihan" mereka sebahagian besarnya ialah kesan "pegang hingga had masa".
- Pilihan lorong 2 yang sebenar ialah titik pada sempadan risiko lawan pulangan: 4× atau 5×. Ia bukan pilihan jenis carta.

### Gaps
- Sempadan hanya ada tiga titik (3×, 4×, 5×), jadi ekstrapolasi (*) bagi HA, LB3, RENKO_1x_2, RENKO_2x_2 dan KAGI5 kurang tepat. Arah keputusan tidak berubah.

## Soalan 3: Adakah keputusan kukuh merentas pemberat, had pegangan, tahun, dan berbanding keluar kaedah sendiri?

### Takeaway
Ya. Kesimpulan GAGAL kukuh merentas semua pemberat, had pegangan dan tahun.
- **Pemberat K** (setiap kaedah sama berat): tiada calon lulus. KAGI5 gagal (b) kerana t SELECT hanya 2.3, dan RENKO_2x_2 kalah dalam VALIDATE-T (−0.02).
- **Had 120 hari**: susunan sama dengan had 60.
- **Ikut tahun**: calon mengikuti CH4 dengan rapat.
- **Lebihan SPY**: semua peraturan keluar, termasuk CH4, memberi lebihan SPY sebulan yang negatif atas kolam 30 kaedah ini di 2000 saham.
- **Keluar kaedah sendiri**: CH4 masih mengatasinya dalam ketiga-tiga sampel.

### Cited Findings
Pemberat K (970,627 dagangan laluan 1, 1/n setiap kaedah), had 60. Lebihan SPY sebulan bagi SELECT / VALIDATE-B / VALIDATE-T:

| Peraturan | Lebihan SPY sebulan (%) | Beza vs CH4 | t | 5% terburuk SELECT (%) |
|---|---|---|---|---|
| CH4 | −0.37 / −0.39 / −0.68 | – | – | −16.89 |
| KAGI5 | −0.32 / −0.34 / −0.67 | +0.05 / +0.05 / +0.01 | 2.3 (SELECT) | −20.47 |
| RENKO_2x_2 | −0.33 / −0.34 / −0.69 | +0.05 / +0.04 / −0.02 | 2.3 (SELECT) | – |
| (0) Keluar kaedah sendiri (`trade_ret`) | −0.53 / −0.50 / −0.77 | −0.16 / −0.11 / −0.09 | −5.7 / −3.7 / −2.6 | −14.38 |

Keluar kaedah sendiri: hari pegang 30.1 dan 5% terburuk −14.38 dalam SELECT. Ekor kirinya lebih baik daripada CH4, tetapi lebihannya lebih rendah. Sumber: `jadual.md` "K … t60"; `lulus.json` kunci `K|…`.

Had 120 hari (U), lebihan SPY sebulan SELECT / VALIDATE-B / VALIDATE-T:

| Peraturan | Lebihan SPY sebulan (%) | t SELECT | 5% terburuk SELECT (%) | Hari |
|---|---|---|---|---|
| CH4 | −0.20 / −0.27 / −0.80 | – | −16.14 | 46.3 |
| CH5 | −0.12 / −0.21 / −0.74 | – | – | – |
| KAGI5 | −0.13 / −0.19 / −0.78 | 4.1 | −20.82 | 68.7 |
| RENKO_2x_2 | −0.13 / −0.20 / −0.79 | 4.0 | −20.01 | – |

Semua calon lain kalah kepada CH4 atau setara dengannya. Ekor kiri KAGI5 lebih buruk 4.7 mata, jadi (c) masih gagal. Sumber: `jadual.md` "U … t120".

Ikut tahun masuk (U, A+B, had 60), lebihan SPY sebulan CH4:

| Tahun | CH4 (%) |
|---|---|
| 2013 | +0.20 |
| 2014 | −0.76 |
| 2015 | −0.74 |
| 2016 | −0.13 |
| 2017 | −0.43 |
| 2018 | −0.70 |
| 2019 | −0.84 |
| 2020 | +1.85 |
| 2021 | −1.65 |
| 2022 | −0.62 |
| 2023 | −1.28 |
| 2024 | −1.00 |
| 2025 | −0.08 |
| 2026 | −1.04 (sebahagian masih terbuka) |

- KAGI5 dan RENKO_2x_2 lebih baik daripada CH4 dalam kebanyakan tahun, dengan beza ≤ 0.22 mata.
- Kedua-duanya lebih buruk dalam 2019, 2023, 2025 dan 2026, dengan beza ≤ 0.11 mata (KAGI5 2023: −1.39).
- HA2 negatif dalam setiap tahun, termasuk 2020 (−1.16).

Sumber: `jadual.md` "Tahun t60".

### Inferences
- Atas kolam ini (30 kaedah RENDAH/GUNA, 2000 saham AS, 2013–2026), lorong 2 CH4 tidak mengatasi SPY: −0.30 hingga −0.80% sebulan. Ini berbeza daripada +1.2% atas set 431 dalam [KAJIAN_LORONG2](../../KAJIAN_LORONG2.md).
  - Kedua-dua kajian bersetuju pada satu perkara: lebihan tertumpu pada tahun trend kuat (2020; 2025 hampir sifar di sini).
  - Penjelasan yang mungkin ialah set 431 mempunyai bias pemilihan dan bias penyintas, manakala kolam ini lebih luas dan mengandungi kaedah lemah. Kesimpulan ini tidak diuji di sini.
- Lorong 2 CH4 tetap lebih baik daripada keluar kaedah sendiri secara purata (t −5.7 SELECT). Oleh itu, dapatan lorong 2 lawan lorong 1 dalam KAJIAN_LORONG2 kekal sah pada universe lebih luas, walaupun dengan kos ekor kiri lebih buruk (−16.89 lawan −14.38).

### Gaps
- Pulangan SPY bagi garis dasar (0) yang keluar dengan henti atau sasaran intrahari (bukan pada buka) dianggarkan dengan tutup SPY hari keluar. Kesannya pada lebihan sebulan dijangka kecil, tetapi tidak diukur.
- Kolam ini mewarisi had data AUTOTUNE: harga yfinance terlaras dan tiada data intrahari. Tahap bias penyintas dalam saham yang dinyahsenarai tidak disemak di sini.

## Soalan 4: Adakah pelaksanaan Chandelier 4× sepadan dengan `standard/keluar_lorong.py`, dan apakah butiran pelaksanaannya?

### Takeaway
Ya. CH4 tanpa had dalam skrip ini sepadan dengan `keluar_lorong.lorong_henti` bagi **3,000 / 3,000** kemasukan rawak. Padanan merangkumi bar keluar, harga keluar dan jenis keluar.

### Cited Findings
- Semakan: `uji_lorong3.py semak --n 3000`, dengan benih rawak 20261022.
  - Untuk setiap kemasukan, ATR dikira dengan `keluar_lorong.atr` atas sejarah penuh ticker.
  - Padanan dikira apabila bar keluar dan harga buka sama, atau apabila `menunggu`/`terbuka` sepadan dengan tutup terakhir dalam sim.
  - Hasil `{"n": 3000, "sama": 3000}`. Sumber: `semak.json`.
- Set kemasukan:
  - U = 741,341 kemasukan unik dan K = 970,627 dagangan laluan 1. Semua kemasukan mempunyai A0 (ATR14 bar k−1); 0 dikecualikan.
  - Tiada tutup NaN dalam 9,973,939 bar (3,194 ticker). Sumber: `sim.log`.
- Hari pegang garis dasar (0) yang dikira semula sebagai J−k+1 sama dengan `hold_days` kolam bagi 100% dagangan. Sumber: `hasil.json` `semak_hari_kaedah_sama_kolam = 1.0`.
- Butiran pelaksanaan yang tidak dinyatakan secara eksplisit dalam pradaftar (tafsiran, bukan pindaan):
  - Garis dasar (0): harga keluar = e × (1+trade_ret)(1+kos)/(1−kos). SPY diukur ke buka hari keluar jika `exit_reason = isyarat keluar` atau jika harga keluar = buka hari itu (gap henti). Bagi kes lain, SPY diukur ke tutup.
  - Isyarat pada bar terakhir data, atau tiada keluar sebelum data tamat: dinilai pada tutup terakhir.
  - SHA20: bar j−1 boleh jadi bar k−1, jadi pertukaran hijau → merah pada bar k sendiri dikira.
  - HA2/HA3: kiraan merah bermula dari bar k.
  - t: kaedah delta atas nisbah purata(lebihan)/purata(hari), dengan sumbangan setiap dagangan dijumlahkan ikut tarikh masuk (G/(G−1) × Σ kelompok²). Bagi K, versi berpemberat digunakan.
  - Kuantil (median, 5%) bagi K ialah kuantil berpemberat.

### Inferences
- Oleh sebab CH4 dalam skrip sepadan sepenuhnya dengan peraturan lorong 2 yang digunakan dalam Papertrade C dan Lejar, semua beza yang dilapor di atas ialah beza peraturan keluar, bukan beza pelaksanaan.

### Gaps
- Tiada.

## Kesimpulan untuk keputusan

**GAGAL. Tiada keluar carta alternatif (Heikin-Ashi, HA dilicinkan, Renko, Kagi, Point & Figure, Line Break) mengatasi Chandelier tutup 4×ATR14 di bawah peraturan pradaftar.** Lorong 2 kekal seperti sekarang.

- **Renko 2×ATR dan Kagi 5×ATR**: menang kecil (+0.03 hingga +0.06 mata % sebulan) hanya kerana lebih longgar. Kedua-duanya terletak pada sempadan CH4–CH5, dengan ekor kiri lebih buruk 2.7–4.8 mata.
- **Line Break dan HA mentah**: memotong pemenang terlalu awal.
- **HA dilicinkan dan P&F**: tidak dapat dibezakan daripada CH4.

Jika pengguna mahu memegang lebih lama, pilihan yang sama berkesan dan lebih mudah ialah gandaan Chandelier 5×, bukan carta alternatif. CH5 sendiri juga gagal syarat ekor kiri berbanding CH4 (−2.15 mata dalam SELECT).
