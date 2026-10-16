# Padhan Paper Desk — live scorecard

> **Paper trading only.** No wallet, no keys, no real money. Every trade is simulated on live Solana prices
> with realistic fees, slippage and rug-pull losses. Updated 2026-10-16 09:22 UTC · day 7.0

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
| Equity | $422.43 | $697.32 |
| Return | -57.76% | -30.27% |
| Closed trades | 199 | 96 |
| Win rate | 37.2% | 28.1% |
| Avg win / avg loss | +32.4% / -35.4% | +34.1% / -28.5% |
| Profit factor | 0.54 | 0.46 |
| Max drawdown | 58.5% | 30.4% |
| Profit without top 3 trades | $-659.27 | $-368.29 |
| Rug / liquidity-pull exits | 7 | 4 |
| Open positions now | 0 | 0 |

Tokens screened: **798,434** across 9,899 scans. Top reasons the safety agent (LUNA) said no:
dex (335,969), liq_low (219,421), too_old (108,824), odd_quote (65,977), lp_unlocked (14,016), too_new (5,327), fdv_liq_thin (3,824), rug_danger (3,654)

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
