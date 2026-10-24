# Log formula Papan Penganalisis

Setiap perubahan cara skor, kedudukan, status, pantau atau P(5 teratas) dikira mesti menaikkan `VERSI_FORMULA` dalam
`standard/penganalisis.py` dan menambah satu baris di bawah (`- vX.Y (YYYY-MM-DD): perubahan`). Papan memaparkan versi dan cap
jari formula (`formula.cap`); jika cap berubah antara dua sesi, tab Kaedah menanda "formula berubah" dan anak panah kedudukan
dibuang, supaya perubahan kedudukan kerana formula tidak disangka perubahan prestasi.

- v1.0 (2026-10-20): Papan Penganalisis asal: skor gabungan backtest dipotong (25% + 25% bagi setiap semakan luar sampel) dan posisi hadapan matang.
- v2.0 (2026-10-22): kukuh: purata matang penuh, n berkesan ikut hari beli, BELUM CUKUP < 10 hari beli, label pantau (BERSARA/GANTUNG/AMARAN).
- v3.0 (2026-10-24): ranking tunggal: P(5 teratas) dan pangkat 90% Monte Carlo, meter bukti, tarikh keluar BELUM CUKUP, ekor, kelompok; pantau v3 (sasaran winsor, ambang bergulir, CUSUM k 0.25, bootstrap blok bulanan, pengawal bukti).
- v3.1 (2026-10-24): medan bukti bebas AUTOTUNE (ujian bersih 2013–2018, tempoh kunci, DSR, PBO); pintu wang sebenar di halaman.
