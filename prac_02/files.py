# version 1
FILENAME = "name.txt"

name = input("Enter name: ")
out_file = open(FILENAME, 'w')
print("{}".format(name), file=out_file)

out_file.close()

# version 2
FILENAME = "name.txt"

name = input("Enter name: ")
out_file = open(FILENAME, 'w')
print("Your name is {}".format(name), file=out_file)

out_file.close()

# version 3

FILENAME = "numbers.txt"

out_file = open(FILENAME, 'r')
first_number = out_file.readline()
second_number = out_file.readline()
first_two_numbers = first_number + second_number
print(first_two_numbers)

sum_two_numbers = int(first_number) + int(second_number)
print(sum_two_numbers)

# version 4
FILENAME = "numbers.txt"

in_file = open(FILENAME, 'r')
lines = in_file.readlines()
print(lines)

sum_of_numbers = 0
for line in lines:
    data = line.split('\n')
    numbers = int(data[0])
    sum_of_numbers += numbers

print(sum_of_numbers)



