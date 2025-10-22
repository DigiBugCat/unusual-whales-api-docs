# Institution API Endpoints

Track institutional holdings, activity, sectors, and ownership data for major institutions.

## Overview

This category contains **4 endpoints** for accessing institution data from the Unusual Whales API.

## Endpoints

1. **GET /api/institution/{name}/activity**
   - Institutional Activity
   - [View Documentation](./activity.md)

2. **GET /api/institution/{name}/holdings**
   - Institutional Holdings
   - [View Documentation](./holdings.md)

3. **GET /api/institution/{name}/sectors**
   - Sector Exposure
   - [View Documentation](./sectors.md)

4. **GET /api/institution/{ticker}/ownership**
   - Institutional Ownership
   - [View Documentation](./ownership.md)


## Authentication

All endpoints require API key authentication:

```bash
Authorization: Bearer YOUR_API_KEY
```

## Base URL

```
https://api.unusualwhales.com
```

## Getting Started

1. Choose an endpoint from the list above
2. Review the endpoint documentation
3. Use the provided code examples (cURL, Python, JavaScript)
4. Test with your API key

## Common Parameters

Many endpoints in this category support:
- Date filtering
- Pagination (limit/offset)
- Sorting options
- Specific ticker/symbol filtering

## Rate Limiting

Standard API rate limits apply. See individual endpoint documentation for specific details.

## Related Categories

- [Institutions](../institutions/README.md)
- [Stock](../stock/README.md)

## Support

For API support and questions:
- Documentation: https://docs.unusualwhales.com
- API Issues: Contact Unusual Whales support

---

*Last Updated: 2025-10-22*
