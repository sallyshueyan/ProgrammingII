# version 1
character = input("Enter a character: ")
character_code = ord(character)
print(f"The ASCII code for {character} is {character_code}")

number_code = int(input(f"Enter a number between 33 and 127: "))
number_in_letter = chr(number_code)
print(f"The character for {number_code} is {number_in_letter}")


# version 2

def main():
    LOWER = 33
    UPPER = 127

    alphabet = input("Enter a character: ")
    ascii_code_converter = ord(alphabet)
    print(f"The ASCII code for {alphabet} is {ascii_code_converter}")

    ascii_code = int(input(f"Enter a number: "))

    while not LOWER < ascii_code < UPPER:
        print(f"Number must be between {LOWER} and {UPPER}.")
        ascii_code = int(input(f"Enter a number: "))

        string = chr(ascii_code)
        print(f"The character for {ascii_code} is {string}")


main()


# version 3
def main():
    LOWER = 33
    UPPER = 127

    for i in range(LOWER, UPPER + 1):
        print(f"{i:>3} - {chr(i) : <3} ")


main()

# version 4
columns = int(input("Please Enter the total Number of Columns  : "))
for i in range(1, columns + 1):
    for j in range(1, columns + 1):
        print('1', end='  ')
    print()