from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharaterTextSplitter

def load_pdf(path):
    loader = PyPDFLoader(path)
    docs=loader.load()
    
    splitter= RecursiveCharaterTextSplitter(chunk_size=500,chunk_overlap=50)
    return splitter.split_documents(docs)
