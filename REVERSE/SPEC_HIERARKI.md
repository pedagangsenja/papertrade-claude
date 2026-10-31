# Pradaftar E6 — GABUNGAN `GB07`: hierarki merentas paksi

Ditulis dan dikomit **sebelum** sebarang keputusan dilihat. Skrip:
`REVERSE/step29_hierarki.py`. Keluaran: `REVERSE/HIERARKI.md`, `REVERSE/hierarki.csv`,
`REVERSE/hierarki_ringkas.csv`. Baris gilir: `REVERSE/STRATEGI.md` §4 E6 — **eksperimen
terakhir**. Selepas ini, tanpa T1/T3, syarat **BERHENTI–TUTUP** tercapai.

## 1. Soalan

`GB07` = "signal A tentukan **ALAM**, signal B tentukan **URUTAN**". Ia satu-satunya
operator gabungan yang belum diuji, dan satu-satunya yang menggunakan signal pada **paksi
berlainan**. `GB01` `DAN`, `GB02` `ATAU`, `GB03` undi, `GB04` agregat pangkat dan `GB08`
penapis terbalik semuanya sudah diuji.

E4 memberinya makna baharu dan tepat. Di sana, `GB02_atau3` sebagai **pintu masuk harian**
memusnahkan putaran berpangkat: ia memberi **7.7 isyarat/sesi**, jadi pemeringkat kehilangan
calon dan lorong bersignal (+24.04%) kalah kepada lorong **tanpa** isyarat (+47.44%).

Tetapi "menapis" dan "mentakrif alam" bukan perkara yang sama:

- **Pintu harian** (apa yang gagal): nama layak hanya pada hari isyarat mencetus. Kolam
  runtuh kepada segelintir.
- **Saringan berdiri** (apa yang E6 uji): nama layak **selagi** syarat benar. Kolam kekal
  ratusan, tetapi yang paling teruk dikecualikan.

E6 menguji sama ada saringan berdiri boleh memberi apa yang pintu harian tidak boleh.

## 2. Alam dan mekanik

Alam asas: **`AL04` titik-masa 500 teratas** ikut nilai dagangan 20 hari pada sauh itu
sendiri — luas, supaya saringan mempunyai ruang untuk bekerja tanpa meruntuhkan kolam.
Kausal; pembetulan yang dipaksa oleh E4 dikekalkan.

Enjin: `step27.simulasi` (putaran berpangkat `X32`, imbang 63) dengan `had_ind` E5. Saringan
A dikenakan dengan **memotong peta calon pada setiap sauh** — tiada perubahan enjin, jadi
kawalan regresi E4/E5 kekal sah.

## 3. Grid

**Signal A — ALAM (saringan berdiri, 5):**

| | syarat | dijangka mengekalkan |
|---|---|---|
| `A0` | tiada saringan (asas, = E5) | 500 |
| `A1` | `tutup > ma200` | separuh hingga tiga perempat |
| `A2` | `rs_pst ≥ 50` (atas median RS) | ~separuh |
| `A3` | `rs_pst ≥ 80` (kuintil teratas RS) | ~seperlima |
| `A4` | `atr_pct` di bawah **median keratan rentas** pada sauh itu | ~separuh |

`A4` ialah satu-satunya saringan yang menyasarkan paksi yang **gagal** (risiko) dan bukan
paksi yang sudah lulus (pulangan). Semua ambang dinilai **pada sauh**, keratan rentas, tiada
maklumat selepas sauh.

**Signal B — URUTAN (3):** `U02` persentil RS (pemenang E4) · `U14` momentum 12−1 ·
`U01` rawak (kawalan, 20 benih)

**SLOT** (2): 8, 20 · **HAD INDUSTRI** (2): tiada, 2 · **IMBANG**: 63 dikunci

5 × 3 × 2 × 2 = **60 konfigurasi**; `U01` 20 benih → **440 larian**.

Dikunci: cara `C01`, saiz `SZ01`, keluar `X32`, kos penuh dua sisi, tiada margin, satu
posisi setiap ticker. Tingkap keputusan 2020–2025; latih 2012–2019 direkod.

## 4. Gate dan **setiap** gabungan keputusan

- **P1** CAGR > 17.95% · **P2** MDD ≥ −26.82% · **T1** = P1 ∧ P2
- **T3** CAGR ≥ 15% ∧ MDD ≥ −15%
- **P3** CAGR > persentil-95 kawalan `U01` pada (A, slot, had) yang sama
- **P4** nisbah > 0.669
- **E6a** (khusus E6): ada saringan `A1`–`A4` yang mengalahkan `A0` pada **KEDUA-DUA**
  CAGR dan MDD pada sel (B, slot, had) yang sama. Mengalahkan satu paksi sahaja **tidak**
  memadai — itu pertukaran, bukan penambahbaikan.

| T1 ∨ T3 | P3 | E6a | Keputusan |
|---|---|---|---|
| ya | ya | — | **BERHENTI–MENANG.** Bekukan, ujian hadapan ≥ 126 sesi. |
| ya | tidak | — | Beta bukan pemilihan; lapor sebagai `T4`-kelas, kemudian **BERHENTI–TUTUP**. |
| tidak | — | ya | Hierarki ialah lever sebenar tetapi tidak mencukupi. Rekod sebagai komponen terbaik untuk kerja hadapan, kemudian **BERHENTI–TUTUP**. |
| tidak | — | tidak | Tiada dapatan. **BERHENTI–TUTUP.** |

`BERHENTI–TUTUP` bermakna: kajian signal/pembinaan ditutup, terima `T4` (SPUS + tunai pada
berat pilihan pengguna), **tiada eksperimen ke-7 ditambah selepas melihat keputusan ini**.
Itu dipersetujui pengguna pada 31 Okt 2026 sebelum E1 dijalankan.

## 5. Jangkaan priori — ditulis sebelum larian

1. **T1 = 0 dan T3 = 0** — kali keenam. Hujah strukturnya kini ada lima pengesahan bebas.
2. **`A4` memberi MDD paling cetek antara kelima-lima saringan**, kerana ia satu-satunya
   yang menyasarkan volatiliti secara langsung.
3. **`E6a` GAGAL.** Setiap saringan ialah pertukaran: `A4` membeli MDD dengan CAGR,
   `A1`–`A3` membeli CAGR dengan calon. Saya jangka **tiada** saringan mengalahkan `A0`
   pada kedua-dua paksi serentak.
4. **`A3` (kuintil teratas RS) lebih teruk daripada `A2` (atas median)**, mengulangi
   mekanisme E4: menapis lebih ketat membuang calon yang pemeringkat perlukan. Dan
   `A2` ≈ `A0`, kerana membuang separuh terburuk daripada 500 jarang mengubah 8 teratas.
5. **`U02` kekal urutan terbaik**, seperti E4.

Jika jangkaan 3 salah — jika satu saringan berdiri memang mengalahkan `A0` pada kedua-dua
paksi — itu dapatan paling berguna dalam seluruh baris gilir, kerana ia satu-satunya cara
yang tinggal untuk menggerakkan paksi MDD tanpa memegang tunai.

## 6. Apa yang larian ini TIDAK boleh buktikan

- `AL04` membetulkan keahlian tetapi **bukan** delist; alam asas `a02` tiada saham delist.
- Ambang saringan (`ma200`, RS 50/80, median ATR%) dipilih tanpa penalaan, tetapi ia
  **dipilih oleh saya** daripada ruang yang sama yang menghasilkan keputusan terdahulu —
  keputusan kekal **bersyarat**.
- Hanya `U01` mempunyai jalur benih.
- `imbang` dikunci 63; `CARA` dikunci `C01`.
- Lima saringan ialah sampel kecil bagi ruang "saringan berdiri"; kegagalan di sini
  **tidak** membuktikan tiada saringan berdiri boleh berfungsi, hanya bahawa kelima-lima ini
  tidak.
