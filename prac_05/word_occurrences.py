def main():
    word_to_count = {}
    text = input("Text: ")
    words = text.split()

    for word in words:
        word_to_count[word] = word_to_count.get(word, 0) + 1

    words = list(word_to_count.keys())
    words.sort()



main()
