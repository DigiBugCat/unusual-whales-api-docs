# Price Change Per Month Per Year

## Endpoint Details

**Path**: `GET /api/seasonality/{ticker}/year-month`

**Operation ID**: `PublicApi.SeasonalityController.year_month`

**Summary**: Price change per month per year

**Tags**: seasonality

## Description

Returns the relative price change for all past months over multiple years for a given ticker. This endpoint provides a detailed breakdown of monthly performance across years, allowing analysis of how specific months have performed for a stock across its trading history.

## Authentication

- **Required**: Yes
- **Type**: API Key
- **Header**: `Authorization: Bearer YOUR_API_KEY`

## Request Parameters

### Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ticker | string | Yes | Stock ticker symbol (e.g., AAPL, TSLA) |

### Query Parameters

None

### Request Body

None

## Example Requests

### cURL

```bash
curl -X GET "https://api.unusualwhales.com/api/seasonality/AAPL/year-month" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

### Python

```python
import requests

url = "https://api.unusualwhales.com/api/seasonality/AAPL/year-month"
headers = {
    "Authorization": "Bearer YOUR_API_KEY"
}

response = requests.get(url, headers=headers)
data = response.json()
print(data)
```

### JavaScript (Fetch)

```javascript
const url = "https://api.unusualwhales.com/api/seasonality/AAPL/year-month";
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
      "close": "236",
      "open": "250.42",
      "month": 1,
      "year": 2025,
      "change": "-0.0576"
    }
  ]
}
```

### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| data | array | Array of monthly price change records |
| year | integer | The calendar year (e.g., 2025, 2024) |
| month | integer | The calendar month (1-12) |
| open | string | Opening price for the month |
| close | string | Closing price for the month |
| change | string | Relative price change for the month (decimal format) |

## Example Response

```json
{
  "data": [
    {
      "close": "236",
      "open": "250.42",
      "month": 1,
      "year": 2025,
      "change": "-0.0576"
    },
    {
      "close": "241.84",
      "open": "236",
      "month": 2,
      "year": 2025,
      "change": "0.0247"
    },
    {
      "close": "222.13",
      "open": "241.84",
      "month": 3,
      "year": 2025,
      "change": "-0.0815"
    },
    {
      "close": "184.40",
      "open": "192.53",
      "month": 1,
      "year": 2024,
      "change": "-0.0422"
    }
  ]
}
```

## Error Responses

| Status Code | Description | Response Body |
|-------------|-------------|---------------|
| 400 | Bad Request | `{"error": "Invalid parameters"}` |
| 401 | Unauthorized | `{"error": "Invalid API key"}` |
| 404 | Not Found | `{"error": "Ticker not found"}` |
| 422 | Unprocessable Entity | `{"error": "Invalid ticker symbol"}` |
| 500 | Internal Server Error | `{"error": "Server error"}` |

## Rate Limiting

The API enforces rate limits on requests. Standard tier allows reasonable request frequency. Check response headers for rate limit information.

## Notes

- Returns data for multiple years, typically 15-20+ years of history depending on ticker age
- Data is sorted by year descending (most recent first)
- Change values are in decimal format (e.g., -0.0576 = -5.76%)
- Open and close prices represent the monthly boundaries
- Useful for comparing how specific months have performed across different years
- Data is updated with the most recent trading data daily

## Related Endpoints

- `/api/seasonality/market` - Get seasonality for major market indices
- `/api/seasonality/{ticker}/monthly` - Get average monthly seasonality statistics
- `/api/seasonality/{month}/performers` - Get best performing stocks for a specific month

## Validation Results

**Tested**: Yes

**Test Date**: 2025-10-22

**Status**: Working

**Notes**: Endpoint successfully returns year-month data for AAPL. Response includes data spanning multiple years (2024-2025 visible in test). Each record includes OHLC-style month data. No errors encountered during testing.
