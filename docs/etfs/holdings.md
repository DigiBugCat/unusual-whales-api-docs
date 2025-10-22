# ETF Holdings

## Endpoint Details

**Path**: `GET /api/etfs/{ticker}/holdings`

**Operation ID**: `PublicApi.EtfController.holdings`

**Summary**: Holdings

**Tags**: etfs

## Description

Returns the holdings of the specified ETF. This endpoint provides detailed information about all stocks and assets held by an ETF, including current prices, weights, volumes, and options data.

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
curl -X GET "https://api.unusualwhales.com/api/etfs/SPY/holdings" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

### Python

```python
import requests

url = "https://api.unusualwhales.com/api/etfs/SPY/holdings"
headers = {
    "Authorization": "Bearer YOUR_API_KEY"
}

response = requests.get(url, headers=headers)
data = response.json()
print(data)
```

### JavaScript (Fetch)

```javascript
const url = "https://api.unusualwhales.com/api/etfs/SPY/holdings";
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
      "close": "string (decimal)",
      "high": "string (decimal)",
      "low": "string (decimal)",
      "name": "string or null",
      "type": "string",
      "ticker": "string",
      "updated": "string (date YYYY-MM-DD)",
      "weight": "string (decimal)",
      "country_code": "string",
      "volume": "string (integer)",
      "sector": "string",
      "etf": "string",
      "put_volume": "integer",
      "call_volume": "integer",
      "put_premium": "string (decimal)",
      "call_premium": "string (decimal)",
      "has_options": "boolean",
      "avg30_volume": "string (decimal)",
      "week52_high": "string (decimal)",
      "week52_low": "string (decimal)",
      "bearish_premium": "string (decimal)",
      "bullish_premium": "string (decimal)",
      "short_name": "string",
      "prev_price": "string (decimal)",
      "country_name": "string",
      "continent": "string",
      "shares": "string (integer)",
      "cusip": "string or null",
      "isin": "string or null"
    }
  ]
}
```

### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| close | string | Current closing price |
| high | string | Day's high price |
| low | string | Day's low price |
| name | string/null | Full company name |
| type | string | Asset type (e.g., 'stock') |
| ticker | string | Stock ticker symbol |
| updated | string | Last update date |
| weight | string | Portfolio weight percentage |
| country_code | string | Country code (e.g., 'US') |
| volume | string | Trading volume |
| sector | string | Industry sector |
| etf | string | Parent ETF ticker |
| put_volume | integer | Put options trading volume |
| call_volume | integer | Call options trading volume |
| put_premium | string | Total put options premium |
| call_premium | string | Total call options premium |
| has_options | boolean | Whether stock has options |
| avg30_volume | string | 30-day average volume |
| week52_high | string | 52-week high price |
| week52_low | string | 52-week low price |
| bearish_premium | string | Bearish options premium |
| bullish_premium | string | Bullish options premium |
| short_name | string | Shortened company name |
| prev_price | string | Previous close price |
| country_name | string | Full country name |
| continent | string | Geographic continent |
| shares | string | Number of shares held |
| cusip | string/null | CUSIP identifier |
| isin | string/null | ISIN identifier |

## Example Response

```json
{
  "data": [
    {
      "close": "180.28",
      "high": "183.44",
      "low": "176.76",
      "name": null,
      "type": "stock",
      "ticker": "NVDA",
      "updated": "2025-10-20",
      "weight": "7.753154",
      "country_code": "US",
      "volume": "161400996",
      "sector": "Technology",
      "etf": "SPY",
      "put_volume": 759109,
      "call_volume": 1469771,
      "put_premium": "292760850.00",
      "call_premium": "584262177.00",
      "has_options": true,
      "avg30_volume": "176506264.86363636",
      "week52_high": "195.62",
      "week52_low": "86.62",
      "bearish_premium": "372292302.00",
      "bullish_premium": "352513806.00",
      "short_name": "NVIDIA",
      "prev_price": "181.16",
      "country_name": "UNITED STATES",
      "continent": "North America",
      "shares": "289344903",
      "cusip": null,
      "isin": null
    },
    {
      "close": "520.54",
      "high": "525.23",
      "low": "517.71",
      "name": null,
      "type": "stock",
      "ticker": "MSFT",
      "updated": "2025-10-20",
      "weight": "6.683123",
      "country_code": "US",
      "volume": "18170777",
      "sector": "Technology",
      "etf": "SPY",
      "put_volume": 106959,
      "call_volume": 203182,
      "put_premium": "54101087.00",
      "call_premium": "159868473.0000",
      "has_options": true,
      "avg30_volume": "17401944.227272727273",
      "week52_high": "555.45",
      "week52_low": "344.79",
      "bearish_premium": "92518552.0000",
      "bullish_premium": "102087243.0000",
      "short_name": "MICROSOFT",
      "prev_price": "517.66",
      "country_name": "UNITED STATES",
      "continent": "North America",
      "shares": "88145205",
      "cusip": null,
      "isin": null
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

- Returns the complete list of ETF holdings
- Data is updated daily after market close
- For broad-based ETFs like SPY, the response can contain 500+ items
- Options data is included for holdings that have options
- Numeric values are returned as strings to preserve precision
- Country code may be null for some international assets

## Related Endpoints

- [Exposure](/docs/etfs/exposure.md) - Find which ETFs hold a specific stock
- [Info](/docs/etfs/info.md) - Get general information about an ETF
- [Weights](/docs/etfs/weights.md) - Get sector and country weights

## Validation Results

**Tested**: Yes

**Test Date**: 2025-10-22

**Status**: Working

**Notes**: Endpoint returns comprehensive holdings data with 500+ items for SPY. All numeric fields return valid data. Successfully tested and data matches expected ETF composition.
