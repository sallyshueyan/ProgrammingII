PASSWORD = 10


def main():
    password = input("Enter password: ")
    if len(password) != PASSWORD:
        for i in range(len(password)):
            print("*", end="")


main()
