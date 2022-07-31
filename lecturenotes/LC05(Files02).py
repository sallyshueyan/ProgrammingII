FILENAME = "numbers.txt"
OUTPUT_FILENAME = "result.txt"


def main():
    in_file = open(FILENAME, "r")
    first_line = in_file.readline()
    second_line = in_file.readline()
    in_file.close()  # close right after reading

    print(repr(first_line))  # check string or int
    print(repr(second_line))  # check string or int
    print(first_line)
    print(second_line)
    total = int(first_line) + int(second_line)
    print(total)

    out_file = open(OUTPUT_FILENAME, "w")
    print(f"Total = {total}", file=out_file)
    out_file.close()


main()
