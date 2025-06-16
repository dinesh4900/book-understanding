from .document_ingestion import DocumentIngestion
from .document_search import DocumentSearch

class VectorStore:
    """
    A unified interface to manage all interactions with the Weaviate vector store.
    This class now delegates to specialized services for cleaner separation of concerns.
    """
    def __init__(self):
        """Initialize VectorStore with ingestion and search capabilities."""
        print("--- Initializing VectorStore ---")
        self._ingestion_service = None
        self._search_service = None

    def ingest_data(self, chunks: list[dict]):
        """
        Embeds and ingests data chunks with metadata into the Weaviate collection.
        """
        if not self._ingestion_service:
            self._ingestion_service = DocumentIngestion()
        
        self._ingestion_service.ingest_chunks(chunks)

    def query(self, query_text: str, top_k: int = 1) -> list[dict]:
        """
        Queries the vector store for the most relevant chunks for a given text.
        Returns a list of chunk objects, each containing 'content' and 'source'.
        """
        if not self._search_service:
            self._search_service = DocumentSearch()
        
        return self._search_service.search(query_text, top_k)

    def close(self):
        """Closes all connections."""
        if self._ingestion_service:
            self._ingestion_service.close()
        if self._search_service:
            self._search_service.close()
        print("\n✅ All VectorStore connections closed properly.")