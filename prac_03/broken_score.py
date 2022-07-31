import random


def main():
    score = get_score()
    result = check_score(score)
    display_result(result)


def get_score():
    """Get input as score"""
    score = float(input("Enter score: "))
    return score


def check_score(score):
    """Check range of score, return result"""
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
    """Display result of input score"""
    print(f"Your score is {result}")


random_score = random.randint(0, 100)  # generate random score from 0-10
result = check_score(random_score)  # check random score's result
print(f"Random score is {random_score} and is {result}")

main()
