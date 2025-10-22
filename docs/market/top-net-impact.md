# Top Net Impact

## Endpoint Details

**Path**: `GET /api/market/top-net-impact`

**Operation ID**: `PublicApi.MarketController.top_net_impact`

**Summary**: Returns top tickers by net premium impact

**Tags**: market

## Description

Returns the top tickers by net premium (half bullish, half bearish). This shows which individual stocks have the most significant options activity in terms of net premium flow. Defaults to last market day if no date is specified.

## Authentication

- **Required**: Yes
- **Type**: API Key
- **Header**: `Authorization: Bearer YOUR_API_KEY`

## Request Parameters

### Query Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| date | string | No | last market day | Market date in YYYY-MM-DD format |
| issue_types[] | string | No | all | Filter by issue type (stock, etf, index) |
| limit | integer | No | 20 | Maximum number of results (max: 100, min: 1) |

## Example Requests

### cURL

```bash
curl -X GET "https://api.unusualwhales.com/api/market/top-net-impact?limit=5" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

### Python

```python
import requests

url = "https://api.unusualwhales.com/api/market/top-net-impact"
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
const url = "https://api.unusualwhales.com/api/market/top-net-impact?limit=5";
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
      "ticker": "string",
      "net_premium": "float"
    }
  ]
}
```

### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| data | array | Array of tickers sorted by net premium |
| ticker | string | Stock ticker symbol |
| net_premium | float | Net premium (positive = bullish, negative = bearish) |

## Example Response

```json
{
  "data": [
    {
      "ticker": "CRWV",
      "net_premium": 16550771.0
    },
    {
      "ticker": "GDX",
      "net_premium": 13537522.0
    },
    {
      "ticker": "UUUU",
      "net_premium": 13387886.0
    },
    {
      "ticker": "TSLA",
      "net_premium": -47051475.0
    },
    {
      "ticker": "NFLX",
      "net_premium": -75002255.0
    }
  ]
}
```

## Error Responses

| Status Code | Description | Response Body |
|-------------|-------------|---------------|
| 400 | Bad Request | `{"error": "Invalid parameters"}` |
| 401 | Unauthorized | `{"error": "Invalid API key"}` |
| 422 | Unprocessable Entity | `{"error": "Invalid date or filters"}` |
| 500 | Internal Server Error | `{"error": "Server error"}` |

## Rate Limiting

Standard API rate limits apply.

## Notes

- Positive net_premium indicates more bullish options activity (calls at ask, puts at bid)
- Negative net_premium indicates more bearish options activity (calls at bid, puts at ask)
- The endpoint returns approximately half bullish and half bearish tickers
- Results are sorted by absolute net premium value
- Larger premium values indicate more significant options activity
- The limit parameter controls how many tickers are returned
- Issue type filtering allows focusing on specific security types (stocks, ETFs, indices)

## Related Endpoints

- [/api/market/market-tide](./market-tide.md) - Market-wide options sentiment
- [/api/market/sector-etfs](./sector-etfs.md) - Sector ETF statistics
- [/api/option-trades/flow-alerts](../option-trades/flow-alerts.md) - Individual flow alerts

## Validation Results

**Tested**: Yes

**Test Date**: 2025-10-22

**Status**: Working

**Notes**: Endpoint returns top tickers by net premium impact with both bullish and bearish positions. Useful for identifying market-wide options sentiment by individual security.

**Response Time**: < 1 second

**Sample Data**:
- Bullish tickers (positive net premium): CRWV, GDX, UUUU
- Bearish tickers (negative net premium): TSLA, NFLX

**Test Command**:
```bash
curl -s "https://api.unusualwhales.com/api/market/top-net-impact?limit=5" \
  -H "Authorization: Bearer YOUR_API_KEY"
```
