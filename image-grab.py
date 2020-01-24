import numpy as np
from PIL import ImageGrab
import cv2
import pytesseract
from PIL import Image


pytesseract.pytesseract.tesseract_cmd = 'Tesseract-OCR\\tesseract.exe'

def screen_grab():
	while True:
	    #printscreen =  np.array(ImageGrab.grab(bbox=(0,40,800,640)))
	    printscreen = np.array(ImageGrab.grab())
	    cv2.imshow('window', printscreen)
	    cv2.waitKey(0)

def read_text():
	#printscreen = np.array(ImageGrab.grab())
	printscreen =  np.array(ImageGrab.grab(bbox=(0,40,800,640)))
	#text = pytesseract.image_to_string(Image.open('tets3.png'))
	text = pytesseract.image_to_string(printscreen);
	cv2.imshow('window', printscreen)
	print(text)
	cv2.waitKey(0)
	

read_text()
