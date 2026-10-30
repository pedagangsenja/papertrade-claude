# Setup pilihan — peraturan penuh, nombor luar sampel

Dipilih daripada 672 setup yang diuji dalam `REVERSE/SETUP.md`. Nombor di bawah ialah **tingkap
TAHAN 2020–2025** — tempoh yang **tidak dilihat** ketika setup dipilih. Kos penuh sudah ditolak
(komisen 0.1% setiap sisi + slippage).

Pemilihan dibuat pada data 2012–2019 sahaja. Itu bermakna nombor 2020–2025 ialah prestasi
**luar sampel**, bukan backtest yang ditala.

---

## SETUP A — yang terbaik diukur

### Masuk — ketiga-tiga syarat pada hari yang sama

1. **MACD baru silang naik** — MACD(12,26) melintasi ke atas garis isyarat EMA(9) dalam
   **5 hari dagangan terakhir**, termasuk hari ini
2. **Stokastik %K(14) antara 20 dan 50** — `%K = (tutup − rendah terendah 14) ÷ (tinggi tertinggi 14 − rendah terendah 14) × 100`, **mentah, tanpa pelicinan**
3. **Volum hari ini ≥ 1.2 ×** purata volum **50 hari**

**Beli pada BUKA hari berikutnya.**

### Henti

`harga masuk − 2 × ATR14`, dikira pada hari masuk. ATR14 = Wilder.
Jika rendah menyentuh paras itu → **jual pada buka hari berikutnya**.

### Pegang dan keluar

Jika henti tidak tersentuh: **pegang 63 sesi dagangan** (kira-kira 3 bulan), kemudian jual pada
buka hari berikutnya.

### Prestasi luar sampel 2020–2025

| | |
|---|---|
| Dagangan | **29,074** |
| Kadar menang | **34.7%** |
| Untung purata bila menang | **+23.16%** |
| Rugi purata bila rugi | **−8.65%** |
| **Jangkaan setiap dagangan** | **+2.375%** |

---

## SETUP B — lebih kerap menyala

Sama, tetapi tukar syarat 2: **RSI(14) antara 40 dan 55** (ganti stokastik).

n 59,843 · menang 33.5% · untung +20.92% · rugi −8.18% · **jangkaan +1.557%**

## SETUP C — pengesahan lebih ketat

Sama seperti B, tetapi MACD silang dalam **3 hari** (bukan 5).

n 42,007 · menang 33.4% · untung +21.09% · rugi −8.27% · **jangkaan +1.538%**

---

## Tiga perkara yang menentukan sama ada ia berfungsi untuk anda

**1. Anda akan rugi 65% daripada masa.** Itu bukan kerosakan — itu reka bentuknya. Untung purata
+23% berbanding rugi purata −9% yang membayar. Jika anda tidak boleh menanggung 6 atau 7 kerugian
berturut-turut tanpa mengubah peraturan, setup ini akan merugikan anda walaupun nombornya positif.

**2. Tempoh pegang 63 sesi, bukan beberapa hari.** Keuntungan datang daripada memegang pemenang
selama ~3 bulan. Menjual awal kerana "sudah untung 5%" memusnahkan keseluruhannya — purata +23%
itu termasuk dagangan yang naik 60–80%.

**3. Henti 2×ATR, bukan peratusan tetap.** Untuk saham ATR 3%, itu −6%. Untuk saham ATR 6%, itu
−12%. Menggunakan −8% tetap untuk semua saham akan menghentikan saham meruap terlalu awal dan
saham tenang terlalu lewat.

## Satu kaveat, dinyatakan sekali

Membeli saham **secara rawak** pada tingkap yang sama memberi **+3.03%** setiap dagangan — lebih
tinggi daripada Setup A (`REVERSE/SETUP.md`). Jadi setup ini **positif tetapi tidak mengalahkan
tidak-menapis**, dan tiada satu pun daripada 672 setup melakukannya.

Maknanya: ini setup terbaik yang **diukur**, bukan setup yang **mengalahkan pasaran**. Jika
matlamat anda ialah pulangan maksimum, pegang indeks. Jika matlamat anda ialah **berdagang swing
dengan prosedur yang jelas dan nombor yang jujur**, inilah prosedurnya.

## Cara menjejakinya

Papertrade C sudah berjalan setiap malam. Untuk menguji setup ini ke hadapan tanpa wang:

1. Catat setiap kali ketiga-tiga syarat menyala pada saham dalam `papertrade/watchlist.csv`
2. Rekod harga buka hari berikutnya, paras henti, dan tarikh keluar 63 sesi
3. Selepas ~30 dagangan ditutup, bandingkan jangkaan sebenar dengan **+2.375%**

Kuasa statistik (`laporan/KAEDAH_TERBAIK.md`): untuk membezakan jangkaan 1 mata peratus,
anda perlu kira-kira **77 dagangan ditutup**. Di bawah itu, hasilnya hingar.
