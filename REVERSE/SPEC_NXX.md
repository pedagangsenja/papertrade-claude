# SPEC_NXX — pradaftar ujian registry Nxx

**Dikomit sebelum sebarang keputusan dilihat.** Permintaan pengguna 30 Okt 2026: "Nxx list ni
saya nak backtest dahulu."

Ini pradaftar ketujuh dalam REVERSE. Enam yang sebelumnya: `SPEC.md` (fasa 1), `SPEC_1B.md`,
`SPEC_FASA2.md`, `SPEC_SILANG.md`, `SPEC_SETUP.md`, `SPEC_KOMBINASI.md`, `SPEC_PEMBINAAN.md`,
`SPEC_SISTEM.md`. Kesemuanya ditolak. Pradaftar ini mengikut disiplin yang sama.

---

## 1. Soalan

Daripada 147 baris MASUK dalam `data/registry_N.csv`, adakah mana-mana mempunyai **lift
positif atas asas "beli setiap bar"** pada kedua-dua tingkap masa, bertahan pembetulan pelbagai
ujian, dan kekal positif selepas pemenang 5% teratas dibuang?

Bukan "adakah ia menguntungkan". `SETUP.md` sudah mengukur bahawa setup boleh menguntungkan
sambil mempunyai lift **negatif** — 10 daripada 10 setup teratasnya positif di luar sampel
tetapi kesemuanya kalah kepada membeli setiap bar.

## 2. Alam dan data

Sama seperti `SETUP.md` dan `KOMBINASI.md`, supaya keputusan boleh dibandingkan terus:

| | |
|---|---|
| Sumber harga | `AUTOTUNE/.cache_autotune-data-a02` (Release `autotune-data-a02`) |
| Tempoh | 2012–2025 (14 tahun) |
| Penapis cair | median nilai dolar 20 bar >= USD100 ribu, bar mempunyai julat dan volum |
| Bar dengan pulangan hadapan | 10,030,157 (cache `REVERSE/.cache/pul_kombinasi.parquet`) |
| Kos | komisen 0.1% setiap sisi + slippage, sudah termasuk dalam cache |
| LATIH | 2012–2019 |
| TAHAN | 2020–2025 |

**Bias yang diketahui dan tidak boleh dihapus di sini:** alam A02 tiada saham delist
(`SPEC.md`). Ia memihak kepada SEMUA keputusan, termasuk asas, jadi ia tidak memihak kepada
satu setup berbanding yang lain — tetapi ia bermakna tiada nombor mutlak dalam laporan ini
boleh dibaca sebagai jangkaan dunia nyata.

## 3. Reka bentuk: DIFAKTORKAN, bukan silang penuh

Silang penuh 70 masuk x 26 keluar = 1,820 ujian. Itu membunuh FDR tanpa sebab. Reka bentuk
yang betul memfaktorkannya:

**Bahagian A (dijalankan sekarang) — 70 MASUK x 4 keluar asas = 280 ujian.**
Empat keluar itu (`X01` sasaran 1xATR, `X02` sasaran 4xATR, `X03` tiada sasaran pegang 63,
`X04` ekori 2xATR) sudah mempunyai asas terukur dalam `KOMBINASI.md`, jadi lift boleh dikira
terus terhadap asas keluar **yang sama**.

70 MASUK ialah kesemua baris berstatus `SEDIA`, tolak `N121`:

```
N06 N07 N08 N09 N15 N16 N17 N18 N19 N20 N21 N22 N23 N24 N25 N27 N28 N29 N31 N33
N35 N36 N37 N38 N39 N40 N41 N42 N43 N44 N45 N46 N47 N48 N49 N50 N51 N52 N53 N54
N55 N56 N57 N58 N62 N64 N65 N66 N67 N68 N69 N70 N73 N74 N75 N76 N77 N78 N79 N80
N104 N106 N113 N115 N116 N118 N119 N120 N123 N124
```

**`N121` (Weinstein Stage 2) DIKELUARKAN dan statusnya dibetulkan kepada
`PERLU:sejarah_stage`.** Sebabnya diaudit, bukan diandaikan: `data/stage/status.json` ialah
petikan harian (7 commit sahaja), tiada sejarah titik-masa. Ia BOLEH dikira semula daripada
stor harga oleh `standard/stage.py`, tetapi itu larian berasingan.

**Bahagian B (pradaftar, dijalankan kemudian) — 26 KELUAR x 3 masuk tetap = 78 ujian.**
Tiga masuk tetap: `N01` (satu-satunya lift positif yang diketahui), `N76` (`tutup > ma50`,
penapis tunggal paling mudah), dan **tiada penapis** (setiap bar) sebagai asas.

**Jumlah ujian dipradaftar: 280 + 78 = 358.** FDR dikira merentas 358, bukan merentas bahagian.

## 4. Lajur terbitan yang perlu ditambah

12 daripada 70 masuk memerlukan lajur terbitan ringkas yang belum ada. Kesemuanya ditakrifkan
di sini **sebelum** larian supaya tiada kelonggaran selepas melihat keputusan:

| Lajur | Takrif |
|---|---|
| `ema10` | EMA(10) tutup |
| `tinggi20` | tertinggi `tinggi` 20 bar lalu, tidak termasuk bar ini |
| `tinggi_sepanjang` | cummax(`tutup`) hingga bar sebelum |
| `hari_minggu` | 0=Isnin .. 4=Jumaat daripada `date` |
| `bulan` | 1..12 daripada `date` |
| `pos_buka` | (`buka` − `rendah`) / (`tinggi` − `rendah`) |
| `pos_tutup` | (`tutup` − `rendah`) / (`tinggi` − `rendah`) |
| `julat4_min` | benar jika julat bar ini terkecil dalam 4 bar |
| `turun_4d5` | benar jika 4 daripada 5 tutup terakhir lebih rendah daripada sebelumnya |
| `cerun_ma200_21` | `ma200` > `ma200` 21 bar lalu |
| `gap` | `buka` / `tutup[-1]` − 1 |
| `sentuh_ema20` | `rendah` <= `ema20` pada bar ini |

`N104` (kesan hari minggu) diuji sebagai **5 ujian berasingan**, satu setiap hari. `N106`
(Nov–Apr) sebagai 1. Jadi kiraan ujian sebenar bahagian A ialah **280 + 4 = 284**, dan jumlah
dipradaftar **362**. FDR mengira 362.

## 5. Tiga gate — ketiga-tiganya mesti lulus

1. **Lift positif pada KEDUA-DUA tingkap**, dikira terhadap asas **keluar yang sama**
   (kesilapan `SPEC_SETUP.md` §4 ialah menggunakan jangkaan mutlak; ia tidak diulang di sini).
2. **BH-FDR q <= 0.05** merentas 362 ujian, pada t berkelompok **ikut hari beli** (posisi yang
   dibeli pada hari sama bergerak bersama).
3. **Jangkaan selepas membuang 5% pemenang teratas > 0**, pada tingkap TAHAN.

Gate 3 ialah gate yang membunuh segala-galanya setakat ini. `KOMBINASI.md`: 100% daripada 598
setup negatif selepas buang 5% teratas, dan **asasnya juga** (−2.410%). Ia dikekalkan kerana
tanpanya "kelebihan" hanya bermakna "menangkap lebih banyak ekor", yang 8–10 slot tidak boleh
lakukan.

## 6. Semakan pemalsuan (WAJIB dibaca sebelum keputusan lain)

`N01` = `ma10` silang naik `ma20` DAN `vol_n50 >= 1.2` **sudah diukur** dalam `KOMBINASI.md`:
lift `X3` **+0.123 (latih) / +0.392 (tahan)**, n 28,117, jangkaan tahan +2.988%.

Larian ini mesti menghasilkan semula angka itu dalam toleransi ±0.02 mata lift. **Jika tidak,
alat ini rosak dan tiada satu pun keputusan lain boleh dipercayai.** Ia dilaporkan DAHULU,
sebelum mana-mana keputusan baharu.

## 7. Jangkaan priori saya (ditulis sebelum larian)

Saya mesti merekodkan ini supaya saya tidak boleh mendakwa kemudian bahawa saya sudah tahu.
Dua pradaftar terakhir (`SPEC_SILANG` §7, `SPEC_SISTEM` §7) jangkaan priori saya **salah**, dan
kedua-duanya pada ruang yang belum diukur — jadi berat sebelah saya sendiri terukur.

| Gate | Jangkaan saya | Asas |
|---|---|---|
| Gate 1 (lift positif dua tingkap) | **8–25 daripada 284** | `KOMBINASI.md` 3/40 = 7.5%; 284 x 7.5% ≈ 21 |
| Gate 2 (bertahan FDR) | **0–4** | 284 ujian pada q 0.05 bermakna palang tinggi |
| Gate 3 (ekor) | **0** | asas sendiri gagal gate 3; signal mewarisi masalah itu (`SILANG.md`) |

**Keluarga mana saya jangka paling baik:** `MA` dan `KETAT`. Sebabnya `N01` ialah silang MA
dengan pengesahan volum, dan keluarga `KETAT` (NR7, inside day, mampat) memilih bar
volatiliti-rendah sebelum pengembangan — secara struktur ia berbeza daripada penapis keadaan.

**Keluarga mana saya jangka paling teruk:** `KALENDAR` dan `REJIM`, kerana ia memilih MASA
bukan saham, dan pintu masa ialah peruntukan tunai yang disamarkan (lihat `SPEC_SEMUA_N.md`).
Jangkaannya mungkin positif tetapi liftnya dijangka ~0 kerana ia tidak membezakan saham.

## 8. Apa yang akan disimpulkan pada setiap keputusan

| Keputusan | Kesimpulan |
|---|---|
| 0 lulus ketiga-tiga gate | Ruang MASUK registry Nxx ditutup. Berhenti menambah baris MASUK. Keutamaan beralih sepenuhnya kepada paksi GABUNGAN, SAIZ, ALAM, INSTRUMEN. |
| 1–3 lulus | Setiap satu masuk ke Gate C portfolio (8 dan 40 slot, 20 benih, lawan SPUS pada kedua-dua konvensyen) sebelum apa-apa dakwaan dibuat. |
| > 3 lulus | Syak alat rosak dahulu, bukan kejayaan. Jalankan 1000 permutasi label dalam-bulan dan dua bootstrap blok (ticker dan minggu) sebelum melaporkan apa-apa. |

Lift positif **tanpa** gate 3 bukan kegagalan penuh: ia bermakna kelebihan itu nyata tetapi
hidup dalam ekor kanan. Dalam kes itu kesimpulannya ialah **naikkan bilangan slot** (`SZ10`,
`IS02`), bukan guna signal itu pada 8–10 slot.

## 9. Apa yang pradaftar ini TIDAK uji

- Paksi `CARA` — kesemua ujian guna `C01` (beli pada buka berikutnya). Jadi kecacatan henti
  hari-0 (`KOLAM_EKOR.md` §4a) **hadir dalam setiap keputusan di sini**.
- Paksi `GABUNGAN` — setiap baris MASUK ialah syarat `DAN` dalaman, jadi ini ujian `GB01`
  sahaja. `GB02`/`GB04`/`GB08` ialah pradaftar berasingan.
- Paksi `SAIZ`, `ALAM`, `KORELASI`, `IMBANG`, `INSTRUMEN` — dikunci pada asas repo.
- 64 baris MASUK berstatus `PERLU` dan 12 baris `KELUAR` berstatus `PERLU`.

Jadi larian ini menjawab **satu kotak daripada sebelas**, dan saya menyatakannya di sini supaya
keputusannya tidak dibaca lebih luas daripada yang sepatutnya.

---

## 10. Pembetulan pra-larian (30 Okt 2026, sebelum sebarang keputusan dilihat)

Audit pemetaan peraturan → lajur menemui empat baris yang **tidak boleh** diuji sebagai
penapis per-bar. Dibetulkan di sini, bukan selepas melihat keputusan.

| ID | Masalah | Tindakan |
|---|---|---|
| `N77` | "pangkat keratan rentas pulangan 252 hari, **ambil 3 teratas**, imbang bulanan" | **Dikeluarkan.** Ia peraturan URUTAN, bukan penapis. Sumbernya guna alam 9 ETF sektor; alam repo 2,800 saham, jadi "3 teratas" bermakna 0.1% — bukan peraturan yang sama. Padanannya ialah `U11`. |
| `N78` | sama, 3 TERBAWAH 21 hari | **Dikeluarkan.** Sebab sama. |
| `N79` | "2 teratas alam" | **Dikeluarkan.** Sebab sama. |
| `N123` | "gap **earnings**" | **Dikeluarkan.** Perlu tarikh earnings titik-masa; `data/sec/` ada tetapi penyertaannya tugas data berasingan. Status → `PERLU:tarikh_earnings`. |

**Takrif yang ditetapkan di sini supaya tiada kelonggaran kemudian:**

`RS` dalam `N69` dan `N120` = **persentil keratan rentas `rs_spy_6b` dalam tarikh yang sama**
(0–100). `N69` kuintil teratas bermakna persentil >= 80. `N120` `RS >= 70` bermakna
persentil >= 70. Ini satu-satunya tafsiran yang mungkin kerana `rs_spy_6b` ialah nisbah mentah,
bukan rating.

**Kiraan ujian dibetulkan.** Spec §3 dan §4 mengira 284 bagi bahagian A; aritmetik itu salah.
Yang betul:

| | |
|---|---|
| MASUK `SEDIA` | 70 |
| tolak N77, N78, N79, N123 | 66 |
| N104 dipecah 5 hari minggu (+4 topeng) | **70 topeng** |
| × 4 keluar asas | **280 ujian (bahagian A)** |
| Bahagian B: 26 keluar × 3 masuk | **78 ujian** |
| **Jumlah dipradaftar, FDR mengira** | **358** |

Saya menyatakan dengan jelas: 358 < 362, jadi pembetulan ini **melonggarkan** palang FDR
sedikit. Ia dibuat sebelum melihat keputusan, dan sebabnya pemetaan peraturan, bukan hasil.

---

## 11. Pembetulan pra-larian bahagian B (31 Okt 2026 00:10 MY, sebelum keputusan dilihat)

26 keluar `SEDIA` diaudit. Tiga **bukan** keluar per-dagangan dan tidak boleh diuji dalam
rangka ini:

| ID | Masalah | Tindakan |
|---|---|---|
| `X20` | "separa 1/3 pada 2R, ekori baki" — keluar BERPERINGKAT, satu dagangan jadi dua | Dikeluarkan. Perlu rangka saiz, bukan rangka pulangan-setiap-bar. |
| `X31` | "jatuh keluar 3 teratas pangkat 252 hari" — keratan rentas + imbang | Dikeluarkan. Ia paksi `URUTAN` + `IMBANG`, bukan keluar. |
| `X32` | "imbang berkala sahaja" — peringkat portfolio | Dikeluarkan. Ia paksi `IMBANG`. |

**Bahagian B dibetulkan: 23 keluar x 3 masuk tetap = 69 ujian** (bukan 78).

Tiga masuk tetap, ditetapkan di sini: `N115` (Holy Grail — momentum-undur, lulus gate2
bahagian A), `N19` (bawah jalur BB + rsi14 < 30 — lift terbesar bahagian A), dan **tiada
penapis** (setiap bar) sebagai asas.

**Jumlah dipradaftar dikemas: 280 (A, selesai) + 69 (B) = 349.** FDR bahagian B mengira 349.

### Syarat tambahan yang bahagian A dedahkan (spec §5 dipinda untuk B sahaja)

Bahagian A menunjukkan `N16` x `X1` lulus gate 1 dan 2 dengan lift +0.193 **tetapi jangkaan
mutlak -0.088%** — merugikan, kerana asas `X1` sendiri negatif. Gate asal tidak menangkapnya.

**Gate 0 ditambah untuk bahagian B: jangkaan mutlak tingkap TAHAN mesti > 0.** Ia dinyatakan
di sini sebelum larian B, dan ia TIDAK digunakan ke belakang pada keputusan A yang sudah
dilaporkan.

### Jangkaan priori saya untuk bahagian B

Jangkaan priori saya salah tiga kali berturut-turut, kedua-dua kali terakhir ke arah terlalu
rendah. Jadi kali ini saya menyesuaikan ke ATAS dengan sengaja, dan merekodkannya:

| | Jangkaan |
|---|---|
| Gate 0+1 (mutlak > 0 dan lift positif dua tingkap) | 15-35 daripada 69 |
| Gate 2 (FDR m=349) | 3-10 |
| Gate 3 (ekor mutlak > 0) | **0-2** |

**Keluar mana saya jangka terbaik:** `X29` (pegang tetap 10 bar) dan `X33` (keluar pada tutup
sesi masuk) — kerana `KOMBINASI.md` sudah ukur bahawa SETIAP sasaran untung merugikan, dan
keluar terpantas mengelak paling banyak masa dalam pasaran. **Terburuk:** `X10` (sasaran 2%
tetap) dan `X27` (sasaran +3%), atas sebab yang sama tetapi bertentangan arah.

**Saya jangka asas tanpa-penapis akan mengalahkan kedua-dua N115 dan N19 pada sekurang-kurangnya
separuh keluar**, kerana itu yang berlaku pada 598 setup `SETUP.md`.
