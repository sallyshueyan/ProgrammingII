def main():
    quote = "If you are going to be a great investor you have to fit the style to who you are"
    words = quote.lower().split()
    print(len(words))

    unique_words = set(words)
    print("Number of unique words:", len(unique_words))
    print(unique_words)


main()
