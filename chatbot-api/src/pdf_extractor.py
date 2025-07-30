# PDF text extraction only

import os
import fitz  # PyMuPDF
from . import config

class PDFExtractor:
    """Handles PDF text extraction operations."""
    
    @staticmethod
    def extract_pages(pdf_path: str = None) -> list[dict]:
        """
        Extracts text content along with metadata (page number) from each page of the PDF.
        Returns a list of dictionaries, where each dictionary represents a page.
        """
        if pdf_path is None:
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
