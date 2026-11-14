# Serahan: Carian Setup (CS) dan keluarga F — keadaan pada 14 Nov 2026

Ditulis pada akhir sesi kerja 13–14 Nov 2026 supaya chat baharu boleh menyambung tanpa membaca chat lama. Fail ini ialah nota serahan (ditulis tangan, bertarikh); nombor di sini dipetik daripada fail hasil yang dinamakan, dan fail hasil itulah sumber kebenaran.

**Baca mengikut susunan ini:** fail ini → `kajian/SPEC_CARIAN_SETUP.md` (pradaftar + pindaan (a)–(h)) → `kajian/CARIAN_SETUP.md` (papan semasa) → `kajian/KAJIAN_PRASYARAT_PAKAR.md` → `jejak_f/RINGKASAN.md`.

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

Semua laluan `hasil/…` di bawah `BacktestShariah2/kajian/carian_setup/`. PR #45 dan #46 sudah digabung ke `main`; kerja 14 Nov digabung melalui PR berikutnya (lihat §7).

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

- Kerja 13 Nov di `main` (PR #45, #46). Kerja 14 Nov (pindaan (h), tinjauan, kajian pakar, fail serahan ini) digabung ke `main` melalui PR daripada branch `claude/magical-lovelace-jzz46o`; jika fail ini dibaca di `main`, gabungan itu sudah berlaku.
- `jejak_f.yml` berjalan selepas workflow "Lejar penuh" berjaya (06:17 dan 10:17 UTC, Sel–Sab). Stor harga yang dibaca penjejak dikemas kini oleh Lejar, BUKAN `harga_harian.yml`. Setakat 14 Nov 02:40 UTC `jejak_f/lejar.csv` masih kosong (harga hingga 20261112); isyarat pertama dijangka selepas Lejar 14 Nov.
- **Perkara untuk disemak oleh chat baharu:** adakah `jejak_f.yml` berjalan selepas Lejar 14 Nov dan `jejak_f/RINGKASAN.md` menunjukkan harga ≥ 20261113? `workflow_run` TIDAK tercetus jika Lejar didispatch oleh penjaga dengan `GITHUB_TOKEN`; jika itu berlaku, dispatch `jejak_f.yml` secara manual dan cadangkan langkah cetus terus dalam `lejar.yml` (seperti `analisis.yml`). Jangan ubah `lejar.yml` tanpa keputusan pengguna.
- Ujian: `python3 -m unittest discover -s BacktestShariah2/ujian`; `python3 BacktestShariah2/standard/sahkan.py --betulkan` mesti keluar 0.

## 8. Keputusan: sudah dibuat dan yang tinggal

**Sudah diputuskan pengguna (14 Nov 2026):** jalankan carian sekali lagi untuk SEMUA kaedah dengan prasyarat + syarat (pusingan **CS05**), di chat baharu. Butiran teknikal diserahkan kepada Claude, sentiasa berbalik kepada matlamat §1.

**Tinggal untuk Claude putuskan dalam pindaan (i) (bukan soalan kepada pengguna):** senarai dan ambang prasyarat, bilangan prasyarat setiap peraturan, peraturan lulus, dan sama ada lajur prasyarat/syarat dimasukkan terus ke `data/registry_F.csv` dan `jejak_f/RINGKASAN.md` (cadangan: ya, bersama CS05).

**Hanya ini yang perlu keputusan pengguna kemudian:** menukar kohort jejak hadapan (papertrade) selepas CS05, dan apa-apa berkaitan wang sebenar.

Tertangguh lebih lama (belum dimulakan): keluarga indikator berparameter penuh; data saham delist; simulasi portfolio berasaskan slot untuk setup kadar tangkap; carian suku tahunan automatik di GitHub Actions.

## 9. Reka bentuk CS05 yang dicadangkan (prasyarat × syarat, semua kaedah)

Cadangan, BELUM dipradaftar. Tulis pindaan (i) dalam `SPEC_CARIAN_SETUP.md` dan komit SEBELUM menjalankan apa-apa.

1. **Ruang carian.** Peraturan masuk = **prasyarat** (tiada, atau satu daripada senarai) × **pencetus** (kesemua 500: setiap benih M asal + 2 varian, setiap benih N, setiap indikator) × **penapis saham** (0–2 daripada 27 penapis peringkat saham; tiga penapis pasaran lama `F26`–`F28` berpindah ke lapisan prasyarat). Dengan ~45 prasyarat: kira-kira 46 × 500 × 379 ≈ 8.7 juta peraturan masuk. Pangkat ikut kadar tangkap seperti CS03 (laju: CS03 menskor 233,000 peraturan dalam ~40 saat).
2. **Senarai prasyarat.** 38 daripada tinjauan (h) (`cs_prasyarat.PRASYARAT`; buang pasangan pelengkap yang serupa) + takrif pakar yang belum diukur (`KAJIAN_PRASYARAT_PAKAR.md` §5a: follow-through day, kiraan distribution day, breadth thrust, nisbah 4 %, regangan turun-naik, peringkat Weinstein, hari 90 %). Ambang dikunci dalam pindaan.
3. **Cari dan sahkan.** Cari pada kumpulan A (E1 2010–2019, E2 2020–2024); sahkan 200 teratas + 200 rawak pada kumpulan B (K1, K2, K3 = 2025–Ogo 2026). Isyarat benih kumpulan B perlu dibina untuk semua pencetus yang terpilih (~1 jam).
4. **Banding wajib dalam laporan.** (a) Bagi SETIAP pencetus: skor syarat sahaja (`hasil/CS03/SEMUA_PENCETUS.csv`) lawan skor terbaik dengan prasyarat, supaya nampak kaedah mana yang ditolong prasyarat. (b) Padanan jenis setup (pecah keluar/momentum lawan pantulan/undur, dikelaskan sebelum hasil dilihat) × prasyarat. (c) Plasebo: prasyarat peringkat hari mempunyai sedikit pemerhatian bebas, jadi bandingkan dengan siri prasyarat yang sama dianjak masa (atau prasyarat rawak dengan % masa benar yang sama); lebih banyak gabungan dicuba = lebih banyak nasib. (d) Kadar kena henti di sebelah kadar lari.
5. **Selepas itu.** Pilih henti × keluar untuk papan (seperti CS03), daftar `Fxx` baharu dengan lajur prasyarat dan syarat berasingan, kemudian cadangkan kemas kini kohort jejak hadapan dengan pindaan bertarikh.

Kaveat untuk dibawa: "earnings akan datang" memakai tarikh sebenar (pandang ke hadapan ringan; dalam papertrade perlukan kalendar earnings); peta sektor/industri ialah peta semasa; tiada saham delist; set 2000 bukan tapisan Shariah; papan ialah pangkat backtest, BUKAN bukti.

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
```

CS01 sama dengan set `431` dan `kunci` (pusingan `CS01`). **Awas:** `cs_lapor.py` (walaupun dengan `arkib`), `cs_tangkap.py` dan `cs_tala.py` menulis `data/registry_F.csv`; tanpa `arkib`, `cs_lapor.py` juga menulis ganti `kajian/CARIAN_SETUP.md`, begitu juga `cs_tangkap.py` dan `cs_tala.py`; jangan jalankan semula pusingan lama kecuali untuk mengesahkan, dan semak `git diff` selepasnya.

Disimpan sebagai rekod: `hasil/CS03/semua_masuk.csv.gz` (SEMUA 182,903 peraturan masuk yang diskor pada kumpulan A: bilangan, kadar lari / capai +10 % / kena henti dan asas rawak setiap era, skor) dan `hasil/CS03/SEMUA_PENCETUS.csv|md` (satu baris setiap kaedah); `hasil/CS01|CS02/tepat_semua.csv` (~1,960–1,990 setup dengan skor tepat), `senarai_kunci.csv` (200 teratas + 200 rawak pada Kunci), `papan.csv`, `meta.json`, `besar_meta.json` (taburan skor), dan log larian (`*.log`, masa UTC).

## 11. Perangkap teknikal yang sudah ditemui

- Jangan namakan modul `teras.py` dalam folder kajian: ia menindih pakej `REVERSE/teras` dan mematahkan `ujian/test_reverse_*`. Sebab itu awalan `cs_`.
- Modul benih N (bingkai indikator besar) dengan 4 pekerja pada 1,000+ saham kehabisan memori; `multiprocessing.Pool` tergantung selepas pekerja terbunuh. Penyelesaian sedia ada: 100 saham setiap kelompok, `ProcessPoolExecutor`, titik semak setiap 20 modul, `CS_PEKERJA`.
- Kerja latar sesi Claude dihadkan 2 jam dan kontena boleh dimulakan semula: semua langkah panjang ada titik semak; sambung dengan arahan yang sama.
- Lajur `param` dalam `registry_F.csv` ialah JSON bertanda koma; baca dengan `pandas`/`csv`, bukan `cut -d,`.
- Kembar formula yang diketahui: `N201` ≈ `P07` sahaja.
- Ujian statistik setiap kaedah: jangan guna SE berkelompok ikut hari beli (lulus plasebo sehingga 45 %); ikut reka bentuk `standard/lift_kaedah.py`.
