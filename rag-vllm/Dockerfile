# Base image with CUDA 12.1 + cuDNN
FROM nvidia/cuda:12.1.1-cudnn8-runtime-ubuntu22.04

# Avoid interactive prompts during install
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    git \
    wget \
    curl \
    ca-certificates \
    python3 \
    python3-dev \
    python3-pip \
    python3-venv \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN python3 -m pip install --upgrade pip

# Install PyTorch with CUDA support (adjust for your GPU/CUDA version)
RUN pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121

# Install vLLM and dependencies
RUN pip install vllm transformers accelerate safetensors

# Optional: install FlashAttention (if not included via vLLM)
RUN pip install flash-attention

# Set working directory
WORKDIR /app

# Copy the configuration file into the container
COPY config.yaml /app/config.yaml

# Copy your start script or entrypoint (if any)
COPY start.sh /app/start.sh
RUN chmod +x /app/start.sh

# Default command to start the API
CMD ["/app/start.sh"]
