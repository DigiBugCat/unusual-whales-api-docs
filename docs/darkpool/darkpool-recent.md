# Recent Darkpool Trades

## Endpoint Details

**Path**: `GET /api/darkpool/recent`

**Operation ID**: `PublicApi.DarkpoolController.darkpool_recent`

**Summary**: Recent Darkpool Trades

**Tags**: darkpool

## Description

Returns the latest darkpool trades.


## Authentication

- **Required**: Yes
- **Type**: API Key
- **Header**: `Authorization: Bearer YOUR_API_KEY`

## Request Parameters

### Query Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| limit | string | No |  |
| date | string | No |  |
| min_premium | string | No |  |
| max_premium | string | No |  |
| min_size | string | No |  |
| max_size | string | No |  |
| min_volume | string | No |  |
| max_volume | string | No |  |


## Example Requests

### cURL

```bash
curl -X GET "https://api.unusualwhales.com/api/darkpool/recent?limit=10" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

### Python

```python
import requests

url = "https://api.unusualwhales.com/api/darkpool/recent"
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
const url = "https://api.unusualwhales.com/api/darkpool/recent?limit=10";
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
      "size": 5764,
      "ticker": "MRNA",
      "price": "25.58",
      "volume": 7764959,
      "executed_at": "2025-10-22T21:24:30Z",
      "premium": "147443.12",
      "nbbo_bid": "25.54",
      "nbbo_ask": "26",
      "canceled": false,
      "ext_hour_sold_codes": "extended_hours_trade",
      "market_center": "L",
      "nbbo_ask_quantity": 100,
      "nbbo_bid_quantity": 100,
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
