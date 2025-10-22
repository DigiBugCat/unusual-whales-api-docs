# Etfs API Endpoints

Comprehensive ETF data including holdings, exposure, flows, and sector weights.

## Overview

This category contains **5 endpoints** for accessing etfs data from the Unusual Whales API.

## Endpoints

1. **GET /api/etfs/{ticker}/exposure**
   - Exposure
   - [View Documentation](./exposure.md)

2. **GET /api/etfs/{ticker}/holdings**
   - Holdings
   - [View Documentation](./holdings.md)

3. **GET /api/etfs/{ticker}/in-outflow**
   - Inflow & Outflow
   - [View Documentation](./in-outflow.md)

4. **GET /api/etfs/{ticker}/info**
   - Information
   - [View Documentation](./info.md)

5. **GET /api/etfs/{ticker}/weights**
   - Sector & Country weights
   - [View Documentation](./weights.md)


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

- [Stock](../stock/README.md)
- [Market](../market/README.md)

## Support

For API support and questions:
- Documentation: https://docs.unusualwhales.com
- API Issues: Contact Unusual Whales support

---

*Last Updated: 2025-10-22*
