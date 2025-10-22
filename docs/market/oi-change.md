# OI Change

## Endpoint Details

**Path**: `GET /api/market/oi-change`

**Operation ID**: `PublicApi.MarketController.oi_change`

**Summary**: Returns contracts with highest open interest changes

**Tags**: market

## Description

Returns the non-Index/non-ETF contracts and OI change data with the highest OI change (default: descending order). Date must be the current or a past date. If no date is given, returns data for the current/last market day.

This endpoint is useful for identifying which option contracts are attracting the most new interest, which can indicate significant positioning changes or hedging activity.

## Authentication

- **Required**: Yes
- **Type**: API Key
- **Header**: `Authorization: Bearer YOUR_API_KEY`

## Request Parameters

### Query Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| date | string | No | current/last market day | Market date in YYYY-MM-DD format |
| limit | integer | No | 100 | Maximum number of results (max: 200, min: 1) |
| order | string | No | descending | Sort order: "ascending" or "descending" |

## Example Requests

### cURL

```bash
curl -X GET "https://api.unusualwhales.com/api/market/oi-change?limit=5" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

### Python

```python
import requests

url = "https://api.unusualwhales.com/api/market/oi-change"
headers = {
    "Authorization": "Bearer YOUR_API_KEY"
}
params = {
    "limit": 5,
    "order": "descending"
}

response = requests.get(url, headers=headers, params=params)
data = response.json()
print(data)
```

### JavaScript (Fetch)

```javascript
const url = "https://api.unusualwhales.com/api/market/oi-change?limit=5";
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
      "option_symbol": "string",
      "underlying_symbol": "string",
      "volume": "integer",
      "trades": "integer",
      "oi_change": "string (decimal)",
      "oi_diff_plain": "integer",
      "curr_oi": "integer",
      "last_oi": "integer",
      "curr_date": "string (YYYY-MM-DD)",
      "last_date": "string (YYYY-MM-DD)",
      "avg_price": "string (decimal)",
      "last_fill": "string (decimal)",
      "last_ask": "string (decimal)",
      "last_bid": "string (decimal)",
      "percentage_of_total": "string (decimal)"
    }
  ]
}
```

### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| option_symbol | string | Option contract symbol (e.g., AAPL241220C00230000) |
| underlying_symbol | string | Underlying stock ticker |
| volume | integer | Total trading volume for the contract |
| trades | integer | Total number of trades executed |
| oi_change | string | Percentage change in open interest |
| oi_diff_plain | integer | Absolute change in open interest |
| curr_oi | integer | Current open interest |
| last_oi | integer | Previous open interest (last date) |
| curr_date | string | Current date |
| last_date | string | Last date open interest was recorded |
| avg_price | string | Average price paid for the contracts |
| last_fill | string | Price of the last fill |
| last_ask | string | Current ask price |
| last_bid | string | Current bid price |
| percentage_of_total | string | Contract OI as percentage of total market OI |

## Example Response

```json
{
  "data": [
    {
      "volume": 57909,
      "option_symbol": "LAZR251128P00001500",
      "underlying_symbol": "LAZR",
      "trades": 380,
      "curr_date": "2025-10-22",
      "avg_price": "0.3406534390163877808285413322",
      "curr_oi": 55814,
      "last_fill": "0.45",
      "prev_ask_volume": 32734,
      "prev_bid_volume": 20997,
      "prev_multi_leg_volume": 0,
      "prev_neutral_volume": 0,
      "prev_stock_multi_leg_volume": 0,
      "prev_total_premium": "1972690.00",
      "days_of_oi_increases": 2,
      "days_of_vol_greater_than_oi": 1,
      "oi_change": "319.7701149425287356",
      "last_ask": "0.49",
      "last_bid": "0.40",
      "last_date": "2025-10-21",
      "last_oi": 174,
      "oi_diff_plain": 55640,
      "percentage_of_total": "0.50508935813904806761",
      "rnk": 2
    }
  ]
}
```

## Error Responses

| Status Code | Description | Response Body |
|-------------|-------------|---------------|
| 400 | Bad Request | `{"error": "Invalid date format"}` |
| 401 | Unauthorized | `{"error": "Invalid API key"}` |
| 500 | Internal Server Error | `{"error": "Server error"}` |

## Rate Limiting

Standard API rate limits apply.

## Notes

- This endpoint excludes Index and ETF contracts, focusing on individual equities
- OI change is calculated as a percentage to show relative growth
- Contracts with OI_change > 100% indicate OI has more than doubled
- Volume can exceed OI if there was significant intraday trading
- Results are sorted by OI change in descending order by default
- Previous OI data (prev_) fields show volume breakdown by trade type
- The timestamp fields show when the most recent data was recorded

## Related Endpoints

- [/api/market/top-net-impact](./top-net-impact.md) - Top tickers by net premium impact
- [/api/option-contract/{id}/flow](../option-contract/flow.md) - Flow data for specific option contract
- [/api/screener/option-contracts](../screener/option-contracts.md) - Contract screener with multiple filters

## Validation Results

**Tested**: Yes

**Test Date**: 2025-10-22

**Status**: Working

**Notes**: Endpoint returns detailed OI change data for option contracts with highest changes. Useful for identifying significant positioning activity.

**Response Time**: < 1 second

**Test Command**:
```bash
curl -s "https://api.unusualwhales.com/api/market/oi-change?limit=5" \
  -H "Authorization: Bearer 5d1ec006-49f0-4a2a-90ae-5176c72425e3"
```
