def main():
    name_to_age = {"Bill": 17, "Jane": 34, "Jack": 56, "Sven":13}
    result = {name: age for name, age in name_to_age.items() if age <18}
    print(result)
    print()

    new_result = {}
    for name, age in name_to_age.items():
        if age <18:
            new_result[name] = age

    print(new_result)

main()