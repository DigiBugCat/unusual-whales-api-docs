# Insider API Endpoints

Monitor insider trading activity by sector, ticker, and individual transactions.

## Overview

This category contains **4 endpoints** for accessing insider data from the Unusual Whales API.

## Endpoints

1. **GET /api/insider/transactions**
   - Transactions
   - [View Documentation](./transactions.md)

2. **GET /api/insider/{sector}/sector-flow**
   - Sector Flow
   - [View Documentation](./sector-flow.md)

3. **GET /api/insider/{ticker}**
   - Insiders
   - [View Documentation](./ticker-flow.md)

4. **GET /api/insider/{ticker}/ticker-flow**
   - Ticker Flow
   - [View Documentation](./ticker-flow.md)


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
- [Congress](../congress/README.md)

## Support

For API support and questions:
- Documentation: https://docs.unusualwhales.com
- API Issues: Contact Unusual Whales support

---

*Last Updated: 2025-10-22*
