# Lorong T4 satu-kaedah (jejak hadapan; rekod sahaja)

Dijana 2026-11-19 10:50 UTC oleh `standard/portfolio_t4.py` (Actions `analisis.yml`). Tiada order, tiada wang sebenar. Jangan ubah secara manual.

> **Status keputusan (kad skor, harga 2026-11-18):** TERBUKTI 0 · CALON 0 · BELUM CUKUP 225 · GAGAL 1 · NEGATIF 0. Rejim QQQ OFF sejak 2026-10-16. Hanya **TERBUKTI** layak untuk wang sebenar (`laporan/KAD_SKOR.md`); nombor dalam laporan ini BUKAN keputusan dan tidak boleh dibaca sebagai pangkat untuk wang sebenar.

Sesi terakhir 2026-11-18. **226 kaedah**, setiap satu dua lorong (L1 = keluar kaedah, L2 = Chandelier 4xATR14). Kawalan: 20 cabutan rawak 10 slot atas seluruh kolam Lejar, diasas semula pada tarikh mula setiap lorong. Penanda aras: SPUS, asas buka sesi pertama.

## Gate G6 (dikunci dalam `standard/kad_skor.py`)

Lorong L1 mesti (pindaan 7 Nov 2026): sesi >= 126; pulangan > 0; pulangan pada MDD -10% > SPUS pada MDD sama; nisbah pulangan/|MDD| > maksimum jalur rawak. 
**0 lulus.** Lorong paling lama ada 24 sesi; G6 tidak boleh lulus sebelum 126 sesi (anggaran 2027-04-09).

## 15 lorong L1 teratas ikut pulangan (BUKAN pangkat: semuanya BELUM CUKUP sehingga G6 dinilai)

| Kaedah | Mula | Sesi | Pul % | MDD % | Berat utk MDD -10% | Pul pada MDD -10% | SPUS pada MDD -10% | Nisbah pul/MDD | Maks jalur | T4 70/30 % |
|---|---|---|---|---|---|---|---|---|---|---|
| `M10` | 2026-10-16 | 24 | +10.20 | -5.26 | 1.00 | +10.20 | -7.78 | 1.94 | 1.38 | -2.55 |
| `M48` | 2026-10-16 | 24 | +8.74 | -5.45 | 1.00 | +8.74 | -7.78 | 1.60 | 1.38 | -2.94 |
| `M151` | 2026-10-16 | 24 | +8.14 | -1.61 | 1.00 | +8.14 | -7.78 | 5.05 | 1.38 | -3.13 |
| `M13` | 2026-10-16 | 24 | +6.52 | -3.56 | 1.00 | +6.52 | -7.78 | 1.83 | 1.38 | -3.59 |
| `M146` | 2026-10-16 | 24 | +5.74 | -6.15 | 1.00 | +5.74 | -7.78 | 0.93 | 1.38 | -3.80 |
| `M33` | 2026-10-16 | 24 | +5.70 | -4.40 | 1.00 | +5.70 | -7.78 | 1.30 | 1.38 | -3.81 |
| `M39` | 2026-10-16 | 24 | +5.26 | -2.51 | 1.00 | +5.26 | -7.78 | 2.10 | 1.38 | -3.96 |
| `M118` | 2026-10-16 | 24 | +5.13 | -5.90 | 1.00 | +5.13 | -7.78 | 0.87 | 1.38 | -3.99 |
| `M159` | 2026-10-16 | 24 | +5.02 | -6.13 | 1.00 | +5.02 | -7.78 | 0.82 | 1.38 | -4.01 |
| `M137` | 2026-10-16 | 24 | +3.97 | -5.91 | 1.00 | +3.97 | -7.78 | 0.67 | 1.38 | -4.32 |
| `M145` | 2026-10-16 | 24 | +3.93 | -2.18 | 1.00 | +3.93 | -7.78 | 1.80 | 1.38 | -4.32 |
| `M25` | 2026-10-16 | 24 | +3.80 | -6.06 | 1.00 | +3.80 | -7.78 | 0.63 | 1.38 | -4.36 |
| `M133` | 2026-10-16 | 24 | +2.93 | -4.90 | 1.00 | +2.93 | -7.78 | 0.60 | 1.38 | -4.62 |
| `M129` | 2026-10-16 | 24 | +2.62 | -3.39 | 1.00 | +2.62 | -7.78 | 0.77 | 1.38 | -4.71 |
| `M104` | 2026-11-06 | 9 | +2.32 | -0.02 | 1.00 | +2.32 | -1.63 | 108.43 | 0.70 | -0.44 |

## Cara membaca

- Pulangan beberapa sesi ialah hingar. `REVERSE/KEPEKATAN_BENIH.md`: SD pemilihan 4.15 mata/tahun pada 8 slot; kelebihan 20 mata/tahun perlu ~122 sesi untuk dilihat, 10 mata ~489 sesi (`laporan/BANDING_SPUS.md`).
- "Pada MDD -10%" = pulangan jika pendedahan dikecilkan (baki tunai) sehingga MDD tepat -10%, toleransi pengguna. Membanding pada MDD yang sama ialah satu-satunya bandingan adil dengan SPUS.
- Lajur T4 = teras SPUS + satelit kaedah, imbang bulanan. Nisbah CAGR/MDD SPUS+tunai hampir pemalar merentas berat (`REVERSE/SISTEM.md`), jadi berat ialah soalan toleransi drawdown, bukan soalan data.
- Kawalan rawak diambil daripada SELURUH kolam (Mxx + Nxx), jadi kaedah yang dibeli dalam tingkap menaik dibanding dengan pemilihan rawak dalam tingkap SAMA, bukan dengan sifar.

