""" Script to built a chatbot powered by openAI GPT """
import os
from dotenv import load_dotenv
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv("/Users/karthicksundar/Documents/learnings/Projects/LangChain-Chatbot/.env")


## Langsmith tracking
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

## Prompt message for the LLM model to set the context
prompt = ChatPromptTemplate.from_messages(
            [
                ('system','You are very helpful assisstant. Please respond to all the questions asked by the user'),
                ('user', 'Question:{question}')
            ]
)

## streamlit framework
st.title('Chatbot powered by OPENAI API')
input_text=st.text_input("Search the topic u want")


## openAI LLM
llm = ChatOpenAI(model="gpt-3.5-turbo", api_key=os.getenv("OPENAI_API_KEY_"))
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))