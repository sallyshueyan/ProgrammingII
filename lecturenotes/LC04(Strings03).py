def main():
    text = "Welcome to Python Class"
    print(text.upper())  # applying method to an object (method depending on object)

    another_text = "bye bye!"
    print(another_text.upper()) # object.upper()

    print(len(text))  # function is not dependent; need to pass in things
    print(len([1, 2, 3, 4])) # len(object)


main()


def main():
    text = "Welcome to Python Class"
    print(text.upper()) # Return vakue from text.upper() - Copy of the string in uppercase

    print(text) #The original string is not changes (String are immutable)

    # So what if we really want to store in uppercase?
    text = text.upper()
    print(text)


main()
