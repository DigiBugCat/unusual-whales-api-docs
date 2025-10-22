import json
import yaml

# Load data
with open('endpoints_breakdown.json', 'r') as f:
    breakdown = json.load(f)

with open('openapi-spec.yaml', 'r') as f:
    spec = yaml.safe_load(f)

# Create comprehensive API reference
output = """# Unusual Whales API Reference

**Complete reference for all 109 endpoints**

**Base URL**: `https://api.unusualwhales.com`

**Authentication**: Bearer token in Authorization header

**Last Updated**: 2025-10-22

---

## Quick Navigation

"""

# Add category links
for category in sorted(breakdown['categories'].keys()):
    count = len(breakdown['categories'][category])
    output += f"- [{category.title().replace('-', ' ')}](#{category.replace('-', '-')}) ({count} endpoints)\n"

output += "\n---\n\n"

# For each category
for category, endpoints in sorted(breakdown['categories'].items()):
    output += f"## {category.title().replace('-', ' ')}\n\n"
    output += f"**{len(endpoints)} endpoints**\n\n"
    
    # For each endpoint
    for ep in sorted(endpoints, key=lambda x: x['path']):
        path = ep['path']
        method = ep['method']
        summary = ep['summary'] or 'N/A'
        op_id = ep['operationId']
        
        # Get more details from OpenAPI spec
        endpoint_detail = spec['paths'].get(path, {}).get(method.lower(), {})
        params = endpoint_detail.get('parameters', [])
        description = endpoint_detail.get('description', '').strip()[:200]
        
        output += f"### `{method} {path}`\n\n"
        output += f"**Summary**: {summary}\n\n"
        
        if description:
            output += f"**Description**: {description}...\n\n"
        
        # Parameters
        if params:
            output += "**Parameters**:\n\n"
            output += "| Name | Type | Location | Required | Description |\n"
            output += "|------|------|----------|----------|-------------|\n"
            
            for param in params[:10]:  # Limit to 10 for brevity
                name = param.get('name', '')
                param_in = param.get('in', '')
                required = 'Yes' if param.get('required', False) else 'No'
                param_schema = param.get('schema', {})
                param_type = param_schema.get('type', 'string')
                param_desc = param.get('description', 'N/A')[:50]
                
                output += f"| {name} | {param_type} | {param_in} | {required} | {param_desc} |\n"
            
            if len(params) > 10:
                output += f"\n*...and {len(params) - 10} more parameters*\n"
            output += "\n"
        
        # Example
        output += "**Example**:\n```bash\n"
        
        # Build example URL
        example_path = path
        if '{ticker}' in path:
            example_path = path.replace('{ticker}', 'AAPL')
        if '{id}' in path:
            example_path = path.replace('{id}', 'AAPL251219C00175000')
        if '{name}' in path:
            example_path = path.replace('{name}', 'VANGUARD%20GROUP%20INC')
        if '{sector}' in path:
            example_path = path.replace('{sector}', 'Technology')
        if '{flow_group}' in path:
            example_path = path.replace('{flow_group}', 'all')
        if '{expiry}' in path:
            example_path = path.replace('{expiry}', '2025-12-19')
        if '{politician_id}' in path:
            example_path = path.replace('{politician_id}', '12345')
        if '{candle_size}' in path:
            example_path = path.replace('{candle_size}', '1D')
        if '{date}' in path:
            example_path = path.replace('{date}', '2025-10-22')
        if '{month}' in path:
            example_path = path.replace('{month}', 'January')
        
        output += f'curl "{example_path}" \\\n'
        output += '  -H "Authorization: Bearer YOUR_API_KEY"\n'
        output += "```\n\n"
        
        # Link to detailed docs
        doc_file = f"docs/{category}/README.md"
        output += f"**Documentation**: [View Details](./{doc_file})\n\n"
        output += "---\n\n"

# Add footer
output += """
## Authentication

All endpoints require authentication via Bearer token:

```bash
Authorization: Bearer YOUR_API_KEY
```

Get your API key at: https://unusualwhales.com

---

## Rate Limiting

- Standard rate limits apply
- Limits vary by subscription tier
- Implement exponential backoff for retries

---

## Common Parameters

### Query Parameters (Many Endpoints)

| Parameter | Type | Description |
|-----------|------|-------------|
| limit | integer | Limit number of results (default varies) |
| offset | integer | Offset for pagination |
| date | string | Date filter (ISO 8601 format) |
| newer_than | string | Filter records newer than timestamp |
| older_than | string | Filter records older than timestamp |

### Path Parameters

| Parameter | Description | Example |
|-----------|-------------|---------|
| {ticker} | Stock ticker symbol | AAPL, SPY, TSLA |
| {id} | Option contract ID | AAPL251219C00175000 |
| {name} | Institution name | VANGUARD GROUP INC |
| {sector} | Sector name | Technology, Healthcare |
| {expiry} | Expiration date | 2025-12-19 |

---

## Response Format

All endpoints return JSON with this structure:

```json
{
  "data": [...],  // Array of results or single object
  "count": 100    // Optional: total count
}
```

---

## Error Responses

| Code | Meaning |
|------|---------|
| 400 | Bad Request - Invalid parameters |
| 401 | Unauthorized - Invalid API key |
| 403 | Forbidden - Insufficient permissions |
| 404 | Not Found - Resource doesn't exist |
| 429 | Too Many Requests - Rate limit exceeded |
| 500 | Internal Server Error |

---

## Related Documentation

- [README.md](./README.md) - Overview and getting started
- [ENDPOINT_RELATIONSHIPS.md](./ENDPOINT_RELATIONSHIPS.md) - How endpoints connect
- [DATA_FLOW_EXAMPLES.md](./DATA_FLOW_EXAMPLES.md) - Integration patterns
- [QUICK_CHAINS.md](./QUICK_CHAINS.md) - Common endpoint combinations
- [Individual endpoint docs](./docs/) - Detailed documentation

---

## Categories Summary

"""

# Add category summary table
output += "| Category | Endpoints | Description |\n"
output += "|----------|-----------|-------------|\n"

category_descriptions = {
    "alerts": "User alerts and notifications",
    "congress": "Congressional trading activity",
    "darkpool": "Dark pool trading data",
    "earnings": "Earnings calendar and history",
    "etfs": "ETF holdings and exposure",
    "group-flow": "Grouped options flow",
    "insider": "Insider trading activity",
    "institution": "Institutional holdings",
    "institutions": "Institution listings",
    "market": "Market-wide indicators",
    "net-flow": "Net premium flow",
    "news": "Financial news headlines",
    "option-contract": "Option contract details",
    "option-trades": "Options trading activity",
    "politician-portfolios": "Politician portfolios",
    "screener": "Stock and option screeners",
    "seasonality": "Seasonal patterns",
    "shorts": "Short selling data",
    "socket": "WebSocket connections",
    "stock": "Stock and options data"
}

for category, endpoints in sorted(breakdown['categories'].items()):
    count = len(endpoints)
    desc = category_descriptions.get(category, "")
    output += f"| {category} | {count} | {desc} |\n"

output += f"\n**Total**: {breakdown['total']} endpoints across 20 categories\n"

# Write file
with open('API_REFERENCE.md', 'w') as f:
    f.write(output)

print("✓ Created API_REFERENCE.md")
print(f"  Total endpoints: {breakdown['total']}")
print(f"  Categories: {len(breakdown['categories'])}")
print(f"  File size: {len(output)} characters")

