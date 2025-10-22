# ETF Information

## Endpoint Details

**Path**: `GET /api/etfs/{ticker}/info`

**Operation ID**: `PublicApi.EtfController.info`

**Summary**: Information

**Tags**: etfs

## Description

Returns detailed information about a given ETF ticker. This includes fund characteristics, assets under management, trading volume, expense ratios, and other key metrics useful for understanding the ETF's profile.

## Authentication

- **Required**: Yes
- **Type**: API Key
- **Header**: `Authorization: Bearer YOUR_API_KEY`

## Request Parameters

### Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ticker | string | Yes | The ETF ticker symbol (e.g., SPY, QQQ, IWM) |

### Query Parameters

None

### Request Body

Not applicable for this endpoint.

## Example Requests

### cURL

```bash
curl -X GET "https://api.unusualwhales.com/api/etfs/SPY/info" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

### Python

```python
import requests

url = "https://api.unusualwhales.com/api/etfs/SPY/info"
headers = {
    "Authorization": "Bearer YOUR_API_KEY"
}

response = requests.get(url, headers=headers)
data = response.json()
print(data)
```

### JavaScript (Fetch)

```javascript
const url = "https://api.unusualwhales.com/api/etfs/SPY/info";
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
  "data": {
    "name": "string",
    "description": "string",
    "has_options": "boolean",
    "avg30_volume": "string (decimal)",
    "aum": "string (decimal in billions)",
    "opt_vol": "integer",
    "call_vol": "integer",
    "put_vol": "integer",
    "stock_vol": "integer",
    "website": "string (URL)",
    "domicile": "string",
    "etf_company": "string",
    "expense_ratio": "string (decimal)",
    "holdings_count": "integer",
    "inception_date": "string (YYYY-MM-DD)"
  }
}
```

### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| name | string | Full name of the ETF |
| description | string | Detailed description of the ETF's investment objective |
| has_options | boolean | Whether the ETF has listed options |
| avg30_volume | string | 30-day average daily trading volume |
| aum | string | Assets Under Management in billions |
| opt_vol | integer | Total options volume |
| call_vol | integer | Call options volume |
| put_vol | integer | Put options volume |
| stock_vol | integer | Stock trading volume |
| website | string | ETF provider's website URL |
| domicile | string | Country of ETF domicile |
| etf_company | string | ETF provider/issuer name |
| expense_ratio | string | Annual expense ratio as percentage |
| holdings_count | integer | Total number of holdings |
| inception_date | string | Date the ETF was created |

## Example Response

```json
{
  "data": {
    "name": "SPDR S&P 500 ETF Trust",
    "description": "The Trust seeks to achieve its investment objective by holding a portfolio of the common stocks that are included in the index (the \"Portfolio\"), with the weight of each stock in the Portfolio substantially corresponding to the weight of such stock in the index.",
    "has_options": true,
    "avg30_volume": "78403939.227272727273",
    "aum": "671.281922",
    "opt_vol": 10368645,
    "call_vol": 4645362,
    "put_vol": 5723283,
    "stock_vol": 74194787,
    "website": "https://www.ssga.com/us/en/institutional/etfs/funds/spdr-sp-500-etf-trust-spy",
    "domicile": "US",
    "etf_company": "SPDR",
    "expense_ratio": "0.0945",
    "holdings_count": 503,
    "inception_date": "1993-01-22"
  }
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

- AUM is returned in billions of dollars
- Expense ratio is the annual cost to hold the ETF
- The inception_date indicates when the ETF was first created
- Options availability varies by ETF
- Website URLs may redirect to investor relations pages

## Related Endpoints

- [Holdings](/docs/etfs/holdings.md) - Get the list of holdings in the ETF
- [Exposure](/docs/etfs/exposure.md) - Find which ETFs hold a specific stock
- [Weights](/docs/etfs/weights.md) - Get sector and country allocation weights

## Validation Results

**Tested**: Yes

**Test Date**: 2025-10-22

**Status**: Working

**Notes**: Endpoint returns comprehensive ETF information with all expected fields. Successfully tested with SPY ticker. Data includes all metadata, volume statistics, and fund characteristics.
