Project Tree


<!-- PROJECT TREE START -->
```text
.
├── docker-compose.yml
├── .githooks
│   └── pre-commit
├── models
│   ├── clip
│   │   └── 1
│   │       └── config.pbtxt
│   └── resnet50
│       ├── 1
│       │   ├── model.onnx
│       │   └── model.onnxclear
│       └── config.pbtxt
├── README.md
└── scripts
    └── setup-githooks.sh

8 directories, 8 files
```
<!-- PROJECT TREE END -->

# Triton Inference Server with ResNet50 (ONNX)

This project demonstrates how to run NVIDIA Triton Inference Server in Docker with a sample ResNet50 ONNX model.

## 📦 Requirements

- NVIDIA GPU + drivers
- Docker and Docker Compose
- NVIDIA Container Toolkit (for GPU passthrough to Docker)

Verify GPU is visible to Docker:

```bash
docker run --rm --gpus all nvidia/cuda:12.2.0-base nvidia-smi
```

## ⚙️ Setup

1. Clone this repository (or create a working directory):

```bash
mkdir -p ~/Docker/triton && cd ~/Docker/triton
```

2. Create the model repository structure:

```bash
mkdir -p models/resnet50/1
```

3. Download the ResNet50 ONNX model:

```bash
wget https://media.githubusercontent.com/media/onnx/models/main/vision/classification/resnet/model/resnet50-v1-7.onnx -O models/resnet50/1/model.onnx
```

4. Create a `config.pbtxt` for the model (`models/resnet50/config.pbtxt`):

```text
name: "resnet50"
platform: "onnxruntime_onnx"
max_batch_size: 8
input [
  {
    name: "data"
    data_type: TYPE_FP32
    dims: [ 3, 224, 224 ]
  }
]
output [
  {
    name: "resnetv17_dense0_fwd"
    data_type: TYPE_FP32
    dims: [ 1000 ]
  }
]
```

5. Create a `docker-compose.yml` to run Triton:

```yaml
services:
  triton_server:
    image: nvcr.io/nvidia/tritonserver:23.12-py3
    runtime: nvidia
    environment:
      - NVIDIA_VISIBLE_DEVICES=all
    volumes:
      - ./models:/models
    ports:
      - "8000:8000"
      - "8001:8001"
      - "8002:8002"
    command: ["tritonserver", "--model-repository=/models"]
```

## 🚀 Run Triton

```bash
docker compose up -d
```

## ✅ Test the Model

You can query the server using `curl` or `tritonclient`:

```bash
pip install nvidia-pip nvidia-pip-tritonclient[all]
```

Example using Python client:

```python
import tritonclient.http as httpclient
import numpy as np

client = httpclient.InferenceServerClient(url="localhost:8000")
input_data = np.random.randn(1,3,224,224).astype(np.float32)
inputs = [httpclient.InferInput("data", input_data.shape, "FP32")]
inputs[0].set_data_from_numpy(input_data)
results = client.infer("resnet50", inputs)
output_data = results.as_numpy("resnetv17_dense0_fwd")
print(output_data)
```
