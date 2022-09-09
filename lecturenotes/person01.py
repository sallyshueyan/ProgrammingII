class Person:
    def __init__(self, name="", gender="", age=0):
        self.name = name
        self.gender = gender
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.gender})"

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age and self.gender == other.gender


if __name__ == '__main__':
    person_one = Person("Simu", "m", 33)
    person_two = Person("Simu", "f", 33)

    print(person_one == person_two)  # one is male another is female
