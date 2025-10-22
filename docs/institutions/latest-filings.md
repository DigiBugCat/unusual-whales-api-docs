# Latest Filings

## Endpoint Details

**Path**: `GET /api/institutions/latest_filings`

**Operation ID**: `PublicApi.InstitutionController.latest_filings`

**Summary**: Latest Filings

**Tags**: institutions

## Description

Returns the latest institutional filings. This endpoint provides recent SEC Form 13F filings from institutional investors, allowing you to track the most recent portfolio changes and institutional activity across the market.

## Authentication

- **Required**: Yes
- **Type**: API Key
- **Header**: `Authorization: Bearer YOUR_API_KEY`

## Request Parameters

### Path Parameters

None

### Query Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| limit | integer | No | 50 | Maximum number of filings to return |
| offset | integer | No | 0 | Pagination offset |
| date_from | string | No | - | Filter from date (YYYY-MM-DD) |
| date_to | string | No | - | Filter to date (YYYY-MM-DD) |
| is_hedge_fund | boolean | No | - | Filter by hedge fund status |

### Request Body

Not applicable for this endpoint.

## Example Requests

### cURL

```bash
curl -X GET "https://api.unusualwhales.com/api/institutions/latest_filings?limit=20" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

### Python

```python
import requests

url = "https://api.unusualwhales.com/api/institutions/latest_filings"
headers = {
    "Authorization": "Bearer YOUR_API_KEY"
}
params = {
    "limit": 20
}

response = requests.get(url, headers=headers, params=params)
data = response.json()
print(data)
```

### JavaScript (Fetch)

```javascript
const url = "https://api.unusualwhales.com/api/institutions/latest_filings?limit=20";
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
  "data": [
    {
      "name": "string",
      "cik": "string",
      "filing_date": "string (YYYY-MM-DD)",
      "short_name": "string",
      "is_hedge_fund": "boolean",
      "tags": ["string"],
      "people": ["string"]
    }
  ]
}
```

### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| name | string | Full institution name |
| cik | string | SEC Central Index Key |
| filing_date | string | Date the filing was submitted |
| short_name | string | Abbreviated institution name |
| is_hedge_fund | boolean | Whether classified as hedge fund |
| tags | array | Tags associated with the institution |
| people | array | Names of key people associated |

## Example Response

```json
{
  "data": [
    {
      "name": "4J WEALTH MANAGEMENT LLC",
      "cik": "0001840775",
      "filing_date": "2025-10-22",
      "short_name": "4j Wealth",
      "is_hedge_fund": false,
      "tags": [],
      "people": []
    },
    {
      "name": "ABACUS PLANNING GROUP, INC.",
      "cik": "0001602730",
      "filing_date": "2025-10-22",
      "short_name": "Abacus Planning",
      "is_hedge_fund": false,
      "tags": [],
      "people": []
    },
    {
      "name": "ABUNDANCE WEALTH COUNSELORS",
      "cik": "0001767080",
      "filing_date": "2025-10-22",
      "short_name": "Abundance Wealth Counselors",
      "is_hedge_fund": true,
      "tags": ["hedge_fund"],
      "people": []
    }
  ]
}
```

## Error Responses

| Status Code | Description | Response Body |
|-------------|-------------|---------------|
| 400 | Bad Request | `{"error": "Invalid query parameters"}` |
| 401 | Unauthorized | `{"error": "Invalid or missing API key"}` |
| 429 | Too Many Requests | `{"error": "Rate limit exceeded"}` |
| 500 | Internal Server Error | `{"error": "Server error"}` |

## Rate Limiting

Standard API rate limits apply. Monitor the response headers for rate limit information.

## Notes

- Returns Form 13F filings which are filed quarterly (typically within 45 days of quarter end)
- Filings represent portfolio positions as of the report date
- Hedge funds, asset managers, and other institutional investors file these reports
- CIK can be used to look up more details on SEC Edgar
- Tags indicate special classifications (hedge_fund, etc.)
- Latest filings appear first in the list
- Some institutions may file multiple times if they manage multiple funds

## Related Endpoints

- [List](/docs/institutions/list.md) - Get list of all institutions
- [Holdings](/docs/institution/holdings.md) - Get holdings for a specific institution
- [Activity](/docs/institution/activity.md) - Get activity for a specific institution

## Validation Results

**Tested**: Yes

**Test Date**: 2025-10-22

**Status**: Working

**Notes**: Endpoint returns the latest institutional 13F filings. Successfully tested returning recent filings from 2025-10-22 with complete institution information and filing metadata.
