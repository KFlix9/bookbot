def get_character_count(input):
    count_by_char = {}
    for char in list(input.lower()):
        if char in count_by_char:
            count_by_char[char] += 1
        else:
            count_by_char[char] = 1
    return count_by_char

def get_word_count(input):
    return len(input.split())

def main():
    book_path = "books/frankenstein.txt"
    with open(book_path) as f:
        file_contents = f.read()

    print(f"### Begin of the book report on {book_path} ###\n")
    print(f"{get_word_count(file_contents)} words found in the document\n")
    character_count = get_character_count(file_contents)
    for key in character_count.keys():
        if key.isalpha():
            print(f"the '{key}' was found {character_count[key]} times")
    print(f"\n### End of the book report on {book_path} ###")

if __name__ == "__main__":
    main()