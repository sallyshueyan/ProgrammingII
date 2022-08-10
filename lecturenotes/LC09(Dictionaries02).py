# Name: Mario
# Age: 34
# Jack - 56
# Bill - 21
# Mario - 34
# Jane - 4
def main():
    name_to_age = {"Bill": 21, "Jane": 4, "Jack": 56}
    name = input("Name? ")
    age = int(input("Age? "))

    name_to_age[name] = age  # add the new pair into the dictionary

    for name, age in name_to_age.items():
        print(f"{name:6} - {age:2}")


main()
