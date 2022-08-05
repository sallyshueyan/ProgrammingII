"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    display_data(data)
    print(data)


def display_data(data):
    """Display subject details"""
    for information in data:
        print("{:5} is taught by {:12} and has {:3} students.".format(*information))


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    subject = []  # a list of lists ( a list of subject list)
    input_file = open(FILENAME)
    for line in input_file:
        print(line)  # See what a line looks like
        # print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        # print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        # print(parts)  # See if that worked
        # print("----------")
        subject.append(parts)  # put in the subject into a list of subjects
    input_file.close()
    return subject


main()
