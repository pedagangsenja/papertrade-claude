# Lift MASUK setiap kaedah (gate G3)

Dijana 2026-11-21 11:23 UTC oleh `standard/lift_kaedah.py` (Actions `analisis.yml`). Pradaftar: `standard/SPEC_KAD_SKOR.md` pindaan 7 Nov 2026. Rekod analisis sahaja: tiada order, tiada wang sebenar.

## Apa yang diukur

Adakah kaedah ini memilih saham yang lebih baik daripada saham lain yang dibeli Lejar **pada hari yang sama dan tahap turun-naik (tercile ATR) yang sama**? Pulangan diukur pada ufuk TETAP 10 sesi (buka hari beli → tutup sesi ke-10, kos 0.2%), jadi peraturan keluar TIDAK mempengaruhi nombor ini. Nilai keluar diukur oleh G2 (buku harian) dan G6 (portfolio).

Versi lama (padanan baldi hari pegang, SE ikut hari beli) dibuang kerana ia meluluskan belian RAWAK: henti + sasaran rawak mendapat lift +2.17 mata, dan SE lama meluluskan plasebo sehingga 51% masa. Reka bentuk ini lulus plasebo pada kadar 1.9–3.4% (`laporan/PLASEBO_GATE.md`).

## Data

Hari beli LANGSUNG sahaja (Mxx sejak isyarat 2026-10-15, Nxx/GB sejak 2026-11-03). **30,488 saham-hari** dengan ufuk 10 sesi lengkap, 17 hari beli, 223 kaedah. Rejim (QQQ > SMA50 dan SMA10 > SMA20) pada hari beli ini: ON 1 · OFF 16.

## Keputusan

Diuji (≥ 30 saham-hari, ≥ 5 minggu): **83** kaedah. Lift positif lulus BH-FDR: **0**. Lift negatif lulus BH-FDR: **0**.

| Kaedah | Saham-hari | Hari beli | Minggu | Pulangan 10 sesi % | **Lift mata** | t | p | BH | Status |
|---|---|---|---|---|---|---|---|---|---|
| `M133` Bull Hook (Crabel) | 47 | 12 | 5 | +1.92 | **+3.91** | +2.65 | 0.0572 | tidak | BELUM CUKUP |
| `M15` Break & Retest + Henti ATR | 265 | 17 | 5 | +0.98 | **+2.08** | +2.26 | 0.0866 | tidak | BELUM CUKUP |
| `M150` Trend Bar Failure (Brooks) | 82 | 16 | 5 | +1.05 | **+1.86** | +2.15 | 0.0979 | tidak | BELUM CUKUP |
| `M80` Radge Saluran Purata Bergerak  | 251 | 17 | 5 | +0.64 | **+1.82** | +2.27 | 0.0855 | tidak | BELUM CUKUP |
| `M18` EMA9/21 Pullback | 314 | 17 | 5 | -0.11 | **+1.71** | +1.57 | 0.1904 | tidak | BELUM CUKUP |
| `M158` Doubly Adaptive Profit Targets | 337 | 17 | 5 | +0.61 | **+1.49** | +2.07 | 0.1077 | tidak | BELUM CUKUP |
| `M93` Bollinger Kaedah II: %b + MFI | 247 | 17 | 5 | +0.63 | **+1.47** | +2.00 | 0.1157 | tidak | BELUM CUKUP |
| `M10` EMA3 + CCI + MACD | 102 | 17 | 5 | -0.34 | **+1.36** | +1.30 | 0.2640 | tidak | BELUM CUKUP |
| `M137` Livermore System | 151 | 17 | 5 | -0.33 | **+1.16** | +1.65 | 0.1738 | tidak | BELUM CUKUP |
| `M25` VWAP Wave (proksi harian) | 169 | 16 | 5 | -0.96 | **+1.13** | +1.58 | 0.1902 | tidak | BELUM CUKUP |
| `M145` Yum-Yum Continuation | 279 | 17 | 5 | -0.41 | **+1.00** | +1.74 | 0.1572 | tidak | BELUM CUKUP |
| `M33` Supertrend + SMA10 | 203 | 17 | 5 | -0.73 | **+0.92** | +0.49 | 0.6469 | tidak | BELUM CUKUP |
| `M01` Bollinger Band + RSI | 107 | 17 | 5 | -2.25 | **+0.84** | +0.39 | 0.7188 | tidak | BELUM CUKUP |
| `M23` Breitstein Kapitulasi + Kesina | 111 | 17 | 5 | -1.87 | **+0.83** | +0.76 | 0.4905 | tidak | BELUM CUKUP |
| `M161` EMA 10/21 + Supertrend (10,3) | 421 | 17 | 5 | -0.54 | **+0.72** | +1.37 | 0.2417 | tidak | BELUM CUKUP |
| `M118` Expansion Pivot (Cooper) | 72 | 17 | 5 | -1.55 | **+0.71** | +0.41 | 0.7006 | tidak | BELUM CUKUP |
| `M127` Slingshot Bullish | 95 | 15 | 5 | -1.12 | **+0.69** | +0.60 | 0.5809 | tidak | BELUM CUKUP |
| `M155` Market Cycle Strategy | 599 | 17 | 5 | -0.22 | **+0.66** | +1.37 | 0.2415 | tidak | BELUM CUKUP |
| `M82` Arthur Hill Rotasi Sasaran 10% | 544 | 17 | 5 | +0.07 | **+0.62** | +1.29 | 0.2676 | tidak | BELUM CUKUP |
| `M35` Pocket Pivot Morales & Kacher | 291 | 17 | 5 | -0.58 | **+0.61** | +1.00 | 0.3748 | tidak | BELUM CUKUP |
| `M31` Band Walk (BB 20/2) | 373 | 17 | 5 | -0.41 | **+0.60** | +0.46 | 0.6711 | tidak | BELUM CUKUP |
| `M105` Supertrend tulen | 319 | 17 | 5 | -0.86 | **+0.60** | +0.39 | 0.7192 | tidak | BELUM CUKUP |
| `M91` Stochastic Pop (Bernstein/Stec | 34 | 12 | 5 | -1.52 | **+0.58** | +0.18 | 0.8653 | tidak | BELUM CUKUP |
| `M08` SMA20 + SMA200 | 154 | 15 | 5 | -1.75 | **+0.55** | +0.52 | 0.6310 | tidak | BELUM CUKUP |
| `M36` Turtle 55/20 | 304 | 17 | 5 | -1.01 | **+0.52** | +0.66 | 0.5478 | tidak | BELUM CUKUP |

## Bila jadual ini boleh dipercayai

Hari beli diperlukan untuk melihat lift 2 mata merentas kaedah diuji: **107** (dikira semula setiap larian). Ada 17. Kad skor juga mewajibkan ≥ 10 hari beli dalam setiap rejim (G1), supaya keputusan tidak datang daripada satu fasa pasaran.

## Had

- Lift ialah kemahiran MASUK relatif kepada saham lain yang Lejar beli, bukan pulangan akaun.
- Kolam ialah alam Lejar (saham patuh Syariah ≥ USD10), bukan seluruh pasaran.
- Sasaran +10%/bulan tidak boleh dibaca daripada jadual ini (`REVERSE/SASARAN.md`).
