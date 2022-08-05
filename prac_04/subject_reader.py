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
    for subject in subjects:
        print(
            f"{subject[0]} is taught by {subject[1]:12} and has {subject[2]:4} students")


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
