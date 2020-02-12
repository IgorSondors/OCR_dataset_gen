# -*- coding: utf-8 -*-
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

# If you don't have tesseract executable in your PATH, include the following:
pytesseract.pytesseract.tesseract_cmd = r'C:\\Users\\sondors\\AppData\\Local\\Tesseract-OCR\\tesseract'


# French text image to string
print(pytesseract.image_to_string(Image.open('9.jpg'), lang='rus'))

with open('text.txt', 'w', encoding="utf8") as f:
    f.write(str(pytesseract.image_to_string(Image.open('9.jpg'), lang='rus')))