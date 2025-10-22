# GEX

## Endpoint Details

**Path**: `GET /api/socket/gex`

**Operation ID**: `PublicApi.SocketController.gex`

**Summary**: GEX

**Category**: socket

## Description

**NOTE:**
This is the documentation for websocket channels `gex:<TICKER>`, `gex_strike:<TICKER>`, and `gex_strike_expiry:<TICKER>`.
Websocket access for personal use is only available through the[Advanced plan](https://unusualwhales.com/pricing?product=api).

You can find fully-functional examples that stream data from many channels here:

- Python: [https://github.com/unusual-whales/api-examples/tree/main/examples/ws-multi-channel-multi-output](https://github.com/unusual-whales/api-examples/tree/main/examples/ws-multi-channel-multi-output)
- Javascript: [https://github.com/unusual-whales/api-examples/tree/main/examples/ws-multi-channel-multi-output-nodejs](https://github.com/unusual-whales/api-examples/tree/main/examples/ws-multi-channel-multi-output-nodejs)



Connect to the websocket URI:

`wss://api.unusualwhales.com/socket?token=<YOUR_API_TOKEN>`

then `join` the channel you wish to stream, for example `gex:SPY` for live GEX updates for SPY, `gex_strike:SPY` for strike-level GEX data, or `gex_strike_expiry:SPY` for strike and expiry level GEX data.

Payload format:

Format for `gex:<TICKER>`:
```
[
  "gex:SPY",
  {
    "ticker": "SPY",
    "timestamp": 1726670396000,
    "gamma_per_one_percent_move_oi": "-262444980.31",
    "delta_per_one_percent_move_oi": "",
    "charm_per_one_percent_move_oi": "-1677926539943.05",
    "vanna_per_one_percent_move_oi": "2842602508.57",
    "price": "562.86",
    "gamma_per_one_percent_move_vol": "-934307209.58",
    "delta_per_one_percent_move_vol": "",
    "charm_per_one_percent_move_vol": "-556207588704.10",
    "vanna_per_one_percent_move_vol": "128814703.59",
    "gamma_per_one_percent_move_dir": "-9372185.61",
    "charm_per_one_percent_move_dir": "-2055997560.50",
    "vanna_per_one_percent_move_dir": "-6220855.09"
  }
]
```

Format for `gex_strike:<TICKER>`:
```
[
  "gex_strike:SPY",
  {
    "ticker": "SPY",
    "timestamp": 1726670426000,
    "call_gamma_oi": "174792.59",
    "put_gamma_oi": "-1172037.66",
    "call_charm_oi": "85658181.72",
    "put_charm_oi": "-315259003.37",
    "call_vanna_oi": "-6103.51",
    "put_vanna_oi": "1337727.64",
    "call_gamma_vol": "15596.81",
    "put_gamma_vol": "-236.69",
    "call_charm_vol": "-326871.58",
    "put_charm_vol": "-68457.78",
    "call_vanna_vol": "2063.13",
    "put_vanna_vol": "845.06",
    "strike": "290",
    "price": "562.96",
    "call_gamma_ask_vol": "-4064.62",
    "call_gamma_bid_vol": "11532.18",
    "put_gamma_ask_vol": "-140.95",
    "put_gamma_bid_vol": "95.73",
    "call_charm_ask_vol": "85184.72",
    "call_charm_bid_vol": "-241686.87",
    "put_charm_ask_vol": "-59412.37",
    "put_charm_bid_vol": "9045.42",
    "call_vanna_ask_vol": "-537.66",
    "call_vanna_bid_vol": "1525.46",
    "put_vanna_ask_vol": "523.79",
    "put_vanna_bid_vol": "-321.27"
  }
]
```

Format for `gex_strike_expiry:<TICKER>`:
```
[
  "gex_strike_expiry:SPY",
  {
    "ticker": "SPY",
    "expiry": "2025-01-24",
    "timestamp": 1726670426000,
    "call_gamma_oi": "174792.59",
    "put_gamma_oi": "-1172037.66",
    "call_charm_oi": "85658181.72",
    "put_charm_oi": "-315259003.37",
    "call_vanna_oi": "-6103.51",
    "put_vanna_oi": "1337727.64",
    "call_gamma_vol": "15596.81",
    "put_gamma_vol": "-236.69",
    "call_charm_vol": "-326871.58",
    "put_charm_vol": "-68457.78",
    "call_vanna_vol": "2063.13",
    "put_vanna_vol": "845.06",
    "strike": "290",
    "price": "562.96",
    "call_gamma_ask_vol": "-4064.62",
    "call_gamma_bid_vol": "11532.18",
    "put_gamma_ask_vol": "-140.95",
    "put_gamma_bid_vol": "95.73",
    "call_charm_ask_vol": "85184.72",
    "call_charm_bid_vol": "-241686.87",
    "put_charm_ask_vol": "-59412.37",
    "put_charm_bid_vol": "9045.42",
    "call_vanna_ask_vol": "-537.66",
    "call_vanna_bid_vol": "1525.46",
    "put_vanna_ask_vol": "523.79",
    "put_vanna_bid_vol": "-321.27"
  }
]
```


## Authentication

- **Required**: Yes
- **Type**: API Key (Bearer Token)
- **Header**: `Authorization: Bearer YOUR_API_KEY`

## Example Requests

### cURL

```bash
curl -X GET "https://api.unusualwhales.com/api/socket/gex" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

### Python

```python
import requests

url = "https://api.unusualwhales.com/api/socket/gex"
headers = {
    "Authorization": "Bearer YOUR_API_KEY"
}

response = requests.get(url, headers=headers)
data = response.json()
print(data)
```

### JavaScript (Fetch)

```javascript
const url = "https://api.unusualwhales.com/api/socket/gex";
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
