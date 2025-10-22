# Call/Put Net/Vol Ticks

## Endpoint Details

**Path**: `GET /api/stock/{ticker}/net-prem-ticks`

**Operation ID**: `PublicApi.TickerController.net_prem_ticks`

**Summary**: Call/Put Net/Vol Ticks

**Category**: stock

## Description

Returns the net premium ticks for a given ticker which can be used to build the following chart:
![Net Prem chart](https://i.imgur.com/Rom1kcB.png)

----
Each tick is resembling the data for a single minute tick. To build a daily chart
you would have to add the previous data to the current tick:
```javascript
const url =
  'https://api.unusualwhales.com/api/stock/AAPL/net-prem-ticks';
const options = {
  method: 'GET',
  headers: {
    Accept: 'application/json',
    Authorization: 'Bearer YOUR_TOKEN'
  }
};

fetch(url, options)
.then(r => r.json())
.then(r => {
  const {data} = r.data;
  const fieldsToSum = [
    "net_call_premium",
    "net_call_volume",
    "net_put_premium",
    "net_put_volume"
  ];

  let result = [];
  data.forEach((e, idx) => {
    e.net_call_premium = parseFloat(e.net_call_premium);
    e.net_put_premium = parseFloat(e.net_put_premium);
    if (idx !== 0) {
      fieldsToSum.forEach((field) => {
        e[field] = e[field] + result[idx-1][field];
      })
    }
    result.push(e);
  })

  return result;
});

```


## Authentication

- **Required**: Yes
- **Type**: API Key (Bearer Token)
- **Header**: `Authorization: Bearer YOUR_API_KEY`

## Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ticker | string | Yes |  |

## Query Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| date | string | No |  |

## Example Requests

### cURL

```bash
curl -X GET "https://api.unusualwhales.com/api/stock/{ticker}/net-prem-ticks" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

### Python

```python
import requests

url = "https://api.unusualwhales.com/api/stock/{ticker}/net-prem-ticks"
headers = {
    "Authorization": "Bearer YOUR_API_KEY"
}

response = requests.get(url, headers=headers)
data = response.json()
print(data)
```

### JavaScript (Fetch)

```javascript
const url = "https://api.unusualwhales.com/api/stock/{ticker}/net-prem-ticks";
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
