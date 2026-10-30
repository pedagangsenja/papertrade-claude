# Katalog kombinasi daripada pakar dan komuniti

Dikumpul 30 Okt 2026 daripada carian web, atas permintaan pengguna: **kumpul dahulu seberapa
banyak, uji kemudian.**

**Dapatan pertama yang mesti dinyatakan:** peraturan ini **TIDAK diseragamkan**. Hampir setiap
"strategi" terkenal mempunyai 3–5 versi dengan ambang berbeza, dan sumber tidak bersetuju antara
satu lain. Jadi setiap baris di bawah menyimpan **versi sumbernya sendiri**, bukan satu versi
"betul". Jika dua sumber memberi ambang berbeza, kedua-duanya disenaraikan sebagai baris berasingan.

Lajur **Status**:
- `DIUJI` — sudah diuji dalam `REVERSE/KOMBINASI.md`
- `SEDIA` — semua indikator sudah ada, boleh diuji terus
- `PERLU <x>` — memerlukan indikator baharu dikira

---

## A. Purata bergerak

| # | Peraturan | Sumber | Status |
|---|---|---|---|
| A1 | `MA10` silang naik `MA20` + `vol ≥ 1.2×` | permintaan pengguna | **DIUJI** — lift +0.123/+0.392, terbaik daripada 40 |
| A2 | `MA20` silang naik `MA50` | klasik | DIUJI |
| A3 | `MA20` silang naik `MA200` | skrip TradingView MA+ATR | DIUJI |
| A4 | `EMA20 > EMA50` + `RSI 50–70` | skrip TradingView | DIUJI |
| A5 | `tutup > EMA20 > SMA100` + `vol ≥ 1.2×` | babypips (20EMA+100SMA) | DIUJI |
| A6 | `MA50` silang naik `MA200` (golden cross) | klasik | SEDIA (`hari_gc`) |
| A7 | Tiga MA tersusun: `MA10 > MA20 > MA50`, masuk bila susunan terbentuk | triple-MA klasik | SEDIA |
| A8 | `tutup > EMA20`, dan **langkau** jika `tutup` > 1.5×ATR dari `EMA20` | babypips (elak terlalu jauh) | SEDIA |

## B. RSI

| # | Peraturan | Sumber | Status |
|---|---|---|---|
| B1 | `RSI14` silang naik `SMA14(RSI14)` | skrip sumber terbuka | DIUJI |
| B2 | `RSI14` 40–50 + `tutup > MA50` (pullback) | forum | DIUJI |
| B3 | `RSI14` 40–60 + `tutup > EMA20` + `MA50` naik | konsensus blog | DIUJI |
| B4 | **Connors RSI(2) < 5** + `tutup > SMA200`; keluar `tutup > SMA5` **atau** `tutup < SMA200` | Connors, variasi 200-hari | **PERLU `ma5`** |
| B5 | **Connors RSI(2) < 10** + `tutup > SMA200`; keluar `RSI2 > 65` | MQL5 EA | SEDIA (`rsi2`) |
| B6 | `RSI14 ≤ 30` + `EMA20 > EMA50` + `MACD > 0` + `vol ≥ 1.5×` | skrip awam | DIUJI |

## C. Bollinger + RSI

| # | Peraturan | Sumber | Status |
|---|---|---|---|
| C1 | `tutup` **bawah** jalur bawah BB(20,2) + `RSI14 < 30`; keluar `RSI14 > 70` | LuxAlgo | SEDIA (`bb_pctb < 0`) |
| C2 | `tutup` kembali **masuk** jalur + `RSI14` silang naik 30; henti pada ekstrem luar, keluar **jalur tengah** | therighttrader (varian swing harian) | SEDIA |
| C3 | BB + `RSI14` ambang **40/60**, sasaran untung **2%** | Fmz | SEDIA |
| C4 | BB pecah + RSI lepas ambang; keluar **jalur tengah** | StockSharp | SEDIA |
| C5 | BB + RSI; keluar bila `RSI14` silang naik **50** | skrip TradingView | SEDIA |

## D. Trend / sistem

| # | Peraturan | Sumber | Status |
|---|---|---|---|
| D1 | `Supertrend(10, 3)` menaik + `ADX14 > 20` | therighttrader | SEDIA |
| D2 | `Supertrend` menaik + `tutup > EMA` + `ADX14 > 23` | skrip TradingView | SEDIA |
| D3 | Tiga Supertrend positif + `tutup > EMA` + `ADX14 >` ambang | LuxAlgo triple-Supertrend | **PERLU 3 Supertrend** |
| D4 | `Ichimoku`: `tutup` atas awan + `tenkan` atas `kijun` | klasik | SEDIA (`atas_awan`, `tenkan_atas`) |

## E. Pecahan / kotak

| # | Peraturan | Sumber | Status |
|---|---|---|---|
| E1 | **Turtle**: pecah `Donchian20`; henti `2 × ATR20`; keluar `Donchian10` bertentangan | Dennis/Eckhardt, didokumen | **PERLU `donchian10` keluar** |
| E2 | Pecah `Donchian50` (kotak Darvas ringkas) | MQL5 Darvas EA | **PERLU `donchian50`** |
| E3 | Pecah `Donchian` + penapis `EMA200`; henti pada jalur bertentangan | skrip TradingView | SEDIA (`donchian20` + `j_ma200`) |
| E4 | **Darvas Box**: pecah tinggi terdahulu, undur hampir paras itu, henti bawah kotak | Darvas, tiada peraturan berangka standard | **PERLU kotak Darvas** |
| E5 | `Donchian55` pecah | Turtle sistem 2 | SEDIA |

---

## Peraturan KELUAR yang dikumpul (ini bahagian yang paling kurang diperhatikan)

| # | Keluar | Sumber | Status |
|---|---|---|---|
| X1 | henti `1.5 × ATR`, sasaran `1 × ATR` | babypips | **DIUJI — asas jadi −0.281%** |
| X2 | henti `2 × ATR`, sasaran `4 × ATR` | pelbagai | DIUJI — asas +0.953% |
| X3 | henti `2 × ATR`, pegang 63 sesi | asas kajian | DIUJI — asas **+2.595%** (terbaik) |
| X4 | ekori `2 × ATR` | pelbagai | DIUJI — asas +1.156% |
| X5 | keluar pada **jalur tengah BB** | therighttrader, StockSharp | SEDIA |
| X6 | keluar bila `tutup < SMA5` | Connors | **PERLU `ma5`** |
| X7 | keluar bila `RSI2 > 65` atau `> 90` | MQL5, Fmz | SEDIA |
| X8 | sasaran untung **2%** tetap | Fmz | SEDIA |
| X9 | keluar `Donchian10` bertentangan | Turtle | **PERLU `donchian10`** |
| X10 | henti pada **ekstrem luar jalur BB** | therighttrader | SEDIA |

---

## Ringkasan apa yang perlu dikira baharu

`ma5` · `donchian10` · `donchian50` · tiga Supertrend (ATR berbeza) · kotak Darvas ·
jalur BB atas/bawah/tengah eksplisit (sekarang hanya `bb_pctb`)

## Jumlah

**30 peraturan masuk** (10 sudah diuji, 14 sedia, 6 perlu indikator baharu) ×
**10 peraturan keluar** (4 sudah diuji, 4 sedia, 2 perlu indikator baharu).

Grid penuh = 300 kombinasi. Itu terlalu besar untuk satu pradaftar tanpa kawalan pemilihan yang
ketat — `SETUP.md` menunjukkan menguji 672 menghasilkan pemenang latih walaupun tiada kelebihan.
Jadi larian seterusnya mesti mengekalkan pecahan **LATIH 2012–2019 / TAHAN 2020–2025** dan
melaporkan **lift terhadap asas keluar yang sama**, seperti `KOMBINASI.md`.

## Nota kejujuran tentang sumber

Tiada satu pun sumber ini memberi **bukti bebas** tentang kelebihan. Mereka cadangan dan kod, bukan
hasil yang disahkan. Satu backtest yang dijumpai (Connors RSI2 pada Nasdaq 100, Okt 2016–Okt 2026)
melaporkan **+26.9% jumlah lawan +528.3% beli-dan-pegang**, CAGR +2.4% lawan +20.2% — iaitu
strategi itu **jauh kalah** kepada memegang indeks pada ujian itu.

Menguji katalog ini bermakna menguji **cadangan**, bukan mengesahkan dakwaan yang sudah terbukti.
