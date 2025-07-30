# ingest.py

# This must be the first import to ensure environment variables are loaded
# before any other module (like vector_store) tries to access them.
from dotenv import load_dotenv
load_dotenv()

# Import the modules you've built
from src.data_processing import extract_pages_from_pdf, chunk_pages
from src.vector_store import VectorStore

def main():
    """
    The main function that orchestrates the entire data ingestion pipeline.
    This function connects all the pieces you've built.
    """
    print("--- Starting RAG Ingestion Pipeline ---")
    
    store = None
    try:
        # Step 1: Connect to Weaviate and Ollama.
        # Creating a VectorStore instance automatically does this.
        store = VectorStore()
        
        # Step 2: Create the chunks from your PDF.
        print("\n--- Phase 1: Data Processing ---")
        pages = extract_pages_from_pdf()
        chunks = chunk_pages(pages)
        
        # Step 3: Store the chunks in Weaviate.
        # This calls the ingest_data method you just created.
        store.ingest_data(chunks)
        
        print("\n--- Ingestion Pipeline Completed Successfully! ---")
        print("Your knowledge base is now ready to be queried.")

    except Exception as e:
        # This will catch any errors from connecting, processing, or ingesting.
        print(f"\n❌ An error occurred during the ingestion pipeline: {e}")
    
    finally:
        # Step 4: Always ensure the connection is closed.
        if store:
            store.close()

# This standard Python construct makes the script runnable from the command line.
if __name__ == "__main__":
    main()