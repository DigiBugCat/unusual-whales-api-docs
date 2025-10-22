# Average Return per Month

## Endpoint Details

**Path**: `GET /api/seasonality/{ticker}/monthly`

**Operation ID**: `PublicApi.SeasonalityController.monthly`

**Summary**: Average return per month

**Tags**: seasonality

## Description

Returns the average return by month for the given ticker. This endpoint provides historical seasonality analysis showing how a specific stock typically performs in each calendar month based on historical data.

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
curl -X GET "https://api.unusualwhales.com/api/seasonality/AAPL/monthly" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

### Python

```python
import requests

url = "https://api.unusualwhales.com/api/seasonality/AAPL/monthly"
headers = {
    "Authorization": "Bearer YOUR_API_KEY"
}

response = requests.get(url, headers=headers)
data = response.json()
print(data)
```

### JavaScript (Fetch)

```javascript
const url = "https://api.unusualwhales.com/api/seasonality/AAPL/monthly";
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
      "month": 1,
      "ticker": "AAPL",
      "years": 18,
      "sector": "Technology",
      "marketcap": "3899609280300",
      "positive_months_perc": "0.5000",
      "min_change": "-0.3215",
      "median_change": "-0.0117",
      "max_change": "0.1147",
      "avg_change": "-0.0166",
      "positive_closes": 9
    }
  ]
}
```

### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| data | array | Array of 12 monthly seasonality records |
| month | integer | Calendar month (1-12) |
| ticker | string | The requested ticker symbol |
| years | integer | Number of years of data included in the calculation |
| sector | string | Sector classification of the stock |
| marketcap | string | Market capitalization of the company |
| positive_months_perc | string | Percentage of months that closed positive (0.0-1.0) |
| min_change | string | Minimum monthly return across all years |
| median_change | string | Median monthly return |
| max_change | string | Maximum monthly return |
| avg_change | string | Average monthly return |
| positive_closes | integer | Count of months that closed positive |

## Example Response

```json
{
  "data": [
    {
      "month": 1,
      "ticker": "AAPL",
      "years": 18,
      "sector": "Technology",
      "marketcap": "3899609280300",
      "positive_months_perc": "0.5000",
      "min_change": "-0.3215",
      "median_change": "-0.0117",
      "max_change": "0.1147",
      "avg_change": "-0.0166",
      "positive_closes": 9
    },
    {
      "month": 2,
      "ticker": "AAPL",
      "years": 18,
      "sector": "Technology",
      "marketcap": "3899609280300",
      "positive_months_perc": "0.6667",
      "min_change": "-0.1017",
      "median_change": "0.0239",
      "max_change": "0.1831",
      "avg_change": "0.0144",
      "positive_closes": 12
    },
    {
      "month": 3,
      "ticker": "AAPL",
      "years": 18,
      "sector": "Technology",
      "marketcap": "3899609280300",
      "positive_months_perc": "0.6667",
      "min_change": "-0.0992",
      "median_change": "0.0418",
      "max_change": "0.1947",
      "avg_change": "0.0416",
      "positive_closes": 12
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

- Returns 12 records (one for each month) sorted by month number
- All percentage values are returned as decimal strings (e.g., "0.5000" = 50%)
- The data includes sector and market cap information for additional context
- Works with any valid stock ticker symbol
- Historical data typically spans 15-20 years depending on the stock's trading history
- Useful for identifying seasonal trading patterns for specific stocks

## Related Endpoints

- `/api/seasonality/market` - Get seasonality for major market indices
- `/api/seasonality/{ticker}/year-month` - Get year-by-year monthly price changes
- `/api/seasonality/{month}/performers` - Get best performing stocks for a specific month

## Validation Results

**Tested**: Yes

**Test Date**: 2025-10-22

**Status**: Working

**Notes**: Endpoint successfully returns monthly seasonality data for AAPL. Response includes 12 months of data with complete statistics. Sector information and market cap data included. No errors encountered.
