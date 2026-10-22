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
