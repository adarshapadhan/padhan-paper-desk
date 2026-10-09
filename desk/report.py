#!/usr/bin/env python3
"""Builds the scorecard: README.md (repo front page) + docs/data.json (dashboard feed).

The invest / don't-invest rules are fixed here BEFORE results come in, so the
answer can't be bent to fit the numbers afterwards.
"""
import argparse
import csv
import json
import os
import time

RULES = [
    ("sample", "At least 14 days live and 100 closed desk trades"),
    ("profit", "Desk is net profitable after all fees, slippage and rugs"),
    ("pf", "Profit factor (gross wins / gross losses) is 1.3 or better"),
    ("dd", "Worst peak-to-trough drawdown is 30% or less"),
    ("edge", "Desk beats the random control book by 10+ percentage points"),
    ("luck", "Still profitable after removing its 3 best trades"),
]


def read_csv(path):
    if not os.path.exists(path):
        return []
    with open(path, newline="") as f:
        return list(csv.DictReader(f))


def f(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return 0.0


def book_stats(trades, eq_rows, key, start):
    pnl = [f(t["pnl_usd"]) for t in trades]
    wins = [p for p in pnl if p > 0]
    losses = [p for p in pnl if p <= 0]
    equity = f(eq_rows[-1][key]) if eq_rows else start
    peak, dd = start, 0.0
    for r in eq_rows:
        e = f(r[key])
        peak = max(peak, e)
        dd = max(dd, 1 - e / peak if peak else 0)
    top3 = sum(sorted(pnl, reverse=True)[:3]) if pnl else 0
    reasons = {}
    for t in trades:
        reasons[t["exit_reason"]] = reasons.get(t["exit_reason"], 0) + 1
    return {
        "equity": round(equity, 2),
        "return_pct": round((equity / start - 1) * 100, 2),
        "trades": len(pnl),
        "win_rate": round(len(wins) / len(pnl) * 100, 1) if pnl else 0,
        "avg_win_pct": round(sum(f(t["pnl_pct"]) for t in trades if f(t["pnl_usd"]) > 0) / len(wins), 1) if wins else 0,
        "avg_loss_pct": round(sum(f(t["pnl_pct"]) for t in trades if f(t["pnl_usd"]) <= 0) / len(losses), 1) if losses else 0,
        "profit_factor": round(sum(wins) / abs(sum(losses)), 2) if losses and sum(losses) else (99.0 if wins else 0),
        "max_dd_pct": round(dd * 100, 1),
        "realized_usd": round(sum(pnl), 2),
        "realized_ex_top3_usd": round(sum(pnl) - top3, 2),
        "best_trade_usd": round(max(pnl), 2) if pnl else 0,
        "worst_trade_usd": round(min(pnl), 2) if pnl else 0,
        "rug_exits": reasons.get("liquidity_pulled", 0) + reasons.get("vanished_rug", 0),
        "exit_reasons": reasons,
    }


def verdict(days, desk, ctrl):
    checks = {
        "sample": days >= 14 and desk["trades"] >= 100,
        "profit": desk["return_pct"] > 0,
        "pf": desk["profit_factor"] >= 1.3,
        "dd": desk["max_dd_pct"] <= 30,
        "edge": desk["return_pct"] - ctrl["return_pct"] >= 10,
        "luck": desk["realized_ex_top3_usd"] > 0,
    }
    if not checks["sample"]:
        v = "TOO EARLY — keep watching"
    elif all(checks.values()):
        v = "PASSED — eligible for a small real-money pilot (only with Boss's consent)"
    else:
        v = "DO NOT INVEST — failed: " + ", ".join(k for k, ok in checks.items() if not ok)
    return v, checks


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", default="data")
    ap.add_argument("--out", default=".")
    a = ap.parse_args()
    st_path = os.path.join(a.data, "state.json")
    if not os.path.exists(st_path):
        return
    st = json.load(open(st_path))
    start = 1000.0
    trades = read_csv(os.path.join(a.data, "trades.csv"))
    eq = read_csv(os.path.join(a.data, "equity.csv"))
    days = (time.time() - st["started"]) / 86400
    desk = book_stats([t for t in trades if t["book"] == "desk"], eq, "desk_equity", start)
    ctrl = book_stats([t for t in trades if t["book"] == "control"], eq, "control_equity", start)
    v, checks = verdict(days, desk, ctrl)
    open_pos = [{"book": bn, "symbol": p["symbol"], "url": p.get("url"), "opened": time.strftime("%Y-%m-%d %H:%M", time.gmtime(p["opened"])),
                 "cost": round(p["cost"], 2), "entry": p["entry_price"], "last": p["last_price"],
                 "chg_pct": round((p["last_price"] / p["entry_price"] - 1) * 100, 1), "score": p["score"]}
                for bn, b in st["books"].items() for p in b["positions"].values()]
    data = {
        "updated_utc": time.strftime("%Y-%m-%d %H:%M", time.gmtime()), "days": round(days, 2),
        "verdict": v, "checks": checks, "rules": RULES, "desk": desk, "control": ctrl,
        "scans": st["stats"]["scans"], "candidates_seen": st["stats"]["candidates_seen"],
        "rejections": st["stats"]["rejections"], "open_positions": open_pos,
        "recent_trades": trades[-40:][::-1],
        "equity": [{"t": r["utc"], "d": f(r["desk_equity"]), "c": f(r["control_equity"])} for r in eq][-2000:],
    }
    os.makedirs(os.path.join(a.out, "docs"), exist_ok=True)
    with open(os.path.join(a.out, "docs", "data.json"), "w") as fh:
        json.dump(data, fh)

    tick = lambda ok: "✅" if ok else "❌"
    rows = "\n".join(f"| {tick(checks[k])} | {txt} |" for k, txt in RULES)
    rej = sorted(st["stats"]["rejections"].items(), key=lambda x: -x[1])[:8]
    md = f"""# Padhan Paper Desk — live scorecard

> **Paper trading only.** No wallet, no keys, no real money. Every trade is simulated on live Solana prices
> with realistic fees, slippage and rug-pull losses. Updated {data['updated_utc']} UTC · day {days:.1f}

## Verdict: **{v}**

| | Invest only if ALL of these hold (rules fixed before the test started) |
|---|---|
{rows}

## Books (each started with $1,000 paper)

| | AI desk | Random control |
|---|---:|---:|
| Equity | ${desk['equity']:,.2f} | ${ctrl['equity']:,.2f} |
| Return | {desk['return_pct']:+.2f}% | {ctrl['return_pct']:+.2f}% |
| Closed trades | {desk['trades']} | {ctrl['trades']} |
| Win rate | {desk['win_rate']}% | {ctrl['win_rate']}% |
| Avg win / avg loss | {desk['avg_win_pct']:+}% / {desk['avg_loss_pct']:+}% | {ctrl['avg_win_pct']:+}% / {ctrl['avg_loss_pct']:+}% |
| Profit factor | {desk['profit_factor']} | {ctrl['profit_factor']} |
| Max drawdown | {desk['max_dd_pct']}% | {ctrl['max_dd_pct']}% |
| Profit without top 3 trades | ${desk['realized_ex_top3_usd']:,.2f} | ${ctrl['realized_ex_top3_usd']:,.2f} |
| Rug / liquidity-pull exits | {desk['rug_exits']} | {ctrl['rug_exits']} |
| Open positions now | {sum(1 for p in open_pos if p['book']=='desk')} | {sum(1 for p in open_pos if p['book']=='control')} |

Tokens screened: **{data['candidates_seen']:,}** across {data['scans']:,} scans. Top reasons the safety agent (LUNA) said no:
{', '.join(f'{k} ({n:,})' for k, n in rej) or '—'}

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
"""
    with open(os.path.join(a.out, "README.md"), "w") as fh:
        fh.write(md)


if __name__ == "__main__":
    main()
