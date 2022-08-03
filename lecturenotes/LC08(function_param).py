def value_change(param):
    param += 123  # assignment creates another Python object

    print(param)


def my_function(param_list):
    param_list[0] += 777  # mutable change on the array
    print(f"Param list {param_list}")


def my_function2(param_list):
    param_list = [100, 200, 300]  # assignment creates another list object
    print(f"Param list in function 2: {param_list}")


def main():
    arg = 999
    value_change(arg)
    print(arg)

    my_list = [1, 2, 3]
    my_function(my_list)
    print(f"My list: {my_list}")

    my_function2(my_list)
    print(f"My param list after function 2: {my_list}")


main()
