"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number_of_months."""
    incomes = []
    number_of_months = int(input("How many months? "))

    for month in range(1, number_of_months + 1):
        income = float(input("Enter income for month {}:".format(str(month))))
        incomes.append(income)

    display_report(incomes, number_of_months)


def display_report(incomes, number_of_months):
    """Display report based on the incomes as inputs."""
    print("\nIncome Report\n-------------")
    total = 0
    for index, i in enumerate(incomes, start= 1):
        income = incomes[index - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(index, income, total))


main()