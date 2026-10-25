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

**Isu diketahui RS_10 (audit 25 Okt 2026; tidak diubah kerana eksperimen beku).** RS pasaran ialah integer, jadi seri kerap.
`portfolio_slot.susun` mengisih calon ikut saham, kemudian isihan stabil ikut RS menurun, jadi seri dipecah ikut **abjad saham**.
Pada 16 Okt 2026 ada 5 calon RS 99 dan 9 calon RS 98; RS_10 mengambil kesemua RS 99 dan lima RS 98 pertama ikut abjad (AGL, AUGO,
BAND, BUUU, GRAL), manakala MU, MXL, SAIH dan TEAM tercicir kerana abjad sahaja. Semua 10 slot juga diisi pada sesi pertama.
Kajian dalam sampel memecah seri secara rawak (`bunyi` berbenih), jadi jejak hadapan RS_10 tidak sama tepat dengan peraturan yang
diuji. PLAYBOOK_10 (di bawah) memecah seri secara rawak berbenih dan menghadkan 3 belian sehari.

## Batasan
- Bias kemandirian set 431: ujian buang pemenang hanya mengurangkannya, tidak menghapuskannya.
- Kaedah sendiri dibina dan ditapis dengan melihat data 2019–2026 (dalam sampel).
- Peta industri ialah peta semasa (`papertrade/peta_industri.csv`), bukan peta sejarah. RS dan industri tiada data bagi ~4% calon
  (diisi neutral 50).
- Tiada had kecairan atau slippage selain kos 0.1%. Masuk pada harga buka.
- Satu tempoh sahaja (Nov 2020 – Okt 2026), yang termasuk ledakan semikonduktor/AI 2023–2026. Persentil rawak bersifat kasar
  (30 benih; 10 bagi 5/20 slot; 20 dalam ujian ketahanan).

## Rangka risiko: PLAYBOOK_10 lawan RAWAK_PADAN_10 (25 Okt 2026; dalam sampel)

> **Amaran.** Semua angka di bawah ialah **dalam sampel** atas **alam penyintas** (set 431 = senarai Shariah hari ini; saham yang
> jatuh atau dinyahsenarai sejak 2019 tiada). Kaedah sendiri juga dibina atas data yang sama. Set "buang 40 pemenang" hanya
> mengurangkan bias ini. Angka ini bukan jangkaan pulangan hadapan.

Peraturan dipra-daftar sebelum ujian: `kajian/portfolio/PRA_DAFTAR_PLAYBOOK.md` (commit `5be8cf2`). Ujian memakai enjin yang sama
dengan jejak hadapan (`standard/portfolio_slot.bina_pb`, penapis `tapis_pb`). Skrip: `kaji_portfolio.py playbook`. Hasil:
`playbook.csv` (setiap larian), `playbook_ringkas.csv`, `playbook_tahunan.csv`, `playbook_corong.csv`, `mdd_jangka.json`.
Calon = 284,102 pasangan saham × sesi masuk daripada 763,327 dagangan enjin (Nov 2020 – Okt 2026). 7.75% lulus semua penapis;
81% sesi ada sekurang-kurangnya satu calon lulus (median 15 sesehari, p90 28). Pecahan calon yang gagal setiap penapis (tidak
eksklusif): RS 80–94 79.7%, Trend Template 67.9%, industri E 17.2%, rejim SPY 16.3%, kecairan 14.1%, earnings 11.2% (1.8% tidak
diketahui), ATR14% 7.7%, harga 7.4%, jurang 2.9%, sejarah 1.5%, semak data 0.4%. Penanda aras tempoh sama: SPY CAGR 16.9% (MDD
−24.5%); sama rata 423 saham 26.3% (MDD −27.6%).

### Keputusan (median 20 benih; p5–p95; PLAYBOOK = 20 benih pecah seri, RAWAK_PADAN = 20 benih susunan)
| Portfolio | Set | CAGR % | MDD % (p5) | MAR | CAGR H1 / H2 % | Heat median / p90 % | Tunai % | Posisi purata | Dagangan |
|---|---|---|---|---|---|---|---|---|---|
| **PLAYBOOK_10, pra-daftar** | penuh | 4.6 (1.4–8.4) | −17.4 (−19.1) | 0.26 | 8.3 / 0.0 | 0.0 / 9.8 | 64 | 4.8 | 279 |
| **RAWAK_PADAN_10, pra-daftar** | penuh | 4.0 (1.7–9.5) | −16.6 (−18.6) | 0.23 | 7.2 / 0.0 | 0.0 / 9.4 | 68 | 4.1 | 253 |
| PLAYBOOK_10, pra-daftar | buang 40 | 5.3 (3.1–7.2) | −17.1 (−18.5) | 0.32 | 10.5 / 0.0 | 0.0 / 9.6 | 65 | 4.7 | 276 |
| RAWAK_PADAN_10, pra-daftar | buang 40 | 3.4 (1.9–5.1) | −16.6 (−18.3) | 0.20 | 6.9 / 0.0 | 0.0 / 9.4 | 73 | 3.5 | 220 |
| PLAYBOOK_10 tanpa brek/kill_switch * | penuh | 18.5 (11.7–23.7) | −21.8 (−25.2) | 0.82 | 8.3 / 28.5 | 8.7 / 10.8 | 22 | 10.6 | 653 |
| RAWAK_PADAN_10 tanpa brek/kill_switch * | penuh | 12.3 (5.3–17.1) | −21.3 (−27.5) | 0.58 | 7.0 / 16.2 | 8.3 / 10.3 | 18 | 11.0 | 693 |
| PLAYBOOK_10 tanpa brek/kill_switch * | buang 40 | 11.5 (9.1–14.8) | −21.7 (−27.3) | 0.53 | 11.0 / 13.2 | 8.5 / 10.4 | 21 | 10.8 | 681 |
| RAWAK_PADAN_10 tanpa brek/kill_switch * | buang 40 | 8.0 (4.4–11.6) | −22.9 (−26.5) | 0.33 | 4.6 / 11.2 | 8.1 / 10.2 | 18 | 11.0 | 703 |
| PLAYBOOK_10 brek lengkung bayang * | penuh | 13.7 (−0.9–20.0) | −22.8 (−26.3) | 0.61 | 8.3 / 19.6 | 8.1 / 10.7 | 35 | 8.4 | 518 |
| RS_10 rujukan (RS pasaran 10 × 10%, lorong 2, kos 0.1%) | penuh | 72.7 (62.5–76.3) | −48.0 (−50.5) | 1.50 | 47.5 / 102.5 | – | – | 10.0 | 321 |
| RAWAK_10 rujukan (rawak 10 × 10%, kos 0.1%) | penuh | 24.8 (12.5–44.9) | −31.5 (−39.7) | 0.84 | 17.7 / 34.0 | – | – | 10.0 | 351 |
| RS_10 rujukan, kos 0.25% | penuh | 70.3 | −48.3 | 1.44 | 45.7 / 99.6 | – | – | 10.0 | 321 |
| RS_10 rujukan (kos 0.1% / 0.25%) | buang 40 | 28.5 / 26.5 | −33.5 / −34.3 | 0.84 / 0.77 | 20.2 / 37.7 | – | – | 10.0 | 344 |
| RAWAK_10 rujukan (kos 0.1% / 0.25%) | buang 40 | 17.6 / 15.8 | −30.6 / −31.9 | 0.57 / 0.49 | 12.0 / 22.7 | – | – | 10.0 | 347 |

\* Analisis kepekaan, **bukan peraturan pra-daftar**: "tanpa brek/kill_switch" = peraturan sama tanpa K4; "brek lengkung bayang" =
brek 15%/pulih −10% dinilai pada lengkung portfolio sama tanpa brek (kill_switch kekal pada ekuiti sebenar).
Heat dikira pada tutup (had 10% dikenakan semasa beli; heat boleh naik apabila harga naik menjauhi paras keluar).

Persentil PLAYBOOK_10 benih 0 lawan 20 benih RAWAK_PADAN_10 (CAGR / H1 / H2 / MAR / MDD lebih cetek): pra-daftar penuh
100 / 100 / 85 / 100 / 70 (CAGR 11.0%, MDD −16.2%); pra-daftar buang 40 100 / 100 / 95 / 95 / 0 (6.6%, −18.9%); tanpa brek penuh
100 / 100 / 95 / 100 / 45 (23.6%, −21.6%); tanpa brek buang 40 95 / 100 / 60 / 95 / 85 (12.6%, −20.6%). Merentas semua pasangan
benih (tanpa brek), PLAYBOOK mengatasi RAWAK_PADAN dalam 88% (penuh) dan 89% (buang 40) pasangan. H2 pra-daftar hampir sifar
kerana portfolio berhenti membeli (persentil H2 tidak bermakna).

R-multiple (dagangan keluar + terbuka di hujung pada tutup akhir; R = harga beli − paras Chandelier awal): PLAYBOOK pra-daftar
purata +0.10R, median +0.03R, ≥ +2R 4.4%, ≤ −1R 8.4%; tanpa brek purata +0.20R (buang 40 +0.12R), median +0.03R, ≥ +2R 5.1%,
≤ −1R 8.6%; RAWAK_PADAN tanpa brek +0.13R (buang 40 +0.08R). Keluar: henti masa 60%, Chandelier 39%. Pegang purata 25 sesi.
Tumpuan untung 5 saham teratas (tanpa brek): 71% (penuh), 61% (buang 40).

Pulangan tahunan % (median benih; 2020 = Nov–Dis, 2026 hingga Okt; `playbook_tahunan.csv`):
| | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|---|
| PLAYBOOK_10 pra-daftar, penuh | 6.9 | 23.2 | −7.6 | 4.7 | 0.0 | 0.0 | 0.0 |
| RAWAK_PADAN_10 pra-daftar, penuh | 8.5 | 23.1 | −6.4 | −0.3 | 0.0 | 0.0 | 0.0 |
| PLAYBOOK_10 tanpa brek, penuh * | 6.9 | 23.2 | −7.6 | 14.6 | 20.9 | 24.2 | 27.3 |
| RAWAK_PADAN_10 tanpa brek, penuh * | 8.5 | 23.3 | −7.0 | 6.8 | 15.8 | 10.2 | 8.3 |
| PLAYBOOK_10 tanpa brek, buang 40 * | 8.6 | 28.9 | −8.7 | 15.5 | 15.4 | 17.4 | −4.1 |
| RAWAK_PADAN_10 tanpa brek, buang 40 * | 8.4 | 23.1 | −7.5 | 3.9 | 13.6 | 9.9 | −3.8 |
| RS_10 rujukan kos 0.25%, penuh | 38.3 | 37.0 | 34.2 | 57.0 | 65.1 | 54.6 | 127.1 |
| RS_10 rujukan kos 0.25%, buang 40 | 25.1 | 32.6 | 10.2 | 8.3 | 31.0 | 45.7 | 4.0 |
| SPY | 13.7 | 28.7 | −18.2 | 26.2 | 24.9 | 17.7 | 13.1 |

### Dapatan
1. **Brek pra-daftar menjadi kekal (kecacatan peraturan).** "Tiada belian baharu sehingga pulih ke −10%" tidak boleh pulih apabila
   posisi sedia ada sudah keluar: ekuiti tunai tidak bergerak. Dalam sampel, brek tercetus dalam 20/20 benih kedua-dua portfolio
   (Mac 2021 – Ogo 2024, kebanyakannya Jan 2022 – Okt 2023) dan tidak pernah dilepaskan; portfolio tunai ~64–73% masa, CAGR 3–5%.
   kill_switch (−25%) tidak tercetus kerana brek menghentikan belian dahulu. Ini juga berlaku ke hadapan: PLAYBOOK_10 dan
   RAWAK_PADAN_10 akan berhenti kekal pada kejatuhan pertama ≥ 15%. Peraturan TIDAK diubah (pra-daftar); keputusan pengguna
   diperlukan (cadangan: portfolio baharu dengan pra-daftar baharu, cth. tanpa brek, atau brek bertempoh).
2. **Nilai pemilihan kekal dalam rangka risiko.** Dengan peraturan sama, susunan RS 80–94 mengatasi susunan rawak: tanpa brek
   +6.2 mata CAGR (penuh) dan +3.5 mata (buang 40), persentil benih 0 = 100 / 95, MDD setara (−21.8% lawan −21.3%; −21.7% lawan
   −22.9%). Dengan brek pra-daftar beza ini mengecil (+0.6 / +1.9 mata) kerana kedua-duanya berhenti.
3. **Rangka risiko mengecilkan MDD tetapi lebih banyak mengecilkan pulangan.** MDD turun daripada −48% (RS_10) / −31.5% (RAWAK_10)
   kepada ~−22% (tanpa brek), tetapi CAGR turun kepada 18.5% (penuh) dan 11.5% (buang 40). MAR 0.82 / 0.53 lebih rendah daripada
   RS_10 rujukan (1.50 / 0.84) dan hampir sama dengan RAWAK_10 (0.84 / 0.57). Dalam set buang 40, CAGR 11.5% di bawah SPY 16.9% dengan
   MDD setara (−21.7% lawan −24.5%). Rejim SPY melindungi 2022 (−7.6% lawan SPY −18.2%).
4. **Pemacu**: had heat 10% (risiko 1% setiap posisi) mengehadkan purata ~10.6 posisi dan tunai ~22%; had 20 posisi jarang
   terpakai. Henti masa (bar ke-20 < +1R) menutup 60% dagangan; median R hanya +0.03R. Kesan setiap komponen (henti masa, had
   heat, penapis) belum diasingkan — tidak dipra-daftar, jadi tidak diuji di sini.
5. Brek lengkung bayang (kepekaan) tidak membantu: CAGR 13.7% dan MDD −22.8% (penuh), dan kill_switch tercetus dalam 8–11 daripada
   20 benih.

### Batasan khusus ujian ini
- Ciri dikira daripada `data_mentah` yang dilaras (harga ≥ USD10 dan nilai dagangan atas harga dilaras). Kalendar earnings
  `tarikh_pendapatan.csv` dianggap diketahui pada tarikh isyarat (tarikh earnings biasanya diumum beberapa minggu lebih awal);
  saham tanpa sejarah earnings = tidak diketahui (gagal). Peta industri dan sektor ialah peta semasa. P4(a)/(b) (Lejar/ambil alih)
  tidak terpakai dalam sampel.
- `mdd_jangka.json` (dibaca `jana_db.py`) = MDD seluruh tempoh peraturan pra-daftar; MDD PLAYBOOK rendah sebahagiannya kerana
  belian berhenti selepas brek. Tanpa brek, MDD median −21.8% (p5 −25.2%).
- Satu tempoh (Nov 2020 – Okt 2026); 20 benih sahaja.
