# ALAM — `AL02`: kelebihan pada alam yang repo benar-benar dagang

Pradaftar: `REVERSE/SPEC_ALAM.md` (komit `bb970c8`, sebelum larian).
Skrip: `REVERSE/step25_alam.py` · Data: `REVERSE/alam.csv`, `REVERSE/alam_ringkas.csv`,
`REVERSE/alam_ekor.csv`

160 konfigurasi `AL02` (2 masuk × 5 slot × 2 keluar × 4 had pegang × 2 urutan), `U01` 20
benih → **1,680 larian**, 9 minit. Nombor `AL01` dibaca terus daripada larian E1 yang sudah
dikomit — tidak dijana semula.

## Keputusan: T1 **0**, T3 **0** pada KEDUA-DUA alam

| | `AL01` (a02, 3,260 ticker) | `AL02` (SPUS, 214 ticker) |
|---|---:|---:|
| T1 (CAGR > 17.95% **dan** MDD ≥ −26.82%) | **0** / 160 | **0** / 160 |
| T3 (CAGR ≥ 15% **dan** MDD ≥ −15%) | **0** / 160 | **0** / 160 |
| lulus keempat-empat gate | 0 | 0 |
| gate (a) isyarat > p95 kawalan | 56.2% | **46.2%** (ambang 25%) |
| gate (b) had 42/63 > tiada had | 67.5% | **27.5%** (ambang 50%) |

Corak `P1` lawan `P2` daripada E1 berulang tanpa perubahan: sel terbaik `AL02`
(`GB02_atau3` · 20 slot · `X15` · had 63 · `U01`) memberi CAGR **+21.01%** — **melebihi**
SPUS 17.95% — tetapi MDD **−38.10%**. Paksi pulangan dan paksi risiko tidak pernah sejajar.

## KECACATAN PRADAFTAR — mesti dinyatakan sebelum apa-apa tafsiran

Spec §5 menetapkan dua keadaan sahaja:

- **KEKAL** = (a) **DAN** (b)
- **MATI** = **(a) gagal**

Keputusan sebenar ialah **(a) LULUS, (b) GAGAL** — iaitu **bukan** KEKAL dan **bukan** MATI.
Spec saya tidak meliputi kes ini. Lebih buruk, kod saya mengira `kekal = (a) and (b)` dan
mencetak `E2 MATI` apabila itu palsu, jadi **pelaksanaan saya membuat keputusan yang spec
tidak benarkan**.

Rasional MATI yang ditulis dalam spec ialah: *"Kelebihan isyarat tidak wujud pada alam yang
kita dagang, jadi menguji E3–E6 pada `AL01` adalah menguji pada alam yang salah."* Premis
itu **dipalsukan** oleh keputusan: gate (a) lulus pada 46.2%, jauh di atas ambang 25%.
Kelebihan isyarat **memang wujud** pada alam dagangan.

Jadi mengisytiharkan BERHENTI–TUTUP bermakna menerima kesimpulan yang premisnya palsu, dan
mengisytiharkan KEKAL bermakna mengabaikan perkataan "DAN" yang saya tulis sendiri.
**Keputusan ini diserahkan kepada pengguna, bukan dipilih selepas melihat nombor.**

Pembetulan proses untuk pradaftar seterusnya: setiap spec mesti menyenaraikan **setiap
gabungan** keputusan gate, bukan hanya "semua lulus" dan "yang utama gagal".

## Dapatan yang paling penting: masalah EKOR ialah sifat ALAM, bukan hukum pasaran

Diagnostik setiap dagangan (`GB02_atau3` × `X13` × had 42, tingkap keputusan, enjin keluar
yang sama):

| alam | n | purata | 5% teratas = % jumlah pulangan | purata **tanpa** 5% teratas |
|---|---:|---:|---:|---:|
| `AL01` (a02) | 195,671 | +4.604% | **101.67%** | **−0.081%** |
| `AL02` (SPUS) | 12,665 | +4.892% | **47.92%** | **+2.682%** |

Pada `AL01`, 5% dagangan teratas membawa **lebih daripada 100%** jumlah pulangan — 95% yang
lain adalah **negatif bersih**. Pada `AL02` mereka membawa 47.9%, dan baki 95% memberi
**+2.682%**.

**Ini kali PERTAMA dalam seluruh kajian bahawa `tanpa5` adalah POSITIF.** Setiap laporan
terdahulu — `SETUP.md` (598/598 negatif), `NXX.md`, `GABUNGAN.md`, `KOMBINASI.md` —
mendapati `tanpa5` negatif dan merumuskan bahawa kelebihan "hidup sepenuhnya dalam ekor
kanan". Keputusan ini menunjukkan rumusan itu **khusus kepada alam a02**, bukan hukum: alam
3,260 nama termasuk ekor mikro-kapitalisasi seperti loteri; alam 214 nama permodalan besar
tidak.

**Had yang membatalkan separuh daripada dapatan ini:** keahlian SPUS ialah petikan
**semasa**, dan bias itu menghasilkan **tepat** kesan ini — syarikat yang kekal dalam indeks
sampai hari ini mempunyai taburan yang kurang seperti loteri **mengikut binaan**. Spec §4
mengisytiharkan asimetri ini sebelum larian. Jadi `tanpa5 = +2.682%` ialah **petunjuk
mekanisme, bukan ukuran yang ditetapkan**. Ia memerlukan keahlian titik-masa untuk
disahkan, dan repo tidak mempunyainya.

## `AL02` lebih baik pada KEDUA-DUA paksi, tetapi masih tidak cukup

Pada 80 sel sepadan (`GB02_atau3`):

- median beza CAGR `AL02 − AL01` = **+2.69 mata**
- median beza MDD = **+6.19 mata lebih cetek**; MDD lebih cetek pada **58 daripada 80** sel

Jadi alam dagangan sebenar memberi nombor **lebih baik** daripada alam kajian, bukan lebih
buruk. Itu bertentangan dengan jangkaan biasa bahawa alam yang lebih kecil akan melemahkan
hasil — dan ia konsisten dengan dapatan ekor di atas serta dengan bias keahlian semasa.

## Had pegangan TIDAK merentas alam

E1 mendapati had 42 bar mengalahkan "tiada had" dalam **72/128** sel `AL01` (+27 mata pada
sel terbaik). Pada `AL02` ia **27.5%** — ia **gagal** merentas alam.

Mekanismenya boleh dibaca daripada ketumpatan isyarat: `AL01` membekalkan **105.2**
isyarat/sesi, jadi memotong pegangan membebaskan modal yang segera diisi semula. `AL02`
membekalkan **7.7**/sesi; memotong pegangan di sana hanya memindahkan modal ke **tunai**.
Lajur `dedah` mengesahkannya — `GB02_atau3` · 160 slot · `X13` · had 21 jatuh kepada
**29.41%** dilabur.

**Pelajaran yang boleh dipindahkan: had pegangan bukan peraturan, ia pertukaran antara
pusing ganti dan ketumpatan isyarat.** Ia membantu hanya apabila kolam calon boleh mengisi
semula slot yang dikosongkan. Jangan bawa "had 42 bar" ke E3–E6 sebagai tetapan tetap.

## Jangkaan priori lawan keputusan

| | Saya jangka | Berlaku | |
|---|---|---|---|
| (1) kelebihan isyarat mati pada `AL02`, gate (a) gagal | gagal (< 25%) | **lulus 46.2%** | **salah** |
| (2) kesan had pegangan bertahan, gate (b) lulus | lulus (≥ 50%) | **gagal 27.5%** | **salah** |
| (3) MDD `AL02` lebih cetek pada majoriti sel | ya | ya, **58/80** | betul |
| (4) T3 tercapai pada sel yang gate (a) gagal (beta bukan isyarat) | ya | **T3 = 0** | **salah** |
| (5) T1 tidak tercapai | ya | ya | betul |

Dua betul, tiga salah — dan kedua-dua jangkaan yang saya nyatakan paling yakin (#1
mekanisme ekor nipis melemahkan kelebihan, #4 "paling mudah dipalsukan") adalah salah, dan
**salah ke arah bertentangan**: ekor yang lebih nipis menjadikan kelebihan **lebih sihat**,
bukan lebih lemah.

Ini pradaftar keenam berturut-turut dengan majoriti jangkaan salah. Corak itu sendiri
dapatan: **jangkaan priori saya tidak bermaklumat dan patut diabaikan memihak kepada
ukuran.**

## Had

- Keahlian SPUS **semasa** ditolak ke belakang sampai 2012. Bukan titik-masa. Bias memihak
  kepada sistem, dan ia **mengacau** dapatan ekor di atas secara langsung.
- `AL02` ialah subset `AL01`; bias tiada-delist **kekal**, malah lebih teruk.
- Kolam 12 signal `GB02` dan keluar `X13`/`X15` dipilih daripada data yang sama. Bersyarat.
- `AL02` 214 ticker dengan 7.7 isyarat/sesi — kapasiti 108 (tiada had) dan 67 (had 42), jadi
  slot 160 tidak mengikat langsung dan sel itu ialah `SZ10` pada alam SPUS.
- Paksi `CARA` kekal `C01`.
- Jalur benih `AL02` lebih sempit daripada `AL01` (sel terbaik p5 17.59 – p95 24.55 = 6.96
  mata lawan 42.8 mata pada E1), tetapi ia **bukan** sifar; tiada nombor tunggal di sini
  boleh dirapatkan kepada kurang daripada ±3 mata.
