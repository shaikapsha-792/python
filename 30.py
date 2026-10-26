# Student Records
records = [
    ("john123@college.edu", "CSE-2025-101"),
    ("mary@college", "ECE2025-102"),
    ("alex@@college.edu", "IT-202-103"),
    ("sara.college.edu", "MECH-2025-104"),
    ("rohit@college.edu", "EEE-2025-105")
]

valid_records = []
errors = []

for email, reg_id in records:  # tuple unpacking
    email_valid = True
    reg_valid = True

    # ------------------
    # Email Validation
    # ------------------
    if email.count("@") != 1:
        email_valid = False
        errors.append([email, "Malformed separator '@'"])

    elif "." not in email.split("@")[1]:
        email_valid = False
        errors.append([email, "Missing domain extension"])

    else:
        username, domain = email.split("@")

        if username == "":
            email_valid = False
            errors.append([email, "Missing username"])

    # ------------------
    # Registration ID Validation
    # ------------------
    parts = reg_id.split("-")

    if len(parts) != 3:
        reg_valid = False
        errors.append([reg_id, "Malformed separator '-'"])

    else:
        dept, year, roll = parts

        if not dept.isalpha():
            reg_valid = False
            errors.append([reg_id, "Invalid department code"])

        if not (year.isdigit() and len(year) == 4):
            reg_valid = False
            errors.append([reg_id, "Invalid year group"])

        if not (roll.isdigit() and len(roll) == 3):
            reg_valid = False
            errors.append([reg_id, "Invalid roll number"])

    # ------------------
    # Store Valid Records
    # ------------------
    if email_valid and reg_valid:
        valid_records.append((email, reg_id))

# ------------------
# Summary
# ------------------
summary = (
    len(records),
    len(valid_records),
    len(errors)
)

# ------------------
# Output
# ------------------
print("VALID RECORDS")
for item in valid_records:
    print(item)

print("\nERROR REPORT")
for error in errors:
    print(error)

print("\nSUMMARY")
print("Total Records :", summary[0])
print("Valid Records :", summary[1])
print("Errors Found  :", summary[2])