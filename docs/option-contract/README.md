# Option Contract API Endpoints

Detailed option contract data including flow, historical data, intraday pricing, and volume profiles.

## Overview

This category contains **4 endpoints** for accessing option-contract data from the Unusual Whales API.

## Endpoints

1. **GET /api/option-contract/{id}/flow**
   - Flow Data
   - [View Documentation](./flow.md)

2. **GET /api/option-contract/{id}/historic**
   - Historic Data
   - [View Documentation](./historic.md)

3. **GET /api/option-contract/{id}/intraday**
   - Intraday Data
   - [View Documentation](./intraday.md)

4. **GET /api/option-contract/{id}/volume-profile**
   - Volume Profile
   - [View Documentation](./volume-profile.md)


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
- [Option Trades](../option-trades/README.md)

## Support

For API support and questions:
- Documentation: https://docs.unusualwhales.com
- API Issues: Contact Unusual Whales support

---

*Last Updated: 2025-10-22*
