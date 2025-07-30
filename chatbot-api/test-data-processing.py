# test_data_processing.py

from src.data_processing import extract_text_from_pdf, chunk_text

def run_test():
    """
    A simple function to test the data processing logic.
    """
    print("--- Running Data Processing Test ---")
    try:
        # 1. Test PDF extraction
        book_text = extract_text_from_pdf()
        
        if not book_text:
            print("🔥 Test Failed: No text was extracted from the PDF.")
            return

        # 2. Test text chunking
        chunks = chunk_text(book_text)
        
        if not chunks:
            print("🔥 Test Failed: The text was not split into chunks.")
            return

        print("\n--- Sample of the first chunk: ---")
        print(chunks[0])
        print("------------------------------------")
        print("\n🎉 Test Passed: Data processing module works as expected!")

    except Exception as e:
        print(f"\n🔥 Test Failed: An error occurred: {e}")

if __name__ == "__main__":
    run_test()