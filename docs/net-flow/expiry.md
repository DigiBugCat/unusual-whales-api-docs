# Net Flow Expiry

## Endpoint Details

**Path**: `GET /api/net-flow/expiry`

**Operation ID**: `PublicApi.NetFlowController.expiry`

**Summary**: Returns net premium flow by expiry, moneyness, and tide type

**Tags**: market

## Description

Returns net premium flow by `tide_type` category, `moneyness` category, and `expiration` category, allowing you to create chart variations like [https://unusualwhales.com/zero-dte](https://unusualwhales.com/zero-dte).

This endpoint provides highly filtered net flow data to analyze specific trading dynamics:

- **tide_type**: Filter results by equity type (all, equity_only, etf_only, index_only)
- **moneyness**: Filter by contract moneyness (all, itm, otm, atm)
- **expiration**: Filter by expiration type (weekly, zero_dte)

## Authentication

- **Required**: Yes
- **Type**: API Key
- **Header**: `Authorization: Bearer YOUR_API_KEY`

## Request Parameters

### Query Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| date | string | No | last market day | Market date in YYYY-MM-DD format |
| moneyness[] | string array | No | all | Moneyness filter: all, itm, otm, atm |
| tide_type[] | string array | No | all | Tide type filter: all, equity_only, etf_only, index_only |
| expiration[] | string array | No | weekly, zero_dte | Expiration filter: weekly, zero_dte |

## Example Requests

### cURL

```bash
curl -X GET "https://api.unusualwhales.com/api/net-flow/expiry" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

Filter for zero-DTE OTM equity options:
```bash
curl -X GET "https://api.unusualwhales.com/api/net-flow/expiry?expiration=zero_dte&moneyness=otm&tide_type=equity_only" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

### Python

```python
import requests

url = "https://api.unusualwhales.com/api/net-flow/expiry"
headers = {
    "Authorization": "Bearer YOUR_API_KEY"
}
params = {
    "expiration": "zero_dte",
    "moneyness": "otm",
    "tide_type": "equity_only"
}

response = requests.get(url, headers=headers, params=params)
data = response.json()
print(data)
```

### JavaScript (Fetch)

```javascript
const url = "https://api.unusualwhales.com/api/net-flow/expiry?expiration=zero_dte";
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
      "data": [
        {
          "timestamp": "string (ISO 8601)",
          "date": "string (YYYY-MM-DD)",
          "net_call_premium": "string (decimal)",
          "net_put_premium": "string (decimal)",
          "net_volume": "integer",
          "underlying_price": "string (decimal)"
        }
      ]
    }
  ]
}
```

### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| data | array | Array of filtered tide responses |
| timestamp | string | ISO 8601 formatted timestamp |
| date | string | Trading date in YYYY-MM-DD format |
| net_call_premium | string | Net call premium for the filtered set |
| net_put_premium | string | Net put premium for the filtered set |
| net_volume | integer | Net volume for the filtered set |
| underlying_price | string | Current underlying price reference |

## Example Response

```json
{
  "data": [
    {
      "data": [
        {
          "timestamp": "2025-10-22T13:30:00Z",
          "date": "2025-10-22",
          "net_call_premium": "155067.40",
          "net_put_premium": "247552.00",
          "net_volume": "-4469",
          "underlying_price": "671.15"
        },
        {
          "timestamp": "2025-10-22T13:31:00Z",
          "date": "2025-10-22",
          "net_call_premium": "-1153468.60",
          "net_put_premium": "1544633.20",
          "net_volume": "-12673",
          "underlying_price": "670.99"
        },
        {
          "timestamp": "2025-10-22T13:32:00Z",
          "date": "2025-10-22",
          "net_call_premium": "-877775.94",
          "net_put_premium": "665490.30",
          "net_volume": "-3398",
          "underlying_price": "671.075"
        }
      ]
    }
  ]
}
```

## Error Responses

| Status Code | Description | Response Body |
|-------------|-------------|---------------|
| 400 | Bad Request | `{"error": "Invalid parameters"}` |
| 401 | Unauthorized | `{"error": "Invalid API key"}` |
| 422 | Unprocessable Entity | `{"error": "Unprocessable Entity"}` |
| 500 | Internal Server Error | `{"error": "Server error"}` |

## Rate Limiting

Standard API rate limits apply.

## Notes

- The endpoint returns data nested in a "data" array structure
- You can combine multiple filters for highly specific analysis
- Default expiration filter includes both weekly and zero-DTE contracts
- Zero-DTE (0 days to expiration) shows same-day expiring options activity
- Moneyness filtering removes noise by focusing on specific contract types
- Positive net premium indicates bullish activity, negative indicates bearish
- Particularly useful for analyzing end-of-day options activity

## Moneyness Definitions

- **ITM (In The Money)**: Call contracts with strike < current price, Put contracts with strike > current price
- **OTM (Out Of The Money)**: Call contracts with strike > current price, Put contracts with strike < current price
- **ATM (At The Money)**: Contracts with strike near current price
- **All**: No moneyness filter applied

## Related Endpoints

- [/api/market/market-tide](../market/market-tide.md) - Full market tide without filters
- [/api/option-trades/flow-alerts](../option-trades/flow-alerts.md) - Individual flow alerts
- [/api/market/sector-tide](../market/sector-tide.md) - Sector-specific tide data

## Validation Results

**Tested**: Yes

**Test Date**: 2025-10-22

**Status**: Working

**Notes**: Endpoint returns nested structure with filtered net premium flow data. Useful for analyzing specific expiration and moneyness combinations.

**Response Time**: < 1 second

**Test Command**:
```bash
curl -s "https://api.unusualwhales.com/api/net-flow/expiry" \
  -H "Authorization: Bearer 5d1ec006-49f0-4a2a-90ae-5176c72425e3"
```
