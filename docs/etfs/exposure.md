# ETF Exposure

## Endpoint Details

**Path**: `GET /api/etfs/{ticker}/exposure`

**Operation ID**: `PublicApi.EtfController.exposure`

**Summary**: Exposure

**Tags**: etfs

## Description

Returns all ETFs in which the given ticker is a holding. This endpoint helps identify which ETFs contain a specific stock, useful for understanding portfolio overlap and market exposure.

## Authentication

- **Required**: Yes
- **Type**: API Key
- **Header**: `Authorization: Bearer YOUR_API_KEY`

## Request Parameters

### Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ticker | string | Yes | The stock ticker symbol to find ETF exposure for (e.g., SPY, AAPL) |

### Query Parameters

None

### Request Body

Not applicable for this endpoint.

## Example Requests

### cURL

```bash
curl -X GET "https://api.unusualwhales.com/api/etfs/SPY/exposure" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

### Python

```python
import requests

url = "https://api.unusualwhales.com/api/etfs/SPY/exposure"
headers = {
    "Authorization": "Bearer YOUR_API_KEY"
}

response = requests.get(url, headers=headers)
data = response.json()
print(data)
```

### JavaScript (Fetch)

```javascript
const url = "https://api.unusualwhales.com/api/etfs/SPY/exposure";
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
      "weight": "string (decimal)",
      "full_name": "string",
      "etf": "string (ticker)",
      "last_price": "string (decimal)",
      "prev_price": "string (decimal)",
      "shares": "integer"
    }
  ]
}
```

### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| data | array | Array of ETF records containing the specified ticker |
| weight | string | The weight percentage of the ticker within the ETF |
| full_name | string | The full name of the ETF |
| etf | string | The ETF ticker symbol |
| last_price | string | The most recent price of the ETF |
| prev_price | string | The previous closing price of the ETF |
| shares | integer | Number of shares of the ticker held by the ETF |

## Example Response

```json
{
  "data": [
    {
      "weight": "56.075506755133",
      "full_name": "MAIN BUYWRITE ETF",
      "etf": "BUYW",
      "last_price": "14.21",
      "prev_price": "14.26",
      "shares": 573800
    },
    {
      "weight": "20.970086",
      "full_name": "SIMPLIFY VOLATILITY PREMIUM ETF",
      "etf": "SVOL",
      "last_price": "17.78",
      "prev_price": "17.88",
      "shares": 351940
    },
    {
      "weight": "48.7",
      "full_name": "ADVISORSHARES DORSEY WRIGHT FSM US CORE ETF",
      "etf": "DWUS",
      "last_price": "53.9014",
      "prev_price": "54.4867",
      "shares": 144947
    }
  ]
}
```

## Error Responses

| Status Code | Description | Response Body |
|-------------|-------------|---------------|
| 400 | Bad Request | `{"error": "Invalid ticker symbol"}` |
| 401 | Unauthorized | `{"error": "Invalid or missing API key"}` |
| 404 | Not Found | `{"error": "Ticker not found in any ETFs"}` |
| 429 | Too Many Requests | `{"error": "Rate limit exceeded"}` |
| 500 | Internal Server Error | `{"error": "Server error"}` |

## Rate Limiting

Standard API rate limits apply. Monitor the response headers for rate limit information.

## Notes

- The endpoint returns a sorted list of ETFs containing the specified ticker
- Weights are returned as string decimals for precision
- Share counts reflect the current holdings data
- Prices are delayed and may not be real-time
- For broad-based indices like SPY, the result set can be quite large

## Related Endpoints

- [Holdings](/docs/etfs/holdings.md) - Get holdings of an ETF
- [Info](/docs/etfs/info.md) - Get detailed information about an ETF

## Validation Results

**Tested**: Yes

**Test Date**: 2025-10-22

**Status**: Working

**Notes**: Endpoint returns valid ETF data for stock tickers. Successfully tested with SPY ticker which returned 25+ ETFs containing SPY as a holding.
