# Pradaftar E3 — INSTRUMEN `IS02`: putaran bakul sektor

Ditulis dan dikomit **sebelum** sebarang keputusan dilihat. Skrip: `REVERSE/step26_instrumen.py`.
Keluaran: `REVERSE/INSTRUMEN.md`, `REVERSE/instrumen.csv`, `REVERSE/instrumen_ringkas.csv`.
Baris gilir: `REVERSE/STRATEGI.md` §4 E3, dijalankan pada **`AL02`** (keputusan pengguna
31 Okt 2026 selepas E2).

## 1. Soalan, dan mengapa ia prior positif terkuat dalam registry

`SETUP.md` mengukur **598 daripada 598** setup saham gagal syarat ekor — setiap satu negatif
selepas membuang 5% dagangan teratas. Dalam larian yang sama, **SPY +3.356%** dan
**QQQ +4.419%** melepasinya dengan mudah (menang ~77% lawan ~31%), kerana **indeks ITULAH
kepelbagaian merentas ekor**.

E2 mengesahkan mekanisme itu dari arah lain: pada alam a02 yang luas, 5% dagangan teratas
membawa **101.67%** jumlah pulangan (95% yang lain negatif bersih); pada alam SPUS yang
sempit, **47.92%**, dan `tanpa5` menjadi **+2.682%** — positif buat kali pertama dalam
kajian.

`IS02` ialah **titik tengah** antara satu saham dan satu indeks penuh, dan ia tidak pernah
diuji.

## 2. Instrumen: bakul sektor sintetik, bukan ETF SPDR — dan sebabnya

**Setiap hos data pasaran langsung disekat dalam sesi ini**, disahkan sebelum reka bentuk:
`stooq.com` (proksi menolak CONNECT), `query1/query2.finance.yahoo.com`, `financialmodelingprep.com`
dan `www.alphavantage.co` kesemuanya memberi kod `000`. `yfinance` tidak dipasang. Jadi
XLK/XLF/XLE sebenar **tidak boleh** diperoleh.

Gantinya: **bakul sektor sintetik berat sama rata**, dibina daripada harga yang sudah ada di
cakera. Peta ticker→sektor datang daripada `data/skrin/tv_us.csv` (liputan **215/215**
ticker SPUS).

Ini bukan sekadar ganti — bagi hipotesis §1 ia **lebih bersih**, dan itu mesti dinyatakan
sebagai pilihan reka bentuk, bukan alasan:

- Universe, harga, kalendar dan model kos **sama** seperti E1/E2, jadi perbezaan tidak boleh
  datang daripada vendor data lain.
- Berat sama rata mengasingkan **kepelbagaian** daripada pemberat-permodalan ETF sebenar.
- Tiada yuran pengurusan, tiada ralat penjejakan.

**Had yang datang bersamanya, dinyatakan sekarang:** ia **bukan** XLK/XLF. Ia tiada nisbah
perbelanjaan, tiada ralat penjejakan, dan ia mengimbang mengikut binaan. Ia juga mewarisi
bias keahlian SPUS **semasa** daripada E2. Kesimpulan "bakul sektor berfungsi" **tidak**
bermakna "beli XLK".

**Bakul**: 11 sektor dengan ≥ 7 ahli SPUS, **192 ticker**:
Electronic Technology (34) · Health Technology (33) · Technology Services (28) ·
Producer Manufacturing (25) · Consumer Non-Durables (15) · Retail Trade (14) ·
Process Industries (11) · Transportation (11) · Distribution Services (7) ·
Non-Energy Minerals (7) · Industrial Services (7).

Liputan bar disemak sebelum grid: 169/192 pada 2012, 176 pada 2016, 184 pada 2020, 191 pada
2025, dan **tiada** sektor pernah jatuh di bawah 5 ahli berbar pada tahun yang disemak.

**Pembinaan**: aras bakul ialah indeks pulangan berat sama rata yang diimbang **harian** —
`aras_t = aras_{t-1} × (1 + purata pulangan tutup-ke-tutup ahli berbar)`, dan aras buka
sepadan `buka_t = aras_{t-1} × (1 + purata(buka_t / tutup_{t-1} − 1))`, supaya pelaksanaan
"beli pada buka" kekal seperti seluruh kajian. Nilai dagangan bakul = **jumlah** nilai
dagangan 20 hari ahli, jadi `kos_sisi` memberi slippage jaluran tertinggi.

## 3. Mekanik BERBEZA daripada E1/E2 — diisytihar, bukan disembunyikan

Sistem ini memutar **11 instrumen** dengan **imbang berkala**, bukan memilih daripada ribuan
saham dengan peraturan keluar setiap posisi. Maka `step26` **tidak** boleh memakai
`step24.simulasi`, dan **kawalan regresi E1/E2 tidak terpakai**. Gantinya ia membawa
kawalannya **sendiri** (§5): pegang-semua dan pilihan rawak, pada enjin yang sama.

`PB.cagr`, `PB.mdd`, `PB.penanda_aras` dan `teras.kos` diguna semula tanpa perubahan.

## 4. Grid

- **URUTAN** (4): `U11` pulangan gabungan 1+3+6 bulan · `U14` momentum 12−1 bulan ·
  `U03` cerun regresi Clenow 90 hari · **`RAWAK`** (kawalan, 20 benih)
- **k** (5): 1, 2, 3, 5, **11** — `k = 11` ialah **pegang semua**, iaitu ujian kepelbagaian
  tulen tanpa pemilihan, dan ia juga `SZ10` pada paksi instrumen
- **IMBANG** (2): 21 sesi (`IB04` bulanan) · 63 sesi (suku)

4 × 5 × 2 = 40 konfigurasi; `RAWAK` 20 benih → **3 × 5 × 2 + 20 × 5 × 2 = 230 larian**.
(`k = 11` adalah sama bagi setiap urutan kerana tiada pemilihan berlaku; ia dilaporkan sekali
sebagai `PEGANG_SEMUA` dan tidak dikira berulang dalam gate.)

Dikunci: alam `AL02`, cara `C01` (beli pada buka berikutnya), saiz `SZ01` berat sama rata
`1/k`, kos penuh dua sisi, tiada margin, tiada leverage. Tingkap keputusan **2020–2025**;
latih 2012–2019 direkod.

## 5. Gate dan **setiap** gabungan keputusan

Pembetulan proses daripada E2: setiap gabungan disenaraikan, bukan hanya dua.

- **P1** CAGR > 17.95% · **P2** MDD ≥ −26.82% · **T1** = P1 ∧ P2
- **T3** CAGR ≥ 15% ∧ MDD ≥ −15%
- **P3** CAGR > persentil-95 kawalan `RAWAK` pada `k` dan imbang yang **sama**
- **P4** nisbah `CAGR ÷ |MDD|` > 0.669

| (T1 ∨ T3) | P3 | Keputusan |
|---|---|---|
| ya | ya | **BERHENTI–MENANG.** Pemilihan sektor berfungsi. Bekukan, ujian hadapan ≥ 126 sesi. |
| ya | tidak | **Kepelbagaian, bukan pemilihan.** Jika sel itu `k = 11` (pegang semua), ia `T4` dalam samaran dan mesti dilaporkan begitu. **Bukan** BERHENTI–MENANG; baris gilir **diteruskan** ke E4, dan hasilnya direkod sebagai calon lorong instrumen. |
| tidak | ya | Isyarat sektor menambah nilai tetapi tidak mencukupi. **Teruskan ke E4**; catat lift atas kawalan. |
| tidak | tidak | **Teruskan ke E4.** Tiada dapatan. |

`P4` dilapor sebagai **BERHENTI–SEPARA** (lorong risiko-rendah) seperti `STRATEGI.md` §3;
ia tidak pernah menghentikan baris gilir.

## 6. Diagnostik yang direkod (bukan gate)

- **Bahagian ekor bakul**: 5% dagangan teratas sebagai % jumlah pulangan, dan `tanpa5` —
  definisi yang **sama** seperti E2, supaya ia boleh dibanding terus dengan 101.67% / −0.081%
  (`AL01` saham) dan 47.92% / +2.682% (`AL02` saham). **Ini ujian langsung bagi hipotesis
  `SETUP.md`.**
- CAGR/MDD setiap bakul secara individu (beli-dan-pegang), supaya "putaran" boleh dibanding
  dengan "pegang satu sektor sahaja".
- Pusing ganti, seretan kos setahun, pendedahan, jalur benih `RAWAK` p5–p95.

## 7. Jangkaan priori — ditulis sebelum larian

Rekod saya: majoriti jangkaan salah dalam **enam** pradaftar berturut-turut, dan pada E2
kedua-dua jangkaan yang saya paling yakin salah ke arah **bertentangan**. Jangkaan ini
dicatat supaya kesilapan boleh dikira, bukan kerana ia patut dipercayai.

1. **`tanpa5` bakul adalah POSITIF dan jauh lebih tinggi daripada saham** — ini jangkaan
   paling kuat saya, dan ia mekanisme `SETUP.md` diuji terus. Saya jangka **> +1%**.
2. **`k = 11` (pegang semua) mengalahkan `k = 1` dan `k = 2`** pada MDD, dan hampir sama
   pada CAGR. Kepelbagaian membeli risiko, bukan pulangan.
3. **P3 gagal pada majoriti sel** — pemilihan sektor ikut momentum tidak mengalahkan
   pemilihan rawak daripada 11 bakul, kerana 11 ialah sampel terlalu kecil untuk momentum
   memisahkan.
4. **T1 gagal pada setiap sel.** MDD bakul sektor dalam 2020 dan 2022 akan menghampiri MDD
   SPUS kerana kesemuanya ekuiti AS panjang sahaja.
5. **T3 gagal pada setiap sel** — syarat MDD ≥ −15% terlalu ketat untuk portfolio ekuiti
   100% tanpa tunai.

## 8. Apa yang larian ini TIDAK boleh buktikan

- Bakul sintetik **bukan** ETF boleh dagang. Tiada yuran, tiada ralat penjejakan, dan ia
  mengimbang harian mengikut binaan — ETF sebenar tidak.
- Keahlian SPUS **semasa** ditolak ke belakang (warisan E2). Bias memihak kepada sistem.
- Tiada saham delist dalam alam asas.
- 11 bakul ialah sampel kecil: jalur benih kawalan `RAWAK` akan lebar, dan `P3` pada `k`
  besar hampir tidak bermakna (pada `k = 11` tiada pemilihan langsung, jadi `P3` tidak
  dinilai di sana).
- Tempoh 2020–2025 mengandungi satu rejim teknologi yang dominan; bakul Electronic
  Technology dan Technology Services berkongsi pemacu yang sama, jadi "11 sektor" **bukan**
  11 taruhan bebas.
