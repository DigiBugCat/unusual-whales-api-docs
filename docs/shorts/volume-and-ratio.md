# Short Volume and Ratio

## Endpoint Details

**Path**: `GET /api/shorts/{ticker}/volume-and-ratio`

**Operation ID**: `PublicApi.ShortController.short_volume_and_ratio`

**Summary**: Short Volume and Ratio

**Tags**: shorts

## Description

Returns short volume and short ratio data for a ticker. This endpoint provides information about the daily short volume traded and the ratio of short volume to total volume, helping identify days with heavy short selling activity.

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
curl -X GET "https://api.unusualwhales.com/api/shorts/AAPL/volume-and-ratio" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

### Python

```python
import requests

url = "https://api.unusualwhales.com/api/shorts/AAPL/volume-and-ratio"
headers = {
    "Authorization": "Bearer YOUR_API_KEY"
}

response = requests.get(url, headers=headers)
data = response.json()
print(data)
```

### JavaScript (Fetch)

```javascript
const url = "https://api.unusualwhales.com/api/shorts/AAPL/volume-and-ratio";
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
  "si": [
    {
      "total_volume": 19597053,
      "market_date": "2025-10-21",
      "short_volume": 9801022,
      "short_volume_ratio": "0.5001273405751364758772658318"
    }
  ]
}
```

### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| si | array | Array of daily short volume records |
| market_date | string | Trading date in YYYY-MM-DD format |
| total_volume | integer | Total trading volume for the day |
| short_volume | integer | Volume sold short during the day |
| short_volume_ratio | string | Short volume as ratio of total volume (0.0-1.0) |

## Example Response

```json
{
  "si": [
    {
      "total_volume": 19597053,
      "market_date": "2025-10-21",
      "short_volume": 9801022,
      "short_volume_ratio": "0.5001273405751364758772658318"
    },
    {
      "total_volume": 35139387,
      "market_date": "2025-10-20",
      "short_volume": 16591704,
      "short_volume_ratio": "0.4721682822753851682159395666"
    },
    {
      "total_volume": 17617168,
      "market_date": "2025-10-17",
      "short_volume": 7857807,
      "short_volume_ratio": "0.4460312236336736982924837863"
    }
  ]
}
```

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

- Data includes recent trading days, typically showing last 20-30 days of history
- short_volume_ratio is returned as a decimal string with high precision
- A ratio above 0.50 (50%) indicates more than half the volume was sold short
- Data is updated daily after market close
- Useful for identifying days with unusually high short selling pressure
- Total short volume is reported by FINRA and publicly available
- High short volume ratios can indicate institutional short selling or related activity
- Particularly useful when combined with price action analysis

## Related Endpoints

- `/api/shorts/{ticker}/data` - Get current short borrow rates
- `/api/shorts/{ticker}/ftds` - Get failures to deliver data
- `/api/shorts/{ticker}/interest-float` - Get short interest and float data
- `/api/shorts/{ticker}/volumes-by-exchange` - Get short volumes by exchange

## Validation Results

**Tested**: Yes

**Test Date**: 2025-10-22

**Status**: Working

**Notes**: Endpoint returns daily short volume data for AAPL. Response includes multiple recent trading days with accurate volume calculations. Short volume ratios show appropriate range (0.35-0.50). Data is consistently updated with latest market information.
