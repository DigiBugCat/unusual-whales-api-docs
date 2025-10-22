# Greek Exposure

## Endpoint Details

**Path**: `GET /api/stock/{ticker}/greek-exposure`

**Operation ID**: `PublicApi.TickerController.greek_exposure`

**Summary**: Greek Exposure

**Category**: stock

## Description

Greek Exposure is the assumed greek exposure that market makers are exposed to.

The most popular greek exposure is gamma exposure (GEX).

Investors and large funds lower risk and protect their money by selling calls and buying puts. Market makers provide the liquidity to facilitate these trades.

GEX assumes that market makers are part of every transaction and that the bulk of their transactions are buying calls and selling puts to investors hedging their portfolios.

If a market maker has one contract open with a gamma value of 0.05, then that market maker is exposed to 0.05 * [100 shares] of gamma. The total market maker exposure is calculated by summing up the exposure values of all open contracts determined by the daily open interest.

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
| timeframe | string | No |  |

## Example Requests

### cURL

```bash
curl -X GET "https://api.unusualwhales.com/api/stock/{ticker}/greek-exposure" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

### Python

```python
import requests

url = "https://api.unusualwhales.com/api/stock/{ticker}/greek-exposure"
headers = {
    "Authorization": "Bearer YOUR_API_KEY"
}

response = requests.get(url, headers=headers)
data = response.json()
print(data)
```

### JavaScript (Fetch)

```javascript
const url = "https://api.unusualwhales.com/api/stock/{ticker}/greek-exposure";
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
