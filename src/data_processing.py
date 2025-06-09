# src/data_processing.py

import os
import fitz  # PyMuPDF
from langchain_text_splitters import RecursiveCharacterTextSplitter
from . import config

def extract_pages_from_pdf() -> list[dict]:
    """
    Extracts text content along with metadata (page number) from each page of the PDF.
    Returns a list of dictionaries, where each dictionary represents a page.
    """
    pdf_path = config.PDF_FILE_PATH
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"Error: The file '{pdf_path}' was not found.")
    
    print(f"📚 Extracting pages from '{os.path.basename(pdf_path)}'...")
    doc = fitz.open(pdf_path)
    
    pages_with_metadata = []
    for i, page in enumerate(doc):
        page_data = {
            "page_number": i + 1,
            "text": page.get_text()
        }
        pages_with_metadata.append(page_data)
        
    doc.close()
    print(f"✅ Extracted {len(pages_with_metadata)} pages.")
    return pages_with_metadata

def chunk_pages(pages: list[dict]) -> list[dict]:
    """
    Splits the text from each page into smaller chunks, preserving the metadata.
    This is the key function that creates the dictionary structure.
    """
    print(f"--- Chunking text from pages...")
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=config.CHUNK_SIZE,
        chunk_overlap=config.CHUNK_OVERLAP,
        length_function=len,
    )
    
    all_chunks = []
    for page in pages:
        page_text = page['text']
        page_number = page['page_number']
        
        chunks_of_text = text_splitter.split_text(page_text)
        
        # This loop ensures each chunk is a dictionary with 'text' and 'source'
        for chunk_text in chunks_of_text:
            all_chunks.append({
                "text": chunk_text,
                "source": f"Page {page_number}"
            })
            
    print(f"✅ Text chunked into {len(all_chunks)} pieces with metadata.")
    return all_chunks