---
name: stock-liquidity
description: >
  Analyze how liquid a stock is using Yahoo Finance data (yfinance): bid-ask spreads,
  volume and dollar volume (ADTV), top-of-book and options depth, square-root market
  impact and slippage estimates, turnover ratio, and Amihud illiquidity, rolled into a
  liquidity grade. Use this skill whenever the user asks about liquidity or trading
  costs — how easily a position can be entered or exited, what a large order would do
  to the price, spread or execution-cost estimates, order book depth, volume patterns,
  or liquidity comparisons — especially for small caps, penny stocks, and thinly
  traded names.
---

# Stock Liquidity Analysis Skill

If your host has not already executed the shell probes below (for example, in Codex), run the commands inside the `!` wrappers with its shell tool before choosing a setup path. Use the actual output; if shell access is unavailable, report that limitation.

Analyzes stock liquidity across multiple dimensions — bid-ask spreads, volume patterns, order book depth, estimated market impact, and turnover ratios — using data from Yahoo Finance via [yfinance](https://github.com/ranaroussi/yfinance).

Liquidity matters because it determines the real cost of trading. The quoted price is not what you actually pay — spreads, slippage, and market impact all eat into returns, especially for larger positions or less liquid names.

**Important**: This is for research and educational purposes only. Not financial advice. yfinance is not affiliated with Yahoo, Inc.

---

## Step 1: Ensure Dependencies Are Available

**Current environment status:**

```
!`python3 -c "exec('try:\n import yfinance, pandas, numpy\n print(f\'yfinance={yfinance.__version__} pandas={pandas.__version__} numpy={numpy.__version__}\')\nexcept Exception:\n print(\'DEPS_MISSING\')')"`
```

If `DEPS_MISSING`, install required packages:

```python
import subprocess, sys
subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", "yfinance", "pandas", "numpy"])
```

If already installed, skip and proceed.

If a function below returns `None`, or Yahoo Finance cannot be reached, retry once after 5 seconds. If it
fails again, tell the user "no data returned for <ticker>" with the error text, and stop. Never fill in
numbers from memory. Why: an invented spread or volume looks exactly like a real one.

---

## Step 2: Route to the Correct Sub-Skill

Classify the user's request and jump to the matching section. If the user asks for a general liquidity assessment without specifying a particular metric, run **Sub-Skill A** (Liquidity Dashboard) which computes all key metrics together.

| User Request | Route To | Examples |
|---|---|---|
| General liquidity check, "how liquid is X" | **Sub-Skill A: Liquidity Dashboard** | "how liquid is AAPL", "liquidity analysis for TSLA", "is this stock liquid enough" |
| Bid-ask spread, trading costs, effective spread | **Sub-Skill B: Spread Analysis** | "bid-ask spread for AMD", "what's the spread on NVDA options", "trading cost estimate" |
| Volume, ADTV, dollar volume, volume profile | **Sub-Skill C: Volume Analysis** | "volume analysis MSFT", "average daily volume", "volume profile for SPY" |
| Order book depth, market depth, level 2 | **Sub-Skill D: Order Book Depth** | "order book depth for AAPL", "market depth", "show me the book" |
| Market impact, slippage, execution cost for large orders | **Sub-Skill E: Market Impact** | "how much would 50k shares move the price", "slippage estimate", "market impact of $1M order" |
| Turnover ratio, trading activity relative to float | **Sub-Skill F: Turnover Ratio** | "turnover ratio for GME", "float turnover", "how actively traded is this" |
| Compare liquidity across multiple stocks | **Sub-Skill A** (multi-ticker mode) | "compare liquidity AAPL vs TSLA", "which is more liquid AMD or INTC" |

### Defaults

| Parameter | Default |
|---|---|
| Lookback period | `3mo` (3 months) |
| Data interval | `1d` (daily) |
| Market impact model | Square-root model |
| Intraday interval (when needed) | `5m` |

---

## Sub-Skill A: Liquidity Dashboard

**Goal**: Produce a comprehensive liquidity snapshot combining all key metrics for one or more tickers.

### A1: Fetch data and compute all metrics

```python
import yfinance as yf
import pandas as pd
import numpy as np

def liquidity_dashboard(ticker_symbol, period="3mo"):
    ticker = yf.Ticker(ticker_symbol)
    info = ticker.info
    hist = ticker.history(period=period)

    if hist.empty:
        return None

    # --- Spread metrics (from current quote) ---
    bid = info.get("bid", None)
    ask = info.get("ask", None)
    current_price = info.get("currentPrice") or info.get("regularMarketPrice") or hist["Close"].iloc[-1]

    spread = None
    spread_pct = None
    if bid and ask and bid > 0 and ask > 0:
        spread = round(ask - bid, 4)
        midpoint = (ask + bid) / 2
        spread_pct = round((spread / midpoint) * 100, 4)

    # --- Volume metrics ---
    avg_volume = hist["Volume"].mean()
    median_volume = hist["Volume"].median()
    avg_dollar_volume = (hist["Close"] * hist["Volume"]).mean()
    volume_std = hist["Volume"].std()
    volume_cv = volume_std / avg_volume if avg_volume > 0 else None  # coefficient of variation

    # --- Turnover ratio ---
    shares_outstanding = info.get("sharesOutstanding", None)
    float_shares = info.get("floatShares", None)
    base_shares = float_shares or shares_outstanding
    turnover_ratio = round(avg_volume / base_shares, 6) if base_shares else None

    # --- Amihud illiquidity ratio ---
    # Average of |daily return| / daily dollar volume
    returns = hist["Close"].pct_change().dropna()
    dollar_volume = (hist["Close"] * hist["Volume"]).iloc[1:]  # align with returns
    amihud_values = returns.abs() / dollar_volume
    amihud = amihud_values[amihud_values.replace([np.inf, -np.inf], np.nan).notna()].mean()

    # --- Market impact estimate (square-root model) ---
    # For a hypothetical order of 1% of ADV
    adv = avg_volume
    order_size = adv * 0.01
    daily_volatility = returns.std()
    sigma = daily_volatility
    participation_rate = order_size / adv if adv > 0 else 0
    impact_bps = sigma * np.sqrt(participation_rate) * 10000  # in basis points

    return {
        "ticker": ticker_symbol,
        "current_price": round(current_price, 2),
        "bid": bid,
        "ask": ask,
        "spread": spread,
        "spread_pct": spread_pct,
        "avg_daily_volume": int(avg_volume),
        "median_daily_volume": int(median_volume),
        "avg_dollar_volume": round(avg_dollar_volume, 0),
        "volume_cv": round(volume_cv, 3) if volume_cv else None,
        "shares_outstanding": shares_outstanding,
        "float_shares": float_shares,
        "turnover_ratio": turnover_ratio,
        "amihud_illiquidity": round(amihud * 1e9, 4) if not np.isnan(amihud) else None,
        "daily_volatility": round(daily_volatility * 100, 2),
        "impact_1pct_adv_bps": round(impact_bps, 2),
        "observations": len(hist),
    }
```

### A2: Interpret and present

Present as a summary card. For the Amihud illiquidity ratio, multiply by 1e9 for readability (standard convention).

**Liquidity grade** (thresholds for US equities). Assign it in three steps:

1. Grade each metric that has a value separately, using its column in the table.
2. The overall grade is the least liquid of those grades. Why: the weakest dimension sets the real cost of trading.
3. If a metric is `None` (for example, no bid/ask outside market hours), leave it out and say which metric
   was missing.

| Grade | Avg Dollar Volume | Spread (%) | Amihud (×10⁹) |
|---|---|---|---|
| Very High | > $500M/day | < 0.03% | < 0.01 |
| High | $50M–$500M/day | 0.03–0.10% | 0.01–0.1 |
| Moderate | $5M–$50M/day | 0.10–0.50% | 0.1–1.0 |
| Low | $500K–$5M/day | 0.50–2.00% | 1.0–10 |
| Very Low | < $500K/day | > 2.00% | > 10 |

When comparing multiple tickers, show a side-by-side table and highlight which is more liquid and why.

---

## Sub-Skill B: Spread Analysis

**Goal**: Detailed bid-ask spread analysis including current spread, historical context from options data, and effective spread estimates.

### B1: Current spread from quote

```python
import yfinance as yf

def spread_analysis(ticker_symbol):
    ticker = yf.Ticker(ticker_symbol)
    info = ticker.info

    bid = info.get("bid", 0)
    ask = info.get("ask", 0)
    bid_size = info.get("bidSize", None)
    ask_size = info.get("askSize", None)
    current_price = info.get("currentPrice") or info.get("regularMarketPrice", 0)

    result = {"bid": bid, "ask": ask, "bid_size": bid_size, "ask_size": ask_size}

    if bid > 0 and ask > 0:
        midpoint = (bid + ask) / 2
        result["absolute_spread"] = round(ask - bid, 4)
        result["relative_spread_pct"] = round((ask - bid) / midpoint * 100, 4)
        result["relative_spread_bps"] = round((ask - bid) / midpoint * 10000, 2)
    return result
```

### B2: Options spread context

Options data from yfinance includes bid/ask for each strike, which gives a sense of derivatives liquidity. Use the nearest expiration, extract near-the-money calls and puts, and compute spread and spread percentage for each.

See `references/liquidity_reference.md` § "Options Spread Analysis" for the full code template.

### B3: Present results

Show:
- Current quoted spread (absolute, relative %, basis points)
- Bid/ask sizes if available
- Near-the-money options spreads for context
- Which row of the Spread (%) column in the Sub-Skill A grade table the relative spread falls in

---

## Sub-Skill C: Volume Analysis

**Goal**: Analyze trading volume patterns — averages, trends, relative volume, and dollar volume.

### C1: Compute volume metrics

```python
import yfinance as yf
import pandas as pd
import numpy as np

def volume_analysis(ticker_symbol, period="3mo"):
    ticker = yf.Ticker(ticker_symbol)
    hist = ticker.history(period=period)

    if hist.empty:
        return None

    vol = hist["Volume"]
    close = hist["Close"]
    dollar_vol = vol * close

    # Relative volume (today vs average)
    rvol = vol.iloc[-1] / vol.mean() if vol.mean() > 0 else None

    # Volume trend (linear regression slope over the period)
    x = np.arange(len(vol))
    slope, _ = np.polyfit(x, vol.values, 1) if len(vol) > 1 else (0, 0)
    trend_pct = (slope * len(vol)) / vol.mean() * 100  # % change over period

    # Volume profile by day of week
    hist_copy = hist.copy()
    hist_copy["DayOfWeek"] = hist_copy.index.dayofweek
    day_names = {0: "Mon", 1: "Tue", 2: "Wed", 3: "Thu", 4: "Fri"}
    vol_by_day = hist_copy.groupby("DayOfWeek")["Volume"].mean()
    vol_by_day.index = vol_by_day.index.map(day_names)

    # High/low volume days
    high_vol_days = hist.nlargest(5, "Volume")[["Close", "Volume"]]
    low_vol_days = hist.nsmallest(5, "Volume")[["Close", "Volume"]]

    return {
        "avg_volume": int(vol.mean()),
        "median_volume": int(vol.median()),
        "avg_dollar_volume": round(dollar_vol.mean(), 0),
        "current_volume": int(vol.iloc[-1]),
        "relative_volume": round(rvol, 2) if rvol else None,
        "volume_trend_pct": round(trend_pct, 1),
        "volume_by_day": vol_by_day.to_dict(),
        "high_vol_days": high_vol_days,
        "low_vol_days": low_vol_days,
        "max_volume": int(vol.max()),
        "min_volume": int(vol.min()),
    }
```

### C2: Present results

Show:
- Average daily volume (shares and dollar) with median for comparison
- Relative volume (RVOL) — today's volume vs. the average. RVOL > 1.5 is elevated; RVOL < 0.5 is unusually quiet
- Volume trend — is trading activity increasing or declining?
- Day-of-week pattern, only if the busiest weekday's average volume is at least 20% above the quietest weekday's
- Top 5 highest-volume days with context (earnings? news?)

---

## Sub-Skill D: Order Book Depth

**Goal**: Estimate order book depth using available bid/ask data from the equity quote and options chain.

Yahoo Finance does not provide full Level 2 / order book data. Be upfront about this limitation. What we can do:

1. **Equity quote**: bid, ask, bid size, ask size (top of book only)
2. **Options chain**: bid/ask and open interest across strikes give a proxy for derivatives depth
3. **Intraday volume distribution**: how volume is distributed within the day suggests how deep the continuous market is

### D1: Gather available depth data

Collect three data points:

1. **Top of book** — bid, ask, bidSize, askSize from `ticker.info`
2. **Intraday volume distribution** — 5-min bars over the last 5 days, grouped by time-of-day and normalized to percentage of daily volume
3. **Options open interest** — total call/put OI and volume from the nearest expiration as a derivatives depth proxy

See `references/liquidity_reference.md` § "Order Book Depth Proxy" for the full code template.

### D2: Present results

Show:
- **Top of book**: current bid/ask with sizes
- **Intraday volume shape**: where volume concentrates (open/close vs. midday)
- **Options depth**: total open interest and volume as a proxy for derivatives liquidity
- **Honest limitation**: "Yahoo Finance provides top-of-book only. For full Level 2 depth, a direct market data feed (e.g., NYSE OpenBook, NASDAQ TotalView) is needed."

---

## Sub-Skill E: Market Impact

**Goal**: Estimate how much a given order size would move the price, using the square-root market impact model.

The standard model in practice is: **Impact (%) = σ × √(Q / V)** where σ is daily volatility, Q is order size in shares, and V is average daily volume. This is a simplified version of the Almgren-Chriss framework used by institutional traders.

### E1: Compute market impact estimate

```python
import yfinance as yf
import numpy as np

def market_impact(ticker_symbol, order_shares=None, order_dollars=None, period="3mo"):
    ticker = yf.Ticker(ticker_symbol)
    hist = ticker.history(period=period)
    info = ticker.info

    if hist.empty:
        return None

    current_price = info.get("currentPrice") or hist["Close"].iloc[-1]
    avg_volume = hist["Volume"].mean()
    daily_volatility = hist["Close"].pct_change().dropna().std()

    # Determine order size in shares
    if order_dollars and not order_shares:
        order_shares = order_dollars / current_price
    elif not order_shares:
        # Default: estimate for various sizes
        order_shares = avg_volume * 0.01  # 1% of ADV

    participation_rate = order_shares / avg_volume if avg_volume > 0 else 0
    pct_adv = (order_shares / avg_volume * 100) if avg_volume > 0 else 0

    # Square-root impact model
    impact_pct = daily_volatility * np.sqrt(participation_rate) * 100
    impact_bps = impact_pct * 100
    impact_dollars = impact_pct / 100 * current_price * order_shares

    # Generate impact curve for multiple order sizes
    sizes = [0.001, 0.005, 0.01, 0.02, 0.05, 0.10, 0.20, 0.50]  # as fraction of ADV
    curve = []
    for s in sizes:
        q = avg_volume * s
        imp = daily_volatility * np.sqrt(s) * 100
        curve.append({
            "pct_adv": round(s * 100, 1),
            "shares": int(q),
            "dollars": round(q * current_price, 0),
            "impact_bps": round(imp * 100, 1),
            "impact_dollars_per_share": round(imp / 100 * current_price, 4),
        })

    return {
        "ticker": ticker_symbol,
        "current_price": round(current_price, 2),
        "avg_daily_volume": int(avg_volume),
        "daily_volatility_pct": round(daily_volatility * 100, 2),
        "order_shares": int(order_shares),
        "order_dollars": round(order_shares * current_price, 0),
        "pct_of_adv": round(pct_adv, 2),
        "estimated_impact_bps": round(impact_bps, 1),
        "estimated_impact_pct": round(impact_pct, 4),
        "estimated_impact_total_dollars": round(impact_dollars, 2),
        "impact_curve": curve,
    }
```

### E2: Present results

Show:
- The estimated impact for the user's specific order size
- An impact curve table showing how cost scales with order size
- Context: "This uses the square-root market impact model, a standard institutional estimate. Actual impact depends on execution strategy (VWAP, TWAP, etc.), time of day, and current market conditions."
- Above ~25 bps, note that the order is large for the stock's liquidity; above ~50 bps, flag it clearly and suggest the user consider algorithmic execution or splitting the order across days

---

## Sub-Skill F: Turnover Ratio

**Goal**: Measure how actively a stock trades relative to its shares outstanding and free float.

### F1: Compute turnover metrics

```python
import yfinance as yf
import pandas as pd
import numpy as np

def turnover_analysis(ticker_symbol, period="3mo"):
    ticker = yf.Ticker(ticker_symbol)
    hist = ticker.history(period=period)
    info = ticker.info

    if hist.empty:
        return None

    avg_volume = hist["Volume"].mean()
    shares_outstanding = info.get("sharesOutstanding")
    float_shares = info.get("floatShares")

    result = {
        "avg_daily_volume": int(avg_volume),
        "shares_outstanding": shares_outstanding,
        "float_shares": float_shares,
    }

    if shares_outstanding:
        daily_turnover = avg_volume / shares_outstanding
        result["daily_turnover_ratio"] = round(daily_turnover, 6)
        result["annualized_turnover"] = round(daily_turnover * 252, 2)
        result["days_to_trade_float"] = round(
            (float_shares or shares_outstanding) / avg_volume, 1
        ) if avg_volume > 0 else None

    if float_shares:
        float_turnover = avg_volume / float_shares
        result["float_turnover_daily"] = round(float_turnover, 6)
        result["float_turnover_annualized"] = round(float_turnover * 252, 2)

    # Turnover trend
    vol = hist["Volume"]
    base = float_shares or shares_outstanding
    if base:
        hist_copy = hist.copy()
        hist_copy["turnover"] = hist_copy["Volume"] / base
        recent_turnover = hist_copy["turnover"].tail(20).mean()
        older_turnover = hist_copy["turnover"].head(20).mean()
        if older_turnover > 0:
            result["turnover_trend_pct"] = round(
                (recent_turnover - older_turnover) / older_turnover * 100, 1
            )

    return result
```

### F2: Present results

Show:
- Daily and annualized turnover ratios (vs. outstanding and float)
- "Days to trade the float" — how many days at average volume to turn over the entire free float
- Turnover trend — is the stock becoming more or less actively traded?
- Context:

| Turnover (Annualized) | Interpretation |
|---|---|
| > 500% | Extremely active — likely speculative or momentum-driven |
| 100–500% | Actively traded |
| 30–100% | Moderate activity |
| < 30% | Thinly traded — likely institutional buy-and-hold or neglected |

---

## Step 3: Respond to the User

After running the appropriate sub-skill:

### Always include

- The **lookback period** used for historical metrics
- The **data timestamp** — spreads and quotes are snapshots, not real-time
- Any tickers that returned **empty data** (invalid symbol, delisted, etc.)

### Always caveat

- Yahoo Finance quote data has a **15-minute delay** for most exchanges — spreads shown may not reflect the current live market
- Full order book (Level 2) data is **not available** through Yahoo Finance
- Market impact estimates are **models, not guarantees** — actual execution costs depend on strategy, timing, and market conditions
- Liquidity can **change rapidly** — a stock that's liquid today may not be tomorrow (especially around events, halts, or during extended hours)

### Practical guidance (include a line only when its condition is true)

- **Position sizing** (condition: estimated impact above 25 bps): the position may be too large for the stock's liquidity (see the thresholds in Sub-Skill E)
- **Small/micro-cap warning** (condition: average dollar volume below $1M per day): suggest limit orders and splitting the order across days
- **Spread costs compound** (condition: the user trades the stock often, or asks about strategy costs): a 0.10% spread on a round-trip (buy + sell) costs 0.20%
- **Illiquidity premium** (condition: overall grade is Low or Very Low): less liquid stocks historically earn higher returns as compensation, but transaction costs can eat this premium

Present liquidity data and let the user make their own decisions; don't recommend specific trades.
Why: this skill measures trading cost; it does not judge whether a trade is a good idea.

### Example of a finished answer

Request: "How liquid is A (Agilent)?" Sub-Skill A, 3-month lookback. Bid/ask and share counts were not
available in this run, so spread and turnover are reported as missing.

```
A (Agilent) liquidity, 2026-08-18 to 2026-11-17 (65 trading days, daily bars)

Price (last close)          172.22
Average daily volume        2,340,959 shares (median 2,255,860)
Average dollar volume       $385.8M per day
Volume variability (CV)     0.284
Amihud illiquidity (x1e9)   0.0413
Daily volatility            1.92%
Impact of 1% of ADV         19.2 bps (23,409 shares, about $4.0M)
Bid-ask spread              not available
Turnover ratio              not available

Grade by metric: dollar volume High ($50M to $500M) | Amihud High (0.01 to 0.1) | spread missing
Overall grade: High (least liquid of the available grades)

Impact curve: 1% of ADV 19.2 bps | 5% of ADV 43.0 bps | 10% of ADV 60.8 bps
Position sizing: an order above about 1.7% of ADV crosses 25 bps; 10% of ADV is above 50 bps, so consider
splitting it across days.

Caveats: quotes are delayed about 15 minutes and are snapshots; Level 2 depth is not available from
Yahoo Finance; impact figures are model estimates, not guarantees; liquidity can change quickly around events.
```

---

## Reference Files

- `references/liquidity_reference.md` — Detailed formulas, extended code templates, metric interpretation guides, and academic references for all liquidity measures

Read the reference file when you need exact formulas, edge case handling, or deeper background on liquidity metrics.

## Final Checklist (run before saying you are done)

- [ ] The sub-skill code ran in this session and the answer quotes its output.
- [ ] Every number in the answer appears in that output; none came from memory.
- [ ] The lookback period and the data date are stated.
- [ ] Any metric that came back `None` is reported as "not available", not left out silently.
- [ ] The grade was assigned with the three-step rule, and the answer says which metrics it used.
- [ ] All four "Always caveat" points are included.
- [ ] A practical-guidance line appears only where its condition is true.
- [ ] The answer does not recommend buying or selling.
