from openai import OpenAI
from ..utils.config import Config
from ..rag.retriever import retrieve_context

client = OpenAI(api_key=Config.OPENAI_API_KEY)

def process_text(text, context=None, use_rag=True):
    """
    Process text with LLM, with optional RAG integration.
    
    Args:
        text: Input query
        context: Prefetched context (optional)
        use_rag: Whether to use RAG (default: True)
    """
    try:
        if use_rag and context is None:
            context = retrieve_context(text)
            
        if context:
            prompt = f"Context: {context}\n\nQuestion: {text}\n\nAnswer:"
        else:
            prompt = text
        
        response = client.chat.completions.create(
            model=Config.LLM_MODEL,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
        
        return response.choices[0].message.content
    except Exception as e:
        raise Exception(f"Text processing failed: {str(e)}")