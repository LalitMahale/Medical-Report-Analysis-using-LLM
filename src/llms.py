import os
import google.generativeai as genai
from .setting import MODEL_NAME
from dotenv import load_dotenv
from .prompts import Prompts
load_dotenv()


class LLM:
    def __init__(self):
        self.API_KEY = os.getenv("GOOGLE_API_KEY")

    def get_json(self,input_data:str,key:str = None):
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
            print(e)

