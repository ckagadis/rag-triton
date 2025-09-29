from fastapi import FastAPI, UploadFile
import pytesseract
from PIL import Image

app = FastAPI()

@app.post("/ocr")
async def ocr_image(file: UploadFile):
    image = Image.open(file.file)
    text = pytesseract.image_to_string(image)
    return {"text": text}
