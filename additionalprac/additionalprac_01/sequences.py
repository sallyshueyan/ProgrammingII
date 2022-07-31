x = int(input("Enter an even number to start: ")) # start point
y = int(input("Enter an even number to end: ")) # end point


if x % 2 == 1:
    x = x + 1

for i in range(x, y, 2):
    print(i, end=' ')
print()

for i in range(x + 1, y, 2):
    print(i, end=' ')
print()

for i in range(x, y):
    print(i**2, end=' ')
print()

print("Thank you.")
