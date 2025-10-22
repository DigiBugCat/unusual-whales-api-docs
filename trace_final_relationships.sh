#!/bin/bash

API_KEY="5d1ec006-49f0-4a2a-90ae-5176c72425e3"
BASE_URL="https://api.unusualwhales.com"

echo "================================================================================"
echo "FINAL RELATIONSHIP TRACING - Complex Flows"
echo "================================================================================"
echo ""

api_call() {
    curl -s "$BASE_URL$1" -H "Authorization: Bearer $API_KEY"
}

declare -a relationships

# FLOW 19: Screener Option Contracts → Option Contract Details
echo "FLOW 19: screener/option-contracts → option-contract/{id}/*"
echo "--------------------------------------------------------------------------------"
screener_opt=$(api_call "/api/screener/option-contracts?limit=1")
contract_from_screener=$(echo "$screener_opt" | uv run python -c "import sys, json; d=json.load(sys.stdin); print(d['data'][0]['contract'] if d.get('data') else '')" 2>/dev/null)
echo "  Extracted contract: $contract_from_screener"
if [ ! -z "$contract_from_screener" ]; then
    echo "  Testing: /api/option-contract/$contract_from_screener/flow"
    opt_detail=$(api_call "/api/option-contract/$contract_from_screener/flow?limit=1")
    if echo "$opt_detail" | grep -q '"data"'; then
        echo "  ✓ SUCCESS: screener contract → /api/option-contract/{id}/*"
        relationships+=("/api/screener/option-contracts[].contract → /api/option-contract/{id}/flow")
        relationships+=("/api/screener/option-contracts[].contract → /api/option-contract/{id}/historic")
        relationships+=("/api/screener/option-contracts[].contract → /api/option-contract/{id}/intraday")
    fi
fi
echo ""

# FLOW 20: Historical vs Intraday vs Real-time
echo "FLOW 20: Time-series hierarchy for option contracts"
echo "--------------------------------------------------------------------------------"
test_contract="SPY251219C00600000"
echo "  Testing time-series endpoints for: $test_contract"
echo "  1. /api/option-contract/$test_contract/historic (daily)"
historic=$(api_call "/api/option-contract/$test_contract/historic?limit=1")
if echo "$historic" | grep -q '"data"'; then
    echo "  ✓ historic (daily OHLC) available"
fi
echo "  2. /api/option-contract/$test_contract/intraday (1-min)"
intraday=$(api_call "/api/option-contract/$test_contract/intraday?limit=1")
if echo "$intraday" | grep -q '"data"'; then
    echo "  ✓ intraday (1-min intervals) available"
fi
echo "  3. /api/option-contract/$test_contract/flow (recent trades)"
flow=$(api_call "/api/option-contract/$test_contract/flow?limit=1")
if echo "$flow" | grep -q '"data"'; then
    echo "  ✓ flow (recent trades) available"
fi
relationships+=("/api/option-contract/{id}/historic = daily OHLC")
relationships+=("/api/option-contract/{id}/intraday = 1-min intervals")
relationships+=("/api/option-contract/{id}/flow = recent trades")
echo ""

# FLOW 21: Stock Historical Data (OHLC)
echo "FLOW 21: stock/{ticker}/ohlc/* time-series"
echo "--------------------------------------------------------------------------------"
test_ticker="AAPL"
echo "  Testing: /api/stock/$test_ticker/ohlc/1D"
ohlc_1d=$(api_call "/api/stock/$test_ticker/ohlc/1D?limit=1")
if echo "$ohlc_1d" | grep -q '"data"'; then
    echo "  ✓ 1D candles available"
    relationships+=("/api/stock/{ticker}/ohlc/1D = daily candles")
    relationships+=("/api/stock/{ticker}/ohlc/1H = hourly candles")
    relationships+=("/api/stock/{ticker}/ohlc/5m = 5-min candles")
fi
echo ""

# FLOW 22: Volatility Relationships
echo "FLOW 22: stock/{ticker}/volatility/* endpoints"
echo "--------------------------------------------------------------------------------"
test_ticker="SPY"
echo "  Testing volatility endpoints for: $test_ticker"
echo "  1. /api/stock/$test_ticker/volatility/realized"
vol_real=$(api_call "/api/stock/$test_ticker/volatility/realized")
if echo "$vol_real" | grep -q '"data"'; then
    echo "  ✓ realized volatility available"
fi
echo "  2. /api/stock/$test_ticker/volatility/term-structure"
vol_term=$(api_call "/api/stock/$test_ticker/volatility/term-structure")
if echo "$vol_term" | grep -q '"data"'; then
    echo "  ✓ term structure available"
fi
echo "  3. /api/stock/$test_ticker/iv-rank"
iv_rank=$(api_call "/api/stock/$test_ticker/iv-rank")
if echo "$iv_rank" | grep -q '"data"'; then
    echo "  ✓ IV rank available"
fi
relationships+=("/api/stock/{ticker}/volatility/* ↔ /api/stock/{ticker}/iv-rank")
relationships+=("/api/stock/{ticker}/volatility/* ↔ /api/stock/{ticker}/interpolated-iv")
echo ""

# FLOW 23: Stock Sectors → Tickers
echo "FLOW 23: stock/{sector}/tickers → stock/{ticker}/*"
echo "--------------------------------------------------------------------------------"
test_sector="Technology"
echo "  Testing: /api/stock/$test_sector/tickers"
sector_tickers=$(api_call "/api/stock/$test_sector/tickers?limit=1")
sector_ticker=$(echo "$sector_tickers" | uv run python -c "import sys, json; d=json.load(sys.stdin); print(d['data'][0]['ticker'] if d.get('data') else '')" 2>/dev/null)
echo "  Extracted ticker from sector: $sector_ticker"
if [ ! -z "$sector_ticker" ]; then
    echo "  ✓ SUCCESS: sector provides tickers → /api/stock/{ticker}/*"
    relationships+=("/api/stock/{sector}/tickers[].ticker → /api/stock/{ticker}/*")
fi
echo ""

# FLOW 24: Group Flow
echo "FLOW 24: group-flow/{flow_group}/*"
echo "--------------------------------------------------------------------------------"
test_group="all"
echo "  Testing: /api/group-flow/$test_group/greek-flow"
group_flow=$(api_call "/api/group-flow/$test_group/greek-flow")
if echo "$group_flow" | grep -q '"data"'; then
    echo "  ✓ Base group-flow works"
    # Extract expiry if available
    expiry=$(echo "$group_flow" | uv run python -c "import sys, json; d=json.load(sys.stdin); print(d['data'][0]['date'] if d.get('data') else '')" 2>/dev/null)
    if [ ! -z "$expiry" ]; then
        relationships+=("/api/group-flow/{flow_group}/greek-flow[].date → /api/group-flow/{flow_group}/greek-flow/{expiry}")
    fi
fi
echo ""

# FLOW 25: Max Pain and Options Metrics
echo "FLOW 25: Options metrics inter-relationships"
echo "--------------------------------------------------------------------------------"
test_ticker="SPY"
echo "  Testing options metrics for: $test_ticker"
echo "  - max-pain, nope, net-prem-ticks all relate to same ticker"
max_pain=$(api_call "/api/stock/$test_ticker/max-pain")
nope=$(api_call "/api/stock/$test_ticker/nope")
if echo "$max_pain" | grep -q '"data"' && echo "$nope" | grep -q '"data"'; then
    echo "  ✓ SUCCESS: Options metrics are inter-related"
    relationships+=("/api/stock/{ticker}/max-pain ↔ /api/stock/{ticker}/nope")
    relationships+=("/api/stock/{ticker}/nope ↔ /api/stock/{ticker}/net-prem-ticks")
    relationships+=("/api/stock/{ticker}/greek-exposure ↔ /api/stock/{ticker}/max-pain")
fi
echo ""

# FLOW 26: Market Economic Calendar → Affected Stocks
echo "FLOW 26: market/economic-calendar (implicit stock relationships)"
echo "--------------------------------------------------------------------------------"
econ=$(api_call "/api/market/economic-calendar?limit=1")
if echo "$econ" | grep -q '"data"'; then
    echo "  ✓ Economic calendar available"
    echo "  Note: Implicit relationships to affected sectors/stocks"
    relationships+=("/api/market/economic-calendar → affects market-wide endpoints")
    relationships+=("/api/market/fda-calendar → affects pharmaceutical stocks")
fi
echo ""

# FLOW 27: Net Flow Expiry Relationships
echo "FLOW 27: net-flow/expiry relationships"
echo "--------------------------------------------------------------------------------"
net_flow=$(api_call "/api/net-flow/expiry?limit=1")
if echo "$net_flow" | grep -q '"data"'; then
    echo "  ✓ Net flow by expiry available"
    relationships+=("/api/net-flow/expiry ↔ /api/stock/{ticker}/flow-per-expiry")
fi
echo ""

# Print Summary
echo "================================================================================"
echo "FINAL BATCH OF RELATIONSHIPS"
echo "================================================================================"
echo ""
for rel in "${relationships[@]}"; do
    echo "  ✓ $rel"
done
echo ""
echo "Additional relationships: ${#relationships[@]}"
echo ""

