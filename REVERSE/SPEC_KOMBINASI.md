# SPEC KOMBINASI — pradaftar, 30 Okt 2026

**Dikomit SEBELUM apa-apa keputusan dilihat.** Permintaan pengguna: kaji apa yang pedagang
sebenar guna di laman web dan forum, kemudian uji **gabungan mereka**, bukan indikator mentah.

## 1. Sumber

Carian web 30 Okt 2026. Dapatan pertama yang penting: **peraturan ini TIDAK diseragamkan**.
Setiap sumber memberi versi berbeza bagi "gabungan yang sama". Jadi setiap baris di bawah
dinamakan dengan sumbernya, dan saya menguji **peraturan sumber itu**, bukan tafsiran saya.

Sumber: skrip awam TradingView, forum babypips/globegain, panduan 5paisa, pocketful.in,
cloudzy, stockcharts, therighttrader, dev.to.

Konsensus yang paling kerap diulang: **trend (EMA 20/50) + momentum (RSI 14) + pengesahan
volum**, dengan MACD pilihan. Beberapa sumber menyatakan MACD **berlebihan** jika EMA 20/50
sudah diguna, kerana MACD hanyalah gambaran jarak antara dua EMA.

## 2. Indikator BAHARU yang perlu dikira

Tidak ada dalam 71 lajur sedia ada, jadi dikira khas untuk ujian ini:
`ma10` `ma20` `ma50` `ma200` `ema20` `ema50` `sma100` `rsi_sma14`
dan silang: `ma10×ma20`, `ma20×ma50`, `ma20×ma200`, `ema20×ema50`, `rsi14×rsi_sma14`.

**`ma10 × ma20` diminta khusus oleh pengguna** dan memang tiada sebelum ini.

## 3. Grid MASUK — 10 gabungan, dikunci

| Kod | Peraturan | Sumber |
|---|---|---|
| `K1` | `ema20 > ema50` **dan** `rsi14` 50–70 | skrip TradingView |
| `K2` | `ema20 > ema50` **dan** `rsi14 ≤ 30` **dan** `macd > 0` **dan** `vol_n50 ≥ 1.5` | skrip awam |
| `K3` | `tutup > ema20` **dan** `cerun_ma50 > 0` **dan** `rsi14` 40–60 | konsensus trend+momentum+volum |
| `K4` | `rsi14` 40–50 **dan** `tutup > ma50` | pendekatan pullback forum |
| `K5` | **`ma10` silang naik `ma20`** **dan** `vol_n50 ≥ 1.2` | permintaan pengguna |
| `K6` | `ma20` silang naik `ma50` | klasik |
| `K7` | `rsi14` silang naik `SMA14(rsi14)` | skrip sumber terbuka |
| `K8` | `tutup > ema20 > sma100` **dan** `vol_n50 ≥ 1.2` | 20EMA + 100SMA + volum |
| `K9` | `ma20` silang naik `ma200` | skrip MA-cross + ATR |
| `K10` | `K1` **dan** `vol_n50 ≥ 1.5` | K1 + pengesahan volum |

## 4. Grid KELUAR — 4 peraturan yang sumber tetapkan

| Kod | Peraturan |
|---|---|
| `X1` | henti **1.5 × ATR14**, sasaran **1 × ATR14** (sumber 20EMA+100SMA) |
| `X2` | henti **2 × ATR14**, sasaran **4 × ATR14** |
| `X3` | henti **2 × ATR14**, pegang **63 sesi** (asas kajian, untuk perbandingan) |
| `X4` | **ekori 2 × ATR14** daripada tutup tertinggi sejak masuk |

Semua: masuk pada **buka esok**, keluar pada **buka selepas syarat dipenuhi**, kos penuh
(`REVERSE/teras/kos.py`). Had imbasan 126 sesi bagi X1/X2/X4.

**10 × 4 = 40 kombinasi.** Grid ini **tidak akan dilebarkan**. Tiada parameter ditala; setiap
nilai diambil daripada sumbernya.

## 5. Pecahan latihan/tahan dan LIFT

- **LATIH 2012–2019**: kesemua 40 dinilai.
- **TAHAN 2020–2025**: kesemua 40 dinilai **juga**. Tiada pemilihan 10-teratas kali ini —
  grid cukup kecil (40) untuk dilaporkan penuh, jadi tiada bias pemilihan untuk dikawal.

**Lift dikira terhadap asas KELUAR YANG SAMA.** Itu pembetulan kepada kesilapan
`SPEC_SETUP.md` §4 saya: setiap peraturan keluar mempunyai kadar asas berbeza, jadi
membandingkan K1+X1 dengan asas X3 tidak sah. Asas = **beli SETIAP bar** dengan keluar itu.

## 6. Keputusan

Satu kombinasi **LULUS** hanya jika:

1. **Lift positif** atas asas keluar yang sama, pada **LATIH DAN TAHAN**
2. `n` ≥ 200 pada tahan
3. Jangkaan > 0 selepas membuang **5% pemenang teratas**

Jika tiada kombinasi lulus syarat 1: **DITOLAK**, dan sebab yang sama seperti `SETUP.md`
terpakai (menapis membuang peluang pada ekor).

## 7. Jangkaan priori (ditulis sebelum larian)

Saya jangka **lift negatif pada kesemua 40**, atas sebab yang sudah diukur: `SETUP.md`
mendapati 0 daripada 598 penapis mempunyai lift positif, dan gabungan ini ialah penapis juga.

**Tetapi dua perkara di sini BELUM diukur dan saya tidak boleh menolaknya:**
- `ma10 × ma20` dan `ma20 × ma50` tidak pernah dikira dalam repo ini
- Keluar `X1` (sasaran 1×ATR) dan `X2` (sasaran 4×ATR) tidak pernah diuji — kajian hanya
  pernah menguji henti + ufuk tetap + ekor, bukan **sasaran untung**

Sasaran untung ialah yang paling mungkin mengubah sesuatu, kerana `KOLAM_EKOR.md` menunjukkan
keluar membawa kesan lebih besar daripada mana-mana pemicu. Dan jangkaan priori saya sudah
salah **dua kali** dalam dua pradaftar terakhir.

## 8. Apa yang ujian ini TIDAK boleh buktikan

- Ia tidak boleh mencapai +10%/bulan (`SASARAN.md`).
- Sumber forum dan blog **tiada bukti bebas** tentang kelebihan; mereka cadangan, bukan hasil.
  Menguji mereka bermakna menguji cadangan itu, bukan mengesahkannya.
