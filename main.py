def main():
    book_path = "books/frankenstein.txt"
    story = get_book_test(book_path)
    print(word_count(story))

def get_book_test(path):
    with open(path) as f:
        return f.read()

def word_count(story):
    words = story.split()
    return len(words)



main()