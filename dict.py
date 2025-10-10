student = {
    "name": "Sara",
    "age": 20,
    "courses": ["Math", "Physics"]
}
print("Original dict:", student)

# Access value by key
print("Name:", student["name"])

# Add new key
student["grade"] = "A"
print("After adding grade:", student)

# Change value
student["age"] = 21
print("After changing age:", student)

# Remove a key
del student["courses"]
print("After deleting 'courses':", student)

# Loop through dictionary
print("Loop through keys and values:")
for key, value in student.items():
    print(f" {key} => {value}")


student_scores = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "Diana": 90
}
print("Student scores:", student_scores)

# Access a value
print("Bob's score:", student_scores["Bob"])

# Add a new student
student_scores["Eve"] = 88
print("After adding Eve:", student_scores)

# Change a score
student_scores["Charlie"] = 82
print("After updating Charlie's score:", student_scores)

# Remove a student
del student_scores["Alice"]
print("After deleting Alice:", student_scores)

print("\nChecking performance:")

# Loop through and do if/else checks
for student, score in student_scores.items():
    # conditional logic
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    else:
        grade = "F"
    print(f"{student}: Score = {score}, Grade = {grade}")

print("\nOther operations:")

# Check membership
print("Is 'Bob' in student_scores?", "Bob" in student_scores)
print("Is 95 in scores (values)?", 95 in student_scores.values())

# Get all keys, all values
keys = student_scores.keys()
values = student_scores.values()
print("All students:", list(keys))
print("All scores:", list(values))
