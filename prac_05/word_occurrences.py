def main():
    word_to_count = {}
    text = input("Text: ")
    words = text.split()

    for word in words:
        word_to_count[word] = word_to_count.get(word, 0) + 1

    words = list(word_to_count.keys())
    words.sort()

    def check_alignment():
        """Check alignment."""
        length_of_word = 0
        for word in word_to_count:
            if length_of_word < len(word):
                length_of_word = len(word)
        return length_of_word

    for word in words:
        print(f"{word:{check_alignment()}} : {word_to_count[word]}")


main()
