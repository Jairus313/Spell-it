from PIL import Image
import pytesseract
from gtts import gTTS 
import os 

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
img = Image.open('image.jpg')

text = pytesseract.image_to_string(img)
print (text)
  
mytext = text
  
language = 'en'
  
myobj = gTTS(text=mytext, lang=language, slow=False) 
  
myobj.save("text.mp3") 
  
