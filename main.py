import sys
from stats import get_num_words, get_letters_dict, letters_dict_to_sorted_list

print(sys.argv)

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents


def main():
    path = sys.argv[1]
    text = get_book_text(path)
    num_words = get_num_words(text)
    letters_dict = get_letters_dict(text)
    letters_sorted_list = letters_dict_to_sorted_list(letters_dict)

    print_report(path, num_words, letters_sorted_list)


def print_report(path, num_words, letters_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for letter in letters_sorted_list:
        print(f"{letter['char']}: {letter['num']}")
    print("============= END ===============")

    


main()



