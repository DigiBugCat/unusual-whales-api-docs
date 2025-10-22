# Unusual Whales API - Data Flow Examples

**Practical integration patterns showing how to chain API endpoints**

---

## Table of Contents

1. [Finding Hot Options Activity](#1-finding-hot-options-activity)
2. [Institutional Position Tracking](#2-institutional-position-tracking)
3. [Options Greeks Analysis](#3-options-greeks-analysis)
4. [Congress Trading Tracker](#4-congress-trading-tracker)
5. [Short Squeeze Detector](#5-short-squeeze-detector)
6. [Earnings Play Scanner](#6-earnings-play-scanner)
7. [ETF Rebalancing Impact](#7-etf-rebalancing-impact)
8. [Real-Time Flow Monitoring](#8-real-time-flow-monitoring)

---

## 1. Finding Hot Options Activity

**Use Case**: Find stocks with unusual options activity and analyze the details

### Flow

```
1. Get flow alerts
2. Extract ticker and contract
3. Get stock info
4. Get greek exposure
5. Get contract details
```

### Implementation

```bash
#!/bin/bash
API_KEY="your_api_key"
BASE="https://api.unusualwhales.com"

# Step 1: Get top flow alerts
echo "Finding unusual options activity..."
alerts=$(curl -s "$BASE/api/option-trades/flow-alerts?limit=5" \
  -H "Authorization: Bearer $API_KEY")

# Step 2: Extract first ticker and contract
ticker=$(echo "$alerts" | jq -r '.data[0].ticker')
contract=$(echo "$alerts" | jq -r '.data[0].contract')
sentiment=$(echo "$alerts" | jq -r '.data[0].sentiment')

echo "Top alert: $ticker ($sentiment sentiment)"

# Step 3: Get stock context
echo "Fetching stock info..."
stock_info=$(curl -s "$BASE/api/stock/$ticker/info" \
  -H "Authorization: Bearer $API_KEY")

price=$(echo "$stock_info" | jq -r '.data.last_price')
mcap=$(echo "$stock_info" | jq -r '.data.marketcap')

echo "Price: \$$price, Market Cap: \$$mcap"

# Step 4: Get greek exposure (GEX levels)
echo "Checking gamma exposure..."
gex=$(curl -s "$BASE/api/stock/$ticker/greek-exposure" \
  -H "Authorization: Bearer $API_KEY")

net_gex=$(echo "$gex" | jq -r '.data[0].net_gamma // "N/A"')
echo "Net GEX: $net_gex"

# Step 5: Get contract flow details
if [ ! -z "$contract" ] && [ "$contract" != "null" ]; then
    echo "Analyzing contract: $contract"
    flow=$(curl -s "$BASE/api/option-contract/$contract/flow?limit=10" \
      -H "Authorization: Bearer $API_KEY")

    total_premium=$(echo "$flow" | jq '[.data[].cost_basis] | add')
    echo "Total premium in recent trades: \$$total_premium"
fi
```

### Expected Output

```
Finding unusual options activity...
Top alert: TSLA (bullish sentiment)
Fetching stock info...
Price: $245.50, Market Cap: $780B
Checking gamma exposure...
Net GEX: 125000000
Analyzing contract: TSLA251219C00250000
Total premium in recent trades: $1250000
```

---

## 2. Institutional Position Tracking

**Use Case**: Monitor what major institutions are buying/selling

### Flow

```
1. List top institutions
2. Get their holdings
3. Identify position changes
4. Check stock ownership concentration
5. Analyze underlying stocks
```

### Implementation

```python
import requests

API_KEY = "your_api_key"
BASE = "https://api.unusualwhales.com"
headers = {"Authorization": f"Bearer {API_KEY}"}

# Step 1: Get top institutions
print("Fetching top institutions...")
institutions = requests.get(
    f"{BASE}/api/institutions?limit=10",
    headers=headers
).json()

for inst in institutions['data'][:3]:
    name = inst['name']
    print(f"\n=== {name} ===")

    # Step 2: Get holdings
    holdings = requests.get(
        f"{BASE}/api/institution/{name}/holdings?limit=10",
        headers=headers
    ).json()

    # Step 3: Identify changes
    for holding in holdings['data']:
        ticker = holding['ticker']
        units_change = holding['units_change']
        value = holding['value']

        if units_change > 0:
            action = "INCREASED"
        elif units_change < 0:
            action = "DECREASED"
        else:
            action = "MAINTAINED"

        print(f"{ticker}: {action} position (${value:,})")

        # Step 4: Check ownership concentration
        ownership = requests.get(
            f"{BASE}/api/institution/{ticker}/ownership?limit=5",
            headers=headers
        ).json()

        total_institutional = sum(h['value'] for h in ownership['data'])
        print(f"  Total institutional ownership: ${total_institutional:,}")
```

### Expected Output

```
Fetching top institutions...

=== VANGUARD GROUP INC ===
AAPL: INCREASED position ($50,000,000,000)
  Total institutional ownership: $250,000,000,000
MSFT: MAINTAINED position ($45,000,000,000)
  Total institutional ownership: $200,000,000,000
NVDA: INCREASED position ($30,000,000,000)
  Total institutional ownership: $150,000,000,000
```

---

## 3. Options Greeks Analysis

**Use Case**: Deep dive into a stock's options exposure

### Flow

```
1. Get stock info
2. Get overall greek exposure
3. Break down by expiration
4. Break down by strike
5. Find max pain
6. Calculate support/resistance
```

### Implementation

```python
import requests
import pandas as pd

API_KEY = "your_api_key"
BASE = "https://api.unusualwhales.com"
headers = {"Authorization": f"Bearer {API_KEY}"}

ticker = "SPY"

# Step 1: Stock info
print(f"Analyzing {ticker} options greeks...")
info = requests.get(f"{BASE}/api/stock/{ticker}/info", headers=headers).json()
price = float(info['data']['last_price'])
print(f"Current price: ${price}")

# Step 2: Overall GEX
gex = requests.get(f"{BASE}/api/stock/{ticker}/greek-exposure", headers=headers).json()
net_gamma = sum(float(d['net_gamma']) for d in gex['data'] if d.get('net_gamma'))
print(f"Net Gamma Exposure: {net_gamma:,.0f}")

# Step 3: GEX by expiration
gex_expiry = requests.get(
    f"{BASE}/api/stock/{ticker}/greek-exposure/expiry",
    headers=headers
).json()

print("\nGamma by Expiration:")
for exp in gex_expiry['data'][:5]:
    date = exp['expiration']
    gamma = float(exp.get('net_gamma', 0))
    print(f"  {date}: {gamma:,.0f}")

# Step 4: GEX by strike
gex_strike = requests.get(
    f"{BASE}/api/stock/{ticker}/greek-exposure/strike",
    headers=headers
).json()

# Find strikes with highest GEX
strikes_df = pd.DataFrame(gex_strike['data'])
strikes_df['net_gamma'] = pd.to_numeric(strikes_df['net_gamma'])
top_strikes = strikes_df.nlargest(5, 'net_gamma')

print("\nTop Gamma Strikes (potential pinning levels):")
for _, row in top_strikes.iterrows():
    print(f"  ${row['strike']}: {row['net_gamma']:,.0f}")

# Step 5: Max pain
max_pain = requests.get(
    f"{BASE}/api/stock/{ticker}/max-pain",
    headers=headers
).json()

mp_price = max_pain['data'][0]['max_pain_price']
print(f"\nMax Pain: ${mp_price}")
print(f"Distance from current: ${abs(price - float(mp_price)):.2f}")
```

---

## 4. Congress Trading Tracker

**Use Case**: Track congressional trades and correlate with stock performance

### Flow

```
1. Get recent congress trades
2. Group by ticker
3. Get stock info and price history
4. Calculate returns since trade
5. Identify patterns
```

### Implementation

```javascript
const API_KEY = "your_api_key";
const BASE = "https://api.unusualwhales.com";

async function trackCongressTrades() {
    // Step 1: Get recent trades
    const trades = await fetch(`${BASE}/api/congress/recent-trades?limit=50`, {
        headers: { 'Authorization': `Bearer ${API_KEY}` }
    }).then(r => r.json());

    // Step 2: Group by ticker
    const byTicker = {};
    trades.data.forEach(trade => {
        if (!byTicker[trade.ticker]) {
            byTicker[trade.ticker] = [];
        }
        byTicker[trade.ticker].push(trade);
    });

    // Step 3: Analyze each ticker
    for (const [ticker, tickerTrades] of Object.entries(byTicker)) {
        console.log(`\n${ticker}:`);

        // Get stock info
        const info = await fetch(`${BASE}/api/stock/${ticker}/info`, {
            headers: { 'Authorization': `Bearer ${API_KEY}` }
        }).then(r => r.json());

        const currentPrice = parseFloat(info.data.last_price);

        // Analyze trades
        const buys = tickerTrades.filter(t => t.type === 'purchase');
        const sells = tickerTrades.filter(t => t.type === 'sale');

        console.log(`  Current Price: $${currentPrice}`);
        console.log(`  Buys: ${buys.length}, Sells: ${sells.length}`);

        if (buys.length > sells.length) {
            console.log(`  ⬆️  Net BULLISH (${buys.length - sells.length} more buys)`);
        } else if (sells.length > buys.length) {
            console.log(`  ⬇️  Net BEARISH (${sells.length - buys.length} more sells)`);
        }
    }
}

trackCongressTrades();
```

---

## 5. Short Squeeze Detector

**Use Case**: Find stocks with short squeeze potential

### Flow

```
1. Screen for high short interest
2. Get borrow rates
3. Check failure to delivers
4. Analyze recent short volume
5. Check options activity (gamma squeeze potential)
6. Calculate squeeze score
```

### Implementation

```python
import requests

API_KEY = "your_api_key"
BASE = "https://api.unusualwhales.com"
headers = {"Authorization": f"Bearer {API_KEY}"}

def analyze_short_squeeze_potential(ticker):
    """Comprehensive short squeeze analysis"""

    print(f"\n{'='*60}")
    print(f"Short Squeeze Analysis: {ticker}")
    print(f"{'='*60}")

    # Step 1: Short interest and float
    si_data = requests.get(
        f"{BASE}/api/shorts/{ticker}/interest-float",
        headers=headers
    ).json()

    if si_data['data']:
        si = si_data['data'][0]
        short_interest_pct = float(si.get('short_interest_pct', 0))
        days_to_cover = float(si.get('days_to_cover', 0))
        print(f"Short Interest: {short_interest_pct:.2f}%")
        print(f"Days to Cover: {days_to_cover:.2f}")

    # Step 2: Borrow rates
    borrow_data = requests.get(
        f"{BASE}/api/shorts/{ticker}/data?limit=1",
        headers=headers
    ).json()

    if borrow_data['data']:
        rate = borrow_data['data'][0].get('fee_rate', 0)
        print(f"Borrow Rate: {rate}%")

    # Step 3: Short volume trend
    volume_data = requests.get(
        f"{BASE}/api/shorts/{ticker}/volume-and-ratio?limit=10",
        headers=headers
    ).json()

    if volume_data['data']:
        recent_ratios = [float(d['short_ratio']) for d in volume_data['data']]
        avg_short_ratio = sum(recent_ratios) / len(recent_ratios)
        print(f"Avg Short Ratio (10d): {avg_short_ratio:.2f}")

    # Step 4: Check gamma exposure (potential gamma squeeze)
    gex_data = requests.get(
        f"{BASE}/api/stock/{ticker}/greek-exposure",
        headers=headers
    ).json()

    if gex_data['data']:
        net_gamma = sum(float(d.get('net_gamma', 0)) for d in gex_data['data'])
        print(f"Net Gamma Exposure: {net_gamma:,.0f}")

        if net_gamma > 0:
            print("⚠️  Positive gamma = potential gamma squeeze")

    # Calculate squeeze score (0-100)
    score = 0
    if short_interest_pct > 20:
        score += 30
    if float(rate) > 10:
        score += 25
    if avg_short_ratio > 0.4:
        score += 20
    if net_gamma > 0:
        score += 25

    print(f"\n🎯 Squeeze Score: {score}/100")

    if score > 70:
        print("🔥 HIGH squeeze potential!")
    elif score > 50:
        print("⚠️  MODERATE squeeze potential")
    else:
        print("✓ LOW squeeze potential")

# Test with known stocks
for ticker in ['GME', 'TSLA', 'AAPL']:
    analyze_short_squeeze_potential(ticker)
```

---

## 6. Earnings Play Scanner

**Use Case**: Find earnings opportunities and position analysis

### Flow

```
1. Get upcoming earnings
2. For each ticker:
   - Historical earnings performance
   - Current options activity
   - IV rank (high = expensive options)
   - Max pain level
3. Rank opportunities
```

### Implementation

```bash
#!/bin/bash
API_KEY="your_api_key"
BASE="https://api.unusualwhales.com"

echo "=== EARNINGS PLAY SCANNER ==="
echo ""

# Get premarket earnings
echo "Premarket Earnings:"
premarket=$(curl -s "$BASE/api/earnings/premarket" \
  -H "Authorization: Bearer $API_KEY")

echo "$premarket" | jq -r '.data[0:5][] | "\(.ticker) - \(.name) (EPS: \(.eps_estimate))"'

# Analyze first ticker
ticker=$(echo "$premarket" | jq -r '.data[0].ticker')
echo ""
echo "Analyzing $ticker..."

# Historical earnings
historical=$(curl -s "$BASE/api/earnings/$ticker" \
  -H "Authorization: Bearer $API_KEY")

echo "Historical earnings performance:"
echo "$historical" | jq -r '.data[0:3][] | "  \(.date): Actual \(.actual_eps) vs Est \(.eps_estimate)"'

# IV Rank (options expensiveness)
iv_rank=$(curl -s "$BASE/api/stock/$ticker/iv-rank" \
  -H "Authorization: Bearer $API_KEY")

iv=$(echo "$iv_rank" | jq -r '.data[0].iv_rank')
echo ""
echo "IV Rank: $iv% (>50 = expensive options)"

# Options flow (positioning)
flow=$(curl -s "$BASE/api/stock/$ticker/flow-alerts?limit=10" \
  -H "Authorization: Bearer $API_KEY")

calls=$(echo "$flow" | jq '[.data[] | select(.sentiment == "bullish")] | length')
puts=$(echo "$flow" | jq '[.data[] | select(.sentiment == "bearish")] | length')

echo "Recent flow: $calls calls vs $puts puts"

if [ $calls -gt $puts ]; then
    echo "✓ Net BULLISH positioning"
else
    echo "✓ Net BEARISH positioning"
fi
```

---

## 7. ETF Rebalancing Impact

**Use Case**: Predict rebalancing flows and impacts

### Flow

```
1. Get ETF holdings
2. Calculate weights
3. Compare to target allocations
4. Estimate rebalancing flows
5. Check impact on underlying stocks
```

### Implementation

```python
import requests
import pandas as pd

API_KEY = "your_api_key"
BASE = "https://api.unusualwhales.com"
headers = {"Authorization": f"Bearer {API_KEY}"}

def analyze_etf_rebalancing(etf_ticker):
    print(f"Analyzing {etf_ticker} rebalancing impact...")

    # Get ETF info
    info = requests.get(
        f"{BASE}/api/etfs/{etf_ticker}/info",
        headers=headers
    ).json()

    aum = float(info['data']['aum'])
    print(f"AUM: ${aum/1e9:.2f}B")

    # Get current holdings
    holdings = requests.get(
        f"{BASE}/api/etfs/{etf_ticker}/holdings",
        headers=headers
    ).json()

    # Get current weights
    weights = requests.get(
        f"{BASE}/api/etfs/{etf_ticker}/weights",
        headers=headers
    ).json()

    # Analyze top holdings
    print("\nTop 10 Holdings:")
    for holding in holdings['data'][:10]:
        ticker = holding['ticker']
        weight = float(holding.get('weight', 0))
        shares = int(holding.get('shares', 0))

        print(f"{ticker}: {weight:.2f}% ({shares:,} shares)")

        # Estimate impact of 1% rebalancing
        rebalance_value = aum * weight * 0.01
        print(f"  1% rebalance = ${rebalance_value/1e6:.2f}M")

        # Check stock's options activity
        flow = requests.get(
            f"{BASE}/api/stock/{ticker}/flow-recent?limit=5",
            headers=headers
        ).json()

        if flow['data']:
            print(f"  Recent options activity: {len(flow['data'])} trades")

# Analyze major ETFs
for etf in ['SPY', 'QQQ', 'IWM']:
    analyze_etf_rebalancing(etf)
    print("\n" + "="*60 + "\n")
```

---

## 8. Real-Time Flow Monitoring

**Use Case**: Monitor options flow in real-time

### Flow

```
1. Get initial state (recent flow alerts)
2. Connect to WebSocket for live updates
3. For each alert:
   - Get contract details
   - Check stock exposure
   - Calculate impact
4. Alert on significant flows
```

### Implementation (Conceptual - WebSocket)

```python
import requests
import websocket
import json

API_KEY = "your_api_key"
BASE = "https://api.unusualwhales.com"
WS_BASE = "wss://api.unusualwhales.com"

# Step 1: Get initial state via REST
headers = {"Authorization": f"Bearer {API_KEY}"}
initial_flow = requests.get(
    f"{BASE}/api/option-trades/flow-alerts?limit=20",
    headers=headers
).json()

print(f"Loaded {len(initial_flow['data'])} recent alerts")

# Step 2: Connect to WebSocket for live updates
def on_message(ws, message):
    data = json.loads(message)

    # Step 3: Analyze each alert
    if data['type'] == 'flow_alert':
        ticker = data['ticker']
        contract = data['contract']
        premium = data['premium']
        sentiment = data['sentiment']

        print(f"\n🚨 ALERT: {ticker} ({sentiment})")
        print(f"   Contract: {contract}")
        print(f"   Premium: ${premium:,}")

        # Get additional context via REST
        gex = requests.get(
            f"{BASE}/api/stock/{ticker}/greek-exposure",
            headers=headers
        ).json()

        if gex['data']:
            net_gamma = sum(float(d.get('net_gamma', 0)) for d in gex['data'])
            print(f"   Net GEX: {net_gamma:,.0f}")

        # Step 4: Alert threshold
        if float(premium) > 1000000:  # $1M+
            print(f"   ⚠️  LARGE FLOW - Premium > $1M!")

def on_error(ws, error):
    print(f"Error: {error}")

def on_close(ws, close_status_code, close_msg):
    print("WebSocket closed")

def on_open(ws):
    print("WebSocket connected - monitoring flow...")
    # Subscribe to flow alerts channel
    ws.send(json.dumps({
        "action": "subscribe",
        "channel": "flow_alerts"
    }))

# Connect
ws = websocket.WebSocketApp(
    f"{WS_BASE}/api/socket/flow_alerts",
    header={"Authorization": f"Bearer {API_KEY}"},
    on_message=on_message,
    on_error=on_error,
    on_close=on_close,
    on_open=on_open
)

ws.run_forever()
```

---

## Common Patterns Summary

| Pattern | Entry Point | Key Endpoints | Output |
|---------|-------------|---------------|--------|
| Hot Activity | flow-alerts | stock/*, option-contract/* | Unusual options trades |
| Institutional | institutions | institution/*, stock/* | Major position changes |
| Greeks Analysis | stock/info | greek-exposure/*, max-pain | GEX levels, pinning |
| Congress Tracking | congress/recent-trades | stock/* | Congressional positioning |
| Short Squeeze | shorts/* | darkpool/*, greek-exposure | Squeeze potential score |
| Earnings Plays | earnings/* | volatility/*, flow-* | Earnings opportunity rank |
| ETF Impact | etfs/*/holdings | stock/* | Rebalancing flow estimates |
| Real-Time | flow-alerts + WebSocket | stock/*, option-contract/* | Live flow monitoring |

---

## Best Practices

1. **Cache aggressively**: Stock info, greeks don't change every second
2. **Batch requests**: Get multiple tickers in sequence with minimal delay
3. **Use WebSocket for real-time**: Don't poll REST endpoints
4. **Handle rate limits**: Implement exponential backoff
5. **Chain efficiently**: Extract all needed IDs in one pass
6. **Error handling**: APIs may return empty data for some tickers

---

## Related Documents

- [ENDPOINT_RELATIONSHIPS.md](./ENDPOINT_RELATIONSHIPS.md) - All relationship mappings
- [QUICK_CHAINS.md](./QUICK_CHAINS.md) - Quick reference endpoint combinations
- [Individual endpoint docs](./docs/) - Detailed endpoint documentation
