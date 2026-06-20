# Expense Tracker Program

total = 0  # accumulator variable

print("=== Expense Tracker ===")
print("Enter your expenses one by one.")
print("Type 0 to stop.\n")

while True:
    expense = float(input("Enter expense amount: "))

    if expense == 0:
        break

    total = total + expense  # accumulator logic

print("\nTotal Spent =", total)