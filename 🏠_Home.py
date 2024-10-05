import streamlit as st
from src.pipeline import Pipeline
from dotenv import load_dotenv
import os

check = load_dotenv()


st.set_page_config(page_title="🩺 Medical Report Analyzer",page_icon= "*")

st.markdown("<h1 style='text-align: center;'>Medical Report Analyzer 🔎</h1>", unsafe_allow_html=True)
st.caption("Health Insights Based on The Lab Reports")

if not check:
    api_key = st.text_input("API KEY",placeholder='Provide google api key',help="click to get api key : https://ai.google.dev/")
    os.environ['GOOGLE_API_KEY'] = api_key


file = st.file_uploader(label="Upload Lab Report", type=["PDF", "JPG", "PNG", "JPEG"])
if st.button("Process"):
    if file != None:
        file_type = file.name.split(".")[-1]
        response = Pipeline.process(file=file,type = file_type)
        st.write(response)

    else:
        st.warning("Please Upload file.",icon="⚠️")