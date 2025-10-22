# Short Data

## Endpoint Details

**Path**: `GET /api/shorts/{ticker}/data`

**Operation ID**: `PublicApi.ShortController.short_data`

**Summary**: Short Data

**Tags**: shorts

## Description

Returns short data including rebate rate and short shares available for a ticker. This endpoint provides real-time or near real-time information about borrowing costs and availability for short positions, updated frequently throughout the trading day.

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
curl -X GET "https://api.unusualwhales.com/api/shorts/AAPL/data" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

### Python

```python
import requests

url = "https://api.unusualwhales.com/api/shorts/AAPL/data"
headers = {
    "Authorization": "Bearer YOUR_API_KEY"
}

response = requests.get(url, headers=headers)
data = response.json()
print(data)
```

### JavaScript (Fetch)

```javascript
const url = "https://api.unusualwhales.com/api/shorts/AAPL/data";
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
      "name": "APPLE INC",
      "timestamp": "2025-10-22T15:16:53Z",
      "symbol": "AAPL",
      "short_shares_available": 10000000,
      "rebate_rate": "3.8600",
      "fee_rate": "0.2500"
    }
  ]
}
```

### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| data | array | Array of short data points, typically includes multiple timestamps throughout the day |
| name | string | Full company name |
| symbol | string | Stock ticker symbol |
| timestamp | string | ISO 8601 timestamp when the data was recorded |
| short_shares_available | integer | Number of shares available to borrow for short selling |
| rebate_rate | string | Rebate rate percentage (what you earn on short proceeds) |
| fee_rate | string | Borrow fee rate percentage (cost of borrowing shares) |

## Example Response

```json
{
  "data": [
    {
      "name": "APPLE INC",
      "timestamp": "2025-10-22T15:16:53Z",
      "symbol": "AAPL",
      "short_shares_available": 10000000,
      "rebate_rate": "3.8600",
      "fee_rate": "0.2500"
    },
    {
      "name": "APPLE INC",
      "timestamp": "2025-10-22T14:45:48Z",
      "symbol": "AAPL",
      "short_shares_available": 10000000,
      "rebate_rate": "3.8600",
      "fee_rate": "0.2500"
    },
    {
      "name": "APPLE INC",
      "timestamp": "2025-10-21T15:16:49Z",
      "symbol": "AAPL",
      "short_shares_available": 10000000,
      "rebate_rate": "3.7019",
      "fee_rate": "0.4081"
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

- Response includes multiple data points throughout the day, sorted by timestamp descending (most recent first)
- Rebate rate is the return on short cash proceeds held with the broker
- Fee rate is the cost of borrowing shares (annual percentage)
- Both rates are returned as string percentages (e.g., "3.8600" = 3.86%)
- Short shares available can change frequently based on demand
- Net borrow cost = fee_rate - rebate_rate
- Data is typically updated every 30 minutes during market hours
- Used to evaluate short position costs and availability

## Related Endpoints

- `/api/shorts/{ticker}/interest-float` - Get short interest and float data
- `/api/shorts/{ticker}/ftds` - Get failures to deliver data
- `/api/shorts/{ticker}/volume-and-ratio` - Get short volume and ratio data
- `/api/shorts/{ticker}/volumes-by-exchange` - Get short volumes by exchange

## Validation Results

**Tested**: Yes

**Test Date**: 2025-10-22

**Status**: Working

**Notes**: Endpoint successfully returns short borrow data for AAPL. Response includes multiple historical data points from recent dates. Rebate rates and fee rates vary over time as shown. All fields populated correctly with valid data.
