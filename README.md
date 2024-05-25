# llama-web-scraper

A robust and versatile web scraping and analysis system powered by cutting-edge Language Models (LLMs) and advanced scraping techniques.

## Installation

```bash
pip install -e .
```

## Usage

```python
from llama_web_scraper import LlamaWebScraperClient

# Initialize the client
client = LlamaWebScraperClient(api_key="your-api-key")
result = client.query("your query")
print(result)
```

## Features

- Fast and efficient
- Easy to use API
- Comprehensive documentation

## Development

### Setup

```bash
# Clone the repository
git clone https://github.com/nikjois/llama-web-scraper.git
cd llama-web-scraper

# Install development dependencies
pip install -e ".[dev]"
```

### Testing

```bash
pytest
```

## License

MIT

## Author

Nik Jois (nikjois@llamasearch.ai)
