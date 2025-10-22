# Unusual Whales API - Endpoint Relationships

**Last Updated**: 2025-10-22
**Total Relationships Documented**: 48
**Relationship Types**: Direct, Hierarchical, Aggregation, Time-Series, Implicit

---

## Overview

This document maps all discovered relationships between the 109 API endpoints, showing how data flows between different endpoints and which fields from one endpoint serve as parameters for others.

**Relationship Discovery Method**: Systematic curl tracing with actual API calls

---

## Table of Contents

1. [Direct Field Mappings](#1-direct-field-mappings)
2. [Hierarchical Relationships](#2-hierarchical-relationships)
3. [Aggregation Relationships](#3-aggregation-relationships)
4. [Time-Series Relationships](#4-time-series-relationships)
5. [Cross-Category Flows](#5-cross-category-flows)
6. [Implicit Relationships](#6-implicit-relationships)
7. [WebSocket Relationships](#7-websocket-relationships)

---

## 1. Direct Field Mappings

These relationships show clear field → parameter mappings where data from one endpoint is used as input to another.

### Market → Options & Stocks

```
/api/market/oi-change[].option_symbol → /api/option-contract/{id}/flow
/api/market/oi-change[].underlying_symbol → /api/stock/{ticker}/*
/api/market/sector-etfs[].ticker → /api/market/{ticker}/etf-tide
/api/market/oi-change[].underlying_symbol → /api/darkpool/{ticker}
```

**Example Flow**:
```bash
# Get top OI change
curl /api/market/oi-change?limit=1
# Returns: {"data": [{"underlying_symbol": "AAPL", "option_symbol": "AAPL251219C00175000"}]}

# Use ticker
curl /api/stock/AAPL/info

# Use contract ID
curl /api/option-contract/AAPL251219C00175000/flow
```

### Screeners → Details

```
/api/screener/stocks[].ticker → /api/stock/{ticker}/*
/api/screener/option-contracts[].contract → /api/option-contract/{id}/*
/api/screener/analysts[].ticker → /api/stock/{ticker}/*
```

**Example Flow**:
```bash
# Screen for stocks
curl /api/screener/stocks?limit=1
# Returns: {"data": [{"ticker": "SPY"}]}

# Get full stock details
curl /api/stock/SPY/info
curl /api/stock/SPY/option-chains
curl /api/stock/SPY/greek-exposure
```

### Stock → Option Contracts

```
/api/stock/{ticker}/info → /api/stock/{ticker}/option-chains
/api/stock/{ticker}/option-chains[].contract → /api/option-contract/{id}/*
/api/stock/{ticker}/option-chains[] → provides contract IDs for:
  - /api/option-contract/{id}/flow
  - /api/option-contract/{id}/historic
  - /api/option-contract/{id}/intraday
  - /api/option-contract/{id}/volume-profile
```

**Example Flow**:
```bash
# Get option chains for stock
curl /api/stock/AAPL/option-chains
# Returns contracts: ["AAPL251219C00175000", ...]

# Get contract details
curl /api/option-contract/AAPL251219C00175000/flow
curl /api/option-contract/AAPL251219C00175000/historic
```

### Institutions → Holdings → Stocks

```
/api/institutions[].name → /api/institution/{name}/holdings
/api/institutions[].name → /api/institution/{name}/activity
/api/institutions[].name → /api/institution/{name}/sectors
/api/institution/{name}/holdings[].ticker → /api/institution/{ticker}/ownership
/api/institution/{name}/holdings[].ticker → /api/stock/{ticker}/*
```

**Example Flow**:
```bash
# List institutions
curl /api/institutions?limit=1
# Returns: {"data": [{"name": "VANGUARD GROUP INC"}]}

# Get holdings
curl /api/institution/VANGUARD%20GROUP%20INC/holdings
# Returns: {"data": [{"ticker": "AAPL", "shares": "1000000"}]}

# Check ownership
curl /api/institution/AAPL/ownership
```

### ETFs → Holdings → Stocks

```
/api/etfs/{ticker}/holdings[].ticker → /api/stock/{ticker}/*
/api/etfs/{ticker}/exposure[].ticker → /api/stock/{ticker}/*
/api/etfs/{ticker}/weights → shows sector/country allocations
```

**Example Flow**:
```bash
# Get ETF holdings
curl /api/etfs/SPY/holdings
# Returns: {"data": [{"ticker": "AAPL", "weight": "7.2%"}]}

# Get holding details
curl /api/stock/AAPL/info
```

### Congressional/Insider Trading → Stocks

```
/api/congress/recent-trades[].ticker → /api/stock/{ticker}/*
/api/congress/congress-trader[].ticker → /api/stock/{ticker}/*
/api/insider/transactions[].ticker → /api/insider/{ticker}
/api/insider/transactions[].ticker → /api/stock/{ticker}/*
/api/insider/transactions[].sector → /api/insider/{sector}/sector-flow
```

**Example Flow**:
```bash
# Get congress trades
curl /api/congress/recent-trades?limit=1
# Returns: {"data": [{"ticker": "TSLA", "trader": "Nancy Pelosi"}]}

# Get stock details
curl /api/stock/TSLA/info
```

### Darkpool → Stocks

```
/api/darkpool/recent[].ticker → /api/darkpool/{ticker}
/api/darkpool/recent[].ticker → /api/stock/{ticker}/*
```

### Flow Alerts → Contracts & Stocks

```
/api/option-trades/flow-alerts[].ticker → /api/stock/{ticker}/flow-alerts
/api/option-trades/flow-alerts[].ticker → /api/stock/{ticker}/flow-recent
/api/option-trades/flow-alerts[].contract → /api/option-contract/{id}/*
```

### Earnings → Stocks

```
/api/earnings/premarket[].ticker → /api/earnings/{ticker}
/api/earnings/afterhours[].ticker → /api/earnings/{ticker}
/api/earnings/*[].ticker → /api/stock/{ticker}/*
```

---

## 2. Hierarchical Relationships

These show parent-child relationships where endpoints branch into more specific views.

### Greek Exposure Hierarchy

```
/api/stock/{ticker}/greek-exposure (aggregated)
  ├── /api/stock/{ticker}/greek-exposure/expiry (by expiration)
  ├── /api/stock/{ticker}/greek-exposure/strike (by strike price)
  └── /api/stock/{ticker}/greek-exposure/strike-expiry (by both)
```

### Spot Exposures Hierarchy

```
/api/stock/{ticker}/spot-exposures (aggregated GEX by spot price)
  ├── /api/stock/{ticker}/spot-exposures/strike
  ├── /api/stock/{ticker}/spot-exposures/expiry-strike
  └── /api/stock/{ticker}/spot-exposures/{expiry}/strike
```

### Greek Flow Hierarchy

```
/api/stock/{ticker}/greek-flow (all expirations)
  └── /api/stock/{ticker}/greek-flow/{expiry} (specific expiration)

/api/group-flow/{flow_group}/greek-flow (all expirations)
  └── /api/group-flow/{flow_group}/greek-flow/{expiry} (specific expiration)
```

### Open Interest Hierarchy

```
/api/stock/{ticker}/oi-change (overall changes)
  ├── /api/stock/{ticker}/oi-per-expiry (by expiration)
  └── /api/stock/{ticker}/oi-per-strike (by strike)
```

### Options Flow Hierarchy

```
/api/stock/{ticker}/flow-recent (recent trades)
  ├── /api/stock/{ticker}/flow-per-expiry (by expiration)
  ├── /api/stock/{ticker}/flow-per-strike (by strike)
  └── /api/stock/{ticker}/flow-per-strike-intraday (intraday by strike)
```

### Stock Information Tiers

```
/api/stock/{ticker}/info (basic info)
  ├── /api/stock/{ticker}/greeks (options greeks summary)
  ├── /api/stock/{ticker}/greek-exposure (detailed GEX)
  ├── /api/stock/{ticker}/option-chains (all contracts)
  └── /api/stock/{ticker}/option-contracts (filtered contracts)
```

---

## 3. Aggregation Relationships

These show how market-wide data aggregates from ticker-specific endpoints.

### Market Aggregations

```
/api/market/market-tide = aggregate(multiple tickers' options flow)
/api/market/{ticker}/etf-tide = aggregate(ETF holdings' options flow)
/api/market/total-options-volume = sum(/api/stock/{ticker}/options-volume[])
/api/market/top-net-impact = top(/api/stock/{ticker}/flow-recent[])
/api/market/oi-change = top(/api/stock/{ticker}/oi-change[])
```

### Sector Aggregations

```
/api/market/{sector}/sector-tide = aggregate(sector stocks' options flow)
/api/stock/{sector}/tickers[].ticker → /api/stock/{ticker}/*
```

---

## 4. Time-Series Relationships

These show how endpoints relate across different time granularities.

### Option Contract Time-Series

```
/api/option-contract/{id}/historic = daily OHLC data
/api/option-contract/{id}/intraday = 1-minute interval data
/api/option-contract/{id}/flow = recent trades (real-time)
```

**Granularity**: Daily → 1-min → Real-time

### Stock Time-Series

```
/api/stock/{ticker}/ohlc/1D = daily candles
/api/stock/{ticker}/ohlc/1H = hourly candles
/api/stock/{ticker}/ohlc/5m = 5-minute candles
```

**Granularity**: Daily → Hourly → 5-min

### Historical References

```
Any ticker endpoint can reference:
  - /api/seasonality/{ticker}/monthly (historical monthly patterns)
  - /api/seasonality/{ticker}/year-month (year-over-year monthly data)
  - /api/earnings/{ticker} (historical earnings)
```

---

## 5. Cross-Category Flows

These show common integration patterns across multiple categories.

### Pattern 1: Ticker Discovery → Deep Dive

```
Entry Point (any):
  - /api/screener/stocks
  - /api/market/oi-change
  - /api/option-trades/flow-alerts
  - /api/congress/recent-trades
  - /api/darkpool/recent
  - /api/insider/transactions

↓ Extract ticker

Stock Data:
  - /api/stock/{ticker}/info
  - /api/stock/{ticker}/greek-exposure
  - /api/stock/{ticker}/flow-recent
  - /api/stock/{ticker}/options-volume

↓ Get contracts

Option Details:
  - /api/stock/{ticker}/option-chains
  - /api/option-contract/{id}/flow
```

### Pattern 2: Options Analysis Chain

```
/api/stock/{ticker}/option-chains
  → get contract IDs
  → /api/option-contract/{id}/flow (recent activity)
  → /api/option-contract/{id}/volume-profile (price levels)
  → /api/option-contract/{id}/historic (price history)
  → /api/stock/{ticker}/greek-exposure (overall GEX)
  → /api/stock/{ticker}/max-pain (support/resistance)
```

### Pattern 3: Institutional Analysis

```
/api/institutions (find major players)
  → /api/institution/{name}/holdings (what they own)
  → /api/institution/{name}/activity (recent changes)
  → /api/institution/{ticker}/ownership (who owns what)
  → /api/stock/{ticker}/info (stock details)
```

### Pattern 4: Short Analysis

```
/api/stock/{ticker}/info
  → /api/shorts/{ticker}/interest-float (SI%, float)
  → /api/shorts/{ticker}/volume-and-ratio (daily short volume)
  → /api/shorts/{ticker}/data (borrow rates)
  → /api/shorts/{ticker}/ftds (failures to deliver)
  → /api/darkpool/{ticker} (off-exchange activity)
```

---

## 6. Implicit Relationships

These endpoints don't have direct field mappings but are contextually related.

### Options Metrics Suite (Same Ticker)

```
All relate to same ticker's options:
  - /api/stock/{ticker}/max-pain (price with max decay)
  - /api/stock/{ticker}/nope (net options pricing effect)
  - /api/stock/{ticker}/net-prem-ticks (premium flow)
  - /api/stock/{ticker}/greek-exposure (GEX levels)
  - /api/stock/{ticker}/volatility/realized (historical vol)
  - /api/stock/{ticker}/iv-rank (current vs historical IV)
```

### Volatility Analysis Suite

```
Related volatility metrics:
  - /api/stock/{ticker}/volatility/realized
  - /api/stock/{ticker}/volatility/term-structure
  - /api/stock/{ticker}/volatility/stats
  - /api/stock/{ticker}/iv-rank
  - /api/stock/{ticker}/interpolated-iv
  - /api/stock/{ticker}/historical-risk-reversal-skew
```

### Event-Based Relationships

```
/api/market/economic-calendar → affects all market/stock endpoints
/api/market/fda-calendar → affects pharmaceutical sector stocks
/api/earnings/{ticker} → affects /api/stock/{ticker}/flow-* (event-driven flow)
/api/news/headlines → affects mentioned tickers
```

### Net Flow Relationships

```
/api/net-flow/expiry (market-wide)
  ↔ /api/stock/{ticker}/flow-per-expiry (ticker-specific)
```

---

## 7. WebSocket Relationships

WebSocket endpoints provide real-time streams of data also available via REST.

### WebSocket Channels

```
/api/socket/price
  → Real-time updates for stock prices
  → REST equivalent: /api/stock/{ticker}/ohlc/*

/api/socket/flow_alerts
  → Real-time flow alerts
  → REST equivalent: /api/option-trades/flow-alerts

/api/socket/option_trades
  → Real-time option trades
  → REST equivalent: /api/option-contract/{id}/flow

/api/socket/news
  → Real-time news
  → REST equivalent: /api/news/headlines

/api/socket/gex
  → Real-time gamma exposure updates
  → REST equivalent: /api/stock/{ticker}/greek-exposure
```

**Pattern**: Use REST for initial state, WebSocket for live updates

---

## Relationship Summary

### By Category

| Category | Direct Edges | Hierarchical | Aggregation | Time-Series |
|----------|--------------|--------------|-------------|-------------|
| Stock | 15 | 8 | 2 | 3 |
| Market | 5 | 1 | 5 | 0 |
| Options | 8 | 4 | 0 | 3 |
| Institutions | 5 | 0 | 0 | 0 |
| Congress/Insider | 4 | 1 | 0 | 0 |
| Screeners | 3 | 0 | 0 | 0 |
| Others | 8 | 2 | 1 | 1 |

### By Relationship Type

- **Direct Field Mappings**: 32 relationships
- **Hierarchical**: 16 relationships
- **Aggregation**: 8 relationships
- **Time-Series**: 7 relationships
- **Implicit**: 15+ relationships

---

## Usage Patterns

### Finding Related Endpoints

1. **Start with entry points** (no parameters needed):
   - Screeners
   - Market-wide data
   - Recent activity feeds

2. **Extract identifiers**:
   - Tickers
   - Contract IDs
   - Institution names
   - Sectors

3. **Follow the graph**:
   - Use identifiers in related endpoints
   - Check hierarchical breakdowns
   - Explore implicit relationships

### Common Queries

**"What can I do with a ticker?"**
```
ticker → 41 stock/* endpoints
ticker → seasonality endpoints
ticker → earnings endpoint
ticker → shorts endpoints
ticker → darkpool endpoint
ticker → insider endpoint
ticker → etf exposure (if ETF)
```

**"What can I do with a contract ID?"**
```
contract_id → 4 option-contract/* endpoints
contract_id → extract underlying → all stock/* endpoints
```

**"How do I find institutional positions?"**
```
/api/institutions → names
→ /api/institution/{name}/holdings → tickers
→ /api/institution/{ticker}/ownership → full ownership
→ /api/stock/{ticker}/* → stock details
```

---

## Notes

- All relationships validated with actual API calls on 2025-10-22
- Some endpoints may have additional relationships not yet discovered
- WebSocket relationships require connection upgrade (not HTTP)
- Rate limiting may affect chained API calls
- Some relationships require specific subscription tiers

---

**Related Documents**:
- [DATA_FLOW_EXAMPLES.md](./DATA_FLOW_EXAMPLES.md) - Practical integration examples
- [QUICK_CHAINS.md](./QUICK_CHAINS.md) - Common endpoint combinations
- [RELATIONSHIP_GRAPH.json](./RELATIONSHIP_GRAPH.json) - Machine-readable format
