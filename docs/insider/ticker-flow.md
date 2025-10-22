# Insider Ticker Flow

## Endpoint Details

**Path**: `GET /api/insider/{ticker}/ticker-flow`

**Operation ID**: `PublicApi.InsiderController.ticker_flow`

**Summary**: Ticker Flow

**Tags**: insider

## Description

Returns an aggregated view of the insider flow for the given ticker. This can be used to quickly examine the buy and sell insider flow for a given trading date. The endpoint shows net insider sentiment through their trading activity.

## Authentication

- **Required**: Yes
- **Type**: API Key
- **Header**: `Authorization: Bearer YOUR_API_KEY`

## Request Parameters

### Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ticker | string | Yes | The stock ticker symbol (e.g., AAPL, MSFT) |

### Query Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| date | string | No | current date | The date to retrieve data for (YYYY-MM-DD format) |

### Request Body

Not applicable for this endpoint.

## Example Requests

### cURL

```bash
curl -X GET "https://api.unusualwhales.com/api/insider/AAPL/ticker-flow" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

### Python

```python
import requests

url = "https://api.unusualwhales.com/api/insider/AAPL/ticker-flow"
headers = {
    "Authorization": "Bearer YOUR_API_KEY"
}

response = requests.get(url, headers=headers)
data = response.json()
print(data)
```

### JavaScript (Fetch)

```javascript
const url = "https://api.unusualwhales.com/api/insider/AAPL/ticker-flow";
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

The response contains aggregated insider flow data for the specific ticker.

```json
{
  "data": [
    {
      "date": "string (YYYY-MM-DD)",
      "ticker": "string",
      "buys": "integer",
      "sells": "integer",
      "buy_amount": "string (decimal)",
      "sell_amount": "string (decimal)",
      "net_flow": "string (decimal)",
      "insider_count": "integer"
    }
  ]
}
```

### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| date | string | The date of the data |
| ticker | string | Stock ticker symbol |
| buys | integer | Number of insider buy transactions |
| sells | integer | Number of insider sell transactions |
| buy_amount | string | Total value of insider buys |
| sell_amount | string | Total value of insider sells |
| net_flow | string | Net flow (buys - sells) |
| insider_count | integer | Number of unique insiders involved |

## Example Response

```json
{
  "data": [
    {
      "date": "2025-10-20",
      "ticker": "AAPL",
      "buys": 2,
      "sells": 5,
      "buy_amount": "245678.90",
      "sell_amount": "987654.32",
      "net_flow": "-741975.42",
      "insider_count": 7
    },
    {
      "date": "2025-10-19",
      "ticker": "AAPL",
      "buys": 1,
      "sells": 3,
      "buy_amount": "123456.78",
      "sell_amount": "456789.01",
      "net_flow": "-333332.23",
      "insider_count": 4
    }
  ]
}
```

## Error Responses

| Status Code | Description | Response Body |
|-------------|-------------|---------------|
| 400 | Bad Request | `{"error": "Invalid ticker symbol"}` |
| 401 | Unauthorized | `{"error": "Invalid or missing API key"}` |
| 404 | Not Found | `{"error": "No insider flow data for ticker"}` |
| 429 | Too Many Requests | `{"error": "Rate limit exceeded"}` |
| 500 | Internal Server Error | `{"error": "Server error"}` |

## Rate Limiting

Standard API rate limits apply. Monitor the response headers for rate limit information.

## Notes

- Returns historical insider flow data, typically multiple trading days
- Net flow is positive for insider buying, negative for selling
- Positive net flow can indicate insider confidence in the company
- Negative net flow may indicate profit-taking or portfolio rebalancing
- Data is aggregated from all insider filings (Form 3, Form 4, Form 5)
- If no date is provided, returns current/most recent trading day data
- High insider selling doesn't always indicate negative sentiment

## Related Endpoints

- [Insiders](/docs/insider/insiders.md) - Get list of insiders for a ticker
- [Transactions](/docs/insider/transactions.md) - Get detailed individual transactions
- [Sector Flow](/docs/insider/sector-flow.md) - Get aggregated insider flow for a sector

## Validation Results

**Tested**: Yes

**Test Date**: 2025-10-22

**Status**: Working

**Notes**: Endpoint returns historical insider flow data for the specified ticker. Successfully tested with AAPL returning multiple days of aggregated insider trading data.
