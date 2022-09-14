import csv

def main():
    with open("scores.csv","r") as in_file:
        csv_reader = csv.reader(in_file)
        for row in csv_reader:
            print(row)


    new_student = ["Bulba", "80", "60", "50", "70"]

    with open("scores.csv", "a") as out_file:
        csv_writer = csv.writer(out_file)
        csv_writer.writerow(new_student)

if __name__ == '__main__':
    main()