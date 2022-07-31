FILENAME = 'guitar.txt'
def main():
    in_file = open(FILENAME, 'r')

    lines = in_file.readlines() # read all the lines in guitars.txt (each line as string into a list)
    print(lines) # list of strings

    for line in lines:
        guitar_data = line.split(",")
        name = guitar_data[0]
        year = int(guitar_data[1])  # convert to integer
        price = float(guitar_data[2]) # convert to float
        print(f"Guitar {name} is made in {year} and costs ${price}")

        # after high inflation, each guitar cost 20% more
        print(f"  --> Now Guitar {name} made in {year} is costing ${price * 1.2:.2f}")

    in_file.close()

main()