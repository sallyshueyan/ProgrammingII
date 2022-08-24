class Student:  # class name must start with a Capital letter
    # file name must be all lowercase followed by _ if necessary

    def __init__(self, first_name="", last_name="", student_id=0):  # constructor - constructs the object
        # initializes the object with appropriate values
        self.first_name = first_name
        self.last_name = last_name
        self.id = student_id
        # self.first_name is an attribute of Student object.
        # first_name is just a parameter.

    def __str__(self):  # overwrite the default implementation that returns the object's address
        return f"{self.first_name}, {self.last_name} -> ({self.id})"


if __name__ == "__main__":
    student1 = Student("Michael", "Jordan", 23)
    print(f"First name: {student1.first_name}, Last name: {student1.last_name}, Student ID: {student1.id}")

    print(student1)
    # OR
    print(student1.__str__())
