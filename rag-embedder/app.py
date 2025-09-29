from fastapi import FastAPI
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer

app = FastAPI()
model = SentenceTransformer("all-MiniLM-L6-v2")

class TextIn(BaseModel):
    text: str

@app.post("/embed/text")
async def embed_text(payload: TextIn):
    embedding = model.encode(payload.text).tolist()
    return {"embedding": embedding}
