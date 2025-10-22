# Congress API Endpoints

Track congressional trading activity, late reports, and stock transactions by members of Congress.

## Overview

This category contains **3 endpoints** for accessing congress data from the Unusual Whales API.

## Endpoints

1. **GET /api/congress/congress-trader**
   - Recent Reports By Trader
   - [View Documentation](./congress-trader.md)

2. **GET /api/congress/late-reports**
   - Recent Late Reports
   - [View Documentation](./congress-late-reports.md)

3. **GET /api/congress/recent-trades**
   - Recent Congress Trades
   - [View Documentation](./congress-recent-trades.md)


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

- [Insider](../insider/README.md)
- [Politician Portfolios](../politician-portfolios/README.md)

## Support

For API support and questions:
- Documentation: https://docs.unusualwhales.com
- API Issues: Contact Unusual Whales support

---

*Last Updated: 2025-10-22*
