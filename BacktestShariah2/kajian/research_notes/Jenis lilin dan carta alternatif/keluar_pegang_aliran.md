# Jenis lilin dan carta alternatif sebagai peraturan KELUAR / pegang aliran (lawan Chandelier tutup 4×ATR14)

Skop: Heikin-Ashi (HA), HA dilicinkan, Renko, Kagi, Line Break (Three Line Break), Point & Figure (P&F), range bar — digunakan sebagai peraturan keluar/trailing bagi swing long saham AS (data harian OHLCV sahaja, isyarat pada tutup, laksana buka esok), dibandingkan dengan Chandelier tutup (tutup < tutup tertinggi sejak beli − 4×ATR14, paras hanya naik).

Nota kaedah penyelidikan: carian web berjaya, tetapi hampir semua halaman penuh (quantifiedstrategies.com, stockcharts.com, fidelity.com, liberatedstocktrader.com, readthedocs) disekat oleh proksi sesi ini (DNS/CONNECT 403). Maka angka di bawah datang daripada ringkasan hasil carian dan abstrak, bukan teks penuh — setiap satu ditanda. Bukti setempat repo (KAJIAN_LORONG2.md) dipetik terus daripada fail.

## 1. Bukti empirikal / backtest bagi HA, Renko, Kagi, Line Break, P&F (keluar atau ikut aliran) pada data harian saham

### Takeaway
Tiada kajian akademik atau ujian pengamal yang ketat (berskala ribuan saham, kos, luar sampel) yang menguji mana-mana jenis carta ini sebagai peraturan KELUAR untuk swing long saham AS. Bukti yang ada adalah kecil (satu indeks/satu pasaran), dari forex/niaga hadapan, atau blog vendor dengan kaedah tidak didedahkan; satu-satunya ujian majalah yang boleh dikesan (Carr 2008, P&F, S&C) menyimpulkan isyarat P&F ringkas "mengecewakan".

### Cited Findings
**Heikin-Ashi**
- Satu-satunya kertas berwasit yang ditemui: Trivedi (2022), *International Journal of Finance & Economics*, menguji HA dan HASTOC (stokastik atas HA) pada tiga mata wang, satu indeks dan satu saham, tiga rangka masa; pulangan positif konsisten hanya "for select time frames and markets"; ada bootstrap dan ujian luar sampel. Bukan saham AS berskala luas; bukan kajian keluar. — [Wiley abstract](https://onlinelibrary.wiley.com/doi/abs/10.1002/ijfe.2245); [ResearchGate](https://www.researchgate.net/publication/343798625_Technical_analysis_using_Heiken_Ashi_Stochastic_To_catch_a_trend_use_a_HASTOC)
- Versi kertas kerja HASTOC (MPRA) diuji pada data sejam USD/INR (forex intrahari — tidak relevan terus). — [MPRA 89594](https://mpra.ub.uni-muenchen.de/89594/)
- Păuna (ITEMA 2018; IJEMS 2019) "Smoothed Heikin-Ashi algorithms": satu backtest DAX30 2015–2018, 78 dagangan, tanpa pengesahan luar sampel/pelbagai pasaran; pengarang sendiri menyebutnya model matematik. — [ITEMA PDF](https://www.itema-conference.com/wp-content/uploads/2019/09/pauna_smoothed_heikin-ashi_algorithms_optimized_for_automated_trading_systems_pp_514-525.pdf); [ResearchGate](https://www.researchgate.net/publication/328811639_SMOOTHED_HEIKIN-ASHI_ALGORITHMS_OPTIMIZED_FOR_AUTOMATED_TRADING_SYSTEMS)
- Quantified Strategies (blog pengamal, ringkasan carian sahaja): sistem HA ikut aliran BULANAN atas S&P 500 sejak 1960 — pulangan tahunan 5.2% lawan 7.5% beli-dan-pegang, drawdown maksimum 29% lawan 52.56%; varian lain bulanan CAGR 8.4%, drawdown 28% (B&H 55%), dilabur 73% masa; satu lagi ujian melaporkan kadar menang 52% dan drawdown lebih rendah tetapi pulangan mutlak lebih rendah daripada B&H. Ini indeks, bukan saham individu, dan tidak menguji HA sebagai keluar swing. — [Quantified Strategies HA rules (substack)](https://quantifiedstrategies.substack.com/p/heikin-ashi-trading-rules-and-strategy); [Quantified Strategies HA strategy](https://www.quantifiedstrategies.com/heikin-ashi-trading-strategy/)
- Liberated Stock Trader (vendor, mempromosi TrendSpider; kaedah tidak penuh): atas 30 saham Dow selama 8 tahun, EMA20 pada carta HA "83% win rate across 111 trades", manakala tetapan OHLC biasa rugi; MACD harian pada HA hanya mengatasi B&H 26% masa. "Win rate" sering bermaksud peratus ticker yang mengatasi B&H, bukan peratus dagangan menang — angka tidak setara. — [LST EMA](https://www.liberatedstocktrader.com/exponential-moving-average/); [LST MACD](https://www.liberatedstocktrader.com/macd-indicator/); [LST HA](https://www.liberatedstocktrader.com/heikin-ashi-candles/)
- Tuntutan "66% daripada 30 saham AS mengatasi indeks dalam 12 tahun" dan "HA meramal arah lilin seterusnya hingga 75%" muncul di Wikipedia/laman pendidikan tanpa kajian asal yang boleh dikenal pasti. — [Wikipedia Heikin-Ashi](https://en.wikipedia.org/wiki/Heikin-Ashi_chart)
- Pendapat forum (anekdot): HA "terrible for entries but great indicator for exit". — [TradingQnA](https://tradingqna.com/t/are-heikin-ashi-strategies-actually-profitable/131520)
- Vervoort, "Trading with the Heikin-Ashi Candlestick Oscillator" (HACO), S&C Dis 2008; versi jangka panjang S&C Ogos 2012 (TEMA atas data HA dan HL2). Artikel memberi peraturan, bukan statistik saham berskala luas (teks penuh berbayar). — [Traders' Tips Dis 2008](https://www.traders.com/Documentation/FEEDbk_docs/2008/12/TradersTips.html); [MotiveWave HACO LT](https://motivewave.com/studies/heikin_ashi_candles_oscillator_lt.htm)

**Point & Figure**
- Anderson & Faff (2008), *International Review of Financial Analysis* 17:198–217: kaedah pengiraan P&F daripada data frekuensi ultra-tinggi; lapan peraturan objektif atas niaga hadapan S&P 500 1990–1998; dengan pelarasan bootstrap, kesignifikanan "mixed" — sesetengah peraturan signifikan, banyak tidak. (Niaga hadapan, sebelum 2000.) — [Western Sydney Univ](https://researchers.westernsydney.edu.au/en/publications/point-and-figure-charting-a-computational-methodology-and-trading/); [Bond Univ](https://research.bond.edu.au/en/publications/point-and-figure-charting-a-computational-methodology-and-trading/)
- Carr, "Testing Point & Figure Patterns", S&C V.26:9 (2008), saham S&P 500, pegangan 5/20/60 hari: dalam tempoh lebih panjang hanya isyarat beli triple-top mengatasi pasaran; penapis aliran "did not result in any significant performance improvement"; kesimpulan: pedagang yang bergantung semata-mata pada isyarat P&F ringkas "would be disappointed". Angka jadual triple-top (48.48 / 31.57 / 91.71 lawan pasaran 56.27 / 61.90 / 68.72) — label lajur tidak jelas dalam petikan, jangan tafsir sebagai % pulangan tanpa teks penuh. — [Fidelity PDF Carr](https://www.fidelity.com/bin-public/060_www_fidelity_com/documents/TestingPointFigure.pdf); [Traders.com arkib Carr](https://technical.traders.com/archive/combo/display5.asp?author=Michael+Carr+CMT)
- Tuntutan "64% / 72% kadar menang double/triple top (Dorsey Wright)" dan "65–75% kejayaan double-top atas garis sokongan 45°" tiada metodologi/kajian boleh dikesan — tahap pemasaran. — [TradeAlgo](https://www.tradealgo.com/trading-guides/technical-analysis/point-and-figure-charts-the-classic-method-for-spotting-breakouts-and-price-targets); [Finwiz](https://finwiz.io/technical-analysis/point-and-figure)

**Renko / Kagi**
- Pastukhov (2004), *Theory of Probability and its Applications* 49(2): asas matematik model renko & kagi, konsep H-volatiliti; bagi proses Wiener sifat H-volatiliti berbeza daripada pasaran sebenar, menandakan peluang arbitraj yang diperoleh dengan strategi renko-/kagi-H. Teori, bukan backtest saham. — [Math-Net.ru](https://mathnet.ru/eng/tvp220); [SIAM](https://epubs.siam.org/doi/10.1137/S0040585X97981020)
- Hudson & Thames: H-volatiliti = purata jarak antara titik pusingan bersebelahan; H-volatiliti tinggi → proses cenderung bergerak satu arah lama sebelum berpusing (bacaan momentum); proses balik-min ada lebih banyak H-inversion. — [Hudson & Thames docs](https://hudson-and-thames-arbitragelab.readthedocs-hosted.com/en/latest/time_series_approach/h_strategy.html); [Hudson & Thames blog](https://hudsonthames.org/pairs-trading-based-on-renko-and-kagi-models/)
- Bogomolov (2013), *Quantitative Finance* 13(9):1411–1430: dagangan pasangan berasaskan renko/kagi, untung teori bagi proses OU (pasangan, bukan long-only). — [IDEAS](https://ideas.repec.org/a/taf/quantf/v13y2013i9p1411-1430.html)
- Sun (2025), kertas kerja Univ. Warsaw (pendahuluan): strategi pasangan Renko/Kagi atas indeks ekuiti AS & China — lebihan pulangan signifikan sebelum kos; geseran dagangan mengurangkan untung; Renko lebih tahan terutama semasa krisis. — [WNE UW PDF](https://www.wne.uw.edu.pl/download_file/6099/0)
- Tiada ujian Renko/Kagi sebagai keluar long saham dengan angka ditemui; panduan broker sahaja (cth. "start with an ATR(14)-based box ... bigger boxes for swing"; jika carta berbalik setiap 2–3 bata, kotak terlalu kecil; saiz kotak terbaik masa lalu tidak semestinya terbaik ke hadapan). — [NAGA academy Renko](https://naga.com/en/academy/renko-charts)

**Line Break / range bar**
- Tiada angka backtest Three Line Break atau Kagi atas saham ditemui; sumber hanya peraturan dan amaran (lihat bahagian 3). Skrip TradingView Three Line Break menyatakan "for purpose educate only". — [TradingView threelinebreak](https://tradingview.com/scripts/threelinebreak)

**Bukti setempat repo (bukan carta alternatif, tetapi garis dasar)**
- KAJIAN_LORONG2.md: 763,327 dagangan enjin v1.2, 134 kaedah, set 431, masuk 1 Nov 2019 – 2 Okt 2026, kos 0.1% sebelah; >30 calon keluar (N tutup turun 2–4, Chandelier tinggi/tutup 2–5×ATR14/22, trailing 8–25%, MA20/MA50, rendah 10/20 hari, mingguan). Pilihan Chandelier tutup 4×ATR14 paras naik tanpa henti: purata 5.1%, median −2.8%, 5% terburuk −18.2%, 43.8 hari, 2.4%/bulan, lebihan SPY 1.2%/bulan, atasi lorong 1 dalam 80% kaedah. Peraturan lama "2 tutup turun" paling lemah (keluar purata selepas 7 hari, hampir tiada bahagian trend besar). Lebihan tertumpu pada tahun 2020 dan 2025; tanpa kedua-duanya semua varian Chandelier 3–5×ATR sedikit bawah SPY. — [KAJIAN_LORONG2.md (repo)](../../KAJIAN_LORONG2.md)

### Inferences
- Tahap bukti: tiada satu pun jenis carta alternatif mempunyai bukti ketat bahawa ia memberi keluar yang lebih baik bagi swing long saham AS. Bukti "positif" HA berasal daripada vendor (Liberated Stock Trader) atau indeks bulanan (Quantified Strategies), dan bukti P&F yang paling objektif (Carr 2008; Anderson & Faff 2008) adalah bercampur/negatif.
- Kerana HA tanpa pengesahan ialah penapis sangat pantas (lihat bahagian 4), ia dijangka berkelakuan seperti "2 tutup turun" — calon paling lemah dalam KAJIAN_LORONG2. HA mentah tidak wajar dijangka mengatasi Chandelier 4×ATR untuk objektif "pegang selagi naik".
- Satu-satunya cara mendapat jawapan sah ialah menguji sendiri dalam rangka `kajian/lorong2/kaji_lorong2.py` (set dagangan, kos, metrik sama).

### Gaps
- Tiada teks penuh Quantified Strategies, Carr, Trivedi atau Vervoort dapat dibaca (proksi menyekat) — peraturan tepat dan jadual penuh tidak disahkan.
- Tidak ditemui ujian Oxfordstrat, Bulkowski atau Kaufman ("Trading Systems and Methods") dengan angka khusus bagi HA/Renko/Kagi/Line Break/P&F sebagai keluar; Kaufman membincangkan P&F dan swing charts, tetapi tiada petikan angka yang boleh disahkan dalam sesi ini.
- Tiada bukti Line Break atau range bar pada saham sama sekali.

## 2. Perbandingan dengan ATR / Chandelier / trailing peratus — kajian kepala-ke-kepala

### Takeaway
Tiada kajian kepala-ke-kepala carta alternatif lawan Chandelier ditemui. Kajian trailing stop yang ada (pengamal) bercanggah: Decoding Markets (≈11,000 saham AS sejak 1990) mendapati trailing 20–25% mengatasi Chandelier (ATR baru elok pada ≥5×), manakala kajian repo sendiri (2019–2026) mendapati Chandelier tutup 4×ATR14 mengatasi trailing 8–25%. Literatur akademik stop-loss menyokong nilai stop hanya apabila ada momentum/rejim.

### Cited Findings
- Decoding Markets / Stocks & Trading: ≈11,000 saham AS sejak Julai 1990 — trailing peratus "outperforms the Chandelier exit in almost every case"; skor pulangan/risiko ATR terbaik ≈ separuh skor peratus terbaik; hentian ATR(21) mata memberi pulangan/risiko negatif; Chandelier bertambah baik dengan pengganda ≥5; trailing 20% dan 25% "does a decent job of capturing upward trends"; "The Chandelier stop and moving average line produced disappointing results". (Ringkasan carian; kaedah penuh tidak dibaca.) — [Decoding Markets](https://decodingmarkets.com/which-trailing-stop-is-the-best/); [stocksoftresearch mirror](https://stocksoftresearch.com/which-trailing-stop-is-the-best/)
- Bercanggah dengan repo: dalam KAJIAN_LORONG2, "Trailing % tetap tidak mengatasi SPY selepas pegangan panjang", dan Chandelier 4×ATR "paling cekap" juga pada ujian titik masuk proksi breakout (13,306 dagangan). — [KAJIAN_LORONG2.md (repo)](../../KAJIAN_LORONG2.md)
- Incredible Charts: hentian ATR lebih adaptif daripada hentian peratus tetapi "achieve similar results when applied to stocks that have been filtered for a strong trend". — [Incredible Charts ATR trailing](https://www.incrediblecharts.com/indicators/atr_average_true_range_trailing_stops.php)
- Arthur Hill (StockCharts, 2016): RSI(5) balik-min + Chandelier keluar, SPY/QQQ/IJR 2000–2016 harian, komisen $10; Chandelier ketat (22,1) memperbaiki CAR dan kadar menang berbanding tetapan lebih lebar; IJR CAR/MDD 0.86, menang 83%; IJR naik lagi 3–5% selepas keluar. Hanya ETF, kemasukan balik-min, tiada perbandingan peratus. — [StockCharts Arthur Hill](https://articles.stockcharts.com/article/articles-arthurhill-2016-12-systemtrader---testing-a-mean-reverion-system-with-the-chandelier-exit-spy-qqq-ijr---rsi5/)
- Chandelier kanonik LeBeau = tertinggi 22 bar − 3×ATR; sama ada keluar atas sentuhan intrabar atau tutup sahaja ialah pilihan pelaksanaan yang mengubah hasil (ujian berbeza tidak boleh dibanding terus). — [LuxAlgo trailing taxonomy](https://www.luxalgo.com/library/concept/trailing-method-taxonomy.md)
- Kaminski & Lo (J. Financial Markets 2014): di bawah jalan rawak, peraturan stop-loss 0/1 mengurangkan pulangan jangkaan; dengan momentum stop boleh menambah nilai; data bulanan 1950–2004: sesetengah peraturan menambah 50–100 bp/bulan semasa tempoh stop-out (dikaitkan dengan "flight-to-quality"). — [MIT DSpace](https://dspace.mit.edu/handle/1721.1/114876)
- Han & Zhou (2014) "Taming Momentum Crashes": stop 10% pada strategi momentum (1926–2011) — kerugian bulanan terburuk EW dari ≈−49.79% ke ≈−11.34%; VW ≈−65.34% ke ≈−23.69%; purata pulangan dan Sharpe lebih daripada dua kali; Alpha Architect: lebih banyak dagangan, kos tidak dimasukkan. — [Alpha Architect](https://alphaarchitect.com/2016/08/taming-the-momentum-roller-coaster-fact-or-fiction/)
- Tuntutan "kajian Journal of Trading 2021: hentian ATR mengatasi hentian peratus 1.7%/tahun, drawdown 12% lebih rendah" — tidak dapat disahkan wujud; anggap tidak sah. — [LuxAlgo ATR stop (sumber tuntutan sekunder)](https://www.luxalgo.com/blog/5-atr-stop-loss-strategies-for-risk-control/)

### Inferences
- Hubungan matematik (diterbitkan daripada definisi, bukan dari kajian): Renko tutup dengan bata b dan balikan 2 bata, P&F kotak b dengan balikan 3 kotak, dan Kagi dengan balikan R pada dasarnya ialah trailing stop dari puncak yang DIKUANTUM. Contoh: Renko b = 2×ATR14, balikan 2 bata ≈ Chandelier 4×ATR, tetapi paras hanya naik dalam langkah b, jadi jarak sebenar dari tutup tertinggi berada antara 4 dan 6×ATR (bata separa tidak dikira). Kagi dengan R tetap (balikan dari ekstrem) = trailing stop jarak tetap R — sama dengan Chandelier jika R = 4×ATR14 dibekukan pada hari beli. Maka beza utama yang boleh diuji ialah (a) kuantum/langkah, (b) ATR dibeku lawan bergerak, (c) peraturan "yin/double-bottom" (pecah paras rendah ayunan sebelumnya) yang lebih longgar daripada balikan mudah.
- Kerana KAJIAN_LORONG2 mendapati Chandelier lebih longgar (paras boleh turun, 54.1 hari) memberi purata 6.1% dan trend besar 29.4% berbanding 5.1%/25.1%, peraturan carta alternatif yang efektifnya LEBIH LONGGAR (Renko/P&F terkuantum, Kagi yin, Line Break dalam lonjakan besar) dijangka menaikkan purata dan bahagian trend besar tetapi memburukkan 5% terburuk — pertukaran yang sama, bukan "alpha" baharu.
- Literatur stop-loss (Kaminski & Lo; Han & Zhou) menunjukkan nilai sebarang trailing datang daripada momentum/rejim, bukan daripada bentuk carta; maka jenis carta tidak dijangka mengubah keputusan secara asas berbanding parameter jarak.

### Gaps
- Tiada kajian membanding Renko/Kagi/P&F/Line Break/HA lawan Chandelier/ATR pada set dagangan sama.
- Kaedah penuh Decoding Markets (Chandelier dari tinggi atau tutup, kos, kemasukan) tidak dapat dibaca; percanggahan dengan repo mungkin disebabkan kemasukan berbeza (rawak/semua saham lawan isyarat kaedah) dan tempoh (1990– lawan 2019–2026).

## 3. Perangkap yang diketahui

### Takeaway
Perangkap utama: (1) harga HA bukan harga boleh didagang; (2) Renko/P&F/Kagi/Line Break bergantung laluan dan sering diuji secara tidak realistik (data intrabar dibuang, "open" bata palsu, saiz bata ATR yang dikira semula atas seluruh sejarah); (3) lag dan whipsaw. Kesemuanya boleh dielak dengan membina carta daripada TUTUP harian sahaja, saiz bata dibekukan/diketahui pada masa itu, dan pelaksanaan pada buka sebenar esok.

### Cited Findings
- HA: enjin backtest biasa mengisi pada buka bar seterusnya dan "the Open price is a pure fabrication on Heikin Ashi bars"; penyelesaian = isyarat daripada HA, pelaksanaan pada lilin biasa. — [NinjaTrader forum](https://forum.ninjatrader.com/forum/ninjatrader-8/strategy-development/1128094-the-curious-case-of-heiken-ashi-bars); [TradingView HA strategy example](https://vn.tradingview.com/script/xFBoQENG-Heikin-Ashi-Strategy-Example)
- HA: tutup HA ketinggalan tutup sebenar, jadi isyarat pada tutup lilin hijau HA diisi dalam backtest pada harga di bawah harga pasaran sebenar; jalankan backtest atas lilin sebenar dengan yuran dan slippage ("backtest trap"). — [BJF Trading Group](https://bjftradinggroup.com/heikin-ashi-trading-strategy/)
- Formula HA (tutup HA = purata O,H,L,C; buka HA = purata buka & tutup HA sebelumnya) — rekursif, jadi nilai bergantung pada titik mula siri. — [Wikipedia Heikin-Ashi](https://en.wikipedia.org/wiki/Heikin-Ashi_chart)
- Renko: sokongan NinjaTrader — umumnya bukan idea baik backtest bata Renko kerana kelakuan tertentu tidak boleh disimulasi dengan data sejarah; data harga di luar bata akhir "is deleted from backtesting", mencipta bias positif bagi stop dan target; buka bata balikan berada satu bata dari buka sebenar. — [NinjaTrader Renko backtest](https://ninjatrader.com/support/forum/forum/ninjatrader-8/strategy-development/1126126-backtest-in-renko-charts); [NinjaTrader 31905](https://forum.ninjatrader.com/forum/historical-beta-archive/historical-version-7-beta-threads/version-7-beta-general-questions-bug-reports/31905-backtesting-renko-charts-invalid)
- Renko biasanya hanya guna harga tutup bagi rangka masa dipilih; bata separa tidak diplot sehingga jarak penuh dilalui. — [Wikipedia Renko](https://www.wikipedia.com/wiki/Renko_chart)
- Renko mod ATR: saiz bata berubah mengikut ATR semasa carta. — [TradingView Renko Overlay Ribbon](https://www.tradingview.com/script/stEIF1xR-Renko-Overlay-Ribbon/)
- Line Break & Kagi: pengguna MultiCharts melaporkan "great discrepancy between realtime and backtested results" (terutama bilangan dagangan); staf: isyarat dikira berbeza atas data sejarah dan masa nyata. — [MultiCharts forum](https://www.multicharts.com/discussion/viewtopic.php?p=37116)
- Three Line Break: perubahan garis ikut harga tutup; garis balikan apabila tutup melepasi tinggi/rendah N garis sebelumnya (lalai 3, boleh laras); elak dagang apabila garis berselang-seli (tiada aliran). — [Microsoft Chart docs](https://learn.microsoft.com/en-us/previous-versions/dd456721(v=vs.140)); [Fyers Line Break](https://fyers.in/school-of-stocks/chapter/technical-analysis/line-break-charts.html)
- Line Break tidak memerlukan amaun balikan pilihan pengguna; Kagi bergantung pada amaun balikan pengguna dan isyarat melalui ketebalan garis pada ekstrem sebelumnya. — [LuxAlgo Line Break](https://www.luxalgo.com/library/concept/line-break.md)
- Kagi: amaun balikan biasanya tetap tetapi boleh berdasarkan ATR; tiada garis jika pergerakan < amaun. — [TradingView Kagi experiment](https://www.tradingview.com/chart/BTCUSD/sYJ0X9wB-Big-Experiment-part-3-Kagi)
- Renko: saiz kotak terbaik masa lalu tidak semestinya terbaik ke hadapan (risiko lebih-padan parameter). — [NAGA academy Renko](https://naga.com/en/academy/renko-charts)
- Saiz sampel: jangan percaya backtest < 300–500 dagangan merentas ≥5 tahun; strategi aliran masuk drawdown dalam pasaran mendatar. — [TradingQnA](https://tradingqna.com/t/are-heikin-ashi-strategies-actually-profitable/131520)
- Keluar pada sentuhan intrabar lawan tutup sahaja mengubah hasil secara material. — [LuxAlgo trailing taxonomy](https://www.luxalgo.com/library/concept/trailing-method-taxonomy.md)

### Inferences
- Look-ahead khusus data harian: membina Renko/P&F/Kagi daripada TINGGI/RENDAH harian memerlukan andaian susunan laluan intrahari (tinggi dahulu atau rendah dahulu) — tidak diketahui daripada OHLC. Peraturan keluar mesti guna TUTUP sahaja (konsisten dengan Chandelier tutup repo), atau, jika guna rendah, keluar dilaksanakan pada buka esok sahaja (bukan pada paras), dan hari yang sama tidak boleh mencipta bata naik dan balikan sekaligus.
- Repaint: jika saiz bata = ATR terkini (cara biasa pada platform carta), seluruh sejarah bata berubah apabila ATR berubah → look-ahead. Untuk backtest, bekukan b = k×ATR14 pada hari beli (tutup hari isyarat), atau kemas kini b hanya secara sebab-akibat (ATR pada hari bata dibentuk).
- Kebergantungan laluan/titik mula: Renko/P&F/Kagi/HA bergantung pada bar pertama; bagi keluar, mulakan pembinaan pada harga beli (buka hari beli) atau tutup hari beli, supaya keputusan setiap posisi boleh dihasilkan semula dan bebas sejarah sebelum beli. HA perlu "pemanasan" ≥ 10–20 bar sebelum beli supaya buka HA rekursif stabil (pemanasan menggunakan data sebelum beli adalah sah kerana diketahui).
- Jurang (gap) dan earnings: semua peraturan tutup-sahaja keluar pada buka esok; carta bata tidak mengubah risiko jurang — kerugian 5% terburuk tidak dijangka bertambah baik berbanding Chandelier.
- Range bar memerlukan laluan intrahari; dengan OHLC harian ia hanya boleh dianggarkan dan akan mewarisi masalah susunan tinggi/rendah — tidak sesuai untuk projek ini.

### Gaps
- Tidak ditemui kajian formal (berwasit) tentang bias backtest Renko/Kagi/Line Break; bukti ialah forum vendor (NinjaTrader, MultiCharts) — arah konsisten tetapi tidak dikuantifikasi.
- Tidak disahkan secara bersumber bahawa TradingView "ATR box" mengira semula bata sejarah dengan ATR terkini (hanya inferens daripada penerangan "constantly changing in size").

## 4. Spesifikasi peraturan mekanikal yang wajar diuji sebagai "lorong 3" (data harian, tutup → buka esok)

### Takeaway
Calon paling munasabah ialah yang BERBEZA secara struktur daripada Chandelier: (a) HA dilicinkan / HA dengan pengesahan 2–3 bar (keluar lebih pantas apabila momentum hilang), (b) Renko/P&F tutup dengan kotak ATR dibekukan dan peraturan "double-bottom/yin" (keluar lebih longgar, ikut struktur ayunan), (c) Line Break 3 (tanpa parameter). Semua perlu diuji dalam `kaji_lorong2.py` dengan metrik sama seperti jadual KAJIAN_LORONG2; jangkaan awal (berdasarkan teori dan bukti) ialah tiada yang mengatasi Chandelier secara bermakna, kecuali mungkin sebagai peraturan longgar alternatif untuk trend besar.

### Cited Findings
- Definisi asas yang dipakai di bawah: HA (Wikipedia) — [Wikipedia Heikin-Ashi](https://en.wikipedia.org/wiki/Heikin-Ashi_chart); Renko tutup, bata penuh — [Wikipedia Renko](https://www.wikipedia.com/wiki/Renko_chart); Line Break N=3 lalai, tutup melepasi tinggi/rendah N garis — [Microsoft Chart docs](https://learn.microsoft.com/en-us/previous-versions/dd456721(v=vs.140)); Kagi balikan ATR — [TradingView Kagi](https://www.tradingview.com/chart/BTCUSD/sYJ0X9wB-Big-Experiment-part-3-Kagi); P&F triple-top = lajur X melepasi dua lajur X sebelumnya (cerminnya triple-bottom) — [Carr via Fidelity](https://www.fidelity.com/bin-public/060_www_fidelity_com/documents/TestingPointFigure.pdf); HA dilicinkan (EMA/TEMA atas data HA) — [MotiveWave HACO LT](https://motivewave.com/studies/heikin_ashi_candles_oscillator_lt.htm); [Wealth-Lab HeikinAshi (varian tutup "Valcu" lawan Vervoort)](https://www.wealth-lab.com/Support/ApiReference/HeikinAshi)
- Saiz bata permulaan ATR(14) atau 0.25–1% harga, lebih besar untuk swing; jika balik setiap 2–3 bata, terlalu kecil. — [NAGA academy Renko](https://naga.com/en/academy/renko-charts)
- Line Break 2 garis = lebih banyak isyarat balikan; lebih banyak garis = jangka lebih panjang. — [TradingView threelinebreak](https://tradingview.com/scripts/threelinebreak)

### Inferences (spesifikasi cadangan — reka bentuk, belum diuji)
Konvensyen semua calon: t0 = hari beli (beli pada buka t0). ATR = `enjin.atr` 14 (sama seperti lorong 2). Isyarat dinilai pada tutup hari t ≥ t0; jual pada buka t+1. Kos 0.1% sebelah. Tiada henti kaedah (selari dengan keputusan lorong 2). Laporkan: purata, median, 5% terburuk, hari, %/bulan, lebihan SPY/bulan, trend besar, Semikon 2026, % kaedah atasi lorong 1, serta tahun 2020/2025 dikecualikan.

1. **HA-N (Heikin-Ashi pengesahan)**
   - HAc_t = (O+H+L+C)/4; HAo_t = (HAo_{t−1} + HAc_{t−1})/2; benih HAo = (O+C)/2 pada bar 20 sebelum t0 (pemanasan 20 bar).
   - Merah: HAc < HAo. "Merah kuat": merah dan tiada bayang atas (HAh = max(H, HAo, HAc) == HAo).
   - Keluar: N bar merah berturut-turut, N ∈ {2, 3}; varian B: 1 bar "merah kuat"; varian C: N=2 dan tutup < tutup tertinggi sejak beli − 2×ATR14 (penapis jarak, elak keluar dalam rehat kecil).
   - Jangkaan: N=2 hampir setara "2 tutup turun" (terlalu pantas); N=3 dan varian C ialah yang berbaloi diuji.
2. **SHA-L (HA dilicinkan)**
   - O',H',L',C' = EMA_L bagi O,H,L,C (L ∈ {10, 20}); bina HA atas O'..C'; licin lagi HAo/HAc dengan EMA_L (bentuk Valcu/Vervoort; satu varian sahaja untuk elak lebih-padan).
   - Keluar: warna bertukar hijau → merah pada tutup (HAc'' < HAo''); varian dengan pengesahan 2 bar.
3. **RENKO-k-r (Renko tutup, bata ATR dibeku)**
   - b = k × ATR14(t0−1), k ∈ {1, 1.5, 2}; dibekukan sepanjang posisi (varian: b dikemas kini setiap kali bata naik baharu dibentuk, menggunakan ATR hari itu).
   - Asas T = tutup t0 (atau buka beli). Bata naik baharu bila C_t ≥ T + b (boleh beberapa bata sehari; T += b × floor((C_t − T)/b)).
   - Keluar bila C_t ≤ T − r×b, r ∈ {2, 3} (Renko tradisional r=2 = jatuh satu bata di bawah dasar bata naik terakhir).
   - Pasangan perbandingan langsung: (k=2, r=2) dan (k=1, r=4) ≈ Chandelier 4×ATR terkuantum — menguji kesan kuantum sahaja.
4. **PF-b-3 (Point & Figure tutup, balikan 3 kotak)**
   - Kotak b = 1×ATR14(t0−1) dibeku (varian: 2% harga beli). Hanya tutup.
   - Lajur X naik apabila C ≥ atas + b; lajur O bermula apabila C ≤ atas − 3b.
   - Keluar A: lajur O pertama (≈ trailing 3b terkuantum). Keluar B (isyarat jual Dorsey "double-bottom"): lajur O semasa jatuh di bawah dasar lajur O sebelumnya (jika tiada lajur O sebelumnya sejak beli, guna dasar = harga beli − 3b sebagai henti awal).
   - Keluar B ialah calon "struktur ayunan" yang lebih longgar; dijangka menaikkan trend besar tetapi memburukkan 5% terburuk.
5. **KAGI-R (Kagi tutup)**
   - R = k × ATR14(t0−1), k ∈ {3, 4, 5} (dibeku). Garis naik meneruskan selagi tutup naik; pusingan apabila tutup turun ≥ R dari ekstrem semasa.
   - Keluar A: pusingan pertama (= trailing jarak tetap; hampir sama Chandelier 4×ATR dengan ATR dibeku — kawalan ATR dibeku lawan bergerak).
   - Keluar B (yin): tutup < "pinggang" (rendah pusingan sebelumnya) — iaitu pecah rendah ayunan terakhir yang disahkan oleh balikan ≥ R.
6. **LB-N (Line Break tutup)**
   - Garis putih baharu bila C > atas garis terakhir; garis hitam (balikan) bila C < bawah terendah N garis putih terakhir; N ∈ {3, 4, 5}; tiada parameter saiz.
   - Keluar: garis hitam pertama selepas beli. Bermula dengan garis pertama = tutup t0 (jika < N garis wujud, guna semua yang ada; varian: tambah henti awal = harga beli − 4×ATR14 sehingga N garis wujud).
   - Risiko diketahui: dalam aliran merangkak (banyak tutup baharu kecil), paras balikan sangat dekat → whipsaw; dalam lonjakan jurang, paras sangat jauh.
7. **Pengesahan (untuk semua)**: varian "2 tutup berturut di bawah paras" sebelum jual — mengurangkan whipsaw dengan kos 1 hari lag; uji hanya pada 1–2 calon terbaik untuk elak ledakan grid.
8. **Tidak disyorkan**: range bar (perlu data intrahari); HA mentah 1 bar (sudah setara peraturan lama terlemah); grid parameter penuh (risiko lebih-padan — hadkan ≤ ~20 varian, pilih menggunakan tahun 2019–2023, sahkan pada 2024–2026 dan pada S1–S4/AUTOTUNE seperti Papan Penganalisis).
9. **Kriteria lulus cadangan** (berpandukan pilihan lorong 2): mengatasi Chandelier tutup 4×ATR14 pada lebihan SPY/bulan DAN tidak lebih buruk > 1 mata peratus pada 5% terburuk, dalam ≥ 2/3 tahun masuk dan apabila 2020 & 2025 dikecualikan; jika tidak, kekalkan Chandelier dan rekod "tidak mengatasi".

### Gaps
- Parameter "disyorkan" di atas adalah reka bentuk berdasarkan definisi dan panduan pengamal (NAGA, Line Break lalai N=3), bukan nilai yang terbukti optimum dalam mana-mana kajian; tiada sumber memberi parameter optimum bagi keluar swing saham.
- Ambang Pastukhov (H-volatiliti relatif kepada H, cth. nisbah 2 bagi jalan rawak) yang boleh menjadi diagnostik murah "adakah keluar Renko/Kagi ikut aliran sesuai untuk saham ini" tidak dapat disahkan daripada sumber dalam sesi ini (abstrak berbayar); jika diperlukan, dapatkan teks penuh Pastukhov (2004) atau dokumentasi Hudson & Thames.
