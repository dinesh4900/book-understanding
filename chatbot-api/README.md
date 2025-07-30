# Chatbot API

This folder contains the backend API for the book understanding chatbot.

## Structure

- `src/` - Source code modules
  - `config.py` - Configuration settings (TOP_K=7 for at least 7 contexts)
  - `vector_store.py` - Vector database operations
  - `greeting_handler.py` - Greeting detection and responses
  - `prompt_manager.py` - Prompt creation and management
  - `pdf_extractor.py` - PDF text extraction
  - `text_chunker.py` - Text chunking for embeddings
  - `embedding_service.py` - Text embedding generation
  - Other modules for various functionality

- `data/` - Data files
  - `12-rules-for-life.pdf` - The book being analyzed

- Root files:
  - `chat.py` - Interactive chat interface
  - `ingest.py` - Data ingestion script
  - `app.py` - Main application entry point
  - `requirements.txt` - Python dependencies

## Usage

```bash
cd chatbot-api
python chat.py
```

## Configuration

The chatbot is configured to use at least 7 context chunks (TOP_K=7) when answering questions from the book.
