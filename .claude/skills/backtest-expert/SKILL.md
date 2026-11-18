---
name: backtest-expert
description: >
  Use when the user asks to backtest, validate, stress-test or judge a systematic
  (rule-based) trading strategy, or shares backtest results and asks whether they can
  be trusted: "is this backtest robust?", "is this overfit / curve-fitted?", "how much
  slippage should I assume?", "is the sample big enough?", "can I trade this?". Gives a
  fixed 6-step method (hypothesis, rules, initial test, stress tests, out-of-sample,
  scored decision) and a scoring script. Do not use for discretionary setups that need
  subjective judgement, for fetching price data (use yfinance-data), or for testing
  whether returns are only benchmark exposure (use residual-edge-analyzer).
---

# Backtest Expert

**Goal**: find strategies that break the least, not strategies that profit the most on paper.
**Why**: a strategy that survives pessimistic assumptions is more likely to work in live trading.

## Before You Start

- Python 3.9+ for the evaluation script. No API keys. No data downloads: the user supplies the metrics.
- This skill covers systematic strategies only: all rules fixed in advance, no "feel", tested on every
  historical case, news and macro context deliberately stripped out. If the setup needs subjective
  judgement, say this skill does not apply and stop.
- If the project's `CLAUDE.md` sets its own yardstick, deployment rule or list of forbidden studies,
  that file wins over this skill. Why: project rules record decisions the user has already made.

## Workflow

Do the six steps in order. Do not skip a step; if a step cannot be done, write "not done" and why.
Spend about 20% of the effort on steps 1-3 and 80% on steps 4-5. Why: the value is in trying to break the idea.

### Step 1. Write the hypothesis in one sentence

1. Write: "[which instruments] that [exact condition] tend to [outcome] because [reason]."
2. Example: "Stocks that gap up >3% on earnings and pull back to the previous day's close within the
   first hour provide a mean-reversion opportunity."
3. If you cannot write it in one sentence, ask the user to clarify and do not test.
   Why: an idea that cannot be stated cannot be proven wrong.

### Step 2. Write the rules with zero discretion

Write all five. Each must be checkable by code with no human judgement.

1. **Entry**: exact condition, timing, price type (for example, next day's open).
2. **Exit**: stop loss, profit target, time-based exit. Write "none" for any that is unused.
3. **Position sizing**: fixed dollars, % of portfolio, or volatility-adjusted.
4. **Filters**: market cap, volume, sector, volatility conditions.
5. **Universe**: which instruments are eligible.

Check: if any rule contains a word such as "strong", "looks", "roughly" or "good", replace it with a number.
Why: a subjective rule cannot be run the same way twice.

### Step 3. Run the initial backtest

1. Test at least 5 years; use 10 or more when the data exists.
2. The period must contain at least one bull market, one bear market, one high-volatility period and
   one low-volatility period.
3. Include commissions and conservative slippage from the first run.
4. Viability gate: if expectancy per trade is zero or negative after costs, go back to step 1.
   Do not stress-test it. Why: stress tests only make results worse.

### Step 4. Stress test the strategy

Run 4a to 4e in order. Record the result of each in a table (test, setting, result, pass/fail).

**4a. Parameter sensitivity**
1. Stop loss at 50%, 75%, 100%, 125% and 150% of the baseline value.
2. Profit target at 80%, 90%, 100%, 110% and 120% of the baseline value.
3. Entry and exit timing shifted by 15 to 30 minutes each way (intraday strategies; for daily-bar
   strategies write "not applicable").
4. Pass = profitable across a range (a plateau), for example any stop from 1.5% to 3.0%.
   Fail = profitable only at one value, for example a stop of exactly 2.13%.
   Why: a stable range points to a real edge; a narrow spike points to curve-fitting.

**4b. Execution friction**
1. Slippage at 1.5x to 2x the typical estimate.
2. Worst-case fills: buy at ask + 1 tick, sell at bid - 1 tick.
3. Order rejections and partial fills.
4. Commissions higher than the real schedule.
   Why: strategies that survive pessimistic costs often outperform live; those that do not were never profitable.

**4c. Time robustness**
1. Build a year-by-year table.
2. Pass = positive expectancy in more than half of the years.
3. Remove the best 1 or 2 periods and recompute. Pass = still positive.
   Why: an edge that lives in 1-2 exceptional periods is luck, not a rule.
4. Report each market regime separately.

**4d. Sample size**
- Fewer than 30 trades: not evaluable.
- 30 to 99: bare minimum.
- 100 to 199: preferred.
- 200 or more: high confidence.
- Small edges need large samples: a 5% edge per trade needs 100+ trades to tell from luck.

**4e. All cases, not chosen examples**
Test every instrument that met the rules, including the ones that failed. Never study hand-picked
winners. Why: chosen examples create survivorship bias and overstate the strategy.

### Step 5. Out-of-sample validation (walk-forward)

1. Optimize on a training period (for example, years 1-3).
2. Test on the next period (year 4) without changing anything.
3. Roll forward one period and repeat until the data ends.
4. Compare in-sample with out-of-sample performance.
5. Any one of these warning signs means the result is not Deploy:
   - out-of-sample performance below 50% of in-sample;
   - parameters must be re-optimized frequently to keep working;
   - optimal parameters change dramatically between periods.
   Why: all three mean the parameters fit past noise.

### Step 6. Score and decide

1. Collect the eight inputs: total trades, win rate %, average win %, average loss % (positive number),
   max drawdown %, years tested, number of tunable parameters, whether slippage was tested.
2. Run the script from the repository root:

   ```bash
   python3 .claude/skills/backtest-expert/scripts/evaluate_backtest.py \
     --total-trades 150 \
     --win-rate 62 \
     --avg-win-pct 1.8 \
     --avg-loss-pct 1.2 \
     --max-drawdown-pct 15 \
     --years-tested 8 \
     --num-parameters 3 \
     --slippage-tested \
     --output-dir reports/
   ```

   If the skill is installed elsewhere, replace `.claude/skills/backtest-expert` with this skill's folder.
   Add `--max-acceptable-drawdown-pct N` to set a personal limit below the hard 50% ceiling; a drawdown
   equal to the personal limit is allowed. Omit `--slippage-tested` if slippage was not modeled.
   Invalid inputs exit with status 1 and write no report.
3. Read `decision` and `blocking_reasons` first. They are authoritative.
   Why: the 0-100 `quality_score` is diagnostic only and cannot override a blocking gate.
4. Answer each question with yes or no plus the evidence:
   - Does the edge survive pessimistic assumptions (4b)?
   - Is performance stable across parameter variations (4a)?
   - Does it work in multiple market regimes (4c)?
   - Is the sample size sufficient (4d)?
   - Are the results realistic, not "too good to be true"?
5. State the decision:
   - **Deploy**: survives all stress tests and no gate blocks.
   - **Refine**: core logic sound, parameters need adjustment.
   - **Abandon**: fails stress tests or relies on fragile assumptions.

## Script Output

- `reports/backtest_eval_<timestamp>.json`: per-dimension scores, red flags, `decision`, `blocking_reasons`, verdict.
- `reports/backtest_eval_<timestamp>.md`: dimension table, key metrics, red flag details.

The script scores 5 dimensions, 20 points each: Sample Size, Expectancy, Risk Management, Robustness, Execution Realism.

Key JSON fields:

- `decision`: one of `DEPLOY`, `REFINE`, `ABANDON`, `REJECT`, `RISK_LIMIT_EXCEEDED`, `VALIDATION_REQUIRED`,
  `NOT_EVALUABLE`. Gate precedence: `NOT_EVALUABLE` (fewer than 30 trades or profit-factor overflow), then
  `REJECT` (non-positive expectancy or drawdown of 50% or more), then `RISK_LIMIT_EXCEEDED` (above the user's
  drawdown limit), then `VALIDATION_REQUIRED` (no slippage test, under 5 years, or `too_good`). Only when no
  gate blocks does the score give `DEPLOY`, `REFINE` or `ABANDON`.
- `blocking_reasons`: IDs of every gate that fired (`profit_factor_overflow`, `small_sample`,
  `negative_expectancy`, `zero_expectancy`, `excessive_drawdown`, `risk_limit_exceeded`, `no_slippage_test`,
  `short_test_period`, `too_good`). All are kept even when a higher-precedence gate sets the decision.
- `too_good`: win rate above 90% with max drawdown below 5%. Audit for look-ahead bias and data errors before adoption.
- `verdict`: conservative Deploy/Refine/Abandon compatibility field; never better than the score-based verdict.
- `profit_factor`: may be `null`. `profit_factor_status` says why: `FINITE` (numeric value), `NO_LOSSES`
  (gross profit, no gross loss), `UNDEFINED_ZERO_GROSS` (no gross profit and no gross loss), `OVERFLOW`
  (ratio overflow despite nonzero losses).

## Example of a Finished Answer

Produced by running the command in step 6 exactly as written:

```
Hypothesis: Stocks that gap up >3% on earnings and pull back to the previous day's close
            within the first hour provide a mean-reversion opportunity.
Inputs:     150 trades | win rate 62% | avg win 1.8% | avg loss 1.2% | max drawdown 15%
            8 years | 3 parameters | slippage tested
Script:     decision DEPLOY | blocking_reasons none | quality_score 81/100
            Sample Size 17/20 | Expectancy 11/20 | Risk Management 17/20
            Robustness 16/20 | Execution Realism 20/20
            Profit factor 2.45 | expectancy 0.660% per trade | red flags none
Questions:  pessimistic costs yes (slippage tested) | sample size yes (150 trades)
            parameter stability NOT CHECKED | regimes NOT CHECKED | realistic yes (no too_good flag)
Not done:   steps 4a, 4c and 5 (no parameter table, year-by-year table or walk-forward supplied).
Decision:   Refine, not Deploy, until 4a, 4c and 5 are supplied and pass.
```

## Common Failure Patterns

Name the pattern when you see it. Details and a diagnostic framework are in `references/failed_tests.md`.

1. **Parameter sensitivity**: works only with exact parameter values.
2. **Regime-specific**: great in some years, terrible in others.
3. **Slippage sensitivity**: unprofitable once realistic costs are added.
4. **Small sample**: too few trades for statistical confidence.
5. **Look-ahead bias**: "too good to be true" results.
6. **Over-optimization**: many parameters, poor out-of-sample results.

## Rules That Apply Throughout

- Intuition may generate the hypothesis; only data may validate it. Why: attachment to an idea bends
  how results are read.
- If the strategy needs "perfect context" to work, it is not robust enough for systematic trading.
- State the backtesting platform's known quirks (price interpolation, low-liquidity handling, data
  alignment) in the answer, or write "platform quirks not checked".

## Reference Files

- `references/methodology.md`: read when you need detail on a testing technique (stress testing,
  parameter sensitivity, slippage and friction modeling, sample size, regime classification, biases).
- `references/failed_tests.md`: read when a strategy fails a test (failure patterns with examples,
  case-study framework, red-flag checklist).

## Final Checklist (run before saying you are done)

- [ ] Hypothesis is one sentence.
- [ ] All five rule groups are written; no subjective words remain.
- [ ] Test period is 5+ years and the regimes covered are named.
- [ ] 4a to 4e each have a recorded result, or are marked "not done" with the reason.
- [ ] Walk-forward result is reported, or marked "not done".
- [ ] The script was run and exited 0; `decision` and `blocking_reasons` are quoted exactly.
- [ ] Every number in the answer comes from the user's inputs or the script output.
- [ ] The five questions are each answered yes, no or NOT CHECKED.
- [ ] The decision is not Deploy if any stress test or the walk-forward is "not done" or failed.
- [ ] The project's `CLAUDE.md` rules on yardstick and deployment were checked and followed.
