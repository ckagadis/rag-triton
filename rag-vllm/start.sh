#!/bin/bash
set -e

# Use YAML config for vLLM
vllm serve --config /app/config.yaml --port 8000
