import random


def main():
    numbers_of_quick_picks = int(input("How many quick picks? "))
    for i in range(numbers_of_quick_picks):
        quick_pick = []
        for j in range(6):
            number = random.randint(1, 45)
            quick_pick.append(number)
        print(quick_pick)


main()
