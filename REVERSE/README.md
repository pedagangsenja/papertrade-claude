# REVERSE — reverse engineer saham padu US (ENTRY / HOLD / EXIT)

Kajian **signal dan indikator**, bukan kaedah Mxx repo dan bukan penalaan parameter. Tiada Optuna.
Arah terbalik daripada backtest: **hasil dahulu, signal kemudian**.

- Spec dikunci sebelum larian pertama: **`SPEC.md`** (termasuk 9 pindaan bertarikh 27 Okt 2026).
- Laporan setiap tahun: **`LAPORAN_2025.md`**, **`LAPORAN_2024.md`**, **`LAPORAN_2023.md`**, **`LAPORAN_2022.md`**, **`LAPORAN_2021.md`**, **`LAPORAN_2020.md`** (dijana `jana_laporan.py`).
- Setiap signal/kombinasi yang diuji: `log_ujian.csv`.
- Imbasan pandang ke hadapan: `PANDANG_HADAPAN_<TAHUN>.md` (14 tarikh potong setiap tahun, 0 kegagalan).
- Perbandingan merentas tahun: **`BANDING_TAHUN.md`** (dijana `banding_tahun.py`).
- Jadual keputusan satu baris setiap tahun: **`JADUAL_KEPUTUSAN.csv`** (dijana `jadual_keputusan.py`).

## Jalankan semula (urutan)

```
python3 REVERSE/semak_hadapan.py 2025             # kesediaan 0.3f
python3 REVERSE/step1_run.py 2025                 # Step 1-2 + cache indikator  (~270 s)
python3 REVERSE/step2b_kohort.py 2025             # Step 2b                     (~30 s)
python3 REVERSE/step3_signal.py 2025              # kuintil dibeku + dedup      (~7 s)
python3 REVERSE/step4_common.py 2025              # Step 4 + corong             (~10 s)
python3 REVERSE/step5_6_hold_exit.py 2025         # Step 5-6 (CALON)            (~215 s)
python3 REVERSE/step7_false.py 2025               # Step 7                      (~40 s)
python3 REVERSE/step7b_hadapan.py 2025            # Step 7b, 234 sistem         (~25 s)
python3 REVERSE/step8_kawalan.py 2025             # Step 8                      (~105 s)
python3 REVERSE/step9_portfolio.py 2025           # Step 9 (kriteria akhir)      (~20 s)
python3 REVERSE/jana_laporan.py 2025
python3 REVERSE/banding_tahun.py                  # selepas >= 2 tahun siap
```

Tahun lain: kod dan parameter **sama tanpa ubah**, universe ikut bulan tahun itu —
tukar sahaja argumen tahun pada setiap skrip. Jangan ubah `SPEC.md` kecuali sebagai pindaan
bertarikh. Siap setakat ini: **2025, 2024, 2023, 2022, 2021, 2020**. Universe 2021-2025 ialah 2000 saham sebulan; **2020 lebih kecil (1638/1832/1940 min/median/maks)**, jadi bilangan mutlaknya tidak setara dan laporan 2020 membawa kaveat saiz universe.

## Data

Harga: Release GitHub `autotune-data-a02` melalui `AUTOTUNE/teras/data.py` `ambil()` — **jangan**
guna Release `autotune-data` (A01 membuang saham meruap). Cache tempatan `REVERSE/.cache/`
(dalam `.gitignore`; parquet dan fail per-hari TIDAK dicommit).

## Teras

| Modul | Isi |
|---|---|
| `teras/data.py` | universe titik-masa, harga A02, sektor/industri, indeks sektor berpemberat sama |
| `teras/ind.py` | 77 lajur indikator, tetapan standard, semua kausal |
| `teras/run.py` | definisi run, tarikh sah, kaki, jenis kenaikan, peristiwa sah kausal |
| `teras/keluar.py` | 13 signal EXIT grid sistem + 18 peraturan HOLD sebagai veto |
| `teras/signal.py` | binaan signal, dedup Spearman, senarai keutamaan tetap |
| `teras/stat.py` | lift/presisi, kelas, BH-FDR, permutasi label, bootstrap blok |
| `teras/kos.py` | komisen 0.1% + slippage ikut median nilai dagangan 20 hari |

## FASA 2 (27 Okt 2026) — pulangan boleh didagangkan dan ablasi 2×2

FASA 1 memberi lift 10–20× tetapi portfolio yang kalah kepada entri rawak. Puncanya ialah sasaran
kajian: `tarikh_puncak` (§4.3) dan `mfe63 ≥ 30%` (Step 7) ialah **maksimum pandang-belakang** dalam
tetingkap, jadi carian menumpu pada kemeruapan, bukan kelebihan boleh dagang. FASA 2 menukar sasaran
dan unit penilaian; data, universe, kos dan definisi indikator tidak berubah. Reka bentuk dikunci
dalam `SPEC.md` §13.12 B sebelum sebarang angka dilihat.

- **Laporan: [`FASA2.md`](FASA2.md)**; data `fasa2_jangkaan.csv`, `fasa2_portfolio.csv`,
  `fasa2_hold.csv`.
- Keputusan ringkas: 1 daripada 138 ujian lulus syarat ablasi (jangkaan nasib ≈ 7); pemilihan
  **rawak** daripada universe mengalahkan kesemua 46 signal pada median, kadar menang dan purata
  dipangkas; 0 daripada 282 kombinasi mencapai median +10% sebulan; kelas pullback sebagai
  peraturan jual merugikan.
- Data 2000–2010: [`DATA_2000.md`](DATA_2000.md) — tidak boleh dengan Release A02 (mula
  2009-01-02); pilihan vendor dan cadangan ada di sana.

```
python3 REVERSE/fasa2_kuintil.py <TAHUN>     # pilihan: bina semula cache laju (disahkan setara)
python3 REVERSE/fasa2_ablasi.py              # ablasi 2x2 + portfolio bergabung 2020-2025
python3 REVERSE/fasa2_hold.py                # kelas pullback sebagai peraturan jual
python3 REVERSE/fasa2_laporan.py             # jana FASA2.md
```

## Pembetulan pelaksanaan (SPEC §13.12 A)

1. `step9_portfolio.py` memilih `keputusan == 'CALON'` sahaja, jadi signal yang dinaik taraf ke
   DITERIMA terkeluar daripada asas entry. **2020 terjejas:** tahun itu mempunyai 3 DITERIMA dan
   3 CALON, jadi portfolio lama dibina atas 3 signal sahaja — `REF_chandelier_4atr` +82.15%
   sebenarnya **−9.01%** atas asas 6 signal yang betul (kawalan rawak kekal +102.84%). Lima tahun
   lain hanya label `asas_entry` yang bertukar. Butiran: `FASA2.md` §6.
2. `jangkaan_bulanan_anggaran` melaporkan jangkaan setiap dagangan (ufuk ≤ 63 hari) sebagai
   jangkaan sebulan — kira-kira 3× terlebih nyata. Diganti `jangkaan_per_21_hari`.
3. Penapis Step 7.4 tidak pernah dinilai atas pulangan; kini melaporkan `jangkaan_dengan_penapis`
   dan `delta_jangkaan`.
4. Kelas pullback dikira dengan dua peraturan berbeza bergantung pada hasil (pulih lawan tidak
   pulih). Satu peraturan sekarang; jurang SIHAT−AMARAN melebar, seperti dinyatakan lebih awal
   dalam pindaan.

## Had fasa

Gate 8.1 memerlukan kelas yang sama dalam **≥ 2 tahun LAIN**, dan (pindaan §13.11) kelas tahun itu
sendiri mesti TERAS/UNIQUE/LANGKA. Dengan enam tahun siap: **7 label DITERIMA** (3 pada 2020,
1 pada 2023, 3 pada 2025); 0 pada 2021, 2022 dan 2024.

**Baca amaran percanggahan dalam `BANDING_TAHUN.md` §7 sebelum menggunakan label itu.** Gate 8.1
seperti ditulis hanya memerlukan *kelas* yang sama, bukan *keputusan* yang sama; kedua-dua signal
DITERIMA itu sebenarnya DITOLAK pada 2022, 2023 DAN 2024 kerana gagal G4 (bootstrap) dan
G5 (outlier). Enam tahun, dan **tiada satu signal pun mengekalkan kelas TERAS/UNIQUE/LANGKA pada
kesemua enam tahun**.
Mengetatkan gate 8.1 ialah keputusan pengguna, bukan perubahan spec selepas melihat hasil.
