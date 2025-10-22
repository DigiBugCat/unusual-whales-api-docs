# Option Trades API Endpoints

Options flow alerts and full tape data for significant options trading activity.

## Overview

This category contains **2 endpoints** for accessing option-trades data from the Unusual Whales API.

## Endpoints

1. **GET /api/option-trades/flow-alerts**
   - Flow Alerts
   - [View Documentation](./flow-alerts.md)

2. **GET /api/option-trades/full-tape/{date}**
   - Full Tape
   - [View Documentation](./flow-alerts.md)


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

- [Option Contract](../option-contract/README.md)
- [Stock](../stock/README.md)

## Support

For API support and questions:
- Documentation: https://docs.unusualwhales.com
- API Issues: Contact Unusual Whales support

---

*Last Updated: 2025-10-22*
