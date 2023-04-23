#モジュールのimport
import os
import sys
import pyocr
from PIL import Image

#tesseractの指定
tesseract_path = r"C:\Program Files\Tesseract-OCR"
if tesseract_path not in os.environ["PATH"].split(os.pathsep):
    os.environ["PATH"] += os.pathsep + tesseract_path