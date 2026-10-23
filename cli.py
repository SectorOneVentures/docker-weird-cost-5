#!/usr/bin/env python3
"""
Docker Weird Cost — Managed Cloud vs. Self-Hosted GPU & Scraper Arbitrage Calculator — Command-Line Cost Calculator
Live Web Calculator: https://sectoroneventures.github.io/docker-weird-cost-5/
"""
import argparse

PROVIDERS = [
  {
    "name": "Vast.ai Rented GPU + Open-Source Worker Stack",
    "cost_per_unit": 0.14,
    "min_monthly": 4.5,
    "speed_note": "Starts at $0.19/hr on RTX 3090 or $0.35/hr on RTX 4090",
    "cta_label": "Launch on Vast.ai \u2192",
    "cta_url": "https://cloud.vast.ai/?ref_id=749467",
    "highlight": true
  },
  {
    "name": "Apify Cloud Actors + Residential Proxy Pool",
    "cost_per_unit": 0.45,
    "min_monthly": 0.0,
    "speed_note": "Includes $5/mo free platform credit",
    "cta_label": "Try Apify Free \u2192",
    "cta_url": "https://apify.com?fpr=infrabench7552",
    "highlight": false
  },
  {
    "name": "ScrapingBee Stealth Browser API",
    "cost_per_unit": 0.58,
    "min_monthly": 0.0,
    "speed_note": "Includes 1,000 free API calls",
    "cta_label": "Try ScrapingBee \u2192",
    "cta_url": "https://www.scrapingbee.com?fpr=infrabench7552",
    "highlight": false
  },
  {
    "name": "Enterprise Managed Cloud API Tier",
    "cost_per_unit": 3.2,
    "min_monthly": 99.0,
    "speed_note": "High per-unit usage markup",
    "cta_label": "Switch & Save 85%+ \u2192",
    "cta_url": "https://cloud.vast.ai/?ref_id=749467",
    "highlight": false
  }
]

def main() -> None:
    parser = argparse.ArgumentParser(description="Interactive monthly cost calculator for Docker Weird workloads comparing managed SaaS/APIs against rented Vast.ai GPUs, Apify, and ScrapingBee.")
    parser.add_argument("--volume", type=float, default=100, help="Monthly Docker Weird Workload Units (in Thousands)")
    args = parser.parse_args()
    print(f"=== {args.volume:g} k units/mo Cost Comparison ===")
    for p in PROVIDERS:
        cost = max(float(p["min_monthly"]), args.volume * float(p["cost_per_unit"]))
        print(f"* {p['name']}: ${cost:,.2f}/mo ({p['speed_note']})")
        print(f"  -> {p['cta_url']}")
    print(f"\nInteractive web calculator: https://sectoroneventures.github.io/docker-weird-cost-5/")

if __name__ == "__main__":
    main()
