from datetime import datetime
VINTAGE_AGE = 50


class Guitar:
    def __init__(self, name="", year=0, cost=0):
        """Function define attributes."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Function return guitar details."""
        return "{} CES ({}) : ${}".format(self.name, self.year, self.cost)

    def get_age(self):
        """Calculate age of guitar."""
        today = datetime.today()
        return today.year - self.year

    def is_vintage(self):
        """Check vintage status."""
        if self.get_age() >= VINTAGE_AGE:
            return True
        else:
            return False

        # OR
        # return self.get_age() >= VINTAGE_AGE

