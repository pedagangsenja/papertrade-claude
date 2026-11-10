# Data Moomoo/SST — MANUAL sebulan sekali (sejak 10 Nov 2026; asal tugasan berjadual mingguan 27 Okt 2026, `PERALIHAN.md`)

**Keputusan pengguna 10 Nov 2026:** tugasan berjadual Ahad (`trig_01CYKa7pZBDanjL4dUBLtrfY`) DIMATIKAN. Ia tiada connector
Moomoo/SST dan repo tidak dilampirkan, jadi larian 8 Nov gagal senyap (status SUCCEEDED, tiada commit, ntfy 403). Harga dan
dashboard tidak perlu Moomoo (yfinance = app Moomoo, 55/55 saham sepadan 10 Nov 2026). Hanya senarai Shariah (langkah 2)
tiada sumber percuma lain, jadi prosedur ini dijalankan MANUAL dalam sesi bersama pengguna apabila connector Moo_Moo
disambung, sekurang-kurangnya sebulan sekali. Tripwire: `koordinator.py --semak` (harian.yml) gagal → ntfy apabila
`data/harga/univ_status.json` > 35 hari. Pasaran AS sebaiknya tutup (data tutup sesi terakhir).
LARANGAN: tiada order (`trading_order_*`, `sim_trade_input/modify/cancel_order`); hook projek menyekatnya.
Keputusan pengguna 17 Okt 2026 (dipinda 10 Nov 2026): data yang hanya Moomoo/SST boleh beri dikumpul secara manual; selebihnya GitHub Actions.
Hasil alat besar disimpan ke fail oleh sistem — proses dengan Python; jangan salin data ke dalam jawapan.

Alat (ToolSearch; jika `select:mcp__Moo_Moo__…` gagal, cari ikut nama alat, cth. "quote_stock_screen"):
`select:mcp__Moo_Moo__quote_stock_screen,mcp__Moo_Moo__quote_plate_list,mcp__Moo_Moo__quote_plate_stock`,
`select:mcp__SST_Terminal__market_events,mcp__SST_Terminal__institutional_flow,mcp__SST_Terminal__unusual_volume`,
`select:mcp__Moo_Moo__quote_financials_statements,mcp__Moo_Moo__quote_financials_earnings_price_history,mcp__Moo_Moo__quote_market_snapshot,mcp__Moo_Moo__quote_corporate_actions_rehab`,

1. `git pull --rebase origin main`.
2. Universe Shariah (skrin Moomoo; screen_queries & retrieve_queries sama seperti `jadual/imbas_2002.md` langkah 2, limit 250,
   ulang next_key hingga has_more=false). `python3 BacktestShariah2/kod/parse_screen.py BacktestShariah2/data/harga/univ.csv <fail…>`,
   kemudian tulis semua ticker (tanpa `US.`) ke `BacktestShariah2/data/harga/univ.txt` (Actions mengimbas universe ini dan
   menarik harganya; `univ.csv` memberi nama syarikat). Kurang daripada 800 ticker → jangan tulis; catat ralat.
   Selepas menulis, kemas kini `BacktestShariah2/data/harga/univ_status.json`: `tarikh` = tarikh skrin (YYYY-MM-DD),
   `bilangan` = bilangan ticker (tripwire 35 hari membaca `tarikh`; jangan kemas kini jika skrin gagal).
3. Peta industri: jika `papertrade/peta_industri.csv` lebih 30 hari, bina semula seperti `jadual/kemas_kini_0602.md` 5(b).
4. Sektor seluruh pasaran AS: skrin semua saham AS ≥ USD5 (arahan dalam kepala `standard/sektor_pasaran.py`, ~21 halaman × 300),
   `python3 BacktestShariah2/standard/sektor_pasaran.py --skrin <fail…> --peta BacktestShariah2/papertrade/peta_industri.csv
   --tarikh <tutup Jumaat> --out BacktestShariah2/papertrade/sektor_pasaran.csv --json <scratchpad>/sektor_pasaran.json`.
5. SST: `institutional_flow` dan `unusual_volume` (market US) → simpan JSON di `BacktestShariah2/data/sst/`;
   `market_events` (market US, daysLookahead 40) → `BacktestShariah2/data/pemangkin/market_events.json` (gred QR; dipakai
   Actions sehingga 9 hari). Ralat SST → langkau dan catat.
6. **DILANGKAU sejak 6 Nov 2026 (dashboard v156):** tab Sektor diarkib dan halaman tidak lagi melanggan `sektor/snapshot`
   (audit v154 pepijat #3: `data/db/sektor_snapshot.json` tidak pernah sampai ke `main`, jadi tab itu beku). Langkah asal, untuk rujukan:
   Snapshot sektor dashboard: `ArtifactData get` `sektor/snapshot` dengan out_dir (fail lama), kemudian
   `python3 BacktestShariah2/standard/snapshot_sektor_db.py --pasaran <sektor_pasaran.json> --lama <fail lama>
   --peta BacktestShariah2/papertrade/peta_industri.csv --papertrade BacktestShariah2/papertrade --dibina "<YYYY-MM-DD HH:MM> MYT"
   --out BacktestShariah2/data/db/sektor_snapshot.json` (jana_db.py menolaknya bersama dokumen harian).
7. **DIBUANG 10 Nov 2026:** semak akaun simulasi Moomoo. Tiada order sejak 13 Okt 2026, kos/unit sepadan 100% (12 Okt) dan
   harga yfinance = app (55/55 saham, 10 Nov 2026), jadi semakan ini tidak menambah maklumat.
7b. Kewangan (gred kewangan v7; dahulu `jadual/imbas_2002.md` langkah 5c setiap malam): ikut 5c tepat (alat, 2 panggilan
   setiap mesej, berhenti pada had kadar, `tuai_kewangan.py` → `gred_kewangan.py simpan` → `gred_kewangan.py isi` →
   `pecah_claude.py --pecah`), dijalankan dari akar repo atas `papertrade/senarai_beli.csv` dan `watchlist.csv` semasa.
   Tiada baris `perlu` → langkau. Catat bilangan saham dan ticker dalam log.
7c. Peristiwa korporat besar (dahulu `jadual/kemas_kini_0602.md` langkah 2d setiap pagi): `python3 BacktestShariah2/kod/peristiwa.py calon`;
   bagi setiap calon semak `quote_corporate_actions_rehab` dan `tambah`/`tolak` seperti 2d (jangan reka faktor; alat tiada →
   biarkan calon dan catat). Posisi C dilaras oleh `harian_c.py malam` seterusnya (`tidak_layak.py posisi`), stor/Lejar oleh `lejar.py stor`.
8. `python3 BacktestShariah2/standard/sahkan.py` → mesti 0. Catatan dalam `standard/binaan_v2_log.md`
   (bilangan universe, sektor_pasaran, SST, kewangan, peristiwa). Commit `Data Moomoo/SST manual <tarikh>: <ringkas>` + push
   (sesi bersama pengguna: ke cawangan sesi, pengguna menggabung).
8b. **DIPINDAH 10 Nov 2026:** ringkasan mingguan 5 baris kini dijana oleh `analisis.yml` setiap Sabtu (UTC), dengan ntfy baris 1
   dan 5. Ia tidak perlu Moomoo.
9. Laporkan kepada pengguna dalam sesi (universe <n>, sektor <tarikh>, SST <ok/ralat>, kewangan <n>, peristiwa <n>).
