def main():
    """Start of program."""
    email_to_name = {}
    user_email = input("Email: ")

    while user_email != "":
        user_name = get_name_from_email(user_email)
        name_confirmation = input(f"Is your name {user_name}? (Y/n)").upper()
        if name_confirmation.upper() != "Y" and name_confirmation != "":
            user_name = input("Name: ")
        email_to_name[user_email] = user_name
        user_email = input("Email: ")

    for user_email, user_name in email_to_name.items():
        print(f"{user_name} ({user_email})")


def get_name_from_email(user_email):
    """Organise user name using input."""
    prefix = user_email.split('@')[0]
    parts = prefix.split('.')
    name = " ".join(parts).title()
    return name


main()
