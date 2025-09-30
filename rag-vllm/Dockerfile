# Use NVIDIA PyTorch base with CUDA + cuDNN
FROM nvcr.io/nvidia/pytorch:23.10-py3

WORKDIR /app

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Install extra utilities
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    curl \
    ca-certificates \
 && rm -rf /var/lib/apt/lists/*

# Install Python deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

RUN chmod +x start.sh

EXPOSE 8000
CMD ["./start.sh"]
