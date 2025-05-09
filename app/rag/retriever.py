from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from ..utils.config import Config

vectorstore = None

def load_vectorstore():
    global vectorstore
    if vectorstore is None:
        embeddings = OpenAIEmbeddings(openai_api_key=Config.OPENAI_API_KEY)
        vectorstore = FAISS.load_local(Config.VECTORSTORE_PATH, embeddings,allow_dangerous_deserialization=True  )
    return vectorstore

def retrieve_context(query, k=3):
    """
    Retrieve relevant context for a query using RAG
    """
    try:
        vectorstore = load_vectorstore()
        docs = vectorstore.similarity_search(query, k=k)
        return "\n".join([doc.page_content for doc in docs])
    except Exception as e:
        raise Exception(f"Context retrieval failed: {str(e)}")