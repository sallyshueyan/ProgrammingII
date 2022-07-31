"""
Parse phrases and count letters, words and vowels.

Phrase Parser. Created by Avatar, Jul 2022
"""


import string


def main():
    """Start of program."""
    phrase = "The cow jumped over the elephant."
    number_of_letters = count_letters(phrase)  # phrase is the argument
    print(f"Number of letters: {number_of_letters}")


def count_letters(text):  # text is the parameter
    """Count the number of letters in the text.""" # cannot use 'Counts, Not counted, Counting'
    count = 0
    for character in text.lower():
        if character.lower() in string.ascii_lowercase:
            count += 1
    return count


main()
