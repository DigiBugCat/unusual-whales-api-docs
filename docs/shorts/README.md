# Shorts API Endpoints

Short selling data including short interest, failures to deliver, volume, and exchange data.

## Overview

This category contains **5 endpoints** for accessing shorts data from the Unusual Whales API.

## Endpoints

1. **GET /api/shorts/{ticker}/data**
   - Short Data
   - [View Documentation](./short-data.md)

2. **GET /api/shorts/{ticker}/ftds**
   - Failures to Deliver
   - [View Documentation](./failures-to-deliver.md)

3. **GET /api/shorts/{ticker}/interest-float**
   - Short Interest and Float
   - [View Documentation](./interest-float.md)

4. **GET /api/shorts/{ticker}/volume-and-ratio**
   - Short Volume and Ratio
   - [View Documentation](./volume-and-ratio.md)

5. **GET /api/shorts/{ticker}/volumes-by-exchange**
   - Short Volume By Exchange
   - [View Documentation](./volumes-by-exchange.md)


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
