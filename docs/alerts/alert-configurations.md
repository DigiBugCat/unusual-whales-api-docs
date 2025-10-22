# Alert configurations

## Endpoint Details

**Path**: `GET /api/alerts/configuration`

**Operation ID**: `PublicApi.AlertsController.configs`

**Summary**: Alert configurations

**Tags**: alerts

## Description

Returnst all alert configurations of the user.

Users can create alerts for:
- Market tide
- Gamma exposure (GEX), Vanna exposure (VEX), Charm exposure (CEX)
- Interval Contract screeners (replicates and alerts on the Flow Feed)
- Analyst ratings, price targets, and actions
- Politician trades
- Insider trades
- OI changes for contract in premarket
- FDA
- Flow alerts
- Contract screener (replicates and alerts on the Hottest Chains)
- Stock screeners
- News
- Earnings
- Dividends
- Splits
- Trading stats (halts, unhalts)
- Economic release
- SEC filings

The alerts are the same alerts as the user created on [https://unusualwhales.com/custom-alerts](https://unusualwhales.com/custom-alerts)


## Authentication

- **Required**: Yes
- **Type**: API Key
- **Header**: `Authorization: Bearer YOUR_API_KEY`

## Request Parameters

No parameters required.

## Example Requests

### cURL

```bash
curl -X GET "https://api.unusualwhales.com/api/alerts/configuration?limit=10" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

### Python

```python
import requests

url = "https://api.unusualwhales.com/api/alerts/configuration"
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
const url = "https://api.unusualwhales.com/api/alerts/configuration?limit=10";
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
      "id": "ffa0466a-f1ee-4e54-b96a-07208bec8544",
      "name": "Test Chain OI Change",
      "status": "active",
      "config": {
        "min_oi_change": 1000,
        "option_symbols": [
          "SPY250131C00550000",
          "SPY250131P00500000"
        ],
        "symbols": "all"
      },
      "description": null,
      "created_at": "2025-06-28T02:30:11Z",
      "updated_at": null,
      "noti_type": "chain_oi_change",
      "mobile_only": false
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
