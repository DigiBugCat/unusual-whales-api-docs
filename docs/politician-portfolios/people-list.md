# Politicians List

## Endpoint Details

**Path**: `GET /api/politician-portfolios/people`

**Operation ID**: `PublicApi.PoliticianPortfoliosController.people`

**Summary**: Politicians List

**Tags**: politician_portfolios

## Description

Returns all politician names and IDs. This endpoint provides a directory of all politicians whose portfolios are tracked in the system, returning their names and unique identifiers for use with other politician portfolio endpoints.

**IMPORTANT**: This is an enterprise-only endpoint. Contact dan@unusualwhales.com for details about accessing this data. Standard API keys may not have access to this endpoint.

## Authentication

- **Required**: Yes
- **Type**: API Key (Enterprise tier required)
- **Header**: `Authorization: Bearer YOUR_API_KEY`
- **Access Level**: Enterprise Only

## Request Parameters

### Path Parameters

None

### Query Parameters

None - this endpoint does not accept query parameters.

### Request Body

None

## Example Requests

### cURL

```bash
curl -X GET "https://api.unusualwhales.com/api/politician-portfolios/people" \
  -H "Authorization: Bearer YOUR_ENTERPRISE_API_KEY"
```

### Python

```python
import requests

url = "https://api.unusualwhales.com/api/politician-portfolios/people"
headers = {
    "Authorization": "Bearer YOUR_ENTERPRISE_API_KEY"
}

response = requests.get(url, headers=headers)
data = response.json()
print(data)
```

### JavaScript (Fetch)

```javascript
const url = "https://api.unusualwhales.com/api/politician-portfolios/people";
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
      "id": "550e8400-e29b-41d4-a716-446655440000",
      "name": "John Smith"
    },
    {
      "id": "660e8400-e29b-41d4-a716-446655440111",
      "name": "Jane Doe"
    }
  ]
}
```

### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| data | array | Array of politician records |
| id | string | Unique identifier (UUID) for the politician |
| name | string | Full name of the politician |

## Example Response

```json
{
  "data": [
    {
      "id": "550e8400-e29b-41d4-a716-446655440000",
      "name": "John Smith"
    },
    {
      "id": "660e8400-e29b-41d4-a716-446655440111",
      "name": "Jane Doe"
    },
    {
      "id": "770e8400-e29b-41d4-a716-446655440222",
      "name": "Robert Johnson"
    },
    {
      "id": "880e8400-e29b-41d4-a716-446655440333",
      "name": "Sarah Williams"
    }
  ]
}
```

## Error Responses

| Status Code | Description | Response Body |
|-------------|-------------|---------------|
| 401 | Unauthorized | `{"error": "Invalid API key"}` |
| 403 | Forbidden | `{"msg": "Missing access for politician ports. This is an enterprise only endpoint. Contact dan@unusualwhales.com"}` |
| 422 | Unprocessable Entity | `{"error": "Unprocessable Entity"}` |
| 500 | Internal Server Error | `{"error": "Server error"}` |

## Rate Limiting

The API enforces rate limits on requests. Enterprise tier may have higher rate limits. Check response headers for rate limit information.

## Notes

- **Enterprise Access Required**: This endpoint is restricted to enterprise-tier API keys
- Standard API keys will receive a 403 Forbidden response
- Contact dan@unusualwhales.com to request access
- Returns a complete list of all politicians tracked in the system
- IDs are UUIDs and should be used with `/api/politician-portfolios/{politician_id}` endpoint
- No pagination parameters are available - all results are returned in a single response
- Data is updated as new politicians are added to the tracking system
- Useful for building a directory or dropdown list of available politicians
- The list can be quite extensive depending on the system

## Related Endpoints

- `/api/politician-portfolios/{politician_id}` - Get full portfolio details for a specific politician
- `/api/politician-portfolios/holders/{ticker}` - Get politicians holding a specific ticker

## Validation Results

**Tested**: Yes

**Test Date**: 2025-10-22

**Status**: Enterprise Access Required

**Notes**: Endpoint is functional but requires enterprise-tier API key. Standard API key returns 403 Forbidden with message "Missing access for politician ports. This is an enterprise only endpoint. Contact dan@unusualwhales.com". Endpoint structure confirmed. No query parameters or complex filtering available. Contact support for enterprise access to test full functionality.
