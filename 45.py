# Appliance Names
appliances = ["Fan", "AC", "Fridge", "Washing Machine"]

# Weekly Consumption Matrix (7 Days)
readings = [
    [1, 2, 1, 2, 1, 2, 1],
    [8, 7, 9, 8, 9, 10, 8],
    [3, 3, 3, 3, 3, 3, 3],
    [2, 1, 2, 1, 2, 1, 2]
]

appliance_limit = 40
daily_limit = 15

appliance_totals = []
daily_totals = [0] * 7

highest_appliance = ""
highest_consumption = 0

print("APPLIANCE TOTALS")

for appliance, week_data in zip(appliances, readings):

    total = sum(week_data)
    appliance_totals.append(total)

    print(appliance, "=", total, "units")

    if total > appliance_limit:
        print("  Limit Exceeded!")

    if total > highest_consumption:
        highest_consumption = total
        highest_appliance = appliance

# Daily Totals
print("\nDAILY TOTALS")

for day in range(7):

    total = 0

    for appliance in readings:
        total += appliance[day]

    daily_totals[day] = total

    print("Day", day + 1, "=", total, "units")

    if total > daily_limit:
        print("  Daily Limit Exceeded!")

# Tuple Summary
summary = (
    highest_appliance,
    highest_consumption,
    sum(appliance_totals)
)

# Tuple Unpacking
name, consumption, overall = summary

print("\nSUMMARY")
print("Highest Appliance :", name)
print("Consumption       :", consumption, "units")
print("Overall Usage     :", overall, "units")