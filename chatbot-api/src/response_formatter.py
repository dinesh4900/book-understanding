# src/response_formatter.py

class ResponseFormatter:
    """Handles formatting of responses and sources."""
    
    @staticmethod
    def format_sources(context_chunks: list[dict]) -> str:
        """Extract and format sources from context chunks."""
        if not context_chunks:
            return ""
        
        sources = sorted(list(set(chunk['source'] for chunk in context_chunks)))
        return ", ".join(sources)
    
    @staticmethod
    def format_context_preview(context_chunks: list[dict], max_length: int = 200) -> str:
        """Format a preview of the context chunks for debugging."""
        if not context_chunks:
            return "No relevant chunks found."
        
        previews = []
        for i, chunk in enumerate(context_chunks[:3]):  # Show max 3 chunks
            content = chunk.get('content', '')
            source = chunk.get('source', 'Unknown')
            preview = content[:max_length] + "..." if len(content) > max_length else content
            previews.append(f"{i+1}. [{source}]: {preview}")
        
        return "\n".join(previews)
    
    @staticmethod
    def format_response_with_sources(response: str, context_chunks: list[dict]) -> str:
        """Format the final response with sources."""
        sources = ResponseFormatter.format_sources(context_chunks)
        
        if sources:
            return f"{response}\n\nSources: {sources}"
        else:
            return response
