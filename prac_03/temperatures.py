MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def main():
    choice = get_choice()
    while choice != "Q":
        check_choice(choice)
        choice = get_choice()

    if choice == "Q":
        print("Thank you.")


def get_choice():
    """Get input, return input as choice"""
    print(MENU)
    choice = input(">>> ").upper()
    return choice


def check_choice(choice):
    """Check choice, get input for celsius or fahrenheit"""
    if choice == "C":
        celsius = float(input("Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print("Result: {:.2f} F".format(fahrenheit))
    elif choice == "F":
        fahrenheit = float(input("Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print("Result: {:.2f} F".format(celsius))
    else:
        print("Invalid option")


def celsius_to_fahrenheit(celsius):
    """Return calculation of fahrenheit"""
    return celsius * 9.0 / 5 + 32


def fahrenheit_to_celsius(fahrenheit):
    """Return calculation of celsius"""
    return 5 / 9 * (fahrenheit - 32)


main()
