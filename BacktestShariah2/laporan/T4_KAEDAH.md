# Lorong T4 satu-kaedah (jejak hadapan; rekod sahaja)

Dijana 2026-11-20 07:45 UTC oleh `standard/portfolio_t4.py` (Actions `analisis.yml`). Tiada order, tiada wang sebenar. Jangan ubah secara manual.

> **Status keputusan (kad skor, harga 2026-11-18):** TERBUKTI 0 · CALON 0 · BELUM CUKUP 225 · GAGAL 1 · NEGATIF 0. Rejim QQQ OFF sejak 2026-10-16. Hanya **TERBUKTI** layak untuk wang sebenar (`laporan/KAD_SKOR.md`); nombor dalam laporan ini BUKAN keputusan dan tidak boleh dibaca sebagai pangkat untuk wang sebenar.

Sesi terakhir 2026-11-19. **226 kaedah**, setiap satu dua lorong (L1 = keluar kaedah, L2 = Chandelier 4xATR14). Kawalan: 20 cabutan rawak 10 slot atas seluruh kolam Lejar, diasas semula pada tarikh mula setiap lorong. Penanda aras: SPUS, asas buka sesi pertama.

## Gate G6 (dikunci dalam `standard/kad_skor.py`)

Lorong L1 mesti (pindaan 7 Nov 2026): sesi >= 126; pulangan > 0; pulangan pada MDD -10% > SPUS pada MDD sama; nisbah pulangan/|MDD| > maksimum jalur rawak. 
**0 lulus.** Lorong paling lama ada 25 sesi; G6 tidak boleh lulus sebelum 126 sesi (anggaran 2027-04-09).

## 15 lorong L1 teratas ikut pulangan (BUKAN pangkat: semuanya BELUM CUKUP sehingga G6 dinilai)

| Kaedah | Mula | Sesi | Pul % | MDD % | Berat utk MDD -10% | Pul pada MDD -10% | SPUS pada MDD -10% | Nisbah pul/MDD | Maks jalur | T4 70/30 % |
|---|---|---|---|---|---|---|---|---|---|---|
| `N28X16` | 2026-11-04 | 12 | +61.58 | -6.27 | 1.00 | +61.58 | -5.36 | 9.82 | 0.45 | +14.73 |
| `N28X36` | 2026-11-04 | 12 | +58.73 | -6.27 | 1.00 | +58.73 | -5.36 | 9.37 | 0.45 | +13.87 |
| `M10` | 2026-10-16 | 25 | +7.43 | -5.26 | 1.00 | +7.43 | -7.40 | 1.41 | 0.87 | -3.06 |
| `M48` | 2026-10-16 | 25 | +6.82 | -5.45 | 1.00 | +6.82 | -7.40 | 1.25 | 0.87 | -3.23 |
| `M151` | 2026-10-16 | 25 | +5.57 | -2.61 | 1.00 | +5.57 | -7.40 | 2.14 | 0.87 | -3.60 |
| `M13` | 2026-10-16 | 25 | +4.69 | -4.81 | 1.00 | +4.69 | -7.40 | 0.97 | 0.87 | -3.84 |
| `M118` | 2026-10-16 | 25 | +3.89 | -7.01 | 1.00 | +3.89 | -7.40 | 0.56 | 0.87 | -4.07 |
| `M146` | 2026-10-16 | 25 | +3.81 | -6.15 | 1.00 | +3.81 | -7.40 | 0.62 | 0.87 | -4.06 |
| `M159` | 2026-10-16 | 25 | +3.42 | -6.13 | 1.00 | +3.42 | -7.40 | 0.56 | 0.87 | -4.21 |
| `M33` | 2026-10-16 | 25 | +2.52 | -7.28 | 1.00 | +2.52 | -7.40 | 0.35 | 0.87 | -4.43 |
| `M137` | 2026-10-16 | 25 | +2.36 | -5.91 | 1.00 | +2.36 | -7.40 | 0.40 | 0.87 | -4.52 |
| `M133` | 2026-10-16 | 25 | +2.18 | -5.34 | 1.00 | +2.18 | -7.40 | 0.41 | 0.87 | -4.57 |
| `M25` | 2026-10-16 | 25 | +2.13 | -6.73 | 1.00 | +2.13 | -7.40 | 0.32 | 0.87 | -4.56 |
| `M104` | 2026-11-06 | 10 | +2.05 | -0.26 | 1.00 | +2.05 | -1.22 | 7.83 | 0.17 | -0.24 |
| `M39` | 2026-10-16 | 25 | +1.96 | -5.57 | 1.00 | +1.96 | -7.40 | 0.35 | 0.87 | -4.63 |

## Cara membaca

- Pulangan beberapa sesi ialah hingar. `REVERSE/KEPEKATAN_BENIH.md`: SD pemilihan 4.15 mata/tahun pada 8 slot; kelebihan 20 mata/tahun perlu ~122 sesi untuk dilihat, 10 mata ~489 sesi (`laporan/BANDING_SPUS.md`).
- "Pada MDD -10%" = pulangan jika pendedahan dikecilkan (baki tunai) sehingga MDD tepat -10%, toleransi pengguna. Membanding pada MDD yang sama ialah satu-satunya bandingan adil dengan SPUS.
- Lajur T4 = teras SPUS + satelit kaedah, imbang bulanan. Nisbah CAGR/MDD SPUS+tunai hampir pemalar merentas berat (`REVERSE/SISTEM.md`), jadi berat ialah soalan toleransi drawdown, bukan soalan data.
- Kawalan rawak diambil daripada SELURUH kolam (Mxx + Nxx), jadi kaedah yang dibeli dalam tingkap menaik dibanding dengan pemilihan rawak dalam tingkap SAMA, bukan dengan sifar.

