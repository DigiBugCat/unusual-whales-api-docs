# Socket API Endpoints

WebSocket connections for real-time streaming data (prices, flow alerts, news, GEX).

## Overview

This category contains **6 endpoints** for accessing socket data from the Unusual Whales API.

## Endpoints

1. **GET /api/socket**
   - WebSocket channels
   - [View Documentation](./socket-gex.md)

2. **GET /api/socket/flow_alerts**
   - Flow alerts
   - [View Documentation](./socket-flow_alerts.md)

3. **GET /api/socket/gex**
   - GEX
   - [View Documentation](./socket-gex.md)

4. **GET /api/socket/news**
   - News
   - [View Documentation](./socket-news.md)

5. **GET /api/socket/option_trades**
   - Option trades
   - [View Documentation](./socket-option_trades.md)

6. **GET /api/socket/price**
   - Price
   - [View Documentation](./socket-price.md)


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
- [News](../news/README.md)

## Support

For API support and questions:
- Documentation: https://docs.unusualwhales.com
- API Issues: Contact Unusual Whales support

---

*Last Updated: 2025-10-22*
