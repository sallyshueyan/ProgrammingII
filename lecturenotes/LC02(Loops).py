
# for loop
for i in range(5):  # 0, 1, 2, 3, 4
    print(i)


# shortcuts
def main():
    score = 68
    grade = ""

    if 80 <= score <= 100:
        grade = "A"
    elif 80 > score >= 50:
        grade = "B"
    elif 65 > score >= 50:
        grade = "C"
    else:
        grade = "F"
    print(f"Your grade is {grade}")


main()


# Independent Function
def main():
    total_cost = 1500
    member_response = input("Are you member? (Y/N) ")
    voucher_response = input("Do you have a voucher? (Y/N) ")

    if member_response == "Y":
        total_cost *= 0.85

    if voucher_response == "Y":
        total_cost *= 0.95

    print(total_cost)


main()

# infinite loop
count = 20

while count >= 10:
    print(10)
    count += 1

# fail to enter the loop
count = 5

while count >= 10:
    print(10)
    count += 1


# range function (1 argument)
def main():
    for i in range(5):  # range(end), start = 0, step = 1
        print(i)  # 0,1,2,3,4 -> excluding the end

    # range function (2 arguments)
    for i in range(3, 10):  # range(start, end) step = 1
        print(i)  # 3,4, 5, 6, 7, 8, 9 -> excluding the end

    for i in range(20, 10, -2):  # range(start, end, step)
        print(f"{i}___", end="")  # 20, 18, 16, 14, 12 -> excluding the end


main()
