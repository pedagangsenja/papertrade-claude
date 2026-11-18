---
name: residual-edge-analyzer
description: Separate a strategy return series into declared baseline exposure and residual edge with returns-based OLS attribution, HAC inference, rolling stability, alternate-baseline sensitivity, and regime breakdowns. Use when evaluating whether backtest, out-of-sample, or live returns contain independent alpha beyond market, equal-weight, momentum, sector, or user-supplied factor returns; when explaining whether a drawdown came from baseline exposure or strategy-specific behavior; or when a strategy needs an attribution quality gate after backtesting. Do not use for holdings-based Brinson attribution, feature-level Shapley explanations, or analysis from summary metrics without a dated return series.
---

# Residual Edge Analyzer

## Overview

Test whether a strategy's apparent performance survives explicit comparison with
predeclared baseline return series. Produce an auditable JSON artifact and a concise
Markdown report without fetching data or changing trading exposure.

Treat this as a falsification gate after `backtest-expert`, not as trade authorization.

## Prerequisites

- Use Python 3.9+.
- Prepare one CSV containing an ISO date, strategy return, and every baseline return on
  the same row.
- Prepare a JSON specification following `references/input-contract.md` in this skill's folder
  (copy the JSON example there and change the column names).
- Supply actual period returns. Do not substitute CAGR, Sharpe, cumulative P&L, or other
  summary metrics.

## Workflow

### 1. Define the question before inspecting results

State the claimed independent edge in one sentence. Select a primary baseline that is a
plausible simple copy of the strategy, then select at least one alternate baseline model.

Record these declarations in the config:

- `baseline_selection: predeclared`
- `strategy_return_basis` and `baseline_return_basis`: both `gross` or both `net`
- `analysis_scope`: `out_of_sample`, `live`, or `in_sample`
- `universe_data`: `point_in_time`, `current_constituents`, or `not_applicable`

Every declaration is mandatory for a decision-grade verdict. Omitting one is treated as
undeclared, not as benign, and drops the report to `REVIEW_REQUIRED`. `not_applicable`
exists so that a baseline with no universe membership can be declared explicitly rather
than left blank.

Do not choose a baseline because it gives the preferred residual result.

### 2. Validate the return-series contract

Require:

- unique ISO dates;
- finite numeric returns greater than -100%;
- identical frequency and cost basis across strategy and baselines;
- point-in-time membership for same-universe equal-weight or momentum baselines;
- regime labels defined independently of the loss periods being explained.

Stop if the input lacks a dated strategy return series. Report summary-only input as
insufficient rather than inventing observations.

### 3. Run the analyzer

Run from the repository root:

```bash
python3 .claude/skills/residual-edge-analyzer/scripts/analyze_residual_edge.py \
  --input reports/strategy_returns.csv \
  --config reports/residual_edge_config.json \
  --output-json reports/residual_edge_report.json \
  --output-markdown reports/residual_edge_report.md
```

If the skill is installed elsewhere, replace `.claude/skills/residual-edge-analyzer` with this skill's folder.
The script prints the two files it wrote and exits 0. If it exits with any other status, read the error,
fix the CSV or the config, and run it again. Do not write a report by hand.
Why: a hand-written report has no audit trail.

The script runs the predeclared primary model and all sensitivity models in one execution.
It uses an intercept OLS model and HAC/Newey-West standard errors. It reports the residual
edge ratio as annualized alpha divided by annualized residual volatility; do not calculate
a Sharpe ratio from raw OLS residual mean because an intercept makes that mean zero.

### 4. Interpret the evidence

Use the four statuses as diagnostic labels:

- `RESIDUAL_EDGE`: alpha, residual edge ratio, and rolling stability clear configured
  thresholds.
- `BASELINE_EXPLAINED`: baseline R-squared is high while residual evidence is weak.
- `RESIDUAL_FRAGILE`: results fail one or more robustness gates or change across declared
  baseline models. Also use this status when rolling analysis is disabled, unavailable,
  incomplete, or no sensitivity model was supplied.
- `INSUFFICIENT_EVIDENCE`: the sample is below the configured minimum.

Read `decision_eligibility` separately. A statistically interesting result remains
`REVIEW_REQUIRED` when critical provenance, cost-basis, sample, or multicollinearity
warnings exist, when rolling evidence is unavailable, or when no alternate baseline was
tested.

Inspect all six, in this order, and quote each value from the report:

1. primary and sensitivity-model status;
2. annualized alpha and HAC t-stat;
3. residual edge ratio and residual autocorrelation;
4. rolling alpha stability;
5. VIF for multi-factor models;
6. active-return breakdown across predeclared regimes.

### 5. Hand off findings

- Send baseline-choice, OOS, and stability findings back to `backtest-expert`.
- Send recurring residual failure regimes to `signal-postmortem`.
- Pass only evidence and operating constraints to `trade-performance-coach`.
- If one of these skills is not installed, write the finding under a "Hand-off" heading in your answer instead.
  Why: the finding must not be lost because the receiving skill is missing.
- Never change position size, exposure, or orders automatically.
  Why: this skill produces evidence; a person decides what to trade.

## Boundaries

- Do not call this holdings-based contribution analysis. Brinson allocation, selection,
  and interaction effects require historical holdings, benchmark weights, and constituent
  returns.
- Do not claim stock-selection alpha from a market-index-only baseline.
- Do not build equal-weight baselines from current constituents and label them
  point-in-time.
- Do not interpret in-sample residual edge as confirmed alpha.
- Do not mine many regime definitions after seeing losses. Predeclare a small set and
  confirm findings out of sample.
- Do not assume high R-squared makes a strategy worthless; capacity, tail behavior, costs,
  and implementation value require separate evidence.

## Example of a Finished Answer

Produced by the command in step 3 on a 300-day daily series with the config from `references/input-contract.md`
(`universe_data: not_applicable`):

```
Claim tested: the strategy earns return beyond its market exposure.
Status: RESIDUAL_EDGE | Decision eligibility: ELIGIBLE
Period: 2025-01-02 to 2026-02-25 (300 observations) | Primary model: market

1. Model status: market RESIDUAL_EDGE | equal_weight RESIDUAL_EDGE | market_plus_momentum RESIDUAL_EDGE
2. Annualized alpha 19.72%, HAC t-stat 2.034
3. Residual edge ratio 2.116 (annualized residual volatility 9.32%)
4. Rolling alpha stability: alpha positive in 88.7% of 238 rolling windows (threshold 60%)
5. VIF: 1.000 (market_return loading 0.8209, R-squared 0.6286)
6. Regimes (volatility_regime): high N=79, active return 21.84% | low N=221, active return 18.96%

Evidence warnings: none.
Limits: 300 observations is about 14 months; confirm on untouched out-of-sample or live data.
        This report does not authorize a trade or an exposure change.
Hand-off: baseline choice and stability findings go to backtest-expert.
```

## Final Checklist (run before saying you are done)

- [ ] The claimed edge is written in one sentence, and the baselines were chosen before looking at results.
- [ ] All five declarations are in the config (`baseline_selection`, both return bases, `analysis_scope`, `universe_data`).
- [ ] The script ran and exited 0; the JSON and Markdown files exist.
- [ ] `status` and `decision_eligibility` are quoted exactly as the report gives them.
- [ ] All six inspection items are reported with their values.
- [ ] Every evidence warning in the report is repeated in the answer.
- [ ] No rule under "Boundaries" is broken (for example, in-sample edge is not called confirmed alpha).
- [ ] The answer says the report does not authorize a trade.

## Resources

- `scripts/analyze_residual_edge.py` — deterministic CSV-to-JSON/Markdown analyzer.
- `references/input-contract.md` — CSV/config contract and runnable example.
- `references/methodology.md` — statistical definitions, interpretation, and limitations.
