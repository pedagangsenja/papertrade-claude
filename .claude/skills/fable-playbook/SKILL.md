---
name: fable-playbook
description: >
  Cara kerja wajib bagi SETIAP tugasan dalam repo ini yang memerlukan lebih daripada
  satu langkah: menulis atau mengubah kod, analisis data, backtest, laporan, dashboard,
  kemas kini fail, atau apa-apa jawapan yang memetik nombor. Muatkan SEBELUM langkah
  pertama. Ia memberi urutan tetap rancang, pecah, buat, semak, lapor, dan senarai
  semak yang mesti dijalankan sebelum berkata "siap". Langkau hanya bagi soalan satu
  baris yang tidak menyentuh fail atau nombor.
---

# Playbook kerja (rancang → pecah → buat → semak → lapor)

Ikut bahagian 1 hingga 5 mengikut urutan. Jangan langkau bahagian 4.
Jika playbook ini bercanggah dengan `CLAUDE.md`, `CLAUDE.md` menang.
Sebab: `CLAUDE.md` merekod keputusan pengguna; playbook ini hanya cara kerja.

## 1. Rancang sebelum menyentuh apa-apa

1. Tulis matlamat dalam SATU ayat, dengan perkataan pengguna sendiri.
   Jika tidak dapat menulisnya, tanya pengguna satu soalan pendek dan berhenti.
   Sebab: kerja yang betul bagi matlamat yang salah mesti dibuat semula.
2. Tulis "siap bermakna": 1 hingga 3 perkara yang boleh disemak dengan arahan atau
   fail (cth. "ujian lulus", "fail X wujud", "nombor Y sama dengan fail sumber").
   Sebab: tanpa takrif siap, kerja berhenti apabila letih, bukan apabila betul.
3. Baca dahulu, jangan teka:
   a. bahagian `CLAUDE.md` yang berkaitan;
   b. fail dalam jadual "Sumber kebenaran" yang menjawab soalan itu;
   c. setiap fail yang akan diubah, dari baris pertama hingga akhir;
   d. cari (Grep nama DAN kandungan) sama ada benda itu sudah wujud.
   Had: jangan ubah fail yang belum dibaca. Sebab: tekaan tentang kod sedia ada
   ialah punca utama perubahan yang merosakkan.
4. Semak tiga larangan. Jika mana-mana "ya", berhenti dan tanya pengguna:
   a. Adakah kajian ini sudah diukur ("Dapatan yang sudah diukur" dalam `CLAUDE.md`)?
   b. Adakah ia memerlukan keputusan pengguna atau pindaan bertarikh pada spec dahulu?
   c. Adakah ia menyentuh wang sebenar, order, kad skor, atau fail berlabel "jangan ubah"?
   Sebab: larangan itu ditulis selepas kesilapan sebenar; mengulanginya membazir masa pengguna.
5. Senaraikan apa yang belum diketahui. Bagi setiap satu, pilih satu:
   "boleh disemak sendiri" (semak sekarang) atau "hanya pengguna tahu" (tanya).
   Keputusan teknikal dibuat sendiri; MAKSUD dan MATLAMAT ditanya.
6. Pilih cara paling kecil yang memenuhi "siap bermakna". Jangan tambah ciri, fail
   atau kerja sampingan yang tidak diminta. Sebab: setiap tambahan ialah benda
   baharu yang boleh rosak dan perlu disemak pengguna.

## 2. Pecahkan kerja

1. Pecahkan kepada langkah yang setiap satunya ada SATU hasil yang boleh disemak
   (satu arahan, satu fail, atau satu nombor). Jika lebih 3 langkah, rekod dalam
   senarai tugasan.
2. Letak dahulu langkah yang paling mungkin menggagalkan rancangan, dan cuba pada
   sampel kecil (1 saham, 1 setup, atau 20 baris) sebelum larian penuh.
   Sebab: gagal pada minit pertama lebih murah daripada gagal selepas sejam.
3. Larian yang dijangka melebihi 2 minit: uji pada sampel kecil, kemudian jalankan
   di latar belakang.
4. Satu perubahan, satu semakan: jalankan semakan langkah itu sebelum langkah
   seterusnya. Sebab: dua perubahan tanpa semakan bermakna tidak tahu yang mana rosak.
5. Jika satu langkah gagal 2 kali dengan cara yang sama, berhenti mengulang. Baca
   ralat penuh, tulis puncanya dalam satu ayat, kemudian tukar cara.
   Jika masih gagal selepas cara kedua, beritahu pengguna apa yang dicuba dan apa ralatnya.

## 3. Semasa membuat

1. Setiap nombor yang ditulis mesti datang daripada output arahan atau fail yang
   dibaca DALAM sesi ini. Jangan petik daripada ingatan atau daripada `CLAUDE.md`.
   Sebab: nombor yang disalin hanyut.
2. Baca ralat dari baris pertama, bukan baris terakhir sahaja.
   Sebab: punca biasanya di atas, gejala di bawah.
3. Fail yang dijana (papan, laporan, kad skor, lejar, KOORDINATOR): ubah penjananya,
   kemudian jana semula. Jangan sunting dengan tangan. Sebab: suntingan tangan
   hilang pada larian seterusnya.
4. Sebelum memadam atau menulis ganti, lihat sasarannya dahulu (`ls`, `git status`, baca fail).
5. Tindakan yang sukar dibalik (push ke `main`, terbit dashboard, tolak db, padam
   data, ubah fail kohort) perlu keputusan pengguna, kecuali prosedur dalam
   `BacktestShariah2/jadual/` membenarkannya secara bertulis.
6. Jangan longgarkan ujian, ambang atau semakan supaya lulus. Baiki puncanya.
   Sebab: semakan yang dilonggarkan tidak lagi menyemak apa-apa.
7. Kerja yang tidak bergantung antara satu sama lain dijalankan serentak.

## 4. Semak sebelum berkata "siap"

Jalankan semua tujuh. Jika satu tidak dapat dijalankan, tulis "belum disemak" dalam laporan.

1. Jalankan semula setiap perkara "siap bermakna" dan baca outputnya.
2. Jika kod atau data di bawah `BacktestShariah2/` berubah:
   `python3 -m unittest discover -s BacktestShariah2/ujian` mesti lulus.
   Sebelum push data: `python3 BacktestShariah2/standard/sahkan.py --betulkan` mesti keluar 0.
3. `git status` dan `git diff --stat`: hanya fail yang dimaksudkan berubah.
4. Semak nombor: pilih 3 nombor dalam jawapan (semua jika kurang daripada 3) dan
   jejak setiap satu ke output atau fail asalnya. Kira semula 1 daripadanya dengan cara kedua.
5. Bagi dapatan backtest, jawab tiga soalan dengan ya atau tidak:
   a. Dibanding dengan kawalan rawak yang dibeli hari sama dan dipegang dengan cara sama?
   b. Disemak ikut TAHUN, bukan hanya ikut saham?
   c. Bebas daripada maklumat masa hadapan (cth. harga buka esok)?
   Jika mana-mana "tidak", laporkan sebagai "belum disemak", bukan sebagai dapatan.
6. Baca semula permintaan asal perkataan demi perkataan. Padankan setiap frasa
   dengan satu hasil. Frasa tanpa hasil = belum siap.
7. Tulis laporan dalam tiga bahagian: apa yang dibuat; apa yang disemak dan
   hasilnya; apa yang TIDAK dibuat atau gagal. Jangan tulis "sepatutnya berfungsi":
   sama ada sudah disemak, atau katakan belum.

## 5. Kesilapan yang perlu diawasi

Sebelum menghantar jawapan, semak bahawa tiada satu pun berlaku:

1. Berkata "siap" tanpa menjalankan semakan. (Paling kerap.)
2. Memetik nombor daripada ingatan atau ringkasan, bukan daripada fail sumber.
3. Menilai setup carian (CS, F, T) dengan kayu ukur yang salah. Kayu ukur dan
   larangan ada dalam `CLAUDE.md`, "Matlamat carian setup": baca sebelum menilai.
4. Menganggap purata setiap dagangan atau kadar menang sebagai hasil akaun.
5. Mencadangkan kajian, pusingan atau kerja sampingan yang tidak diminta, atau yang sudah diukur.
6. Meneka maksud pengguna apabila tidak faham. Tanya satu soalan pendek.
7. Membaiki gejala: menukar ujian, menambah `try/except` yang menelan ralat, atau
   menapis baris yang gagal.
8. Mempercayai ringkasan sendiri atau ringkasan subagen tanpa membuka fail yang dirujuk.
9. Berkata "tiada" selepas satu carian sahaja. Cari dengan sekurang-kurangnya 2
   cara (nama fail dan kandungan).
10. Jawapan panjang atau penuh istilah dalaman. Ikut peraturan jawapan dalam `CLAUDE.md`.

## Contoh kerja yang siap

Tugasan sebenar (18 Nov 2026): "skill backtest-expert gagal menjalankan skripnya".

```
Matlamat: skill backtest-expert boleh menjalankan skrip penilaiannya dalam repo ini.
Siap bermakna: (1) arahan dalam SKILL.md berjalan dari akar repo, exit 0;
               (2) hanya SKILL.md berubah.
Sudah dibaca: SKILL.md penuh; `ls skills` -> tiada folder; skrip berada di
              .claude/skills/backtest-expert/scripts/evaluate_backtest.py.
Belum diketahui: tiada.
Langkah:
  1. Jalankan skrip dengan laluan sebenar.            Semak: exit 0.          LULUS
  2. Tukar laluan dalam SKILL.md.                     Semak: grep laluan lama. 0 padanan
  3. git diff --stat.                                 Semak: 1 fail berubah.   LULUS
Laporan:
  Dibuat: laluan skrip dalam SKILL.md dibetulkan.
  Disemak: skrip dijalankan dengan contoh dalam SKILL.md -> exit 0, DEPLOY, 81/100.
  Tidak dibuat: ujian repo tidak dijalankan (tiada kod di bawah BacktestShariah2/ berubah).
```

## Senarai semak akhir (jalankan sebelum berkata "siap")

- [ ] Matlamat satu ayat ditulis, dan jawapan menjawab ayat itu.
- [ ] Setiap perkara "siap bermakna" dijalankan semula dan outputnya dibaca.
- [ ] Ujian dan `sahkan.py` dijalankan jika berkenaan; hasilnya dinyatakan.
- [ ] `git diff --stat` hanya menunjukkan fail yang dimaksudkan.
- [ ] 3 nombor dijejak ke sumbernya; 1 dikira semula dengan cara kedua.
- [ ] Tiada larangan bahagian 1 langkah 4 dilanggar.
- [ ] Tiada kesilapan bahagian 5 berlaku.
- [ ] Laporan menyatakan apa yang TIDAK dibuat atau belum disemak.
- [ ] Format jawapan mengikut `CLAUDE.md` (pendek, perkataan biasa, jadual akhir, notifikasi).
