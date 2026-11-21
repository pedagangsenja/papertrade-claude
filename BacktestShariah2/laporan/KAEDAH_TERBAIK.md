# Kaedah mana terbaik buat masa sekarang?

> **Status keputusan (kad skor, harga 2026-11-19):** TERBUKTI 0 · CALON 0 · BELUM CUKUP 225 · GAGAL 1 · NEGATIF 0. Rejim QQQ OFF sejak 2026-10-16. Hanya **TERBUKTI** layak untuk wang sebenar (`laporan/KAD_SKOR.md`); nombor dalam laporan ini BUKAN keputusan dan tidak boleh dibaca sebagai pangkat untuk wang sebenar.

> Ujian dalam laporan ini memakai posisi DITUTUP sahaja dengan SE berkelompok ikut hari beli. Ujian plasebo 7 Nov 2026 (`laporan/PLASEBO_GATE.md`) mengukur SE jenis itu meluluskan pemilihan rawak sehingga 45% masa, dan penapisan keluar memesongkan sampel ditutup. Bilangan "terbukti NEGATIF/positif" di bawah ialah DIAGNOSTIK, bukan label kaedah; label yang sah hanya dalam kad skor.

Dijana 2026-11-21 09:55 UTC oleh `standard/kaedah_terbaik.py`. Rekod analisis sahaja.

Papan Penganalisis (`laporan/PENGANALISIS.md`) sudah membanding semua kaedah dan dijana semula setiap malam. Dokumen ini tidak mengulanginya — ia menjawab soalan yang mesti dijawab **dahulu** sebelum mana-mana pangkat boleh dipercayai.

**REVERSE menguji signal/indikator, BUKAN kaedah Mxx** (`CLAUDE.md`). Keputusan REVERSE tidak terpakai di sini. Ini populasi berasingan.

## 1. Jawapan pendek

**2 kaedah lulus ujian itu — tetapi baca bahagian 3a sebelum mempercayainya.** Daripada 157 kaedah yang mempunyai cukup posisi ditutup untuk diuji, **131 terbukti NEGATIF** pada BH-FDR q ≤ 0.05 dengan ralat piawai berkelompok ikut hari beli, dan **2 terbukti positif**.

Itu bukan bermakna semua kaedah buruk. Ia bermakna tingkap hadapan masih terlalu pendek, dan bahagian 2 menunjukkan mengapa pangkat yang anda lihat sekarang tidak boleh diguna.

## 2. Adakah pangkat backtest meramal prestasi hadapan?

Korelasi mentah jangkaan backtest lawan pulangan realisasi Papertrade C merentas **126 kaedah**: Spearman rho **-0.714**, p 0.0000.

Negatif. Dibaca mentah, itu bermakna kaedah dengan backtest LEBIH BAIK berprestasi LEBIH BURUK ke hadapan — dan itu akan menjadi dapatan yang besar. **Ia salah.**

Jangkaan backtest berkorelasi **+0.873** dengan hari pegang backtest — sepele: pegang lebih lama memberi pulangan lebih besar setiap dagangan. Dan dalam tingkap hadapan 3 minggu, kaedah pegang-panjang belum ada masa untuk berfungsi.

| Korelasi | rho | p |
|---|---|---|
| Mentah: backtest → realisasi | **-0.714** | 0.0000 |
| Separa, kawal lebar henti | -0.685 | 0.0000 |
| **Separa, kawal hari pegang** | **-0.083** | **0.3571** |

Mengawal hari pegang, korelasi bertukar daripada -0.714 kepada **-0.083** dan **tidak lagi signifikan** (p 0.357). Jadi tanda negatif itu **artifak panjang tingkap**, bukan bukti pangkat terbalik.

**Kesimpulan bahagian ini:** pangkat backtest tidak mempunyai kuasa ramalan yang boleh diukur pada data hadapan sekarang — tidak positif, tidak negatif. Jadi "kaedah teratas papan" bukan jawapan kepada "kaedah terbaik".

## 3. Ada kaedah yang positif secara boleh ukur?

Ujian: purata pulangan realisasi setiap kaedah dengan ≥ 20 posisi ditutup, t dengan ralat piawai **berkelompok ikut hari beli** (posisi hari sama bergerak bersama pasaran), BH-FDR q ≤ 0.05 merentas 157 kaedah yang diuji.

| Kaedah | n | Hari beli | Realisasi | Median | Menang | t | p | FDR | Backtest hari |
|---|---|---|---|---|---|---|---|---|---|
| `M136` Short/Intermediate-term Lo | 129 | 26 | -10.35% | -9.77% | 0% | -21.4 | 0.0000 | **lulus** | 343.2 |
| `M80` Radge Saluran Purata Berge | 114 | 28 | -10.72% | -9.91% | 1% | -18.8 | 0.0000 | **lulus** | 65.9 |
| `M88` O'Neil Shakeout +3 | 57 | 21 | -8.07% | -8.00% | 2% | -29.2 | 0.0000 | **lulus** | 32.2 |
| `M54` IBD Power Trend | 124 | 27 | -6.72% | -6.11% | 1% | -17.9 | 0.0000 | **lulus** | 36.8 |
| `M79` Radge: 20% Flipper | 95 | 23 | -12.00% | -12.94% | 1% | -19.3 | 0.0000 | **lulus** | 59.8 |
| `M147` Improved Three-Bar Pullbac | 47 | 16 | -14.62% | -14.81% | 0% | -30.0 | 0.0000 | **lulus** | 441.7 |
| `M102` Stockbee SLTB | 216 | 31 | -3.48% | -2.80% | 1% | -13.4 | 0.0000 | **lulus** | 15.6 |
| `M55` Guppy GMMA | 166 | 28 | -6.06% | -4.83% | 0% | -14.0 | 0.0000 | **lulus** | 28.2 |
| `M12` Parabolic SAR | 165 | 29 | -5.97% | -5.02% | 5% | -12.7 | 0.0000 | **lulus** | 23.2 |
| `M36` Turtle 55/20 | 157 | 29 | -7.45% | -6.12% | 1% | -12.6 | 0.0000 | **lulus** | 29.6 |

**131 daripada 157 kaedah terbukti negatif; 2 terbukti positif.** Jadual di atas 10 teratas ikut p.

Calon positif terbaik ialah `M01` Bollinger Band + RSI: **+12.08%** atas 31 posisi ditutup merentas 14 hari beli, kadar menang 100%, median +9.00%, t +6.01, p 0.0000.

Ia **bertahan** pembetulan pelbagai ujian (p 0.0000 ≤ ambang BH 0.0226 merentas 157 kaedah). Itu syarat statistik sahaja; bahagian 3a menunjukkan mengapa ia masih belum boleh dibaca sebagai kelebihan.

### 3a. HAD YANG MENGIKAT: ujian ini melihat posisi DITUTUP sahaja

Peraturan keluar itu sendiri yang memilih posisi mana ditutup dahulu, jadi sampel "ditutup" **bukan** sampel rawak bagi dagangan kaedah — dan arah biasnya bergantung pada jenis keluar:

- Kaedah ber**sasaran untung** keluar awal bila MENANG; yang rugi kekal terbuka. Purata ditutupnya terlebih tinggi.
- Kaedah ber**henti ketat** keluar awal bila RUGI; yang menang kekal terbuka. Purata ditutupnya terlebih rendah.

Diukur pada Lejar Penuh (6 Nov 2026), tanda bertukar antara dua kumpulan itu pada kaedah yang sama:

| Kaedah | Ditutup | Purata ditutup | Terbuka | Purata terbuka |
|---|---|---|---|---|
| `M82` sasaran 10% | 122 | **+4.19%** (menang 61%) | 359 | **−0.57%** |
| `M15` henti ATR ketat | 108 | **−4.18%** (menang 6.5%) | 130 | **+9.48%** |
| `M33` Supertrend + SMA10 | 23 | **−10.27%** (menang 4.3%) | 133 | **+7.66%** |

Jadi mana-mana kaedah bersasaran yang muncul positif di sini, dan mana-mana kaedah berhenti-ketat yang muncul negatif, mesti dibaca sebagai **artifak penapisan keluar** sampai posisi terbukanya tutup. Jawapan yang sah ialah **kad skor** (`laporan/KAD_SKOR.md`): lift masuk ufuk tetap yang lulus ujian plasebo (`laporan/LIFT_KAEDAH.md`, `laporan/PLASEBO_GATE.md`). Laporan ini tidak memberi status kaedah.

## 4. Mengapa separuh papan belum boleh dinilai

| Kumpulan backtest | Kaedah | Posisi masih terbuka | Realisasi purata | Positif |
|---|---|---|---|---|
| pegang ≤ 10 hari | 20 | 13% | -1.91% | 0/18 |
| pegang 11–20 hari | 27 | 25% | -4.13% | 0/26 |
| pegang > 20 hari | 83 | 47% | -7.72% | 2/55 |

Kaedah pegang-panjang mempunyai **47% posisi masih terbuka**, jadi "realisasi" bagi mereka hanyalah himpunan posisi yang dihentikan awal — yang paling buruk daripada taburan. Angka itu bukan prestasi kaedah; ia prestasi hentinya dalam tiga minggu.

## 5. "Setiap kaedah ada sebab musabab daripada pakar" — ya, dan ini yang diukur

Premis itu betul: kaedah ini datang daripada pedagang yang berjaya dengannya. Tetapi repo ini sudah menguji versi mekanikalnya di luar sampel, dan hasilnya:

- Lulus S1–S4: **6** daripada 232 kaedah
- Lulus WFO 2023–2026: **22**
- Lulus AUTOTUNE 2000 saham AS 2013–2024: **0**
- Lulus **≥ 2 daripada 3**: **0**

Semakan 2000-saham-AS ialah yang paling menuntut kerana ia menguji kaedah LENGKAP (masuk + keluar + henti) pada alam dan tempoh yang tidak pernah dilihat. **0 kaedah melepasinya.**

**Had yang jujur, dan ia penting:** kaedah ini ialah **anggaran mekanikal** bagi kaedah yang asalnya mempunyai pertimbangan manusia — pemilihan saham, saiz, masa keluar, keadaan pasaran yang tidak dikodkan. `spec/SPEC_SEMUA_KAEDAH.md` menanda `FAIL ASAL` di tempat spec asal tidak dapat ditentukan. Jadi kegagalan di sini bermakna "versi mekanikal kami tidak berfungsi pada alam kami", **bukan** "pakar itu salah". Perbezaan itu nyata dan saya tidak boleh merapatkannya dengan data yang ada.

## 6. Bila pangkat kaedah boleh dipercayai

Sisihan piawai pulangan setiap posisi (median dalam-kaedah): **6.25 mata**.

| Untuk membezakan dua kaedah yang berbeza | Perlu posisi DITUTUP setiap kaedah |
|---|---|
| 3.0 mata setiap posisi | ~34 |
| 2.0 mata setiap posisi | ~76 |
| 1.0 mata setiap posisi | ~306 |
| 0.5 mata setiap posisi | ~1,224 |

Sekarang: median **49** posisi ditutup setiap kaedah, maksimum **258**. Jadi perbezaan bawah ~2 mata setiap posisi belum boleh dilihat bagi hampir semua kaedah.

## 7. Syor

1. **Jangan pilih kaedah sekarang.** Pangkat backtest tiada kuasa ramalan yang boleh diukur (bahagian 2); mana-mana kaedah yang kelihatan positif pada posisi ditutup tertakluk kepada penapisan keluar (bahagian 3a), dan lift yang dipadan ikut hari beli tidak bertahan BH-FDR bagi satu kaedah pun.
2. **Betulkan kecacatan henti hari-0 dahulu.** `REVERSE/KOLAM_EKOR.md` §4a: 421 daripada 1,770 posisi dibeli dan dihentikan pada hari masuk dengan kadar menang 0.00% kerana paras henti terletak dalam julat intrabar hari masuk. Itu bukan prestasi kaedah, itu pepijat pelaksanaan, dan ia mencemari setiap pangkat di atas.
3. **Perhatikan kaedah pegang-pendek dahulu.** Hanya kumpulan ≤ 10 hari ada data yang hampir matang (13% masih terbuka lawan 47% bagi pegang-panjang). Pangkat pegang-panjang tidak bermakna sebelum satu tempoh pegang penuh berlalu.
4. **Baca semula selepas 6 bulan.** Papan dijana semula setiap malam tanpa kos. Jadual bahagian 6 memberi bilangan posisi yang diperlukan.

**Ia tidak akan mencapai +10%/bulan.** Kaedah teratas papan ikut skor sebulan memberi +3.40% dengan status BELUM CUKUP dan 0 posisi hadapan matang. Lihat `REVERSE/SASARAN.md`.
