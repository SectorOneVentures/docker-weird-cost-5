# Docker Weird Cost — Managed Cloud vs. Self-Hosted GPU & Scraper Arbitrage Calculator

👉 **Live Interactive Calculator:** **[https://sectoroneventures.github.io/docker-weird-cost-5/](https://sectoroneventures.github.io/docker-weird-cost-5/)**

Managed cloud APIs for Docker Weird workloads charge 5x to 15x markup at scale, whereas pairing a $0.19/hr Vast.ai GPU worker with Apify ($5 free credit) and ScrapingBee cuts monthly bills by 80%-95%.

---

## Quick Comparison Table

| Stack / Provider | Notes | Direct Link |
| :--- | :--- | :--- |
| **Vast.ai Rented GPU + Open-Source Worker Stack** | Starts at $0.19/hr on RTX 3090 or $0.35/hr on RTX 4090 | **[Launch / Compare →](https://cloud.vast.ai/?ref_id=749467)** |
| **Apify Cloud Actors + Residential Proxy Pool** | Includes $5/mo free platform credit | **[Launch / Compare →](https://apify.com?fpr=infrabench7552)** |
| **ScrapingBee Stealth Browser API** | Includes 1,000 free API calls | **[Launch / Compare →](https://www.scrapingbee.com?fpr=infrabench7552)** |
| **Enterprise Managed Cloud API Tier** | High per-unit usage markup | **[Launch / Compare →](https://cloud.vast.ai/?ref_id=749467)** |

---

## Run From Your Terminal (`cli.py`)

```bash
python3 cli.py --volume 100
```

## Related Developer Cost Calculators
* **[GPU Memory & Hourly Price Calculator](https://sectoroneventures.github.io/infrabench/)**
* **[Headless Browser & Scraping API Benchmark](https://sectoroneventures.github.io/infrabench/headless-scraper-benchmark.html)**
* **[Docker VPS vs. Cloud Scraper TCO Estimator](https://sectoroneventures.github.io/infrabench/docker-vps-tco-estimator.html)**
