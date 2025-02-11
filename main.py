def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    text = count_char(text)
    sort_for_report(text)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def num_words(text):
    i = 0
    for words in text.split():
        i += 1
    print(i)
    return i

def count_char(text):
    char_counts = {}
    for char in text:
        char=char.lower()
        if char not in char_counts:
            char_counts[char]=1
        else:
            char_counts[char]+=1
    return char_counts

def sort_on(dict):
    return dict["num"]

def sort_for_report(dict):
    charlist= []
    for char in dict:
        if char.isalpha():
            charlist.append({"char":char,"num": dict[char]})
            #print(f"added char {char} with {dict[char]} times")
    charlist.sort(reverse=True, key=sort_on)
    for chardict in charlist:
        print(f"The '{chardict["char"]}' character was found {chardict["num"]} times")
    

    

main()
    
