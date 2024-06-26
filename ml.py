"""
The AI model that will take an image as an input and give a str type output of the text on the image
"""


import pytesseract
import numpy as np 
from PIL import Image

# Specify the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'


def extract_text(image_path) -> str:
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    # Remove symbols and split by lines for better display
    characters_to_remove = "!()@—*“>+-/,'|£#%$&^_~"
    text = ''.join(char for char in text if char not in characters_to_remove)
    text_lines = text.split("\n")
    return text_lines

# Example usage
# image_path = 'my_code/flask-app/sample_data/img.png'
# extracted_text = extract_text(image_path)
# print("Extracted Text:", extracted_text)




