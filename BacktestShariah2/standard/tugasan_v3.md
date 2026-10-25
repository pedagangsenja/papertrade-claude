# Tugasan v3 — Peraturan semasa papertrade harian

Dokumen ini **satu-satunya** rujukan peraturan yang berkuat kuasa (sejak 14 Okt 2026; menggantikan `tugasan_v2.md`,
`papertrade_harian.md` dan §5 `00_NOTA_SERAHAN.md`, yang kini TERBATAL). Jika bercanggah dengan dokumen, prompt tugasan
berjadual atau ingatan lain, dokumen ini menang. Langkah setiap tugasan: `BacktestShariah2/jadual/`. Sejarah dan bukti setiap
keputusan bertarikh: `standard/SEJARAH_KEPUTUSAN.md`. §12 = cadangan 25 Okt 2026 yang MENUNGGU kelulusan pengguna.

## 1. Mod
- Papertrade C (Claude, maya) SAHAJA untuk belian baharu, dilayan seperti papertrade sebenar: harga buka sebenar, tiada pandang
  belakang. Tiada order Moomoo (`sim_trade_input/modify/cancel_order`, `trading_order_*`, `crypto_account_*_order`), tiada
  jualan, tiada wang sebenar tanpa kelulusan pengguna.
- Hook `.claude/settings.json`: PreToolUse menyekat semua alat order tanpa mengira awalan pelayan; SessionStart memasang
  `requirements.txt`. Jangan buang atau longgarkan.
- Posisi Moomoo lama (akaun simulasi AS acc_id 4135388, market 100; 200 posisi sah, 4 hari beli 1–8 Okt 2026) = sejarah: harga sahaja dikemas
  kini; tidak dicampur dalam Combine (§7).
- "Kalau tak beli, cakap tak beli." Data mesti betul; jangan reka.
- Hari operasi: hari dagangan NYSE sahaja (cuti = catat dan berhenti).

## 2. Jadual (model `claude-sonnet-5-5` bagi semua tugasan berjadual Claude)
| Mod (`BacktestShariah2/MOD_ACTIONS`) | Kerja harian | Tolakan db dashboard |
|---|---|---|
| `bayang` (sekarang) | Rutin Claude rasmi: kemas kini 6:02 pagi MYT Sel–Sab (`jadual/kemas_kini_0602.md`), imbas 7:47 malam MYT Isn–Jum (`imbas_2002.md`), beli 9:35 NY Isn–Jum (`beli_0935.md`); Actions menulis ke `bayang/` | dalam setiap rutin |
| `rasmi` (selepas peralihan, §10) | GitHub Actions `harian.yml`, `lejar.yml` → `analisis.yml`, `petang.yml`, `beli.yml` | `jadual/tolak_db.md` A (pasca-harian) dan B (pasca-beli); data Moomoo/SST mingguan `jadual/mingguan.md` |

Masa tepat (UTC/MYT/NY, DST) dan lampu dashboard: `jadual/README.md`, `jadual/CADANGAN_JADUAL.md`.

## 3. Kaedah dan isyarat
- 134 kaedah M (87 asal + 47 calon K145+ M115–M161; prompt lama yang menyebut "87 kaedah" sudah lapuk). Calon K145+: entry
  `spec/KATALOG_K145.md`, henti/keluar/tempoh = varian V1 beku pilihan WFO (`WFO/laporan/W01_LAPORAN.md`), tiada `hampir()`
  → tiada watchlist. Varian dipilih dalam registry set 431: skor tertinggi bukan DITOLAK, jika tiada, CAGR tertinggi.
  Indikator I01–I32 tidak digunakan. Kod: `BacktestShariah2/kod/` (sumber kebenaran; `kod/README.md`); enjin v1.2 beku.
- Kaedah baharu (tertakluk moratorium §12.2): `kod/registry/<ID>.csv`, baris ke `data/registry_M_gabung.csv`, db dashboard
  `registry/<ID>` (`standard/dashboard_kemaskini.py`), jana semula papan; skrip STEP-2 `WFO/kaedah_baru/step2_<ID>.py`.
- Skop imbasan: saham AS Shariah (screener Moomoo, `data/harga/univ.txt`) harga ≥ USD10; senarai 431 diutamakan.
- Jejak kertas M166 V1 (`uji_kertas/jejak_M166.csv`; rekod sahaja, tiada belian, tiada kesan pada senarai beli/watchlist; hingga
  15 Jan 2027). `uji_kertas/log.csv` = arkib beku (`uji_kertas/README.md`).
- **Senarai beli** = isyarat entry 100% dipenuhi pada tutup sesi DAN lulus kesahihan:
  - (a) isyarat MINGGUAN (M52 dan modul yang guna `akhir`) sah hanya pada hari dagangan terakhir minggu;
  - (b) setiap baris wajib ada `henti`, `nota_henti` (formula jika henti bergantung pada buka masuk, cth. M52 = 0.60×buka),
    `buka_maks` (cth. M08 = 1.05×SMA20) dan `sasaran`, daripada `sedia()` modul kaedah.
- **Saham tidak layak** — satu pintu `kod/tidak_layak.py`; ditapis daripada senarai beli, watchlist dan Lejar Penuh; pintu akhir
  `tidak_layak.py fail --tulis` atas `senarai_beli.csv` dan `watchlist.csv` (termasuk baris watchlist yang dibawa):
  1. Diambil alih = isyarat palsu (`kod/ambil_alih.py`): corak harga terkunci (jurang buka ≥ +10%, volum ≥ 4× median 50 hari,
     julat ≤ 3% pada hari pengumuman; kekal selagi 10 bar terakhir median julat ≤ 1.5% dan julat tutup ≤ 4%) ATAU senarai sah
     `data/ambil_alih.csv` (tambah perjanjian bayaran saham/campuran; `bayaran` = `bukan` mematikan pengesanan tersilap).
     Posisi C dibeli pada/selepas tarikh pengumuman → `tidak_sah`, kedua-dua lorong ditutup pada tutup bar terakhir; dibeli
     sebelum pengumuman kekal sah.
  2. Tidak cair: 20 bar terakhir ada ≥ 3 bar tanpa julat, ≥ 2 bar tanpa volum, atau median nilai dagangan < USD100 ribu →
     isyarat ditolak; posisi sedia ada tidak diubah.
  3. Kelas berganda (`data/kelas_berganda.csv`, disemak manual): hanya kelas paling cair (median nilai 20 bar) diimbas; posisi C
     kaedah+hari beli sama yang membeli dua kelas → kelas kurang cair `tidak_sah`.
  4. Lapisan EDGAR (`edgar.yml`, `standard/tawaran_edgar.py`: SC TO-T, SC 14D9, SC 13E3, 425 satu subject → `ambil_alih.csv`
     bayaran `edgar`; 25-NSE → `tarikh_tamat`; PREM14A/DEFM14A dan 425 berbilang subject → `data/edgar/calon.csv`): **TIDAK
     AKTIF sehingga rahsia repo `SEC_USER_AGENT` (nama + e-mel) ditetapkan** (`edgar.yml` melangkau tanpa menulis apa-apa).
  - Delist / tiada data: tiada bar ≥ 10 sesi pasaran → lorong yang belum keluar ditutup pada tutup bar terakhir; kekal sah
    (C: `tidak_layak.py posisi --tulis`; Lejar: sebab_keluar `delist`).
- **Watchlist (Hampir Signal)** = 90–99% dipenuhi (semua syarat kecuali pencetus; pencetus dalam ≤ 2%; pencetus kalendar ≤ 3
  hari dagangan); maks 5 setiap kaedah (431 dahulu, kemudian skor). Dinilai semula pada kemas kini dan imbasan; terkeluar
  (< 90% atau isyarat batal/tidak sah) → BUANG serta-merta. Calon baharu hanya pada imbasan; calon 100% dipindah ke senarai beli
  pada imbasan. % hampir maks 99.9 kecuali isyarat lengkap (`harian_c.py watch`; jarak 0 tanpa isyarat lengkap → `disentuh`).
  Calon tanpa jarak pencetus boleh diukur (`jarak_pct` kosong) tidak dimasukkan.
- **Belian semula**: saham yang sudah keluar terus diimbas; isyarat 100% baharu = belian ke-2, ke-3 … (`belian_ke`). Hanya
  posisi C kaedah SAMA yang masih terbuka dikecualikan (kaedah lain boleh, dengan `kaedah_kongsi`). Terbuka = lorong 1 belum
  keluar; lorong 2 tidak menyekat (`kod/scanner.py pegangan_c`). Prestasi belian semula dinilai berasingan selepas ≥ 20
  dagangan tertutup.

## 4. Belian maya (9:35 NY)
- Calon = semua baris senarai_beli (tiada had slot). 1 unit setiap saham; kaedah kedua untuk saham sama = `kaedah_kongsi`.
- Langkau jika: buka ≤ henti; buka > buka_maks; buka ≥ sasaran (jika kaedah melangkau); isyarat batal; kunci
  kaedah+saham+tarikh_isyarat sudah wujud dalam claude*.csv.
- Belum didagangkan pada masa belian (buka = 0): TIDAK dilangkau — harga sementara = tutup isyarat, nota `buka_lewat`; buka
  rasmi dan kesahihan (§5.4) disahkan dengan bar harian keesokannya (sama seperti Lejar).
- Harga beli = harga buka sebenar; buka sementara dibetulkan oleh kemas kini seterusnya (§5.2).

## 5. Kualiti data (wajib)
1. Quote dengan low/high = 0 bermaksud tiada dagangan; JANGAN tafsir sebagai kena henti. Guna bar harian.
2. Harga beli rasmi = buka bar harian muktamad hari beli. Mod `bayang`: kline Moomoo (rutin 6:02). Mod `rasmi`: bar yfinance
   muktamad dalam stor repo (`harian_c.py` membetulkan buka sementara); kline Moomoo hanya semakan sampel mingguan
   (`jadual/mingguan.md` 7d) — beza dilapor, dibetulkan dengan `standard/betul_harga_beli.py` hanya selepas disahkan.
3. Keluar dinilai dengan enjin rasmi (`kod/`) dan `standard/harian_nilai_keluar.py` `keluar()`: henti dari hari masuk (buka
   jurang bawah henti dari hari kedua → harga buka); sasaran hanya dari hari selepas masuk, dengan tgt hari sebelumnya; isyarat
   keluar kaedah → jual pada BUKA hari berikutnya; had masa → tutup. Kaedah replika (`kod/dagangan.py` REPLIKA: M02, M19,
   M20, M26, M31, M38, M41, M47, M76, M78, M81, M82, M100): lajur exitc/tgt modul milik dagangan replika enjin, jadi posisi
   hadapan dinilai dengan `dagangan.sedia_dagangan()` (dagangan sendiri; Lejar, `harian_c.py`, `dagangan.py betul --tulis`).
3a. **Dua lorong keluar**, direkod berasingan (`papertrade/SKEMA.md`): lorong 1 = peraturan kaedah (perkara 3); lorong 2 =
   "pegang selagi naik", Chandelier tutup: tutup < tutup tertinggi sejak beli − 4×ATR14 → jual pada buka esok; paras hanya
   naik; tanpa henti kaedah (lajur `*_henti`; `kajian/KAJIAN_LORONG2.md`). Dinilai selepas lorong 1:
   `standard/keluar_lorong.py --stor <stor kerja>`. `tutup_semua` = kedua-dua keluar. Lejar Penuh memakai peraturan sama.
4. Kesahihan belian: belian semalam disemak semula dengan `sedia()` atas bar hari beli; `sig` = False → TIDAK DIBELI. Baris
   `tidak_dibeli`/`tidak_sah` tidak dikira dalam prestasi atau pendedahan sektor.
5. Sebelum push data: `python3 BacktestShariah2/standard/sahkan.py --betulkan` MESTI keluar 0. Jika 1: betulkan; jika tidak
   boleh, JANGAN push data rosak — catat ralat dalam log dan push log sahaja.
6. Setiap saham wajib ada sektor & industri (SST `get_stock`, sandaran Moomoo `quote_owner_plate`; tiada → "Tiada data" + catat).
   Data tidak boleh dibiar kosong untuk analisis: skrip isi semula `henti_isi.py`, `isi_audit.py`, `qr_isi.py` +
   `kalendar_earnings.py`, `gred_kewangan_isi.py`; yang tidak boleh ditentukan ditanda dengan sebab (cth. `sumber_earnings`
   "tidak diketahui (…)"). Saham baharu tanpa sejarah harga → `data/harga/perlu_sejarah.txt`.

## 6. Stor
- Repo `pedagangsenja/papertrade-claude`. Rutin dan bot: `git pull --rebase origin main` dahulu, commit, `git push origin main`
  (ditolak → pull --rebase, cuba semula maks 3 kali; tiada `--force`, tiada `-X theirs`). Pembangunan: cawangan + PR
  (polisi git `CLAUDE.md`). Skema CSV: `papertrade/SKEMA.md`.
- Dashboard: https://claude.ai/code/artifact/12bb853e-34ef-4d6c-885d-10f46984437e (db melalui ArtifactData; JANGAN cipta artifact
  baharu). Dokumen dijana `standard/jana_db.py` (senarai dalam kepala skrip; `papertrade/claude_N` tanpa had, watchlist dan
  dokumen besar dibahagi `bahagi_db.py`). JSON padat; had keras 262,144 bait setiap dokumen: dokumen ≥ had dilangkau dan
  dicatat dalam `harian/status.ralat`, amaran ≥ 80% (juga dalam notifikasi); `pecah_claude.py --pecah` memecah `claude*.csv`
  yang unjurannya > 240 KB (CI menyemak setiap push).
- Log: imbasan → `standard/binaan_v2_log.md`; kemas kini dan belian → `standard/binaan_v2_log_tambahan.md` (tambah di hujung;
  kiraan disalin daripada output skrip, bukan ditaip).
- Harga yfinance: `harga_harian.yml` (21:37 UTC Isn–Jum, sandaran 00:23 UTC) dan `harian.yml` sendiri (05:07 UTC) →
  `data/harga/terkini.csv` (10 sesi; universe 431 + papertrade + `univ.txt` + SPY/QQQ), `status.json`, `sejarah.csv` (3 tahun
  bagi `perlu_sejarah.txt`); skrip `standard/harga_yf.py`. Data ditarik < 00:20 UTC selepas sesi atau liputan < 99% = belum
  muktamad (sesi ditangguh). Mod `bayang`: rutin 6:02 menyemak silang dengan kline Moomoo (`harga_yf.py semak`; beza > 0.5%
  → guna Moomoo). Mod `rasmi`: bar yfinance muktamad = rasmi; tiada semakan Moomoo harian (§5.2).
- Stor harga = repo `data/harga/stor/` (`harga_A.csv`, `harga_B.csv`, `harga_idx.csv`; format `kod/stor.py`, 520 bar),
  dikemas kini `lejar.py stor` (lejar.yml dan harian.yml). Rutin menyalinnya ke folder kerja; jangan ubah atau commit. Aset
  dashboard `harga_aset` A/B/idx tersangkut pada 12 Okt 2026 — JANGAN guna.
- Konvensyen stor: bar sebelum ~2 Okt 2026 = data backtest (dilaras hadapan termasuk dividen); bar yfinance selepasnya dilaras
  pecahan sahaja. Sejarah dilaras hanya jika nisbah bar bertindih seragam (`kod/stor.py nisbah_laras`: serak ≤ 0.2%, ≥ 3 bar
  atau nisbah pecahan; selainnya 'anomali'; log `data/harga/stor/log_laras.csv`). Spin-off, dividen ≥ 2% dan pengagihan ≥ 25%
  melalui `data/harga/faktor.csv` (`kod/peristiwa.py`: dividen yfinance automatik; jurang ≤ −15% tanpa earnings →
  `faktor_calon.csv` → sahkan dengan Moomoo `quote_corporate_actions_rehab`; jangan reka faktor). Posisi C merentasi tarikh_ex
  dilaras (`tidak_layak.py posisi`); posisi 'kena henti' pada/selepas tarikh_ex yang Low tidak sampai henti dilaras dibuka
  semula. Versi pustaka dipin `kekangan.txt`.
- Alat besar: hasil disimpan ke fail oleh sistem — proses dengan Python; jangan salin data harga secara manual. Kline Moomoo
  ~4 panggilan seminit, maks 24 ticker setiap larian, sentiasa `autype` 0 (tanpa pelarasan).

## 7. Prestasi
- Papertrade C (gabungan semua claude*.csv) dan Combine = **Papertrade C sahaja** (§12.6); Papertrade M (posisi Moomoo lama)
  dipapar berasingan sebagai sejarah. Baris sah sahaja. KPI, untung purata setiap kaedah, kadar menang, penurunan maksimum,
  Paling Teruk, skor Untung×Selamat (paparan). Skrip `standard/harian_prestasi.py <folder>` (DIBINA, HARGA_PADA melalui env),
  `jana_db.py` (`prestasi/ringkasan`) dan `bina_p4_mae.py`.
- Label TERUSKAN / PERHATI / HENTIKAN **dibersarakan** (§12.6): keputusan kaedah = pintu Papan Penganalisis (§11, `pantau`).
  `harian_prestasi.py` mengekalkan medan lama untuk keserasian (`keputusan` = "dibersarakan"; `teruskan`/`hentikan`/`bil` =
  null; `pantau_penganalisis`). `jana_db.py prestasi()` dan halaman dashboard masih mengira label dan Combine lama sehingga
  dikemas kini — jangan jadikan label itu asas keputusan.
- Metrik portfolio dalam dolar: setiap posisi = USD1,000 (sama berat); rekod CSV kekal 1 unit.

## 8. Gred calon (rekod dan uji dahulu, bukan penapis)
Dikira pada hari isyarat oleh `standard/gred.py` dan direkod bersama setiap belian; setiap baris memakai snapshot tarikh sama
dengan sesi isyarat (`tarikh_isyarat` / `tarikh_data`; tiada pandang hadapan); tiada data → "–".
1. **Industri** dan 2. **Sektor** (v2; `gred_kumpulan.yml` → `data/kumpulan/gred_kumpulan.csv`; seluruh pasaran AS ~5,600 saham
   ≥ USD5; industri = plate Moomoo `papertrade/peta_industri.csv`; sektor = 11 sektor Morningstar; indeks = purata sama rata).
   Industri: pangkat persentil (Weinstein: Mansfield RS > 0, RS naik 21 sesi, indeks > SMA150 yang naik; + pangkat median
   pulangan 1 bulan); tidak terpakai bagi 15 kaedah pantulan (`kod/jenis_kaedah.csv`). Sektor: pangkat persentil % saham di
   atas SMA200 — paparan sahaja. Gred A > 80, B > 60, C > 40, D > 20, E ≤ 20. Gred v1 (sebelum 19 Okt 2026) tidak dicampur.
   Bukti: `kajian/KAJIAN_GRED_KUMPULAN.md`.
3. **RS rating** 1–99 (gaya IBD 40/20/20/20) lawan seluruh pasaran AS ≥ USD5 (`rs_pasaran.yml` → `data/rs/`; sandaran stor,
   `rs_sumber`; sejarah pendek → anggaran `gred.rs_pendek`, maks C). A = 90–99 disahkan, B = 80–89 disahkan, C = 70–79 atau
   ≥ 80 tidak disahkan, D < 70; disahkan = saham naik 12 bulan, SPY > SMA200 dan Mansfield > 0 (`rs_sah`, `rs_tanda`; RS 95+
   ditanda berisiko). Bukti dan had: `kajian/rs/RINGKASAN.md`. `rs_industri` direkod sahaja.
4. **Pemangkin v3**: K1 earnings 6–21 hari dagangan lagi +2, 1–5 hari +1; K2 reaksi earnings ≥ +20% lawan SPY, umur ≤ 10 hari
   +4, 11–20 hari +3 (🔥 PANAS); veto berita ≤ 20 hari dagangan: tawaran saham atau keputusan FDA → had C, sasaran ambil alih →
   had D. A ≥ 3, B 2, C 1, D 0; E tidak dipakai. Tajuk berita, analisis, volum, orang dalam tidak diberi mata. Data: Moomoo/SST
   atau `pemangkin.yml` (`data/pemangkin/yahoo.json`, `earnings_nasdaq.json`); bukti dalam ulasan `gred.py`.
5. **QR** = hari dagangan ke laporan suku seterusnya (SST `market_events`; kalendar Nasdaq ≤ 4 hari; jika tiada, earnings
   lalu + 91 hari). K1 (jangkaan pulangan) dan QR (risiko jurang melepasi henti) dibaca bersama.
- Gred keseluruhan (paparan) = purata mata Industri (kecuali kaedah pantulan), Pemangkin dan QR. Gred kewangan v7
  (`spec/GRED_KEWANGAN_v7.md`) direkod sahaja. Sesuatu gred dinilai selepas ≥ 20 dagangan tertutup; gred tidak menapis belian
  sehingga pengguna memutuskan.
- Status trend D10H2-r2 (`data/trend/status.json`, `standard/trend_status.py`, `harian.yml`; susunan SMA 50/150/200, ATR14% +
  kuintil, rejim SPY) = paparan sahaja: bukan penapis dan bukan peraturan jual (kajian 23 Okt 2026: tidak meramal pulangan
  3–30 hari).

## 9. Lejar Penuh
- SEMUA isyarat setiap kaedah dibeli pada buka rasmi esok dan dikeluarkan ikut peraturan kaedah (enjin v1.2, dua lorong §5.3a),
  tanpa had sekaedah dan tanpa keutamaan 431. Harga: stor repo. Saham tidak layak ditapis (§3).
- `lejar.yml` (06:17 UTC Sel–Sab, sandaran 10:17; tanpa LLM, tanpa Moomoo; larian terlepas ditampung; sesi ditangguh jika data
  belum muktamad) → `lejar/` (`lejar/README.md`, `standard/lejar.py`) dan `portfolio_slot/` (`standard/portfolio_slot.py`:
  RS_10, RAWAK_10, GABUNGAN_10, TOP1_10, RAWAK_KAEDAH_10; 10 slot, keluar lorong 2; log gantung `portfolio_slot/gantung.csv`;
  kajian `kajian/KAJIAN_PORTFOLIO.md`). Rekod sahaja; rutin tidak menulis ke `lejar/` atau `portfolio_slot/`.

## 10. Peralihan ke GitHub Actions (mod selari sejak 17 Okt 2026)
- Kerja harian tanpa LLM: `standard/harian_c.py` (kemas kini posisi, imbas 134 kaedah, gred, beli 9:35 NY) melalui `harian.yml`
  (05:07 UTC Sel–Sab + sandaran), `beli.yml` (9:40 NY + sandaran) dan `petang.yml` (gred P sebelum buka). Peraturan sama dengan
  §3–§8. Harga beli 9:35 NY = buka sementara yfinance, dibetulkan kepada buka bar harian muktamad keesokannya (§5.2).
- `MOD_ACTIONS` = `bayang`: Actions menulis ke `BacktestShariah2/bayang/` sahaja (jangan ubah manual) dan membanding setiap
  tarikh MYT yang belum dibanding (`banding_bayang.py belum` → `bayang/BANDING_<tarikh>.md`); rutin Claude kekal rasmi (§2).
  `rasmi`: Actions menulis ke `papertrade/`, rutin Claude dimatikan, dashboard ditolak `jadual/tolak_db.md` (A selepas
  harian + lejar + analisis; B selepas beli), data Moomoo/SST mingguan. Langkah: `jadual/PERALIHAN.md`; hanya selepas
  pengguna meluluskan.
- `penjaga_jadual.yml` mendispatch workflow berjadual yang cetusan cronnya hilang/lewat (30 minit; beli 8 minit) dalam had
  masa; dicetus juga dari luar oleh tugasan berjadual Claude (`jadual/README.md`).

## 11. Papan Penganalisis (rekod analisis sahaja; tidak menapis belian)
- `standard/penganalisis.py` → `laporan/PENGANALISIS.md` + `data/analisis/papan.json` (db `analisis/papan`); `analisis.yml`
  dicetus sebaik `lejar.yml` siap; parameter backtest `data/analisis/kalibrasi_skor.json` (`kalibrasi_skor.py`). Jangan ubah
  output secara manual.
- Skor (purata pulangan bersih setiap dagangan) = (n0 × jangkaan backtest + n × purata posisi hadapan matang) ÷ (n0 + n).
  Jangkaan = purata set 431 varian aktif × (25% + 25% bagi setiap semakan luar sampel lulus: S1–S4 ≥ 3/4 atasi EW; WFO W01
  CAGR > EW 423; AUTOTUNE A01 CAGR > SPY dalam kumpulan A dan B); n0 = 1 ÷ (1/30 + 1/dagangan backtest). Bukti hadapan =
  Lejar Penuh + kohort Papertrade C sebelum Lejar (tanpa kiraan berganda; harga beli Lejar dilaras jika stor dilaras); matang =
  dibeli ≥ maks(14 hari, 1.5 × hari pegang backtest) lalu. n = n berkesan ikut hari beli (< 5 hari beli → bilangan hari);
  purata = purata matang PENUH (pangkas 5% semakan sahaja); median, hari beli, lintas earnings dilapor.
- Status: BELUM CUKUP (< 20 matang atau < 10 hari beli), AMARAN (≥ 10 matang, t < −2), KUAT / LEMAH (julat 95% skor di atas /
  di bawah 0), PERHATI. Swing = pegang backtest 3–30 hari; kedudukan ikut skor sebulan (skor ÷ hari pegang × 21, tanpa
  bundar); < 100 dagangan backtest = sampel kecil. Setiap baris: `p_top1`/`p_top5`/pangkat p5–p95 (Monte Carlo berbiji),
  `lb_bulan`, meter bukti, kelompok korelasi (ρ ≥ 0.7), `tarikh_sebenar`.
- **Pantau** (label pintu kaedah; menggantikan label §7): BERSARA (P(purata ≤ 0) > 0.9 dengan ≥ 20 hari beli, atau ≥ 2 amaran
  CUSUM), GANTUNG (kejatuhan ekuiti kohort > 1.5× atau tempoh di bawah puncak > maks backtest, atau purata 20 hari beli matang
  terakhir < p5 purata bergulir backtest dilaras ke jangkaan), AMARAN (1 amaran CUSUM), OK, BELUM CUKUP. CUSUM: sasaran =
  min(purata winsor, kekal × purata winsor), k 0.25, h bootstrap blok bulanan; pengawal bukti (≥ 10 hari beli matang dan nb ≥ 10)
  sebelum BERSARA/GANTUNG/AMARAN. Portfolio GABUNGAN_10 tidak membeli kaedah GANTUNG/BERSARA (`portfolio_slot/gantung.csv`).

## 12. CADANGAN 25 Okt 2026 — menunggu kelulusan pengguna
Hasil audit operasi 25 Okt 2026 (`standard/SEJARAH_KEPUTUSAN.md`). Bahagian ini BELUM berkuat kuasa; selepas pengguna
meluluskan (merge cawangan pratonton), setiap perkara dipindah ke seksyen berkaitan dan dicatat dalam SEJARAH_KEPUTUSAN.md.
Perkara bertanda (agen lain) dibina dalam cawangan pratonton lain; butirannya disahkan dalam cawangan itu.
1. **Pembekuan peraturan** ≥ 20 hari dagangan NYSE selepas hari pertama `MOD_ACTIONS` = `rasmi`: tiada perubahan pada entry,
   keluar, penapis, skor, label atau senarai kaedah. Dibenarkan: pembetulan pepijat yang menghasilkan data salah (versi
   peraturan dinaikkan + catatan), kerja infrastruktur yang tidak mengubah keputusan dagangan, dan paparan dashboard.
2. **Moratorium kaedah baharu** dalam tempoh yang sama, kecuali M168 (kaedah manual pengguna; agen lain). Kaedah yang ada
   kekal; tiada penalaan semula yang diguna (`tala_semula.py guna`).
3. **Penanda aras utama = EW alam Shariah**: `standard/penanda_ew.py` → `data/analisis/ew_harian.csv` (sama berat, alam
   `univ.txt` ≥ USD10, kelayakan ikut tutup semalam, pulangan harian dihad ±50%). SPY kekal penanda kedua. (Belum dijalankan
   oleh workflow; perlu langkah dalam `lejar.yml` atau `analisis.yml`.)
4. **Sasaran baharu**: "untung minimum 10% sebulan" (`00_NOTA_SERAHAN.md` §1) diganti "lebihan bersih kos atas EW alam Shariah,
   dengan MDD portfolio ≤ 20%", diukur pada portfolio maya 10 slot ke hadapan.
5. **Pintu wang sebenar A–F** (setiap kaedah dipapar dengan "apa yang masih kurang"; `reports/Audit pratonton swing trader.md`
   item 18): A dibekukan dan didaftar; B lulus luar sampel bebas (AUTOTUNE ≥ SEDERHANA, DSR dilapor, PBO ≤ 0.5); C bukti hadapan
   terlaras ujian berbilang; D inkubasi ≥ 6–12 bulan yang merangkumi satu fasa pasaran turun; E portfolio 10 slot mengatasi
   RAWAK_KAEDAH_10 dan SPY selepas kos; F saiz berperingkat dengan peraturan henti bertulis. Ambang D–F = cadangan audit.
   Tiada wang sebenar sebelum A–F lulus DAN pengguna meluluskan secara bertulis.
6. **Bersara label §7 dan Combine tanpa Moomoo** (§7): pintu kaedah = Pantau Papan Penganalisis (§11). Dilaksanakan dalam
   `harian_prestasi.py` (pratonton `pt/ops`); `jana_db.py prestasi()` dan pengiraan halaman dashboard masih memakai label lama
   dan Combine lama sehingga dikemas kini (fail agen lain).
7. **Playbook / PLAYBOOK_10 dan RAWAK_PADAN_10** (agen lain; `portfolio_slot`): portfolio maya bersaiz risiko mengikut
   playbook bertulis, lawan kawalan rawak yang dipadankan; rekod sahaja.
8. **`versi_peraturan` dan kohort backfill** (agen lain): setiap posisi/kohort membawa versi peraturan yang memakainya, supaya
   prestasi sebelum dan selepas perubahan tidak dicampur.
9. **Penganalisis v2** (agen lain): susunan dan pintu Papan Penganalisis disemak semula (laporan audit pratonton P0–P2).
10. **M168** (agen lain): kaedah manual pengguna, satu-satunya pengecualian moratorium.
11. **Jadual operasi**: tolakan db A pasca-harian (~06:47 UTC / 14:47 MYT, selepas `harian.yml` + `lejar.yml` + `analisis.yml`)
   dan B pasca-beli (10:33 NY, ikut DST); penjaga tugasan berjadual 2 slot (pasca-harian 13:41 MYT, pra-beli 9:50 NY) ganti
   6 slot UTC; notifikasi malam digabung ke tolakan A; lampu dashboard `jangkaSesi` dianjak — `jadual/CADANGAN_JADUAL.md`.
12. **Amaran data luar** dalam notifikasi (`notifikasi.py --amaran --db`): SST > 8 hari, EDGAR tidak aktif atau > 2 sesi,
   kalendar earnings > 2 sesi, dokumen db ≥ 80% had.
13. **Polisi git** (`CLAUDE.md`): pembangunan di cawangan + PR; tiada push kod 05:00–13:30 UTC; kiraan log dijana skrip;
   workflow bot tanpa `-X theirs`.
