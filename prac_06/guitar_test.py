from prac_06.guitar import Guitar


def main():
    guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    guitar2 = Guitar("Another Guitar", 2013, 0)
    guitar3 = Guitar("50-year old guitar", 1970, 0)
    print(f"{guitar1.name} get_age() - Expected 98. Got {guitar1.get_age()}")
    print(f"{guitar2.name} get_age() - Expected 7. Got {guitar2.get_age()}")
    print(f"{guitar1.name} is_vintage() - Expected True. Got {guitar1.is_vintage()}")
    print(f"{guitar2.name} is_vintage() - Expected False. Got {guitar2.is_vintage()}")
    print(f"{guitar3.name} is_vintage() - Expected True. Got {guitar3.is_vintage()}")


main()
