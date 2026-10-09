#!/usr/bin/env python3
"""
Padhan Paper Desk — a PAPER-ONLY multi-agent Solana meme-coin trading desk.

It copies the structure of the "24/7 AI trading desk" reel so the idea can be
tested honestly before any money is risked. No wallet, no keys, no real orders:
every trade is simulated against live market prices with realistic costs.

Agents (one job each)
  RADAR  - discovers fresh tokens (DexScreener profiles/boosts, GeckoTerminal new + trending pools)
  LUNA   - safety gate: liquidity, age, FDV, RugCheck (mint/freeze authority, LP lock, holders). Fails closed.
  ATLAS  - money flow: buy/sell pressure, transaction count, volume acceleration
  VEGA   - attention/narrative: socials, website, paid boosts, trending lists
  ORION  - momentum: short-term price action, not too early, not too late
  TITAN  - sizing and risk: position size, liquidity cap, max positions, daily loss stop
  NOVA   - execution simulator: slippage from pool depth, DEX fees, priority fees, exits

Two books run side by side:
  desk    - trades only what the agents score highest
  control - for every desk entry, buys a RANDOM token that also passed LUNA's safety gate,
            same size, same exit rules. If the desk can't beat the control, the "AI" adds nothing.

Standard library only, so it runs unchanged on GitHub Actions or a Windows PC.
"""
import argparse
import csv
import json
import os
import random
import sys
import time
import urllib.error
import urllib.request

# ----------------------------------------------------------------------------- config
CFG = {
    "start_cash": 1000.0,          # paper USD per book
    "scan_every_s": 60,            # discovery cycle
    "tick_every_s": 15,            # open-position price checks
    # LUNA hard gates
    "min_liq": 25_000, "max_liq": 5_000_000,
    "min_age_min": 15, "max_age_h": 72,
    "min_fdv": 50_000, "max_fdv_to_liq": 40,
    "min_lp_locked_pct": 80,
    "allowed_dex": {"raydium", "pumpswap", "meteora", "orca", "meteoradbc", "raydium-clmm", "raydium-cp"},
    "max_rug_checks_per_scan": 6,
    # entry
    "entry_score": 65,
    "token_cooldown_h": 12,
    # TITAN
    "base_risk_frac": 0.04,        # 4% of equity per position at score 65, up to 6% at 100
    "max_risk_frac": 0.06,
    "max_frac_of_liq": 0.01,       # never more than 1% of pool liquidity
    "max_positions": 6,
    "daily_loss_stop": 0.10,       # stop new entries for the UTC day after -10%
    "min_order_usd": 5,
    # NOVA costs
    "dex_fee": 0.0025,             # per side
    "priority_fee_usd": 0.30,      # per transaction (priority + Jito tip), realistic for sniping
    "base_slippage": 0.010,        # per side, on top of price impact
    # exits
    "tp1_gain": 0.40, "tp1_sell_frac": 0.5,
    "trail_pct": 0.20,
    "stop_loss": 0.25,
    "max_hold_h": 4,
    "rug_liq_drop": 0.50,          # liquidity falls 50% from entry -> emergency exit
    "rug_extra_slippage": 0.30,
}

UA = {"User-Agent": "padhan-paper-desk/1.0 (paper trading research)", "Accept": "application/json"}
GT_HDR = dict(UA, Accept="application/json;version=20230302")

DS = "https://api.dexscreener.com"
GT = "https://api.geckoterminal.com/api/v2"
RC = "https://api.rugcheck.xyz/v1"


# ----------------------------------------------------------------------------- plumbing (swappable in tests)
def _http_get_json(url, headers=None, timeout=15):
    req = urllib.request.Request(url, headers=headers or UA)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode("utf-8"))


FETCH = _http_get_json
NOW = time.time
SLEEP = time.sleep
LOG_LINES = []


def log(*a):
    line = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(NOW())) + "Z " + " ".join(str(x) for x in a)
    LOG_LINES.append(line)
    print(line, flush=True)


def get(url, headers=None, default=None):
    for attempt in range(3):
        try:
            return FETCH(url, headers)
        except urllib.error.HTTPError as e:
            if e.code == 429:
                SLEEP(5 * (attempt + 1))
                continue
            if e.code in (404,):
                return default
            log("http", e.code, url[:90])
        except Exception as e:  # network blips must never kill the desk
            log("net-err", type(e).__name__, url[:90])
        SLEEP(1 + attempt)
    return default


def fnum(x, d=0.0):
    try:
        v = float(x)
        return v if v == v else d
    except (TypeError, ValueError):
        return d


def clamp(x, lo=0.0, hi=100.0):
    return max(lo, min(hi, x))


# ----------------------------------------------------------------------------- RADAR: discovery
def radar():
    """Return {mint: {"sources": set, "boosted": bool, "trending": bool}}."""
    found = {}

    def add(mint, src, **flags):
        if not mint or not isinstance(mint, str):
            return
        c = found.setdefault(mint, {"sources": set(), "boosted": False, "trending": False})
        c["sources"].add(src)
        for k, v in flags.items():
            c[k] = c[k] or v

    for path, src, flags in (
        ("/token-profiles/latest/v1", "ds_profile", {}),
        ("/token-boosts/latest/v1", "ds_boost", {"boosted": True}),
        ("/token-boosts/top/v1", "ds_boost_top", {"boosted": True}),
    ):
        data = get(DS + path, default=[]) or []
        if isinstance(data, dict):
            data = [data]
        for it in data:
            if isinstance(it, dict) and it.get("chainId") == "solana":
                add(it.get("tokenAddress"), src, **flags)

    for path, src, flags in (
        ("/networks/solana/new_pools?page=1", "gt_new", {}),
        ("/networks/solana/trending_pools?page=1", "gt_trending", {"trending": True}),
    ):
        data = get(GT + path, GT_HDR, default={}) or {}
        for p in data.get("data", []) if isinstance(data, dict) else []:
            try:
                tid = p["relationships"]["base_token"]["data"]["id"]
            except (KeyError, TypeError):
                continue
            if tid.startswith("solana_"):
                mint = tid[len("solana_"):]
                if mint != "So11111111111111111111111111111111111111112":
                    add(mint, src, **flags)
    return found


BP_STATUS = {"ok": True}


def best_pairs(mints):
    """DexScreener pairs for up to 30 mints per call; keep the deepest Solana pair per mint."""
    out = {}
    mints = list(mints)
    for i in range(0, len(mints), 30):
        chunk = mints[i:i + 30]
        data = get(DS + "/tokens/v1/solana/" + ",".join(chunk), default=None)
        if data is None:
            BP_STATUS["ok"] = False
            data = []
        if isinstance(data, dict):
            data = data.get("pairs") or []
        for p in data:
            if not isinstance(p, dict) or p.get("chainId") != "solana":
                continue
            mint = (p.get("baseToken") or {}).get("address")
            if mint not in chunk:
                continue
            liq = fnum((p.get("liquidity") or {}).get("usd"))
            if mint not in out or liq > fnum((out[mint].get("liquidity") or {}).get("usd")):
                out[mint] = p
    return out


# ----------------------------------------------------------------------------- LUNA: safety
def luna_pregate(p, now):
    """Cheap checks from pair data. Returns reason string or None if passed."""
    liq = fnum((p.get("liquidity") or {}).get("usd"))
    fdv = fnum(p.get("fdv") or p.get("marketCap"))
    created = fnum(p.get("pairCreatedAt")) / 1000.0
    age_min = (now - created) / 60 if created else -1
    if p.get("dexId") not in CFG["allowed_dex"]:
        return "dex:" + str(p.get("dexId"))
    if fnum(p.get("priceUsd")) <= 0:
        return "no_price"
    if liq < CFG["min_liq"]:
        return "liq_low"
    if liq > CFG["max_liq"]:
        return "liq_high"
    if age_min < 0 or age_min < CFG["min_age_min"]:
        return "too_new"
    if age_min > CFG["max_age_h"] * 60:
        return "too_old"
    if fdv < CFG["min_fdv"]:
        return "fdv_low"
    if fdv / max(liq, 1) > CFG["max_fdv_to_liq"]:
        return "fdv_liq_thin"
    return None


RUG_CACHE = {}


def luna_rugcheck(mint, now):
    """RugCheck summary. Fails closed: if we can't verify, we don't trade."""
    hit = RUG_CACHE.get(mint)
    if hit and now - hit[0] < 1800:
        return hit[1]
    rep = get(f"{RC}/tokens/{mint}/report/summary", default=None)
    if not isinstance(rep, dict):
        res = "rugcheck_unavailable"
    else:
        dangers = [r.get("name", "?") for r in rep.get("risks") or []
                   if isinstance(r, dict) and str(r.get("level", "")).lower() == "danger"]
        names = " ".join(str(r.get("name", "")).lower() for r in rep.get("risks") or [] if isinstance(r, dict))
        lp = rep.get("lpLockedPct")
        if dangers:
            res = "rug_danger:" + "|".join(dangers)[:80]
        elif "mint authority" in names or "freeze authority" in names:
            res = "authority_enabled"
        elif lp is not None and fnum(lp) < CFG["min_lp_locked_pct"]:
            res = f"lp_unlocked:{fnum(lp):.0f}%"
        else:
            res = None
    RUG_CACHE[mint] = (now, res)
    return res


# ----------------------------------------------------------------------------- ATLAS / VEGA / ORION: scoring
def atlas(p):
    t5 = (p.get("txns") or {}).get("m5") or {}
    b, s = fnum(t5.get("buys")), fnum(t5.get("sells"))
    n = b + s
    ratio = b / n if n else 0
    vol = p.get("volume") or {}
    accel = fnum(vol.get("m5")) * 12 / max(fnum(vol.get("h1")), 1.0)
    sc = clamp((ratio - 0.45) / 0.25 * 50) + clamp((n - 10) / 60 * 25) + clamp((accel - 0.8) / 1.7 * 25)
    return clamp(sc), {"buy_ratio": round(ratio, 2), "tx_m5": int(n), "vol_accel": round(accel, 2)}


def vega(p, cand):
    info = p.get("info") or {}
    socials = {str(s.get("type", "")).lower() for s in info.get("socials") or [] if isinstance(s, dict)}
    sc = 0
    sc += 25 if "twitter" in socials or "x" in socials else 0
    sc += 15 if "telegram" in socials else 0
    sc += 15 if info.get("websites") else 0
    sc += 20 if cand.get("boosted") or fnum((p.get("boosts") or {}).get("active")) > 0 else 0
    sc += 25 if cand.get("trending") else 0
    return clamp(sc), {"socials": sorted(socials), "boosted": bool(cand.get("boosted")),
                       "trending": bool(cand.get("trending"))}


def orion(p):
    pc = p.get("priceChange") or {}
    m5, h1 = fnum(pc.get("m5")), fnum(pc.get("h1"))
    # sweet spot: rising now (+2..+25% in 5m), not already a vertical blow-off
    s5 = 0 if m5 <= 0 else (clamp(m5 / 8 * 60) if m5 <= 8 else clamp(60 - (m5 - 25) * 3) if m5 > 25 else 60)
    s1 = 40 if 0 <= h1 <= 150 else (20 if 150 < h1 <= 400 else 0)
    return clamp(s5 + s1), {"m5": m5, "h1": h1}


def luna_quality(p):
    liq = fnum((p.get("liquidity") or {}).get("usd"))
    fdv = fnum(p.get("fdv") or p.get("marketCap"))
    turnover = fnum((p.get("volume") or {}).get("h1")) / max(liq, 1)
    sc = clamp((liq - 25_000) / 175_000 * 50) + clamp(50 - (fdv / max(liq, 1) - 5) * 2) * 0.5 + clamp(turnover * 25, 0, 25)
    return clamp(sc), {"liq": round(liq), "fdv": round(fdv), "turnover_h1": round(turnover, 2)}


def score(p, cand):
    a, ad = atlas(p)
    v, vd = vega(p, cand)
    o, od = orion(p)
    q, qd = luna_quality(p)
    total = 0.30 * a + 0.25 * v + 0.25 * o + 0.20 * q
    return round(total, 1), {"atlas": round(a), "vega": round(v), "orion": round(o), "luna": round(q),
                             **ad, **vd, **od, **qd}


# ----------------------------------------------------------------------------- NOVA: execution model
def impact(size_usd, liq_usd):
    """Constant-product price impact for a trade of size_usd into a pool with liq_usd (both sides)."""
    side = max(liq_usd / 2.0, 1.0)
    return size_usd / (side + size_usd)


def fill_buy(price, size_usd, liq):
    slip = CFG["base_slippage"] + impact(size_usd, liq)
    eff_price = price * (1 + slip)
    spend = size_usd - CFG["priority_fee_usd"]
    qty = spend * (1 - CFG["dex_fee"]) / eff_price
    return qty, eff_price, size_usd


def fill_sell(price, qty, liq, extra_slip=0.0):
    gross = qty * price
    slip = CFG["base_slippage"] + impact(gross, liq) + extra_slip
    proceeds = gross * (1 - min(slip, 0.99)) * (1 - CFG["dex_fee"]) - CFG["priority_fee_usd"]
    return max(proceeds, 0.0)


# ----------------------------------------------------------------------------- books & state
def new_book(name):
    return {"name": name, "cash": CFG["start_cash"], "positions": {}, "realized": 0.0,
            "fees_est": 0.0, "day": "", "day_start_equity": CFG["start_cash"], "halted_day": "",
            "trades": 0, "peak_equity": CFG["start_cash"], "max_dd": 0.0}


def load_state(d):
    path = os.path.join(d, "state.json")
    if os.path.exists(path):
        with open(path) as f:
            st = json.load(f)
    else:
        st = {"started": NOW(), "books": {"desk": new_book("desk"), "control": new_book("control")},
              "cooldown": {}, "stats": {"scans": 0, "candidates_seen": 0, "rejections": {}}, "last_prices": {}}
    return st


def save_state(d, st):
    os.makedirs(d, exist_ok=True)
    tmp = os.path.join(d, "state.json.tmp")
    with open(tmp, "w") as f:
        json.dump(st, f, indent=1, default=list)
    os.replace(tmp, os.path.join(d, "state.json"))


def append_csv(d, name, row, header):
    path = os.path.join(d, name)
    new = not os.path.exists(path)
    with open(path, "a", newline="") as f:
        w = csv.writer(f)
        if new:
            w.writerow(header)
        w.writerow(row)


TRADE_HDR = ["book", "mint", "symbol", "opened_utc", "closed_utc", "hold_min", "score", "cost_usd",
             "proceeds_usd", "pnl_usd", "pnl_pct", "exit_reason", "entry_price", "exit_price", "peak_price"]
EQ_HDR = ["utc", "desk_equity", "control_equity", "desk_open", "control_open"]


def book_equity(b, prices):
    eq = b["cash"]
    for mint, pos in b["positions"].items():
        px, liq = prices.get(mint, (pos["last_price"], pos["last_liq"]))
        eq += fill_sell(px, pos["qty"], liq)
    return eq


def utc(ts):
    return time.strftime("%Y-%m-%d %H:%M", time.gmtime(ts))


# ----------------------------------------------------------------------------- TITAN: sizing / entries
def titan_size(b, sc, liq, equity):
    if len(b["positions"]) >= CFG["max_positions"]:
        return 0, "max_positions"
    if b["halted_day"] == b["day"]:
        return 0, "daily_loss_stop"
    frac = CFG["base_risk_frac"] + (CFG["max_risk_frac"] - CFG["base_risk_frac"]) * clamp((sc - CFG["entry_score"]) / (100 - CFG["entry_score"]), 0, 1)
    size = min(equity * frac, liq * CFG["max_frac_of_liq"], b["cash"])
    if size < CFG["min_order_usd"]:
        return 0, "too_small"
    return round(size, 2), None


def open_pos(b, mint, p, sc, detail, now, size):
    price = fnum(p.get("priceUsd"))
    liq = fnum((p.get("liquidity") or {}).get("usd"))
    qty, eff, cost = fill_buy(price, size, liq)
    b["cash"] -= cost
    b["positions"][mint] = {
        "symbol": (p.get("baseToken") or {}).get("symbol", "?"), "pair": p.get("pairAddress"),
        "url": p.get("url"), "opened": now, "qty": qty, "qty0": qty, "cost": cost, "entry_price": price,
        "fill_price": eff, "peak": price, "entry_liq": liq, "last_price": price, "last_liq": liq,
        "score": sc, "detail": detail, "tp1_done": False, "proceeds": 0.0, "last_seen": now,
    }
    log(f"[{b['name']}] BUY {b['positions'][mint]['symbol']} ${cost:.2f} @ {price:.8g} score={sc} liq=${liq:,.0f}")


def close_part(d, b, mint, frac, price, liq, reason, now, extra=0.0):
    pos = b["positions"][mint]
    q = pos["qty"] * frac
    got = fill_sell(price, q, liq, extra)
    pos["qty"] -= q
    pos["proceeds"] += got
    b["cash"] += got
    if frac >= 0.999 or pos["qty"] <= 1e-12:
        pnl = pos["proceeds"] - pos["cost"]
        b["realized"] += pnl
        b["trades"] += 1
        append_csv(d, "trades.csv", [
            b["name"], mint, pos["symbol"], utc(pos["opened"]), utc(now), round((now - pos["opened"]) / 60, 1),
            pos["score"], round(pos["cost"], 2), round(pos["proceeds"], 2), round(pnl, 2),
            round(pnl / pos["cost"] * 100, 1), reason, pos["entry_price"], price, pos["peak"]], TRADE_HDR)
        log(f"[{b['name']}] EXIT {pos['symbol']} {reason} pnl=${pnl:+.2f} ({pnl / pos['cost'] * 100:+.1f}%)")
        del b["positions"][mint]
    else:
        log(f"[{b['name']}] PARTIAL {pos['symbol']} {reason} sold {frac:.0%} for ${got:.2f}")


# ----------------------------------------------------------------------------- exits (shared rules, both books)
def manage(d, st, prices, now):
    for b in st["books"].values():
        for mint in list(b["positions"]):
            pos = b["positions"][mint]
            if mint not in prices:
                # Only judge a "vanished" pair when the price feed itself is healthy (prices["_ok"]).
                # Gone for 10+ minutes while the feed works -> treat as rug, exit at 10% of last value.
                if prices.get("_ok") and now - pos.get("last_seen", pos["opened"]) > 600:
                    close_part(d, b, mint, 1.0, pos["last_price"] * 0.1, pos["last_liq"], "vanished_rug", now, 0.5)
                continue
            px, liq = prices[mint]
            pos["last_price"], pos["last_liq"], pos["last_seen"] = px, liq, now
            pos["peak"] = max(pos["peak"], px)
            chg = px / pos["entry_price"] - 1
            if liq < pos["entry_liq"] * (1 - CFG["rug_liq_drop"]):
                close_part(d, b, mint, 1.0, px, liq, "liquidity_pulled", now, CFG["rug_extra_slippage"])
            elif chg <= -CFG["stop_loss"]:
                close_part(d, b, mint, 1.0, px, liq, "stop_loss", now)
            elif not pos["tp1_done"] and chg >= CFG["tp1_gain"]:
                pos["tp1_done"] = True
                close_part(d, b, mint, CFG["tp1_sell_frac"], px, liq, "take_profit_1", now)
            elif pos["tp1_done"] and px <= pos["peak"] * (1 - CFG["trail_pct"]):
                close_part(d, b, mint, 1.0, px, liq, "trailing_stop", now)
            elif now - pos["opened"] > CFG["max_hold_h"] * 3600:
                close_part(d, b, mint, 1.0, px, liq, "time_exit", now)


def price_map(st):
    mints = set()
    for b in st["books"].values():
        mints |= set(b["positions"])
    BP_STATUS["ok"] = True
    out = {}
    for mint, p in best_pairs(mints).items():
        out[mint] = (fnum(p.get("priceUsd")), fnum((p.get("liquidity") or {}).get("usd")))
    out = {m: v for m, v in out.items() if v[0] > 0}
    out["_ok"] = BP_STATUS["ok"]
    return out


# ----------------------------------------------------------------------------- one discovery + decision cycle
def scan(d, st, now, rng):
    st["stats"]["scans"] += 1
    found = radar()
    held = set()
    for b in st["books"].values():
        held |= set(b["positions"])
    cool = st["cooldown"]
    fresh = [m for m in found if m not in held and now - cool.get(m, 0) > CFG["token_cooldown_h"] * 3600]
    if not fresh:
        return
    pairs = best_pairs(fresh)
    st["stats"]["candidates_seen"] += len(pairs)
    rej = st["stats"]["rejections"]
    gated, scored = [], []
    for mint, p in pairs.items():
        why = luna_pregate(p, now)
        if why:
            key = why.split(":")[0]
            rej[key] = rej.get(key, 0) + 1
            continue
        sc, det = score(p, found[mint])
        scored.append((sc, mint, p, det))
    scored.sort(key=lambda x: -x[0])
    # Rugcheck the best few (desk candidates) plus a few random ones (control pool)
    checks = scored[:CFG["max_rug_checks_per_scan"]]
    rest = scored[CFG["max_rug_checks_per_scan"]:]
    checks += rng.sample(rest, min(3, len(rest)))
    for sc, mint, p, det in checks:
        why = luna_rugcheck(mint, now)
        if why:
            key = why.split(":")[0]
            rej[key] = rej.get(key, 0) + 1
            continue
        gated.append((sc, mint, p, det))
    gated.sort(key=lambda x: -x[0])
    prices = price_map(st)
    desk, ctrl = st["books"]["desk"], st["books"]["control"]
    for sc, mint, p, det in gated:
        if sc < CFG["entry_score"]:
            break
        eq = book_equity(desk, prices)
        size, why = titan_size(desk, sc, fnum((p.get("liquidity") or {}).get("usd")), eq)
        if not size:
            rej["titan_" + why] = rej.get("titan_" + why, 0) + 1
            break
        open_pos(desk, mint, p, sc, det, now, size)
        cool[mint] = now
        # control: random safe token not held, same dollar size
        pool = [g for g in gated if g[1] not in desk["positions"] and g[1] not in ctrl["positions"]]
        if pool:
            csc, cm, cp, cdet = rng.choice(pool)
            ceq = book_equity(ctrl, prices)
            csize, _ = titan_size(ctrl, CFG["entry_score"], fnum((cp.get("liquidity") or {}).get("usd")), ceq)
            csize = min(size, csize) if csize else 0
            if csize:
                open_pos(ctrl, cm, cp, csc, cdet, now, csize)
                cool[cm] = now
    # trim cooldown map
    st["cooldown"] = {m: t for m, t in cool.items() if now - t < 48 * 3600}


def roll_day(st, prices, now):
    day = time.strftime("%Y-%m-%d", time.gmtime(now))
    for b in st["books"].values():
        eq = book_equity(b, prices)
        if b["day"] != day:
            b["day"], b["day_start_equity"] = day, eq
        if eq < b["day_start_equity"] * (1 - CFG["daily_loss_stop"]) and b["halted_day"] != day:
            b["halted_day"] = day
            log(f"[{b['name']}] DAILY LOSS STOP hit — no new entries until next UTC day")
        b["peak_equity"] = max(b["peak_equity"], eq)
        b["max_dd"] = max(b["max_dd"], 1 - eq / b["peak_equity"])


# ----------------------------------------------------------------------------- main loop
def run(d, minutes, seed=None):
    rng = random.Random(seed)
    os.makedirs(d, exist_ok=True)
    st = load_state(d)
    end = NOW() + minutes * 60
    next_scan = 0
    last_eq = 0
    while NOW() < end:
        now = NOW()
        prices = price_map(st)
        manage(d, st, prices, now)
        roll_day(st, prices, now)
        if now >= next_scan:
            try:
                scan(d, st, now, rng)
            except Exception as e:  # keep running; log and move on
                log("scan-error", type(e).__name__, str(e)[:200])
            next_scan = now + CFG["scan_every_s"]
        if now - last_eq >= 300:
            prices = price_map(st)
            de, ce = book_equity(st["books"]["desk"], prices), book_equity(st["books"]["control"], prices)
            append_csv(d, "equity.csv", [utc(now), round(de, 2), round(ce, 2),
                                         len(st["books"]["desk"]["positions"]),
                                         len(st["books"]["control"]["positions"])], EQ_HDR)
            last_eq = now
        save_state(d, st)
        SLEEP(CFG["tick_every_s"])
    save_state(d, st)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", default="data")
    ap.add_argument("--minutes", type=float, default=15)
    a = ap.parse_args()
    run(a.data, a.minutes)
