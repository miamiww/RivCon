import io
import requests
import pytesseract
from PIL import Image
response = requests.get("https://image.slidesharecdn.com/forslideshare-160301153508/95/can-we-assess-creativity-1-1024.jpg?cb=1456850231")
img = Image.open(io.BytesIO(response.content))
text = pytesseract.image_to_string(img)
print(text)


def text_read(slide_location):
    response = requests.get(slide_location)
    img = Image.open(io.BytesIO(response.content))
    text = pytesseract.image_to_string(img)
    return(text)
