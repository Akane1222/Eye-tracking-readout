#モジュールのimport
import os
import sys
import pyocr
from PIL import Image

#tesseractの指定
tesseract_path = r"C:\Program Files\Tesseract-OCR"
if tesseract_path not in os.environ["PATH"].split(os.pathsep):
    os.environ["PATH"] += os.pathsep + tesseract_path

#OCRエンジンを取得
tools = pyocr.get_available_tools() 
if len(tools) == 0:
    print("OCRエンジンが指定されていません")
    sys.exit(1)
else:
    tool = tools[0]

#画像の読み込み
img = Image.open(r"\test.png")
img.show()

#文字を読み取り
builder = pyocr.builders.TextBuilder(tesseract_layout=6)
result = tool.image_to_string(img,lang="jpn",builder=builder)

#結果を出力
print(result)