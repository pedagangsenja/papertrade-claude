# Kajian portfolio modal terhad 10 slot (19 Okt 2026)

Permintaan pengguna 19 Okt 2026: Papertrade C membeli setiap isyarat (~800 sehari, 1 unit). Dengan modal sebenar 10 slot
(10% ekuiti setiap satu), isyarat mana patut diambil apabila isyarat lebih banyak daripada slot kosong?
Skrip: `kajian/portfolio/kaji_portfolio.py` (`sedia`, `semak`, `sim`, `ringkas`, `tahan`). Hasil: `kajian/portfolio/keputusan.csv`,
`ketahanan.csv`, `tahunan.csv`. Kajian ini rekod sahaja; tiada peraturan papertrade diubah.

## Data dan kaedah
- Calon: 763,327 dagangan enjin v1.2 bagi 134 kaedah (set 431, `data_mentah`; dijana `kajian/lorong2/kaji_lorong2.py jana`,
  bilangan sama dengan kajian lorong 2). Lapan saham dengan peristiwa korporat tidak terlaras dibuang (ASST, FCEL, MTDR, OVV, PR,
  SM, VAL, XENE; LAPORAN_UTAMA §10), jadi alam ujian ialah 423 saham. Larian pertama yang belum membuang lapan saham ini
  meletakkan ASST, FCEL dan PR antara penyumbang untung teratas.
- Tempoh portfolio: masuk 2 Nov 2020 – 2 Okt 2026. Dagangan sejak Nov 2019 hanya digunakan sebagai sejarah skor kaedah
  walk-forward. H1 = Nov 2020 – Okt 2023, H2 = Nov 2023 – Okt 2026.
- Portfolio: 10 slot. Saiz posisi = min(tunai, ekuiti semalam × 10%). Satu posisi sahaja bagi setiap saham. Masuk pada buka
  hari selepas isyarat. Kos 0.1% setiap belah. Logik sama dengan `enjin.portfolio` v1.2; semakan (`semak`, 8 slot, M03/M27/M119)
  menunjukkan beza CAGR ≤ 0.5 mata.
- Cara keluar: L1 = peraturan kaedah (enjin). L2 = Chandelier tutup 4×ATR14, paras hanya naik, tanpa henti kaedah (lorong 2 semasa).
- Peraturan pemilihan: setiap pagi, isyarat disusun ikut skor tertinggi. Semua skor diambil pada tutup hari isyarat (tiada
  pandang hadapan), kecuali yang ditanda rujukan.
  - Konsensus: bilangan kaedah yang memberi isyarat bagi saham dan tarikh sama.
  - RS pasaran: `kajian/rs/rs_pasaran_431.csv.gz`, RS lawan seluruh pasaran AS.
  - RS disahkan dahulu: RS ≥ 80 dan disahkan diutamakan; syarat sah ikut `gred.py`, iaitu naik 12 bulan, Mansfield > 0 dan
    SPY > SMA200.
  - Industri v2: skor `gred_kumpulan.py` dibina semula daripada `kumpulan_harian.csv.gz`, cawangan `kajian-gred`.
  - Kaedah walk-forward: purata lebihan SPY dagangan kaedah itu yang sudah keluar dalam 12 bulan sebelum isyarat (≥ 10 dagangan).
  - Momentum 6 bulan.
  - ATR14% rendah atau tinggi.
  - Gabungan: purata pangkat persentil kaedah walk-forward, RS, Industri dan konsensus.
  - Kaedah statik (rujukan sahaja, ada pandang hadapan): purata lebihan kaedah atas seluruh tempoh.
- Rawak: susunan rawak, 30 benih. Persentil sesuatu peraturan = % benih rawak yang dikalahkannya bagi CAGR, H1 dan H2.
- Penanda aras dalam tempoh sama: SPY CAGR 16.9% (MDD −24.5%). Beli dan pegang sama rata 423 saham CAGR 26.3% (MDD −27.6%).

## Keputusan (10 slot, tanpa penapis rejim; persentil lawan rawak CAGR/H1/H2)
| Peraturan | L1 CAGR % | L1 MDD % | L1 persentil | L2 CAGR % | L2 MDD % | L2 persentil |
|---|---|---|---|---|---|---|
| Rawak (median 30 benih) | 23.8 | −30.9 | – | 24.5 | −30.5 | – |
| Konsensus kaedah | 25.0 | −32.0 | 53/13/80 | 21.2 | −31.4 | 33/37/33 |
| RS pasaran | 78.0 | −45.4 | 100/100/100 | 72.6 | −48.6 | 100/100/100 |
| RS disahkan dahulu | 75.9 | −50.3 | 100/100/100 | 78.3 | −46.5 | 100/100/100 |
| Industri v2 | 22.1 | −38.5 | 37/67/37 | 32.0 | −35.8 | 80/77/80 |
| Kaedah walk-forward 12 bulan | 31.5 | −37.1 | 87/3/97 | 23.3 | −27.5 | 43/73/33 |
| Momentum 6 bulan | 54.0 | −48.0 | 100/97/100 | 58.6 | −42.1 | 100/97/93 |
| Volatiliti rendah | 7.2 | −19.8 | 0/33/0 | 7.5 | −20.2 | 0/7/10 |
| Volatiliti tinggi | 74.3 | −56.8 | 100/93/100 | 78.0 | −58.3 | 100/97/100 |
| Gabungan | 25.2 | −33.3 | 53/80/40 | 26.7 | −27.9 | 63/83/40 |
| Kaedah statik (pandang hadapan, rujukan) | 33.1 | −31.5 | 87/93/63 | 40.1 | −39.9 | 93/70/93 |

- Isyarat yang dipilih secara rawak (23.8–24.5%) tidak mengatasi beli dan pegang sama rata 423 saham (26.3%), dan MDD-nya lebih
  dalam. Pada peringkat portfolio 10 slot, isyarat kaedah sendiri tidak menambah nilai. Nilai hanya datang daripada cara memilih.
- Memilih kaedah "terbaik" bukan sumber nilai utama. Kaedah statik, yang melihat keputusan masa depan, hanya mencapai 33–40%.
  Kaedah walk-forward tidak stabil: persentil H1 3 lawan H2 97 (L1).
- Penapis rejim SPY > SMA200 (larian berasingan) menurunkan CAGR rawak (L2 24.5% → 14.6%; L1 23.8% → 15.5%) tanpa mengurangkan
  MDD (L2 −33.7% lawan −30.5%), jadi ia tidak dicadangkan.
- Bilangan slot (L2): dengan 5 slot hasil sangat bergantung nasib (rawak p5–p95 6.9–52.7%). Dengan 20 slot hasil lebih stabil
  (rawak 25.8%, MDD −28.3%; RS 57.1%, MDD −42.5%).

## Ketahanan: bias set 431
Set 431 ialah senarai Shariah hari ini. Saham yang jatuh teruk atau dinyahsenarai sejak 2019 tiada dalam set, dan pemenang
besarnya sudah diketahui. Kajian RS seluruh pasaran (`kajian/rs/RINGKASAN.md` §11) menunjukkan lebihan RS 95–99 dalam set 431
= +2.05% setiap 21 hari (t 4.65), lawan +0.39% (t 1.15) bagi saham lain, iaitu kira-kira 5 kali ganda. Ujian `tahan` membuang
20 atau 40 saham dengan pulangan tertinggi 2020–2026 (dipilih dengan pandang hadapan: AEHR, CLS, SNDK, WFRD, MOD, BE, MU, DELL,
BTU, SMCI, NVDA …), kemudian mengulang simulasi (rawak 20 benih).

| Peraturan (CAGR %; persentil CAGR/H1/H2) | L2 buang 0 | L2 buang 20 | L2 buang 40 | L1 buang 0 | L1 buang 20 | L1 buang 40 |
|---|---|---|---|---|---|---|
| Beli dan pegang sama rata | 26.3 | 19.4 | 16.4 | 26.3 | 19.4 | 16.4 |
| Rawak (median) | 24.8 | 19.0 | 17.6 | 24.9 | 15.3 | 16.3 |
| **RS pasaran** | 72.6 (100/100/100) | 36.8 (100/95/95) | **30.7 (100/100/100)** | 78.0 (100/100/100) | 25.3 (90/95/80) | 17.1 (50/45/60) |
| Momentum 6 bulan | 58.6 (100/95/90) | 29.6 (90/95/85) | 16.8 (45/35/60) | 54.0 (100/100/100) | 23.9 (90/100/40) | 10.0 (15/10/20) |
| Volatiliti tinggi | 78.0 (100/95/100) | 45.8 (100/80/100) | 35.1 (100/60/100) | 74.3 (100/95/100) | 23.7 (90/30/95) | 36.6 (100/95/100) |
| Industri v2 | 32.0 (75/75/80) | 25.6 (85/90/60) | 21.7 (85/95/60) | 22.1 (35/70/35) | 22.6 (85/50/85) | 27.5 (100/95/90) |
| Kaedah walk-forward | 23.3 (40/70/30) | 18.9 (50/90/30) | 17.7 (50/80/35) | 31.5 (85/5/95) | 19.6 (65/95/30) | 17.6 (50/5/95) |
| Gabungan | 26.7 (60/80/35) | 31.1 (95/95/85) | 28.8 (100/100/95) | 25.2 (50/85/40) | 19.1 (65/65/75) | 19.4 (65/75/60) |

MDD (buang 40): RS L2 −33.1%, rawak L2 −30.6%, volatiliti tinggi L2 −51.9%, Gabungan L2 −31.2%. Tumpuan untung: 5 saham
teratas menyumbang 37–89% untung bersih dalam kebanyakan larian (RS L2 66% tanpa buang; volatiliti tinggi 89%).

- **RS dengan keluar L1**: kelebihan hilang sepenuhnya selepas 40 pemenang dibuang (17.1% lawan rawak 16.3%, persentil 50).
  Hasil ini bergantung pada pemenang yang sudah diketahui.
- **RS dengan keluar L2 (Chandelier)**: kekal 30.7% selepas 40 pemenang dibuang, lawan rawak 17.6% dan sama rata 16.4%, dengan
  persentil 100 dalam H1 dan H2, dan MDD hampir sama dengan rawak (−33% lawan −31%). Ini satu-satunya gabungan yang kekal jelas
  di atas rawak dalam semua ujian. Ia sepadan dengan dua kajian lain: kajian RS seluruh pasaran (kelebihan RS 90+ wujud tetapi
  kecil) dan kajian lorong 2 (Chandelier membiarkan trend berkembang).
- Momentum 6 bulan runtuh selepas 40 pemenang dibuang (bias).
- Volatiliti tinggi kekal tinggi tetapi MDD −52% hingga −58%. Ia paling terdedah kepada bias, kerana saham volatil yang gagal
  tiada dalam set. Tidak sesuai untuk modal sebenar.
- Industri v2 dan Gabungan sederhana dan tidak konsisten antara ujian.

## Cadangan (rekod sahaja; perlu bukti hadapan sebelum modal sebenar)
**10 slot RS + Chandelier:**
- Setiap pagi, daripada senarai beli (isyarat 100% semua kaedah), isi slot kosong dengan saham yang RS pasarannya tertinggi.
- Satu posisi bagi setiap saham, saiz 10% ekuiti.
- Keluar ikut lorong 2 (Chandelier tutup 4×ATR14, paras naik, tanpa henti kaedah). Tiada penapis rejim.
- Dalam set penuh: ~55 belian setahun (~1 seminggu), pegang purata 47 hari, kadar menang 48%, purata +14.8% setiap dagangan.
- Jangkaan realistik jauh di bawah CAGR backtest 72.6%. Selepas 40 pemenang dibuang, CAGR 30.7% dan MDD −33%, dan bias
  kemandirian baki set masih ada. Bersedia untuk MDD −35% hingga −50%.
- Langkah seterusnya ialah jejak hadapan dalam papertrade, yang mengimbas seluruh pasaran AS secara langsung dan oleh itu
  tiada bias kemandirian. Rekod dua portfolio maya 10 slot: RS + Chandelier, dan rawak sebagai kawalan. Nilai selepas
  sekurang-kurangnya 6–12 bulan.

## Jejak hadapan (dilaksanakan 19 Okt 2026, keputusan pengguna)
`standard/portfolio_slot.py` (ujian `ujian/test_portfolio_slot.py`), dijalankan oleh `lejar.yml` setiap malam selepas Lejar Penuh.
Ia membina semula dua portfolio maya daripada posisi lejar, iaitu isyarat 100% semua kaedah atas seluruh alam Shariah ≥ USD10:
- RS_10: slot kosong diisi dengan RS pasaran tertinggi (`data/rs/rs_pasaran.csv`, tarikh isyarat).
- RAWAK_10: susunan rawak tetap (benih = tarikh beli), sebagai kawalan.
Peraturan sama dengan kajian: 10% ekuiti, satu posisi setiap saham, keluar lorong 2, kos 0.1%. Mula 16 Okt 2026 (sesi beli
pertama lejar). Hasil dalam `BacktestShariah2/portfolio_slot/`: `RINGKASAN.md`, `<portfolio>_posisi.csv`, `<portfolio>_ekuiti.csv`
(lajur `spy` = SPY dinormalkan pada buka hari pertama).

## Batasan
- Bias kemandirian set 431: ujian buang pemenang hanya mengurangkannya, tidak menghapuskannya.
- Kaedah sendiri dibina dan ditapis dengan melihat data 2019–2026 (dalam sampel).
- Peta industri ialah peta semasa (`papertrade/peta_industri.csv`), bukan peta sejarah. RS dan industri tiada data bagi ~4% calon
  (diisi neutral 50).
- Tiada had kecairan atau slippage selain kos 0.1%. Masuk pada harga buka.
- Satu tempoh sahaja (Nov 2020 – Okt 2026), yang termasuk ledakan semikonduktor/AI 2023–2026. Persentil rawak bersifat kasar
  (30 benih; 10 bagi 5/20 slot; 20 dalam ujian ketahanan).

## Ujian luar sampel (saham bukan set 431, 2011–2026)
Soalan (19 Okt 2026): adakah peraturan pemilihan di atas, terutama RS pasaran + Chandelier, masih mengatasi rawak apabila
alamnya bukan set 431 (senarai Shariah hari ini yang dipilih dengan melihat pemenang) dan tempohnya lebih panjang, termasuk
2011–2019 sebelum kaedah-kaedah ini direka? Skrip `kajian/portfolio_luar/kaji_luar.py`, dijalankan oleh GitHub Actions
`kajian_portfolio_luar.yml` (sesi Claude tidak boleh capai Yahoo): tarik data → matriks 10 kerja dagangan 134 kaedah →
gabung (ciri, simulasi). Hasil: `kajian/portfolio_luar/` (`keputusan.csv`, `penanda.csv`, `ketahanan.csv`, `tahunan.csv`,
`dagangan_rs.csv`, `meta.json`) dan kawalan `kajian/portfolio_luar/kawalan_431/`. Enjin portfolio, metrik, skor kaedah
walk-forward dan peraturan diimport daripada `kaji_portfolio.py` tanpa ubah. Data harga dan dagangan hanya artifact Actions.

### Data dan kaedah
- Alam luar: saham dalam `data/skrin/tv_us.csv` tolak set 431, tolak simbol pelik (757: ETF, dana, saham keutamaan/depositari,
  waran, hak, unit, SPAC "Acquisition", nota/debentur, simbol dengan `/`). yfinance 2009-01-02 hingga 2026-10-16
  (`auto_adjust=False`: terlaras pecahan, tidak terlaras dividen), OHLCV, `turnover` = tutup × volum; SPY dan QQQ untuk `idx`.
  2,998 saham dimuat turun, 0 gagal; 208 dibuang (lonjakan sehari `kajian_rs.bersih` > 5 kali, OHLC tidak konsisten > 1% bar,
  atau < 300 bar) → 2,790 saham.
- Calon: dagangan enjin v1.2 semua 134 kaedah (`sedia` setiap kaedah, `enjin.trades`; kaedah silang merentas seluruh alam
  luar). Isyarat layak hanya jika tutup hari isyarat ≥ USD10 (seperti lejar) dan purata nilai dagangan 50 hari ≥ USD5 juta:
  5,364,868 dagangan atas 2,407 saham; 5,102,357 calon masuk sejak 3 Jan 2011 (dagangan 2009–2010 hanya sejarah skor
  walk-forward). L1 = keluar kaedah, L2 = Chandelier tutup 4×ATR14 paras naik tanpa henti kaedah (`kaji_lorong2.sim`).
- RS pasaran dikira sendiri setiap hari (formula `kajian_rs.py`: 40% r63 + 20% tiga suku sebelumnya, persentil 1–99 antara
  semua saham yang dimuat turun termasuk set 431, tutup ≥ USD5 dan ≥ 253 bar), nilai hari isyarat sahaja; liputan 97.4%.
  Industri v2 dan Gabungan tiada (tiada gred industri sejarah bagi alam ini).
- Portfolio 10 slot seperti di atas (saiz min(tunai, ekuiti semalam × 10%), satu posisi setiap saham, masuk buka esok, kos 0.1%
  setiap belah). Tempoh 3 Jan 2011 – 16 Okt 2026; era 1 = 2011–2019 (sebelum kaedah direka), era 2 = 2020–2026. Rawak 30 benih
  (20 dalam ujian buang pemenang); persentil = % benih rawak yang dikalahkan bagi CAGR/era 1/era 2.
- Penanda aras: SPY; beli dan pegang sama rata saham layak pada 3 Jan 2011 (690 saham); sama rata saham layak imbang semula
  setiap 21 hari (purata 1,211 saham; saham tersenarai kemudian masuk apabila layak).
- Kawalan: semuanya diulang atas set 431 dengan data yfinance dan tempoh yang sama (422 saham; 1,368,811 dagangan), supaya
  beza alam tidak dikelirukan oleh beza sumber data atau tempoh.

### Keputusan alam luar (10 slot; persentil lawan rawak CAGR/era 1/era 2)
| Peraturan | L1 CAGR % | L1 MDD % | L1 era 1/era 2 % | L1 persentil | L2 CAGR % | L2 MDD % | L2 era 1/era 2 % | L2 persentil |
|---|---|---|---|---|---|---|---|---|
| Rawak (median 30 benih; p5–p95 L1 −2.8–7.1, L2 1.1–9.8) | 2.2 | −52.9 | 4.7/−1.3 | – | 4.9 | −48.8 | 8.4/1.7 | – |
| Konsensus kaedah | −0.6 | −56.4 | 6.4/−9.2 | 13/73/7 | 4.1 | −49.3 | 4.3/3.8 | 40/7/60 |
| RS pasaran | 3.8 | −73.7 | −0.0/9.1 | 63/0/87 | −6.2 | −87.0 | 2.3/−16.4 | 0/3/0 |
| RS disahkan dahulu | 4.6 | −64.4 | 8.0/0.3 | 67/90/57 | 1.4 | −72.7 | 5.0/−3.1 | 7/10/23 |
| Kaedah walk-forward 12 bulan | 6.2 | −55.7 | 8.1/3.7 | 90/93/77 | 1.1 | −56.3 | 5.4/−4.3 | 7/10/23 |
| Momentum 6 bulan | −11.4 | −90.1 | −8.5/−15.2 | 0/0/0 | −11.8 | −97.0 | 6.2/−31.0 | 0/23/0 |
| Volatiliti rendah | −3.2 | −60.4 | −0.9/−6.2 | 7/0/20 | 2.2 | −36.1 | 3.5/0.6 | 17/3/47 |
| Volatiliti tinggi | −9.1 | −89.5 | −7.3/−11.5 | 0/0/3 | −26.3 | −99.5 | −8.2/−44.8 | 0/0/0 |

| Penanda aras (tempoh sama) | CAGR % | MDD % | Era 1 % | Era 2 % |
|---|---|---|---|---|
| SPY | 12.0 | −34.1 | 10.9 | 13.6 |
| Beli dan pegang sama rata (690 saham layak 3 Jan 2011) | 9.3 | −39.3 | 10.2 | 8.1 |
| Sama rata saham layak, imbang semula 21 hari (purata 1,211 saham) | 8.9 | −42.4 | 10.0 | 7.4 |

- Dagangan yang diambil (10 slot): rawak L1 2,146 dagangan, menang 37%, purata +0.3%, pegang 19 hari; rawak L2 862, 41%,
  +1.4%, 47 hari. RS pasaran L1 2,005, 36%, +1.0%, 18 hari; RS pasaran L2 992, 36%, +0.2%, 41 hari. Kaedah walk-forward L1
  929, 36%, +1.9%, 44 hari. Volatiliti tinggi L2 1,041, 30%, −4.3%, 39 hari.
- Tiada satu pun peraturan, termasuk rawak, mencapai SPY (12.0%) atau sama rata (8.9–9.3%). Pemilihan rawak hanya 2.2% (L1) dan
  4.9% (L2) dengan MDD −49% hingga −53%: isyarat kaedah atas alam luar mengekori pasaran dengan lebihan SPY negatif setiap
  dagangan (−0.6% hingga −1.0%).
- RS pasaran + L2 ialah peraturan terburuk kedua: CAGR −6.2%, MDD −87%, persentil 0/3/0, dan di bawah rawak dalam kedua-dua era
  (era 1 2.3% lawan rawak 8.4%; era 2 −16.4% lawan 1.7%). Dengan L1 ia 3.8% (persentil 63), tetapi era 1 −0.0% (persentil 0)
  dan MDD −74%. 20 slot tidak membantu (RS L1 −0.7%, L2 −0.8%; rawak 2.9% dan 5.6%).
- Satu-satunya peraturan yang di atas rawak dalam kedua-dua era ialah Kaedah walk-forward 12 bulan dengan L1 (6.2%; persentil
  90/93/77), tetapi masih di bawah SPY dan sama rata, dan dengan L2 ia 1.1% (persentil 7). Momentum 6 bulan dan volatiliti
  tinggi musnah (MDD −90% hingga −99.5%). Volatiliti rendah + L2 ialah satu-satunya dengan MDD lebih cetek daripada SPY (−36%)
  tetapi CAGR 2.2%.
- Pulangan tahunan RS pasaran L2 (luar): 2013 +78%, 2016 −53%, 2019 +68%, 2024 +42%, 2025 −44%, 2026 −61%. Saham RS 95–99
  seluruh pasaran ialah saham lonjakan spekulatif (NVAX, CLDX, VKTX, RIOT, AXSM, GME, HYMC, CLSK): untung lima teratas 207%
  modal awal, rugi lima terbawah −67%, bersih −65%.

### Kawalan: set 431 dengan data dan tempoh yang sama
| Peraturan | L1 CAGR % | L1 MDD % | L1 era 1/era 2 % | L1 persentil | L2 CAGR % | L2 MDD % | L2 era 1/era 2 % | L2 persentil |
|---|---|---|---|---|---|---|---|---|
| Rawak (median 30 benih; p5–p95 L1 3.6–11.4, L2 6.3–14.1) | 7.6 | −43.5 | 4.8/12.6 | – | 10.0 | −39.7 | 7.5/14.2 | – |
| Konsensus kaedah | 10.1 | −37.0 | 4.6/17.9 | 73/50/87 | 16.2 | −34.7 | 10.0/25.1 | 100/83/100 |
| RS pasaran | 18.1 | −43.0 | 9.1/31.1 | 100/93/100 | 24.1 | −44.9 | 9.8/45.9 | 100/80/100 |
| RS disahkan dahulu | 18.9 | −45.4 | 9.0/33.5 | 100/93/100 | 25.8 | −45.2 | 12.0/46.9 | 100/97/100 |
| Kaedah walk-forward 12 bulan | 12.3 | −33.6 | 7.8/18.6 | 97/73/87 | 5.3 | −46.5 | 1.5/10.6 | 3/7/27 |
| Momentum 6 bulan | 15.1 | −46.1 | 9.1/23.5 | 100/93/97 | 24.0 | −44.4 | 15.1/36.8 | 100/100/100 |
| Volatiliti rendah | 4.7 | −33.2 | 6.8/2.0 | 10/70/0 | 7.5 | −24.2 | 9.7/4.6 | 20/80/3 |
| Volatiliti tinggi | 8.9 | −71.4 | 9.7/7.7 | 70/93/27 | 17.2 | −66.3 | 4.9/35.7 | 100/20/100 |

Penanda aras set 431 (tempoh sama): beli dan pegang sama rata 203 saham layak 3 Jan 2011 CAGR 10.2% (era 9.0/11.8), sama rata
imbang semula 21 hari 12.9% (9.8/17.2). Dagangan RS pasaran L2: 881, menang 42%, purata +6.3%, pegang 46 hari (lawan +0.2% dalam
alam luar). Dengan data dan kod yang sama, set 431 mengulang corak kajian asal: RS pasaran + L2 24.1% (persentil 100/80/100),
kekal 19.8% (100/100/100) selepas 100 pemenang terbesar dibuang (rawak 5.7%). Dalam era 1 (2011–2019, sebelum kaedah direka),
RS + L2 dalam set 431 masih 9.8% lawan rawak 7.5% (persentil 80), tetapi hampir sama dengan sama rata 9.0–9.8%.

### Ketahanan: buang 40 / 100 saham pulangan tertinggi 2011–2026 (alam luar; rawak 20 benih)
| Peraturan (CAGR %; persentil CAGR/era 1/era 2) | L2 buang 0 | L2 buang 40 | L2 buang 100 | L1 buang 0 | L1 buang 40 | L1 buang 100 |
|---|---|---|---|---|---|---|
| Rawak (median) | 5.0 | 4.6 | 3.6 | 1.9 | 2.6 | 2.0 |
| RS pasaran | −6.2 (0/5/0) | −1.1 (0/10/10) | −5.4 (0/0/0) | 3.8 (70/0/85) | −3.0 (0/90/0) | −12.7 (0/0/0) |
| Momentum 6 bulan | −11.8 (0/25/0) | −10.5 (0/30/0) | −4.6 (0/45/0) | −11.4 (0/0/0) | −17.4 (0/0/0) | −21.4 (0/0/0) |
| Volatiliti tinggi | −26.3 (0/0/0) | −26.4 (0/0/0) | −23.8 (0/0/0) | −9.1 (0/0/5) | −0.7 (15/40/35) | −14.1 (0/0/0) |

Pemenang yang dibuang (CELH, TSLA, IESC, PARR, PAYS, PATK, FIX, TPL, MPWR …) hampir tidak mengubah rawak (5.0% → 3.6%): dalam
alam luar, peraturan pemilihan tidak pernah bergantung pada pemenang besar; ia memilih saham lonjakan yang kemudian runtuh.
Kawalan set 431 pula: RS pasaran L2 24.1% → 18.8% (buang 40) → 19.8% (buang 100), persentil 100 dalam semua ujian; momentum
6 bulan 24.0% → 18.9% → 19.3%.

### Hasil setiap dagangan calon ikut gred RS pasaran hari isyarat (L2; purata % / lebihan SPY %)
| RS | Luar era 1 | Luar era 2 | Set 431 era 1 | Set 431 era 2 |
|---|---|---|---|---|
| 01–59 | +0.77 / −0.75 | +0.75 / −1.35 | +0.58 / −0.89 | +1.94 / +0.05 |
| 60–79 | +1.01 / −0.36 | +1.10 / −0.94 | +0.90 / −0.21 | +2.61 / +0.50 |
| 80–89 | +1.29 / −0.19 | +1.58 / −0.65 | +0.67 / −0.26 | +3.02 / +0.79 |
| 90–94 | +1.22 / −0.19 | +2.43 / −0.05 | +1.49 / +0.29 | +4.16 / +2.45 |
| 95–99 | +0.32 / −0.86 | −0.17 / −2.56 | +2.16 / +0.77 | +6.99 / +5.61 |

Dalam alam luar, RS 95–99 ialah gred terburuk (median −5.0% dan −8.6%, menang 33–36%), dan tiada gred yang mengatasi SPY;
RS 90–94 sedikit lebih baik daripada gred rendah tetapi masih di bawah SPY. Dalam set 431, hasil naik secara monoton dengan RS
dalam kedua-dua era, dan gred 95–99 paling baik (+7.0% setiap dagangan era 2). Ini sepadan dengan `kajian/rs/RINGKASAN.md` §1
dan §11 (RS 95–99 seluruh pasaran: median ≈ 0; lebihan dalam set 431 ≈ 5 kali ganda saham lain).

### Kesimpulan
- **RS pasaran + Chandelier tidak mengatasi rawak di luar set 431.** Atas 2,790 saham AS bukan set 431, 2011–2026, ia CAGR
  −6.2%, MDD −87%, persentil 0 lawan rawak dalam CAGR dan kedua-dua era, dan kekal di bawah rawak dalam semua ujian buang
  pemenang. Ia juga tidak mengatasi sama rata (8.9–9.3%) mahupun SPY (12.0%).
- **Tiada peraturan konsisten merentas kedua-dua era** kecuali Kaedah walk-forward 12 bulan dengan keluar L1 (persentil
  90/93/77), dan itupun CAGR 6.2%, di bawah sama rata dan SPY. Dengan L2 ia gagal (persentil 7).
- **Beza alam, bukan beza data atau tempoh.** Dengan data yfinance dan tempoh yang sama, set 431 mengulang corak kajian
  asal (RS + L2 24.1%, persentil 100, tahan buang 100 pemenang). Kelebihan RS yang dilaporkan di atas ialah sifat senarai
  431 (saham berkualiti yang dipilih pada 2026 dengan melihat hasilnya; RS tinggi dalam senarai itu ialah pemenang berkualiti),
  bukan sifat RS secara umum: dalam seluruh pasaran, RS 95–99 ialah saham lonjakan spekulatif yang purata hasilnya negatif.
- **Isyarat kaedah sendiri tidak menambah nilai di luar set 431**: walaupun alam ini mempunyai bias kemandirian yang
  menguntungkan (hanya saham yang masih tersenarai hari ini), pemilihan rawak daripada isyarat 134 kaedah hanya 2–5% setahun
  dengan MDD −50%, jauh di bawah beli dan pegang alam yang sama.
- Cadangan "10 slot RS + Chandelier" di atas tidak mempunyai bukti luar set 431. Jejak hadapan RS_10 lawan RAWAK_10
  (`portfolio_slot/`) mengimbas alam Shariah ≥ USD10 yang lebih luas daripada set 431; hasilnya perlu dibaca dengan jangkaan
  bahawa RS 95–99 seluruh pasaran bukan kelebihan. Tiada peraturan papertrade diubah.

### Bias dan batasan yang masih ada
- yfinance tiada saham yang sudah dinyahsenarai: alam = senarai hari ini (bias kemandirian memihak kepada semua strategi, namun
  hasilnya tetap lemah). Saham yang muflis atau diambil alih sebelum 2026 tiada.
- Harga tidak terlaras dividen/pecahan korporat: dividen khas dan pemisahan (spin-off) kelihatan sebagai jatuh harga, yang
  merugikan posisi L2 dan penanda aras beli-pegang sama-sama. Penapis ≥ USD10 memakai harga terlaras pecahan, jadi tempoh
  sebelum pecahan songsang boleh lulus penapis.
- Alam tv_us.csv ialah saham AS semasa dengan tapisan simbol pelik berdasarkan nama (757 dibuang); 208 saham dibuang kerana data
  rosak atau pendek. RS dipangkat antara 3,212 saham yang dimuat turun, bukan ~3,800 seperti `kajian_rs.py`.
- Kaedah-kaedah dibina atas set 431 2019–2026; era 1 (2011–2019) benar-benar di luar masa, era 2 bertindih dengan tempoh
  reka bentuk. Tiada gelinciran selain kos 0.1%; persentil rawak kasar (30 benih; 20 dalam ujian buang pemenang).
