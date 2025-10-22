# Insider Transactions

## Endpoint Details

**Path**: `GET /api/insider/transactions`

**Operation ID**: `PublicApi.InsiderController.transactions`

**Summary**: Transactions

**Tags**: insider

## Description

Returns the latest insider transactions. By default, all transactions that have been filled by the same person on the same day with the same trade code are aggregated into a single row. This endpoint provides comprehensive data on insider buying and selling activity across all securities.

## Authentication

- **Required**: Yes
- **Type**: API Key
- **Header**: `Authorization: Bearer YOUR_API_KEY`

## Request Parameters

### Path Parameters

None

### Query Parameters

Multiple query parameters available for filtering (see full specification):

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| limit | integer | No | 100 | Number of transactions to return |
| offset | integer | No | 0 | Pagination offset |
| transaction_code | string | No | - | Filter by transaction code (B, S, etc.) |
| date_from | string | No | - | Filter from date (YYYY-MM-DD) |
| date_to | string | No | - | Filter to date (YYYY-MM-DD) |

### Request Body

Not applicable for this endpoint.

## Example Requests

### cURL

```bash
curl -X GET "https://api.unusualwhales.com/api/insider/transactions?limit=10" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

### Python

```python
import requests

url = "https://api.unusualwhales.com/api/insider/transactions"
headers = {
    "Authorization": "Bearer YOUR_API_KEY"
}
params = {
    "limit": 10,
    "transaction_code": "S"
}

response = requests.get(url, headers=headers, params=params)
data = response.json()
print(data)
```

### JavaScript (Fetch)

```javascript
const url = "https://api.unusualwhales.com/api/insider/transactions?limit=10";
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
      "id": "string (UUID)",
      "ticker": "string",
      "amount": "integer",
      "transactions": "integer",
      "price": "string (decimal)",
      "sector": "string",
      "marketcap": "string (integer)",
      "next_earnings_date": "string (YYYY-MM-DD)",
      "is_s_p_500": "boolean",
      "filing_date": "string (YYYY-MM-DD)",
      "transaction_date": "string (YYYY-MM-DD)",
      "is_director": "boolean",
      "is_officer": "boolean",
      "is_ten_percent_owner": "boolean",
      "reporter_is_public_company": "boolean",
      "stock_price": "string (decimal)",
      "security_title": "string",
      "formtype": "string",
      "transaction_code": "string",
      "is_10b5_1": "boolean",
      "owner_name": "string",
      "officer_title": "string",
      "shares_owned_before": "integer or null",
      "shares_owned_after": "integer or null",
      "ids": ["string (UUID)"]
    }
  ]
}
```

### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| id | string | Unique transaction identifier |
| ticker | string | Stock ticker symbol |
| amount | integer | Transaction amount (positive for buy, negative for sell) |
| transactions | integer | Number of individual transactions aggregated |
| price | string | Transaction price per share |
| sector | string | Company sector |
| marketcap | string | Company market capitalization |
| next_earnings_date | string | Next earnings announcement date |
| is_s_p_500 | boolean | Whether stock is in S&P 500 |
| filing_date | string | SEC filing date |
| transaction_date | string | Actual transaction date |
| is_director | boolean | Whether filer is a director |
| is_officer | boolean | Whether filer is an officer |
| is_ten_percent_owner | boolean | Whether filer owns 10%+ |
| reporter_is_public_company | boolean | Whether reporter is public company |
| stock_price | string | Current stock price |
| security_title | string | Title of security traded |
| formtype | string | SEC form type (4, 144, etc.) |
| transaction_code | string | Code (B=Buy, S=Sell, etc.) |
| is_10b5_1 | boolean | Whether covered by Rule 10b5-1 |
| owner_name | string | Name of insider |
| officer_title | string | Officer title if applicable |
| shares_owned_before | integer | Shares owned before transaction |
| shares_owned_after | integer | Shares owned after transaction |
| ids | array | Array of underlying transaction IDs |

## Example Response

```json
{
  "data": [
    {
      "id": "6e4688de-15dd-41ba-95c1-2b225f13b105",
      "ticker": "UTHR",
      "amount": -4000,
      "transactions": 1,
      "price": "422.1500",
      "sector": "Healthcare",
      "marketcap": "19109452483",
      "next_earnings_date": "2025-10-29",
      "is_s_p_500": false,
      "filing_date": "2025-10-22",
      "transaction_date": "2025-10-22",
      "is_director": true,
      "is_officer": true,
      "is_ten_percent_owner": false,
      "reporter_is_public_company": false,
      "stock_price": "421.64",
      "security_title": null,
      "formtype": "144",
      "transaction_code": "S",
      "is_10b5_1": true,
      "owner_name": "ROTHBLATT MARTINE",
      "officer_title": "Chairperson & CEO",
      "shares_owned_before": null,
      "shares_owned_after": null,
      "ids": ["65f621b4-9f55-4625-b155-12abec58e58a"]
    }
  ]
}
```

## Error Responses

| Status Code | Description | Response Body |
|-------------|-------------|---------------|
| 400 | Bad Request | `{"error": "Invalid query parameters"}` |
| 401 | Unauthorized | `{"error": "Invalid or missing API key"}` |
| 429 | Too Many Requests | `{"error": "Rate limit exceeded"}` |
| 500 | Internal Server Error | `{"error": "Server error"}` |

## Rate Limiting

Standard API rate limits apply. Monitor the response headers for rate limit information. This endpoint may have higher volume than others.

## Notes

- Transactions are aggregated by default (same person, same day, same code)
- Transaction codes: B=Buy, S=Sell, etc.
- Negative amounts indicate sales
- Data is updated daily with new SEC filings
- Some fields may be null for certain transaction types
- 10b5-1 plans indicate pre-planned trading strategies
- Officers and directors are more significant than ordinary shareholders

## Related Endpoints

- [Insiders](/docs/insider/insiders.md) - Get list of insiders for a specific ticker
- [Ticker Flow](/docs/insider/ticker-flow.md) - Get aggregated insider flow for a specific ticker
- [Sector Flow](/docs/insider/sector-flow.md) - Get aggregated insider flow for a sector

## Validation Results

**Tested**: Yes

**Test Date**: 2025-10-22

**Status**: Working

**Notes**: Endpoint returns comprehensive insider transaction data. Successfully returns latest transactions with all expected fields populated. Response includes 25+ recent insider transactions with detailed metadata.
