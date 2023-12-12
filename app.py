import streamlit as st
from pathlib import Path
from tempfile import NamedTemporaryFile
import time
import shutil
import os
from langchain.document_loaders import PDFPlumberLoader
from langchain.text_splitter import CharacterTextSplitter, TokenTextSplitter
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain import HuggingFacePipeline
from langchain.embeddings import HuggingFaceInstructEmbeddings, HuggingFaceEmbeddings
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.llms import OpenAI
import torch
# from sentence_transformers import SentenceTransformer, util
from chromadb.utils import embedding_functions
import tempfile
from web_extract import *

device = "cuda" if torch.cuda.is_available() else "cpu"
st.set_page_config(
    page_title="Hello, I'm Medoc Chatbot",
    page_icon='🔖',
    layout='wide',
    initial_sidebar_state='auto',
)
from PIL import Image
logo = Image.open("C:\\Users\\saura\\OneDrive\\Desktop\\Medoc\\medoc.jpg")

st.image(logo, width=100)  # Adjust the width to suit your needs

st.title("Hello, I'm Medoc Chatbot")
os.environ['OPENAI_API_KEY'] = "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"

# Mode selection
mode = st.radio("Select Mode:", ('Developer Mode', 'User Mode'))
if mode == 'Developer Mode':
    st.session_state['mode'] = 'developer'
elif mode == 'User Mode':
    query = ''
    st.session_state['mode'] = 'user'
    if 'queries_and_responsesuser' not in st.session_state:
        st.session_state.queries_and_responsesuser = []

if 'mode' not in st.session_state:
    st.session_state['mode'] = 'developer'  # Default mode

if st.session_state['mode'] == 'developer':
    uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")
    uploaded_url = st.text_input("Enter a URL")
    if uploaded_url == '':
        uploaded_url = None
    if 'vectordb' not in st.session_state:
        documents1= []
        documents2= []
        if uploaded_url is not None:
            documents1 = web_extract(uploaded_url)
            documents = documents1 + documents2

        if uploaded_file is not None:
            with NamedTemporaryFile(delete=False, suffix='.pdf') as tmp:
                shutil.copyfileobj(uploaded_file, tmp)
                tmp_path = tmp.name  # Convert Path object to string
                # PDF Processing
                loader = PDFPlumberLoader(tmp_path)
                documents2 = loader.load()
                documents = documents1 + documents2
        
        if uploaded_file is not None or uploaded_url is not None:
            # Text Splitting
            text_splitter = CharacterTextSplitter(chunk_size=100, chunk_overlap=0)
            texts = text_splitter.split_documents(documents)

            # Embeddings and Vector DB
            embedding = OpenAIEmbeddings()
            
            # Embeddings and Vector DB - only done once
            embedding = OpenAIEmbeddings()
            st.session_state.vectordb = Chroma.from_documents(documents=texts, embedding=embedding, persist_directory=None)
            st.session_state.retriever = st.session_state.vectordb.as_retriever(search_kwargs={"k":3})

    if 'queries_and_responses' not in st.session_state:
                st.session_state.queries_and_responses = []

    if 'retriever' in st.session_state:
        # QA System
        qa = RetrievalQA.from_chain_type(llm=OpenAI(), chain_type="stuff", retriever=st.session_state.retriever)

        # Query Input
        query = st.text_input("Enter your Symptoms here", key="new_query")

        if query:
            response = qa({"query": query}, return_only_outputs=False)
            answer = response['result']
            st.session_state.queries_and_responses.append((query, answer))
            st.write(answer)
            query = ''  # Clear the input box

        # Display previous queries and responses in reverse order
        for q, a in reversed(st.session_state.queries_and_responses):
            st.text(f"Q: {q}")
            st.text(f"A: {a}")
            st.write("---")

elif st.session_state['mode'] == 'user':

    if 'retriever' in st.session_state:
        # QA System
        qa = RetrievalQA.from_chain_type(llm=OpenAI(), chain_type="stuff", retriever=st.session_state.retriever)

        # Query Input
        query = st.text_input("Enter your query here", key="new_query")

        if query:
            response = qa({"query": query}, return_only_outputs=False)
            answer = response['result']
            st.session_state.queries_and_responsesuser.append((query, answer))
            st.write(answer)
            query = ''  # Clear the input box

        # Display previous queries and responses in reverse order
        for q, a in reversed(st.session_state.queries_and_responsesuser):
            st.text(f"Q: {q}")
            st.text(f"A: {a}")
            st.write("---")

