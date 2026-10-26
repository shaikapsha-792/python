# Route Data
routes = [

    ("Route A", 50,
     [45, 52, 48, 55, 50],
     [60, 65, 58, 62, 61],
     [10, 11, 9, 12, 10]),

    ("Route B", 40,
     [35, 39, 42, 38, 36],
     [55, 57, 56, 54, 58],
     [8, 8, 9, 7, 8]),

    ("Route C", 60,
     [58, 62, 65, 61, 59],
     [70, 68, 72, 69, 71],
     [15, 14, 16, 15, 14])
]

report = []

best_route = ""
best_efficiency = 0

print("BUS ROUTE PERFORMANCE REPORT")
print("-" * 50)

for route_name, capacity, passengers, times, fuel in routes:

    total_passengers = sum(passengers)

    avg_time = sum(times) / len(times)

    total_fuel = sum(fuel)

    efficiency = total_passengers / total_fuel

    overloaded_days = 0

    for count in passengers:

        if count > capacity:
            overloaded_days += 1

    report.append(
        (
            route_name,
            total_passengers,
            round(avg_time, 2),
            total_fuel,
            round(efficiency, 2),
            overloaded_days
        )
    )

    if efficiency > best_efficiency:
        best_efficiency = efficiency
        best_route = route_name

# Display Report
for route in report:

    (
        name,
        passengers_total,
        avg_journey,
        fuel_total,
        efficiency,
        overloads
    ) = route

    print("\nRoute :", name)
    print("Passengers :", passengers_total)
    print("Average Time :", avg_journey)
    print("Fuel Used :", fuel_total)
    print("Efficiency :", efficiency)

    if overloads > 0:
        print("Overloaded Days :", overloads)
    else:
        print("No Overloads")

# Summary Tuple
summary = (
    best_route,
    round(best_efficiency, 2),
    len(routes)
)

# Tuple Unpacking
route, efficiency, total_routes = summary

print("\nSUMMARY")
print("Best Route :", route)
print("Best Efficiency :", efficiency)
print("Routes Analysed :", total_routes)