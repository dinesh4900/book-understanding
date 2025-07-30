# test_connections.py

# This must be the first import to load the .env file
from dotenv import load_dotenv
load_dotenv()

from src.vector_store import VectorStore

def run_test():
    """
    A simple function to test the connection logic in our VectorStore class.
    """
    print("--- Running Connection Test ---")
    store = None
    try:
        # This one line will trigger the connection logic in VectorStore's __init__
        store = VectorStore()
        
        # If we get here, it means both connections were successful!
        print("\n🎉 Test Passed: All connections were successful!")

    except Exception as e:
        print(f"\n🔥 Test Failed: An error occurred during initialization: {e}")
    finally:
        # This ensures we always try to close the connection, even if an error occurred.
        if store:
            store.close()

if __name__ == "__main__":
    run_test()