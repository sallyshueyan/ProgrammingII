class ProgrammingLanguage:

    def __init__(self, name="", dynamic="", reflection="", year=0):
        """Function define attributes."""
        self.name = name
        self.dynamic = dynamic
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return programming language and details."""
        return f"{self.name}, {self.dynamic} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """Check programming language's dynamic status."""
        return self.dynamic == "Dynamic"

    def __repr__(self):
        return "{}".format(self.name)


if __name__ == "__main__":
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(ruby.__str__())

    languages = [ruby, python, visual_basic]
    print(f"Languages list contain: {[str(language) for language in languages]}")
    print(f"Languages list contain these few languages: {[str(languages)]}")

    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)

