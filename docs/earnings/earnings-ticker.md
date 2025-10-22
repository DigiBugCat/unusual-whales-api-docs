# Historical Ticker Earnings

## Endpoint Details

**Path**: `GET /api/earnings/{ticker}`

**Operation ID**: `PublicApi.EarningsController.ticker`

**Summary**: Historical Ticker Earnings

**Tags**: earnings

## Description

Returns the historical earnings for the given ticker.


## Authentication

- **Required**: Yes
- **Type**: API Key
- **Header**: `Authorization: Bearer YOUR_API_KEY`

## Request Parameters

### Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ticker | string | Yes |  |


## Example Requests

### cURL

```bash
curl -X GET "https://api.unusualwhales.com/api/earnings/AAPL?limit=10" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

### Python

```python
import requests

url = "https://api.unusualwhales.com/api/earnings/AAPL"
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
const url = "https://api.unusualwhales.com/api/earnings/AAPL?limit=10";
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
      "source": "company",
      "report_date": "2025-10-30",
      "report_time": "postmarket",
      "actual_eps": null,
      "ending_fiscal_quarter": "2025-09-30",
      "expected_move": "10.20",
      "expected_move_perc": "0.03946604759141033082",
      "post_earnings_move_1d": null,
      "post_earnings_move_1w": null,
      "post_earnings_move_2w": null,
      "post_earnings_move_3d": null,
      "pre_earnings_move_1d": null,
      "pre_earnings_move_1w": null,
      "pre_earnings_move_2w": null,
      "pre_earnings_move_3d": null,
      "street_mean_est": "1.74",
      "short_straddle_1w": null,
      "short_straddle_1d": null,
      "long_straddle_1w": null,
      "long_straddle_1d": null
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
