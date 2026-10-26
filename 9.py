# Travel Budget
budget = 50000

# Exchange Rates (to INR)
rates = {
    "USD": 83,
    "EUR": 90,
    "JPY": 0.56
}

# Expenses stored as tuples
expenses = [
    ("Hotel", 200, "USD"),
    ("Food", 150, "EUR"),
    ("Transport", 10000, "JPY"),
    ("Shopping", 100, "USD")
]

conversion_fee_rate = 0.02  # 2%

total_spending = 0
largest_category = ""
largest_amount = 0

expense_report = []

for category, amount, currency in expenses:  # tuple unpacking

    converted = amount * rates[currency]

    fee = converted * conversion_fee_rate

    final_cost = converted + fee

    total_spending += final_cost

    expense_report.append(
        [category, currency, amount, round(final_cost, 2)]
    )

    if final_cost > largest_amount:
        largest_amount = final_cost
        largest_category = category

print("Expense Details")
for item in expense_report:
    print(item)

print("\nTotal Spending:", round(total_spending, 2))

if total_spending > budget:
    print("Status: Budget Exceeded")
    print("Exceeded By:",
          round(total_spending - budget, 2))
else:
    print("Status: Within Budget")
    print("Remaining Budget:",
          round(budget - total_spending, 2))

summary = (
    round(total_spending, 2),
    largest_category,
    round(largest_amount, 2)
)

print("\nSummary")
print("Total Spending:", summary[0])
print("Largest Category:", summary[1])
print("Largest Expense:", summary[2])