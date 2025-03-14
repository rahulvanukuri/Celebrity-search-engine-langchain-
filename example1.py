#Integrate the openapi key 
import os
from langchain.llms import OpenAI
from constants import openai_key
from langchain import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain

import streamlit as st 
os.environ['OPENAI_API_KEY']=openai_key
#streamlit title
st.title("Celebrity search engine")
input_text=st.text_input("Search the topic you want")
#Prompt template
first_input=PromptTemplate(
    input_variables=['name'],
    template="Tell me about celebrity{name}"

)

##OPEN AI LLMS
llm=OpenAI(temperature=0.8)
chain=LLMChain(llm=llm,prompt=first_input,verbose=True,output_key='person')
#Prompt template
second_input=PromptTemplate(
    input_variables=['person'],
    template="when was {person} born"

)
chain2=LLMChain(llm=llm,prompt=second_input,verbose=True,output_key='dob')

third_input=PromptTemplate(
    input_variables=['dob'],
    template="Mention higlights of his challenges or top 5 events of why his famous:{dob}"

)
chain3=LLMChain(llm=llm,prompt=third_input,verbose=True,output_key='describe')
parentchain=SequentialChain(chains=[chain,chain2,chain3],input_variables=['name'],output_variables=['person','dob','describe'],verbose=True)
if input_text:
    st.write(parentchain({'name':input_text}))