# jadual/ — prosedur tugasan berjadual

Prompt tugasan berjadual hanya perlu: repo sudah dilampirkan (jangan `add_repo`), `git pull`, kemudian "ikut
`BacktestShariah2/jadual/<fail>.md`". Prosedur disimpan di sini supaya berversi dalam git; peraturan: `standard/tugasan_v3.md`.
Model: `claude-sonnet-5-5` sahaja. Sejarah pengawas dan jadual lama: `standard/SEJARAH_KEPUTUSAN.md`.

## Sekarang (`MOD_ACTIONS` = `bayang`; rutin Claude rasmi)
| Fail | Tugasan berjadual | Masa |
|---|---|---|
| `kemas_kini_0602.md` | Papertrade – Kemas kini 6:02 pagi (`trig_01R2RcT5GZ4xGkncK5xa1jnH`) | 6:02 pagi MYT, Sel–Sab |
| `imbas_2002.md` | Papertrade – Imbas 7:47 malam (`trig_012DQb9KbjfhpKuopsMByNDh`) | 7:47 malam MYT, Isn–Jum |
| `beli_0935.md` | Papertrade – Beli 9:35 NY (`trig_018pfWtxtyMaC6aaThn7UDCo`) | 9:35 pagi New York, Isn–Jum |

GitHub Actions `harian.yml`, `beli.yml`, `petang.yml` berjalan selari ke `BacktestShariah2/bayang/` dan membanding setiap tarikh
MYT yang belum dibanding (`banding_bayang.py belum` → `bayang/BANDING_<tarikh>.md`). Rutin boleh ditembak dua kali, jadi setiap
prosedur rutin bermula dengan "Semak pendua". Pengawas jadual dimatikan 19 Okt 2026.

Penjaga jadual: `.github/workflows/penjaga_jadual.yml` (cron :23 dan :53 setiap jam, setiap push ke `main`, selepas workflow
berjadual selesai) mendispatch workflow yang cetusan cronnya hilang/lewat. Kerana cron GitHub sendiri lewat (median 100–297
minit), tugasan berjadual Claude `trig_01N3Qx1S6bRhf9h5BEKk85bQ` mencetusnya dari luar ke sesi Sonnet khas
`session_018zpLxNRJ3rxZBvGT9yztVT` (run_workflow sahaja, tanpa notifikasi): kini `20 5,6,12,14,22,23 * * 1-6` UTC; cadangan
2 slot (13:41 MYT pasca-harian, 9:50 NY pra-beli) dalam `CADANGAN_JADUAL.md`. Jangan buang atau longgarkan.

## Selepas peralihan (`rasmi`; `PERALIHAN.md`)
| Fail | Bila | Kerja |
|---|---|---|
| (Actions) `harian.yml` → `lejar.yml` → `analisis.yml` | 05:07 UTC Sel–Sab (+ sandaran; penjaga) | kemas kini posisi, imbas, gred, Lejar, Penganalisis |
| (Actions) `petang.yml`, `beli.yml` | 11:47 UTC; 9:40 NY Isn–Jum | gred P sebelum buka; beli maya |
| `tolak_db.md` A pasca-harian | 14:47 MYT Sel–Sab (cadangan) | tunggu harian + lejar + analisis, tolak db, notifikasi malam |
| `tolak_db.md` B pasca-beli | 10:33 NY Isn–Jum (cadangan) | tunggu beli, tolak db, notifikasi beli |
| `mingguan.md` | Ahad 10:47 pagi MYT | universe, sektor, SST, kewangan, peristiwa, akaun Moomoo, sampel Moomoo |
| `notifikasi_harian.md` | 3:17 ptg MYT Sel–Sab | HANYA jika jadual lama dikekalkan (digabung ke tolakan A dalam cadangan) |

Jadual lama yang diluluskan 17/24 Okt 2026 (satu tolakan 10:20 NY Isn–Sab + notifikasi 3:17 ptg MYT) kekal sah sehingga
jadual cadangan diluluskan. Garis masa penuh UTC/MYT/NY (DST tamat 1 Nov 2026) dan lampu dashboard: `CADANGAN_JADUAL.md`.
