from fastapi import FastAPI, UploadFile
import pdfplumber, docx, pandas as pd

app = FastAPI()

@app.post("/ingest/pdf")
async def ingest_pdf(file: UploadFile):
    with pdfplumber.open(file.file) as pdf:
        text = "\n".join([page.extract_text() for page in pdf.pages])
    return {"text": text}
