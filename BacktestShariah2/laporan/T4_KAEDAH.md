# Lorong T4 satu-kaedah (jejak hadapan; rekod sahaja)

Dijana 2026-11-11 14:29 UTC oleh `standard/portfolio_t4.py` (Actions `analisis.yml`). Tiada order, tiada wang sebenar. Jangan ubah secara manual.

> **Status keputusan (kad skor, harga 2026-11-10):** TERBUKTI 0 · CALON 0 · BELUM CUKUP 223 · GAGAL 0 · NEGATIF 0. Rejim QQQ OFF sejak 2026-10-16. Hanya **TERBUKTI** layak untuk wang sebenar (`laporan/KAD_SKOR.md`); nombor dalam laporan ini BUKAN keputusan dan tidak boleh dibaca sebagai pangkat untuk wang sebenar.

Sesi terakhir 2026-11-10. **223 kaedah**, setiap satu dua lorong (L1 = keluar kaedah, L2 = Chandelier 4xATR14). Kawalan: 20 cabutan rawak 10 slot atas seluruh kolam Lejar, diasas semula pada tarikh mula setiap lorong. Penanda aras: SPUS, asas buka sesi pertama.

## Gate G6 (dikunci dalam `standard/kad_skor.py`)

Lorong L1 mesti (pindaan 7 Nov 2026): sesi >= 126; pulangan > 0; pulangan pada MDD -10% > SPUS pada MDD sama; nisbah pulangan/|MDD| > maksimum jalur rawak. 
**0 lulus.** Lorong paling lama ada 18 sesi; G6 tidak boleh lulus sebelum 126 sesi (anggaran 2027-04-09).

## 15 lorong L1 teratas ikut pulangan (BUKAN pangkat: semuanya BELUM CUKUP sehingga G6 dinilai)

| Kaedah | Mula | Sesi | Pul % | MDD % | Berat utk MDD -10% | Pul pada MDD -10% | SPUS pada MDD -10% | Nisbah pul/MDD | Maks jalur | T4 70/30 % |
|---|---|---|---|---|---|---|---|---|---|---|
| `M118` | 2026-10-16 | 18 | +10.44 | -2.71 | 1.00 | +10.44 | -4.81 | 3.86 | 5.19 | -0.35 |
| `M02` | 2026-10-16 | 18 | +10.10 | -4.42 | 1.00 | +10.10 | -4.81 | 2.28 | 5.19 | -0.45 |
| `M10` | 2026-10-16 | 18 | +9.15 | -5.26 | 1.00 | +9.15 | -4.81 | 1.74 | 5.19 | -0.72 |
| `M33` | 2026-10-16 | 18 | +8.81 | -2.67 | 1.00 | +8.81 | -4.81 | 3.30 | 5.19 | -0.80 |
| `M91` | 2026-10-16 | 18 | +8.58 | -7.84 | 1.00 | +8.58 | -4.81 | 1.09 | 5.19 | -0.80 |
| `M13` | 2026-10-16 | 18 | +7.92 | -3.56 | 1.00 | +7.92 | -4.81 | 2.22 | 5.19 | -1.07 |
| `M48` | 2026-10-16 | 18 | +7.72 | -5.45 | 1.00 | +7.72 | -4.81 | 1.42 | 5.19 | -1.13 |
| `M151` | 2026-10-16 | 18 | +7.47 | -1.22 | 1.00 | +7.47 | -4.81 | 6.14 | 5.19 | -1.21 |
| `M133` | 2026-10-16 | 18 | +7.43 | -4.15 | 1.00 | +7.43 | -4.81 | 1.79 | 5.19 | -1.22 |
| `M159` | 2026-10-16 | 18 | +7.34 | -6.13 | 1.00 | +7.34 | -4.81 | 1.20 | 5.19 | -1.23 |
| `M124` | 2026-10-16 | 18 | +6.74 | -4.58 | 1.00 | +6.74 | -4.81 | 1.47 | 5.19 | -1.40 |
| `M39` | 2026-10-16 | 18 | +6.30 | -2.40 | 1.00 | +6.30 | -4.81 | 2.63 | 5.19 | -1.54 |
| `N45X16` | 2026-11-04 | 5 | +6.29 | -0.78 | 1.00 | +6.29 | -2.71 | 8.02 | 2.28 | -0.01 |
| `M146` | 2026-10-16 | 18 | +6.24 | -6.15 | 1.00 | +6.24 | -4.81 | 1.01 | 5.19 | -1.52 |
| `M137` | 2026-10-16 | 18 | +6.13 | -5.91 | 1.00 | +6.13 | -4.81 | 1.04 | 5.19 | -1.59 |

## Cara membaca

- Pulangan beberapa sesi ialah hingar. `REVERSE/KEPEKATAN_BENIH.md`: SD pemilihan 4.15 mata/tahun pada 8 slot; kelebihan 20 mata/tahun perlu ~122 sesi untuk dilihat, 10 mata ~489 sesi (`laporan/BANDING_SPUS.md`).
- "Pada MDD -10%" = pulangan jika pendedahan dikecilkan (baki tunai) sehingga MDD tepat -10%, toleransi pengguna. Membanding pada MDD yang sama ialah satu-satunya bandingan adil dengan SPUS.
- Lajur T4 = teras SPUS + satelit kaedah, imbang bulanan. Nisbah CAGR/MDD SPUS+tunai hampir pemalar merentas berat (`REVERSE/SISTEM.md`), jadi berat ialah soalan toleransi drawdown, bukan soalan data.
- Kawalan rawak diambil daripada SELURUH kolam (Mxx + Nxx), jadi kaedah yang dibeli dalam tingkap menaik dibanding dengan pemilihan rawak dalam tingkap SAMA, bukan dengan sifar.

