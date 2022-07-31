"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion

display menu
get input of choice
while choice != 'Q'
    if choice == 'C'
        get value of celsius
        calculate conversion of Celsius to Fahrenheit
        display result
    else if choice == 'F'
        get value of fahrenheit
        calculate conversion of Fahrenheit to Celsius
        display result
    else
        display option is invalid
    display menu
    get new input of choice
display finished message

"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()

while choice != "Q":
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
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")
