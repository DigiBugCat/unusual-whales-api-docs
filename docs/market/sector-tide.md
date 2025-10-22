# Sector Tide

## Endpoint Details

**Path**: `GET /api/market/{sector}/sector-tide`

**Operation ID**: `PublicApi.MarketController.sec_indst`

**Summary**: Returns options sentiment for a specific sector

**Tags**: market

## Description

The Sector Tide is similar to the Market Tide. While the market tide is based on options activity of the whole market, the sector tide is only based on the options activity of companies which are in that specific sector.

This allows you to identify sector-specific sentiment and rotation opportunities.

## Authentication

- **Required**: Yes
- **Type**: API Key
- **Header**: `Authorization: Bearer YOUR_API_KEY`

## Request Parameters

### Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| sector | string | Yes | Sector name (e.g., Technology, Healthcare, Financials, Energy, etc.) |

### Query Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| date | string | No | current/last market day | Market date in YYYY-MM-DD format |

## Example Requests

### cURL

```bash
curl -X GET "https://api.unusualwhales.com/api/market/Technology/sector-tide" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

With specific date:
```bash
curl -X GET "https://api.unusualwhales.com/api/market/Healthcare/sector-tide?date=2025-10-21" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

### Python

```python
import requests

url = "https://api.unusualwhales.com/api/market/Technology/sector-tide"
headers = {
    "Authorization": "Bearer YOUR_API_KEY"
}

response = requests.get(url, headers=headers)
data = response.json()
print(data)
```

### JavaScript (Fetch)

```javascript
const url = "https://api.unusualwhales.com/api/market/Technology/sector-tide";
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
      "net_volume": "integer"
    }
  ]
}
```

### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| data | array | Array of sector tide data points |
| timestamp | string | ISO 8601 formatted timestamp with timezone |
| date | string | Trading date in YYYY-MM-DD format |
| net_call_premium | string | Net call premium for the sector |
| net_put_premium | string | Net put premium for the sector |
| net_volume | integer | Net trading volume for the sector |

## Example Response

```json
{
  "data": [
    {
      "timestamp": "2025-10-22T13:30:00Z",
      "date": "2025-10-22",
      "net_call_premium": "-3258803.00",
      "net_put_premium": "-1339425.00",
      "net_volume": -7800
    },
    {
      "timestamp": "2025-10-22T13:31:00Z",
      "date": "2025-10-22",
      "net_call_premium": "-395316.0000",
      "net_put_premium": "-2447924.0000",
      "net_volume": -558
    },
    {
      "timestamp": "2025-10-22T13:32:00Z",
      "date": "2025-10-22",
      "net_call_premium": "-1192269.0000",
      "net_put_premium": "-857768.0000",
      "net_volume": 6063
    }
  ]
}
```

## Error Responses

| Status Code | Description | Response Body |
|-------------|-------------|---------------|
| 400 | Bad Request | `{"error": "Invalid sector name"}` |
| 401 | Unauthorized | `{"error": "Invalid API key"}` |
| 422 | Unprocessable Entity | `{"error": "Invalid parameters"}` |
| 500 | Internal Server Error | `{"error": "Server error"}` |

## Rate Limiting

Standard API rate limits apply.

## Notes

- Sector names should match standard sector classification (e.g., Technology, Healthcare, Financials, Energy, Consumer Discretionary, Consumer Staples, Industrials, Materials, Real Estate, Utilities)
- Data is provided in 1-minute intervals during market hours
- Sentiment interpretation is the same as Market Tide: positive net premium = bullish, negative = bearish
- This endpoint is useful for sector rotation analysis
- Returns data for the specified date or current market day if not provided
- Can be compared with other sectors to identify relative strength

## Related Endpoints

- [/api/market/market-tide](./market-tide.md) - Market-wide options sentiment
- [/api/market/etf-tide](./etf-tide.md) - Options sentiment for specific ETF holdings
- [/api/market/sector-etfs](./sector-etfs.md) - Sector ETF statistics

## Validation Results

**Tested**: Yes

**Test Date**: 2025-10-22

**Status**: Working

**Notes**: Endpoint returns detailed sector-level options sentiment with timestamp data. Technology sector showed mixed sentiment with negative call and put premiums during the tested time period.

**Response Time**: < 1 second

**Sample Sector**: Technology

**Test Command**:
```bash
curl -s "https://api.unusualwhales.com/api/market/Technology/sector-tide" \
  -H "Authorization: Bearer YOUR_API_KEY"
```
