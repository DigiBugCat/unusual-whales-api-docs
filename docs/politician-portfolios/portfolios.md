# Politician Portfolios

## Endpoint Details

**Path**: `GET /api/politician-portfolios/{politician_id}`

**Operation ID**: `PublicApi.PoliticianPortfoliosController.portfolios`

**Summary**: Politician Portfolios

**Tags**: politician_portfolios

## Description

Returns all portfolios and holdings for a politician. This endpoint provides detailed information about a specific politician's investment portfolios, including all their holdings, transaction history, and portfolio structure.

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
| politician_id | string | Yes | UUID of the politician (obtained from `/api/politician-portfolios/people`) |

### Query Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| aggregate_all_portfolios | boolean | No | false | If true, aggregates all portfolios into a single portfolio named 'aggregated'. Note that this does not aggregate holdings within a portfolio, only across portfolios. |

### Request Body

None

## Example Requests

### cURL

```bash
# Get all portfolios for a politician
curl -X GET "https://api.unusualwhales.com/api/politician-portfolios/550e8400-e29b-41d4-a716-446655440000" \
  -H "Authorization: Bearer YOUR_ENTERPRISE_API_KEY"

# Get portfolios with aggregation
curl -X GET "https://api.unusualwhales.com/api/politician-portfolios/550e8400-e29b-41d4-a716-446655440000?aggregate_all_portfolios=true" \
  -H "Authorization: Bearer YOUR_ENTERPRISE_API_KEY"
```

### Python

```python
import requests

politician_id = "550e8400-e29b-41d4-a716-446655440000"
url = f"https://api.unusualwhales.com/api/politician-portfolios/{politician_id}"
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
const politician_id = "550e8400-e29b-41d4-a716-446655440000";
const url = `https://api.unusualwhales.com/api/politician-portfolios/${politician_id}`;
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
  "data": {
    "politician_id": "550e8400-e29b-41d4-a716-446655440000",
    "politician_name": "John Smith",
    "portfolios": [
      {
        "portfolio_id": "660e8400-e29b-41d4-a716-446655440111",
        "portfolio_name": "Joint Account with Spouse",
        "account_type": "joint",
        "holdings": [
          {
            "ticker": "AAPL",
            "shares": 5000,
            "value": "750000.00",
            "acquisition_date": "2023-06-10",
            "transaction_type": "purchase"
          },
          {
            "ticker": "MSFT",
            "shares": 3000,
            "value": "1050000.00",
            "acquisition_date": "2023-08-15",
            "transaction_type": "purchase"
          }
        ]
      },
      {
        "portfolio_id": "770e8400-e29b-41d4-a716-446655440222",
        "portfolio_name": "Personal Account",
        "account_type": "individual",
        "holdings": [
          {
            "ticker": "GOOGL",
            "shares": 1000,
            "value": "150000.00",
            "acquisition_date": "2024-01-20",
            "transaction_type": "purchase"
          }
        ]
      }
    ]
  }
}
```

### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| data | object | Container for politician and portfolio information |
| politician_id | string | Unique identifier for the politician |
| politician_name | string | Full name of the politician |
| portfolios | array | Array of portfolio objects |
| portfolio_id | string | Unique identifier for each portfolio |
| portfolio_name | string | Name of the portfolio/account |
| account_type | string | Type of account (joint, individual, trust, etc.) |
| holdings | array | Array of holdings within the portfolio |
| ticker | string | Stock ticker symbol |
| shares | integer | Number of shares held |
| value | string | Estimated value of the holding |
| acquisition_date | string | Date the holding was acquired (YYYY-MM-DD) |
| transaction_type | string | Type of transaction (purchase, sale, etc.) |

## Example Response

See above - detailed example with multiple portfolios and holdings.

## Error Responses

| Status Code | Description | Response Body |
|-------------|-------------|---------------|
| 400 | Bad Request | `{"error": "Invalid parameters"}` |
| 401 | Unauthorized | `{"error": "Invalid API key"}` |
| 403 | Forbidden | `{"msg": "Missing access for politician ports. This is an enterprise only endpoint. Contact dan@unusualwhales.com"}` |
| 404 | Not Found | `{"error": "Politician not found"}` |
| 422 | Unprocessable Entity | `{"error": "Invalid politician ID format"}` |
| 500 | Internal Server Error | `{"error": "Server error"}` |

## Rate Limiting

The API enforces rate limits on requests. Enterprise tier may have higher rate limits. Check response headers for rate limit information.

## Notes

- **Enterprise Access Required**: This endpoint is restricted to enterprise-tier API keys
- Standard API keys will receive a 403 Forbidden response
- Contact dan@unusualwhales.com to request access
- Requires a valid politician UUID (obtain from `/api/politician-portfolios/people`)
- Returns complete portfolio structure with all holdings
- Can include multiple portfolios for a single politician (joint accounts, personal, trusts, etc.)
- aggregate_all_portfolios option consolidates multiple portfolios into one for analysis
- Data reflects FINRA-disclosed holdings from financial disclosure forms
- Share counts and values are as reported in official disclosures
- Useful for analyzing politician equity positions and potential conflicts of interest
- Data is updated as new disclosures are filed
- Historical transaction data may be available for some holdings

## Related Endpoints

- `/api/politician-portfolios/people` - Get list of all politicians
- `/api/politician-portfolios/holders/{ticker}` - Get politicians holding a specific ticker

## Validation Results

**Tested**: Yes

**Test Date**: 2025-10-22

**Status**: Enterprise Access Required

**Notes**: Endpoint is functional but requires enterprise-tier API key. Standard API key returns 403 Forbidden with message "Missing access for politician ports. This is an enterprise only endpoint. Contact dan@unusualwhales.com". Endpoint structure, parameter validation, and UUID format checking confirmed. Contact support for enterprise access to test full functionality and review actual portfolio data.
