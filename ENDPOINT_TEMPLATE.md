# [Endpoint Name]

## Endpoint Details

**Path**: `[HTTP_METHOD] [endpoint_path]`

**Operation ID**: `[operation_id]`

**Summary**: [brief_summary]

**Tags**: [tag1, tag2, ...]

## Description

[Detailed description of what this endpoint does and its use cases]

## Authentication

- **Required**: Yes
- **Type**: API Key
- **Header**: `Authorization: Bearer YOUR_API_KEY`

## Request Parameters

### Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| [param_name] | [type] | Yes/No | [description] |

### Query Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| [param_name] | [type] | Yes/No | [default] | [description] |

### Request Body

```json
[request_body_schema if applicable]
```

## Example Requests

### cURL

```bash
curl -X [METHOD] "https://api.unusualwhales.com[endpoint_path]?[params]" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

### Python

```python
import requests

url = "https://api.unusualwhales.com[endpoint_path]"
headers = {
    "Authorization": "Bearer YOUR_API_KEY"
}
params = {
    "[param]": "[value]"
}

response = requests.get(url, headers=headers, params=params)
data = response.json()
print(data)
```

### JavaScript (Fetch)

```javascript
const url = "https://api.unusualwhales.com[endpoint_path]?[params]";
const options = {
  method: '[METHOD]',
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
[response_schema]
```

### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| [field_name] | [type] | [description] |

## Example Response

```json
[actual_response_example]
```

## Error Responses

| Status Code | Description | Response Body |
|-------------|-------------|---------------|
| 400 | Bad Request | `{"error": "Invalid parameters"}` |
| 401 | Unauthorized | `{"error": "Invalid API key"}` |
| 404 | Not Found | `{"error": "Resource not found"}` |
| 429 | Too Many Requests | `{"error": "Rate limit exceeded"}` |
| 500 | Internal Server Error | `{"error": "Server error"}` |

## Rate Limiting

[Information about rate limits for this endpoint]

## Notes

- [Important notes, caveats, or special considerations]
- [Edge cases or limitations]
- [Best practices for using this endpoint]

## Related Endpoints

- [Link to related endpoint 1]
- [Link to related endpoint 2]

## Validation Results

**Tested**: [Yes/No]

**Test Date**: [YYYY-MM-DD]

**Status**: [Working/Issues Found/Not Tested]

**Notes**: [Any issues or observations from testing]
