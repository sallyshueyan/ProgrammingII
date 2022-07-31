# a valid age is 0 to 120
def main():
    valid_input = False
    while not valid_input:
        try:
            age = int(input("Age: "))
            if 0 <= age <= 120:
                valid_input = True
            else:
                print("Age must be between 0 and 120.")
        except ValueError:  # or just except:
            print("Invalid (not an integer)")

    print("Next year you will be", age + 1)


main()