# Premarket

## Endpoint Details

**Path**: `GET /api/earnings/premarket`

**Operation ID**: `PublicApi.EarningsController.premarket`

**Summary**: Premarket

**Tags**: earnings

## Description

Returns the premarket earnings for a given date.


## Authentication

- **Required**: Yes
- **Type**: API Key
- **Header**: `Authorization: Bearer YOUR_API_KEY`

## Request Parameters

### Query Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| date | string | No |  |
| limit | string | No |  |
| page | string | No |  |


## Example Requests

### cURL

```bash
curl -X GET "https://api.unusualwhales.com/api/earnings/premarket?limit=10" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

### Python

```python
import requests

url = "https://api.unusualwhales.com/api/earnings/premarket"
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
const url = "https://api.unusualwhales.com/api/earnings/premarket?limit=10";
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
      "symbol": "TMO",
      "source": "company",
      "country_code": "US",
      "full_name": "THERMO FISHER SCIENTIFIC",
      "sector": "Healthcare",
      "has_options": true,
      "marketcap": "210703787397",
      "is_s_p_500": true,
      "country_name": "UNITED STATES",
      "continent": "North America",
      "report_date": "2025-10-22",
      "report_time": "premarket",
      "actual_eps": null,
      "ending_fiscal_quarter": "2025-09-30",
      "expected_move": "22.49",
      "expected_move_perc": "0.040307",
      "reaction": "0.0165",
      "street_mean_est": "5.50",
      "pre_earnings_date": "2025-10-21",
      "pre_earnings_close": "557.99",
      "post_earnings_date": "2025-10-22",
      "post_earnings_close": "567.2"
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
