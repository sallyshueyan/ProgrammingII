import random

NUMBERS_IN_LINE = 6
MINIMUN_NUMBER = 1
MAXIMUM_NUMBERS = 45


def main():
    '''Request for input and generate the number of rows according to the input'''
    numbers_of_quick_picks = int(input("How many quick picks? "))
    while numbers_of_quick_picks < 0:
        print("Put a valid number.")
        numbers_of_quick_picks = int(input("How many quick picks? "))

    for i in range(numbers_of_quick_picks):
        quick_pick = []
        for j in range(NUMBERS_IN_LINE): # numbers for each line is 6
            number = random.randint(MINIMUN_NUMBER, MAXIMUM_NUMBERS)
            while number in quick_pick:
                number = random.randint(MINIMUN_NUMBER, MAXIMUM_NUMBERS)
            quick_pick.append(number)
        quick_pick.sort()
        print(quick_pick)


main()
