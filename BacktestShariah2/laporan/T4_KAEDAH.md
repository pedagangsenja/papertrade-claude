# Lorong T4 satu-kaedah (jejak hadapan; rekod sahaja)

Dijana 2026-11-25 12:24 UTC oleh `standard/portfolio_t4.py` (Actions `analisis.yml`). Tiada order, tiada wang sebenar. Jangan ubah secara manual.

> **Status keputusan (kad skor, harga 2026-11-24):** TERBUKTI 0 · CALON 0 · BELUM CUKUP 226 · GAGAL 1 · NEGATIF 0. Rejim QQQ OFF sejak 2026-10-16. Hanya **TERBUKTI** layak untuk wang sebenar (`laporan/KAD_SKOR.md`); nombor dalam laporan ini BUKAN keputusan dan tidak boleh dibaca sebagai pangkat untuk wang sebenar.

Sesi terakhir 2026-11-24. **227 kaedah**, setiap satu dua lorong (L1 = keluar kaedah, L2 = Chandelier 4xATR14). Kawalan: 20 cabutan rawak 10 slot atas seluruh kolam Lejar, diasas semula pada tarikh mula setiap lorong. Penanda aras: SPUS, asas buka sesi pertama.

## Gate G6 (dikunci dalam `standard/kad_skor.py`)

Lorong L1 mesti (pindaan 7 Nov 2026): sesi >= 126; pulangan > 0; pulangan pada MDD -10% > SPUS pada MDD sama; nisbah pulangan/|MDD| > maksimum jalur rawak. 
**0 lulus.** Lorong paling lama ada 28 sesi; G6 tidak boleh lulus sebelum 126 sesi (anggaran 2027-04-09).

## 15 lorong L1 teratas ikut pulangan (BUKAN pangkat: semuanya BELUM CUKUP sehingga G6 dinilai)

| Kaedah | Mula | Sesi | Pul % | MDD % | Berat utk MDD -10% | Pul pada MDD -10% | SPUS pada MDD -10% | Nisbah pul/MDD | Maks jalur | T4 70/30 % |
|---|---|---|---|---|---|---|---|---|---|---|
| `M10` | 2026-10-16 | 28 | +9.63 | -6.59 | 1.00 | +9.63 | -8.36 | 1.46 | 0.44 | -4.39 |
| `M48` | 2026-10-16 | 28 | +9.42 | -5.73 | 1.00 | +9.42 | -8.36 | 1.64 | 0.44 | -4.41 |
| `M151` | 2026-10-16 | 28 | +7.26 | -4.00 | 1.00 | +7.26 | -8.36 | 1.81 | 0.44 | -5.05 |
| `M33` | 2026-10-16 | 28 | +6.81 | -7.28 | 1.00 | +6.81 | -8.36 | 0.94 | 0.44 | -5.19 |
| `M159` | 2026-10-16 | 28 | +6.75 | -6.13 | 1.00 | +6.75 | -8.36 | 1.10 | 0.44 | -5.17 |
| `M137` | 2026-10-16 | 28 | +6.54 | -5.91 | 1.00 | +6.54 | -8.36 | 1.11 | 0.44 | -5.24 |
| `M146` | 2026-10-16 | 28 | +6.14 | -7.02 | 1.00 | +6.14 | -8.36 | 0.87 | 0.44 | -5.38 |
| `M13` | 2026-10-16 | 28 | +5.84 | -6.63 | 1.00 | +5.84 | -8.36 | 0.88 | 0.44 | -5.47 |
| `M118` | 2026-10-16 | 28 | +5.48 | -8.32 | 1.00 | +5.48 | -8.36 | 0.66 | 0.44 | -5.57 |
| `M145` | 2026-10-16 | 28 | +5.31 | -3.87 | 1.00 | +5.31 | -8.36 | 1.37 | 0.44 | -5.57 |
| `M39` | 2026-10-16 | 28 | +4.92 | -6.53 | 1.00 | +4.92 | -8.36 | 0.75 | 0.44 | -5.73 |
| `M25` | 2026-10-16 | 28 | +3.93 | -7.99 | 1.00 | +3.93 | -8.36 | 0.49 | 0.44 | -6.01 |
| `M133` | 2026-10-16 | 28 | +3.37 | -6.02 | 1.00 | +3.37 | -8.36 | 0.56 | 0.44 | -6.17 |
| `M160` | 2026-10-16 | 28 | +3.12 | -5.75 | 1.00 | +3.12 | -8.36 | 0.54 | 0.44 | -6.24 |
| `M104` | 2026-11-06 | 13 | +2.83 | -0.26 | 1.00 | +2.83 | -4.13 | 10.79 | -0.05 | -2.04 |

## Cara membaca

- Pulangan beberapa sesi ialah hingar. `REVERSE/KEPEKATAN_BENIH.md`: SD pemilihan 4.15 mata/tahun pada 8 slot; kelebihan 20 mata/tahun perlu ~122 sesi untuk dilihat, 10 mata ~489 sesi (`laporan/BANDING_SPUS.md`).
- "Pada MDD -10%" = pulangan jika pendedahan dikecilkan (baki tunai) sehingga MDD tepat -10%, toleransi pengguna. Membanding pada MDD yang sama ialah satu-satunya bandingan adil dengan SPUS.
- Lajur T4 = teras SPUS + satelit kaedah, imbang bulanan. Nisbah CAGR/MDD SPUS+tunai hampir pemalar merentas berat (`REVERSE/SISTEM.md`), jadi berat ialah soalan toleransi drawdown, bukan soalan data.
- Kawalan rawak diambil daripada SELURUH kolam (Mxx + Nxx), jadi kaedah yang dibeli dalam tingkap menaik dibanding dengan pemilihan rawak dalam tingkap SAMA, bukan dengan sifar.

