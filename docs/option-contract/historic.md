# Option Contract Historic Data

## Endpoint Details

**Path**: `GET /api/option-contract/{id}/historic`

**Operation ID**: `PublicApi.OptionContractController.history`

**Summary**: Returns historic daily data for an option contract

**Tags**: option-contract

## Description

Returns for every trading day historic data for the given option contract. This provides a daily OHLC-style view of the option contract's price history and key metrics.

## Authentication

- **Required**: Yes
- **Type**: API Key
- **Header**: `Authorization: Bearer YOUR_API_KEY`

## Request Parameters

### Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| id | string | Yes | Option contract symbol (e.g., AAPL241220C00230000) |

### Query Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| limit | integer | No | null | Maximum number of days to return (min: 1) |

## Example Requests

### cURL

```bash
curl -X GET "https://api.unusualwhales.com/api/option-contract/AAPL241220C00230000/historic?limit=5" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

### Python

```python
import requests

url = "https://api.unusualwhales.com/api/option-contract/AAPL241220C00230000/historic"
headers = {
    "Authorization": "Bearer YOUR_API_KEY"
}
params = {
    "limit": 5
}

response = requests.get(url, headers=headers, params=params)
data = response.json()
print(data)
```

### JavaScript (Fetch)

```javascript
const url = "https://api.unusualwhales.com/api/option-contract/AAPL241220C00230000/historic?limit=5";
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
      "date": "string (YYYY-MM-DD)",
      "open": "string (decimal)",
      "high": "string (decimal)",
      "low": "string (decimal)",
      "close": "string (decimal)",
      "volume": "integer",
      "open_interest": "integer",
      "iv": "string (decimal)"
    }
  ]
}
```

### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| date | string | Trading date in YYYY-MM-DD format |
| open | string | Opening price for the day |
| high | string | High price for the day |
| low | string | Low price for the day |
| close | string | Closing price for the day |
| volume | integer | Daily trading volume |
| open_interest | integer | Open interest at end of day |
| iv | string | Implied volatility |

## Example Response

```json
{
  "data": [
    {
      "date": "2025-10-22",
      "open": "2.50",
      "high": "2.65",
      "low": "2.45",
      "close": "2.55",
      "volume": 150000,
      "open_interest": 500000,
      "iv": "0.35"
    },
    {
      "date": "2025-10-21",
      "open": "2.45",
      "high": "2.60",
      "low": "2.40",
      "close": "2.50",
      "volume": 120000,
      "open_interest": 490000,
      "iv": "0.34"
    }
  ]
}
```

## Error Responses

| Status Code | Description | Response Body |
|-------------|-------------|---------------|
| 400 | Bad Request | `{"error": "Invalid option contract symbol"}` |
| 401 | Unauthorized | `{"error": "Invalid API key"}` |
| 404 | Not Found | `{"error": "Option contract not found"}` |
| 422 | Unprocessable Entity | `{"error": "Invalid parameters"}` |
| 500 | Internal Server Error | `{"error": "Server error"}` |

## Rate Limiting

Standard API rate limits apply.

## Notes

- Data is returned in reverse chronological order (most recent first)
- Open Interest (OI) is a key indicator of contract liquidity and interest
- Implied Volatility (IV) shows market's expectation of future volatility
- Volume indicates trading interest and liquidity
- OHLC data can be used for technical analysis and charting
- Limit parameter controls how many days of history are returned
- Without limit, returns all available historical data for the contract

## Related Endpoints

- [/api/option-contract/{id}/flow](./flow.md) - Recent option trades
- [/api/option-contract/{id}/intraday](./intraday.md) - Intraday minute-level data
- [/api/option-contract/{id}/volume-profile](./volume-profile.md) - Volume profile by price

## Validation Results

**Tested**: Yes

**Test Date**: 2025-10-22

**Status**: Working

**Notes**: Endpoint returns daily OHLC and metrics data for option contracts. Useful for technical analysis and tracking contract metrics over time.

**Response Time**: < 1 second

**Test Command**:
```bash
curl -s "https://api.unusualwhales.com/api/option-contract/AAPL241220C00230000/historic?limit=5" \
  -H "Authorization: Bearer 5d1ec006-49f0-4a2a-90ae-5176c72425e3"
```
