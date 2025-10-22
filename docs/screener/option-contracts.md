# Hottest Option Contracts

## Endpoint Details

**Path**: `GET /api/screener/option-contracts`

**Operation ID**: `PublicApi.ScreenerController.contract_screener`

**Summary**: Hottest Chains

**Tags**: screener

## Description

A contract screener endpoint to screen the market for option contracts by a variety of filter options. This powerful tool identifies hot options contracts based on volume, open interest, Greeks, and other option-specific metrics. See the [Hottest Contracts](https://unusualwhales.com) feature for an example implementation.

## Authentication

- **Required**: Yes
- **Type**: API Key
- **Header**: `Authorization: Bearer YOUR_API_KEY`

## Request Parameters

### Path Parameters

None

### Query Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ticker | string | No | Filter by stock ticker symbol |
| limit | integer | No | Number of results to return (default: 50, max: 500) |
| offset | integer | No | Pagination offset |
| min_volume | integer | No | Minimum option volume |
| min_open_interest | integer | No | Minimum option open interest |
| min_delta | number | No | Minimum delta value |
| max_delta | number | No | Maximum delta value |
| min_gamma | number | No | Minimum gamma value |
| min_theta | number | No | Minimum theta value |
| min_vega | number | No | Minimum vega value |
| option_type | string | No | Filter by type (call, put) |
| expiration_days | integer | No | Days to expiration |
| min_price | number | No | Minimum underlying stock price |
| max_price | number | No | Maximum underlying stock price |
| sector | string | No | Filter by sector |
| sort_by | string | No | Field to sort by (volume, open_interest, delta, theta, etc.) |
| order | string | No | Sort order (asc, desc) |

See OpenAPI spec for complete list of 91+ available filter parameters.

### Request Body

None

## Example Requests

### cURL

```bash
# Get most active option contracts
curl -X GET "https://api.unusualwhales.com/api/screener/option-contracts?limit=20" \
  -H "Authorization: Bearer YOUR_API_KEY"

# Find high delta calls with significant volume
curl -X GET "https://api.unusualwhales.com/api/screener/option-contracts?option_type=call&min_delta=0.7&min_volume=100000&limit=25" \
  -H "Authorization: Bearer YOUR_API_KEY"

# Screen for short dated puts with high gamma
curl -X GET "https://api.unusualwhales.com/api/screener/option-contracts?option_type=put&expiration_days=7&min_gamma=0.01&limit=50" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

### Python

```python
import requests

url = "https://api.unusualwhales.com/api/screener/option-contracts"
headers = {
    "Authorization": "Bearer YOUR_API_KEY"
}
params = {
    "limit": 25,
    "min_volume": 50000,
    "option_type": "call",
    "sort_by": "volume"
}

response = requests.get(url, headers=headers, params=params)
data = response.json()
print(data)
```

### JavaScript (Fetch)

```javascript
const url = "https://api.unusualwhales.com/api/screener/option-contracts?limit=25&min_volume=50000&option_type=call";
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
      "option_symbol": "SPY251022C00671000",
      "ticker_symbol": "SPY",
      "stock_price": "667.8",
      "last_fill": "2025-10-22T20:14:59Z",
      "open": "2.01",
      "high": "2.01",
      "low": "0.01",
      "close": "0.01",
      "volume": 516026,
      "open_interest": 16136,
      "delta": "0.01901005106497827",
      "gamma": "0.03214143855314979",
      "theta": "-0.00887041154514212",
      "vega": "0.03156392659340953",
      "premium": "23932734.00",
      "roc": "0.0035577577875885897778803130",
      "trades": 39571,
      "sweep_volume": 25500,
      "multileg_volume": 28824,
      "days_of_vol_greater_than_oi": 7,
      "days_of_oi_increases": 9,
      "avg_price": "0.4637893051900485634444776013",
      "bid_side_volume": 254526,
      "ask_side_volume": 238506,
      "bid_side_perc_7_day": "0.777778",
      "ask_side_perc_7_day": "0.111111",
      "chain_prev_close": "1.63"
    }
  ]
}
```

### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| option_symbol | string | The option contract symbol (e.g., SPY251022C00671000) |
| ticker_symbol | string | Underlying stock ticker symbol |
| stock_price | string | Current underlying stock price |
| last_fill | string | ISO 8601 timestamp of last trade |
| open | string | Opening price |
| high | string | Daily high price |
| low | string | Daily low price |
| close | string | Closing price |
| volume | integer | Daily trading volume |
| open_interest | integer | Open interest (outstanding contracts) |
| delta | string | Delta Greek (directional exposure) |
| gamma | string | Gamma Greek (delta acceleration) |
| theta | string | Theta Greek (time decay) |
| vega | string | Vega Greek (volatility exposure) |
| premium | string | Total premium value |
| roc | string | Rate of change |
| trades | integer | Number of individual trades |
| sweep_volume | integer | Aggressive sweep volume |
| multileg_volume | integer | Multi-leg volume |
| days_of_vol_greater_than_oi | integer | Days where volume exceeded open interest |
| days_of_oi_increases | integer | Days with increasing open interest |
| avg_price | string | Average price traded |
| bid_side_volume | integer | Volume traded on bid side |
| ask_side_volume | integer | Volume traded on ask side |
| bid_side_perc_7_day | string | Percentage of 7-day volume on bid side |
| ask_side_perc_7_day | string | Percentage of 7-day volume on ask side |
| chain_prev_close | string | Previous close of the chain |

## Error Responses

| Status Code | Description | Response Body |
|-------------|-------------|---------------|
| 400 | Bad Request | `{"error": "Invalid filter parameters"}` |
| 401 | Unauthorized | `{"error": "Invalid API key"}` |
| 422 | Unprocessable Entity | `{"error": "Invalid parameter format"}` |
| 500 | Internal Server Error | `{"error": "Server error"}` |

## Rate Limiting

The API enforces rate limits on requests. Standard tier allows reasonable request frequency. Check response headers for rate limit information. Complex queries with many filters may use more rate limit points.

## Notes

- This endpoint supports 91+ filter parameters for precise options screening
- All price and calculation metrics are returned as string values for precision
- Greeks (delta, gamma, theta, vega) are the standard option sensitivities
- Delta: directional exposure (0-1 for calls, -1-0 for puts)
- Gamma: rate of delta change, higher gamma means more explosive moves
- Theta: time decay, negative for long positions
- Vega: volatility exposure
- Sweep volume indicates aggressive buying or selling
- Multi-leg volume includes spreads and complex structures
- Data is updated in real-time during market hours
- Pagination supported via limit and offset parameters
- Results can be sorted by any returned field
- Useful for identifying unusual options activity and potential breakouts
- Volume > OI for multiple days can signal strong interest in a contract

## Related Endpoints

- `/api/screener/stocks` - Screen stocks by technical and volatility metrics
- `/api/screener/analysts` - Get analyst ratings

## Validation Results

**Tested**: Yes

**Test Date**: 2025-10-22

**Status**: Working

**Notes**: Endpoint successfully returns option contract screener data. Response includes comprehensive Greeks and order flow metrics. Sample includes SPY call option with complete data. All calculated fields present and valid. Sweep volume and multi-leg volume metrics properly calculated. No rate limit issues encountered.
