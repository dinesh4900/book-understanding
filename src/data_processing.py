# src/data_processing.py

from .pdf_extractor import PDFExtractor
from .text_chunker import TextChunker

# Convenience functions that maintain backward compatibility
def extract_pages_from_pdf() -> list[dict]:
    """
    Extracts text content along with metadata (page number) from each page of the PDF.
    Returns a list of dictionaries, where each dictionary represents a page.
    """
    return PDFExtractor.extract_pages()

def chunk_pages(pages: list[dict]) -> list[dict]:
    """
    Splits the text from each page into smaller chunks, preserving the metadata.
    This is the key function that creates the dictionary structure.
    """
    chunker = TextChunker()
    return chunker.chunk_pages(pages)