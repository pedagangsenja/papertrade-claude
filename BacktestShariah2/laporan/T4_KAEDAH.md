# Lorong T4 satu-kaedah (jejak hadapan; rekod sahaja)

Dijana 2026-11-28 11:41 UTC oleh `standard/portfolio_t4.py` (Actions `analisis.yml`). Tiada order, tiada wang sebenar. Jangan ubah secara manual.

> **Status keputusan (kad skor, harga 2026-11-25):** TERBUKTI 0 · CALON 0 · BELUM CUKUP 225 · GAGAL 2 · NEGATIF 0. Rejim QQQ OFF sejak 2026-10-16. Hanya **TERBUKTI** layak untuk wang sebenar (`laporan/KAD_SKOR.md`); nombor dalam laporan ini BUKAN keputusan dan tidak boleh dibaca sebagai pangkat untuk wang sebenar.

Sesi terakhir 2026-11-27. **227 kaedah**, setiap satu dua lorong (L1 = keluar kaedah, L2 = Chandelier 4xATR14). Kawalan: 20 cabutan rawak 10 slot atas seluruh kolam Lejar, diasas semula pada tarikh mula setiap lorong. Penanda aras: SPUS, asas buka sesi pertama.

## Gate G6 (dikunci dalam `standard/kad_skor.py`)

Lorong L1 mesti (pindaan 7 Nov 2026): sesi >= 126; pulangan > 0; pulangan pada MDD -10% > SPUS pada MDD sama; nisbah pulangan/|MDD| > maksimum jalur rawak. 
**0 lulus.** Lorong paling lama ada 30 sesi; G6 tidak boleh lulus sebelum 126 sesi (anggaran 2027-04-12).

## 15 lorong L1 teratas ikut pulangan (BUKAN pangkat: semuanya BELUM CUKUP sehingga G6 dinilai)

| Kaedah | Mula | Sesi | Pul % | MDD % | Berat utk MDD -10% | Pul pada MDD -10% | SPUS pada MDD -10% | Nisbah pul/MDD | Maks jalur | T4 70/30 % |
|---|---|---|---|---|---|---|---|---|---|---|
| `M159` | 2026-10-16 | 30 | +11.22 | -6.13 | 1.00 | +11.22 | -7.49 | 1.83 | 1.22 | -3.57 |
| `M10` | 2026-10-16 | 30 | +11.10 | -6.59 | 1.00 | +11.10 | -7.49 | 1.68 | 1.22 | -3.69 |
| `M48` | 2026-10-16 | 30 | +11.05 | -5.73 | 1.00 | +11.05 | -7.49 | 1.93 | 1.22 | -3.65 |
| `M146` | 2026-10-16 | 30 | +8.30 | -7.02 | 1.00 | +8.30 | -7.49 | 1.18 | 1.22 | -4.49 |
| `M13` | 2026-10-16 | 30 | +8.22 | -6.63 | 1.00 | +8.22 | -7.49 | 1.24 | 1.22 | -4.51 |
| `M33` | 2026-10-16 | 30 | +8.05 | -7.28 | 1.00 | +8.05 | -7.49 | 1.11 | 1.22 | -4.56 |
| `M137` | 2026-10-16 | 30 | +8.02 | -5.91 | 1.00 | +8.02 | -7.49 | 1.36 | 1.22 | -4.53 |
| `M151` | 2026-10-16 | 30 | +7.93 | -4.00 | 1.00 | +7.93 | -7.49 | 1.98 | 1.22 | -4.57 |
| `M39` | 2026-10-16 | 30 | +6.98 | -6.53 | 1.00 | +6.98 | -7.49 | 1.07 | 1.22 | -4.85 |
| `M160` | 2026-10-16 | 30 | +6.79 | -5.75 | 1.00 | +6.79 | -7.49 | 1.18 | 1.22 | -4.90 |
| `M118` | 2026-10-16 | 30 | +6.76 | -8.32 | 1.00 | +6.76 | -7.49 | 0.81 | 1.22 | -4.92 |
| `M145` | 2026-10-16 | 30 | +5.92 | -3.87 | 1.00 | +5.92 | -7.49 | 1.53 | 1.22 | -5.11 |
| `M70` | 2026-10-16 | 30 | +5.81 | -5.77 | 1.00 | +5.81 | -7.49 | 1.01 | 1.22 | -5.16 |
| `M25` | 2026-10-16 | 30 | +5.60 | -7.99 | 1.00 | +5.60 | -7.49 | 0.70 | 1.22 | -5.25 |
| `M54` | 2026-10-16 | 30 | +4.52 | -10.41 | 0.96 | +4.34 | -7.49 | 0.43 | 1.22 | -5.52 |

## Cara membaca

- Pulangan beberapa sesi ialah hingar. `REVERSE/KEPEKATAN_BENIH.md`: SD pemilihan 4.15 mata/tahun pada 8 slot; kelebihan 20 mata/tahun perlu ~122 sesi untuk dilihat, 10 mata ~489 sesi (`laporan/BANDING_SPUS.md`).
- "Pada MDD -10%" = pulangan jika pendedahan dikecilkan (baki tunai) sehingga MDD tepat -10%, toleransi pengguna. Membanding pada MDD yang sama ialah satu-satunya bandingan adil dengan SPUS.
- Lajur T4 = teras SPUS + satelit kaedah, imbang bulanan. Nisbah CAGR/MDD SPUS+tunai hampir pemalar merentas berat (`REVERSE/SISTEM.md`), jadi berat ialah soalan toleransi drawdown, bukan soalan data.
- Kawalan rawak diambil daripada SELURUH kolam (Mxx + Nxx), jadi kaedah yang dibeli dalam tingkap menaik dibanding dengan pemilihan rawak dalam tingkap SAMA, bukan dengan sifar.

