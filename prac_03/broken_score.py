import random


def main():
    score = get_score()
    result = check_score(score)
    display_result(result)


def get_score():
    score = float(input("Enter score: "))
    return score


def check_score(score):
    if score < 0 or score > 100:
        result = "Invalid score"
    elif 50 < score <= 90:
        result = "Passable"
    elif score > 90:
        result = "Excellent"
    else:
        result = "Bad"
    return result


def display_result(result):
    print(f"Your score is {result}")


random_number = random.randint(0, 100)
result = check_score(random_number)
print(f"Random score is {random_number} and is {result}")

main()
