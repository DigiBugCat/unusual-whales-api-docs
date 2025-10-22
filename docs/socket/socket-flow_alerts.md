# Flow alerts

## Endpoint Details

**Path**: `GET /api/socket/flow_alerts`

**Operation ID**: `PublicApi.SocketController.flow_alerts`

**Summary**: Flow alerts

**Category**: socket

## Description

**NOTE:**
This is the documentation for websocket channel `flow-alerts`.
Websocket access for personal use is only available through the [Advanced plan](https://unusualwhales.com/pricing?product=api).

You can find fully-functional examples that stream data from many channels here:

- Python: [https://github.com/unusual-whales/api-examples/tree/main/examples/ws-multi-channel-multi-output](https://github.com/unusual-whales/api-examples/tree/main/examples/ws-multi-channel-multi-output)
- Javascript: [https://github.com/unusual-whales/api-examples/tree/main/examples/ws-multi-channel-multi-output-nodejs](https://github.com/unusual-whales/api-examples/tree/main/examples/ws-multi-channel-multi-output-nodejs)



Connect to the websocket URI:

`wss://api.unusualwhales.com/socket?token=<YOUR_API_TOKEN>`

then `join` the channel you wish to stream: `flow-alerts` for all flow alerts.

Payload format:

```
[
  "flow-alerts",
  {
    "rule_id": "5ce5ec11-087c-4c00-b164-08106b015856",
    "rule_name": "RepeatedHitsDescendingFill",
    "ticker": "DIA",
    "option_chain": "DIA241018C00415000",
    "underlying_price": 415.981,
    "volume": 106,
    "total_size": 50,
    "total_premium": 36466,
    "total_ask_side_prem": 36466,
    "total_bid_side_prem": 0,
    "start_time": 1726670212648,
    "end_time": 1726670212748,
    "url": "",
    "price": 7.3,
    "has_multileg": false,
    "has_sweep": false,
    "has_floor": false,
    "open_interest": 575,
    "all_opening_trades": false,
    "id": "29ed5829-e4ce-4934-876b-51985d2f9b70",
    "has_singleleg": true,
    "volume_oi_ratio": 0,
    "trade_ids": [
      "417f0cd6-09ae-4d43-8542-38557bb713aa",
      "4af4c646-4b21-4a27-8326-db7b0698d3d8",
      "74ddcd55-dcb3-4543-a488-16ee7ca91d45",
      "4ec49859-74a2-4d32-9911-ea329dd77326",
      "e164da3a-a6aa-41d9-a948-c17817453a21",
      "b0d98eeb-1429-4494-9dcc-8d5e7eb46f7d",
      "81b1dcad-f3f6-48a2-bf51-0bfd362ad372"
    ],
    "trade_count": 7,
    "expiry_count": 1,
    "executed_at": 1726670212748,
    "ask_vol": 52,
    "bid_vol": 49,
    "no_side_vol": 0,
    "mid_vol": 5,
    "multi_vol": 0,
    "stock_multi_vol": 0,
    "upstream_condition_details": [
      "auto",
      "slan"
    ],
    "exchanges": [
      "XCBO",
      "MPRL"
    ],
    "bid": "7.15",
    "ask": "7.3"
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
curl -X GET "https://api.unusualwhales.com/api/socket/flow_alerts" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

### Python

```python
import requests

url = "https://api.unusualwhales.com/api/socket/flow_alerts"
headers = {
    "Authorization": "Bearer YOUR_API_KEY"
}

response = requests.get(url, headers=headers)
data = response.json()
print(data)
```

### JavaScript (Fetch)

```javascript
const url = "https://api.unusualwhales.com/api/socket/flow_alerts";
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
