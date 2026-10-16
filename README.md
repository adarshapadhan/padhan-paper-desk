# Padhan Paper Desk — live scorecard

> **Paper trading only.** No wallet, no keys, no real money. Every trade is simulated on live Solana prices
> with realistic fees, slippage and rug-pull losses. Updated 2026-10-16 12:09 UTC · day 7.1

## Verdict: **TOO EARLY — keep watching**

| | Invest only if ALL of these hold (rules fixed before the test started) |
|---|---|
| ❌ | At least 14 days live and 100 closed desk trades |
| ❌ | Desk is net profitable after all fees, slippage and rugs |
| ❌ | Profit factor (gross wins / gross losses) is 1.3 or better |
| ❌ | Worst peak-to-trough drawdown is 30% or less |
| ❌ | Desk beats the random control book by 10+ percentage points |
| ❌ | Still profitable after removing its 3 best trades |

## Books (each started with $1,000 paper)

| | AI desk | Random control |
|---|---:|---:|
| Equity | $430.06 | $711.46 |
| Return | -56.99% | -28.85% |
| Closed trades | 201 | 96 |
| Win rate | 37.8% | 28.1% |
| Avg win / avg loss | +32.1% / -35.4% | +34.1% / -28.5% |
| Profit factor | 0.55 | 0.46 |
| Max drawdown | 58.5% | 30.4% |
| Profit without top 3 trades | $-651.65 | $-368.29 |
| Rug / liquidity-pull exits | 7 | 4 |
| Open positions now | 2 | 3 |

Tokens screened: **811,136** across 10,064 scans. Top reasons the safety agent (LUNA) said no:
dex (342,220), liq_low (221,793), too_old (110,978), odd_quote (67,369), lp_unlocked (14,189), too_new (5,430), fdv_liq_thin (3,989), rug_danger (3,654)

## How it works
Six agents, one job each — **RADAR** finds new tokens · **LUNA** blocks unsafe ones (liquidity, age, RugCheck: mint/freeze
authority, LP lock, holder concentration; fails closed) · **ATLAS** reads buy/sell pressure and volume acceleration ·
**VEGA** reads attention (socials, boosts, trending) · **ORION** reads momentum · **TITAN** sizes (4–6% of equity, ≤1% of pool,
max 6 positions, −10% daily stop) · **NOVA** simulates fills (pool price impact + 1% slippage + 0.25% DEX fee + $0.30
priority fee per side). Exits: −25% stop, sell half at +40%, 20% trailing stop on the rest, 4-hour time limit,
emergency exit if liquidity drops 50%.

The **control book** buys a *random* token that passed the same safety gate every time the desk buys, same size, same exits.
If the desk can't beat random picks, the "AI" adds nothing.

Files: `data/trades.csv` (every closed trade) · `data/equity.csv` (5-minute equity) · `data/state.json` (open positions).
