def main():
    names, dates_of_birth = load_names_and_birthdays("birthdays.csv")
    name_to_date_of_birth = convert_lists_to_dictionary(names, dates_of_birth)

    print(name_to_date_of_birth)


def load_names_and_birthdays(filename):
    """Return parallel lists of names and birthday tuples."""
    names = []
    dates_of_birth = []

    with open("birthdays.csv", "r") as in_file:
        lines = in_file.readlines()
        for line in lines:
            date = line.split(",")  # data[0] ->name,data[1] -> birthdate in dd/mm/yyyy format
            names.append(date[0])
            birthday = tuple([int(x) for x in date[1].split("/")])  # dd/mm/yyyy ->(dd,mm,yyyy)
            dates_of_birth.append(birthday)

    return names, dates_of_birth


def convert_lists_to_dictionary(keys, values):
    """Return two parallel lists as a dictionary."""
    return dict(zip(keys, values))


if __name__ == '__main__':
    main()