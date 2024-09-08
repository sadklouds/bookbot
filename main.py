

def main():
    path_to_book = "books/frankenstein.txt"
    text = read_text(path_to_book)
    count = count_words(text)
    char_dict = char_dictionary(text)
    report(count, char_dict)
    
def read_text(path_to_book):
    with open(path_to_book) as f:
        file_contents = f.read()
        return file_contents

def count_words(text):
    words = text.split()
    count = len(words)
    return count

def char_dictionary(text):
    char_counts = {}
    words = text.lower()
    for char in words:
        if char in char_counts:
            char_counts[char] += 1 
        else:
            char_counts[char] = 1 
    return char_counts

def sort_on(dict):
    return dict["num"]

def report(word_count,char_count):
    dict_list = []
    for char, count in char_count.items():
        if char.isalpha():
            dict_list.append({"char":char, "num":count})

    print("--- Begin report of books/frankenstein.txt ---")      
    print(f"{word_count} words found in the document\n")

    dict_list.sort(reverse=True, key=sort_on)
    for item in dict_list:
        print(f"The '{item["char"]}' was found {item["num"]} times")

main()
    