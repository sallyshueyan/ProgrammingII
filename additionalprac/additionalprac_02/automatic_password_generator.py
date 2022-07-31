"""
CP1404/CP5632 - Practical
Random word generator - based on format of words

Another way to get just consonants would be to use string.ascii_lowercase
(all letters) and remove the vowels.
"""
import random

ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"
NUMERIC = "1234567890"


def main():
    password_length = int(input("Enter your length choice: "))

    upper = input("Upper? (Y/N): ").lower()
    lower = input("Lower? (Y/N): ").lower()
    number = input("Numeric? (Y/N): ").lower()
    special_character = input("Special character? (Y/N): ").lower()

    password = ''
    for i in range(password_length):
        if upper == 'y':
            password += random.choice(ALPHABETS.upper())
            valid_length()
        if lower == 'y':
            password += random.choice(ALPHABETS.lower())
            valid_length()
        if number == 'y':
            password += random.choice(NUMERIC)
            valid_length()
        if special_character == 'y':
            password += random.choice(SPECIAL_CHARACTERS)
            valid_length()
    print(password)


def valid_length(password, password_length):
    if len(password) == password_length:
        return "Okay"

main()
