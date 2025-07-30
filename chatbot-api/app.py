import os
import weaviate
import ollama
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def main():
    """
    This function will hold the main logic of our application.
    """
    # --- 1. Connect to Weaviate Cloud Services ---
    wcs_url = os.getenv("WEAVIATE_URL")
    wcs_api_key = os.getenv("WEAVIATE_API_KEY")

    if not wcs_url or not wcs_api_key:
        print("🔴 FATAL: Please set the WEAVIATE_URL and WEAVIATE_API_KEY environment variables.")
        print(f"Debug: WEAVIATE_URL = {wcs_url}")
        print(f"Debug: WEAVIATE_API_KEY = {'*' * len(wcs_api_key) if wcs_api_key else None}")
        return None # Return None to indicate failure

    # Add https:// prefix if not present
    if not wcs_url.startswith('https://'):
        wcs_url = f"https://{wcs_url}"
    
    print(f"Attempting to connect to: {wcs_url}")

    try:
        client = weaviate.connect_to_weaviate_cloud(
            cluster_url=wcs_url,
            auth_credentials=weaviate.auth.AuthApiKey(wcs_api_key),
        )
        print("✅ Successfully connected to your Weaviate Cloud instance!")
        
        # Test the connection
        if client.is_ready():
            print("✅ Weaviate client is ready!")
        else:
            print("⚠️ Weaviate client connected but not ready")
            
    except Exception as e:
        print(f"❌ An error occurred while connecting to Weaviate: {e}")
        print(f"❌ Error type: {type(e).__name__}")
        return None

    # --- 2. Verify Connection to Local Ollama Instance ---
    try:
        ollama.list()
        print("✅ Successfully connected to your local Ollama instance!")
    except Exception as e:
        print("❌ Could not connect to Ollama. Please ensure it's running.")
        print(f"❌ Ollama error: {e}")
        # We still return the client here, because the Weaviate connection succeeded
        # But we might want to close it before exiting the program.
        return client

    print("--- Setup complete. Ready for the next step. ---")
    
    # We return the client so we can close it in the finally block
    return client


# --- This is the main execution block ---
if __name__ == "__main__":
    weaviate_client = None
    try:
        # Run the main function and get the client object
        weaviate_client = main()

        #
        # LATER, ALL OUR CHATBOT LOGIC WILL GO HERE
        # For now, we just connect and then disconnect.
        #
    
    finally:
        # This block of code will RUN NO MATTER WHAT.
        # It runs if the 'try' block succeeds, or if it fails.
        # This GUARANTEES we close the connection.
        if weaviate_client:
            weaviate_client.close()
            print("\n✅ Connection to Weaviate closed properly.")