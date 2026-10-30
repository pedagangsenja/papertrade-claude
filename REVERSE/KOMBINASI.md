# Gabungan daripada laman web dan forum: diuji

Dijana 2026-10-30 09:10 UTC oleh `REVERSE/step17_kombinasi.py`. Pradaftar `REVERSE/SPEC_KOMBINASI.md`.

## Keputusan: **DITOLAK**

10 gabungan yang pedagang sebenar guna × 4 peraturan keluar yang **sumber itu sendiri tetapkan** = 40 kombinasi. Dua daripada keluar itu mempunyai **sasaran untung**, yang kajian ini belum pernah uji.

### Asas: beli SETIAP bar, ikut peraturan keluar

| Keluar | Peraturan | Jangkaan latih | Jangkaan tahan | Menang tahan |
|---|---|---|---|---|
| `X1` | henti 1.5×ATR, sasaran 1×ATR | -0.319% | -0.281% | 61.1% |
| `X2` | henti 2×ATR, sasaran 4×ATR | +0.481% | +0.953% | 37.7% |
| `X3` | henti 2×ATR, 63 sesi | +1.204% | +2.595% | 30.2% |
| `X4` | ekori 2×ATR | +0.525% | +1.156% | 35.4% |

**Setiap peraturan keluar mempunyai kadar asas yang berbeza**, jadi lift mesti dikira terhadap asas keluar yang SAMA. Itu pembetulan kepada kesilapan `SPEC_SETUP.md` §4 saya.

## 40 kombinasi — lift atas asas keluar yang sama

| Masuk | Keluar | n tahan | Menang | Jangkaan tahan | **Lift latih** | **Lift tahan** | Lulus |
|---|---|---|---|---|---|---|---|
| K5 ma10 silang ma20 & vol>=1.2 | `X3` | 28,117 | 30.0% | +2.988% | +0.123 | **+0.392** | tidak |
| K9 ma20 silang ma200 | `X3` | 19,146 | 29.9% | +2.804% | -0.342 | **+0.209** | tidak |
| K5 ma10 silang ma20 & vol>=1.2 | `X2` | 28,117 | 38.4% | +1.123% | +0.076 | **+0.170** | tidak |
| K7 rsi14 silang SMA14(rsi) | `X1` | 378,548 | 61.2% | -0.275% | +0.016 | **+0.006** | tidak |
| K10 K1 & vol>=1.5 | `X3` | 142,341 | 29.3% | +2.562% | -0.003 | **-0.033** | tidak |
| K5 ma10 silang ma20 & vol>=1.2 | `X1` | 28,117 | 61.0% | -0.320% | -0.091 | **-0.039** | tidak |
| K5 ma10 silang ma20 & vol>=1.2 | `X4` | 28,117 | 36.1% | +1.105% | +0.076 | **-0.052** | tidak |
| K6 ma20 silang ma50 | `X1` | 48,876 | 61.2% | -0.343% | -0.027 | **-0.062** | tidak |
| K4 rsi 40-50 & tutup>ma50 | `X1` | 256,251 | 61.1% | -0.345% | -0.024 | **-0.064** | tidak |
| K7 rsi14 silang SMA14(rsi) | `X2` | 378,548 | 37.6% | +0.882% | -0.010 | **-0.072** | tidak |
| K3 tutup>ema20 & ma50 naik & rsi 40-60 | `X1` | 714,569 | 60.9% | -0.361% | -0.080 | **-0.080** | tidak |
| K1 ema20>ema50 & rsi 50-70 | `X1` | 1,471,488 | 60.4% | -0.392% | -0.087 | **-0.111** | tidak |
| K9 ma20 silang ma200 | `X1` | 19,146 | 60.7% | -0.400% | -0.071 | **-0.119** | tidak |
| K4 rsi 40-50 & tutup>ma50 | `X2` | 256,251 | 38.1% | +0.821% | -0.139 | **-0.132** | tidak |
| K10 K1 & vol>=1.5 | `X1` | 142,341 | 60.3% | -0.437% | -0.137 | **-0.155** | tidak |
| K8 tutup>ema20>sma100 & vol>=1.2 | `X1` | 341,620 | 60.2% | -0.448% | -0.123 | **-0.167** | tidak |
| K6 ma20 silang ma50 | `X2` | 48,876 | 37.6% | +0.782% | -0.053 | **-0.172** | tidak |
| K7 rsi14 silang SMA14(rsi) | `X3` | 378,548 | 30.0% | +2.377% | -0.002 | **-0.218** | tidak |
| K10 K1 & vol>=1.5 | `X2` | 142,341 | 37.7% | +0.721% | -0.155 | **-0.232** | tidak |
| K7 rsi14 silang SMA14(rsi) | `X4` | 378,548 | 35.1% | +0.906% | +0.011 | **-0.250** | tidak |
| K9 ma20 silang ma200 | `X2` | 19,146 | 37.4% | +0.696% | -0.310 | **-0.257** | tidak |
| K4 rsi 40-50 & tutup>ma50 | `X4` | 256,251 | 35.7% | +0.817% | -0.078 | **-0.339** | tidak |
| K10 K1 & vol>=1.5 | `X4` | 142,341 | 35.4% | +0.812% | -0.057 | **-0.344** | tidak |
| K3 tutup>ema20 & ma50 naik & rsi 40-60 | `X2` | 714,569 | 37.3% | +0.573% | -0.225 | **-0.381** | tidak |
| K6 ma20 silang ma50 | `X4` | 48,876 | 35.8% | +0.764% | -0.069 | **-0.392** | tidak |
| K9 ma20 silang ma200 | `X4` | 19,146 | 35.0% | +0.746% | -0.349 | **-0.410** | tidak |
| K8 tutup>ema20>sma100 & vol>=1.2 | `X2` | 341,620 | 36.8% | +0.492% | -0.219 | **-0.462** | tidak |
| K6 ma20 silang ma50 | `X3` | 48,876 | 29.6% | +2.132% | -0.080 | **-0.463** | tidak |
| K8 tutup>ema20>sma100 & vol>=1.2 | `X3` | 341,620 | 28.0% | +2.129% | -0.068 | **-0.467** | tidak |
| K1 ema20>ema50 & rsi 50-70 | `X2` | 1,471,488 | 36.9% | +0.481% | -0.305 | **-0.472** | tidak |
| K4 rsi 40-50 & tutup>ma50 | `X3` | 256,251 | 30.1% | +2.100% | -0.183 | **-0.495** | tidak |
| K3 tutup>ema20 & ma50 naik & rsi 40-60 | `X4` | 714,569 | 35.0% | +0.553% | -0.166 | **-0.604** | tidak |
| K8 tutup>ema20>sma100 & vol>=1.2 | `X4` | 341,620 | 34.4% | +0.514% | -0.243 | **-0.643** | tidak |
| K1 ema20>ema50 & rsi 50-70 | `X3` | 1,471,488 | 28.7% | +1.950% | -0.320 | **-0.645** | tidak |
| K3 tutup>ema20 & ma50 naik & rsi 40-60 | `X3` | 714,569 | 29.1% | +1.923% | -0.254 | **-0.673** | tidak |
| K1 ema20>ema50 & rsi 50-70 | `X4` | 1,471,488 | 34.5% | +0.459% | -0.296 | **-0.698** | tidak |
| K2 ema20>ema50 & rsi<=30 & macd>0 & vol>=1.5 | `X1` | 338 | 53.0% | -1.491% | -0.307 | **-1.210** | tidak |
| K2 ema20>ema50 & rsi<=30 & macd>0 & vol>=1.5 | `X2` | 338 | 32.0% | -0.972% | -0.246 | **-1.926** | tidak |
| K2 ema20>ema50 & rsi<=30 & macd>0 & vol>=1.5 | `X4` | 338 | 31.4% | -2.077% | -0.988 | **-3.233** | tidak |
| K2 ema20>ema50 & rsi<=30 & macd>0 & vol>=1.5 | `X3` | 338 | 27.5% | -1.826% | -1.491 | **-4.422** | tidak |

Lift POSITIF: **5 daripada 40** pada latih, **4 daripada 40** pada tahan, **0** pada kedua-duanya + syarat n dan ekor.

## Tafsiran

**Tiada kombinasi lulus ketiga-tiga syarat.** Tetapi melaporkannya begitu sahaja akan menyembunyikan dapatan positif PERTAMA dalam seluruh kajian ini.

### 3 kombinasi mempunyai lift POSITIF pada KEDUA-DUA tingkap

| Masuk | Keluar | n tahan | Lift latih | Lift tahan | Tanpa 5% teratas |
|---|---|---|---|---|---|
| K5 ma10 silang ma20 & vol>=1.2 | `X3` | 28,117 | +0.123 | **+0.392** | -2.369% |
| K5 ma10 silang ma20 & vol>=1.2 | `X2` | 28,117 | +0.076 | **+0.170** | -0.950% |
| K7 rsi14 silang SMA14(rsi) | `X1` | 378,548 | +0.016 | **+0.006** | -0.862% |

Itu **3 daripada 40**. `SETUP.md` mendapati **0 daripada 598** penapis mempunyai lift positif, jadi ini perkara baharu — walaupun kecil.

**`K5` (MA10 silang MA20 + volum ≥ 1.2×) memegang 2 daripada 3 slot itu** — dengan DUA peraturan keluar berbeza. Lift positif pada dua tingkap dan dua keluar bukan satu cabutan; itu pola.

Gabungan itu **diminta khusus oleh pengguna** dan memang tidak pernah ada dalam 71 lajur indikator repo ini. Permintaan itu betul.

**Mengapa ia masih gagal:** syarat 3 memerlukan jangkaan > 0 selepas membuang 5% pemenang teratas. Kesemuanya negatif di sana — dan begitu juga asas. Jadi kelebihan itu nyata tetapi ia hidup **sepenuhnya dalam ekor kanan**, sama seperti segala-galanya dalam kajian ini.

Maknanya: ia bukan kelebihan yang boleh ditangkap dengan 8–10 slot. Ia kelebihan yang memerlukan banyak posisi untuk direalisasikan.


## Kesan SASARAN UNTUNG (yang belum pernah diuji)

| Keluar | Jangkaan asas tahan | Beza dari `X3` (tiada sasaran) |
|---|---|---|
| `X3` henti 2×ATR, 63 sesi | +2.595% | +0.000 |
| `X1` henti 1.5×ATR, sasaran 1×ATR | -0.281% | -2.877 |
| `X2` henti 2×ATR, sasaran 4×ATR | +0.953% | -1.642 |
| `X4` ekori 2×ATR | +1.156% | -1.439 |

Keluar terburuk: `X1` (henti 1.5×ATR, sasaran 1×ATR). Keluar terbaik: `X3`.

**Kedua-dua sasaran untung merugikan.** Sasaran 1×ATR dan 4×ATR kedua-duanya memberi jangkaan LEBIH RENDAH daripada tiada sasaran. Itu dapatan `KOLAM_EKOR.md` lagi: memotong pemenang pada paras tetap membuang ekor kanan, dan ekor kanan itulah yang membayar.

Ini menjawab soalan yang sumber forum tidak pernah uji: **mengambil untung pada 1×ATR atau 4×ATR adalah lebih buruk daripada tidak mengambil untung sama sekali.**

## Perangkap kadar menang — premis 70/30 diukur

Inilah jawapan terbaik kepada andaian "70% menang, 30% rugi ditampung henti" — daripada data anda sendiri, bukan hujah:

| Keluar | Kadar menang | Untung purata | Rugi purata | **Jangkaan** |
|---|---|---|---|---|
| `X1` sasaran 1×ATR | **61.1%** | +4.11% | -7.18% | **-0.281%** |
| `X3` tiada sasaran | 30.2% | +29.11% | -8.88% | **+2.595%** |

Ambil untung pada 1×ATR dan kadar menang anda naik ke **61.1%** — hampir tepat angka yang anda sebut. Dan jangkaannya menjadi **-0.281%**, iaitu **RUGI**.

Tanpa sasaran, kadar menang jatuh ke 30.2% — kalah 7 daripada 10 kali — dan jangkaannya **+2.595%**, iaitu **UNTUNG**.

Sebabnya satu baris: untung purata naik daripada +4.11% kepada +29.11% apabila sasaran dibuang. Sasaran memotong pemenang; henti tidak memotong apa-apa yang bernilai.

**Sistem yang menang 61% masa boleh merugikan anda. Sistem yang menang 30% masa boleh menguntungkan anda.** Kadar menang bukan maklumat.

## Had

- Sumber forum dan blog **tiada bukti bebas** tentang kelebihan. Menguji mereka bermakna menguji cadangan, bukan mengesahkan dakwaan yang sudah disahkan.
- Peraturan sumber **tidak diseragamkan**; versi yang diuji dinyatakan penuh dalam `SPEC_KOMBINASI.md` §3 dan §4.
- Lift positif ≠ mengalahkan SPUS. Ia hanya bermakna mengalahkan "beli setiap bar dengan keluar yang sama".
- Alam `autotune-data-a02`, bukan ditapis Syariah.
