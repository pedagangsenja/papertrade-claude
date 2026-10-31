# PORTFOLIO_N — `GB02_atau3/4` sebagai portfolio, lawan SPUS

Pradaftar: `REVERSE/SPEC_PORTFOLIO_N.md` §3 (komit `5ad55ab`, sebelum larian).
Skrip: `REVERSE/step22_portfolio_n.py` · Data: `REVERSE/portfolio_n.csv`,
`REVERSE/portfolio_n_ringkas.csv`

3 masuk × 2 slot × 2 keluar × 3 urutan = **36 konfigurasi**; `U01` 20 benih → **264 larian**.
Alam A02 cair, kos penuh dua sisi, sauh HARIAN, saiz berat sama rata `1/slot`, tiada margin.
481,762 bar berisyarat; 391,348 calon layak merentas 3,752 sesi bagi `GB02_atau3`.

## Keputusan: 0 daripada 36 lulus keempat-empat gate

**SPUS 2020–2025: CAGR 17.95% · MDD −26.82% · nisbah 0.669**

| Gate | | |
|---|---|---|
| P1 | CAGR median > SPUS | **3/36** |
| P2 | MDD median ≥ SPUS | **6/36** |
| P3 | CAGR median > persentil-95 kawalan RAWAK | **15/36** (15 daripada 24 konfigurasi berisyarat) |
| P4 | CAGR ÷ \|MDD\| > 0.669 | **1/36** |
| | **lulus semua** | **0/36** |

### Baris yang penting

| masuk | slot | keluar | urutan | benih | CAGR | p5 – p95 | MDD | nisbah | dedah | P1 | P2 | P3 | P4 |
|---|---:|---|---|---:|---:|---|---:|---:|---:|:-:|:-:|:-:|:-:|
| GB02_atau4 | 40 | X15 | U02 | 1 | **29.28%** | – | −56.51% | 0.52 | 94% | ✓ | ✗ | ✓ | ✗ |
| GB02_atau3 | 40 | X15 | U02 | 1 | 25.89% | – | −55.82% | 0.46 | 95% | ✓ | ✗ | ✓ | ✗ |
| GB02_atau3 | 40 | X13 | U01 | 20 | 13.92% | 7.21 – 21.16 | −38.38% | 0.36 | 82% | ✗ | ✗ | ✓ | ✗ |
| GB02_atau3 | 8 | X13 | U01 | 20 | **9.40%** | 1.14 – 24.45 | −44.82% | 0.21 | 83% | ✗ | ✗ | ✗ | ✗ |
| *RAWAK* | 8 | X15 | U08 | 1 | 11.19% | – | **−12.14%** | **0.92** | 99% | ✗ | ✓ | ✗ | **✓** |

## Jawapan kepada soalan yang ditanya

**+8.541% setiap dagangan menjadi CAGR 9.40% pada 8 slot dan 13.92% pada 40 slot.
SPUS memberi 17.95%. MDD −44.8% dan −38.4% lawan SPUS −26.8%.**

Kelebihan setiap dagangan itu **nyata** — ia tidak hilang, dan ia bukan artifak. Ia cuma
tidak boleh dipindahkan kepada portfolio 8–40 slot.

## Mengapa: diukur, bukan ditafsir

Percanggahan antara "+8.541% setiap dagangan" dan "CAGR 9.40%" perlu dijelaskan sebelum
nombor itu boleh dipercayai. Saya merekod pulangan setiap dagangan yang **benar-benar
diambil** oleh portfolio dan membandingkannya dengan populasi penuh:

| | min | median | menang | pegang purata | tanpa 5% teratas |
|---|---:|---:|---:|---:|---:|
| Populasi penuh (195,681 dagangan) | +8.541% | – | 64.2% | – | +2.858% |
| Diambil, 8 slot (674 dagangan) | **+8.015%** | +7.271% | 67.1% | **84.9 bar** | **+1.558%** |
| Diambil, 40 slot (3,495 dagangan) | +7.483% | +5.587% | 63.5% | 81.5 bar | +1.140% |

**Tiada bias pemilihan.** Dagangan yang portfolio ambil memberi purata +8.0%, hampir sama
dengan populasi +8.5%. Enjin memilih sampel yang mewakili.

Jurangnya datang daripada dua perkara yang kedua-duanya boleh diukur:

1. **Tempoh pegang 84.9 bar (≈ 4 bulan).** Setiap slot hanya berpusing ~3 kali setahun,
   bukan 7. `+8%` setiap 4 bulan yang dikompaun tiga kali ialah ~26%/tahun sebelum apa-apa
   seretan — bukan 60%.
2. **Kelebihan itu hidup dalam ekor, dan ekor tidak boleh dikompaun.** Selepas membuang 5%
   dagangan terbaik yang DIAMBIL, purata jatuh kepada **+1.558%** setiap 4 bulan. 95%
   daripada apa yang portfolio pegang hampir rata; baki dibawa oleh beberapa posisi, dan
   satu posisi yang naik 300% dalam satu slot daripada lapan hanya menambah 1/8 daripadanya.

Inilah `KOLAM_EKOR.md` §1 diukur terus: purata aritmetik setiap dagangan **bukan** kadar
kompaun portfolio apabila taburan dipandu ekor.

## Tiga dapatan sampingan yang bernilai

### 1. Isyarat itu berfungsi — ia cuma tidak cukup

`P3` lulus **15 daripada 24** konfigurasi berisyarat: `GB02` mengalahkan **persentil ke-95**
kawalan rawak pada slot, keluar dan urutan yang sama. Itu ambang ketat — mengalahkan median
rawak boleh berlaku dengan nasib, mengalahkan cabutan rawak yang bertuah tidak. Jadi isyarat
itu menambah nilai yang boleh diukur.

Ia cuma menambah nilai daripada pangkalan yang terlalu rendah. `RAWAK` 40 slot `X13` `U01`
memberi 9.23%; `GB02_atau3` memberi 13.92%. Isyarat bernilai **+4.7 mata setahun** — dan
masih 4 mata di bawah SPUS.

### 2. URUTAN mengawal MDD, bukan bilangan slot

Jangkaan priori saya ialah 8 slot memberi MDD lebih dalam dan 40 slot membetulkannya.
**Salah.** Lima daripada enam konfigurasi yang lulus `P2` memakai `U08` (ATR% menaik —
beli yang paling kurang bergoyang dahulu), pada 8 slot *dan* 40 slot. Bilangan slot hampir
tidak mengubah MDD; **urutan** yang mengubahnya.

### 3. Satu-satunya konfigurasi yang melepasi garis campuran tiada isyarat langsung

Satu baris melepasi `P4`: **`RAWAK` · 8 slot · `X15` Chandelier · `U08`** — nisbah **0.92**
lawan garis campuran SPUS+tunai 0.669, dengan MDD **−12.14%** (SPUS −26.82%).

Masuk **rawak**. Tiada isyarat. Yang bekerja ialah urutan ATR rendah + henti mengekor.
CAGR 11.19% masih di bawah SPUS 17.95%, jadi ia gagal `P1` dan tidak boleh didakwa. Tetapi
ia satu-satunya perkara dalam seluruh kajian yang pernah berada **di atas** garis campuran,
dan ia tidak memerlukan satu pun daripada 147 peraturan masuk.

## Jangkaan priori lawan keputusan

| | Saya jangka | Berlaku | |
|---|---|---|---|
| P1 | gagal @8, mungkin lulus @40 | gagal @8; lulus @40 hanya dengan `X15`+`U02` (3/12) | separa betul |
| P2 | gagal @8, lulus @40 | ditentukan oleh **urutan**, bukan slot | **salah** |
| P3 | lulus | 15/24 | **betul** |
| P4 | gagal | 1/36, dan yang itu kawalan | **betul** |

Dua betul, satu separa, satu salah — lebih baik daripada corak tiga pradaftar sebelumnya
(salah pada 2 daripada 3 gate setiap kali). Corak kesilapan kali ini berbeza: saya
mengandaikan **pemusatan** (bilangan slot) memandu risiko, sedangkan **pemilihan dalam
pemusatan** (urutan) yang memandunya.

## Had

- **Bersyarat**: kolam 12 signal `GB02` dan keluar `X13`/`X15` dipilih daripada data yang
  sama. Tingkap bebas tidak wujud lagi.
- `U02` dan `U08` bersifat tentu (satu cabutan), jadi `P3` bagi baris itu ialah satu cabutan
  lawan satu cabutan — tiada jalur benih. Hanya `U01` mempunyai 20 benih, dan jalurnya lebar:
  1.14% – 24.45% pada 8 slot. Itu **23.3 mata peratus** merentas benih, mengesahkan semula
  hingar pemilihan 17.3 mata/tahun yang `KEPEKATAN_BENIH.md` ukur. Satu larian 5 benih yang
  saya jalankan sebagai diagnostik mendarat pada 14.40% — dalam jalur yang sama. **Sesiapa
  yang melaporkan satu cabutan di sini melaporkan hingar.**
- Alam A02 **tiada saham delist**: setiap CAGR di atas condong ke atas. `AL02` (alam SPUS
  sebenar) masih belum diuji.
- Saiz dikunci `SZ01` berat sama rata; `SZ03` risiko berskala tidak diuji di sini.
- `+10%/bulan` kekal tertutup secara aritmetik (`SASARAN.md`). Tiada dakwaan sedemikian
  dibuat.
