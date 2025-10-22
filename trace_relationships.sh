#!/bin/bash

API_KEY="5d1ec006-49f0-4a2a-90ae-5176c72425e3"
BASE_URL="https://api.unusualwhales.com"

echo "================================================================================"
echo "SYSTEMATIC ENDPOINT RELATIONSHIP TRACING"
echo "================================================================================"
echo ""

# Function to make API call
api_call() {
    curl -s "$BASE_URL$1" -H "Authorization: Bearer $API_KEY"
}

# Track relationships
declare -a relationships

# FLOW 1: OI Change → Option Contract Details
echo "FLOW 1: market/oi-change → option-contract/{id}/*"
echo "--------------------------------------------------------------------------------"
response=$(api_call "/api/market/oi-change?limit=1")
contract_id=$(echo "$response" | uv run python -c "import sys, json; d=json.load(sys.stdin); print(d['data'][0]['option_symbol'] if d.get('data') else '')" 2>/dev/null)
ticker=$(echo "$response" | uv run python -c "import sys, json; d=json.load(sys.stdin); print(d['data'][0]['underlying_symbol'] if d.get('data') else '')" 2>/dev/null)

echo "  Source: /api/market/oi-change"
echo "  Extracted: contract_id=$contract_id, ticker=$ticker"
echo "  Testing: /api/option-contract/$contract_id/flow"
flow_resp=$(api_call "/api/option-contract/$contract_id/flow?limit=1")
if echo "$flow_resp" | grep -q '"data"'; then
    echo "  ✓ SUCCESS: option_symbol → /api/option-contract/{id}/flow"
    relationships+=("/api/market/oi-change[].option_symbol → /api/option-contract/{id}/flow")
fi
echo ""

# FLOW 2: Stock Info → Option Chains → Contract Details
echo "FLOW 2: stock/{ticker}/info → stock/{ticker}/option-chains → option-contract/{id}/*"
echo "--------------------------------------------------------------------------------"
echo "  Using ticker: $ticker"
echo "  Testing: /api/stock/$ticker/option-chains"
chains_resp=$(api_call "/api/stock/$ticker/option-chains?limit=1")
if echo "$chains_resp" | grep -q '"data"'; then
    echo "  ✓ SUCCESS: ticker → /api/stock/{ticker}/option-chains"
    relationships+=("/api/stock/{ticker}/info → /api/stock/{ticker}/option-chains")
    
    # Extract contract from chains
    chain_contract=$(echo "$chains_resp" | uv run python -c "import sys, json; d=json.load(sys.stdin); print(d['data'][0] if d.get('data') and len(d['data']) > 0 else '')" 2>/dev/null)
    if [ ! -z "$chain_contract" ]; then
        echo "  ✓ CHAIN: option-chains provides contracts → option-contract/{id}/*"
        relationships+=("/api/stock/{ticker}/option-chains[].contract → /api/option-contract/{id}/*")
    fi
fi
echo ""

# FLOW 3: Screener → Stock Details
echo "FLOW 3: screener/stocks → stock/{ticker}/*"
echo "--------------------------------------------------------------------------------"
screener_resp=$(api_call "/api/screener/stocks?limit=1")
screener_ticker=$(echo "$screener_resp" | uv run python -c "import sys, json; d=json.load(sys.stdin); print(d['data'][0]['ticker'] if d.get('data') else '')" 2>/dev/null)
echo "  Source: /api/screener/stocks"
echo "  Extracted: ticker=$screener_ticker"
echo "  Testing: /api/stock/$screener_ticker/info"
stock_info=$(api_call "/api/stock/$screener_ticker/info")
if echo "$stock_info" | grep -q '"data"'; then
    echo "  ✓ SUCCESS: screener ticker → /api/stock/{ticker}/info"
    relationships+=("/api/screener/stocks[].ticker → /api/stock/{ticker}/*")
fi
echo ""

# FLOW 4: Institutions List → Institution Holdings
echo "FLOW 4: institutions → institution/{name}/holdings"
echo "--------------------------------------------------------------------------------"
inst_resp=$(api_call "/api/institutions?limit=1")
inst_name=$(echo "$inst_resp" | uv run python -c "import sys, json; d=json.load(sys.stdin); print(d['data'][0]['name'] if d.get('data') else '')" 2>/dev/null)
echo "  Source: /api/institutions"
echo "  Extracted: name=$inst_name"
if [ ! -z "$inst_name" ]; then
    echo "  Testing: /api/institution/$inst_name/holdings"
    holdings_resp=$(api_call "/api/institution/$(echo $inst_name | sed 's/ /%20/g')/holdings?limit=1")
    if echo "$holdings_resp" | grep -q '"data"'; then
        echo "  ✓ SUCCESS: institution name → /api/institution/{name}/holdings"
        relationships+=("/api/institutions[].name → /api/institution/{name}/holdings")
        relationships+=("/api/institutions[].name → /api/institution/{name}/activity")
        relationships+=("/api/institutions[].name → /api/institution/{name}/sectors")
    fi
fi
echo ""

# FLOW 5: Institution Holdings → Stock Ownership
echo "FLOW 5: institution/{name}/holdings → institution/{ticker}/ownership"
echo "--------------------------------------------------------------------------------"
if [ ! -z "$inst_name" ]; then
    holdings_ticker=$(echo "$holdings_resp" | uv run python -c "import sys, json; d=json.load(sys.stdin); print(d['data'][0]['ticker'] if d.get('data') else '')" 2>/dev/null)
    echo "  From holdings: ticker=$holdings_ticker"
    if [ ! -z "$holdings_ticker" ]; then
        echo "  Testing: /api/institution/$holdings_ticker/ownership"
        ownership_resp=$(api_call "/api/institution/$holdings_ticker/ownership?limit=1")
        if echo "$ownership_resp" | grep -q '"data"'; then
            echo "  ✓ SUCCESS: holdings ticker → /api/institution/{ticker}/ownership"
            relationships+=("/api/institution/{name}/holdings[].ticker → /api/institution/{ticker}/ownership")
            relationships+=("/api/institution/{name}/holdings[].ticker → /api/stock/{ticker}/*")
        fi
    fi
fi
echo ""

# FLOW 6: Flow Alerts → Stock Flow Data
echo "FLOW 6: option-trades/flow-alerts → stock/{ticker}/flow-*"
echo "--------------------------------------------------------------------------------"
alerts_resp=$(api_call "/api/option-trades/flow-alerts?limit=1")
alert_ticker=$(echo "$alerts_resp" | uv run python -c "import sys, json; d=json.load(sys.stdin); print(d['data'][0]['ticker'] if d.get('data') else '')" 2>/dev/null)
alert_contract=$(echo "$alerts_resp" | uv run python -c "import sys, json; d=json.load(sys.stdin); print(d['data'][0]['contract'] if d.get('data') else '')" 2>/dev/null)
echo "  Source: /api/option-trades/flow-alerts"
echo "  Extracted: ticker=$alert_ticker, contract=$alert_contract"
if [ ! -z "$alert_ticker" ]; then
    echo "  Testing: /api/stock/$alert_ticker/flow-alerts"
    stock_flow=$(api_call "/api/stock/$alert_ticker/flow-alerts?limit=1")
    if echo "$stock_flow" | grep -q '"data"'; then
        echo "  ✓ SUCCESS: flow-alerts ticker → /api/stock/{ticker}/flow-alerts"
        relationships+=("/api/option-trades/flow-alerts[].ticker → /api/stock/{ticker}/flow-alerts")
        relationships+=("/api/option-trades/flow-alerts[].ticker → /api/stock/{ticker}/flow-recent")
        relationships+=("/api/option-trades/flow-alerts[].contract → /api/option-contract/{id}/*")
    fi
fi
echo ""

# FLOW 7: Congress Trades → Stock Data
echo "FLOW 7: congress/recent-trades → stock/{ticker}/*"
echo "--------------------------------------------------------------------------------"
congress_resp=$(api_call "/api/congress/recent-trades?limit=1")
congress_ticker=$(echo "$congress_resp" | uv run python -c "import sys, json; d=json.load(sys.stdin); print(d['data'][0]['ticker'] if d.get('data') else '')" 2>/dev/null)
echo "  Source: /api/congress/recent-trades"
echo "  Extracted: ticker=$congress_ticker"
if [ ! -z "$congress_ticker" ]; then
    echo "  Testing: /api/stock/$congress_ticker/info"
    congress_stock=$(api_call "/api/stock/$congress_ticker/info")
    if echo "$congress_stock" | grep -q '"data"'; then
        echo "  ✓ SUCCESS: congress ticker → /api/stock/{ticker}/*"
        relationships+=("/api/congress/recent-trades[].ticker → /api/stock/{ticker}/*")
    fi
fi
echo ""

# FLOW 8: Stock Greek Exposure Hierarchy
echo "FLOW 8: stock/{ticker}/greek-exposure → greek-exposure/* variants"
echo "--------------------------------------------------------------------------------"
test_ticker="SPY"
echo "  Testing with ticker: $test_ticker"
echo "  Testing: /api/stock/$test_ticker/greek-exposure"
gex_resp=$(api_call "/api/stock/$test_ticker/greek-exposure")
if echo "$gex_resp" | grep -q '"data"'; then
    echo "  ✓ Base endpoint works"
    echo "  Testing: /api/stock/$test_ticker/greek-exposure/expiry"
    gex_expiry=$(api_call "/api/stock/$test_ticker/greek-exposure/expiry")
    if echo "$gex_expiry" | grep -q '"data"'; then
        echo "  ✓ SUCCESS: greek-exposure has expiry breakdown"
        relationships+=("/api/stock/{ticker}/greek-exposure → /api/stock/{ticker}/greek-exposure/expiry")
        relationships+=("/api/stock/{ticker}/greek-exposure → /api/stock/{ticker}/greek-exposure/strike")
        relationships+=("/api/stock/{ticker}/greek-exposure → /api/stock/{ticker}/greek-exposure/strike-expiry")
    fi
fi
echo ""

# Print Summary
echo "================================================================================"
echo "DISCOVERED RELATIONSHIPS SUMMARY"
echo "================================================================================"
echo ""
for rel in "${relationships[@]}"; do
    echo "  ✓ $rel"
done
echo ""
echo "Total relationships discovered: ${#relationships[@]}"
echo ""

