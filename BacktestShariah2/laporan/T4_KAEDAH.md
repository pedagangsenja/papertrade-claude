# Lorong T4 satu-kaedah (jejak hadapan; rekod sahaja)

Dijana 2026-11-21 09:56 UTC oleh `standard/portfolio_t4.py` (Actions `analisis.yml`). Tiada order, tiada wang sebenar. Jangan ubah secara manual.

> **Status keputusan (kad skor, harga 2026-11-19):** TERBUKTI 0 · CALON 0 · BELUM CUKUP 225 · GAGAL 1 · NEGATIF 0. Rejim QQQ OFF sejak 2026-10-16. Hanya **TERBUKTI** layak untuk wang sebenar (`laporan/KAD_SKOR.md`); nombor dalam laporan ini BUKAN keputusan dan tidak boleh dibaca sebagai pangkat untuk wang sebenar.

Sesi terakhir 2026-11-20. **227 kaedah**, setiap satu dua lorong (L1 = keluar kaedah, L2 = Chandelier 4xATR14). Kawalan: 20 cabutan rawak 10 slot atas seluruh kolam Lejar, diasas semula pada tarikh mula setiap lorong. Penanda aras: SPUS, asas buka sesi pertama.

## Gate G6 (dikunci dalam `standard/kad_skor.py`)

Lorong L1 mesti (pindaan 7 Nov 2026): sesi >= 126; pulangan > 0; pulangan pada MDD -10% > SPUS pada MDD sama; nisbah pulangan/|MDD| > maksimum jalur rawak. 
**0 lulus.** Lorong paling lama ada 26 sesi; G6 tidak boleh lulus sebelum 126 sesi (anggaran 2027-04-09).

## 15 lorong L1 teratas ikut pulangan (BUKAN pangkat: semuanya BELUM CUKUP sehingga G6 dinilai)

| Kaedah | Mula | Sesi | Pul % | MDD % | Berat utk MDD -10% | Pul pada MDD -10% | SPUS pada MDD -10% | Nisbah pul/MDD | Maks jalur | T4 70/30 % |
|---|---|---|---|---|---|---|---|---|---|---|
| `M10` | 2026-10-16 | 26 | +5.61 | -6.59 | 1.00 | +5.61 | -9.51 | 0.85 | 0.57 | -6.53 |
| `M48` | 2026-10-16 | 26 | +4.63 | -5.73 | 1.00 | +4.63 | -9.51 | 0.81 | 0.57 | -6.79 |
| `M151` | 2026-10-16 | 26 | +4.06 | -4.00 | 1.00 | +4.06 | -9.51 | 1.01 | 0.57 | -6.97 |
| `M33` | 2026-10-16 | 26 | +3.47 | -7.28 | 1.00 | +3.47 | -9.51 | 0.48 | 0.57 | -7.13 |
| `M13` | 2026-10-16 | 26 | +2.69 | -6.63 | 1.00 | +2.69 | -9.51 | 0.41 | 0.57 | -7.36 |
| `M118` | 2026-10-16 | 26 | +2.43 | -8.32 | 1.00 | +2.43 | -9.51 | 0.29 | 0.57 | -7.44 |
| `M146` | 2026-10-16 | 26 | +2.33 | -7.02 | 1.00 | +2.33 | -9.51 | 0.33 | 0.57 | -7.45 |
| `M104` | 2026-11-06 | 11 | +2.31 | -0.26 | 1.00 | +2.31 | -5.61 | 8.79 | 0.22 | -3.24 |
| `M159` | 2026-10-16 | 26 | +2.15 | -6.13 | 1.00 | +2.15 | -9.51 | 0.35 | 0.57 | -7.49 |
| `M137` | 2026-10-16 | 26 | +2.09 | -5.91 | 1.00 | +2.09 | -9.51 | 0.35 | 0.57 | -7.52 |
| `M133` | 2026-10-16 | 26 | +1.76 | -5.73 | 1.00 | +1.76 | -9.51 | 0.31 | 0.57 | -7.63 |
| `M145` | 2026-10-16 | 26 | +1.20 | -3.87 | 1.00 | +1.20 | -9.51 | 0.31 | 0.57 | -7.76 |
| `M39` | 2026-10-16 | 26 | +0.92 | -6.53 | 1.00 | +0.92 | -9.51 | 0.14 | 0.57 | -7.87 |
| `M25` | 2026-10-16 | 26 | +0.75 | -7.99 | 1.00 | +0.75 | -9.51 | 0.09 | 0.57 | -7.91 |
| `N202X36` | 2026-11-13 | 6 | +0.07 | -2.12 | 1.00 | +0.07 | -8.60 | 0.03 | -0.12 | -6.00 |

## Cara membaca

- Pulangan beberapa sesi ialah hingar. `REVERSE/KEPEKATAN_BENIH.md`: SD pemilihan 4.15 mata/tahun pada 8 slot; kelebihan 20 mata/tahun perlu ~122 sesi untuk dilihat, 10 mata ~489 sesi (`laporan/BANDING_SPUS.md`).
- "Pada MDD -10%" = pulangan jika pendedahan dikecilkan (baki tunai) sehingga MDD tepat -10%, toleransi pengguna. Membanding pada MDD yang sama ialah satu-satunya bandingan adil dengan SPUS.
- Lajur T4 = teras SPUS + satelit kaedah, imbang bulanan. Nisbah CAGR/MDD SPUS+tunai hampir pemalar merentas berat (`REVERSE/SISTEM.md`), jadi berat ialah soalan toleransi drawdown, bukan soalan data.
- Kawalan rawak diambil daripada SELURUH kolam (Mxx + Nxx), jadi kaedah yang dibeli dalam tingkap menaik dibanding dengan pemilihan rawak dalam tingkap SAMA, bukan dengan sifar.

