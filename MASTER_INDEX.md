# Unusual Whales API - Master Index

**Total Endpoints**: 109

**Categories**: 20

**Documentation Status**: In Progress

**Last Updated**: 2025-10-22

---

## Progress Overview

| Category | Endpoints | Documented | Status |
|----------|-----------|------------|--------|
| alerts | 2 | 0/2 | 🔴 Not Started |
| congress | 3 | 0/3 | 🔴 Not Started |
| darkpool | 2 | 0/2 | 🔴 Not Started |
| earnings | 3 | 0/3 | 🔴 Not Started |
| etfs | 5 | 0/5 | 🔴 Not Started |
| group-flow | 2 | 0/2 | 🔴 Not Started |
| insider | 4 | 0/4 | 🔴 Not Started |
| institution | 4 | 0/4 | 🔴 Not Started |
| institutions | 2 | 0/2 | 🔴 Not Started |
| market | 12 | 0/12 | 🔴 Not Started |
| net-flow | 1 | 0/1 | 🔴 Not Started |
| news | 1 | 0/1 | 🔴 Not Started |
| option-contract | 4 | 0/4 | 🔴 Not Started |
| option-trades | 2 | 0/2 | 🔴 Not Started |
| politician-portfolios | 3 | 0/3 | 🔴 Not Started |
| screener | 3 | 0/3 | 🔴 Not Started |
| seasonality | 4 | 0/4 | 🔴 Not Started |
| shorts | 5 | 0/5 | 🔴 Not Started |
| socket | 6 | 0/6 | 🔴 Not Started |
| stock | 41 | 0/41 | 🔴 Not Started |

---

## Endpoints by Category


### Alerts (2 endpoints)

| # | Path | Method | Summary | Status |
|---|------|--------|---------|--------|
| 1 | `/api/alerts` | GET | Alerts | 🔴 |
| 2 | `/api/alerts/configuration` | GET | Alert configurations | 🔴 |

### Congress (3 endpoints)

| # | Path | Method | Summary | Status |
|---|------|--------|---------|--------|
| 1 | `/api/congress/congress-trader` | GET | Recent Reports By Trader | 🔴 |
| 2 | `/api/congress/late-reports` | GET | Recent Late Reports | 🔴 |
| 3 | `/api/congress/recent-trades` | GET | Recent Congress Trades | 🔴 |

### Darkpool (2 endpoints)

| # | Path | Method | Summary | Status |
|---|------|--------|---------|--------|
| 1 | `/api/darkpool/recent` | GET | Recent Darkpool Trades | 🔴 |
| 2 | `/api/darkpool/{ticker}` | GET | Ticker Darkpool Trades | 🔴 |

### Earnings (3 endpoints)

| # | Path | Method | Summary | Status |
|---|------|--------|---------|--------|
| 1 | `/api/earnings/afterhours` | GET | Afterhours | 🔴 |
| 2 | `/api/earnings/premarket` | GET | Premarket | 🔴 |
| 3 | `/api/earnings/{ticker}` | GET | Historical Ticker Earnings | 🔴 |

### Etfs (5 endpoints)

| # | Path | Method | Summary | Status |
|---|------|--------|---------|--------|
| 1 | `/api/etfs/{ticker}/exposure` | GET | Exposure | 🔴 |
| 2 | `/api/etfs/{ticker}/holdings` | GET | Holdings | 🔴 |
| 3 | `/api/etfs/{ticker}/in-outflow` | GET | Inflow & Outflow | 🔴 |
| 4 | `/api/etfs/{ticker}/info` | GET | Information | 🔴 |
| 5 | `/api/etfs/{ticker}/weights` | GET | Sector & Country weights | 🔴 |

### Group-Flow (2 endpoints)

| # | Path | Method | Summary | Status |
|---|------|--------|---------|--------|
| 1 | `/api/group-flow/{flow_group}/greek-flow` | GET | Greek flow | 🔴 |
| 2 | `/api/group-flow/{flow_group}/greek-flow/{expiry}` | GET | Greek flow by expiry | 🔴 |

### Insider (4 endpoints)

| # | Path | Method | Summary | Status |
|---|------|--------|---------|--------|
| 1 | `/api/insider/transactions` | GET | Transactions | 🔴 |
| 2 | `/api/insider/{sector}/sector-flow` | GET | Sector Flow | 🔴 |
| 3 | `/api/insider/{ticker}` | GET | Insiders | 🔴 |
| 4 | `/api/insider/{ticker}/ticker-flow` | GET | Ticker Flow | 🔴 |

### Institution (4 endpoints)

| # | Path | Method | Summary | Status |
|---|------|--------|---------|--------|
| 1 | `/api/institution/{name}/activity` | GET | Institutional Activity | 🔴 |
| 2 | `/api/institution/{name}/holdings` | GET | Institutional Holdings | 🔴 |
| 3 | `/api/institution/{name}/sectors` | GET | Sector Exposure | 🔴 |
| 4 | `/api/institution/{ticker}/ownership` | GET | Institutional Ownership | 🔴 |

### Institutions (2 endpoints)

| # | Path | Method | Summary | Status |
|---|------|--------|---------|--------|
| 1 | `/api/institutions` | GET | List of Institutions | 🔴 |
| 2 | `/api/institutions/latest_filings` | GET | Latest Filings | 🔴 |

### Market (12 endpoints)

| # | Path | Method | Summary | Status |
|---|------|--------|---------|--------|
| 1 | `/api/market/correlations` | GET | Correlations | 🔴 |
| 2 | `/api/market/economic-calendar` | GET | Economic calendar | 🔴 |
| 3 | `/api/market/fda-calendar` | GET | FDA Calendar | 🔴 |
| 4 | `/api/market/insider-buy-sells` | GET | Total Insider Buy & Sells | 🔴 |
| 5 | `/api/market/market-tide` | GET | Market Tide | 🔴 |
| 6 | `/api/market/oi-change` | GET | OI Change | 🔴 |
| 7 | `/api/market/sector-etfs` | GET | Sector Etfs | 🔴 |
| 8 | `/api/market/spike` | GET | SPIKE | 🔴 |
| 9 | `/api/market/top-net-impact` | GET | Top Net Impact | 🔴 |
| 10 | `/api/market/total-options-volume` | GET | Total Options Volume | 🔴 |
| 11 | `/api/market/{sector}/sector-tide` | GET | Sector Tide | 🔴 |
| 12 | `/api/market/{ticker}/etf-tide` | GET | ETF Tide | 🔴 |

### Net-Flow (1 endpoints)

| # | Path | Method | Summary | Status |
|---|------|--------|---------|--------|
| 1 | `/api/net-flow/expiry` | GET | Net Flow Expiry | 🔴 |

### News (1 endpoints)

| # | Path | Method | Summary | Status |
|---|------|--------|---------|--------|
| 1 | `/api/news/headlines` | GET | News Headlines | 🔴 |

### Option-Contract (4 endpoints)

| # | Path | Method | Summary | Status |
|---|------|--------|---------|--------|
| 1 | `/api/option-contract/{id}/flow` | GET | Flow Data | 🔴 |
| 2 | `/api/option-contract/{id}/historic` | GET | Historic Data | 🔴 |
| 3 | `/api/option-contract/{id}/intraday` | GET | Intraday Data | 🔴 |
| 4 | `/api/option-contract/{id}/volume-profile` | GET | Volume Profile | 🔴 |

### Option-Trades (2 endpoints)

| # | Path | Method | Summary | Status |
|---|------|--------|---------|--------|
| 1 | `/api/option-trades/flow-alerts` | GET | Flow Alerts | 🔴 |
| 2 | `/api/option-trades/full-tape/{date}` | GET | Full Tape | 🔴 |

### Politician-Portfolios (3 endpoints)

| # | Path | Method | Summary | Status |
|---|------|--------|---------|--------|
| 1 | `/api/politician-portfolios/holders/{ticker}` | GET | Politician Portfolio Holders by Ticker | 🔴 |
| 2 | `/api/politician-portfolios/people` | GET | Politicians List | 🔴 |
| 3 | `/api/politician-portfolios/{politician_id}` | GET | Politician Portfolios | 🔴 |

### Screener (3 endpoints)

| # | Path | Method | Summary | Status |
|---|------|--------|---------|--------|
| 1 | `/api/screener/analysts` | GET | Analyst Rating | 🔴 |
| 2 | `/api/screener/option-contracts` | GET | Hottest Chains | 🔴 |
| 3 | `/api/screener/stocks` | GET | Stock Screener | 🔴 |

### Seasonality (4 endpoints)

| # | Path | Method | Summary | Status |
|---|------|--------|---------|--------|
| 1 | `/api/seasonality/market` | GET | Market Seasonality | 🔴 |
| 2 | `/api/seasonality/{month}/performers` | GET | Month Performers | 🔴 |
| 3 | `/api/seasonality/{ticker}/monthly` | GET | Average return per month | 🔴 |
| 4 | `/api/seasonality/{ticker}/year-month` | GET | Price change per month per year | 🔴 |

### Shorts (5 endpoints)

| # | Path | Method | Summary | Status |
|---|------|--------|---------|--------|
| 1 | `/api/shorts/{ticker}/data` | GET | Short Data | 🔴 |
| 2 | `/api/shorts/{ticker}/ftds` | GET | Failures to Deliver | 🔴 |
| 3 | `/api/shorts/{ticker}/interest-float` | GET | Short Interest and Float | 🔴 |
| 4 | `/api/shorts/{ticker}/volume-and-ratio` | GET | Short Volume and Ratio | 🔴 |
| 5 | `/api/shorts/{ticker}/volumes-by-exchange` | GET | Short Volume By Exchange | 🔴 |

### Socket (6 endpoints)

| # | Path | Method | Summary | Status |
|---|------|--------|---------|--------|
| 1 | `/api/socket` | GET | WebSocket channels | 🔴 |
| 2 | `/api/socket/flow_alerts` | GET | Flow alerts | 🔴 |
| 3 | `/api/socket/gex` | GET | GEX | 🔴 |
| 4 | `/api/socket/news` | GET | News | 🔴 |
| 5 | `/api/socket/option_trades` | GET | Option trades | 🔴 |
| 6 | `/api/socket/price` | GET | Price | 🔴 |

### Stock (41 endpoints)

| # | Path | Method | Summary | Status |
|---|------|--------|---------|--------|
| 1 | `/api/stock/{sector}/tickers` | GET | Companies in Sector | 🔴 |
| 2 | `/api/stock/{ticker}/atm-chains` | GET | ATM Chains | 🔴 |
| 3 | `/api/stock/{ticker}/expiry-breakdown` | GET | Expiry Breakdown | 🔴 |
| 4 | `/api/stock/{ticker}/flow-alerts` | GET | Flow Alerts | 🔴 |
| 5 | `/api/stock/{ticker}/flow-per-expiry` | GET | Flow per expiry | 🔴 |
| 6 | `/api/stock/{ticker}/flow-per-strike` | GET | Flow per strike | 🔴 |
| 7 | `/api/stock/{ticker}/flow-per-strike-intraday` | GET | Flow per strike intraday | 🔴 |
| 8 | `/api/stock/{ticker}/flow-recent` | GET | Recent flows | 🔴 |
| 9 | `/api/stock/{ticker}/greek-exposure` | GET | Greek Exposure | 🔴 |
| 10 | `/api/stock/{ticker}/greek-exposure/expiry` | GET | Greek Exposure By Expiry | 🔴 |
| 11 | `/api/stock/{ticker}/greek-exposure/strike` | GET | Greek Exposure By Strike | 🔴 |
| 12 | `/api/stock/{ticker}/greek-exposure/strike-expiry` | GET | Greek Exposure By Strike And Expiry | 🔴 |
| 13 | `/api/stock/{ticker}/greek-flow` | GET | Greek flow | 🔴 |
| 14 | `/api/stock/{ticker}/greek-flow/{expiry}` | GET | Greek flow by expiry | 🔴 |
| 15 | `/api/stock/{ticker}/greeks` | GET | Greeks | 🔴 |
| 16 | `/api/stock/{ticker}/historical-risk-reversal-skew` | GET | Historical Risk Reversal Skew | 🔴 |
| 17 | `/api/stock/{ticker}/info` | GET | Information | 🔴 |
| 18 | `/api/stock/{ticker}/insider-buy-sells` | GET | Insider buy & sells | 🔴 |
| 19 | `/api/stock/{ticker}/interpolated-iv` | GET | Interpolated IV | 🔴 |
| 20 | `/api/stock/{ticker}/iv-rank` | GET | IV Rank | 🔴 |
| 21 | `/api/stock/{ticker}/max-pain` | GET | Max Pain | 🔴 |
| 22 | `/api/stock/{ticker}/net-prem-ticks` | GET | Call/Put Net/Vol Ticks | 🔴 |
| 23 | `/api/stock/{ticker}/nope` | GET | Nope | 🔴 |
| 24 | `/api/stock/{ticker}/ohlc/{candle_size}` | GET | OHLC | 🔴 |
| 25 | `/api/stock/{ticker}/oi-change` | GET | OI Change | 🔴 |
| 26 | `/api/stock/{ticker}/oi-per-expiry` | GET | OI per Expiry | 🔴 |
| 27 | `/api/stock/{ticker}/oi-per-strike` | GET | OI per Strike | 🔴 |
| 28 | `/api/stock/{ticker}/option-chains` | GET | Option Chains | 🔴 |
| 29 | `/api/stock/{ticker}/option-contracts` | GET | Option contracts | 🔴 |
| 30 | `/api/stock/{ticker}/option/stock-price-levels` | GET | Option Price Levels | 🔴 |
| 31 | `/api/stock/{ticker}/option/volume-oi-expiry` | GET | Volume & OI per Expiry | 🔴 |
| 32 | `/api/stock/{ticker}/options-volume` | GET | Options Volume | 🔴 |
| 33 | `/api/stock/{ticker}/spot-exposures` | GET | Spot GEX exposures per 1min | 🔴 |
| 34 | `/api/stock/{ticker}/spot-exposures/expiry-strike` | GET | Spot GEX exposures by strike & expiry | 🔴 |
| 35 | `/api/stock/{ticker}/spot-exposures/strike` | GET | Spot GEX exposures by strike | 🔴 |
| 36 | `/api/stock/{ticker}/spot-exposures/{expiry}/strike` | GET | Spot GEX exposures by strike & expiry (Deprecated) | 🔴 |
| 37 | `/api/stock/{ticker}/stock-state` | GET | Stock State | 🔴 |
| 38 | `/api/stock/{ticker}/stock-volume-price-levels` | GET | Off/Lit Price Levels | 🔴 |
| 39 | `/api/stock/{ticker}/volatility/realized` | GET | Realized Volatility | 🔴 |
| 40 | `/api/stock/{ticker}/volatility/stats` | GET | Volatility Statistics | 🔴 |
| 41 | `/api/stock/{ticker}/volatility/term-structure` | GET | Implied Volatility Term Structure | 🔴 |


---

## Legend

- 🔴 Not Started
- 🟡 In Progress
- 🟢 Completed
- ✅ Validated

---

## Notes

- Each endpoint will have its own dedicated markdown file
- Files are organized by category in the `docs/` directory
- Use the ENDPOINT_TEMPLATE.md as a starting point for new documentation
- All endpoints should be tested with actual API calls before marking as completed
