class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "{} ({})".format(self.name, self.age)

    def __repr__(self):
        return "{} ({})".format(self.name, self.age)


p1 = Person("Jane", 19)
print(f"p1: {p1}")
people = [Person("Alexa", 21), Person("Siri", 25)]
print(f"people: {people}")  # without line 9-10 is wrong
print([str(person) for person in people])
