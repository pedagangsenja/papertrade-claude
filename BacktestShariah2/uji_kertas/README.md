# uji_kertas/

| Fail | Status | Penulis | Pembaca |
|---|---|---|---|
| `log.csv` | **ARKIB (beku)** sejak 7 Okt 2026 — jangan kemas kini, jangan padam | log uji kertas asal Project "Backtest Shariah" (62 baris; masuk 1 dan 6 Okt 2026; harga hingga tutup 7 Okt) | `standard/dashboard_kemaskini.py --papertrade` (alat lama; dokumen `_papertrade.json`); `00_NOTA_SERAHAN.md` |
| `jejak_M166.csv` | AKTIF hingga 15 Jan 2027 | `WFO/kaedah_baru/jejak_M166.py` (rutin imbas 7:47 langkah 4b; selepas peralihan `harian.yml`, mod rasmi) | analisis M166 (`WFO/kaedah_baru/README.md`) |

- `log.csv` dibekukan kerana uji kertas digantikan oleh Papertrade C (`papertrade/claude*.csv`, sejak 13 Okt 2026) dan Lejar
  Penuh (`lejar/`, sejak 16 Okt 2026). Lajur `tutup_6okt`/`tutup_7okt`, `untung_pct` dan `status` ("terbuka" bagi 36 baris)
  ialah keadaan pada 7 Okt 2026, BUKAN keadaan semasa; jangan guna untuk prestasi. Halaman dashboard
  (`standard/dashboard_v2.html`) tidak melanggan dokumen db yang dibina daripadanya (disemak 25 Okt 2026, baca sahaja).
- `jejak_M166.csv`: jejak kertas M166 V1 sahaja (rekod, tiada belian, tiada kesan pada senarai beli/watchlist; permintaan
  pengguna 17 Okt 2026). Jangan ubah secara manual.
