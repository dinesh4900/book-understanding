# Handles document ingestion workflow

from .connections import WeaviateConnection, OllamaConnection
from .collection_manager import CollectionManager
from .embedding_service import EmbeddingService

class DocumentIngestion:
    """Handles document ingestion into the vector store."""
    
    def __init__(self):
        self.weaviate_conn = WeaviateConnection()
        self.collection_manager = CollectionManager(self.weaviate_conn)
        self.embedding_service = EmbeddingService()
        
        # Check Ollama connection
        OllamaConnection.check_connection()
    
    def ingest_chunks(self, chunks: list[dict]):
        """Ingest document chunks into Weaviate."""
        print("\n--- Starting Data Ingestion into Weaviate ---")
        
        # Create collection
        collection = self.collection_manager.create_collection()
        
        # Batch insert chunks
        print("- Preparing to ingest data in batches...")
        with collection.batch.dynamic() as batch:
            for i, chunk in enumerate(chunks):
                print(f"- Processing chunk {i+1}/{len(chunks)} from {chunk['source']}...")
                
                # Prepare data object
                data_object = {
                    "content": chunk['text'],
                    "source": chunk['source'],
                }
                
                # Generate embedding
                vector = self.embedding_service.embed_text(chunk['text'])
                
                # Add to batch
                batch.add_object(
                    properties=data_object,
                    vector=vector
                )
        
        print("✅ Data ingestion complete!")
    
    def close(self):
        """Close connections."""
        self.weaviate_conn.close()
