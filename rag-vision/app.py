from fastapi import FastAPI, UploadFile
from PIL import Image
import torch
from transformers import CLIPProcessor, CLIPModel

app = FastAPI()

model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

@app.post("/embed/image")
async def embed_image(file: UploadFile):
    image = Image.open(file.file)
    inputs = processor(images=image, return_tensors="pt")
    with torch.no_grad():
        embeddings = model.get_image_features(**inputs)
    return {"embedding": embeddings[0].tolist()}
