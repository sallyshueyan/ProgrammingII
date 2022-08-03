def multiply_list(my_list: list, mutiplier: float) -> list:
    new_list = [x * mutiplier for x in my_list]
    return new_list


def main():
    your_list = [1, 3, 5, 19]
    your_new_list = multiply_list(your_list, 2)
    print(your_new_list)


main()
