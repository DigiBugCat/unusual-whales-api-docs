# Market API Endpoints

Market-wide data including tide indicators, correlations, economic calendar, and sector statistics.

## Overview

This category contains **12 endpoints** for accessing market data from the Unusual Whales API.

## Endpoints

1. **GET /api/market/correlations**
   - Correlations
   - [View Documentation](./market-correlations.md)

2. **GET /api/market/economic-calendar**
   - Economic calendar
   - [View Documentation](./economic-calendar.md)

3. **GET /api/market/fda-calendar**
   - FDA Calendar
   - [View Documentation](./fda-calendar.md)

4. **GET /api/market/insider-buy-sells**
   - Total Insider Buy & Sells
   - [View Documentation](./insider-buy-sells.md)

5. **GET /api/market/market-tide**
   - Market Tide
   - [View Documentation](./market-tide.md)

6. **GET /api/market/oi-change**
   - OI Change
   - [View Documentation](./oi-change.md)

7. **GET /api/market/sector-etfs**
   - Sector Etfs
   - [View Documentation](./sector-etfs.md)

8. **GET /api/market/spike**
   - SPIKE
   - [View Documentation](./spike.md)

9. **GET /api/market/top-net-impact**
   - Top Net Impact
   - [View Documentation](./top-net-impact.md)

10. **GET /api/market/total-options-volume**
   - Total Options Volume
   - [View Documentation](./total-options-volume.md)

11. **GET /api/market/{sector}/sector-tide**
   - Sector Tide
   - [View Documentation](./sector-tide.md)

12. **GET /api/market/{ticker}/etf-tide**
   - ETF Tide
   - [View Documentation](./etf-tide.md)


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
- [News](../news/README.md)

## Support

For API support and questions:
- Documentation: https://docs.unusualwhales.com
- API Issues: Contact Unusual Whales support

---

*Last Updated: 2025-10-22*
