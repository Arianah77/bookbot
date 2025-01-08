def main():
    book_path = "books/frankenstein.txt"
    
    # Get the word count
    word_count = count_words(book_path)
    
    # Get the character counts
    char_count = count_characters(book_path)
    
    # Print the report
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document\n")
    
    # Sort characters by count in descending order and print the result
    sorted_char_count = sorted(char_count.items(), key=lambda x: x[1], reverse=True)
    
    for char, count in sorted_char_count:
        print(f"The '{char}' character was found {count} times")
    
    print("--- End report ---")

def get_book_text(path):
	with open('books/frankenstein.txt', 'r', encoding='utf-8') as f:
		return f.read()

def count_words(path):
	with open(path, 'r', encoding='utf-8') as f:
		text = f.read()
	
	words = text.split()
	return len(words)

def count_characters(path):
    char_count = {}  # Dictionary to store character counts
    
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # Loop through each character in the text
    for char in text:
        char = char.lower()  # Convert character to lowercase
        if char.isalpha():  # Only count alphabetic characters
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    
    return char_count

main()	
