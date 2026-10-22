# Ujian 1, 3 dan 4: ciri bar sebagai lapisan VETO atau RANKING atas isyarat kaedah sedia ada (AUTOTUNE, 2000 saham AS)

Nota ini ialah hasil pengiraan sendiri atas kolam isyarat ([kolam_isyarat.md](kolam_isyarat.md)), bukan sumber web. Setiap angka dirujuk kepada skrip dan fail output. Latar belakang: laporan [Jenis lilin dan carta alternatif](../../reports/Jenis%20lilin%20dan%20carta%20alternatif.md), bahagian "Uji lima perkara", dan nota [penapis_ranking.md](../Jenis%20lilin%20dan%20carta%20alternatif/penapis_ranking.md).

## Soalan 1: Apakah reka bentuk yang didaftarkan sebelum melihat hasil, dan adakah simulator portfolio sah?

### Takeaway
Reka bentuk pra-daftar dikekalkan tanpa perubahan. Simulator portfolio disahkan **tepat**: rantai isyarat yang dibina semula sama dengan laluan 1, ahli portfolio sama dengan `pegang8` (beza 0 dalam 30/30 kaedah × kumpulan A/B), dan lengkung sama dengan beza 0. **Keputusan: 20 daripada 20 varian GAGAL.** Tiada varian mencapai t > 3 dalam SELECT; t tertinggi ialah 1.77 (V1). Hanya V1 dan R3 positif dalam ketiga-tiga sampel di peringkat dagangan.

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

**Hasil (diisi 22 Okt 2026 selepas larian; reka bentuk di atas tidak diubah).**

- Pra-daftar di atas di-commit sebelum sebarang hasil dikira (commit `7baf91e`, "pradaftar ujian veto/ranking dan lorong 3"). Larian pertama terhenti kerana bekas dimulakan semula. Tiada skrip atau fail hasil ujian daripada larian itu ditemui, jadi semua hasil di bawah dikira semula daripada awal.
- Skrip: [`BacktestShariah2/kajian/lilin/veto_ranking.py`](../../lilin/veto_ranking.py). Peringkatnya `sedia`, `dagangan`, `ujian`, `portfolio`, `laporan`, `khusus` dan `plasebo`. Setiap peringkat menulis checkpoint ke `/tmp/claude-0/-home-user-papertrade-claude/0793050f-2ee1-522e-9bf0-b633a13089db/scratchpad/lilin/`:
  - `vr_kolam.parquet`, `vr_dagangan_info.json` dan `vr_sempadan_tercil.json` (peringkat `dagangan`);
  - `vr_ujian.json` (peringkat dagangan, semua varian);
  - `vr_sah.json` dan `vr_port/<kaedah>.json` (portfolio);
  - `vr_jadual.md` (semua jadual);
  - `vr_khusus.md` (t setiap kaedah);
  - `vr_plasebo.md` (diagnostik rawak).
- Larian: `ujian` siap dalam 123 s; `portfolio` dalam beberapa minit. Satu proses sahaja; RSS maksimum 2.2 GB semasa `sedia` dan 1.1 GB semasa `dagangan`.
- **Butiran pelaksanaan yang tidak dinyatakan dalam pra-daftar.** Butiran ini ditetapkan semasa menulis skrip, sebelum hasil dilihat:
  - Ciri NaN tidak diveto. Dalam ranking, nilai NaN diletakkan terakhir.
  - Tercil: bawah = x ≤ q1/3 dan atas = x ≥ q2/3, dengan q dikira dalam kaedah atas dagangan laluan 1 SELECT. Kaedah dikecualikan jika q1 = q2.
  - Varian dalam tercil RS (R5, R6, B6–B8):
    - Sempadan tercil ciri dikira dalam (kaedah × tercil RS).
    - Strata (kaedah × tercil RS) layak jika setiap sisi ≥ 20 dagangan. Kaedah = purata strata layaknya, dan baris dengan rs12_pct NaN dikecualikan.
    - Dalam portfolio, susunannya tercil RS TINGGI dahulu, kemudian ciri, kemudian `rank_value`.
  - Dalam semua ranking portfolio, seri dipecahkan dengan `rank_value`.
  - Arah R5 dan R6 ditetapkan oleh SELECT: R1 SELECT = −0.16 mata, jadi R5 = id_share20 RENDAH dahulu. R3 SELECT = +0.12, jadi R6 = id_share60 TINGGI dahulu.
  - Peraturan (iv): purata kaedah bagi p5 set a, ditolak purata kaedah bagi p5 semua dagangan bagi kaedah yang sama, mestilah ≥ −1 mata dalam setiap sampel.
  - Peraturan (iii): hari masuk unik bagi setiap sisi, dikumpul antara kaedah. Lajur "hari min strata" pula ialah sel terkecil (kaedah atau kaedah × tercil RS).
  - Peraturan (v): > 15 daripada 30 kaedah mempunyai ΔCAGR > 0 dalam setiap sampel. Bagi VALIDATE-2022, Δ = purata ΔA dan ΔB. Varian dalam tercil RS dibanding dengan kawalan RS.
- **Pengesahan simulator** (`vr_sah.json`):
  - Rantai yang dibina semula tanpa veto sama dengan set laluan 1 bagi 30/30 kaedah. Ini termasuk M20, M26, M41 dan M78 (`ikut_laluan`) serta M167.
  - Ahli portfolio 8 slot yang disimulasi sama dengan bendera `pegang8` kolam: beza 0 dagangan bagi kumpulan A dan B dalam 30/30 kaedah.
  - Lengkung daripada rantai yang dibina semula sama dengan lengkung laluan 1, dengan beza ekuiti mutlak maksimum 0.0.
  - Simulator memakai `enjin_at.Pasaran.lengkung` sendiri dengan matriks tutup yang disimpan (3,222 ticker × 3,469 hari). **Toleransi yang dinyatakan: padanan tepat (0)**, dan ia dicapai.
- Garis dasar portfolio (CAGR/MDD setiap kaedah, kumpulan dan tempoh) ada dalam `vr_jadual.md`. Contoh:
  - M30: A 2013–21 = 21.5% / −32.8%; B 2013–21 = 12.4% / −35.6%; A 2022+ = −4.3% / −39.0%; B 2022+ = −6.8% / −56.3%.
  - M167: A 2013–21 = 7.7% / −55.8%; B 2022+ = −27.0% / −78.0%.

### Inferences
- Simulator dan kolam konsisten sepenuhnya dengan enjin. Oleh itu, sebarang perbezaan portfolio di bawah datang daripada veto atau ranking itu sendiri, bukan daripada ralat pembinaan semula.
- Garis dasar CAGR berbeza sangat besar antara kumpulan A dan B bagi kaedah yang sama (M30: 21.5% lawan 12.4%; M41: 12.1% lawan −1.6%). Ini bermakna portfolio 8 slot setiap kaedah sangat bising, dan Δ portfolio kecil tidak bermakna. Soalan 6 mengukur hingar ini.

### Gaps
- Pra-daftar tidak menyatakan arah susunan tercil RS dalam portfolio atau pemecah seri. Kedua-duanya ditetapkan di atas sebelum hasil dilihat. Hasil boleh berbeza jika pilihan lain dibuat.

## Soalan 2: Adakah veto lonjakan/perhatian (Ujian 1) memperbaiki isyarat?

### Takeaway
**Tidak. Keenam-enam varian GAGAL.** Tiada varian mencapai t > 3 dalam SELECT; t tertinggi ialah 1.77 bagi V1. Hanya V1 (hari 1% teratas setahun) memberi beza positif dalam ketiga-tiga sampel, iaitu +0.38, +0.19 dan +0.43 mata, tetapi hanya 13 daripada 30 kaedah bertambah baik di peringkat portfolio dalam SELECT. Veto MAX20 (V2, V3) sebenarnya membuang dagangan yang pulangannya **lebih tinggi** pada 2013–2021. Ia hanya memotong ekor kiri dan mengurangkan MDD, iaitu kesan risiko, bukan kelebihan pulangan.

### Cited Findings
Peringkat dagangan (`lebih_pegang`, beza disimpan − diveto, mata peratus; purata sama-pemberat kaedah; t berkelompok ikut tarikh isyarat; `vr_jadual.md`). Format sel: beza (t).

| Varian | Bahagian diveto (SELECT / 2022+) | SELECT | VALIDATE-B | VALIDATE-2022 | p5 disimpan − p5 semua (SELECT) | Portfolio: kaedah CAGR naik (SELECT / B / 2022+) | median ΔMDD SELECT / B / 2022+ | Keputusan |
|---|---|---|---|---|---|---|---|---|
| V1 atas1pct_1t | 8.7% / 10.3% | +0.38 (1.77) | +0.19 (0.90) | +0.43 (2.09) | +0.16 | 13 / 18 / 16 | +0.63 / +1.77 / +0.10 | GAGAL (ii, v) |
| V2 max20 ≥ p90 (0.0999) | 10.3% / 15.2% | −0.75 (−1.78) | −0.65 (−1.79) | +0.21 (0.72) | +1.15 | 19 / 20 / 15 | +6.23 / +4.36 / +3.04 | GAGAL (i, ii, v) |
| V3 max20 ≥ p95 (0.1381) | 5.1% / 7.6% | −0.76 (−1.35) | −1.17 (−2.22) | +0.35 (0.77) | +0.69 | 19 / 16 / 18 | +2.64 / +0.26 / +2.66 | GAGAL (i, ii) |
| V4 gap_atr ≥ 1 | 6.9% / 8.6% | −0.02 (−0.04) | −0.02 (−0.07) | +0.13 (0.57) | +0.07 | 14 / 15 / 10 | +0.00 / −1.59 / −0.55 | GAGAL (i, ii, v) |
| V5 gap_atr ≥ 2 | 3.0% / 3.7% | −0.14 (−0.34) | +0.17 (0.57) | +0.56 (1.76) | +0.06 | 12 / 15 / 8 | −0.06 / +0.00 / −0.84 | GAGAL (i, ii, v) |
| V6 rcc_srs60 > 3 | 8.8% / 10.2% | +0.20 (0.76) | −0.18 (−0.84) | +0.22 (1.03) | +0.15 | 17 / 19 / 10 | +0.04 / +0.61 / −0.93 | GAGAL (i, ii, v) |

- Ambang MAX20 dikira atas 447,212 baris unik SELECT: p90 = 0.0999 dan p95 = 0.1381. — `vr_dagangan_info.json`
- Bagi V2 dan V3, isyarat yang diveto mempunyai purata lebihan yang lebih tinggi pada 2013–2021: min diveto −0.09% berbanding disimpan −0.84% (V2 SELECT); bagi V3 VALIDATE-B, diveto +0.37% berbanding disimpan −0.80%. Pada masa yang sama, 5% terburuk bagi yang diveto jauh lebih buruk: −18.12% berbanding −11.49% bagi yang disimpan (V2 SELECT), dan −19.61% berbanding −11.95% (V3 SELECT). Dagangan MAX20 tinggi ialah taburan berekor lebar di kedua-dua arah. — `vr_jadual.md`
- Kadar menang: veto gap_atr (V4, V5) dan V6 **menurunkan** kadar menang set disimpan berbanding set diveto, sebanyak −3.1 hingga −5.6 mata. Isyarat dengan gap besar lebih kerap menang tetapi tidak lebih banyak secara purata. — `vr_jadual.md`
- Semakan kepekaan atas semua isyarat (termasuk laluan ≥ 2) memberi gambaran sama: V1 +0.41 (t 2.2), +0.24 (1.2), +0.38 (1.8); V3 −0.60, −1.34 (t −2.7), +0.62. — `vr_jadual.md`
- Lebih20 (fwd20 − spy20) tidak menyokong V1: beza −0.42, +0.09 dan +0.06 mata. — `vr_jadual.md`

### Inferences
- Bukti berwasit tentang kesan MAX (Bali, Cakici & Whitelaw 2011) tidak diterjemahkan kepada veto yang berguna atas isyarat kaedah kita. Pada 2013–2021, isyarat dengan MAX20 tinggi memberi purata lebih tinggi tetapi ekor kiri yang lebih teruk. Veto MAX20 berfungsi sebagai penapis risiko, iaitu memperbaiki 5% terburuk dan MDD portfolio, tetapi bukan penapis pulangan. Peningkatan MDD portfolio itu pun berada dalam julat plasebo veto rawak (Soalan 6).
- V1 ialah satu-satunya veto yang arahnya konsisten, tetapi saiznya kecil (+0.2 hingga +0.4 mata setiap dagangan) dan t < 3. Ia tidak memperbaiki majoriti portfolio dalam SELECT (13/30). Ia tidak wajar dipakai sebagai peraturan.
- "Kos membeli pada buka" (Berkman et al. 2012) tidak kelihatan melalui gap_atr pada hari isyarat. Veto gap besar tidak mengubah purata lebihan dengan bermakna dalam 2013–2021.

### Gaps
- Veto dalam tercil RS (seperti kriteria laporan asal) tidak termasuk dalam enam varian pra-daftar, dan tidak diuji.
- Pulangan 5/10 hari dan peluang +10% dalam 20 hari (kriteria laporan) tidak dijadikan metrik keputusan dalam pra-daftar ini, dan tidak dilapor.

## Soalan 3: Adakah pecahan semalaman/intrahari (Ujian 3) berguna sebagai kunci ranking?

### Takeaway
**Tidak. Keenam-enam varian GAGAL.** Bagi id_share20, arahnya bertukar: RENDAH dahulu lebih baik pada 2013–2021 (+0.16 dan +0.33 mata), tetapi TINGGI dahulu lebih baik pada 2022+ (+0.26). id_share60 TINGGI dahulu (R3), iaitu momentum yang terbentuk intrahari, adalah satu-satunya varian yang positif dalam ketiga-tiga sampel di peringkat dagangan (+0.12, +0.15, +0.31) **dan** memperbaiki majoriti portfolio (17, 19, 21 daripada 30). Namun t hanya 0.73, 0.71 dan 1.58, jauh di bawah 3. Dalam tercil RS, kedua-dua ciri tidak menambah nilai berbanding kawalan RS.

### Cited Findings
| Varian | SELECT | VALIDATE-B | VALIDATE-2022 | Portfolio naik (SELECT / B / 2022+) | median ΔCAGR | Keputusan |
|---|---|---|---|---|---|---|
| R1 id_share20 TINGGI | −0.16 (−0.92) | −0.33 (−1.87) | +0.26 (1.37) | 13 / 20 / 16 | −0.26 / +1.52 / +1.03 | GAGAL (i, ii, v) |
| R2 id_share20 RENDAH | +0.16 (0.92) | +0.33 (1.87) | −0.26 (−1.37) | 16 / 19 / 16 | +0.22 / +0.62 / +0.30 | GAGAL (i, ii) |
| R3 id_share60 TINGGI | +0.12 (0.73) | +0.15 (0.71) | +0.31 (1.58) | 17 / 19 / 21 | +0.56 / +0.97 / +1.06 | GAGAL (ii sahaja) |
| R4 id_share60 RENDAH | −0.12 (−0.73) | −0.15 (−0.71) | −0.31 (−1.58) | 10 / 14 / 14 | −1.20 / −0.14 / −0.05 | GAGAL |
| R5 id_share20 dalam tercil RS (RENDAH) | +0.26 (1.48) | +0.44 (2.51) | −0.18 (−0.93) | lawan kawalan: 14 / 9 / 15 | −0.17 / −0.90 / −0.10 | GAGAL (i, ii, v) |
| R6 id_share60 dalam tercil RS (TINGGI) | −0.02 (−0.14) | +0.01 (0.04) | +0.16 (0.80) | lawan kawalan: 16 / 11 / 18 | +0.21 / −0.71 / +1.11 | GAGAL (i, ii, v) |

- Beza dilapor sebagai tercil atas − bawah dalam arah varian, dalam mata peratus `lebih_pegang`, dengan t dalam kurungan. Bagi R5 dan R6, ΔCAGR dibanding dengan kawalan RS. — `vr_jadual.md`
- 5% terburuk set atas R3 lebih baik daripada semua dagangan dalam ketiga-tiga sampel: −12.09 lawan −12.64 (SELECT), −12.24 lawan −12.61, dan −13.88 lawan −14.08. — `vr_jadual.md`
- Semakan kepekaan semua isyarat: R3 +0.10 (0.6), +0.09 (0.5), +0.35 (2.0); R5 +0.24 (1.6), +0.48 (3.1), −0.27 (−1.3). — `vr_jadual.md`
- Sel tercil semua besar: ≥ 2,257 hari beli berbeza dalam 2013–2021 dan ≥ 1,197 dalam 2022+. Strata terkecil mempunyai 22–51 hari. Peraturan (iii) tidak mengikat. — `vr_jadual.md`

### Inferences
- Arah R3 (intrahari tinggi dahulu, 60 hari) selari dengan Barardehi, Bogousslavsky & Muravyev: momentum yang terbentuk intrahari berterusan. Namun kesannya terlalu kecil untuk dibezakan daripada hingar dalam data ini (t ≤ 1.6), dan portfolio yang bertambah baik (17–21/30) hampir sama dengan julat plasebo ranking rawak (12–18/30; Soalan 6). Ia boleh disimpan sebagai calon yang dipantau, tetapi tidak sebagai peraturan.
- id_share20 bertukar tanda antara tempoh. Ini satu bentuk ketidakstabilan yang menjadi sebab utama peraturan "ketiga-tiga sampel" diwujudkan.
- Percanggahan "M167 GUNA secara dalaman lawan literatur" tidak dapat diselesaikan di peringkat semua kaedah. Lihat Soalan 5 untuk M167 sahaja.

### Gaps
- Kuintil monotonik (kriteria laporan) tidak diuji; pra-daftar memakai tercil.
- Tiada data intrahari sebenar. id_share dikira daripada OHLC harian terlaras (lihat [kolam_isyarat.md](kolam_isyarat.md)).

## Soalan 4: Adakah volum hari naik dan jarak paras tertinggi 52 minggu (Ujian 4) berguna sebagai bonus/ranking?

### Takeaway
**Tidak. Kelapan-lapan varian GAGAL.** Bonus hari hijau bervolum tinggi (B1, B8) **merugikan** dalam ketiga-tiga sampel: −0.30, −0.19, −0.18 mata, dengan 5% terburuk set bonus lebih teruk 1.13 mata. Ini bertentangan dengan jangkaan "volum mungkin lulus". h52 dan h52_industri TINGGI dahulu (B3, B5) memperbaiki majoriti portfolio dalam ketiga-tiga sampel dan sangat memperbaiki 5% terburuk serta MDD. Namun di peringkat dagangan, beza purata hampir sifar pada 2013–2021 (B3: −0.07, +0.01; B5: +0.05, −0.04), jadi kedua-duanya gagal (i) dan (ii). Dalam tercil RS, tiada ciri menambah nilai berbanding kawalan RS.

### Cited Findings
| Varian | SELECT | VALIDATE-B | VALIDATE-2022 | p5 atas lawan semua (SELECT) | beza kadar menang (SELECT / B / 2022+) | Portfolio naik (SELECT / B / 2022+) | median ΔMDD | Keputusan |
|---|---|---|---|---|---|---|---|---|
| B1 hijau_vol90 | −0.30 (−1.87) | −0.19 (−1.06) | −0.18 (−0.87) | −13.77 / −12.64 | +1.2 / +0.7 / +1.3 | 13 / 13 / 16 | +3.29 / +0.42 / +1.42 | GAGAL (i, ii, iv, v) |
| B2 vol_pctl50 | −0.04 (−0.28) | +0.03 (0.18) | −0.37 (−1.92) | −13.57 / −12.64 | +1.8 / +2.1 / +1.5 | 14 / 21 / 20 | +4.48 / +1.87 / +2.78 | GAGAL (i, ii, v) |
| B3 h52 | −0.07 (−0.33) | +0.01 (0.02) | +0.34 (1.46) | −10.76 / −12.64 | +2.5 / +3.3 / +3.5 | 18 / 18 / 18 | +7.48 / +2.82 / +7.49 | GAGAL (i, ii) |
| B4 h52 ≥ 0.95 | −0.18 (−0.83) | −0.13 (−0.58) | +0.27 (1.33) | −11.18 / −12.64 | +1.9 / +2.6 / +2.5 | 18 / 19 / 14 | +4.36 / +2.84 / +1.97 | GAGAL (i, ii, v) |
| B5 h52_industri | +0.05 (0.28) | −0.04 (−0.21) | +0.27 (0.96) | −10.87 / −12.64 | +0.8 / +0.6 / +0.5 | 16 / 22 / 20 | +6.35 / +2.13 / +8.41 | GAGAL (i, ii) |
| B6 h52 dalam tercil RS | −0.17 (−0.75) | +0.04 (0.17) | −0.16 (−0.66) | −10.35 / −12.64 | +3.1 / +3.9 / +2.5 | lawan kawalan: 15 / 13 / 22 | +1.09 / +0.25 / +2.12 | GAGAL |
| B7 h52_industri dalam tercil RS | +0.19 (0.97) | +0.10 (0.52) | −0.32 (−1.12) | −10.89 / −12.64 | +1.0 / +0.8 / −1.0 | lawan kawalan: 14 / 13 / 19 | +1.88 / −0.05 / +3.06 | GAGAL |
| B8 hijau_vol90 dalam tercil RS | −0.29 (−1.77) | −0.24 (−1.35) | −0.27 (−1.29) | −13.74 / −12.64 | +1.0 / +0.9 / +1.1 | lawan kawalan: 12 / 11 / 18 | −0.35 / −0.19 / −0.06 | GAGAL (i, ii, iv, v) |

- Nilai p5 dalam peratus pulangan dagangan. Bagi B6–B8, ΔMDD dibanding dengan kawalan RS. — `vr_jadual.md`
- Bahagian dagangan dengan bendera: hijau_vol90 = 22% (78% tanpa bendera dalam semua sampel); h52 ≥ 0.95 = 44% (2013–21) dan 32% (2022+). — `vr_ujian.json`
- Pada 2022+, taburan h52 isyarat beralih ke bawah. Tercil atas SELECT hanya meliputi 23% dagangan 2022+ (B3) dan 15% (B5), kerana sempadan dibeku daripada SELECT. — `vr_kolam.parquet` (semakan `terc_*`)
- **Kawalan RS sahaja** (tercil RS rs12_pct TINGGI dahulu, kemudian `rank_value`, tanpa ciri bar) memperbaiki CAGR portfolio dalam 20 / 21 / 19 daripada 30 kaedah, dengan median ΔCAGR +1.63 / +1.43 / +0.68 mata dan ΔMDD +1.13 / +2.13 / +2.81 mata. Ini lebih konsisten daripada mana-mana ciri bar. — `vr_jadual.md`

### Inferences
- Premium volum tinggi (Gervais, Kaniel & Mingelgrin 2001) tidak muncul sebagai bonus atas isyarat kaedah. Hari hijau bervolum tinggi pada hari isyarat cenderung menjadi hari "perhatian", sama seperti Ujian 1. Hasilnya pulangan selepas itu lebih rendah dan ekor kiri lebih teruk.
- h52 tinggi memilih dagangan yang lebih kerap menang (+2.5 hingga +3.5 mata) dengan ekor kiri yang lebih nipis (p5 lebih baik ~1.9 mata), tetapi purata lebihannya tidak lebih tinggi pada 2013–2021. Kesannya pada portfolio (MDD lebih kecil) ialah kesan risiko. Ini selari dengan h52 yang bertindih dengan RS (ρ 0.43): dalam tercil RS (B6), kesannya hilang.
- Pengajaran paling jelas daripada ujian ini bukan ciri bar, tetapi `rank_value` kaedah. Penyusunan semula ikut RS sahaja memperbaiki majoriti portfolio, dan ranking rawak hampir sama baik dengan `rank_value` (Soalan 6). Ini menunjukkan rank asal banyak kaedah dalam kolam ini lemah. Soalan itu berbeza dan tidak diuji di sini, tetapi selari dengan kerja RS_10 dalam portfolio_slot.

### Gaps
- `h52_industri` memakai peta industri semasa (bukan titik masa). Perbandingan dengan gred V3 (kriteria laporan) tidak dibuat.
- Ambang h52 {0.75, 0.85} daripada laporan tidak termasuk dalam pra-daftar. Hanya 0.95 dan tercil yang diuji.

## Soalan 5: Bagaimana hasilnya bagi M167 dan kaedah breakout (M04, M30, M33, M79, M135)?

### Takeaway
Dalam M167, isyarat dengan id_share20 TINGGI (kenaikan 20 hari yang terbentuk intrahari) mengatasi yang RENDAH dengan kuat dalam SELECT (+1.87 mata, t 3.21) dan 2022+ (+2.22, t 3.58), tetapi **tidak dalam VALIDATE-B** (+0.05, t 0.07). Oleh itu ia gagal peraturan ketiga-tiga sampel. h52 TINGGI dalam M167 positif dalam ketiga-tiga sampel (+0.88, +1.25, +2.12), tetapi t SELECT hanya 1.21. Bagi kaedah breakout, tiada corak veto yang konsisten. Veto hari 1% teratas membuang 22–40% isyarat breakout tanpa memperbaiki purata secara konsisten.

### Cited Findings
t setiap kaedah (K = 1, berkelompok ikut tarikh; `vr_khusus.md`). Format sel: beza `lebih_pegang` mata (t).

| Kaedah | Varian | SELECT | VALIDATE-B | VALIDATE-2022 | ΔCAGR portfolio SELECT / B / 2022+ |
|---|---|---|---|---|---|
| M167 | R1 id_share20 TINGGI | +1.87 (3.21) | +0.05 (0.07) | +2.22 (3.58) | +3.36 / +11.84 / +22.93 |
| M167 | R3 id_share60 TINGGI | +0.36 (0.51) | +0.42 (0.68) | +1.28 (2.47) | +1.46 / +4.48 / +9.38 |
| M167 | B3 h52 TINGGI | +0.88 (1.21) | +1.25 (1.78) | +2.12 (3.88) | −5.19 / +9.55 / +24.43 |
| M167 | B5 h52_industri TINGGI | +0.19 (0.27) | +0.91 (1.37) | +2.94 (3.79) | −4.74 / +5.61 / +5.82 |
| M167 | B6 h52 dalam tercil RS | +0.26 (0.35) | +1.71 (2.30) | +1.98 (3.14) | −9.44 / +11.47 / +17.56 (lawan kawalan) |
| M167 | V1 (veto 4% isyarat) | +0.70 (0.87) | −1.31 (−0.89) | +1.56 (1.96) | −2.05 / −3.12 / +0.37 |
| M04 | V1 (veto 29%) | −0.08 (−0.16) | −0.12 (−0.40) | +0.19 (0.55) | −5.55 / +3.68 / +8.17 |
| M30 | V1 (veto 25%) | −0.67 (−1.31) | −0.22 (−0.68) | +0.04 (0.12) | −6.38 / −0.59 / −2.13 |
| M33 | V1 (veto 23%) | −0.06 (−0.13) | −0.18 (−0.72) | +0.41 (1.51) | +0.57 / +10.94 / +1.35 |
| M79 | V1 (veto 22%) | +1.48 (2.05) | +0.75 (1.31) | −0.65 (−0.96) | +4.11 / −1.70 / −10.61 |
| M135 | V1 (veto 40%) | +0.07 (0.15) | −0.58 (−1.10) | +0.93 (1.52) | −2.39 / −5.06 / +0.79 |
| M135 | B1 hijau_vol90 | −1.82 (−3.30) | −0.65 (−1.08) | −0.07 (−0.09) | −2.84 / −0.41 / +1.84 |
| M33 | B3 h52 TINGGI | +0.18 (0.44) | +0.99 (3.53) | +0.54 (1.87) | +2.87 / +4.97 / +5.06 |
| M30 | B4 h52 ≥ 0.95 | +0.31 (0.74) | +0.61 (2.13) | +0.67 (2.18) | +0.15 / −2.08 / +2.70 |
| M30 | V3 max20 ≥ p95 | −3.04 (−1.45) | −1.21 (−0.96) | −0.27 (−0.33) | −5.69 / −3.88 / −3.25 |

- Jadual penuh bagi 20 varian × 6 kaedah ada dalam `vr_khusus.md` (t) dan bahagian "M167 dan kaedah breakout" dalam `vr_jadual.md` (ΔCAGR).
- Kaedah breakout mempunyai bahagian isyarat yang tinggi pada hari 1% teratas setahun (SELECT: M135 40%, M04 29%, M30 25%, M33 23%, M79 22%). Bahagian bagi M167 hanya 4%. — `vr_jadual.md`

### Inferences
- Bagi M167 (kunci OVN252 = momentum semalaman), memilih saham yang kenaikan terbarunya terbentuk intrahari selari dengan literatur. Ia memberi kesan terbesar dalam keseluruhan ujian (≈ +2 mata setiap dagangan dalam dua daripada tiga sampel). Namun ia gagal dalam VALIDATE-B. Ini juga hasil pasca-hoc: 20 varian × 6 kaedah × 3 sampel = 360 ujian, dan beberapa |t| > 3 dijangka secara kebetulan. Jika hendak diteruskan, ia mesti didaftarkan semula sebagai hipotesis M167 sahaja dan diuji atas data baharu (Lejar Penuh hadapan atau set 431), bukan dipakai terus.
- Bagi kaedah breakout, veto "hari perhatian" bukan penyelesaian: ia membuang sebahagian besar isyarat dengan beza yang bertukar tanda antara sampel.

### Gaps
- Tiada t portfolio setiap kaedah. ΔCAGR portfolio setiap kaedah sangat bising (contohnya M167 R1 +3.36 lawan +22.93 mata), jadi ia tidak boleh dibaca bersendirian.

## Soalan 6: Sejauh mana ujian portfolio boleh dipercayai? (diagnostik tambahan, bukan pra-daftar)

### Takeaway
Ujian majoriti portfolio (peraturan v) mempunyai kuasa yang rendah. Ranking rawak memperbaiki CAGR dalam 12–18 daripada 30 kaedah setiap sampel dan memperbaiki median MDD sebanyak +1.55 hingga +5.16 mata dalam SELECT. Veto rawak dengan bahagian yang sama seperti V2/V3 memperbaiki 12–20 kaedah. Oleh itu, kiraan 16–22/30 bagi varian terbaik (R3, B3, B5, V3) tidak jauh daripada kebetulan. Peraturan t > 3 peringkat dagangan yang menjadi penentu.

### Cited Findings
Peringkat `plasebo` ([`veto_ranking.py`](../../lilin/veto_ranking.py), `vr_plasebo.md`; 5 benih):

| Plasebo | Kaedah CAGR naik SELECT | VALIDATE-B | VALIDATE-2022 | median ΔMDD SELECT |
|---|---|---|---|---|
| Ranking rawak (benih 1–5) | 15, 14, 12, 15, 12 | 18, 15, 18, 17, 18 | 16, 13, 15, 17, 17 | +1.85, +1.55, +4.09, +4.66, +5.16 |
| Veto rawak, bahagian = V2 | 16, 17, 14, 18, 12 | 18, 13, 19, 17, 20 | 13, 16, 17, 18, 14 | +0.92, +2.42, +1.92, +1.69, +0.21 |
| Veto rawak, bahagian = V3 | 16, 15, 13, 14, 12 | 16, 15, 17, 19, 16 | 15, 14, 14, 12, 13 | +0.85, −0.39, −0.21, +2.61, +0.29 |

- Hanya 1 daripada 15 larian plasebo (veto rawak V2, benih 4: 18 / 17 / 18) yang lulus peraturan (v) dalam ketiga-tiga sampel. Varian sebenar yang lulus (v): V3, R2, R3, B3, B5. — `vr_plasebo.md`, `vr_jadual.md`

### Inferences
- `rank_value` kaedah dalam kolam ini tidak lebih baik daripada rawak bagi MDD portfolio. Ranking rawak memperbaiki median MDD dalam SELECT dalam 5/5 benih. Sebarang kunci baharu yang "mempelbagaikan" susunan boleh kelihatan baik di peringkat portfolio tanpa maklumat sebenar.
- Kesimpulan akhir: **tiada ciri bar (Ujian 1, 3, 4) yang lulus sebagai lapisan veto atau ranking atas isyarat kaedah sedia ada dalam alam AUTOTUNE 2000 saham.** Tiada peraturan langsung (papertrade C, Lejar, `harian_c.py`) wajar diubah atas dasar ujian ini.

### Gaps
- t berkelompok ikut tarikh isyarat tidak mengambil kira pertindihan tempoh pegangan antara tarikh. Ralat piawai sebenar mungkin lebih besar, jadi t sebenar lebih kecil. Ini tidak mengubah keputusan GAGAL.
- Data AUTOTUNE mempunyai bias survivorship (tiada saham delist), jadi semua angka ialah had atas. S1–S4, WFO W01 dan set 431 tidak diuji dalam nota ini.
- Bagi M20, M26, M41 dan M78 (`ikut_laluan`), veto portfolio ialah anggaran: isyarat laluan ≥ 2 tiada keluar sendiri, jadi ia tidak boleh menggantikan isyarat yang diveto.
- `lebih_pegang` menolak SPY tanpa kos, manakala `trade_ret` sudah bersih kos. Ini adil bagi beza a − b (kedua-dua sisi sama), tetapi paras mutlak `min a`/`min b` mengandungi kos.
