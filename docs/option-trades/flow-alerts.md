# Flow Alerts

## Endpoint Details

**Path**: `GET /api/option-trades/flow-alerts`

**Operation ID**: `PublicApi.OptionTradeController.flow_alerts`

**Summary**: Returns the latest option flow alerts

**Tags**: option-trade

## Description

Returns the latest flow alerts showing significant option trading activity that triggers predefined alert rules. These alerts help identify institutional order flow and unusual options activity that may indicate significant market moves.

## Authentication

- **Required**: Yes
- **Type**: API Key
- **Header**: `Authorization: Bearer YOUR_API_KEY`

## Request Parameters

### Query Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| ticker_symbol | string | No | null | Filter by underlying ticker symbol |
| min_premium | integer | No | null | Minimum total premium in dollars |
| max_premium | integer | No | null | Maximum total premium in dollars |
| min_size | integer | No | null | Minimum number of contracts traded |
| max_size | integer | No | null | Maximum number of contracts traded |
| min_volume | integer | No | null | Minimum total volume |
| max_volume | integer | No | null | Maximum total volume |
| min_open_interest | integer | No | null | Minimum open interest |
| max_open_interest | integer | No | null | Maximum open interest |
| all_opening | boolean | No | false | Filter for opening trades only |
| is_floor | boolean | No | false | Filter for floor trades |
| is_sweep | boolean | No | false | Filter for sweep orders |
| is_call | boolean | No | false | Filter for call options |
| is_put | boolean | No | false | Filter for put options |
| is_ask_side | boolean | No | false | Filter for ask-side trades |
| is_bid_side | boolean | No | false | Filter for bid-side trades |
| rule_name[] | string | No | null | Filter by alert rule name |
| min_diff | integer | No | null | Minimum difference (price/strike) |
| max_diff | integer | No | null | Maximum difference |
| min_volume_oi_ratio | float | No | null | Minimum volume-to-OI ratio |
| max_volume_oi_ratio | float | No | null | Maximum volume-to-OI ratio |
| is_otm | boolean | No | false | Filter for OTM contracts only |
| issue_types[] | string | No | null | Filter by issue type (stock, etf, index) |
| min_dte | integer | No | null | Minimum days to expiration |
| max_dte | integer | No | null | Maximum days to expiration |
| newer_than | string | No | null | Filter alerts created after this timestamp |
| older_than | string | No | null | Filter alerts created before this timestamp |
| limit | integer | No | 100 | Maximum number of results (max: 200, min: 1) |

## Example Requests

### cURL

```bash
curl -X GET "https://api.unusualwhales.com/api/option-trades/flow-alerts?limit=10" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

Filter for large premium moves:
```bash
curl -X GET "https://api.unusualwhales.com/api/option-trades/flow-alerts?is_sweep=true&min_premium=100000&limit=10" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

Filter by ticker:
```bash
curl -X GET "https://api.unusualwhales.com/api/option-trades/flow-alerts?ticker_symbol=AAPL&limit=10" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

### Python

```python
import requests

url = "https://api.unusualwhales.com/api/option-trades/flow-alerts"
headers = {
    "Authorization": "Bearer YOUR_API_KEY"
}
params = {
    "limit": 10,
    "is_sweep": True
}

response = requests.get(url, headers=headers, params=params)
data = response.json()
print(data)
```

### JavaScript (Fetch)

```javascript
const url = "https://api.unusualwhales.com/api/option-trades/flow-alerts?limit=10";
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
      "option_chain": "string",
      "type": "string (call/put)",
      "strike": "string",
      "expiry": "string (YYYY-MM-DD)",
      "total_size": "integer",
      "total_premium": "string",
      "price": "string",
      "volume": "integer",
      "open_interest": "integer",
      "volume_oi_ratio": "float",
      "alert_rule": "string",
      "has_sweep": "boolean",
      "all_opening_trades": "boolean",
      "created_at": "string (ISO 8601)",
      "trade_count": "integer"
    }
  ]
}
```

### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| ticker | string | Underlying stock ticker |
| option_chain | string | Full option contract symbol |
| type | string | Option type (call or put) |
| strike | string | Strike price |
| expiry | string | Expiration date |
| total_size | integer | Total number of contracts traded |
| total_premium | string | Total premium value in dollars |
| price | string | Average price of the trade |
| volume | integer | Total volume |
| open_interest | integer | Open interest for the contract |
| volume_oi_ratio | float | Volume to open interest ratio |
| alert_rule | string | Name of the alert rule that triggered |
| has_sweep | boolean | Whether trade included sweep orders |
| all_opening_trades | boolean | Whether all trades were opening trades |
| created_at | string | Timestamp when the alert was created |
| trade_count | integer | Number of individual trades |

## Example Response

```json
{
  "data": [
    {
      "total_size": 514,
      "has_singleleg": true,
      "has_sweep": false,
      "rule_id": "e6b9f0b6-fcd9-44fe-9d1c-f53521c152c3",
      "next_earnings_date": null,
      "all_opening_trades": false,
      "price": "2.8",
      "open_interest": 1061,
      "bid": "2.79",
      "sector": null,
      "expiry_count": 1,
      "total_ask_side_prem": "143920",
      "iv_end": "0.161479236210277",
      "has_floor": false,
      "total_bid_side_prem": "0",
      "expiry": "2025-10-28",
      "start_time": 1761164032782,
      "iv_start": "0.161479236210277",
      "created_at": "2025-10-22T20:27:01.354429Z",
      "volume": 34468,
      "underlying_price": "605.65",
      "ask": "2.8",
      "volume_oi_ratio": "32.4863336475024",
      "end_time": 1761164032828,
      "alert_rule": "RepeatedHits",
      "has_multileg": false,
      "strike": "611",
      "id": "fda36fab-b0a8-4d12-9bd4-79b8880cc78f",
      "option_chain": "QQQ251028C00611000",
      "er_time": null,
      "total_premium": "143920",
      "type": "call",
      "marketcap": "385698577500",
      "ticker": "QQQ",
      "trade_count": 8
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

Standard API rate limits apply. This endpoint provides real-time flow alert data.

## Notes

- Flow alerts identify significant options activity that may indicate institutional positioning
- Sweep orders indicate large orders that were split across multiple price levels
- Opening trades suggest new positions being established
- High volume-to-OI ratio (> 1.0) indicates unusual activity relative to existing positions
- Multiple filter combinations can create highly specific searches
- Recent alerts appear first in the list
- Alerts are generated throughout the trading day based on predefined rules

## Alert Rules

Common alert rules include:
- **RepeatedHits**: Multiple trades at same strike
- **Sweep Orders**: Large institutional orders
- **IV Change**: Significant implied volatility changes
- **Volume Spike**: Unusual volume activity
- **OI Change**: Open interest increases

## Related Endpoints

- [/api/option-contract/{id}/flow](../option-contract/flow.md) - Individual contract flow data
- [/api/market/top-net-impact](../market/top-net-impact.md) - Top tickers by net premium
- [/api/option-trades/full-tape](./full-tape.md) - Complete trading tape for a date

## Validation Results

**Tested**: Yes

**Test Date**: 2025-10-22

**Status**: Working

**Notes**: Endpoint returns flow alerts with comprehensive filtering options. Useful for identifying institutional order flow and significant options activity.

**Response Time**: < 1 second

**Test Command**:
```bash
curl -s "https://api.unusualwhales.com/api/option-trades/flow-alerts?limit=3" \
  -H "Authorization: Bearer YOUR_API_KEY"
```
