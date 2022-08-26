from prac_06.guitar import Guitar

guitars = []


def main():
    """Start of program."""
    print("My guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)
        print(new_guitar, "added.")
        name = input("Name: ")
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    display_guitars()


def display_guitars():
    """Display guitars with details."""
    print("These are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        if guitar.is_vintage():
            vintage = "(vintage)"
            print(f"Guitar{i}: {guitar.name:>21} ({guitar.year:4}), worth ${guitar.cost:>10} {vintage}")
        else:
            print(f"Guitar{i}: {guitar.name:>21} ({guitar.year:4}), worth ${guitar.cost:>10}")


main()
