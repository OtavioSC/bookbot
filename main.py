path_to_file = './books/frankenstein.txt'

with open(path_to_file) as f:
    file_contents = f.read()

def count_characters(text):
    dictionary_of_characters = {}
    for word in text:
        dictionary_of_characters[word.lower()] = dictionary_of_characters.get(word.lower(), 0) + 1

    return dictionary_of_characters

def count_words(text):
    words = text.split()
    number_of_words = 0

    for word in words:
        number_of_words += 1

    return number_of_words 

def create_report(dict):
    alphabet = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
    print("--- Begin report of books/frankenstein.txt ---")
    dictionary_of_characters = count_characters(file_contents)
    for character, count in dictionary_of_characters.items():
        if character in alphabet:
            print(f"The '{character}' character was found {count} times")

    print("--- End report ---")
def main():
    # print(file_contents)
    # print(count_words(file_contents))
    print(create_report(file_contents))

main()
