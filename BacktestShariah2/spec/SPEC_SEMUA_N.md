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

Masuk: 100 (11 DIUJI, 60 SEDIA, 29 PERLU). Keluar: 32 (7 DIUJI, 22 SEDIA, 3 PERLU). Cara: 8 (1 DIUJI, 6 SEDIA, 1 PERLU). Urutan: 8 (5 DIUJI, 1 SEDIA, 2 PERLU).

Indikator baharu yang diperlukan: `alligator`, `alphatrend`, `arxiv`, `atrts`, `chop`, `coppock`, `crsi`, `darvas`, `donchian10`, `donchian50`, `efi`, `eri`, `fisher`, `htf`, `huggingface`, `isi_tutup`, `kst`, `kvo`, `ma5`, `pgo`, `qqe`, `rwi`, `squeeze_ttm`, `stc`, `supertrend3`, `tinggi_swing`, `tmo`, `tsv`, `vhf`, `vortex`, `vwap20`, `vwap_ankor`.

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

**N76 Tutup > MA50 (penapis trend tunggal)** — `tutup > ma50` · QuantJourney O04 (quantjourney-bt) · SEDIA · berguna sebagai ASAS penapis tunggal untuk mengira lift

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

**N75 RSI14 < 40 tanpa penapis** — `rsi14 < 40` · QuantJourney O03 (quantjourney-bt) · SEDIA · sumber pasangkan dengan buy-limit 1.5% bawah tutup (C03)

**N82 Connors RSI penuh < 10** — `crsi = purata(RSI(3), RSI(2) atas panjang streak, pangkat peratus ROC(1) 100 hari) < 10` · Larry Connors (pandas_ta) · PERLU:crsi · TIGA komponen; N14-N16 hanya guna rsi2 = versi ringkas sahaja

### BB

**N19 Bawah jalur BB + RSI<30** — `bb_pctb < 0 DAN rsi14 < 30` · LuxAlgo (LuxAlgo) · SEDIA · keluar asal rsi14 > 70

**N20 Kembali masuk jalur + RSI silang 30** — `bb_pctb[-1] < 0 DAN bb_pctb > 0 DAN rsi14 silang naik 30` · therighttrader (blog) · SEDIA · henti pada ekstrem luar; keluar jalur tengah

**N21 BB + RSI 40/60** — `bb_pctb < 20 DAN rsi14 > 40` · Fmz (Fmz) · SEDIA · sasaran untung 2% tetap

**N22 BB pecah atas + RSI** — `bb_pctb > 100 DAN rsi14 > 50` · StockSharp (StockSharp) · SEDIA · keluar jalur tengah

**N23 BB squeeze kemudian pecah** — `bb_squeeze[-1] DAN tutup > ema20` · klasik (umum) · SEDIA

**N73 Tutup bawah jalur bawah BB(20,2)** — `tutup < SMA20 - 2 x SD20` · QuantJourney W21 (quantjourney-bt) · SEDIA · keluar asal: tutup > jalur tengah SMA20

### TREND

**N24 Supertrend(10,3) + ADX>20** — `supertrend > 0 DAN adx14 > 20` · therighttrader (blog) · SEDIA · sumber: ATR 10, pengganda 3, ADX Wilder 14, ambang 20

**N25 Supertrend + EMA + ADX>23** — `supertrend > 0 DAN tutup > ema20 DAN adx14 > 23` · skrip awam (TradingView) · SEDIA

**N26 Tiga Supertrend + EMA + ADX** — `ketiga supertrend > 0 DAN tutup > ema20 DAN adx14 > ambang` · LuxAlgo (LuxAlgo) · PERLU:supertrend3 · tiga pengganda ATR berbeza

**N27 Ichimoku atas awan** — `atas_awan DAN tenkan_atas` · klasik (umum) · SEDIA

**N28 ADX>25 + DI+ > DI-** — `adx14 > 25 DAN mdi < adx14` · Wilder (buku) · SEDIA · proksi DI daripada lajur sedia ada

**N29 PSAR naik + tutup>MA50** — `psar_arah > 0 DAN tutup > ma50` · klasik (umum) · SEDIA

**N74 MACD atas garis isyarat (keadaan, bukan silang)** — `macd > macd_sig` · QuantJourney W22 (quantjourney-bt) · SEDIA · BERBEZA daripada macd_cross: keadaan berterusan, bukan peristiwa silang

**N83 AlphaTrend menaik** — `alphatrend > alphatrend[-2]` · KivancOzbilgic (TradingView / pandas_ta) · PERLU:alphatrend · ATR + MFI (atau RSI) memilih jalur

**N86 Vortex VI+ silang naik VI-** — `vtxp silang naik vtxm` · Botes & Siepman (TASC Jan 2010) (pandas_ta) · PERLU:vortex

**N87 VHF > 0.35 + tutup > MA50** — `vhf(28) > 0.35 DAN tutup > ma50` · Adam White (pandas_ta) · PERLU:vhf · Vertical Horizontal Filter: tinggi = trend, rendah = sisi

**N92 Alligator mulut terbuka menaik** — `jaw(13) < teeth(8) DAN teeth(8) < lips(5) DAN tutup > lips` · Bill Williams (pandas_ta) · PERLU:alligator

**N95 Choppiness Index < 38.2 + tutup > MA50** — `chop(14) < 38.2 DAN tutup > ma50` · E.W. Dreiss (pandas_ta) · PERLU:chop · rendah = trend, tinggi = sisi; 38.2 ialah paras Fibonacci yang sumber guna

**N96 Random Walk Index tinggi > 1** — `rwi_tinggi > 1 DAN rwi_tinggi > rwi_rendah` · Michael Poulos (pandas_ta) · PERLU:rwi · > 1 bermakna gerakan melebihi apa yang jalan rawak boleh terangkan

**N99 ATR Trailing Stop naik dan tutup di atasnya** — `atrts > atrts[-1] DAN tutup > atrts` · pandas_ta (atrts) (pandas_ta) · PERLU:atrts · serupa lorong 2 Chandelier repo tetapi pengangkaan berbeza

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

**N80 Tinggi sepanjang masa** — `tutup >= tutup tertinggi sepanjang masa` · Wilcox & Crittenden (2005); Zarattini, Pagani & Wilcox (2025) (Quantpedia) · SEDIA · SAMA dengan K195 dalam katalog K; henti ekor asal 10 x ATR, pegangan purata ~305 hari (kedudukan, bukan swing)

### VOLUM

**N40 OBV tinggi baharu + MA50** — `obv_tinggi_baru DAN tutup > ma50` · klasik (umum) · SEDIA

**N41 CMF20>0 + tutup>EMA20** — `cmf20 > 0 DAN tutup > ema20` · Chaikin (buku) · SEDIA

**N42 Lonjakan volum 2x** — `vol_n50 >= 2.0 DAN tutup > tutup[-1]` · umum (umum) · SEDIA

**N88 Elder Force Index > 0 + tutup > EMA21** — `efi(13) > 0 DAN tutup > ema21` · Alexander Elder (pandas_ta) · PERLU:efi

**N89 Elder Ray: bull power > 0 dan bear power menaik** — `eri_bull > 0 DAN eri_bear > eri_bear[-1]` · Alexander Elder (pandas_ta) · PERLU:eri

**N90 Klinger Volume Oscillator silang naik 0** — `kvo silang naik 0` · Stephen Klinger (pandas_ta) · PERLU:kvo

**N91 Time Segmented Volume > 0 + tutup > MA50** — `tsv(18) > 0 DAN tutup > ma50` · Worden Brothers (pandas_ta) · PERLU:tsv

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

**N81 TTM Squeeze lepas + momentum naik** — `squeeze OFF pada bar ini DAN ON pada bar sebelum DAN momentum squeeze > 0` · John Carter (pandas_ta / Simpler Trading) · PERLU:squeeze_ttm · BERBEZA daripada bb_squeeze repo (lebar BB): TTM = BB(20,2) berada DALAM KC(20,1.5,ATR)

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

**N77 Pulangan 252 hari dalam 3 teratas alam** — `pangkat keratan rentas pulangan 252 hari, ambil 3 teratas, imbang bulanan` · QuantJourney W15 / Jegadeesh-Titman (quantjourney-bt) · SEDIA · momentum keratan rentas klasik; BERBEZA daripada N72 (Clenow guna regresi 90 hari x R^2)

**N78 Pulangan 21 hari dalam 3 terbawah alam (pembalikan)** — `pangkat keratan rentas pulangan 21 hari, ambil 3 TERBAWAH, imbang mingguan` · QuantJourney W16 (quantjourney-bt) · SEDIA · PEMBALIKAN - bertentangan momentum; didaftar untuk kelengkapan, bukan kerana dijangka lulus

**N79 Momentum ganda (relatif + mutlak)** — `pulangan 252 hari dalam 2 teratas alam DAN pulangan 252 hari > 0` · QuantJourney W04 / Antonacci (quantjourney-bt) · SEDIA · syarat mutlak ialah penapis rejim terbina dalam

### OSILATOR

**N84 Schaff Trend Cycle silang naik 25** — `stc silang naik 25` · Doug Schaff (pandas_ta) · PERLU:stc · MACD melalui dua lapisan stokastik

**N85 QQE silang naik** — `qqe garis cepat silang naik garis perlahan` · QQE (Quantitative Qualitative Estimation) (pandas_ta) · PERLU:qqe

**N93 Fisher Transform silang naik 0** — `fisher silang naik 0` · John Ehlers (pandas_ta) · PERLU:fisher

**N94 Pretty Good Oscillator > 3** — `pgo(14) > 3` · Mark Johnson (pandas_ta) · PERLU:pgo · sumber: > 3 bermakna pecah kuat, < -3 jual kuat

**N97 Coppock Curve silang naik 0** — `coppock silang naik 0` · Edwin Coppock (Barron’s 1962) (pandas_ta) · PERLU:coppock · JUJUR: direka untuk isyarat BULANAN pada indeks, bukan swing saham harian

**N98 KST silang naik garis isyarat** — `kst silang naik kst_sig` · Martin Pring (pandas_ta) · PERLU:kst

**N100 True Momentum Oscillator silang naik garis isyarat** — `tmo silang naik tmo_sig` · pandas_ta (tmo) (pandas_ta) · PERLU:tmo

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

**X26** — `ekori 4% (peratus tetap, bukan ATR)` · QuantJourney O09 (quantjourney-bt) · SEDIA · ekor diurus enjin isi, bukan dikemas kini strategi

**X27** — `sasaran limit +3% atas harga masuk purata` · QuantJourney O03 (quantjourney-bt) · SEDIA · bandingkan dengan dapatan KOMBINASI.md: sasaran kecil merugikan

**X28** — `sasaran limit +4%; keluar pasaran jika tutup < MA50` · QuantJourney O04 (quantjourney-bt) · SEDIA · sasaran DAN kegagalan trend sebagai dua keluar berasingan

**X29** — `pegang tetap 10 bar kemudian keluar pasaran` · QuantJourney O05/O14 (quantjourney-bt) · SEDIA

**X30** — `keluar bila macd < macd_sig` · QuantJourney W22 (quantjourney-bt) · SEDIA

**X31** — `keluar bila jatuh keluar 3 teratas pangkat 252 hari; imbang bulanan` · QuantJourney W15 (quantjourney-bt) · SEDIA

**X32** — `imbang semula berkala sahaja, tiada syarat keluar lain` · QuantJourney W04 (quantjourney-bt) · SEDIA · keluar hanya berlaku apabila pangkat berubah pada tarikh imbang

## Cara masuk diisi (paksi ketiga)

**Repo hanya pernah menguji `C01`.** Setiap keputusan dalam REVERSE, setiap kedudukan dalam Papan Penganalisis dan setiap baris Lejar Penuh menganggap belian berlaku pada **buka sesi berikutnya**, tanpa syarat. Itu bukan satu-satunya pilihan, dan ia PUNCA kecacatan yang sudah diukur: `KOLAM_EKOR.md` §4a mendapati 421 daripada 1,770 posisi C ditutup dibeli DAN dihentikan pada hari masuk dengan kadar menang **0.00%**. Pesanan buy-stop atau buy-limit mengubah tepat perkara itu, kerana harga isi tidak lagi ditetapkan oleh buka tanpa mengira apa yang bar itu buat.

**C01** — `beli pada buka sesi berikutnya` · asas repo (repo) · DIUJI · asas SEMUA keputusan kajian setakat ini; juga PUNCA kecacatan henti hari-0 (KOLAM_EKOR.md §4a: 421/1,770 posisi C dibeli dan dihentikan pada hari masuk, menang 0.00%)

**C02** — `buy-stop pada tinggi 20 hari x 1.002; luput selepas 5 bar` · QuantJourney O05 (quantjourney-bt) · SEDIA · pengesahan harga: tiada isi bermakna tiada dagangan, jadi ia MENAPIS pecah palsu pada peringkat pelaksanaan, bukan peringkat isyarat

**C03** — `buy-limit 1.5% bawah tutup isyarat; luput selepas 3 bar` · QuantJourney O03 (quantjourney-bt) · SEDIA · isi pasif; sumber pasangkan dengan rsi14 < 40 (N75)

**C04** — `buy-limit 1% bawah tutup isyarat` · QuantJourney O04 (quantjourney-bt) · SEDIA · sumber syaratkan tutup > ma50 (N76) sebelum meletakkan limit

**C05** — `OCO: buy-limit -2% lawan buy-stop +2%; yang isi dahulu batalkan yang lain` · QuantJourney O14 (quantjourney-bt) · SEDIA · menguji undur lawan pecah pada saham yang SAMA tanpa memilih dahulu

**C06** — `bracket: masuk pasaran + sasaran +6% + henti -3% sebagai pasangan OCO` · QuantJourney O12 (quantjourney-bt) · SEDIA · henti dan sasaran aktif serentak sejak bar masuk

**C07** — `buy-stop 1% atas tinggi semalam` · panduan pecah (blog) · SEDIA

**C08** — `beli pada tutup hari isyarat` · umum (umum) · PERLU:isi_tutup · TIDAK boleh dilaksanakan dalam papertrade repo kerana isyarat dikira SELEPAS tutup; didaftar hanya sebagai siling teori

## Urutan alam (paksi keempat)

Bila isyarat melebihi slot, sesuatu mesti menentukan siapa dibeli. Itu **bukan** penapis: penapis MEMBUANG bar, urutan MENYUSUN bar. Perbezaan itu penting kerana `SETUP.md` mengukur bahawa setiap penapis merugikan (0 daripada 598 dengan lift positif) **dan sebabnya struktur** — menapis membuang peluang pada ekor kanan, satu-satunya bahagian yang membayar. Menyusun tidak membuang apa-apa.

Dan `SISTEM.md` mengukur sesuatu yang lebih kuat: urutan ikut **skor berterusan** mempunyai sebaran 20 benih **0.00 mata**, manakala susunan sewenang-wenang mempunyai hingar pemilihan **17.3 mata peratus setahun** (`KEPEKATAN_BENIH.md`). Jadi keputusan atas skor berterusan boleh dipercayai pada sampel jauh lebih kecil. Itu satu-satunya struktur dalam seluruh kajian yang mempunyai sifat itu.

**U01** — `rawak berbenih` · kawalan repo (repo) · DIUJI · hingar pemilihan 17.3 mata peratus/tahun pada 8 slot (KEPEKATAN_BENIH.md); jalur 20 cabutan dalam portfolio_slot/rawak_jalur_ekuiti.csv

**U02** — `RS pasaran tertinggi` · repo (repo) · DIUJI · lorong RS_10; 29 Okt 2026 -2.15%, persentil 0 dalam jalur rawak (BANDING_SPUS.md)

**U03** — `skor momentum Clenow: (exp(cerun regresi log 90 hari x 252) - 1) x R^2` · Clenow (buku) · DIUJI · Sistem B; sebaran 20 benih 0.00 = TIADA hingar pemilihan (SISTEM.md). Ini satu-satunya struktur dalam seluruh kajian yang keputusannya boleh dipercayai pada sampel kecil.

**U04** — `gabungan kaedah beku dengan kuota slot` · repo (repo) · DIUJI · lorong GABUNGAN_10 / TOP1_10 / RAWAK_KAEDAH_10

**U05** — `skor gabungan Papan Penganalisis (backtest dipotong)` · repo (repo) · DIUJI · KAEDAH_TERBAIK.md: pangkat backtest TIADA kuasa ramalan yang boleh diukur - rho +0.16, p = 0.105 selepas mengawal hari pegang. JANGAN guna sebagai urutan.

**U06** — `101 alfa formula harga-volum (rank, ts_rank, scale -> satu skor)` · Kakushadze, Lauprete & Tulchinsky, arXiv:1601.00991 Appendix A (arXiv) · PERLU:arxiv · arxiv.org DISEKAT DNS dalam sesi ini. Formula TIDAK boleh ditulis daripada ingatan - mesti dibaca daripada Appendix A. Alfa proprietari WorldQuant LLC, diterbitkan dengan kebenaran: daftar rujukan dan laksana sendiri, JANGAN salin pukal ke repo. Inputnya hampir semuanya harga-volum harian (buka, tinggi, rendah, tutup, volum, vwap) = sepadan dengan alam repo.

**U07** — `212 peramal keratan rentas + SignalDoc (status replikasi setiap satu)` · Chen & Zimmermann, Critical Finance Review 2022 (openassetpricing.com / Hugging Face) · PERLU:huggingface · Pakej PyPI openassetpricing 0.1.0 SUDAH dimuat turun dan dibaca, tetapi datanya di huggingface.co yang DISEKAT proksi (403 CONNECT tunnel). Nilainya bukan peramal baharu: ia memberitahu peramal mana yang SUDAH diukur dan mana yang bertahan, jadi ia menghentikan repo mengukur semula ruang yang sudah diukur.

**U08** — `ATR% songsang sebagai URUTAN (bukan sebagai saiz)` · belum diuji (repo) · SEDIA · RISIKO_10 guna ATR untuk SAIZ atas susunan RS_10; ini akan guna ATR untuk URUTAN. Belum pernah diuji dan boleh dijalankan dengan lajur yang sudah ada.

## Saluran rangkaian: apa yang boleh dicapai dalam sesi awan

Diuji 30 Okt 2026. Ini menentukan sumber mana yang boleh digunakan sekarang dan mana yang perlu dibenarkan dahulu.

**BERFUNGSI:** PyPI (`pip download` bagi mana-mana pakej), carian web.

**DISEKAT:** `arxiv.org` (DNS), `huggingface.co` (proksi 403 CONNECT tunnel), `quants.md` (DNS), `www.quantifiedstrategies.com` (DNS), `quantifiedstrategies.substack.com` (DNS).

Akibatnya **PyPI ialah saluran sumber yang paling boleh dipercayai**: pakej yang **membenamkan** definisinya dalam kod boleh dibaca, pakej yang **mengambil** datanya dari hos lain tidak. Itu sebab `openassetpricing` 0.1.0 dapat dimuat turun tetapi datanya tidak (`U07`), manakala `pandas_ta` dapat dibaca sepenuhnya.

## Sumber: apa yang setiap satu sebenarnya beri

**QuantJourney Backtester** (`quantjourney-bt` 0.12.5, Apache 2.0, PyPI) — ia sebuah **rangka kerja**, bukan katalog kelebihan. 50 contoh strateginya berjalan pada 3 ETF (SPY/QQQ/IWM) atau 9 ETF sektor, dan logik isyaratnya mudah (silang SMA, pembalikan RSI, Donchian, MACD, Bollinger). Nilai sebenarnya kepada repo ini ialah **mekanik pelaksanaan**: ia memodelkan MARKET, LIMIT, STOP, STOP_TRAIL, STOP_LIMIT, BRACKET dan OCO dengan luput-selepas-N-bar — kesemuanya `C02`-`C06` dan `X26`-`X29` di atas. Ia juga ada walk-forward dengan **purge + embargo** (`example_wf_03`), yang WFO repo tiada. **`example_wf_05` guna Optuna: JANGAN guna** — arahan kajian melarang Optuna dan apa-apa pengoptimum. Ia TIDAK ditambah sebagai kebergantungan repo: repo sudah ada enjinnya sendiri, dan dua enjin bermakna dua sumber kebenaran.

**pandas_ta** (`pandas-ta` 0.4.71b0, MIT, Kevin Johnson) — ~150 indikator terkod dalam 8 kategori (candle · momentum · trend · volatility · volume · overlap · cycle · statistics). Ia memberi `N81`-`N100`: TTM Squeeze Carter yang betul (BB dalam KC, bukan lebar BB), Connors RSI **tiga komponen** (repo hanya ada `rsi2`), AlphaTrend, Schaff Trend Cycle, QQE, Vortex, VHF, Elder Force Index, Elder Ray, Klinger, Time Segmented Volume, Alligator, Fisher Transform, Pretty Good Oscillator, Choppiness, Random Walk Index, Coppock, KST, ATR Trailing Stop, TMO. **JANGAN pasang sebagai kebergantungan:** ia memerlukan `numba==0.61.2` yang memaksa `numpy<2.3`, sedangkan persekitaran repo ialah numpy 2.5.3 + pandas 3.0.5 — pemasangan akan MENURUNKAN taraf numpy dan berisiko merosakkan workflow malam. Guna ia sebagai **rujukan spesifikasi** (lesen MIT membenarkan, dengan atribusi) dan laksanakan indikator yang diperlukan terus dalam `REVERSE/teras/ind.py`, sama seperti 71 lajur yang lain.

**AMARAN STRUKTUR tentang N81-N100.** Kedua puluh ini ialah **penapis**, dan ruang penapis sudah diukur: `SETUP.md` mendapati **0 daripada 598** setup mempunyai lift positif, dengan sebab **struktur** bukan pemilihan. Menambah 20 penapis lagi dijangka gagal dengan cara yang sama. Ia didaftar supaya ia tidak dicari lagi, bukan kerana saya menjangka ia lulus. **Yang berbeza secara jenis ialah `U06`-`U08` (urutan) dan `C02`-`C06` (cara) — bukan indikator lagi.**

**Quantpedia** — sudah menjadi sumber dalam repo ini sejak Okt 2026: `spec/KATALOG_K145.md` memetiknya bagi K195, K241, K242 dan K270. Populasinya ialah **strategi faktor/portfolio akademik**, kebanyakannya pangkat keratan rentas yang diimbang bulanan atau suku tahunan. Itu paksi **pembinaan**, yang `REVERSE/PEMBINAAN.md` sudah ukur dan tolak lawan SPUS. Jadi Quantpedia akan menambah banyak strategi, tetapi kebanyakannya dalam paksi yang sudah ditutup. Yang berasaskan bar OHLCV harian masuk ke sini (contoh `N80`); yang berasaskan faktor bulanan kekal dalam katalog K.

**Quantified Strategies** — `www.quantifiedstrategies.com` dan `quantifiedstrategies.substack.com` KEDUA-DUANYA tidak dapat diselesaikan (DNS) dalam sesi awan ini. `N16`, `N18` dan `X07` didaftar daripada ringkasan carian web, BUKAN daripada teks penuh sumber. Untuk peraturan penuh, domain itu perlu dibenarkan dalam tetapan rangkaian sesi.

**quants.md** — tidak dapat diselesaikan (DNS) dalam sesi ini; belum dinilai. Perlu dibenarkan dalam tetapan rangkaian sesi sebelum apa-apa daripadanya boleh didaftar.

## Sempadan K / M / N

Tiga katalog, tiga populasi berbeza. Jangan campur.

- **K1-K397** (`spec/KATALOG_K145.md`) — calon kaedah daripada kajian dalam talian dan akademik, termasuk Quantpedia. 47 daripadanya menjadi M115-M161.
- **Mxx** (`spec/SPEC_SEMUA_KAEDAH.md`, `kod/kaedah/`) — kaedah lengkap yang sudah dikodkan dan dijalankan setiap malam dalam Lejar Penuh.
- **Nxx** (fail ini) — kombinasi indikator gaya pedagang pada bar harian, didaftar dahulu dan diuji kemudian, dengan paksi `CARA` yang K dan M tiada.

## Cara menguji

1. Pradaftar: tulis `REVERSE/SPEC_<nama>.md` dengan senarai id yang akan diuji, pecahan LATIH/TAHAN, dan jangkaan priori. Komit sebelum larian.
2. Kira lift lawan asas keluar yang sama (bukan jangkaan mutlak — kesilapan `SPEC_SETUP.md` §4).
3. Syarat lulus: lift positif pada KEDUA-DUA tingkap, BH-FDR q <= 0.05 merentas bilangan ujian yang dipradaftar, dan jangkaan selepas buang 5% teratas kekal positif.
4. Setakat ini hanya `N01` (MA10 silang MA20 + volum >= 1.2x) mencapai syarat 1 dan 2; tiada satu pun mencapai syarat 3.
