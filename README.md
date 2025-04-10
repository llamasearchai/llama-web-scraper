# llama-web-scraper

[![PyPI version](https://img.shields.io/pypi/v/llama_web_scraper.svg)](https://pypi.org/project/llama_web_scraper/)
[![License](https://img.shields.io/github/license/llamasearchai/llama-web-scraper)](https://github.com/llamasearchai/llama-web-scraper/blob/main/LICENSE)
[![Python Version](https://img.shields.io/pypi/pyversions/llama_web_scraper.svg)](https://pypi.org/project/llama_web_scraper/)
[![CI Status](https://github.com/llamasearchai/llama-web-scraper/actions/workflows/llamasearchai_ci.yml/badge.svg)](https://github.com/llamasearchai/llama-web-scraper/actions/workflows/llamasearchai_ci.yml)

**Llama Web Scraper (llama-web-scraper)** is a toolkit for building intelligent web scrapers within the LlamaSearch AI ecosystem. It combines traditional web scraping techniques with AI models for tasks like content extraction, understanding page structure, and handling dynamic websites.

## Key Features

- **Web Scraping Engine:** Core components for fetching and parsing web pages (`scraper/`).
- **AI-Powered Extraction:** Utilizes AI models for intelligent content extraction, potentially handling complex layouts or JavaScript-rendered pages (`ai/`, `models/`).
- **Command-Line Interface:** Provides CLI tools for initiating and configuring scraping tasks (`cli/`).
- **Utilities:** Includes helper functions for requests, parsing, and data handling (`utils/`).
- **Core Orchestration:** Manages the scraping workflow (`core.py`, `main.py`).
- **Configurable:** Allows defining target URLs, scraping rules, AI models, output formats, etc. (`config.py`).

## Installation

```bash
pip install llama-web-scraper
# Or install directly from GitHub for the latest version:
# pip install git+https://github.com/llamasearchai/llama-web-scraper.git
```

## Usage

### Command-Line Interface (CLI)

*(CLI usage examples for scraping specific URLs or using configuration files will be added here.)*

```bash
llama-web-scraper scrape --url https://example.com/article --output article.json --use-ai
llama-web-scraper run --config scrape_job.yaml
```

### Python Client / Embedding

*(Python usage examples for programmatically controlling the scraper will be added here.)*

```python
# Placeholder for Python client usage
# from llama_web_scraper import Scraper, ScrapeConfig

# config = ScrapeConfig.load("config.yaml")
# scraper = Scraper(config)

# # Scrape a single URL
# results = scraper.scrape_url(
#     "https://blog.example.com/latest-post",
#     extract_elements=['title', 'body', 'author']
# )
# print(results)

# # Run a scraping job defined in config
# # job_results = scraper.run_job("news_sites_job")
```

## Architecture Overview

```mermaid
graph TD
    A[User / CLI (cli)] --> B{Core Scraper Orchestrator (core.py, main.py)};
    B -- Initiates Scrape --> C{Scraping Engine (scraper/)};
    C -- Fetches --> D((Target Website));
    D -- HTML/Content --> C;
    C -- Raw Content --> E{AI Processing Module (ai/, models/)};
    E -- Extracts Data --> C;
    C --> F[Structured Scraped Data];
    F --> B;
    B --> G[Output (File, DB, API)];

    H[Utilities (utils/)] -- Used by --> C;
    H -- Used by --> E;
    I[Configuration (config.py)] -- Configures --> B;
    I -- Configures --> C;
    I -- Configures --> E;

    style B fill:#f9f,stroke:#333,stroke-width:2px
    style E fill:#aef,stroke:#333,stroke-width:1px
```

1.  **Interface:** User initiates scraping via the CLI or programmatically.
2.  **Orchestrator:** Manages the scraping task based on configuration.
3.  **Scraping Engine:** Handles fetching web content (HTML, etc.) from target sites.
4.  **AI Processing:** (Optional) AI models analyze the raw content for intelligent extraction, structure understanding, or rendering JavaScript.
5.  **Data Extraction:** Relevant data is extracted either through rules or AI processing.
6.  **Output:** Structured data is saved to a file, database, or sent to another service.
7.  **Config/Utils:** Configuration defines targets and rules; utilities provide support.

## Configuration

*(Details on configuring target URLs/sites, scraping rules (CSS selectors, XPath), AI model selection, JavaScript rendering options, output formats, rate limits, proxy usage, etc., will be added here.)*

## Development

### Setup

```bash
# Clone the repository
git clone https://github.com/llamasearchai/llama-web-scraper.git
cd llama-web-scraper

# Install in editable mode with development dependencies
pip install -e ".[dev]"
```

### Testing

```bash
pytest tests/
```

### Contributing

Contributions are welcome! Please refer to [CONTRIBUTING.md](CONTRIBUTING.md) and submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
*Developed by lalamasearhc.*
