# Politician Portfolios API Endpoints

Track politician stock portfolios and holdings (Enterprise tier).

## Overview

This category contains **3 endpoints** for accessing politician-portfolios data from the Unusual Whales API.

## Endpoints

1. **GET /api/politician-portfolios/holders/{ticker}**
   - Politician Portfolio Holders by Ticker
   - [View Documentation](./holders-by-ticker.md)

2. **GET /api/politician-portfolios/people**
   - Politicians List
   - [View Documentation](./people-list.md)

3. **GET /api/politician-portfolios/{politician_id}**
   - Politician Portfolios
   - [View Documentation](./people-list.md)


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

- [Congress](../congress/README.md)
- [Stock](../stock/README.md)

## Support

For API support and questions:
- Documentation: https://docs.unusualwhales.com
- API Issues: Contact Unusual Whales support

---

*Last Updated: 2025-10-22*
