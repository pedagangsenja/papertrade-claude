# Candle-shape and alternative-chart features as FILTERS / RANKING keys for long swing candidates (US stocks, daily OHLCV)

Research note, 22 Oct 2026. Method note: web search only. Direct fetches of full-text PDFs (LSE, Yale, Invesco, BSIC) were blocked by the session proxy, so most numbers below come from abstracts, publisher pages and secondary write-ups returned by search. Each claim says which. Nothing here has been backtested on our data yet.

## Q1. Evidence for bar-shape features in return prediction (CLV, body/shadow, overnight vs intraday split, range volatility, strong close, gaps, high-volume days, 52-week high)

### Takeaway
The strongest peer-reviewed evidence is for **decomposing returns into overnight (prior close→open) and intraday (open→close)**, for **52-week-high proximity**, for **abnormal volume** (high-volume return premium) and for **avoiding extreme single-day winners (MAX effect)**. Single-bar shape features (CLV / internal bar strength, body/shadow ratios, candlestick patterns) have little rigorous support as continuation signals. Where they do show up, they work as **1-day mean-reversion** signals (close near the low leads to a bounce), which is the opposite of the "strong close" idea and too short for a 3–30 day hold. The best formal evidence that bar shape carries information is the CNN-on-OHLC-images work (Jiang, Kelly & Xiu 2023). The edge it finds is concentrated in small stocks and weakens sharply in large caps.

### Cited Findings

**Overnight vs intraday decomposition**
- Lou, Polk & Skouras, "A tug of war: overnight versus intraday expected returns," *JFE* 2019. Abnormal momentum returns are earned almost entirely **overnight**, while most other anomalies earn their profits **intraday**. Across 14 strategies, profits come either entirely overnight (reversal and several momentum variants) or entirely intraday, usually with opposite-signed components. The pattern is stronger in large-cap and high-price stocks. The authors attribute it to clientele: institutions trade intraday and against momentum, while individuals trade more at the open. Variation in the overnight–intraday spread is about 2% per month when momentum-trading activity is low or institutions need to rebalance. Sources: [LSE Research Online](https://researchonline.lse.ac.uk/id/eprint/119010), [NBER conf. version](https://conference.nber.org/conf_papers/f78239/f78239.pdf), [Alpha Architect summary](https://alphaarchitect.com/2015/02/overnight-momentum-vs-intraday-momentum/) (abstract-level; full text not fetched).
- Barardehi, Bogousslavsky & Muravyev, "What Drives Momentum and Reversal? Evidence from Day and Night Signals" (SSRN 2022; later *RFS*). They split past returns into intraday and overnight parts over 1926–2019. News mostly drives overnight returns, while investor trading mostly drives intraday returns. Portfolios formed on **past intraday returns** show momentum without long-term reversal. Portfolios formed on **past overnight returns** show no momentum (published wording) and only long-term reversal. The working-paper and published summaries word this differently (the WP also mentions short-term reversal for intraday-formed portfolios). Sources: [ResearchGate WP](https://www.researchgate.net/publication/365627693_What_Drives_Momentum_and_Reversal_Evidence_from_Day_and_Night_Signals), [Illinois Experts](https://experts.illinois.edu/en/publications/what-drives-momentum-and-reversal-evidence-from-day-and-night-sig/), [Wharton Jacobs Levy PDF](https://jacobslevycenter.wharton.upenn.edu/wp-content/uploads/2022/09/Bogousslavsky.pdf), [CXO summary](https://www.cxoadvisory.com/momentum-investing/intraday-and-overnight-return-momentum-and-reversal-signals/).
- Aboody, Even-Tov, Lehavy & Trueman, "Overnight Returns and Firm-Specific Investor Sentiment," *JFQA* 2018. Overnight returns persist in the short term (press releases say up to about 12 weeks), more strongly for hard-to-value firms. High-overnight-return stocks then **underperform over longer horizons**, consistent with temporary sentiment mispricing. Sources disagree on the sample end: Berkeley/UCLA say 1992–2013, Michigan says 1992–2015. Sources: [JFQA PDF via UCLA](https://anderson-review.ucla.edu/wp-content/uploads/2021/03/Aboody-et-al_overnight_returns_and_firmspecific_investor_sentiment_JFQA2018.pdf), [IDEAS](https://ideas.repec.org/a/cup/jfinqa/v53y2018i02p485-505_00.html), [Berkeley Haas](https://newsroom.haas.berkeley.edu/how-after-hours-trading-sheds-light-investor-sentiment/), [UCLA brief](https://anderson-review.ucla.edu/overnight-returns).
- Berkman, Koch, Tuttle & Zhang, "Paying Attention: Overnight Returns and the Hidden Cost of Buying at the Open," *JFQA* 2012 (3,000 largest US stocks, 1996–2008). For high-attention stocks, positive overnight returns are followed by intraday reversal because the **open is high relative to intraday prices**. The effect is strongest when retail attention is high, for hard-to-value or costly-to-arbitrage stocks, and in high-sentiment periods. The implicit cost to retail buyers at the open often exceeds the effective half-spread. Sources: [IDEAS](https://ideas.repec.org/a/cup/jfinqa/v47y2012i04p715-741_00.html), [KU ScholarWorks PDF](https://kuscholarworks.ku.edu/bitstream/1808/10965/1/Koch_Paying%20Attention.pdf).

**Close location / internal bar strength (IBS = CLV in 0–1 form)**
- No peer-reviewed study was found that tests close-position-in-range as a **cross-sectional continuation** predictor for individual US stocks. Searches turned up only practitioner claims without tests. LuxAlgo explicitly says open and close levels do not predict the next move on their own. Sources: [search summary incl. LuxAlgo](https://www.luxalgo.com/blog/daily-open-and-close-essential-metrics/), [QuantVPS](https://www.quantvps.com/blog/daily-open-and-close).
- Pagonidis, "The IBS Effect: Mean Reversion in Equity ETFs" (NAAIM, data to May 2013). IBS = (C−L)/(H−L). A **low** IBS is followed by **higher** next-day close-to-close returns, and a high IBS by lower ones. Secondary sources cite +0.35% after IBS<0.2 and −0.13% after IBS>0.8 (not checked against the original). The effect is stronger in volatile markets and, for US index ETFs, appears only on high-volume days. Sources: [NAAIM PDF](https://www.naaim.org/wp-content/uploads/2014/04/00V_Alexander_Pagonidis_The-IBS-Effect-Mean-Reversion-in-Equity-ETFs-1.pdf), [ResearchGate](https://www.researchgate.net/publication/256065291_The_IBS_Effect_Daily_Mean_Reversion_of_Equity_Indices), [TA-Lib IBS definition](https://ta-lib.org/functions/ibs.html).
- Replication is mixed. Pandey & Joshi (arXiv 2023, country ETFs) find IBS a strong predictor of next-day returns. A StockViz 2016 backtest found trading IBS mean reversion a losing proposition. Sources: [arXiv 2306.12434](https://arxiv.org/pdf/2306.12434), [StockViz](https://stockviz.biz/2016/06/22/internal-bar-strength/), [Kinlay blog](https://jonathankinlay.com/2019/07/the-internal-bar-strength-indicator/) (blog).
- Related close-price microstructure: stocks closing just **above a round number** outperform those just below by about 24.6 bp the next day, attributed to limit-order clustering (Zhang, SSRN). This is a 1-day effect. Source: [SSRN 4718961](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4718961).

**Candlestick patterns (body/shadow based)**
- Marshall, Young & Rose (DJIA stocks, 1992–2002, 28 candlestick signals, 10-day hold) found candlestick strategies **generally unprofitable** for large US stocks. Bullish single-day signals were followed by gains less than half the time, and no bullish signal reliably predicted abnormal positive returns. The authors suggest the patterns might complement other timing methods. Sources: [paper PDF mirror](https://c.mql5.com/forextsd/forum/211/Market%20Timing%20with%20Candlestick%20Technical%20Analysis.pdf), [CXO "Candlesticks or fiddlesticks"](https://www.cxoadvisory.com/technical-trading/candlesticks-fiddlesticks/). Evidence is pre-2003 and large-cap only.
- Results depend on the exit rule: on Dow stocks, three-day reversal patterns were profitable under the Caginalp-Laurent holding rule but not under the Marshall-Young-Rose rule after costs and data-snooping adjustment. Source: [IDEAS revfin 2012](https://ideas.repec.org/a/eee/revfin/v21y2012i2p63-68.html).

**Learned OHLC-shape information (CNN on chart images)**
- Jiang, Kelly & Xiu, "(Re-)Imag(in)ing Price Trends," *JF* 78(6) 2023. A CNN trained on images of daily OHLC bars plus moving average and volume (5/20/60-day windows) predicts the direction of future returns. Training covers 1993–2000 and the out-of-sample test 2001–2019 (per BSIC). Reported long-short Sharpe ratios are about 7.2 / 6.8 / 4.9 for the 5/20/60-day models, falling to **slightly above 1 when restricted to the 500 largest stocks**. These figures come from a secondary blog and were not checked against the paper. The authors report robustness to transaction costs and transfer to international markets. Sources: [Yale-hosted JF PDF](https://economics.yale.edu/sites/default/files/2023-11/The%20Journal%20of%20Finance%20-%202023%20-%20JIANG%20-%20Re%25E2%2580%2590%20Imag%20in%20ing%20Price%20Trends_0.pdf) (not fetched), [BSIC summary](https://bsic.it/technical-analysis-on-steroids/), [Semantic Scholar](https://www.semanticscholar.org/paper/(Re-)Imag(in)ing-Price-Trends-Jiang-Kelly/3484a4929dd82cff5a903ea7ca912c1ddac174cb).
- A saliency-map study found the CNN concentrates on **closing prices near the daily high/low extremes in the most recent days**, with volume spikes as secondary cues. This suggests close location carries information only in combination with other features, and its sign was not established here. Source: [Guan, Li & Si, SSRN 6389479](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6389479).
- An independent open-source replication on R1000/ETFs reports very weak out-of-sample power (test AUC about 0.507). Source: [GitHub ArjunDivecha/Pattern](https://github.com/ArjunDivecha/Pattern) (unreviewed).

**Volume, extreme days, 52-week high**
- Gervais, Kaniel & Mingelgrin, "The High-Volume Return Premium," *JF* 2001 (CRSP 1963–1996). Stocks with unusually **high volume** over a day or week (top 10% of the last 50 days' volume) **rise over the following month**, and unusually low-volume stocks fall. The proposed mechanism is visibility. Returns autocorrelation, announcements, risk and liquidity do not explain it. The premium is found in almost all developed markets (Kaniel, Li & Starks), and a 2021 *JFE* paper finds it is not explained by factor models. Sources: [Wiley](https://onlinelibrary.wiley.com/doi/abs/10.1111/0022-1082.00349), [Duke page](https://sites.duke.edu/sgervais/research/gervais-kaniel-mingelgrin-2001/), [Kaniel-Li-Starks SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=474100), [JFE 2021](https://ideas.repec.org/a/eee/jfinec/v140y2021i1p325-345.html), [replication report](https://dmurav.com/replications/releases/v2026-09-06/reports/paper-c87efbd9bcc6.pdf) (conclusions not seen). Pre-2000 core sample.
- Bali, Cakici & Whitelaw, "Maxing Out," *JFE* 2011. Stocks with a high **maximum daily return over the prior month (MAX)** earn **lower** returns the next month. The Fama-MacBeth slope on MAX is −0.090 (t = −6.22) after controlling for MIN, IVOL, beta, size, B/M, momentum, short-term reversal and liquidity. Momentum and reversal partly but not fully explain it. Gorman et al. argue it is generic overreaction to extreme gains rather than lottery demand. Fong & Toh link it to sentiment using more recent data. Sources: [JFE PDF](https://pages.stern.nyu.edu/~rwhitela/papers/max%20jfe11.pdf), [NBER WP](https://www.nber.org/system/files/working_papers/w14804/w14804.pdf), [Gorman et al. CFR](https://cfr.ivo-welch.info/published/papers/gorman2021could.pdf), [Fong & Toh](https://www.researchgate.net/publication/262770549_Investor_Sentiment_and_the_MAX_Effect). A 2025 paper reports a "surprising" MAX × momentum interaction, but the snippet does not say in which direction: [Tandfonline 2025](https://www.tandfonline.com/doi/full/10.1080/15427560.2025.2580935).
- George & Hwang, *JF* 2004. Nearness to the 52-week high explains a large part of momentum profits, and its forecasts **do not reverse long-run**. Source: [summary](https://academicnewsletter.sufe.edu.cn/info/361244). Hong, Jordan & Liu (*PBFJ* 2015, 1963–2009) find the effect is driven mainly by **industry** 52-week-high nearness (0.46%/month vs 0.32% for the idiosyncratic version; another summary says 0.60%). It survives controls for stock and industry momentum and is attributed to anchoring. Sources: [UKY PDF](https://gattonweb.uky.edu/faculty/lium/52weekhigh.pdf), [ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0927538X15000347). Internationally, 10 of 20 markets show significant 52-week-high momentum profits that do not reverse (Liu, Liu & Ma 2011): [SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1364566). Du (2008) finds momentum and reversal co-exist in international indexes, which disputes George–Hwang's claim that 52-week-high profits do not reverse: [NAU](https://experts.nau.edu/en/publications/the-52-week-high-and-momentum-investing-in-international-stock-in/).

**Range-based volatility**
- Range estimators are statistically more efficient than close-to-close: Parkinson about 2.5–5×, Garman–Klass about 7.4×. Parkinson and GK assume zero drift and overstate variance when drift is large. Rogers–Satchell handles drift, and only Yang–Zhang handles opening jumps. Bali & Weinbaum (2005) rank GK best. Sources: [Molnár, core.ac.uk](https://core.ac.uk/download/pdf/30793839.pdf), [PortfolioOptimizer](https://portfoliooptimizer.io/blog/range-based-volatility-estimators-overview-and-examples-of-usage/), [R. O'Connell](https://ryanoconnellfinance.com/historical-volatility-estimators/).
- No source was found that tests a range-based volatility measure as a **cross-sectional return anomaly** (as opposed to a volatility forecaster). See Gaps.

### Inferences
- **Execution matters more than shape for us.** We buy at the next open. Lou–Polk–Skouras and Berkman et al. imply that momentum-type candidates earn their premium overnight, and that high-attention names (large up day, gap, news) tend to open rich and fade intraday. Buying at the open after a high-attention day is therefore structurally expensive. A filter that **penalises a large expected gap** or a large signal-day overnight return (high attention) may improve fills more than any shape rule.
- **Intraday-formed vs overnight-formed momentum.** Barardehi et al. suggest the persistent part of momentum comes from **intraday** price moves, which reflect trading pressure, while overnight-driven gains (news) carry no momentum and may reverse long-run (Aboody et al.). That gives a candidate **rank-modifier that is not plain RS**: the share of the stock's 20–60 day return earned intraday.
- **Close location is most likely a short-horizon reversal feature, not a quality filter.** The rigorous-ish evidence (IBS) points to mean reversion at 1-day horizons in ETFs. For a buy-next-open, 3–30 day hold, a "strong close" filter is unlikely to add much and could slightly worsen the entry price, since a close at the high is followed by a weaker next day on average. Treat it as **testable, not established**.
- **Avoid extreme single-day spikes.** MAX and Berkman et al. both say that buying right after an extreme up day is a negative. This is directly usable as a veto, for example rejecting candidates whose signal-day return is in the top percentile of their own 1-year distribution, or whose 20-day MAX is in the top cross-sectional decile.
- **Abnormal volume on an up day is the best-supported "positive" bar feature** (high-volume return premium, 1-month horizon, which matches our hold). The core evidence is pre-2000, so it must be re-tested.

### Gaps
- No full-text verification of Lou–Polk–Skouras or Jiang–Kelly–Xiu tables (fetch blocked). Monthly overnight/intraday magnitudes per strategy are not recorded here.
- No peer-reviewed cross-sectional test of CLV, body/range or shadow ratios as **continuation** predictors for US single stocks at 1–30 day horizons.
- No source found on **gap-up continuation** for single US stocks outside earnings contexts. Evidence on "strong close" effects from Quantified Strategies / Oxfordstrat was not retrieved.
- No source on range-based (Parkinson/GK/RS) volatility as a cross-sectional anomaly. The idiosyncratic-volatility puzzle (Ang et al. 2006) was not retrieved in this session.
- 52-week-high evidence after 2010 for US stocks was not confirmed.

## Q2. Heikin-Ashi / Renko / P&F / Kagi state as trend-quality filter; Dorsey Wright P&F relative strength and DWA indexes / PDP

### Takeaway
There is **no peer-reviewed evidence** that Heikin-Ashi, Renko, Kagi or P&F *chart states* add predictive power for US stocks. The available material is practitioner backtests and marketing. Dorsey Wright's P&F relative-strength approach is in effect a **noise-filtered relative-strength momentum ranking**. Its live record (PDP since March 2007) is momentum-like: strong in trends, with deep drawdowns (−46% in 2008, −24% in 2022). No period-matched comparison showing persistent outperformance versus the S&P 500 was found.

### Cited Findings
- Heikin-Ashi definition: HA_close = (O+H+L+C)/4; HA_open = (prev HA_open + prev HA_close)/2; HA_high = max(H, HA_open, HA_close); HA_low = min(L, HA_open, HA_close). Source: [Wikipedia](https://en.wikipedia.org/wiki/Heikin-Ashi_chart).
- No peer-reviewed journal study tests Heikin-Ashi or Renko performance on stocks. One AfricArXiv/OSF preprint (Tchoudi 2022) claims Heikin-Ashi has lower entropy (less noise) than raw prices across 10 stocks. That is unverified and not a return test. Sources: [Liberated Stock Trader](https://www.liberatedstocktrader.com/heikin-ashi-candles/) (blog), search summary.
- Quantified Strategies' HA trend-following backtest on a US index since 1960 reports 85 trades and a 29% max drawdown versus 52.56% for buy-and-hold, but a **lower** annual return than buy-and-hold. Source: [Quantified Strategies](https://www.quantifiedstrategies.com/heikin-ashi-trading-strategy/) (practitioner). The BJF write-up warns about inflated naive HA backtests. Source: [BJF](https://bjftradinggroup.com/heikin-ashi-trading-strategy/).
- Dorsey Wright relative strength: divide the security price by the benchmark price, multiply by 100, and plot on a P&F chart. The default box size is **6.5% for stocks**. Source: [Nasdaq Dorsey Wright – Relative Strength Basics](https://nasdaqdorseywright.zendesk.com/hc/en-us/articles/15938757529869-Relative-Strength-Basics), [DWA P&F Basics PDF](https://www.nasdaq.com/docs/DWA-Point-Figure-Basics_0.pdf).
- The DWA "Technical Attribute" / matrix ranking builds a P&F RS chart for **every pair** of symbols in a universe and aggregates the pairwise buy signals into a rank. Source: [DWA Technical Attribute ranking PDF](https://sageadv.net/wp-content/uploads/2022/11/Technical-Attribute-Stock-Ranking-System.pdf). It was not confirmed that this exact mechanism drives the Technical Leaders (DWTL) selection.
- DWTL index: about 100 US stocks with strong relative strength, rebalanced and reconstituted quarterly. The official methodology weights constituents by a proprietary relative strength score with a 5%/25% concentration cap. Sources: [Nasdaq methodology](https://indexes.nasdaqomx.com/docs/Methodology_DorseyWrightTechnicalIndexes.pdf), [Nasdaq DWTL overview](https://indexes.nasdaq.com/Index/Overview/DWTL), [Nasdaq article 2018](https://www.nasdaq.com/articles/dorsey-wright-technical-leaders-index-2018-07-18).
- Performance snapshots (all point-in-time, none period-matched):
  - Nasdaq research note: DWTL TR +10.28% YTD to 21 Jun 2018 vs +3.81% for SPXTR, about 1% ahead of MSCI USA Momentum. Source: [DWTL 2018 Research](https://indexes.nasdaqomx.com/docs/DWTL%202018%20Research.pdf) (index provider, marketing context).
  - DWTL TR fact sheet: +31.21% 1-year and +21.48% in calendar 2023 (as of 28 Mar 2024). Source: [FS_DWTLTR](https://indexes.NASDAQomx.com/docs/FS_DWTLTR.pdf). For comparison, the S&P 500 returned about 26% in 2023 (general knowledge, not from a retrieved source).
  - PDP (inception 1 Mar 2007): Yahoo lists 5-year 11.43% vs 10.16% and 10-year 14.01% vs 15.87% as of 9 Jul 2026. The comparison column appears to be the Large Growth category, not the S&P 500. Calendar returns: −46.21% in 2008 and −24.49% in 2022. Sources: [Yahoo PDP performance](https://finance.yahoo.com/quote/PDP/performance/), [ETFdb](https://etfdb.com/etf/PDP/).
  - PDP tracking difference vs its index: −0.92% (period not stated). Source: [P&I](https://etf.pionline.com/fund/PDP).
- Older practitioner test: Moody & Parker (*Stocks & Commodities*, 1993) tested Chartcraft P&F RS buy/sell signals; results were not visible. Fidelity has a practitioner document on P&F pattern tests. Sources: [Traders.com](https://store.traders.com/-v11-c02-pointfi-pdf.html), [Fidelity PDF](https://www.fidelity.com/bin-public/060_www_fidelity_com/documents/TestingPointFigure.pdf).

### Inferences
- Alternative charts are **deterministic smoothers / denoisers of the same price path**. HA is roughly a 2-bar EMA of the OHLC average. Renko and P&F are path filters with a box threshold. Kagi is a reversal-threshold line. They cannot contain information beyond OHLC, and P&F/Renko/Kagi even discard time and volume. Their potential value is as a **robust trend-state indicator** that is less whipsawed than a moving-average cross, not as new information.
- DWA P&F RS is a **relative-strength momentum ranking** with hysteresis (3-box reversal at 6.5%). Our market-wide RS rating already captures most of this. PDP's record (deep 2008/2022 drawdowns, roughly in line with growth/momentum peers) is consistent with plain momentum exposure rather than a separate P&F alpha.
- The most plausible use for us is the **hysteresis** idea. A candidate whose RS line versus SPY (or versus its sector) is in a P&F "column of Xs" with a recent RS buy signal is in a confirmed relative uptrend. That can be tested as a tie-breaker inside an RS bucket. Expect it to be highly correlated with RS rank.

### Gaps
- No independent, period-matched since-inception PDP vs S&P 500 TR figure; Invesco's site could not be fetched. The SEC N-CSR filings for Invesco ETF Trust contain these numbers but were not opened: [N-CSR FY2022](https://www.sec.gov/Archives/edgar/data/1209466/000119312522188419/d331661dncsr.htm).
- No academic test of Renko, Kagi or HA consecutive-bar counts as cross-sectional filters.
- The exact DWTL selection rule (pairwise matrix vs single RS score) is unconfirmed.

## Q3. How candle features interact with momentum / relative-strength ranking

### Takeaway
The best-documented interactions are: (i) **momentum premium is earned overnight while intraday pressure fights it**, so buy-at-open execution is the weak point; (ii) **52-week-high nearness, especially at industry level, adds to or partly subsumes momentum**, and it complements our sector/industry grade; (iii) **extreme recent up days (MAX) and high-attention gaps hurt subsequent returns even among momentum stocks**; (iv) **intraday-formed momentum persists while overnight-formed momentum does not**.

### Cited Findings
- Momentum profits are earned overnight and partly reversed intraday. The overnight–intraday split varies by about 2% per month with institutional rebalancing pressure and momentum-trading activity. Source: [Lou, Polk & Skouras (LSE)](https://researchonline.lse.ac.uk/id/eprint/119010).
- Portfolios formed on past intraday returns show momentum without long-term reversal, while overnight-formed portfolios show none. Source: [Barardehi et al. (Illinois Experts)](https://experts.illinois.edu/en/publications/what-drives-momentum-and-reversal-evidence-from-day-and-night-sig/).
- The 52-week high explains a large part of momentum profits and does not reverse (George & Hwang 2004): [summary](https://academicnewsletter.sufe.edu.cn/info/361244). The industry version beats the stock-level version and survives momentum controls: [Hong, Jordan & Liu](https://gattonweb.uky.edu/faculty/lium/52weekhigh.pdf).
- The MAX effect survives controls for momentum and short-term reversal, which only partly explain it: [Bali, Cakici & Whitelaw](https://pages.stern.nyu.edu/~rwhitela/papers/max%20jfe11.pdf).
- High-attention stocks, whose overnight return is followed by intraday reversal, are concentrated in hard-to-value names and high-sentiment periods: [Berkman et al.](https://ideas.repec.org/a/cup/jfinqa/v47y2012i04p715-741_00.html).
- The CNN image signal is reported as distinct from standard short-term momentum/reversal, with a higher Sharpe ratio. Source: [Semantic Scholar abstract](https://www.semanticscholar.org/paper/(Re-)Imag(in)ing-Price-Trends-Jiang-Kelly/3484a4929dd82cff5a903ea7ca912c1ddac174cb), [arXiv 2408.08483](https://arxiv.org/html/2408.08483v1).

### Inferences
- **Features most likely to add information beyond RS + sector grade**, in priority order:
  1. intraday share of trend (intraday vs overnight decomposition)
  2. signal-day attention/gap veto (overnight return or gap size relative to ATR)
  3. MAX veto
  4. abnormal volume on up days
  5. 52-week-high nearness at stock and industry level. This is partly redundant with RS but has the documented "no long-run reversal" property and is anchor-based rather than return-based.
- **Features likely redundant with RS:** HA/Renko/P&F trend state, DWA P&F RS, and consecutive-up-bar counts.
- **Features with weak or contrary evidence:** strong close / high CLV and bullish candlestick patterns.

### Gaps
- No study found that tests candle-shape filters **conditional on already being in the top RS decile**. This has to be tested in-house.
- No evidence on Shariah-screened universes specifically. Shariah screens tilt away from financials and high-leverage firms, which may change attention and volume dynamics; this is untested.

## Q4. Exact formulas and suggested parameters to test as a filter layer (all computable from daily OHLCV)

### Takeaway
Below is a ready-to-code feature set: formulas from standard definitions, parameter ranges from the literature where available, and otherwise our own proposals (marked "proposed"). Each feature should be tested as (a) a hard veto and (b) a tie-break rank within an existing buy signal. The outcome to measure is the 3–30 day forward return from the **next open**, plus the hit rate for reaching +10%.

### Cited Findings
- IBS / close location: IBS = (C−L)/(H−L), with literature thresholds at 0.2 and 0.8. CLV = ((C−L)−(H−C))/(H−L) = 2·IBS−1. Source: [TA-Lib IBS](https://ta-lib.org/functions/ibs.html), [Pagonidis NAAIM](https://www.naaim.org/wp-content/uploads/2014/04/00V_Alexander_Pagonidis_The-IBS-Effect-Mean-Reversion-in-Equity-ETFs-1.pdf).
- Range estimators are listed below (Parkinson, Garman–Klass, Rogers–Satchell). Sources: [PortfolioOptimizer](https://portfoliooptimizer.io/blog/range-based-volatility-estimators-overview-and-examples-of-usage/), [Molnár](https://core.ac.uk/download/pdf/30793839.pdf).
- High-volume definition: formation-day volume in the top (bottom) 10% of the previous 50 daily volumes; horizon about 1 month. Source: [replication report spec](https://dmurav.com/replications/releases/v2026-09-06/reports/paper-c87efbd9bcc6.pdf), [GKM 2001](https://onlinelibrary.wiley.com/doi/abs/10.1111/0022-1082.00349).
- MAX: the maximum daily return over the prior month, used with a 1-month horizon. Source: [BCW 2011](https://pages.stern.nyu.edu/~rwhitela/papers/max%20jfe11.pdf).
- 52-week high ratio: P_t / max(P over 52 weeks). The industry version is computed from industry-level price/high ratios. Sources: [George & Hwang summary](https://academicnewsletter.sufe.edu.cn/info/361244), [Hong, Jordan & Liu](https://gattonweb.uky.edu/faculty/lium/52weekhigh.pdf).
- DWA RS for P&F: RS_t = 100·P_t / Bench_t, box 6.5%, 3-box reversal (standard DWA convention). Source: [DWA RS Basics](https://nasdaqdorseywright.zendesk.com/hc/en-us/articles/15938757529869-Relative-Strength-Basics).
- HA formulas: [Wikipedia](https://en.wikipedia.org/wiki/Heikin-Ashi_chart).

### Inferences: formula sheet (t = signal day; C_{t-1} = prior close; use adjusted OHLC consistently)

Basic bar decomposition
- `rng = H − L` (if rng = 0, set shape features to NaN; our `tidak_layak` illiquidity screen already rejects many zero-range bars)
- `IBS = (C − L)/rng`; `CLV = 2·IBS − 1`
- `body_ratio = |C − O| / rng`; `dir = sign(C − O)`
- `upper_shadow = (H − max(O,C)) / rng`; `lower_shadow = (min(O,C) − L) / rng` (body + upper + lower = 1)
- `r_on = ln(O_t / C_{t-1})` (overnight); `r_id = ln(C_t / O_t)` (intraday); `r_cc = r_on + r_id`
- `gap_atr = (O_t − C_{t-1}) / ATR14_{t-1}`
- `rng_atr = rng / ATR14_{t-1}` (range expansion)

Multi-day shape aggregates (proposed; these smooth out the noise of a single bar)
- `IBS_avg5 = mean(IBS, last 5 bars)`; `IBS_avg20`
- `ID_share_N = Σ r_id / (|Σ r_on| + |Σ r_id|)` over N ∈ {20, 60}, or simply `Σ r_id − Σ r_on` over N. This captures the intraday-formed vs overnight-formed momentum distinction from Barardehi et al. and Lou et al. Proposed: rank high-ID_share above high-overnight-share among equal-RS candidates.
- `ON_cum_N = Σ r_on` over N ∈ {5, 20}: a sentiment/attention proxy (Aboody et al.). Proposed: test both directions, short-term persistence vs longer reversal.
- `HA_bull_run` = number of consecutive HA bars with HA_close > HA_open and no lower HA shadow (HA_low = HA_open). Proposed values to test: ≥ 3 and ≥ 5.
- Renko state with ATR bricks: brick = ATR14 at entry, or the 14-day ATR fixed monthly; direction = last brick direction; `renko_run` = consecutive bricks up. Proposed: require the last 2 bricks up.
- P&F RS state (DWA style): build P&F on `RS = 100·C/SPY_close` (or vs sector ETF) with a 6.5% box (log-scaled boxes) and 3-box reversal. States: in X column (yes/no); last signal = buy (double-top break) or sell. Proposed tie-break: RS in Xs AND last RS signal = buy.

Volatility / range (range-based, daily; average over N = 20)
- Parkinson: `σ²_P = (1/(4 ln2)) · mean( ln(H/L)² )`
- Garman–Klass: `σ²_GK = mean( 0.5·ln(H/L)² − (2 ln2 − 1)·ln(C/O)² )`
- Rogers–Satchell (drift-robust): `σ²_RS = mean( ln(H/C)·ln(H/O) + ln(L/C)·ln(L/O) )`
- Yang–Zhang combines overnight variance, open-to-close variance and RS with weight k = 0.34/(1.34 + (N+1)/(N−1)). Use it when opening gaps are large, which matters because we buy at the open.
- Proposed uses: (a) normalise targets (+10% expressed as k·σ to judge feasibility in 1–4 weeks); (b) compare `vol_ratio = σ_RS,5 / σ_RS,60` for contraction-then-expansion setups; (c) **do not assume** low or high range-vol is an alpha signal, because no cross-sectional evidence was retrieved.

Attention / extreme-day vetoes (proposed parameters)
- `MAX20 = max(r_cc over last 20 days)`. Veto if in the top 10% cross-sectionally of the eligible universe (BCW decile logic).
- Signal-day spike veto: reject if `r_cc,t > 3·σ_RS,60·√1`, or if `gap_atr_{t}` is in the top percentile. Rationale: Berkman et al. (high open, intraday fade) and MAX.
- Expected next-open slippage cannot be known at the close. As a proxy, penalise candidates whose last 5 days show `ON_cum_5` in the top decile (retail-attention names).

Volume
- `vol_pctl50 = percentile rank of V_t within last 50 days` (GKM). Proposed positive feature: `vol_pctl50 ≥ 0.9 AND C > O AND IBS ≥ 0.5`, a high-volume up day. Test as a rank bonus with a 1-month horizon.
- `rvol = V_t / median(V, 50)`.

Anchor / context
- `H52_ratio = C_t / max(H over 252 days)` (G&H use close; a high-based version is a variant). Proposed filter: H52_ratio ≥ 0.85 (test 0.75 / 0.85 / 0.95). Industry version: median H52_ratio of the stock's industry members, used as an alternative or complement to the sector grade.

Suggested testing protocol (proposed)
1. Take existing buy signals (Lejar Penuh universe, all methods). For each feature, compute the conditional mean and trimmed mean of the forward 5/10/20-day return from the next open, and the probability of reaching +10% within 20 days, by feature quintile. Do this **within RS-rating terciles**, to measure information beyond RS.
2. Report the Spearman correlation of each feature with the RS rating and with the sector/industry grade, and drop features with |ρ| > 0.6 to RS.
3. Require monotonic quintiles, consistency across the S1–S4 / WFO splits, and n ≥ 10 distinct buy dates per cell, matching our "BELUM CUKUP" rule.
4. Report the overnight vs intraday split of realised trade P&L (entry at open), to see whether our edge is overnight-type (momentum) as Lou et al. would predict.

### Gaps
- Parameter values marked "proposed" have no literature backing for this specific use. They are starting grids only.
- Yang–Zhang constant k comes from the standard definition and was not checked against a retrieved source in this session.
- No source quantifies how many candidates a MAX or gap veto would remove in a momentum-selected universe. An in-house count is needed.
