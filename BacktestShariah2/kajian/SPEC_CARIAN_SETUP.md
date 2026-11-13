# SPEC_CARIAN_SETUP — pradaftar carian setup berterusan (pusingan CS01)

**Dipradaftar 13 Nov 2026**, dikomit **sebelum** mana-mana keputusan carian dilihat. Kod: `kajian/carian_setup/`.
Keputusan pengguna 13 Nov 2026 (`koordinator/keputusan.csv`): carian kombinasi indikator dan penalaan dari benih M/N
dibenarkan **berterusan dan tanpa had bilangan**; **backtest dahulu, papertrade kemudian**. Ini pengecualian kedua kepada
"jangan cadang carian kombinasi lagi pada data lama" (`CLAUDE.md`).

## 1. Apa yang dicari (requirement pengguna, disahkan 13 Nov 2026)

Satu setup lengkap — bila masuk, bagaimana pegang, bila keluar — yang menangkap saham ketika ia mula naik kuat
(≥ 5 % minggu pertama, lebih baik ≥ 10 %, kemudian naik lagi 2–4 minggu) dan memegangnya selagi ia naik.

Peraturan WAJIB setiap setup (bukan pilihan carian):

| Perkara | Peraturan |
|---|---|
| Swing | tiada jual pada hari beli; pegang paling lama 20 sesi (4 minggu), sesi 1 = hari beli |
| Henti rugi | wajib, longgar sahaja: `H1` −8 % · `H2` −10 % · `H3` 3×ATR14 · `H4` 4×ATR14 di bawah harga beli |
| Sasaran untung | tiada sasaran tetap (10 % ialah matlamat, bukan paras jual) |
| Keluar | ikut indikator atau kombinasi dua indikator |

## 2. Apa ini, dan apa ia BUKAN

- Hasil ialah **papan pangkat backtest**, bukan bukti. `laporan/KAD_SKOR.md` kekal satu-satunya keputusan wang sebenar.
- Dapatan lama tidak dibatalkan: tinjauan ~1.35 juta gabungan (`KAJIAN_ISYARAT_KOMBINASI.md`) mendapati yang "terbaik"
  tidak mengatasi pilihan rawak pada saham lain. Sebab itu angka papan dilaporkan pada saham dan tahun yang carian
  **tidak pernah lihat** (§5 Kunci), bersebelahan dengan setup yang dipilih **rawak** daripada ruang yang sama.
- Tiada setup masuk papertrade daripada kajian ini tanpa keputusan pengguna yang berasingan.

## 3. Data dan tempoh

| Peranan | Saham | Tarikh isyarat |
|---|---|---|
| **Latih** (cari) | set 431 `data_mentah/dataset_S1–S4.csv` | 2020-01-02 … 2023-06-30 |
| **Sah** (pilih) | set 431 | 2023-07-03 … 2026-08-28 |
| **Kunci K1** (lapor) | 1,000 saham dipilih rawak (benih 20261113) daripada saham Release `autotune-data-a02` yang TIADA dalam set 431 | 2010-01-04 … 2019-12-31 |
| **Kunci K2** (lapor) | 1,000 saham yang sama | 2020-01-02 … 2026-08-28 |

Layak pada bar isyarat: ≥ 252 bar sejarah; set 431: tutup ≥ USD 10 dan purata 20 hari (tutup × volum) ≥ USD 1 juta;
Kunci: saham dalam universe bulanan titik-masa A02 (`teras/data.topeng`). Kaveat kekal: tiada saham delist dalam
kedua-dua set (angka condong ke atas); K2 berkongsi tahun dengan Latih/Sah (saham berbeza, pasaran sama).

## 4. Mekanik dagangan (dikunci)

- Isyarat dikira pada TUTUP bar *i* (data ≤ *i*); beli pada BUKA bar *i*+1, harga `P`. Pencetus = hari pertama isyarat
  (benar hari ini, palsu semalam).
- Henti: paras ditetapkan semasa beli (`H3`/`H4` guna ATR14 bar *i*). Aktif intrahari **mulai sesi 2**: buka ≤ paras →
  jual pada buka; rendah ≤ paras → jual pada paras. Sesi 1 (hari beli): jika TUTUP ≤ paras → jual pada buka esok.
- Keluar indikator: syarat dinilai pada tutup sesi 1…19 → jual pada BUKA sesi berikutnya.
- Tiada keluar hingga sesi 20 → jual pada TUTUP sesi 20.
- Kos 0.5 % pusingan. `R` = harga jual ÷ `P` − 1 − 0.005.
- Saham yang tiada 20 sesi selepas beli tidak dikira.

## 5. Ruang carian

**Masuk** = satu pencetus DAN 0, 1 atau 2 penapis.

- Pencetus indikator: senarai `PENCETUS` dalam `carian_setup/atom.py` (silang MA, MACD, RSI, pecah tinggi N hari,
  Keltner/Bollinger, squeeze, Supertrend, ADX, Ichimoku, Stochastic, gap/lonjakan volum, tapak, undur dalam trend).
- Benih M: lajur `sig` setiap modul `AUTOTUNE/kaedah/Mxx.py` dengan parameter asal, **dan dua varian parameter** setiap
  kaedah: setiap parameter `tala = Y` diambil seragam dalam [`bawah`, `atas`] `param_julat.csv` (benih 20261113 + nombor
  varian). Varian yang gagal dijalankan dicatat dan ditinggalkan.
- Benih N: lajur `sig` setiap masuk N unik dalam `kod/kaedah/N*.py`.
- Penapis (keadaan): senarai `PENAPIS` (trend MA, RSI, MACD, ADX, Supertrend, kekuatan relatif, jarak puncak 52 minggu,
  volum, ATR %, squeeze, rejim QQQ, SPY > SMA200, bentuk lilin).

**Henti** = `H1`–`H4`. **Keluar** = senarai `KELUAR` (24 atom indikator) secara tunggal, pasangan ATAU (mana-mana satu
menyala), pasangan DAN (kedua-dua menyala), dan `X00` (tiada keluar indikator: henti dan had 20 sesi sahaja).

Setiap (masuk × henti × keluar) dinilai. Tiada had bilangan; bilangan sebenar dilaporkan.

## 6. Ukuran dan pemilihan (dikunci)

Setiap setup, setiap tempoh: `n`, purata `R`, sisihan piawai, **had bawah** `LB` = purata − 2 × sd ÷ √n.

1. **Peringkat besar** (semua kombinasi; isyarat bertindih pada saham sama dibenarkan): syarat `n` ≥ 100 dalam Latih
   DAN Sah. `skor` = min(`LB` Latih, `LB` Sah). Simpan 8 (henti × keluar) terbaik setiap peraturan masuk, dan satu
   (henti × keluar) rawak setiap peraturan masuk (kolam rawak).
2. **Peringkat tepat**: 2,000 teratas ikut `skor` (paling banyak 3 setiap peraturan masuk) dinilai semula dengan
   peraturan **satu posisi setiap saham** (isyarat semasa saham masih dipegang diabaikan). `skor tepat` dikira sama;
   syarat `n` ≥ 100 kekal.
3. **Papan 10 teratas** = susun `skor tepat` menurun; setiap benih muncul sekali sahaja (keluarga = ID kaedah M
   termasuk variannya, ID masuk N, atau ID pencetus indikator).
4. **Kunci**: 10 teratas, 200 teratas `skor tepat`, dan 200 setup rawak (benih 20261113, daripada kolam rawak) dinilai
   pada K1 dan K2 dengan peraturan satu posisi setiap saham. **Kunci tidak mengubah pangkat**; ia hanya dilaporkan.

Peratus yang dipaparkan bagi setiap setup papan (Latih, Sah, K1, K2):
bilangan dagangan · purata `R` · % menang · **% dagangan ≥ +10 %** · **% ≥ +20 %** · % rugi ≤ −8 % ·
% saham naik ≥ 5 % pada tutup sesi 5 (tanpa kos; sifat masuk) · purata sesi pegang · purata seminggu
(= purata `R` ÷ sesi pegang × 5) · lebihan atas beli rawak hari sama (purata `R` setup − purata `R` semua bar layak
pada tarikh isyarat yang sama dengan henti dan keluar yang sama) · MDD buku harian (semua posisi sama berat).

Tiga tapis (lajur ✓/✗, maklumat untuk keputusan papertrade kemudian):

| Tapis | Lulus jika |
|---|---|
| T1 tahan | `skor tepat` > 0 pada keempat-empat pilihan henti dengan masuk dan keluar yang sama |
| T2 tidak dilihat | purata `R` > 0 dalam K1 DAN K2 |
| T3 kalahkan rawak | purata `R` Kunci (K1+K2) > persentil ke-95 purata `R` Kunci 200 setup rawak |

Semakan kejujuran yang dilaporkan bersama: Spearman antara `skor tepat` dan purata `R` Kunci merentas 200 teratas
(adakah pangkat carian meramal hasil pada saham yang tidak dilihat), dan kedudukan median 10 teratas dalam taburan
rawak.

## 7. Keluaran

`kajian/CARIAN_SETUP.md` (dijana `carian_setup/lapor.py`), `kajian/carian_setup/hasil/*.csv`. Fail perantaraan besar
ditulis ke folder kerja di luar repo. Jangan sunting keluaran secara manual.

### Pindaan 13 Nov 2026 (a) — keluarga F (sebelum carian dijalankan; tiada keputusan dilihat)

Keputusan pengguna 13 Nov 2026: kaedah baharu daripada carian ini didaftarkan dengan nombor bermula **`Fxx`**.
Setiap setup papan mendapat ID `F01`, `F02`, … mengikut kedudukan papan, dalam `data/registry_F.csv` (dijana
`carian_setup/lapor.py`). ID **kekal**: takrif (`pencetus|penapis|henti|keluar`) yang sudah berdaftar mengekalkan
ID-nya pada pusingan berikutnya; takrif baharu mendapat nombor seterusnya. Lajur `status` = `BACKTEST` bermaksud belum
papertrade: tiada modul `kod/kaedah/Fxx.py`, tiada dalam Lejar atau kad skor. Pendaftaran tidak mengubah pemilihan
atau pangkat (§6).

## 8. Apa yang TIDAK dibuat dalam CS01

Penalaan Optuna penuh 1,303 parameter kaedah M (hanya dua varian rawak setiap kaedah), gabungan ≥ 3 penapis, gabungan
≥ 3 indikator keluar, carian pada set 2000 penuh (dirancang melalui Actions selepas keputusan pengguna), dan simulasi
portfolio berslot. Pusingan seterusnya memerlukan pindaan bertarikh pada fail ini **sebelum** dijalankan.
