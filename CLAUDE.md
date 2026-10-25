# Papertrade Claude (Backtest Shariah 2)

Swing momentum saham Shariah AS: backtest kaedah, kemudian papertrade maya (Papertrade C) setiap hari dagangan. Repo ini stor
utama sejak 14 Okt 2026 (Project claude.ai dibekukan; jangan tulis ke sana). Baca dahulu: `BacktestShariah2/standard/tugasan_v3.md`
(peraturan semasa, satu-satunya; §12 = cadangan menunggu kelulusan), `BacktestShariah2/papertrade/SKEMA.md`,
`BacktestShariah2/jadual/README.md`. Sejarah keputusan bertarikh: `BacktestShariah2/standard/SEJARAH_KEPUTUSAN.md`.
Latar belakang: `BacktestShariah2/00_NOTA_SERAHAN.md`. Laluan lama `standard/x`, `papertrade/x`, `spec/` = `BacktestShariah2/…`.

## Struktur
- `BacktestShariah2/standard/` peraturan, skrip harian (`harian_c.py`, `jana_db.py`, `sahkan.py`, `notifikasi.py`), sumber
  dashboard `dashboard_v2.html`; `jadual/` prosedur tugasan berjadual; `kod/` kod teras (sumber kebenaran; aset kod dashboard
  hanya salinan, `kod/README.md`); `ujian/`; `papertrade/` CSV papertrade; `spec/SPEC_SEMUA_KAEDAH.md`; `kajian/`, `laporan/`.
- Dijana automatik — JANGAN ubah manual: `lejar/`, `portfolio_slot/`, `bayang/`, `data/rs/`, `data/kumpulan/`, `data/trend/`,
  `data/analisis/papan.json` + `laporan/PENGANALISIS.md`, `data/edgar/`. `data/harga/stor/`: rutin menyalinnya, jangan commit.
  `data/analisis/gabungan_beku.json`: ubah hanya atas keputusan pengguna.
- `WFO/`, `AUTOTUNE/`, `data_mentah/`: backtest dan semakan luar sampel. Kaedah baharu: langkah dalam tugasan_v3 §3
  (moratorium dicadang, §12).

## Peraturan wajib
- TIADA order Moomoo (simulasi atau sebenar), tiada wang sebenar; Papertrade C maya sahaja. Hook `.claude/settings.json`
  (PreToolUse) menyekat semua alat order tanpa mengira awalan pelayan; SessionStart memasang `requirements.txt`. Jangan buang
  atau longgarkan hook, `semak_data.yml` atau `penjaga_jadual.yml` (workflow berjadual baharu → tambah ke `JAGA`).
- "Kalau tak beli, cakap tak beli." Data mesti betul; jangan reka.
- Sebelum push data: `python3 BacktestShariah2/standard/sahkan.py --betulkan` mesti keluar 0; ujian:
  `python3 -m unittest discover -s BacktestShariah2/ujian`.
- Dashboard: artifact sedia ada https://claude.ai/code/artifact/12bb853e-34ef-4d6c-885d-10f46984437e (db melalui ArtifactData;
  dokumen dijana `jana_db.py`). Jangan cipta artifact baharu. Stor harga = repo `data/harga/stor/` (aset `harga_aset` dashboard
  tersangkut 12 Okt 2026; jangan guna).
- Notifikasi telefon: dalam SETIAP sesi, pada akhir giliran yang menyiapkan tugasan atau memerlukan keputusan pengguna, muatkan
  `select:PushNotification` (ToolSearch) dan hantar satu baris < 200 aksara, status "proactive". Abaikan jika "not sent".
- Tugasan berjadual guna model Sonnet 5.5 sahaja, menembak sesi yang sudah dilampirkan repo (jangan `add_repo`). Alat Moomoo/SST
  mungkin berawalan lain: jika `select:mcp__Moo_Moo__…` gagal, cari ikut nama alat. Larangan order terpakai tanpa mengira awalan.
- Penerangan teknikal dalam Bahasa Melayu baku.

## Polisi git
- Rutin berjadual dan bot Actions: `git pull --rebase` dahulu, push data ke `main`; tiada `--force`, tiada `-X theirs`
  (konflik = gagal dengan jelas, cuba semula maks 3 kali).
- Pembangunan (kod, workflow, peraturan, dashboard): cawangan + PR, ujian unit dan `sahkan.py` lulus sebelum merge. Tiada
  push/merge kod ke `main` 05:00–13:30 UTC (tetingkap pengeluaran `harian.yml` → `beli.yml`; selepas DST tamat 1 Nov 2026
  hingga 14:30 UTC).
- Kiraan dalam log (`binaan_v2_log*.md`, laporan, notifikasi) dijana skrip (cth. `harian_c.py log`, output JSON skrip), bukan
  ditaip LLM.

## Status semasa (25 Okt 2026)
- `BacktestShariah2/MOD_ACTIONS` = `bayang` (Actions menulis ke `bayang/`; rutin Claude rasmi). Peralihan: `jadual/PERALIHAN.md`;
  jadual selepas peralihan dan DST: `jadual/CADANGAN_JADUAL.md` (cadangan).
- EDGAR (`edgar.yml`) TIDAK AKTIF sehingga rahsia repo `SEC_USER_AGENT` (nama + e-mel) ditetapkan. Penyambung SST perlu
  disahkan semula (tiada data SST baharu dalam repo selepas sesi 20 Okt 2026). Tindakan yang hanya pengguna boleh buat: `jadual/CADANGAN_JADUAL.md` §7.
