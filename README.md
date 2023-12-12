
# MeDoc Chatbot

## Overview
This custom chatbot application extracts text from PDF files and website URLs, converts this text into vector embeddings, and performs similarity searches based on user queries. It utilizes Python libraries and machine learning models to provide contextual responses and is built with Streamlit for an interactive user interface.

## Key Concepts and Libraries
1. **Streamlit**: For creating web applications.
2. **PDFPlumberLoader**: From `langchain`, extracts text from PDFs.
3. **CharacterTextSplitter & TokenTextSplitter**: From `langchain`, splits texts into chunks.
4. **Chroma**: From `langchain.vectorstores`, creates and manages a vector database.
5. **RetrievalQA**: From `langchain.chains`, performs question-answering.
6. **HuggingFaceEmbeddings & OpenAIEmbeddings**: Converts text into vector embeddings.
7. **BeautifulSoup**: Parses HTML content from web pages.

## Installation Guide
1. Clone the repository from GitHub.
2. Install required libraries:
   ```
   pip install streamlit langchain torch requests beautifulsoup4 pandas pdfplumber
   ```

## Running the Streamlit Application
Run the application with:
```bash
streamlit run app.py
```
Replace `app.py` with the Python file name.

## User Interface
- **Developer Mode**: Upload PDFs and URLs for text extraction.
- **User Mode**: Enter queries for responses based on extracted text context.

## Workflow
1. **Document Extraction**: Processes PDFs and URLs for text.
2. **Text Splitting**: Splits extracted text into chunks.
3. **Vector Embedding**: Converts text chunks into vector embeddings.
4. **Similarity Search & Response Generation**: Searches the vector database for relevant text chunks for query responses.

_Note: This documentation provides an overview and does not include specific code implementations._
