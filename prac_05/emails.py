def main():
    email_to_name = {}
    user_email = input("Email: ")

    while user_email != "":
        user_name = get_name_from_email(user_email)


def get_name_from_email(user_email):
    prefix = user_email.split('@')[0]
    parts = prefix.split('.')
    name = " ".join(parts).title()
    return name


main()
