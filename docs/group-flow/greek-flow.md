# Greek Flow

## Endpoint Details

**Path**: `GET /api/group-flow/{flow_group}/greek-flow`

**Operation ID**: `PublicApi.GroupFlowController.greek_flow`

**Summary**: Greek flow

**Tags**: group-flow

## Description

Returns the group flow's greek flow (delta & vega flow) for the given market day broken down per minute. Date must be the current or a past date. If no date is given, returns data for the current/last market day. This endpoint is useful for analyzing options Greeks flow across different time periods.

## Authentication

- **Required**: Yes
- **Type**: API Key
- **Header**: `Authorization: Bearer YOUR_API_KEY`

## Request Parameters

### Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| flow_group | string | Yes | The flow group identifier (e.g., call_oi_1dte, put_oi_1dte) |

### Query Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| date | string | No | current/last date | The market date to retrieve data for (YYYY-MM-DD format) |

### Request Body

Not applicable for this endpoint.

## Example Requests

### cURL

```bash
curl -X GET "https://api.unusualwhales.com/api/group-flow/call_oi_1dte/greek-flow?date=2025-10-22" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

### Python

```python
import requests

url = "https://api.unusualwhales.com/api/group-flow/call_oi_1dte/greek-flow"
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
const url = "https://api.unusualwhales.com/api/group-flow/call_oi_1dte/greek-flow?date=2025-10-22";
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

The response contains greek flow data broken down per minute with delta and vega information.

```json
{
  "data": [
    {
      "time": "string (HH:MM format)",
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
| 400 | Bad Request | `{"error": "Invalid flow_group or date format"}` |
| 401 | Unauthorized | `{"error": "Invalid or missing API key"}` |
| 404 | Not Found | `{"error": "No data available for the specified date"}` |
| 429 | Too Many Requests | `{"error": "Rate limit exceeded"}` |
| 500 | Internal Server Error | `{"error": "Server error"}` |

## Rate Limiting

Standard API rate limits apply. Monitor the response headers for rate limit information.

## Notes

- Data is provided per minute for the trading day
- Date must be a trading day
- Delta and vega flows are cumulative metrics
- If no date is provided, the current or most recent market day data is returned
- Data may not be available immediately after market close
- Different flow_group values provide data for different option categories

## Related Endpoints

- [Greek Flow by Expiry](/docs/group-flow/greek-flow-expiry.md) - Get greek flow data broken down by expiration date

## Validation Results

**Tested**: Yes

**Test Date**: 2025-10-22

**Status**: Working

**Notes**: Endpoint accepts flow_group and date parameters. Returns minute-level greek flow data.
