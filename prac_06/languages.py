from prac_06.programming_language import ProgrammingLanguage


def main():
    """Start of program."""
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    display_dynamic_programming_language(python, ruby, visual_basic)


def display_dynamic_programming_language(python, ruby, visual_basic):
    """Display dynamically typed languages."""
    languages = [ruby, python, visual_basic]
    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


main()
