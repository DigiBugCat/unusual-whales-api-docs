# Short Interest and Float

## Endpoint Details

**Path**: `GET /api/shorts/{ticker}/interest-float`

**Operation ID**: `PublicApi.ShortController.short_interest_and_float`

**Summary**: Short Interest and Float

**Tags**: shorts

## Description

Returns short interest and float data for percentage calculations for a ticker. This endpoint provides information about the percentage of float that is shorted, the float size, and the days to cover. It's useful for assessing short squeeze potential and understanding short positioning.

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
curl -X GET "https://api.unusualwhales.com/api/shorts/AAPL/interest-float" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

### Python

```python
import requests

url = "https://api.unusualwhales.com/api/shorts/AAPL/interest-float"
headers = {
    "Authorization": "Bearer YOUR_API_KEY"
}

response = requests.get(url, headers=headers)
data = response.json()
print(data)
```

### JavaScript (Fetch)

```javascript
const url = "https://api.unusualwhales.com/api/shorts/AAPL/interest-float";
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
      "date": "2025-10-21",
      "ticker": "AAPL",
      "short_interest": 125000000,
      "float": 15200000000,
      "short_float_perc": "0.0082",
      "shares_outstanding": 15500000000,
      "short_interest_perc": "0.0081",
      "days_to_cover": 2.5,
      "avg_volume": 50000000
    }
  ]
}
```

### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| data | array | Array of short interest and float records |
| date | string | Report date in YYYY-MM-DD format |
| ticker | string | Stock ticker symbol |
| short_interest | integer | Total shares sold short but not yet covered |
| float | integer | Freely tradeable shares (excluding restricted shares) |
| short_float_perc | string | Short interest as percentage of float |
| shares_outstanding | integer | Total shares outstanding |
| short_interest_perc | string | Short interest as percentage of shares outstanding |
| days_to_cover | number | Number of days of average volume needed to cover all shorts |
| avg_volume | integer | Average daily trading volume |

## Example Response

```json
{
  "data": [
    {
      "date": "2025-10-21",
      "ticker": "AAPL",
      "short_interest": 125000000,
      "float": 15200000000,
      "short_float_perc": "0.0082",
      "shares_outstanding": 15500000000,
      "short_interest_perc": "0.0081",
      "days_to_cover": 2.5,
      "avg_volume": 50000000
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

- Data is typically reported bi-weekly and updated frequently
- short_float_perc is the key metric for short squeeze potential analysis
- Days to cover = short_interest / avg_volume - indicates how many trading days it would take to cover all shorts
- Higher days_to_cover values may indicate greater short squeeze potential
- Float is typically less than shares_outstanding due to restricted shares
- Used by traders to identify potential short squeeze candidates
- Percentage values are returned as decimal strings

## Related Endpoints

- `/api/shorts/{ticker}/data` - Get current short borrow rates
- `/api/shorts/{ticker}/ftds` - Get failures to deliver data
- `/api/shorts/{ticker}/volume-and-ratio` - Get short volume and ratio data
- `/api/shorts/{ticker}/volumes-by-exchange` - Get short volumes by exchange

## Validation Results

**Tested**: Yes (endpoint structure confirmed)

**Test Date**: 2025-10-22

**Status**: Working

**Notes**: Endpoint accessible and returns short interest and float metrics. Key metrics for short squeeze analysis are available. Data is updated regularly with latest short interest reports.
