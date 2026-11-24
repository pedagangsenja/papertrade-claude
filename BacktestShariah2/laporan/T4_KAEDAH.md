# Lorong T4 satu-kaedah (jejak hadapan; rekod sahaja)

Dijana 2026-11-24 13:55 UTC oleh `standard/portfolio_t4.py` (Actions `analisis.yml`). Tiada order, tiada wang sebenar. Jangan ubah secara manual.

> **Status keputusan (kad skor, harga 2026-11-20):** TERBUKTI 0 · CALON 0 · BELUM CUKUP 226 · GAGAL 1 · NEGATIF 0. Rejim QQQ OFF sejak 2026-10-16. Hanya **TERBUKTI** layak untuk wang sebenar (`laporan/KAD_SKOR.md`); nombor dalam laporan ini BUKAN keputusan dan tidak boleh dibaca sebagai pangkat untuk wang sebenar.

Sesi terakhir 2026-11-23. **227 kaedah**, setiap satu dua lorong (L1 = keluar kaedah, L2 = Chandelier 4xATR14). Kawalan: 20 cabutan rawak 10 slot atas seluruh kolam Lejar, diasas semula pada tarikh mula setiap lorong. Penanda aras: SPUS, asas buka sesi pertama.

## Gate G6 (dikunci dalam `standard/kad_skor.py`)

Lorong L1 mesti (pindaan 7 Nov 2026): sesi >= 126; pulangan > 0; pulangan pada MDD -10% > SPUS pada MDD sama; nisbah pulangan/|MDD| > maksimum jalur rawak. 
**0 lulus.** Lorong paling lama ada 27 sesi; G6 tidak boleh lulus sebelum 126 sesi (anggaran 2027-04-09).

## 15 lorong L1 teratas ikut pulangan (BUKAN pangkat: semuanya BELUM CUKUP sehingga G6 dinilai)

| Kaedah | Mula | Sesi | Pul % | MDD % | Berat utk MDD -10% | Pul pada MDD -10% | SPUS pada MDD -10% | Nisbah pul/MDD | Maks jalur | T4 70/30 % |
|---|---|---|---|---|---|---|---|---|---|---|
| `M10` | 2026-10-16 | 27 | +9.77 | -6.59 | 1.00 | +9.77 | -6.81 | 1.48 | 0.74 | -3.01 |
| `M48` | 2026-10-16 | 27 | +8.50 | -5.73 | 1.00 | +8.50 | -6.81 | 1.48 | 0.74 | -3.34 |
| `M151` | 2026-10-16 | 27 | +5.75 | -4.00 | 1.00 | +5.75 | -6.81 | 1.44 | 0.74 | -4.15 |
| `M33` | 2026-10-16 | 27 | +5.31 | -7.28 | 1.00 | +5.31 | -6.81 | 0.73 | 0.74 | -4.26 |
| `M159` | 2026-10-16 | 27 | +5.08 | -6.13 | 1.00 | +5.08 | -6.81 | 0.83 | 0.74 | -4.32 |
| `M13` | 2026-10-16 | 27 | +4.90 | -6.63 | 1.00 | +4.90 | -6.81 | 0.74 | 0.74 | -4.39 |
| `M146` | 2026-10-16 | 27 | +4.47 | -7.02 | 1.00 | +4.47 | -6.81 | 0.64 | 0.74 | -4.49 |
| `M118` | 2026-10-16 | 27 | +4.23 | -8.32 | 1.00 | +4.23 | -6.81 | 0.51 | 0.74 | -4.58 |
| `M137` | 2026-10-16 | 27 | +4.01 | -5.91 | 1.00 | +4.01 | -6.81 | 0.68 | 0.74 | -4.65 |
| `M25` | 2026-10-16 | 27 | +3.18 | -7.99 | 1.00 | +3.18 | -6.81 | 0.40 | 0.74 | -4.88 |
| `M39` | 2026-10-16 | 27 | +3.11 | -6.53 | 1.00 | +3.11 | -6.81 | 0.48 | 0.74 | -4.91 |
| `M104` | 2026-11-06 | 12 | +2.70 | -0.26 | 1.00 | +2.70 | -2.13 | 10.32 | 0.67 | -0.68 |
| `M145` | 2026-10-16 | 27 | +2.62 | -3.87 | 1.00 | +2.62 | -6.81 | 0.68 | 0.74 | -5.04 |
| `M133` | 2026-10-16 | 27 | +2.32 | -5.73 | 1.00 | +2.32 | -6.81 | 0.40 | 0.74 | -5.14 |
| `M160` | 2026-10-16 | 27 | +1.98 | -5.75 | 1.00 | +1.98 | -6.81 | 0.34 | 0.74 | -5.24 |

## Cara membaca

- Pulangan beberapa sesi ialah hingar. `REVERSE/KEPEKATAN_BENIH.md`: SD pemilihan 4.15 mata/tahun pada 8 slot; kelebihan 20 mata/tahun perlu ~122 sesi untuk dilihat, 10 mata ~489 sesi (`laporan/BANDING_SPUS.md`).
- "Pada MDD -10%" = pulangan jika pendedahan dikecilkan (baki tunai) sehingga MDD tepat -10%, toleransi pengguna. Membanding pada MDD yang sama ialah satu-satunya bandingan adil dengan SPUS.
- Lajur T4 = teras SPUS + satelit kaedah, imbang bulanan. Nisbah CAGR/MDD SPUS+tunai hampir pemalar merentas berat (`REVERSE/SISTEM.md`), jadi berat ialah soalan toleransi drawdown, bukan soalan data.
- Kawalan rawak diambil daripada SELURUH kolam (Mxx + Nxx), jadi kaedah yang dibeli dalam tingkap menaik dibanding dengan pemilihan rawak dalam tingkap SAMA, bukan dengan sifar.

