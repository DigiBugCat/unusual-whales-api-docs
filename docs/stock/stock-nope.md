# Nope

## Endpoint Details

**Path**: `GET /api/stock/{ticker}/nope`

**Operation ID**: `PublicApi.TickerController.nope`

**Summary**: Nope

**Category**: stock

## Description

Returns the tickers NOPE for the given market day broken down per minute.

NOPE is the Net Options Pricing Effect, which tracks the intraday net delta of any ticker, but most research has been done on indexes.
It functions under 2 assumptions:
1) MM's take short side of any call or put traded during the day
2) MM's try to minimize risk by dynamically hedging their delta-gamma exposure, and do so by buying/shorting the underlying stock in proportion to the total net delta being tradedBased on these assumptions, options trading in large amounts (re: very liquid tickers) can potentially drive the price of the underlying, to a certain extent. Large movements might exacerbate this real time hedging, and drive price movements further in respective directions.

In short, NOPE represents a best-estimate of expected number of shares to be hedged at any given time, and will show a general expected direction on the underlying

The original NOPE calculation was based on the following formula:
`NOPE = (Call Delta - Put Delta) / Stock Volume`
where call/put delta is obtained by multiplying each chains volume with its latest delta and then summing those values up.

`NOPE fill` on the other hand is based on the delta at the time of the transaction

Date must be the current or a past date. If no date is given, returns data for the current/last market day.


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
curl -X GET "https://api.unusualwhales.com/api/stock/{ticker}/nope" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

### Python

```python
import requests

url = "https://api.unusualwhales.com/api/stock/{ticker}/nope"
headers = {
    "Authorization": "Bearer YOUR_API_KEY"
}

response = requests.get(url, headers=headers)
data = response.json()
print(data)
```

### JavaScript (Fetch)

```javascript
const url = "https://api.unusualwhales.com/api/stock/{ticker}/nope";
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
