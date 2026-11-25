# Lift MASUK setiap kaedah (gate G3)

Dijana 2026-11-25 17:19 UTC oleh `standard/lift_kaedah.py` (Actions `analisis.yml`). Pradaftar: `standard/SPEC_KAD_SKOR.md` pindaan 7 Nov 2026. Rekod analisis sahaja: tiada order, tiada wang sebenar.

## Apa yang diukur

Adakah kaedah ini memilih saham yang lebih baik daripada saham lain yang dibeli Lejar **pada hari yang sama dan tahap turun-naik (tercile ATR) yang sama**? Pulangan diukur pada ufuk TETAP 10 sesi (buka hari beli → tutup sesi ke-10, kos 0.2%), jadi peraturan keluar TIDAK mempengaruhi nombor ini. Nilai keluar diukur oleh G2 (buku harian) dan G6 (portfolio).

Versi lama (padanan baldi hari pegang, SE ikut hari beli) dibuang kerana ia meluluskan belian RAWAK: henti + sasaran rawak mendapat lift +2.17 mata, dan SE lama meluluskan plasebo sehingga 51% masa. Reka bentuk ini lulus plasebo pada kadar 1.9–3.4% (`laporan/PLASEBO_GATE.md`).

## Data

Hari beli LANGSUNG sahaja (Mxx sejak isyarat 2026-10-15, Nxx/GB sejak 2026-11-03). **36,245 saham-hari** dengan ufuk 10 sesi lengkap, 19 hari beli, 223 kaedah. Rejim (QQQ > SMA50 dan SMA10 > SMA20) pada hari beli ini: ON 1 · OFF 18.

## Keputusan

Diuji (≥ 30 saham-hari, ≥ 5 minggu): **96** kaedah. Lift positif lulus BH-FDR: **0**. Lift negatif lulus BH-FDR: **0**.

| Kaedah | Saham-hari | Hari beli | Minggu | Pulangan 10 sesi % | **Lift mata** | t | p | BH | Status |
|---|---|---|---|---|---|---|---|---|---|
| `M133` Bull Hook (Crabel) | 47 | 12 | 5 | +1.74 | **+3.89** | +2.47 | 0.0686 | tidak | BELUM CUKUP |
| `M146` 3-Bar Momentum Pattern | 76 | 17 | 5 | +1.15 | **+2.60** | +2.50 | 0.0664 | tidak | BELUM CUKUP |
| `M117` Landry Pullback (high 2 bulan) | 131 | 16 | 5 | -0.23 | **+2.28** | +2.63 | 0.0584 | tidak | BELUM CUKUP |
| `M93` Bollinger Kaedah II: %b + MFI | 259 | 19 | 5 | +0.83 | **+1.87** | +2.21 | 0.0913 | tidak | BELUM CUKUP |
| `M80` Radge Saluran Purata Bergerak  | 272 | 19 | 5 | +0.33 | **+1.82** | +2.44 | 0.0708 | tidak | BELUM CUKUP |
| `M18` EMA9/21 Pullback | 344 | 19 | 5 | -0.40 | **+1.70** | +1.71 | 0.1617 | tidak | BELUM CUKUP |
| `M15` Break & Retest + Henti ATR | 290 | 19 | 5 | +0.24 | **+1.69** | +1.40 | 0.2330 | tidak | BELUM CUKUP |
| `M150` Trend Bar Failure (Brooks) | 100 | 18 | 5 | +0.21 | **+1.68** | +2.32 | 0.0808 | tidak | BELUM CUKUP |
| `M118` Expansion Pivot (Cooper) | 83 | 19 | 5 | -1.45 | **+1.49** | +1.04 | 0.3579 | tidak | BELUM CUKUP |
| `M158` Doubly Adaptive Profit Targets | 351 | 19 | 5 | +0.40 | **+1.44** | +2.11 | 0.1021 | tidak | BELUM CUKUP |
| `M25` VWAP Wave (proksi harian) | 173 | 17 | 5 | -1.02 | **+1.17** | +1.66 | 0.1714 | tidak | BELUM CUKUP |
| `M127` Slingshot Bullish | 105 | 16 | 5 | -0.99 | **+1.07** | +0.86 | 0.4362 | tidak | BELUM CUKUP |
| `M119` 180 Bullish (Cooper) | 149 | 18 | 5 | -1.06 | **+0.99** | +1.38 | 0.2389 | tidak | BELUM CUKUP |
| `M77` Undercut & Rally pada Purata B | 54 | 17 | 5 | -2.13 | **+0.91** | +0.62 | 0.5688 | tidak | BELUM CUKUP |
| `M145` Yum-Yum Continuation | 299 | 19 | 5 | -0.73 | **+0.91** | +1.52 | 0.2040 | tidak | BELUM CUKUP |
| `M161` EMA 10/21 + Supertrend (10,3) | 458 | 19 | 5 | -0.69 | **+0.86** | +1.47 | 0.2157 | tidak | BELUM CUKUP |
| `M107` Golden Cross SMA50/200 | 34 | 16 | 5 | -1.80 | **+0.78** | +0.59 | 0.5843 | tidak | BELUM CUKUP |
| `M01` Bollinger Band + RSI | 111 | 19 | 5 | -2.51 | **+0.77** | +0.36 | 0.7359 | tidak | BELUM CUKUP |
| `M35` Pocket Pivot Morales & Kacher | 307 | 19 | 5 | -0.63 | **+0.76** | +1.26 | 0.2746 | tidak | BELUM CUKUP |
| `M137` Livermore System | 166 | 19 | 5 | -1.03 | **+0.73** | +0.92 | 0.4108 | tidak | BELUM CUKUP |
| `M31` Band Walk (BB 20/2) | 392 | 19 | 5 | -0.50 | **+0.72** | +0.59 | 0.5858 | tidak | BELUM CUKUP |
| `M153` Range Leader | 1244 | 19 | 5 | -1.89 | **+0.68** | +0.96 | 0.3905 | tidak | BELUM CUKUP |
| `M82` Arthur Hill Rotasi Sasaran 10% | 565 | 19 | 5 | -0.05 | **+0.66** | +1.45 | 0.2194 | tidak | BELUM CUKUP |
| `M160` Measured Move Up | 106 | 17 | 5 | -2.18 | **+0.64** | +0.65 | 0.5531 | tidak | BELUM CUKUP |
| `M33` Supertrend + SMA10 | 217 | 19 | 5 | -1.24 | **+0.61** | +0.34 | 0.7493 | tidak | BELUM CUKUP |

## Bila jadual ini boleh dipercayai

Hari beli diperlukan untuk melihat lift 2 mata merentas kaedah diuji: **123** (dikira semula setiap larian). Ada 19. Kad skor juga mewajibkan ≥ 10 hari beli dalam setiap rejim (G1), supaya keputusan tidak datang daripada satu fasa pasaran.

## Had

- Lift ialah kemahiran MASUK relatif kepada saham lain yang Lejar beli, bukan pulangan akaun.
- Kolam ialah alam Lejar (saham patuh Syariah ≥ USD10), bukan seluruh pasaran.
- Sasaran +10%/bulan tidak boleh dibaca daripada jadual ini (`REVERSE/SASARAN.md`).
