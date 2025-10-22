# Recent Late Reports

## Endpoint Details

**Path**: `GET /api/congress/late-reports`

**Operation ID**: `PublicApi.CongressController.congress_late_reports`

**Summary**: Recent Late Reports

**Tags**: congress

## Description

Returns the recent late reports by congress members.
If a date is given, will only return recent late reports, which's report date is <= the given input date.


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


## Example Requests

### cURL

```bash
curl -X GET "https://api.unusualwhales.com/api/congress/late-reports?limit=10" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

### Python

```python
import requests

url = "https://api.unusualwhales.com/api/congress/late-reports"
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
const url = "https://api.unusualwhales.com/api/congress/late-reports?limit=10";
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
      "ticker": "ONSOLVE LLC",
      "issuer": "ONSOLVE LLC",
      "reporter": "Pat Ryan",
      "txn_type": "Sell",
      "amounts": "$15,001 - $50,000",
      "notes": "",
      "transaction_date": "2024-07-31",
      "filed_at_date": "2025-10-10",
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
