# Seasonality API Endpoints

Seasonal performance patterns for stocks and market by month and year.

## Overview

This category contains **4 endpoints** for accessing seasonality data from the Unusual Whales API.

## Endpoints

1. **GET /api/seasonality/market**
   - Market Seasonality
   - [View Documentation](./market.md)

2. **GET /api/seasonality/{month}/performers**
   - Month Performers
   - [View Documentation](./month-performers.md)

3. **GET /api/seasonality/{ticker}/monthly**
   - Average return per month
   - [View Documentation](./monthly.md)

4. **GET /api/seasonality/{ticker}/year-month**
   - Price change per month per year
   - [View Documentation](./year-month.md)


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
