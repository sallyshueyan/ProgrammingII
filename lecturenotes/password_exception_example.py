from custom_password_exception import CustomPasswordException

def main():
    your_password = input("Enter password: ")
    try:
        check_password(your_password)
    except CustomPasswordException as custom_exception:
        print(f"Error! {custom_exception}")
    else:
        print("Good Password!")

def check_password(password):
    if password == "password":
        return True
    else:
        raise CustomPasswordException
if __name__ == '__main__':
    main()