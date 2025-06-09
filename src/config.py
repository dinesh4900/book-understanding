# src/config.py

import os

# --- PATHS ---
# Use os.path.join for cross-platform compatibility
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(ROOT_DIR, "data")
PDF_FILE_PATH = os.path.join(DATA_PATH, "12-rules-for-life.pdf") # Make sure your book is here

# --- WEAVIATE ---
COLLECTION_NAME = "BookEnterprise" # Using a new name for the new structure

# --- OLLAMA ---
OLLAMA_EMBEDDING_MODEL = "nomic-embed-text"
OLLAMA_LLM = "llama3.2:latest"

# --- DATA PROCESSING ---
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 150
TOP_K = 5