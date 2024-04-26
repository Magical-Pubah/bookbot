def main():
    book_path = "books/frankenstein.txt"
    story = get_book_test(book_path)
    lett_count = letter_count(story)
    organized_list = organize(lett_count)

    print(f"--- Begin report of {book_path} ---")
    print(f"There are {word_count(story)} words in this book.")
    print()
    for letter in organized_list:
        print(f"The '{letter["character"]}' character was found {letter["number"]} times.")
    print()
    print("--- End report ---")

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

def sort_on(dict):
    return dict["number"]

def organize(dict):
    alpha_list = []
    for letter in dict:
        alpha_list.append({"character": letter, "number": dict[letter]})
    alpha_list.sort(reverse=True, key=sort_on)
    return alpha_list

main()