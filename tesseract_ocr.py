import pytesseract
from pdf2image import convert_from_path
from PIL import Image
import os

# Set Tesseract path if on Windows
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"  # adjust this!

# Path to your PDF
pdf_path = "F:/Projects folder/RAG-LLM/DATA/HSC26-Bangla1st-Paper.pdf"

# Convert PDF pages to images
pages = convert_from_path(pdf_path, dpi=300)

# Process each page
for i, page in enumerate(pages):
    image_path = f"page_{i+1}.png"
    page.save(image_path, "PNG")

    # OCR using Bengali language
    text = pytesseract.image_to_string(Image.open(image_path), lang="ben")
    
    # Save extracted text
    with open(f"page_{i+1}_ocr.txt", "w", encoding="utf-8") as f:
        f.write(text)

    print(f"✅ OCR complete for page {i+1}")
