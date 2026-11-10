# Kajian rejim QQQ dan industri sebelum membeli (10 Nov 2026)

Soalan pengguna: adakah rejim QQQ benar-benar penting sebelum membeli saham, dan perlukah sektor/industri dilihat dahulu sebelum memilih saham? Contoh pengguna: semikonduktor naik serentak pada April 2026.

Skrip: `kajian/rejim_industri/rejim_industri.py` (tiada fail ditulis; output dicetak). **Bukan pradaftar** — kajian penerokaan untuk menjawab soalan, bukan eksperimen ke-7 baris gilir E dan bukan kaedah Mxx/Nxx baharu. Keputusan ialah maklumat; ia tidak mengubah kad skor.

## Data
- QQQ harian 2019-01-02 hingga 2026-11-09: `data_mentah/index_benchmark.csv` (hingga Okt 2024) disambung `data/harga/stor/harga_idx.csv` (490 hari bertindih, nisbah 1.000000). QQQ sebelum 2019 tiada dalam repo; muat turun dari luar ditolak dalam sesi ini.
- Rejim ON = QQQ tutup > SMA50 **dan** SMA10 > SMA20 (definisi `standard/SPEC_KAD_SKOR.md`). Hari ON 61% (2019–2026).
- Indeks industri harian sama rata 2005–2026-10-16, 3,855 saham AS, industri Moomoo (`kajian/industri/industri_harian.csv.gz`); industri dengan ≥ 5 ahli sahaja.
- Saham individu: stor harga repo (864 saham dengan ≥ 250 hari, Sep 2024 – Nov 2026), industri daripada `papertrade/peta_industri.csv`.

## 1. Rejim QQQ: brek risiko, bukan peramal pulangan

Pulangan hadapan selepas isyarat pada tutup (t+1 … t+H), 2019–2026:

| Siri | Ufuk | OFF: min / median / positif | ON: min / median / positif |
|---|---|---|---|
| QQQ | 21 sesi | +2.84% / +3.44% / 69% | +1.08% / +1.99% / 64% |
| Purata saham (sama rata, luas) | 21 sesi | +1.15% / +1.78% / 60% | −0.01% / +0.29% / 52% |
| Purata saham | 10 sesi | +0.30% / +1.02% / 57% | +0.15% / +0.08% / 51% |

Pulangan selepas hari OFF **tidak lebih rendah**; ia lebih tinggi tetapi lebih berselerak (sisihan QQQ 21 sesi 6.9% lawan 5.6%). Lantunan terbesar bermula ketika rejim masih OFF.

Pegang QQQ hanya ketika ON (isyarat tutup t, pulangan t+1), lawan pegang terus dan lawan pendedahan statik yang sama:

| | CAGR | MDD | 2022 | 2025 MDD |
|---|---|---|---|---|
| Pegang QQQ 100% | 20.1% | −35.1% | −32.6% | −22.8% |
| QQQ bila ON sahaja (purata pendedahan 61%) | 13.6% | **−15.5%** | −7.4% | −6.1% |
| QQQ statik 61% + tunai | 12.6% | −22.4% | −20.4% | −14.4% |

Bacaan: rejim **menukar pulangan dengan kedalaman kejatuhan**. Pada pendedahan sama ia lebih baik daripada berat statik pada kedua-dua paksi dalam tingkap ini — tetapi ini ujian pada **indeks itu sendiri**, satu tingkap 7 tahun dengan tiga kejatuhan besar (2020, 2022, 2025), dan peraturan rejim ditetapkan 7 Nov 2026 selepas melihat data (dalam sampel). Untuk **portfolio saham**, kajian terdahulu tidak menyokong rejim sebagai penambah pulangan: penapis SPY > SMA200 menurunkan CAGR tanpa menurunkan MDD (`KAJIAN_PORTFOLIO.md`), dan pada pendedahan sama SPUS + tunai mengalahkan Clenow berejim (`REVERSE/SISTEM.md`). Data langsung Papertrade C: belian dalam OFF −5.40% setiap dagangan, dalam ON −3.62% (`FABLE_PENILAIAN.md` §5).

Kesimpulan §1: guna rejim untuk menentukan **sama ada / berapa banyak** membeli (OFF = tiada belian baharu), bukan untuk memilih saham dan bukan sebagai jangkaan pasaran akan naik.

## 2. Berapa banyak pergerakan saham datang daripada pasaran dan industri

R² harian (Sep 2024 – Nov 2026): regresi pulangan saham atas QQQ, kemudian tambah indeks industri rakan (tanpa saham itu, ditolak QQQ).

| Kumpulan | QQQ | Industri (tambahan) | Saham sendiri |
|---|---|---|---|
| Median 864 saham, 75 industri | 7% | 17% | 68% |
| Semikonduktor (49 saham) | 39% | 13% | 44% |
| Industri paling "serentak" | Pembinaan kediaman 76%, Emas 69%, Minyak & gas bersepadu 64%, E&P 60% (bahagian industri) | | |

Dua pertiga pergerakan harian saham biasa ialah milik saham itu sendiri. Semikonduktor berbeza: lebih separuh daripada QQQ + industri — sebab ia kelihatan "naik serentak". Komoditi (emas, minyak) dan pembinaan kediaman lebih bergantung pada industri, bukan QQQ.

## 3. Membeli industri teratas: hampir syiling

Industri dipangkat ikut pulangan 21 sesi; 20% teratas (A) lawan 20% terbawah (E); lebihan 21 sesi berikutnya (masuk esok) berbanding purata semua industri; sampel tidak bertindih setiap 21 sesi, 6 ofset.

| Tingkap | A | E | A−E | t (ofset 0) | A > E |
|---|---|---|---|---|---|
| 2005–2026 | +0.06% | −0.12% | +0.18% | ≈ 0 | 51% bulan |
| 2019–2026 | +0.06% | −0.30% | +0.35% | 0.63 | 52% bulan |
| 2019–2026, QQQ ON | | | +0.66% | 1.16 | |
| 2019–2026, QQQ OFF | | | −0.13% | −0.27 | |

- Industri 20% teratas masih 20% teratas selepas 21 sesi: **23%**.
- Semikonduktor apabila 20% teratas (2005–2026, n 394 sampel): lebihan purata +1.05% tetapi median +0.24%, positif 52% — purata ditarik oleh ekor kanan.
- Selaras dengan `KAJIAN_GRED_KUMPULAN.md`: gred Weinstein + 1 bulan (definisi lebih baik daripada 1 bulan sahaja) A−E +0.40% / 21 hari, t 1.49; set Shariah 431 +0.15%, t 0.44; terbalik ketika SPY < SMA200. Kajian ini menambah: corak yang sama berlaku ikut rejim **QQQ** — sedikit positif dalam ON, hilang/terbalik dalam OFF.
- Gred **sektor** (11 kumpulan) tidak membantu memilih saham (kajian 18 Okt).

## 4. Kes semikonduktor 2026

| Tarikh | Peristiwa |
|---|---|
| 30 Mac | QQQ dasar (−9.0% sejak 31 Dis). Semiconductors +4.1% dan Semi Equipment +22.9% sejak 31 Dis — sudah kuat relatif semasa pasaran jatuh |
| 1 Apr | Kedua-dua industri masuk 20% teratas (pangkat 1 bulan) |
| 13 Apr | QQQ ON |
| 31 Mac → 15 Jun | Semiconductors **+104.5%**, Semi Equipment +72.7%, QQQ +28.9%, purata saham +10.1%; 96% saham semikonduktor dalam stor naik (median +77.6%) lawan 64% saham lain (median +6.8%) |
| 16 Jun | QQQ OFF |
| 22 Jun | Semikonduktor **masih** persentil 97–100 (kelihatan "industri terkuat") |
| 22 Jun → 21 sesi | Semiconductors −18.5%, Semi Equipment −19.1%; hingga 16 Okt −34.3% / −37.6% |
| Pertengahan Jul | Pangkat jatuh ke persentil 4–13 |
| 15 Jun → 6 Nov | 96% saham semikonduktor turun (median −46.9%) lawan 52% saham lain (median −0.7%) |

Masuk pada isyarat industri (1 Apr) memberi +50.6% dalam 21 sesi dan +75.4% dalam 63 sesi (purata saham +7.6% / +10.3%). Tetapi isyarat yang **sama** masih menyala pada 22 Jun, betul-betul sebelum kejatuhan. Pemangkat industri tidak tahu bila trend tamat; yang memotong kerugian ialah **keluar** (rejim OFF 16 Jun, Chandelier 4×ATR), selaras dengan "keluar ~12× lebih berpengaruh daripada masuk" (`REVERSE/NXX_KELUAR.md`). Mengikut sejarah 2005–2026 (§3), April 2026 ialah ekor kanan yang jarang, bukan hasil biasa apabila semikonduktor teratas.

## Kesimpulan — urutan yang disokong data
1. **Rejim QQQ dahulu**: menentukan sama ada / berapa banyak membeli (OFF = tiada belian baharu). Kesannya pada risiko, bukan pada jangkaan pulangan.
2. **Pilih saham ikut kaedah**, bukan ikut sektor/industri terkuat (A−E hampir syiling; kekal teratas hanya 23%).
3. **Industri sebagai kawalan risiko**: had 1 saham setiap industri (`REVERSE/KEPUTUSAN_AKHIR.md` dapatan 3) — elak 6/8 slot dalam satu industri seperti semikonduktor Jun 2026 yang jatuh bersama (96% turun).
4. **Keluar ialah lever terbesar**: Chandelier 4×ATR tutup (lorong 2).

## Had
- QQQ hanya 2019–2026 (≈ 7.8 tahun, 735 hari OFF); keputusan rejim bergantung pada tiga kejatuhan besar.
- Peraturan rejim ditetapkan selepas melihat data (7 Nov 2026); ujian pada QQQ sendiri, bukan portfolio saham.
- Indeks industri sama rata, tiada saham delist (bias survivorship); peta industri bukan titik-masa.
- §2 ialah R² harian; pada ufuk bulanan bahagian pasaran/industri boleh berbeza. Stor harga hanya Sep 2024 – Nov 2026.
- Tiada kawalan pelbagai ujian; nombor t ialah petunjuk, bukan gate.
