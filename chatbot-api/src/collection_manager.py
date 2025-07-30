# Manages Weaviate collections and schemas

import weaviate.classes as wvc
from .connections import WeaviateConnection
from . import config

class CollectionManager:
    """Manages Weaviate collections and schemas."""
    
    def __init__(self, weaviate_connection: WeaviateConnection):
        self.client = weaviate_connection.client
        self.collection_name = config.COLLECTION_NAME
    
    def create_collection(self):
        """Create the document collection with proper schema."""
        # Delete existing collection for fresh start
        if self.client.collections.exists(self.collection_name):
            print(f"- Deleting existing collection '{self.collection_name}' to ensure a clean slate.")
            self.client.collections.delete(self.collection_name)

        # Create new collection
        print(f"- Creating new collection: '{self.collection_name}'")
        collection = self.client.collections.create(
            name=self.collection_name,
            properties=[
                wvc.config.Property(name="content", data_type=wvc.config.DataType.TEXT),
                wvc.config.Property(name="source", data_type=wvc.config.DataType.TEXT),
            ],
            vectorizer_config=wvc.config.Configure.Vectorizer.none(),
        )
        return collection
    
    def get_collection(self):
        """Get existing collection."""
        return self.client.collections.get(self.collection_name)
    
    def collection_exists(self) -> bool:
        """Check if collection exists."""
        return self.client.collections.exists(self.collection_name)
