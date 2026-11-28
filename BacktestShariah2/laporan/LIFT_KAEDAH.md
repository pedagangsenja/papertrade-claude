# Lift MASUK setiap kaedah (gate G3)

Dijana 2026-11-28 11:41 UTC oleh `standard/lift_kaedah.py` (Actions `analisis.yml`). Pradaftar: `standard/SPEC_KAD_SKOR.md` pindaan 7 Nov 2026. Rekod analisis sahaja: tiada order, tiada wang sebenar.

## Apa yang diukur

Adakah kaedah ini memilih saham yang lebih baik daripada saham lain yang dibeli Lejar **pada hari yang sama dan tahap turun-naik (tercile ATR) yang sama**? Pulangan diukur pada ufuk TETAP 10 sesi (buka hari beli → tutup sesi ke-10, kos 0.2%), jadi peraturan keluar TIDAK mempengaruhi nombor ini. Nilai keluar diukur oleh G2 (buku harian) dan G6 (portfolio).

Versi lama (padanan baldi hari pegang, SE ikut hari beli) dibuang kerana ia meluluskan belian RAWAK: henti + sasaran rawak mendapat lift +2.17 mata, dan SE lama meluluskan plasebo sehingga 51% masa. Reka bentuk ini lulus plasebo pada kadar 1.9–3.4% (`laporan/PLASEBO_GATE.md`).

## Data

Hari beli LANGSUNG sahaja (Mxx sejak isyarat 2026-10-15, Nxx/GB sejak 2026-11-03). **40,209 saham-hari** dengan ufuk 10 sesi lengkap, 21 hari beli, 226 kaedah. Rejim (QQQ > SMA50 dan SMA10 > SMA20) pada hari beli ini: ON 1 · OFF 20.

## Keputusan

Diuji (≥ 30 saham-hari, ≥ 5 minggu): **99** kaedah. Lift positif lulus BH-FDR: **0**. Lift negatif lulus BH-FDR: **0**.

| Kaedah | Saham-hari | Hari beli | Minggu | Pulangan 10 sesi % | **Lift mata** | t | p | BH | Status |
|---|---|---|---|---|---|---|---|---|---|
| `M133` Bull Hook (Crabel) | 51 | 14 | 5 | +1.17 | **+3.57** | +2.08 | 0.1061 | tidak | BELUM CUKUP |
| `M146` 3-Bar Momentum Pattern | 77 | 18 | 5 | +1.19 | **+2.68** | +2.60 | 0.0598 | tidak | BELUM CUKUP |
| `M117` Landry Pullback (high 2 bulan) | 147 | 18 | 5 | -0.66 | **+2.07** | +2.40 | 0.0743 | tidak | BELUM CUKUP |
| `M93` Bollinger Kaedah II: %b + MFI | 267 | 21 | 5 | +0.71 | **+1.85** | +2.30 | 0.0833 | tidak | BELUM CUKUP |
| `M80` Radge Saluran Purata Bergerak  | 288 | 21 | 5 | -0.01 | **+1.67** | +2.10 | 0.1033 | tidak | BELUM CUKUP |
| `M18` EMA9/21 Pullback | 376 | 21 | 5 | -0.69 | **+1.62** | +1.72 | 0.1597 | tidak | BELUM CUKUP |
| `M150` Trend Bar Failure (Brooks) | 104 | 19 | 5 | +0.05 | **+1.60** | +2.26 | 0.0865 | tidak | BELUM CUKUP |
| `M15` Break & Retest + Henti ATR | 304 | 21 | 5 | +0.00 | **+1.56** | +1.22 | 0.2888 | tidak | BELUM CUKUP |
| `M158` Doubly Adaptive Profit Targets | 375 | 21 | 5 | +0.22 | **+1.47** | +2.30 | 0.0832 | tidak | BELUM CUKUP |
| `M118` Expansion Pivot (Cooper) | 85 | 20 | 5 | -1.62 | **+1.40** | +1.01 | 0.3680 | tidak | BELUM CUKUP |
| `M25` VWAP Wave (proksi harian) | 183 | 19 | 5 | -1.07 | **+1.21** | +1.80 | 0.1463 | tidak | BELUM CUKUP |
| `M127` Slingshot Bullish | 107 | 18 | 5 | -1.01 | **+1.06** | +0.88 | 0.4290 | tidak | BELUM CUKUP |
| `M119` 180 Bullish (Cooper) | 153 | 19 | 5 | -1.11 | **+0.98** | +1.42 | 0.2293 | tidak | BELUM CUKUP |
| `M107` Golden Cross SMA50/200 | 39 | 18 | 5 | -1.78 | **+0.98** | +0.85 | 0.4434 | tidak | BELUM CUKUP |
| `M137` Livermore System | 175 | 21 | 5 | -1.10 | **+0.94** | +1.22 | 0.2890 | tidak | BELUM CUKUP |
| `M100` Bulkowski Segi Empat & Segi Ti | 59 | 15 | 5 | +0.24 | **+0.92** | +0.58 | 0.5909 | tidak | BELUM CUKUP |
| `M77` Undercut & Rally pada Purata B | 54 | 17 | 5 | -2.13 | **+0.91** | +0.62 | 0.5688 | tidak | BELUM CUKUP |
| `M161` EMA 10/21 + Supertrend (10,3) | 473 | 21 | 5 | -0.76 | **+0.85** | +1.50 | 0.2086 | tidak | BELUM CUKUP |
| `M01` Bollinger Band + RSI | 112 | 20 | 5 | -2.48 | **+0.81** | +0.39 | 0.7188 | tidak | BELUM CUKUP |
| `M31` Band Walk (BB 20/2) | 399 | 21 | 5 | -0.53 | **+0.79** | +0.66 | 0.5430 | tidak | BELUM CUKUP |
| `M32` Momentum Burst | 57 | 14 | 5 | -1.29 | **+0.79** | +0.37 | 0.7284 | tidak | BELUM CUKUP |
| `M08` SMA20 + SMA200 | 201 | 19 | 5 | -2.07 | **+0.77** | +0.90 | 0.4198 | tidak | BELUM CUKUP |
| `M35` Pocket Pivot Morales & Kacher | 311 | 21 | 5 | -0.69 | **+0.73** | +1.23 | 0.2857 | tidak | BELUM CUKUP |
| `M160` Measured Move Up | 113 | 19 | 5 | -2.17 | **+0.73** | +0.76 | 0.4873 | tidak | BELUM CUKUP |
| `M145` Yum-Yum Continuation | 308 | 21 | 5 | -1.14 | **+0.65** | +0.99 | 0.3777 | tidak | BELUM CUKUP |

## Bila jadual ini boleh dipercayai

Hari beli diperlukan untuk melihat lift 2 mata merentas kaedah diuji: **118** (dikira semula setiap larian). Ada 21. Kad skor juga mewajibkan ≥ 10 hari beli dalam setiap rejim (G1), supaya keputusan tidak datang daripada satu fasa pasaran.

## Had

- Lift ialah kemahiran MASUK relatif kepada saham lain yang Lejar beli, bukan pulangan akaun.
- Kolam ialah alam Lejar (saham patuh Syariah ≥ USD10), bukan seluruh pasaran.
- Sasaran +10%/bulan tidak boleh dibaca daripada jadual ini (`REVERSE/SASARAN.md`).
