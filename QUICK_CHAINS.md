# Quick Endpoint Chains

**Fast reference for common API endpoint combinations**

---

## Basic Chains

### 🎯 Ticker → Full Analysis

```bash
ticker="AAPL"

# Core info
GET /api/stock/$ticker/info
GET /api/stock/$ticker/greeks
GET /api/stock/$ticker/options-volume

# Greek exposure
GET /api/stock/$ticker/greek-exposure
GET /api/stock/$ticker/greek-exposure/expiry
GET /api/stock/$ticker/spot-exposures

# Flow analysis
GET /api/stock/$ticker/flow-recent
GET /api/stock/$ticker/flow-alerts
GET /api/stock/$ticker/flow-per-expiry

# Options metrics
GET /api/stock/$ticker/max-pain
GET /api/stock/$ticker/nope
GET /api/stock/$ticker/iv-rank
```

### 📊 Contract → Full Details

```bash
contract_id="AAPL251219C00175000"

# All timeframes
GET /api/option-contract/$contract_id/historic
GET /api/option-contract/$contract_id/intraday
GET /api/option-contract/$contract_id/flow

# Volume analysis
GET /api/option-contract/$contract_id/volume-profile
```

### 🏢 Institution → Holdings → Stocks

```bash
institution="VANGUARD GROUP INC"

# Get holdings
GET /api/institution/$institution/holdings
# Extract tickers from response

# For each ticker:
GET /api/stock/{ticker}/info
GET /api/institution/{ticker}/ownership
```

---

## Discovery Chains

### 🔍 Find Hot Stocks

```bash
# Method 1: From flow alerts
GET /api/option-trades/flow-alerts?limit=10
# → Extract tickers

# Method 2: From OI changes
GET /api/market/oi-change?limit=10
# → Extract underlying_symbol

# Method 3: From screener
GET /api/screener/stocks?limit=10
# → Extract tickers

# Then analyze each:
GET /api/stock/{ticker}/info
GET /api/stock/{ticker}/greek-exposure
```

### 💰 Find Hot Contracts

```bash
# Method 1: From screener
GET /api/screener/option-contracts?limit=10
# → Extract contracts

# Method 2: From flow alerts
GET /api/option-trades/flow-alerts?limit=10
# → Extract contracts

# Method 3: From ticker chains
GET /api/stock/{ticker}/option-chains
# → Extract contracts

# Then analyze:
GET /api/option-contract/{id}/flow
GET /api/option-contract/{id}/volume-profile
```

---

## Analysis Chains

### 📈 Full Options Analysis

```bash
ticker="SPY"

# 1. Base metrics
GET /api/stock/$ticker/options-volume
GET /api/stock/$ticker/max-pain

# 2. Greek exposure breakdown
GET /api/stock/$ticker/greek-exposure
GET /api/stock/$ticker/greek-exposure/expiry
GET /api/stock/$ticker/greek-exposure/strike

# 3. Flow analysis
GET /api/stock/$ticker/flow-per-expiry
GET /api/stock/$ticker/flow-per-strike
GET /api/stock/$ticker/greek-flow

# 4. Open interest
GET /api/stock/$ticker/oi-per-expiry
GET /api/stock/$ticker/oi-per-strike

# 5. Spot GEX levels
GET /api/stock/$ticker/spot-exposures
GET /api/stock/$ticker/spot-exposures/strike
```

### 📉 Short Analysis

```bash
ticker="GME"

# Complete short picture
GET /api/shorts/$ticker/interest-float
GET /api/shorts/$ticker/volume-and-ratio
GET /api/shorts/$ticker/data
GET /api/shorts/$ticker/ftds
GET /api/shorts/$ticker/volumes-by-exchange

# Cross-reference with darkpool
GET /api/darkpool/$ticker

# Check gamma exposure (squeeze potential)
GET /api/stock/$ticker/greek-exposure
```

### 💹 Volatility Analysis

```bash
ticker="TSLA"

# All vol metrics
GET /api/stock/$ticker/volatility/realized
GET /api/stock/$ticker/volatility/term-structure
GET /api/stock/$ticker/volatility/stats
GET /api/stock/$ticker/iv-rank
GET /api/stock/$ticker/interpolated-iv
GET /api/stock/$ticker/historical-risk-reversal-skew
```

---

## Event-Driven Chains

### 📅 Earnings Play

```bash
# 1. Find upcoming earnings
GET /api/earnings/premarket
GET /api/earnings/afterhours

# 2. For each ticker:
ticker="NVDA"

GET /api/earnings/$ticker  # Historical
GET /api/stock/$ticker/iv-rank  # IV level
GET /api/stock/$ticker/flow-alerts  # Positioning
GET /api/stock/$ticker/max-pain  # Options concentration
GET /api/stock/$ticker/volatility/term-structure  # Vol curve
```

### 🏛️ Congress Trade

```bash
# 1. Get recent trades
GET /api/congress/recent-trades?limit=20

# 2. For each ticker:
ticker="TSLA"

GET /api/stock/$ticker/info
GET /api/stock/$ticker/flow-recent  # Options activity
GET /api/institution/$ticker/ownership  # Who else owns it
```

### 🔄 ETF Rebalancing

```bash
etf="SPY"

# 1. ETF structure
GET /api/etfs/$etf/info
GET /api/etfs/$etf/weights
GET /api/etfs/$etf/holdings

# 2. Top holdings impact
GET /api/etfs/$etf/holdings?limit=10
# For each holding ticker:
GET /api/stock/{ticker}/info
GET /api/stock/{ticker}/greek-exposure
```

---

## Market-Wide Chains

### 🌊 Market Sentiment

```bash
# Aggregate views
GET /api/market/market-tide
GET /api/market/total-options-volume
GET /api/market/top-net-impact

# Sector breakdown
GET /api/market/sector-etfs
# For each sector ETF:
GET /api/market/{ticker}/etf-tide

# Options leaders
GET /api/market/oi-change?limit=20
GET /api/market/spike
```

### 📰 News Impact

```bash
# 1. Get latest news
GET /api/news/headlines?limit=20
# → Extract mentioned tickers

# 2. For each ticker:
GET /api/stock/{ticker}/info
GET /api/stock/{ticker}/flow-recent  # Reaction
GET /api/stock/{ticker}/options-volume  # Activity spike
```

---

## Time-Series Chains

### 📊 Historical → Real-Time

```bash
contract_id="SPY251219C00600000"

# Historical (days)
GET /api/option-contract/$contract_id/historic?limit=30

# Intraday (1-min intervals)
GET /api/option-contract/$contract_id/intraday

# Real-time (recent trades)
GET /api/option-contract/$contract_id/flow?limit=50
```

### 🕐 Stock Price History

```bash
ticker="AAPL"

# Different granularities
GET /api/stock/$ticker/ohlc/1D?limit=30  # 30 days
GET /api/stock/$ticker/ohlc/1H?limit=24  # 24 hours
GET /api/stock/$ticker/ohlc/5m?limit=78  # Trading day
```

---

## Cross-Reference Chains

### 🔗 Institution + Stock

```bash
# Start with stock
ticker="NVDA"

# Who owns it?
GET /api/institution/$ticker/ownership

# For each major holder:
institution="VANGUARD GROUP INC"
GET /api/institution/$institution/holdings
GET /api/institution/$institution/activity
GET /api/institution/$institution/sectors
```

### 🔗 Insider + Stock

```bash
# Start with ticker
ticker="AAPL"

# Insider activity
GET /api/insider/$ticker
GET /api/insider/$ticker/ticker-flow

# Or start with sector
sector="Technology"
GET /api/insider/$sector/sector-flow

# All recent insider transactions
GET /api/insider/transactions?limit=50
```

### 🔗 Darkpool + Options

```bash
ticker="TSLA"

# Darkpool activity
GET /api/darkpool/$ticker
GET /api/darkpool/recent?ticker=$ticker

# Cross-reference with options
GET /api/stock/$ticker/flow-recent
GET /api/stock/$ticker/greek-exposure

# Check if darkpool correlates with GEX
```

---

## Aggregation Patterns

### 🎯 Sector Analysis

```bash
sector="Technology"

# Get all tickers in sector
GET /api/stock/$sector/tickers

# Aggregate metrics (you build this)
for ticker in tickers:
    GET /api/stock/$ticker/options-volume
    GET /api/stock/$ticker/greek-exposure
    # Sum/average across sector

# Insider flows
GET /api/insider/$sector/sector-flow
```

### 🎯 Market Reconstruction

```bash
# Bottom-up market view
# 1. Get major components
GET /api/etfs/SPY/holdings?limit=50

# 2. For each:
GET /api/stock/{ticker}/greek-exposure
GET /api/stock/{ticker}/flow-recent

# 3. Aggregate to match
GET /api/market/market-tide
```

---

## Real-Time Monitoring

### 🚨 Live Flow

```bash
# Initial state (REST)
GET /api/option-trades/flow-alerts?limit=20
GET /api/market/market-tide

# Then switch to WebSocket
WS /api/socket/flow_alerts  # Live alerts
WS /api/socket/option_trades  # Live trades

# On each alert, fetch via REST:
GET /api/stock/{ticker}/greek-exposure
GET /api/option-contract/{id}/flow
```

### 📡 Price + Flow

```bash
# WebSocket streams
WS /api/socket/price  # Live prices
WS /api/socket/gex  # Live GEX updates
WS /api/socket/flow_alerts  # Live flow

# Complement with REST for deep dive
GET /api/stock/{ticker}/greek-exposure/strike
GET /api/stock/{ticker}/max-pain
```

---

## Cheat Sheet

### Entry Points (No Parameters)

```
✓ /api/market/oi-change
✓ /api/market/market-tide
✓ /api/screener/stocks
✓ /api/screener/option-contracts
✓ /api/option-trades/flow-alerts
✓ /api/congress/recent-trades
✓ /api/insider/transactions
✓ /api/darkpool/recent
✓ /api/institutions
✓ /api/earnings/premarket
✓ /api/earnings/afterhours
✓ /api/news/headlines
```

### Core Parameters

```
ticker → 41 stock/* endpoints + related categories
contract_id → 4 option-contract/* endpoints
institution_name → institution/{name}/* endpoints
sector → stock/{sector}/tickers, insider/{sector}/*
expiry → greek-flow/{expiry}, spot-exposures/{expiry}/*
```

### Most Useful 3-Endpoint Chains

```
1. screener/stocks → stock/info → stock/greek-exposure
2. flow-alerts → option-contract/flow → stock/greek-exposure
3. institutions → institution/holdings → institution/ownership
4. oi-change → stock/option-chains → option-contract/flow
5. market/market-tide → stock/flow-recent → stock/max-pain
```

---

## Pro Tips

1. **Cache entry point responses** - they change slowly
2. **Extract ALL IDs in one pass** - avoid redundant calls
3. **Use URL parameters** - limit, date filters reduce data
4. **Chain hierarchically** - base → expiry → strike
5. **WebSocket for real-time** - don't poll
6. **Parallel requests** - fetch independent data simultaneously

---

## Related Documents

- [ENDPOINT_RELATIONSHIPS.md](./ENDPOINT_RELATIONSHIPS.md) - Full relationship map
- [DATA_FLOW_EXAMPLES.md](./DATA_FLOW_EXAMPLES.md) - Complete code examples
- [Individual docs](./docs/) - Detailed endpoint documentation
