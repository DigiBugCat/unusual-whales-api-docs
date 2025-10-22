# Institutional Holdings

## Endpoint Details

**Path**: `GET /api/institution/{name}/holdings`

**Operation ID**: `PublicApi.InstitutionController.holdings`

**Summary**: Institutional Holdings

**Tags**: institution

## Description

Returns the holdings for a given institution. This endpoint provides a comprehensive view of the current portfolio positions held by a large institutional investor, including sectors, asset classes, and individual securities.

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
| limit | integer | No | 100 | Maximum number of holdings to return |
| offset | integer | No | 0 | Pagination offset |
| sector | string | No | - | Filter by sector |
| asset_type | string | No | - | Filter by asset type (stock, fund, etc.) |

### Request Body

Not applicable for this endpoint.

## Example Requests

### cURL

```bash
curl -X GET "https://api.unusualwhales.com/api/institution/Vanguard/holdings?limit=20" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

### Python

```python
import requests

url = "https://api.unusualwhales.com/api/institution/Vanguard/holdings"
headers = {
    "Authorization": "Bearer YOUR_API_KEY"
}
params = {
    "limit": 20,
    "asset_type": "stock"
}

response = requests.get(url, headers=headers, params=params)
data = response.json()
print(data)
```

### JavaScript (Fetch)

```javascript
const url = "https://api.unusualwhales.com/api/institution/Vanguard/holdings?limit=20";
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

The response contains detailed holdings information including quantities, values, and asset types.

```json
{
  "data": [
    {
      "ticker": "string",
      "name": "string",
      "shares": "integer",
      "value": "string (decimal)",
      "sector": "string",
      "asset_type": "string",
      "weight": "string (decimal)",
      "filing_date": "string (YYYY-MM-DD)"
    }
  ]
}
```

### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| ticker | string | Security ticker symbol |
| name | string | Security name |
| shares | integer | Number of shares held |
| value | string | Total value of position |
| sector | string | Industry sector |
| asset_type | string | Type of asset (stock, ETF, bond, etc.) |
| weight | string | Percentage weight in portfolio |
| filing_date | string | Date of the filing |

## Example Response

```json
{
  "data": [
    {
      "ticker": "AAPL",
      "name": "Apple Inc.",
      "shares": 1234567,
      "value": "456789012.34",
      "sector": "Technology",
      "asset_type": "stock",
      "weight": "7.45",
      "filing_date": "2025-08-11"
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

- Holdings represent current positions from the most recent filing
- Large institutions may hold thousands of positions
- Weights are calculated as percentage of total portfolio
- Data is sourced from 13F filings (quarterly)
- Pagination is recommended for large result sets
- Some positions may be very small and shown with minimal weight

## Related Endpoints

- [Activity](/docs/institution/activity.md) - Get recent trading activity
- [Sectors](/docs/institution/sectors.md) - Get sector allocation
- [Ownership](/docs/institution/ownership.md) - Get institutional ownership of a specific ticker
- [List](/docs/institutions/list.md) - Get list of all institutions

## Validation Results

**Tested**: Yes

**Test Date**: 2025-10-22

**Status**: Working

**Notes**: Endpoint successfully returns institutional holdings data with complete position information.
