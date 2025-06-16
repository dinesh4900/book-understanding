# Text chunking operations only

from langchain_text_splitters import RecursiveCharacterTextSplitter
from . import config

class TextChunker:
    """Handles text chunking operations."""
    
    def __init__(self, chunk_size: int = None, chunk_overlap: int = None):
        """Initialize text chunker with custom or default settings."""
        self.chunk_size = chunk_size or config.CHUNK_SIZE
        self.chunk_overlap = chunk_overlap or config.CHUNK_OVERLAP
        
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.chunk_size,
            chunk_overlap=self.chunk_overlap,
            length_function=len,
        )
    
    def chunk_pages(self, pages: list[dict]) -> list[dict]:
        """
        Splits the text from each page into smaller chunks, preserving the metadata.
        This is the key function that creates the dictionary structure.
        """
        print(f"--- Chunking text from {len(pages)} pages...")
        
        all_chunks = []
        for page in pages:
            page_text = page['text']
            page_number = page['page_number']
            
            # Skip empty pages
            if not page_text.strip():
                continue
            
            chunks_of_text = self.text_splitter.split_text(page_text)
            
            # Create chunk dictionaries with metadata
            for chunk_text in chunks_of_text:
                if chunk_text.strip():  # Only add non-empty chunks
                    all_chunks.append({
                        "text": chunk_text,
                        "source": f"Page {page_number}"
                    })
                
        print(f"✅ Text chunked into {len(all_chunks)} pieces with metadata.")
        return all_chunks
    
    def chunk_text(self, text: str, source: str = "Unknown") -> list[dict]:
        """Chunk a single text with given source."""
        chunks_of_text = self.text_splitter.split_text(text)
        
        return [
            {"text": chunk, "source": source}
            for chunk in chunks_of_text
            if chunk.strip()
        ]
