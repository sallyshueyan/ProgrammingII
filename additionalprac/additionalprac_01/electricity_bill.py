# Version 1
print("Electricity bill estimator")
cents_per_kWh = int(input("Enter cents per kWh: "))
daily_use_in_kWh = float(input("Enter daily use in kWh: "))
numbers_of_billing_days = int(input("Enter number of billing days: "))

cents_in_dollars = cents_per_kWh / 100
estimated_bill = cents_in_dollars * daily_use_in_kWh * numbers_of_billing_days
print(f"Estimated bill: ${estimated_bill}")

# Version 2
TARIFF_11 = 0.244618
TARIFF_31 = 0.136928


def main():
    print("Electricity bill estimator 2.0")
    tariff = int(input("Which tariff? 11 or 31:"))

    if tariff == 11:
        price_per_kWh = TARIFF_11

    else:
        price_per_kWh = TARIFF_31

    daily_use_in_kWh = float(input("Enter daily use in kWh: "))
    numbers_of_billing_days = int(input("Enter number of billing days: "))
    estimated_bill = price_per_kWh * daily_use_in_kWh * numbers_of_billing_days
    print(f"Estimated bill: ${estimated_bill:.2f}")


main()
