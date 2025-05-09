from langchain_community.document_loaders import  PyPDFLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from ..utils.config import Config
from pathlib import Path

def ingest_documents(docs_dir='./docs'):
    """
    Ingest documents from the docs directory and create a vector store
    """
    try:
        loaders = {
            '.pdf': PyPDFLoader,
            '.txt': TextLoader
        }
        
        documents = []
        for filepath in Path(docs_dir).glob("*"):
            ext = filepath.suffix.lower()
            loader_cls = loaders.get(ext)
            if loader_cls:
                doc_loader = loader_cls(str(filepath))
                documents.extend(doc_loader.load())
        
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )
        texts = text_splitter.split_documents(documents)
        
        embeddings = OpenAIEmbeddings(openai_api_key=Config.OPENAI_API_KEY)
        vectorstore = FAISS.from_documents(texts, embeddings)
        
        vectorstore.save_local(Config.VECTORSTORE_PATH)
        
        return True
    except Exception as e:
        raise Exception(f"Document ingestion failed: {str(e)}")