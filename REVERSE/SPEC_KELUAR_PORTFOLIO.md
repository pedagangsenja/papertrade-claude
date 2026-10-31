# Pradaftar E4 — KELUAR peringkat PORTFOLIO (`X31`, `X32`)

Ditulis dan dikomit **sebelum** sebarang keputusan dilihat. Skrip:
`REVERSE/step27_keluar_portfolio.py`. Keluaran: `REVERSE/KELUAR_PORTFOLIO.md`,
`REVERSE/keluar_portfolio.csv`, `REVERSE/keluar_portfolio_ringkas.csv`.
Baris gilir: `REVERSE/STRATEGI.md` §4 E4, dijalankan pada **`AL02`**.

## 1. Soalan

Pilihan keluar diukur **~12× lebih berpengaruh** daripada pilihan masuk: `NXX_KELUAR.md`
mendapati sebaran keluar **4.997 mata peratus** (`X13` +4.350% hingga `X18` −0.647%) sedangkan
lift masuk terbaik yang pernah bertahan dua tingkap ialah `N01` **+0.392 mata**.

Tetapi **kesemua 23 keluar yang pernah diuji ialah peraturan setiap posisi** — ia melihat
satu saham dan bertanya "patutkah saya jual ini?". `X31` dan `X32` ialah keluar peringkat
**portfolio**: ia melihat seluruh kedudukan dan bertanya "siapa yang patut diganti?".

Itu menyerang kesesakan yang `PORTFOLIO_N.md` diagnosis secara langsung — pegangan 84.9 bar
bermakna setiap slot berpusing ~3 kali setahun sahaja.

## 2. Bacaan setia kedua-dua baris sumber

| baris | teks registry | sumber |
|---|---|---|
| `X31` | keluar bila jatuh keluar **3 teratas pangkat 252 hari**; imbang bulanan | QuantJourney W15 |
| `X32` | imbang semula berkala sahaja, **tiada syarat keluar lain**; keluar hanya berlaku apabila pangkat berubah pada tarikh imbang | QuantJourney W04 |

Dibaca sebagaimana ditulis, kedua-duanya ialah **putaran berpangkat**; satu-satunya
perbezaan ialah `X31` **menetapkan metrik pangkat** (pulangan 252 hari) dan contoh
sumbernya memegang 3 nama, manakala `X32` membiarkan metrik terbuka.

Maka pelaksanaan:

- **`X32`** — putaran: pada setiap tarikh imbang, portfolio menjadi **k teratas** mengikut
  metrik paksi `URUTAN`, dipilih daripada (pegangan semasa ∪ calon berisyarat). Pegangan
  dijual **hanya** apabila ia keluar daripada k teratas. Tiada henti, tiada sasaran.
- **`X31`** — sama, tetapi metrik pangkat **dikunci kepada pulangan 252 hari**, mengikut
  spesifikasi sumber. Paksi `URUTAN` tidak dikenakan padanya.

Saya **tidak** menambah jalur histeresis yang sumber tidak sebut. Kesan sampingannya ialah
`X31` menjadi kes khas `X32`, dan itu memang apa yang teks sumber katakan; melaporkannya
begitu lebih jujur daripada mereka-reka perbezaan.

## 3. Rujukan perbandingan — tidak dijana semula

Keluar **setiap posisi** pada alam dan kos yang sama sudah diukur dalam E2
(`REVERSE/alam.csv`, komit `d8262a1`). Nombor itu dibaca terus, tidak dijalankan semula,
supaya perbandingan memakai angka yang sudah dikomit. Rujukan utama: `AL02` ·
`GB02_atau3` · `X15` · tiada had · `U01` · 20 slot = **CAGR +21.01% / MDD −38.10%**
(terbaik E2).

## 4. Grid

- **MASUK** (2): `GB02_atau3`, `RAWAK` (kawalan)
- **SLOT** (3): 8, 20, 40 — kapasiti `AL02` diukur 108, jadi ketiga-tiganya mengikat
- **IMBANG** (2): 21 sesi (bulanan, seperti kedua-dua sumber) · 63 sesi (suku)
- **KELUAR**:
  - `X32` × **URUTAN** (3): `U02` persentil RS · `U14` momentum 12−1 · `U01` rawak (20 benih)
  - `X31` (metrik dikunci 252 hari; paksi `URUTAN` tidak dikenakan)

`X32`: 2 × 3 × 2 × 3 = 36 konfigurasi · `X31`: 2 × 3 × 2 = 12 → **48 konfigurasi**,
`U01` 20 benih → **276 larian**.

Dikunci: alam `AL02`, cara `C01` (beli pada buka berikutnya), saiz `SZ01` berat sama rata
`1/slot`, kos penuh dua sisi, tiada margin, satu posisi setiap ticker. Tingkap keputusan
**2020–2025**; latih 2012–2019 direkod.

**Mekanik berbeza daripada `step24`** (putaran berpangkat dengan jam imbang, bukan keluar
setiap posisi), jadi kawalan regresi E1/E2 **tidak terpakai**. Enjin membawa kawalannya
sendiri: `RAWAK` masuk dan `U01` pangkat rawak dengan 20 benih.

## 5. Gate dan **setiap** gabungan keputusan

- **P1** CAGR > 17.95% · **P2** MDD ≥ −26.82% · **T1** = P1 ∧ P2
- **T3** CAGR ≥ 15% ∧ MDD ≥ −15%
- **P3** CAGR > persentil-95 kawalan `U01` pada (masuk, slot, imbang) yang sama
- **P4** nisbah > 0.669
- **E4a** (khusus E4) CAGR terbaik `X31`/`X32` > **+21.01%**, iaitu keluar peringkat
  portfolio mengalahkan keluar setiap posisi terbaik pada alam yang sama

| (T1 ∨ T3) | P3 | E4a | Keputusan |
|---|---|---|---|
| ya | ya | — | **BERHENTI–MENANG.** Bekukan, ujian hadapan ≥ 126 sesi. |
| ya | tidak | — | Kepelbagaian/beta, bukan pemilihan. Lapor sebagai `T4`-kelas; **teruskan ke E5**. |
| tidak | — | ya | Keluar portfolio **mengalahkan** keluar setiap posisi tetapi masih bawah SPUS. Rekod sebagai arah paling menjanjikan yang tinggal; **teruskan ke E5**. |
| tidak | — | tidak | Tiada dapatan. **Teruskan ke E5.** |

`P4` dilapor sebagai BERHENTI–SEPARA; ia tidak pernah menghentikan baris gilir.

## 6. Diagnostik yang direkod (bukan gate)

Pusing ganti (dagangan/slot/tahun), **pendedahan** (lajur kritikal: E2 menunjukkan memotong
pegangan pada alam bersignal nipis hanya memindahkan modal ke tunai — jika `X32` berbuat
sama, pendedahan akan runtuh dan itu penjelasannya, bukan pulangan), seretan kos setahun,
tempoh pegangan purata, bahagian ekor 5% teratas dan `tanpa5` (takrif sama seperti E2/E3),
jalur benih `U01` p5–p95, dan bilangan slot yang benar-benar terisi.

## 7. Jangkaan priori — ditulis sebelum larian

1. **T1 = 0 dan T3 = 0.** Keyakinan tinggi: E1, E2 dan E3 kesemuanya memberi `P2` ≈ 0, dan
   hujah strukturnya kini ada tiga pengesahan bebas — portfolio ekuiti panjang-sahaja yang
   100% melabur tidak boleh mempunyai MDD lebih cetek daripada indeks ekuiti.
2. **Pendedahan `X32` runtuh pada `imbang` 21 dengan masuk `GB02_atau3`**, kerana `AL02`
   membekalkan hanya 7.7 isyarat/sesi. Saya jangka pendedahan **< 70%** pada sekurang-
   kurangnya separuh sel bersignal — mekanisme yang sama seperti kegagalan gate (b) E2.
3. **`E4a` GAGAL**: CAGR terbaik tidak melebihi +21.01%. Putaran menambah kos tanpa
   menambah kemahiran, seperti E3 di mana putaran kalah kepada memegang bakul terbaik.
4. **`P3` lulus pada minoriti sel** (< 50%), dan jika mana-mana urutan menang ia **`U14`**,
   mengulangi E3.
5. **`X31` ≈ `X32` dengan `U14`**, kerana pulangan 252 hari dan momentum 12−1 berkorelasi
   tinggi. Saya jangka bezanya **< 3 mata CAGR** pada sel yang sepadan.

## 8. Apa yang larian ini TIDAK boleh buktikan

- `AL02` mewarisi bias keahlian SPUS **semasa** dan tiada saham delist.
- Kolam 12 signal `GB02` dan metrik pangkat dipilih daripada data yang sama. Bersyarat.
- Paksi `CARA` kekal `C01`.
- Hanya `U01` mempunyai jalur benih; `U02`, `U14` dan `X31` adalah satu cabutan tentu, jadi
  `P3` bagi baris itu ialah satu cabutan lawan satu jalur.
- `imbang` 21 dan 63 ialah dua titik; lengkung kekerapan imbang tidak dipetakan.
