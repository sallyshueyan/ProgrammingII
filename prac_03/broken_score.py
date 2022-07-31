def main():
    score = get_score()
    check_score(score)


def check_score(score):
    if score < 0 or score > 100:
        print("Invalid score")
    elif 50 < score <= 90:
        print("Passable")
    elif score > 90:
        print("Excellent")
    else:
        print("Bad")


def get_score():
    score = float(input("Enter score: "))
    return score


main()