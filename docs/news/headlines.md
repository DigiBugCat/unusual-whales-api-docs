# News Headlines

## Endpoint Details

**Path**: `GET /api/news/headlines`

**Operation ID**: `PublicApi.NewsController.headlines`

**Summary**: Returns the latest news headlines for financial markets

**Tags**: news

## Description

Returns the latest news headlines for financial markets. This endpoint provides access to news headlines that may impact the markets, including company-specific news, sector news, and market-wide events. Headlines can be filtered by source, content, and significance.

The data includes the headline text, source, related tickers, sentiment, and whether it's considered a major news item.

## Authentication

- **Required**: Yes
- **Type**: API Key
- **Header**: `Authorization: Bearer YOUR_API_KEY`

## Request Parameters

### Query Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| sources | string | No | null | Comma-separated list of news sources |
| search_term | string | No | null | Search term for headline content |
| major_only | boolean | No | false | Return only major news items |
| limit | integer | No | 50 | Maximum number of results (max: 100, min: 1) |
| page | integer | No | 1 | Page number for pagination |

## Example Requests

### cURL

```bash
curl -X GET "https://api.unusualwhales.com/api/news/headlines?limit=3" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

Get major news only:
```bash
curl -X GET "https://api.unusualwhales.com/api/news/headlines?major_only=true&limit=10" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

Search for specific news:
```bash
curl -X GET "https://api.unusualwhales.com/api/news/headlines?search_term=Tesla&limit=5" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

### Python

```python
import requests

url = "https://api.unusualwhales.com/api/news/headlines"
headers = {
    "Authorization": "Bearer YOUR_API_KEY"
}
params = {
    "limit": 10,
    "major_only": True
}

response = requests.get(url, headers=headers, params=params)
data = response.json()
print(data)
```

### JavaScript (Fetch)

```javascript
const url = "https://api.unusualwhales.com/api/news/headlines?limit=10&major_only=true";
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
      "headline": "string",
      "source": "string",
      "tickers": ["string"],
      "is_major": "boolean",
      "sentiment": "string",
      "created_at": "string (ISO 8601)",
      "tags": ["string"],
      "meta": {}
    }
  ]
}
```

### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| data | array | Array of news headline objects |
| headline | string | The news headline text |
| source | string | News source (e.g., Investors.com, Reuters, Bloomberg) |
| tickers | array | Array of related ticker symbols |
| is_major | boolean | Whether this is considered major market-moving news |
| sentiment | string | Sentiment classification (positive, negative, neutral) |
| created_at | string | ISO 8601 timestamp when the news was published |
| tags | array | Tags associated with the news |
| meta | object | Additional metadata |

## Example Response

```json
{
  "data": [
    {
      "meta": {},
      "source": "Investors.com",
      "created_at": "2025-10-22T21:24:29Z",
      "tags": [],
      "headline": "Tesla's Q3 revenue exceeds expectations, however earnings miss causing TSLA stock to fall. Investors await Elon Musk's comments on robotaxis.",
      "tickers": [
        "TSLA"
      ],
      "is_major": true,
      "sentiment": "neutral"
    },
    {
      "meta": {},
      "source": "Investors.com",
      "created_at": "2025-10-22T21:24:26Z",
      "tags": [],
      "headline": "Arcturus Therapeutics shares plummet 50% due to disappointing results for cystic fibrosis drug.",
      "tickers": [],
      "is_major": false,
      "sentiment": "neutral"
    },
    {
      "meta": {},
      "source": "Investors.com",
      "created_at": "2025-10-22T21:24:24Z",
      "tags": [],
      "headline": "Southwest beats Q3 estimates, American Airlines reports soon. Delta trades near buy zone.",
      "tickers": [],
      "is_major": false,
      "sentiment": "neutral"
    }
  ]
}
```

## Error Responses

| Status Code | Description | Response Body |
|-------------|-------------|---------------|
| 400 | Bad Request | `{"error": "Invalid parameters"}` |
| 401 | Unauthorized | `{"error": "Invalid API key"}` |
| 422 | Unprocessable Entity | `{"error": "Unprocessable Entity"}` |
| 500 | Internal Server Error | `{"error": "Server error"}` |

## Rate Limiting

Standard API rate limits apply. This endpoint provides frequently updated news data.

## Notes

- Headlines are updated continuously throughout the trading day
- The `is_major` flag indicates news that may have significant market impact
- Sentiment is automatically classified; some headlines may show "neutral" due to mixed signals
- Tickers array may be empty for broader market news
- News sources include major financial news outlets and press releases
- Pagination allows retrieving large numbers of headlines efficiently
- Search functionality is case-insensitive

## Related Endpoints

- [/api/alerts](../alerts/alerts.md) - User-configured alerts based on news and events
- [/api/market/economic-calendar](../market/economic-calendar.md) - Scheduled economic events
- [/api/market/fda-calendar](../market/fda-calendar.md) - FDA approval timeline events

## Validation Results

**Tested**: Yes

**Test Date**: 2025-10-22

**Status**: Working

**Notes**: Endpoint returns current financial news headlines with source, sentiment, and related ticker information. Useful for real-time market news monitoring.

**Response Time**: < 1 second

**Sample Headlines**:
- Major earnings surprises
- Corporate announcements
- Sector-specific news

**Test Command**:
```bash
curl -s "https://api.unusualwhales.com/api/news/headlines?limit=3" \
  -H "Authorization: Bearer 5d1ec006-49f0-4a2a-90ae-5176c72425e3"
```
