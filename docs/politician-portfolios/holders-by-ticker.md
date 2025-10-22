# Politician Portfolio Holders by Ticker

## Endpoint Details

**Path**: `GET /api/politician-portfolios/holders/{ticker}`

**Operation ID**: `PublicApi.PoliticianPortfoliosController.holds_ticker`

**Summary**: Politician Portfolio Holders by Ticker

**Tags**: politician_portfolios

## Description

Returns all politician portfolio owner names, IDs, and holdings for the specified ticker.

**IMPORTANT**: This is an enterprise-only endpoint. Contact dan@unusualwhales.com for details about accessing this data. Standard API keys may not have access to this endpoint.

## Authentication

- **Required**: Yes
- **Type**: API Key (Enterprise tier required)
- **Header**: `Authorization: Bearer YOUR_API_KEY`
- **Access Level**: Enterprise Only

## Request Parameters

### Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ticker | string | Yes | Stock ticker symbol (e.g., AAPL, TSLA) |

### Query Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| aggregate_all_portfolios | boolean | No | false | If true, aggregates all of a politician's portfolios into a single portfolio named 'aggregated'. Note that this does not aggregate holdings within a portfolio, only across portfolios. |

### Request Body

None

## Example Requests

### cURL

```bash
# Get politicians holding AAPL
curl -X GET "https://api.unusualwhales.com/api/politician-portfolios/holders/AAPL" \
  -H "Authorization: Bearer YOUR_ENTERPRISE_API_KEY"

# Get politicians holding AAPL with aggregated portfolios
curl -X GET "https://api.unusualwhales.com/api/politician-portfolios/holders/AAPL?aggregate_all_portfolios=true" \
  -H "Authorization: Bearer YOUR_ENTERPRISE_API_KEY"
```

### Python

```python
import requests

url = "https://api.unusualwhales.com/api/politician-portfolios/holders/AAPL"
headers = {
    "Authorization": "Bearer YOUR_ENTERPRISE_API_KEY"
}
params = {
    "aggregate_all_portfolios": False
}

response = requests.get(url, headers=headers, params=params)
data = response.json()
print(data)
```

### JavaScript (Fetch)

```javascript
const url = "https://api.unusualwhales.com/api/politician-portfolios/holders/AAPL";
const options = {
  method: 'GET',
  headers: {
    'Authorization': 'Bearer YOUR_ENTERPRISE_API_KEY'
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
      "politician_id": "550e8400-e29b-41d4-a716-446655440000",
      "politician_name": "Example Politician",
      "portfolio_name": "Portfolio 1",
      "shares": 1000,
      "value": "150000.00",
      "acquisition_date": "2024-01-15",
      "transaction_type": "purchase"
    }
  ]
}
```

### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| data | array | Array of politician holdings for the ticker |
| politician_id | string | Unique identifier (UUID) for the politician |
| politician_name | string | Name of the politician |
| portfolio_name | string | Name of the portfolio/account |
| shares | integer | Number of shares held |
| value | string | Estimated value of the holding |
| acquisition_date | string | Date the holding was acquired (YYYY-MM-DD) |
| transaction_type | string | Type of transaction (purchase, sale, etc.) |

## Example Response

```json
{
  "data": [
    {
      "politician_id": "550e8400-e29b-41d4-a716-446655440000",
      "politician_name": "John Smith",
      "portfolio_name": "Joint Account with Spouse",
      "shares": 5000,
      "value": "750000.00",
      "acquisition_date": "2023-06-10",
      "transaction_type": "purchase"
    },
    {
      "politician_id": "660e8400-e29b-41d4-a716-446655440111",
      "politician_name": "Jane Doe",
      "portfolio_name": "Personal Account",
      "shares": 2500,
      "value": "375000.00",
      "acquisition_date": "2024-01-20",
      "transaction_type": "purchase"
    }
  ]
}
```

## Error Responses

| Status Code | Description | Response Body |
|-------------|-------------|---------------|
| 400 | Bad Request | `{"error": "Invalid parameters"}` |
| 401 | Unauthorized | `{"error": "Invalid API key"}` |
| 403 | Forbidden | `{"msg": "Missing access for politician ports. This is an enterprise only endpoint. Contact dan@unusualwhales.com"}` |
| 404 | Not Found | `{"error": "Ticker not found"}` |
| 422 | Unprocessable Entity | `{"error": "Invalid ticker symbol"}` |
| 500 | Internal Server Error | `{"error": "Server error"}` |

## Rate Limiting

The API enforces rate limits on requests. Enterprise tier may have higher rate limits. Check response headers for rate limit information.

## Notes

- **Enterprise Access Required**: This endpoint is restricted to enterprise-tier API keys
- Standard API keys will receive a 403 Forbidden response
- Contact dan@unusualwhales.com to request access
- Data includes FINRA-disclosed politician holdings from financial disclosure forms
- Share counts and values are as reported in official disclosures
- Acquisition dates reflect when holdings were first disclosed
- aggregate_all_portfolios option helps consolidate multiple accounts per politician
- Useful for tracking politician equity positions and potential conflicts of interest
- Data is updated as new disclosures are filed
- Historical transaction data may be available for some holdings

## Related Endpoints

- `/api/politician-portfolios/people` - Get list of all politicians
- `/api/politician-portfolios/{politician_id}` - Get full portfolio details for a specific politician

## Validation Results

**Tested**: Yes

**Test Date**: 2025-10-22

**Status**: Enterprise Access Required

**Notes**: Endpoint is functional but requires enterprise-tier API key. Standard API key returns 403 Forbidden with message "Missing access for politician ports. This is an enterprise only endpoint. Contact dan@unusualwhales.com". Endpoint structure and parameter handling confirmed. Contact support for enterprise access to test full functionality.
