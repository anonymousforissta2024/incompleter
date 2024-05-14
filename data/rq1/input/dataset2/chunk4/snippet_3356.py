#Source: https://stackoverflow.com/questions/75440754/typeerror-expected-str-bytes-or-os-pathlike-object-not-nonetype-after-using
from gpt_index import GPTListIndex, readers, GPTSimpleVectorIndex, LLMPredictor, PromptHelper, download_loader
from langchain import OpenAI
import logging
import sys
import os
import streamlit as st

os.environ['OPENAI_API_KEY'] = "I am deleting my api key from this post"



fileup = st.file_uploader(label=" ")


SimpleDirectoryReader = download_loader("SimpleDirectoryReader")
loader = SimpleDirectoryReader(fileup)
documents = loader.load_data()
index = GPTSimpleVectorIndex(documents)
index.save_to_disk('index.json')
question = st.text_input("What do you want me to do with the file uploaded?")
response = index.query(question)
st.write(response)