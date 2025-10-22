import json
import os

# Load the endpoints breakdown
with open('endpoints_breakdown.json', 'r') as f:
    data = json.load(f)

# Category descriptions
category_descriptions = {
    "alerts": "Configure and retrieve user alerts for market events, options flow, and trading signals.",
    "congress": "Track congressional trading activity, late reports, and stock transactions by members of Congress.",
    "darkpool": "Access darkpool trading data for specific tickers and recent darkpool transactions.",
    "earnings": "Retrieve earnings calendar data, including premarket and afterhours earnings reports.",
    "etfs": "Comprehensive ETF data including holdings, exposure, flows, and sector weights.",
    "group-flow": "Analyze options greek flow grouped by various criteria and expiration dates.",
    "insider": "Monitor insider trading activity by sector, ticker, and individual transactions.",
    "institution": "Track institutional holdings, activity, sectors, and ownership data for major institutions.",
    "institutions": "List institutional investors and their latest 13F filings.",
    "market": "Market-wide data including tide indicators, correlations, economic calendar, and sector statistics.",
    "net-flow": "Net premium flow analysis by expiration and moneyness.",
    "news": "Financial news headlines and market-moving news events.",
    "option-contract": "Detailed option contract data including flow, historical data, intraday pricing, and volume profiles.",
    "option-trades": "Options flow alerts and full tape data for significant options trading activity.",
    "politician-portfolios": "Track politician stock portfolios and holdings (Enterprise tier).",
    "screener": "Powerful screening tools for stocks, options contracts, and analyst ratings.",
    "seasonality": "Seasonal performance patterns for stocks and market by month and year.",
    "shorts": "Short selling data including short interest, failures to deliver, volume, and exchange data.",
    "socket": "WebSocket connections for real-time streaming data (prices, flow alerts, news, GEX).",
    "stock": "Comprehensive stock and options data including greeks, flow, volatility, open interest, and technical indicators."
}

# Create README for each category
for category, endpoints in sorted(data['categories'].items()):
    readme_content = f"""# {category.title().replace('-', ' ')} API Endpoints

{category_descriptions.get(category, 'API endpoints for ' + category)}

## Overview

This category contains **{len(endpoints)} endpoint{"s" if len(endpoints) != 1 else ""}** for accessing {category} data from the Unusual Whales API.

## Endpoints

"""
    
    # List all endpoints
    for i, ep in enumerate(sorted(endpoints, key=lambda x: x['path']), 1):
        # Generate filename (simplified)
        path_parts = ep['path'].split('/')
        filename = path_parts[-1] if path_parts[-1] else path_parts[-2]
        filename = filename.replace('{', '').replace('}', '')
        
        # Try to find the actual file
        category_dir = f"docs/{category}"
        files = os.listdir(category_dir) if os.path.exists(category_dir) else []
        
        # Use first file match or generate expected name
        matching_file = None
        for f in files:
            if filename.lower() in f.lower():
                matching_file = f
                break
        
        if not matching_file and files:
            # Just use files in order
            if i - 1 < len(files):
                matching_file = files[i - 1]
        
        doc_link = f"./{matching_file}" if matching_file else f"./{filename}.md"
        
        readme_content += f"{i}. **{ep['method']} {ep['path']}**\n"
        readme_content += f"   - {ep['summary'] or 'N/A'}\n"
        readme_content += f"   - [View Documentation]({doc_link})\n\n"
    
    readme_content += f"""
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

"""
    
    # Add related categories
    related = {
        "alerts": ["market", "stock"],
        "congress": ["insider", "politician-portfolios"],
        "darkpool": ["stock", "option-trades"],
        "earnings": ["stock", "news"],
        "etfs": ["stock", "market"],
        "group-flow": ["stock", "option-contract"],
        "insider": ["stock", "congress"],
        "institution": ["institutions", "stock"],
        "institutions": ["institution", "stock"],
        "market": ["stock", "news"],
        "net-flow": ["stock", "option-contract"],
        "news": ["market", "stock"],
        "option-contract": ["stock", "option-trades"],
        "option-trades": ["option-contract", "stock"],
        "politician-portfolios": ["congress", "stock"],
        "screener": ["stock", "option-contract"],
        "seasonality": ["stock", "market"],
        "shorts": ["stock", "market"],
        "socket": ["stock", "market", "news"],
        "stock": ["market", "option-contract"]
    }
    
    for rel_cat in related.get(category, []):
        readme_content += f"- [{rel_cat.title().replace('-', ' ')}](../{rel_cat}/README.md)\n"
    
    readme_content += """
## Support

For API support and questions:
- Documentation: https://docs.unusualwhales.com
- API Issues: Contact Unusual Whales support

---

*Last Updated: 2025-10-22*
"""
    
    # Write README
    readme_path = f"docs/{category}/README.md"
    with open(readme_path, 'w') as f:
        f.write(readme_content)
    
    print(f"✓ Created {readme_path}")

print(f"\n✓ Created {len(data['categories'])} category README files")
