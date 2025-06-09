# src/prompt_manager.py

from . import config

def create_prompt(query: str, context_chunks: list[dict]) -> str:
    """
    Creates a detailed, context-aware prompt for the LLM, including sourced context.
    """
    # Format the retrieved context chunks with their sources for the LLM to see
    context_str = ""
    for i, chunk in enumerate(context_chunks):
        context_str += f"Source ({chunk.get('source', 'N/A')}), Snippet {i+1}:\n"
        context_str += f"\"{chunk.get('content', '')}\"\n\n"

    # The main prompt template that instructs the LLM
    prompt_template = f"""
You are a world-class expert assistant on the book '{config.PDF_FILE_PATH}'.
Your mission is to provide accurate, helpful answers based ONLY on the context provided below.

**CONTEXT FROM THE BOOK:**
---
{context_str}
---

**INSTRUCTIONS:**
1.  Analyze the provided context to answer the user's question.
2.  Your answer must be based *exclusively* on the text in the context above. Do not use any external knowledge.
3.  If the context does not contain the information needed to answer the question, you must state clearly: "Based on the provided context, I cannot answer this question."
4.  After your answer, list the sources you used from the context (e.g., "Sources: Page 87, Page 92").

**USER'S QUESTION:**
{query}

**YOUR EXPERT ANSWER:**
"""
    return prompt_template