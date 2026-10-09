# Padhan Paper Desk — live scorecard

> **Paper trading only.** No wallet, no keys, no real money. Every trade is simulated on live Solana prices
> with realistic fees, slippage and rug-pull losses. Updated 2026-10-09 14:04 UTC · day 0.2

## Verdict: **TOO EARLY — keep watching**

| | Invest only if ALL of these hold (rules fixed before the test started) |
|---|---|
| ❌ | At least 14 days live and 100 closed desk trades |
| ❌ | Desk is net profitable after all fees, slippage and rugs |
| ❌ | Profit factor (gross wins / gross losses) is 1.3 or better |
| ✅ | Worst peak-to-trough drawdown is 30% or less |
| ❌ | Desk beats the random control book by 10+ percentage points |
| ❌ | Still profitable after removing its 3 best trades |

## Books (each started with $1,000 paper)

| | AI desk | Random control |
|---|---:|---:|
| Equity | $892.94 | $966.03 |
| Return | -10.71% | -3.40% |
| Closed trades | 16 | 7 |
| Win rate | 43.8% | 14.3% |
| Avg win / avg loss | +29.7% / -48.8% | +27.3% / -29.4% |
| Profit factor | 0.46 | 0.16 |
| Max drawdown | 10.8% | 4.1% |
| Profit without top 3 trades | $-146.33 | $-48.61 |
| Rug / liquidity-pull exits | 2 | 0 |
| Open positions now | 1 | 2 |

Tokens screened: **18,406** across 240 scans. Top reasons the safety agent (LUNA) said no:
dex (7,126), liq_low (7,017), too_old (2,175), odd_quote (1,714), too_new (94), rug_danger (62), fdv_low (5), fdv_liq_thin (2)

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
