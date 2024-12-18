import fitz
from PIL import Image
from src.setting import LOCAL_TEST
import numpy as np
from src import logging


class PDF_Processing:
    def __init__(self):
        pass

    def pdf_to_image(file):
        """
        This function will take pdf file and convert first page into image and return it.

        LOCAL_TEST : True / False
        
        """

        try:
            if LOCAL_TEST:
                pdf_file = fitz.open(filename=file,filetype="pdf")
            else:
                pdf_file = fitz.open(stream=file.read(), filetype="pdf")

            page = pdf_file.load_page(0)
            pix = page.get_pixmap(matrix=fitz.Matrix(300/72, 300/72))  # 300 DPI
            image_bytes = pix.samples
            image = Image.frombytes("RGB", [pix.width, pix.height], image_bytes)
            image_np = np.array(image)

            return image_np
        except Exception as e:
            logging.info(f"Error {e} : pdf_to_image")

    def load_image(file):
        """
        This function take image and return numpy array
        """
        try:
            image = Image.open(file)
            image_np = np.array(image)
            return image_np
        except Exception as e:
            logging.info(f"Error {e} : load_image")
