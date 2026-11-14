# Portfolio 10 slot bagi setup berprasyarat (backtest pada saham yang tidak dilihat; BUKAN bukti)

> **Status keputusan (kad skor, harga 2026-11-12):** TERBUKTI 0 · CALON 0 · BELUM CUKUP 223 · GAGAL 0 · NEGATIF 0. Rejim QQQ OFF sejak 2026-10-16. Hanya **TERBUKTI** layak untuk wang sebenar (`laporan/KAD_SKOR.md`); nombor dalam laporan ini BUKAN keputusan dan tidak boleh dibaca sebagai pangkat untuk wang sebenar.

Dijana `kajian/carian_setup/cs_portfolio6.py`. Pradaftar: `kajian/SPEC_CARIAN_SETUP.md` pindaan 14 Nov 2026 (l), dikomit sebelum dijalankan. **Jangan sunting secara manual.**

Soalan: isyarat setup berprasyarat datang berkelompok. Jika akaun hanya ada **10 slot** (10 % setiap satu), berapa banyak isyarat yang sempat diambil, dan bagaimana hasil akaun? Kumpulan B, 20100104 – 20260828 (16.6 tahun); kos 0.5 % pusingan; tunai 0 %; isyarat berlebihan dipilih rawak, diulang 200 kali (angka = median). **Jalur rawak** = isyarat yang sama digantikan saham rawak pada hari dan tahap turun-naik yang sama, dengan henti dan keluar yang sama.

## 1. Akaun

| Setup | Isyarat | Diambil | Dagangan setahun | Bulan tanpa belian | Pendedahan purata % | CAGR % | MDD % | **CAGR pada MDD −10 %** | Jalur rawak: median (p5 – p95) | Kedudukan dalam jalur | Tahun positif | Tahun terburuk % | K3: CAGR % / MDD % | Menambah di peringkat akaun? |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `F39` | 547 | 332 (61 %) | 20 | 64 % | 12 | +0.5 | -29.6 | **+0.27** | +0.65 (-0.25 – +2.54) | persentil ke-32 | 8 / 17 | -12.8 | -13.8 / -24.8 | **TIDAK** |
| `F40` | 731 | 373 (51 %) | 22 | 62 % | 14 | +3.1 | -24.3 | **+1.41** | +0.17 (-0.40 – +1.32) | persentil ke-97 | 11 / 17 | -3.4 | +1.5 / -17.2 | **YA** |
| `F58` | 386 | 334 (87 %) | 20 | 56 % | 12 | +0.1 | -33.4 | **+0.15** | -0.04 (-0.51 – +0.75) | persentil ke-68 | 9 / 17 | -20.5 | +4.8 / -14.6 | **TIDAK** |
| `F49` | 1,130 | 258 (23 %) | 16 | 78 % | 10 | +8.9 | -24.7 | **+3.74** | +1.17 (+0.40 – +2.41) | persentil ke-100 | 12 / 17 | -0.8 | +15.0 / -16.6 | **YA** |
| `PILIH3` | 1,664 | 645 (39 %) | 39 | 39 % | 23 | +1.0 | -36.3 | **+0.48** | -0.01 (-0.51 – +0.94) | persentil ke-78 | 10 / 17 | -20.1 | -7.1 / -25.2 | **TIDAK** |
| `SEMUA4` | 2,794 | 820 (29 %) | 49 | 29 % | 30 | +7.2 | -40.3 | **+2.01** | +0.51 (-0.17 – +1.49) | persentil ke-100 | 12 / 17 | -20.1 | +4.8 / -26.0 | **YA** |

- "CAGR pada MDD −10 %" = pendedahan dikecilkan (baki tunai) sehingga kejatuhan terburuk akaun kira-kira −10 %, iaitu toleransi pengguna. **Bacaan dikunci:** "menambah" hanya jika angka itu positif DAN melebihi persentil ke-95 jalur rawak.
- Maklumat sahaja (bukan kayu ukur): SPY beli-dan-pegang pada MDD −10 % = +4.37 % setahun (CAGR +14.3 %, MDD -33.7 %).

## 2. Dagangan yang benar-benar diambil akaun

Setiap sel: setup (jalur rawak, median). Tangkap penuh = naik ≥ 5 % minggu pertama DAN dijual dengan untung ≥ 10 %.

| Setup | Tangkap penuh % | Jadi (dijual ≥ +10 %) % | Menang % | Rugi ≥ 8 % % | Purata setiap dagangan % |
|---|---|---|---|---|---|
| `F39` | **18.4** (7.7) | 22.9 (18.0) | 47 (50) | 37.8 (26.1) | +0.15 (+0.64) |
| `F40` | **19.6** (7.1) | 26.6 (16.2) | 49 (49) | 34.8 (26.8) | +1.36 (+0.20) |
| `F58` | **21.9** (7.5) | 29.0 (16.6) | 45 (47) | 37.9 (27.8) | +0.29 (-0.11) |
| `F49` | **29.5** (18.0) | 41.2 (29.9) | 64 (56) | 22.1 (25.2) | +5.98 (+2.27) |
| `PILIH3` | **19.6** (6.9) | 25.3 (16.1) | 47 (47) | 37.9 (27.4) | +0.37 (-0.01) |
| `SEMUA4` | **21.7** (9.5) | 28.8 (19.2) | 51 (49) | 34.4 (27.0) | +1.64 (+0.44) |

## 3. Bacaan

- Menambah di peringkat akaun (bacaan dikunci): `F40`, `F49`, `SEMUA4`.
- Kadar tangkap pada belian yang diambil lawan jalur rawak menunjukkan sama ada kelebihan memilih saham kekal selepas had slot; lajur akaun menunjukkan sama ada kelebihan itu cukup besar untuk kelihatan pada wang.

## 4. Kaveat

- Tiada saham delist (condong ke atas); set 2000 bukan tapisan Shariah; prasyarat earnings memakai tarikh sebenar.
- Kumpulan B sudah dilihat dalam CS05 dan CS06; setup ini dipilih kerana kedudukannya di papan, jadi angka ini bukan ujian bebas. Satu akaun 10 slot ialah satu cara membina portfolio, bukan satu-satunya.
- Backtest sahaja. Tiada jejak hadapan, tiada order; kad skor kekal satu-satunya keputusan wang sebenar.
