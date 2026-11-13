# Lorong T4 satu-kaedah (jejak hadapan; rekod sahaja)

Dijana 2026-11-13 17:46 UTC oleh `standard/portfolio_t4.py` (Actions `analisis.yml`). Tiada order, tiada wang sebenar. Jangan ubah secara manual.

> **Status keputusan (kad skor, harga 2026-11-12):** TERBUKTI 0 · CALON 0 · BELUM CUKUP 223 · GAGAL 0 · NEGATIF 0. Rejim QQQ OFF sejak 2026-10-16. Hanya **TERBUKTI** layak untuk wang sebenar (`laporan/KAD_SKOR.md`); nombor dalam laporan ini BUKAN keputusan dan tidak boleh dibaca sebagai pangkat untuk wang sebenar.

Sesi terakhir 2026-11-12. **223 kaedah**, setiap satu dua lorong (L1 = keluar kaedah, L2 = Chandelier 4xATR14). Kawalan: 20 cabutan rawak 10 slot atas seluruh kolam Lejar, diasas semula pada tarikh mula setiap lorong. Penanda aras: SPUS, asas buka sesi pertama.

## Gate G6 (dikunci dalam `standard/kad_skor.py`)

Lorong L1 mesti (pindaan 7 Nov 2026): sesi >= 126; pulangan > 0; pulangan pada MDD -10% > SPUS pada MDD sama; nisbah pulangan/|MDD| > maksimum jalur rawak. 
**0 lulus.** Lorong paling lama ada 20 sesi; G6 tidak boleh lulus sebelum 126 sesi (anggaran 2027-04-09).

## 15 lorong L1 teratas ikut pulangan (BUKAN pangkat: semuanya BELUM CUKUP sehingga G6 dinilai)

| Kaedah | Mula | Sesi | Pul % | MDD % | Berat utk MDD -10% | Pul pada MDD -10% | SPUS pada MDD -10% | Nisbah pul/MDD | Maks jalur | T4 70/30 % |
|---|---|---|---|---|---|---|---|---|---|---|
| `M02` | 2026-10-16 | 20 | +10.84 | -4.42 | 1.00 | +10.84 | -3.40 | 2.45 | 4.31 | +0.77 |
| `M10` | 2026-10-16 | 20 | +9.59 | -5.26 | 1.00 | +9.59 | -3.40 | 1.82 | 4.31 | +0.42 |
| `M118` | 2026-10-16 | 20 | +8.99 | -2.71 | 1.00 | +8.99 | -3.40 | 3.32 | 4.31 | +0.25 |
| `M33` | 2026-10-16 | 20 | +8.71 | -2.67 | 1.00 | +8.71 | -3.40 | 3.26 | 4.31 | +0.19 |
| `M48` | 2026-10-16 | 20 | +8.56 | -5.45 | 1.00 | +8.56 | -3.40 | 1.57 | 4.31 | +0.12 |
| `M13` | 2026-10-16 | 20 | +8.34 | -3.56 | 1.00 | +8.34 | -3.40 | 2.34 | 4.31 | +0.07 |
| `M133` | 2026-10-16 | 20 | +6.83 | -4.15 | 1.00 | +6.83 | -3.40 | 1.65 | 4.31 | -0.38 |
| `M91` | 2026-10-16 | 20 | +6.75 | -7.84 | 1.00 | +6.75 | -3.40 | 0.86 | 4.31 | -0.27 |
| `M151` | 2026-10-16 | 20 | +6.65 | -1.61 | 1.00 | +6.65 | -3.40 | 4.13 | 4.31 | -0.43 |
| `M39` | 2026-10-16 | 20 | +6.46 | -2.40 | 1.00 | +6.46 | -3.40 | 2.70 | 4.31 | -0.48 |
| `N45X16` | 2026-11-04 | 7 | +5.61 | -1.43 | 1.00 | +5.61 | -1.27 | 3.93 | 1.14 | +0.79 |
| `M146` | 2026-10-16 | 20 | +5.51 | -6.15 | 1.00 | +5.51 | -3.40 | 0.90 | 4.31 | -0.70 |
| `M25` | 2026-10-16 | 20 | +5.47 | -5.78 | 1.00 | +5.47 | -3.40 | 0.95 | 4.31 | -0.75 |
| `M159` | 2026-10-16 | 20 | +5.07 | -6.13 | 1.00 | +5.07 | -3.40 | 0.83 | 4.31 | -0.89 |
| `M129` | 2026-10-16 | 20 | +4.84 | -2.82 | 1.00 | +4.84 | -3.40 | 1.72 | 4.31 | -0.95 |

## Cara membaca

- Pulangan beberapa sesi ialah hingar. `REVERSE/KEPEKATAN_BENIH.md`: SD pemilihan 4.15 mata/tahun pada 8 slot; kelebihan 20 mata/tahun perlu ~122 sesi untuk dilihat, 10 mata ~489 sesi (`laporan/BANDING_SPUS.md`).
- "Pada MDD -10%" = pulangan jika pendedahan dikecilkan (baki tunai) sehingga MDD tepat -10%, toleransi pengguna. Membanding pada MDD yang sama ialah satu-satunya bandingan adil dengan SPUS.
- Lajur T4 = teras SPUS + satelit kaedah, imbang bulanan. Nisbah CAGR/MDD SPUS+tunai hampir pemalar merentas berat (`REVERSE/SISTEM.md`), jadi berat ialah soalan toleransi drawdown, bukan soalan data.
- Kawalan rawak diambil daripada SELURUH kolam (Mxx + Nxx), jadi kaedah yang dibeli dalam tingkap menaik dibanding dengan pemilihan rawak dalam tingkap SAMA, bukan dengan sifar.

