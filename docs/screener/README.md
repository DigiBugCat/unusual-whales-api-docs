# Screener API Endpoints

Powerful screening tools for stocks, options contracts, and analyst ratings.

## Overview

This category contains **3 endpoints** for accessing screener data from the Unusual Whales API.

## Endpoints

1. **GET /api/screener/analysts**
   - Analyst Rating
   - [View Documentation](./analysts.md)

2. **GET /api/screener/option-contracts**
   - Hottest Chains
   - [View Documentation](./option-contracts.md)

3. **GET /api/screener/stocks**
   - Stock Screener
   - [View Documentation](./stocks.md)


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
- [Option Contract](../option-contract/README.md)

## Support

For API support and questions:
- Documentation: https://docs.unusualwhales.com
- API Issues: Contact Unusual Whales support

---

*Last Updated: 2025-10-22*
