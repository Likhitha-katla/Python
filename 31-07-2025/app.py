import os
from dotenv import load_dotenv

from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

os.environ["Langchain_API_KEY"] = os.getenv("Langchain_API_KEY")
os.environ["Langchain_Tracking_v2"] = "true"
os.environ["Langchain_Project"] = os.getenv("Langchain_Project") 

prompt = ChatPromptTemplate.from_messages(
    [
        ("system","you are an helping assistenet in healt care, please respond to the questions asked"),
        ("user","question:{question}")
    ]
)

st.title("Health care assistant")
input_text = st.text_input("what question you have in your mind")

llm = Ollama(model = "llama3")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))