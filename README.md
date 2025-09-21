# Local LLM Text Classification

This project implements a text classification system powered by Large Language Models (LLMs) running locally. The goal is to leverage the capabilities of modern LLMs to automatically categorize and label text data without relying on external APIs or manual human labeling, ensuring privacy, autonomy, and efficiency in text processing tasks.

- Inference engine: [Ollama](https://ollama.com/)
- Target models:
  - gpt-oss:20b
  - llama3.1:8b

## Why Local LLMs for Classification?

- Privacy by default: data never leaves your machine.
- No external API costs or rate limits.
- Flexible prompting: zero-shot, few-shot, or chain-of-thought (with care).
- Rapid iteration: tweak prompts/labels and re-run instantly.

## Prerequisites

- macOS, Linux, or Windows machine with sufficient RAM/VRAM.
- Ollama installed and running:
  - macOS: `brew install ollama && ollama serve`
  - Linux: `curl -fsSL https://ollama.com/install.sh | sh`
  - Windows: see https://ollama.com/download
  - [Ollama documentation](https://ollama.readthedocs.io/en/api/#request-raw-mode)
- Pull the required models:
  ```bash
  ollama pull gpt-oss:20b
  ollama pull llama3.1:8b
  ```

## Model Selection

- gpt-oss:20b
  - Pros: Higher instruction-following quality, better few-shot adherence.
  - Cons: Heavier, uses more VRAM/RAM, slower on CPU-only.
  - Use when: label space is nuanced or you need stronger reasoning.

- llama3.1:8b
  - Pros: Fast, lightweight, good baseline quality, great for batch throughput.
  - Cons: Can occasionally deviate from strict formatting.
  - Use when: you need speed or are running on limited hardware.

## License

This project is licensed under the GNU General Public License v3.0.
