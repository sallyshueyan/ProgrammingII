FILENAME = "content.txt"


def main():
    in_file = open(FILENAME, "r")
    content = in_file.read()  # read everything
    print(repr(f"Everything in file is : {content}"))

    print(content)
    next_line = in_file.readline()
    print(repr(next_line))  # is empty bcuz is at the end of the file

    print("---Using readlines()---")
    in_file.seek(0)  # go back to the start of the file
    for line in in_file.readlines():  # store everything in a list
        print(line)

    in_file.close()

    print("NEXT")
    in_file = open(FILENAME, "r")
    not_strings = in_file.readline()
    print(f"readline(): {not_strings}")

    strings = in_file.readlines()
    print(f"readlines(): {strings}")

    in_file.close()


main()
