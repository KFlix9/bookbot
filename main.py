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
    print(file_contents)
    print(get_word_count(file_contents))
    some_dict = get_character_count(file_contents)
    print(get_character_count(file_contents))


if __name__ == "__main__":
    main()