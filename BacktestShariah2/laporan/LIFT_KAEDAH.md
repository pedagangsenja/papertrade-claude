# Lift MASUK setiap kaedah (gate G3)

Dijana 2026-11-24 13:54 UTC oleh `standard/lift_kaedah.py` (Actions `analisis.yml`). Pradaftar: `standard/SPEC_KAD_SKOR.md` pindaan 7 Nov 2026. Rekod analisis sahaja: tiada order, tiada wang sebenar.

## Apa yang diukur

Adakah kaedah ini memilih saham yang lebih baik daripada saham lain yang dibeli Lejar **pada hari yang sama dan tahap turun-naik (tercile ATR) yang sama**? Pulangan diukur pada ufuk TETAP 10 sesi (buka hari beli → tutup sesi ke-10, kos 0.2%), jadi peraturan keluar TIDAK mempengaruhi nombor ini. Nilai keluar diukur oleh G2 (buku harian) dan G6 (portfolio).

Versi lama (padanan baldi hari pegang, SE ikut hari beli) dibuang kerana ia meluluskan belian RAWAK: henti + sasaran rawak mendapat lift +2.17 mata, dan SE lama meluluskan plasebo sehingga 51% masa. Reka bentuk ini lulus plasebo pada kadar 1.9–3.4% (`laporan/PLASEBO_GATE.md`).

## Data

Hari beli LANGSUNG sahaja (Mxx sejak isyarat 2026-10-15, Nxx/GB sejak 2026-11-03). **34,519 saham-hari** dengan ufuk 10 sesi lengkap, 18 hari beli, 223 kaedah. Rejim (QQQ > SMA50 dan SMA10 > SMA20) pada hari beli ini: ON 1 · OFF 17.

## Keputusan

Diuji (≥ 30 saham-hari, ≥ 5 minggu): **94** kaedah. Lift positif lulus BH-FDR: **0**. Lift negatif lulus BH-FDR: **0**.

| Kaedah | Saham-hari | Hari beli | Minggu | Pulangan 10 sesi % | **Lift mata** | t | p | BH | Status |
|---|---|---|---|---|---|---|---|---|---|
| `M133` Bull Hook (Crabel) | 47 | 12 | 5 | +1.92 | **+3.90** | +2.65 | 0.0570 | tidak | BELUM CUKUP |
| `M146` 3-Bar Momentum Pattern | 76 | 17 | 5 | +1.15 | **+2.60** | +2.50 | 0.0666 | tidak | BELUM CUKUP |
| `M46` Jurang Naik Boleh Beli (Buyabl | 34 | 11 | 5 | -0.92 | **+2.41** | +1.20 | 0.2973 | tidak | BELUM CUKUP |
| `M117` Landry Pullback (high 2 bulan) | 126 | 15 | 5 | -0.06 | **+2.41** | +2.81 | 0.0481 | tidak | BELUM CUKUP |
| `M93` Bollinger Kaedah II: %b + MFI | 255 | 18 | 5 | +0.90 | **+1.86** | +2.17 | 0.0960 | tidak | BELUM CUKUP |
| `M15` Break & Retest + Henti ATR | 284 | 18 | 5 | +0.39 | **+1.76** | +1.53 | 0.2002 | tidak | BELUM CUKUP |
| `M80` Radge Saluran Purata Bergerak  | 259 | 18 | 5 | +0.46 | **+1.75** | +2.13 | 0.1002 | tidak | BELUM CUKUP |
| `M18` EMA9/21 Pullback | 324 | 18 | 5 | -0.20 | **+1.73** | +1.67 | 0.1711 | tidak | BELUM CUKUP |
| `M150` Trend Bar Failure (Brooks) | 99 | 17 | 5 | +0.23 | **+1.68** | +2.30 | 0.0826 | tidak | BELUM CUKUP |
| `M158` Doubly Adaptive Profit Targets | 349 | 18 | 5 | +0.45 | **+1.48** | +2.12 | 0.1010 | tidak | BELUM CUKUP |
| `M137` Livermore System | 162 | 18 | 5 | -0.54 | **+1.15** | +1.71 | 0.1621 | tidak | BELUM CUKUP |
| `M25` VWAP Wave (proksi harian) | 169 | 16 | 5 | -0.96 | **+1.13** | +1.58 | 0.1900 | tidak | BELUM CUKUP |
| `M145` Yum-Yum Continuation | 291 | 18 | 5 | -0.44 | **+1.11** | +1.98 | 0.1188 | tidak | BELUM CUKUP |
| `M161` EMA 10/21 + Supertrend (10,3) | 447 | 18 | 5 | -0.40 | **+1.08** | +1.48 | 0.2133 | tidak | BELUM CUKUP |
| `M127` Slingshot Bullish | 105 | 16 | 5 | -0.99 | **+1.06** | +0.86 | 0.4367 | tidak | BELUM CUKUP |
| `M77` Undercut & Rally pada Purata B | 53 | 16 | 5 | -2.05 | **+0.94** | +0.61 | 0.5734 | tidak | BELUM CUKUP |
| `M119` 180 Bullish (Cooper) | 146 | 17 | 5 | -1.19 | **+0.78** | +1.13 | 0.3218 | tidak | BELUM CUKUP |
| `M01` Bollinger Band + RSI | 109 | 18 | 5 | -2.37 | **+0.76** | +0.35 | 0.7432 | tidak | BELUM CUKUP |
| `M35` Pocket Pivot Morales & Kacher | 303 | 18 | 5 | -0.61 | **+0.72** | +1.22 | 0.2901 | tidak | BELUM CUKUP |
| `M153` Range Leader | 1212 | 18 | 5 | -1.79 | **+0.70** | +0.95 | 0.3953 | tidak | BELUM CUKUP |
| `M160` Measured Move Up | 105 | 16 | 5 | -2.10 | **+0.69** | +0.68 | 0.5346 | tidak | BELUM CUKUP |
| `M91` Stochastic Pop (Bernstein/Stec | 35 | 13 | 5 | -1.49 | **+0.67** | +0.21 | 0.8406 | tidak | BELUM CUKUP |
| `M33` Supertrend + SMA10 | 216 | 18 | 5 | -1.18 | **+0.67** | +0.37 | 0.7277 | tidak | BELUM CUKUP |
| `M23` Breitstein Kapitulasi + Kesina | 117 | 18 | 5 | -2.13 | **+0.66** | +0.66 | 0.5454 | tidak | BELUM CUKUP |
| `M31` Band Walk (BB 20/2) | 391 | 18 | 5 | -0.54 | **+0.65** | +0.52 | 0.6307 | tidak | BELUM CUKUP |

## Bila jadual ini boleh dipercayai

Hari beli diperlukan untuk melihat lift 2 mata merentas kaedah diuji: **114** (dikira semula setiap larian). Ada 18. Kad skor juga mewajibkan ≥ 10 hari beli dalam setiap rejim (G1), supaya keputusan tidak datang daripada satu fasa pasaran.

## Had

- Lift ialah kemahiran MASUK relatif kepada saham lain yang Lejar beli, bukan pulangan akaun.
- Kolam ialah alam Lejar (saham patuh Syariah ≥ USD10), bukan seluruh pasaran.
- Sasaran +10%/bulan tidak boleh dibaca daripada jadual ini (`REVERSE/SASARAN.md`).
