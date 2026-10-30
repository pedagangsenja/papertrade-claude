# SPEC SISTEM — pradaftar, 30 Okt 2026

**Dikomit SEBELUM apa-apa keputusan dilihat.** Keputusan pengguna 30 Okt 2026.

## 1. Mengapa ini berbeza daripada SEMUA ujian terdahulu

Setiap ujian sebelum ini menguji **PENAPIS MASUK**. `SETUP.md` menutup ruang itu: 0 daripada 598
penapis mengalahkan "beli setiap bar", kerana setiap penapis membuang bar dan pulangan hidup dalam
ekor yang dibuang.

Ujian ini menguji **DUA SISTEM LENGKAP** — masuk **dan** pegang **dan** keluar **dan** saiz **dan**
rejim. Itu arah yang data sendiri tunjuk: `PEMBINAAN.md` mendapati perubahan pembinaan memperbaiki
kedua-dua paksi **+7.90 mata pulangan dan +14.69 mata MDD**, lebih besar daripada apa-apa yang
mana-mana pemicu hasilkan; `KOLAM_EKOR.md` mendapati henti sahaja berharga **9.79 mata/tahun**.

Dua tiang yang saya **tinggalkan** daripada 672 setup, dan yang merupakan teras kaedah pakar,
dimasukkan di sini: **kekuatan relatif** dan **rejim pasaran**.

## 2. Sistem A — pakej O'Neil / Minervini / Qullamaggie

Mekanisasi saya bagi unsur yang ketiga-tiga mereka kongsi. Saya nyatakan terus bahawa ini
**anggaran**; kaedah asal mengandungi pertimbangan yang tidak boleh dikodkan.

| Unsur | Peraturan |
|---|---|
| Alam | `rs_spy_6b` dalam **kuintil teratas** rentas-keratan hari itu **DAN** `sektor_atas_ma50` |
| Rejim | beli hanya bila SPY **atas MA50 DAN MA200** |
| Masuk | `donchian20` **ATAU** `breakout_asas` **ATAU** `vcp`; masuk pada buka esok |
| Henti awal | **−8%** daripada harga masuk (gaya O'Neil/Minervini, bukan −2×ATR) |
| Jual separa | **1/3** posisi pada **+10%** atau **hari ke-5**, mana dahulu |
| Ekor baki | keluar bila **tutup < MA20** |
| Saiz | sama rata merentas slot |
| Slot | 10 |

## 3. Sistem B — momentum Clenow (*Stocks on the Move*)

Peraturan diterbitkan penuh; ini pelaksanaan setia.

| Unsur | Peraturan |
|---|---|
| Skor | kecerunan regresi eksponen 90 hari (disetahunkan) **×** R² regresi itu |
| Diskualifikasi | pernah bergerak **> 15%** dalam satu hari dalam 90 hari lepas |
| Rejim | beli hanya bila SPY **atas MA200** |
| Pemeringkatan | susun menurun ikut skor; pegang **20 teratas** |
| Saiz | **pariti risiko**: `nilai = ekuiti × 0.001 / ATR20%` |
| Imbang portfolio | setiap **Rabu**: jual jika keluar **20% teratas** peringkat, **atau** tutup < MA100 sendiri, **atau** diskualifikasi |
| Imbang saiz | setiap **Rabu kedua** |

## 4. Populasi, kos, penanda aras

- Alam Release `autotune-data-a02`, 2012–2025, penapis kecairan median nilai 20 bar ≥ USD 100,000.
- Kos: `REVERSE/teras/kos.py` tanpa perubahan (komisen 0.1%/sisi + slippage berperingkat).
- Tunai tidak berbunga (0%) — merugikan sistem dengan sengaja.
- Panjang sahaja, tiada margin, tiada leverage.
- Penanda aras **SPUS**, tingkap keputusan **2020–2025**, **kedua-dua** konvensyen
  (median tahunan dan CAGR tingkap) seperti `PEMBINAAN.md`.
- **20 benih** kerana hingar pemilihan 17.3 mata/tahun (`KEPEKATAN_BENIH.md`). Benih menukar
  susunan pemecah seri sahaja, bukan peraturan.

## 5. Gate — kesemuanya diperlukan

**LULUS** hanya jika sekurang-kurangnya satu sistem memenuhi **KETIGA-TIGA**:

1. **Pulangan**: median 20 benih CAGR 2020–2025 > CAGR SPUS
2. **MDD**: median 20 benih MDD lebih cetek daripada MDD SPUS
3. **Di luar hingar**: **p10** 20 benih CAGR masih > CAGR SPUS

Keputusan mesti bertahan pada **kedua-dua** konvensyen penanda aras.

Jika satu sistem lulus 1 dan 2 tetapi gagal 3: dilaporkan sebagai **dalam hingar pemilihan**,
bukan lulus.

## 6. Grid TETAP: dua sistem, tiada varian

**Tiada parameter ditala. Tiada varian diuji. Tiada pengoptimum** (`ARAHAN`). Setiap nilai di atas
diambil daripada sumber terbitannya atau daripada repo, bukan dicari. Menguji varian dan melaporkan
yang terbaik adalah kesilapan yang `SETUP.md` §4 saya sendiri lakukan; ia tidak diulang.

## 7. Jangkaan priori (ditulis sebelum larian)

**Sistem B (Clenow)**: saya jangka ia **menghampiri** SPUS pada pulangan tetapi **gagal syarat
MDD**. Sebabnya momentum rentas-keratan direplikasi secara bebas merentas 40+ negara, jadi saya
tidak jangka ia kosong — tetapi kemalangan momentum (2009, 2020) memberi drawdown lebih dalam
daripada indeks, dan SPUS MDD −10.14% (median tahunan) ialah paras yang tinggi.

**Sistem A**: saya **tidak pasti**. Ia mengandungi dua tiang yang saya tinggalkan sebelum ini
(RS, rejim) dan keluar yang jauh lebih baik daripada 63-hari-tetap. Tetapi `data/trend/status.json`
repo sudah mendapati Trend Template gaya Minervini tidak meramal pulangan 3–30 hari.

**Keyakinan saya rendah pada kedua-duanya, dan itu sebab terbaik untuk menjalankannya.**
Pradaftar `SPEC_SILANG.md` §7 saya salah kerana saya memanjangkan kecenderungan am kepada ruang
yang belum diukur; ini ruang yang belum diukur.

## 8. Apa yang ujian ini TIDAK boleh buktikan

- Ia tidak boleh mencapai **+10%/bulan** (`SASARAN.md`). Momentum akademik memberi kira-kira
  pasaran + beberapa mata setahun, bukan 3.14×/tahun.
- LULUS bermakna "sistem ini mengalahkan SPUS dalam backtest 2020–2025" — ia **mesti** disahkan
  ke hadapan sebagai lorong `portfolio_slot/` sebelum dipercayai.
- Sistem A ialah **anggaran mekanikal** kaedah diskresi. Kegagalannya bukan bukti pakar itu salah
  (`laporan/KAEDAH_TERBAIK.md` §5).
