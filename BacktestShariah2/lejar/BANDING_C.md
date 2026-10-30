# Banding Papertrade C dengan Lejar Penuh (fasa 1)

Dijana oleh `standard/lejar.py banding`. Lejar bermula 2026-10-15; sesi terakhir 2026-10-29. Kunci: kaedah + saham + tarikh_isyarat. Beza dijangka: sumber harga (C: Moomoo; lejar: yfinance), had 10 sekaedah dan keutamaan 431 dalam C (lejar membeli semua isyarat).

- Posisi C (isyarat >= 2026-10-15): 6352; ada dalam lejar: 5689; tiada: 663 {'isyarat ada, belum diproses': 11, 'tiada isyarat dalam lejar': 15, 'isyarat ada, dipegang lejar': 637}
- Posisi lejar: 15134 (C hanya 6352; lejar 2.4×)
- Harga beli berbeza > 0.5%: 0 daripada 5689
- Status keluar sama: 5688 daripada 5689; berbeza: 1

## Status keluar berbeza

- M13 SBH 2026-10-15: C keluar 2026-10-19 / lejar keluar 2026-10-20 henti
