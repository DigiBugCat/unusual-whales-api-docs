# Ticker Darkpool Trades

## Endpoint Details

**Path**: `GET /api/darkpool/{ticker}`

**Operation ID**: `PublicApi.DarkpoolController.darkpool_ticker`

**Summary**: Ticker Darkpool Trades

**Tags**: darkpool

## Description

Returns the darkpool trades for the given ticker on a given day.
Date must be the current or a past date. If no date is given, returns data for the current/last market day.


## Authentication

- **Required**: Yes
- **Type**: API Key
- **Header**: `Authorization: Bearer YOUR_API_KEY`

## Request Parameters

### Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ticker | string | Yes |  |


### Query Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| date | string | No |  |
| newer_than | string | No |  |
| older_than | string | No |  |
| min_premium | string | No |  |
| max_premium | string | No |  |
| min_size | string | No |  |
| max_size | string | No |  |
| min_volume | string | No |  |
| max_volume | string | No |  |
| limit | string | No |  |


## Example Requests

### cURL

```bash
curl -X GET "https://api.unusualwhales.com/api/darkpool/AAPL?limit=10" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

### Python

```python
import requests

url = "https://api.unusualwhales.com/api/darkpool/AAPL"
headers = {
    "Authorization": "Bearer YOUR_API_KEY"
}
params = {
    "limit": 10
}

response = requests.get(url, headers=headers, params=params)
data = response.json()
print(data)
```

### JavaScript (Fetch)

```javascript
const url = "https://api.unusualwhales.com/api/darkpool/AAPL?limit=10";
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

The response returns data matching the schema defined in the OpenAPI specification.

## Example Response

```json
{
  "data": [
    {
      "size": 9399,
      "ticker": "AAPL",
      "price": "258.45",
      "volume": 44915021,
      "executed_at": "2025-10-22T21:23:24Z",
      "premium": "2429171.55",
      "nbbo_bid": "258.5",
      "nbbo_ask": "258.6",
      "canceled": false,
      "ext_hour_sold_codes": "extended_hours_trade",
      "market_center": "L",
      "nbbo_ask_quantity": 97,
      "nbbo_bid_quantity": 40,
      "sale_cond_codes": null,
      "tracking_id": 0,
      "trade_code": null,
      "trade_settlement": "regular"
    }
  ]
}
```

## Error Responses

| Status Code | Description |
|-------------|-------------|
| 200 | OK - Successful response |
| 400 | Bad Request - Invalid parameters |
| 401 | Unauthorized - Invalid API key |
| 422 | Unprocessable Entity - Invalid filter parameters |
| 500 | Internal Server Error |

## Rate Limiting

API rate limits are enforced per API key. Monitor the response headers for rate limit information.

## Notes

- The endpoint requires valid authentication via API key
- Results can be filtered using available query parameters
- The API returns structured data in JSON format
- Paginated results may be available through limit parameter

## Related Endpoints

- [Alerts](/api/alerts) - Get user alerts
- [Congress Trades](/api/congress/recent-trades) - Get congress member trades
- [Darkpool Trades](/api/darkpool/recent) - Get darkpool trading data
- [Earnings Data](/api/earnings) - Get earnings information

## Validation Results

**Tested**: Yes

**Test Date**: 2025-10-22

**Status**: Working

**Notes**: Endpoint returned 200 OK with valid response data.
