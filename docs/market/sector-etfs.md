# Sector ETFs

## Endpoint Details

**Path**: `GET /api/market/sector-etfs`

**Operation ID**: `PublicApi.MarketController.sector_etfs`

**Summary**: Returns current trading day statistics for SPDR sector ETFs

**Tags**: market

## Description

Returns the current trading day's statistics for all SPDR sector ETFs. This provides a comprehensive view of sector rotation and can be used to build a market overview showing which sectors are attracting the most options activity.

## Authentication

- **Required**: Yes
- **Type**: API Key
- **Header**: `Authorization: Bearer YOUR_API_KEY`

## Request Parameters

### Query Parameters

This endpoint does not accept any query parameters.

## Example Requests

### cURL

```bash
curl -X GET "https://api.unusualwhales.com/api/market/sector-etfs" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

### Python

```python
import requests

url = "https://api.unusualwhales.com/api/market/sector-etfs"
headers = {
    "Authorization": "Bearer YOUR_API_KEY"
}

response = requests.get(url, headers=headers)
data = response.json()
print(data)
```

### JavaScript (Fetch)

```javascript
const url = "https://api.unusualwhales.com/api/market/sector-etfs";
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
      "ticker": "string",
      "full_name": "string",
      "high": "string (decimal)",
      "low": "string (decimal)",
      "open": "string (decimal)",
      "last": "string (decimal)",
      "volume": "integer",
      "put_volume": "integer",
      "call_volume": "integer",
      "put_premium": "string (decimal)",
      "call_premium": "string (decimal)",
      "marketcap": "string (decimal)",
      "prev_date": "string (YYYY-MM-DD)",
      "in_out_flow": "array"
    }
  ]
}
```

### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| ticker | string | ETF symbol (e.g., SPY, XLK, XLV) |
| full_name | string | Full name of the sector or index |
| high | string | Day's high price |
| low | string | Day's low price |
| open | string | Opening price |
| last | string | Last traded price |
| volume | integer | Total trading volume |
| put_volume | integer | Total put option volume |
| call_volume | integer | Total call option volume |
| put_premium | string | Total put premium traded |
| call_premium | string | Total call premium traded |
| marketcap | string | Market capitalization in billions |
| prev_date | string | Previous trading date |
| in_out_flow | array | Historical inflow/outflow data |

## Example Response

```json
{
  "data": [
    {
      "high": "672",
      "low": "663.3",
      "open": "672",
      "last": "667.8",
      "ticker": "SPY",
      "full_name": "S&P 500 Index",
      "volume": 80299025,
      "put_volume": 5723283,
      "call_volume": 4645362,
      "put_premium": "1042762183.00",
      "call_premium": "742703414.0000",
      "marketcap": "671.281922",
      "prev_date": "2025-10-21",
      "in_out_flow": [
        {
          "date": "2025-10-15",
          "change": -8050000
        },
        {
          "date": "2025-10-16",
          "change": 3450000
        }
      ]
    }
  ]
}
```

## Error Responses

| Status Code | Description | Response Body |
|-------------|-------------|---------------|
| 401 | Unauthorized | `{"error": "Invalid API key"}` |
| 500 | Internal Server Error | `{"error": "Server error"}` |

## Rate Limiting

Standard API rate limits apply.

## Notes

- Data includes all major SPDR sector ETFs (Technology, Healthcare, Financials, Energy, etc.)
- Also includes broad market indices like SPY, QQQ, IWM
- Premium values represent total dollar value of options transactions
- Volume includes both stock and options trading volumes
- In/out flow data shows historical capital movements for the ETF
- Data is updated throughout the trading day
- This endpoint is useful for sector rotation analysis and identifying relative strength

## Related Endpoints

- [/api/market/market-tide](./market-tide.md) - Market-wide options sentiment
- [/api/market/sector-tide](./sector-tide.md) - Options sentiment by sector
- [/api/market/total-options-volume](./total-options-volume.md) - Total market options volume

## Validation Results

**Tested**: Yes

**Test Date**: 2025-10-22

**Status**: Working

**Notes**: Endpoint returns real-time trading statistics for all major sector ETFs including price action, volume, and options metrics.

**Response Time**: < 1 second

**ETFs Included**: SPY, QQQ, IWM, and various XL* sector ETFs

**Test Command**:
```bash
curl -s "https://api.unusualwhales.com/api/market/sector-etfs" \
  -H "Authorization: Bearer 5d1ec006-49f0-4a2a-90ae-5176c72425e3"
```
