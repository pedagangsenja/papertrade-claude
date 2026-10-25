# CADANGAN jadual operasi selepas peralihan (25 Okt 2026) — menunggu kelulusan pengguna

Pratonton sahaja (cawangan `pt/ops`). TIADA tugasan berjadual diubah dan tiada workflow dicetus semasa menyediakan cadangan ini;
arahan `update_trigger` / `create_trigger` di §5 untuk dijalankan hanya selepas pengguna meluluskan. Peraturan berkaitan:
`standard/tugasan_v3.md` §12.11–§12.13. Data masa: larian GitHub 21–24 Okt 2026 (`mcp__github__actions_list`, baca sahaja).

## 1. Masalah (audit operasi 25 Okt 2026)
1. Tolakan db 10:20 NY (jadual lulus 17 Okt): data sesi D sampai di dashboard ~50 minit SELEPAS buka D+1 (panel Esok basi
   sepanjang pra-buka MYT), dan hanya 4–7 minit selepas beli (beli dispatch penjaga 22–23 Okt: 10:13–10:16 NY, siap 10:16–10:25).
2. DST AS tamat Ahad 1 Nov 2026: `trig_01N3Qx1S6bRhf9h5BEKk85bQ` (cron UTC tetap `20 5,6,12,14,22,23 * * 1-6`) — slot 14:20 UTC
   menjadi 9:20 EST, sebelum gerbang beli 9:31; cetusan 13:40 UTC `beli.yml` menjadi 8:40 EST (larian kosong). Selepas itu
   tiada slot Claude hingga 22:20 UTC (> had beli 16:45 NY), jadi belian bergantung pada cron GitHub yang lewat median 100–297
   minit.
3. Penjaga mencetus LLM 36 kali seminggu (6 × Isn–Sab) hanya sebagai cron; 22:20/23:20 UTC tidak diperlukan selepas rutin 6:02
   dimatikan.
4. Rantai harian → lejar → analisis tidak automatik bagi larian dispatch bot (GITHUB_TOKEN tidak menjana `workflow_run`/push):
   24 Okt harian 06:21–06:48 UTC, Lejar baru 07:25–07:31, Penganalisis 07:31–07:32.

## 2. Garis masa cadangan (hari dagangan sesi D)
| Peristiwa | UTC (EDT, hingga 31 Okt) | UTC (EST, dari 1 Nov) | MYT (EDT / EST) | Nota |
|---|---|---|---|---|
| Tutup AS sesi D | 20:00 D | 21:00 D | 04:00 / 05:00 D+1 | |
| `harga_harian.yml` | 21:37 D, 00:23 D+1 | sama | | data < 00:20 UTC belum muktamad |
| `harian.yml` cron | 05:07 D+1 | sama | 13:07 | biasanya lewat; penjaga |
| **Penjaga P1 pasca-harian** | 05:41 | sama | 13:41 | dispatch harian (lewat > 30 min) dan workflow pagi lain |
| `harian.yml` siap | ~06:15 | sama | ~14:15 | larian 27–34 minit |
| `lejar.yml` → `analisis.yml` | cron 06:17; dengan C1 sebaik harian siap | sama | ~14:25 | lejar ~6 min, analisis ~1 min |
| **Tolak db A** | 06:47 (+ tunggu ≤ 60 min) | sama | 14:47 (≤ 15:47) | sebelum 21:00 MYT; notifikasi malam |
| `petang.yml` | 11:47, 12:17 | sama | 19:47 / 20:17 | NY 07:47 EDT / 06:47 EST |
| Buka AS D+1 | 13:30 | 14:30 | 21:30 / 22:30 | |
| `beli.yml` cron | 13:40 (9:40 NY), 14:40 | 13:40 (8:40 NY, kosong), 14:40 (9:40 NY) | | gerbang 9:31–17:00 NY |
| **Penjaga P2 pra-beli** | 13:50 | 14:50 | 21:50 / 22:50 | 9:50 NY; `LEWAT_KHAS` beli 8 min |
| **Tolak db B** | 14:33 (+ tunggu ≤ 30 min) | 15:33 | 22:33 / 23:33 | 10:33 NY; juga slot penjaga "10:30 NY" |

Tolak A dan P1 memakai `CRON_TZ=Asia/Kuala_Lumpur` kerana rantai harian ditambat pada cron UTC GitHub (05:07/06:17 UTC) dan data
yfinance muktamad (≥ 00:20 UTC); MYT tiada DST, jadi jamnya tetap dalam UTC. `CRON_TZ=America/New_York` bagi A akan menganjak
tolakan sejam lewat pada 1 Nov tanpa sebab. Slot yang ditambat pada pasaran (P2, B) memakai `America/New_York` (ikut DST).

## 3. Rantai C1 (cadangan perubahan `harian.yml`; BELUM dibuat — di luar skop "perubahan dinyatakan")
Selepas push berjaya, `harian.yml` mencetus `lejar.yml` terus (seperti `lejar.yml` mencetus `analisis.yml`), supaya tolakan A
pada 06:47 UTC tidak perlu menunggu cron 06:17 yang lewat. Lejar idempoten (sesi diproses sekali) dan larian dispatch bot
mencetus `analisis.yml` melalui langkah akhir `lejar.yml`. Ia juga mengelak `harian.yml` dan `lejar.yml` menulis
`data/harga/stor/` serentak (konflik rebase kini gagal dengan jelas tanpa `-X theirs`).
```yaml
permissions:
  contents: write
  actions: write          # tambah
# … langkah akhir job harian, selepas "Commit dan push":
      - name: Cetus Lejar penuh (rantai harian -> lejar -> analisis)
        if: success() && steps.malam.outputs.baru == 'ya'
        env:
          GH_TOKEN: ${{ github.token }}
        run: gh workflow run lejar.yml --ref main --repo "$GITHUB_REPOSITORY"
```

## 4. Cron cadangan (tugasan berjadual Claude)
| Tugasan | Cron | Sesi | Ganti |
|---|---|---|---|
| Penjaga P1 pasca-harian | `CRON_TZ=Asia/Kuala_Lumpur 41 13 * * 2-6` | persistent `session_018zpLxNRJ3rxZBvGT9yztVT` | slot 05:20, 06:20 UTC |
| Penjaga P2 pra-beli | `CRON_TZ=America/New_York 50 9 * * 1-5` | persistent `session_018zpLxNRJ3rxZBvGT9yztVT` | slot 12:20, 14:20, 22:20, 23:20 UTC |
| Penjaga "10:30 NY" | digabung ke tolak db B (langkah 2 `notifikasi.py sedia --untuk beli` + tembak `beli.yml`) | — | — |
| Tolak db A pasca-harian | `CRON_TZ=Asia/Kuala_Lumpur 47 14 * * 2-6` | baharu setiap kali | tolak 10:20 NY + notifikasi 3:17 ptg MYT |
| Tolak db B pasca-beli | `CRON_TZ=America/New_York 33 10 * * 1-5` | baharu setiap kali | tolak 10:20 NY |
| Mingguan | `CRON_TZ=Asia/Kuala_Lumpur 47 10 * * 0` (tidak berubah) | baharu setiap kali | — |

LLM seminggu: 5 + 5 (penjaga) + 5 + 5 (tolak) + 1 (mingguan) = **21**, lawan jadual lama 36 + 6 + 5 + 1 = 48. Petang (gred P,
had 9:15 NY) kekal dijaga penjaga GitHub sahaja; jika perlu, tambah slot `CRON_TZ=America/New_York 41 8 * * 1-5`.

### Lampu dashboard (`jangkaSesi`, `standard/dashboard_v2.html`; fail agen lain — cadangan sahaja)
| Saluran | Sekarang | Cadangan (selepas tolak A/B) |
|---|---|---|
| Harga & posisi, Posisi C, Trend, Lorong 2, Watchlist, MAE/MFE (`js`) | `jangkaSesi(23)` = sesi t sedia 23:00 UTC t (rutin 6:02 MYT) | `jangkaSesi(31.75)` = sesi t sedia 07:45 UTC t+1 (15:45 MYT; tolak A + tunggu 60 min) |
| Lejar Penuh, Penganalisis, Portfolio 10 slot (`jl`) | `hariKerjaSebelum(js)` (satu sesi di belakang) | `js` (tolak A menunggu Lejar + Penganalisis sesi sama) |
| SST (`j2`, ≤ 2 sesi) | `hariKerjaSebelum(jl)` | `hariKerjaSebelum(hariKerjaSebelum(js))` (makna kekal) |
| Belian 9:35 NY (`jb`) | `jangkaSesi(10.85, true)` = 10:51 NY | `jangkaSesi(11.1, true)` = 11:06 NY (tolak B 10:33 + tunggu 30 min) |

Tanpa perubahan ini, dengan jadual lama 10:20 NY, saluran `js` "lewat" dari 23:00 UTC hingga ~14:20/15:20 UTC setiap hari.
"Kemas kini terakhir" (merah > 30 jam; 74 jam merentas hujung minggu) kekal sesuai: jurang terpanjang Sab 06:47 UTC → Isn
14:33/15:33 UTC ≈ 56–57 jam. Teks tip `data_kini` ("ditolak … selepas belian 9:35 NY") perlu dikemas kini.

## 5. Arahan tugasan berjadual (JANGAN jalankan sebelum kelulusan pengguna)
Peralihan `trig_01MUQxMSZmi3HroCCApwit2b` (26 Okt 01:00 UTC) membaca `PERALIHAN.md` di `main`, iaitu jadual LAMA (cawangan ini
belum digabung). Pilihan: (a) biarkan peralihan mencipta jadual lama, kemudian selepas kelulusan jalankan 1–7 di bawah
(senaraikan dahulu dengan `list_triggers` untuk ID tugasan tolak db 10:20 NY dan notifikasi 3:17 ptg yang dicipta peralihan);
atau (b) jika diluluskan sebelum 26 Okt 01:00 UTC, gabung cawangan ini dahulu (di luar tetingkap 05:00–13:30 UTC) dan
kemas kini prompt `trig_01MUQxMSZmi3HroCCApwit2b` supaya merujuk `PERALIHAN.md` langkah 5 "JIKA … diluluskan".
1. `update_trigger` `trig_01N3Qx1S6bRhf9h5BEKk85bQ`: `name` "Cetus penjaga jadual – pra-beli 9:50 NY",
   `cron_expression` "CRON_TZ=America/New_York 50 9 * * 1-5" (prompt tidak berubah).
2. `create_trigger`: `name` "Cetus penjaga jadual – pasca-harian", `cron_expression` "CRON_TZ=Asia/Kuala_Lumpur 41 13 * * 2-6",
   `persistent_session_id` "session_018zpLxNRJ3rxZBvGT9yztVT", `initiation` "human_request", `prompt` sama dengan
   `trig_01N3Qx…`: "Cetus penjaga_jadual.yml sekarang seperti arahan pertama sesi ini (run_workflow, ref main; cuba sekali lagi
   jika gagal). Satu baris keputusan sahaja; tiada kerja lain, tiada PushNotification."
3. `create_trigger` (atau `update_trigger` tugasan tolak db 10:20 NY yang dicipta peralihan): `name` "Papertrade – Tolak db A
   pasca-harian", `cron_expression` "CRON_TZ=Asia/Kuala_Lumpur 47 14 * * 2-6", `create_new_session_on_fire` true, `connectors`
   hanya yang perlu (tiada Moomoo/SST), `notifications` {} (prosedur menghantar PushNotification sendiri), `initiation`
   "human_request", `prompt`: "Larian berjadual: tolak db dashboard bahagian A (pasca-harian). Automatik; jangan tanya soalan.
   Repo pedagangsenja/papertrade-claude sudah dilampirkan (JANGAN guna add_repo). `git checkout main && git pull --rebase origin
   main`; baca CLAUDE.md, kemudian IKUT TEPAT BacktestShariah2/jadual/tolak_db.md bahagian A. Model Sonnet. Tiada order, tiada
   wang sebenar. Kalau tak beli, cakap tak beli." Model: `claude-sonnet-5-5` (sesi baharu mewarisi model persekitaran; sahkan).
4. `create_trigger`: `name` "Papertrade – Tolak db B pasca-beli", `cron_expression` "CRON_TZ=America/New_York 33 10 * * 1-5",
   lain-lain sama dengan 3 tetapi "bahagian B (pasca-beli)".
5. Tugasan notifikasi harian 3:17 ptg MYT (jika dicipta peralihan): `update_trigger` `enabled` false (digabung ke A).
6. `update_trigger` `trig_01LmjLfYCAhTPyqnaqozLWBq` (Tala semula suku, 1 Jan 2027): prompt masih "muat turun stor harga (aset
   dashboard harian/status → harga_aset A/B/idx)" — aset itu tersangkut 12 Okt; ganti dengan "stor harga repo
   BacktestShariah2/data/harga/stor/ (WFO/jadual/tala_suku.md langkah 2)".
7. Prompt `trig_012DQb9KbjfhpKuopsMByNDh` (imbas) masih "imbas 87 kaedah"; tidak perlu dibetulkan kerana dimatikan pada peralihan
   (tugasan_v3 §3 menang: 134 kaedah).
Pemerhatian: `trig_01CkyFZsHK42BXBwY6bkmEqT` (analisis mingguan Sabtu) menulis db `analisis/sebenar` yang tidak dilanggan halaman
(audit dashboard 24 Okt); keputusan pengguna sama ada dikekalkan.

## 6. Perubahan dalam cawangan ini yang menyokong jadual
- `penjaga_jadual.py`: `LEWAT_KHAS = {'beli.yml': 8}` (slot 9:50 NY bertindak ~10 minit selepas cron 9:40 NY; diuji EDT/EST).
- `notifikasi.py sedia --untuk malam|beli`: kesediaan harian + Lejar + Penganalisis / belian, senarai `tembak`; `--amaran` dan
  `--db`: SST/EDGAR/kalendar/db ≥ 80% dalam notifikasi.
- `tolak_db.md` A/B, `PERALIHAN.md` langkah 1 & 5, `README.md`, `notifikasi_harian.md` (gabung), `mingguan.md` 7d (sampel
  Moomoo mingguan menggantikan semakan harian).
- `harian.yml`, `beli.yml`, `petang.yml`: tanpa `-X theirs` (rebase biasa, maks 3 kali, `::error::` dengan senarai fail
  bercanggah); `harian.yml` membanding SEMUA tarikh yang belum dibanding (`banding_bayang.py belum`).

## 7. Tindakan yang HANYA pengguna boleh buat
1. **Rahsia `SEC_USER_AGENT`** (EDGAR tidak aktif tanpanya): GitHub repo → Settings → Secrets and variables → Actions → New
   repository secret, nilai "<nama> <e-mel hubungan>" (diwajibkan SEC; rahsia tidak terdedah dalam repo awam). Kemudian
   dispatch `edgar.yml` dengan `mula` (cth. 2026-10-01) untuk isi semula.
2. **Sahkan semula penyambung SST** di tetapan penyambung claude.ai (tiada data SST baharu dalam repo selepas sesi 20 Okt 2026;
   log rutin "SST tidak tersedia (perlu kebenaran semula)").
3. **Matikan alat order di tetapan penyambung Moomoo** claude.ai (hook projek hanya melindungi sesi Claude Code yang memuat
   `.claude/settings.json`; chat claude.ai dan tugasan lama tidak): `trading_order_place`, `trading_order_confirm`,
   `trading_order_cancel`, `trading_order_replace`, `sim_trade_input_order`, `sim_trade_modify_order`, `sim_trade_cancel_order`,
   `crypto_account_create_order`, `crypto_account_modify_order`, `crypto_account_cancel_order`.
4. **Padam tugasan berjadual lama yang dimatikan** (`list_triggers` 25 Okt 2026). Keutamaan — mengandungi arahan order simulasi
   atau penyambung Moomoo penuh dengan mod auto:
   - `trig_01HHsqGGQWhMqYK48A78UFQ6` "Beli Papertrade Shariah" (8 Okt): "WAJIB: guna HANYA `mcp__Moo_Moo__sim_trade_input_order`".
   - `trig_012FxdyuvKyJkx6LR7tDohhr` "Harian v2 – Beli bila pasaran AS buka" (12 Okt): "… sim_trade_input_order, order pasaran …".
   - `trig_01XG8vjsP1jzYs1L7d5PhKX2` "Harian v2 – Beli bila pasaran AS buka (Project 2)" (13 Okt): melarang `sim_trade_*` tetapi
     penyambung Moo_Moo penuh, `permission_mode` auto.
   Juga dimatikan dan boleh dipadam: `trig_01Kr3GdPKbgZ7F1fvBCMQBmU`, `trig_01VmQhmem7EM86R6ASU5NU4D` (Papertrade Shariah 8 Okt),
   `trig_01Jok7ECiP6Nc8cgaZj45b6j`, `trig_01SuWSAzrrpsLCm5CUNKkCBq` (Harian v2 12 Okt), `trig_019eLSreMxzMXRhvE4gcigJm`,
   `trig_01YRNZtvNq6hqNwS3covz7Yy` (Harian v2 Project 2), pengawas `trig_018eaPB3VHoodMscT1s8BiLs`,
   `trig_01AJf4h6GffXNmHXmQsVzzGF`, `trig_018zyZSoegh4fQWpWGv3wS9m`.
5. **Kelulusan peralihan**: tugasan sekali `trig_01MUQxMSZmi3HroCCApwit2b` (26 Okt 2026 01:00 UTC) akan bertanya terus
   (AskUserQuestion; tenggat 11:00 UTC, sebelum imbas Claude 11:47 UTC).
6. **Kelulusan cadangan** `standard/tugasan_v3.md` §12 dan jadual ini (merge cawangan pratonton; arahan §5).
7. **Sejarah git** masih menyimpan nama penuh pemilik dan `NOTA_SERAHAN_BacktestShariah2.pdf` (repo awam). Membuangnya
   memerlukan penulisan semula sejarah + force push oleh pemilik (memecahkan klon/cawangan lain); keputusan pemilik.
