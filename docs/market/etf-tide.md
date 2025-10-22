# ETF Tide

## Endpoint Details

**Path**: `GET /api/market/{ticker}/etf-tide`

**Operation ID**: `PublicApi.MarketController.etf_tide`

**Summary**: Returns options sentiment for holdings of a specific ETF

**Tags**: market

## Description

The ETF Tide is similar to the Market Tide. While the market tide is based on options activity of the whole market, the ETF Tide is only based on the options activity of the holdings of the specified ETF.

This allows you to identify specific ETF's constituent sentiment and understand which holdings are driving options activity.

## Authentication

- **Required**: Yes
- **Type**: API Key
- **Header**: `Authorization: Bearer YOUR_API_KEY`

## Request Parameters

### Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ticker | string | Yes | ETF ticker symbol (e.g., SPY, QQQ, IWM, XLK) |

### Query Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| date | string | No | current/last market day | Market date in YYYY-MM-DD format |

## Example Requests

### cURL

```bash
curl -X GET "https://api.unusualwhales.com/api/market/SPY/etf-tide" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

With specific date:
```bash
curl -X GET "https://api.unusualwhales.com/api/market/QQQ/etf-tide?date=2025-10-21" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

### Python

```python
import requests

url = "https://api.unusualwhales.com/api/market/SPY/etf-tide"
headers = {
    "Authorization": "Bearer YOUR_API_KEY"
}

response = requests.get(url, headers=headers)
data = response.json()
print(data)
```

### JavaScript (Fetch)

```javascript
const url = "https://api.unusualwhales.com/api/market/SPY/etf-tide";
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
      "timestamp": "string (ISO 8601)",
      "date": "string (YYYY-MM-DD)",
      "net_call_premium": "string (decimal)",
      "net_put_premium": "string (decimal)",
      "net_volume": "integer",
      "underlying_price": "string (decimal)"
    }
  ]
}
```

### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| data | array | Array of ETF tide data points |
| timestamp | string | ISO 8601 formatted timestamp |
| date | string | Trading date in YYYY-MM-DD format |
| net_call_premium | string | Net call premium for ETF holdings |
| net_put_premium | string | Net put premium for ETF holdings |
| net_volume | integer | Net trading volume |
| underlying_price | string | Price of the ETF at that timestamp |

## Example Response

```json
{
  "data": [
    {
      "timestamp": "2025-10-22T13:30:00.000000Z",
      "date": "2025-10-22",
      "net_call_premium": "-539039.0000",
      "net_put_premium": "1176044.0000",
      "net_volume": "-14156",
      "underlying_price": "665.66"
    },
    {
      "timestamp": "2025-10-22T13:31:00.000000Z",
      "date": "2025-10-22",
      "net_call_premium": "-1736341.0000",
      "net_put_premium": "-231771.0000",
      "net_volume": "-18021",
      "underlying_price": "663.52"
    },
    {
      "timestamp": "2025-10-22T13:32:00.000000Z",
      "date": "2025-10-22",
      "net_call_premium": "-5785047.0000",
      "net_put_premium": "506363.0000",
      "net_volume": "-17266",
      "underlying_price": "671.05"
    }
  ]
}
```

## Error Responses

| Status Code | Description | Response Body |
|-------------|-------------|---------------|
| 400 | Bad Request | `{"error": "Invalid ETF ticker"}` |
| 401 | Unauthorized | `{"error": "Invalid API key"}` |
| 422 | Unprocessable Entity | `{"error": "Invalid parameters"}` |
| 500 | Internal Server Error | `{"error": "Server error"}` |

## Rate Limiting

Standard API rate limits apply.

## Notes

- ETF tide reflects the combined sentiment of the ETF's holdings
- Useful for understanding which constituents are driving ETF-level options activity
- Includes underlying ETF price for context and correlation analysis
- Data is provided in 1-minute intervals during market hours
- Sentiment interpretation: positive net premium = bullish, negative = bearish
- Works with any ETF that has significant options volume
- Popular ETFs: SPY (S&P 500), QQQ (Nasdaq 100), IWM (Russell 2000), and sector ETFs (XLK, XLV, XLF, etc.)

## Related Endpoints

- [/api/market/market-tide](./market-tide.md) - Market-wide options sentiment
- [/api/market/sector-tide](./sector-tide.md) - Sector-specific options sentiment
- [/api/market/sector-etfs](./sector-etfs.md) - Sector ETF statistics

## Validation Results

**Tested**: Yes

**Test Date**: 2025-10-22

**Status**: Working

**Notes**: Endpoint returns detailed options sentiment for ETF holdings with timestamp and price data. SPY holdings showed bearish sentiment during the tested period with both negative call premium and positive put premium.

**Response Time**: < 1 second

**Sample ETF**: SPY (S&P 500)

**Price Range**: 663.52 - 671.05

**Test Command**:
```bash
curl -s "https://api.unusualwhales.com/api/market/SPY/etf-tide" \
  -H "Authorization: Bearer YOUR_API_KEY"
```
