class ProgrammingLanguage:

    def __init__(self, name="", dynamic="", reflection="", year=0):
        self.name = name
        self.dynamic = dynamic
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return f"{self.name}, {self.dynamic} Typing, Reflection={self.reflection}, First appeared in {self.year}"


if __name__ == "__main__":
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(ruby.__str__())

    languages = [ruby, python, visual_basic]
    print(languages)


