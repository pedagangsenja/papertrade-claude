# STRATEGI — satu rancangan, satu baris gilir, peraturan keputusan dipra-komit

**Status keadaan semasa dijana oleh `python3 REVERSE/strategi.py`, bukan daripada ingatan.**
Dokumen ini menetapkan matlamat, syarat berhenti dan pokok keputusan. Skrip membaca CSV
keputusan sebenar dan memberitahu kita berada di cabang mana. Ujian unit
`ujian/test_strategi.py` gagal jika registry menyatakan sesuatu belum diuji sedangkan fail
keputusan sudah mengandunginya — itu tepat pepijat yang membuat `GB08` dan `GB04` disenarai
sebagai "calon" selepas kedua-duanya diuji dan gagal.

## 1. Mengapa kajian ini tidak pernah tamat

Empat sebab struktur, bukan kecuaian:

1. **Tiada takrif siap.** `SASARAN.md` mengukur +10%/bulan = 3.14×/tahun = 8,994,377× atas
   14 tahun, dan SPY sendiri memberi 0% bulan ≥ +10% dalam 13 daripada 14 tahun. Sasaran itu
   **tertutup**. Tetapi tiada sasaran gantian pernah ditulis, jadi setiap keputusan membaca
   "gagal" dan carian tidak boleh berhenti.
2. **Tiada baris gilir.** Eksperimen dipilih reaktif setiap perbualan.
3. **Sumber kebenaran hanyut** daripada keputusan sebenar.
4. **Tiada peraturan keputusan dipra-komit** — setiap keputusan dibincang semula dari kosong.

## 2. Matlamat — bertingkat, boleh diukur, dan satu daripadanya mesti dipilih

Penanda aras ialah **SPUS** (patuh Syariah; `PENANDA_ARAS_SYARIAH.md`), bukan SPY.
Dua konvensyen, **jangan dicampur**: CAGR seluruh tingkap **17.95% / MDD −26.82% /
nisbah 0.669**, atau median setiap tahun **26.09% / MDD −10.14%**. Semua gate di bawah
memakai konvensyen pertama.

| Tingkat | Takrif | Status |
|---|---|---|
| **T0** | +10%/bulan | **TERTUTUP** secara aritmetik. Tidak akan dibuka semula. |
| **T1** | CAGR > 17.95% **DAN** MDD ≥ −26.82% | belum dicapai oleh apa-apa (0 / 413 + 36) |
| **T2** | nisbah `CAGR ÷ \|MDD\|` > 0.669 **DAN** CAGR > 17.95% | belum dicapai |
| **T3** | CAGR ≈ SPUS (≥ 15%) dengan MDD **jauh lebih cetek** (≥ −15%) | belum diuji sebagai sasaran |
| **T4** | Terima SPUS + tunai pada berat pilihan pengguna | **tersedia sekarang, tiada kajian diperlukan** |

T4 bukan kekalahan: `SISTEM.md` mengukur nisbah campuran SPUS+tunai hampir **pemalar
0.642–0.669** merentas setiap berat, jadi berat ialah soalan **toleransi drawdown**, bukan
soalan data. 100% → +17.95%/−26.82%; 60% → +10.87%/−16.62%; 40% → +7.27%/−11.25%.

## 3. Syarat berhenti — dipra-komit, tidak boleh dilonggarkan selepas melihat keputusan

**BERHENTI–MENANG:** mana-mana eksperimen dalam baris gilir §4 melepasi **T1 atau T2**
dengan kawalan rawak dan jalur benih, pada tingkap tahan. Tindakan: bekukan konfigurasi,
tulis spec hadapan, jalankan sebagai lorong `portfolio_slot/` selama ≥ 126 sesi sebelum
sebarang dakwaan.

**BERHENTI–TUTUP:** jika **E1 hingga E6 selesai dan tiada satu pun melepasi T1 atau T2**,
kajian signal/pembinaan **ditutup**. Tindakan: terima **T4**, pengguna pilih berat, dan
sumber dialih sepenuhnya kepada pelaksanaan (kecacatan henti hari-0, kualiti data, jejak
hadapan). **Tiada eksperimen ke-7 ditambah selepas melihat keputusan E1–E6.**

**BERHENTI–SEPARA:** jika sesuatu melepasi **T3** sahaja, ia dilaporkan sebagai lorong
risiko-rendah dan diuji ke hadapan, tetapi **tidak** didakwa mengalahkan SPUS.

Syarat tambahan yang mengikat semua: apa-apa dapatan pada alam `AL01` kekal **bersyarat**
sehingga `E2` menjalankannya pada alam dagangan sebenar.

## 4. Baris gilir — enam eksperimen, berurutan, dengan cabang ditulis dahulu

Urutan dipilih mengikut **nilai jangkaan ÷ kos**, bukan minat. Setiap item menyatakan bukti
repo yang menyebabkan ia wujud, supaya tiada eksperimen "sebab terfikir".

### E1 · PEGANG × SLOT · *sedang berjalan*
Pradaftar `SPEC_PEGANG_SLOT.md`, skrip `step24_pegang_slot.py` (komit `3370a4f`).
**Bukti:** jangkaan/dagangan dan pusingan/tahun bergerak bertentangan dan hanya dua hujung
pernah diukur (`X29` 10 bar +0.294%; `X13` ~85 bar +4.350%); lengkung slot menaik monoton
pada kedua-dua paksi dalam DUA kajian bebas dan tidak pernah dijalankan ke hadnya.
- **JIKA T1/T2 lulus** → BERHENTI–MENANG.
- **JIKA had pegangan menang tetapi masih bawah T1** → bawa had terbaik ke E2–E4 sebagai
  tetapan tetap; jangan ulang paksi ini.
- **JIKA slot tinggi menang hanya kerana isyarat tidak lagi menyumbang** (gate `P3` gagal di
  sana) → itu **struktur indeks**, bukan isyarat; lompat terus ke E3 dan catat dalam §6.
- **JIKA kedua-duanya gagal** → E2.

### E2 · ALAM `AL02` — alam dagangan sebenar
**Bukti:** setiap satu daripada 449 ujian berjalan pada `A01`/A02 yang (a) **tiada saham
delist** = bias survivorship ke atas, dan (b) **bukan** alam yang repo tapis untuk belian.
Ini bukan mencari alfa; ia menentukan sama ada nombor sedia ada bermakna.
**Kos:** rendah (tapis panel sedia ada).
**Had yang mesti ditulis dalam spec:** `data/skrin/etf_shariah.csv` ialah 326 konstituen
**semasa sahaja, tiada tarikh**, jadi ujian ini membawa bias keahlian-ke-belakang. Ia
dijalankan sebagai **semakan kesahan dua arah**, bukan sebagai dakwaan prestasi.
- **JIKA kelebihan mati pada `AL02`** → BERHENTI–TUTUP dipercepat; E3–E6 dibatalkan kerana
  ia semua akan diuji pada alam yang salah.
- **JIKA bertahan** → E3.

### E3 · INSTRUMEN `IS02` — putaran ETF sektor
**Bukti:** prior positif paling kuat dalam seluruh registry. `SETUP.md` mengukur SPY
**+3.356%** dan QQQ **+4.419%** melepasi syarat ekor yang **598 daripada 598** setup saham
gagal, kerana indeks **itulah** kepelbagaian merentas ekor. ETF sektor ialah titik tengah
antara satu saham dan satu indeks, dan ia tidak pernah diuji.
**Kos:** sederhana — repo **tiada** data ETF sektor (A02 = 3,260 saham; `idx.parquet` hanya
SPY + QQQ). Perlu muat turun ~11 ticker SPDR, 2009–2026, ke dalam stor yang sama.
- **JIKA T1/T2 lulus** → BERHENTI–MENANG.
- **JIKA hanya T3** → BERHENTI–SEPARA, dan E4–E6 dijalankan hanya jika pengguna mahu.
- **JIKA gagal** → E4.

### E4 · KELUAR `X31`/`X32` — keluar peringkat PORTFOLIO
**Bukti:** pilihan keluar diukur **12× lebih berpengaruh** daripada masuk (sebaran 4.997
mata lawan lift terbaik 0.392), tetapi **kesemua 23** keluar yang diuji ialah peraturan
setiap posisi. `X31` (gugur daripada 3 teratas pangkat 252 hari) dan `X32` (imbang berkala
sahaja) ialah keluar peringkat portfolio dan menyerang kesesakan yang `PORTFOLIO_N.md`
diagnosis: pusing ganti ~3 kali/slot/tahun.
**Kos:** sederhana — perlu gelung pangkat + imbang dalam enjin `step22`.
- Cabang sama seperti E3.

### E5 · KORELASI `KR03` — had bilangan setiap industri
**Bukti:** tidak pernah diukur. 8–10 slot yang semuanya satu industri = berkesan 2–3 slot.
`PORTFOLIO_N.md` mendapati MDD dikawal oleh **urutan**, bukan bilangan slot — had industri
ialah lever kedua pada paksi yang sama.
**Kos:** rendah jika peta ticker→industri wujud; perlu disemak dahulu.
- Cabang sama seperti E3.

### E6 · GABUNGAN `GB07` — hierarki merentas paksi
**Bukti:** satu-satunya operator gabungan yang belum diuji yang menggunakan signal pada
**paksi berlainan** (signal A menentukan ALAM, signal B menentukan URUTAN). `GB01` `DAN`,
`GB02` `ATAU`, `GB03` undi, `GB04` agregat pangkat dan `GB08` penapis terbalik **semuanya
sudah diuji**; empat gagal, satu (`GB02`) lulus gate setiap-dagangan tetapi gagal portfolio.
**Kos:** rendah.
- **JIKA gagal** → **BERHENTI–TUTUP.**

## 5. Apa yang TIDAK akan diuji lagi, dan mengapa

Ditulis supaya ia tidak boleh dicadangkan semula tanpa bukti baharu:

- **Peraturan MASUK baharu** — 280 ujian, gate3 **0**. Ruang ditutup.
- **Penapis gaya setup** — 598 setup, lift positif **0**. Gagal kerana **struktur**: menapis
  membuang bar, dan taburan dipandu ekor kanan.
- **Fundamental / SEC / silang-keluarga** — ditutup oleh `KEPUTUSAN_FASA2_SEC.md` dan
  `SILANG_GATE_C.md`.
- **Sasaran untung tetap** — diukur merugikan **lima kali** (`X10` menang 94.1% dengan
  jangkaan −0.023%; `C06` menang 32.9% dengan −0.591%).
- **Penalaan parameter / Optuna** — di luar skop kajian sejak hari pertama.
- **`C07`/`C09`/`C11`** — satu keluarga dengan `C02` yang kalah pada **kedua-dua** paksi.
- **`U06`/`U07`/`U12`** (WorldQuant 101, OpenAP 212, GTJA 191) — tersekat rangkaian:
  `arxiv.org` dan `huggingface.co` disekat DNS/proksi, dan pakej PyPI `alpha101` memberi
  **404** sedangkan `pandas` dan `qlib` memberi 200, jadi ia bukan sekatan proksi — pakej
  itu tiada. Dibuka semula hanya jika sumber sah muncul.
- **PG/IB baki** — dijawab oleh E1; jangan ulang sebagai paksi berasingan.

## 6. Log cabang

Setiap eksperimen menambah satu baris di sini apabila selesai: keputusan, cabang yang
diambil, dan sebabnya. Ini rekod *mengapa* kita berada di langkah semasa.

| # | Eksperimen | Keputusan | Cabang diambil |
|---|---|---|---|
| — | A masuk (280) | 0 lulus gate3 | ruang masuk ditutup |
| — | B keluar (69) | 0 lulus gate3 | keluar setiap-posisi ditutup |
| — | GABUNGAN (14) | 2 lulus gate3 (`GB02` kesatuan) | bawa ke portfolio |
| — | Silang akhir (8) | 8 lulus gate setiap-dagangan | bawa ke portfolio |
| — | PORTFOLIO (36) | **0 lulus P1–P4** | diagnosis: pegang 84.9 bar + ekor |
| — | CARA (6) | 0 lulus; `C01` terbaik | paksi cara ditutup |
| E1 | PEGANG × SLOT | *sedang berjalan* | — |

## 7. Peraturan proses — supaya kesilapan yang sama tidak berulang

1. **Spec DAN kod dikomit sebelum keputusan dilihat.** Sudah diikut; kekalkan.
2. **Ujian asap mesti meliputi KOMBINASI penuh, bukan komponen.** Lima pepijat terlepas pada
   30 Okt 2026 kerana komponen diuji berasingan.
3. **Setiap larian baharu mesti membawa kawalan regresi** terhadap larian sebelumnya pada
   konfigurasi bertindih (contoh: `step24` had=tiada memberi ekuiti identik `step22`).
4. **Pradaftar mesti mengandungi syarat `jangkaan mutlak > 0`** — lift positif atas asas
   negatif masih merugikan (`N16`×`X1`).
5. **Jangkaan priori ditulis sebelum larian.** Rekod saya: salah pada 2 daripada 3 gate dalam
   tiga pradaftar berturut-turut. Menulisnya menjadikan kesilapan itu boleh dikira.
6. **`strategi.py` dijalankan pada permulaan setiap sesi kajian** sebelum apa-apa dicadangkan.
   Ia, bukan ingatan atau `CLAUDE.md`, yang menyatakan apa yang sudah diuji.
