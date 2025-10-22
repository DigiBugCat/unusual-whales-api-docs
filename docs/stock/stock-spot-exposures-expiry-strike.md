# Spot GEX exposures by strike & expiry

## Endpoint Details

**Path**: `GET /api/stock/{ticker}/spot-exposures/expiry-strike`

**Operation ID**: `PublicApi.TickerController.spot_exposures_by_strike_expiry_v2`

**Summary**: Spot GEX exposures by strike & expiry

**Category**: stock

## Description

Returns the most recent spot GEX exposures across all strikes for the given ticker & expiration on a given date. Calculated either with open interest or with volume.

Data is available since 2025-01-16.

[Click here for the spot docs](https://api.unusualwhales.com/docs#/operations/PublicApi.TickerController.spot_exposures_by_strike)


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
| expirations[] | string | Yes |  |
| date | string | No |  |
| limit | string | No |  |
| page | string | No |  |
| min_strike | string | No |  |
| max_strike | string | No |  |
| min_dte | string | No |  |
| max_dte | string | No |  |

## Example Requests

### cURL

```bash
curl -X GET "https://api.unusualwhales.com/api/stock/{ticker}/spot-exposures/expiry-strike" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

### Python

```python
import requests

url = "https://api.unusualwhales.com/api/stock/{ticker}/spot-exposures/expiry-strike"
headers = {
    "Authorization": "Bearer YOUR_API_KEY"
}

response = requests.get(url, headers=headers)
data = response.json()
print(data)
```

### JavaScript (Fetch)

```javascript
const url = "https://api.unusualwhales.com/api/stock/{ticker}/spot-exposures/expiry-strike";
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
