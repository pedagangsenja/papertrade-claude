# CS09 — keluarga K26 "lonjak lalu undur" (zon Fibonacci sebagai parameter): backtest, BUKAN bukti

> **Status keputusan (kad skor, harga 2026-11-13):** TERBUKTI 0 · CALON 0 · BELUM CUKUP 226 · GAGAL 0 · NEGATIF 0. Rejim QQQ OFF sejak 2026-10-16. Hanya **TERBUKTI** layak untuk wang sebenar (`laporan/KAD_SKOR.md`); nombor dalam laporan ini BUKAN keputusan dan tidak boleh dibaca sebagai pangkat untuk wang sebenar.

Dijana `kajian/carian_setup/cs_cs09.py`; peraturan dikunci `kajian/SPEC_CARIAN_SETUP.md` pindaan 16 Nov 2026 (r) (POST-HOC: idea daripada tangkapan skrin pengguna dan penerokaan pada set 431). Jangan sunting secara manual.

## Ringkasan

- Grid 100 varian; skor A > 0: **54** daripada 92 varian yang cukup isyarat.
- Papan 6 setup (henti/keluar dikunci: pegang 20 sesi `X00` + henti 5×ATR14); **dipercayai pada kumpulan B: 4** → kod F: `F96`, `F97`, `F98`, `F99`.
- **Fibonacci istimewa? YA** (kumpulan B): zon iklan 61.8–78.6 % mengatasi purata zon jiran (50–61.8 %, 78.6–100 %) dalam **13** daripada 20 pasangan (tempoh, saiz kaki); kelebihan zon iklan sendiri positif dalam 17 daripada 20. Kumpulan A (maklumat): 13 dan 14.

## Papan (kumpulan B, satu posisi setiap saham)

| # | F | Pencetus | Prasyarat | Penapis saham | Skor A | Belian B (setahun) | Naik lagi % (rawak) | Kelebihan K1 / K2 / K3 | Menang % | Purata % | Dijual ≥ +10 % | Rugi ≥ 8 % | Dipercayai |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| C01 | `F96` | `K26.025` lonjak >= 20% dalam 15 hari lalu undur ke zon 38.2%-78.6% kaki | SPY Peringkat 2 Weinstein (atas SMA150 yang naik) DAN earnings dalam 1-5 sesi akan datang | tiada | +3.4 | 620 (36) | 13.9 (10.0) | +4.2 / +2.1 / +7.2 | 47.6 | -0.3 | 23.4 | 30.6 | **ya** |
| C02 | `F97` | `K26.021` lonjak >= 20% dalam 15 hari lalu undur ke zon 38.2%-50.0% kaki | Mei-Okt DAN earnings dalam 1-5 sesi akan datang | tiada | +3.2 | 373 (22) | 16.9 (12.4) | +3.2 / +3.0 / +10.8 | 57.4 | +2.6 | 26.5 | 23.9 | **ya** |
| C03 | `F98` | `K26.081` lonjak >= 20% dalam 40 hari lalu undur ke zon 38.2%-50.0% kaki | SPY atas SMA200 DAN earnings dalam 1-5 sesi akan datang | hari naik (tutup > buka) | +2.3 | 307 (18) | 13.4 (9.8) | +6.7 / +1.5 / +2.7 | 50.8 | +0.3 | 18.9 | 30.0 | **ya** |
| C04 | `F99` | `K26.085` lonjak >= 20% dalam 40 hari lalu undur ke zon 38.2%-78.6% kaki | SPY atas SMA200 DAN earnings dalam 1-5 sesi akan datang | hari naik (tutup > buka) | +2.3 | 312 (18) | 13.1 (9.7) | +6.4 / +1.4 / +2.7 | 51.0 | +0.4 | 18.9 | 29.8 | **ya** |
| C05 | – | `K26.044` lonjak >= 20% dalam 20 hari lalu undur ke zon 78.6%-100.0% kaki | QQQ dalam 3% dari puncak 52 minggu DAN industri 20% terbawah (pulangan 63 sesi) | >= 30% di bawah puncak 52 minggu | +2.1 | 445 (26) | 10.8 (9.8) | +1.5 / -0.3 / +2.8 | 44.3 | -2.1 | 20.9 | 37.5 | tidak |
| C06 | – | `K26.048` lonjak >= 30% dalam 20 hari lalu undur ke zon 61.8%-78.6% kaki | tiada earnings dalam 20 sesi akan datang | RS >= 70 DAN dalam 15% dari puncak 52 minggu | +2.0 | 231 (14) | 12.6 (11.1) | +3.3 / +2.0 / -4.2 | 53.7 | +2.0 | 27.7 | 24.2 | tidak |

## Sumbangan corak K26 di atas prasyarat (semakan tambahan SELEPAS hasil dilihat; tidak mengubah pendaftaran)

Soalan: adakah corak "lonjak lalu undur" memilih saham yang lebih baik daripada saham LAIN yang lulus prasyarat dan penapis yang sama, pada hari sama dan tercile ATR % sama? Satu posisi, pegang 20 sesi; kumpulan B.

| # | F | Naik lagi % setup | Sumbangan K26 (2 ralat piawai) | K1 / K2 / K3 | Prasyarat + penapis, saham mana-mana: naik lagi % (rawak) | Pencetus K26 sahaja: naik lagi % (rawak) |
|---|---|---|---|---|---|---|
| C01 | `F96` | 13.9 | -0.8 (±2.8) | -2.9 / -1.3 / +3.6 | 11.4 (5.8) | 10.0 (9.7) |
| C02 | `F97` | 16.9 | +0.6 (±3.9) | -1.7 / -0.4 / +7.3 | 12.9 (7.5) | 10.1 (9.6) |
| C03 | `F98` | 13.4 | -0.4 (±4.0) | +1.4 / -1.5 / -1.1 | 11.7 (5.9) | 8.8 (8.2) |
| C04 | `F99` | 13.1 | -0.7 (±3.9) | +0.8 / -1.6 / -1.1 | 11.7 (5.9) | 8.8 (8.3) |
| C05 | – | 10.8 | +0.7 (±2.7) | +0.5 / -0.3 / +3.4 | 10.2 (9.2) | 13.1 (12.0) |
| C06 | – | 12.6 | +1.1 (±4.1) | +3.3 / +1.8 / -5.7 | 5.7 (6.0) | 13.5 (12.3) |

Sumbangan K26 jelas positif (melebihi 2 ralat piawai) bagi **0** daripada 6 setup papan: kelebihan setup datang terutamanya daripada prasyaratnya (earnings dalam 1–5 sesi akan datang, seperti CS05/CS06) dan pemilihan saham turun-naik tinggi, bukan daripada corak "lonjak lalu undur".

## Fibonacci: zon undur, pencetus sahaja (kumpulan B; satu posisi, pegang 20 sesi)

Kelebihan = kadar "naik lagi" (`terus`) tolak saham rawak hari sama × tercile ATR %, mata peratus; purata semua (tempoh, saiz kaki). Zon iklan = 61.8–78.6 %.

| Zon undur | Belian B (jumlah) | Kelebihan B purata | Kelebihan A purata |
|---|---|---|---|
| 0.382-0.500 | 125,539 | +1.0 | +0.4 |
| 0.500-0.618 | 122,635 | +1.0 | +1.0 |
| 0.618-0.786 | 109,597 | +0.8 | +0.6 |
| 0.786-1.000 | 78,951 | +0.7 | +0.1 |
| 0.382-0.786 | 135,762 | +0.9 | +0.1 |

| Tempoh | Kaki | Zon iklan B | Purata zon jiran B | Iklan lebih baik? |
|---|---|---|---|---|
| 10 | 20% | +1.0 | +1.3 | tidak |
| 10 | 30% | +0.7 | +1.0 | tidak |
| 10 | 40% | +1.1 | +1.1 | ya |
| 10 | 50% | +0.5 | +1.1 | tidak |
| 15 | 20% | +1.0 | +0.8 | ya |
| 15 | 30% | +0.8 | +0.7 | ya |
| 15 | 40% | -0.3 | +0.6 | tidak |
| 15 | 50% | -1.4 | +0.7 | tidak |
| 20 | 20% | +1.2 | +1.0 | ya |
| 20 | 30% | +1.2 | +1.1 | ya |
| 20 | 40% | +0.5 | +0.6 | tidak |
| 20 | 50% | -0.6 | +0.4 | tidak |
| 30 | 20% | +1.1 | +0.6 | ya |
| 30 | 30% | +1.5 | +0.7 | ya |
| 30 | 40% | +1.5 | +1.1 | ya |
| 30 | 50% | +1.3 | +1.0 | ya |
| 40 | 20% | +0.7 | +0.5 | ya |
| 40 | 30% | +1.2 | +0.8 | ya |
| 40 | 40% | +1.7 | +1.2 | ya |
| 40 | 50% | +1.8 | +0.9 | ya |

## 10 varian teratas ikut skor A (maklumat)

| Varian | Pencetus | Prasyarat | Penapis | Skor A | n E1 / E2 |
|---|---|---|---|---|---|
| `K26.025` | lonjak >= 20% dalam 15 hari lalu undur ke zon 38.2%-78.6% kaki | SPY Peringkat 2 Weinstein (atas SMA150 yang naik) DAN earnings dalam 1-5 sesi akan datang | tiada | +3.4 | 4,259 / 6,536 |
| `K26.021` | lonjak >= 20% dalam 15 hari lalu undur ke zon 38.2%-50.0% kaki | Mei-Okt DAN earnings dalam 1-5 sesi akan datang | tiada | +3.2 | 3,911 / 5,754 |
| `K26.081` | lonjak >= 20% dalam 40 hari lalu undur ke zon 38.2%-50.0% kaki | SPY atas SMA200 DAN earnings dalam 1-5 sesi akan datang | hari naik (tutup > buka) | +2.3 | 8,982 / 9,561 |
| `K26.085` | lonjak >= 20% dalam 40 hari lalu undur ke zon 38.2%-78.6% kaki | SPY atas SMA200 DAN earnings dalam 1-5 sesi akan datang | hari naik (tutup > buka) | +2.3 | 9,582 / 10,360 |
| `K26.044` | lonjak >= 20% dalam 20 hari lalu undur ke zon 78.6%-100.0% kaki | QQQ dalam 3% dari puncak 52 minggu DAN industri 20% terbawah (pulangan 63 sesi) | >= 30% di bawah puncak 52 minggu | +2.1 | 3,257 / 5,483 |
| `K26.048` | lonjak >= 30% dalam 20 hari lalu undur ke zon 61.8%-78.6% kaki | tiada earnings dalam 20 sesi akan datang | RS >= 70 DAN dalam 15% dari puncak 52 minggu | +2.0 | 1,414 / 3,253 |
| `K26.043` | lonjak >= 20% dalam 20 hari lalu undur ke zon 61.8%-78.6% kaki | Mei-Okt DAN sektor 3 terbawah (pulangan 63 sesi) | tutup > MA200 DAN MA50 > MA200 | +1.8 | 4,642 / 7,243 |
| `K26.045` | lonjak >= 20% dalam 20 hari lalu undur ke zon 38.2%-78.6% kaki | 7 hari pertama bulan DAN earnings dalam 1-5 sesi akan datang | tutup > MA50 DAN MA50 naik (lawan 20 bar lalu) | +1.8 | 5,872 / 8,290 |
| `K26.030` | lonjak >= 30% dalam 15 hari lalu undur ke zon 38.2%-78.6% kaki | QQQ ON | RS >= 90 DAN ATR% >= 4 | +1.8 | 1,238 / 2,994 |
| `K26.001` | lonjak >= 20% dalam 10 hari lalu undur ke zon 38.2%-50.0% kaki | nisbah 4% (10 hari) > 2 | tutup > MA50 DAN Supertrend naik | +1.7 | 2,304 / 3,720 |

Kaveat (dikunci (r)): idea post-hoc; kumpulan B sudah dilihat untuk label lain dan bertindih dengan set 431; tiada saham delist; setup di sini BUKAN calon papertrade tanpa keputusan pengguna berasingan; kedudukan akhir penuh (`hasil/KEDUDUKAN_AKHIR.md`) belum dijana semula dengan setup CS09.
