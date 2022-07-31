password = input("Enter password: ")
count = len(password)

if count != 10:
    for i in range(count):
        print("*", end="")
