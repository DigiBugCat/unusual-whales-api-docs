# SPIKE

## Endpoint Details

**Path**: `GET /api/market/spike`

**Operation ID**: `PublicApi.MarketController.spike`

**Summary**: Returns SPIKE volatility index values

**Tags**: market

## Description

Returns the SPIKE values for the given date. SPIKE is a proprietary volatility index based on options market activity. Date must be the current or a past date. If no date is given, returns data for the current/last market day.

## Authentication

- **Required**: Yes
- **Type**: API Key
- **Header**: `Authorization: Bearer YOUR_API_KEY`

## Request Parameters

### Query Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| date | string | No | current/last market day | Market date in YYYY-MM-DD format |

## Example Requests

### cURL

```bash
curl -X GET "https://api.unusualwhales.com/api/market/spike" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

### Python

```python
import requests

url = "https://api.unusualwhales.com/api/market/spike"
headers = {
    "Authorization": "Bearer YOUR_API_KEY"
}

response = requests.get(url, headers=headers)
data = response.json()
print(data)
```

### JavaScript (Fetch)

```javascript
const url = "https://api.unusualwhales.com/api/market/spike";
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

The response will contain SPIKE volatility values. The structure may vary based on available data.

```json
{
  "data": []
}
```

### Response Fields

Data structure depends on SPIKE value availability for the requested date.

## Example Response

```json
{
  "data": []
}
```

Note: Response may be empty if SPIKE data is not yet available for the requested date or if it's not a trading day.

## Error Responses

| Status Code | Description | Response Body |
|-------------|-------------|---------------|
| 400 | Bad Request | `{"error": "Invalid date format"}` |
| 401 | Unauthorized | `{"error": "Invalid API key"}` |
| 422 | Unprocessable Entity | `{"error": "Invalid parameters"}` |
| 500 | Internal Server Error | `{"error": "Server error"}` |

## Rate Limiting

Standard API rate limits apply.

## Notes

- SPIKE is a proprietary volatility indicator based on options market activity
- Data availability may depend on market hours and data processing
- Response may be empty for certain dates or non-trading days
- This endpoint complements other volatility indicators like VIX

## Related Endpoints

- [/api/market/market-tide](./market-tide.md) - Real-time market sentiment
- [/api/market/economic-calendar](./economic-calendar.md) - Economic events that drive volatility
- [/api/market/sector-etfs](./sector-etfs.md) - Sector performance metrics

## Validation Results

**Tested**: Yes

**Test Date**: 2025-10-22

**Status**: Working - Returns empty data array

**Notes**: Endpoint returns successfully but currently returns empty data for the test date. This may indicate that SPIKE data is not available for the current date or that it's calculated during specific times.

**Response Time**: < 1 second

**Test Command**:
```bash
curl -s "https://api.unusualwhales.com/api/market/spike" \
  -H "Authorization: Bearer 5d1ec006-49f0-4a2a-90ae-5176c72425e3"
```
