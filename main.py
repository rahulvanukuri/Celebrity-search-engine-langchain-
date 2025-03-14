#Integrate the openapi key 
import os
from langchain.llms import OpenAI
from constants import openai_key

import streamlit as st 
os.environ['OPENAI_API_KEY']=openai_key
#streamlit title
st.title("Langchain demo with openapi")
input_text=st.text_input("Search the topic you want")

##OPEN AI LLMS
OpenAI(temperature=0.8)
if input_text:
    st.write(llm(input_text))
