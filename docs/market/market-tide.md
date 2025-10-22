# Market Tide

## Endpoint Details

**Path**: `GET /api/market/market-tide`

**Operation ID**: `PublicApi.MarketController.market_tide`

**Summary**: Market Tide - Real-time proprietary sentiment indicator based on options market activity

**Tags**: market

## Description

Market Tide is a proprietary tool that provides real-time data based on a proprietary formula that examines market-wide options activity and filters out noise. The Market Tide chart provides sentiment indicators broken down by minute intervals.

The indicator calculates net premium flow based on transactions at the ask (bullish) versus bid (bearish) prices:
- Transactions at the ask increase net call/put premium (bullish for calls, bearish for puts)
- Transactions at the bid decrease net call/put premium (bearish for calls, bullish for puts)
- Transactions at the mid are not accounted for

Date must be the current or a past date. If no date is given, returns data for the current/last market day.

Per default data are returned in 1 minute intervals. Use `interval_5m=true` to have this return data in 5 minute intervals instead.

Data goes back to 2022-09-28.

## Authentication

- **Required**: Yes
- **Type**: API Key
- **Header**: `Authorization: Bearer YOUR_API_KEY`

## Request Parameters

### Query Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| date | string | No | current/last market day | Market date in YYYY-MM-DD format |
| otm_only | boolean | No | false | Filter to only out-of-the-money (OTM) contracts |
| interval_5m | boolean | No | false | Return data in 5-minute candles instead of 1-minute |

## Example Requests

### cURL

```bash
curl -X GET "https://api.unusualwhales.com/api/market/market-tide" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

With 5-minute intervals:
```bash
curl -X GET "https://api.unusualwhales.com/api/market/market-tide?interval_5m=true" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

### Python

```python
import requests

url = "https://api.unusualwhales.com/api/market/market-tide"
headers = {
    "Authorization": "Bearer YOUR_API_KEY"
}
params = {
    "interval_5m": True
}

response = requests.get(url, headers=headers, params=params)
data = response.json()
print(data)
```

### JavaScript (Fetch)

```javascript
const url = "https://api.unusualwhales.com/api/market/market-tide?interval_5m=true";
const options = {
  method: 'GET',
  headers: {
    'Authorization': 'Bearer YOUR_API_KEY'
  }
};

fetch(url, options)
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));
```

## Response Schema

### Success Response (200 OK)

```json
{
  "data": [
    {
      "timestamp": "string (ISO 8601)",
      "date": "string (YYYY-MM-DD)",
      "net_call_premium": "string (decimal)",
      "net_put_premium": "string (decimal)",
      "net_volume": "integer"
    }
  ]
}
```

### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| data | array | Array of market tide data points |
| timestamp | string | ISO 8601 formatted timestamp with timezone |
| date | string | Trading date in YYYY-MM-DD format |
| net_call_premium | string | Net call premium for the interval (cumulative or interval delta) |
| net_put_premium | string | Net put premium for the interval (cumulative or interval delta) |
| net_volume | integer | Net trading volume across calls and puts |

## Example Response

```json
{
  "data": [
    {
      "timestamp": "2025-10-22T09:30:00-04:00",
      "date": "2025-10-22",
      "net_call_premium": "-5498810.0000",
      "net_put_premium": "-270018.0000",
      "net_volume": -20396
    },
    {
      "timestamp": "2025-10-22T09:35:00-04:00",
      "date": "2025-10-22",
      "net_call_premium": "-16868723.0000",
      "net_put_premium": "-778333.0000",
      "net_volume": -11280
    },
    {
      "timestamp": "2025-10-22T09:40:00-04:00",
      "date": "2025-10-22",
      "net_call_premium": "-11149962.0000",
      "net_put_premium": "77188.0000",
      "net_volume": 24123
    },
    {
      "timestamp": "2025-10-22T09:45:00-04:00",
      "date": "2025-10-22",
      "net_call_premium": "-15734922.0000",
      "net_put_premium": "-13712074.0000",
      "net_volume": 83671
    }
  ]
}
```

## Error Responses

| Status Code | Description | Response Body |
|-------------|-------------|---------------|
| 400 | Bad Request | `{"error": "Invalid date format"}` |
| 401 | Unauthorized | `{"error": "Invalid API key"}` |
| 422 | Unprocessable Entity | `{"error": "Invalid parameters"}` |
| 500 | Internal Server Error | `{"error": "Server error"}` |

## Rate Limiting

Standard API rate limits apply. This endpoint provides real-time data that updates frequently.

## Notes

- Market Tide sentiment interpretation:
  - Increasingly bullish: Call premium increasing faster OR Put premium decreasing faster
  - Increasingly bearish: Call premium decreasing faster OR Put premium increasing faster
- Negative net premiums indicate more bid-side activity (bearish pressure)
- Positive net premiums indicate more ask-side activity (bullish pressure)
- The OTM-only filter removes in-the-money contracts, reducing noise from deep ITM trades
- 5-minute candles aggregate data into longer periods for trend analysis
- Data is available back to September 28, 2022
- Premium values can be very large and are formatted as strings to preserve precision

## Related Endpoints

- [/api/market/sector-tide](./sector-tide.md) - Market tide filtered by sector
- [/api/market/etf-tide](./etf-tide.md) - Market tide for specific ETF holdings
- [/api/market/top-net-impact](./top-net-impact.md) - Top tickers by net premium
- [/api/net-flow/expiry](../net-flow/expiry.md) - Net flow by expiration type

## Validation Results

**Tested**: Yes

**Test Date**: 2025-10-22

**Status**: Working

**Notes**: Endpoint returns real-time market tide data with minute-by-minute sentiment indicators. Data is structured for time-series analysis and charting.

**Response Time**: < 1 second

**Data Points**: Multiple entries per trading day (typically one per minute during market hours)

**Test Command**:
```bash
curl -s "https://api.unusualwhales.com/api/market/market-tide" \
  -H "Authorization: Bearer YOUR_API_KEY"
```
