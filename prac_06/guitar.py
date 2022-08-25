YEAR = 2020

class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return "{} CES ({}) : ${}".format(self.name, self.year, self.cost)

    def get_age(self):
        return YEAR - self.year


