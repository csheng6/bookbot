import sys

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n\n")
    char_count = get_char_count(text)
    get_report(char_count)
    print("--- End report ---")

def get_num_words(text) -> int:
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_char_count(text) -> dict:
    count = {}
    text = text.lower()
    words = text.split()
    for word in words:
        for char in word:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
    return count

def get_report(count):
    char_count = []
    for key, value in count.items():
        if key.isalpha():
            letter_count = (key, value)
            char_count.append(letter_count)
    char_count.sort(key=lambda tup: tup[1], reverse=True)
    for x in char_count:
        print(f"The {x[0]} character was found {x[1]} times")

if __name__ == '__main__':
    sys.exit(main())