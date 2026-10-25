# Sejarah keputusan (12–25 Okt 2026)

Rekod bertarikh keputusan pengguna dan perubahan peraturan yang dahulu tersebar dalam `CLAUDE.md` dan `standard/tugasan_v3.md`
(dipindah 25 Okt 2026, audit operasi item 7). **Fail ini sejarah sahaja**: peraturan yang berkuat kuasa ada dalam
`standard/tugasan_v3.md`; jika bercanggah, tugasan_v3 menang. Butiran bukti: fail kajian yang dirujuk dan log
`standard/binaan_v2_log.md`, `standard/binaan_v2_log_tambahan.md`. Tambah entri baharu di hujung (satu baris setiap keputusan,
dengan tarikh, siapa memutuskan, dan fail yang berubah).

## 12–14 Okt 2026: serahan ke repo
- 12 Okt: aset dashboard `harga_aset` (stor harga A/B/idx) tersangkut pada data 12 Okt; tidak dipakai lagi sejak 16 Okt
  (stor repo `data/harga/stor/`).
- 13 Okt: Project claude.ai "Backtest Shariah" penuh (99.2%); nota serahan `00_NOTA_SERAHAN.md`. Papertrade C (Claude, maya)
  SAHAJA untuk belian baharu; tiada order Moomoo, tiada wang sebenar (keputusan pengguna).
- 14 Okt: repo `pedagangsenja/papertrade-claude` menggantikan Project "Backtest Shariah 2" sebagai stor utama; salinan Project
  dibekukan. `tugasan_v3.md` berkuat kuasa (menggantikan `tugasan_v2.md`, `papertrade_harian.md`, §5 nota serahan; semua
  TERBATAL). Rutin berjadual menembak sesi Sonnet yang sudah dilampirkan repo (tiada `add_repo`).
- 14 Okt (pengguna): label §7 TERUSKAN/PERHATI/HENTIKAN (< 20 dagangan tertutup = BELUM CUKUP DATA; HENTIKAN jika untung
  purata ≤ −3% atau gagal ≥ 75% atau skor < 25; TERUSKAN jika skor ≥ 55 dan untung purata > 0; selainnya PERHATI). Metrik
  portfolio USD1,000 sama berat. Ujian luar sampel backtest tidak dibuat. Gred calon A–E: rekod dan uji dahulu, bukan penapis.
- 14 Okt: harga yfinance GitHub Actions `harga_harian.yml` (sumber tidak rasmi; semak silang Moomoo; beza > 0.5% → Moomoo).

## 15–17 Okt 2026
- 15 Okt: imbas malam dianjak 8:02 → 7:47 malam MYT. Pengawas jadual (sesi Sonnet `session_01686xK3etzJNAReGbsM8sAw`,
  `trig_018zyZSoegh4fQWpWGv3wS9m`, `trig_01AJf4h6GffXNmHXmQsVzzGF`, `trig_018eaPB3VHoodMscT1s8BiLs`) menembak semula rutin
  yang gagal; prosedur bermula dengan "Semak pendua". Skala Berita Panas 15–17 Okt (dibatalkan 18 Okt).
- 16 Okt (pengguna): belian semula saham yang sudah keluar (isyarat 100% baharu = belian ke-2, ke-3 …; `belian_ke`).
  47 calon K145+ M115–M161 ditambah (entry `spec/KATALOG_K145.md`; henti/keluar/tempoh = pilihan WFO suku terkini dibekukan
  sebagai V1; tiada `hampir()`). Lejar Penuh fasa 1 (`lejar.yml`; semua isyarat semua kaedah; keputusan pengguna: data adil).
  Stor harga repo menggantikan aset dashboard. `claude_N` tanpa had. Rekod semua isyarat malam `data/isyarat/*.csv.gz`.
- 16 Okt: automasi — hook PreToolUse menyekat semua alat order, SessionStart memasang `requirements.txt`, `semak_data.yml`
  (ujian unit + `sahkan.py` setiap push). Notifikasi telefon pada akhir setiap giliran (permintaan pengguna).
- 17 Okt (pengguna): dua lorong keluar — lorong 1 kaedah, lorong 2 "pegang selagi naik" (asal: 2 tutup turun berturut atau
  henti); lorong 10% dibuang hari yang sama. Belian semula dipinda: hanya posisi C kaedah sama yang masih terbuka dikecualikan
  (17–18 Okt: terbuka sehingga `tutup_semua`).
- 17 Okt (pengguna): peralihan rutin Claude → GitHub Actions (`harian_c.py`, `harian.yml`, `beli.yml`, `petang.yml`; jimat
  ~37 juta token sehari) dengan mod selari 3 hari dagangan; belian kekal ~9:35 NY; data Moomoo/SST mingguan; dashboard
  ditolak satu sesi Claude ringkas. Jejak kertas M166 V1 (rekod sahaja, hingga 15 Jan 2027).

## 18–20 Okt 2026
- 18 Okt (pengguna): RS rating lawan SELURUH pasaran AS ≥ USD5 (`rs_pasaran.yml`); gred RS A = 90–99 disahkan, B = 80–89
  disahkan, C = 70–79 atau ≥ 80 tidak disahkan, D < 70 (bukti `kajian/rs/RINGKASAN.md`; dakwaan lama "+4.2%, mendahului
  setiap tahun" dibatalkan). RS tidak lagi dalam gred keseluruhan. Pemangkin v3 (K1 earnings, K2 reaksi earnings, veto berita).
  Kajian gred kumpulan (`kajian/KAJIAN_GRED_KUMPULAN.md`) → Gred Sektor/Industri v2.
- 19 Okt: lorong 2 = Chandelier tutup (tutup < tutup tertinggi sejak beli − 4×ATR14 → jual buka esok; paras hanya naik;
  `kajian/KAJIAN_LORONG2.md`); posisi terbuka = lorong 1 belum keluar (lorong 2 tidak menyekat belian semula). Gred S/I v2
  berkuat kuasa (gred_pada ≥ 19 Okt); gred keseluruhan = Industri (kecuali pantulan) + Pemangkin + QR. Portfolio maya 10 slot
  (RS_10, RAWAK_10; `portfolio_slot.py`). `papertrade/senarai_beli` tidak lagi ditolak ke db.
- 19 Okt: cron workflow didaftar semula (tiada cetusan 17 Okt 14:10 – 19 Okt UTC). `penjaga_jadual.yml` + tugasan berjadual
  Claude `trig_01N3Qx1S6bRhf9h5BEKk85bQ` (05:20, 06:20, 12:20, 14:20, 22:20, 23:20 UTC Isn–Sab; sesi Sonnet
  `session_018zpLxNRJ3rxZBvGT9yztVT`, run_workflow sahaja). Pengawas jadual DIMATIKAN (pengguna; jimat ~4 juta token sehari).
- 20 Okt (pengguna): Papan Penganalisis (`penganalisis.py`, `analisis.yml` selepas `lejar.yml`; rekod analisis sahaja).
  Gred kewangan v7 (`spec/GRED_KEWANGAN_v7.md`; imbas langkah 5c).

## 21–22 Okt 2026
- 21 Okt (pengguna): saham diambil alih = isyarat palsu (BRZE 20 Okt: 13 kaedah membeli selepas pengumuman Salesforce);
  `kod/ambil_alih.py` + `data/ambil_alih.csv`; 89 posisi C `tidak_sah`. Saham tidak cair (20 bar: ≥ 3 tanpa julat, ≥ 2 tanpa
  volum, median nilai < USD100 ribu). Delist: tiada bar ≥ 5 sesi → ditutup pada tutup akhir. Satu pintu `kod/tidak_layak.py`.
- 22 Okt: kelas berganda (`data/kelas_berganda.csv`); delist 5 → 10 sesi; pintu akhir `tidak_layak.py fail --tulis` (NWS).
  Lapisan EDGAR `edgar.yml` / `tawaran_edgar.py` (SC TO-T, SC 14D9, SC 13E3, 425 satu subject; 25-NSE = tamat) — **tidak
  pernah aktif**: rahsia repo `SEC_USER_AGENT` belum ditetapkan (tiada `data/edgar/`).
- 22 Okt: kaedah replika (R10; `kod/dagangan.py`): exitc/tgt M02, M19, M20, M26, M31, M38, M41, M47, M76, M78, M81, M82, M100
  milik dagangan replika enjin. Konvensyen stor harga dan peristiwa besar (`kod/stor.py nisbah_laras`, `kod/peristiwa.py`,
  `data/harga/faktor.csv`; laporan `kajian/reports/Pengesanan data tercemar yang tinggal.md`); kline Moomoo `autype` 0; versi
  pustaka dipin `kekangan.txt`. Belian "belum didagangkan" tidak dilangkau (`buka_lewat`). R1: `lejar.tampal_moomoo` hanya
  nota (buka sementara 9:35 NY pernah disimpan sebagai "Moomoo menang").
- 22 Okt (pengguna): Papan Penganalisis kukuh (purata matang PENUH; pangkas 5% semakan sahaja; n berkesan ikut hari beli;
  BELUM CUKUP < 10 hari beli) dan Pantau (BERSARA / GANTUNG / AMARAN / OK / BELUM CUKUP; `kalibrasi_skor.py`). Gabungan beku
  `data/analisis/gabungan_beku.json` (GABUNGAN_10, TOP1_10, RAWAK_KAEDAH_10; sementara; jangan ubah tanpa keputusan pengguna).
- 22 Okt: 9 larian CI gagal, 6 daripadanya 05:21–07:51 UTC (pembangunan dipush terus ke `main` dalam tetingkap pengeluaran).

## 23–24 Okt 2026
- 23 Okt (pengguna): audit data dashboard — data tidak boleh dibiar kosong (`henti_isi.py`, `isi_audit.py`, `qr_isi.py`,
  `kalendar_earnings.py`, `gred_kewangan_isi.py`; `perlu_sejarah.txt`). Status trend D10H2-r2 (`trend_status.py`; paparan
  sahaja: kajian 23 Okt tidak meramal pulangan 3–30 hari). `lejar.yml` mencetus `analisis.yml` terus bagi larian dispatch bot
  (GITHUB_TOKEN tidak menjana `workflow_run`).
- 24 Okt (PRATONTON, cawangan `pratonton-audit`): ranking tunggal + pantau v3 Penganalisis (skor sebulan tanpa bundar,
  `p_top1`/`p_top5`/pangkat Monte Carlo, meter bukti, kelompok korelasi, CUSUM k 0.25 dengan h bootstrap blok bulanan,
  pengawal bukti ≥ 10 hari beli matang dan nb ≥ 10). Kira semula bebas (`kira_semula.py`, `sampel_semak.py`, `sahkan.py`
  semakan sumber). `jana_db.py`: dokumen ≥ had db dilangkau (bukan SystemExit), amaran ≥ 80%. Medan SST > 2 sesi dibuang.
- 24 Okt (pengguna): notifikasi telefon bagi kerja papertrade Actions (`notifikasi.py`, `jadual/notifikasi_harian.md`).
  Peralihan ditangguh ke Isnin 26 Okt 01:00 UTC (tugasan sekali `trig_01MUQxMSZmi3HroCCApwit2b`).

## 25 Okt 2026: audit operasi (CADANGAN — menunggu kelulusan pengguna)
Penemuan: tolakan db 10:20 NY selepas peralihan memberi data sesi D ~50 minit SELEPAS buka D+1 dan hanya 4–7 minit selepas
beli; DST tamat 1 Nov menganjak slot UTC penjaga (14:20 UTC = 9:20 EST, sebelum gerbang beli 9:31); cron GitHub lewat median
100–297 minit; `git pull --rebase -X theirs` boleh menimpa perubahan serentak; harian.yml membanding "MYT semalam" sahaja
(tiada BANDING_2026-10-24); pembangunan dipush terus ke `main` dalam tetingkap pengeluaran; SST mati sejak 19 Okt dan EDGAR
tidak aktif tanpa amaran; dokumen bercanggah; label §7 tidak stabil (set HENTIKAN berubah 3 kali dalam 5 hari); 200 posisi
Moomoo lama (4 hari beli) dalam Combine; `uji_kertas/log.csv` beku sejak 6–7 Okt; nama penuh pemilik dalam repo awam;
3 tugasan berjadual lama yang dimatikan masih mengandungi arahan order simulasi; penjaga mencetus LLM 36×/minggu sebagai cron;
kiraan log ditaip LLM. Cadangan: `standard/tugasan_v3.md` §12 dan `jadual/CADANGAN_JADUAL.md`.
- Dilaksanakan dalam pratonton `pt/ops` (berkuat kuasa hanya selepas merge): tanpa `-X theirs`; `banding_bayang.py belum`;
  amaran SST/EDGAR/kalendar/db dalam `notifikasi.py` + `notifikasi.py sedia`; label §7 dibersarakan dan Combine tanpa Moomoo
  (`harian_prestasi.py`); penjaga `LEWAT_KHAS` beli 8 minit; dokumen dipadatkan (fail ini); nama penuh pemilik dibuang
  daripada nota serahan dan PDF dibuang (sejarah git masih menyimpannya); `uji_kertas/README.md` (log.csv diarkib).
