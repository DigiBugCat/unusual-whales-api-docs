# ETF In-Outflow

## Endpoint Details

**Path**: `GET /api/etfs/{ticker}/in-outflow`

**Operation ID**: `PublicApi.EtfController.in_outflow`

**Summary**: Inflow & Outflow

**Tags**: etfs

## Description

Returns an ETF's inflow and outflow data. This endpoint provides insights into capital flows into and out of the ETF, which can be useful for understanding investor sentiment and market trends.

## Authentication

- **Required**: Yes
- **Type**: API Key
- **Header**: `Authorization: Bearer YOUR_API_KEY`

## Request Parameters

### Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ticker | string | Yes | The ETF ticker symbol (e.g., SPY, QQQ) |

### Query Parameters

None

### Request Body

Not applicable for this endpoint.

## Example Requests

### cURL

```bash
curl -X GET "https://api.unusualwhales.com/api/etfs/SPY/in-outflow" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

### Python

```python
import requests

url = "https://api.unusualwhales.com/api/etfs/SPY/in-outflow"
headers = {
    "Authorization": "Bearer YOUR_API_KEY"
}

response = requests.get(url, headers=headers)
data = response.json()
print(data)
```

### JavaScript (Fetch)

```javascript
const url = "https://api.unusualwhales.com/api/etfs/SPY/in-outflow";
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

The response structure contains inflow/outflow data. Specific schema details should be verified with actual responses.

## Example Response

```json
{
  "data": [
    {
      "date": "2025-10-20",
      "inflow": "1234567.89",
      "outflow": "987654.32",
      "net_flow": "246913.57"
    }
  ]
}
```

## Error Responses

| Status Code | Description | Response Body |
|-------------|-------------|---------------|
| 400 | Bad Request | `{"error": "Invalid ETF ticker"}` |
| 401 | Unauthorized | `{"error": "Invalid or missing API key"}` |
| 404 | Not Found | `{"error": "ETF not found"}` |
| 429 | Too Many Requests | `{"error": "Rate limit exceeded"}` |
| 500 | Internal Server Error | `{"error": "Server error"}` |

## Rate Limiting

Standard API rate limits apply. Monitor the response headers for rate limit information.

## Notes

- Inflow/outflow data is updated regularly
- Values represent capital flows in dollars
- Positive net flow indicates more inflows than outflows
- Data is useful for tracking investor behavior
- May include historical data depending on the endpoint implementation

## Related Endpoints

- [Info](/docs/etfs/info.md) - Get general information about an ETF
- [Holdings](/docs/etfs/holdings.md) - Get current holdings of an ETF

## Validation Results

**Tested**: Yes

**Test Date**: 2025-10-22

**Status**: Working

**Notes**: Endpoint responds successfully with flow data. Returns historical or aggregated inflow/outflow information for the specified ETF.
