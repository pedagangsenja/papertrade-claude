# INSTRUMEN — `IS02`: putaran bakul sektor

Pradaftar: `REVERSE/SPEC_INSTRUMEN.md` (komit `38ba8d2`, sebelum larian).
Skrip: `REVERSE/step26_instrumen.py` · Data: `REVERSE/instrumen.csv`,
`REVERSE/instrumen_ringkas.csv`, `REVERSE/instrumen_bakul.csv`

11 bakul sektor sintetik berat sama rata daripada alam `AL02` (SPUS, 192 ticker),
4 urutan × 5 `k` × 2 imbang = 40 konfigurasi, `RAWAK` 20 benih → 230 larian.

## Keputusan: T1 **0**, T3 **0** → teruskan ke E4

| Gate | | |
|---|---|---|
| P1 | CAGR > 17.95% | **26 / 40** |
| P2 | MDD ≥ −26.82% | **0 / 40** |
| P3 | CAGR > persentil-95 kawalan `RAWAK` | **5 / 40** |
| P4 | nisbah > 0.669 | **1 / 40** |
| **T1** | P1 ∧ P2 | **0** |
| **T3** | CAGR ≥ 15% ∧ MDD ≥ −15% | **0** |

**MDD gagal pada setiap sel tanpa kecuali.** Yang paling cetek daripada 40 ialah
**−31.61%**, lawan SPUS **−26.82%**. Ini kali **ketiga berturut-turut** (E1, E2, E3) paksi
pulangan lulus secara meluas dan paksi risiko gagal sepenuhnya, dan ketiga-tiganya pada
mekanik yang berbeza. Coraknya bukan kebetulan: portfolio ekuiti panjang-sahaja 100%
melabur tidak boleh mempunyai MDD lebih cetek daripada indeks ekuiti melainkan ia memegang
tunai, dan memegang tunai ialah `T4`.

## Hipotesis `SETUP.md` DISAHKAN — kepelbagaian memang membetulkan masalah ekor

Ini sebab E3 dijalankan, dan ia keluar seperti yang dipradaftar.

| populasi | 5% teratas = % jumlah pulangan | purata **tanpa** 5% teratas |
|---|---:|---:|
| Saham, alam a02 luas (E2) | **101.67%** | **−0.081%** |
| Saham, alam SPUS sempit (E2) | 47.92% | +2.682% |
| **Bakul sektor** (`U14`, k=3) | **38.69%** | **+4.77%** |
| **Bakul sektor** (`U14`, k=1) | 41.37% | +4.25% |
| Bakul sektor (`U03`, k=3) | 30.84% | +2.44% |
| Bakul sektor (`RAWAK`, k=1) | 46.95% | +0.75% |

`tanpa5` adalah **positif pada kesemua lapan** sel bakul yang diukur, dan **+4.77%** ialah
nilai tertinggi yang pernah diukur dalam kajian ini. `SETUP.md` mendapati **0 daripada 598**
setup saham positif selepas membuang 5% teratas; bakul sektor positif pada 8 daripada 8.

**Mekanisme itu nyata: kepelbagaian merentas ekor menukar kelebihan yang rapuh dan
bergantung-ekor menjadi kelebihan yang teragih.** Itu dapatan yang kekal, bebas daripada
kegagalan gate.

Ia **tidak** mencukupi untuk mengalahkan SPUS, kerana masalahnya berpindah: bukan lagi ekor,
tetapi **drawdown**.

## Hanya SATU urutan berfungsi, dan ia bukan yang repo guna

| urutan | lulus P3 |
|---|---|
| `U14` momentum 12−1 bulan | **5 / 8** |
| `U11` pulangan gabungan 1+3+6 bulan | 0 / 8 |
| `U03` cerun regresi Clenow 90 hari | 0 / 8 |

| urutan | k | imbang | CAGR | p95 kawalan | MDD | nisbah |
|---|---:|---:|---:|---:|---:|---:|
| `U14` | 1 | 21 | **+27.55%** | 24.78 | −36.81% | **0.75** |
| `U14` | 2 | 21 | +24.72% | 22.93 | −37.57% | 0.66 |
| `U14` | 1 | 63 | +23.68% | 20.53 | −38.57% | 0.61 |
| `U14` | 3 | 21 | +22.91% | 21.12 | −35.79% | 0.64 |
| `U14` | 5 | 21 | +21.76% | 19.12 | −34.96% | 0.62 |

`U14` (momentum 12−1 klasik) ialah **satu-satunya** sel yang melepasi `P4`
(nisbah 0.75 > 0.669) — itu **BERHENTI–SEPARA** mengikut `STRATEGI.md` §3: lorong
risiko-rendah dilaporkan, baris gilir diteruskan.

`U03` Clenow gagal di sini walaupun `SISTEM.md` mendapati ia mempunyai sebaran benih 0.00
pada saham. Kelebihan "skor berterusan tiada hingar pemilihan" tidak bermakna skor itu
**betul** pada 11 instrumen.

## Diagnostik yang membatalkan dakwaan "putaran sektor berfungsi"

Beli-dan-pegang **satu** bakul sahaja, 2020–2025:

| bakul | CAGR | MDD | | bakul | CAGR | MDD |
|---|---:|---:|---|---|---:|---:|
| Electronic Technology | **+32.67%** | −37.68% | | Technology Services | +18.87% | −33.45% |
| Non-Energy Minerals | +25.91% | −45.42% | | Transportation | +14.45% | −31.79% |
| Distribution Services | +24.78% | −35.68% | | Process Industries | +11.77% | −37.52% |
| Industrial Services | +24.19% | −50.36% | | Health Technology | +11.31% | −26.55% |
| Producer Manufacturing | +20.44% | −38.57% | | Consumer Non-Durables | +7.38% | −30.16% |
| Retail Trade | +19.00% | −40.01% | | | | |

**Memegang Electronic Technology sahaja memberi +32.67%, mengalahkan setiap konfigurasi
putaran** termasuk `U14` k=1 (+27.55%). Jadi putaran momentum **tidak** menangkap pemenang
dengan boleh dipercayai — ia mengambil kos dan ketinggalan.

Dan satu bakul itu ialah pilihan **selepas melihat keputusan**: pada 2020 tiada siapa tahu
teknologi akan menang. Jalur kawalan rawak `k=1` ialah **p5 7.69% – p95 24.78% = 17.1 mata**
— memilih satu bakul ialah lontaran duit syiling yang lebar.

Pegang-semua (`k = 11`) memberi **+19.66% / −35.54%** dengan **11 dagangan** dan seretan kos
**0.06%/tahun**. Itu `SZ10` pada paksi instrumen: ia mengalahkan CAGR SPUS tetapi
MDD-nya 8.7 mata lebih dalam.

## Jangkaan priori lawan keputusan

| | Saya jangka | Berlaku | |
|---|---|---|---|
| (1) `tanpa5` bakul positif, > +1% | ya | positif **8/8**, > +1% pada **6/8** | **betul** |
| (2) `k=11` kalahkan `k=1`/`k=2` pada MDD, CAGR hampir sama | ya | MDD ya (−35.54 lawan −36.81/−37.57); CAGR **tidak** (19.66 lawan 27.55) | separa |
| (3) P3 gagal pada majoriti sel | ya | 35/40 gagal | **betul** |
| (4) T1 gagal setiap sel; MDD menghampiri SPUS | ya | T1 = 0; MDD **lebih dalam** daripada SPUS pada setiap sel | **betul** |
| (5) T3 gagal setiap sel | ya | T3 = 0 | **betul** |

**Empat betul, satu separa — pradaftar PERTAMA di mana majoriti jangkaan saya betul.**
Sebabnya boleh dibaca: E3 menguji mekanisme yang `SETUP.md` **sudah** ukur, bukan ruang yang
belum diukur. Dalam lima pradaftar sebelum ini saya meramal ruang belum diukur dan salah
setiap kali. Itu menyokong kesimpulan `NXX.md`: jangkaan priori saya hanya berguna apabila
ia ekstrapolasi daripada ukuran sedia ada.

## Had

- Bakul sintetik **bukan** ETF boleh dagang: tiada yuran pengurusan, tiada ralat penjejakan,
  dan ia mengimbang harian mengikut binaan. **"Bakul sektor berfungsi" tidak bermakna
  "beli XLK".**
- Keahlian SPUS **semasa** ditolak ke belakang (warisan E2); alam asas tiada saham delist.
- 11 bakul ialah sampel kecil. Jalur kawalan `k=1` ialah 17.1 mata; `U14` k=1 (+27.55%)
  berada 2.77 mata di atas p95 kawalan, jadi ia lulus `P3` tetapi bukan dengan margin besar.
- Electronic Technology dan Technology Services berkongsi pemacu yang sama; "11 sektor"
  **bukan** 11 taruhan bebas, dan 2020–2025 ialah satu rejim teknologi dominan.
- `U14`, `U11`, `U03` adalah tentu (satu cabutan, nb = 1); hanya `RAWAK` mempunyai jalur.
