YEAR = 2020
VINTAGE_AGE = 50


class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return "{} CES ({}) : ${}".format(self.name, self.year, self.cost)

    def get_age(self):
        return YEAR - self.year

    def is_vintage(self):
        if self.get_age() >= VINTAGE_AGE:
            return True
        else:
            return False

