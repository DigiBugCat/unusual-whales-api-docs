# Institutional Sector Exposure

## Endpoint Details

**Path**: `GET /api/institution/{name}/sectors`

**Operation ID**: `PublicApi.InstitutionController.sectors`

**Summary**: Sector Exposure

**Tags**: institution

## Description

Returns the sector exposure for a given institution. This endpoint shows how an institutional investor's portfolio is allocated across different industry sectors, providing insights into their investment strategy and thematic focus.

## Authentication

- **Required**: Yes
- **Type**: API Key
- **Header**: `Authorization: Bearer YOUR_API_KEY`

## Request Parameters

### Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| name | string | Yes | The institution name (e.g., Vanguard, BlackRock) |

### Query Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| limit | integer | No | 50 | Maximum number of sectors |
| offset | integer | No | 0 | Pagination offset |

### Request Body

Not applicable for this endpoint.

## Example Requests

### cURL

```bash
curl -X GET "https://api.unusualwhales.com/api/institution/Vanguard/sectors" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

### Python

```python
import requests

url = "https://api.unusualwhales.com/api/institution/Vanguard/sectors"
headers = {
    "Authorization": "Bearer YOUR_API_KEY"
}

response = requests.get(url, headers=headers)
data = response.json()
print(data)
```

### JavaScript (Fetch)

```javascript
const url = "https://api.unusualwhales.com/api/institution/Vanguard/sectors";
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

The response contains sector allocation data with weights and values.

```json
{
  "data": [
    {
      "sector": "string",
      "weight": "string (decimal)",
      "value": "string (decimal)",
      "holding_count": "integer"
    }
  ]
}
```

### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| sector | string | Sector name |
| weight | string | Percentage allocation in portfolio |
| value | string | Total value of sector holdings |
| holding_count | integer | Number of individual holdings in sector |

## Example Response

```json
{
  "data": [
    {
      "sector": "Technology",
      "weight": "28.45",
      "value": "1756234567.89",
      "holding_count": 245
    },
    {
      "sector": "Healthcare",
      "weight": "15.32",
      "value": "945678901.23",
      "holding_count": 182
    },
    {
      "sector": "Finance",
      "weight": "14.78",
      "value": "912345678.90",
      "holding_count": 156
    }
  ]
}
```

## Error Responses

| Status Code | Description | Response Body |
|-------------|-------------|---------------|
| 400 | Bad Request | `{"error": "Invalid query parameters"}` |
| 401 | Unauthorized | `{"error": "Invalid or missing API key"}` |
| 404 | Not Found | `{"error": "Institution not found"}` |
| 429 | Too Many Requests | `{"error": "Rate limit exceeded"}` |
| 500 | Internal Server Error | `{"error": "Server error"}` |

## Rate Limiting

Standard API rate limits apply. Monitor the response headers for rate limit information.

## Notes

- Sector allocations sum to approximately 100%
- Weights represent percentage of total portfolio value
- Data is sourced from the most recent 13F filing
- Different institutions may have different sector allocations reflecting their strategies
- Some sectors may have zero or minimal allocation
- Sector definitions follow standard market classification systems

## Related Endpoints

- [Holdings](/docs/institution/holdings.md) - Get detailed list of holdings
- [Activity](/docs/institution/activity.md) - Get recent trading activity
- [List](/docs/institutions/list.md) - Get list of all institutions

## Validation Results

**Tested**: Yes

**Test Date**: 2025-10-22

**Status**: Working

**Notes**: Endpoint successfully returns sector allocation data for institutions.
