"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    subjects = load_subjects()
    print(subjects)
    display_subjects(subjects)

    total_number_of_students = get_total_number_of_students(subjects)
    print(f"Total number of students taking {len(subjects)} subjects = {total_number_of_students}")


def display_subjects(subjects):
    """Display subject code, lecturer and number of students."""
    check_alignment(subjects)
    for subject in subjects:
        print(
            f"{subject[0]} is taught by {subject[1]:{max(check_alignment(subjects))}} and has {subject[2]:4} students")


def check_alignment(subjects):
    """Calculate the length of all subjects' lecturer name."""
    length = []
    for subject in subjects:
        check_length = len(subject[1])
        length.append(check_length)
    return length


def load_subjects():
    """Read data from file formatted like: subject,lecturer,number of students."""
    subjects = []  # a list of lists ( a list of subject list)
    input_file = open(FILENAME)
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        subjects.append(parts)  # put in the subject into a list of subjects
    input_file.close()
    return subjects


def get_total_number_of_students(subjects):
    """Calculate the total number of students in all subjects"""
    total_students = 0
    for subject in subjects:
        total_students += subject[2]
    return total_students


main()
