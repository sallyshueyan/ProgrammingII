FILENAME = "content.txt"


def main():
    in_file = open(FILENAME, "r")
    content = in_file.read()  # read everything
    print(repr(f"Everything in file is : {content}"))

    print(content)
    next_line = in_file.readline()
    print(repr(next_line))  # is empty bcuz is at the end of the file

    in_file.seek(0)  # go back to the start of the file
    header = in_file.readline()  # skip header

    print("Header: ", header)

    first_three_numbers = in_file.read(3)  # read bytes
    print(f"The first 3 numbers are: {first_three_numbers}")
    rest_of_the_line = in_file.read()
    print(f"The rest of the numbers are: {rest_of_the_line}")

    in_file.close()


main()
