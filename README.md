# Eye-tracking-readout
アイトラッキングによる文字の選択を行い認識された文字の読み上げを行う

## 必要モジュール

PyOCR
```
pip install PyOCR == 0.8.3
pip install Wave==0.0.2
pip install Pillow==9.5.0
pip install pyopenjtalk==0.1.3
pip install scipy==1.10.1
pip install numpy==1.24.3
```

tesseract(外部ソフトなのでインストールが必要)
> https://github.com/UB-Mannheim/tesseract/wiki

Google OCR(使用検討中)
> https://cloud.google.com/vision/docs/ocr?hl=ja

Google text-to-speech(仕様検討)
> https://cloud.google.com/text-to-speech?hl=ja

順次追加

## 使用手順

文字認識

PyOCRとtesseractの導入(上を参照)  
↓  
main.pyをダウンロード  
↓  
認識したい画像を自分のコンピュータ内に置きパスを取得  
↓  
パスを31行目にパスを入力  
↓  
Python3.9にて実行  