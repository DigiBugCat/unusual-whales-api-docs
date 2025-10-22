#!/bin/bash

API_KEY="5d1ec006-49f0-4a2a-90ae-5176c72425e3"
BASE_URL="https://api.unusualwhales.com"

echo "================================================================================"
echo "ADVANCED RELATIONSHIP TRACING"
echo "================================================================================"
echo ""

api_call() {
    curl -s "$BASE_URL$1" -H "Authorization: Bearer $API_KEY"
}

declare -a relationships

# FLOW 9: Market-wide to Ticker-specific (Aggregation)
echo "FLOW 9: Market aggregation → Ticker-specific"
echo "--------------------------------------------------------------------------------"
echo "  Testing: /api/market/sector-etfs"
sector_etfs=$(api_call "/api/market/sector-etfs")
test_ticker="XLK"
echo "  Found sector ETF: $test_ticker (Technology)"
echo "  Testing: /api/market/$test_ticker/etf-tide"
etf_tide=$(api_call "/api/market/$test_ticker/etf-tide")
if echo "$etf_tide" | grep -q '"data"'; then
    echo "  ✓ SUCCESS: sector-etfs ticker → /api/market/{ticker}/etf-tide"
    relationships+=("/api/market/sector-etfs[].ticker → /api/market/{ticker}/etf-tide")
fi
echo ""

# FLOW 10: ETF → Holdings → Stocks
echo "FLOW 10: etfs/{ticker}/holdings → stock/{ticker}/*"
echo "--------------------------------------------------------------------------------"
test_etf="SPY"
echo "  Testing: /api/etfs/$test_etf/holdings"
holdings=$(api_call "/api/etfs/$test_etf/holdings?limit=1")
holding_ticker=$(echo "$holdings" | uv run python -c "import sys, json; d=json.load(sys.stdin); print(d['data'][0]['ticker'] if d.get('data') else '')" 2>/dev/null)
echo "  Extracted holding: ticker=$holding_ticker"
if [ ! -z "$holding_ticker" ]; then
    echo "  Testing: /api/stock/$holding_ticker/info"
    stock_info=$(api_call "/api/stock/$holding_ticker/info")
    if echo "$stock_info" | grep -q '"data"'; then
        echo "  ✓ SUCCESS: ETF holdings ticker → /api/stock/{ticker}/*"
        relationships+=("/api/etfs/{ticker}/holdings[].ticker → /api/stock/{ticker}/*")
        relationships+=("/api/etfs/{ticker}/exposure[].ticker → /api/stock/{ticker}/*")
    fi
fi
echo ""

# FLOW 11: Darkpool → Stock
echo "FLOW 11: darkpool/recent → darkpool/{ticker} + stock/{ticker}/*"
echo "--------------------------------------------------------------------------------"
dark_resp=$(api_call "/api/darkpool/recent?limit=1")
dark_ticker=$(echo "$dark_resp" | uv run python -c "import sys, json; d=json.load(sys.stdin); print(d['data'][0]['ticker'] if d.get('data') else '')" 2>/dev/null)
echo "  Extracted from darkpool/recent: ticker=$dark_ticker"
if [ ! -z "$dark_ticker" ]; then
    echo "  Testing: /api/darkpool/$dark_ticker"
    dark_ticker_resp=$(api_call "/api/darkpool/$dark_ticker")
    if echo "$dark_ticker_resp" | grep -q '"data"'; then
        echo "  ✓ SUCCESS: darkpool/recent ticker → /api/darkpool/{ticker}"
        relationships+=("/api/darkpool/recent[].ticker → /api/darkpool/{ticker}")
        relationships+=("/api/darkpool/recent[].ticker → /api/stock/{ticker}/*")
    fi
fi
echo ""

# FLOW 12: Insider → Stock
echo "FLOW 12: insider/transactions → insider/{ticker} + stock/{ticker}/*"
echo "--------------------------------------------------------------------------------"
insider_resp=$(api_call "/api/insider/transactions?limit=1")
insider_ticker=$(echo "$insider_resp" | uv run python -c "import sys, json; d=json.load(sys.stdin); print(d['data'][0]['ticker'] if d.get('data') else '')" 2>/dev/null)
insider_sector=$(echo "$insider_resp" | uv run python -c "import sys, json; d=json.load(sys.stdin); print(d['data'][0]['sector'] if d.get('data') else '')" 2>/dev/null)
echo "  Extracted: ticker=$insider_ticker, sector=$insider_sector"
if [ ! -z "$insider_ticker" ]; then
    echo "  Testing: /api/insider/$insider_ticker"
    insider_ticker_resp=$(api_call "/api/insider/$insider_ticker?limit=1")
    if echo "$insider_ticker_resp" | grep -q '"data"'; then
        echo "  ✓ SUCCESS: insider/transactions ticker → /api/insider/{ticker}"
        relationships+=("/api/insider/transactions[].ticker → /api/insider/{ticker}")
        relationships+=("/api/insider/transactions[].ticker → /api/stock/{ticker}/*")
    fi
fi
if [ ! -z "$insider_sector" ]; then
    echo "  Testing: /api/insider/$insider_sector/sector-flow"
    sector_flow=$(api_call "/api/insider/$insider_sector/sector-flow?limit=1")
    if echo "$sector_flow" | grep -q '"data"'; then
        echo "  ✓ SUCCESS: insider sector → /api/insider/{sector}/sector-flow"
        relationships+=("/api/insider/transactions[].sector → /api/insider/{sector}/sector-flow")
    fi
fi
echo ""

# FLOW 13: Seasonality → Stock
echo "FLOW 13: seasonality/market → seasonality/{ticker}/*"
echo "--------------------------------------------------------------------------------"
season_resp=$(api_call "/api/seasonality/market")
# Extract ticker from seasonality market (usually ETFs like SPY, QQQ, etc.)
season_ticker="AAPL"
echo "  Testing seasonality for ticker: $season_ticker"
echo "  Testing: /api/seasonality/$season_ticker/monthly"
season_monthly=$(api_call "/api/seasonality/$season_ticker/monthly")
if echo "$season_monthly" | grep -q '"data"'; then
    echo "  ✓ SUCCESS: ticker → /api/seasonality/{ticker}/monthly"
    relationships+=("/api/stock/{ticker}/* → /api/seasonality/{ticker}/monthly")
    relationships+=("/api/stock/{ticker}/* → /api/seasonality/{ticker}/year-month")
fi
echo ""

# FLOW 14: Earnings → Stock
echo "FLOW 14: earnings/* → earnings/{ticker} + stock/{ticker}/*"
echo "--------------------------------------------------------------------------------"
earn_resp=$(api_call "/api/earnings/premarket?limit=1")
earn_ticker=$(echo "$earn_resp" | uv run python -c "import sys, json; d=json.load(sys.stdin); print(d['data'][0]['ticker'] if d.get('data') else '')" 2>/dev/null)
echo "  Extracted from earnings/premarket: ticker=$earn_ticker"
if [ ! -z "$earn_ticker" ]; then
    echo "  Testing: /api/earnings/$earn_ticker"
    earn_ticker_resp=$(api_call "/api/earnings/$earn_ticker")
    if echo "$earn_ticker_resp" | grep -q '"data"'; then
        echo "  ✓ SUCCESS: earnings calendar ticker → /api/earnings/{ticker}"
        relationships+=("/api/earnings/premarket[].ticker → /api/earnings/{ticker}")
        relationships+=("/api/earnings/afterhours[].ticker → /api/earnings/{ticker}")
        relationships+=("/api/earnings/*[].ticker → /api/stock/{ticker}/*")
    fi
fi
echo ""

# FLOW 15: Shorts → Stock
echo "FLOW 15: Stock ticker → shorts/{ticker}/* endpoints"
echo "--------------------------------------------------------------------------------"
test_ticker="TSLA"
echo "  Testing shorts endpoints for: $test_ticker"
echo "  Testing: /api/shorts/$test_ticker/data"
shorts_data=$(api_call "/api/shorts/$test_ticker/data?limit=1")
if echo "$shorts_data" | grep -q '"data"'; then
    echo "  ✓ SUCCESS: ticker → /api/shorts/{ticker}/data"
    relationships+=("/api/stock/{ticker}/* → /api/shorts/{ticker}/data")
    relationships+=("/api/stock/{ticker}/* → /api/shorts/{ticker}/volume-and-ratio")
    relationships+=("/api/stock/{ticker}/* → /api/shorts/{ticker}/interest-float")
    relationships+=("/api/stock/{ticker}/* → /api/shorts/{ticker}/ftds")
    relationships+=("/api/stock/{ticker}/* → /api/shorts/{ticker}/volumes-by-exchange")
fi
echo ""

# FLOW 16: Greek Flow Relationships
echo "FLOW 16: stock/{ticker}/greek-flow variants"
echo "--------------------------------------------------------------------------------"
test_ticker="SPY"
echo "  Testing: /api/stock/$test_ticker/greek-flow"
greek_flow=$(api_call "/api/stock/$test_ticker/greek-flow")
if echo "$greek_flow" | grep -q '"data"'; then
    # Extract expiry from greek-flow
    expiry=$(echo "$greek_flow" | uv run python -c "import sys, json; d=json.load(sys.stdin); print(d['data'][0]['date'] if d.get('data') else '')" 2>/dev/null)
    echo "  ✓ Base greek-flow works"
    if [ ! -z "$expiry" ]; then
        echo "  Testing: /api/stock/$test_ticker/greek-flow/$expiry"
        greek_flow_expiry=$(api_call "/api/stock/$test_ticker/greek-flow/$expiry")
        if echo "$greek_flow_expiry" | grep -q '"data"'; then
            echo "  ✓ SUCCESS: greek-flow provides expiry → /api/stock/{ticker}/greek-flow/{expiry}"
            relationships+=("/api/stock/{ticker}/greek-flow[].date → /api/stock/{ticker}/greek-flow/{expiry}")
        fi
    fi
fi
echo ""

# FLOW 17: Stock Options Volume → OI relationships
echo "FLOW 17: stock/{ticker}/options-volume → stock/{ticker}/oi-* endpoints"
echo "--------------------------------------------------------------------------------"
test_ticker="AAPL"
echo "  Testing: /api/stock/$test_ticker/options-volume"
opt_vol=$(api_call "/api/stock/$test_ticker/options-volume")
if echo "$opt_vol" | grep -q '"data"'; then
    echo "  ✓ options-volume works"
    echo "  Testing: /api/stock/$test_ticker/oi-change"
    oi_change=$(api_call "/api/stock/$test_ticker/oi-change?limit=1")
    if echo "$oi_change" | grep -q '"data"'; then
        echo "  ✓ SUCCESS: Related endpoints for same ticker"
        relationships+=("/api/stock/{ticker}/options-volume ↔ /api/stock/{ticker}/oi-change")
        relationships+=("/api/stock/{ticker}/oi-change ↔ /api/stock/{ticker}/oi-per-expiry")
        relationships+=("/api/stock/{ticker}/oi-per-expiry ↔ /api/stock/{ticker}/oi-per-strike")
    fi
fi
echo ""

# FLOW 18: Spot Exposures Hierarchy
echo "FLOW 18: stock/{ticker}/spot-exposures variants"
echo "--------------------------------------------------------------------------------"
test_ticker="SPY"
echo "  Testing spot exposures hierarchy for: $test_ticker"
echo "  Testing: /api/stock/$test_ticker/spot-exposures"
spot_exp=$(api_call "/api/stock/$test_ticker/spot-exposures")
if echo "$spot_exp" | grep -q '"data"'; then
    echo "  ✓ Base spot-exposures works"
    relationships+=("/api/stock/{ticker}/spot-exposures → /api/stock/{ticker}/spot-exposures/strike")
    relationships+=("/api/stock/{ticker}/spot-exposures → /api/stock/{ticker}/spot-exposures/expiry-strike")
    relationships+=("/api/stock/{ticker}/spot-exposures → /api/stock/{ticker}/spot-exposures/{expiry}/strike")
fi
echo ""

# Print Summary
echo "================================================================================"
echo "ADDITIONAL RELATIONSHIPS DISCOVERED"
echo "================================================================================"
echo ""
for rel in "${relationships[@]}"; do
    echo "  ✓ $rel"
done
echo ""
echo "New relationships discovered: ${#relationships[@]}"
echo ""

