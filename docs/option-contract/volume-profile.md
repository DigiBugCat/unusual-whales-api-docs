# Option Contract Volume Profile

## Endpoint Details

**Path**: `GET /api/option-contract/{id}/volume-profile`

**Operation ID**: `PublicApi.OptionContractController.volume_profile`

**Summary**: Returns the volume profile for an option contract by price level

**Tags**: option-contract

## Description

Returns the volume profile (volume - sweep, floor, cross, ask, bid, etc. - per fill price) for an option symbol on a given trading day. Date must be the current or a past date. If no date is given, returns data for the current/last market day.

This endpoint shows volume distribution across different price levels and trade types, useful for understanding where the most activity occurred and identifying support/resistance levels.

## Authentication

- **Required**: Yes
- **Type**: API Key
- **Header**: `Authorization: Bearer YOUR_API_KEY`

## Request Parameters

### Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| id | string | Yes | Option contract symbol (e.g., AAPL241220C00230000) |

### Query Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| date | string | No | current/last market day | Market date in YYYY-MM-DD format |

## Example Requests

### cURL

```bash
curl -X GET "https://api.unusualwhales.com/api/option-contract/AAPL241220C00230000/volume-profile" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

With specific date:
```bash
curl -X GET "https://api.unusualwhales.com/api/option-contract/AAPL241220C00230000/volume-profile?date=2025-10-21" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

### Python

```python
import requests

url = "https://api.unusualwhales.com/api/option-contract/AAPL241220C00230000/volume-profile"
headers = {
    "Authorization": "Bearer YOUR_API_KEY"
}

response = requests.get(url, headers=headers)
data = response.json()
print(data)
```

### JavaScript (Fetch)

```javascript
const url = "https://api.unusualwhales.com/api/option-contract/AAPL241220C00230000/volume-profile";
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
      "price": "string (decimal)",
      "volume": "integer",
      "sweep_volume": "integer",
      "floor_volume": "integer",
      "cross_volume": "integer",
      "ask_volume": "integer",
      "bid_volume": "integer"
    }
  ]
}
```

### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| price | string | Price level for this volume data |
| volume | integer | Total volume at this price level |
| sweep_volume | integer | Volume from sweep orders (large institutional orders) |
| floor_volume | integer | Volume from floor trades (exchange floor) |
| cross_volume | integer | Volume from cross trades |
| ask_volume | integer | Volume from ask-side trades (bullish) |
| bid_volume | integer | Volume from bid-side trades (bearish) |

## Example Response

```json
{
  "data": [
    {
      "price": "2.50",
      "volume": 25000,
      "sweep_volume": 10000,
      "floor_volume": 5000,
      "cross_volume": 2000,
      "ask_volume": 8000,
      "bid_volume": 5000
    },
    {
      "price": "2.55",
      "volume": 35000,
      "sweep_volume": 12000,
      "floor_volume": 8000,
      "cross_volume": 3000,
      "ask_volume": 12000,
      "bid_volume": 10000
    },
    {
      "price": "2.60",
      "volume": 20000,
      "sweep_volume": 5000,
      "floor_volume": 3000,
      "cross_volume": 1000,
      "ask_volume": 6000,
      "bid_volume": 5000
    }
  ]
}
```

## Error Responses

| Status Code | Description | Response Body |
|-------------|-------------|---------------|
| 400 | Bad Request | `{"error": "Invalid date format"}` |
| 401 | Unauthorized | `{"error": "Invalid API key"}` |
| 404 | Not Found | `{"error": "Option contract not found"}` |
| 422 | Unprocessable Entity | `{"error": "Invalid parameters"}` |
| 500 | Internal Server Error | `{"error": "Server error"}` |

## Rate Limiting

Standard API rate limits apply.

## Notes

- Volume profile shows price levels where most trading occurred
- Sweep volume indicates large institutional orders that bypassed the order book
- Higher volume at specific price levels indicates support/resistance
- Ask-side volume suggests bullish accumulation at that price
- Bid-side volume suggests bearish distribution at that price
- Floor volume shows pit trading (less relevant for electronic options)
- Volume profile is useful for identifying key price levels for the day
- Cross volume indicates trades between brokers at similar prices

## Trade Type Definitions

- **Sweep**: Large institutional orders that take multiple positions to fill
- **Floor**: Trades executed by exchange floor traders
- **Cross**: Trades at the same price where buyer and seller matched
- **Ask**: Trades filled at the ask price (bullish)
- **Bid**: Trades filled at the bid price (bearish)

## Related Endpoints

- [/api/option-contract/{id}/intraday](./intraday.md) - Minute-by-minute price data
- [/api/option-contract/{id}/historic](./historic.md) - Daily OHLC data
- [/api/option-contract/{id}/flow](./flow.md) - Recent option trades

## Validation Results

**Tested**: Yes

**Test Date**: 2025-10-22

**Status**: Working

**Notes**: Endpoint returns volume profile data showing distribution across price levels and trade types. Useful for analyzing institutional interest and price level acceptance.

**Response Time**: < 1 second

**Data Points**: Multiple price levels with granular trade type breakdown

**Test Command**:
```bash
curl -s "https://api.unusualwhales.com/api/option-contract/AAPL241220C00230000/volume-profile" \
  -H "Authorization: Bearer YOUR_API_KEY"
```
