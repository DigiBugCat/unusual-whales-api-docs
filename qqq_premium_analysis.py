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

# API Configuration
BASE_URL = "https://api.unusualwhales.com/api"
API_KEY = os.environ.get("UNUSUAL_WHALES_API_KEY", "")

class QQQOptionsAnalyzer:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.headers = {"Authorization": f"Bearer {api_key}"}
        self.ticker = "QQQ"

    def get_current_price(self) -> Optional[float]:
        """Get current QQQ stock price"""
        try:
            url = f"{BASE_URL}/stock/{self.ticker}/info"
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            data = response.json()
            price = data.get('data', {}).get('last_price')
            if not price:
                # Fallback to other price fields
                price = data.get('data', {}).get('close', data.get('data', {}).get('price'))
            print(f"✓ Current QQQ Price: ${price:.2f}")
            return float(price)
        except Exception as e:
            print(f"✗ Error fetching QQQ price: {e}")
            return None

    def get_options_chain(self, min_dte: int = 1, max_dte: int = 4) -> List[Dict]:
        """Get options chain filtered by DTE"""
        try:
            url = f"{BASE_URL}/screener/option-contracts"
            params = {
                'ticker_symbol': self.ticker,
                'min_dte': min_dte,
                'max_dte': max_dte,
                'is_otm': 'true',
                'min_volume': 10,  # Filter out low volume options
                'limit': 500
            }

            print(f"\n📊 Fetching options with {min_dte}-{max_dte} DTE...")
            response = requests.get(url, headers=self.headers, params=params)
            response.raise_for_status()
            data = response.json()

            contracts = data.get('data', [])
            print(f"✓ Found {len(contracts)} OTM contracts")
            return contracts

        except Exception as e:
            print(f"✗ Error fetching options chain: {e}")
            return []

    def filter_by_strike_distance(self, contracts: List[Dict], current_price: float,
                                   target_otm: float = 5.0, tolerance: float = 2.0) -> List[Dict]:
        """Filter contracts to those approximately $5 OTM"""
        filtered = []

        for contract in contracts:
            strike = float(contract.get('strike', 0))
            option_type = contract.get('option_type', '').lower()

            if option_type == 'call':
                # For calls, OTM means strike > current price
                distance = strike - current_price
            else:  # put
                # For puts, OTM means strike < current price
                distance = current_price - strike

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

            response = requests.get(url, headers=self.headers, params=params)
            response.raise_for_status()
            data = response.json()

            return data.get('data', [])

        except Exception as e:
            # Don't print error for each contract to avoid spam
            return None

    def analyze_premium_changes(self, contracts: List[Dict]) -> List[Dict]:
        """Analyze premium changes over the past week"""
        results = []

        print(f"\n📈 Analyzing premium changes over last 7 days...")
        print("=" * 80)

        for contract in contracts:
            symbol = contract.get('option_symbol', '')
            if not symbol:
                continue

            history = self.get_contract_history(symbol, days=7)
            if not history or len(history) < 2:
                continue

            # Sort by date
            history.sort(key=lambda x: x.get('date', ''))

            # Get most recent and week-ago prices
            current_data = history[-1]
            week_ago_data = history[0]

            current_price = float(current_data.get('close', 0))
            week_ago_price = float(week_ago_data.get('close', 0))

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

        # Get current price
        current_price = self.get_current_price()
        if not current_price:
            return

        # Get options chain
        contracts = self.get_options_chain(min_dte=1, max_dte=4)
        if not contracts:
            return

        # Filter by strike distance (~$5 OTM)
        filtered_contracts = self.filter_by_strike_distance(
            contracts,
            current_price,
            target_otm=5.0,
            tolerance=2.0
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
