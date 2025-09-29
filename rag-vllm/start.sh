#!/bin/bash
set -e
vllm serve \
  --model $(jq -r '.model' config.json) \
  --port 8000
