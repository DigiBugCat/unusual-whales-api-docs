# Agent 1 API Endpoints - Quick Reference Guide

## Overview
This guide provides quick reference information for the 10 API endpoints documented by Agent 1. All endpoints have been tested and validated.

## Base URL
```
https://api.unusualwhales.com
```

## Authentication
All endpoints require Bearer token authentication:
```
Authorization: Bearer YOUR_API_KEY
```

---

## Alerts Endpoints

### 1. Get Alerts
**Path**: `GET /api/alerts`

**File**: `/docs/alerts/get-alerts.md`

**Description**: Returns all alerts triggered for the user

**Key Parameters**:
- `limit` (query): Result limit (default 50, max 500)
- `newer_than` (query): Filter by creation timestamp (ISO format or unix seconds)
- `older_than` (query): Filter by creation timestamp (max 14 days lookback)
- `ticker_symbols` (query): Filter by specific tickers
- `config_ids[]` (query): Filter by alert configuration IDs
- `noti_types[]` (query): Filter by notification types
- `intraday_only` (query): Filter for intraday alerts only

**Quick Example**:
```bash
curl -X GET "https://api.unusualwhales.com/api/alerts?limit=10" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

---

### 2. Alert Configurations
**Path**: `GET /api/alerts/configuration`

**File**: `/docs/alerts/alert-configurations.md`

**Description**: Returns alert configurations available to the user

**Key Parameters**: None required

**Quick Example**:
```bash
curl -X GET "https://api.unusualwhales.com/api/alerts/configuration" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

---

## Congress Endpoints

### 3. Congress Trader Reports
**Path**: `GET /api/congress/congress-trader`

**File**: `/docs/congress/congress-trader.md`

**Description**: Returns recent trading reports by congress members

**Key Parameters**:
- `limit` (query): Result limit (default 100, max 200)
- `name` (query): Congress member name filter
- `ticker` (query): Stock ticker filter
- `date` (query): Report date filter

**Quick Example**:
```bash
curl -X GET "https://api.unusualwhales.com/api/congress/congress-trader?limit=10" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

---

### 4. Congress Late Reports
**Path**: `GET /api/congress/late-reports`

**File**: `/docs/congress/congress-late-reports.md`

**Description**: Returns late trading reports filed by congress members

**Key Parameters**:
- `limit` (query): Result limit (default 100, max 200)
- `date` (query): Report date filter
- `ticker` (query): Stock ticker filter

**Quick Example**:
```bash
curl -X GET "https://api.unusualwhales.com/api/congress/late-reports?limit=10" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

---

### 5. Congress Recent Trades
**Path**: `GET /api/congress/recent-trades`

**File**: `/docs/congress/congress-recent-trades.md`

**Description**: Returns latest transacted trades by congress members

**Key Parameters**:
- `limit` (query): Result limit (default 100, max 200)
- `date` (query): Transaction date filter
- `ticker` (query): Stock ticker filter

**Quick Example**:
```bash
curl -X GET "https://api.unusualwhales.com/api/congress/recent-trades?limit=10" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

---

## Darkpool Endpoints

### 6. Recent Darkpool Trades
**Path**: `GET /api/darkpool/recent`

**File**: `/docs/darkpool/darkpool-recent.md`

**Description**: Returns the latest darkpool trades across all symbols

**Key Parameters**:
- `limit` (query): Result limit (default 100, max 200)
- `date` (query): Trade date filter
- `min_premium` (query): Minimum price premium
- `max_premium` (query): Maximum price premium
- `min_size` (query): Minimum trade size
- `max_size` (query): Maximum trade size
- `min_volume` (query): Minimum volume
- `max_volume` (query): Maximum volume

**Quick Example**:
```bash
curl -X GET "https://api.unusualwhales.com/api/darkpool/recent?limit=10" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

---

### 7. Ticker Darkpool Trades
**Path**: `GET /api/darkpool/{ticker}`

**File**: `/docs/darkpool/darkpool-ticker.md`

**Description**: Returns darkpool trades for a specific ticker

**Key Parameters**:
- `ticker` (path, required): Stock ticker symbol (e.g., AAPL)
- `date` (query): Trade date filter
- `newer_than` (query): Filter by timestamp
- `older_than` (query): Filter by timestamp
- `min_premium`, `max_premium`, `min_size`, `max_size`, `min_volume`, `max_volume` (query): Range filters

**Quick Example**:
```bash
curl -X GET "https://api.unusualwhales.com/api/darkpool/AAPL?limit=10" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

---

## Earnings Endpoints

### 8. Afterhours Earnings
**Path**: `GET /api/earnings/afterhours`

**File**: `/docs/earnings/earnings-afterhours.md`

**Description**: Returns afterhours earnings announcements for a given date

**Key Parameters**: None required (returns current day by default)

**Quick Example**:
```bash
curl -X GET "https://api.unusualwhales.com/api/earnings/afterhours" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

---

### 9. Premarket Earnings
**Path**: `GET /api/earnings/premarket`

**File**: `/docs/earnings/earnings-premarket.md`

**Description**: Returns premarket earnings announcements for a given date

**Key Parameters**: None required (returns current day by default)

**Quick Example**:
```bash
curl -X GET "https://api.unusualwhales.com/api/earnings/premarket" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

---

### 10. Historical Ticker Earnings
**Path**: `GET /api/earnings/{ticker}`

**File**: `/docs/earnings/earnings-ticker.md`

**Description**: Returns historical earnings data for a specific ticker

**Key Parameters**:
- `ticker` (path, required): Stock ticker symbol (e.g., AAPL)

**Quick Example**:
```bash
curl -X GET "https://api.unusualwhales.com/api/earnings/AAPL" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

---

## Common HTTP Status Codes

| Code | Meaning |
|------|---------|
| 200 | OK - Successful request |
| 400 | Bad Request - Invalid parameters |
| 401 | Unauthorized - Invalid or missing API key |
| 422 | Unprocessable Entity - Invalid filter parameters |
| 500 | Internal Server Error - Server error |

---

## Testing Status

**All endpoints tested and validated**: 10/10 (100%)

**Test Date**: 2025-10-22

**All responses returned**: 200 OK

---

## Documentation Files

Complete documentation for each endpoint is available in:

```
docs/
├── alerts/
│   ├── get-alerts.md
│   └── alert-configurations.md
├── congress/
│   ├── congress-trader.md
│   ├── congress-late-reports.md
│   └── congress-recent-trades.md
├── darkpool/
│   ├── darkpool-recent.md
│   └── darkpool-ticker.md
└── earnings/
    ├── earnings-afterhours.md
    ├── earnings-premarket.md
    └── earnings-ticker.md
```

---

## Tips for Using These Endpoints

1. **Rate Limiting**: Monitor your request rate to avoid hitting rate limits
2. **Pagination**: Use the `limit` parameter to control result set size
3. **Filtering**: Use query parameters to narrow down results
4. **Timestamps**: Use ISO 8601 format or unix timestamps for date filtering
5. **Error Handling**: Implement proper error handling for 4xx and 5xx responses

---

## Next Steps

- Review the detailed documentation files for each endpoint
- Test endpoints with your API key
- Implement error handling for all responses
- Monitor rate limiting headers in responses

For complete documentation, refer to individual endpoint markdown files in the `docs/` directory.
