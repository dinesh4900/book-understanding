# Handles document search and retrieval

from .connections import WeaviateConnection, OllamaConnection
from .collection_manager import CollectionManager
from .embedding_service import EmbeddingService
from . import config

class DocumentSearch:
    """Handles document search and retrieval."""
    
    def __init__(self):
        self.weaviate_conn = WeaviateConnection()
        self.collection_manager = CollectionManager(self.weaviate_conn)
        self.embedding_service = EmbeddingService()
        
        # Check Ollama connection
        OllamaConnection.check_connection()
    
    def search(self, query_text: str, top_k: int = None) -> list[dict]:
        """Search for relevant document chunks."""
        if top_k is None:
            top_k = config.TOP_K
            
        print(f"\n🔎 Searching for context relevant to: '{query_text}'...")
        
        # Generate query embedding
        query_vector = self.embedding_service.embed_text(query_text)
        
        # Get collection
        collection = self.collection_manager.get_collection()
        
        # Perform vector search
        response = collection.query.near_vector(
            near_vector=query_vector,
            limit=top_k,
            return_properties=["content", "source"]
        )
        
        retrieved_chunks = [item.properties for item in response.objects]
        print(f"✅ Found {len(retrieved_chunks)} relevant chunks.")
        
        return retrieved_chunks
    
    def close(self):
        """Close connections."""
        self.weaviate_conn.close()
