# Recent Reports By Trader

## Endpoint Details

**Path**: `GET /api/congress/congress-trader`

**Operation ID**: `PublicApi.CongressController.congress_trader`

**Summary**: Recent Reports By Trader

**Tags**: congress

## Description

Returns the recent reports by the given congress member.


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
| ticker | string | No |  |
| name | string | No |  |


## Example Requests

### cURL

```bash
curl -X GET "https://api.unusualwhales.com/api/congress/congress-trader?limit=10" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

### Python

```python
import requests

url = "https://api.unusualwhales.com/api/congress/congress-trader"
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
const url = "https://api.unusualwhales.com/api/congress/congress-trader?limit=10";
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
      "name": "Nancy Pelosi",
      "ticker": "AVGO",
      "issuer": "spouse",
      "reporter": "Hon. Nancy Pelosi",
      "txn_type": "Exercise",
      "amounts": "$1,000,001 - $5,000,000",
      "notes": "Broadcom Inc. - Common Stock (AVGO) [ST] FILING STATUS: New",
      "transaction_date": "2025-06-20",
      "filed_at_date": "2025-07-09",
      "member_type": "house"
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
