# Price

## Endpoint Details

**Path**: `GET /api/socket/price`

**Operation ID**: `PublicApi.SocketController.price`

**Summary**: Price

**Category**: socket

## Description

**NOTE:**
This is the documentation for websocket channel `price:<TICKER>`.
Websocket access for personal use is only available through the[Advanced plan](https://unusualwhales.com/pricing?product=api).

You can find fully-functional examples that stream data from many channels here:

- Python: [https://github.com/unusual-whales/api-examples/tree/main/examples/ws-multi-channel-multi-output](https://github.com/unusual-whales/api-examples/tree/main/examples/ws-multi-channel-multi-output)
- Javascript: [https://github.com/unusual-whales/api-examples/tree/main/examples/ws-multi-channel-multi-output-nodejs](https://github.com/unusual-whales/api-examples/tree/main/examples/ws-multi-channel-multi-output-nodejs)



Connect to the websocket URI:

`wss://api.unusualwhales.com/socket?token=<YOUR_API_TOKEN>`

then `join` the channel you wish to stream, for example `price:SPY` for live price updates for SPY.

Payload format:

```
["price:SPY",{"close":"562.82","time":1726670327692,"vol":6015555}]
```


## Authentication

- **Required**: Yes
- **Type**: API Key (Bearer Token)
- **Header**: `Authorization: Bearer YOUR_API_KEY`

## Example Requests

### cURL

```bash
curl -X GET "https://api.unusualwhales.com/api/socket/price" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

### Python

```python
import requests

url = "https://api.unusualwhales.com/api/socket/price"
headers = {
    "Authorization": "Bearer YOUR_API_KEY"
}

response = requests.get(url, headers=headers)
data = response.json()
print(data)
```

### JavaScript (Fetch)

```javascript
const url = "https://api.unusualwhales.com/api/socket/price";
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
