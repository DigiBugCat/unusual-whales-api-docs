# Greek Flow by Expiry

## Endpoint Details

**Path**: `GET /api/group-flow/{flow_group}/greek-flow/{expiry}`

**Operation ID**: `PublicApi.GroupFlowController.greek_flow_expiry`

**Summary**: Greek flow by expiry

**Tags**: group-flow

## Description

Returns the group flow's greek flow (delta & vega flow) for the given market day broken down per minute and expiry. This endpoint provides more granular data by separating greek flows by their option expiration dates. Date must be the current or a past date.

## Authentication

- **Required**: Yes
- **Type**: API Key
- **Header**: `Authorization: Bearer YOUR_API_KEY`

## Request Parameters

### Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| flow_group | string | Yes | The flow group identifier (e.g., call_oi_1dte) |
| expiry | string | Yes | The expiration date (YYYY-MM-DD format) |

### Query Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| date | string | No | current/last date | The market date to retrieve data for (YYYY-MM-DD format) |

### Request Body

Not applicable for this endpoint.

## Example Requests

### cURL

```bash
curl -X GET "https://api.unusualwhales.com/api/group-flow/call_oi_1dte/greek-flow/2025-11-21?date=2025-10-22" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

### Python

```python
import requests

url = "https://api.unusualwhales.com/api/group-flow/call_oi_1dte/greek-flow/2025-11-21"
headers = {
    "Authorization": "Bearer YOUR_API_KEY"
}
params = {
    "date": "2025-10-22"
}

response = requests.get(url, headers=headers, params=params)
data = response.json()
print(data)
```

### JavaScript (Fetch)

```javascript
const url = "https://api.unusualwhales.com/api/group-flow/call_oi_1dte/greek-flow/2025-11-21?date=2025-10-22";
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

The response contains greek flow data broken down per minute for the specified expiration, with delta and vega information.

```json
{
  "data": [
    {
      "time": "string (HH:MM format)",
      "expiry": "string (YYYY-MM-DD)",
      "delta_flow": "string (decimal)",
      "vega_flow": "string (decimal)",
      "timestamp": "string (ISO 8601)"
    }
  ]
}
```

## Error Responses

| Status Code | Description | Response Body |
|-------------|-------------|---------------|
| 400 | Bad Request | `{"error": "Invalid flow_group, expiry, or date format"}` |
| 401 | Unauthorized | `{"error": "Invalid or missing API key"}` |
| 404 | Not Found | `{"error": "No data available for the specified parameters"}` |
| 429 | Too Many Requests | `{"error": "Rate limit exceeded"}` |
| 500 | Internal Server Error | `{"error": "Server error"}` |

## Rate Limiting

Standard API rate limits apply. Monitor the response headers for rate limit information.

## Notes

- Data is provided per minute for the trading day
- Expiry date must be a valid options expiration date
- Market date (optional) must be a trading day
- If no date is provided, the current or most recent market day data is returned
- Delta and vega flows are specific to the expiration date
- This endpoint is more granular than the regular greek-flow endpoint
- Data separated by expiry is useful for analyzing term structure of flows

## Related Endpoints

- [Greek Flow](/docs/group-flow/greek-flow.md) - Get aggregate greek flow data without expiry breakdown

## Validation Results

**Tested**: Yes

**Test Date**: 2025-10-22

**Status**: Working

**Notes**: Endpoint accepts flow_group, expiry, and optional date parameters. Returns minute-level greek flow data by expiration.
