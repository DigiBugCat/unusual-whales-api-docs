# Alerts

## Endpoint Details

**Path**: `GET /api/alerts`

**Operation ID**: `PublicApi.AlertsController.alerts`

**Summary**: Alerts

**Tags**: alerts

## Description

Returns all the alerts that have been triggered for the user.

Time filtering is available using the `newer_than` and `older_than` parameters:
- The maximum lookback period is 14 days
- If no time range is specified, defaults to the last 14 days
- If only one time parameter is provided, the other is automatically calculated to maintain the 14-day limit
- If both parameters are provided but exceed 14 days, the range is adjusted to 14 days from the `older_than` timestamp

The alerts are the same alerts as the user created on [https://unusualwhales.com/custom-alerts](https://unusualwhales.com/custom-alerts)


## Authentication

- **Required**: Yes
- **Type**: API Key
- **Header**: `Authorization: Bearer YOUR_API_KEY`

## Request Parameters

### Query Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| limit | string | No |  |
| intraday_only | string | No |  |
| config_ids[] | string | No |  |
| ticker_symbols | string | No |  |
| noti_types[] | string | No |  |
| newer_than | string (datetime) | No |  |
| older_than | string (datetime) | No |  |


## Example Requests

### cURL

```bash
curl -X GET "https://api.unusualwhales.com/api/alerts?limit=10" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

### Python

```python
import requests

url = "https://api.unusualwhales.com/api/alerts"
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
const url = "https://api.unusualwhales.com/api/alerts?limit=10";
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

The response returns an object with a `data` array containing alert objects. Each alert object contains:
- `id`: Unique identifier for the alert
- `meta`: Metadata object with alert-specific information
- `name`: Name of the alert configuration
- `symbol`: Stock ticker symbol
- `created_at`: ISO timestamp when alert was created
- `tape_time`: ISO timestamp when alert was triggered
- `noti_type`: Type of notification (analyst_rating, insider_trades, thirteen_f_alert, etc.)
- `symbol_type`: Type of symbol (stock, option, etc.)

## Example Response

```json
{
  "data": [
    {
      "id": "1f953b1b-f622-42c6-9e68-daf8a57ae738",
      "meta": {
        "action": "Upgraded",
        "analyst_name": "Lucky Schreiner",
        "curr_stock_price": "64.4157",
        "firm_name": "DA Davidson",
        "price_target": "85.0000",
        "recommendation": "buy",
        "stock_price": "64.4157",
        "ticker": "PEGA",
        "up_downside": "0.3195540838646479041600106806"
      },
      "name": "Test Analyst Ratings",
      "symbol": "PEGA",
      "created_at": "2025-10-22T21:23:51Z",
      "tape_time": "2025-10-22T21:23:50Z",
      "user_noti_config_id": "fb17e5ef-4b84-4b36-8ce2-b13b88f359c3",
      "noti_type": "analyst_rating",
      "symbol_type": "stock"
    },
    {
      "id": "b9a7fb2e-9ee9-4fa1-959a-578702c58346",
      "meta": {
        "amount": 17269,
        "filing_date": "2025-10-22",
        "formtype": "4",
        "is_director": true,
        "is_officer": true,
        "officer_title": "Executive Chairman",
        "owner_name": "STEERS ROBERT HAMILTON",
        "price": 70.0224,
        "transaction_code": "P",
        "transaction_date": "2025-10-22"
      },
      "name": "Test Large Insider Trades",
      "symbol": "CNS",
      "created_at": "2025-10-22T21:13:38Z",
      "tape_time": "2025-10-22T21:13:37Z",
      "noti_type": "insider_trades",
      "symbol_type": "stock"
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
