# Pradaftar E5 — KORELASI `KR03`: had bilangan pegangan setiap industri

Ditulis dan dikomit **sebelum** sebarang keputusan dilihat. Skrip:
`REVERSE/step28_korelasi.py`. Keluaran: `REVERSE/KORELASI.md`, `REVERSE/korelasi.csv`,
`REVERSE/korelasi_ringkas.csv`. Baris gilir: `REVERSE/STRATEGI.md` §4 E5.

## 1. Soalan, dan mengapa ia eksperimen paling tepat sasaran yang tinggal

Merentas E1–E4 — **568 konfigurasi, empat mekanik berbeza** — `P1` (pulangan) lulus 26, 29
dan 33 kali, dan **`P2` (MDD) lulus SIFAR kali**. Paksi risiko ialah satu-satunya pengikat.

`KR03` ialah satu-satunya baris registry yang menyerang paksi itu **secara langsung**:
8–10 slot yang semuanya dalam satu industri ialah **berkesan 2–3 slot**, dan itu tidak
pernah diukur. Setiap eksperimen terdahulu berjalan dengan `KR01` (tiada had).

## 2. Alam: `AL04` titik-masa — pembetulan yang dipaksa oleh E4

E4 membuktikan keahlian SPUS **hari ini**, ditolak ke belakang, menyanjung MDD sebanyak
**30.9 mata** (−37.94% menjadi −68.80% apabila keahlian dijadikan kausal). Mengukur kesan
had industri pada paksi **risiko** menggunakan alam yang paksi risikonya sudah terbukti
rosak adalah tidak bermakna.

Maka E5 memakai **`AL04` titik-masa**: **N teratas ikut nilai dagangan 20 hari pada sauh
itu sendiri**. Ia kausal sepenuhnya — tiada maklumat selepas sauh diguna. N ∈ {214, 500};
214 memadankan saiz SPUS supaya nombornya setanding dengan E2–E4.

**Had yang kekal:** `AL04` membetulkan keahlian tetapi **bukan** delist. Alam asas `a02`
tiada saham delist, jadi tiada alam dalam kajian ini bersih sepenuhnya.

## 3. Peta industri

`data/skrin/tv_us.csv`: **4,146 ticker**, **127 industri** dalam **20 sektor**. Liputan A02
2025 = 2,595/3,260 (79.6%); liputan pada 214 teratas nilai20 = **206/214**.

Ticker tanpa industri dikumpulkan sebagai **satu** kumpulan `TIDAK_DIKETAHUI` yang **tertakluk
kepada had yang sama**. Itu pilihan konservatif: melayan setiap yang tidak diketahui sebagai
kumpulannya sendiri akan membuka lubang yang membenarkan kepekatan tanpa had. Bilangan
pegangan tidak diketahui direkod.

Peta industri ialah petikan **semasa** — ia tidak berubah mengikut masa. Industri syarikat
jarang berubah, tetapi ini tetap ketidaksempurnaan dan dinyatakan di §8.

## 4. Mekanik

Enjin E4 (`step27.simulasi`, putaran berpangkat `X32`) diguna semula, dengan **satu**
tambahan: semasa memilih k teratas, calon dilangkau jika industrinya sudah mencapai had
dalam set sasaran. Parameter lalai `had_ind=None` memberi tingkah laku **identik** dengan
E4 — disahkan dalam ujian asap sebagai kawalan regresi.

## 5. Grid

- **ALAM** (2): `AL04` 214 teratas · `AL04` 500 teratas (titik-masa)
- **MASUK** (2): `RAWAK` (seluruh alam diperingkat) · `GB02_atau3` (isyarat)
- **URUTAN** (2): `U02` persentil RS (pemenang E4) · `U01` rawak (kawalan, 20 benih)
- **SLOT** (3): 8, 20, 40
- **HAD INDUSTRI** (4): tiada (`KR01` asas) · 1 · 2 · 3
- **IMBANG**: **63 dikunci.** Suku menang di E4, dan soalan E5 ialah kekangan **struktur**
  bukan kekangan **masa**; mengubah dua perkara sekali gus akan mengelirukan sebabnya.

2 × 2 × 2 × 3 × 4 = **96 konfigurasi**; `U01` 20 benih → **1,008 larian**.

Dikunci: cara `C01`, saiz `SZ01` berat sama rata `1/slot`, keluar `X32`, kos penuh dua sisi,
tiada margin, satu posisi setiap ticker. Tingkap keputusan 2020–2025; latih 2012–2019
direkod.

## 6. Gate dan **setiap** gabungan keputusan

- **P1** CAGR > 17.95% · **P2** MDD ≥ −26.82% · **T1** = P1 ∧ P2
- **T3** CAGR ≥ 15% ∧ MDD ≥ −15%
- **P3** CAGR > persentil-95 kawalan `U01` pada (alam, masuk, slot, had) yang sama
- **P4** nisbah > 0.669
- **E5a** (khusus E5, dua bahagian):
  - **(a-MDD)** had 1/2/3 memberi MDD median **lebih cetek** daripada `tiada` pada **≥ 50%**
    sel sepadan
  - **(a-NISBAH)** sekurang-kurangnya satu had memberi nisbah median **lebih tinggi**
    daripada `tiada` pada sel sepadannya

| T1 ∨ T3 | E5a-MDD | E5a-NISBAH | Keputusan |
|---|---|---|---|
| ya | — | — | **BERHENTI–MENANG.** Bekukan, ujian hadapan ≥ 126 sesi. |
| tidak | ya | ya | Had industri **berfungsi** sebagai lever risiko walaupun tidak mencukupi. Rekod sebagai komponen untuk mana-mana lorong hadapan; **teruskan ke E6**. |
| tidak | ya | tidak | Had industri mengurangkan MDD **dan** pulangan dalam kadar yang sama = **peruntukan tunai dalam samaran** (`SISTEM.md`: nisbah campuran hampir pemalar 0.642–0.669). Bukan lever baharu; **teruskan ke E6**. |
| tidak | tidak | — | `KR03` tidak berfungsi. **Teruskan ke E6.** |

`P4` dilapor sebagai BERHENTI–SEPARA; ia tidak menghentikan baris gilir.

## 7. Jangkaan priori — ditulis sebelum larian

1. **T1 = 0 dan T3 = 0** — kali kelima. Keyakinan sangat tinggi; hujah strukturnya kini ada
   empat pengesahan bebas.
2. **E5a-MDD LULUS.** Had industri ialah kawalan kepekatan langsung; ia sepatutnya
   mencetekkan MDD pada majoriti sel.
3. **E5a-NISBAH GAGAL.** Ini jangkaan sebenar saya dan ia mengikut terus daripada
   `SISTEM.md`: mengekang kepekatan mengurangkan pulangan **dan** risiko bersama, jadi
   nisbahnya hampir tidak berubah. Jika saya salah di sini, `KR03` ialah lever tulen dan
   itu dapatan.
4. **Dapatan E4 berulang pada alam kausal**: `RAWAK` > `GB02_atau3`, kerana menapis membuang
   calon yang pemeringkat perlukan.
5. **Had 1 memberi MDD paling cetek tetapi CAGR paling rendah**, dan had 3 hampir sama
   dengan tiada had kerana 8 slot jarang mengandungi 4 nama industri yang sama.

## 8. Apa yang larian ini TIDAK boleh buktikan

- `AL04` membetulkan keahlian tetapi **bukan** delist; alam asas `a02` tiada saham delist.
- Peta industri ialah petikan **semasa**, bukan titik-masa. Industri jarang berubah tetapi
  penyusunan semula dan perubahan model perniagaan berlaku.
- Liputan industri 79.6% pada alam penuh; 8/214 pegangan berpotensi `TIDAK_DIKETAHUI`.
- `imbang` dikunci 63; interaksi had industri × kekerapan imbang tidak diuji.
- Hanya `U01` mempunyai jalur benih; `U02` ialah satu cabutan tentu.
- Paksi `CARA` kekal `C01`.
