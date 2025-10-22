# Total Insider Buy & Sells

## Endpoint Details

**Path**: `GET /api/market/insider-buy-sells`

**Operation ID**: `PublicApi.MarketController.insider_buy_sells`

**Summary**: Returns total insider buy and sell statistics for the market

**Tags**: market

## Description

Returns the total amount of purchases and sales as well as notional values for insider transactions across the entire market. This endpoint provides a high-level view of insider activity sentiment and can be used to track whether insiders are buying or selling on aggregate.

## Authentication

- **Required**: Yes
- **Type**: API Key
- **Header**: `Authorization: Bearer YOUR_API_KEY`

## Request Parameters

### Query Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| limit | integer | No | 100 | Maximum number of records to return (min: 1) |

## Example Requests

### cURL

```bash
curl -X GET "https://api.unusualwhales.com/api/market/insider-buy-sells?limit=10" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

### Python

```python
import requests

url = "https://api.unusualwhales.com/api/market/insider-buy-sells"
headers = {
    "Authorization": "Bearer YOUR_API_KEY"
}
params = {
    "limit": 10
}

response = requests.get(url, headers=headers, params=params)
data = response.json()
print(data)
```

### JavaScript (Fetch)

```javascript
const url = "https://api.unusualwhales.com/api/market/insider-buy-sells?limit=10";
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
      "filing_date": "string (YYYY-MM-DD)",
      "purchases": "integer",
      "purchases_notional": "string (decimal)",
      "sells": "integer",
      "sells_notional": "string (decimal)"
    }
  ]
}
```

### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| data | array | Array of insider activity records |
| filing_date | string | Date the insider transactions were filed (YYYY-MM-DD format) |
| purchases | integer | Total number of insider purchase transactions |
| purchases_notional | string | Total dollar value of insider purchases |
| sells | integer | Total number of insider sale transactions |
| sells_notional | string | Total dollar value of insider sales (negative value) |

## Example Response

```json
{
  "data": [
    {
      "filing_date": "2025-10-22",
      "purchases": 21,
      "purchases_notional": "3091953.20",
      "sells": 121,
      "sells_notional": "-211058591.8635"
    },
    {
      "filing_date": "2025-10-21",
      "purchases": 49,
      "purchases_notional": "7751037.1373",
      "sells": 168,
      "sells_notional": "-435788926.5650"
    },
    {
      "filing_date": "2025-10-20",
      "purchases": 39,
      "purchases_notional": "7436681.5128",
      "sells": 217,
      "sells_notional": "-416761306.3681"
    },
    {
      "filing_date": "2025-10-17",
      "purchases": 40,
      "purchases_notional": "47231139.7142",
      "sells": 516,
      "sells_notional": "-991918973.4169"
    }
  ]
}
```

## Error Responses

| Status Code | Description | Response Body |
|-------------|-------------|---------------|
| 400 | Bad Request | `{"error": "Invalid parameters"}` |
| 401 | Unauthorized | `{"error": "Invalid API key"}` |
| 422 | Unprocessable Entity | `{"error": "Invalid limit parameter"}` |
| 500 | Internal Server Error | `{"error": "Server error"}` |

## Rate Limiting

Standard API rate limits apply.

## Notes

- Data is aggregated by filing date (when insider transactions are filed with the SEC)
- Sells are represented as negative values
- The buy/sell ratio can indicate market sentiment from insiders perspective
- When sells significantly exceed purchases, it may indicate insider caution
- When purchases exceed sells, it may indicate insider confidence
- Notional values are in dollars and can be very large; returned as strings to preserve precision
- Results are returned in reverse chronological order (most recent first)
- The limit parameter controls how many days of data are returned

## Related Endpoints

- [/api/insider/transactions](../insider/transactions.md) - Detailed insider transaction records
- [/api/insider/{ticker}/ticker-flow](../insider/ticker-flow.md) - Insider flow for specific ticker
- [/api/insider/{sector}/sector-flow](../insider/sector-flow.md) - Insider flow by sector

## Validation Results

**Tested**: Yes

**Test Date**: 2025-10-22

**Status**: Working

**Notes**: Endpoint returns insider activity statistics aggregated across the entire market by filing date. Data shows both purchase and sell activity with notional values.

**Response Time**: < 1 second

**Sample Data**:
- Recent dates include buy/sell transaction counts and values
- Shows insider confidence/concern trends over time

**Test Command**:
```bash
curl -s "https://api.unusualwhales.com/api/market/insider-buy-sells?limit=10" \
  -H "Authorization: Bearer YOUR_API_KEY"
```
