def main():
    book_path = "books/frankenstein.txt"
    story = get_book_test(book_path)
    print(f"There are {word_count(story)} words in this book.")
    print(letter_count(story))

def get_book_test(path):
    with open(path) as f:
        return f.read()

def word_count(story):
    words = story.split()
    return len(words)

def letter_count(words):
    letters = list(words.lower())
    letter_dict = {}
    for letter in letters:
        if letter in letter_dict:
            pass
        elif letter.isalpha():
            letter_dict.setdefault(letter, letters.count(letter))
        else:
            pass
    return letter_dict


main()