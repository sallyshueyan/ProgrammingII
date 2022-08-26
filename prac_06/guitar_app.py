from guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """Console program for Guitar application."""
    guitars = []
    load_guitars(guitars)
    display_guitars(guitars)


def load_guitars(guitars):
    """Load and create Guitar objects from file."""
    with open(FILENAME, "r") as in_file:
        for line in in_file.readlines():
            data = line.split(",")
            name = data[0].strip()
            year = int(data[1].strip())
            cost = float(data[2].strip())
            new_guitar = Guitar(name, year, cost)
            guitars.append(new_guitar)


def display_guitars(guitars):
    """Display Guitar objects in a nice format."""
    for index, guitar in enumerate(guitars):
        print(f"{index:2}) {guitar}")


main()
