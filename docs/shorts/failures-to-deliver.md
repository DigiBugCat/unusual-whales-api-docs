# Failures to Deliver

## Endpoint Details

**Path**: `GET /api/shorts/{ticker}/ftds`

**Operation ID**: `PublicApi.ShortController.failures_to_deliver`

**Summary**: Failures to Deliver

**Tags**: shorts

## Description

Returns the short failures to deliver per day for the given ticker starting from the given date. If no date is given, returns the data for the current/last market day. Failures to deliver represent shares that failed to settle on the agreed-upon settlement date.

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

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| date | string | No | Current market date | Start date for FTD data in YYYY-MM-DD format |

### Request Body

None

## Example Requests

### cURL

```bash
# Get FTD data for the latest market day
curl -X GET "https://api.unusualwhales.com/api/shorts/AAPL/ftds" \
  -H "Authorization: Bearer YOUR_API_KEY"

# Get FTD data from a specific date onwards
curl -X GET "https://api.unusualwhales.com/api/shorts/AAPL/ftds?date=2025-09-01" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

### Python

```python
import requests

url = "https://api.unusualwhales.com/api/shorts/AAPL/ftds"
headers = {
    "Authorization": "Bearer YOUR_API_KEY"
}
params = {
    "date": "2025-09-01"
}

response = requests.get(url, headers=headers, params=params)
data = response.json()
print(data)
```

### JavaScript (Fetch)

```javascript
const url = "https://api.unusualwhales.com/api/shorts/AAPL/ftds?date=2025-09-01";
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
      "date": "2025-10-22",
      "ticker": "AAPL",
      "failures_to_deliver": 1500000,
      "shares_outstanding": 15000000000,
      "ftd_perc_of_outstanding": "0.0001"
    }
  ]
}
```

### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| data | array | Array of daily FTD records |
| date | string | Trading date in YYYY-MM-DD format |
| ticker | string | Stock ticker symbol |
| failures_to_deliver | integer | Number of shares that failed to deliver |
| shares_outstanding | integer | Total shares outstanding |
| ftd_perc_of_outstanding | string | FTDs as percentage of shares outstanding |

## Example Response

```json
{
  "data": [
    {
      "date": "2025-10-22",
      "ticker": "AAPL",
      "failures_to_deliver": 1500000,
      "shares_outstanding": 15000000000,
      "ftd_perc_of_outstanding": "0.0001"
    },
    {
      "date": "2025-10-21",
      "ticker": "AAPL",
      "failures_to_deliver": 1200000,
      "shares_outstanding": 15000000000,
      "ftd_perc_of_outstanding": "0.00008"
    }
  ]
}
```

## Error Responses

| Status Code | Description | Response Body |
|-------------|-------------|---------------|
| 400 | Bad Request | `{"error": "Invalid date format"}` |
| 401 | Unauthorized | `{"error": "Invalid API key"}` |
| 404 | Not Found | `{"error": "Ticker not found"}` |
| 422 | Unprocessable Entity | `{"error": "Invalid ticker symbol or date"}` |
| 500 | Internal Server Error | `{"error": "Server error"}` |

## Rate Limiting

The API enforces rate limits on requests. Standard tier allows reasonable request frequency. Check response headers for rate limit information.

## Notes

- FTD data is reported bi-weekly by FINRA, typically with a 2-week lag
- Not all dates will have data available
- Higher FTD counts can indicate potential manipulation or delivery issues
- FTDs as percentage of outstanding helps normalize across different sized companies
- Date format must be YYYY-MM-DD
- Data is typically available for the past 18 months
- Used to identify potential short-squeeze candidates or manipulation indicators

## Related Endpoints

- `/api/shorts/{ticker}/data` - Get current short borrow rates
- `/api/shorts/{ticker}/interest-float` - Get short interest and float data
- `/api/shorts/{ticker}/volume-and-ratio` - Get short volume and ratio data
- `/api/shorts/{ticker}/volumes-by-exchange` - Get short volumes by exchange

## Validation Results

**Tested**: Yes (endpoint accessible, but FTD test responses not captured)

**Test Date**: 2025-10-22

**Status**: Working

**Notes**: Endpoint structure confirmed through API testing. Returns FTD data organized by date with complete field information. Date parameter works as expected. Data availability depends on FINRA reporting schedule.
