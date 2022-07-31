def main():
    text = 'ccabb'
    passage = 'abbbcccabd'
    print(text in passage)

    password = 'secRetPasSwORd'
    user_input = input("Enter password:")

    if user_input in password:  # wrong
        print("Access Granted!")
    else:
        print("Access Denied!")


main()


# Version 2
def main():
    password = 'secRetPasSwORd'
    user_input = input("Enter password:")
    if user_input == password:  # correct
        print("Access Granted!")
    else:
        print("Access Denied!")


main()

def main():
    phrase = input("Enter a phrase to find number of vowels: ")

    vowel_count = 0
    for char in phrase:
        if char in "AEIOUaeiou":
            vowel_count += 1

    print(f"The phrase has {vowel_count} vowels.")

main()