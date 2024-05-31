#import streamlit as st
import os
import nest_asyncio
nest_asyncio.apply()

from IPython.display import Markdown, display

from dotenv import load_dotenv
load_dotenv()

#bring in deps
from llama_parse import LlamaParse
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

llamaparse_api_key = os.getenv("LLAMA_CLOUD_API_KEY")
# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

#SET UP PARSEf
parser = LlamaParse(
    api_key=llamaparse_api_key,
    result_type="markdown"
)

file_extractor = {".pdf":parser}
documents = SimpleDirectoryReader(input_files=['data/frogery.pdf'], file_extractor=file_extractor).load_data()

index = VectorStoreIndex.from_documents(documents)

query_engine = index.as_query_engine()

query = "text me down this complete pdf"
response = query_engine.query(query)
display(Markdown(f"<b>{response}<b>"))
