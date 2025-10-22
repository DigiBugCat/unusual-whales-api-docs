# Total Options Volume

## Endpoint Details

**Path**: `GET /api/market/total-options-volume`

**Operation ID**: `PublicApi.MarketController.total_options_volume`

**Summary**: Returns total options volume and premium for the market

**Tags**: market

## Description

Returns the total options volume and premium for all trade executions that happened on a given trading date. This provides an overview of the overall options market activity and can be used to build a comprehensive market options overview.

## Authentication

- **Required**: Yes
- **Type**: API Key
- **Header**: `Authorization: Bearer YOUR_API_KEY`

## Request Parameters

### Query Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| limit | integer | No | 1 | Maximum number of days to return (max: 500, min: 1) |

## Example Requests

### cURL

```bash
curl -X GET "https://api.unusualwhales.com/api/market/total-options-volume?limit=1" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

### Python

```python
import requests

url = "https://api.unusualwhales.com/api/market/total-options-volume"
headers = {
    "Authorization": "Bearer YOUR_API_KEY"
}
params = {
    "limit": 1
}

response = requests.get(url, headers=headers, params=params)
data = response.json()
print(data)
```

### JavaScript (Fetch)

```javascript
const url = "https://api.unusualwhales.com/api/market/total-options-volume?limit=1";
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
      "date": "string (YYYY-MM-DD)",
      "put_volume": "integer",
      "call_volume": "integer",
      "put_premium": "string (decimal)",
      "call_premium": "string (decimal)"
    }
  ]
}
```

### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| data | array | Array of daily options volume data |
| date | string | Trading date in YYYY-MM-DD format |
| put_volume | integer | Total put option volume for the day |
| call_volume | integer | Total call option volume for the day |
| put_premium | string | Total dollar value of put premium traded |
| call_premium | string | Total dollar value of call premium traded |

## Example Response

```json
{
  "data": [
    {
      "date": "2025-10-22",
      "put_volume": 28514402,
      "call_volume": 39934165,
      "put_premium": "13761692269.70",
      "call_premium": "20244470412.33"
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

- Premium values are in dollars and can be very large
- Call/put ratio can indicate market sentiment (calls > puts often indicates bullish sentiment)
- This endpoint provides high-level market overview rather than individual contract data
- Data is aggregated across all option contracts for the given date(s)
- Premium represents the total dollar value of options transactions, not just buyer cost
- The limit parameter allows retrieving multiple days of historical data
- Default limit of 1 returns just the most recent trading day

## Related Endpoints

- [/api/market/market-tide](./market-tide.md) - Minute-by-minute market sentiment
- [/api/market/sector-etfs](./sector-etfs.md) - Sector-level options volume
- [/api/market/top-net-impact](./top-net-impact.md) - Individual stock options impact

## Validation Results

**Tested**: Yes

**Test Date**: 2025-10-22

**Status**: Working

**Notes**: Endpoint returns daily options volume and premium statistics. On October 22, 2025, the market saw approximately 68.4M total options volume with calls representing 57% of volume.

**Response Time**: < 1 second

**Sample Data**:
- Total Call Volume: 39,934,165 contracts
- Total Put Volume: 28,514,402 contracts
- Total Premium: 34 billion+ (calls + puts)

**Test Command**:
```bash
curl -s "https://api.unusualwhales.com/api/market/total-options-volume?limit=1" \
  -H "Authorization: Bearer 5d1ec006-49f0-4a2a-90ae-5176c72425e3"
```
