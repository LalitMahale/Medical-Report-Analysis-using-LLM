from src.document import PDF_Processing
from src.ocr_model import OCR
from src.llms import LLM
from src import logging
import os


class Pipeline:
    def __init__(self):
        self.cwd = os.getcwd()

    def process(file,type):
        """
        file : data it can be image or pdf
        Type : format of PDF / Image (png, jpg)
        
        return : Clean Text.
        """
        try:
            print("startd")
            if type == "pdf":
                image = PDF_Processing.pdf_to_image(file)
            else:
                image = PDF_Processing.load_image(file)
            text = OCR.extract_text(image)
            json_text = LLM().get_json(input_data=text,key = "json")
            final = LLM().get_json(input_data=json_text)
            return final
        except Exception as e:
            logging.info(f"Error :{e} :Pipeline.process")

if __name__ == "__main__":
    path = "test_docs/CBC-test-report-format-example-sample-template-Drlogy-lab-report.pdf"
    result = Pipeline.process(path)