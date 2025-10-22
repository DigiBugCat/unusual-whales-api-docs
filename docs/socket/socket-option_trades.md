# Option trades

## Endpoint Details

**Path**: `GET /api/socket/option_trades`

**Operation ID**: `PublicApi.SocketController.option_trades`

**Summary**: Option trades

**Category**: socket

## Description

**NOTE:**
This is the documentation for websocket channels `option_trades` and `option_trades:<TICKER>`.
Websocket access for personal use is only available through the [Advanced plan](https://unusualwhales.com/pricing?product=api).

You can find fully-functional examples that stream data from many channels here:

- Python: [https://github.com/unusual-whales/api-examples/tree/main/examples/ws-multi-channel-multi-output](https://github.com/unusual-whales/api-examples/tree/main/examples/ws-multi-channel-multi-output)
- Javascript: [https://github.com/unusual-whales/api-examples/tree/main/examples/ws-multi-channel-multi-output-nodejs](https://github.com/unusual-whales/api-examples/tree/main/examples/ws-multi-channel-multi-output-nodejs)



Connect to the websocket URI:

`wss://api.unusualwhales.com/socket?token=<YOUR_API_TOKEN>`

then `join` the channel(s) you wish to stream, for example `option_trades` for all tickers or `option_trades:TSLA` for TSLA transactions only.

Payload format:

```
{
    "id":"a4dc6020-0611-4c23-b0bc-99944c7348ab",
    "underlying_symbol":"UVIX",
    "executed_at":1726670167412,
    "nbbo_bid":"0.01",
    "nbbo_ask":"0.09",
    "size":1,
    "price":"0.01",
    "option_symbol":"UVIX240920C00025000",
    "created_at":1726670167461,
    "report_flags":[

    ],
    "tags":[
      "bid_side",
      "bearish",
      "etf"
    ],
    "expiry":"2024-09-20",
    "option_type":"call",
    "open_interest":410,
    "strike":"25.0000000000",
    "premium":"1.00",
    "volume":105,
    "underlying_price":"4.9261",
    "ewma_nbbo_ask":"0.09",
    "ewma_nbbo_bid":"0.01",
    "implied_volatility":"8.46381958089369",
    "delta":"0.01132315610146539",
    "theta":"-0.02291485773244166",
    "gamma":"0.00962272181839715",
    "vega":"0.0001082948756510385",
    "rho":"0.000002508438316242667",
    "theo":"0.01",
    "trade_code":"slan",
    "exchange":"XCBO",
    "ask_vol":10,
    "bid_vol":95,
    "no_side_vol":0,
    "mid_vol":0,
    "multi_vol":0,
    "stock_multi_vol":0
}
```


## Authentication

- **Required**: Yes
- **Type**: API Key (Bearer Token)
- **Header**: `Authorization: Bearer YOUR_API_KEY`

## Example Requests

### cURL

```bash
curl -X GET "https://api.unusualwhales.com/api/socket/option_trades" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

### Python

```python
import requests

url = "https://api.unusualwhales.com/api/socket/option_trades"
headers = {
    "Authorization": "Bearer YOUR_API_KEY"
}

response = requests.get(url, headers=headers)
data = response.json()
print(data)
```

### JavaScript (Fetch)

```javascript
const url = "https://api.unusualwhales.com/api/socket/option_trades";
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

The response structure varies by endpoint. Refer to the OpenAPI specification for detailed response schemas.

## Error Responses

| Status Code | Description |
|-------------|-------------|
| 400 | Bad Request - Invalid parameters |
| 401 | Unauthorized - Invalid or missing API key |
| 404 | Not Found - Resource not found |
| 429 | Too Many Requests - Rate limit exceeded |
| 500 | Internal Server Error |

## Rate Limiting

Rate limiting applies to all endpoints. Headers returned with each response contain rate limit information.

## Notes

- This endpoint requires a valid API key
- Include relevant date parameters where applicable
- Refer to the main API documentation for additional details

## Validation Results

**Tested**: Yes

**Test Date**: 2025-10-22

**Status**: Endpoint configuration validated

## Related Endpoints

- See API documentation for related endpoints
