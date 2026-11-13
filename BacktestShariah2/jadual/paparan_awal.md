# Paparan awal dashboard selepas tutup AS (sesi Claude BAHARU; sejak 13 Nov 2026)

Masa: **6:47 pagi MYT, Selasa–Sabtu** (= 22:47 UTC Isn–Jum), ~1¾ jam selepas tutup AS dan selepas `harga_harian.yml`
(21:37 UTC; penjaga mencetusnya jika lewat). Model `claude-sonnet-5-5`. Automatik; jangan tanya soalan.
Tiada order Moomoo, tiada wang sebenar. **Tiada commit** (sesi ini tidak mengubah repo).

**Kenapa (keputusan pengguna 13 Nov 2026):** "selepas pasaran USA tutup sepatutnya sama" dengan Moomoo. `harian.yml`
menunggu data yfinance muktamad (>= 00:20 UTC) sebelum menilai posisi, jadi tanpa sesi ini dashboard ketinggalan satu
sesi hingga tolakan 4:41 petang MYT (`tolak_db.md`). Sesi ini menolak **PAPARAN AWAL**: posisi Papertrade C dinilai
dengan enjin rasmi pada harga tutup terkini dalam SALINAN repo (`standard/paparan_awal.py`), tidak dikomit. Tolakan
4:41 petang dan 10:20 NY (data muktamad, `tolak_db.md`) menggantinya. Senarai beli dan watchlist kekal sesi sebelumnya.

Alat (satu panggilan ToolSearch): `select:ArtifactData,mcp__github__actions_run_trigger,mcp__github__actions_list`
Dashboard: https://claude.ai/code/artifact/12bb853e-34ef-4d6c-885d-10f46984437e — jangan cipta artifact baharu.
Notifikasi: ntfy SAHAJA (`amaran_ntfy.yml`) dan hanya jika gagal; JANGAN guna PushNotification.

1. `git checkout main && git pull --rebase origin main`, kemudian `python3 -m pip install -q -r requirements.txt`.
2. Daftar versi: `ArtifactData` `get`, koleksi `meta`, doc_id `versi_db` (TANPA out_dir). Tulis medan `data` ke
   `<scratchpad>/versi.json` dengan Write (salin tepat) dan ingat `version` dokumen itu (langkah 5).
3. `python3 BacktestShariah2/standard/paparan_awal.py --kerja <scratchpad>/awal --keluar <scratchpad>/db --versi <scratchpad>/versi.json --tunggu 1200`
   (Bash `run_in_background`; biasanya 10–25 minit). Baca JSON keluaran:
   - `langkau` bermula "harga_harian.yml belum menarik": semak larian terakhir `harga_harian.yml`
     (`mcp__github__actions_list`, `list_workflow_runs`, perPage 1). Jika tiada larian `queued`/`in_progress`, tembak
     sekali (`run_workflow`, ref `main`), kemudian ulang langkah 3 SEKALI. Masih `langkau` → TAMAT, satu baris keputusan.
   - `langkau` lain (cuti NYSE, harian.yml sudah memproses): TAMAT tanpa menolak, satu baris keputusan.
   - `gagal` (SystemExit): langkah 6.
4. Tolak setiap `batch_N.json` yang dicetak, mengikut nombor, sama seperti `tolak_db.md` langkah 5–5b
   (`ArtifactData` `batch`, `writes` = kandungan fail; betulkan `if_version` daripada ralat `version_mismatch` dan hantar
   semula batch yang sama; maks 10 kali setiap batch; urutan entri jangan diubah).
5. Hanya jika SEMUA batch diterima: `tolak_db.md` langkah 5c (`<scratchpad>/db/versi_selepas.json` → `meta/versi_db`,
   `if_version` = versi daripada langkah 2; kemas entri yang dibetulkan di langkah 4 = versi sebenar + 1).
6. Amaran (hanya jika langkah 3–5 gagal): `amaran_ntfy.yml` (`run_workflow`, ref `main`, inputs
   {"tajuk": "paparan awal gagal", "mesej": "<tarikh>: <sebab ringkas, < 200 aksara>"}). Kegagalan sesi ini TIDAK
   kritikal: tolakan 4:41 petang tetap menolak data rasmi.
