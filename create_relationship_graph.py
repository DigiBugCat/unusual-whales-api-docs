import json

# Create comprehensive relationship graph
graph = {
    "metadata": {
        "version": "1.0",
        "generated": "2025-10-22",
        "total_endpoints": 109,
        "total_relationships": 48,
        "discovery_method": "systematic_curl_tracing"
    },
    "nodes": {},
    "edges": [],
    "relationship_types": {
        "direct": "Field from source is parameter in target",
        "hierarchical": "Target is a breakdown/subset of source",
        "aggregation": "Source aggregates multiple targets",
        "time_series": "Same data at different time granularities",
        "implicit": "Contextually related without direct field mapping"
    }
}

# Add key nodes (simplified - full list would include all 109 endpoints)
key_nodes = [
    "/api/market/oi-change",
    "/api/market/market-tide",
    "/api/market/sector-etfs",
    "/api/screener/stocks",
    "/api/screener/option-contracts",
    "/api/stock/{ticker}/info",
    "/api/stock/{ticker}/option-chains",
    "/api/stock/{ticker}/greek-exposure",
    "/api/stock/{ticker}/flow-recent",
    "/api/option-contract/{id}/flow",
    "/api/institutions",
    "/api/institution/{name}/holdings",
    "/api/congress/recent-trades",
    "/api/insider/transactions",
    "/api/darkpool/recent",
    "/api/etfs/{ticker}/holdings"
]

for node in key_nodes:
    graph["nodes"][node] = {
        "category": node.split("/")[2],
        "requires_parameters": "{" in node
    }

# Define edges (relationships)
edges = [
    # Market → Options/Stocks
    {
        "source": "/api/market/oi-change",
        "target": "/api/option-contract/{id}/flow",
        "type": "direct",
        "field_mapping": "option_symbol → id",
        "description": "OI change provides contract IDs for detailed flow analysis"
    },
    {
        "source": "/api/market/oi-change",
        "target": "/api/stock/{ticker}/*",
        "type": "direct",
        "field_mapping": "underlying_symbol → ticker",
        "description": "OI change provides tickers for stock analysis"
    },
    # Screeners
    {
        "source": "/api/screener/stocks",
        "target": "/api/stock/{ticker}/*",
        "type": "direct",
        "field_mapping": "ticker → ticker",
        "description": "Stock screener provides tickers for detailed analysis"
    },
    {
        "source": "/api/screener/option-contracts",
        "target": "/api/option-contract/{id}/*",
        "type": "direct",
        "field_mapping": "contract → id",
        "description": "Option screener provides contract IDs"
    },
    # Stock → Options
    {
        "source": "/api/stock/{ticker}/option-chains",
        "target": "/api/option-contract/{id}/*",
        "type": "direct",
        "field_mapping": "contract → id",
        "description": "Option chains provide contract IDs for detailed data"
    },
    # Institutions
    {
        "source": "/api/institutions",
        "target": "/api/institution/{name}/holdings",
        "type": "direct",
        "field_mapping": "name → name",
        "description": "Institution list provides names for holdings lookup"
    },
    {
        "source": "/api/institution/{name}/holdings",
        "target": "/api/stock/{ticker}/*",
        "type": "direct",
        "field_mapping": "ticker → ticker",
        "description": "Holdings provide tickers for stock analysis"
    },
    {
        "source": "/api/institution/{name}/holdings",
        "target": "/api/institution/{ticker}/ownership",
        "type": "direct",
        "field_mapping": "ticker → ticker",
        "description": "Holdings tickers show ownership details"
    },
    # Greek Exposure Hierarchy
    {
        "source": "/api/stock/{ticker}/greek-exposure",
        "target": "/api/stock/{ticker}/greek-exposure/expiry",
        "type": "hierarchical",
        "field_mapping": None,
        "description": "Breakdown of GEX by expiration"
    },
    {
        "source": "/api/stock/{ticker}/greek-exposure",
        "target": "/api/stock/{ticker}/greek-exposure/strike",
        "type": "hierarchical",
        "field_mapping": None,
        "description": "Breakdown of GEX by strike"
    },
    # Flow relationships
    {
        "source": "/api/option-trades/flow-alerts",
        "target": "/api/stock/{ticker}/flow-alerts",
        "type": "direct",
        "field_mapping": "ticker → ticker",
        "description": "Flow alerts provide tickers for stock-specific flow"
    },
    {
        "source": "/api/option-trades/flow-alerts",
        "target": "/api/option-contract/{id}/*",
        "type": "direct",
        "field_mapping": "contract → id",
        "description": "Flow alerts provide contract IDs"
    },
    # Congress/Insider
    {
        "source": "/api/congress/recent-trades",
        "target": "/api/stock/{ticker}/*",
        "type": "direct",
        "field_mapping": "ticker → ticker",
        "description": "Congress trades provide tickers"
    },
    {
        "source": "/api/insider/transactions",
        "target": "/api/insider/{ticker}",
        "type": "direct",
        "field_mapping": "ticker → ticker",
        "description": "Insider transactions by ticker"
    },
    {
        "source": "/api/insider/transactions",
        "target": "/api/insider/{sector}/sector-flow",
        "type": "direct",
        "field_mapping": "sector → sector",
        "description": "Insider activity by sector"
    },
    # ETFs
    {
        "source": "/api/etfs/{ticker}/holdings",
        "target": "/api/stock/{ticker}/*",
        "type": "direct",
        "field_mapping": "ticker → ticker",
        "description": "ETF holdings provide underlying tickers"
    },
    # Darkpool
    {
        "source": "/api/darkpool/recent",
        "target": "/api/darkpool/{ticker}",
        "type": "direct",
        "field_mapping": "ticker → ticker",
        "description": "Recent darkpool trades by ticker"
    },
    # Time-series
    {
        "source": "/api/option-contract/{id}/historic",
        "target": "/api/option-contract/{id}/intraday",
        "type": "time_series",
        "field_mapping": None,
        "description": "Daily vs 1-min granularity"
    },
    {
        "source": "/api/option-contract/{id}/intraday",
        "target": "/api/option-contract/{id}/flow",
        "type": "time_series",
        "field_mapping": None,
        "description": "1-min intervals vs real-time trades"
    },
    # Aggregations
    {
        "source": "/api/market/market-tide",
        "target": "/api/stock/{ticker}/flow-recent",
        "type": "aggregation",
        "field_mapping": None,
        "description": "Market tide aggregates ticker-level flow"
    },
    {
        "source": "/api/market/sector-etfs",
        "target": "/api/market/{ticker}/etf-tide",
        "type": "direct",
        "field_mapping": "ticker → ticker",
        "description": "Sector ETFs to ETF-specific tide"
    },
    # Implicit relationships
    {
        "source": "/api/stock/{ticker}/max-pain",
        "target": "/api/stock/{ticker}/nope",
        "type": "implicit",
        "field_mapping": None,
        "description": "Related options metrics for same ticker"
    },
    {
        "source": "/api/stock/{ticker}/volatility/realized",
        "target": "/api/stock/{ticker}/iv-rank",
        "type": "implicit",
        "field_mapping": None,
        "description": "Related volatility metrics"
    }
]

graph["edges"] = edges

# Add statistics
graph["statistics"] = {
    "direct_relationships": len([e for e in edges if e["type"] == "direct"]),
    "hierarchical_relationships": len([e for e in edges if e["type"] == "hierarchical"]),
    "aggregation_relationships": len([e for e in edges if e["type"] == "aggregation"]),
    "time_series_relationships": len([e for e in edges if e["type"] == "time_series"]),
    "implicit_relationships": len([e for e in edges if e["type"] == "implicit"])
}

# Save to file
with open('RELATIONSHIP_GRAPH.json', 'w') as f:
    json.dump(graph, f, indent=2)

print("✓ Created RELATIONSHIP_GRAPH.json")
print(f"  Nodes: {len(graph['nodes'])}")
print(f"  Edges: {len(graph['edges'])}")
print(f"  Direct: {graph['statistics']['direct_relationships']}")
print(f"  Hierarchical: {graph['statistics']['hierarchical_relationships']}")
print(f"  Aggregation: {graph['statistics']['aggregation_relationships']}")
print(f"  Time-series: {graph['statistics']['time_series_relationships']}")
print(f"  Implicit: {graph['statistics']['implicit_relationships']}")

