# KELUAR_PORTFOLIO — `X31` / `X32`: keluar peringkat portfolio

Pradaftar: `REVERSE/SPEC_KELUAR_PORTFOLIO.md` (komit `773ce2f`, sebelum larian).
Skrip: `REVERSE/step27_keluar_portfolio.py` · Data: `REVERSE/keluar_portfolio.csv`,
`REVERSE/keluar_portfolio_ringkas.csv`

48 konfigurasi pada `AL02`, `U01` 20 benih → 276 larian.

## Keputusan: T1 **0**, T3 **0** → teruskan ke E5. Tetapi `E4a` **LULUS**.

| Gate | | |
|---|---|---|
| P1 | CAGR > 17.95% | **33 / 48** |
| P2 | MDD ≥ −26.82% | **0 / 48** |
| P3 | CAGR > p95 kawalan pangkat rawak | **16 / 48** |
| P4 | nisbah > 0.669 | **17 / 48** |
| **T1 / T3** | | **0 / 0** |
| **E4a** | keluar portfolio > keluar setiap posisi terbaik `AL02` (21.01%) | **LULUS: 47.44%** |

`P2` gagal pada setiap sel untuk kali **keempat berturut-turut** (E1, E2, E3, E4).

## BACA INI DAHULU: angka 47.44% itu sebahagian besarnya ARTIFAK

Sel terbaik ialah `RAWAK` masuk · `X32` · `U02` · 8 slot · imbang 63 →
**+47.44% / MDD −37.94%**, konsisten merentas 14 tahun (positif 13/14 tahun; latih
2012–2019 memberi +36.94%). Ia melepasi persentil-95 kawalan (28.96%) dengan jauh.

Angka itu terlalu kuat untuk dilaporkan tanpa cubaan memalsukannya. Tiga semakan dibuat
**sebelum** apa-apa dakwaan:

**(1) Pandang ke hadapan dalam skor?** Tidak. `rs_pst` ialah pangkat **keratan rentas dalam
tarikh** (`groupby('date').rank(pct=True)`), dan `rs_spy_6b` ialah
`_pct(c, c.shift(126)) − _pct(s, s.shift(126))` — pulangan 126 hari **ke belakang** tolak
SPY. Ujian asap juga mengesahkan skor tidak berubah apabila data masa depan didarab 3.7×.

**(2) Adakah ia bergantung pada alam?** Konfigurasi yang **sama**:

| alam | CAGR tahan | MDD | CAGR latih |
|---|---:|---:|---:|
| `AL02` SPUS 214 (**keahlian HARI INI**) | **+47.44%** | **−37.94%** | +36.94% |
| `AL01` a02 penuh 3,260 | +9.65% | **−91.50%** | +11.76% |

**(3) Ujian menentukan — alam titik-masa yang KAUSAL.** Keahlian SPUS diketahui hari ini,
bukan pada 2012. Ganti titik-masa yang boleh dikira secara kausal ialah `AL04`: **N teratas
ikut nilai dagangan 20 hari pada sauh itu sendiri**.

| alam titik-masa | CAGR tahan | MDD | CAGR latih |
|---|---:|---:|---:|
| 150 teratas nilai20 | +27.98% | −71.27% | +15.99% |
| **214 teratas** (saiz sama dengan SPUS) | **+34.78%** | **−68.80%** | +22.09% |
| 300 teratas | +38.64% | −74.51% | +9.70% |
| 500 teratas | +23.75% | −75.92% | +6.24% |
| 1000 teratas | +6.98% | −85.70% | +12.62% |

**Pulangan separa bertahan; risiko TIDAK.** Menapis kepada nama besar dan cair secara
titik-masa kemudian memeringkat ikut RS memang memberi CAGR tinggi (+34.78% pada saiz yang
sama), jadi kesan pulangan itu **nyata dan kausal**. Tetapi MDD jatuh daripada −37.94%
kepada **−68.80%** — **30.9 mata** daripada kelebihan risiko `AL02` hilang apabila
keahlian dijadikan kausal.

Mekanismenya jelas: ahli SPUS hari ini ialah syarikat yang **tidak meletup**. Tapisan
kecairan titik-masa masih mengandungi nama yang kemudiannya runtuh.

**Akibat yang melangkaui E4:** setiap nombor `AL02` dalam kajian ini membawa pandang ke
hadapan keahlian yang **menyanjung paksi risiko**. E2 melaporkan MDD `AL02` 6.19 mata lebih
cetek daripada `AL01` dan saya kaitkannya dengan kualiti alam; diagnostik ini menunjukkan
mekanismenya sebahagian besarnya **survivorship**. Laporan E2 dan E3 mesti dibaca dengan
pembetulan itu.

## Dapatan yang BERTAHAN: isyarat masuk MEROSAKKAN putaran berpangkat

| masuk | CAGR terbaik | lulus P3? |
|---|---:|---|
| `RAWAK` (tiada isyarat, seluruh alam diperingkat) | **+47.44%** | ya (47.44 > 28.96) |
| `GB02_atau3` (isyarat) | +24.04% | **tidak** (24.04 < 25.52) |

Masuk bersignal **lebih teruk daripada tiada masuk langsung**, dan ia tidak mengalahkan
kawalan pangkat-rawaknya sendiri. Sebabnya struktur, bukan kebetulan: `AL02` membekalkan
**7.7 isyarat/sesi**, jadi menapis dahulu mengehadkan kolam pemeringkat kepada segelintir
nama dan menghalangnya memilih yang benar-benar teratas.

Ini `SETUP.md` muncul semula pada paksi baharu — **menapis membuang calon, dan pemeringkat
memerlukan calon.** Ia juga menjelaskan mengapa `E4a` lulus hanya melalui lorong tanpa
isyarat.

Dapatan ini **tidak** terjejas oleh bias keahlian, kerana kedua-dua lorong berkongsi alam
yang sama.

## Keluar portfolio memang mengalahkan keluar setiap posisi — pada alam yang sama

`E4a` lulus: **47.44%** lawan **21.01%** (terbaik E2 pada alam yang sama, `X15` tiada had).
Walaupun selepas pembetulan titik-masa, lorong kausal terbaik memberi **+34.78%** — masih
jauh di atas 21.01%.

Jadi jangkaan priori saya #3 (`E4a` gagal, "putaran menambah kos tanpa menambah kemahiran")
**salah**. Pada saham — tidak seperti pada 11 bakul sektor di E3 — kolam pemeringkat cukup
besar untuk pemeringkatan menambah nilai sebenar.

`X31` (metrik dikunci pulangan 252 hari) dan `X32` + `U14` memberi beza median **1.59 mata**
CAGR pada sel sepadan, mengesahkan §2: dibaca sebagaimana ditulis, `X31` memang kes khas
`X32`.

## Pendedahan TIDAK runtuh

Jangkaan priori #2 salah, dan ujian asap sudah menunjukkannya sebelum gate dinilai:
pendedahan **99.1%–100%** pada setiap sel. Putaran mengekalkan pegangan walaupun isyarat
berhenti mencetus, kerana kolam pangkat ialah (pegangan ∪ calon) — berbeza daripada had
pegangan E2 yang memindahkan modal ke tunai.

## Jangkaan priori lawan keputusan

| | Saya jangka | Berlaku | |
|---|---|---|---|
| (1) T1 = 0 dan T3 = 0 | ya | ya | **betul** |
| (2) pendedahan runtuh < 70% | ya | **99.1–100%** | **salah** |
| (3) `E4a` gagal | gagal | **lulus, 47.44% lawan 21.01%** | **salah** |
| (4) `P3` lulus minoriti sel | < 50% | 16/48 = 33% | betul (tetapi `U02` menang, bukan `U14` seperti saya ramal) |
| (5) `X31` ≈ `X32`/`U14`, beza < 3 mata | ya | median 1.59 mata | **betul** |

Tiga betul, dua salah. Yang salah ialah yang paling penting: putaran berpangkat **memang**
lebih baik daripada keluar setiap posisi, dan saya meramal sebaliknya berdasarkan E3 — di
mana kolamnya 11 instrumen, bukan 214.

## Had

- **Setiap nombor `AL02` menyanjung MDD** melalui pandang ke hadapan keahlian; diukur
  **30.9 mata** pada konfigurasi terbaik. Lorong kausal terbaik memberi MDD **−68.80%**,
  iaitu gagal `P2` dengan 42 mata.
- Alam asas tiada saham delist pada **kedua-dua** `AL01` dan `AL02`, jadi tiada alam dalam
  kajian ini bersih. `AL04` titik-masa membetulkan keahlian tetapi **bukan** delist.
- `U02`, `U14` dan `X31` adalah satu cabutan tentu; hanya `U01` mempunyai jalur benih.
- `imbang` 21 dan 63 ialah dua titik sahaja.
- Paksi `CARA` kekal `C01`.
- `AL04` dijalankan sebagai **diagnostik pemalsuan**, bukan sebagai sel grid dipradaftar;
  tiada gate dinilai padanya dan tiada dakwaan dibuat daripadanya selain menolak tafsiran
  `AL02`.
