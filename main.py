import string
import text_stats


def main():
    text = "Cats and dogs are fun, but cats are definitely funnier than dogs!"
    lower_text = text.lower()
    cleaned_text = ""
    for char in string.punctuation:
        lower_text = lower_text.replace(char, "")

    words = lower_text.split()
    print("cleaned_text:", lower_text)
    print("Words list:", words)
    print(text_stats.get_unique_word_count(words))


if __name__ == "__main__":
    main()