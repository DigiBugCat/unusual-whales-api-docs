# Stock Screener

## Endpoint Details

**Path**: `GET /api/screener/stocks`

**Operation ID**: `PublicApi.ScreenerController.stock_screener`

**Summary**: Stock Screener

**Tags**: screener

## Description

A comprehensive stock screener endpoint to screen the market for stocks by a variety of filter options. This is a powerful tool for identifying stocks based on technical indicators, options metrics, volatility, and other fundamental characteristics. See the [Stock Screener](https://unusualwhales.com) for an example implementation.

## Authentication

- **Required**: Yes
- **Type**: API Key
- **Header**: `Authorization: Bearer YOUR_API_KEY`

## Request Parameters

### Path Parameters

None

### Query Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ticker | string | No | Filter by specific ticker symbol |
| limit | integer | No | Number of results to return (default: 50, max: 500) |
| offset | integer | No | Pagination offset |
| sector | string | No | Filter by sector (Technology, Healthcare, Energy, etc.) |
| min_price | number | No | Minimum stock price |
| max_price | number | No | Maximum stock price |
| min_market_cap | number | No | Minimum market capitalization |
| max_market_cap | number | No | Maximum market capitalization |
| min_volume | integer | No | Minimum average daily volume |
| min_iv_rank | number | No | Minimum IV rank |
| max_iv_rank | number | No | Maximum IV rank |
| min_iv30d | number | No | Minimum 30-day implied volatility |
| max_iv30d | number | No | Maximum 30-day implied volatility |
| implied_move_filter | number | No | Filter by implied move percentage |
| put_call_ratio_min | number | No | Minimum put/call ratio |
| put_call_ratio_max | number | No | Maximum put/call ratio |
| sort_by | string | No | Field to sort results (price, volume, iv_rank, market_cap, etc.) |
| order | string | No | Sort order (asc, desc) |

See OpenAPI spec for complete list of 66+ available filter parameters.

### Request Body

None

## Example Requests

### cURL

```bash
# Get stocks with high IV rank
curl -X GET "https://api.unusualwhales.com/api/screener/stocks?limit=10&min_iv_rank=70" \
  -H "Authorization: Bearer YOUR_API_KEY"

# Screen for high volatility tech stocks
curl -X GET "https://api.unusualwhales.com/api/screener/stocks?sector=Technology&min_iv30d=0.25&limit=20" \
  -H "Authorization: Bearer YOUR_API_KEY"

# Find high volume stocks with elevated IV
curl -X GET "https://api.unusualwhales.com/api/screener/stocks?min_volume=5000000&min_iv_rank=60&limit=50" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

### Python

```python
import requests

url = "https://api.unusualwhales.com/api/screener/stocks"
headers = {
    "Authorization": "Bearer YOUR_API_KEY"
}
params = {
    "limit": 25,
    "min_iv_rank": 50,
    "min_volume": 1000000,
    "sort_by": "iv_rank"
}

response = requests.get(url, headers=headers, params=params)
data = response.json()
print(data)
```

### JavaScript (Fetch)

```javascript
const url = "https://api.unusualwhales.com/api/screener/stocks?limit=25&min_iv_rank=50&sort_by=iv_rank";
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
      "ticker": "SPY",
      "full_name": "SPDR S&P 500 ETF",
      "date": "2025-10-22",
      "close": "667.8",
      "low": "663.3",
      "high": "672",
      "week_52_low": "481.80",
      "week_52_high": "673.95",
      "marketcap": "681311007065",
      "sector": null,
      "issue_type": "ETF",
      "volatility": "0.152000",
      "iv_rank": "17.0535",
      "iv30d": "0.152000",
      "implied_move": "19.768000",
      "implied_move_perc": "0.029000",
      "put_call_ratio": "1.2320424113341436",
      "call_volume": 4645362,
      "put_volume": 5723283,
      "call_open_interest": 4719155,
      "put_open_interest": 12331058,
      "total_open_interest": 17050213,
      "stock_volume": 74194787,
      "avg30_volume": "78403939.227272727273"
    }
  ]
}
```

### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| ticker | string | Stock ticker symbol |
| full_name | string | Full company name |
| date | string | Date of the data (YYYY-MM-DD) |
| close | string | Current closing price |
| low | string | Daily low price |
| high | string | Daily high price |
| week_52_low | string | 52-week low price |
| week_52_high | string | 52-week high price |
| marketcap | string | Market capitalization |
| sector | string | Sector classification |
| issue_type | string | Type (ETF, Stock, etc.) |
| volatility | string | Current volatility |
| iv_rank | string | Implied volatility rank (0-100) |
| iv30d | string | 30-day implied volatility |
| implied_move | string | Expected price move based on options pricing |
| implied_move_perc | string | Implied move as percentage |
| put_call_ratio | string | Ratio of put to call open interest |
| call_volume | integer | Daily call option volume |
| put_volume | integer | Daily put option volume |
| call_open_interest | integer | Call option open interest |
| put_open_interest | integer | Put option open interest |
| total_open_interest | integer | Total option open interest |
| stock_volume | integer | Stock trading volume |
| avg30_volume | string | 30-day average volume |

## Example Response

See above - single stock example with all major fields populated.

## Error Responses

| Status Code | Description | Response Body |
|-------------|-------------|---------------|
| 400 | Bad Request | `{"error": "Invalid filter parameters"}` |
| 401 | Unauthorized | `{"error": "Invalid API key"}` |
| 422 | Unprocessable Entity | `{"error": "Invalid parameter format"}` |
| 500 | Internal Server Error | `{"error": "Server error"}` |

## Rate Limiting

The API enforces rate limits on requests. Standard tier allows reasonable request frequency. Check response headers for rate limit information. Complex queries with many filters may use more rate limit points.

## Notes

- This endpoint supports 66+ filter parameters for precise screening
- All price and financial metrics are returned as string values for precision
- IV Rank ranges from 0-100, with higher values indicating higher volatility relative to history
- Implied move represents the expected price range based on options pricing
- Put/call ratio helps identify sentiment and positioning
- Data is updated daily after market close
- Pagination supported via limit and offset parameters
- Results can be sorted by any returned field
- Particularly useful for options traders analyzing volatility and positioning
- Default limit is 50 results, maximum is 500

## Related Endpoints

- `/api/screener/analysts` - Get analyst ratings
- `/api/screener/option-contracts` - Screen options contracts

## Validation Results

**Tested**: Yes

**Test Date**: 2025-10-22

**Status**: Working

**Notes**: Endpoint successfully returns stock screener data for SPY. Response includes comprehensive options and volatility metrics. All calculated fields present and valid. Pagination working correctly. Filter parameters properly applied. No rate limit issues encountered.
