# Student Names
students = ["Rahul", "Priya", "Arun", "Sneha"]

# Subject Names
subjects = ["Math", "Science", "English"]

# Marks Matrix
marks = [
    [85, 90, 78],
    [92, 88, 95],
    [70, 75, 80],
    [95, 91, 89]
]

threshold = 80

student_report = []

topper = ""
highest_total = 0

print("STUDENT PERFORMANCE REPORT")
print("-" * 40)

# Row-wise Analysis
for student, score_list in zip(students, marks):

    total = sum(score_list)
    average = total / len(score_list)

    student_report.append(
        (student, total, round(average, 2))
    )

    print(
        student,
        "Total =", total,
        "Average =", round(average, 2)
    )

    if total > highest_total:
        highest_total = total
        topper = student

# Column-wise Analysis
subject_averages = []
low_subjects = []

print("\nSUBJECT ANALYSIS")

for col in range(len(subjects)):

    total = 0

    for row in range(len(students)):
        total += marks[row][col]

    avg = total / len(students)

    subject_averages.append(avg)

    print(
        subjects[col],
        "Average =",
        round(avg, 2)
    )

    if avg < threshold:
        low_subjects.append(subjects[col])

# Summary Tuple
summary = (
    topper,
    highest_total,
    len(low_subjects)
)

# Tuple Unpacking
top_student, top_score, low_count = summary

print("\nTOP PERFORMER")
print(top_student, "-", top_score)

print("\nLOW PERFORMING SUBJECTS")

if low_subjects:
    for subject in low_subjects:
        print(subject)
else:
    print("None")

print("\nSUMMARY")
print("Top Student:", top_student)
print("Highest Score:", top_score)
print("Low Subjects:", low_count)