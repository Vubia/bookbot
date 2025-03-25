import sys
from stats import get_num_words, count_characters

def main():
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    # Use the second argument as the book path
    book_path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    
    print("--------- Character Count -------")
    characters = count_characters(text)
    for char, count in characters.items():
        print(f"{char}: {count}")


def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
