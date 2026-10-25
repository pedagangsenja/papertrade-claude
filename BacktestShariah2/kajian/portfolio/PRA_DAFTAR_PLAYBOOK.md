# Pra-daftar PLAYBOOK_10 dan RAWAK_PADAN_10 (25 Okt 2026, 12:44 MYT)

Status: **pra-daftar**. Ditulis dan di-commit (cawangan pratonton `pt/playbook`, asas `938b720`) SEBELUM ujian dalam sampel
dijalankan dan SEBELUM kedua-dua portfolio dikira atas Lejar Penuh hadapan. Rekod sahaja: tiada order, tiada wang sebenar.
Lima portfolio sedia ada (RS_10, RAWAK_10, GABUNGAN_10, TOP1_10, RAWAK_KAEDAH_10) tidak diubah.

Latar: audit 25 Okt 2026 mendapati sistem tiada saiz ikut risiko, had heat, had sektor atau brek portfolio. Heat RS_10
≈ 34–49% ekuiti (rawak 11–14%); RS_10 hadapan memilih saham ATR14 median 9.2% (backtest 5.4%) dan nilai dagangan < USD5 juta;
MDD backtest berpunca daripada tumpuan sektor; ATR14% ≤ 6% satu-satunya penapis yang memperbaiki MDD dalam set penuh dan set
"buang 40 pemenang". Parameter di bawah ditetapkan oleh pengguna; tiada parameter dipilih daripada hasil.

## 1. Soalan
- **Nilai pemilihan**: dengan rangka risiko yang sama, adakah susunan RS (80–94) mengatasi susunan rawak? (PLAYBOOK_10 lawan
  RAWAK_PADAN_10)
- **Nilai rangka risiko**: adakah saiz ikut risiko + had heat/sektor + brek mengurangkan kejatuhan berbanding RS_10/RAWAK_10?

## 2. Alam calon (sama bagi kedua-dua portfolio)
- Setiap sesi beli d: semua posisi Lejar Penuh (`lejar/terbuka.csv` + `lejar/tutup/*.csv`) dengan `tarikh_beli` = d, digabung
  menjadi satu calon setiap saham (harga beli = buka d dalam Lejar; tarikh isyarat = sesi sebelumnya; `id_kaedah` = semua
  kaedah yang memberi isyarat). Mula jejak: **16 Okt 2026** (sesi beli pertama Lejar).
- Calon mesti lulus SEMUA penapis di bawah. Ciri dikira pada **tutup tarikh isyarat** daripada stor harga repo
  (`data/harga/stor/`), `data/rs/rs_pasaran.csv`, `data/kumpulan/gred_kumpulan_sejarah.csv` dan kalendar earnings; tiada pandang
  hadapan. Ciri yang tiada bagi tarikh itu = **tidak lulus** (sebab direkod).

| # | Penapis | Takrif tepat |
|---|---|---|
| P1 | Harga | tutup isyarat ≥ USD10 |
| P2 | Kecairan | median 20 bar (bar isyarat dan 19 sebelumnya) tutup × volum ≥ USD20 juta |
| P3 | Sejarah | bilangan bar stor hingga bar isyarat ≥ 252 |
| P4 | Sah data | (a) masih posisi Lejar pada larian (Lejar menapis `tidak_layak`: ambil alih, tidak cair, kelas berganda); (b) tiada dalam `data/ambil_alih.csv` dengan `tarikh_umum` ≤ tarikh isyarat; (c) bukan "semak data": tiada pergerakan tutup-ke-tutup > 40% dalam 60 pulangan berakhir bar isyarat (takrif `trend_status.py`) |
| P5 | RS pasaran | 80 ≤ RS ≤ 94 (`rs_pasaran.csv`, tarikh isyarat) |
| P6 | Trend Template | tutup > SMA50 > SMA150 > SMA200 (purata mudah tutup); SMA200 > SMA200 21 bar sebelumnya; tutup ≥ 0.85 × tinggi 52 minggu (tinggi intrahari tertinggi 252 bar hingga bar isyarat), iaitu ≤ 15% di bawah tinggi (lebih ketat daripada syarat ≤ 25%) |
| P7 | Industri v2 | gred industri (`gred_kumpulan_sejarah.csv`, jenis Industri, tarikh isyarat; industri = `papertrade/peta_industri.csv`) bukan E. Industri tanpa gred (< 3 saham) = tidak lulus (tiada sandaran sektor) |
| P8 | Volatiliti | ATR14 ÷ tutup ≤ 6% (ATR14 = purata mudah 14 julat sebenar, `keluar_lorong.atr`) |
| P9 | Jurang buka | harga beli (buka d) ÷ tutup isyarat − 1 ≤ +3% (diketahui pada buka; lebih = langkau) |
| P10 | Earnings | tiada sesi reaksi earnings dalam 5 sesi dagangan NYSE selepas tarikh isyarat (S1–S5; S1 = sesi beli). Sesi reaksi: masa pra-pasaran → hari earnings; selepas pasaran → sesi berikutnya; masa tidak diketahui → kedua-duanya. Kalendar: `kalendar_earnings.muat` (Nasdaq sejarah + `earnings_nasdaq.json` + yfinance + tambahan disahkan); masa daripada `tarikh_pendapatan.csv` / `earnings_nasdaq.json`. Lulus hanya jika liputan diketahui: earnings seterusnya yang boleh dipercayai (`kalendar_earnings.seterusnya`) selepas S5, ATAU earnings terakhir ≤ 40 hari kalendar sebelum tarikh isyarat, ATAU `earnings_nasdaq.json` meliputi S1–S5 dan saham itu ada dalamnya. Selainnya "earnings tidak diketahui" = tidak lulus |
| P11 | Rejim | SPY tutup > SMA200 SPY pada tarikh isyarat; jika tidak, tiada belian baharu pada sesi itu |

## 3. Susunan calon dalam sesi
- PLAYBOOK_10: RS menurun. Seri dipecah rawak berbenih tetap: calon diisih ikut saham, dipermutasi dengan
  `np.random.default_rng([0, YYYYMMDD sesi beli])`, kemudian diisih stabil ikut RS menurun.
- RAWAK_PADAN_10: permutasi rawak sahaja (tanpa RS) dengan `np.random.default_rng([1, YYYYMMDD sesi beli])`. Jejak hadapan
  memakai benih 1 sahaja; kajian dalam sampel melaporkan median 20 benih (0–19).

## 4. Saiz, heat dan had (sama bagi kedua-dua)
- Ekuiti mula 1.0. Ekuiti = tunai + Σ amaun × tutup ÷ harga beli.
- Paras keluar awal = tutup isyarat − 4 × ATR14 isyarat. r = (harga beli − paras awal) ÷ harga beli (R sesaham = r × harga beli).
  r ≤ 0 → langkau.
- Saiz sasaran = ekuiti tutup semalam × min(15%, 1% ÷ r) (risiko 1% ekuiti, had 15% setiap posisi). Amaun = min(tunai, sasaran);
  amaun < 1% ekuiti semalam → langkau (tunai tidak cukup).
- Heat = Σ nilai × jarak ke paras keluar ÷ ekuiti, jarak = max(0, (tutup − paras) ÷ tutup) pada tutup semalam; posisi yang dibeli
  pada sesi sama = amaun × r. Belian yang menjadikan heat > 10% ditolak (calon seterusnya dinilai).
- Maksimum 20 posisi; ≤ 3 posisi setiap `sektor_us` dan ≤ 2 setiap `industri_us` (sektor_us = `sektor_pasaran.SEKTOR_INDUSTRI`
  bagi industri peta); ≤ 3 belian baharu setiap sesi; satu posisi setiap saham (boleh dibeli semula selepas keluar).
- Kos 0.25% setiap belah: hasil jual = amaun × harga keluar ÷ harga beli × (1 − 0.0025) ÷ (1 + 0.0025).

## 5. Keluar
- K1 Chandelier tutup 4×ATR14 seperti lorong 2 (`keluar_lorong.lorong_henti`): setiap bar j ≥ bar beli, puncak = tutup tertinggi
  sejak beli, paras = max(paras, puncak − 4 × ATR14[j]) (hanya naik); tutup < paras → jual pada buka bar berikutnya.
- K2 Henti masa: pada tutup bar ke-20 (bar beli = 1), jika tutup < harga beli + 1R → jual pada buka bar berikutnya. Disemak sekali.
- K3 Delist: tiada bar ≥ 10 sesi SPY berturut → ditutup pada tutup bar terakhir (seperti `tidak_layak`).
- K4 Brek portfolio (selepas setiap tutup; puncak = ekuiti tertinggi setakat itu, minimum 1.0):
  - kejatuhan ≥ 15% dari puncak → tiada belian baharu mulai sesi berikutnya, sehingga tutup dengan kejatuhan ≤ 10% (pulih ke −10%);
  - kejatuhan ≥ 25% → `kill_switch`: semua posisi dijual pada buka sesi berikutnya dan tiada belian baharu lagi. Mula semula hanya
    dengan keputusan pengguna dan pra-daftar baharu.
- Susunan dalam sesi: jualan pada buka (K1, K2, K4 yang dicetus pada tutup semalam) → belian pada buka → nilai pada tutup → semak
  K1/K2/K3/K4.

## 6. Rekod beku (kestabilan bina semula)
Portfolio dibina semula setiap malam daripada Lejar Penuh (`lejar.yml` → `standard/portfolio_slot.py`). Supaya keputusan lampau
tidak berubah apabila tetingkap stor (520 bar) atau kalendar bergerak, keputusan penapis setiap sesi beli direkod sekali dan
dibekukan: `portfolio_slot/PLAYBOOK_calon.csv` (calon lulus dan cirinya, tambah sahaja) dan `portfolio_slot/PLAYBOOK_tapis.csv`
(bilangan calon dan gagal setiap penapis setiap sesi). Sesi yang sumber RS atau gred industrinya belum ada bagi tarikh isyarat
ditangguh sehingga 5 sesi, kemudian direkod dengan sebab "data tiada". Calon beku yang tidak lagi ada dalam Lejar (bina semula
tidak_layak) atau kemudian tersenarai ambil alih dengan `tarikh_umum` ≤ tarikh isyarat digugurkan. Sesi 16–23 Okt 2026 dinilai
pada 25 Okt 2026 (selepas berlaku, sebelum hasil dikira); **tempoh hadapan bersih bermula sesi 26 Okt 2026**.

## 7. Penilaian (dirancang lebih awal)
- Ukuran: pulangan, MDD, heat harian median/p90, tunai purata, tempoh di bawah puncak, R-multiple dagangan keluar, lawan SPY
  dan EW alam Shariah (`data/analisis/ew_harian.csv`) tempoh sama.
- Perbandingan utama selepas ≥ 250 sesi hadapan bersih (≈ Okt 2027); semakan interim 125 sesi rekod sahaja:
  1. PLAYBOOK_10 − RAWAK_PADAN_10 = nilai pemilihan RS dalam rangka risiko.
  2. RAWAK_PADAN_10 lawan RAWAK_10 dan PLAYBOOK_10 lawan RS_10 = kesan rangka risiko (pulangan dan MDD).
  3. PLAYBOOK_10 lawan EW dan SPY.
- Analisis tambahan dibenarkan (bukan portfolio rasmi): 20 benih RAWAK_PADAN hadapan untuk persentil.
- Tiada perubahan peraturan semasa jejak. Pembetulan pepijat yang tidak mengubah peraturan dicatat dalam §8 dengan tarikh.
  Perubahan peraturan = portfolio baharu (nama baharu) dengan pra-daftar baharu.

## 8. Ujian dalam sampel (dirancang; `kajian/portfolio/kaji_portfolio.py playbook`)
- Enjin portfolio yang SAMA (`portfolio_slot.bina_pb`) atas calon = dagangan enjin v1.2 134 kaedah (set 431 tolak 8 saham
  bermasalah, `data_mentah`), masuk Nov 2020 – Okt 2026, satu calon setiap saham setiap sesi masuk.
- Ciri daripada `data_mentah` (harga dilaras; harga ≥ USD10 atas harga dilaras), RS `kajian/rs/rs_pasaran_431.csv.gz`, skor
  industri v2 `kaji_portfolio.skor_industri` (cawangan `kajian-gred`; E = skor ≤ 20), earnings `data/pemangkin/tarikh_pendapatan.csv`
  (masa ikut lajur `masa`), SPY `index_benchmark.csv`. P4(a)/(b) tidak terpakai (alam set 431 semasa); P4(c) terpakai.
- Larian: PLAYBOOK (benih seri 0; juga benih 0–19 untuk sebaran), RAWAK_PADAN (benih 0–19), set penuh dan set "buang 40
  pemenang" (40 saham pulangan tertinggi 2020–2026, seperti `tahan`). Rujukan: RS pasaran dan rawak 10 × 10% lorong 2.
- Laporan: CAGR, MDD, heat harian median/p90, R-multiple, tahun demi tahun, persentil PLAYBOOK lawan 20 benih RAWAK_PADAN.
  Amaran: dalam sampel, alam penyintas.

## 9. Pindaan
- 25 Okt 2026, sebelum sebarang hasil (dalam sampel atau hadapan) dikira — penjelasan pelaksanaan, bukan perubahan peraturan:
  1. Masa earnings bentuk HH:MM dalam `tarikh_pendapatan.csv`: < 09:30 = pra-pasaran, ≥ 16:00 = selepas pasaran, selainnya
     tidak diketahui.
  2. Jarak heat dihad kepada [0, 1] (paras ≤ 0 = seluruh nilai berisiko; tidak berlaku dengan ATR14% ≤ 6%).
  3. Perincian risiko lima portfolio lama (paparan sahaja): paras keluar lorong kaedah = henti kaedah Lejar (`henti`);
     tiada henti = seluruh nilai dikira berisiko.

## 10. Catatan selepas ujian dalam sampel (25 Okt 2026; tiada perubahan peraturan)
- K4 brek ("tiada belian baharu sehingga pulih ke −10%") bersifat kekal: tanpa belian, ekuiti tunai tidak boleh pulih selepas
  posisi sedia ada keluar. Dalam sampel ia tercetus dalam 20/20 benih kedua-dua portfolio dan tidak dilepaskan
  (`kajian/KAJIAN_PORTFOLIO.md`, bahagian Rangka risiko). Jejak hadapan kekal dengan peraturan ini; sebarang pembetulan
  memerlukan keputusan pengguna dan portfolio baharu dengan pra-daftar baharu (§7).
