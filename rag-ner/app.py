from fastapi import FastAPI
from pydantic import BaseModel
import spacy

app = FastAPI()
nlp = spacy.load("en_core_web_sm")

class TextIn(BaseModel):
    text: str

@app.post("/ner")
async def extract_entities(payload: TextIn):
    doc = nlp(payload.text)
    entities = [{"text": ent.text, "label": ent.label_} for ent in doc.ents]
    return {"entities": entities}
