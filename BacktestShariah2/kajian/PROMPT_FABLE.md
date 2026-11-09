# Prompt penilaian untuk Fable 5.1

Disediakan 9 Nov 2026 atas permintaan pengguna. Cara guna: buka chat baharu Claude Code dalam repo ini, pilih model Fable 5.1 melalui `/model`, kemudian salin dan tampal keseluruhan blok di bawah. Laluan fail dan akses data disahkan wujud pada 9 Nov 2026; jika fail dinamakan semula, kemas kini prompt ini.

```
Saya pedagang swing saham syariah AS (penanda aras SPUS, bukan SPY). Repo ini menjejak 223 kaedah dagangan dalam papertrade dan Lejar: 129 Mxx dan 94 Nxx (Nxx berbentuk masuk x keluar, contoh N19X13). Setiap kali saya minta ukuran, saya tidak dapat jawapan yang jelas, jadi saya tidak tahu kaedah mana yang baik. Saya perlukan anda sebagai pakar penilaian strategi (statistik kuantitatif) dan pedagang swing momentum berpengalaman, untuk memberi saya gambaran jujur dan satu pelan yang boleh saya ikut.

Matlamat saya: untung bersih melebihi rugi (bukan sekadar kadar menang tinggi), pegang maksimum 10 sesi, kira-kira +5% setiap dagangan, MDD akaun tidak lebih teruk daripada -10%. Tiada wang sebenar sehingga BacktestShariah2/laporan/KAD_SKOR.md menanda TERBUKTI. "Foolproof" tidak wujud; saya mahu yang TERBAIK TERUKUR, dan jika tiada, katakan terus.

SUMBER (mula dengan CLAUDE.md dan KOORDINATOR.md; kedua-duanya menunjuk ke sumber kebenaran)
- Latar dan sejarah: BacktestShariah2/00_NOTA_SERAHAN.md, BacktestShariah2/SEJARAH_KAJIAN.md (bahagian berkaitan sahaja), BacktestShariah2/standard/tugasan_v3.md
- Laporan: BacktestShariah2/laporan/KAD_SKOR.md, BacktestShariah2/laporan/SKOR_KAEDAH.md, BacktestShariah2/laporan/PENGANALISIS.md, BacktestShariah2/laporan/LIFT_KAEDAH.md, BacktestShariah2/laporan/T4_KAEDAH.md, BacktestShariah2/laporan/PLASEBO_GATE.md, BacktestShariah2/laporan/SOP_MOMENTUM.md, BacktestShariah2/laporan/BANDING_SPUS.md
- Spesifikasi: BacktestShariah2/standard/SPEC_KAD_SKOR.md, BacktestShariah2/standard/SPEC_SKOR_KAEDAH.md
- Kajian REVERSE: REVERSE/KEPUTUSAN_AKHIR.md, REVERSE/STRATEGI.md (jalankan python3 REVERSE/strategi.py untuk apa yang sudah diuji / tinggal), REVERSE/SASARAN.md, REVERSE/SISTEM.md, REVERSE/GABUNGAN.md, REVERSE/SILANG_AKHIR.md, REVERSE/PORTFOLIO_N.md, REVERSE/NXX_KELUAR.md, REVERSE/KOMBINASI.md, REVERSE/SETUP.md, REVERSE/KOLAM_EKOR.md, REVERSE/CARA_94.md, REVERSE/KOS_DRAG.md, REVERSE/PENANDA_ARAS_SYARIAH.md, BacktestShariah2/kajian/KAJIAN_PORTFOLIO.md
- Data analisis: BacktestShariah2/data/analisis/kad_skor.json, BacktestShariah2/data/analisis/skor_kaedah.json, BacktestShariah2/data/analisis/lift.json, BacktestShariah2/data/analisis/gabungan_beku.json
- Data mentah: BacktestShariah2/lejar/, BacktestShariah2/papertrade/ (skema BacktestShariah2/papertrade/SKEMA.md), BacktestShariah2/data/konteks/, BacktestShariah2/portfolio_slot/, data_mentah/. Panel backtest A02 dimuat turun automatik oleh REVERSE/teras/data.py (Release autotune-data-a02, kira-kira 218 MB).
- Dashboard: BacktestShariah2/standard/dashboard.md dan BacktestShariah2/standard/dashboard_v2.html
- Kod penting: GB01 hingga GB08 ialah blok gabungan dalam BacktestShariah2/standard/registry_n.py. GB02_atau3 = beli jika mana-mana satu menyala: N19 (bawah jalur BB + RSI14 < 30), N37 (gap and go), N115 (Holy Grail Raschke); GB02_atau4 tambah N20. Keluar: X13 = jual bila RSI14 > 70; X15 = Chandelier 4 x ATR14; X17 = jual bila ADX14 < 20; X3 = henti 2 x ATR, pegang 63 sesi. Data langsung dikira untuk Mxx sejak isyarat 2026-10-15 dan Nxx sejak 2026-11-03.

BAHAGIAN 1 — Penilaian dan pelan (data sedia ada sahaja; tiada backtest baharu). Jawab:
1. Kenapa setiap pengukuran tiada keputusan: kaedah lemah, data tidak cukup, atau cara ukur? Bila keputusan pertama boleh dibuat?
2. Kaedah teratas (SKOR_KAEDAH dan backtest): adakah angka backtest bertahan dalam data langsung? Lapor jangkaan, kadar menang, untung purata, rugi purata.
3. Apakah kadar menang tertinggi yang masih memberi jangkaan positif selepas kos? Bolehkah 70% dicapai?
4. Gabungan apa yang sudah diuji dan apa hasilnya, termasuk prestasi hadapan gabungan_beku (M70 + M03 + M18) dan N19X13?
5. Kenapa Papertrade C rugi (rejim, sektor, henti hari-0, saiz)?
6. Kawal risiko untuk MDD -10%: berat SPUS + tunai; bilangan slot dan peratus modal setiap saham; had 1 saham setiap industri; stop loss yang paling kurang merugikan, dengan formula saiz posisi; apa yang berubah bila rejim QQQ ON atau OFF.
7. Dashboard: 5 perkara yang perlu saya lihat setiap hari dan maksudnya.
Kemudian kelaskan kaedah kepada PANTAU / BUANG / BELUM BOLEH KATA (sebab satu baris; ini pendapat pakar, bukan keputusan wang sebenar), dan beri SATU pelan swing paling disokong data (masuk, keluar, henti, saiz, berat SPUS + tunai) dengan jangkaan, kadar menang dan MDD terukur, atau katakan terus tiada pelan yang disokong.
Tulis dapatan dalam BacktestShariah2/kajian/FABLE_PENILAIAN.md (paparkan baris status kad skor daripada BacktestShariah2/standard/status_kad.py di atasnya), komit dan push, kemudian BERHENTI dan laporkan kepada saya.

BAHAGIAN 2 — Kajian baharu (hanya selepas saya luluskan). Saya membenarkan SATU kajian gabungan baharu (keputusan 9 Nov 2026) walaupun baris gilir E1 hingga E6 sudah ditutup:
- Satu gabungan belum diuji untuk pegangan maksimum 10 sesi (titik mula GB02_atau3 dengan had pegang 10 sesi; tambah penapis rejim atau RS hanya jika Bahagian 1 menyokongnya). Pradaftar dahulu: hipotesis, peraturan, saiz, metrik, ambang lulus, latih 2012 hingga 2019, tahan 2020 hingga 2025; komit spec dan kod sebelum melihat keputusan. Uji setiap dagangan dan portfolio 8 hingga 10 slot lawan rawak 20 benih, kos penuh, kedua-dua rejim, banding SPUS + tunai pada MDD -10%.
- Jika lulus, daftar untuk jejak langsung: skrip WFO/kaedah_baru/step2_<ID>.py, fail BacktestShariah2/kod/registry/<ID>.csv, baris BacktestShariah2/data/registry_M_gabung.csv, db registry/<ID> melalui BacktestShariah2/standard/dashboard_kemaskini.py, baris BacktestShariah2/standard/katalog_kaedah.json, kemudian jana semula papan.
- Pradaftar peraturan cantas untuk mengurangkan 223 kaedah (bina atas label BERSARA / GANTUNG dalam BacktestShariah2/standard/penganalisis.py). Cadangan sahaja.
- Senarai semak sebelum wang sebenar (syarat TERBUKTI, kos broker, cukai, slippage, had rugi akaun) dan format ringkasan mingguan 5 baris untuk BacktestShariah2/jadual/mingguan.md. Cadangan sahaja.

SEMPADAN
- Ukuran utama ialah jangkaan positif selepas kos; setiap kadar menang dilapor bersama untung purata, rugi purata dan payoff.
- Ujian statistik setiap kaedah mesti guna reka bentuk dalam BacktestShariah2/standard/lift_kaedah.py (kluster dua hala saham + minggu, asas hari x tercile ATR); sebarang gate kemahiran baharu mesti lulus BacktestShariah2/standard/plasebo_gate.py (lulus palsu maksimum 5%).
- Bezakan dalam sampel / luar sampel / langsung; ambil kira bias survivorship (alam A02 tiada saham delist) dan ujian berganda (223 kaedah).
- Kebersihan data: kecualikan ticker dalam BacktestShariah2/data/harga/kuarantin.csv dan saham tidak layak (BacktestShariah2/kod/tidak_layak.py); kaedah replika dinilai dengan BacktestShariah2/kod/dagangan.py; dua lorong keluar (kaedah dan Chandelier) dibaca berasingan (BacktestShariah2/standard/keluar_lorong.py).
- Jangan ulang kajian yang sudah ditutup (REVERSE/KEPUTUSAN_AKHIR.md, KOORDINATOR.md bahagian 7) selain yang dibenarkan di atas. Jangan ubah ambang kad skor, jangan sunting fail dijana, jangan buat order, jangan cipta artifact baharu, jangan terbitkan semula dashboard. Jangan reka nombor; jika data tidak cukup, katakan dan nyatakan bila ia cukup.
- Sebelum setiap push: python3 -m unittest discover -s BacktestShariah2/ujian dan python3 BacktestShariah2/standard/sahkan.py --betulkan mesti keluar 0.

CARA BEKERJA
- Dalam setiap bahagian, teruskan tanpa meminta izin untuk langkah yang boleh diterbalikkan. Berhenti hanya di hujung Bahagian 1, sebelum menjalankan kajian Bahagian 2, atau untuk tindakan yang tidak boleh diterbalikkan.
- Agihkan soalan yang bebas antara satu sama lain kepada sub-agen dan teruskan kerja sementara ia berjalan.
- Sebelum melaporkan apa-apa nombor atau kemajuan, sahkan ia dengan hasil alat dalam sesi ini. Untuk kod backtest, jalankan ujian asap pada GABUNGAN masuk + keluar, bukan komponen sahaja (pepijat lama: harga keluar merentas ticker; henti di atas harga masuk), dan minta sub-agen dengan konteks baharu menyemak kod sebelum keputusan dilihat.
- Jika satu bahagian tersekat, siapkan bahagian lain sepenuhnya dan nyatakan apa yang tertinggal dan kenapa.
- Sebelum menjalankan skrip REVERSE atau AUTOTUNE, pasang dahulu: pip install -c kekangan.txt -r requirements.txt pyarrow (pyarrow tiada dalam requirements.txt tetapi diperlukan untuk membaca data parquet; pemasangan mengambil kira-kira 3 minit).

LAPORAN KEPADA SAYA
Bahasa Melayu mudah dan pendek; ayat pertama ialah jawapannya. Mulakan dengan satu perenggan "apa saya patut buat minggu ini". Tulis ayat penuh, tanpa singkatan atau anak panah. Akhiri dengan jadual tiga lajur: Selesai, Tertangguh, Perlu keputusan anda.
```
