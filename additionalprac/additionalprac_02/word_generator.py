"""
CP1404/CP5632 - Practical
Random word generator - based on format of words

Another way to get just consonants would be to use string.ascii_lowercase
(all letters) and remove the vowels.
"""
import random

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"
LIST = [VOWELS,CONSONANTS, SPECIAL_CHARACTERS]

word_format = input("Enter a word format or Enter (R): ").lower()
freestyle = random.choice(LIST)

word = ""
for kind in word_format:
    if kind == "c":
        word += random.choice(CONSONANTS)
    elif kind in SPECIAL_CHARACTERS:
        word += random.choice(SPECIAL_CHARACTERS)
    elif kind == "r":
        word = freestyle
    else:
        word += random.choice(VOWELS)

print(word)
