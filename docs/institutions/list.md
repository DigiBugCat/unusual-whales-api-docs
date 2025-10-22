# List of Institutions

## Endpoint Details

**Path**: `GET /api/institutions`

**Operation ID**: `PublicApi.InstitutionController.list`

**Summary**: List of Institutions

**Tags**: institutions

## Description

Returns a list of institutions. This endpoint provides a comprehensive directory of major institutional investors tracked by the platform, including asset managers, hedge funds, and other large investment firms. Useful for discovering which institutions are available for detailed analysis.

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
| limit | integer | No | 100 | Maximum number of institutions to return |
| offset | integer | No | 0 | Pagination offset |
| search | string | No | - | Search for institutions by name |
| is_hedge_fund | boolean | No | - | Filter by hedge fund status |
| min_value | string | No | - | Minimum portfolio value filter |
| sort_by | string | No | total_value | Sort field (name, total_value, etc.) |

### Request Body

Not applicable for this endpoint.

## Example Requests

### cURL

```bash
curl -X GET "https://api.unusualwhales.com/api/institutions?limit=20" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

### Python

```python
import requests

url = "https://api.unusualwhales.com/api/institutions"
headers = {
    "Authorization": "Bearer YOUR_API_KEY"
}
params = {
    "limit": 20,
    "sort_by": "total_value"
}

response = requests.get(url, headers=headers, params=params)
data = response.json()
print(data)
```

### JavaScript (Fetch)

```javascript
const url = "https://api.unusualwhales.com/api/institutions?limit=20";
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
      "date": "string (YYYY-MM-DD)",
      "cik": "string",
      "filing_date": "string (YYYY-MM-DD)",
      "short_name": "string",
      "is_hedge_fund": "boolean",
      "total_value": "string (decimal)",
      "share_value": "string (decimal)",
      "call_value": "string (decimal)",
      "put_value": "string (decimal)",
      "warrant_value": "string (decimal)",
      "pfd_value": "string (decimal)",
      "debt_value": "string (decimal)",
      "buy_value": "string (decimal)",
      "sell_value": "string (decimal)"
    }
  ]
}
```

### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| name | string | Full institution name |
| date | string | Report date |
| cik | string | SEC CIK identifier |
| filing_date | string | Date of the filing |
| short_name | string | Short or abbreviated name |
| is_hedge_fund | boolean | Whether classified as hedge fund |
| total_value | string | Total portfolio value |
| share_value | string | Value of equity holdings |
| call_value | string | Value of call options |
| put_value | string | Value of put options |
| warrant_value | string | Value of warrants |
| pfd_value | string | Value of preferred stock |
| debt_value | string | Value of debt holdings |
| buy_value | string | Total value of recent buys |
| sell_value | string | Total value of recent sells |

## Example Response

```json
{
  "data": [
    {
      "name": "VANGUARD GROUP INC",
      "date": "2025-06-30",
      "cik": "0000102909",
      "filing_date": "2025-08-11",
      "short_name": "Vanguard",
      "is_hedge_fund": false,
      "total_value": "6178129573955",
      "share_value": "6111134010813",
      "call_value": "0",
      "put_value": "0",
      "warrant_value": "895870",
      "pfd_value": "246661461",
      "debt_value": "0",
      "buy_value": "125595584057.19",
      "sell_value": "-30864777431.95"
    },
    {
      "name": "BLACKROCK, INC.",
      "date": "2025-06-30",
      "cik": "0002012383",
      "filing_date": "2025-08-12",
      "short_name": null,
      "is_hedge_fund": false,
      "total_value": "5253068841298",
      "share_value": "5065796818106",
      "call_value": "25367224442",
      "put_value": "2076244021",
      "warrant_value": "1497746",
      "pfd_value": "3081493409",
      "debt_value": "3286287612",
      "buy_value": "103208810541.70",
      "sell_value": "-88576910145.81"
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

- List includes asset managers, hedge funds, pension funds, and other large investors
- Institutions are ranked by total portfolio value by default
- Data is sourced from 13F filings
- Pagination is recommended for exploring the full list
- Search functionality allows finding specific institutions by name
- Short names may be null for some institutions

## Related Endpoints

- [Activity](/docs/institution/activity.md) - Get trading activity for an institution
- [Holdings](/docs/institution/holdings.md) - Get holdings for an institution
- [Latest Filings](/docs/institutions/latest-filings.md) - Get recent institution filings

## Validation Results

**Tested**: Yes

**Test Date**: 2025-10-22

**Status**: Working

**Notes**: Endpoint successfully returns paginated list of institutions with comprehensive portfolio data. Tested with default parameters returning top 100+ institutions by total value.
