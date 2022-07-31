def main():

    age = 23
    name = "Michael Jordan"

    # Hi I am Michael Jordan, 23 this yea.
    print("Hi I am", name, ",", age, "this year")
    print("Hi I am" + name + "," + str(age) + "this year")

    print("Hi I am {}, {} this year".format(name, age))
    print(f"Hi I am {name}, {age} this year")

    print(f"Hi, I am {name}, {age} this year and I am going to be {age} every year!")
    print("Hi, I am {0}, {1} this year and I am going to be {1} every year!".format(name, age))


main()