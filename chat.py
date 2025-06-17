# chat.py

from dotenv import load_dotenv
load_dotenv()

import ollama
from src.vector_store import VectorStore
from src.prompt_manager import create_prompt
from src.greeting_handler import is_greeting, is_simple_greeting, get_greeting_response
from src import config

def main():
    """The main function to run the interactive RAG chat session with greeting support."""
    print("--- Interactive Book Chat Assistant ---")
    print("🤖 Hello! I'm your book assistant. I can greet you and answer questions about the book!")
    
    store = None
    try:
        store = VectorStore()
        
        print("\n✅ Chatbot is ready! Say hello or ask a question about your book. Type 'exit' to quit.")
        print("💡 Try: 'Hello', 'Good morning', 'What is this book about?', etc.")
        
        while True:
            # 1. Get user input
            user_query = input("\nYou: ")
            if user_query.lower() == 'exit':
                print("👋 Goodbye! Thanks for exploring the book with me!")
                break

            # 2. Check if it's a simple greeting first
            if is_simple_greeting(user_query):
                greeting_response = get_greeting_response(user_query)
                print(f"\n🤖 Assistant: {greeting_response}")
                continue
            
            # 3. If message contains greeting but has more content
            if is_greeting(user_query):
                greeting_response = get_greeting_response(user_query)
                print(f"\n🤖 Assistant: {greeting_response}")
                print("Now let me search the book for your question...")

            # 4. Retrieve relevant context from the vector store
            context_chunks = store.query(user_query, config.TOP_K)

            print(f"\nChunks: {context_chunks}")

            # 3. Create a detailed prompt for the LLM
            prompt = create_prompt(user_query, context_chunks)

            # 4. Generate the answer using the generative LLM
            print("\nLLM Assistant: Thinking...")
            response = ollama.chat(
                model=config.OLLAMA_LLM,
                messages=[{'role': 'user', 'content': prompt}]
            )
            
            answer = response['message']['content']
            print(answer)
            
            # Extract and display the sources for verification
            sources = ", ".join(sorted(list(set(chunk['source'] for chunk in context_chunks))))
            if sources:
                print(f"\nSources: {sources}")

    except Exception as e:
        print(f"\n❌ An error occurred: {e}")
    finally:
        # Ensure the VectorStore connection is closed gracefully
        if store:
            store.close()

if __name__ == "__main__":
    main()