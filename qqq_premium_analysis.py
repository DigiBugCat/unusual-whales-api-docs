#!/usr/bin/env python3
"""
QQQ Options Premium Analysis Script
Analyzes 1-4 DTE option premiums for strikes ~$5 OTM and tracks weekly changes
"""

import os
import requests
from datetime import datetime, timedelta
from typing import Dict, List, Optional
import json
import time

# API Configuration
BASE_URL = "https://api.unusualwhales.com/api"
API_KEY = os.environ.get("UNUSUAL_WHALES_API_KEY", "")

class QQQOptionsAnalyzer:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.headers = {"Authorization": f"Bearer {api_key}"}
        self.ticker = "QQQ"

    def api_request_with_retry(self, url: str, params: dict = None, max_retries: int = 3) -> Optional[dict]:
        """Make API request with retry logic for rate limiting"""
        for attempt in range(max_retries):
            try:
                if attempt > 0:
                    wait_time = 2 ** attempt  # Exponential backoff
                    print(f"  Retrying in {wait_time}s... (attempt {attempt + 1}/{max_retries})")
                    time.sleep(wait_time)

                response = requests.get(url, headers=self.headers, params=params, timeout=30)
                response.raise_for_status()
                return response.json()

            except requests.exceptions.HTTPError as e:
                if e.response.status_code in [429, 503]:  # Rate limit or service unavailable
                    if attempt < max_retries - 1:
                        continue
                raise
            except requests.exceptions.Timeout:
                if attempt < max_retries - 1:
                    continue
                raise

        return None

    def get_options_chain(self, min_dte: int = 1, max_dte: int = 4) -> tuple[List[Dict], Optional[float]]:
        """Get options chain filtered by DTE and extract current price"""
        try:
            # Use the simpler option-contracts endpoint with minimal parameters
            url = f"{BASE_URL}/stock/{self.ticker}/option-contracts"
            params = {
                'limit': 200  # Smaller limit to reduce load
            }

            print(f"\n📊 Fetching {self.ticker} options contracts...")
            data = self.api_request_with_retry(url, params)

            all_contracts = data.get('data', [])
            print(f"✓ Found {len(all_contracts)} option contracts")

            # Filter by DTE manually by parsing option symbols
            # Option symbol format: TICKER + YYMMDD + C/P + STRIKE (e.g., QQQ251107P00600000)
            from datetime import datetime, timedelta
            today = datetime.now().date()

            # Debug: collect all DTEs to see what's available
            dte_counts = {}
            contracts = []

            for contract in all_contracts:
                symbol = contract.get('option_symbol', '')
                if not symbol or len(symbol) < 15:
                    continue

                try:
                    # Extract date from symbol (YYMMDD format after ticker)
                    # For QQQ (3 chars): positions 3-9 contain YYMMDD
                    ticker_len = len(self.ticker)
                    date_str = symbol[ticker_len:ticker_len+6]
                    option_type = symbol[ticker_len+6]  # C or P

                    # Parse date
                    expiry = datetime.strptime(date_str, '%y%m%d').date()
                    dte = (expiry - today).days

                    # Extract strike (remaining digits / 1000)
                    strike_str = symbol[ticker_len+7:]
                    strike = float(strike_str) / 1000

                    # Add parsed data to contract
                    contract['dte'] = dte
                    contract['expiration_date'] = expiry.strftime('%Y-%m-%d')
                    contract['option_type'] = 'call' if option_type == 'C' else 'put'
                    contract['strike'] = strike

                    # Count DTEs for debugging
                    dte_counts[dte] = dte_counts.get(dte, 0) + 1

                    if min_dte <= dte <= max_dte:
                        contracts.append(contract)
                except Exception as e:
                    # Skip contracts we can't parse
                    continue

            # Show available DTEs
            if dte_counts:
                sorted_dtes = sorted(dte_counts.keys())[:10]  # First 10 DTEs
                print(f"Debug - Available DTEs: {sorted_dtes}")

            print(f"✓ Filtered to {len(contracts)} contracts with {min_dte}-{max_dte} DTE")

            # Estimate current price from ATM strikes
            current_price = None
            if contracts and len(contracts) > 0:
                # Try to find stock_price field first
                for contract in contracts[:10]:  # Check first 10
                    if 'stock_price' in contract:
                        current_price = float(contract['stock_price'])
                        print(f"✓ Current QQQ Price: ${current_price:.2f} (from contract data)")
                        break

                # If not found, estimate from ATM strikes (most volume/OI near current price)
                if not current_price:
                    strikes = [c.get('strike', 0) for c in contracts if c.get('strike')]
                    if strikes:
                        current_price = sum(strikes) / len(strikes)  # Average of strikes as approximation
                        print(f"✓ Estimated QQQ Price: ~${current_price:.2f} (from ATM strikes)")

            return contracts, current_price

        except Exception as e:
            print(f"✗ Error fetching options chain: {e}")
            import traceback
            traceback.print_exc()
            return [], None

    def filter_by_strike_distance(self, contracts: List[Dict], current_price: float,
                                   target_otm: float = 5.0, tolerance: float = 2.0) -> List[Dict]:
        """Filter contracts to those approximately $5 OTM"""
        filtered = []

        # Debug: print first few strikes to see what we're working with
        if contracts:
            print(f"\nDebug - Current price: ${current_price:.2f}")
            print(f"Debug - First 5 contracts:")
            for i, c in enumerate(contracts[:5]):
                strike = c.get('strike', 'missing')
                opt_type = c.get('option_type', 'missing')
                symbol = c.get('option_symbol', 'missing')
                print(f"  {i+1}. {symbol} - Strike: {strike}, Type: {opt_type}")

        for contract in contracts:
            strike_raw = contract.get('strike')
            if strike_raw is None:
                continue

            strike = float(strike_raw)
            option_type = contract.get('option_type', '').lower()

            if option_type == 'call':
                # For calls, OTM means strike > current price
                distance = strike - current_price
            elif option_type == 'put':
                # For puts, OTM means strike < current price
                distance = current_price - strike
            else:
                continue

            # Check if within tolerance of target OTM distance
            if abs(distance - target_otm) <= tolerance:
                contract['otm_distance'] = distance
                filtered.append(contract)

        print(f"✓ Filtered to {len(filtered)} contracts ~${target_otm:.0f} OTM (±${tolerance:.0f})")
        return filtered

    def get_contract_history(self, contract_symbol: str, days: int = 7) -> Optional[List[Dict]]:
        """Get historical data for a specific contract"""
        try:
            url = f"{BASE_URL}/option-contract/{contract_symbol}/historic"
            params = {'limit': days}

            data = self.api_request_with_retry(url, params, max_retries=2)
            if data:
                # Historical data is under 'chains' not 'data'
                return data.get('chains', data.get('data', []))
            return None

        except Exception as e:
            # Don't print error for each contract to avoid spam
            return None

    def analyze_premium_changes(self, contracts: List[Dict]) -> List[Dict]:
        """Analyze premium changes over the past week"""
        results = []

        print(f"\n📈 Analyzing premium changes over last 7 days...")
        print(f"Checking {len(contracts)} contracts for historical data...")
        print("=" * 80)

        successful_fetches = 0
        for i, contract in enumerate(contracts):
            symbol = contract.get('option_symbol', '')
            if not symbol:
                continue

            # Show progress every 5 contracts
            if (i + 1) % 5 == 0:
                print(f"  Progress: {i+1}/{len(contracts)} contracts checked, {successful_fetches} with data...")

            history = self.get_contract_history(symbol, days=10)  # Try 10 days for more data
            if not history or len(history) < 2:
                continue

            successful_fetches += 1

            # Sort by date
            history.sort(key=lambda x: x.get('date', ''))

            # Get most recent and week-ago prices
            current_data = history[-1]
            week_ago_data = history[0]

            # Historical data uses 'last_price' not 'close'
            current_price = float(current_data.get('last_price', current_data.get('avg_price', 0)))
            week_ago_price = float(week_ago_data.get('last_price', week_ago_data.get('avg_price', 0)))

            if week_ago_price == 0:
                continue

            # Calculate changes
            price_change = current_price - week_ago_price
            pct_change = (price_change / week_ago_price) * 100

            results.append({
                'symbol': symbol,
                'option_type': contract.get('option_type', '').upper(),
                'strike': float(contract.get('strike', 0)),
                'expiration': contract.get('expiration_date', ''),
                'dte': contract.get('dte', 0),
                'otm_distance': contract.get('otm_distance', 0),
                'current_premium': current_price,
                'week_ago_premium': week_ago_price,
                'price_change': price_change,
                'pct_change': pct_change,
                'current_volume': contract.get('volume', 0),
                'current_oi': contract.get('open_interest', 0),
                'current_iv': contract.get('implied_volatility', 0),
                'current_date': current_data.get('date', ''),
                'week_ago_date': week_ago_data.get('date', '')
            })

        # Sort by percentage change (descending)
        results.sort(key=lambda x: x['pct_change'], reverse=True)

        return results

    def print_analysis(self, results: List[Dict], current_price: float):
        """Print formatted analysis results"""
        if not results:
            print("\n⚠️  No contracts found with sufficient historical data")
            return

        print(f"\n{'='*80}")
        print(f"QQQ OPTIONS PREMIUM ANALYSIS - ~$5 OTM, 1-4 DTE")
        print(f"Current QQQ Price: ${current_price:.2f}")
        print(f"Analysis Period: {results[0]['week_ago_date']} to {results[0]['current_date']}")
        print(f"Total Contracts Analyzed: {len(results)}")
        print(f"{'='*80}\n")

        # Summary statistics
        avg_change = sum(r['pct_change'] for r in results) / len(results)
        calls = [r for r in results if r['option_type'] == 'CALL']
        puts = [r for r in results if r['option_type'] == 'PUT']

        print("📊 SUMMARY STATISTICS:")
        print(f"  Average Premium Change: {avg_change:+.2f}%")
        print(f"  Calls Analyzed: {len(calls)}")
        print(f"  Puts Analyzed: {len(puts)}")
        if calls:
            print(f"  Avg Call Premium Change: {sum(r['pct_change'] for r in calls)/len(calls):+.2f}%")
        if puts:
            print(f"  Avg Put Premium Change: {sum(r['pct_change'] for r in puts)/len(puts):+.2f}%")

        # Top gainers
        print(f"\n🔥 TOP 10 PREMIUM GAINERS:")
        print(f"{'Symbol':<30} {'Type':<6} {'Strike':<8} {'DTE':<5} {'Week Ago':<10} {'Current':<10} {'Change':<12}")
        print("-" * 95)

        for i, r in enumerate(results[:10], 1):
            print(f"{r['symbol']:<30} {r['option_type']:<6} ${r['strike']:<7.2f} {r['dte']:<5} "
                  f"${r['week_ago_premium']:<9.2f} ${r['current_premium']:<9.2f} "
                  f"{r['price_change']:+.2f} ({r['pct_change']:+.1f}%)")

        # Top losers
        print(f"\n📉 TOP 10 PREMIUM LOSERS:")
        print(f"{'Symbol':<30} {'Type':<6} {'Strike':<8} {'DTE':<5} {'Week Ago':<10} {'Current':<10} {'Change':<12}")
        print("-" * 95)

        for i, r in enumerate(results[-10:], 1):
            print(f"{r['symbol']:<30} {r['option_type']:<6} ${r['strike']:<7.2f} {r['dte']:<5} "
                  f"${r['week_ago_premium']:<9.2f} ${r['current_premium']:<9.2f} "
                  f"{r['price_change']:+.2f} ({r['pct_change']:+.1f}%)")

        # Breakdown by DTE
        print(f"\n📅 BREAKDOWN BY DTE:")
        for dte in range(1, 5):
            dte_contracts = [r for r in results if r['dte'] == dte]
            if dte_contracts:
                avg_dte_change = sum(r['pct_change'] for r in dte_contracts) / len(dte_contracts)
                print(f"  {dte} DTE: {len(dte_contracts)} contracts, Avg Change: {avg_dte_change:+.2f}%")

        # Save to JSON
        output_file = 'qqq_premium_analysis_results.json'
        with open(output_file, 'w') as f:
            json.dump({
                'analysis_date': datetime.now().isoformat(),
                'current_qqq_price': current_price,
                'summary': {
                    'total_contracts': len(results),
                    'avg_premium_change_pct': avg_change,
                    'total_calls': len(calls),
                    'total_puts': len(puts)
                },
                'contracts': results
            }, f, indent=2)

        print(f"\n💾 Full results saved to: {output_file}")
        print(f"{'='*80}\n")

    def run_analysis(self):
        """Run complete analysis"""
        if not self.api_key:
            print("❌ Error: UNUSUAL_WHALES_API_KEY environment variable not set!")
            print("\nPlease set your API key:")
            print("  export UNUSUAL_WHALES_API_KEY='your_api_key_here'")
            return

        print("🐋 QQQ Options Premium Analysis")
        print("=" * 80)

        # Get options chain and current price
        # Using 5-14 DTE to ensure contracts have sufficient historical data
        print("Note: Using 5-14 DTE for better historical data availability")
        contracts, current_price = self.get_options_chain(min_dte=5, max_dte=14)
        if not contracts or not current_price:
            print("⚠️  Unable to fetch options data or current price")
            return

        # Filter by strike distance (~$5 OTM)
        # For QQQ at ~$600, we'll use a wider tolerance to capture more strikes
        filtered_contracts = self.filter_by_strike_distance(
            contracts,
            current_price,
            target_otm=5.0,
            tolerance=5.0  # Wider tolerance to capture strikes from $0-10 OTM
        )

        if not filtered_contracts:
            print("⚠️  No contracts found within $5 OTM range")
            return

        # Analyze premium changes
        results = self.analyze_premium_changes(filtered_contracts)

        # Print results
        self.print_analysis(results, current_price)


def main():
    """Main entry point"""
    analyzer = QQQOptionsAnalyzer(API_KEY)
    analyzer.run_analysis()


if __name__ == "__main__":
    main()
