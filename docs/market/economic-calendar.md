# Economic Calendar

## Endpoint Details

**Path**: `GET /api/market/economic-calendar`

**Operation ID**: `PublicApi.MarketController.events`

**Summary**: Returns the economic calendar with upcoming economic events and releases.

**Tags**: market

## Description

Returns the economic calendar containing information about upcoming and past economic events, releases, and their impact on financial markets. The calendar includes events like employment reports, inflation data, GDP releases, consumer sentiment, housing starts, and other key economic indicators.

## Authentication

- **Required**: Yes
- **Type**: API Key
- **Header**: `Authorization: Bearer YOUR_API_KEY`

## Request Parameters

### Query Parameters

This endpoint does not accept any query parameters.

## Example Requests

### cURL

```bash
curl -X GET "https://api.unusualwhales.com/api/market/economic-calendar" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

### Python

```python
import requests

url = "https://api.unusualwhales.com/api/market/economic-calendar"
headers = {
    "Authorization": "Bearer YOUR_API_KEY"
}

response = requests.get(url, headers=headers)
data = response.json()
print(data)
```

### JavaScript (Fetch)

```javascript
const url = "https://api.unusualwhales.com/api/market/economic-calendar";
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
      "type": "string",
      "time": "string (ISO 8601)",
      "event": "string",
      "reported_period": "string",
      "prev": "string",
      "forecast": "string"
    }
  ]
}
```

### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| data | array | Array of economic calendar events |
| type | string | Type of event (e.g., "report", "13F", "employment", etc.) |
| time | string | ISO 8601 formatted timestamp of event release |
| event | string | Name of the economic event |
| reported_period | string | Period that the data covers (e.g., "Q3", "September", "October") |
| prev | string | Previous reported value for comparison |
| forecast | string | Market forecast/expectation for the event |

## Example Response

```json
{
  "data": [
    {
      "type": "13F",
      "time": "2025-11-14T23:00:00Z",
      "prev": "",
      "event": "13F Deadline",
      "reported_period": "Q3",
      "forecast": ""
    },
    {
      "type": "report",
      "time": "2025-10-24T14:00:00Z",
      "prev": "800000",
      "event": "*New home sales",
      "reported_period": "September",
      "forecast": "710000"
    },
    {
      "type": "report",
      "time": "2025-10-24T14:00:00Z",
      "prev": "55",
      "event": "Consumer sentiment (final)",
      "reported_period": "October",
      "forecast": "54.4"
    }
  ]
}
```

## Error Responses

| Status Code | Description | Response Body |
|-------------|-------------|---------------|
| 401 | Unauthorized | `{"error": "Invalid API key"}` |
| 500 | Internal Server Error | `{"error": "Server error"}` |

## Rate Limiting

Standard API rate limits apply. This endpoint retrieves static calendar data with minimal computational overhead.

## Notes

- The calendar is typically updated daily with new economic events
- Times are provided in UTC/ISO 8601 format
- Some fields (prev, forecast) may be empty for certain event types
- Events are listed chronologically and may include both future and past events
- The asterisk (*) in event names may indicate special events or revised data
- No parameters are required; this endpoint returns the full economic calendar

## Related Endpoints

- [/api/market/fda-calendar](./fda-calendar.md) - FDA calendar events and drug approval timelines
- [/api/market/spike](./spike.md) - SPIKE volatility index values
- [/api/market/market-tide](./market-tide.md) - Market sentiment based on options activity

## Validation Results

**Tested**: Yes

**Test Date**: 2025-10-22

**Status**: Working

**Notes**: Endpoint returns successfully with economic calendar data. Response includes both upcoming events and recent historical events.

**Response Time**: < 1 second

**Sample Events Include**:
- 13F Filings
- New Home Sales
- Consumer Sentiment
- Other major economic indicators

**Test Command**:
```bash
curl -s "https://api.unusualwhales.com/api/market/economic-calendar" \
  -H "Authorization: Bearer 5d1ec006-49f0-4a2a-90ae-5176c72425e3"
```
