# Pradaftar — lengkung TEMPOH PEGANG dan lengkung SLOT

Ditulis dan dikomit **sebelum** sebarang keputusan dilihat. Skrip:
`REVERSE/step24_pegang_slot.py` (dikomit dalam komit yang sama).
Keluaran: `REVERSE/PEGANG_SLOT.md`, `REVERSE/pegang_slot.csv`,
`REVERSE/pegang_slot_ringkas.csv`.

## 1. Dua soalan

**Q1 — PEGANG.** Jangkaan setiap dagangan dan bilangan pusingan setahun bergerak ke arah
**bertentangan** apabila tempoh pegangan dihadkan. Repo sudah ukur hujungnya sahaja:

| keluar | pegang | jangkaan/dagangan (tahan, bersih) | pusingan/slot/tahun | kompaun aritmetik |
|---|---:|---:|---:|---:|
| `X29` pegang tetap 10 bar | 10 bar | **+0.294%** | ~25 | 1.00294²⁵ = **+7.6%** |
| `X13` `rsi14 > 70` | ~85 bar | **+4.350%** | ~3 | 1.0435³ = **+13.6%** |

Antara 10 dan 85 bar: **tiada satu titik pun diukur.** Lajur terakhir ialah aritmetik atas
dua titik yang diukur, bukan ramalan. Jika 21 bar memberi +1.2%, 1.012¹² = **+15.4%** dan
had pegangan MENANG; jika ia memberi +0.8%, 1.008¹² = +10.0% dan ia KALAH. Soalannya ialah
di mana lengkung itu berada, dan ia tidak boleh dijawab daripada kajian setiap-dagangan
(yang tidak nampak pusing ganti) mahupun daripada `PORTFOLIO_N.md` (yang mengunci pegangan
kepada peraturan keluar).

Kekangan pengguna yang tidak pernah dikenakan: repo mentakrifkan swing = **3–30 hari**, dan
**setiap** konfigurasi menang dalam 413 ujian memegang ~85 bar ≈ 4 bulan.

**Q2 — SLOT (`SZ10`).** Dua kajian bebas mengukur penambahbaikan **monoton pada kedua-dua
paksi** apabila slot bertambah, dan kedua-duanya berhenti sebelum lengkung rata:

- `PORTFOLIO_N.md`: 8 slot → CAGR 9.40% / MDD −44.82%; 40 slot → **13.92% / −38.38%**
- `PEMBINAAN.md`: `A8` → `C40` = pulangan **+7.90 mata**, MDD **+14.69 mata lebih cetek**
- `KOLAM_EKOR.md`: kolam penuh berat sama rata **+1.64%/bulan** lawan saham median +0.82%

80, 160, 320 slot tidak pernah dijalankan. `SZ10` kekal `SEDIA` sejak didaftarkan.

## 2. Mengapa kedua-duanya dalam satu larian

Q1 dan Q2 **berinteraksi**. Had pegangan menaikkan pusing ganti, yang menaikkan bilangan
posisi serentak yang boleh dibiayai pada bilangan slot tetap; menambah slot menurunkan berat
setiap posisi, yang menukar berapa banyak satu pemenang ekor menyumbang. Menguji satu paksi
sambil mengunci satu lagi ialah tepat kesilapan yang `PORTFOLIO_N.md` lakukan pada paksi ini.

## 3. Grid — tepat, tiada penambahan selepas melihat keputusan

- **MASUK** (2): `GB02_atau3` = `N19` ∪ `N37` ∪ `N115`; `RAWAK` = semua calon layak (kawalan)
- **SLOT** (8): 8, 20, 40, 80, 160, 320, 640, 1280
- **KELUAR** (2): `X13` (`rsi14 > 70`), `X15` (Chandelier 4×ATR14)
- **PEGANG** (5): tiada had, 63, 42, 21, 10 bar — had bermaksud **keluar pada buka bar
  ke-N selepas masuk jika peraturan keluar belum tercetus**; ia memotong, tidak pernah
  melanjutkan
- **URUTAN** (2): `U01` rawak berbenih (20 benih → jalur), `U08` ATR% menaik (tentu, 1 larian)

2 × 8 × 2 × 5 × 2 = **320 konfigurasi**; `U01` 20 benih → **3,360 larian**.

### 3.1 Kapasiti kolam — diukur sebelum grid ditetapkan

Had slot teratas tidak boleh dipilih sewenang-wenang: jika ia di bawah kapasiti kolam,
`SZ10` tidak pernah diukur. Diagnostik kapasiti (slot 100,000 = tidak mengikat; `U08`;
tiada gate dinilai) memberi:

| masuk | had pegang | posisi serentak pada tepu | pegang purata |
|---|---|---:|---:|
| `GB02_atau3` | tiada | **1,739** | 74.4 bar |
| `GB02_atau3` | 21 | **753** | 17.4 bar |
| `RAWAK` | tiada | 2,992 | 16.1 bar |
| `RAWAK` | 21 | 2,949 | 10.1 bar |

Calon layak purata 2,395/sesi; calon berisyarat `GB02_atau3` 104/sesi.

Maka pada **slot 1280**: lorong berhad-pegangan sudah **melepasi** kapasiti (753 < 1280),
jadi `SZ10` diukur **terus** di sana, bukan dianggar; lorong tanpa had berada pada 74%
kapasiti. Lajur `buka_purata` melaporkan ikatan sebenar setiap sel.

Tetap pada nilai yang sama seperti `PORTFOLIO_N.md` supaya hanya dua paksi berubah:
alam `AL01` (A02 cair), cara `C01` (beli buka esok), saiz `SZ01` (berat sama rata `1/slot`),
imbang `IB01` (pada isyarat sahaja), korelasi `KR01` (tiada had), instrumen `IS01`,
sauh HARIAN, kos penuh dua sisi (0.1% komisen + slippage 0.05/0.10/0.25% ikut nilai20),
tiada margin, satu posisi setiap ticker, had imbasan keluar 504 bar.

Tingkap keputusan **2020–2025**; tingkap latih **2012–2019** direkod bagi setiap baris.

## 4. Gate — ditetapkan sekarang

Sama seperti `SPEC_PORTFOLIO_N.md` §3.4, pada median merentas benih:

- **P1** CAGR median > **SPUS 17.95%**
- **P2** MDD median ≥ **SPUS −26.82%** (iaitu lebih cetek)
- **P3** CAGR median > **persentil-95** kawalan `RAWAK` pada (slot, keluar, pegang, urutan)
  yang **sama**
- **P4** `CAGR ÷ |MDD|` > **0.669** (garis campuran SPUS + tunai, `SISTEM.md`)
- **LULUS** = keempat-empatnya

Dua dakwaan tambahan yang ditetapkan sekarang, supaya ia tidak boleh dilonggarkan kemudian:

- **Q1 LULUS** hanya jika sekurang-kurangnya satu had pegangan memberi CAGR median **lebih
  tinggi** daripada `tiada had` pada (masuk, slot, keluar, urutan) yang sama, **dan**
  bezanya melebihi jalur benih `U01` pada sel itu (p5–p95).
- **Q2 / `SZ10` LULUS** hanya jika terdapat satu bilangan slot yang melepasi **P1 DAN P2
  serentak**. "MDD lebih cetek sahaja" **bukan** kelulusan — itu kesan pendedahan, dan
  `SISTEM.md` sudah tunjukkan nisbah campuran hampir pemalar 0.642–0.669 merentas berat.

## 5. Diagnostik yang direkod (bukan gate)

Tanpa ini lengkung tidak boleh dibaca: `pulangan_dagangan` (purata pulangan bersih setiap
dagangan DITUTUP), `pegang_purata` (bar), `pusing_slot_tahun` (dagangan ÷ slot ÷ tahun),
`buka_purata` (purata posisi terbuka), `dedah` (% dilabur), `n_dagangan`, `kos_tahun`
(anggaran seretan kos setahun = pusingan × kos pergi-balik purata).

`buka_purata` ialah ujian ketepuan: jika `buka_purata` < `slot`, kekangan slot **tidak
mengikat** dan bilangan slot itu sudah **kolam penuh** — itulah `SZ10` diukur, bukan
dianggarkan.

## 6. Jangkaan priori — ditulis sebelum larian

Rekod saya: salah pada 2 daripada 3 gate dalam tiga pradaftar berturut-turut
(`SPEC_SILANG` §7, `SPEC_SISTEM` §7, `SPEC_NXX`), dan pada `SPEC_PORTFOLIO_N` saya betul 2,
separa 1, salah 1. Jangkaan di bawah mesti dibaca dengan rekod itu.

1. **Had 10 bar KALAH jelas.** `X29` sudah memberi +0.294% bersih dan seretan kos pada ~25
   pusingan ialah 7.5–17.5 mata/tahun lawan 0.9–2.1 pada 3 pusingan.
2. **Had 21–42 bar ialah kes sebenar.** Saya jangka ia **kalah**, tetapi dengan jurang kecil
   (dalam 3 mata CAGR) — bukan runtuh seperti had 10 bar. Jika mana-mana had menang, saya
   jangka **42 bar** dengan `X15`, bukan 21 dengan `X13`.
3. **Lengkung slot terus menaik sampai ~160 kemudian rata**, dan MDD terus mencetek. Saya
   jangka **P1 lulus** pada slot tinggi dan **P2 lulus** pada slot tinggi, tetapi **P3 gagal**
   di sana — kerana apabila slot menghampiri kolam penuh, sumbangan isyarat → 0 dan lorong
   bersignal menumpu kepada kawalan rawak. Itu akan menjadikan `SZ10` "menang" atas sebab
   yang menafikan seluruh kajian: memiliki semuanya, bukan memilih.
4. **`SZ10` LULUS P1+P2 pada sekurang-kurangnya satu slot.** Ini jangkaan paling kuat saya
   dan ia bertentangan dengan setiap keputusan terdahulu repo; jika ia benar, yang menang
   ialah **struktur indeks**, bukan isyarat.
5. **Ketepuan.** Diagnostik §3.1 sudah menjawab sebahagiannya: kapasiti ialah 1,739
   (tanpa had) dan 753 (had 21). Jangkaan saya yang tinggal ialah bahawa **CAGR mencapai
   puncak jauh sebelum kapasiti** — sekitar 160–320 slot — dan mendatar atau merosot
   selepas itu kerana kos dan kecairan, bukan kerana kekurangan calon.

## 7. Apa yang larian ini TIDAK boleh buktikan

- Alam `AL01` **tiada saham delist** — setiap CAGR condong ke atas, dan lorong slot tinggi
  condong **lebih banyak** kerana ia memegang lebih banyak saham ekor.
- Kolam 12 signal `GB02` dan keluar `X13`/`X15` dipilih daripada data yang **sama**; tiada
  tingkap bebas tinggal. Keputusan kekal **bersyarat**.
- Paksi `CARA` kekal `C01`, jadi kecacatan henti hari-0 hadir dalam setiap nombor.
- Slot 160–320 mengandaikan kecairan menyerap saiz pesanan; model kos hanya menyesuaikan
  slippage ikut nilai dagangan 20 hari, ia **tidak** memodelkan impak pasaran.
- `+10%/bulan` kekal tertutup secara aritmetik (`SASARAN.md`). Tiada dakwaan sedemikian
  akan dibuat.
