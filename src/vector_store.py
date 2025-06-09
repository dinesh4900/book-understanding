# src/vector_store.py

import os
import weaviate
import weaviate.classes as wvc
import ollama
from langchain_community.embeddings import OllamaEmbeddings
from . import config

class VectorStore:
    """
    A class to manage all interactions with the Weaviate vector store.
    """
    def __init__(self):
        """
        The constructor for the VectorStore class.
        It automatically handles connecting to Weaviate and checking Ollama.
        """
        self.client = None
        print("--- Initializing VectorStore ---")
        self._connect_to_weaviate()
        self._check_ollama_connection()

    def _connect_to_weaviate(self):
        # This method is perfect as is. No changes needed.
        print("--> Attempting to connect to Weaviate...")
        wcs_url = os.getenv("WEAVIATE_URL")
        wcs_api_key = os.getenv("WEAVIATE_API_KEY")

        if not wcs_url or not wcs_api_key:
            raise ValueError("WEAVIATE_URL and WEAVIATE_API_KEY must be set in your .env file")

        try:
            client = weaviate.connect_to_weaviate_cloud(
                cluster_url=wcs_url,
                auth_credentials=weaviate.auth.AuthApiKey(wcs_api_key),
                skip_init_checks=True
            )
            self.client = client
            print("✅ Successfully connected to Weaviate.")
        except Exception as e:
            print(f"❌ FAILED to connect to Weaviate: {e}")
            raise

    def _check_ollama_connection(self):
        # This method is perfect as is. No changes needed.
        print("--> Checking connection to Ollama...")
        try:
            ollama.list()
            print("✅ Successfully connected to Ollama.")
        except Exception:
            print("❌ FAILED to connect to Ollama. Please ensure the Ollama application is running.")
            raise

    def ingest_data(self, chunks: list[dict]):
        """
        Embeds and ingests data chunks with metadata into the Weaviate collection.
        """
        print("\n--- Starting Data Ingestion into Weaviate ---")
        
        # Initialize the embedding model from Ollama
        embeddings = OllamaEmbeddings(model=config.OLLAMA_EMBEDDING_MODEL)
        
        # Get the collection name from our config file
        collection_name = config.COLLECTION_NAME

        # For development, it's good practice to start fresh.
        if self.client.collections.exists(collection_name):
            print(f"- Deleting existing collection '{collection_name}' to ensure a clean slate.")
            self.client.collections.delete(collection_name)

        # Define the structure of our data collection in Weaviate
        print(f"- Creating new collection: '{collection_name}'")
        collection = self.client.collections.create(
            name=collection_name,
            properties=[
                # This property will store the raw text of the chunk
                wvc.config.Property(name="content", data_type=wvc.config.DataType.TEXT),
                # This property will store our metadata (e.g., "Page 54")
                wvc.config.Property(name="source", data_type=wvc.config.DataType.TEXT),
            ],
            # We must tell Weaviate not to use its own vectorizer, since we are providing our own
            vectorizer_config=wvc.config.Configure.Vectorizer.none(),
        )
        
        # Use batching for efficient data insertion
        print("- Preparing to ingest data in batches...")
        with collection.batch.dynamic() as batch:
            for i, chunk in enumerate(chunks):
                print(f"- Processing chunk {i+1}/{len(chunks)} from {chunk['source']}...")
                
                # The data object to be stored, including our metadata
                data_object = {
                    "content": chunk['text'],
                    "source": chunk['source'],
                }
                
                # Generate the vector embedding for the text content
                vector = embeddings.embed_query(chunk['text'])
                
                # Add the complete object (data + vector) to the batch
                batch.add_object(
                    properties=data_object,
                    vector=vector
                )
        
        print("✅ Data ingestion complete!")


    def close(self):
        """Closes the Weaviate client connection if it exists."""
        if self.client:
            self.client.close()
            print("\n✅ Connection to Weaviate closed properly.")