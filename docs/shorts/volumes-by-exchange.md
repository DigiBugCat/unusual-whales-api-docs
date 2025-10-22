# Short Volume by Exchange

## Endpoint Details

**Path**: `GET /api/shorts/{ticker}/volumes-by-exchange`

**Operation ID**: `PublicApi.ShortController.short_volume_by_exchange`

**Summary**: Short Volume by Exchange

**Tags**: shorts

## Description

Returns short volume data broken down by exchange for a ticker. This endpoint shows which exchanges (market centers) are contributing to the overall short volume, useful for understanding order flow and market microstructure.

## Authentication

- **Required**: Yes
- **Type**: API Key
- **Header**: `Authorization: Bearer YOUR_API_KEY`

## Request Parameters

### Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ticker | string | Yes | Stock ticker symbol (e.g., AAPL, TSLA) |

### Query Parameters

None

### Request Body

None

## Example Requests

### cURL

```bash
curl -X GET "https://api.unusualwhales.com/api/shorts/AAPL/volumes-by-exchange" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

### Python

```python
import requests

url = "https://api.unusualwhales.com/api/shorts/AAPL/volumes-by-exchange"
headers = {
    "Authorization": "Bearer YOUR_API_KEY"
}

response = requests.get(url, headers=headers)
data = response.json()
print(data)
```

### JavaScript (Fetch)

```javascript
const url = "https://api.unusualwhales.com/api/shorts/AAPL/volumes-by-exchange";
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
      "date": "2025-10-21",
      "total_volume": 19597053,
      "market_center": "B,Q,N",
      "short_volume": 9801022,
      "exchange_name": "FINRA CNMS"
    }
  ]
}
```

### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| data | array | Array of short volume records by exchange |
| date | string | Trading date in YYYY-MM-DD format |
| total_volume | integer | Total trading volume on this exchange for the day |
| market_center | string | Comma-separated list of market center codes (B=NASDAQ, Q=NASDAQ, N=NYSE, etc.) |
| short_volume | integer | Volume sold short on this exchange |
| exchange_name | string | Full name of the exchange or reporting organization |

## Example Response

```json
{
  "data": [
    {
      "date": "2025-10-21",
      "total_volume": 19597053,
      "market_center": "B,Q,N",
      "short_volume": 9801022,
      "exchange_name": "FINRA CNMS"
    },
    {
      "date": "2025-10-20",
      "total_volume": 35139387,
      "market_center": "B,Q,N",
      "short_volume": 16591704,
      "exchange_name": "FINRA CNMS"
    },
    {
      "date": "2025-10-17",
      "total_volume": 17617168,
      "market_center": "B,Q,N",
      "short_volume": 7857807,
      "exchange_name": "FINRA CNMS"
    }
  ]
}
```

## Market Center Codes

| Code | Exchange/Center |
|------|-----------------|
| N | NYSE |
| Q | NASDAQ |
| B | NASDAQ OMX BX |
| P | NYSE MKT (formerly AMEX) |
| A | NYSE MKT |
| X | NASDAQ OMX PSX |
| Z | BATS |
| J | Direct Edge A |
| K | Direct Edge X |
| M | NASDAQ Stock Exchange |

## Error Responses

| Status Code | Description | Response Body |
|-------------|-------------|---------------|
| 400 | Bad Request | `{"error": "Invalid parameters"}` |
| 401 | Unauthorized | `{"error": "Invalid API key"}` |
| 404 | Not Found | `{"error": "Ticker not found"}` |
| 422 | Unprocessable Entity | `{"error": "Invalid ticker symbol"}` |
| 500 | Internal Server Error | `{"error": "Server error"}` |

## Rate Limiting

The API enforces rate limits on requests. Standard tier allows reasonable request frequency. Check response headers for rate limit information.

## Notes

- Data is aggregated from FINRA CNMS and individual exchange reporting
- Market center codes identify which exchanges contributed to the volume
- Multiple exchanges may report combined (e.g., "B,Q,N" for NASDAQ OMX BX, NASDAQ, and NYSE)
- Data is updated daily after market close
- FINRA CNMS (Consolidated National Market System) is the primary reporting source
- Useful for identifying order flow imbalances between exchanges
- Can help detect if shorting is concentrated on specific exchanges or markets
- Data reflects official FINRA reportings

## Related Endpoints

- `/api/shorts/{ticker}/data` - Get current short borrow rates
- `/api/shorts/{ticker}/ftds` - Get failures to deliver data
- `/api/shorts/{ticker}/interest-float` - Get short interest and float data
- `/api/shorts/{ticker}/volume-and-ratio` - Get short volume and ratio data

## Validation Results

**Tested**: Yes

**Test Date**: 2025-10-22

**Status**: Working

**Notes**: Endpoint successfully returns short volume data by exchange for AAPL. Response includes recent trading days with FINRA CNMS reporting. Market centers properly identified. Data consistent with overall short volume metrics from other endpoints.
