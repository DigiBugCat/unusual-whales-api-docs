# Institutional Ownership

## Endpoint Details

**Path**: `GET /api/institution/{ticker}/ownership`

**Operation ID**: `PublicApi.InstitutionController.ownership`

**Summary**: Institutional Ownership

**Tags**: institution

## Description

Returns the institutional ownership of a given ticker. This endpoint shows which major institutions hold positions in a specific stock, their ownership percentages, and changes in their positions over time.

## Authentication

- **Required**: Yes
- **Type**: API Key
- **Header**: `Authorization: Bearer YOUR_API_KEY`

## Request Parameters

### Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ticker | string | Yes | The stock ticker symbol (e.g., AAPL, MSFT) |

### Query Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| limit | integer | No | 100 | Maximum number of institutions to return |
| offset | integer | No | 0 | Pagination offset |
| min_value | string | No | - | Filter institutions with minimum value |
| sort_by | string | No | value | Sort field (value, units, change) |

### Request Body

Not applicable for this endpoint.

## Example Requests

### cURL

```bash
curl -X GET "https://api.unusualwhales.com/api/institution/AAPL/ownership?limit=10" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

### Python

```python
import requests

url = "https://api.unusualwhales.com/api/institution/AAPL/ownership"
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
const url = "https://api.unusualwhales.com/api/institution/AAPL/ownership?limit=10";
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
      "value": "integer",
      "units": "integer",
      "filing_date": "string (YYYY-MM-DD)",
      "short_name": "string",
      "units_changed": "integer",
      "first_buy": "string (YYYY-MM-DD)",
      "inst_share_value": "string (decimal)",
      "inst_value": "string (decimal)",
      "historical_units": ["integer"],
      "report_date": "string (YYYY-MM-DD)"
    }
  ]
}
```

### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| name | string | Institution name |
| value | integer | Current value of position |
| units | integer | Number of shares held |
| filing_date | string | Date of the filing |
| short_name | string | Short name or abbreviation |
| units_changed | integer | Change in units from previous filing |
| first_buy | string | Date of first purchase |
| inst_share_value | string | Total institutional share value |
| inst_value | string | Total institutional value |
| historical_units | array | Array of historical unit counts |
| report_date | string | Report date |

## Example Response

```json
{
  "data": [
    {
      "name": "VANGUARD GROUP INC",
      "value": 290506933377,
      "units": 1415932804,
      "filing_date": "2025-08-11",
      "short_name": "Vanguard",
      "units_changed": 15141995,
      "first_buy": "2013-12-31",
      "inst_share_value": "6111134010813",
      "inst_value": "6178129573955",
      "historical_units": [1415932804, 1400790809, 1395785512, 1346616669],
      "report_date": "2025-06-30"
    },
    {
      "name": "BLACKROCK, INC.",
      "value": 235707295634,
      "units": 1148838990,
      "filing_date": "2025-08-12",
      "short_name": null,
      "units_changed": 8636120,
      "first_buy": "2024-09-30",
      "inst_share_value": "5065796818106",
      "inst_value": "5253068841298",
      "historical_units": [1148838990, 1140202870, 1123417607, 1093618174],
      "report_date": "2025-06-30"
    }
  ]
}
```

## Error Responses

| Status Code | Description | Response Body |
|-------------|-------------|---------------|
| 400 | Bad Request | `{"error": "Invalid ticker symbol"}` |
| 401 | Unauthorized | `{"error": "Invalid or missing API key"}` |
| 404 | Not Found | `{"error": "No institutional ownership data"}` |
| 429 | Too Many Requests | `{"error": "Rate limit exceeded"}` |
| 500 | Internal Server Error | `{"error": "Server error"}` |

## Rate Limiting

Standard API rate limits apply. Monitor the response headers for rate limit information.

## Notes

- Data is sourced from 13F filings (quarterly)
- Historical units track position changes over time
- Large institutions are listed first by default
- Some ownership data may be estimated or delayed
- Units changed indicates buying or selling in most recent period
- First buy date shows when the institution first acquired shares

## Related Endpoints

- [Holdings](/docs/institution/holdings.md) - Get all holdings for an institution
- [Activity](/docs/institution/activity.md) - Get trading activity for an institution
- [List](/docs/institutions/list.md) - Get list of all institutions

## Validation Results

**Tested**: Yes

**Test Date**: 2025-10-22

**Status**: Working

**Notes**: Endpoint returns comprehensive institutional ownership data including position values, historical changes, and filing information for major institutional investors.
