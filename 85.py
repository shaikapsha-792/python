# Courses (Course, Students)
courses = [
    ("Python", 40),
    ("Data Science", 70),
    ("AI", 35),
    ("Cyber Security", 50)
]

# Rooms and Capacities
rooms = {
    "A101": 50,
    "B201": 80,
    "C301": 40
}

# Timetable Allocation
# (Course, Room, Period)
allocations = [
    ("Python", "A101", "P1"),
    ("Data Science", "B201", "P1"),
    ("AI", "C301", "P1"),
    ("Cyber Security", "A101", "P1")
]

clashes = []
capacity_errors = []
scheduled_courses = []
used_slots = []

print("SMART CLASSROOM TIMETABLE REPORT")
print("-" * 45)

for course_name, room, period in allocations:
    scheduled_courses.append(course_name)

    # Find student count
    students = 0
    for course, count in courses:
        if course == course_name:
            students = count
            break

    # Capacity Validation
    if students > rooms[room]:
        capacity_errors.append(
            (course_name, room, students, rooms[room])
        )

    # Clash Detection
    slot = (room, period)

    if slot in used_slots:
        clashes.append(
            (course_name, room, period)
        )
    else:
        used_slots.append(slot)

# Capacity Report
print("\nCAPACITY CHECK")
if capacity_errors:
    for course, room, students, capacity in capacity_errors:
        print(
            f"{course} exceeds capacity "
            f"({students}/{capacity})"
        )
else:
    print("No Capacity Issues")

# Clash Report
print("\nCLASH CHECK")
if clashes:
    for course, room, period in clashes:
        print(
            f"Clash: {course} "
            f"in {room} during {period}"
        )
else:
    print("No Clashes")

# Unscheduled Courses
unscheduled = []

for course, count in courses:
    if course not in scheduled_courses:
        unscheduled.append(course)

print("\nUNSCHEDULED COURSES")
if unscheduled:
    for c in unscheduled:
        print(c)
else:
    print("All Courses Scheduled")

# Summary Tuple
summary = (
    len(courses),
    len(clashes),
)