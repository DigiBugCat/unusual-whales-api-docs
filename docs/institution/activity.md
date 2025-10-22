# Institutional Activity

## Endpoint Details

**Path**: `GET /api/institution/{name}/activity`

**Operation ID**: `PublicApi.InstitutionController.activity`

**Summary**: Institutional Activity

**Tags**: institution

## Description

Returns the trading activities for a given institution. This endpoint provides insights into the recent buying and selling activity of large institutional investors, which can indicate market trends and institutional sentiment.

## Authentication

- **Required**: Yes
- **Type**: API Key
- **Header**: `Authorization: Bearer YOUR_API_KEY`

## Request Parameters

### Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| name | string | Yes | The institution name or identifier (e.g., Vanguard, BlackRock) |

### Query Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| limit | integer | No | 50 | Maximum number of records to return |
| offset | integer | No | 0 | Pagination offset |
| date_from | string | No | - | Filter from date (YYYY-MM-DD) |
| date_to | string | No | - | Filter to date (YYYY-MM-DD) |

### Request Body

Not applicable for this endpoint.

## Example Requests

### cURL

```bash
curl -X GET "https://api.unusualwhales.com/api/institution/Vanguard/activity?limit=10" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

### Python

```python
import requests

url = "https://api.unusualwhales.com/api/institution/Vanguard/activity"
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
const url = "https://api.unusualwhales.com/api/institution/Vanguard/activity?limit=10";
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

The response contains institutional activity data with trading information.

```json
{
  "data": [
    {
      "ticker": "string",
      "activity_type": "string (BUY or SELL)",
      "amount": "string (decimal)",
      "date": "string (YYYY-MM-DD)",
      "filing_date": "string (YYYY-MM-DD)",
      "shares": "integer",
      "value": "string (decimal)"
    }
  ]
}
```

## Error Responses

| Status Code | Description | Response Body |
|-------------|-------------|---------------|
| 400 | Bad Request | `{"error": "Invalid institution name"}` |
| 401 | Unauthorized | `{"error": "Invalid or missing API key"}` |
| 404 | Not Found | `{"error": "Institution not found"}` |
| 429 | Too Many Requests | `{"error": "Rate limit exceeded"}` |
| 500 | Internal Server Error | `{"error": "Server error"}` |

## Rate Limiting

Standard API rate limits apply. Monitor the response headers for rate limit information.

## Notes

- Institution names should match official names in the database
- Activity is sourced from 13F filings and other regulatory documents
- Data represents significant changes in holdings
- Pagination is recommended for large result sets
- Multiple institutions may have similar names; use exact names for clarity

## Related Endpoints

- [Holdings](/docs/institution/holdings.md) - Get current holdings for an institution
- [Sectors](/docs/institution/sectors.md) - Get sector exposure for an institution
- [List](/docs/institutions/list.md) - Get list of all institutions

## Validation Results

**Tested**: Yes

**Test Date**: 2025-10-22

**Status**: Working

**Notes**: Endpoint accepts institution name and returns trading activity data.
