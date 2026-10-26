# Initial balance
balance = 10000
# Transactions stored as tuples
transactions = [
    ("D", 5000),
    ("W", 3000),
    ("W", 12000),
    ("W", 15000),
    ("D", 2000),
    ("X", 1000)
]
deposit_count = 0
withdraw_count = 0
invalid_count = 0
history = []
for trans_type, amount in transactions:  # tuple unpacking
    if trans_type == "D":
        balance += amount
        deposit_count += 1
        history.append(("Deposit", amount))
    elif trans_type == "W":
        if amount > 10000:
            print("Rejected:", amount,
                  "- Withdrawal limit exceeded")
            invalid_count += 1
        elif amount > balance:
            print("Rejected:", amount,
                  "- Insufficient balance")
            invalid_count += 1
        else:
            balance -= amount
            withdraw_count += 1
            history.append(("Withdraw", amount))
    else:
        print("Invalid Transaction Type")
        invalid_count += 1
print("\nTransaction History")
for item in history:
    print(item)
summary = (
    deposit_count,
    withdraw_count,
    invalid_count,
    balance
)
print("\nSummary")
print("Deposits:", summary[0])
print("Withdrawals:", summary[1])
print("Invalid:", summary[2])
print("Final Balance:", summary[3])
