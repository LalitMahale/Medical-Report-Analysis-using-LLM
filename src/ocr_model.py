from easyocr import Reader
from .setting import OCR_MODEL_LANGUAGE

class OCR:
    def __init__(self):
        pass

    def extract_text(image):
        try:
            ocr = Reader(lang_list=[OCR_MODEL_LANGUAGE])
            result = ocr.readtext(image)
            text = [bbox[1] for bbox in result]
            text = "\n".join(text)
            return text
        except Exception as e:
            print(e)
