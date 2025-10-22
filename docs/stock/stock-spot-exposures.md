# Spot GEX exposures per 1min

## Endpoint Details

**Path**: `GET /api/stock/{ticker}/spot-exposures`

**Operation ID**: `PublicApi.TickerController.spot_exposures_one_minute`

**Summary**: Spot GEX exposures per 1min

**Category**: stock

## Description

Returns the spot GEX exposures for the given ticker per minute.

Spot GEX is the assumed $ value of the given greek (ie. gamma) exposure that market makers need to hedge per 1% change of the underlying stock's price movement. A positive value is long and a negative value is short.

Investors and large funds lower risk and protect their money by selling calls and buying puts. Market makers provide the liquidity to facilitate these trades.

GEX assumes that market makers are part of every transaction and that the bulk of their transactions are buying calls and selling puts to investors hedging their portfolios.

If a market maker has one contract open with a gamma value of 0.05, then if the underlying stock price moves by 1%, that market maker is exposed to $[0.05 * 100 shares * 0.01 * stock price * underlying parameter of the greek variable (for gamma this variable is the stock price)]. The total market maker spot exposure is calculated by summing up the spot exposure of all open contracts determined by the daily open interest or by volume.

Market makers profit from the bid-ask spreads and as such, they constantly gamma hedge (they buy and sell shares to keep their positions delta neutral).

Long call positions are positive gamma - as the stock price increases and delta rises (approaches 1), market makers hedge by selling shares, and they buy shares if the stock price decreases and delta falls.

Short put positions are negative gamma - as the stock price increases and delta falls (approaches -1), market makers hedge by buying shares, and they sell shares if the stock price decreases and delta rises.

As such, in the event of large positive gamma, volatility is suppressed as market makers will hedge by buying as the stock price decreases and selling as the stock price increases. And in the event of large negative gamma, volatility is amplified as market makers will hedge by buying as the stock price increases and selling as the stock price decreases.


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
curl -X GET "https://api.unusualwhales.com/api/stock/{ticker}/spot-exposures" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

### Python

```python
import requests

url = "https://api.unusualwhales.com/api/stock/{ticker}/spot-exposures"
headers = {
    "Authorization": "Bearer YOUR_API_KEY"
}

response = requests.get(url, headers=headers)
data = response.json()
print(data)
```

### JavaScript (Fetch)

```javascript
const url = "https://api.unusualwhales.com/api/stock/{ticker}/spot-exposures";
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
