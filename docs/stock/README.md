# Stock API Endpoints

Comprehensive stock and options data including greeks, flow, volatility, open interest, and technical indicators.

## Overview

This category contains **41 endpoints** for accessing stock data from the Unusual Whales API.

## Endpoints

1. **GET /api/stock/{sector}/tickers**
   - Companies in Sector
   - [View Documentation](./stock-tickers.md)

2. **GET /api/stock/{ticker}/atm-chains**
   - ATM Chains
   - [View Documentation](./stock-atm-chains.md)

3. **GET /api/stock/{ticker}/expiry-breakdown**
   - Expiry Breakdown
   - [View Documentation](./stock-expiry-breakdown.md)

4. **GET /api/stock/{ticker}/flow-alerts**
   - Flow Alerts
   - [View Documentation](./stock-flow-alerts.md)

5. **GET /api/stock/{ticker}/flow-per-expiry**
   - Flow per expiry
   - [View Documentation](./stock-flow-per-expiry.md)

6. **GET /api/stock/{ticker}/flow-per-strike**
   - Flow per strike
   - [View Documentation](./stock-flow-per-strike.md)

7. **GET /api/stock/{ticker}/flow-per-strike-intraday**
   - Flow per strike intraday
   - [View Documentation](./stock-flow-per-strike-intraday.md)

8. **GET /api/stock/{ticker}/flow-recent**
   - Recent flows
   - [View Documentation](./stock-flow-recent.md)

9. **GET /api/stock/{ticker}/greek-exposure**
   - Greek Exposure
   - [View Documentation](./stock-greek-exposure.md)

10. **GET /api/stock/{ticker}/greek-exposure/expiry**
   - Greek Exposure By Expiry
   - [View Documentation](./stock-oi-per-expiry.md)

11. **GET /api/stock/{ticker}/greek-exposure/strike**
   - Greek Exposure By Strike
   - [View Documentation](./stock-greek-exposure-strike.md)

12. **GET /api/stock/{ticker}/greek-exposure/strike-expiry**
   - Greek Exposure By Strike And Expiry
   - [View Documentation](./stock-greek-exposure-strike-expiry.md)

13. **GET /api/stock/{ticker}/greek-flow**
   - Greek flow
   - [View Documentation](./stock-greek-flow.md)

14. **GET /api/stock/{ticker}/greek-flow/{expiry}**
   - Greek flow by expiry
   - [View Documentation](./stock-oi-per-expiry.md)

15. **GET /api/stock/{ticker}/greeks**
   - Greeks
   - [View Documentation](./stock-greeks.md)

16. **GET /api/stock/{ticker}/historical-risk-reversal-skew**
   - Historical Risk Reversal Skew
   - [View Documentation](./stock-historical-risk-reversal-skew.md)

17. **GET /api/stock/{ticker}/info**
   - Information
   - [View Documentation](./stock-info.md)

18. **GET /api/stock/{ticker}/insider-buy-sells**
   - Insider buy & sells
   - [View Documentation](./stock-insider-buy-sells.md)

19. **GET /api/stock/{ticker}/interpolated-iv**
   - Interpolated IV
   - [View Documentation](./stock-interpolated-iv.md)

20. **GET /api/stock/{ticker}/iv-rank**
   - IV Rank
   - [View Documentation](./stock-iv-rank.md)

21. **GET /api/stock/{ticker}/max-pain**
   - Max Pain
   - [View Documentation](./stock-max-pain.md)

22. **GET /api/stock/{ticker}/net-prem-ticks**
   - Call/Put Net/Vol Ticks
   - [View Documentation](./stock-net-prem-ticks.md)

23. **GET /api/stock/{ticker}/nope**
   - Nope
   - [View Documentation](./stock-nope.md)

24. **GET /api/stock/{ticker}/ohlc/{candle_size}**
   - OHLC
   - [View Documentation](./stock-greek-exposure-expiry.md)

25. **GET /api/stock/{ticker}/oi-change**
   - OI Change
   - [View Documentation](./stock-oi-change.md)

26. **GET /api/stock/{ticker}/oi-per-expiry**
   - OI per Expiry
   - [View Documentation](./stock-oi-per-expiry.md)

27. **GET /api/stock/{ticker}/oi-per-strike**
   - OI per Strike
   - [View Documentation](./stock-oi-per-strike.md)

28. **GET /api/stock/{ticker}/option-chains**
   - Option Chains
   - [View Documentation](./stock-option-chains.md)

29. **GET /api/stock/{ticker}/option-contracts**
   - Option contracts
   - [View Documentation](./stock-option-contracts.md)

30. **GET /api/stock/{ticker}/option/stock-price-levels**
   - Option Price Levels
   - [View Documentation](./stock-spot-exposures-strike.md)

31. **GET /api/stock/{ticker}/option/volume-oi-expiry**
   - Volume & OI per Expiry
   - [View Documentation](./stock-option-volume-oi-expiry.md)

32. **GET /api/stock/{ticker}/options-volume**
   - Options Volume
   - [View Documentation](./stock-options-volume.md)

33. **GET /api/stock/{ticker}/spot-exposures**
   - Spot GEX exposures per 1min
   - [View Documentation](./stock-spot-exposures.md)

34. **GET /api/stock/{ticker}/spot-exposures/expiry-strike**
   - Spot GEX exposures by strike & expiry
   - [View Documentation](./stock-spot-exposures-expiry-strike.md)

35. **GET /api/stock/{ticker}/spot-exposures/strike**
   - Spot GEX exposures by strike
   - [View Documentation](./stock-greek-exposure-strike.md)

36. **GET /api/stock/{ticker}/spot-exposures/{expiry}/strike**
   - Spot GEX exposures by strike & expiry (Deprecated)
   - [View Documentation](./stock-greek-exposure-strike.md)

37. **GET /api/stock/{ticker}/stock-state**
   - Stock State
   - [View Documentation](./stock-stock-state.md)

38. **GET /api/stock/{ticker}/stock-volume-price-levels**
   - Off/Lit Price Levels
   - [View Documentation](./stock-stock-volume-price-levels.md)

39. **GET /api/stock/{ticker}/volatility/realized**
   - Realized Volatility
   - [View Documentation](./stock-volatility-realized.md)

40. **GET /api/stock/{ticker}/volatility/stats**
   - Volatility Statistics
   - [View Documentation](./stock-volatility-stats.md)

41. **GET /api/stock/{ticker}/volatility/term-structure**
   - Implied Volatility Term Structure
   - [View Documentation](./stock-volatility-term-structure.md)


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
- [Option Contract](../option-contract/README.md)

## Support

For API support and questions:
- Documentation: https://docs.unusualwhales.com
- API Issues: Contact Unusual Whales support

---

*Last Updated: 2025-10-22*
