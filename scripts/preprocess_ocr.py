import cv2
import pytesseract
from PIL import Image
import numpy as np
from transformers import CLIPTokenizer

# Load image
image_path = "comic_page.jpg"
image = cv2.imread(image_path)
image_resized = cv2.resize(image, (224, 224))
image_array = np.transpose(image_resized, (2, 0, 1)).astype(np.float32) / 255.0  # Normalize for CLIP

# Extract text
text = pytesseract.image_to_string(Image.open(image_path), config='--psm 6')  # Better for comics
tokenizer = CLIPTokenizer.from_pretrained("openai/clip-vit-base-patch32")
text_array = tokenizer([text], return_tensors="np", padding=True, truncation=True)["input_ids"]

# Save for Triton
np.save("image_input.npy", image_array)
np.save("text_input.npy", text_array)
print("OCR Text:", text)