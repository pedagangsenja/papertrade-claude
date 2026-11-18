---
name: yfinance-data
description: >
  Fetch financial and market data with the yfinance Python library (Yahoo Finance).
  Use this skill whenever the user wants stock data: current quotes and price history,
  financial statements (income statement, balance sheet, cash flow), options chains,
  dividends and splits, earnings and analyst estimates, price targets and ratings,
  institutional and insider holdings, news, multi-ticker comparisons, stock screens,
  or sector and industry data. Use it even when the user gives only a ticker symbol
  (AAPL, MSFT, TSLA) and the intent has to be inferred. For earnings previews or
  recaps, estimate revisions, valuation, correlation, liquidity, or ETF premium
  analysis, prefer the dedicated skill.
---

# yfinance Data Skill

If your host has not already executed the shell probes below (for example, in Codex), run the commands inside the `!` wrappers with its shell tool before choosing a setup path. Use the actual output; if shell access is unavailable, report that limitation.

Fetches financial and market data from Yahoo Finance using the [yfinance](https://github.com/ranaroussi/yfinance) Python library.

**Important**: yfinance is not affiliated with Yahoo, Inc. Data is for research and educational purposes.

---

## Step 1: Ensure yfinance Is Available

**Current environment status:**

```
!`python3 -c "exec('try:\n import yfinance\n print(\'yfinance \' + yfinance.__version__ + \' installed\')\nexcept Exception:\n print(\'YFINANCE_NOT_INSTALLED\')')"`
```

If `YFINANCE_NOT_INSTALLED`, install it before running any code:

```python
import subprocess, sys
subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", "yfinance"])
```

If yfinance is already installed, skip the install step and proceed directly.

If the repository has a constraints or requirements file that pins yfinance (for example `kekangan.txt`),
install that exact version instead: `pip install -q -c kekangan.txt yfinance`.
Why: an unpinned version can change column names and break code that reads the data.

---

## Step 2: Identify What the User Needs

1. Match the user's request to one or more rows of the table below.
2. If only a ticker is given (for example "AAPL"), fetch the current price and the last 1 month of daily history.
3. Use the code for that row from `references/api_reference.md`.

| User Request | Data Category | Primary Method |
|---|---|---|
| Stock price, quote | Current price | `ticker.info` or `ticker.fast_info` |
| Price history, chart data | Historical OHLCV | `ticker.history()` or `yf.download()` |
| Balance sheet | Financial statements | `ticker.balance_sheet` |
| Income statement, revenue | Financial statements | `ticker.income_stmt` |
| Cash flow | Financial statements | `ticker.cashflow` |
| Dividends | Corporate actions | `ticker.dividends` |
| Stock splits | Corporate actions | `ticker.splits` |
| Options chain, calls, puts | Options data | `ticker.option_chain()` |
| Earnings, EPS | Analysis | `ticker.earnings_history` |
| Analyst price targets | Analysis | `ticker.analyst_price_targets` |
| Recommendations, ratings | Analysis | `ticker.recommendations` |
| Upgrades/downgrades | Analysis | `ticker.upgrades_downgrades` |
| Institutional holders | Ownership | `ticker.institutional_holders` |
| Insider transactions | Ownership | `ticker.insider_transactions` |
| Company overview, sector | General info | `ticker.info` |
| Compare multiple stocks | Bulk download | `yf.download()` |
| Screen/filter stocks | Screener | `yf.screen()` + `yf.EquityQuery` |
| Sector/industry data | Market data | `yf.Sector` / `yf.Industry` |
| News | News | `ticker.news` |

---

## Step 3: Write and Execute the Code

### General pattern

```python
import yfinance as yf

ticker = yf.Ticker("AAPL")
# ... use the appropriate method from the reference
```

### Key rules

1. **Always wrap in try/except.** Why: Yahoo Finance may rate-limit, block the connection or return empty data.
2. **If the call fails or returns an empty result, retry once after 5 seconds.** If it fails again, tell the user
   "no data returned for <ticker>" with the error text, and stop. Never fill in numbers from memory.
   Why: an invented price looks exactly like a real one.
3. **Use `yf.download()` for multi-ticker comparisons.** Why: it fetches tickers in parallel, so it is faster.
4. **For options, list expiration dates first** with `ticker.options` before calling `ticker.option_chain(date)`.
   Why: `option_chain` fails on a date that is not a listed expiration.
5. **For quarterly data**, use the `quarterly_` prefix: `ticker.quarterly_income_stmt`, `ticker.quarterly_balance_sheet`, `ticker.quarterly_cashflow`.
6. **Intraday limits**: 1m data covers only the last ~7 days; 1h data only the last ~730 days. If the requested
   range is longer than the limit, use the next larger interval and say which interval you used.
7. **Print at most 20 rows**, with `.to_string()` or `.to_markdown()`, and only the columns the user asked about.
   Why: a wider or longer table hides the answer.
8. **Timezone handling**: yfinance returns tz-aware datetime indices (e.g., `America/New_York`). When comparing dates, always use `pd.Timestamp(..., tz=...)` or strip timezones with `.tz_localize(None)`. See the reference file for details.

### Valid periods and intervals

| Periods | `1d`, `5d`, `1mo`, `3mo`, `6mo`, `1y`, `2y`, `5y`, `10y`, `ytd`, `max` |
|---|---|
| **Intervals** | `1m`, `2m`, `5m`, `15m`, `30m`, `60m`, `90m`, `1h`, `1d`, `5d`, `1wk`, `1mo`, `3mo` |

---

## Step 4: Present the Data

Write the answer in this order:

1. The number the user asked for, in the first line, with its date.
2. The supporting table (markdown, at most 20 rows, key columns only).
3. Notable items, only if they appear in the data you fetched:
   - earnings beat or miss (reported EPS against the estimate);
   - unusual volume (latest volume more than 1.5x the average of the period shown);
   - a dividend change (latest dividend differs from the previous one).
4. Context that changes how the numbers read (sector average, historical range, analyst consensus), only if
   you fetched it in this session. Why: context quoted from memory may be out of date.
5. One line stating the source (Yahoo Finance via yfinance), the period and the interval.
6. If the user wants a chart, add a visualization of the same data.

### Example of a finished answer

Request: "Price history for A (Agilent), last 5 trading days."

```
A closed at 172.22 on 2026-11-17.

| Date       |   Open |   High |    Low |  Close |    Volume |
|------------|-------:|-------:|-------:|-------:|----------:|
| 2026-11-11 | 178.99 | 181.27 | 176.83 | 176.95 | 1,908,700 |
| 2026-11-12 | 173.90 | 174.62 | 171.26 | 173.01 | 1,714,800 |
| 2026-11-13 | 174.11 | 174.62 | 170.71 | 173.96 | 1,415,200 |
| 2026-11-16 | 172.96 | 174.05 | 170.55 | 172.92 | 1,824,700 |
| 2026-11-17 | 173.37 | 174.36 | 171.34 | 172.22 | 2,464,081 |

Notable: none (latest volume is 1.3x the 5-day average, below the 1.5x mark).
Source: Yahoo Finance daily bars, 2026-11-11 to 2026-11-17, interval 1d.
```

---

## Reference Files

- `references/api_reference.md` — Complete yfinance API reference with code examples for every data category

Read the reference file when you need exact method signatures or edge case handling.

## Final Checklist (run before saying you are done)

- [ ] The code ran in this session and its output is what the answer quotes.
- [ ] Every number in the answer appears in that output; none came from memory.
- [ ] The first line answers the question and carries a date.
- [ ] The table has at most 20 rows and only the columns asked about.
- [ ] Source, period and interval are stated.
- [ ] Any ticker that returned no data is named, with the error.
