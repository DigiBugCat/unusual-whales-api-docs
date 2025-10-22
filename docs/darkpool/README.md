# Darkpool API Endpoints

Access darkpool trading data for specific tickers and recent darkpool transactions.

## Overview

This category contains **2 endpoints** for accessing darkpool data from the Unusual Whales API.

## Endpoints

1. **GET /api/darkpool/recent**
   - Recent Darkpool Trades
   - [View Documentation](./darkpool-recent.md)

2. **GET /api/darkpool/{ticker}**
   - Ticker Darkpool Trades
   - [View Documentation](./darkpool-ticker.md)


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
