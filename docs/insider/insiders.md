# Insiders

## Endpoint Details

**Path**: `GET /api/insider/{ticker}`

**Operation ID**: `PublicApi.InsiderController.insiders`

**Summary**: Insiders

**Tags**: insider

## Description

Returns all insiders for the given ticker. This endpoint provides information about all company officers, directors, and significant shareholders who file insider trading reports with the SEC.

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

None

### Request Body

Not applicable for this endpoint.

## Example Requests

### cURL

```bash
curl -X GET "https://api.unusualwhales.com/api/insider/AAPL" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

### Python

```python
import requests

url = "https://api.unusualwhales.com/api/insider/AAPL"
headers = {
    "Authorization": "Bearer YOUR_API_KEY"
}

response = requests.get(url, headers=headers)
data = response.json()
print(data)
```

### JavaScript (Fetch)

```javascript
const url = "https://api.unusualwhales.com/api/insider/AAPL";
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
      "id": "integer",
      "name": "string",
      "ticker": "string",
      "display_name": "string",
      "name_slug": "string",
      "logo_url": "string or null",
      "social_links": "array",
      "is_person": "boolean"
    }
  ]
}
```

### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| id | integer | Unique insider identifier |
| name | string | Name of the insider |
| ticker | string | Stock ticker symbol |
| display_name | string | Formatted name for display |
| name_slug | string | URL-friendly slug of the name |
| logo_url | string/null | URL to logo image if available |
| social_links | array | Array of social media links |
| is_person | boolean | Whether the insider is a person (vs. entity) |

## Example Response

```json
{
  "data": [
    {
      "id": 79310,
      "name": "IGER ROBERT A",
      "ticker": "AAPL",
      "display_name": "IGER ROBERT A",
      "name_slug": "iger-robert-a",
      "logo_url": "https://storage.googleapis.com/uwassets/insiders/965",
      "social_links": [],
      "is_person": true
    },
    {
      "id": 167541,
      "name": "COOK TIMOTHY",
      "ticker": "AAPL",
      "display_name": "COOK TIMOTHY",
      "name_slug": "cook-timothy",
      "logo_url": null,
      "social_links": [],
      "is_person": true
    },
    {
      "id": 167550,
      "name": "ADAMS KATHERINE",
      "ticker": "AAPL",
      "display_name": "ADAMS KATHERINE",
      "name_slug": "adams-katherine",
      "logo_url": null,
      "social_links": [],
      "is_person": true
    }
  ]
}
```

## Error Responses

| Status Code | Description | Response Body |
|-------------|-------------|---------------|
| 400 | Bad Request | `{"error": "Invalid ticker symbol"}` |
| 401 | Unauthorized | `{"error": "Invalid or missing API key"}` |
| 404 | Not Found | `{"error": "No insiders found for ticker"}` |
| 429 | Too Many Requests | `{"error": "Rate limit exceeded"}` |
| 500 | Internal Server Error | `{"error": "Server error"}` |

## Rate Limiting

Standard API rate limits apply. Monitor the response headers for rate limit information.

## Notes

- Returns all registered insiders who have filed Form 4 or Form 5 with the SEC
- Insiders include officers, directors, and 10% shareholders
- Name slug can be used to construct URLs or unique identifiers
- Logo URLs may be null if not available
- Social links array may be empty for many insiders
- Large-cap companies typically have more insiders listed

## Related Endpoints

- [Transactions](/docs/insider/transactions.md) - Get all recent insider transactions
- [Ticker Flow](/docs/insider/ticker-flow.md) - Get aggregated insider flow for a ticker
- [Sector Flow](/docs/insider/sector-flow.md) - Get aggregated insider flow for a sector

## Validation Results

**Tested**: Yes

**Test Date**: 2025-10-22

**Status**: Working

**Notes**: Endpoint returns comprehensive list of insiders for the specified ticker. Successfully tested with AAPL returning 25+ insiders including officers, directors, and shareholders.
