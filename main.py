def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    character_count_dict = get_character_count(text)
    character_count_single_sorted = character_count_dict_to_sorted_list(character_count_dict)
    # ouput
    print(f"### Begin of the book report on {book_path} ###")
    print(f"{get_word_count(text)} words found in the document")
    print()

    for item in character_count_single_sorted:
        if item['char'].isalpha():
            print(f"the '{item['char']}' was found {item['num']} times")

    print()
    print(f"### End of the book report on {book_path} ###")

def get_text(book_path):
    with open(book_path) as f:
        file_contents = f.read()
    return file_contents


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


def get_character_count(input):
    count_by_char = {}
    for char in list(input.lower()):
        if char in count_by_char:
            count_by_char[char] += 1
        else:
            count_by_char[char] = 1
    return count_by_char


def character_count_dict_to_sorted_list(character_count):
    sorted_list = [] 
    for character in character_count.keys():
        sorted_list.append({"char":character, "num":character_count[character]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list 


def sort_on(d):
    return d["num"]

if __name__ == "__main__":
    main()