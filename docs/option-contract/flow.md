# Option Contract Flow Data

## Endpoint Details

**Path**: `GET /api/option-contract/{id}/flow`

**Operation ID**: `PublicApi.OptionContractController.flow`

**Summary**: Returns the latest option trades (flow) for a given option contract

**Tags**: option-contract

## Description

Returns the last 50 option trades for the given option chain. Optionally a min premium and a side can be supplied in the query for further filtering. If no date is specified, data for the last trading day is returned.

This endpoint provides detailed flow information for a specific option contract, useful for analyzing recent trading activity and identifying institutional order flow.

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
| side | string | No | null | Trade side: "ask" or "bid" |
| min_premium | integer | No | null | Minimum trade premium in dollars |
| limit | integer | No | 50 | Maximum number of trades to return (min: 1) |
| date | string | No | last market day | Market date in YYYY-MM-DD format |

## Example Requests

### cURL

```bash
curl -X GET "https://api.unusualwhales.com/api/option-contract/AAPL241220C00230000/flow?limit=10" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

Filter for ask-side trades with minimum premium:
```bash
curl -X GET "https://api.unusualwhales.com/api/option-contract/AAPL241220C00230000/flow?side=ask&min_premium=10000&limit=10" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

### Python

```python
import requests

url = "https://api.unusualwhales.com/api/option-contract/AAPL241220C00230000/flow"
headers = {
    "Authorization": "Bearer YOUR_API_KEY"
}
params = {
    "limit": 10,
    "side": "ask"
}

response = requests.get(url, headers=headers, params=params)
data = response.json()
print(data)
```

### JavaScript (Fetch)

```javascript
const url = "https://api.unusualwhales.com/api/option-contract/AAPL241220C00230000/flow?limit=10";
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

Response contains an array of option trades with detailed information about each transaction.

### Response Fields

The response structure contains individual trade records with details about timing, size, premium, and trade characteristics.

## Example Response

```json
{
  "data": [
    {
      "symbol": "AAPL241220C00230000",
      "underlying": "AAPL",
      "timestamp": "2025-10-22T14:30:15Z",
      "quantity": 100,
      "price": "5.25",
      "premium": "525000",
      "side": "ask",
      "trade_type": "regular"
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

- Returns the most recent trades first (newest to oldest)
- Ask-side trades indicate bullish pressure (buyers willing to pay ask)
- Bid-side trades indicate bearish pressure (sellers willing to accept bid)
- Premium = quantity × price × 100 (options contracts are for 100 shares)
- Large premium trades often indicate institutional or block activity
- Limited to the most recent 50 trades without pagination
- The limit parameter caps results but cannot exceed actual available trades

## Related Endpoints

- [/api/option-contract/{id}/intraday](./intraday.md) - Minute-by-minute option data
- [/api/option-contract/{id}/historic](./historic.md) - Historical daily option data
- [/api/option-contract/{id}/volume-profile](./volume-profile.md) - Volume profile by price level

## Validation Results

**Tested**: Yes

**Test Date**: 2025-10-22

**Status**: Working

**Notes**: Endpoint successfully returns recent option trade flow data. Useful for analyzing institutional order flow and recent trading activity.

**Response Time**: < 1 second

**Test Command**:
```bash
curl -s "https://api.unusualwhales.com/api/option-contract/AAPL241220C00230000/flow?limit=10" \
  -H "Authorization: Bearer YOUR_API_KEY"
```
