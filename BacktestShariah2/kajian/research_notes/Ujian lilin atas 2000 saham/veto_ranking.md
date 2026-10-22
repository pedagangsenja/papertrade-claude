# Ujian 1, 3 dan 4: ciri bar sebagai lapisan VETO atau RANKING atas isyarat kaedah sedia ada (AUTOTUNE, 2000 saham AS)

Nota ini ialah hasil pengiraan sendiri atas kolam isyarat ([kolam_isyarat.md](kolam_isyarat.md)), bukan sumber web. Setiap angka dirujuk kepada skrip dan fail output. Latar belakang: laporan [Jenis lilin dan carta alternatif](../../reports/Jenis%20lilin%20dan%20carta%20alternatif.md), bahagian "Uji lima perkara", dan nota [penapis_ranking.md](../Jenis%20lilin%20dan%20carta%20alternatif/penapis_ranking.md).

## Soalan 1: Apakah reka bentuk yang didaftarkan sebelum melihat hasil, dan adakah simulator portfolio sah?

### Takeaway
(Diisi selepas larian.)

### Cited Findings

**Pra-pendaftaran (ditulis 22 Okt 2026 sebelum sebarang hasil ujian dikira; tidak diubah selepas itu).**

Sampel:
- SELECT = kumpulan A, tarikh isyarat 2013-01-01 hingga 2021-12-31.
- VALIDATE-B = kumpulan B, tempoh sama.
- VALIDATE-2022 = kumpulan A + B, tarikh isyarat 2022-01-01 hingga hujung kolam (15 Okt 2026).

Set dagangan peringkat dagangan (utama): dagangan enjin laluan 1 (`dagangan_enjin == True`) dengan `trade_ret` bukan NaN. Baris laluan ≥ 2 kaedah `ikut_laluan` (NaN) dikecualikan. Laluan 1 tidak bertindih bagi ticker yang sama, jadi lebih bebas daripada semua isyarat (M167 berulang setiap hari). Semakan kepekaan: semua isyarat dengan `trade_ret` bukan NaN, metrik utama sahaja.

Metrik peringkat dagangan (dikira dalam setiap kaedah, kemudian dipuratakan dengan pemberat sama antara kaedah; kaedah dimasukkan bagi satu sel jika kedua-dua belah perbandingan mempunyai ≥ 20 dagangan dalam sampel itu):
- `lebih_pegang` (UTAMA) = trade_ret − pulangan SPY sepanjang pegangan. SPY: buka hari masuk hingga tutup hari keluar; jika sebab keluar `isyarat keluar` (keluar pada buka), hingga buka hari keluar.
- `lebih20` = fwd20 − spy20 (sekunder).
- kadar menang (trade_ret > 0), 5% terburuk (persentil 5 trade_ret).
- t perbezaan (disimpan − diveto, atau atas − bawah) bagi `lebih_pegang`: ralat piawai berkelompok ikut tarikh isyarat, melalui fungsi pengaruh penganggar purata sama-pemberat antara kaedah (setiap pemerhatian menyumbang ±(x − purata sel kaedahnya) / (n sel × bilangan kaedah); jumlah setiap tarikh dikuasaduakan; faktor G/(G−1)).
- hari beli berbeza (tarikh masuk unik) bagi setiap sel, dikumpul antara kaedah.

Ujian 1 (veto lonjakan/perhatian; 6 varian; veto = buang isyarat itu):
- V1 `atas1pct_1t == 1` (hari isyarat dalam 1% teratas pulangan harian 252 hari sendiri).
- V2 `max20 ≥ p90`, V3 `max20 ≥ p95`; p90/p95 dikira atas baris unik ticker × tarikh isyarat sampel SELECT (bukan seluruh kolam, supaya tiada maklumat VALIDATE).
- V4 `gap_atr ≥ 1`, V5 `gap_atr ≥ 2`.
- V6 `rcc_srs60 > 3` (takrif asal laporan: r_cc > 3 × σ Rogers-Satchell 60 hari).
- Perbandingan peringkat dagangan: disimpan − diveto.

Ujian 3 (pecahan semalaman/intrahari sebagai kunci ranking; 6 varian):
- R1 `id_share20` TINGGI dahulu, R2 `id_share20` RENDAH dahulu, R3 `id_share60` TINGGI dahulu, R4 `id_share60` RENDAH dahulu. Peringkat dagangan: tercil atas − tercil bawah (R2/R4 = tanda bertentangan). Sempadan tercil dikira dalam setiap kaedah atas sampel SELECT dan dipakai pada semua sampel.
- R5 `id_share20` dalam tercil RS, R6 `id_share60` dalam tercil RS. Tercil RS = `rs12_pct` < 1/3, 1/3–2/3, ≥ 2/3 (sudah persentil keratan rentas). Peringkat dagangan: purata sama-pemberat (atas − bawah) dalam tiga tercil RS. Arah R5/R6 ditetapkan oleh tanda R1 (atau R3) dalam SELECT sahaja.

Ujian 4 (volum dan paras tertinggi 52 minggu; 8 varian; semua arah TINGGI dahulu):
- B1 `hijau_vol90` bonus (C > O dan vol_pctl50 ≥ 0.9; takrif laporan). Peringkat dagangan: bendera 1 − 0.
- B2 `vol_pctl50` (tercil atas − bawah).
- B3 `h52` (tercil atas − bawah).
- B4 `h52 ≥ 0.95` bonus (bendera 1 − 0).
- B5 `h52_industri` (tercil atas − bawah; peta industri semasa, bukan titik masa).
- B6 `h52` dalam tercil RS, B7 `h52_industri` dalam tercil RS, B8 `hijau_vol90` dalam tercil RS.

Portfolio (setiap kaedah, setiap kumpulan A/B, 8 slot × 12.5%, `enjin_at._portfolio` melalui `Pasaran.lengkung`, tetingkap 2013-01-01 hingga hujung, sama seperti `pegang8`):
- Rantai dagangan dibina semula daripada kolam: bagi setiap ticker, isyarat (bukan NaN, tidak diveto) diambil mengikut tarikh; isyarat seterusnya hanya sah jika tarikh isyaratnya > tarikh keluar dagangan sebelumnya (peraturan `_trades`: `i = j + 1`). Tanpa veto, rantai ini mesti sama dengan laluan 1.
- Veto: isyarat diveto dibuang sebelum rantai dibina (isyarat laluan ≥ 2 boleh menggantikannya). Bagi `ikut_laluan` (M20, M26, M41, M78), isyarat NaN tidak boleh menggantikan; ini anggaran.
- Ranking: rantai laluan 1 tidak berubah; susunan calon pada hari masuk yang sama diganti dengan kunci baharu (R1–R4, B2, B3, B5: ciri menggantikan `rank_value`; B1, B4: bendera dahulu, kemudian `rank_value`; R5, R6, B6–B8: tercil RS dahulu, kemudian ciri). Bagi R5, R6, B6–B8, kawalan = tercil RS dahulu kemudian `rank_value`, dan perubahan dilapor berbanding kawalan dan garis dasar.
- Metrik setiap sampel daripada keratan lengkung: SELECT = lengkung A 2013–2021; VALIDATE-B = lengkung B 2013–2021; VALIDATE-2022 = purata metrik lengkung A dan B 2022-01-01 hingga hujung. CAGR = nisbah ekuiti (dinormalkan pada hari sebelum tetingkap)^(365.25/(hari kalendar+1)) − 1; MDD termasuk modal awal (formula `AUTOTUNE/teras/objektif.py`).
- Pengesahan simulator dahulu: rantai tanpa veto lawan laluan 1, ahli portfolio lawan bendera `pegang8`, dan CAGR/MDD lawan lengkung enjin atas dagangan laluan 1 kolam terus. Toleransi dilapor.

Peraturan lulus (setiap varian): (i) perbezaan `lebih_pegang` > 0 dalam ketiga-tiga sampel; (ii) t > 3 dalam SELECT; (iii) ≥ 10 hari beli berbeza dalam setiap sel; (iv) 5% terburuk set disimpan/atas tidak lebih buruk > 1 mata peratus berbanding semua dagangan (purata kaedah) dalam mana-mana sampel; (v) majoriti kaedah (> 50%) memperbaiki CAGR portfolio berbanding garis dasar (atau kawalan) dalam ketiga-tiga sampel. Jika mana-mana gagal, varian GAGAL. Hasil M167 dan kaedah breakout (M04, M30, M33, M79, M135) dilapor berasingan.

(Hasil di bawah diisi selepas larian.)
