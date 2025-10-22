# Analyst Ratings

## Endpoint Details

**Path**: `GET /api/screener/analysts`

**Operation ID**: `PublicApi.ScreenerController.analyst_ratings`

**Summary**: Analyst Rating

**Tags**: screener

## Description

Returns the latest analyst ratings and recommendations for a given ticker. This endpoint provides access to sell-side analyst coverage including recommendations, price targets, and analyst actions (upgrades, downgrades, maintained, initiated).

## Authentication

- **Required**: Yes
- **Type**: API Key
- **Header**: `Authorization: Bearer YOUR_API_KEY`

## Request Parameters

### Path Parameters

None

### Query Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| ticker | string | Yes | - | Stock ticker symbol (e.g., AAPL, TSLA) |
| limit | integer | No | 50 | Maximum number of ratings to return |
| offset | integer | No | 0 | Pagination offset |
| sort_by | string | No | timestamp | Field to sort by (timestamp, firm, analyst_name) |

### Request Body

None

## Example Requests

### cURL

```bash
# Get latest analyst ratings for AAPL
curl -X GET "https://api.unusualwhales.com/api/screener/analysts?ticker=AAPL" \
  -H "Authorization: Bearer YOUR_API_KEY"

# Get latest 10 analyst ratings with custom sorting
curl -X GET "https://api.unusualwhales.com/api/screener/analysts?ticker=AAPL&limit=10&sort_by=firm" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

### Python

```python
import requests

url = "https://api.unusualwhales.com/api/screener/analysts"
headers = {
    "Authorization": "Bearer YOUR_API_KEY"
}
params = {
    "ticker": "AAPL",
    "limit": 25
}

response = requests.get(url, headers=headers, params=params)
data = response.json()
print(data)
```

### JavaScript (Fetch)

```javascript
const url = "https://api.unusualwhales.com/api/screener/analysts?ticker=AAPL&limit=25";
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
      "timestamp": "2025-10-21T13:27:55.000000Z",
      "ticker": "AAPL",
      "action": "maintained",
      "target": "290.0000",
      "sector": "Technology",
      "analyst_name": "Aaron Rakers",
      "recommendation": "buy",
      "firm": "Wells Fargo"
    }
  ]
}
```

### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| data | array | Array of analyst rating records |
| timestamp | string | ISO 8601 timestamp when the rating was published |
| ticker | string | Stock ticker symbol |
| action | string | Analyst action (maintained, upgraded, downgraded, initiated, reiterated) |
| target | string | Price target from the analyst |
| sector | string | Stock sector classification |
| analyst_name | string | Name of the analyst making the recommendation |
| recommendation | string | Rating recommendation (buy, sell, hold) |
| firm | string | Name of the analyst's firm |

## Example Response

```json
{
  "data": [
    {
      "timestamp": "2025-10-21T13:27:55.000000Z",
      "ticker": "AAPL",
      "action": "maintained",
      "target": "290.0000",
      "sector": "Technology",
      "analyst_name": "Aaron Rakers",
      "recommendation": "buy",
      "firm": "Wells Fargo"
    },
    {
      "timestamp": "2025-10-20T13:15:04.000000Z",
      "ticker": "AAPL",
      "action": "upgraded",
      "target": "315.0000",
      "sector": "Technology",
      "analyst_name": "Ananda Baruah",
      "recommendation": "buy",
      "firm": "Loop Capital"
    },
    {
      "timestamp": "2025-10-03T12:53:20.000000Z",
      "ticker": "AAPL",
      "action": "downgraded",
      "target": "205.1600",
      "sector": "Technology",
      "analyst_name": "Edison Lee",
      "recommendation": "sell",
      "firm": "Jefferies"
    }
  ]
}
```

## Error Responses

| Status Code | Description | Response Body |
|-------------|-------------|---------------|
| 400 | Bad Request | `{"error": "Ticker parameter is required"}` |
| 401 | Unauthorized | `{"error": "Invalid API key"}` |
| 404 | Not Found | `{"error": "Ticker not found"}` |
| 422 | Unprocessable Entity | `{"error": "Invalid ticker symbol"}` |
| 500 | Internal Server Error | `{"error": "Server error"}` |

## Rate Limiting

The API enforces rate limits on requests. Standard tier allows reasonable request frequency. Check response headers for rate limit information.

## Notes

- Ticker parameter is required
- Data is sorted by timestamp descending (most recent first) by default
- Analyst names may be null for some records
- Price targets are returned as string values with decimal precision
- Action values: "maintained", "upgraded", "downgraded", "initiated", "reiterated"
- Recommendations: "buy", "sell", "hold"
- Data includes both published analyst research and action-based updates
- Historical data typically spans multiple years
- Useful for consensus rating analysis and tracking analyst sentiment changes

## Related Endpoints

- `/api/screener/stocks` - Stock screener with multiple filter options
- `/api/screener/option-contracts` - Option contract screener

## Validation Results

**Tested**: Yes

**Test Date**: 2025-10-22

**Status**: Working

**Notes**: Endpoint successfully returns analyst ratings for AAPL. Response includes comprehensive analyst data with timestamps, actions, recommendations, and price targets. Data spans recent and historical ratings. Over 80 records returned in single query, demonstrating good historical data availability.
