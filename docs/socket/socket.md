# WebSocket channels

## Endpoint Details

**Path**: `GET /api/socket`

**Operation ID**: `PublicApi.SocketController.channels`

**Summary**: WebSocket channels

**Category**: socket

## Description

Returns the available WebSocket channels for connections.

## Websocket Guide
#You can find fully-functional examples that stream data from many channels here:

- Python: [https://github.com/unusual-whales/api-examples/tree/main/examples/ws-multi-channel-multi-output](https://github.com/unusual-whales/api-examples/tree/main/examples/ws-multi-channel-multi-output)
- Javascript: [https://github.com/unusual-whales/api-examples/tree/main/examples/ws-multi-channel-multi-output-nodejs](https://github.com/unusual-whales/api-examples/tree/main/examples/ws-multi-channel-multi-output-nodejs)



The following channels are available:
| Channel                     | Description                                                                                                           |
|-----------------------------|-----------------------------------------------------------------------------------------------------------------------|
| option_trades               | Receive live option trades throughout the trading session. Expect 6-10M records per day.                              |
| option_trades:TICKER        | Similar to `option_trades` but receive all trades only for the specified ticker.                                      |
| flow-alerts                 | Receive live flow alerts (all of them unfiltered). This data can be used to build views like [https://unusualwhales.com/option-flow-alerts](https://unusualwhales.com/option-flow-alerts). |
| price:TICKER                | Receive live price updates for the given ticker.                                                                      |
| news                        | Receive live headline news.                                                                                           |
| lit_trades                  | Receive live lit (exchange-based) trades throughout the trading session.                                               |
| off_lit_trades              | Receive live off-lit (dark pool) trades throughout the trading session.                                                |
| gex:TICKER                  | Receive live gex update for the given ticker.                                                                         |
| gex_strike:TICKER           | Receive live gex strike updates for every strike of the given ticker.                                                 |
| gex_strike_expiry:TICKER    | Receive live gex strike updates for every strike & expiry of the given ticker.                                        |

The `option_trades` channel will stream all 6,000,000 option trades in real-time, `option_trades:<TICKER>` will stream
all option trades for the given ticker in real-time.

`flow-alerts` will stream from the alerts [page](https://unusualwhales.com/option-flow-alerts?limit=50)

## Connect
For a python example script that streams gex by ticker (gex:TICKER), flow alerts (flow-alerts), and all TSLA option trades (option_trades:TSLA), see our "examples" repo on Github: [https://github.com/unusual-whales/api-examples/tree/main/examples/ws-multi-channel-multi-output](https://github.com/unusual-whales/api-examples/tree/main/examples/ws-multi-channel-multi-output)

We will use [websocat](https://github.com/vi/websocat) to demonstrate how to connect to the WebSocket server.

```bash
websocat "wss://api.unusualwhales.com/socket?token=<YOUR_API_TOKEN>"
{"channel":"option_trades","msg_type":"join"}
```
The server will then reply with
```bash
["option_trades",{"response":{},"status":"ok"}]
```
indicating that the connection was successful.

You will then receive data in the following format:
```bash
[<CHANNEL_NAME>, <PAYLOAD>]
```
during market hours.

To receive the trades only for a specific ticker, use the following command:
```bash
{"channel":"option_trades","msg_type":"join"}
```

You can join multiple channels with the same websocket connection:
```bash
websocat "wss://api.unusualwhales.com/socket?token=<YOUR_API_TOKEN>"
{"channel":"option_trades","msg_type":"join"}
["option_trades",{"response":{},"status":"ok"}]
{"channel":"option_trades:JPM","msg_type":"join"}
["option_trades:JPM",{"response":{},"status":"ok"}]
```

## Using a client
If you are using Python, you can use the [websocket-client](https://github.com/websocket-client/websocket-client) library to connect to the server.

```python
import websocket
import time
import rel
import json

def on_message(ws, msg):
    msg = json.loads(msg)
    channel, payload = msg
    print(f"Got a message on channel {channel}: Payload: {payload}")

def on_error(ws, error):
    print(error)

def on_close(ws, close_status_code, close_msg):
    print("### closed ###")

def on_open(ws):
    print("Opened connection")
    msg = {"channel":"option_trades","msg_type":"join"}
    ws.send(json.dumps(msg))

if __name__ == "__main__":
    websocket.enableTrace(False)
    ws = websocket.WebSocketApp("wss://api.unusualwhales.com/socket?token=<YOUR_TOKEN>",
                              on_open=on_open,
                              on_message=on_message,
                              on_error=on_error,
                              on_close=on_close)

    ws.run_forever(dispatcher=rel, reconnect=5)  # Set dispatcher to automatic reconnection, 5 second reconnect delay if connection closed unexpectedly
    rel.signal(2, rel.abort)  # Keyboard Interrupt
    rel.dispatch()


## Historic data
To download/access historic data, use the endpoint [/api/option-trades/full-tape](https://api.unusualwhales.com/docs#/operations/PublicApi.OptionTradeController.full_tape)


## Authentication

- **Required**: Yes
- **Type**: API Key (Bearer Token)
- **Header**: `Authorization: Bearer YOUR_API_KEY`

## Example Requests

### cURL

```bash
curl -X GET "https://api.unusualwhales.com/api/socket" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

### Python

```python
import requests

url = "https://api.unusualwhales.com/api/socket"
headers = {
    "Authorization": "Bearer YOUR_API_KEY"
}

response = requests.get(url, headers=headers)
data = response.json()
print(data)
```

### JavaScript (Fetch)

```javascript
const url = "https://api.unusualwhales.com/api/socket";
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
