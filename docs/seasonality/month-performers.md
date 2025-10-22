# Month Performers

## Endpoint Details

**Path**: `GET /api/seasonality/{month}/performers`

**Operation ID**: `PublicApi.SeasonalityController.month_performers`

**Summary**: Month Performers

**Tags**: seasonality

## Description

Returns the tickers with the highest performance in terms of price change in the specified month over the years. By default, results are ordered by positive_months_perc descending, then median_change descending. This endpoint helps identify which stocks historically perform best in specific calendar months.

## Authentication

- **Required**: Yes
- **Type**: API Key
- **Header**: `Authorization: Bearer YOUR_API_KEY`

## Request Parameters

### Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| month | integer | Yes | Calendar month number (1-12, where 1=January, 12=December) |

### Query Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| limit | integer | No | 50 | Maximum number of results to return |
| offset | integer | No | 0 | Pagination offset |
| sort_by | string | No | positive_months_perc | Field to sort results by (positive_months_perc, median_change, avg_change) |
| order | string | No | desc | Sort order (asc, desc) |

### Request Body

None

## Example Requests

### cURL

```bash
# Get top performers for January
curl -X GET "https://api.unusualwhales.com/api/seasonality/1/performers?limit=10" \
  -H "Authorization: Bearer YOUR_API_KEY"

# Get performers for March with custom sorting
curl -X GET "https://api.unusualwhales.com/api/seasonality/3/performers?limit=20&sort_by=median_change" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

### Python

```python
import requests

url = "https://api.unusualwhales.com/api/seasonality/1/performers"
headers = {
    "Authorization": "Bearer YOUR_API_KEY"
}
params = {
    "limit": 10,
    "sort_by": "median_change"
}

response = requests.get(url, headers=headers, params=params)
data = response.json()
print(data)
```

### JavaScript (Fetch)

```javascript
const url = "https://api.unusualwhales.com/api/seasonality/1/performers?limit=10&sort_by=median_change";
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
      "ticker": "TFLO",
      "years": 10,
      "sector": null,
      "marketcap": "6549383822",
      "positive_months_perc": "1.1000",
      "min_change": "0.0005",
      "median_change": "0.0021",
      "max_change": "0.0046",
      "avg_change": "0.0022",
      "positive_closes": 11
    }
  ]
}
```

### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| data | array | Array of best performing stocks for the given month |
| month | integer | The requested calendar month (1-12) |
| ticker | string | Stock ticker symbol |
| years | integer | Number of years of data for this stock |
| sector | string | Sector classification (may be null) |
| marketcap | string | Market capitalization |
| positive_months_perc | string | Percentage of months that closed positive |
| min_change | string | Minimum monthly change observed |
| median_change | string | Median monthly change |
| max_change | string | Maximum monthly change observed |
| avg_change | string | Average monthly change |
| positive_closes | integer | Count of positive months |

## Example Response

```json
{
  "data": [
    {
      "month": 1,
      "ticker": "TFLO",
      "years": 10,
      "sector": null,
      "marketcap": "6549383822",
      "positive_months_perc": "1.1000",
      "min_change": "0.0005",
      "median_change": "0.0021",
      "max_change": "0.0046",
      "avg_change": "0.0022",
      "positive_closes": 11
    },
    {
      "month": 1,
      "ticker": "NGL",
      "years": 13,
      "sector": "Energy",
      "marketcap": "805438765",
      "positive_months_perc": "1.0000",
      "min_change": "-0.1193",
      "median_change": "0.1110",
      "max_change": "0.4174",
      "avg_change": "0.1191",
      "positive_closes": 13
    },
    {
      "month": 1,
      "ticker": "MINT",
      "years": 15,
      "sector": null,
      "marketcap": "11905234200",
      "positive_months_perc": "1.0000",
      "min_change": "-0.0015",
      "median_change": "0.0014",
      "max_change": "0.0086",
      "avg_change": "0.0023",
      "positive_closes": 15
    }
  ]
}
```

## Error Responses

| Status Code | Description | Response Body |
|-------------|-------------|---------------|
| 400 | Bad Request | `{"error": "Invalid month - must be 1-12"}` |
| 401 | Unauthorized | `{"error": "Invalid API key"}` |
| 422 | Unprocessable Entity | `{"error": "Invalid month parameter"}` |
| 500 | Internal Server Error | `{"error": "Server error"}` |

## Rate Limiting

The API enforces rate limits on requests. Standard tier allows reasonable request frequency. Check response headers for rate limit information.

## Notes

- Month parameter is 1-indexed (1=January, 12=December)
- Default sorting is by positive_months_perc descending, then median_change descending
- positive_months_perc values can exceed 1.0 (represented as decimal string)
- Results are paginated with limit and offset parameters
- Useful for identifying seasonal trading opportunities
- Data spans multiple years for robust statistical analysis
- Includes stocks across all sectors and market caps

## Related Endpoints

- `/api/seasonality/market` - Get seasonality for major market indices
- `/api/seasonality/{ticker}/monthly` - Get seasonality for a specific ticker
- `/api/seasonality/{ticker}/year-month` - Get year-by-year monthly changes

## Validation Results

**Tested**: Yes

**Test Date**: 2025-10-22

**Status**: Working

**Notes**: Endpoint successfully returns top performers for January (month=1). Returns diverse set of stocks sorted by performance metrics. Includes sector and market cap data. Pagination appears to work correctly. No errors encountered.
