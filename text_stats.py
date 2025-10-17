import string

text = "Cats and dogs are fun, but cats are definitely funnier than dogs."

def main():
    lower_text = text.lower()
    clean_text = ""
    for char in lower_text:
        if char not in string.punctuation: 
            clean_text += char
    words = clean_text.split(" ")
    print("clean_text:", clean_text)
    print("Words list:", words)
def get_unique_word_count(words):
    unique_words = set(words)
    return len(unique_words)
# def get_unique_word_count(words):
#     longest = max(words, key=len)
#     return longest 


if __name__ == "__main__":
    main()

