# Sector rotation (11 GICS sectors, sector ETFs) and stacking market-regime, sector and industry filters on a stock-selection rule: measured evidence, US equities, as of November 2026

Method note (read first): in this session WebFetch could not reach quantpedia.com, cxoadvisory.com or acfr.aut.ac.nz (hosts outside the session's allowed network), so I stopped fetching pages. Every finding below comes from WebSearch result summaries of abstracts, working-paper PDFs, vendor pages and news pages. I did not read any table myself. Where the search tool did not say which of several result URLs a number came from, I say so. Numbers marked "(version-dependent)" differ between working-paper and published versions. Anything I only remember, without a source retrieved this session, is under Gaps, not Findings. Basic industry-momentum literature (Moskowitz and Grinblatt 1999, Asness-Porter-Stevens, Novy-Marx, Arnott et al., McLean and Pontiff, Mamaysky 2024) is already in `research_notes/Reka bentuk gred kekuatan industri/akademik_momentum_industri.md` and `akademik_leadlag_reversal.md`; it is cross-referenced here, not repeated.

---

## 1. Sector ETF relative-strength rotation: reported returns, drawdowns, turnover, and out-of-sample performance 2010–2026

### Takeaway
The headline backtest (Faber 2010, 1928–2009, no costs) looks strong, but every later test I found on real sector ETFs or live funds is weak: results are sensitive to the lookback, barely beat an equal-weight sector basket, and live relative-strength sector funds trailed the S&P 500 after 2010. Twelve-month sector momentum inside the S&P 500 is reported to have disappeared in 2010–2020.

### Cited Findings
**Faber (2010), "Relative Strength Strategies for Investing" (in-sample, gross of costs, long-only)**
- Data: ten value-weighted US industry portfolios (French-Fama), monthly, July 1926 – December 2009; tests start 1928 because one year is needed for ranking — [CXO Advisory summary](https://www.cxoadvisory.com/?p=5688); [Quantpedia strategy page](https://quantpedia.com/strategies/sector-momentum-rotational-system)
- Rule: hold the top X sectors (X from 1 to 9) equal-weighted; a sector is sold only when it drops out of the top X at the monthly rebalance — [StockCharts ChartSchool](https://chartschool.stockcharts.com/table-of-contents/trading-strategies-and-models/trading-strategies/fabers-sector-rotation-trading-strategy)
- Paper's own claim: relative-strength portfolios beat buy-and-hold in about 70% of all years; adding a trend-following hedge "decreases both volatility and drawdown" — [Quantpedia strategy page](https://quantpedia.com/strategies/sector-momentum-rotational-system); [SSRN 1585517 copy](https://www.scribd.com/doc/116882543/SSRN-id1585517)
- The trend hedge moves to cash when the S&P 500 is below its 10-month moving average; a secondary summary says the filtered version gives "slightly improved Sharpe ratios and similar absolute returns, but with marked reductions in drawdown" — [the7circles summary](https://the7circles.uk/?p=35490) (via search summary)
- The method "works on all of the measurement periods from one month to twelve months" (secondary summary) — [the7circles summary](https://the7circles.uk/?p=35490)
- Results exclude taxes, commissions and slippage — [SSRN 1585517 copy](https://www.scribd.com/doc/116882543/SSRN-id1585517) (via search summary)
- Quantpedia lists the sector version at 13.94% indicative annual return, 10 instruments, source-paper period 1928–2009; the search tool could not tell which top-N this is. Quantpedia's page also shows maximum drawdowns of -46.29% and -71.29% for two exhibits with different settings — [Quantpedia strategy page](https://quantpedia.com/strategies/sector-momentum-rotational-system); [Quantpedia screener](https://quantpedia.com/Screener/Details/3)

**Tests on real sector ETFs and funds (mostly after costs or with stated friction)**
- CXO Advisory, nine Select Sector SPDR ETFs, December 1998 – December 2015, 0.25% switching friction, long-only, monthly rotation to the top sector: erratic sensitivity to the ranking interval; the best interval (10 months) only modestly beats an equal-weighted sector benchmark. CXO's conclusion: the tests "offer little support" for a simple sector ETF momentum strategy — [CXO Advisory](https://www.cxoadvisory.com/momentum-investing/simple-sector-etf-momentum-strategy-robustnesssensitivity-tests/)
- CXO Advisory, "Jay's Pure Momentum" (top 5 of 39 Fidelity sector mutual funds by 240-day return, monthly, 2002–2015, long-only): 10.8% CAGR against 6.1% for SPY, but a lower Sharpe ratio than SPY; CXO attributes part of the edge to market timing, not sector selection — [CXO Advisory](https://cxoadvisory.com/momentum-investing/assessing-jays-pure-momentum-system)
- CXO Advisory, sector "alpha momentum" (sector ETFs, 1999–2014): long-only 5.5% against 2.0% for the S&P 500, but only five independent 3-year lookback intervals, and the long-short version did not work — [CXO Advisory](https://www.cxoadvisory.com/momentum-investing/sector-alpha-momentum-strategy/)
- CXO Advisory on style versus sector ETF momentum: both "offer little or no advantage relative to buying and holding IWB" (Russell 1000 ETF) — [CXO Advisory](https://www.cxoadvisory.com/momentum-investing/which-kind-of-etf-momentum-is-best) (via search summary; sample period not shown)
- Quantpedia, "How to Improve ETF Sector Momentum" (2024; nine Select Sector SPDRs, SPY benchmark, data 22 December 1998 – 5 September 2024): long-only sector momentum is more effective holding 4, 5 or 6 sectors than 1–3; varying the ranking period from 1 to 12 months "did not yield any beneficial results" in long-short tests. The numeric tables were not retrievable — [Quantpedia](https://quantpedia.com/how-to-improve-etf-sector-momentum/); [Elitetrader repost](https://elitetrader.com/et/threads/how-to-improve-etf-sector-momentum.381486)
- StockViz (blog, low weight): a simple momentum rotation over the sector SPDRs "worked before 2010 and stopped working after that" — [StockViz](https://stockviz.substack.com/p/rotating-spiders)

**Post-2010 evidence**
- Li and Turkington (State Street, "Mapping Momentum", summarised August 2021; S&P 500 stocks; latest sub-period 2010–2020; long-short): 12-month momentum at the sector and industry level "does not exist anymore", while one-month reversal at the sector/industry level intensified — [Quantpedia summary](https://quantpedia.com/an-important-analysis-of-stock-momentum-and-reversal-factors/); [IBKR repost](https://www.interactivebrokers.com/campus/ibkr-quant-news/an-important-analysis-of-stock-momentum-and-reversal-factors/)
- Live fund 1: First Trust Dorsey Wright Focus 5 ETF (FV; holds 5 First Trust sector/industry ETFs chosen by relative strength; launched 2014). Its index returned 10.72% a year since inception against 12.79% for the S&P 500, as of 31 March 2025 (index, before the fund's fee) — [First Trust fund page](https://www.ftportfolios.com/Retail/Etf/EtfSummary.aspx?Ticker=FV)
- FV 10-year return 9.58% a year against 10.79% for the S&P 500 (end date not shown); maximum drawdown 34.0% from 2014 through June 2026; expense ratio 0.89% — fund-data pages returned by the search (the tool did not say which page gave which figure; candidates: [PortfoliosLab](https://portfolioslab.com/symbol/FV), [YCharts](https://ycharts.com/companies/FV/annualized_daily_ten_year_total_return), [MyPlanIQ](https://ns2.myplaniq.com/invest/quote/FV/))
- Live fund 2: Molchanov and Stangl open their paper with a sector-rotation mutual fund (NAVFX) that underperformed the S&P 500 since 2010 by about 8.1% a year in one version of the paper and by about 4.9 points (7.34% against 12.23%) in another (version-dependent) — [Massey repository PDF](https://mro.massey.ac.nz/server/api/core/bitstreams/30b85d2d-90a8-4a38-bbac-acf85540dfa0/content); [Massey repository record](https://mro.massey.ac.nz/items/ccadcb8d-2658-456b-9aab-4ba840fba845)
- Newfound Research (Corey Hoffstein, c. 2018–2019; long-short, post-1944 focus, French-Fama industries): sector rotation is "entirely subsumed by the momentum factor"; the 10-sector version was profitable over about 90 years but "dramatically underperformed" single-stock momentum; it held up better in the 2008–2009 momentum crash — [Advisor Analyst repost 1](https://advisoranalyst.com/?p=89173)
- Newfound follow-up: no evidence that risk-adjusted momentum helps a long-only sector rotation system; a top-three risk-adjusted portfolio returned about 2.75% with 11.30% volatility against 3.90% and 12.65% for plain momentum (long-short excess returns; period not shown) — [Advisor Analyst repost 2](https://advisoranalyst.com/?p=91231)
- Quantpedia (2026): trailing 252-day sector momentum on the nine sector SPDRs earns its spread mainly on the first trading day of the month; the long-short variant is reported at 5.99% a year with a 0.55 Sharpe ratio — [Quantpedia](https://quantpedia.com/sectoral-intramonth-momentum-cycle/) (via search summary; costs and period not shown)

### Inferences
- The sequence is the usual one for a published anomaly: a long no-cost backtest on index portfolios (1928–2009), followed by weak and parameter-sensitive results on tradable ETFs (1998–2015, 1998–2024) and by live funds that trailed the S&P 500 after 2010. I found no source showing sector relative-strength rotation beating the S&P 500 net of costs from 2010 onward.
- Where sector rotation "worked" (Jay's system, Faber with the trend hedge), the authors or reviewers credit the market-timing layer for much of the gain. The sector layer alone gets little support.
- Sector rotation carries the same bet as stock momentum but weaker (Newfound). It should not be expected to add return on top of a stock-level momentum or trend rule; its documented benefit is a smaller momentum crash.
- Quantpedia's finding that 4–6 of 9 sectors is better than 1–3 means the "edge" grows as the portfolio approaches the equal-weight sector basket. That is evidence for diversification, not for picking the strongest sector.
- Part of the post-2010 shortfall of equal-weighted sector rotation against the cap-weighted S&P 500 is structural: the index itself became a concentrated technology bet (section 7), which any equal-weighted rotation among 9–11 sectors underweights. The fair benchmark for the sector layer is the equal-weight sector basket, and against it the measured edge is small.

### Gaps
- Faber's exact exhibit numbers (CAGR, volatility, maximum drawdown and turnover for top 1/2/3 sectors against buy-and-hold) were not retrievable; the paper is on SSRN (abstract 1585517) and cambriainvestments.com.
- I found no turnover figure for any sector rotation study in this session.
- Allocate Smartly, Alpha Architect, Robeco and Research Affiliates: the searches returned no sector-rotation-specific performance study from these firms. This is "not found in this session", not "does not exist".
- No source gave a clean 2010–2026 CAGR and drawdown for a fixed-rule sector ETF momentum strategy against SPY and against the equal-weight sector basket. The repo could compute this itself from the sector SPDR price history.
- Mamaysky (2024) reportedly still finds sector ETF winners beating losers for 3–24 month formation (see the earlier notes file); I did not re-check it here, and it conflicts in tone with Li and Turkington.

---

## 2. Business-cycle sector rotation (Stovall's model, Fidelity's business-cycle framework): what the evidence says

### Takeaway
The best academic test finds no systematic sector outperformance in the cycle stages where the popular model expects it. Even an investor who knew the cycle dates perfectly would have earned roughly 0.1–0.2% a month before costs, which disappears after costs and realistic timing errors.

### Cited Findings
- Molchanov and Stangl, "The Myth of Business Cycle Sector Rotation", International Journal of Finance and Economics (DOI 10.1002/ijfe.2882; online September 2023): no proof that sectors perform systematically in the business-cycle phases popular belief expects; "at best" modest outperformance that "quickly diminishes after allowing for transaction costs and incorrectly timing the business cycle"; robust to alternative sector and cycle definitions — [Massey repository record](https://mro.massey.ac.nz/items/ccadcb8d-2658-456b-9aab-4ba840fba845); [library record](https://bvbvf1.bib-bvb.de/vufind/PrimoRecord/cdi_proquest_journals_3116445404)
- Generalised test in the same paper (dropping the assumptions of any one rotation model): sector predictive power across cycle stages is not significantly different from random chance — [Massey repository PDF](https://mro.massey.ac.nz/server/api/core/bitstreams/30b85d2d-90a8-4a38-bbac-acf85540dfa0/content)
- Sample and size (version-dependent): an earlier version covers 10 NBER-dated cycles, 1948–2018, with a perfect-foresight risk-adjusted edge of about 0.11% a month before costs; the published version covers 15 cycles, 1948–2022, with 0.16% a month before costs — [Evidence Investor summary](https://www.evidenceinvestor.com/post/sector-rotation-foresight-myth); [Massey repository PDF](https://mro.massey.ac.nz/bitstreams/1f32a859-5ef9-442d-a5f8-ac8e0f5b1a83/download)
- In the published version, a simple market-timing rule (hold the market except during early recession) generates 0.18% outperformance, slightly more than the full perfect-foresight sector rotation — [Massey repository PDF](https://mro.massey.ac.nz/bitstreams/1f32a859-5ef9-442d-a5f8-ac8e0f5b1a83/download) (via search summary)
- Earlier related paper, Stangl, Jacobsen and Visaltanachoti, "Sector Rotation over Business Cycles" (US, 1948–2007): with perfect foresight and no costs, sector rotation generates at best 2.3% a year of outperformance; with trading frictions 1.1%–1.9% a year, statistically indistinguishable from zero — [CXO Advisory summary](https://www.cxoadvisory.com/economic-indicators/perfect-sector-rotation). Another source cites the figure as 2.01% for 1948–2006 (version-dependent) — [Massey repository PDF](https://mro.massey.ac.nz/server/api/core/bitstreams/30b85d2d-90a8-4a38-bbac-acf85540dfa0/content)
- Cycle staging in these papers splits NBER recessions (peak to trough) into two stages of equal length (stages IV–V) — [Scribd copy of "Sector Rotation over Business Cycles"](https://es.scribd.com/document/54155014/Sector-Rotation-Over-Business-Cycles) (via search summary)

### Inferences
- These are perfect-hindsight upper bounds. NBER dates are announced many months late, so a real investor does worse than 0.11–0.16% a month. Business-cycle sector rotation should be treated as measured empty for our purposes.
- The one layer that carried value in the same test was a market-state rule (stay out in early recession). This matches the repo's own result that the QQQ regime is a risk brake while sector selection is close to a coin toss.

### Gaps
- I did not retrieve Fidelity's own published hit-rates for its business-cycle framework or Sam Stovall's original tables, so I cannot compare their claims with the Molchanov-Stangl test number by number.
- Number of sectors/industries and the transaction-cost assumption in the published Molchanov-Stangl paper were not confirmed (one query suggested 48 industries; unverified).
- Publication year of the Stangl-Jacobsen-Visaltanachoti working paper was not confirmed (I recall about 2009).

---

## 3. Does sector/industry momentum depend on the market state?

### Takeaway
Yes. Stock momentum pays only after up markets and crashes in rebounds after bear markets, and the one US study specific to industries finds industry momentum profitable only after UP markets. Sources disagree on whether industry momentum has the same violent crash profile as stock momentum.

### Cited Findings
- Cooper, Gutierrez and Hameed (2004, Journal of Finance), US stocks, 1929–1995, long-short, gross: mean monthly momentum profit is +0.93% after positive market returns and -0.37% after negative market returns — [paper copy](https://typeset.io/pdf/market-states-and-momentum-4wtc7g4rqv.pdf)
- Their state definition: UP when the lagged three-year market return is positive, DOWN otherwise — [Waikato working paper describing the method](https://researchcommons.waikato.ac.nz/bitstream/10289/11238/5/IREF_accepted.pdf)
- Daniel and Moskowitz (2016, Journal of Financial Economics), US stocks, 1927–2013, long-short deciles, gross: crashes occur in "panic" states, after market declines and when volatility is high, together with a sharp market rebound — [NBER working paper 20439](https://www.nber.org/system/files/working_papers/w20439/w20439.pdf)
- Same paper: the two worst months are July and August 1932, when the past-loser decile returned 232%; in March–May 2009 the past-loser decile rose 163% while past winners gained 8% (an earlier draft says 156%; version-dependent) — [NBER working paper 20439](https://www.nber.org/system/files/working_papers/w20439/w20439.pdf); [Columbia draft](https://business.columbia.edu/sites/default/files-efs/pubfiles/4607/mom11.pdf)
- Same paper: after major declines loser-decile betas can exceed 3 while winner betas fall below 0.5, so bear-market momentum behaves "like written call options on the market" — [Alpha Architect summary](https://alphaarchitect.com/avoiding-momentum-crashes/); [Swedroe summary](https://www.etf.com/sections/index-investor-corner/swedroe-downside-momentum)
- Hühn (working paper, October 2015, FAU Erlangen-Nürnberg; US industry portfolios; long-short): industry momentum is "only profitable following UP markets"; no positive and significant risk-adjusted returns following DOWN markets, "regardless of market transitions" — [Hedge Fund Alpha abstract page](https://hedgefundalpha.com/strategies/industry-momentum-the-role-of-time-varying-factor-exposures-and-market-conditions/); [Quantpedia note](https://quantpedia.com/?p=628)
- Hühn also finds industry momentum has time-varying factor exposures (five-factor model); hedging them shrinks the outperformance and makes it insignificant for strategies based on recent past returns; and no link to market volatility or investor sentiment — [Hedge Fund Alpha abstract page](https://hedgefundalpha.com/strategies/industry-momentum-the-role-of-time-varying-factor-exposures-and-market-conditions/)
- Asem and Tian (2010): momentum profits are higher when the market stays in the same state and lower at transitions; a separate relative-strength study reports payoffs "substantially lower over transitions between states" — [Market Cycles and the Performance of Relative Strength Strategies](https://law-journals-books.vlex.com/vid/market-cycles-and-the-855584159) (via search summary)
- Grobys, Ruotsalainen and Äijö (2018, Quantitative Finance 18(10), 1715–1733), 49 French-Fama value-weighted industry portfolios, long-short, no costs: "neither plain industry momentum strategies nor the risk-managed industry momentum strategies are subject to optionality effects"; volatility scaling improves results across estimators and subsamples; the industry "echo effect" works only in the most recent subsample — [IDEAS record](https://ideas.repec.org/a/taf/quantf/v18y2018i10p1715-1733.html); cost caveat from [CXO Advisory](https://www.cxoadvisory.com/volatility-effects/suppressing-industry-momentum-strategy-crashes/)
- Conflict: Grobys et al. find no option-like crash behaviour in industry momentum, while Hühn reports industry momentum is "disrupted by periods of strong negative risk-adjusted returns" — [Hedge Fund Alpha abstract page](https://hedgefundalpha.com/strategies/industry-momentum-the-role-of-time-varying-factor-exposures-and-market-conditions/); contradicted in part by [Grobys et al.](https://ideas.repec.org/a/taf/quantf/v18y2018i10p1715-1733.html)
- Li and Turkington (2021, S&P 500): most one-month effects, reversal and momentum alike, "fail to generate reliable results of any kind when volatility is high" — [Quantpedia summary](https://quantpedia.com/an-important-analysis-of-stock-momentum-and-reversal-factors/)
- Non-US counter-example: in Moroccan industries momentum is present in both UP and DOWN markets (Gharaibeh et al., 2022, Cogent Business and Management) — [IDEAS record](https://ideas.repec.org/a/taf/oabmxx/v9y2022i1p2135217.html)

### Inferences
- The market state does not create a sector edge; it switches an existing (weak) relative-strength effect on and off. After down markets the expected value of "buy the strongest group" is about zero or negative, and at the turn from bear to rebound it is strongly negative for stock momentum.
- A regime filter therefore mostly removes the periods where relative strength hurts. That is a risk result (smaller drawdown), which is what the repo measured for the QQQ regime. The repo's finding that leadership advantage changes sign with the QQQ regime (12 of 17 years) agrees with Cooper et al. and Hühn.
- All the numbers in this section are long-short and gross. For a long-only book the crash comes from holding winners that lag a rebound, not from shorting losers, so the long-only damage is smaller than the long-short figures suggest; the winner leg in March–May 2009 still gained 8%.

### Gaps
- Hühn's actual monthly returns for UP and DOWN states were not retrievable (SSRN abstract 2653979); it is a working paper and I could not confirm formal publication.
- I found no study that conditions sector ETF rotation (11 GICS sectors) on market state using data through 2026.
- I found no long-only version of the state-dependence tests.

---

## 4. How much of a stock's return variance is explained by the market, sector and industry? Variation by industry

### Takeaway
For a typical US stock the market explains roughly one fifth of return variance and sector membership adds only a few percentage points; most variance is firm-specific. A few commodity-linked names are exceptions where the sector explains up to about a third.

### Cited Findings
- Roll (1988, Journal of Finance, "R²"): for large US stocks the average adjusted R² from systematic influences, same-industry returns and public firm news is "only about .35 with monthly data and .20 with daily data"; little relation between explanatory power and either firm size or industry — [Caltech repository abstract](https://resolver.caltech.edu/CaltechAUTHORS:20190426-145910927)
- Campbell, Lettau, Malkiel and Xu (2001, Journal of Finance 56(1), 1–43), US stocks, 1962–1997: volatility is split into market, industry and firm components without estimating betas; market and industry variances were "fairly stable", while firm-level variance more than doubled — [paper copy](https://personal.utdallas.edu/~yexiaoxu/clmx1_44.pdf); [RePEc record](https://econpapers.repec.org/RePEc:bla:jfinan:v:56:y:2001:i:1:p:1-43)
- Update by the same authors (NBER working paper 29916, April 2022; Critical Finance Review 2023), data through 2021: idiosyncratic volatility spiked in 1999–2000 and then declined; market, industry and idiosyncratic volatility all rose sharply in 2008–2009 and 2020–2021 — [NBER w29916](https://www.nber.org/papers/w29916); [RePEc record](https://econpapers.repec.org/RePEc:now:jnlcfr:104.00000128)
- Practitioner decomposition (US stocks, in-sample; period not shown): the market explains about 20% of return variance (median about 18%); sector factors measured on market residuals add a median of about 2.9% and a mean of about 4.2%; the single-stock maximum is about 34%, with Exxon Mobil and the energy sector given as the example of a large sector share — [Hedge Fund Alpha, "The explanatory power of sectors and style"](https://hedgefundalpha.com/stocks/the-explanatory-power-of-sectors-and-style/)
- Early studies (1960s–1970s data) put industry effects at roughly 10% of total variance, or 18–20% of residual variance, and later authors concluded King's original estimate was probably overstated — [Financial Decisions article](https://www.financialdecisionsonline.org/archive/pdffiles/v09n2/bae.pdf) (via search summary; the tool did not confirm which result URL carried this)

### Inferences
- If sector membership explains only about 3–4% of a typical stock's variance beyond the market, a sector or industry strength filter cannot move a stock rule's expected return much. It can still matter for portfolio risk, because that small common component is what makes several holdings in one industry fall together.
- The share is not uniform. In commodity-linked groups (energy; by extension gold miners) one external price drives the group, so two stocks from that group are close to one bet. This supports a per-industry cap as a risk control and argues against treating industry strength as a selection score, which is the repo's existing position.
- Common-factor variance rises in crises (2008–2009, 2020–2021), exactly when diversification across names is needed. A cap by industry is worth most in those periods.

### Gaps
- The exact split in Campbell et al. (2001) was not retrievable. From memory, unverified in this session: firm-level about 72%, market about 16%, industry about 12% of total variance over 1962–1997. Check Table/figures in the paper before quoting.
- I found no source giving the market/sector/industry R² separately for semiconductors, energy, gold miners or homebuilders. The repo can compute these directly from its price store (regress each stock on QQQ or SPUS, then on its industry average).
- Heston and Rouwenhorst (industry versus country effects) and newer risk-model decompositions (MSCI Barra, Axioma) were not retrieved.

---

## 5. Short-term reversal at the industry level (one week to one month) and lead-lag between industries, as reasons "buy the strongest group now" can fail

### Takeaway
Historically industries continued for one month while stocks reversed inside their industry; in 2010–2020 S&P 500 data the one-month effect at the sector/industry level is reported as reversal. The industry-leads-market result weakens after data revisions. Detail is in the earlier notes file `akademik_leadlag_reversal.md`.

### Cited Findings
- Hameed and Mian (2015, Journal of Financial and Quantitative Analysis 50, 89–117), US stocks, 1968–2010, long-short: an intra-industry reversal strategy earns about 0.97% a month risk-adjusted against 0.63% for the unconditional reversal — [IDEAS record](https://ideas.repec.org/a/cup/jfinqa/v50y2015i1-2p89-117_00.html); [Cambridge record](https://resolve.cambridge.org/core/journals/journal-of-financial-and-quantitative-analysis/article/industries-and-stock-return-reversals/92B5101FBEA7B40717D46DB60913BF41)
- Da, Liu and Schaumburg (working paper 2011, "Decomposing the Short-Term Return Reversal"): short-term reversal within industries, momentum across industries — cited in [Hameed and Mian working-paper copy](https://web2-bschool.nus.edu.sg/wp-content/uploads/media_rp/publications/BwXb81392625636.pdf)
- The conventional six-month industry momentum of Moskowitz and Grinblatt "concentrates in the first month" — [Georgia Southern paper record](https://digitalcommons.georgiasouthern.edu/finance-facpubs/5) (via search summary)
- Li and Turkington (2021; S&P 500 stocks; latest sub-period 2010–2020): "12-month momentum in industries does not exist anymore, but the opposite holds for a 1-month reversal"; the reversal "in industries or sectors is even more apparent" than in single stocks — [IBKR repost](https://www.interactivebrokers.com/campus/ibkr-quant-news/an-important-analysis-of-stock-momentum-and-reversal-factors/); [Quantpedia summary](https://quantpedia.com/an-important-analysis-of-stock-momentum-and-reversal-factors/)
- Hong, Torous and Valkanov (2007, Journal of Financial Economics 83(2), 367–396), 34 US industries: retail, services, commercial real estate, metal and petroleum lead the stock market by up to two months — [working-paper copy](https://escholarship.org/uc/item/6x49x543)
- Tse (2015, Journal of Empirical Finance 34, 195–203), same 34 industries, 1946–2002: the results are less significant after data revisions, with some evidence of predictability running from the market to industries; consistent with market efficiency — [IDEAS record](https://ideas.repec.org/a/eee/empfin/v34y2015icp195-203.html)
- An early summary of the Hong et al. result adds that the lead is "not economically significant for traders" — [CXO Advisory](https://www.cxoadvisory.com/economic-indicators/market-leading-industries) (via search summary)

### Inferences
- The sign of the one-month industry effect appears to have flipped between the 1963–1995 sample (continuation) and 2010–2020 (reversal). A rule that buys the group with the best recent 1–4 week return is, on the newest evidence, buying into a reversal.
- For a 10–15 session holding period the relevant horizon is exactly the one where the evidence is now negative or unstable. This is an external reason for the repo's finding that buying the top industry is close to a coin toss.

### Gaps
- No weekly-horizon (5-session) industry reversal number for US sectors was retrieved.
- CXO Advisory has a note "Short-term reversal by industry" that I could not open.
- Li and Turkington's effect sizes (monthly spreads, t-statistics) were not retrievable; only the direction is confirmed.

---

## 6. Concentration: sector-neutral versus sector-concentrated momentum, and capping positions per sector or industry

### Takeaway
For a long-only factor portfolio, removing sector bets usually lowers return, while for long-short it usually helps. Sector neutrality does not remove momentum crashes. I found no study that measures the drawdown saved and the return lost by a per-industry cap on a long-only momentum portfolio.

### Cited Findings
- Ehsani, Harvey and Li (2023, Financial Analysts Journal 79(3), 95–117): "the average long–short investor is more likely to benefit from hedging out sector bets, whereas the long-only investor should, on average, avoid sector neutralization" — [CFA Institute page](https://rpc.cfainstitute.org/research/financial-analysts-journal/2023/is-sector-neutrality-in-factor-investing-a-mistake); [author copy](https://people.duke.edu/~charvey/Research/Published_Papers/P165_Is_sector_neutrality.pdf)
- A summary of the same paper: keeping the sector component gives better long-short factors in only 20% of trials but better long-only factors in 78% of trials; the analysis is ex post on historical data — [Alpha Architect summary](https://alphaarchitect.com/factor-investing-and-sector-neutrality/); [Quantpedia summary](https://quantpedia.com/should-factor-investors-neutralize-the-sector-exposure/) (figures not checked against the paper; momentum-specific numbers not retrieved)
- Robeco (Blitz and Honarvar, February 2023), MSCI Developed universe, equal-weighted, monthly, region- and sector-neutral construction, January 2001 – January 2023: 12-1 month price momentum still has large drawdowns that "often occur after bear markets and coincide with rebounding markets"; a composite of residual momentum, earnings revisions and news sentiment gave similar returns with shallower drawdowns — [Robeco](https://www.robeco.com/en-uk/insights/2023/02/quant-chart-taming-momentum-crashes)
- MSCI (2019, "Back-to-school (momentum) blues?"): a 2019 US price-momentum drawdown was broad-based across sectors and driven mainly by strong returns of negative-momentum stocks — [MSCI](https://www.msci.com/research-and-insights/blog-post/back-to-school-momentum-blues)
- Newfound Research (long-short): moving from 49 industries to fewer, broader sectors reduces exposure to the pure momentum factor and "the strategy drawdown is reduced", at the price of lower total return — [Advisor Analyst repost](https://advisoranalyst.com/?p=89173)
- Quantpedia (2024; nine sector SPDRs, 1998–2024, long-only): holding 4–6 sectors gives better risk-adjusted results than holding 1–3 — [Quantpedia](https://quantpedia.com/how-to-improve-etf-sector-momentum/)
- Live example of uncapped concentration, 2026: five stocks accounted for more than half of the iShares MSCI USA Momentum ETF's (MTUM) year-to-date return; one commentator describes full-weight holders as "running a leveraged chip trade disguised as a factor strategy" — [24/7 Wall St., 6 July 2026](https://247wallst.com/personal-finance/2026/07/06/mtum-owns-the-winners-but-july-could-turn-into-a-momentum-bloodbath/) (news commentary)
- Indirect analogue from low-volatility indices: the sector-constrained MSCI Minimum Volatility index and the unconstrained S&P Low Volatility index behaved differently around the technology bubble, and the author judges sector-neutral construction better "when there are no clear market extremes" — [Fortune Financial Advisors](https://fortunefinancialadvisors.com/?p=3542) (low weight; not about momentum)
- An older study of active strategies under Shariah constraints: the constraints are "likely to have less effect on the performance of an active strategy if there are limits on sector concentration" — returned by search without a confirmed URL; candidates [HBKU paper](https://ibir-api.hbku.edu.qa/sites/default/files/2019-10/pdf_005.pdf), [CORE paper](https://core.ac.uk/download/301021846.pdf)

### Inferences
- For a long-only stock book the published evidence says sector tilts are part of where the factor return comes from. Full sector neutrality costs return on average. A soft cap (for example one stock per industry) is a much weaker constraint than neutrality and should cost less, but the cost has not been measured in anything I found.
- Sector neutrality and caps do not protect against the market-wide momentum crash (Robeco, MSCI). They protect against a different risk: one group collapsing on its own (energy 2014, semiconductors mid-2026). The two risks need two tools: a market-state brake for the first and a concentration cap for the second.
- The return-versus-drawdown trade for a cap is an empirical question the repo is better placed to answer than the literature: run the same entries with caps of 1, 2 and unlimited per industry and compare MDD and expectancy.

### Gaps
- No direct comparison of sector-capped versus uncapped long-only momentum (CAGR, MDD) from MSCI, S&P DJI, AQR or Robeco was found. The MSCI Momentum and S&P Momentum index methodologies (issuer caps, any sector limits) were not retrieved.
- Ehsani-Harvey-Li momentum-specific tables (Sharpe and drawdown with and without sector neutralisation) were not retrievable.
- No source on risk parity across sectors was retrieved.

---

## 7. The failure mode "the strongest industry is strongest right at the top" (technology 2000, energy 2014 and 2022, semiconductors/AI 2024–2026)

### Takeaway
Sector leadership has repeatedly peaked together with sector weight and then reversed hard: energy was about 28% of the S&P 500 in 1980 and about 3% now; technology was about 33–35% in March 2000 and nearly 40% in 2026. In mid-2026 a crowded AI/semiconductor momentum trade lost about 35% from its June peak within weeks. The evidence is descriptive (a handful of episodes), not a tested timing rule.

### Cited Findings
- Energy reached "nearly 28%" of the S&P 500 in 1980 after the oil shock and has retreated to "roughly 3% today" — [CME Group, 2026](https://www.cmegroup.com/openmarkets/economics/2026/What-Past-Sector-Concentrations-Tell-Us-About-Todays-Tech-Heavy-SP-500.html)
- Information technology went from about 6.7–7% of the S&P 500 in 1990 to 39.6% ("nearly 40%") in 2026 — [CME Group, 2026](https://www.cmegroup.com/openmarkets/economics/2026/What-Past-Sector-Concentrations-Tell-Us-About-Todays-Tech-Heavy-SP-500.html); [Institutional Investor version](https://www.institutionalinvestor.com/article/sponsored-content/what-past-sector-concentrations-tell-us-about-todays-tech-heavy-sp-500)
- At the March 2000 peak IT was about 33% of the index (another source says 35%), falling back to mid-teens in the early 2000s — [Zephyr](https://informaconnect.com/zephyr/article/when-giants-dominate-understanding-market-concentration-and-its-historical-impact/); [PortfolioPilot](https://portfoliopilot.com/resources/posts/is-the-s-p-500-still-truly-diversified) (the tool did not say which page gave which figure)
- After the March 2000 peak the S&P 500 fell 34.57% over the next 24 months and needed 86 months (to October 2007) to recover — [Zephyr](https://informaconnect.com/zephyr/article/when-giants-dominate-understanding-market-concentration-and-its-historical-impact/) (via search summary)
- Financials were about 20–22% of the S&P 500 before the 2008 crisis (real estate was then inside financials) — CME research note returned by search; candidates [CME 2026](https://www.cmegroup.com/insights/economic-research/2026/why-us-equity-benchmarks-are-moving-together-and-drifting-apart.html), [CME 2025](https://www.cmegroup.com/articles/2025/how-to-diversify-equities-portfolio.html)
- After the peaks of the "Nifty Fifty" (1973) and technology stocks (1999), 10-year excess returns in favour of non-mega-cap stocks reached about 8% — [Hussman Funds, January 2025](https://www.hussmanfunds.com/research/rs250115/) (commentary; annualisation not confirmed)
- Energy was the best S&P 500 sector in 2022 at +65.7% — [Novel Investor sector table](https://novelinvestor.com/sector-performance/). In 2023 energy and utilities were the only sectors with negative returns, while technology returned about 57% — [E*TRADE, "As the sectors turn"](https://us.etrade.com/knowledge/library/perspectives/daily-insights/stock-sectors-2023)
- 2026 AI/semiconductor momentum unwind, from news reports: Goldman Sachs put momentum positioning at the 100th percentile of the past five years; on 8 May (reported in 2026 coverage; year not independently confirmed) MTUM fell 1.8%, its worst day since late March, and Goldman's high-beta momentum basket dropped 8%, described as its biggest unwind in five years — [Pulse report](https://www.pulse.bot/stock-trading/news/momentum-etfs-slip-18-as-goldman-sachs-flags-buying-opportunity-5635f665-703e-48a0-a074-c879177be624/); [Real Investment Advice](https://realinvestmentadvice.com/resources/blog/momentum-meltdown-catches-traders-by-surprise/)
- By mid-to-late July 2026 the Goldman momentum basket was reported 35–36% below its June 2026 peak, described as the worst momentum-factor drawdown in almost two decades (since the financial crisis); in the July sell-off the MSCI ACWI semiconductor index lost 14.6% against 14.4% for the momentum index — [Trustnet](https://www.trustnet.com/news/13480892/why-ai-and-chip-stocks-are-getting-beat-down); [Real Investment Advice](https://realinvestmentadvice.com/resources/blog/momentum-meltdown-catches-traders-by-surprise/) (news reports; sources differ between 35% and 36%; the tool did not map each figure to one page)
- Before the unwind MTUM was up roughly 27–29% year to date and five stocks made up more than half of that gain — [24/7 Wall St., 6 July 2026](https://247wallst.com/personal-finance/2026/07/06/mtum-owns-the-winners-but-july-could-turn-into-a-momentum-bloodbath/)
- By 14 August 2026 a sector table showed energy leading 2026 year-to-date sector returns — [ChartRow](https://chartrow.com/sp500/sector-performance) (via search summary)

### Inferences
- A relative-strength rank is highest by construction at the end of a long run, so the strongest group is always strongest at its top as well as on the way up. The rank cannot tell the two apart. The mid-2026 semiconductor episode matches the repo's own note that the same industry signal fired at the June peak and that the exit saved the position.
- The practical defences supported by this evidence are an exit rule and a concentration cap, not a better entry filter. This agrees with the repo's finding that exits matter about 12 times more than entries.
- These are 4–5 episodes over 45 years. They show the failure mode exists and is large; they do not show that high sector weight or high relative strength predicts a top with any usable timing.

### Gaps
- No source was retrieved for energy around its 2014 peak (2014–2015 sector returns), or for energy's 2021 return.
- No systematic study was found that tests "top-ranked sector by 6–12 month return" forward returns conditional on the sector's index weight or valuation.
- News coverage found ends around late July 2026; I found nothing on how momentum or semiconductors performed from August to November 2026.

---

## 8. Sector-constrained universes: Shariah-compliant stock universes (no conventional financials, heavy technology and health care)

### Takeaway
A US Shariah universe is structurally a technology bet: SPUS is roughly 52–63% technology and 12–13% health care in 2026, depending on the classification. Academic work on momentum inside Shariah universes is thin and gives no measurement of how that concentration changes momentum drawdowns.

### Cited Findings
- S&P Global BMI Shariah: information technology was 40.4% of the index against 26.8% in the conventional S&P Global BMI as of 31 October 2025 — [S&P DJI Indexology, 7 January 2026](https://www.indexologyblog.com/2026/01/07/index-based-investing-in-islamic-finance-2025-review/)
- A Q2 2026 S&P commentary puts IT at over 45% of the S&P Global BMI Shariah — S&P DJI page returned by search without a confirmed URL; candidates [S&P Shariah scorecard](https://spglobal.com/spdji/es/documents/performance-reports/scorecard-sp-shariah-djim.pdf), [Indexology, 30 July 2026](https://www.indexologyblog.com/2026/07/30/taking-the-pulse-what-private-wealth-managers-are-saying-in-arcs-market-sentiment-survey-q2-2026/)
- S&P DJI education paper (2023, exhibits dated December 2022): Shariah indices have the highest representation in information technology, health care, industrials and energy, and the lowest in financials, utilities and communication services — [S&P DJI Practice Essentials](https://spglobal.com/spdji/en/documents/education/practice-essentials-how-indexing-affects-shariah-compliant-investing.pdf)
- SPUS (SP Funds S&P 500 Sharia Industry Exclusions ETF), GICS-style figures: information technology 52.76% and health care 12.65% as of 28 February 2026 — [ETF Central](https://www.etfcentral.com/fund/SPUS); information technology 51.86% and health care 13.03% as of 31 March 2026 — [Trackinsight](https://www.trackinsight.com/en/fund/SPUS)
- SPUS, broader "Technology" classification: 63.3% technology and 11.79% health care as of 31 July 2026 — [ETF Central comparison page](https://www.etfcentral.com/compare-etfs/XLSR-vs-SPUS); 59.9% technology and 11.8% health care with an asset date of 31 August 2026 — [ETF Beacon](https://etfbeacon.com/etf/SPUS) (the tool did not confirm which page gave the August figure)
- Li, Ee, Boo and Rashid (2016, Emerald book chapter, "The Last Alibi: Shari'ah Compliant Stocks on Momentum Profitability Assessment"): momentum returns exist in Shariah-compliant stocks in Pakistan and Malaysia and are not driven by industry momentum or small size; no momentum profit in global Shariah portfolios, largely because small Shariah stocks reverse — [Emerald chapter](https://www.emerald.com/books/edited-volume/10492/chapter/80028877/The-Last-Alibi-Shari-ah-Compliant-Stocks-on)
- A 2025 paper reports idiosyncratic (residual) momentum profits in US Shariah-compliant stocks over 1986–2020 — [Journal of Finance & Economics Research](https://journals.iqra.edu.pk/archives/view/jfer/10/JFER25100101) (minor journal; long-short or long-only not confirmed)
- ETF comparison site: HLAL (FTSE USA Shariah) worst drawdown -33.6% against -34.1% for MTUM "over the last decade", with about 18.4% overlapping technology weight — [BestETF comparison](https://www.bestetf.net/compare/MTUM-vs-HLAL) (commercial source; HLAL is younger than ten years as far as I know, so treat the period label with caution)
- Practitioner description of the structural tilt: Shariah screening pushes weight "towards tech, healthcare and capital-light businesses – and away from banks" — [Ghost Mail interview, 2026](https://www.ghostmail.co.za/ghost-stories-103-how-shariah-compliant-investing-can-outperform-with-maahir-jakoet/)

### Inferences
- In a universe that is 50–60% technology, a momentum or relative-strength rule has less room to rotate: when technology leads, the rule and the benchmark hold the same thing; when technology breaks, most candidates break together. Sector-strength filters therefore add less information here than in the full S&P 500, and concentration risk is higher at the same number of holdings.
- The similar worst drawdowns reported for HLAL and MTUM fit the idea that a US Shariah index already behaves like a growth/momentum-tilted portfolio. SPUS as benchmark already contains much of what a sector-strength filter would select.
- Because the sector share of variance is larger when holdings cluster in one sector, a per-industry cap matters more in a Shariah universe than in a broad one. This supports keeping the cap as a risk control.

### Gaps
- No study was found that measures how sector concentration in a Shariah universe changes momentum returns or momentum drawdowns. A dedicated backtest would be needed.
- No official S&P 500 Shariah factsheet with dated sector weights was retrieved; the SPUS weights above come from third-party data pages with different classification schemes and dates.
- A Schwab table dated 30 June 2026 showing IT 38.0% and health care 8.9% appeared in search results without saying which index it describes; I did not use it.

---

## 9. Objective question: when a stock rule is conditioned on market state AND sector/industry strength together, does the combination add return, or mainly change risk?

### Takeaway
No study I found tests the full stack (market regime × sector strength × industry strength × stock rule) with costs. The pieces that are measured point one way: the market-state layer changes risk (drawdown) and sometimes carries most of any gain, the sector layer adds little or no return beyond stock-level momentum, and neither removes the momentum crash.

### Cited Findings
- Market-state layer on top of sector rotation: Faber's 10-month moving-average hedge gives "similar absolute returns" with "marked reductions in drawdown" (1928–2009, gross) — [the7circles summary](https://the7circles.uk/?p=35490); [Quantpedia strategy page](https://quantpedia.com/strategies/sector-momentum-rotational-system)
- In the most favourable sector-fund test (2002–2015), the reviewer attributes part of the edge to market timing and the Sharpe ratio was below SPY's — [CXO Advisory](https://cxoadvisory.com/momentum-investing/assessing-jays-pure-momentum-system)
- A plain market-timing rule (out of the market in early recession only) produced 0.18% outperformance against 0.16% a month for perfect-foresight sector rotation, 1948–2022, before costs — [Massey repository PDF](https://mro.massey.ac.nz/bitstreams/1f32a859-5ef9-442d-a5f8-ac8e0f5b1a83/download)
- Sector layer on top of stock momentum: sector rotation is "entirely subsumed by the momentum factor"; it gives up return in exchange for less exposure to momentum crashes (long-short, post-1944) — [Advisor Analyst repost of Newfound](https://advisoranalyst.com/?p=89173)
- Conditional effect: industry momentum is profitable only after UP markets (Hühn 2015), and stock momentum earns +0.93% a month after UP states against -0.37% after DOWN states (Cooper et al. 2004, 1929–1995) — [Hedge Fund Alpha abstract page](https://hedgefundalpha.com/strategies/industry-momentum-the-role-of-time-varying-factor-exposures-and-market-conditions/); [Cooper et al. copy](https://typeset.io/pdf/market-states-and-momentum-4wtc7g4rqv.pdf)
- For long-only factor portfolios, stripping out the sector component lowers performance in most trials (78% of trials favour keeping it) — [Alpha Architect summary](https://alphaarchitect.com/factor-investing-and-sector-neutrality/); [CFA Institute page](https://rpc.cfainstitute.org/research/financial-analysts-journal/2023/is-sector-neutrality-in-factor-investing-a-mistake)
- Sector- and region-neutral momentum still suffers the rebound crash — [Robeco, 2023](https://www.robeco.com/en-uk/insights/2023/02/quant-chart-taming-momentum-crashes); a 2019 US momentum drawdown was broad-based across sectors — [MSCI, 2019](https://www.msci.com/research-and-insights/blog-post/back-to-school-momentum-blues)

### Inferences
- Stacking the filters is not additive in return. The market-state filter and the sector/industry filter both select the same thing (stocks in uptrends during uptrends), so the second and third filters mostly reduce the number of trades and concentrate what is left.
- The interaction is real but it is about sign, not size: relative strength at any level (stock, industry, sector) has positive expectancy after up markets and zero or negative after down markets. A stack that requires "regime ON and strong industry" is therefore mainly a way of not trading in the bad state. The gain shows up as smaller drawdown.
- Stacking raises concentration: in regime-ON periods the strongest industries are few and correlated (section 7), so "regime ON + top industry + top stock" produces a book that is one bet. Without a per-industry cap the stack increases tail risk at exactly the point where the signals agree most.
- For a long-only book, the sector component is part of the return (Ehsani-Harvey-Li), so the right use of sector/industry information is a soft cap (limit names per industry), not neutrality and not a selection score.
- This is the same conclusion the repo reached on its own data (regime = risk brake; top industry ≈ coin toss; industry useful as a cap). The outside evidence gives no reason to add a sector-strength or industry-strength entry filter to the stock rules.

### Gaps
- I found no factorial study (regime on/off × sector filter on/off × industry filter on/off) on US stocks, long-only, with costs. The claim "no evidence that the stack adds return" rests on the separate pieces above.
- Antonacci-style "dual momentum" sector rotation (absolute plus relative momentum on sectors) was not retrieved; it is the closest published two-layer design and should be checked if the report needs a named example.
- No evidence was found on the triple stack for holding periods as short as 10–15 sessions; nearly all sources use monthly rebalancing.
