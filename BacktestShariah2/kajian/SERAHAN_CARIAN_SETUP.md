# Serahan: Carian Setup (CS) dan keluarga F — keadaan pada 14 Nov 2026 (selepas CS06)

Ditulis pada akhir sesi kerja 13–14 Nov 2026 dan dikemas kini pada 14 Nov 2026 selepas pusingan CS05 dan CS06, supaya chat baharu boleh menyambung tanpa membaca chat lama. Fail ini ialah nota serahan (ditulis tangan, bertarikh); nombor di sini dipetik daripada fail hasil yang dinamakan, dan fail hasil itulah sumber kebenaran.

**Baca mengikut susunan ini:** fail ini → `kajian/SPEC_CARIAN_SETUP.md` (pradaftar + pindaan (a)–(i)) → `kajian/CARIAN_SETUP.md` (papan semasa = CS06) → `kajian/carian_setup/hasil/CS06/SEMUA_PENCETUS_LENGKAP.md` (setiap kaedah) dan `hasil/CS06/TALA.md` → `kajian/KAJIAN_PRASYARAT_PAKAR.md` → `jejak_f/RINGKASAN.md`.

**Ringkasan CS05 dalam lima baris (butiran §9):** (1) prasyarat MENOLONG kadar tangkap bagi hampir semua kaedah, jauh melebihi plasebo; (2) hampir semuanya datang daripada SATU prasyarat: earnings dalam 1–5 sesi akan datang; (3) prasyarat pasaran panik menaikkan kadar lari SEMUA saham (bila membeli), bukan kemahiran memilih, dan kena henti naik bersama; prasyarat aliran ikut trend dan sektor/industri kuat tidak menolong; (4) pencetus (kaedah M/N/indikator) menambah sedikit sahaja di atas prasyarat + penapis; (5) pegang/keluar (pindaan (j)): pegang hampir 20 sesi dengan henti longgar; indikator keluar jarang mengatasi "tiada keluar indikator".

**Ringkasan CS06 (butiran §9a):** (6) memangkatkan masuk terus ikut TANGKAP PENUH (naik ≥ 5 % minggu pertama DAN dijual dengan untung ≥ 10 %) tidak mengubah kesimpulan: prasyarat menolong 432 daripada 461 kaedah, masih kerana earnings 1–5 sesi; tetapi separuh daripada 200 teratas dan papan bertukar; (7) setup "terbaik" papan jumlah (`F62`, 37 %) bergantung pada kira-kira 10 hari dasar pasaran (Dis 2018, Mac 2020); setup papan pilih (`F39`, `F40`, `F58`, ~20–22 % lawan rawak 8–11 %) berdagang setiap tahun; (8) **tala bersama prasyarat TIDAK menolong**: hanya 6 daripada 18 anak mengatasi induk pada saham tidak dilihat, 4 daripada 17 pada 2025–26.

**Status (keputusan pengguna 14 Nov 2026): backtest dahulu. JANGAN mula jejak hadapan bagi setup CS05/CS06.**

## 1. Apa yang pengguna cari (disahkan pengguna 13 Nov 2026)

Satu setup lengkap (bila masuk, bagaimana pegang, bila keluar) yang **paling kerap menangkap saham ketika ia mula naik kuat**, dan memegangnya selagi ia terus naik.

1. Saham yang dicari: naik ≥ 5 % dalam minggu pertama, lebih baik 10 %, kemudian naik lagi 2–4 minggu.
2. Masuk: kombinasi indikator + parameter yang paling kerap memberi isyarat sebelum kenaikan begitu.
3. Pegang: selagi untung dan selagi naik; tiada jual awal. 10 % ialah sasaran untuk dicapai, BUKAN paras jual.
4. Keluar: kombinasi indikator yang memberitahu kenaikan sudah tamat.
5. Henti rugi: wajib.
6. Swing: beberapa hari hingga 4 minggu; tiada beli dan jual pada hari yang sama.
7. Cara mencari: mesin sentiasa mencari dan menala dari benih (kaedah M dan N, indikator sedia ada); tiada had bilangan, tiada yang dibekukan.
8. Hasil: ranking setup terbaik dengan peratus.
9. Susunan: **backtest dahulu, papertrade kemudian.**
10. Kos: jimat token.
11. (14 Nov) Struktur dua lapis: **prasyarat** (isyarat BUKAN daripada saham itu sendiri: pasaran, keluasan, sektor, industri, earnings) dahulu, kemudian **syarat** (saham itu sendiri). Pengguna menilai kita terlalu fokus pada saham tanpa prasyarat.
12. **Keputusan pengguna 14 Nov 2026:** CS01–CS04 ialah pusingan "syarat sahaja". Pusingan seterusnya (di chat baharu) ialah **larian semula untuk SEMUA kaedah (bukan 50 teratas sahaja) dengan prasyarat DAN syarat**: "kita akan run sekali lagi dengan prasyarat semuanya".

**Ukuran yang betul = KADAR TANGKAP** ("lari": naik ≥ 5 % minggu pertama, capai ≥ 10 % sebelum henti −8 %, masih ≥ 10 % pada minggu ke-4), lawan saham rawak pada hari dan tercile ATR% yang sama. BUKAN purata setiap dagangan, BUKAN banding indeks.

## 2. Cara bekerja dengan pengguna (pelajaran sesi ini)

- Jawapan pendek, Bahasa Melayu mudah; jadual tiga lajur di jawapan penutup; notifikasi telefon setiap giliran (CLAUDE.md).
- Pengguna menyerahkan keputusan teknikal kepada Claude ("apa sahaja keputusan di tangan anda, tetapi sentiasa berbalik kepada matlamat saya"). Kurangkan soalan; putuskan, laksana, lapor.
- Jangan menolak sasaran pengguna sebelum mengukurnya. Jangan reka had sendiri (cth. "maks 4 calon") atau membekukan carian.
- Jangan tukar kayu ukur. Kesilapan saya dalam sesi ini: memangkatkan ikut purata setiap dagangan (CS01/CS02), kemudian mengesyorkan berhenti kerana kalah SPY pada MDD −10 %. Pengguna membetulkan: "baca balik chat kita, apa yang saya cari". Jawapannya §1.
- Jika tersilap jangka, cakap terus (cth. isyarat pertama jejak F direkod selepas Lejar, bukan selepas `harga_harian`).
- (14 Nov, CS05) Sebelum mengisytiharkan sesuatu pusingan "siap", semak SETIAP bahagian setup lawan §1: masuk DAN henti/pegang/keluar. Saya melaporkan CS05 siap dan mencadangkan jejak hadapan sedangkan pegang/keluar masih dipilih ikut purata setiap dagangan (warisan pindaan (d)); pengguna: "check betul-betul matlamat backtest ini; tak boleh tersasar". Pembetulan = pindaan (j). Jangan cadangkan papertrade selagi backtest belum lengkap.
- Tetap terpakai tanpa pengecualian: tiada order, tiada wang sebenar sehingga `laporan/KAD_SKOR.md` menanda TERBUKTI; pradaftar bertarikh SEBELUM hasil dilihat; fail dijana tidak disunting tangan.

## 3. Apa yang sudah dibuat

| Bila | Apa | Fail |
|---|---|---|
| 13 Nov | Pradaftar carian setup + enjin carian (numba) + ujian | `kajian/SPEC_CARIAN_SETUP.md`, `kajian/carian_setup/cs_*.py`, `ujian/test_carian_setup.py` |
| 13 Nov | **CS01**: set 431 → Kunci 1,000 saham lain | `hasil/CS01/` → `F01`–`F10` |
| 13 Nov | **CS02**: kumpulan A → kumpulan B (set 2000), dua era + tahun tidak dilihat | `hasil/CS02/` → `F11`–`F20` |
| 13 Nov | Semakan portfolio 10 slot pada MDD −10 % (pindaan (c)) | `hasil/CS02/PORTFOLIO.md` |
| 13 Nov | **CS03**: pangkat semula ikut kadar tangkap (pindaan (d)) | `hasil/CS03/`, `hasil/CS03/TOP50.md` → `F21`–`F30` |
| 13 Nov | **CS04**: tala parameter di sekitar pemenang (pindaan (e)) | `hasil/CS04/`, `kajian/CARIAN_SETUP.md` → `F31`–`F38` |
| 13 Nov | Kohort jejak hadapan F (pindaan (f), (g)) + workflow | `jejak_f/`, `.github/workflows/jejak_f.yml`, `cs_hadapan.py` |
| 14 Nov | Pecahan prasyarat lawan syarat bagi 38 setup F | `hasil/PRASYARAT/PEMBAHAGIAN_F.md` (`cs_ringkas.py`) |
| 14 Nov | Tinjauan 38 prasyarat (pindaan (h)) | `hasil/PRASYARAT/LAPORAN.md`, `prasyarat.csv` (`cs_prasyarat.py`) |
| 14 Nov | Kajian pakar prasyarat/syarat (carian web) | `kajian/KAJIAN_PRASYARAT_PAKAR.md` |
| 14 Nov | Rekod SEMUA kaedah dengan syarat sahaja (asas untuk larian berprasyarat): 500 pencetus, 182,903 peraturan masuk | `hasil/CS03/SEMUA_PENCETUS.md` + `.csv`, `hasil/CS03/semua_masuk.csv.gz` (`cs_tangkap.py <kerja> semua`) |
| 14 Nov | **CS05**: prasyarat + syarat bagi SEMUA kaedah (pindaan (i) + tambahan, dikomit sebelum dijalankan); 103,088,000 peraturan masuk + larian plasebo | `hasil/CS05/` (`LAPORAN.md`, `SEMUA_PENCETUS.md`, `papan.csv`, `PADANAN.csv`, `senarai_kunci.csv`, `terbaik_prasyarat.csv.gz`), `kajian/CARIAN_SETUP.md` → `F39`–`F57` (`cs_lapis.py`, `cs_cs05.py`) |
| 14 Nov | `data/registry_F.csv` mendapat lajur `prasyarat` dan `syarat` (semua 57 baris) | `cs_lapor.LAJUR_F`, `cs_cs05.daftar`, `hasil/PRASYARAT/PEMBAHAGIAN_F.md` |
| 14 Nov | **CS06 bahagian A** (pindaan (k)): carian 103,088,000 peraturan diulang dengan sasaran tangkap penuh (pegang piawai H4 + X00) + plasebo; papan, setiap kaedah, setup lengkap ikut tangkap penuh sendiri; jadual taburan belian mengikut tahun | `CS_PUS=CS06 cs_cs05.py`, `cs_lengkap.py`; `hasil/CS06/` (`LAPORAN.md`, `SEMUA_PENCETUS*.md`, `TOP50.md`, `papan.csv`), `kajian/CARIAN_SETUP.md` → `F58`–`F69` |
| 14 Nov | **CS06 bahagian B: tala bersama prasyarat** (pindaan (k)): 240 varian pencetus + ambang penapis + ambang prasyarat (36 prasyarat berambang, `cs_lapis.GRID_PRA`/`Mentah`), ikut dataran; induk lawan anak pada kumpulan B | `cs_tala6.py`; `hasil/CS06/TALA.md`, `tala.csv` → `F70`–`F87` |
| 14 Nov | PR #48 digabung ke `main` (CS05 + pindaan (k)); `lejar.yml` mencetus `jejak_f.yml` terus selepas Lejar dispatch penjaga | `.github/workflows/lejar.yml` |
| 14 Nov | **CS05 peringkat lengkap** (pindaan (j), selepas semakan lawan matlamat): henti × keluar dipilih ikut kadar dagangan "jadi" (dijual dengan untung ≥ 10 %), bagi 19 setup papan dan bagi setiap kaedah (S dan P); `F39`–`F57` kekal ID, henti/keluar diganti | `cs_lengkap.py`; `hasil/CS05/LAPORAN.md` §3–§5, `SEMUA_PENCETUS_LENGKAP.md`, `TOP50.md` |

Semua laluan `hasil/…` di bawah `BacktestShariah2/kajian/carian_setup/`. PR #45–#48 sudah digabung ke `main` (CS05 termasuk); kerja CS06 berada di branch `claude/dreamy-lovelace-38z7wm` (lihat §7).

## 4. Hasil utama

**Ruang carian.** 500 pencetus (49 indikator + 134 benih M × (asal + 2 varian parameter rawak) + 49 benih N) × 466 gabungan 0–2 daripada 30 penapis = 233,000 peraturan masuk; × 4 henti × 577 peraturan keluar = **537,764,000 kombinasi**, diuji pada set 431 (367.4 juta cukup dagangan) dan sekali lagi pada set 2000 (422.1 juta). CS03 memangkatkan semula 233,000 peraturan masuk (182,903 cukup isyarat). CS04: 144 varian parameter + ~3,200 sel ambang.

**Mekanik (dikunci, SPEC §4).** Isyarat pada tutup → beli buka esok; tiada jual hari beli; henti H1 −8 %, H2 −10 %, H3 3×ATR14, H4 4×ATR14; keluar ikut indikator dinilai pada tutup sesi 1–19; pegang paling lama 20 sesi; kos 0.5 % pergi balik.

| Pusingan | Dapatan | Sumber |
|---|---|---|
| CS01 | Setup teratas mengatasi rawak hanya pada tahun yang sama dengan carian (K2 +2.05 % lawan −0.30 %), tidak pada K1 (−0.26 % lawan −0.23 %) | `hasil/CS01/LAPORAN.md` |
| CS02 | Median 200 teratas setiap dagangan K1/K2/K3 +1.68/+2.16/+0.95 % lawan rawak ≈ −0.3 %. Pemenang kebanyakannya "QQQ OFF + ≥ 30 % di bawah puncak, pegang ~18.5 sesi, H4". Lebihan atas beli rawak HARI SAMA cuma +0.3 hingga +0.5 % | `hasil/CS02/LAPORAN.md` |
| Portfolio | `F11`–`F20` dalam 10 slot pada MDD −10 %: +0.6 hingga +2.1 % setahun lawan SPY +4.3 %. Isyarat berkelompok; `F11` hanya mengambil 1,277 daripada 17,371 isyarat. **Purata setiap dagangan bukan hasil akaun.** | `hasil/CS02/PORTFOLIO.md` |
| CS03 | Papan menangkap pelari 11–15 % lawan 10–12 % rawak. Median lebihan 200 teratas +2.15/+2.12/+1.38 mata (K1/K2/K3). Kebanyakannya juga lebih kerap kena henti | `hasil/CS03/LAPORAN.md`, `TOP50.md` |
| CS04 | 8/10 induk ditala; 6 anak mengatasi induk pada kumpulan B, 4 pada K3 | `hasil/CS04/LAPORAN.md` |

**Setup terbaik secara keseluruhan: `F27`** (N73 tutup bawah jalur bawah Bollinger; RS ≥ 70 + ATR% ≥ 4; H4; keluar X07 DAN X21). Kumpulan B: lari 14.6 % lawan 12.1 %; capai +10 % dahulu 38.5 % lawan 34.2 %; kena henti dahulu 49.0 % lawan 48.3 %; setiap dagangan +1.7/+1.4/+3.2 % (K1/K2/K3); menang 53–56 %; pegang ~19 sesi. `F24`, `F28`, `F30` untung kecil yang konsisten.

**Kohort jejak hadapan (papertrade maya F, isyarat sejak 2026-11-13):** `F21`, `F22`, `F34`, `F27`, `F28`, `F38`, `F30` + `F24` (post-hoc, dilabel). Penjejak BERASINGAN daripada Lejar dan kad skor. Perlu ≥ 100 belian dengan tetingkap lengkap bagi setiap setup sebelum dibandingkan dengan backtest.

**Kaveat tetap:** tiada saham delist (condong ke atas); set 2000 bukan tapisan Shariah; papan ialah pangkat backtest, BUKAN bukti.

## 5. Ukuran awal dalam chat (13 Nov; tiada fail lain menyimpannya)

Diukur ad hoc daripada stor harga (930–947 saham Shariah, Sep 2024 – Okt 2026) dan papertrade langsung (16 Okt – 5 Nov 2026, 26,292 posisi, 15 hari beli dalam pasaran menurun). Skripnya tidak disimpan; angka seperti dilaporkan dalam chat. Inilah asas takrif "lari".

**Beli pada buka, pegang 5 sesi** ("rawak" = mana-mana saham pada hari yang sama):

| Ukuran | Naik 5 %+ seminggu | Naik 10 %+ seminggu |
|---|---|---|
| Semua saham sejak Sep 2024 | 17.8 % (1 dalam 6) | 5.9 % (1 dalam 17) |
| Semua kaedah papertrade | 18.8 % (rawak 20.1 %) | 7.1 % (rawak 8.1 %) |
| Kaedah yang mengatasi rawak | 36 daripada 81 | 26 daripada 81 |
| M01 | 33 % (rawak 22 %) | 17 % (rawak 9 %) |
| M32 | 29 % (rawak 19 %) | 16 % (rawak 7 %) |
| M18 | 28 % (rawak 21 %) | 13 % (rawak 8 %) |
| M158 | 27 % (rawak 20 %) | 10 % (rawak 7 %) |
| M15 | 24 % (rawak 20 %) | 10 % (rawak 7 %) |
| Jatuh sebanyak itu, semua saham | 14.8 % | 4.4 % |
| Jatuh sebanyak itu, papertrade | 20.5 % (rawak 22.8 %) | 8.6 % (rawak 9.8 %) |
| Purata seminggu tertinggi antara 81 kaedah | +2.3 % | +2.3 % |

**Lebih lama dipegang** (947 saham, Sep 2024 – Okt 2026):

| Tempoh pegang | Naik 10 %+ | Naik 20 %+ | Jatuh 10 %+ | Purata |
|---|---|---|---|---|
| 1 minggu | 5.8 % | 1.2 % | 4.2 % | +0.5 % |
| 2 minggu | 12.4 % | 3.1 % | 8.5 % | +1.2 % |
| 3 minggu | 17.7 % | 5.5 % | 12.0 % | +1.8 % |
| 4 minggu | 21.7 % | 7.8 % | 14.7 % | +2.4 % |

- Saham yang naik 5 %+ pada minggu pertama: purata +10.4 % (minggu 1) → +13.2 % (minggu 4); 24 % sampai +20 %; 19 % jatuh balik sehingga rugi.
- Saham yang jatuh 5 %+ pada minggu pertama: 75 % masih rugi pada minggu 4; hanya 8 % pulih ke +10 %.
- Tiada kaedah yang PURATA 5 % seminggu; "minimum 5 % seminggu" dipakai sebagai ukuran kekerapan, bukan janji.

## 6. Prasyarat lawan syarat (14 Nov)

- **Pecahan 38 setup F:** 14 QQQ OFF, 2 QQQ ON (`F22`, `F32`), 2 SPY > SMA200 (`F23`, `F33`), 20 tiada prasyarat. Ruang carian hanya ada tiga prasyarat pasaran (`cs_atom.PENAPIS` indeks 25–27). Jadual: `hasil/PRASYARAT/PEMBAHAGIAN_F.md`.
- **Tinjauan 38 prasyarat** (kadar lari benar / palsu, kumpulan B; konsisten dalam 5 kepingan): earnings dalam 1–5 sesi akan datang 12.0 / 4.9; QQQ RSI14 < 35 11.1 / 5.3 (kena henti tidak naik, benar 4 % masa); ≤ 30 % saham di atas MA50 10.5 / 4.9; turun-naik SPY ≥ 25 % 10.3 / 5.0; SPY bawah SMA200 9.9 / 4.7; hasil tumbuh ≥ 20 % 7.6 / 4.9; QQQ OFF 6.9 / 4.5. TIDAK membantu: sektor 3 teratas, industri 20 % teratas, QQQ ON, QQQ dekat puncak, turun-naik rendah, 5–19 sesi selepas earnings. Konsisten 5/5 bagi isyarat KOHORT F: QQQ OFF, SPY bawah SMA200, earnings 1–5 sesi akan datang, SUE > 0, hasil tumbuh ≥ 20 %. Jadual penuh dan kaveat: `hasil/PRASYARAT/LAPORAN.md`.
- **Kajian pakar:** semua menilai pasaran dahulu; dua aliran (ikut trend lawan pantulan) yang masing-masing memadankan jenis setup dengan keadaan pasaran. Data kita menyokong aliran pantulan untuk kadar lari dan tidak menyokong dakwaan industri kuat. Butiran, sumber dan senarai yang belum diukur: `kajian/KAJIAN_PRASYARAT_PAKAR.md`.

## 7. Keadaan repo

- Kerja 13–14 Nov hingga CS05 di `main` (PR #45–#48; #48 = CS05, pindaan (i), (j), (k) dan baris `lejar.yml`). Kerja CS06 (`cs_tala6.py`, `hasil/CS06/`, `F58`–`F87`, fail ini) berada di branch `claude/dreamy-lovelace-38z7wm`; ia sampai ke `main` hanya selepas pengguna meminta PR. Jika fail ini dibaca di `main`, gabungan itu sudah berlaku.
- `jejak_f.yml` berjalan selepas workflow "Lejar penuh" berjaya (06:17 dan 10:17 UTC, Sel–Sab). Stor harga yang dibaca penjejak dikemas kini oleh Lejar, BUKAN `harga_harian.yml`. Disemak 14 Nov 03:10 UTC: `jejak_f.yml` TERBUKTI tercetus melalui `workflow_run` selepas Lejar berjadual 13 Nov 17:45 UTC (larian #2, berjaya); `jejak_f/lejar.csv` masih kosong hanya kerana Lejar bagi sesi 2026-11-13 belum berjalan pada waktu itu (harga hingga 20261112).
- **Perkara untuk disemak oleh chat baharu:** adakah `jejak_f/RINGKASAN.md` menunjukkan harga ≥ 20261113 dan isyarat pertama? Sejak 14 Nov 2026 (PR #48, keputusan pengguna) langkah akhir `lejar.yml` mencetus `jejak_f.yml` terus selepas larian Lejar yang didispatch penjaga, jadi ia tidak lagi menunggu larian berjadual.
- Ujian: `python3 -m unittest discover -s BacktestShariah2/ujian`; `python3 BacktestShariah2/standard/sahkan.py --betulkan` mesti keluar 0.

## 8. Keputusan: sudah dibuat dan yang tinggal

**Sudah diputuskan pengguna (14 Nov 2026) dan SUDAH dilaksanakan:** carian sekali lagi untuk SEMUA kaedah dengan prasyarat + syarat (pusingan **CS05**, §9).

**Diputuskan pengguna 14 Nov 2026 (selepas CS05):** JANGAN mula jejak hadapan bagi setup CS05; backtest mesti lengkap dan menepati matlamat §1 dahulu. Kohort 13 Nov (8 setup) tidak disentuh.

**Diputuskan pengguna 14 Nov 2026 ("ya untuk tiga-tiga") dan SUDAH dilaksanakan:** (1) pusingan **CS06**: pangkat masuk ikut tangkap penuh + tala bersama prasyarat (pindaan (k), §9a); (2) kerja CS05 digabung ke `main` (PR #48); (3) `lejar.yml` mencetus `jejak_f.yml` terus.

**Menunggu keputusan pengguna:**
1. Gabung hasil CS06 ke `main` melalui PR? (Kelulusan PR pengguna setakat ini meliputi CS05.)
2. Arah seterusnya. Tiga pusingan berturut (CS04, CS05 (j), CS06) menunjukkan penalaan dan pemilihan indikator keluar tidak menambah pada saham tidak dilihat; yang belum diukur ialah (a) simulasi portfolio berslot bagi setup berprasyarat (hari isyarat berkelompok; adakah akaun dapat mengambil belian itu?) dan (b) data saham delist. Cadangan Claude: (a) dahulu, bagi `F39`, `F40`, `F58` (berdagang setiap tahun) dan `F49`. Jejak hadapan kekal ditangguh sehingga pengguna membenarkannya.

**Tiada yang berkaitan wang sebenar berubah:** kad skor kekal satu-satunya keputusan.

Tertangguh lebih lama (belum dimulakan): keluarga indikator berparameter penuh; data saham delist; simulasi portfolio berasaskan slot untuk setup kadar tangkap (penting bagi setup berprasyarat: hari isyaratnya berkelompok); carian suku tahunan automatik di GitHub Actions; VIX sebenar bagi `QH07`; kalendar earnings harian (hanya jika jejak hadapan setup berprasyarat dibenarkan kelak).

## 9. CS05: apa yang dibuat dan apa yang didapati (14 Nov 2026)

Pradaftar: pindaan (i) + tambahan (i), kedua-duanya dikomit sebelum larian penuh. Sumber angka: `hasil/CS05/LAPORAN.md` (= `kajian/CARIAN_SETUP.md`), `SEMUA_PENCETUS.md|csv`, `PADANAN.csv`, `meta.json`.

**Reka bentuk.** Peraturan masuk = [0–1 prasyarat PASARAN daripada 33] DAN [0–1 prasyarat KUMPULAN/SYARIKAT daripada 15] DAN pencetus (500) DAN [0–2 penapis SAHAM daripada 27] = 103,088,000 peraturan; 43,784,217 cukup isyarat. Prasyarat = 38 daripada tinjauan (h) (semua, tanpa pemilihan) + 10 takrif pakar `QH01`–`QH10` (follow-through day, distribution day, breadth thrust Zweig, nisbah 4 %, regangan turun-naik, QQQ SMA10 > SMA20, Peringkat 2 Weinstein, hari 90 %). Dua kayu ukur kadar tangkap: **pilih** (lawan saham rawak HARI SAMA; kayu ukur pindaan (d)) dan **jumlah** (lawan saham rawak sepanjang ERA; memasukkan kesan bila membeli). Carian diulang dengan prasyarat **plasebo** (dianjak 437 sesi). Semua angka di bawah daripada kumpulan B.

**Dapatan (semuanya kumpulan B, saham yang tidak dilihat):**

| Soalan | Jawapan | Angka |
|---|---|---|
| Adakah prasyarat menolong setiap kaedah? | Ya, bagi kedua-dua kayu ukur, termasuk K3 | Pilih: median kadar lari 8.4 % (syarat sahaja) → 11.2 % (dengan prasyarat); median beza kelebihan +4.65 mata lawan plasebo +0.62; 430 daripada 463 pencetus bertambah baik; K3 +5.61 lawan +0.51. Jumlah: +4.71 lawan +2.16; K3 +6.06 lawan +0.57 |
| Prasyarat mana? | Satu sahaja yang menaikkan kemahiran memilih: **earnings dalam 1–5 sesi akan datang** | Bila benar: kadar lari pencetus +5.9 mata, kelebihan +5.3 (plasebo +0.7), kena henti +5.0. Kesemua 200 peraturan teratas (pilih) memakainya |
| Pasaran panik (SPY bawah SMA200, QQQ ≥ 10 % di bawah puncak, QQQ RSI14 < 35, keluasan ≤ 30 %, turun-naik ≥ 25 %)? | Menaikkan kadar lari SEMUA saham (masa), bukan pemilihan | Kadar lari pencetus +2 hingga +6 mata; kelebihan lawan hari sama ≈ 0 (−1.3 hingga +0.2); kena henti +3 hingga +10 mata (kecuali QQQ RSI14 < 35: −1 hingga −2) |
| Aliran ikut trend (FTD, Weinstein, breadth thrust, MA10 > MA20, QQQ ON) dan sektor/industri kuat? | Tidak menaikkan kadar tangkap | Perubahan kadar lari kebanyakannya −1.6 hingga +0.6 mata; kelebihan ≈ 0 (−0.3 hingga +0.3) |
| Padanan jenis setup × pasaran (dakwaan pakar)? | Tidak disokong | 434 pencetus IKUT TREND dan 31 PANTULAN bertindak balas hampir sama terhadap setiap prasyarat |
| Berapa banyak daripada pencetus (kaedah M/N/indikator)? | Sedikit, selepas prasyarat + penapis | `F39`: setup penuh 21.2 % lari; buang pencetus 20.1 %; buang prasyarat 9.1 % |

**Peringkat lengkap (pindaan (j)): henti, pegang dan keluar ikut kadar tangkap yang direalisasi.** Semakan lawan §1 (diminta pengguna) mendapati pegang/keluar pindaan (d)/(i) dipilih ikut PURATA setiap dagangan, hanya bagi setup papan, dan beberapa menjual awal (`F48`: pegang 5.4 sesi, 12 % dagangan dijual ≥ +10 %). Kini (henti × keluar) dipilih supaya paling kerap **jadi** (dagangan DIJUAL dengan untung bersih ≥ 10 %), bagi setup papan dan bagi setiap kaedah. **Tangkap penuh** = saham itu lari (corak §1) DAN dijual dengan untung ≥ 10 %.

| Dapatan (kumpulan B) | Angka |
|---|---|
| Setiap kaedah, tangkap penuh: syarat sahaja → dengan prasyarat | median 8.1 % → 10.3 % (lebih tinggi bagi 358 daripada 463 kaedah; K3 278 daripada 347) |
| Setiap kaedah, jadi (lebih luas: termasuk yang naik perlahan) | median 18.4 % (rawak 16.9 %) syarat sahaja lawan 16.1 % (rawak 12.7 %) dengan prasyarat: TIDAK lebih tinggi (204 daripada 463). Peraturan masuk dipilih untuk corak "lari"; setup syarat sahaja memilih saham lebih meruap |
| Cara pegang | median 16–18 sesi; henti `H4` (4×ATR14) paling kerap terpilih (1,244 daripada 1,873 peraturan) |
| Adakah indikator keluar menambah? | Jarang: keluar terpilih mengatasi "tiada keluar indikator" (`X00`) hanya bagi 120–198 daripada ~463 kaedah, dan bezanya kecil; kebanyakan keluar terpilih ialah pasangan DAN yang jarang menyala |
| Rugi ≥ 8 % | median 26–30 % dagangan, dengan atau tanpa prasyarat |
| Keluar lama (ikut purata) lawan baharu, papan pilih | `F39` 20.3 % → 27.3 % jadi; `F44` 18.8 % → 26.3 %; `F48` 12.0 % → 25.8 % |

**Setup lengkap teratas** (kumpulan B; tangkap penuh · jadi (rawak dengan cara pegang sama) · rugi ≥ 8 % · pegang):

- `F49` QQQ ≥ 10 % di bawah puncak + earnings 1–5 sesi + N119 (3 tutup turun) + MACD > isyarat + ATR% ≥ 4; henti `H4`, keluar X12 (RSI14 silang turun bawah 70): 25.3 % · 38.7 % (19.4 %) · 21.0 % · 17.1 sesi; kelebihan jadi K1 / K2 / K3 +30.5 / +17.8 / +19.5; 1,068 belian pada 201 hari.
- `F55` turun-naik SPY ≥ 25 % + sektor 3 terbawah + N75 + ADX < 20 + ≥ 30 % di bawah puncak; `H4`, X10 DAN X21: 21.7 % · 42.4 % (18.7 %) · 12.0 % · 19.3 sesi; +26.7 / +19.4 / +34.0 (484 belian, 115 hari).
- `F50`, `F54`, `F56` (pasaran jatuh): jadi 35–36 % lawan rawak 17–19 %. `F51`: 29.7 % lawan 14.9 %.
- Papan pilih: `F40` rejim ON baharu + earnings 1–5 sesi + M14 + Supertrend naik + ≥ 30 % di bawah puncak; `H3`, X14 DAN X21: 20.9 % · 28.0 % (18.8 %) · 32.0 % · 16.4 sesi; +8.1 / +8.5 / +12.4. `F39` serupa: 20.8 % · 27.3 % (20.3 %).
- Gagal pada K3: semua setup "Januari + tiada earnings 20 sesi" (`F43`, `F52`, `F53`); `F41` (kelebihan jadi K3 −0.4).

**Cara membaca dengan jujur.** (i) Earnings ialah peristiwa dua hala: kadar lari naik, kadar kena henti dan rugi besar turut naik (`F41`: 53 % dagangan rugi ≥ 8 %); label "lari" mengehadkan rugi pada −8 % sedangkan jurang turun selepas earnings boleh lebih besar, jadi baca lajur purata setiap dagangan bersama. (ii) Setup papan jumlah membeli semasa pasaran jatuh: hari isyarat berbeza hanya 15 hingga 332 bagi setiap setup dalam 16 tahun (lajur "hari isyarat"), dan data tiada saham delist (saham yang jatuh lalu dinyahsenarai tiada). (iii) `QF01` memakai tarikh earnings sebenar; papertrade memerlukan kalendar earnings. (iv) Papan ialah pangkat backtest, BUKAN bukti; tiada simulasi portfolio.

**Apa yang masih BELUM dibuat dalam backtest (lawan §1):** (a) penalaan parameter kaedah dengan prasyarat (item 7: "mesin sentiasa mencari dan menala"; CS04 menala syarat sahaja); (b) peraturan masuk dipangkatkan ikut label "lari", bukan terus ikut "tangkap penuh"/"jadi" setup lengkap; (c) simulasi portfolio berslot (hari isyarat berkelompok); (d) data saham delist. Jejak hadapan setup CS05 TIDAK dimulakan (keputusan pengguna, §8); jika kelak dibenarkan ia memerlukan kalendar earnings harian dan prasyarat pasaran dalam penjejak.

## 9a. CS06: pangkat ikut tangkap penuh, dan tala bersama prasyarat (14 Nov 2026)

Pradaftar: pindaan (k), dikomit sebelum dijalankan. Sumber angka: `hasil/CS06/LAPORAN.md` (= `kajian/CARIAN_SETUP.md`), `SEMUA_PENCETUS_LENGKAP.md`, `TALA.md`, `meta.json`, `tala_meta.json`. Semua angka kumpulan B.

**A. Pangkat masuk ikut tangkap penuh.** Sasaran `tp` = tutup sesi 5 ≥ harga beli + 5 % DAN dagangan dijual dengan untung bersih ≥ 10 % dengan pegang piawai (henti 4×ATR14, tiada keluar indikator, 20 sesi). Ruang carian, dua kayu ukur, plasebo dan papan sama seperti CS05.

| Soalan | Jawapan | Angka |
|---|---|---|
| Adakah kesimpulan CS05 berubah? | Tidak | Pilih: median tangkap penuh 9.3 % (syarat sahaja) → 11.1 % (dengan prasyarat); beza kelebihan +4.50 mata lawan plasebo +0.57; 432 daripada 461 kaedah; K3 +5.54 lawan +0.49. Jumlah: +4.83 lawan +2.12; K3 +5.30 lawan +0.40 |
| Adakah pangkat berubah? | Ya, di hujung atas | 115 (pilih) dan 118 (jumlah) daripada 200 teratas CS06 juga dalam 200 teratas CS05; papan: 6 daripada 10 (pilih) dan 2 daripada 10 (jumlah) peraturan masuk sama. Walaupun 95 % bar "lari" juga tangkap penuh, hujung atas ialah beza kecil antara setup yang hampir seri |
| Setup lengkap setiap kaedah (tangkap penuh dengan henti dan keluar sendiri) | Prasyarat menambah sedikit | Median 9.3 % → 10.7 % (pilih; 342 daripada 462 kaedah; K3 268 daripada 341); 11.8 % → 12.2 % (jumlah; 320 daripada 460) |
| Indikator keluar | Masih tidak menambah | Median tangkap penuh dengan keluar terpilih lawan tanpa keluar indikator: 10.7 % lawan 10.9 % (pilih, dengan prasyarat) |

**Papan pilih (berdagang SETIAP tahun; 17 daripada 17 tahun):** `F40` rejim ON baharu + earnings 1–5 sesi + M14 + Supertrend naik + ≥ 30 % di bawah puncak: 21.9 % lawan rawak 10.6 %; setup lengkap (`H3`, keluar RSI14 > 80) 22.9 % lawan 10.7 %, kelebihan K1 / K2 / K3 +12.4 / +11.2 / +14.3; rugi ≥ 8 % 32 %. `F39` serupa (21.2 %). `F58` (baharu) N16 RSI2 < 10 + ≥ 60 % saham di atas MA50 + earnings 1–5 sesi + Supertrend naik + ≥ 30 % di bawah puncak: 19.8 % lawan 7.6 %; setup lengkap 22.1 % lawan 7.4 %, +15.1 / +13.2 / +18.6.

**Papan jumlah (pasaran jatuh; belian tertumpu):** `F62` (baharu) QQQ ≥ 20 % di bawah puncak + M73 + RSI14 < 40 + ≥ 30 % di bawah puncak: 37.1 % lawan 8.4 %, TETAPI 1,314 belian pada 144 hari dalam 5 tahun sahaja; 650 belian pada 10 hari (Dis 2018, Mac 2020) dengan kadar 60 %, manakala 603 belian sepanjang 2022 hanya 15 %. `F49` 29.4 % lawan 9.2 % (setup lengkap 30.1 % lawan 9.0 %; +24.7 / +20.5 / +21.8), 68 % belian dalam 2020 dan 2022. `F64`, `F67`, `F69` (turun-naik SPY ≥ 25 %) 22–27 %. Jadual "taburan belian mengikut tahun" dalam laporan menunjukkan kepekatan setiap setup.

**B. Tala bersama prasyarat.** 20 induk (papan CS06); tiga paksi serentak: 240 varian pencetus (10 induk kaedah M × 24), ambang penapis saham, ambang 36 prasyarat berambang (`cs_lapis.GRID_PRA`; ciri mentah `cs_lapis.Mentah` disahkan menghasilkan lapisan (i) tepat pada ambang asal: 0 bar berbeza). Anak dipilih ikut dataran pada kumpulan A.

- 2 induk kekal; 18 mendapat anak. **Anak mengatasi induk pada kumpulan B: 6 daripada 18; pada K3: 4 daripada 17; kedua-duanya: 3 daripada 18. Bacaan dikunci: tala TIDAK menolong.**
- Ini pusingan ketiga dengan dapatan yang sama arah (CS04: 6/8 pada kumpulan B, 4/8 pada K3; (j): indikator keluar tidak mengatasi pegang sahaja). Menala lebih halus pada data yang sama tidak menambah kadar tangkap pada saham yang tidak dilihat.
- Anak didaftarkan `F70`–`F87` (status BACKTEST) sebagai rekod; ia BUKAN cadangan.

## 10. Apa yang TIDAK disimpan dalam repo, dan cara menjana semula

Folder kerja (panel indikator, isyarat benih, jadual besar; ~3.4 GB pickle) berada di luar repo dan hilang bersama sesi. Semuanya boleh dijana semula secara deterministik (`cs_atom.BENIH = 20261113`); data mentah set 2000 dimuat turun dari Release `autotune-data-a02` (perlukan `pyarrow`: `pip install pyarrow`; ia tiada dalam fail requirements repo).

```bash
cd BacktestShariah2/kajian/carian_setup
K=<folder kerja di luar repo>          # CS_PEKERJA=2 atau 3 jika memori terhad
python3 cs_cari.py panel $K A && python3 cs_cari.py benih $K A      # ~1 jam 10 min (4 pekerja)
python3 cs_cari.py besar $K CS02                                    # ~1 jam; titik semak setiap 25 pencetus
python3 cs_cari.py tepat $K CS02
python3 cs_cari.py panel $K B && python3 cs_cari.py kunci $K CS02   # ~30 min
python3 cs_lapor.py $K CS02 arkib                                   # 'arkib' = jangan tulis ganti kajian/CARIAN_SETUP.md
python3 cs_tangkap.py $K                                            # CS03, ~7 min
python3 cs_tangkap.py $K semua                                      # rekod SEMUA peraturan masuk kumpulan A, ~1 min
python3 cs_tala.py $K                                               # CS04, ~16 min
python3 cs_prasyarat.py $K                                          # tinjauan prasyarat, ~2 min selepas panel/benih ada
python3 cs_ringkas.py                                               # TOP50 + PEMBAHAGIAN_F (tiada folder kerja)
python3 cs_hadapan.py jejak                                         # penjejak hadapan (stor harga repo)
# CS05 (pindaan (i)): perlukan panel A dan B + benih A dan B bagi SEMUA modul
CS_PEKERJA=3 python3 cs_cari.py benih $K B                          # ~50 min; 4 pekerja mencecah had memori 15 GB
python3 cs_lapis.py $K                                              # lapisan prasyarat A dan B (+ plasebo), ~1 min
python3 cs_cs05.py besar $K && python3 cs_cs05.py plasebo $K        # ~6 min setiap satu (4 pekerja)
python3 cs_cs05.py tepat $K && python3 cs_cs05.py kunci $K          # ~3 min + ~2 min
python3 cs_lengkap.py asas $K && python3 cs_lengkap.py pilih $K     # pindaan (j): ~3 min + ~4 min
python3 cs_cs05.py lapor $K                                         # hasil/CS05/, kajian/CARIAN_SETUP.md, registry F
# CS06 (pindaan (k)): enjin yang sama dengan CS_PUS=CS06 (fail kerja berawalan cs06_; sasaran tangkap penuh)
export CS_PUS=CS06
python3 cs_cs05.py besar $K && python3 cs_cs05.py plasebo $K && python3 cs_cs05.py tepat $K && python3 cs_cs05.py kunci $K
python3 cs_lengkap.py asas $K && python3 cs_lengkap.py pilih $K     # asas dibina semula (kini termasuk tangkap penuh)
python3 cs_tala6.py benih $K && python3 cs_tala6.py tala $K         # 240 varian (~25 min) + tala (~2 min)
python3 cs_cs05.py lapor $K && python3 cs_tala6.py lapor $K         # hasil/CS06/, kajian/CARIAN_SETUP.md, registry F
unset CS_PUS
```

Susunan `lapor`: CS05 dahulu, kemudian CS06 (yang terakhir menulis `kajian/CARIAN_SETUP.md`), kemudian `cs_tala6.py lapor`, kemudian `cs_ringkas.py`.

`CS05_KELUAR=<folder> python3 cs_cs05.py lapor $K` menulis semua keluaran CS05 ke folder lain (uji kering: tiada tulisan ke repo).

CS01 sama dengan set `431` dan `kunci` (pusingan `CS01`). **Awas:** `cs_lapor.py` (walaupun dengan `arkib`), `cs_tangkap.py` dan `cs_tala.py` menulis `data/registry_F.csv`; tanpa `arkib`, `cs_lapor.py` juga menulis ganti `kajian/CARIAN_SETUP.md`, begitu juga `cs_tangkap.py` dan `cs_tala.py`; jangan jalankan semula pusingan lama kecuali untuk mengesahkan, dan semak `git diff` selepasnya.

Disimpan sebagai rekod: `hasil/CS03/semua_masuk.csv.gz` (SEMUA 182,903 peraturan masuk yang diskor pada kumpulan A: bilangan, kadar lari / capai +10 % / kena henti dan asas rawak setiap era, skor) dan `hasil/CS03/SEMUA_PENCETUS.csv|md` (satu baris setiap kaedah); `hasil/CS01|CS02/tepat_semua.csv` (~1,960–1,990 setup dengan skor tepat), `senarai_kunci.csv` (200 teratas + 200 rawak pada Kunci), `papan.csv`, `meta.json`, `besar_meta.json` (taburan skor), dan log larian (`*.log`, masa UTC).

## 11. Perangkap teknikal yang sudah ditemui

- Jangan namakan modul `teras.py` dalam folder kajian: ia menindih pakej `REVERSE/teras` dan mematahkan `ujian/test_reverse_*`. Sebab itu awalan `cs_`.
- Modul benih N (bingkai indikator besar) dengan 4 pekerja pada 1,000+ saham kehabisan memori; `multiprocessing.Pool` tergantung selepas pekerja terbunuh. Penyelesaian sedia ada: 100 saham setiap kelompok, `ProcessPoolExecutor`, titik semak setiap 20 modul, `CS_PEKERJA`.
- Kerja latar sesi Claude dihadkan 2 jam dan kontena boleh dimulakan semula: semua langkah panjang ada titik semak; sambung dengan arahan yang sama.
- Lajur `param` dalam `registry_F.csv` ialah JSON bertanda koma; baca dengan `pandas`/`csv`, bukan `cut -d,`.
- Kembar formula yang diketahui: `N201` ≈ `P07` sahaja.
- Ujian statistik setiap kaedah: jangan guna SE berkelompok ikut hari beli (lulus plasebo sehingga 45 %); ikut reka bentuk `standard/lift_kaedah.py`.
- (CS05) Modul benih N dengan 4 pekerja mencecah 13 GB daripada 15 GB; guna `CS_PEKERJA=3` untuk kumpulan B. Jam kontena sesi berjalan normal: binaan penuh (panel + benih A + benih B + CS05) mengambil kira-kira 1 jam 45 minit.
- (CS05) Had kepelbagaian papan memerlukan kolam calon yang lebih luas daripada 2,000 teratas sejagat (hampir semuanya berkongsi satu prasyarat); lihat tambahan pindaan (i).
