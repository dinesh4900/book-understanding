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

**CRITICAL INSTRUCTIONS:**
1.  You MUST base your answer exclusively on the context provided below. Do not use any outside knowledge.
2.  Analyze ALL context snippets provided. The answer may require combining information from multiple snippets.
3.  Provide a detailed, multi-sentence answer. Do not give one-line or overly brief responses. Elaborate on your answer.
4.  If, and only if, the information is not present across all the provided context snippets, you must respond with exactly this phrase: "Based on the provided excerpts from the book, I cannot find the information to answer this question."

**CONTEXT FROM THE BOOK:**
---
{context_str}
---

**USER'S QUESTION:**
{query}

**YOUR EXPERT ANSWER:**
"""
    return prompt_template