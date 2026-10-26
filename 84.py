# Monitoring Stations
stations = ["Station A", "Station B", "Station C"]

# Air Quality Readings
readings = [
    [45, 50, 55, 48, 52],
    [80, 85, 90, 82, 88],
    [120, 125, 118, 122, 130]
]

report = []

highest_value = float('-inf')
lowest_value = float('inf')

print("ENVIRONMENTAL REPORT")
print("-" * 40)

for station, data in zip(stations, readings):   # tuple unpacking

    average = sum(data) / len(data)
    maximum = max(data)
    minimum = min(data)

    highest_value = max(highest_value, maximum)
    lowest_value = min(lowest_value, minimum)

    # Classification
    if average <= 50:
        category = "Good"
    elif average <= 100:
        category = "Moderate"
    else:
        category = "Poor"

    report.append(
        (station, round(average, 2),
         maximum, minimum, category)
    )

    print(f"\n{station}")
    print("Average :", round(average, 2))
    print("Maximum :", maximum)
    print("Minimum :", minimum)
    print("Status  :", category)

# Create Summary Tuple
summary = (
    highest_value,
    lowest_value,
    len(stations)
)

# Tuple Unpacking
highest, lowest, total_stations = summary

print("\nSUMMARY")
print("Highest Reading :", highest)
print("Lowest Reading  :", lowest)
print("Stations Analyzed :", total_stations)