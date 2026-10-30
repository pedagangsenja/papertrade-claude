# Dua sistem lengkap lawan SPUS

Dijana 2026-10-30 06:30 UTC oleh `REVERSE/step16_sistem.py`. Pradaftar `REVERSE/SPEC_SISTEM.md` (dikomit sebelum larian ini).

## Keputusan: **DITOLAK**

Ini ujian pertama dalam kajian ini yang menguji **sistem lengkap** — masuk **dan** pegang **dan** keluar **dan** saiz **dan** rejim — bukan penapis masuk.

**SPUS 2020–2025:** CAGR **+17.95%** / MDD **-26.82%** · median tahunan +26.09% / MDD -10.14%.

| Sistem | CAGR median | p10 | p90 | MDD median | CAGR 14 thn | MDD 14 thn | Sebaran benih | Lulus |
|---|---|---|---|---|---|---|---|---|
| **B — momentum Clenow** | +6.38% | +6.38% | +6.38% | -11.59% | +3.88% | -21.56% | 0.00 mata | tidak |
| **A — pakej O'Neil/Minervini/Qullamaggie** | -1.03% | -4.83% | +5.90% | -40.65% | -1.96% | -48.91% | 4.01 mata | tidak |
| **SPUS** | **+17.95%** | — | — | **-26.82%** | — | — | — | — |

`S1` CAGR > SPUS · `S2` MDD lebih cetek · `S3` **p10** masih > SPUS · ditambah syarat konvensyen median tahunan. Spec §5 memerlukan **kesemuanya**.

| Sistem | S1 pulangan | S2 MDD | S3 p10 | Konvensyen median |
|---|---|---|---|---|
| `A_pakar` | tidak | tidak | tidak | tidak |
| `B_clenow` | tidak | ya | tidak | tidak |

## Sistem B deterministik — dan itu bermaklumat

Sebaran 20 benih bagi Sistem B ialah **0.000 mata**. Peringkat Clenow ialah skor berterusan, jadi seri praktiknya tiada dan benih tidak mengubah apa-apa.

Bandingkan Sistem A: sebaran **4.01 mata** daripada pemecah seri rawak antara calon yang layak.

Itu kelebihan struktur Clenow yang jarang disebut: ia **tiada hingar pemilihan**. `KEPEKATAN_BENIH.md` mengukur hingar itu sebagai 17.3 mata peratus setahun pada susunan sewenang-wenang. Sistem yang memeringkat ikut skor objektif tidak mempunyainya sama sekali — jadi keputusannya boleh dipercayai pada sampel yang jauh lebih kecil.

## Pendedahan menerangkan KEDUA-DUA nombor Sistem B

Sistem B memegang **18.7 daripada 20 slot** tetapi pendedahan pasarannya hanya **35.4% purata** (median 37.6%), dan ia di bawah 50% pada **89.9%** daripada hari.

Sebabnya saiz pariti risiko Clenow: `0.001 × ekuiti ÷ ATR%`. Dengan ATR peneraju momentum kira-kira 5–6%, setiap posisi hanya ~1.8% ekuiti, jadi 19 posisi memberi ~35% pendedahan. Itu **peraturan Clenow, bukan pepijat** — bukunya menegaskan kawalan risiko, bukan mengalahkan indeks dalam pasaran menaik.

Itu menjadikan perbandingan mentah **tidak adil pada kedua-dua arah**: SPUS melabur 100%, Sistem B melabur 35%. CAGR mentah **menghukum** Sistem B; MDD mentah **menyanjungnya**.

| Ukuran | Sistem B | SPUS |
|---|---|---|
| CAGR | +6.38% | +17.95% |
| MDD | -11.59% | -26.82% |
| CAGR / abs(MDD) | 0.551 | 0.669 |
| Pendedahan purata | 35.4% | 100% |
| **CAGR setiap unit pendedahan** | **18.01%** | **17.95%** |

Baris terakhir ialah dapatan sebenar: **18.0% lawan 17.9% setiap unit pendedahan pasaran** — praktiknya **sama**. Momentum Clenow tidak menambah pulangan; ia menambah **kawalan risiko**, dan ia membayar kawalan itu dengan pendedahan yang lebih rendah.

**Amaran yang mesti disertakan:** jangan tafsir ini sebagai "naikkan pendedahan 3× dan dapat 18%". Menaikkan pendedahan menaikkan drawdown secara berkadar; itu bukan alfa, itu beta. Dan menaikkannya melebihi 100% memerlukan margin, iaitu riba.

Pendedahan setiap tahun: `2012:47% 2013:41% 2014:39% 2015:38% 2016:35% 2017:42% 2018:34% 2019:37% 2020:27% 2021:30% 2022:14% 2023:39% 2024:38% 2025:35%`. Penapis rejim memang berfungsi — pendedahan paling rendah tepat pada tahun jatuh, dan itu sebab MDD-nya cetek.

## Ujian penguasaan: campuran SPUS + tunai pada pendedahan SAMA

Jika Sistem B memperoleh pulangan setiap unit pendedahan yang sama dengan SPUS, maka memegang SPUS pada **berat yang lebih rendah** sepatutnya memberi perkara yang sama tanpa mesin. Itu akibat logik yang mesti diuji, bukan diandaikan.

| Berat SPUS (baki tunai 0%) | CAGR | MDD | CAGR ÷ abs(MDD) |
|---|---|---|---|
| 100% | +17.95% | -26.82% | 0.669 |
| 60% | +10.87% | -16.62% | 0.654 |
| 40% | +7.27% | -11.25% | 0.646 |
| 35% ← pendedahan Sistem B | +6.44% | -10.00% | 0.644 |
| 30% | +5.46% | -8.50% | 0.642 |
| **Sistem B (Clenow)** | **+6.38%** | **-11.59%** | **0.551** |

Pada pendedahan yang **sama** (35.4%): SPUS memberi **+6.44% / -10.00%** lawan Clenow **+6.38% / -11.59%**. Pulangan lebih baik: **SPUS**. MDD lebih cetek: **SPUS**.

**Campuran SPUS + tunai MENGUASAI sistem Clenow pada kedua-dua paksi.** Itu kesimpulan terakhir seluruh kajian: selepas 134 kaedah, 672 setup, 20,640 ujian pemicu dan dua sistem pakar lengkap, tiada satu pun mengalahkan garis yang dilukis oleh satu ETF dan satu nisbah tunai.

Nisbah `CAGR ÷ abs(MDD)` campuran itu hampir **pemalar** merentas berat (0.64–0.67), jadi tiada titik "optimum" untuk dicari. Pilihan berat bukan soalan data — ia soalan **berapa banyak drawdown anda boleh tahan**.

## Tafsiran

**Tiada sistem lulus kesemua syarat.** Tetapi bacaan yang betul bukan "sistem pakar tidak berfungsi" — periksa syarat mana yang gagal bagi setiap satu, kerana gagal pada MDD sahaja bermakna perkara yang sangat berbeza daripada gagal pada pulangan.

- `A_pakar` gagal pada: pulangan (-1.03% lawan +17.95%), MDD (-40.65% lawan -26.82%)
- `B_clenow` gagal pada: pulangan (+6.38% lawan +17.95%)

### Jangkaan priori saya salah ke arah BERTENTANGAN

Spec §7 menyatakan: *"Sistem B menghampiri SPUS pada pulangan tetapi gagal syarat MDD."* Yang berlaku songsang:

- **MDD LULUS dengan lega**: -11.59% lawan SPUS -26.82% — lebih cetek **15.23 mata**, bukan lebih dalam.
- **Pulangan GAGAL dengan jauh**: +6.38% lawan +17.95% — jurang 11.57 mata.

Saya menjangka kemalangan momentum memperdalam drawdown. Sebaliknya penapis rejim + saiz pariti risiko menjadikannya sistem **berisiko rendah, pulangan rendah**. Bahagian pendedahan di atas menerangkan sebabnya, dan ia bukan tentang momentum sama sekali — ia tentang berapa banyak modal yang dilaburkan.

Itu kali **kedua** jangkaan priori saya salah dalam dua pradaftar terakhir (`SPEC_SILANG.md` §7 juga salah). Kedua-duanya pada ruang yang belum diukur. Saya catat itu sebagai pola, bukan kebetulan: ramalan saya tidak boleh dipercayai di tempat yang belum diukur, dan itu sebab pradaftar ada.

Sistem A gagal pada kedua-dua paksi (-1.03%, MDD -40.65%) walaupun ia mengandungi RS, sektor, rejim dan keluar aktif yang saya tinggalkan daripada 672 setup. Jadi menambah dua tiang itu **tidak** menyelamatkan pendekatan pecahan-dan-penapis. Sebaran benihnya 4.01 mata, jadi ia juga tertakluk hingar pemilihan yang Sistem B tiada sama sekali.

## Had

- Alam Release `autotune-data-a02`, **bukan** ditapis Syariah; SPUS ditapis. Tapisan Syariah membuang semua kewangan.
- Sistem A ialah **anggaran mekanikal** kaedah diskresi: pemilihan antara calon, saiz atas keyakinan, dan masa keluar manual tidak boleh dikodkan. Kegagalannya bukan bukti pakar itu salah (`laporan/KAEDAH_TERBAIK.md` §5).
- Sistem B: had saiz 20% ditambah untuk keselamatan berangka; ia bukan peraturan Clenow. Imbang Rabu; jika Rabu bukan hari dagangan, sesi itu dilangkau.
- Tunai tidak berbunga (0%), yang merugikan kedua-dua sistem.
- Tingkap keputusan 2020–2025 sahaja (6 tahun) kerana SPUS mula Dis 2019; ia merangkumi satu pasaran menaik yang kuat dan dua drawdown tajam.

**Ia tidak mencapai +10%/bulan.** Lihat `SASARAN.md`.
