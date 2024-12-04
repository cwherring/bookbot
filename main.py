def read_book(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def count_words(book):
    words = book.split()
    return len(words)

def count_letters(book):
    letters = set(book)
    letter_count = {}
    for l in letters:
        if l.isalpha():
            letter_count[l] = book.count(l)

    return sorted(letter_count.items(), key=lambda item: item[1], reverse=True)


    return letters

def main():
    path = "books/frankenstein.txt"
    title = "Frankenstein"
    
    book = read_book(path)

    print(f"--- Begin report of the book '{title}' in {path} ---")
    print(f"There are {count_words(book)} words in the book {title}")
    print("")
    for letter in count_letters(book.lower()):
        print(f"The '{letter[0]}' character was found {letter[1]} times")
    print("--- End report ---")
main()