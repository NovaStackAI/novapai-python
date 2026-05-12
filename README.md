# NovaPAI Python SDK Example

> Use NovaPAI in Python — OpenAI-compatible API in 3 lines of code.

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![API](https://img.shields.io/badge/API-NovaPAI-6C47FF)](https://api.novapai.ai)
[![Python](https://img.shields.io/badge/Python-SDK-brightgreen)](#)

## What is NovaPAI?

[NovaPAI](https://api.novapai.ai) is an **OpenAI-compatible API gateway** that gives you access to top-tier LLMs like **DeepSeek V4 Pro** through the standard OpenAI SDK. If you know how to use the OpenAI API, you already know how to use NovaPAI — just change the `base_url`.

## Quick Start

### 1. Get an API Key

Sign up at [api.novapai.ai](https://api.novapai.ai) to get your free API key.

### 2. Install the SDK

```bash
pip install openai
```

### 3. Run the Example

```bash
git clone https://github.com/NovaStackAI/novapai-python.git
cd novapai-python
export NOVAPAI_API_KEY="your-api-key"
python example.py
```

## Examples Included

This repo contains a single `example.py` with all examples:

| Example | Description |
|---------|------------|
| Basic Chat | Single-turn chat completion |
| Streaming | Real-time token-by-token output |
| Multi-turn Conversation | Context-aware multi-message dialogue |
| List Models | Fetch all available models |

## Core Concept

```python
# Standard OpenAI Python SDK — just change base_url!
from openai import OpenAI

client = OpenAI(
    api_key="your-novapai-key",
    base_url="https://api.novapai.ai/router/v1"  # ← Only this line changes!
)

response = client.chat.completions.create(
    model="deepseek-v4-pro",
    messages=[{"role": "user", "content": "Hello!"}]
)
print(response.choices[0].message.content)
```

**That's it.** The OpenAI SDK you already know works directly with NovaPAI. No new SDK to learn.

## Why NovaPAI?

- **OpenAI-Compatible** — Use any OpenAI SDK in any language
- **Top Models** — Access DeepSeek V4 Pro and more
- **One API Key** — All models, one account
- **No Vendor Lock-in** — Switch models with one line change

## All SDK Examples

- [novapai-python](https://github.com/NovaStackAI/novapai-python)
- [novapai-javascript](https://github.com/NovaStackAI/novapai-javascript)
- [novapai-typescript](https://github.com/NovaStackAI/novapai-typescript)
- [novapai-go](https://github.com/NovaStackAI/novapai-go)
- [novapai-rust](https://github.com/NovaStackAI/novapai-rust)
- [novapai-java](https://github.com/NovaStackAI/novapai-java)
- [novapai-csharp](https://github.com/NovaStackAI/novapai-csharp)
- [novapai-php](https://github.com/NovaStackAI/novapai-php)
- [novapai-ruby](https://github.com/NovaStackAI/novapai-ruby)
- [novapai-curl](https://github.com/NovaStackAI/novapai-curl)

## Links

- [API Documentation](https://api.novapai.ai)
- [NovaStackAI GitHub](https://github.com/NovaStackAI)

---

Made with by [NovaStackAI](https://github.com/NovaStackAI)
