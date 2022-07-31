
def main():
    password = get_password()
    password_length = len(password) # count length of password
    display_asterisks(password_length)


def display_asterisks(password_length):
    for i in range(password_length):
        print("*", end="")


def get_password():
    password = input("Enter password: ")
    return password


main()
