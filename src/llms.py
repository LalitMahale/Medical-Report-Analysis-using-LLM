import os
import google.generativeai as genai
from src.setting import MODEL_NAME
from dotenv import load_dotenv
from src.prompts import Prompts
from src import logging
load_dotenv()


class LLM:
    def __init__(self):
        self.API_KEY = os.getenv("GOOGLE_API_KEY")

    def get_json(self,input_data:str,key:str = None):
        """
        Input_data : It is a string input. It can take json as well as raw text

        key : Default None.
            It can Json and None. If the input_data is json than key will json else None
        
        """
        if key == "json":
            prompts = Prompts.text_json_prompt().format(text = input_data)
        else:
            prompts = Prompts.final_prompt().format(json_data = input_data)

        try:
            genai.configure(api_key = self.API_KEY)
            model = genai.GenerativeModel(model_name=MODEL_NAME)
            response = model.generate_content(prompts)
            return response.text
        except Exception as e:
            logging.info(f"Error :{e}  : LLM.get_json")
