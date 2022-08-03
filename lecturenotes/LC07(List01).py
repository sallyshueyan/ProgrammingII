def main():
    numbers = [11, 23, 15, 18, 20, 5, 8]
    numbers[4] += 100

    # function, returns a copy of reversed sorted sequence
    reversed_numbers = sorted(numbers, reverse=True)
    print(f"Reversed numbers after sorted: {reversed_numbers}")
    print(f"Original numbers after sorted: {numbers}")

    numbers.sort()  # apply to numbers directly
    print(numbers)

    numbers.extend([88, 99, 111])
    print(numbers)

    numbers.insert(1, 10)
    print(numbers)


main()
