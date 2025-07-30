# Handles Weaviate & Ollama Connections

import os
import weaviate
import ollama
from . import config

class WeaviateConnection:
    """Handles Weaviate connection management."""
    
    def __init__(self):
        self.client = None
        self._connect()
    
    def _connect(self):
        """Connect to Weaviate Cloud Services."""
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
    
    def close(self):
        """Close the Weaviate client connection."""
        if self.client:
            self.client.close()
            print("✅ Connection to Weaviate closed properly.")

class OllamaConnection:
    """Handles Ollama connection verification."""
    
    @staticmethod
    def check_connection():
        """Check if Ollama is running and accessible."""
        print("--> Checking connection to Ollama...")
        try:
            ollama.list()
            print("✅ Successfully connected to Ollama.")
            return True
        except Exception:
            print("❌ FAILED to connect to Ollama. Please ensure the Ollama application is running.")
            raise
