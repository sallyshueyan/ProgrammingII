def main():
    name_to_age = {"barbara": 18, "jim": 17, "don": 20, "evelyn": 25, "cat": 19}
    name_to_age2 = {"yuki": 23, "fisal": 21, "don": 25, "wee": 20}
    for name in name_to_age:
        print(name)

    for age in name_to_age.values():
        print(age)

    for name, age in name_to_age.items():
        print(f"{name} is {age} next year.")

    for name, age in name_to_age.items():
        print(f"{name} is {age + 1} next year.")
    print()

    for name in sorted(name_to_age.keys()):
        print(f"{name.title()} is {name_to_age[name] + 1} next year.")
    print()

    print(f"Before update: length of dictionary: {len(name_to_age)}")

    name_to_age.update(name_to_age2)
    print(f"After update: length of dictionary:{len(name_to_age)}")
    print(name_to_age)


main()
