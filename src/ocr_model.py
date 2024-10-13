from easyocr import Reader
from src.setting import OCR_MODEL_LANGUAGE
from src import logging

class OCR:
    def __init__(self):
        pass

    def extract_text(image):
        """
        image : image or numpy array.

        This function is for OCR 

        Return : raw text from ocr model
        
        """
        try:
            ocr = Reader(lang_list=[OCR_MODEL_LANGUAGE])
            result = ocr.readtext(image)
            text = [bbox[1] for bbox in result]
            text = "\n".join(text)
            return text
        except Exception as e:
            logging.info(f"Error : {e} : OCR.extract_text")