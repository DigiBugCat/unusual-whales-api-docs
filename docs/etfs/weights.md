# ETF Sector & Country Weights

## Endpoint Details

**Path**: `GET /api/etfs/{ticker}/weights`

**Operation ID**: `PublicApi.EtfController.weights`

**Summary**: Sector & Country weights

**Tags**: etfs

## Description

Returns the sector and country weights for a given ETF ticker. This endpoint provides the allocation breakdown by industry sector and geographic country, showing how the ETF's assets are distributed across these dimensions.

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
curl -X GET "https://api.unusualwhales.com/api/etfs/SPY/weights" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

### Python

```python
import requests

url = "https://api.unusualwhales.com/api/etfs/SPY/weights"
headers = {
    "Authorization": "Bearer YOUR_API_KEY"
}

response = requests.get(url, headers=headers)
data = response.json()
print(data)
```

### JavaScript (Fetch)

```javascript
const url = "https://api.unusualwhales.com/api/etfs/SPY/weights";
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

```json
{
  "country": [
    {
      "country": "string",
      "weight": "string (decimal)"
    }
  ],
  "sector": [
    {
      "sector": "string",
      "weight": "string (decimal)"
    }
  ]
}
```

### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| country | array | Array of country allocations |
| country[].country | string | Country name |
| country[].weight | string | Weight as decimal percentage |
| sector | array | Array of sector allocations |
| sector[].sector | string | Sector or industry name |
| sector[].weight | string | Weight as decimal percentage |

## Example Response

```json
{
  "country": [
    {
      "country": "Bermuda",
      "weight": "0.0012"
    },
    {
      "country": "Canada",
      "weight": "0.0009"
    },
    {
      "country": "Ireland",
      "weight": "0.0004"
    },
    {
      "country": "United Kingdom",
      "weight": "0.001"
    },
    {
      "country": "United States",
      "weight": "0.9937"
    }
  ],
  "sector": [
    {
      "weight": "0.0094867",
      "sector": "Distribution Services"
    },
    {
      "weight": "0.0966",
      "sector": "Health Technology"
    },
    {
      "weight": "0.0358",
      "sector": "Energy"
    },
    {
      "weight": "0.1228",
      "sector": "Finance"
    },
    {
      "weight": "0.0225",
      "sector": "Health Services"
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

- Weights are returned as decimal values (0.5 = 50%)
- Country allocation shows geographic diversification
- Sector allocation shows industry concentration
- Weights should sum to approximately 1.0 (100%)
- Some ETFs may have "Other" categories for uncategorized allocations
- Country codes like "Bermuda" indicate headquarters/domicile of holdings, not necessarily trading country

## Related Endpoints

- [Info](/docs/etfs/info.md) - Get general ETF information
- [Holdings](/docs/etfs/holdings.md) - Get detailed list of holdings with individual weights

## Validation Results

**Tested**: Yes

**Test Date**: 2025-10-22

**Status**: Working

**Notes**: Endpoint returns sector and country allocation data with proper structure. For SPY, returns all major sectors and countries. United States has 99.37% allocation as expected for a US equity ETF.
