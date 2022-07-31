def main():
    gender = input("M/F? ").upper()

    # while loop
    while not gender in "MF":
        print("Values must be M or F only!")
        gender = input("M/F? ").upper()

    if gender == "M":
        print("Hi Mister!")
    else:
        print("Hi Miss!")

main()