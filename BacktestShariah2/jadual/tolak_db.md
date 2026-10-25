# Tolak db dashboard (sesi Claude BAHARU setiap kali; aktif selepas peralihan, lihat `PERALIHAN.md`)

Reka semula 25 Okt 2026 (cadangan audit operasi; `jadual/CADANGAN_JADUAL.md`). Dahulu satu tolakan 10:20 NY: data sesi D sampai
~50 minit SELEPAS buka D+1 (panel Esok basi sepanjang pra-buka) dan hanya 4–7 minit selepas beli. Kini dua tolakan:

| Bahagian | Masa (tugasan berjadual) | Menunggu | Notifikasi |
|---|---|---|---|
| **A pasca-harian** | `CRON_TZ=Asia/Kuala_Lumpur 47 14 * * 2-6` = 14:47 MYT Sel–Sab = 06:47 UTC tetap (tidak terkesan DST) | `harian.yml` + `lejar.yml` + `analisis.yml` sudah memproses sesi dijangka; maks 60 minit | `notifikasi.py malam` (menggantikan `notifikasi_harian.md`) |
| **B pasca-beli** | `CRON_TZ=America/New_York 33 10 * * 1-5` = 10:33 NY Isn–Jum (ikut DST; 14:33 UTC EDT, 15:33 UTC EST) | `beli.yml` sudah merekod belian hari ini; maks 30 minit | `notifikasi.py beli` |

Sasaran: data sesi D dalam dashboard ~14:50–15:45 MYT D+1 (≥ 5.5 jam sebelum buka AS 21:30/22:30 MYT); posisi belian D dalam
dashboard ≤ 11:05 NY D. Jika jadual cadangan belum diluluskan, jadual lama kekal: satu tolakan `CRON_TZ=America/New_York 20 10 * * 1-6`
yang menjalankan A kemudian B dalam sesi sama (langkah 2 dengan `--untuk malam`, kemudian `--untuk beli`).

Model `claude-sonnet-5-5`. Automatik; jangan tanya soalan. Tiada order Moomoo, tiada wang sebenar. Semua pengiraan dibuat oleh
GitHub Actions; sesi ini hanya (1) memastikan Actions sudah berjalan dan (2) menolak fail yang sudah dijana ke db dashboard.
Jangan baca fail CSV besar dan jangan bina JSON dengan tangan; guna skrip. Kiraan dalam notifikasi disalin daripada skrip.

Alat (satu panggilan ToolSearch): `select:ArtifactData,PushNotification,mcp__github__actions_list,mcp__github__actions_run_trigger`
Dashboard: https://claude.ai/code/artifact/12bb853e-34ef-4d6c-885d-10f46984437e

1. `git pull --rebase origin main`.
2. Kesediaan: `python3 BacktestShariah2/standard/notifikasi.py sedia --untuk malam` (A) atau `--untuk beli` (B) → satu baris
   JSON (`jangka`, `siap`, `belum`, `tembak`); kod 0 = siap, 3 = belum.
   - B dengan `cuti: true` (pasaran AS tutup) → terus ke langkah 6 (tiada tolakan).
   - Belum siap: bagi setiap workflow dalam `tembak`, semak larian terakhir (`mcp__github__actions_list`, method
     `list_workflow_runs`, owner `pedagangsenja`, repo `papertrade-claude`, resource_id nama workflow, perPage 1). Jika tiada
     larian `queued`/`in_progress`, tembak SEKALI (`mcp__github__actions_run_trigger`, method `run_workflow`, workflow_id nama
     workflow, ref `main`). (`analisis.yml` dicetus sendiri selepas `lejar.yml`; ia hanya dalam `tembak` jika Lejar sudah siap.)
   - Tunggu tanpa `sleep` latar depan: Bash `run_in_background` (timeout 3600000 bagi A, 1800000 bagi B) dengan
     `until python3 BacktestShariah2/standard/notifikasi.py sedia --untuk <malam|beli> >/dev/null; do sleep 300; git pull -q --rebase origin main; done`,
     kemudian tunggu notifikasi selesai. Tamat masa → teruskan dengan data sedia ada; catat `separa: <belum>` dalam `--tambah`.
3. Versi dokumen db: `ArtifactData` `list` bagi koleksi `papertrade` (query.limit 100; ulang dengan next_cursor),
   `prestasi`, `harian`, `sektor`, `analisis` dan `posisi`, dengan `out_dir` <scratchpad>/lama (kandungan tidak perlu dibaca).
   Tulis `<scratchpad>/versi.json` = {"papertrade/claude": versi, …} untuk SEMUA dokumen yang disenaraikan.
4. `python3 BacktestShariah2/standard/jana_db.py --keluar <scratchpad>/db --versi <scratchpad>/versi.json`
   (pecah_claude/bahagi_db sudah dijalankan oleh Actions; dokumen ≥ had 262,144 bait dilangkau dan dicatat dalam `ralat`).
4a. Kira semula bebas: salin `BacktestShariah2/data/semakan/*.json` ke `<scratchpad>/semakan/`, jalankan
   `python3 BacktestShariah2/standard/kira_semula.py --db <scratchpad>/db --json <scratchpad>/semakan/kira_semula.json`
   (kod 1 = beza: teruskan, catat dalam notifikasi), kemudian
   `python3 BacktestShariah2/standard/jana_db.py --keluar <scratchpad>/db --semakan-sahaja --semakan-dir <scratchpad>/semakan`
   (batch merujuk file_path, jadi tolakan membawa `harian/status.semakan` baharu). Fail repo tidak diubah.
5. Bagi setiap fail `batch_N.json` yang dicetak: `ArtifactData` `batch`, `writes` = kandungan fail itu (setiap entri sudah
   ada `file_path` dan `if_version`). Ditolak kerana versi berubah → ulang langkah 3–5 sekali.
6. Notifikasi (langkah terakhir, juga jika gagal): senarai workflow gagal seperti `notifikasi_harian.md` langkah 2, kemudian
   A: `python3 BacktestShariah2/standard/notifikasi.py malam --amaran --db <scratchpad>/db --gagal "<…>" --tambah "db <ok|gagal: sebab><; separa: …><; tembak …>"`
   B: `python3 BacktestShariah2/standard/notifikasi.py beli --amaran --db <scratchpad>/db --gagal "<…>" --tambah "…"`
   → `PushNotification`, status "proactive", mesej = baris itu TEPAT. "Kalau tak beli, cakap tak beli" (skrip menulisnya).
   `--amaran` menambah "AMARAN: …" bagi SST > 8 hari, EDGAR tidak aktif/lewat, kalendar earnings lewat dan dokumen db ≥ 80% had.
Tiada commit diperlukan (sesi ini tidak mengubah fail repo).
