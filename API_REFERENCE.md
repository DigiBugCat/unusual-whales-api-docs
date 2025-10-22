# Unusual Whales API Reference

**Complete reference for all 109 endpoints**

**Base URL**: `https://api.unusualwhales.com`

**Authentication**: Bearer token in Authorization header

**Last Updated**: 2025-10-22

---

## Quick Navigation

- [Alerts](#alerts) (2 endpoints)
- [Congress](#congress) (3 endpoints)
- [Darkpool](#darkpool) (2 endpoints)
- [Earnings](#earnings) (3 endpoints)
- [Etfs](#etfs) (5 endpoints)
- [Group Flow](#group-flow) (2 endpoints)
- [Insider](#insider) (4 endpoints)
- [Institution](#institution) (4 endpoints)
- [Institutions](#institutions) (2 endpoints)
- [Market](#market) (12 endpoints)
- [Net Flow](#net-flow) (1 endpoints)
- [News](#news) (1 endpoints)
- [Option Contract](#option-contract) (4 endpoints)
- [Option Trades](#option-trades) (2 endpoints)
- [Politician Portfolios](#politician-portfolios) (3 endpoints)
- [Screener](#screener) (3 endpoints)
- [Seasonality](#seasonality) (4 endpoints)
- [Shorts](#shorts) (5 endpoints)
- [Socket](#socket) (6 endpoints)
- [Stock](#stock) (41 endpoints)

---

## Alerts

**2 endpoints**

### `GET /api/alerts`

**Summary**: Alerts

**Description**: Returns all the alerts that have been triggered for the user.

Time filtering is available using the `newer_than` and `older_than` parameters:
- The maximum lookback period is 14 days
- If no time ran...

**Parameters**:

| Name | Type | Location | Required | Description |
|------|------|----------|----------|-------------|
| limit | string | query | No |  |
| intraday_only | string | query | No |  |
| config_ids[] | string | query | No |  |
| ticker_symbols | string | query | No |  |
| noti_types[] | string | query | No |  |
| newer_than | string | query | No |  |
| older_than | string | query | No |  |

**Example**:
```bash
curl "/api/alerts" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/alerts/README.md)

---

### `GET /api/alerts/configuration`

**Summary**: Alert configurations

**Description**: Returnst all alert configurations of the user.

Users can create alerts for:
- Market tide
- Gamma exposure (GEX), Vanna exposure (VEX), Charm exposure (CEX)
- Interval Contract screeners (replicates ...

**Example**:
```bash
curl "/api/alerts/configuration" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/alerts/README.md)

---

## Congress

**3 endpoints**

### `GET /api/congress/congress-trader`

**Summary**: Recent Reports By Trader

**Description**: Returns the recent reports by the given congress member....

**Parameters**:

| Name | Type | Location | Required | Description |
|------|------|----------|----------|-------------|
| limit | string | query | No |  |
| date | string | query | No |  |
| ticker | string | query | No |  |
| name | string | query | No |  |

**Example**:
```bash
curl "/api/congress/congress-trader" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/congress/README.md)

---

### `GET /api/congress/late-reports`

**Summary**: Recent Late Reports

**Description**: Returns the recent late reports by congress members.
If a date is given, will only return recent late reports, which's report date is <= the given input date....

**Parameters**:

| Name | Type | Location | Required | Description |
|------|------|----------|----------|-------------|
| limit | string | query | No |  |
| date | string | query | No |  |
| ticker | string | query | No |  |

**Example**:
```bash
curl "/api/congress/late-reports" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/congress/README.md)

---

### `GET /api/congress/recent-trades`

**Summary**: Recent Congress Trades

**Description**: Returns the latest transacted trades by congress members.
If a date is given, will only return reports, which's transaction date is <= the given input date....

**Parameters**:

| Name | Type | Location | Required | Description |
|------|------|----------|----------|-------------|
| limit | string | query | No |  |
| date | string | query | No |  |
| ticker | string | query | No |  |

**Example**:
```bash
curl "/api/congress/recent-trades" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/congress/README.md)

---

## Darkpool

**2 endpoints**

### `GET /api/darkpool/recent`

**Summary**: Recent Darkpool Trades

**Description**: Returns the latest darkpool trades....

**Parameters**:

| Name | Type | Location | Required | Description |
|------|------|----------|----------|-------------|
| limit | string | query | No |  |
| date | string | query | No |  |
| min_premium | string | query | No |  |
| max_premium | string | query | No |  |
| min_size | string | query | No |  |
| max_size | string | query | No |  |
| min_volume | string | query | No |  |
| max_volume | string | query | No |  |

**Example**:
```bash
curl "/api/darkpool/recent" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/darkpool/README.md)

---

### `GET /api/darkpool/{ticker}`

**Summary**: Ticker Darkpool Trades

**Description**: Returns the darkpool trades for the given ticker on a given day.
Date must be the current or a past date. If no date is given, returns data for the current/last market day....

**Parameters**:

| Name | Type | Location | Required | Description |
|------|------|----------|----------|-------------|
| ticker | string | path | Yes |  |
| date | string | query | No |  |
| newer_than | string | query | No |  |
| older_than | string | query | No |  |
| min_premium | string | query | No |  |
| max_premium | string | query | No |  |
| min_size | string | query | No |  |
| max_size | string | query | No |  |
| min_volume | string | query | No |  |
| max_volume | string | query | No |  |

*...and 1 more parameters*

**Example**:
```bash
curl "/api/darkpool/AAPL" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/darkpool/README.md)

---

## Earnings

**3 endpoints**

### `GET /api/earnings/afterhours`

**Summary**: Afterhours

**Description**: Returns the afterhours earnings for a given date....

**Parameters**:

| Name | Type | Location | Required | Description |
|------|------|----------|----------|-------------|
| date | string | query | No |  |
| limit | string | query | No |  |
| page | string | query | No |  |

**Example**:
```bash
curl "/api/earnings/afterhours" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/earnings/README.md)

---

### `GET /api/earnings/premarket`

**Summary**: Premarket

**Description**: Returns the premarket earnings for a given date....

**Parameters**:

| Name | Type | Location | Required | Description |
|------|------|----------|----------|-------------|
| date | string | query | No |  |
| limit | string | query | No |  |
| page | string | query | No |  |

**Example**:
```bash
curl "/api/earnings/premarket" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/earnings/README.md)

---

### `GET /api/earnings/{ticker}`

**Summary**: Historical Ticker Earnings

**Description**: Returns the historical earnings for the given ticker....

**Parameters**:

| Name | Type | Location | Required | Description |
|------|------|----------|----------|-------------|
| ticker | string | path | Yes |  |

**Example**:
```bash
curl "/api/earnings/AAPL" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/earnings/README.md)

---

## Etfs

**5 endpoints**

### `GET /api/etfs/{ticker}/exposure`

**Summary**: Exposure

**Description**: Returns all ETFs in which the given ticker is a holding...

**Parameters**:

| Name | Type | Location | Required | Description |
|------|------|----------|----------|-------------|
| ticker | string | path | Yes |  |

**Example**:
```bash
curl "/api/etfs/AAPL/exposure" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/etfs/README.md)

---

### `GET /api/etfs/{ticker}/holdings`

**Summary**: Holdings

**Description**: Returns the holdings of the ETF...

**Parameters**:

| Name | Type | Location | Required | Description |
|------|------|----------|----------|-------------|
| ticker | string | path | Yes |  |

**Example**:
```bash
curl "/api/etfs/AAPL/holdings" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/etfs/README.md)

---

### `GET /api/etfs/{ticker}/in-outflow`

**Summary**: Inflow & Outflow

**Description**: Returns an ETF's inflow and outflow...

**Parameters**:

| Name | Type | Location | Required | Description |
|------|------|----------|----------|-------------|
| ticker | string | path | Yes |  |

**Example**:
```bash
curl "/api/etfs/AAPL/in-outflow" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/etfs/README.md)

---

### `GET /api/etfs/{ticker}/info`

**Summary**: Information

**Description**: Returns the information about the given ETF ticker....

**Parameters**:

| Name | Type | Location | Required | Description |
|------|------|----------|----------|-------------|
| ticker | string | path | Yes |  |

**Example**:
```bash
curl "/api/etfs/AAPL/info" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/etfs/README.md)

---

### `GET /api/etfs/{ticker}/weights`

**Summary**: Sector & Country weights

**Description**: Returns the sector & country weights for the given ETF ticker....

**Parameters**:

| Name | Type | Location | Required | Description |
|------|------|----------|----------|-------------|
| ticker | string | path | Yes |  |

**Example**:
```bash
curl "/api/etfs/AAPL/weights" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/etfs/README.md)

---

## Group Flow

**2 endpoints**

### `GET /api/group-flow/{flow_group}/greek-flow`

**Summary**: Greek flow

**Description**: Returns the group flow's greek flow (delta & vega flow) for the given market day broken down per minute.
Date must be the current or a past date. If no date is given, returns data for the current/last...

**Parameters**:

| Name | Type | Location | Required | Description |
|------|------|----------|----------|-------------|
| flow_group | string | path | Yes |  |
| date | string | query | No |  |

**Example**:
```bash
curl "/api/group-flow/all/greek-flow" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/group-flow/README.md)

---

### `GET /api/group-flow/{flow_group}/greek-flow/{expiry}`

**Summary**: Greek flow by expiry

**Description**: Returns the group flow's greek flow (delta & vega flow) for the given market day broken down per minute & expiry.
Date must be the current or a past date. If no date is given, returns data for the cur...

**Parameters**:

| Name | Type | Location | Required | Description |
|------|------|----------|----------|-------------|
| flow_group | string | path | Yes |  |
| expiry | string | path | Yes |  |
| date | string | query | No |  |

**Example**:
```bash
curl "/api/group-flow/{flow_group}/greek-flow/2025-12-19" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/group-flow/README.md)

---

## Insider

**4 endpoints**

### `GET /api/insider/transactions`

**Summary**: Transactions

**Description**: Returns the latest insider transactions.

By default all transacations that have been filled by the same person on the same day with the same trade code are aggregated into a single row.
Each of those...

**Parameters**:

| Name | Type | Location | Required | Description |
|------|------|----------|----------|-------------|
| ticker_symbol | string | query | No |  |
| min_value | string | query | No | Minimum transaction value in dollars |
| max_value | string | query | No | Maximum transaction value in dollars |
| min_price | string | query | No | Minimum stock price at the time of transaction |
| max_price | string | query | No | Maximum stock price at the time of transaction |
| owner_name | string | query | No | Name of the insider who made the transaction |
| sectors | string | query | No | Filter by company sector(s) |
| industries | string | query | No | Filter by company industry or industries |
| min_marketcap | string | query | No |  |
| max_marketcap | string | query | No |  |

*...and 14 more parameters*

**Example**:
```bash
curl "/api/insider/transactions" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/insider/README.md)

---

### `GET /api/insider/{sector}/sector-flow`

**Summary**: Sector Flow

**Description**: Returns an aggregated view of the insider flow for the given sector.

This can be used to quickly examine the buy & sell insider flow for a given trading date...

**Parameters**:

| Name | Type | Location | Required | Description |
|------|------|----------|----------|-------------|
| sector | string | path | Yes |  |

**Example**:
```bash
curl "/api/insider/Technology/sector-flow" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/insider/README.md)

---

### `GET /api/insider/{ticker}`

**Summary**: Insiders

**Description**: Returns all insiders for the given ticker...

**Parameters**:

| Name | Type | Location | Required | Description |
|------|------|----------|----------|-------------|
| ticker | string | path | Yes |  |

**Example**:
```bash
curl "/api/insider/AAPL" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/insider/README.md)

---

### `GET /api/insider/{ticker}/ticker-flow`

**Summary**: Ticker Flow

**Description**: Returns an aggregated view of the insider flow for the given ticker.

This can be used to quickly examine the buy & sell insider flow for a given trading date...

**Parameters**:

| Name | Type | Location | Required | Description |
|------|------|----------|----------|-------------|
| ticker | string | path | Yes |  |

**Example**:
```bash
curl "/api/insider/AAPL/ticker-flow" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/insider/README.md)

---

## Institution

**4 endpoints**

### `GET /api/institution/{name}/activity`

**Summary**: Institutional Activity

**Description**: The trading activities for a given institution....

**Parameters**:

| Name | Type | Location | Required | Description |
|------|------|----------|----------|-------------|
| name | string | path | Yes |  |
| date | string | query | No |  |
| limit | string | query | No |  |
| page | string | query | No |  |

**Example**:
```bash
curl "/api/institution/VANGUARD%20GROUP%20INC/activity" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/institution/README.md)

---

### `GET /api/institution/{name}/holdings`

**Summary**: Institutional Holdings

**Description**: Returns the holdings for a given institution....

**Parameters**:

| Name | Type | Location | Required | Description |
|------|------|----------|----------|-------------|
| name | string | path | Yes |  |
| date | string | query | No |  |
| start_date | string | query | No |  |
| end_date | string | query | No |  |
| security_types | string | query | No |  |
| limit | string | query | No |  |
| page | string | query | No |  |
| order | string | query | No |  |
| order_direction | string | query | No |  |

**Example**:
```bash
curl "/api/institution/VANGUARD%20GROUP%20INC/holdings" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/institution/README.md)

---

### `GET /api/institution/{name}/sectors`

**Summary**: Sector Exposure

**Description**: The sector exposure for a given institution....

**Parameters**:

| Name | Type | Location | Required | Description |
|------|------|----------|----------|-------------|
| name | string | path | Yes |  |
| date | string | query | No |  |
| limit | string | query | No |  |
| page | string | query | No |  |

**Example**:
```bash
curl "/api/institution/VANGUARD%20GROUP%20INC/sectors" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/institution/README.md)

---

### `GET /api/institution/{ticker}/ownership`

**Summary**: Institutional Ownership

**Description**: The institutional ownership of a given ticker....

**Parameters**:

| Name | Type | Location | Required | Description |
|------|------|----------|----------|-------------|
| ticker | string | path | Yes |  |
| date | string | query | No |  |
| start_date | string | query | No |  |
| end_date | string | query | No |  |
| tags | string | query | No |  |
| order | string | query | No |  |
| order_direction | string | query | No |  |
| limit | string | query | No |  |
| page | string | query | No |  |

**Example**:
```bash
curl "/api/institution/AAPL/ownership" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/institution/README.md)

---

## Institutions

**2 endpoints**

### `GET /api/institutions`

**Summary**: List of Institutions

**Description**: Returns a list of institutions....

**Parameters**:

| Name | Type | Location | Required | Description |
|------|------|----------|----------|-------------|
| name | string | query | No |  |
| min_total_value | string | query | No |  |
| max_total_value | string | query | No |  |
| min_share_value | string | query | No |  |
| max_share_value | string | query | No |  |
| tags | string | query | No |  |
| order | string | query | No |  |
| order_direction | string | query | No |  |
| limit | string | query | No |  |
| page | string | query | No |  |

**Example**:
```bash
curl "/api/institutions" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/institutions/README.md)

---

### `GET /api/institutions/latest_filings`

**Summary**: Latest Filings

**Description**: The latest institutional filings....

**Parameters**:

| Name | Type | Location | Required | Description |
|------|------|----------|----------|-------------|
| name | string | query | No |  |
| date | string | query | No | Date in format YYYY-MM-DD |
| order | string | query | No |  |
| order_direction | string | query | No |  |
| limit | string | query | No |  |
| page | string | query | No |  |

**Example**:
```bash
curl "/api/institutions/latest_filings" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/institutions/README.md)

---

## Market

**12 endpoints**

### `GET /api/market/correlations`

**Summary**: Correlations

**Description**: Returns the correlations between a list of tickers.
Date must be the current or a past date. If no date is given, returns data for the current/last market day.

You can filter the time period either b...

**Parameters**:

| Name | Type | Location | Required | Description |
|------|------|----------|----------|-------------|
| tickers | string | query | Yes |  |
| interval | string | query | No |  |
| start_date | string | query | No |  |
| end_date | string | query | No |  |

**Example**:
```bash
curl "/api/market/correlations" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/market/README.md)

---

### `GET /api/market/economic-calendar`

**Summary**: Economic calendar

**Description**: Returns the economic calendar....

**Example**:
```bash
curl "/api/market/economic-calendar" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/market/README.md)

---

### `GET /api/market/fda-calendar`

**Summary**: FDA Calendar

**Description**: Returns FDA calendar data with filtering options.

The FDA calendar contains information about:
- PDUFA (Prescription Drug User Fee Act) dates
- Advisory Committee Meetings
- FDA Decisions
- Clinical ...

**Parameters**:

| Name | Type | Location | Required | Description |
|------|------|----------|----------|-------------|
| announced_date_min | string | query | No | Minimum announced date (YYYY-MM-DD) |
| announced_date_max | string | query | No | Maximum announced date (YYYY-MM-DD) |
| target_date_min | string | query | No | Minimum target date (supports Q1-Q4, H1-H2, MID, L |
| target_date_max | string | query | No | Maximum target date (supports Q1-Q4, H1-H2, MID, L |
| drug | string | query | No | Filter by drug name (partial match) |
| ticker | string | query | No | Filter by ticker symbol |
| limit | string | query | No | Maximum number of results to return |

**Example**:
```bash
curl "/api/market/fda-calendar" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/market/README.md)

---

### `GET /api/market/insider-buy-sells`

**Summary**: Total Insider Buy & Sells

**Description**: Returns the total amount of purchases & sells as well as notional values for insider transactions
across the market...

**Parameters**:

| Name | Type | Location | Required | Description |
|------|------|----------|----------|-------------|
| limit | string | query | No |  |

**Example**:
```bash
curl "/api/market/insider-buy-sells" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/market/README.md)

---

### `GET /api/market/market-tide`

**Summary**: Market Tide

**Description**: Market Tide is a proprietary tool that can be viewed from the Market Overview page. The Market Tide chart provides real time data based on a proprietary formula that examines market wide options activ...

**Parameters**:

| Name | Type | Location | Required | Description |
|------|------|----------|----------|-------------|
| date | string | query | No |  |
| otm_only | string | query | No |  |
| interval_5m | string | query | No |  |

**Example**:
```bash
curl "/api/market/market-tide" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/market/README.md)

---

### `GET /api/market/oi-change`

**Summary**: OI Change

**Description**: Returns the non-Index/non-ETF contracts and OI change data with the highest OI change (default: descending).
Date must be the current or a past date. If no date is given, returns data for the current/...

**Parameters**:

| Name | Type | Location | Required | Description |
|------|------|----------|----------|-------------|
| date | string | query | No |  |
| limit | string | query | No |  |
| order | string | query | No |  |

**Example**:
```bash
curl "/api/market/oi-change" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/market/README.md)

---

### `GET /api/market/sector-etfs`

**Summary**: Sector Etfs

**Description**: Returns the current trading days statistics for the SPDR sector etfs

----
This can be used to build a market overview such as:

![sectors etf](https://i.imgur.com/yQ5o6rR.png)...

**Example**:
```bash
curl "/api/market/sector-etfs" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/market/README.md)

---

### `GET /api/market/spike`

**Summary**: SPIKE

**Description**: Returns the SPIKE values for the given date.
Date must be the current or a past date. If no date is given, returns data for the current/last market day....

**Parameters**:

| Name | Type | Location | Required | Description |
|------|------|----------|----------|-------------|
| date | string | query | No |  |

**Example**:
```bash
curl "/api/market/spike" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/market/README.md)

---

### `GET /api/market/top-net-impact`

**Summary**: Top Net Impact

**Description**: Returns the top tickers by net premium (half bullish, half bearish). Defaults to last market day....

**Parameters**:

| Name | Type | Location | Required | Description |
|------|------|----------|----------|-------------|
| date | string | query | No |  |
| issue_types[] | string | query | No |  |
| limit | string | query | No |  |

**Example**:
```bash
curl "/api/market/top-net-impact" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/market/README.md)

---

### `GET /api/market/total-options-volume`

**Summary**: Total Options Volume

**Description**: Returns the total options volume and premium for all trade executions
that happened on a given trading date.

----
This can be used to build a market options overview such as:

![Market State](https:/...

**Parameters**:

| Name | Type | Location | Required | Description |
|------|------|----------|----------|-------------|
| limit | string | query | No |  |

**Example**:
```bash
curl "/api/market/total-options-volume" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/market/README.md)

---

### `GET /api/market/{sector}/sector-tide`

**Summary**: Sector Tide

**Description**: The Sector tide is similar to the Market Tide. While the market tide is based on options activity of the whole market
the sector tide is only based on the options activity of companies which are in th...

**Parameters**:

| Name | Type | Location | Required | Description |
|------|------|----------|----------|-------------|
| sector | string | path | Yes |  |
| date | string | query | No |  |

**Example**:
```bash
curl "/api/market/Technology/sector-tide" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/market/README.md)

---

### `GET /api/market/{ticker}/etf-tide`

**Summary**: ETF Tide

**Description**: The ETF tide is similar to the Market Tide. While the market tide is based on options activity of the whole market
the ETF tide is only based on the options activity of the holdings of the specified E...

**Parameters**:

| Name | Type | Location | Required | Description |
|------|------|----------|----------|-------------|
| ticker | string | path | Yes |  |
| date | string | query | No |  |

**Example**:
```bash
curl "/api/market/AAPL/etf-tide" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/market/README.md)

---

## Net Flow

**1 endpoints**

### `GET /api/net-flow/expiry`

**Summary**: Net Flow Expiry

**Description**: Returns net premium flow by `tide_type` category, `moneyness` category, and `expiration` category, allowing you to create chart variations like [https://unusualwhales.com/zero-dte](https://unusualwhal...

**Parameters**:

| Name | Type | Location | Required | Description |
|------|------|----------|----------|-------------|
| date | string | query | No | Market date to get data for (defaults to last mark |
| moneyness | array | query | No | Moneyness filter (defaults to 'all') |
| tide_type | array | query | No | Tide type filter (defaults to 'all') |
| expiration | array | query | No | Expiration filter (defaults to ['weekly', 'zero_dt |

**Example**:
```bash
curl "/api/net-flow/expiry" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/net-flow/README.md)

---

## News

**1 endpoints**

### `GET /api/news/headlines`

**Summary**: News Headlines

**Description**: Returns the latest news headlines for financial markets.

This endpoint provides access to news headlines that may impact the markets, including company-specific
news, sector news, and market-wide eve...

**Parameters**:

| Name | Type | Location | Required | Description |
|------|------|----------|----------|-------------|
| sources | string | query | No |  |
| search_term | string | query | No |  |
| major_only | string | query | No |  |
| limit | string | query | No |  |
| page | string | query | No |  |

**Example**:
```bash
curl "/api/news/headlines" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/news/README.md)

---

## Option Contract

**4 endpoints**

### `GET /api/option-contract/{id}/flow`

**Summary**: Flow Data

**Description**: Returns the last 50 option trades for the given option chain. Optionally a min premium and a side can be supplied in the query for further filtering.
If no date is specified data for the last trading ...

**Parameters**:

| Name | Type | Location | Required | Description |
|------|------|----------|----------|-------------|
| id | string | path | Yes |  |
| side | string | query | No |  |
| min_premium | string | query | No |  |
| limit | string | query | No |  |
| date | string | query | No |  |

**Example**:
```bash
curl "/api/option-contract/AAPL251219C00175000/flow" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/option-contract/README.md)

---

### `GET /api/option-contract/{id}/historic`

**Summary**: Historic Data

**Description**: Returns for every trading day historic data for the given option contract...

**Parameters**:

| Name | Type | Location | Required | Description |
|------|------|----------|----------|-------------|
| id | string | path | Yes |  |
| limit | string | query | No |  |

**Example**:
```bash
curl "/api/option-contract/AAPL251219C00175000/historic" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/option-contract/README.md)

---

### `GET /api/option-contract/{id}/intraday`

**Summary**: Intraday Data

**Description**: Returns 1 minute interval intraday data for the given option contract.
Date must be the current or a past date. If no date is given, returns data for the current/last market day....

**Parameters**:

| Name | Type | Location | Required | Description |
|------|------|----------|----------|-------------|
| id | string | path | Yes |  |
| date | string | query | No |  |

**Example**:
```bash
curl "/api/option-contract/AAPL251219C00175000/intraday" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/option-contract/README.md)

---

### `GET /api/option-contract/{id}/volume-profile`

**Summary**: Volume Profile

**Description**: Returns the volume profile (volume - sweep, floor, cross, ask, bid, etc. - per fill price) for an option symbol on a given trading day.
Date must be the current or a past date. If no date is given, re...

**Parameters**:

| Name | Type | Location | Required | Description |
|------|------|----------|----------|-------------|
| id | string | path | Yes |  |
| date | string | query | No |  |

**Example**:
```bash
curl "/api/option-contract/AAPL251219C00175000/volume-profile" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/option-contract/README.md)

---

## Option Trades

**2 endpoints**

### `GET /api/option-trades/flow-alerts`

**Summary**: Flow Alerts

**Description**: Returns the latest flow alerts....

**Parameters**:

| Name | Type | Location | Required | Description |
|------|------|----------|----------|-------------|
| ticker_symbol | string | query | No |  |
| min_premium | string | query | No |  |
| max_premium | string | query | No |  |
| min_size | string | query | No |  |
| max_size | string | query | No |  |
| min_volume | string | query | No |  |
| max_volume | string | query | No |  |
| min_open_interest | string | query | No |  |
| max_open_interest | string | query | No |  |
| all_opening | string | query | No |  |

*...and 18 more parameters*

**Example**:
```bash
curl "/api/option-trades/flow-alerts" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/option-trades/README.md)

---

### `GET /api/option-trades/full-tape/{date}`

**Summary**: Full Tape

**Description**: Download all option transactions (the "full tape") for a given trading date.

NOTICE: Access to this endpoint is only included in the Advanced API subscription.

The last 3 trading days are available ...

**Parameters**:

| Name | Type | Location | Required | Description |
|------|------|----------|----------|-------------|
| date | string | path | Yes |  |

**Example**:
```bash
curl "/api/option-trades/full-tape/2025-10-22" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/option-trades/README.md)

---

## Politician Portfolios

**3 endpoints**

### `GET /api/politician-portfolios/holders/{ticker}`

**Summary**: Politician Portfolio Holders by Ticker

**Description**: Returns all politician portfolio owner names, ID, and holdings for the specified ticker.

This is an enterprise only endpoint. Contact dan@unusualwhales.com for details about accessing this data....

**Parameters**:

| Name | Type | Location | Required | Description |
|------|------|----------|----------|-------------|
| ticker | string | path | Yes | Stock ticker symbol (e.g., AAPL, TSLA) |
| aggregate_all_portfolios | boolean | query | No | If true, aggregates all of a politicians portfolio |

**Example**:
```bash
curl "/api/politician-portfolios/holders/AAPL" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/politician-portfolios/README.md)

---

### `GET /api/politician-portfolios/people`

**Summary**: Politicians List

**Description**: Returns all politician names and IDs.

This is an enterprise only endpoint. Contact dan@unusualwhales.com for details about accessing this data....

**Example**:
```bash
curl "/api/politician-portfolios/people" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/politician-portfolios/README.md)

---

### `GET /api/politician-portfolios/{politician_id}`

**Summary**: Politician Portfolios

**Description**: Returns all portfolios and holdings for a politician.

This is an enterprise only endpoint. Contact dan@unusualwhales.com for details about accessing this data....

**Parameters**:

| Name | Type | Location | Required | Description |
|------|------|----------|----------|-------------|
| politician_id | string | path | Yes |  |
| aggregate_all_portfolios | boolean | query | No | If true, aggregates all portfolios into a single p |

**Example**:
```bash
curl "/api/politician-portfolios/12345" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/politician-portfolios/README.md)

---

## Screener

**3 endpoints**

### `GET /api/screener/analysts`

**Summary**: Analyst Rating

**Description**: Returns the latest analyst rating for the given ticker....

**Parameters**:

| Name | Type | Location | Required | Description |
|------|------|----------|----------|-------------|
| ticker | string | query | No |  |
| limit | integer | query | No | How many items to return. Default: 500, Max: 500,  |
| action | string | query | No |  |
| recommendation | string | query | No |  |

**Example**:
```bash
curl "/api/screener/analysts" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/screener/README.md)

---

### `GET /api/screener/option-contracts`

**Summary**: Hottest Chains

**Description**: A contract screener endpoint to screen the market for contracts by a variety of filter options.

For an example of what can be build with this endpoint check out the [Hottest Contracts](https://unusua...

**Parameters**:

| Name | Type | Location | Required | Description |
|------|------|----------|----------|-------------|
| ticker_symbol | string | query | No |  |
| sectors[] | string | query | No |  |
| min_underlying_price | string | query | No | The minimum stock price. |
| max_underlying_price | string | query | No | The maximum stock price. |
| is_otm | boolean | query | No | Only include contracts which are currently out of  |
| exclude_ex_div_ticker | boolean | query | No | When set to true, all tickers that trade ex-divide |
| min_dte | integer | query | No | The minimum days to expiry. |
| max_dte | integer | query | No | The maximum days to expiry. |
| min_diff | string | query | No | The minimum OTM diff of a contract. |
| max_diff | string | query | No | The maximum OTM diff of a contract. |

*...and 81 more parameters*

**Example**:
```bash
curl "/api/screener/option-contracts" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/screener/README.md)

---

### `GET /api/screener/stocks`

**Summary**: Stock Screener

**Description**: A stock screener endpoint to screen the market for stocks by a variety of filter options.

For an example of what can be build with this endpoint check out the [Stock Screener](https://unusualwhales.c...

**Parameters**:

| Name | Type | Location | Required | Description |
|------|------|----------|----------|-------------|
| ticker | string | query | No |  |
| issue_types[] | string | query | No |  |
| min_change | string | query | No | The minimum % change to the previous trading day. |
| max_change | string | query | No | The maximum % change to the previous trading day. |
| min_underlying_price | string | query | No | The minimum stock price. |
| max_underlying_price | string | query | No | The maximum stock price. |
| is_s_p_500 | boolean | query | No | Boolean whether to only include stocks which are p |
| has_dividends | boolean | query | No | Boolean wheter to only include stocks which pay di |
| sectors[] | string | query | No |  |
| min_marketcap | string | query | No | The minimum marketcap. |

*...and 56 more parameters*

**Example**:
```bash
curl "/api/screener/stocks" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/screener/README.md)

---

## Seasonality

**4 endpoints**

### `GET /api/seasonality/market`

**Summary**: Market Seasonality

**Description**: Returns the average return by month for the tickers SPY, QQQ, IWM, XLE, XLC, XLK, XLV, XLP, XLY, XLRE, XLF, XLI, XLB ....

**Example**:
```bash
curl "/api/seasonality/market" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/seasonality/README.md)

---

### `GET /api/seasonality/{month}/performers`

**Summary**: Month Performers

**Description**: Returns the tickers with the highest performance in terms of price change in the month over the years.
Per default the result is ordered by 'positive_months_perc' descending, then 'median_change' desc...

**Parameters**:

| Name | Type | Location | Required | Description |
|------|------|----------|----------|-------------|
| month | string | path | Yes |  |
| min_years | string | query | No |  |
| ticker_for_sector | string | query | No |  |
| s_p_500_nasdaq_only | string | query | No |  |
| min_oi | string | query | No |  |
| limit | string | query | No |  |
| order | string | query | No |  |
| order_direction | string | query | No |  |

**Example**:
```bash
curl "/api/seasonality/January/performers" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/seasonality/README.md)

---

### `GET /api/seasonality/{ticker}/monthly`

**Summary**: Average return per month

**Description**: Returns the average return by month for the given ticker....

**Parameters**:

| Name | Type | Location | Required | Description |
|------|------|----------|----------|-------------|
| ticker | string | path | Yes |  |

**Example**:
```bash
curl "/api/seasonality/AAPL/monthly" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/seasonality/README.md)

---

### `GET /api/seasonality/{ticker}/year-month`

**Summary**: Price change per month per year

**Description**: Returns the relative price change for all past months over multiple years....

**Parameters**:

| Name | Type | Location | Required | Description |
|------|------|----------|----------|-------------|
| ticker | string | path | Yes |  |

**Example**:
```bash
curl "/api/seasonality/AAPL/year-month" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/seasonality/README.md)

---

## Shorts

**5 endpoints**

### `GET /api/shorts/{ticker}/data`

**Summary**: Short Data

**Description**: Returns short data including rebate rate and short shares available for a ticker....

**Parameters**:

| Name | Type | Location | Required | Description |
|------|------|----------|----------|-------------|
| ticker | string | path | Yes |  |

**Example**:
```bash
curl "/api/shorts/AAPL/data" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/shorts/README.md)

---

### `GET /api/shorts/{ticker}/ftds`

**Summary**: Failures to Deliver

**Description**: Returns the short failures to deliver per day for the given ticker starting from the given date.
If no date is given, returns the data for the current/last market day....

**Parameters**:

| Name | Type | Location | Required | Description |
|------|------|----------|----------|-------------|
| ticker | string | path | Yes |  |

**Example**:
```bash
curl "/api/shorts/AAPL/ftds" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/shorts/README.md)

---

### `GET /api/shorts/{ticker}/interest-float`

**Summary**: Short Interest and Float

**Description**: Returns short interest and float data for percentage calculations for a ticker.
This endpoint provides information about the percentage of float that is shorted,
the float size, and the days to cover ...

**Parameters**:

| Name | Type | Location | Required | Description |
|------|------|----------|----------|-------------|
| ticker | string | path | Yes |  |

**Example**:
```bash
curl "/api/shorts/AAPL/interest-float" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/shorts/README.md)

---

### `GET /api/shorts/{ticker}/volume-and-ratio`

**Summary**: Short Volume and Ratio

**Description**: Returns short volume and short ratio data for a ticker....

**Parameters**:

| Name | Type | Location | Required | Description |
|------|------|----------|----------|-------------|
| ticker | string | path | Yes |  |

**Example**:
```bash
curl "/api/shorts/AAPL/volume-and-ratio" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/shorts/README.md)

---

### `GET /api/shorts/{ticker}/volumes-by-exchange`

**Summary**: Short Volume By Exchange

**Description**: Returns short volume data broken down by exchange for a ticker....

**Parameters**:

| Name | Type | Location | Required | Description |
|------|------|----------|----------|-------------|
| ticker | string | path | Yes |  |

**Example**:
```bash
curl "/api/shorts/AAPL/volumes-by-exchange" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/shorts/README.md)

---

## Socket

**6 endpoints**

### `GET /api/socket`

**Summary**: WebSocket channels

**Description**: Returns the available WebSocket channels for connections.

## Websocket Guide
#You can find fully-functional examples that stream data from many channels here:

- Python: [https://github.com/unusual-w...

**Example**:
```bash
curl "/api/socket" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/socket/README.md)

---

### `GET /api/socket/flow_alerts`

**Summary**: Flow alerts

**Description**: **NOTE:**
This is the documentation for websocket channel `flow-alerts`.
Websocket access for personal use is only available through the [Advanced plan](https://unusualwhales.com/pricing?product=api)....

**Example**:
```bash
curl "/api/socket/flow_alerts" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/socket/README.md)

---

### `GET /api/socket/gex`

**Summary**: GEX

**Description**: **NOTE:**
This is the documentation for websocket channels `gex:<TICKER>`, `gex_strike:<TICKER>`, and `gex_strike_expiry:<TICKER>`.
Websocket access for personal use is only available through the[Adva...

**Example**:
```bash
curl "/api/socket/gex" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/socket/README.md)

---

### `GET /api/socket/news`

**Summary**: News

**Description**: **NOTE:**
This is the documentation for websocket channel `news`.
Websocket access for personal use is only available through the [Advanced plan](https://unusualwhales.com/pricing?product=api).

You c...

**Example**:
```bash
curl "/api/socket/news" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/socket/README.md)

---

### `GET /api/socket/option_trades`

**Summary**: Option trades

**Description**: **NOTE:**
This is the documentation for websocket channels `option_trades` and `option_trades:<TICKER>`.
Websocket access for personal use is only available through the [Advanced plan](https://unusual...

**Example**:
```bash
curl "/api/socket/option_trades" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/socket/README.md)

---

### `GET /api/socket/price`

**Summary**: Price

**Description**: **NOTE:**
This is the documentation for websocket channel `price:<TICKER>`.
Websocket access for personal use is only available through the[Advanced plan](https://unusualwhales.com/pricing?product=api...

**Example**:
```bash
curl "/api/socket/price" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/socket/README.md)

---

## Stock

**41 endpoints**

### `GET /api/stock/{sector}/tickers`

**Summary**: Companies in Sector

**Description**: Returns a list of tickers which are in the given sector....

**Parameters**:

| Name | Type | Location | Required | Description |
|------|------|----------|----------|-------------|
| sector | string | path | Yes |  |

**Example**:
```bash
curl "/api/stock/Technology/tickers" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/stock/README.md)

---

### `GET /api/stock/{ticker}/atm-chains`

**Summary**: ATM Chains

**Description**: Returns the ATM chains for the given expirations...

**Parameters**:

| Name | Type | Location | Required | Description |
|------|------|----------|----------|-------------|
| ticker | string | path | Yes |  |
| expirations[] | string | query | Yes |  |

**Example**:
```bash
curl "/api/stock/AAPL/atm-chains" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/stock/README.md)

---

### `GET /api/stock/{ticker}/expiry-breakdown`

**Summary**: Expiry Breakdown

**Description**: Returns all expirations for the given trading day for a ticker....

**Parameters**:

| Name | Type | Location | Required | Description |
|------|------|----------|----------|-------------|
| ticker | string | path | Yes |  |
| date | string | query | No |  |

**Example**:
```bash
curl "/api/stock/AAPL/expiry-breakdown" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/stock/README.md)

---

### `GET /api/stock/{ticker}/flow-alerts`

**Summary**: Flow Alerts

**Description**: This endpoint has been deprecated and will be removed.
Please migrate to this Flow Alerts endpoint, which provides a more detailed response: [https://api.unusualwhales.com/docs#/operations/PublicApi.O...

**Parameters**:

| Name | Type | Location | Required | Description |
|------|------|----------|----------|-------------|
| ticker | string | path | Yes |  |
| limit | string | query | No |  |
| is_ask_side | string | query | No |  |
| is_bid_side | string | query | No |  |

**Example**:
```bash
curl "/api/stock/AAPL/flow-alerts" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/stock/README.md)

---

### `GET /api/stock/{ticker}/flow-per-expiry`

**Summary**: Flow per expiry

**Description**: Returns the option flow per expiry for the last trading day...

**Parameters**:

| Name | Type | Location | Required | Description |
|------|------|----------|----------|-------------|
| ticker | string | path | Yes |  |

**Example**:
```bash
curl "/api/stock/AAPL/flow-per-expiry" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/stock/README.md)

---

### `GET /api/stock/{ticker}/flow-per-strike`

**Summary**: Flow per strike

**Description**: Returns the option flow per strike for a given trading day....

**Parameters**:

| Name | Type | Location | Required | Description |
|------|------|----------|----------|-------------|
| ticker | string | path | Yes |  |
| date | string | query | No |  |

**Example**:
```bash
curl "/api/stock/AAPL/flow-per-strike" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/stock/README.md)

---

### `GET /api/stock/{ticker}/flow-per-strike-intraday`

**Summary**: Flow per strike intraday

**Description**: Returns the options flow for a given date in one minute intervals (the one minute intervals are not aggregated with each other)....

**Parameters**:

| Name | Type | Location | Required | Description |
|------|------|----------|----------|-------------|
| ticker | string | path | Yes |  |
| date | string | query | No |  |
| filter | string | query | No |  |

**Example**:
```bash
curl "/api/stock/AAPL/flow-per-strike-intraday" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/stock/README.md)

---

### `GET /api/stock/{ticker}/flow-recent`

**Summary**: Recent flows

**Description**: Returns the latest flows for the given ticker. Optionally a min premium and a side can be supplied in the query for further filtering....

**Parameters**:

| Name | Type | Location | Required | Description |
|------|------|----------|----------|-------------|
| ticker | string | path | Yes |  |
| side | string | query | No |  |
| min_premium | string | query | No |  |

**Example**:
```bash
curl "/api/stock/AAPL/flow-recent" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/stock/README.md)

---

### `GET /api/stock/{ticker}/greek-exposure`

**Summary**: Greek Exposure

**Description**: Greek Exposure is the assumed greek exposure that market makers are exposed to.

The most popular greek exposure is gamma exposure (GEX).

Investors and large funds lower risk and protect their money ...

**Parameters**:

| Name | Type | Location | Required | Description |
|------|------|----------|----------|-------------|
| ticker | string | path | Yes |  |
| date | string | query | No |  |
| timeframe | string | query | No |  |

**Example**:
```bash
curl "/api/stock/AAPL/greek-exposure" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/stock/README.md)

---

### `GET /api/stock/{ticker}/greek-exposure/expiry`

**Summary**: Greek Exposure By Expiry

**Description**: The greek exposure of a ticker grouped by expiry dates across all contracts on a given market date....

**Parameters**:

| Name | Type | Location | Required | Description |
|------|------|----------|----------|-------------|
| ticker | string | path | Yes |  |
| date | string | query | No |  |

**Example**:
```bash
curl "/api/stock/AAPL/greek-exposure/expiry" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/stock/README.md)

---

### `GET /api/stock/{ticker}/greek-exposure/strike`

**Summary**: Greek Exposure By Strike

**Description**: The greek exposure of a ticker grouped by strike price across all contracts on a given market date....

**Parameters**:

| Name | Type | Location | Required | Description |
|------|------|----------|----------|-------------|
| ticker | string | path | Yes |  |
| date | string | query | No |  |

**Example**:
```bash
curl "/api/stock/AAPL/greek-exposure/strike" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/stock/README.md)

---

### `GET /api/stock/{ticker}/greek-exposure/strike-expiry`

**Summary**: Greek Exposure By Strike And Expiry

**Description**: The greek exposure of a ticker grouped by strike price for a specific expiry date....

**Parameters**:

| Name | Type | Location | Required | Description |
|------|------|----------|----------|-------------|
| ticker | string | path | Yes |  |
| date | string | query | No |  |
| expiry | string | query | Yes |  |

**Example**:
```bash
curl "/api/stock/AAPL/greek-exposure/strike-expiry" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/stock/README.md)

---

### `GET /api/stock/{ticker}/greek-flow`

**Summary**: Greek flow

**Description**: Returns the tickers greek flow (delta & vega flow) for the given market day broken down per minute.
Date must be the current or a past date. If no date is given, returns data for the current/last mark...

**Parameters**:

| Name | Type | Location | Required | Description |
|------|------|----------|----------|-------------|
| ticker | string | path | Yes |  |
| date | string | query | No |  |

**Example**:
```bash
curl "/api/stock/AAPL/greek-flow" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/stock/README.md)

---

### `GET /api/stock/{ticker}/greek-flow/{expiry}`

**Summary**: Greek flow by expiry

**Description**: Returns the tickers greek flow (delta & vega flow) for the given market day broken down per minute & expiry.
Date must be the current or a past date. If no date is given, returns data for the current/...

**Parameters**:

| Name | Type | Location | Required | Description |
|------|------|----------|----------|-------------|
| ticker | string | path | Yes |  |
| date | string | query | No |  |
| expiry | string | path | Yes |  |

**Example**:
```bash
curl "/api/stock/{ticker}/greek-flow/2025-12-19" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/stock/README.md)

---

### `GET /api/stock/{ticker}/greeks`

**Summary**: Greeks

**Description**: Returns the greeks for each strike for a single expiry date....

**Parameters**:

| Name | Type | Location | Required | Description |
|------|------|----------|----------|-------------|
| ticker | string | path | Yes |  |
| date | string | query | No |  |
| expiry | string | query | Yes |  |

**Example**:
```bash
curl "/api/stock/AAPL/greeks" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/stock/README.md)

---

### `GET /api/stock/{ticker}/historical-risk-reversal-skew`

**Summary**: Historical Risk Reversal Skew

**Description**: Returns the historical risk reversal skew (the difference between put and call volatility) at a delta of 25 or 10 (colloquial for 0.25 or 0.1) for a given expiry date....

**Parameters**:

| Name | Type | Location | Required | Description |
|------|------|----------|----------|-------------|
| ticker | string | path | Yes |  |
| date | string | query | No |  |
| expiry | string | query | Yes |  |
| timeframe | string | query | No |  |
| delta | string | query | Yes |  |

**Example**:
```bash
curl "/api/stock/AAPL/historical-risk-reversal-skew" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/stock/README.md)

---

### `GET /api/stock/{ticker}/info`

**Summary**: Information

**Description**: Returns a information about the given ticker....

**Parameters**:

| Name | Type | Location | Required | Description |
|------|------|----------|----------|-------------|
| ticker | string | path | Yes |  |

**Example**:
```bash
curl "/api/stock/AAPL/info" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/stock/README.md)

---

### `GET /api/stock/{ticker}/insider-buy-sells`

**Summary**: Insider buy & sells

**Description**: Returns the total amount of purchases & sells as well as notional values for insider transactions
for the given ticker...

**Parameters**:

| Name | Type | Location | Required | Description |
|------|------|----------|----------|-------------|
| ticker | string | path | Yes |  |

**Example**:
```bash
curl "/api/stock/AAPL/insider-buy-sells" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/stock/README.md)

---

### `GET /api/stock/{ticker}/interpolated-iv`

**Summary**: Interpolated IV

**Description**: Returns the Interpolated IV for a given trading day. If there is no expiration then the data is calcualted via linear interpolation
with the next 2 closest expirations

Date must be the current or a p...

**Parameters**:

| Name | Type | Location | Required | Description |
|------|------|----------|----------|-------------|
| ticker | string | path | Yes |  |
| date | string | query | No |  |

**Example**:
```bash
curl "/api/stock/AAPL/interpolated-iv" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/stock/README.md)

---

### `GET /api/stock/{ticker}/iv-rank`

**Summary**: IV Rank

**Description**: Returns the IV rank data for a ticker over a period of time.
IV rank is a measure of where current implied volatility stands relative to its historical range....

**Parameters**:

| Name | Type | Location | Required | Description |
|------|------|----------|----------|-------------|
| ticker | string | path | Yes |  |
| date | string | query | No |  |
| timespan | string | query | No |  |

**Example**:
```bash
curl "/api/stock/AAPL/iv-rank" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/stock/README.md)

---

### `GET /api/stock/{ticker}/max-pain`

**Summary**: Max Pain

**Description**: Returns the max pain for all expirations for the given ticker for the last 120 days...

**Parameters**:

| Name | Type | Location | Required | Description |
|------|------|----------|----------|-------------|
| ticker | string | path | Yes |  |
| date | string | query | No |  |

**Example**:
```bash
curl "/api/stock/AAPL/max-pain" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/stock/README.md)

---

### `GET /api/stock/{ticker}/net-prem-ticks`

**Summary**: Call/Put Net/Vol Ticks

**Description**: Returns the net premium ticks for a given ticker which can be used to build the following chart:
![Net Prem chart](https://i.imgur.com/Rom1kcB.png)

----
Each tick is resembling the data for a single ...

**Parameters**:

| Name | Type | Location | Required | Description |
|------|------|----------|----------|-------------|
| ticker | string | path | Yes |  |
| date | string | query | No |  |

**Example**:
```bash
curl "/api/stock/AAPL/net-prem-ticks" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/stock/README.md)

---

### `GET /api/stock/{ticker}/nope`

**Summary**: Nope

**Description**: Returns the tickers NOPE for the given market day broken down per minute.

NOPE is the Net Options Pricing Effect, which tracks the intraday net delta of any ticker, but most research has been done on...

**Parameters**:

| Name | Type | Location | Required | Description |
|------|------|----------|----------|-------------|
| ticker | string | path | Yes |  |
| date | string | query | No |  |

**Example**:
```bash
curl "/api/stock/AAPL/nope" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/stock/README.md)

---

### `GET /api/stock/{ticker}/ohlc/{candle_size}`

**Summary**: OHLC

**Description**: Returns the Open High Low Close (OHLC) candle data for a given ticker.

Results are limited to 2,500 elements even if there are more available.

Note: If you select 1d as a candle_size then the candle...

**Parameters**:

| Name | Type | Location | Required | Description |
|------|------|----------|----------|-------------|
| ticker | string | path | Yes |  |
| candle_size | string | path | Yes |  |
| timeframe | string | query | No |  |
| end_date | string | query | No |  |
| date | string | query | No |  |
| limit | string | query | No |  |

**Example**:
```bash
curl "/api/stock/{ticker}/ohlc/1D" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/stock/README.md)

---

### `GET /api/stock/{ticker}/oi-change`

**Summary**: OI Change

**Description**: Returns the tickers contracts' OI change data ordered by absolute OI change (default: descending).
Date must be the current or a past date. If no date is given, returns data for the current/last marke...

**Parameters**:

| Name | Type | Location | Required | Description |
|------|------|----------|----------|-------------|
| ticker | string | path | Yes |  |
| date | string | query | No |  |
| limit | string | query | No |  |
| page | string | query | No |  |
| order | string | query | No |  |

**Example**:
```bash
curl "/api/stock/AAPL/oi-change" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/stock/README.md)

---

### `GET /api/stock/{ticker}/oi-per-expiry`

**Summary**: OI per Expiry

**Description**: Returns the total open interest for calls and puts for a specific expiry date....

**Parameters**:

| Name | Type | Location | Required | Description |
|------|------|----------|----------|-------------|
| ticker | string | path | Yes |  |
| date | string | query | No |  |

**Example**:
```bash
curl "/api/stock/AAPL/oi-per-expiry" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/stock/README.md)

---

### `GET /api/stock/{ticker}/oi-per-strike`

**Summary**: OI per Strike

**Description**: Returns the total open interest for calls and puts for a specific strike....

**Parameters**:

| Name | Type | Location | Required | Description |
|------|------|----------|----------|-------------|
| ticker | string | path | Yes |  |
| date | string | query | No |  |

**Example**:
```bash
curl "/api/stock/AAPL/oi-per-strike" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/stock/README.md)

---

### `GET /api/stock/{ticker}/option-chains`

**Summary**: Option Chains

**Description**: Returns all option symbols for the given ticker that were present at the given day.

If no date is given, returns data for the current/last market day.

You can use the following regex to extract unde...

**Parameters**:

| Name | Type | Location | Required | Description |
|------|------|----------|----------|-------------|
| ticker | string | path | Yes |  |
| date | string | query | No |  |

**Example**:
```bash
curl "/api/stock/AAPL/option-chains" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/stock/README.md)

---

### `GET /api/stock/{ticker}/option-contracts`

**Summary**: Option contracts

**Description**: Returns all option contracts for the given ticker...

**Parameters**:

| Name | Type | Location | Required | Description |
|------|------|----------|----------|-------------|
| ticker | string | path | Yes |  |
| expiry | string | query | No |  |
| option_type | string | query | No |  |
| vol_greater_oi | boolean | query | No | Wether to only return chains where volume > open i |
| exclude_zero_vol_chains | boolean | query | No | Wether to only return chains where volume > 0 |
| exclude_zero_dte | boolean | query | No | Wether to only return chains which do not expire o |
| exclude_zero_oi_chains | boolean | query | No | Wether to only return chains where open interest > |
| maybe_otm_only | boolean | query | No | Wether to only return chains which are out of the  |
| option_symbol | array | query | No | Options symbols to filter by |
| limit | string | query | No |  |

*...and 1 more parameters*

**Example**:
```bash
curl "/api/stock/AAPL/option-contracts" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/stock/README.md)

---

### `GET /api/stock/{ticker}/option/stock-price-levels`

**Summary**: Option Price Levels

**Description**: Returns the call and put volume per price level for the given ticker.

----
Can be used to build a chart such as following:
![Option Price Level chart](https://i.imgur.com/y6BZ4sG.png)...

**Parameters**:

| Name | Type | Location | Required | Description |
|------|------|----------|----------|-------------|
| ticker | string | path | Yes |  |
| date | string | query | No |  |

**Example**:
```bash
curl "/api/stock/AAPL/option/stock-price-levels" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/stock/README.md)

---

### `GET /api/stock/{ticker}/option/volume-oi-expiry`

**Summary**: Volume & OI per Expiry

**Description**: Returns the total volume and open interest per expiry for the given ticker....

**Parameters**:

| Name | Type | Location | Required | Description |
|------|------|----------|----------|-------------|
| ticker | string | path | Yes |  |
| date | string | query | No |  |

**Example**:
```bash
curl "/api/stock/AAPL/option/volume-oi-expiry" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/stock/README.md)

---

### `GET /api/stock/{ticker}/options-volume`

**Summary**: Options Volume

**Description**: Returns the options volume & premium for all trade executions
that happened on a given trading date for the given ticker.

----
This can be used to build a ticker options overview such as:

![Table](h...

**Parameters**:

| Name | Type | Location | Required | Description |
|------|------|----------|----------|-------------|
| ticker | string | path | Yes |  |
| limit | string | query | No |  |

**Example**:
```bash
curl "/api/stock/AAPL/options-volume" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/stock/README.md)

---

### `GET /api/stock/{ticker}/spot-exposures`

**Summary**: Spot GEX exposures per 1min

**Description**: Returns the spot GEX exposures for the given ticker per minute.

Spot GEX is the assumed $ value of the given greek (ie. gamma) exposure that market makers need to hedge per 1% change of the underlyin...

**Parameters**:

| Name | Type | Location | Required | Description |
|------|------|----------|----------|-------------|
| ticker | string | path | Yes |  |
| date | string | query | No |  |

**Example**:
```bash
curl "/api/stock/AAPL/spot-exposures" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/stock/README.md)

---

### `GET /api/stock/{ticker}/spot-exposures/expiry-strike`

**Summary**: Spot GEX exposures by strike & expiry

**Description**: Returns the most recent spot GEX exposures across all strikes for the given ticker & expiration on a given date. Calculated either with open interest or with volume.

Data is available since 2025-01-1...

**Parameters**:

| Name | Type | Location | Required | Description |
|------|------|----------|----------|-------------|
| ticker | string | path | Yes |  |
| expirations[] | string | query | Yes |  |
| date | string | query | No |  |
| limit | string | query | No |  |
| page | string | query | No |  |
| min_strike | string | query | No |  |
| max_strike | string | query | No |  |
| min_dte | string | query | No |  |
| max_dte | string | query | No |  |

**Example**:
```bash
curl "/api/stock/AAPL/spot-exposures/expiry-strike" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/stock/README.md)

---

### `GET /api/stock/{ticker}/spot-exposures/strike`

**Summary**: Spot GEX exposures by strike

**Description**: Returns the most recent spot GEX exposures across all strikes for the given ticker on a given date. Calculated either with open interest or with volume.

Spot GEX is the assumed $ value of the given g...

**Parameters**:

| Name | Type | Location | Required | Description |
|------|------|----------|----------|-------------|
| ticker | string | path | Yes |  |
| date | string | query | No |  |
| min_strike | string | query | No |  |
| max_strike | string | query | No |  |
| limit | string | query | No |  |
| page | string | query | No |  |

**Example**:
```bash
curl "/api/stock/AAPL/spot-exposures/strike" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/stock/README.md)

---

### `GET /api/stock/{ticker}/spot-exposures/{expiry}/strike`

**Summary**: Spot GEX exposures by strike & expiry (Deprecated)

**Description**: This endpoint has been deprecated and will be removed, please migrate to the new [endpoint](https://api.unusualwhales.com/docs#/operations/PublicApi.TickerController.spot_exposures_by_strike_expiry_v2...

**Parameters**:

| Name | Type | Location | Required | Description |
|------|------|----------|----------|-------------|
| ticker | string | path | Yes |  |
| expiry | string | path | Yes |  |
| date | string | query | No |  |
| min_strike | string | query | No |  |
| max_strike | string | query | No |  |

**Example**:
```bash
curl "/api/stock/{ticker}/spot-exposures/2025-12-19/strike" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/stock/README.md)

---

### `GET /api/stock/{ticker}/stock-state`

**Summary**: Stock State

**Description**: Returns the last stock state for the given ticker.

This is the easiest way to retreive the open, close, high, low and volume of the last trading day....

**Parameters**:

| Name | Type | Location | Required | Description |
|------|------|----------|----------|-------------|
| ticker | string | path | Yes |  |

**Example**:
```bash
curl "/api/stock/AAPL/stock-state" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/stock/README.md)

---

### `GET /api/stock/{ticker}/stock-volume-price-levels`

**Summary**: Off/Lit Price Levels

**Description**: Returns the lit & off lit stock volume per price level for the given ticker.

----
Important: The volume does **NOT** represent the full market dialy volume. It
only represents the volume of executed ...

**Parameters**:

| Name | Type | Location | Required | Description |
|------|------|----------|----------|-------------|
| ticker | string | path | Yes |  |
| date | string | query | No |  |

**Example**:
```bash
curl "/api/stock/AAPL/stock-volume-price-levels" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/stock/README.md)

---

### `GET /api/stock/{ticker}/volatility/realized`

**Summary**: Realized Volatility

**Description**: The implied and realized volatility of a given ticker. The implied volatility is the expected 30 day forward looking volatility.

The realized/historical volatility is the volatility of the stock pric...

**Parameters**:

| Name | Type | Location | Required | Description |
|------|------|----------|----------|-------------|
| ticker | string | path | Yes |  |
| date | string | query | No |  |
| timeframe | string | query | No |  |

**Example**:
```bash
curl "/api/stock/AAPL/volatility/realized" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/stock/README.md)

---

### `GET /api/stock/{ticker}/volatility/stats`

**Summary**: Volatility Statistics

**Description**: Returns comprehensive volatility statistics for a ticker on a specific date, including
implied volatility data, realized volatility data, and their respective high/low values
for the past year....

**Parameters**:

| Name | Type | Location | Required | Description |
|------|------|----------|----------|-------------|
| ticker | string | path | Yes |  |
| date | string | query | No |  |

**Example**:
```bash
curl "/api/stock/AAPL/volatility/stats" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/stock/README.md)

---

### `GET /api/stock/{ticker}/volatility/term-structure`

**Summary**: Implied Volatility Term Structure

**Description**: The average of the latest volatilities for the at the money call and put contracts for every expiry date....

**Parameters**:

| Name | Type | Location | Required | Description |
|------|------|----------|----------|-------------|
| ticker | string | path | Yes |  |
| date | string | query | No |  |

**Example**:
```bash
curl "/api/stock/AAPL/volatility/term-structure" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Documentation**: [View Details](./docs/stock/README.md)

---


## Authentication

All endpoints require authentication via Bearer token:

```bash
Authorization: Bearer YOUR_API_KEY
```

Get your API key at: https://unusualwhales.com

---

## Rate Limiting

- Standard rate limits apply
- Limits vary by subscription tier
- Implement exponential backoff for retries

---

## Common Parameters

### Query Parameters (Many Endpoints)

| Parameter | Type | Description |
|-----------|------|-------------|
| limit | integer | Limit number of results (default varies) |
| offset | integer | Offset for pagination |
| date | string | Date filter (ISO 8601 format) |
| newer_than | string | Filter records newer than timestamp |
| older_than | string | Filter records older than timestamp |

### Path Parameters

| Parameter | Description | Example |
|-----------|-------------|---------|
| {ticker} | Stock ticker symbol | AAPL, SPY, TSLA |
| {id} | Option contract ID | AAPL251219C00175000 |
| {name} | Institution name | VANGUARD GROUP INC |
| {sector} | Sector name | Technology, Healthcare |
| {expiry} | Expiration date | 2025-12-19 |

---

## Response Format

All endpoints return JSON with this structure:

```json
{
  "data": [...],  // Array of results or single object
  "count": 100    // Optional: total count
}
```

---

## Error Responses

| Code | Meaning |
|------|---------|
| 400 | Bad Request - Invalid parameters |
| 401 | Unauthorized - Invalid API key |
| 403 | Forbidden - Insufficient permissions |
| 404 | Not Found - Resource doesn't exist |
| 429 | Too Many Requests - Rate limit exceeded |
| 500 | Internal Server Error |

---

## Related Documentation

- [README.md](./README.md) - Overview and getting started
- [ENDPOINT_RELATIONSHIPS.md](./ENDPOINT_RELATIONSHIPS.md) - How endpoints connect
- [DATA_FLOW_EXAMPLES.md](./DATA_FLOW_EXAMPLES.md) - Integration patterns
- [QUICK_CHAINS.md](./QUICK_CHAINS.md) - Common endpoint combinations
- [Individual endpoint docs](./docs/) - Detailed documentation

---

## Categories Summary

| Category | Endpoints | Description |
|----------|-----------|-------------|
| alerts | 2 | User alerts and notifications |
| congress | 3 | Congressional trading activity |
| darkpool | 2 | Dark pool trading data |
| earnings | 3 | Earnings calendar and history |
| etfs | 5 | ETF holdings and exposure |
| group-flow | 2 | Grouped options flow |
| insider | 4 | Insider trading activity |
| institution | 4 | Institutional holdings |
| institutions | 2 | Institution listings |
| market | 12 | Market-wide indicators |
| net-flow | 1 | Net premium flow |
| news | 1 | Financial news headlines |
| option-contract | 4 | Option contract details |
| option-trades | 2 | Options trading activity |
| politician-portfolios | 3 | Politician portfolios |
| screener | 3 | Stock and option screeners |
| seasonality | 4 | Seasonal patterns |
| shorts | 5 | Short selling data |
| socket | 6 | WebSocket connections |
| stock | 41 | Stock and options data |

**Total**: 109 endpoints across 20 categories
