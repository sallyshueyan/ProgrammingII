
def main():
    password = get_password()
    password_length = len(password) # count length of password
    display_asterisks(password_length)


def display_asterisks(password_length):
    """Function display asterisks based on length of password"""
    for i in range(password_length):
        print("*", end="")


def get_password():
    """Function request for password as input"""
    password = input("Enter password: ")
    return password


main()
