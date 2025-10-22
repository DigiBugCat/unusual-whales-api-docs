#!/usr/bin/env python3
"""
API Testing Script for Unusual Whales Endpoints
Tests all 20 assigned endpoints and generates documentation
"""

import requests
import json
from datetime import datetime
import sys
from typing import Dict, Optional, Any

# Configuration
BASE_URL = "https://api.unusualwhales.com"
API_KEY = "5d1ec006-49f0-4a2a-90ae-5176c72425e3"

headers = {
    "Authorization": f"Bearer {API_KEY}"
}

# Test data for endpoints
test_configs = {
    "/api/market/correlations": {
        "params": {"tickers": "AAPL,MSFT", "interval": "1m"},
        "method": "GET"
    },
    "/api/market/economic-calendar": {
        "params": {},
        "method": "GET"
    },
    "/api/market/fda-calendar": {
        "params": {"limit": 10},
        "method": "GET"
    },
    "/api/market/insider-buy-sells": {
        "params": {"limit": 10},
        "method": "GET"
    },
    "/api/market/market-tide": {
        "params": {},
        "method": "GET"
    },
    "/api/market/oi-change": {
        "params": {"limit": 10},
        "method": "GET"
    },
    "/api/market/sector-etfs": {
        "params": {},
        "method": "GET"
    },
    "/api/market/spike": {
        "params": {},
        "method": "GET"
    },
    "/api/market/top-net-impact": {
        "params": {"limit": 10},
        "method": "GET"
    },
    "/api/market/total-options-volume": {
        "params": {"limit": 1},
        "method": "GET"
    },
    "/api/market/Technology/sector-tide": {
        "params": {},
        "method": "GET"
    },
    "/api/market/SPY/etf-tide": {
        "params": {},
        "method": "GET"
    },
    "/api/net-flow/expiry": {
        "params": {},
        "method": "GET"
    },
    "/api/news/headlines": {
        "params": {"limit": 10},
        "method": "GET"
    },
    "/api/option-contract/AAPL241220C00230000/flow": {
        "params": {"limit": 10},
        "method": "GET"
    },
    "/api/option-contract/AAPL241220C00230000/historic": {
        "params": {"limit": 5},
        "method": "GET"
    },
    "/api/option-contract/AAPL241220C00230000/intraday": {
        "params": {},
        "method": "GET"
    },
    "/api/option-contract/AAPL241220C00230000/volume-profile": {
        "params": {},
        "method": "GET"
    },
    "/api/option-trades/flow-alerts": {
        "params": {"limit": 10},
        "method": "GET"
    },
    "/api/option-trades/full-tape/2025-10-21": {
        "params": {},
        "method": "GET"
    }
}

def test_endpoint(endpoint: str, config: Dict) -> Dict[str, Any]:
    """Test a single endpoint and return the result"""
    try:
        url = f"{BASE_URL}{endpoint}"
        response = requests.get(
            url,
            headers=headers,
            params=config["params"],
            timeout=15
        )

        return {
            "endpoint": endpoint,
            "status_code": response.status_code,
            "success": response.status_code < 400,
            "response_sample": response.json() if response.headers.get("content-type") == "application/json" else None,
            "error": None,
            "response_headers": dict(response.headers),
            "response_time": response.elapsed.total_seconds()
        }
    except requests.exceptions.Timeout:
        return {
            "endpoint": endpoint,
            "status_code": None,
            "success": False,
            "response_sample": None,
            "error": "Request timeout",
            "response_headers": {},
            "response_time": None
        }
    except requests.exceptions.RequestException as e:
        return {
            "endpoint": endpoint,
            "status_code": None,
            "success": False,
            "response_sample": None,
            "error": str(e),
            "response_headers": {},
            "response_time": None
        }
    except Exception as e:
        return {
            "endpoint": endpoint,
            "status_code": None,
            "success": False,
            "response_sample": None,
            "error": f"Unexpected error: {str(e)}",
            "response_headers": {},
            "response_time": None
        }

def main():
    """Run all tests"""
    print("Starting API endpoint tests...")
    print(f"Base URL: {BASE_URL}")
    print(f"Timestamp: {datetime.now().isoformat()}")
    print("=" * 80)

    results = []
    for endpoint, config in test_configs.items():
        print(f"Testing: {endpoint}...", end=" ")
        result = test_endpoint(endpoint, config)
        results.append(result)

        if result["success"]:
            print(f"OK ({result['status_code']}) - {result['response_time']:.2f}s")
        else:
            print(f"FAIL ({result['status_code'] or 'Error'}) - {result['error']}")

    # Save results
    with open("/Users/andrew.sulistio/dev/cassandra/unusual-whales-documentation/test_results.json", "w") as f:
        json.dump(results, f, indent=2, default=str)

    # Summary
    successful = sum(1 for r in results if r["success"])
    print("=" * 80)
    print(f"Results: {successful}/{len(results)} endpoints working")

    return results

if __name__ == "__main__":
    results = main()
