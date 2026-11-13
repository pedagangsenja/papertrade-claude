# Paparan awal dashboard selepas tutup AS (sesi Claude BAHARU; sejak 13 Nov 2026)

Masa: **6:47 pagi MYT, Selasa–Sabtu** (= 22:47 UTC Isn–Jum; trig_014q7xdrErWubfa2ff43Ka66), ~1¾ jam selepas tutup AS dan selepas `harga_harian.yml`
(21:37 UTC; penjaga mencetusnya jika lewat). Model `claude-sonnet-5-5`. Automatik; jangan tanya soalan.
Tiada order Moomoo, tiada wang sebenar. **Tiada commit** (sesi ini tidak mengubah repo).

**Kenapa (keputusan pengguna 13 Nov 2026):** "selepas pasaran USA tutup sepatutnya sama" dengan Moomoo. `harian.yml`
menunggu data yfinance muktamad (>= 00:20 UTC) sebelum menilai posisi, jadi tanpa sesi ini dashboard ketinggalan satu
sesi hingga tolakan 4:41 petang MYT (`tolak_db.md`). Sesi ini menolak **PAPARAN AWAL**: posisi Papertrade C dinilai
dengan enjin rasmi pada harga tutup terkini dalam SALINAN repo (`standard/paparan_awal.py`), tidak dikomit. Tolakan
4:41 petang dan 10:20 NY (data muktamad, `tolak_db.md`) menggantinya. Senarai beli dan watchlist kekal sesi sebelumnya.

Alat (satu panggilan ToolSearch): `select:ArtifactData`. Sesi berjadual tiada alat GitHub (diukur 13 Nov 2026); repo
diklon dengan git jika tiada, dan amaran dihantar terus ke ntfy (`standard/amaran.py`).
Dashboard: https://claude.ai/code/artifact/12bb853e-34ef-4d6c-885d-10f46984437e — jangan cipta artifact baharu.
Notifikasi: ntfy SAHAJA (`standard/amaran.py`) dan hanya jika gagal; JANGAN guna PushNotification.

1. `git checkout main && git pull --rebase origin main`, kemudian `python3 -m pip install -q -r requirements.txt`.
2. Daftar versi: `ArtifactData` `get`, koleksi `meta`, doc_id `versi_db` (TANPA out_dir). Tulis medan `data` ke
   `<scratchpad>/versi.json` dengan Write (salin tepat) dan ingat `version` dokumen itu (langkah 5).
3. `python3 BacktestShariah2/standard/paparan_awal.py --kerja <scratchpad>/awal --keluar <scratchpad>/db --versi <scratchpad>/versi.json --tunggu 900`
   (Bash `run_in_background`; biasanya 10–25 minit). Saham tanpa bar sesi itu diisi daripada carta Yahoo; jika
   `harga_harian.yml` masih belum menarik sesi itu selepas 15 minit, SEMUA bar sesi dibina daripada carta Yahoo
   (langkah `isi_bar … (semua)`, ~5 minit lagi). Baca JSON keluaran:
   - `langkau` (cuti NYSE, atau harian.yml sudah memproses sesi itu): TAMAT tanpa menolak, satu baris keputusan.
   - `gagal` (SystemExit): langkah 6.
4. Tolak setiap `batch_N.json` yang dicetak, mengikut nombor, sama seperti `tolak_db.md` langkah 5–5b
   (`ArtifactData` `batch`, `writes` = kandungan fail; betulkan `if_version` daripada ralat `version_mismatch` dan hantar
   semula batch yang sama; maks 10 kali setiap batch; urutan entri jangan diubah).
5. Hanya jika SEMUA batch diterima: `tolak_db.md` langkah 5c (`<scratchpad>/db/versi_selepas.json` → `meta/versi_db`,
   `if_version` = versi daripada langkah 2; kemas entri yang dibetulkan di langkah 4 = versi sebenar + 1).
6. Amaran (hanya jika langkah 3–5 gagal): `python3 BacktestShariah2/standard/amaran.py --tajuk "paparan awal gagal" --mesej "<tarikh>: <sebab ringkas, < 200 aksara>"` (ntfy terus; sesi
   berjadual TIADA alat GitHub sejak 13 Nov 2026). Hanya jika ia keluar 1 DAN alat GitHub ada: `amaran_ntfy.yml`
   melalui `mcp__github__actions_run_trigger` (`run_workflow`, ref `main`, inputs {"tajuk", "mesej"}).
   Kegagalan sesi ini TIDAK kritikal: tolakan 4:41 petang tetap menolak data rasmi.
