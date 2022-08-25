class ProgrammingLanguage:

    def __init__(self,  name="", dynamic="", reflection="", year=""):
        self.name = name
        self.dynamic = dynamic
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return f"{self.name}, {self.dynamic} Typing, Reflection={self.reflection}, First appeared in {self.year}"

if __name__ == "__main__":

