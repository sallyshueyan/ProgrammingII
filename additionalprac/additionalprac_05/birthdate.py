def main():
    name_to_date_of_birth = {}

    for i in range(2):
        name = input(f"{i + 1}) Name? ")
        date_of_birth = input("Birthday (dd/mm/yy)? ")  # string
        data_of_birth = tuple([int(x) for x in date_of_birth.split("/")])
        name_to_date_of_birth[name] = date_of_birth

    print(name_to_date_of_birth)


if __name__ == '__main__':
<<<<<<< HEAD
    main()
=======
    main()
>>>>>>> origin/master
