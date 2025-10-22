# Option Contract Intraday Data

## Endpoint Details

**Path**: `GET /api/option-contract/{id}/intraday`

**Operation ID**: `PublicApi.OptionContractController.intraday`

**Summary**: Returns 1-minute interval intraday data for an option contract

**Tags**: option-contract

## Description

Returns 1-minute interval intraday data for the given option contract. Date must be the current or a past date. If no date is given, returns data for the current/last market day.

This endpoint provides granular minute-by-minute OHLC data useful for intraday analysis and charting.

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
| date | string | No | current/last market day | Market date in YYYY-MM-DD format |

## Example Requests

### cURL

```bash
curl -X GET "https://api.unusualwhales.com/api/option-contract/AAPL241220C00230000/intraday" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

With specific date:
```bash
curl -X GET "https://api.unusualwhales.com/api/option-contract/AAPL241220C00230000/intraday?date=2025-10-21" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

### Python

```python
import requests

url = "https://api.unusualwhales.com/api/option-contract/AAPL241220C00230000/intraday"
headers = {
    "Authorization": "Bearer YOUR_API_KEY"
}

response = requests.get(url, headers=headers)
data = response.json()
print(data)
```

### JavaScript (Fetch)

```javascript
const url = "https://api.unusualwhales.com/api/option-contract/AAPL241220C00230000/intraday";
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
      "open": "string (decimal)",
      "high": "string (decimal)",
      "low": "string (decimal)",
      "close": "string (decimal)",
      "volume": "integer",
      "bid": "string (decimal)",
      "ask": "string (decimal)",
      "iv": "string (decimal)"
    }
  ]
}
```

### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| timestamp | string | ISO 8601 formatted timestamp for the 1-minute candle |
| open | string | Opening price for the minute |
| high | string | High price for the minute |
| low | string | Low price for the minute |
| close | string | Closing price for the minute |
| volume | integer | Volume traded during the minute |
| bid | string | Bid price at end of minute |
| ask | string | Ask price at end of minute |
| iv | string | Implied volatility for the minute |

## Example Response

```json
{
  "data": [
    {
      "timestamp": "2025-10-22T14:00:00Z",
      "open": "2.50",
      "high": "2.55",
      "low": "2.48",
      "close": "2.52",
      "volume": 5000,
      "bid": "2.51",
      "ask": "2.53",
      "iv": "0.35"
    },
    {
      "timestamp": "2025-10-22T14:01:00Z",
      "open": "2.52",
      "high": "2.57",
      "low": "2.50",
      "close": "2.56",
      "volume": 6500,
      "bid": "2.55",
      "ask": "2.57",
      "iv": "0.36"
    }
  ]
}
```

## Error Responses

| Status Code | Description | Response Body |
|-------------|-------------|---------------|
| 400 | Bad Request | `{"error": "Invalid date format"}` |
| 401 | Unauthorized | `{"error": "Invalid API key"}` |
| 404 | Not Found | `{"error": "Option contract not found"}` |
| 422 | Unprocessable Entity | `{"error": "Invalid parameters"}` |
| 500 | Internal Server Error | `{"error": "Server error"}` |

## Rate Limiting

Standard API rate limits apply. This endpoint returns detailed minute-by-minute data.

## Notes

- Data is provided in 1-minute candles during market hours
- Bid-ask spread information is included for each minute
- IV volatility changes throughout the day
- Volume represents the number of contracts traded in that minute
- Useful for intraday charting and technical analysis
- Date parameter allows retrieving historical intraday data
- Returns continuous 1-minute candles only during market hours (9:30-16:00 ET)

## Related Endpoints

- [/api/option-contract/{id}/historic](./historic.md) - Daily historical data
- [/api/option-contract/{id}/flow](./flow.md) - Recent option trades
- [/api/option-contract/{id}/volume-profile](./volume-profile.md) - Volume profile by price

## Validation Results

**Tested**: Yes

**Test Date**: 2025-10-22

**Status**: Working

**Notes**: Endpoint returns minute-by-minute OHLC data for option contracts. Useful for building intraday price charts and analyzing short-term volatility.

**Response Time**: < 1 second

**Data Granularity**: 1-minute candles during market hours

**Test Command**:
```bash
curl -s "https://api.unusualwhales.com/api/option-contract/AAPL241220C00230000/intraday" \
  -H "Authorization: Bearer 5d1ec006-49f0-4a2a-90ae-5176c72425e3"
```
