# Lorong T4 satu-kaedah (jejak hadapan; rekod sahaja)

Dijana 2026-11-27 12:23 UTC oleh `standard/portfolio_t4.py` (Actions `analisis.yml`). Tiada order, tiada wang sebenar. Jangan ubah secara manual.

> **Status keputusan (kad skor, harga 2026-11-25):** TERBUKTI 0 · CALON 0 · BELUM CUKUP 225 · GAGAL 2 · NEGATIF 0. Rejim QQQ OFF sejak 2026-10-16. Hanya **TERBUKTI** layak untuk wang sebenar (`laporan/KAD_SKOR.md`); nombor dalam laporan ini BUKAN keputusan dan tidak boleh dibaca sebagai pangkat untuk wang sebenar.

Sesi terakhir 2026-11-25. **227 kaedah**, setiap satu dua lorong (L1 = keluar kaedah, L2 = Chandelier 4xATR14). Kawalan: 20 cabutan rawak 10 slot atas seluruh kolam Lejar, diasas semula pada tarikh mula setiap lorong. Penanda aras: SPUS, asas buka sesi pertama.

## Gate G6 (dikunci dalam `standard/kad_skor.py`)

Lorong L1 mesti (pindaan 7 Nov 2026): sesi >= 126; pulangan > 0; pulangan pada MDD -10% > SPUS pada MDD sama; nisbah pulangan/|MDD| > maksimum jalur rawak. 
**0 lulus.** Lorong paling lama ada 29 sesi; G6 tidak boleh lulus sebelum 126 sesi (anggaran 2027-04-09).

## 15 lorong L1 teratas ikut pulangan (BUKAN pangkat: semuanya BELUM CUKUP sehingga G6 dinilai)

| Kaedah | Mula | Sesi | Pul % | MDD % | Berat utk MDD -10% | Pul pada MDD -10% | SPUS pada MDD -10% | Nisbah pul/MDD | Maks jalur | T4 70/30 % |
|---|---|---|---|---|---|---|---|---|---|---|
| `M10` | 2026-10-16 | 29 | +9.71 | -6.59 | 1.00 | +9.71 | -9.54 | 1.47 | 0.47 | -5.99 |
| `M48` | 2026-10-16 | 29 | +8.83 | -5.73 | 1.00 | +8.83 | -9.54 | 1.54 | 0.47 | -6.18 |
| `M159` | 2026-10-16 | 29 | +7.75 | -6.13 | 1.00 | +7.75 | -9.54 | 1.26 | 0.47 | -6.47 |
| `M33` | 2026-10-16 | 29 | +7.59 | -7.28 | 1.00 | +7.59 | -9.54 | 1.04 | 0.47 | -6.60 |
| `M146` | 2026-10-16 | 29 | +7.12 | -7.02 | 1.00 | +7.12 | -9.54 | 1.01 | 0.47 | -6.74 |
| `M151` | 2026-10-16 | 29 | +6.92 | -4.00 | 1.00 | +6.92 | -9.54 | 1.73 | 0.47 | -6.76 |
| `M137` | 2026-10-16 | 29 | +6.71 | -5.91 | 1.00 | +6.71 | -9.54 | 1.14 | 0.47 | -6.80 |
| `M13` | 2026-10-16 | 29 | +6.71 | -6.63 | 1.00 | +6.71 | -9.54 | 1.01 | 0.47 | -6.85 |
| `M118` | 2026-10-16 | 29 | +6.35 | -8.32 | 1.00 | +6.35 | -9.54 | 0.76 | 0.47 | -6.95 |
| `M39` | 2026-10-16 | 29 | +6.25 | -6.53 | 1.00 | +6.25 | -9.54 | 0.96 | 0.47 | -6.96 |
| `M145` | 2026-10-16 | 29 | +5.99 | -3.87 | 1.00 | +5.99 | -9.54 | 1.55 | 0.47 | -6.97 |
| `M25` | 2026-10-16 | 29 | +3.93 | -7.99 | 1.00 | +3.93 | -9.54 | 0.49 | 0.47 | -7.63 |
| `M160` | 2026-10-16 | 29 | +3.89 | -5.75 | 1.00 | +3.89 | -9.54 | 0.68 | 0.47 | -7.63 |
| `M133` | 2026-10-16 | 29 | +3.52 | -6.02 | 1.00 | +3.52 | -9.54 | 0.58 | 0.47 | -7.74 |
| `M54` | 2026-10-16 | 29 | +3.36 | -10.41 | 0.96 | +3.23 | -9.54 | 0.32 | 0.47 | -7.74 |

## Cara membaca

- Pulangan beberapa sesi ialah hingar. `REVERSE/KEPEKATAN_BENIH.md`: SD pemilihan 4.15 mata/tahun pada 8 slot; kelebihan 20 mata/tahun perlu ~122 sesi untuk dilihat, 10 mata ~489 sesi (`laporan/BANDING_SPUS.md`).
- "Pada MDD -10%" = pulangan jika pendedahan dikecilkan (baki tunai) sehingga MDD tepat -10%, toleransi pengguna. Membanding pada MDD yang sama ialah satu-satunya bandingan adil dengan SPUS.
- Lajur T4 = teras SPUS + satelit kaedah, imbang bulanan. Nisbah CAGR/MDD SPUS+tunai hampir pemalar merentas berat (`REVERSE/SISTEM.md`), jadi berat ialah soalan toleransi drawdown, bukan soalan data.
- Kawalan rawak diambil daripada SELURUH kolam (Mxx + Nxx), jadi kaedah yang dibeli dalam tingkap menaik dibanding dengan pemilihan rawak dalam tingkap SAMA, bukan dengan sifar.

