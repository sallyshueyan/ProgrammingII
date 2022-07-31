MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def main():
    print(MENU)
    choice = input(">>> ").upper()

    while choice != "Q":
        check_choice(choice)
        print(MENU)
        choice = input(">>> ").upper()

    if choice == "Q":
        print("Thank you.")


def check_choice(choice):
    if choice == "C":
        celsius = float(input("Celsius: "))
        fahrenheit = celsius * 9.0 / 5 + 32
        print("Result: {:.2f} F".format(fahrenheit))
    elif choice == "F":
        fahrenheit = float(input("Fahrenheit: "))
        celsius = 5 / 9 * (fahrenheit - 32)
        print("Result: {:.2f} F".format(celsius))
    else:
        print("Invalid option")


main()
