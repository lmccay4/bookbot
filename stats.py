import string

def get_num_words(text):
    words = text.split()
    total = len(words)
    return total

def get_letters_dict(text):
    letter_dict = {}
    lower_text = text.lower()

    for letter in string.ascii_lowercase:
        num = lower_text.count(letter)
        letter_dict[letter] = num

    return letter_dict

def sort_on(d):
    return d["num"]

def letters_dict_to_sorted_list(letter_dict):
    sorted_list = []
    for letter in letter_dict:
        sorted_list.append({"char": letter, "num":letter_dict[letter]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list



