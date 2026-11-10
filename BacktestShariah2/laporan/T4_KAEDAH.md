# Lorong T4 satu-kaedah (jejak hadapan; rekod sahaja)

Dijana 2026-11-10 13:58 UTC oleh `standard/portfolio_t4.py` (Actions `analisis.yml`). Tiada order, tiada wang sebenar. Jangan ubah secara manual.

> **Status keputusan (kad skor, harga 2026-11-06):** TERBUKTI 0 · CALON 0 · BELUM CUKUP 223 · GAGAL 0 · NEGATIF 0. Rejim QQQ OFF sejak 2026-10-16. Hanya **TERBUKTI** layak untuk wang sebenar (`laporan/KAD_SKOR.md`); nombor dalam laporan ini BUKAN keputusan dan tidak boleh dibaca sebagai pangkat untuk wang sebenar.

Sesi terakhir 2026-11-09. **223 kaedah**, setiap satu dua lorong (L1 = keluar kaedah, L2 = Chandelier 4xATR14). Kawalan: 20 cabutan rawak 10 slot atas seluruh kolam Lejar, diasas semula pada tarikh mula setiap lorong. Penanda aras: SPUS, asas buka sesi pertama.

## Gate G6 (dikunci dalam `standard/kad_skor.py`)

Lorong L1 mesti (pindaan 7 Nov 2026): sesi >= 126; pulangan > 0; pulangan pada MDD -10% > SPUS pada MDD sama; nisbah pulangan/|MDD| > maksimum jalur rawak. 
**0 lulus.** Lorong paling lama ada 17 sesi; G6 tidak boleh lulus sebelum 126 sesi (anggaran 2027-04-09).

## 15 lorong L1 teratas ikut pulangan (BUKAN pangkat: semuanya BELUM CUKUP sehingga G6 dinilai)

| Kaedah | Mula | Sesi | Pul % | MDD % | Berat utk MDD -10% | Pul pada MDD -10% | SPUS pada MDD -10% | Nisbah pul/MDD | Maks jalur | T4 70/30 % |
|---|---|---|---|---|---|---|---|---|---|---|
| `M118` | 2026-10-16 | 17 | +10.93 | -2.71 | 1.00 | +10.93 | -4.21 | 4.04 | 5.98 | +0.22 |
| `M02` | 2026-10-16 | 17 | +10.50 | -4.42 | 1.00 | +10.50 | -4.21 | 2.37 | 5.98 | +0.09 |
| `M91` | 2026-10-16 | 17 | +10.08 | -7.84 | 1.00 | +10.08 | -4.21 | 1.29 | 5.98 | +0.06 |
| `M10` | 2026-10-16 | 17 | +9.74 | -5.26 | 1.00 | +9.74 | -4.21 | 1.85 | 5.98 | -0.12 |
| `M13` | 2026-10-16 | 17 | +8.69 | -3.56 | 1.00 | +8.69 | -4.21 | 2.44 | 5.98 | -0.42 |
| `M151` | 2026-10-16 | 17 | +8.40 | -1.22 | 1.00 | +8.40 | -4.21 | 6.90 | 5.98 | -0.51 |
| `M33` | 2026-10-16 | 17 | +8.34 | -2.67 | 1.00 | +8.34 | -4.21 | 3.12 | 5.98 | -0.50 |
| `M48` | 2026-10-16 | 17 | +8.12 | -5.45 | 1.00 | +8.12 | -4.21 | 1.49 | 5.98 | -0.58 |
| `N45X16` | 2026-11-04 | 4 | +7.13 | 0.00 | 1.00 | +7.13 | -2.10 | 7133000.00 | 3.40 | +0.67 |
| `M133` | 2026-10-16 | 17 | +6.49 | -4.15 | 1.00 | +6.49 | -4.21 | 1.56 | 5.98 | -1.06 |
| `M146` | 2026-10-16 | 17 | +6.45 | -6.15 | 1.00 | +6.45 | -4.21 | 1.05 | 5.98 | -1.02 |
| `M124` | 2026-10-16 | 17 | +6.36 | -4.58 | 1.00 | +6.36 | -4.21 | 1.39 | 5.98 | -1.09 |
| `M159` | 2026-10-16 | 17 | +6.32 | -6.13 | 1.00 | +6.32 | -4.21 | 1.03 | 5.98 | -1.10 |
| `M137` | 2026-10-16 | 17 | +6.09 | -5.91 | 1.00 | +6.09 | -4.21 | 1.03 | 5.98 | -1.18 |
| `M129` | 2026-10-16 | 17 | +5.96 | -2.82 | 1.00 | +5.96 | -4.21 | 2.11 | 5.98 | -1.21 |

## Cara membaca

- Pulangan beberapa sesi ialah hingar. `REVERSE/KEPEKATAN_BENIH.md`: SD pemilihan 4.15 mata/tahun pada 8 slot; kelebihan 20 mata/tahun perlu ~122 sesi untuk dilihat, 10 mata ~489 sesi (`laporan/BANDING_SPUS.md`).
- "Pada MDD -10%" = pulangan jika pendedahan dikecilkan (baki tunai) sehingga MDD tepat -10%, toleransi pengguna. Membanding pada MDD yang sama ialah satu-satunya bandingan adil dengan SPUS.
- Lajur T4 = teras SPUS + satelit kaedah, imbang bulanan. Nisbah CAGR/MDD SPUS+tunai hampir pemalar merentas berat (`REVERSE/SISTEM.md`), jadi berat ialah soalan toleransi drawdown, bukan soalan data.
- Kawalan rawak diambil daripada SELURUH kolam (Mxx + Nxx), jadi kaedah yang dibeli dalam tingkap menaik dibanding dengan pemilihan rawak dalam tingkap SAMA, bukan dengan sifar.

