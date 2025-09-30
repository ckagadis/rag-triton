#!/bin/bash
set -e
vllm serve --config /app/config.json --port 8000
