# Market Correlations

## Endpoint Details

**Path**: `GET /api/market/correlations`

**Operation ID**: `PublicApi.MarketController.correlations`

**Summary**: Returns the correlations between a list of tickers.

**Tags**: market

## Description

Returns the correlations between a list of tickers. Date must be the current or a past date. If no date is given, returns data for the current/last market day.

You can filter the time period either by:
1. Using the `interval` parameter (e.g. "1y", "6m", "3m", "1m")
2. Using `start_date` and optionally `end_date` (if `end_date` is not provided, it defaults to the current date)

If you send `interval` alongside `start_date`, `interval` filter will take priority.

## Authentication

- **Required**: Yes
- **Type**: API Key
- **Header**: `Authorization: Bearer YOUR_API_KEY`

## Request Parameters

### Query Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| tickers | string | Yes | N/A | Comma-separated list of ticker symbols to correlate (e.g., "AAPL,MSFT,GOOGL") |
| interval | string | No | null | Time period for correlation calculation: "1y", "6m", "3m", "1m". Takes priority over start_date if both provided |
| start_date | string | No | null | Start date for correlation period in YYYY-MM-DD format |
| end_date | string | No | current date | End date for correlation period in YYYY-MM-DD format |

## Example Requests

### cURL

```bash
curl -X GET "https://api.unusualwhales.com/api/market/correlations?tickers=AAPL,MSFT&interval=1m" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

### Python

```python
import requests

url = "https://api.unusualwhales.com/api/market/correlations"
headers = {
    "Authorization": "Bearer YOUR_API_KEY"
}
params = {
    "tickers": "AAPL,MSFT",
    "interval": "1m"
}

response = requests.get(url, headers=headers, params=params)
data = response.json()
print(data)
```

### JavaScript (Fetch)

```javascript
const url = "https://api.unusualwhales.com/api/market/correlations?tickers=AAPL,MSFT&interval=1m";
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

The response returns a data array containing correlation matrices and data points for the specified tickers.

### Response Structure

```json
{
  "data": [
    {
      "ticker1": "string",
      "ticker2": "string",
      "correlation": "float"
    }
  ]
}
```

### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| data | array | Array of correlation data between ticker pairs |
| ticker1 | string | First ticker symbol in the correlation pair |
| ticker2 | string | Second ticker symbol in the correlation pair |
| correlation | float | Correlation coefficient between -1 and 1 |

## Example Response

```json
{
  "data": []
}
```

Note: The response may be empty if there is no correlation data available for the specified parameters or date range.

## Error Responses

| Status Code | Description | Response Body |
|-------------|-------------|---------------|
| 400 | Bad Request | `{"error": "Invalid parameters"}` |
| 401 | Unauthorized | `{"error": "Invalid API key"}` |
| 422 | Unprocessable Entity | `{"error": "Invalid ticker symbols or date range"}` |
| 500 | Internal Server Error | `{"error": "Server error"}` |

## Rate Limiting

Standard API rate limits apply. No specific rate limiting documented for this endpoint.

## Notes

- The `tickers` parameter is required and must contain at least 2 tickers to calculate correlations
- Correlation values range from -1 (perfect negative correlation) to +1 (perfect positive correlation)
- If no date is provided, data for the current or last market day is returned
- The `interval` parameter takes priority over `start_date` if both are provided
- Historical data availability may vary; check the response for actual available data

## Related Endpoints

- [/api/market/market-tide](./market-tide.md) - Real-time market sentiment based on options activity
- [/api/market/sector-etfs](./sector-etfs.md) - Current trading day statistics for SPDR sector ETFs
- [/api/market/spike](./spike.md) - SPIKE volatility values

## Validation Results

**Tested**: Yes

**Test Date**: 2025-10-22

**Status**: Working

**Notes**: Endpoint returns successfully but may return empty data array if no correlation data is available for the specified tickers and date range. This is expected behavior when data is not yet available or for future dates.

**Response Time**: < 1 second

**Test Command**:
```bash
curl -s "https://api.unusualwhales.com/api/market/correlations?tickers=AAPL,MSFT&interval=1m" \
  -H "Authorization: Bearer 5d1ec006-49f0-4a2a-90ae-5176c72425e3"
```
