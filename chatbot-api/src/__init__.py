"""
Book Understanding Application - Core package initialization
"""

__version__ = "1.0.0"

# Essential imports for main application
try:
    from . import config
except ImportError:
    config = None

# Data processing functions
try:
    from .data_processing import extract_pages_from_pdf, chunk_pages
except ImportError:
    extract_pages_from_pdf = None
    chunk_pages = None

# Vector store for RAG functionality
try:
    from .vector_store import VectorStore
except ImportError:
    VectorStore = None

# Prompt management
try:
    from .prompt_manager import create_prompt
except ImportError:
    create_prompt = None

# Response formatting
try:
    from .response_formatter import ResponseFormatter
except ImportError:
    ResponseFormatter = None

__all__ = [
    "__version__",
    "config",
    "extract_pages_from_pdf",
    "chunk_pages", 
    "VectorStore",
    "create_prompt",
    "ResponseFormatter",
]
