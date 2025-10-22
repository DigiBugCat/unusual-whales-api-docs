# Insider Sector Flow

## Endpoint Details

**Path**: `GET /api/insider/{sector}/sector-flow`

**Operation ID**: `PublicApi.InsiderController.sector_flow`

**Summary**: Sector Flow

**Tags**: insider

## Description

Returns an aggregated view of the insider flow for the given sector. This can be used to quickly examine the buy and sell insider flow for a given trading date. The endpoint provides insights into whether insiders are net buying or selling in a particular industry sector.

## Authentication

- **Required**: Yes
- **Type**: API Key
- **Header**: `Authorization: Bearer YOUR_API_KEY`

## Request Parameters

### Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| sector | string | Yes | The industry sector name (e.g., Technology, Healthcare, Finance) |

### Query Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| date | string | No | current date | The date to retrieve data for (YYYY-MM-DD format) |

### Request Body

Not applicable for this endpoint.

## Example Requests

### cURL

```bash
curl -X GET "https://api.unusualwhales.com/api/insider/Technology/sector-flow" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

### Python

```python
import requests

url = "https://api.unusualwhales.com/api/insider/Technology/sector-flow"
headers = {
    "Authorization": "Bearer YOUR_API_KEY"
}

response = requests.get(url, headers=headers)
data = response.json()
print(data)
```

### JavaScript (Fetch)

```javascript
const url = "https://api.unusualwhales.com/api/insider/Technology/sector-flow";
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

The response contains aggregated insider flow data for the sector.

```json
{
  "data": {
    "sector": "string",
    "date": "string (YYYY-MM-DD)",
    "buys": "integer",
    "sells": "integer",
    "buy_amount": "string (decimal)",
    "sell_amount": "string (decimal)",
    "net_flow": "string (decimal)"
  }
}
```

### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| sector | string | The sector name |
| date | string | The date of the data |
| buys | integer | Number of insider buy transactions |
| sells | integer | Number of insider sell transactions |
| buy_amount | string | Total value of insider buys |
| sell_amount | string | Total value of insider sells |
| net_flow | string | Net flow (buys - sells) |

## Example Response

```json
{
  "data": {
    "sector": "Technology",
    "date": "2025-10-22",
    "buys": 45,
    "sells": 82,
    "buy_amount": "5234567.89",
    "sell_amount": "8234567.89",
    "net_flow": "-3000000.00"
  }
}
```

## Error Responses

| Status Code | Description | Response Body |
|-------------|-------------|---------------|
| 400 | Bad Request | `{"error": "Invalid sector name"}` |
| 401 | Unauthorized | `{"error": "Invalid or missing API key"}` |
| 404 | Not Found | `{"error": "Sector not found"}` |
| 429 | Too Many Requests | `{"error": "Rate limit exceeded"}` |
| 500 | Internal Server Error | `{"error": "Server error"}` |

## Rate Limiting

Standard API rate limits apply. Monitor the response headers for rate limit information.

## Notes

- Sector names must match official sector classifications
- If no date is provided, returns current/most recent trading day data
- Net flow is positive for insider buying and negative for selling
- Insider activity can indicate confidence or portfolio rebalancing
- Sector-wide trends are less specific than individual ticker trends
- High sell flow may indicate profit-taking or diversification

## Related Endpoints

- [Ticker Flow](/docs/insider/ticker-flow.md) - Get insider flow for a specific ticker
- [Transactions](/docs/insider/transactions.md) - Get list of individual transactions
- [Insiders](/docs/insider/insiders.md) - Get list of insiders for a ticker

## Validation Results

**Tested**: Yes

**Test Date**: 2025-10-22

**Status**: Working

**Notes**: Endpoint successfully returns aggregated insider flow data by sector. Returns buy/sell counts and amounts for the specified sector.
