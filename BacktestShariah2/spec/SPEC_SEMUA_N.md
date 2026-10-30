# SPEC SEMUA N — kombinasi daripada pakar, forum dan platform sosial

**Dijana oleh `BacktestShariah2/standard/registry_n.py`. Jangan sunting fail ini secara manual** — sunting senarai dalam skrip itu, kemudian jalankan semula.

## Mengapa dua keluarga

`Mxx` = kaedah lengkap daripada pedagang bernama, sudah dikodkan dalam `BacktestShariah2/kod/kaedah/`. Spec: `SPEC_SEMUA_KAEDAH.md`.

`Nxx` = **kombinasi indikator** yang dikumpul daripada sumber awam (TradingView, babypips, MQL5, LuxAlgo, StockSharp, Fmz, Stockezee, Tradezella, Quantified Strategies, YouTube, X/Twitter, blog pedagang, buku). Didaftar DAHULU, diuji KEMUDIAN. Pendaftaran dahulu ialah disiplin pradaftar yang sama seperti REVERSE: senarai penuh dikomit sebelum keputusan dilihat, supaya bilangan ujian diketahui dan FDR boleh dikira.

**Dapatan carian web yang penting:** peraturan pedagang **TIDAK diseragamkan**. Setiap sumber memberi versi berbeza bagi setup yang sama (ambang gap 3%-5%, pengganda volum 1.5x-2x, ADX 20-25, henti bawah rendah undur lawan bawah EMA). Jadi setiap baris di bawah ialah **satu versi tertentu daripada satu sumber tertentu**, bukan "peraturan rasmi" setup itu.

## Status

- `DIUJI` — sudah ada hasil terukur; nota memberi angkanya dan fail laporan.
- `SEDIA` — semua indikator yang diperlukan sudah dikira oleh kod repo (`REVERSE/teras/ind.py` atau `REVERSE/step15_setup.py` / `step17_kombinasi.py`); boleh diuji tanpa kod indikator baharu.
- `PERLU:<x>` — perlu indikator baharu `<x>` dahulu.

Masuk: 72 (11 DIUJI, 52 SEDIA, 9 PERLU). Keluar: 25 (7 DIUJI, 15 SEDIA, 3 PERLU).

Indikator baharu yang diperlukan: `darvas`, `donchian10`, `donchian50`, `htf`, `ma5`, `supertrend3`, `tinggi_swing`, `vwap20`, `vwap_ankor`.

## Peraturan masuk

### MA

**N01 MA10 silang MA20 + volum** — `ma10 silang naik ma20 DAN vol_n50 >= 1.2` · permintaan pengguna (pengguna) · DIUJI · lift +0.123 latih / +0.392 tahan; TERBAIK daripada 40 (KOMBINASI.md)

**N02 MA20 silang MA50** — `ma20 silang naik ma50` · klasik (umum) · DIUJI · lift negatif pada kedua-dua tingkap

**N03 MA20 silang MA200** — `ma20 silang naik ma200` · skrip MA+ATR (TradingView) · DIUJI · lift -0.342 latih / +0.209 tahan — tidak konsisten

**N04 EMA20>EMA50 + RSI 50-70** — `ema20 > ema50 DAN 50 <= rsi14 <= 70` · skrip awam (TradingView) · DIUJI · lift negatif

**N05 tutup>EMA20>SMA100 + volum** — `tutup > ema20 DAN ema20 > sma100 DAN vol_n50 >= 1.2` · pedagang forum (babypips) · DIUJI · lift negatif

**N06 Golden cross MA50/MA200** — `ma50 silang naik ma200` · klasik (umum) · SEDIA · hari_gc sudah ada

**N07 Tiga MA tersusun** — `hari pertama ma10 > ma20 > ma50` · triple-MA klasik (umum) · SEDIA

**N08 tutup>EMA20 tidak terlalu jauh** — `tutup > ema20 DAN (tutup - ema20) <= 1.5 x atr14` · pedagang forum (babypips) · SEDIA · sumber menegaskan LANGKAU jika terlalu jauh dari EMA20

**N09 Undur EMA10 + penapis EMA50** — `tutup > ema10 DAN tutup[-1] < ema10[-1] DAN tutup > ema50` · skrip 10ema (TradingView) · SEDIA

### RSI

**N10 RSI14 silang SMA14(RSI)** — `rsi14 silang naik SMA14(rsi14)` · skrip sumber terbuka (TradingView) · DIUJI · lift +0.016 / +0.006 — hampir sifar

**N11 RSI 40-50 + tutup>MA50** — `40 <= rsi14 <= 50 DAN tutup > ma50` · pedagang forum (forum) · DIUJI · lift negatif

**N12 RSI 40-60 + EMA20 + MA50 naik** — `tutup > ema20 DAN cerun_ma50 > 0 DAN 40 <= rsi14 <= 60` · konsensus blog (blog) · DIUJI · lift negatif

**N13 RSI<=30 + EMA + MACD + volum** — `ema20 > ema50 DAN rsi14 <= 30 DAN macd > 0 DAN vol_n50 >= 1.5` · skrip awam (TradingView) · DIUJI · lift negatif

**N14 Connors RSI2<5 + SMA200** — `rsi2 < 5 DAN tutup > ma200` · Connors (varian 200-hari) (buku/blog) · PERLU:ma5 · keluar asal: tutup > SMA5 ATAU tutup < SMA200

**N15 Connors RSI2<10 + SMA200** — `rsi2 < 10 DAN tutup > ma200` · EA MQL5 (MQL5) · SEDIA · keluar asal rsi2 > 65

**N16 RSI2<10 tanpa penapis** — `rsi2 < 10` · Quantified Strategies (YouTube/Substack) · SEDIA · keluar asal rsi2 > 60; pegang 1-10 hari

**N17 RSI14 silang naik 30** — `rsi14 silang naik 30` · klasik terlebih jual (umum) · SEDIA

**N18 RSI 30-50 pullback** — `30 <= rsi14 <= 50 DAN tutup > ma200` · Quantified Strategies (YouTube/Substack) · SEDIA · sumber lapor CAGR 5.3%, 196 dagangan, menang 81% pada S&P 500

### BB

**N19 Bawah jalur BB + RSI<30** — `bb_pctb < 0 DAN rsi14 < 30` · LuxAlgo (LuxAlgo) · SEDIA · keluar asal rsi14 > 70

**N20 Kembali masuk jalur + RSI silang 30** — `bb_pctb[-1] < 0 DAN bb_pctb > 0 DAN rsi14 silang naik 30` · therighttrader (blog) · SEDIA · henti pada ekstrem luar; keluar jalur tengah

**N21 BB + RSI 40/60** — `bb_pctb < 20 DAN rsi14 > 40` · Fmz (Fmz) · SEDIA · sasaran untung 2% tetap

**N22 BB pecah atas + RSI** — `bb_pctb > 100 DAN rsi14 > 50` · StockSharp (StockSharp) · SEDIA · keluar jalur tengah

**N23 BB squeeze kemudian pecah** — `bb_squeeze[-1] DAN tutup > ema20` · klasik (umum) · SEDIA

### TREND

**N24 Supertrend(10,3) + ADX>20** — `supertrend > 0 DAN adx14 > 20` · therighttrader (blog) · SEDIA · sumber: ATR 10, pengganda 3, ADX Wilder 14, ambang 20

**N25 Supertrend + EMA + ADX>23** — `supertrend > 0 DAN tutup > ema20 DAN adx14 > 23` · skrip awam (TradingView) · SEDIA

**N26 Tiga Supertrend + EMA + ADX** — `ketiga supertrend > 0 DAN tutup > ema20 DAN adx14 > ambang` · LuxAlgo (LuxAlgo) · PERLU:supertrend3 · tiga pengganda ATR berbeza

**N27 Ichimoku atas awan** — `atas_awan DAN tenkan_atas` · klasik (umum) · SEDIA

**N28 ADX>25 + DI+ > DI-** — `adx14 > 25 DAN mdi < adx14` · Wilder (buku) · SEDIA · proksi DI daripada lajur sedia ada

**N29 PSAR naik + tutup>MA50** — `psar_arah > 0 DAN tutup > ma50` · klasik (umum) · SEDIA

### PECAH

**N30 Turtle sistem 1** — `donchian20 pecah` · Dennis/Eckhardt (buku) · PERLU:donchian10 · henti 2xATR20; keluar Donchian10 bertentangan

**N31 Turtle sistem 2** — `donchian55 pecah` · Dennis/Eckhardt (buku) · SEDIA

**N32 Donchian50 (Darvas ringkas)** — `donchian50 pecah` · EA Darvas (MQL5) · PERLU:donchian50

**N33 Donchian20 + penapis MA200** — `donchian20 pecah DAN j_ma200 > 0` · skrip awam (TradingView) · SEDIA · henti pada jalur bertentangan

**N34 Darvas Box** — `pecah atas kotak Darvas` · Darvas (buku) · PERLU:darvas · tiada peraturan berangka standard; henti bawah kotak

**N35 Pecah 52 minggu tinggi** — `breakout_52w` · klasik (umum) · SEDIA

**N36 Pocket pivot** — `pocket_pivot` · Morales/Kacher (buku) · SEDIA · juga M35 dalam keluarga Mxx

**N37 Gap and go** — `gap_and_go` · klasik intraday (umum) · SEDIA

**N38 VCP pecah** — `vcp` · Minervini (buku) · SEDIA · juga M06

**N39 NR7 kemudian pecah** — `nr7[-1] DAN donchian20` · Crabel (buku) · SEDIA

### VOLUM

**N40 OBV tinggi baharu + MA50** — `obv_tinggi_baru DAN tutup > ma50` · klasik (umum) · SEDIA

**N41 CMF20>0 + tutup>EMA20** — `cmf20 > 0 DAN tutup > ema20` · Chaikin (buku) · SEDIA

**N42 Lonjakan volum 2x** — `vol_n50 >= 2.0 DAN tutup > tutup[-1]` · umum (umum) · SEDIA

### UNDUR

**N43 Undur EMA8 + penapis MA50** — `tutup[-1] < ema9[-1] DAN tutup > ema9 DAN tutup > ma50` · Morpheus Trading (Deel) (blog) · SEDIA · sumber guna EMA8; repo ada ema9 — proksi terdekat

**N44 Undur EMA21 + EMA21>MA50** — `tutup > ema21 DAN tutup[-1] < ema21[-1] DAN ema21 > ma50` · panduan 8/21 EMA (blog) · SEDIA · sumber: 21 EMA atas 50 EMA dan harga atas kedua-duanya

**N45 Undur EMA21 cerun positif** — `tutup > ema21 DAN cerun_ema21 > 0 DAN julat10 < julat20` · panduan 8/21 EMA (blog) · SEDIA · sumber syarat "EMA 45 darjah" — proksi cerun; elak EMA rata

**N46 Pecah tinggi bar penolakan** — `rendah[-1] <= ema21[-1] DAN tutup > tinggi[-1]` · journalplus/kotakneo (blog) · SEDIA · sumber TEGAS: masuk pada pecah tinggi lilin penolakan, BUKAN pada undur itu sendiri

### KETAT

**N47 NR7 + EMA9>EMA21** — `nr7 DAN ema9 > ema21 DAN tutup > ema21` · Stockezee (screener) · SEDIA · sumber asal 10EMA>20EMA pasaran India; ema9/ema21 proksi

**N48 Inside day pecah** — `inside_day[-1] DAN tutup > tinggi[-1]` · Crabel (buku) · SEDIA · order henti atas tinggi inside day — tidak meramal arah

**N49 NR7 + inside day serentak** — `nr7 DAN inside_day` · Crabel (buku) · SEDIA · Crabel: gabungan dua ini paling mampat

**N50 Mampat + pecah volum 1.5x** — `julat10 < 0.5 x julat20 DAN vol_n50 >= 1.5 DAN tutup > tinggi[-1]` · Stockezee (screener) · SEDIA · sumber tolak pecah bervolum lemah (< 1.5x) dan langkau 5 hari sebelum earnings

**N51 BB squeeze + Supertrend** — `bb_squeeze DAN supertrend > 0` · Squeeze Momentum (LazyBear) (YouTube) · SEDIA

**N52 Squeeze lepas + atas MA200** — `bb_squeeze[-1] DAN bb_lebar > bb_lebar[-1] DAN j_ma200 > 0` · Squeeze + EMA200 (YouTube) · SEDIA · video guna EMA200 sebagai penapis trend

### ADX

**N53 Supertrend + ADX>25** — `supertrend > 0 DAN adx14 > 25` · StockSharp (StockSharp) · SEDIA · keluar asal: supertrend berbalik (dipakai sebagai henti ekor)

**N54 Supertrend + RSI>50** — `supertrend > 0 DAN rsi14 > 50` · skrip posisional (TradingView) · SEDIA · ADX pilihan dalam sumber

**N55 BB + RSI + ADX>20** — `bb_pctb < 20 DAN rsi14 > 40 DAN adx14 > 20` · "Super Swing Strategy" (TradingView) · SEDIA

**N56 RSI>50 + ADX>20** — `rsi14 > 50 DAN adx14 > 20` · MTF RSI-ADX-ATR (TradingView) · SEDIA · henti ATR dalam sumber

**N57 ADX bangkit daripada <20** — `adx14 > 20 DAN adx14[-1] <= 20 DAN tutup > ma50` · Wilder (buku) · SEDIA

**N58 DI+ silang DI- + ADX>20** — `pdi silang naik mdi DAN adx14 > 20` · Wilder (buku) · SEDIA

### VWAP

**N59 tutup>VWAP + ADX>25** — `tutup > vwap20 DAN adx14 > 25` · StockSharp (StockSharp) · PERLU:vwap20 · sumber lapor ~157%/tahun tetapi pada KRIPTO, bukan saham; keluar bila adx14 < 20

**N60 VWAP + ADX + nisbah volum** — `tutup > vwap20 DAN adx14 > 20 DAN vol_n50 >= 1.5` · SwingTrade ADX v6 (TradingView) · PERLU:vwap20

**N61 VWAP berankor** — `tutup > vwap_ankor sejak pecah terakhir` · pedagang X (X/Twitter) · PERLU:vwap_ankor · tiada definisi standard bagi titik ankor

### POLA

**N62 Flat base pecah** — `julat20 <= 0.08 x tutup DAN tutup > tinggi20[-1]` · Tradezella/O’Neil (blog) · SEDIA · sumber: MA mengetat dan julat harian mengecil

**N63 High tight flag** — `gap >= 3% DAN vol_n50 >= 2.0 pada hari gap DAN sisi 3-8 hari DAN tutup > tinggi bendera` · skrip gaya Minervini (TradingView) · PERLU:htf

**N64 Episodic pivot** — `gap_and_go DAN vol_n50 >= 2.0` · Qullamaggie/Tradezella (blog/YouTube) · SEDIA · sumber tawar "high-volume close" sebagai masuk kedua

**N65 Gap 4% + volum + hampir 52w** — `gap_and_go DAN vol_n50 >= 1.5 DAN j_52w_tinggi >= -0.05` · pemeriksa pramasa (blog) · SEDIA · sumber: gap 4%, volum pramasa > 100k, pemangkin dalam 24 jam

**N66 52w tinggi + pengesahan 1%** — `tutup > 1.01 x tinggi_52w[-1]` · panduan amaran pecah (blog) · SEDIA · sumber: cetus 1-2% ATAS paras untuk tapis pecah palsu; elak saham tipis

**N67 Hammer di MA50** — `hammer DAN rendah <= ma50 DAN tutup > ma50` · klasik lilin (umum) · SEDIA

**N68 Bullish engulfing + EMA21** — `bullish_engulfing DAN tutup > ema21` · klasik lilin (umum) · SEDIA

### KEKUATAN

**N69 RS kuintil 5 + sektor atas MA50** — `rs_spy_6b dalam kuintil teratas DAN sektor_atas_ma50` · O’Neil/Minervini (buku) · SEDIA · dua daripada tiga tiang yang DITINGGALKAN daripada grid 672 setup

**N70 Garis RS tinggi baharu** — `garis_rs_tinggi` · Minervini (buku) · SEDIA

**N71 RS + pecah + rejim SPY** — `rs_spy_6b kuintil teratas DAN sektor_atas_ma50 DAN donchian20 DAN spy > ma50 DAN spy > ma200` · pakej Sistem A (buku) · DIUJI · Sistem A penuh: CAGR -1.03%, MDD -40.65%, sebaran benih 4.01 (SISTEM.md)

**N72 Momentum Clenow 90 hari** — `skor = (exp(cerun regresi log 90 hari x 252) - 1) x R^2; ambil 20 teratas, imbang bulanan` · Clenow (buku) · DIUJI · Sistem B: CAGR +6.38%, MDD -11.59%, sebaran benih 0.00; pendedahan hanya 35.4%

## Peraturan keluar

Keluar diuji **bersilang** dengan masuk, kerana `KOMBINASI.md` menunjukkan keluar mengubah tanda jangkaan: asas tanpa sasaran +2.595% lawan sasaran 1xATR **-0.281%** pada tingkap tahan yang sama. Lift mesti dikira lawan asas **keluar yang sama**.

**X01** — `henti 1.5 x ATR14, sasaran 1 x ATR14` · pedagang forum (babypips) · DIUJI · asas tahan -0.281% — MENUKAR ASAS JADI NEGATIF; kadar menang 61.1%

**X02** — `henti 2 x ATR14, sasaran 4 x ATR14` · pelbagai (umum) · DIUJI · asas tahan +0.953%

**X03** — `henti 2 x ATR14, pegang 63 sesi` · asas kajian (repo) · DIUJI · asas tahan +2.595% — TERBAIK; kadar menang 30.2%

**X04** — `ekori 2 x ATR14` · pelbagai (umum) · DIUJI · asas tahan +1.156%

**X05** — `keluar pada jalur tengah BB(20)` · therighttrader/StockSharp (blog) · SEDIA

**X06** — `keluar bila tutup < SMA5` · Connors (buku) · PERLU:ma5

**X07** — `keluar bila rsi2 > 60` · Quantified Strategies (YouTube/Substack) · SEDIA

**X08** — `keluar bila rsi2 > 80` · Connors (buku) · SEDIA · sumber lapor CAGR 9% pada SPY 1993+, melabur hanya ~28% masa

**X09** — `keluar bila rsi2 > 65` · EA MQL5 (MQL5) · SEDIA

**X10** — `sasaran untung 2% tetap` · Fmz (Fmz) · SEDIA

**X11** — `keluar Donchian10 bertentangan` · Turtle (buku) · PERLU:donchian10

**X12** — `henti pada ekstrem luar jalur BB` · therighttrader (blog) · SEDIA

**X13** — `keluar bila rsi14 > 70` · LuxAlgo (LuxAlgo) · SEDIA

**X14** — `keluar bila rsi14 silang naik 50` · skrip awam (TradingView) · SEDIA

**X15** — `ekori Chandelier 4 x ATR14` · lorong 2 repo (repo) · SEDIA · sudah dipakai Papertrade C

**X16** — `keluar bila supertrend berbalik (henti ekor)` · StockSharp (StockSharp) · SEDIA

**X17** — `keluar bila adx14 < 20` · StockSharp VWAP+ADX (StockSharp) · SEDIA

**X18** — `keluar Donchian20 bertentangan` · Turtle sistem 2 (buku) · SEDIA

**X19** — `ekori EMA21 (jual bila tutup < ema21)` · panduan 8/21 EMA (blog) · SEDIA

**X20** — `separa 1/3 pada 2R, ekori baki dengan EMA20` · panduan 8/21 EMA (blog) · SEDIA · sumber: ambil separa pada 2R atau tinggi swing terdahulu

**X21** — `jual 1/3 pada +10% atau hari-5, ekori MA20` · Minervini/Qullamaggie (buku) · DIUJI · komponen Sistem A (SISTEM.md)

**X22** — `henti keras -8% daripada harga masuk` · O’Neil (buku) · DIUJI · komponen Sistem A

**X23** — `keluar bila jatuh keluar 20 teratas pangkat momentum; imbang bulanan` · Clenow (buku) · DIUJI · komponen Sistem B; sebaran benih 0.00

**X24** — `keluar pada tinggi swing terdahulu` · umum (blog) · PERLU:tinggi_swing

**X25** — `henti 1% bawah EMA21 atau bawah rendah undur, mana lebih ketat` · panduan 8/21 EMA (blog) · SEDIA

## Cara menguji

1. Pradaftar: tulis `REVERSE/SPEC_<nama>.md` dengan senarai id yang akan diuji, pecahan LATIH/TAHAN, dan jangkaan priori. Komit sebelum larian.
2. Kira lift lawan asas keluar yang sama (bukan jangkaan mutlak — kesilapan `SPEC_SETUP.md` §4).
3. Syarat lulus: lift positif pada KEDUA-DUA tingkap, BH-FDR q <= 0.05 merentas bilangan ujian yang dipradaftar, dan jangkaan selepas buang 5% teratas kekal positif.
4. Setakat ini hanya `N01` (MA10 silang MA20 + volum >= 1.2x) mencapai syarat 1 dan 2; tiada satu pun mencapai syarat 3.
