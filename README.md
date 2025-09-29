# ragmaster

**ragmaster** is a modular, containerized Retrieval-Augmented Generation (RAG) pipeline with **multimodal support**, **continual learning**, and **mandatory web search**.  

- Supports ingestion of all common document formats: images (PNG, JPG), PDFs, Word, Excel, PowerPoint, and plain text.  
- Integrates OCR and vision-language models for image-heavy content (e.g., comic pages).  
- Uses [SearxNG](https://github.com/searxng/searxng) for every query to ensure answers are always up to date.  
- Stores all knowledge (documents, web search results, user interactions) in **ChromaDB with persistent volumes**.  
- Runs **vLLM** for efficient GPU-accelerated inference.  
- Modular design: each service runs in its own container and communicates over well-defined APIs.  

---

## 🚀 First-Time Setup

After cloning the repository, run the following script to enable Git hooks:

```bash
./scripts/setup-githooks.sh
```

This ensures the **project tree in this README** is automatically updated on every commit.  

---

## 🐳 Running the Pipeline

Start all services with:

```bash
docker compose up --build
```

This will spin up all components: ingestion, OCR, embeddings, vision models, web search (SearxNG), ChromaDB, vLLM, backend, and the web UI.  

---

## 📂 Project Tree

The following section is automatically updated before each commit:

<!-- PROJECT TREE START -->
```
.
├── docker-compose.yml
├── .githooks
│   └── pre-commit
├── rag-backend
│   └── README.md
├── rag-chromadb
│   └── README.md
├── rag-embedder
│   └── README.md
├── rag-ingestion
│   └── README.md
├── ragmaster
├── rag-ner
│   └── README.md
├── rag-ocr
│   └── README.md
├── rag-vision
│   └── README.md
├── rag-vllm
│   └── README.md
├── rag-websearch
│   └── README.md
├── rag-webui
│   └── README.md
├── README.md
└── scripts
    └── setup-githooks.sh

14 directories, 14 files
```
<!-- PROJECT TREE END -->

---

## 🧩 Components

- **rag-backend** – Orchestration layer (FastAPI).  
- **rag-ingestion** – Document ingestion (PDF, Word, Excel, PowerPoint, text).  
- **rag-ocr** – OCR service for image-based content.  
- **rag-vision** – Vision-language embeddings (e.g., CLIP, BLIP, LLaVA).  
- **rag-embedder** – Text embeddings (OCR output, web content, documents).  
- **rag-ner** – Named entity and relation extraction.  
- **rag-websearch** – SearxNG container (mandatory for every query).  
- **rag-vllm** – vLLM GPU inference server.  
- **rag-webui** – User-facing web interface.  
- **rag-chromadb** – Vector database with persistent storage.  

---

## 🔗 Networking

- All containers are connected to a single custom Docker network: **`rag-master`**.  
- Communication between containers is **only allowed via HTTP APIs**.  
- No container can directly access another’s filesystem or database.  
- This ensures modularity, reproducibility, and makes it easy to swap out components without breaking the rest of the pipeline.  

---

## 🖥️ Hardware Used for Development & Testing

This repository was built and tested on the following hardware configuration:

- **Processor (CPU)**: Intel Core i9-13900KS (24-core, 32-thread, Raptor Lake, up to 6.0 GHz)  
- **Memory (RAM)**: 192GB CORSAIR Vengeance RGB DDR5  
- **Graphics Card (GPU)**: GIGABYTE AORUS GeForce RTX 5090 Master, 32GB GDDR7  
- **Motherboard**: GIGABYTE Z790 AORUS ELITE AX (LGA 1700, Intel Z790 chipset)  
- **Storage**: NVMe SSD (2TB recommended minimum for datasets, embeddings, and model weights) 

> ⚠️ **Note**: Minimum hardware requirements will be specified once the core multimodal and LLM models are finalized. At present, this project has only been tested on the configuration listed above.

> ⚠️ The system is designed for GPU acceleration. While most services will run on CPU-only setups, components such as **rag-vllm** and **rag-vision** require a modern NVIDIA GPU with sufficient VRAM for practical performance.  

### Minimum vs. Tested Hardware

| Component | Minimum | Recommended (tested) |
|-----------|----------|-----------------------|
| CPU       | 8 cores | Intel i9-13900KS (24 cores) |
| RAM       | 32GB | 192GB DDR5 |
| GPU       | NVIDIA RTX 3090 (24GB VRAM) | RTX 5090 (32GB VRAM) |
| Storage   | 500GB SSD | 2TB NVMe SSD |

---

## 📝 Notes

- All containers, images, volumes, and directories use the `rag-` prefix for consistency.  
- Persistent Docker volumes are created for every service that needs long-term storage.  
- Web search results from SearxNG are always **embedded and persisted** in ChromaDB, so the system continually expands its knowledge.  
