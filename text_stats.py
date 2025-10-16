import string

text = "Cats and dogs are fun, but cats are definitely funnier than dogs!"
lower_text = text.lower()
cleaned_text = ""

def main():
    for char in range(len(lower_text)):
        if lower_text[char] in string.punctuation: 
            cleaned_text += ""
        else:
            cleaned_text += lower_text[char]
words = cleaned_text.split()
print("cleaned_text:", cleaned_text)
print("Words list:", words)

if __name__ == "__main__":
    main()

    kl;kl;k;lk