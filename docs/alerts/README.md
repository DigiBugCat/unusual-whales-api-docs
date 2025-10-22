# Alerts API Endpoints

Configure and retrieve user alerts for market events, options flow, and trading signals.

## Overview

This category contains **2 endpoints** for accessing alerts data from the Unusual Whales API.

## Endpoints

1. **GET /api/alerts**
   - Alerts
   - [View Documentation](./get-alerts.md)

2. **GET /api/alerts/configuration**
   - Alert configurations
   - [View Documentation](./alert-configurations.md)


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

- [Market](../market/README.md)
- [Stock](../stock/README.md)

## Support

For API support and questions:
- Documentation: https://docs.unusualwhales.com
- API Issues: Contact Unusual Whales support

---

*Last Updated: 2025-10-22*
