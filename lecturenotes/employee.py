from person01 import Person


class Employee(Person):
    def __init__(self, name="", gender="", salary=0):
        # Person.__init__(self, name, gender)
        super().__init__(name, gender)
        self.salary = salary

    def get_salary(self):
        return self.salary

    def __str__(self):
        # return Person.__str__(self) + f"\nSalary: ${self.salary:2f}"
        return super().__str__() + f"\nSalary: ${self.salary:.2f}"
