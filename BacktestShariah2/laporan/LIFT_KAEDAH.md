# Lift MASUK setiap kaedah (gate G3)

Dijana 2026-11-26 19:39 UTC oleh `standard/lift_kaedah.py` (Actions `analisis.yml`). Pradaftar: `standard/SPEC_KAD_SKOR.md` pindaan 7 Nov 2026. Rekod analisis sahaja: tiada order, tiada wang sebenar.

## Apa yang diukur

Adakah kaedah ini memilih saham yang lebih baik daripada saham lain yang dibeli Lejar **pada hari yang sama dan tahap turun-naik (tercile ATR) yang sama**? Pulangan diukur pada ufuk TETAP 10 sesi (buka hari beli → tutup sesi ke-10, kos 0.2%), jadi peraturan keluar TIDAK mempengaruhi nombor ini. Nilai keluar diukur oleh G2 (buku harian) dan G6 (portfolio).

Versi lama (padanan baldi hari pegang, SE ikut hari beli) dibuang kerana ia meluluskan belian RAWAK: henti + sasaran rawak mendapat lift +2.17 mata, dan SE lama meluluskan plasebo sehingga 51% masa. Reka bentuk ini lulus plasebo pada kadar 1.9–3.4% (`laporan/PLASEBO_GATE.md`).

## Data

Hari beli LANGSUNG sahaja (Mxx sejak isyarat 2026-10-15, Nxx/GB sejak 2026-11-03). **38,794 saham-hari** dengan ufuk 10 sesi lengkap, 20 hari beli, 223 kaedah. Rejim (QQQ > SMA50 dan SMA10 > SMA20) pada hari beli ini: ON 1 · OFF 19.

## Keputusan

Diuji (≥ 30 saham-hari, ≥ 5 minggu): **99** kaedah. Lift positif lulus BH-FDR: **0**. Lift negatif lulus BH-FDR: **0**.

| Kaedah | Saham-hari | Hari beli | Minggu | Pulangan 10 sesi % | **Lift mata** | t | p | BH | Status |
|---|---|---|---|---|---|---|---|---|---|
| `M133` Bull Hook (Crabel) | 48 | 13 | 5 | +1.53 | **+3.73** | +2.22 | 0.0905 | tidak | BELUM CUKUP |
| `M146` 3-Bar Momentum Pattern | 77 | 18 | 5 | +1.19 | **+2.68** | +2.60 | 0.0598 | tidak | BELUM CUKUP |
| `M117` Landry Pullback (high 2 bulan) | 146 | 17 | 5 | -0.67 | **+2.06** | +2.38 | 0.0762 | tidak | BELUM CUKUP |
| `M93` Bollinger Kaedah II: %b + MFI | 266 | 20 | 5 | +0.69 | **+1.82** | +2.30 | 0.0831 | tidak | BELUM CUKUP |
| `M80` Radge Saluran Purata Bergerak  | 286 | 20 | 5 | +0.05 | **+1.70** | +2.18 | 0.0952 | tidak | BELUM CUKUP |
| `M18` EMA9/21 Pullback | 365 | 20 | 5 | -0.64 | **+1.61** | +1.65 | 0.1743 | tidak | BELUM CUKUP |
| `M150` Trend Bar Failure (Brooks) | 104 | 19 | 5 | +0.05 | **+1.60** | +2.26 | 0.0868 | tidak | BELUM CUKUP |
| `M15` Break & Retest + Henti ATR | 300 | 20 | 5 | +0.04 | **+1.58** | +1.25 | 0.2804 | tidak | BELUM CUKUP |
| `M158` Doubly Adaptive Profit Targets | 365 | 20 | 5 | +0.23 | **+1.44** | +2.20 | 0.0926 | tidak | BELUM CUKUP |
| `M118` Expansion Pivot (Cooper) | 85 | 20 | 5 | -1.62 | **+1.40** | +1.01 | 0.3681 | tidak | BELUM CUKUP |
| `M25` VWAP Wave (proksi harian) | 180 | 18 | 5 | -1.08 | **+1.19** | +1.75 | 0.1555 | tidak | BELUM CUKUP |
| `M127` Slingshot Bullish | 106 | 17 | 5 | -0.98 | **+1.09** | +0.88 | 0.4289 | tidak | BELUM CUKUP |
| `M107` Golden Cross SMA50/200 | 37 | 17 | 5 | -1.75 | **+1.04** | +0.86 | 0.4386 | tidak | BELUM CUKUP |
| `M119` 180 Bullish (Cooper) | 153 | 19 | 5 | -1.11 | **+0.98** | +1.42 | 0.2296 | tidak | BELUM CUKUP |
| `M137` Livermore System | 174 | 20 | 5 | -1.09 | **+0.94** | +1.22 | 0.2902 | tidak | BELUM CUKUP |
| `M100` Bulkowski Segi Empat & Segi Ti | 59 | 15 | 5 | +0.24 | **+0.92** | +0.58 | 0.5913 | tidak | BELUM CUKUP |
| `M77` Undercut & Rally pada Purata B | 54 | 17 | 5 | -2.13 | **+0.91** | +0.62 | 0.5688 | tidak | BELUM CUKUP |
| `M161` EMA 10/21 + Supertrend (10,3) | 471 | 20 | 5 | -0.76 | **+0.85** | +1.48 | 0.2124 | tidak | BELUM CUKUP |
| `M01` Bollinger Band + RSI | 112 | 20 | 5 | -2.48 | **+0.81** | +0.39 | 0.7187 | tidak | BELUM CUKUP |
| `M31` Band Walk (BB 20/2) | 397 | 20 | 5 | -0.51 | **+0.79** | +0.66 | 0.5481 | tidak | BELUM CUKUP |
| `M35` Pocket Pivot Morales & Kacher | 310 | 20 | 5 | -0.65 | **+0.77** | +1.29 | 0.2670 | tidak | BELUM CUKUP |
| `M08` SMA20 + SMA200 | 196 | 18 | 5 | -2.10 | **+0.72** | +0.82 | 0.4590 | tidak | BELUM CUKUP |
| `M153` Range Leader | 1289 | 20 | 5 | -1.97 | **+0.71** | +1.01 | 0.3680 | tidak | BELUM CUKUP |
| `M160` Measured Move Up | 112 | 18 | 5 | -2.22 | **+0.70** | +0.73 | 0.5054 | tidak | BELUM CUKUP |
| `M82` Arthur Hill Rotasi Sasaran 10% | 574 | 20 | 5 | -0.08 | **+0.68** | +1.52 | 0.2024 | tidak | BELUM CUKUP |

## Bila jadual ini boleh dipercayai

Hari beli diperlukan untuk melihat lift 2 mata merentas kaedah diuji: **120** (dikira semula setiap larian). Ada 20. Kad skor juga mewajibkan ≥ 10 hari beli dalam setiap rejim (G1), supaya keputusan tidak datang daripada satu fasa pasaran.

## Had

- Lift ialah kemahiran MASUK relatif kepada saham lain yang Lejar beli, bukan pulangan akaun.
- Kolam ialah alam Lejar (saham patuh Syariah ≥ USD10), bukan seluruh pasaran.
- Sasaran +10%/bulan tidak boleh dibaca daripada jadual ini (`REVERSE/SASARAN.md`).
