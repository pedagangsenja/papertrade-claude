# Lorong T4 satu-kaedah (jejak hadapan; rekod sahaja)

Dijana 2026-11-12 15:21 UTC oleh `standard/portfolio_t4.py` (Actions `analisis.yml`). Tiada order, tiada wang sebenar. Jangan ubah secara manual.

> **Status keputusan (kad skor, harga 2026-11-11):** TERBUKTI 0 · CALON 0 · BELUM CUKUP 223 · GAGAL 0 · NEGATIF 0. Rejim QQQ OFF sejak 2026-10-16. Hanya **TERBUKTI** layak untuk wang sebenar (`laporan/KAD_SKOR.md`); nombor dalam laporan ini BUKAN keputusan dan tidak boleh dibaca sebagai pangkat untuk wang sebenar.

Sesi terakhir 2026-11-11. **223 kaedah**, setiap satu dua lorong (L1 = keluar kaedah, L2 = Chandelier 4xATR14). Kawalan: 20 cabutan rawak 10 slot atas seluruh kolam Lejar, diasas semula pada tarikh mula setiap lorong. Penanda aras: SPUS, asas buka sesi pertama.

## Gate G6 (dikunci dalam `standard/kad_skor.py`)

Lorong L1 mesti (pindaan 7 Nov 2026): sesi >= 126; pulangan > 0; pulangan pada MDD -10% > SPUS pada MDD sama; nisbah pulangan/|MDD| > maksimum jalur rawak. 
**0 lulus.** Lorong paling lama ada 19 sesi; G6 tidak boleh lulus sebelum 126 sesi (anggaran 2027-04-09).

## 15 lorong L1 teratas ikut pulangan (BUKAN pangkat: semuanya BELUM CUKUP sehingga G6 dinilai)

| Kaedah | Mula | Sesi | Pul % | MDD % | Berat utk MDD -10% | Pul pada MDD -10% | SPUS pada MDD -10% | Nisbah pul/MDD | Maks jalur | T4 70/30 % |
|---|---|---|---|---|---|---|---|---|---|---|
| `M02` | 2026-10-16 | 19 | +11.76 | -4.42 | 1.00 | +11.76 | -3.75 | 2.66 | 5.21 | +0.78 |
| `M48` | 2026-10-16 | 19 | +10.99 | -5.45 | 1.00 | +10.99 | -3.75 | 2.02 | 5.21 | +0.57 |
| `M118` | 2026-10-16 | 19 | +10.30 | -2.71 | 1.00 | +10.30 | -3.75 | 3.81 | 5.21 | +0.37 |
| `M10` | 2026-10-16 | 19 | +10.29 | -5.26 | 1.00 | +10.29 | -3.75 | 1.96 | 5.21 | +0.36 |
| `M13` | 2026-10-16 | 19 | +9.99 | -3.56 | 1.00 | +9.99 | -3.75 | 2.80 | 5.21 | +0.28 |
| `M91` | 2026-10-16 | 19 | +9.30 | -7.84 | 1.00 | +9.30 | -3.75 | 1.19 | 5.21 | +0.18 |
| `M33` | 2026-10-16 | 19 | +8.89 | -2.67 | 1.00 | +8.89 | -3.75 | 3.33 | 5.21 | -0.01 |
| `M133` | 2026-10-16 | 19 | +7.95 | -4.15 | 1.00 | +7.95 | -3.75 | 1.92 | 5.21 | -0.31 |
| `M39` | 2026-10-16 | 19 | +7.60 | -2.40 | 1.00 | +7.60 | -3.75 | 3.17 | 5.21 | -0.41 |
| `M151` | 2026-10-16 | 19 | +7.47 | -1.22 | 1.00 | +7.47 | -3.75 | 6.14 | 5.21 | -0.45 |
| `M159` | 2026-10-16 | 19 | +7.29 | -6.13 | 1.00 | +7.29 | -3.75 | 1.19 | 5.21 | -0.50 |
| `M146` | 2026-10-16 | 19 | +6.71 | -6.15 | 1.00 | +6.71 | -3.75 | 1.09 | 5.21 | -0.62 |
| `M137` | 2026-10-16 | 19 | +6.51 | -5.91 | 1.00 | +6.51 | -3.75 | 1.10 | 5.21 | -0.72 |
| `N45X16` | 2026-11-04 | 6 | +6.48 | -0.78 | 1.00 | +6.48 | -1.63 | 8.25 | 2.23 | +0.80 |
| `M129` | 2026-10-16 | 19 | +5.91 | -2.82 | 1.00 | +5.91 | -3.75 | 2.10 | 5.21 | -0.89 |

## Cara membaca

- Pulangan beberapa sesi ialah hingar. `REVERSE/KEPEKATAN_BENIH.md`: SD pemilihan 4.15 mata/tahun pada 8 slot; kelebihan 20 mata/tahun perlu ~122 sesi untuk dilihat, 10 mata ~489 sesi (`laporan/BANDING_SPUS.md`).
- "Pada MDD -10%" = pulangan jika pendedahan dikecilkan (baki tunai) sehingga MDD tepat -10%, toleransi pengguna. Membanding pada MDD yang sama ialah satu-satunya bandingan adil dengan SPUS.
- Lajur T4 = teras SPUS + satelit kaedah, imbang bulanan. Nisbah CAGR/MDD SPUS+tunai hampir pemalar merentas berat (`REVERSE/SISTEM.md`), jadi berat ialah soalan toleransi drawdown, bukan soalan data.
- Kawalan rawak diambil daripada SELURUH kolam (Mxx + Nxx), jadi kaedah yang dibeli dalam tingkap menaik dibanding dengan pemilihan rawak dalam tingkap SAMA, bukan dengan sifar.

