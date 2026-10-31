# Pradaftar E2 — ALAM `AL02`: adakah kelebihan wujud pada alam yang repo benar-benar dagang?

Ditulis dan dikomit **sebelum** sebarang keputusan dilihat. Skrip: `REVERSE/step25_alam.py`
(dikomit dalam komit yang sama). Keluaran: `REVERSE/ALAM.md`, `REVERSE/alam.csv`,
`REVERSE/alam_ringkas.csv`. Baris gilir: `REVERSE/STRATEGI.md` §4 E2.

## 1. Soalan

Kesemua **449 ujian** dalam kajian ini berjalan pada alam `AL01` = Release
`autotune-data-a02`, 3,260 ticker. Alam itu mempunyai dua masalah yang saling bebas:

1. **Tiada saham delist** → bias survivorship yang mencondongkan setiap CAGR ke atas.
2. **Ia bukan alam yang repo dagang.** Repo menapis belian melalui **SPUS**
   (`data/skrin/etf_shariah.csv`). Alam kajian dan alam dagangan **bukan sama**.

E2 tidak mencari alfa baharu. Ia menentukan sama ada nombor yang sudah ada bermakna pada
alam yang akan digunakan untuk membeli.

## 2. Dua fakta data yang diukur sebelum grid ditetapkan

**(a) Fail konstituen mengandungi DUA ETF, dan hanya satu daripadanya berkaitan.**
`etf_shariah.csv` ada 326 baris: **218 SPUS** dan **108 SPTE** (SP Funds S&P Global
Technology — ETF **global**, mengandungi `2308 TT`, `4062 JP`, `ASML NA`). Menggunakan
kesemua 326 sebagai "alam SPUS" adalah salah. E2 memakai **SPUS sahaja**.

Daripada 218 baris SPUS, tiga bukan ticker (`003654100CVR`, `2602335D`, `CASH&OTHER`) →
**215 ticker**, dan **214** wujud dalam panel A02 (`FDXF` tiada). Liputan bar: 190/214 pada
2012, 206/214 pada 2020.

**(b) Ketumpatan isyarat jatuh 14×.** `GB02_atau3` mencetus **105.2 isyarat/sesi** pada A02
tetapi **7.7/sesi** pada SPUS; ticker unik berisyarat 3,180 lawan **212**. Maka slot di atas
~160 melepasi kapasiti alam SPUS, dan grid slot mesti berhenti di sana.

**(c) Kapasiti `AL02` diukur sebelum grid ditetapkan** (slot 100,000 = tidak mengikat,
`U08`): **108** posisi serentak tanpa had pegangan, **67** dengan had 42 bar. Maka pada
slot **160** kekangan slot **tidak mengikat langsung** pada mana-mana lorong — itulah
`SZ10` (berat sama rata kolam penuh) diukur terus pada alam SPUS. Lajur `buka_purata`
melaporkan ikatan sebenar setiap sel.

## 3. Grid

`AL02` sahaja dijalankan. Nombor `AL01` **tidak dijana semula** — ia diambil terus daripada
`pegang_slot_ringkas.csv` (E1, komit `4f78aba`), yang sudah mengandungi setiap sel yang sama.
Itu menjamin perbandingan memakai angka `AL01` yang **identik** dengan yang sudah dikomit,
bukan larian baharu yang boleh berbeza.

- **MASUK** (2): `GB02_atau3`, `RAWAK` (kawalan)
- **SLOT** (5): 8, 20, 40, 80, 160
- **KELUAR** (2): `X13`, `X15`
- **PEGANG** (4): tiada had, 63, 42, 21 — had 10 digugurkan; E1 mengukurnya kalah pada
  setiap gate dan E2 mengesahkan kesahan, bukan mencari semula
- **URUTAN** (2): `U01` rawak berbenih (20 benih), `U08` ATR% menaik

2 × 5 × 2 × 4 × 2 = **160 konfigurasi**; `U01` 20 benih → **1,680 larian**.

Segala yang lain dikunci sama seperti E1: cara `C01`, saiz `SZ01`, imbang `IB01`, korelasi
`KR01`, instrumen `IS01`, sauh HARIAN, kos penuh dua sisi, tiada margin, satu posisi setiap
ticker, had imbasan keluar 504 bar. Tingkap keputusan 2020–2025; latih 2012–2019 direkod.

Enjin: `step25` **mengimport** `step24.keluar` dan `step24.simulasi` terus. Tiada enjin
kedua; alam dikenakan dengan memotong peta calon kepada indeks ticker SPUS sahaja.

## 4. Arah bias — asimetri yang menentukan apa yang boleh disimpulkan

`etf_shariah.csv` ialah petikan keahlian **semasa, tiada tarikh**. Memakainya ke belakang
sampai 2012 bermakna setiap ticker ialah syarikat yang **kekal** dalam indeks sehingga hari
ini. Itu bias **memihak kepada sistem**, bukan menentangnya.

Maka E2 boleh menghasilkan kesimpulan **negatif yang kuat** tetapi **tidak pernah**
kesimpulan positif yang kuat:

- Jika kelebihan **mati** walaupun dengan bias yang memihak → kesimpulan kukuh.
- Jika kelebihan **bertahan** → lemah, kerana bias membantunya. Ia membenarkan baris gilir
  diteruskan; ia bukan bukti.

## 5. Keputusan — ditetapkan sekarang

- **E2 KEKAL → teruskan ke E3** jika KEDUA-DUA:
  (a) `GB02_atau3` mengalahkan persentil-95 kawalan `RAWAK` yang sepadan dalam **≥ 25%**
  sel `AL02` (`AL01` memberi 101/320 = 31.6%), **dan**
  (b) kesan had pegangan mengekalkan tandanya: had 42 atau 63 mengalahkan `tiada` dalam
  **≥ 50%** sel `AL02` (`AL01` memberi 72/128 = 56%).
- **E2 MATI → BERHENTI–TUTUP dipercepat, E3–E6 dibatalkan** jika (a) gagal. Kelebihan
  isyarat tidak wujud pada alam yang kita dagang, jadi menguji E3–E6 pada `AL01` adalah
  menguji pada alam yang salah.
- **T1 atau T3 tercapai → BERHENTI–MENANG**, dengan satu syarat di §6.

## 6. Perangkap yang mesti diisytihar SEKARANG: T3 melalui beta bukan T3 melalui isyarat

SPUS berat pada teknologi permodalan besar, dan 2020–2025 ialah tempoh yang sangat baik
untuk kumpulan itu. Jadi `AL02` boleh mencapai **T3** (CAGR ≥ 15% dengan MDD ≥ −15%)
semata-mata kerana ia **memegang saham seperti SPUS**, bukan kerana isyarat memilih dengan
baik.

Maka: **jika T1/T3 tercapai pada `AL02` TETAPI gate (a) gagal** (isyarat tidak mengalahkan
kawalan rawak), itu **bukan** dapatan isyarat. Ia `T4` dalam samaran — memiliki alam itu,
bukan memilih daripadanya — dan ia mesti dilaporkan begitu, bukan sebagai BERHENTI–MENANG.
Ini ditulis sebelum larian supaya ia tidak boleh dirasionalkan selepas melihat keputusan.
Ia juga cabang `E1` yang sama (`STRATEGI.md` §4: "struktur indeks, bukan isyarat").

## 7. Diagnostik yang direkod (bukan gate)

- **Bahagian ekor** `AL01` lawan `AL02`, dikira pada **setiap isyarat** dalam tingkap
  keputusan melalui enjin keluar yang sama (`GB02_atau3` × `X13` × had 42): purata,
  **5% teratas sebagai % jumlah pulangan**, dan **purata tanpa 5% teratas** (`tanpa5`).
  `KOLAM_EKOR.md` mengukur 63.7% pada A02. Jika SPUS jauh lebih rendah, itu **mekanisme**
  bagi apa-apa perbezaan, bukan sekadar nombor.

  Dua pepijat dalam diagnostik ini ditangkap oleh ujian asap **sebelum** larian dan direkod
  di sini supaya ia tidak diulang: (i) memotong sampel pada N dagangan pertama memotong
  mengikut **urutan sauh**, jadi sampel `AL01` akan terdiri daripada awal 2020 sahaja
  (kejatuhan COVID) manakala `AL02` merentas seluruh tingkap — bias **masa**, bukan
  perbezaan alam; had itu dibuang. (ii) "bahagian jumlah pulangan" tidak tertakrif apabila
  jumlah itu **negatif**; ia dilapor NaN dan `tanpa5` dibawa sebagai metrik utama kerana ia
  tertakrif pada kedua-dua tanda dan ia metrik yang seluruh kajian ini guna.
- `buka_purata` (ikatan slot), `pulangan_dagangan`, `pegang_purata`, `pusing_slot_tahun`,
  `kos_tahun`, `dedah`, jalur benih p5–p95.

## 8. Jangkaan priori — ditulis sebelum larian

Rekod saya setakat lima pradaftar: salah pada majoriti gate setiap kali, dan pada E1 saya
salah 3, separa 2, betul 1. Jangkaan ini dicatat supaya kesilapan boleh dikira, bukan kerana
ia patut dipercayai.

1. **Kelebihan isyarat MELEMAH dengan banyak pada `AL02`** dan gate (a) **gagal** (< 25%).
   Mekanismenya: SPUS ialah permodalan besar, dan ekor kanan permodalan besar lebih nipis.
   `KOLAM_EKOR.md` mengukur 5% teratas = 63.7% jumlah pulangan pada A02; saya jangka angka
   itu **jauh lebih rendah** pada SPUS, dan `GB02` ialah pemungut ekor.
2. **Kesan had pegangan BERTAHAN** (gate (b) lulus). Ia kesan mekanikal pusing ganti lawan
   kos, bukan kesan ekor, jadi ia tidak sepatutnya bergantung pada alam.
3. **MDD `AL02` lebih cetek** daripada `AL01` pada sel yang sepadan, pada majoriti sel.
4. **T3 tercapai pada sekurang-kurangnya satu sel `AL02`** — dan apabila ia berlaku, ia akan
   berlaku pada sel yang gate (a) **gagal**, iaitu kes §6 (beta bukan isyarat). Ini jangkaan
   paling spesifik saya dan yang paling mudah dipalsukan.
5. **T1 tidak tercapai** pada mana-mana sel.

## 9. Apa yang larian ini TIDAK boleh buktikan

- Keahlian SPUS **semasa** ditolak ke belakang; ia bukan keahlian titik-masa. Tiada sejarah
  keahlian SPUS dalam repo, dan ini **tidak** boleh dibetulkan dalam larian ini.
- `AL02` juga tiada saham delist — ia subset `AL01`, jadi bias itu **kekal**, malah lebih
  teruk kerana keahlian semasa menapis keluar setiap syarikat yang gagal.
- Kolam 12 signal `GB02` dan keluar `X13`/`X15` dipilih daripada data yang sama. Bersyarat.
- Paksi `CARA` kekal `C01`, jadi kecacatan henti hari-0 hadir.
- Hingar pemilihan: E1 mengukur jalur benih **42.8 mata** pada sel terbaik. Jalur `AL02`
  akan dilaporkan dan **tiada nombor tunggal boleh dirapatkan** tanpa merujuknya.
