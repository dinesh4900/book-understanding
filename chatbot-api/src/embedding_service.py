# Manages text embedding operations

from langchain_ollama import OllamaEmbeddings
from . import config

class EmbeddingService:
    """Handles text embedding operations using Ollama."""
    
    def __init__(self):
        self.embeddings = OllamaEmbeddings(model=config.OLLAMA_EMBEDDING_MODEL)
    
    def embed_text(self, text: str) -> list[float]:
        """Generate embedding vector for a single text."""
        return self.embeddings.embed_query(text)
    
    def embed_documents(self, texts: list[str]) -> list[list[float]]:
        """Generate embedding vectors for multiple texts."""
        return self.embeddings.embed_documents(texts)
