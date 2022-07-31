def main():
    score = get_score()
    grade = check_score(score)
    display_result(grade)


def get_score():
    score = float(input("Enter score: "))
    return score


def check_score(score):
    if score < 0 or score > 100:
        grade = "Invalid score"
    elif 50 < score <= 90:
        grade = "Passable"
    elif score > 90:
        grade = "Excellent"
    else:
        grade = "Bad"
    return grade


def display_result(grade):
    print(f"Your score is {grade}")


main()
