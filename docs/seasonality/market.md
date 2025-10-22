# Market Seasonality

## Endpoint Details

**Path**: `GET /api/seasonality/market`

**Operation ID**: `PublicApi.SeasonalityController.market_seasonality`

**Summary**: Market Seasonality

**Tags**: seasonality

## Description

Returns the average return by month for the major market index ETFs: SPY, QQQ, IWM, XLE, XLC, XLK, XLV, XLP, XLY, XLRE, XLF, XLI, XLB.

This endpoint provides historical seasonality data showing average returns for each calendar month across these representative market indices, helping traders identify seasonal trends and patterns.

## Authentication

- **Required**: Yes
- **Type**: API Key
- **Header**: `Authorization: Bearer YOUR_API_KEY`

## Request Parameters

### Path Parameters

None

### Query Parameters

None - this endpoint does not accept query parameters.

### Request Body

None

## Example Requests

### cURL

```bash
curl -X GET "https://api.unusualwhales.com/api/seasonality/market" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

### Python

```python
import requests

url = "https://api.unusualwhales.com/api/seasonality/market"
headers = {
    "Authorization": "Bearer YOUR_API_KEY"
}

response = requests.get(url, headers=headers)
data = response.json()
print(data)
```

### JavaScript (Fetch)

```javascript
const url = "https://api.unusualwhales.com/api/seasonality/market";
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
      "ticker": "IWM",
      "years": 18,
      "positive_months_perc": "0.4444",
      "min_change": "-0.1057",
      "median_change": "-0.0125",
      "max_change": "0.1278",
      "avg_change": "-0.0086",
      "positive_closes": 8
    }
  ]
}
```

### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| data | array | Array of seasonality records for each ticker/month combination |
| month | integer | Calendar month (1-12) |
| ticker | string | Symbol of the ETF (SPY, QQQ, IWM, XLE, etc.) |
| years | integer | Number of years of data included in the calculation |
| positive_months_perc | string | Percentage of months that closed positive (0.0-1.0) |
| min_change | string | Minimum monthly return across all years for this month/ticker |
| median_change | string | Median monthly return for this month/ticker |
| max_change | string | Maximum monthly return for this month/ticker |
| avg_change | string | Average monthly return for this month/ticker |
| positive_closes | integer | Count of months that closed positive |

## Example Response

```json
{
  "data": [
    {
      "month": 1,
      "ticker": "IWM",
      "years": 18,
      "positive_months_perc": "0.4444",
      "min_change": "-0.1057",
      "median_change": "-0.0125",
      "max_change": "0.1278",
      "avg_change": "-0.0086",
      "positive_closes": 8
    },
    {
      "month": 2,
      "ticker": "IWM",
      "years": 18,
      "positive_months_perc": "0.6667",
      "min_change": "-0.1033",
      "median_change": "0.0082",
      "max_change": "0.0556",
      "avg_change": "0.0033",
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
| 422 | Unprocessable Entity | `{"error": "Unprocessable Entity"}` |
| 500 | Internal Server Error | `{"error": "Server error"}` |

## Rate Limiting

The API enforces rate limits on requests. Standard tier allows reasonable request frequency. Check response headers for rate limit information.

## Notes

- The endpoint returns data for 13 major market index ETFs
- Data includes up to 18 years of historical seasonal information
- All percentage values are returned as decimal strings (e.g., "0.5000" = 50%)
- The data helps identify which months historically have positive or negative returns
- This is a static endpoint - it doesn't require any parameters and returns comprehensive data
- Data appears to be updated with daily market close prices
- Used to help traders understand seasonal market trends and patterns

## Related Endpoints

- `/api/seasonality/{ticker}/monthly` - Get seasonality data for a specific ticker
- `/api/seasonality/{ticker}/year-month` - Get year-by-year monthly price changes
- `/api/seasonality/{month}/performers` - Get best performing stocks for a specific month

## Validation Results

**Tested**: Yes

**Test Date**: 2025-10-22

**Status**: Working

**Notes**: Endpoint returns valid data for all 13 major market indices. Response structure is consistent with documented schema. No authentication errors or rate limit issues encountered during testing. Data includes complete seasonal analysis across multiple years.
